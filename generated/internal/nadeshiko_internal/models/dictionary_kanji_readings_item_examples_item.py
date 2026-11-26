from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dictionary_kanji_readings_item_examples_item_furigana_item import (
        DictionaryKanjiReadingsItemExamplesItemFuriganaItem,
    )


T = TypeVar("T", bound="DictionaryKanjiReadingsItemExamplesItem")


@_attrs_define
class DictionaryKanjiReadingsItemExamplesItem:
    """
    Attributes:
        id (str):  Example: jmdict:1358280.
        headword (str):  Example: 食べる.
        reading (None | str):  Example: たべる.
        furigana (list[DictionaryKanjiReadingsItemExamplesItemFuriganaItem]): The headword split into runs, with ruby
            over each kanji run (JmdictFurigana).
    """

    id: str
    headword: str
    reading: None | str
    furigana: list[DictionaryKanjiReadingsItemExamplesItemFuriganaItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        headword = self.headword

        reading: None | str
        reading = self.reading

        furigana = []
        for furigana_item_data in self.furigana:
            furigana_item = furigana_item_data.to_dict()
            furigana.append(furigana_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "headword": headword,
                "reading": reading,
                "furigana": furigana,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_kanji_readings_item_examples_item_furigana_item import (
            DictionaryKanjiReadingsItemExamplesItemFuriganaItem,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        id = _src.pop("id")

        headword = _src.pop("headword")

        def _parse_reading(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reading = _parse_reading(_src.pop("reading"))

        furigana = []
        _furigana = _src.pop("furigana")
        for furigana_item_data in _furigana:
            furigana_item = DictionaryKanjiReadingsItemExamplesItemFuriganaItem.from_dict(
                furigana_item_data
            )

            furigana.append(furigana_item)

        dictionary_kanji_readings_item_examples_item = cls(
            id=id,
            headword=headword,
            reading=reading,
            furigana=furigana,
        )

        dictionary_kanji_readings_item_examples_item.additional_properties = _src
        return dictionary_kanji_readings_item_examples_item

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
