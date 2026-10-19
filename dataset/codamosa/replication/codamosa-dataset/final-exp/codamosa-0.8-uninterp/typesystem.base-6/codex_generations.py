

# Generated at 2022-06-14 14:12:45.555209
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value = "value"
    error = ValidationError(text="error")
    res = ValidationResult(value=value)
    assert res.value == value
    assert res.error == None

# Generated at 2022-06-14 14:12:50.440466
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    from typesystem import validate_or_error
    from typesystem.primitives import String
    field = String()
    result1 = validate_or_error(field, 'hello')
    assert tuple(result1) == ('hello', None)
    result2 = validate_or_error(field, None)
    assert (tuple(result2) == (None, {"" : "This field is required."}))

# Generated at 2022-06-14 14:12:51.904881
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr = ValidationResult(error=ValidationError(text="Error"))
    i = iter(vr)
    assert i


# Generated at 2022-06-14 14:12:56.652905
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    class Type:
        def validate_or_error(self, value, *, json_pointer: str = None) -> ValidationResult:
            # An error message
            return ValidationResult(error=ValidationError(text=(value)))


    value = Type().validate_or_error(1)
    assert value
    assert value.value is None
    assert isinstance(value.error, ValidationError)

    # Test __iter__ method
    v, e = value
    assert v is None
    assert isinstance(e, ValidationError)

# Generated at 2022-06-14 14:13:01.519941
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    val = ValidationResult(value=1)
    assert tuple(val) == (1, None)

    val = ValidationResult(value=1, error=ValidationError(text="bad error"))
    assert tuple(val) == (1, ValidationError(text="bad error"))


# Generated at 2022-06-14 14:13:12.416115
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # GIVEN
    b1 = BaseError()
    b2 = BaseError()
    b3 = BaseError(text="More than 100 characters.", code="max_length", key="username")

    # WHEN
    is_equal_to1 = b1.__eq__(b1)
    is_equal_to2 = b1.__eq__(b2)
    is_equal_to3 = b1.__eq__(b3)
    is_equal_to4 = b2.__eq__(b2)
    is_equal_to5 = b2.__eq__(b3)
    is_equal_to6 = b3.__eq__(b3)

    # THEN
    assert is_equal_to1 is True
    assert is_equal_to2 is True
    assert is_equal_to3

# Generated at 2022-06-14 14:13:16.255372
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="xxx", code="yyy", key="zzz")
    m2 = Message(text="xxx", code="zzz", key="zzz")
    assert m1 == m2


# Generated at 2022-06-14 14:13:20.341597
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value = "abcd"
    error = "error"
    vr = ValidationResult(value=value, error=error)
    assert vr.value == value
    assert vr.error == error
    assert list(vr) == [value, error]
    
    

# Generated at 2022-06-14 14:13:25.726596
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    import pytest

    x, y = ValidationResult(value=1)
    assert x == 1
    assert y is None

    x, y = ValidationResult(error=ValidationError(text="error"))
    assert x is None
    assert y.messages()[0].text == "error"

    with pytest.raises(TypeError):
        bool(ValidationResult())

# Generated at 2022-06-14 14:13:29.654540
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    x = ValidationResult(value=1)
    assert next(iter(x)) == 1
    assert next(iter(x)) == None
    assert ValidationResult(error="something") == (None, "something")

# Generated at 2022-06-14 14:13:35.656254
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    msg1 = Message(text='text', code='code', index=['index'])
    msg2 = Message(text='text', code='code', index=['index'])

    # msg1 and msg2 have same arguments, therefore they are equal
    assert msg1 == msg2



# Generated at 2022-06-14 14:13:36.286339
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    pass

# Generated at 2022-06-14 14:13:47.522295
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    from pprint import pprint
    d1 = {
        "message": "Not a string",
        "index": None,
        "code": "type_error.string",
        "start_position": Position(line_no=1, column_no=1, char_index=0),
        "end_position": Position(line_no=1, column_no=1, char_index=0),
    }
    d2 = {
        "message": "Not a string",
        "index": None,
        "code": "type_error.string",
        "start_position": Position(line_no=1, column_no=1, char_index=0),
        "end_position": Position(line_no=1, column_no=1, char_index=0),
    }

# Generated at 2022-06-14 14:13:53.320720
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error1 = BaseError(messages=[Message(text="Error 1", code="code1", index=["index1"])])
    error2 = BaseError(messages=[Message(text="Error 2", code="code2", index=["index2"])])
    assert error1 == error1
    assert error2 == error2
    assert not error1 == error2
    assert not error1 == []
    assert not error1 == object()


# Generated at 2022-06-14 14:13:55.266936
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    obj = BaseError()
    result = obj.__eq__(obj)
    obj.__eq__(result)



# Generated at 2022-06-14 14:13:56.337461
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    BaseError() == BaseError()


