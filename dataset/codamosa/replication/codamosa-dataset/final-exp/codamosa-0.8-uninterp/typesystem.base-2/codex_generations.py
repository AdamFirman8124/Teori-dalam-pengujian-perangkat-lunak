

# Generated at 2022-06-14 14:12:54.643777
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    # Test Value
    value = "a"
    # Expected
    expected = ('a', None)
    # Actual
    actual = ValidationResult(value = value)
    # Compare
    assert actual == expected
    # Test Error
    error = "Error"
    # Expected
    expected = (None, 'Error')
    # Actual
    actual = ValidationResult(error = error)
    # Compare
    assert actual == expected


# Generated at 2022-06-14 14:12:59.250262
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value = "test"
    error = ValidationError()
    result = ValidationResult(value=value)
    result_with_error = ValidationResult(error=error)

    assert tuple(result) == (value, None)
    assert tuple(result_with_error) == (None, error)


# Generated at 2022-06-14 14:13:02.819241
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value_data = [1, 2, 3]
    value = ValidationResult(value=value_data)
    for i, val in enumerate(value):
        assert value_data[i] == val


# Generated at 2022-06-14 14:13:08.992420
# Unit test for method __str__ of class BaseError
def test_BaseError___str__():
    assert str(BaseError(text="Error message", code="test_code")) == "Error message"
    assert str(BaseError(messages=[Message(text="Error message 1", code="test_code_1"), Message(text="Error message 2", code="test_code_2")])) == "{'test_code_1': 'Error message 1', 'test_code_2': 'Error message 2'}"


# Generated at 2022-06-14 14:13:19.677260
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # __eq__ 1
    text = "May not have more than 100 characters"
    # __eq__ 1.1
    code = "max_length"
    # __eq__ 1.2
    key = "username"
    # __eq__ 1.3
    position = Position(line_no=12, column_no=21, char_index=123)

    # __eq__ 2
    text2 = "Required"
    # __eq__ 2.1
    code2 = "required"
    # __eq__ 2.2
    key2 = "password"
    # __eq__ 2.3
    position2 = Position(line_no=1, column_no=2, char_index=3)


# Generated at 2022-06-14 14:13:31.583688
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error1 = BaseError(text="Missing username")
    error2 = BaseError(text="Missing username")
    assert error1 == error2
    assert not (error1 != error2)

    error3 = BaseError(text="Missing username", code="missing_username")
    assert error1 != error3
    assert not (error1 == error3)

    error4 = BaseError(text="Missing username", key="username")
    assert error1 != error4
    assert not (error1 == error4)

    error5 = BaseError(text="Missing password", key="password")
    assert error1 != error5
    assert not (error1 == error5)

    error6 = BaseError(text="Missing password", key="password", position=Position(1, 2, 3))
    assert error5 != error6

# Generated at 2022-06-14 14:13:37.411959
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    v = ValidationResult()
    assert list(v) == [None, None]
    v = ValidationResult(value="foo")
    assert list(v) == ["foo", None]
    v = ValidationResult(error=ValidationError("bar"))
    assert list(v) == [None, ValidationError("bar")]

# Generated at 2022-06-14 14:13:42.401548
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    validation_result: ValidationResult = ValidationResult(value=123)
    value, error = validation_result
    assert value == 123
    assert error is None

    validation_result: ValidationResult = ValidationResult(error='my error')
    value, error = validation_result
    assert value is None
    assert error == 'my error'

# Generated at 2022-06-14 14:13:47.733572
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    v = ValidationResult()
    assert list(v) == [None, None]
    v = ValidationResult(value=5)
    assert list(v) == [5, None]
    v = ValidationResult(error=ValidationError())
    assert list(v) == [None, ValidationError()]


