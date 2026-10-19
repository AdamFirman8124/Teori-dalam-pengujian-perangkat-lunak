

# Generated at 2022-06-14 14:45:19.584471
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    import typesystem
    from typesystem.tokenize.positions import Position

    class Object(typesystem.Schema):
        """
        {
            "field": 0
        }
        """
        field = typesystem.Integer(minimum=1)

    assert Object.validate({"field": 0}) == {"field": 0}

    token = Token.from_python({"field": 0})
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Object)

# Generated at 2022-06-14 14:45:29.066704
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parse import parse
    from typesystem.tokenize.validators import String, Integer
    from typesystem.tokenize.schemas import StringField, IntegerField

    schema = parse({"type": "object", "properties": {"foo": "string", "bar": "int"}})

    token = parse({"foo": "hello", "bar": 42})
    assert validate_with_positions(token=token, validator=schema) == token.value

    token = parse({"foo": "hello"})

# Generated at 2022-06-14 14:45:35.807425
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest

    from typesystem import parse
    from typesystem.tokenize.tokenizer import Tokenizer

    from tests.schema import schema

    document = """
        {
            "name": "Star Wars"
        }
    """
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(document)
    with pytest.raises(ValidationError) as excinfo:
        schema.validate(parse(tokens))
    assert excinfo.value.messages[0].text == "The field 'type' is required."
    assert excinfo.value.messages[1].text == "The field 'director' is required."


# Generated at 2022-06-14 14:45:47.423531
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.decorators import create_schema

    class PersonSchema(Schema):
        class Meta:
            strict = True

        name = "Person"
        name_field = "name"
        fields = [Field(name="name", type=str, required=True)]

    @create_schema(PersonSchema)
    class Person:
        pass

    person = Person(name="John")
    assert person.name == "John"

    with pytest.raises(ValidationError) as exc_info:
        Person()

    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.start_position.line_index == 0
    assert message.start_position.char_index == 1
    assert message.end_position.line

# Generated at 2022-06-14 14:45:55.337720
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class MySchema(Schema):
        foo = String()

    token = Token(
        {
            "foo": "hello",
        }
    )
    try:
        validate_with_positions(token=token, validator=MySchema())
        # Shouldn't happen, we throw an exception in the unit test
        assert False
    except ValidationError as error:
        message = error.messages()[0]
        assert message.start_position == (1, 7)
        assert message.end_position == (1, 8)
        assert message.text == "Value must be a string."

# Generated at 2022-06-14 14:46:06.105740
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem

    class MyField(Field):
        def validate(self, value: str) -> int:
            try:
                return int(value)
            except Exception:
                self.error("invalid_int")

    class MySchema(Schema):
        name = MyField()

    token = Token(
        value={
            "name": "100",
        },
        lookup=lambda x: Token(
            value=x, start={"line": 1, "col": 1, "char_index": 1}, end={}
        ),
    )

    assert validate_with_positions(token=token, validator=MySchema) == {
        "name": 100
    }

    token.value["name"] = "jesse"

    with pytest.raises(typesystem.ValidationError):
        validate_

# Generated at 2022-06-14 14:46:16.471944
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokenize, Token

    class Person(Schema):
        name = Field(type=str, required=True)
        age = Field(type=int)

    person = Person(name="foo", age=42)
    data = person.serialize(person)
    tokens = list(tokenize(data))
    assert [t.value for t in tokens] == [{'name': 'foo', 'age': 42}]

    token = tokens[0]
    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        print(error)
        assert error.messages()[0].start_position.char_index == 1

# Generated at 2022-06-14 14:46:22.242795
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(str)
    token = Token(None, "hello")
    assert validate_with_positions(token=token, validator=field) is None

    field = Field(str, required=True)
    token = Token(None, None)
    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as error:
        message = error.get_message()
        assert message.text == "The field None is required."

