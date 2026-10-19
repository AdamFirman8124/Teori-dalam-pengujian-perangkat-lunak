

# Generated at 2022-06-14 14:45:19.020985
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class ExampleField(Field):
        def validate(self, value):
            raise ValidationError(value=value, messages=["Something wrong!"])

    # We do not have start_position or end_position, so just the error message is
    # the same
    token = Token(value="5", path=[1], start=None, end=None)
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=ExampleField())
    assert len(exc.value.messages) == 1
    assert exc.value.messages[0].code == "error"
    assert exc.value.messages[0].index == token.path
    assert exc.value.messages[0].text == "Something wrong!"

# Generated at 2022-06-14 14:45:28.497404
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import JSONSchema

    schema = JSONSchema(
        {
            "type": "object",
            "properties": {
                "firstName": {"type": "string"},
                "lastName": {"type": "string", "required": True},
                "age": {"type": "integer", "minimum": 0, "maximum": 110},
            },
        }
    )
    document = """
    {
      "firstName": "John",
      "age": 23
    }
    """

# Generated at 2022-06-14 14:45:36.695529
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer, String
    from typesystem.schemas import (
        List,
        MetaSchema,
        Object,
        Reference,
        Root,
    )
    import typesystem.tokenize.tokens
    from typesystem.tokenize.tokens import (
        ArrayToken,
        FieldToken,
        IntegerToken,
        ObjectToken,
        StringToken,
        ValueToken,
    )

    class Position(typesystem.tokenize.tokens.Position):
        def __init__(self, *, char_index: int):
            super().__init__(char_index=char_index)


# Generated at 2022-06-14 14:45:45.396062
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    from json.decoder import JSONDecodeError
    from typesystem.validators import String

    try:
        validate_with_positions(
            token=Token(value=json.loads('{"s": 123}')), validator=String()
        )
    except JSONDecodeError as error:
        assert error.args[0] == "Expecting property name enclosed in double quotes"
    except ValidationError as error:
        assert error.args[0] == [
            "Expecting property name enclosed in double quotes: line 1 column 3 (char 2)"
        ]

# Generated at 2022-06-14 14:45:54.726566
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token
    from typesystem.types import String

    class Person(Schema):
        name = String(required=True)

    token = Token(
        value={},
        start={"line_number": 1, "char_index": 1},
        end={"line_number": 2, "char_index": 2},
    )
    try:
        validate_with_positions(token=token, validator=Person)
        assert False
    except ValidationError as error:
        assert [m.text for m in error.messages()] == ["The field 'name' is required."]
        assert [m.code for m in error.messages()] == ["required"]

# Generated at 2022-06-14 14:46:04.789630
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize.parser import parse

    field = String(min_length=5)

    # Valid data
    data = '{"foo": "bar"}'
    token = parse(data)
    validate_with_positions(token=token, validator=field)
    # Test that a valid value is returned.
    assert validate_with_positions(token=token, validator=field) == data

    # Invalid data, without a required field
    data = '{}'
    token = parse(data)
    # Test that a ValidationError is raised.
    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=field)

    # Invalid data, with a non-string field
    data = '{"foo": 1}'

# Generated at 2022-06-14 14:46:15.527532
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer, String
    from typesystem.schemas import Schema
    from typesystem.tokenize.scanner import scan
    from typesystem.tokenize.tokens import Token

    scanner = scan(
        """{
            "foo": "bar",
            "x": "abc",
            "y": 4
        }"""
    )
    token = Token.from_scanner(scanner)

    class MySchema(Schema):
        foo = String()
        x = Integer()
        y = Integer()

    validate_with_positions(token=token, validator=MySchema)

    scanner = scan(
        """{
            "foo": "bar",
            "x": 2,
            "y": "abc"
        }"""
    )
    token = Token.from_scan

# Generated at 2022-06-14 14:46:24.423018
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.base import TokenizeField
    from typesystem.tokenize.utils import raw_tokenize
    from typesystem.structures import Dict, List, String

    validator = Dict({"items": List(String())})
    token = raw_tokenize(
        validator,
        """
        {
            "items": [
                "foo",
                "bar",
                "baz",
            ]
        }
        """,
    )

    validate_with_positions(token=token, validator=validator)


