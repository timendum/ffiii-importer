import json
import sys
from dataclasses import dataclass
from functools import lru_cache

from ffiii_importer.firefly_iii_client import AuthenticatedClient
from ffiii_importer.firefly_iii_client.api.accounts import get_account as get_account
from ffiii_importer.firefly_iii_client.api.rules import list_rule
from ffiii_importer.firefly_iii_client.api.transactions import store_transaction
from ffiii_importer.firefly_iii_client.models.rule_action import RuleAction
from ffiii_importer.firefly_iii_client.models.rule_action_keyword import RuleActionKeyword
from ffiii_importer.firefly_iii_client.models.rule_trigger import RuleTrigger
from ffiii_importer.firefly_iii_client.models.rule_trigger_keyword import RuleTriggerKeyword
from ffiii_importer.firefly_iii_client.models.rule_trigger_type import RuleTriggerType
from ffiii_importer.firefly_iii_client.models.transaction_single import TransactionSingle
from ffiii_importer.firefly_iii_client.models.transaction_split_store import TransactionSplitStore
from ffiii_importer.firefly_iii_client.models.transaction_store import TransactionStore
from ffiii_importer.firefly_iii_client.models.transaction_type_property import (
    TransactionTypeProperty,
)
from ffiii_importer.firefly_iii_client.types import UNSET


def _get_client() -> AuthenticatedClient:
    with open("config.json", encoding="utf8") as fp:
        config = json.load(fp)
    token = config["token"]
    base_url = config["instance"]
    return AuthenticatedClient(base_url=base_url, token=token)


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


def send(transactions: list[TransactionSplitStore]) -> bool:
    for i, transaction in enumerate(transactions):
        resp = store_transaction.sync(
            client=CLIENT, body=TransactionStore(transactions=[transaction], apply_rules=False)
        )
        print_progress(i + 1, len(transactions))
        if not isinstance(resp, TransactionSingle):
            print(resp, transaction)
            continue
    return True


def send_rich(transactions: list[TransactionSplitStore]) -> str:
    apply_rules(transactions)
    for i, transaction in enumerate(transactions):
        # check datamodel
        TransactionSplitStore.from_dict(transaction.to_dict())
        resp = store_transaction.sync(
            client=CLIENT, body=TransactionStore(transactions=[transaction], apply_rules=False)
        )
        print_progress(i + 1, len(transactions))
        if resp and not isinstance(resp, TransactionSingle):
            print(resp, transaction)
            continue
    return ""


@dataclass
class TRule:
    id: str
    triggers: list[RuleTrigger]
    actions: list[RuleAction]


def get_rules():
    resp = list_rule.sync(client=CLIENT)
    if not resp or not isinstance(resp, list_rule.RuleArray):
        return None
    rules: list[TRule] = []
    page = 1
    while page >= 0:
        resp = list_rule.sync(client=CLIENT, page=page)
        if not resp or not isinstance(resp, list_rule.RuleArray):
            return rules
        if (
            resp.meta.pagination
            and resp.meta.pagination.current_page
            and resp.meta.pagination.total_pages
            and resp.meta.pagination.current_page < resp.meta.pagination.total_pages
        ):
            page += 1
        else:
            page = -1
        for rule in resp.data:
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
    resp = get_account.sync(client=CLIENT, id=account_id)
    if not resp or not isinstance(resp, get_account.AccountSingle):
        return None
    return resp.data.attributes.name


def _check_trigger(trigger: RuleTrigger, transaction: TransactionSplitStore) -> bool:
    tvalue = trigger.value.lower().strip()
    match trigger.type_:
        case RuleTriggerKeyword.NOTES_STARTS | RuleTriggerKeyword.NOTES_START:
            return (transaction.notes or "").lower().strip().startswith(tvalue)
        case RuleTriggerKeyword.NOTES_CONTAIN | RuleTriggerKeyword.NOTES_CONTAINS:
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
            return tvalue == transaction.type_.lower().strip()
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
            print("unknown trigger type", trigger.type_)
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
                        transaction.destination_id = UNSET
                        transaction.destination_name = tvalue
                    case RuleActionKeyword.SET_CATEGORY:
                        transaction.category_id = UNSET
                        transaction.category_name = tvalue
                    case RuleActionKeyword.CONVERT_DEPOSIT:
                        transaction.type_ = TransactionTypeProperty.DEPOSIT
                        transaction.destination_id = UNSET
                        transaction.destination_name = tvalue
                    case RuleActionKeyword.CONVERT_TRANSFER:
                        transaction.type_ = TransactionTypeProperty.TRANSFER
                        transaction.destination_id = UNSET
                        transaction.destination_name = tvalue
                    case _:
                        print("unknown action type", action.type_)
                        return False
    return True
