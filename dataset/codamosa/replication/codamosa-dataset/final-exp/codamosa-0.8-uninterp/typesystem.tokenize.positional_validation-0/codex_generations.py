

# Generated at 2022-06-14 14:45:22.891203
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Validator is a Field
    schema = {"title": {"type": "string", "required": True}}
    element_token = Token(["title"], "foo", {"line": 1, "column": 2}, {"line": 1, "column": 5})
    token = Token(
        "title",
        element_token,
        {"line": 1, "column": 1},
        {"line": 1, "column": 6},
        ["title"],
        {"title": Field(**schema["title"])},
    )
    assert validate_with_positions(token=token, validator=token.fields[0]) == "foo"

    # Validator is a Schema

# Generated at 2022-06-14 14:45:29.142863
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import FieldToken, ObjectToken

    token = ObjectToken(value={"name": "Foo"}, start=1, end=4)
    validator = Field(name="name", type_=str)

    with raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=validator)

    message = exc_info.value.messages[0]
    assert message.text == "Field name is required."
    assert message.start_position.char_index == 3



# Generated at 2022-06-14 14:45:37.119743
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    from typesystem_json_schema import JSONSchema

    from .validators import validators

    validator = JSONSchema({"type": "array", "items": {"type": "string"}})
    text = "['Hello','World','!']"
    tokens = tuple(tokenize(text))
    assert len(tokens) == 7
    assert [t.value for t in tokens] == [
        "[",
        "'Hello'",
        ",",
        "'World'",
        ",",
        "'!'",
        "]",
    ]


# Generated at 2022-06-14 14:45:49.192586
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenizer
    from typesystem.fields import String
    from typesystem.errors import Error
    from typesystem.tokenize import Position

    schema = {
        "name": String(max_length=5),
        "address": {"postcode": String(length=5)},
    }
    t = tokenizer(schema, '{"name": "Foo Bar", "address": {"postcode": "1234"}}')
    result = validate_with_positions(token=t, validator=schema)
    assert result == {
        "name": "Foo Bar",
        "address": {"postcode": "1234"},
    }


# Generated at 2022-06-14 14:45:56.872504
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import JSONSchema

    class SomeSchema(JSONSchema):
        type = "object"
        properties = {"foo": {"type": "string"}}
        required = ["foo"]

    from typesystem.tokenize.tokens import ObjectToken

    token = ObjectToken(start={"line": 1, "char": 0}, value={}, schema=SomeSchema)

# Generated at 2022-06-14 14:46:08.357735
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Boolean, Integer

    from .utils import tokenize, token_to_dict

    schema = String(name="name") | Boolean(name="bool") | Integer(name="num")

    try:
        validate_with_positions(token=tokenize("{}"), validator=schema)
    except ValidationError as error:
        tokens = [
            token_to_dict(m.start_position, m.end_position, m.code)  # type: ignore
            for m in error.messages()
        ]

# Generated at 2022-06-14 14:46:18.949845
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Field validation
    class MyField(Field):
        def check_length(self, value):
            if len(value) < 3:
                raise self.fail("too_short")

    field = MyField(name="foo")

    token = Token(
        name="string",
        value="ab",
        start=Position(line=1, character=1),
        end=Position(line=1, character=3),
    )

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=field)

    message = excinfo.value.messages[0]
    assert message.text == "too_short"
    assert message.start_position == Position(line=1, character=1)

# Generated at 2022-06-14 14:46:28.089199
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from typesystem.tokenize.lexer import lex
    from typesystem.tokenize.parsing import parse

    from .fields import String
    from .schemas import Object, Array

    data = '{"foo": 123, "bar": [{"baz": "hi"}], "qux": "hi"}'
    tokens, _ = lex(data)
    tree = parse(tokens)
    schema = Object({"foo": String, "bar": Array(Object({"baz": String}))})

    # Within field.
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=tree.lookup("foo"), validator=String)

    message = exc_info.value.messages[0]
    assert message.code == "invalid_type"
    assert message

# Generated at 2022-06-14 14:46:39.460373
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = {"name": "test_schema", "fields": {"x": {"type": "number"}}}
    schema = Schema(schema)
    validator = schema.fields["x"]
    token = Token(
        "start", "end", {"x": Token(start=1, end=2, value="foo", children={})}, {}
    )
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=validator)
    exc_message = exc.value.messages
    assert len(exc_message) == 1
    assert exc_message[0].text == "Must be of type number."
    assert exc_message[0].code == "type_error"
    assert exc_message[0].index == ("x",)

