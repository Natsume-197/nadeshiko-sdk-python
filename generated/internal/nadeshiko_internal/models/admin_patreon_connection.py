from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_patreon_connection_quota_source import (
    AdminPatreonConnectionQuotaSource,
    check_admin_patreon_connection_quota_source,
)

T = TypeVar("T", bound="AdminPatreonConnection")


@_attrs_define
class AdminPatreonConnection:
    """
    Attributes:
        user_id (int):  Example: 42.
        username (str):  Example: tanaka_san.
        email (str):  Example: tanaka@example.com.
        patreon_user_id (str):  Example: 12345678.
        full_name (None | str):  Example: Tanaka Taro.
        patron_status (None | str):  Example: active_patron.
        monthly_amount_cents (int): Monthly USD cents, normalized to the Patreon tier list price when the member appears
            in the live campaign list (excludes Apple iOS IAP markup); otherwise Patreon's raw entitled amount. Example:
            1000.
        resolved_tier_id (None | str):  Example: pro.
        resolved_tier_name (None | str):  Example: Flower.
        effective_quota_limit (int):  Example: 30000.
        quota_source (AdminPatreonConnectionQuotaSource):  Example: patreon.
        unmatched_tier_ids (list[str]): Entitled Patreon tier IDs that match no configured Tier row.
        is_active (bool): True when active_patron with positive pledge and checked within the staleness bound.
        is_stale (bool): True when membershipCheckedAt is older than the 7-day staleness bound.
        has_issue (bool): True when stale, declined, or carrying unmatched Patreon tier IDs.
        membership_checked_at (datetime.datetime):
        linked_at (datetime.datetime):
    """

    user_id: int
    username: str
    email: str
    patreon_user_id: str
    full_name: None | str
    patron_status: None | str
    monthly_amount_cents: int
    resolved_tier_id: None | str
    resolved_tier_name: None | str
    effective_quota_limit: int
    quota_source: AdminPatreonConnectionQuotaSource
    unmatched_tier_ids: list[str]
    is_active: bool
    is_stale: bool
    has_issue: bool
    membership_checked_at: datetime.datetime
    linked_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user_id = self.user_id

        username = self.username

        email = self.email

        patreon_user_id = self.patreon_user_id

        full_name: None | str
        full_name = self.full_name

        patron_status: None | str
        patron_status = self.patron_status

        monthly_amount_cents = self.monthly_amount_cents

        resolved_tier_id: None | str
        resolved_tier_id = self.resolved_tier_id

        resolved_tier_name: None | str
        resolved_tier_name = self.resolved_tier_name

        effective_quota_limit = self.effective_quota_limit

        quota_source: str = self.quota_source

        unmatched_tier_ids = self.unmatched_tier_ids

        is_active = self.is_active

        is_stale = self.is_stale

        has_issue = self.has_issue

        membership_checked_at = self.membership_checked_at.isoformat()

        linked_at = self.linked_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "userId": user_id,
                "username": username,
                "email": email,
                "patreonUserId": patreon_user_id,
                "fullName": full_name,
                "patronStatus": patron_status,
                "monthlyAmountCents": monthly_amount_cents,
                "resolvedTierId": resolved_tier_id,
                "resolvedTierName": resolved_tier_name,
                "effectiveQuotaLimit": effective_quota_limit,
                "quotaSource": quota_source,
                "unmatchedTierIds": unmatched_tier_ids,
                "isActive": is_active,
                "isStale": is_stale,
                "hasIssue": has_issue,
                "membershipCheckedAt": membership_checked_at,
                "linkedAt": linked_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        user_id = _src.pop("userId")

        username = _src.pop("username")

        email = _src.pop("email")

        patreon_user_id = _src.pop("patreonUserId")

        def _parse_full_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        full_name = _parse_full_name(_src.pop("fullName"))

        def _parse_patron_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        patron_status = _parse_patron_status(_src.pop("patronStatus"))

        monthly_amount_cents = _src.pop("monthlyAmountCents")

        def _parse_resolved_tier_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_tier_id = _parse_resolved_tier_id(_src.pop("resolvedTierId"))

        def _parse_resolved_tier_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_tier_name = _parse_resolved_tier_name(_src.pop("resolvedTierName"))

        effective_quota_limit = _src.pop("effectiveQuotaLimit")

        quota_source = check_admin_patreon_connection_quota_source(_src.pop("quotaSource"))

        unmatched_tier_ids = cast(list[str], _src.pop("unmatchedTierIds"))

        is_active = _src.pop("isActive")

        is_stale = _src.pop("isStale")

        has_issue = _src.pop("hasIssue")

        membership_checked_at = datetime.datetime.fromisoformat(_src.pop("membershipCheckedAt"))

        linked_at = datetime.datetime.fromisoformat(_src.pop("linkedAt"))

        admin_patreon_connection = cls(
            user_id=user_id,
            username=username,
            email=email,
            patreon_user_id=patreon_user_id,
            full_name=full_name,
            patron_status=patron_status,
            monthly_amount_cents=monthly_amount_cents,
            resolved_tier_id=resolved_tier_id,
            resolved_tier_name=resolved_tier_name,
            effective_quota_limit=effective_quota_limit,
            quota_source=quota_source,
            unmatched_tier_ids=unmatched_tier_ids,
            is_active=is_active,
            is_stale=is_stale,
            has_issue=has_issue,
            membership_checked_at=membership_checked_at,
            linked_at=linked_at,
        )

        admin_patreon_connection.additional_properties = _src
        return admin_patreon_connection

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
