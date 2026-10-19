

# Generated at 2022-06-14 14:56:29.256174
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = "---\nname: Luke\nage: 23\n"
    tok = tokenize_yaml(content)

    def isinstance_many(obj, *types: type) -> bool:
        return any(isinstance(obj, typ) for typ in types)

    def is_scalar_token(tok) -> bool:
        return isinstance_many(tok, ScalarToken, int, float, bool, type(None))

    def is_list_token(tok) -> bool:
        return isinstance_many(tok, ListToken, list)

    def is_dict_token(tok) -> bool:
        return isinstance_many(tok, DictToken, dict)

    assert is_dict_token(tok)

# Generated at 2022-06-14 14:56:36.722584
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "a: 1"
    schema = Schema.from_fields({"a": Field(int)})
    value, error_messages = validate_yaml(content, schema)
    assert isinstance(value, dict)
    assert value == {"a": 1}
    assert len(error_messages) == 0

    content = "a: 1\nb: \"abc\""
    schema = Schema.from_fields({"a": Field(int), "b": Field(str)})
    value, error_messages = validate_yaml(content, schema)
    assert value == {"a": 1, "b": "abc"}
    assert len(error_messages) == 0

    content = "a: 1\nb: 2\nc: 3"

# Generated at 2022-06-14 14:56:48.156418
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("[1, 2, 3]") == ListToken([1, 2, 3], 0, 6, content="[1, 2, 3]")
    assert tokenize_yaml('{"a": "hello", "b": "world"}') == DictToken(
        {"a": "hello", "b": "world"},
        0,
        23,
        content='{"a": "hello", "b": "world"}',
    )
    assert tokenize_yaml("1") == ScalarToken(1, 0, 0, content="1")
    assert tokenize_yaml("1.0") == ScalarToken(1.0, 0, 2, content="1.0")
    assert tokenize_yaml("1e1") == ScalarToken(10.0, 0, 2, content="1e1")

# Generated at 2022-06-14 14:56:56.479923
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_str = '''
        name: Mark
        email: mark@example.com
        age: True
    '''
    class UserSchema(Schema):
        name = fields.String()
        email = fields.String()
        age = fields.Integer()

    value, error_messages = validate_yaml(content=yaml_str, validator=UserSchema)
    assert len(error_messages) > 0
    assert error_messages[0].position.line_no == 4
    assert error_messages[0].position.column_no == 5
    assert error_messages[0].position.char_index == 41
    assert error_messages[0].code == "invalid_type"

# Generated at 2022-06-14 14:57:06.184146
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    # Put all the assertions in the same way as the unit test for tokenize_json
    assert tokenize_yaml(b"[]") == ListToken([], 0, 1, content=b"[]")
    assert tokenize_yaml(b"[1]") == ListToken([1], 0, 3, content=b"[1]")
    assert tokenize_yaml(b"[1,2]") == ListToken([1, 2], 0, 6, content=b"[1,2]")
    assert tokenize_yaml(b"[1, 2]") == ListToken([1, 2], 0, 7, content=b"[1, 2]")

# Generated at 2022-06-14 14:57:17.209049
# Unit test for function validate_yaml
def test_validate_yaml():
    import json
    import random
    import string
    import unittest
    import sys

    from typesystem.base import MessageType
    from typesystem.exceptions import ValidationError
    from typesystem.fields import String

    # Create a schema for testing with.
    class MySchema(Schema):
        field = String(max_length=2)

    # Create content for testing with.
    content = u"""\
field: a
"""

    # Test 1: ensure that valid content validates and returns cleanly.
    (value, error_messages) = validate_yaml(content=content, validator=MySchema)
    assert error_messages == []

    # Test 2: ensure that invalid content raises ValidationError.
    content = u"""\
field: abc
"""

# Generated at 2022-06-14 14:57:28.159080
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(tokenize_yaml(""), DictToken)
    assert isinstance(tokenize_yaml("{}"), DictToken)
    assert isinstance(tokenize_yaml("[]"), ListToken)
    assert isinstance(tokenize_yaml("test"), ScalarToken)
    assert isinstance(tokenize_yaml("111"), ScalarToken)
    assert isinstance(tokenize_yaml("1.11"), ScalarToken)
    assert isinstance(tokenize_yaml("true"), ScalarToken)
    assert isinstance(tokenize_yaml("false"), ScalarToken)
    assert isinstance(tokenize_yaml("null"), ScalarToken)

