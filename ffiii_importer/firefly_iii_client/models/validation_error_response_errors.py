from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ValidationErrorResponseErrors")


@_attrs_define
class ValidationErrorResponseErrors:
    """
    Attributes:
        email (Union[Unset, list[str]]):
        force (Union[Unset, list[str]]):
        blocked (Union[Unset, list[str]]):
        field (Union[Unset, list[str]]):
        role (Union[Unset, list[str]]):
        blocked_code (Union[Unset, list[str]]):
        name (Union[Unset, list[str]]):
        type_ (Union[Unset, list[str]]):
        iban (Union[Unset, list[str]]):
        start (Union[Unset, list[str]]):
        end (Union[Unset, list[str]]):
        date (Union[Unset, list[str]]):
    """

    email: Union[Unset, list[str]] = UNSET
    force: Union[Unset, list[str]] = UNSET
    blocked: Union[Unset, list[str]] = UNSET
    field: Union[Unset, list[str]] = UNSET
    role: Union[Unset, list[str]] = UNSET
    blocked_code: Union[Unset, list[str]] = UNSET
    name: Union[Unset, list[str]] = UNSET
    type_: Union[Unset, list[str]] = UNSET
    iban: Union[Unset, list[str]] = UNSET
    start: Union[Unset, list[str]] = UNSET
    end: Union[Unset, list[str]] = UNSET
    date: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: Union[Unset, list[str]] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email

        force: Union[Unset, list[str]] = UNSET
        if not isinstance(self.force, Unset):
            force = self.force

        blocked: Union[Unset, list[str]] = UNSET
        if not isinstance(self.blocked, Unset):
            blocked = self.blocked

        field: Union[Unset, list[str]] = UNSET
        if not isinstance(self.field, Unset):
            field = self.field

        role: Union[Unset, list[str]] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role

        blocked_code: Union[Unset, list[str]] = UNSET
        if not isinstance(self.blocked_code, Unset):
            blocked_code = self.blocked_code

        name: Union[Unset, list[str]] = UNSET
        if not isinstance(self.name, Unset):
            name = self.name

        type_: Union[Unset, list[str]] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        iban: Union[Unset, list[str]] = UNSET
        if not isinstance(self.iban, Unset):
            iban = self.iban

        start: Union[Unset, list[str]] = UNSET
        if not isinstance(self.start, Unset):
            start = self.start

        end: Union[Unset, list[str]] = UNSET
        if not isinstance(self.end, Unset):
            end = self.end

        date: Union[Unset, list[str]] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if force is not UNSET:
            field_dict["force"] = force
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if field is not UNSET:
            field_dict["field"] = field
        if role is not UNSET:
            field_dict["role"] = role
        if blocked_code is not UNSET:
            field_dict["blocked_code"] = blocked_code
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if iban is not UNSET:
            field_dict["iban"] = iban
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if date is not UNSET:
            field_dict["date"] = date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = cast(list[str], d.pop("email", UNSET))

        force = cast(list[str], d.pop("force", UNSET))

        blocked = cast(list[str], d.pop("blocked", UNSET))

        field = cast(list[str], d.pop("field", UNSET))

        role = cast(list[str], d.pop("role", UNSET))

        blocked_code = cast(list[str], d.pop("blocked_code", UNSET))

        name = cast(list[str], d.pop("name", UNSET))

        type_ = cast(list[str], d.pop("type", UNSET))

        iban = cast(list[str], d.pop("iban", UNSET))

        start = cast(list[str], d.pop("start", UNSET))

        end = cast(list[str], d.pop("end", UNSET))

        date = cast(list[str], d.pop("date", UNSET))

        validation_error_response_errors = cls(
            email=email,
            force=force,
            blocked=blocked,
            field=field,
            role=role,
            blocked_code=blocked_code,
            name=name,
            type_=type_,
            iban=iban,
            start=start,
            end=end,
            date=date,
        )

        validation_error_response_errors.additional_properties = d
        return validation_error_response_errors

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
