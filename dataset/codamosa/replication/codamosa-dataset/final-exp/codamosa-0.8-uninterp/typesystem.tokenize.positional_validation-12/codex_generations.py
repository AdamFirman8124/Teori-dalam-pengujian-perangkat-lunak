

# Generated at 2022-06-14 14:45:20.860460
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.schemas import Schema
    from typesystem.fields import Field, String

    class Address(Schema):
        street = Field(String)
        postal_code = Field(String)

    class Person(Schema):
        name = Field(String)
        age = Field(String)
        address = Field(Address)

    data = {
        "name": "John",
        "age": "42",
        "address": {
            "street": "Main St",
            "postal_code": "12345",
        }
    }

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=Token(data), validator=Person)


# Generated at 2022-06-14 14:45:30.036709
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Dict, String
    from typesystem.tokenize import tokenize

    schema = Dict({"name": String(max_length=5)})
    message = "The field 'name' should contain less than 5 characters."
    message += " Current length is 8."

    try:
        validate_with_positions(
            token=tokenize("{'name': 'johndoe'}"), validator=schema
        )
    except ValidationError as error:

        assert error.messages()[0].text == message
        assert error.messages()[0].start_position.line == 0
        assert error.messages()[0].start_position.char_index == 8
        assert error.messages()[0].end_position.line == 0
        assert error.messages()[0].end

# Generated at 2022-06-14 14:45:36.358882
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class Todo(Schema):
        title = Field(type=str, required=True)
        position = Field(type=int)

    raw = {
        "title": "Foo",
        "position": "1",
    }

    token = tokenize(raw)

    try:
        validate_with_positions(token=token, validator=Todo)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        message = messages[0]
        assert message.text == "The field 'position' must be of type 'int'."
        assert message.start_position.char_index == 20
        assert message.end_position.char_index == 24



# Generated at 2022-06-14 14:45:48.218050
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from typesystem.schemas import Schema
    from typesystem.fields import Integer, String
    from typesystem.tokenize import parse

    schema = Schema(fields={"x": String(), "y": Integer()})

    token = parse(
        r"""{
            "x": "a",
            "y": "b"
        }"""
    )

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=schema)
    errors = excinfo.value.messages()
    assert len(errors) == 2
    x_error = next(e for e in errors if e.index[-1] == "x")
    assert x_error.text == '"a" is not a valid String.'
    assert x_error.start_position.line

# Generated at 2022-06-14 14:45:56.881652
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # XXX: this is horrible
    import pytest
    from typesystem.fields import String
    from typesystem.schemas import Schema

    from typesystem.tokenize.tokens import StringToken

    schema = Schema({"name": String()})
    value = "bob"
    token = StringToken(value="bob", name="name")
    # check no exception is thrown
    schema.validate(value)
    # check that an exception IS thrown
    with pytest.raises(ValidationError) as excinfo:
        value = {"name": "bob"}
        # get the string representation of our dict,
        # and add that to the token
        token = StringToken(value=str(value), name="name")
        validate_with_positions(token=token, validator=schema)
    # check

# Generated at 2022-06-14 14:46:08.357376
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem import fields
    import json

    schema = fields.Dict({"foo": fields.Integer()}, required=True)
    value = {}
    token = Token.from_value(value)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    assert exc_info.value.messages() == [
        Message(
            text='The field "foo" is required.',
            code="required",
            index=("foo",),
            start_position=token.start,
            end_position=token.end,
        )
    ]
    value = json.loads('{"foo": "bar"}')

    token = Token.from_value(value)
   

# Generated at 2022-06-14 14:46:19.015138
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.base import Tokenizer
    from typesystem.tokenize.composite import Dictionary

    fields = {
        "field_with_validation_error": Field[int](required=True)
    }
    tokenizer = Tokenizer()
    token = tokenizer.tokenize({}, Dictionary(fields))
    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(token=token, validator=Dictionary(fields))

