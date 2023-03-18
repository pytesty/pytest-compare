# Overview

[![PyPI Latest Release](https://img.shields.io/pypi/v/pytest_compare.svg)](https://pypi.org/project/pytest-compare/)
[![License](https://camo.githubusercontent.com/2439ed6934e5c87e17a7d562cfb92c91d2a673d8/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f726168756c646b6a61696e2f6769746875622d70726f66696c652d726561646d652d67656e657261746f723f7374796c653d666c61742d737175617265)](https://pytesty.github.io/pytest-compare/license/)
[![Documentation](https://readthedocs.org/projects/pytest/badge/?version=latest)](https://pytesty.github.io/pytest-compare/documentation/)
[![DOI](https://github.com/pytest-dev/pytest/workflows/test/badge.svg)](https://github.com/pytesty/pytest-compare/actions?query=workflow%3Atests)
[![Downloads](https://static.pepy.tech/badge/pytest-compare/month)](https://pepy.tech/project/pytest-compare)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

When testing Python code, it's important to validate the method call arguments to ensure that the code is working correctly. The `pytest-compare` package is a useful tool for comparing and validating complex data structures in your test code.

`pytest-compare` is specifically designed to work seamlessly with [assert methods](https://docs.python.org/3/library/unittest.mock.html#the-mock-class). While it's relatively easy to compare simple Python variables, complex structures like `pd.DataFrame` require more effort and time to validate. With `pytest-compare`, you can quickly and easily compare complex data structures, making it easier to validate your test cases and ensure that your code is functioning as expected.
