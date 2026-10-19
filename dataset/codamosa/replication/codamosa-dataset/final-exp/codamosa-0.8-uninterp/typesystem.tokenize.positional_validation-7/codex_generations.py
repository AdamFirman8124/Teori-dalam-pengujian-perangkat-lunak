

# Generated at 2022-06-14 14:45:23.292139
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import pytest
    from typesystem.fields import Array, Dictionary
    from typesystem.schemas import Schema
    from typesystem.tokenize.context import Context
    from typesystem.tokenize.tokens import Tokenizer

    class User(Schema):
        username = Field(type=str, required=True)
        email = Field(type=str, required=True)

    class Event(Schema):
        name = Field(type=str, required=True)
        users = Array(type=User, required=True)


# Generated at 2022-06-14 14:45:34.756067
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.parse import parse
    from typesystem.tokenize.lex import string_to_tokens
    from typesystem.tokenize.positions import serialize_positions

    # Set up the validator
    class PersonSchema(typesystem.Schema):
        name = typesystem.String(min_length=1, max_length=10)

    # Create a dummy lexer, parser and tokenizer
    class DummyLexer(object):
        def __init__(self, tokens):
            self.tokens = tokens

        def lex(self, text):
            for token in self.tokens:
                yield token

    class DummyParser(object):
        def __init__(self, start):
            self.start

# Generated at 2022-06-14 14:45:46.358182
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, String
    from typesystem.tokenize import Tokenizer

    class MySchema(Schema):
        name = String(required=True)
        age = Integer()

    tokenizer = Tokenizer(tokenize_types=True)
    tokens = tokenizer.tokenize("""
        {
            "name": "Joe",
            "age": "100",
        }
    """)
    # Loosen our optional requirements for unit testing
    # pyre-fixme[16]: `Token` has no attribute `lookup`.
    tokens.lookup = lambda x: tokens

# Generated at 2022-06-14 14:45:53.524337
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class UserSchema(Schema):
        name = Field(str)
        signup_date = Field(str)

    data = {"name": "Bob"}
    token = Token.from_data(data, signup_date=None)

    with pytest.raises(ValidationError) as error_info:
        validate_with_positions(token=token, validator=UserSchema)

    assert (
        error_info.value.args[0]
        == "The field 'signup_date' is required at line 1, column 9."
    )

# Generated at 2022-06-14 14:46:03.771032
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import parse

    class Item(Schema):
        title = Field(required=True)
        is_done = Field()

    class TodoList(Schema):
        description = Field(required=True)
        items = Field(types=Item, repeated=True)

    data = {
        "description": "My Todo List",
        "items": [{"is_done": True}],
    }
    token = parse(data)

    try:
        validate_with_positions(token=token, validator=TodoList)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2

        title_message = messages[0]
        assert title_message.start_position.line_index == 2

# Generated at 2022-06-14 14:46:13.935070
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.serialization.loaders import TokenLoader  # type: ignore
    from typesystem.schemas import Object

    class Person(Object):
        fields = {
            "name": {"type": "string"},
            "age": {"type": "integer"},
        }

    class Article(Object):
        fields = {
            "author": {"type": Person},
            "body": {"type": "string"},
        }

    tokens = TokenLoader.load('{"author": { "name": 42 } }')
    try:
        validate_with_positions(token=tokens, validator=Article)
    except ValidationError as error:
        [message] = error.messages()
        assert message.text == "Invalid type. Expected string, received integer."
        assert message.start_position.line_number == 1


# Generated at 2022-06-14 14:46:23.441135
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.base import serialize_errors

    # Create a simple field-based validator.
    class Validator(Field):
        def __init__(self):
            super(Validator, self).__init__(required=True)

        def validate(self, value):
            if value != "foo":
                raise ValidationError("Value must be foo.")

    # Create a context.
    class Position:
        def __init__(self, line, line_index, char_index):
            self.line = line
            self.line_index = line_index
            self.char_index = char_index

    context = [
        (Position(1, 0, 0), ""),
        (Position(2, 1, 0), ""),
        (Position(3, 2, 0), ""),
    ]

    # Create a token

