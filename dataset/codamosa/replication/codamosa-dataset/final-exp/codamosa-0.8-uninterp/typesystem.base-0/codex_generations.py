

# Generated at 2022-06-14 14:12:51.776563
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result = ValidationResult(error='validation error')
    assert next(iter(result)) == result.value
    assert next(iter(result)) == result.error


# Generated at 2022-06-14 14:12:58.380407
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    from pprint import pprint
    from copy import deepcopy
    from typesystem import ValidationError
    a = ValidationError(text='f', code='g', key='h')
    b = ValidationError(text='f', code='g', key='h')
    c = ValidationError(text='i', code='j', key='k')
    print(a == b)
    print(a == c)


# Generated at 2022-06-14 14:13:05.942751
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    validationResult_1 = ValidationResult(value=None, error=None)
    assert iter(validationResult_1) == iter([None, None])

    validationResult_2 = ValidationResult(value=1, error=None)
    assert iter(validationResult_2) == iter([1, None])

    validationResult_3 = ValidationResult(value=None, error='error')
    assert iter(validationResult_3) == iter([None, 'error'])

# Generated at 2022-06-14 14:13:15.337622
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    from typesystem import Schema, String, Integer

    class User(Schema):
        name = String(min_length=1, max_length=20)
        age = Integer(minimum=0, maximum=130)

    try:
        value, error = User.validate_or_error({"name": "", "age": 1000})
    except ValidationError as e:
        assert error == e, "The first error was not equal to the error raised"
        error1 = error
    else:
        raise AssertionError("Did not raise a validation error")

    try:
        value, error = User.validate_or_error({"name": "", "age": 1000})
    except ValidationError as e:
        assert error == e, "The second error was not equal to the error raised"
        error2 = error

# Generated at 2022-06-14 14:13:17.217926
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    ValidationResult(error="typing").__iter__()
    ValidationResult(value=1).__iter__()

# Generated at 2022-06-14 14:13:19.677552
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    validation_result = ValidationResult(value={"value"})
    assert set(iter(validation_result)) == {{"value"}, None}

# Generated at 2022-06-14 14:13:26.405346
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    # Invalid case
    validation_result = ValidationResult()
    assert list(validation_result) == [None, None]
    # Valid case
    validation_result = ValidationResult(value=1)
    assert list(validation_result) == [1, None]
    # Valid case
    validation_result = ValidationResult(error=ValidationError(text="Error"))
    assert list(validation_result) == [None, ValidationError(text="Error")]


# Generated at 2022-06-14 14:13:31.378976
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr = ValidationResult(value=[1,2,3])
    l = list(vr)
    assert l == [vr.value, vr.error]
    assert l[0] == [1,2,3]
    assert l[1] == None


# Generated at 2022-06-14 14:13:36.279475
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    obj = ValidationResult(value = "value")
    el0 = next(iter(obj))
    el1 = next(iter(obj))

    return bool(el0) is True and bool(el1) is False


# Generated at 2022-06-14 14:13:42.967595
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    messages = [
        Message(
            text="foo",
            code="bar",
            key="baz",
            position=Position(line_no=1, column_no=2, char_index=3),
        )
    ]

    # If a single message is given an error, compare it with an error
    # with multiple messages containing the same message.
    error1 = BaseError(text="foo", code="bar", key="baz", position=Position(line_no=1, column_no=2, char_index=3))
    error2 = BaseError(messages=messages)
    assert error1 == error2

    # If multiple messages are given an error, compare it with an error
    # with a single message containing one of the given messages.
    error3 = BaseError(messages=messages)

# Generated at 2022-06-14 14:13:50.886442
# Unit test for constructor of class ParseError
def test_ParseError():
    try:
        raise ParseError(text="hello")
    except:
        import traceback
        info = traceback.format_exc()
        if "ParseError(text='hello')" in info:
            print("test_ParseError ok")
        else:
            print("test_ParseError fail")


