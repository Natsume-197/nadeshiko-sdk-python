from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dictionary_candidate_custom_frequencies_item import (
        DictionaryCandidateCustomFrequenciesItem,
    )
    from ..models.dictionary_candidate_entries_item import DictionaryCandidateEntriesItem
    from ..models.dictionary_candidate_forms_item import DictionaryCandidateFormsItem
    from ..models.dictionary_candidate_frequency_by_category_item import (
        DictionaryCandidateFrequencyByCategoryItem,
    )
    from ..models.dictionary_candidate_furigana_item import DictionaryCandidateFuriganaItem
    from ..models.dictionary_candidate_parts_item import DictionaryCandidatePartsItem
    from ..models.dictionary_candidate_pitch_item import DictionaryCandidatePitchItem


T = TypeVar("T", bound="DictionaryCandidate")


@_attrs_define
class DictionaryCandidate:
    """One ranked answer from Nadeshiko's dictionary (JMdict/JMnedict plus the
    reader's uploaded custom Yomitan dictionaries). Pitch audio is not provided yet.

        Attributes:
            id (str): `<dictionary>:<ent_seq>`. Example: jmdict:1358280.
            headword (str):  Example: 食べる.
            reading (None | str):  Example: たべる.
            common (bool):
            name (bool): A proper name rather than a word.
            source_id (str): The JMdict/JMnedict entry sequence number. Example: 1358280.
            dictionary (str):  Example: jmdict.
            jlpt (None | str): Unofficial JLPT level estimate (N5-N1). Example: N5.
            frequency (int | None): Rank in Nadeshiko's own corpus (1 is the most frequent word); null when not counted.
                Example: 19.
            forms (list[DictionaryCandidateFormsItem]):
            entries (list[DictionaryCandidateEntriesItem]):
            frequency_by_category (list[DictionaryCandidateFrequencyByCategoryItem] | Unset): Rank in each kind of media the
                word occurs in, the kind that uses it most first (by occurrences per
                million words of that kind). Absent when not counted.
            custom_frequencies (list[DictionaryCandidateCustomFrequenciesItem] | Unset): Frequencies from the authenticated
                reader's enabled custom Yomitan frequency dictionaries.
            base_form (bool | Unset): Present and true when nothing is filed under the text looked up and this word is its
                dictionary form
                (食べた → 食べる).
            inflection (list[str] | Unset): With `baseForm`: what the conjugation does, in the word card's inflection
                labels, outermost first.
                 Example: ['past'].
            pitch (list[DictionaryCandidatePitchItem] | Unset): Accent patterns from the user's custom pitch dictionaries or
                UniDic fallback.
            parts (list[DictionaryCandidatePartsItem] | Unset): The words a compound or expression is made of (捜査本部: 捜査,
                本部), content words only, each one
                resolvable by the card. Absent for a word of one piece.
            furigana (list[DictionaryCandidateFuriganaItem] | Unset):
    """

    id: str
    headword: str
    reading: None | str
    common: bool
    name: bool
    source_id: str
    dictionary: str
    jlpt: None | str
    frequency: int | None
    forms: list[DictionaryCandidateFormsItem]
    entries: list[DictionaryCandidateEntriesItem]
    frequency_by_category: list[DictionaryCandidateFrequencyByCategoryItem] | Unset = UNSET
    custom_frequencies: list[DictionaryCandidateCustomFrequenciesItem] | Unset = UNSET
    base_form: bool | Unset = UNSET
    inflection: list[str] | Unset = UNSET
    pitch: list[DictionaryCandidatePitchItem] | Unset = UNSET
    parts: list[DictionaryCandidatePartsItem] | Unset = UNSET
    furigana: list[DictionaryCandidateFuriganaItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        headword = self.headword

        reading: None | str
        reading = self.reading

        common = self.common

        name = self.name

        source_id = self.source_id

        dictionary = self.dictionary

        jlpt: None | str
        jlpt = self.jlpt

        frequency: int | None
        frequency = self.frequency

        forms = []
        for forms_item_data in self.forms:
            forms_item = forms_item_data.to_dict()
            forms.append(forms_item)

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        frequency_by_category: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.frequency_by_category, Unset):
            frequency_by_category = []
            for frequency_by_category_item_data in self.frequency_by_category:
                frequency_by_category_item = frequency_by_category_item_data.to_dict()
                frequency_by_category.append(frequency_by_category_item)

        custom_frequencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.custom_frequencies, Unset):
            custom_frequencies = []
            for custom_frequencies_item_data in self.custom_frequencies:
                custom_frequencies_item = custom_frequencies_item_data.to_dict()
                custom_frequencies.append(custom_frequencies_item)

        base_form = self.base_form

        inflection: list[str] | Unset = UNSET
        if not isinstance(self.inflection, Unset):
            inflection = self.inflection

        pitch: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pitch, Unset):
            pitch = []
            for pitch_item_data in self.pitch:
                pitch_item = pitch_item_data.to_dict()
                pitch.append(pitch_item)

        parts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.parts, Unset):
            parts = []
            for parts_item_data in self.parts:
                parts_item = parts_item_data.to_dict()
                parts.append(parts_item)

        furigana: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.furigana, Unset):
            furigana = []
            for furigana_item_data in self.furigana:
                furigana_item = furigana_item_data.to_dict()
                furigana.append(furigana_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "headword": headword,
                "reading": reading,
                "common": common,
                "name": name,
                "sourceId": source_id,
                "dictionary": dictionary,
                "jlpt": jlpt,
                "frequency": frequency,
                "forms": forms,
                "entries": entries,
            }
        )
        if frequency_by_category is not UNSET:
            field_dict["frequencyByCategory"] = frequency_by_category
        if custom_frequencies is not UNSET:
            field_dict["customFrequencies"] = custom_frequencies
        if base_form is not UNSET:
            field_dict["baseForm"] = base_form
        if inflection is not UNSET:
            field_dict["inflection"] = inflection
        if pitch is not UNSET:
            field_dict["pitch"] = pitch
        if parts is not UNSET:
            field_dict["parts"] = parts
        if furigana is not UNSET:
            field_dict["furigana"] = furigana

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_candidate_custom_frequencies_item import (
            DictionaryCandidateCustomFrequenciesItem,  # noqa: PLC0415
        )
        from ..models.dictionary_candidate_entries_item import DictionaryCandidateEntriesItem  # noqa: PLC0415
        from ..models.dictionary_candidate_forms_item import DictionaryCandidateFormsItem  # noqa: PLC0415
        from ..models.dictionary_candidate_frequency_by_category_item import (
            DictionaryCandidateFrequencyByCategoryItem,  # noqa: PLC0415
        )
        from ..models.dictionary_candidate_furigana_item import DictionaryCandidateFuriganaItem  # noqa: PLC0415
        from ..models.dictionary_candidate_parts_item import DictionaryCandidatePartsItem  # noqa: PLC0415
        from ..models.dictionary_candidate_pitch_item import DictionaryCandidatePitchItem  # noqa: PLC0415

        _src = dict(src_dict)
        id = _src.pop("id")

        headword = _src.pop("headword")

        def _parse_reading(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reading = _parse_reading(_src.pop("reading"))

        common = _src.pop("common")

        name = _src.pop("name")

        source_id = _src.pop("sourceId")

        dictionary = _src.pop("dictionary")

        def _parse_jlpt(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        jlpt = _parse_jlpt(_src.pop("jlpt"))

        def _parse_frequency(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        frequency = _parse_frequency(_src.pop("frequency"))

        forms = []
        _forms = _src.pop("forms")
        for forms_item_data in _forms:
            forms_item = DictionaryCandidateFormsItem.from_dict(forms_item_data)

            forms.append(forms_item)

        entries = []
        _entries = _src.pop("entries")
        for entries_item_data in _entries:
            entries_item = DictionaryCandidateEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        _frequency_by_category = _src.pop("frequencyByCategory", UNSET)
        frequency_by_category: list[DictionaryCandidateFrequencyByCategoryItem] | Unset = UNSET
        if _frequency_by_category is not UNSET:
            frequency_by_category = []
            for frequency_by_category_item_data in _frequency_by_category:
                frequency_by_category_item = DictionaryCandidateFrequencyByCategoryItem.from_dict(
                    frequency_by_category_item_data
                )

                frequency_by_category.append(frequency_by_category_item)

        _custom_frequencies = _src.pop("customFrequencies", UNSET)
        custom_frequencies: list[DictionaryCandidateCustomFrequenciesItem] | Unset = UNSET
        if _custom_frequencies is not UNSET:
            custom_frequencies = []
            for custom_frequencies_item_data in _custom_frequencies:
                custom_frequencies_item = DictionaryCandidateCustomFrequenciesItem.from_dict(
                    custom_frequencies_item_data
                )

                custom_frequencies.append(custom_frequencies_item)

        base_form = _src.pop("baseForm", UNSET)

        inflection = cast(list[str], _src.pop("inflection", UNSET))

        _pitch = _src.pop("pitch", UNSET)
        pitch: list[DictionaryCandidatePitchItem] | Unset = UNSET
        if _pitch is not UNSET:
            pitch = []
            for pitch_item_data in _pitch:
                pitch_item = DictionaryCandidatePitchItem.from_dict(pitch_item_data)

                pitch.append(pitch_item)

        _parts = _src.pop("parts", UNSET)
        parts: list[DictionaryCandidatePartsItem] | Unset = UNSET
        if _parts is not UNSET:
            parts = []
            for parts_item_data in _parts:
                parts_item = DictionaryCandidatePartsItem.from_dict(parts_item_data)

                parts.append(parts_item)

        _furigana = _src.pop("furigana", UNSET)
        furigana: list[DictionaryCandidateFuriganaItem] | Unset = UNSET
        if _furigana is not UNSET:
            furigana = []
            for furigana_item_data in _furigana:
                furigana_item = DictionaryCandidateFuriganaItem.from_dict(furigana_item_data)

                furigana.append(furigana_item)

        dictionary_candidate = cls(
            id=id,
            headword=headword,
            reading=reading,
            common=common,
            name=name,
            source_id=source_id,
            dictionary=dictionary,
            jlpt=jlpt,
            frequency=frequency,
            forms=forms,
            entries=entries,
            frequency_by_category=frequency_by_category,
            custom_frequencies=custom_frequencies,
            base_form=base_form,
            inflection=inflection,
            pitch=pitch,
            parts=parts,
            furigana=furigana,
        )

        dictionary_candidate.additional_properties = _src
        return dictionary_candidate

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
