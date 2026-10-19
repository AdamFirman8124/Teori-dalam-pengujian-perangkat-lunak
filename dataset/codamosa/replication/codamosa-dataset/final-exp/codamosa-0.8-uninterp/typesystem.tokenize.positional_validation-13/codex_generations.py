

# Generated at 2022-06-14 14:45:23.892936
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from typesystem.schemas import Schema

    class MySchema(Schema):
        foo = "foo"
        bar = "bar"

    class MyField(Field):
        def validate(self, value):
            return value

    # returns the value
    value = validate_with_positions(
        token=Token("foo", {"start": {"char_index": 0}}), validator=MyField()
    )
    assert value == "foo"

    # raise correct error
    schema = MySchema()
    schema.add_field("baz")
    try:
        validate_with_positions(
            token=Token("foo", {"start": {"char_index": 3}}), validator=schema
        )
    except ValidationError as error:
        assert len(error.messages) == 2
        assert list

# Generated at 2022-06-14 14:45:32.095510
# Unit test for function validate_with_positions
def test_validate_with_positions():

    import hypothesis
    import hypothesis.strategies as st

    def message_to_str(message: Message) -> str:
        return " ".join(
            (
                f"{message.code}",
                f'{message.start_position}:{message.end_position}',
                message.text,
            )
        )

    from typesystem.tokenize.tokens import MetaToken, TokenImpl

    from typesystem.fields import Array
    from typesystem import types
    from typesystem.schemas import Schema

    array_of_string = Array(of=types.String())
    array_of_number = Array(of=types.Number())
    array_of_array_of_number = Array(of=array_of_number)

# Generated at 2022-06-14 14:45:42.283542
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import StringField
    from typesystem.tokenize.tokens import StringToken

    schema = Schema(fields={"name": StringField(required=True)})
    token = StringToken(value='{"name": "John"}', start="1:1", end="1:17")

    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.code == "required"
        assert message.text == "The field 'name' is required."
        assert message.start_position.line == 1
        assert message.start_position.char_index == 10
        assert message.end_position.line == 1
        assert message.end_

# Generated at 2022-06-14 14:45:53.405713
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse_file_contents as parse

    def test_validate_with_positions(json):
        schema = Schema({"foo": Field(required=True)})
        token = parse(json)
        validate_with_positions(token=token, validator=schema)

    with pytest.raises(ValidationError) as error:
        test_validate_with_positions("{}")
    assert error.value.messages() == [
        Message(
            start_position=Location(filename='', line=1, char_index=0),
            end_position=Location(filename='', line=1, char_index=1),
            text="The field 'foo' is required.", code='required', index=['foo']
        )
    ]

# Generated at 2022-06-14 14:46:03.760894
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.source import SourceMap
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import String, Structure
    from typesystem.schemas import Schema

    source_map = {
        "start": {"line": 1, "char": 0},
        "end": {"line": 1, "char": 17},
    }
    source = SourceMap(
        "string", source_map, f"{source_map['start']['line']}:{source_map['start']['char']}"
    )
    token = Token(source, {"string": "hello"}, "ROOT", {})

    class TestSchema(Schema):
        name = String(required=True)

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions

# Generated at 2022-06-14 14:46:13.924735
# Unit test for function validate_with_positions

# Generated at 2022-06-14 14:46:23.439694
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem

    class Person(typesystem.Schema):
        name = typesystem.String(max_length=10)

    class Team(typesystem.Schema):
        members = typesystem.Array(items=Person)

    class Company(typesystem.Schema):
        teams = typesystem.Array(items=Team)

    class Root(typesystem.Schema):
        companies = typesystem.Array(items=Company)


# Generated at 2022-06-14 14:46:34.663893
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import (
        ArrayToken,
        DictToken,
        IntToken,
        ListToken,
        StringToken,
    )

    from typesystem.fields import Number, String
    from typesystem.schemas import Schema, Structure

    token = StringToken(
        value="hi",
        start={
            "line_number": 1,
            "char_index": 0,
            "byte_index": 0,
            "line_start_index": 0,
        },
        end={
            "line_number": 1,
            "char_index": 2,
            "byte_index": 2,
            "line_start_index": 0,
        },
    )
    validate_with_positions(token=token, validator=String(format="email"))


