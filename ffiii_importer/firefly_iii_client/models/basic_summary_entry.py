from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BasicSummaryEntry")


@_attrs_define
class BasicSummaryEntry:
    """
    Attributes:
        key (Union[Unset, str]): This is a reference to the type of info shared, not influenced by translations or user
            preferences. The EUR value is a reference to the currency code. Possibilities are: balance-in-ABC, spent-in-ABC,
            earned-in-ABC, bills-paid-in-ABC, bills-unpaid-in-ABC, left-to-spend-in-ABC and net-worth-in-ABC. Example:
            balance-in-EUR.
        title (Union[Unset, str]): A translated title for the information shared. Example: Balance ($).
        monetary_value (Union[Unset, float]): The amount as a float. Example: 123.45.
        currency_id (Union[Unset, str]): The currency ID of the associated currency. Example: 5.
        currency_code (Union[Unset, str]):  Example: EUR.
        currency_symbol (Union[Unset, str]):  Example: $.
        currency_decimal_places (Union[Unset, int]): Number of decimals for the associated currency. Example: 2.
        no_available_budgets (Union[Unset, bool]): True if there are no available budgets available.
        value_parsed (Union[Unset, str]): The amount formatted according to the users locale Example: $ 12.45.
        local_icon (Union[Unset, str]): Reference to a font-awesome icon without the fa- part. Example: balance-scale.
        sub_title (Union[Unset, str]): A short explanation of the amounts origin. Already formatted according to the
            locale of the user or translated, if relevant. Example: $20 + $-40.
    """

    key: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    monetary_value: Union[Unset, float] = UNSET
    currency_id: Union[Unset, str] = UNSET
    currency_code: Union[Unset, str] = UNSET
    currency_symbol: Union[Unset, str] = UNSET
    currency_decimal_places: Union[Unset, int] = UNSET
    no_available_budgets: Union[Unset, bool] = UNSET
    value_parsed: Union[Unset, str] = UNSET
    local_icon: Union[Unset, str] = UNSET
    sub_title: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        title = self.title

        monetary_value = self.monetary_value

        currency_id = self.currency_id

        currency_code = self.currency_code

        currency_symbol = self.currency_symbol

        currency_decimal_places = self.currency_decimal_places

        no_available_budgets = self.no_available_budgets

        value_parsed = self.value_parsed

        local_icon = self.local_icon

        sub_title = self.sub_title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if title is not UNSET:
            field_dict["title"] = title
        if monetary_value is not UNSET:
            field_dict["monetary_value"] = monetary_value
        if currency_id is not UNSET:
            field_dict["currency_id"] = currency_id
        if currency_code is not UNSET:
            field_dict["currency_code"] = currency_code
        if currency_symbol is not UNSET:
            field_dict["currency_symbol"] = currency_symbol
        if currency_decimal_places is not UNSET:
            field_dict["currency_decimal_places"] = currency_decimal_places
        if no_available_budgets is not UNSET:
            field_dict["no_available_budgets"] = no_available_budgets
        if value_parsed is not UNSET:
            field_dict["value_parsed"] = value_parsed
        if local_icon is not UNSET:
            field_dict["local_icon"] = local_icon
        if sub_title is not UNSET:
            field_dict["sub_title"] = sub_title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key", UNSET)

        title = d.pop("title", UNSET)

        monetary_value = d.pop("monetary_value", UNSET)

        currency_id = d.pop("currency_id", UNSET)

        currency_code = d.pop("currency_code", UNSET)

        currency_symbol = d.pop("currency_symbol", UNSET)

        currency_decimal_places = d.pop("currency_decimal_places", UNSET)

        no_available_budgets = d.pop("no_available_budgets", UNSET)

        value_parsed = d.pop("value_parsed", UNSET)

        local_icon = d.pop("local_icon", UNSET)

        sub_title = d.pop("sub_title", UNSET)

        basic_summary_entry = cls(
            key=key,
            title=title,
            monetary_value=monetary_value,
            currency_id=currency_id,
            currency_code=currency_code,
            currency_symbol=currency_symbol,
            currency_decimal_places=currency_decimal_places,
            no_available_budgets=no_available_budgets,
            value_parsed=value_parsed,
            local_icon=local_icon,
            sub_title=sub_title,
        )

        basic_summary_entry.additional_properties = d
        return basic_summary_entry

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
