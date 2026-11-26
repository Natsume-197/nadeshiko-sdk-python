from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_state_configured_providers_item import (
    TrackerStateConfiguredProvidersItem,
    check_tracker_state_configured_providers_item,
)

if TYPE_CHECKING:
    from ..models.tracker_state_connection_type_0 import TrackerStateConnectionType0
    from ..models.tracker_state_coverage_type_0 import TrackerStateCoverageType0
    from ..models.tracker_state_entries_item import TrackerStateEntriesItem
    from ..models.tracker_state_missing_anime_item import TrackerStateMissingAnimeItem


T = TypeVar("T", bound="TrackerState")


@_attrs_define
class TrackerState:
    """Provider-agnostic anime tracker connection, catalog coverage, and resolved search filter entries.

    Attributes:
        configured_providers (list[TrackerStateConfiguredProvidersItem]):
        can_use_patron_perks (bool):
        connection (None | TrackerStateConnectionType0):
        coverage (None | TrackerStateCoverageType0):
        custom_lists (list[str]):
        custom_list_count (int):
        entries (list[TrackerStateEntriesItem]):
        missing_anime (list[TrackerStateMissingAnimeItem]):
    """

    configured_providers: list[TrackerStateConfiguredProvidersItem]
    can_use_patron_perks: bool
    connection: None | TrackerStateConnectionType0
    coverage: None | TrackerStateCoverageType0
    custom_lists: list[str]
    custom_list_count: int
    entries: list[TrackerStateEntriesItem]
    missing_anime: list[TrackerStateMissingAnimeItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tracker_state_connection_type_0 import TrackerStateConnectionType0  # noqa: PLC0415
        from ..models.tracker_state_coverage_type_0 import TrackerStateCoverageType0  # noqa: PLC0415

        configured_providers = []
        for configured_providers_item_data in self.configured_providers:
            configured_providers_item: str = configured_providers_item_data
            configured_providers.append(configured_providers_item)

        can_use_patron_perks = self.can_use_patron_perks

        connection: dict[str, Any] | None
        if isinstance(self.connection, TrackerStateConnectionType0):
            connection = self.connection.to_dict()
        else:
            connection = self.connection

        coverage: dict[str, Any] | None
        if isinstance(self.coverage, TrackerStateCoverageType0):
            coverage = self.coverage.to_dict()
        else:
            coverage = self.coverage

        custom_lists = self.custom_lists

        custom_list_count = self.custom_list_count

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        missing_anime = []
        for missing_anime_item_data in self.missing_anime:
            missing_anime_item = missing_anime_item_data.to_dict()
            missing_anime.append(missing_anime_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuredProviders": configured_providers,
                "canUsePatronPerks": can_use_patron_perks,
                "connection": connection,
                "coverage": coverage,
                "customLists": custom_lists,
                "customListCount": custom_list_count,
                "entries": entries,
                "missingAnime": missing_anime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracker_state_connection_type_0 import TrackerStateConnectionType0  # noqa: PLC0415
        from ..models.tracker_state_coverage_type_0 import TrackerStateCoverageType0  # noqa: PLC0415
        from ..models.tracker_state_entries_item import TrackerStateEntriesItem  # noqa: PLC0415
        from ..models.tracker_state_missing_anime_item import TrackerStateMissingAnimeItem  # noqa: PLC0415

        _src = dict(src_dict)
        configured_providers = []
        _configured_providers = _src.pop("configuredProviders")
        for configured_providers_item_data in _configured_providers:
            configured_providers_item = check_tracker_state_configured_providers_item(
                configured_providers_item_data
            )

            configured_providers.append(configured_providers_item)

        can_use_patron_perks = _src.pop("canUsePatronPerks")

        def _parse_connection(data: object) -> None | TrackerStateConnectionType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                connection_type_0 = TrackerStateConnectionType0.from_dict(data)

                return connection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TrackerStateConnectionType0, data)

        connection = _parse_connection(_src.pop("connection"))

        def _parse_coverage(data: object) -> None | TrackerStateCoverageType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                coverage_type_0 = TrackerStateCoverageType0.from_dict(data)

                return coverage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TrackerStateCoverageType0, data)

        coverage = _parse_coverage(_src.pop("coverage"))

        custom_lists = cast(list[str], _src.pop("customLists"))

        custom_list_count = _src.pop("customListCount")

        entries = []
        _entries = _src.pop("entries")
        for entries_item_data in _entries:
            entries_item = TrackerStateEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        missing_anime = []
        _missing_anime = _src.pop("missingAnime")
        for missing_anime_item_data in _missing_anime:
            missing_anime_item = TrackerStateMissingAnimeItem.from_dict(missing_anime_item_data)

            missing_anime.append(missing_anime_item)

        tracker_state = cls(
            configured_providers=configured_providers,
            can_use_patron_perks=can_use_patron_perks,
            connection=connection,
            coverage=coverage,
            custom_lists=custom_lists,
            custom_list_count=custom_list_count,
            entries=entries,
            missing_anime=missing_anime,
        )

        tracker_state.additional_properties = _src
        return tracker_state

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
