from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.start_tracker_link_body_provider import (
    StartTrackerLinkBodyProvider,
    check_start_tracker_link_body_provider,
)

T = TypeVar("T", bound="StartTrackerLinkBody")


@_attrs_define
class StartTrackerLinkBody:
    """
    Attributes:
        provider (StartTrackerLinkBodyProvider):
    """

    provider: StartTrackerLinkBodyProvider
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: str = self.provider

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        provider = check_start_tracker_link_body_provider(_src.pop("provider"))

        start_tracker_link_body = cls(
            provider=provider,
        )

        start_tracker_link_body.additional_properties = _src
        return start_tracker_link_body

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
