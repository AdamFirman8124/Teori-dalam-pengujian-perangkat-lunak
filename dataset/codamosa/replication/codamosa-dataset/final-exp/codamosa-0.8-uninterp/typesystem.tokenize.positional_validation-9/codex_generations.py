

# Generated at 2022-06-14 14:45:20.353001
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class IntSchema(Schema):
        int = Field(type="int")

    # First test with successful validation
    token = Token(value="2", start=None, end=None)
    assert validate_with_positions(token=token, validator=IntSchema) == {"int": 2}

    # Then test with a required field
    token = Token(value={}, start=None, end=None)
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=IntSchema)
    assert excinfo.value.messages()[0].text == "The field 'int' is required."

    # And then a type validation
    token = Token(value="string", start=None, end=None)

# Generated at 2022-06-14 14:45:26.589706
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Given
    token = Token(
        value={"title": "abc"},
        start_position=Position(line=3, char_index=1, line_index=1),
    )
    validator = Schema(
        {
            "title": Field(required=True),
            "url": Field(default=None),
        }
    )

    # When
    with pytest.raises(ValidationError) as err:
        validate_with_positions(token=token, validator=validator)

    # Then
    error_messages = err.value.messages

# Generated at 2022-06-14 14:45:34.184080
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Array, String
    from typesystem.tokenize.tokens import ArrayToken, StringToken
    from typesystem.tokenize.positions import Position, Range
    from typesystem.tokenize.exceptions import TokenizeSyntaxError

    source = "hello world"
    token = StringToken(value="hello world", start=Position(0, 0), end=Range(0, 0, 10))

    # Validation succeeds
    validate_with_positions(token=token, validator=String())

    # Validation fails
    with pytest.raises(TokenizeSyntaxError) as context:
        validate_with_positions(token=token, validator=Array(items=String()))

# Generated at 2022-06-14 14:45:44.547935
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    from typesystem.fields import Integer

    text = '{"foo": "bar", "baz": 42}'
    data = json.loads(text)
    token = Token(text=text, value=data, root=True)

    field = Integer(name="foo")
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(validator=field, token=token)

    assert exc_info.value.messages()[0].start_position.char_index == 8
    assert exc_info.value.messages()[0].end_position.char_index == 11
    assert exc_info.value.messages()[0].text == "The field 'foo' must be an integer."

# Generated at 2022-06-14 14:45:54.619366
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem import types, fields
    from typesystem.schemas import Schema
    from typesystem.exceptions import ValidationError

    def create_validator(field: Field):
        class Validator(Schema):
            value = field

        return Validator

    token = tokenize("value", {"value": "bar"})

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=create_validator(types.String()))

    error_message: Message = exc_info.value.messages[0]
    assert error_message.text == "Invalid type"
    assert error_message.code == "invalid_type"
    assert error_message.index == ("value",)
    assert error_

# Generated at 2022-06-14 14:46:01.726724
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.types import Primitive
    from typesystem.fields import Int

    schema = {
        "type": "object",
        "properties": {
            "a": {"type": "number"},
            "b": {"type": "number"},
            "c": {"type": "number"},
        },
    }
    document = '{"a": "x", "b": "y", "c": "z"}'

    tokens = tokenize(document)
    root_token = tokens[0]
    int_field = Int()

    # Check that we get the right exception
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=root_token, validator=schema)

    # Check that the exception messages have

# Generated at 2022-06-14 14:46:11.303337
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import Field
    from typesystem.tokenize.tokens import Token

    class Dog(Schema):
        name = Field(type=str, required=True)

    schema = Dog()

    # Token has no nesting, and error is at the root level.
    token = Token(value={"name": None}, start=(1, 1), end=(1, 5))
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=schema)
    error = exc.value.messages()[0]
    assert error.index == ["name"]
    assert error.start_position == (1, 3)
    assert error.end_position == (1, 5)

    # Token has no nesting, but

# Generated at 2022-06-14 14:46:16.743513
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer
    from typesystem.schemas import Object, String

    class Person(Schema):
        name = String(min_length=1)
        age = Integer()

    person = Person()
    person.validate_with_positions(
        {
            "name": "John",
            "age": "Not an int",
        }
    )

