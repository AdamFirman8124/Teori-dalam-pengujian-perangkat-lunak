

# Generated at 2022-06-14 14:12:49.390468
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    schema = typesystem.String(max_length=100)
    value = schema.validate_or_error("foo")
    assert value == ("foo", None)
    assert next(value) == "foo"
    assert next(value) is None

# Generated at 2022-06-14 14:12:51.525675
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    result = ValidationResult(value=1)
    assert [r for r in result] == [1, None]



# Generated at 2022-06-14 14:12:57.923090
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    """Unit tests for method __eq__ of class Message."""
    assert Message(text='a', code='b', key='c') == Message(text='a', code='b', key='c')
    assert Message(text='a', code='b', key='c') == Message(text='a', code='b', key='c', position=Position(line_no=1, column_no=2, char_index=3))

# Generated at 2022-06-14 14:13:01.287849
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text = 'text1', code = 'code1')
    m2 = Message(text = 'text1', code = 'code1')
    assert m1 == m2


# Generated at 2022-06-14 14:13:12.195899
# Unit test for constructor of class ParseError
def test_ParseError():
    with pytest.raises(TypeError):
        ParseError()

    with pytest.raises(TypeError):
        ParseError(text="Parse error message.")

    with pytest.raises(TypeError):
        ParseError(text="Parse error message.", position="foo")

    with pytest.raises(TypeError):
        ParseError(text="Parse error message.", position=Position(1, 2, 3))

    assert ParseError(
        text="Parse error message.",
        code="parse_error_code",
        position=Position(1, 2, 3),
    ) == ParseError(
        text="Parse error message.",
        code="parse_error_code",
        position=Position(1, 2, 3),
    )


# Generated at 2022-06-14 14:13:19.276211
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    position1 = Position(1, 2, 3)
    position2 = Position(4, 5, 6)
    message1 = Message(text='foo')
    message2 = Message(text='foo')
    message3 = Message(text='bar')
    message4 = Message(text='foo', code='baz')
    message5 = Message(text='foo', code='baz')
    message6 = Message(text='foo', key=42)
    message7 = Message(text='foo', key=42)
    message8 = Message(text='foo', index=[42])
    message9 = Message(text='foo', index=[42])
    message10 = Message(text='foo', position=position1)
    message11 = Message(text='foo', position=position1)
    message12 = Message(text='foo', position=position2)


# Generated at 2022-06-14 14:13:26.139231
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    res = ValidationResult(value=1)
    assert next(iter(res)) == 1
    assert next(iter(res)) is None
    assert list(iter(res)) == [1, None]

    res = ValidationResult(error=ParseError())
    assert next(iter(res)) is None
    assert isinstance(next(iter(res)), ParseError)
    assert list(iter(res)) == [None, ParseError()]


# Generated at 2022-06-14 14:13:29.493219
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    assert list(ValidationResult(value=42)) == [42, None]
    assert list(ValidationResult(error="oh no")) == [None, "oh no"]

# Generated at 2022-06-14 14:13:38.691465
# Unit test for method __iter__ of class ValidationResult
def test_ValidationResult___iter__():
    print("test_ValidationResult___iter__")
    v, e = ValidationResult(value=2).__iter__()
    assert v == 2
    assert e is None
    
    l = [int, str]
    v, e = ValidationResult(error=ValidationError(messages=l)).__iter__()
    assert isinstance(e, ValidationError)
    assert isinstance(e.messages()[0], Message)
    assert e.messages()[0].index[0] == int
    assert e.messages()[1].index[0] == str


# Generated at 2022-06-14 14:13:43.965254
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    assert repr(BaseError(text='test')) == "BaseError(text='test', code='custom')"
    assert repr(BaseError(messages=[Message(text='test', code='test', key='test')])) == "BaseError([Message(text='test', code='test', index=['test'], position=None)])"

# Generated at 2022-06-14 14:13:55.978901
# Unit test for constructor of class ParseError
def test_ParseError():
    # Valid
    ParseError(messages=[Message(text="message1", code="code1")])
    ParseError(messages=[Message(text="message1", code="code1"), Message(text="message2", code="code2")])
    ParseError(text="message1")
    ParseError(text="message1", code="code1")
    ParseError(text="message1", key="key1")
    ParseError(text="message1", code="code1", key="key1")
    ParseError(text="message1", code="code1", position=Position(1,1,1))
    ParseError(text="message1", code="code1", start_position=Position(1,1,1), end_position=Position(1,1,1))
    # Invalid

