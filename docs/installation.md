# Installation
To install `pytest-compare` from PyPi, run the commmand:

```sh
pip install pytest-compare
```

## Optional dependencies
Depending on the data structures you plan to compare, you may need to install additional packages.

### Pandas
If you need to compare [pandas](https://pandas.pydata.org/)data structures, you can include the `pandas` option in your installation command:

```sh
pip install pytest-compare[pandas]
```

This will install the necessary dependencies for comparing pandas data structures with `pytest-compare`.