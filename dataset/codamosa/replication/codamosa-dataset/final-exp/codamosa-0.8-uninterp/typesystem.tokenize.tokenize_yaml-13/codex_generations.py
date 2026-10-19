

# Generated at 2022-06-14 14:56:31.619076
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    pydict = {"a": 6, "b": [1, 2, 3], "c": {"d": "e"}, "f": "g", "h": []}
    expected = {
        "a": 6,
        "b": [1, 2, 3],
        "c": {"d": "e"},
        "f": "g",
        "h": []
    }
    content = "a: 6\nb:\n  - 1\n  - 2\n  - 3\nc:\n  d: e\nf: g\nh: []"
    token = tokenize_yaml(content)
    assert token == expected


# Generated at 2022-06-14 14:56:37.444923
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml(content=b'{"age": 42, "name": "Morty"}')
    assert type(token) == DictToken
    assert len(token) == 2
    assert token["age"] == ScalarToken(42, 12, 13)
    assert token["name"] == ScalarToken("Morty", 29, 35)



# Generated at 2022-06-14 14:56:43.781730
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Anything, Float, Integer, String, TypedDict
    from typesystem.schemas import Schema

    class UserSchema(Schema):
        name = String()
        age = Integer()

    user_schema = UserSchema()

    class User(TypedDict):
        name: str
        age: int

    content = """
    name: Pranav
    age: 23
    """

    value, error_messages = validate_yaml(content, user_schema)
    assert error_messages == []
    assert value == {'name': 'Pranav', 'age': 23}

    content = """
    name: Pranav
    age: 23
    a: 1
    """

    value, error_messages = validate_yaml(content, UserSchema)


# Generated at 2022-06-14 14:56:52.399048
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    schema = Schema([String("hello")])

    # Successful YAML
    yaml_text = "hello: world"
    value, errors = validate_yaml(yaml_text, schema)
    assert value == {"hello": "world"}
    assert errors is None

    # Failing YAML
    yaml_text = "hello: 4"
    value, errors = validate_yaml(yaml_text, schema)
    assert errors == [
        Message(
            text="Value must be a string.",
            code="invalid",
            type="value_error.string",
            position=Position(line_no=1, column_no=7, char_index=7),
        )
    ]

    # YAML parse

# Generated at 2022-06-14 14:56:57.756336
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    valid_yaml = '''
test:
    - foo: bar
    - baz: true
    - bar: []
    - baz: {}
    '''
    actual_result = tokenize_yaml(valid_yaml)
    expected_result = {
        "test": [
            {"foo": "bar"},
            {"baz": True},
            {"bar": []},
            {"baz": {}},
        ]
    }
    assert actual_result == expected_result

# Generated at 2022-06-14 14:57:06.685894
# Unit test for function validate_yaml
def test_validate_yaml():
    # pylint: disable=redefined-outer-name, unused-variable
    from typesystem.fields import String, Integer, DateTime
    from typesystem.schemas import Schema

    # pylint: disable=too-few-public-methods

    class Animal(Schema):
        type = String()
        age = Integer()

    class Person(Schema):
        name = String(format="name")
        email = String(format="email")
        birthday = DateTime()
        pets = List(Animal)

    yaml = """
    name: Fred Jones
    email: invalid-email-address
    birthday: 1987-12-13
    pets:
        - type: Dog
          age: 12
        - type: Cat
          age: 7
        - type: Monkey
          age: 6
    """
    response = validate

# Generated at 2022-06-14 14:57:08.810158
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        first_name = String()
        last_name = String()
        age = Integer()

    validate_yaml(content="""first_name: Alice
last_name: Smith
age: 30""", validator=MySchema)



# Generated at 2022-06-14 14:57:19.797040
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    # Test for empty content
    content = '{}'
    validator = {
        "a": {"type": int}
    }
    assert validate_yaml(content, validator) == ({}, [])

    # Test for simple validator type string to int
    content = '{"a": "1"}'
    assert validate_yaml(content, validator) == ({"a": 1}, [])

    # Test for simple validator type int to str
    validator = {
        "a": {"type": int}
    }
    content = '{"a": "1"}'
    assert validate_yaml(content, validator) == ({"a": 1}, [])

    # Test for simple validator type int to float

# Generated at 2022-06-14 14:57:23.407368
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    word = "word"
    content = "content"
    char_index = 0
    tokenize_yaml_output = tokenize_yaml(content)
    assert(isinstance(tokenize_yaml_output, Token))



