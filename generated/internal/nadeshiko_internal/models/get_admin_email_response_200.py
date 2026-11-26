from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_email_event import AdminEmailEvent
    from ..models.admin_email_send import AdminEmailSend


T = TypeVar("T", bound="GetAdminEmailResponse200")


@_attrs_define
class GetAdminEmailResponse200:
    """
    Attributes:
        email (AdminEmailSend): One email the site sent, tried to send, or refused to send.
        events (list[AdminEmailEvent]):
    """

    email: AdminEmailSend
    events: list[AdminEmailEvent]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email.to_dict()

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "events": events,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_email_event import AdminEmailEvent  # noqa: PLC0415
        from ..models.admin_email_send import AdminEmailSend  # noqa: PLC0415

        _src = dict(src_dict)
        email = AdminEmailSend.from_dict(_src.pop("email"))

        events = []
        _events = _src.pop("events")
        for events_item_data in _events:
            events_item = AdminEmailEvent.from_dict(events_item_data)

            events.append(events_item)

        get_admin_email_response_200 = cls(
            email=email,
            events=events,
        )

        get_admin_email_response_200.additional_properties = _src
        return get_admin_email_response_200

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
