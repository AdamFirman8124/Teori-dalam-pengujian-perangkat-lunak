

# Generated at 2022-06-14 14:45:22.353904
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import StringToken, ObjectToken
    from .test_types import UserSchema
    from typesystem.compat import json

    class UserToken(ObjectToken):
        schema = UserSchema


# Generated at 2022-06-14 14:45:30.958318
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from typesystem.schemas import Schema
    from typesystem.fields import String, Number, Boolean, Integer
    from typesystem.tokenize.tokenize import Tokenize
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.positions import Positions

    class Example(Schema):
        name = String()
        age = Integer()
        adult = Boolean()
        height = Number()

    tokens = Tokenize("example.json")

# Generated at 2022-06-14 14:45:36.184825
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import IntegerField, StringField
    from typesystem.schemas import Schema

    class BookSchema(Schema):
        title = StringField()
        pages = IntegerField()

    token = Token(
        {
            "title": "Life, the Universe and Everything",
            "pages": 42,
        },
        start=(1, 0),
        end=(1, 0),
    )

    validate_with_positions(token=token, validator=BookSchema)



# Generated at 2022-06-14 14:45:48.007168
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import typesystem

    class ZipCode(typesystem.String):
        pattern = r"^\d{4,8}(?:[-\s]\d{4})?$"

    class Person(typesystem.Schema):
        name = typesystem.String(max_length=255)
        zipcode = ZipCode()

    data = {"name": "Petr", "zipcode": "4330"}
    token = Token.from_native(data)
    validate_with_positions(token=token, validator=Person)

    data = {"name": "Petr", "zipcode": "4330-12"}
    token = Token.from_native(data)

# Generated at 2022-06-14 14:45:56.741391
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """Ensure that the positional information is maintained."""
    from typesystem.tokenize.tokens.objects import ObjectToken
    from typesystem.fields import String

    validator = String(required=True)

    errors = None
    try:
        validate_with_positions(
            token=ObjectToken(
                start={"line_index": 0, "char_index": 0},
                end={"line_index": 0, "char_index": 3},
                value={},
            ),
            validator=validator,
        )
    except ValidationError as error:
        errors = error

    assert errors is not None

    message = errors.messages()[0]
    assert message.start_position == {"line_index": 0, "char_index": 0}

# Generated at 2022-06-14 14:46:08.356200
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class Profile(Schema):
        first_name = Field(str, required=True)
        last_name = Field(str, required=True)

    json = """{
        "first_name": "Jane",
        "last_name": "Doe",
        "age": 35
    }"""
    tokens = tokenize(json)["Profile"]
    try:
        validate_with_positions(token=tokens, validator=Profile)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2
        assert messages[0].text == "The field 'age' is not a valid field."
        assert messages[0].start_position.line == 3
        assert messages[0].start_position.char_index == 6


# Generated at 2022-06-14 14:46:18.043483
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.schemas import Object
    from typesystem.fields import String

    class MySchema(Object):
        name = String(required=False)

    schema = MySchema()
    token = tokenize('{"name": 1234}')
    try:
        res = validate_with_positions(token=token, validator=schema)
    except ValueError as error:
        assert error.message == Message(
            text='Expected type "string", received type "number".',
            code="type_error.string",
            index=(),
            start_position=token.start_position,
            end_position=token.end_position,
        )
    else:
        raise AssertionError(res)

# Generated at 2022-06-14 14:46:24.453468
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(value={"foo": None}, start=(1, 1), end=(10, 1))
    validator = Field(type="string", required=True)

    # assert that the error contains positional information
    try:
        validate_with_positions(token=token, validator=validator)
    except ValidationError as error:
        message = error.message()
        assert message.code == "required"
        assert message.index == ("foo",)
        assert message.start_position == (2, 5)
        assert message.end_position == (2, 8)
    else:
        assert False

# Generated at 2022-06-14 14:46:35.258227
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize_yaml
    from typesystem.tokenize.tokens import Token

    field = Field(type="string")
    # The text below is not valid yaml, but is still valid enough
    # to be tokenize
    text = """
    foo:
      bar: true
    """
    token = tokenize_yaml(text=text)
    assert isinstance(token, Token)

    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        message = messages[0]
        assert message.text == "The field foo.bar is required."
        assert message.code == "required"
        assert message.index == ("foo", "bar")