# Generated at 2022-06-14 14:46:34.618129
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.structures import (
        Struct,
        List,
        String,
        Integer,
    )

    schema = Struct(properties={
        "name": String(),
        "address": Struct(properties={
            "street": String(),
            "city": String(max_length=2),
        })
    })
    token = Token.parse({
        "name": "John Doe",
        "address": {
            "street": "Anywhere St. 17",
        }
    })
    with pytest.raises(ValidationError) as exc:
        schema.validate(token.value)

# Generated at 2022-06-14 14:46:44.043226
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Schema, fields
    from typesystem.tokenize import Tokenizer

    schema = Schema(
        {
            "id": fields.Integer(),
            "name": fields.String(),
            "friends": fields.Array(items=fields.Object({"id": fields.Integer()})),
        }
    )
    tokenizer = Tokenizer()
    token = tokenizer.tokenize('{"id": 1, "name": "Tommaso"}')

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=schema)


# Generated at 2022-06-14 14:46:54.546515
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        name="something",
        start=Position(line=1, column=1, char_index=0),
        end=Position(line=1, column=10, char_index=10),
    )

    class Something(Schema):
        value = Field()

    try:
        validate_with_positions(token=token, validator=Something)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field 'value' is required.",
                code="required",
                index=("value",),
                start_position=Position(line=1, column=1, char_index=0),
                end_position=Position(line=1, column=10, char_index=10),
            )
        ]

# Generated at 2022-06-14 14:47:08.877220
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import marshmallow as mm
    
    class MessageSchema(mm.Schema):
        content = mm.String(required=True)
        author = mm.String(required=True)
        created_at = mm.DateTime()

    def test_missing_required_field_no_extra():
        data = {"author": "Monty"}
        with pytest.raises(mm.ValidationError) as exc_info:
            MessageSchema().load(data)
        error = exc_info.value
        assert error.messages == {"content": ["Missing data for required field."]}

    def test_missing_required_field_with_extra():
        data = {"author": "Monty", "extra": "data"}

# Generated at 2022-06-14 14:47:18.478457
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.inputs import String
    from typesystem.schemas import Schema
    from typesystem.tokenize import Token
    from typesystem.tokenize.errors import TokenizeError


# Generated at 2022-06-14 14:47:24.761133
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    from typesystem.tokenize import tokenize_json

    json = r"""{
   "field1": 1,
   "missing_field": "moo"
}"""

    class MySchema(typesystem.Schema):
        field1 = typesystem.Integer(required=True)
        field2 = typesystem.Integer(required=True)
        field3 = typesystem.Integer(required=True)

    tokens = tokenize_json(json)
    token = tokens[0]

    error = None
    try:
        validate_with_positions(token=token, validator=MySchema)
    except ValidationError as error:
        pass

    assert error.messages()[0].start_position.char_index == 17
    assert error.messages()[1].start_position.char_index

# Generated at 2022-06-14 14:47:33.174411
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.base import Tokenize

    from .fixtures.tokenize import (
        test_tokenize_object,
        test_tokenize_array,
        test_tokenize_string,
        test_tokenize_number,
    )

    tokenize = Tokenize()
    tokenize.register("object", test_tokenize_object)
    tokenize.register("array", test_tokenize_array)
    tokenize.register("string", test_tokenize_string)
    tokenize.register("number", test_tokenize_number)

    assert validate_with_positions(
        token=tokenize.tokenize("[{}]"), validator=[{"a": int}]
    ) == [{"a": 0}]

    with pytest.raises(ValidationError) as excinfo:
        validate

# Generated at 2022-06-14 14:47:43.743868
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema(fields={"age": Field(type=int)})
    value = {"age": "24"}
    token = Token(
        value=value,
        start={"line": 1, "column": 1},
        end={"line": 1, "column": 7},
    )
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        expected = [
            Message(
                text="The field 'age' is required.",
                code="required",
                index=["age"],
                start_position={"line": 1, "column": 1},
                end_position={"line": 1, "column": 7},
            )
        ]
        assert error.messages() == expected



# Generated at 2022-06-14 14:47:55.073102
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer
    from typesystem.tokenize import parse_token

    token_value = parse_token(
        b"\n\n\n\n    \n\n\n\n\n\n  \n\n\n\n\n\n\n\n\n\n\n{}",
    )

    validator = Integer(required=True)
    try:
        validate_with_positions(token=token_value, validator=validator)
    except ValidationError as error:
        msg = error.messages()[0]
        assert msg.start_position.byte_index == 47
        assert msg.end_position.byte_index == 48
        assert msg.start_position.char_index == 0
        assert msg.end_position.char_index == 1
        assert msg

