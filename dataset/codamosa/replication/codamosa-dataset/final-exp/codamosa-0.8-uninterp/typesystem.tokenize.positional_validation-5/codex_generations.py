

# Generated at 2022-06-14 14:45:20.898480
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    
    class User(Schema):
        username = Field(str)
        
    def run(*, text, validator):
        token = Token.parse(text)
        try:
            validate_with_positions(token=token, validator=validator)
        except ValidationError as error:
            return [
                dict(
                    message.to_dict(),
                    start_line=message.start_position.line,
                    start_column=message.start_position.char_index,
                    end_line=message.end_position.line,
                    end_column=message.end_position.char_index,
                )
                for message in error.messages()
            ]
        return None
        

# Generated at 2022-06-14 14:45:30.036247
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Integer
    from typesystem.tokenize.tokens import ObjectToken, StringToken

    token = ObjectToken(
        {
            "name": StringToken("Fred"),
            "age": StringToken("twenty five"),
            "hobbies": ObjectToken({"sport": StringToken("cricket")}),
        }
    )

    schema = Schema({"name": String, "age": Integer})

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)

    messages = exc_info.value.messages()

    assert len(messages) == 1

    message = messages[0]
    assert message.text == "Must be a valid integer."
    assert message.start_position.line_number == 2

# Generated at 2022-06-14 14:45:38.529529
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    schema = String(required=True, min_length=2)

    token = Token(
        {
            "user_id": "b03d313b-18da-49a5-8d0b-9e9d7ebaa0a5",
            "full_name": "Jane Doe",
        }
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=token, validator=schema
        )  # type: ignore
    assert len(exc_info.value.messages) == 2
    assert exc_info.value.messages[0].text == "The field 'full_name' is required."
    assert exc_info.value.messages[0].start_position.char_index == 17

# Generated at 2022-06-14 14:45:50.442027
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class SimpleSchema(Schema):
        foo = Field(required=True)

    token = Token("foo", "bar")
    assert validate_with_positions(token=token, validator=SimpleSchema) == {
        "foo": "bar"
    }

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Field(required=True))

    assert exc_info.value.messages() == [
        Message(
            text="The field <root> is required.",
            code="required",
            index=(),
            start_position=token.start,
            end_position=token.end,
        )
    ]

    class NestedSchema(Schema):
        schema = SimpleSchema(required=True)

    nested_token

# Generated at 2022-06-14 14:45:58.313263
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class MyField(Field):
        def validate(self, value):
            return {"foo": value}

    class MySchema(Schema):
        foo = MyField()

    assert validate_with_positions(
        token=Token("my-field", {"foo": "baz"}, position=Position(1, 2)),
        validator=MyField(),
    ) == {"foo": "baz"}

    token = Token(
        "my-field",
        {"bar": "baz"},
        position=Position(1, 2),
    )

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=MyField())


# Generated at 2022-06-14 14:46:08.528981
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parse import parse_string
    from typesystem.tokenize.string import String
    from typesystem.txtypes import String as StringType

    token = parse_string("""
        {
            "a": "foo",
            "b": "bar",
            "c": "qux"
        }
    """)
    assert validate_with_positions(token=token, validator=StringType(required=True)) == "foo"

    try:
        validate_with_positions(token=token, validator=StringType(required=False))
    except ValidationError as error:
        message = error.messages[0]
        assert message.start_position == StringPosition(line=2, column=15, char_index=19)

# Generated at 2022-06-14 14:46:19.187859
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer

    field = String(name="foo")
    token = Token(value="foo", start=[1, 1], end=[1, 4])
    assert validate_with_positions(token=token, validator=field) == "foo"

    token = Token(value=None, start=[1, 1], end=[1, 4])
    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field 'foo' is required.",
                code="required",
                index=("foo",),
                start_position=[1, 1],
                end_position=[1, 4],
            )
        ]

    validator = {"foo": Integer(minimum=0)}


# Generated at 2022-06-14 14:46:28.335912
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from pydantic import ValidationError
    from pydantic.fields import FieldInfo
    from pydantic.schema import ModelMetadata
    from typesystem import fields
    from typesystem.tokenize import Token

    metadata = ModelMetadata(
        name="Root",
        title="Root",
        fields=[FieldInfo("name", fields.StringField(min_length=1), "")],
    )
    token = Token("""{"name": ""}""", metadata=metadata)

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=metadata)

