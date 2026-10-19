

# Generated at 2022-06-14 14:45:19.732979
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Boolean, Integer, String
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token

    class TestSchema(Schema):
        a = Integer()
        b = String()
        c = Boolean()

    test_schema = validate_with_positions(
        token=Token(
            value={
                "a": "not an integer",
                "b": "",
                "c": "not a boolean",
            }
        ),
        validator=TestSchema,
    )


# Generated at 2022-06-14 14:45:29.259206
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, String, Structure

    class TestSchema(Structure):
        field1 = Integer(min_value=2)
        field2 = String(max_length=4)

    from typesystem.tokenize.lexers import JSONLexer

    lexer = JSONLexer()
    tokens = lexer.tokenize("""
    {
        "field1": "not-an-integer",
        "field2": "too long"
    }
    """)

    try:
        validate_with_positions(token=tokens[0], validator=TestSchema)
    except ValidationError as error:
        message = sorted(
            error.messages(),
            key=lambda m: m.start_position.line_index + m.start_position.char_index,
        )[0]
       

# Generated at 2022-06-14 14:45:37.201885
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # pylint: disable=no-value-for-parameter
    from typesystem.schemas import Schema, Integer, String
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import ValueToken

    schema = Schema(properties={"foo": String(), "bar": Integer()})

    tokens = tokenize({"foo": "hello"})
    result = validate_with_positions(
        token=ValueToken(value=tokens, start=(1, 0), end=(1, 0)), validator=schema
    )
    assert result == {"foo": "hello"}

    tokens = tokenize({"bar": "hello"})

# Generated at 2022-06-14 14:45:49.292037
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import Tokenizer

    tokenizer = Tokenizer(
        {"a": {"type": "string"}, "b": {"type": "integer"}},
        extra_validators={"string": Field(max_length=3)}
    )
    token = tokenizer.tokenize('{"a": "123", "b": null}')
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=tokenizer.schema)
    message = exc_info.value.messages[0]
    assert message.code == "max_length"
    assert message.text == "Ensure this value has at most 3 characters."
    assert message.start_position.line_no == 1
    assert message.end_position.line_no == 1


# Generated at 2022-06-14 14:45:56.982345
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.tokenize.tokens import Token


    class PersonSchema(Schema):
        first_name = String()
        last_name = String()

    value = {
        "first_name": "Paweł",
        "last_name": "Błaszczak",
    }
    token = Token(
        value=value,
        start=Position(
            line_index=1,
            char_index=1,
        ),
        end=Position(
            line_index=3,
            char_index=1,
        ),
    )
    try:
        validate_with_positions(token=token, validator=PersonSchema)
    except ValidationError as error:
        assert error

# Generated at 2022-06-14 14:46:08.357346
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import io

    class NameSchema(Schema):
        name = Field(type="string", required=True)

    data = {"name": "John Smith", "age": 32}
    token = Token.from_native(data)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=NameSchema)

    messages = exc_info.value.messages
    assert messages == [Message(text="The field 'age' is required.", code="required",
                                index=("age",),
                                start_position=Position(offset=14, line=0, column=14, char_index=14),
                                end_position=Position(offset=16, line=0, column=16, char_index=16)
                                )]



# Generated at 2022-06-14 14:46:18.950769
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.tokenize.tokens import ObjectToken, StringToken

    from typesystem.tokenize.exceptions import ParseError
    from typesystem.exceptions import ValidationError as ValueError

    class SubSchema(Schema):
        sub_field = Integer(min_value=1, max_value=100)

    class TestSchema(Schema):
        field_a = String()  # type: ignore
        field_b = String(required=False)
        sub_field = SubSchema(required=False)


