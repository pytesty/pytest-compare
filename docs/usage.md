# Usage
The comparation modules are design to be used with [assert methods](https://docs.python.org/3/library/unittest.mock.html#the-mock-class). When validating patched method call arguments 

```python
df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})

with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(df)
```

```python
# will raise an exception
mock_method.assert_called_once_with(df)

# the correct way
mock_method.assert_called_once_with(CompareDataFrame(df))
```

## Multiple arguments in a call
When a method is called using multiple arguments, all of them must be addressed in the test. while python native varibles can be easily compared, `pytest-compare` is designed to compare a more complicated structures and do custom compares.

```python
with patch.object(ProductionClass, 'method', return_value=None) as mock_method:
    thing = ProductionClass()
    thing.method(1, "str", df1, df2)
    
# the correct way
mock_method.assert_called_once_with(1, "str", CompareDataFrame(df1), CompareDataFrame(df2))
```

## Args and Kwargs
When validating the call, the expected values must be passed in the exact same mix of args and kwargs as when they were called.

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
