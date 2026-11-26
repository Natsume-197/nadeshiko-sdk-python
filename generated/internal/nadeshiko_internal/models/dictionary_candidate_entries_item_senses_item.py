from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dictionary_candidate_entries_item_senses_item_definitions_item import (
        DictionaryCandidateEntriesItemSensesItemDefinitionsItem,
    )
    from ..models.dictionary_candidate_entries_item_senses_item_tags_item import (
        DictionaryCandidateEntriesItemSensesItemTagsItem,
    )


T = TypeVar("T", bound="DictionaryCandidateEntriesItemSensesItem")


@_attrs_define
class DictionaryCandidateEntriesItemSensesItem:
    """
    Attributes:
        position (int):
        definitions (list[DictionaryCandidateEntriesItemSensesItemDefinitionsItem]):
        tags (list[DictionaryCandidateEntriesItemSensesItemTagsItem]):
        notes (list[str] | Unset):
    """

    position: int
    definitions: list[DictionaryCandidateEntriesItemSensesItemDefinitionsItem]
    tags: list[DictionaryCandidateEntriesItemSensesItemTagsItem]
    notes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        position = self.position

        definitions = []
        for definitions_item_data in self.definitions:
            definitions_item = definitions_item_data.to_dict()
            definitions.append(definitions_item)

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        notes: list[str] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "position": position,
                "definitions": definitions,
                "tags": tags,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_candidate_entries_item_senses_item_definitions_item import (
            DictionaryCandidateEntriesItemSensesItemDefinitionsItem,  # noqa: PLC0415
        )
        from ..models.dictionary_candidate_entries_item_senses_item_tags_item import (
            DictionaryCandidateEntriesItemSensesItemTagsItem,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        position = _src.pop("position")

        definitions = []
        _definitions = _src.pop("definitions")
        for definitions_item_data in _definitions:
            definitions_item = DictionaryCandidateEntriesItemSensesItemDefinitionsItem.from_dict(
                definitions_item_data
            )

            definitions.append(definitions_item)

        tags = []
        _tags = _src.pop("tags")
        for tags_item_data in _tags:
            tags_item = DictionaryCandidateEntriesItemSensesItemTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        notes = cast(list[str], _src.pop("notes", UNSET))

        dictionary_candidate_entries_item_senses_item = cls(
            position=position,
            definitions=definitions,
            tags=tags,
            notes=notes,
        )

        dictionary_candidate_entries_item_senses_item.additional_properties = _src
        return dictionary_candidate_entries_item_senses_item

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
