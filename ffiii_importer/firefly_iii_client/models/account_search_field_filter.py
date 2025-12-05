from enum import Enum


class AccountSearchFieldFilter(str, Enum):
    ALL = "all"
    IBAN = "iban"
    ID = "id"
    NAME = "name"
    NUMBER = "number"

    def __str__(self) -> str:
        return str(self.value)
