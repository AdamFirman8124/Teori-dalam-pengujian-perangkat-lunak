

# Generated at 2022-06-14 14:13:01.833573
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    from typesystem import ValidationResult

    result = ValidationResult(value=1)
    assert next(iter(result)) == 1
    assert next(iter(result)) is None

    result = ValidationResult(error=ValidationError(text="an error"))
    assert next(iter(result)) is None
    assert next(iter(result)) == ValidationError(text="an error")


# Generated at 2022-06-14 14:13:06.333426
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    from typesystem import Position

    assert Position(line_no=1, column_no=1, char_index=0) == Position(line_no=1, column_no=1, char_index=0)


# Generated at 2022-06-14 14:13:07.774803
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    validationResult = ValidationResult(value=8)
    assert list(iter(validationResult)) == [8, None]


# Generated at 2022-06-14 14:13:12.260681
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr1 = ValidationResult(value=1)
    assert iter(vr1).__next__() == 1
    assert iter(vr1).__next__() is None
    vr2 = ValidationResult(error=2)
    assert iter(vr2).__next__() is None
    assert iter(vr2).__next__() == 2


# Generated at 2022-06-14 14:13:15.224548
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    v = ValidationResult(value=1) 
    assert list(v) == [1, None]

    v = ValidationResult(error=2)
    assert list(v) == [None, 2]



# Generated at 2022-06-14 14:13:17.076075
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value = ValidationResult().__iter__().__next__()

    assert value is None

# Generated at 2022-06-14 14:13:20.803490
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value, error = ValidationResult(value=5)
    assert list(value) == [5, None]

    value, error = ValidationResult(error=ValidationError("Bad data"))
    assert list(value) == [None, ValidationError("Bad data")]


# Generated at 2022-06-14 14:13:24.433154
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    _test = ValidationResult(error=ValidationError(text="test"))
    _list = list(_test)
    _expected = [None, ValidationError(text="test")]
    assert_equal(_list, _expected)



# Generated at 2022-06-14 14:13:27.381191
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    a = Position(1, 2, 3)
    b = Position(1, 2, 3)
    assert a == b
    assert a == a == b



# Generated at 2022-06-14 14:13:32.262700
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    test_str = "x = 1"
    value = 1
    error = ValidationError()
    vr = ValidationResult(value=value, error=error)
    assert vr.__iter__() == [value, error]

# Generated at 2022-06-14 14:13:43.907370
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    test_val1 = Message(text='text', code='code', key=None, index=[], position=None, start_position=None, end_position=None)
    test_val2 = Message(text='text', code='code', key=None, index=[], position=None, start_position=None, end_position=None)
    assert (test_val1 == test_val2)


# Generated at 2022-06-14 14:13:48.291957
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="abc") == Message(text="abc")
    assert Message(text="abc") != Message(text="ABC")
    assert Message(text="abc") != "abc"
    assert Message(text="abc") != 123


# Generated at 2022-06-14 14:13:57.267627
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Case 1: equality of two Position objects with identical values
    position1 = Position(100, 100, 100)
    position2 = Position(100, 100, 100)
    expected_outcome = True
    actual_outcome = (position1 == position2)
    assert actual_outcome == expected_outcome, f"The expected outcome was: {expected_outcome}, but the actual outcome was: {actual_outcome}"
    # Case 2: inequality of two Position objects with different values
    position1 = Position(100, 100, 100)
    position2 = Position(0, 0, 0)
    expected_outcome = False
    actual_outcome = (position1 == position2)
    assert actual_outcome == expected_outcome, f"The expected outcome was: {expected_outcome}, but the actual outcome was: {actual_outcome}"

# Generated at 2022-06-14 14:14:04.326024
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    p1 = Position(line_no=1, column_no=2, char_index=3)
    p2 = Position(line_no=1, column_no=2, char_index=3)
    p3 = Position(line_no=1, column_no=2, char_index=4)
    assert p1 == p2  # noqa: E712
    assert p1 != p3  # noqa: E712



# Generated at 2022-06-14 14:14:08.101978
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text='text',
        code='code',
        key=1,
        index=[1, 2, 3],
        start_position=Position(1, 2, 3),
        end_position=Position(4, 5, 6),
    )
    m2 = Message(text='text',
        code='code',
        key=1,
        index=[1, 2, 3],
        start_position=Position(1, 2, 3),
        end_position=Position(4, 5, 6),
    )
    assert m1 == m2

# Generated at 2022-06-14 14:14:12.141170
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # valid case
    message = Message(text='this is a message', code='custom', key='the key', position=Position(1, 2, 3))
    other = Message(text='this is a message', code='custom', key='the key', position=Position(1, 2, 3))
    assert message.__eq__(other) == True
    # invalid case
    message = Message(text='this is message 1', code='custom', key='the key', position=Position(1, 2, 3))
    other = Message(text='this is message 2', code='custom', key='the key', position=Position(3, 4, 5))
    assert message.__eq__(other) == False
    # assertion

