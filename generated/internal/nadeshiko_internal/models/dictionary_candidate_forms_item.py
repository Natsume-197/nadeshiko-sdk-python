from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dictionary_candidate_forms_item_script import (
    DictionaryCandidateFormsItemScript,
    check_dictionary_candidate_forms_item_script,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="DictionaryCandidateFormsItem")


@_attrs_define
class DictionaryCandidateFormsItem:
    """
    Attributes:
        text (str):
        script (DictionaryCandidateFormsItemScript):
        common (bool):
        frequency (int | Unset): Corpus rank of this specific spelling when enough occurrences exist.
        share (float | Unset): Fraction (0..1) of this word's corpus occurrences written in this spelling.
    """

    text: str
    script: DictionaryCandidateFormsItemScript
    common: bool
    frequency: int | Unset = UNSET
    share: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        script: str = self.script

        common = self.common

        frequency = self.frequency

        share = self.share

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "script": script,
                "common": common,
            }
        )
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if share is not UNSET:
            field_dict["share"] = share

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        text = _src.pop("text")

        script = check_dictionary_candidate_forms_item_script(_src.pop("script"))

        common = _src.pop("common")

        frequency = _src.pop("frequency", UNSET)

        share = _src.pop("share", UNSET)

        dictionary_candidate_forms_item = cls(
            text=text,
            script=script,
            common=common,
            frequency=frequency,
            share=share,
        )

        dictionary_candidate_forms_item.additional_properties = _src
        return dictionary_candidate_forms_item

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
