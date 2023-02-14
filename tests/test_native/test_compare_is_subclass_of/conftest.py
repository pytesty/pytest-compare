from typing import Dict, Tuple

import pytest

from pytest_compare.base import CompareBase
from pytest_compare.native import CompareIsInstanceOf


class ParentClass:
    pass


class ChildClass(ParentClass):
    pass


@pytest.fixture
def mock_test_class() -> ChildClass:
    return ChildClass()


@pytest.fixture
def actual_call_args(mock_test_class: ChildClass) -> Tuple[ChildClass]:
    return (mock_test_class,)


@pytest.fixture
def actual_call_kwargs(mock_test_class: ChildClass) -> Dict[str, ChildClass]:
    return {
        "expected": mock_test_class,
    }


@pytest.fixture
def expected_call_args() -> Tuple[CompareBase]:
    return (CompareIsInstanceOf(ParentClass),)


@pytest.fixture
def expected_call_kwargs() -> Dict[str, CompareBase]:
    return {"expected": CompareIsInstanceOf(ParentClass)}
