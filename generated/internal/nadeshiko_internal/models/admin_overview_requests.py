from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminOverviewRequests")


@_attrs_define
class AdminOverviewRequests:
    """
    Attributes:
        open_ (int): Content requests waiting in OPEN status. Example: 12.
        boosted_open (int): Open content requests that have at least one patron boost. Example: 3.
    """

    open_: int
    boosted_open: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        open_ = self.open_

        boosted_open = self.boosted_open

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "open": open_,
                "boostedOpen": boosted_open,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        open_ = _src.pop("open")

        boosted_open = _src.pop("boostedOpen")

        admin_overview_requests = cls(
            open_=open_,
            boosted_open=boosted_open,
        )

        admin_overview_requests.additional_properties = _src
        return admin_overview_requests

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
