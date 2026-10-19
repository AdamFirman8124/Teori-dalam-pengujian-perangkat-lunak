

# Generated at 2022-06-14 14:56:33.453293
# Unit test for function validate_yaml
def test_validate_yaml():
    class RobotSchema(Schema):
        name = fields.String()
        battery_level = fields.Float(min_value=0, max_value=100)

    content = """
    name: Wall-e
    battery_level: 4.0
    """

    value, error_messages = validate_yaml(content, RobotSchema)

    assert value == {"name": "Wall-e", "battery_level": 4.0}
    assert not error_messages

    content = """
    name: Wall-e
    battery_level: wall-e
    """

    _, error_messages = validate_yaml(content, RobotSchema)
    assert len(error_messages) == 1
    assert error_messages[0].code == "type_error.float"

# Generated at 2022-06-14 14:56:37.444523
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""---
    foo:
        bar: baz
    """)
    assert isinstance(token, DictToken)
    assert token.value == {'foo': {'bar': 'baz'}}



# Generated at 2022-06-14 14:56:39.985742
# Unit test for function validate_yaml
def test_validate_yaml():
    val, errors = validate_yaml(
        content="foo: bar", validator=typesystem.Dict({"foo": typesystem.String()})
    )
    assert val == {"foo": "bar"}
    assert errors == []

# Generated at 2022-06-14 14:56:47.396855
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test that function works when str is passed as argument
    test_str = "a: b"
    token = tokenize_yaml(test_str)
    assert(token.value == {"a": "b"})
    # Test that function works when bytes is passed as argument
    test_bytes = bytes("a: b", 'utf-8')
    token = tokenize_yaml(test_bytes)
    assert(token.value == {"a": "b"})


# Generated at 2022-06-14 14:56:55.574022
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String

    content = """
    name: test name
    age: "01"
    """

    validator = {
        "name": String(max_length=5),
        "age": String(max_length=2),
    }

    value, error_messages = validate_yaml(content, validator)

    assert len(error_messages) == 2
    assert error_messages[0].position.char_index == 12
    assert error_messages[0].text == "Value is too long."
    assert error_messages[1].position.char_index == 22
    assert error_messages[1].text == "Value is too long."

# Generated at 2022-06-14 14:57:05.803214
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.types import String  # noqa

    field = String(min_length=1)
    content = "Hello, World!"
    value, error_messages = validate_yaml(content, field)
    assert value == "Hello, World!"
    assert error_messages == []

    content = "Hello, World!"
    value, error_messages = validate_yaml(content, field)
    assert value == "Hello, World!"
    assert error_messages == []

    content = b"Hello, World!"
    value, error_messages = validate_yaml(content, field)
    assert value == "Hello, World!"
    assert error_messages == []

    field = String(min_length=20)  # noqa
    content = "Hello, World!"
    value, error_messages = validate_

# Generated at 2022-06-14 14:57:16.968224
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("") == ""
    assert tokenize_yaml("  ") == ""
    assert tokenize_yaml("\n\n") == ""

    assert tokenize_yaml('"foo"') == ScalarToken("foo", 0, 4, content='"foo"')
    assert tokenize_yaml("'foo'") == ScalarToken("foo", 0, 4, content="'foo'")

    assert tokenize_yaml("123") == ScalarToken(123, 0, 2, content="123")
    assert tokenize_yaml("12.3") == ScalarToken(12.3, 0, 3, content="12.3")
    assert tokenize_yaml(".123") == ScalarToken(0.123, 0, 4, content=".123")

# Generated at 2022-06-14 14:57:27.976831
# Unit test for function validate_yaml
def test_validate_yaml():
    # pylint: disable=global-statement
    global tokenize_yaml, validate_yaml

# Generated at 2022-06-14 14:57:34.867900
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("{}") == DictToken({}, 0, 0)
    assert tokenize_yaml("[]") == ListToken([], 0, 0)
    assert tokenize_yaml("3") == ScalarToken(3, 0, 0)
    assert tokenize_yaml("3.0") == ScalarToken(3.0, 0, 2)
    assert tokenize_yaml("true") == ScalarToken(True, 0, 3)
    assert tokenize_yaml("false") == ScalarToken(False, 0, 4)
    assert tokenize_yaml("null") == ScalarToken(None, 0, 3)
    assert tokenize_yaml("test") == ScalarToken("test", 0, 3)

# Generated at 2022-06-14 14:57:44.515993
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    with pytest.raises(ParseError):
        tokenize_yaml("[a: 1, b: 2]")

    with pytest.raises(ParseError):
        tokenize_yaml("{a: [1, 2, 3]}")

    with pytest.raises(ParseError):
        tokenize_yaml("{a: 'hello'}")

    with pytest.raises(ParseError):
        tokenize_yaml("[1, 2, 3, 4]")

    assert tokenize_yaml("{a: '2'}") == {'a': '2'}
    assert tokenize_yaml("[1, 2, 3, 4]") == [1, 2, 3, 4]
    assert tokenize_yaml("[a: 2]") == {'a': 2}

# Generated at 2022-06-14 14:57:52.531924
# Unit test for function validate_yaml
def test_validate_yaml():
    value, error_messages = validate_yaml(
        'string: "hello world"',  # type: ignore[func-returns-value]
        Schema([
            Field(name="string", type="string"),
        ]),
    )
    print(value)
    print(error_messages)

# Generated at 2022-06-14 14:57:59.307799
# Unit test for function validate_yaml
def test_validate_yaml():
    from unittest.mock import Mock
    from unittest.mock import call
    from typesystem.fields import String

    schema = Mock()
    value = "bar"
    errors = []
    schema.validate = Mock()
    schema.validate.return_value = value
    validate_yaml("foo: bar", schema)
    schema.validate.assert_called_once_with(value)
    validate_yaml("foo: bar", String())
    assert schema.validate.call_count == 2
    # Testing the default case
    token = tokenize_yaml("foo: bar")
    validate_with_positions(token=token, validator=String())
    assert schema.validate.call_count == 3

# Generated at 2022-06-14 14:58:03.888173
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import SchemaField
    from typesystem.schemas import Schema

    class ChatMessage(Schema):
        text = SchemaField(str)

    assert validate_yaml(b"foo: 'bar'\n", ChatMessage) == {
        "text": "bar"
    }



# Generated at 2022-06-14 14:58:13.000038
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "python"
    field = Field(type="number")
    with pytest.raises(ValidationError, match="Expected a number."):
        validate_yaml(content, field)

    content = "123"
    field = Field(type="str")
    with pytest.raises(ValidationError, match="Expected a string."):
        validate_yaml(content, field)

    class TestSchema(Schema):
        name = Field(type="string")

    content = {"name": 123}
    with pytest.raises(ValidationError, match="Expected a string."):
        validate_yaml(content, TestSchema)

    content = {"name": 123}
    field = Field.many(type="string")

# Generated at 2022-06-14 14:58:23.981032
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(name="age", type="number")
    # Test valid case
    yaml_input = b"age: 45"
    result = validate_yaml(content=yaml_input, validator=validator)
    assert isinstance(result, typing.Tuple)
    assert (result[0] == 45)
    assert (result[1] == {})
    # Test invalid case with error message
    yaml_input = b"""age: 45
    name: Bob
    """
    result = validate_yaml(content=yaml_input, validator=validator)
    assert isinstance(result, typing.Tuple)
    assert (result[0] == 45)
    assert (isinstance(result[1], Message))
    assert ("name" in result[1].context)
    # Test error case with multiple

# Generated at 2022-06-14 14:58:32.232971
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    {
      "int": "1",
      "float": "2.2",
      "bool": "true",
      "null": "null",
      "list": [
        "1",
        "2"
      ],
      "dict": {
        "key": "value"
      }
    }
    """
    content = \
    '''{
      "int": "1",
      "float": "2.2",
      "bool": "true",
      "null": "null",
      "list": [
        "1",
        "2"
      ],
      "dict": {
        "key": "value"
      }
    }'''

    token = tokenize_yaml(content)

    # print(token.value)
    # print(yaml.dump(token,