# Generated at 2022-06-14 14:46:25.107438
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class TodoSchema(Schema):
        title = Field(type=str, min_length=1)
        status = Field(type=str, enum=["new", "done"])

    schema = TodoSchema()

    todo_dict = {"title": "write some code", "status": "work"}
    todo_node = yaml.load(yaml.dump(todo_dict))

    # Invalid because status is not in the allowed list
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=todo_node, validator=schema)

    # Invalid because status is not in the allowed list
    error = exc_info.value.messages[1]
    assert error.code == "enum"
    assert error.start_position.line == 1


# Generated at 2022-06-14 14:46:32.086003
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from .test_tokenize import (
        TokenizeTests,
        TestTokenize,
        TestTokenizeEmbedded,
        TestTokenizeEmbeddedList,
    )
    from .test_fields import PrimitiveFieldTests, TestField

    tests = TokenizeTests()
    tests.run_test_cases("test_validate_with_positions")

    primitive_tests = PrimitiveFieldTests()
    primitive_tests.run_test_cases("test_validate_with_positions")



# Generated at 2022-06-14 14:46:44.339478
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.api import tokenize_json_schema
    from typesystem.schemas import JSONSchema, Schema
    from typesystem.fields import Integer
    from typesystem.properties import Properties
    from typesystem.fields import Array
    import pytest

    def is_valid(schema: str) -> None:
        assert validate_with_positions(
            token=tokenize_json_schema(schema), validator=JSONSchema
        ) is None

    def raises(schema: str) -> None:
        with pytest.raises(ValidationError):
            validate_with_positions(token=tokenize_json_schema(schema), validator=JSONSchema)

    is_valid("{}")
    is_valid("[]")
    is_valid("1")

# Generated at 2022-06-14 14:46:55.017542
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizers import Tokenizer

    tokenizer = Tokenizer.from_schema({"type": "object", "properties": {"x": {"type": "string"}}})

    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(
            token=tokenizer.tokenize('{"x": 1}', path="test.json"),
            validator=tokenizer.schema.fields["x"],
        )


# Generated at 2022-06-14 14:47:05.551421
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class MyField(Field):
        def check_value(self, value):
            if value < 0:
                return False
            else:
                return True

        def coerce_value(self, value):
            return str(value)

    class MySchema(Schema):
        field1 = MyField()
        field2 = MyField()
        field3 = MyField()

    from typesystem.tokenize.lexers import ValueLexer

    value = {"field1": [1, 2, 3], "field2": [4, 5, 6], "field3": [7, 8, 9]}
    tokens = ValueLexer().tokenize(value)
    validate_with_positions(token=tokens, validator=MySchema)


# Generated at 2022-06-14 14:47:14.941140
# Unit test for function validate_with_positions
def test_validate_with_positions():
    print("Testing 'validate_with_positions'...")
    from typesystem import Integer
    schema = {"age": {"type": Integer, "required": True}}
    token = Token("root", {"age": "1"}, 0, 0)
    validate_with_positions(token=token, validator=schema)
    try:
        validate_with_positions(token=token, validator={"age": {"type": Integer}})
    except ValidationError as error:
        print("expected error:")
        for message in error.messages():
            print(message)
    else:
        raise AssertionError("expected error")
    data = """
    {"person": {"name": "", "age": 1}}
    """

# Generated at 2022-06-14 14:47:26.485278
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String
    from typesystem.tokenize.tokens import DictToken

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=DictToken(  # type: ignore
                start={"line": 1, "char": 0}, end={"line": 1, "char": 0}, value={}
            ),
            validator=String(required=True),
        )

    error = exc_info.value

    assert len(error.messages()) == 1

    message = error.messages()[0]

    assert message.start_position == {"line": 1, "char": 0}
    assert message.end_position == {"line": 1, "char": 0}
    assert message.text == "The field 'name' is required."
    assert message

# Generated at 2022-06-14 14:47:33.865941
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    from .utils import SortKeys
    from .utils import get_obj

    class UserSchema(Schema):
        name = Field(type="string")

    json_str = """{"name": "not a string"}"""
    obj = get_obj(json_str)
    tokens = tokenize(obj)

    token = tokens.lookup([])
    try:
        validate_with_positions(token=token, validator=UserSchema)
    except ValidationError as error:
        messages = [SortKeys().sort_key(m.to_dict()) for m in error.messages]