# Generated at 2022-06-14 14:46:44.074234
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer

    class Person(Schema):
        name = String(max_length=2)
        age = Integer(minimum=18)

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(
            token=Token(b'{"name": "John James Smith", "age": 17}'), validator=Person
        )

    error = excinfo.value
    assert len(error.messages()) == 3
    assert error.messages()[0].text == 'The field "age" is required.'
    assert error.messages()[0].start_position.line == 1
    assert error.messages()[1].text == 'Value is too short.'
    assert error.messages()[1].start_

# Generated at 2022-06-14 14:46:51.985242
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Array, String

    schema = Array(items=String())
    value = ["abc", 1, "abc"]
    message = validate_with_positions(token=Token(value=value), validator=schema)
    assert message == Message(
        text="Items in the array must all be strings.",
        code="type_error.array.items",
        index=[1],
        start_position=Token(value="1").start,
        end_position=Token(value="1").end,
    )

# Generated at 2022-06-14 14:47:11.376439
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Boolean, Integer, String, Array
    from typesystem.schemas import Schema, Structure

    from .mock_tokenizer import mock_tokenizer

    token = mock_tokenizer({"foo": "bar", "baz": True, "quux": [1, 2, 3]})
    schema = Structure({"foo": String(), "baz": Boolean(), "quux": Array(Integer())})

    try:
        schema.validate(token)
    except ValidationError as error:
        # Duplicate location information
        messages = list(error.messages())

    try:
        result = validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        # Unique location information at the field level
        messages = list(error.messages())


# Generated at 2022-06-14 14:47:20.871270
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    from typesystem.fields import Integer, String

    class Person(Schema):
        """
        A person with a name and an age.
        """

        name = String(max_length=256)
        age = Integer(minimum=0)

    # Create a token for a JSON object representing a person.
    token = tokenize({"name": "John Doe", "age": 42})[0]

    # Validate the person.
    person = validate_with_positions(token=token, validator=Person)

    # Check the validation succeeded.
    assert isinstance(person, dict)
    assert person["name"] == "John Doe"
    assert person["age"] == 42

# Generated at 2022-06-14 14:47:30.427337
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.exceptions import PositionalValidationError
    from typesystem.tokenize import Tokenizer
    from typesystem.fields import IntegerField
    from json import loads

    class Person(Schema):
        """
        A person
        """
        name = IntegerField(required=False)

    class People(Schema):
        """
        A group of people
        """
        members = Person.array()

    tokenizer = Tokenizer(options={"start_position": True})
    tokenized = tokenizer.tokenize(loads(r"""[{"name": "Zach"}]"""))
    tokenized = tokenized.data
    with pytest.raises(PositionalValidationError) as exc:
        validate_with_positions(token=tokenized, validator=People)


# Generated at 2022-06-14 14:47:42.097864
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json

    import pytest

    from typesystem.tokenize.tokenizers import JSONTokenizer

    from typesystem.tokenize.errors import ValidationErrorWithPositions

    schema = Schema({
        'username': s.String(required=True, max_length=3),
        'user_id': s.Integer(required=True),
    })

    validator = schema.get_validator()

    with pytest.raises(ValidationErrorWithPositions) as excinfo:
        validator({'username': 'Al'}, json_tokenizer=JSONTokenizer)

# Generated at 2022-06-14 14:47:53.956905
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from .utils import get_token
    from .types import Author

    token = get_token(
        """
        {
            "name": "John Lennon",
        }
        """
    )
    try:
        validate_with_positions(token=token, validator=Author)
    except ValidationError as error:
        assert len(error.messages()) == 2

        assert error.messages()[0].code == "required"
        assert error.messages()[0].text == "The field 'age' is required."
        assert error.messages()[0].start_position.line_number == 3
        assert error.messages()[0].start_position.char_index == 9

        assert error.messages()[1].code == "invalid_type"
        assert error.messages()[1].text

# Generated at 2022-06-14 14:48:00.571712
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object

    class MySchema(Object):
        field1 = Field(type="string")

    schema = MySchema()
    token = Token("", {}, [
        Token("", {"field1": None}, [])
    ])

# Generated at 2022-06-14 14:48:06.289989
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema({"name": Field(str)})
    def as_char(offset: int) -> int:
        return offset * 4
    text = """{
        "name": "Ahmad"
    }"""
    token = Token.parse(text=text, offset_to_char=as_char)
    validate_with_positions(token=token, validator=schema)