# Generated at 2022-06-14 14:46:28.089111
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizer import tokenize
    from typesystem.tokenize.types import TokenType

    schema = Schema.from_dict_structure(
        {
            "title": {
                "type": str,
                "description": "Title of the article.",
            },
            "tags": {
                "type": [str],
                "description": "List of tags for the article.",
            },
            "content": {
                "type": str,
                "description": "The content of this article.",
            },
        }
    )

    input_str = """
    {
        "title": "Hello World",
        "tags": ["ok"],
        "content": "This is my content",
    }
    """

    tokens = tokenize(input_str)

    token = tokens[0]
   

# Generated at 2022-06-14 14:46:39.417815
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize_xml
    from typesystem.xml import XMLSchema

    schema = XMLSchema(
        [("person", {"name": "string", "age": "integer"}), ("animal", {"name": "string"})]
    )

    xml = """
    <data>
        <person>
          <name>Alice</name>
          <age>Alice</age>
          <age>34</age>
        </person>
        <animal>
          <name>Bob</name>
        </animal>
    </data>
    """

    token = tokenize_xml(xml)
    token = token.lookup(["data", "person"])

    try:
        schema.validate(token.value)
    except ValidationError as error:
        messages = []

# Generated at 2022-06-14 14:46:46.815543
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from unittest.mock import Mock
    from typesystem.fields import Integer, String, Array
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token

    class SubItem(Schema):
        foo = Integer(required=True)

    class Item(Schema):
        name = String()
        bar = Array(items=[SubItem(), Integer()])

    class Data(Schema):
        foo = Array(items=[Integer(), Item()])


# Generated at 2022-06-14 14:46:55.387036
# Unit test for function validate_with_positions
def test_validate_with_positions():
    assert validate_with_positions(
        token=Token(value={"a": [{"b": 4}]}, start=(1, 1), end=(1, 3))
    ) == {}

    with pytest.raises(ValidationError):
        validate_with_positions(
            token=Token(value=[], start=(1, 1), end=(1, 3)), validator=Schema({"a": []})
        )

# Generated at 2022-06-14 14:47:05.899850
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parsers.primitives import string, boolean
    from typesystem.tokenize.tokens import Token

    # The function under test
    from typesystem.tokenize.utils import validate_with_positions

    # Initialize a Token with data
    token = Token(
        {"title": "My Title", "completed": True},
        {
            "title": string,
            "completed": boolean,
        },
    )

    assert validate_with_positions(token=token, validator=token.validator) == {
        "title": "My Title",
        "completed": True,
    }

    # Make a schema to conform to
    class Todo(Schema):
        title = string(required=True)
        completed = boolean()

    # Invalidate the token, by changing

# Generated at 2022-06-14 14:47:15.065173
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token

    class PersonSchema(Schema):
        name = Field(type=str)

    person = PersonSchema({"name": "John Doe"})

    token = Token(
        value=person,
        start={"line_number": 0, "char_index": 0},
        end={"line_number": 0, "char_index": 14},
        name="Person",
        lookup=lambda x: token,
    )

    try:
        validate_with_positions(token=token, validator=PersonSchema)
    except ValidationError as error:
        error_message = error.messages()[0]
        assert error_message.text == "The field name is required."

# Generated at 2022-06-14 14:47:26.574937
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import DocumentToken
    from typesystem.exceptions import ValidationError
    from typesystem.string import String

    string = String(min_length=5)

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(
            token=DocumentToken(
                start={"char_index": 1, "line_index": 1, "column_index": 1},
                end={"char_index": 3, "line_index": 1, "column_index": 3},
                value="x",
            ),
            validator=string,
        )

    messages = exc.value.messages()

# Generated at 2022-06-14 14:47:29.169452
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token("""{"foo": {"bar": false}}""")
    class Validator(Schema):
        foo = Field(type="string")
    validate_with_positions(token=token, validator=Validator)

# Generated at 2022-06-14 14:47:40.817927
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import DictToken

    class MySchema(Schema):
        field1 = Field(required=True)
        field2 = Field()

    def validate_my_schema(token: DictToken) -> typing.Any:
        return validate_with_positions(
            token=token, validator=MySchema()
        )


