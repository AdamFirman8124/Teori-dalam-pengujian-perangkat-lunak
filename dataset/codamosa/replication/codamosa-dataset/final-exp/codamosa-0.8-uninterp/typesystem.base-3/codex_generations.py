

# Generated at 2022-06-14 14:12:51.313613
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text='text of message1', code='code of message1', start_position=Position(1,1,1))
    message2 = Message(text='text of message2', code='code of message2', start_position=Position(2,2,2))
    assert message1 != message2
    assert message1 != "message1"
    assert message1 == message1

# Generated at 2022-06-14 14:12:56.129431
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    def _test():
        r = ValidationResult(value=None)
        for item in r:
            pass
    def _test_1():
        r = ValidationResult(value=None)
        assert r[0] is None
        assert r[1] is None
    _test()
    _test_1()

# Generated at 2022-06-14 14:13:08.076890
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    test_instance = Position(line_no=1, column_no=2, char_index=3)
    equal_instance1 = Position(line_no=1, column_no=2, char_index=3)
    equal_instance2 = Position(line_no=1, column_no=2, char_index=3)
    not_equal_instance1 = Position(line_no=1, column_no=3, char_index=3)
    not_equal_instance2 = Position(line_no=2, column_no=2, char_index=3)
    not_equal_instance3 = Position(line_no=1, column_no=2, char_index=4)
    assert test_instance == equal_instance1
    assert equal_instance1 == equal_instance2
    assert equal_instance2 == test_

# Generated at 2022-06-14 14:13:11.374159
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    v1 = ValidationResult(value = 1)
    for v in v1:
        assert v == 1
    v2 = ValidationResult(error = "error1")
    for v in v2:
        assert v == "error1"

# Generated at 2022-06-14 14:13:13.832692
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    assert list(ValidationResult(value=3)) == [3, None]
    assert list(ValidationResult(error=ValidationError(text='error'))) == [None, ValidationError(text='error')]

# Generated at 2022-06-14 14:13:18.880594
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message_1 = Message(text='May not have more than 100 characters', code='max_length', key='username')
    message_2 = Message(text='May not have more than 100 characters', code='max_length', key='username')
    
    assert message_1.__eq__(message_2)



# Generated at 2022-06-14 14:13:20.243399
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    pass # no need to implement


# Generated at 2022-06-14 14:13:23.826281
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    """
    Iteration over ValidationResult objects is tested
    """
    val_res = ValidationResult(value=1, error=None)
    for expected in [1, None]:
        assert next(iter(val_res)) == expected


# Generated at 2022-06-14 14:13:36.942125
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Test with same char_index, same line_no, same column_no
    pos1 = Position(line_no = 1, column_no = 1, char_index = 1)
    pos2 = Position(line_no = 1, column_no = 1, char_index = 1)
    assert pos1 == pos2

    # Test with different char_index same line_no, same column_no
    pos1 = Position(line_no = 1, column_no = 1, char_index = 1)
    pos2 = Position(line_no = 1, column_no = 1, char_index = 2)
    assert pos1 != pos2

    # Test with same char_index, different line_no, same column_no
    pos1 = Position(line_no = 1, column_no = 1, char_index = 1)
    pos

# Generated at 2022-06-14 14:13:45.530625
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    """
    Test if method __eq__ of class Position works as expected

    Test if expected result is returned when method __eq__ of class Position is invoked
    """
    lst = [1, 4, 5, 6]
    line_no = 4
    column_no = 4
    char_index = 5
    positional = Position(line_no, column_no, char_index)
    expected = Position(char_index, column_no, char_index)
    actual = positional.__eq__(lst)
    assert expected == actual, "Expected: {0}, Actual: {1}".format(expected, actual)


# Generated at 2022-06-14 14:13:54.526471
# Unit test for method __eq__ of class Message
def test_Message___eq__():
	_message1 = Message(text = "Hi", code = "custom", key = "username", start_position = Position(line_no = 0, column_no = 0, char_index = 0), end_position = Position(line_no = 0, column_no = 0, char_index = 0))
	_message2 = Message(text = "Hi", code = "custom", key = "username", start_position = Position(line_no = 0, column_no = 0, char_index = 0), end_position = Position(line_no = 0, column_no = 0, char_index = 0))

	assert ( _message1 == _message2 )
	print("test_Message___eq__: pass")

