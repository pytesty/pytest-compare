from typing import Tuple, Dict

import pytest

from pytest_compare.base import CompareBase
from pytest_compare.dict import CompareDictKeys


@pytest.fixture
def actual_call_args(actual_dict: dict) -> Tuple[dict]:
    return (actual_dict,)


@pytest.fixture
def actual_call_kwargs(actual_dict: dict) -> Dict[str, dict]:
    return {"expected": actual_dict}


@pytest.fixture
def expected_call_args(expected_dict: dict) -> Tuple[CompareBase]:
    return (CompareDictKeys(expected_dict),)


@pytest.fixture
def expected_call_kwargs(expected_dict: dict) -> Dict[str, CompareBase]:
    return {
        "expected": CompareDictKeys(expected_dict),
    }
