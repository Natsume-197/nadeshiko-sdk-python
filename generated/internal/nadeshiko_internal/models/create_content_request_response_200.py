from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_content_request_response_200_outcome import (
    CreateContentRequestResponse200Outcome,
    check_create_content_request_response_200_outcome,
)

if TYPE_CHECKING:
    from ..models.content_request import ContentRequest


T = TypeVar("T", bound="CreateContentRequestResponse200")


@_attrs_define
class CreateContentRequestResponse200:
    """
    Attributes:
        request (ContentRequest): A reader's request for content, shared by everyone who wants the same title.
        outcome (CreateContentRequestResponse200Outcome):
    """

    request: ContentRequest
    outcome: CreateContentRequestResponse200Outcome
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        request = self.request.to_dict()

        outcome: str = self.outcome

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "request": request,
                "outcome": outcome,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.content_request import ContentRequest  # noqa: PLC0415

        _src = dict(src_dict)
        request = ContentRequest.from_dict(_src.pop("request"))

        outcome = check_create_content_request_response_200_outcome(_src.pop("outcome"))

        create_content_request_response_200 = cls(
            request=request,
            outcome=outcome,
        )

        create_content_request_response_200.additional_properties = _src
        return create_content_request_response_200

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
