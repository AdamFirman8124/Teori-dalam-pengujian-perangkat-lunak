

# Generated at 2022-06-14 14:12:56.754294
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result = ValidationResult(value=1)
    assert result.value == 1
    assert result.error is None
    assert next(iter(result)) == 1
    assert next(iter(result)) is None
    assert next(iter(result)) is None


# Generated at 2022-06-14 14:13:01.184174
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value, error = ValidationResult(value=12).__iter__()
    assert value == 12
    assert error is None

    value, error = ValidationResult(error="error").__iter__()
    assert value is None
    assert error == "error"


# Generated at 2022-06-14 14:13:03.214632
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    t = ValidationResult(value=1)
    assert tuple(t) == (1, None)
    

# Generated at 2022-06-14 14:13:13.850042
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    from . import types
    from . import utils
    from . import validation_utils

    def test(schema: types.Schema) -> None:
        for data in utils.get_test_values(schema):
            result = schema.validate_or_error(data)
            value, error = result  # type: ignore
            if error is None:
                assert value == result.value
            else:
                assert error == result.error
                assert result.value is None

    schema = types.Dict(
        properties={
            "username": types.String(),
            "age": types.Integer(),
            "favourite_food": types.String(),
        },
        additional_properties=types.String(),
        required=["username"],
    )
    test(schema)


# Generated at 2022-06-14 14:13:20.794664
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    validation_result = ValidationResult(value=5)
    assert next(iter(validation_result)) == 5
    assert next(iter(validation_result)) is None
    assert next(iter(validation_result)) == 5

    validation_result = ValidationResult(error=ValidationError(text="error message"))
    assert next(iter(validation_result)) is None
    assert next(iter(validation_result)) is not None


# Generated at 2022-06-14 14:13:25.830664
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(1, 2, 3) == Position(1, 2, 3)
    assert Position(1, 2, 3) != Position(1, 2, 4)
    assert Position(1, 2, 3) != Position(1, 3, 3)
    assert Position(1, 2, 3) != Position(2, 2, 3)


# Generated at 2022-06-14 14:13:31.963949
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    p = Position(1, 2, 3)
    p.__eq__(Position(1, 2, 3))
    p.__eq__(Position(0, 2, 3))
    p.__eq__(Position(1, 0, 3))
    p.__eq__(Position(1, 2, 0))


# Generated at 2022-06-14 14:13:33.882911
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    # TODO
    print('Add Unit test here')
    print('__iter__')

# Generated at 2022-06-14 14:13:35.744925
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    value = "Hi"
    error = ValidationError(text="I'm an error")
    validation_result = ValidationResult(value=value, error=error)
    
    assert list(iter(validation_result)) == [value, error]

# Generated at 2022-06-14 14:13:42.663689
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # test_Message___eq__#1
    message = Message(text='abc')
    assert message == Message(text='abc')

    # test_Message___eq__#2
    message = Message(text='abc')
    assert message != Message(text='xyz')

    # test_Message___eq__#3
    message = Message(text='abc', code='def')
    assert message == Message(text='abc', code='def')

    # test_Message___eq__#4
    message = Message(text='abc', code='def')
    assert message != Message(text='abc', code='xyz')

    # test_Message___eq__#5
    message = Message(text='abc', index=[1])
    assert message == Message(text='abc', index=[1])

    # test_Message___eq__#6
    message

# Generated at 2022-06-14 14:13:56.975740
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    assert eval(repr(BaseError(text='a', code='b', key='c'))) == BaseError(text='a', code='b', key='c')
    assert eval(repr(BaseError(text='a', code='b', position=Position(1, 2, 3)))) == BaseError(text='a', code='b', position=Position(1, 2, 3))
    assert eval(repr(BaseError(messages=[Message(text='a', code='b', index=['c'])]))) == BaseError(messages=[Message(text='a', code='b', index=['c'])])
    assert eval(repr(BaseError(messages=[Message(text='a', code='b', index=[])]))) == BaseError(messages=[Message(text='a', code='b', index=[])])

# Generated at 2022-06-14 14:14:03.306254
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    # Test for method BaseError.__repr__
    # of class BaseError without an error message
    err = BaseError()
    assert repr(err) == "BaseError(error='')"
    # of class BaseError with error message
    err = BaseError(text="error message")
    assert repr(err) == "BaseError(error='error message')"


