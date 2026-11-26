from typing import Literal

AdminEmailSendSource = Literal["backfill", "live"]

ADMIN_EMAIL_SEND_SOURCE_VALUES: set[AdminEmailSendSource] = {
    "backfill",
    "live",
}


def check_admin_email_send_source(value: str) -> AdminEmailSendSource:
    if value in ADMIN_EMAIL_SEND_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_EMAIL_SEND_SOURCE_VALUES!r}"
    )
