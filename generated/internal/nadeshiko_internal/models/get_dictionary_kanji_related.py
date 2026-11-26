from typing import Literal

GetDictionaryKanjiRelated = Literal["all", "short"]

GET_DICTIONARY_KANJI_RELATED_VALUES: set[GetDictionaryKanjiRelated] = {
    "all",
    "short",
}


def check_get_dictionary_kanji_related(value: str) -> GetDictionaryKanjiRelated:
    if value in GET_DICTIONARY_KANJI_RELATED_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DICTIONARY_KANJI_RELATED_VALUES!r}"
    )
