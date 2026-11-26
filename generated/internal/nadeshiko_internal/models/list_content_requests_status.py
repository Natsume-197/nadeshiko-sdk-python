from typing import Literal

ListContentRequestsStatus = Literal["ACTIVE", "DECLINED", "IN_PROGRESS", "RELEASED"]

LIST_CONTENT_REQUESTS_STATUS_VALUES: set[ListContentRequestsStatus] = {
    "ACTIVE",
    "DECLINED",
    "IN_PROGRESS",
    "RELEASED",
}


def check_list_content_requests_status(value: str) -> ListContentRequestsStatus:
    if value in LIST_CONTENT_REQUESTS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_CONTENT_REQUESTS_STATUS_VALUES!r}"
    )
