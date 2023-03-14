from abc import ABC
from typing import Dict

from pytest_compare.base import CompareBase


class CompareDictBase(CompareBase, ABC):
    EXPECTED_TYPE = Dict
    ACTUAL_TYPE = Dict


class CompareDictContains(CompareDictBase):
    """CompareDictSubSet is a class that compares two dictionaries and
    checks if the first dictionary is a subset of the second dictionary.
    """

    def __init__(self, expected: Dict, reverse_contains: bool = False):
        """Initialize the class.

        Args:
            expected (dict): First dictionary.
            reverse_contains (bool, optional): If True, the comparison is reversed.
        """
        super().__init__(expected)

        if reverse_contains and not isinstance(reverse_contains, bool):
            raise TypeError(
                f"'reverse_contains' must be a bool, not {type(reverse_contains)}"
            )
        self._reverse_contains = reverse_contains

    def compare(self, actual: Dict) -> bool:
        """Compare two dictionaries and check if the first dictionary is a
        subset of the second dictionary.

        Args:
            actual (dict): Second dictionary.

        Returns:
            bool: True if the first dictionary is a subset of the second
                dictionary, False otherwise.
        """
        if self._reverse_contains:
            return actual.items() <= self.expected.items()
        else:
            return self.expected.items() <= actual.items()


class CompareDickKeys(CompareDictBase):
    """CompareDickKeys is a class that compares two dictionaries and
    checks if the first dictionary has the same keys as the second
    dictionary.
    """

    def compare(self, actual: Dict) -> bool:
        """Compare two dictionaries and check if the first dictionary has
        the same keys as the second dictionary.

        Args:
            actual (dict): Second dictionary.

        Returns:
            bool: True if the first dictionary has the same keys as the
                second dictionary, False otherwise.
        """
        return set(actual.keys()) == set(self.expected.keys())