# Generated at 2022-06-14 14:14:14.425649
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test with same code and index
    msg = Message(text='May not have more than 100 characters.', code='max_length', index=['key'])
    msg_same = Message(text='May not have more than 100 characters.', code='max_length', index=['key'])
    assert msg == msg_same

    # Test with different text and same code and index
    msg_same = Message(text='May not have more than 2000 characters.', code='max_length', index=['key'])
    assert msg != msg_same

    # Test with different code and same text and index
    msg_same = Message(text='May not have more than 100 characters.', code='min_length', index=['key'])
    assert msg != msg_same

    # Test with different index and same text and code

# Generated at 2022-06-14 14:14:24.269560
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    # Test with one message.
    error = BaseError(text="hello", code="max_length", key="username")
    assert repr(error) == "BaseError(text='hello', code='max_length')"

    # Test with a list of messages.
    messages = [Message(text="hello", index=["hello"]), Message(text="goodbye")]
    error = BaseError(messages=messages)
    assert repr(error) == "BaseError([Message(text='hello', code='custom', index=['hello']), Message(text='goodbye', code='custom')])"

# Generated at 2022-06-14 14:14:26.288742
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    msg = BaseError(text='test')
    assert repr(msg) == "BaseError(text='test', code='custom')"


# Generated at 2022-06-14 14:14:35.646104
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    obj = Message(text="hi", code="hi", key="hi", position="hi")
    obj2 = Message(text="hi", code="hi", key="hi", position="hi")
    obj3 = Message(text="hi", code="hi", key="hi", position="hi")
    obj4 = Message(text="hi", code="hi", key="hi", position="hi")
    obj5 = Message(text="hi", code="hi", key="hi", position="hi")
    assert obj == obj2
    assert obj == obj3
    assert obj == obj4
    assert obj == obj5
    assert obj2 == obj3
    assert obj2 == obj4
    assert obj2 == obj5
    assert obj3 == obj4
    assert obj3 == obj5
    assert obj4 == obj5


# Generated at 2022-06-14 14:14:48.275833
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    # Not key
    assert BaseError(text="Some message").__repr__() == 'BaseError(text="Some message")'
    # Key
    assert BaseError(text="Some message", key="__key__").__repr__() == 'BaseError(text="Some message", code="custom", index=["__key__"])'
    # Code
    assert BaseError(text="Some message", code="__code__").__repr__() == 'BaseError(text="Some message", code="__code__")'
    # Index
    assert BaseError(text="Some message", index=["__index__"]).__repr__() == 'BaseError(text="Some message", code="custom", index=["__index__"])'
    # Key, Code

# Generated at 2022-06-14 14:15:00.109475
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    # s = "aaa"
    # assert repr(s) == '"aaa"'
    # assert repr(s) == repr(s)
    # assert repr(s) != repr(s * 2)
    # assert repr(s * 2) == '"aaaaaa"'

    # mess = Message(text='aaaaaa', code=None, index=[])
    mess = Message(text='aaaaaa', code='max_length', index=[])
    assert repr(mess) == "Message(text='aaaaaa', code='max_length')"
    print(repr(mess))

    # mess = Message(text='aaaaaa', code='max_length', index=[])
    # assert repr(mess) == "Message(text='aaaaaa', code='max_length', index=[])"
    # print(repr(mess))

    error = BaseError

# Generated at 2022-06-14 14:15:02.782579
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    assert repr(BaseError(text="May not be blank")) == "BaseError(text='May not be blank', code='custom')"


# Generated at 2022-06-14 14:15:08.524628
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="", code="", key=None, index=None, position=None, start_position=None, end_position=None) == Message(text="", code="", key=None, index=None, position=None, start_position=None, end_position=None)
    assert Message(text="", code="", key="", index=None, position=None, start_position=None, end_position=None) == Message(text="", code="", key="", index=None, position=None, start_position=None, end_position=None)
    assert Message(text="", code="", key=None, index=[], position=None, start_position=None, end_position=None) == Message(text="", code="", key=None, index=[], position=None, start_position=None, end_position=None)

