from typing import Optional, List

import pandas as pd

from pytest_compare.base import CompareBase


class CompareDataFrame(CompareBase):
    """Compare two dataframes."""

    def __init__(self, dataframe: pd.DataFrame, columns: Optional[List[str]] = None):
        """Initialize the class."""
        self.dataframe = dataframe
        self.columns = columns

    def compare(self, other) -> bool:
        """Compare two dataframes."""
        if not isinstance(other, pd.DataFrame):
            return False

        if not self.columns:
            return self.dataframe.equals(other)
        else:
            return self.dataframe[self.columns].equals(other[self.columns])
