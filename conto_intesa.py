import json
import sys
from datetime import datetime as dt

from openpyxl import load_workbook

import ffapi


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_conto = config["assets"]["Intesa"]
    expense = config["expenses"]["Generic"]
    return asset_conto, expense


ASSET_CONTO, EXPENSE = _load_config()


def _transform_date(sdate: dt) -> str:
    return sdate.date().isoformat()


def read_conto(filename: str):
    wb = load_workbook(filename)
    ws = wb.worksheets[0]
    transactions = []
    job_tag = "import-intesa-" + dt.now().isoformat(timespec="minutes")
    for row in ws.rows:
        if len(row) < 7:
            continue
        values = [c.value for c in row]
        if not values[0] or not values[1] or not values[4]:
            if values[0] and values[1] and not values[4] and values[3] and isinstance(values[3], float):
                print(f"Skipped: {row[3].value} - {row[5].value}")
            continue
        if not isinstance(values[4], float):
            continue
        amounts = values[4]
        if amounts < 0:
            amounts = -amounts
        contabile = _transform_date(row[0].value)
        valuta = _transform_date(row[1].value)
        transactions.append(
            {
                "type": "withdrawal",
                "source_id": ASSET_CONTO,
                "destination_id": EXPENSE,
                "amount": repr(amounts),
                "date": contabile,
                "description": values[2].strip(),
                "notes": values[5].strip(),
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
