import json
import re
import sys
from datetime import datetime as dt

import ffapi
from htmltable import read_file as read_html_file

ASSET_CARTA = None
ASSET_CONTO = None
EXPENSE = None


def _load_config():
    with open("config.json", "r", encoding="utf8") as fp:
        config = json.load(fp)
    global ASSET_CARTA, ASSET_CONTO, EXPENSE
    ASSET_CARTA = config["assets"]["Carta Credito ING"]
    ASSET_CONTO = config["assets"]["Arancio"]
    EXPENSE = config["expenses"]["Generic"]


_load_config()


def _transform_date(sdate: str) -> str:
    return dt.strptime(sdate, "%d/%m/%Y").date().isoformat()


def read_carta(filename: str):
    table = read_html_file(filename)
    job_tag = "import-" + dt.now().isoformat(timespec="minutes")
    transactions = []
    for row in table:
        if len(row) != 5:
            continue
        description = row[2].strip()
        match = re.search(r"(.+?)\s+[A-Z]{3}\sEUR", description)
        if match:
            # Remove " ITA EUR 100,00"
            description = match.group(1)
        amounts = row[4].split(",")
        if len(amounts) != 2:
            continue
        book_date = _transform_date(row[1])
        transactions.append(
            {
                "type": "withdrawal",
                "source_id": ASSET_CARTA,
                "destination_id": EXPENSE,
                "amount": str(int(amounts[0])) + "." + amounts[1],
                "date": book_date,
                "description": description,
                "book_date": book_date,
                "payment_date": _transform_date(row[0]),
                "tags": [job_tag],
            }
        )
    resp = ffapi.send(transactions)
    return resp or "See {}/tags/show/{}".format(ffapi.INSTANCE, job_tag)


if __name__ == "__main__":
    import pprint

    if len(sys.argv) < 2:
        result = "python " + sys.argv[0] + " filename"
    else:
        result = read_carta(sys.argv[2])
    pprint.pprint(result)
