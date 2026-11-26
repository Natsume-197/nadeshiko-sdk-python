from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.tracker_state_missing_anime_item_request_type_0_status import (
    TrackerStateMissingAnimeItemRequestType0Status,
    check_tracker_state_missing_anime_item_request_type_0_status,
)

T = TypeVar("T", bound="TrackerStateMissingAnimeItemRequestType0")


@_attrs_define
class TrackerStateMissingAnimeItemRequestType0:
    """
    Attributes:
        public_id (UUID):
        status (TrackerStateMissingAnimeItemRequestType0Status):
        vote_count (int):
        voted (bool): The reader already voted for it (filing counts as a vote).
    """

    public_id: UUID
    status: TrackerStateMissingAnimeItemRequestType0Status
    vote_count: int
    voted: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        public_id = str(self.public_id)

        status: str = self.status

        vote_count = self.vote_count

        voted = self.voted

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "publicId": public_id,
                "status": status,
                "voteCount": vote_count,
                "voted": voted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        public_id = UUID(_src.pop("publicId"))

        status = check_tracker_state_missing_anime_item_request_type_0_status(_src.pop("status"))

        vote_count = _src.pop("voteCount")

        voted = _src.pop("voted")

        tracker_state_missing_anime_item_request_type_0 = cls(
            public_id=public_id,
            status=status,
            vote_count=vote_count,
            voted=voted,
        )

        tracker_state_missing_anime_item_request_type_0.additional_properties = _src
        return tracker_state_missing_anime_item_request_type_0

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
