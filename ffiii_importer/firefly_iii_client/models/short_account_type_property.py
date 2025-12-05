from enum import Enum


class ShortAccountTypeProperty(str, Enum):
    ASSET = "asset"
    CASH = "cash"
    EXPENSE = "expense"
    IMPORT = "import"
    INITIAL_BALANCE = "initial-balance"
    LIABILITIES = "liabilities"
    LIABILITY = "liability"
    RECONCILIATION = "reconciliation"
    REVENUE = "revenue"

    def __str__(self) -> str:
        return str(self.value)