# Generated at 2022-06-14 14:46:44.375811
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import ObjectToken
    from typesystem.tokenize.tokenize import tokenize

    class TestSchema(Schema):
        foo = Field(type="integer", required=True)
        bar = Field(type="integer", required=True)
        baz = Field(type="integer")

    schema = TestSchema()

    token = tokenize(
        '{"foo": 1, "bar": 2, "baz": "not a number!"}',
        start_position=Position(line=3, char_index=12),
    )


# Generated at 2022-06-14 14:46:56.211753
# Unit test for function validate_with_positions
def test_validate_with_positions():

    def test_suite(
        input: str, output: typing.Any, error_message: str,
    ):
        token = Token.parse(input)
        try:
            result = validate_with_positions(token=token, validator=Field())
            assert result == output
        except ValidationError as error:
            message = str(error)
            assert message == error_message

    test_suite(input='"foo"', output='foo', error_message="")
    test_suite(
        input='{"foo": "bar"}',
        output={"foo": "bar"},
        error_message="The field 'foo' is required.",
    )


validate = validate_with_positions

# Generated at 2022-06-14 14:47:07.360313
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import parse_token

    token_str = """\
        {
            "a": "hello",
            "b": 1,
        }
    """
    token = parse_token(token_str)

    from typesystem.fields import String, Integer, Array, Object

    class NestedSchema(Schema):
        foo_list = Array(String())

    class TestSchema(Schema):
        a = String()
        b = Integer()
        c = Object(NestedSchema)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=TestSchema)

    messages = exc_info.value.messages()
    assert not messages[0].index


# Generated at 2022-06-14 14:47:14.362693
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Schema, types

    class Person(Schema):
        name = types.String()
        age = types.Integer()

    import json

    string = '{"name": "john", "age": "???"}'
    token = json.loads(string)
    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.code == "invalid_integer"
        assert message.text == "The supplied value is not an integer."
        assert message.start_position == (2, 16)

# Generated at 2022-06-14 14:47:26.031473
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token

    def start_position(field: str, line: int, column: int) -> Position:
        return Position(field=field, line=line, column=column)

    schema = Schema(fields={"a": Field(required=True)})
    token = Token(
        value={"b": "b"},
        start=start_position("", line=1, column=1),
        end=start_position("", line=1, column=4),
    )
    ex = pytest.raises(ValidationError)
    with ex as exc_info:
        validate_with_positions(token=token, validator=schema)
    assert exc_info.value.message == "The field 'a' is required."


# Generated at 2022-06-14 14:47:35.593250
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema(fields={"first_name": Field()})
    token = (
        Token(value={"last_name": "Smith"}, start=(1, 1), end=(1, 1))
        .descend("first_name")
        .descend("last_name")
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    message = exc_info.value.messages[0]
    assert message.start_position == (1, 27)
    assert message.end_position == (1, 32)
    assert message.text == "The field 'first_name' is required."
    assert message.code == "required"

# Generated at 2022-06-14 14:47:43.290295
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Boolean, Array

    class Person(Schema):
        name = String(min_length=1)
        connected = Boolean()

    data = """
    - name:
        - something
      connected: true
    """

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=Token.parse(data), validator=Array(item=Person)
        )
    message = exc_info.value.messages[0]
    assert message.start_position.char_index == 13



# Generated at 2022-06-14 14:47:53.913458
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    # Tests that we can get the correct field names from dot notation
    schema = Schema({"a.b": Field(type=str)})
    token = tokenize({"a": {"b": 42}})
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(validator=schema, token=token)

    error = excinfo.value
    assert error.messages() == [
        Message(
            index=(0,),
            text="The field 'b' is required.",
            code="required",
            start_position=token.start,
            end_position=token.end,
        )
    ]

