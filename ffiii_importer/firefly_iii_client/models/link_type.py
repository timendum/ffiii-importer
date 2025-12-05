from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkType")


@_attrs_define
class LinkType:
    """
    Attributes:
        name (str):  Example: Paid.
        inward (str):  Example: is (partially) paid for by.
        outward (str):  Example: (partially) pays for.
        editable (Union[Unset, bool]):
    """

    name: str
    inward: str
    outward: str
    editable: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        inward = self.inward

        outward = self.outward

        editable = self.editable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "inward": inward,
                "outward": outward,
            }
        )
        if editable is not UNSET:
            field_dict["editable"] = editable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        inward = d.pop("inward")

        outward = d.pop("outward")

        editable = d.pop("editable", UNSET)

        link_type = cls(
            name=name,
            inward=inward,
            outward=outward,
            editable=editable,
        )

        link_type.additional_properties = d
        return link_type

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
