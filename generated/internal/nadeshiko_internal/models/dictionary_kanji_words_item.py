from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DictionaryKanjiWordsItem")


@_attrs_define
class DictionaryKanjiWordsItem:
    """
    Attributes:
        id (str):  Example: jmdict:1358280.
        headword (str):  Example: 食べる.
        reading (None | str):  Example: たべる.
        frequency (int): Rank in Nadeshiko's corpus (1 is the most frequent word). Example: 195.
        gloss (None | str):  Example: to eat.
    """

    id: str
    headword: str
    reading: None | str
    frequency: int
    gloss: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        headword = self.headword

        reading: None | str
        reading = self.reading

        frequency = self.frequency

        gloss: None | str
        gloss = self.gloss

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "headword": headword,
                "reading": reading,
                "frequency": frequency,
                "gloss": gloss,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        headword = _src.pop("headword")

        def _parse_reading(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reading = _parse_reading(_src.pop("reading"))

        frequency = _src.pop("frequency")

        def _parse_gloss(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        gloss = _parse_gloss(_src.pop("gloss"))

        dictionary_kanji_words_item = cls(
            id=id,
            headword=headword,
            reading=reading,
            frequency=frequency,
            gloss=gloss,
        )

        dictionary_kanji_words_item.additional_properties = _src
        return dictionary_kanji_words_item

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
