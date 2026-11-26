from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_401 import Error401
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.list_my_content_requests_category import (
    ListMyContentRequestsCategory,
)
from ...models.list_my_content_requests_response_200 import ListMyContentRequestsResponse200
from ...models.list_my_content_requests_scope import (
    ListMyContentRequestsScope,
)
from ...models.list_my_content_requests_sort import (
    ListMyContentRequestsSort,
)
from ...models.list_my_content_requests_status import (
    ListMyContentRequestsStatus,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    scope: ListMyContentRequestsScope | Unset = "OWN",
    status: ListMyContentRequestsStatus | Unset = "ALL",
    category: ListMyContentRequestsCategory | Unset = UNSET,
    sort: ListMyContentRequestsSort | Unset = "RECENT",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_scope: str | Unset = UNSET
    if not isinstance(scope, Unset):
        json_scope = scope

    params["scope"] = json_scope

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
        "url": "/v1/requests/mine",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListMyContentRequestsResponse200.from_dict(response.json())

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
) -> Response[Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    scope: ListMyContentRequestsScope | Unset = "OWN",
    status: ListMyContentRequestsStatus | Unset = "ALL",
    category: ListMyContentRequestsCategory | Unset = UNSET,
    sort: ListMyContentRequestsSort | Unset = "RECENT",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
) -> Response[Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200]:
    """List the signed-in reader's own or voted content requests

     Returns requests filed by the signed-in reader (`OWN`) or requests they voted for or boosted
    (`VOTED`), across all statuses.

    Args:
        scope (ListMyContentRequestsScope | Unset):  Default: 'OWN'.
        status (ListMyContentRequestsStatus | Unset):  Default: 'ALL'.
        category (ListMyContentRequestsCategory | Unset):
        sort (ListMyContentRequestsSort | Unset):  Default: 'RECENT'.
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200]
    """

    kwargs = _get_kwargs(
        scope=scope,
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
    client: AuthenticatedClient,
    scope: ListMyContentRequestsScope | Unset = "OWN",
    status: ListMyContentRequestsStatus | Unset = "ALL",
    category: ListMyContentRequestsCategory | Unset = UNSET,
    sort: ListMyContentRequestsSort | Unset = "RECENT",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
) -> Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200 | None:
    """List the signed-in reader's own or voted content requests

     Returns requests filed by the signed-in reader (`OWN`) or requests they voted for or boosted
    (`VOTED`), across all statuses.

    Args:
        scope (ListMyContentRequestsScope | Unset):  Default: 'OWN'.
        status (ListMyContentRequestsStatus | Unset):  Default: 'ALL'.
        category (ListMyContentRequestsCategory | Unset):
        sort (ListMyContentRequestsSort | Unset):  Default: 'RECENT'.
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200
    """

    return sync_detailed(
        client=client,
        scope=scope,
        status=status,
        category=category,
        sort=sort,
        q=q,
        page=page,
        take=take,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    scope: ListMyContentRequestsScope | Unset = "OWN",
    status: ListMyContentRequestsStatus | Unset = "ALL",
    category: ListMyContentRequestsCategory | Unset = UNSET,
    sort: ListMyContentRequestsSort | Unset = "RECENT",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
) -> Response[Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200]:
    """List the signed-in reader's own or voted content requests

     Returns requests filed by the signed-in reader (`OWN`) or requests they voted for or boosted
    (`VOTED`), across all statuses.

    Args:
        scope (ListMyContentRequestsScope | Unset):  Default: 'OWN'.
        status (ListMyContentRequestsStatus | Unset):  Default: 'ALL'.
        category (ListMyContentRequestsCategory | Unset):
        sort (ListMyContentRequestsSort | Unset):  Default: 'RECENT'.
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200]
    """

    kwargs = _get_kwargs(
        scope=scope,
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
    client: AuthenticatedClient,
    scope: ListMyContentRequestsScope | Unset = "OWN",
    status: ListMyContentRequestsStatus | Unset = "ALL",
    category: ListMyContentRequestsCategory | Unset = UNSET,
    sort: ListMyContentRequestsSort | Unset = "RECENT",
    q: str | Unset = UNSET,
    page: int | Unset = 1,
    take: int | Unset = 24,
) -> Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200 | None:
    """List the signed-in reader's own or voted content requests

     Returns requests filed by the signed-in reader (`OWN`) or requests they voted for or boosted
    (`VOTED`), across all statuses.

    Args:
        scope (ListMyContentRequestsScope | Unset):  Default: 'OWN'.
        status (ListMyContentRequestsStatus | Unset):  Default: 'ALL'.
        category (ListMyContentRequestsCategory | Unset):
        sort (ListMyContentRequestsSort | Unset):  Default: 'RECENT'.
        q (str | Unset):
        page (int | Unset):  Default: 1.
        take (int | Unset):  Default: 24.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error429 | Error500 | ListMyContentRequestsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            scope=scope,
            status=status,
            category=category,
            sort=sort,
            q=q,
            page=page,
            take=take,
        )
    ).parsed
