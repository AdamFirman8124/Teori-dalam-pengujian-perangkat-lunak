

# Generated at 2022-06-14 14:56:31.540171
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Check that an empty string raises a parse error
    empty_content = ""
    with pytest.raises(ParseError) as e:
        tokenize_yaml(empty_content)
    assert e.value.code == 'no_content'

    # Check that an empty dictionary raises no error, and returns a dict
    dict_content = "{}"
    assert isinstance(tokenize_yaml(dict_content), DictToken)

    # Check that an empty list raises no error, and returns a list
    list_content = "[]"
    assert isinstance(tokenize_yaml(list_content), ListToken)

    # Check that invalid yaml raises a parse error
    invalid_content = "{ }"
    with pytest.raises(ParseError) as e:
        tokenize_yaml(invalid_content)
   

# Generated at 2022-06-14 14:56:38.878299
# Unit test for function validate_yaml
def test_validate_yaml():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    content = """
    key:
      key: value
    """
    class YAMLSchema(Schema):
        class Meta:
            content_type = "application/x-yaml"
        key = fields.String()
    schema = YAMLSchema()

    value, errors = validate_yaml(content, schema)

if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 14:56:41.491049
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml('{"key": "value"}')
    assert 'value' == token['key']



# Generated at 2022-06-14 14:56:49.855932
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema, fields
    from typesystem.testing import TestCase

    class MySchema(Schema):
        name = fields.String()
        count = fields.Integer()

    data = """name: John
    count: 123
    """

    value, error_messages = validate_yaml(data, validator=MySchema)
    expected_value = {"name": "John", "count": 123}
    expected_error_messages = []
    TestCase().assertEqual(expected_value, value)
    TestCase().assertEqual(expected_error_messages, error_messages)

# Generated at 2022-06-14 14:57:00.859359
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("test") == "test"
    assert tokenize_yaml("123") == 123
    assert tokenize_yaml("3.14") == 3.14
    assert tokenize_yaml("true") is True
    assert tokenize_yaml("false") is False
    assert tokenize_yaml("null") is None
    assert tokenize_yaml("[1, 2, 3]") == [1, 2, 3]
    assert tokenize_yaml("{a: b}") == {"a": "b"}
    assert tokenize_yaml("{a: [b, c]}") == {"a": ["b", "c"]}

    # Test the position information that is attached to the tokens.
    parsed_value = tokenize_yaml("[1, 2, 3]")

    assert parsed_value

# Generated at 2022-06-14 14:57:05.030339
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('["a","b"]') == [ScalarToken('a',2,3,""),ScalarToken('b',6,7,"")]
    assert tokenize_yaml('["a", 12]') == [ScalarToken('a',2,3,""),ScalarToken('12',6,8,"")]


# Generated at 2022-06-14 14:57:10.634176
# Unit test for function validate_yaml
def test_validate_yaml():
    class YamlSchema(Schema):
        a = Field(type="integer")
        b = Field(type="integer")
        c = Field(type="integer", required=True)
        d = Field(type="integer")
    try:
        assert validate_yaml(b"", YamlSchema) != None
    except Exception as e:
        assert "No content" in e

# Generated at 2022-06-14 14:57:21.854801
# Unit test for function validate_yaml
def test_validate_yaml():
    data = '''
    - 1
    - 2
    '''
    val, errors = validate_yaml(data, Field(type="integer"))
    assert val == [1, 2]
    assert errors == []

    data = '''
    - 1
    - 2
    - "3"
    '''
    val, errors = validate_yaml(data, Field(type="integer"))
    assert val == [1, 2, 3]
    assert errors == []

    data = '''
    - 1
    - 2
    - "3"
    - 4
    - 5
    '''
    val, errors = validate_yaml(data, Field(type="integer", max_length=5))
    assert val == [1, 2, 3, 4, 5]
    assert errors == []


# Generated at 2022-06-14 14:57:28.303696
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # tokenize_yaml and validate_yaml are both used later in the file. The
    # unit tests for them are placed here for convenience and to avoid
    # code duplication.
    from typesystem.fields import Integer

    # Valid yaml.
    token = tokenize_yaml("123")
    assert isinstance(token, ScalarToken)
    assert token.value == 123

    token = tokenize_yaml("key: value")
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}

    token = tokenize_yaml("- value")
    assert isinstance(token, ListToken)
    assert token.value == ["value"]

    value, error_messages = validate_yaml("123", Integer())
    assert value == 123
    assert len(error_messages) == 0