# Generated at 2022-06-14 14:46:39.680966
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import docdecs

    @docdecs.positional_arg
    def make_field(
        name: str,
        field_class: typing.Type[Field],
        value: typing.Any,
        token: Token,
    ) -> Field:
        return field_class(name=name, default=value)

    @docdecs.positional_arg
    def make_schema(
        token: Token, name: str, fields: typing.List[Field]
    ) -> typing.Type[Schema]:
        return type(name, (Schema,), {"fields": {"data": fields}})

    # Test field
    str_field = make_field(
        "str_field", Field, value="a string", token=Token(position=0, value="a string")
    )
    int_field = make_field

# Generated at 2022-06-14 14:46:51.621872
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.positions import Position, Range
    import json

    class TestSchema(Schema):
        bar = Field(type="string")
        foo = Field(type="test_schema")

    class TestField(Field):
        def __init__(self, *args, **kwargs):
            self.position = kwargs.pop("position", None)
            super().__init__(*args, **kwargs)

        def validate(self, value, *, context=None):
            if self.position and value == "error":
                tokens = {"foo": {"bar": "error"}, "test_field": 1}
                token = Token(tokens, self.position)
                raise ValidationError(token, "test")

# Generated at 2022-06-14 14:47:01.574854
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexer import lex
    from typesystem.tokenize.parser import parse

    schema = Schema({"id": Field(required=True), "name": Field(required=True)})
    tokens = lex(b'{"id": "123", "name": "Hans"}', source="<byte string>")
    top_level_token = parse(tokens)
    validate_with_positions(token=top_level_token, validator=schema)



# Generated at 2022-06-14 14:47:12.030113
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import types

    # this is used in the tests below:
    class TestSchema(Schema):
        i = types.Integer()
        s = types.String()

    def test_validates_without_error():
        token = Token(
            {
                "i": 2,
                "s": "hello"
            },
            start="(1, 1)",
            end="(1, 21)",
        )
        validate_with_positions(token=token, validator=TestSchema)

    def test_validates_and_raises_error():
        token = Token(
            {
                "i": "oops",
                "s": "hello"
            },
            start="(1, 1)",
            end="(1, 21)",
        )

# Generated at 2022-06-14 14:47:18.276417
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokenize, tokenize_with_position

    class TestSchema(Schema):
        field = Field(required=True)

    schema = TestSchema()
    result = validate_with_positions(
        token=tokenize_with_position(tokenize("{}")), validator=schema
    )
    assert result == {"field": None}

# Generated at 2022-06-14 14:47:25.978685
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.tokenize import tokens
    from tests.types import Person

    token = tokens.load()
    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        message = error.messages[0]
        assert message.code == "required"
        assert message.index == ("data", "user", "email")
        assert message.start_position.line == 3
        assert message.start_position.char_index == 7
    else:
        assert False, "should have raised an exception"

# Generated at 2022-06-14 14:47:36.434393
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import unittest.mock as mock
    
    _validator = mock.Mock()
    _validator.validate.side_effect = ValidationError(
        [Message(index=[], text="This is an error message.", code="invalid",)]
    )
    _token = mock.Mock()
    _token.start = mock.Mock()
    _token.start.char_index = 0
    _token.end = mock.Mock()
    _token.end.char_index = 4
    _token.lookup.return_value = _token
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=_token, validator=_validator)


# Generated at 2022-06-14 14:47:45.925999
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import toml
    from typesystem import fields

    tokens = toml.loads("""
        [user.name]
        first = "Frank"

        [[user.address]]
        location = "home"
        [user.address.details]
        address = ""
    """)
    address_schema = fields.Schema(
        fields={
            "location": fields.String(),
            "address": fields.String(required=True),
        }
    )
    user_schema = fields.Schema(
        fields={
            "name": {"first": fields.String()},
            "address": fields.Array(of=address_schema),
        }
    )

    # Top level object
    token = tokens
    assert token.value == tokens
    assert token.path == []