# Generated at 2022-06-14 14:46:33.025758
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import lex, parse
    from typesystem.tokenize import Tokens

    text = '<Person name="Oscar" age="18">'
    tokens = lex(text)
    program = parse(tokens)
    assert isinstance(program, Tokens)
    person = program.lookup(["Person"])
    assert isinstance(person, Token)

    from typesystem.fields import String
    from typesystem.schemas import Schema

    class Person(Schema):
        name = String(required=True)
        age = String()

    validate_with_positions(token=person, validator=Person)

# Generated at 2022-06-14 14:46:43.160206
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from json import loads
    from typesystem import String, Integer, Boolean
    from typesystem.schemas import Dictionary, Array

    class Person(Schema):
        name = String()
        age = Integer(minimum=0, maximum=120)

    class Person2(Person):
        name = String(min_length=1)
        age = Integer(minimum=0, maximum=120)

    class Pet(Schema):
        name = String()
        age = Integer(minimum=1, maximum=30)

    class Dog(Pet):
        is_good_boy = Boolean()

    class Cat(Pet):
        mood = String(choice=["hungry", "happy", "angry"])

    class House(Schema):
        residents = Array(items=Person())
        pets = Array(items=Array(items=Pet()))


# Generated at 2022-06-14 14:46:56.087384
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize_json

    # Given an instance of a ComplexField and a complex dictionary
    class PersonSchema(Schema):
        name = Field(type="string")
        age = Field(type="integer")

    person = {"name": "Foo", "age": "bar"}

    # When the validator is validated
    tokens = tokenize_json(person)
    try:
        validate_with_positions(token=tokens, validator=PersonSchema)
    except ValidationError as error:
        # Then a validation error should be raised
        assert error
        # And the text should contain the field name and type
        assert "name" in error.texts()
        assert "Foo" in error.texts()
        assert "bar" in error.texts()

# Generated at 2022-06-14 14:47:04.237053
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer
    from typesystem.tokenize.parse import parse
    from typesystem.tokenize.tokens import RootToken

    validator = Integer()
    token = RootToken(parse(b'{"x": 0}'))

    try:
        validate_with_positions(token=token, validator=validator)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "Invalid 'Integer' type."
        assert message.start_position.char_index == 7
        assert message.end_position.char_index == 8



# Generated at 2022-06-14 14:47:13.978916
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem import defines
    from typesystem.fields import Integer, String
    from typesystem.schemas import Schema

    class User(Schema):
        name = String()
        age = Integer(minimum=18, maximum=65)

    data = '{"name": "Jane", "age": 13}'
    token = Token.parse(data)

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=User())
        assert [m.code for m in error.value.messages()] == [
            defines.TOO_LOW,
            defines.TOO_MANY,
        ]

# Generated at 2022-06-14 14:47:25.787149
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.positions import CharIndex

    Field(
        __schema__={"properties": {"prop": {"type": "integer"}}},
        required=["prop"],
        __token__=Token(
            "valid",
            {
                "prop": 1,  # valid integer
                # the field `test` is invalid because it is not required
                "test": "Some Text",
            },
            start=CharIndex(line_index=1, char_index=1),
            end=CharIndex(line_index=1, char_index=2),
        ),
    )

# Generated at 2022-06-14 14:47:36.189168
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # given
    token = Token(
        value={
            "foo": [
                {"bar": None},
                {
                    "bar": {"baz": None},
                    "bar1": "bar1",
                    "bar2": "bar2",
                },
                {},
            ],
            "field_required": "",
            "list_required": [],
        },
        start=Token.Position(line=1, char_index=0),
        end=Token.Position(line=1, char_index=999),
    )

    # when

# Generated at 2022-06-14 14:47:36.767562
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:47:43.706704
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class Person(Schema):
        name = Field(required=True)

    tokens = tokenize("{name: ''}")
    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(token=tokens.root, validator=Person)
    assert error_info.value.messages[0].start_position == tokens["name"].start
    assert error_info.value.messages[0].end_position == tokens["name"].end