# Generated at 2022-06-14 14:13:57.084867
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    from random import randint
    from unittest import TestCase

    class TestValidationResult(TestCase):
        def test1(self):
            for _ in range(int(1e4)):
                a = randint(0,1)
                if a == 1:
                    v1 = randint(0,1e6)
                    v2 = None
                else:
                    v1 = None
                    v2 = randint(0,1e6)
                t = ValidationResult(value = v1, error = v2)
                it = iter(t)
                self.assertIsInstance(it, typing.Iterator)
                self.assertIsInstance(next(it), int)
                self.assertIsInstance(next(it), int)

    TestValidationResult().test1()


# Generated at 2022-06-14 14:14:06.086712
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    BaseError(code=None, key=None, position=None, text='Invalid type', key=None, code=None, text='Invalid type', position=None)


# Generated at 2022-06-14 14:14:18.605308
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    class TestBaseError:
        def __init__(self, text, code, key):
            self._messages = [Message(text, code, key)]
            self._message_dict = {key: text}
        def messages(self, *, add_prefix=None):
            if add_prefix is not None:
                return [Message(self._messages[0].text, self._messages[0].code, [add_prefix] + self._messages[0].index)]
            return list(self._messages)
        def __iter__(self):
            return iter(self._message_dict)
        def __len__(self):
            return len(self._message_dict)
        def __getitem__(self, key):
            return self._message_dict[key]

# Generated at 2022-06-14 14:14:25.491472
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text="text", code="code", key="key", position=Position(1, 1, 1))
    message_1 = Message(text="text", code="code", key="key", position=Position(1, 1, 1))
    message_2 = Message(text="text2", code="code2", key="key2", position=Position(1, 1, 1))
    print(message == message_1)
    print(message == message_2)
    print(message == "message")


# Generated at 2022-06-14 14:14:32.957340
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # case 1
    test_input_1 = {
        text: "test1",
        code: "test2",
        key: "test3",
        position: "test4",
        messages: "test5",
    }
    obj = BaseError(**test_input_1)
    test_input_2 = {
        text: "test6",
        code: "test7",
        key: "test8",
        position: "test9",
        messages: "test10",
    }
    other = BaseError(**test_input_2)
    test_output = obj == other
    assert test_output == False

    # case 2

# Generated at 2022-06-14 14:14:34.169556
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    """
    need to add test case
    """


# Generated at 2022-06-14 14:14:36.902237
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    msg1 = Message(text="abc", code="custom")
    msg2 = Message(text="xyz", code="custom")
    msg3 = Message(text="xyz", code="custom")

    assert msg2 == msg3
    assert msg1 != msg2

# Generated at 2022-06-14 14:14:49.367480
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # No error
    e = BaseError()
    assert e == e
    # Single error with no index
    e = BaseError(text='abc',code='xyz')
    e2 = BaseError(text='abc',code='xyz')
    assert e == e2
    # Multiple errors
    e = BaseError(messages=[Message(text='abc',code='xyz'), Message(text='abc',code='xyz')])
    e2 = BaseError(messages=[Message(text='abc',code='xyz'), Message(text='abc',code='xyz')])
    assert e == e2
    # Single error with index
    e = BaseError(text='abc',index=[123])
    e2 = BaseError(text='abc',index=[123])
    assert e == e2


# Generated at 2022-06-14 14:15:00.962119
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    a = BaseError(text="message", code="code", key="key", position=Position(1, 2, 3))
    b = BaseError(text="message", code="code", key="key", position=Position(1, 2, 3))
    assert a == b

    c = BaseError(text="message", code="code", key="key", position=Position(1, 2, 3))
    d = BaseError(text="message", code="code_diff", key="key_diff", position=Position(1, 2, 3))
    assert c != d

    e = BaseError(text="message", code="code", key="key", position=Position(1, 2, 3))
    f = BaseError(text="message", code="code", key="key", position=Position(1, 2, 4))
    assert e != f


# Unit