# Generated at 2022-06-14 14:47:56.164043
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import Tokenizer
    from typesystem.tokenize.base import BaseTokenizer
    from typesystem.tokenize.config import TokenizeConfig
    from typesystem.tokenize.fields import TokenizeField
    from typesystem.tokenize.schema import TokenizeSchema

    class SimpleSchema(TokenizeSchema):
        a = TokenizeField(str)

    def test_schema(schema: TokenizeSchema, data: bytes):
        tokenizer = Tokenizer(schema=schema, config=TokenizeConfig(endian=b">"))
        tokens = tokenizer.tokenize(data)
        return tokens.lookup([0])

    token = test_schema(SimpleSchema, b"a")

# Generated at 2022-06-14 14:48:05.885283
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(type="string")
    try:
        validate_with_positions(token=Token("my-token", value="123"), validator=field)
    except ValidationError as e:
        assert e.messages()[0].start_position.line_index == 1  # type: ignore
        assert e.messages()[0].start_position.column_index == 0  # type: ignore
        assert e.messages()[0].end_position.line_index == 1  # type: ignore
        assert e.messages()[0].end_position.column_index == 7  # type: ignore

# Generated at 2022-06-14 14:48:18.210084
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import ArrayToken, FieldToken
    from typesystem.tokenize.tokens import ObjectToken, StringToken
    from typesystem.tokenize.tokens import WhitespaceToken
    from typesystem.tokenize import Location

    class Person(Schema):
        name = "string"

    class People(Schema):
        people = "array:Person"
        count = "integer"

    class Phonebook(Schema):
        entries = "object:People"
        name = "string"
        count = "integer"

    # Phonebook

# Generated at 2022-06-14 14:48:28.721467
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.exceptions import TokenizeError
    from typesystem.tokenize.tokens import Array
    from typesystem.tokenize.tokens import Field as _Field
    from typesystem.tokenize.tokens import Object
    from typesystem.tokenize.tokens import Value

    from .schema import IntSchema

    schema = IntSchema()
    schema.validate("15")

    with pytest.raises(ValidationError):
        validate_with_positions(
            token=Array(value=[Value("foo"), Value("bar")]),
            validator=schema,
        )


# Generated at 2022-06-14 14:48:43.215450
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.tokenize.tokens import Token
    from typesystem.schemas import Schema
    from typesystem.fields import Field

    class TestSchema(Schema):
        required = Field(str)

    token = Token(
        start={"line_index": 0, "char_index": 0},
        end={"line_index": 2, "char_index": 5},
        value={"required": None},
    )

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=TestSchema)

    message = exc.value.messages()[0]
    assert message.start_position == {"line_index": 0, "char_index": 0}

# Generated at 2022-06-14 14:48:52.110634
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize.json import JsonTokenizer
    from typesystem.tokenize.exceptions import TokenizeError

    tokenizer = JsonTokenizer(
        String(min_length=1, max_length=1), structure="object"
    )

    with pytest.raises(ValidationError):
        validate_with_positions(token=tokenizer.parse('{"a": ""}'), validator=tokenizer)

    assert (
        str(tokenizer.parse('{"a": ""}').validate())
        == "1 error\nThe field 'a' is required."
    )

    with pytest.raises(ValidationError):
        validate_with_positions(token=tokenizer.parse('{"a": ""}'), validator=String)


# Generated at 2022-06-14 14:48:55.549775
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import lex  # type: ignore

    token = lex(code="", language="python")[0]
    assert validate_with_positions(token=token, validator=str) == ""

# Generated at 2022-06-14 14:49:02.872610
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize, TokenType

    token = tokenize("foo", "foo")[0]
    token.add_child(
        Token(type=TokenType.SECTION_START, value="[", start={"char_index": 0})
    )
    token.add_child(
        Token(type=TokenType.Section, value="foo", start={"char_index": 0})
    )
    token.add_child(
        Token(type=TokenType.SECTION_END, value="]", start={"char_index": 4})
    )

    validate_with_positions(token=token, validator=Field(pattern=r"[0-9]+"))

# Generated at 2022-06-14 14:49:10.180079
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class ExampleSchema(Schema):
        field = Field(str, required=True)

    # A sucessful validation
    token = Token(
        {
            "field": "hello",
        },
        start=TokenPosition(line=1, column=1, char_index=0),
        end=TokenPosition(line=1, column=15, char_index=14),
    )
    validate_with_positions(token=token, validator=ExampleSchema)

    # An unsuccessful validation
    token = Token(
        {},
        start=TokenPosition(line=1, column=1, char_index=0),
        end=TokenPosition(line=1, column=15, char_index=14),
    )
    with pytest.raises(ValidationError) as excinfo:
        validate_with_pos

