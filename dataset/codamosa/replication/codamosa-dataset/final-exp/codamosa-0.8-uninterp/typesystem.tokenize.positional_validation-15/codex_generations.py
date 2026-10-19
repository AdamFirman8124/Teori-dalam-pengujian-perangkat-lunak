

# Generated at 2022-06-14 14:45:19.732104
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        value=dict(
            test=[dict(nested="value")],
            another=dict(nested=dict(nested="value")),
            required=None,
        ),
        start=Position(line=1, column=1),
        end=Position(line=5, column=5),
    )

    class Nested(Schema):
        nested = Field(str)

    class Test(Schema):
        test = Field(Nested, many=True)
        another = Field(Nested)
        required = Field(str, required=True)

    validate_with_positions(
        token=token,
        validator=Test,
    )

    token.value.get("required")
    token.value.get("another")["required"]


# Generated at 2022-06-14 14:45:21.684744
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # TODO: implement test
    pass  # pragma: no cover

# Generated at 2022-06-14 14:45:29.104247
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer

    integer = Integer()
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(
            token=Token(value="abc", start=(1, 1), end=(1, 4)), validator=integer
        )
    assert (
        excinfo.value.messages[0].text
        == "Value must be an integer (1-byte signed integer)."
    )
    assert excinfo.value.messages[0].start_position == (1, 1)
    assert excinfo.value.messages[0].end_position == (1, 4)



# Generated at 2022-06-14 14:45:37.089005
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.positions import Position
    from typesystem.tokenize.tokens import BooleanToken, NullToken, ObjectToken
    from typesystem.fields import String

    schema = Schema({"name": String()})
    object_token = ObjectToken(
        start=Position(path="tests.json", line_number=1, char_index=1),
        end=Position(path="tests.json", line_number=1, char_index=2),
        content={"name": BooleanToken(True)},
    )
    text = "Expected a value of type 'string' for field 'name', but got a value of type 'boolean' instead."

# Generated at 2022-06-14 14:45:49.136381
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Unit(Schema):
        m = Field(type="integer")
        a = Field(type="integer")

    class Integers(Schema):
        integers = Field(type="array", items=Field(type=Unit))

    schema = Integers()

    def validate(string):
        token = Token.parse(string)
        return validate_with_positions(token=token, validator=schema)

    validate("""
    integers:
      - m: 1
        a: 3
      - m: 2
        a: 2
    """)

    with pytest.raises(ValidationError) as exc:
        validate("""
        integers:
          - m: 1
            a: 3
          - m: 2
        """)
    assert exc.value.messages()[0].start_position.line_index

# Generated at 2022-06-14 14:45:55.585774
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    schema = String(min_length=5)

    class Person(Schema):
        name = String(min_length=5)
        age = String(min_length=3)

    token = Token(
        value={
            "name": "bar",
            "age": "21",
        },
        start=1,
        end=1,
    )

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(
            token=token,
            validator=Person,
        )
    assert excinfo.value.messages()[0].text == "The field 'name' is required."

# Generated at 2022-06-14 14:46:03.033250
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import sys

    from typesystem.base import Message
    from typesystem.fields import String, Integer
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokenize

    json_schema = json.loads(
        """
        {
          "type": "object",
          "properties": {
            "x": {
              "type": "integer"
            },
            "y": {
              "type": "integer"
            }
          },
          "required": [
            "x",
            "y"
          ]
        }
    """
    )
    schema = Schema.from_json_schema(json_schema)
    token = tokenize("{}").lookup("root")

# Generated at 2022-06-14 14:46:13.969707
# Unit test for function validate_with_positions
def test_validate_with_positions():
    data = {"a": {"b": "c"}}
    token = Token("value", data)

    field = Field(type="object")
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=field)

    messages = exc.value.messages
    assert len(messages) == 1
    assert messages[0].text == "The field 'a' is required."
    assert messages[0].code == "required"
    assert messages[0].index == ["a"]
    assert messages[0].start_position.line == 0
    assert messages[0].start_position.char_index == 3
    assert messages[0].end_position.line == 0
    assert messages[0].end_position.char_index == 4


