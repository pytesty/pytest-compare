# Contributing

## Github

The `pytest-compare` package is hosted on Github. The repository is located at https://github.com/pytesty/pytest-compare. ou can find the source code, issues, and pull requests on this repository.

## Setup

To set up your development environment, follow the instructions below.

### Virtual Environment

It is recommended to create a virtual environment for development. To create a virtual environment and install the dependencies, run the following commands:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -e ".[pandas]" -r requirements-dev.txt -r requirements-quality.txt
```

### Pre-commit Hooks

To install the hooks, run the following command:

```shell
$ hooks/autohook.sh install
```

## Creating tests

### Running tests

To run tests, use the following command:

```shell
$ pytest
```

### Writing tests

Tests for `pytest-compare` are written using the `pytest` framework. To create a test for a new `Compare` module, create two files in the `tests` directory: `conftest.py` and a test file starting with `test_`.

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

This way, two base tests will be run for each `Compare` module, one for the `args` and one for the `kwargs` of the method call.