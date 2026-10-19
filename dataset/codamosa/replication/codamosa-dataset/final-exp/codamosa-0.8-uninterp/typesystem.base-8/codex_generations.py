

# Generated at 2022-06-14 14:13:01.470583
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    x = iter(ValidationResult(error=ValidationError(messages=[Message(text="a message")])))
    assert next(x) == None
    assert next(x) == ValidationError(messages=[Message(text="a message")])
    try:
        next(x)
    except StopIteration:
        pass
    else:
        assert False

    y = iter(ValidationResult(value=7))
    assert next(y) == 7
    assert next(y) == None
    try:
        next(y)
    except StopIteration:
        pass
    else:
        assert False


# Generated at 2022-06-14 14:13:05.032771
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    b=BaseError(text="test")
    c=BaseError(text="test")
    d=BaseError(text="fail")
    assert b==c
    assert b!=d

# Generated at 2022-06-14 14:13:11.135069
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    instance = BaseError(text='Rrrrrr!')
    assert str(instance) == 'Rrrrrr!'
    instance = BaseError(messages=[Message(text='Rrrrrr!', code='invalid')])
    assert str(instance) == "{'': 'Rrrrrr!'}"
    instance = BaseError(messages=[Message(text='Rrrrrr!', code='invalid')])
    assert str(instance) == "{'': 'Rrrrrr!'}"

# Generated at 2022-06-14 14:13:18.715884
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message("text", key="123") == Message("text", key="123")
    assert Message("text", key="123") != Message("text", key="1234")
    assert Message("text", key="123") != Message("text2", key="123")
    assert Message("text", key="123") != Message("text", key="123", index=[123])
    assert Message("text", key="123") != Message("text", key="123", code="code")
    a = Message("text", key="123")
    assert a == a
    assert not(a != a)
    b = Message("text", key="123")
    assert a == b
    assert not(a != b)
    assert b == a
    assert not(b != a)

# Generated at 2022-06-14 14:13:20.036084
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    ValidationResult.__iter__()



# Generated at 2022-06-14 14:13:25.441537
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text='No foo', code='no_foo', key='foo')
    m2 = Message(text='No foo', code='no_foo', key='foo')
    m3 = Message(text='No foo', code='no_foo', key='foo', index=['bar'])
    assert m1 == m2
    assert m1 != m3

# Generated at 2022-06-14 14:13:30.353769
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result = ValidationResult(value=42)
    assert list(result) == [42, None]
    result = ValidationResult(error=ValidationError(text="hello"))
    assert list(result) == [None, ValidationError(text="hello")]


# Generated at 2022-06-14 14:13:33.507291
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    validationResult = ValidationResult()
    expected_result = (None, None)
    assert tuple(validationResult) == expected_result


# Generated at 2022-06-14 14:13:37.820621
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result = ValidationResult(error=ValidationError(text='Test Error'))
    assert list(result) == [None, ValidationError(text='Test Error')]
    result = ValidationResult(value=True)
    assert list(result) == [True, None]


# Generated at 2022-06-14 14:13:41.299860
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    try:
        raise BaseError(text='New text', code='max_length', key='code')
    except BaseError as err:
        assert str(err) == 'New text'



# Generated at 2022-06-14 14:13:55.595313
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    BaseError()


# Generated at 2022-06-14 14:13:58.093659
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    assert str(BaseError(text="Value is not a valid integer")) == "Value is not a valid integer"


# Generated at 2022-06-14 14:14:09.378031
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    print('test_Message___eq__')
    line_no = 1
    column_no = 2
    char_index = 3
    pos = Position(line_no, column_no, char_index)
    text = 'text'
    code = 'code'
    index = ['index']
    msg_1 = Message(text=text, code=code, index=index, position=pos)
    msg_2 = Message(text=text, code=code, index=index, start_position=pos, end_position=pos)
    msg_3 = Message(text=text, code=code, index=index, start_position=pos, end_position=pos)
    assert msg_1 == msg_2
    assert msg_2 == msg_3


