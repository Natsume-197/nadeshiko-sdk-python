from typing import Literal

NotificationKind = Literal["request-update", "word-available", "word-digest"]

NOTIFICATION_KIND_VALUES: set[NotificationKind] = {
    "request-update",
    "word-available",
    "word-digest",
}


def check_notification_kind(value: str) -> NotificationKind:
    if value in NOTIFICATION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NOTIFICATION_KIND_VALUES!r}")
