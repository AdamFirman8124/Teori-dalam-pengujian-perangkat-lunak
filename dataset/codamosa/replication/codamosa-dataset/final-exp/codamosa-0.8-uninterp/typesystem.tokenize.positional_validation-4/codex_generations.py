

# Generated at 2022-06-14 14:45:19.585108
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class ExampleSchema(Schema):
        name = Field(type=str)

    token = Token(
        start={"line_index": 1, "char_index": 0},
        end={"line_index": 1, "char_index": 5},
        value={"name": ""},
    )

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=ExampleSchema())

    message = exc_info.value.messages[0]

    assert message.code == "required"
    assert message.text == "The field 'name' is required."
    assert message.index == ("name",)
    assert message.start_position == {"line_index": 1, "char_index": 0}

# Generated at 2022-06-14 14:45:29.026430
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Boolean, String
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.exceptions import TokenizationError

    class User(Schema):
        first_name = String(required=True)
        last_name = String(required=True)
        is_active = Boolean(required=True)

    with pytest.raises(TokenizationError) as exc_info:
        validate_with_positions(
            token=tokenize("""{first_name: "John", last_name: 1234}""")[-1],
            validator=User,
        )
    error = exc_info.value
    assert len(error.messages) == 2

# Generated at 2022-06-14 14:45:37.059885
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json

    class PersonSchema(Schema):
        name = Field(str, required=True)
        age = Field(int, required=False)
        occupation = Field(str, required=True)

    schema = PersonSchema()
    data = {"name": "Ernest", "age": "a", "occupation": "z"}
    token = Token(json.dumps(data))
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 2
        for message in messages:
            if message.code == "required":
                assert message.text == "The field 'occupation' is required."
            else:
                assert message.text == "Value must be an integer number."

# Generated at 2022-06-14 14:45:49.069053
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        name="name",
        value="{}",
        start=Position(line_index=1, char_index=10),
        end=Position(line_index=1, char_index=11),
    )

    message = Message(
        text="This field is required.",
        code="required",
        index=("the_field",),
        start_position=Position(line_index=1, char_index=10),
        end_position=Position(line_index=1, char_index=11),
    )

    schema = Schema({"the_field": Field(required=True)})

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=schema)

    error = error.value
    assert error.messages

# Generated at 2022-06-14 14:45:55.888744
# Unit test for function validate_with_positions
def test_validate_with_positions():
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=Token({}), validator=Schema)

    error = exc_info.value
    message = error.messages()[0]
    assert message.text == "The field 'name' is required."
    assert message.code == "required"
    assert message.start_position.line_number == 1
    assert message.start_position.char_index == 2
    assert message.end_position.line_number == 1
    assert message.end_position.char_index == 2



# Generated at 2022-06-14 14:46:03.311856
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import textwrap
    from typesystem.base import String, Number, Array
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokens

    schema = Schema(properties=[("id", String), ("data", Array(items=Number))])
    tokenize = tokens.tokenize
    tokens = tokenize(json.dumps({"id": "foo", "data": [1, 2]}))
    token_id = tokens.lookup(("id",))
    validate_with_positions(
        token=token_id, validator=schema.properties["id"]
    )

    tokens = tokenize(json.dumps({"id": "foo"}))
    token_id = tokens.lookup(("id",))

# Generated at 2022-06-14 14:46:14.243324
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from ast import parse
    from typesystem import types
    from typesystem.tokenize.tokens import get_tokens, token_to_ast

    tree = parse("""def foo(a, b, c, d=1): pass""")
    tokens = get_tokens(tree)
    token_to_ast(tokens)
    schema = types.Schema({"arguments": types.List(types.String)})
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=tokens, validator=schema)

# Generated at 2022-06-14 14:46:23.402548
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, serialize, deserialize

    class Exercice(Schema):
        title = String(required=True)

    # Validate with positions
    try:
        token = deserialize('{"title": ""}', Exercice)
        validate_with_positions(token=token, validator=Exercice)
    except ValidationError as error:
        serialized = serialize(error)
        assert (
            serialized["messages"][0]["text"]
            == 'The field "title" is required.'
        )
        assert serialized["messages"][0]["start_position"] == {"line": 0, "column": 6}
        assert serialized["messages"][0]["end_position"] == {"line": 0, "column": 14}

