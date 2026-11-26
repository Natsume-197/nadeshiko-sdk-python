from typing import Literal

StartTrackerLinkBodyProvider = Literal["ANILIST", "MAL"]

START_TRACKER_LINK_BODY_PROVIDER_VALUES: set[StartTrackerLinkBodyProvider] = {
    "ANILIST",
    "MAL",
}


def check_start_tracker_link_body_provider(value: str) -> StartTrackerLinkBodyProvider:
    if value in START_TRACKER_LINK_BODY_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {START_TRACKER_LINK_BODY_PROVIDER_VALUES!r}"
    )
