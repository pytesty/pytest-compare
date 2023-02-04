# Contributing

## Setup

### Virtual Environment

Create a virtual environment and install the dependencies:

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -e ".[pandas]" -r requirements-dev.txt

### Pre-commit Hooks

Start by installing the pre-commit hooks which will run `black`, `mypy`, `flake8`, and `codespell` on every commit.:

    $ hooks/autohook.sh install

## Creating tests

### Running tests

To test the code, run the following command:

    $ pytest

### Writing tests

Tests are written using the `pytest` framework. To create a test for a new `Compare` module, create two files in the `tests` directory: `conftest.py` and the test file witch must start with `test_`.
The `conftest.py` file must implement the following fixtures:

```python
@pytest.fixture
def actual_call_args() -> Tuple[Any]:
    raise NotImplementedError("`actual_call_args` must be implemented")


@pytest.fixture
def actual_call_kwargs() -> Dict[str, Any]:
    raise NotImplementedError("`actual_call_kwargs` must be implemented")


@pytest.fixture
def expected_call_args() -> Tuple[Any]:
    raise NotImplementedError("`expected_call_args` must be implemented")


@pytest.fixture
def expected_call_kwargs() -> Dict[str, CompareBase]:
    raise NotImplementedError("`expected_call_kwargs` must be implemented")
```

The test file must implement a test class that inherits from `BaseTest`.

That way two base tests will be run for each `Compare` module that wil test the `args` and `kwargs` of the method call.