# Generated at 2022-06-14 14:46:30.826509
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, Object, String

    class Pet(Object):
        id = Integer(description="The ID of the pet to fetch.", required=True)
        name = String()

    token = Token(
        value={
            "id": "1",
            "name": "abc",
            "unknown": "abc",
        },
        start=Position(line=1, column=1, char_index=0),
        end=Position(line=3, column=7, char_index=30),
    )

    assert validate_with_positions(token=token, validator=Pet) == {
        "id": 1,
        "name": "abc",
    }

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Pet)



# Generated at 2022-06-14 14:46:41.659023
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import ErrorMessage

    from .fixtures import Token, Field

    def validate(value):
        if not isinstance(value, str):
            raise ValidationError("Not a string")

    token = Token("_")
    message = validate_with_positions(token=token, validator=Field(validate))
    assert isinstance(message, ErrorMessage)
    assert message.start_position == (1, 0)
    assert message.end_position == (1, 1)

    token = Token("", start=(10, 10))
    message = validate_with_positions(token=token, validator=Field(validate))
    assert isinstance(message, ErrorMessage)
    assert message.start_position == (10, 10)
    assert message.end_position == (10, 11)

# Generated at 2022-06-14 14:46:53.752775
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import parse

    schema = Schema({"name": Field(required=True)})
    tokens = parse("{}")
    token = tokens.lookup("")

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=schema)

    assert error.value.messages()[0].code == "required"
    position = error.value.messages()[0].start_position
    assert position.line_number == 1
    assert position.char_index == 2
    assert position.column == 2

# Generated at 2022-06-14 14:47:02.828823
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import Integer
    from typesystem.schemas import Schema

    class School(Schema):
        name = Integer()

    def test():
        try:
            validate_with_positions(
                token=Token([["school", {"name": ""}]], start=0, end=100),
                validator=School(),
            )
        except Exception as error:
            assert (
                str(error)
                == """ValidationError:
The field "name" is required.
  File "string", line 1
   {"name": ""}
                ^^
"""
            )

    test()

# Generated at 2022-06-14 14:47:13.020342
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import MissingToken

    field = String(required=True)
    tokens = tokenize("{}")

    try:
        validate_with_positions(token=tokens[0], validator=field)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field 'name' is required.",
                code="required",
                index=["name"],
                start_position=tokens[0].start,
                end_position=tokens[0].end,
            )
        ]
    else:
        raise AssertionError("Should have raised error.")


# Generated at 2022-06-14 14:47:24.313305
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from tests.typesystem.test_validation import build_token

    class PersonSchema(Schema):
        name = Field(primitive_type="string")
        age = Field(primitive_type="integer")

    token = build_token(data={"age": "0"})
    try:
        validate_with_positions(token=token, validator=PersonSchema)
    except ValidationError as e:
        assert [
            Position(line=1, char_index=3, character_no=3)
        ] == [
            message.start_position
            for message in e.messages()
            if message.text.startswith("The field")
        ]


# Generated at 2022-06-14 14:47:32.659438
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import trafaret as t

    from typesystem.tokenize import tokenize

    from .utils import assert_message

    token = tokenize("{}")[0]

    schema = {
        "data": t.Object({"foo": t.String, "bar": t.Int})
    }

    class ValidatedSchema(Schema):
        schema = schema

    validator = ValidatedSchema()

    # Proper validation.
    result = validate_with_positions(token=token, validator=validator)
    assert result == {"data": {"foo": None, "bar": None}}

    # ValidationError with position.
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=validator.schema["data"])

# Generated at 2022-06-14 14:47:43.668783
# Unit test for function validate_with_positions
def test_validate_with_positions():
    person_schema = Schema({
        "name": Field(str),
        "age": Field(int),
    })

    person_token = Token(
        "person",
        raw='{"name": "Foo", "age": 30}',
        value={
            "name": "Foo",
            "age": 30,
        },
        start=Position(line_index=1, char_index=2),
        end=Position(line_index=1, char_index=18),
    )

    try:
        validate_with_positions(
            token=person_token, validator=person_schema
        )
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        message = messages[0]
        assert message.code == "required"

# Generated at 2022-06-14 14:47:55.036928
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.tokenize import tokenize

    class Developer(Schema):
        name = String(max_length=20)
        age = Integer(minimum=18)

    tokens = tokenize(
        """
        {
            "name": "Julia",
            "age": 17
        }
        """
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=tokens, validator=Developer(),
        )

    assert len(exc_info.value.messages()) == 1
    message = exc_info.value.messages()[0]
    assert message.code == "minimum"
    assert message.index == ["age"]

