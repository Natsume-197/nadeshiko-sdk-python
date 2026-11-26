from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_state_missing_anime_item_external_source import (
    TrackerStateMissingAnimeItemExternalSource,
    check_tracker_state_missing_anime_item_external_source,
)
from ..models.tracker_state_missing_anime_item_status import (
    TrackerStateMissingAnimeItemStatus,
    check_tracker_state_missing_anime_item_status,
)

if TYPE_CHECKING:
    from ..models.tracker_state_missing_anime_item_request_type_0 import (
        TrackerStateMissingAnimeItemRequestType0,
    )


T = TypeVar("T", bound="TrackerStateMissingAnimeItem")


@_attrs_define
class TrackerStateMissingAnimeItem:
    """
    Attributes:
        external_source (TrackerStateMissingAnimeItemExternalSource):
        external_id (str):
        title (str):
        status (TrackerStateMissingAnimeItemStatus):
        source_url (str):
        request (None | TrackerStateMissingAnimeItemRequestType0): The content request already filed for this title
            (active or declined), or null.
    """

    external_source: TrackerStateMissingAnimeItemExternalSource
    external_id: str
    title: str
    status: TrackerStateMissingAnimeItemStatus
    source_url: str
    request: None | TrackerStateMissingAnimeItemRequestType0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tracker_state_missing_anime_item_request_type_0 import (
            TrackerStateMissingAnimeItemRequestType0,  # noqa: PLC0415
        )

        external_source: str = self.external_source

        external_id = self.external_id

        title = self.title

        status: str = self.status

        source_url = self.source_url

        request: dict[str, Any] | None
        if isinstance(self.request, TrackerStateMissingAnimeItemRequestType0):
            request = self.request.to_dict()
        else:
            request = self.request

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "externalSource": external_source,
                "externalId": external_id,
                "title": title,
                "status": status,
                "sourceUrl": source_url,
                "request": request,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracker_state_missing_anime_item_request_type_0 import (
            TrackerStateMissingAnimeItemRequestType0,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        external_source = check_tracker_state_missing_anime_item_external_source(
            _src.pop("externalSource")
        )

        external_id = _src.pop("externalId")

        title = _src.pop("title")

        status = check_tracker_state_missing_anime_item_status(_src.pop("status"))

        source_url = _src.pop("sourceUrl")

        def _parse_request(data: object) -> None | TrackerStateMissingAnimeItemRequestType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                request_type_0 = TrackerStateMissingAnimeItemRequestType0.from_dict(data)

                return request_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TrackerStateMissingAnimeItemRequestType0, data)

        request = _parse_request(_src.pop("request"))

        tracker_state_missing_anime_item = cls(
            external_source=external_source,
            external_id=external_id,
            title=title,
            status=status,
            source_url=source_url,
            request=request,
        )

        tracker_state_missing_anime_item.additional_properties = _src
        return tracker_state_missing_anime_item

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
