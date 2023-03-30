from typing import Dict, Tuple, Any

import pytest

from pytest_compare.base import CompareBase
from pytest_compare.native import CompareIn


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
def actual_call_args(substring: str, reverse: bool) -> Tuple[str, bool]:
    return substring, reverse


@pytest.fixture
def actual_call_kwargs(substring: str, reverse: bool) -> Dict[str, Any]:
    return {
        "expected": substring,
        "reverse": reverse,
    }


@pytest.fixture
def expected_call_args(string: str, reverse: bool) -> Tuple[CompareBase, bool]:
    return CompareIn(string, reverse), reverse


@pytest.fixture
def expected_call_kwargs(string: str, reverse: bool) -> Dict[str, CompareBase]:
    return {"expected": CompareIn(string, reverse), "reverse": reverse}
