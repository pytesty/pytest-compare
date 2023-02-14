from typing import Dict, Tuple, Any

import pytest

from pytest_compare.base import CompareBase
from pytest_compare.native import CompareSubString


@pytest.fixture
def string() -> str:
    return "mock_string"


@pytest.fixture
def substring(string) -> str:
    return string[1:]


@pytest.fixture
def reverse() -> bool:
    return False


@pytest.fixture
def actual_call_args(string, reverse: bool) -> Tuple[str, bool]:
    return string, reverse


@pytest.fixture
def actual_call_kwargs(string, reverse: bool) -> Dict[str, Any]:
    return {
        "expected": string,
        "reverse": reverse,
    }


@pytest.fixture
def expected_call_args(substring: str, reverse: bool) -> Tuple[CompareBase, bool]:
    return CompareSubString(substring, reverse), reverse


@pytest.fixture
def expected_call_kwargs(substring: str, reverse: bool) -> Dict[str, CompareBase]:
    return {"expected": CompareSubString(substring, reverse), "reverse": reverse}