# Generated at 2022-06-14 14:47:55.037683
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Integer, Array
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import Token

    class Person(Schema):
        name = String(min_length=2)
        age = Integer(minimum=0)

    class Address(Schema):
        city = String()
        street = String()
        zip_code = String()

    class Company(Schema):
        name = String()
        CEO = Person()
        employees = Array(items=Person())
        offices = Array(items=Address())


# Generated at 2022-06-14 14:48:06.333739
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokenize

    string = r"""{"foo": {"bar":"baz"}}"""

    expected_message = Message(
        text="The field 'bar' is required.",
        code="required",
        index=["foo"],
        start_position=lambda: None,
        end_position=lambda: None,
    )

    class MySchema(Schema):
        foo = {"bar": str}

    token = tokenize(string)
    try:
        validate_with_positions(token=token, validator=MySchema)
    except ValidationError as error:
        message = error.messages()[0]
        assert message == expected_message



# Generated at 2022-06-14 14:48:15.540159
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Array, Integer
    from typesystem.tokenize.tokens import TokenTree

    schema = Array([Integer(), String()])

    # Valid token
    token = TokenTree(["0", "1", "foo"])
    value = validate_with_positions(token=token, validator=schema)
    assert value == [0, "foo"]

    with pytest.raises(ValidationError):
        # Invalid token
        token = TokenTree(["0", "1", "foo", "2"])
        validate_with_positions(token=token, validator=schema)

# Generated at 2022-06-14 14:48:29.323075
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class TestValidator(Schema):
        string = Field(type="string")
        number = Field(type="number")

    token = Token(
        {
            "string": "abc",
            "number": 123,
            "extra_key": "extra",
        },
        start={"line": 1, "column": 1, "char_index": 1},
        end={"line": 1, "column": 100, "char_index": 100},
    )

    validate_with_positions(token=token, validator=TestValidator)


# Generated at 2022-06-14 14:48:39.039725
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    from typesystem.tokenize.tokenize import tokenize
    from typesystem.tokenize.tokens import ObjectToken

    class TestSchema(typesystem.Schema):
        foo = typesystem.String()

    token = tokenize({"foo": "bar"})
    assert token.is_anonymous

    validate_with_positions(token=token, validator=TestSchema)

    # Should NOT raise ValidationError
    token = tokenize({"foo": "bar"})
    assert token.is_anonymous
    assert isinstance(token, ObjectToken)
    assert token.lookup(["foo"]).is_anonymous is False



# Generated at 2022-06-14 14:48:47.572688
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import types, Structure
    from typesystem.tokenize.tokenizer import tokenize

    schema = Structure(
        {
            "first_name": types.String(required=True),
            "last_name": types.String,
            "age": types.Integer,
            "friends": types.Array(types.String),
        }
    )

    text = '{"first_name": "John"}'
    node = tokenize(text)
    assert validate_with_positions(token=node, validator=schema) == {
        "first_name": "John"
    }

    text = '{"friends": ["John", 2]}'
    node = tokenize(text)

# Generated at 2022-06-14 14:48:59.717570
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    # Invalid usage
    with pytest.raises(TypeError):
        field = String()
        token = Token(value=dict())
        validate_with_positions(token=token, validator=field)

    # Invalid values
    token = Token(value=dict())
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=Data)
    assert excinfo.value.messages() == [
        Message(
            index=(),
            code="invalid-type",
            text="Expected type 'object'",
            start_position=value_token.start,
            end_position=value_token.end,
        )
    ]

    value_token = Token(value=dict())

# Generated at 2022-06-14 14:49:06.053715
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.base import BaseTokenizer
    from typesystem.tokenize.positions import Position, PositionMode

    class Tokenizer(BaseTokenizer):
        def tokenize(self, value: typing.Any) -> typing.Iterator[Token]:
            yield Token(position=Position(0, 0, PositionMode.LINE_COLUMN))

    schema = Schema(fields=[Field(type="string")])

    try:
        validate_with_positions(
            token=next(Tokenizer().tokenize("foo")), validator=schema
        )
    except ValidationError as error:
        assert error
    else:
        assert False

