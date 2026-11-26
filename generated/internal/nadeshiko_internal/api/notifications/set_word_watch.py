from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.error_503 import Error503
from ...models.set_word_watch_body import SetWordWatchBody
from ...models.word_watch_set_response import WordWatchSetResponse
from ...types import Response


def _get_kwargs(
    *,
    body: SetWordWatchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/word-watches",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse | None:
    if response.status_code == 200:
        response_200 = WordWatchSetResponse.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = WordWatchSetResponse.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error403.from_dict(response.json())

        return response_403

    if response.status_code == 429:
        response_429 = Error429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = Error503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SetWordWatchBody,
) -> Response[
    Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse
]:
    """Watch a word, or switch the alert you have on it

     Creates the reader's alert on a word, or switches their existing alert on the
    same word and match mode to the asked mode. The word must be one Japanese word
    of up to 16 characters. `FIRST` is refused for a word that already has
    sentences in the reader's search, and `NEW_SENTENCES` for a `CONTAINS` search.

    Args:
        body (SetWordWatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SetWordWatchBody,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse | None:
    """Watch a word, or switch the alert you have on it

     Creates the reader's alert on a word, or switches their existing alert on the
    same word and match mode to the asked mode. The word must be one Japanese word
    of up to 16 characters. `FIRST` is refused for a word that already has
    sentences in the reader's search, and `NEW_SENTENCES` for a `CONTAINS` search.

    Args:
        body (SetWordWatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SetWordWatchBody,
) -> Response[
    Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse
]:
    """Watch a word, or switch the alert you have on it

     Creates the reader's alert on a word, or switches their existing alert on the
    same word and match mode to the asked mode. The word must be one Japanese word
    of up to 16 characters. `FIRST` is refused for a word that already has
    sentences in the reader's search, and `NEW_SENTENCES` for a `CONTAINS` search.

    Args:
        body (SetWordWatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SetWordWatchBody,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse | None:
    """Watch a word, or switch the alert you have on it

     Creates the reader's alert on a word, or switches their existing alert on the
    same word and match mode to the asked mode. The word must be one Japanese word
    of up to 16 characters. `FIRST` is refused for a word that already has
    sentences in the reader's search, and `NEW_SENTENCES` for a `CONTAINS` search.

    Args:
        body (SetWordWatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | Error503 | WordWatchSetResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
