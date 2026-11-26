from typing import Literal

UserPreferencesCustomThemeType0Base = Literal["dark", "light"]

USER_PREFERENCES_CUSTOM_THEME_TYPE_0_BASE_VALUES: set[UserPreferencesCustomThemeType0Base] = {
    "dark",
    "light",
}


def check_user_preferences_custom_theme_type_0_base(
    value: str,
) -> UserPreferencesCustomThemeType0Base:
    if value in USER_PREFERENCES_CUSTOM_THEME_TYPE_0_BASE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_PREFERENCES_CUSTOM_THEME_TYPE_0_BASE_VALUES!r}"
    )
