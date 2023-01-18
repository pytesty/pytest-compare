from typing import Tuple
from unittest.mock import Mock

import pytest

from pytest_compare.base import CompareBase
from tests.base_test import BaseTest


class TestCompareDictKeys(BaseTest):
    @pytest.mark.parametrize("expected_dict_length", [0, 9, 11])
    def test_dict_different_lengths_args(
        self,
        method_call_test_args: Mock,
        expected_call_args: Tuple[CompareBase],
        expected_dict_length: int,
    ):
        with pytest.raises(AssertionError):
            method_call_test_args.assert_called_once_with(*expected_call_args)

    @pytest.mark.parametrize("expected_dict_length", [0, 9, 11])
    def test_dict_different_lengths_kwargs(
        self,
        method_call_test_kwargs: Mock,
        expected_call_args: Tuple[CompareBase],
        expected_dict_length: int,
    ):
        with pytest.raises(AssertionError):
            method_call_test_kwargs.assert_called_once_with(*expected_call_args)

    @pytest.mark.parametrize("expected_entries_format", ["incorrect_{}"])
    def test_dict_different_formats_args(
        self,
        method_call_test_args: Mock,
        expected_call_args: Tuple[CompareBase],
        expected_entries_format: str,
    ):
        with pytest.raises(AssertionError):
            method_call_test_args.assert_called_once_with(*expected_call_args)

    @pytest.mark.parametrize("expected_entries_format", ["incorrect_{}"])
    def test_dict_different_formats_kwargs(
        self,
        method_call_test_kwargs: Mock,
        expected_call_args: Tuple[CompareBase],
        expected_entries_format: str,
    ):
        with pytest.raises(AssertionError):
            method_call_test_kwargs.assert_called_once_with(*expected_call_args)
