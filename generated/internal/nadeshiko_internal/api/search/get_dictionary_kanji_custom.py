from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.dictionary_kanji_custom import DictionaryKanjiCustom
from ...models.error_400 import Error400
from ...models.error_403 import Error403
from ...models.error_429 import Error429
from ...models.error_500 import Error500
from ...types import Response


def _get_kwargs(
    character: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/dictionary/kanji/{character}/custom".format(
            character=quote(str(character), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500 | None:
    if response.status_code == 200:
        response_200 = DictionaryKanjiCustom.from_dict(response.json())

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
) -> Response[DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500]:
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
) -> Response[DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500]:
    """One kanji from the reader's own kanji dictionaries, for our own server only

     The reader's part of the kanji card: entries and frequencies from their enabled custom kanji
    dictionaries.
    Separate from the shared kanji card so that one stays cached for everyone. The frontend server
    forwards the
    reader's session cookie; without a session the answer is empty. Refused unless the request came
    through our own
    Nitro proxy.

    Args:
        character (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        character=character,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    character: str,
    *,
    client: AuthenticatedClient | Client,
) -> DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500 | None:
    """One kanji from the reader's own kanji dictionaries, for our own server only

     The reader's part of the kanji card: entries and frequencies from their enabled custom kanji
    dictionaries.
    Separate from the shared kanji card so that one stays cached for everyone. The frontend server
    forwards the
    reader's session cookie; without a session the answer is empty. Refused unless the request came
    through our own
    Nitro proxy.

    Args:
        character (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500
    """

    return sync_detailed(
        character=character,
        client=client,
    ).parsed


async def asyncio_detailed(
    character: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500]:
    """One kanji from the reader's own kanji dictionaries, for our own server only

     The reader's part of the kanji card: entries and frequencies from their enabled custom kanji
    dictionaries.
    Separate from the shared kanji card so that one stays cached for everyone. The frontend server
    forwards the
    reader's session cookie; without a session the answer is empty. Refused unless the request came
    through our own
    Nitro proxy.

    Args:
        character (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500]
    """

    kwargs = _get_kwargs(
        character=character,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    character: str,
    *,
    client: AuthenticatedClient | Client,
) -> DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500 | None:
    """One kanji from the reader's own kanji dictionaries, for our own server only

     The reader's part of the kanji card: entries and frequencies from their enabled custom kanji
    dictionaries.
    Separate from the shared kanji card so that one stays cached for everyone. The frontend server
    forwards the
    reader's session cookie; without a session the answer is empty. Refused unless the request came
    through our own
    Nitro proxy.

    Args:
        character (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DictionaryKanjiCustom | Error400 | Error403 | Error429 | Error500
    """

    return (
        await asyncio_detailed(
            character=character,
            client=client,
        )
    ).parsed
