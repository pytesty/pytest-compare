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
class CompareIn(CompareBase):
    """Compare in."""

    EXPECTED_TYPE = Any
    ACTUAL_TYPE = Any

    def __init__(self, expected: EXPECTED_TYPE, reverse: bool = False):
        """Initialize the class.

        Args:
            expected (str): The expected value.
            reverse (bool): If True, the actual value is expected to be a
                substring of the expected value. If False, the expected value is
                expected to be a substring of the actual value.
        """
        super().__init__(expected)
        self.reverse = reverse

    def compare(self, actual: ACTUAL_TYPE) -> bool:
        """Compare if the actual value is in the expected value.

        Args:
            actual (Any): The actual value.

        Returns:
            True if the expected value is in the actual value.
        """
        if self.reverse:
            return self.expected in actual
        return actual in self.expected


@typechecked
class CompareSubString(CompareBase):
    """Compare substring.

    To test if the actual value is a substring of the expected value, use CompareSubString(expected).

    For example:

    ```python
    with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
        thing = ProductionClass()
        thing.method("actual_string")

    # test if mock_method was called with "string" as a substring of the actual value
    mock_method.assert_called_once_with(CompareSubString("string"))

    # test if the called value is a substring of the expected value
    mock_method.assert_called_once_with(CompareSubString("expected_string_containing_actual_string", reverse=True))

    # test that the called value is not a substring of the expected value
    mock_method.assert_called_once_with(CompareSubString("not_called_value", contains=False))
    ```
    """

    EXPECTED_TYPE = str
    ACTUAL_TYPE = str

    def __init__(
        self, expected: EXPECTED_TYPE, reverse: bool = False, contains: bool = True
    ):
        """Initialize the class.

        Args:
            expected (str): The expected value.
            reverse (bool): If True, the actual value is expected to be a
                substring of the expected value. If False, the expected value is
                expected to be a substring of the actual value.
            contains (bool): If True, the expected value is expected to be a
                substring of the actual value. If False, the expected value is
                expected to not be a substring of the actual value.
        """
        super().__init__(expected)
        self.reverse = reverse
        self.contains = contains

    def compare(self, actual: ACTUAL_TYPE) -> bool:
        """Compare if the actual value is a substring of the expected value.

        Args:
            actual (str): The actual value.

        Returns:
            True if the expected value is a substring of the actual value.
        """
        if self.reverse:
            return not ((self.expected in actual) ^ self.contains)
        return not ((actual in self.expected) ^ self.contains)
