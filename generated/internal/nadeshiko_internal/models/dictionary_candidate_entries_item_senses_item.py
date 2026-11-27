from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dictionary_candidate_entries_item_senses_item_antonyms_item import (
        DictionaryCandidateEntriesItemSensesItemAntonymsItem,
    )
    from ..models.dictionary_candidate_entries_item_senses_item_definitions_item import (
        DictionaryCandidateEntriesItemSensesItemDefinitionsItem,
    )
    from ..models.dictionary_candidate_entries_item_senses_item_see_also_item import (
        DictionaryCandidateEntriesItemSensesItemSeeAlsoItem,
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
        see_also (list[DictionaryCandidateEntriesItemSensesItemSeeAlsoItem] | Unset): Related cross-referenced JMdict
            entries for this sense (e.g. 彼氏 for 彼女).
        antonyms (list[DictionaryCandidateEntriesItemSensesItemAntonymsItem] | Unset): Antonym cross-referenced JMdict
            entries for this sense.
    """

    position: int
    definitions: list[DictionaryCandidateEntriesItemSensesItemDefinitionsItem]
    tags: list[DictionaryCandidateEntriesItemSensesItemTagsItem]
    notes: list[str] | Unset = UNSET
    see_also: list[DictionaryCandidateEntriesItemSensesItemSeeAlsoItem] | Unset = UNSET
    antonyms: list[DictionaryCandidateEntriesItemSensesItemAntonymsItem] | Unset = UNSET
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

        see_also: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.see_also, Unset):
            see_also = []
            for see_also_item_data in self.see_also:
                see_also_item = see_also_item_data.to_dict()
                see_also.append(see_also_item)

        antonyms: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.antonyms, Unset):
            antonyms = []
            for antonyms_item_data in self.antonyms:
                antonyms_item = antonyms_item_data.to_dict()
                antonyms.append(antonyms_item)

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
        if see_also is not UNSET:
            field_dict["seeAlso"] = see_also
        if antonyms is not UNSET:
            field_dict["antonyms"] = antonyms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_candidate_entries_item_senses_item_antonyms_item import (
            DictionaryCandidateEntriesItemSensesItemAntonymsItem,  # noqa: PLC0415
        )
        from ..models.dictionary_candidate_entries_item_senses_item_definitions_item import (
            DictionaryCandidateEntriesItemSensesItemDefinitionsItem,  # noqa: PLC0415
        )
        from ..models.dictionary_candidate_entries_item_senses_item_see_also_item import (
            DictionaryCandidateEntriesItemSensesItemSeeAlsoItem,  # noqa: PLC0415
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

        _see_also = _src.pop("seeAlso", UNSET)
        see_also: list[DictionaryCandidateEntriesItemSensesItemSeeAlsoItem] | Unset = UNSET
        if _see_also is not UNSET:
            see_also = []
            for see_also_item_data in _see_also:
                see_also_item = DictionaryCandidateEntriesItemSensesItemSeeAlsoItem.from_dict(
                    see_also_item_data
                )

                see_also.append(see_also_item)

        _antonyms = _src.pop("antonyms", UNSET)
        antonyms: list[DictionaryCandidateEntriesItemSensesItemAntonymsItem] | Unset = UNSET
        if _antonyms is not UNSET:
            antonyms = []
            for antonyms_item_data in _antonyms:
                antonyms_item = DictionaryCandidateEntriesItemSensesItemAntonymsItem.from_dict(
                    antonyms_item_data
                )

                antonyms.append(antonyms_item)

        dictionary_candidate_entries_item_senses_item = cls(
            position=position,
            definitions=definitions,
            tags=tags,
            notes=notes,
            see_also=see_also,
            antonyms=antonyms,
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
