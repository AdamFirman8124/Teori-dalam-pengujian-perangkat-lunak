

# Generated at 2022-06-14 14:45:24.419903
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizers import MsgpackTokenizer
    from typesystem.fields import Object, String, Integer, Boolean

    class TestObject(Object):
        field_one = String(required=True)
        field_two = Integer()
        field_three = Boolean()

    tokenizer = MsgpackTokenizer()
    token = tokenizer.tokenize({})
    error = None
    try:
        validate_with_positions(token=token, validator=TestObject)
    except ValidationError as e:
        error = e

    assert len(error.messages()) == 1
    message = error.messages()[0]
    assert message.text == "The field 'field_one' is required."
    assert message.code == "required"
    assert message.index == ("field_one",)

# Generated at 2022-06-14 14:45:34.943509
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class MySchema(Schema):
        fields = [Field(name="a")]

    class MyField(Field):
        pass

    token = Token(value={"a": None}, offset=0)
    assert validate_with_positions(token=token, validator=MySchema) == {"a": None}

    token = Token(value={"a": None}, offset=0)
    assert validate_with_positions(token=token, validator=MyField) == {"a": None}

    token = Token(value={"a": None}, offset=0)
    try:
        validate_with_positions(token=token, validator=MyField(required=True))
    except ValidationError as error:
        message = error.messages()[0]
        assert message.code == "required"

# Generated at 2022-06-14 14:45:46.527101
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    from typesystem.fields import Array

    from typesystem.schemas import Schema

    from typesystem.types import String

    class UserSchema(Schema):
        name = String()
        email = String()

    class EmailSchema(Schema):
        subject = String()
        to = String()
        body = String()

    class MessageSchema(Schema):
        author = UserSchema()
        messages = Array(EmailSchema())


# Generated at 2022-06-14 14:45:55.994417
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.main import Schema
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.tokens import Document

    class TestSchema(Schema):
        foo = Field(
            {
                "type": "integer",
                "minimum": 0,
                "maximum": 100,
                "required": True,
            },
            position=True,
        )

    tokens = [
        Token(
            "test",
            value=123,
            start={"line": 1, "column": 6, "char_index": 5},
            end={"line": 1, "column": 9, "char_index": 8},
        )
    ]

# Generated at 2022-06-14 14:46:03.371547
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import (
        ObjectToken,
        StringToken,
        TokenType,
    )
    from typesystem.validators import (
        Enum,
        Integer,
        Object,
        String,
    )
    from typesystem.fields import Field

    token = ObjectToken(
        value={
            "name": "John",
            "age": "a",
        },
        name=None,
        start=TokenType(line_number=1, column_number=0, char_index=0),
        end=TokenType(line_number=1, column_number=0, char_index=0),
    )
    validator = Object(
        {
            "name": String(max_length=2),
            "age": Integer(),
        }
    )

# Generated at 2022-06-14 14:46:14.287348
# Unit test for function validate_with_positions
def test_validate_with_positions(): # noqa
    from typesystem.tokenize import Token, TokenType
    from typesystem.fields import String
    from typesystem.tokenize.errors import TokenizeError

    string = String()
    string = string.validate

    try:
        validate_with_positions(token=Token(TokenType.STRING, "a", start=0, end=2), validator=string)
    except TokenizeError as error:
        assert len(error.messages()) == 1
        assert error.messages()[0].text == "String value expected."
        assert error.messages()[0].start_position.line_index == 0
        assert error.messages()[0].end_position.line_index == 0
        assert error.messages()[0].start_position.char_index == 0

# Generated at 2022-06-14 14:46:23.151763
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import structure, fields

    schema = structure.Structure(
        {"text": fields.String(), "number": fields.Integer()},
        required=["text", "number"],
    )
    try:
        validate_with_positions(token=Token({"text": "hello"}), validator=schema)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field 'number' is required.",
                code="required",
                index=("number",),
                start_position=Position(line=1, column=11, character_index=11),
                end_position=Position(line=1, column=19, character_index=19),
            )
        ]



