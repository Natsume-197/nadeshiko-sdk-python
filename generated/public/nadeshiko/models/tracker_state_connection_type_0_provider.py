from typing import Literal

TrackerStateConnectionType0Provider = Literal["ANILIST", "MAL"]

TRACKER_STATE_CONNECTION_TYPE_0_PROVIDER_VALUES: set[TrackerStateConnectionType0Provider] = {
    "ANILIST",
    "MAL",
}


def check_tracker_state_connection_type_0_provider(
    value: str,
) -> TrackerStateConnectionType0Provider:
    if value in TRACKER_STATE_CONNECTION_TYPE_0_PROVIDER_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRACKER_STATE_CONNECTION_TYPE_0_PROVIDER_VALUES!r}"
    )
