

# Generated at 2022-06-14 14:45:22.637140
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, String

    class Address(Schema):
        city = String(required=True)
        state = String(required=True)
        zip = Integer(required=True)

    class Person(Schema):
        name = String(required=True)
        age = Integer(required=True)
        address = Address(required=True)

    schema = Person()

    schema.validate({})


# Generated at 2022-06-14 14:45:31.145582
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tests.tokens import tokenize

    def make_non_field_validator(index, code):
        class TestValidator(Schema):
            __slots__ = ()
            f1 = Field(str)
            f2 = Field(int)

            def validate(self, value):
                raise ValidationError(messages=[Message(index=index, code=code)])

        return TestValidator()

    # Test required field in top-level document
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=tokenize({"f1": "abc", "f2": 123}),
            validator=make_non_field_validator(index=["f3"], code="required"),
        )
    assert str(exc_info.value)

# Generated at 2022-06-14 14:45:37.284286
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.compatibility import text_type
    from typesystem.fields import Array, Boolean, Integer, String
    from typesystem.schemas import Object
    from typesystem.tokenize.tokens import ObjectToken
    from typesystem.tokenize.util import tokenize_json

    data = {
        "name": "John Doe",
        "age": 21,
        "lives": ["New York"],
        "interests": [{"name": "Golf", "level": 1}],
        "gender": True,
    }

    Person = Object.of(
        {
            "name": String,
            "age": Integer,
            "lives": Array[String],
            "interests": Array[Object.of({"name": String, "level": Integer})],
            "gender": Boolean,
        }
    )

# Generated at 2022-06-14 14:45:49.391481
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema

    class TestSchema(Schema):
        foo = Field(type="integer", required=True)

        def validate_foo(self, value):
            if value != 42:
                raise ValueError("Foo must be 42!")

    token = Token(
        {
            "foo": Token(value=43, start={'char_index': 4, 'line_index': 2}, end={'char_index': 5, 'line_index': 2}),
        },
        start={'char_index': 2, 'line_index': 2},
        end={'char_index': 6, 'line_index': 2},
    )

    schema = TestSchema()


# Generated at 2022-06-14 14:45:57.097402
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import NumberToken

    class Number(Field):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.add_validator("validator", self.validate_number)

        def validate_number(self, value):
            if value < 0:
                raise ValidationError("must be greater than zero")

    token = NumberToken(value=10, start=(1, 10), end=(1, 11))
    assert validate_with_positions(token=token, validator=Number()) == 10

    token = NumberToken(value=-1, start=(1, 10), end=(1, 11))

# Generated at 2022-06-14 14:46:06.235853
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem import fields

    schema = fields.Object(properties={"name": fields.String()})
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=tokenize("{}"),
            validator=schema
        )

    positional_messages = exc_info.value.messages
    assert len(positional_messages) == 1
    positional_message = positional_messages[0]
    assert positional_message.start_position.line == 1
    assert positional_message.start_position.char_index == 1

# Generated at 2022-06-14 14:46:15.843214
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer

    token = Token("foo", start=(1, 1), end=(1, 4))
    schema = {"foo": String(max_length=3)}
    validator = Schema(schema)

    try:
        validate_with_positions(token=token, validator=validator)
    except ValidationError as error:
        messages = error.messages()
        message = messages[0]
        assert message.code == "max_length"
        assert message.start_position.line_index == 1
        assert message.start_position.char_index == 1
        assert message.end_position.line_index == 1
        assert message.end_position.char_index == 4



# Generated at 2022-06-14 14:46:24.630238
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import datetime

    from typesystem.exceptions import ValidationError
    from typesystem.fields import Integer
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import (
        Collection,
        Date,
        DateTime,
        Element,
        Field,
        Object,
        String,
        Time,
    )

    class LocalizedString:
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            if isinstance(other, LocalizedString):
                return self.value == other.value
            else:
                return False

        def __repr__(self):
            return repr(self.value)


# Generated at 2022-06-14 14:46:35.686151
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize.parser import SchemaParser

    class TestSchema(Schema):
        a = Field(parse_error="custom error")
        b = Field(default="foo")

    parser = SchemaParser()
    schema = TestSchema()

    token = parser.parse("""
        {
            "a": 123,
            "b": 321,
            "c": 456
        }
    """)

    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1

        message = messages[0]
        assert message.text == "custom error"
        assert message.start_position.line_number == 2


