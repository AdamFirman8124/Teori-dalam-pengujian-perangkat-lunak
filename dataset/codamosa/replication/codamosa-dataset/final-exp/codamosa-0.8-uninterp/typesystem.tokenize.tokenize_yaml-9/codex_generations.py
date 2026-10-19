

# Generated at 2022-06-14 14:56:33.650172
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('"hello"') == ScalarToken("hello", 0, 6, content='"hello"')
    assert tokenize_yaml("- - 3.0\n  - 2.0") == ListToken([[ScalarToken(3.0, 4, 7, content="- - 3.0\n  - 2.0")], [ScalarToken(2.0, 11, 14, content="- - 3.0\n  - 2.0")]], 0, 16, content="- - 3.0\n  - 2.0")

# Generated at 2022-06-14 14:56:40.921402
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Tests scalar tokens
    string_token = tokenize_yaml("foo: bar")
    assert isinstance(string_token, DictToken)
    assert string_token.fields == {"foo": "bar"}
    assert string_token.start_index == 0
    assert string_token.end_index == 7
    assert string_token.content == "foo: bar"

    # Tests integer tokens
    int_token = tokenize_yaml("100")
    assert isinstance(int_token, ScalarToken)
    assert int_token.start_index == 0
    assert int_token.end_index == len("100")
    assert int_token.content == "100"
    assert int_token.value == 100

    # Test float tokens
    float_token = tokenize_yaml("123.456")
    assert isinstance

# Generated at 2022-06-14 14:56:47.396558
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(
        b"""
        foo: 1
        bar: 'hello'
        baz: [1,2,3,4]
        """,
        {'foo': int, 'bar': str, 'baz': [int]},
    ) == ({'foo': 1, 'bar': 'hello', 'baz': [1, 2, 3, 4]}, [])



# Generated at 2022-06-14 14:56:56.813983
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        email = EmailType()
        age = IntegerType()

    content = """
    age: "not a number"
    email: not an email address
    """

    value, error_messages = validate_yaml(content=content, validator=TestSchema())

    assert value is None
    assert len(error_messages) == 2

    age_error = error_messages[0]
    assert isinstance(age_error, ValidationError)
    assert age_error.code == "invalid_type"
    assert age_error.text == "Must be an integer type."
    assert age_error.position.line_no == 2

    email_error = error_messages[1]
    assert isinstance(email_error, ValidationError)

# Generated at 2022-06-14 14:57:03.990881
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    assert tokenize_yaml("42") == ScalarToken(42)
    assert tokenize_yaml("42\n") == ScalarToken(42)
    assert tokenize_yaml("42\n\n") == ScalarToken(42)
    assert tokenize_yaml("42\n43") == ScalarToken(42)
    assert tokenize_yaml("42\n---\n43") == ScalarToken(42)



# Generated at 2022-06-14 14:57:11.875288
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    yaml_input = """
- a: 1
- b: 2
"""
    token = tokenize_yaml(yaml_input)
    assert isinstance(token, ListToken)
    assert isinstance(token.value[0], DictToken)
    assert isinstance(token.value[1], DictToken)
    assert token.value[0].value == {"a": 1}
    assert token.value[1].value == {"b": 2}
    assert token.start == 0
    assert token.end == 24
    assert token.content == yaml_input


# Generated at 2022-06-14 14:57:16.471537
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "id: 123\n"
    validator = Schema([Field(name="id", type="integer")])
    value, errors = validate_yaml(content, validator)
    assert errors == []
    assert value == {"id": 123}

# Generated at 2022-06-14 14:57:27.530332
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, fields
    from typesystem import Array, Boolean, Map, Number, String
    from typesystem.fields import Field
    from typesystem.schemas import Schema
    import io

    class ExampleSchema(Schema):

        name = String(max_length=100)
        age = Number(minimum=0, exclusive_minimum=True)
        is_ok = Boolean()
        tags = Array(items=String(min_length=2))
        nested = Map(items=Map(properties={"name": String(max_length=1)}))


    schema = ExampleSchema()

# Generated at 2022-06-14 14:57:34.615621
# Unit test for function validate_yaml
def test_validate_yaml():
    # check whether it can pass the test of the test
    yaml_content = '{"animal":"cat"}'
    content = yaml_content.encode()
    value, error = validate_yaml(content, "abcd")
    assert value == {"animal":"cat"}
    assert len(error) == 1
    assert isinstance(error, list)
    assert isinstance(error[0], ParseError)
    # check whether it can pass the test of parse error
    yaml_content = '{"animal":"cat"}}'
    content = yaml_content.encode()
    value, error = validate_yaml(content, "abcd")
    assert value == None
    assert len(error) == 1
    assert isinstance(error, list)
    assert isinstance(error[0], ParseError)
    # check whether