# Generated at 2022-06-14 14:48:07.060347
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.test_tokenize import tokenize

    from typesystem import fields

    field_token = tokenize('[{"id": 1, "title": "A"}]')[0].value[0]
    field = fields.Field()
    field.name = "id"

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=field_token, validator=field)
    assert len(error.value.messages) == 2

    assert error.value.messages[0].text == "The field id is required"
    assert error.value.messages[0].start_position.line == 1
    assert error.value.messages[0].start_position.char_index == 4

    assert error.value.messages[1].text == "The field id is required"
   

# Generated at 2022-06-14 14:48:19.352583
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer

    class Address(Schema):
        street = String()
        number = Integer()

    class Person(Schema):
        name = String(required=True)
        age = Integer(required=True)
        address = Address()

    person = Person()
    value = {"name": "Foo", "age": "Bar"}

    try:
        person.validate(value)
    except ValidationError as error:
        messages = [
            Message(
                text="The field 'age' is required.",
                code="required",
                index=("age",),
            ),
            Message(
                text="Value must be of type 'integer'",
                code="invalid_type",
                index=("age",),
            ),
        ]

# Generated at 2022-06-14 14:48:29.601609
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.text import format_position
    from typesystem.fields import String

    text = '{"foo": "bar"}'

    token = Token.from_text(text=text, start_position=format_position(0, 0))
    token.parse()
    assert token.start.char_index == 0
    assert token.end.char_index == len(text)
    assert validate_with_positions(token=token, validator=String) == text

    field_token = token.lookup(["foo"])
    assert field_token.start.char_index == 7
    assert field_token.end.char_index == 14
    assert validate_with_positions(token=field_token, validator=String) == "bar"



# Generated at 2022-06-14 14:48:36.420852
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.primitives import String
    token = Token(
        value={
            "name": "",
            "count": "three",
            "tags": ["latest", "great"],
        }
    )
    validator = Schema(
        {
            "name": String(min_length=3),
            "count": String(min_length=3, max_length=4),
            "tags": String(min_length=3, max_length=4),
        }
    )
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=validator)

    messages = excinfo.value.messages()
    assert messages[0].text == "The field 'name' is required."
    assert messages[0].start_

# Generated at 2022-06-14 14:48:46.267659
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokenize

    class Foo(Schema):
        field = Field(required=True, format="ipv4")

    source = b"{}"
    tokens = tokenize(source)
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=tokens[0], validator=Foo)
    msg = excinfo.value.messages[0]
    assert msg.text == 'The field "field" is required.'



# Generated at 2022-06-14 14:48:58.703320
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Author(Schema):
        name = Field(type="string")
        age = Field(type="integer")

    class BookSchema(Schema):
        name = Field(type="string")
        author = Field(type=Author)

    book = {
        "name": "The Stand",
        "author": {
            "name": "Stephen King",
            "age": 70
        }
    }

    BookSchema.validate(book)

    del book["author"]["age"]


# Generated at 2022-06-14 14:49:06.613040
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String
    from typesystem.tokenize.tokenize import tokenize
    from typesystem.tokenize.positions import EndPosition
    from typesystem.tokenize.positions import StartPosition

    token = tokenize(
        schema=String,
        value="""{"name": ""}""",
        start_position=StartPosition(
            file_path="path/to/file.json",
            line_index=0,
            line="{}",
            char_index=0,
        ),
        end_position=EndPosition(
            file_path="path/to/file.json",
            line_index=0,
            line="{}",
            char_index=3,
        ),
    )
    error = None

# Generated at 2022-06-14 14:49:18.653278
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import yaml

    from typesystem.fields import String, Integer, Array
    from typesystem.tokenize.tokens import Token, TokenType
    from typesystem.tokenize.errors import TokenizerError

    schema = {"type": "object", "properties": {"x": {"type": "integer"}}}


# Generated at 2022-06-14 14:49:30.458525
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class Person(Schema):
        name = Field(type="string")
        age = Field(type="integer")

    validate = lambda x: validate_with_positions(token=x, validator=Person)

    validate(Token('{"name":"Alice", "age":"38"}'))

    with pytest.raises(ValidationError) as exc_info:
        validate(Token('{"name":"Alice", "age": "foobar"}'))


