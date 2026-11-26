from typing import Literal

CreateContentRequestResponse200Outcome = Literal["already_voted", "voted"]

CREATE_CONTENT_REQUEST_RESPONSE_200_OUTCOME_VALUES: set[CreateContentRequestResponse200Outcome] = {
    "already_voted",
    "voted",
}


def check_create_content_request_response_200_outcome(
    value: str,
) -> CreateContentRequestResponse200Outcome:
    if value in CREATE_CONTENT_REQUEST_RESPONSE_200_OUTCOME_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CREATE_CONTENT_REQUEST_RESPONSE_200_OUTCOME_VALUES!r}"
    )
