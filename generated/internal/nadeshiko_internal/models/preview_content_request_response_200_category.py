from typing import Literal

PreviewContentRequestResponse200Category = Literal["ANIME", "AUDIOBOOK", "JDRAMA", "YOUTUBE"]

PREVIEW_CONTENT_REQUEST_RESPONSE_200_CATEGORY_VALUES: set[
    PreviewContentRequestResponse200Category
] = {
    "ANIME",
    "AUDIOBOOK",
    "JDRAMA",
    "YOUTUBE",
}


def check_preview_content_request_response_200_category(
    value: str,
) -> PreviewContentRequestResponse200Category:
    if value in PREVIEW_CONTENT_REQUEST_RESPONSE_200_CATEGORY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PREVIEW_CONTENT_REQUEST_RESPONSE_200_CATEGORY_VALUES!r}"
    )
