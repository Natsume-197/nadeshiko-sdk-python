from typing import Literal

ListMyContentRequestsCategory = Literal["ANIME", "AUDIOBOOK", "JDRAMA", "YOUTUBE"]

LIST_MY_CONTENT_REQUESTS_CATEGORY_VALUES: set[ListMyContentRequestsCategory] = {
    "ANIME",
    "AUDIOBOOK",
    "JDRAMA",
    "YOUTUBE",
}


def check_list_my_content_requests_category(value: str) -> ListMyContentRequestsCategory:
    if value in LIST_MY_CONTENT_REQUESTS_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MY_CONTENT_REQUESTS_CATEGORY_VALUES!r}"
    )