# Generated at 2022-06-14 14:46:30.417476
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer
    from typesystem.tokenize.parse import parse_string
    from typesystem.tokenize.tokens import Token

    schema = {"id": {"type": "integer"}}
    token = parse_string(schema, '{"id": "foo"}')

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(token=token, validator=schema)

    assert len(exc.value.messages()) == 1

    message = exc.value.messages()[0]
    assert isinstance(message.index, list)

    assert message.start_position == Token.Position(
        line_index=2,
        char_index=8,
    )

# Generated at 2022-06-14 14:46:41.397092
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.tokenize import parse_tokens, tokenize
    from typesystem.tokenize.tokens import Token

    class SimpleSchema(Schema):
        field_a = Int()
        field_b = Str()
        field_c = Str(default="hi")

    token_tree = [
        Token(value={"field_a": 1, "field_b": "a"}, start=0, end=0),
        Token(value={"field_a": 2, "field_b": "b"}, start=0, end=0),
    ]

    class SimpleSchema(Schema):
        field_a = Int()
        field_b = Str()
        field_c = Str(default="hi")


# Generated at 2022-06-14 14:46:55.421665
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse_string

    class Query(Schema):
        name = Field(str)
        age = Field(int, default="20")

    # ValidationError without positions
    try:
        Query().validate({"name": "", "age": "abc"})
    except ValidationError as e:
        message = e.messages()[0]
        assert message.index == ("age",)
        assert "value should be an integer" in message.text

    # ValidationError with positions
    try:
        validate_with_positions(
            token=parse_string('{"name": "", "age": "abc"}'), validator=Query()
        )
    except ValidationError as e:
        message = e.messages()[0]
        assert message.index == ("age",)

# Generated at 2022-06-14 14:47:06.308687
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.validators import String
    from typesystem.tokenize.tokens import ObjectToken

    class PersonSchema(Schema):
        name = String()

    def assert_valid(value: str, expected: str) -> None:
        token = ObjectToken(content=value)
        output = validate_with_positions(token=token, validator=PersonSchema)
        assert output == expected

    def assert_invalid(value: str, expected: ValidationError) -> None:
        token = ObjectToken(content=value)
        with pytest.raises(ValidationError) as exc_info:
            validate_with_positions(token=token, validator=PersonSchema)
        assert exc_info.value is expected

    assert_valid("{" "}", {})


# Generated at 2022-06-14 14:47:15.126799
# Unit test for function validate_with_positions

# Generated at 2022-06-14 14:47:25.885762
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String, Structure

    class MyStructure(Structure):
        foo = String(required=True)

    token = Token.parse('{"foo": "Hello World!"}')

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=MyStructure)

    assert exc_info.value.messages()[0].start_position.line_number == 1
    assert exc_info.value.messages()[0].start_position.char_index == 10
    assert exc_info.value.messages()[0].end_position.line_number == 1
    assert exc_info.value.messages()[0].end_position.char_index == 22

# Generated at 2022-06-14 14:47:36.337753
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String
    from typesystem.tokenize.tests.utils import tokenize_and_parse
    from typesystem.tokenize import tokens

    string_field = String()

    result = tokenize_and_parse('{"a": "b"}')
    assert isinstance(result, tokens.Token)
    assert result.children[0].children[1].value == "b"
    assert validate_with_positions(token=result, validator=string_field) == "b"
    assert validate_with_positions(token=result, validator={"a": string_field}) == {
        "a": "b"
    }

    result = tokenize_and_parse('{"a": "b", "c": null}')

# Generated at 2022-06-14 14:47:45.806338
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import get_tokens

    class Person(Schema):
        name = Field(type=str)
        age = Field(type=int)

    tokens = get_tokens({"name": "", "age": ""})
    assert validate_with_positions(token=tokens, validator=Person) == (None, None)

    tokens = get_tokens({"name": "", "age": ""})
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=tokens, validator=Person)

