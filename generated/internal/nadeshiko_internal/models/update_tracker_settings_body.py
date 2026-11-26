from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateTrackerSettingsBody")


@_attrs_define
class UpdateTrackerSettingsBody:
    """
    Attributes:
        auto_sync_enabled (bool | Unset):
        spoiler_guard_enabled (bool | Unset):
        hide_plan_to_watch (bool | Unset):
    """

    auto_sync_enabled: bool | Unset = UNSET
    spoiler_guard_enabled: bool | Unset = UNSET
    hide_plan_to_watch: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        auto_sync_enabled = self.auto_sync_enabled

        spoiler_guard_enabled = self.spoiler_guard_enabled

        hide_plan_to_watch = self.hide_plan_to_watch

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_sync_enabled is not UNSET:
            field_dict["autoSyncEnabled"] = auto_sync_enabled
        if spoiler_guard_enabled is not UNSET:
            field_dict["spoilerGuardEnabled"] = spoiler_guard_enabled
        if hide_plan_to_watch is not UNSET:
            field_dict["hidePlanToWatch"] = hide_plan_to_watch

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        auto_sync_enabled = _src.pop("autoSyncEnabled", UNSET)

        spoiler_guard_enabled = _src.pop("spoilerGuardEnabled", UNSET)

        hide_plan_to_watch = _src.pop("hidePlanToWatch", UNSET)

        update_tracker_settings_body = cls(
            auto_sync_enabled=auto_sync_enabled,
            spoiler_guard_enabled=spoiler_guard_enabled,
            hide_plan_to_watch=hide_plan_to_watch,
        )

        update_tracker_settings_body.additional_properties = _src
        return update_tracker_settings_body

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
