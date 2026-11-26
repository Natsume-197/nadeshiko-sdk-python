from typing import Literal

DictionaryCandidateEntriesItemSensesItemTagsItemCategory = Literal[
    "dialect", "field", "misc", "partOfSpeech"
]

DICTIONARY_CANDIDATE_ENTRIES_ITEM_SENSES_ITEM_TAGS_ITEM_CATEGORY_VALUES: set[
    DictionaryCandidateEntriesItemSensesItemTagsItemCategory
] = {
    "dialect",
    "field",
    "misc",
    "partOfSpeech",
}


def check_dictionary_candidate_entries_item_senses_item_tags_item_category(
    value: str,
) -> DictionaryCandidateEntriesItemSensesItemTagsItemCategory:
    if value in DICTIONARY_CANDIDATE_ENTRIES_ITEM_SENSES_ITEM_TAGS_ITEM_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DICTIONARY_CANDIDATE_ENTRIES_ITEM_SENSES_ITEM_TAGS_ITEM_CATEGORY_VALUES!r}"
    )