# Generated at 2022-06-14 14:47:48.143065
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Attribute

    token = Attribute(
        "unknown",
        start={
            "line": 1,
            "column": 15,
            "char_index": 14
        },
        end={
            "line": 1,
            "column": 23,
            "char_index": 22
        },
    )
    validator = Field(required=True)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=validator)
    messages = exc_info.value.messages()
    assert messages[0].code == "required"
    assert messages[0].start_position == {
        "line": 1,
        "column": 15,
        "char_index": 14
    }
   

# Generated at 2022-06-14 14:47:56.962125
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(required=True)
        age = Field(type="integer")

    token = Token(
        key="person",
        value={"name": "Alice", "age": 35},
        start={
            "line_number": 1,
            "col_number": 3,
            "char_index": 2,
            "filename": "<string>",
        },
        end={
            "line_number": 1,
            "col_number": 15,
            "char_index": 14,
            "filename": "<string>",
        },
    )

    try:
        Person().validate(token.value)
    except ValidationError as error:
        assert error.messages()[0].start_position == (1, 5, 4, "<string>")
        assert error.mess

# Generated at 2022-06-14 14:48:08.149592
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.parser import parse_type, parse_field
    from typesystem.tokenize.positions import Positions
    from typesystem.tokenize.tokens import ListToken, ObjectToken

    # Test that positional information can be obtained from a Schema

    schema = parse_type(
        {
            "type": "object",
            "additionalProperties": False,
            "properties": {"foo": {"type": "string", "minLength": 2}},
        },
        positions=Positions(
            line_offset=1, column_offset=2, line_starts=[0, 10, 12, 14]
        ),
    )

# Generated at 2022-06-14 14:48:14.959394
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(type=str)
        age = Field(type=int)
    token = Token(value={"name": "John Doe"}, children=[
        Token(value="John Doe"),
        Token(value=None),
    ])
    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=Person)

# Generated at 2022-06-14 14:48:26.029202
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(type="string", required=True)

    data = {"name": "Jane"}
    token = Token(value=data)

    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        assert (
            error.messages[0].start_position
            == error.messages[0].end_position
            == token.start
        )
        return

    raise ValueError("Validation Error not raised")



# Generated at 2022-06-14 14:48:34.462031
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import errors, fields, schemas, tokenize
    from typesystem.tokenize.tokens import Token
    from pyrsistent import PRecord, field

    class Person(schemas.Schema):
        first_name = fields.String(required=True)
        last_name = fields.String(required=True)

    source_code = """
        first_name: Jane
        last_name: Doe
    """

    # https://github.com/python/mypy/issues/6962
    # test = Person.validate_with_positions(token=token)  # type: ignore
    tokenizer = tokenize.tokenize(source_code)
    token = next(tokenizer)
    test = validate_with_positions(token=token, validator=Person)

# Generated at 2022-06-14 14:48:45.785068
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.json_schema import JSONSchema

    schema = JSONSchema({"type": "number"})
    token = Token("4", start=(1, 1), end=(1, 2))
    validated = validate_with_positions(token=token, validator=schema)
    assert validated == 4

    token = Token("foo", start=(1, 1), end=(1, 4))
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    error = exc_info.value
    assert error.messages()[0].start_position == (1, 1)
    assert error.messages()[0].end_position == (1, 4)

# Generated at 2022-06-14 14:48:53.440678
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class TestSchema(Schema):
        required_field = Field(required=True)

    with pytest.raises(ValidationError) as exc_info:
        token = Token(value={"not_required_field": "baz"}, start=[0, 0], end=[0, 0])
        validate_with_positions(token=token, validator=TestSchema)

    assert str(exc_info.value) == "The field 'required_field' is required."

