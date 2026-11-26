from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.admin_overview_announcement import AdminOverviewAnnouncement
    from ..models.admin_overview_emails import AdminOverviewEmails
    from ..models.admin_overview_reports import AdminOverviewReports
    from ..models.admin_overview_requests import AdminOverviewRequests
    from ..models.admin_overview_users import AdminOverviewUsers


T = TypeVar("T", bound="AdminOverview")


@_attrs_define
class AdminOverview:
    """
    Attributes:
        reports (AdminOverviewReports):
        requests (AdminOverviewRequests):
        users (AdminOverviewUsers):
        announcement (AdminOverviewAnnouncement):
        emails (AdminOverviewEmails):
    """

    reports: AdminOverviewReports
    requests: AdminOverviewRequests
    users: AdminOverviewUsers
    announcement: AdminOverviewAnnouncement
    emails: AdminOverviewEmails
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reports = self.reports.to_dict()

        requests = self.requests.to_dict()

        users = self.users.to_dict()

        announcement = self.announcement.to_dict()

        emails = self.emails.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reports": reports,
                "requests": requests,
                "users": users,
                "announcement": announcement,
                "emails": emails,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.admin_overview_announcement import AdminOverviewAnnouncement  # noqa: PLC0415
        from ..models.admin_overview_emails import AdminOverviewEmails  # noqa: PLC0415
        from ..models.admin_overview_reports import AdminOverviewReports  # noqa: PLC0415
        from ..models.admin_overview_requests import AdminOverviewRequests  # noqa: PLC0415
        from ..models.admin_overview_users import AdminOverviewUsers  # noqa: PLC0415

        _src = dict(src_dict)
        reports = AdminOverviewReports.from_dict(_src.pop("reports"))

        requests = AdminOverviewRequests.from_dict(_src.pop("requests"))

        users = AdminOverviewUsers.from_dict(_src.pop("users"))

        announcement = AdminOverviewAnnouncement.from_dict(_src.pop("announcement"))

        emails = AdminOverviewEmails.from_dict(_src.pop("emails"))

        admin_overview = cls(
            reports=reports,
            requests=requests,
            users=users,
            announcement=announcement,
            emails=emails,
        )

        admin_overview.additional_properties = _src
        return admin_overview

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