# Generated at 2022-06-14 14:57:28.529369
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    yaml_str = """
    hello: world
    """
    token = tokenize_yaml(document=yaml_str)
    assert (
        type(token) == DictToken
    ), f"YAML dict as root should return DictToken, not {type(token)}"
    assert token.value == {"hello": "world"}

# Generated at 2022-06-14 14:57:40.482459
# Unit test for function validate_yaml
def test_validate_yaml():
    """Test validate_yaml()"""
    from typesystem import types
    from typesystem.schemas import Schema

    class TestSchema(Schema):
        first_name = types.String()

    value, error_messages = validate_yaml(
        """
        first_name: John
        last_name: Doe
        """,
        validator=TestSchema,
    )
    assert error_messages
    assert 'last_name' in error_messages

    value, error_messages = validate_yaml(
        """
        first_name: John
        """,
        validator=TestSchema,
    )
    assert not error_messages

# Generated at 2022-06-14 14:57:50.905600
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # dictionary
    dict_yaml = """
    foo: bar
    lorem: ipsum
    """
    dict_token = tokenize_yaml(dict_yaml)
    assert isinstance(dict_token, DictToken)
    assert dict_token.value == {"foo": "bar", "lorem": "ipsum"}
    assert dict_token.indexes == (0, 22)

    dict_token = tokenize_yaml(dict_yaml.encode())
    assert isinstance(dict_token, DictToken)
    assert dict_token.value == {"foo": "bar", "lorem": "ipsum"}
    assert dict_token.indexes == (0, 22)

    # list
    list_yaml = """
    - a
    - b
    - c
    """
    list_

# Generated at 2022-06-14 14:57:52.211076
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert 'tokenize_yaml' == 'tokenize_yaml'


# Generated at 2022-06-14 14:57:59.102032
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema.from_spec(
        name="MySchema",
        fields={
            "Name": {"type": "string", "title": "Name of the person"},
            "Age": {"type": "integer", "title": "Age of the person"},
        },
    )

    value, error_messages = validate_yaml(
        b"""
    Name: 'John'
    Age: -20
    """,
        validator=schema,
    )
    print(error_messages)



# Generated at 2022-06-14 14:58:06.553359
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    import typesys
    from typesystem.types import String, Boolean

    class Quote(typesys.Schema):
        body = String()
        favorite = Boolean(default=False)

    quote = """
    body: Hello, world.
    favorite: true
    """

    value, _ = validate_yaml(quote, Quote)
    assert value == {"body": "Hello, world.", "favorite": True}

    # Parse error
    with pytest.raises(typesys.ParseError) as excinfo:
        validate_yaml("fdsa", Quote)

    message = excinfo.value.message
    assert message.text == "Unexpected ':' while looking for the next token."

    # Validation error

# Generated at 2022-06-14 14:58:14.544500
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    str_content = """
        simple: a simple value
        list:
        - one
        - two
        - three
        """
    token = tokenize_yaml(str_content)

    assert token.content == str_content
    assert token.start == 0
    assert token.end == len(str_content)

    assert isinstance(token, DictToken)
    assert len(token) == 2

    a = token[0]
    assert isinstance(a, DictToken)
    assert len(a) == 2
    assert a.get_start() == a.start
    assert a.get_end() == a.end
    assert a.get_content() == a.content[a.start:a.end]
    assert a.get_text() == "simple: a simple value"


# Generated at 2022-06-14 14:58:25.145472
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = typing.Type[Schema]
    field = typing.Type[Field]

    assert validate_yaml(
        """
        name: test
        email: test@example.com
        age: 23
    """,
        field=field,
    ) == (
        {
            "name": "test",
            "email": "test@example.com",
            "age": 23,
        },
        [],
    )

    assert validate_yaml("", field=field) == ({}, [])

    assert validate_yaml("", schema=schema) == ({}, [])

    # class SomeSchema(Schema):
    #    pass

    # assert validate_yaml("", schema=SomeSchema) == ({}, [])


# Generated at 2022-06-14 14:58:30.170067
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Arrange
    content = """
    # A dictionary
    a:
      # A list
      - b
      - c
    """
    expected = {'a': ['b', 'c']}
    # Act
    token = tokenize_yaml(content)
    actual = yaml.load(content, yaml.SafeLoader)
    # Assert
    assert token.value == expected
    assert token.value == actual


# Generated at 2022-06-14 14:58:34.854092
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

