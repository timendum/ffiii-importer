import json
import re
import sys
import warnings
from datetime import datetime as dt

from openpyxl import load_workbook

import ffapi
from conto_arancio import transform_date


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_carta = config["assets"]["Carta Credito ING"]
    expense = config["expenses"]["Generic"]
    return asset_carta, expense


ASSET_CARTA, EXPENSE = _load_config()


def read_carta(filename: str):
    wb = None
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore", category=UserWarning, module=re.escape("openpyxl.styles.stylesheet")
        )
        wb = load_workbook(filename)
    ws = wb.worksheets[0]
    job_tag = "import-cartaing-" + dt.now().isoformat(timespec="minutes")
    transactions = []
    for row in ws.rows:
        if len(row) != 5:
            continue
        if not all(row[i].value for i in (1, 2, 3, 4)):
            continue
        description = row[3].value.strip()
        amounts = str(row[4].value).split(".")
        if len(amounts) != 2:
            continue
        if amounts[0][0] == "-":
            amounts[0] = amounts[0][1:]
        contabile = transform_date(row[2].value)
        valuta = transform_date(row[1].value)
        transactions.append(
            {
                "type": "withdrawal",
                "source_id": ASSET_CARTA,
                "destination_id": EXPENSE,
                "amount": str(int(amounts[0])) + "." + amounts[1],
                "date": contabile,
                "description": description,
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
        result = read_carta(sys.argv[1])
    print(result)