# Generated at 2022-06-14 14:46:30.729616
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import Token

    def validate(schema, json_str):
        token = tokenize(json_str)
        return validate_with_positions(token=token, validator=schema)

    schema = Schema(fields={"foo": Field(type="string")})

    invalid_input = '{"bar": "baz"}'
    with pytest.raises(ValidationError):
        validate(schema, invalid_input)

    invalid_input = '{"foo": 15}'
    with pytest.raises(ValidationError) as excinfo:
        validate(schema, invalid_input)
    error = excinfo.value.messages[0]
    assert error.text == "Must be of type 'string'"
    assert error

# Generated at 2022-06-14 14:46:41.622490
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    from .schemas import employee_schema, salary_schema

    from .base import SimpleMessage, SimplePosition

    class MyPosition(SimplePosition):
        char_index = 0

    tokens = tokenize(
        """
        name: "John",
        age: 10,
        title: "Developer",
        salary: 10000
    """
    )


# Generated at 2022-06-14 14:46:53.280354
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer

    class PetSchema(Schema):
        name = String()
        age = Integer()

    import typesystem.tokenize as tokenize

    tokens = tokenize.tokenize({"name": "Fido", "age": "10"})


# Generated at 2022-06-14 14:47:08.924261
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import fields, tokenize, schemas

    schema = schemas.Schema(
        title="Test",
        fields={
            "id": fields.String(),
            "name": fields.String(),
            "age": fields.Integer(),
            "email": fields.String(format="email"),
            "price": fields.Number(),
            "tags": fields.Array(items=fields.String()),
            "address": fields.Object(
                fields={
                    "street": fields.String(),
                    "number": fields.String(),
                    "zipcode": fields.String(),
                }
            ),
            "is_active": fields.Boolean(),
        },
    )

    # Basic error:

# Generated at 2022-06-14 14:47:15.087430
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizer import tokenize

    class MySchema(Schema):

        name = Field(type="string", required=True)

    tokens = tokenize('{"name": 123}')
    token = tokens[0]
    try:
        validate_with_positions(token=token, validator=MySchema)
        assert False, "Should not get here"
    except ValidationError as error:
        message = error.messages[0]
        assert message.start_position == tokens[0].end
        assert message.end_position == tokens[1].start