# Generated at 2022-06-14 14:47:56.116483
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.json_schema import JSONSchema
    from typesystem.tokenize.tokens import Token

    test_schema = JSONSchema({
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "foo": {
                "type": "string",
            },
            "bar": {
                "type": "string",
            },
        },
    })


# Generated at 2022-06-14 14:48:07.824657
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Structure
    from typesystem.tokenize import tokenize_string

    blob = tokenize_string(
        """
    {
        "name": null,
        "password": "s3cret",
        "age": "not a number"
    }
    """
    )
    schema = Structure(
        {"name": Field(required=True), "password": Field(required=True), "age": Field()}
    )

# Generated at 2022-06-14 14:48:20.255892
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import Integer, Object

    schema = Schema(fields={"a": {"fields": {"b": Integer(required=True)}}})

    try:
        validate_with_positions(
            token=Token({"a": {"b": None}}), validator=schema
        )
    except ValidationError as error:
        [message] = error.messages()
        assert (
            message.text == "The field 'b' is required."  # type: ignore
        )  # type: ignore
        assert message.start_position.line_number == 1  # type: ignore
        assert message.start_position.char_index == 6  # type: ignore
        assert message.end_position.char_index == 10  # type: ignore

# Generated at 2022-06-14 14:48:30.385858
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.exceptions import ValidationError
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class Person(Schema):
        name = String()

    try:
        Person().validate({"nome": "John"})
    except ValidationError as error:
        str(error.messages()[0]) == "'name' is a required field."

    try:
        validate_with_positions(
            token=Token("hello", start=(1, 2), end=(1, 7)), validator=String(max_length=1)
        )
    except ValidationError as error:
        assert str(error.messages()[0]) == "Ensure this value has at most 1 characters (it has 5)."

# Generated at 2022-06-14 14:48:46.727975
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import LineToken
    from typesystem.tokenize.tokens import Position
    from typesystem.tokenize.tokens import RootToken
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.tokens import Tokenizer

    source = dedent(
        """
        A
        B
        C
        """
    ).strip()

    tokenizer = Tokenizer()
    linetokens = tokenizer.tokenize(source)

    root = RootToken()
    root.add_child(linetokens[0])
    root.add_child(linetokens[1])
    root.add_child(linetokens[2])

    class MyValidator(Schema):
        value = Field(type="string")


# Generated at 2022-06-14 14:48:58.702769
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexers import JSONLexer
    schema = Schema(fields={"a": {"type": "number"}, "b": {"type": "number"}}, required=["a"])
    json = '{"a": 1, "c": 2}'
    token = JSONLexer().tokenize(json)
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=schema)
    assert len(excinfo.value.messages()) == 1
    message = excinfo.value.messages()[0]
    assert message.text == "The field 'b' is required."
    assert message.start_position.index == 8
    assert message.end_position.index == 19



# Generated at 2022-06-14 14:49:06.584136
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # Simplified replace for LineColPosition
    class ColPosition:
        __slots__ = ("char_index", "byte_index")

        def __init__(self, char_index: int, byte_index: int) -> None:
            self.char_index = char_index
            self.byte_index = byte_index

    # Simplified replace for Token
    class Token:
        __slots__ = ("value", "index")

        def __init__(self, value: typing.Any, *, index: typing.Tuple[int, ...]):
            self.value = value
            self.index = index

        def lookup(self, index: typing.Tuple[int, ...]) -> "Token":
            return Token(self.value[index[0]], index=self.index + index)


# Generated at 2022-06-14 14:49:18.598421
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.tokenize.parser import parse_token_tree
    from typesystem.tokenize.tokens import ObjectToken

    class MySchema(Schema):
        first_name = String()
        last_name = String()

    source = "{" + '"first_name": "Alice", "last_name": "Baker"' + "}"
    tokens = parse_token_tree(source)
    assert len(tokens) == 1
    token = tokens[0]
    assert isinstance(token, ObjectToken)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=MySchema)
    assert len(exc_info.value.messages)

