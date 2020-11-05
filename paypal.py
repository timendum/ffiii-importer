import csv
import json
from datetime import datetime as dt

import ffapi

ASSET_PAYPAL = None
EXPENSE = None


def _load_config():
    with open("config.json", "r", encoding="utf8") as fp:
        config = json.load(fp)
    global ASSET_PAYPAL, EXPENSE
    ASSET_PAYPAL = config["assets"]["Paypal"]
    EXPENSE = config["expenses"]["Generic"]


_load_config()


def _transform_date(sdate: str) -> str:
    return dt.strptime(sdate, "%d/%m/%Y").date().isoformat()


class PP_Dialect(csv.Dialect):
    delimiter = ","
    quotechar = '"'
    doublequote = True
    skipinitialspace = False
    lineterminator = "\n"
    quoting = csv.QUOTE_MINIMAL


PP_DIALECT = PP_Dialect()


def process_csv(filename: str):
    transactions = []
    job_tag = "import-" + dt.now().isoformat(timespec="minutes")
    with open(filename, newline="", encoding="utf8") as f:
        reader = csv.reader(f, dialect=PP_DIALECT)
        # skip header
        next(reader)
        for row in reader:
            amounts = row[7].split(".")
            if len(amounts) != 2:
                amounts = row[7].split(",")
                if len(amounts) != 2:
                    continue
            if amounts[0][0] != "-":
                print("Skipped: " + " ".join(row[3:5]))
                continue
            amounts[0] = amounts[0][1:]
            transactions.append(
                {
                    "type": "withdrawal",
                    "date": _transform_date(row[0]),
                    "source_id": ASSET_PAYPAL,
                    "destination_id": EXPENSE,
                    "amount": str(int(amounts[0])) + "." + amounts[1],
                    "description": " - ".join(row[3:5]),
                    "currency_code": row[6],
                    "tags": [job_tag],
                }
            )
        if not transactions:
            return "No transaction"
        resp = ffapi.send(transactions)
        return resp or "See {}/tags/show/{}".format(ffapi.INSTANCE, job_tag)


if __name__ == "__main__":
    import pprint
    import sys

    if len(sys.argv) < 2:
        result = "python " + sys.argv[0] + " filename"
    else:
        result = process_csv(sys.argv[1])
    pprint.pprint(result)
