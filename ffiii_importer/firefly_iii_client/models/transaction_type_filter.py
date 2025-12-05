from enum import Enum


class TransactionTypeFilter(str, Enum):
    ALL = "all"
    DEFAULT = "default"
    DEPOSIT = "deposit"
    DEPOSITS = "deposits"
    EXPENSE = "expense"
    INCOME = "income"
    OPENING_BALANCE = "opening_balance"
    RECONCILIATION = "reconciliation"
    SPECIAL = "special"
    SPECIALS = "specials"
    TRANSFER = "transfer"
    TRANSFERS = "transfers"
    WITHDRAWAL = "withdrawal"
    WITHDRAWALS = "withdrawals"

    def __str__(self) -> str:
        return str(self.value)
