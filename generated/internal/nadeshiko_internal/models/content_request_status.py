from typing import Literal

ContentRequestStatus = Literal["DECLINED", "IN_PROGRESS", "OPEN", "PLANNED", "RELEASED"]

CONTENT_REQUEST_STATUS_VALUES: set[ContentRequestStatus] = {
    "DECLINED",
    "IN_PROGRESS",
    "OPEN",
    "PLANNED",
    "RELEASED",
}


def check_content_request_status(value: str) -> ContentRequestStatus:
    if value in CONTENT_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CONTENT_REQUEST_STATUS_VALUES!r}"
    )
