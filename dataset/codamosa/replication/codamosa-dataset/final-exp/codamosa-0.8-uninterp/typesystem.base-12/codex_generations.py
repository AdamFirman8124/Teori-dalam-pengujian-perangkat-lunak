

# Generated at 2022-06-14 14:12:55.610605
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    r = ValidationResult(value=1)
    x, = list(r)
    assert x == 1
    x, y = list(r)
    assert x == 1
    assert y is None
    r = ValidationResult(error=ValidationError(text='error 1'))
    assert list(r) == [None, r.error]


# Generated at 2022-06-14 14:12:59.981223
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr = ValidationResult(value=1)
    assert list(vr) == [1, None]
    vr = ValidationResult(error=ValidationError(text="msg"))
    assert list(vr) == [None, ValidationError(text="msg")]

# Generated at 2022-06-14 14:13:06.750623
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    """
    Input:
    instance of ValidationResult with value and error field set to 0 and 1
    respectively.
    Expected result:
    Iterator over value and error
    """
    # create instance with value 0, error 1
    validationResult = ValidationResult(value=0,error=1)

    # test __iter__
    assert [0,1] == list(validationResult)


# Generated at 2022-06-14 14:13:08.489167
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    ValidationResult(value="hello")
    ValidationResult(error=ValueError("hello"))


# Generated at 2022-06-14 14:13:13.338411
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="Error")
    msg2 = Message(text="Error")
    msg3 = Message(text="error")
    assert msg1 == msg2
    assert msg1 == msg1
    assert msg2 == msg2
    assert msg3 == msg3
    assert not (msg1 == msg3)
    assert not (msg2 == msg3)
    assert not (msg1 == 0)


# Generated at 2022-06-14 14:13:22.567526
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    from typesystem import validate_or_error

    result = validate_or_error({'number': 6}, {'number': 'number'})
    value, error = result
    assert value == 6
    assert error == None
    # assert result == [6, None]
    print(result)

    result = validate_or_error({'number': 'six'}, {'number': 'number'})
    value, error = result
    assert value == None
    assert error != None
    print(result)
    # assert result == [None, {'number': 'is not a number.'}]



# Generated at 2022-06-14 14:13:25.435588
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    with pytest.raises(TypeError):
        ValidationResult(value='str') + ValidationResult(error=ValidationError(text='message'))  # type: ignore

# Generated at 2022-06-14 14:13:36.810308
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    left_side = Position(line_no=1, column_no=2, char_index=3)

    # identical
    assert left_side == Position(line_no=1, column_no=2, char_index=3)

    # different line_no
    assert left_side != Position(line_no=2, column_no=2, char_index=3)

    # different column_no
    assert left_side != Position(line_no=1, column_no=3, char_index=3)

    # different char_index
    assert left_side != Position(line_no=1, column_no=2, char_index=4)


# Generated at 2022-06-14 14:13:40.188891
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    p1 = Position(line_no=1, column_no=2, char_index=3)
    p2 = Position(line_no=1, column_no=2, char_index=3)
    assert p1 == p2



# Generated at 2022-06-14 14:13:44.290967
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    obj = ValidationResult(value=1)
    result = list(obj)
    assert result == [1, None]
    obj = ValidationResult(error=1)
    result = list(obj)
    assert result == [None, 1]


# Generated at 2022-06-14 14:13:52.998076
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="May not have more than 100 characters", code="max_length")
    msg2 = Message(text="May not have more than 100 characters", code="max_length")
    msg3 = Message(text="May not have more than 101 characters", code="max_length")
    assert msg1 == msg2
    assert not msg1 == msg3


# Generated at 2022-06-14 14:14:01.600134
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message_A = Message(text='some text', code='some code', key='some key', position=Position(1,2,3))
    message_B = Message(text='some text', code='some code', key='some key', position=Position(1,2,3))
    message_C = Message(text='some text', code='some code', key='some other key', position=Position(1,2,3))

    assert message_A == message_B
    assert message_B == message_A
    assert message_A != message_C
    assert message_C != message_A


# Generated at 2022-06-14 14:14:07.428838
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no=1, column_no=1, char_index=0) == Position(line_no=1, column_no=1, char_index=0)
    assert Position(line_no=1, column_no=1, char_index=0) != Position(line_no=1, column_no=1, char_index=1)


# Generated at 2022-06-14 14:14:10.704438
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    result = Message(text="text", code="code", key="key", index=["index"]).__eq__(Message(text="text", code="code", key="key", index=["index"]))
    assert (result == True)


# Generated at 2022-06-14 14:14:13.960388
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no=1, column_no=2, char_index=3) == Position(line_no=1, column_no=2, char_index=3)

