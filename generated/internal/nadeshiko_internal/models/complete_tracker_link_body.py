from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.complete_tracker_link_body_provider import (
    CompleteTrackerLinkBodyProvider,
    check_complete_tracker_link_body_provider,
)

T = TypeVar("T", bound="CompleteTrackerLinkBody")


@_attrs_define
class CompleteTrackerLinkBody:
    """
    Attributes:
        provider (CompleteTrackerLinkBodyProvider):
        code (str):
        state (str):
    """

    provider: CompleteTrackerLinkBodyProvider
    code: str
    state: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: str = self.provider

        code = self.code

        state = self.state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "code": code,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        provider = check_complete_tracker_link_body_provider(_src.pop("provider"))

        code = _src.pop("code")

        state = _src.pop("state")

        complete_tracker_link_body = cls(
            provider=provider,
            code=code,
            state=state,
        )

        complete_tracker_link_body.additional_properties = _src
        return complete_tracker_link_body

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
