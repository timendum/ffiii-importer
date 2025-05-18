import json
import sys
from datetime import datetime as dt

from openpyxl import load_workbook

import ffapi


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_conto = config["assets"]["Arancio"]
    expense = config["expenses"]["Generic"]
    return asset_conto, expense


ASSET_CONTO, EXPENSE = _load_config()


def transform_date(sdate: str | dt) -> str:
    if isinstance(sdate, dt):
        return sdate.date().isoformat()
    return dt.strptime(sdate, "%d/%m/%Y").date().isoformat()


def read_conto(filename: str):
    wb = load_workbook(filename)
    ws = wb.worksheets[0]
    transactions = []
    job_tag = "import-arancio-" + dt.now().isoformat(timespec="minutes")
    for row in ws.rows:
        if len(row) < 6:
            continue
        if not all(row[i].value for i in (1, 2, 3, 4, 5)):
            continue
        amounts = str(row[5].value).split(".")
        if len(amounts) != 2:
            continue
        if amounts[0][0] == "-":
            amounts[0] = amounts[0][1:]
        contabile = transform_date(row[1].value)
        valuta = transform_date(row[2].value)
        transactions.append(
            {
                "type": "withdrawal",
                "source_id": ASSET_CONTO,
                "destination_id": EXPENSE,
                "amount": str(int(amounts[0])) + "." + amounts[1],
                "date": contabile,
                "description": row[4].value.strip(),
                "interest_date": contabile,
                "payment_date": valuta,
                "tags": [job_tag, row[3].value.strip().replace(" ", "-").replace("/", "-")],
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
