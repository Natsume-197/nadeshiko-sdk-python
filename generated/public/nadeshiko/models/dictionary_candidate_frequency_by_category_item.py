from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dictionary_candidate_frequency_by_category_item_category import (
    DictionaryCandidateFrequencyByCategoryItemCategory,
    check_dictionary_candidate_frequency_by_category_item_category,
)

T = TypeVar("T", bound="DictionaryCandidateFrequencyByCategoryItem")


@_attrs_define
class DictionaryCandidateFrequencyByCategoryItem:
    """
    Attributes:
        category (DictionaryCandidateFrequencyByCategoryItemCategory):
        rank (int): 1 is the most frequent word in that kind of media. Example: 212.
        per_million (float): Occurrences per million words of that kind of media. Example: 431.7.
    """

    category: DictionaryCandidateFrequencyByCategoryItemCategory
    rank: int
    per_million: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        category: str = self.category

        rank = self.rank

        per_million = self.per_million

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "category": category,
                "rank": rank,
                "perMillion": per_million,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        category = check_dictionary_candidate_frequency_by_category_item_category(
            _src.pop("category")
        )

        rank = _src.pop("rank")

        per_million = _src.pop("perMillion")

        dictionary_candidate_frequency_by_category_item = cls(
            category=category,
            rank=rank,
            per_million=per_million,
        )

        dictionary_candidate_frequency_by_category_item.additional_properties = _src
        return dictionary_candidate_frequency_by_category_item

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
