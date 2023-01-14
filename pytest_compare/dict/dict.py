from pytest_compare.base import CompareBase


class CompareDictSubSet(CompareBase):
    """CompareDictSubSet is a class that compares two dictionaries and
    checks if the first dictionary is a subset of the second dictionary.
    """

    def __init__(self, first: dict, reverse: bool = False):
        """Initialize the class.

        Args:
            first (dict): First dictionary.
            reverse (bool, optional): If True, the comparison is reversed.
        """
        self.first = first
        self.reverse = reverse

    def compare(self, second) -> bool:
        """Compare two dictionaries and check if the first dictionary is a
        subset of the second dictionary.

        Args:
            second (dict): Second dictionary.

        Returns:
            bool: True if the first dictionary is a subset of the second
                dictionary, False otherwise.
        """
        if not isinstance(second, dict):
            return False

        if self.reverse:
            return second.items() <= self.first.items()
        else:
            return self.first.items() <= second.items()


class CompareDickKeys(CompareBase):
    """CompareDickKeys is a class that compares two dictionaries and
    checks if the first dictionary has the same keys as the second
    dictionary.
    """

    def __init__(self, first: dict):
        """Initialize the class.

        Args:
            first (dict): First dictionary.
        """
        self.first = first

    def compare(self, second) -> bool:
        """Compare two dictionaries and check if the first dictionary has
        the same keys as the second dictionary.

        Args:
            second (dict): Second dictionary.

        Returns:
            bool: True if the first dictionary has the same keys as the
                second dictionary, False otherwise.
        """
        return isinstance(second, dict) and set(self.first.keys()) == set(second.keys())