# Generated at 2022-06-14 14:57:40.332305
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    content = "a: 1\nb:2"
    expected = DictToken([("a", ScalarToken(1, 0, 1, content)), ("b", ScalarToken(2, 3, 4, content))], 0, 4, content)
    assert tokenize_yaml(content) == expected

# Integration test for function validate_yaml

# Generated at 2022-06-14 14:57:45.543672
# Unit test for function validate_yaml
def test_validate_yaml():
    assert(validate_yaml("name: Ben", validator={"name": str()}) is not None)

# Generated at 2022-06-14 14:57:55.561927
# Unit test for function validate_yaml
def test_validate_yaml():
    '''
    Tests the validate_yaml function using a simple test case
    '''
    content = "name: Arya\nage: 13\n"
    result, errors = validate_yaml(content, {'name': str, 'age': int})
    assert result['name'] == 'Arya'
    assert result['age'] == 13
    assert len(errors) == 0
    content = "name: Arya\nage: thirteen\n"
    result, errors = validate_yaml(content, {'name': str, 'age': int})
    assert errors[0].code == 'invalid_type'
    assert errors[0].position.column_no == 5
    assert errors[0].position.line_no == 2
    assert errors[0].position.char_index == 23
    assert errors[0].text

# Generated at 2022-06-14 14:58:00.187570
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    a: 1
    b: 2
    """
    tokens = tokenize_yaml(content)
    assert tokens.keys() == ["a", "b"]
    assert tokens["a"] == 1
    assert tokens["b"] == 2



# Generated at 2022-06-14 14:58:10.591254
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml("", "str") == (None, [])
    assert validate_yaml("key: 1", "str")[1][0].text == "Invalid syntax"
    assert validate_yaml("key: 1", "int")[1][0].text == "Value is not a valid number"
    assert validate_yaml("key: 1", "number") == (1, [])
    assert validate_yaml("key: 1.1", "int")[1][0].text == "Value is not a valid number"
    assert validate_yaml("key: 1.1", "number") == (1.1, [])
    assert validate_yaml("key: true", "boolean") == (True, [])
    assert validate_yaml("1", "str")[1][0].text == "Invalid syntax"
   

# Generated at 2022-06-14 14:58:16.779934
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(
        tokenize_yaml(
            """
name: "Michelle"
location: San Francisco
age: 26
"""
        ),
        DictToken,
    )

    assert isinstance(
        tokenize_yaml(
            """
- name: "Michelle"
  location: San Francisco
- job: "Engineer"
"""
        ),
        ListToken,
    )



# Generated at 2022-06-14 14:58:26.529152
# Unit test for function validate_yaml
def test_validate_yaml():
    # Validate valid input
    content = u"""
    items:
      - name: my_app
        image: "my_app:latest"
        env:
          - name: MY_VAR
            value: my_val
    """
    errors = validate_yaml(content, DeploymentSchema)
    assert not errors

    # Validate invalid input
    content = u"""
    items:
      - name: my_app
        image: "my_app:latest"
        env:
          - name: MY_VAR
            value: my_val
    invalid_key: invalid value
    """
    errors = validate_yaml(content, DeploymentSchema)

# Generated at 2022-06-14 14:58:34.150742
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''
        a: 123
        b: [456, 789]
        c: fOo
    '''
    validator = Schema(
        {"a": int, "b": [int], "c": str}
    )
    value, error_messages = validate_yaml(content, validator)
    assert value == {"a": 123, "b": [456, 789], "c": "fOo"}
    assert error_messages == []


# Generated at 2022-06-14 14:58:39.403045
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml("1", int) == (1, None)
    assert validate_yaml("1", float) == (1.0, None)
    assert validate_yaml("true", bool) == (True, None)
    assert validate_yaml("1", "int") == (1, None)
    assert validate_yaml("1", "float") == (1.0, None)
    assert validate_yaml("true", "bool") == (True, None)
    errors = validate_yaml("1", "string")[1]
    assert len(errors) == 1
    assert errors[0].code == "type"
    assert str(errors[0].position) == "1:1"
    with pytest.raises(ParseError):
        validate_yaml("a : b", "string")

#

# Generated at 2022-06-14 14:58:49.924107
# Unit test for function validate_yaml
def test_validate_yaml():
    string = '''
    name: "John"
    age: 23
    married: true
    '''
    class Person(Schema):
        name = fields.String(required=True)
        age = fields.Integer(minimum=1, maximum=100, required=True)
        married = fields.Boolean()

    value, error_messages = validate_yaml(string, Person)

    assert value == {
        'name': 'John',
        'age': 23,
        'married': True
    }
    assert error_messages == []


# Generated at 2022-06-14 14:59:01.518316
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = field(str)

    content = """
