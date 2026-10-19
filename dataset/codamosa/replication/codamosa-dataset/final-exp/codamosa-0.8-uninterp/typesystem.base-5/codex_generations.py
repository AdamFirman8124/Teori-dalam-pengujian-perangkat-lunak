

# Generated at 2022-06-14 14:12:59.508471
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    validation_result = ValidationResult(value=int(1))
    # Test __iter__ of class ValidationResult when condition if self.error is not None is not satisfied
    assert 1 in validation_result
    assert None not in validation_result
    # Test __iter__ of class ValidationResult when condition if self.error is not None is satisfied
    validation_result = ValidationResult(error=ValidationError())
    assert validation_result.error in validation_result
    assert validation_result.value not in validation_result


# Generated at 2022-06-14 14:13:07.566642
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # arrange
    message1 = Message(text='1', code='1', key='1', start_position=Position(1, 1, 1), end_position=Position(1, 1, 1))
    message2 = Message(text='2', code='2', key='2', start_position=Position(2, 2, 2), end_position=Position(2, 2, 2))
    # act
    message1 == message2
    # assert
    assert False == (message1 == message2)



# Generated at 2022-06-14 14:13:16.456802
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    v = ValidationResult()
    assert v.value is None
    assert v.error is None
    [value, error] = v
    assert value is None
    assert error is None

    v = ValidationResult(value=1)
    assert v.value == 1
    assert v.error is None
    [value, error] = v
    assert value == 1
    assert error is None

    v = ValidationResult(error=ValidationError(text='xx'))
    assert v.value is None
    assert isinstance(v.error, ValidationError)
    [value, error] = v
    assert value is None
    assert isinstance(error, ValidationError)

    v = ValidationResult(value=1, error=ValidationError(text='xx'))
    assert v.value is None

# Generated at 2022-06-14 14:13:20.141514
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr = ValidationResult(value='Hello World')
    assert list(vr) == ['Hello World', None]

    vr = ValidationResult(error='Error')
    assert list(vr) == [None, 'Error']


# Generated at 2022-06-14 14:13:22.895965
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result = ValidationResult(value=1)
    values = []
    for value in result:
        values.append(value)
    assert values == [1, None]


# Generated at 2022-06-14 14:13:28.557198
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    r = ValidationResult(value=None, error=ValueError)
    assert next(iter(r)) == r.value
    assert next(iter(r)) == r.error
    with pytest.raises(StopIteration):
        next(iter(r))
    assert list(r) == [r.value, r.error]

# Generated at 2022-06-14 14:13:33.994043
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    a, b = ValidationResult(value=1, error=None)
    assert a == 1
    assert b == None

    a, b = ValidationResult(value=None, error=ValidationError(text='error1'))
    assert a == None
    assert b.text == 'error1'


# Generated at 2022-06-14 14:13:34.696918
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr = ValidationResult()
    list(vr)



# Generated at 2022-06-14 14:13:38.172749
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr = ValidationResult(value=1.0, error=ValidationError(text='error'))
    l = []
    for el in vr:
        l.append(el)
    assert l == [1.0, ValidationError(text='error')]


# Generated at 2022-06-14 14:13:42.146850
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    message = Message(text='test', code='test', index = ['test'])
    error = BaseError(messages = [message])
    error1 = BaseError(messages = [message])
    assert error == error1


# Generated at 2022-06-14 14:13:52.362404
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    expected_output = True
    result = Message('text=1', code='code', index = ['index'], position = Position(1,2,3)) == Message('text=1', code='code', index = ['index'], position = Position(1,2,3))
    if result == expected_output:
        print("test__Message___eq__: PASS")
    else:
        print("test__Message___eq__: FAIL")
        

# Generated at 2022-06-14 14:13:57.519075
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    msg1 = Message(text='text1', code='code1', index=['index1'])
    msg2 = Message(text='text2', code='code2', index=['index2'])
    error1 = ValidationError(messages=[msg1, msg2])
    error2 = ValidationError(messages=[msg1, msg2])
    assert error1 == error2