# Generated at 2022-06-14 14:47:26.616768
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import typesystem
    from typesystem.tokenize.tokens import Token

    class MySchema(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()


# Generated at 2022-06-14 14:47:37.643278
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    from .lex import lex

    from .parse import parse

    from .resolve import resolve

    from .load import load_file

    from .render import render

    from .validate import validate_with_positions

    from .exceptions import ValidationError

    from .errors import GraphError, Position, Source

    # pylint: disable=no-value-for-parameter

    source = Source(
        name="<string>",
        text="""
            query GetFriend ($id: ID!) {
                friend(id: $id) {
                    name
                }
            }
        """,
        parse_error=None,
        encoding=None,
    )
    tokens = lex(source)
    result = parse("Document", tokens)
    doc = result.value

# Generated at 2022-06-14 14:47:38.746191
# Unit test for function validate_with_positions
def test_validate_with_positions():
    assert False

# Generated at 2022-06-14 14:47:44.644096
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(type="integer", required=True)
    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(token=Token(value=None), validator=field)

    messages = error_info.value.messages()
    assert len(messages) == 1
    assert messages[0].index == ("",)
    assert messages[0].start_position.char_index == 0
    assert messages[0].end_position.char_index == 3


# Generated at 2022-06-14 14:47:55.605078
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import io
    import json

    from typesystem.tokenize.json import JSONTokenizer
    from typesystem.tokenize.tokens import DictToken

    class TestSchema(Schema):
        name = Field(required=True)
        age = Field(required=True, type="integer")

    json_source = io.StringIO("""{"name": "John"}""")
    tokenizer = JSONTokenizer(source=json_source)
    token = DictToken(tokenizer)
    try:
        validate_with_positions(token=token, validator=TestSchema)
    except ValidationError as error:
        messages = list(error.messages())

    assert len(messages) == 1
    assert messages[0].code == "required"
    assert messages[0].index == ("age",)

# Generated at 2022-06-14 14:48:07.527982
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token

    data = {
        "text": {
            "start_position": {"char_index": 0, "line_number": 1},
            "end_position": {"char_index": 5, "line_number": 1},
            "value": "hello",
        }
    }
    token = Token(value=data)

    schema = Schema({"text": String()})
    result = validate_with_positions(token=token, validator=schema)
    assert result == {"text": "hello"}


# Generated at 2022-06-14 14:48:19.850160
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Schema, fields
    from typesystem.tokenize.tokens import Token

    schema = Schema({"foo": fields.String()})
    stream = [Token("foo", {"foo": "bar"})]

    assert len(schema.full_messages(stream)) == 0
    stream[0] = Token("foo", {"foo": ""})
    assert len(schema.full_messages(stream)) == 1
    stream[0] = Token("foo", {})
    assert len(schema.full_messages(stream)) == 1
    stream[0] = Token("foo", "hello")
    assert len(schema.full_messages(stream)) == 1

    # Test non-root validation.
    schema = Schema({"foo": {"bar": fields.String()}})

# Generated at 2022-06-14 14:48:25.333846
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Boolean, Integer
    from typesystem.schemas import Object
    from typesystem.tokenize import tokenize

    class TestSchema(Schema):
        required_field = Integer(required=True)
        nullable_field = Boolean(nullable=True, default=True)
        optional_field = Boolean()

    schema = TestSchema()
    document = {"required_field": 1}
    tokens = tokenize(document)
    error = None
    try:
        validate_with_positions(token=tokens, validator=schema)
    except ValidationError as e:
        error = e

    assert error is not None
    message = error.messages()[0]

    assert message.start_position.line == 1
    assert message.start_position.column == 0
    assert message

# Generated at 2022-06-14 14:48:41.401521
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexers import Lexer
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import String

    field = String(min_length=1)
    lexer = Lexer()

    schema = {
        "type": "object",
        "properties": {
            "foo": {"type": "string"},
            "bar": {"type": "string"},
            "baz": {"type": "string"},
        },
    }
    token = Token.parse_tree(
        tokens=lexer.tokenize(schema),
        validator=field,
        value=schema,
        root=True,
    )

    data = {"bar": ""}

# Generated at 2022-06-14 14:48:48.517250
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.base import validator
    from typesystem.types import String
    from typesystem.tokenize import Token as Token
    from typesystem.errors import ValidationError as ValidationError

    schema = {"a": {"b": validator(String(max_length=1))}}
    token = Token(schema).lookup(["a", "b"])
    token.start = "5:2"
    token.end = "5:3"
    try:
        validate_with_positions(token=token, validator=String(max_length=1))
    except ValidationError as error:
        assert error.messages()[0].start_position == "5:2"
        assert error.messages()[0].end_position == "5:3"


T = typing.TypeVar("T")



# Generated at 2022-06-14 14:49:00.420047
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import pytest
    from typesystem.primitives import String
    from typesystem.schemas import Schema
    from typesystem.utils import load_yaml

    class Person(Schema):
        name = String(required=True)
        age = String(required=True)

    sample = load_yaml("""
        name: Bob
    """)

    sample_json = json.dumps(sample, indent=2)
    sample_yaml = sample_json.splitlines()

    errors = []

    try:
        Person.validate(sample)
    except ValidationError as error:
        errors = error.messages()

    if len(errors) != 1:
        print(errors)
        pytest.fail()

    message = errors[0]
    # there should be a check for the code


# Generated at 2022-06-14 14:49:07.409302
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import io
    from typesystem.tokenize.json import tokenize

    text = "['foo', 'bar', 'baz']"
    fp = io.StringIO(text)

    token = tokenize(fp)
    assert isinstance(token, Token)

    field = Field(type=str)
    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as error:
        message = error.messages[0]
        assert message.text == "Value must be of type str."
        assert message.start_position.char_index == 0
        assert message.end_position.char_index == len(text) - 1



# Generated at 2022-06-14 14:49:19.465112
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from datetime import date
    from typesystem.fields import Date, Integer, String, Array

    class User(Schema):
        name = String()
        age = Integer()
        birthday = Date()

    class Store(Schema):
        users = Array(items=User())

    user = {"name": "foo", "age": "bar"}
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=user, validator=User)
    message = exc.value.messages[0]
    assert message.code == "invalid_type"
    assert message.text == 'Expected value of type "integer" for field "age".'
    assert message.start_position == (1, 8)
    assert message.end_position == (1, 11)


