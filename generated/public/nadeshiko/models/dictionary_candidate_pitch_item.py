from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DictionaryCandidatePitchItem")


@_attrs_define
class DictionaryCandidatePitchItem:
    """
    Attributes:
        downstep (int): 0 is flat (heiban); n is the mora after which the pitch drops.
        audio_url (str | Unset): A recording of the reading with this accent (Opus in Ogg), when one exists. Synthesised
            with
            VOICEVOX:四国めたん; absent for words outside the most frequent ones.
             Example: https://cdn.nadeshiko.co/pitch-audio/metan-v1/%E3%81%AF%E3%81%97_2.opus.
        source (str | Unset): Custom pitch dictionary title when sourced from a user upload.
        nasal (list[int] | Unset):
        devoice (list[int] | Unset):
        tags (list[str] | Unset):
    """

    downstep: int
    audio_url: str | Unset = UNSET
    source: str | Unset = UNSET
    nasal: list[int] | Unset = UNSET
    devoice: list[int] | Unset = UNSET
    tags: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        downstep = self.downstep

        audio_url = self.audio_url

        source = self.source

        nasal: list[int] | Unset = UNSET
        if not isinstance(self.nasal, Unset):
            nasal = self.nasal

        devoice: list[int] | Unset = UNSET
        if not isinstance(self.devoice, Unset):
            devoice = self.devoice

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "downstep": downstep,
            }
        )
        if audio_url is not UNSET:
            field_dict["audioUrl"] = audio_url
        if source is not UNSET:
            field_dict["source"] = source
        if nasal is not UNSET:
            field_dict["nasal"] = nasal
        if devoice is not UNSET:
            field_dict["devoice"] = devoice
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        _src = dict(src_dict)
        downstep = _src.pop("downstep")

        audio_url = _src.pop("audioUrl", UNSET)

        source = _src.pop("source", UNSET)

        nasal = cast(list[int], _src.pop("nasal", UNSET))

        devoice = cast(list[int], _src.pop("devoice", UNSET))

        tags = cast(list[str], _src.pop("tags", UNSET))

        dictionary_candidate_pitch_item = cls(
            downstep=downstep,
            audio_url=audio_url,
            source=source,
            nasal=nasal,
            devoice=devoice,
            tags=tags,
        )

        dictionary_candidate_pitch_item.additional_properties = _src
        return dictionary_candidate_pitch_item

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
