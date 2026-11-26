from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.word_watch_match_mode import WordWatchMatchMode, check_word_watch_match_mode
from ..models.word_watch_mode import WordWatchMode, check_word_watch_mode
from ..models.word_watch_status import WordWatchStatus, check_word_watch_status

T = TypeVar("T", bound="WordWatch")


@_attrs_define
class WordWatch:
    """One of the reader's word alerts.

    Attributes:
        id (UUID):
        query (str): The watched word, NFKC-normalised.
        match_mode (WordWatchMatchMode):
        mode (WordWatchMode): `FIRST`: one notice when the word starts returning sentences, then the
            alert is `FULFILLED`. `NEW_SENTENCES`: a weekly digest of new sentences.
        status (WordWatchStatus):
        last_notified_at (datetime.datetime | None):
        created_at (datetime.datetime):
    """

    id: UUID
    query: str
    match_mode: WordWatchMatchMode
    mode: WordWatchMode
    status: WordWatchStatus
    last_notified_at: datetime.datetime | None
    created_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        query = self.query

        match_mode: str = self.match_mode

        mode: str = self.mode

        status: str = self.status

        last_notified_at: None | str
        if isinstance(self.last_notified_at, datetime.datetime):
            last_notified_at = self.last_notified_at.isoformat()
        else:
            last_notified_at = self.last_notified_at

        created_at = self.created_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "query": query,
                "matchMode": match_mode,
                "mode": mode,
                "status": status,
                "lastNotifiedAt": last_notified_at,
                "createdAt": created_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        id = UUID(_src.pop("id"))

        query = _src.pop("query")

        match_mode = check_word_watch_match_mode(_src.pop("matchMode"))

        mode = check_word_watch_mode(_src.pop("mode"))

        status = check_word_watch_status(_src.pop("status"))

        def _parse_last_notified_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_notified_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_notified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_notified_at = _parse_last_notified_at(_src.pop("lastNotifiedAt"))

        created_at = datetime.datetime.fromisoformat(_src.pop("createdAt"))

        word_watch = cls(
            id=id,
            query=query,
            match_mode=match_mode,
            mode=mode,
            status=status,
            last_notified_at=last_notified_at,
            created_at=created_at,
        )

        word_watch.additional_properties = _src
        return word_watch

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