# Generated at 2022-06-14 14:46:23.476471
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object

    class Person(Object):
        name = Field(str, required=True)

    token = Token(
        value={
            "name": "Bob",
        },
        start=0,
        end=100,
    )

    validate_with_positions(token=token, validator=Person)

    def assert_one_message(token, errors):
        assert len(errors) == 1
        message = errors[0]
        assert message.start_position == token.start
        assert message.end_position == token.end

    token = Token(
        value={},
        start=0,
        end=100,
    )

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=Person)
   

# Generated at 2022-06-14 14:46:34.141051
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String

    token = Token(value="foo", start=(1, 1), end=(1, 4))
    value = validate_with_positions(token=token, validator=String(max_length=2))
    assert value == "foo"

    try:
        validate_with_positions(token=token, validator=String(min_length=4))
    except ValidationError as error:
        assert len(error.messages()) == 1
        message = error.messages()[0]
        assert message.code == "min_length"
        assert message.text == "Must be at least 4 characters."
        assert message.index == []
        assert message.start_position == (1, 1)
        assert message.end_position == (1, 4)

# Generated at 2022-06-14 14:46:48.927948
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pathlib
    import pytest
    from typesystem.fields import String, Integer, Array
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokenize

    class MySchema(Schema):
        arr = Array(of=Integer())
        name = String()

    schema = MySchema()

    path = str((pathlib.Path(__file__).parent / "users.json").resolve())
    tokens = tokenize(open(path).read())
    token = tokens.lookup("users.0.name")

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=Integer())

    assert len(exc.value.messages) == 1
    message = exc.value.messages[0]
    assert message.start

# Generated at 2022-06-14 14:46:57.581356
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import parse

    schema_token = Token(
        "schema",
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "date": {"type": "string", "format": "datetime"},
            },
            "required": ["name", "date"],
        },
    )

    try:
        validate_with_positions(
            validator=parse(schema_token.value), token=Token("value", {"name": 1})
        )
        assert False, "Should have failed validation."
    except ValidationError as error:
        assert len(error.messages()) == 2, "Should have failed two validations."
        assert error.messages()[0].text == "The field 'date' is required."

# Generated at 2022-06-14 14:47:08.539802
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.grammar.tokens import (
        FieldToken,
        ObjectToken,
        StringToken,
        Token,
    )

    # Create a nested object with a string field in it.
    obj = ObjectToken(
        start_position=Token.Positional(line_index=0, char_index=0),
        value={
            "x": ObjectToken(
                start_position=Token.Positional(line_index=0, char_index=5),
                value={"y": StringToken(
                    start_position=Token.Positional(line_index=1, char_index=2),
                    value="z",
                )},
            )
        },
    )

    # Define a field that requires the string field in the nested object.
    class TheSchema(Schema[str]):
        x

# Generated at 2022-06-14 14:47:16.245484
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Array, Integer, String
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token, DocumentToken, PrimitiveToken

    class TestSchema(Schema):
        name = String(required=True)

    class TestSubSchema(Schema):
        age = Integer(required=True)

    class TestArraySchema(Schema):
        data = Array(items=TestSubSchema)


# Generated at 2022-06-14 14:47:27.339231
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexer import create_lexer
    from typesystem.tokenize.parser import create_parser
    from typesystem.tokenize.tokens import Document

    schema = Schema(fields={"name": Field(required=True)})
    lexer = create_lexer()
    parser = create_parser()
    document = lexer.tokenize(b"""{"name": "John", "age": 30}""")
    document = parser.parse(document)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=document, validator=schema)

    message = exc_info.value.messages[0]
    assert message.text == "The field 'name' is required."
    assert message.start_position == (1, 11)
   

# Generated at 2022-06-14 14:47:34.414864
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import Parser

    token = Parser().parse('{"a": 1')
    try:
        validate_with_positions(token=token, validator={"a": Field(type="integer")})
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field 'a' is required.",
                code="required",
                index=["a"],
                start_position=Position(line=1, char_index=6),
                end_position=Position(line=1, char_index=7),
            )
        ]

    token = Parser().parse('{"a": "foo"}')