name: John
"""

    value, errors = validate_yaml(content, PersonSchema())
    assert value == {"name": "John"}
    assert errors == []

    content = """
name: John
age: 32
"""

    value, errors = validate_yaml(content, PersonSchema())
    assert value is None
    assert len(errors) == 1
    assert errors[0].text == 'Additional properties are not allowed ("age" was unexpected).'
    assert errors[0].position == Position(line_no=2, column_no=0, char_index=13)

    content = """
name: John
age: 32
"""

    value, errors = validate_yaml(content, PersonSchema(strict=False))
   

# Generated at 2022-06-14 14:59:14.944824
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test basic validation
    content = """
    title: "Hello World"
    """
    value, messages = validate_yaml(content, {"title": str})
    assert value == {"title": "Hello World"}
    assert not messages
    # Test that values are coerced to their target type.
    content = """
    title: "1"
    """
    value, messages = validate_yaml(content, {"title": int})
    assert value == {"title": 1}
    assert not messages
    # Test that errors are returned if parsing fails
    content = "{"
    value, messages = validate_yaml(content, {"title": int})
    assert value is None
    assert len(messages) == 1
    assert messages[0].code == "parse_error"

# Generated at 2022-06-14 14:59:20.824605
# Unit test for function validate_yaml
def test_validate_yaml():
    with open(os.path.join(BASE_DIR, 'test_validate_yaml.yaml')) as f:
        content = f.read()
    # Test for happy path
    value, message_lst = validate_yaml(content=content, validator=validator)
    assert(not message_lst)
    assert(value.raw_data['version'] == '0.0.1')
    assert(value.namespace['id'] == '1')
    assert(value.namespace['labels']['key1'] == 'value1')
    assert(value.namespace['labels']['key2'] == 'value2')

    # Test for unhappy path
    # content = """
    #     version: '0.0.1'
    #     namespace:
    #         id: '1

# Generated at 2022-06-14 14:59:31.765504
# Unit test for function validate_yaml
def test_validate_yaml():

    class SimpleSchema(Schema):
        s = fields.String(required=True)

    # Test validating a string
    (value, error_messages) = validate_yaml("s: hello", SimpleSchema)

    assert value == {"s": "hello"}
    assert len(error_messages) == 0

    # Test validating a string with an error
    content = "text: hi"
    (value, error_messages) = validate_yaml(content, SimpleSchema)
    assert value == None
    assert len(error_messages) == 1
    assert error_messages[0].text == "Error validating 's'. This field is required."

    # Test validating a bytestring
    content_bytes = content.encode()

