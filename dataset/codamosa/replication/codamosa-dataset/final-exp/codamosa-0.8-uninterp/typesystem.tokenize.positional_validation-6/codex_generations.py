

# Generated at 2022-06-14 14:45:24.396095
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Array, Integer, String
    from typesystem.schemas import object_schema
    from typesystem.tokenize.tokens import Token

    schema = object_schema(
        {
            "foo": Integer(),
            "bar": Array(String(), max_length=2),
            "baz": Integer(),
        }
    )

    token = Token.from_dict(
        {
            "foo": "invalid",
            "baz": "missing",
        }
    )

    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        assert error.messages()[0].text == (
            "Value of field ``foo`` must be an integer."
        )

# Generated at 2022-06-14 14:45:31.017457
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(type="string")
    token = Token(
        value="",
        start=Position(line_number=1, char_index=1, byte_offset=0),
        end=Position(line_number=1, char_index=2, byte_offset=1),
    )
    assert validate_with_positions(token=token, validator=field) is None



# Generated at 2022-06-14 14:45:38.295130
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.tokenize import ast, to_token

    token = to_token(ast)
    with pytest.raises(ValidationError) as error:
        validate_with_positions(
            token=token, validator=Schema({"comparators": [Field()]}),
        )

# Generated at 2022-06-14 14:45:50.205740
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """Test the function validate_with_positions."""

    from typesystem.fields import Integer

    # First we define our type:
    class Person(Schema):
        age = Integer()
        name = Integer()

    # Now we want to validate the following JSON:
    input_ = {
        "age": "hi",
        "name": None,
    }

    # We then tokenize the data:
    from typesystem.tokenize.json import tokenize_json
    token = tokenize_json(input_)

    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        messages = error.messages()
        # The messages should contain the list below:


# Generated at 2022-06-14 14:45:58.053975
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import validators, fields, CompositeField
    from typesystem.tokenize.token_types import TokenType

    schema = fields.Object(properties={"foo": fields.Integer()})
    tokens = [
        Token(token_type=TokenType.object_start),
        Token(token_type=TokenType.key, value="foo"),
        Token(token_type=TokenType.colon),
        Token(token_type=TokenType.literal_string, value="bar"),
        Token(token_type=TokenType.object_end),
    ]

    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(token=tokens[0], validator=schema)

    assert len(error_info.value.messages()) == 1

# Generated at 2022-06-14 14:46:08.500573
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.schemas import Object, Integer


# Generated at 2022-06-14 14:46:09.750024
# Unit test for function validate_with_positions
def test_validate_with_positions():
    validate_with_positions(token=object(), validator=object())

# Generated at 2022-06-14 14:46:20.392979
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.types import ObjectToken
    from typesystem.tokenize.tokens import FieldToken
    from typesystem.fields import String
    from typesystem.schemas import Schema
    import typesystem

    class CommentSchema(Schema):
        text = String()

    schema = CommentSchema()

    class Comment(Schema):
        comment = typesystem.Object(schema=schema)

    comment = Comment()

# Generated at 2022-06-14 14:46:24.968452
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json

    from typesystem.tokenize.simple import json_tokenize

    comment_schema = Schema(
        {"comment": Field(type="string"), "read": Field(type="boolean")}
    )

    tokens = json_tokenize(json.dumps({"read": True, "comment": "foo"}))
    token = tokens[0]
    assert validate_with_positions(token=token, validator=comment_schema)

# Generated at 2022-06-14 14:46:35.992902
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import Tokenize
    from typesystem.base import Message as MessageType
    from typesystem.exceptions import ValidationError
    from typesystem.schemas import Schema
    from typesystem.types import String, Integer

    class DictSchema(Schema):
        foo = Integer()
        bar = String()

    class ListSchema(Schema):
        items = [Integer()]

    code = "a = 5\nb = 42\nc = 5"
    tokens = Tokenize(input=code, language="python").tokenize()
    schema = {"a": Integer(), "b": Integer(), "c": Integer()}
    error = validate_with_positions(token=tokens, validator=schema)
    assert isinstance(error, ValidationError)