# Generated at 2022-06-14 14:49:31.288413
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Integer, Boolean, OneOf, fields
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.position import OffsetPosition
    from typesystem.validation import ValidationError

    field = String(required=True)
    token = tokenize("")[0]
    assert validate_with_positions(token=token, validator=field) == ""

    field = String(required=True)
    token = tokenize("a")[0]
    assert validate_with_positions(token=token, validator=field) == "a"

    field = Integer()
    token = tokenize("42")[0]
    assert validate_with_positions(token=token, validator=field) == 42

    field = OneOf(name="one of", choices=[Integer(), Boolean()])
   

# Generated at 2022-06-14 14:49:41.283834
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer

    class Alpha(Schema):
        alpha = String(required=True)
        beta = String()
        gamma = String()

    class Foo(Schema):
        foo = String(required=True)
        bar = Integer()
        baz = String()

    class Union(Alpha, Foo):
        pass

    class RootSchema(Schema):
        a = Union(required=True)
        b = Union()

    schema = RootSchema()

    try:
        schema.validate({})
    except ValidationError as e:
        error = e
    assert len(error.messages()) == 1

# Generated at 2022-06-14 14:49:49.835628
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer

    class User(Schema):
        name = String(required=True)
        age = Integer()
        address = String()

    class Address(Schema):
        street = String(required=True)
        number = Integer(required=True)

    class Document(Schema):
        user = User()
        address = Address()

    body = {
        "user": {"name": "peter"},
        "address": {"street": "", "number": 1, "zipcode": 123456},
    }

    document = Document(required=True)
    try:
        document.validate(body)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2

# Generated at 2022-06-14 14:49:54.813787
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(type="string")
    token = Token(
        value="abc",
        start=LinePosition(line=0, column=0, char_index=3),
        end=LinePosition(line=0, column=0, char_index=7),
    )

# Generated at 2022-06-14 14:50:00.614309
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class FooSchema(Schema):
        field = Field(required=True)

    token = Token("", value={"field": "bar"})

    schema = FooSchema()
    result = validate_with_positions(validator=schema, token=token)

    assert result == {"field": "bar"}

    with pytest.raises(ValidationError):
        token = Token("", value={})
        schema = FooSchema()
        validate_with_positions(validator=schema, token=token)

# Generated at 2022-06-14 14:50:17.650172
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(start=None, end=None, value="123")
    # test with valid input
    try:
        validate_with_positions(token=token, validator=Field(type=str))
    except ValidationError:
        assert False, "ValidationError should not be raised"
    # test with invalid input
    token = Token(start=None, end=None, value=1234)
    try:
        validate_with_positions(token=token, validator=Field(type=str))
    except ValidationError as error:
        message = error.messages()[0]
        assert message.code == "invalid_type"
        assert message.index == []
        assert message.start_position == None
        assert message.end_position == None
        assert message.text == "An invalid type was provided"

# Generated at 2022-06-14 14:50:18.097466
# Unit test for function validate_with_positions
def test_validate_with_positions():
    assert True

# Generated at 2022-06-14 14:50:28.058623
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import RootToken
    from typesystem.fields import Boolean, Dict, Integer, String
    from typesystem.fields.base import REQUIRED
    from typesystem.schemas import Array

    token = RootToken(
        value={
            "items": {
                "type": "a",
                "properties": {},
                "additionalProperties": True,
            }
        }
    )

    schema_field = Array(
        of=Dict(
            properties={"active": Boolean(required=True), "age": Integer()},
            additional_properties=Dict(properties={"name": String()}),
        ),
    )


# Generated at 2022-06-14 14:50:39.792671
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        key="dummy",
        value={
            "a": {"b": {"c": "foo"}, "d": "bar", "e": {"f": "baz"}},
            "g": {"h": {"i": "qux"}},
        },
    )
    class Foo(Schema):

        a = Field(type="object")
        b = Field(type="integer")
        c = Field(type="number")
        e = Field(type="object")
        f = Field(type="string")
        h = Field(type="object")
        i = Field(type="string")
        j = Field(type="string")

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=Foo)