# Generated at 2022-06-14 14:57:34.949067
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import yaml

    content = """
      - one
      - two
      - three
    """
    token = tokenize_yaml(content)
    assert isinstance(token, ListToken)
    assert len(token) == 3

    content = """
      one: 1
      two: 2
      three: 3
    """
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert len(token) == 3

    content = "this is a string"
    token = tokenize_yaml(content)
    assert isinstance(token, ScalarToken)
    assert token.value == content

    content = "123"
    token = tokenize_yaml(content)
    assert isinstance(token, ScalarToken)
    assert token.value == 123


# Generated at 2022-06-14 14:57:44.549500
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("") == ListToken([], 0, -1)
    assert tokenize_yaml("[0, 1]") == ListToken([0, 1], 0, 6)
    assert tokenize_yaml("{a: b}") == DictToken({"a": "b"}, 0, 5)
    assert tokenize_yaml("{a: b, c: d}") == DictToken({"a": "b", "c": "d"}, 0, 11)
    assert tokenize_yaml("0") == ScalarToken(0, 0, 0)
    assert tokenize_yaml("1") == ScalarToken(1, 0, 0)
    assert tokenize_yaml("a") == ScalarToken("a", 0, 0)

# Generated at 2022-06-14 14:57:52.302261
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Text, Integer
    from typesystem.schemas import Schema

    class SimpleSchema(Schema):
        name = Text()
        age = Integer()

    content = """
name: foo
age: bar
"""
    value, errors = validate_yaml(content, SimpleSchema)
    assert not value
    assert len(errors) == 1
    assert errors[0].text == "Value must be a valid integer."
    assert errors[0].position.line_no == 3
    assert errors[0].position.column_no == 6



# Generated at 2022-06-14 14:58:06.930846
# Unit test for function validate_yaml
def test_validate_yaml():
    class SimpleSchema(Schema):
        foo = Field(type="string")
        bar = Field(type="string", min_length=2)
        baz = Field(type="string", min_length=2, max_length=5)
        number = Field(type="integer")
        float_number = Field(type="float")

    content = yaml.dump(
        {"foo": "spam", "bar": "spam spam spam spam spam spam spam spam spam spam spam", "number": 7.5, "float_number": 5.6}
    )
    value, errors = validate_yaml(content, SimpleSchema)


# Generated at 2022-06-14 14:58:09.933964
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, Schema

    class PetSchema(Schema):
        name = Integer()
        age = Integer()

    PetSchema.validate_yaml('name: 1\nage: 2')



# Generated at 2022-06-14 14:58:13.018135
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    a: "b"
    """
    validator = Field(type=str)
    assert validate_yaml(content, validator) == ("b", [])



# Generated at 2022-06-14 14:58:24.024475
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.base import ValidationError
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.tokenize import validate_yaml

    class MySchema(Schema):
        my_field = String()

    value, errors = validate_yaml(content="---\nmy_field: value", validator=MySchema)
    assert value == {"my_field": "value"}
    assert errors == []

    value, errors = validate_yaml(
        content="---\nmy_field: value", validator=MySchema(required=["my_field"])
    )
    assert value == {}
    assert errors[0].args == (
        "Missing required value for field 'my_field'.",
        "required_field",
    )

# Generated at 2022-06-14 14:58:28.926013
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '---\nname: Kevin\n'
    data_type = typing.Dict[str, str]
    try:
        value, messages = validate_yaml(content, data_type)
    except ParseError as e:
        assert False, "It should work normally."


if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 14:58:38.361102
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    def test(yaml, field, expected_msg=None, expected_errors=None, expected_value=None):
        field = field()
        value, errors = validate_yaml(yaml, field)
        # assert value == expected_value
        assert expected_msg == errors[0].text
        assert expected_errors == errors[0].code
        return value, errors

    test(
        "test",
        typesystem.String,
        expected_msg="Must be valid JSON.",
        expected_errors="parse_error",
        expected_value=None,
    )

# Generated at 2022-06-14 14:58:44.270224
# Unit test for function validate_yaml
def test_validate_yaml():
    import json

    content = (
        "---\n"
        "employees:\n"
        "  - name: John Smith\n"
        "    age: 33\n"
        "    department: Engineering\n"
        "  - name: Alice White\n"
        "    age: 27\n"
        "    department: IT\n"
    )

    class Employee(Schema):
        name = String()
        age = Integer()
        department = String()

    class EmployeeList(Schema):
        employees = List(items=Employee())

    success, messages = validate_yaml(content, EmployeeList)
    assert success is None
    assert messages == []


# Generated at 2022-06-14 14:58:54.082290
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """Tokenize the following yaml and check the result."""

    input_yaml = "{'key1':'string', 'key2': True, 'key3': 1, 'key4': 2.0, 'key5': None, 'key6': [1, 2, 3], 'key7': [{'key8': 'value8'}, {'key9':'value9'}]}"
    expected_result = {
        "key1": "string",
        "key2": True,
        "key3": 1,
        "key4": 2.0,
        "key5": None,
        "key6": [1, 2, 3],
        "key7": [
            {"key8": "value8"}, 
            {"key9": "value9"}
        ]
    }

    result = tokenize_yaml

# Generated at 2022-06-14 14:59:01.334161
# Unit test for function validate_yaml
def test_validate_yaml():
    a = Field(required=True, primitive_type=int)
    b = Field(required=True, primitive_type=str)
    c = Field(required=True, primitive_type=str)
    class SchemaTest(Schema):
        a = a
        b = b
        c = c

    value, error_messages = validate_yaml(content="a: 1", validator=SchemaTest)
    assert value is not None
    assert error_messages == []

    value, error_messages = validate_yaml(content="a: [1, 2]", validator=SchemaTest)
    assert value is None

# Generated at 2022-06-14 14:59:13.206324
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    name: typesystem
    age: "40"
    married: true
    """
    class Person(Schema):
        name = field(type=str)
        age = field(type=int)
        married = field(type=bool)

    value, error_messages = validate_yaml(content=content, validator=Person())
    assert isinstance(value, Person)

    content = """
    name: typesystem
    age: "40"
    married: true
    """
    class Person(Schema):
        name = field(type=str)
        age = field(type=str)
        married = field(type=str)

    value, error_messages = validate_yaml(content=content, validator=Person())
    assert isinstance(value, Person)


