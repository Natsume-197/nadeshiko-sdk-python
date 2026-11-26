from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteUserDictionaryResponse200")


@_attrs_define
class DeleteUserDictionaryResponse200:
    """
    Attributes:
        stack_fingerprint (None | str):
    """

    stack_fingerprint: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_fingerprint: None | str
        stack_fingerprint = self.stack_fingerprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stackFingerprint": stack_fingerprint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)

        def _parse_stack_fingerprint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        stack_fingerprint = _parse_stack_fingerprint(_src.pop("stackFingerprint"))

        delete_user_dictionary_response_200 = cls(
            stack_fingerprint=stack_fingerprint,
        )

        delete_user_dictionary_response_200.additional_properties = _src
        return delete_user_dictionary_response_200

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
