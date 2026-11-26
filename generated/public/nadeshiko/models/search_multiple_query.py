from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_multiple_query_match_mode import (
    SearchMultipleQueryMatchMode,
    check_search_multiple_query_match_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchMultipleQuery")


@_attrs_define
class SearchMultipleQuery:
    """What to search for (multiple words)

    Attributes:
        words (list[str]): List of words to search for Example: ['彼女', '私'].
        exact_match (bool | Unset): Require exact phrase matching (disables fuzzy and partial matches). Same as
            `matchMode` `EXACT`; ignored when `matchMode` is set. Default: False.
        match_mode (SearchMultipleQueryMatchMode | Unset): How each word is matched, as in the main search's
            `matchMode`. When omitted, `exactMatch` decides between `WORD` and `EXACT`.
            - `WORD` (default): whole words, in surface, dictionary and normalized form, plus EN/ES translations
            - `EXACT`: the exact phrase, surface form only
            - `CONTAINS`: Japanese words that contain the text anywhere, so `憬` counts sentences with `憧憬`. A word written
            with a leading `*` (`*憬*`) is counted this way in `WORD` mode too
             Example: CONTAINS.
    """

    words: list[str]
    exact_match: bool | Unset = False
    match_mode: SearchMultipleQueryMatchMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        words = self.words

        exact_match = self.exact_match

        match_mode: str | Unset = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "words": words,
            }
        )
        if exact_match is not UNSET:
            field_dict["exactMatch"] = exact_match
        if match_mode is not UNSET:
            field_dict["matchMode"] = match_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        words = cast(list[str], _src.pop("words"))

        exact_match = _src.pop("exactMatch", UNSET)

        _match_mode = _src.pop("matchMode", UNSET)
        match_mode: SearchMultipleQueryMatchMode | Unset
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_search_multiple_query_match_mode(_match_mode)

        search_multiple_query = cls(
            words=words,
            exact_match=exact_match,
            match_mode=match_mode,
        )

        search_multiple_query.additional_properties = _src
        return search_multiple_query

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
