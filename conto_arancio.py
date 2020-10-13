import json
import re
import sys
from datetime import datetime as dt

import ffapi
from htmltable import read_file as read_html_file

ASSET_CONTO = None
EXPENSE = None


def _load_config():
    with open("config.json", "r", encoding="utf8") as fp:
        config = json.load(fp)
    global ASSET_CONTO, EXPENSE
    ASSET_CONTO = config["assets"]["Arancio"]
    EXPENSE = config["expenses"]["Generic"]


_load_config()


def _transform_date(sdate: str) -> str:
    return dt.strptime(sdate, "%d/%m/%Y").date().isoformat()


def read_conto(filename: str):
    table = read_html_file(filename)
    transactions = []
    job_tag = "import-" + dt.now().isoformat(timespec="minutes")
    for row in table:
        if len(row) != 5:
            continue
        amounts = row[4][2:].split(",")
        if len(amounts) != 2:
            continue
        if amounts[0][0] == "-":
            amounts[0] = amounts[0][1:]
        contabile = _transform_date(row[0])
        valuta = _transform_date(row[1])
        transactions.append(
            {
                "amount": str(int(amounts[0])) + "." + amounts[1],
                "date": contabile,
                "description": row[3].strip(),
                "interest_date": contabile,
                "payment_date": valuta,
                "notes": row[3],
                "tags": [job_tag],
            }
        )
    resp = ffapi.send(transactions)
    if not resp:
        print("See {}/tags/show/{}".format(ffapi.INSTANCE, job_tag))


if __name__ == "__main__":
    import pprint

    if len(sys.argv) < 2:
        result = "python " + sys.argv[0] + " filename"
    else:
        result = read_conto(sys.argv[2])
    pprint.pprint(result)
