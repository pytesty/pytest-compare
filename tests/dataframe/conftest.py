from typing import List, Tuple, Dict, Any

import pandas as pd
import pytest

from pytest_compare.base import CompareBase
from pytest_compare.dataframe import CompareDataFrame


def create_dataframe(columns: List[str], rows_n: int = 10) -> pd.DataFrame:
    """Create a dataframe with the given columns."""
    return pd.DataFrame({column: [n for n in range(rows_n)] for column in columns})


@pytest.fixture
def actual_df_columns() -> List[str]:
    return ["column_1", "column_2", "column_3"]


@pytest.fixture
def expected_df_columns() -> List[str] | None:
    return None


@pytest.fixture
def df(actual_df_columns: List[str]) -> pd.DataFrame:
    return create_dataframe(actual_df_columns)


@pytest.fixture
def expected_call_args(
    df: pd.DataFrame, expected_df_columns: List[str], actual_df_columns: List[str]
) -> Tuple[CompareBase | Any]:
    return CompareDataFrame(df, expected_df_columns), actual_df_columns


@pytest.fixture
def expected_call_kwargs(
    df: pd.DataFrame, expected_df_columns: List[str], actual_df_columns: List[str]
) -> Dict[str, CompareBase | Any]:
    return {
        "dataframe": CompareDataFrame(df, expected_df_columns),
        "columns": actual_df_columns,
    }


@pytest.fixture
def actual_call_args(
    df: pd.DataFrame, actual_df_columns: List[str]
) -> Tuple[pd.DataFrame]:
    return df, actual_df_columns


@pytest.fixture
def actual_call_kwargs(
    df: pd.DataFrame, actual_df_columns: List[str]
) -> Dict[str, pd.DataFrame]:
    return {"dataframe": df, "columns": actual_df_columns}
