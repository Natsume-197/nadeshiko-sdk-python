from typing import Literal

WordWatchSetResponseOutcome = Literal["created", "updated"]

WORD_WATCH_SET_RESPONSE_OUTCOME_VALUES: set[WordWatchSetResponseOutcome] = {
    "created",
    "updated",
}


def check_word_watch_set_response_outcome(value: str) -> WordWatchSetResponseOutcome:
    if value in WORD_WATCH_SET_RESPONSE_OUTCOME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORD_WATCH_SET_RESPONSE_OUTCOME_VALUES!r}"
    )
