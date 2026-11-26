from typing import Literal

SetWordWatchBodyMode = Literal["FIRST", "NEW_SENTENCES"]

SET_WORD_WATCH_BODY_MODE_VALUES: set[SetWordWatchBodyMode] = {
    "FIRST",
    "NEW_SENTENCES",
}


def check_set_word_watch_body_mode(value: str) -> SetWordWatchBodyMode:
    if value in SET_WORD_WATCH_BODY_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_WORD_WATCH_BODY_MODE_VALUES!r}"
    )
