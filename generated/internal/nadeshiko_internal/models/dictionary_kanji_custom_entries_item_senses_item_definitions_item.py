from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dictionary_kanji_custom_entries_item_senses_item_definitions_item_lang import (
    DictionaryKanjiCustomEntriesItemSensesItemDefinitionsItemLang,
    check_dictionary_kanji_custom_entries_item_senses_item_definitions_item_lang,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DictionaryKanjiCustomEntriesItemSensesItemDefinitionsItem")


@_attrs_define
class DictionaryKanjiCustomEntriesItemSensesItemDefinitionsItem:
    """
    Attributes:
        lang (DictionaryKanjiCustomEntriesItemSensesItemDefinitionsItemLang):
        text (str):
        structured_content (Any | Unset): Sanitized Yomitan structured-content AST.
    """

    lang: DictionaryKanjiCustomEntriesItemSensesItemDefinitionsItemLang
    text: str
    structured_content: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lang: str = self.lang

        text = self.text

        structured_content = self.structured_content

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "lang": lang,
                "text": text,
            }
        )
        if structured_content is not UNSET:
            field_dict["structuredContent"] = structured_content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        lang = check_dictionary_kanji_custom_entries_item_senses_item_definitions_item_lang(
            _src.pop("lang")
        )

        text = _src.pop("text")

        structured_content = _src.pop("structuredContent", UNSET)

        dictionary_kanji_custom_entries_item_senses_item_definitions_item = cls(
            lang=lang,
            text=text,
            structured_content=structured_content,
        )

        dictionary_kanji_custom_entries_item_senses_item_definitions_item.additional_properties = (
            _src
        )
        return dictionary_kanji_custom_entries_item_senses_item_definitions_item

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
