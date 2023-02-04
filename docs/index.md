# Overview

The `pytest-compare` helps validate method call arguments when testing python code.

`pytest-compare` is designed to work with [assert methods](https://docs.python.org/3/library/unittest.mock.html#the-mock-class). While python native variables can be easily compared, a more complicated structures sometimes do not. For example validating a `pd.DataFrame` will raise an exception. This is where `pytest-compare` comes in. It allows this kind of structures to be easily compared.
