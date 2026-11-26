from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RefreshAllAdminPatreonConnectionsResponse200")


@_attrs_define
class RefreshAllAdminPatreonConnectionsResponse200:
    """
    Attributes:
        checked (int):
        failed (int):
    """

    checked: int
    failed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checked = self.checked

        failed = self.failed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "checked": checked,
                "failed": failed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        checked = _src.pop("checked")

        failed = _src.pop("failed")

        refresh_all_admin_patreon_connections_response_200 = cls(
            checked=checked,
            failed=failed,
        )

        refresh_all_admin_patreon_connections_response_200.additional_properties = _src
        return refresh_all_admin_patreon_connections_response_200

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
