import pytest


DICT_LENGTH = 10


def create_dict(entries_format: str, length: int) -> dict:
    """Create a dict with a given format."""
    return {entries_format.format(n): n for n in range(length)}


@pytest.fixture
def actual_entries_format() -> str:
    return "key_{}"


@pytest.fixture
def actual_dict_length() -> int:
    return DICT_LENGTH


@pytest.fixture
def actual_dict(actual_entries_format, actual_dict_length: int) -> dict:
    return create_dict(actual_entries_format, actual_dict_length)


@pytest.fixture
def expected_entries_format(actual_entries_format: str) -> str:
    return actual_entries_format


@pytest.fixture
def expected_dict_length(actual_dict_length: int) -> int:
    return actual_dict_length


@pytest.fixture
def expected_dict(expected_entries_format, expected_dict_length: int) -> dict:
    return create_dict(expected_entries_format, expected_dict_length)
