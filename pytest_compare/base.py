from abc import abstractmethod
from typing import Any


class CompareBase:
    """Base class for all comparison classes."""

    @abstractmethod
    def compare(self, actual: Any) -> bool:
        """
        Compare two objects.

        Args:
            actual (pd.DataFrame): The other object to compare to.

        Returns:
             bool: True if the objects are equal, False otherwise.
        """
        pass

    def __eq__(self, actual):
        return self.compare(actual)