# Generated at 2022-06-14 14:14:08.678538
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    be1 = BaseError(text="error1")
    be2 = BaseError(text="error2")
    be3 = BaseError(text="error3")

    assert be1 == be1
    assert be1 != be2
    assert be1 != be3

    be4 = BaseError(messages=[Message(text="error1")])
    be5 = BaseError(messages=[Message(text="error2")])
    be6 = BaseError(messages=[Message(text="error3")])

    assert be4 == be4
    assert be4 != be5
    assert be4 != be6

    be7 = BaseError(messages=[Message(text="error1"), Message(text="error2")])
    be8 = BaseError(messages=[Message(text="error2"), Message(text="error3")])
    be9

# Generated at 2022-06-14 14:14:10.478762
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    input = Position(0,0,0)
    assert input == Position(0,0,0)

# Generated at 2022-06-14 14:14:17.237472
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    b1 = BaseError(messages=[Message(text="hello", code="code", key="key")])
    b2 = BaseError(messages=[Message(text="hello", code="code", key="key")])
    assert b1.__eq__(b2) == True
    assert b1 == b2


# Generated at 2022-06-14 14:14:27.721638
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    position_1 = Position(line_no = 1, column_no = 1, char_index = 1)
    position_2 = Position(line_no = 1, column_no = 1, char_index = 1)
    position_3 = Position(line_no = 2, column_no = 1, char_index = 1)
    position_4 = Position(line_no = 1, column_no = 2, char_index = 1)
    position_5 = Position(line_no = 1, column_no = 1, char_index = 2)
    position_6 = Position(line_no = 1, column_no = 1, char_index = 1)
    assert position_1 == position_2
    assert position_1 != position_3
    assert position_1 != position_4
    assert position_1 != position_5
    assert position

# Generated at 2022-06-14 14:14:45.237164
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    tst = Position(1, 2, 3)
    with pytest.raises(Exception):
        tst == None
    assert isinstance(tst.__eq__(Position(1, 2, 3)), bool) == True


# Generated at 2022-06-14 14:14:55.237038
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    val1 = Message(text = 'May not have more than 100 characters',code = 'max_length',index = ['username'],
    start_position = Position(1,2,3),end_position = Position(4,5,6))
    val2 = Message(text = 'May not have more than 100 characters',code = 'max_length',index = ['username'],
    start_position = Position(1,2,3),end_position = Position(4,5,6))
    val3 = Message(text = 'May not have more than 100 characters',code = 'max_length',index = ['username'],
    start_position = Position(1,2,3),end_position = Position(4,5,6))
    assert (val1==val2) and (val2==val3)


# Generated at 2022-06-14 14:15:04.276391
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    instance = Position(line_no=1, column_no=1, char_index=1,)
    assert instance == Position(line_no=1, column_no=1, char_index=1,)
    assert not instance == Position(line_no=2, column_no=1, char_index=1,)
    assert not instance == Position(line_no=1, column_no=2, char_index=1,)
    assert not instance == Position(line_no=1, column_no=1, char_index=2,)
    assert not instance == object()


# Generated at 2022-06-14 14:15:09.079922
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    one_Message = Message(text="", code='', key='', index='', position='', start_position='', end_position='')
    two_Message = Message(text="", code='', key='', index='', position='', start_position='', end_position='')
    assert one_Message == two_Message


# Generated at 2022-06-14 14:15:21.085154
# Unit test for method __eq__ of class Message

# Generated at 2022-06-14 14:15:27.296357
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    pos1 = Position(1,2,3)
    pos2 = Position(1,2,3)
    pos3 = Position(1,2,4)
    pos4 = Position(1,3,3)
    pos5 = Position(2,2,3)
    assert pos1 == pos2
    assert pos1 != pos3
    assert pos1 != pos4
    assert pos1 != pos5
    assert pos1 == pos1


# Generated at 2022-06-14 14:15:30.418923
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    position = Position(
        line_no=1, column_no=2, char_index=3
    )
    another_position = Position(
        line_no=2, column_no=3, char_index=4
    )
    assert position == position
    assert position != another_position

# Generated at 2022-06-14 14:15:36.791558
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Setup
    line_no_1 = 1; column_no_1 = 1; char_index_1 = 1
    position_1 = Position(line_no_1, column_no_1, char_index_1)
    line_no_2 = 2; column_no_2 = 2; char_index_2 = 2
    position_2 = Position(line_no_2, column_no_2, char_index_2)

    # Test
    assert position_1 == position_1
    assert not position_1 == position_2


# Generated at 2022-06-14 14:15:43.672291
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no=0, column_no=0, char_index=0) != 0
    assert Position(line_no=0, column_no=0, char_index=0) != Position(line_no=0, column_no=0, char_index=1)
    assert Position(line_no=0, column_no=0, char_index=0) != Position(line_no=0, column_no=1, char_index=0)
    assert Position(line_no=0, column_no=0, char_index=0) != Position(line_no=1, column_no=0, char_index=0)