# Generated at 2022-06-14 14:58:39.827235
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema([
            Field("foo", type=String()),
            Field("bar", type=Integer()),
            Field("baz", type=Boolean())
        ])
    content = """
    bar: 1
    foo: hello
    baz: true
    """
    print("\n\n---- Test validate_yaml ----")
    print("\nContent:\n", content)
    print("\nSchema:\n",schema)
    print("\nResult:\n", validate_yaml(content, validator=schema))

# Generated at 2022-06-14 14:58:46.746817
# Unit test for function validate_yaml
def test_validate_yaml():
    from .utils import is_validation_error

    class MySchema(Schema):
        prop = Field(type="string")

    result = validate_yaml('prop: "hello"', MySchema)
    assert isinstance(result, tuple) and len(result) == 2
    assert result[0] == {"prop": "hello"}
    assert result[1] == []

    result = validate_yaml('prop: "hello"\nfoo: 123', MySchema)
    assert isinstance(result, tuple) and len(result) == 2
    assert result[0] == {"prop": "hello"}

    error_message = result[1]
    assert isinstance(error_message, list) and error_message

    error = error_message[0]
    assert isinstance(error, Message)
    assert is_validation_

# Generated at 2022-06-14 14:58:55.728923
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, String, Integer, Float, Boolean, Enum, Array, Object, Dict
    from typesystem.fields import Field
    d = """
    name: "John Doe"
    age: 45
    """
    class Foo(Schema):
        name = String(max_length=10)
        age = Integer()
    class Person(Schema):
        name = String(max_length=10)
        age = Integer(minimum=18)
        active = Boolean(default=True)
        foo = Foo()
        some_list = Array(items=Enum(choices=["one", "two", "three"]))
        active = Boolean(default=True)
        family_member = Array(items=Person())
        some_dict = Dict(keys=String(), values=Integer())

