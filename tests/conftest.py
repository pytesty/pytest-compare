from typing import Any, Tuple, Dict
from unittest.mock import Mock

import pytest

from pytest_compare.base import CompareBase


@pytest.fixture
def actual_call_args() -> Tuple[Any]:
    raise NotImplementedError("`actual_call_args` must be implemented")


@pytest.fixture
def actual_call_kwargs() -> Dict[str, Any]:
    raise NotImplementedError("`actual_call_kwargs` must be implemented")


@pytest.fixture
def expected_call_args() -> Tuple[Any]:
    raise NotImplementedError("`expected_call_args` must be implemented")


@pytest.fixture
def expected_call_kwargs() -> Dict[str, CompareBase]:
    raise NotImplementedError("`expected_call_kwargs` must be implemented")


@pytest.fixture
def method_call_test_args(actual_call_args: Tuple[Any]) -> Mock:
    mock = Mock()
    mock(*actual_call_args)

    return mock


@pytest.fixture
def method_call_test_kwargs(actual_call_kwargs: Dict[str, Any]) -> Mock:
    mock = Mock()
    mock(**actual_call_kwargs)

    return mock
