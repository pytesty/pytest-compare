from abc import abstractmethod, ABC
from typing import Any, Type


class CompareBase(ABC):
    """Base class for all comparison classes."""

    EXPECTED_TYPE: Type = Any
    ACTUAL_TYPE: Type = Any

    def __init__(self, expected: EXPECTED_TYPE):
        if self.EXPECTED_TYPE != Any and not isinstance(expected, self.EXPECTED_TYPE):
            raise TypeError(
                f"'expected' must be a {self.EXPECTED_TYPE}, not {type(expected)}"
            )

        self.expected = expected

    def __eq__(self, actual: ACTUAL_TYPE) -> bool:
        if self.ACTUAL_TYPE != Any and not isinstance(actual, self.ACTUAL_TYPE):
            raise TypeError(
                f"'actual' must be a {self.ACTUAL_TYPE}, not {type(actual)}"
            )

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