# Generated at 2022-06-14 14:50:50.991062
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        first_name = Field(type="string", required=True)

    from typesystem.tokenize import tokenize

    tokens = tokenize(
        {
            "first_name": "",
            "last_name": "boo",
        }
    )

    person = tokens.lookup(["root"])

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(
            token=person, validator=Person
        )

    errors = excinfo.value.messages
    assert len(errors) == 1
    error = errors[0]
    assert error.start_position == tokens.start
    assert error.end_position == tokens.end

# Generated at 2022-06-14 14:50:56.300761
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.validators import MinLength
    from typesystem.tokenize.lexers import Lexer
    from typesystem.tokenize.source import CodeSource

    field = Field(type="string", validators=[MinLength(2)])

    source = CodeSource("""{"foo": "a"}""")
    lexer = Lexer(source=source, schema={"foo": field})

    token = lexer.next()
    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=field)

# Generated at 2022-06-14 14:51:05.901642
# Unit test for function validate_with_positions
def test_validate_with_positions():

    # This is the class we're testing.
    class MySchema(Schema):
        name = Field(type=str, optional=True)

    # Create a test string.
    test_str = '{"name":"Joe"}'

    # Get the tokenized form of the test string.
    test_json = json.loads(test_str)
    test_tokens = Token.from_python(test_json)

    # Call the validate with positions function with a valid token.
    # We expect no errors.
    validate_with_positions(token=test_tokens, validator=MySchema)

    # Call the validate with positions function with a token that has
    # errors. We expect errors.
    test_str = '{"name": []}'
    test_json = json.loads(test_str)
    test

# Generated at 2022-06-14 14:51:16.968244
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import fields
    from typesystem.tokenize import tokenize_and_group
    from typesystem.tokenize.groups import Group

    # Example from the documentation
    class BookSchema(Schema):
        id = fields.Integer()
        title = fields.String()
        isbn = fields.String()
        authors = fields.Array(items=fields.String())
        published_at = fields.DateTime()

        class Meta:
            allow_unknown = True

    group = Group([{"id": 1}, {"title": "How to Train Your Dragon"}])
    try:
        BookSchema.validate(group)
    except ValidationError as error:
        messages = list(error.messages())

# Generated at 2022-06-14 14:51:28.611839
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import schema_registry
    from typesystem.fields import String
    from typesystem.tokenize.django import DjangoTokenizer
    from typesystem.tokenize.tokens import Token

    tokenizer = DjangoTokenizer()
    tokens = tokenizer.tokenize(
        {"name": None, "address": {"city": None}}, schema_registry
    )

    assert tokens[0] == Token(
        index=[0],
        key="name",
        value=None,
        start=0,
        end=5,
        schema=String(),
    )

# Generated at 2022-06-14 14:51:38.730395
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest

    from typesystem.types import Integer
    from typesystem.tokenize.tokens import Token, FileToken

    file_token = FileToken(
        "abc 1 2 3",
        "hello.txt",
        line_index=1,
        char_index=1,
        width=1,
        line_width=8,
    )

    integer_type = Integer()
    string_type = Integer()

    token = Token(
        value="1",
        start=file_token,
        end=FileToken(
            line="234",
            filepath="hello.txt",
            line_index=1,
            char_index=2,
            width=1,
            line_width=8,
        ),
    )


# Generated at 2022-06-14 14:52:05.007080
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.base import Tokens
    from typesystem import Integer

    token = Tokens(
        [
            Token(value=1, start=[0, 1, 0], end=[0, 1, 1]),
            Token(value=0, start=[0, 1, 1], end=[0, 1, 2]),
            Token(value="a", start=[1, 1, 0], end=[1, 1, 1]),
            Token(value=1, start=[1, 1, 1], end=[1, 1, 2]),
        ]
    )

    integer = Integer(minimum=1)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=integer)

    message = exc_info.value.messages[0]

# Generated at 2022-06-14 14:52:13.741740
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tests import PersonSchema

    token = Token(value={"name": "John"}, start=0, end=1)
    try:
        validate_with_positions(token=token, validator=PersonSchema)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field 'age' is required.",
                code="required",
                index=("age",),
                start_position=0,
                end_position=1,
            )
        ]
    else:
        assert False, "Function validate_with_positions should raise an exception"

# Generated at 2022-06-14 14:52:18.854636
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class User(Schema):
        name = Field(str, min_length=1, max_length=30)
        age = Field(int)

    user = """
        { "name": "", "age": 2 }
    """
    t = tokenize(user)

    with pytest.raises(ValidationError):
        validate_with_positions(token=t, validator=User)



