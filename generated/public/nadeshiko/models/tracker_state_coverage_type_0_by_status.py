from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TrackerStateCoverageType0ByStatus")


@_attrs_define
class TrackerStateCoverageType0ByStatus:
    """
    Attributes:
        watching (int):
        completed (int):
        paused (int):
        dropped (int):
        planning (int):
    """

    watching: int
    completed: int
    paused: int
    dropped: int
    planning: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        watching = self.watching

        completed = self.completed

        paused = self.paused

        dropped = self.dropped

        planning = self.planning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "WATCHING": watching,
                "COMPLETED": completed,
                "PAUSED": paused,
                "DROPPED": dropped,
                "PLANNING": planning,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        watching = _src.pop("WATCHING")

        completed = _src.pop("COMPLETED")

        paused = _src.pop("PAUSED")

        dropped = _src.pop("DROPPED")

        planning = _src.pop("PLANNING")

        tracker_state_coverage_type_0_by_status = cls(
            watching=watching,
            completed=completed,
            paused=paused,
            dropped=dropped,
            planning=planning,
        )

        tracker_state_coverage_type_0_by_status.additional_properties = _src
        return tracker_state_coverage_type_0_by_status

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