# Generated at 2022-06-14 14:49:03.549093
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import RecordSchema
    from typesystem.fields import StringField

    class UserRecord(RecordSchema):
        name = StringField(required=True)
        email = StringField(required=True)

    token = Token(
        value={"name": "", "email": ""},
        start={"line": 0, "column": 0, "char_index": 0},
        end={"line": 0, "column": 0, "char_index": 0},
    )

    try:
        validate_with_positions(validator=UserRecord(), token=token)
    except ValidationError as error:
        assert len(error.messages) == 2
        assert error.messages[0].text == "The field 'name' is required."

# Generated at 2022-06-14 14:49:08.831146
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer

    token = Token(value=1, start=0, end=10)
    assert validate_with_positions(token=token, validator=Integer()) == 1

    token = Token(value="", start=0, end=10)
    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=Integer())
    assert all(message.start_position.char_index == 0 for message in error.value.messages)  # type: ignore

# Generated at 2022-06-14 14:49:20.608500
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Document, Literal

    document = Document(
        [
            Literal("foo", start=1, end=2),
            Literal("bar", start=3, end=4),
        ]
    )

    class FooSchema(Schema):
        pass

    class BarSchema(Schema):
        pass

    errors = []
    try:
        document.validate([FooSchema(), BarSchema()])
    except ValidationError as error:
        errors = error.messages()

    assert len(errors) == 2
    foo, bar = errors
    if foo.start_position.line_index == 0 and foo.start_position.char_index == 0:
        foo, bar = bar, foo

    assert foo.code == "required"
    assert foo.text

# Generated at 2022-06-14 14:49:28.290046
# Unit test for function validate_with_positions
def test_validate_with_positions():
    f = Field(type="string")
    token = Token(value="", start_position=0, end_position=0)
    try:
        validate_with_positions(token=token, validator=f)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field '' is required.",
                code="required",
                index=("",),
                start_position=0,
                end_position=0,
            )
        ]

# Generated at 2022-06-14 14:49:37.873473
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Integer, Array

    schema = {"a": Integer, "b": String, "foo": {"c": Array[Integer], "d": String}}

    source = """
{
  "a": 1,
  "b": "foo",
  "foo": {
    "c": [1, 2, 3],
    "d": 123
  }
}
    """

    parsed = parse_json(source)
    try:
        validate_with_positions(token=parsed, validator=schema)
    except ValidationError as error:
        messages = list(error.messages())
        assert len(messages) == 1
        message = messages[0]
        assert message.text == "Invalid string value."
        assert message.start_position.line == 8

# Generated at 2022-06-14 14:49:47.851276
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer, String
    from typesystem.schemas import Object, Schema

    class TestObject(Schema):
        a = Integer()
        b = String()

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=Token(value={"a": 1, "b": 2}, start=(0, 0), end=(1, 1)),
            validator=TestObject,
        )
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert (
        message.text
        == 'Value 2 is not a valid string: not a valid string. Expected value is 1.'
    )
    assert message.code == "invalid"

# Generated at 2022-06-14 14:50:01.274217
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.schema import Schema
    from typesystem.fields import Object
    from typesystem.tokenize import JSONLDParser

    class UserSchema(Schema):
        first_name = Object(name="first_name", fields={"first": str, "last": str})

    parser = JSONLDParser()
    token = parser.parse('{"first_name": {"first": "Oink", "last": "Pig"}}')
    validated = validate_with_positions(token=token, validator=UserSchema)
    assert validated == {"first_name": {"first": "Oink", "last": "Pig"}}

    token = parser.parse('{"first_name": {"first": "Oink"}}')

# Generated at 2022-06-14 14:50:13.044364
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class A:
        a = 1

    class B(Schema):
        a = Field(type=int)

    token = Token(
        start={"char_index": 0},
        end={"char_index": 1},
        value=A(),
        lookup=lambda key: Token(
            start={"char_index": key + 1},
            end={"char_index": key + 2},
            value={"a": 1},
        ),
    )

    try:
        validate_with_positions(token=token, validator=B)
    except ValidationError as error:
        assert error.messages()[0].start_position == {"char_index": 1}
        assert error.messages()[0].end_position == {"char_index": 2}

