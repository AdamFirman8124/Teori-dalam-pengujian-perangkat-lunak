

# Generated at 2022-06-14 14:45:21.423060
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.types import String

    field = String(name="test")

    token = Token(value="foobar", start={"line": 0, "char_index": 5}, end={"line": 10})

    try:
        validate_with_positions(token=token, validator=field)
    except ValidationError as e:
        message = e.messages()[0]
        assert message.text == "Value must be at most 6 characters long."
        assert message.start_position == {"line": 0, "char_index": 5}
        assert message.end_position == {"line": 10}

# Generated at 2022-06-14 14:45:27.639857
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize

    class Person(Schema):
        name = Field(str)

    payload = {"additional_data": "blah blah blah"}
    token = tokenize(payload)
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=Person)
    assert excinfo.value.messages[0].start_position.line == 1
    assert excinfo.value.messages[0].start_position.char_index == 1

# Generated at 2022-06-14 14:45:36.089209
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import json
    from typesystem.fields import Integer
    from typesystem.tokenize.tokens import ObjectToken
    from typesystem import error_messages

    value = {
        "field_a": 100,
        "field_b": 101,
    }

    def look_up(index):
        return value[index]

    token = ObjectToken(
        value=value, start=[0, 0], end=[1, 1], lookup=look_up, name="root"
    )

    required_field = Integer(required=True)
    optional_field = Integer(required=False)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=required_field)


# Generated at 2022-06-14 14:45:39.541497
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer, String  # noqa


# Generated at 2022-06-14 14:45:51.238896
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import Tokenizer
    from typesystem.types import String, Integer
    from typesystem.schemas import Schema
    from typesystem.validators import max_length, required

    tokenizer = Tokenizer()

    class PersonSchema(Schema):
        name = String(validators=[required(), max_length(2)])
        age = Integer()

    errors = []
    try:
        validate_with_positions(
            token=tokenizer.tokenize({"name": "Jane", "age": 18}), validator=PersonSchema
        )
    except ValidationError as error:
        errors = sorted(error.messages(), key=lambda e: e.start_position.char_index)

    assert errors[0].text == 'Value is too long (maximum is 2 characters).'

# Generated at 2022-06-14 14:45:59.041931
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.schemas import Schema
    from typesystem.tokenize import tokenize

    class InvalidSchema(Schema):
        name = Field(required=True)
        age = Field(required=True, type=int)

    @pytest.mark.parametrize(
        "text,key",
        [
            ('{"age": 17}', "name"),
            ('{"age": "17"}', "age"),
            ('{"name": "Alice"}', "age"),
        ],
    )
    def test_validate_with_positions(text, key):
        token = tokenize(text)
        with pytest.raises(ValidationError) as exc_info:
            validate_with_positions(token=token, validator=InvalidSchema)

        message = exc_info

# Generated at 2022-06-14 14:46:09.194935
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from pprint import pprint
    from json import loads
    from typesystem.tokenize.lexers import JsonLexer
    from typesystem.tokenize.parsers import JsonParser
    from typesystem.schemas import ObjectSchema

    class Person(ObjectSchema):
        name = String(required=True)

    # lexer = JsonLexer()
    # tokens = lexer.tokenize("""{"name": "bob"}""")
    # parser = JsonParser(tokens=tokens)
    # token = parser.parse()
    # pprint(token.as_dict())
    # validate_with_positions(token=token, validator=Person)

    lexer = JsonLexer()
    tokens = lexer.tokenize("""{"name": ""}""")
    parser = J

# Generated at 2022-06-14 14:46:19.916810
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema(
        fields={"name": Field(required=True)},
        openapi={
            "info": {
                "title": "Validate with positions",
                "version": "1.0.0",
            },
        },
    )

    data = {"name": 1}
    data_token = Token(value=data, start=Position(1, 1, 1), end=Position(1, 1, 1))

    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=data_token, validator=schema)

    error_messages = excinfo.value.messages()
    error = error_messages[0]
    assert isinstance(error, Message)
    assert error.text == "The field 'name' is required."

# Generated at 2022-06-14 14:46:28.875253
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from unitsystem import currencies, systems
    import typesystem

    class Currency(typesystem.types.String):
        pattern = currencies.valid_symbols

    class CurrencySymbols(typesystem.types.Object):
        currency_code = Currency.as_field()
        symbol = Currency.as_field()
        validated_value = lambda *args: (
            f"{args[0].currency_code} {args[0].symbol}"
        )

    class UnitSystem(typesystem.types.Object):
        name = typesystem.types.String.as_field()
        symbol = typesystem.types.String.as_field(pattern=systems.valid_symbols)
        currency = CurrencySymbols.as_field()