# Generated at 2022-06-14 14:15:07.910829
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # A BaseError that has different index, attributes index and messages are different, method __eq__ should return False
    message = Message(code = 'schema_error', key = 'age.1')
    error = BaseError(messages = [message])
    message = Message(code = 'schema_error', key = 'age.0')
    error_ = BaseError(messages = [message])
    assert error == error_ == False
    assert error != error_ == True


# Generated at 2022-06-14 14:15:11.122919
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text = "May not have more than 100 characters", code = "max_length", position = Position(line_no = 1, column_no = 1, char_index = 1))
    assert message.__eq__(message) == True


# Generated at 2022-06-14 14:15:25.861777
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    message = Message(
        text='Request failed with status code 400',
        code='http',
        key=None,
        index=None,
        start_position=None,
        end_position=None,
    )

    _message = [message]

    _message_dict = {}
    _message_dict[''] = message.text

    error = ValidationError(text='Request failed with status code 400', code='http', key=None)

    assert error._messages == _message
    assert error._message_dict == _message_dict
    assert isinstance(error, BaseError)
    assert error.messages() == [message]
    assert list(error) == ['']
    assert error[''] == 'Request failed with status code 400'

# Generated at 2022-06-14 14:15:28.874075
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    messages = [Message(text="A", code="a"), Message(text="B", code="b")]
    error1 = BaseError(messages=messages)
    error2 = BaseError(messages=messages)
    assert error1 == error2


# Generated at 2022-06-14 14:15:36.247681
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    _data = {"_messages": [{"text": "text1", "code": "code1", "key": "key1", "index": ["index1"], "position": {"line_no": 1, "column_no": 1, "char_index": 1}, "start_position": {"line_no": 1, "column_no": 1, "char_index": 1}, "end_position": {"line_no": 1, "column_no": 1, "char_index": 1}}]}
    _validator = lambda obj: (BaseError(**obj) if isinstance(obj, dict) else None)
    obj = _validator(_data)

# Generated at 2022-06-14 14:15:44.393356
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="X") == BaseError(text="X")
    assert BaseError(text="X") != BaseError(text="Y")
    assert BaseError(text="X", code="a") == BaseError(text="X", code="a")
    assert BaseError(text="X", code="a") != BaseError(text="Y", code="a")
    assert BaseError(text="X", code="a") != BaseError(text="X", code="b")
    assert BaseError(
        text="X", code="a", key="key"
    ) == BaseError(text="X", code="a", key="key")
    assert BaseError(
        text="X", code="a", key="key"
    ) != BaseError(text="Y", code="a", key="key")

# Generated at 2022-06-14 14:15:55.063737
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    message1 = Message(text="May not have more than 100 characters", code="max_length",key="username",index=['users',3,'username'],start_position=Position(line_no=1, column_no=4, char_index=4), end_position=Position(line_no=1, column_no=4, char_index=4))
    message2 = Message(text="May not have more than 100 characters", code="max_length",key="username",index=['users',3,'username'],start_position=Position(line_no=1, column_no=4, char_index=4), end_position=Position(line_no=1, column_no=4, char_index=4))
    assert message1 == message2

# Generated at 2022-06-14 14:15:59.571932
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    m1 = Message('May not have more than 100 characters', code='max_length')
    m2 = Message('May not have more than 100 characters', code='max_length')
    e1 = BaseError(messages=[m1])
    e2 = BaseError(messages=[m2])
    assert e1 == e2


# Generated at 2022-06-14 14:16:10.056856
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="foo") == Message(text="foo", code="custom")
    assert Message(text="foo") == Message(text="foo", code="custom", start_position=Position(0, 0, 0), end_position=Position(0, 0, 3))
    assert Message(text="foo", index=[1]) == Message(text="foo", code="custom", key=1)
    assert Message(text="foo") != Message(text="foo", code="other")
    assert Message(text="foo") != Message(text="foo", index=[1])
    assert Message(text="foo") != Message(text="foo", code="custom", start_position=Position(0, 0, 0), end_position=Position(0, 0, 3))

