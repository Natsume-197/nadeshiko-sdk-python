from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_patreon_connection import AdminPatreonConnection
    from ..models.admin_patreon_overview_campaign import AdminPatreonOverviewCampaign
    from ..models.admin_patreon_overview_manual_grants_item import (
        AdminPatreonOverviewManualGrantsItem,
    )
    from ..models.admin_patreon_overview_summary import AdminPatreonOverviewSummary
    from ..models.admin_patreon_overview_tiers_item import AdminPatreonOverviewTiersItem


T = TypeVar("T", bound="AdminPatreonOverview")


@_attrs_define
class AdminPatreonOverview:
    """
    Attributes:
        configured (bool): Whether Patreon OAuth credentials and campaign ID are configured on this server.
        campaign_id (None | str): Configured Patreon campaign ID, if set.
        summary (AdminPatreonOverviewSummary):
        campaign (AdminPatreonOverviewCampaign):
        tiers (list[AdminPatreonOverviewTiersItem]):
        connections (list[AdminPatreonConnection]):
        manual_grants (list[AdminPatreonOverviewManualGrantsItem]):
    """

    configured: bool
    campaign_id: None | str
    summary: AdminPatreonOverviewSummary
    campaign: AdminPatreonOverviewCampaign
    tiers: list[AdminPatreonOverviewTiersItem]
    connections: list[AdminPatreonConnection]
    manual_grants: list[AdminPatreonOverviewManualGrantsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configured = self.configured

        campaign_id: None | str
        campaign_id = self.campaign_id

        summary = self.summary.to_dict()

        campaign = self.campaign.to_dict()

        tiers = []
        for tiers_item_data in self.tiers:
            tiers_item = tiers_item_data.to_dict()
            tiers.append(tiers_item)

        connections = []
        for connections_item_data in self.connections:
            connections_item = connections_item_data.to_dict()
            connections.append(connections_item)

        manual_grants = []
        for manual_grants_item_data in self.manual_grants:
            manual_grants_item = manual_grants_item_data.to_dict()
            manual_grants.append(manual_grants_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configured": configured,
                "campaignId": campaign_id,
                "summary": summary,
                "campaign": campaign,
                "tiers": tiers,
                "connections": connections,
                "manualGrants": manual_grants,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_patreon_connection import AdminPatreonConnection  # noqa: PLC0415
        from ..models.admin_patreon_overview_campaign import AdminPatreonOverviewCampaign  # noqa: PLC0415
        from ..models.admin_patreon_overview_manual_grants_item import (
            AdminPatreonOverviewManualGrantsItem,  # noqa: PLC0415
        )
        from ..models.admin_patreon_overview_summary import AdminPatreonOverviewSummary  # noqa: PLC0415
        from ..models.admin_patreon_overview_tiers_item import AdminPatreonOverviewTiersItem  # noqa: PLC0415

        _src = dict(src_dict)
        configured = _src.pop("configured")

        def _parse_campaign_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        campaign_id = _parse_campaign_id(_src.pop("campaignId"))

        summary = AdminPatreonOverviewSummary.from_dict(_src.pop("summary"))

        campaign = AdminPatreonOverviewCampaign.from_dict(_src.pop("campaign"))

        tiers = []
        _tiers = _src.pop("tiers")
        for tiers_item_data in _tiers:
            tiers_item = AdminPatreonOverviewTiersItem.from_dict(tiers_item_data)

            tiers.append(tiers_item)

        connections = []
        _connections = _src.pop("connections")
        for connections_item_data in _connections:
            connections_item = AdminPatreonConnection.from_dict(connections_item_data)

            connections.append(connections_item)

        manual_grants = []
        _manual_grants = _src.pop("manualGrants")
        for manual_grants_item_data in _manual_grants:
            manual_grants_item = AdminPatreonOverviewManualGrantsItem.from_dict(
                manual_grants_item_data
            )

            manual_grants.append(manual_grants_item)

        admin_patreon_overview = cls(
            configured=configured,
            campaign_id=campaign_id,
            summary=summary,
            campaign=campaign,
            tiers=tiers,
            connections=connections,
            manual_grants=manual_grants,
        )

        admin_patreon_overview.additional_properties = _src
        return admin_patreon_overview

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
