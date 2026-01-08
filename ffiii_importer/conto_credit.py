import csv
import json
from datetime import datetime as dt

from ffiii_importer import ffapi
from ffiii_importer.models import TransactionSplitStore, TransactionTypeProperty


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_conto = config["assets"]["Credit Agricole"]
    expense = config["expenses"]["Generic"]
    return asset_conto, expense


ASSET_CONTO, EXPENSE = _load_config()


def _transform_date(sdate: str) -> dt:
    return dt.strptime(sdate, "%d/%m/%Y")


class CADialect(csv.Dialect):
    delimiter = ";"
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = "\n"
    quoting = csv.QUOTE_MINIMAL


CA_DIALECT = CADialect()


def process_csv(filename: str):
    transactions = []
    job_tag = "import-cagric-" + dt.now().isoformat(timespec="minutes")
    with open(filename, newline="", encoding="utf8") as f:
        reader = csv.reader(f, dialect=CA_DIALECT)
        # skip header
        next(reader)
        for row in reader:
            amounts = row[4].replace(".", "").split(",")
            amounts[0] = amounts[0].strip().lstrip("'")
            if len(amounts) != 2:
                print("Wrong amount: ", row[4])
                continue
            if amounts[0][0] != "-":
                print(f"Skipped: {row[4]} - {row[3]}")
                continue
            amounts[0] = amounts[0][1:]
            transactions.append(
                TransactionSplitStore(
                    type=TransactionTypeProperty.WITHDRAWAL,
                    source_id=ASSET_CONTO,
                    destination_id=EXPENSE,
                    date=_transform_date(row[1]),
                    description=row[3].strip(),
                    amount=float("".join(amounts[0].split(".")) + "." + amounts[1]),
                    notes=row[2].strip(),
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