# Generated at 2022-06-14 14:16:16.048969
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # Create objects with the same property values
    message1 = Message(text="error message 1", code="code1")
    message2 = Message(text="error message 2", code="code2")
    error1 = BaseError(messages=[message1, message2])
    error2 = BaseError(messages=[message1, message2])

    # Compare objects
    assert (error1 == error2) == True

# Generated at 2022-06-14 14:16:24.205383
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # Test for BaseError(text='', code='', key=None, messages=None), BaseError(text='', code='', key=None, messages=None)
    assert BaseError(text='', code='', key=None, messages=None) == BaseError(text='', code='', key=None, messages=None)
    # Test for BaseError(text='a', code='', key=None, messages=None), BaseError(text='', code='', key=None, messages=None)
    assert not BaseError(text='a', code='', key=None, messages=None) == BaseError(text='', code='', key=None, messages=None)
    # Test for BaseError(text='', code='', key=None, messages=None), BaseError(text='a', code='', key=None, messages=None)

# Generated at 2022-06-14 14:16:26.955990
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    obj1 = ValidationError()
    obj2 = ValidationError()

    assert obj1 == obj1
    assert obj1 == obj2
    assert obj2 == obj1

# Generated at 2022-06-14 14:16:44.699162
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="foo") == Message(text="foo")
    assert Message(text="foo") != Message(text="bar")
    assert Message(text="foo") != Message(text="foo", code="bar")
    assert Message(text="foo", index=["key1", "key2"]) != Message(
        text="foo", index=["key1", "key3"]
    )
    assert Message(text="foo", index=["key1", "key2"]) != Message(
        text="foo", index=["key1", "key2", "key3"]
    )
    assert Message(
        text="foo", start_position=Position(1, 2, 3)
    ) == Message(text="foo", start_position=Position(1, 2, 3))

# Generated at 2022-06-14 14:16:49.543522
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert not (BaseError() == BaseError())
    assert not (BaseError() == BaseError(text="1"))
    assert not (BaseError(text="1") == BaseError(text="1", code="2"))
    assert BaseError(text="1", code="2") == BaseError(text="1", code="2")


# Generated at 2022-06-14 14:16:57.136673
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert ValidationError(text="Test 1", code="my_code_1") == ValidationError(text="Test 1", code="my_code_1")
    assert ValidationError(text="Test 2", code="my_code_2") != ValidationError(text="Test 1", code="my_code_1")

    assert ValidationError(text="Test 3", code="my_code_3", key=42) == ValidationError(text="Test 3", code="my_code_3", key=42)
    assert ValidationError(text="Test 4", code="my_code_4", key="user_name") == ValidationError(text="Test 4", code="my_code_4", key="user_name")
    assert ValidationError(text="Test 5", code="my_code_5", key=42) != ValidationError

# Generated at 2022-06-14 14:17:00.397576
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error = BaseError(text = "Hey", code = "custom", key = "username")
    result = error.__eq__(error)
    assert result == True



# Generated at 2022-06-14 14:17:12.033208
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    schema = {
        "type": "object",
        "properties": {
            "baz": {"type": "string"}
        },
    }
    s = json_schema(schema)
    a = BaseError(
        text="bar",
        code="max_length",
        key="foo",
        position=Position(line_no=0, column_no=1, char_index=1),
    )
    b = BaseError(
        text="bar",
        code="max_length",
        key="foo",
        position=Position(line_no=0, column_no=1, char_index=1),
    )

    # Unit test for method __eq__ in class BaseError
    assert a == b
    assert not a == s
    assert not a == "bar"
    assert a == a


