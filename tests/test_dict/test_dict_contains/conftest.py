from typing import Dict, Optional, Union, Tuple

import pytest

from pytest_compare.base import CompareBase
from pytest_compare.dict import CompareDictContains


@pytest.fixture
def actual_reverse_contains() -> Optional[bool]:
    return None


@pytest.fixture
def actual_call_args(
    actual_dict: dict, actual_reverse_contains: Optional[bool]
) -> Union[Tuple[dict], Tuple[dict, bool]]:
    if actual_reverse_contains is None:
        return (actual_dict,)
    else:
        return actual_dict, actual_reverse_contains


@pytest.fixture
def actual_call_kwargs(
    actual_dict: dict, actual_reverse_contains: bool
) -> Dict[str, Union[Dict, bool]]:
    return {"expected": actual_dict, "reverse_contains": actual_reverse_contains}


@pytest.fixture
def expected_reverse_contains(actual_reverse_contains: bool) -> Optional[bool]:
    return actual_reverse_contains


@pytest.fixture
def expected_call_args(
    expected_dict: dict, expected_reverse_contains: bool, actual_reverse_contains: bool
) -> Union[Tuple[CompareDictContains, bool], Tuple[CompareDictContains]]:
    compare_method = (
        CompareDictContains(expected_dict, actual_reverse_contains)
        if expected_reverse_contains
        else CompareDictContains(expected_dict)
    )
    if expected_reverse_contains is None:
        return (compare_method,)
    else:
        return compare_method, expected_reverse_contains


@pytest.fixture
def expected_call_kwargs(
    expected_dict: dict,
    expected_reverse_contains: bool,
    actual_reverse_contains: Optional[bool],
) -> Dict[str, Union[CompareBase, bool]]:
    expected = (
        CompareDictContains(expected_dict, actual_reverse_contains)
        if actual_reverse_contains is not None
        else CompareDictContains(expected_dict)
    )

    return {
        "expected": expected,
        "reverse_contains": expected_reverse_contains,
    }
