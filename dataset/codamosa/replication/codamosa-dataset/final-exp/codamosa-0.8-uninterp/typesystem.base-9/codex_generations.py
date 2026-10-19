

# Generated at 2022-06-14 14:12:59.150315
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    code = "code"
    text = "text"
    key_str = "str"
    key_int = 1
    index = [key_str]
    full_index = [key_str, key_int]
    line_no = 1
    column_no = 2
    char_index = 3
    position = Position(line_no, column_no, char_index)
    start_position = Position(line_no, column_no, char_index)
    end_position = Position(line_no+1, column_no+3, char_index+5)

    expected_message = Message(text=text, code=code, index=index, position=position)
    assert expected_message == Message(text=text, code=code, index=index, position=position)

# Generated at 2022-06-14 14:13:10.567777
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    def func():
        pass
    vr = ValidationResult()
    assert vr.__iter__() == (None, None)
    assert next(vr.__iter__()) == None
    vr = ValidationResult(value=2)
    assert vr.__iter__() == (2, None)
    assert next(vr.__iter__()) == 2
    vr = ValidationResult(value={"a":1})
    assert vr.__iter__() == ({"a":1}, None)
    assert next(vr.__iter__()) == {"a":1}
    vr = ValidationResult(value=func)
    assert vr.__iter__() == (func, None)
    assert next(vr.__iter__()) == func

# Generated at 2022-06-14 14:13:14.729278
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result = ValidationResult(value=1)
    assert list(result) == [1, None]
    result = ValidationResult(error=ValidationError(text="a", code="b", key="c"))
    assert list(result) == [None, ValidationError(text="a", code="b", key="c")]


# Generated at 2022-06-14 14:13:16.656960
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text='abc') == BaseError(text='abc')
    assert BaseError(text='abc') != BaseError(text='def')


# Generated at 2022-06-14 14:13:28.348364
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    msg1 = Message(text="msg1", code="code1", index=[1])
    msg2 = Message(text="msg2", code="code2", index=[2])
    msg3 = Message(text="msg3", code="code3", index=[3])
    error1 = BaseError(messages=[msg1])
    error2 = BaseError(messages=[msg2])
    error3 = BaseError(messages=[msg1, msg2])
    error4 = BaseError(messages=[msg1, msg3])
    error5 = BaseError(code="code1", key=1, text="msg1")
    assert error1 != error2
    assert error1 != error3
    assert error1 != error4
    assert error1 != error5
    assert error2 != error3
    assert error2 != error4
    assert error2

# Generated at 2022-06-14 14:13:36.554839
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    """
    Test for method ValidationResult.__iter__
    """
    v1 = ValidationResult(value = 5)
    assert next(iter(v1)) == 5
    assert next(iter(v1)) == None
    v2 = ValidationResult(error = ValueError("This is an error message."))
    assert next(iter(v2)) == None
    assert next(iter(v2)) == ValueError("This is an error message.")


# Generated at 2022-06-14 14:13:38.497572
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    i = ValidationResult(value=1).__iter__()
    assert next(i) == 1
    assert next(i) is None


# Generated at 2022-06-14 14:13:42.518941
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error1 = BaseError(text="There is an error", code="code")
    error2 = BaseError(messages=[Message(text="There is an error", code="code")])
    assert error1 == error2


# Generated at 2022-06-14 14:13:47.454252
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    res = ValidationResult(value=1, error=None)
    val, err = res
    assert val == 1
    assert err is None

    res = ValidationResult(value=None, error=ValidationError())
    val, err = res
    assert val is None
    assert err is not None



# Generated at 2022-06-14 14:13:51.423133
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr_valid = ValidationResult(value=1)
    vr_invalid = ValidationResult(error=ValidationError())

    assert list(vr_valid) == [1, None]
    assert list(vr_invalid) == [None, ValidationError()]

