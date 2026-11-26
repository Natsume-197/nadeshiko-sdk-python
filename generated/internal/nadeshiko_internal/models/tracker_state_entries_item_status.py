from typing import Literal

TrackerStateEntriesItemStatus = Literal["COMPLETED", "DROPPED", "PAUSED", "PLANNING", "WATCHING"]

TRACKER_STATE_ENTRIES_ITEM_STATUS_VALUES: set[TrackerStateEntriesItemStatus] = {
    "COMPLETED",
    "DROPPED",
    "PAUSED",
    "PLANNING",
    "WATCHING",
}


def check_tracker_state_entries_item_status(value: str) -> TrackerStateEntriesItemStatus:
    if value in TRACKER_STATE_ENTRIES_ITEM_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRACKER_STATE_ENTRIES_ITEM_STATUS_VALUES!r}"
    )