# Generated at 2022-06-14 14:49:17.776950
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object

    class Person(Object):
        fields = {"name": "string"}

    class PersonMessage(Message):
        def text(self):
            return f"{self.index[-1]} is required"

    class PersonError(ValidationError):
        message_cls = PersonMessage

    class PersonField(Field):
        validators = [PersonError]

    class PersonSchema(Schema):
        fields = {"person": PersonField}

    schema = PersonSchema()
    data = {"person": {"name": "Bob"}}
    schema.validate(data)

    with pytest.raises(ValidationError) as exc_info:
        data = {"person": {}}
        schema.validate(data)
    message = exc_info.value.messages[0]

# Generated at 2022-06-14 14:49:29.926783
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.language_en import (
        TokenizeEnglish,
    )  # noqa: E402  # flake8 issue in test
    from typesystem.types import String  # noqa: E402  # flake8 issue in test
    from typesystem.tokenize.tokens import Token  # noqa: E402  # flake8 issue in test

    tokenizer = TokenizeEnglish()
    language_token = tokenizer.tokenize("I am going to the bar.")[0]
    validation_token = Token(value=language_token)
    field = String(max_length=10)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=validation_token, validator=field)

# Generated at 2022-06-14 14:49:41.305687
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.test_utils import sample_schema
    from typesystem.tokenize import parse

    schema = sample_schema()


# Generated at 2022-06-14 14:49:49.833909
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.validators import IntegerField, Message, Position, Schema

    class TestSchema(Schema):
        integer = IntegerField(required=True)

    data = {
        "integer": "foo",
        "properties": {
            "integer": {"type": "integer"},
            "properties": {
                "type": {"type": "string", "enum": ["object"]},
                "properties": {
                    "type": {"type": "string", "enum": ["string"]}
                },
                "required": {"type": "array", "items": {"type": "string"}},
            },
            "required": {"type": "array", "items": {"type": "string"}},
        },
    }

# Generated at 2022-06-14 14:49:57.572681
# Unit test for function validate_with_positions
def test_validate_with_positions():

    import typesystem

    class Person(typesystem.Schema):
        name = typesystem.String(max_length=10)

    import json
    from typesystem.tokenize import tokenize

    token = tokenize({"name": "John Doe"})

    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        for message in error.messages:
            assert message.start_position is not None
            assert message.end_position is not None

# Generated at 2022-06-14 14:50:15.151588
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer, Array
    from typesystem.schemas import Schema, Structure

    class PersonSchema(Structure):
        name = String()
        age = Integer()

    class PeopleSchema(Schema):
        people = Array(of=PersonSchema())

    from typesystem.tokenize import from_json

    token = from_json(
        """
        {
            "people": [
                {
                    "name": "Matt",
                    "age": 24
                },
                {
                    "name": "Mike",
                    "age": 42
                }
            ]
        }
        """
    )
    people = validate_with_positions(token=token, validator=PeopleSchema())

# Generated at 2022-06-14 14:50:26.108810
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import tokenize_str, tokenize_node
    from typesystem.tokenize.tokens import Token

    schema = Schema(fields=[Field(name="foo", required=True)])

    # token.lookup() works with both tokenize_node() and tokenize_str()
    tokens = tokenize_str(
        schema,
        """
        {
            "foo": "bar",
            "baz": 42
        }
        """,
    )
    assert isinstance(tokens, Token)
    example_token = tokens.prev
    assert isinstance(example_token, Token)
    assert example_token.value == {"foo": "bar", "baz": 42}
    assert example_token.lookup(["foo"]).value == "bar"
    assert example_token

# Generated at 2022-06-14 14:50:33.222611
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class Item(Schema):
        name = Field(max_length=100)

    schema = Schema(
        {"items": Field(array_type=Item), "total": Field(integer=True)}
    )

    token = tokenize(
        """
    {
        "items": [
            {
                "name": "foo"
            },
            {
                "name": ""
            },
            {
                "name": "bar"
            }
        ],
        "total": "not a number"
    }
    """.strip()
    )

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=schema)

    messages = excinfo.value.messages()


