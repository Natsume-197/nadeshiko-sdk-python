from typing import Literal

ListAdminContentRequestsCategory = Literal["ANIME", "AUDIOBOOK", "JDRAMA", "YOUTUBE"]

LIST_ADMIN_CONTENT_REQUESTS_CATEGORY_VALUES: set[ListAdminContentRequestsCategory] = {
    "ANIME",
    "AUDIOBOOK",
    "JDRAMA",
    "YOUTUBE",
}


def check_list_admin_content_requests_category(value: str) -> ListAdminContentRequestsCategory:
    if value in LIST_ADMIN_CONTENT_REQUESTS_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ADMIN_CONTENT_REQUESTS_CATEGORY_VALUES!r}"
    )
