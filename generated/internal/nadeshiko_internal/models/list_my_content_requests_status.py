from typing import Literal

ListMyContentRequestsStatus = Literal["ACTIVE", "ALL", "DECLINED", "IN_PROGRESS", "RELEASED"]

LIST_MY_CONTENT_REQUESTS_STATUS_VALUES: set[ListMyContentRequestsStatus] = {
    "ACTIVE",
    "ALL",
    "DECLINED",
    "IN_PROGRESS",
    "RELEASED",
}


def check_list_my_content_requests_status(value: str) -> ListMyContentRequestsStatus:
    if value in LIST_MY_CONTENT_REQUESTS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MY_CONTENT_REQUESTS_STATUS_VALUES!r}"
    )
