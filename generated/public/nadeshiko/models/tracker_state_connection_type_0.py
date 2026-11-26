from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_state_connection_type_0_provider import (
    TrackerStateConnectionType0Provider,
    check_tracker_state_connection_type_0_provider,
)

if TYPE_CHECKING:
    from ..models.tracker_state_connection_type_0_effective_settings import (
        TrackerStateConnectionType0EffectiveSettings,
    )
    from ..models.tracker_state_connection_type_0_settings import (
        TrackerStateConnectionType0Settings,
    )


T = TypeVar("T", bound="TrackerStateConnectionType0")


@_attrs_define
class TrackerStateConnectionType0:
    """
    Attributes:
        provider (TrackerStateConnectionType0Provider):
        external_username (None | str):
        supports_custom_lists (bool):
        last_synced_at (datetime.datetime | None):
        last_sync_error (None | str):
        linked_at (datetime.datetime):
        settings (TrackerStateConnectionType0Settings):
        effective_settings (TrackerStateConnectionType0EffectiveSettings):
        next_manual_sync_at (datetime.datetime | None):
        manual_cooldown_seconds (int):
    """

    provider: TrackerStateConnectionType0Provider
    external_username: None | str
    supports_custom_lists: bool
    last_synced_at: datetime.datetime | None
    last_sync_error: None | str
    linked_at: datetime.datetime
    settings: TrackerStateConnectionType0Settings
    effective_settings: TrackerStateConnectionType0EffectiveSettings
    next_manual_sync_at: datetime.datetime | None
    manual_cooldown_seconds: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        provider: str = self.provider

        external_username: None | str
        external_username = self.external_username

        supports_custom_lists = self.supports_custom_lists

        last_synced_at: None | str
        if isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        last_sync_error: None | str
        last_sync_error = self.last_sync_error

        linked_at = self.linked_at.isoformat()

        settings = self.settings.to_dict()

        effective_settings = self.effective_settings.to_dict()

        next_manual_sync_at: None | str
        if isinstance(self.next_manual_sync_at, datetime.datetime):
            next_manual_sync_at = self.next_manual_sync_at.isoformat()
        else:
            next_manual_sync_at = self.next_manual_sync_at

        manual_cooldown_seconds = self.manual_cooldown_seconds

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "provider": provider,
                "externalUsername": external_username,
                "supportsCustomLists": supports_custom_lists,
                "lastSyncedAt": last_synced_at,
                "lastSyncError": last_sync_error,
                "linkedAt": linked_at,
                "settings": settings,
                "effectiveSettings": effective_settings,
                "nextManualSyncAt": next_manual_sync_at,
                "manualCooldownSeconds": manual_cooldown_seconds,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracker_state_connection_type_0_effective_settings import (
            TrackerStateConnectionType0EffectiveSettings,  # noqa: PLC0415
        )
        from ..models.tracker_state_connection_type_0_settings import (
            TrackerStateConnectionType0Settings,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        provider = check_tracker_state_connection_type_0_provider(_src.pop("provider"))

        def _parse_external_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        external_username = _parse_external_username(_src.pop("externalUsername"))

        supports_custom_lists = _src.pop("supportsCustomLists")

        def _parse_last_synced_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_synced_at = _parse_last_synced_at(_src.pop("lastSyncedAt"))

        def _parse_last_sync_error(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_sync_error = _parse_last_sync_error(_src.pop("lastSyncError"))

        linked_at = datetime.datetime.fromisoformat(_src.pop("linkedAt"))

        settings = TrackerStateConnectionType0Settings.from_dict(_src.pop("settings"))

        effective_settings = TrackerStateConnectionType0EffectiveSettings.from_dict(
            _src.pop("effectiveSettings")
        )

        def _parse_next_manual_sync_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                next_manual_sync_at_type_0 = datetime.datetime.fromisoformat(data)

                return next_manual_sync_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        next_manual_sync_at = _parse_next_manual_sync_at(_src.pop("nextManualSyncAt"))

        manual_cooldown_seconds = _src.pop("manualCooldownSeconds")

        tracker_state_connection_type_0 = cls(
            provider=provider,
            external_username=external_username,
            supports_custom_lists=supports_custom_lists,
            last_synced_at=last_synced_at,
            last_sync_error=last_sync_error,
            linked_at=linked_at,
            settings=settings,
            effective_settings=effective_settings,
            next_manual_sync_at=next_manual_sync_at,
            manual_cooldown_seconds=manual_cooldown_seconds,
        )

        tracker_state_connection_type_0.additional_properties = _src
        return tracker_state_connection_type_0

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
