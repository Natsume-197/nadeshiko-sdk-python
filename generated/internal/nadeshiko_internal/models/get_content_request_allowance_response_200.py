from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_content_request_allowance_response_200_boosts import (
        GetContentRequestAllowanceResponse200Boosts,
    )


T = TypeVar("T", bound="GetContentRequestAllowanceResponse200")


@_attrs_define
class GetContentRequestAllowanceResponse200:
    """
    Attributes:
        is_patron (bool):
        open_count (int):
        open_limit (int | None): Null for admins (no limit).
        own_count (int): Total requests filed by this reader across all statuses.
        voted_count (int): Total requests this reader voted for or boosted across all statuses.
        boosts (GetContentRequestAllowanceResponse200Boosts):
        voted_ids (list[UUID]):
        boosted_ids (list[UUID]):
        own_ids (list[UUID]): Active requests this reader filed.
    """

    is_patron: bool
    open_count: int
    open_limit: int | None
    own_count: int
    voted_count: int
    boosts: GetContentRequestAllowanceResponse200Boosts
    voted_ids: list[UUID]
    boosted_ids: list[UUID]
    own_ids: list[UUID]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_patron = self.is_patron

        open_count = self.open_count

        open_limit: int | None
        open_limit = self.open_limit

        own_count = self.own_count

        voted_count = self.voted_count

        boosts = self.boosts.to_dict()

        voted_ids = []
        for voted_ids_item_data in self.voted_ids:
            voted_ids_item = str(voted_ids_item_data)
            voted_ids.append(voted_ids_item)

        boosted_ids = []
        for boosted_ids_item_data in self.boosted_ids:
            boosted_ids_item = str(boosted_ids_item_data)
            boosted_ids.append(boosted_ids_item)

        own_ids = []
        for own_ids_item_data in self.own_ids:
            own_ids_item = str(own_ids_item_data)
            own_ids.append(own_ids_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "isPatron": is_patron,
                "openCount": open_count,
                "openLimit": open_limit,
                "ownCount": own_count,
                "votedCount": voted_count,
                "boosts": boosts,
                "votedIds": voted_ids,
                "boostedIds": boosted_ids,
                "ownIds": own_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_content_request_allowance_response_200_boosts import (
            GetContentRequestAllowanceResponse200Boosts,  # noqa: PLC0415
        )

        _src = dict(src_dict)
        is_patron = _src.pop("isPatron")

        open_count = _src.pop("openCount")

        def _parse_open_limit(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        open_limit = _parse_open_limit(_src.pop("openLimit"))

        own_count = _src.pop("ownCount")

        voted_count = _src.pop("votedCount")

        boosts = GetContentRequestAllowanceResponse200Boosts.from_dict(_src.pop("boosts"))

        voted_ids = []
        _voted_ids = _src.pop("votedIds")
        for voted_ids_item_data in _voted_ids:
            voted_ids_item = UUID(voted_ids_item_data)

            voted_ids.append(voted_ids_item)

        boosted_ids = []
        _boosted_ids = _src.pop("boostedIds")
        for boosted_ids_item_data in _boosted_ids:
            boosted_ids_item = UUID(boosted_ids_item_data)

            boosted_ids.append(boosted_ids_item)

        own_ids = []
        _own_ids = _src.pop("ownIds")
        for own_ids_item_data in _own_ids:
            own_ids_item = UUID(own_ids_item_data)

            own_ids.append(own_ids_item)

        get_content_request_allowance_response_200 = cls(
            is_patron=is_patron,
            open_count=open_count,
            open_limit=open_limit,
            own_count=own_count,
            voted_count=voted_count,
            boosts=boosts,
            voted_ids=voted_ids,
            boosted_ids=boosted_ids,
            own_ids=own_ids,
        )

        get_content_request_allowance_response_200.additional_properties = _src
        return get_content_request_allowance_response_200

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
