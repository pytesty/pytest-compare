from typing import Any, Type

from typeguard import typechecked

from pytest_compare.base import CompareBase


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
class CompareSubString(CompareBase):
    """Compare substring."""

    EXPECTED_TYPE = str
    ACTUAL_TYPE = str

    def __init__(self, expected: EXPECTED_TYPE, reverse: bool = False):
        super().__init__(expected)
        self.reverse = reverse

    def compare(self, actual: ACTUAL_TYPE) -> bool:
        """Compare if the actual value is a substring of the expected value.

        Args:
            actual (str): The actual value.

        Returns:
            True if the actual value is a substring of the expected value.
        """
        if self.reverse:
            return actual in self.expected
        return self.expected in actual