# Generated at 2022-06-14 14:46:46.862246
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import TokenString

    from tests.utils import validate_with_positions as outer_validate_with_positions

    assert outer_validate_with_positions(
        token=TokenString('{"foo": 42}'),
        validator={"foo": int},
    ) == {"foo": 42}

    assert outer_validate_with_positions(
        token=TokenString('{"foo": "bar"}'),
        validator={"foo": int},
    ) == ValidationError

    class MySchema(Schema):
        foo = int

    assert outer_validate_with_positions(
        token=TokenString('{"foo": 42}'),
        validator=MySchema,
    ) == {"foo": 42}


# Generated at 2022-06-14 14:46:59.027593
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import lex

    class Number(Field):
        """A number."""

        def validate(self, v, path=None):
            try:
                return float(v)
            except ValueError:
                raise ValidationError(index=path, text="Not a number.")

    a = Number(name="a")
    b = Number(name="b")
    c = Number(name="c")
    d = Number(name="d")
    schema = Schema(
        properties={
            "a": a,
            "b": b,
            "c": c,
            "d": d,
        },
        required=["a", "d"],
    )


# Generated at 2022-06-14 14:47:09.963872
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import tokenize

    token = tokenize('{"field": [1, 2, 3]}')
    schema = Schema({"field": [int]})
    assert validate_with_positions(token=token, validator=schema) == {
        "field": [1, 2, 3]
    }

    # Required field missing
    token = tokenize('{}')
    schema = Schema({"field": [int]})
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=schema)
    assert exc.value.messages[0].token_start == 1
    assert exc.value.messages[0].token_end == 1

    # Nested required field missing

# Generated at 2022-06-14 14:47:16.965429
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class Book(Schema):
        name = Field(type="string", required=True)

    class Author(Schema):
        name = Field(type="string", required=True)
        books = Field(type="array", items=Book)

    author = Author()

    text = """
    {
        "name": "Leo Tolstoy",
        "books": [
            {
                "name": "War and Peace"
            },
            {
                "name": "Anna Karenina"
            }
        ]
    }
    """

# Generated at 2022-06-14 14:47:27.874745
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import dataclasses

    @dataclasses.Schema
    class Author:
        name: str

    @dataclasses.Schema
    class Page:
        title: str
        author: Author

    @dataclasses.Schema
    class Book:
        title: str
        pages: typing.List[Page]

    def validate(data, schema):
        from typesystem.tokenize import tokenize

        token = tokenize(data)
        return validate_with_positions(token=token, validator=schema)

    data = {}
    with pytest.raises(ValidationError) as error:
        validate(data, Book)

    fields = [m.index[-1] for m in error.value.messages if m.code == "required"]
    assert fields == ["title", "pages"]



# Generated at 2022-06-14 14:47:39.575455
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import fields
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokenizer import tokenize

    token = tokenize({"a": {"b": {"c": "foo"}}})
    field = fields.Dictionary(properties={"a": {"b": {"c": fields.String()}}})

    validate_with_positions(token=token, validator=field)

    errors = field.validate({"a": {"b": {"c": ""}}})
    assert list(errors) == [
        Message(
            start_position=Position(line=2, column=13),
            end_position=Position(line=2, column=13),
            index=["a", "b", "c"],
            code="string.empty",
            text="Field cannot be blank.",
        )
    ]

# Generated at 2022-06-14 14:47:47.504908
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import schema

    class UserSchema(schema.Schema):
        name = schema.String(max_length=100)
        age = schema.Integer()

    value = {
        "name": "John Smith",
        "age": "30",
    }
    text = json.dumps(value)
    token = Token.from_json(json.loads(text))


# Generated at 2022-06-14 14:47:55.317787
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import JSONParser  # type: ignore

    parser = JSONParser({"name": "foo"})
    token = parser.parse()

    class MySchema(Schema):
        name = Field(required=True)

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=MySchema)

    message = error.value.messages()[0]
    assert message.start_position.line_number == 0
    assert message.start_position.char_index == 7



