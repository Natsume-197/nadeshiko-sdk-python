from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DictionaryKanjiCustomEntriesItemStatsItem")


@_attrs_define
class DictionaryKanjiCustomEntriesItemStatsItem:
    """
    Attributes:
        code (str):  Example: strokes.
        label (str):  Example: Stroke count.
        category (str):  Example: misc.
        value (str):  Example: 5.
    """

    code: str
    label: str
    category: str
    value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        label = self.label

        category = self.category

        value = self.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "code": code,
                "label": label,
                "category": category,
                "value": value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        code = _src.pop("code")

        label = _src.pop("label")

        category = _src.pop("category")

        value = _src.pop("value")

        dictionary_kanji_custom_entries_item_stats_item = cls(
            code=code,
            label=label,
            category=category,
            value=value,
        )

        dictionary_kanji_custom_entries_item_stats_item.additional_properties = _src
        return dictionary_kanji_custom_entries_item_stats_item

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