# Generated at 2022-06-14 14:46:39.851029
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema.of(name=str)
    token = Token.of({"name": "foo"}, start={}, end={})
    validated_data = validate_with_positions(token=token, validator=schema)
    assert "name" in validated_data

# Generated at 2022-06-14 14:46:54.361697
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import Tokenize
    from typesystem.tokenize.tokens import Token

    raw = """
    {
        "title": "Add a group",
        "type": "object",
        "properties": {
            "group_name": {
                "type": "string",
                "description": "The name of your group",
                "required": true
            }
        }
    }
    """
    tokenize = Tokenize()
    token = tokenize.tokenize(raw=raw)

# Generated at 2022-06-14 14:47:05.103686
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import Basic, Integer
    from typesystem.schemas import Object, Schema


    class TestSchema(Schema):
        value = Integer(required=True)

    assert validate_with_positions(
        token=Token(start=(1, 1), end=(1, 7), value={"value": None}),
        validator=TestSchema,
    ) == TestSchema.validate({"value": None})

    try:
        validate_with_positions(
            token=Token(start=(1, 1), end=(1, 7), value={"value": None}),
            validator=TestSchema,
        )
    except ValidationError as error:
        messages = list(error.messages)


# Generated at 2022-06-14 14:47:14.611083
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import ujson
    from typesystem.tokenize import token_stream_from_json

    token = token_stream_from_json(
        ujson.loads(
            """
    {
        "id": 3,
        "name": "Jenkins",
        "address": {
            "line1": null,
            "town": "London"
        }
    }
    """
        )
    )
    validator = Field(required=True)

# Generated at 2022-06-14 14:47:26.306333
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.tokenize.tokenizer import tokenize

    class PersonSchema(Schema):
        name = Field(str, min_length=1)
        age = Field(int, min_value=1)

    # Verify that the error message contains start and end positions
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(
            token=tokenize(
                """
                {
                  name: null,
                  age: null,
                }
                """
            ),
            validator=PersonSchema(),
        )
    assert len(excinfo.value.messages()) == 2

    name_error = excinfo.value.messages()[0]
    assert name_error.start_position.line == 2
    assert name_error.start_position.char

# Generated at 2022-06-14 14:47:31.668753
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer

    class Thing(Schema):
        name = Integer()
        age = Integer()

    value = [{"name": "foo", "age": "bar"}]
    with pytest.raises(ValidationError):
        token = Token(value, start=Position(0, 0, 0), end=Position(1, 15, 15))
        validate_with_positions(token=token, validator=Thing())



# Generated at 2022-06-14 14:47:42.314183
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Raise an error when no fields have been provided
    schema = Schema({"name": {"type": "string"}, "age": {"type": "integer"}})
    token = Token({})
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    assert exc_info.value.messages[0].text == 'Expecting a dict, but found "{}" instead.'
    assert exc_info.value.messages[0].start_position.char_index == 0
    assert exc_info.value.messages[0].end_position.char_index == 1
    assert len(exc_info.value.messages) == 1



# Generated at 2022-06-14 14:47:49.286610
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # pylint:disable=redefined-outer-name
    import json
    from typesystem.field import make_field
    from typesystem.tokenize.tokenizer import make_token

    raw_data = json.dumps({"name": "scooby"})
    token = make_token(raw_data)

    schema = make_field(name="name")
    validate_with_positions(token=token, validator=schema)

# Generated at 2022-06-14 14:47:55.693271
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Boolean, Array, Integer, String

    schema = Array[String]
    token = Token.from_json([1, 2, 3])

    error = None
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as exc:
        error = exc

    assert error is not None
    assert error.messages() == [
        Message(
            text="Item 1 is not of a valid type.",
            code="invalid_type",
            index=(1,),
            start_position=token[1].start,  # type: ignore
            end_position=token[1].end,  # type: ignore
        )
    ]



# Generated at 2022-06-14 14:48:07.564491
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Array, Dict, String
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.tokens import ObjectToken
    from typesystem.tokenize.tokens import ArrayToken
    from typesystem.tokenize.tokens import KeyToken
    from typesystem.tokenize.tokens import ValueToken

    from typesystem.tokenize.positions import CharPosition

    token = Token(
        start=CharPosition(line=1, line_index=1, char_index=0),
        end=CharPosition(line=2, line_index=2, char_index=0),
    )

