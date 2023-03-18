# Usage
The comparison modules provided by `pytest-compare` are designed to be used with [assert methods](https://docs.python.org/3/library/unittest.mock.html#the-mock-class)to validate patched method call arguments. When validating call arguments for a method that takes a Pandas DataFrame as an argument, the `CompareDataFrame` class provided by `pytest-compare` can be used to perform the comparison.

For example, suppose you have a `ProductionClass` with a method that takes a Pandas DataFrame as an argument, and you want to validate that the method was called with the expected DataFrame argument:

```python
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(df)
    
# will raise a ValueError exception
mock_method.assert_called_once_with(df)

# Validate that the method was called with the expected DataFrame argument
mock_method.assert_called_once_with(CompareDataFrame(df))
```

## Multiple arguments in a call
Note that when a method is called using multiple arguments, all of them must be addressed in the test. While Python native variables can be easily compared, `pytest-compare` is designed to compare more complicated structures and perform custom comparisons.

```python
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, "str", df1, df2)
    
# the correct way
mock_method.assert_called_once_with(1, "str", CompareDataFrame(df1), CompareDataFrame(df2))
```

## Args and Kwargs
When validating a call that includes both args and kwargs, the expected values must be passed in the exact same mix of args and kwargs as when they were called.

```python
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(df1, dataframe=df2)
    
# the correct way
mock_method.assert_called_once_with(CompareDataFrame(df1), dataframe=CompareDataFrame(df2))
```

### Actual and Expected convention
* actual: The values that the method was originally called with.
* expected: Test values to see if the method was called with.

For example here, `arg_actual` is the actual value while `arg_expected` is the expected value.

```python
mock_method = Mock()

mock_method(arg_actual)
mock_method.assert_called_once_with(arg_expected)
```

If `arg_actual` is not equal to `arg_expected`, an exception will be raised.

## Creating custom comparisons

To create a custom comparison, create a class that inherits from `CompareBase` and implement the `compare` method. The `compare` method should return `True` if the actual value matches the expected value, and `False` otherwise.

```python
class CompareCustom(CompareBase):
    def compare(self, actual: Any) -> bool:
        result =  # compare actual and expected

        return result
```

### Type validation

The types are validated using the `EXPECTED_TYPE` and `ACTUAL_TYPE` class attributes. If the types are not equal, an exception will be raised.

```python
class CustomClass:
    pass


class CompareCustom(CompareBase):
    EXPECTED_TYPE = CustomClass
    ACTUAL_TYPE = CustomClass

    def compare(self, actual: ACTUAL_TYPE) -> bool:
        result =  # compare actual and expected

        return result
```