# Generated at 2022-06-14 14:46:47.455021
# Unit test for function validate_with_positions
def test_validate_with_positions():
    "Test that validate_with_positions reports errors with correct positions."
    from typesystem.primitives import String

    content = """
    foo: bar
    bar: baz
    """

    from typesystem.tokenize.identifier import IdentifierTokenizer
    from typesystem.tokenize.map import MapTokenizer

    tokenizer = MapTokenizer(IdentifierTokenizer("foo"))
    tokenizer.tokenize(content)
    assert len(tokenizer.errors) == 1
    error = tokenizer.errors[0]
    assert error.text == "The field 'bar' is required."
    assert error.start_position.line == 2
    assert error.start_position.char_index == 4
    assert error.end_position.line == 2
    assert error.end_position.char_index == 7

# Generated at 2022-06-14 14:46:53.796191
# Unit test for function validate_with_positions
def test_validate_with_positions():
    list_field = Field(type=ListType(String()))
    token = Token.root([
        Token(start=2, end=5, value='key', name='key'),
        Token(start=6, end=9, value='val', name='val'),
        Token(start=10, end=22, value='[1, 2, 3]', name='other'),
    ])
    validate_with_positions(token=token, validator=list_field)

# Generated at 2022-06-14 14:47:04.578698
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class SimpleSchema(Schema):
        city = Field(type=str)
        number = Field(type=int)
        foo = Field(type=str)

    token = Token(
        "SimpleSchema",
        value={
            "city": "Brantford",
            "number": "foo",
        },
    )
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(
            token=token, validator=SimpleSchema
        )
    message = excinfo.value.messages[0]
    assert message.start_position.line_number == 1
    assert message.start_position.char_index == 17
    assert message.text == "The value is not a valid integer."
    assert message.code == "invalid_type"

# Generated at 2022-06-14 14:47:14.224607
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import Field, Text, Integer, Boolean
    from typesystem.tokenize.tokens import Token

    class Car(Schema):
        make = Text(max_length=8)
        year = Integer(gte=1900, lte=2100)
        is_electric = Boolean()

    token = Token.load(
        {
            "name": "Tesla",
            "year": 2016,
            "is_electric": True,
            "category": "sedan",
        },
        start_position=0,
        end_position=10,
    )
    validate_with_positions(token=token, validator=Car)


# Generated at 2022-06-14 14:47:25.886392
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.schemas import Object
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.positions import Position

    schema = Object(properties={"name": String(), "and": Integer()})

    token = Token(
        value={
            "name": "Hello",
            "and": 42,
        },
        start=Position(
            line_index=1, char_index=0, absolute_offset=0, line_text="{}"
        ),
        end=Position(
            line_index=1,
            char_index=7,
            absolute_offset=7,
            line_text="{'name': 'Hello', 'and': 42}",
        ),
    )


# Generated at 2022-06-14 14:47:33.498010
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class Person(Schema):
        name = Field(required=True)
        email = Field(required=True)

    token = tokenize({"name": "", "email": "joe@example.com"})

    try:
        validate_with_positions(token=token, validator=Person)
        raise Exception("An error should have been raised.")
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == 'The field "name" is required.'
        assert message.code == "required"
        assert message.start_position.line == 1
        assert message.start_position.char_index == 3
        assert message.end_position.line == 1
        assert message.end_position.char_index == 4