# Generated at 2022-06-14 14:47:41.699972
# Unit test for function validate_with_positions
def test_validate_with_positions():
    string = '{ "name": "Alice" }'
    token = Token(json.loads(string), start={}, end={})
    field = Field(validators=[Field(), Field()])
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=field)
    assert exc_info.value.messages()[0].start_position == (1, 0)
    assert exc_info.value.messages()[0].end_position == (1, 4)

# Generated at 2022-06-14 14:47:53.830349
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem import types

    class PersonSchema(Schema):
        name = types.String()
        phone = types.String()

    schema = PersonSchema()

    text = """
    name: jon
    phone: 555-111-111
    """

    token = Token.parse_source(text)
    with pytest.raises(ValidationError) as exc:
        schema.validate(token.value)

    text = """
    name: jon
    """

    token = Token.parse_source(text)
    with pytest.raises(ValidationError) as exc:
        schema.validate(token.value)


# Generated at 2022-06-14 14:48:03.202453
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """
    Tests the simple case that a token is validated with a simple field.
    """
    # Create the field and give it a dummy value
    field = Field(type="string")
    field.value = "dummy_value"

    # Create a token for the value and add it to the parent token
    token = Token(value="hello", line=1, char_index=0)

    # Validate the token with the field
    assert field.validate(token.value) == "hello"
    assert validate_with_positions(token=token, validator=field) == "hello"

# Generated at 2022-06-14 14:48:10.438547
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class NumberSchema(Schema):
        number = Field(int)

    with pytest.raises(ValidationError) as exc_info:
        result = validate_with_positions(
            token=tokenize('{"number": "string"}'), validator=NumberSchema
        )
    assert exc_info.value.messages() == [
        Message(
            text="Must be an integer.",
            code="invalid",
            index=["number"],
            start_position=Position(line_index=0, char_index=15),
            end_position=Position(line_index=0, char_index=23),
        )
    ]

# Generated at 2022-06-14 14:48:24.801073
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.schemas import Schema
    from typesystem.fields import String, Array

    class SimpleSchema(Schema):
        text = String()

        class Meta:
            allow_unknown = True

    class ListSchema(Schema):
        values = Array(items=String(format="email"))

    simple_schema = SimpleSchema()
    list_schema = ListSchema()
    tokens = tokenize({"text": "hello"})
    assert simple_schema.validate(tokens) == {"text": "hello"}
    tokens = tokenize({"text": "hello", "wrong field": "value"})
    assert simple_schema.validate(tokens) == {"text": "hello", "wrong field": "value"}

# Generated at 2022-06-14 14:48:25.423114
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:48:34.176739
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem

    class User(typesystem.Schema):
        name = typesystem.String()

    class Post(typesystem.Schema):
        title = typesystem.String(required=True)
        user = typesystem.Object(User, required=True)

    post = Post({"title": "My post"})
    try:
        post.validate()
    except typesystem.ValidationError as exc:
        message = exc.messages[0]
        assert message.text == "The field 'user' is required."
        assert message.start_position.line_num == 1
        assert message.start_position.char_index == 2
        assert message.end_position.line_num == 1
        assert message.end_position.char_index == 9


# Generated at 2022-06-14 14:48:41.251313
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object, String, Integer

    class Example(Object):
        foo = String(required=True)
        bar = Integer(required=True)

    token = Token(
        type="dict", value={"foo": "123"}, start=None, end=None,
    )

    # Running the validation should raise a ValidationError.
    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=Example)

# Generated at 2022-06-14 14:48:48.800140
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema({"name": Field(str, required=True)})
    token = Token({"name": Token(123)}, start=0, end=1)

    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as exception:
        assert exception.messages() == [Message(
            text='The field "name" is required.', code="required",
            start_position=0, end_position=1, index=[]
        )]
    else:
        assert False, 'ValidationError not raised.'

# Generated at 2022-06-14 14:49:00.639430
# Unit test for function validate_with_positions
def test_validate_with_positions():

    token = Token()
    token.start = (1, 0)
    token.end = (1, 5)

    class MySchema(Schema):
        field1: str
        field2: int

    token.value = {"field1": "foo", "field2": "bar"}

    try:
        validate_with_positions(token=token, validator=MySchema)
    except ValidationError as error:
        messages: typing.List[Message] = error.messages()
        assert messages[0].text == (
            'Value "bar" (type str) does not match expected type ' "int."
        )
        assert messages[0].start_position == (1, 3)
        assert messages[0].end_position == (1, 6)
        assert messages[0].code == "type_error"