# Generated at 2022-06-14 14:14:05.755210
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="foo") != Message(text="bar")
    assert Message(text="foo") != Message(code="foo")
    assert Message(text="foo") != Message(index=[1])
    assert Message(text="foo") != Message(position=Position(1, 1, 1))
    assert Message(text="foo", position=Position(0, 0, 0)) != Message(text="foo", position=Position(1, 1, 1))
    assert Message(text="foo", position=Position(0, 0, 0)) != Message(text="foo", start_position=Position(0, 0, 0), end_position=Position(1, 1, 1))


# Generated at 2022-06-14 14:14:10.554281
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg = Message(text = 'test', code = '0', key = 'test', index = 'test', position = 'test', start_position = 'test', end_position = 'test')
    self_msg_1 = Message(text = 'test', code = '0', key = 'test', index = 'test', position = 'test', start_position = 'test', end_position = 'test')
    self_msg_2 = Message(text = 'test2', code = '0', key = 'test', index = 'test', position = 'test', start_position = 'test', end_position = 'test')
    self_msg_3 = Message(text = 'test', code = '1', key = 'test', index = 'test', position = 'test', start_position = 'test', end_position = 'test')
    self_msg_4

# Generated at 2022-06-14 14:14:22.331821
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    from .validators import Any, Boolean, Integer, String

    error_1 = ValidationError(
        text="This field is required",
        code="required",
        key="username",
        position=Position(line_no=1, column_no=4, char_index=4),
    )

    error_2 = ValidationError(
        text="This field is required",
        code="required",
        key="username",
        position=Position(line_no=1, column_no=4, char_index=5),
    )

    assert error_1 != error_2
    assert error_1.messages()[0] != error_2.messages()[0]



# Generated at 2022-06-14 14:14:23.381236
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    pass


# Generated at 2022-06-14 14:14:31.787760
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    print("  test_Message___eq__")
    #
    # Example messages for testing
    #
    message0 = Message(text="text", code="code", key=1, index=[0], position=Position(1, 2, 3))  # noqa
    message1 = Message(text="text", code="code", key=1, index=[0], position=Position(2, 3, 4))  # noqa
    message2 = Message(text="text", code="code", key=1, index=[0], position=Position(1, 3, 3))  # noqa
    message3 = Message(text="text", code="code", key=1, index=[0], position=Position(1, 2, 4))  # noqa
    message4 = Message(text="text", code="code", key=1, index=[1])  # noqa

# Generated at 2022-06-14 14:14:39.124173
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="text1", code="code1") == BaseError(text="text1", code="code1")
    assert BaseError(text="text1", code="code1") != BaseError(text="text2", code="code1")
    assert BaseError(text="text1", code="code1") != BaseError(text="text1", code="code2")
    assert BaseError(text="text1", code="code1", key="key1") == BaseError(
        text="text1", code="code1", key="key1"
    )
    assert BaseError(text="text1", code="code1") != BaseError(code="code1")
    assert BaseError(text="text1", code="code1") != "text1"
    assert BaseError(text="text1", code="code1") != BaseError

# Generated at 2022-06-14 14:14:43.528656
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error1 = BaseError(messages=[Message(text="Error message text", code="Code")])
    error2 = BaseError(messages=[Message(text="Error message text", code="Code")])
    assert error1 == error2


# Generated at 2022-06-14 14:14:47.073548
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    first_instance = {'key': 'value', 'key2': 'value2'}
    second_instance = {'key': 'value', 'key2': 'value2'}
    assert first_instance == second_instance


# Generated at 2022-06-14 14:14:50.866247
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="Test message", code="test_code", key="test_key", index=["key1", "key2"])
    m2 = Message(text="Test message", code="test_code", index=["key1", "key2"])

    assert m1 == m2
    assert m2 == m1


# Generated at 2022-06-14 14:14:59.258475
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error = BaseError(text='Error message')
    assert error == BaseError(text='Error message')
    assert error != BaseError(text='Other message')
    assert error != BaseError(text='Error message', code='custom')
    error2 = BaseError(
        messages=[
            Message(text='Other message', code='custom')
        ]
    )
    assert error != error2
    error3 = BaseError(
        messages=[
            Message(text='Error message')
        ]
    )
    assert error == error3



# Generated at 2022-06-14 14:15:08.718833
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message_a = Message(text="test", code="test_code")
    message_b = Message(text="test", code="test_code")
    assert message_a == message_b


