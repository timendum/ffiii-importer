from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ArrayEntryWithCurrencyAndSum")


@_attrs_define
class ArrayEntryWithCurrencyAndSum:
    """
    Attributes:
        currency_id (Union[Unset, str]):  Example: 5.
        currency_code (Union[Unset, str]):  Example: USD.
        currency_symbol (Union[Unset, str]):  Example: $.
        currency_decimal_places (Union[Unset, int]): Number of decimals supported by the currency Example: 2.
        sum_ (Union[Unset, str]): The amount earned, spent or transferred. Example: 123.45.
    """

    currency_id: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    currency_symbol: Union[Unset, str] = UNSET
    currency_decimal_places: Union[Unset, int] = UNSET
    sum_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency_id = self.currency_id

        currency_code = self.currency_code

        currency_symbol = self.currency_symbol

        currency_decimal_places = self.currency_decimal_places

        sum_ = self.sum_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol
        if currency_decimal_places is not UNSET:
            field_dict["currency_decimal_places"] = currency_decimal_places
        if sum_ is not UNSET:
            field_dict["sum"] = sum_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        currency_id = d.pop("currency_id", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        currency_symbol = d.pop("currency_symbol", UNSET)

        currency_decimal_places = d.pop("currency_decimal_places", UNSET)

        sum_ = d.pop("sum", UNSET)

        array_entry_with_currency_and_sum = cls(
            currency_id=currency_id,
            currency_code=currency_code,
            currency_symbol=currency_symbol,
            currency_decimal_places=currency_decimal_places,
            sum_=sum_,
        )

        array_entry_with_currency_and_sum.additional_properties = d
        return array_entry_with_currency_and_sum

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
