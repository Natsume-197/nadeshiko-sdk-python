from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_500 import Error500
from ...models.start_tracker_link_body import StartTrackerLinkBody
from ...models.start_tracker_link_response_201 import StartTrackerLinkResponse201
from ...types import Response


def _get_kwargs(
    *,
    body: StartTrackerLinkBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/user/connections/tracker",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error500 | StartTrackerLinkResponse201 | None:
    if response.status_code == 201:
        response_201 = StartTrackerLinkResponse201.from_dict(response.json())

        return response_201

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
) -> Response[Error400 | Error401 | Error500 | StartTrackerLinkResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: StartTrackerLinkBody,
) -> Response[Error400 | Error401 | Error500 | StartTrackerLinkResponse201]:
    """Begin anime tracker OAuth linking

     Returns the provider's OAuth authorization URL with sealed state bound to the signed-in reader.

    Args:
        body (StartTrackerLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error500 | StartTrackerLinkResponse201]
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
    body: StartTrackerLinkBody,
) -> Error400 | Error401 | Error500 | StartTrackerLinkResponse201 | None:
    """Begin anime tracker OAuth linking

     Returns the provider's OAuth authorization URL with sealed state bound to the signed-in reader.

    Args:
        body (StartTrackerLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error500 | StartTrackerLinkResponse201
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: StartTrackerLinkBody,
) -> Response[Error400 | Error401 | Error500 | StartTrackerLinkResponse201]:
    """Begin anime tracker OAuth linking

     Returns the provider's OAuth authorization URL with sealed state bound to the signed-in reader.

    Args:
        body (StartTrackerLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error500 | StartTrackerLinkResponse201]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: StartTrackerLinkBody,
) -> Error400 | Error401 | Error500 | StartTrackerLinkResponse201 | None:
    """Begin anime tracker OAuth linking

     Returns the provider's OAuth authorization URL with sealed state bound to the signed-in reader.

    Args:
        body (StartTrackerLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error500 | StartTrackerLinkResponse201
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
