

# Generated at 2022-06-14 14:12:52.982537
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="error1") == BaseError(text="error2")
    assert BaseError(text="error1") != BaseError(text="error1")


# Generated at 2022-06-14 14:13:05.293625
# Unit test for method __eq__ of class Message
def test_Message___eq__():

    # Message.__eq__: Argument 'other' has incorrect type (expected Message, got int)

    with pytest.raises(TypeError, match=r"Argument 'other' has incorrect type \(expected Message, got int\)"):
        Message(text="", code="").__eq__((1))

    # Message.__eq__: Argument 'other' has incorrect type (expected Message, got NoneType)

    with pytest.raises(TypeError, match=r"Argument 'other' has incorrect type \(expected Message, got NoneType\)"):
        Message(text="", code="").__eq__((None))

    # Message.__eq__: Message.text: Expected string, got None


# Generated at 2022-06-14 14:13:07.608265
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result_0 = ValidationResult(value=1)
    result_1 = ValidationResult(error=ValidationError())
    assert tuple(result_0) == (1, None)
    assert tuple(result_1) == (None, ValidationError())


# Generated at 2022-06-14 14:13:10.816052
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result = ValidationResult(value="test")
    assert list(result) == ["test", None]

    result = ValidationResult(error=ValidationError(text="test"))
    assert list(result) == [None, ValidationError(text="test")]

# Generated at 2022-06-14 14:13:13.634065
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    a = ValidationResult(value=1)
    b = iter(a)
    x = next(b)
    assert x == 1
    y = next(b)
    assert y == None



# Generated at 2022-06-14 14:13:22.316773
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    """
    Unit test for method __eq__ of class Message
    """
    pos = Position(line_no=1, column_no=2, char_index=3)
    m = Message(text="test", code="test", key=1, index=[1, 2], position=pos,
                start_position=pos, end_position=pos)
    m2 = Message(text="test", code="test", key=1, index=[1, 2], position=pos,
                 start_position=pos, end_position=pos)
    assert m == m2


# Generated at 2022-06-14 14:13:29.287882
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value = 123
    error = ValidationError()
    vr = ValidationResult(value=value)
    iter_result = iter(vr)
    assert next(iter_result) == value
    assert next(iter_result) is None
    vr = ValidationResult(error=error)
    iter_result = iter(vr)
    assert next(iter_result) is None
    assert next(iter_result) == error


# Generated at 2022-06-14 14:13:35.421711
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value, error = ValidationResult(value=1).__iter__()
    assert value == 1
    assert error is None
    value, error = ValidationResult(error=ValidationError(text="error")).__iter__()
    assert value is None
    assert error == ValidationError(text="error")


# Generated at 2022-06-14 14:13:36.651828
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert ValidationError(text="error message").__eq__(ValidationError(text="error message")) == True



# Generated at 2022-06-14 14:13:40.189189
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    assert list(ValidationResult(value=None, error="Error")) == [None, "Error"]
    assert list(ValidationResult(value=32, error=ValidationError(text="Error"))) == [32, ValidationError(text="Error")]