# Generated at 2022-06-14 14:49:42.053914
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexer import lex
    from typesystem.tokenize.parser import parse

    schema = Schema(
        {"name": Field(required=True), "age": Field(required=True)}
    )
    source = """
    name: John
    age: 98
    """
    tokens = lex(source=source)
    root_token = parse(tokens=tokens)
    # The `age` field is required.
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=root_token, validator=schema)

    assert len(exc_info.value.messages) == 1
    assert exc_info.value.messages[0].text == "The field 'age' is required."
    assert exc_info.value.mess

# Generated at 2022-06-14 14:49:49.619362
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    schema = Schema({"foo": String(), "bar": String()}, required=["foo", "baz"])
    token = Token({"foo": "x", "bar": "y"}, start=(0, 0), end=(1, 0))
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        assert len(error.messages) == 1

        message = error.messages[0]
        assert message.code == "required"
        assert message.index == ("baz",)
        assert message.start_position == (0, 0)
        assert message.end_position == (1, 0)

# Generated at 2022-06-14 14:49:55.187235
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class TestSchema(Schema):
        foo = Field(required=True)

    text = '{"foo": "bar"}'
    token = tokenize(text)
    validate_with_positions(token=token, validator=TestSchema)



# Generated at 2022-06-14 14:50:02.129433
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class TestSchema(Schema):
        name = Field(str, max_length=10)

    # Validation errors
    with pytest.raises(ValidationError):
        value = Token("root", {"name": "Flavio"})
        validate_with_positions(token=value, validator=TestSchema())

    # Validation success
    value = Token("root", {"name": "Flavio"})
    assert validate_with_positions(token=value, validator=TestSchema(required=False))

# Generated at 2022-06-14 14:50:10.753243
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from typesystem_json_schema import JSONSchema, typesystem_schema

    SchemaClass = typesystem_schema(JSONSchema)
    type = JSONSchema({"type": "object", "properties": {"hello": {"type": "string"}}})
    schema = SchemaClass(type=type)

    from typesystem_json_schema import parse, tokenize

    tokens = tokenize('{"hello": ""}')
    validate_with_positions(token=parse(tokens), validator=schema)



# Generated at 2022-06-14 14:50:27.857824
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.json_schema import String, Integer, Array
    # define a test JSON string that is a part of an input
    json_string = """
    {
      "name": "nucleus",
      "number": "7",
      "invalid_number": "foo",
      "numbers": ["1", "2", "3"],
      "wrong_numbers": ["1", 2, 3],
      "extra_properties": {
        "one": 1,
        "two": 2,
        "three": 3
      }
    }
    """
    # use the function `tokenize` from `typesystem.tokenize` to get a Token object
    token = tokenize(json_string)
    # define a Schema class, and use it to call the function `validate`

# Generated at 2022-06-14 14:50:38.105340
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import tokenize_string

    class CustomSchema(Schema):
        name = Field(type="string")
        age = Field(type="number")

    token = tokenize_string('{"name": "joe", "age": "blah"}')
    # Validate with CustomSchema and return ValidationError
    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=CustomSchema)
    assert error.value.messages()[0].start_position == (1, 13)
    assert error.value.messages()[0].end_position == (1, 18)

# Generated at 2022-06-14 14:50:45.949062
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.primitives import String
    from typesystem.tokenize import tokenize_string
    from typesystem.tokenize.exceptions import TokenizeError

    string_field = String(min_length=2)
    input_ = '{"name":"Bob"}'
    tokens = tokenize_string(input_)
    assert validate_with_positions(
        token=tokens[1], validator=string_field
    ) == "Bob"

    with pytest.raises(TokenizeError) as excinfo:
        validate_with_positions(token=tokens[2], validator=string_field)
    assert excinfo.value.messages[0].text == "Expected a string."


# Generated at 2022-06-14 14:50:51.446651
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import yaml
    from typesystem.fields import Array, Integer

    class Complex(Schema):
        integers = Array[Integer]()

    yaml_str = "integers: [1, '2']\n"
    assert validate_with_positions(
        token=Token.from_yaml(yaml_str), validator=Complex
    ) == {"integers": [1, 2]}



