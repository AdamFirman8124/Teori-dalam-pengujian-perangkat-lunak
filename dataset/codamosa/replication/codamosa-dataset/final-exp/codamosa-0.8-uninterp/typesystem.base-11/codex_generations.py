

# Generated at 2022-06-14 14:12:57.376117
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = None
    b = None
    assert (Message(text="A", code="custom") == Message(text="A", code="custom")) is True
    assert (Message(text="A", code="custom") == Message(text="B", code="custom")) is False
    assert (Message(text="A", code="custom") == Message(text="A", code="bar")) is False
    assert (Message(text="A", code="custom") == Message(text="A", code="custom", key="foo")) is False
    assert (Message(text="A") == Message(text="A")) is True
    assert (Message(text="A", position=Position(1, 2, 3)) == Message(text="A", start_position=Position(1, 2, 3), end_position=Position(1, 2, 3))) is True

# Generated at 2022-06-14 14:12:59.352555
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    instance = Position(1,2,3)
    assert instance == Position(1,2,3)


# Generated at 2022-06-14 14:13:01.519171
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result = ValidationResult(value=None)
    assert iter(result) == iter((None, None))



# Generated at 2022-06-14 14:13:02.994304
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value = 1
    error = ValidationError(code="test", text="test")
    result = ValidationResult(value=value, error=error)
    assert (next(result), next(result)) == (1, error)

# Generated at 2022-06-14 14:13:13.634102
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # given
    first = Position(1, 2, 3)
    second = Position(4, 5, 6)
    x = Position(1, 2, 3)
    y = Position(2, 2, 3)
    z = Position(1, 3, 3)
    a = Position(1, 2, 4)
    # when
    first_second = first.__eq__(second)
    first_x = first.__eq__(x)
    first_y = first.__eq__(y)
    first_z = first.__eq__(z)
    first_a = first.__eq__(a)
    # then
    assert not first_second
    assert first_x
    assert not first_y
    assert not first_z
    assert not first_a


# Generated at 2022-06-14 14:13:21.090184
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value1 = 1

    vr = ValidationResult(value = value1)
    it = iter(vr)
    assert next(it) == value1
    assert next(it) == None

    value2 = 2
    error2 = ValidationError(text = "test")

    vr = ValidationResult(value = value2, error = error2)
    it = iter(vr)
    assert next(it) == value2
    assert next(it) == error2


# Generated at 2022-06-14 14:13:27.022194
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result1 = ValidationResult()
    assert [result for result in result1] == [None, None]

    result2 = ValidationResult(value=[1, 2])
    assert [result for result in result2] == [[1, 2], None]

    result3 = ValidationResult(error=ValidationError())
    assert [result for result in result3] == [None, ValidationError()]


# Generated at 2022-06-14 14:13:31.583784
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr = ValidationResult(value=3)
    assert list(iter(vr)) == [3, None]
    vr = ValidationResult(error=ValidationError())
    assert list(iter(vr)) == [None, ValidationError()]

# Generated at 2022-06-14 14:13:39.463700
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    # empty object
    vr = ValidationResult()
    assert list(vr) == [None, None]
    # object with values
    vr = ValidationResult(value=1, error=ValidationError())
    assert list(vr) == [1, ValidationError()]
    # object with error
    vr = ValidationResult(error=ValidationError())
    assert list(vr) == [None, ValidationError()]
    # object with value
    vr = ValidationResult(value=1)
    assert list(vr) == [1, None]


# Generated at 2022-06-14 14:13:51.067126
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    test_objects = [
        Position(
            line_no=1, column_no=2, char_index=3
        ),
        Position(
            line_no=1, column_no=2, char_index=4
        ),
        Position(
            line_no=1, column_no=3, char_index=3
        ),
        Position(
            line_no=2, column_no=2, char_index=3
        ),
        Position(
            line_no=1, column_no=2, char_index=3
        )
    ]

# Generated at 2022-06-14 14:14:02.513296
# Unit test for constructor of class ParseError
def test_ParseError():
    error = ParseError(text="Invalid token", position=Position(1, 1, 2))
    assert error.messages() == [Message(text="Invalid token", position=Position(1, 1, 2))]

# Generated at 2022-06-14 14:14:12.589953
# Unit test for constructor of class ValidationError
def test_ValidationError():
    validation_error_instance = ValidationError(text='Test error message', code=None, key=None, position=None, messages=None)
    assert validation_error_instance.__init__(text='Test error message', code=None, key=None, position=None, messages=None)
    assert "{'error': 'Test error message'}"
    validation_error_instance = ValidationError(text=None, code=None, key=None, position=None, messages=['error1', 'error2', 'error3'])
    assert validation_error_instance.__init__(text=None, code=None, key=None, position=None, messages=['error1', 'error2', 'error3'])
    assert "{}"