# Generated at 2022-06-14 14:14:26.550456
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    """
    Method __eq__ of class Message
    """
    pos1 = Position(1, 1, 1)
    pos2 = Position(2, 2, 2)

    message1 = Message(text="text1", code="code1", key="key1", index=["a", "b"])
    message2 = Message(text="text2", code="code2", key="key2", index=["a", "b"])
    message3 = Message(text="text3", code="code3", key=None, index=["a", "b"])
    message4 = Message(text="text4", code="code4", key=None, index=["a", "c"])
    message5 = Message(text="text5", code="code5", key=None, index=None)

# Generated at 2022-06-14 14:14:35.421481
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no=1, column_no=2, char_index=3) == Position(line_no=1, column_no=2, char_index=3)
    assert not (Position(line_no=1, column_no=2, char_index=3) == Position(line_no=2, column_no=2, char_index=3))
    assert not (Position(line_no=1, column_no=2, char_index=3) == Position(line_no=1, column_no=3, char_index=3))
    assert not (Position(line_no=1, column_no=2, char_index=3) == Position(line_no=1, column_no=2, char_index=4))


# Generated at 2022-06-14 14:14:48.016197
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text = None, code = None, key = None, index = None) == Message(text = None, code = None, key = None, index = None)

    assert (not (Message(text = None, code = None, key = None, index = None) == None))
    assert (not (Message(text = None, code = None, key = None, index = None) == 1))
    assert (not (Message(text = None, code = None, key = None, index = None) == "a"))
    assert (not (Message(text = None, code = None, key = None, index = None) == Message()))
    assert (not (Message(text = None, code = None, key = None, index = None) == Message(text = "a")))

# Generated at 2022-06-14 14:15:00.007867
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="Msg") == Message(text="Msg")
    assert Message(text="Msg", code="Custom") == Message(text="Msg", code="Custom")
    assert Message(text="Msg", index=["Users"]) == Message(text="Msg", index=["Users"])
    assert (
        Message(text="Msg", position=Position(line_no=1, column_no=1, char_index=1))
        == Message(text="Msg", position=Position(line_no=1, column_no=1, char_index=1))
    )

# Generated at 2022-06-14 14:15:05.353920
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    p = Position(line_no=1, column_no=1, char_index=1)
    assert p == p
    assert p == Position(line_no=1, column_no=1, char_index=1)
    assert p != Position(line_no=2, column_no=2, char_index=2)


# Generated at 2022-06-14 14:15:11.230396
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    value = Message("text")
    target = Message("text")
    assert value == target


# Generated at 2022-06-14 14:15:23.187596
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="text", code="code", index=["index"],
                       start_position=Position(1,1,1),
                       end_position=Position(1,2,2))
    # messages with equal properties should be equal
    message2 = Message(text="text", code="code", index=["index"],
                       start_position=Position(1,1,1),
                       end_position=Position(1,2,2))
    assert message1 == message2
    # messages with different text property should not be equal
    message3 = Message(text="different text", code="code", index=["index"],
                       start_position=Position(1,1,1),
                       end_position=Position(1,2,2))
    assert message1 != message3
    # messages with different code property should not be equal

# Generated at 2022-06-14 14:15:33.323251
# Unit test for method __eq__ of class Message

# Generated at 2022-06-14 14:15:39.649463
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text='May not have more than 100 characters', code='max_length', key='username')
    message2 = Message(text='May not have more than 100 characters', code='max_length', key='username')
    message3 = 'May not have more than 100 characters'
    message4 = Message(text='May not have more than 100 characters', code='max_length', key='email')
    message5 = Message(text='May not have more than 100 characters', code='max_length', key='email')
    message6 = Message(text='May not have more than 100 characters', code='max_length', key='email')
    message7 = Message(text='May not have more than 100 characters', code='max_length', key='email')
    

# Generated at 2022-06-14 14:15:40.466130
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    pass


# Generated at 2022-06-14 14:15:52.237370
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="May not have more than 100 characters",
                       code="max_length",
                       key="username",
                       index=["users", 3, "username"],
                       position=Position(line_no=3, column_no=1, char_index=30),
                       start_position=Position(line_no=3, column_no=1, char_index=30),
                       end_position=Position(line_no=3, column_no=1, char_index=30))

# Generated at 2022-06-14 14:15:57.805410
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    #given
    message1 = Message('text', 'code', 'key', start_position = Position(4, 2, 1), end_position = Position(4, 2, 6))
    message2 = Message('text', 'code', 'key', start_position = Position(4, 2, 1), end_position = Position(4, 2, 6))
    #when
    res1 = message1 == message2
    #then
    assert res1 == True


# Generated at 2022-06-14 14:16:03.806628
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message('text', 'code', 'key', ['index'], 'position') == Message(
        'text', 'code', 'key', ['index'], 'position')
    assert Message('text', 'code', 'key', ['index']) != Message(
        'text', 'code', 'key', ['index'], 'position')