# Generated at 2022-06-14 14:50:43.116433
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typing import List, Tuple, Optional
    from markdown_it.token import Token
    from pathlib import Path
    import typesystem
    from typesystem.fields import Integer

    def generate_validate_with_positions(path: Path) -> None:
        with open(path, "r") as f:
            content = f.read()
        tokens = typesystem.tokenize(content)
        assert isinstance(tokens, list)
        for token in tokens:
            validate_with_positions(token=token, validator=Integer())

    def generate_validate_with_positions_invalid(path: Path) -> None:
        with open(path, "r") as f:
            content = f.read()
        tokens = typesystem.tokenize(content)

# Generated at 2022-06-14 14:50:49.047226
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class Person(Schema):
        name = Field(required=True, type='string')

    doc = '{"name": "foo"}'
    token = tokenize(doc)
    person = validate_with_positions(token=token, validator=Person)
    assert person == {"name": "foo"}

    doc = '{"age": "foo"}'
    token = tokenize(doc)
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=Person)

    assert exc.value.messages[0].code == 'required'
    assert (
        exc.value.messages[0].text
        == "The field 'name' is required at 'root[name]'."
    )
    assert exc.value

# Generated at 2022-06-14 14:50:56.653528
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    token = tokenize(
        {
            "foo": "bar",
            "baz": 123,
        }
    )

# Generated at 2022-06-14 14:51:06.066722
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import os
    import sys
    import tempfile
    import unittest
    import json

    from typesystem.tokenize import tokenize_file

    # The code below is a copy of examples/schema.py from the typesystem repository.
    from typesystem import fields, schemas

    # A schema to validate a JSON file that looks like:
    #
    # {
    #     "authors": [
    #         {
    #             "first_name": "Bob",
    #             "last_name": "Al-Amri"
    #         },
    #         {
    #             "first_name": "John",
    #             "last_name": "Smith"
    #         }
    #     ]
    # }

# Generated at 2022-06-14 14:51:15.396196
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(start=Position(0, 1, 2), end=Position(5, 6, 7))
    token.value = None

    try:
        validate_with_positions(token=token, validator=Field(type=str))
    except ValidationError as error:
        assert error.messages()[0].code == "required"
        assert error.messages()[0].start_position.line == 1
        assert error.messages()[0].start_position.column == 2
        assert error.messages()[0].end_position.line == 6
        assert error.messages()[0].end_position.column == 7



# Generated at 2022-06-14 14:51:22.169083
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem.tokenize.base as tokenize

    from typesystem.fields import Integer

    field = Integer()

    schema_token = tokenize.tokenize_json(
        {"name": "test", "type": "object", "properties": {"test": {"type": "integer"}}}
    )

    token = schema_token.value.properties["test"]

    validate_with_positions(token=token, validator=field)

# Generated at 2022-06-14 14:51:31.209684
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from  typesystem.types import String

# Generated at 2022-06-14 14:51:49.427402
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parse import parse_source
    from typesystem.tokenize.tokens import Object
    from typesystem.schemas import Schema
    from typesystem import fields
    import typesystem
    class PersonSchema(Schema):
        title = fields.String(required=True)
        age = fields.Integer()

    source = "{'title': 'Mr', 'age': 'coconut', 'balance': '10.00'}"
    token = parse_source(source)

    # Make sure that it raises an error with positions set
    with pytest.raises(typesystem.ValidationError) as excinfo:
        validate_with_positions(token=token, validator=PersonSchema)

    assert isinstance(
        excinfo.value.messages[1].token, Object
    )

# Generated at 2022-06-14 14:51:59.769483
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema

    class CustomSchema(Schema):
        a = Field(type=str)
        b = Field(type=int, required=False)
        c = Field(type=int)

    def custom_validate(data):
        if data["b"] > data["c"]:
            raise ValidationError(
                messages=[
                    Message(text="b should be less than c", code="b-is-greater-than-c")
                ]
            )

    CustomSchema.validate = custom_validate

    def get_messages(token, validator):
        errors = []
        try:
            validate_with_positions(token=token, validator=validator)
        except ValidationError as e:
            errors = e.messages()
        return errors

   

# Generated at 2022-06-14 14:52:11.812824
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String
    from typesystem.tokenize.positions import Position

    field = String(min_length=1)
    token = Token(value="a", start=Position(line=1, char_index=0))
    assert validate_with_positions(token=token, validator=field) == "a"

    token = Token(value="", start=Position(line=1, char_index=0))
    try:
        validate_with_positions(token=token, validator=field)
        assert False, "Expected ValidationError"
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "Enter a value."
        assert message.start_position == Position(line=1, char_index=0)