# Generated at 2022-06-14 14:59:22.544410
# Unit test for function validate_yaml
def test_validate_yaml():
    content = dedent(
        """
        name: Evan
        schema: {type: string, min_length: 3, max_length: 10}
        """
    )
    validator = {
        "name": "string",
        "schema": {"type": "object", "properties": {"type": {"type": "string"}}},
    }
    v = validate_yaml(content, validator)
    assert not v.errors, (
        "Expected success, but got errors:\n" + "\n".join(map(repr, v.errors))
    )

# Generated at 2022-06-14 14:59:33.107632
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Boolean, Integer, String
    from typesystem.schemas import Schema

    class YAML(Schema):
        count = Integer()
        flag = Boolean()
        text = String()

    content = "count: 1\nflag: true\ntext: hello\n"
    assert validate_yaml(content, YAML) == ({"count": 1, "flag": True, "text": "hello"}, [])

    content = """\
    count: 1
    flag: true
    text: hello
    """
    assert validate_yaml(content, YAML) == ({"count": 1, "flag": True, "text": "hello"}, [])

    content = """\
    count: x
    flag: true
    text: hello
    """
    value, errors = validate_yaml

# Generated at 2022-06-14 14:59:45.827563
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test parse error
    invalid_yaml = """
    - string
    - 1
    - true
    """
    try:
        value, errors = validate_yaml(invalid_yaml, validator=list)
    except ParseError as exc:
        assert exc.position.line_no == 4
        assert exc.position.column_no == 9
        assert exc.position.char_index == 24
        assert exc.code == "parse_error"

    # Test validation error for an invalid field
    invalid_yaml = """
    bool_field: True
    """
    try:
        value, errors = validate_yaml(invalid_yaml, validator=Field())
    except ValidationError as exc:
        assert exc.position.line_no == 2
        assert exc.position.column_no == 0


# Generated at 2022-06-14 14:59:50.983960
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml('{"a": 123}',{'a':'Number'}) == ({'a': 123}, [])
    assert validate_yaml('["one", "two", "three"]',['Text']) == (['one', 'two', 'three'], [])
    assert validate_yaml('1', 'Number') == (1, [])
    assert validate_yaml('true', 'Boolean') == (True, [])
    assert validate_yaml('null', 'Null') == (None, [])

# Generated at 2022-06-14 15:00:01.703281
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert(tokenize_yaml("foo") == ScalarToken("foo",0,2,content="foo"))
    assert(tokenize_yaml("'foo'") == ScalarToken("foo",0,5,content="'foo'"))
    assert(tokenize_yaml("\"foo\"") == ScalarToken("foo",0,5,content='"foo"'))
    assert(tokenize_yaml("- foo") == ListToken(["foo"],0,5,content="- foo"))
    assert(tokenize_yaml("- 1\n- 2\n- 3") == ListToken([1,2,3],0,12,content="- 1\n- 2\n- 3"))

