from abc import ABC

from pytest_compare.base import CompareBase


class CompareDictBase(CompareBase, ABC):
    def __init__(self, expected: dict):
        """Initialize the class.

        Args:
            expected (dict): First dictionary.
        """
        if not isinstance(expected, dict):
            raise TypeError(f"Expected must be a dictionary, not {type(expected)}")

        self._expected = expected


class CompareDictContains(CompareDictBase):
    """CompareDictSubSet is a class that compares two dictionaries and
    checks if the first dictionary is a subset of the second dictionary.
    """

    def __init__(self, expected: dict, reverse_contains: bool = False):
        """Initialize the class.

        Args:
            expected (dict): First dictionary.
            reverse_contains (bool, optional): If True, the comparison is reversed.
        """
        super().__init__(expected)
        self._reverse_contains = reverse_contains

    def compare(self, actual) -> bool:
        """Compare two dictionaries and check if the first dictionary is a
        subset of the second dictionary.

        Args:
            actual (dict): Second dictionary.

        Returns:
            bool: True if the first dictionary is a subset of the second
                dictionary, False otherwise.
        """
        if not isinstance(actual, dict):
            return False

        if self._reverse_contains:
            return actual.items() <= self._expected.items()
        else:
            return self._expected.items() <= actual.items()


class CompareDickKeys(CompareDictBase):
    """CompareDickKeys is a class that compares two dictionaries and
    checks if the first dictionary has the same keys as the second
    dictionary.
    """

    def compare(self, actual) -> bool:
        """Compare two dictionaries and check if the first dictionary has
        the same keys as the second dictionary.

        Args:
            actual (dict): Second dictionary.

        Returns:
            bool: True if the first dictionary has the same keys as the
                second dictionary, False otherwise.
        """
        return isinstance(actual, dict) and set(actual.keys()) == set(
            self._expected.keys()
        )