# Generated at 2022-06-14 14:13:58.010443
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1: Message = Message(text="wrong schema", index=["users", 1])
    msg2: Message = Message(text="wrong schema", index=["users", 1])
    assert msg1 == msg2
    msg3: Message = Message(text="wrong schema", index=["users", 2])
    assert not (msg1 == msg3)


# Generated at 2022-06-14 14:14:04.172221
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="no text", code="custom", key=None, index=[])
    m2 = Message(text="no text", code="custom", key=None, index=[])
    m3 = Message(text="has text", code="custom", key=None, index=[])
    assert m1 == m2
    assert m1 != m3


# Generated at 2022-06-14 14:14:06.422368
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    msg1 = Message(text="text")
    msg2 = Message(text="text")
    err1 = BaseError(messages=[msg1])
    err2 = BaseError(messages=[msg2])
    assert err1 == err2

test_BaseError___eq__()


# Generated at 2022-06-14 14:14:19.004897
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # Instantiate with a list of error messages
    BaseError1 = BaseError(messages=[
        Message(text='May not have more than 100 characters', code='max_length', index=[], start_position=Position(1, 0, 1), end_position=Position(1, 5, 5)),
        Message(text='May not have less than 5 characters', code='min_length', index=['username'], start_position=Position(1, 0, 1), end_position=Position(1, 5, 5)),
    ])
    # Instantiate with a single message
    BaseError2 = BaseError(text='May not have more than 100 characters', code='max_length', index=[], start_position=Position(1, 0, 1), end_position=Position(1, 5, 5))
    # Instantiate with a single message
    BaseError3 = Base

# Generated at 2022-06-14 14:14:27.869914
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error = BaseError(text="May not have more than 100 characters",
                      code="max_length",
                      key="username")

    # Test that a BaseError is equal to itself
    assert error == error

    # Test that a BaseError with the same text is equal
    other_error = BaseError(text="May not have more than 100 characters",
                            code="max_length",
                            key="username")
    assert error == other_error

    # Test that a BaseError with different text is not equal
    other_error = BaseError(text="May not have less than 10 characters",
                            code="max_length",
                            key="username")
    assert not error == other_error


# Generated at 2022-06-14 14:14:30.417382
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    p1 = Position(1,2,3)
    p2 = Position(1,2,3)
    print(p1 == p2)


# Generated at 2022-06-14 14:14:33.486921
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    err1 = BaseError(text="error message", code="custom", key=1)
    err2 = BaseError(text="error message", code="custom", key=1)
    assert err1 == err2
    assert err2 == err1


# Generated at 2022-06-14 14:14:40.013669
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    class_instance_1 = Position(line_no=1, column_no=2, char_index=3)
    class_instance_2 = Position(line_no=1, column_no=2, char_index=3)
    class_instance_3 = Position(line_no=2, column_no=2, char_index=3)
    class_instance_4 = Position(line_no=1, column_no=3, char_index=3)
    class_instance_5 = Position(line_no=1, column_no=2, char_index=4)

    assert class_instance_1 == class_instance_1
    assert class_instance_1 == class_instance_2
    assert class_instance_1 != class_instance_3
    assert class_instance_1 != class_instance_4

# Generated at 2022-06-14 14:14:46.463393
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    pos1 = Position(line_no=42, column_no=42, char_index=42)
    pos2 = Position(line_no=42, column_no=42, char_index=42)
    assert pos1 == pos2
    pos2 = Position(line_no=42, column_no=42, char_index=43)
    assert pos1 != pos2


# Generated at 2022-06-14 14:14:56.708533
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg = Message(text="May not have more than 100 characters")
    assert msg == Message(text="May not have more than 100 characters")
    assert msg != Message(text="Must not have more than 100 characters")
    assert msg != Message(text="May not have more than 100 characters", code="max_length")
    assert msg != Message(text="May not have more than 100 characters", key="username")
    assert msg != Message(text="May not have more than 100 characters", index=["users", 3, "username"])


