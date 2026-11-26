from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_patreon_overview_campaign_status import (
    AdminPatreonOverviewCampaignStatus,
    check_admin_patreon_overview_campaign_status,
)

if TYPE_CHECKING:
    from ..models.admin_patreon_campaign_member import AdminPatreonCampaignMember


T = TypeVar("T", bound="AdminPatreonOverviewCampaign")


@_attrs_define
class AdminPatreonOverviewCampaign:
    """
    Attributes:
        status (AdminPatreonOverviewCampaignStatus):
        error_message (None | str):
        fetched_at (datetime.datetime | None):
        members (list[AdminPatreonCampaignMember]):
    """

    status: AdminPatreonOverviewCampaignStatus
    error_message: None | str
    fetched_at: datetime.datetime | None
    members: list[AdminPatreonCampaignMember]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str = self.status

        error_message: None | str
        error_message = self.error_message

        fetched_at: None | str
        if isinstance(self.fetched_at, datetime.datetime):
            fetched_at = self.fetched_at.isoformat()
        else:
            fetched_at = self.fetched_at

        members = []
        for members_item_data in self.members:
            members_item = members_item_data.to_dict()
            members.append(members_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "errorMessage": error_message,
                "fetchedAt": fetched_at,
                "members": members,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_patreon_campaign_member import AdminPatreonCampaignMember  # noqa: PLC0415

        _src = dict(src_dict)
        status = check_admin_patreon_overview_campaign_status(_src.pop("status"))

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(_src.pop("errorMessage"))

        def _parse_fetched_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                fetched_at_type_0 = datetime.datetime.fromisoformat(data)

                return fetched_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        fetched_at = _parse_fetched_at(_src.pop("fetchedAt"))

        members = []
        _members = _src.pop("members")
        for members_item_data in _members:
            members_item = AdminPatreonCampaignMember.from_dict(members_item_data)

            members.append(members_item)

        admin_patreon_overview_campaign = cls(
            status=status,
            error_message=error_message,
            fetched_at=fetched_at,
            members=members,
        )

        admin_patreon_overview_campaign.additional_properties = _src
        return admin_patreon_overview_campaign

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