# Generated at 2022-06-14 14:48:07.015428
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import Integer, String
    from typesystem.exceptions import ValidationError
    from typesystem.tokenize.position import Position

    token = Token(
        value={
            "a": "1",
            "b": "",
            "c": {"d": 2},
            "e": [
                {"f": "a"},
                {"f": None},
                {"f": {"g": 3}},
                {"f": {"g": [4, 5, 6]}},
            ],
        },
        start=Position(line_number=1, line_index=0, char_index=0),
        end=Position(line_number=1, line_index=20, char_index=0),
        lookup=None,
    )


# Generated at 2022-06-14 14:48:13.214372
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Schema, fields
    from typesystem.tokenize import tokenize

    class Address(Schema):
        city = fields.String(required=True)
        state = fields.String(required=True)
        postal_code = fields.String()

    class Person(Schema):
        first_name = fields.String(required=True)
        last_name = fields.String(required=True)
        age = fields.Integer(minimum=18)
        address = fields.Schema(Address)

    document = "John Doe 19 Pleasantville 12345"

    token = tokenize(document)

    try:
        token = Person.validate(token)
    except ValidationError as error:
        assert error.messages[0].start_position == (1, 16)
        assert error.messages[0].end_position

# Generated at 2022-06-14 14:48:24.526827
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize_string
    from typesystem.fields import String, Number, Integer  # noqa: F401
    from typesystem.schemas import Schema  # noqa: F401

    class PersonSchema(Schema):
        name = String(min_length=3)
        age = Integer(min_value=18)

    document = """{
    "name": "Jack",
    "age": "17"
}"""


# Generated at 2022-06-14 14:48:35.707070
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Schema, Validator
    from typesystem.tokenize.tokens import Token
    from typesystem import structured_message

    token = Token(
        start={"line_index": 5, "char_index": 6},
        end={"line_index": 6, "char_index": 7},
        value={"name": 1},
    )

    class Person(Schema):
        name = String(required=True)

    class PersonValidator(Validator[Person]):
        def validate(self, value):
            return super().validate(value)

    PersonValidator.initialize()


# Generated at 2022-06-14 14:48:47.358450
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.token_stream import TokenStream
    from typesystem.tokenize.tokens import ListToken, ObjectToken, TokenType

    from .test_tokenizer import tokenize

    class PersonSchema(Schema):
        name = Field(type=str, required=True)
        numbers = Field(type=ListToken)

    stream = TokenStream(tokenize("""
        {
            "name": "Joe",
            "numbers": [1, 2, 3]
        }
    """))
    token = stream.next(type=TokenType.OBJECT)
    assert isinstance(token, ObjectToken)


# Generated at 2022-06-14 14:48:59.500986
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import IntToken

    assert validate_with_positions(
        token=IntToken(value=2, start=(1, 0), end=(1, 2)), validator=Field(required=True)
    ) == 2

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(
            token=IntToken(value=2, start=(1, 0), end=(1, 2)),
            validator=Field(required=True, minimum=4),
        )

    assert excinfo.value.messages[0].start_position == (1, 0)
    assert excinfo.value.messages[0].end_position == (1, 2)
    assert excinfo.value.messages[0].text == "Value must be at least 4."

# Generated at 2022-06-14 14:49:05.897481
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, String, Structure

    class Person(Structure):
        name = String(required=True)
        age = Integer(required=True)

    class Author(Person):
        publish_date = String(required=True)

    try:
        validate_with_positions(token=Token(type="obj", value=dict(name="Bob")),  # type: ignore
                                validator=Person)
    except ValidationError as error:
        messages = [str(e) for e in error.messages()]
        assert messages == [
            '"age" is required',
            '"publish_date" is required',
        ]

# Generated at 2022-06-14 14:49:17.622413
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize_string
    from typesystem.types import String
    from typesystem.exceptions import ValidationError
    from typesystem.schemas import Schema

    class Address(Schema):
        street_name = String(required=True)

    class Person(Schema):
        name = String()
        address = Address()

    token = tokenize_string(
        '{"name": "Eric", "address": {"post_code": 90210}}'
    )
    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == "The field 'street_name' is required."
        assert message.code == "required"

