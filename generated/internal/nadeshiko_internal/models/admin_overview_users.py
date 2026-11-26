from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminOverviewUsers")


@_attrs_define
class AdminOverviewUsers:
    """
    Attributes:
        total (int): Active (non-deleted) user accounts. Example: 1420.
        active_patrons (int): Linked Patreon accounts with an active paid membership. Example: 7.
    """

    total: int
    active_patrons: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        active_patrons = self.active_patrons

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "activePatrons": active_patrons,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        total = _src.pop("total")

        active_patrons = _src.pop("activePatrons")

        admin_overview_users = cls(
            total=total,
            active_patrons=active_patrons,
        )

        admin_overview_users.additional_properties = _src
        return admin_overview_users

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