# Generated at 2022-06-14 14:49:20.301974
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer
    from typesystem.tokenize.tokens import IntegerToken

    integer = Integer()

    value = validate_with_positions(
        token=IntegerToken(
            value=None,
            start={
                "line": 0,
                "char_index": 0,
                "column": 0,
                "character": "",
                "path": "",
            },
            end={
                "line": 0,
                "char_index": 0,
                "column": 0,
                "character": "",
                "path": "",
            },
        ),
        validator=integer,
    )

    assert value == 0


# Generated at 2022-06-14 14:49:30.188380
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(type="string")

    from typesystem.tokenize.tokens import JsonToken
    token = JsonToken.parse({"name": None}, start=1, end=2)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Person)

    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.start_position.char_index == 7
    assert message.end_position.char_index == 8
    assert message.code == "required"

# Generated at 2022-06-14 14:49:35.135892
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json

    from typesystem.schemas import Object, String
    from typesystem.tokenize.tokens import Token

    json_str = """{
        "name": "John"
    }"""

    schema = Object({"name": String()})
    token = Token.from_json(json.loads(json_str))

    validate_with_positions(token=token, validator=schema)

# Generated at 2022-06-14 14:49:45.197648
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.string import String

    String().validate('foo')
    String().validate('foo', validate=True)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=Token(Token.ROOT, 'foo', 1, 3),
            validator=String(required=False),
        )
    message = exc_info.value.messages[0]
    assert message.code == "invalid"
    assert message.text == "Value must be a string."
    assert message.start_position.line == 1
    assert message.start_position.char_index == 0
    assert message.end_position.line == 1
    assert message.end_position.char_index == 3


# Generated at 2022-06-14 14:49:57.484449
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.position import LinePosition
    from typesystem.tokenize.tokens import ObjectToken, PrimitiveToken
    from typesystem.fields import String
    from typesystem.schemas import Object

    def a():  # pragma: no cover
        assert False

    class MySchema(Schema):
        a = String()

    token = ObjectToken(
        [PrimitiveToken(value="b", start=LinePosition(line=1, column=1))],
        start=LinePosition(line=1, column=1),
        end=LinePosition(line=1, column=1),
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=MySchema)


# Generated at 2022-06-14 14:50:14.719773
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Text, Integer, Object
    import json

    class User(Schema):
        name = Text(required=True)
        age = Integer(minimum=21, maximum=99)

    input_ = """
    {
        "name": "bob",
        "age": 12
    }
    """
    token = Token(value=json.loads(input_), start=Position(line=1, column=1))
    try:
        validate_with_positions(token=token, validator=User)
    except ValidationError as error:
        assert len(error.messages()) == 2

        message = error.messages()[0]

        assert message.text == "The field age is too low."
        assert message.start_position.line == 4
        assert message.start_position.column == 18
       

# Generated at 2022-06-14 14:50:25.630802
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize, Token

    # If we don't provide any positional information then we can't determine
    # the position of a message.
    input = "a=1\nb=2\nc=3"
    token = tokenize(input)
    with pytest.raises(ValidationError):
        validate_with_positions(
            token=token, validator={"a": int, "b": int, "c": "z",}  # type: ignore
        )

    # Now if we do provide the positional information we can...
    token = tokenize(input)
    token = Token(token, start=0, end=len(input))

# Generated at 2022-06-14 14:50:32.982750
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizer import Tokenizer
    from typesystem.fields import Integer, String

    field = Integer(maximum=2)
    tokenizer = Tokenizer(field)
    token = tokenizer.tokenize('{"value": 3}')

    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as error:
        assert len(error.messages()) == 1
        message = error.messages()[0]
        assert message.index == []
        assert (
            message.start_position.char_index
            == token.lookup(message.index).start.char_index
        )
        assert (
            message.end_position.char_index
            == token.lookup(message.index).end.char_index
        )

    schema = Schema