# Generated at 2022-06-14 14:17:19.793482
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # Arrange
    arg1 = BaseError()
    arg2 = BaseError()
    arg3 = BaseError(text='error message', key='username')
    arg4 = BaseError(text='error message', key='username')
    arg5 = BaseError(text='error message', key='password')
    arg6 = BaseError(messages=[Message(text='error message', key='username')])
    arg7 = BaseError(messages=[Message(text='error message', key='username')])
    arg8 = BaseError(messages=[Message(text='error message', key='password')])
    expect_true = [
        (arg1, arg2), (arg3, arg4), (arg6, arg7),
    ]

# Generated at 2022-06-14 14:17:22.971597
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="error") == BaseError(text="error")
    assert BaseError(text="error") != BaseError(text="another error")

# Generated at 2022-06-14 14:17:32.654270
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error1 = BaseError(text='May not have more than 100 characters', code='max_length', key='username', position=Position(4, 5, 7))
    error2 = BaseError(text='May not have more than 100 characters', code='max_length', key='username', position=Position(4, 5, 7))
    assert error1 == error2
    error1 = BaseError(messages=[Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(4, 5, 7))])
    error2 = BaseError(messages=[Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(4, 5, 7))])
    assert error1 == error2


# Generated at 2022-06-14 14:17:37.397339
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text='test', code='test', key='test', index=[], position=None)
    m2 = Message(text='test', code='test', key='test', index=[], position=None)
    assert m1 == m2
    assert m2 == m1

# Generated at 2022-06-14 14:17:38.521861
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError() == BaseError()

# Generated at 2022-06-14 14:17:54.602292
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError() == BaseError()
    assert BaseError(text='aaa') == BaseError(text='aaa')
    assert BaseError(text='aaa', code='bbb') == BaseError(text='aaa', code='bbb')
    assert BaseError(text='aaa', code='bbb', key='ccc') == BaseError(text='aaa', code='bbb', key='ccc')
    assert BaseError(text='aaa', code='bbb', index=[]) == BaseError(text='aaa', code='bbb', key=None)
    assert BaseError(text='aaa', code='bbb', key='ccc', index=['ccc']) == BaseError(text='aaa', code='bbb', key='ccc')

# Generated at 2022-06-14 14:18:05.287979
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # True
    msg = Message(
        text="May not have more than 100 characters", 
        code="max_length", 
        start_position=Position(line_no=1, column_no=1, char_index=1),
        end_position=Position(line_no=1, column_no=1, char_index=2)
    )
    msg2 = Message(
        text="May not have more than 100 characters", 
        code="max_length", 
        start_position=Position(line_no=1, column_no=1, char_index=1),
        end_position=Position(line_no=1, column_no=1, char_index=2)
    )
    assert msg == msg2
    # False

# Generated at 2022-06-14 14:18:12.647174
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    e1 = BaseError(text="a")
    e2 = BaseError(text="a")
    assert e1==e2
    e1 = BaseError(text="a")
    e2 = BaseError(text="b")
    assert not(e1==e2)
    e1 = BaseError(text="a")
    e2 = BaseError(text="b", code="abc")
    assert not(e1==e2)
    e1 = BaseError(text="a")
    e2 = BaseError(text="a", code="abc")
    assert not(e1==e2)
    e1 = BaseError(text="a", code="abc")
    e2 = BaseError(text="a", code="abc")
    assert e1==e2

# Generated at 2022-06-14 14:18:22.306330
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(text='a', code='c', key='k', position='p')
    assert a == a
    assert a == Message(text='a', code='c', key='k', position='p')
    assert a != Message(text='b', code='c', key='k', position='p')
    assert a != Message(text='a', code='d', key='k', position='p')
    assert a != Message(text='a', code='c', key='l', position='p')
    assert a != Message(text='a', code='c', key='k', position='q')
    assert a != 'a' and a != 1

# Generated at 2022-06-14 14:18:29.250799
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    first = Message(text="text", code="code", key="key")
    assert first == Message(text="text", code="code", key="key")
    assert first != Message(text="text", code="code", key="key2")
    assert first != Message(text="text", code="code2", key="key")
    assert first != Message(text="text2", code="code", key="key")
    assert first != Message(text="text1", code="code1", key="key1", index=["a", "b"])