# Generated at 2022-06-14 14:46:28.124610
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from datetime import date
    from typesystem import Integer, String, Date, Schema

    from .tokenize import tokenize

    class TestSchema(Schema):
        id = Integer()
        name = String()
        birthday = Date()

    string = """
    {
      "id": 1,
      "name": "John Doe",
      "birthday": "1948-01-15"
    }
    """
    tokens = tokenize(string)
    token = tokens[0]
    assert validate_with_positions(token=token, validator=TestSchema) == {
        "id": 1,
        "name": "John Doe",
        "birthday": date(1948, 1, 15),
    }


# Generated at 2022-06-14 14:46:36.310318
# Unit test for function validate_with_positions
def test_validate_with_positions():
    try:
        validate_with_positions(
            token=Token(value={"foo": "hello"}, path=["path"], start=None, end=None),
            validator=Schema({"foo": Field(required=True, deserialize=str)}),
        )
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field 'bar' is required.",
                code="required",
                index=["bar"],
                start_position=None,
                end_position=None,
            )
        ]

# Generated at 2022-06-14 14:46:44.843931
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.json_schema import JSONSchema
    from typesystem.tokenize import tokenize

    schema = JSONSchema.from_dict(
        {
            "properties": {
                "a": {"type": "string"},
                "b": {"type": "integer"},
                "c": {"enum": ["a", "b", "c"]},
            },
            "required": ["a", "c", "d"],
        }
    )

    token = tokenize({"a": "foo", "b": 10, "c": "a"})

    assert validate_with_positions(token=token, validator=schema) == token.value

    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        assert len(error.messages())

# Generated at 2022-06-14 14:46:58.309964
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typing import Mapping
    from typesystem.fields import Dict, Number
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.utils import load_grammar

    schema = Dict(
        properties={"a": Dict(properties={"b": Number(required=True)}, required=True)}
    )

    grammar, root = load_grammar("tests/examples/basic.json")
    try:
        validate_with_positions(
            token=root, validator=schema,
        )
    except ValidationError:
        assert False

    grammar, root = load_grammar("tests/examples/basic.json")

# Generated at 2022-06-14 14:47:09.361456
# Unit test for function validate_with_positions

# Generated at 2022-06-14 14:47:19.458818
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import schema, fields

    class UserSchema(schema.Schema):
        name = fields.String(max_length=10, required=True)
        age = fields.Integer()

    @UserSchema.validator()
    def validate_schema(self, value: schema.Dict):
        token = Token(value)
        return validate_with_positions(token=token, validator=self)

    value = {"name": "Bob"}
    try:
        UserSchema.validate(value)
    except ValidationError as error:
        assert len(error.messages()) == 1
        assert error.messages()[0].text == "The field 'age' is required."
        assert error.messages()[0].start_position.line == 1
        assert error.messages()[0].start

# Generated at 2022-06-14 14:47:29.501413
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest

    from typesystem.tokenize.lexers.json import JsonLexer
    from typesystem.fields import String
    from typesystem.schemas import Schema

    lexer = JsonLexer()
    value = lexer.tokenize("""{"a": 5}""")
    schema = Schema({"a": String()})

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=value, validator=schema)

    assert error.value.messages[0].text == "The field 'a' must be a string."
    assert [m.index for m in error.value.messages] == [['a']]
    assert error.value.messages[0].start_position.line == 1
    assert error.value.messages[0].start

# Generated at 2022-06-14 14:47:36.671053
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import ObjectToken

    token = ObjectToken(value={"field": None}, position=None)
    schema = Schema(validators={"field": Field(required=True)})

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)

    assert exc_info.value.messages[0].start_position.char_index == 11

# Generated at 2022-06-14 14:47:46.067883
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import DictToken, ListToken, RootToken, Token
    from typesystem.tokenize.tokenizer import tokenize_for_schema
    from typesystem.schemas import Schema
    from typesystem.fields import String, Number, Array

    class UserSchema(Schema):
        id = Number(required=True)
        name = String(required=True)
        friends = Array(items=String(), required=True)

    class User(RootToken):
        @classmethod
        def tokenizer(cls, value):
            return tokenize_for_schema(UserSchema(), value)


