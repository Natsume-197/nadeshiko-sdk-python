from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.set_word_watch_body_match_mode import (
    SetWordWatchBodyMatchMode,
    check_set_word_watch_body_match_mode,
)
from ..models.set_word_watch_body_mode import SetWordWatchBodyMode, check_set_word_watch_body_mode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SetWordWatchBody")


@_attrs_define
class SetWordWatchBody:
    """
    Attributes:
        query (str):
        mode (SetWordWatchBodyMode):
        match_mode (SetWordWatchBodyMatchMode | Unset):  Default: 'WORD'.
    """

    query: str
    mode: SetWordWatchBodyMode
    match_mode: SetWordWatchBodyMatchMode | Unset = "WORD"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        mode: str = self.mode

        match_mode: str | Unset = UNSET
        if not isinstance(self.match_mode, Unset):
            match_mode = self.match_mode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "mode": mode,
            }
        )
        if match_mode is not UNSET:
            field_dict["matchMode"] = match_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        query = _src.pop("query")

        mode = check_set_word_watch_body_mode(_src.pop("mode"))

        _match_mode = _src.pop("matchMode", UNSET)
        match_mode: SetWordWatchBodyMatchMode | Unset
        if isinstance(_match_mode, Unset):
            match_mode = UNSET
        else:
            match_mode = check_set_word_watch_body_match_mode(_match_mode)

        set_word_watch_body = cls(
            query=query,
            mode=mode,
            match_mode=match_mode,
        )

        set_word_watch_body.additional_properties = _src
        return set_word_watch_body

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