# Generated at 2022-06-14 14:48:06.118439
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    from typesystem.tokenize import tokenizers
    from typesystem.tokenize.tokens import Token

    schema = typesystem.Schema(
        {"a": typesystem.Integer(), "b": typesystem.Integer(), "c": typesystem.Integer()},
        required=["a", "b", "c"],
    )
    tokenizer = tokenizers.JSONTokenizer()
    tokens = tokenizer.tokenize({"b": "two"})
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, Token)

# Generated at 2022-06-14 14:48:16.789535
# Unit test for function validate_with_positions
def test_validate_with_positions():
    x = Token("{'name': 'Joe'}", 0, 15)
    class Person(Schema):
        name = Field(str, required=True)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=x, validator=Person)
    message = exc_info.value.messages[0]
    assert message.index == ("name",)
    assert message.text == "The field 'name' is required."
    assert message.start_position.line_number == 1
    assert message.start_position.char_index == 2
    assert message.end_position.line_number == 1
    assert message.end_position.char_index == 7

# Generated at 2022-06-14 14:48:27.632816
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import (
        Array,
        Boolean,
        Integer,
        Literal,
        Number,
        Object,
        String,
    )

    class User(Schema):
        username = String()
        age = Integer(minimum=0, maximum=100)
        password = String(min_length=8)

    class Post(Schema):
        title = String()
        body = String()
        tags = Array(items=String())

    class CreatePostRequest(Schema):
        author = User()
        post = Post()


# Generated at 2022-06-14 14:48:40.722285
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Clear
    from typesystem.tokenize.tokens import Array, FieldToken, ListToken

    class Schema(Clear):
        values = validate_with_positions(
            token=Array("values"),
            validator=ListToken(
                value_type=FieldToken(
                    name="value",
                    validator=Nullable(Integer()),
                ),
                min_length=1
            ),
        )

    errors = Schema.validate.validate({"values": []}).messages
    assert errors == [
        Message(text="The field 'value' is required.", code="required")
    ]



# Generated at 2022-06-14 14:48:50.407957
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.test_tokens import Source, Position
    from tests.test_fields import String, Number
    from typesystem.fields import Integer

    token = Token("title", "string", value="foo", start=Position(line=1, char_index=0))
    token = token.lookup("products")
    token = token.lookup("1")
    token = token.lookup("variants")
    token = token.lookup("1")
    token = token.lookup("price")
    token = token.lookup("inr")
    token = token.lookup("value")


# Generated at 2022-06-14 14:48:55.652859
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token("abc")
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=Field(type="string"))
    message = exc.value.messages[0]
    assert message.start_position.char_index == 1
    assert message.end_position.char_index == 1

# Generated at 2022-06-14 14:49:04.966938
# Unit test for function validate_with_positions

# Generated at 2022-06-14 14:49:16.955172
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, String, Struct

    class Person(Struct):
        first_name = String(max_length=10)  # type: ignore
        last_name = String(max_length=10)  # type: ignore
        age = Integer(min_value=18)  # type: ignore

    token = Token(
        type="object",
        start=Position(line=1, column=2, char_index=1),
        end=Position(line=1, column=11, char_index=10),
        value={
            "first_name": "Robert"
        },
    )

    try:
        validate_with_positions(token=token, validator=Person())
    except ValidationError as error:
        for message in error.messages():
            assert message.start_position.char_index == 6

# Generated at 2022-06-14 14:49:28.984476
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import from_json
    from typesystem import types
    from typesystem import validation_error
    from typesystem.exceptions import ValidationError

    from .helpers import _check_error

    class PointSchema(Schema):
        x = types.Integer(required=True)
        y = types.Integer(required=True)

    source = """
    {
        "x": 1
    }
    """
    token = from_json(source)

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=PointSchema)

# Generated at 2022-06-14 14:49:38.358179
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # type: () -> None
    from typesystem.schemas import Schema
    from typesystem.types import Integer

    class MySchema(Schema):

        field1 = Integer()
        field2 = Integer()

    token = Token(
        start_location=Token.SourceLocation(line_index=10, char_index=20),
        end_location=Token.SourceLocation(line_index=10, char_index=30),
        value={
            "field2": "hello",
            "field1": "1",
        },
    )
    try:
        validate_with_positions(token=token, validator=MySchema)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        message = messages[0]