# Generated at 2022-06-14 14:57:34.106405
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    foo: bar
    example: 123
    """
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    dict_repr = "<DictToken {'foo': <ScalarToken 'bar'>, 'example': <ScalarToken 123>}>"
    assert repr(token) == dict_repr



# Generated at 2022-06-14 14:57:44.361005
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem.schemas import Schema
    from typesystem.types import String
    class Person(Schema):
        name = String()
        age = Integer()

    person_yaml = '''
    name: Bob
    age: 42'''
    value, errors = validate_yaml(person_yaml, validator=Person)
    # assert errors is None
    # assert value == {"name": "Bob", "age": 42}
    print(value)
    print(errors)

# Generated at 2022-06-14 14:57:46.264227
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(validator = '{"name": "test"}', content = 'test')

# Generated at 2022-06-14 14:57:52.715208
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '[{"foo": "hello", "bar": "world"}, {"foo": "sup", "bar": "yo"}]'
    validator = Schema(foo=str, bar=str)
    
    result = validate_yaml(content, validator)
    errors = result[1]
    assert errors.is_valid == True
    assert result[0] == [{"foo": "hello", "bar": "world"}, {"foo": "sup", "bar": "yo"}]

# Generated at 2022-06-14 14:57:56.190094
# Unit test for function validate_yaml
def test_validate_yaml():
  schema = Schema({'age': int})
  data = validate_yaml(
    """
    age: "age"
    """,
    schema
  )
  assert data[1][0].message == "Must be an integer"

# Generated at 2022-06-14 14:58:07.913544
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class Person(Schema):
        name = String()
        age = String()

    content = """name: John
age: 42"""

    value, msg = validate_yaml(content, Person)
    assert value == {"name": "John", "age": "42"}
    assert msg == []

    content = """age: 42
name: John"""

    value, msg = validate_yaml(content, Person)
    assert value == {"name": "John", "age": "42"}
    assert msg == []

    content = """name: John"""

    value, msg = validate_yaml(content, Person)
    assert value == {"name": "John"}
    assert msg[0].messages == ["This field is required."]

# Generated at 2022-06-14 14:58:18.589887
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        username = fields.String()
        password = fields.String()

    # Should be successful
    value = {"username": "fred", "password": "secret"}
    result = validate_yaml(yaml.dump(value), UserSchema)
    assert isinstance(result, tuple)
    assert result[0]["username"] == "fred"
    assert result[0]["password"] == "secret"
    assert isinstance(result[1], list)
    assert len(result[1]) == 0

    # Should have parse error: 'username' is required
    value = {"password": "secret"}
    result = validate_yaml(yaml.dump(value), UserSchema)
    assert isinstance(result, tuple)
    assert result[0] == {}

# Generated at 2022-06-14 14:58:22.578580
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import validation

    class Foo(Schema):
        x = validation.String()
    foo_schema = Foo()
    assert validate_yaml("{x: x}", foo_schema) == ({'x': 'x'}, [])


# Generated at 2022-06-14 14:58:28.081511
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    foo: bar
    baz: boo
    """
    schema = Schema.from_dict({"foo": str, "baz": str})
    value, errors = validate_yaml(content, schema)
    assert value == {"foo": "bar", "baz": "boo"}
    assert not errors

# Generated at 2022-06-14 14:58:39.965910
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_schema = """\
    type: object
    properties:
      name:
        type: string
      age:
        type: number
    """
    content = """\
    name: Bob
    age: 32
    """
    value, errors = validate_yaml(content, yaml_schema)
    assert value == {u"name": u"Bob", u"age": 32}
    assert errors == []
    content = """\
    name: Bob
    age: thirty two
    """
    value, errors = validate_yaml(content, yaml_schema)
    assert value == {u"name": u"Bob"}

