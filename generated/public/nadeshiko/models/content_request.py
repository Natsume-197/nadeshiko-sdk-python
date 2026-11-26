from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.content_request_category import ContentRequestCategory, check_content_request_category
from ..models.content_request_kind import ContentRequestKind, check_content_request_kind
from ..models.content_request_status import ContentRequestStatus, check_content_request_status

if TYPE_CHECKING:
    from ..models.content_request_media_type_0 import ContentRequestMediaType0


T = TypeVar("T", bound="ContentRequest")


@_attrs_define
class ContentRequest:
    """A reader's request for content, shared by everyone who wants the same title.

    Attributes:
        id (UUID):
        category (ContentRequestCategory):
        kind (ContentRequestKind): NEW asks for a title not on Nadeshiko; UPDATE asks for more of one that is.
        status (ContentRequestStatus):
        title (str):
        note (str):
        source_url (str):
        cover_url (None | str):
        decline_reason (None | str): Why a declined request was declined; null otherwise.
        vote_count (int):
        boost_count (int):
        score (int): Votes plus five per boost.
        media (ContentRequestMediaType0 | None): The published media this request is for (UPDATE) or produced
            (RELEASED).
        created_at (datetime.datetime):
        released_at (datetime.datetime | None):
    """

    id: UUID
    category: ContentRequestCategory
    kind: ContentRequestKind
    status: ContentRequestStatus
    title: str
    note: str
    source_url: str
    cover_url: None | str
    decline_reason: None | str
    vote_count: int
    boost_count: int
    score: int
    media: ContentRequestMediaType0 | None
    created_at: datetime.datetime
    released_at: datetime.datetime | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.content_request_media_type_0 import ContentRequestMediaType0  # noqa: PLC0415

        id = str(self.id)

        category: str = self.category

        kind: str = self.kind

        status: str = self.status

        title = self.title

        note = self.note

        source_url = self.source_url

        cover_url: None | str
        cover_url = self.cover_url

        decline_reason: None | str
        decline_reason = self.decline_reason

        vote_count = self.vote_count

        boost_count = self.boost_count

        score = self.score

        media: dict[str, Any] | None
        if isinstance(self.media, ContentRequestMediaType0):
            media = self.media.to_dict()
        else:
            media = self.media

        created_at = self.created_at.isoformat()

        released_at: None | str
        if isinstance(self.released_at, datetime.datetime):
            released_at = self.released_at.isoformat()
        else:
            released_at = self.released_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "category": category,
                "kind": kind,
                "status": status,
                "title": title,
                "note": note,
                "sourceUrl": source_url,
                "coverUrl": cover_url,
                "declineReason": decline_reason,
                "voteCount": vote_count,
                "boostCount": boost_count,
                "score": score,
                "media": media,
                "createdAt": created_at,
                "releasedAt": released_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_request_media_type_0 import ContentRequestMediaType0  # noqa: PLC0415

        _src = dict(src_dict)
        id = UUID(_src.pop("id"))

        category = check_content_request_category(_src.pop("category"))

        kind = check_content_request_kind(_src.pop("kind"))

        status = check_content_request_status(_src.pop("status"))

        title = _src.pop("title")

        note = _src.pop("note")

        source_url = _src.pop("sourceUrl")

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(_src.pop("coverUrl"))

        def _parse_decline_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        decline_reason = _parse_decline_reason(_src.pop("declineReason"))

        vote_count = _src.pop("voteCount")

        boost_count = _src.pop("boostCount")

        score = _src.pop("score")

        def _parse_media(data: object) -> ContentRequestMediaType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                media_type_0 = ContentRequestMediaType0.from_dict(data)

                return media_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ContentRequestMediaType0 | None, data)

        media = _parse_media(_src.pop("media"))

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        def _parse_released_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                released_at_type_0 = datetime.datetime.fromisoformat(data)

                return released_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        released_at = _parse_released_at(_src.pop("releasedAt"))

        content_request = cls(
            id=id,
            category=category,
            kind=kind,
            status=status,
            title=title,
            note=note,
            source_url=source_url,
            cover_url=cover_url,
            decline_reason=decline_reason,
            vote_count=vote_count,
            boost_count=boost_count,
            score=score,
            media=media,
            created_at=created_at,
            released_at=released_at,
        )

        content_request.additional_properties = _src
        return content_request

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
