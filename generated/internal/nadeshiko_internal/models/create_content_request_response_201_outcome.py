from typing import Literal

CreateContentRequestResponse201Outcome = Literal["created"]

CREATE_CONTENT_REQUEST_RESPONSE_201_OUTCOME_VALUES: set[CreateContentRequestResponse201Outcome] = {
    "created",
}


def check_create_content_request_response_201_outcome(
    value: str,
) -> CreateContentRequestResponse201Outcome:
    if value in CREATE_CONTENT_REQUEST_RESPONSE_201_OUTCOME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONTENT_REQUEST_RESPONSE_201_OUTCOME_VALUES!r}"
    )
