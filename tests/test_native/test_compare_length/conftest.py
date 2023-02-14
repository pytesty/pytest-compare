from typing import Dict, Tuple, Any, List

import pytest

from pytest_compare.base import CompareBase
from pytest_compare.native import CompareLength


@pytest.fixture
def mock_len() -> int:
    return 10


@pytest.fixture
def mock_list(mock_len: int) -> List[int]:
    return [n for n in range(mock_len)]


@pytest.fixture
def actual_call_args(mock_list: List[int]) -> Tuple[List[int]]:
    return (mock_list,)


@pytest.fixture
def actual_call_kwargs(mock_list: List[int]) -> Dict[str, Any]:
    return {
        "expected": mock_list,
    }


@pytest.fixture
def expected_call_args(mock_len: int) -> Tuple[CompareBase]:
    return (CompareLength(mock_len),)


@pytest.fixture
def expected_call_kwargs(mock_len: int) -> Dict[str, CompareBase]:
    return {"expected": CompareLength(mock_len)}
