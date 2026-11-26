from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.dictionary_candidate_entries_item_senses_item import (
        DictionaryCandidateEntriesItemSensesItem,
    )


T = TypeVar("T", bound="DictionaryCandidateEntriesItem")


@_attrs_define
class DictionaryCandidateEntriesItem:
    """
    Attributes:
        dictionary (str):
        dictionary_name (str):
        senses (list[DictionaryCandidateEntriesItemSensesItem]):
    """

    dictionary: str
    dictionary_name: str
    senses: list[DictionaryCandidateEntriesItemSensesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dictionary = self.dictionary

        dictionary_name = self.dictionary_name

        senses = []
        for senses_item_data in self.senses:
            senses_item = senses_item_data.to_dict()
            senses.append(senses_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dictionary": dictionary,
                "dictionaryName": dictionary_name,
                "senses": senses,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_candidate_entries_item_senses_item import (
            DictionaryCandidateEntriesItemSensesItem,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        dictionary = _src.pop("dictionary")

        dictionary_name = _src.pop("dictionaryName")

        senses = []
        _senses = _src.pop("senses")
        for senses_item_data in _senses:
            senses_item = DictionaryCandidateEntriesItemSensesItem.from_dict(senses_item_data)

            senses.append(senses_item)

        dictionary_candidate_entries_item = cls(
            dictionary=dictionary,
            dictionary_name=dictionary_name,
            senses=senses,
        )

        dictionary_candidate_entries_item.additional_properties = _src
        return dictionary_candidate_entries_item

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
