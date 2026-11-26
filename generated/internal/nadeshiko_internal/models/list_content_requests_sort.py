from typing import Literal

ListContentRequestsSort = Literal["RECENT", "TOP"]

LIST_CONTENT_REQUESTS_SORT_VALUES: set[ListContentRequestsSort] = {
    "RECENT",
    "TOP",
}


def check_list_content_requests_sort(value: str) -> ListContentRequestsSort:
    if value in LIST_CONTENT_REQUESTS_SORT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CONTENT_REQUESTS_SORT_VALUES!r}"
    )