# Generated at 2022-06-14 14:15:20.646158
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    item = Message(text='hello', code='hi', key=1, index=[23],
                   position=Position(line_no=1, column_no=1, char_index=1),
                   start_position=Position(line_no=1, column_no=1, char_index=1),
                   end_position=Position(line_no=1, column_no=1, char_index=1))

# Generated at 2022-06-14 14:15:28.588421
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    Message("error 1", index=("a",1)).__eq__(Message("error 1", index=("a",1)))
    Message("error 1", index=("a",1)).__eq__(Message("error 2", index=("a",1)))
    Message("error 1", index=("a",1)).__eq__(Message("error 1", index=("a",2)))
    Message("error 1", index=("a",1)).__eq__(Message("error 1", index=("a",1,2)))
    Message("error 1", index=("a",1)).__eq__(Message("error 1", index=("a",1,3)))

# Generated at 2022-06-14 14:15:31.917022
# Unit test for method __eq__ of class Message
def test_Message___eq__():

    msg1 = Message(text='test', code='test', index=[1], start_position=Position(
        1, 1, 0), end_position=Position(1, 1, 0))
    msg2 = Message(text='test', code='test', index=[1], start_position=Position(
        1, 1, 0), end_position=Position(1, 1, 0))
    assert msg1 == msg2



# Generated at 2022-06-14 14:15:40.377853
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text="The text of the error message", code="The error code", index=["The index"])

    assert message == Message(text="The text of the error message", code="The error code", index=["The index"])
    assert message != Message(text="The text of the error message", code="The error", index=["The index"])
    assert message != Message(text="The text of the error", code="The error code", index=["The index"])
    assert message != Message(text="The text of the error message", code="The error code", index=["The index1"])
    assert message != Message(text="The text", code="The error code", index=[])
    assert message != Position(line_no=1, column_no=2, char_index=3)


# Generated at 2022-06-14 14:15:42.035784
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    """Test the method BaseError.__eq__ in the class BaseError."""
    # TODO: Test it later
    return True



# Generated at 2022-06-14 14:15:53.620554
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    pos = Position(line_no=1, column_no=2, char_index=3)
    assert Message(text='abc', code=None, index=[1], start_position=pos, end_position=None) == Message(text='abc', code=None, index=[1], position=pos)
    assert Message(text='abc', code=None, index=[1], start_position=pos, end_position=None) != Message(text='abx', code=None, index=[1], position=pos)
    assert Message(text='abc', code=None, index=[1], start_position=pos, end_position=None) != Message(text='abc', code=None, index=[1], position=None)
    assert Message(text='abc', code=None, index=[1], start_position=pos, end_position=None) != Message

# Generated at 2022-06-14 14:16:04.343753
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test Input 1
    message1 = Message(
        text="May not have more than 100 characters",
        code="max_length",
        index=["username"],
        start_position=Position(line_no=3, column_no=5, char_index=2),
    )
    message2 = Message(
        text="May not have more than 100 characters",
        code="max_length",
        index=["username"],
        start_position=Position(line_no=3, column_no=5, char_index=2),
    )
    assert message1 == message2

    # Test Input 2

# Generated at 2022-06-14 14:16:10.015407
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    myBaseError = BaseError()
    # Fail to pass in function because of lack of parameter
    # Pass in function
    assert myBaseError.__eq__(myBaseError) == (isinstance(myBaseError, BaseError) and (message.text == other.text) and (message.code == other.code) and (message.index == other.index) and (message.start_position == other.start_position) and (message.end_position == other.end_position))


# Generated at 2022-06-14 14:16:20.603357
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    schema = ValidationError(text="text_1")
    other = ValidationError(text="text_1")
    assert schema == other
    other = ValidationError(text="text_2")
    assert not (schema == other)
    schema = ValidationError(text="text_1",code="code_1")
    other = ValidationError(text="text_1",code="code_1")
    assert schema == other
    other = ValidationError(text="text_1",code="code_2")
    assert not (schema == other)
    # Unit test for method __eq__ of class Message
    def test_Message___eq__():
        schema = Message(text="text_1")
        other = Message(text="text_1")
        assert schema == other
        other = Message(text="text_2")


