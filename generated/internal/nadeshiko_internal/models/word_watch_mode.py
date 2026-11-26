from typing import Literal

WordWatchMode = Literal["FIRST", "NEW_SENTENCES"]

WORD_WATCH_MODE_VALUES: set[WordWatchMode] = {
    "FIRST",
    "NEW_SENTENCES",
}


def check_word_watch_mode(value: str) -> WordWatchMode:
    if value in WORD_WATCH_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORD_WATCH_MODE_VALUES!r}")