# Generated at 2022-06-14 14:13:52.958103
# Unit test for constructor of class ValidationError
def test_ValidationError():
    msg = Message(text="This is a message")
    ValidationError(messages=[msg])
    ValidationError(text="This is a message")

# Generated at 2022-06-14 14:13:55.266842
# Unit test for constructor of class BaseError
def test_BaseError():
  error_generated_by_constructor = BaseError(
    text= 'error message'
  )
  assert error_generated_by_constructor.text == 'error message'

# Generated at 2022-06-14 14:14:00.334489
# Unit test for constructor of class BaseError
def test_BaseError():
    error = BaseError(key='key', text='text', code='code', position=Position(1, 1, 1))
    assert error.messages() == [Message(key='key', text='text', code='code', position=Position(1, 1, 1))]



# Generated at 2022-06-14 14:14:03.859120
# Unit test for constructor of class ValidationError
def test_ValidationError():
    msg = Message(text = "May not be empty", code = "null", key = "name")
    error = ValidationError(text = "empty", messages = [msg])
    assert error.messages() == [msg]

# Generated at 2022-06-14 14:14:06.594925
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError(text="Error text") == ParseError({
        "": "Error text",
    })


# Generated at 2022-06-14 14:14:10.646133
# Unit test for constructor of class BaseError
def test_BaseError():
    messages = [
        Message(text='May not have more than 100 characters', code='max_length', key='username')
    ]

    with pytest.raises(AssertionError):
        BaseError(text='May not have more than 100 characters', code='max_length', key='username', messages=messages)

    base_error = BaseError(messages=messages)

    assert len(base_error) == 1
    assert isinstance(base_error, Mapping)
    assert isinstance(base_error, dict)
    assert isinstance(base_error, Exception)
    assert isinstance(base_error, BaseError)

    # assert BaseError(messages=messages) == BaseError(messages=messages)

# Generated at 2022-06-14 14:14:14.493490
# Unit test for constructor of class ParseError
def test_ParseError():
    assert ParseError(text="abc") == ParseError([Message(text="abc")])
    assert ParseError(text="abc", code="cde") == ParseError([Message(text="abc", code="cde")])

# Generated at 2022-06-14 14:14:26.843595
# Unit test for constructor of class ValidationError
def test_ValidationError():
	error = ValidationError(text="Message ERROR")
	assert error.text == "Message ERROR"
	assert error.code == "custom"
	assert error.key == None
	assert error.position == None
	assert error.messages() == [Message(text="Message ERROR", code="custom", position=None, index=[])]
	
	error2 = ValidationError(messages=[Message(text="Message ERROR", code="custom", position=None, index=[])])
	assert error2.text == None
	assert error2.code == None
	assert error2.key == None
	assert error2.position == None
	assert error2.messages() == [Message(text="Message ERROR", code="custom", position=None, index=[])]

if __name__ == "__main__":
	test_ValidationError()

# Generated at 2022-06-14 14:14:30.872124
# Unit test for constructor of class ParseError
def test_ParseError():
    e = ParseError(text = "Not an int", code = "type_error", key = "age")
    assert e.messages() == [Message(text = "Not an int", code = "type_error", key = "age")]
    assert e == ParseError(messages = e.messages())


# Generated at 2022-06-14 14:14:34.712604
# Unit test for constructor of class ValidationError
def test_ValidationError():
    print(ValidationError(text='Single error message'))
    print(ValidationError(messages=[Message(text='Multiple error messages')]))

# Generated at 2022-06-14 14:14:35.832104
# Unit test for constructor of class ParseError
def test_ParseError():
    # Test constructor without parameters
    ParseError()


# Generated at 2022-06-14 14:14:36.595602
# Unit test for constructor of class ParseError
def test_ParseError():
    ParseError(text="error")


