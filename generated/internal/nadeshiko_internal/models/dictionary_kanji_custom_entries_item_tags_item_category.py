from typing import Literal

DictionaryKanjiCustomEntriesItemTagsItemCategory = Literal[
    "dialect", "field", "misc", "partOfSpeech"
]

DICTIONARY_KANJI_CUSTOM_ENTRIES_ITEM_TAGS_ITEM_CATEGORY_VALUES: set[
    DictionaryKanjiCustomEntriesItemTagsItemCategory
] = {
    "dialect",
    "field",
    "misc",
    "partOfSpeech",
}


def check_dictionary_kanji_custom_entries_item_tags_item_category(
    value: str,
) -> DictionaryKanjiCustomEntriesItemTagsItemCategory:
    if value in DICTIONARY_KANJI_CUSTOM_ENTRIES_ITEM_TAGS_ITEM_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DICTIONARY_KANJI_CUSTOM_ENTRIES_ITEM_TAGS_ITEM_CATEGORY_VALUES!r}"
    )