# Generated at 2022-06-14 14:59:44.345275
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
        id: 123
        name: 'test name'
        """.strip()
    class Person(Schema):
        id = typesystem.Integer(minimum=100, maximum=200)
        name = typesystem.String()
    value, error_messages = validate_yaml(content, Person)
    print(value)
    print(error_messages)
    assert value['id'] == 123
    assert value['name'] == 'test name'

    content = """
        id: 123
        name: 'test name'
        """.strip()
    class Person(Schema):
        id = typesystem.Integer(minimum=100, maximum=200)
        name = typesystem.String(max_length=5)
    value, error_messages = validate_yaml(content, Person)
    print(value)

# Generated at 2022-06-14 14:59:47.901515
# Unit test for function validate_yaml
def test_validate_yaml():
    # Init
    content = '{"name": "test.yaml"}'
    validator = Field()
    # Run
    result = validate_yaml(content, validator)
    # Assert
    assert result is not None

# Generated at 2022-06-14 14:59:58.289440
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(required=True, primitive_type=str)
    assert validate_yaml(b'', field) == (None, [Message.required()])
    assert validate_yaml('{"foo": "bar"}', field) == (
        None,
        [
            Message(
                text="{'foo': 'bar'} is not a 'string'.",
                code=ValidationError.INVALID,
                position=Position(line_no=1, column_no=2, char_index=1),
            )
        ],
    )
    assert validate_yaml('"Hello!"', field) == (
        "Hello!",
        [],
    )

# Generated at 2022-06-14 15:00:06.858330
# Unit test for function validate_yaml
def test_validate_yaml():
    from yaml import safe_load
    from typesystem import String, Integer

    d = safe_load("""
    name: John
    age: 42
    """)

    class Person(Schema):
        name = String()
        age = Integer()

    token = tokenize_yaml("""
    name: John
    age: 42
    """)

    value, errors = validate_yaml("""
    name: John
    age: 42
    """, Person)

    assert value == d
    assert errors == []

    assert value == token.value
    assert errors == token.validate(validator=Person).messages

# Generated at 2022-06-14 15:00:17.182088
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String

    field = String(format="uri")
    content = "https://www.example.org"
    result = validate_yaml(content, field)
    assert result == (content, None)

    field = String(format="uri")
    content = "http://127.0.0.1"
    result = validate_yaml(content, field) # noqa F841
    assert result == (content, None)

    field = String(format="uri")
    content = "htp://127.0.0.1"
    result = validate_yaml(content, field) # noqa F841
    assert result[0] is None
    assert result[1].code == "invalid_uri"

# Generated at 2022-06-14 15:00:26.775558
# Unit test for function validate_yaml
def test_validate_yaml():
    #define typesystem schema for validating
    class PetSchema(Schema):
        name = String(max_length=100)
        age = Integer(minimum=1)

    #check typesystem schema in operation
    content = """
    name: "test"
    age: 1
    """
    assert validate_yaml(content, PetSchema) == (
        {"name": "test", "age": 1},
        [],
    )
    assert validate_yaml(content, PetSchema) != None

    #check invalid input
    content = """
    name: 100
    age: 0
    """

# Generated at 2022-06-14 15:00:38.655614
# Unit test for function validate_yaml
def test_validate_yaml():
    class SimpleSchema(Schema):
        name = "string"
        description = "text"
        age = "integer"

    fields = {}
    fields['name'] = "Jane Doe"
    fields['description'] = "This is Jane Doe"
    fields['age'] = 12
    # Success test
    value, errors = validate_yaml(yaml.dump(fields), SimpleSchema)
    assert isinstance(errors, list)
    assert len(errors) == 0
    assert isinstance(value, dict)
    for k, v in fields.items():
        assert value[k] == v
    # Failure test
    fields['age'] = "12"
    value, errors = validate_yaml(yaml.dump(fields), SimpleSchema)
    assert isinstance(errors, list)
    assert len(errors) == 1

# Generated at 2022-06-14 15:00:51.127690
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(fields={
        "a": Field(required=True, type="string", max_length=3),
        "b": Field(type="integer"),
        "c": Field(type="float", min_value=0.0),
        "d": Field(type="array", items=Field(type="string", max_length=10)),
        "e": Field(type="object", properties={
            "f": Field(type="string", max_length=3)
        })
    })
    data = """
    a: abc
    b: 123
    c: 1e10
    d:
        - foo
        - bar
    e:
        f: xyz
    """
    value, errors = validate_yaml(data, schema)
    assert errors == []

# Generated at 2022-06-14 15:01:03.436935
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = StringField(required=True)
        address = StringField(required=True)
        age = IntegerField(required=True)
        color = StringField(required=False)
        shapes = StringField(required=False)
        email = StringField(required=False)
        phone = IntegerField(required=False)

    input_file = open("data.yaml")
    yaml_content = input_file.read()
    input_file.close()

    value, errors = validate_yaml(content=yaml_content, validator=TestSchema)
    print("Errors from validate_yaml:", errors)

    class TestSchema_2(Schema):
        name = StringField(required=True)
        address = StringField(required=True)
        age = Integer

# Generated at 2022-06-14 15:01:12.763867
# Unit test for function validate_yaml
def test_validate_yaml():
    # Configure the validator to use a custom `yaml.safe_load` function that
    # uses our Token classes.
    validator = Schema(
        {
            "foo": [
                {"bar": str},
                {"fizz": str},
                {"buzz": int},
            ],
        }
    )

    # Validate the data.
    value, _ = validate_yaml(
        b"""
        foo:
          - bar: hello
          - fizz: world
          - buzz: 42
        """,
        validator,
    )
    assert value == {
        "foo": [
            {"bar": "hello"},
            {"fizz": "world"},
            {"buzz": 42},
        ],
    }

    # Validate data with a validation error.
    _, messages = validate_y

# Generated at 2022-06-14 15:01:21.801820
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String
    from typesystem.schemas import Schema

    class UserSchema(Schema):
        name = String(required=True)
        age = Integer()

    data = """
    name: "Joe"
    age: 50
    """
    value, errors = validate_yaml(data, UserSchema)
    assert errors == []
    assert value == {"name": "Joe", "age": 50}

    data = """
    name: "Joe"
    foo: "bar"
    """
    value, errors = validate_yaml(data, UserSchema)
    assert errors[0].code == "unknown_field"
    assert errors[0].position.line_no == 3
    assert errors[0].position.column_no == 2
    assert errors[0].position.char_

# Generated at 2022-06-14 15:01:33.462286
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        int_field = Field(type_hint="integer", required=True)

    content1 = "int_field:\n  - \"42\""
    content2 = "int_field: 42"

    val, errors = validate_yaml(content1, MySchema)
    assert val == {"int_field": 42}
    assert not errors

    val, errors = validate_yaml(content2, MySchema)
    assert val == {"int_field": 42}
    assert not errors

    val, errors = validate_yaml(content1, Field(type_hint="integer"))
    assert val == 42
    assert not errors

    val, errors = validate_yaml(content2, Field(type_hint="integer"))
    assert val == 42
    assert not errors



# Generated at 2022-06-14 15:01:44.208633
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Schema
    from typesystem.yaml import validate_yaml

    class ContactSchema(Schema):
        name = String(max_length=60)
        location = String(max_length=60)

    content = """
    name: A.J.
    location: USA
    """
    good, errors = validate_yaml(content, ContactSchema())
    assert not errors
    assert good["name"] == "A.J."
    assert good["location"] == "USA"

    content = """
    name: A.J.
    location:
        city: USA
        state: CA
    """
    good, errors = validate_yaml(content, ContactSchema())
    assert not good
    assert isinstance(errors, list)
    assert len(errors) == 1
    error = errors

# Generated at 2022-06-14 15:01:49.593678
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test that valid yaml can be provided
    assert validate_yaml("bob: nikolov") == ({'bob': 'nikolov'}, None)
    # Test that bad yaml results in an error
    assert len(validate_yaml("a: b: c")[1]) == 1


# Generated at 2022-06-14 15:01:58.660592
# Unit test for function validate_yaml
def test_validate_yaml():
    data = "a: 1"

    schema = {
        "a": int
    }

    # Test valid
    _, errors = validate_yaml(data, schema)
    assert errors == []

    # Test invalid
    data = "a: b"
    _, errors = validate_yaml(data, schema)

    assert len(errors) == 1
    assert isinstance(errors[0], ValidationError)
    assert errors[0].path == ["a"]
    assert errors[0].position == Position(
        line_no=1, column_no=4, char_index=3
    )

    # Test invalid YAML
    data = "a: b"
    _, errors = validate_yaml("a: b", schema)
    assert len(errors) == 1

# Generated at 2022-06-14 15:02:09.743010
# Unit test for function validate_yaml

# Generated at 2022-06-14 15:02:21.017670
# Unit test for function validate_yaml
def test_validate_yaml():
    """ Test validate_yaml()"""
    import yaml
    from typesystem.base import Message, ParseError
    from typesystem.fields import (
        Array,
        Boolean,
        Choice,
        DateTime,
        Float,
        Integer,
        Object,
        String,
    )
    from typesystem import schemas

    yaml_1 = """---