# Generated at 2022-06-14 14:14:47.296522
# Unit test for constructor of class BaseError
def test_BaseError():
    err = BaseError(messages=[Message(text="message1")])
    assert err._message_dict == {"": "message1"}

    err = BaseError(text="message1")
    assert err._message_dict == {"": "message1"}

    err = BaseError(text="message1", key="key")
    assert err._message_dict == {"key": "message1"}

    err = BaseError(
        text="message1",
        code="code",
        key="key",
        position=Position(1, 2, None),
    )
    assert err._message_dict == {"key": "message1"}



# Generated at 2022-06-14 14:14:54.288585
# Unit test for constructor of class ParseError
def test_ParseError():
    # Calling constructor with no argument
    with pytest.raises(TypeError) as excinfo:
        ParseError()
    assert "missing 1 required keyword-only argument: 'text'" in str(excinfo.value)
    # Calling constructor with 1 argument
    ParseError(text="test_message")
    # Calling constructor with 4 arguments
    ParseError(text="test_message", code="custom", key="test_key", position=Position(line_no=0, column_no=1, char_index=0))
    # Calling constructor with 5 arguments

# Generated at 2022-06-14 14:15:06.522207
# Unit test for constructor of class ParseError
def test_ParseError():

    def test():
        exc = ParseError(
            text='A bad thing happened',
            code='bad',
            key='foo',
            position=Position(line_no=10, column_no=20),
        )
        assert exc['foo'] == "A bad thing happened"
        assert exc.messages() == [
            Message(
                text='A bad thing happened',
                code='bad',
                index=['foo'],
                position=Position(line_no=10, column_no=20),
            )
        ]
        assert exc.messages(add_prefix='bar') == [
            Message(
                text='A bad thing happened',
                code='bad',
                index=['bar', 'foo'],
                position=Position(line_no=10, column_no=20),
            )
        ]

# Generated at 2022-06-14 14:15:17.364584
# Unit test for constructor of class ValidationError
def test_ValidationError():
    # Instantiated as a ValidationError with a single error message
    v = ValidationError(text='test_message', code='test_code', key='test_key')
    assert v['test_key'] == 'test_message'

    v = ValidationError(text='test_message', code='test_code', key='test_key', position=Position(1, 1, 1))
    assert v['test_key'] == 'test_message'

    v = ValidationError(text='test_message', code='test_code', key='test_key',
                        start_position=Position(1, 1, 1), end_position=Position(1, 1, 1))
    assert v['test_key'] == 'test_message'

    # Instantiated as a ValidationError with multiple error messages

# Generated at 2022-06-14 14:15:22.562258
# Unit test for constructor of class BaseError
def test_BaseError():
    data = {'value': {}}
    msg = 'error'
    obj = BaseError(text=msg, code=None, key='key', position=None, messages=None)
    data['value']['key'] = obj
    assert data['value']['key'][''] == msg

test_BaseError()


# Generated at 2022-06-14 14:15:28.116839
# Unit test for constructor of class BaseError
def test_BaseError():
    text_message = 'The field is not valid'
    code_message = 'invalid'
    key_message = 'field_name'

    # Verify that the message is properly constructed
    message = Message(text=text_message, code=code_message, key=key_message)
    assert message.text == text_message and message.code == code_message and message.index == [key_message]

# Generated at 2022-06-14 14:15:37.188903
# Unit test for constructor of class ValidationError
def test_ValidationError():
    v = ValidationError(text = "abc", code = "123", key = "456", index = ["1", "2", "3"], position = [1, 2], start_position = [1, 2, 3], end_position = [4, 5, 6], messages = ["a", "b", "c"])
    assert v == v
    assert v.messages == ["a", "b", "c"]
    assert v.__repr__() == "ValidationError(['a', 'b', 'c'])"
    assert v.__str__() == "{}"
    # Test constructor with only text, code, key
    v = ValidationError(text = "abc", code = "123", key = "456")