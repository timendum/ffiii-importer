from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.object_link_0 import ObjectLink0


T = TypeVar("T", bound="ObjectLink")


@_attrs_define
class ObjectLink:
    """
    Attributes:
        self_ (Union[Unset, str]):  Example: https://demo.firefly-iii.org/api/v1/OBJECTS/1.
        field_0 (Union[Unset, ObjectLink0]):
    """

    self_: Union[Unset, str] = UNSET
    field_0: Union[Unset, "ObjectLink0"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        self_ = self.self_

        field_0: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.field_0, Unset):
            field_0 = self.field_0.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if self_ is not UNSET:
            field_dict["self"] = self_
        if field_0 is not UNSET:
            field_dict["0"] = field_0

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_link_0 import ObjectLink0

        d = dict(src_dict)
        self_ = d.pop("self", UNSET)

        _field_0 = d.pop("0", UNSET)
        field_0: Union[Unset, ObjectLink0]
        if isinstance(_field_0, Unset):
            field_0 = UNSET
        else:
            field_0 = ObjectLink0.from_dict(_field_0)

        object_link = cls(
            self_=self_,
            field_0=field_0,
        )

        object_link.additional_properties = d
        return object_link

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