# Generated at 2022-06-14 14:13:59.764893
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    """Test for method __eq__ of class BaseError"""
    raise NotImplementedError()


# Generated at 2022-06-14 14:14:11.067983
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError() == BaseError()
    assert BaseError(text="") == BaseError(text="")
    assert BaseError(text="") != BaseError(text="")
    assert BaseError(text="", code="") == BaseError(text="",code="")
    assert BaseError(text="", code="") != BaseError(text="",code="")
    assert BaseError(text="", key="") == BaseError(text="", key="")
    assert BaseError(text="", key="") != BaseError(text="", key="")
    assert BaseError(text="", position="") == BaseError(text="", position="")
    assert BaseError(text="", position="") != BaseError(text="", position="")
    assert BaseError(messages="") == BaseError(messages="")

# Generated at 2022-06-14 14:14:21.225999
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message.__eq__(
        Message(text="msg", code="code", key="key",  position=Position(1,1,1)),
        Message(text="msg", code="code", key="key",  position=Position(1,1,1))
    )
    assert not Message.__eq__(
        Message(text="msg1", code="code1", key="key",  position=Position(1,1,1)),
        Message(text="msg2", code="code2", key="key",  position=Position(2,2,2))
    )


# Generated at 2022-06-14 14:14:30.353028
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    message_1 = Message(text='test', code='test', index=['test'], position=Position(0, 0, 0))
    message_2 = Message(text='test', code='test', index=['test'], position=Position(0, 0, 0))
    message_3 = Message(text='test', code='test', index=['test'], position=Position(0, 0, 0))
    message_4 = Message(text='test', code='test', index=['test'], position=Position(0, 0, 0))
    message_5 = Message(text='test', code='test', index=['test'], position=Position(0, 0, 0))
    message_6 = Message(text='test', code='test', index=['test'], position=Position(0, 0, 0))

# Generated at 2022-06-14 14:14:38.260106
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    def assert_eq(e1, e2):
        assert e1 == e2
        assert e2 == e1
        assert e1.__hash__() == e2.__hash__()

    # Same messages, same exact order.

# Generated at 2022-06-14 14:14:49.607353
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    with pytest.raises(AssertionError):
        msg = Message(text='text', code='code', index=['key'])
        BaseError(messages=[msg])

    with pytest.raises(AssertionError):
        msg = Message(text='text', code='code', index=['key'])
        BaseError(text='text', code='code', key='key', messages=[msg])

    msg = Message(text='text', code='code', index=['key'])
    error = BaseError(messages=[msg])
    assert error == error
    assert error == BaseError(messages=[msg])
    assert error != BaseError(messages=[Message(text='text', code='code', index=['key'])])
    assert error != BaseError(messages=[msg, msg])
    assert error != BaseError

# Generated at 2022-06-14 14:14:53.709253
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error_1 = BaseError(text='test_message', code='test_code', key='test_key')
    error_2 = BaseError(text='test_message', code='test_code', key='test_key-1')
    assert error_1 != error_2


# Generated at 2022-06-14 14:15:05.669286
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    messages1 = [Message(position=Position(1, 2, 3), text="abc")]
    messages2 = [Message(position=Position(1, 2, 3), text="def")]
    messages3 = [Message(position=Position(1, 2, 4), text="abc")]
    messages4 = [Message(position=Position(1, 2, 3), text="abc"),
                Message(position=Position(1, 2, 3), text="abc")]

    base_error1 = BaseError(messages=messages1)
    base_error2 = BaseError(messages=messages1)
    assert base_error1 == base_error2

    base_error1 = BaseError(messages=messages1)
    base_error2 = BaseError(messages=messages2)
    assert base_error1 != base_