# Generated at 2022-06-14 14:48:19.900246
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(str)
        age = Field(int)

    token = Token("foo")

# Generated at 2022-06-14 14:48:34.702587
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import StringToken

    class ExampleSchema(Schema):
        field = Field(required=True)

    class ExampleField(Field):
        def validate(self, value, context=None):
            return value

    class OtherField(Field):
        def validate(self, value, context=None):
            raise ValidationError("Something went wrong.")

    def test(mock):
        token = mock.Mock(spec=StringToken)
        token.lookup = mock.Mock(side_effect=lambda *args, **kwargs: token)
        return token

    token = test(mock=mock)
    validate_with_positions(token=token, validator=ExampleSchema)
    token.lookup.assert_called_once_with(["field"])

    token.look

# Generated at 2022-06-14 14:48:39.519530
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema()
    field = schema.add_field("value", type="integer")
    value = "1"
    token = Token(value=value, index=("value",))
    assert validate_with_positions(token=token, validator=field) == 1

# Generated at 2022-06-14 14:48:42.514169
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import Context, Token
    from typesystem.tokenize.validators import validate_type

    context = Context()

# Generated at 2022-06-14 14:48:49.101030
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexers import JSONLexer
    from typesystem.tokenize.parsers import parse

    lexer = JSONLexer()
    token = parse(lexer.lex(text='{"foo": "bar"}'))
    token = token.lookup(["foo"])
    validate_with_positions(token=token, validator=Field(type="string"))
    token = token.lookup([])
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Field(type="string"))
    assert len(exc_info.value.messages()) == 1
    message = exc_info.value.messages()[0]
    assert message.start_position.char_index == 2
    assert message.end_position.char

# Generated at 2022-06-14 14:49:00.898161
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer

    from typesystem.tokenize import tokenize, TokenType

    from typesystem.util import ValidationError as ValidationError

    s = "hello\n  there\n   world"
    document = tokenize(s, token_type=TokenType.BLOCK)
    document_root = document.children[0]
    hello_token = document_root.children[0]
    hello_token.value = "A"

    s = "hello\n  there\n   world"
    document = document.pretty_print()
    assert "hello\n  there\n   world" == document
    assert "hello\n  there\n  *A* world" == hello_token.pretty_print()

    with pytest.raises(ValidationError) as exc_info:
        validate_with_

# Generated at 2022-06-14 14:49:07.108303
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.models import KeywordsSchema
    import json

    schema = KeywordsSchema()
    token = Token.from_native(json.loads('{"x": "foo"}'))
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=schema)
    assert exc.value.messages() == [
        Message(text='Keyword "y" is required.', code="required", index=(), start_position=Position(char_index=13, line_index=1, column_index=12), end_position=Position(char_index=19, line_index=1, column_index=19))
    ]

# Generated at 2022-06-14 14:49:19.108371
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class SimpleField(Field):
        def validate(self, value):
            if not isinstance(value, int):
                raise ValidationError()

    class PassThrough(Schema):
        pass_through = SimpleField()

    token = Token.create(
        start_line=1,
        start_char=0,
        end_line=1,
        end_char=3,
        key="pass_through",
        value="foo",
    ).freeze()

    try:
        validate_with_positions(token=token, validator=PassThrough)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.start_position.line == 1
        assert message.start_position.char_index == 0
        assert message.end_position.line == 1

# Generated at 2022-06-14 14:49:30.921738
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        value={"field": "value"},
        start=1,
        end=2,
    )
    token2 = Token(
        value={"field": {"field": "value"}},
        start=1,
        end=2,
    )
    schema = Schema(
        {
            "field": Field(int),
            "field2": Schema(
                {"field": Field(str, required=False)}, nested=True, required=False
            ),
        }
    )
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=schema)


# Generated at 2022-06-14 14:49:40.982739
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.jsonschema import tokenize_data
    from typesystem.tokenize.jsonschema import validate_with_positions
    from typesystem.schemas import Object
    from typesystem.fields import String
    from typesystem import ValidationError

    schema = Object(properties={"name": String()})
    try:
        validate_with_positions(
            token=tokenize_data({"age": 20}), validator=schema
        )
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "The field 'name' is required."

