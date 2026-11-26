from typing import Literal

AdminContentRequestPossibleDuplicateOfType0Status = Literal[
    "DECLINED", "IN_PROGRESS", "OPEN", "PLANNED", "RELEASED"
]

ADMIN_CONTENT_REQUEST_POSSIBLE_DUPLICATE_OF_TYPE_0_STATUS_VALUES: set[
    AdminContentRequestPossibleDuplicateOfType0Status
] = {
    "DECLINED",
    "IN_PROGRESS",
    "OPEN",
    "PLANNED",
    "RELEASED",
}


def check_admin_content_request_possible_duplicate_of_type_0_status(
    value: str,
) -> AdminContentRequestPossibleDuplicateOfType0Status:
    if value in ADMIN_CONTENT_REQUEST_POSSIBLE_DUPLICATE_OF_TYPE_0_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_CONTENT_REQUEST_POSSIBLE_DUPLICATE_OF_TYPE_0_STATUS_VALUES!r}"
    )