if __name__ == '__main__':
    import pytest, sys
    errno = pytest.main(['-x', '--pdb', __file__])
    sys.exit(errno)

# Generated at 2022-06-14 14:58:43.722704
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml(b'{#comment\n"foo": "bar"}')
    assert isinstance(token, DictToken)
    assert token._start == 1
    assert token._end == 19

    scalar_tokens = list(token.values())
    assert isinstance(scalar_tokens[0], ScalarToken)
    assert scalar_tokens[0].value == 'foo'
    assert scalar_tokens[0]._start == 10
    assert scalar_tokens[0]._end == 13

    assert isinstance(scalar_tokens[1], ScalarToken)
    assert scalar_tokens[1].value == 'bar'
    assert scalar_tokens[1]._start == 16

# Generated at 2022-06-14 14:58:50.177441
# Unit test for function validate_yaml
def test_validate_yaml():
    from tests.schemas import Employee

    content = 'name: "Prateek"\nage: 32\naddress: "Hyderabad"'

    errors = validate_yaml(content=content, validator=Employee)

    assert not errors

# Generated at 2022-06-14 14:58:55.036711
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(
        fields={"name": Field(str)}
    )

    try:
        value, errors = validate_yaml(content="{}", validator=schema)
        print(value)
        print(errors)
    except ParseError as exc:
        print(exc)



# Generated at 2022-06-14 14:59:07.354203
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("null") == None
    assert tokenize_yaml("null") == None
    assert tokenize_yaml("true") == ScalarToken(True,0,3)
    assert tokenize_yaml("[1.0,2.0]") == ListToken([1.0,2.0],0,9)
    assert tokenize_yaml("[1,2]") == ListToken([1,2],0,4)
    assert tokenize_yaml("[a,b]") == ListToken(['a','b'],0,4)
    assert tokenize_yaml("""{a: 2.0, b: "test"}""") == DictToken({'a': 2.0, 'b': 'test'},0,20)

# Generated at 2022-06-14 14:59:16.550045
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("")
    # print(token)
    assert token == []
    # print("========================================")
    token = tokenize_yaml("[]")
    # print(token)
    assert token == []
    # print("========================================")
    token = tokenize_yaml("{}")
    # print(token)
    assert token == {}
    # print("========================================")
    token = tokenize_yaml(":-")
    # print(token)
    assert token == []
    # print("========================================")
    token = tokenize_yaml("a: a")
    # print(token)
    assert token == {"a": "a"}
    # print("========================================")
    token = tokenize_yaml("a")
    # print(token)
    assert token == "a"


# Generated at 2022-06-14 14:59:20.287161
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml(
        """
    foo:
        bar: 1
        baz: 2
    """
    ) == {
        "foo": {
            "bar": 1,
            "baz": 2,
        }
    }



# Generated at 2022-06-14 14:59:26.935186
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # test scalar
    assert isinstance(tokenize_yaml("foo"), ScalarToken)
    assert tokenize_yaml("foo").value == "foo"
    assert tokenize_yaml("40").value == 40
    assert tokenize_yaml("40.0").value == 40.0
    assert tokenize_yaml("true").value == True

    # test list
    assert isinstance(tokenize_yaml('[1, 2, "foo"]'), ListToken)
    assert tokenize_yaml('[1, 2, "foo"]').value == [1, 2, "foo"]

    # test dict
    assert isinstance(
        tokenize_yaml('{"foo": [1, 2, "foo"], "bar": "baz"}'), DictToken
    )

# Generated at 2022-06-14 14:59:35.615134
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        username = StringField(max_length=50)
        first_name = StringField(max_length=50, required=False)
        last_name = StringField(max_length=50, required=False)

    schema = UserSchema()
    yaml_content = """
    username: Test User
    first_name: Test
    last_name: User
    """

    token, errors = validate_yaml(content=yaml_content, validator=schema)
    assert not errors

    yaml_content = """
    username: Test User who is too long!
    first_name: Test
    last_name: User
    """

    _, errors = validate_yaml(content=yaml_content, validator=schema)
    assert errors

# Generated at 2022-06-14 14:59:41.740413
# Unit test for function validate_yaml
def test_validate_yaml():
    with open('test_validate_yaml.yaml') as f:
        document = yaml.safe_load(f)
    assert yaml is not None, "'pyyaml' must be installed."
    assert document is not None, "file must be readable"

    token = tokenize_yaml(document)
    return validate_with_positions(token=token, validator=validator)


