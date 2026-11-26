from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.reserve_user_dictionary_upload_response_201_method import (
    ReserveUserDictionaryUploadResponse201Method,
    check_reserve_user_dictionary_upload_response_201_method,
)

if TYPE_CHECKING:
    from ..models.reserve_user_dictionary_upload_response_201_headers import (
        ReserveUserDictionaryUploadResponse201Headers,
    )


T = TypeVar("T", bound="ReserveUserDictionaryUploadResponse201")


@_attrs_define
class ReserveUserDictionaryUploadResponse201:
    """
    Attributes:
        upload_id (UUID):
        url (str): Presigned URL to PUT the file to.
        method (ReserveUserDictionaryUploadResponse201Method):
        headers (ReserveUserDictionaryUploadResponse201Headers): Headers the PUT must send.
        expires_at (datetime.datetime):
    """

    upload_id: UUID
    url: str
    method: ReserveUserDictionaryUploadResponse201Method
    headers: ReserveUserDictionaryUploadResponse201Headers
    expires_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        upload_id = str(self.upload_id)

        url = self.url

        method: str = self.method

        headers = self.headers.to_dict()

        expires_at = self.expires_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uploadId": upload_id,
                "url": url,
                "method": method,
                "headers": headers,
                "expiresAt": expires_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.reserve_user_dictionary_upload_response_201_headers import (
            ReserveUserDictionaryUploadResponse201Headers,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        upload_id = UUID(_src.pop("uploadId"))

        url = _src.pop("url")

        method = check_reserve_user_dictionary_upload_response_201_method(_src.pop("method"))

        headers = ReserveUserDictionaryUploadResponse201Headers.from_dict(_src.pop("headers"))

        expires_at = datetime.datetime.fromisoformat(_src.pop("expiresAt"))

        reserve_user_dictionary_upload_response_201 = cls(
            upload_id=upload_id,
            url=url,
            method=method,
            headers=headers,
            expires_at=expires_at,
        )

        reserve_user_dictionary_upload_response_201.additional_properties = _src
        return reserve_user_dictionary_upload_response_201

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
