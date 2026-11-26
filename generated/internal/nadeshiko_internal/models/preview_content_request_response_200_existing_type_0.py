from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.preview_content_request_response_200_existing_type_0_media import (
        PreviewContentRequestResponse200ExistingType0Media,
    )


T = TypeVar("T", bound="PreviewContentRequestResponse200ExistingType0")


@_attrs_define
class PreviewContentRequestResponse200ExistingType0:
    """The published title this link names, or null when it is not on Nadeshiko.

    Attributes:
        media (PreviewContentRequestResponse200ExistingType0Media):
        episodes (int): Episodes (or videos
        total_episodes (int | None): Episodes the source lists (anime only); null when unknown or still airing without a
            count.
        complete (bool): True when the source has finished airing and Nadeshiko holds every episode. Such a title cannot
            be requested.
    """

    media: PreviewContentRequestResponse200ExistingType0Media
    episodes: int
    total_episodes: int | None
    complete: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        media = self.media.to_dict()

        episodes = self.episodes

        total_episodes: int | None
        total_episodes = self.total_episodes

        complete = self.complete

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "media": media,
                "episodes": episodes,
                "totalEpisodes": total_episodes,
                "complete": complete,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_content_request_response_200_existing_type_0_media import (
            PreviewContentRequestResponse200ExistingType0Media,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        media = PreviewContentRequestResponse200ExistingType0Media.from_dict(_src.pop("media"))

        episodes = _src.pop("episodes")

        def _parse_total_episodes(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        total_episodes = _parse_total_episodes(_src.pop("totalEpisodes"))

        complete = _src.pop("complete")

        preview_content_request_response_200_existing_type_0 = cls(
            media=media,
            episodes=episodes,
            total_episodes=total_episodes,
            complete=complete,
        )

        preview_content_request_response_200_existing_type_0.additional_properties = _src
        return preview_content_request_response_200_existing_type_0

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