# Generated at 2022-06-14 14:48:18.272136
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """
    Validate a value (i.e. parse) and get detailed error messages
    with locations.
    """
    from typesystem.tokenize.tokens import AttributeToken, DictionaryToken, ListToken
    from typesystem.tokenize import parse
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class MySchema(Schema):
        name = String()

    token = parse({"name": None}, schema=MySchema)
    try:
        validate_with_positions(token=token, validator=MySchema)
    except ValidationError as error:
        [m] = error.messages()
        assert m.code == "required"
        assert m.index == ["name"]
        assert m.text == 'The field "name" is required.'

# Generated at 2022-06-14 14:48:23.312052
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    import typesystem_sql as sql
    from typesystem_sql import (
        Reference,
        Select,
        Table,
        Column,
        Function,
        BinaryOperation,
        ColumnReference,
        Alias,
        WindowDefinition,
        Literal,
        WindowFunction,
    )
    from typesystem_sql.ast import ASTNode
    from typesystem_sql.tokenize import tokenize

    # Create a schema with all elements that can occur in a SQL
    # select statement.

# Generated at 2022-06-14 14:48:32.746652
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import Tokenizer, tokenize

    tokenizer = Tokenizer()

    class Person(Schema):
        name = Field(type=str)
        age = Field(type=int)

    token = tokenize("{}", tokenizer)
    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=Person)
    errors = error.value.messages()
    assert {m.index for m in errors} == {("name",), ("age",)}
    assert [m.text for m in errors] == [
        "The field 'name' is required.",
        "The field 'age' is required.",
    ]
    for message in errors:
        assert message.start_position.char_index is not None  # type: ignore


# Generated at 2022-06-14 14:48:49.976099
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.utils import get_tokens

    class Position(tuple):
        def __repr__(self):
            return f"Position(line_index={self[0]}, char_index={self[1]})"

    class Token(Token):
        def __add__(self, other):
            if isinstance(other, Token):
                value = self.value + other.value
                start = min(self.start, other.start)
                end = max(self.end, other.end)
                return Token(value, start, end)
            return NotImplemented

    class DummyTokenizer:
        def __init__(self, tokens):
            self.tok

# Generated at 2022-06-14 14:48:55.325822
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.tokenize.lexers import Lexer
    from typesystem.tokenize.tokens import Token
    from typesystem.types import String
    from typesystem.error_messages import ErrorMessage

    schema = String(max_length=10)

    lexer = Lexer(
        """
        foo bar baz
    """
    )
    message = pytest.raises(ValidationError, validate_with_positions, token=lexer[0], validator=schema)
    start_position = ErrorMessage(line_index=2, char_index=6)
    message = message.value.messages

# Generated at 2022-06-14 14:49:04.763902
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class Person(Schema):
        name: String
        age: String

    r = tokenize("{ name: 'hello', age: '' }")
    try:
        validate_with_positions(token=r, validator=Person)
    except ValidationError as e:
        assert len(e.messages) == 2
        assert e.messages[0].code == "required"
        assert str(e.messages[0]) == "The field name is required."
        assert e.messages[0].start_position == (1, 5)
        assert e.messages[0].end_position == (1, 10)

# Generated at 2022-06-14 14:49:15.289012
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizer import Tokenizer
    from typesystem.fields import String

    validator = String(min_length=1)

    tokenizer = Tokenizer(json_data='"a"')
    tokenizer.next()
    token = tokenizer.next()
    assert token.value == "a"

    validate_with_positions(token=token, validator=validator)

    tokenizer = Tokenizer(json_data='""')
    tokenizer.next()
    token = tokenizer.next()
    assert token.value == ""

    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=validator)