# Generated at 2022-06-14 14:58:52.433288
# Unit test for function validate_yaml
def test_validate_yaml():
    from typing import List
    from typesystem.schemas import Schema
    from typesystem.fields import Integer, String, Float, Boolean, Object

    class User(Schema):
        name = String(required=True)
        age = Integer()
        numbers = List[Integer]()
        float = Float()
        bool = Boolean()


    assert validate_yaml("name: rob", User) == ({'name': 'rob'}, [])
    assert validate_yaml(b'name: rob\nage: 10\nnumbers: [1, 2, 3]\nfloat: 1.2\nbool: True', User) == ({'name': 'rob', 'age': 10, 'numbers': [1, 2, 3], 'float': 1.2, 'bool': True}, [])

# Generated at 2022-06-14 14:59:07.679953
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    - name: Darren
      age: 38
      sport: golf
    - name: Rachel
      age: 36
      sport: badminton
    """
    field_schema = {
        'type': 'object',
        'properties': {
            'name': {'type': 'string'},
            'age': {'type': 'integer'},
            'sport': {'type': 'string', 'enum': ['golf', 'badminton']},
        }
    }
    validator = Field(**field_schema)
    value, errors = validate_yaml(content, validator)
    assert len(errors) == 0

# Generated at 2022-06-14 14:59:14.868192
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = fields.String(max_length=10)
        age = fields.Integer()

    content = b"{name: 'matt', age: 100}"
    value, errors = validate_yaml(content, Person)
    assert value == {"name": "matt", "age": 100}
    assert errors == []

    content = "!Person {name: 'matt', age: 100}"
    value, errors = validate_yaml(content, Person)
    assert value == {"name": "matt", "age": 100}
    assert errors == []

# Generated at 2022-06-14 14:59:20.105387
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = "string"

    # Parse and validate a YAML string
    value, errors = validate_yaml(b"name: 12", validator=TestSchema)

    assert len(errors) == 1

    # Parse and validate a text string
    value, errors = validate_yaml("name: 12", validator=TestSchema)

    assert len(errors) == 1

# Generated at 2022-06-14 14:59:31.637589
# Unit test for function validate_yaml
def test_validate_yaml():

    class SimpleSchema(Schema):
        first_name = Field(required=True)
        last_name = Field(required=True)

    content = "first_name: Akshay\nlast_name: Narayan"
    parsed_data, error_messages = validate_yaml(content, SimpleSchema)
    print("type(parsed_data)", type(parsed_data))
    print("parsed_data", parsed_data)
    print("parsed_data['last_name']", parsed_data["last_name"])
    # print("type(error_messages)", type(error_messages))
    print("error_messages", error_messages)
    assert error_messages == []

# Generated at 2022-06-14 14:59:41.792704
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = "string(min_length=3)"
        age = "integer(minimum=18)"
        location = "dict(name=string, country=string)"

    output = validate_yaml(
        b"age: 16\nname: Jon\nlocation:\n  name: Jon\n  country: Nowhere", Person
    )
    assert output == [
        Message(
            text="Must be greater than or equal to 18.",
            code="minimum",
            position=Position(column_no=5, line_no=2, char_index=11),
            error_type=ValidationError,
        )
    ]

# Generated at 2022-06-14 14:59:44.850786
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(b'{"foo": "bar"}',
                         Schema({'foo': fields.Text()})) == ({"foo": "bar"}, [])

# Generated at 2022-06-14 14:59:49.169906
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.strings import String

    assert validate_yaml(b"", String()) == (None, [])
    assert validate_yaml(b"foo", String()) == ("foo", [])
    assert validate_yaml(b"foo\n", String()) == (None, [Message(code="invalid")])



# Generated at 2022-06-14 15:00:00.680465
# Unit test for function validate_yaml
def test_validate_yaml():
    fail_indentation = "a:\n b:"
    fail_indentation_msg = validate_yaml(fail_indentation, "string")
    assert isinstance(fail_indentation_msg, tuple)
    assert isinstance(fail_indentation_msg[0], ParseError)
    assert fail_indentation_msg[0].position.line_no == 2
    assert fail_indentation_msg[0].position.column_no == 1

    fail_horizontal_tabs = "a:|\nb:"
    fail_horizontal_tabs_msg = validate_yaml(fail_horizontal_tabs, "string")
    assert isinstance(fail_horizontal_tabs_msg, tuple)
    assert isinstance(fail_horizontal_tabs_msg[0], ParseError)


# Generated at 2022-06-14 15:00:12.633025
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest
    from typesystem import String, Integer

    class Author(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0)

    class Book(Schema):
        title = String()
        authors = Author.as_list()

    content = """
        {
            "title": "Fundamentals of Astrodynamics",
            "authors": [
                {"name": "Vance", "age": 50},
                {"name": "Vance", "age": 51}
            ]
        }
    """

    (value, messages) = validate_yaml(content, Book)

# Generated at 2022-06-14 15:00:20.826806
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert(tokenize_yaml("") == None)
    assert(tokenize_yaml("foo")["value"] == "foo")
    assert(tokenize_yaml("foo")["value"] == "foo")
    assert(tokenize_yaml("0")["value"] == 0)
    assert(tokenize_yaml("0.")["value"] == 0.0)
    assert(tokenize_yaml("0e0")["value"] == 0.0)
    assert(tokenize_yaml("True")["value"] == True)
    assert(tokenize_yaml("False")["value"] == False)
    assert(tokenize_yaml("null")["value"] == None)
    assert(tokenize_yaml("[0, 1, 2]")[1]["value"] == 0)

# Generated at 2022-06-14 15:00:30.469981
# Unit test for function validate_yaml
def test_validate_yaml():
    class JSONSchema(Schema):
        schema = {
            "type": "object",
            "properties": {
                "foo": {"type": "string"},
                "bar": {"type": "integer"},
            },
            "required": ["foo"],
        }

    value, error_messages = validate_yaml(
        """
    foo:
    bar: 42
    """,
        JSONSchema,
    )

    assert value == {"foo": "", "bar": 42}
    assert len(error_messages) == 2
    assert error_messages[0].code == "required"
    assert error_messages[0].position == Position(line_no=2, column_no=5, char_index=8)
    assert error_messages[1].code == "required"
    assert error_messages

# Generated at 2022-06-14 15:00:35.886767
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.types import StringType
    field = String(min_length=10)
    value, errors = validate_yaml('test', field)
    assert isinstance(errors, list)
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no == 1

# Generated at 2022-06-14 15:00:47.177773
# Unit test for function validate_yaml
def test_validate_yaml():
    raw_yaml = """
        hello: world
        foo:
        - bar: baz
        - foobar: baz
    """.strip()
    from typesystem.fields import String
    from typesystem.schemas import Schema
    import yaml

    class MySchema(Schema):
        hello = String()
        foo = String()

    parsed = yaml.load(raw_yaml, Loader=yaml.SafeLoader)
    value, errors = validate_yaml(raw_yaml, MySchema)
    assert value == parsed
    assert isinstance(errors, list)
    assert len(errors) == 1
    error = errors[0]
    assert error.code == "type"
    assert error.text == "Value must be of type 'String' (type: 'list')."

# Generated at 2022-06-14 15:00:55.365774
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = fields.String()
        age = fields.Integer()
        is_active = fields.Boolean()

    yaml_data = 'name: Jonathan\nage: 27\nis_active: true\n'

    value, error_messages = validate_yaml(yaml_data, PersonSchema)
    assert value['name'] == 'Jonathan'
    assert value['age'] == 27
    assert value['is_active'] is True
    assert error_messages == []



# Generated at 2022-06-14 15:01:07.276429
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.tests.yaml import PetSchema

    content = """
    id: 3
    name: Freya
    age: 0.3
    is_sick: false
    email:
      - a@example.com
      - b@example.com
    """
    value, errors = validate_yaml(content, PetSchema)
    assert errors == []
    assert isinstance(value, dict)
    assert value["id"] == 3
    assert value["name"] == "Freya"
    assert value["age"] == 0.3
    assert value["is_sick"] is False
    assert value["email"] == ["a@example.com", "b@example.com"]



# Generated at 2022-06-14 15:01:15.435260
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(properties={
        "foo": Field(type="string"),
        "bar": Field(type="integer"),
        "baz": Field(type="boolean"),
    })

    content = "foo: good\nbar: 42\nbaz: true\n"
    value, errors = validate_yaml(content, schema)
    assert not errors

    content = "foo: good\nbar: 42\nbaz: not-a-bool\n"
    value, errors = validate_yaml(content, schema)
    assert isinstance(errors[0], ValidationError)
    position = Position(
        line_no=3, column_no=6, char_index=26,
    )
    assert errors[0].position == position

# Generated at 2022-06-14 15:01:19.373464
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = {
        "type" : "string",
        "format": "email"
    }
    content = "test@test.com"

    value, messages = validate_yaml(content, schema)
    assert value == "test@test.com"
    assert messages == []
    


# Generated at 2022-06-14 15:01:31.239125
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    from pprint import pprint
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer, Float
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken
    from typesystem.tokenize.yaml import tokenize_yaml
    from typesystem.tokenize.tokens import tokenize as _tokenize
    from typesystem.tokenize.positional_validation import validate_with_positions
    from typesystem.fields import Field
    schema = Schema([Integer, String])  
    # pprint(_tokenize(schema))
    # pprint(_tokenize({'a': [1,2,3], 'b': 'c'}))
    pprint(tokenize_yaml('a: [1,2,3]\nb: c'))


# Generated at 2022-06-14 15:01:37.806360
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    test function validate_yaml
    """
    input_str = "data:\n  name: John\n"
    schema = Schema({"data": {"name": str}})

    value, errors = validate_yaml(input_str, schema)
    assert value == {"data": {"name": "John"}}
    assert not errors



