from typing import Any, Type

from pytest_compare.base import CompareBase


class CompareType(CompareBase):
    """Compare type."""

    EXPECTED_TYPE = Type

    def compare(self, actual: Any) -> bool:
        """Compare the actual type to the expected type.

        Args:
            actual: The actual value.

        Returns:
            True if the actual value matches the expected value.
        """
        return type(actual) == self.expected


class CompareIsInstanceOf(CompareBase):
    """Compare instance of."""

    EXPECTED_TYPE = Type

    def compare(self, actual: Any) -> bool:
        """Compare the actual type to the expected type.

        Args:
            actual: The actual value.

        Returns:
            True if the actual value matches the expected value.
        """
        return isinstance(actual, self.expected)


class CompareIsSubclassOf(CompareBase):
    """Compare instance of."""

    EXPECTED_TYPE = Type

    def compare(self, actual: Any) -> bool:
        """Compare the actual type to the expected type.

        Args:
            actual: The actual value.

        Returns:
            True if the actual value matches the expected value.
        """
        return issubclass(actual, self.expected)


class CompareLength(CompareBase):
    """Compare length."""

    def compare(self, actual: Any) -> bool:
        """Compare the actual length to the expected length.

        Args:
            actual: The actual value.

        Returns:
            True if the actual value matches the expected value.
        """
        return len(actual) == self.expected


class CompareSubString(CompareBase):
    """Compare substring."""

    EXPECTED_TYPE = str
    ACTUAL_TYPE = str

    def __init__(self, expected: EXPECTED_TYPE, reverse: bool = False):
        if not isinstance(reverse, bool):
            raise TypeError(f"'reverse' must be a bool, not {type(reverse)}")

        super().__init__(expected)
        self.reverse = reverse

    def compare(self, actual: Any) -> bool:
        """Compare the actual substring to the expected substring.

        Args:
            actual: The actual value.

        Returns:
            True if the actual value matches the expected value.
        """
        if self.reverse:
            return actual in self.expected
        return self.expected in actual
