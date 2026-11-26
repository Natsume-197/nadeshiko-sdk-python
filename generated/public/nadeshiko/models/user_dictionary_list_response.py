from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.user_dictionary import UserDictionary
    from ..models.user_dictionary_list_response_builtin import UserDictionaryListResponseBuiltin
    from ..models.user_dictionary_list_response_quota import UserDictionaryListResponseQuota


T = TypeVar("T", bound="UserDictionaryListResponse")


@_attrs_define
class UserDictionaryListResponse:
    """The signed-in user's custom Yomitan dictionary stack, built-in JMdict placement, and account quota.

    Attributes:
        dictionaries (list[UserDictionary]):
        builtin (UserDictionaryListResponseBuiltin):
        quota (UserDictionaryListResponseQuota):
        stack_fingerprint (None | str):
        direct_upload (bool): Whether uploads go straight to storage (reserve, PUT, complete) rather than through the
            upload endpoint.
    """

    dictionaries: list[UserDictionary]
    builtin: UserDictionaryListResponseBuiltin
    quota: UserDictionaryListResponseQuota
    stack_fingerprint: None | str
    direct_upload: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dictionaries = []
        for dictionaries_item_data in self.dictionaries:
            dictionaries_item = dictionaries_item_data.to_dict()
            dictionaries.append(dictionaries_item)

        builtin = self.builtin.to_dict()

        quota = self.quota.to_dict()

        stack_fingerprint: None | str
        stack_fingerprint = self.stack_fingerprint

        direct_upload = self.direct_upload

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "dictionaries": dictionaries,
                "builtin": builtin,
                "quota": quota,
                "stackFingerprint": stack_fingerprint,
                "directUpload": direct_upload,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_dictionary import UserDictionary  # noqa: PLC0415
        from ..models.user_dictionary_list_response_builtin import UserDictionaryListResponseBuiltin  # noqa: PLC0415
        from ..models.user_dictionary_list_response_quota import UserDictionaryListResponseQuota  # noqa: PLC0415

        _src = dict(src_dict)
        dictionaries = []
        _dictionaries = _src.pop("dictionaries")
        for dictionaries_item_data in _dictionaries:
            dictionaries_item = UserDictionary.from_dict(dictionaries_item_data)

            dictionaries.append(dictionaries_item)

        builtin = UserDictionaryListResponseBuiltin.from_dict(_src.pop("builtin"))

        quota = UserDictionaryListResponseQuota.from_dict(_src.pop("quota"))

        def _parse_stack_fingerprint(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        stack_fingerprint = _parse_stack_fingerprint(_src.pop("stackFingerprint"))

        direct_upload = _src.pop("directUpload")

        user_dictionary_list_response = cls(
            dictionaries=dictionaries,
            builtin=builtin,
            quota=quota,
            stack_fingerprint=stack_fingerprint,
            direct_upload=direct_upload,
        )

        user_dictionary_list_response.additional_properties = _src
        return user_dictionary_list_response

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