# Generated at 2022-06-14 14:52:25.277821
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class FieldType(Field):
        def validate(self, value):
            if not isinstance(value, int):
                raise ValidationError("Field must be an integer.")
            if not 2000 <= value <= 2050:
                raise ValidationError("Field must be between 2000 and 2050.")
            return value

    token = Token(
        value={
            "id": "123",
            "name": "Bob",
            "age": "a string",
            "year": 3000,
        },
        start=Token.Start(
            line=1, column=1, byte_index=0, char_index=0, line_contents="abc"
        ),
        end=Token.End(
            line=1, column=1, byte_index=0, char_index=0, line_contents="abc"
        ),
    )

   

# Generated at 2022-06-14 14:52:36.325129
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class MySchema(Schema):
        foo = {"required": True, "type": "string"}

    source_text = "foobar"
    token = Token(source_text, start=0, end=6, lookup=None, value="foobar")

    validate_with_positions(token=token, validator=MySchema)

    schema = MySchema()
    try:
        schema.validate(token.value)
    except ValidationError as error:
        messages = error.messages()

        for message in messages:
            assert message.index == ("foo",)
            assert message.start_position == token.start
            assert message.end_position == token.end


# Generated at 2022-06-14 14:52:46.123136
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.tokenize.parser import parse_string
    from typesystem.tokenize.tokens import Object
    from typesystem.schemas import (
        Schema,
        Object as ObjectSchema,
        String as StringSchema,
        Integer as IntegerSchema,
    )

    schema = ObjectSchema(properties={"id": IntegerSchema(required=True)})

    source = '{"id": "foo"}'

    with pytest.raises(ValidationError) as error:
        token = parse_string(source)
        validate_with_positions(token=token, validator=schema)
    message = error.value.messages()[0]
    assert isinstance(message, Message)
    assert message.text == "'foo' is not of type 'integer'"
    assert message

# Generated at 2022-06-14 14:52:53.475149
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class TestSchema(Schema):
        foo = Field(name="foo", type=str)

    token = Token(name="root", start=(1, 1), end=(3, 1), value={"foo": ""})

    try:
        validate_with_positions(token=token, validator=TestSchema)
    except ValidationError as error:
        message = error.messages[0]

        assert message.start_position == (2, 1)
        assert message.end_position == (3, 1)

# Generated at 2022-06-14 14:53:02.973465
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.strings import String  # NOQA
    from typesystem.tokenize.lists import List  # NOQA
    from typesystem.schemas import Schema
    import typesystem

    class CheckList(typesystem.Schema):
        item = typesystem.String()

    class Check(Schema):
        a = typesystem.String(required=True)
        b = typesystem.String()
        c = List(item=CheckList())

    class Root(Schema):
        check = Check()

    tokens = tokenize({"check": {"a": "hi", "b": 1, "c": ["1", 2]}}, Root)
    assert isinstance(tokens, Token)
    assert isinstance(tokens.children["check"], Token)

   

# Generated at 2022-06-14 14:53:12.872301
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import schema
    import datetime
    from typesystem.tokenize import tokenize_by_positions

    class MySchema(schema.Schema):
        foo = schema.String()
        bar = schema.String(required=False)
        baz = schema.DateTime()

    json_string = '{"foo": "string", "baz": "2013-02-21T11:05:34"}'
    tokens = tokenize_by_positions(data=json_string)
    try:
        validate_with_positions(token=tokens[1], validator=MySchema)
    except ValidationError as error:
        assert len(error.messages()) == 1
        assert error.messages()[0].start_position.char_index == 9


# Generated at 2022-06-14 14:53:24.170463
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schema import SchemaMetaclass
    from typesystem.fields import String
    from typesystem.tokenize import tokenize

    class Person(metaclass=SchemaMetaclass):
        name = String(required=True)
        age = String()

    tokens = list(tokenize("""
        {
            "name": "John",
        }
    """))

    try:
        validate_with_positions(token=tokens[0], validator=Person)
    except ValidationError as error:
        message = error.messages[0]
        assert message.text == "The field 'age' is required."
        assert message.start_position == (0, 25)
        assert message.end_position == (0, 25)
    else:
        assert False