# Generated at 2022-06-14 14:58:58.725041
# Unit test for function validate_yaml
def test_validate_yaml():
    content ='"hello"'
    schema = typing.List(typing.String)
    assert validate_yaml(content, schema) == ([], [])


# Generated at 2022-06-14 14:59:13.453549
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(tokenize_yaml("1"), ScalarToken)
    assert isinstance(tokenize_yaml("1.1"), ScalarToken)
    assert isinstance(tokenize_yaml("true"), ScalarToken)
    assert isinstance(tokenize_yaml("false"), ScalarToken)
    assert isinstance(tokenize_yaml("null"), ScalarToken)
    assert isinstance(tokenize_yaml("'abc'"), ScalarToken)
    assert isinstance(tokenize_yaml('"abc"'), ScalarToken)
    assert isinstance(tokenize_yaml("""["abc"]"""), ListToken)
    assert isinstance(tokenize_yaml("""{'abc':'def'}"""), DictToken)



# Generated at 2022-06-14 14:59:23.043450
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = typing.Dict[str, typing.Optional[str]]

    value, messages = validate_yaml("""foo: bar""", validator)
    assert value == {'foo': 'bar'}

    value, messages = validate_yaml("""foo: null""", validator)
    assert value == {'foo': None}

    value, messages = validate_yaml("""foo: null, bar: baz""", validator)
    assert value == {'foo': None, 'bar': 'baz'}

    value, messages = validate_yaml("""foo: bar, bar: null""", validator)
    assert value == {'foo': 'bar', 'bar': None}

    value, messages = validate_yaml("""foo: bar, bar: baz, baz: null""", validator)

# Generated at 2022-06-14 14:59:33.440359
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String
    from typesystem.base import validate

    field = String(min_length=2, max_length=4)

    value, error_messages = validate_yaml(
        b"name: Luke Skywalker\n", field
    )  # type: ignore
    assert value == "Luke Skywalker"
    assert not error_messages

    value, error_messages = validate_yaml(
        b"name: T\n", field
    )  # type: ignore
    assert value is None
    assert [str(message) for message in error_messages] == [
        'Problems in field "name":',
        '"T" is shorter than the minimum length (2).',
    ]


# Generated at 2022-06-14 14:59:40.252624
# Unit test for function validate_yaml
def test_validate_yaml():
    try:
        import yaml
    except ImportError:  # pragma: no cover
        assert True, "YAML test requires pyyaml"
        return
    validator = Schema.of({"test": String()})
    text = """test: a"""
    result, messages = validate_yaml(content=text, validator=validator)
    assert result == {"test": "a"}

# Generated at 2022-06-14 14:59:50.249796
# Unit test for function validate_yaml
def test_validate_yaml():
    """Unit test for function validate_yaml."""
    from typesystem import Integer
    from pytest import raises

    # When `validate_yaml` is called with a string that is not valid YAML
    # Then a `ParseError` is raised.
    with raises(ParseError, match="No content."):
        validate_yaml("", Integer(required=True))

    with raises(ParseError, match="expected '<document start>', but found '<block mapping start>'"):
        validate_yaml("key: value", Integer(required=True))

    # When `validate_yaml` is called with a valid YAML string that is not valid
    # for the provided validator (e.g. it is a string but the validator is
    # an integer)
    # Then a list of ValidationError is

# Generated at 2022-06-14 14:59:56.132684
# Unit test for function validate_yaml
def test_validate_yaml():

    yaml_text = """
    version: 1.0
    name: 'Foo Bar'
    """
    class MySchema(Schema):
        name = types.String()
    token, error_messages = validate_yaml(content=yaml_text, validator=MySchema)
    print(token)
    print(error_messages)