# Generated at 2022-06-14 14:49:45.944374
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizers import string_tokenizer
    from typesystem.fields import String
    from typesystem.exceptions import ValidationError

    token = string_tokenizer.tokenize("foo = 'bar'", start=0)
    field = Field(
        name="foo",
        field_type=String(),
        default="",
        required=True,
        description="A foo.",
    )
    value = validate_with_positions(token=token, validator=field)
    assert value == "bar"

    token = string_tokenizer.tokenize("bar", start=0)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=field)
    message = exc_info.value.messages()[0]
   

# Generated at 2022-06-14 14:49:57.884538
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.enums import Enum
    from typesystem.types import String
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.parsers import parse_json_string

    class Color(Enum):
        red = "red"
        green = "green"
        blue = "blue"

        class Meta:
            nullable = True

    class Person(Schema):
        name = String(required=True)
        color = Color()

    json_str = '{"name": "John", "color": 123}'
    root = parse_json_string(json_str)

    with pytest.raises(ValidationError) as exc_info:
        Person.validate(root)

    message = exc_info.value.messages[0]

# Generated at 2022-06-14 14:50:10.176279
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse_string

    token = parse_string(
        """
    {
        "a": "a",
        "b": "hello",
        "c": [1, 2, 3],
        "d": null,
        "e": "",
        "f": [
            "a",
            "b",
            3,
        ]
    }
    """
    )

    class TestSchema(Schema):
        a = Field(string_types)
        b = Field(string_types)
        c = Field(array_types)
        d = Field(array_types, nullable=True)
        e = Field(string_types, required=False)
        f = Field(array_types, items=string_types)


# Generated at 2022-06-14 14:50:23.522658
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(
        name="foo",
        description="Description for foo",
    )

    with pytest.raises(ValidationError) as execinfo:
        validate_with_positions(
            token=Token(
                name="foo",
                value=None,
                start=Position(char_index=0, byte_index=0, line=1, column=1),
                end=Position(char_index=3, byte_index=3, line=1, column=4),
            ),
            validator=field,
        )
    assert execinfo.value.messages()[0].text == "The field 'foo' is required."



# Generated at 2022-06-14 14:50:30.328841
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import fields
    import json

    class User(Schema):
        name = fields.String()
        age = fields.Integer()

    json_token = Token("{name: 'John', age: 'invalid'}")
    try:
        validate_with_positions(token=json_token, validator=User)
    except ValidationError as error:
        errors = error.format_errors()
        lines = []
        for field, messages in errors.items():
            for text in messages:
                lines.append(f"Field '{field}': {text}")

        assert len(errors) == 1
        text = "\n".join(lines)

# Generated at 2022-06-14 14:50:41.243735
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import os.path
    import pkg_resources
    import pytest
    from pprint import pformat
    from typesystem import Schema, fields
    from typesystem.tokenize import open_file, tokenize
    from typesystem.types import Boolean, Integer

    schema = Schema(
        {
            "a": fields.Array(fields.Integer()),
            "b": Boolean(),
            "c": fields.String(description="description"),
            "d": fields.Dict({"e": Integer()}),
            "f": Boolean(),
            "g": Integer(),
            "h": fields.Dict({"i": Integer(), "j": fields.Object({"k": Integer()})}),
        }
    )


# Generated at 2022-06-14 14:50:53.360519
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.parse import parse_schema
    from typesystem.tokenize.tokens import ObjectToken
    from typesystem.tokenize.tokens import ScalarToken
    from typesystem.tokenize.tokens import Source
    from typesystem.tokenize.tokens import Token

    source = Source("""
        {
            "foo": "bar",
            "baz": 5
        }
    """.strip())
    token = Token.parse(source)
    assert isinstance(token, ObjectToken)

    schema = parse_schema(
        input_data="""
        type: object
        properties:
            foo:
                type: string
        """,
        source=source,
    )
    assert isinstance(schema, Schema)


# Generated at 2022-06-14 14:51:02.008215
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import typesystem
    from typesystem.fields import String

    class Person(typesystem.Schema):
        name = String(min_length=5)

    raw_text = '{ "name": "Vitor" }'
    token = json.loads(raw_text).tokenize()
    with pytest.raises(ValidationError) as validation_error:
        validate_with_positions(token=token, validator=Person())
    assert validation_error.value.messages()[0].text == (
        'Ensure this value has at least 5 characters (it has 4).'
    )