# Generated at 2022-06-14 14:47:44.146590
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import structures, types, validators

    # This is an example where you have to 'type ignore' in the implementation
    # because the field is a @property, and mypy doesn't treat this as a type
    # error
    assert isinstance(
        Message(text="foo").start_position,
        structures.CharacterPosition,
    )

    # This is our input document
    document = {"name": "Sam", "age": "27"}

    # This is our tokenized input document
    token = Token.from_python_value(document)

    # This is our test field
    field = Field(
        name="age",
        type=types.Integer,
        validators=[validators.Min(10)],
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_pos

# Generated at 2022-06-14 14:47:53.389882
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema({"name": Field(required=True)})
    token = Token(
        {"name": "Pep Guardiola"}, start=POSITION, end=POSITION, parent=None
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)

    error = exc_info.value
    assert len(error.messages()) == 1
    message = error.messages()[0]
    assert message.start_position == POSITION
    assert message.end_position == POSITION



# Generated at 2022-06-14 14:48:05.592703
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """
    It is possible to transform a tokenized message into a message with start and end indices.
    """
    from typesystem.schemas import RootSchema
    from typesystem.tokenize.tokens import Token

    class FooSchema(RootSchema):
        age = Field(type=int)

    tokenized_error = FooSchema().validate("{}")
    error = validate_with_positions(
        token=Token.from_jsondict("{}"), validator=FooSchema()
    )
    for t, p in zip(tokenized_error.messages(), error.messages()):
        assert t.text == p.text
        assert t.code == p.code
        assert t.index == p.index
        assert t.start_position is None

# Generated at 2022-06-14 14:48:17.780425
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.schemas import Schema as SchemaType
    from typesystem.schemas import Object
    from typesystem.tokenize.tokens import Token as TokenType

    class TestToken(TokenType):
        name = "TestToken"

        def lookup(self, path):
            return TestToken()

    class TestSchema(SchemaType):
        fields = {"foo": String()}


# Generated at 2022-06-14 14:48:34.674698
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """
    The function validate_with_positions uses message indexes to look up tokens
    in the token tree. If it doesn't find the token, it uses the first token.
    Since token.start and token.end are tuples,
    message.start_position and message.end_position need to be replaced
    by PositionalTokens.
    """

    from typesystem.tokenize.tokens import PositionalToken

    field = Field(required=True)
    token = Token(value=42, start=(0, 0), end=(0, 2))
    error = ValidationError(messages=[Message(text="The field 'name' is required.", index=["name"])])
    error.throw = lambda: None
    field.validate = lambda value: error.throw() # type: ignore


# Generated at 2022-06-14 14:48:46.645857
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import Tokenizer

    tokenizer = Tokenizer(
        {"value": "2", "name": "number"},
        {"value": "{"},
        {"value": "a"},
        {"value": "}"},
        {"value": "3", "name": "number"},
        {"value": "{"},
    )
    tokens = list(tokenizer)

    validate_with_positions(token=tokens[0], validator="number")
    validate_with_positions(token=tokens[4], validator="number")

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=tokens[2], validator="number")
    messages = excinfo.value.messages
    assert len(messages) == 1

# Generated at 2022-06-14 14:48:59.036798
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """
    # Test if a validation error is correctly rewritten to include positions.
    """
    from typesystem.tokenize import tokenize

    from tests.typesystem_test.tokenize.tokens import Object

    from . import person

    class PersonSchema(Schema):
        first_name = person.first_name
        last_name = person.last_name

    token = tokenize("{}").next()

# Generated at 2022-06-14 14:49:01.991430
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import fields

    class MySchema(Schema):
        field = fields.String(required=True)

    token = Token.build({"field": "value"})
    validate_with_positions(token=token, validator=MySchema)

# Generated at 2022-06-14 14:49:09.543150
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import tokenize
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem import validate

    class Person(Schema):
        name = String()

    token = tokenize({})
    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        _, positional_messages = validate(
            error.messages(), token.value
        )  # type: ignore

    assert len(positional_messages) == 1
    message = positional_messages[0]
    assert message.text == "The field 'name' is required."
    assert message.start_position.line_number == 1
    assert message.start_position.column_number == 1
    assert message.start_position

# Generated at 2022-06-14 14:49:21.641149
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from unittest.mock import Mock
    from typesystem.tokenize.tokenizer import Tokenizer
    from typesystem.tokenize.filters import Lowercase
    from typesystem.fields import Field, String

    tokenizer = Tokenizer(
        filters=[Lowercase()],
        position=(0, 0),
        text="WILD WILD",
    )
    token = tokenizer.next()
    token.lookup = Mock(return_value=token)

    field = Field(typ=String())
    result = validate_with_positions(token=token, validator=field)
    assert result == "wild wild"

    field = Field(typ=String(), required=True)
    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(token=token, validator=field)