# Generated at 2022-06-14 15:01:46.511425
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, fields, validate_yaml

    class MySchema(Schema):
        name = fields.String(max_length=10)

    assert validate_yaml(
        content="""
        name: foo
        """,
        validator=MySchema,
    ) == ({'name': 'foo'}, [])

# Generated at 2022-06-14 15:01:56.591494
# Unit test for function validate_yaml
def test_validate_yaml():
    # pylint: disable=no-member
    field = typesystem.String(max_length=1)
    content = b"""
    A : 1
    """
    value, errors = validate_yaml(content, field)
    assert value is content
    assert len(errors) == 1
    assert isinstance(errors[0], ParseError)
    assert errors[0].text == "Unable to scan the next token."
    assert errors[0].code == "parse_error"
    assert errors[0].position == Position(column_no=2, line_no=1, char_index=1)



# Generated at 2022-06-14 15:02:08.114824
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml

    # yaml.safe_load(source)
    MAPPING = """
        # Example
        name:
            # Details
            family: Smith   # Very common
            given: Alice    # One of the siblings
    """
    # print(yaml.safe_load(MAPPING))
    # {'name': {'family': 'Smith', 'given': 'Alice'}}

    SEQUENCE = """
        - Mark McGwire
        - Sammy Sosa
        - Ken Griffey
    """
    # print(yaml.safe_load(SEQUENCE))
    # ['Mark McGwire', 'Sammy Sosa', 'Ken Griffey']

    try:
        print(yaml.safe_load("{'json': 'like'}"))
    except yaml.YAMLError as exc:
        print