# Generated at 2022-06-14 14:14:08.354129
# Unit test for constructor of class BaseError
def test_BaseError():
	messages = [Message(text= '', code = None, key =None, index = None, position=None, start_position= None, end_position= None)]
	messages = [Message(text= 'hello', code = 'thisisacode', key ='thisisakey', index = 'thisisaindex', position=Position, start_position= Position, end_position= Position)]
	messages = [Message(text= 'hello', code = None, key ='thisisakey', index = 'thisisaindex', position=None, start_position= Position, end_position= Position)]
	messages = [Message(text= '', code = 'thisisacode', key =None, index = 'thisisaindex', position=None, start_position= Position, end_position= Position)]

# Generated at 2022-06-14 14:14:21.222517
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    assert repr(BaseError(text="xxx")) == "BaseError(text='xxx', code='custom')"
    assert repr(BaseError(text="xxx", code="yyy")) == "BaseError(text='xxx', code='yyy')"
    assert repr(BaseError(text="xxx", code="yyy", key="zzz")) == "BaseError(text='xxx', code='yyy', index=['zzz'])"
    assert repr(BaseError(text="xxx", code="yyy", key="zzz", position=Position(1, 2, 3))) == "BaseError(text='xxx', code='yyy', index=['zzz'], position=Position(line_no=1, column_no=2, char_index=3))"

# Generated at 2022-06-14 14:14:23.185136
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg = Message('error')
    msg2 = Message('error')
    assert msg == msg2

# Generated at 2022-06-14 14:14:24.832162
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    '''
        message1 = Message(text='May not have more than 100 characters', code='max_length', key='username')
        message2 = Message(text='May not have more than 100 characters', code='max_length', key='username')
        assert message1 == message2
    '''


# Generated at 2022-06-14 14:14:29.689901
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="some text", code="custom", key="my_key", start_position=Position(1,2,3), end_position=Position(4,5,6))
    m2 = Message(text="some text", code="custom", key="my_key", start_position=Position(1,2,3), end_position=Position(4,5,6))
    assert m1 == m2


# Generated at 2022-06-14 14:14:37.830779
# Unit test for constructor of class BaseError
def test_BaseError():

    # Check that constructors return initialized BaseError instances
    assert BaseError(
        text='Some text',
        code='Some code',
        key='Some key',
        position=Position(line_no=1, column_no=1, char_index=1),
    ) == BaseError(
        text='Some text',
        code='Some code',
        key='Some key',
        position=Position(line_no=1, column_no=1, char_index=1),
    )


# Generated at 2022-06-14 14:14:45.648229
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    value1 = Message(text = 'text', code = 'code', index = ['index'], start_position = Position(1,1,1), end_position = Position(2,2,2))
    value2 = Message(text = 'text', code = 'code', index = ['index'], start_position = Position(1,1,1), end_position = Position(2,2,2))
    assert(value1 == value2)


# Generated at 2022-06-14 14:14:53.314742
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    import typesystem
    import yaml
    schema = typesystem.Schema(str)
    schema.validate('valid string')
    content = '''
    # test_yaml_document_validator
    #!tag
    base:
        # base-key-1
        key-1: value-1
        # base-key-2
        key-2: value-2
    derivered:
        # derivered-key-1
        key-1: value-1
        # derivered-key-2
        key-2: value-2
    '''
    tokens = schema.tokenize_yaml(yaml.safe_load(content))
    for token in tokens:
        if token.error is not None:
            print("token.error:")
            print(repr(token.error))

# Generated at 2022-06-14 14:15:05.265611
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    error = ValidationError(messages=[Message(text="foo", code="custom")])
    assert repr(error) == "ValidationError([Message(text='foo', code='custom')])"
    assert str(error) == "{'': 'foo'}"
    error = ValidationError(messages=[Message(text="foo", code="custom", key="foo")])
    assert repr(error) == "ValidationError([Message(text='foo', code='custom', index=['foo'])])"
    assert str(error) == "{'foo': 'foo'}"
    error = ValidationError(messages=[Message(text="foo", code="custom", index=["foo", 3])])
    assert repr(error) == "ValidationError([Message(text='foo', code='custom', index=['foo', 3])])"
    assert str

