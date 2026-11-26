from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.list_content_requests_category import (
    ListContentRequestsCategory,
)
from ...models.list_content_requests_response_200 import ListContentRequestsResponse200
from ...models.list_content_requests_sort import (
    ListContentRequestsSort,
)
from ...models.list_content_requests_status import (
    ListContentRequestsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    status: ListContentRequestsStatus | Unset = "ACTIVE",
    category: ListContentRequestsCategory | Unset = UNSET,
    sort: ListContentRequestsSort | Unset = "TOP",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
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

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort

    params["sort"] = json_sort

    params["q"] = q

    params["page"] = page

    params["take"] = take

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/requests",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error429 | Error500 | ListContentRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListContentRequestsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

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
) -> Response[Error400 | Error429 | Error500 | ListContentRequestsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListContentRequestsStatus | Unset = "ACTIVE",
    category: ListContentRequestsCategory | Unset = UNSET,
    sort: ListContentRequestsSort | Unset = "TOP",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
) -> Response[Error400 | Error429 | Error500 | ListContentRequestsResponse200]:
    """List content requests

     Public list of content requests, sorted by score (votes plus five per boost) or by date. Requester
    identities never appear.

    Args:
        status (ListContentRequestsStatus | Unset):  Default: 'ACTIVE'.
        category (ListContentRequestsCategory | Unset):
        sort (ListContentRequestsSort | Unset):  Default: 'TOP'.
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error429 | Error500 | ListContentRequestsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        category=category,
        sort=sort,
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
    client: AuthenticatedClient | Client,
    status: ListContentRequestsStatus | Unset = "ACTIVE",
    category: ListContentRequestsCategory | Unset = UNSET,
    sort: ListContentRequestsSort | Unset = "TOP",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
) -> Error400 | Error429 | Error500 | ListContentRequestsResponse200 | None:
    """List content requests

     Public list of content requests, sorted by score (votes plus five per boost) or by date. Requester
    identities never appear.

    Args:
        status (ListContentRequestsStatus | Unset):  Default: 'ACTIVE'.
        category (ListContentRequestsCategory | Unset):
        sort (ListContentRequestsSort | Unset):  Default: 'TOP'.
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error429 | Error500 | ListContentRequestsResponse200
    """

    return sync_detailed(
        client=client,
        status=status,
        category=category,
        sort=sort,
        q=q,
        page=page,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    status: ListContentRequestsStatus | Unset = "ACTIVE",
    category: ListContentRequestsCategory | Unset = UNSET,
    sort: ListContentRequestsSort | Unset = "TOP",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
) -> Response[Error400 | Error429 | Error500 | ListContentRequestsResponse200]:
    """List content requests

     Public list of content requests, sorted by score (votes plus five per boost) or by date. Requester
    identities never appear.

    Args:
        status (ListContentRequestsStatus | Unset):  Default: 'ACTIVE'.
        category (ListContentRequestsCategory | Unset):
        sort (ListContentRequestsSort | Unset):  Default: 'TOP'.
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error429 | Error500 | ListContentRequestsResponse200]
    """

    kwargs = _get_kwargs(
        status=status,
        category=category,
        sort=sort,
        q=q,
        page=page,
        take=take,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    status: ListContentRequestsStatus | Unset = "ACTIVE",
    category: ListContentRequestsCategory | Unset = UNSET,
    sort: ListContentRequestsSort | Unset = "TOP",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
) -> Error400 | Error429 | Error500 | ListContentRequestsResponse200 | None:
    """List content requests

     Public list of content requests, sorted by score (votes plus five per boost) or by date. Requester
    identities never appear.

    Args:
        status (ListContentRequestsStatus | Unset):  Default: 'ACTIVE'.
        category (ListContentRequestsCategory | Unset):
        sort (ListContentRequestsSort | Unset):  Default: 'TOP'.
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error429 | Error500 | ListContentRequestsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            status=status,
            category=category,
            sort=sort,
            q=q,
            page=page,
            take=take,
        )
    ).parsed