# Generated at 2022-06-14 14:49:29.803188
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class StringLength(Field):
        min_length = 3
        max_length = 5

    class Person(Schema):
        name = StringLength()
        age = Field(type=int)

    token = Token(
        value={
            "name": "123456789",
            "age": "bad_value",
            "gender": "n/a",
        },
        start=(7, 0),
        end=(7, 72),
    )

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=Person)

    message = excinfo.value.messages[0]
    assert message.text == "The field age is required"
    assert message.start_position.row == 7
    assert message.start_position.char_index == 44


# Generated at 2022-06-14 14:49:30.457327
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:49:42.054393
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.schemas import Schema, Structure
    from typesystem.tokenize.tokens import Token

    class MySchema(Structure):
        foo = String()
        bar = Integer(default=0)

    schema = MySchema()

    token = Token.parse(
        """
        {
            "foo": 1,
            "baz": "abc"
        }
        """
    )
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        assert len(error.messages()) == 3

    message = error.messages()[0]
    assert message.code == "invalid_type"
    assert message.text == "Expected a String."
    assert message.index

# Generated at 2022-06-14 14:49:50.408115
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class UserSchema(Schema):
        id = Field(type="integer")
        name = Field(type="string")

    from typesystem.tokenize.lexers import JSONLexer, YAMLLexer

    lexers = {".json": JSONLexer, ".yaml": YAMLLexer}

    for ext, lexer in lexers.items():
        with open("./tests/fixtures/minimal_record" + ext) as file:
            source = file.read()

        UserSchema.validate(source, lexer=lexer, json=True)

    with open("./tests/fixtures/minimal_record.json") as file:
        source = file.read()


# Generated at 2022-06-14 14:50:00.579199
# Unit test for function validate_with_positions
def test_validate_with_positions():
    text = """
    {
        "name": "Frank",
        "age": "unknown",
        "languages": ["Python", "C"]
    }
    """

    class UserSchema(Schema):
        name = Field(type="string", required=True)
        age = Field(type="integer", required=True)
        languages = Field(type="list", items=Field(type="string"))

    from typesystem.tokenize import tokenize
    from typesystem.parse import parse_dict

    tokens = tokenize(text)
    token = parse_dict(tokens)
    try:
        schema = UserSchema()
        schema.validate(token.value)
        assert False
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 3
        # Test

# Generated at 2022-06-14 14:50:15.299056
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse

    from typesystem.schemas import Schema
    from typesystem.fields import IntegerField

    schema_class = Schema({"foo": IntegerField()})
    token = parse("{}")
    try:
        validate_with_positions(token=token, validator=schema_class)
    except ValidationError as error:
        message = error.messages()[0]
        assert error.messages()[0].text == "The field 'foo' is required."
        assert message.start_position.line == 1
        assert message.start_position.column == 1
        assert message.start_position.char_index == 0
        assert message.end_position.line == 1
        assert message.end_position.column == 1
        assert message.end_position.char_

# Generated at 2022-06-14 14:50:26.242260
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import TokenParser, ParseError

    from tests.schemas import Article

    schema = Article()

    text = """{
        "title": "example",
        "link": "https://example.com",
        "text": "sample",
        "punchline": ":)",
        "content": {
            "body": "sample",
            "image": "https://example.com/image.png"
        }
    }"""
    tokens = TokenParser().parse(text)

    try:
        validate_with_positions(token=tokens, validator=schema)
    except ValidationError as error:
        messages = error.messages()

    assert len(messages) == 2

    message = messages[0]
    assert message.index == ("content", "body")


# Generated at 2022-06-14 14:50:32.023594
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class PersonSchema(Schema):
        name = Field(type=str, required=True)

    data = {"name": "foo"}
    token = Token.root(data)
    validate_with_positions(token=token, validator=PersonSchema)

# Generated at 2022-06-14 14:50:42.176244
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class User(Schema):
        first_name = Field(type="string", min_length=1)
        last_name = Field(type="string", min_length=1)

    token = Token(
        field="user",
        value={
            "first_name": "Rob",
            "last_name": "Pike",
            "nicknames": ["Uncle Rob", "Robbie"],
        },
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=User)
    assert (
        exc_info.value.messages()[0].text
        == "The field 'nicknames' is not a valid field."
    )


