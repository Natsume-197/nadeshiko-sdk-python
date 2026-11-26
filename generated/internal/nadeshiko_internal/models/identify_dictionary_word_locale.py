from typing import Literal

IdentifyDictionaryWordLocale = Literal["en", "es"]

IDENTIFY_DICTIONARY_WORD_LOCALE_VALUES: set[IdentifyDictionaryWordLocale] = {
    "en",
    "es",
}


def check_identify_dictionary_word_locale(value: str) -> IdentifyDictionaryWordLocale:
    if value in IDENTIFY_DICTIONARY_WORD_LOCALE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {IDENTIFY_DICTIONARY_WORD_LOCALE_VALUES!r}"
    )