# Generated at 2022-06-14 15:02:12.385615
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = StringType()
        age = IntegerType()

    content = """
name: John
age: 30
"""
    value, messages = validate_yaml(content, Person)
    assert value == {"name": "John", "age": 30}
    assert messages == []



# Generated at 2022-06-14 15:02:18.493505
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem import types
    from typesystem.fields import String, Dict, List, Integer

    schema = Dict(fields={
        "name": String(),
        "roles": List(items=String()),
        "age": Integer()
    })
    data = yaml.safe_load('''
    name: John Doe
    age: 23
    ''')
    value, messages = validate_yaml(yaml.safe_dump(data), schema)
    assert value['name'] == 'John Doe'
    assert value['age'] == 23
    assert messages[0].message == 'Missing key "roles".'
    data = yaml.safe_load('''
    name: John Doe
    roles:
      - user
      - admin
    age: 23
    ''')
    value

# Generated at 2022-06-14 15:02:30.648162
# Unit test for function validate_yaml
def test_validate_yaml():

    content = """
    ---
    foo:
        - 123
        - bar
        - abc: 123
    bar:
        - 123
        - "123"
        - abc: 123
    """

    validator = Schema(
        {
            "foo": [
                [int],
                [str],
                {"abc": int},
            ],
            "bar": [
                [int],
                [str],
                {"abc": int},
            ],
        },
        allow_unknown=False,
    )

    value, errors = validate_yaml(content, validator)

    # value is the python data structure