# Generated at 2022-06-14 14:49:32.847288
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.json import parse_json

    schema = Schema(
        {
            "field_1": Field(type="integer"),
            "field_2": Field(type="string", required=True),
        }
    )
    
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(
            token=parse_json(text='{"field_1": "2"}'),
            validator=schema
        )
        
    messages = exc.value.messages()
    assert len(messages) == 1
    assert "{field_2}" in messages[0].text
    

# Generated at 2022-06-14 14:49:43.595257
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(type="string")
    class IssueChildren(Schema):
        title = field
    
    class Issue(Schema):
        title = field
        children = Field(type="array", items=IssueChildren)
        
    token = Token.read(
        {
            "title": "My Issue",
            "children": [
                {
                    "title": "Issue 1",
                },
                {},
                {
                    "title": "Issue 1",
                    "children": [
                        {},
                    ]
                }
            ]
        }
    )


# Generated at 2022-06-14 14:49:48.840919
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Integer, Array, Object

    class Person(Object):
        name = String(max_length=10)

    class PersonWithRequired(Object):
        name = String(required=True)

    # Should throw validation error without positions
    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(
            token=Token({"name": "Jørgen"}), validator=PersonWithRequired
        )

    # Should throw validation error with positions
    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(
            token=Token({"name": "Jørgen"}), validator=PersonWithRequired
        )
        message = error_info.value.messages[0]
        assert message.start_position.char_index

# Generated at 2022-06-14 14:49:59.976545
# Unit test for function validate_with_positions
def test_validate_with_positions():

    schema = {
        "type": "object",
        "properties": {
            "max": {"type": "string"},
            "members": {
                "type": "array",
                "items": {"$ref": "#/definitions/Member"},
            },
        },
        "definitions": {
            "Member": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "age": {"type": "integer"},
                    "married": {"type": "boolean"},
                },
                "additionalProperties": False,
                "required": ["name", "age", "married"],
            }
        },
        "additionalProperties": False,
        "required": ["max", "members"],
    }


# Generated at 2022-06-14 14:50:27.846114
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import pathlib
    import datetime
    import typesystem.fields as fields
    import typesystem.schemas as schemas

    class ChildSchema(schemas.Schema):
        name = fields.String()

    class TestSchema(schemas.Schema):
        child = fields.Nested(child_schema=ChildSchema())

    path = pathlib.Path(__file__).parent / "test.json"
    token = Token.parse(json.loads(path.read_text()))

    try:
        validate_with_positions(token=token, validator=TestSchema())
    except (ValidationError,) as error:
        assert error.messages()[0].start_position == (1, 2,)

# Generated at 2022-06-14 14:50:39.806130
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class MockField(Field):
        def validate(self, value, **kwargs):
            if value != 1:
                raise ValidationError([Message("not 1", code="not_1")])
            else:
                return value


# Generated at 2022-06-14 14:50:52.080275
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem

    class SlugField(typesystem.String):
        def validate(self, value):
            super().validate(value)
            if not value.isalnum():
                raise ValidationError("Slug must be alphanumeric.")

    class PostSchema(typesystem.Schema):
        slug = SlugField()
        title = typesystem.String()
        intro = typesystem.String(required=False)

    # test: object with invalid field
    token = Token.build({
        "slug": 'S01-keywords',
        "title": 'Python & TypeScript',
        "intro": 'A blog post about types.',
    })

    with pytest.raises(ValidationError) as info:
        validate_with_positions(token=token, validator=PostSchema)

# Generated at 2022-06-14 14:51:03.253466
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize.json_schema import tokenize_json_schema
    from typesystem.tokenize import Token

    schema = {"type": "object", "properties": {"name": {"type": "string"}}}
    token = tokenize_json_schema(schema)
    assert isinstance(token, Token)

    field = String(required=True)
    with pytest.raises(ValidationError) as e:
        validate_with_positions(token=token, validator=field)
    assert e.value.messages[0].start_position.char_index == 0
    assert e.value.messages[0].end_position.char_index == 1

    data = {"name": ""}
    token = tokenize_json_schema(data)