# Generated at 2022-06-14 14:15:00.500704
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    sample_message1 = Message(text='text', code='code', index=[1,2,3], start_position=Position(1, 1, 1), end_position=Position(1, 1, 1))
    sample_message2 = Message(text='text', code='code', index=[1,2,3], start_position=Position(1, 1, 1), end_position=Position(1, 1, 1))
    sample_message3 = Message(text='text', code='code', index=[1,2,3], start_position=Position(2, 1, 1), end_position=Position(2, 1, 1))
    sample_message_list = [sample_message1, sample_message2]
    BaseError_obj1 = BaseError(text='text', code='code', key=1, messages=sample_message_list)
    Base

# Generated at 2022-06-14 14:15:06.464503
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error1 = BaseError(text='error1', code='code1', key='key1')
    error2 = BaseError(text='error2', code='code2', key='key2')
    assert (error1 != error2)
    error3 = BaseError(text='error1', code='code1', key='key1')
    assert (error1 == error3)


# Generated at 2022-06-14 14:15:09.176386
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text='This is a text', code='tk-100', key='0')
    msg2 = Message(text='This is a text', code='tk-100', key='0')

    assert msg1 == msg2


# Generated at 2022-06-14 14:15:13.125473
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    """
    Unit test for method __eq__ of class BaseError

    """

    e = BaseError(text="text", code="code")
    e2 = BaseError(text="text", code="code")

    assert e == e2


# Generated at 2022-06-14 14:15:24.957907
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    pos1 = Position(line_no = 1, column_no = 1, char_index = 1)
    pos2 = Position(line_no = 2, column_no = 2, char_index = 2)
    msg = Message(text = "str", code = "str", index = ["str"], position = pos1, start_position = pos1, end_position = pos1)
    msg2 = Message(text = "str2", code = "str2", index = ["str2"], position = pos2, start_position = pos2, end_position = pos2)
    msg_true = Message(text = "str", code = "str", index = ["str"], position = pos1, start_position = pos1, end_position = pos1)

# Generated at 2022-06-14 14:15:33.278343
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m0 = Message(
        text="Invalid object",
        code="invalid_object",
        key=None,
        index=[],
        position=Position(line_no=0, column_no=0, char_index=0),
        start_position=Position(line_no=0, column_no=0, char_index=0),
        end_position=Position(line_no=0, column_no=0, char_index=0),
    )


# Generated at 2022-06-14 14:15:35.827982
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="Error", code="Code", index=["Index"])
    message2 = Message(text="Error", code="Code", index=["Index"])
    assert message1 == message2
    assert message1 != "Error"


# Generated at 2022-06-14 14:15:44.200966
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="a") == Message(text="a")
    assert Message(text="a", code="a") == Message(text="a", code="a")
    assert Message(text="a", code="a", key="a") == Message(text="a", code="a", key="a")
    assert Message(text="a", code="a", index=["a"]) == Message(text="a", code="a", index=["a"])
    assert Message(
        text="a", code="a", position=Position(line_no=1, column_no=2, char_index=3)
    ) == Message(
        text="a",
        code="a",
        position=Position(line_no=1, column_no=2, char_index=3),
    )


# Generated at 2022-06-14 14:15:55.662259
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    str_instance = "str"
    key = 'username'
    text = 'text'
    code = 'code'
    index = ['username']
    position = Position(1, 2, 3)
    start_position = Position(4, 5, 6)
    end_position = Position(7, 8, 9)

    assert Message(text=text, code=code, key=key, position=position) == Message(
        text=text, code=code, key=key, position=position
    )
    assert Message(text=text, code=code, key=key, position=position) == Message(
        text=text, code=code, index=index, position=position
    )

# Generated at 2022-06-14 14:16:06.762429
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    value1 = Position(line_no= 1 , column_no= 2, char_index=3)
    value2 = Position(line_no= 1 , column_no= 2, char_index=3)
    assert value1==value2


# Generated at 2022-06-14 14:16:14.543253
# Unit test for method __eq__ of class Message
def test_Message___eq__():

    # Test eq to self
    message = Message(text='', code=None, key=None, index=None, position=None, start_position=None, end_position=None)
    assert (
            isinstance(message.__eq__(message), bool)
            and message.__eq__(message) == True
    )

    # Test eq to other with same attrs
    message = Message(text='', code=None, key=None, index=None, position=None, start_position=None, end_position=None)
    message2 = Message(text='', code=None, key=None, index=None, position=None, start_position=None, end_position=None)

