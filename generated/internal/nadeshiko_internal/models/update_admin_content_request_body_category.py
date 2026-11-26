from typing import Literal

UpdateAdminContentRequestBodyCategory = Literal["ANIME", "AUDIOBOOK", "JDRAMA", "YOUTUBE"]

UPDATE_ADMIN_CONTENT_REQUEST_BODY_CATEGORY_VALUES: set[UpdateAdminContentRequestBodyCategory] = {
    "ANIME",
    "AUDIOBOOK",
    "JDRAMA",
    "YOUTUBE",
}


def check_update_admin_content_request_body_category(
    value: str,
) -> UpdateAdminContentRequestBodyCategory:
    if value in UPDATE_ADMIN_CONTENT_REQUEST_BODY_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {UPDATE_ADMIN_CONTENT_REQUEST_BODY_CATEGORY_VALUES!r}"
    )