# Generated at 2022-06-14 14:15:19.242765
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='May not have more than 100 characters',code='max_length')==Message(text='May not have more than 100 characters',code='max_length')
    assert Message(text='May not have more than 100 characters',code='max_length')!=Message(text='May not have more than 100 characters',code='min_length')
    # Two message objects are same if index is not specified in both
    assert Message(text='May not have more than 100 characters',code='max_length')==Message(text='May not have more than 100 characters',code='max_length',key='username')

# Generated at 2022-06-14 14:15:29.729420
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Test with different line numbers.
    assert Message(
        text="May not have more than 100 characters",
        code="max_length",
        key="username",
        position=Position(1, 3, 4),
    ) != Message(
        text="May not have more than 100 characters",
        code="max_length",
        key="username",
        position=Position(1, 3, 5),
    )

    # Test with different column numbers.
    assert Message(
        text="May not have more than 100 characters",
        code="max_length",
        key="username",
        position=Position(1, 3, 4),
    ) != Message(
        text="May not have more than 100 characters",
        code="max_length",
        key="username",
        position=Position(1, 4, 4),
    )

   

# Generated at 2022-06-14 14:15:33.393055
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text = "text1", code = "code1", key = "key1")
    message2 = Message(text = "text1", code = "code1", key = "key1")
    message3 = Message(text = "text2", code = "code2", key = "key2")
    assert message1 == message2
    assert message1 != message3

if __name__ == '__main__':
    test_Message___eq__()

# Generated at 2022-06-14 14:15:34.420914
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    with pytest.raises(Exception):
        BaseError()


# Generated at 2022-06-14 14:15:42.150997
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    class Message:

        def __init__(self):
            pass

        def __eq__(self, other):
            return isinstance(other, Message)

        def __hash__(self):
            return 0

        def __repr__(self):
            class_name = self.__class__.__name__
            return f"{class_name}()"

    class TestClass:
        def __init__(self):
            self.messages = [Message()]
            self.__message_dict = {'key': 'value'}
            self.__message_dict = {'k': 'v'}

        def messages(self, *, add_prefix: typing.Union[str, int] = None) -> typing.List[Message]:
            return self.messages


# Generated at 2022-06-14 14:15:47.869596
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    instance1 = BaseError(text='May not have more than 100 characters', code='max_length', key='username')
    instance2 = BaseError(messages=[Message(text='May not have more than 100 characters', code='max_length', index=['username'])])
    print(instance1)
    print(instance2)



# Generated at 2022-06-14 14:15:54.329206
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    # Case 1
    assert Message("text") == Message("text")
    # Case 2
    assert Message("text") == Message("text", code="foo")
    # Case 3
    assert Message("text") == Message("text", key=0)
    # Case 4
    assert Message("text") == Message("text", index=[0])
    # Case 5
    assert Message("text") == Message("text", index=[0, 1])
    # Case 6
    assert Message("text") == Message("text", position=Position(0, 0, 0))
    # Case 7
    assert Message("text") == Message("text", index=[1, 0], position=Position(0, 0, 0))
    # Case 8
    assert Message("text") == Message("text", index=[0], position=Position(0, 0, 0))
    # Case 9


# Generated at 2022-06-14 14:16:05.308699
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    """__eq__(self, other)"""
    m1 = Message(text='message text', code='code', key='key', position=Position(1,1,1))
    m2 = Message(text='message text', code='code', key='key', position=Position(1,1,1))
    m3 = Message(text='message text', code='code', key='key', position=Position(1,1,5), start_position=Position(1,1,1), end_position=Position(1,1,5))

    # test for valid call
    assert m1 == m2
    assert m1 == m3
    # test for invalid call
    m4 = Message(text='message text', code='code', key='key')
    try:
        assert m1 == m4
    except:
        pass
    # Invalid call

# Generated at 2022-06-14 14:16:07.399501
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    print(BaseError(text='text'))
    print(BaseError(messages=['messages']))


