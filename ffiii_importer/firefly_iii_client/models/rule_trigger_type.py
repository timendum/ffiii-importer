from enum import Enum


class RuleTriggerType(str, Enum):
    STORE_JOURNAL = "store-journal"
    UPDATE_JOURNAL = "update-journal"
    MANUAL_ACTIVATION = "manual-activation"

    def __str__(self) -> str:
        return str(self.value)