# Generated at 2022-06-14 14:15:22.513160
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    position_1 = Position(line_no=1, column_no=2, char_index=3)
    position_2 = Position(line_no=4, column_no=5, char_index=6)
    message_1 = Message(
        text='Could not parse value',
        code='type_error',
        key='username',
        start_position=position_1,
        end_position=position_2
    )
    message_2 = Message(
        text='Could not parse value',
        code='type_error',
        key='username',
        start_position=position_1,
        end_position=position_2
    )
    assert message_1 == message_2


# Generated at 2022-06-14 14:15:30.491131
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text = "2", code = "2", key = "2")
    m2 = Message(text = "2", code = "2", key = "2")
    assert m1 == m2
    m3 = Message(text = "3", code = "2", key = "2")
    assert m1 != m3
    m4 = Message(text = "2", code = "3", key = "2")
    assert m1 != m4
    m5 = Message(text = "2", code = "2", key = "3")
    assert m1 != m5


# Generated at 2022-06-14 14:15:38.027014
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    position = Position(line_no=1, column_no=2, char_index=3)
    message = Message(
        text='text',
        code='code',
        key='key',
        position=position,
        start_position=position,
        end_position=position
    )
    same_message = Message(
        text='text',
        code='code',
        key='key',
        position=position,
        start_position=position,
        end_position=position
    )
    assert message == same_message
    assert message == message
    assert message != 'not a Message'
    assert message != Message(None, None, None, None, None)
    

# Generated at 2022-06-14 14:15:43.089981
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test case 1:
    """
    An instance of class Message is compared with an instance of another class,
    calls the super()'s __eq__() method.

    Note: The super()'s __eq__() method should be called here.
    """
    m1 = Message(text='Test message 1')
    m2 = []
    try:
        t = m1 == m2
    except Exception as e:
        print(e)
    else:
        print('test case 1 passed.')


# Generated at 2022-06-14 14:15:49.545402
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    import unittest
    class TestCase(unittest.TestCase):
        def test(self):
            m1 = Message(text="test_Message___eq__")
            m2 = Message(text="test_Message___eq__")
            self.assertTrue(m1 == m2)
    test_case = TestCase()
    test_case.test()


# Generated at 2022-06-14 14:15:55.310040
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text='text', code='code', key='key', position=Position(1, 2, None))
    msg2 = Message(text='text', code='code', key='key', position=Position(1, 2, None))
    assert msg1 == msg2


# USAGE
# python3 -m pytest tests/typesystem/test_base_classes.py
# pytest tests/typesystem/test_base_classes.py

# Generated at 2022-06-14 14:16:00.512456
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text='A', code='B', index=['C'])
    m2 = Message(text='A', code='B', index=['C'])
    assert m1 == m2
    m3 = Message(text='A', code='B', key='C')
    assert m1 == m3
    assert m1 != object()



# Generated at 2022-06-14 14:16:10.590381
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    import unittest
    import pytest


# Generated at 2022-06-14 14:16:20.994975
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="a", code="b", position=Position(1, 2, 3))
    m2 = Message(text="a", code="b", position=Position(1, 2, 3))
    m3 = Message(text="a", code="b", position=Position(4, 2, 3))
    m4 = Message(text="a", code="b", position=Position(1, 2, 4))
    m5 = Message(text="a", code="c", position=Position(1, 2, 3))
    m6 = Message(text="b", code="b", position=Position(1, 2, 3))

    assert m1 == m1
    assert m1 == m2
    assert m1 != m3
    assert m1 != m4
    assert m1 != m5
    assert m1 != m6



# Generated at 2022-06-14 14:16:29.527750
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="May not have more than 100 characters", code="max_length", key="username")
    message2 = Message(text="May not have more than 100 characters", code="max_length", key="username", index=['username'])
    message3 = Message(text="Invalid value", code="invalid", key="username")
    message4 = Message(text="Must be of type int", code="type_error", key="age")
    assert message1 == message2
    assert message1 != message3
    assert message1 != message4
    assert message3 != message4


