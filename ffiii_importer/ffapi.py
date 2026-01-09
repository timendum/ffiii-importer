import json
import sys
from dataclasses import dataclass
from functools import lru_cache

import httpx

from ffiii_importer.models import (
    AccountSingle,
    RuleAction,
    RuleActionKeyword,
    RuleArray,
    RuleTrigger,
    RuleTriggerKeyword,
    RuleTriggerType,
    TransactionSingle,
    TransactionSplitStore,
    TransactionStore,
    TransactionTypeProperty,
)


def _get_client() -> httpx.Client:
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    token = config["token"]
    base_url = config["instance"]
    client = httpx.Client()
    client.base_url = base_url
    client.timeout = 10.0
    client.headers.update(
        {
            "Authorization": f"Bearer {token}"  # Replace with your token
        }
    )
    return client


CLIENT = _get_client()


def get_base_url() -> str:
    return "/".join(CLIENT._base_url.split("/")[:-2])


def print_progress(done: int, total: int) -> None:
    if total < 1:
        return
    i = 100 * done // total
    print("\r", end="")
    print(f"Progress:   {i}%: ", "=" * (i // 2), end="")
    if done >= total:
        print("\n", end="")
    sys.stdout.flush()


def send_rich(transactions: list[TransactionSplitStore]) -> str:
    apply_rules(transactions)
    for i, transaction in enumerate(transactions):
        # check data-model
        try:
            transaction.model_validate(TransactionSplitStore)
        except ValueError as e:
            print("Invalid transaction:", e, transaction.model_dump())
        resp = CLIENT.post(
            "/v1/transactions",
            content=TransactionStore(transactions=[transaction], apply_rules=False).model_dump_json(
                exclude_unset=True, exclude_none=True
            ),
        )
        resp.raise_for_status()
        transaction_single = TransactionSingle.model_validate_json(resp.text)
        print(transaction_single.data.id)
        print_progress(i + 1, len(transactions))
    return ""


@dataclass
class TRule:
    id: str
    triggers: list[RuleTrigger]
    actions: list[RuleAction]


def get_rules():
    rules: list[TRule] = []
    page = 1
    while page >= 0:
        resp = CLIENT.get("/v1/rules")
        resp.raise_for_status()
        list_rule = RuleArray.model_validate_json(resp.text)
        if (
            list_rule.meta.pagination
            and list_rule.meta.pagination.current_page
            and list_rule.meta.pagination.total_pages
            and list_rule.meta.pagination.current_page < list_rule.meta.pagination.total_pages
        ):
            page += 1
        else:
            page = -1
        for rule in list_rule.data:
            if rule.attributes.trigger != RuleTriggerType.STORE_JOURNAL:
                print(f"skip {rule.id} for trigger = {rule.attributes.trigger}")
                continue
            if not rule.attributes.active:
                print(f"skip {rule.id} for active = {rule.attributes.active}")
                continue
            if not rule.attributes.strict:
                print(f"skip {rule.id} for strict = {rule.attributes.strict}")
                continue
            rules.append(
                TRule(
                    rule.id,
                    rule.attributes.triggers,
                    rule.attributes.actions,
                )
            )
    return rules


@lru_cache(maxsize=128)
def get_account_name(account_id) -> str | None:
    resp = CLIENT.get(f"/v1/accounts/{account_id}")
    resp.raise_for_status()
    account_single = AccountSingle.model_validate_json(resp.text)
    return account_single.data.attributes.name


def _check_trigger(trigger: RuleTrigger, transaction: TransactionSplitStore) -> bool:
    tvalue = trigger.value.lower().strip()
    match trigger.type:
        case RuleTriggerKeyword.NOTES_START:
            return (transaction.notes or "").lower().strip().startswith(tvalue)
        case RuleTriggerKeyword.NOTES_CONTAINS:
            return tvalue in (transaction.notes or "").lower().strip()
        case RuleTriggerKeyword.SOURCE_ACCOUNT_IS:
            if transaction.source_name:
                dname = transaction.source_name
            elif transaction.source_id:
                dname = get_account_name(transaction.source_id)
            else:
                print("No destination info in transaction", transaction)
                return False
            return tvalue == (dname or "").lower().strip()
        case RuleTriggerKeyword.DESTINATION_ACCOUNT_IS:
            if transaction.destination_name:
                dname = transaction.destination_name
            elif transaction.destination_id:
                dname = get_account_name(transaction.destination_id)
            else:
                print("No destination info in transaction", transaction)
                return False
            return tvalue == (dname or "").lower().strip()
        case RuleTriggerKeyword.TRANSACTION_TYPE:
            return tvalue == transaction.type.lower().strip()
        case RuleTriggerKeyword.DESCRIPTION_IS:
            return tvalue == transaction.description.lower().strip()
        case RuleTriggerKeyword.DESCRIPTION_STARTS:
            return transaction.description.lower().strip().startswith(tvalue)
        case RuleTriggerKeyword.DESCRIPTION_CONTAINS:
            return tvalue in transaction.description.lower().strip()
        case RuleTriggerKeyword.AMOUNT_MORE:
            return float(transaction.amount) > float(tvalue)
        case RuleTriggerKeyword.AMOUNT_LESS:
            return float(transaction.amount) < float(tvalue)
        case RuleTriggerKeyword.AMOUNT_EXACTLY:
            return float(transaction.amount) == float(tvalue)
        case RuleTriggerKeyword.CURRENCY_IS:
            # A missing value is ok
            return tvalue == (transaction.currency_code or tvalue).lower().strip()
        case _:
            print("unknown trigger type", trigger.type)
            return False


def apply_rules(transactions: list[TransactionSplitStore]) -> bool:
    rules = get_rules()
    if not rules:
        return False
    for transaction in transactions:
        for rule in rules:
            apply = True
            for trigger in rule.triggers:
                apply = apply and _check_trigger(trigger, transaction)
            if not apply:
                continue
            for action in rule.actions:
                if not action.value:
                    raise ValueError(f"Action {rule} has no value")
                tvalue = action.value
                match action.type_:
                    case RuleActionKeyword.LINK_TO_BILL:
                        transaction.bill_name = tvalue
                    case RuleActionKeyword.ADD_TAG:
                        transaction.tags = transaction.tags or []
                        transaction.tags.append(tvalue)
                    case RuleActionKeyword.SET_DESTINATION_ACCOUNT:
                        transaction.destination_id = None
                        transaction.destination_name = tvalue
                    case RuleActionKeyword.SET_CATEGORY:
                        transaction.category_id = None
                        transaction.category_name = tvalue
                    case RuleActionKeyword.CONVERT_DEPOSIT:
                        transaction.type = TransactionTypeProperty.DEPOSIT
                        transaction.destination_id = None
                        transaction.destination_name = tvalue
                    case RuleActionKeyword.CONVERT_TRANSFER:
                        transaction.type = TransactionTypeProperty.TRANSFER
                        transaction.destination_id = None
                        transaction.destination_name = tvalue
                    case _:
                        print("unknown action type", action.type_)
                        return False
    return True