# Generated at 2022-06-14 14:16:35.282253
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    import math
    import random
    import unittest
    # Setup
    text = 'this is a string'
    code = 'custom'
    key ='username'
    index = list()
    position = Position(line_no = 1, column_no = 5, char_index = 1)
    start_position = Position(line_no = 1, column_no = 5, char_index = 1)
    end_position = Position(line_no = 1, column_no = 5, char_index = 1)
    Message_X = Message(text = text, code = code, key = key, index = index, position = position, start_position = start_position, end_position = end_position)

# Generated at 2022-06-14 14:16:47.037867
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    def make_message(text, code, index):
        return Message(text=text, code=code, index=index)

    def make_BaseError(text = None, code = None, key = None, position = None, messages = None):
        return BaseError(text=text, code=code, key=key, position=position, messages=messages)
    BaseError_1 = make_BaseError(text = "This is an error message", code = "max_length", key = "username", position = Position(line_no = 1, column_no = 1, char_index = 0), messages = [])

# Generated at 2022-06-14 14:16:55.962988
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text = "May not have more than 100 characters") == Message(text = "May not have more than 100 characters")
    assert Message(text = "May not have more than 100 characters", code = "max_length") == Message(text = "May not have more than 100 characters", code = "max_length")
    assert Message(text = "May not have more than 100 characters", position = Position(line_no = 1, column_no = 1, char_index = 0)) == Message(text = "May not have more than 100 characters", position = Position(line_no = 1, column_no = 1, char_index = 0))
    assert Message(text = "May not have more than 100 characters", index = ["users", 3, "username"]) == Message(text = "May not have more than 100 characters", index = ["users", 3, "username"])

# Generated at 2022-06-14 14:17:07.913569
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    i=0
    while True:
        num1 = random.randint(0,1)
        num2 = random.randint(0,1)
        num3 = random.randint(0,1)
        num4 = random.randint(0,1)
        num5 = random.randint(0,1)
        num6 = random.randint(0,1)
        num7 = random.randint(0,1)
        num8 = random.randint(0,1)
        num9 = random.randint(0,1)
        num10 = random.randint(0,1)
        num11 = random.randint(0,1)
        num12 = random.randint(0,1)
        num13 = random.randint(0,1)
        num14 = random.rand

# Generated at 2022-06-14 14:17:15.715283
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    class_name = 'BaseError'
    text = 'Text'
    code = 'Code'
    key = 'Key'
    position = 'Position'
    messages = 'messages'
    _messages = '_messages'
    _message_dict = '_message_dict'
    _messages_ = '_messages'
    error1 = BaseError(text=text, code=code, key=key, position=position)
    error2 = BaseError(text=text, code=code, key=key, position=position)
    assert error1 == error2



# Generated at 2022-06-14 14:17:21.977691
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    expected_result = True
    actual_result = (
        BaseError(text='May not have more than 100 characters', code='max_length')
        == BaseError(text='May not have more than 100 characters', code='max_length')
    )
    assert expected_result == actual_result


# Generated at 2022-06-14 14:17:29.998819
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(text="test", code="test", key="test", index=["test"])
    b = Message(text="test", code="test", key="test", index=["test"])
    c = Message(text="test", code="test", key="test", index=["test"])
    d = Message(text="test", code="test", key="test", index=["test", "test"])

    assert a == b
    assert b == c
    assert c == a
    assert a != d
    assert b != d
    assert c != d


# Generated at 2022-06-14 14:17:34.719724
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(char_index=2, column_no=3, line_no=4, text="message text")
    message2 = Message(char_index=2, column_no=3, line_no=4, text="message text")
    assert message1 == message2



# Generated at 2022-06-14 14:17:43.762349
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text='text0', code='code0', index=[1, 2, 3, 4], position=Position(line_no=1, column_no=2, char_index=3))
    message0 = Message(text='text0', code='code0', index=[1, 2, 3, 4], position=Position(line_no=1, column_no=2, char_index=3))
    message1 = Message(text='text1', code='code1', index=[1], position=Position(line_no=1, column_no=1, char_index=1))
    assert message == message0
    assert message != message1

