from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_dictionary_status import UserDictionaryStatus, check_user_dictionary_status

T = TypeVar("T", bound="UserDictionary")


@_attrs_define
class UserDictionary:
    """One custom Yomitan dictionary attached to the user's account.

    Attributes:
        id (int):
        stack_id (str):  Example: custom:42.
        title (str):
        revision (str):
        author (None | str):
        description (None | str):
        url (None | str):
        frequency_mode (None | str):
        has_terms (bool):
        has_frequency (bool):
        has_pitch (bool):
        term_count (int):
        frequency_count (int):
        pitch_count (int):
        zip_bytes (int):
        sqlite_bytes (int):
        status (UserDictionaryStatus):
        error_message (None | str):
        enabled (bool):
        sort_order (int):
        created_at (datetime.datetime):
        progress (int | None): How far a running import got, 0-100; null when it is queued, ready or failed.
        queue_position (int | None): Place in the import queue while waiting to start (1 = next); null once it runs or
            is done.
    """

    id: int
    stack_id: str
    title: str
    revision: str
    author: None | str
    description: None | str
    url: None | str
    frequency_mode: None | str
    has_terms: bool
    has_frequency: bool
    has_pitch: bool
    term_count: int
    frequency_count: int
    pitch_count: int
    zip_bytes: int
    sqlite_bytes: int
    status: UserDictionaryStatus
    error_message: None | str
    enabled: bool
    sort_order: int
    created_at: datetime.datetime
    progress: int | None
    queue_position: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        stack_id = self.stack_id

        title = self.title

        revision = self.revision

        author: None | str
        author = self.author

        description: None | str
        description = self.description

        url: None | str
        url = self.url

        frequency_mode: None | str
        frequency_mode = self.frequency_mode

        has_terms = self.has_terms

        has_frequency = self.has_frequency

        has_pitch = self.has_pitch

        term_count = self.term_count

        frequency_count = self.frequency_count

        pitch_count = self.pitch_count

        zip_bytes = self.zip_bytes

        sqlite_bytes = self.sqlite_bytes

        status: str = self.status

        error_message: None | str
        error_message = self.error_message

        enabled = self.enabled

        sort_order = self.sort_order

        created_at = self.created_at.isoformat()

        progress: int | None
        progress = self.progress

        queue_position: int | None
        queue_position = self.queue_position

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "stackId": stack_id,
                "title": title,
                "revision": revision,
                "author": author,
                "description": description,
                "url": url,
                "frequencyMode": frequency_mode,
                "hasTerms": has_terms,
                "hasFrequency": has_frequency,
                "hasPitch": has_pitch,
                "termCount": term_count,
                "frequencyCount": frequency_count,
                "pitchCount": pitch_count,
                "zipBytes": zip_bytes,
                "sqliteBytes": sqlite_bytes,
                "status": status,
                "errorMessage": error_message,
                "enabled": enabled,
                "sortOrder": sort_order,
                "createdAt": created_at,
                "progress": progress,
                "queuePosition": queue_position,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = _src.pop("id")

        stack_id = _src.pop("stackId")

        title = _src.pop("title")

        revision = _src.pop("revision")

        def _parse_author(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        author = _parse_author(_src.pop("author"))

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(_src.pop("description"))

        def _parse_url(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        url = _parse_url(_src.pop("url"))

        def _parse_frequency_mode(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        frequency_mode = _parse_frequency_mode(_src.pop("frequencyMode"))

        has_terms = _src.pop("hasTerms")

        has_frequency = _src.pop("hasFrequency")

        has_pitch = _src.pop("hasPitch")

        term_count = _src.pop("termCount")

        frequency_count = _src.pop("frequencyCount")

        pitch_count = _src.pop("pitchCount")

        zip_bytes = _src.pop("zipBytes")

        sqlite_bytes = _src.pop("sqliteBytes")

        status = check_user_dictionary_status(_src.pop("status"))

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(_src.pop("errorMessage"))

        enabled = _src.pop("enabled")

        sort_order = _src.pop("sortOrder")

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        def _parse_progress(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        progress = _parse_progress(_src.pop("progress"))

        def _parse_queue_position(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        queue_position = _parse_queue_position(_src.pop("queuePosition"))

        user_dictionary = cls(
            id=id,
            stack_id=stack_id,
            title=title,
            revision=revision,
            author=author,
            description=description,
            url=url,
            frequency_mode=frequency_mode,
            has_terms=has_terms,
            has_frequency=has_frequency,
            has_pitch=has_pitch,
            term_count=term_count,
            frequency_count=frequency_count,
            pitch_count=pitch_count,
            zip_bytes=zip_bytes,
            sqlite_bytes=sqlite_bytes,
            status=status,
            error_message=error_message,
            enabled=enabled,
            sort_order=sort_order,
            created_at=created_at,
            progress=progress,
            queue_position=queue_position,
        )

        user_dictionary.additional_properties = _src
        return user_dictionary

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