# Generated at 2022-06-14 14:14:25.535059
# Unit test for constructor of class BaseError
def test_BaseError():
    with pytest.raises(ValueError, match="Either 'messages' must"):
        BaseError(text="hello", code="max_length", key="hello")
    with pytest.raises(ValueError, match="Either 'messages' must"):
        BaseError(messages=[])
    with pytest.raises(ValueError, match="Either 'messages' must"):
        BaseError(text="hello", code="max_length", messages=[])
    with pytest.raises(ValueError, match="Either 'messages' must"):
        BaseError(text="hello", key="hello", messages=[])
    with pytest.raises(ValueError, match="Either 'messages' must"):
        BaseError(text="hello", messages=[])

# Generated at 2022-06-14 14:14:29.091833
# Unit test for constructor of class ValidationError
def test_ValidationError():
    error = ValidationError(text='test')
    assert error._messages == [Message(text='test', code='custom')]
    assert error._message_dict == {'': 'test'}
    assert str(error) == 'test'
    assert repr(error) == "ValidationError('test', code='custom')"

# Generated at 2022-06-14 14:14:33.772486
# Unit test for constructor of class BaseError
def test_BaseError():
    BaseError()
    BaseError(messages=[])
    BaseError(text='Error mesasge', code='error_code', key='key', position=Position(1, 2, 3))
    BaseError(messages=[Message(text='Error mesasge', code='error_code', key='key', position=Position(1, 2, 3))])



# Generated at 2022-06-14 14:14:45.842258
# Unit test for constructor of class ValidationError
def test_ValidationError():
    error1 = ValidationError(text='not permitted')
    assert error1._messages == [Message(text='not permitted', code='custom')]
    assert error1._message_dict == {'': 'not permitted'}
    assert error1.messages() == [Message(text='not permitted', code='custom')]

    error2 = ValidationError(
        text='not permitted', code='custom', key='username'
    )
    assert error2._messages == [
        Message(text='not permitted', code='custom', key='username')
    ]
    assert error2._message_dict == {'username': 'not permitted'}
    assert error2.messages() == [
        Message(text='not permitted', code='custom', key='username')
    ]


# Generated at 2022-06-14 14:14:53.428794
# Unit test for constructor of class BaseError
def test_BaseError():
    assert BaseError(text='May not have more than 100 characters', code='max_length', key='username') == {'username': 'May not have more than 100 characters'}
    assert BaseError(text='Invalid email address',code='invalid_email',key='email_address') == {'email_address': 'Invalid email address'}
    assert len(BaseError(text='Invalid email address',code='invalid_email',key='email_address')) == 1
    assert BaseError(text='Invalid email address',code='invalid_email',key='email_address').messages(add_prefix='email') == [Message(text='Invalid email address', code='invalid_email', index=['email', 'email_address'])]

# Generated at 2022-06-14 14:14:58.456408
# Unit test for constructor of class ValidationError
def test_ValidationError():
    error = ValidationError(text='Sample Text', code='Sample Code', key='Sample Key', position='Sample Position')
    assert error.text == 'Sample Text'
    assert error.code == 'Sample Code'
    assert error.key == 'Sample Key'
    assert error.position == 'Sample Position'


# Generated at 2022-06-14 14:15:09.574235
# Unit test for constructor of class BaseError
def test_BaseError():
    error = BaseError(text='a')
    assert error.messages() == [Message(text='a', code='custom')]

    error = BaseError(text='a', code='b')
    assert error.messages() == [Message(text='a', code='b')]

    error = BaseError(text='a', code='b', key='c')
    assert error.messages() == [Message(text='a', code='b', key='c')]

    error = BaseError(messages=[Message(text='a', code='b')])
    assert error.messages() == [Message(text='a', code='b')]

    error = BaseError(
        messages=[Message(text='a', code='b')], key='c'
    )

# Generated at 2022-06-14 14:15:20.066871
# Unit test for constructor of class ValidationError
def test_ValidationError():
    exception = ValidationError(text="Hello world", code="code", key="key")
    assert exception["key"] == "Hello world"
    error_messages = [Message(text="Hello world", code="code", key="key")]
    exception2 = ValidationError(messages=error_messages)
    assert exception2["key"] == "Hello world"
    exception3 = ValidationError(text="Hello world", code="code")
    assert exception3[""] == "Hello world"
    error_messages3 = [Message(text="Hello world", code="code")]
    exception4 = ValidationError(messages=error_messages3)
    assert exception4[""] == "Hello world"


# Generated at 2022-06-14 14:15:32.577102
# Unit test for constructor of class ValidationError
def test_ValidationError():
    error = ValidationError(*[{Message}])
    assert error._messages == [{Message}]
    assert error._message_dict == {}


