from enum import Enum


class InterestPeriodPropertyType1(str, Enum):
    HALF_YEAR = "half-year"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    WEEKLY = "weekly"
    YEARLY = "yearly"

    def __str__(self) -> str:
        return str(self.value)
