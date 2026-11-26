from typing import Literal

UserDictionaryStatus = Literal["failed", "processing", "ready"]

USER_DICTIONARY_STATUS_VALUES: set[UserDictionaryStatus] = {
    "failed",
    "processing",
    "ready",
}


def check_user_dictionary_status(value: str) -> UserDictionaryStatus:
    if value in USER_DICTIONARY_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {USER_DICTIONARY_STATUS_VALUES!r}"
    )
