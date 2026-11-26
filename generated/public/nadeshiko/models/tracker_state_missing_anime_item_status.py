from typing import Literal

TrackerStateMissingAnimeItemStatus = Literal[
    "COMPLETED", "DROPPED", "PAUSED", "PLANNING", "WATCHING"
]

TRACKER_STATE_MISSING_ANIME_ITEM_STATUS_VALUES: set[TrackerStateMissingAnimeItemStatus] = {
    "COMPLETED",
    "DROPPED",
    "PAUSED",
    "PLANNING",
    "WATCHING",
}


def check_tracker_state_missing_anime_item_status(value: str) -> TrackerStateMissingAnimeItemStatus:
    if value in TRACKER_STATE_MISSING_ANIME_ITEM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRACKER_STATE_MISSING_ANIME_ITEM_STATUS_VALUES!r}"
    )
