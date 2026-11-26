from typing import Literal

CompleteTrackerLinkBodyProvider = Literal["ANILIST", "MAL"]

COMPLETE_TRACKER_LINK_BODY_PROVIDER_VALUES: set[CompleteTrackerLinkBodyProvider] = {
    "ANILIST",
    "MAL",
}


def check_complete_tracker_link_body_provider(value: str) -> CompleteTrackerLinkBodyProvider:
    if value in COMPLETE_TRACKER_LINK_BODY_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMPLETE_TRACKER_LINK_BODY_PROVIDER_VALUES!r}"
    )