# Generated at 2022-06-14 14:47:56.237273
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Schema, fields, tokenize
    from typesystem.tokenize.errors import ParseError

    class MySchema(Schema):
        title = fields.String(required=True)
        age = fields.Integer(minimum=12)

    schema = MySchema.fields["age"]

    token = tokenize.parse({}, "age: 11")[0]
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=schema)
    assert str(excinfo.value) == "The field 'age' must be at least 12."

    token = tokenize.parse({}, "title: 'Jim'")[0]

# Generated at 2022-06-14 14:48:03.922827
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass
    # data = {"a": {"b": {"c": ""}}}
    # schema = Field(type="object", properties={"a": Field(type="object", properties={"b": Field(type="object", properties={"c": Field(required=True)})})})
    # token = tokenize(data)
    # error = validate_with_positions(token=token, validator=schema)
    # print(error.messages())

# Generated at 2022-06-14 14:48:04.530963
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:48:11.793816
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(
        type="string",
        min_length=1,
        # Here, we will use the "required" error message to test
        # positional errors.
        required=True,
    )

    def validate_value(value: typing.Any) -> str:
        return validate_with_positions(token=value, validator=field)

    assert validate_value("foo") == "foo"

    try:
        validate_value("")
    except ValidationError as error:
        assert len(error.messages()) == 1
        message = error.messages()[0]
        assert message.start_position.line_index == 0
        assert message.start_position.char_index == 0
        assert message.end_position.line_index == 0
        assert message.end_position.char_index == 0


# Generated at 2022-06-14 14:48:26.357707
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        value={
            "foo": {
                "a": 1,
                "b": 2,
                "c": {
                    "a": 1,
                    "b": 2,
                },
            },
        },
        start=None,
        end=None,
    )

    class MyField(Field):
        def to_python(self, value):
            return value * 2

    class MySchema(Schema):
        foo = MyField()
        bar = MyField(required=True)

    # Validator is a Field
    validate_with_positions(token=token, validator=MyField())

    # Validator is a Schema
    validate_with_positions(token=token, validator=MySchema())

    # Validation error

# Generated at 2022-06-14 14:48:34.583870
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.tokenize import tokenize_json

    class Token(typing.NamedTuple):
        value: typing.Any
        start: typing.Tuple[int, int]
        end: typing.Tuple[int, int]
        lookup: typing.Callable[[typing.List[str]], "Token"]

    tree = {
        "name": "arthur",
        "age": "2",
        "address": None,
        "things": [1, 2, 3, "b"],
    }
    field = String(min_length=1)

# Generated at 2022-06-14 14:48:46.566006
# Unit test for function validate_with_positions
def test_validate_with_positions():  # noqa
    # pylint: disable=import-outside-toplevel
    from typesystem.tokenize.tokens import ObjectToken
    from typesystem.tokenize.types import Position
    from typesystem.tokenize.utils import tokenize

    schema = Schema({"name": Field(required=True)})
    text = '{"name": "foo"}'

    start = Position(line=1, column=1, char_index=0)
    end = Position(line=1, column=16, char_index=15)
    token = ObjectToken(start=start, end=end, value={"name": "foo"})
    assert validate_with_positions(token=token, validator=schema) == {"name": "foo"}

    text = '{"hello": "world"}'

# Generated at 2022-06-14 14:48:58.934239
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.positions import Position
    from tests.helpers import assert_error_message_equal

    class Person(Schema):
        name = Field(type=str)
        age = Field(type=int)

    text = '{"name": "Foo", "age": "15"}'
    token = Token.from_json(text)

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=Person)

    exc_message = exc.value.messages[0]

# Generated at 2022-06-14 14:49:05.484551
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.fields import String

    errors = None
    token = tokenize('"abc"')
    try:
        validate_with_positions(token=token, validator=String(max_length=2))
    except ValidationError as error:
        errors = error.messages()

    assert len(errors) == 1
    assert errors[0].start_position.line_number == 1
    assert errors[0].start_position.char_index == 0
    assert errors[0].end_position.line_number == 1
    assert errors[0].end_position.char_index == 4