note: This is a sample
parameters:
    string: abc
    number: 3.9
    boolean: true
    blank:
    null: null
    integer: 2
"""


# Generated at 2022-06-14 15:02:25.828643
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    name: Siva
    age: 12
    """
    class User(Schema):
        name = String()
        age = Integer()
    _, errors = validate_yaml(content, User)
    assert not errors, errors

# Generated at 2022-06-14 15:02:34.364729
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String
    from typesystem.schemas import Schema

    class Person(Schema):
        name = String(max_length=200)
        age = Integer(minimum=0, maximum=120)

    content = """
    name: Stephen
    age: 30
    """
    assert validate_yaml(content, Person) == ({'name': 'Stephen', 'age': 30}, [])

    content = """
    name: Stephen
    """
    error_messages = [
        {
            "code": "required",
            "field": "age",
            "text": "This field is required.",
            "position": {
                "line_no": 3,
                "column_no": 1,
                "char_index": 20,
            },
        }
    ]
    assert validate_

# Generated at 2022-06-14 15:02:45.146178
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestValidator(Schema):
        name = Field(str)
        age = Field(int, required=False)
        score = Field(float)

    content = """
    name: test
    age: 24
    """
    data, errors = validate_yaml(content, TestValidator)
    assert data == {"name": "test", "age": 24}
    assert len(errors) == 1
    error = errors[0]
    assert error.code == "required"
    assert error.text == "Missing field."
    assert error.position.column_no == 6
    assert error.position.line_no == 4
    assert error.position.char_index == 24

    content = """
    name: hello
    age: 24
    score: three
    """

