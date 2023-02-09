from typing import Tuple, Any, Dict, Union
from unittest.mock import Mock

import pytest

from pytest_compare.base import CompareBase
from tests.base_test import BaseTest


class TestCompareDataFrame(BaseTest):
    @pytest.mark.parametrize(
        "expected_columns",
        [
            ["column_1", "column_2", "column_3"],
            ["column_1", "column_2"],
            ["column_1"],
            [],
        ],
    )
    def test_call_args_with_columns(
        self,
        method_call_test_args: Mock,
        expected_call_args: Tuple[Union[CompareBase, Any]],
        expected_columns,
    ):
        method_call_test_args.assert_called_once_with(*expected_call_args)

    @pytest.mark.parametrize(
        "expected_columns",
        [
            ["column_1", "column_2", "column_3"],
            ["column_1", "column_2"],
            ["column_1"],
            [],
        ],
    )
    def test_call_kwargs_with_columns(
        self,
        method_call_test_kwargs: Mock,
        expected_call_kwargs: Dict[str, Union[CompareBase, Any]],
        expected_columns,
    ):
        method_call_test_kwargs.assert_called_once_with(**expected_call_kwargs)

    @pytest.mark.parametrize(
        "expected_columns", [["column_1", "column_2", "column_3", "not_in_df"]]
    )
    def test_call_args_unidentified_column(
        self,
        method_call_test_args: Mock,
        expected_call_args: Tuple[Union[CompareBase, Any]],
        expected_columns,
    ):
        with pytest.raises(KeyError):
            method_call_test_args.assert_called_once_with(*expected_call_args)

    @pytest.mark.parametrize(
        "expected_columns", [["column_1", "column_2", "column_3", "not_in_df"]]
    )
    def test_call_kwargs_unidentified_column(
        self,
        method_call_test_kwargs: Mock,
        expected_call_kwargs: Dict[str, Union[CompareBase, Any]],
        expected_columns,
    ):
        with pytest.raises(KeyError):
            method_call_test_kwargs.assert_called_once_with(**expected_call_kwargs)
