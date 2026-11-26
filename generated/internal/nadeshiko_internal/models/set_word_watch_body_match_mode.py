from typing import Literal

SetWordWatchBodyMatchMode = Literal["CONTAINS", "EXACT", "WORD"]

SET_WORD_WATCH_BODY_MATCH_MODE_VALUES: set[SetWordWatchBodyMatchMode] = {
    "CONTAINS",
    "EXACT",
    "WORD",
}


def check_set_word_watch_body_match_mode(value: str) -> SetWordWatchBodyMatchMode:
    if value in SET_WORD_WATCH_BODY_MATCH_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SET_WORD_WATCH_BODY_MATCH_MODE_VALUES!r}"
    )