# Generated at 2022-06-14 14:16:47.325979
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="my-message") == Message(text="my-message")
    assert Message(text="my-message") != Message(text="another-message")
    assert Message(text="my-message", code="code") != Message(text="my-message")
    assert Message(text="my-message", key="key") != Message(text="my-message")
    assert Message(text="my-message", index=["index"]) != Message(text="my-message")
    assert Message(text="my-message", position=Position(1, 1, 1)) != Message(text="my-message")
    assert Message(text="my-message", start_position=Position(1, 1, 1)) != Message(text="my-message")

# Generated at 2022-06-14 14:16:52.855593
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Assert with None
    message_1 = Message(text='text')
    try:
        message_1.__eq__(None)
        
    except AttributeError:
        pass
    else:
        raise Exception
            
    # Assert with False
    message_2 = Message(text='text')
    if message_1.__eq__(message_2) == False:
        pass
    else:
        raise Exception
    
    # Assert with True
    message_2 = Message(text='text')
    if message_1.__eq__(message_2) == False:
        pass
    else:
        raise Exception



# Generated at 2022-06-14 14:17:04.243879
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text='text', code='code', index=[], position=Position(1,1,1))
    message2 = Message(text='text', code='code', index=[], position=Position(1,1,1))
    message3 = Message(text='text', code='code', index=[], position=Position(1,1,1))
    assert message1 == message2
    assert message2 == message3
    assert message1 == message3
    message4 = Message(text='text', code='code', index=[], position=Position(1,1,1))
    assert message1 == message4
    message5 = Message(text='text', code='code', index=[], position=Position(1,1,2))
    assert message1 != message5

# Generated at 2022-06-14 14:17:09.438535
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(
        text="A message", code="custom", key="key", position=Position(1,1,1)
    )
    message2 = Message(
        text="A message", code="custom", key="key", position=Position(1,1,1)
    )
    assert message1 == message2

# Generated at 2022-06-14 14:17:18.425618
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="a", code="c", key="k", index=[1,2,3]) == Message(text="a", code="c", key="k", index=[1,2,3])
    assert Message(text="a", code="c", key="k", index=[1,2,3]) != Message(text="b", code="c", key="k", index=[1,2,3])
    assert Message(text="a", code="c", key="k", index=[1,2,3]) != Message(text="a", code="d", key="k", index=[1,2,3])
    assert Message(text="a", code="c", key="k", index=[1,2,3]) != Message(text="a", code="c", key="l", index=[1,2,3])

# Generated at 2022-06-14 14:17:30.325598
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Equal
    first_object = Message(text="text", code="code", index=["index1", "index2"],
        start_position=Position(line_no=0, column_no=1, char_index=2),
        end_position=Position(line_no=3, column_no=4, char_index=5))
    second_object = Message(text="text", code="code", index=["index1", "index2"],
        start_position=Position(line_no=0, column_no=1, char_index=2),
        end_position=Position(line_no=3, column_no=4, char_index=5))

    assert first_object == second_object

    # Not equal

# Generated at 2022-06-14 14:17:34.388487
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    error = Message(text="test error", code="test code", index=[1,2,3])
    temp = Message(text="test error", code="test code", index=[1,2,3])
    assert error == temp 


# Generated at 2022-06-14 14:17:40.126473
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test: test_Message___eq__ :: message1 == message1
    message1 = Message(text='text', code='code', key='key', index=['a', 'b'])
    message2 = Message(text='text', code='code', key='key', index=['a', 'b'])

    assert message1 == message2


# Generated at 2022-06-14 14:17:45.337284
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    try:
        assert Message(
            text="May not have more than 100 characters",
            code="max_length",
            key="username",
        ).__eq__(
            Message(
                text="May not have more than 100 characters",
                code="max_length",
                key="username",
            )
        )
    except AssertionError:
        print("test_Message___eq__ Failed")
    else:
        print("test_Message___eq__ Passed")



# Generated at 2022-06-14 14:17:52.589806
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    obj = Message(text='text', code='code', key=1, index=[1, 2], position=Position(0, 0, 0), start_position=Position(0, 0, 0), end_position=Position(0, 0, 0))
    obj2 = Message(text='text', code='code', key=1, index=[1, 2], position=Position(0, 0, 0), start_position=Position(0, 0, 0), end_position=Position(0, 0, 0))
    method = obj.__eq__(obj2)
    assert method == True
    