# Generated at 2022-06-14 14:14:23.523200
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(1, 2, 3) == Position(1, 2, 3)
    assert Position(1, 2, 3) != Position(0, 2, 3)
    assert Position(1, 2, 3) != Position(1, 0, 3)
    assert Position(1, 2, 3) != Position(1, 2, 0)
    assert Position(1, 2, 3) != Position(1, 2, 4)
    assert Position(1, 2, 3) != Position(1, 3, 3)
    assert Position(1, 2, 3) != Position(2, 2, 3)
    assert Position(1, 2, 3) != Position(1, 2, 3, 4)


# Generated at 2022-06-14 14:14:27.721317
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # case: 
    args = None
    line_no = None
    column_no = None
    char_index = None
    # expect/return: 
    actual_result = None # type: typing.Any
    expected_result = None # type: typing.Any
    assert actual_result == expected_result


# Generated at 2022-06-14 14:14:36.595898
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    from .jsonschema import JsonSchema

    data = [
        {
            "code": "type_error",
            "index": [],
            "text": "Value must be of type integer",
        },
        {
            "code": "type_error",
            "index": [],
            "text": "Value must be of type integer",
        },
        {
            "code": "type_error",
            "index": [],
            "text": "Value must be of type integer",
        },
    ]

    schema = JsonSchema.string(max_length=10)
    error = schema.validate_or_error(data)
    assert len(error) == 1

    messages = error.messages()
    assert len(messages) == 3

# Generated at 2022-06-14 14:14:39.888961
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(1, 2, 3) == Position(1, 2, 3)



# Generated at 2022-06-14 14:14:54.063258
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message_1 = Message(text="test message 1", code="test code 1", key="test key 1", index=[1, 2, 3])
    message_2 = Message(text="test message 2", code="test code 2", key="test key 2", index=[1, 2, 3])
    message_3 = Message(text="test message 1", code="test code 1", key="test key 1", index=[4, 5, 6])
    message_4 = Message(text="test message 1", code="test code 1", key="test key 1", index=[1, 2, 3])
    assert message_1 != message_2, "Case 1 failed: Message:__eq__()"
    assert message_1 != message_3, "Case 2 failed: Message:__eq__()"

# Generated at 2022-06-14 14:14:56.818840
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    p1 = Position(1, 2, 3)
    p2 = Position(1, 2, 3)
    assert p1 == p2


# Generated at 2022-06-14 14:15:08.365495
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    """
    Assert that Message.__eq__() works
    """
    # Test: Instantiate two Messages with the same values
    # Expectation: Messages are equal
    m1 = Message(text="text", code="code", index=[1, 2, 3], position=Position(1, 2, 3))
    m2 = Message(text="text", code="code", index=[1, 2, 3], position=Position(1, 2, 3))
    assert m1 == m2

    # Test: Instantiate two Messages with the same values
    # Expectation: Messages are equal
    m1 = Message(text="text", code="code", index=[1, 2, 3], position=Position(1, 2, 3))

# Generated at 2022-06-14 14:15:20.273847
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    """
    Check the class Message.
    """
    code = "max_length"
    key = "username"
    index = ['users', 3, 'username']
    text1 = "May not have more than 100 characters"
    text2 = "May not have more than 100 characters"
    text3 = "May not have more than 1000 characters"
    position = Position(1, 3, 45)
    start_position = position
    end_position = position
    message1 = Message(text=text1, code=code, key=key, position=position)
    message2 = Message(text=text2, code=code, key=key, index=index)
    message3 = Message(text=text3, code=code, key=key, position=position)

# Generated at 2022-06-14 14:15:22.454492
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    pass # FIXME


# Generated at 2022-06-14 14:15:32.709663
# Unit test for method __eq__ of class Message
def test_Message___eq__():
	assert Message(text="May not have more than 100 characters", code="max_length",
                              key="username", position=Position(line_no=1, column_no=10, char_index=10)) == Message(text="May not have more than 100 characters", code="max_length",
                              key="username", position=Position(line_no=1, column_no=10, char_index=10))
							  

# Generated at 2022-06-14 14:15:34.999916
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    first = Message("foo")
    second = Message("bar")
    third = Message("foo")
    assert first != second
    assert first == third



