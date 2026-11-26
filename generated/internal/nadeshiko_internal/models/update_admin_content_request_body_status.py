from typing import Literal

UpdateAdminContentRequestBodyStatus = Literal[
    "DECLINED", "IN_PROGRESS", "OPEN", "PLANNED", "RELEASED"
]

UPDATE_ADMIN_CONTENT_REQUEST_BODY_STATUS_VALUES: set[UpdateAdminContentRequestBodyStatus] = {
    "DECLINED",
    "IN_PROGRESS",
    "OPEN",
    "PLANNED",
    "RELEASED",
}


def check_update_admin_content_request_body_status(
    value: str,
) -> UpdateAdminContentRequestBodyStatus:
    if value in UPDATE_ADMIN_CONTENT_REQUEST_BODY_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ADMIN_CONTENT_REQUEST_BODY_STATUS_VALUES!r}"
    )