# Generated at 2022-06-14 14:15:26.420928
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="This is an error message", code="error", key="key1", index=[1], position=Position(line_no=1, column_no=1, char_index=3))
    msg2 = Message(text="This is an error message", code="error", key="key1", index=[1], position=Position(line_no=1, column_no=1, char_index=3))
    assert msg1 == msg2

    msg1 = Message(text="This is an error message", code="error", key="key1", index=[1], position=Position(line_no=1, column_no=1, char_index=3))

# Generated at 2022-06-14 14:15:34.090038
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="May not have more than 100 characters", code="max_length") == Message(text="May not have more than 100 characters", code="max_length")
    assert Message(text="May not have more than 100 characters", code="max_length") != Message(text="May not have more than 100 characters", code="min_length")
    assert Message(text="May not have more than 100 characters", code="max_length") != Message(text="May not have more than 100 characters")
    assert Message(text="May not have more than 100 characters", index=[1, "username"]) == Message(text="May not have more than 100 characters", index=[1, "username"])

# Generated at 2022-06-14 14:15:36.536739
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Equals itself
    msg = Message(text=None, code=None, key=None, index=None, position=None, start_position=None, end_position=None)
    assert msg == msg


# Generated at 2022-06-14 14:15:44.473434
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='dummy') != 1

    assert Message(text='dummy') == Message(text='dummy')
    assert Message(text='dummy') != Message(text='dummy_')
    assert Message(text='dummy') != Message(text='dummy', code='custom')
    assert Message(text='dummy', code='custom') != Message(text='dummy', code='custom_')
    assert Message(text='dummy', code='custom') != Message(text='dummy', code='custom', key='key')
    assert Message(text='dummy', code='custom', key='key') != Message(text='dummy', code='custom', key='key_')
    assert Message(text='dummy', code='custom', key='key') != Message(text='dummy', code='custom', key='key', index=[])

# Generated at 2022-06-14 14:15:50.010839
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="", code="", key=None, index=None, position=None, start_position=None, end_position=None) == Message(text="", code="", key=None, index=None, position=None, start_position=None, end_position=None)

# Generated at 2022-06-14 14:15:59.091788
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='e1') == Message(text='e1')
    assert Message(text='e1') != Message(text='e2')
    assert Message(text='e1', code='c1') == Message(text='e1', code='c1')
    assert Message(text='e1', code='c1') != Message(text='e1', code='c2')
    assert Message(text='e1', code='c1', key='k1') == Message(text='e1', code='c1', key='k1')
    assert Message(text='e1', code='c1', key='k1') != Message(text='e1', code='c1', key='k2')

# Generated at 2022-06-14 14:16:02.410838
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="test", code="test", key="test")
    m2 = Message(text="test", code="test", key="test")
    assert m1 == m2


# Generated at 2022-06-14 14:16:12.090566
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="text", code="code", index=[1, "key"], start_position=Position(0, 0, 0), end_position=Position(0, 0, 27))
    assert m1.text == "text"
    assert m1.code == "code"
    assert m1.index == [1, "key"]
    assert m1.start_position.line_no == 0
    assert m1.start_position.column_no == 0
    assert m1.start_position.char_index == 0
    assert m1.end_position.line_no == 0
    assert m1.end_position.column_no == 0
    assert m1.end_position.char_index == 27

# Generated at 2022-06-14 14:16:22.160818
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text='abc', code='abc', key='abc', index=[1, 2, 3], position=Position(1, 2, 3), start_position=Position(1, 2, 3), end_position=Position(1, 2, 3))
    m2 = Message(text='abc', code='abc', key='abc', index=[1, 2, 3], position=Position(1, 2, 3), start_position=Position(1, 2, 3), end_position=Position(1, 2, 3))
    m3 = Message(text='abc', code='abc', key='abc', index=[1, 2, 3], position=Position(1, 2, 3), start_position=Position(1, 2, 3), end_position=Position(4, 5, 6))
    assert m1 == m2
    assert m1 != m3


