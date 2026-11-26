from typing import Literal

SearchQueryMatchMode = Literal["CONTAINS", "EXACT", "WORD"]

SEARCH_QUERY_MATCH_MODE_VALUES: set[SearchQueryMatchMode] = {
    "CONTAINS",
    "EXACT",
    "WORD",
}


def check_search_query_match_mode(value: str) -> SearchQueryMatchMode:
    if value in SEARCH_QUERY_MATCH_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_QUERY_MATCH_MODE_VALUES!r}"
    )
