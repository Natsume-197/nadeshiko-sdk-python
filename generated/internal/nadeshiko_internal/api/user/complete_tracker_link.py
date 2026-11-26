from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_tracker_link_body import CompleteTrackerLinkBody
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_500 import Error500
from ...models.tracker_state import TrackerState
from ...types import Response


def _get_kwargs(
    *,
    body: CompleteTrackerLinkBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/user/connections/tracker/callback",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error500 | TrackerState | None:
    if response.status_code == 200:
        response_200 = TrackerState.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Error401.from_dict(response.json())

        return response_401

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error400 | Error401 | Error500 | TrackerState]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteTrackerLinkBody,
) -> Response[Error400 | Error401 | Error500 | TrackerState]:
    """Complete anime tracker OAuth linking

     Exchanges the one-time OAuth code, stores encrypted credentials, replaces any prior tracker, and
    runs the initial list sync.

    Args:
        body (CompleteTrackerLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error500 | TrackerState]
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
    body: CompleteTrackerLinkBody,
) -> Error400 | Error401 | Error500 | TrackerState | None:
    """Complete anime tracker OAuth linking

     Exchanges the one-time OAuth code, stores encrypted credentials, replaces any prior tracker, and
    runs the initial list sync.

    Args:
        body (CompleteTrackerLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error500 | TrackerState
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CompleteTrackerLinkBody,
) -> Response[Error400 | Error401 | Error500 | TrackerState]:
    """Complete anime tracker OAuth linking

     Exchanges the one-time OAuth code, stores encrypted credentials, replaces any prior tracker, and
    runs the initial list sync.

    Args:
        body (CompleteTrackerLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error500 | TrackerState]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CompleteTrackerLinkBody,
) -> Error400 | Error401 | Error500 | TrackerState | None:
    """Complete anime tracker OAuth linking

     Exchanges the one-time OAuth code, stores encrypted credentials, replaces any prior tracker, and
    runs the initial list sync.

    Args:
        body (CompleteTrackerLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error500 | TrackerState
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