# Generated at 2022-06-14 14:15:44.114036
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert (Message(text='foo', index=[]) == Message(text='foo', index=[]))
    assert (Message(text='foo', index=[]) == Message(text='foo', index=[]))
    assert (Message(text='foo', index=[]) == Message(text='foo', index=[]))
    assert (Message(text='foo', index=[]) == Message(text='foo', index=[]))
    assert (Message(text='foo', index=[]) == Message(text='foo', index=[]))
    assert (Message(text='foo', index=[]) == Message(text='foo', index=[]))
    assert (Message(text='foo', index=[]) == Message(text='foo', index=[]))
    assert (Message(text='foo', index=[]) == Message(text='foo', index=[]))

# Generated at 2022-06-14 14:15:55.620146
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='a', code='c', key='k') == Message(text='a', code='c', key='k')
    assert not (Message(text='a') == 'a')
    assert not (Message(text='a', key='k1') == Message(text='a', key='k2'))
    assert not (
        Message(text='a', code='c') == Message(text='a', code='c', position=Position(1,1,1))
    )
    assert not (
        Message(text='a', code='c') == Message(text='a', code='c', start_position=Position(1,1,1), end_position=Position(1,1,1))
    )

# Generated at 2022-06-14 14:16:02.078081
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text='May not have more than 100 characters', code='max_length')
    message2 = Message(text='May not have more than 100 characters', code='max_length')
    message3 = Message(text='May not have less than 10 characters', code='min_length')
    assert message1 == message2
    assert message2 == message1
    assert not (message1 == message3)
    assert not (message3 == message1)



# Generated at 2022-06-14 14:16:11.702931
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    expected = Position(line_no=1, column_no=1, char_index=1)
    assert expected == Position(line_no=1, column_no=1, char_index=1)
    assert expected != Position(line_no=2, column_no=1, char_index=1)
    assert expected != Position(line_no=1, column_no=2, char_index=1)
    assert expected != Position(line_no=1, column_no=1, char_index=2)
    assert expected != object()



# Generated at 2022-06-14 14:16:16.147619
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    p1 = Position(
        line_no=1, column_no=2, char_index=3
    )
    p2 = Position(
        line_no=1, column_no=2, char_index=3
    )

    assert p1 == p2


# Generated at 2022-06-14 14:16:25.671038
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    Position(line_no=1, column_no=2, char_index=3) == Position(line_no=1, column_no=2, char_index=3)
    Position(line_no=1, column_no=2, char_index=3) != Position(line_no=1, column_no=4, char_index=3)
    Position(line_no=1, column_no=2, char_index=3) != Position(line_no=4, column_no=2, char_index=3)
    Position(line_no=1, column_no=2, char_index=3) != Position(line_no=1, column_no=2, char_index=4)

# Generated at 2022-06-14 14:16:34.564076
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Case 1
    p1 = Position(line_no=10, column_no=2, char_index=20)
    p2 = Position(line_no=10, column_no=2, char_index=20)
    assert p1.__eq__(p2) == True

    # Case 2
    p1 = Position(line_no=10, column_no=2, char_index=20)
    p2 = Position(line_no=11, column_no=2, char_index=20)
    assert p1.__eq__(p2) == False

    # Case 3
    p1 = Position(line_no=10, column_no=2, char_index=20)
    p2 = Position(line_no=10, column_no=3, char_index=20)
    assert p1

# Generated at 2022-06-14 14:16:38.907802
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    position_1 = Position(line_no=2, column_no=4, char_index=4)
    position_2 = Position(line_no=2, column_no=4, char_index=4)
    assert position_1 == position_2


# Generated at 2022-06-14 14:16:42.604604
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    x = Position(1,1,1)
    y = Position(2,2,2)
    assert x == Position(1,1,1)
    assert x != y


# Generated at 2022-06-14 14:16:52.991076
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no=5, column_no=5, char_index=5) == Position(line_no=5, column_no=5, char_index=5)
    assert Position(line_no=1, column_no=1, char_index=1) != Position(line_no=2, column_no=1, char_index=1)
    assert Position(line_no=1, column_no=1, char_index=1) != Position(line_no=1, column_no=2, char_index=1)
    assert Position(line_no=1, column_no=1, char_index=1) != Position(line_no=1, column_no=1, char_index=2)
    # __eq__ always returns True or False

# Generated at 2022-06-14 14:16:55.753551
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    pos = Position(line_no = 1, column_no = 2, char_index = 3)
    assert pos == Position(line_no = 1, column_no = 2, char_index = 3)


# Generated at 2022-06-14 14:16:59.608095
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no=1, column_no=2, char_index=3) == Position(line_no=1, column_no=2, char_index=3)


# Generated at 2022-06-14 14:17:04.981365
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Setup
    self = Position(line_no=1, column_no=2, char_index=3)

    # Invocation
    result = self.__eq__(other=Position(line_no=1, column_no=2, char_index=3))

    # Verification
    assert result is True
