from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.dictionary_kanji_meanings_language import (
    DictionaryKanjiMeaningsLanguage,
    check_dictionary_kanji_meanings_language,
)

if TYPE_CHECKING:
    from ..models.dictionary_kanji_components_item import DictionaryKanjiComponentsItem
    from ..models.dictionary_kanji_radical_type_0 import DictionaryKanjiRadicalType0
    from ..models.dictionary_kanji_readings_item import DictionaryKanjiReadingsItem
    from ..models.dictionary_kanji_related import DictionaryKanjiRelated
    from ..models.dictionary_kanji_words_item import DictionaryKanjiWordsItem


T = TypeVar("T", bound="DictionaryKanji")


@_attrs_define
class DictionaryKanji:
    """One kanji as the word card's kanji view draws it (task 44).

    Attributes:
        character (str):  Example: 食.
        stroke_count (int):  Example: 9.
        grade (int | None): KANJIDIC2 school grade. 1-6 elementary school, 8 the rest of the jōyō list, 9-10 jinmeiyō.
            Example: 2.
        frequency (int | None): Rank among the 2,500 kanji most used in newspapers (KANJIDIC2). Example: 328.
        corpus_rank (int | None): Rank by how often it is written in Nadeshiko's sentences (anime, drama, audiobooks and
            YouTube), 1 for the most written. Null until the frequency job has counted it. Example: 77.
        jlpt (int | None): Current JLPT level, 5 for N5 (Jonathan Waller's unofficial lists). Example: 5.
        kanken (None | str): Kanji Kentei (漢検) level it is tested at, `10級` (easiest) to `1級` (mimneko/kanji-data, CC0).
            Example: 9級.
        radical (DictionaryKanjiRadicalType0 | None): The classical (Kangxi) radical it is filed under, named by Kanji
            alive.
        readings (list[DictionaryKanjiReadingsItem]): On readings first, then kun, each with up to three of the corpus's
            most frequent words read that way.
        meanings (list[str]):  Example: ['eat', 'food'].
        meanings_language (DictionaryKanjiMeaningsLanguage): The language `meanings` are in; English when KANJIDIC2 has
            none in the requested one.
        components (list[DictionaryKanjiComponentsItem]): The parts it is built from (KRADFILE).
        strokes (list[str]): One SVG path per stroke in writing order, in KanjiVG's 109×109 view box. Empty when not
            drawn.
        stroke_numbers (list[list[float]]): Where KanjiVG places each stroke's number, as `[x, y]`. Empty when it has
            none.
        words (list[DictionaryKanjiWordsItem]): Words written with this kanji, most frequent in Nadeshiko's corpus first
            (up to 40).
        same_radical (list[DictionaryKanjiRelated]): Other kanji filed under the same radical, school kanji first (12,
            or all with `related=all`).
        same_radical_count (int):  Example: 92.
        contained_in (list[DictionaryKanjiRelated]): Kanji with this one as a part and filed under another radical,
            school kanji first (12, or all with `related=all`).
        contained_in_count (int):  Example: 5.
    """

    character: str
    stroke_count: int
    grade: int | None
    frequency: int | None
    corpus_rank: int | None
    jlpt: int | None
    kanken: None | str
    radical: DictionaryKanjiRadicalType0 | None
    readings: list[DictionaryKanjiReadingsItem]
    meanings: list[str]
    meanings_language: DictionaryKanjiMeaningsLanguage
    components: list[DictionaryKanjiComponentsItem]
    strokes: list[str]
    stroke_numbers: list[list[float]]
    words: list[DictionaryKanjiWordsItem]
    same_radical: list[DictionaryKanjiRelated]
    same_radical_count: int
    contained_in: list[DictionaryKanjiRelated]
    contained_in_count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.dictionary_kanji_radical_type_0 import DictionaryKanjiRadicalType0  # noqa: PLC0415

        character = self.character

        stroke_count = self.stroke_count

        grade: int | None
        grade = self.grade

        frequency: int | None
        frequency = self.frequency

        corpus_rank: int | None
        corpus_rank = self.corpus_rank

        jlpt: int | None
        jlpt = self.jlpt

        kanken: None | str
        kanken = self.kanken

        radical: dict[str, Any] | None
        if isinstance(self.radical, DictionaryKanjiRadicalType0):
            radical = self.radical.to_dict()
        else:
            radical = self.radical

        readings = []
        for readings_item_data in self.readings:
            readings_item = readings_item_data.to_dict()
            readings.append(readings_item)

        meanings = self.meanings

        meanings_language: str = self.meanings_language

        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        strokes = self.strokes

        stroke_numbers = []
        for stroke_numbers_item_data in self.stroke_numbers:
            stroke_numbers_item = stroke_numbers_item_data

            stroke_numbers.append(stroke_numbers_item)

        words = []
        for words_item_data in self.words:
            words_item = words_item_data.to_dict()
            words.append(words_item)

        same_radical = []
        for same_radical_item_data in self.same_radical:
            same_radical_item = same_radical_item_data.to_dict()
            same_radical.append(same_radical_item)

        same_radical_count = self.same_radical_count

        contained_in = []
        for contained_in_item_data in self.contained_in:
            contained_in_item = contained_in_item_data.to_dict()
            contained_in.append(contained_in_item)

        contained_in_count = self.contained_in_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "character": character,
                "strokeCount": stroke_count,
                "grade": grade,
                "frequency": frequency,
                "corpusRank": corpus_rank,
                "jlpt": jlpt,
                "kanken": kanken,
                "radical": radical,
                "readings": readings,
                "meanings": meanings,
                "meaningsLanguage": meanings_language,
                "components": components,
                "strokes": strokes,
                "strokeNumbers": stroke_numbers,
                "words": words,
                "sameRadical": same_radical,
                "sameRadicalCount": same_radical_count,
                "containedIn": contained_in,
                "containedInCount": contained_in_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_kanji_components_item import DictionaryKanjiComponentsItem  # noqa: PLC0415
        from ..models.dictionary_kanji_radical_type_0 import DictionaryKanjiRadicalType0  # noqa: PLC0415
        from ..models.dictionary_kanji_readings_item import DictionaryKanjiReadingsItem  # noqa: PLC0415
        from ..models.dictionary_kanji_related import DictionaryKanjiRelated  # noqa: PLC0415
        from ..models.dictionary_kanji_words_item import DictionaryKanjiWordsItem  # noqa: PLC0415

        _src = dict(src_dict)
        character = _src.pop("character")

        stroke_count = _src.pop("strokeCount")

        def _parse_grade(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        grade = _parse_grade(_src.pop("grade"))

        def _parse_frequency(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        frequency = _parse_frequency(_src.pop("frequency"))

        def _parse_corpus_rank(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        corpus_rank = _parse_corpus_rank(_src.pop("corpusRank"))

        def _parse_jlpt(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        jlpt = _parse_jlpt(_src.pop("jlpt"))

        def _parse_kanken(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        kanken = _parse_kanken(_src.pop("kanken"))

        def _parse_radical(data: object) -> DictionaryKanjiRadicalType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                radical_type_0 = DictionaryKanjiRadicalType0.from_dict(data)

                return radical_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DictionaryKanjiRadicalType0 | None, data)

        radical = _parse_radical(_src.pop("radical"))

        readings = []
        _readings = _src.pop("readings")
        for readings_item_data in _readings:
            readings_item = DictionaryKanjiReadingsItem.from_dict(readings_item_data)

            readings.append(readings_item)

        meanings = cast(list[str], _src.pop("meanings"))

        meanings_language = check_dictionary_kanji_meanings_language(_src.pop("meaningsLanguage"))

        components = []
        _components = _src.pop("components")
        for components_item_data in _components:
            components_item = DictionaryKanjiComponentsItem.from_dict(components_item_data)

            components.append(components_item)

        strokes = cast(list[str], _src.pop("strokes"))

        stroke_numbers = []
        _stroke_numbers = _src.pop("strokeNumbers")
        for stroke_numbers_item_data in _stroke_numbers:
            stroke_numbers_item = cast(list[float], stroke_numbers_item_data)

            stroke_numbers.append(stroke_numbers_item)

        words = []
        _words = _src.pop("words")
        for words_item_data in _words:
            words_item = DictionaryKanjiWordsItem.from_dict(words_item_data)

            words.append(words_item)

        same_radical = []
        _same_radical = _src.pop("sameRadical")
        for same_radical_item_data in _same_radical:
            same_radical_item = DictionaryKanjiRelated.from_dict(same_radical_item_data)

            same_radical.append(same_radical_item)

        same_radical_count = _src.pop("sameRadicalCount")

        contained_in = []
        _contained_in = _src.pop("containedIn")
        for contained_in_item_data in _contained_in:
            contained_in_item = DictionaryKanjiRelated.from_dict(contained_in_item_data)

            contained_in.append(contained_in_item)

        contained_in_count = _src.pop("containedInCount")

        dictionary_kanji = cls(
            character=character,
            stroke_count=stroke_count,
            grade=grade,
            frequency=frequency,
            corpus_rank=corpus_rank,
            jlpt=jlpt,
            kanken=kanken,
            radical=radical,
            readings=readings,
            meanings=meanings,
            meanings_language=meanings_language,
            components=components,
            strokes=strokes,
            stroke_numbers=stroke_numbers,
            words=words,
            same_radical=same_radical,
            same_radical_count=same_radical_count,
            contained_in=contained_in,
            contained_in_count=contained_in_count,
        )

        dictionary_kanji.additional_properties = _src
        return dictionary_kanji

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