# Generated at 2022-06-14 14:14:21.068100
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text='a') == BaseError(text='a')
    assert BaseError(text='a', code='b', key='c') == BaseError(text='a', code='b', key='c')
    assert BaseError(text='a', code='b', key='c') != BaseError(text='a', code='b')
    assert BaseError(text='a', code='b', key='c') != BaseError(text='a', code='b', key='d')
    assert BaseError(messages=[Message(text='a')]) != BaseError(messages=[Message(text='b')])
    assert BaseError(text='a') != BaseError(messages=[Message(text='a')])


# Generated at 2022-06-14 14:14:29.396805
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    """
        >>> msg1 = Message(text="Authorization failed", code="authorization_failed")
    >>> msg2 = Message(text="Authorization failed", code="authorization_failed")
    >>> msg3 = Message(text="Authorization failed", code="authorization_failed", key="username")
    >>> msg4 = Message(text="Authorization failed", code="authorization_failed")
    >>> msg1 == msg1
    True
    >>> msg1 == msg2
    True
    >>> msg1 == msg3
    False
    >>> msg2 == msg3
    False
    >>> msg1 == msg4
    True
    >>> msg1 == "auth"
    False
    """
    pass


# Generated at 2022-06-14 14:14:33.852524
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message_1 = Message(text='test', code='test', position=Position(line_no=1, column_no=0, char_index=0))
    message_2 = Message(text='test', code='test', position=Position(line_no=1, column_no=0, char_index=0))
    assert message_1 == message_2

# Generated at 2022-06-14 14:14:37.978443
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="test_text", code="test_code", key="test_key", position="test_position", messages="test_messages") == BaseError(text="test_text", code="test_code", key="test_key", position="test_position", messages="test_messages")


# Generated at 2022-06-14 14:14:46.761648
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Tested that the contents of the class are equal to another object
    assert Position(1, 2, 3) == Position(1, 2, 3)
    assert not Position(1, 2, 3) == Position(2, 3, 4)
    # Tested that the class is equal to itself
    assert Position(1, 2, 3) == Position(1, 2, 3)
    # Tested that the class is equal to itself with some attributes modified
    assert Position(1, 2, 3) == Position(1, 2, 3)


# Generated at 2022-06-14 14:14:53.977931
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    import os
    from pathlib import Path
    from json import loads
    from yaml import safe_load

    def test_case(name: str, content: typing.Any, error_data: typing.Any, ext: str, parse_method: typing.Callable):
        error_object = ValidationError(**error_data)
        error = str(error_object)
        print(f"{name} error: {error}")

        # Save the error to a file, to ensure the str(error) output is parseable.
        file_path = Path("__tests__/tmp/") / f"{name} error.{ext}"
        file_path.mkdir(exist_ok=True, parents=True)
        with open(file_path, "w") as f:
            f.write(error)

        # Read the error

# Generated at 2022-06-14 14:15:00.007489
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    text_var = 'May not have more than 100 characters'
    code_var = 'max_length'
    key_var = 'username'
    x = Message(text=text_var, code=code_var, key=key_var)
    y = Message(text=text_var, code=code_var, key=key_var)
    assert x == y


# Generated at 2022-06-14 14:15:13.652317
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    import random
    import string
    import sys
    import time


# Generated at 2022-06-14 14:15:25.503076
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    e = ValidationError(text="This is the error")
    assert str(e) == "This is the error"

    e = ValidationError(messages=[Message(text="This is the error")])
    assert str(e) == "{'': 'This is the error'}"

    e = ValidationError(messages=[Message(text="This is the error", key="key1")])
    assert str(e) == "{'key1': 'This is the error'}"

    e = ValidationError(messages=[Message(text="This is the error", key="key2")])
    assert str(e) == "{'key2': 'This is the error'}"


# Generated at 2022-06-14 14:15:35.168298
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(
        text="message_1_foo", key="foo"
    ) == BaseError(text="message_1_foo", key="foo")
    assert BaseError(
        text="message_1_bar", key="bar"
    ) == BaseError(text="message_1_bar", key="bar")
    assert BaseError(
        text="message_2_foo", key="foo"
    ) == BaseError(text="message_2_foo", key="foo")
    assert BaseError(
        text="message_2_bar", key="bar"
    ) == BaseError(text="message_2_bar", key="bar")
    assert BaseError(
        text="message_3_foo", key="foo"
    ) == BaseError(text="message_3_foo", key="foo")
    assert BaseError

