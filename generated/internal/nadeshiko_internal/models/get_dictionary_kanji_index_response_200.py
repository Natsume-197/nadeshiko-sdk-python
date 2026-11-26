from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_dictionary_kanji_index_response_200_kanji_item import (
        GetDictionaryKanjiIndexResponse200KanjiItem,
    )


T = TypeVar("T", bound="GetDictionaryKanjiIndexResponse200")


@_attrs_define
class GetDictionaryKanjiIndexResponse200:
    """
    Attributes:
        kanji (list[GetDictionaryKanjiIndexResponse200KanjiItem]): School kanji first by grade, then by newspaper
            frequency.
    """

    kanji: list[GetDictionaryKanjiIndexResponse200KanjiItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kanji = []
        for kanji_item_data in self.kanji:
            kanji_item = kanji_item_data.to_dict()
            kanji.append(kanji_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kanji": kanji,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_dictionary_kanji_index_response_200_kanji_item import (
            GetDictionaryKanjiIndexResponse200KanjiItem,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        kanji = []
        _kanji = _src.pop("kanji")
        for kanji_item_data in _kanji:
            kanji_item = GetDictionaryKanjiIndexResponse200KanjiItem.from_dict(kanji_item_data)

            kanji.append(kanji_item)

        get_dictionary_kanji_index_response_200 = cls(
            kanji=kanji,
        )

        get_dictionary_kanji_index_response_200.additional_properties = _src
        return get_dictionary_kanji_index_response_200

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