# Generated at 2022-06-14 14:49:30.403765
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.plaintext import PlaintextTokenizer
    from typesystem.fields import String

    def raise_validation_error(error: Message) -> None:
        raise ValidationError([error])

    source = '{"a": 1, "b": "hello world"}'
    ctx = PlaintextTokenizer(source).parse()
    try:
        validate_with_positions(
            token=ctx,
            validator=Schema({"a": String(), "b": String()}, raise_on_error=raise_validation_error),
        )
    except ValidationError as error:
        error = error.messages()[0]
        assert error.text == "Must be a string."
        assert error.code == "type_error"
        assert error.start_position.line_index == 0

# Generated at 2022-06-14 14:49:40.254981
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.base import Source

    class User(Schema):
        first_name = Field(type="string")

    data = {
        "first_name": "John",
        "last_name": "Doe",
    }
    source = Source("""{
        "first_name": "John",
        "last_name": "Doe",
    }""")
    token = source.parse()
    try:
        validate_with_positions(token=token, validator=User)
    except ValidationError as error:
        message = error.messages()[0]
        assert message.text == '"last_name" is not a valid field.'
        assert message.start_position.line == 2
        assert message.start_position.column == 9
        assert message.start_position.char_

# Generated at 2022-06-14 14:49:47.370277
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import types
    from typesystem.tokenize import tokenize

    with pytest.raises(ValidationError):
        validate_with_positions(token=tokenize("123"), validator=types.String())

    with pytest.raises(ValidationError) as error:
        validate_with_positions(
            token=tokenize({"a": 1}), validator=types.Schema({"b": types.String()})
        )

    assert "The field 'b' is required." in str(error.value)
    assert "The field 'a' is not valid." in str(error.value)

# Generated at 2022-06-14 14:49:54.468472
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    from .test_tokenize import test_str

    token = tokenize(
        test_str,
        dict(
            username=str,
            email=str,
            age=int,
            active=bool,
            tags=list,
        ),
    )
    print(token)
    validate_with_positions(token=token, validator=token.validator)

# Generated at 2022-06-14 14:50:04.571358
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class PersonSchema(Schema):
        name = Field(types=str, required=True)
        age = Field(types=int, required=True)
        title = Field(types=str, required=False)

    class TeamSchema(Schema):
        members = Field(types=PersonSchema, required=True)

    doc = {
        "@type": "Team",
        "members": [
            {"@type": "Person", "name": "Hendrik", "age": 38},
            {"@type": "Person", "name": "Barbara", "age": 38},
        ],
    }

    # Example 1:
    #
    # Changes to specified list
    doc["members"][0]["age"] = "38"
    token = Token.from_dict(data=doc)
    # must fail with validation error

# Generated at 2022-06-14 14:50:05.435523
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:50:17.145842
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize import tokenize

    token = tokenize("a: b")[2]
    with pytest.raises(ValidationError):
        validate_with_positions(token=token, validator=String())



# Generated at 2022-06-14 14:50:26.898721
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizers import Tokenizer
    from typesystem.tokenize.tokens import IdentifierToken
    from typesystem.fields import String
    from typesystem.utils import indent

    string = """
    Rule:
        name: String(required=True)
        version: String
    """
    print(indent(string))
    tokenizer = Tokenizer(string)
    tokens = list(tokenizer.tokenize())
    assert isinstance(tokens[0], IdentifierToken)
    try:
        validate_with_positions(token=tokens[0], validator=String())
    except ValidationError as error:
        print(error.message())


test_validate_with_positions()

# Generated at 2022-06-14 14:50:28.276836
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:50:39.983960
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parser
    from tests.normalize import normalize

    node = parser.parse("""
    foo:
        bar:
            - 1
            - "Two"
            - 3
    """)
    validator = Schema(fields={"foo": Field(type="object", fields={"bar": Field()})})

