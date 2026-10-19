

# Generated at 2022-06-14 14:12:54.060935
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='txt1', code='code1', key='key1', index=['index1'], position=Position(line_no=1, column_no=1, char_index=1), start_position=Position(line_no=1, column_no=1, char_index=1), end_position=Position(line_no=1, column_no=1, char_index=1)) == Message(text='txt1', code='code1', key='key1', index=['index1'], position=Position(line_no=1, column_no=1, char_index=1), start_position=Position(line_no=1, column_no=1, char_index=1), end_position=Position(line_no=1, column_no=1, char_index=1))


# Generated at 2022-06-14 14:12:56.502146
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    ValidationResultTest = ValidationResult(value=1)
    assert list(ValidationResultTest) == [1, None]



# Generated at 2022-06-14 14:12:59.872869
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    from unittest import mock
    from typesystem.base import ValidationResult
    instance = ValidationResult()
    response = instance.__iter__()
    assert isinstance(response, typing.Iterator)


# Generated at 2022-06-14 14:13:06.228870
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    # Test that when the BaseError objects being compared have the same values
    # for the attributes '_messages', then the method __eq__ returns true
    b1 = BaseError(messages=[Message(key=[1,2,3])])
    b2 = BaseError(messages=[Message(key=[1,2,3])])
    assert b1 == b2



# Generated at 2022-06-14 14:13:10.252782
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result1 = ValidationResult(value="Hello")
    x, y = result1
    assert x == "Hello"
    assert y == None

    result2 = ValidationResult(error="Error")
    x, y = result2
    assert x == None
    assert y == "Error"



# Generated at 2022-06-14 14:13:13.444986
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    assert list(iter(ValidationResult(value=1))) == [1, None]
    assert list(iter(ValidationResult(error=ValidationError(text="error")))) == [None, ValidationError(text="error")]


# Generated at 2022-06-14 14:13:20.140524
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    vr_0 = ValidationResult(value=None, error=None)
    vr_1 = ValidationResult(value=1, error=None)
    vr_2 = ValidationResult(value=None, error=2)
    assert tuple(vr_0) == (None, None)
    assert tuple(vr_1) == (1, None)
    assert tuple(vr_2) == (None, 2)

# Generated at 2022-06-14 14:13:29.235354
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    msg1 = Message(text='Hello World')
    msg2 = Message(text='Hello World')
    msg3 = Message(text='Hello, World')
    err_1 = BaseError(messages=[msg1])
    err_2 = BaseError(messages=[msg2])
    err_3 = BaseError(messages=[msg3])

    # check equal
    assert err_1 == err_2
    assert err_1 == err_1
    assert err_2 == err_1

    # check not equal
    assert err_1 != err_3
    assert err_3 != err_1


# Generated at 2022-06-14 14:13:35.369989
# Unit test for constructor of class ParseError
def test_ParseError():
    test_ParseError = ParseError(text='Text for ParseError')
    assert isinstance(test_ParseError, BaseError)
    test_message = test_ParseError.messages()[0]
    assert test_message.text == 'Text for ParseError'



# Generated at 2022-06-14 14:13:40.692631
# Unit test for constructor of class ParseError
def test_ParseError():
    parse_error = ParseError(text = "Parse Error", code = "Parse Error",
                             key = "Parse Error", position = Position(line_no = 1,
                             column_no = 2, char_index = 3))
    assert parse_error.messages() == [Message(text = "Parse Error", code = "Parse Error",
                                              key = "Parse Error", position = Position(line_no = 1,
                                              column_no = 2, char_index = 3))]


# Generated at 2022-06-14 14:13:55.224759
# Unit test for method __eq__ of class BaseError

# Generated at 2022-06-14 14:14:07.703873
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    mes1 = Message(text='hello', code=None, key=None, index=['foo', 'bar', 'baz'])
    mes2 = Message(text='hello', code=None, key=None, index=['foo', 'bar', 'baz'])
    mes3 = Message(text='hello', code=None, key=None, index=['foo', 'bar', 'baz', 'boo'])
    mes4 = Message(text='hello', code=None, key=None, index=['foo', 'bar', '123'])
    mes5 = Message(text='hello', code=None, key=None, index=['foo', 'bar', None])
    assert mes1 == mes2
    assert mes1 != mes3
    assert mes1 != mes4
    assert mes1 != mes5
    assert mes3 != mes4

# Generated at 2022-06-14 14:14:13.245615
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    be1 = BaseError(text="Invalid Username")
    assert be1 == BaseError(text="Invalid Username")
    assert be1 != BaseError(text="Invalid Password")

    be2 = BaseError(text="Invalid Password", key="password")
    assert be2 == BaseError(text="Invalid Password", key="password")
    assert be2 != BaseError(text="Invalid Username", key="username")