# Generated at 2022-06-14 15:00:04.222501
# Unit test for function validate_yaml
def test_validate_yaml():
    # validator is a schema
    class TestSchema(Schema):
        name = fields.String()
        age = fields.Integer()
        date_joined = fields.DateTime()
        is_admin = fields.Boolean()
        balance = fields.Number()

    content = """
    name: Joe Bloggs
    age: 42
    is_admin: true
    date_joined: '2013-08-06T05:03:00Z'
    balance: 100.00
    """

    value, errors = validate_yaml(content, validator=TestSchema)


# Generated at 2022-06-14 15:00:15.483717
# Unit test for function validate_yaml
def test_validate_yaml():

    # step 1: create field
    field = Field(name="x", type_name="string")

    # step 2: create schema
    class TestSchema(Schema):
        class Meta:
            fields = [field]

    # step 3: validate
    assert validate_yaml(content='{"x": "abc"}', validator=field)[0] == "abc"
    assert validate_yaml(content='{"x": 1}', validator=field)[1][0].validator_name \
        == "string"

    assert validate_yaml(content='{"x": "abc"}', validator=TestSchema)[0] == {"x": "abc"}
    assert validate_yaml(content='{"x": 1}', validator=TestSchema)[1][0].validator_name \
        == "string"

# Generated at 2022-06-14 15:00:17.846456
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(tokenize_yaml(''), Token)

# Unit tests for function validate_yaml

# Generated at 2022-06-14 15:00:27.083458
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String
    from typesystem.schemas import Schema
    from typesystem.tokenize.positional_validation import validate_with_positions
    from typesystem.tokenize.tokens import DictToken, ScalarToken

    class UserSchema(Schema):
        name = String(max_length=10)
        age = Integer(minimum=0, maximum=120)

    # valid data
    value, messages = validate_yaml(
        content="""-
  name: "John Doe"
  age: 23
-
  name: "Jane Doe"
  age: 45""",
        validator=UserSchema,
    )

# Generated at 2022-06-14 15:00:40.206692
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content1 = """
    foo: bar
    baz:
      - this
      - is
      - a
      - list
    """
    result1 = tokenize_yaml(content1)
    assert type(result1) == DictToken
    assert result1["foo"] == "bar"
    assert type(result1["baz"]) == ListToken
    assert result1["baz"][2] == "a"

    content2 = "1"
    result2 = tokenize_yaml(content2)
    assert result2 == 1

    content3 = "true"
    result3 = tokenize_yaml(content3)
    assert result3 == True

    content4 = "false"
    result4 = tokenize_yaml(content4)
    assert result4 == False

    content5 = "null"


# Generated at 2022-06-14 15:00:43.615438
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Unit test for validate_yaml
    """
    content = """
    id: 1
    name: test
    """
    validator = Schema({"id": "integer", "name": "string"})
    value, errs = validate_yaml(content, validator)

    assert value["id"] == 1
    assert value["name"] == "test"
    assert errs == []

# Generated at 2022-06-14 15:00:52.205929
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    - Cat
    - Dog
    - Bird
    """
    inputs = ["Cat", "Dog", "Bird"]
    token = tokenize_yaml(content)
    assert inputs == token.value
    validator = ListToken(inputs, start=0, end=0, content=content)
    value, error_messages = validate_with_positions(token, validator)
    assert value == inputs
    assert error_messages == []

    content = """
    name : Zarl
    age : 20
    """
    inputs = {"name": "Zarl", "age": "20"}
    token = tokenize_yaml(content)
    assert inputs == token.value
    validator = DictToken(inputs, start=0, end=0, content=content)
    value, error_messages

# Generated at 2022-06-14 15:00:58.092372
# Unit test for function validate_yaml
def test_validate_yaml():

    class PersonSchema(Schema):
        name = fields.String(max_length=10)
        age = fields.Integer()

    person = validate_yaml("""\
name: Cassandra
age: 42
""", PersonSchema)

    assert isinstance(person, dict)
    assert person["name"] == "Cassandra"
    assert person["age"] == 42



# Generated at 2022-06-14 15:01:09.767984
# Unit test for function validate_yaml
def test_validate_yaml():
    # parse and validate a YAML string, returning positionally marked error messages on parse or validation failures
    class Person(Schema):
        name = Field(String(), max_length=50)
        age = Field(Integer())

    assert validate_yaml(
        content='''name: "John Doe"
age: 100''',
        validator=Person,
    ) == ({"name": "John Doe", "age": 100}, [])

    value, messages = validate_yaml(
        content='''name: "John Doe"
age: "str"''',
        validator=Person,
    )
    assert value == {"name": "John Doe", "age": "str"}

