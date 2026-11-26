from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminOverviewEmails")


@_attrs_define
class AdminOverviewEmails:
    """
    Attributes:
        failed (int): Sends that failed in the last 24 hours. Example: 0.
        bounced (int): Bounces and complaints reported in the last 24 hours. Example: 1.
    """

    failed: int
    bounced: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        failed = self.failed

        bounced = self.bounced

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "failed": failed,
                "bounced": bounced,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        failed = _src.pop("failed")

        bounced = _src.pop("bounced")

        admin_overview_emails = cls(
            failed=failed,
            bounced=bounced,
        )

        admin_overview_emails.additional_properties = _src
        return admin_overview_emails

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