# Generated at 2022-06-14 14:49:06.910128
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema.of({"name": Field(str, required=True)})
    token = Token({"name": ""}, start=Token.Position(0, 0, 0), end=Token.Position(2, 0, 0))
    with raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    assert exc_info.value.messages() == [Message(text="The field 'name' is required.", code="required", index=[], start_position=Token.Position(0, 0, 0), end_position=Token.Position(2, 0, 0))]

# Generated at 2022-06-14 14:49:11.875133
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """This test is just to improve coverage"""
    import json

    data = json.loads("""{"hello": {"world": "!"}}""")
    token = Token(data)

    class Hello(Schema):
        world = Field(str)

    validate_with_positions(token=token, validator=Hello)

# Generated at 2022-06-14 14:49:24.241662
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.fields import String
    from typesystem.fields import String
    from typesystem.fields import String
    from typesystem.fields import String

    class Person(Schema):
        name = String(max_length=8)
        age = String(max_length=8)
        email = String(max_length=8)
        password = String(max_length=8)

# Generated at 2022-06-14 14:49:34.630191
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer, Array
    from typesystem.schemas import BaseSchema
    from typesystem.tokenize.parser import parse

    class Person(BaseSchema):
        id = Integer(required=False)
        name = String(required=True)
        friends = Array(items=Person(required=True))

    class Root(BaseSchema):
        person = Person(required=True)

    token = parse('{"person": {"name": "", "friends": []}}')

    try:
        validate_with_positions(token=token, validator=Root())
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2
        assert messages[0].text == "The field 'name' is required."
        assert messages[0].start_position.char

# Generated at 2022-06-14 14:49:41.138939
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import String

    data = """
    {
        "name": {
            "first": "Tester"
        },
        "phone": "555-555-5555"
    }
    """
    token = Token.from_data(data)
    assert token["phone"].value == "555-555-5555"
    phone = String(max_length=10)
    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token["phone"], validator=phone)

# Generated at 2022-06-14 14:49:49.727871
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import typesystem

    class ExampleSchema(typesystem.Schema):
        name = typesystem.String(max_length=10)
        age = typesystem.Integer()

    # Missing name
    example_dict = {"age": 20}
    example_str = json.dumps(example_dict)
    token = Token(example_str)
    with pytest.raises(typesystem.exceptions.ValidationError) as exc:
        validate_with_positions(token=token, validator=ExampleSchema)
    assert exc.value.messages[0].start_position.line == 1
    assert exc.value.messages[0].start_position.char_index == 2

    # Missing age
    example_dict = {"name": "Larry"}

# Generated at 2022-06-14 14:50:00.441029
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object
    from typesystem.types import String

    class User(Object):
        name = String()
        age = String()

    token = Token(
        value={"name": "Steve"},
        items={
            "name": Token(
                value="Steve", start={"line": 0, "char": 10}, end={"line": 0, "char": 15}
            )
        },
        start={"line": 0, "char": 0},
        end={"line": 0, "char": 16},
    )

# Generated at 2022-06-14 14:50:10.753316
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String
    from typesystem.tokenize.parser import parse_string

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=parse_string("{}"), validator=String(required=True))
    assert exc_info.value.messages() == [
        Message(
            code="required",
            index=["data", "name"],
            text="The field 'name' is required.",
            start_position=Position(line=1, char_index=1),
            end_position=Position(line=1, char_index=2),
        )
    ]



# Generated at 2022-06-14 14:50:18.611511
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    from ..schemas import ExampleSchema

    schema = ExampleSchema()

    token = tokenize("hello [name]")

    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        assert len(error.messages) == 1
        message = error.messages[0]
        assert message.start_position.line_index == 0
        assert message.start_position.char_index == 9
        assert message.end_position.line_index == 0
        assert message.end_position.char_index == 17

        assert message.text == "The field 'name' is required."

    token = tokenize("hello [name]\n[name]")