# Generated at 2022-06-14 15:01:18.263394
# Unit test for function validate_yaml
def test_validate_yaml():
    # Given
    class MySchema(Schema):
        my_field = Field(required=False, primative=int)

    # When
    value, errors = validate_yaml(content="my_field: 123", validator=MySchema)

    # Then
    assert isinstance(value, DictToken)
    assert isinstance(errors, list)
    assert len(errors) == 0
    assert value["my_field"] == 123
    assert value.get_position(position_index=0) == Position(line_no=1, column_no=1, char_index=0)



# Generated at 2022-06-14 15:01:20.495441
# Unit test for function validate_yaml
def test_validate_yaml(): 
    content = b"some_content: 5"
    validator = {"some_content": typesystem.Integer()}
    assert validate_yaml(content, validator)

# Generated at 2022-06-14 15:01:32.401075
# Unit test for function validate_yaml
def test_validate_yaml():
    class Article(Schema):
        title = String(required=True)
        description = String(required=True)
        body = String(required=True)
        tags = Array(of_type=String(required=True), required=True)

    value, errors = validate_yaml(
        content=b"""
        title: "title"
        description: "description"
        body: "body"
        tags:
          - tag1
          - tag2
          - tag3
        """,
        validator=Article(),
    )
    assert errors == []
    assert isinstance(value, Article)
    

# Generated at 2022-06-14 15:01:43.720327
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = "Example"
        fields = [
            Field(name="value", type_name="string", required=True),
        ]

    value, errors = validate_yaml(b"value: one", TestSchema)
    assert value == "one"
    assert errors == []

    value, errors = validate_yaml(b"value: 1", TestSchema)
    assert value == "1"
    assert errors == []

    # No errors are raised for extra keys.
    value, errors = validate_yaml(b"value: one\ntwo: 2", TestSchema)
    assert value == "one"
    assert errors == []

    value, errors = validate_yaml(b"", TestSchema)

# Generated at 2022-06-14 15:01:50.979450
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(type="string")
    value, errors = validate_yaml("Nimish", validator)
    assert value == "Nimish"
    assert errors == []

    value, errors = validate_yaml("", validator)
    assert value is None
    assert errors[0].text == "String value expected ('')."

if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 15:02:06.849708
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class ValidationSchema(Schema):
        a = String()
        b = String()

    content = '"a": "foo",\n"b": "bar"'
    schema = ValidationSchema()
    output = validate_yaml(content=content, validator=schema)
    assert isinstance(output, tuple)
    assert len(output) == 2
    value = output[0]
    errors = output[1]
    assert value == {"a": "foo", "b": "bar"}
    assert errors == []

    content = '"a": "foo",\n"b": "bar",\n'
    output = validate_yaml(content=content, validator=schema)
    assert isinstance(output, tuple)

# Generated at 2022-06-14 15:02:10.249473
# Unit test for function validate_yaml
def test_validate_yaml():
    sample_schema = Schema.from_dict({"title": {"type": "string"}})
    sample_content = "title: my title"
    result, errors = validate_yaml(content=sample_content, validator=sample_schema)
    assert result == {"title": "my title"}
    assert not errors



# Generated at 2022-06-14 15:02:12.142597
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(content="foo: bar", validator=Schema({}))

# Generated at 2022-06-14 15:02:16.740151
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    try to validate an empty yaml string.
    """
    schema = Schema("root", {"x": Integer()}, content=True)
    yaml_str = ""
    validate_yaml(content=yaml_str, validator=schema)

# Generated at 2022-06-14 15:02:19.705975
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    errors = validate_yaml(content=b"{}", validator=String(max_length=10))
    assert type(errors) == list



# Generated at 2022-06-14 15:02:27.674866
# Unit test for function validate_yaml
def test_validate_yaml():
    input_string = "test: 123"
    field = Field(type=str)
    value, error_messages = validate_yaml(input_string, field)
    assert error_messages == [ValidationError(
        text="Expected a string value.",
        code="invalid_type",
        position=Position(line_no=1, column_no=8, char_index=7),
    )]

# Generated at 2022-06-14 15:02:35.158926
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String, Integer
    from typesystem.schemas import Schema
    from typesystem.schemas import MissingValue

    class TestSchema(Schema):
        test = Integer()

    content = 'test: "invalid"'
    value, messages = validate_yaml(content, validator=TestSchema)

    assert messages == [
        {
            "text": "Does not match Integer type.",
            "code": "invalid_type",
            "position": {"line_no": 1, "column_no": 1, "char_index": 0},
        }
    ]

    content = 'test: ["invalid"]'
    value, messages = validate_yaml(content, validator=TestSchema)


# Generated at 2022-06-14 15:02:39.893820
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = Field(str)
        age = Field(int)

    content = """\