# Generated at 2022-06-14 14:18:40.604858
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    a = Message(text="a")
    b = Message(text="b")

    assert a != b
    assert b != a
    
    assert BaseError(messages=[a]) != BaseError(messages=[a])
    assert BaseError(messages=[a]) == BaseError(messages=[a])
    assert BaseError(messages=[a]) != BaseError(messages=[a, b])
    assert BaseError(messages=[a]) != BaseError(messages=[b])
    assert BaseError(messages=[a, b]) != BaseError(messages=[a])
    assert BaseError(messages=[a, b]) != BaseError(messages=[b, a])
    assert BaseError(messages=[a, b]) == BaseError(messages=[a, b])

# Generated at 2022-06-14 14:18:47.207135
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error1 = BaseError()
    error2 = BaseError()
    error3 = BaseError(text="An error message")
    error4 = BaseError(text="An error message")
    error5 = BaseError(text="Another error message")
    assert error1 == error2
    assert error3 == error3
    assert error3 == error4
    assert error3 != error5


# Generated at 2022-06-14 14:18:57.365879
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="a") == BaseError(text="a")
    assert BaseError(text="a", code="b") == BaseError(text="a", code="b")
    assert BaseError(text="a", key="b") == BaseError(text="a", key="b")
    assert BaseError(text="a", position="b") != BaseError(text="a")
    assert BaseError(text="a") != BaseError(text="b")
    assert BaseError(text="a", code="b") != BaseError(text="a")
    assert BaseError(text="a", code="b") != BaseError(text="a", code="c")
    assert BaseError(text="a", key="b") != BaseError(text="a", key="c")


# Generated at 2022-06-14 14:18:58.716564
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError() == BaseError()


test_BaseError___eq__()

# Generated at 2022-06-14 14:19:04.847981
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    message = Message(text="No message text")
    with pytest.raises(
        AssertionError,
        match="Assertion failed. Expected = None. Actual = No message text.",
    ):
        raise ValidationError(messages=[message])



# Generated at 2022-06-14 14:19:24.789200
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    #assert BaseError(text="ERROR_1") == BaseError(text="ERROR_1")
    assert BaseError(text="ERROR_1", code="CODE_1") == BaseError(text="ERROR_1", code="CODE_1")
    assert BaseError(text="ERROR_1", code="OTHER_ERROR", key=1) == BaseError(text="ERROR_1", code="OTHER_ERROR", key=1)
    assert BaseError(text="ERROR_1", code="OTHER_ERROR", key=1) != BaseError(text="ERROR_1", code="OTHER_ERROR", key=2)
    assert BaseError(text="ERROR_1", code="OTHER_ERROR", key=1) != BaseError(text="ERROR_1", code="ERROR_1")
    expected_result = 1


# Generated at 2022-06-14 14:19:26.806937
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    foo = BaseError(text="example")
    bar = BaseError(text="example")
    assert foo == bar


# Generated at 2022-06-14 14:19:34.593718
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error = BaseError(text='May not have more than 100 characters', code='max_length')
    assert error == BaseError(text='May not have more than 100 characters', code='max_length')
    assert error == BaseError(text='May not have more than 100 characters', code='custom')
    assert error != BaseError(text='May not have more than 100 characters', code='min_length')
    assert error != BaseError(text='May have more than 100 characters', code='max_length')
    assert error != BaseError(text='May have more than 100 characters', code='min_length')
    assert error == BaseError(messages=[Message(text='May not have more than 100 characters',
        code='max_length')])


