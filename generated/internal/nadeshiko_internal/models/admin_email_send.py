from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_email_send_source import AdminEmailSendSource, check_admin_email_send_source
from ..models.admin_email_send_status import AdminEmailSendStatus, check_admin_email_send_status

T = TypeVar("T", bound="AdminEmailSend")


@_attrs_define
class AdminEmailSend:
    """One email the site sent, tried to send, or refused to send.

    Attributes:
        id (int):  Example: 1203.
        sent_at (datetime.datetime):
        address (str):  Example: reader@example.com.
        user_id (int | None):  Example: 42.
        username (None | str): The account's username when the send is tied to one.
        kind (str):  Example: magic-link.
        campaign (None | str):  Example: dormant-30-2026-11.
        subject (None | str): Null on rows rebuilt from older tables that never stored it.
        status (AdminEmailSendStatus): `failed` and `suppressed` never left. A message that left is `sent` until SES
            reports it
            `delivered`, `bounced` or `complained`.
        error (None | str): Why sending failed.
        ses_message_id (None | str):
        source (AdminEmailSendSource): `backfill` rows were rebuilt from older tables when the log started.
        resendable (bool): Whether the admin view can send this again (sign-in links, and welcomes tied to an account).
    """

    id: int
    sent_at: datetime.datetime
    address: str
    user_id: int | None
    username: None | str
    kind: str
    campaign: None | str
    subject: None | str
    status: AdminEmailSendStatus
    error: None | str
    ses_message_id: None | str
    source: AdminEmailSendSource
    resendable: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sent_at = self.sent_at.isoformat()

        address = self.address

        user_id: int | None
        user_id = self.user_id

        username: None | str
        username = self.username

        kind = self.kind

        campaign: None | str
        campaign = self.campaign

        subject: None | str
        subject = self.subject

        status: str = self.status

        error: None | str
        error = self.error

        ses_message_id: None | str
        ses_message_id = self.ses_message_id

        source: str = self.source

        resendable = self.resendable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sentAt": sent_at,
                "address": address,
                "userId": user_id,
                "username": username,
                "kind": kind,
                "campaign": campaign,
                "subject": subject,
                "status": status,
                "error": error,
                "sesMessageId": ses_message_id,
                "source": source,
                "resendable": resendable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        sent_at = datetime.datetime.fromisoformat(_src.pop("sentAt"))

        address = _src.pop("address")

        def _parse_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        user_id = _parse_user_id(_src.pop("userId"))

        def _parse_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        username = _parse_username(_src.pop("username"))

        kind = _src.pop("kind")

        def _parse_campaign(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        campaign = _parse_campaign(_src.pop("campaign"))

        def _parse_subject(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        subject = _parse_subject(_src.pop("subject"))

        status = check_admin_email_send_status(_src.pop("status"))

        def _parse_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error = _parse_error(_src.pop("error"))

        def _parse_ses_message_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ses_message_id = _parse_ses_message_id(_src.pop("sesMessageId"))

        source = check_admin_email_send_source(_src.pop("source"))

        resendable = _src.pop("resendable")

        admin_email_send = cls(
            id=id,
            sent_at=sent_at,
            address=address,
            user_id=user_id,
            username=username,
            kind=kind,
            campaign=campaign,
            subject=subject,
            status=status,
            error=error,
            ses_message_id=ses_message_id,
            source=source,
            resendable=resendable,
        )

        admin_email_send.additional_properties = _src
        return admin_email_send

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