# Generated at 2022-06-14 14:15:40.878193
# Unit test for constructor of class BaseError
def test_BaseError():
    # Test with a single message
    err = BaseError(text="Hello World")
    assert dict(err) == {"": "Hello World"}
    assert err.messages() == [Message(text="Hello World", code="custom")]

    err = BaseError(text="Hello World", code="invalid")
    assert dict(err) == {"": "Hello World"}
    assert err.messages() == [Message(text="Hello World", code="invalid")]

    err = BaseError(text="Hello World", key="a_key")
    assert dict(err) == {"a_key": "Hello World"}
    assert err.messages() == [Message(text="Hello World", code="custom", key="a_key")]

    err = BaseError(text="Hello World", key=3)

# Generated at 2022-06-14 14:15:52.492646
# Unit test for constructor of class ValidationError
def test_ValidationError():
    # test in the case when messages is None
    err1 = ValidationError(text = "err1", code = "code1", key = "key1", position = "position1")
    # correct
    if err1.text == "err1" and err1.code == "code1" and err1.key == "key1" and err1.position == "position1":
        print("SUCEESS")
        
    # test in the case when messages is not None
    err2 = ValidationError(messages = ["text"])
    if err2.text == None and err2.code == None and err2.key == None and err2.position == None:
        print("SUCCESS")
    #print(err1)
    #print(err2)

test_ValidationError()

# Generated at 2022-06-14 14:15:57.024419
# Unit test for constructor of class ValidationError
def test_ValidationError():
    # Instantiated as a ValidationError with a single error message.
    error = ValidationError(text="May not have more than 100 characters", code="max_length", key="username")
    # Instantiated as a ValidationError with multiple error messages.
    error = ValidationError(messages=[Message(text="May not have more than 100 characters", code="max_length", key="username")])


# Generated at 2022-06-14 14:16:01.943709
# Unit test for constructor of class ParseError
def test_ParseError():
    with pytest.raises(AssertionError) as execinfo:
        ParseError(text="",code="",key="",messages=[])
    assert "can't be specified with" in str(execinfo.value)
    assert "messages" in str(execinfo.value)


# Generated at 2022-06-14 14:16:11.776971
# Unit test for constructor of class ValidationError
def test_ValidationError():
    # Test the constructor of class ValidationError with a single message
    text = 'user must be a string'
    code = 'must_be_string'
    key = 'user'
    error = ValidationError(text = text, code = code, key = key)
    assert error.text == text
    assert error.code == code
    assert error.key == key

    # Test the constructor of class ValidationError with multiple messages
    a = Message(text = 'user must be a string', code = 'must_be_string', key = 'user')
    b = Message(text = 'password must be a string', code = 'must_be_string', key = 'password')
    errors = [a, b]
    error = ValidationError(messages = errors)
    assert error.messages == errors


# Generated at 2022-06-14 14:16:22.307041
# Unit test for constructor of class ValidationError
def test_ValidationError():
    expected = ValidationError(text='invalid phone', code='invalid_phone')
    actual = ValidationError(text='invalid phone', code='invalid_phone')
    assert(expected == actual)

    expected = ValidationError(text='invalid phone', code='invalid_phone')
    actual = ValidationError(text='invalid phone', code='invalid_phone', key='phone')
    assert(expected != actual)

    expected = ValidationError(text='invalid phone', code='invalid_phone')
    actual = ValidationError(text='invalid phone', code='invalid_phone', position=Position(1,1,1))
    assert(expected != actual)


# Generated at 2022-06-14 14:16:32.308122
# Unit test for constructor of class ValidationError
def test_ValidationError():
    error = ValidationError(text='Error in data', code='invalid', key='mykey', position = Position(1, 2, 3))
    assert error.text == 'Error in data'
    assert error.code == 'invalid'
    assert error.key == 'mykey'
    assert error.position == Position(1, 2, 3)
    assert error.messages() == [Message(text='Error in data', code='invalid', key='mykey', position = Position(1, 2, 3))]
    assert error == ValidationError(messages=[Message(text='Error in data', code='invalid', key='mykey', position = Position(1, 2, 3))])

# Generated at 2022-06-14 14:16:43.807859
# Unit test for constructor of class ParseError
def test_ParseError():
    messages = [
        Message(
            text=f"{i}", code="test_code", key="test_key", position=Position(i, i, i)
        )
        for i in range(5)
    ]
    error = ParseError(messages=messages)
    assert len(error) == 5
    assert list(error) == ["0", "1", "2", "3", "4"]
    assert error[0] == "0"
    assert error[2] == "2"
    assert error[4] == "4"
    assert error["0"] == "0"
    assert error["2"] == "2"
    assert error["4"] == "4"
    assert error.messages() == messages

# Generated at 2022-06-14 14:16:47.695017
# Unit test for constructor of class ParseError
def test_ParseError():
    message = ParseError(text="Invalid data", code="invalid_data")
    assert message.messages() == [Message(text="Invalid data", code="invalid_data")]
    assert dict(message) == {"": "Invalid data"}