name: Bob
age: 42
    """
    messages = validate_yaml(content, validator=Person)
    assert len(messages) == 0



# Generated at 2022-06-14 15:02:47.701280
# Unit test for function validate_yaml
def test_validate_yaml(): 
    def tester(inp_content, schema, expected_value, expected_messages):
        """
        inp_content - the yaml string to be tested
        schema - the schema to evaluate inp_content against
        expected_value - the expected value returned by validate_yaml
        expected_messages - the expected error messages returned by validate_yaml
        """
        value, messages = validate_yaml(inp_content, schema)
        assert value == expected_value
        assert messages == expected_messages # messages[0].code == expected_messages[0].code
    
    from typesystem import String, Number, Boolean


# Generated at 2022-06-14 15:02:58.175999
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String
    from typesystem.schemas import Schema

    class AuthorSchema(Schema):
        name = String(max_length=100)

    class BookSchema(Schema):
        title = String(max_length=100)
        author = AuthorSchema()

    yaml_str = """
    title: This is a book
    author:
      name: This is an author
    """

    value, error_msgs = validate_yaml(yaml_str, validator=BookSchema)
    assert(error_msgs == [])

    yaml_str = """
    title: This is a book
    """

    value, error_msgs = validate_yaml(yaml_str, validator=BookSchema)

# Generated at 2022-06-14 15:03:10.316963
# Unit test for function validate_yaml
def test_validate_yaml():
    input = '''
    uuid: "d2923d06-9fba-41d8-84d2-d6b3844c3e88"
    name: "Pizza"
    price: 35
    '''
    field = {
        "uuid": {"type": "string", "format": "uuid"},
        "name": "string",
        "price": "number",
        "description": {"type": "string", "required": False},
    }
    schema = Schema(field)
    value, errors = validate_yaml(input, schema)
    assert len(errors) == 0
    assert value["uuid"] == "d2923d06-9fba-41d8-84d2-d6b3844c3e88"
    assert value["name"] == "Pizza"


# Generated at 2022-06-14 15:03:21.976272
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String

    class Example(Schema):
        name = String()
        age = Integer()

    content = "name: Jane Doe\nage: abc"
    (value, error_messages) = validate_yaml(content, Example)
    assert len(error_messages) == 1
    assert error_messages[0].position.line_no == 2
    assert error_messages[0].position.column_no == 5

    content = "name: Jane Doe\nage: 42"
    (value, error_messages) = validate_yaml(content, Example)
    assert error_messages == []

    content = "name: Jane Doe"
    (value, error_messages) = validate_yaml(content, Example)
    assert len(error_messages) == 1


# Generated at 2022-06-14 15:03:32.280033
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String, Integer

    field = Integer()
    value, error_messages = validate_yaml(
        """
        a: "123"
        b: "456"
        c: "789"
        """,
        validator=field,
    )
    assert value == 123
    assert error_messages == {
        "b": [Message(text="This value should be an integer.", code="invalid_type")],
        "c": [Message(text="This value should be an integer.", code="invalid_type")],
    }

    schema = Schema(
        {"a": String(), "b": String(), "c": String()}, metas={"foo": "bar"}
    )

# Generated at 2022-06-14 15:03:39.122177
# Unit test for function validate_yaml
def test_validate_yaml():
    class Item(Schema):
        name = String()

    data = b"""
    - name: foo
    - name: bar
    - name: 1.23
    """

    value, error_messages = validate_yaml(data, validator=List(Item))
    assert error_messages == [
        Message(
            text="Must be of type 'string'.",
            code="invalid_type",
            position=Position(
                line_no=4, column_no=4, char_index=22, path=["2", "name"]
            ),
        )
    ]

# Generated at 2022-06-14 15:03:49.873264
# Unit test for function validate_yaml
def test_validate_yaml():

    # Test missing content case
    with pytest.raises(ParseError) as excinfo:
        validate_yaml("", str) # type: ignore

    assert str(excinfo.value) == "parse_error (1:1): No content."

    # Test string content with invalid YAML
    with pytest.raises(ParseError) as excinfo:
        validate_yaml("not yaml content", str) # type: ignore

    assert str(excinfo.value) == "parse_error (1:1): could not found expected '<document start>'."

    # Test bytes content with invalid YAML
    with pytest.raises(ParseError) as excinfo:
        validate_yaml(b"not yaml content", str) # type: ignore


# Generated at 2022-06-14 15:03:56.809320
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    hello: world
    foo: 1
    """

    validator = Schema({"hello": fields.String(), "foo": fields.Integer()})
    try:
        value = validate_yaml(content, validator)
    except ValueError:
        print("oh no")
    else:
        print("yes")

    # Returns tuple of value and error_messages.
    value, error_messages = validate_yaml(content, validator)
    # Returns an empty list if no errors on validation.
    assert isinstance(error_messages, collections.abc.Iterable)
    assert not error_messages