# Generated at 2022-06-14 14:16:17.738233
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    a = Position(line_no=1, column_no=10, char_index=100)
    b = Position(line_no=1, column_no=10, char_index=100)
    c = Position(line_no=1, column_no=10, char_index=200)
    assert a == a
    assert a == b
    assert a != c


# Generated at 2022-06-14 14:16:22.940826
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    from typesystem import Schema

    class MySchema(Schema):
        integer = None
        string = None

    schema = MySchema()
    message = Message(text="Value is required", code="required", key="integer")
    error = BaseError(messages=[message])
    assert error == error
    error2 = BaseError(messages=[message])
    assert error == error2
    with pytest.raises(ValueError):
        assert error == message



# Generated at 2022-06-14 14:16:28.055613
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    expected_output = True
    line_no = 1
    column_no = 1
    char_index = 1
    pos1 = Position(line_no, column_no, char_index)
    pos2 = Position(line_no, column_no, char_index)
    assert pos1 == pos2
    assert expected_output == (pos1 == pos2)


# Generated at 2022-06-14 14:16:34.713933
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    BaseError(text="abc")
    BaseError(text="abc")
    BaseError(text="abc", code="custom") == BaseError(text="abc")
    BaseError(text="abc", code="custom") != BaseError(text="abc", code="other")
    BaseError(text="abc") == BaseError(text="abc", key="key") == BaseError(
        text="abc", key="key", position=Position(line_no=1, column_no=1, char_index=0)
    )
    BaseError(messages=[Message(text="abc", key="key")]) == BaseError(
        messages=[Message(text="abc", key="key", position=Position(line_no=1, column_no=1, char_index=0))]
    )

# Generated at 2022-06-14 14:16:46.374073
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    from typesystem import error

    # Test that equals works when two instances of the same class have
    # the same attributes (i.e. the same values for the same properties).
    assert error.Message(text='text', code='code', key='key', index=['index'], start_position=error.Position(0, 0, 0), end_position=error.Position(1, 1, 1)) == error.Message(text='text', code='code', key='key', index=['index'], start_position=error.Position(0, 0, 0), end_position=error.Position(1, 1, 1))

    # Test that equals works when two instances of the same class have
    # different attributes (i.e. different values for the same properties).

# Generated at 2022-06-14 14:16:55.577735
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message_one = Message(
        text="May not have more than 100 characters",
        code="max_length",
        key="username",
        start_position=Position(line_no=1, column_no=1, char_index=0),
        end_position=Position(line_no=1, column_no=1, char_index=0),
    )
    message_two = Message(
        text="May not have more than 100 characters",
        code="max_length",
        key="username",
        start_position=Position(line_no=1, column_no=1, char_index=0),
        end_position=Position(line_no=1, column_no=1, char_index=0),
    )
    assert message_one == message_two



# Generated at 2022-06-14 14:17:01.232083
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    pos = Position(line_no=1, column_no=2, char_index=3)
    message_1 = Message(text="text_1", code="code_1", position=pos)
    message_2 = Message(text="text_1", code="code_1", position=pos)
    assert message_1 == message_2


# Generated at 2022-06-14 14:17:12.691953
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    a = Message(text="Invalid value", position=Position(line_no=1, column_no=16, char_index=18))
    b = Message(text="Invalid value", position=Position(line_no=1, column_no=16, char_index=18))
    assert a == b

    a = Message(text="Invalid value", position=Position(line_no=1, column_no=16, char_index=18))
    b = Message(text="Invalid value", position=Position(line_no=1, column_no=16, char_index=19))
    assert a != b

    a = Message(text="Invalid value", position=Position(line_no=1, column_no=16, char_index=18))

# Generated at 2022-06-14 14:17:33.269060
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="a") == Message(text="a")
    assert Message(text="a", code="b") == Message(text="a", code="b")
    assert (
        Message(
            text="a",
            code="b",
            index=[1, 2],
            start_position=Position(1, 2, 3),
            end_position=Position(2, 3, 4),
        )
        == Message(
            text="a",
            code="b",
            index=[1, 2],
            start_position=Position(1, 2, 3),
            end_position=Position(2, 3, 4),
        )
    )
    assert (
        Message(text="a", code="b", index=[1, 2]) == Message(text="a", index=[1, 2])
    )
    assert Message

