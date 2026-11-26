from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dictionary_candidate import DictionaryCandidate


T = TypeVar("T", bound="IdentifyDictionaryWordResponse200")


@_attrs_define
class IdentifyDictionaryWordResponse200:
    """
    Attributes:
        candidates (list[DictionaryCandidate]): Best first; empty when no entry matches.
        stack_fingerprint (None | str | Unset): Fingerprint of the reader's custom dictionary stack when custom
            dictionaries were applied.
        custom_dictionaries_pending (bool | Unset): True when the answer lacks one of the reader's enabled custom
            dictionaries, because it is still indexing or this server is still fetching it. Such an answer must not be
            cached.
    """

    candidates: list[DictionaryCandidate]
    stack_fingerprint: None | str | Unset = UNSET
    custom_dictionaries_pending: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        candidates = []
        for candidates_item_data in self.candidates:
            candidates_item = candidates_item_data.to_dict()
            candidates.append(candidates_item)

        stack_fingerprint: None | str | Unset
        if isinstance(self.stack_fingerprint, Unset):
            stack_fingerprint = UNSET
        else:
            stack_fingerprint = self.stack_fingerprint

        custom_dictionaries_pending = self.custom_dictionaries_pending

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "candidates": candidates,
            }
        )
        if stack_fingerprint is not UNSET:
            field_dict["stackFingerprint"] = stack_fingerprint
        if custom_dictionaries_pending is not UNSET:
            field_dict["customDictionariesPending"] = custom_dictionaries_pending

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictionary_candidate import DictionaryCandidate  # noqa: PLC0415

        _src = dict(src_dict)
        candidates = []
        _candidates = _src.pop("candidates")
        for candidates_item_data in _candidates:
            candidates_item = DictionaryCandidate.from_dict(candidates_item_data)

            candidates.append(candidates_item)

        def _parse_stack_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        stack_fingerprint = _parse_stack_fingerprint(_src.pop("stackFingerprint", UNSET))

        custom_dictionaries_pending = _src.pop("customDictionariesPending", UNSET)

        identify_dictionary_word_response_200 = cls(
            candidates=candidates,
            stack_fingerprint=stack_fingerprint,
            custom_dictionaries_pending=custom_dictionaries_pending,
        )

        identify_dictionary_word_response_200.additional_properties = _src
        return identify_dictionary_word_response_200

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
