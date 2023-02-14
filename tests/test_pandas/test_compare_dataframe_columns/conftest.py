from typing import List, Tuple, Dict, Optional

import pandas as pd
import pytest

from pytest_compare.base import CompareBase
from pytest_compare.pandas import CompareDataFrameColumns
from tests.test_pandas.conftest import create_dataframe


@pytest.fixture
def actual_columns() -> List[str]:
    return ["column_1", "column_2", "column_3"]


@pytest.fixture
def df(actual_columns: List[str]) -> pd.DataFrame:
    return create_dataframe(actual_columns)


@pytest.fixture
def expected_call_args(df: pd.DataFrame) -> Tuple[CompareBase]:
    return (CompareDataFrameColumns(df),)


@pytest.fixture
def expected_call_kwargs(df: pd.DataFrame) -> Dict[str, CompareBase]:
    return {
        "expected": CompareDataFrameColumns(df),
    }


@pytest.fixture
def actual_call_args(df: pd.DataFrame) -> Tuple[pd.DataFrame]:
    return (df,)


@pytest.fixture
def actual_call_kwargs(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    return {"expected": df}