# Generated at 2022-06-14 14:14:25.941902
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text='message') == BaseError(text='message')
    assert BaseError(text='message') == BaseError(text='message', code='code')
    assert BaseError(text='message') != BaseError(text='other message')
    assert BaseError(text='message') != BaseError(text='message', code='other code')
    assert BaseError(text='message') != BaseError(text='message', key='x')
    assert BaseError(text='message') != BaseError(text='message', index=[0])
    assert BaseError(text='message') != BaseError(text='message', position=Position(0, 0, 0))
    assert BaseError(text='message') != BaseError(text='message', start_position=Position(0, 0, 0))

# Generated at 2022-06-14 14:14:31.515617
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    pos = Position(line_no=1, column_no=2, char_index=3)
    eq_pos = Position(line_no=1, column_no=2, char_index=3)
    neq_pos = Position(line_no=1, column_no=2, char_index=4)
    assert pos == eq_pos
    assert pos != neq_pos



# Generated at 2022-06-14 14:14:38.972616
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    e1 = BaseError(text="foo")
    e2 = BaseError(text="foo")
    assert e1 == e2
    assert e2 == e1
    e3 = BaseError(text="bar")
    assert e1 != e3
    assert e2 != e3
    assert e3 != e1
    assert e3 != e2
    e4 = BaseError(text="foo", code="custom")
    assert e1 != e4
    assert e2 != e4
    assert e4 != e1
    assert e4 != e2
    e5 = BaseError(text="foo", key="bar")
    assert e4 != e5
    assert e5 != e4
    e6 = BaseError(text="foo", key="baz")
    assert e5 != e6
    assert e6 != e5
    e

# Generated at 2022-06-14 14:14:49.833177
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    from .types import String, Integer
    from . import Schema, fields

    class User(Schema):
        name = fields.StringField(max_length=100)
        age = fields.IntegerField(minimum=0)

    class Users(Schema):
        users = fields.ArrayField(fields.NestedField(User))

    # Unpacking

    users = Users.validate_or_error(dict(users=[dict(name="Bob", age=-1)]))
    assert len(users.error) == 1
    error = users.error
    assert error['users'][0]['age'] == 'Must be greater than or equal to 0'

    # Message

    assert Message(text="Not a string") == Message(text="Not a string")
    assert Message(text="Not a string") != Message(text="Not a number")
   

# Generated at 2022-06-14 14:15:00.159798
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="hello") != BaseError(text="world")
    assert BaseError(text="hello") == BaseError(text="hello")
    assert BaseError(code="bad") != BaseError(code="good")
    assert BaseError(code="bad") == BaseError(code="bad")
    assert BaseError(key="name") != BaseError(key="age")
    assert BaseError(key="name") == BaseError(key="name")
    assert BaseError(position=Position(1,2,3)) != BaseError(position=Position(4,5,6))
    assert BaseError(position=Position(1,2,3)) == BaseError(position=Position(1,2,3))

# Generated at 2022-06-14 14:15:08.044334
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    position_1 = Position(
        line_no=1,
        column_no=2,
        char_index=2,
    )
    position_2 = Position(
        line_no=1,
        column_no=2,
        char_index=2,
    )
    position_3 = Position(
        line_no=1,
        column_no=3,
        char_index=0,
    )
    assert position_1 == position_2
    assert position_1 != position_3


# Generated at 2022-06-14 14:15:13.652931
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    # A method to test '__eq__' method of Position
    p1 = Position(
        line_no=3, column_no=3, char_index=3
    )  # Test case 1 - True
    p2 = Position(
        line_no=3, column_no=3, char_index=3
    )  # Test case 2 - True
    p3 = Position(
        line_no=5, column_no=5, char_index=5
    )  # Test case 3 - False
    print(p1 == p2)
    print(p2 == p3)



# Generated at 2022-06-14 14:15:22.749058
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text ="", code = "", key = 0)
    other = Message(text ="", code = "", key = 0)
    assert message == other


# Generated at 2022-06-14 14:15:32.931848
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(
        text="too short",
        code="min_length",
        key="foo",
        index=[1, "bar"],
        position=Position(line_no=0, column_no=0, char_index=0),
        start_position=Position(line_no=0, column_no=0, char_index=0),
        end_position=Position(line_no=0, column_no=0, char_index=100),
    )

