from enum import Enum


class LiabilityDirectionPropertyType1(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"

    def __str__(self) -> str:
        return str(self.value)