# Generated at 2022-06-14 14:15:55.151884
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Given
    position_1 = Position(1, 2, 3)

    # When
    result_0 = position_1.__eq__(None)
    result_1 = position_1.__eq__(object())
    result_2 = position_1.__eq__(Position(1, 2, 3))
    result_3 = position_1.__eq__(Position(1, 2, 4))
    result_4 = position_1.__eq__(Position(1, 3, 3))
    result_5 = position_1.__eq__(Position(2, 2, 3))

    # Then
    assert result_0 is False
    assert result_1 is False
    assert result_2 is True
    assert result_3 is False
    assert result_4 is False
    assert result_5 is False



# Generated at 2022-06-14 14:16:05.935070
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="lol", code="custom")
    message2 = Message(text="lol", code="custom")
    assert message1 == message2


# Generated at 2022-06-14 14:16:13.553897
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(text="text a", code="code a", index=['one', 'two'], start_position=Position(1,1,1), end_position=Position(2,2,2))
    b = Message(text="text a", code="code a", index=['one', 'two'], start_position=Position(1,1,1), end_position=Position(2,2,2))
    c = Message(text="text b", code="code b", index=['three', 'four'], start_position=Position(3,3,3), end_position=Position(4,4,4))

    # Checks if the condition is true
    assert a == b
    assert not (a == c)


# Generated at 2022-06-14 14:16:17.820869
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg = Message(text = 'test', code = 'test code', index = ['index 1', 'index 2', 'index 3'], start_position = Position(1, 2, 3), end_position = Position(4, 5, 6))
    assert msg.__eq__(msg) == True


# Generated at 2022-06-14 14:16:22.306084
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text='May not have more than 100 characteres',code='max_length', key='username',start_position=Position(1,1,1))
    msg2 = Message(text='May not have more than 100 characteres',code='max_length', key='username',start_position=Position(1,1,1))
    assert msg1 == msg2


# Generated at 2022-06-14 14:16:32.267738
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(text="a", code="a", index=["a"], start_position=Position(1, 2, 3), end_position=Position(4, 5, 6))
    b = Message(text="a", code="a", index=["a"], start_position=Position(1, 2, 3), end_position=Position(4, 5, 6))
    c = Message(text="a", code="a", index=["a"], start_position=Position(7, 8, 9))
    d = Message(text="b", code="a", index=["a"], start_position=Position(1, 2, 3), end_position=Position(4, 5, 6))
    # a == b
    try:
        assert a == b
    except AssertionError as e:
        print("Error!")

# Generated at 2022-06-14 14:16:43.758781
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test equal
    message1 = Message(text="text", code="code", index=["index"])
    message1_copy = Message(text="text", code="code", index=["index"])
    assert message1 == message1_copy
    message2 = Message(text="text", code="code")
    message2_copy = Message(text="text", code="code")
    assert message2 == message2_copy
    message3 = Message(text="text", position=Position(1, 1, 1))
    message3_copy = Message(text="text", position=Position(1, 1, 1))
    assert message3 == message3_copy
    message4 = Message(text="text", start_position=Position(1, 1, 1), end_position=Position(2, 2, 2))

# Generated at 2022-06-14 14:16:52.497300
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text='may not be empty', code='required', key='username')
    message2 = Message(text='may not be empty', code='required', key='username')
    message3 = Message(text='may not be empty', code='regex_failure', key='username')
    message4 = Message(text='may not be empty', code='required', key='password')
    message5 = Message(text='may not be empty', code='required', key='username', index=['users', 2, 'username'])
    assert message1 == message2
    assert message1 != message3
    assert message1 != message4
    assert message1 != message5


# Generated at 2022-06-14 14:17:03.319163
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    Message(text="text", code="code")
    Message(text="text", code="code")
    Message(text="text", code="")
    Message(text="text", code="code", index=[1])
    Message(text="text", code="", index=[1])
    Message(text="text", code="code", index=[1], position=Position(0, 0, 0))
    Message(text="text", code="code", index=[1], start_position=Position(0, 0, 0), end_position=Position(0, 0, 0))
    Message(text="text", code="code", index=[1], start_position=Position(0, 0, 0), end_position=Position(0, 0, 0))

# Generated at 2022-06-14 14:17:14.688732
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Same text, code, index, start_position and end_position
    message_1_1 = Message(text="text", code="code", index=[1],
                          start_position=Position(1, 1, 1), end_position=Position(1, 1, 1))
    message_1_2 = Message(text="text", code="code", index=[1],
                          start_position=Position(1, 1, 1), end_position=Position(1, 1, 1))
    assert message_1_1 == message_1_2

    # Different text
    message_2_1 = Message(text="text_1", code="code", index=[1],
                          start_position=Position(1, 1, 1), end_position=Position(1, 1, 1))

# Generated at 2022-06-14 14:17:18.630918
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(text='abc')
    b = Message(text='abc', position=Position(1,1,1))
    assert a == b