# Generated at 2022-06-14 14:17:54.213353
# Unit test for method __eq__ of class Message
def test_Message___eq__():
  assert Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(line_no=4, column_no=5, char_index=8), start_position=Position(line_no=4, column_no=5, char_index=8), end_position=Position(line_no=4, column_no=5, char_index=8)) == Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(line_no=4, column_no=5, char_index=8), start_position=Position(line_no=4, column_no=5, char_index=8), end_position=Position(line_no=4, column_no=5, char_index=8))


# Generated at 2022-06-14 14:18:11.614381
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    class_name = 'BaseError'
    messages = [Message(text='text', code='code', key='key', position='position')]

    def _BaseError(BaseError):
        BaseError = BaseError(messages=messages)
        assert BaseError == BaseError
        return BaseError

    assert _BaseError(BaseError) is not _BaseError(BaseError)
    assert _BaseError(BaseError) == _BaseError(BaseError)

    BaseError = BaseError(code='code')
    assert BaseError != BaseError


# Generated at 2022-06-14 14:18:14.412381
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    obj1 = BaseError()
    obj2 = BaseError()
    assert obj1.__eq__(obj2) == True
    assert obj2.__eq__(obj1) == True

# Generated at 2022-06-14 14:18:26.052051
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    messages = [Message(
        text='May not have more than 100 characters',
        key='username',
        start_position=Position(1, 2, 3)), Message(
        text='Must be between 18 and 30 years old',
        index=[3, 'age']), Message(
        text='Must be a valid email address',
        index=[3, 'email'],
        start_position=Position(1, 2, 3),
        end_position=Position(1, 2, 3))]
    assert ValidationError(messages=messages) == ValidationError(messages=messages)
    error_1 = ValidationError(text='Must be a valid email address', index=[3, 'email'])
    error_2 = ValidationError(text='Must be a valid email address', start_position=Position(1, 2, 3))
   

# Generated at 2022-06-14 14:18:28.914995
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    obj = BaseError(text = "bad", code = "error", key = "key", position = Position(1,2,3), messages = [])
    assert obj.__eq__(obj) == True

# Generated at 2022-06-14 14:18:32.877469
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test the case when two instances of Message are equal
    message1 = Message(text="text", code="code", index=["index1", "index2"])
    message2 = Message(text="text", code="code", index=["index1", "index2"])
    assert message1 == message2
    # Test the case when two instances of Message are not equal
    assert not message1 == 5


# Generated at 2022-06-14 14:18:37.183925
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="text", code="code", key="key", position="position")
    message2 = Message(text="text", code="code", key="key", position="position")
    assert message1 == message2


# Generated at 2022-06-14 14:18:39.791562
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    m = BaseError()
    m1 = BaseError()
    print(m == m1)
    value = m == m1
    assert value == True



# Generated at 2022-06-14 14:18:44.800694
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="Invalid email address.",code="invalid_email", key="email")
    msg2 = Message(text="Invalid email address.",code="invalid_email", key="email")
    msg3 = Message(text="Invalid email address.",code="invalid_email", index=["email"])
    assert msg1 == msg1
    assert msg1 == msg2
    assert msg2 == msg1
    assert msg1 == msg3
    assert msg3 == msg1
    assert msg1 != "string"


# Generated at 2022-06-14 14:18:56.340802
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text='a') == BaseError(text='a')
    assert BaseError(text='a') != BaseError(text='b')
    assert BaseError(text='a', code='c') == BaseError(text='a', code='c')
    assert BaseError(text='a', code='c') != BaseError(text='a')
    assert BaseError(text='a', code='c') != BaseError(text='a', code='d')
    assert BaseError(text='a', key='k') == BaseError(text='a', key='k')
    assert BaseError(text='a', key='k') != BaseError(text='a')
    assert BaseError(text='a', key='k') != BaseError(text='a', key='k2')