# Generated at 2022-06-14 14:50:52.915196
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexers import JsonLexer

    lexer = JsonLexer()
    tokens = lexer.tokenize(
        """
        {
            "name": "John Smith",
            "age": 20,
            "phone_numbers": [
                "555-1234"
            ]
        }
        """
    )
    token = tokens.lookup(["root", 0, "properties", "name"])
    validate_with_positions(token=token, validator=Field(type="string", min_length=10))
    token = tokens.lookup(["root", 0, "properties", "age"])
    validate_with_positions(token=token, validator=Field(type="integer", minimum=21))

# Generated at 2022-06-14 14:51:03.834379
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize.tokens import JSONArray, JSONObject
    from typesystem.validators import min_length
    from typesystem.errors import ValidationError

    sample_json = b'[{"id": "123", "name": "Fred"}, {"id": "456", "name": "George"}]'
    sample_token = JSONArray.parse(sample_json)

    # Object validation error (validation error class)
    name_field = String(validators=[min_length(4)])
    user_schema = Schema({"name": name_field, "id": String()})
    with pytest.raises(ValidationError) as e:
        validate_with_positions(token=sample_token[0], validator=user_schema)

    # Missing required field


# Generated at 2022-06-14 14:51:15.614687
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Schema, Integer, String

    class FOO(Schema):
        field = Integer(required=True)

    class BAR(Schema):
        field = String(required=True)

    schema = FOO(strict=True)
    validate_with_positions(
        token=Token(value={}, start={"line": 0, "char_index": 0}, end={"line": 0, "char_index": 0}),
        validator=schema,
    )
    with pytest.raises(ValidationError):
        validate_with_positions(
            token=Token(
                value={},
                start={"line": 0, "char_index": 0},
                end={"line": 0, "char_index": 0},
            ),
            validator=schema,
        )

   

# Generated at 2022-06-14 14:51:20.230970
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.validators import JSONField

    field = JSONField()
    token = Token(value={"a": {"c": True}}, start=0, end=15)
    validate_with_positions(token=token, validator=field)

# Generated at 2022-06-14 14:51:28.158806
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.tokenize import tokenize

    token = tokenize('{"a": "foo"}')
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator={"a": int})
    assert exc_info.value.messages() == [Message(
        text="a must be int.",
        code="type_error.integer",
        index=["a"],
        start_position=token.start,
        end_position=token.end,
    )]

# Generated at 2022-06-14 14:51:38.453543
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schema import Schema
    from typesystem.fields import Integer, String

    class PersonSchema(Schema):
        name = String()
        age = Integer()

    token = Token.parse(
        {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
                "weight": {"type": "number"},
            },
        },
        "Person",
        start_position={"line": 1, "char_index": 0},
    )

    try:
        validate_with_positions(token=token, validator=PersonSchema)
    except ValidationError as error:
        assert len(error.messages()) == 1

# Generated at 2022-06-14 14:51:57.957015
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.scanner import TokenizeObject
    from typesystem.tokenize.scanner import TokenizeList
    from typesystem.tokenize.scanner import TokenizeString
    from typesystem.tokenize.scanner import TokenizeNumber
    from typesystem.tokenize.scanner import TokenizeBoolean
    from typesystem.tokenize.scanner import TokenizeNull
    from typesystem.tokenize.scanner import TokenizeComma
    from typesystem.tokenize.scanner import TokenizeColon

    from typesystem.fields import String
    from typesystem.fields import Integer
    from typesystem.fields import Float
    from typesystem.fields import Boolean
    from typesystem.fields import Date
    from typesystem.fields import DateTime
    from typesystem.fields import Time
    from typesystem.fields import Array

# Generated at 2022-06-14 14:52:01.432236
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token("name", "Alice")
    try:
        validate_with_positions(token=token, validator=Field(required=True))
    except ValidationError as error:
        message, = error.messages()
        assert message.text == "The field 'name' is required."

# Generated at 2022-06-14 14:52:13.819394
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenize import tokenize

    from .test_validation import MockField
    from .test_validation import MockSchema
    from .test_validation import MockError
    from .test_validation import MockMessage

    field = MockField()
    field.validate = lambda value: value
    field_error = MockError(
        messages=[MockMessage(code="required", index=["field"])],
    )
    field.validate.side_effect = field_error

    schema = MockSchema()
    schema.validate = lambda value: value
    schema_error = MockError(
        messages=[MockMessage(code="required", index=["schema"])],
    )
    schema.validate.side_effect = schema_error