# Generated at 2022-06-14 14:47:44.496630
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Arrange
    from typesystem.schemas import Object, Text, Number
    from typesystem.tokenize import tokenize, Token

    class Data(Object):
        name = Text()
        age = Number(minimum=0, maximum=100)

    data = {"first_name": "", "last_name": "doe", "age": "123"}
    token = tokenize(data)  # type: Token

    # Assert
    class AssertValidationError(Exception):
        pass

    try:
        validate_with_positions(token=token, validator=Data)  # type: ignore
    except ValidationError as error:
        message = error.messages[0]
        assert message.code == "minimum"
        assert message.text == "The value must be at least 0."
    else:
        raise Ass

# Generated at 2022-06-14 14:47:55.248667
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Tokens, TokenType
    from typesystem.schemas import BooleanSchema

    data = {"v": False}
    tokens = Tokens("True")

    tokens.append(
        Token(data=data, value=True, start=0, end=3, type=TokenType.DICT)
    )

    token = tokens.lookup("v")
    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(token=token, validator=BooleanSchema())

    messages = error_info.value.messages
    assert messages[0].text == "Expected a boolean."
    assert messages[0].start_position == 0
    assert messages[0].end_position == 3



# Generated at 2022-06-14 14:48:07.215085
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(type="string")

    token = Token(
        value="",
        start=Position(line=1, column=1, char_index=0),
        end=Position(line=1, column=1, char_index=0),
    )
    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(token=token, validator=field)
    assert error_info.value.messages() == [
        Message(
            text="The field {0!r} is required.".format(None),
            code="required",
            start_position=Position(line=1, column=1, char_index=0),
            end_position=Position(line=1, column=1, char_index=0),
            index=(),
        )
    ]

   

# Generated at 2022-06-14 14:48:16.415084
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(str)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=Token(value={}), validator=Person)

    message = exc_info.value.messages[0]
    assert message.text == "The field name is required."
    assert message.start_position.line == 0
    assert message.start_position.char_index == 3
    assert message.end_position.line == 0
    assert message.end_position.char_index == 4

# Generated at 2022-06-14 14:48:33.147612
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(type="string")

    schema = Person()
    token = Token.from_value({"name": "Cathy"})
    assert validate_with_positions(token=token, validator=schema) == {"name": "Cathy"}

    empty_token = Token.from_value({})
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=empty_token, validator=schema)

    message = excinfo.value.messages[0]
    assert message.start_position.line_number == 1
    assert message.start_position.char_index == 1
    assert message.end_position.line_number == 1
    assert message.end_position.char_index == 2


# Generated at 2022-06-14 14:48:45.070474
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """
    Unit test for positional error reporting in type `type`,
    """
    from typesystem import types

    class Address(types.Schema):

        street = types.String(min_length=5)
        zip_code = types.String()

    class Person(types.Schema):
        name = types.String(min_length=5)
        address = types.Schema(Address)

    json = {"name": "John", "address": {"street": ""}}
    token = Token.from_python(json)

    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        assert len(error.messages()) == 2
        assert error.messages()[0].index == ["address", "street"]

# Generated at 2022-06-14 14:48:57.124853
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import typesystem.tokenize as tokenize

    schema = tokenize.parse_schema(
        """
[
    {
        "name": "firstName"
    },
    {
        "name": "lastName"
    }
]
"""
    )

    data = json.loads(
        """
{
    "firstName": "Aaron",
    "middleName": "H",
    "lastName": "Hall"
}
"""
    )

    try:
        validate_with_positions(token=tokenize.tokenize(data), validator=schema)
    except ValidationError as error:
        for message in error.messages():
            print(message.text)
            print(message.start_position)


if __name__ == "__main__":
    test_validate

# Generated at 2022-06-14 14:49:04.437450
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize import tokenize

    token = tokenize('{"key": "value"}')
    token = token.lookup(["key"])

    validator = String()
    validate_with_positions(token=token, validator=validator)

    validator = String(required=True)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=validator)
    field_error = exc_info.value.messages[0]
    assert field_error.text == "The field 'key' is required."



# Generated at 2022-06-14 14:49:16.220801
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from datetime import date
    from unittest import mock

    from typesystem.tokenize import tokenize

    timestamp_field = Field(type="string", format="timestamp")

    with mock.patch.object(timestamp_field, "validate", side_effect=ValidationError):
        doc = '{"created": "01/01/2020"}'
        tokens = tokenize(doc)

        try:
            validate_with_positions(token=tokens, validator=timestamp_field)
        except ValidationError as error:
            assert error.messages[0].text == "Incorrect timestamp format."
            assert error.messages[0].start_position.char_index == 14


