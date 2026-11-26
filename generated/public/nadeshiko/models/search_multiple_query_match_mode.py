from typing import Literal

SearchMultipleQueryMatchMode = Literal["CONTAINS", "EXACT", "WORD"]

SEARCH_MULTIPLE_QUERY_MATCH_MODE_VALUES: set[SearchMultipleQueryMatchMode] = {
    "CONTAINS",
    "EXACT",
    "WORD",
}


def check_search_multiple_query_match_mode(value: str) -> SearchMultipleQueryMatchMode:
    if value in SEARCH_MULTIPLE_QUERY_MATCH_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SEARCH_MULTIPLE_QUERY_MATCH_MODE_VALUES!r}"
    )
