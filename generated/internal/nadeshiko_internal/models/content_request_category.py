from typing import Literal

ContentRequestCategory = Literal["ANIME", "AUDIOBOOK", "JDRAMA", "YOUTUBE"]

CONTENT_REQUEST_CATEGORY_VALUES: set[ContentRequestCategory] = {
    "ANIME",
    "AUDIOBOOK",
    "JDRAMA",
    "YOUTUBE",
}


def check_content_request_category(value: str) -> ContentRequestCategory:
    if value in CONTENT_REQUEST_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTENT_REQUEST_CATEGORY_VALUES!r}"
    )