# Generated at 2022-06-14 14:48:07.292038
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.typesystem_test.test_tokenize.test_tokens import (
        get_test_json_file,
    )

    from typesystem.tokenize.tokenize import tokenize

    from typesystem.schemas import Record
    from typesystem.fields import String

    file = get_test_json_file("test_tokenize_list.json").read_text()
    token = tokenize(file)
    schema = Record({
        "name": String(),
        "age": Int(),
        "sex": Choice(["male", "female"])
    })
    result = validate_with_positions(token=token, validator=schema)
    assert result == {
        "name": "John Doe",
        "age": 42,
        "sex": "male"
    }

# Generated at 2022-06-14 14:48:16.544331
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    data = [
        ({"name": "foobar"}, True),
        ({"name": None}, False),
        ({"name": ""}, False),
    ]
    schema = {"name": String}

    class MySchema(Schema):
        name: String

    for value, expected in data:
        succeeded = False
        try:
            validate_with_positions(validator=MySchema, token=Token(value=value))
            succeeded = True
        except ValidationError:
            pass

        assert succeeded == expected

# Generated at 2022-06-14 14:48:27.410944
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.base import Tokenizer
    from typesystem.tokenize.tokens import DictToken
    from typesystem.tokenize.tokens import ListToken
    from typesystem.tokenize.tokens import ScalarToken
    from typesystem.tokenize.tokens import Token

    class IntField(Field):
        def validate(self, value: typing.Any) -> typing.Any:
            return int(value)

    class DictSchema(Schema):
        a = IntField(required=True)
        b = IntField(required=True)

    class ListSchema(Schema):
        a = IntField(required=True)
        b = IntField(required=True)

    class RootSchema(Schema):
        a = IntField(required=True)

# Generated at 2022-06-14 14:48:43.085337
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from sys import stderr
    from json import loads
    from typesystem.tokenize.jsontokens import parse_json

    stderr.write(
        "tokenize.jsontokens.parse_json() - "
        "expecting error messages with LSP position information\n"
    )
    src = """{
        "type": "object",
        "properties": {
            "hello": {
                "type": "array",
                "minItems": 1
            },
            "world": {
                "type": "number"
            }
        }
    }"""
    tokens = parse_json(src)
    token = next(tokens)
    schema = Schema.from_token(token)

# Generated at 2022-06-14 14:48:51.060120
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from json import dumps
    from typesystem import Schema, String

    class MyField(Field):
        def is_valid_type(self, value):
            return value == "bob"

    class MySchema(Schema):
        name = String(required=True)
        age = MyField()

    def validate(value):
        return validate_with_positions(
            token=Token.from_json(value), validator=MySchema
        )
    validate(dumps({"name": "bob", "age": "bob"}))

    with pytest.raises(ValidationError):
        validate(dumps({"name": "bob", "age": "frank"}))

# Generated at 2022-06-14 14:48:58.069808
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class MySchema(Schema):
        my_field = String(required=True)

    schema = MySchema()

    token = Token(
        value={},
        start=Position(line_index=0, char_index=0),
        end=Position(line_index=0, char_index=0),
    )
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(
            token=token, validator=schema
        )
    assert len(exc.value.messages()) == 1
    assert exc.value.messages()[0].text == "The field 'my_field' is required."
    assert exc.value.messages()[0].start_position.line_index

# Generated at 2022-06-14 14:49:06.365670
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class Person(Schema):
        name = Field(type="string")

    class Document(Schema):
        person = Field(type="object", properties=Person())

    assert validate_with_positions(
        token=Token.parse({"person": {}}), validator=Document()
    ) == {"person": {"name": None}}

    assert validate_with_positions(token=Token.parse({}), validator=Document()) == {
        "person": None
    }

    assert validate_with_positions(
        token=Token.parse({}), validator=Field(type="string")
    ) is None

    assert validate_with_positions(token=Token.parse({}), validator=Field(type="object")) == {}  # noqa


# Generated at 2022-06-14 14:49:18.409642
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import ValidationError as ValidationErrorToken
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import String, Integer
    from typesystem.schemas import Schema

    class PersonSchema(Schema):
        name = String(required=True)
        age = Integer(minimum=18)

    input_data = {
        "name": "Tiago",
        "age": "invalid",
    }
    token = Token.from_data(input_data)
    try:
        validate_with_positions(token=token, validator=PersonSchema)
    except ValidationError as error:
        error_data = error.as_data()
        assert len(error_data["messages"]) == 2, error_data
        assert error_data