# Generated at 2022-06-14 14:50:28.398216
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer
    from typesystem.tokenize.tokenize import Tokenizer

    tokenizer = Tokenizer(
        {
            "integer": Integer(default=0, minimum=1, maximum=100),
            "string": Integer(default="a"),
        }
    )
    token = tokenizer.tokenize("")
    try:
        validate_with_positions(token=token, validator=tokenizer.schema)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        message = messages[0]
        assert message.index == ["integer"]
        assert message.start_position.char_index == 0
        assert message.start_position.line_index == 1
        assert message.end_position.char_index == 0

# Generated at 2022-06-14 14:50:40.074134
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import tokenize_string
    from typesystem.fields import String
    from typesystem.base import FormatError

    tokens = tokenize_string("[{}, {}]")
    tokens = tokens[1]  # type: ignore

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(
            token=tokens, validator={"type": "string", "format": "email"}
        )
    message = excinfo.value.messages[0]
    assert message.text == "Invalid format."
    assert message.start_position == tokens[0][0].start
    assert message.end_position == tokens[0][1].end

    string_field = String()
    string_field.format("email")

# Generated at 2022-06-14 14:50:52.393824
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import tokenize, TokenType

    from tests.examples import Pet

    class Dog(Pet):
        dog_field = Field(type=str, required=True)

    tokens = tokenize("""
        {
            "name": "balto",
            "age": 12,
            "size": "large"
        }
    """)

    results = []
    for token in tokens:
        if token.type == TokenType.OBJECT:
            results.append(validate_with_positions(
                token=token, validator=Dog))
        else:
            results.append(token.value)


# Generated at 2022-06-14 14:51:03.504844
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import IntegerField, Schema, StringField
    from typesystem.tokenize.tokens import DocumentToken, ElementToken
    from typesystem.tokenize.utils import tokenize

    user = Schema({"name": StringField(), "age": IntegerField()})
    token = tokenize("{name: 'hello', age: 'not an age'}")
    assert isinstance(token, DocumentToken)
    assert list(token.keys()) == ["data"]
    child = token["data"]
    assert isinstance(child, ElementToken)
    assert list(child.keys()) == ["name", "age"]

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=child, validator=user)

# Generated at 2022-06-14 14:51:14.565040
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Object, String as StringToken

    class Author(Schema):
        name = String()

    class Book(Schema):
        author = Author()
        title = String(required=True)

    data = {
        "author": {"name": "John"},
        "title": "The Meaning of Life",
    }
    token = Object({
        "author": Object({"name": StringToken("John")}),
        "title": StringToken("The Meaning of Life"),
    })

    result = validate_with_positions(token=token, validator=Book)

    assert result == data



# Generated at 2022-06-14 14:51:30.826254
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """Unit test for function validate_with_positions"""
    from typesystem.fields import Int
    from typesystem.schemas import Structure

    class Person(Structure):
        name = Field(str)
        age = Field(Int())

    person = Person()

    token = Token(value={"name": "Eric", "age": "42"})

    assert validate_with_positions(token=token, validator=person) == {}

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=person)
    error: ValidationError
    assert len(error.value.messages) == 1
    message = error.value.messages[0]
    assert message.index == ("age",)
    assert message.start_position.line == 1

# Generated at 2022-06-14 14:51:40.350793
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from json import loads
    from typesystem.fields import String

    json_string = """{"foo": "bar"}"""
    token = Token.from_json(json_string)

    # Check that ValidationError is raised
    string_field = String()
    with pytest.raises(ValidationError, match="The field 'bar' is required."):
        validate_with_positions(token=token, validator=string_field)

    # Check that ValidationError is raised
    json_string = '{"bar": "baz"}'
    token = Token.from_json(json_string)
    string_field = String(required=True)
    with pytest.raises(ValidationError, match="The field 'bar' is required."):
        validate_with_positions(token=token, validator=string_field)

# Generated at 2022-06-14 14:51:41.950955
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # TODO: Write unit test for this function.
    pass

# Generated at 2022-06-14 14:51:53.330338
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.json_schema import JSONSchema

    token = Token(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "location": {"type": "string"},
            },
            "required": ["name"],
        }
    )

    schema = JSONSchema.parse(token.value)

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=schema)