# Generated at 2022-06-14 14:17:34.387705
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    pass


# Generated at 2022-06-14 14:17:40.173853
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # given
    class MyError(BaseError):
        pass
    error1 = MyError(messages=[Message(text='Error1')])
    error2 = MyError(messages=[Message(text='Error1')])

    # when
    actual = error1 == error2

    # then
    assert actual == True


# Generated at 2022-06-14 14:17:41.492071
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    BaseError({})


# Generated at 2022-06-14 14:17:51.500004
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Test body
    # Create Position object to test
    position = Position(line_no = 1, column_no = 1, char_index = 1)

    # Test case: method __eq__ return TRUE with same position object
    _position = Position(line_no = 1, column_no = 1, char_index = 1)
    assert position.__eq__(_position) == True

    # Test case: method __eq__ return FALSE with diffrent position object
    _position = Position(line_no = 2, column_no = 2, char_index = 2)
    assert position.__eq__(_position) == False


# Generated at 2022-06-14 14:17:58.319367
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text='abc', code='abc', key='abc', position=Position(line_no=1, column_no=1, char_index=1))
    message2 = Message(text='abc', code='abc', key='abc', position=Position(line_no=1, column_no=1, char_index=1))
    message3 = Message(
        text='def', code='def', key='def', index=[1, 2, 3], position=Position(line_no=1, column_no=1, char_index=1)
    )
    assert message1 == message2
    assert message2 == message1
    assert message1 != message3
    assert message3 != message1

# Generated at 2022-06-14 14:18:09.055290
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    index = [123, "foo", "bar"]
    instance = Message(text="test", index=index, start_position=Position(1, 2, 3), end_position=Position(2, 3, 4))
    result = instance.__eq__(Message(text="test", index=index, start_position=Position(1, 2, 3), end_position=Position(2, 3, 4)))
    assert result == True
    result = instance.__eq__(Message(text="test", index=index, start_position=Position(1, 2, 3), end_position=Position(2, 3, 5)))
    assert result == False
    result = instance.__eq__(Message(text="test", index=index, start_position=Position(1, 2, 3), end_position=Position(2, 4, 4)))

# Generated at 2022-06-14 14:18:19.843552
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    text = "error message"
    code = "custom"
    key = "username"
    position = Position(line_no=12, column_no=50, char_index=50)
    message_a = Message(text=text, code=code, key=key, position=position)
    messages_a = [message_a]
    error_a = BaseError(messages=messages_a)
    assert error_a == error_a
    messages_b = [message_a, message_a]
    error_b = BaseError(messages=messages_b)
    assert not error_a == error_b
    message_c = Message(text=text, code=code, key=key)
    messages_c = [message_c]
    error_c = BaseError(messages=messages_c)


# Generated at 2022-06-14 14:18:30.207211
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    expected = {
        "text": "",
        "code": "",
        "key": None,
        "index": [],
        "position": None,
        "start_position": None,
        "end_position": None,
    }
    message1 = Message(
        text=expected["text"],
        code=expected["code"],
        key=expected["key"],
        index=expected["index"],
        position=expected["position"],
    )
    message2 = Message(
        text=expected["text"],
        code=expected["code"],
        key=expected["key"],
        index=expected["index"],
        position=expected["position"],
    )

# Generated at 2022-06-14 14:18:33.902201
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert (
        ValidationError(text="get_a_life", code="loser")
        == ValidationError(text="get_a_life", code="loser")
    )



# Generated at 2022-06-14 14:18:56.424401
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # Case 1: Different number of messages
    error1 = BaseError(messages=[Message(text="Item is required", code="required")])
    error2 = BaseError(
        messages=[
            Message(text="Item is required", code="required"),
            Message(text="Length must be more than 100 bytes", code="max_length"),
        ],
    )
    assert error1 != error2

    # Case 2: Different index.
    messages1 = [
        Message(text="Item is required", code="required"),
        Message(text="Length must be more than 100 bytes", index=["field"], code="max_length"),
    ]
    messages2 = [
        Message(text="Item is required", code="required"),
        Message(text="Length must be more than 100 bytes", index=["item"], code="max_length"),
    ]


