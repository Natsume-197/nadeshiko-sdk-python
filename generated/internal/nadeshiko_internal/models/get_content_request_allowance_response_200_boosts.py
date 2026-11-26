from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetContentRequestAllowanceResponse200Boosts")


@_attrs_define
class GetContentRequestAllowanceResponse200Boosts:
    """
    Attributes:
        per_month (int):
        used (int):
        remaining (int):
        resets_at (datetime.datetime):
    """

    per_month: int
    used: int
    remaining: int
    resets_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        per_month = self.per_month

        used = self.used

        remaining = self.remaining

        resets_at = self.resets_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "perMonth": per_month,
                "used": used,
                "remaining": remaining,
                "resetsAt": resets_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        per_month = _src.pop("perMonth")

        used = _src.pop("used")

        remaining = _src.pop("remaining")

        resets_at = datetime.datetime.fromisoformat(_src.pop("resetsAt"))

        get_content_request_allowance_response_200_boosts = cls(
            per_month=per_month,
            used=used,
            remaining=remaining,
            resets_at=resets_at,
        )

        get_content_request_allowance_response_200_boosts.additional_properties = _src
        return get_content_request_allowance_response_200_boosts

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