# Generated at 2022-06-14 15:02:56.020383
# Unit test for function validate_yaml
def test_validate_yaml():
    message=validate_yaml(
        content='''
        name: John
        age: 27
        ''',
        validator=Schema(fields={"name": String(), "age": Integer()})
    )
    assert message.text == '27 is not a valid value for field "age".'
    assert message.position.line_no == 3
    assert message.position.column_no == 5

    message_list=validate_yaml(
        content='''
        - name: John
          age: 27
        - name: Jack
          age: '28'
        ''',
        validator=Schema(fields={'name': String(), 'age': Integer()})
    )
    assert message_list[0].text == '27 is not a valid value for field "age".'

# Generated at 2022-06-14 15:03:07.754301
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    int: 123
    float: 123.4
    string: foo
    list: [1, 2]
    dict: {a: 1, b: 2}
    null: ~
    """
    from pydantic import BaseModel
    from typesystem.fields import Field

    class ValidateYamlSchema(BaseModel):
        int = Field(typ=int)
        float = Field(typ=float)
        string = Field(typ=str)
        list = Field(typ=list)
        dict = Field(typ=dict)
        null = Field(typ=type(None))

    value, error_messages = validate_yaml(content=content, validator=ValidateYamlSchema)

# Generated at 2022-06-14 15:03:20.041862
# Unit test for function validate_yaml
def test_validate_yaml():
    class User(Schema):
        name = String(max_length=50)

    data = """
    name: 'Joe'
    """
    value, errors = validate_yaml(data, User)
    assert value["name"] == "Joe"
    assert errors == []

    data = """
    name: 'John'
    """
    value, errors = validate_yaml(data, User)
    assert value["name"] == "John"
    assert errors == []

    data = """
    name: 'Mike'
    """
    value, errors = validate_yaml(data, User)
    assert value["name"] == "Mike"
    assert errors == []

    data = """
    name: 'Lela'
    """
    value, errors = validate_yaml(data, User)

# Generated at 2022-06-14 15:03:26.890748
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b"\n\"This is just a string\"\n"
    value, errors = validate_yaml(
        content, validator = Field(type = str)
    )
    assert value == "This is just a string"
    assert not errors

    content = b"\n\"This is just a string\"\n"
    value, errors = validate_yaml(
        content, validator = Field(type = int)
    )
    assert value is None
    assert len(errors) == 1
    assert not errors[0].position



# Generated at 2022-06-14 15:03:36.237200
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    test_content = """
    foo: "bar"
    baz: quux
    """
    token = tokenize_yaml(test_content)
    # Makes sure the token is a DictToken
    assert type(token) == DictToken
    #Makes sure there are two children
    assert len(token.value) == 2
    # Makes sure the children are both ScalarTokens
    assert type(token.value[0]) == ScalarToken
    assert type(token.value[1]) == ScalarToken
    # Makes sure the children have the right value
    assert token.value[0].value == "bar"
    assert token.value[1].value == "quux"


# Generated at 2022-06-14 15:03:39.341107
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    - Python
    - is
    - cool
    """
    validator = Field()
    assert validate_yaml(content, validator) == (
        ["Python", "is", "cool"],
        None,
    )

# Generated at 2022-06-14 15:03:50.050095
# Unit test for function validate_yaml
def test_validate_yaml():
    import json
    from typesystem.fields import String

    content = """
name: john smith
age: 21
height: 6'2"
is_student: true
"""

    class NotRequiredString(String):
        def is_required(self, value: typing.Any) -> bool:
            return False

    class Person(Schema):
        name = NotRequiredString()
        age = NotRequiredString()
        height = NotRequiredString()
        is_student = NotRequiredString()

    value, error_messages = validate_yaml(content, validator=Person)

    try:
        assert len(error_messages) == 0
    except AssertionError as e:
        print(json.dumps(error_messages, indent=2))
        raise e


# Generated at 2022-06-14 15:03:58.005006
# Unit test for function validate_yaml
def test_validate_yaml():
    class SimpleSchema(Schema):
        age = Field(type="integer")
        
    content = "age: 32"
    value, error_messages = validate_yaml(content, SimpleSchema)
    assert error_messages == ""
    assert value['age'] == 32
    
# Test for function validate_yaml with invalid data

# Generated at 2022-06-14 15:04:05.344143
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml(content={"a": 1}) == DictToken({"a": 1}, 0, 6)
    assert tokenize_yaml(content=["a", 1]) == ListToken(["a", 1], 0, 5)
    assert tokenize_yaml(content="a") == ScalarToken("a", 0, 0)
    assert tokenize_yaml(content=1) == ScalarToken(1, 0, 0)
    assert tokenize_yaml(content=None) == ScalarToken(None, 0, 0)
    assert tokenize_yaml(content=True) == ScalarToken(True, 0, 0)
    assert tokenize_yaml(content=False) == ScalarToken(False, 0, 0)