# Generated at 2022-06-14 14:54:06.992886
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.exceptions import ValidationError
    from typesystem.primitives import String
    from typesystem.tokenize import Source, TokenizeError
    from typesystem.tokenize.tokens import Token

    string = String(min_length=10)
    token = Token(value="hello", parent=Token(value={"foo": "hello"}))
    try:
        validate_with_positions(token=token, validator=string)
    except ValidationError as e:
        message = e.messages()[0]
    assert message.code == "min_length"
    assert message.text == "Must have at least 10 characters."
    assert message.index == ["foo"]

# Generated at 2022-06-14 14:54:16.594463
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import String

    schema = String()

    token = Token(value=None, start=(0, 0), end=(0, 0))
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    assert exc_info.value.messages()[0].start_position == (0, 0)
    assert exc_info.value.messages()[0].end_position == (0, 0)


# Generated at 2022-06-14 14:54:26.274366
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.json_schema import JSONSchema

    schema = JSONSchema({"type": "integer"})
    tokens = Token.parse(
        [{"type": "integer", "value": -5}, {"type": "integer", "value": 10}]
    )

    result = validate_with_positions(
        token=tokens[0], validator=schema
    )
    assert result == -5

    try:
        _ = validate_with_positions(token=tokens[1], validator=schema)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        assert messages[0].start_position.line_index == 0
        assert messages[0].start_position.char_index == 7

        assert messages[0].end

# Generated at 2022-06-14 14:54:28.375055
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.schemas import Schema
    import typesystem

# Generated at 2022-06-14 14:54:38.640484
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.tokenize import tokenize

    class TestSchema(Schema):
        foo = String(required=True)

    tokens = tokenize('{"foo": null}')
    token = tokens[0]

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=TestSchema)

    assert exc_info.value.messages() == [
        Message(
            text="The field 'foo' is required.",
            index=tuple(),
            code="required",
            start_position=token.start,
            end_position=token.end,
        )
    ]

# Generated at 2022-06-14 14:54:46.376233
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from .test_parser_definition import (
        ArticleSchema,
        complex_document,
        simple_document,
    )

    complex_token = complex_document()
    simple_token = simple_document()

    try:
        validate_with_positions(token=complex_token, validator=ArticleSchema)
    except ValidationError as error:
        assert len(error.messages) == 2
        assert error.messages[0].code == "required"
        assert error.messages[0].text == "The field 'title' is required."
        assert error.messages[1].code == "required"
        assert error.messages[1].text == "The field 'text' is required."

    # Now with a simple document

# Generated at 2022-06-14 14:54:55.666849
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import TokenParser

    validator = Field(type="integer")
    tokens = TokenParser(text='{"data": "100"}').parse()
    with pytest.raises(ValidationError) as info:
        validate_with_positions(token=tokens[0]["data"], validator=validator)

    messages = info.value.messages()
    assert len(messages) == 1
    assert messages[0].text == "The value could not be parsed as an integer."
    assert messages[0].start_position.line_index == 0
    assert messages[0].start_position.char_index == 12
    assert messages[0].end_position.line_index == 0
    assert messages[0].end_position.char_index == 13

# Generated at 2022-06-14 14:55:05.154422
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer, String

    # Given that I have a token and a field
    token = Token("foo")
    field = Integer()

    # When I validate the token with the field
    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as error:
        messages = error.messages()

    # Then I see a message with the correct start and end position
    assert messages[0].start_position.line_number == 1
    assert messages[0].start_position.char_index == 0
    assert messages[0].start_position.path == ""
    assert messages[0].end_position.line_number == 1
    assert messages[0].end_position.char_index == 3
    assert messages[0].end_position.path == ""

    # When I

# Generated at 2022-06-14 14:55:14.521417
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token

    class Pet(Field):
        pass

    class User(Schema):
        pets = [Pet]

    from typesystem import errors

    token = Token(
        key="pets",
        value={"name": "Spike"},
        tokens={
            "name": Token(
                key="name", value="Spike", start=(1, 0), end=(1, 9)
            )
        },
        start=(1, 0),
        end=(1, 9),
    )
    with pytest.raises(errors.ValidationError) as _:
        validate_with_positions(token=token, validator=Pet)