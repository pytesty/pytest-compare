from abc import ABC
from typing import Optional, List, Union

import pandas as pd

from pytest_compare.base import CompareBase


class CompareDataFrameBase(CompareBase, ABC):
    EXPECTED_TYPE = Union[pd.DataFrame, pd.Series]
    ACTUAL_TYPE = Union[pd.DataFrame, pd.Series]


class CompareDataFrame(CompareDataFrameBase):
    """Compare two dataframes"""

    EXPECTED_TYPE = pd.DataFrame
    ACTUAL_TYPE = pd.DataFrame

    def __init__(self, expected: pd.DataFrame, columns: Optional[List[str]] = None):
        """Initialize the class.

        Args:
            expected (pd.DataFrame): Dataframe to compare.
            columns (Optional[List[str]], optional): Columns to compare. If None, all columns are compared. Defaults to None.
        """
        super().__init__(expected)

        if columns and not isinstance(columns, list):
            raise TypeError(f"Columns must be a list, not {type(columns)}")
        if columns and not all(isinstance(column, str) for column in columns):
            raise TypeError(f"Columns must be a list of strings")

        self._columns = columns

    def compare(self, actual: pd.DataFrame) -> bool:
        """Compare two dataframes.

        Args:
            actual (pd.DataFrame): Dataframe to compare.

        Returns:
            bool: True if the first dictionary is a subset of the second
                dictionary, False otherwise.
        """
        if not self._columns:
            return actual.equals(self.expected)
        else:
            return actual[self._columns].equals(self.expected[self._columns])


class CompareDataFrameColumns(CompareDataFrameBase):
    """Compare two dataframe columns"""

    EXPECTED_TYPE = pd.DataFrame
    ACTUAL_TYPE = pd.DataFrame

    def compare(self, actual: pd.DataFrame) -> bool:
        """Compare two dataframe columns.

        Args:
            actual (pd.DataFrame): Dataframe to compare.

        Returns:
            bool: True if columns are identical, False otherwise.
        """
        return actual.columns.equals(self.expected.columns)


class CompareSeries(CompareDataFrameBase):
    """Compare two series"""

    EXPECTED_TYPE = pd.Series
    ACTUAL_TYPE = pd.Series

    def compare(self, actual: pd.Series) -> bool:
        """Compare two series.

        Args:
            actual (pd.Series): Series to compare.

        Returns:
            bool: True if the first dictionary is a subset of the second
                dictionary, False otherwise.
        """
        return actual.equals(self.expected)
