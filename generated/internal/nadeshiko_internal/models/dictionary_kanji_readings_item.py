from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dictionary_kanji_readings_item_kind import (
    DictionaryKanjiReadingsItemKind,
    check_dictionary_kanji_readings_item_kind,
)

if TYPE_CHECKING:
    from ..models.dictionary_kanji_readings_item_examples_item import (
        DictionaryKanjiReadingsItemExamplesItem,
    )


T = TypeVar("T", bound="DictionaryKanjiReadingsItem")


@_attrs_define
class DictionaryKanjiReadingsItem:
    """
    Attributes:
        kind (DictionaryKanjiReadingsItemKind):
        reading (str): Katakana for on; hiragana with `.` before the okurigana for kun. Example: た.べる.
        examples (list[DictionaryKanjiReadingsItemExamplesItem]):
    """

    kind: DictionaryKanjiReadingsItemKind
    reading: str
    examples: list[DictionaryKanjiReadingsItemExamplesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        reading = self.reading

        examples = []
        for examples_item_data in self.examples:
            examples_item = examples_item_data.to_dict()
            examples.append(examples_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "reading": reading,
                "examples": examples,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_kanji_readings_item_examples_item import (
            DictionaryKanjiReadingsItemExamplesItem,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        kind = check_dictionary_kanji_readings_item_kind(_src.pop("kind"))

        reading = _src.pop("reading")

        examples = []
        _examples = _src.pop("examples")
        for examples_item_data in _examples:
            examples_item = DictionaryKanjiReadingsItemExamplesItem.from_dict(examples_item_data)

            examples.append(examples_item)

        dictionary_kanji_readings_item = cls(
            kind=kind,
            reading=reading,
            examples=examples,
        )

        dictionary_kanji_readings_item.additional_properties = _src
        return dictionary_kanji_readings_item

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