# Generated at 2022-06-14 14:15:41.126750
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="May not have more than 100 characters", code="max_length") == Message(text="May not have more than 100 characters", code="max_length")
    assert Message(text="May not have more than 100 characters", code="max_length", key="username") == Message(text="May not have more than 100 characters", code="max_length", key="username")
    assert Message(text="May not have more than 100 characters", code="max_length", key="username") == Message(text="May not have more than 100 characters", code="max_length", key="username")
    assert Message(text="May not have more than 100 characters", code="max_length", index=['username']) == Message(text="May not have more than 100 characters", code="max_length", index=['username'])

# Generated at 2022-06-14 14:15:52.903405
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    msg1 = Message(text = 'payload should be a mapping' , key = 'payload', index = ['payload'])
    msg2 = Message(text = 'payload should be a mapping' , key = 'payload', index = ['payload'])
    msg3 = Message(text = 'payload should be a mapping' , key = 'payload', index = ['payload'])

    list1 = [msg1, msg2, msg3]
    list2 = [msg1, msg2, msg3, Message(text="test", index=['foo'])]

    error1 = ValidationError(messages=list1)
    error2 = ValidationError(messages=list2)
    error3 = ValidationError(messages=list1)


# Generated at 2022-06-14 14:15:57.927694
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    b = BaseError(code='custom')
    t = BaseError(code='custom')
    assert b == t
    assert hash(b) == hash(t)

    b = BaseError(code='custom', position=Position(1, 2, 3))
    t = BaseError(code='custom', position=Position(1, 2, 3))
    assert b == t
    assert hash(b) == hash(t)



# Generated at 2022-06-14 14:16:06.264163
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    assert BaseError(text="abc", key=1) == BaseError(text="abc", key=1)
    assert BaseError(text="abc", key=1) != BaseError(text="abc", key=2)
    assert BaseError(text="abc", key=1) != BaseError(text="def", key=1)
    assert BaseError(text="abc", key=1) != BaseError(text="def", key=2)
    assert BaseError(text="abc", key=1) != BaseError(text="abc")


# Generated at 2022-06-14 14:16:10.923900
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    x = BaseError()
    y = BaseError()
    z = BaseError(messages=[])
    assert (x == y) == True
    assert (x == z) == False

# Generated at 2022-06-14 14:16:21.299109
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    position_1 = Position(line_no=1, column_no=2, char_index=3)
    position_2 = Position(line_no=1, column_no=2, char_index=3)
    position_3 = Position(line_no=3, column_no=3, char_index=3)
    position_4 = Position(line_no=1, column_no=3, char_index=3)
    position_5 = Position(line_no=1, column_no=2, char_index=4)
    assert position_1 == position_2
    assert position_2 == position_1
    assert not (position_1 == position_3)
    assert not (position_1 == position_4)
    assert not (position_1 == position_5)


# Generated at 2022-06-14 14:16:27.399434
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    p1 = Position(line_no=1, column_no=1, char_index=0)
    p2 = Position(line_no=2, column_no=2, char_index=1)
    assert p1 == p1
    assert not p1 == p2
    assert not p1 == None
    assert not p1 == "foo"


# Generated at 2022-06-14 14:16:35.553832
# Unit test for method __eq__ of class BaseError
def test_BaseError___eq__():
    error1 = BaseError(text='aaaa')
    error2 = BaseError(text='bbbb')
    error3 = BaseError(messages=[Message(text='aaaa'), Message(text='bbbb')])
    error4 = BaseError(messages=[Message(text='aaaa'), Message(text='bbbb'), Message(text='cccc')])
    assert error1 == error1
    assert error1 != error2
    assert error1 != error3
    assert error3 == error3
    assert error3 != error4
    assert error4 == error4
    dict1 = dict(error1)
    dict2 = dict(error2)
    dict3 = dict(error3)
    dict4 = dict(error4)
    assert dict1 == {'': 'aaaa'}
    assert dict2 == {'': 'bbbb'}

# Generated at 2022-06-14 14:16:55.320845
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="Error1", code="code1", key="key1")
    m2 = Message(text="Error2", code="code2", key="key2")
    m3 = Message(text="Error1", code="code1", key="key1")

    assert m1 != m2
    assert m1 == m3


# Generated at 2022-06-14 14:17:07.225854
# Unit test for method __eq__ of class Position
def test_Position___eq__():

    # Test 1
    position_1 = Position(line_no=5, column_no=13, char_index=101)
    position_2 = Position(line_no=5, column_no=12, char_index=101)

    assert position_1 != position_2

    # Test 2
    position_1 = Position(line_no=5, column_no=13, char_index=101)
    position_2 = Position(line_no=5, column_no=13, char_index=102)

    assert position_1 != position_2

    # Test 3
    position_1 = Position(line_no=5, column_no=13, char_index=101)
    position_2 = Position(line_no=6, column_no=13, char_index=101)

    assert position_1 != position_

