from typing import Literal

DictionaryKanjiReadingsItemKind = Literal["kun", "on"]

DICTIONARY_KANJI_READINGS_ITEM_KIND_VALUES: set[DictionaryKanjiReadingsItemKind] = {
    "kun",
    "on",
}


def check_dictionary_kanji_readings_item_kind(value: str) -> DictionaryKanjiReadingsItemKind:
    if value in DICTIONARY_KANJI_READINGS_ITEM_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DICTIONARY_KANJI_READINGS_ITEM_KIND_VALUES!r}"
    )
