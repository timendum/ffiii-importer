from enum import Enum


class AccountRolePropertyType3Type1(str, Enum):
    CASHWALLETASSET = "cashWalletAsset"
    CCASSET = "ccAsset"
    DEFAULTASSET = "defaultAsset"
    SAVINGASSET = "savingAsset"
    SHAREDASSET = "sharedAsset"

    def __str__(self) -> str:
        return str(self.value)
