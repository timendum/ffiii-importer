from enum import Enum


class CreditCardTypePropertyType1(str, Enum):
    MONTHLYFULL = "monthlyFull"

    def __str__(self) -> str:
        return str(self.value)