# Generated at 2022-06-14 15:00:13.744118
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml(b"foo: bar")
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == 7
    assert token.value == {"foo": "bar"}
    assert token.content == "foo: bar"

    # Test parsing invalid YAML strings.
    with pytest.raises(ParseError) as excinfo:
        tokenize_yaml("foo: bar:")

    assert excinfo.value.text == "mapping values are not allowed here."
    assert excinfo.value.position.column_no == 9
    assert excinfo.value.position.line_no == 1
    assert excinfo.value.position.char_index == 8

    # Test parsing empty strings.

# Generated at 2022-06-14 15:00:19.161789
# Unit test for function validate_yaml
def test_validate_yaml():
    data = "number: '16'"
    field = Field(type='integer', required=True)
    value, errors = validate_yaml(data, field)
    assert errors[0].text == "Value '16' is not a valid integer."
    assert errors[0].code == "invalid_type"

# Generated at 2022-06-14 15:00:28.009162
# Unit test for function validate_yaml
def test_validate_yaml():
    # pylint: disable=redefined-outer-name
    content = """
# This is a comment.
name: Example
location:
  name: USA
  lat: 38
  long: -77
"""

    class LocationSchema(Schema):
        name = Field(label="Location Name", required=True)
        lat = Field(label="Latitude", required=True)
        long = Field(label="Longitude", required=True)

    class Location(Schema):
        name = Field(label="Name", required=True)
        location = Field(label="Location", validators=[LocationSchema()], required=True)

    location = Location().validate(content)
    assert isinstance(location, dict)
    assert location["name"] == "Example"
    assert location["location"]["name"] == "USA"
   

# Generated at 2022-06-14 15:00:38.918745
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Test that the value returned from tokenize_yaml matches the input
    """
    input = """\
m1:
  - 1
  - a
m2:
  m21:
    - b
    - c
    - "null"
m3:
  - x
  -
    m31: y
        m32:
          - a
          -
            m321: b"""
    output = tokenize_yaml(input)
    expected = {
        "m1": ["1", "a"],
        "m2": {"m21": ["b", "c", "null"]},
        "m3": ["x", {"m31": "y", "m32": ["a", {"m321": "b"}]}],
    }

    assert output == expected



# Generated at 2022-06-14 15:00:42.354772
# Unit test for function validate_yaml
def test_validate_yaml():
    #Test file is from validators.py
    #validate_yaml("""
    # a:
    #   - b
    #   - c
    #""", fields.Dict())
    assert True

# Generated at 2022-06-14 15:00:52.834984
# Unit test for function validate_yaml
def test_validate_yaml():
    class User(Schema):
        name = fields.String()
        email = fields.String()
        active = fields.Boolean(default=True)

    message = validate_yaml(
        content="""
        name: "John Smith"
        email: "jsmith@example.com"
        active: true
    """,
        validator=User
    )
    assert message == Message('{"name": "John Smith", "email": "jsmith@example.com", "active": true}')

    message = validate_yaml(
        content="""
        name: "John Smith"
        email: jsmith@example.com
        active: true
    """,
        validator=User
    )

# Generated at 2022-06-14 15:00:57.027940
# Unit test for function validate_yaml
def test_validate_yaml():
    token = tokenize_yaml('hello: world\n')
    def validate_with_positions(token, validator):
        return "hello"
    assert validate_yaml('hello: world\n', 'func') == validate_with_positions(token, 'func')

# Generated at 2022-06-14 15:01:08.458924
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert not "!" in tokenize_yaml("!!!")
    assert tokenize_yaml("a: 1") == {'a': 1}
    assert tokenize_yaml('1') == 1
    assert tokenize_yaml('test') == 'test'
    assert tokenize_yaml('1.1') == 1.1
    assert tokenize_yaml('"1"') == '1'
    assert tokenize_yaml('true') is True
    assert tokenize_yaml('false') is False
    assert tokenize_yaml('null') is None
    assert tokenize_yaml('[1, 2]') == [1, 2]
    assert tokenize_yaml('[1, [2, 3]]') == [1, [2, 3]]