# Generated at 2022-06-14 14:19:45.215095
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test __eq__ with equal Message objects
    message_1 = Message(text="message text", code="message code", key="message key")
    message_2 = Message(text="message text", code="message code", key="message key")
    assert message_1 == message_2
    assert message_2 == message_1
    
    # Test __eq__ with another object
    message = Message(text="message text", code="message code", key="message key")
    assert message != "Other"
    assert "Other" != message
    
    # Test __eq__ with different Message objects
    message_1 = Message(text="message text 1", code="message code")
    message_2 = Message(text="message text 2", code="message code", key="message key")

# Generated at 2022-06-14 14:19:48.515939
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    n = 1
    m = 2
    e1 = BaseError(n, m)
    e2 = BaseError(n, m)
    if e1 == e2:
        print('test_BaseError___eq__ ok')
    else:
        raise AssertionError('test_BaseError___eq__ fail')

# Generated at 2022-06-14 14:20:00.507222
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text='May not have more than 100 characters') == BaseError(text='May not have more than 100 characters')
    assert BaseError(text='May not have more than 100 characters') != BaseError(text='May not have more than 100 characters', code='max_length')
    assert BaseError(text='May not have more than 100 characters') != BaseError(text='May not have more than 100 characters', key='name')
    assert BaseError(text='May not have more than 100 characters', position=Position(1,2,3)) != BaseError(text='May not have more than 100 characters', position=Position(4,2,3))

# Generated at 2022-06-14 14:20:05.977485
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(
        text="May not have more than 100 characters", code="max_length"
    ) == Message(
        text="May not have more than 100 characters", code="max_length"
    )
    assert Message(text="Something went wrong") == Message(text="Something went wrong")
    assert Message(text="Something went wrong") != Message(text="Something went very wrong")



# Generated at 2022-06-14 14:20:09.835384
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    err1 = BaseError(text="Test text", code="Test code", key="Test key")
    err2 = BaseError(messages=[Message(text="Test text", code="Test code", key="Test key")])
    assert err1 == err2, "BaseError.__eq__() is not working correctly"


# Generated at 2022-06-14 14:20:20.866894
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(
        text = 'text',
        code = 'code',
        key = 'key',
        index = ['index1', 'index2'], 
        position = Position(line_no = 1, column_no = 1, char_index = 1),
        start_position = Position(line_no = 1, column_no = 1, char_index = 1),
        end_position = Position(line_no = 1, column_no = 1, char_index = 1),
    )


# Generated at 2022-06-14 14:20:30.338938
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error_1 = BaseError(text="A", code="code_A", key="key_A")
    error_2 = BaseError(text="A", code="code_A", key="key_A")
    assert error_1 == error_2

    error_1 = BaseError(text="A", code="code_A", key="key_A")
    error_2 = BaseError(text="B", code="code_A", key="key_A")
    assert not error_1 == error_2
    error_1 = BaseError(text="A", code="code_A", key="key_A")
    error_2 = BaseError(text="A", code="code_B", key="key_A")
    assert not error_1 == error_2

# Generated at 2022-06-14 14:20:57.655906
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="some text")==BaseError(messages=[Message(text="some text")])
    assert BaseError(text="some text")!=BaseError(text="some other text")
    assert BaseError(text="some text")==BaseError(messages=[Message(text="some text")])
    assert BaseError(text="some text")!=None
    assert BaseError(text="some text")!="xx"


# Generated at 2022-06-14 14:21:07.914282
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    import sys
    import io
    import contextlib
    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        be = BaseError(text="text1", code="code1", key="key1")
        be2 = BaseError(text="text1", code="code1", key="key1")
        assert be == be2

        be = BaseError(text="text1", code="code1", key="key1")
        be2 = BaseError(text="text2", code="code1", key="key1")
        assert be != be2

        be = BaseError(text="text1", code="code1", key="key1")
        be2 = BaseError(text="text1", code="code2", key="key1")
        assert be != be2


