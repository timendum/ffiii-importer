import csv
import json
from datetime import datetime as dt

from ffiii_importer import ffapi
from ffiii_importer.models import TransactionSplitStore, TransactionTypeProperty


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_paypal = config["assets"]["Paypal"]
    expense = config["expenses"]["Generic"]
    return asset_paypal, expense


ASSET_PAYPAL, EXPENSE = _load_config()


def _transform_date(sdate: str) -> dt:
    return dt.strptime(sdate, "%d/%m/%Y").replace(hour=12, minute=0, second=0, microsecond=0)


class PPDialect(csv.Dialect):
    delimiter = ","
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = "\n"
    quoting = csv.QUOTE_MINIMAL


PP_DIALECT = PPDialect()


def process_csv(filename: str) -> str:
    transactions = list[TransactionSplitStore]()
    job_tag = "import-paypal-" + dt.now().isoformat(timespec="minutes")
    with open(filename, newline="", encoding="utf8") as f:
        reader = csv.reader(f, dialect=PP_DIALECT)
        # skip header
        next(reader)
        for row in reader:
            amounts = row[7].split(".")
            if len(amounts) != 2 or len(amounts[1]) != 2:
                amounts = row[7].split(",")
                if len(amounts) != 2:
                    continue
            if amounts[0][0] != "-":
                print("Skipped: " + " ".join(row[3:5]))
                continue
            amounts[0] = amounts[0][1:]
            transactions.append(
                TransactionSplitStore(
                    type=TransactionTypeProperty.WITHDRAWAL,
                    date=_transform_date(row[0]),
                    source_id=ASSET_PAYPAL,
                    destination_id=EXPENSE,
                    amount=float("".join(amounts[0].split(".")) + "." + amounts[1]),
                    description=" - ".join(row[3:5]),
                    currency_code=row[6],
                    tags=[job_tag],
                )
            )

        if not transactions:
            return "No transaction"
        resp = ffapi.send_rich(transactions)
    return resp or f"See {ffapi.get_base_url()}/tags/show/{job_tag}"


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        result = "python " + sys.argv[0] + " filename"
    else:
        result = process_csv(sys.argv[1])
    print(result)