# Generated at 2022-06-14 14:49:49.034474
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.base import Validator
    from typesystem.tokenize.tokens import Object
    from typesystem.fields import String
    
    class MyValidator(Validator):
    
        def __init__(self):
            self.name = String(required=True)
        
        def validate(self, data: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
            return self.name.validate(data['name'])

    
    token = Object(
        None,
        [
            Token(None, 'name', 'Jane'),
            Token(None, 'age', 7)
        ]
    )
    validate_with_positions(token=token, validator=MyValidator())

# Generated at 2022-06-14 14:50:15.157760
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.exceptions import ErrorMessage

    class Test(Schema):
        foo = String(required=True)
        bar = Integer()

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=Token(
                {
                    "foo": "",
                    "bar": "",
                    "baz": "",
                    "qux": "",
                },
                start=(0, 0),
                end=(0, 0),
            ),
            validator=Test,
        )

    messages = exc_info.value.messages

# Generated at 2022-06-14 14:50:26.107637
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem import fields
    from typesystem.exceptions import ValidationError


    class Person(fields.Schema):
        """A person."""

        name = fields.String(required=True, max_length=20)
        age = fields.Integer()


    input = {
        "age": "a",
        "name": "Oscar",
    }
    token = Token.from_python_value(input)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Person())

    for m in exc_info.value.messages:
        if m.code == "invalid_type":
            assert m.start_position.char_index == 6
            assert m.end

# Generated at 2022-06-14 14:50:32.598276
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import io
    from typesystem.fields import Text
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import (
        Comment,
        EndOfObject,
        Newline,
        Separator,
        StartOfObject,
        Token,
    )

    from .test_python_extractor import PythonExtractor

    class PersonSchema(Schema):
        name = Text(required=True)

    content = '{"name": ""}'
    tokens = tokenize(content)

    schema = PersonSchema()
    try:
        schema.validate(tokens)
    except ValidationError as error:
        messages = [
            message
            for message in error.messages()
            if message.start_position.char_index == 16
        ]

# Generated at 2022-06-14 14:50:42.520209
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import types

    def test_function(*, value: types.String) -> None:
        pass

    schema = types.Schema(test_function)

    # This is a good test of a simple function
    body = "{'value': 'something'}"
    assert validate_with_positions(token=Token.parse(body), validator=schema) == None

    # This is a more complicated test of a Schema
    schema = types.Schema(
        {
            "fields": {
                "b": types.String(required=True),
                "c": types.String(required=True),
                "d": types.String(required=True),
                "e": types.String(required=True),
            }
        }
    )


# Generated at 2022-06-14 14:50:53.586766
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.fields import String

    field = String(required=True)

    try:
        validate_with_positions(token=tokenize("null").next(), validator=field)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "The field '' is required."
        assert message.code == "required"
        assert message.index == (0,)
        assert message.start_position.offset == 0
        assert message.start_position.line == 0
        assert message.start_position.column == 0
        assert message.start_position.char_index == 0
        assert message.end_position.offset == 4
        assert message.end_position.line == 0
        assert message.end_position.column == 4
       

# Generated at 2022-06-14 14:51:04.283601
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import fields  # noqa: F401
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token

    class TestSchema(Schema):
        foo = fields.Integer()

    # Required field
    source = "{}"
    schema = TestSchema()
    try:
        validate_with_positions(
            token=Token.parse(schema.fields["foo"], source), validator=schema
        )
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "The field 'foo' is required."
        assert message.code == "required"
        assert message.start_position == (1, 1, 1)
        assert message.end_position == (1, 1, 1)

    # Required nested field

# Generated at 2022-06-14 14:51:15.919321
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.primitives import Integer
    from typesystem.tokenize import tokenize

    token = tokenize({"a": 1, "b": "foo"})

    validator = {
        "a": Integer,
        "b": {"x": ["required", Integer], "y": ["required", Integer]},
    }

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=validator)

    messages = exc_info.value.messages()
    assert len(messages) == 2

    start_positions = [msg.start_position for msg in messages]
    assert start_positions == [
        (1, 0),
        (1, 2),
    ]

    end_positions = [msg.end_position for msg in messages]