# Generated at 2022-06-14 14:52:21.033442
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # type: () -> None
    token = Token(
        value={
            "foo": "bar",
            "baz": [
                {"foo": "bar"},
                {"foo": "baz"},
                {"foo": 3},
                {"foo": "bar"},
            ],
        },
        start=Position(line_index=1, char_index=1),
        end=Position(line_index=7, char_index=1),
    )
    schema = Schema(
        fields={"foo": "string", "baz": [Schema(fields={"foo": "string"})]}
    )
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError:
        assert True
    else:
        assert False

# Generated at 2022-06-14 14:52:28.955493
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.schemas import Object

    class MySchema(Schema):
        name = String()

    token = Token(
        type="object",
        key="name",
        value=None,
        start={"line_no": 1, "char_index": 0},
        end={"line_no": 3, "char_index": 1},
    )

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=MySchema())
    assert exc.value.format_messages() == [
        'Line 1, character 0: The field "name" is required.'
    ]

# Generated at 2022-06-14 14:52:37.037299
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    from typesystem.tokenize import tokenize

    schema = typesystem.Schema(
        fields={"#nested": typesystem.Schema(fields={"name": typesystem.String()})}
    )
    try:
        validate_with_positions(token=tokenize({"#nested": {}}), validator=schema)
    except ValueError as error:
        message = error.args[0]
        assert message == "The field 'name' is required."
    else:
        assert False, "Should not get here"

# Generated at 2022-06-14 14:52:45.782484
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class UserSchema(Schema):
        type: Field[str]
        username: Field[str]

    token = Token(type_="object", value={"type": "user", "username": "bob"})

    try:
        validate_with_positions(token=token, validator=UserSchema)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text='The field "username" is required.',
                code="required",
                index=["username"],
                start_position=Position(line=0, char_index=1),
                end_position=Position(line=0, char_index=1),
            )
        ]

# Generated at 2022-06-14 14:52:56.948963
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Integer
    from typesystem.tokenize import tokenize

    token = tokenize("42")

    assert validate_with_positions(token=token, validator=Integer()) == 42

    import pytest

    try:
        validate_with_positions(token=token, validator=Integer(min_value=50))
    except ValidationError as error:
        for message in error.messages():
            assert message.text == "Must be greater than or equal to 50."
            assert message.start_position.line_index == 1
            assert message.start_position.char_index == 0
            assert message.end_position.line_index == 1
            assert message.end_position.char_index == 1
        return
    pytest.fail("Should not reach this point.")



# Generated at 2022-06-14 14:53:05.267686
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import io
    import json
    from typesystem.schemas import Schema
    from typesystem.fields import String, Number
    from typesystem.tokenize.impl import tokenize
    from typesystem.tokenize.tokens import Token

    class MySchema(Schema):
        name = String(required=True)
        id = Number(required=True)

    s = MySchema()
    with io.StringIO('{"name": "foo", "id": "123"}') as f:
        tokens = tokenize(f)
        token = Token(tokens[0])
        try:
            validate_with_positions(token=token, validator=s)
        except ValidationError as e:
            messages = e.messages()
            assert len(messages) == 1
            message = messages[0]


# Generated at 2022-06-14 14:53:14.665002
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class TestSchema(Schema):
        field1 = Field(type="string", required=True)
        field2 = Field(type="integer")

    class TestSchema2(Schema):
        field3 = Field(type="string", required=True)
        field4 = Field(type="integer")

    class TestSchema3(Schema):
        field5 = Field(type="string", required=True)
        field6 = Field(type="integer")

    class TestSchema4(Schema):
        field7 = Field(type="string", required=True)
        field8 = Field(type="integer")


# Generated at 2022-06-14 14:53:39.127853
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Array, Object, String
    from typesystem.tokenize.lexer import lex

    schema = Object({"foo": Array(String())})
    tokens = lex(
        "foo: [1, 2, [3]]",
        start="document",
        pos_info=True,
        partial=True,
        end_on_terminator=True,
    )
    token = Token.build(tokens, child_validator=validate_with_positions)

