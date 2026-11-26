from typing import Literal

DictionaryCandidateFormsItemScript = Literal["kana", "kanji"]

DICTIONARY_CANDIDATE_FORMS_ITEM_SCRIPT_VALUES: set[DictionaryCandidateFormsItemScript] = {
    "kana",
    "kanji",
}


def check_dictionary_candidate_forms_item_script(value: str) -> DictionaryCandidateFormsItemScript:
    if value in DICTIONARY_CANDIDATE_FORMS_ITEM_SCRIPT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DICTIONARY_CANDIDATE_FORMS_ITEM_SCRIPT_VALUES!r}"
    )
