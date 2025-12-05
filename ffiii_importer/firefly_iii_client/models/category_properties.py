import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.array_entry_with_currency_and_sum import ArrayEntryWithCurrencyAndSum


T = TypeVar("T", bound="CategoryProperties")


@_attrs_define
class CategoryProperties:
    """
    Attributes:
        name (str):  Example: Lunch.
        created_at (Union[Unset, datetime.datetime]):  Example: 2025-10-01T00:00:00+00:00.
        updated_at (Union[Unset, datetime.datetime]):  Example: 2025-10-01T00:00:00+00:00.
        notes (Union[None, Unset, str]):  Example: Some example notes.
        object_has_currency_setting (Union[Unset, bool]): This object never has its own currency setting, so this value
            is always false.
        primary_currency_id (Union[Unset, str]): The currency ID of the administration's primary currency. Example: 5.
        primary_currency_name (Union[Unset, str]): The currency name of the administration's primary currency. Example:
            Euro.
        primary_currency_code (Union[Unset, str]): The currency code of the administration's primary currency. Example:
            EUR.
        primary_currency_symbol (Union[Unset, str]): The currency symbol of the administration's primary currency.
            Example: $.
        primary_currency_decimal_places (Union[Unset, int]): The currency decimal places of the administration's primary
            currency. Example: 2.
        spent (Union[Unset, list['ArrayEntryWithCurrencyAndSum']]): Amount(s) spent in the currencies in the database
            for this category. ONLY present when start and date are set.
        pc_spent (Union[Unset, list['ArrayEntryWithCurrencyAndSum']]): Amount(s) spent in the primary currency in the
            database for this category. ONLY present when start and date are set.
        earned (Union[Unset, list['ArrayEntryWithCurrencyAndSum']]): Amount(s) earned in the currencies in the database
            for this category. ONLY present when start and date are set.
        pc_earned (Union[Unset, list['ArrayEntryWithCurrencyAndSum']]): Amount(s) earned in the primary currency in the
            database for this category. ONLY present when start and date are set.
        transferred (Union[Unset, list['ArrayEntryWithCurrencyAndSum']]): Amount(s) transferred in the currencies in the
            database for this category. ONLY present when start and date are set.
        pc_transferred (Union[Unset, list['ArrayEntryWithCurrencyAndSum']]): Amount(s) transferred in primary currency
            in the database for this category. ONLY present when start and date are set.
    """

    name: str
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    notes: Union[None, Unset, str] = UNSET
    object_has_currency_setting: Union[Unset, bool] = UNSET
    primary_currency_id: Union[Unset, str] = UNSET
    primary_currency_name: Union[Unset, str] = UNSET
    primary_currency_code: Union[Unset, str] = UNSET
    primary_currency_symbol: Union[Unset, str] = UNSET
    primary_currency_decimal_places: Union[Unset, int] = UNSET
    spent: Union[Unset, list["ArrayEntryWithCurrencyAndSum"]] = UNSET
    pc_spent: Union[Unset, list["ArrayEntryWithCurrencyAndSum"]] = UNSET
    earned: Union[Unset, list["ArrayEntryWithCurrencyAndSum"]] = UNSET
    pc_earned: Union[Unset, list["ArrayEntryWithCurrencyAndSum"]] = UNSET
    transferred: Union[Unset, list["ArrayEntryWithCurrencyAndSum"]] = UNSET
    pc_transferred: Union[Unset, list["ArrayEntryWithCurrencyAndSum"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        notes: Union[None, Unset, str]
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        object_has_currency_setting = self.object_has_currency_setting

        primary_currency_id = self.primary_currency_id

        primary_currency_name = self.primary_currency_name

        primary_currency_code = self.primary_currency_code

        primary_currency_symbol = self.primary_currency_symbol

        primary_currency_decimal_places = self.primary_currency_decimal_places

        spent: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.spent, Unset):
            spent = []
            for spent_item_data in self.spent:
                spent_item = spent_item_data.to_dict()
                spent.append(spent_item)

        pc_spent: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pc_spent, Unset):
            pc_spent = []
            for pc_spent_item_data in self.pc_spent:
                pc_spent_item = pc_spent_item_data.to_dict()
                pc_spent.append(pc_spent_item)

        earned: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.earned, Unset):
            earned = []
            for earned_item_data in self.earned:
                earned_item = earned_item_data.to_dict()
                earned.append(earned_item)

        pc_earned: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pc_earned, Unset):
            pc_earned = []
            for pc_earned_item_data in self.pc_earned:
                pc_earned_item = pc_earned_item_data.to_dict()
                pc_earned.append(pc_earned_item)

        transferred: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.transferred, Unset):
            transferred = []
            for transferred_item_data in self.transferred:
                transferred_item = transferred_item_data.to_dict()
                transferred.append(transferred_item)

        pc_transferred: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pc_transferred, Unset):
            pc_transferred = []
            for pc_transferred_item_data in self.pc_transferred:
                pc_transferred_item = pc_transferred_item_data.to_dict()
                pc_transferred.append(pc_transferred_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if notes is not UNSET:
            field_dict["notes"] = notes
        if object_has_currency_setting is not UNSET:
            field_dict["object_has_currency_setting"] = object_has_currency_setting
        if primary_currency_id is not UNSET:
            field_dict["primary_currency_id"] = primary_currency_id
        if primary_currency_name is not UNSET:
            field_dict["primary_currency_name"] = primary_currency_name
        if primary_currency_code is not UNSET:
            field_dict["primary_currency_code"] = primary_currency_code
        if primary_currency_symbol is not UNSET:
            field_dict["primary_currency_symbol"] = primary_currency_symbol
        if primary_currency_decimal_places is not UNSET:
            field_dict["primary_currency_decimal_places"] = primary_currency_decimal_places
        if spent is not UNSET:
            field_dict["spent"] = spent
        if pc_spent is not UNSET:
            field_dict["pc_spent"] = pc_spent
        if earned is not UNSET:
            field_dict["earned"] = earned
        if pc_earned is not UNSET:
            field_dict["pc_earned"] = pc_earned
        if transferred is not UNSET:
            field_dict["transferred"] = transferred
        if pc_transferred is not UNSET:
            field_dict["pc_transferred"] = pc_transferred

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.array_entry_with_currency_and_sum import ArrayEntryWithCurrencyAndSum

        d = dict(src_dict)
        name = d.pop("name")

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _updated_at = d.pop("updated_at", UNSET)
        updated_at: Union[Unset, datetime.datetime]
        if isinstance(_updated_at, Unset):
            updated_at = UNSET
        else:
            updated_at = isoparse(_updated_at)

        def _parse_notes(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        notes = _parse_notes(d.pop("notes", UNSET))

        object_has_currency_setting = d.pop("object_has_currency_setting", UNSET)

        primary_currency_id = d.pop("primary_currency_id", UNSET)

        primary_currency_name = d.pop("primary_currency_name", UNSET)

        primary_currency_code = d.pop("primary_currency_code", UNSET)

        primary_currency_symbol = d.pop("primary_currency_symbol", UNSET)

        primary_currency_decimal_places = d.pop("primary_currency_decimal_places", UNSET)

        spent = []
        _spent = d.pop("spent", UNSET)
        for spent_item_data in _spent or []:
            spent_item = ArrayEntryWithCurrencyAndSum.from_dict(spent_item_data)

            spent.append(spent_item)

        pc_spent = []
        _pc_spent = d.pop("pc_spent", UNSET)
        for pc_spent_item_data in _pc_spent or []:
            pc_spent_item = ArrayEntryWithCurrencyAndSum.from_dict(pc_spent_item_data)

            pc_spent.append(pc_spent_item)

        earned = []
        _earned = d.pop("earned", UNSET)
        for earned_item_data in _earned or []:
            earned_item = ArrayEntryWithCurrencyAndSum.from_dict(earned_item_data)

            earned.append(earned_item)

        pc_earned = []
        _pc_earned = d.pop("pc_earned", UNSET)
        for pc_earned_item_data in _pc_earned or []:
            pc_earned_item = ArrayEntryWithCurrencyAndSum.from_dict(pc_earned_item_data)

            pc_earned.append(pc_earned_item)

        transferred = []
        _transferred = d.pop("transferred", UNSET)
        for transferred_item_data in _transferred or []:
            transferred_item = ArrayEntryWithCurrencyAndSum.from_dict(transferred_item_data)

            transferred.append(transferred_item)

        pc_transferred = []
        _pc_transferred = d.pop("pc_transferred", UNSET)
        for pc_transferred_item_data in _pc_transferred or []:
            pc_transferred_item = ArrayEntryWithCurrencyAndSum.from_dict(pc_transferred_item_data)

            pc_transferred.append(pc_transferred_item)

        category_properties = cls(
            name=name,
            created_at=created_at,
            updated_at=updated_at,
            notes=notes,
            object_has_currency_setting=object_has_currency_setting,
            primary_currency_id=primary_currency_id,
            primary_currency_name=primary_currency_name,
            primary_currency_code=primary_currency_code,
            primary_currency_symbol=primary_currency_symbol,
            primary_currency_decimal_places=primary_currency_decimal_places,
            spent=spent,
            pc_spent=pc_spent,
            earned=earned,
            pc_earned=pc_earned,
            transferred=transferred,
            pc_transferred=pc_transferred,
        )

        category_properties.additional_properties = d
        return category_properties

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
