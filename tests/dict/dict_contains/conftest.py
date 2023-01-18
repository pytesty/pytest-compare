from typing import Tuple, Dict, Optional

import pytest

from pytest_compare.base import CompareBase
from pytest_compare.dict import CompareDictContains


@pytest.fixture
def actual_reverse_contains() -> Optional[bool]:
    return None


@pytest.fixture
def actual_call_args(actual_dict: dict, actual_reverse_contains: bool) -> Tuple[dict]:
    return (actual_dict,)


@pytest.fixture
def actual_call_kwargs(
    actual_dict: dict, actual_reverse_contains: bool
) -> Dict[str, dict]:
    return {"expected": actual_dict, "reverse_contains": actual_reverse_contains}


@pytest.fixture
def expected_reverse_contains(actual_reverse_contains: bool) -> Optional[bool]:
    return actual_reverse_contains


@pytest.fixture
def expected_call_args(
    expected_dict: dict, expected_reverse_contains: bool, actual_reverse_contains: bool
) -> Tuple[CompareBase, Optional[bool]]:
    compare_method = (
        CompareDictContains(expected_dict, actual_reverse_contains)
        if expected_reverse_contains
        else CompareDictContains(expected_dict)
    )
    if expected_reverse_contains:
        return compare_method, expected_reverse_contains
    else:
        return (compare_method,)


@pytest.fixture
def expected_call_kwargs(
    expected_dict: dict, expected_reverse_contains: bool, actual_reverse_contains: bool
) -> Dict[str, CompareBase | bool]:
    return {
        "expected": CompareDictContains(expected_dict, actual_reverse_contains),
        "reverse_contains": expected_reverse_contains,
    }
