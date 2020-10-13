import json
import urllib.parse

import requests

TOKEN = None
INSTANCE = None


def _load_config():
    with open("config.json", "r", encoding="utf8") as fp:
        config = json.load(fp)
    global TOKEN, INSTANCE
    TOKEN = config["token"]
    INSTANCE = config["instance"]


_load_config()


def send(transactions):
    url = urllib.parse.urljoin(INSTANCE, "/api/v1/transactions")
    for transaction in transactions:
        response = requests.post(
            url=url,
            json={"transactions": [transaction]},
            headers={"Authorization": "Bearer " + TOKEN, "Accept": "application/json"},
        )
        if response.status_code != 200:
            return response.text
    return False