# Generated at 2022-06-14 15:01:16.398680
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    - one
    - two
    - three
    """
    result, error_messages = validate_yaml(content, List[ScalarToken])
    assert error_messages == []
    assert result == [
        ScalarToken("one", 0, 3, content),
        ScalarToken("two", 5, 8, content),
        ScalarToken("three", 10, 16, content),
    ]

    content = """
    - one
    - [1, 2, 3]
    - three
    """
    result, error_messages = validate_yaml(content, List[ScalarToken])
    assert len(error_messages) == 1
    assert isinstance(error_messages[0], ValidationError)
    assert error_messages[0].code == "invalid_field"


# Generated at 2022-06-14 15:01:24.036199
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_input = '''
    color_name: blue
    age: 21
    '''
    schema = Schema(
        {"color_name": Field(str), "age": Field(int, lower_bound=21, upper_bound=25)}
    )
    (value, error_list) = validate_yaml(yaml_input, schema)
    assert not error_list

    yaml_input = '''
    color_name: blue
    age: 20
    '''
    (value, error_list) = validate_yaml(yaml_input, schema)
    assert error_list
    error = error_list[0]
    assert isinstance(error, ValidationError)
    assert error.key == "age"
    assert not error.value
    assert error.code == "min_value"
   

# Generated at 2022-06-14 15:01:34.793482
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.structures import Map, String

    token = tokenize_yaml("""\
    id: 'abc'
    name: 'Test'
    """)
    schema = Map({"id": String(), "name": String()})
    test_result = validate_yaml("""\
    id: 'abc'
    name: 'Test'
    """, schema)
    assert test_result == ({'id': 'abc', 'name': 'Test'}, [])

    test_result = validate_yaml("""\
    id: 'abc'
    name:
    """, schema)
    assert test_result == None

    test_result = validate_yaml("""
    id: 'abc'
    name: 'Test'
    """, schema)
    assert test_result == None

    test_result = validate

# Generated at 2022-06-14 15:01:41.152815
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.exceptions import ValidationError, ParseError
    
    
    content = """
    - 1
    - 2
    - 3
    """
    validator = String()
    assert validate_yaml(content, validator) == (None, [{'code': 'invalid_type', 'messages': [{'code': 'expected_string', 'text': 'A string is required.', 'position': {'column_no': 5, 'line_no': 2, 'char_index': 6}}]}])
    
    # Test expected error message format.
    content = """
    - one
    - two
    - three
    """
    validator = String()

# Generated at 2022-06-14 15:01:48.574010
# Unit test for function validate_yaml
def test_validate_yaml():
    # content = b"string"
    # print (content)
    # print(validate_yaml(content, String))

    content = '["foo", "bar", "baz"]'
    print(content)
    print(validate_yaml(content, List))

    # # raises ParseError
    # print("\nThe following raises ParseError:\n")
    # content = b'{123: "foo"}'
    # print(content)
    # print(validate_yaml(content, String))

# following yields exception
    # print("\nThe following yields exception:\n")
    # content = b'[123, "bar", "baz"]'
    # print(content)
    # print(validate_yaml(content, List))

    # raises ValidationError

# Generated at 2022-06-14 15:01:57.877427
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        name = String()
        email = String()

    content = "name: Greg\nemail: greg@example.com\n"
    assert validate_yaml(content, UserSchema) == ("name: Greg\nemail: greg@example.com\n",[])

    content1 = "name: Greg\nemail: INVALID\n"
    assert validate_yaml(content1, UserSchema) == (None, [
        Message(
            text="Must be valid email address.",
            code="invalid",
            field_name="email",
            position=Position(
                line_no=2, column_no=7, char_index=16
            ),
        ),
    ])


# Generated at 2022-06-14 15:02:09.184635
# Unit test for function validate_yaml
def test_validate_yaml():
    class Sample(Schema):
        a_number = Integer(minimum=2)

    valid_yaml = "a_number: 1"
    assert validate_yaml(valid_yaml, Sample) == (
        {},
        [
            Message(
                text="Must be greater than or equal to 2.",
                code="min_value",
                position=Position(line_no=1, column_no=1, char_index=7),
            )
        ],
    )

    invalid_yaml = "a_number 1"

# Generated at 2022-06-14 15:02:23.133489
# Unit test for function validate_yaml
def test_validate_yaml():
    input = """
    name: Bob
    age: 30
    """

    schema = """
    type: object
    properties:
        name:
            type: string
            minLength: 1
        age:
            type: integer
            minimum: 0
    required:
        - name
        - age
    """

    schema = Field(schema=yaml.load(schema))

    data, errors = validate_yaml(input, schema)
    assert len(errors) == 0

    # Test scalar validation error.
    input = """
    name: Bob
    age: -30
    """

    value, errors = validate_yaml(input, schema)
    assert len(errors) == 1
    error = errors[0]
    assert error.code == "minimum"

# Generated at 2022-06-14 15:02:33.176727
# Unit test for function validate_yaml
def test_validate_yaml():
    from jupyter_server.serverapp import validate_yaml
    from typesystem import String

    yaml_content = u"""
        name: JupyterHub
        base_url: /hub
        proxy_api_ip: 127.0.0.1
        hub:
          ip: 0.0.0.0
          port: 8081
          cookie_secret: "fuckyou"
        """

    schema = {
        "name": String(),
        "base_url": String(),
        "proxy_api_ip": String(),
        "hub": {
            "ip": String(),
            "port": String(),
            "cookie_secret": String(),
        }
    }

    value, errors = validate_yaml(yaml_content, schema)

# Generated at 2022-06-14 15:02:44.494457
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    import yaml
    class BookSchema(typesystem.Schema):
        author = typesystem.String()
        title = typesystem.String(max_length=100)
        price = typesystem.Number(minimum=0.0)
        release_date = typesystem.Date()
        tags = typesystem.Array(items=typesystem.String())

    content = yaml.safe_load('''
        author: "...author name..."
        title: "Title of the book"
        price: 10.00
        release_date: ... your favorite date ...
        tags:
            - "tag one"
            - "tag two"
    ''')

    book_schema = BookSchema()
    value, errors = validate_yaml(content, book_schema)
    assert value == content  # parsed

# Generated at 2022-06-14 15:02:53.358751
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(type="string")
    schema = Schema(fields={"foo": field})
    data, errors = validate_yaml(b"foo: abc", schema)
    assert data == {"foo": "abc"}
    assert errors == []
    data, errors = validate_yaml(b"foo: ", schema)
    assert data == {"foo": ""}
    assert len(errors) == 1
    assert errors[0].code == "required"
    data, errors = validate_yaml(b"foo: 123", schema)
    assert errors[0].code == "invalid_type"


# Generated at 2022-06-14 15:02:54.755523
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert _get_position(content={"test": "value"})

# Generated at 2022-06-14 15:03:00.994412
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("123") == ScalarToken(123, 0, 2)

    assert tokenize_yaml("key: value") == DictToken({"key": "value"}, 0, 9)

    assert tokenize_yaml("[1, 2, 3]") == ListToken([1, 2, 3], 0, 8)

    assert tokenize_yaml("") == ScalarToken("", 0, 0)

    with pytest.raises(ParseError, match="No content."):
        tokenize_yaml(" ")



# Generated at 2022-06-14 15:03:09.020374
# Unit test for function validate_yaml
def test_validate_yaml():
    content = bytes(
        """\n
        birth_date: 2020-04-01
        first_name: Val
        last_name: Emmich\n
        """,
        encoding="utf-8",
    )
    fields = {
        "first_name": Field(type="string"),
        "last_name": Field(type="string"),
        "birth_date": Field(type="date"),
    }
    OnePerson = Schema(fields=fields)
    value, errors = validate_yaml(content, validator=OnePerson)
    print(value, errors)


if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 15:03:10.557387
# Unit test for function validate_yaml
def test_validate_yaml():#TODO: write tests
    assert True

# Generated at 2022-06-14 15:03:15.774330
# Unit test for function validate_yaml
def test_validate_yaml():
    class AnimalSchema(Schema):
        name = Field.string()
        age = Field.integer()

    content = """
    name: Cow
    age: 4
    """
    result = validate_yaml(content, AnimalSchema)  #type: ignore
    assert result == ({'name': 'Cow', 'age': 4},[])

# Generated at 2022-06-14 15:03:26.474815
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None
    from typesystem import fields

    schema = fields.Dictionary(
        {"number": fields.Float(required=True), "name": fields.String(required=True)}
    )

    # Valid content
    value, errors = validate_yaml("""
        number: 3.14
        name: pi
    """, schema)
    assert not errors

    # Invalid content
    value, errors = validate_yaml("""
        number: pie
        name: pi
    """, schema)
    assert errors
    assert errors[0].code == "invalid_type"
    assert errors[0].position.column_no == 9
    assert errors[0].position.line_no == 2

    # Empty content
    value, errors = validate_yaml("", schema)
    assert errors

# Generated at 2022-06-14 15:03:41.423482
# Unit test for function validate_yaml
def test_validate_yaml():
    str_yaml = """\
    name: "John"
    age: 27
    """
    schema = Schema(
        name=str,
        age=int
    )
    (value, error_messages) = validate_yaml(str_yaml, schema)
    assert value == {'name': 'John', 'age': 27}
    assert len(error_messages) == 0


# Generated at 2022-06-14 15:03:51.667492
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Tests the validation method 'validate_yaml'
    """
    from typesystem import String
    from typesystem.schemas import Schema
    from typesystem.exceptions import ValidationError, ParseError

    validator = Schema(
        {
            "integer": String(min_length=6, max_length=15),
            "string": String(),
            "decimal": String(),
        }
    )

    yaml_input = """
        integer: hello
        string: "hello world"
        decimal: 3.4
    """

    # Tests for validator field
    with raises(ValidationError) as e:
        validate_yaml(yaml_input, validator)
    assert e.value.code == "min_length"