# Generated at 2022-06-14 14:18:59.785347
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # ==
    val_0 = BaseError()
    val_1 = BaseError()
    assert val_0 == val_1
    # !=
    val_0 = BaseError()
    val_1 = BaseError(text="foo")
    assert not val_0 == val_1

# Generated at 2022-06-14 14:19:09.119895
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # Test case where the 1st and 2nd args are equal to the expected value
    exception1 = BaseError()
    exception2 = BaseError()
    assert exception1.__eq__(exception2) == True

    # Test case where the 2nd and 3rd args are equal to the expected value
    exception1 = BaseError()
    exception2 = BaseError()
    assert exception2.__eq__(exception1) == True

    # Test case where the 1st, 2nd, and 3rd args are equal to the expected value
    exception1 = BaseError()
    exception2 = BaseError()
    assert exception1.__eq__(exception2) == True
    assert exception2.__eq__(exception1) == True

    # Test case where the 1st and 2nd args are not equal to the expected value
    exception1 = BaseError

# Generated at 2022-06-14 14:19:20.149180
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # Test for __eq__ returns True when self._messages equal
    message1 = Message(text="message1", code="code1", index=[1,2])
    message2 = Message(text="message2", code="code2", index=[1,3])
    message3 = Message(text="message3", code="code3", index=[2])
    message4 = Message(text="message4", code="code4", index=[1,2])
    message5 = Message(text="message5", code="code5", index=[1])

    messages1 = [message1, message2, message3]
    messages2 = [message2, message3, message4]
    messages3 = [message1, message2, message3]
    messages4 = [message1, message2, message3, message5]


# Generated at 2022-06-14 14:19:27.390877
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    A = BaseError(text = "asdf", code = "23", key = "2")
    A1 = BaseError(text = "asdf", code = "23", key = "2")
    A2 = BaseError(text = "asdf", code = "23", key = "2", messages = [Message(text = "asdf", code = "23", key = "2")])
    B = BaseError(messages = [Message(text = "asdf", code = "23", key = "2")])
    assert A == A1
    assert A == A2
    assert A == B


# Generated at 2022-06-14 14:19:36.490957
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    msg = Message(
        text="This is a test",
        code="custom",
        index=[],
        position=Position(line_no=10, column_no=10, char_index=101),
    )
    be1 = BaseError(text="This is a test", code="custom", key="", position=Position(
        line_no=10, column_no=10, char_index=101))
    be2 = BaseError(messages=[msg])
    be3 = BaseError(messages=[
                   msg])  # this is a copy of be2 as it has the same fields
    be4 = BaseError(text="This is another test", code="custom",
                    key="", position=Position(line_no=10, column_no=10, char_index=101))

# Generated at 2022-06-14 14:19:44.420415
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    """
    Test whether __eq__ of class BaseError works correctly.
    """
    BaseError1 = BaseError(key=10, position=Position(0, 1, 2), messages=[Message(text='this is a test', code='max_length')])
    BaseError2 = BaseError(key=10, position=Position(0, 1, 2), messages=[Message(text='this is a test', code='max_length')])
    assert BaseError1 == BaseError2, f'BaseError1 = {BaseError1}, BaseError2 = {BaseError2} (expected to be the same)'


# Generated at 2022-06-14 14:19:50.766008
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    m1 = Message(text="abc", code="abc", index=[1, 2])
    m2 = Message(text="abc", code="abc", index=[1, 2])
    assert m1 == m2
    m1 = Message(text="abc", code="abc", index=None)
    m2 = Message(text="abc", code="abc", key="")
    assert m1 == m2
    m1 = Message(text="abc", code="abc", index=[1])
    m2 = Message(text="abc", code="abc", key=1)
    assert not (m1 == m2)
    m1 = Message(text="abc", code="abc", index=[1])
    m2 = Message(text="abc", code="abc", index=None)
    assert not (m1 == m2)


# Generated at 2022-06-14 14:19:56.114005
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    obj0 = BaseError(code=str(), text=str(), key=str(), messages=typing.List[Message]())
    obj1 = BaseError(code=str(), text=str(), key=str(), messages=typing.List[Message]())
    assert obj0 == obj1


