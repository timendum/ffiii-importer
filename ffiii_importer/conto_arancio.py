import json
import sys
from datetime import datetime as dt

from openpyxl import load_workbook

from ffiii_importer import ffapi
from ffiii_importer.models import TransactionSplitStore, TransactionTypeProperty


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_conto = config["assets"]["Arancio"]
    expense = config["expenses"]["Generic"]
    return asset_conto, expense


ASSET_CONTO, EXPENSE = _load_config()


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
        contabile = row[1].value
        valuta = row[2].value
        transactions.append(
            TransactionSplitStore(
                type=TransactionTypeProperty.WITHDRAWAL,
                source_id=ASSET_CONTO,
                destination_id=EXPENSE,
                amount=float(amounts[0] + "." + amounts[1]),
                date=contabile,
                description=row[4].value.strip(),
                interest_date=contabile,
                payment_date=valuta,
                tags=[job_tag, row[3].value.strip().replace(" ", "-").replace("/", "-")],
            )
        )
    if not transactions:
        return "No transaction"
    resp = ffapi.send_rich(transactions)
    return resp or f"See {ffapi.get_base_url()}/tags/show/{job_tag}"


if __name__ == "__main__":
    if len(sys.argv) < 2:
        result = "python " + sys.argv[0] + " filename"
    else:
        result = read_conto(sys.argv[1])
    print(result)