# Generated at 2022-06-14 14:16:17.472250
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    v = BaseError()
    assert v.__repr__() == 'BaseError({})'
    v = BaseError(text = 'asdf')
    assert v.__repr__() == "BaseError(text='asdf', code='custom')"
    v = BaseError(text = 'asdf', code = 'asf')
    assert v.__repr__() == "BaseError(text='asdf', code='asf')"
    v = BaseError(messages = [Message(text = 'asdf')])
    assert v.__repr__() == "BaseError([Message(text='asdf', code='custom', index=[])])"
    

# Generated at 2022-06-14 14:16:34.860797
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert (Message(text='abc', code='abc') == Message(text='abc', code='abc')) == True
    assert (Message(text='abc', code='abc') == Message(text='abx', code='abc')) == False
    assert (Message(text='abc', code='abc') == Message(text='abc', code='abx')) == False
    assert (Message(text='abc', code=None) == Message(text='abc', code=None)) == True
    assert (Message(text='abc', code=None) == Message(text='abc', code='abc')) == False
    assert (Message(text='abc', code='abc') == Message(text='abc', code=None)) == False
    assert (Message(text='abc', key='') == Message(text='abc', key='')) == True

# Generated at 2022-06-14 14:16:38.861152
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text='May not have more than 100 characters', code='max_length')
    message1 = Message(text='May not have more than 100 characters', code='max_length')
    assert message == message1


# Generated at 2022-06-14 14:16:48.504620
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    from datetime import datetime

    assert Message(
        text="Message1",
        code="Message1",
        key="Message1",
        index=["Message1"],
        position=Position(1,2,3),
        start_position=Position(4,5,6),
        end_position=Position(7,8,9),
    ) == Message(
        text="Message1",
        code="Message1",
        key="Message1",
        index=["Message1"],
        position=Position(1,2,3),
        start_position=Position(4,5,6),
        end_position=Position(7,8,9),
    )


# Generated at 2022-06-14 14:16:51.117630
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    first_message = Message(text="test text")
    second_message = Message(text="test text")
    assert first_message == second_message


# Generated at 2022-06-14 14:17:01.232967
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    assert BaseError().__repr__() == "BaseError({})"
    assert BaseError(text="error").__repr__() == "BaseError(text='error', code='custom')"
    assert BaseError(text="error", code="max_length").__repr__() == \
        "BaseError(text='error', code='max_length')"
    assert BaseError(text="error", key=12).__repr__() == \
        "BaseError(text='error', code='custom', index=[12])"

# Generated at 2022-06-14 14:17:11.931097
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(
        text='May not have more than 100 characters',
        code='max_length',
        key='username'
    )
    message2 = Message(
        text='May not have more than 100 characters',
        code='max_length',
        key='username'
    )
    message3 = Message(
        text='May not have more than 100 characters',
        code='max_length'
    )
    message4 = Message(
        text='May not have more than 100 characters',
        code='max_length',
        key='username',
        start_position=Position(1, 1, 2)
    )
    assert message1 == message2
    assert message1 != message3
    assert message1 != message4


# Generated at 2022-06-14 14:17:15.946659
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    error = BaseError()
    assert repr(error) == "BaseError(messages=[])"
    error = BaseError(text='May not have more than 100 characters')
    assert repr(error) == "BaseError(text='May not have more than 100 characters', code='custom')"


# Generated at 2022-06-14 14:17:25.655723
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    Msg1 = Message(text="text1", code="code1", key=1, index=2, position=Position(1,2,3), start_position=Position(1,2,3), end_position=Position(1,2,3))
    Msg2 = Message(text="text1", code="code1", key=1, index=2, position=Position(1,2,3), start_position=Position(1,2,3), end_position=Position(1,2,3))
    assert Msg1 == Msg2


# Generated at 2022-06-14 14:17:29.820996
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    # Given: A validation error object
    v = ValidationError(text = "text", code = "code")
    
    # Then: It should return a string containing the text and code
    expected = 'ValidationError(text="text", code="code")'
    assert(str(v) == expected)

# Generated at 2022-06-14 14:17:32.552380
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    BaseError(text="hello", code="code", key="key", position="position")
    BaseError(messages=["messages"])


# Generated at 2022-06-14 14:17:51.633176
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    # Test when instantiated with a single error message.
    error = BaseError(
        text="May not have more than 100 characters", code="max_length", key="username"
    )
    assert repr(error) == "BaseError(text='May not have more than 100 characters', code='max_length')"

    # Test when instantiated with multiple error messages.
    error = BaseError(
        messages=[
            Message(text="May not have more than 100 characters", code="max_length")
        ]
    )
    assert (
        repr(error)
        == "BaseError([Message(text='May not have more than 100 characters', code='max_length', index=[])])"
    )



