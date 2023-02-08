from typing import Tuple, Any, Dict, Union
from unittest.mock import Mock

from pytest_compare.base import CompareBase


class BaseTest:
    def test_call_args(
        self, method_call_test_args: Mock, expected_call_args: Tuple[Union[CompareBase, Any]]
    ):
        method_call_test_args.assert_called_once_with(*expected_call_args)

    def test_call_kwargs(
        self,
        method_call_test_kwargs: Mock,
        expected_call_kwargs: Dict[str, Union[CompareBase, Any]],
    ):
        method_call_test_kwargs.assert_called_once_with(**expected_call_kwargs)