# Generated at 2022-06-14 14:49:29.233381
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class MyField(Field):
        def validate(self, value):
            raise ValidationError("This is a bad value", code="bad-value")

    token = Token(value=5, start=(1, 0), end=(1, 1))
    try:
        validate_with_positions(token=token, validator=MyField())
    except ValidationError as error:
        assert error.messages()[0].start_position.line_number == 1
        assert error.messages()[0].start_position.char_index == 0
        assert error.messages()[0].end_position.line_number == 1
        assert error.messages()[0].end_position.char_index == 1
        return

    assert False



# Generated at 2022-06-14 14:49:38.562584
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """Test that the position information is correctly added."""
    from typesystem.tokenize.tokens import (
        StartBracketToken,
        EndBracketToken,
        StartArrayToken,
        EndArrayToken,
        FieldToken,
        StringToken,
    )

    from .examples import DictionaryField, StringField

    field = StringField(required=True)
    dictionary_field = DictionaryField(
        fields={"name": StringField(required=True), "age": StringField()}, required=True
    )

    # Missing field, with positions

# Generated at 2022-06-14 14:49:46.063845
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class IntField(Field):
        def validate(self, value: int) -> int:
            if value % 2 != 0:
                raise ValidationError(
                    "Value must be even", index=["data"], code="wrong_value"
                )
            return value

    class DocumentSchema(Schema):
        data = IntField(required=True)

    token = Token.from_dict({"data": "skein"})
    token.start = token.start.move(char_index=-1)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=DocumentSchema)

    assert exc_info.value.messages()[0].start_position == token.start
    assert exc_info.value.messages()[0].end_position

# Generated at 2022-06-14 14:49:57.926611
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.objects import Object
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.positions import Position
    from typesystem.tokenize.tokens import StringToken, BraceToken

    class TokenField(Field):
        def validate_token(self, token):
            return validate_with_positions(token=token, validator=String(max_length=2))

    class TestSchema(Schema):
        field = TokenField()

    text = "testing"
    tokens = [StringToken(value="testing", start=Position(0), end=Position(7))]
    token = Token(None, tokens)
    TestSchema().validate(token)

    text = "testing"

# Generated at 2022-06-14 14:50:10.185725
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import (
        DictionaryToken,
        ListToken,
        RootToken,
        TextToken,
    )
    from typesystem.tokenize.parse import parse
    from typesystem.schemas import Schema
    from typesystem.fields import Integer, String

    class TestSchema(Schema):
        id = Integer(required=True)
        name = String(required=True)

    token = parse({"id": "foo", "name": "bar"})
    error = None
    try:
        validate_with_positions(token=token, validator=TestSchema)
    except ValidationError as error_:
        error = error_

    assert error is not None
    assert len(error.messages()) == 2

# Generated at 2022-06-14 14:50:27.447319
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import pytest

    from typesystem.json_schema import JSONSchema

    schema = JSONSchema({"properties": {"name": {"type": "string"}}})
    token = Token(json.loads('{"name": "Joe"}'))

    value = validate_with_positions(token=token, validator=schema)
    assert value == {"name": "Joe"}

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema.fields["name"])
    error = exc_info.value
    assert len(error.messages()) == 1
    message = error.messages()[0]
    assert message.text == 'The field "name" is required.'
    assert message.code == "required"
    assert message

# Generated at 2022-06-14 14:50:34.831561
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class Person(Schema):
        name = Field(str)
        address = Field(str)

    document = """
    name: "John Doe"
    address: "15 St. Mary Avenue"
    """

    token = tokenize(document)
    errors = validate_with_positions(
        token=token, validator=Person()
    ).messages()
    assert errors == []

# Generated at 2022-06-14 14:50:43.839492
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        first_name = Field(required=True)

    from typesystem.tokenize.parser import Tokenizer

    tokenizer = Tokenizer(doc={'first_name': None})
    token = tokenizer.parse()  # type: ignore
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=Person)
    messages = exc.value.messages()
    message = messages[0]
    assert message.text == "The field 'first_name' is required."
    assert message.start_position.line_number == 1
    assert message.start_position.char_index == 2
    assert message.end_position.line_number == 1
    assert message.end_position.char_index == 11

# Generated at 2022-06-14 14:50:54.009655
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.text_to_ast import text_to_ast

    error = None

    try:
        validate_with_positions(
            token=text_to_ast(
                r"""
{
    "name": "John Doe",
    "age": 42
}
  """
            ),
            validator=Schema.from_dict(
                fields={
                    "name": {
                        "type": "string"
                    },
                    "age": {
                        "type": "number",
                        "minimum": 18
                    }
                }
            ),
        )
    except ValidationError as e:
        error = e


