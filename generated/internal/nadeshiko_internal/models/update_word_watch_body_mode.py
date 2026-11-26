from typing import Literal

UpdateWordWatchBodyMode = Literal["FIRST", "NEW_SENTENCES"]

UPDATE_WORD_WATCH_BODY_MODE_VALUES: set[UpdateWordWatchBodyMode] = {
    "FIRST",
    "NEW_SENTENCES",
}


def check_update_word_watch_body_mode(value: str) -> UpdateWordWatchBodyMode:
    if value in UPDATE_WORD_WATCH_BODY_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_WORD_WATCH_BODY_MODE_VALUES!r}"
    )
