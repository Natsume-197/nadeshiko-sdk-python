from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_403 import Error403
from ...models.error_500 import Error500
from ...models.list_admin_content_requests_category import (
    ListAdminContentRequestsCategory,
)
from ...models.list_admin_content_requests_response_200 import ListAdminContentRequestsResponse200
from ...models.list_admin_content_requests_status import (
    ListAdminContentRequestsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: ListAdminContentRequestsStatus | Unset = UNSET,
    category: ListAdminContentRequestsCategory | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 50,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    json_category: str | Unset = UNSET
    if not isinstance(category, Unset):
        json_category = category

    params["category"] = json_category

    params["flagged"] = flagged

    params["q"] = q

    params["page"] = page

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAdminContentRequestsResponse200.from_dict(response.json())

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

    if response.status_code == 500:
        response_500 = Error500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    status: ListAdminContentRequestsStatus | Unset = UNSET,
    category: ListAdminContentRequestsCategory | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 50,
) -> Response[Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200]:
    """List content requests with requester and duplicate flags

    Args:
        status (ListAdminContentRequestsStatus | Unset):
        category (ListAdminContentRequestsCategory | Unset):
        flagged (bool | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        category=category,
        flagged=flagged,
        q=q,
        page=page,
        take=take,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    status: ListAdminContentRequestsStatus | Unset = UNSET,
    category: ListAdminContentRequestsCategory | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 50,
) -> Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200 | None:
    """List content requests with requester and duplicate flags

    Args:
        status (ListAdminContentRequestsStatus | Unset):
        category (ListAdminContentRequestsCategory | Unset):
        flagged (bool | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200
    """

    return sync_detailed(
        client=client,
        status=status,
        category=category,
        flagged=flagged,
        q=q,
        page=page,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    status: ListAdminContentRequestsStatus | Unset = UNSET,
    category: ListAdminContentRequestsCategory | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 50,
) -> Response[Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200]:
    """List content requests with requester and duplicate flags

    Args:
        status (ListAdminContentRequestsStatus | Unset):
        category (ListAdminContentRequestsCategory | Unset):
        flagged (bool | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        category=category,
        flagged=flagged,
        q=q,
        page=page,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    status: ListAdminContentRequestsStatus | Unset = UNSET,
    category: ListAdminContentRequestsCategory | Unset = UNSET,
    flagged: bool | Unset = UNSET,
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 50,
) -> Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200 | None:
    """List content requests with requester and duplicate flags

    Args:
        status (ListAdminContentRequestsStatus | Unset):
        category (ListAdminContentRequestsCategory | Unset):
        flagged (bool | Unset):
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error500 | ListAdminContentRequestsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            category=category,
            flagged=flagged,
            q=q,
            page=page,
            take=take,
        )
    ).parsed