# Generated at 2022-06-14 14:19:59.310051
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    a = BaseError(text="abc")
    b = BaseError(text="def")
    c = BaseError(text="abc")
    assert a == c
    assert not a == b


# Generated at 2022-06-14 14:20:24.241398
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    messages = []
    error = ValidationError(messages=messages)
    assert error == ValidationError(messages=messages)


# Generated at 2022-06-14 14:20:31.976573
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    """Test the method BaseError.__eq__()"""
    message_a = Message(
        text='May not have more than 100 characters',
        code='max_length',
        key='username',
        position=Position(1, 2, 5),
    )
    message_b = Message(
        text='May not have more than 100 characters',
        code='max_length',
        index=['username'],
        position=Position(1, 2, 5),
    )
    message_c = Message(
        text='A username is required',
        code='required',
        key='username',
        position=Position(1, 2, 5),
    )

# Generated at 2022-06-14 14:20:34.583446
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
  a = BaseError()
  b = BaseError()
  assert a==b
  

# Generated at 2022-06-14 14:20:44.663800
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error1 = BaseError(text='10', code='max_length', key='a', position=Position(line_no=1, column_no=1, char_index=1))
    error2 = BaseError(text='10', code='max_length', key='a', position=Position(line_no=1, column_no=1, char_index=1))
    error3 = BaseError(text='10', code='max_length', key='a', position=Position(line_no=1, column_no=2, char_index=2))
    error4 = BaseError(text='11', code='max_length', key='a', position=Position(line_no=1, column_no=1, char_index=1))

# Generated at 2022-06-14 14:20:54.475951
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    def _assert_ValidationError_equals(
        actual: ValidationError, expected: ValidationError
    ) -> None:
        assert actual == expected
        assert expected == actual
        assert actual.messages() == expected.messages()

    a_single_message_error = ValidationError(
        text="May not have more than 100 characters", code="max_length"
    )
    a_single_message_error_2 = ValidationError(
        text="May not have more than 100 characters", code="max_length"
    )
    _assert_ValidationError_equals(a_single_message_error, a_single_message_error_2)

    username_message = Message(
        text="May not have more than 100 characters", code="max_length", key="username"
    )
    username_message_copy

# Generated at 2022-06-14 14:20:57.605029
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    message1 = Message(text="Error text")
    message2 = Message(text="Error text")
    error1 = BaseError(messages=[message1])
    error2 = BaseError(messages=[message2])
    assert error1 == error2



# Generated at 2022-06-14 14:21:07.836844
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    data = {
        'text': 'May not have more than 100 characters',
        'code': 'max_length',
        'key': 'username',
    }
    b = BaseError(**data)
    b1 = BaseError(**data)
    assert b.__eq__(b1)
    b2 = BaseError(**data)
    b2._messages = [Message(text='May not ', code='max', key='name1')]
    b2._message_dict = {'d': 'd'}
    assert not b.__eq__(b2)
    b3 = BaseError(**data)
    b3._messages = [Message(text='May not have more than 100 characters', code='max_length', key='username')]
    b3._message_dict = dict()

# Generated at 2022-06-14 14:21:09.282575
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    obj1 = BaseError()
    obj2 = BaseError()
    assert obj1 == obj2


# Generated at 2022-06-14 14:21:12.616975
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    try:
        assert BaseError.__eq__(None, BaseError)
        assert BaseError.__eq__(BaseError, None)
        assert not BaseError.__eq__(None, None)
        # TODO: Test when other is an instance of BaseError
    except:
        print("Failed test_BaseError___eq__")


# Generated at 2022-06-14 14:21:22.860967
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    er1 = BaseError(messages=[Message(text="text1", code="code1", index=["index11"])])
    er2 = BaseError(messages=[Message(text="text2", code="code2", index=["index21"])])
    er3 = BaseError(messages=[Message(text="text1", code="code1", index=["index11"])])
    er4 = BaseError(messages=[Message(text="text1", code="code1", index=["index11"]), Message(text="text2", code="code2", index=["index21"])])

    assert not (er1 == er2)
    assert not (er2 == er3)
    assert not (er1 == er4)
    assert not (er2 == er4)
    assert not (er3 == er4)
   