# Generated at 2022-06-14 15:04:04.615326
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Boolean, Integer, String

    class PersonSchema(Schema):
        first_name = String(max_length=100)
        last_name = String(max_length=100)
        age = Integer(minimum=0, maximum=200)

    class NewPersonSchema(Schema):
        first_name = String(max_length=100)
        age = Integer(minimum=0, maximum=200)
        is_validated = Boolean()
        is_submitted = Boolean()

    class UpdatePersonSchema(Schema):
        first_name = String(max_length=100, required=False)
        age = Integer(minimum=0, maximum=200, required=False)
        is_validated = Boolean(required=False)
        is_submitted = Boolean(required=False)

    # Test valid case


# Generated at 2022-06-14 15:04:13.278928
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String(required=True)
        age = Integer(minimum=0)

    # Valid input
    assert validate_yaml(b"name: Joe", Person) == ({"name": "Joe"}, [])

    assert validate_yaml(b"name: Joe\nage: 10", Person) == ({"name": "Joe", "age": 10}, [])

    # Invalid input
    errors = validate_yaml(b"name: Joe\nage: -10", Person)[1]
    assert errors == [Message(text="-10 is less than the minimum of 0.", code="minimum")]

    # Example output:
    #
    # validate_yaml(b"name: Joe\nage: -10", Person)[1]
    # [Message(text="-10 is less than the minimum of 0

# Generated at 2022-06-14 15:04:23.921600
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem import ValidationError
    from typesystem.tokenize.tokens import DictToken, ScalarToken, ListToken

    class Person(Schema):
        full_name = String(min_length=5)

    error_message = """
    [{"code": "required", "text": "This field is required.", "position": {"column_no": 11, "line_no": 1, "char_index": 10}}, {"code": "min_length", "text": "Must be at least 5 characters long.", "position": {"column_no": 11, "line_no": 1, "char_index": 10}}]
    """
    content = """
    full_name: 
    """
    assert validate_yaml

# Generated at 2022-06-14 15:04:30.886810
# Unit test for function validate_yaml
def test_validate_yaml():
    print('\n\n')
    print('===============================================')
    print('| Unit test for function validate_yaml       |')
    print('===============================================')
    from typesystem import String, Boolean
    from typesystem.schemas import Schema

    class TestSchema(Schema):
        name = String()
        is_active = Boolean()

    content = str(
        """
        name: "Test"
        is_active: true
        """
    )
    value, error = validate_yaml(content, validator=TestSchema)
    print('content: ', content)
    print('value, error: ', value, error)



# Generated at 2022-06-14 15:04:42.515617
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = "TestSchema"
        age = Field(type="integer")

    content = b"name: str"
    TestSchema.validate(content)
    value, errors = validate_yaml(content, TestSchema)

    assert errors[0].message == "Field 'age' is required."
    assert errors[0].position == Position(line_no=1, column_no=1, char_index=0)

# Generated at 2022-06-14 15:04:48.380637
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String
    field = String(max_length=3)
    value, error_messages = validate_yaml('"string"', field)
    assert value=="string"
    assert error_messages==[]

    value, error_messages = validate_yaml('"longer"', field)
    assert value=="longer"
    assert error_messages==[Message(text="Must be less than or equal to 3 characters.", type="max_length", position=Position(line_no=1, column_no=1, char_index=0))]

# Generated at 2022-06-14 15:04:58.170940
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    from typesystem import Schema, fields

    content = """
        # A person's first and last names.
        first: John
        last: Smith
        age: 28
        """

    class Person(Schema):
        first = fields.String(max_length=10, required=True)
        last = fields.String(max_length=10, required=True)
        age = fields.Integer(min_value=18, max_value=60, required=True)

    person, errors = validate_yaml(content, Person)
    assert errors is None
    assert person == {"first": "John", "last": "Smith", "age": 28}
    assert isinstance(person, dict)