# Generated at 2022-06-14 15:04:01.433245
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test dict tokenization
    str_content = "{"
    token = tokenize_yaml(str_content)
    assert isinstance(token, DictToken)

    # Test list tokenization
    str_content = "["
    token = tokenize_yaml(str_content)
    assert isinstance(token, ListToken)

    # Test value tokenization
    str_content = "True"
    token = tokenize_yaml(str_content)
    assert isinstance(token, ScalarToken)

    # Test start / end tokens
    str_content = "true"
    token = tokenize_yaml(str_content)
    assert token.start == 0
    assert token.end == 3

    # Test exception handling
    str_content = "? False\n"

# Generated at 2022-06-14 15:04:09.186430
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String

    assert validate_yaml("", String()) == (None, [])
    assert (
        validate_yaml("", String(required=True))
        == (None, [Message(text="This field is required.", code="required")])
    )

    # Test a string
    assert validate_yaml("foo", String()) == ("foo", [])
    assert (
        validate_yaml("foo", String(min_length=3)) == ("foo", [])
    )  # type: ignore
    assert (
        validate_yaml("foo", String(max_length=3)) == ("foo", [])
    )  # type: ignore
    assert (
        validate_yaml("foo", String(pattern='"foo"')) == ("foo", [])
    )  # type: ignore

