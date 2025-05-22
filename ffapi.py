import json
import sys
import urllib.parse

import requests

TOKEN = None
INSTANCE = None


def _load_config():
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    global TOKEN, INSTANCE
    TOKEN = config["token"]
    INSTANCE = config["instance"]


_load_config()


def print_progess(done: int, total: int) -> None:
    if total < 1:
        return
    i = 100 * done // total
    print("\r", end="")
    print(f"Progress:   {i}%: ", "=" * (i // 2), end="")
    if done >= total:
        print("\n", end="")
    sys.stdout.flush()


def send(transactions):
    url = urllib.parse.urljoin(INSTANCE, "/api/v1/transactions")
    for i, transaction in enumerate(transactions):
        response = requests.post(
            url=url,
            json={"transactions": [transaction]},
            headers={"Authorization": "Bearer " + TOKEN, "Accept": "application/json"},
        )
        print_progess(i + 1, len(transactions))
        if response.status_code != 200:
            print(response.text, transaction)
            continue
    return False
