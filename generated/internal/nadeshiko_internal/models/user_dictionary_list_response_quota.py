from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="UserDictionaryListResponseQuota")


@_attrs_define
class UserDictionaryListResponseQuota:
    """
    Attributes:
        used (int):
        max_ (int):
        max_zip_bytes (int):
        is_patron (bool):
        indexed_bytes_used (int): Disk the account's dictionaries take once indexed, in bytes.
        max_indexed_bytes (int): Indexed space the account may use, in bytes; new uploads are refused once it is used
            up.
    """

    used: int
    max_: int
    max_zip_bytes: int
    is_patron: bool
    indexed_bytes_used: int
    max_indexed_bytes: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        used = self.used

        max_ = self.max_

        max_zip_bytes = self.max_zip_bytes

        is_patron = self.is_patron

        indexed_bytes_used = self.indexed_bytes_used

        max_indexed_bytes = self.max_indexed_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "used": used,
                "max": max_,
                "maxZipBytes": max_zip_bytes,
                "isPatron": is_patron,
                "indexedBytesUsed": indexed_bytes_used,
                "maxIndexedBytes": max_indexed_bytes,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        used = _src.pop("used")

        max_ = _src.pop("max")

        max_zip_bytes = _src.pop("maxZipBytes")

        is_patron = _src.pop("isPatron")

        indexed_bytes_used = _src.pop("indexedBytesUsed")

        max_indexed_bytes = _src.pop("maxIndexedBytes")

        user_dictionary_list_response_quota = cls(
            used=used,
            max_=max_,
            max_zip_bytes=max_zip_bytes,
            is_patron=is_patron,
            indexed_bytes_used=indexed_bytes_used,
            max_indexed_bytes=max_indexed_bytes,
        )

        user_dictionary_list_response_quota.additional_properties = _src
        return user_dictionary_list_response_quota

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
