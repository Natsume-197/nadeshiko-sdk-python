from typing import Literal

AdminContentRequestExternalSourceType3Type1 = Literal[
    "ANILIST", "ASIN", "IMDB", "MAL", "TMDB", "TVDB", "YOUTUBE"
]

ADMIN_CONTENT_REQUEST_EXTERNAL_SOURCE_TYPE_3_TYPE_1_VALUES: set[
    AdminContentRequestExternalSourceType3Type1
] = {
    "ANILIST",
    "ASIN",
    "IMDB",
    "MAL",
    "TMDB",
    "TVDB",
    "YOUTUBE",
}


def check_admin_content_request_external_source_type_3_type_1(
    value: str,
) -> AdminContentRequestExternalSourceType3Type1:
    if value in ADMIN_CONTENT_REQUEST_EXTERNAL_SOURCE_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_CONTENT_REQUEST_EXTERNAL_SOURCE_TYPE_3_TYPE_1_VALUES!r}"
    )
