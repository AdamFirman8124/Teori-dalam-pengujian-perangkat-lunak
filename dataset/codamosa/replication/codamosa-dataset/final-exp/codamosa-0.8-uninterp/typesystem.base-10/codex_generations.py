

# Generated at 2022-06-14 14:12:55.977764
# Unit test for constructor of class ParseError
def test_ParseError():
    input = {
    "messages": [
        {
            "text": "May not have more than 100 characters",
            "code": "max_length",
            "key": "username"
        }
    ]}
    obj = ParseError(**input)
    path = {}
    for i in input:
        if isinstance(input[i], dict):
            for j in input[i]:
                path[i + "." + j] = input[i][j]
        else:
            path[i] = input[i]
    assert obj.__dict__ == path


# Generated at 2022-06-14 14:13:03.162875
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message_1 = Message(text='password too short', code='too_short')
    message_2 = Message(text='password too short', code='too_short')
    message_3 = Message(text='username too short', code='too_short')
    message_4 = Message(text='password too short', code='too_long')

    assert message_1 == message_2
    assert not message_1 == message_3
    assert not message_1 == message_4


# Generated at 2022-06-14 14:13:06.647013
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(text="Message A", code="Code A")
    b = Message(text="Message A", code="Code A")
    assert a == b


# Generated at 2022-06-14 14:13:08.388779
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # BaseError
    base_error1 = BaseError()
    # BaseError
    base_error2 = BaseError()
    assert base_error1 == base_error2



# Generated at 2022-06-14 14:13:17.026986
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test: Operator '==' should return True when it is supplied with Message object
    # which is equal to self.
    text = "May not have more than 100 characters"
    code = "max_length"
    key = 0
    index = [0]
    position = Position(line_no=1, column_no=1, char_index=1)
    equal_message = Message(text=text, code=code, key=key, position=position)
    message = Message(text=text, code=code, key=key, position=position)
    eq = message.__eq__(equal_message)
    assert eq == True

    # Test: Operator '==' should return False when it is supplied with Message object
    # which is not equal to self.
    text_different = "May have more than 100 characters"
    code_different

# Generated at 2022-06-14 14:13:28.765250
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="MyMessage") == Message(text="MyMessage")
    assert Message(text="MyMessage", index=["index1", "index2"]) == Message(text="MyMessage", index=["index1", "index2"])
    assert Message(text="MyMessage", index=["index1", "index2"]) != Message(text="MyMessage", index=["index1", "index2", "index3"])
    assert Message(text="MyMessage", index=["index1", "index2"], position=Position(1, 2, 3)) == Message(text="MyMessage", index=["index1", "index2"], end_position=Position(1, 2, 3))

# Generated at 2022-06-14 14:13:34.956605
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value = 10
    error = ValidationError()
    V = ValidationResult(value=value)
    v = ValidationResult(error=error)
    assert v.__iter__() == [error, None]
    assert V.__iter__() == [10, None]


# Generated at 2022-06-14 14:13:38.057777
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    x = ValidationResult(error=ValidationError(text="Error"))
    assert list(x) == [None, ValidationError(text="Error")]

    y = ValidationResult(value=1)
    assert list(y) == [1, None]

# Generated at 2022-06-14 14:13:42.470500
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    a, b = ValidationResult(value=1)
    assert a == 1
    assert b is None

    a, b = ValidationResult(error=ValidationError(text="error"))
    assert a is None
    assert b == ValidationError(text="error")


# Generated at 2022-06-14 14:13:44.291398
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    assert list(ValidationResult(value=object())) == [object(), None]


# Generated at 2022-06-14 14:13:59.854283
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    text = 'May not have more than 100 characters'
    code = 'max_length'
    key = 'username'
    start_position = Position(1, 1, 1)
    end_position = Position(1, 10, 10)
    message1 = Message(text=text, code=code, key=key, start_position=start_position, end_position=end_position)
    message2 = Message(text=text, code=code, key=key, start_position=start_position, end_position=end_position)
    messages = [message1, message2]
    error1 = BaseError(messages=messages)
    error2 = BaseError(messages=messages)
    assert(error1 == error2)


# Generated at 2022-06-14 14:14:08.077475
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    line_no = 1
    column_no = 2
    char_index = 3
    position = Position(line_no, column_no, char_index)
    assert position == Position(line_no, column_no, char_index)
    assert position != Position(line_no + 1, column_no, char_index)
    assert position != Position(line_no, column_no + 1, char_index)
    assert position != Position(line_no, column_no, char_index + 1)
    assert position != ""


# Generated at 2022-06-14 14:14:09.050699
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    pass # TODO


# Generated at 2022-06-14 14:14:17.987617
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    instance1 = Message(
        text="B", code="B", key="B", index="B", position="B", messages="B"
    )
    instance2 = Message(
        text="A", code="B", key="B", index="B", position="B", messages="B"
    )
    assert instance1.__eq__(instance1) is True
    assert instance1.__eq__(instance2) is False
    assert instance2.__eq__(instance1) is False


# Generated at 2022-06-14 14:14:28.122329
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error = BaseError(text="Error !")
    assert error == error
    error2 = BaseError(text="Error !")
    error3 = BaseError(text="Error !")
    assert error2 == error2
    assert error2 == error3
    assert error == error2 and error2 == error

    error = BaseError(messages=[Message(text="Error !", code="custom")])
    assert error == error
    error2 = BaseError(messages=[Message(text="Error !", code="custom")])
    error3 = BaseError(messages=[Message(text="Error !", code="custom")])
    assert error2 == error2
    assert error2 == error3
    assert error == error2 and error2 == error


