from typing import Literal

GetDictionaryKanjiIndexLocale = Literal["en", "es"]

GET_DICTIONARY_KANJI_INDEX_LOCALE_VALUES: set[GetDictionaryKanjiIndexLocale] = {
    "en",
    "es",
}


def check_get_dictionary_kanji_index_locale(value: str) -> GetDictionaryKanjiIndexLocale:
    if value in GET_DICTIONARY_KANJI_INDEX_LOCALE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DICTIONARY_KANJI_INDEX_LOCALE_VALUES!r}"
    )