# Generated at 2022-06-14 14:16:32.188264
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m = Message(text="May not have more than 100 characters", code="max_length", key="username")

    assert m == Message(text="May not have more than 100 characters", code="max_length", key="username")
    assert m != Message(text="May not have more than 50 characters", code="max_length", key="username")
    assert m != Message(text="May not have more than 100 characters", code="min_length", key="username")
    assert m != Message(text="May not have more than 100 characters", code="max_length", key="password")
    assert m != Message(text="May not have more than 100 characters", code="max_length", index=["users", "username"])
    assert m != Message(text="May not have more than 100 characters", code="max_length", position=Position(0, 0, 0))


# Generated at 2022-06-14 14:16:50.167825
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert (Message(text="May not have more than 100 characters", code="max_length")==Message(text="May not have more than 100 characters", code="max_length"))
    assert not (Message(text="May not have more than 100 characters", code="max_length")==Message(text="May not have more than 100 characters", code="min_length"))
    assert not (Message(text="May not have more than 100 characters", code="max_length")==Message(text="May not have more than 100 characters", code=None))
    assert not (Message(text="May not have more than 100 characters", code="max_length")==dict())
    assert not (Message(text="May not have more than 100 characters", code="max_length")==None)

# Generated at 2022-06-14 14:16:57.395422
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    from typing import cast

    assert Message(text='foo') == Message(text='foo')
    assert Message(text='foo', code='bar') == Message(text='foo', code='bar')
    assert Message(text='foo', index=['bar']) == Message(text='foo', index=['bar'])
    assert Message(text='foo', position=cast(Position, None)) == Message(text='foo', position=cast(Position, None))

    assert Message(text='foo') != Message(text='bar')
    assert Message(text='foo', code='bar') != Message(text='foo', code='123')
    assert Message(text='foo', index=['bar']) != Message(text='foo', index=['123'])

# Generated at 2022-06-14 14:17:02.015677
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="foo", code="bar")
    message2 = Message(text="foo", code="baz")
    message3 = Message(text="foo", code="baz")
    assert message1 != message2
    assert message2 == message3


# Generated at 2022-06-14 14:17:13.725767
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text='text', code='code', key='key', position='position', start_position='start_position', end_position='end_position')
    message2 = Message(text='text', code='code', key='key', position='position', start_position='start_position', end_position='end_position')
    message3 = Message(text='text1', code='code1', key='key1', position='position', start_position='start_position', end_position='end_position')
    message4 = Message(text='text', code='code', key='key', position='position1', start_position='start_position', end_position='end_position')
    message5 = Message(text='text', code='code', key='key', position='position', start_position='start_position1', end_position='end_position')

# Generated at 2022-06-14 14:17:16.627904
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1=Message(text="error text 1", code="error code 1", key=1, position=Position(1,2,3))
    message2=Message(text="error text 1", code="error code 1", key=1, position=Position(1,2,3))
    message3=Message(text="error text 1", code="error code 3", key=1, position=Position(1,2,3))
    
    assert message1 == message2
    assert not message1 == message3
    assert not message1 == "not a message"


# Generated at 2022-06-14 14:17:21.009109
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text="text", code="code", index=["index"])
    message_ = Message(text="text", code="code", index=["index"])
    assert message == message_


# Generated at 2022-06-14 14:17:31.723186
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg = Message(text='test', code='test_code', index=['index0', 'index1'], start_position=Position(1, 2, 3), end_position=Position(4, 5, 6))
    msg1 = Message(text='test', code='test_code', index=['index0', 'index1'], start_position=Position(1, 2, 3), end_position=Position(4, 5, 6))
    msg2 = Message(text='test', code='test_code1', index=['index0', 'index1'], start_position=Position(1, 2, 3), end_position=Position(4, 5, 6))