# Generated at 2022-06-14 14:50:42.724628
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.exceptions import TokenizeError

    schema = Integer(max_value=5)
    tokens = tokenize(schema, b"123456789")

    try:
        validate_with_positions(token=tokens[3], validator=schema)
    except TokenizeError as error:
        messages = error.messages()
        assert len(messages) == 1
        assert messages[0].text == "Ensure this value is less than or equal to 5."
        assert messages[0].start_position.line_number == 1
        assert messages[0].start_position.column_number == 2
        assert messages[0].end_position.line_number == 1

# Generated at 2022-06-14 14:50:47.163112
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema({"name": Field(required=True)})

    # Valid document
    document = {"name": "Joe"}
    token = from_python(document)
    assert validate_with_positions(token=token, validator=schema) == document

    # Invalid document
    document = {}
    token = from_python(document)
    with raises(ValidationError, match="The field 'name' is required."):
        validate_with_positions(token=token, validator=schema)

# Generated at 2022-06-14 14:50:57.361379
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Test some validation errors
    from typesystem.errors import ValidationError

    try:
        from typesystem.schemas import Schema
    except ImportError:
        from typesystem.schemas.base import Schema

    # Test a basic schema
    class TestSchema(Schema):
        a = Field(required=True)

    token = Token(value={"a": "b"})
    validate_with_positions(token=token, validator=TestSchema)
    # Test a bad schema
    token = Token(value={"b": "b"})
    try:
        validate_with_positions(token=token, validator=TestSchema)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "The field 'a' is required."


# Generated at 2022-06-14 14:51:06.501706
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import tokenize
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import String

    token = tokenize(
        """
        foo:
            bar: "baz"
    """
    )
    token = token.lookup(["foo", "bar"])
    assert isinstance(token, Token)
    assert token.value == "baz"
    assert str(validate_with_positions(token=token, validator=String())) == "baz"

    try:
        validate_with_positions(token=token, validator=String(required=True))
    except ValidationError as error:
        message = error.messages()[0]
    else:
        raise AssertionError("Expected ValidationError")


# Generated at 2022-06-14 14:51:17.255889
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.simple import tokenize

    value = {"foo": "bar"}

    class DocumentSchema(Schema):
        foo = Field()

    class HeaderSchema(Schema):
        document = DocumentSchema()

    class RootSchema(Schema):
        header = HeaderSchema()

    assert validate_with_positions(
        token=tokenize(value, schema=RootSchema()), validator=DocumentSchema()
    ) == {"foo": "bar"}

    value = {}

    with pytest.raises(ValidationError):
        validate_with_positions(
            token=tokenize(value, schema=RootSchema()), validator=HeaderSchema()
        )


# Generated at 2022-06-14 14:51:28.818806
# Unit test for function validate_with_positions
def test_validate_with_positions():
    Token = typing.TypeVar("Token")
    import json
    import pytest
    from typesystem.tokenize import tokenize


# Generated at 2022-06-14 14:51:38.903475
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Test with nested field
    data = {"y": [{"x": "foo"}]}
    token = tokenize_data(data)
    class Test(Schema):
        x = String()

    class Test2(Schema):
        y = List(schema=Test())

    try:
        validate_with_positions(token=token, validator=Test2())
    except ValidationError as error:
        assert len(error.messages()) == 1

        message = error.messages()[0]
        assert message.index == ["y", 0, "x"]
        assert (
            message.start_position.char_index == 12
        )  # start position of "foo"

    # Test with root field
    class Test3(Schema):
        x = String(required=True)

    data = {}
    token

# Generated at 2022-06-14 14:52:00.791340
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, Schema, String

    class UserSchema(Schema):
        name = String(max_length=100)
        age = Integer(min_value=1, max_value=100)

    errors = UserSchema.validate_and_return_errors(
        name="John Doe", age=101,
    )
    assert len(errors) == 1
    error = errors[0]
    assert error.token.end.line_number == 3
    assert error.start_position.line_number == 3
    assert error.end_position.line_number == 3

    errors = UserSchema.validate_and_return_errors(
        name="John Doe",
    )
    assert len(errors) == 1
    error = errors[0]
    assert error.token.end.line_number == 4

