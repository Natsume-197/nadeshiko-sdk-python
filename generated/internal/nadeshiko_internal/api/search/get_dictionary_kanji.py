from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dictionary_kanji import DictionaryKanji
from ...models.error_400 import Error400
from ...models.error_403 import Error403
from ...models.error_404 import Error404
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...models.get_dictionary_kanji_locale import (
    GetDictionaryKanjiLocale,
)
from ...models.get_dictionary_kanji_related import (
    GetDictionaryKanjiRelated,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    character: str,
    *,
    locale: GetDictionaryKanjiLocale | Unset = "en",
    related: GetDictionaryKanjiRelated | Unset = "short",
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_locale: str | Unset = UNSET
    if not isinstance(locale, Unset):
        json_locale = locale

    params["locale"] = json_locale

    json_related: str | Unset = UNSET
    if not isinstance(related, Unset):
        json_related = related

    params["related"] = json_related

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dictionary/kanji/{character}".format(
            character=quote(str(character), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = DictionaryKanji.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Error400.from_dict(response.json())

        return response_400

    if response.status_code == 403:
        response_403 = Error403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = Error404.from_dict(response.json())

        return response_404

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
) -> Response[DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    character: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetDictionaryKanjiLocale | Unset = "en",
    related: GetDictionaryKanjiRelated | Unset = "short",
) -> Response[DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500]:
    """One kanji's card from Nadeshiko's own dictionary, for our own server only

     What the word card shows when a reader opens one of a word's kanji: readings
    and meanings (KANJIDIC2), its parts (KRADFILE), its stroke order (KanjiVG) and
    the words written with it that Nadeshiko's subtitles use most. Called by the
    frontend server, which caches it; refused unless the request came through our
    own Nitro proxy.

    Args:
        character (str):
        locale (GetDictionaryKanjiLocale | Unset):  Default: 'en'.
        related (GetDictionaryKanjiRelated | Unset):  Default: 'short'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        character=character,
        locale=locale,
        related=related,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    character: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetDictionaryKanjiLocale | Unset = "en",
    related: GetDictionaryKanjiRelated | Unset = "short",
) -> DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500 | None:
    """One kanji's card from Nadeshiko's own dictionary, for our own server only

     What the word card shows when a reader opens one of a word's kanji: readings
    and meanings (KANJIDIC2), its parts (KRADFILE), its stroke order (KanjiVG) and
    the words written with it that Nadeshiko's subtitles use most. Called by the
    frontend server, which caches it; refused unless the request came through our
    own Nitro proxy.

    Args:
        character (str):
        locale (GetDictionaryKanjiLocale | Unset):  Default: 'en'.
        related (GetDictionaryKanjiRelated | Unset):  Default: 'short'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500
    """

    return sync_detailed(
        character=character,
        client=client,
        locale=locale,
        related=related,
    ).parsed


async def asyncio_detailed(
    character: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetDictionaryKanjiLocale | Unset = "en",
    related: GetDictionaryKanjiRelated | Unset = "short",
) -> Response[DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500]:
    """One kanji's card from Nadeshiko's own dictionary, for our own server only

     What the word card shows when a reader opens one of a word's kanji: readings
    and meanings (KANJIDIC2), its parts (KRADFILE), its stroke order (KanjiVG) and
    the words written with it that Nadeshiko's subtitles use most. Called by the
    frontend server, which caches it; refused unless the request came through our
    own Nitro proxy.

    Args:
        character (str):
        locale (GetDictionaryKanjiLocale | Unset):  Default: 'en'.
        related (GetDictionaryKanjiRelated | Unset):  Default: 'short'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        character=character,
        locale=locale,
        related=related,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    character: str,
    *,
    client: AuthenticatedClient | Client,
    locale: GetDictionaryKanjiLocale | Unset = "en",
    related: GetDictionaryKanjiRelated | Unset = "short",
) -> DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500 | None:
    """One kanji's card from Nadeshiko's own dictionary, for our own server only

     What the word card shows when a reader opens one of a word's kanji: readings
    and meanings (KANJIDIC2), its parts (KRADFILE), its stroke order (KanjiVG) and
    the words written with it that Nadeshiko's subtitles use most. Called by the
    frontend server, which caches it; refused unless the request came through our
    own Nitro proxy.

    Args:
        character (str):
        locale (GetDictionaryKanjiLocale | Unset):  Default: 'en'.
        related (GetDictionaryKanjiRelated | Unset):  Default: 'short'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictionaryKanji | Error400 | Error403 | Error404 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            character=character,
            client=client,
            locale=locale,
            related=related,
        )
    ).parsed
