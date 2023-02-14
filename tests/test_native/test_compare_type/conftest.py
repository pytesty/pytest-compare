from typing import Dict, Tuple, Any

import pytest

from pytest_compare.base import CompareBase
from pytest_compare.native import CompareType


class TestClass:
    pass


@pytest.fixture
def actual_call_args() -> Tuple[Any]:
    return (TestClass(),)


@pytest.fixture
def actual_call_kwargs() -> Dict[str, Any]:
    return {"expected": TestClass()}


@pytest.fixture
def expected_call_args() -> Tuple[Any]:
    return (CompareType(TestClass),)


@pytest.fixture
def expected_call_kwargs() -> Dict[str, CompareBase]:
    return {"expected": CompareType(TestClass)}