# Generated at 2022-06-14 15:04:13.651718
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    # Test schema without errors
    schema = String(min_length=1, max_length=2)
    content = "apple"
    error_messages = validate_yaml(content, schema)[1]
    assert len(error_messages) == 0

    # Test schema with errors
    schema = String(min_length=5, max_length=5)
    content = "apple"
    error_messages = validate_yaml(content, schema)[1]
    assert isinstance(error_messages[0], Message)
    assert isinstance(error_messages[0].position, Position)
    assert error_messages[0].code == "too_short"
    assert error_messages[0].text == "Value is too short."

# Generated at 2022-06-14 15:04:19.799679
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "abc"
    validator = Field
    assert validate_yaml(content, validator) == ("abc", [])

    content = "123"
    validator = int
    assert validate_yaml(content, validator) == (123, [])

    content = "1.23"
    validator = float
    assert validate_yaml(content, validator) == (1.23, [])



# Generated at 2022-06-14 15:04:24.310295
# Unit test for function validate_yaml
def test_validate_yaml():

    class TestSchema(Schema):
        field = Field(type_=str)
        
    yaml_data = """
    field: test
    """
    value, error_messages = validate_yaml(content=yaml_data, validator=TestSchema)
    assert value == {'field': 'test'}
    assert error_messages == []

# Generated at 2022-06-14 15:04:31.922589
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    class CustomSafeLoader(SafeLoader):
        pass

    def construct_mapping(loader, node):
        start = node.start_mark.index
        end = node.end_mark.index
        mapping = loader.construct_mapping(node)
        return DictToken(mapping, start, end - 1, "test_content")

    def construct_sequence(loader, node):
        start = node.start_mark.index
        end = node.end_mark.index
        value = loader.construct_sequence(node)
        return ListToken(value, start, end - 1, "test_content")

    def construct_scalar(loader, node):
        start = node.start_mark.index
        end = node.end_mark.index
        value = loader.construct_scalar(node)
        return ScalarToken

# Generated at 2022-06-14 15:04:42.562756
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer, Boolean, Number
    from typesystem import Array, Dict

    assert validate_yaml(b"", String) == ("", [])
    assert validate_yaml(b"", Integer) == (0, [])
    assert validate_yaml(b"", Boolean) == (False, [])
    assert validate_yaml(b"", Number) == (0.0, [])
    assert validate_yaml(b"", Array(Integer)) == ([], [])
    assert validate_yaml(b"", Dict()) == ({}, [])

    assert validate_yaml(b"foo", String) == ("foo", [])
    assert validate_yaml(b"42", Integer) == (42, [])
    assert validate_yaml(b"true", Boolean) == (True, [])


# Generated at 2022-06-14 15:04:47.947077
# Unit test for function validate_yaml
def test_validate_yaml():
    value, error_messages = validate_yaml(
        "# Here's an example\n"
        "key: value\n"
        "key2: 2",
        Field(type="string"),
    )
    assert value == "# Here's an example\nkey: value\nkey2: 2"
    assert len(error_messages) == 1
    assert error_messages[0].position.line_no == 1
    assert error_messages[0].position.column_no == 9

# Generated at 2022-06-14 15:04:55.252978
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer

    class Person(Schema):
        name = String()
        age = Integer(minimum=0, maximum=150)


    value, errors = validate_yaml(b"name: Bob", Person)
    assert errors[0].text == "Missing required field 'age'"

    value, errors = validate_yaml(b"age: 10", Person)
    assert errors[0].text == "Missing required field 'name'"



# Generated at 2022-06-14 15:05:06.133803
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(type_name="string")
    assert validate_yaml(content=b"foo: bar", validator=validator)[0] == "foo: bar"

    validator = Field(type_name="string")
    assert validate_yaml(content=b"foo: 123", validator=validator) == ("", [])

    validator = Field(type_name="string")
    assert validate_yaml(content=b"foo: 123", validator=validator)[1][0] == Message(
        code="invalid_type",
        text="Expected a string.",
        path=["foo"],
        position=Position(column_no=1, line_no=1),
    )

    class SimpleSchema(Schema):
        foo = Field(type_name="string")

    validator = SimpleSche

