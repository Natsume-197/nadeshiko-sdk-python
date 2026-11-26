from typing import Literal

DictionaryKanjiMeaningsLanguage = Literal["en", "es"]

DICTIONARY_KANJI_MEANINGS_LANGUAGE_VALUES: set[DictionaryKanjiMeaningsLanguage] = {
    "en",
    "es",
}


def check_dictionary_kanji_meanings_language(value: str) -> DictionaryKanjiMeaningsLanguage:
    if value in DICTIONARY_KANJI_MEANINGS_LANGUAGE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DICTIONARY_KANJI_MEANINGS_LANGUAGE_VALUES!r}"
    )