# Generated at 2022-06-14 14:49:17.325826
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object
    from typesystem.fields import String

    token = Token({"name": "", "age": 42})
    schema = Object({"name": String(), "age": String()})

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)

    message = exc_info.value.messages[0]
    assert message.text == "The field 'name' may not be blank."
    assert message.start_position.line == 1
    assert message.start_position.char_index == 7
    assert message.end_position.line == 1
    assert message.end_position.char_index == 11

    message = exc_info.value.messages[1]

# Generated at 2022-06-14 14:49:29.341315
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from typesystem.tokenize.json import load_json

    def assert_error_text(
        *, source: str, expected_text: typing.List[str]
    ) -> None:
        root_token = load_json(source)
        class Person(Schema):
            name = Field(str)
            age = Field(int)

        try:
            validate_with_positions(token=root_token, validator=Person)
        except ValidationError as error:
            assert [msg.text for msg in error.messages()] == expected_text
        else:
            pytest.fail(
                "Expected to see a ValidationError, but received no error."
            )


# Generated at 2022-06-14 14:49:37.729063
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    string = String(required=True)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=Token(""), validator=string)

    messages = [
        Message(
            text="The field '' is required.",
            code="required",
            index=(),
            start_position=Position(char_index=0, line_index=1, column_index=1),
            end_position=Position(char_index=0, line_index=1, column_index=1),
        )
    ]
    assert exc_info.value.messages == messages


# Generated at 2022-06-14 14:49:47.692338
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import types

    field = types.String(max_length=10)

    token = Token(value=["a", "b", "c"], start=Position(line=1, char_index=10))
    validate_with_positions(token=token, validator=field)

    token = Token(value=["a", "b", "c", "d", "e", "f"], start=Position(line=1, char_index=10))
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=field)
    assert exc_info.value.messages == [Message(text="Must have no more than 10 items.", code="max_items")]


# Generated at 2022-06-14 14:49:54.615397
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class BeginSchema(Schema):
        key = Field(key=True)
        value = Field()

    json_string = """
    {
       "key": 1,
       "value": 1
    }
    """

    json_token = Token.from_data(json.loads(json_string))
    validate_with_positions(token=json_token, validator=BeginSchema)

# Generated at 2022-06-14 14:50:14.041803
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Structure
    from typesystem.tokenize.tokens import ObjectToken

    class TestSchema(Structure):
        a = 1
        b = 2
        c = 3
        d = 4

    class NoDefaultField(Field):
        pass

    class DefaultField(Field):
        default = 1

    test_schema = TestSchema(fields={"a": NoDefaultField(), "b": DefaultField()})

    token = ObjectToken(
        value={"a": 2, "c": 30, "d": "foo"},
        start={"line": 1, "char_index": 1},
        end={"line": 2, "char_index": 5},
    )


# Generated at 2022-06-14 14:50:25.316941
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from . import tokenize_field, tokenize_schema

    from typesystem.fields import Int, String
    from typesystem.schemas import Schema

    class User(Schema):
        username = String(required=True)
        age = Int()

    token = tokenize_schema(User, {"username": "bob"})

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=User)

    error = excinfo.value
    message = error.messages[0]
    assert message.code == "required"
    assert message.text == "The field 'age' is required."
    assert message.start_position.line == 1
    assert message.start_position.char_index == 18
    assert message.end_position.line == 1

# Generated at 2022-06-14 14:50:32.777266
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(type="string")

    token = Token.from_yaml({"name": "Alice"})
    validate_with_positions(token=token, validator=Person)

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=Person(required=True))

    errors = exc.value.messages()

    assert len(errors) == 1
    error = errors[0]
    assert (error.start_position.line, error.start_position.char_index) == (
        token.start.line,
        token.start.char_index,
    )

