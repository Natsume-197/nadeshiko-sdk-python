from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dictionary_kanji_custom_entries_item_senses_item import (
        DictionaryKanjiCustomEntriesItemSensesItem,
    )
    from ..models.dictionary_kanji_custom_entries_item_stats_item import (
        DictionaryKanjiCustomEntriesItemStatsItem,
    )
    from ..models.dictionary_kanji_custom_entries_item_tags_item import (
        DictionaryKanjiCustomEntriesItemTagsItem,
    )


T = TypeVar("T", bound="DictionaryKanjiCustomEntriesItem")


@_attrs_define
class DictionaryKanjiCustomEntriesItem:
    """
    Attributes:
        dictionary (str):  Example: custom:42.
        dictionary_name (str):  Example: KANJIDIC.
        tags (list[DictionaryKanjiCustomEntriesItemTagsItem]):
        onyomi (list[str] | Unset):  Example: ['ホン'].
        kunyomi (list[str] | Unset):  Example: ['もと'].
        meanings (list[str] | Unset):  Example: ['book', 'present', 'main'].
        stats (list[DictionaryKanjiCustomEntriesItemStatsItem] | Unset): The dictionary's own figures for the kanji
            (stroke count, grade, index numbers...).
        senses (list[DictionaryKanjiCustomEntriesItemSensesItem] | Unset): The article of a kanji dictionary shipped as
            a term dictionary, in the word card's shape.
    """

    dictionary: str
    dictionary_name: str
    tags: list[DictionaryKanjiCustomEntriesItemTagsItem]
    onyomi: list[str] | Unset = UNSET
    kunyomi: list[str] | Unset = UNSET
    meanings: list[str] | Unset = UNSET
    stats: list[DictionaryKanjiCustomEntriesItemStatsItem] | Unset = UNSET
    senses: list[DictionaryKanjiCustomEntriesItemSensesItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dictionary = self.dictionary

        dictionary_name = self.dictionary_name

        tags = []
        for tags_item_data in self.tags:
            tags_item = tags_item_data.to_dict()
            tags.append(tags_item)

        onyomi: list[str] | Unset = UNSET
        if not isinstance(self.onyomi, Unset):
            onyomi = self.onyomi

        kunyomi: list[str] | Unset = UNSET
        if not isinstance(self.kunyomi, Unset):
            kunyomi = self.kunyomi

        meanings: list[str] | Unset = UNSET
        if not isinstance(self.meanings, Unset):
            meanings = self.meanings

        stats: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = []
            for stats_item_data in self.stats:
                stats_item = stats_item_data.to_dict()
                stats.append(stats_item)

        senses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.senses, Unset):
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
                "tags": tags,
            }
        )
        if onyomi is not UNSET:
            field_dict["onyomi"] = onyomi
        if kunyomi is not UNSET:
            field_dict["kunyomi"] = kunyomi
        if meanings is not UNSET:
            field_dict["meanings"] = meanings
        if stats is not UNSET:
            field_dict["stats"] = stats
        if senses is not UNSET:
            field_dict["senses"] = senses

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_kanji_custom_entries_item_senses_item import (
            DictionaryKanjiCustomEntriesItemSensesItem,  # noqa: PLC0415
        )
        from ..models.dictionary_kanji_custom_entries_item_stats_item import (
            DictionaryKanjiCustomEntriesItemStatsItem,  # noqa: PLC0415
        )
        from ..models.dictionary_kanji_custom_entries_item_tags_item import (
            DictionaryKanjiCustomEntriesItemTagsItem,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        dictionary = _src.pop("dictionary")

        dictionary_name = _src.pop("dictionaryName")

        tags = []
        _tags = _src.pop("tags")
        for tags_item_data in _tags:
            tags_item = DictionaryKanjiCustomEntriesItemTagsItem.from_dict(tags_item_data)

            tags.append(tags_item)

        onyomi = cast(list[str], _src.pop("onyomi", UNSET))

        kunyomi = cast(list[str], _src.pop("kunyomi", UNSET))

        meanings = cast(list[str], _src.pop("meanings", UNSET))

        _stats = _src.pop("stats", UNSET)
        stats: list[DictionaryKanjiCustomEntriesItemStatsItem] | Unset = UNSET
        if _stats is not UNSET:
            stats = []
            for stats_item_data in _stats:
                stats_item = DictionaryKanjiCustomEntriesItemStatsItem.from_dict(stats_item_data)

                stats.append(stats_item)

        _senses = _src.pop("senses", UNSET)
        senses: list[DictionaryKanjiCustomEntriesItemSensesItem] | Unset = UNSET
        if _senses is not UNSET:
            senses = []
            for senses_item_data in _senses:
                senses_item = DictionaryKanjiCustomEntriesItemSensesItem.from_dict(senses_item_data)

                senses.append(senses_item)

        dictionary_kanji_custom_entries_item = cls(
            dictionary=dictionary,
            dictionary_name=dictionary_name,
            tags=tags,
            onyomi=onyomi,
            kunyomi=kunyomi,
            meanings=meanings,
            stats=stats,
            senses=senses,
        )

        dictionary_kanji_custom_entries_item.additional_properties = _src
        return dictionary_kanji_custom_entries_item

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
