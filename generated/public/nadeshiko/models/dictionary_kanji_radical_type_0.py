from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DictionaryKanjiRadicalType0")


@_attrs_define
class DictionaryKanjiRadicalType0:
    """The classical (Kangxi) radical it is filed under, named by Kanji alive.

    Attributes:
        glyph (str):  Example: ⾷.
        number (int):  Example: 184.
        reading (str):  Example: しょく.
        meaning (str):  Example: food, to eat.
        character (None | str): The kanji the radical is written as, when it has a card. Example: 食.
    """

    glyph: str
    number: int
    reading: str
    meaning: str
    character: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        glyph = self.glyph

        number = self.number

        reading = self.reading

        meaning = self.meaning

        character: None | str
        character = self.character

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "glyph": glyph,
                "number": number,
                "reading": reading,
                "meaning": meaning,
                "character": character,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        glyph = _src.pop("glyph")

        number = _src.pop("number")

        reading = _src.pop("reading")

        meaning = _src.pop("meaning")

        def _parse_character(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        character = _parse_character(_src.pop("character"))

        dictionary_kanji_radical_type_0 = cls(
            glyph=glyph,
            number=number,
            reading=reading,
            meaning=meaning,
            character=character,
        )

        dictionary_kanji_radical_type_0.additional_properties = _src
        return dictionary_kanji_radical_type_0

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