# Generated at 2022-06-14 14:50:42.611429
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # pylint: disable=redefined-outer-name,no-self-use

    import pytest

    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token

    class MySchema(Schema):

        field1 = int
        field2 = str

    # Create test tokens that can be used to make the test repeatable
    fake_source_code = '{"field1": "foo", "field2": 42}'
    pos_0 = Token.Position(line=1, column=1, char_index=0)
    pos_1 = Token.Position(line=1, column=2, char_index=1)
    pos_2 = Token.Position(line=1, column=3, char_index=2)

# Generated at 2022-06-14 14:50:53.625367
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer

    class Person(Schema):
        name = String()
        age = Integer()

    def test_person(s):
        return validate_with_positions(
            token=tokenize(s), validator=Person()
        )

    test_person("{name: 'John', age: 8}")

    with pytest.raises(ValidationError) as exc_info:
        test_person("{name: 'John'}")

    error = exc_info.value
    assert len(error.messages()) == 1
    message = error.messages()[0]
    assert message.index == ["age",]
    assert message.start_position.line_num == 1

# Generated at 2022-06-14 14:51:04.271553
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object, String
    from typesystem.tokenize.parser import parse

    schema = Object(
        properties={"name": String(min_length=5, max_length=10), "age": String(max_length=2)}
    )
    token = parse("""
    {
        "name": "Joe",
        "age": 89
    }
    """)
    try:
        value = validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2
        assert messages[0].text == "String value is too short."
        assert messages[1].text == "String value is too long."
    else:
        assert False, "Should have raised an exception."

# Generated at 2022-06-14 14:51:15.918235
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """
    Validate_with_positions creates ValidationErrors whose messages contain
    start and end positions. This allows us to find out where in the
    JSON/YAML/XML input a validation error occured.
    """
    from .utils import get_example_schema

    schema = get_example_schema()

    # Creating a schema object from the schema.
    schema_schema = Schema.from_fields(schema.fields)

    token = schema.tokenize(dict(name="John Doe"))

    # -> Does not raise a ValidationError
    validate_with_positions(token=token, validator=schema_schema)


# Generated at 2022-06-14 14:51:27.819228
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Type helpers
    def validate(*, token: Token) -> typing.Any:
        return validate_with_positions(token=token, validator=Schema)

    # Happy path

# Generated at 2022-06-14 14:51:38.180351
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest

    from tests.base import Person, PersonSchema

    field = Field(required=True, type="integer")
    token = Token(value=None, start=None, end=None)
    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.start_position is None
        assert message.end_position is None
    else:
        assert False, "Expected a ValidationError to be raised."

    schema = PersonSchema(strict=True)
    token = Token(value=Person(name="John Doe"), start=None, end=None)

# Generated at 2022-06-14 14:51:49.520903
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import parse
    from typesystem.json_schema import from_json_schema
    from typesystem import fields, schemas
    from typesystem.tokenize.tokens import Token, KeyToken, ValueToken

    # Define a simple schema
    class UserSchema(schemas.Schema):
        username = fields.String(max_length=64)
        password = fields.String(min_length=8)

    schema = from_json_schema(
        {
            "type": "object",
            "properties": {
                "username": {"type": "string", "maxLength": 64},
                "password": {"type": "string", "minLength": 8},
            },
        }
    )

    # Build and parse a JSON payload.

# Generated at 2022-06-14 14:52:15.253149
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import yaml

    schema = """
    title: Person
    properties:
      name:
        type: string
        required: true
      age:
        type: integer
    """

    token = Token.from_python_structure(
        json.loads(
            """
            {
              "name": "Fred",
              "age": "21"
            }
            """
        ),
        parser=json.loads,
        serializer=lambda x: json.dumps(x, indent=2),
    )

    try:
        validate_with_positions(
            token=token, validator=yaml.load(schema, Loader=yaml.SafeLoader)
        )
    except ValidationError as error:
        message = error.messages()[0]
        assert message.end_position

# Generated at 2022-06-14 14:52:25.389425
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # type: () -> None
    token = Token(
        value={"age": "old", "gender": "?", "address": {"street": "example"}},
        start=Token.Position(line_number=1, char_index=1),
        end=None,
    )

    schema = Schema(
        {
            "age": Field(required=True, type="string"),
            "gender": Field(required=True, type="string"),
            "address": Schema({"street": Field(required=True, type="string")}),
        }
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)