# Generated at 2022-06-14 14:59:51.047223
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(
        content=b"""{
            "integer": 42,
            "string": "value"
        }""",
        validator=Schema(
            fields={
                "integer": {"type": "integer"},
                "string": {"type": "string"},
            }
        ),
    ) == (
        {"integer": 42, "string": "value"},
        [],
    )


# Generated at 2022-06-14 14:59:59.731469
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = "Person"
        fields = {"first_name": "string", "last_name": "string"}

    content = "first_name: Ken\nlast_name: Reitz"
    validator = PersonSchema()

    result, error_messages = validate_yaml(content, validator)
    json_result = json.dumps(result, indent=2)

    assert (
        json_result
        == '{'
        '  "first_name": "Ken",'
        '  "last_name": "Reitz"'
        "}"
    )

# Generated at 2022-06-14 15:00:09.291814
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        first_name = String(max_length=100)
        last_name = String(max_length=100)
        age = Integer(minimum=0, maximum=150)

    result = validate_yaml(
        b"""first_name: Test
            last_name: Test
            age: 10""",
        validator=Person
    )
    assert result.is_valid

# Generated at 2022-06-14 15:00:17.554887
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer, Boolean
    from typesystem.schemas import Schema
    from typesystem.schemas import schema
    from typesystem.schemas import data_validator

    @schema
    class Person(Schema):
        name = String()
        age = Integer(minimum=1, maximum=150)
        retired = Boolean()
    
    content = '''name: Jane Doe
age: 42
retired: false'''
    
    assert validate_yaml(content, validator=Person) == \
        (
            {
                'age': 42,
                'name': 'Jane Doe',
                'retired': False
            },
            []
        )

# Generated at 2022-06-14 15:00:23.267483
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        """
        A test schema for Testing
        """
        a = Integer(maximum=10)

    test_string = "a: 11"
    assert validate_yaml(test_string, TestSchema) == (None, [Message(text="Must be at most 10.", code="max_value", position=Position(column_no=4, line_no=1, char_index=4))])

# Generated at 2022-06-14 15:00:30.425273
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('"foo"') is "foo"
    assert tokenize_yaml('foo') is "foo"
    assert tokenize_yaml('123') == 123
    assert tokenize_yaml('-123') == -123
    assert tokenize_yaml('123.0') == 123.0
    assert tokenize_yaml('-123.0') == -123.0
    assert tokenize_yaml('1.0e4') == 10000.0
    assert tokenize_yaml('1.0e-4') == 0.0001
    assert tokenize_yaml('true') is True
    assert tokenize_yaml('false') is False
    assert tokenize_yaml('null') is None
    assert tokenize_yaml('[1, 2, 3]') == [1, 2, 3]


# Generated at 2022-06-14 15:00:40.258928
# Unit test for function validate_yaml
def test_validate_yaml():
    # Error message when content is bad
    content = '''
    x: 100
    y: -100
    '''
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    value, error_messages = validate_with_positions(token=token, validator=Schema)
    assert error_messages == [Message(
        code='unknown_field',
        position=Position(char_index=9, column_no=4, line_no=2),
        text='Unknown field `x`',
    )]
    assert value == {}

    # Good content
    content = '''
    x: 100
    y: -100
    '''
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    value, error_messages

# Generated at 2022-06-14 15:00:48.611318
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, String

    # This is what a user would do.
    class UserSchema(Schema):
        name = String(max_length=10)
        age = Integer()

    # Validation returns a two-tuple of (value, error_messages)
    (value, error_messages) = validate_yaml(
        """
        name: 3
        age: "10"
        """,
        validator=UserSchema,
    )
    assert error_messages and error_messages[0].position == Position(
        line_no=2, column_no=2, char_index=11
    )