# Generated at 2022-06-14 14:17:54.091837
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text = 'hello', code = 'custom')
    msg2 = Message(text = 'hello', code = 'custom')

    if msg1 == msg2:
        print('test_Message___eq__ [YES]')
    else:
        print('test_Message___eq__ [NO]')


# Generated at 2022-06-14 14:17:56.161695
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    messages = [Message(text="Invalid format")]
    e = BaseError(messages=messages)
    print(e)

# Generated at 2022-06-14 14:18:07.025659
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    p1 = Position(1,2,3)
    p2 = Position(4,5,6)
    p3 = Position(7,8,9)
    m1 = Message(text="foo", index=["a", 1, 2], start_position=p1, end_position=p2)
    assert m1 == m1
    m2 = Message(text="foo", index=["a", 1, 2], start_position=p1, end_position=p2)
    assert m1 == m2
    m3 = Message(text="foo", index=["a", 2, 1], start_position=p1, end_position=p2)
    assert m1 != m3
    m4 = Message(text="foo", index=["a", 1, 2], start_position=p2, end_position=p1)


# Generated at 2022-06-14 14:18:13.757901
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    # Arrange
    from typesystem import Schema
    from jsonschema import Draft7Validator
    from jsonschema.exceptions import ValidationError as JSONSchemaValidationError
    def hello_schema():
        return Schema(
            type="string",
            pattern=r"^hello",
            error_prefix="Invalid hello: ",
        )
    # Act
    try:
        hello_schema().validate("world")
    except ValidationError as error:
        assert repr(error) == "ValidationError(['Invalid hello: May not have more than 100 characters'])"


# Generated at 2022-06-14 14:18:20.149267
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="May not have more than 100 characters", position=Position(line_no=1, column_no=1, char_index=0))
    msg2 = Message(text="May not have more than 100 characters", position=Position(line_no=1, column_no=1, char_index=0))
    assert msg1 == msg2


# Generated at 2022-06-14 14:18:25.039593
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1=Message(text="abc",code="abc",key="abc",index=["abc"],position=Position(1,2,3))
    message2=Message(text="abc",code="abc",key="abc",index=["abc"],position=Position(1,2,3))
    assert message1 == message2


# Generated at 2022-06-14 14:18:33.171906
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    # Instantiate with single message
    message = Message(text='text', code='code', key='key', position=None)
    error = BaseError(text='text', code='code', key='key', position=None)
    assert repr(error) == "BaseError(text='text', code='code', index=['key'])"
    # Instantiate with multiple messages
    messages = [message, message]
    error = BaseError(messages=messages)
    assert repr(error) == (
        "BaseError(["
        "Message(text='text', code='code', index=['key'], position=None),"
        " Message(text='text', code='code', index=['key'], position=None)]"
        ")"
    )


# Generated at 2022-06-14 14:18:35.254434
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    # Test for __repr__ for class BaseError
    pass


# Generated at 2022-06-14 14:18:44.151887
# Unit test for method __repr__ of class BaseError
def test_BaseError___repr__():
    import inspect
    import json
    import re
    import sys
    from pprint import pprint

    from swagger_codegen.api.paths import *
    from swagger_codegen.api.responses import *
    from swagger_codegen.api.security import *
    from swagger_codegen.api.tags import *
    from swagger_codegen.api.schemas import *
    from swagger_codegen.api.parameters import *
    from swagger_codegen.data_types import *
    from swagger_codegen.loaders import *
    from swagger_codegen.api.components import *
    from swagger_codegen.api.exceptions import *
    from swagger_codegen.api.definitions import *

    def get_method_name():
        import inspect
       

# Generated at 2022-06-14 14:18:56.502358
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    first = Message(text='abc', code= 'abc', key='abc', index=['abc', 'abc'], position=None, start_position=None, end_position=None)
    second = Message(text='abc', code= 'abc', key='abc', index=['abc', 'abc'], position=None, start_position=None, end_position=None)
    assert first.__eq__(second) == True


