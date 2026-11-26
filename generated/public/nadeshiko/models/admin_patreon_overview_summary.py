from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminPatreonOverviewSummary")


@_attrs_define
class AdminPatreonOverviewSummary:
    """
    Attributes:
        total_linked (int):
        active (int):
        issues (int):
        campaign_active (int):
        campaign_unlinked_active (int):
        campaign_monthly_cents (int): Gross monthly pledge total in campaign currency cents across active Patreon
            campaign members.
        campaign_lifetime_cents (int): Gross all-time support total in campaign currency cents across all Patreon
            campaign members.
        campaign_paying_ever (int): Count of campaign members with non-zero historical or active support.
    """

    total_linked: int
    active: int
    issues: int
    campaign_active: int
    campaign_unlinked_active: int
    campaign_monthly_cents: int
    campaign_lifetime_cents: int
    campaign_paying_ever: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_linked = self.total_linked

        active = self.active

        issues = self.issues

        campaign_active = self.campaign_active

        campaign_unlinked_active = self.campaign_unlinked_active

        campaign_monthly_cents = self.campaign_monthly_cents

        campaign_lifetime_cents = self.campaign_lifetime_cents

        campaign_paying_ever = self.campaign_paying_ever

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "totalLinked": total_linked,
                "active": active,
                "issues": issues,
                "campaignActive": campaign_active,
                "campaignUnlinkedActive": campaign_unlinked_active,
                "campaignMonthlyCents": campaign_monthly_cents,
                "campaignLifetimeCents": campaign_lifetime_cents,
                "campaignPayingEver": campaign_paying_ever,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        total_linked = _src.pop("totalLinked")

        active = _src.pop("active")

        issues = _src.pop("issues")

        campaign_active = _src.pop("campaignActive")

        campaign_unlinked_active = _src.pop("campaignUnlinkedActive")

        campaign_monthly_cents = _src.pop("campaignMonthlyCents")

        campaign_lifetime_cents = _src.pop("campaignLifetimeCents")

        campaign_paying_ever = _src.pop("campaignPayingEver")

        admin_patreon_overview_summary = cls(
            total_linked=total_linked,
            active=active,
            issues=issues,
            campaign_active=campaign_active,
            campaign_unlinked_active=campaign_unlinked_active,
            campaign_monthly_cents=campaign_monthly_cents,
            campaign_lifetime_cents=campaign_lifetime_cents,
            campaign_paying_ever=campaign_paying_ever,
        )

        admin_patreon_overview_summary.additional_properties = _src
        return admin_patreon_overview_summary

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