# Generated at 2022-06-14 14:51:02.693668
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Integer, Boolean

    # A simplistic JSON schema.
    class ContactSchema(Schema):
        id = Integer()
        first_name = String(required=True)
        last_name = String(required=True)
        address = String(required=True)
        state = String(required=True)
        zipcode = String(required=True)
        is_active = Boolean()

    from typesystem.tokenize import tokenize

    data = tokenize('{"id": 1234, "is_active": true}')
    try:
        ContactSchema().validate(data)
    except ValidationError as exception:
        assert len(exception.messages()) == 4

        first_name, last_name, address, state = exception.messages()
        assert first_name.code == "required"
       

# Generated at 2022-06-14 14:51:15.263873
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    SimpleSchema = Schema.of({"name": Field(str), "age": Field(int)})

    tokens = tokenize(
        """
        {
            "name": "Alice",
            "age": "123",
        }
    """
    )

    # Initially, the age value is not valid.
    value = validate_with_positions(token=tokens.root, validator=SimpleSchema)
    assert value == {"name": "Alice", "age": 123}

    # Now we make the age value invalid.
    tokens = tokenize(
        """
        {
            "name": "Alice",
            "age": undefined,
        }
    """
    )
    with pytest.raises(ValidationError) as error:
        validate_with_pos

# Generated at 2022-06-14 14:51:25.383397
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Base:
        a = Field()

    class Derived(Base):
        b = Field()

    token_list = [
        Token(value={"a": "value"}, start=Position(0, 0, 0), end=Position(0, 0, 0))
    ]
    token = token_list[0]

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=Derived)

    excinfo.match(
        r"The field b is required\.",
        flags=re.MULTILINE | re.DOTALL | re.UNICODE,
    )



# Generated at 2022-06-14 14:51:33.441247
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse
    from typesystem.tokenize.tokens import Token

    token = parse("""\
        {
            "foo": "bar",
            "baz": []
        }""")

    class MySchema(Schema):
        foo = Field(type=str)
        baz = Field(type=list)

    validate_with_positions(token=token, validator=MySchema)

    class MySchema(Schema):
        foo = Field(type=int)
        baz = Field(type=list)

    try:
        validate_with_positions(token=token, validator=MySchema)
    except ValidationError as error:
        token = token.lookup(error.messages()[0].index[:-1])
        assert error.mess

# Generated at 2022-06-14 14:51:41.931921
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import String
    from typesystem.structures import Dict

    token = Token(
        value={
            "text": "hello",
            "nested": "",
            "another_nested": [
                {"text": "world!"},
                {"text": "hello world!"},
                {"text": "world!"},
            ],
        },
        start=None,
        end=None,
    )


# Generated at 2022-06-14 14:51:53.278344
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import BooleanToken, IntegerToken
    from typesystem.tokenize.tokens import NullToken, ObjectToken
    from typesystem.fields import Boolean, Integer
    from typesystem.schemas import Object
    from typesystem.tokenize.exceptions import TokenizeError

    schema = Object(properties={"name": Boolean(), "age": Integer()})

    # Test with valid input
    source = "name: true age: 42"
    root_token = ObjectToken.parse(source)
    assert validate_with_positions(token=root_token, validator=schema) == {
        "name": True,
        "age": 42,
    }

    # Test with invalid input
    source = "name: null age: 42"
    root_token = ObjectToken.parse(source)

# Generated at 2022-06-14 14:52:16.174883
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem.types as ts
    from typesystem.tokenize.tokens import ObjectToken
    from typesystem.tokenize.parse import parse

    from typesystem.tokenize.position import (
        Position,
        LinePosition,
        PointPosition,
        CharPosition,
    )

    # Parse a text
    nested = parse(
        """
        {
            "name": {
                "first": "Tom",
                "last": "Smith"
            }
        }
    """
    )

    # Define a schema with a nested field
    class User(object):
        name = ts.Object(fields={"first": ts.String(), "last": ts.String()})  # type: ignore

    # Wrap it in a Token to make it easier to work with