# Generated at 2022-06-14 14:49:26.089855
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Schema, fields
    from typesystem.tokenize import Tokenizer, tokens
    tokenizer = Tokenizer({"type": "string"}, check_fields=False)
    try:
        result = validate_with_positions(
            token=tokens.StringToken(data='"foo"'), validator=fields.String()
        )
    except ValidationError as error:
        assert error.messages()[0].text == "The field 'type' is required."
        assert error.messages()[0].start_position.line == 0
        assert error.messages()[0].start_position.char_index == 0



# Generated at 2022-06-14 14:49:26.715789
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:49:36.464391
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.exceptions import ValidationError
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import DocumentToken

    class MySchema(Schema):
        foo = Field(required=True)

    s = MySchema()
    document = """{"foo": "foo"}"""

    try:
        validate_with_positions(token=DocumentToken(document=document), validator=s)
    except ValidationError as e:
        # assert exception
        assert e.messages[0].code == "required"
        assert e.messages[0].index == ["foo"]
        assert e.messages[0].text == "The field 'foo' is required."
        assert e.messages[0].start_position.line == 0
        assert e.messages[0].start_

# Generated at 2022-06-14 14:49:43.979448
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.testing import build_token

    from typesystem.fields import String

    token = build_token({})
    try:
        validate_with_positions(token=token, validator=String())
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field s is required.",
                code="required",
                index=(0,),
                start_position=token.start,
                end_position=token.end,
            )
        ]
    else:
        assert False, "validate_with_positions did not fail"



# Generated at 2022-06-14 14:49:51.885833
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tokenize.tokens import Token, TokenList, TokenType, NumberToken

    # Create a schema that expects an object with one field "num" that should be an integer
    class NumSchema(Schema):
        num: int

        class Meta:
            strict = True

    # Create a token list that contains a single number token
    token_list = TokenList(
        [NumberToken(value=42, start=(1, 3), end=(1, 5))], type=TokenType.OBJECT
    )
    token: Token = token_list[0]

    # Validation should succeed
    assert validate_with_positions(token=token, validator=NumSchema) == {"num": 42}

    # Create a token list that contains an empty object
    token_list = TokenList([], type=TokenType.OBJECT)
    token

# Generated at 2022-06-14 14:50:16.486046
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class PersonSchema(Schema):
        name = Field(type="string", required=True)
        age = Field(type="integer")

    p = {"age": "abc"}

# Generated at 2022-06-14 14:50:27.028604
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Array

    class Person(Schema):
        name = String()
        friends = Array(items=String())

    token = Token.parse("""{
        name: "John"
        friends: [
            "Bill",
            "Jane",
        ]
    }""")

    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field 'age' is required.",
                code="required",
                index=("age",),
                start_position=Position(line=3, char_index=2),
                end_position=Position(line=3, char_index=5),
            )
        ]
    else:
        assert False, "Should have raised"

# Generated at 2022-06-14 14:50:39.458245
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import parse_to_tokens

    schema = Schema({"foo": Field(required=True)})

    source = """{
    "foo": 123,
    "bar": "baz"
}"""

    tokens = parse_to_tokens(source)

    # successful validation
    try:
        schema.validate(tokens)
    except ValidationError:
        assert False

    # unknown field
    with pytest.raises(ValidationError) as e:
        schema.validate(tokens[1:])
    assert [m.text for m in e.value.messages] == ["The field 'bar' is unknown."]

    # missing required field

# Generated at 2022-06-14 14:50:49.875433
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object

    class TestSchema(Object):
        name = "TestSchema"
        properties = {"foo": str, "bar": float}

    token = Token(
        "TestToken", "", context={"foo": "abc", "bar": "def"}, start=None, end=None
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=TestSchema)
    (message,) = exc_info.value.messages()

    assert message.start_position is None
    assert message.end_position is None

# Generated at 2022-06-14 14:50:54.960055
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    exception = validate_with_positions.__validators__[0][1]
    schema = exception("code", String(), required=True)
    value = validate_with_positions(token=Token("string"), validator=schema)



# Generated at 2022-06-14 14:51:00.891895
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Dictionary, String

    schema = Dictionary(fields={"foo": String()})
    data = {}
    try:
        validate_with_positions(token=Token(value=data, start={}, end={}), validator=schema)
    except ValidationError as error:
        assert error.messages() == [Message(index=["foo"], code="required")]



