from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dictionary_kanji_custom_entries_item import DictionaryKanjiCustomEntriesItem
    from ..models.dictionary_kanji_custom_frequencies_item import (
        DictionaryKanjiCustomFrequenciesItem,
    )


T = TypeVar("T", bound="DictionaryKanjiCustom")


@_attrs_define
class DictionaryKanjiCustom:
    """One kanji from the authenticated reader's own kanji dictionaries (Yomitan `kanji_bank` and `kanji_meta_bank`, and
    kanji dictionaries shipped as term dictionaries), in their stack order. Empty for a reader without any.

        Attributes:
            entries (list[DictionaryKanjiCustomEntriesItem]):
            frequencies (list[DictionaryKanjiCustomFrequenciesItem]): Ranks from the reader's kanji frequency dictionaries.
            stack_fingerprint (None | str | Unset): Fingerprint of the reader's custom dictionary stack.
            custom_dictionaries_pending (bool | Unset): True when the answer lacks one of the reader's enabled dictionaries,
                still indexing or still being fetched. Such an answer must not be cached.
    """

    entries: list[DictionaryKanjiCustomEntriesItem]
    frequencies: list[DictionaryKanjiCustomFrequenciesItem]
    stack_fingerprint: None | str | Unset = UNSET
    custom_dictionaries_pending: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        frequencies = []
        for frequencies_item_data in self.frequencies:
            frequencies_item = frequencies_item_data.to_dict()
            frequencies.append(frequencies_item)

        stack_fingerprint: None | str | Unset
        if isinstance(self.stack_fingerprint, Unset):
            stack_fingerprint = UNSET
        else:
            stack_fingerprint = self.stack_fingerprint

        custom_dictionaries_pending = self.custom_dictionaries_pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
                "frequencies": frequencies,
            }
        )
        if stack_fingerprint is not UNSET:
            field_dict["stackFingerprint"] = stack_fingerprint
        if custom_dictionaries_pending is not UNSET:
            field_dict["customDictionariesPending"] = custom_dictionaries_pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_kanji_custom_entries_item import DictionaryKanjiCustomEntriesItem  # noqa: PLC0415
        from ..models.dictionary_kanji_custom_frequencies_item import (
            DictionaryKanjiCustomFrequenciesItem,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        entries = []
        _entries = _src.pop("entries")
        for entries_item_data in _entries:
            entries_item = DictionaryKanjiCustomEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        frequencies = []
        _frequencies = _src.pop("frequencies")
        for frequencies_item_data in _frequencies:
            frequencies_item = DictionaryKanjiCustomFrequenciesItem.from_dict(frequencies_item_data)

            frequencies.append(frequencies_item)

        def _parse_stack_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stack_fingerprint = _parse_stack_fingerprint(_src.pop("stackFingerprint", UNSET))

        custom_dictionaries_pending = _src.pop("customDictionariesPending", UNSET)

        dictionary_kanji_custom = cls(
            entries=entries,
            frequencies=frequencies,
            stack_fingerprint=stack_fingerprint,
            custom_dictionaries_pending=custom_dictionaries_pending,
        )

        dictionary_kanji_custom.additional_properties = _src
        return dictionary_kanji_custom

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