# Generated at 2022-06-14 14:52:00.443112
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import TextToken
    from typesystem.tokenize.tokenize import tokenize
    from typesystem.fields import Dict, Text
    from typesystem import ValidationError

    class FooDict(Dict):
        foo = Text(required=True)

    token = tokenize(FooDict(), {"foo": "Hello"}, source="main.json")
    try:
        # This should succeed
        validate_with_positions(token=token, validator=FooDict())
    except ValidationError as error:
        print(error.json())

# Generated at 2022-06-14 14:52:13.002750
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem import types, validators
    from typesystem.tokenize.tokenizer import Tokenizer

    class MySchema(Schema):
        name = types.String(required=True, validators=[validators.Length(max=5)])
        age = types.Integer()

    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(
        {
            "name": "John Doe",
            "age": 0,
            "middle": "middle",
            "sub": {
                "sname": "John Doe",
                "sage": "0",
                "smiddle": "middle",
                "ssub": {
                    "ssname": "John Doe",
                },
            },
        }
    )

    my_schema = MySchema()
   

# Generated at 2022-06-14 14:52:22.102031
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(type="string")

    schema = Schema(
        properties={"foo": {"type": "string", "title": "Foo"}}
    )

    token = Token.object(value={"foo": "bar"}, start=0, end=1000)

    with pytest.raises(ValidationError) as exception_info:
        validate_with_positions(token=token, validator=field)
    assert (
        str(exception_info.value)
        == "The field 'foo' is required. (code: required)"
    )
    for message in exception_info.value.messages():
        assert message.start_position == (0, 0)
        assert message.end_position == (1000, 1000)

    with pytest.raises(ValidationError) as exception_info:
        validate_

# Generated at 2022-06-14 14:52:30.028304
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import lex, parse, PyParsingSyntaxError
    from typesystem.fields import String, Integer, Float

    def assert_positions(token, field, expected_position):
        try:
            validate_with_positions(token=token, validator=field)
        except ValidationError as error:
            assert error.messages()[0].start_position == expected_position, \
                error.messages()[0].start_position
        else:
            assert False, "Expected to raise ValidationError"

    # String field
    field = String()
    token = lex("""
        {
            "a": "b",
            "c": "d"
        }
    """)
    token = parse(token)

# Generated at 2022-06-14 14:52:38.921222
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Document
    from typesystem.fields import Integer
    from typesystem.tokenize.streams import Stream

    schema = {
        "number": Integer(),
    }
    stream = Stream(schema=schema)
    document = Document(stream=stream)
    token = document.lookup(["number"])

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=Integer())

    message = excinfo.value.messages[0]
    assert message.text == "This field is required."

# Generated at 2022-06-14 14:52:47.947073
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import pytest
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token

    class PersonSchema(Schema):
        name = Field(max_length=32)
        age = Field(type="integer")
        bio = Field(max_length=64)

    class FamilySchema(Schema):
        father = Field(type="object", schema=PersonSchema)
        mother = Field(type="object", schema=PersonSchema)

    # Error
    with pytest.raises(ValidationError) as excinfo:
        with open("tests/data/family.json") as file:
            data = json.load(file)
        token = Token.from_data(data)
        validate_with_positions(token=token, validator=FamilySchema)

# Generated at 2022-06-14 14:53:11.797724
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Test that it works with a simple field
    field = Field(type="string")

    # Test that it works with an error from the field
    err = pytest.raises(ValidationError, validate_with_positions, token=Token(None), validator=field)
    assert err is not None

    messages = err.value.messages()
    assert len(messages) == 1
    assert messages[0].text == "This field is required."

    # Test that it works with a schema
    schema = type(
        "MySchema",
        (Schema,),
        {
            "name": Field(type="string"),
            "age": Field(type="integer"),
            "address": Field(type="string"),
        },
    )

    # Test that point to the field when it fails

# Generated at 2022-06-14 14:53:23.304601
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.fields import String, Integer, Choice
    from typesystem.schemas import Schema, pre_load

    class UserSchema(Schema):
        id = Integer()
        name = String()
        login_type = Choice(choices=["student", "admin"])

    with open("file.json", "wb") as f:
        f.write(
            b"""
        {
            "id": 5,
            "favorite_number": "6", # <- should fail
            "login_type": "teacher" # <- should fail
        }
        """
        )

    tokens = pre_load(open("file.json", "rb").read())