# Generated at 2022-06-14 14:52:13.298482
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Document, Field, Value

    class DataSchema(Schema):
        name = Field(type="string")
        age = Field(type="integer")

    document = Document(
        fields=[
            Field(key=Value(start=(0, 0), end=(0, 9)), value=Value(start=(0, 0), end=(0, 9))),
            Field(key=Value(start=(1, 0), end=(1, 2)), value=Value(start=(1, 0), end=(1, 2))),
        ]
    )

    try:
        validate_with_positions(token=document, validator=DataSchema)
    except ValidationError as e:
        message = e.messages()[0]

# Generated at 2022-06-14 14:52:22.169885
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.schemas import Schema
    from typesystem.validators import one_of
    from typesystem.tokenize import parse

    schema = Schema(
        {
            "name": String(max_length=20),
            "age": Integer(),
            "gender": String(validators=[one_of(choices=["male", "female"])]),
        }
    )

    token = parse(
        datetime.now(),
        {"name": "david", "age": "10", "gender": "unknown"},
        parent=None,
    )


# Generated at 2022-06-14 14:52:30.052416
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json

    class Article(Schema):
        title = Field(str)
        author = Field(str)

    schema = Article()

    def run_test(*, input: str, expected: typing.List[Message]):
        tokens = json.loads(input)
        try:
            schema.validate(tokens)
        except ValidationError as error:
            assert error.messages() == expected


# Generated at 2022-06-14 14:52:41.438614
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse_token

    token = parse_token(b'{"i": 1}')  # type: ignore

# Generated at 2022-06-14 14:52:49.451414
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem

    class Person(typesystem.Schema):
        name = typesystem.String(max_length=5)

    class Job(typesystem.Schema):
        title = typesystem.String()

        class Meta:
            title = "job"

    class PersonWithJob(typesystem.Schema):
        person = Person()
        job = Job()


# Generated at 2022-06-14 14:53:00.027892
# Unit test for function validate_with_positions
def test_validate_with_positions():
    def assert_positions(token: Token, code: str):
        with pytest.raises(ValidationError) as excinfo:
            validate_with_positions(token=token, validator=Field(required=True))
            assert excinfo.match(code)
            for message in excinfo.messages:
                assert message.start_position.line == 2
                assert message.start_position.char_index == 10
                assert message.end_position.line == 2
                assert message.end_position.char_index == 11

    # File format:
    #  line 1 <---- start_position
    #  line 2 <---- end_position
    #  line 3
    file = textwrap.dedent(
        """
        {
          "foo":
        }
        """
    )
    # Type: string (or

# Generated at 2022-06-14 14:53:10.847316
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    from typesystem.tokenize.schema import get_tokens
    from typesystem.tokenize.tokens import Token
    from typesystem.schema import Schema

    class BookSchema(Schema):
        title = typesystem.String(required=True)

        class Meta:
            title = "Book"

    class UserSchema(Schema):
        name = typesystem.String(required=True)
        book = BookSchema(required=True)

        class Meta:
            title = "User"

    tokens = get_tokens({"name": "miles", "book": {}})
    assert len(tokens) == 1
    assert isinstance(tokens[0], Token)
    assert tokens[0].lookup_path == [0]
    validate_with_positions

# Generated at 2022-06-14 14:53:11.524239
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:53:22.997652
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer

    token = Token(
        key="root",
        value={
            "foo": {},
            "bar": {"baz": []},
            "qux": [{"quux": "abc"}],
            "corge": "abc",
        },
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=token, validator=Integer(name="corge", required=True)
        )

    exc = exc_info.value

    assert len(exc.messages()) == 1
    message = exc.messages()[0]
    assert message.text == "The field 'corge' is required."
    assert message.start_position.line_index == 0  # type: ignore
    assert message.start_position

# Generated at 2022-06-14 14:53:43.130816
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import Parser
    from typesystem.schemas import Schema

    class User(Schema):
        username = Field(format="alphanumeric", max_length=20)
        email = Field(format="email")

    parser = Parser(template="{{ username }} - {{ email }}")
    tokens = parser.parse("Ruben - j@m.com")
    assert validate_with_positions(validator=User, token=tokens[0]) == {
        "username": "Ruben",
        "email": "j@m.com",
    }