# Generated at 2022-06-14 15:05:22.457501
# Unit test for function validate_yaml
def test_validate_yaml():
    # Validator is a Field
    field = Field(name="a", required=True)
    assert validate_yaml('---\na: 1', field) == ({'a': 1}, [])

    # Validator is a Schema
    class SimpleSchema(Schema):
        b = Field(name='b', required=True)
    assert validate_yaml('---\nb: 2', SimpleSchema) == ({'b': 2}, [])

    # Validation error
    field = Field(
        name="c",
        required=True,
        validators=[lambda x: x == 3]
    )
    messages = validate_yaml('---\nc: 2', field)[1]
    assert len(messages) == 1
    assert isinstance(messages[0], ValidationError)

    # Parse error

# Generated at 2022-06-14 15:05:29.532293
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem import error_messages

    class PersonSchema(Schema):
        name = String()
        age = String()

    content = "# This is a comment\nname: Alice\nage: 15"
    expected_msgs = [
        Message(
            text=error_messages.EXPECTED_INTEGER.format(field_name="age"),
            code="expected_integer",
            position=Position(line_no=3, column_no=5, char_index=14),
        ),
    ]
    assert validate_yaml(content, PersonSchema) == ({"name": "Alice", "age": "15"}, expected_msgs)


# Generated at 2022-06-14 15:05:33.858059
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = Field(type="string")
    
    # validates_data('validate_yaml') to be a unit test for the function

    if __name__ == '__main__':
        unittest.main()

# Generated at 2022-06-14 15:05:43.091037
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Array
    from typesystem.types import Text
    from typesystem.exceptions import ValidationError
    schema = Array(items=Text(), min_items=2)
    value, errors = validate_yaml('- foo\n- bar\n- baz', validator=schema)
    assert value == ['foo', 'bar', 'baz']
    assert errors == []
    value, errors = validate_yaml('- foo\n- bar', validator=schema)
    assert value == ['foo', 'bar']
    assert errors == []
    value, errors = validate_yaml('- foo', validator=schema)
    assert value == ['foo']
    assert errors == [ValidationError(code='min_items', text='Expected at least 2 items.')]


# Generated at 2022-06-14 15:05:51.097245
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(tokenize_yaml("{}"), DictToken)
    assert isinstance(tokenize_yaml("[]"), ListToken)
    assert isinstance(tokenize_yaml("test"), ScalarToken)
    assert isinstance(tokenize_yaml("- test"), ListToken)
    assert isinstance(tokenize_yaml("- test - test"), ListToken)
    assert isinstance(tokenize_yaml("{a: test}"), DictToken)
    assert isinstance(tokenize_yaml("{a: test, b: test}"), DictToken)
    assert isinstance(tokenize_yaml("{a: test} - test"), ListToken)
    assert isinstance(tokenize_yaml("{a: test} - {}"), ListToken)

# Generated at 2022-06-14 15:06:03.076669
# Unit test for function validate_yaml
def test_validate_yaml():

    class FieldSchema(Schema):
        field = Field(type="string")

    schema = FieldSchema()

    assert validate_yaml('field: foo', schema)[0] == {"field": "foo"}
    error = validate_yaml('field: 42', schema)[1][0]
    assert error.text == "Must be a string."
    assert error.position.line_no == 1
    assert error.position.column_no == 8
    assert error.position.char_index == 7
    assert error.code == "invalid_type"
    error = validate_yaml('{"field": 42}', schema)[1][0]
    assert error.text == "Must be a string."
    assert error.position.line_no == 1
    assert error.position.column_no == 9
    assert error.position.char_index

# Generated at 2022-06-14 15:06:09.741222
# Unit test for function validate_yaml
def test_validate_yaml():
    """Unit test for function validate_yaml"""
    import typesystem

    class TestSchema(typesystem.Schema):
        name = typesystem.String()

    content = """
    name:
    """

    value, errors = validate_yaml(content, validator=TestSchema)
    assert not value
    assert len(errors) == 1
    assert isinstance(errors[0], Message)
    assert errors[0].code == "required"
    assert errors[0].position.char_index == 6



# Generated at 2022-06-14 15:06:20.202413
# Unit test for function validate_yaml
def test_validate_yaml():  # pragma: no cover
    from typesystem.schemas import Schema

    class SimpleSchema(Schema):
        name = fields.String(max_length=64)
        age = fields.Integer(min_value=1)

    value, errors = validate_yaml(
        content="""name: Jane Doe
age: 26""",
        validator=SimpleSchema(),
    )

    assert value == {"name": "Jane Doe", "age": 26}
    assert not errors

    value, errors = validate_yaml(
        content="""name: Jane Doe
age: 0""",
        validator=SimpleSchema(),
    )

    assert value is None
    assert [e.text for e in errors] == ["must be greater than or equal to 1."]
