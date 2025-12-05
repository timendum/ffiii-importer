from enum import Enum


class TransactionTypeProperty(str, Enum):
    DEPOSIT = "deposit"
    OPENING_BALANCE = "opening balance"
    RECONCILIATION = "reconciliation"
    TRANSFER = "transfer"
    WITHDRAWAL = "withdrawal"

    def __str__(self) -> str:
        return str(self.value)