# Generated at 2022-06-14 15:00:51.672947
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    test: hello
    """
    validator = Field(type="string")
    expected = ("hello", [])
    assert expected == validate_yaml(content, validator)

# Generated at 2022-06-14 15:01:03.942572
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = types.StringType(min_length=1)
        age = types.IntegerType(minimum=0)

    error, value = validate_yaml(content=b'{"name": "John", "age": 20}', validator=PersonSchema)
    assert not error
    assert isinstance(value, dict)
    assert value == {'name': 'John', 'age': 20}

    error, value = validate_yaml(content=b'{"name": "John", "age": -1}', validator=PersonSchema)
    assert not error
    assert isinstance(value, dict)
    assert value == {'name': 'John', 'age': -1}


# Generated at 2022-06-14 15:01:13.032664
# Unit test for function validate_yaml
def test_validate_yaml():
    from flask import Flask
    from flask_restx import Api, Namespace, fields, Resource
    from typesystem.contrib.flask.fields import String, Integer
    import pytest

    app = Flask(__name__)
    api = Api(app)

    test_ns = api.namespace("Test", description="Test description")

    # Test that an empty string produces an error
    with pytest.raises(typesystem.ParseError):
        validate_yaml("", validator=String())

    # Test with a valid YAML string
    valid_yaml = "hello"
    value, errors = validate_yaml(valid_yaml, validator=String())
    assert value == "hello"
    assert errors == []

    # Test with an invalid YAML string
    invalid_yaml = "123"


# Generated at 2022-06-14 15:01:22.015868
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    class PetSchema(Schema):
        name = Field(type="string")
        age = Field(type="number")
        size = Field(type="string", enum=["small", "medium"], required=False)

    error_messages, valid_data = validate_yaml(
        b"""
    name: Fluffy
    age: 10
    size: medium
    """,
        PetSchema,
    )
    assert error_messages is None
    assert valid_data == {
        "name": "Fluffy",
        "age": 10,
        "size": "medium",
    }

    # If a string is passed to validate_yaml and it's not valid YAML, we'll still
    # do our best to return a helpful parse error

# Generated at 2022-06-14 15:01:32.133321
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer

    class Person(Schema):
        name = String()
        age = Integer()

    content = """
        name: John
        age: 20
        """

    value, errors = validate_yaml(content, Person)
    assert value == {"name": "John", "age": 20}
    assert len(errors) == 0



# Generated at 2022-06-14 15:01:43.465721
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    a: 10
    b: 'hello'
    c:
        - 20
        - 'world'
    d:
        message: 'This is a message'
        code: 'ABC123'
    e:
        -
            message: 'This is a message'
            code: 'ABC123'
        -
            message: 'This is another message'
            code: 'XYZ789'
        -
            message: 'This is another message'
            code: 'XYZ789'
    """


# Generated at 2022-06-14 15:01:55.448716
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("""{
            "name": "foo",
            "age": 10,
            "type": "bar",
            "tags": [1, 2, 3],
            "options": {
                "a": 1,
                "b": 2
            },
            "is_enabled": true
        }""") == {
        "name": "foo",
        "age": 10,
        "type": "bar",
        "tags": [1, 2, 3],
        "options": {"a": 1, "b": 2},
        "is_enabled": True,
    }
    assert tokenize_yaml("""{"foo": "bar", "baz": "qux"}""") == {
        "foo": "bar",
        "baz": "qux",
    }
    assert tokenize_

# Generated at 2022-06-14 15:02:03.894555
# Unit test for function validate_yaml
def test_validate_yaml():
    content = io.StringIO(u'''
    {
        "foo": [{
            "bar" : "baz"
        }]
    }
    ''')
    class MySchema(Schema):
        foo = Field(type=list, items=Field(type=dict, fields={
            "bar": Field(type=str),
        }))

    value, _ = validate_yaml(content=content, validator=MySchema())
    assert value == {"foo": [{"bar": "baz"}]}

# Generated at 2022-06-14 15:02:12.265191
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    if yaml is None:
        print("\nThe following tests depend on pyyaml being installed.")
        return
    from typesystem import Integer, Object, String

    class Pet(Object):
        name = String()

    class Person(Object):
        name = String()
        age = Integer(required=False)
        pet = Pet()

    def check(*args, **kwargs):
        value, errors = validate_yaml(*args, **kwargs)
        errors_text = [error.text for error in errors]
        if errors_text == ["Required field 'name' is missing."]:
            raise AssertionError(errors_text[0])
        if errors_text == ["Value at 'pet' is invalid."]:
            raise AssertionError(errors_text[0])
    