# Generated at 2022-06-14 14:53:34.836560
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from json import loads
    from typesystem.exceptions import UnsupportedTokenError
    from typesystem.schemas import Schema
    from typesystem.fields import (
        IntegerField,
        StringField,
        ObjectField,
        ArrayField,
    )
    from typesystem.tokenize.tokens import (
        ObjectToken,
        ArrayToken,
        IntegerToken,
        StringToken,
        NullToken,
    )
    from typesystem.tokenize.positions import Position

    if PY35:
        return  # pragma: no cover

    class Post(ObjectField):
        title = StringField()
        body = StringField()

    class User(ObjectField):
        username = StringField()
        posts = ArrayField(items=Post)


# Generated at 2022-06-14 14:53:41.296923
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(type="string")

    token = Token(name="person", value={"name": ""})

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Person)

    error = exc_info.value
    message = error.messages[0]
    assert message.code == "required"
    assert message.text == "The field 'name' is required."
    assert message.start_position == (1, 2)
    assert message.end_position == (1, 2)

# Generated at 2022-06-14 14:53:49.147753
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class TestSchema(Schema):
        field = Field(required=True)

    token = Token("test", value={"field": "value"})
    validate_with_positions(token=token, validator=TestSchema)

    token = Token("test", value={})
    try:
        validate_with_positions(token=token, validator=TestSchema)
    except ValidationError as error:
        assert len(error.messages()) == 1

# Generated at 2022-06-14 14:54:00.673420
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.schemas import Object

    class MySchema(Object):
        field = String(required=True)

    token = Token.create({"field": "value"})

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token.lookup(["field"]), validator=Boolean())

    assert error.value.messages == [
        Message(
            text="Expected a boolean.",
            code="invalid",
            index=["field"],
            start_position=token.lookup(["field"]).start,
            end_position=token.lookup(["field"]).end,
        )
    ]


# Generated at 2022-06-14 14:54:07.768947
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        start=Token.Position(row=1, column=1, char_index=0),
        end=Token.Position(row=1, column=2, char_index=1),
        value="a",
    )
    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=None)
    assert len(error.value.messages) == 1
    message = error.value.messages[0]
    assert message.code == "required"
    assert message.text == "The field None is required."
    assert message.index == []
    assert message.start_position == Token.Position(row=1, column=1, char_index=0)

# Generated at 2022-06-14 14:54:17.137870
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.exceptions import ValidationError
    from typesystem.fields import IntegerField
    from typesystem.tokenize.parser import parse_string

    try:
        validate_with_positions(token=parse_string("12.34"), validator=IntegerField())
    except ValidationError as error:
        messages = list(error.messages())
    else:
        raise AssertionError("ValidationError not raised")

    assert len(messages) == 1
    assert messages[0].code == "invalid_type"
    assert messages[0].text == (
        'Expected an integer value, but received a float value instead.'
    )
    assert messages[0].index == []
    assert messages[0].start_position.index == 0
    assert messages[0].start_position.line == 1

# Generated at 2022-06-14 14:54:26.494484
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Document
    from typesystem.fields import String

    class MySchema(Schema):
        a = String(min_length=1)
        b = String(max_length=1)

    document = Document(
        '{"a": "", "b": ""}',
    )

    try:
        validate_with_positions(token=document, validator=MySchema())
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2
        start, end = messages
        assert start.start_position.line_no == 1
        assert start.start_position.char_index == 2  # type: ignore
        assert start.start_position.column_no == 3  #

# Generated at 2022-06-14 14:54:36.280074
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parsers import python
    from typesystem.validators import String

    tokens = python.tokenize("foo")

    assert validate_with_positions(token=tokens[0], validator=String()) == "foo"

    try:
        validate_with_positions(token=tokens[0], validator=String(max_length=2))
    except ValidationError as error:
        assert len(error.messages()) == 1
        message = error.messages()[0]
        assert message.text == "The field '' must be at most 2 characters long."
        assert message.start_position.line == 1
        assert message.start_position.char_index == 0
        assert message.end_position.line == 1
        assert message.end_position.char_index == 3
   

# Generated at 2022-06-14 14:55:14.059502
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import types

    class Person(Schema):
        name = types.String(required=True)

    token = Token.from_value(
        {
            "name": "Alice",
            "age": 42,
            "birth_date": "unknown",
            "friends": [],
            "lucky_number": None,
        }
    )