# Generated at 2022-06-14 14:51:15.125161
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class TestSchema(Schema):
        name = Field(type="string", required=True)

    source = "{'name': 'John Doe'}"
    token = tokenize(source, start=0, end=None)
    name, = TestSchema.validate_with_positions(token=token)
    assert name == "John Doe"

    source = "{}"
    token = tokenize(source, start=0, end=None)
    try:
        TestSchema.validate_with_positions(token=token)
    except ValidationError as error:
        message = error.messages[0]
        assert not message.start_position.line
        assert not message.start_position.char_index
        assert not message.end_position.line
        assert not message

# Generated at 2022-06-14 14:51:27.144971
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Author(Schema):
        name = Field(str, required=True)
        age = Field(int, required=True)

    class Book(Schema):
        title = Field(str, required=True)
        author = Field(Author, required=True)

    document = {
        "title": "The Art of Computer Programming",
        "author": {"age": 53},
    }
    token = Token(document)

    try:
        schema = Book()
        schema.validate(document)
    except ValidationError as error:
        assert error.messages() == [
            Message(text="The field 'name' is required.", code="required", index=[1, 0]),
            Message(
                text="The field 'author' is required.",
                code="required",
                index=[2],
            ),
        ]
   

# Generated at 2022-06-14 14:51:37.422515
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import JSONSchema
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.exceptions import TokenizeError

    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer", "minimum": 0, "maximum": 100},
        },
        "required": ["name"],
    }

    validator = JSONSchema(schema)
    tokens = list(tokenize('{"name": "Bob", "age": 200}'))
    assert tokens[-1].start.char_index == 0

    try:
        validate_with_positions(token=tokens[-1], validator=validator)
    except TokenizeError as error:
        errors = error.get_errors()

# Generated at 2022-06-14 14:51:48.840899
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.streaming import TokenStream
    from typesystem.tokenize import Tokenizer

    schema = Schema.parse({
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
            },
            "age": {
                "type": "number",
            },
        },
        "required": ["name", "age"],
    })

    # Tokenize the value
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize({"name": "Foo", "age": "20"})

    try:
        validate_with_positions(token=tokens, validator=schema)
    except ValidationError as error:
        messages = [message.text for message in error.messages]

# Generated at 2022-06-14 14:51:51.680254
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import Array, String

    class Person(Schema):
        name = String(required=True)
        a

# Generated at 2022-06-14 14:52:03.692775
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import lexers
    from typesystem.tokenize.parser import Parser
    from typesystem.tokenize.tokens import Emit

    parser = Parser(lexer=lexers.whitespace_sensitive)
    token = parser.parse(".abc.def").token
    assert validate_with_positions(token=token, validator=Field(name="abc")) == token
    assert validate_with_positions(
        token=token, validator=Field(name="ghi")
    ) is Emit.stop

# Generated at 2022-06-14 14:52:13.544337
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # mock type system
    class SchemaMock(Schema):
        field = Field(type="integer")

    with pytest.raises(ValidationError) as error:
        # this should fail because the value is a string not an int
        validate_with_positions(token=Token(value=""), validator=SchemaMock)

    assert error.value.messages == [
        Message(
            code="type",
            text="Value must be of type integer.",
            index=[0, "field"],
            start_position=Position(byte_index=0, char_index=0),
            end_position=Position(byte_index=0, char_index=0),
        )
    ]



# Generated at 2022-06-14 14:52:22.270759
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Object, String, Integer
    from typesystem.tokenize.tokens import ObjectToken

    data = {
        "foo": "bar",
        "baz": {
            "name": "Harry",
            "age": 42,
            "password": "**********",
        },
    }
    object_token = ObjectToken(
        [
            ("foo", "bar"),
            ("baz", {
                "name": "Harry",
                "age": 42,
                "password": "**********",
            }),
        ],
        start=0,
        end=50,
    )