# Generated at 2022-06-14 15:02:22.466039
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    name: Foo
    age: 3
    nested:
        name: Bar
        age: 5
    """
    class MySchema(Schema):
        name = String(min_length=6, max_length=10)
        age = Integer(minimum=1)
        nested = Object({"name": String(), "age": Integer()})
        description = String()
    value, errors = validate_yaml(content, validator=MySchema)

# Generated at 2022-06-14 15:02:32.815236
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    yaml_content = \
    """
    code: 1
    message: "some message"
    """

    value, error_message = validate_yaml(
        yaml_content,
        Schema.of(
            code=int(validators=[greater_than(0)], required=True),
            message=str()
        )
    )

    assert isinstance(error_message, list)
    assert len(error_message) == 1
    assert "code" in error_message[0]
    assert error_message[0]["code"] == "value_must_be_greater_than"
    assert "message" in error_message[0]
    assert error_message[0]["message"] == "value should be greater than 0."

# Generated at 2022-06-14 15:02:42.107892
# Unit test for function validate_yaml
def test_validate_yaml():

    class PersonSchema(Schema):
        name = String(min_length=1, max_length=100)
        age = Integer(minimum=0, maximum=150)

    errors = validate_yaml(
        b"{}",
        validator=PersonSchema,
    )[1]
    assert len(errors) > 0
    assert "name" in errors
    assert "age" in errors

    errors = validate_yaml(
        b"{name: Bryan, age: 133}",
        validator=PersonSchema,
    )[1]
    assert len(errors) == 0



# Generated at 2022-06-14 15:02:51.930498
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class Person(Schema):
        name = String()

    content = yaml.dump(dict(name="Bob"))
    Person.validate(content)

    content = yaml.dump(dict(name=123))
    with pytest.raises(ValidationError) as exc_info:
        Person.validate(content)

    # Check the error message.
    error_message = exc_info.value.as_dict()
    assert error_message["message"] == "This value is not a valid string."
    assert error_message["position"] == {"column_no": 5, "line_no": 1}

# Generated at 2022-06-14 15:03:01.389024
# Unit test for function validate_yaml
def test_validate_yaml():
  content = """
  foo:
    - bar: baz
  """

  class MySchema(Schema):
    foo = ListField(DictField({"bar": StringField()}))

  token, error_messages = validate_yaml(content, MySchema)
  assert len(error_messages) == 0
  assert type(token) is DictToken
  assert token.start == 0
  assert token.end == len(content) - 1
  assert token.content == content
  assert token.value == {"foo": [{"bar": "baz"}]}

  content = """
  foo: bar
  """

  class MySchema(Schema):
    foo = StringField(required=False)
    bar = StringField(required=False)


# Generated at 2022-06-14 15:03:11.398764
# Unit test for function validate_yaml
def test_validate_yaml():

    desired_output = (
        {'a': 1, 'b': 2},
        [],
    )
    assert desired_output == validate_yaml("a: 1 \nb: 2",{"a": int, "b": int})

    desired_output = (
        {'a': 1, 'b': 2},
        [],
    )
    assert desired_output == validate_yaml("a: 1 b: 2", {"a": int, "b": int})

    desired_output = ({'a': 1, 'b': 2}, [])
    assert desired_output == validate_yaml("""a: 1\nb: 2""", {"a": int, "b": int})

    desired_output = (
        {'a': 1, 'b': 2},
        [],
    )
    assert desired_output == validate_

# Generated at 2022-06-14 15:03:22.788242
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer, Float
    from typesystem.schemas import Schema

    class PersonSchema(Schema):
        name = String(required=True)
        age = Integer(required=True)
        salary = Float(required=True)

    yaml_content = """
    name: John
    age: 30
    salary: 40000.0
    """
    value, errors = validate_yaml(yaml_content, PersonSchema)
    assert value == {
        'name': 'John',
        'age': 30,
        'salary': 40000.0
    }
    assert errors == []

    yaml_content = """
    name:
    age: 25
    salary:
    """
    value, errors = validate_yaml(yaml_content, PersonSchema)
    assert value

# Generated at 2022-06-14 15:03:26.639408
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
        core:
            value: 10
            message: "This is the message"
            valid: true
            nothing: null
    """
    class CoreField(Field):
        value = fields.Integer(required=True)
        message = fields.String(required=True)
        valid = fields.Boolean(required=True)
        nothing = fields.String()
    errors = validate_yaml(content, CoreField())
    assert errors == []