# Generated at 2022-06-14 14:51:15.352674
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from typesystem.schemas import Schema
    from typesystem.fields import Integer

    class PersonSchema(Schema):
        age = Integer(title="Age", required=True)

    schema = PersonSchema()

    from typesystem.tokenize.tokens import ObjectToken, StringToken

    data = {"name": "Joe"}
    token = ObjectToken(value=data, name="Person", start=0, end=0)
    try:
        schema.validate(token)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        message = messages[0]
        assert message.index == ("age",)
        assert message.start_position == 0
        assert message.end_position == 0
        assert message.text == "The field 'age' is required."

# Generated at 2022-06-14 14:51:26.517355
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.test_tokenize import tokenize
    Field = typesystem.Field

    schema = typesystem.Schema(properties={"name": Field(type="string")})
    tokens = tokenize({"name": None})
    token = tokens[0]
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "The field 'name' is required."
        assert message.start_position.line_number == 0
        assert message.start_position.char_index == 2
        assert message.end_position.line_number == 0
        assert message.end_position.char_index == 6

# Generated at 2022-06-14 14:51:36.748552
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Array, Boolean, Integer, Text
    from typesystem.tokenize.parse import parse
    from typesystem.tokenize.scanner import Scanner
    from typesystem.utils import PositionalMarkup
    from typesystem.tokenize.position import PositionalToken
    from typesystem.exceptions import ValidationError
    import datetime
    import json
    with open("tests/fixtures/test_tokenize_positions.json") as f:
        test_data = json.load(f)
    for test in test_data:
        string = test["string"]
        tokens = list(Scanner(string))
        markup = PositionalMarkup(string)

# Generated at 2022-06-14 14:51:48.016409
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import ObjectToken
    from typesystem.tokenize.tokens import ArrayToken
    from typesystem.tokenize.tokens import StringToken
    from typesystem.fields import String

    class User(Schema):
        email = String(required=True)

    user = {
        "email": "hello@example.com",
        "emai": "hello@example.com",
    }
    token = ObjectToken(
        {"email": StringToken("hello@example.com"), "emai": StringToken("hello@example.com")},
        start={"line": 1, "char": 1},
        end={"line": 1, "char": 35},
    )

# Generated at 2022-06-14 14:51:58.698219
# Unit test for function validate_with_positions
def test_validate_with_positions():
    @dataclass
    class Person(Schema):
        name: str

    @dataclass
    class Book(Schema):
        author: Person
        title: str

    # Tokenize a document
    data = {
        "author": {"name": 1},
        "title": 1,
    }
    tokens = Token.locate_tokens(data, "_")

    # Validate document
    error: ValidationError
    try:
        validate_with_positions(token=tokens, validator=Book)
    except ValidationError as error:
        pass

    # Ensure all error messages are positional
    assert isinstance(error.messages[0], Message)
    assert isinstance(error.messages[1], Message)

    # Ensure error messages are correct

# Generated at 2022-06-14 14:52:05.188162
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import sys
    from typesystem.json_schema import JSONSchemaField
    from typesystem.tokenize import tokenize_file

    def validate():
        with open(__file__, "r") as f:
            tokens = tokenize_file(
                f,
                field_types={
                    "code": JSONSchemaField({"type": "string", "minLength": 1}),
                    "keywords": JSONSchemaField({"type": "array", "items": {"type": "string"}}),
                },
            )
            return validate_with_positions(token=tokens, validator=tokens.validator)


# Generated at 2022-06-14 14:52:49.160143
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    raw = {"foo": {"bar": "baz"}}
    root_token = tokenize(raw)

    class Foo(Schema):
        bar = Field(type="string")

    bar_token = root_token.lookup("foo", "bar")

    assert validate_with_positions(token=bar_token, validator=Foo) == {"bar": "baz"}

    class Foo(Schema):
        bar = Field(type="integer")

    bar_token = root_token.lookup("foo", "bar")


