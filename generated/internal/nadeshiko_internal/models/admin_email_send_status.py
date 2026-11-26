from typing import Literal

AdminEmailSendStatus = Literal["bounced", "complained", "delivered", "failed", "sent", "suppressed"]

ADMIN_EMAIL_SEND_STATUS_VALUES: set[AdminEmailSendStatus] = {
    "bounced",
    "complained",
    "delivered",
    "failed",
    "sent",
    "suppressed",
}


def check_admin_email_send_status(value: str) -> AdminEmailSendStatus:
    if value in ADMIN_EMAIL_SEND_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_EMAIL_SEND_STATUS_VALUES!r}"
    )
