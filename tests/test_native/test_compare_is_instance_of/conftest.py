from typing import Dict, Tuple

import pytest

from pytest_compare.base import CompareBase
from pytest_compare.native import CompareIsInstanceOf


class TestClass:
    pass


@pytest.fixture
def mock_test_class() -> TestClass:
    return TestClass()


@pytest.fixture
def actual_call_args(mock_test_class: TestClass) -> Tuple[TestClass]:
    return (mock_test_class,)


@pytest.fixture
def actual_call_kwargs(mock_test_class: TestClass) -> Dict[str, TestClass]:
    return {
        "expected": mock_test_class,
    }


@pytest.fixture
def expected_call_args() -> Tuple[CompareBase]:
    return (CompareIsInstanceOf(TestClass),)


@pytest.fixture
def expected_call_kwargs() -> Dict[str, CompareBase]:
    return {"expected": CompareIsInstanceOf(TestClass)}
