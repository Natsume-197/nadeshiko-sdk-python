from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesSiteNotifications")


@_attrs_define
class UserPreferencesSiteNotifications:
    """The site channel of the notification centre (the bell), per category.
    Absent means on. Email has its own switches in `productEmails`.

        Attributes:
            words (bool | Unset):
            requests (bool | Unset):
    """

    words: bool | Unset = UNSET
    requests: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        words = self.words

        requests = self.requests

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if words is not UNSET:
            field_dict["words"] = words
        if requests is not UNSET:
            field_dict["requests"] = requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        words = _src.pop("words", UNSET)

        requests = _src.pop("requests", UNSET)

        user_preferences_site_notifications = cls(
            words=words,
            requests=requests,
        )

        user_preferences_site_notifications.additional_properties = _src
        return user_preferences_site_notifications

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
