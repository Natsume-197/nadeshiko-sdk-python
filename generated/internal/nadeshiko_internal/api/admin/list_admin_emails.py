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
from ...models.list_admin_emails_response_200 import ListAdminEmailsResponse200
from ...models.list_admin_emails_status import ListAdminEmailsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    status: ListAdminEmailsStatus | Unset = UNSET,
    days: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    params["search"] = search

    params["kind"] = kind

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status

    params["status"] = json_status

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/admin/emails",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200 | None:
    if response.status_code == 200:
        response_200 = ListAdminEmailsResponse200.from_dict(response.json())

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
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    status: ListAdminEmailsStatus | Unset = UNSET,
    days: int | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200]:
    """List sent emails

     Returns the email send log newest first, with each message's delivery status, plus counts
    for the last 24 hours.

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        search (str | Unset):
        kind (str | Unset):
        status (ListAdminEmailsStatus | Unset):
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        search=search,
        kind=kind,
        status=status,
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    status: ListAdminEmailsStatus | Unset = UNSET,
    days: int | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200 | None:
    """List sent emails

     Returns the email send log newest first, with each message's delivery status, plus counts
    for the last 24 hours.

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        search (str | Unset):
        kind (str | Unset):
        status (ListAdminEmailsStatus | Unset):
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        search=search,
        kind=kind,
        status=status,
        days=days,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    status: ListAdminEmailsStatus | Unset = UNSET,
    days: int | Unset = UNSET,
) -> Response[Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200]:
    """List sent emails

     Returns the email send log newest first, with each message's delivery status, plus counts
    for the last 24 hours.

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        search (str | Unset):
        kind (str | Unset):
        status (ListAdminEmailsStatus | Unset):
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        search=search,
        kind=kind,
        status=status,
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: int | Unset = 25,
    offset: int | Unset = 0,
    search: str | Unset = UNSET,
    kind: str | Unset = UNSET,
    status: ListAdminEmailsStatus | Unset = UNSET,
    days: int | Unset = UNSET,
) -> Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200 | None:
    """List sent emails

     Returns the email send log newest first, with each message's delivery status, plus counts
    for the last 24 hours.

    Args:
        limit (int | Unset):  Default: 25.
        offset (int | Unset):  Default: 0.
        search (str | Unset):
        kind (str | Unset):
        status (ListAdminEmailsStatus | Unset):
        days (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error401 | Error403 | Error429 | Error500 | ListAdminEmailsResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            search=search,
            kind=kind,
            status=status,
            days=days,
        )
    ).parsed
