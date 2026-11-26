from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_dictionary import UserDictionary


T = TypeVar("T", bound="UserDictionaryUploadResult")


@_attrs_define
class UserDictionaryUploadResult:
    """The dictionary an upload created or attached, and the account's new stack fingerprint.

    Attributes:
        dictionary (UserDictionary): One custom Yomitan dictionary attached to the user's account.
        stack_fingerprint (None | str):
    """

    dictionary: UserDictionary
    stack_fingerprint: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dictionary = self.dictionary.to_dict()

        stack_fingerprint: None | str
        stack_fingerprint = self.stack_fingerprint

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dictionary": dictionary,
                "stackFingerprint": stack_fingerprint,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_dictionary import UserDictionary  # noqa: PLC0415

        _src = dict(src_dict)
        dictionary = UserDictionary.from_dict(_src.pop("dictionary"))

        def _parse_stack_fingerprint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        stack_fingerprint = _parse_stack_fingerprint(_src.pop("stackFingerprint"))

        user_dictionary_upload_result = cls(
            dictionary=dictionary,
            stack_fingerprint=stack_fingerprint,
        )

        user_dictionary_upload_result.additional_properties = _src
        return user_dictionary_upload_result

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