# Generated at 2022-06-14 14:49:27.360675
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.primitives import String
    from typesystem.tokenize.utils import parse

    source = """
    {
        "name": "foo",
        "place": "",
        "children": [1, 2, 3],
        "incorrect_children": ["1", "2", "3"],
    }
    """
    token = parse(source)
    schema = Schema(
        {
            "name": String(min_length=3),
            "place": String(default="world"),
            "children": String(allow_null=False, min_items=1),
            "incorrect_children": String(allow_null=False, min_length=1, min_items=1),
        }
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_pos

# Generated at 2022-06-14 14:49:37.258993
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class Contact(Schema):
        name = Field(type=str, required=False)
        age = Field(type=int, required=False)
        address = Field(type=str, required=False)


# Generated at 2022-06-14 14:49:45.570306
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer, String
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.utils import parse_value, render_value
    from typesystem.tokenize.utils import tokenize_value

    schema = {"hello": String(), "count": Integer()}
    value = {"hello": "world", "count": 3}
    rendered = render_value(value)
    tokens = tokenize_value(rendered)
    assert tokens[0] == Token("{", type="punctuation", value="{")
    assert tokens[1] == Token("hello", type="property", value="hello")
    assert tokens[2] == Token(":", type="punctuation", value=":")
    assert tokens[3] == Token("world", type="string", value='"world"')

# Generated at 2022-06-14 14:49:57.842625
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexers import Lexer
    from typesystem.tokenize.parsers import parse_schema

    token = Lexer(
        '{"a": "99", "b": "not a number", "c": "Missing a"}'
    ).tokenize()
    schema = parse_schema(
        '{"type": "object", "properties": {"a": {"type": "integer"}, "b": {"type": "integer"}}}'
    )

    validated = validate_with_positions(token=token, validator=schema)

    assert validated == {"a": 99, "b": "not a number", "c": "Missing a"}
    assert validated.messages[0].text == "'b' should be of type 'integer'"
    assert validated.messages[0].start_position.line == 0
   

# Generated at 2022-06-14 14:50:04.553480
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize import tokenize

    def assert_validation_error(tokens, messages):
        try:
            validate_with_positions(token=tokens[0], validator=String())
        except ValidationError as error:
            assert len(error.messages()) == len(messages)
            for message, expected_message in zip(error.messages(), messages):
                assert message.code == expected_message["code"]
                assert message.text == expected_message["text"]
                assert message.start_position == expected_message["start_position"]
                assert message.end_position == expected_message["end_position"]
        else:
            assert False, "ValidationError should have been raised."


# Generated at 2022-06-14 14:50:15.409094
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from json import loads
    from typesystem.fields import Dict
    from typesystem.schemas import JSONSchema
    from typesystem.tokenize import json_tokenize

    schema = Dict(properties={"name": {"type": "string", "required": True}})
    token = json_tokenize(loads('{"age": 3}'))

    try:
        validate_with_positions(
            token=token, validator=schema
        )  # type: ignore
    except ValidationError as error:
        assert error.messages()[0].text == "The field 'name' is required."
        assert error.messages()[0].start_position.line == 1
        assert error.messages()[0].start_position.char_index == 1

# Generated at 2022-06-14 14:50:41.943249
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.structures import cmap, cset
    from typesystem.tokenize.tokens import Token, tokenize_yaml_file, tokenize_yaml

    class User(Schema):
        id: int
        username: str
        first_name: str
        last_name: str
        emails: cmap(str, cset(str))

    fake_data = """
    - id: 1
      username: testuser
      first_name: test
      last_name: user
      emails:
        work:
          - test@example.com
        personal:
          - test@example.com
    """
    tokens = tokenize_yaml(fake_data)


# Generated at 2022-06-14 14:50:53.525633
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas.jsonschema import JSONSchema

    schema = JSONSchema(
        {
            "properties": {
                "name": {"type": "string"},
                "address": {"type": "string"},
                "terms": {"type": "boolean"},
            },
            "required": ["name", "address"],
        }
    )

    document = {"name": "Joe", "address": "123 Main Street"}
    token = Token.build(document, parent=None)
    token = token.get_token("name")
    assert token.value == "Joe"

    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as ex:
        from typesystem.tokenize import line_number
        from typesystem.tokenize.position import CharPosition

# Generated at 2022-06-14 14:51:04.234032
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Dict
    from typesystem.fields import String, Boolean
    from typesystem.tokenize.tokenize import tokenize

    token, _ = tokenize('{"name": "Barry", "active": true}')
    schema = Dict(
        {"name": String(), "active": Boolean()},
        tokenize=True,
    )

    try:
        assert validate_with_positions(token=token, validator=schema) == {
            "name": "Barry",
            "active": True,
        }
    except ValidationError as error:
        messages = [
            message.text
            for message in sorted(
                error.messages, key=lambda m: m.start_position.char_index
            )
        ]

# Generated at 2022-06-14 14:51:15.874551
# Unit test for function validate_with_positions
def test_validate_with_positions():
    def mock_message(text, code, index, start_position, end_position):
        message = Message(
            text=text,
            code=code,
            index=index,
            start_position=start_position,
            end_position=end_position,
        )
        return message

    class MockValidationError:
        def __init__(self, messages):
            self._messages = messages

        def messages(self):
            return self._messages

    def mock_validate(value):
        raise MockValidationError(
            [
                mock_message(text="The field 'username' is required.", index=["username"])
            ]
        )

    class MockToken:
        def __init__(self, *, value, start_index=0, end_index=0):
            self.value = value

# Generated at 2022-06-14 14:51:27.775838
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Profile(Schema):
        required_string = Field(type="string")
        optional_string = Field(type="string")
        required_integer = Field(type="integer")
        optional_integer = Field(type="integer")
        required_number = Field(type="number")
        optional_number = Field(type="number")

    token = Token.parse('{"required_string": "x"}')
    value = validate_with_positions(token=token, validator=Profile)
    assert value == {"required_string": "x"}

    token = Token.parse('{"required_string": "x"}')

# Generated at 2022-06-14 14:51:38.174260
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class UserSchema(Schema):
        name = Field(str, required=True)
        email = Field(str, required=True)

    token = Token(
        {
            "name": "John",
            "email": "john@doe.com",
            "age": 30,
        }
    )
    result = validate_with_positions(token=token, validator=UserSchema)
    assert result == {"name": "John", "email": "john@doe.com"}


# Generated at 2022-06-14 14:51:49.520848
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize.lexer import lex

    from .utils import get_errors, get_token

    schema = Schema(fields={"name": Field(required=True)})

    token = get_token('{"name": null}')
    errors = get_errors(lambda: validate_with_positions(token=token, validator=schema))
    assert len(errors) == 1
    assert errors[0]["code"] == "required"
    assert (
        errors[0]["start_position"][0] == 11
    ), "Should start at start of token"
    assert (
        errors[0]["end_position"][0] == 12
    ), "Should end at end of token"
    assert len(errors) == 1

# Generated at 2022-06-14 14:51:54.270212
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize import error_format_string
    from typesystem.tokenize.tokens import Source
    from typesystem.tokenize.tokenize import Tokenize

    source = Source("testing")
    string_tokenizer = Tokenize(source, String)
    token = string_tokenizer.tokenize(include_char_index=True)
    print("---")
    print(token)
    print("---")
    def validator(v):
        if v is not "hello":
            raise ValidationError(text=f"must be hello")
        return v
    try:
        validate_with_positions(token=token, validator=validator)
    except ValidationError as error:
        print("---")
        print(error.messages())
        print("---")

# Generated at 2022-06-14 14:51:59.025134
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class TestSchema(Schema):
        greeting = String(required=True)

    schema = TestSchema()

    token = Token(
        kind="object",
        start=Token.Position(line=1, char_index=0),
        end=Token.Position(line=2, char_index=1),
        value={"greeting": "hello"},
    )

    validate_with_positions(token=token, validator=schema)



# Generated at 2022-06-14 14:52:05.347883
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        value={"foo": "bar"},
        start=StartPosition(char_index=1, line_index=1, column_index=1),
        end=EndPosition(char_index=17, line_index=1, column_index=17),
    )
    schema = Schema.from_dicts(
        {"foo": {"type": str, "required": True}},
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    assert str(exc_info.value) == "ValidationError: 1 field is invalid."
    path, message = exc_info.value.messages()[0].index, exc_info.value.messages()[0].text

# Generated at 2022-06-14 14:52:45.434181
# Unit test for function validate_with_positions
def test_validate_with_positions():  # NOQA
    from tests import make_token

    token = make_token(
        '{"name": "foo", "age": "", "email": "foo@example.com"}'
    )
    schema = Schema(
        {
            "name": Field(str),
            "age": Field(int),
            "email": Field(str),
        },
        many=False,
    )
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        error.messages()[0].start_position  # type: ignore
        error.messages()[0].end_position  # type: ignore

# Generated at 2022-06-14 14:52:56.629341
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.validators import String

    validator = String(min_length=10)
    schema = {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
            },
            "address": {
                "type": "object",
                "properties": {
                    "street": {
                        "type": "string",
                        "pattern": "^[0-9]+$"
                    },
                    "postcode": {
                        "type": "string" 
                    }
                }
            }
        }
    }


    # VALIDATION TEST
    token = Token(
            "address",
            {
                "street": "123",
                "postcode": "123"
            },
            None,
            None,
            None
        )
    


