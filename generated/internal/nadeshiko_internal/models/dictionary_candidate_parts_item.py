from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DictionaryCandidatePartsItem")


@_attrs_define
class DictionaryCandidatePartsItem:
    """
    Attributes:
        text (str):  Example: 捜査.
        lemma (str):  Example: 捜査.
        reading (str):  Example: ソウサ.
        id (str):  Example: jmdict:1399010.
    """

    text: str
    lemma: str
    reading: str
    id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        lemma = self.lemma

        reading = self.reading

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "lemma": lemma,
                "reading": reading,
                "id": id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        text = _src.pop("text")

        lemma = _src.pop("lemma")

        reading = _src.pop("reading")

        id = _src.pop("id")

        dictionary_candidate_parts_item = cls(
            text=text,
            lemma=lemma,
            reading=reading,
            id=id,
        )

        dictionary_candidate_parts_item.additional_properties = _src
        return dictionary_candidate_parts_item

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