# Generated at 2022-06-14 14:51:23.383711
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import Tokenizer
    from typesystem import Integer

    tokenizer = Tokenizer(
        {
            "type": "object",
            "properties": {
                "foo": {"type": "integer"},
                "bar": {"type": "integer"},
            },
        }
    )
    validator = tokenizer.tokenize()
    value = validate_with_positions(token=validator, validator=Integer)
    assert value == ""



# Generated at 2022-06-14 14:51:31.840816
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizer import tokenize
    from typesystem.fields import String, Integer
    from typesystem.schemas import Schema, fields

    class Person(Schema):
        name = fields.String(required=True)
        age = fields.Integer()

    input_string = "name:john age:30"

    token = tokenize(input_string)
    assert token["name"].start.char_index == 0
    assert token["name"].end.char_index == 7
    assert token["age"].start.char_index == 8
    assert token["age"].end.char_index == 11

    Person.validate(token)

    try:
        Person.validate(token.delete("name"))
    except ValidationError as error:
        message = error.messages()[0]


# Generated at 2022-06-14 14:51:42.261516
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.schemas import Schema
    from typesystem.fields import Integer
    from typesystem.exceptions import ValidationError as TypesystemValidationError

    class Person(Schema):
        age = Integer(required=True)

    token = tokenize('{"age": "yes"}'.encode())

    with pytest.raises(TypesystemValidationError) as exc_info:
        validate_with_positions(token=token, validator=Person())

    assert exc_info.value.messages == [
        Message(
            "Integer value expected.",
            start_position=token.value["age"].value.start,  # type: ignore
            end_position=token.value["age"].value.end,  # type: ignore
        )
    ]

# Generated at 2022-06-14 14:52:22.169333
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.positions import CharPosition

    class ExampleSchema(Schema):
        name = String(required=True)

    token = Token(
        "object",
        [
            Token("field", "name", position=CharPosition(line=1, char_index=4)),
            Token("value", "ben"),
        ],
        position=CharPosition(line=1, char_index=0),
    )

    try:
        validate_with_positions(token=token, validator=ExampleSchema)
    except ValidationError as error:
        assert len(error.messages()) == 1

# Generated at 2022-06-14 14:52:28.844693
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class ItemSchema(Schema):
        name = Field(type=str)

    class ListingSchema(Schema):
        title = Field(type=str)
        items = Field(type=ItemSchema)

    token = Token(
        {
            "title": "Jumbo Shrimp",
            "items": [
                {"name": "Shrimp, jumbo"},
                {"name": "Shrimp, medium"},
                {"name": "Shrimp, small"},
            ],
        }
    )
    schema = ListingSchema()
    assert validate_with_positions(token=token, validator=schema) == token.value

# Generated at 2022-06-14 14:52:40.355623
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse_string

    token = parse_string(
        '{"name": "joe", "age": 50, "joe_is_great": true, "hobbies": ["drinking beer", "eating candy"]}'
    )

    class Person(Schema):
        name = Field(type="string")
        age = Field(type="integer", minimum=0)
        joe_is_great = Field(type="boolean")
        hobbies = Field(type="array", items=Field(type="string"))

    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        messages = error.messages()
    assert len(messages) == 1
    assert messages[0].start_position.line_number == 0

# Generated at 2022-06-14 14:52:48.826159
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    import typesystem.tokenize
    import typesystem.tokenize.tokens
    import typesystem.tokenize.positions
    import typesystem.tokenize.positions.line_and_column

    class DummyField(typesystem.Field):
        def validate(self, value):
            return value

    field = DummyField()

    text = """
        name: Don Quixote
        age:
        """

    tokens = typesystem.tokenize.tokens(text)
    try:
        validate_with_positions(token=tokens[1], validator=field)
    except typesystem.ValidationError as error:
        assert len(error.messages) == 2
        message = error.messages[0]

# Generated at 2022-06-14 14:52:57.412895
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Item(Schema):
        name = StringField(required=True)

    class Data(Schema):
        items = ListField(Item)

    data = Data.parse_raw([])
    with raises(ValidationError) as exc_info:
        Data.validate_raw(data)
    assert exc_info.value.messages() == [
        Message(
            text="The field 'items' is required.",
            code="required",
            index=(),
            start_position=(0, 0),
            end_position=(0, 0),
        )
    ]


