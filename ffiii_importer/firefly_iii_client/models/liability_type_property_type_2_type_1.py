from enum import Enum


class LiabilityTypePropertyType2Type1(str, Enum):
    DEBT = "debt"
    LOAN = "loan"
    MORTGAGE = "mortgage"

    def __str__(self) -> str:
        return str(self.value)
