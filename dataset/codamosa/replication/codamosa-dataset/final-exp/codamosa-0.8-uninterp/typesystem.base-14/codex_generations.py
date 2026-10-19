

# Generated at 2022-06-14 14:12:49.516140
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    x = ValidationResult(1, 2)
    y = ValidationResult(None, 3)
    assert list(x.__iter__()) == [1, 2]
    assert list(y.__iter__()) == [None, 3]



# Generated at 2022-06-14 14:12:53.316472
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    class_name = BaseError.__name__
    input = BaseError(messages=[Message(text="Text")])
    expected = BaseError(messages=[Message(text="Text")])
    assert input == expected, f"{class_name}.__eq__() is error!"


# Generated at 2022-06-14 14:12:56.010722
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr = ValidationResult(error=ValidationError(text="test"))
    assert list(vr) == [None, ValidationError(text="test")]

# Generated at 2022-06-14 14:13:05.564090
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr1 = ValidationResult(value=4)
    vr1_iter = iter(vr1)
    assert next(vr1_iter) == 4
    assert next(vr1_iter) is None

    ve = ValidationError(text="cannot be greater than 20")
    vr2 = ValidationResult(error=ve)
    vr2_iter = iter(vr2)
    assert next(vr2_iter) is None
    assert next(vr2_iter) == ve
    try:
        next(vr2_iter)
        assert False
    except StopIteration:
        pass



# Generated at 2022-06-14 14:13:06.069729
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    pass

# Generated at 2022-06-14 14:13:10.858947
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    val = ValidationResult(value=1)
    x = []
    for i in val:
        x.append(i)
    assert x == [1, None]

    val = ValidationResult(error=ValidationError())
    x = []
    for i in val:
        x.append(i)
    assert x == [None, ValidationError()]


# Generated at 2022-06-14 14:13:18.564415
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    class DerivedError(BaseError):
        pass

    error = BaseError(text="text")

    assert error == error
    assert error == BaseError(text="text")
    assert error != BaseError(text="other text")
    assert error != BaseError(text="text", code="code")
    assert error != BaseError(text="text", key="key")
    assert (
        error
        != BaseError(
            text="text",
            position=Position(
                line_no=123, column_no=456, char_index=789,
            ),
        )
    )

# Generated at 2022-06-14 14:13:22.895570
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value, error = ValidationResult(value='a').__iter__()
    assert value == 'a'
    assert error is None
    value, error = ValidationResult(error='b').__iter__()
    assert value is None
    assert error == 'b'


# Generated at 2022-06-14 14:13:28.772737
# Unit test for method __eq__ of class BaseError

# Generated at 2022-06-14 14:13:33.409839
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    assert list(ValidationResult(value=1)) == [1, None]
    assert list(ValidationResult(error=ValidationError(text="some error"))) == [None, ValidationError(text="some error")]