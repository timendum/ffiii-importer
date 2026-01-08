import json
import sys
from datetime import datetime as dt

from openpyxl import load_workbook

from ffiii_importer import ffapi
from ffiii_importer.models import TransactionSplitStore, TransactionTypeProperty


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_conto = config["assets"]["Intesa"]
    expense = config["expenses"]["Generic"]
    return asset_conto, expense


ASSET_CONTO, EXPENSE = _load_config()


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
            if (
                values[0]
                and values[1]
                and not values[4]
                and values[3]
                and isinstance(values[3], float)
            ):
                print(f"Skipped: {row[3].value} - {row[5].value}")
            continue
        if not isinstance(values[4], float):
            continue
        amounts = values[4]
        if amounts < 0:
            amounts = -amounts
        contabile = row[0].value
        valuta = row[1].value
        transactions.append(
            TransactionSplitStore(
                type=TransactionTypeProperty.WITHDRAWAL,
                source_id=ASSET_CONTO,
                destination_id=EXPENSE,
                date=contabile,
                description=row[2].strip(),
                payment_date=valuta,
                amount=amounts,
                notes=row[5].strip(),
                tags=[job_tag],
                interest_date=contabile,
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