# Generated at 2022-06-14 14:53:05.053677
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typing import Dict, Any

    class User(Schema):
        name = Field(str)
        age = Field(str, optional=True)

    class Organization(Schema):
        users = Field(dict, value_type=User)

    with open(f"{os.path.dirname(__file__)}/../tests/data/schema.yaml", "rb") as file:
        data = file.read()
        token = Token.from_string(data)
        value = validate_with_positions(
            token=token, validator=Organization
        )  # type: Dict[str, Any]

        assert type(value["name"]) is str
        assert type(value["users"][0]["name"]) is str

# Generated at 2022-06-14 14:53:14.537074
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize import Tokenizer
    from typesystem.tokenize.errors import TokenizationError

    source = """
        {"first_name": "Joe", "last_name": "Berry"}
    """
    tokenizer = Tokenizer()
    try:
        token = tokenizer.load(source)
    except TokenizationError as error:
        assert len(error.messages) == 0
        return

    class PersonSchema(Schema):
        first_name = String(required=True)
        last_name = String(required=True)

    try:
        data = validate_with_positions(token=token, validator=PersonSchema)
        assert data is None
    except ValidationError as error:
        assert len(error.messages) == 1

# Generated at 2022-06-14 14:53:26.318094
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.tokenizer import Tokenizer
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.validators import is_str
    from typesystem import Message

    text = '{"name": "foo"}'
    tokenizer = Tokenizer()
    token = tokenizer.tokenize(text)

    class Account(Schema):
        name = String(validators=[is_str])

    messages = []

    def on_error(error: ValidationError) -> None:
        messages.extend(error.messages())

    try:
        validate_with_positions(token=token, validator=Account)
    except ValidationError:
        pass

    message = messages[0]
    assert message.text

