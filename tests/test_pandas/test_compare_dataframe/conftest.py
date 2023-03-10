from typing import List, Tuple, Dict, Any, Optional, Union

import pandas as pd
import pytest

from pytest_compare.base import CompareBase
from pytest_compare.pandas import CompareDataFrame
from tests.test_pandas.conftest import create_dataframe


@pytest.fixture
def actual_columns() -> List[str]:
    return ["column_1", "column_2", "column_3"]


@pytest.fixture
def expected_columns() -> Optional[List[str]]:
    return None


@pytest.fixture
def df(actual_columns: List[str]) -> pd.DataFrame:
    return create_dataframe(actual_columns)


@pytest.fixture
def expected_call_args(
    df: pd.DataFrame, expected_columns: List[str], actual_columns: List[str]
) -> Tuple[CompareBase, List]:
    return CompareDataFrame(df, expected_columns), actual_columns


@pytest.fixture
def expected_call_kwargs(
    df: pd.DataFrame, expected_columns: List[str], actual_columns: List[str]
) -> Dict[str, Union[CompareBase, Any]]:
    return {
        "expected": CompareDataFrame(df, expected_columns),
        "columns": actual_columns,
    }


@pytest.fixture
def actual_call_args(
    df: pd.DataFrame, actual_columns: List[str]
) -> Tuple[pd.DataFrame, List]:
    return df, actual_columns


@pytest.fixture
def actual_call_kwargs(
    df: pd.DataFrame, actual_columns: List[str]
) -> Dict[str, pd.DataFrame]:
    return {"expected": df, "columns": actual_columns}
