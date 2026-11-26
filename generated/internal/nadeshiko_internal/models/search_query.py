from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.search_query_match_mode import SearchQueryMatchMode, check_search_query_match_mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchQuery")


@_attrs_define
class SearchQuery:
    """What to search for (omit for queryless browse/stats)

    Attributes:
        search (str | Unset): Search expression (supports boolean operators, wildcards, phrase matching) Example: (猫 OR
            犬) AND 好き.
        exact_match (bool | Unset): Require exact phrase matching (disables fuzzy and partial matches). Same as
            `matchMode` `EXACT`; ignored when `matchMode` is set. Default: False.
        match_mode (SearchQueryMatchMode | Unset): How the Japanese text is matched. When omitted, `exactMatch` decides
            between `WORD` and `EXACT`.
            - `WORD` (default): whole words, in surface, dictionary and normalized form, plus EN/ES translations
            - `EXACT`: the exact phrase, surface form only
            - `CONTAINS`: Japanese words that contain the text anywhere, so `糊` finds `血糊` and `糊付け`. It matches inside one
            word only (`糊が` matches nothing, since `糊` and `が` are separate words), and space-separated terms must all
            match. A `*` at either end of a term is ignored; other wildcards and boolean operators are taken literally, and
            leading-`-` exclusions still work. In `WORD` mode, a query made only of Japanese terms with a leading `*`
            (`*憬*`, `*憬`) is searched this way. Translations are not searched, and results are not ranked by relevance
            within the mode
             Example: CONTAINS.
    """

    search: str | Unset = UNSET
    exact_match: bool | Unset = False
    match_mode: SearchQueryMatchMode | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search = self.search

        exact_match = self.exact_match

        match_mode: str | Unset = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search is not UNSET:
            field_dict["search"] = search
        if exact_match is not UNSET:
            field_dict["exactMatch"] = exact_match
        if match_mode is not UNSET:
            field_dict["matchMode"] = match_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        search = _src.pop("search", UNSET)

        exact_match = _src.pop("exactMatch", UNSET)

        _match_mode = _src.pop("matchMode", UNSET)
        match_mode: SearchQueryMatchMode | Unset
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_search_query_match_mode(_match_mode)

        search_query = cls(
            search=search,
            exact_match=exact_match,
            match_mode=match_mode,
        )

        search_query.additional_properties = _src
        return search_query

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