# Generated at 2022-06-14 14:19:07.508822
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(text="Hello world!", code="invalid")
    message_1 = Message(text="Hello world!", code="invalid")
    message_2 = Message(text="Hello world!", code="invalid", key="key")
    message_3 = Message(text="Hello world!", code="invalid", key="key_1")
    message_4 = Message(text="Hello world!", code="invalid", index=["key"])
    message_5 = Message(text="Hello world!", code="invalid", index=["key_1"])
    message_6 = Message(text="Hello world!", code="invalid", position=Position(1,1,1))
    message_7 = Message(text="Hello world!", code="invalid", position=Position(1,1,2))

# Generated at 2022-06-14 14:19:10.864549
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message(text="hi", key="hi")
    msg2 = Message(text="hi", key="hi")

    assert msg1 == msg2
    assert not (msg1 != msg2)



# Generated at 2022-06-14 14:19:21.343442
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    code = "test"
    position = Position(1, 2, 3)
    message = Message(text=code, code=code, position=position)
    assert message == Message(text=code, code=code, position=position)
    assert message != Message(text=code, code=code, position=Position(5, 6, 7))
    assert message == Message(text=code, code=code, start_position=position, end_position=position)
    assert message != Message(text=code, code=code, start_position=Position(5, 6, 7), end_position=position)
    assert message != Message(text=code, code=code, start_position=position, end_position=Position(5, 6, 7))

# Generated at 2022-06-14 14:19:31.054485
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message = Message(
        text='text_value',
        code='code_value', 
        key='key_value', 
        position=Position(line_no=1, column_no=1, char_index=1),
        start_position=Position(line_no=1, column_no=1, char_index=1),
        end_position=Position(line_no=1, column_no=1, char_index=1),
        )

# Generated at 2022-06-14 14:19:35.767969
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text="hi", code="hi", key="hi", index="hi", position="hi", start_position="hi", end_position="hi") == Message(text="hi", code="hi", key="hi", index="hi", position="hi", start_position="hi", end_position="hi")
    assert not Message(text="hi", code="hi", key="hi", index="hi", position="hi", start_position="hi", end_position="hi") == 1
    assert not Message(text="hi", code="hi", key="hi", index="hi", position="hi", start_position="hi", end_position="hi") == Message(text="hi", code="hi", key="hi", index="hi", position="hi", start_position="hi", end_position="hi2")

# Generated at 2022-06-14 14:19:36.961128
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message() == Message()


# Generated at 2022-06-14 14:19:46.833665
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message_1 = Message(text='my text', code='my_code', key='my_key', start_position=Position(line_no=1, column_no=1, char_index=1))
    message_2 = Message(text='my text', code='my code', key='my_key', start_position=Position(line_no=1, column_no=1, char_index=1))
    message_3 = Message(text='my text', code='my_code', key='my_key', start_position=Position(line_no=3, column_no=3, char_index=3))

    # two messages with same text, code, and position
    assert (message_1 == message_2) == True

    # two messages with same text and code but different positions
    assert (message_1 == message_3) == False

# Generated at 2022-06-14 14:19:59.232120
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    message1 = Message(text="error message")
    message2 = Message(text="error message")
    assert (message1 == message2) == True
    message1 = Message(text="error message", code="custom")
    message2 = Message(text="error message", code="custom")
    assert (message1 == message2) == True
    message1 = Message(text="error message", code="custom", key="username")
    message2 = Message(text="error message", code="custom", key="username")
    assert (message1 == message2) == True
    message1 = Message(text="error message", index=["users", 3, "username"])
    message2 = Message(text="error message", index=["users", 3, "username"])
    assert (message1 == message2) == True

# Generated at 2022-06-14 14:20:05.921251
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    import unittest
    assert not (Message(text="a") == "a")
    assert not (Message(text="a") == 1)
    assert not (Message(text="a") == 0.5)
    assert not (Message(text="a", code="a") == Message(text="a"))
    assert not (Message(text="a", code="a") == Message(text="a", code="b"))
    assert not (Message(text="a") == Message(text="b"))
    assert not (Message(text="a", index=[1]) == Message(text="a", index=[1, 2]))
    assert not (Message(text="a", index=[1]) == Message(text="a", index=[2]))
    assert not (Message(text="a") == Message(text="a", index=["a"]))