# Generated at 2022-06-14 14:50:24.489757
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.asset_utils import parse_asset
    from typesystem.tokenize.tokenization_utils import tokenize_asset
    from typesystem.schemas import Schema
    from typesystem.integer import Integer
    from typesystem.tokenize.tokens import Object, Value

    class TestSchema(Schema):
        field = Integer()

    asset = parse_asset("{'field': 'value'}")
    tokens = list(tokenize_asset(asset))
    token = tokens[0].children[0]
    assert token.kind == Object
    assert len(token.children) == 1
    assert token.children[0].kind == Object.Property
    assert token.children[0].key.value == "field"
    assert token.children[0].value.kind == Value
   

# Generated at 2022-06-14 14:50:31.242096
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Test(Schema):
        name = Field(type="string")
        value = Field(type="integer")

    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(
            token=Token(
                start=(0, 0),
                end=(5, 5),
                value={"value": "10"},
                lookup=lambda path: Token(
                    start=(0, 0),
                    end=(5, 5),
                    value={"value": "10"},
                    lookup=lambda path: Token(
                        start=(1, 3),
                        end=(4, 5),
                        value="10",
                    ),
                )
            ),
            validator=Test(),
        )


# Generated at 2022-06-14 14:50:41.841021
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.values import Integer
    from typesystem.tokenize.rules import JSONPointer
    from typesystem.tokenize.exceptions import TokenizeError

    value = '{"foo": {"bar": "baz", "qux": null}}'
    token = JSONPointer.tokenize(value)
    assert validate_with_positions(token=token, validator=Integer()) # type: ignore

    value = '{"foo": {"bar": "baz", "qux": "quux"}}'
    token = JSONPointer.tokenize(value)
    assert validate_with_positions(token=token, validator=Integer()) # type: ignore

    value = '{"foo": {"bar": 1, "qux": "quux"}}'
    token = JSONPointer.tokenize(value)

# Generated at 2022-06-14 14:50:53.526014
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema, fields
    from typesystem.tokenize import tokenize

    class PersonSchema(Schema):
        name = fields.String(required=True)
        age = fields.Integer(required=True)

    tokens = tokenize(
        """{
        "name": "Piet",
        "age": "thirty-one"
    }"""
    )
    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=tokens, validator=PersonSchema)


# Generated at 2022-06-14 14:51:00.992666
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from json import loads
    from typesystem.tokenize.simple import SimpleJSONTokenizer

    from typesystem import String, Integer

    class TestSchema(Schema):
        name = String(required=False)
        age = Integer()

    raw_json = """
    {
        "name": "foo",
        "age": "bar"
    }
    """

    tokens = SimpleJSONTokenizer().tokenize(raw_json)
    validate_with_positions(token=tokens, validator=TestSchema)

# Generated at 2022-06-14 14:51:08.907959
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer

    class X(Schema):
        a = String(required=True)
        b = Integer(min_value=0, max_value=10)

    # no field provided

# Generated at 2022-06-14 14:51:18.251807
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class MySchema(Schema):
        name = String(min_length=2)

    try:
        validate_with_positions(
            token=tokenize('{"name": ""}'), validator=MySchema
        )
    except ValidationError as error:
        assert error.messages() == [
            Message(
                code="required",
                index=["name"],
                text="The field 'name' is required.",
                start_position=Position(line=1, column=2, char_index=0),
                end_position=Position(line=1, column=10, char_index=8),
            )
        ]
    else:
        raise AssertionError()

# Generated at 2022-06-14 14:51:29.500796
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Array
    from typesystem.fields import Integer, String

    array = Array(min_items=3, items=[String(), Integer()])

    def check(token: Token) -> None:
        validate_with_positions(token=token, validator=array)

    # success
    token = Token(
        type="list",
        value=["1", "2", "3"],
        element_types=["str", "str", "str"],
        start=(1, 0),
        end=(1, 8),
    )
    check(token)

    # error, field

