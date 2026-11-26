from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TrackerStateConnectionType0Settings")


@_attrs_define
class TrackerStateConnectionType0Settings:
    """
    Attributes:
        auto_sync_enabled (bool):
        spoiler_guard_enabled (bool):
        hide_plan_to_watch (bool):
    """

    auto_sync_enabled: bool
    spoiler_guard_enabled: bool
    hide_plan_to_watch: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_sync_enabled = self.auto_sync_enabled

        spoiler_guard_enabled = self.spoiler_guard_enabled

        hide_plan_to_watch = self.hide_plan_to_watch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "autoSyncEnabled": auto_sync_enabled,
                "spoilerGuardEnabled": spoiler_guard_enabled,
                "hidePlanToWatch": hide_plan_to_watch,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        auto_sync_enabled = _src.pop("autoSyncEnabled")

        spoiler_guard_enabled = _src.pop("spoilerGuardEnabled")

        hide_plan_to_watch = _src.pop("hidePlanToWatch")

        tracker_state_connection_type_0_settings = cls(
            auto_sync_enabled=auto_sync_enabled,
            spoiler_guard_enabled=spoiler_guard_enabled,
            hide_plan_to_watch=hide_plan_to_watch,
        )

        tracker_state_connection_type_0_settings.additional_properties = _src
        return tracker_state_connection_type_0_settings

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
