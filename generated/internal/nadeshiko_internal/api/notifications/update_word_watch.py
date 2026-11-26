from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.error_503 import Error503
from ...models.update_word_watch_body import UpdateWordWatchBody
from ...models.word_watch import WordWatch
from ...types import Response


def _get_kwargs(
    watch_id: UUID,
    *,
    body: UpdateWordWatchBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/word-watches/{watch_id}".format(
            watch_id=quote(str(watch_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch | None:
    if response.status_code == 200:
        response_200 = WordWatch.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = Error403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error404.from_dict(response.json())

        return response_404

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
    Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    watch_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateWordWatchBody,
) -> Response[
    Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch
]:
    """Pause, resume or switch a word alert

     `paused: true` pauses the alert. `paused: false` or a new `mode` makes it
    active again and starts counting from now, so a long pause does not arrive
    as one huge digest.

    Args:
        watch_id (UUID):
        body (UpdateWordWatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch]
    """

    kwargs = _get_kwargs(
        watch_id=watch_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    watch_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateWordWatchBody,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch | None:
    """Pause, resume or switch a word alert

     `paused: true` pauses the alert. `paused: false` or a new `mode` makes it
    active again and starts counting from now, so a long pause does not arrive
    as one huge digest.

    Args:
        watch_id (UUID):
        body (UpdateWordWatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch
    """

    return sync_detailed(
        watch_id=watch_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    watch_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateWordWatchBody,
) -> Response[
    Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch
]:
    """Pause, resume or switch a word alert

     `paused: true` pauses the alert. `paused: false` or a new `mode` makes it
    active again and starts counting from now, so a long pause does not arrive
    as one huge digest.

    Args:
        watch_id (UUID):
        body (UpdateWordWatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch]
    """

    kwargs = _get_kwargs(
        watch_id=watch_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    watch_id: UUID,
    *,
    client: AuthenticatedClient,
    body: UpdateWordWatchBody,
) -> Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch | None:
    """Pause, resume or switch a word alert

     `paused: true` pauses the alert. `paused: false` or a new `mode` makes it
    active again and starts counting from now, so a long pause does not arrive
    as one huge digest.

    Args:
        watch_id (UUID):
        body (UpdateWordWatchBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error404 | Error429 | Error500 | Error503 | WordWatch
    """

    return (
        await asyncio_detailed(
            watch_id=watch_id,
            client=client,
            body=body,
        )
    ).parsed