# Generated at 2022-06-14 14:51:43.251539
# Unit test for function validate_with_positions
def test_validate_with_positions():
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=Token(
                value={"foo": None},
                start=TokenPosition(line=1, character=2),
                end=TokenPosition(line=2, character=2),
            ),
            validator=Schema(fields={"foo": Field(required=True)}),
        )
    assert exc_info.value.messages() == [
        Message(
            code="required",
            index=("foo",),
            text="The field 'foo' is required.",
            start_position=TokenPosition(line=1, character=2),
            end_position=TokenPosition(line=2, character=2),
        )
    ]



# Generated at 2022-06-14 14:51:54.983994
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import typesystem
    from typesystem import fields
    from typesystem.tokenize.types import Token

    schema = typesystem.Schema(
        {
            "id": fields.Str(required=True),
            "title": fields.Str(required=True),
            "content": fields.Str(required=True),
            "article": fields.Str(required=True),
            "comments": fields.Array(
                items=fields.Dict(
                    {
                        "author": fields.Str(required=True),
                        "body": fields.Str(required=True),
                    }
                ),
                required=True,
            ),
        }
    )

    input = json.dumps({})

    token = Token.parse(input)

    assert token.start == token.end


# Generated at 2022-06-14 14:52:01.743333
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema([{"name": {"type": "string", "required": True}}])
    data = [{"name": None}]
    token = Token.from_data(data)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    message = exc_info.value.messages()[0]
    assert message.text == "The field 'name' is required."
    assert message.start_position == (1, 7)  # noqa
    assert message.end_position == (1, 8)  # noqa

# Generated at 2022-06-14 14:52:08.382027
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import IntToken
    from typesystem.fields import Integer

    token = IntToken(value=100, start_position={}, end_position={})
    value = validate_with_positions(token=token, validator=Integer(min_value=200))
    assert value is None



# Generated at 2022-06-14 14:52:17.889534
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.tokenize import tokens
    from typesystem.validators import Type

    data = '{"foo": 1, "bar": "1", "baz": 2}'
    tokens = tokenize(data=data)
    token = tokens.lookup(["foo"])
    assert isinstance(token, tokens.Field)
    assert token.name == "foo"
    assert token.value == 1
    assert token.parent is tokens
    assert token.start.line == 1
    assert token.start.index == 2
    assert token.start.char_index == 2
    assert token.start.column == 3

    validate_with_positions(token=token, validator=Type("number"))

    token = tokens.lookup(["bar"])

# Generated at 2022-06-14 14:52:24.780133
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Integer
    from typesystem.tokenize.tokenizer import tokenize_file, InvalidFileError

    class UserSchema(Schema):
        name = String()
        age = Integer(minimum=18)

    try:
        token = tokenize_file("tests/tokenizer/data/user.yaml")
    except InvalidFileError as error:
        messages = (error.messages)
    else:
        try:
            value = validate_with_positions(
                token=token,
                validator=UserSchema,
            )
        except ValidationError as error:
            messages = (error.messages)
        else:
            # print(json.dumps(value, indent=2))
            messages = None

    assert messages

    # name is required
    start_line = 6
    start

# Generated at 2022-06-14 14:52:35.658999
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer

    class AuthorSchema(Schema):
        name = String()
        age = Integer()

    token = Token.parse(
        {"type": "object", "properties": {"name": "Mark", "age": 30}},
        ["name"],
    )

    try:
        validate_with_positions(token=token, validator=AuthorSchema)
    except ValidationError as error:
        assert error.messages() == [Message(code="required", index=["age"])]

    token = Token.parse(
        {"type": "object", "properties": {"name": "Mark", "age": "30"}},
        ["name"],
    )


