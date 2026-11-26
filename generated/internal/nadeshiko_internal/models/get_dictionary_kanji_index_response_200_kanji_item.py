from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="GetDictionaryKanjiIndexResponse200KanjiItem")


@_attrs_define
class GetDictionaryKanjiIndexResponse200KanjiItem:
    """
    Attributes:
        character (str):  Example: 日.
        grade (int | None):  Example: 1.
        jlpt (int | None):  Example: 5.
        frequency (int | None):  Example: 1.
        reading (None | str):  Example: ニチ.
        meaning (None | str):  Example: day.
    """

    character: str
    grade: int | None
    jlpt: int | None
    frequency: int | None
    reading: None | str
    meaning: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        character = self.character

        grade: int | None
        grade = self.grade

        jlpt: int | None
        jlpt = self.jlpt

        frequency: int | None
        frequency = self.frequency

        reading: None | str
        reading = self.reading

        meaning: None | str
        meaning = self.meaning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "character": character,
                "grade": grade,
                "jlpt": jlpt,
                "frequency": frequency,
                "reading": reading,
                "meaning": meaning,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        character = _src.pop("character")

        def _parse_grade(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        grade = _parse_grade(_src.pop("grade"))

        def _parse_jlpt(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        jlpt = _parse_jlpt(_src.pop("jlpt"))

        def _parse_frequency(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        frequency = _parse_frequency(_src.pop("frequency"))

        def _parse_reading(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reading = _parse_reading(_src.pop("reading"))

        def _parse_meaning(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        meaning = _parse_meaning(_src.pop("meaning"))

        get_dictionary_kanji_index_response_200_kanji_item = cls(
            character=character,
            grade=grade,
            jlpt=jlpt,
            frequency=frequency,
            reading=reading,
            meaning=meaning,
        )

        get_dictionary_kanji_index_response_200_kanji_item.additional_properties = _src
        return get_dictionary_kanji_index_response_200_kanji_item

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