# Generated at 2022-06-14 14:52:36.473295
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import JSONField
    from typesystem.schemas import Schema, StructureField, DictionaryField
    from typesystem.tokenize.parser import parse_text

    def test(text: str, validator: typing.Union[Field, typing.Type[Schema]], *, expect: bool):
        token = parse_text(text)
        if expect:
            validate_with_positions(token=token, validator=validator)
        else:
            with raises(ValidationError) as exc_info:
                validate_with_positions(token=token, validator=validator)
        errors = exc_info.value.messages() if not expect else []
        assert errors

    # --- JSON type ---
    test(text='""', validator=JSONField(), expect=True)

# Generated at 2022-06-14 14:52:46.232752
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import (
        ArraySchema,
        BooleanSchema,
        FloatSchema,
        IntegerSchema,
        ObjectSchema,
        StringSchema,
    )
    from typesystem.tokenize.tokens import ArrayToken, StringToken

    for token in [StringToken(value="hello"), ArrayToken(value=[])]:
        try:
            validate_with_positions(token=token, validator=IntegerSchema())
        except ValidationError as error:
            (message,) = error.messages()
    assert (
        message.text == "Expected an integer, but got "
        f"{token.value!r} of type {type(token.value).__name__!r}."
    )

# Generated at 2022-06-14 14:52:57.572688
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize_string
    from typesystem.tokenize.tokens import Token

    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.exceptions import ValidationError

    class PersonSchema(Schema):
        name = String(required=True)

    # Parses into a token stream.
    tokens = tokenize_string("Person", """
    {
        "name": 42
    }
    """)

    # Create a root token.
    token = Token(tokens=tokens, path=[])

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=PersonSchema)

# Generated at 2022-06-14 14:53:04.796240
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.exceptions import ValidationError
    from typesystem.schema import Schema
    from typesystem.fields import String, Integer

    from tests.utils import tokenize

    class Lang(Schema):
        name = String(max_length=10)
        year = Integer()

    schema = Lang()

    tokens = tokenize("""
        [
            {
                name: "Python",
                year: 1991
            },
            {
                name: "Lua",
                year: 1993
            }
        ]
    """)
    array_token = tokens.lookup([3])

    try:
        schema.validate(array_token)
    except ValidationError as error:
        print(error.messages())

# Generated at 2022-06-14 14:53:10.848128
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize import tokenize

    token = tokenize("""
    {
        "a": "foo",
        "b": "bar"
    }
    """)
    assert validate_with_positions(
        token=token, validator=String(name="a", min_length=10)
    )

# Generated at 2022-06-14 14:53:22.304220
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.json_schema import load as load_json_schema
    from typesystem.tokenize.tokenizers import tokenize

    schema = load_json_schema({
        "type": "object",
        "properties": {
            "foo": {"type": "number"},
            "bar": {"type": "number"},
        },
        "required": ["foo"],
    })

    json = '''{
        "foo": 1,
        "bar": "bad-value"
    }'''

    token = tokenize(json)
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2

# Generated at 2022-06-14 14:53:33.693919
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer
    from typesystem.tokenize.tokens import (
        NewlineToken,
        SpaceToken,
        StringToken,
        TokenizerError,
    )

    tokenizer = Tokenizer()
    tree = tokenizer.tokenize(
        "list [\n" "  1\n" "  2\n" "]",
        tokens=[StringToken, NewlineToken, Integer, NewlineToken, Integer, NewlineToken],
    )

    assert tokenizer.errors() == {
        TokenizerError(
            message="Expected an integer.",
            line_index=0,
            column_index=5,
        )
    }


