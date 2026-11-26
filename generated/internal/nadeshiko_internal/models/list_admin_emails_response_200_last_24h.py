from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ListAdminEmailsResponse200Last24H")


@_attrs_define
class ListAdminEmailsResponse200Last24H:
    """
    Attributes:
        sent (int):
        failed (int):
        bounced (int): Bounces and complaints
        suppressed (int):
    """

    sent: int
    failed: int
    bounced: int
    suppressed: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sent = self.sent

        failed = self.failed

        bounced = self.bounced

        suppressed = self.suppressed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sent": sent,
                "failed": failed,
                "bounced": bounced,
                "suppressed": suppressed,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        sent = _src.pop("sent")

        failed = _src.pop("failed")

        bounced = _src.pop("bounced")

        suppressed = _src.pop("suppressed")

        list_admin_emails_response_200_last_24h = cls(
            sent=sent,
            failed=failed,
            bounced=bounced,
            suppressed=suppressed,
        )

        list_admin_emails_response_200_last_24h.additional_properties = _src
        return list_admin_emails_response_200_last_24h

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
