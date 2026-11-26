from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DictionaryCandidateCustomFrequenciesItem")


@_attrs_define
class DictionaryCandidateCustomFrequenciesItem:
    """
    Attributes:
        dictionary (str):
        dictionary_name (str):
        value (float | None):
        display_value (str):
    """

    dictionary: str
    dictionary_name: str
    value: float | None
    display_value: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dictionary = self.dictionary

        dictionary_name = self.dictionary_name

        value: float | None
        value = self.value

        display_value = self.display_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dictionary": dictionary,
                "dictionaryName": dictionary_name,
                "value": value,
                "displayValue": display_value,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        dictionary = _src.pop("dictionary")

        dictionary_name = _src.pop("dictionaryName")

        def _parse_value(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        value = _parse_value(_src.pop("value"))

        display_value = _src.pop("displayValue")

        dictionary_candidate_custom_frequencies_item = cls(
            dictionary=dictionary,
            dictionary_name=dictionary_name,
            value=value,
            display_value=display_value,
        )

        dictionary_candidate_custom_frequencies_item.additional_properties = _src
        return dictionary_candidate_custom_frequencies_item

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
