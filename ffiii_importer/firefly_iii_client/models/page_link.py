from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PageLink")


@_attrs_define
class PageLink:
    """
    Attributes:
        self_ (Union[Unset, str]):  Example: https://demo.firefly-iii.org/api/v1/OBJECT?&page=4.
        first (Union[Unset, str]):  Example: https://demo.firefly-iii.org/api/v1/OBJECT?&page=1.
        next_ (Union[None, Unset, str]):  Example: https://demo.firefly-iii.org/api/v1/OBJECT?&page=3.
        prev (Union[None, Unset, str]):  Example: https://demo.firefly-iii.org/api/v1/OBJECT?&page=2.
        last (Union[Unset, str]):  Example: https://demo.firefly-iii.org/api/v1/OBJECT?&page=12.
    """

    self_: Union[Unset, str] = UNSET
    first: Union[Unset, str] = UNSET
    next_: Union[None, Unset, str] = UNSET
    prev: Union[None, Unset, str] = UNSET
    last: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_

        first = self.first

        next_: Union[None, Unset, str]
        if isinstance(self.next_, Unset):
            next_ = UNSET
        else:
            next_ = self.next_

        prev: Union[None, Unset, str]
        if isinstance(self.prev, Unset):
            prev = UNSET
        else:
            prev = self.prev

        last = self.last

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if first is not UNSET:
            field_dict["first"] = first
        if next_ is not UNSET:
            field_dict["next"] = next_
        if prev is not UNSET:
            field_dict["prev"] = prev
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        self_ = d.pop("self", UNSET)

        first = d.pop("first", UNSET)

        def _parse_next_(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        next_ = _parse_next_(d.pop("next", UNSET))

        def _parse_prev(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        prev = _parse_prev(d.pop("prev", UNSET))

        last = d.pop("last", UNSET)

        page_link = cls(
            self_=self_,
            first=first,
            next_=next_,
            prev=prev,
            last=last,
        )

        page_link.additional_properties = d
        return page_link

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
