from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AdminPatreonCampaignMember")


@_attrs_define
class AdminPatreonCampaignMember:
    """
    Attributes:
        member_id (str):
        patreon_user_id (None | str):
        full_name (str):
        email (None | str):
        patron_status (None | str):
        entitled_amount_cents (int):
        monthly_amount_cents (int): Normalized monthly USD cents using the Patreon tier list price when assigned
            (excludes Apple iOS IAP markup).
        lifetime_support_cents (int):
        pledge_start (datetime.datetime | None):
        last_charge_status (None | str):
        last_charge_date (datetime.datetime | None):
        entitled_tier_ids (list[str]):
        patreon_tier_titles (list[str]):
        resolved_tier_name (None | str):
        unmatched_tier_ids (list[str]):
        linked_user_id (int | None):
        linked_username (None | str):
        matched_user_id (int | None): Existing Nadeshiko user matched by lowercase email when the patron has not linked
            Patreon OAuth yet.
        matched_username (None | str):
    """

    member_id: str
    patreon_user_id: None | str
    full_name: str
    email: None | str
    patron_status: None | str
    entitled_amount_cents: int
    monthly_amount_cents: int
    lifetime_support_cents: int
    pledge_start: datetime.datetime | None
    last_charge_status: None | str
    last_charge_date: datetime.datetime | None
    entitled_tier_ids: list[str]
    patreon_tier_titles: list[str]
    resolved_tier_name: None | str
    unmatched_tier_ids: list[str]
    linked_user_id: int | None
    linked_username: None | str
    matched_user_id: int | None
    matched_username: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        member_id = self.member_id

        patreon_user_id: None | str
        patreon_user_id = self.patreon_user_id

        full_name = self.full_name

        email: None | str
        email = self.email

        patron_status: None | str
        patron_status = self.patron_status

        entitled_amount_cents = self.entitled_amount_cents

        monthly_amount_cents = self.monthly_amount_cents

        lifetime_support_cents = self.lifetime_support_cents

        pledge_start: None | str
        if isinstance(self.pledge_start, datetime.datetime):
            pledge_start = self.pledge_start.isoformat()
        else:
            pledge_start = self.pledge_start

        last_charge_status: None | str
        last_charge_status = self.last_charge_status

        last_charge_date: None | str
        if isinstance(self.last_charge_date, datetime.datetime):
            last_charge_date = self.last_charge_date.isoformat()
        else:
            last_charge_date = self.last_charge_date

        entitled_tier_ids = self.entitled_tier_ids

        patreon_tier_titles = self.patreon_tier_titles

        resolved_tier_name: None | str
        resolved_tier_name = self.resolved_tier_name

        unmatched_tier_ids = self.unmatched_tier_ids

        linked_user_id: int | None
        linked_user_id = self.linked_user_id

        linked_username: None | str
        linked_username = self.linked_username

        matched_user_id: int | None
        matched_user_id = self.matched_user_id

        matched_username: None | str
        matched_username = self.matched_username

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "memberId": member_id,
                "patreonUserId": patreon_user_id,
                "fullName": full_name,
                "email": email,
                "patronStatus": patron_status,
                "entitledAmountCents": entitled_amount_cents,
                "monthlyAmountCents": monthly_amount_cents,
                "lifetimeSupportCents": lifetime_support_cents,
                "pledgeStart": pledge_start,
                "lastChargeStatus": last_charge_status,
                "lastChargeDate": last_charge_date,
                "entitledTierIds": entitled_tier_ids,
                "patreonTierTitles": patreon_tier_titles,
                "resolvedTierName": resolved_tier_name,
                "unmatchedTierIds": unmatched_tier_ids,
                "linkedUserId": linked_user_id,
                "linkedUsername": linked_username,
                "matchedUserId": matched_user_id,
                "matchedUsername": matched_username,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        member_id = _src.pop("memberId")

        def _parse_patreon_user_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        patreon_user_id = _parse_patreon_user_id(_src.pop("patreonUserId"))

        full_name = _src.pop("fullName")

        def _parse_email(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        email = _parse_email(_src.pop("email"))

        def _parse_patron_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        patron_status = _parse_patron_status(_src.pop("patronStatus"))

        entitled_amount_cents = _src.pop("entitledAmountCents")

        monthly_amount_cents = _src.pop("monthlyAmountCents")

        lifetime_support_cents = _src.pop("lifetimeSupportCents")

        def _parse_pledge_start(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pledge_start_type_0 = datetime.datetime.fromisoformat(data)

                return pledge_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        pledge_start = _parse_pledge_start(_src.pop("pledgeStart"))

        def _parse_last_charge_status(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_charge_status = _parse_last_charge_status(_src.pop("lastChargeStatus"))

        def _parse_last_charge_date(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_charge_date_type_0 = datetime.datetime.fromisoformat(data)

                return last_charge_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_charge_date = _parse_last_charge_date(_src.pop("lastChargeDate"))

        entitled_tier_ids = cast(list[str], _src.pop("entitledTierIds"))

        patreon_tier_titles = cast(list[str], _src.pop("patreonTierTitles"))

        def _parse_resolved_tier_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        resolved_tier_name = _parse_resolved_tier_name(_src.pop("resolvedTierName"))

        unmatched_tier_ids = cast(list[str], _src.pop("unmatchedTierIds"))

        def _parse_linked_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        linked_user_id = _parse_linked_user_id(_src.pop("linkedUserId"))

        def _parse_linked_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        linked_username = _parse_linked_username(_src.pop("linkedUsername"))

        def _parse_matched_user_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        matched_user_id = _parse_matched_user_id(_src.pop("matchedUserId"))

        def _parse_matched_username(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        matched_username = _parse_matched_username(_src.pop("matchedUsername"))

        admin_patreon_campaign_member = cls(
            member_id=member_id,
            patreon_user_id=patreon_user_id,
            full_name=full_name,
            email=email,
            patron_status=patron_status,
            entitled_amount_cents=entitled_amount_cents,
            monthly_amount_cents=monthly_amount_cents,
            lifetime_support_cents=lifetime_support_cents,
            pledge_start=pledge_start,
            last_charge_status=last_charge_status,
            last_charge_date=last_charge_date,
            entitled_tier_ids=entitled_tier_ids,
            patreon_tier_titles=patreon_tier_titles,
            resolved_tier_name=resolved_tier_name,
            unmatched_tier_ids=unmatched_tier_ids,
            linked_user_id=linked_user_id,
            linked_username=linked_username,
            matched_user_id=matched_user_id,
            matched_username=matched_username,
        )

        admin_patreon_campaign_member.additional_properties = _src
        return admin_patreon_campaign_member

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
