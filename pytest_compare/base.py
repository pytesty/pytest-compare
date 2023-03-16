from abc import abstractmethod, ABC
from typing import Any, Type

import pkg_resources
from typeguard import check_type


TYPEGUARD_VERSION_MAJOR = int(
    pkg_resources.get_distribution("typeguard").version.split(".")[0]
)


class CompareBase(ABC):
    """Base class for all comparison classes."""

    EXPECTED_TYPE: Type = Any
    ACTUAL_TYPE: Type = Any

    def __init__(self, expected: EXPECTED_TYPE):
        self._check_type("expected", expected, self.EXPECTED_TYPE)
        self.expected = expected

    def __eq__(self, actual: ACTUAL_TYPE) -> bool:
        self._check_type("actual", actual, self.ACTUAL_TYPE)
        return self.compare(actual)

    def _check_type(self, argname: str, value, expected_type):
        if TYPEGUARD_VERSION_MAJOR >= 3:
            check_type(value, expected_type)
        else:
            check_type(argname, value, expected_type)

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