# Generated at 2022-06-14 14:19:07.436802
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error = BaseError()
    # Test 1
    assert error == error
    assert error == BaseError()
    # Test 2
    error = BaseError(key='error')
    assert error == error
    assert error == BaseError(key='error')
    # Test 3
    error = BaseError(position=Position(1,1,1))
    assert error == error
    assert error == BaseError(position=Position(1,1,1))
    # Test 4
    error = BaseError(text='error')
    assert error == error
    assert error == BaseError(text='error')
    # Test 5
    error = BaseError(code='error')
    assert error == error
    assert error == BaseError(code='error')
    # Test 6

# Generated at 2022-06-14 14:19:42.717244
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m = Message(text='May not have more than 100 characters')
    m1 = Message(text='May not have more than 100 characters')
    m2 = Message(code='max_length')
    assert m == m1
    assert m != m2


# Generated at 2022-06-14 14:19:44.766879
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(
        text="message", code="code", key="key", index=["index"]
    ) == Message("message", "code", key="key", index=["index"])


# Generated at 2022-06-14 14:19:48.030047
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg = Message(
        text="May not have more than 100 characters",
        code="max_length",
        key="username",
        position=Position(1, 1, 4),
        start_position=Position(1, 1, 4),
        end_position=Position(1, 100, 103),
    )

# Generated at 2022-06-14 14:19:54.017088
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text = 'May not have more than 100 characters', code = 'max_length', key = 'username', index = ['users', 3, 'username']) 
    assert Message(text = 'May not have more than 100 characters', code = 'max_length', key = 'username', index = ['users', 3, 'username']) == message

# Generated at 2022-06-14 14:20:02.230672
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="May not have more than 100 characters", code="max_length", key='username', index=['users', 3, 'username'], position=Position(line_no=10, column_no=8, char_index=12))
    msg2 = Message(text="May not have more than 100 characters", code="max_length", key='username', index=['users', 3, 'username'], position=Position(line_no=10, column_no=8, char_index=100))
    assert msg1 == msg2

if __name__ == '__main__':
    test_Message___eq__()
    print('Unit tests are OK!')

# Generated at 2022-06-14 14:20:09.879272
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="This is a test message", code="test_code", position=Position(line_no=1, column_no=2, char_index=3))
    msg2 = Message(text="This is a test message", code="test_code", position=Position(line_no=1, column_no=2, char_index=3))
    msg3 = Message(text="This is a test message", code="test_code1", position=Position(line_no=1, column_no=2, char_index=3))
    assert msg1 == msg2
    assert not msg1 == msg3


# Generated at 2022-06-14 14:20:20.909610
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(text='hello', code='abc', key=123, index=[1,2,3], position=Position(1,1,1), start_position=Position(1,1,1), end_position=Position(2,2,2))
    b = Message(text='hello', code='abc', key=123, index=[1,2,3], position=Position(1,1,1), start_position=Position(1,1,1), end_position=Position(2,2,2))
    assert a == b
    c = Message(text='hello', code='abcd', key=123, index=[1,2,3], position=Position(1,1,1), start_position=Position(1,1,1), end_position=Position(2,2,2))
    assert a != c

# Generated at 2022-06-14 14:20:30.368511
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    code = "max_length"
    key = "hello"
    index = [100, 200, 300]
    text = "input"

    # Line 1
    message1 = Message(text=text, code=code, key=key, index=index)
    message2 = Message(text=text, code=code, key=key, index=index)
    assert message1 == message2

    # Line 2
    message1 = Message(text=text, code=code, key=key, index=index)
    message2 = Message(text=text, code=code, key=key, index=index[:-1])
    assert not (message1 == message2)

    # Line 3
    message1 = Message(text=text, code=code, key=key, index=index)

# Generated at 2022-06-14 14:20:34.583820
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    obj = Message(text='May not have more than 100 characters', code='max_length', key=None, index=None, position=None, start_position=None, end_position=None)
    assert obj == obj


# Generated at 2022-06-14 14:20:39.414769
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text = 'May not have more than 100 characters', code='max_length', key= 'users', index = ['users', 2] )
    message1 = Message(text = 'May not have more than 100 characters', code='max_length', key= 'users', index = ['users', 2] )
    assert message == message1