# Generated at 2022-06-14 15:04:16.228719
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = String(min_length=1)
        age = Integer()
        height = Float(max_value=2.22, min_value=1.72)

    payload = """
    name: Joe
    age: 42
    height: 1.93
    """

    data, error_messages = validate_yaml(payload, PersonSchema)

    assert data == {"name": "Joe", "age": 42, "height": 1.93}
    assert error_messages == []

# Generated at 2022-06-14 15:04:26.095090
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem import Integer, String

    class TestSchema(Schema):
        first_name = String(max_length=15)
        last_name = String(max_length=15)
        age = Integer()

    # Test the case of a successful yaml parse and schema validation.
    content = b"first_name: Harry\nlast_name: Potter\nage: 16"
    value, errors = validate_yaml(content, TestSchema)
    assert isinstance(value, dict) and not errors
    assert value["first_name"] == "Harry"
    assert value["last_name"] == "Potter"
    assert value["age"] == 16

    # Test the case of an unsuccessful yaml parse.
    content = b"first_name: 'Harry Potter"

# Generated at 2022-06-14 15:04:36.848999
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = Field(str)
        age = Field(int)
    info = """
    name: John Doe
    age: 23
    """
    assert validate_yaml(info, PersonSchema) == (
        {"name": "John Doe", "age": 23},
        [],
    )
    age_info = """
    name: John Doe
    age: twenty-three
    """

# Generated at 2022-06-14 15:04:45.506329
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "foo: 'bar'"
    validator = Field(type="string")
    val, errors = validate_yaml(content, validator)
    assert val == "bar"
    assert not errors

    content = "foo: 1"
    val, errors = validate_yaml(content, validator)
    assert not val
    assert len(errors) == 1
    error = errors[0]
    assert error.code == "invalid"
    assert error.schema == {'type': 'string'}
    assert error.position.line_no == 1
    assert error.position.column_no == 5
    assert error.position.char_index == 4

