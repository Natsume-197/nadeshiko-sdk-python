from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.admin_content_request import AdminContentRequest
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_500 import Error500
from ...models.merge_admin_content_request_body import MergeAdminContentRequestBody
from ...types import Response


def _get_kwargs(
    request_id: UUID,
    *,
    body: MergeAdminContentRequestBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/admin/requests/{request_id}/merge".format(
            request_id=quote(str(request_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500 | None:
    if response.status_code == 200:
        response_200 = AdminContentRequest.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MergeAdminContentRequestBody,
) -> Response[AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500]:
    """Merge a duplicate request into another

     Moves the duplicate's voters and boosters to the target (no one counts twice) and declines the
    duplicate with a pointer to it.

    Args:
        request_id (UUID):
        body (MergeAdminContentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MergeAdminContentRequestBody,
) -> AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500 | None:
    """Merge a duplicate request into another

     Moves the duplicate's voters and boosters to the target (no one counts twice) and declines the
    duplicate with a pointer to it.

    Args:
        request_id (UUID):
        body (MergeAdminContentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500
    """

    return sync_detailed(
        request_id=request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MergeAdminContentRequestBody,
) -> Response[AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500]:
    """Merge a duplicate request into another

     Moves the duplicate's voters and boosters to the target (no one counts twice) and declines the
    duplicate with a pointer to it.

    Args:
        request_id (UUID):
        body (MergeAdminContentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500]
    """

    kwargs = _get_kwargs(
        request_id=request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    request_id: UUID,
    *,
    client: AuthenticatedClient,
    body: MergeAdminContentRequestBody,
) -> AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500 | None:
    """Merge a duplicate request into another

     Moves the duplicate's voters and boosters to the target (no one counts twice) and declines the
    duplicate with a pointer to it.

    Args:
        request_id (UUID):
        body (MergeAdminContentRequestBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AdminContentRequest | Error400 | Error401 | Error403 | Error404 | Error500
    """

    return (
        await asyncio_detailed(
            request_id=request_id,
            client=client,
            body=body,
        )
    ).parsed
