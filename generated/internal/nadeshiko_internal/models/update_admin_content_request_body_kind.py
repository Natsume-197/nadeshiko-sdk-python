from typing import Literal

UpdateAdminContentRequestBodyKind = Literal["NEW", "UPDATE"]

UPDATE_ADMIN_CONTENT_REQUEST_BODY_KIND_VALUES: set[UpdateAdminContentRequestBodyKind] = {
    "NEW",
    "UPDATE",
}


def check_update_admin_content_request_body_kind(value: str) -> UpdateAdminContentRequestBodyKind:
    if value in UPDATE_ADMIN_CONTENT_REQUEST_BODY_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ADMIN_CONTENT_REQUEST_BODY_KIND_VALUES!r}"
    )
