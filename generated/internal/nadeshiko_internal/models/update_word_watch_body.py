from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.update_word_watch_body_mode import (
    UpdateWordWatchBodyMode,
    check_update_word_watch_body_mode,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWordWatchBody")


@_attrs_define
class UpdateWordWatchBody:
    """
    Attributes:
        mode (UpdateWordWatchBodyMode | Unset):
        paused (bool | Unset):
    """

    mode: UpdateWordWatchBodyMode | Unset = UNSET
    paused: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode

        paused = self.paused

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if paused is not UNSET:
            field_dict["paused"] = paused

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        _mode = _src.pop("mode", UNSET)
        mode: UpdateWordWatchBodyMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = check_update_word_watch_body_mode(_mode)

        paused = _src.pop("paused", UNSET)

        update_word_watch_body = cls(
            mode=mode,
            paused=paused,
        )

        update_word_watch_body.additional_properties = _src
        return update_word_watch_body

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
