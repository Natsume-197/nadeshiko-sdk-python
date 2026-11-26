from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DictionaryKanjiComponentsItem")


@_attrs_define
class DictionaryKanjiComponentsItem:
    """
    Attributes:
        character (str):  Example: 良.
        has_card (bool): The part is a kanji with a card of its own.
        meaning (None | str): The kanji's first meaning, or the radical's (English) for a shape with no card. Example:
            good.
    """

    character: str
    has_card: bool
    meaning: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        character = self.character

        has_card = self.has_card

        meaning: None | str
        meaning = self.meaning

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "character": character,
                "hasCard": has_card,
                "meaning": meaning,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        character = _src.pop("character")

        has_card = _src.pop("hasCard")

        def _parse_meaning(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        meaning = _parse_meaning(_src.pop("meaning"))

        dictionary_kanji_components_item = cls(
            character=character,
            has_card=has_card,
            meaning=meaning,
        )

        dictionary_kanji_components_item.additional_properties = _src
        return dictionary_kanji_components_item

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
