from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_400 import Error400
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.identify_dictionary_word_locale import (
    IdentifyDictionaryWordLocale,
)
from ...models.identify_dictionary_word_response_200 import IdentifyDictionaryWordResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lemma: str,
    surface: str | Unset = UNSET,
    reading: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    locale: IdentifyDictionaryWordLocale | Unset = "en",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lemma"] = lemma

    params["surface"] = surface

    params["reading"] = reading

    params["pos"] = pos

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale

    params["locale"] = json_locale

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dictionary/identify",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200 | None:
    if response.status_code == 200:
        response_200 = IdentifyDictionaryWordResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

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
) -> Response[Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    lemma: str,
    surface: str | Unset = UNSET,
    reading: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    locale: IdentifyDictionaryWordLocale | Unset = "en",
) -> Response[Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200]:
    """Rank Nadeshiko's dictionary entries for one token, for our own server only

     The word card's dictionary lookup. Takes what a stored token carries and
    returns ranked candidates in the card's shape. Called by the frontend server,
    which owns caching; refused unless the request came through our own Nitro proxy.

    Args:
        lemma (str):
        surface (str | Unset):
        reading (str | Unset):
        pos (str | Unset):
        locale (IdentifyDictionaryWordLocale | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200]
    """

    kwargs = _get_kwargs(
        lemma=lemma,
        surface=surface,
        reading=reading,
        pos=pos,
        locale=locale,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    lemma: str,
    surface: str | Unset = UNSET,
    reading: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    locale: IdentifyDictionaryWordLocale | Unset = "en",
) -> Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200 | None:
    """Rank Nadeshiko's dictionary entries for one token, for our own server only

     The word card's dictionary lookup. Takes what a stored token carries and
    returns ranked candidates in the card's shape. Called by the frontend server,
    which owns caching; refused unless the request came through our own Nitro proxy.

    Args:
        lemma (str):
        surface (str | Unset):
        reading (str | Unset):
        pos (str | Unset):
        locale (IdentifyDictionaryWordLocale | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200
    """

    return sync_detailed(
        client=client,
        lemma=lemma,
        surface=surface,
        reading=reading,
        pos=pos,
        locale=locale,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    lemma: str,
    surface: str | Unset = UNSET,
    reading: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    locale: IdentifyDictionaryWordLocale | Unset = "en",
) -> Response[Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200]:
    """Rank Nadeshiko's dictionary entries for one token, for our own server only

     The word card's dictionary lookup. Takes what a stored token carries and
    returns ranked candidates in the card's shape. Called by the frontend server,
    which owns caching; refused unless the request came through our own Nitro proxy.

    Args:
        lemma (str):
        surface (str | Unset):
        reading (str | Unset):
        pos (str | Unset):
        locale (IdentifyDictionaryWordLocale | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200]
    """

    kwargs = _get_kwargs(
        lemma=lemma,
        surface=surface,
        reading=reading,
        pos=pos,
        locale=locale,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    lemma: str,
    surface: str | Unset = UNSET,
    reading: str | Unset = UNSET,
    pos: str | Unset = UNSET,
    locale: IdentifyDictionaryWordLocale | Unset = "en",
) -> Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200 | None:
    """Rank Nadeshiko's dictionary entries for one token, for our own server only

     The word card's dictionary lookup. Takes what a stored token carries and
    returns ranked candidates in the card's shape. Called by the frontend server,
    which owns caching; refused unless the request came through our own Nitro proxy.

    Args:
        lemma (str):
        surface (str | Unset):
        reading (str | Unset):
        pos (str | Unset):
        locale (IdentifyDictionaryWordLocale | Unset):  Default: 'en'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Error400 | Error403 | Error429 | Error500 | IdentifyDictionaryWordResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            lemma=lemma,
            surface=surface,
            reading=reading,
            pos=pos,
            locale=locale,
        )
    ).parsed