# Generated at 2022-06-14 14:52:23.807554
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Tokens
    from typesystem.tokenize.tokens import String
    from typesystem.fields import String as StringField
    from typesystem.schemas import Schema

    class MySchema(Schema):

        field_1 = StringField(min_length=3)
        field_2 = StringField(max_length=3)

    tokens = Tokens(
        [
            String(
                value="field_1",
                start={"line": 1, "column": 1},
                end={"line": 1, "column": 8},
            ),
            String(
                value="field_2",
                start={"line": 1, "column": 10},
                end={"line": 1, "column": 17},
            ),
        ]
    )

# Generated at 2022-06-14 14:52:34.348978
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Position:
        def __init__(self, index: int):
            self.char_index = index

    def assert_char_index(m: Message, expected_index: int) -> None:
        assert m.start_position.char_index == expected_index
        assert m.end_position.char_index == expected_index

    text = "hello world"
    token = Token("", text, start=Position(0), end=Position(1))
    validator = Field(type="string", min_length=5)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=validator)

    messages = exc_info.value.messages()
    assert len(messages) == 1
    message = messages[0]

# Generated at 2022-06-14 14:52:39.033493
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from json import loads
    from typesystem.tokenize.core import parse as tokenize
    from typesystem.tokenize.tokens import ObjectToken
    from typesystem.json_schema import JSONSchema

    data = loads(
        """{
            "one": 1,
            "two": [1,2,3],
            "three": "str"
        }"""
    )
    root_token = tokenize(data)
    schema = {
        "one": {"type": "integer"},
        "two": {"type": "array", "items": {"type": "integer"}},
        "three": {"type": "integer"},
    }

    json_schema = JSONSchema(schema)
    try:
        json_schema.validate(data)
    except Exception:
        pass

# Generated at 2022-06-14 14:52:48.050462
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import typesystem
    from typesystem.tokenize import tokenize

    # Create a tokenizer, and use it to tokenize a JSON string
    tokenizer = tokenize.Tokenizer()
    tokens = tokenizer.tokenize(json.dumps({"foo": "a"}))

    # Validate the JSON string using the provided validator
    validator = typesystem.Dictionary({"foo": typesystem.String()})
    value = validate_with_positions(token=tokens[0], validator=validator)

    # Check that the value is correct
    assert value == {"foo": "a"}

    # Check that the validation error contains a positional message

# Generated at 2022-06-14 14:52:58.213929
# Unit test for function validate_with_positions
def test_validate_with_positions():
    try:
        validator = Field(name="a", type="string")
        validate_with_positions(token=Token(value={}), validator=validator)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "The field 'a' is required."
        assert message.code == "required"
        assert message.index == ["__root__", "a"]
        assert message.start_position.line_number == 0
        assert message.start_position.char_index == 2
        assert message.end_position.line_number == 0
        assert message.end_position.char_index == 2
    else:
        assert False, "should have raised ValidationError"

# Generated at 2022-06-14 14:53:05.913493
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer, Object
    from typesystem.tokenize.tokens.base import Index
    from typesystem.descriptors import Descriptor

    class MyObject(Schema):
        foo = String()

    token = Token(
        name="",
        value={
            "foo": "Hello"
        },
        start=Index(1, 0, 1, 0),
        end=Index(1, 40, 1, 40),
        tokens=[
            Token(
                name="foo",
                value="Hello",
                start=Index(1, 1, 1, 6),
                end=Index(1, 7, 1, 12),
                tokens=[],
            )
        ],
    )
    result = validate_with_positions(token=token, validator=MyObject)

# Generated at 2022-06-14 14:53:15.017252
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Check that errors are represented properly.
    from pygments import lex
    from pygments.lexers import HtmlLexer
    from typesystem.schemas import Schema
    import typesystem

    class UserSchema(Schema):
        first_name = typesystem.String(required=True)
        last_name = typesystem.String(required=True)

    sample_code = """
    <html>
        <head>
            <title>Hello world</title>
        </head>
        <body>
            <main>
                <h1>Hello {{ name }}</h1>
            </main>
        </body>
    </html>
    """

    tokens = list(lex(sample_code, HtmlLexer()))
    user_token = tokens[3]

# Generated at 2022-06-14 14:53:26.780166
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.tokenize.tokens import DictToken, ListToken, ValueToken
    from typesystem.schemas import Schema
    from typesystem.fields import Field

    schema = Schema(
        {
            "foo": Field(type="string"),
            "bar": Field(type="string", required=True),
            "baz": Field(type="integer", required=True),
        }
    )
    schema.tokenize("""
    foo: "hello"
    bar: "world"
    baz: 42
    """)
    token = schema.tokenize("""
    foo: "hello"
    """)

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=schema)

