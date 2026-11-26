from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminEmailEvent")


@_attrs_define
class AdminEmailEvent:
    """One event SES reported for a message.

    Attributes:
        id (int):
        event (str):  Example: hard_bounce.
        occurred_at (datetime.datetime):
        reason (None | str):
        diagnostic_message (None | str):  Example: 550 5.1.1 User unknown.
    """

    id: int
    event: str
    occurred_at: datetime.datetime
    reason: None | str
    diagnostic_message: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        event = self.event

        occurred_at = self.occurred_at.isoformat()

        reason: None | str
        reason = self.reason

        diagnostic_message: None | str
        diagnostic_message = self.diagnostic_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "event": event,
                "occurredAt": occurred_at,
                "reason": reason,
                "diagnosticMessage": diagnostic_message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        event = _src.pop("event")

        occurred_at = datetime.datetime.fromisoformat(_src.pop("occurredAt"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(_src.pop("reason"))

        def _parse_diagnostic_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        diagnostic_message = _parse_diagnostic_message(_src.pop("diagnosticMessage"))

        admin_email_event = cls(
            id=id,
            event=event,
            occurred_at=occurred_at,
            reason=reason,
            diagnostic_message=diagnostic_message,
        )

        admin_email_event.additional_properties = _src
        return admin_email_event

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
