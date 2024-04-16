import json
import sys
from datetime import datetime as dt

import ffapi
from htmltable import read_file as read_html_file


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_conto = config["assets"]["Arancio"]
    expense = config["expenses"]["Generic"]
    return asset_conto, expense


ASSET_CONTO, EXPENSE = _load_config()


def _transform_date(sdate: str) -> str:
    return dt.strptime(sdate, "%d/%m/%Y").date().isoformat()


def read_conto(filename: str):
    table = read_html_file(filename)
    transactions = []
    job_tag = "import-arancio-" + dt.now().isoformat(timespec="minutes")
    for row in table:
        if len(row) != 5:
            continue
        amounts = row[4][2:].replace('.', '').split(",")
        if len(amounts) != 2:
            continue
        if amounts[0][0] == "-":
            amounts[0] = amounts[0][1:]
        contabile = _transform_date(row[0])
        valuta = _transform_date(row[1])
        transactions.append(
            {
                "type": "withdrawal",
                "source_id": ASSET_CONTO,
                "destination_id": EXPENSE,
                "amount": str(int(amounts[0])) + "." + amounts[1],
                "date": contabile,
                "description": row[3].strip(),
                "interest_date": contabile,
                "payment_date": valuta,
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
        result = read_conto(sys.argv[1])
    print(result)
