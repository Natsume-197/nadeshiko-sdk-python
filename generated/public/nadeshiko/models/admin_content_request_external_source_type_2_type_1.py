from typing import Literal

AdminContentRequestExternalSourceType2Type1 = Literal[
    "ANILIST", "ASIN", "IMDB", "MAL", "TMDB", "TVDB", "YOUTUBE"
]

ADMIN_CONTENT_REQUEST_EXTERNAL_SOURCE_TYPE_2_TYPE_1_VALUES: set[
    AdminContentRequestExternalSourceType2Type1
] = {
    "ANILIST",
    "ASIN",
    "IMDB",
    "MAL",
    "TMDB",
    "TVDB",
    "YOUTUBE",
}


def check_admin_content_request_external_source_type_2_type_1(
    value: str,
) -> AdminContentRequestExternalSourceType2Type1:
    if value in ADMIN_CONTENT_REQUEST_EXTERNAL_SOURCE_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_CONTENT_REQUEST_EXTERNAL_SOURCE_TYPE_2_TYPE_1_VALUES!r}"
    )
