from typing import Literal

ListMyContentRequestsSort = Literal["RECENT", "TOP"]

LIST_MY_CONTENT_REQUESTS_SORT_VALUES: set[ListMyContentRequestsSort] = {
    "RECENT",
    "TOP",
}


def check_list_my_content_requests_sort(value: str) -> ListMyContentRequestsSort:
    if value in LIST_MY_CONTENT_REQUESTS_SORT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MY_CONTENT_REQUESTS_SORT_VALUES!r}"
    )
