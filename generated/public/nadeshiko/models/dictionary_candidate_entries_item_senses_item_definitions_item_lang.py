from typing import Literal

DictionaryCandidateEntriesItemSensesItemDefinitionsItemLang = Literal["en", "es", "ja"]

DICTIONARY_CANDIDATE_ENTRIES_ITEM_SENSES_ITEM_DEFINITIONS_ITEM_LANG_VALUES: set[
    DictionaryCandidateEntriesItemSensesItemDefinitionsItemLang
] = {
    "en",
    "es",
    "ja",
}


def check_dictionary_candidate_entries_item_senses_item_definitions_item_lang(
    value: str,
) -> DictionaryCandidateEntriesItemSensesItemDefinitionsItemLang:
    if value in DICTIONARY_CANDIDATE_ENTRIES_ITEM_SENSES_ITEM_DEFINITIONS_ITEM_LANG_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DICTIONARY_CANDIDATE_ENTRIES_ITEM_SENSES_ITEM_DEFINITIONS_ITEM_LANG_VALUES!r}"
    )
