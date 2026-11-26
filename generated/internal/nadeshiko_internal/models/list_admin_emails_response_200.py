from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_email_send import AdminEmailSend
    from ..models.list_admin_emails_response_200_last_24h import ListAdminEmailsResponse200Last24H


T = TypeVar("T", bound="ListAdminEmailsResponse200")


@_attrs_define
class ListAdminEmailsResponse200:
    """
    Attributes:
        emails (list[AdminEmailSend]):
        total (int): Sends matching the filters
        last24h (ListAdminEmailsResponse200Last24H):
    """

    emails: list[AdminEmailSend]
    total: int
    last24h: ListAdminEmailsResponse200Last24H
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        emails = []
        for emails_item_data in self.emails:
            emails_item = emails_item_data.to_dict()
            emails.append(emails_item)

        total = self.total

        last24h = self.last24h.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "emails": emails,
                "total": total,
                "last24h": last24h,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_email_send import AdminEmailSend  # noqa: PLC0415
        from ..models.list_admin_emails_response_200_last_24h import (
            ListAdminEmailsResponse200Last24H,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        emails = []
        _emails = _src.pop("emails")
        for emails_item_data in _emails:
            emails_item = AdminEmailSend.from_dict(emails_item_data)

            emails.append(emails_item)

        total = _src.pop("total")

        last24h = ListAdminEmailsResponse200Last24H.from_dict(_src.pop("last24h"))

        list_admin_emails_response_200 = cls(
            emails=emails,
            total=total,
            last24h=last24h,
        )

        list_admin_emails_response_200.additional_properties = _src
        return list_admin_emails_response_200

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
