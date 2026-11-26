from typing import Literal

UserPreferencesCustomThemeType0Preset = Literal[
    "custom", "indigo", "lavender", "matcha", "midnight", "ocean", "sepia", "sunset"
]

USER_PREFERENCES_CUSTOM_THEME_TYPE_0_PRESET_VALUES: set[UserPreferencesCustomThemeType0Preset] = {
    "custom",
    "indigo",
    "lavender",
    "matcha",
    "midnight",
    "ocean",
    "sepia",
    "sunset",
}


def check_user_preferences_custom_theme_type_0_preset(
    value: str,
) -> UserPreferencesCustomThemeType0Preset:
    if value in USER_PREFERENCES_CUSTOM_THEME_TYPE_0_PRESET_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_CUSTOM_THEME_TYPE_0_PRESET_VALUES!r}"
    )
