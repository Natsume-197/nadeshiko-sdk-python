from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_preferences_custom_theme_type_0_base import (
    UserPreferencesCustomThemeType0Base,
    check_user_preferences_custom_theme_type_0_base,
)
from ..models.user_preferences_custom_theme_type_0_preset import (
    UserPreferencesCustomThemeType0Preset,
    check_user_preferences_custom_theme_type_0_preset,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPreferencesCustomThemeType0")


@_attrs_define
class UserPreferencesCustomThemeType0:
    """A patron's custom theme: a light or dark base plus an accent and a page
    background. Writing a non-null value needs an active Patreon membership
    (any paid tier) or an admin account; `null` clears it. Kept when a
    membership lapses, but left out of the response until it is active again,
    so the site falls back to the dark theme.

        Attributes:
            base (UserPreferencesCustomThemeType0Base):
            accent (str):
            background (str):
            preset (UserPreferencesCustomThemeType0Preset | Unset): The ready-made theme it started from, or `custom`.
    """

    base: UserPreferencesCustomThemeType0Base
    accent: str
    background: str
    preset: UserPreferencesCustomThemeType0Preset | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        base: str = self.base

        accent = self.accent

        background = self.background

        preset: str | Unset = UNSET
        if not isinstance(self.preset, Unset):
            preset = self.preset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "base": base,
                "accent": accent,
                "background": background,
            }
        )
        if preset is not UNSET:
            field_dict["preset"] = preset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        base = check_user_preferences_custom_theme_type_0_base(_src.pop("base"))

        accent = _src.pop("accent")

        background = _src.pop("background")

        _preset = _src.pop("preset", UNSET)
        preset: UserPreferencesCustomThemeType0Preset | Unset
        if isinstance(_preset, Unset):
            preset = UNSET
        else:
            preset = check_user_preferences_custom_theme_type_0_preset(_preset)

        user_preferences_custom_theme_type_0 = cls(
            base=base,
            accent=accent,
            background=background,
            preset=preset,
        )

        user_preferences_custom_theme_type_0.additional_properties = _src
        return user_preferences_custom_theme_type_0

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
