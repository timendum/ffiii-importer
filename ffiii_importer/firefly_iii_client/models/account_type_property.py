from enum import Enum


class AccountTypeProperty(str, Enum):
    ASSET_ACCOUNT = "Asset account"
    BENEFICIARY_ACCOUNT = "Beneficiary account"
    CASH_ACCOUNT = "Cash account"
    DEBT = "Debt"
    DEFAULT_ACCOUNT = "Default account"
    EXPENSE_ACCOUNT = "Expense account"
    IMPORT_ACCOUNT = "Import account"
    INITIAL_BALANCE_ACCOUNT = "Initial balance account"
    LOAN = "Loan"
    MORTGAGE = "Mortgage"
    RECONCILIATION_ACCOUNT = "Reconciliation account"
    REVENUE_ACCOUNT = "Revenue account"

    def __str__(self) -> str:
        return str(self.value)