# Generated at 2022-06-14 14:50:52.265489
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # A token is valid so it should return the value
    token = Token(
        type="dict",
        value={"key": "value"},
        start=Token.Position(line=1, column=1, char_index=0),
        end=Token.Position(line=1, column=9, char_index=8),
    )
    assert validate_with_positions(token=token, validator=type({})) == {"key": "value"}
    # If a token is invalid, it must raise a ValidationError
    token = Token(
        type="int",
        value=1,
        start=Token.Position(line=1, column=1, char_index=0),
        end=Token.Position(line=1, column=1, char_index=0),
    )

# Generated at 2022-06-14 14:51:03.378161
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexers import Lexer
    from typesystem.tokenize.schemas import Object, String, Integer

    object_token = Lexer().tokenize(
        {
            "foo": "bar",
            "fizz": [{"bang": 42}],
            "bazz": {"bazz": {"bazz": {"bazz": 43}}},
            "bazz.bazz.bazz.bazz": 45,
        }
    )

    validate_with_positions(
        token=object_token,
        validator=Object(
            {
                "foo": String(),
                "fizz": Object({"bang": Integer()}),
                "bazz": Object({"bazz": Object({"bazz": Object({"bazz": Integer()})})}),
            }
        ),
    )

# Generated at 2022-06-14 14:51:15.354895
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import (
        DictionaryToken,
        ListToken,
        Token,
    )
    from typesystem.tokenize.lexer import Lexer
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class ColoursSchema(Schema):
        colours = String()

    class ListsSchema(Schema):
        colours = ListToken(String())

    class DictionariesSchema(Schema):
        colours = DictionaryToken(
            keys=String(), values=ListToken(String())
        )

    lexer = Lexer()

    def validate(
        value, validator,
    ):
        return validate_with_positions(
            token=lexer.tokenize(value), validator=validator
        )

    # Test no error

# Generated at 2022-06-14 14:51:27.342040
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.lexers import lex
    from typesystem.tokenize.rules import RULE_SET
    from typesystem.fields import String

    source = '{"name": "Alice"}'
    tree = lex(source, RULE_SET)
    token = tree.tokens[0]
    # Test with a field validator.
    result = validate_with_positions(token=token, validator=String(required=True))
    assert result == "Alice"
    # Test a schema validator.
    assert token.validate(IPAddressSchema)
    # Test with a missing field.
    source = "{}"
    tree = lex(source, RULE_SET)
    token = tree.tokens[0]
    with pytest.raises(ValidationError) as exc:
        validate_with_

# Generated at 2022-06-14 14:51:37.706733
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Object, String
    from typesystem.tokenize.tokens import ObjectToken, StringToken
    from typesystem import ValidationError
    from typesystem.json_schema import Object as JSONSchemaObject

    ob = JSONSchemaObject({"properties": {"one": {"type": "string"}}})
    token = ObjectToken(start=(1, 2), end=(1, 5), value={"one": "1"})
    result = validate_with_positions(token=token, validator=ob)
    assert result == {"one": "1"}

    class Abc(Object):
        one = String()  # type: ignore
    result = validate_with_positions(token=token, validator=Abc)
    assert result == {"one": "1"}


# Generated at 2022-06-14 14:51:48.885181
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # noinspection PyProtectedMember
    from typesystem import String, _as_type
    from typesystem.tokenize.tokens import StringToken

    class Person(Schema):
        first_name = String(max_length=10)
        last_name = String(max_length=10)

    Person = _as_type(Person)

    token = StringToken("first_name", "John", start=(1, 0), end=(1, 5))

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Person.fields["first_name"])

    messages = exc_info.value.messages(as_tuple=True)

# Generated at 2022-06-14 14:52:14.405957
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema, Object
    from typesystem.fields import Field, String
    from typesystem.tokenize import tokenize, Token
    from typesystem import ValidationError

    class UserSchema(Schema):
        name = String(required=True)
        email = String(field_type="email")

    value = {"name": "John Doe", "email": "jdoe@example.com"}
    token = Token.from_native(value)

    result = validate_with_positions(token=token, validator=UserSchema)
    assert result == value

    value = {}
    token = Token.from_native(value)
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=UserSchema)

    assert exc

