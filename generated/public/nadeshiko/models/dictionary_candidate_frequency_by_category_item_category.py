from typing import Literal

DictionaryCandidateFrequencyByCategoryItemCategory = Literal[
    "ANIME", "AUDIOBOOK", "JDRAMA", "YOUTUBE"
]

DICTIONARY_CANDIDATE_FREQUENCY_BY_CATEGORY_ITEM_CATEGORY_VALUES: set[
    DictionaryCandidateFrequencyByCategoryItemCategory
] = {
    "ANIME",
    "AUDIOBOOK",
    "JDRAMA",
    "YOUTUBE",
}


def check_dictionary_candidate_frequency_by_category_item_category(
    value: str,
) -> DictionaryCandidateFrequencyByCategoryItemCategory:
    if value in DICTIONARY_CANDIDATE_FREQUENCY_BY_CATEGORY_ITEM_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DICTIONARY_CANDIDATE_FREQUENCY_BY_CATEGORY_ITEM_CATEGORY_VALUES!r}"
    )