# Generated at 2022-06-14 14:52:30.098216
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokenize

    token = tokenize(
        """{
    "foo": "hello",
    "bar": "world",
    "baz": 10,
    "qux": 20.0
}"""
    )

    schema = Schema(
        {
            "foo": String(max_length=1),
            "bar": String(required=False),
            "baz": Integer(maximum=11),
            "qux": Integer(),
            "quux": Integer(required=False),
        }
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)

    messages = exc_info

# Generated at 2022-06-14 14:52:41.489922
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest

    from typesystem.declarations import Array, Boolean, Integer, Object, String
    from typesystem.fields import Field
    from typesystem.tokenize.tokens import Token

    tok0 = Token(value=None, start=0, end=0)
    tok1 = Token(value=None, start=0, end=0)
    tok2 = Token(value=None, start=0, end=0)
    tok3 = Token(value=None, start=0, end=0)
    tok4 = Token(value=None, start=0, end=0)
    tok5 = Token(value=None, start=0, end=0)
    tok0.children = [tok1, tok5]
    tok1.children = [tok2, tok3]

# Generated at 2022-06-14 14:52:49.479046
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from pprint import pformat
    from typesystem import types
    from typesystem.fields import String

    class MySchema(types.Schema):
        name = String()

    raw_data = [{"name": "Janet"}, {"name": "Janet", "email": "janet@j.net"}]
    token = Token.from_python_value(raw_data)
    try:
        validate_with_positions(token=token, validator=MySchema)
    except ValidationError as e:
        error = e
        assert len(error.messages) == 1
        message = error.messages[0]

# Generated at 2022-06-14 14:53:00.016783
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse
    from typesystem.tokenize.lines import Position, Line
    from typesystem.fields import Integer

    pos1 = Position(line=Line(1, 1, 1), char_index=0)
    pos2 = Position(line=Line(1, 1, 1), char_index=1)

    token = Token(
        raw={"a": 1, "b": -1, "c": "1"},
        start=pos1,
        end=pos2,
        lookup=lambda p: token,  # type: ignore
    )

    assert validate_with_positions(token=token, validator=Integer(min=0)) == 1
    assert token.value == 1

    # Test an error message
    with pytest.raises(ValidationError) as exc:
        validate_with

# Generated at 2022-06-14 14:53:10.055786
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from pytest import raises
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import Token

    text = """
    # An example document
    - hi
    - bye
    """
    tokens = tokenize(text)

    def validator(value):
        if value != "hi":
            raise ValidationError(
                [Message("The value should be 'hi'!", code="invalid")]
            )
        return value

    assert validate_with_positions(token=tokens.lookup("0"), validator=validator) == "hi"

    with raises(ValidationError):
        validate_with_positions(token=tokens.lookup("1"), validator=validator)



# Generated at 2022-06-14 14:53:21.739626
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexer import parse_string
    from typesystem.fields import String
    
    class DemoSchema(Schema):
        foo = String(pattern=r"\d+")
        bar = String()  # <-- intentionally optional

    token = parse_string(b'{"foo": "1", "bar": "2"}')
    try:
        validate_with_positions(token=token, validator=DemoSchema)
    except ValidationError as error:
        assert error.messages()[0].index == ["foo"]
        assert error.messages()[0].start_position.line == 0
        assert error.messages()[0].end_position.line == 0
        assert error.messages()[0].start_position.char_index == 9

# Generated at 2022-06-14 14:53:33.093439
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.exceptions import ValidationError
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.tokens import TokenType

    class CarSchema(Schema):

        wheels = Field(primitive_type=int)
        doors = Field(primitive_type=int)
        name = Field(primitive_type=str)
        color = Field(primitive_type=str)


# Generated at 2022-06-14 14:53:50.049544
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import marshmallow_typesystem as mst
    import typesystem
    my_field = typesystem.Number()

    assert validate_with_positions(
        token=Token("123", start={}), validator=my_field
    ) == 123

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=Token("hello", start={}), validator=my_field)
    assert exc_info.value.messages() == [
        Message(
            text="123 required for this number field.",
            code="required",
            index=[0],
            start_position={},
            end_position={},
        )
    ]

