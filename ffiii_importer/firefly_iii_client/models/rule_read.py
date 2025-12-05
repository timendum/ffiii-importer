from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.object_link import ObjectLink
    from ..models.rule import Rule


T = TypeVar("T", bound="RuleRead")


@_attrs_define
class RuleRead:
    """
    Attributes:
        type_ (str): Immutable value Example: rules.
        id (str):  Example: 2.
        attributes (Rule):
        links (ObjectLink):
    """

    type_: str
    id: str
    attributes: "Rule"
    links: "ObjectLink"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        attributes = self.attributes.to_dict()

        links = self.links.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "attributes": attributes,
                "links": links,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.object_link import ObjectLink
        from ..models.rule import Rule

        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id")

        attributes = Rule.from_dict(d.pop("attributes"))

        links = ObjectLink.from_dict(d.pop("links"))

        rule_read = cls(
            type_=type_,
            id=id,
            attributes=attributes,
            links=links,
        )

        rule_read.additional_properties = d
        return rule_read

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
