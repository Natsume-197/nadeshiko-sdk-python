from typing import Literal

ListContentRequestsCategory = Literal["ANIME", "AUDIOBOOK", "JDRAMA", "YOUTUBE"]

LIST_CONTENT_REQUESTS_CATEGORY_VALUES: set[ListContentRequestsCategory] = {
    "ANIME",
    "AUDIOBOOK",
    "JDRAMA",
    "YOUTUBE",
}


def check_list_content_requests_category(value: str) -> ListContentRequestsCategory:
    if value in LIST_CONTENT_REQUESTS_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CONTENT_REQUESTS_CATEGORY_VALUES!r}"
    )