# Generated at 2022-06-14 14:51:07.697078
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        start=Token.Position(line=1, column=1, char_index=0),
        end=Token.Position(line=1, column=2, char_index=1),
        value=10,
    )

    # Expect validation error with positions
    try:
        validate_with_positions(token=token, validator=Field(type=str))
    except ValidationError as error:
        assert len(error.messages()) == 1
        message = error.messages()[0]
        assert message.start_position.char_index == 0
        assert message.end_position.char_index == 1



# Generated at 2022-06-14 14:51:17.225677
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import parse

    class SimpleSchema(Schema):
        str = Field(type="string", required=True)

    assert validate_with_positions(
        token=parse('{"str": ""}'), validator=SimpleSchema
    ) == {"str": ""}

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=parse('{"str": ""}'), validator=Field(required=True))
    assert exc_info.value.message.start == {"line": 1, "column": 1, "char_index": 0}
    assert exc_info.value.message.end == {"line": 1, "column": 8, "char_index": 7}

# Generated at 2022-06-14 14:51:28.767962
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem import Integer
    from typesystem.tokenize.tokenizer import tokenize
    from typesystem.type import Boolean
    from typesystem.validators import MaxLength

    schema = {
        "blah": Integer(),
        "foo": {
            "foo1": Boolean(),
            "foo2": MaxLength(10),
            "foo3": {
                "foo3a": Boolean(required=True),
                "foo3b": Boolean(),
            }
        }
    }
    tok = tokenize(schema)

    with pytest.raises(ValidationError):
        validate_with_positions(token=tok, validator=schema)

    schema["blah"].required = True

# Generated at 2022-06-14 14:51:38.869967
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object
    from typesystem.fields import String

    def build_schema(keys: typing.List[str]) -> Object:
        class NameSchema(Object):
            attributes = [String(name=key) for key in keys]
        return NameSchema()

    def build_token(keys: typing.List[str]) -> Token:
        return Token("object", {"name": {"first": "", "last": ""}}, keys)

    schema = build_schema(keys=["name"])
    token = build_token(keys=["name"])


# Generated at 2022-06-14 14:52:17.931255
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.tokenize.tokens import Object

    schema = Schema(fields={"foo": String(), "bar": Integer()})
    json_value = {"foo": "hello"}
    token = Object(value=json_value)
    with pytest.raises(ValidationError) as e:
        validate_with_positions(validator=schema, token=token)

    url = "https://example.com/api.json"
    message = (
        f"Line 1, character 16:\n"
        f"The field 'bar' is required.\n"
        f"\n"
        f"<string>: Line 1, character 16:\n"
        f'{" " * 16}^'
    )
    assert str(e.value) == message

# Generated at 2022-06-14 14:52:27.646648
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.tokenize.util import make_token_tree

    token = make_token_tree()

    def test_field(token: Token) -> str:
        return validate_with_positions(token=token, validator=Field(required=True))

    def test_schema(token: Token) -> str:
        return validate_with_positions(token=token, validator=MySchema)

    with pytest.raises(ValidationError) as excinfo:
        test_field(token)

    assert excinfo.value.messages()[0].start_position == token.start
    assert excinfo.value.messages()[0].end_position == token.end

    token["bar"] = "foo"
    test_field(token)


# Generated at 2022-06-14 14:52:33.067961
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema

    class Person(Schema):
        name = Field(required=True)
        age = Field(type="integer")

    data = {"name": "Jane", "age": "42"}
    assert validate_with_positions(
        token=Token(value=data, start=None, end=None), validator=Person
    ) == data

# Generated at 2022-06-14 14:52:43.832881
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    from typesystem.tokenize.tokenize import tokenize

    class Age(typesystem.Integer):
        min_value = 0

    class Person(typesystem.Schema):
        name = typesystem.String()
        age = Age()

    text = "bob = {name: 'Bob', age: -10}"
    tokens = tokenize(text)
    token = tokens[3]
    assert token.value["age"] == -10
    with pytest.raises(ValueError) as error:
        validate_with_positions(token=token, validator=Person())
    error = error.value

