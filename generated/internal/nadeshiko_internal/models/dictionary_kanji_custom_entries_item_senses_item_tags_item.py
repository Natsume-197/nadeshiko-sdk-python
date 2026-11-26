from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dictionary_kanji_custom_entries_item_senses_item_tags_item_category import (
    DictionaryKanjiCustomEntriesItemSensesItemTagsItemCategory,
    check_dictionary_kanji_custom_entries_item_senses_item_tags_item_category,
)

T = TypeVar("T", bound="DictionaryKanjiCustomEntriesItemSensesItemTagsItem")


@_attrs_define
class DictionaryKanjiCustomEntriesItemSensesItemTagsItem:
    """
    Attributes:
        category (DictionaryKanjiCustomEntriesItemSensesItemTagsItemCategory):
        code (str):
        label (str):
    """

    category: DictionaryKanjiCustomEntriesItemSensesItemTagsItemCategory
    code: str
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str = self.category

        code = self.code

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "code": code,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        category = check_dictionary_kanji_custom_entries_item_senses_item_tags_item_category(
            _src.pop("category")
        )

        code = _src.pop("code")

        label = _src.pop("label")

        dictionary_kanji_custom_entries_item_senses_item_tags_item = cls(
            category=category,
            code=code,
            label=label,
        )

        dictionary_kanji_custom_entries_item_senses_item_tags_item.additional_properties = _src
        return dictionary_kanji_custom_entries_item_senses_item_tags_item

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
