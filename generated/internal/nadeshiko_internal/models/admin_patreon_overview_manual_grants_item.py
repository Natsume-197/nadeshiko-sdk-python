from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_patreon_overview_manual_grants_item_quota_source import (
    AdminPatreonOverviewManualGrantsItemQuotaSource,
    check_admin_patreon_overview_manual_grants_item_quota_source,
)

T = TypeVar("T", bound="AdminPatreonOverviewManualGrantsItem")


@_attrs_define
class AdminPatreonOverviewManualGrantsItem:
    """
    Attributes:
        user_id (int):
        username (str):
        email (str):
        tier_id (None | str):
        tier_name (None | str):
        quota_override (int | None):
        effective_quota_limit (int):
        quota_source (AdminPatreonOverviewManualGrantsItemQuotaSource):
    """

    user_id: int
    username: str
    email: str
    tier_id: None | str
    tier_name: None | str
    quota_override: int | None
    effective_quota_limit: int
    quota_source: AdminPatreonOverviewManualGrantsItemQuotaSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        username = self.username

        email = self.email

        tier_id: None | str
        tier_id = self.tier_id

        tier_name: None | str
        tier_name = self.tier_name

        quota_override: int | None
        quota_override = self.quota_override

        effective_quota_limit = self.effective_quota_limit

        quota_source: str = self.quota_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "username": username,
                "email": email,
                "tierId": tier_id,
                "tierName": tier_name,
                "quotaOverride": quota_override,
                "effectiveQuotaLimit": effective_quota_limit,
                "quotaSource": quota_source,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        user_id = _src.pop("userId")

        username = _src.pop("username")

        email = _src.pop("email")

        def _parse_tier_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tier_id = _parse_tier_id(_src.pop("tierId"))

        def _parse_tier_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tier_name = _parse_tier_name(_src.pop("tierName"))

        def _parse_quota_override(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        quota_override = _parse_quota_override(_src.pop("quotaOverride"))

        effective_quota_limit = _src.pop("effectiveQuotaLimit")

        quota_source = check_admin_patreon_overview_manual_grants_item_quota_source(
            _src.pop("quotaSource")
        )

        admin_patreon_overview_manual_grants_item = cls(
            user_id=user_id,
            username=username,
            email=email,
            tier_id=tier_id,
            tier_name=tier_name,
            quota_override=quota_override,
            effective_quota_limit=effective_quota_limit,
            quota_source=quota_source,
        )

        admin_patreon_overview_manual_grants_item.additional_properties = _src
        return admin_patreon_overview_manual_grants_item

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
