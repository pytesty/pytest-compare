from abc import abstractmethod, ABC
from typing import Any, Type

from typeguard import check_type


class CompareBase(ABC):
    """Base class for all comparison classes."""

    EXPECTED_TYPE: Type = Any
    ACTUAL_TYPE: Type = Any

    def __init__(self, expected: EXPECTED_TYPE):
        check_type(expected, self.EXPECTED_TYPE)
        self.expected = expected

    def __eq__(self, actual: ACTUAL_TYPE) -> bool:
        check_type(actual, self.ACTUAL_TYPE)
        return self.compare(actual)

    @abstractmethod
    def compare(self, actual: ACTUAL_TYPE) -> bool:
        """
        Compare two objects.

        Args:
            actual Any: The other object to compare to.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        pass
