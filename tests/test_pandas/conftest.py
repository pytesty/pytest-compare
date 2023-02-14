from typing import List

import pandas as pd


def create_dataframe(columns: List[str], rows_n: int = 10) -> pd.DataFrame:
    """Create a dataframe with the given columns."""
    return pd.DataFrame({column: [n for n in range(rows_n)] for column in columns})


def create_series(columns: List[str], rows_n: int = 10) -> pd.Series:
    """Create a dataframe with the given columns."""
    return pd.Series({column: [n for n in range(rows_n)] for column in columns})
