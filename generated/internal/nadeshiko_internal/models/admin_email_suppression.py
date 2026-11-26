from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.admin_email_suppression_cause import (
    AdminEmailSuppressionCause,
    check_admin_email_suppression_cause,
)

T = TypeVar("T", bound="AdminEmailSuppression")


@_attrs_define
class AdminEmailSuppression:
    """
    Attributes:
        address (str):
        cause (AdminEmailSuppressionCause):
        reason (None | str):
        suppressed_at (datetime.datetime):
        permanent (bool): Complaints are never lifted from the dashboard.
    """

    address: str
    cause: AdminEmailSuppressionCause
    reason: None | str
    suppressed_at: datetime.datetime
    permanent: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address = self.address

        cause: str = self.cause

        reason: None | str
        reason = self.reason

        suppressed_at = self.suppressed_at.isoformat()

        permanent = self.permanent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "address": address,
                "cause": cause,
                "reason": reason,
                "suppressedAt": suppressed_at,
                "permanent": permanent,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        address = _src.pop("address")

        cause = check_admin_email_suppression_cause(_src.pop("cause"))

        def _parse_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        reason = _parse_reason(_src.pop("reason"))

        suppressed_at = datetime.datetime.fromisoformat(_src.pop("suppressedAt"))

        permanent = _src.pop("permanent")

        admin_email_suppression = cls(
            address=address,
            cause=cause,
            reason=reason,
            suppressed_at=suppressed_at,
            permanent=permanent,
        )

        admin_email_suppression.additional_properties = _src
        return admin_email_suppression

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