# Generated at 2022-06-14 14:46:38.813787
# Unit test for function validate_with_positions
def test_validate_with_positions():

    class Article(Schema):
        title = Field(str)
        author = Field(str)

    article = {
        "title": "My Article",
        "author": "123",
    }

    with pytest.raises(ValidationError) as err_info:
        validate_with_positions(token=Token(article), validator=Article)

    error = err_info.value

    assert error.messages() == [
        Message(
            code="type_error.str",
            index=("author",),
            text="Value must be a string.",
            start_position=Token(123).start,
            end_position=Token(123).end,
        )
    ]

# Generated at 2022-06-14 14:46:53.837937
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from dataclasses import dataclass
    from typesystem.fields import String, Integer
    from typesystem.tokenize import tokenize
    from typesystem.tokenize.tokens import RecordToken, FieldToken

    @dataclass
    class Record:
        field: str
        number: int

    class RecordField(Field):
        def validate(self, value):
            return Record(**value)

    class RecordSchema(Schema):
        field = String(required=True)
        number = Integer()
        record = RecordField(Schema=RecordSchema, required=False)

    value = {
        "field": "foo",
        "number": "bar",
        "record": {"field": "foo", "number": "bar"},
    }

# Generated at 2022-06-14 14:47:03.402369
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer, String

    class Basic(Schema):
        name = String()
        age = Integer()

    json = {"name": "Chris", "age": "notanumber"}
    token = Token.parse(json)
    try:
        Basic.validate(json)
    except ValidationError as e:
        position_errors = e.messages()
    try:
        validate_with_positions(token=token, validator=Basic())
    except ValidationError as e:
        validate_with_positions_errors = e.messages()
    # All messages should be the same, just with added positions
    assert position_errors == validate_with_positions_errors

# Generated at 2022-06-14 14:47:12.265957
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer

    class TestSchema(Schema):
        """Test schema class."""

        age = Integer()

    schema = TestSchema()

    token = Token.from_dict({"age": "100"})
    assert validate_with_positions(token=token, validator=schema) == {"age": 100}

    token = Token.from_dict({"age": "foo"})
    with pytest.raises(ValidationError) as ctx:
        validate_with_positions(token=token, validator=schema)
    assert ctx.value.messages()[0].start_position.char_index == 4

# Generated at 2022-06-14 14:47:23.439033
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer

    from typesystem.tokenize import tokenize

    integer_field = Integer(required=True)

    tokens = tokenize("""
{
    "a": "1",
    "b": 2,
    "c": "",
    "d": 4,
    "e": null,
    "f": false,
    "g": {
        "g": 1,
        "h": 2
    }
}
""")
    token = tokens[0]

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=integer_field)

    messages = exc_info.value.messages
    assert len(messages) == 4

    message = messages[0]

# Generated at 2022-06-14 14:47:32.082664
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import Integer
    from typesystem.tokenize.tokens import ObjectToken

    field = Integer(required=True)
    value = ObjectToken({"foo": 1}, start_position=None, end_position=None)
    assert validate_with_positions(token=value, validator=field) == {"foo": 1}

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=ObjectToken({}, start_position=None, end_position=None),
            validator=field,
        )
    assert len(exc_info.value.messages) == 1
    message = exc_info.value.messages[0]
    assert message.text == "The field 'foo' is required."
    assert message.code == "required"

# Generated at 2022-06-14 14:47:43.328962
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse
    from typesystem.schemas import Object

    class MySchema(Object):
        class Meta:
            fields = (("name", String()), ("age", Integer()))

    query = '{"name": "Anderson", "age": "thirty"}'
    token = parse(query).token()
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=MySchema)
    error = exc_info.value
    assert error.messages()[0].text == "The field 'age' is not a valid integer."
    assert error.messages()[0].start_position == token.start.move(13)

# Generated at 2022-06-14 14:47:54.888114
# Unit test for function validate_with_positions
def test_validate_with_positions():
    # A validator that raise the exact same error three times
    class Validator(Field):
        def validate(self, value):
            raise ValidationError(messages=[Message(text='Error message')])

    from typesystem.tokenize import tokenize

    token = tokenize(['hello', 'world', '!'])
    try:
        validate_with_positions(token=token, validator=Validator())
    except ValidationError as exc:
        assert len(exc.messages) == 3
        assert [m.code for m in exc.messages] == ['required'] * 3
        assert [m.text for m in exc.messages] == ['Error message'] * 3
        assert [m.start_position.line_number for m in exc.messages] == [1, 1, 2]

