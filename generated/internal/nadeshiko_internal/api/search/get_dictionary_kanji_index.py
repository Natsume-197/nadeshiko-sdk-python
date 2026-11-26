from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.get_dictionary_kanji_index_locale import (
    GetDictionaryKanjiIndexLocale,
)
from ...models.get_dictionary_kanji_index_response_200 import GetDictionaryKanjiIndexResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    locale: GetDictionaryKanjiIndexLocale | Unset = "en",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale

    params["locale"] = json_locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dictionary/kanji",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200 | None:
    if response.status_code == 200:
        response_200 = GetDictionaryKanjiIndexResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: GetDictionaryKanjiIndexLocale | Unset = "en",
) -> Response[Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200]:
    """Every jōyō and JLPT kanji, for our own server only

     The kanji index page's list: the 2,136 jōyō kanji and any other JLPT kanji,
    each with its school grade, JLPT level, newspaper rank, one reading and one
    meaning. Called by the frontend server, which caches it.

    Args:
        locale (GetDictionaryKanjiIndexLocale | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    locale: GetDictionaryKanjiIndexLocale | Unset = "en",
) -> Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200 | None:
    """Every jōyō and JLPT kanji, for our own server only

     The kanji index page's list: the 2,136 jōyō kanji and any other JLPT kanji,
    each with its school grade, JLPT level, newspaper rank, one reading and one
    meaning. Called by the frontend server, which caches it.

    Args:
        locale (GetDictionaryKanjiIndexLocale | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200
    """

    return sync_detailed(
        client=client,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    locale: GetDictionaryKanjiIndexLocale | Unset = "en",
) -> Response[Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200]:
    """Every jōyō and JLPT kanji, for our own server only

     The kanji index page's list: the 2,136 jōyō kanji and any other JLPT kanji,
    each with its school grade, JLPT level, newspaper rank, one reading and one
    meaning. Called by the frontend server, which caches it.

    Args:
        locale (GetDictionaryKanjiIndexLocale | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200]
    """

    kwargs = _get_kwargs(
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    locale: GetDictionaryKanjiIndexLocale | Unset = "en",
) -> Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200 | None:
    """Every jōyō and JLPT kanji, for our own server only

     The kanji index page's list: the 2,136 jōyō kanji and any other JLPT kanji,
    each with its school grade, JLPT level, newspaper rank, one reading and one
    meaning. Called by the frontend server, which caches it.

    Args:
        locale (GetDictionaryKanjiIndexLocale | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error403 | Error429 | Error500 | GetDictionaryKanjiIndexResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            locale=locale,
        )
    ).parsed