# Generated at 2022-06-14 14:17:43.362464
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(
        text="May not have more than 100 characters", code="max_length"
    ) == Message(
        text="May not have more than 100 characters", code="max_length"
    )
    assert Message(text="Must be a string", code="string") == Message(
        text="Must be a string", code="string"
    )
    assert Message(text="Not a boolean", code="boolean") == Message(
        text="Not a boolean", code="boolean"
    )
    assert Message(text="Not a number", code="number") == Message(
        text="Not a number", code="number"
    )
    assert Message(text="Not a date-time", code="datetime") == Message(
        text="Not a date-time", code="datetime"
    )

# Generated at 2022-06-14 14:17:48.874901
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="hello world", code="custom", position=Position(1,1,1)) == Message(text="hello world", code="custom", position=Position(1,1,1))
    assert Message(text="hello world", code="custom", position=Position(1,1,1)) != Message(text="hello world", code="custom", position=Position(1,1,2))
    assert Message(text="hello world", code="custom", position=Position(1,1,1)) != Message(text="hello world", code="abcd", position=Position(1,1,1))
    assert Message(text="hello world", code="custom", position=Position(1,1,1)) != Message(text="abcdefg", code="custom", position=Position(1,1,1))

test_Message___eq__()

# Generated at 2022-06-14 14:17:57.246821
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='msg') == Message(text='msg')
    assert Message(text='msg 1', code='custom') == Message(text='msg 1', code='custom')
    assert Message(text='msg 2', code='custom', key='name') == Message(text='msg 2', code='custom', key='name')
    assert Message(text='msg 3', code='custom', index=['index']) == Message(text='msg 3', code='custom', index=['index'])
    assert Message(text='msg 4', code='custom', position=Position(1,1,1)) == Message(text='msg 4', code='custom', position=Position(1,1,1))
    assert Message(text='msg 5', code='custom', start_position=Position(1,1,1), end_position=Position(1,1,2)) == Message

# Generated at 2022-06-14 14:18:05.437729
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='', code='', key=0, index=[]) == Message(text='', code='', key=0, index=[])


# Generated at 2022-06-14 14:18:07.184118
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text = 'hello', code='hi', key='awesome')
    assert (message == message) is True

# Generated at 2022-06-14 14:18:08.746884
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # TODO: write unit test for method __eq__ of class Message
    pass


# Generated at 2022-06-14 14:18:19.301131
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    """
    Test the function Message.__eq__(self, other)
    """
    pos = Position(5, 1, 2)
    message_1 = Message(text='May not have more than 100 characters', code='max_length',
                            index = ['users', 3, 'username'], start_position = pos, end_position = pos)
    message_2 = Message(text='May not have more than 100 characters', code='max_length',
                            index = ['users', 3, 'username'], start_position = pos, end_position = pos)
    # test the case where two messages are equal
    assert message_1 == message_2
    # test the case where two messages have different code

# Generated at 2022-06-14 14:18:23.057898
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='message') == Message(text='message', code='custom')
    assert not (Message(text='message', code='custom') == 'message')
    assert Message(text='message', code='custom') != 'message'


# Generated at 2022-06-14 14:18:32.273477
# Unit test for method __eq__ of class Message

# Generated at 2022-06-14 14:18:34.151100
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    print("test_Message___eq__")
    pass


# Generated at 2022-06-14 14:18:42.982959
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="text", code="code", index=[1], position=Position(1, 2, 3))
    m2 = Message(text="text", code="code", index=[1], position=Position(1, 2, 3))
    m3 = Message(text="text", code="code", index=[1], position=Position(4, 2, 3))
    m4 = Message(text="text", code="code", index=[1], position=Position(4, 5, 3))
    assert m1 == m2
    assert m2 == m1
    assert m1 != m3
    assert m3 != m1
    assert m1 != m4
    assert m4 != m1


# Generated at 2022-06-14 14:18:46.487476
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="This is a test message")
    msg2 = Message(text="This is a test message")
    assert msg1 == msg2

