from typing import Literal

AdminEmailSuppressionCause = Literal["complaint", "hard_bounce", "manual", "repeated_soft_bounce"]

ADMIN_EMAIL_SUPPRESSION_CAUSE_VALUES: set[AdminEmailSuppressionCause] = {
    "complaint",
    "hard_bounce",
    "manual",
    "repeated_soft_bounce",
}


def check_admin_email_suppression_cause(value: str) -> AdminEmailSuppressionCause:
    if value in ADMIN_EMAIL_SUPPRESSION_CAUSE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_EMAIL_SUPPRESSION_CAUSE_VALUES!r}"
    )