# Generated at 2022-06-14 14:48:02.084771
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize.lexers import JSONLexer

    field = String(max_length=5)
    lexer = JSONLexer(input='{"name": "bob"}')
    token = lexer.tokenize()
    token = token.lookup(["name"])
    validate_with_positions(token=token, validator=field)

# Generated at 2022-06-14 14:48:10.526228
# Unit test for function validate_with_positions

# Generated at 2022-06-14 14:48:22.570025
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import types
    import pytest  # type: ignore

    schema = types.Schema({"name": types.String(max_length=10)})

# Generated at 2022-06-14 14:48:38.421214
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token.from_json("{}")
    schema = Schema.define({"foo": {"type": "string"}})
    with pytest.raises(ValidationError) as excinfo:
        validate_with_positions(token=token, validator=schema)
    messages = excinfo.value.messages
    assert 1 == len(messages)
    assert messages[0].start_position == Position(line=1, column=1, char_index=0)
    assert messages[0].end_position == Position(line=1, column=1, char_index=0)



# Generated at 2022-06-14 14:48:43.605693
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize
    from typesystem.fields import String

    validator = String()
    document = """
type Person {
  name: String!
}
    """
    token = tokenize(document)
    token = token.lookup("typeDefinition.type_name.value")
    validate_with_positions(token=token, validator=validator)

# Generated at 2022-06-14 14:48:52.413444
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from json import loads
    from typesystem.tokenize import Tokenizer
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import String

    tokenizer = Tokenizer()
    token = tokenizer.parse(
        input="""
        {
          "title": "T",
          "description": "D",
          "price": null
        }
        """
    )

    class Product(Schema):
        title = String(min_length=3)
        description = String(min_length=3)
        price = String(required=True)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Product)
        assert exc_info.messages[0].text == "The field price is required."
        assert exc_

# Generated at 2022-06-14 14:49:02.801051
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, Object, String

    class Person(Object):
        name = String()
        age = Integer()

    token = Token.parse({"name": "Jane", "age": "12" })
    assert validate_with_positions(token=token, validator=Person) == {
        "name": "Jane", "age": 12 }

    token = Token.parse({"name": "Jane", "age": "twelve" })
    try:
        validate_with_positions(token=token, validator=Person)
    except ValidationError as error:
        assert error.message == "The field age must be an integer."
        assert str(error) == """The field age must be an integer.
(line: 2, column: 1)"""
    else:
        assert False, "validation should have failed!"

# Generated at 2022-06-14 14:49:05.579423
# Unit test for function validate_with_positions
def test_validate_with_positions():
    field = Field(name="name", type="string")
    token = Token(value="hello", start=10, end=15)
    result = validate_with_positions(token=token, validator=field)
    assert result == "hello"

# Generated at 2022-06-14 14:49:17.369180
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse

    # Parsing the type system spec for type definitions
    definition_schema = parse("""
    total: bool = True
    """)

    # Parsing the type system spec for a schema
    schema = parse("""
    type Foo:
        a: String(max_length=2)
    """)

    # Getting the token for the field node
    field_token = schema.lookup(["types", "Foo", "fields", "a"])

    # Getting the validator for the schema
    field = definition_schema.lookup(["String"])
    assert isinstance(field, Field)

    # Validating the the field with positions and asserting the result

# Generated at 2022-06-14 14:49:27.730520
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from .fixtures import test_schema

    token = test_schema.tokenize("{")
    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=test_schema)
    assert error.value.messages == [
        Message(
            "The field name is required.",
            "required",
            (0,),
            Position(1, 1),
            Position(1, 1),
        ),
        Message(
            "The field age is required.",
            "required",
            (1,),
            Position(1, 1),
            Position(1, 1),
        ),
    ]

# Generated at 2022-06-14 14:49:34.980116
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tests.test_tokenizer import tokenize

    token = tokenize('{"a": 1}')
    schema = Schema({"a": Field(required=True)})
    try:
        validate_with_positions(token=token, validator=schema)
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="The field 'a' is required.",
                code="required",
                index=("a",),
                start_position=token.start,
                end_position=token.end,
            )
        ]