# Generated at 2022-06-14 14:52:22.676472
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize.scanner import Scanner
    from typesystem.tokenize.tokens import Object, Root
    from typesystem.tokenize.positions import Position

    data = {"first_name": "John", "last_name": "Doe"}
    scanner = Scanner(data)
    tokens = scanner.scan()

# Generated at 2022-06-14 14:52:30.265101
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.exceptions import ValidationError
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.tokens import TokenType

    class Position:
        def __init__(
            self,
            source: str,
            line: int = 0,
            col_index: int = 0,
            char_index: int = 0,
        ) -> None:
            self.line = line
            self.col_index = col_index
            self.char_index = char_index
            self.source = source


# Generated at 2022-06-14 14:52:41.695450
# Unit test for function validate_with_positions
def test_validate_with_positions():

    from io import StringIO

    from typesystem.base import Message
    from typesystem.fields import StringField
    from typesystem.tokenize.base import Tokenizer

    tokenizer = Tokenizer()
    tokenizer.parse(StringIO('{"name":"bob", "age":12}'))
    root = tokenizer.root_group

    schema = StringField(index=["name"])

    try:
        validate_with_positions(token=root, validator=schema)
    except ValidationError as error:
        message = error.messages[0]
    assert message == Message(
        text="The field 'name' is required.",
        code="required",
        index=["name"],
        start_position=root.start,
        end_position=root.end,
    )



# Generated at 2022-06-14 14:52:47.594884
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import types

    class Message(types.Schema):
        subject = types.String()
        body = types.String()

    body = validate_with_positions(
        validator=Message,
        token=Token(start=(1,0), end=(1,11), value={"subject": "Hello", "body": ""}),
    )
    assert body == {}

# Generated at 2022-06-14 14:52:57.461118
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, Object, String

    schema = Object(properties={"x": Integer(minimum=0)})
    code = "{x: true}"

    try:
        validate_with_positions(
            token=Token(value=code, start={"char_index": 0, "line_index": 1,}),
            validator=schema,
        )
    except ValidationError as err:
        message = err.messages[0]
        assert message.code == "invalid_type"
        assert message.text == "Invalid value, expected Integer."
        assert message.start_position.char_index == 5
        assert message.start_position.line_index == 1



# Generated at 2022-06-14 14:53:03.605911
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class TestSchema(Schema):
        foo = Field(required=True)
        bar = Field(required=True)

    class TestSchema2(Schema):
        baz = Field(required=True)

    class BodySchema(Schema):
        schema = TestSchema
        schema2 = TestSchema2

    from typesystem.tokenize import parse_object

    tokens = parse_object({"foo": "bar"}, position=0)
    with pytest.raises(ValidationError):
        validate_with_positions(token=tokens, validator=BodySchema)

# Generated at 2022-06-14 14:53:13.417564
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokens import Token
    from typesystem.tokenize.utils import TokenPosition

    start_position = TokenPosition(line=0, char_index=0)
    end_position = TokenPosition(line=0, char_index=0)

    token = Token(
        value={
            "a": 1,
            "b": {
                "c": 2,
                "d": 3,
            }
        },
        start=start_position,
        end=end_position,
    )

    schema = Schema(fields={"a": Field(type="integer")})
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        messages = error.messages()

        positional_message = messages[0]

# Generated at 2022-06-14 14:53:25.167353
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.tokenizer import Tokenizer
    from typesystem.tokenize.tokens import DictionaryToken
    from typesystem.fields import String

    tokenizer = Tokenizer(
        start_position=tokenize.Position(
            line_index=1, char_index=1, line_text="\n{}", start_position=0, end_position=1
        ),
        end_position=tokenize.Position(
            line_index=1, char_index=3, line_text="\n{}", start_position=2, end_position=3
        ),
        tokens=[],
    )
    token = tokenizer.tokenize(text="{}")
    assert isinstance(token, DictionaryToken)
    with pytest.raises(ValidationError) as exc:
        validate_with_positions