# Generated at 2022-06-14 14:51:00.395670
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.primitives import String, Integer

    class Person(Schema):
        name = String(required=True)
        age = Integer()

    token = Token(type="object", value={"name": "John Doe", "age": 43})
    assert validate_with_positions(token=token, validator=Person) == {
        "name": "John Doe",
        "age": 43,
    }

    token = Token(type="object", value={"age": 43})
    with pytest.raises(ValidationError) as excinfo:
        assert validate_with_positions(token=token, validator=Person) == {
            "name": "John Doe",
            "age": 43,
        }
    messages = excinfo.value.messages()
    assert len(messages) == 1
    assert messages

# Generated at 2022-06-14 14:51:06.201889
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexer import Lexer
    from tests.tokenize import schema

    # Create a lexer for the test schema
    lexer = Lexer()
    lexer.schema = schema

    # Create a mock source
    source = "foo bar\nqux"

    # Tokenize the input using the lexer
    tokens = lexer.tokenize(source)

    # Validate the input using the lexer
    tokens.validate_schema(tokens.tokens, schema())

    assert tokens.errors == []

# Generated at 2022-06-14 14:51:15.124891
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    from typesystem.tokenize.tokens import Token

    query_string = "foo=bar"
    schema = typesystem.Schema({"foo": typesystem.Integer()})

    token = Token.from_string(query_string)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    position = exc_info.value.messages[0].start_position
    assert position.line == 1
    assert position.column == 4
    assert position.char_index == 4



# Generated at 2022-06-14 14:51:23.434638
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import StringToken, TokenList

    class MySchema(Schema):
        field1 = String()
        field2 = String()

    token = StringToken(
        "--field1=value1 --field2=value2", start={"char_index": 0}
    )
    value = validate_with_positions(
        token=token, validator=MySchema
    )  # type: ignore

# Generated at 2022-06-14 14:51:31.864657
# Unit test for function validate_with_positions
def test_validate_with_positions():  # pragma: no cover
    from typesystem.tokenize import tokenize_string

    class TestSchema(Schema):
        email = Field(type="string", required=True)

    schema = TestSchema()

    json = {
        "email": "hi@example.com",
    }

    token = tokenize_string(schema, json)
    validate_with_positions(token=token, validator=schema)

    json = {
        "emal": "hi@example.com",
    }

    token = tokenize_string(schema, json)
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        for message in error.messages():
            print(message.text)

    json = {}

    token = token

# Generated at 2022-06-14 14:51:42.261053
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse
    from typesystem.tokenize.tokens import tokenize

    source = "{foo: 'bar'}"
    tokens = tokenize(source)
    value = parse(tokens)
    validator = Schema({"foo": Field(str)})
    assert validate_with_positions(token=value, validator=validator) == value.value
    try:
        validate_with_positions(token=value, validator=Schema({"bar": Field(str)}))
    except ValidationError as error:
        message = error.messages()[0]
        assert message.index == ("foo",)
        assert (message.start_position.line_index, message.start_position.char_index) == (
            0, 1  # type: ignore
        )


# Generated at 2022-06-14 14:51:59.687925
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.typing import String, Integer
    from typesystem.tokenize import tokenize

    validator = Integer(minimum=4)

    token = tokenize("1")

    try:
        validate_with_positions(token=token, validator=validator)
    except ValidationError as error:
        assert error.messages()[0].start_position.char_index == 0
        assert error.messages()[0].end_position.char_index == 1

    token = tokenize("1 + 2")

    try:
        validate_with_positions(token=token, validator=validator)
    except ValidationError as error:
        assert error.messages()[0].start_position.char_index == 3
        assert error.messages()[0].end_position.char_index == 4

   

# Generated at 2022-06-14 14:52:07.165570
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    schema = Schema({"name": Field(required=True, types=int)})
    token = tokenize("{}")

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)

    message = exc_info.value.messages[0]
    assert message.start_position.char_index == 1

# Generated at 2022-06-14 14:52:16.828582
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    from tests.test_fields import data, StringField, IntegerField, NestedField

    class Login(Schema):
        username = StringField()
        password = StringField()
        age = IntegerField(required=False)

    class Login2(Schema):
        username = StringField()
        password = StringField()
        age = IntegerField()

    class Login3(Schema):
        username = StringField()
        password = StringField()
        age = IntegerField()
        nested = NestedField(Login, required=False)

    class Login4(Schema):
        username = StringField()
        user = NestedField(Login, required=False)
        password = StringField()
        password2 = StringField()

    login_token = Token.from_data(data)