# Generated at 2022-06-14 14:20:24.006752
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='text') == Message(text='text')
    assert Message(text='text', index=['index']) == Message(text='text', index=['index'])
    assert Message(text='text', code='code') == Message(text='text', code='code')
    assert Message(text='text', start_position=Position(line_no=1, column_no=2, char_index=3)) == Message(text='text', start_position=Position(line_no=1, column_no=2, char_index=3))
    assert Message(text='text', end_position=Position(line_no=1, column_no=2, char_index=3)) == Message(text='text', end_position=Position(line_no=1, column_no=2, char_index=3))
    assert Message

# Generated at 2022-06-14 14:20:31.830073
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    assert Message(text='message1', code=None, key=None, index=None, position=Position(line_no=1, column_no=3, char_index=3)) == Message(text='message1', code=None, key=None, index=None, position=Position(line_no=1, column_no=3, char_index=3))
    assert Message(text='message1', code=None, key=None, index=None, position=Position(line_no=1, column_no=3, char_index=3)) != Message(text='message2', code=None, key=None, index=None, position=Position(line_no=1, column_no=3, char_index=3))

# Generated at 2022-06-14 14:20:42.598650
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message('test1', 'test2', 'test3', [4,5,6], Position( 1, 2, 3), Position(4,5,6))
    msg2 = Message('test1', 'test2', 'test3', [4,5,6], Position( 1, 2, 3), Position(4,5,6))
    assert msg1 == msg2
    msg3 = Message('test1', 'test2', 'test3', [4,5,6], Position( 7, 8, 9), Position(10,11,12))
    assert msg1 != msg3
    msg4 = Message('test1', 'test2', 'test3', [4,5,6], Position( 7, 8, 9), Position(4,5,6))
    assert msg1 != msg4

# Generated at 2022-06-14 14:20:48.721957
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    position = Position(line_no=1, column_no=2, char_index=3)
    a = Message(text='abc', code='abc', index=[1, 2, 3], key='a',
                start_position=position, end_position=position)
    b = Message(text='abc', code='abc', index=[1, 2, 3], key='a',
                start_position=position, end_position=position)
    assert a == b


# Generated at 2022-06-14 14:20:56.852094
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    messages_1 = (
        Message(text="Text 1", code=None, index=None, position=None),
        Message(text="Text 2", code=None, index=None, position=None),
        Message(text="Text 3", code=None, index=None, position=None),
    )
    messages_2 = (
        Message(text="Text 1", code=None, index=None, position=None),
        Message(text="Text 2", code=None, index=None, position=None),
        Message(text="Text 3", code=None, index=None, position=None),
    )
    assert (messages_1 == messages_2) # __eq__ = True
    assert not (messages_1 != messages_2) # __ne__ = False


# Generated at 2022-06-14 14:21:00.900518
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    Position.__init__(line_no = 1, column_no = 2, char_index = 3)
    Message.__init__(text = 'May not have more than 100 characters', code = 'max_length', index = [1, 2, 3], start_position = Position, end_position = Position)



# Generated at 2022-06-14 14:21:05.090553
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    msg1 = Message("May not have more than 100 characters")
    msg2 = Message("May not have more than 100 characters")
    assert msg1 == msg2
    assert msg1 == msg1
    assert msg1 != {'text':"May not have more than 100 characters"}


# Generated at 2022-06-14 14:21:05.804216
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    pass

# Generated at 2022-06-14 14:21:10.443577
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    flag = 0
    message1 = Message(text="", code="", key="", index=[], position=None, start_position=None, end_position=None)
    message2 = Message(text="", code="", key="", index=[], position=None, start_position=None, end_position=None)
    if message1 == message2:
        flag = 1
    assert flag == 1


# Generated at 2022-06-14 14:21:16.584060
# Unit test for method __eq__ of class Message
def test_Message___eq__():
    m1 = Message(text="text", code="code", key="key", position="position")
    m2 = Message(text="text", code="code", key="key", position="position")
    m3 = Message(text="text_1", code="code", key="key", position="position")
    m4 = Message(text="text", code="code_1", key="key", position="position")
    m5 = Message(text="text", code="code", key="key_1", position="position")
    m6 = Message(text="text", code="code", key="key", position="position_1")
    assert m1 == m2
    assert m1 != m3
    assert m1 != m4
    assert m1 != m5
    assert m1 != m6