# Generated at 2022-06-14 14:15:38.176530
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
  msg1 = Message(text = 'May not have more than 100 characters')
  msg2 = Message(text = 'May not have more than 100 characters')
  error1 = BaseError(messages = [msg1])
  error2 = BaseError(messages = [msg2])
  assert error1 == error2


# Generated at 2022-06-14 14:15:44.429834
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="Hello, world!") == BaseError(text="Hello, world!")
    assert BaseError(text="Hello, world!") != BaseError(text="Goodbye, world!")
    assert BaseError(text="Hello, world!") != BaseError(
        text="Hello, world!", code="greeting"
    )
    assert BaseError(text="Hello, world!", code="greeting") != BaseError(
        text="Hello, world!", code="farewell"
    )
    assert BaseError(text="Hello, world!", code="greeting") != BaseError(
        text="Goodbye, world!", code="greeting"
    )
    assert BaseError(text="Hello, world!", key="planet") != BaseError(
        text="Hello, world!", key="world"
    )
    assert Base

# Generated at 2022-06-14 14:15:55.108683
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    act = Message(text='a', code='my_code', index=[1, 2, 3], start_position=1, end_position=2)
    actual = Message(text='a', code='my_code', index=[1, 2, 3], start_position=1, end_position=2)
    expe = Message(text='b', code='my_code', index=[1, 2, 3], start_position=1, end_position=2)
    assert __ == act
    assert __ == act
    assert __ != expe
    assert __ != expe
    assert __ != expe
    assert __ != expe
    assert __ != expe
    assert __ != expe
    assert __ != expe
    assert __ != expe



# Generated at 2022-06-14 14:16:02.142918
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test 1
    message1 = Message(text = "error message", code = "custom")
    message2 = Message(text = "error message", code = "custom")
    result = message1.__eq__(message2)
    assert result == True

    # Test 2
    message2 = Message(text = "error message2", code = "custom")
    result = message1.__eq__(message2)
    assert result == False
    assert message1.text == "error message"
    assert message1.code == "custom"

    # Test 3
    message2 = Message(text = "error message", code = "custom2")
    result = message1.__eq__(message2)
    assert result == False
    assert message1.text == "error message"
    assert message1.code == "custom"

# Unit test

# Generated at 2022-06-14 14:16:11.919405
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    print("Test Message.__eq__()")
    assert Message(text="test", code="test", position = Position(0,0,0)) == Message(text="test", code="test", position = Position(0,0,0))
    assert Message(text="test1", code="test1", position = Position(0,0,0)) != Message(text="test2", code="test1", position = Position(0,0,0))
    assert Message(text="test1", code="test1", position = Position(0,0,0)) != Message(text="test1", code="test2", position = Position(0,0,0))
    assert Message(text="test", code="test", position = Position(0,0,0)) != Message(text="test", code="test", position = Position(0,0,1))
    #pass

# Generated at 2022-06-14 14:16:22.096360
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error = BaseError(
        text='Invalid value "{key}"', code='invalid', key='username', position=Position(line_no=1, column_no=1, char_index=1))
    assert error == BaseError(
        text='Invalid value "{key}"', code='invalid', key='username', position=Position(line_no=1, column_no=1, char_index=1))
    assert error != BaseError(
        text='Invalid value "{key}"', code='invalid', key='password', position=Position(line_no=1, column_no=1, char_index=1))
    assert error != BaseError(
        text='Invalid value "{key}"', code='invalid', key='username', position=Position(line_no=1, column_no=1, char_index=2))

# Generated at 2022-06-14 14:16:32.189089
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    text1 = "May not have more than 100 characters"
    code1 = "max_length"
    key1 = "username"
    message1 = Message(text=text1, code=code1, key=key1)
    BaseError_1 = BaseError(text=text1, code=code1, key=key1)
    messages1=[]
    messages1.append(message1)
    BaseError_2 = BaseError(messages=messages1)
    assert BaseError_1 == BaseError_2
    text2 = "May not have more than 100 characters"
    code2 = "max_length"
    key2 = "username"
    message2 = Message(text=text2, code=code2, key=key2)

