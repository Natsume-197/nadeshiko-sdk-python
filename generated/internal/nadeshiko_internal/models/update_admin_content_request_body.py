from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_admin_content_request_body_category import (
    UpdateAdminContentRequestBodyCategory,
    check_update_admin_content_request_body_category,
)
from ..models.update_admin_content_request_body_kind import (
    UpdateAdminContentRequestBodyKind,
    check_update_admin_content_request_body_kind,
)
from ..models.update_admin_content_request_body_status import (
    UpdateAdminContentRequestBodyStatus,
    check_update_admin_content_request_body_status,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAdminContentRequestBody")


@_attrs_define
class UpdateAdminContentRequestBody:
    """
    Attributes:
        status (UpdateAdminContentRequestBodyStatus | Unset):
        title (str | Unset):
        note (str | Unset):
        category (UpdateAdminContentRequestBodyCategory | Unset):
        kind (UpdateAdminContentRequestBodyKind | Unset):
        cover_url (None | str | Unset):
        decline_reason (None | str | Unset):
        media_id (None | str | Unset): Public id of the media the request is for or produced.
        dismiss_duplicate (bool | Unset): Clear the possible-duplicate flag.
        notify (bool | Unset): False moves the request without telling its voters (no bell entry, no email). Default:
            True.
    """

    status: UpdateAdminContentRequestBodyStatus | Unset = UNSET
    title: str | Unset = UNSET
    note: str | Unset = UNSET
    category: UpdateAdminContentRequestBodyCategory | Unset = UNSET
    kind: UpdateAdminContentRequestBodyKind | Unset = UNSET
    cover_url: None | str | Unset = UNSET
    decline_reason: None | str | Unset = UNSET
    media_id: None | str | Unset = UNSET
    dismiss_duplicate: bool | Unset = UNSET
    notify: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        title = self.title

        note = self.note

        category: str | Unset = UNSET
        if not isinstance(self.category, Unset):
            category = self.category

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind

        cover_url: None | str | Unset
        if isinstance(self.cover_url, Unset):
            cover_url = UNSET
        else:
            cover_url = self.cover_url

        decline_reason: None | str | Unset
        if isinstance(self.decline_reason, Unset):
            decline_reason = UNSET
        else:
            decline_reason = self.decline_reason

        media_id: None | str | Unset
        if isinstance(self.media_id, Unset):
            media_id = UNSET
        else:
            media_id = self.media_id

        dismiss_duplicate = self.dismiss_duplicate

        notify = self.notify

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if note is not UNSET:
            field_dict["note"] = note
        if category is not UNSET:
            field_dict["category"] = category
        if kind is not UNSET:
            field_dict["kind"] = kind
        if cover_url is not UNSET:
            field_dict["coverUrl"] = cover_url
        if decline_reason is not UNSET:
            field_dict["declineReason"] = decline_reason
        if media_id is not UNSET:
            field_dict["mediaId"] = media_id
        if dismiss_duplicate is not UNSET:
            field_dict["dismissDuplicate"] = dismiss_duplicate
        if notify is not UNSET:
            field_dict["notify"] = notify

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        _status = _src.pop("status", UNSET)
        status: UpdateAdminContentRequestBodyStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_update_admin_content_request_body_status(_status)

        title = _src.pop("title", UNSET)

        note = _src.pop("note", UNSET)

        _category = _src.pop("category", UNSET)
        category: UpdateAdminContentRequestBodyCategory | Unset
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = check_update_admin_content_request_body_category(_category)

        _kind = _src.pop("kind", UNSET)
        kind: UpdateAdminContentRequestBodyKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = check_update_admin_content_request_body_kind(_kind)

        def _parse_cover_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cover_url = _parse_cover_url(_src.pop("coverUrl", UNSET))

        def _parse_decline_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        decline_reason = _parse_decline_reason(_src.pop("declineReason", UNSET))

        def _parse_media_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        media_id = _parse_media_id(_src.pop("mediaId", UNSET))

        dismiss_duplicate = _src.pop("dismissDuplicate", UNSET)

        notify = _src.pop("notify", UNSET)

        update_admin_content_request_body = cls(
            status=status,
            title=title,
            note=note,
            category=category,
            kind=kind,
            cover_url=cover_url,
            decline_reason=decline_reason,
            media_id=media_id,
            dismiss_duplicate=dismiss_duplicate,
            notify=notify,
        )

        update_admin_content_request_body.additional_properties = _src
        return update_admin_content_request_body

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
