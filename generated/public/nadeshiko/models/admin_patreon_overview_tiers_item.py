from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminPatreonOverviewTiersItem")


@_attrs_define
class AdminPatreonOverviewTiersItem:
    """
    Attributes:
        id (str):
        display_name (str):
        patreon_tier_id (None | str):
        monthly_quota_limit (int):
        monthly_request_boosts (int):
        active_patron_count (int): Count of active linked Nadeshiko OAuth connections resolved to this tier.
        campaign_patron_count (int): Count of active Patreon.com campaign members resolved to this tier.
        campaign_monthly_cents (int): Normalized monthly USD cents from active Patreon.com campaign members in this
            tier.
    """

    id: str
    display_name: str
    patreon_tier_id: None | str
    monthly_quota_limit: int
    monthly_request_boosts: int
    active_patron_count: int
    campaign_patron_count: int
    campaign_monthly_cents: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        display_name = self.display_name

        patreon_tier_id: None | str
        patreon_tier_id = self.patreon_tier_id

        monthly_quota_limit = self.monthly_quota_limit

        monthly_request_boosts = self.monthly_request_boosts

        active_patron_count = self.active_patron_count

        campaign_patron_count = self.campaign_patron_count

        campaign_monthly_cents = self.campaign_monthly_cents

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "displayName": display_name,
                "patreonTierId": patreon_tier_id,
                "monthlyQuotaLimit": monthly_quota_limit,
                "monthlyRequestBoosts": monthly_request_boosts,
                "activePatronCount": active_patron_count,
                "campaignPatronCount": campaign_patron_count,
                "campaignMonthlyCents": campaign_monthly_cents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        display_name = _src.pop("displayName")

        def _parse_patreon_tier_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        patreon_tier_id = _parse_patreon_tier_id(_src.pop("patreonTierId"))

        monthly_quota_limit = _src.pop("monthlyQuotaLimit")

        monthly_request_boosts = _src.pop("monthlyRequestBoosts")

        active_patron_count = _src.pop("activePatronCount")

        campaign_patron_count = _src.pop("campaignPatronCount")

        campaign_monthly_cents = _src.pop("campaignMonthlyCents")

        admin_patreon_overview_tiers_item = cls(
            id=id,
            display_name=display_name,
            patreon_tier_id=patreon_tier_id,
            monthly_quota_limit=monthly_quota_limit,
            monthly_request_boosts=monthly_request_boosts,
            active_patron_count=active_patron_count,
            campaign_patron_count=campaign_patron_count,
            campaign_monthly_cents=campaign_monthly_cents,
        )

        admin_patreon_overview_tiers_item.additional_properties = _src
        return admin_patreon_overview_tiers_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
