from typing import List, Tuple, Dict

import pandas as pd
import pytest

from pytest_compare.base import CompareBase
from pytest_compare.pandas.pandas import CompareSeries


def create_series(columns: List[str], rows_n: int = 10) -> pd.Series:
    """Create a dataframe with the given columns."""
    return pd.Series({column: [n for n in range(rows_n)] for column in columns})


@pytest.fixture
def actual_columns() -> List[str]:
    return ["column_1", "column_2", "column_3"]


@pytest.fixture
def series(actual_columns: List[str]) -> pd.Series:
    return create_series(actual_columns)


@pytest.fixture
def expected_call_args(series: pd.Series) -> Tuple[CompareBase]:
    return (CompareSeries(series),)


@pytest.fixture
def expected_call_kwargs(series, actual_columns: List[str]) -> Dict[str, CompareBase]:
    return {
        "expected": CompareSeries(series),
    }


@pytest.fixture
def actual_call_args(series: pd.Series) -> Tuple[pd.Series]:
    return (series,)


@pytest.fixture
def actual_call_kwargs(series: pd.Series) -> Dict[str, pd.Series]:
    return {"expected": series}
