from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DictionaryKanjiWordRef")


@_attrs_define
class DictionaryKanjiWordRef:
    """A word from Nadeshiko's own dictionary, as the kanji view links it.

    Attributes:
        id (str):  Example: jmdict:1358280.
        headword (str):  Example: 食べる.
        reading (None | str):  Example: たべる.
    """

    id: str
    headword: str
    reading: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        headword = self.headword

        reading: None | str
        reading = self.reading

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "headword": headword,
                "reading": reading,
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

        dictionary_kanji_word_ref = cls(
            id=id,
            headword=headword,
            reading=reading,
        )

        dictionary_kanji_word_ref.additional_properties = _src
        return dictionary_kanji_word_ref

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
