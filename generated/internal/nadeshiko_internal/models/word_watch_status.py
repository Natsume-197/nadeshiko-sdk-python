from typing import Literal

WordWatchStatus = Literal["ACTIVE", "FULFILLED", "PAUSED"]

WORD_WATCH_STATUS_VALUES: set[WordWatchStatus] = {
    "ACTIVE",
    "FULFILLED",
    "PAUSED",
}


def check_word_watch_status(value: str) -> WordWatchStatus:
    if value in WORD_WATCH_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORD_WATCH_STATUS_VALUES!r}")
