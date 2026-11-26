from typing import Literal

AdminPatreonOverviewManualGrantsItemQuotaSource = Literal[
    "default", "legacy_column", "override", "patreon", "tier"
]

ADMIN_PATREON_OVERVIEW_MANUAL_GRANTS_ITEM_QUOTA_SOURCE_VALUES: set[
    AdminPatreonOverviewManualGrantsItemQuotaSource
] = {
    "default",
    "legacy_column",
    "override",
    "patreon",
    "tier",
}


def check_admin_patreon_overview_manual_grants_item_quota_source(
    value: str,
) -> AdminPatreonOverviewManualGrantsItemQuotaSource:
    if value in ADMIN_PATREON_OVERVIEW_MANUAL_GRANTS_ITEM_QUOTA_SOURCE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_PATREON_OVERVIEW_MANUAL_GRANTS_ITEM_QUOTA_SOURCE_VALUES!r}"
    )