# Generated at 2022-06-14 14:14:31.086652
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert dict(ValidationError(messages=[Message(text='hello', code='hi')])) == dict(ValidationError(messages=[Message(text='hello', code='hi')]))


# Generated at 2022-06-14 14:14:38.710150
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no=7, column_no=9, char_index=10) == Position(line_no=7, column_no=9, char_index=10)
    assert Position(line_no=7, column_no=10, char_index=10) != Position(line_no=7, column_no=9, char_index=10)
    assert Position(line_no=7, column_no=9, char_index=11) != Position(line_no=7, column_no=9, char_index=10)
    assert Position(line_no=8, column_no=9, char_index=10) != Position(line_no=7, column_no=9, char_index=10)

# Generated at 2022-06-14 14:14:49.681144
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    x = BaseError(text='test', code='test', key='test')
    y = BaseError(text='test', code='test', key='test')
    assert x == y
    x = BaseError(text='test', code='test', key='test')
    y = BaseError(text='test2', code='test', key='test')
    assert not x == y
    x = BaseError(text='test', code='test', key='test')
    y = BaseError(text='test', code='test2', key='test')
    assert not x == y
    x = BaseError(text='test', code='test', key='test')
    y = BaseError(text='test', code='test', key='test2')
    assert not x == y

# Generated at 2022-06-14 14:15:01.407182
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    msg1 = Message(text="An error message.")
    msg2 = Message(text="An error message.")
    msg3 = Message(text="Another error message.")
    msg4 = Message(text="An error message.", code="custom")
    msg5 = Message(text="An error message.", code="custom")
    msg6 = Message(text="An error message.", code="validation")
    msg7 = Message(text="An error message.", key="username")
    msg8 = Message(text="An error message.", key="username")
    msg9 = Message(text="An error message.", key="password")
    msg10 = Message(text="An error message.", index=["users", 1, "username"])
    msg11 = Message(text="An error message.", index=["users", 1, "username"])

# Generated at 2022-06-14 14:15:04.440703
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # Case positive
    first = "a"
    second = "a"
    # expect_value = 
    assert (first == second)


# Generated at 2022-06-14 14:15:23.856205
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Test when same
    Position.__eq__(Position(1, 2, 3), Position(1, 2, 3))
    # Test when different
    Position.__eq__(Position(1, 2, 3), Position(1, 2, 4))
    Position.__eq__(Position(1, 2, 3), Position(1, 3, 3))
    Position.__eq__(Position(1, 2, 3), Position(2, 2, 3))
    # Test when not a Position
    Position.__eq__(Position(1, 2, 3), "ab")


# Generated at 2022-06-14 14:15:27.067056
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no=1, column_no=2, char_index=3) == Position(line_no=1, column_no=2, char_index=3)


# Generated at 2022-06-14 14:15:29.558139
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    position = Position(1, 2, 3)
    assert position == position
    other = Position(1, 2, 3)
    assert position == other
    other = Position(3, 4, 5)
    assert position != other


# Generated at 2022-06-14 14:15:35.685358
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    x = Position(3, 5, 7)
    y = Position(3, 5, 7)
    z = x
    assert x == y
    assert x is not y
    assert x == z
    assert x is z
    assert not x == "Hello"
    assert x == Position(3, 5, 7)
    assert not x == Position(3, 4, 7)
    assert not x == Position(3, 5, 6)
    assert not x == Position(2, 5, 7)


# Generated at 2022-06-14 14:15:38.153370
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    Position1 = Position(line_no=1, column_no=2, char_index=3)
    Position2 = Position(line_no=1, column_no=2, char_index=3)
    assert Position1 == Position2



# Generated at 2022-06-14 14:15:42.855774
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Prepare input arguments
    line_no = 1
    column_no = 2
    char_index = 3
    other = None
    
    # Call the method
    try:
        return_value = Position(line_no=line_no, column_no=column_no, char_index=char_index) == other
    except Exception as e:
        return_value = str(e)

    # Check the return value
    assert return_value is False


# Generated at 2022-06-14 14:15:48.403136
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # Given
    position = Position(line_no=1, column_no=2, char_index=3)
    other = Position(line_no=1, column_no=2, char_index=3)

    # When
    result = position == other

    # Then
    assert result is True


# Generated at 2022-06-14 14:15:50.778761
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    position1 = Position(1, 1, 1)
    position2 = Position(1, 1, 1)
    assert position1 == position2

# Generated at 2022-06-14 14:15:56.704540
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    """
    Test for method __eq__ of class Position
    """
    # Arrange
    expected_result = True
    line_no = 1
    column_no = 2
    char_index = 3
    position = Position(line_no, column_no, char_index)
    other = Position(line_no, column_no, char_index)

    # Act
    actual_result = position == other

    # Assert
    assert actual_result == expected_result


# Generated at 2022-06-14 14:16:03.704752
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    t1 = Position(1, 1, 1)
    t2 = Position(1, 1, 1)
    t3 = Position(1, 2, 1)
    t4 = Position(2, 1, 1)
    t5 = Position(1, 1, 2)
    assert t1 == t2
    assert not(t1 == t3)
    assert not(t1 == t4)
    assert not(t1 == t5)
