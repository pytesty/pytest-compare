from abc import ABC
from typing import Optional, List

import pandas as pd

from pytest_compare.base import CompareBase


class CompareDataFrameBase(CompareBase, ABC):
    def __init__(self, expected: pd.DataFrame):
        """Initialize the class.

        Args:
            expected (pd.DataFrame): First dataframe.
        """
        if not isinstance(expected, pd.DataFrame):
            raise TypeError(
                f"Dataframe must be a pandas DataFrame, not {type(expected)}"
            )

        self._expected = expected


class CompareDataFrame(CompareDataFrameBase):
    """Compare two dataframes"""

    def __init__(self, expected: pd.DataFrame, columns: Optional[List[str]] = None):
        """Initialize the class.

        Args:
            expected (pd.DataFrame): Dataframe to compare.
            columns (Optional[List[str]], optional): Columns to compare. If None, all columns are compared. Defaults to None.
        """
        if columns and not isinstance(columns, list):
            raise TypeError(f"Columns must be a list, not {type(columns)}")

        super().__init__(expected)
        self._columns = columns

    def compare(self, actual) -> bool:
        """Compare two dataframes.

        Args:
            actual (pd.DataFrame): Dataframe to compare.

        Returns:
            bool: True if the first dictionary is a subset of the second
                dictionary, False otherwise.
        """
        if not isinstance(actual, pd.DataFrame):
            return False

        if not self._columns:
            return actual.equals(self._expected)
        else:
            return actual[self._columns].equals(self._expected[self._columns])