# Generated at 2022-06-14 14:52:26.879573
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import (
        Schema,
        AnyOfSchema,
        AllOfSchema,
        OneOfSchema,
        ObjectSchema,
    )
    from typesystem.fields import (
        String,
        Integer,
        Boolean,
        Array,
        Object,
        OneOf,
        AnyOf,
        AllOf,
    )
    from typesystem.tokenize.tokens import (
        Token,
        ObjectToken,
        ArrayToken,
        StringToken,
        IntegerToken,
    )

    # Test that an ObjectSchema field matches the position of an error in the validation
    # result of a Token.

# Generated at 2022-06-14 14:52:38.056722
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class MessageSchema(Schema):
        name = Field(primitive=str)
        age = Field(primitive=int)

    schema = MessageSchema()
    token = Token(
        value={
            "name": "Test",
            "age": "foo",
        },
        start=Token(line=1, column=1, char_index=0),
        end=Token(line=1, column=1, char_index=0),
        lookup=lambda *index: None,
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)

# Generated at 2022-06-14 14:52:38.706314
# Unit test for function validate_with_positions
def test_validate_with_positions():
    assert False

# Generated at 2022-06-14 14:52:47.798978
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.fields import String
    from typesystem.exceptions import ValidationError
    from typesystem.tokenize.exceptions import TokenizingError

    token = tokenize("""
        {"name": "Aimee", "age": 30}
    """)
    try:
        validate_with_positions(token=token, validator=String(required=True))
    except ValidationError as error:
        assert error.messages() == [Message(
            text="The field name is required.",
            code="required",
            index=["name"],
            start_position=token.start,
            end_position=token.end,
        )]


# Generated at 2022-06-14 14:52:58.709808
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema({"x": Field(int)})
    token = Token({"x": "3"}, None, None)
    assert validate_with_positions(token=token, validator=schema) == {"x": 3}

    token = Token({}, None, None)
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=schema)
    messages = exc.value.messages
    assert len(messages) == 1
    assert messages[0].text == "The field 'x' is required."

    schema = Schema({"x": Field(int)}, partial=True)
    token = Token({}, None, None)
    assert validate_with_positions(token=token, validator=schema) == {}

# Generated at 2022-06-14 14:53:04.611205
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    from typesystem.schemas import JSONSchema

    schema = JSONSchema(properties={"data": {"type": "string", "required": True}})
    json_data = b'{"foo": "bar"}'
    json_value = json.loads(json_data)
    token = Token.parse(json_data)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    assert exc_info.value.messages() == [
        Message(
            text="The field 'data' is required.",
            code="required",
            index=["data"],
            start_position=token.start,
            end_position=token.end,
        )
    ]


# Generated at 2022-06-14 14:53:14.237539
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.compat import json
    from typesystem.fields import CharField, IntegerField
    from typesystem.tokenize.tokens import parse
    from typesystem.schemas import Schema


    class PersonSchema(Schema):
        age = IntegerField(min_value=21)
        first_name = CharField(max_length=50)

    token = parse(json.dumps({"age": 17, "first_name": "Jenny"}))
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=PersonSchema)
    error = exc_info.value

# Generated at 2022-06-14 14:53:32.200840
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Options(Schema):
        name = Field(type=str)
        age = Field(type=int, required=False)

    json = """{"name": "Buster", "age": 42}"""

    token = Token.from_json(json)

    assert validate_with_positions(token=token, validator=Options) == {
        "name": "Buster",
        "age": 42,
    }

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Field(type=float))
    assert [m.start_position.line_index for m in exc_info.value.messages()] == [1]

    missing_json = """{"name": "Buster"}"""

# Generated at 2022-06-14 14:53:38.882762
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.schemas import Schema
    from typesystem.types import Integer, String, List

    class Movie(Schema):
        title = String()
        year = Integer()
        actors = List[String(max_length=100)]

    json = b'{"title": "Jaws", "year": 1975, "actors": ["Roy Scheider", "Robert Shaw"]}'
    token = tokenize(json)
    validate_with_positions(token=token, validator=Movie)

