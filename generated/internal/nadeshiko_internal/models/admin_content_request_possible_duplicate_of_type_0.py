from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_content_request_possible_duplicate_of_type_0_status import (
    AdminContentRequestPossibleDuplicateOfType0Status,
    check_admin_content_request_possible_duplicate_of_type_0_status,
)

T = TypeVar("T", bound="AdminContentRequestPossibleDuplicateOfType0")


@_attrs_define
class AdminContentRequestPossibleDuplicateOfType0:
    """An active request with the same title, flagged for review; never merged automatically.

    Attributes:
        id (UUID):
        title (str):
        status (AdminContentRequestPossibleDuplicateOfType0Status):
    """

    id: UUID
    title: str
    status: AdminContentRequestPossibleDuplicateOfType0Status
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        title = self.title

        status: str = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = UUID(_src.pop("id"))

        title = _src.pop("title")

        status = check_admin_content_request_possible_duplicate_of_type_0_status(_src.pop("status"))

        admin_content_request_possible_duplicate_of_type_0 = cls(
            id=id,
            title=title,
            status=status,
        )

        admin_content_request_possible_duplicate_of_type_0.additional_properties = _src
        return admin_content_request_possible_duplicate_of_type_0

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
