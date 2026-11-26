from typing import Literal

TrackerStateMissingAnimeItemRequestType0Status = Literal[
    "DECLINED", "IN_PROGRESS", "OPEN", "PLANNED"
]

TRACKER_STATE_MISSING_ANIME_ITEM_REQUEST_TYPE_0_STATUS_VALUES: set[
    TrackerStateMissingAnimeItemRequestType0Status
] = {
    "DECLINED",
    "IN_PROGRESS",
    "OPEN",
    "PLANNED",
}


def check_tracker_state_missing_anime_item_request_type_0_status(
    value: str,
) -> TrackerStateMissingAnimeItemRequestType0Status:
    if value in TRACKER_STATE_MISSING_ANIME_ITEM_REQUEST_TYPE_0_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRACKER_STATE_MISSING_ANIME_ITEM_REQUEST_TYPE_0_STATUS_VALUES!r}"
    )