# Generated at 2022-06-14 14:53:53.615218
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class Person(Schema):
        name = Field(type="string", required=True)
        age = Field(type="integer", required=True)

    text = """
    {
        "name": "Petra",
        "age": "24"
    }
    """
    tokens = tokenize(text)
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(
            token=tokens[0], validator=Person
        )
    message = exc.value.messages[0]
    assert message.text == "Expected a valid integer"
    assert message.start_position.line == 5
    assert message.start_position.char_index == 11
    assert message.end_position.line == 5
    assert message.end

# Generated at 2022-06-14 14:54:04.018575
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.objects import Object
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer
    from typesystem.tokenize import tokenize

    class Person(Object):
        name = String()
        age = Integer(name="years")

    token = tokenize('{"name": "Django", "age": 10}')
    assert isinstance(token, Token)
    assert len(token) == 2

    assert validate_with_positions(
        token=token, validator=Person
    ) == {"name": "Django", "age": 10}

    token = tokenize('{"name": "Django", "age": "10"}')
    assert isinstance(token, Token)
    assert len(token) == 2


# Generated at 2022-06-14 14:54:14.986222
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = String(min_length=2)

    token = Token(
        name="person",
        value={"name": ""},
        start=Position(line_number=4, char_index=5),
        end=Position(line_number=5, char_index=5),
    )

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=Person)

    errors = excinfo.value.messages()

# Generated at 2022-06-14 14:54:25.654899
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String

    token = Token(
        "foo",
        {
            "key": Token("string", "foo", source_text="string", start=(1, 0), end=(1, 4))
        },
        start=(1, 0),
        end=(2, 5),
    )
    validate_with_positions(token=token, validator=String())

    try:
        validate_with_positions(token=token, validator=String(required=True))
    except ValidationError as error:
        first_message, *rest = error.messages()
        assert first_message.text == "The field key is required."
        assert first_message.start_position == (1, 0)
        assert first_message.end_position == (1, 4)
        assert first_message.code == "required"

# Generated at 2022-06-14 14:54:35.257413
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class UserSchema(Schema):
        name = Field(str)
        age = Field(int)

    json = """{
  "name": "Fred",
  "age": "bad",
}"""
    try:
        user_info = validate_with_positions(
            token=tokenize(json), validator=UserSchema
        )
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "The value 'bad' is not of type 'integer'."
        assert message.start_position.line_index == 2
        assert message.start_position.char_index == 8
        return

    raise AssertionError("No validation error was raised.")

# Generated at 2022-06-14 14:54:42.538969
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, Object
    from typesystem.tokenize.example_tokens import example_tokens

    class MySchema(Object):
        foo = Integer(required=True)

    token = example_tokens.get("my_schema")
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(validator=MySchema(), token=token)

    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.text == 'The field "foo" is required.'
    assert message.index == ["foo"]
    assert message.start_position.char_index == 6
    assert message.end_position.char_index == 6




# Generated at 2022-06-14 14:54:47.607154
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.unset import Unset

    from typesystem import fields

    from .conftest import assert_validation_error

    assert_validation_error(
        validate_with_positions,
        """\
{
    "foo": "bar"
}""",
        fields.Array(fields.String)
    )


# Generated at 2022-06-14 14:54:56.754640
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import unittest
    import typesystem
    import typesystem.error

    class PositionTest(unittest.TestCase):
        def assertPositionalError(
            self, path, text, code, line, column, position_type, *, value
        ):
            with self.assertRaises(typesystem.error.ValidationError) as exc:
                validate_with_positions(
                    token=value,
                    validator=typesystem.Object(properties={"id": typesystem.Integer()}),
                )
            message = exc.exception.messages[0]
            self.assertEqual(message.index, path)
            self.assertEqual(message.text, text)
            self.assertEqual(message.code, code)
            self.assertEqual(message.start_position.line, line)
           

# Generated at 2022-06-14 14:55:05.492719
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    import typesystem.tokenize

    schema_validator = typesystem.Schema(
        {"id": typesystem.Integer(), "name": typesystem.String()}
    )

    text = '{"id": 123, "name": "joe"}'
    token = typesystem.tokenize.tokenize(text)

    try:
        validate_with_positions(token=token, validator=schema_validator)
    except typesystem.ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        assert messages[0].text == 'The field "age" is required.'
        assert messages[0].code == "required"
        assert messages[0].index == ("age",)