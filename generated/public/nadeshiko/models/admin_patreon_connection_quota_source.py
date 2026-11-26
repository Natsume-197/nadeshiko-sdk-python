from typing import Literal

AdminPatreonConnectionQuotaSource = Literal[
    "default", "legacy_column", "override", "patreon", "tier"
]

ADMIN_PATREON_CONNECTION_QUOTA_SOURCE_VALUES: set[AdminPatreonConnectionQuotaSource] = {
    "default",
    "legacy_column",
    "override",
    "patreon",
    "tier",
}


def check_admin_patreon_connection_quota_source(value: str) -> AdminPatreonConnectionQuotaSource:
    if value in ADMIN_PATREON_CONNECTION_QUOTA_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_PATREON_CONNECTION_QUOTA_SOURCE_VALUES!r}"
    )
