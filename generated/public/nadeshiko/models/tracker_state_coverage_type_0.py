from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tracker_state_coverage_type_0_by_status import TrackerStateCoverageType0ByStatus


T = TypeVar("T", bound="TrackerStateCoverageType0")


@_attrs_define
class TrackerStateCoverageType0:
    """
    Attributes:
        total (int):
        in_catalog (int):
        missing (int):
        by_status (TrackerStateCoverageType0ByStatus):
    """

    total: int
    in_catalog: int
    missing: int
    by_status: TrackerStateCoverageType0ByStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        in_catalog = self.in_catalog

        missing = self.missing

        by_status = self.by_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "inCatalog": in_catalog,
                "missing": missing,
                "byStatus": by_status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tracker_state_coverage_type_0_by_status import (
            TrackerStateCoverageType0ByStatus,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        total = _src.pop("total")

        in_catalog = _src.pop("inCatalog")

        missing = _src.pop("missing")

        by_status = TrackerStateCoverageType0ByStatus.from_dict(_src.pop("byStatus"))

        tracker_state_coverage_type_0 = cls(
            total=total,
            in_catalog=in_catalog,
            missing=missing,
            by_status=by_status,
        )

        tracker_state_coverage_type_0.additional_properties = _src
        return tracker_state_coverage_type_0

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
