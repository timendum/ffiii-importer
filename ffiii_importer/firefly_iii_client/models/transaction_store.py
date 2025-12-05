from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.transaction_split_store import TransactionSplitStore


T = TypeVar("T", bound="TransactionStore")


@_attrs_define
class TransactionStore:
    """
    Attributes:
        transactions (list['TransactionSplitStore']):
        error_if_duplicate_hash (Union[Unset, bool]): Break if the submitted transaction exists already.
        apply_rules (Union[Unset, bool]): Whether or not to apply rules when submitting transaction.
        fire_webhooks (Union[Unset, bool]): Whether or not to fire the webhooks that are related to this event. Default:
            True. Example: True.
        group_title (Union[None, Unset, str]): Title of the transaction if it has been split in more than one piece.
            Empty otherwise. Example: Split transaction title..
    """

    transactions: list["TransactionSplitStore"]
    error_if_duplicate_hash: Union[Unset, bool] = UNSET
    apply_rules: Union[Unset, bool] = UNSET
    fire_webhooks: Union[Unset, bool] = True
    group_title: Union[None, Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        transactions = []
        for transactions_item_data in self.transactions:
            transactions_item = transactions_item_data.to_dict()
            transactions.append(transactions_item)

        error_if_duplicate_hash = self.error_if_duplicate_hash

        apply_rules = self.apply_rules

        fire_webhooks = self.fire_webhooks

        group_title: Union[None, Unset, str]
        if isinstance(self.group_title, Unset):
            group_title = UNSET
        else:
            group_title = self.group_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "transactions": transactions,
            }
        )
        if error_if_duplicate_hash is not UNSET:
            field_dict["error_if_duplicate_hash"] = error_if_duplicate_hash
        if apply_rules is not UNSET:
            field_dict["apply_rules"] = apply_rules
        if fire_webhooks is not UNSET:
            field_dict["fire_webhooks"] = fire_webhooks
        if group_title is not UNSET:
            field_dict["group_title"] = group_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_split_store import TransactionSplitStore

        d = dict(src_dict)
        transactions = []
        _transactions = d.pop("transactions")
        for transactions_item_data in _transactions:
            transactions_item = TransactionSplitStore.from_dict(transactions_item_data)

            transactions.append(transactions_item)

        error_if_duplicate_hash = d.pop("error_if_duplicate_hash", UNSET)

        apply_rules = d.pop("apply_rules", UNSET)

        fire_webhooks = d.pop("fire_webhooks", UNSET)

        def _parse_group_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        group_title = _parse_group_title(d.pop("group_title", UNSET))

        transaction_store = cls(
            transactions=transactions,
            error_if_duplicate_hash=error_if_duplicate_hash,
            apply_rules=apply_rules,
            fire_webhooks=fire_webhooks,
            group_title=group_title,
        )

        transaction_store.additional_properties = d
        return transaction_store

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
