from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DictionaryKanjiRelated")


@_attrs_define
class DictionaryKanjiRelated:
    """Another kanji the kanji view lists, with one reading and one meaning.

    Attributes:
        character (str):  Example: 飯.
        reading (None | str):  Example: ハン.
        meaning (None | str):  Example: meal.
        grade (int | None): School grade (1-6 and 8 jōyō, 9-10 jinmeiyō), to group the list. Example: 4.
    """

    character: str
    reading: None | str
    meaning: None | str
    grade: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        character = self.character

        reading: None | str
        reading = self.reading

        meaning: None | str
        meaning = self.meaning

        grade: int | None
        grade = self.grade

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "character": character,
                "reading": reading,
                "meaning": meaning,
                "grade": grade,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        character = _src.pop("character")

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

        def _parse_grade(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        grade = _parse_grade(_src.pop("grade"))

        dictionary_kanji_related = cls(
            character=character,
            reading=reading,
            meaning=meaning,
            grade=grade,
        )

        dictionary_kanji_related.additional_properties = _src
        return dictionary_kanji_related

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