# Generated at 2022-06-14 14:52:45.668546
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.pygments_lexer import (
        CommonMarkTokenStream,
        CommonMarkLexer,
    )
    from typesystem.tokenize.tokens import Token

    content = """
    This is an *unordered* list:

    * apples
    * peaches
    * pears

    And this is an ordered one:

    1. apples
    2. peaches
    3. pears
    """
    lexer = CommonMarkLexer()
    tokens = lexer.get_tokens(content)
    token_stream = CommonMarkTokenStream(tokens=tokens)
    token = Token.from_stream(token_stream)
    try:
        validate_with_positions(token=token, validator=token)
    except ValidationError as error:
        messages = error

# Generated at 2022-06-14 14:52:54.328599
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.parse import parse

    field = Field(type="integer", required=True)
    token = parse('{"foo": "bar"}')
    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as exc:
        message = exc.messages()[0]
        assert message.text == 'The field "foo" is required.'
        assert message.start_position.line == 0
        assert message.start_position.char_index == 3
        assert message.end_position.line == 0
        assert message.end_position.char_index == 10

# Generated at 2022-06-14 14:53:03.534115
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.types import String
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.tokenizers import JSONTokenizer

    schema = Schema({"a_string": String(max_length=5, min_length=3)})

    def test(*, string: str, expected_message: str):
        token = JSONTokenizer(string).parse()
        with pytest.raises(ValidationError) as exc_info:
            validate_with_positions(
                token=token,
                validator=schema,
            )
        message = exc_info.value.messages[0]
        assert str(message) == expected_message


# Generated at 2022-06-14 14:53:15.179574
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import Tokenizer
    from typesystem.tokenize.exceptions import TokenizeError

    with pytest.raises(
        TokenizeError,
        match='The "name" field is required. (line 1, column 4)',
    ):
        Tokenizer().from_string('{"age": 21}').to_schema(PersonSchema)

    with pytest.raises(
        TokenizeError,
        match=(
            'The "email_address" field is required. '
            "(line 1, column 8)\n"
            'The "name" field is required. (line 1, column 4)'
        ),
    ):
        Tokenizer().from_string('{"age": 21}').to_schema(ContactSchema)



# Generated at 2022-06-14 14:53:26.918826
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.json_schema import JSONSchema

    validator = JSONSchema(
        properties={
            "name": {"title": "Name", "type": "string", "length": [1, 10]}
        }
    )

    value = {"name": ""}

    try:
        validate_with_positions(token=value, validator=validator)
    except ValidationError as error:
        message = error.messages[0]
        assert message.text == 'The field "name" must contain between 1 and 10 items.'
        assert message.code == "length"
        assert message.index == ("name",)
        assert message.start_position.line == 1
        assert message.start_position.char_index == 2
        assert message.end_position.line == 1
        assert message.end_position.char

# Generated at 2022-06-14 14:53:37.625228
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token
    from typesystem import Integer, String

    class TestSchema(Schema):
        int1 = Integer(minimum=1, maximum=2)
        int2 = Integer(minimum=3, maximum=4)
        str1 = String(min_length=1, max_length=2)
        str2 = String(min_length=3, max_length=4)


# Generated at 2022-06-14 14:53:48.752520
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize, Token
    from typesystem.types import String
    from typesystem.fields import Field

    obj = {"name": "Jane", "email": ""}
    field = Field(type=String())

    # Try without the textual representation
    tokens = tokenize(obj)
    validate_with_positions(token=tokens, validator=field)

    # Try with the textual representation
    tokens = tokenize(obj, as_string='{"name": "Jane", "email": ""}')

# Generated at 2022-06-14 14:54:00.454260
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.rules import to_tokens

    class Person(Schema):
        name = Field(str)
    
    # Test that a standard Field error message is converted to a
    # positional message.
    token = to_tokens("{}")[0]
    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=Person)
    message = error.value.messages[0]
    assert message.start_position.line_no == 1
    assert message.start_position.char_no == 1
    assert message.text == "The field 'name' is required."

    # Test that a custom error message is converted to a positional
    # message.

