from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkTypeUpdate")


@_attrs_define
class LinkTypeUpdate:
    """
    Attributes:
        name (Union[Unset, str]):  Example: Paid.
        inward (Union[Unset, str]):  Example: is (partially) paid for by.
        outward (Union[Unset, str]):  Example: (partially) pays for.
    """

    name: Union[Unset, str] = UNSET
    inward: Union[Unset, str] = UNSET
    outward: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        inward = self.inward

        outward = self.outward

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if inward is not UNSET:
            field_dict["inward"] = inward
        if outward is not UNSET:
            field_dict["outward"] = outward

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        inward = d.pop("inward", UNSET)

        outward = d.pop("outward", UNSET)

        link_type_update = cls(
            name=name,
            inward=inward,
            outward=outward,
        )

        link_type_update.additional_properties = d
        return link_type_update

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
