from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.word_watch import WordWatch


T = TypeVar("T", bound="ListWordWatchesResponse200")


@_attrs_define
class ListWordWatchesResponse200:
    """
    Attributes:
        items (list[WordWatch]):
        active_count (int):
        limit (int): Active alerts this reader may have (more for patrons).
    """

    items: list[WordWatch]
    active_count: int
    limit: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        active_count = self.active_count

        limit = self.limit

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "activeCount": active_count,
                "limit": limit,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.word_watch import WordWatch  # noqa: PLC0415

        _src = dict(src_dict)
        items = []
        _items = _src.pop("items")
        for items_item_data in _items:
            items_item = WordWatch.from_dict(items_item_data)

            items.append(items_item)

        active_count = _src.pop("activeCount")

        limit = _src.pop("limit")

        list_word_watches_response_200 = cls(
            items=items,
            active_count=active_count,
            limit=limit,
        )

        list_word_watches_response_200.additional_properties = _src
        return list_word_watches_response_200

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
