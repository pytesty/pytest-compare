from abc import ABC
from typing import Optional, List, Union

import pandas as pd
from typeguard import typechecked

from pytest_compare.base import CompareBase


class CompareDataFrameBase(CompareBase, ABC):
    EXPECTED_TYPE = Union[pd.DataFrame, pd.Series]
    ACTUAL_TYPE = Union[pd.DataFrame, pd.Series]


@typechecked
class CompareDataFrame(CompareDataFrameBase):
    """Compare two dataframes."""

    EXPECTED_TYPE = pd.DataFrame
    ACTUAL_TYPE = pd.DataFrame

    def __init__(self, expected: EXPECTED_TYPE, columns: Optional[List[str]] = None):
        """Initialize the class.

        Args:
            expected (pd.DataFrame): Expected Dataframe.
            columns (List[str], optional): Columns to compare. If None, all columns are compared. Defaults to None.
        """
        super().__init__(expected)
        self._columns = columns

    def compare(self, actual: ACTUAL_TYPE) -> bool:
        """Compare two dataframes.

        Args:
            actual (pd.DataFrame): Actual Dataframe.

        Returns:
            bool: True if the dataframes are equal, False otherwise.
        """
        if not self._columns:
            return actual.equals(self.expected)
        else:
            return actual[self._columns].equals(self.expected[self._columns])


@typechecked
class CompareDataFrameColumns(CompareDataFrameBase):
    """Compare two dataframe columns."""

    EXPECTED_TYPE = Union[pd.DataFrame, List[str]]
    ACTUAL_TYPE = pd.DataFrame

    def compare(self, actual: ACTUAL_TYPE) -> bool:
        """Compare two dataframe columns.

        Args:
            actual (pd.DataFrame): Actual Dataframe.

        Returns:
            bool: True if columns are identical, False otherwise.
        """
        expected_columns = (
            self.expected.columns
            if isinstance(self.expected, pd.DataFrame)
            else self.expected
        )
        return set(actual.columns) == set(expected_columns)


@typechecked
class CompareSeries(CompareDataFrameBase):
    """Compare two series."""

    EXPECTED_TYPE = pd.Series
    ACTUAL_TYPE = pd.Series

    def compare(self, actual: ACTUAL_TYPE) -> bool:
        """Compare two series.

        Args:
            actual (pd.Series): Actual Series.

        Returns:
            bool: True if the series are equal, False otherwise.
        """
        return actual.equals(self.expected)
