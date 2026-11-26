from typing import Literal

ContentRequestKind = Literal["NEW", "UPDATE"]

CONTENT_REQUEST_KIND_VALUES: set[ContentRequestKind] = {
    "NEW",
    "UPDATE",
}


def check_content_request_kind(value: str) -> ContentRequestKind:
    if value in CONTENT_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CONTENT_REQUEST_KIND_VALUES!r}")
