from enum import Enum


class LiabilityDirectionPropertyType3Type1(str, Enum):
    CREDIT = "credit"
    DEBIT = "debit"

    def __str__(self) -> str:
        return str(self.value)
