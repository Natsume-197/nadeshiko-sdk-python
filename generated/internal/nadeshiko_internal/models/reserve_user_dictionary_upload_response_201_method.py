from typing import Literal

ReserveUserDictionaryUploadResponse201Method = Literal["PUT"]

RESERVE_USER_DICTIONARY_UPLOAD_RESPONSE_201_METHOD_VALUES: set[
    ReserveUserDictionaryUploadResponse201Method
] = {
    "PUT",
}


def check_reserve_user_dictionary_upload_response_201_method(
    value: str,
) -> ReserveUserDictionaryUploadResponse201Method:
    if value in RESERVE_USER_DICTIONARY_UPLOAD_RESPONSE_201_METHOD_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESERVE_USER_DICTIONARY_UPLOAD_RESPONSE_201_METHOD_VALUES!r}"
    )
