from typing import Literal

ListMyContentRequestsScope = Literal["OWN", "VOTED"]

LIST_MY_CONTENT_REQUESTS_SCOPE_VALUES: set[ListMyContentRequestsScope] = {
    "OWN",
    "VOTED",
}


def check_list_my_content_requests_scope(value: str) -> ListMyContentRequestsScope:
    if value in LIST_MY_CONTENT_REQUESTS_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_MY_CONTENT_REQUESTS_SCOPE_VALUES!r}"
    )