# Generated at 2022-06-14 14:52:59.710724
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.base import Message
    from typesystem.exceptions import ValidationError
    from typesystem.fields import Field
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.tokens import Offset

    class MySchema(Schema):
        foo = Field(required=True)

    token = Token(
        value={"foo": {"bar": ""}},
        start=Offset(line=1, column=2, char_index=3),
        end=Offset(line=1, column=9, char_index=10),
    )
    try:
        validate_with_positions(token=token, validator=MySchema)
    except ValidationError as error:
        message = error.messages()[0]
       

# Generated at 2022-06-14 14:53:10.166154
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token 
    import pytest
    class Boolean(Field):
        def validate_logic(self, value):
            if value not in ("true", "false"):
                return False
            return True
    
    class Person(Schema):
        name = Field()
        age = Field(type=Integer)
        retired = Boolean()
    
    json_str = """{
        "name": "",
        "age": "20",
        "retired": "maybe"
    }"""
    token = Token.parse(json_str)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Person)

# Generated at 2022-06-14 14:53:21.845788
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse_token

    class Comment(Schema):
        name = Field(type=str)
        email = Field(type=str)
        message = Field(type=str)

    token = parse_token("")

    try:
        validate_with_positions(token=token, validator=Comment)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 3
        assert messages[0].code == "required"
        assert messages[0].index == ("name",)
        assert messages[0].start_position.line == 1
        assert messages[0].start_position.column == 0
        assert messages[0].start_position.char_index == 0
        assert messages[0].end_position.line == 1

# Generated at 2022-06-14 14:53:33.194350
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.types import String
    from typesystem.tokenize.lexers import JSONLexer
    from typesystem.tokenize.tokens import TokenType

    lexer = JSONLexer()
    root_token = lexer.tokenize('{"name": "bob"}')

    try:
        validate_with_positions(token=root_token, validator=String(required=True))
    except ValidationError as error:
        assert error.messages() == [
            Message(
                start_position=Position(row=1, column=1, char_index=0),
                end_position=Position(row=1, column=2, char_index=1),
                text="The field 'name' is required.",
                code="required",
                index=["name"],
            )
        ]

# Generated at 2022-06-14 14:53:41.872519
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import (
        ArrayToken,
        DictionaryToken,
        IntToken,
        StringToken,
    )


# Generated at 2022-06-14 14:53:52.422558
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import String

    schema = String(format="email")
    token0 = Token(value="foo", start=(1, 1), end=(1, 4))
    token1 = Token(value="bar", start=(2, 1), end=(2, 3), parent=token0)
    token2 = Token(value=["foo", "bar"], start=(1, 1), end=(2, 3), parent=token1)

    # Test that ValidationError has correct positioning information
    with pytest.raises(ValidationError) as exception_info:
        validate_with_positions(token=token2, validator=schema)


# Generated at 2022-06-14 14:54:03.237754
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import parse_type, TypesystemError

    def validate_with_positions_wrapper(
        *, token, validator: typing.Union[Field, typing.Type[Schema]]
    ):
        if isinstance(validator, str):
            validator = parse_type(validator)
        try:
            return validate_with_positions(token=token, validator=validator)
        except TypesystemError as e:
            return e.messages

    from typesystem.tokenize import tokenize, Token


# Generated at 2022-06-14 14:54:09.619941
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.string import String

    class Test(Schema):
        foo = String(required=True)

    document = """
    {
        "foo": "bar"
    }
    """

    try:
        validate_with_positions(
            token=Token.parse(document), validator=Test
        )
    except ValidationError:
        pass
    else:
        assert Fa

# Generated at 2022-06-14 14:54:18.122735
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.tokens import Object
    from tests.fields import StringField

    content = """{
        "foo": "hello",
        "bar": "world"
    }"""
    token = tokenize(content)
    assert isinstance(token, Object)

    validate_with_positions(token=token, validator=StringField())

    content = """{
        "foo": "hello",
        "bar": "world",
        "qux": 1
    }"""
    token = tokenize(content)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=StringField())
    text = str(exc_info.value)