# Generated at 2022-06-14 14:16:53.174191
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    assert str(BaseError(text='foo')) == 'foo'
    assert str(BaseError(text='foo bar', code='invalid_type')) == 'foo bar'
    assert str(BaseError(messages=[Message(text='foo')])) == "{'': 'foo'}"
    assert str(
        BaseError(messages=[Message(text='foo', index=['foo', 'bar'])])
    ) == "{'foo': {'bar': 'foo'}}"
    assert str(
        BaseError(messages=[Message(text='foo', index=['foo', 'bar', 3])])
    ) == "{'foo': {'bar': {3: 'foo'}}}"

# Generated at 2022-06-14 14:17:04.700068
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    # Non-nested error
    error = ValidationError(text='The value is invalid.')
    assert str(error) == "The value is invalid."

    # Nested errors
    error = ValidationError(
        messages=[
            Message(text='The value is invalid.', code='invalid', index=[]),
            Message(
                text='The value must be an integer.', code='invalid_type', index=[]
            ),
            Message(text='The value is too big.', code='max_value', index=[]),
        ]
    )
    assert (
        str(error)
        == "{'': 'The value is invalid.', '_schema_errors': {'': ['The value must be an integer.', 'The value is too big.']}}"
    )

    # Nested errors, with keys


# Generated at 2022-06-14 14:17:15.558614
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    e = BaseError()
    assert str(e) == "{}"

    e = BaseError(key="username")
    assert str(e) == "\"\""

    e = BaseError(text="Failed")
    assert str(e) == "Failed"

    e = BaseError(messages=[Message(text="foo", key="username")])
    assert str(e) == "{\"username\": \"foo\"}"

    e = BaseError(messages=[Message(text="bar", key="password")])
    assert str(e) == "{\"password\": \"bar\"}"

    e = BaseError(
        messages=[Message(text="foo", key="username"), Message(text="bar", key="password")]
    )
    assert str(e) == "{\"username\": \"foo\", \"password\": \"bar\"}"

    e = Base

# Generated at 2022-06-14 14:17:23.124297
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    error: BaseError = ValidationError(messages=[Message(text="Invalid date")])

    str_error = str(error)
    if str_error == '{\'\': \'Invalid date\'}':
        print('SUCCESS: BaseError.__str__()')
    else:
        print(f'ERROR: BaseError.__str__(): str(error)={str_error}')



# Generated at 2022-06-14 14:17:27.444450
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    with pytest.raises(AssertionError):
        assert Message("text", code="code") == None

    message1 = Message("text", code="code")
    message2 = Message("text", code="code")
    assert message1 == message2


# Generated at 2022-06-14 14:17:35.234948
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    line_no_1, column_no_1, char_index_1 = 1, 2, 3
    line_no_2, column_no_2, char_index_2 = 4, 5, 6
    position_1 = Position(line_no_1, column_no_1, char_index_1)
    position_2 = Position(line_no_2, column_no_2, char_index_2)

    text = 'Error Message'
    code = 'Error Code'
    key = 'Key'
    index = [key]
    message_1 = Message(
        text = text,
        code = code,
        key = key,
        position = position_1
    )

# Generated at 2022-06-14 14:17:44.163286
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    text = "text"
    code = "code"
    index = ["index"]
    start_position = Position(line_no=0, column_no=0, char_index=0)
    end_position = Position(line_no=0, column_no=10, char_index=10)
    message1 = Message(text=text, code=code, index=index, start_position=start_position, end_position=end_position)
    message2 = Message(text=text, code=code, index=index, start_position=start_position, end_position=end_position)
    assert message1.__eq__(message2)


# Generated at 2022-06-14 14:17:50.333889
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    """Unit test for method __str__ of class BaseError
    
    """
    print("Testing __str__ in BaseError")
    msg = Message(text='username is required')
    err = ValidationError(messages=[msg])
    assert str(err) == "'username is required'"
    print("PASS")


if __name__ == "__main__":
    test_BaseError___str__()