# Generated at 2022-06-14 15:02:42.808054
# Unit test for function validate_yaml
def test_validate_yaml():
    from textwrap import dedent
    from typesystem.schemas import Schema

    class UserSchema(Schema):
        username = String(required=True)

    # Success
    assert validate_yaml(dedent("""\
        username: jane
    """), UserSchema)[0] == {"username": "jane"}

    # ValidationError
    assert validate_yaml(dedent("""\
        username:
    """), UserSchema)[1] == [
        ValidationError(text='Missing required value.', code='required', position=Position(line_no=2, column_no=8, char_index=11))
    ]

    # ParseError

# Generated at 2022-06-14 15:02:54.073931
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = Scalar()
        age = Number()
        bio = Scalar()
        is_author = Boolean()

    class Post(Schema):
        title = Scalar()
        body = Scalar()
        author = Object(Person)
        tags = List(Scalar())


# Generated at 2022-06-14 15:03:05.365297
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, String, Array, Object

    class Pet(Object):
        name = String()
        age = Integer()

    class Person(Object):
        name = String()
        pets = Array(items=Pet)

    # todo, remove this config
    # todo, add a validator for boolean type
    data = '''
    name: "Denny"
    pets:
      - name: "Molly"
        age: 9
      - name: "Milo"
        age: 2
      - name: "Oscar"
        age: 3
      - name: "Elmo"
        age: 1
    '''

    value, errs = validate_yaml(data, Person)
    assert not errs

# Generated at 2022-06-14 15:03:07.551622
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = Field(str)

    result = validate_yaml("name: Foo", Person)
    assert result == {"name": "Foo"}

# Generated at 2022-06-14 15:03:18.885573
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest
    class SimpleSchema(Schema):
        val = Field(str)

    class SimpleSchema2(Schema):
        val = Field(bool)

    pytest.raises(ParseError, validate_yaml, "not valid yaml", SimpleSchema)
    value, error_messages = validate_yaml("val: hello", SimpleSchema)
    assert value == {"val": "hello"}

    # TypeError: The validator must be a Field or a Schema class
    pytest.raises(TypeError, validate_yaml, "", 0)

    value, error_messages = validate_yaml("val: True", SimpleSchema2)
    assert value == {"val": True}



# Generated at 2022-06-14 15:03:27.131962
# Unit test for function validate_yaml
def test_validate_yaml():
    class Dog(Schema):
        age = Field(type="integer")

    values = validate_yaml(
        content="""
        dogs:
            - name: "rover"
              age: "1"
              breed: "Dachshund"
            - name: "spot"
              age: "4"
              breed: "Unknown"
        """.strip(),
        validator={"dogs": [Dog()]},
    )


# Generated at 2022-06-14 15:03:37.587800
# Unit test for function validate_yaml
def test_validate_yaml():
  class Address(Schema):
    country = String(required=True)
    state = String
    city = String()
    street1 = String()
    street2 = String()
    street3 = String()
    zip_code = String()

  class Person(Schema):
    first_name = String()
    last_name = String()
    age = Integer()
    residence = Address()

  class Dog(Schema):
    name = String()
    age = Integer()
    weight = Float()
    owner = Reference(Person)

  class Cat(Schema):
    name = String()
    age = Integer()
    weight = Float()
    owner = Reference(Person)

  class PetSchema(Schema):
    type = Choice(["dog", "cat"])
    dog = Reference(Dog)

# Generated at 2022-06-14 15:03:48.725856
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, fields

    class Person(Schema):
        name = fields.String(max_length=10)
        age = fields.Integer(min_value=0, max_value=120)
        phone = fields.String(pattern=r"\(\d{3}\) \d{3}-\d{4}")

    content = """
    name: John Doe
    age: 25
    phone: (555) 555-5555
    """

    value, errors = validate_yaml(content, Person)

    assert not errors

    # required keys
    content = """
    name: John Doe
    """

    value, errors = validate_yaml(content, Person)

    assert len(errors) == 2
    assert errors[0].code == "required"
    assert errors[0].position.char_index