# Generated at 2022-06-14 14:54:06.797726
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.postgresql.schema import PostgreSQLSchema

    schema = PostgreSQLSchema({"data": {"foo": "int"}})

    token = Token.dumps({"data": {"foo": "abc"}})

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=schema)

    assert exc.value.messages() == [
        Message(
            text="ValueError: invalid literal for int() with base 10: 'abc'",
            code="invalid",
            index=["data", "foo"],
            start_position=(17, 9, 17),
            end_position=(20, 9, 20),
        )
    ]



# Generated at 2022-06-14 14:54:16.486314
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokens

    schema = {
        "string": {"type": "string"},
        "number": {"type": "number"},
        "boolean": {"type": "boolean"},
    }
    schema = Schema.from_dict(schema)
    token = tokens.Dict(
        {
            "string": tokens.Value("foo"),
            "number": tokens.Value(1.0),
            "boolean": tokens.Value(True),
        },
        start=tokens.Position(line=1, char_index=0),
        end=tokens.Position(line=4, char_index=4),
    )

    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        assert error.messages

# Generated at 2022-06-14 14:54:25.978208
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.tokenize.loader import load_string

    class User(Schema):
        name = Field(str, required=True)
        age = Field(int)

    doc = load_string(
        """
        name = "Bob"
        """
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=doc, validator=User())

    [message] = exc_info.value.messages()
    assert message.text == "The field 'age' is required."
    assert message.start_position.line == 1
    assert message.start_position.char_index == 0
    assert message.end_position.line == 1
    assert message.end_position.char_index == 10

# Generated at 2022-06-14 14:54:35.836190
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import IntegerToken
    from typesystem.fields import Integer

    token = IntegerToken(
        value=3.14,
        start=CharacterPosition(line=1, column=1, char_index=0),
        end=CharacterPosition(line=1, column=5, char_index=4),
    )
    validator = Integer(
        min_value=5,
        messages={
            "min_value": "I expect an integer that is greater than {min_value!r}."
        },
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=validator)

    assert len(exc_info.value.messages) == 1


# Generated at 2022-06-14 14:54:41.887571
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.combinators import literal
    from typesystem.tokenize.tokens import Token

    token = literal("[")
    token = token.lookup(["patterns", 0, "elements", 0])
    validator = Field(type="string")

    try:
        validate_with_positions(token=token, validator=validator)
    except ValidationError as error:
        [message] = error.messages()
        assert message.start_position.char_index == 1

# Generated at 2022-06-14 14:54:55.389149
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json

    from typesystem.schemas import Schema
    from typesystem.tokenize.positional import PositionalToken
    from typesystem.tokenize.tokens import Token

    class MonsterSchema(Schema):
        name = Field(str)

    schema = MonsterSchema()

    value = json.dumps(
        {"name": "Zombie", "attack": 10, "defense": 50}, ensure_ascii=True, indent=4
    )

    token = Token(
        value={
            "name": PositionalToken(value=value, start=2, end=9),
            "attack": PositionalToken(value=value, start=12, end=19),
            "defense": PositionalToken(value=value, start=22, end=30),
        }
    )


# Generated at 2022-06-14 14:55:02.043875
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    schema = Schema({"name": Field(type="string", required=True)})

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=tokenize("{}"), validator=schema)

    assert exc_info.value.messages[0].start_position == (1, 1)
    assert exc_info.value.messages[0].end_position == (1, 1)

# Generated at 2022-06-14 14:55:13.605720
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize, TokenType
    from unittest.mock import Mock
    from faker import Faker

    faker = Faker()

    class PageSchema(Schema):
        title = Field(str)
        body = Field(str)
        page_id = Field(str)

    page_schema = PageSchema()
    page_token = tokenize(
        faker.paragraph(), content_type=TokenType.json, path=[faker.pystr()]
    )

    expected_message = Message(
        text=f"The field 'title' is required.",
        code="required",
        index=["title"],
        start_position=page_token.start,
        end_position=page_token.end,
    )
