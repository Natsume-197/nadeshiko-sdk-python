from typing import Literal

TrackerStateConfiguredProvidersItem = Literal["ANILIST", "MAL"]

TRACKER_STATE_CONFIGURED_PROVIDERS_ITEM_VALUES: set[TrackerStateConfiguredProvidersItem] = {
    "ANILIST",
    "MAL",
}


def check_tracker_state_configured_providers_item(
    value: str,
) -> TrackerStateConfiguredProvidersItem:
    if value in TRACKER_STATE_CONFIGURED_PROVIDERS_ITEM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRACKER_STATE_CONFIGURED_PROVIDERS_ITEM_VALUES!r}"
    )
