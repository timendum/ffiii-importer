from enum import Enum


class CreditCardTypePropertyType2Type1(str, Enum):
    MONTHLYFULL = "monthlyFull"

    def __str__(self) -> str:
        return str(self.value)
