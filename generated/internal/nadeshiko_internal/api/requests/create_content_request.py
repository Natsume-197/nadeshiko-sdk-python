from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_content_request_body import CreateContentRequestBody
from ...models.create_content_request_response_200 import CreateContentRequestResponse200
from ...models.create_content_request_response_201 import CreateContentRequestResponse201
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs(
    *,
    body: CreateContentRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/requests",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreateContentRequestResponse200
    | CreateContentRequestResponse201
    | Error400
    | Error401
    | Error403
    | Error429
    | Error500
    | None
):
    if response.status_code == 200:
        response_200 = CreateContentRequestResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = CreateContentRequestResponse201.from_dict(response.json())

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

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreateContentRequestResponse200
    | CreateContentRequestResponse201
    | Error400
    | Error401
    | Error403
    | Error429
    | Error500
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
    body: CreateContentRequestBody,
) -> Response[
    CreateContentRequestResponse200
    | CreateContentRequestResponse201
    | Error400
    | Error401
    | Error403
    | Error429
    | Error500
]:
    """Request content

     Files a request from a link to AniList, TMDB, MyDramaList, Audible, Amazon or YouTube. When the same
    title is
    already requested, adds the reader's vote to that request instead (200). A request for a title
    already on
    Nadeshiko becomes an UPDATE request for it.

    Args:
        body (CreateContentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateContentRequestResponse200 | CreateContentRequestResponse201 | Error400 | Error401 | Error403 | Error429 | Error500]
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
    body: CreateContentRequestBody,
) -> (
    CreateContentRequestResponse200
    | CreateContentRequestResponse201
    | Error400
    | Error401
    | Error403
    | Error429
    | Error500
    | None
):
    """Request content

     Files a request from a link to AniList, TMDB, MyDramaList, Audible, Amazon or YouTube. When the same
    title is
    already requested, adds the reader's vote to that request instead (200). A request for a title
    already on
    Nadeshiko becomes an UPDATE request for it.

    Args:
        body (CreateContentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateContentRequestResponse200 | CreateContentRequestResponse201 | Error400 | Error401 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateContentRequestBody,
) -> Response[
    CreateContentRequestResponse200
    | CreateContentRequestResponse201
    | Error400
    | Error401
    | Error403
    | Error429
    | Error500
]:
    """Request content

     Files a request from a link to AniList, TMDB, MyDramaList, Audible, Amazon or YouTube. When the same
    title is
    already requested, adds the reader's vote to that request instead (200). A request for a title
    already on
    Nadeshiko becomes an UPDATE request for it.

    Args:
        body (CreateContentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreateContentRequestResponse200 | CreateContentRequestResponse201 | Error400 | Error401 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateContentRequestBody,
) -> (
    CreateContentRequestResponse200
    | CreateContentRequestResponse201
    | Error400
    | Error401
    | Error403
    | Error429
    | Error500
    | None
):
    """Request content

     Files a request from a link to AniList, TMDB, MyDramaList, Audible, Amazon or YouTube. When the same
    title is
    already requested, adds the reader's vote to that request instead (200). A request for a title
    already on
    Nadeshiko becomes an UPDATE request for it.

    Args:
        body (CreateContentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreateContentRequestResponse200 | CreateContentRequestResponse201 | Error400 | Error401 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
