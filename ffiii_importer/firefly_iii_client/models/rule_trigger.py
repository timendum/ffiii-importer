import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.rule_trigger_keyword import RuleTriggerKeyword
from ..types import UNSET, Unset

T = TypeVar("T", bound="RuleTrigger")


@_attrs_define
class RuleTrigger:
    """
    Attributes:
        type_ (RuleTriggerKeyword): The type of thing this trigger responds to. A limited set is possible Example:
            user_action.
        value (str): The accompanying value the trigger responds to. This value is often mandatory, but this depends on
            the trigger. Example: tag1.
        id (Union[Unset, str]):  Example: 2.
        created_at (Union[Unset, datetime.datetime]):  Example: 2025-10-01T00:00:00+00:00.
        updated_at (Union[Unset, datetime.datetime]):  Example: 2025-10-01T00:00:00+00:00.
        prohibited (Union[Unset, bool]): If 'prohibited' is true, this rule trigger will be negated. 'Description is'
            will become 'Description is NOT' etc. Default: False.
        order (Union[Unset, int]): Order of the trigger Example: 5.
        active (Union[Unset, bool]): If the trigger is active. Defaults to true. Default: True. Example: True.
        stop_processing (Union[Unset, bool]): When true, other triggers will not be checked if this trigger was
            triggered. Defaults to false. Default: False.
    """

    type_: RuleTriggerKeyword
    value: str
    id: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    updated_at: Union[Unset, datetime.datetime] = UNSET
    prohibited: Union[Unset, bool] = False
    order: Union[Unset, int] = UNSET
    active: Union[Unset, bool] = True
    stop_processing: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        value = self.value

        id = self.id

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at: Union[Unset, str] = UNSET
        if not isinstance(self.updated_at, Unset):
            updated_at = self.updated_at.isoformat()

        prohibited = self.prohibited

        order = self.order

        active = self.active

        stop_processing = self.stop_processing

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "value": value,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if prohibited is not UNSET:
            field_dict["prohibited"] = prohibited
        if order is not UNSET:
            field_dict["order"] = order
        if active is not UNSET:
            field_dict["active"] = active
        if stop_processing is not UNSET:
            field_dict["stop_processing"] = stop_processing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = RuleTriggerKeyword(d.pop("type"))

        value = d.pop("value")

        id = d.pop("id", UNSET)

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

        prohibited = d.pop("prohibited", UNSET)

        order = d.pop("order", UNSET)

        active = d.pop("active", UNSET)

        stop_processing = d.pop("stop_processing", UNSET)

        rule_trigger = cls(
            type_=type_,
            value=value,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            prohibited=prohibited,
            order=order,
            active=active,
            stop_processing=stop_processing,
        )

        rule_trigger.additional_properties = d
        return rule_trigger

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
