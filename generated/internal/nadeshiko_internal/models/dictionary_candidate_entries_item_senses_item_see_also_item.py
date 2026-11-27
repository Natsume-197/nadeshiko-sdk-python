from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DictionaryCandidateEntriesItemSensesItemSeeAlsoItem")


@_attrs_define
class DictionaryCandidateEntriesItemSensesItemSeeAlsoItem:
    """
    Attributes:
        text (str):
        reading (str | Unset):
    """

    text: str
    reading: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        reading = self.reading

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if reading is not UNSET:
            field_dict["reading"] = reading

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        text = _src.pop("text")

        reading = _src.pop("reading", UNSET)

        dictionary_candidate_entries_item_senses_item_see_also_item = cls(
            text=text,
            reading=reading,
        )

        dictionary_candidate_entries_item_senses_item_see_also_item.additional_properties = _src
        return dictionary_candidate_entries_item_senses_item_see_also_item

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
