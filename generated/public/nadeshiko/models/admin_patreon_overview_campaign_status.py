from typing import Literal

AdminPatreonOverviewCampaignStatus = Literal["error", "ok", "unauthorized", "unconfigured"]

ADMIN_PATREON_OVERVIEW_CAMPAIGN_STATUS_VALUES: set[AdminPatreonOverviewCampaignStatus] = {
    "error",
    "ok",
    "unauthorized",
    "unconfigured",
}


def check_admin_patreon_overview_campaign_status(value: str) -> AdminPatreonOverviewCampaignStatus:
    if value in ADMIN_PATREON_OVERVIEW_CAMPAIGN_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADMIN_PATREON_OVERVIEW_CAMPAIGN_STATUS_VALUES!r}"
    )