# Generated at 2022-06-14 15:03:57.838753
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer
    
    class Book(Schema):
        title = String(required=True)
        pages = Integer()

    book_data = """\
    title: Alice in Wonderland
    pages: 271
    """

    value, errors = validate_yaml(book_data, validator=Book)
    assert value == {"title": "Alice in Wonderland", "pages": 271}
    assert errors == []

    book_data = """\
    pages: 271
    title: Alice in Wonderland
    """
    value, errors = validate_yaml(book_data, validator=Book)
    assert value == {"title": "Alice in Wonderland", "pages": 271}
    assert errors == []

    book_data = """\
    title:
    pages: 271
    """


# Generated at 2022-06-14 15:04:05.246137
# Unit test for function validate_yaml
def test_validate_yaml():
    # Validating field
    field = typesystem.String(format="date-time")
    value, error_messages = validate_yaml("2020-04-02T12:00:00Z", field)
    assert value == "2020-04-02T12:00:00Z"
    assert len(error_messages) == 0

    value, error_messages = validate_yaml("2020-04-02T12:00:00", field)
    assert value == "2020-04-02T12:00:00"
    assert len(error_messages) == 1

    # Validating schema
    class User(typesystem.Schema):
        name = typesystem.String(format="date-time")

    value, error_messages = validate_yaml("2020-04-02T12:00:00Z", User)

# Generated at 2022-06-14 15:04:13.574160
# Unit test for function validate_yaml
def test_validate_yaml():
    i_content = """
        people:
          - first_name: Jane
            age: 37
            active: true
          - first_name: John
            age: 25
            active: false
    """
    i_field1 = Field(key="people")
    i_field2 = Field(key="first_name", min_length=2)
    i_field3 = Field(key="age", type="integer", required=False)
    i_field4 = Field(key="active", type="boolean")
    i_fields = [i_field1, [i_field2, i_field3, i_field4]]


# Generated at 2022-06-14 15:04:24.076423
# Unit test for function validate_yaml
def test_validate_yaml():
    class Validator(Schema):
        foo = Field(type="number")
        bar = Field(type="number")

    validator = Validator()

    doc = """
    foo: 5
    bar: "not a number"
    """
    value, errors = validate_yaml(doc, validator)
    assert value == {"foo": 5, "bar": "not a number"}

    assert len(errors) == 1
    assert errors[0].text == "Not a valid number."
    assert errors[0].position.line_no == 3
    assert errors[0].position.column_no == 5

    doc = """
    foo: "yep"
    """
    value, errors = validate_yaml(doc, validator)
    assert value == {"foo": "yep"}
    assert len(errors) == 2

   