# Generated at 2022-06-14 14:52:22.498545
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizers import tokenize, Token
    from typesystem.tokenize import tokens
    from typesystem.fields import String

    class TestSchema(Schema):
        title = String(min_length=2, max_length=2)
        description = String(min_length=2, max_length=2)

    schema = TestSchema()
    token_parts = tokenize("{}")
    token_root = tokens.RootToken(parts=token_parts)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token_root, validator=schema)

    assert exc_info.value.messages  # type: ignore
    message = exc_info.value.messages[0]  # type: ignore


# Generated at 2022-06-14 14:52:30.204974
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    
    from typesystem.parser.parser import parse

    class BookSchema(Schema):
        title = Field(str, required=True)
        price = Field(int, required=True)
        author = Field(str, required=True)

    json_str = """
    {
      "title": "Crime and Punishment",
      "price": "10",
      "author": "Fyodor Dostoyevsky"
    }
    """
    token = parse(json_str)

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=BookSchema)
    error = excinfo.value

# Generated at 2022-06-14 14:52:41.607657
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import typesystem
    from typesystem.tokenize.streams import TokenStream
    from typesystem.tokenize import tokenize_file

    class Person(typesystem.Schema):
        name = typesystem.String(min_length=3, max_length=5)
        age = typesystem.Integer(minimum=0, maximum=200)

    text = '{"name": "foo"}'
    tokens = tokenize_file(text, "test.json")
    token = next(tokens)

# Generated at 2022-06-14 14:52:49.559164
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema({"name": {"type": "string", "required": True}})

    def validator(data):
        try:
            validate_with_positions(token=data, validator=schema)
        except ValidationError as error:
            return error.messages()
        else:
            raise AssertionError("Expected a ValidationError")

    # required

# Generated at 2022-06-14 14:53:00.096599
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizers import tokenizer

    token = tokenizer.tokenize(
        """
{
  "id": 1,
  "name": "name",
  "parent": {
    "id": 2,
    "name": "parent"
  }
}
"""
    )

    class Person(Schema):
        id = Field(type="integer")
        name = Field(type="string")

    class Parent(Schema):
        id = Field(type="integer")
        name = Field(type="string")
        children = Field(type="array", items=Person)

    class PersonWithParent(Schema):
        id = Field(type="integer")
        name = Field(type="string")
        parent = Field(type=Parent)

    # Person

# Generated at 2022-06-14 14:53:10.932034
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from typesystem.tokenize.tokenizer import tokenize
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.typing import JSONValue

    class Person(Schema):
        name = String(required=True)
        age = String(required=True)

    class Family(Schema):
        father = Person(required=True)
        mother = Person(required=True)
        children = Person(many=True, required=True)

    json = {"father": {"name": "John"}, "mother": {"name": "Jane"}, "children": []}

    tokenizer = tokenize(json)


# Generated at 2022-06-14 14:53:22.404000
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    from .fixtures.user_schema import UserSchema

    tokens = tokenize("""
        {
            "name": "Chris",
            "age": "kdj"
        }
    """)

    try:
        validate_with_positions(token=tokens, validator=UserSchema)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="This value is not a valid integer.",
                code="invalid",
                index=["age"],
                start_position=Position(line=3, line_char=11),
                end_position=Position(line=3, line_char=14),
            )
        ]
    else:
        assert False, "Did not raise validation error."

# Generated at 2022-06-14 14:53:44.143256
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class TopLevelSchema(Schema):
        a = Field(required=True)

    token = Token({"a": 3}, start=0, end=10)
    token = token.lookup(["a"])

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Field(required=True))

    assert exc_info.value.messages()[0].start_position.line == 1
    


# Generated at 2022-06-14 14:53:54.073390
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import StringToken

    class MessageSchema(typesystem.Schema):
        text = typesystem.String(required=True)
        code = typesystem.String(required=True)
        index = typesystem.Array(typesystem.String())
        start_position = typesystem.String()
        end_position = typesystem.String()

    class PersonSchema(typesystem.Schema):
        first_name = typesystem.String(required=True)
        last_name = typesystem.String(required=True)
        age = typesystem.Integer()

    source = "{first_name: 'Sebastian '}"
    token = tokenize(source)
    assert isinstance(token, StringToken)


