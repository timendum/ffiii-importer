import json
import re
import sys
from datetime import datetime as dt

import ffapi
from htmltable import read_file as read_html_file


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_carta = config["assets"]["Carta Credito ING"]
    expense = config["expenses"]["Generic"]
    return asset_carta, expense


ASSET_CARTA, EXPENSE = _load_config()


def _transform_date(sdate: str) -> str:
    return dt.strptime(sdate, "%d/%m/%Y").date().isoformat()


def read_carta(filename: str):
    table = read_html_file(filename)
    job_tag = "import-cartaing-" + dt.now().isoformat(timespec="minutes")
    transactions = []
    for row in table:
        if len(row) != 5:
            continue
        description = row[2].strip()
        match = re.search(r"(.+?)\s+[A-Z]{3}\sEUR", description)
        if match:
            # Remove " ITA EUR 100,00"
            description = match.group(1)
        amounts = row[4].replace('.', '').split(",")
        if len(amounts) != 2:
            continue
        if int(amounts[0]) < 0 :
            print("Skipped: " + " ".join(row))
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
    if not transactions:
        return "No transaction"
    resp = ffapi.send(transactions)
    return resp or f"See {ffapi.INSTANCE}/tags/show/{job_tag}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        result = "python " + sys.argv[0] + " filename"
    else:
        result = read_carta(sys.argv[1])
    print(result)