# Generated at 2022-06-14 14:53:57.465073
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class ExampleSchema(Schema):
        field1 = Field()
        field2 = Field(required=True)
    
    json_string = '''{
        "field1": "value1",
        "field3": "value3"
    }'''
    json_token = Token.from_json(json_string)
    with pytest.raises(ValidationError, match="The field \"field2\" is required."):
        validate_with_positions(token=json_token, validator=ExampleSchema)

# Generated at 2022-06-14 14:54:04.424050
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String
    from typesystem.tokenize.parser import parse_string

    token = parse_string("hello world")

    validator = String(min_length=15)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=validator)
    assert exc_info.value.messages() == [
        Message(
            text="Must be at least 15 characters in length.",
            code="min_length",
            start_position=token.start,
            end_position=token.end,
        )
    ]

# Generated at 2022-06-14 14:54:11.801812
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    schema = Schema(fields={"name": String(required=True)})
    token = Token(
        value={"name": "John"},
        start={"line_index": 0, "char_index": 0},
        end={"line_index": 0, "char_index": 10},
    )
    result = validate_with_positions(token=token, validator=schema)
    assert result == {"name": "John"}



# Generated at 2022-06-14 14:54:19.371014
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.fields import String

    class File(Schema):
        filename = String(max_length=10)

    token = tokenize({"filename": "something-long.txt"})
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=File())

    assert exc.value.messages() == [
        Message(
            index=("filename",),
            code="max_length",
            text="Ensure this value has at most 10 characters (it has 16).",
            start_position=Position(line_no=1, char_index=13),
            end_position=Position(line_no=1, char_index=29),
        )
    ]



# Generated at 2022-06-14 14:54:20.267722
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:54:31.256848
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class User(Schema):
        name = Field(type="string")
        age = Field(type="int32")

    json_data = '{"name": "Foo", "age": "abc"}'
    token = Token.parse(json_data)
    assert validate_with_positions(token=token, validator=User) == {"name": "Foo", "age": "abc"}

    try:
        validate_with_positions(token=token, validator=User)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        assert messages[0].code == "type_error.int32"
        assert messages[0].text == "Value does not match int32 type."
        assert messages[0].start_position.char_index == 18
        assert messages

# Generated at 2022-06-14 14:54:41.151331
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.base import parse
    from typesystem.tokenize.utils import tokenize_string

    class Person(Schema):
        age = Field(type="integer")

    person = Person()
    try:
        person.validate({"age": 1})
    except ValidationError as error:
        assert "invalid value" in error.messages()[0].text

    # Test for nested structure
    class Point(Schema):
        x = Field(type="integer")
        y = Field(type="integer")

    class Line(Schema):
        start = Field(type=Point)
        end = Field(type=Point)

    line = Line()

# Generated at 2022-06-14 14:54:48.399933
# Unit test for function validate_with_positions
def test_validate_with_positions():
    try:
        validate_with_positions(
            token=Token.from_dict({"foo": {"bar": "baz"}}),
            validator=Schema({"foo": {"bar": v.String()}}),
        )
    except ValidationError as error:
        assert error.messages()[0].start_position.line_number == 1
        assert error.messages()[0].start_position.column_number == 8

# Generated at 2022-06-14 14:54:57.526412
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import tokenize

    schema = Schema(fields={"a": Field(required=True)})
    tokenize(schema, {"a": 3})
    tokenize(schema, {"a": None})
    tokenize(schema, {})

    # assert validate_with_positions(
    #     token={'a': 3}, validator=schema
    # ).get('a') == 3
    #
    # assert validate_with_positions(
    #     token={'a': None}, validator=schema
    # ).get('a') is None
    #
    # assert validate_with_positions(
    #     token={}, validator=schema
    # ).get('a') is None
    #
    # try:
    #     validate_with_positions

# Generated at 2022-06-14 14:55:12.074166
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from .lexer import lex

    from .schemas import Root

    try:
        json_data = '{"age": "bla"}'
        tokens = lex(json_data)
        token = tokens[0]
        validate_with_positions(token=token, validator=Root())
    except ValidationError as err:
        print(*err.messages(), sep="\n")


__all__ = ["validate_with_positions"]