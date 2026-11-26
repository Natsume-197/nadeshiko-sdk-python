from typing import Literal

GetDictionaryKanjiLocale = Literal["en", "es"]

GET_DICTIONARY_KANJI_LOCALE_VALUES: set[GetDictionaryKanjiLocale] = {
    "en",
    "es",
}


def check_get_dictionary_kanji_locale(value: str) -> GetDictionaryKanjiLocale:
    if value in GET_DICTIONARY_KANJI_LOCALE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_DICTIONARY_KANJI_LOCALE_VALUES!r}"
    )