# Generated at 2022-06-14 15:04:56.503507
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    - 1
    - 2
    - 3
    """
    validator = typing.List[int]
    # python 3.7+
    value, error_messages = validate_yaml(content, validator)
    assert value == [1, 2, 3]
    assert error_messages == []

    content = """
    name: Alice
    age: 42
    """
    validator = typing.Mapping[str, typing.Any]
    value, error_messages = validate_yaml(content, validator)
    assert value == {"name": "Alice", "age": 42}
    assert error_messages == []

    content = """
    not-a-valid-key: value
    """
    validator = typing.Mapping[str, typing.Any]

# Generated at 2022-06-14 15:05:01.028071
# Unit test for function validate_yaml
def test_validate_yaml():
    from yaml import safe_load
    from typesystem.fields import String

    content = """
        key: value
    """
    value, errors = validate_yaml(content, String)
    assert value == safe_load(content)
    assert isinstance(errors, list)
    assert not errors



# Generated at 2022-06-14 15:05:23.153793
# Unit test for function validate_yaml
def test_validate_yaml():
    ok, error_messages = validate_yaml("5", validator=Field(type="integer"))

    assert ok == 5
    assert error_messages == ""

    class MySchema(Schema):
        name = Field(type="string")

    # Validate a YAML string.
    yaml_str = "name: John"
    ok, error_messages = validate_yaml(yaml_str, validator=MySchema)

    assert ok.name == "John"
    assert error_messages == ""

    # Validate a YAML bytestring.
    yaml_bytes = b"name: John"
    ok, error_messages = validate_yaml(yaml_bytes, validator=MySchema)

    assert ok.name == "John"
    assert error_messages == ""



# Generated at 2022-06-14 15:05:36.424517
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_string = """!Schema
    name: str
    age: int
    """
    class Person(Schema):
        name = str
        age = int
    value, err_message = validate_yaml(yaml_string, Person)
    assert value == {"name": "str", "age": "int"}
    assert not err_message, err_message
    yaml_string = """!Schema
    name: str
    age: int
    """
    class Person(Schema):
        name = str
        age = str
    value, err_message = validate_yaml(yaml_string, Person)
    assert err_message == Message(
        text="Enter a valid integer.", code="invalid", position=Position(line_no=3, column_no=5, char_index=23)
    )

# Generated at 2022-06-14 15:05:46.752968
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    import typesystem.tokenize.positional_validation as pos
    schema = typesystem.Schema(
        properties={
            "name": typesystem.String(),
            "age": typesystem.Integer(),
            "address": typesystem.String(),
            "info": typesystem.Schema(
                properties={
                    "description": typesystem.String(),
                },
            ),
        },
    )
    content = """
    name: John Doe
    age: 42
    address: Ye Olde Inn, 123, High Street
    info:
        description: some description
    """
    result = validate_yaml(content, schema)

# Generated at 2022-06-14 15:05:51.685059
# Unit test for function validate_yaml
def test_validate_yaml():
    # These should be perfect
    assert validate_yaml(content=b'name: "John Doe"', validator=Schema([
        {"type": str, "name": "name", "min_length": 5, "max_length": 50}
    ])) == ({"name": "John Doe"}, [])
    assert validate_yaml(content=b'name: "John Doe"', validator=Schema([
        {"type": str, "name": "name", "enum": ["John Doe"]}
    ])) == ({"name": "John Doe"}, [])

# Generated at 2022-06-14 15:06:03.384730
# Unit test for function validate_yaml
def test_validate_yaml():
    # 1. Parse and validate a YAML string, returning positionally marked error messages on parse or validation failures.
    # 1.1 Describe how to parse and validate a YAML string, returning positionally marked error messages on parse or 
    #     validation failures.
    # 1.1.1 Define a class, which inherits from Field, named Field1.
    class Field1(Field):
        # 1.1.1.1 Define a method named check to check whether the type of a value is a bool.
        def check(self, value):
            # 1.1.1.1.1 Check whether the type of the value is a bool.
            if not isinstance(value, bool):
                # 1.1.1.1.1.1 Raise a validation error if the type of the value is not a bool.
                raise ValidationError

# Generated at 2022-06-14 15:06:13.862017
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(
        {
            "people": ListField(
                Schema(
                    {
                        "name": StringField(),
                        "age": IntField(max_value=150),
                        "date_of_birth": DateTimeField(format="%Y-%m-%d"),
                        "address": Schema(
                            {
                                "street_address": StringField(),
                                "city": StringField(),
                                "state": StringField(),
                                "country": StringField(default="USA"),
                                "postal_code": StringField(),
                            }
                        ),
                        "is_present": BooleanField(default=True),
                    }
                )
            )
        },
        strict=True,
    )

    # Create a YAML string to pass to validate_yaml
    yaml