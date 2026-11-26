from typing import Literal

ListAdminContentRequestsStatus = Literal["DECLINED", "IN_PROGRESS", "OPEN", "PLANNED", "RELEASED"]

LIST_ADMIN_CONTENT_REQUESTS_STATUS_VALUES: set[ListAdminContentRequestsStatus] = {
    "DECLINED",
    "IN_PROGRESS",
    "OPEN",
    "PLANNED",
    "RELEASED",
}


def check_list_admin_content_requests_status(value: str) -> ListAdminContentRequestsStatus:
    if value in LIST_ADMIN_CONTENT_REQUESTS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ADMIN_CONTENT_REQUESTS_STATUS_VALUES!r}"
    )