# Generated at 2022-06-14 14:53:37.524728
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokenize_json
    from typesystem.tokenize.tokens import Token

    class User(Schema):
        id = "uuid"
        name = "string"
        admin = "boolean"

    token = Token(
        parse_value=tokenize_json, value={"id": "1234", "name": "Erin", "admin": "true"}
    )
    try:
        User.validate(token.value)
    except ValidationError as error1:
        try:
            validate_with_positions(token=token, validator=User)
        except ValidationError as error2:
            assert error1.messages() == error2.messages()

# Generated at 2022-06-14 14:54:15.847615
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Structure, Array

    from typesystem.tokenize.json import load
    from typesystem.tokenize.positions import serialize

    class Person(Structure):
        name = Field(type="string")
        age = Field(type="integer")

    class Table(Structure):
        header = Field(type="string")
        rows = Field(type=Array(of=Person))

    token = load('{"header": "h", "rows":[{"name":"a","age":1}]}')
    try:
        validate_with_positions(token=token, validator=Table())
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        message = messages[0]
        assert message.text == "The field 'age' is required."
       

# Generated at 2022-06-14 14:54:25.990948
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Token

    def assert_message(message, text, code, index, start_position, end_position):
        assert message.text == text
        assert message.code == code
        assert message.index == index
        assert message.start_position == start_position
        assert message.end_position == end_position

    from typesystem.fields import String, Integer


# Generated at 2022-06-14 14:54:34.283567
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema.of({"x": Field(required=True)})

    try:
        validate_with_positions(validator=schema, token={"x": "", "y": ""})
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "The field 'x' is required."
        assert message.code == "required"
        assert message.index == ("x",)
        assert message.start_position.line_number == 1
        assert message.start_position.char_number == 5
        assert message.end_position.line_number == 1
        assert message.end_position.char_number == 6

# Generated at 2022-06-14 14:54:41.998947
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem import Integer

    result = validate_with_positions(
        token=tokenize("foo: 123"), validator=Integer(required=True)
    )
    assert result == 123

    result = validate_with_positions(
        token=tokenize("foo: 123"), validator=Integer(required=False)
    )
    assert result == 123

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=tokenize("foo: 123"), validator=Integer(required=True)
        )

    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.text == "The field 'foo' is required."

# Generated at 2022-06-14 14:54:47.283639
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.base import Token
    from typesystem.schemas import Schema
    from typesystem.fields import String
    
    class Foo(Schema):
        foo = String()
    
    schema = Foo()
    
    token = Token(
        value={
            "foo": {
                "type": "object",
                "properties": {},
            },
        },
        path=["foo"],
    )
    
    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=schema)

# Generated at 2022-06-14 14:54:53.051193
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object, String

    class TestSchema(Object):
        foo = String()
        bar = String()

    data = {"foo": "hello"}
    error = TestSchema.validate(data)
    positional_errors = validate_with_positions(
        token=Token.from_value(data), validator=TestSchema
    )

    assert positional_errors == error

# Generated at 2022-06-14 14:55:03.392291
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer, String
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize import Tokenizer

    from .helpers import assert_message

    tokenizer = Tokenizer()
    field = Integer(required=True, minimum=10)
    token = Token(root_value={"foo": [1, 2, 3]}, value=3, index=[0])

    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as error:
        assert len(error.messages()) == 1
        assert_message(message=error.messages()[0], code="minimum", text="1 is less than 10.")

    field = Integer(required=True, minimum=10)

# Generated at 2022-06-14 14:55:14.687250
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token({"hello": "world", "foo": {"bar": 123}})
    schema = Schema(
        {"hello": str, "foo": {"bar": int}},
        options={"coerce": True, "unknown": "skip"},
    )
    value = validate_with_positions(token=token, validator=schema)
    assert value == {"hello": "world", "foo": {"bar": 123}}

    token = Token({"hello": "world", "foo": {"baz": 123}})
    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=schema)
    assert len(exc.value.messages) == 2
    assert ["baz"] == exc.value.messages[0].index