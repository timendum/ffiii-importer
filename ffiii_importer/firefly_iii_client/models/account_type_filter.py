from enum import Enum


class AccountTypeFilter(str, Enum):
    ALL = "all"
    ASSET = "asset"
    ASSET_ACCOUNT = "Asset account"
    BENEFICIARY_ACCOUNT = "Beneficiary account"
    CASH = "cash"
    CASH_ACCOUNT = "Cash account"
    DEBT = "Debt"
    DEFAULT_ACCOUNT = "Default account"
    EXPENSE = "expense"
    EXPENSE_ACCOUNT = "Expense account"
    HIDDEN = "hidden"
    IMPORT_ACCOUNT = "Import account"
    INITIAL_BALANCE_ACCOUNT = "Initial balance account"
    LIABILITIES = "liabilities"
    LIABILITY = "liability"
    LOAN = "Loan"
    MORTGAGE = "Mortgage"
    RECONCILIATION_ACCOUNT = "Reconciliation account"
    REVENUE = "revenue"
    REVENUE_ACCOUNT = "Revenue account"
    SPECIAL = "special"

    def __str__(self) -> str:
        return str(self.value)