# Generated at 2022-06-14 14:18:07.021034
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    class_name = "Message"
    method_name = "__eq__"
    m0 = Message(
        text="Must be one of 'apple', 'banana', 'carrot'",
        code="invalid_choice",
        position=Position(line_no=6, column_no=15, char_index=1239),
    )
    m1 = Message(
        text="Must be one of 'apple', 'banana', 'carrot'",
        code="invalid_choice",
        position=Position(line_no=6, column_no=15, char_index=1239),
    )
    assert getattr(m0, method_name)(m1) == True


# Generated at 2022-06-14 14:18:10.302956
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="text", code="code", key=1, position=Position(1, 1, 1),)
    msg2 = Message(text="text", code="code", key=2, position=Position(1, 1, 1),)
    assert msg1 == msg1
    assert msg1 != msg2

# Generated at 2022-06-14 14:18:19.698776
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message_1 = Message(text="msg1", code="code1")
    message_2 = Message(text="msg1", code="code1")
    message_3 = Message(text="msg3", code="code3")
    message_4 = Message(text="msg4", code="code4")

    if message_1 == message_2:
        print("Test successful")
    else:
        print("Test failed")
    if message_1 == message_3:
        print("Test failed")
    else:
        print("Test successful")
    if message_1 == message_4:
        print("Test failed")
    else:
        print("Test successful")



# Generated at 2022-06-14 14:18:29.762222
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg = Message(text= "May not have more than 100 characters",
    code="max_length",
    index=[],
    start_position=Position(line_no=0, column_no=0, char_index=1),
    end_position=Position(line_no=0, column_no=0, char_index=2))

    msg2 = Message(text= "May not have more than 100 characters",
    code="max_length",
    index=[],
    start_position=Position(line_no=0, column_no=0, char_index=1),
    end_position=Position(line_no=0, column_no=0, char_index=2))

    result = (msg == msg2)
    assert result is True


# Generated at 2022-06-14 14:18:37.050438
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="Hello") == Message(text="Hello")
    assert not (Message(text="Hello") != Message(text="Hello"))
    assert Message(text="Hello") != Message(text="He")
    assert Message(text="Hello") != Message(text="He", code="error_code")
    assert Message(text="Hello") != Message()
    message = Message(text="Hello")
    assert message is not message


# Generated at 2022-06-14 14:18:42.951871
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="test1", code="code1", key="key1", start_position=Position(1, 1, 1), end_position=Position(1, 1, 1))
    message2 = Message(text="test2", code="code2", key="key1", start_position=Position(2, 2, 2), end_position=Position(2, 2, 2))
    assert message1 == message1
    assert message2 == message2
    assert message1 != message2
    

# Generated at 2022-06-14 14:18:51.194582
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    attr1 = Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(line_no=0, column_no=0, char_index=0))
    attr2 = Message(text='May not have more than 100 characters', code='max_length', key='username', position=Position(line_no=0, column_no=0, char_index=0))
    assert(attr1 == attr2)


# Generated at 2022-06-14 14:19:00.138242
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    #1
    msg1 = Message(text='This is a text', code='error_code', key=None, index=None,
    position=None, start_position=None, end_position=None)
    msg2 = Message(text='This is a text', code='error_code', key=None, index=None,
    position=None, start_position=None, end_position=None)
    assert msg1.__eq__(msg2) == True

    #2
    msg1 = Message(text='This is a text', code='error_code', key=None, index=None,
    position=None, start_position=None, end_position=None)

# Generated at 2022-06-14 14:19:06.147701
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    test_position = Position(0, 0, 0)
    assert Message(text="text_1", code="code_1", key="key_1", index=["index_1"], position=test_position) == Message(
        text="text_1", code="code_1", key="key_1", index=["index_1"], position=test_position)


# Generated at 2022-06-14 14:19:11.779055
# Unit test for method __eq__ of class Message
def test_Message___eq__():
  message_obj_one = Message(text = 'May not have more than 100 characters', code = 'max_length', key = 'username')
  message_obj_two = Message(text = 'May not have more than 100 characters', code = 'max_length', key = 'username')
  assert message_obj_one == message_obj_two
