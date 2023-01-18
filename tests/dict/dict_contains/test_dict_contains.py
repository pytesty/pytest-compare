from typing import Tuple, Any, Dict
from unittest.mock import Mock

import pytest

from pytest_compare.base import CompareBase
from tests.base_test import BaseTest
from tests.dict.conftest import DICT_LENGTH


class TestCompareDictContains(BaseTest):
    @pytest.mark.parametrize("actual_reverse_contains", [False, True])
    def test_reverse_args(
        self,
        method_call_test_args: Mock,
        expected_call_args: Tuple[CompareBase | Any],
        actual_reverse_contains: bool,
    ):
        method_call_test_args.assert_called_once_with(*expected_call_args)

    @pytest.mark.parametrize("actual_reverse_contains", [False, True])
    def test_reverse_kwargs(
        self,
        method_call_test_kwargs: Mock,
        expected_call_kwargs: Dict[str, CompareBase | Any],
        actual_reverse_contains: bool,
    ):
        method_call_test_kwargs.assert_called_once_with(**expected_call_kwargs)

    @pytest.mark.parametrize(
        "expected_dict_length, actual_reverse_contains",
        [(DICT_LENGTH - 1, False), (DICT_LENGTH + 1, True)],
    )
    def test_contains_correct(
        self,
        method_call_test_args: Mock,
        expected_call_args: Tuple[CompareBase | Any],
        expected_dict_length: int,
        actual_reverse_contains: bool,
    ):
        method_call_test_args.assert_called_once_with(*expected_call_args)

    @pytest.mark.parametrize(
        "expected_dict_length, actual_reverse_contains",
        [(DICT_LENGTH + 1, False), (DICT_LENGTH - 1, True)],
    )
    def test_contains_incorrect(
        self,
        method_call_test_args: Mock,
        expected_call_args: Tuple[CompareBase | Any],
        expected_dict_length: int,
        actual_reverse_contains: bool,
    ):
        with pytest.raises(AssertionError):
            method_call_test_args.assert_called_once_with(*expected_call_args)