# Generated at 2022-06-14 14:52:54.933987
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import TokenError
    from typesystem.types import Boolean
    from typesystem.exceptions import Error

    class MySchema(Schema):
        required_field = Boolean(required=True)
        not_required_field = Boolean(required=False)

    tokenizer = tokenize("{ 'required_field': True, 'not_required_field': 'oops' }")
    my_schema = MySchema()
    try:
        validate_with_positions(
            token=next(tokenizer), validator=MySchema()
        )
        assert False
    except TokenError as error:
        assert error.token.start.char_index == 38
        assert error.token.end.char_index == 47

# Generated at 2022-06-14 14:53:03.958965
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # type: ignore
    """Test positional validation errors."""
    from typesystem.tokenize.positional import PositionalSchema
    from typesystem.tokenize.tokens import (
        Dict,
        List,
        Scalar,
        Tuple,
    )  # type: ignore

    schema = PositionalSchema(
        {
            "a": [
                Scalar("a"),
                Dict({"b": [Scalar("b"), Dict({"c": [Scalar("c")]})],}),
            ],
            "d": [Scalar("d")],
        }
    )
    token = schema.tokenize("""{"a": "a", "d": "d"}""")

# Generated at 2022-06-14 14:53:13.684305
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.types import Integer
    from typesystem.tokenize import tokenize_string
    from typesystem.positions import Position, Range
    integer = Integer()
    token = tokenize_string("abc123").at("document")
    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=integer)
    error = pytest.raises(ValidationError).value
    assert error.messages()[0].start_position == Position(0, 0)
    assert error.messages()[0].end_position == Position(0, 3)
    assert error.messages()[0].text == '"abc123" is not a valid Integer'
    assert error.messages()[0].code == "invalid"

# Generated at 2022-06-14 14:53:22.948212
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.test_tokens import test_token
    from tests.test_validators import test_field

    field = test_field()
    error = None
    try:
        validate_with_positions(token=test_token(), validator=field)
    except ValidationError as e:
        error = e
    assert error is not None
    assert len(error.messages()) == 1
    assert error.messages()[0].code == "required"
    assert error.messages()[0].start_position.char_index == 6
    assert error.messages()[0].end_position.char_index == 6

# Generated at 2022-06-14 14:53:34.368831
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer, String  # type: ignore

    body = {
        "foo": {"bar": {"baz": 3}},
        "qux": [1, 2, "3", 4, 5],
        "quux": {"corge": {"grault": 6, "garply": "7"}},
    }
    token = Token.from_annotations(body)

    # Basic types
    assert validate_with_positions(token=token, validator=Integer) == 3
    assert token.body == body

    # Schema
    class FooSchema(Schema):
        bar = Integer
        baz = String

    foo_token = token.lookup(["foo"])

# Generated at 2022-06-14 14:53:43.778371
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.base import ValidationError
    from typesystem.fields import String
    from typesystem.tokenize.patterns import TokenType
    from typesystem.tokenize.tokens import Token

    # Test error production
    field = String()
    token = Token(
        type=TokenType.TOKEN,
        start=1,
        end=1,
        value={
            "key_1": "value_1",
            "key_2": "value_2",
            "key_3": "value_3",
        },
    )
    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as error:
        assert error.messages[0].text == "The field 'key_1' is required."

# Generated at 2022-06-14 14:54:54.017260
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "email": {"type": "string"},
        },
        "required": ["name"],
    }
    schema = Schema.from_structure(schema)
    data = ""
    token = Token.from_data(data)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)

    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.code == "required"
    assert message.index == ["name"]

# Generated at 2022-06-14 14:55:04.164401
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    from .db import create_token

    token = create_token(
        """\
    {
        "required": true,
        "name": "hello",
        "values": [
            "a"
        ]
    }
    """
    )

    required_field = String(required=True)
    values_field = String(choices=["a", "b", "c", "d"])

    class TestSchema(Schema):
        required = required_field
        name = String(min_length=3)
        values = values_field

    try:
        validate_with_positions(token=token, validator=TestSchema)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2

# Generated at 2022-06-14 14:55:09.130784
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pprint
    from typesystem.tokenize.parser.parser import Parser
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.base import TokenType
    from typesystem.fields import String

    parser = Parser()

    text = """{"key": "value", "key2": "value"}"""
    token = parser.parse(text)