# Generated at 2022-06-14 14:53:42.648813
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import fields, schemas
    from typesystem.tokenize.tokens import Item

    class Validator(fields.Field):
        def validate(self, value):
            if not isinstance(value, str):
                raise ValueError
            return value

    token = Item("bar", start=(1, 1), end=(1, 1))
    value = validate_with_positions(token=token, validator=Validator())
    assert value == "bar"

    schema = schemas.Schema(
        [("x", Validator()), ("y", Validator()), ("z", Validator())]
    )
    token = Item(
        (Item("ab"), Item("cd"), Item("ef")),
        start=(1, 1),
        end=(1, 1),
        data_type="sequence",
    )
   

# Generated at 2022-06-14 14:54:12.820807
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:54:19.735734
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Boolean, Integer, Object, String

    schema = Object(
        {"name": String(max_length=20), "age": Integer, "admin": Boolean}
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=Token(value=True), validator=schema.fields["admin"]
        )

    message = exc_info.value.messages()[0]
    assert message.text == "Value must be a boolean."
    assert message.code == "invalid_type"
    assert message.index == ("admin",)
    assert message.start_position == {"line": 1, "char_index": 16}
    assert message.end_position == {"line": 1, "char_index": 17}

# Generated at 2022-06-14 14:54:30.640934
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import fields
    from typesystem.tokenize.parser import parse
    from typesystem.tokenize.tokens import Field as FieldToken, Integer
    from typesystem.tokenize.positions import get_start, get_end

    token = FieldToken(
        name="foo",
        value=parse(
            [FieldToken(name="bar", value=Integer(value=1, start=get_start(line=1, col=1), end=get_end(line=1, col=2)))]
        ),
        start=get_start(line=1, col=1),
        end=get_end(line=1, col=2),
    )

# Generated at 2022-06-14 14:54:34.209789
# Unit test for function validate_with_positions
def test_validate_with_positions():         # pragma: no cover
    from typesystem.tokenize import Tokenizer
    from typesystem.types import String, Boolean

    tokenizer = Tokenizer()
    token = tokenizer.tokenize({"foo": "bar", "baz": True})

# Generated at 2022-06-14 14:54:41.970322
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize.parser import parse_string

    message: Message = validate_with_positions(
        token=parse_string("[{}]", [String()]), validator=[String()]
    ).messages[0]
    assert message.text == "The field 0 is required."
    assert message.code == "required"
    assert message.start_position.line == 1
    assert message.start_position.char_index == 1
    assert message.start_position.byte_index == 1
    assert message.start_position.column == 1
    assert message.end_position.line == 1
    assert message.end_position.char_index == 1
    assert message.end_position.byte_index == 1
    assert message.end_position.column == 1

# Generated at 2022-06-14 14:54:48.897234
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from typesystem.types import String

    text = """
    {
      "name": "Spam",
      "code": "spam",
      "description": "Spam is a delicacy in many cultures."
    }
    """

    class Item(Schema):
        name = String(max_length=5, required=True)
        code = String(max_length=5)
        description = String()

    token = Token.parse(text)
    try:
        validate_with_positions(token=token, validator=Item)
    except ValidationError as error:
        message = error.message("name")
        assert message.code == "max_length"
        assert message.text == 'Ensure this field has no more than 5 characters.'
        assert message.start_position.line == 2
        assert message.start_

# Generated at 2022-06-14 14:54:57.786352
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token, TokenType
    from typesystem import fields
    from typesystem.tokenize import tokenize_string

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=tokenize_string("", fields.String(max_length=2)),
            validator=fields.String(max_length=2),
        )
    assert exc_info.value.messages[0].start_position.line == 1
    assert exc_info.value.messages[0].start_position.char_index == 0
    assert exc_info.value.messages[0].end_position.line == 1
    assert exc_info.value.messages[0].end_position.char_index == 0
    assert exc_info.value.mess

# Generated at 2022-06-14 14:55:04.865062
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class TestSchema(Schema):
        a = int
        b = int

    schema = TestSchema()
    token = tokenize({"a": 1, "c": 3})

    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        assert messages[0].text == "The field 'b' is required."
        assert messages[0].start_position.char_index == 6
        assert messages[0].end_position.char_index == 6