# Generated at 2022-06-14 14:53:36.162045
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class FooSchema(Schema):
        foo = Field(type="string", required=True)

    token = Token(
        value={
            "foo": "bar",
            "baz": "qux",
        },
        children={
            "foo": Token(
                value="bar",
                start=(1, 1),
                end=(1, 10),
                children={
                    "bar": Token(
                        value="bar",
                        start=(1, 4),
                        end=(1, 10),
                    ),
                },
            ),
            "baz": Token(
                value="qux",
                start=(2, 5),
                end=(2, 11),
            ),
        },
        start=(1, 0),
        end=(3, 0),
    )

# Generated at 2022-06-14 14:54:15.467688
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import String
    from typesystem.tokenize import Token

    field = String(required=True)
    token = Token(name="string", value="hello", start=(1, 0), end=(2, 0))
    assert validate_with_positions(token=token, validator=field) == "hello"

    field = String(required=False)
    token = Token(name="string", value=None, start=(1, 0), end=(2, 0))
    assert validate_with_positions(token=token, validator=field) is None

    from typesystem import Integer

    field = Integer()
    token = Token(name="integer", value=100, start=(1, 0), end=(2, 0))
    assert validate_with_positions(token=token, validator=field) == 100


# Generated at 2022-06-14 14:54:25.795490
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parse import parse_json
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import String

    json = '{"name": "John"}'
    tokens = list(parse_json(json))
    token = Token(tokens=tokens)

    try:
        validate_with_positions(token=token, validator=String(min_length=3))
        assert False, 'All required fields should be present'
    except ValidationError as error:
        messages = error.messages()
        assert len(messages) == 1
        message = messages[0]
        assert message.text == "Ensure this field has at least 3 characters."
        assert message.code == "min_length"
        assert message.index == ("name",)
        assert message.start_

# Generated at 2022-06-14 14:54:35.671343
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class PersonSchema(Schema):

        name = Field(str, required=True)

        def validate_name(self, value):
            if len(value) < 3:
                raise ValidationError(
                    index=["name"], text="Name must be at least 3 characters long."
                )

    # Testing when validation error is raised from required field.
    json_body = """
    {
        "name": "J"
    }
    """
    token = Token.from_json(json_body)
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=PersonSchema)
    assert excinfo.value.messages == [
        Message(code="required", index=["name"], text="The field 'name' is required."),
    ]

   

# Generated at 2022-06-14 14:54:44.426919
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize import tokenize

    token = tokenize({"name": "example"}, "json")[0]
    validator = String(nullable=False)

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=validator)


# Generated at 2022-06-14 14:54:54.776780
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class ProductSchema(Schema):
        name = Field(required=True)
        price = Field(type=float, required=True)

    doc = """{"name": "Widget", "price": "5.5"}"""
    tree = json.loads(doc)
    token = Token.from_python(tree)
    try:
        validate_with_positions(token=token, validator=ProductSchema())
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="Value '5.5' is not a valid float.",
                code="type_error.float",
                index=("price",),
                start_position=Position(line=1, char_index=21),
                end_position=Position(line=1, char_index=26),
            )
        ]

# Generated at 2022-06-14 14:55:04.794293
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from json import loads as parse_json
    from typesystem import Compound, String

    class PersonSchema(Schema):
        name = String(required=True)
        age = String()

    class PeopleSchema(Schema):
        people = Compound(PersonSchema, compound_key="name")

    token = Token.from_value(
        parse_json(
            r"""
        {
            "people": {
                "alice": {
                    "age": "20"
                }
            }
        }
        """
        )
    )
    people = validate_with_positions(
        token=token, validator=PeopleSchema()
    )