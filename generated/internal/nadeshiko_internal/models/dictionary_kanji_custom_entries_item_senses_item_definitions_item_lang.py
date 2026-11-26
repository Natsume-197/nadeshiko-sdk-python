from typing import Literal

DictionaryKanjiCustomEntriesItemSensesItemDefinitionsItemLang = Literal["en", "es", "ja"]

DICTIONARY_KANJI_CUSTOM_ENTRIES_ITEM_SENSES_ITEM_DEFINITIONS_ITEM_LANG_VALUES: set[
    DictionaryKanjiCustomEntriesItemSensesItemDefinitionsItemLang
] = {
    "en",
    "es",
    "ja",
}


def check_dictionary_kanji_custom_entries_item_senses_item_definitions_item_lang(
    value: str,
) -> DictionaryKanjiCustomEntriesItemSensesItemDefinitionsItemLang:
    if value in DICTIONARY_KANJI_CUSTOM_ENTRIES_ITEM_SENSES_ITEM_DEFINITIONS_ITEM_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DICTIONARY_KANJI_CUSTOM_ENTRIES_ITEM_SENSES_ITEM_DEFINITIONS_ITEM_LANG_VALUES!r}"
    )