# Generated at 2022-06-14 14:21:14.936241
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    class_name = "BaseError"
    # assert isinstance(self, Message)
    assert isinstance(BaseError(), Message)

    b1 = BaseError()
    b2 = BaseError()
    assert b1 == b2

    b1.text = "Message1"
    b1.code = "code1"
    b1.index = [1,2,3]

    b2.text = "Message2"
    b2.code = "code2"
    b2.index = [4,5,6]

    assert b1 != b2

    b1.text = "Message1"
    b1.code = "code1"
    b1.index = [1,2,3]

    b2.text = "Message1"
    b2.code = "code1"
    b2.index

# Generated at 2022-06-14 14:21:25.131102
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(line_no=1, column_no=3, char_index=5)
          ) == Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(line_no=1, column_no=3, char_index=5)
          )
    assert Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(line_no=1, column_no=3, char_index=5)
          ) != Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(line_no=2, column_no=3, char_index=5)
          )
    assert Message

# Generated at 2022-06-14 14:21:32.371725
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    message1 = Message(
                    text="text_message_1",
                    code="code_1",
                    index=[1,2,3],
                )
    message2 = Message(
                    text="text_message_2",
                    code="code_2",
                    index=[1,2,3],
                )
    message3 = Message(
                    text="text_message_2",
                    code="code_3",
                    index=[1,2,3],
                )
    message4 = Message(
                    text="text_message_4",
                    code="code_4",
                    index=[1,2,4],
                )
    message5 = Message(
                    text="text_message_4",
                    code="code_4",
                    key=4,
                )

# Generated at 2022-06-14 14:21:41.859845
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    result = Message(text="value_1") == Message(text="value_1")
    assert result == False
    result = Message(text="value_1", code="value_2", index=["value_3", "value_4"],
        start_position=Position(line_no=1, column_no=2, char_index=3),
        end_position=Position(line_no=4, column_no=5, char_index=6),
    ) == Message(text="value_1", code="value_2", index=["value_3", "value_4"],
        start_position=Position(line_no=1, column_no=2, char_index=3),
        end_position=Position(line_no=4, column_no=5, char_index=6),
    )
    assert result == False

# Generated at 2022-06-14 14:21:46.214006
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    def test():
        for f in [
            BaseError(text="asd"),
            BaseError(messages=[Message(text="bbb", code="ccc"), Message(text="ddd")]),
        ]:
            assert f == f
            assert not (f != f)
    test()

# Generated at 2022-06-14 14:21:55.555024
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text='text') == BaseError(text='text')
    assert BaseError(text='text', code='code', key=1) == BaseError(text='text', code='code', key=1)
    assert BaseError(text='text', code='code', key=1) == BaseError(text='text', index=[1], code='code')
    assert BaseError(text='text', code='code', key=1) != BaseError(text='text', code='code')
    assert BaseError(text='text', code='code', key=1) == BaseError(text='text', key=1, code='code')
    assert BaseError(text='text', code='code', key=1) != BaseError(text='text', key='1', code='code')

# Generated at 2022-06-14 14:22:04.197431
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text="Test")
    assert message == Message(text="Test")
    assert message != Message(text="Test", code="custom")
    assert message != Message(text="Test", index=["users"])
    assert message != Message(text="Test", position=Position(1, 2, 3))
    assert message != Message(text="Test", start_position=Position(1, 2, 3))
    assert message != Message(text="Test", end_position=Position(1, 2, 3))
    
    assert not Message(text="Test") == Message(text="Test1")
    assert not Message(text="Test") == Message(text="Test", code="custom1")
    assert not Message(text="Test") == Message(text="Test", index=["users1"])

# Generated at 2022-06-14 14:22:11.839021
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    err1 = BaseError(messages=[Message(text="", code="", key="", position=Position(1, 1, 1)), Message(text="", code="", key="", position=Position(1, 1, 1))])
    err2 = BaseError(messages=[Message(text="", code="", key="", position=Position(1, 1, 1)), Message(text="", code="", key="", position=Position(1, 1, 1))])
    equal = err1 == err2
    print(equal)