# Generated at 2022-06-14 14:17:14.008212
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(1, 1, 1) == Position(1, 1, 1)
    assert not (Position(1, 1, 1) == Position(1, 1, 2))
    assert not (Position(1, 1, 1) == Position(1, 2, 1))
    assert not (Position(1, 1, 1) == Position(2, 1, 1))
    assert not (Position(1, 1, 1) == 1)



# Generated at 2022-06-14 14:17:22.079593
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    result = Message(text='test text', code='test code', key='test key', index=['test index'], position=Position(1, 2, 3), start_position=Position(3, 2, 1), end_position=Position(1, 2, 3)).__eq__(Message(text='test text', code='test code', index=['test index']))
    assert result is True


# Generated at 2022-06-14 14:17:26.279307
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    pos1 = Position(1, 1, 1)
    pos2 = Position(2, 2, 2)
    pos3 = Position(1, 1, 1)
    assert not (pos1 == pos2)
    assert pos1 == pos3

# Generated at 2022-06-14 14:17:34.512157
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no=1, column_no=1, char_index=1) == Position(line_no=1, column_no=1, char_index=1)
    # func(line_no=1, column_no=1, char_index=1) == func(line_no=3, column_no=3, char_index=3)
    assert not Position(line_no=1, column_no=1, char_index=1) == Position(line_no=3, column_no=3, char_index=3)
    assert not Position(line_no=1, column_no=1, char_index=1) == None
    # func(line_no=1, column_no=1, char_index=1) != func(line_no=3, column_no=3, char_index

# Generated at 2022-06-14 14:17:45.021628
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(
        line_no=1, column_no=2, char_index=3
    ) == Position(line_no=1, column_no=2, char_index=3)
    assert not Position(
        line_no=2, column_no=2, char_index=3
    ) == Position(line_no=1, column_no=2, char_index=3)
    assert not Position(
        line_no=1, column_no=3, char_index=3
    ) == Position(line_no=1, column_no=2, char_index=3)
    assert not Position(
        line_no=1, column_no=2, char_index=4
    ) == Position(line_no=1, column_no=2, char_index=3)
    assert not Position

# Generated at 2022-06-14 14:17:50.767192
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    pos1 = Position(1, 1, 1)
    pos2 = Position(1, 1, 1)
    assert pos1 == pos2
    pos3 = Position(1, 2, 1)
    assert pos1 != pos3
    pos4 = Position(1, 1, 2)
    assert pos1 != pos4
    pos5 = Position(2, 1, 1)
    assert pos1 != pos5


# Generated at 2022-06-14 14:17:58.554198
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(line_no = 1, column_no = 2, char_index = 3) == Position(line_no = 1, column_no = 2, char_index = 3)
    assert Position(line_no = 1, column_no = 2, char_index = 3) != Position(line_no = 0, column_no = 2, char_index = 3)
    assert Position(line_no = 1, column_no = 2, char_index = 3) != Position(line_no = 1, column_no = 0, char_index = 3)
    assert Position(line_no = 1, column_no = 2, char_index = 3) != Position(line_no = 1, column_no = 2, char_index = 0)

# Generated at 2022-06-14 14:18:04.339720
# Unit test for method __eq__ of class Position
def test_Position___eq__():
    assert Position(1, 2, 3) == Position(1, 2, 3)
    assert Position(1, 2, 3) != Position(2, 2, 3)
    assert Position(1, 2, 3) != Position(1, 3, 3)
    assert Position(1, 2, 3) != Position(1, 2, 4)


# Generated at 2022-06-14 14:18:22.708368
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    _msg1 = Message(
        text="may not have more than 100 characters",
        key="username",
        index=["users", 3, "username"],
    )

    _msg2 = Message(
        text="may not have more than 100 characters",
        key="username",
        index=["users", 3, "username"],
    )

    assert _msg1 == _msg2


# Generated at 2022-06-14 14:18:32.012615
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Verify compare different objects
    msg = Message(text="This is a test.")
    msg1 = Message(text="This is a test.")
    assert msg == msg1

    # Verify compare different objects
    assert (
        Message(text="This is a test.") == Message(text="This is a test.")
    )

    # Verify compare different objects
    assert (
        Message(text="This is a test.", code="custom")
        == Message(text="This is a test.", code="custom")
    )

    # Verify compare different objects
    assert (
        Message(text="This is a test.", key="username")
        == Message(text="This is a test.", key="username")
    )

    # Verify compare different objects