# Generated at 2022-06-14 15:03:37.066791
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''\
    name:     Steve Rogers
    age:      106
    gender:   Male
    location: New York
    '''
    schema = Schema(
        {"name": str, "age": int, "gender": str, "location": str}
    )
    assert validate_yaml(content, schema) == ({'name': 'Steve Rogers', 'age': 106, 'gender': 'Male', 'location': 'New York'}, None)

    content = '''\
    name:     
    age:      106
    gender:   Male
    location: New York
    '''
    schema = Schema(
        {"name": str, "age": int, "gender": str, "location": str}
    )

# Generated at 2022-06-14 15:03:45.370789
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """a:
      b: 1
      c: true"""
    validator = Schema({"a": {"b": Field(int), "c": Field(bool)}})

    errors = []

    class DummyMessageClass(Message):
        def add(self, *args, **kwargs):
            errors.append((args, kwargs))

    messages = DummyMessageClass()
    value, _errors = validate_yaml(content, validator, messages=messages)
    assert value == {"a": {"b": 1, "c": True}}
    assert errors == []

# Generated at 2022-06-14 15:03:48.720701
# Unit test for function validate_yaml
def test_validate_yaml():
    content=b"---\n- 1"
    validator=typing.List[int]
    r=validate_yaml(content, validator)
    print(r)



# Generated at 2022-06-14 15:03:52.796732
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    a: b
    c:
      d: e
    """

    class MySchema(Schema):
        a = Field()
        c = Field(type=dict)

    assert validate_yaml(content, MySchema) == ({'a': 'b', 'c': {'d': 'e'}}, [])

# Generated at 2022-06-14 15:03:55.685321
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "a: 1"
    field = Field(name="a", type="integer")
    (value, errors) = validate_yaml(content=content, validator=field)
    assert value == 1

# Generated at 2022-06-14 15:04:03.819138
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String

    validator = String()

    # Valid input
    content = '""'
    value, error_messages = validate_yaml(content, validator)
    assert value == ""
    assert error_messages == []

    # Invalid input
    content = '"hello"'
    value, error_messages = validate_yaml(content, validator)
    assert value == None
    assert len(error_messages) == 1
    message = error_messages[0]
    assert message.text == "Validation failed for field 'string'"
    assert message.type == Message.TYPE_ERROR
    assert message.code == "invalid"
    assert message.position.line_no == 1
    assert message.position.column_no == 1
    assert message.position.char_index == 0

    # Missing

# Generated at 2022-06-14 15:04:12.798421
# Unit test for function validate_yaml
def test_validate_yaml():
    from yaml import load_all
    from io import StringIO
    from typesystem import Schema, fields, parse_error, validation_error
    from typesystem.tokenize.tokens import (
        ErrorToken,
        Token,
        parse_token,
        validate_token,
        tokenize,
    )
    from typesystem.tokenize.positional_validation import (
        validate_with_positions,
        get_error_messages,
    )
    import json
    with open('examples/contract.yaml', 'r') as stream:
        data = stream.read()
    print('data: ', data)
    result = validate_yaml(data, fields.Array())
    print('result: ', result)
    assert type(result[1]) == Message
    assert type(result[0]) == list

# Generated at 2022-06-14 15:04:26.406516
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    class NoticeSchema(Schema):
        title = Field(type=str)
        text = Field(type=str)

    schema = NoticeSchema()
    errors = schema.validate_yaml('''
        title: Invalid Notice
        text: This is an invalid notice.
    ''')
    assert not errors

    errors = schema.validate_yaml('''
        title: Invalid Notice
        text: This is an invalid notice.
        extra_key: extra value
    ''')
    assert errors
    assert len(errors) == 1
    assert errors[0].text == "Additional properties are not allowed ('extra_key' was unexpected)."

# Generated at 2022-06-14 15:04:36.894594
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import IntegerField
    from typesystem.schemas import Schema
    from typesystem.tokenize import validate_yaml

    s = Schema({"number": IntegerField(minimum=0, maximum=10)})

    # Valid YAML
    assert validate_yaml(b"number: 2", s) == (
        {"number": 2},
        [],
    )

    # Invalid YAML
    value, errors = validate_yaml(b"!", IntegerField())
    assert len(errors) == 1
    assert errors[0].code == "parse_error"

    # Invalid value
    value, errors = validate_yaml(b"number: 11", s)
    assert value == {"number": 11}
    assert len(errors) == 1



# Generated at 2022-06-14 15:04:46.819010
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Initialize the expected values for testing
    expected_dict_token = {}
    expected_list_token = ['test', 'list']
    expected_scalar_token = ['test', 'scalar']
    expected_int_token = ['test', 'int']
    expected_float_token = ['test', 'float']
    expected_bool_token = ['test', 'bool']
    expected_null_token = ['test', None]

    # Test that the yaml parser parses the yaml string into a tokens
    # containing the expected value
    assert tokenize_yaml(
        'test: dict'
    ) == expected_dict_token, 'tokenize_yaml failed to parse yaml string'


# Generated at 2022-06-14 15:04:57.228062
# Unit test for function validate_yaml
def test_validate_yaml():
    # Success case
    mock_token = DictToken({"foo": "bar"}, start=0, end=10, content="\nfoo: bar")
    mock_schema = Field(name="mock-field", required=True, field_type=str)
    (
        returned_value,
        returned_error_messages,
    ) = validate_with_positions(mock_token, mock_schema)
    assert returned_value == "bar"
    assert returned_error_messages is None

    # Failure case
    mock_token = DictToken({"foo": "bar"}, start=0, end=10, content="\nfoo: bar")
    mock_schema = Field(name="mock-field", required=True, field_type=int)

# Generated at 2022-06-14 15:05:07.152122
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(properties={"foo": Field(type="str")})
    valid, errors = validate_yaml("foo: '123'", schema)
    assert valid == {"foo": "123"} and errors is None
    valid, errors = validate_yaml("foo: 123", schema)
    assert errors == [
        Message(
            text="Expected a string but got a integer.",
            code="type_error",
            position=Position(column_no=5, line_no=1, char_index=4),
            validator="type",
            value=123,
            path=("foo",),
        )
    ]
    valid, errors = validate_yaml("invalid", schema)

# Generated at 2022-06-14 15:05:13.961163
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String(max_length=20, min_length=5)
        age = Integer()
        height = Float()
        male = Boolean()

    content = """
    name: "John Doe"
    age: 33
    height: 1.80
    male: True
    """

    value, error_messages = validate_yaml(content, Person)
    assert value.name == "John Doe"
    assert value.age == 33
    assert value.height == 1.80
    assert value.male is True
    assert len(error_messages) == 0

# Generated at 2022-06-14 15:05:24.844203
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(
        {
            "name": String(required=True),
            "age": Integer(minimum=0, maximum=150),
            "currently_employed": Boolean(),
            "address": String(),
            "birth_date": Date(format="%Y%m%d"),
            "skills": String(choices=["python", "django", "postgres", "javascript"]),
        }
    )

    content = """
        name: John Doe
        age: 35
        currently_employed: yes
        birth_date: 19760329
    """
    value, errors = validate_yaml(content, schema)


# Generated at 2022-06-14 15:05:33.328138
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(
        content=b'{"a": "b"}', 
        validator={"type": 'str', "pattern": "^[0-9]+$"},
    ) == (
        {"a": "b"},
        [Message(code="invalid_pattern", text="a does not match regular expression '^[0-9]+$'.", position=Position(line_no=1, column_no=4, char_index=4))],
    )

# Generated at 2022-06-14 15:05:38.106409
# Unit test for function validate_yaml
def test_validate_yaml():
    if yaml is None: return
    validator = Schema.from_string("""
    type: object
    properties:
      name:
        type: string
      age:
        type: integer
    """)

    (value, errors) = validate_yaml("{name: 'foo'}", validator)
    assert isinstance(errors, ValidationError)
    assert errors[0]["code"] == "missing_property"



# Generated at 2022-06-14 15:05:44.062362
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = String()

    (errors, matched) = validate_yaml("name: John", PersonSchema)
    assert errors == []
    assert matched == {"name": "John"}

    (errors, matched) = validate_yaml("xyz", PersonSchema)
    assert len(errors) == 1
    assert errors[0].code == "parse_error"   # YAML parser error

# Generated at 2022-06-14 15:06:00.675184
# Unit test for function validate_yaml
def test_validate_yaml():
    import sys
    import typesystem

    def validate_yaml_with_messages(content, validator):
        (value, error_messages) = validate_yaml(content, validator)
        return value, error_messages

    def run_test(content, validator):
        try:
            (value, error_messages) = validate_yaml(content, validator)
        except typesystem.ParseError as e:
            print("PARSE ERROR: ", e.position, e.text)
            sys.exit(1)
        except typesystem.ValidationError as e:
            print("VALIDATION ERROR")
            for message in e.messages:
                print("  ", message.position, message.text)
            sys.exit(1)


# Generated at 2022-06-14 15:06:07.715116
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.validators import Not
    from typesystem.fields import Integer
    from typesystem.schemas import Schema

    class MySchema(Schema):
        foo = Integer(validators=[Not(1)], required=True)

    s = MySchema()
    result = validate_yaml(
        b"""foo: 1""",
        s
    )
    assert result[1] == [
        Message(
            text="'1' must not equal '1'.",
            code="does_not_equal",
            field=s.fields["foo"],
            position=Position(
                line_no=1, column_no=5, char_index=4
            ),
        ),
    ]
    assert result[0] is None
