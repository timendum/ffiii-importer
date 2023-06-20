import json
import sys
from datetime import datetime as dt

from openpyxl import load_workbook

import ffapi


ASSET_CONTO = None
EXPENSE = None


def _load_config():
    with open("config.json", "r", encoding="utf8") as fp:
        config = json.load(fp)
    global ASSET_CONTO, EXPENSE
    ASSET_CONTO = config["assets"]["Intesa"]
    EXPENSE = config["expenses"]["Generic"]


_load_config()


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
    return resp or "See {}/tags/show/{}".format(ffapi.INSTANCE, job_tag)


if __name__ == "__main__":
    import pprint

    if len(sys.argv) < 2:
        result = "python " + sys.argv[0] + " filename"
    else:
        result = read_conto(sys.argv[1])
    pprint.pprint(result)