# Generated at 2022-06-14 14:18:42.671583
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    __tracebackhide__ = True
    # code_to_test: str = "Message(text=\"May not have more than 100 characters\", code=\"max_length\", key=\"username\")"
    assert_equal(Message(text="May not have more than 100 characters", code="max_length", key="username"), Message(text="May not have more than 100 characters", code="max_length", key="username"))
    assert_equal(Message(text="May not have more than 100 characters", code="max_length", key="username"), Message(text="May not have more than 100 characters", code="max_length", key="username"))
    assert_equal(Message(text="May not have more than 100 characters", code="max_length", key="username"), Message(text="May not have more than 100 characters", code="max_length", key="username"))
    assert_equal

# Generated at 2022-06-14 14:18:54.594676
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    """
    Test method __eq__(self, other) of class Message
    """
    m1 = Message(text="text1", code="code1", index=["index1"])
    m2 = Message(text="text1", code="code1", index=["index1"])
    m3 = Message(text="text1", code="code2", index=["index1"])
    m4 = Message(text="text1", code="code1", index=["index2"])
    assertion_msg1 = "message should be equal"
    assert m1 == m2, assertion_msg1
    assertion_msg2 = "message should be different"
    assert m1 != m3, assertion_msg2
    assert m1 != m4, assertion_msg2



# Generated at 2022-06-14 14:18:55.605225
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    pass


# Generated at 2022-06-14 14:19:06.772600
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    a = Message(text='abc',code='code1',key='def')
    b = Message(text='abc',code='code1',key='def')
    # Actually a == b
    assert a.__eq__(b) == True
    # Not actually a == b
    assert not a.__eq__(Message(text='abc',code='code1'))
    assert not a.__eq__(Message(text='abc',key='def'))
    assert not a.__eq__(Message(code='code1',key='def'))
    assert not a.__eq__(Message(text='abc',code='code1',key='def',index=[1]))
    assert not a.__eq__(Message(text='abc',code='code1',key='def',start_position=Position(1,1,1)))
   

# Generated at 2022-06-14 14:19:18.054822
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test the method _Message.__eq__ when the error has a list of messages
    message = Message(text="This path is not allowed in this unittest", code="max_length", key=0, index=[0], position="content.yaml:4:4")
    # This test should pass because the two errors have the same properties
    assert message == Message(text="This path is not allowed in this unittest", code="max_length", key=0, index=[0], position="content.yaml:4:4")
    # This test should raise an AssertionError because the error has a different position
    with pytest.raises(AssertionError):
        assert message == Message(code="max_length", key=0, index=[0], position="content.yaml:5:5")
    # This test should raise an Assertion

# Generated at 2022-06-14 14:19:25.911024
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg_1 = Message(text='a', code='b')
    msg_2 = Message(text='a', code='c')
    msg_3 = Message(text='a')
    msg_4 = Message(text='a', code='b', index=[1,2,3])
    msg_5 = Message(text='a', code='b', index=[1,2,3], start_position=Position(1,1,1), end_position=Position(1,1,1))
    msg_6 = Message(text='a', code='b', index=[1,2,3], start_position=Position(1,1,1), end_position=Position(1,2,1))
    msg_7 = Message(text='a', code='b', index=[1])
    msg_8 = Message(text='a', code='b')

# Generated at 2022-06-14 14:19:34.408214
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text='test1', code='max_length', position=Position(1, 1, 1))
    msg2 = Message(text='test1', code='max_length', position=Position(2, 1, 1))
    msg3 = Message(text='test1', code='max_lenght', position=Position(1, 1, 1))
    msg4 = Message(text='test4', code='max_length', position=Position(1, 1, 1))
    msg5 = Message(text='test1', code='max_length', position=Position(1, 1, 1), index=[1])
    msg6 = Message(text='test1', code='max_length', position=Position(1, 1, 1), index=[1, 2])

# Generated at 2022-06-14 14:19:45.053880
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    error1 = Message('Text', 'Code', 'Key', Position(1, 0, 2))
    error2 = Message('Text', 'Code', 'Key')
    error3 = Message('Text2', 'Code2')
    error4 = Message('Text', 'Code', 0)
    error5 = Message('Text', 'Code', [0])
    error6 = Message('Text', 'Code', [0, 1])
    error7 = Message('Text', 'Code', 1, [1])
    error8 = Message('Text', 'Code', 0, [1, 2])
    assert error1 == error1
    assert error2 == error2
    assert error3 == error3
    assert error4 == error4
    assert error5 == error5
    assert error6 == error6
    assert error7 == error7
    assert error8 == error8
   