# Generated at 2022-06-14 14:49:44.046739
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(type="string", max_length=3)

    Person().validate({"name": "Frank"})
    # is valid
    try:
        Person().validate({"name": "Joseph"})
    except ValidationError as error:
        assert error.messages() == [
            Message(
                text="Length must be less than or equal to 3.",
                code="max_length",
                index=["name"],
                start_position=Position(line=1, line_index=1, char_index=7),
                end_position=Position(line=1, line_index=1, char_index=13),
            )
        ]

# Generated at 2022-06-14 14:49:51.884865
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import parse
    from typesystem.schemas import Object
    from typesystem.fields import String, Float

    class PersonSchema(Object):
        name: String(required=True)
        age: Float(required=True)

    token = parse("{}")
    try:
        validate_with_positions(token=token, validator=PersonSchema)
    except ValidationError as error:
        messages = error.messages()

    assert len(messages) == 2
    message = messages[0]
    assert message.text == "The field 'name' is required."
    assert message.code == "required"
    assert message.index == ("name",)
    assert message.start_position == (1, 1)
    assert message.end_position == (1, 1)

    token = parse

# Generated at 2022-06-14 14:50:15.553889
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    schema = Schema(properties={"name": String()})
    message = None
    try:
        validate_with_positions(
            token=Token(value={"name": None}, start=None, end=None),
            validator=schema,
        )
    except ValidationError as error:
        message = error.messages[0]

    assert message is not None
    assert message.code == "required"
    assert message.index == ["name"]
    assert message.text == "The field 'name' is required."
    assert message.start_position is None
    assert message.end_position is None

# Generated at 2022-06-14 14:50:26.507858
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.types import Integer
    from typesystem.tokenize import tokenize

    schema = Schema.of({"id": Integer(), "name": String()})
    document = tokenize("""\
    {
        id: 42,
    }
    """)
    token = document.root
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=schema)
    messages = exc_info.value.messages
    assert len(messages) == 1
    message = messages[0]
    assert message.code == "required"
    assert message["name"] == "name"
    assert message.start_position.line_number == 2
    assert message.start_position.char_index == 6

# Generated at 2022-06-14 14:50:38.373033
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class Person(Schema):
        name = Field(str)
        age = Field(int)

    token = Token(value={"age": "abc"}, start=1, end=2)
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Person)

    message = exc_info.value.messages[0]
    assert message.text == "Value 'abc' is not valid for int."
    assert message.code == "type_error"
    assert message.start_position.line == 1
    assert message.start_position.char_index == 2
    assert message.end_position.line == 1
    assert message.end_position.char_index == 3

# Generated at 2022-06-14 14:50:46.088825
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Record, Text

    class RecordType(Record):
        name = Text(min_length=3)

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=Token(value={"name": "a"}, start=None, end=None),
            validator=RecordType,
        )
    assert exc_info.value.messages()[0].text == 'The field "name" must be at least 3 characters.'

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=Token(value={"name": "a"}, start=None, end=None),
            validator=RecordType.fields["name"],
        )

# Generated at 2022-06-14 14:50:55.220492
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import parse

    class BookSchema(Schema):
        name = Field(str)
        price = Field(int)

    token = parse({"name": "My Book", "price": "10"})

# Generated at 2022-06-14 14:51:05.158999
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        value={"a": 1, "b": 2, "c": ["foo", "bar"]},
        _tokenize={"a": 0, "b": 1, "c": [0, 1]},
    )
    assert validate_with_positions(token=token, validator=Field(type=dict)) == token.value

    token = token.lookup(["a"])
    assert validate_with_positions(token=token, validator=Field(type=int)) == token.value

    invalid_token = Token(value={"a": 1, "b": 2, "x": "foo"}, _tokenize={})

# Generated at 2022-06-14 14:51:14.772272
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.parser import Parser

    parser = Parser(reflect_metadata=False)
    token = parser.parse_literal('{"field": "foo"}')

    # Test validation error with positions
    try:
        validate_with_positions(token=token, validator=Field(format="date-time"))
    except ValidationError as error:
        assert error.messages()[0].start_position.char_index == 9
        assert error.messages()[0].end_position.char_index == 14

    # Test successful validation
    validate_with_positions(token=token, validator=Field(type="string"))