# Generated at 2022-06-14 15:04:32.738660
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Unit test for function validate_yaml.
    """
    yaml_content = """
        name: foo
        age: 15
        tags: 
            - hello
            - world
        """
    # Create the schema.
    class Person(Schema):
        name: str
        age: int
        tags: typing.List[str]

    # Test the schema.
    value, error_messages = validate_yaml(yaml_content, validator=Person)
    assert error_messages == [], error_messages
    assert value == {
        "name": "foo",
        "age": 15,
        "tags": ["hello", "world"],
    }



# Generated at 2022-06-14 15:04:43.321195
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem import Schema, fields

    class SchemaExample(Schema):
        title = fields.String()
        description = fields.String()
        release = fields.String(min_length=2)

    content = yaml.dump(
        {"title": "test", "description": "test", "release": "test"},
        default_flow_style=False,
        encoding="utf-8",
    )
    result = validate_yaml(content, SchemaExample)
    assert result[0] == {"title": "test", "description": "test", "release": "test"}
    assert result[1] == []

# Generated at 2022-06-14 15:04:54.996390
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b"""\
    foo: 7
    """
    field = Field(name="foo", type=int, required=True)
    value, error_messages, _ = validate_yaml(content, field)
    assert value == 7
    assert error_messages == []

    content = b"a: b\n c\n"
    value, error_messages, _ = validate_yaml(content, field)
    assert error_messages == [
        ValidationError(
            text="Unable to convert value.",
            code="invalid",
            path=["foo"],
            position=Position(
                line_no=1, column_no=4, char_index=4, context=b"foo: b\n"
            ),
        )
    ]



# Generated at 2022-06-14 15:05:08.672409
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String

    validator = String()

    value, errors = validate_yaml(content="", validator=validator)
    assert value == ""
    assert errors == []

    value, errors = validate_yaml(content='{"a": "b"}', validator=validator)
    assert value == {}
    assert errors == [
        Message(
            text='"" is not a valid string at position (1, 1).',
            code="invalid",
            position=Position(
                line_no=1, column_no=1, char_index=0
            ),
        )
    ]

    value, errors = validate_yaml(content="'bloop'", validator=validator)
    assert value == "bloop"

# Generated at 2022-06-14 15:05:16.501669
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("- foo\n- bar")
    assert token.value == ["foo", "bar"]  # type: ignore
    assert token.start_pos == Position(char_index=0, line_no=1, column_no=1)
    assert token.end_pos == Position(char_index=8, line_no=2, column_no=4)

    token = tokenize_yaml("[]")
    assert token.value == []  # type: ignore
    assert token.start_pos == Position(char_index=0, line_no=1, column_no=1)
    assert token.end_pos == Position(char_index=2, line_no=1, column_no=3)

    token = tokenize_yaml("{}")
    assert token.value == {}  # type

# Generated at 2022-06-14 15:05:22.542550
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    class TestSchema(Schema):
        field = Field(type="integer", required=True)

    content = "field: 4"

    value, error_messages = validate_yaml(content, TestSchema)

    assert value == {"field": 4}
    assert error_messages == []



# Generated at 2022-06-14 15:05:27.971219
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Schema(
        {"a": int}, 
        error_formatters={"validate_required": "{value} is required.",}
    )
    assert validate_yaml(
        """
        ---
        {}
        """,
        validator=validator,
    ) == (
        {"a": None},
        [
            Message(
                text="'a' is required.", 
                code="validate_required",
                position=Position(column_no=9, line_no=2, char_index=13)
            )
        ],
    )



# Generated at 2022-06-14 15:05:34.130873
# Unit test for function validate_yaml
def test_validate_yaml():
    document = """
    foo: "bar"
    """
    schema = Schema("foo", fields={}, is_strict=False)
    validator = validate_yaml(content=document, validator=schema)
    assert validator[0]["foo"] == "bar"



# Generated at 2022-06-14 15:05:38.141861
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String
    from typesystem.schemas import Schema

    content = "hello"

    class MySchema(Schema):
        name = String(max_length=5)

    value, errors = validate_yaml(
        content=content,
        validator=MySchema(),
    )

    assert value == "hello"
    assert errors == []

# Generated at 2022-06-14 15:05:41.792520
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "1234"
    assert validate_yaml(content,Field(int)) == (1234,[])
    assert validate_yaml(content,Field(str))[1][0].code == "invalid_type"



# Generated at 2022-06-14 15:05:49.720919
# Unit test for function validate_yaml
def test_validate_yaml():
    # attributes to create the Schema
    name = "a_name"
    fields = {"first_field": int, "second_field": str, "third_field": str}
    metadata = {"extra": "value"}

    # create the schema
    schema = Schema(name, fields, metadata)

    # declare YAML string
    content = """
    first_field: 123
    second_field: 456
    third_field: abc
    """
    return_value = validate_yaml(content, schema)
    assert return_value == (
        {
            "first_field": 123,
            "second_field": "456",
            "third_field": "abc",
        },
        [],
    )



# Generated at 2022-06-14 15:06:01.477979
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test a scalar
    test_str = "str"
    token = tokenize_yaml(test_str)
    assert isinstance(token, ScalarToken)
    assert token.value == test_str
    assert token.start == 0
    assert token.end == 3

    # Test a list
    test_str = "- 1\n- 2\n- 3"
    token = tokenize_yaml(test_str)
    assert isinstance(token, ListToken)
    assert token.value == [1, 2, 3]
    assert token.start == 0
    assert token.end == len(test_str)

    # Test a dictionary
    test_str = "{a: 1, b: 2, c: 3}"
    token = tokenize_yaml(test_str)

# Generated at 2022-06-14 15:06:06.624737
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(fields={"name": str, "age": int})
    assert validate_yaml(content=b"name: foo", validator=schema) == ({'name': 'foo'}, [])
    assert validate_yaml(content=b"name: foo\nage: foo", validator=schema) == ({'name': 'foo', 'age': 'foo'}, None)
    assert validate_yaml(content=b"name: foo\nage: foo", validator=schema) != ({}, [])