# Generated at 2022-06-14 14:17:57.988688
# Unit test for method __eq__ of class Message

# Generated at 2022-06-14 14:18:08.827681
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text = 'May not have more than 100 characters',code = 'max_length',key = 'username', position = Position(line_no= 1, column_no = 1, char_index = 1))
    message2 = Message(text = 'May not have more than 100 characters',code = 'max_length',key = 'username', position = Position(line_no= 1, column_no = 1, char_index = 1))
    message3 = Message(text = 'May not have more than 100 characters',code = 'min_length',key = 'username', position = Position(line_no= 1, column_no = 1, char_index = 1))

# Generated at 2022-06-14 14:18:14.694568
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    p1 = Position(1, 2, 3)
    p2 = Position(1, 2, 4)
    assert p1 == p1
    assert p2 == p2
    assert not (p1 == p2)


# Generated at 2022-06-14 14:18:24.417871
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    x = Message(text = "test", code = "code", key = "key", index = ["index"], start_position = Position(line_no = 1,column_no = 1,char_index = 1), end_position = Position(line_no = 3,column_no = 1,char_index = 1))
    y = Message(text = "test", code = "code", key = "key", index = ["index"], start_position = Position(line_no = 1,column_no = 1,char_index = 1), end_position = Position(line_no = 3,column_no = 1,char_index = 1))
    assert x.__eq__(y)


# Generated at 2022-06-14 14:18:28.996729
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg = Message(text="Hello", code="hello", key=None)
    assert msg == msg
    assert msg == Message(text="Hello", code="hello", key=None)
    assert msg != Message(text="Hello", code="hello", key="world")
    assert msg != Message(text="Hello", code="hello")


# Generated at 2022-06-14 14:18:32.511728
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert (Message(text="a", code=None, key=None, index=None, position=None,
                    start_position=None, end_position=None)) == (Message(text="a",
                    code=None, key=None, index=None, position=None, start_position=None,
                    end_position=None))


# Generated at 2022-06-14 14:18:35.987124
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="error", code="code")
    msg2 = Message(text="error", code="code")
    assert msg1 == msg2


# Generated at 2022-06-14 14:18:40.473148
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Create first object
    message1 = Message(
        text = "Max length of title is 15 characters"
    )

    # Create second object
    message2 = Message(
        text = "Max length of title is 15 characters"
    )

    # Assert that both are equal
    assert message1 == message2


# Generated at 2022-06-14 14:18:44.621988
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text='Some error message.', code='minLength', index=['field'])
    m2 = Message(text='Some error message.', code='minLength', index=['field'])
    assert m1 == m2


# Generated at 2022-06-14 14:18:56.269524
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    from copy import deepcopy

    test_cases = [
        {
            "test_case_name":  "Equivalent",
            "text": "test",
            "code": "test",
            "index": ["test"],
            "start_position": Position(1, 1, 0),
            "end_position": Position(1, 10, 9),
        },
        {
            "test_case_name": "Not Equivalent",
            "text": "test",
            "code": "test",
            "index": ["test"],
            "start_position": Position(2, 2, 0),
            "end_position": Position(2, 11, 9),
        },
    ]


# Generated at 2022-06-14 14:19:06.668376
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="text1", code="code1", index=['index1'], start_position=Position(1,2,3), end_position=Position(4,5,6))
    message2 = Message(text="text1", code="code1", index=['index1'], start_position=Position(1,2,3), end_position=Position(4,5,6))
    message3 = Message(text="text3", code="code3", index=['index3'], start_position=Position(7,8,9), end_position=Position(10,11,12))
    assert (message1 == message2) is True
    assert (message1 == message3) is False


# Generated at 2022-06-14 14:19:18.014558
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    some_code = "some_code"
    some_key = "some_key"
    some_index = ["some_index"]
    some_text = "some_text"
    some_start_position = Position(line_no=1, column_no=1, char_index=1)
    some_end_position = Position(line_no=2, column_no=2, char_index=2)
    object1 = Message(text=some_text, code=some_code, key=some_key, index=some_index,
                      start_position=some_start_position, end_position=some_end_position)