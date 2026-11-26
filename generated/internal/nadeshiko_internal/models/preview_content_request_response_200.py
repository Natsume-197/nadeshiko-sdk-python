from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.preview_content_request_response_200_category import (
    PreviewContentRequestResponse200Category,
    check_preview_content_request_response_200_category,
)

if TYPE_CHECKING:
    from ..models.preview_content_request_response_200_existing_type_0 import (
        PreviewContentRequestResponse200ExistingType0,
    )


T = TypeVar("T", bound="PreviewContentRequestResponse200")


@_attrs_define
class PreviewContentRequestResponse200:
    """
    Attributes:
        category (PreviewContentRequestResponse200Category):
        title (None | str):
        cover_url (None | str):
        existing (None | PreviewContentRequestResponse200ExistingType0): The published title this link names, or null
            when it is not on Nadeshiko.
        active_request_id (None | UUID): The open request for the same title; filing adds a vote to it instead.
    """

    category: PreviewContentRequestResponse200Category
    title: None | str
    cover_url: None | str
    existing: None | PreviewContentRequestResponse200ExistingType0
    active_request_id: None | UUID
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.preview_content_request_response_200_existing_type_0 import (
            PreviewContentRequestResponse200ExistingType0,  # noqa: PLC0415
        )

        category: str = self.category

        title: None | str
        title = self.title

        cover_url: None | str
        cover_url = self.cover_url

        existing: dict[str, Any] | None
        if isinstance(self.existing, PreviewContentRequestResponse200ExistingType0):
            existing = self.existing.to_dict()
        else:
            existing = self.existing

        active_request_id: None | str
        if isinstance(self.active_request_id, UUID):
            active_request_id = str(self.active_request_id)
        else:
            active_request_id = self.active_request_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "title": title,
                "coverUrl": cover_url,
                "existing": existing,
                "activeRequestId": active_request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview_content_request_response_200_existing_type_0 import (
            PreviewContentRequestResponse200ExistingType0,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        category = check_preview_content_request_response_200_category(_src.pop("category"))

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(_src.pop("title"))

        def _parse_cover_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        cover_url = _parse_cover_url(_src.pop("coverUrl"))

        def _parse_existing(data: object) -> None | PreviewContentRequestResponse200ExistingType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                existing_type_0 = PreviewContentRequestResponse200ExistingType0.from_dict(data)

                return existing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PreviewContentRequestResponse200ExistingType0, data)

        existing = _parse_existing(_src.pop("existing"))

        def _parse_active_request_id(data: object) -> None | UUID:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                active_request_id_type_0 = UUID(data)

                return active_request_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | UUID, data)

        active_request_id = _parse_active_request_id(_src.pop("activeRequestId"))

        preview_content_request_response_200 = cls(
            category=category,
            title=title,
            cover_url=cover_url,
            existing=existing,
            active_request_id=active_request_id,
        )

        preview_content_request_response_200.additional_properties = _src
        return preview_content_request_response_200

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