# Generated at 2022-06-14 14:53:50.278081
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token, Tokenizer
    from typesystem.schemas import Schema
    from typesystem.fields import StringField, ArrayField, ObjectField

    class TestSchema(Schema):
        name = StringField(required=True)
        values = ArrayField(items=StringField(required=True))

    tokenizer = Tokenizer(
        {
            "name": "Rasmus",
            "values": ["foo", "bar", "baz"],
            "tags": ["spam", 1],
        }
    )
    token = tokenizer.parse()
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=TestSchema)

# Generated at 2022-06-14 14:54:01.575411
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object

    from .utils import create_token_tree

    token_tree = create_token_tree(
        {
            "object1": {},
            "object2": {"other_field": "other_value"},
            "field_1": "value_1",
            "field_2": [
                {"object3": {"field_3": "value_3"}},
                {
                    "object4": {
                        "other_field": "other_value",
                        "field_4": "value_4",
                    }
                },
            ],
            "field_5": "value_5",
        }
    )

    schema = Object(properties={"object4": Object(required=["field_4"])})

    with pytest.raises(ValidationError):
        validate_with

# Generated at 2022-06-14 14:54:11.044075
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.tokenize.tokenize import tokenize

    class MySchema(Schema):
        name = String(blank=True)

    text = '{"name": ""}'
    token = tokenize(text)

    try:
        validate_with_positions(token=token, validator=MySchema)
    except ValidationError as error:
        message = error.messages()[0]
        position = message.start_position
        assert position.line == 1
        assert position.column == 3
        assert position.char_index == 2



# Generated at 2022-06-14 14:54:22.855377
# Unit test for function validate_with_positions

# Generated at 2022-06-14 14:54:33.255408
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class TestField(Field):

        def validate(self, value):
            try:
                return int(value)
            except ValueError as error:
                raise ValidationError([Message(text=str(error))])

    field = TestField()
    token = tokenize(source="'foo'", requires_position=True)
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=field)

    message = excinfo.value.messages()[0]
    assert (
        message.text
        == "invalid literal for int() with base 10: 'foo'"
    )
    assert message.start_position.line_index == 0
    assert message.start_position.line_number == 1
    assert message

# Generated at 2022-06-14 14:54:41.291747
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from .base import tokenize
    from .fields import Text

    schema = Schema({"name": Text()})
    errors = schema.validate({}, raise_exception=False)
    assert errors[0].code == "required"
    assert errors[0].start_position == (1, 0)
    assert errors[0].end_position == (1, 0)
    assert errors[0].text == "The field 'name' is required."

    errors = schema.validate({"name": 1}, raise_exception=False)
    assert errors[0].index == ("name",)
    assert errors[0].start_position == (1, 7)
    assert errors[0].end_position == (1, 8)
    assert errors[0].text == "Expected string for value 1."


# Generated at 2022-06-14 14:54:52.023323
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.schemas import Structure, String

    class MusicAlbum(Structure):
        name = String()
        year = String()

    data = {"name": "The Bends", "year": "1995"}
    token = tokenize(data)
    validate_with_positions(token=token, validator=MusicAlbum)
    data = {"name": "The Bends"}
    token = tokenize(data)
    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=MusicAlbum)
    assert error.value.messages[0].start_position.char_index == 15

# Generated at 2022-06-14 14:54:58.672671
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object
    from typesystem.fields import String

    class Schema(Object):
        foo = String(required=True)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=Token(value={"foo": "bar"}, start=(1, 2), end=(1, 5)),
            validator=Schema,
        )

    assert exc_info.value.messages() == [
        Message(
            text="The field 'bar' is required.",
            code="required",
            index=("bar",),
            start_position=(1, 2),
            end_position=(1, 5),
        )
    ]

# Generated at 2022-06-14 14:55:03.272955
# Unit test for function validate_with_positions
def test_validate_with_positions():
    assert validate_with_positions(
        token=Token(
            start={"line_number": 1, "char_index": 0},
            end={"line_number": 1, "char_index": 5},
            value={"field": "value"},
        ),
        validator=Schema({"field": Field(required=True)}),
    ) == {"field": "value"}