from typing import Literal

ListAdminEmailsStatus = Literal[
    "bounced", "complained", "delivered", "failed", "sent", "suppressed"
]

LIST_ADMIN_EMAILS_STATUS_VALUES: set[ListAdminEmailsStatus] = {
    "bounced",
    "complained",
    "delivered",
    "failed",
    "sent",
    "suppressed",
}


def check_list_admin_emails_status(value: str) -> ListAdminEmailsStatus:
    if value in LIST_ADMIN_EMAILS_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_ADMIN_EMAILS_STATUS_VALUES!r}"
    )
