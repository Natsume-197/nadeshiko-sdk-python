from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PreviewContentRequestResponse200ExistingType0Media")


@_attrs_define
class PreviewContentRequestResponse200ExistingType0Media:
    """
    Attributes:
        id (str):
        slug (str):
        name (str):
    """

    id: str
    slug: str
    name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        slug = self.slug

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "slug": slug,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        slug = _src.pop("slug")

        name = _src.pop("name")

        preview_content_request_response_200_existing_type_0_media = cls(
            id=id,
            slug=slug,
            name=name,
        )

        preview_content_request_response_200_existing_type_0_media.additional_properties = _src
        return preview_content_request_response_200_existing_type_0_media

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