# Generated at 2022-06-14 14:51:26.789333
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem

    class TestSchema(typesystem.Schema):
        properties = {
            "foo": typesystem.String(max_length=2),
            "bar": typesystem.String(max_length=2),
        }

    class TestSchema2(typesystem.Schema):
        properties = {"foo": TestSchema()}

    class TestSchema3(typesystem.Schema):
        properties = {"foo": TestSchema2()}

    class TestSchema4(typesystem.Schema):
        properties = {"foo": TestSchema3()}

    class TestSchema5(typesystem.Schema):
        properties = {"foo": TestSchema4()}

    class TestSchema6(typesystem.Schema):
        properties = {"foo": TestSchema5()}


# Generated at 2022-06-14 14:51:37.048807
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize.helpers import tokenize

    class MyField(Field):
        py_types = (float,)
        parse_value = staticmethod(float)

    class MySchema(Schema):
        foo = MyField()

    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(
            token=tokenize("{}"), validator=MySchema(),
        )
    message = exc_info.value.messages[0]
    assert message.index == ("foo",)
    assert message.start_position.line_number == 0
    assert message.start_position.column_number == 1
    assert message.start_position.char_index == 0
    assert message.end_position.line_number == 0
    assert message.end_position.column_number

# Generated at 2022-06-14 14:51:45.653313
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class TestSchema(Schema):
        field_a = String(validators=["required"])

    data = "{}"

    with pytest.raises(ValidationError) as cm:
        validate_with_positions(token=Token(value=data), validator=TestSchema)

    message = cm.value.messages()[0]
    assert message.start_position.char_index == 1
    assert message.end_position.char_index == 2
    assert message.text == "The field 'field_a' is required."

# Generated at 2022-06-14 14:52:20.764971
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.tokenize import tokenize, PositionalFile

    from typesystem.fields import Integer
    from typesystem.schemas import Schema
    from tests.tokenize.test_tokens import Token

    class Person(Schema):
        age = Integer()

    content = '{"age": "twelve"}'
    file = PositionalFile(content)
    tokens = list(tokenize(content))
    object_token, = [token for token in tokens if token.type == "OBJECT"]
    assert validate_with_positions(token=object_token, validator=Person) == {
        "age": 12
    }



# Generated at 2022-06-14 14:52:29.626198
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import pytest
    from typesystem.tokenize.json_tokens import parse as parse_json
    from typesystem.tokenize.yaml_tokens import parse as parse_yaml
    from typesystem.schemas import Schema
    from typesystem.fields import String, Field, Integer

    schema = Schema(
        {
            "a": String(min_length=2),
            "b": String(min_length=2),
            "c": String(min_length=2),
        }
    )


# Generated at 2022-06-14 14:52:36.373347
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String

    token = Token(value={}, start=(5, 0), end=(10, 1))
    validator = String(name="foo")
    try:
        validate_with_positions(token=token, validator=validator)
    except ValidationError as error:
        assert error.message.start_position == (5, 0)
        assert error.message.end_position == (10, 1)



# Generated at 2022-06-14 14:52:46.159781
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem import Integer, Object, String

    class Address(Object):
        street = String(required=True)
        number = Integer(required=True)

    token = Token(
        {"street": "Broadway", "number": 1},
        start={"line_number": 1, "char_index": 5},
        end={"line_number": 1, "char_index": 6},
    )

    with pytest.raises(ValidationError) as exc:
        validate_with_positions(validator=Address(), token=token)
    messages = exc.value.messages

# Generated at 2022-06-14 14:52:57.511261
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.base import FieldOptions
    from typesystem.json_schema import FormattedString
    from typesystem.tokenize import tokenize_string, tokenize_dict
    from typesystem.validators import Validator

    class TestSchema(Schema):
        name = Field(validators=[Validator(if_="$required")])

    # Test validate_with_positions for FormattedString

    def required(context: typing.Any) -> bool:
        return context.get("$required")

    name_field = Field(
        options=FieldOptions(validators=[Validator(required)]),
        typed_validator=FormattedString(),
    )

    schema = Schema(fields={"name": name_field})


# Generated at 2022-06-14 14:53:05.471451
# Unit test for function validate_with_positions
def test_validate_with_positions():
    instance = {"foo": "hello"}
    token = Token(value=instance, start={}, end={})
    field = Field(name="foo", type="integer")

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=field)
    assert error.value.messages() == [
        Message(
            text="The field 'foo' was not an integer.",
            code="invalid_type",
            index=["foo"],
            start_position=None,
            end_position=None,
        )
    ]



