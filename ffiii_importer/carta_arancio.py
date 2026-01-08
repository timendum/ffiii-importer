import json
import re
import sys
import warnings
from datetime import datetime as dt

from openpyxl import load_workbook

from ffiii_importer import ffapi
from ffiii_importer.models import TransactionSplitStore, TransactionTypeProperty


def _load_config() -> tuple[str, str]:
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    asset_carta = config["assets"]["Carta Credito ING"]
    expense = config["expenses"]["Generic"]
    return asset_carta, expense


ASSET_CARTA, EXPENSE = _load_config()


def read_carta(filename: str) -> str:
    wb = None
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore", category=UserWarning, module=re.escape("openpyxl.styles.stylesheet")
        )
        wb = load_workbook(filename)
    ws = wb.worksheets[0]
    job_tag = "import-cartaing-" + dt.now().isoformat(timespec="minutes")
    transactions = list[TransactionSplitStore]()
    for row in ws.rows:
        if len(row) != 5:
            continue
        if not all(row[i].value for i in (1, 2, 3, 4)):
            continue
        description = str(row[3].value).strip()
        amounts = str(row[4].value).split(".")
        if len(amounts) != 2:
            continue
        if amounts[0][0] == "-":
            amounts[0] = amounts[0][1:]
        contabile = row[2].value
        valuta = row[1].value
        transactions.append(
            TransactionSplitStore(
                type=TransactionTypeProperty.WITHDRAWAL,
                source_id=ASSET_CARTA,
                destination_id=EXPENSE,
                amount=float(amounts[0] + "." + amounts[1]),
                date=contabile,
                description=description,
                interest_date=contabile,
                payment_date=valuta,
                tags=[job_tag],
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
        result = read_carta(sys.argv[1])
    print(result)
