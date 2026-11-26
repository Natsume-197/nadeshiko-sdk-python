from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_state_entries_item_status import (
    TrackerStateEntriesItemStatus,
    check_tracker_state_entries_item_status,
)

T = TypeVar("T", bound="TrackerStateEntriesItem")


@_attrs_define
class TrackerStateEntriesItem:
    """
    Attributes:
        media_public_id (str):
        title (str):
        status (TrackerStateEntriesItemStatus):
        progress (int):
        custom_lists (list[str]):
    """

    media_public_id: str
    title: str
    status: TrackerStateEntriesItemStatus
    progress: int
    custom_lists: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media_public_id = self.media_public_id

        title = self.title

        status: str = self.status

        progress = self.progress

        custom_lists = self.custom_lists

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mediaPublicId": media_public_id,
                "title": title,
                "status": status,
                "progress": progress,
                "customLists": custom_lists,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        media_public_id = _src.pop("mediaPublicId")

        title = _src.pop("title")

        status = check_tracker_state_entries_item_status(_src.pop("status"))

        progress = _src.pop("progress")

        custom_lists = cast(list[str], _src.pop("customLists"))

        tracker_state_entries_item = cls(
            media_public_id=media_public_id,
            title=title,
            status=status,
            progress=progress,
            custom_lists=custom_lists,
        )

        tracker_state_entries_item.additional_properties = _src
        return tracker_state_entries_item

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
