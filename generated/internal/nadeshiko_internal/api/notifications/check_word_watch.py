from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_word_watch_match_mode import (
    CheckWordWatchMatchMode,
)
from ...models.check_word_watch_response_200 import CheckWordWatchResponse200
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    match_mode: CheckWordWatchMatchMode | Unset = "WORD",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["query"] = query

    json_match_mode: str | Unset = UNSET
    if not isinstance(match_mode, Unset):
        json_match_mode = match_mode

    params["matchMode"] = json_match_mode

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/word-watches/check",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = CheckWordWatchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

    if response.status_code == 429:
        response_429 = Error429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    match_mode: CheckWordWatchMatchMode | Unset = "WORD",
) -> Response[CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500]:
    """The reader's alert on one word, if any

     What the search page reads to draw its alert button.

    Args:
        query (str):
        match_mode (CheckWordWatchMatchMode | Unset):  Default: 'WORD'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        query=query,
        match_mode=match_mode,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    match_mode: CheckWordWatchMatchMode | Unset = "WORD",
) -> CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500 | None:
    """The reader's alert on one word, if any

     What the search page reads to draw its alert button.

    Args:
        query (str):
        match_mode (CheckWordWatchMatchMode | Unset):  Default: 'WORD'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
        query=query,
        match_mode=match_mode,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    match_mode: CheckWordWatchMatchMode | Unset = "WORD",
) -> Response[CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500]:
    """The reader's alert on one word, if any

     What the search page reads to draw its alert button.

    Args:
        query (str):
        match_mode (CheckWordWatchMatchMode | Unset):  Default: 'WORD'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        query=query,
        match_mode=match_mode,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    match_mode: CheckWordWatchMatchMode | Unset = "WORD",
) -> CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500 | None:
    """The reader's alert on one word, if any

     What the search page reads to draw its alert button.

    Args:
        query (str):
        match_mode (CheckWordWatchMatchMode | Unset):  Default: 'WORD'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CheckWordWatchResponse200 | Error400 | Error401 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            match_mode=match_mode,
        )
    ).parsed
