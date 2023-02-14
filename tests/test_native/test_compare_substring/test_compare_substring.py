from unittest.mock import Mock

import pytest

from pytest_compare.native import CompareSubString
from tests.base_test import BaseTest


class TestCompareSubstring(BaseTest):
    @pytest.mark.parametrize(
        "string, substring, reverse",
        [("mock_string", "string", False), ("mock", "mock_string", True)],
    )
    def test_compare_substring(
        self, method_call_test_args: Mock, string: str, substring: str, reverse: bool
    ):
        method_call_test_args.assert_called_once_with(
            CompareSubString(substring, reverse), reverse
        )
