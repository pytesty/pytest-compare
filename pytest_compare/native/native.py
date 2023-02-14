from typing import Any, Type

from pytest_compare.base import CompareBase


class CompareType(CompareBase):
    """Compare type."""

    def __init__(self, expected: Type):
        self.expected = expected

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

    def __init__(self, expected: Type):
        self.expected = expected

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

    def __init__(self, expected: Type):
        self.expected = expected

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

    def __init__(self, expected: Any):
        self.expected = expected

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

    def __init__(self, expected: str, reverse: bool = False):
        if not isinstance(expected, str):
            raise TypeError(f"Expected must be a string, not {type(expected)}")
        if not isinstance(reverse, bool):
            raise TypeError(f"Reverse must be a boolean, not {type(reverse)}")

        self.expected = expected
        self.reverse = reverse

    def compare(self, actual: Any) -> bool:
        """Compare the actual substring to the expected substring.

        Args:
            actual: The actual value.

        Returns:
            True if the actual value matches the expected value.
        """
        if not isinstance(actual, str):
            raise TypeError(f"Actual must be a string, not {type(actual)}")

        if self.reverse:
            return actual in self.expected
        return self.expected in actual