# Generated at 2022-06-14 14:54:01.034934
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from .parser import parse_schema, parse_data, Token

    schema = parse_schema("{name: String}")
    data = parse_data('{"name": 42}')
    assert data.start.line_number == 1
    assert data.start.column_number == 1
    with pytest.raises(ValidationError):
        validate_with_positions(token=data, validator=schema)



# Generated at 2022-06-14 14:54:12.910556
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem import fields
    from typesystem import errors
    from typesystem.utils.position import Position

    schema = fields.Array(
        items=fields.Integer(min_value=10),
        min_items=5,
        max_items=5,
    )

    tokens = tokenize('[1, 2, 3, 4, 5]')
    with pytest.raises(errors.ValidationError) as error:
        validate_with_positions(token=tokens, validator=schema)

    assert len(error.value.messages()) == 5
    assert error.value.messages()[0].text == "Value must be >= 10."
    assert error.value.messages()[0].code == "min_value"
    assert error.value.messages

# Generated at 2022-06-14 14:54:18.186744
# Unit test for function validate_with_positions
def test_validate_with_positions():
    """Ensure the function validate_with_positions produces position
    information."""
    import typesystem
    import pytest

    token = Token(value={"a": {"b": 4}})

    field = typesystem.String(name="a", index_as="b")
    field = typesystem.Array(sub_field=field)
    schema = typesystem.Schema(fields={"a": field})
    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=schema)

# Generated at 2022-06-14 14:54:27.469413
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.schemas import Schema, Structure
    from typesystem.tokenize.tokens import Token

    class Person(Schema):
        name = String(required=True)
        age = Integer()

    def test_missing_required():
        """Test missing required field."""
        person_token = Token(
            value={
                "name": "Yoda",
            }
        )
        with pytest.raises(ValidationError) as exc_info:
            validate_with_positions(token=person_token, validator=Person)
        messages = exc_info.value.messages
        assert messages[0].text == "The field 'age' is required."
        assert messages[0].start_position.line == 0
        assert messages[0].start_position

# Generated at 2022-06-14 14:54:38.470304
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class SimpleSchema(Schema):
        username = Field(type=str, required=True)
        password = Field(type=str, required=True)

    token = Token(
        value={
            "username": "test",
            "password": "testpassword",
        },
        start=Token.Position(line_index=1, char_index=4),
        end=Token.Position(line_index=4, char_index=5),
    )
    try:
        validate_with_positions(token=token, validator=SimpleSchema)
    except ValidationError as e:
        assert e.messages()[0].start_position.char_index == 7  # type: ignore
        assert e.messages()[0].end_position.char_index == 16  # type: ignore

# Generated at 2022-06-14 14:54:44.571788
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize_string
    from typesystem.tokenize.source_positions import SourcePosition, SourceSpan

    from typesystem.types import String

    class Name(Schema):
        first = String()
        last = String()

    token = tokenize_string(data={"first": "John", "last": "Doe"})

    assert validate_with_positions(token=token, validator=Name) == {
        "first": "John",
        "last": "Doe",
    }

    try:
        validate_with_positions(token=token, validator=Name(required=["foo"]))
    except ValidationError as error:
        assert error.messages() == [Message(text="The field 'foo' is required.")]

# Generated at 2022-06-14 14:54:54.889038
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.tokenize.tokens import Token

    schema = Schema(fields={"name": String(required=True)})
    token = Token(value={"name": ""})
    # throws exception
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        assert len(error.messages()) == 1
        assert error.messages()[0].text == "The field 'name' is required."
        assert error.messages()[0].start_position.source_name == "<unknown>"
        assert error.messages()[0].start_position.line_number == 1
        assert error.messages()[0].start_position.line_offset == 1

# Generated at 2022-06-14 14:55:04.864272
# Unit test for function validate_with_positions
def test_validate_with_positions():

    def validate_number(value: typing.Any) -> int:
        if value == 42:
            return 42
        raise ValidationError(
            "Not 42",
            code="not_42",
            start_position=Position(0, 0),
            end_position=Position(0, 42),
        )

    class TestSchema(Schema):
        number = Field(validators=[validate_number])

    token = to_token({"number": 42})

    validate_with_positions(token=token, validator=TestSchema())
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=TestSchema.fields["number"])

    messages = exc_info.value.messages

    assert len(messages) == 1