# Generated at 2022-06-14 15:05:07.688237
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    class MySchema(typesystem.Schema):
        name = typesystem.String(
            min_length=2, max_length=10, pattern="*(a|b)"
        )
        email = typesystem.String(format="email")
    parsed_value, errors = validate_yaml(
'''
name: abcdef
email: john@example.com
''',
        validator=MySchema
    )
    assert parsed_value == {
        'name': 'abcdef',
        'email': 'john@example.com'
    }
    assert errors == None

    parsed_value, errors = validate_yaml(
'''
name: a
email: john@example.com
''',
        validator=MySchema
    )
    assert parsed_value == None

# Generated at 2022-06-14 15:05:15.852973
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String, Integer, List, Float, Boolean

    class BookSchema(Schema):
        title = String()
        author = String()
        pages = Integer()
        price = Float()

    class AuthorSchema(Schema):
        name = String()
        age = Integer()
        books = List(item=BookSchema)
        living = Boolean(default=True)

    author_schema = AuthorSchema()

    content = """
    name: "Stephen King"
    books:
      - title: "The Shining"
        author: "Stephen King"
        pages: 447
        price: 10.99
    """
    value, errors = validate_yaml(content=content, validator=author_schema)
    assert len(errors) == 1

# Generated at 2022-06-14 15:05:20.797923
# Unit test for function validate_yaml
def test_validate_yaml():
    doc = '''
        - foo
        - bar
        - baz
    '''
    v, m = validate_yaml(doc, ListField(
        child=StringField()
    ))
    assert v == ['foo', 'bar', 'baz']
    assert m == []

# Generated at 2022-06-14 15:05:22.243452
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(type="boolean")
    content = "true"
    expected = (True, [])
    actual = validate_yaml(content, field)
    assert expected == actual

# Generated at 2022-06-14 15:05:26.372048
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "name: test"
    validator = Field.build(
        type="string",
        description="The name of the user.",
        name='name',
        choices=['test', 'validation'],
    )

    value, error_messages = validate_yaml(content, validator)

    assert value == 'test'
    assert len(error_messages) == 0



# Generated at 2022-06-14 15:05:37.567321
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    def assert_token(token, type_, start, end):
        assert isinstance(token, type_)
        assert token.start == start
        assert token.end == end

    content = "foo: bar"
    token = tokenize_yaml(content)
    assert_token(token, DictToken, 0, 7)
    assert isinstance(token.parameters[0], ScalarToken)
    assert isinstance(token.parameters[1], ScalarToken)

    token = tokenize_yaml(content.encode("utf-8"))
    assert_token(token, DictToken, 0, 7)
    assert isinstance(token.parameters[0], ScalarToken)
    assert isinstance(token.parameters[1], ScalarToken)

    content = "foo:\n  bar"
    token = tokenize

# Generated at 2022-06-14 15:05:47.361396
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    from typesystem.schemas import Schema
    from typesystem.fields import String
    from typesystem.types import _String, _Dict, _List
    assert validate_yaml('s', String()) == ('s', [])
    assert validate_yaml(
        's', String(required=True)) == ('s', [])
    assert validate_yaml(
        '0', String()) == ('0', [])
    assert validate_yaml(
        '', String(required=True)) == ('', ['Value is required.'])
    assert validate_yaml(
        '', String()) == ('', [])
    assert validate_yaml(
        '', String(required=True)) == ('', ['Value is required.'])
    assert validate_yaml

# Generated at 2022-06-14 15:06:03.646637
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, String, Schema
    
    class SimpleSchema(Schema):
        name = String(max_length=10)
        age = Integer(minimum=21)

    content = "name: Sam\nage: 38"
    value, error_messages = validate_yaml(content, validator=SimpleSchema)
    assert value == {"name": "Sam", "age": 38}
    assert not error_messages

    content = "name: Susan\nage: 18"
    value, error_messages = validate_yaml(content, validator=SimpleSchema)
    assert value == {"name": "Susan", "age": 18}

# Generated at 2022-06-14 15:06:06.733928
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(content = (str, "This is a title of the article"))
    title = validate_yaml("content: This is a title of the article", schema)
    assert title[0]['content'] == "This is a title of the article"

# Generated at 2022-06-14 15:06:17.660724
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        field1 = Field(type=int)
        field2 = Field(type=str)

    content = "field1: 'abcd'\nfield2: 1234"
    value, errors = validate_yaml(content, TestSchema)
    assert errors == [
        ValidationError(  # field1
            text="Must be a valid integer.",
            code="invalid_type",
            position=Position(column_no=7, line_no=1, char_index=6),
        ),
        ValidationError(  # field2
            text="Must be a valid string.",
            code="invalid_type",
            position=Position(column_no=9, line_no=2, char_index=21),
        ),
    ]

