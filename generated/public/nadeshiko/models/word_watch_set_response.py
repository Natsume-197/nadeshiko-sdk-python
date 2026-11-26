from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.word_watch_set_response_outcome import (
    WordWatchSetResponseOutcome,
    check_word_watch_set_response_outcome,
)

if TYPE_CHECKING:
    from ..models.word_watch import WordWatch


T = TypeVar("T", bound="WordWatchSetResponse")


@_attrs_define
class WordWatchSetResponse:
    """
    Attributes:
        watch (WordWatch): One of the reader's word alerts.
        outcome (WordWatchSetResponseOutcome):
        sentence_count (int): Sentences the word has in the reader's own search right now.
        common_word (bool): A new-sentences alert on a word so common that the weekly digest will bring a lot; the site
            warns.
    """

    watch: WordWatch
    outcome: WordWatchSetResponseOutcome
    sentence_count: int
    common_word: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        watch = self.watch.to_dict()

        outcome: str = self.outcome

        sentence_count = self.sentence_count

        common_word = self.common_word

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "watch": watch,
                "outcome": outcome,
                "sentenceCount": sentence_count,
                "commonWord": common_word,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.word_watch import WordWatch  # noqa: PLC0415

        _src = dict(src_dict)
        watch = WordWatch.from_dict(_src.pop("watch"))

        outcome = check_word_watch_set_response_outcome(_src.pop("outcome"))

        sentence_count = _src.pop("sentenceCount")

        common_word = _src.pop("commonWord")

        word_watch_set_response = cls(
            watch=watch,
            outcome=outcome,
            sentence_count=sentence_count,
            common_word=common_word,
        )

        word_watch_set_response.additional_properties = _src
        return word_watch_set_response

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
