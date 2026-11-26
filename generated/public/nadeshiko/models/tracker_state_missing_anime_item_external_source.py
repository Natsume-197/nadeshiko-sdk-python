from typing import Literal

TrackerStateMissingAnimeItemExternalSource = Literal["ANILIST", "MAL"]

TRACKER_STATE_MISSING_ANIME_ITEM_EXTERNAL_SOURCE_VALUES: set[
    TrackerStateMissingAnimeItemExternalSource
] = {
    "ANILIST",
    "MAL",
}


def check_tracker_state_missing_anime_item_external_source(
    value: str,
) -> TrackerStateMissingAnimeItemExternalSource:
    if value in TRACKER_STATE_MISSING_ANIME_ITEM_EXTERNAL_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRACKER_STATE_MISSING_ANIME_ITEM_EXTERNAL_SOURCE_VALUES!r}"
    )
