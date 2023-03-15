from abc import ABC
from typing import Dict, List, Union

from typeguard import typechecked

from pytest_compare.base import CompareBase


class CompareDictBase(CompareBase, ABC):
    EXPECTED_TYPE = Dict
    ACTUAL_TYPE = Dict


@typechecked
class CompareDictContains(CompareDictBase):
    """Check if the actual dictionary is a subset of the expected dictionary."""

    def __init__(self, expected: Dict, reverse_contains: bool = False):
        """Initialize the class.

        Args:
            expected (Dict): Expected dictionary.
            reverse_contains (bool): If True, the comparison is reversed.
        """
        super().__init__(expected)
        self._reverse_contains = reverse_contains

    def compare(self, actual: Dict) -> bool:
        """Check if the actual dictionary is a subset of the expected dictionary.
        If reverse_contains is True, the comparison is reversed.

        Args:
            actual (Dict): Actual dictionary.

        Returns:
            bool: True if the first dictionary is a subset of the second dictionary, False otherwise.
        """
        if self._reverse_contains:
            return actual.items() <= self.expected.items()
        else:
            return self.expected.items() <= actual.items()


@typechecked
class CompareDictKeys(CompareDictBase):
    """Compare if the actual dictionary has the expected keys."""

    EXPECTED_TYPE = Union[Dict, List[str]]

    def compare(self, actual: Dict) -> bool:
        """Compare if the actual dictionary has the expected keys.

        Args:
            actual (Dict, List[str]): Actual dictionary or list of expected keys.

        Returns:
            bool: True if the actual dictionary has the expected keys, False otherwise.
        """
        expected_keys = (
            self.expected.keys() if isinstance(self.expected, dict) else self.expected
        )
        return set(actual.keys()) == set(expected_keys)
