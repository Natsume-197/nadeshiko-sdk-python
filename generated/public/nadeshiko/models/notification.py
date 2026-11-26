from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_kind import NotificationKind, check_notification_kind

if TYPE_CHECKING:
    from ..models.notification_payload import NotificationPayload


T = TypeVar("T", bound="Notification")


@_attrs_define
class Notification:
    """One entry in the reader's notification centre (the bell).

    Attributes:
        id (UUID):
        kind (NotificationKind): `word-available`: watched words that started returning sentences.
            `word-digest`: new sentences for followed words this week.
            `request-update`: a content request the reader backed started or shipped.
        payload (NotificationPayload): What the site needs to draw the entry. Word kinds carry `words`, a list of
            `{ query, matchMode, titles, sentences | newSentences }` (the site builds the
            link from the query and match mode); `request-update` carries
            `{ status, title, path }`.
        read (bool):
        created_at (datetime.datetime):
    """

    id: UUID
    kind: NotificationKind
    payload: NotificationPayload
    read: bool
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        kind: str = self.kind

        payload = self.payload.to_dict()

        read = self.read

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
                "payload": payload,
                "read": read,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_payload import NotificationPayload  # noqa: PLC0415

        _src = dict(src_dict)
        id = UUID(_src.pop("id"))

        kind = check_notification_kind(_src.pop("kind"))

        payload = NotificationPayload.from_dict(_src.pop("payload"))

        read = _src.pop("read")

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        notification = cls(
            id=id,
            kind=kind,
            payload=payload,
            read=read,
            created_at=created_at,
        )

        notification.additional_properties = _src
        return notification

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
