from typing import Any, Type

from typeguard import typechecked

from pytest_compare.base import CompareBase, CompareBaseReverse


@typechecked
class CompareType(CompareBase):
    """Compare types."""

    EXPECTED_TYPE = Type

    def compare(self, actual: Any) -> bool:
        """Compare the actual type to the expected type.

        Args:
            actual (Any): The actual value.

        Returns:
            True if the actual value matches the expected value.
        """
        return type(actual) == self.expected


@typechecked
class CompareIsInstanceOf(CompareBase):
    """Compare instanceof."""

    EXPECTED_TYPE = Type

    def compare(self, actual: Any) -> bool:
        """Compare if the actual value is an instance of the expected type.

        Args:
            actual (Any): The actual instance.

        Returns:
            True if the actual instance is an instance of the expected type.
        """
        return isinstance(actual, self.expected)


@typechecked
class CompareIsSubclassOf(CompareBase):
    """Compare issubclass."""

    EXPECTED_TYPE = Type

    def compare(self, actual: Any) -> bool:
        """Compare if the actual value is a subclass of the expected type.

        Args:
            actual (Any): The actual instance.

        Returns:
            True if the actual instance is a subclass of the expected type.
        """
        return issubclass(actual, self.expected)


@typechecked
class CompareLength(CompareBase):
    """Compare length."""

    def compare(self, actual: Any) -> bool:
        """Compare the actual length to the expected length.

        Args:
            actual (Any): The actual value.

        Returns:
            True if the actual instance has the expected length.
        """
        return len(actual) == self.expected


@typechecked
class CompareIn(CompareBaseReverse):
    EXPECTED_TYPE = Any
    ACTUAL_TYPE = Any

    def compare(self, actual: ACTUAL_TYPE, expected: EXPECTED_TYPE) -> bool:
        return actual in expected


@typechecked
class CompareSubString(CompareBaseReverse):
    """Compare substring."""

    EXPECTED_TYPE = str
    ACTUAL_TYPE = str

    def __init__(self, expected: EXPECTED_TYPE, contains: bool = True, reverse: bool = False):
        super().__init__(expected, reverse)
        self.contains = contains

    def compare(self, actual: ACTUAL_TYPE, expected: EXPECTED_TYPE) -> bool:
        """Compare if the actual value is a substring of the expected value.

        Args:
            actual (str): The actual value.
            expected (str): The expected value.

        Returns:
            True if the actual value is a substring of the expected value.
        """
        return (self.expected in actual) ^ self.contains