# Generated at 2022-06-14 14:16:06.666103
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text="test message", code="code", key=0)
    message2 = Message(text="test message", code="code", key=0)
    assert message == message2


# Generated at 2022-06-14 14:16:11.013968
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    first_instance = Message(text="first_instance", code="first")
    second_instance = Message(text="second_instance", code="second")
    third_instance = Message(text="first_instance", code="first")
    # should return False
    assert first_instance is not second_instance
    # should return True
    assert first_instance == third_instance


# Generated at 2022-06-14 14:16:21.069714
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text=str,code=str,key=str,index=[str])
    msg2 = Message(text="",code="",key="",index=[str])
    assert msg1 == msg2, "Messages are equal"


# Generated at 2022-06-14 14:16:32.022078
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    t1 = Message(text='May be None')
    t2 = Message(text='May be None')
    assert t1 == t2
    t1 = Message(text='May be None', key='username')
    t2 = Message(text='May be None', key='username')
    assert t1 == t2
    t1 = Message(text='May be None', code='custom')
    t2 = Message(text='May be None', code='custom')
    assert t1 == t2
    t1 = Message(text='May be None', index=['items', 0, 'username'])
    t2 = Message(text='May be None', index=['items', 0, 'username'])
    assert t1 == t2
    t1 = Message(text='May be None', position=Position(1, 1, 2))
    t

# Generated at 2022-06-14 14:16:35.227629
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='ttt', code='ccc', key='kkk', position=Position(1,2,3)) == Message(text='ttt', code='ccc', key='kkk', position=Position(1,2,3))


# Generated at 2022-06-14 14:16:46.988547
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message("foo") == Message("foo")
    assert not Message("foo") == Message("bar")
    assert Message("foo", code="custom") == Message("foo", code="custom")
    assert not Message("foo", code="custom") == Message("foo", code="invalid")
    assert Message("foo", key="bar") == Message("foo", key="bar")
    assert not Message("foo", key="bar") == Message("foo", key="baz")
    assert Message("foo", index=["bar"]) == Message("foo", index=["bar"])
    assert not Message("foo", index=["bar"]) == Message("foo", index=["baz"])
    assert Message(
        "foo", position=Position(1, 2, 3)
    ) == Message("foo", position=Position(1, 2, 3))

# Generated at 2022-06-14 14:16:55.942218
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text='asd')
    message1.start_position = 1
    message1.end_position = 2
    message2 = Message(text='qwe')
    message2.start_position = 1
    message2.end_position = 2
    assert (message1 == message2) == False
    message2.text = 'asd'
    assert (message1 == message2) == True
    message2.code = 'asd'
    assert (message1 == message2) == False
    message2.code = None
    assert (message1 == message2) == True
    message2.start_position = 2
    assert (message1 == message2) == False
    message2.start_position = 1
    message2.end_position = 1
    assert (message1 == message2) == False
    message2

# Generated at 2022-06-14 14:17:04.497414
# Unit test for method __eq__ of class Message
def test_Message___eq__():

    line_no = 1
    column_no = 2
    char_index = 3
    text = "text"
    code = "code"
    key = "key"
    messages = [Message(text = text, code = code, key = key, position = Position(line_no , column_no, char_index))]
    messages_2 = [Message(text = text, code = code, key = key, position = Position(line_no , column_no, char_index))]

    assert messages == messages_2



# Generated at 2022-06-14 14:17:15.399312
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="May not have more than 100 characters",
        code='max_length',key='username', position=Position(1,1,1)) == Message(text="May not have more than 100 characters",
        code='max_length',key='username', position=Position(1,1,1))

    assert not (Message(text="May not have more than 100 characters",
        code='max_length',key='username', position=Position(1,1,1)) == Message(text="May not have more than 100 characters",
        code='max_length',key='username', position=Position(1,1,2)))


# Generated at 2022-06-14 14:17:20.632598
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text='message1', code='code1', key='key1')
    message2 = Message(text='message2', code='code2', key='key2')
    assert message1 != message2


# Generated at 2022-06-14 14:17:27.081172
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(
        text="something went wrong",
        code="something-wrong",
        position=Position(line_no=3, column_no=2, char_index=14),
    ) == Message(
        text="something went wrong",
        code="something-wrong",
        position=Position(line_no=3, column_no=2, char_index=14),
    )



# Generated at 2022-06-14 14:17:32.314484
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text='text', code='code', key='key')
    m2 = Message(text='text', code='code', key='key')
    m3 = Message(text='text', code='code')
    m4 = Message(text='text', code='other code', key='key')
    assert m1 == m2
    assert m1 != m3
    assert m1 != m4
    assert m3 != m4