# Generated at 2022-06-14 14:53:49.742048
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from .objects import TestObjectType
    from .values import TestValueType
    from .compound import TestCompoundType
    from typesystem.tokenize.base import Tokenizer
    from typesystem.tokenize.transform import transform
    from typesystem.tokenize.compile import compile_ast

    tokenizer = Tokenizer()

    tests = [
        (TestValueType, ["foo"]),
        (TestObjectType, {"foo": "bar"}),
        (TestCompoundType, {"value": "foo", "object": {"foo": "bar"}}),
    ]

    for type, value in tests:
        assert validate_with_positions(
            token=transform(compile_ast(tokenizer, value), token_class=Token),
            validator=type,
        ) == value

# Generated at 2022-06-14 14:53:58.922864
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.primitives import String
    from typesystem.structures import Object, Array

    class Person(Object):
        fields = {"name": String()}

    class Family(Array):
        items = Person()

    family = Family()

    try:
        validate_with_positions(
            token=Token(value=[{}, {}, {}], start=(1, 1), end=(1, 13)),
            validator=family,
        )
    except ValidationError as error:
        message = str(error)
    assert (
        message == r"In item 2: The field 'name' is required (1: 6, 1: 11)"
    )

# Generated at 2022-06-14 14:54:05.683452
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer
    from typesystem.tokenize import tokenize

    text = '{"foo": []}'
    token = tokenize(text)
    try:
        validate_with_positions(token=token, validator={"foo": [Integer]})
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="Expected integer but got list",
                code="invalid_type",
                index=["foo", 0],
                start_position=Position(char_index=7),
                end_position=Position(char_index=8),
            )
        ]
    else:
        assert False



# Generated at 2022-06-14 14:54:15.845041
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parse import parse
    from typesystem.tokenize.presets import CoreTokenizer

    tokenizer = CoreTokenizer()
    token_stream = tokenizer.tokenize('{"a": "hello", "b": "world"}')
    token = parse(token_stream)
    try:
        validate_with_positions(token=token, validator=Field(type="string"))
        assert False, "Should fail"
    except ValidationError as error:
        messages = list(error.messages())
        assert len(messages) == 2
        message = messages[0]
        assert message.code == "invalid_type"
        assert message.text.startswith("Expected string.")

# Generated at 2022-06-14 14:54:17.390842
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # TODO
    pass

# Generated at 2022-06-14 14:54:26.617693
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from . import parse_token, parse_field_schema
    from typesystem.fields import String
    from typesystem.schemas import Schema

    schema = Schema({"foo": {"bar": "string"}})

    token = parse_token({"foo": {"bar": "abc"}})
    validator = parse_field_schema(schema)
    validate_with_positions(token=token, validator=validator)

    token = parse_token({"foo": {"bar": ""}})
    validator = parse_field_schema(schema)
    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=validator)

    schema = Schema({})


# Generated at 2022-06-14 14:54:37.505645
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.schemas import Schema as SchemaClass

    class Author(SchemaClass):
        name = String()
        email = String()

    class Book(SchemaClass):
        title = String(required=True)
        author = Author(required=True)

    source = """[
        {
            "title": "The Mythical Man-Month",
            "author": {
                "email": "fred@example.com"
            }
        }
    ]"""

    import simplejson as json

    tokens = json.loads(source)
    result = validate_with_positions(token=Token.from_data(tokens), validator=Book)

    messages = result[0].errors
    assert len(messages) == 2


# Generated at 2022-06-14 14:54:45.727023
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Root
    from typesystem.tokenize.positions import Position, PositionTracker
    from typesystem.tokenize.tokens import MapToken, ScalarToken

    class SkeletonSchema(Root):
        name = Field(required=True)

    schema = SkeletonSchema()
    position_tracker = PositionTracker(text="{}")

    # First check that the original, untransformed error is raised
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=MapToken(value={}, position_tracker=position_tracker),
            validator=schema,
        )

    [error] = exc_info.value.messages()
    assert error.index == ["name"]

# Generated at 2022-06-14 14:55:09.716811
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import parse_json, JsonTokenizer

    validator = Field(type="string")

    tokens = JsonTokenizer().tokenize('"foo"')
    assert validate_with_positions(token=tokens[0], validator=validator) == "foo"

    tokens = JsonTokenizer().tokenize("null")
    try:
        validate_with_positions(token=tokens[0], validator=validator)
        assert False
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "Must be a string."
        assert message.start_position == (0, 0)
        assert message.end_position == (0, 4)