# Generated at 2022-06-14 14:53:14.796276
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String, Integer
    from typesystem.tokenize import tokenize

    schema = Schema({"a": String(required=True), "b": Integer()})

    source = """\
{
    "a": "foo"
    "b": "bar"
}"""

    token = tokenize(source)

    with pytest.raises(ValidationError) as error:
        validate_with_positions(token=token, validator=schema)


# Generated at 2022-06-14 14:53:26.681091
# Unit test for function validate_with_positions
def test_validate_with_positions():
    token = Token(
        "value",
        start=Position(line_index=1, char_index=3),
        end=Position(line_index=1, char_index=7),
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=Field(name="something"))
    assert len(exc_info.value.messages()) == 1
    assert exc_info.value.messages()[0].start_position.line_index == 1
    assert exc_info.value.messages()[0].start_position.char_index == 3
    assert exc_info.value.messages()[0].end_position.line_index == 1
    assert exc_info.value.messages()[0].end_position.char_index

# Generated at 2022-06-14 14:53:37.439112
# Unit test for function validate_with_positions
def test_validate_with_positions():
    from typesystem.fields import String
    from typesystem.tokenize.tokens import DictToken
    from typesystem.tokenize.tokens import StringToken
    from typesystem.validators import NotNull

    field = String(validators=[NotNull()])
    dict_token = DictToken(
        start={"line": 0, "char_index": 0},
        end={"line": 1, "char_index": 0},
        value={
            "address": {
                "street": {
                    "name": StringToken(
                        start={"line": 0, "char_index": 8},
                        end={"line": 0, "char_index": 15},
                        value="",
                    )
                }
            }
        },
    )

# Generated at 2022-06-14 14:53:48.524811
# Unit test for function validate_with_positions
def test_validate_with_positions():
    class MySchema(Schema):
        name = Field(type="string")
        age = Field(type="integer")
        class Meta:
            fields = ("name", "age")


    data = [{"name": "Jane", "age": 32}]
    token = Token(data)

    schema = MySchema()
    validated = validate_with_positions(token=token, validator=schema)
    assert validated == [{"name": "Jane", "age": 32}]

    token = token.lookup("[0]")
    validated = validate_with_positions(token=token, validator=MySchema())
    assert validated == {"name": "Jane", "age": 32}

    token = token.lookup("age")
    with pytest.raises(ValidationError) as excinfo:
        validate

# Generated at 2022-06-14 14:54:52.967196
# Unit test for function validate_with_positions
def test_validate_with_positions():
    schema = Schema(fields={"x": {"type": int}, "y": {"type": int}})
    value_with_positions = {"x": {"start": {"line": 1, "char": 0}, "end": {"line": 1, "char": 1}}, "y": "three"}
    try:
        validate_with_positions(token=value_with_positions, validator=schema)
    except ValidationError as e:
        assert e.messages()[0].start_position.line == 1

# Generated at 2022-06-14 14:54:53.580479
# Unit test for function validate_with_positions
def test_validate_with_positions():
    pass

# Generated at 2022-06-14 14:55:03.880687
# Unit test for function validate_with_positions
def test_validate_with_positions():
    import typesystem.tokenize  # noqa

    class TestField(Field):
        default = "test"

    token = Token(
        type="type",
        value=None,
        file=typesystem.tokenize.SourceFile("", ""),
        line_index=0,
        char_index=0,
    )
    with pytest.raises(ValidationError) as exc_info:
        validate_with_positions(token=token, validator=TestField())
    messages = sorted(exc_info.value.messages, key=lambda m: m.start_position.char_index)
    assert messages[0].text == 'The field "value" is required.'
    assert messages[0].start_position.line_index == 0
    assert messages[0].start_position.char_index == 0
    assert messages

# Generated at 2022-06-14 14:55:14.688287
# Unit test for function validate_with_positions
def test_validate_with_positions():
    def assert_ok(text, validator):
        token = Token.parse_string(text)
        validate_with_positions(token=token, validator=validator)

    assert_ok("foo", Schema(properties=[("foo", Field(name="foo", type="string"))]))

    def assert_raises(text, validator):
        token = Token.parse_string(text)
        with pytest.raises(ValidationError):
            validate_with_positions(token=token, validator=validator)

    assert_raises("", Schema(properties=[("foo", Field(name="foo", type="string"))]))
    assert_raises('{"foo": 42}', Schema(properties=[("foo", Field(name="foo", type="string"))]))