from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MetaPagination")


@_attrs_define
class MetaPagination:
    """
    Attributes:
        total (Union[Unset, int]):  Example: 3.
        count (Union[Unset, int]):  Example: 20.
        per_page (Union[Unset, int]):  Example: 100.
        current_page (Union[Unset, int]):  Example: 1.
        total_pages (Union[Unset, int]):  Example: 1.
    """

    total: Union[Unset, int] = UNSET
    count: Union[Unset, int] = UNSET
    per_page: Union[Unset, int] = UNSET
    current_page: Union[Unset, int] = UNSET
    total_pages: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        count = self.count

        per_page = self.per_page

        current_page = self.current_page

        total_pages = self.total_pages

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total is not UNSET:
            field_dict["total"] = total
        if count is not UNSET:
            field_dict["count"] = count
        if per_page is not UNSET:
            field_dict["per_page"] = per_page
        if current_page is not UNSET:
            field_dict["current_page"] = current_page
        if total_pages is not UNSET:
            field_dict["total_pages"] = total_pages

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        count = d.pop("count", UNSET)

        per_page = d.pop("per_page", UNSET)

        current_page = d.pop("current_page", UNSET)

        total_pages = d.pop("total_pages", UNSET)

        meta_pagination = cls(
            total=total,
            count=count,
            per_page=per_page,
            current_page=current_page,
            total_pages=total_pages,
        )

        meta_pagination.additional_properties = d
        return meta_pagination

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