# Generated at 2022-06-14 14:53:37.135682
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema(fields={"foo": Field()})
    doc = {"foo": "bar"}
    token = Token.document(doc)
    v = validate_with_positions(token=token, validator=schema)
    assert v == doc

    schema = Schema(fields={"foo": Field(required=False)})
    doc = {"foo": "bar"}
    token = Token.document(doc)
    v = validate_with_positions(token=token, validator=schema)
    assert v == doc

    schema = Schema(fields={"foo": Field()})
    doc = {}
    token = Token.document(doc)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    assert exc_

# Generated at 2022-06-14 14:53:48.130876
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from datetime import date
    from typesystem.base import String
    from typesystem.fields import (
        Boolean,
        Date,
        Integer,
        Object,
        String,
        Union,
    )
    from typesystem.schemas import Schema
    from typesystem.tokenize.parser import parse_document

    class TestSchema(Schema):
        id = Integer()
        name = String()
        age = Integer()
        is_alive = Boolean()
        birthday = Date()
        custom = Union([String(), Integer()])

    doc_string = """id: 123
name: "dummy"
age: abc
is_alive: xyz
birthday: 12/05/1989
custom: true"""
    doc_tokens = parse_document(doc_string)

# Generated at 2022-06-14 14:53:59.736517
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class MySchema(Schema):
        name = Field(str)
        age = Field(int, required=True)

    schema = MySchema()
    tokens = tokenize(b"foo 42")
    actual = validate_with_positions(token=tokens, validator=schema)
    assert actual == {"name": "foo", "age": 42}

    tokens = tokenize(b"foo")
    try:
        validate_with_positions(token=tokens, validator=schema)
    except ValidationError as error:
        assert len(error.messages()) == 1
        assert error.messages()[0].start_position.line == 1
        assert error.messages()[0].start_position.char_index == 5

# Generated at 2022-06-14 14:54:07.513121
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.utils import Pos

    class MyField(Field):
        def validate(self, value):
            if value == "foo":
                raise ValidationError("This value is not allowed.")

    token = Token(
        value={
            "id": "123",
            "foo": "foo",
            "bar": {"baz": "foo", "qux": "qux"},
        },
        start=Pos(line=1, column=1),
        end=Pos(line=1, column=26),
    )

    try:
        validate_with_positions(token=token, validator=MyField())
    except ValidationError as error:
        message = error.messages()[0]
        assert message.start_position.line == 1

# Generated at 2022-06-14 14:54:16.980472
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.typing import Boolean

    from .tokenize import tokenize, Token  # type: ignore

    token = tokenize(
        [
            {"name": "Alice"},
            {"name": "Bob"},
        ],
        name=String(),
        alpha=Boolean(),
        beta=Boolean(),
    )
    token = Token(
        name="array", value=token.value, children=token.children, leaf=False
    )

    field = Field(name="alpha", type=Boolean())
    validate_with_positions(token=token.children[0], validator=field)

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token.children[1], validator=field)
    messages = excinfo.value.messages