# Generated at 2022-06-14 14:53:05.454788
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.positions import Position

    class MyField(Field):
        def validate(self, value):
            raise ValidationError(
                [
                    Message(text="", code="required", index=[]),
                    Message(
                        text="", code="", index=["b"], end_position=Position(3, 1, 0)
                    ),
                    Message(text="", code="", index=["c"], end_position=Position(6, 1, 0)),
                ]
            )


# Generated at 2022-06-14 14:53:14.796149
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    raw_data = b"""
<xml>
    <id>1234</id>
    <name/>
</xml>
    """
    raw_data = raw_data.decode("utf-8")

    try:
        validate_with_positions(
            token=Token.parse(raw_data, "xml"),
            validator={
                "id": String(max_length=4),
                "name": String(required=True),
            },
        )
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2
        id_message, name_message = messages

        assert id_message.text == "Must have no more than 4 characters."
        assert id_message.code == "max_length"
        assert id_message

# Generated at 2022-06-14 14:53:25.390146
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import simple_tokenize

    class PersonSchema(Schema):
        name = Field(type="string")

    result = simple_tokenize('{"name": 123}')
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=result, validator=PersonSchema)

    assert exc_info.value.messages()[0] == Message(
        text="Expected string, found 123.",
        code="type_error.string",
        index=["name"],
        start_position=result.lookup(["name"]).start,
        end_position=result.lookup(["name"]).end,
    )

# Generated at 2022-06-14 14:53:36.385505
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import lex
    from typesystem.tokenize.tokens import Token
    from typesystem.json_schema import Integer, Object, String

    schema = Object(
        {
            "name": String(max_length=10),
            "age": Integer(minimum=18),
            "address": Object({"number": Integer()}),
        }
    )
    tokens = lex("""{"name": "Alex", "age": 17, "address": {"number": 42}}""")
    data = Token("root", tokens)

    try:
        value = validate_with_positions(token=data, validator=schema)
    except ValidationError as error:
        messages = error.messages()
    else:
        pytest.fail("Expected to raise validation error")

    assert len(messages)

# Generated at 2022-06-14 14:53:47.138239
# Unit test for function validate_with_positions
def test_validate_with_positions():
    def _test(
        *,
        token: Token,
        validator: typing.Union[Field, typing.Type[Schema]],
        valid: bool,
    ):
        try:
            validate_with_positions(token=token, validator=validator)
        except ValidationError:
            assert not valid
        else:
            assert valid

    from typesystem.tokenize.parser import parse_string
    from typesystem.fields import String
    from typesystem.schemas import Object

    class Person(Object):
        name: String

    token = parse_string("{ 'name': 'John' }")
    _test(token=token, validator=Person, valid=True)

    token = parse_string("{ 'name': 1 }")

# Generated at 2022-06-14 14:54:58.299166
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import FieldToken, ObjectToken

    from . import schema_validator

    schema = schema_validator({"required": ["name", "age"]})

    payload = ObjectToken(
        {"name": FieldToken("Dan"), "age": FieldToken(27)},
        start=Position(filename="example.txt", line=1, char_index=1),
        end=Position(filename="example.txt", line=3, char_index=0),
    )
    validate_with_positions(token=payload, validator=schema)

    # TODO: Fix error positions.


# Generated at 2022-06-14 14:55:06.343377
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize_json
    from typesystem.tokenize.tokens import Token

    from .test_tokenizer import data

    from typesystem.fields import Integer, String

    class Person(Schema):
        name = String(required=True)
        age = Integer(required=True)

    tokens = list(tokenize_json(data))
    token = Token(tokens)
    field = Person.fields["name"]

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=field)

    message = exc.value.messages[0]
    assert message.text == 'The field "name" is required.'
    assert message.start_position.line_number == 6
    assert message.start_position.line_index == 0

# Generated at 2022-06-14 14:55:13.363917
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String
    from typesystem.tokenize.tokens import Token

    token = Token(
        value={"bar": "foo"},
        start={"line_no": 1, "char_index": 0},
        end={"line_no": 2, "char_index": 3},
    )

    token = token.get_attribute_token("bar")

    field = String(required=True)
    validate_with_positions(token=token, validator=field)