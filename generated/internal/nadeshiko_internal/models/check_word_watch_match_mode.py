from typing import Literal

CheckWordWatchMatchMode = Literal["CONTAINS", "EXACT", "WORD"]

CHECK_WORD_WATCH_MATCH_MODE_VALUES: set[CheckWordWatchMatchMode] = {
    "CONTAINS",
    "EXACT",
    "WORD",
}


def check_check_word_watch_match_mode(value: str) -> CheckWordWatchMatchMode:
    if value in CHECK_WORD_WATCH_MATCH_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CHECK_WORD_WATCH_MATCH_MODE_VALUES!r}"
    )