# Generated at 2022-06-14 14:18:53.083953
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    error1 = Message("error1", "error1", "error1", ["error1"], Position(5,5,5), Position(5,5,5), Position(5,5,5))
    error2 = Message("error1", "error1", "error1", ["error1"], Position(5,5,5), Position(5,5,5), Position(5,5,5))
    print(error1 == error2)



# Generated at 2022-06-14 14:19:10.489993
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text = 'a', code = 'b', key = 'c', index = [1,2,3], position = Position(line_no = 1, column_no = 2, char_index = 3))
    message2 = Message(text = 'a', code = 'b', key = 'c', index = [1,2,3], position = Position(line_no = 1, column_no = 2, char_index = 3))
    message3 = Message(text = 'a1', code = 'b1', key = 'c1', index = [1,2,3], position = Position(line_no = 1, column_no = 2, char_index = 3))
    assert message == message2
    assert message != message3

# Generated at 2022-06-14 14:19:13.984245
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    arg1 = Message(text="Hello, World!", code="test")
    arg2 = Message(text="Hello, World!", code="test")
    assert arg1 == arg2


# Generated at 2022-06-14 14:19:20.427013
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="test_1", code="test_2", key="test_3", index=["test_4"])
    m2 = Message(text="test_1", code="test_2", key="test_3", index=["test_4"])
    m3 = Message(text="test_9", code="test_8", key="test_7", index=["test_6"])
    assert m1 == m2
    assert not m1 == m3


# Generated at 2022-06-14 14:19:22.164036
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message('error message', 'error code', 'key', [])
    assert message == message
    assert message != Message('error message', 'error code', None, [])


# Generated at 2022-06-14 14:19:28.324117
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Message with position
    _message_1 = Message(text='1', start_position=Position(1, 1, 1))
    _message_2 = Message(text='1', start_position=Position(1, 1, 1))
    assert (_message_1 == _message_2)

    _message_2 = Message(text='2', start_position=Position(1, 1, 1))
    assert not (_message_1 == _message_2)

    _message_2 = Message(text='1', start_position=Position(2, 1, 1))
    assert not (_message_1 == _message_2)

    _message_2 = Message(text='1', start_position=Position(1, 2, 1))
    assert not (_message_1 == _message_2)


# Generated at 2022-06-14 14:19:37.203581
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Setup
    text = "text"
    code = "code"
    key = "key"
    position = Position(line_no=1, column_no=2, char_index=3)
    start_position = Position(line_no=3, column_no=2, char_index=1)
    end_position = Position(line_no=4, column_no=5, char_index=6)
    message = Message(
        text=text,
        code=code,
        key=key,
        position=position,
        start_position=start_position,
        end_position=end_position,
    )
    # Execute

# Generated at 2022-06-14 14:19:42.586572
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='May not have more than 100 characters', code='max_length', key=None, position=None, index=None, start_position=None, end_position=None) == Message(text='May not have more than 100 characters', code='max_length', key=None, position=None, index=None, start_position=None, end_position=None)


# Generated at 2022-06-14 14:19:49.864758
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='text1').__eq__(Message(text='text2')) == False
    assert Message(text='text1').__eq__(Message(text='text1')) == True
    assert Message(text='text1').__eq__(Message(text='text1', code='code2')) == False
    assert Message(text='text1').__eq__(Message(text='text1', code='code1')) == True
    assert Message(text='text1').__eq__(Message(text='text1', key='key2')) == False
    assert Message(text='text1').__eq__(Message(text='text1', key='key1')) == True
    assert Message(text='text1').__eq__(Message(text='text1', index=['index2'])) == False

# Generated at 2022-06-14 14:19:51.120744
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    pass # Nothing to test


# Generated at 2022-06-14 14:19:58.599654
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text='text',
                   code='code',
                   index=[5],
                   start_position=Position(1,1,1),
                   end_position=Position(1,1,1))
    msg2 = Message(text='text',
                   code='code',
                   index=[5],
                   start_position=Position(1,1,1),
                   end_position=Position(1,1,1))
    assert(msg1 == msg2)
