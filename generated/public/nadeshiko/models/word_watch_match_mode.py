from typing import Literal

WordWatchMatchMode = Literal["CONTAINS", "EXACT", "WORD"]

WORD_WATCH_MATCH_MODE_VALUES: set[WordWatchMatchMode] = {
    "CONTAINS",
    "EXACT",
    "WORD",
}


def check_word_watch_match_mode(value: str) -> WordWatchMatchMode:
    if value in WORD_WATCH_MATCH_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORD_WATCH_MATCH_MODE_VALUES!r}")
