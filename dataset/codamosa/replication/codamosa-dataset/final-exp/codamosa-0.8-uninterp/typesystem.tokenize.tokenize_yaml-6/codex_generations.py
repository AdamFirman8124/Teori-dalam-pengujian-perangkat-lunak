

# Generated at 2022-06-14 14:56:29.941836
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = b"""
    hello: world
    a: 1
    b: 2
    c: 3
    d: 4
    e: 5
    """
    token = tokenize_yaml(content)
    assert token.value == {
        "hello": "world",
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
    }
    assert token.start == 3
    assert token.end == 45
    assert token.content == b"""
    hello: world
    a: 1
    b: 2
    c: 3
    d: 4
    e: 5
    """


# Generated at 2022-06-14 14:56:37.348579
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test valid yaml
    yaml_valid = """
    foo: bar
    """
    token = tokenize_yaml(yaml_valid)
    assert type(token) == DictToken
    assert token.value == {'foo': 'bar'}
    assert token.start_index == 1
    assert token.end_index == len(yaml_valid) - 1

    # Test content less than 1 character
    yaml_empty = ""
    token = tokenize_yaml(yaml_empty)
    assert type(token) == DictToken
    assert token.value ==  {}
    assert token.start_index == 0
    assert token.end_index == -1

    # Test yaml with no content and spaces
    yaml_no_content = "\n"

# Generated at 2022-06-14 14:56:48.519802
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import fields
    from typesystem import Schema

    string = """
    persons:
      - name: John Doe
        age: 20
      - name: Jane Doe
        age: 21
    """

    class PersonSchema(Schema):

        name = fields.String()
        age = fields.Integer()

    class TeamSchema(Schema):

        persons = fields.Array(items=PersonSchema)

    value, error_messages = validate_yaml(string, TeamSchema)


# Generated at 2022-06-14 14:56:53.368289
# Unit test for function validate_yaml
def test_validate_yaml():
    error_messages = validate_yaml("[{'name': 'Jane', 'age': 40}]", validator=Schema)
    assert len(error_messages) == 2

    error_messages = validate_yaml("[{'name': 'Jane', 'age': 40}]", validator=Field)
    assert len(error_messages) == 2

# Generated at 2022-06-14 14:57:01.350190
# Unit test for function validate_yaml
def test_validate_yaml():
    data = '{"id": 2, "name": "test", "active": false, "items": ["A", "B", "C"]}'
    data = str(data).encode('utf-8')
    schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "active": {"type": "boolean"},
        "items": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
    }
    }
    data = yaml.load(data, Loader=yaml.FullLoader)
    assert validate_yaml(data, schema)


# Generated at 2022-06-14 14:57:08.426795
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    from typesystem.schemas import Schema
    from typesystem.fields import Integer, String

    class SimpleSchema(Schema):
        a = Integer(title="The 'a' field")
        b = Integer(title="The 'b' field")
        c = String(title="The 'c' field")

    content = """
        a: 1
        b: 2
        c: not_an_integer
    """
    value, messages = validate_yaml(content, validator=SimpleSchema)
    assert value is None
    assert len(messages) == 1
    assert messages[0].code == "invalid_type"
    assert messages[0].text == "Must be of type 'integer'."
    assert messages[0].position.line_no

# Generated at 2022-06-14 14:57:16.428481
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("") is None # Empty string
    assert tokenize_yaml("  ") is None # Empty string with spice
    assert tokenize_yaml('''
        # object
        foo: bar
        # array
        baz:
          - 1
          - 2''') == {"foo": "bar", "baz": [1, 2]} # New lines should be ignored
    assert tokenize_yaml("{ foo: bar }") == {"foo": "bar"} # JSON
    assert tokenize_yaml("foo: bar") == {"foo": "bar"} # Without braces
    # Different scalar types
    assert tokenize_yaml("foo: 2") == {"foo": 2}
    assert tokenize_yaml("foo: 1.5") == {"foo": 1.5}

# Generated at 2022-06-14 14:57:27.530351
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    from typesystem.schemas import Schema

    class TestSchema(Schema):
        name = Field(required=True)

    token = tokenize_yaml(content="name: Test")
    assert token["name"].value == "Test"
    assert validate_yaml(content=token, validator=TestSchema) == (
        {"name": "Test"},
        [],
    )

    token = tokenize_yaml(content=["a", "b", 2])
    assert validate_yaml(token, validator=Field(item=Field(type=str))) == (
        ["a", "b", "2"],
        [],
    )

    token = tokenize_yaml(content={"key": "value"})

# Generated at 2022-06-14 14:57:38.677875
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    '''
    Tests that tokenize_yaml handles multiple types of input correctly.
    '''
    token = tokenize_yaml('foo: bar\n')
    assert isinstance(token, DictToken)
    assert token.pos.line_no == 1
    assert token.pos.column_no == 1
    assert token.pos.char_index == 0

    token = tokenize_yaml('foo: bar')
    assert isinstance(token, DictToken)
    assert token.pos.line_no == 1
    assert token.pos.column_no == 1
    assert token.pos.char_index == 0

    token = tokenize_yaml('foo: bar\nfizz: buzz\n')
    assert isinstance(token, DictToken)
    assert token.pos.line_no == 1
    assert token

# Generated at 2022-06-14 14:57:46.487091
# Unit test for function validate_yaml

# Generated at 2022-06-14 14:57:57.706284
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''[{
            "pk": "1",
            "created_by": "user"
        },
        {
            "pk": 2,
            "created_by": "user"
        }
    ]'''
    field = Field(required=True, coerce=int, name="pk")
    schema = Schema(fields=[field])
    value, error_messages = validate_yaml(content, schema)
    expected_error_messages = (
        'Invalid value "1", expected an integer.',
        'Invalid value "user", not of type "string".',
    )
    assert error_messages == expected_error_messages


# Generated at 2022-06-14 14:58:09.001833
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = String(required=True)
        email = String(format="email")

    p1 = Position(line_no=1, column_no=12, char_index=11)
    p2 = Position(line_no=2, column_no=12, char_index=22)
    p3 = Position(line_no=2, column_no=27, char_index=26)

    content = """
        name:
        email: test@example.com
        """

    _, error_messages = validate_yaml(content, validator=TestSchema)
    assert [e["position"] for e in error_messages] == [p1]
    assert [e["text"] for e in error_messages] == ["This field may not be blank."]

# Generated at 2022-06-14 14:58:19.976615
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = typing.Dict[str, typing.Optional[typing.Union[str, int]]]
    validator = Schema({"name": str, "age": int})
    yaml_input = """name: John
age: 21
"""

    # Handle success case.
    value, messages = validate_yaml(content=yaml_input, validator=validator)
    assert value == {"name": "John", "age": 21}
    assert len(messages) == 0

    # Handle error case.
    yaml_input = """age: 21
name: John
"""
    _, messages = validate_yaml(content=yaml_input, validator=validator)
    message = messages[0]
    assert isinstance(message, Message)
    assert message.text == "Value not in schema: 'age'."


# Generated at 2022-06-14 14:58:24.853756
# Unit test for function validate_yaml
def test_validate_yaml():
    SchemaWithDefaults = Schema.of({"name": str, "age": int, "is_puppy": bool})
    assert validate_yaml("is_puppy: true\nname: lucy", SchemaWithDefaults) == ({"name": "lucy", "age": None, "is_puppy": True}, [])


# Generated at 2022-06-14 14:58:32.620743
# Unit test for function validate_yaml
def test_validate_yaml():
    input_content = """
        # A single-line comment.
        title: Hello, World!
        author:
          first_name: Jan
          last_name: Smith
        tags:
        - Python
        - YAML
        """
    validator = Schema(
        title=str,
        author=Schema(
            first_name=str,
            last_name=str,
        ),
        tags=list,
    )

    value, error_messages = validate_yaml(input_content, validator)
    assert error_messages == []
    assert value == {
        "title": "Hello, World!",
        "author": {
            "first_name": "Jan",
            "last_name": "Smith",
        },
        "tags": ["Python", "YAML"],
    }



# Generated at 2022-06-14 14:58:41.344440
# Unit test for function validate_yaml
def test_validate_yaml():
    # check that validate_yaml actually validate YAML content
    content = "foo: bar"
    validator = Schema.from_fields({"foo": String()})
    try:
        validate_yaml(content=content, validator=validator)
    except ValidationError as ex:
        print(ex)
        raise

    # check that validate_yaml actually validate YAML content (parses)
    content = "foo: bar"
    validator = Schema.from_fields({"foo": Integer()})
    try:
        validate_yaml(content=content, validator=validator)
    except ValidationError as ex:
        print(ex)
        raise

    # check that validate_yaml actually validate YAML content
    content = "foo: 10"

# Generated at 2022-06-14 14:58:51.585713
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    a function to test the core functionality of
    validate_yaml
    """
    # class to be used later on
    class Y(Schema):
        a = String()
        b = String()
        c = Integer()

    assert isinstance(validate_yaml("name: Neha\nage: 20", Y), tuple)

    # a test to check if the function raises an exception
    # when a string is entered (here, the string entered
    # is not a valid YAML format)
    with pytest.raises(ParseError):
        validate_yaml("name: Neha, age: 20", Y)

# Generated at 2022-06-14 14:59:03.551204
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer, Field
    from typesystem.validators import Min, Max

    class MySchema(Schema):
        name = String(validators=[Max(5)])
        age = Integer(validators=[Min(18), Max(99)])

    field = Field(validators=[Max(10)])

    # OK
    token, messages = validate_yaml(b"{a: 1, b: 2, c: 3}", MySchema)
    assert token is not None
    assert not messages

    # Missing required field
    token, messages = validate_yaml(
        b"""
        foo: 1
        bar: 2
        baz: 3
        """,
        MySchema,
    )
    assert token is None
    assert messages

# Generated at 2022-06-14 14:59:14.551712
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String()
        age = Integer()

    content = "name: Pat\nage: 30"

    assert validate_yaml(content, Person()) == (
        {"name": "Pat", "age": 30},
        [],
    )

    content = "name: Pat\nage: 30\nheight: 175.8"

    assert validate_yaml(content, Person()) == (
        {"name": "Pat", "age": 30},
        [
            Message(
                text="Extra properties are not allowed ('height' was unexpected).",
                code="extra_properties",
                position=Position(line_no=3, column_no=0, char_index=len(content)),
            )
        ],
    )

    content = "name: Pat\nage: foo"

    assert validate

# Generated at 2022-06-14 14:59:16.344403
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml('name: "Jane"', {
        'name': 'string',
    })


# Generated at 2022-06-14 14:59:30.987484
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''  
    id: 1a
    username: 'james'
    is_admin: False
    '''  # noqa
    class SimpleUser(Schema):
        id = fields.UUID(format='hex_verbose')
        username = fields.String(min_length=3, max_length=32)
        is_admin = fields.Boolean()

    # Test that it parses the content correctly
    value, error_messages = validate_yaml(content, SimpleUser)
    assert value.id == "1a"
    assert value.username == "james"
    assert value.is_admin == False
    assert error_messages == Message([])

    # Test that it raises ParseError if there is no content

# Generated at 2022-06-14 14:59:34.720281
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    yaml_str = """
        - 1
        - 2
        - 4
        - 8
    """
    errors = validate_yaml(yaml_str, typing.List[int])
    assert isinstance(errors, typing.List)
    assert len(errors) == 0



# Generated at 2022-06-14 14:59:46.750770
# Unit test for function validate_yaml
def test_validate_yaml():
    valid_json_string = '''
    user:
      name: John Doe
      age: 43
      email: false
      address:
        city: Melbourne
        country: Australia
    '''

    validator = Schema(
        {
            "user": {
                "name": "string",
                "age": "number",
                "address": {
                    "city": "string",
                    "country": "string"
                }
            }
        }
    )

    result = validate_yaml(valid_json_string, validator)

    assert (result[0] == {'user': {
        'name': 'John Doe',
        'age': 43,
        'address': {
            'city': 'Melbourne',
            'country': 'Australia'
        }
    }})
    assert result[1]

# Generated at 2022-06-14 14:59:58.646714
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    from typesystem.schemas import Schema
    from typesystem.fields import fields

    class YAMLSchema(Schema):
        name = fields.String(description="Name of the person.")

    content = "name: hello world\n"
    try:
        value, error_messages = validate_yaml(content, YAMLSchema)
    except ParseError as exc:
        # If there is a parse error, then we could not extract the position
        # of the error.
        error_messages = [exc]
        value = ""


# Generated at 2022-06-14 15:00:09.946105
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        pass

    assert validate_yaml(b"{}", TestSchema) == ({}, [])

    # Test parse error
    try:
        validate_yaml(b"invalid", TestSchema)
        assert False, "invalid YAML did not raise an exception"
    except ParseError as exc:
        assert exc.text == "mapping values are not allowed here."
        assert exc.position.line_no == 1
        assert exc.position.column_no == 1

    # Test validation error

# Generated at 2022-06-14 15:00:18.895123
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''
validation:
 - Valid URL
 - Valid URL
 - Invalid url

invalid_url:
 - Something else
 - This too
'''
    schema = type('MySchema', (Schema,), {'validation': [url()]})
    value, errors = validate_yaml(content, validator=schema)
    assert len(errors) == 1
    assert errors[0].get('type') == ValidationError
    assert errors[0].get('message') == 'Not a valid URL: Invalid url'

    content = '''
validation:
 - Valid URL
invalid_url:
 - Something else
'''
    value, errors = validate_yaml(content, validator=schema)
    assert len(errors) == 0

# Generated at 2022-06-14 15:00:27.822924
# Unit test for function validate_yaml
def test_validate_yaml():
    class SimpleSchema(Schema):
        f1 = Integer()
        f2 = String()
        f3 = Boolean()

    schema = SimpleSchema()

    assert validate_yaml(
        """
        f1: 1
        f2: foo
        f3: true
        """,
        schema,
    ) == (
        {
            "f1": 1,
            "f2": "foo",
            "f3": True,
        },
        [],
    )

    # Try to load an integer for f2.

# Generated at 2022-06-14 15:00:35.685667
# Unit test for function validate_yaml
def test_validate_yaml():
    token = tokenize_yaml("int: 10.0")
    assert isinstance(token, DictToken)
    
    field = Field(type="integer")
    value, errors = validate_yaml("int: 10.0", field)
    assert value == {"int": 10}, f"Value should be 10, but is {value}"
    assert errors == [], "No error messages should be returned"
    # TODO: Add test for error message
    
    
    
    
    
    

 


# Generated at 2022-06-14 15:00:47.087821
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Please install pyyaml and add the following to your .bashrc or .zshrc
    export PYTHONPATH="/Users/nmehta/Documents/gitrepo/typesystem:$PYTHONPATH"

    To run this test run the following in your terminal
    python -c 'import typesystem.tokenize.yaml;typesystem.tokenize.yaml.test_validate_yaml()'
    """

    from typesystem import Integer

    assert validate_yaml(b"", Integer()) == (None, [])
    assert validate_yaml(b"", Integer(required=True)) == (None, ["This field is required."])
    assert validate_yaml(b"123", Integer()) == (123, [])

# Generated at 2022-06-14 15:00:58.946306
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    name: a
    age: 15
    """
    validator = Schema({"name": str, "age": int})
    value, errors = validate_yaml(content, validator)

    assert value == {"name": "a", "age": 15}
    assert not errors

    content = """
    name: a
    color: orange
    """
    validator = Schema({"name": str, "age": int})
    value, errors = validate_yaml(content, validator)

    assert value == {"name": "a", "color": "orange"}
    assert len(errors) == 1
    assert isinstance(errors[0], ValidationError)
    assert errors[0].position == Position(
        line_no=3, column_no=6, char_index=18
    )
   

# Generated at 2022-06-14 15:01:10.784724
# Unit test for function validate_yaml
def test_validate_yaml():
    pass
    # content = '''
    #     name: Bob
    #     age: 35
    #     int_list:
    #       - 1
    #       - 2
    #       - 3
    # '''
    #
    #
    # class User(Schema):
    #     name = String(min_length=3, max_length=10)
    #     age = Integer()
    #     int_list = List(Integer())
    #
    #
    # value, errors = validate_yaml(content, User)
    # assert value["name"] == "Bob"
    # assert value["age"] == 35
    # assert value["int_list"] == [1, 2, 3]
    # assert not errors



# Generated at 2022-06-14 15:01:20.772340
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, Boolean, Number, String

    class SchemaWithYaml(Schema):
        name = String()
        age = Number()
        active = Boolean()

    # test case: when yaml is valid, the error message is None
    yaml = "name: foo\nage: 20\nactive: yes"
    assert validate_yaml(yaml, SchemaWithYaml)[1] is None

    # test case: when yaml is invalid, the error message is not None
    yaml = "name: foo\nage: 20\nactive: abc"
    assert validate_yaml(yaml, SchemaWithYaml)[1] is not None
    assert validate_yaml(yaml, SchemaWithYaml)[1].code == "invalid_type"

# Generated at 2022-06-14 15:01:32.614384
# Unit test for function validate_yaml
def test_validate_yaml():
  content1 = '''
  test:
    a: 1
    b: 2
    c: 3
    d: 4
    e: 5
    f: 6
    g: 7
  '''
  content2 = '''
  test:
    a: 1
    b: 2
    c: 3
    d: 4
    e: 5
    f: 6
    g: 7
    h: 8
    i: 9
    j: 10
    k: 11
    l: 12
  '''

# Generated at 2022-06-14 15:01:42.106529
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(type="object")
    content = "\n".join(["string key: value", "int key: 123"])
    value, error_messages = validate_yaml(content, validator)
    expected_value = {"string key": "value", "int key": 123}
    assert value == expected_value
    assert not error_messages

    # Detects wrong content
    content = "123"
    value, error_messages = validate_yaml(content, validator)
    assert value is None
    assert len(error_messages) == 1
    assert error_messages[0].text == "No content."



# Generated at 2022-06-14 15:01:46.089877
# Unit test for function validate_yaml
def test_validate_yaml():
    def test_validate_yaml():
        content = "key_b: 'value_b'"
        result = validate_yaml(content, 
                               {
            "key_a": "str",
            "key_b": "str",
        })
        print(result)

    test_validate_yaml()

# Unit Test for function tokenize_yaml

# Generated at 2022-06-14 15:01:56.690297
# Unit test for function validate_yaml
def test_validate_yaml():
    pass
#    source = "validate_yaml"
#    # must get error messages
#    (value, error_messages) = validate_yaml('name: BadName', StringField(max_length=3))
#    assert len(error_messages)==1
#    assert str(error_messages[0])=="name: 5:8"  # get the error position
#    # must get value if successful
#    (value, error_messages) = validate_yaml('name: GoodName', StringField(max_length=10))
#    assert value=='GoodName'
#    # must get error messages
#    (value, error_messages) = validate_yaml('[ 123, 456 ]', ArrayField(items=IntegerField(maximum=100)))
#    assert len(error_messages)==

# Generated at 2022-06-14 15:02:01.604593
# Unit test for function validate_yaml
def test_validate_yaml():
    data = """
        name: foo
        age: bar
    """
    from typesystem import String

    field = String(name="name")
    value, error = validate_yaml(data, field)
    assert value == "foo"
    assert error["name"][0].message == "Must be a string."



# Generated at 2022-06-14 15:02:11.699284
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, String
    from typesystem.schemas import Schema

    class UserSchema(Schema):

        id = Integer(title="ID of the user")
        name = String(max_length=20, title="Name of user")

    # Happy path
    yaml = """
    id: 1
    name: John Doe
    """
    value, _ = validate_yaml(yaml, UserSchema)
    assert value == {"id": 1, "name": "John Doe"}

    # Invalid data type
    yaml = """
    id: "not an int"
    name: John Doe
    """
    _, messages = validate_yaml(yaml, UserSchema)
    errors = messages["data"]["id"]["data"]["errors"]

# Generated at 2022-06-14 15:02:17.737358
# Unit test for function validate_yaml
def test_validate_yaml():
  assert validate_yaml(
        content='- name: mike age: 21 height: 5.8',
        validator=Schema(
            properties={
                "name": String(),
                "age": Integer(),
                "height": Decimal(),
            }
        )
    ) == [{'age': 21, 'height': 5.8, 'name': 'mike'}, None]

# Generated at 2022-06-14 15:02:28.630791
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = fields.String(description="The user's name")
        age = fields.Integer(description="The user's age")
        birthday = fields.String(description="The user's birthday")

    content = """
    name: Foo
    age: "18" 
    birthday: "11/1/2000"
    """

    value, messages = validate_yaml(content, Person)

    expected_messages = [
        Message(
            text="Expected int, but got str.",
            code="invalid_type",
            field="age",
            position=Position(line_no=2, column_no=9, char_index=12),
        )
    ]

    assert messages == expected_messages

# Generated at 2022-06-14 15:02:43.194642
# Unit test for function validate_yaml
def test_validate_yaml():
    @dataclass
    class Pet:
        name: str

    @dataclass
    class Person:
        name: str
        age: int
        pets: typing.List[Pet]

    class PersonSchema(Schema):
        name = "Person Schema"
        fields = [
            Field(name="name", type="string"),
            Field(name="age", type="integer"),
            Field(name="pets", type="array", items=Field(name="pet", type="object", properties=[
                Field(name="name", type="string")
            ])),
        ]

    content = textwrap.dedent(
        """\
        name: Bob
        age: 45
        pets:
          - name: Rover
          - name: Fluffy
        """
    )

# Generated at 2022-06-14 15:02:47.174455
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.types import String, Number

    class TestSchema(Schema):
        title = String(min_length=10)
        year = Number(minimum=1900, maximum=2100)

    content = """
    title: Hello World
    year: 2020
    """
    value, errors = validate_yaml(content, TestSchema)

    assert value == {"title": "Hello World", "year": 2020}
    assert not errors



# Generated at 2022-06-14 15:02:57.690592
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Array

    class Person(Schema):
        name = String()

    class People(Schema):
        people = Array(items=Person())

    class PeopleWithAddress(Schema):
        people = Array(items=Person(fields={"address": String()}))

    class PeopleWithAge(Schema):
        people = Array(
            items=Person(fields={"age": Integer(minimum=0, maximum=150)}),
        )

    fname = 'fixtures/yaml/inputs'
    with open(fname, 'r') as f:
        inputs = yaml.load(f, Loader=yaml.FullLoader)

    for name, v in inputs.items():
        for vv in v:
            result, error_mess

# Generated at 2022-06-14 15:03:03.226432
# Unit test for function validate_yaml
def test_validate_yaml():
    class ArticleSchema(Schema):
        title = String()  #type: ignore
        content = String()  #type: ignore
        author = String()  #type: ignore
        status = String(choices=["published", "draft", "deleted"])  #type: ignore

    content = """
    title: Some article
    content: Some content
    author: Some author
    status: invalid
    """

    valid, errors = validate_yaml(content, ArticleSchema)
    for error in errors:
        print(error["text"] + error["position"])



# Generated at 2022-06-14 15:03:08.749235
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """\
    id: 123
    first_name: Joe
    last_name: Blogs
    email: joeblogs@example.com
    """
    UserSchema = typing.cast(
        typing.Type[Schema],
        typing.cast(
            Schema,
            Schema.define(
                fields={
                    "id": Field(required=True),
                    "first_name": Field(required=True, type=str),
                    "last_name": Field(required=True, type=str),
                    "email": Field(required=True, type=str),
                }
            ),
        ),
    )
    value, errors = validate_yaml(content=content, validator=UserSchema)
    assert errors == []

# Generated at 2022-06-14 15:03:18.269108
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = (
        "key1: 'value1'\n"
        "key2:\n"
        "  - item1\n"
        "  - item2\n"
        "key3: 123\n"
    )
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.content == content
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.value == {"key1": "value1", "key2": ["item1", "item2"], "key3": 123}



# Generated at 2022-06-14 15:03:27.262810
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # testing for yaml file
    test_string = """
    training_data:
        #
        # Sentences which will not be used in training
        #
        skip:
            - Hello! This is a sample. We will not use this in the training.
            - This is a another example, we will not use this in the training.
        #
        # Sentences which will be used in training
        #
        use:
            - Hello! This is a sample. We will use this in the training.
            - This is a another example, we will use this in the training.
    """
    # test if the tokenize_yaml function return a string
    assert isinstance(tokenize_yaml(test_string), str)


# Generated at 2022-06-14 15:03:37.676631
# Unit test for function validate_yaml
def test_validate_yaml():
    assert Field is not None
    assert validate_with_positions is not None
    assert validate_yaml is not None

    schema = Field(name="my_field", type="string")

    assert validate_yaml(content="", validator=schema) == ({}, [])

    (value, messages) = validate_yaml(content="foo: bar", validator=schema)

    assert value == {}
    assert messages == [
        Message(
            text="Expected a 'string' value.",
            code="invalid_type",
            line_no=1,
            column_no=1,
            char_index=0,
        )
    ]

    (value, messages) = validate_yaml(content="[1, 2, 3]", validator=schema)

    assert value == [1, 2, 3]

# Generated at 2022-06-14 15:03:48.764144
# Unit test for function validate_yaml
def test_validate_yaml():
    ###Test with an empty string
    content = ""
    validator = "string"
    with pytest.raises(ParseError):
        value, errors = validate_yaml(content,validator)

    ###Test with a string with an integer value
    content = "42"
    validator = "string"
    with pytest.raises(ValidationError):
        value, errors = validate_yaml(content,validator)

    ###Test with a string with a list value
    content = "['apple']"
    validator = "string"
    with pytest.raises(ValidationError):
        value, errors = validate_yaml(content,validator)

    ###Test with a string with a dictionary value
    content = "{'hello': 'world'}"
    validator = "string"

# Generated at 2022-06-14 15:03:57.482980
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("") == ""
    assert tokenize_yaml("123") == 123
    assert tokenize_yaml("null") is None
    assert tokenize_yaml("true") is True
    assert tokenize_yaml("false") is False
    assert tokenize_yaml("[]") == []
    assert tokenize_yaml("{}") == {}
    assert tokenize_yaml('["a"]') == ["a"]
    assert tokenize_yaml('{"a":"b"}') == {"a": "b"}
    assert tokenize_yaml('"a"') == "a"
    assert tokenize_yaml("'a'") == "a"
    assert tokenize_yaml('"a" "b"') == ["a", "b"]

# Generated at 2022-06-14 15:04:05.957917
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class MySchema(Schema):
        name = String()

    content = """
        name: Foo Bar
    """
    _, errors = validate_yaml(content=content, validator=MySchema)
    assert len(errors) == 0

    _, errors = validate_yaml(content="", validator=MySchema)
    assert len(errors) == 1
    assert errors[0].code == "no_content"

    _, errors = validate_yaml(content="{", validator=MySchema)
    assert len(errors) == 1
    assert errors[0].code == "parse_error"

# Generated at 2022-06-14 15:04:13.890605
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String(required=True, pattern="^[A-Z][a-z]*$")
        age = Integer(minimum=0)
        favorite_color = String(valid_choices=["chartreuse", "blue", "plum"])
        favorite_pizza_toppings = String(
            valid_choices=["pepperoni", "sausage", "mushrooms", "pineapple"]
        )

    content = textwrap.dedent(
        """
        name: Pete
        age: Not an integer!
        favorite_color: not a valid choice
        favorite_pizza_toppings: []
        """
    )

    data, errors = validate_yaml(content, validator=Person)

# Generated at 2022-06-14 15:04:24.310671
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Schema(
        type="object",
        properties={
            "name": {"type": "string", "minLength": 1},
            "age": {"type": "integer", "minimum": 0},
        },
        additionalProperties=False,
    )

    # No errors
    value, errors = validate_yaml("name: John\nage: 30", validator)
    assert value == {"name": "John", "age": 30}
    assert errors == []

    # Parse error
    value, errors = validate_yaml("name: John\nage: thirty", validator)
    assert value == {}

# Generated at 2022-06-14 15:04:34.265106
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema({"name": fields.String, "age": fields.Int})
    content = (
        """\
name: fnord
age: 30
"""
    )
    value, error_messages = validate_yaml(content, schema)
    assert value == {"name": "fnord", "age": 30}
    assert error_messages == []

    content = (
        """\
name: fnord
age: thirty
"""
    )
    value, error_messages = validate_yaml(content, schema)
    assert value == {"name": "fnord"}
    assert error_messages == [Message(text="Ensure this value is not null.", code="null")]

    content = (
        """\
name: fnord
"""
    )

# Generated at 2022-06-14 15:04:42.466670
# Unit test for function validate_yaml
def test_validate_yaml():
    print("test_validate_yaml begin")
    # validate_yaml(content: str, validator: Field)
    #content = "{test:test string}"
    #content = "test:test string"
    content = """
test:test
string
    """
    content_bytes = bytes(content,"utf-8")
    #validator = ""
    validator = Field(type="string")
    ret = validate_yaml(content = content_bytes, validator = validator)
    print(ret)
    print("test_validate_yaml end")


test_validate_yaml()

# Generated at 2022-06-14 15:04:46.590197
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = fields.String()
        age = fields.Integer()

    content = "name: Bob\nage: 28\n"
    body, messages = validate_yaml(content, PersonSchema)
    assert body == {"name": "Bob", "age": 28}
    assert len(messages) == 0

# Generated at 2022-06-14 15:04:57.095932
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        name = fields.StringField()

    # valid yaml
    content = "name: John"
    value, errors = validate_yaml(content, UserSchema)
    assert value == {"name": "John"}
    assert errors == []

    # invalid yaml
    content = "name: John\n"
    value, errors = validate_yaml(content, UserSchema)
    assert errors == [Message(code="parse_error", text="could not find expected ':'", position=Position(line_no=2, column_no=0, char_index=9))]

    # valid yaml but invalid content
    content = "name: John\nage: 5"
    value, errors = validate_yaml(content, UserSchema)

# Generated at 2022-06-14 15:05:03.411070
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer
    from typesystem.fields import String

    # Validate yaml string with a integer field
    value, errors = validate_yaml("123", Integer())
    assert errors == []
    assert value == 123

    # Validate yaml string with a integer field that has an error
    value, errors = validate_yaml("123a", Integer())
    assert errors == [
        Message(
            field_name="",
            text="This value must be an integer.",
            code="integer",
            position=Position(line_no=1, column_no=1, char_index=0),
        )
    ]
    assert value is None

    # Validate yaml string with a string field
    value, errors = validate_yaml("test", String())
    assert errors == []
    assert value == "test"

   

# Generated at 2022-06-14 15:05:10.704426
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('') is None
    assert tokenize_yaml('None') is None
    assert tokenize_yaml('true') is True
    assert tokenize_yaml('false') is False
    assert tokenize_yaml('1') == 1
    assert tokenize_yaml('0') == 0
    assert tokenize_yaml('0.0') == 0.0
    assert tokenize_yaml('0.1') == 0.1
    assert tokenize_yaml('"Hello, world"') == "Hello, world"
    assert tokenize_yaml('"Hello, world\nWith multiple lines"') == "Hello, world\nWith multiple lines"
    assert tokenize_yaml('[1, 2, 3]') == [1, 2, 3]

# Generated at 2022-06-14 15:05:22.859721
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""
        foo:
            - baz
            - baz: baz
            - baz:
                - baz
                - baz: baz
                - baz:
                    - baz
            - baz
    """)
    assert token == {
        "foo": [
            "baz",
            {"baz": "baz"},
            {"baz": ["baz", {"baz": "baz"}, {"baz": ["baz"]}]},
            "baz",
        ]
    }

    # Test that scalar tokens are correctly handled
    token = tokenize_yaml("1")
    assert token == 1

    # Test that position arguments are correctly handled

# Generated at 2022-06-14 15:05:37.132261
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, Object, String
    from typesystem.schemas import Schema
    from typesystem.tokenize.positional_validation import TokenError

    class BookSchema(Schema):
        title = String(max_length=200)
        year = Integer()
        author = String(max_length=200)

    value, errors = validate_yaml(
        """
        title: Asimov, Isaac - Foundation
        author: Asimov, Isaac
        year: 1951
        """,
        BookSchema,
    )

    assert errors[0].code == "required"
    assert errors[0].position.line_no == 4
    assert errors[0].position.column_no == 1


# Generated at 2022-06-14 15:05:46.959639
# Unit test for function validate_yaml
def test_validate_yaml():
    print("Testing validate_yaml function...")
    from typesystem import String, Integer, Boolean, Float
    from typesystem.schemas import Schema
    from typesystem import fields

    class PersonSchema(Schema):
        name = String(min_length=2)
        age = Integer(minimum=0)
        height = Float(minimum=0.0)
        is_married = Boolean()
        siblings = fields.ArrayField(Integer(), min_items=0)

    class Meta:
        schema = PersonSchema


# Generated at 2022-06-14 15:05:53.242613
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    name: Isabella
    age: 12
    """
    class Person(Schema):
        name = String()
        age = Integer()

    value, errors = validate_yaml(content, Person)
    assert isinstance(value, dict)
    assert len(value) == 2
    assert value.get('name') == "Isabella"
    assert value.get('age') == 12



# Generated at 2022-06-14 15:05:57.639187
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''
    type: object
    properties:
        name:
            type: string
        favorite_number:
            type: integer
        friends:
            type: array
            items:
                type: object
                properties:
                    name:
                        type: string
        favorite_foods:
            type: array
            items:
                type: string
    '''
    Person = Schema(schema=content)
    (value, messages) = validate_yaml(
        content='name: "James"', validator=Person)
    assert value == dict(name="James")
    assert len(messages) == 3
    message_texts = [message.text for message in messages]
    assert "Required property friend is missing." in message_texts
    assert "Required property favorite_foods is missing." in message_text

# Generated at 2022-06-14 15:06:04.561567
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    from azure_devtools.scenario_tests.exceptions import AzureTestError
    from azure.cli.core.util import CLIError
    import json


# Generated at 2022-06-14 15:06:15.178814
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field.any()
    value, error = validate_yaml("", validator)
    assert value == None
    assert error.code == "no_content"
    value, error = validate_yaml(" ", validator)
    assert value == None
    assert error.code == "parse_error"
    value, error = validate_yaml("{}", validator)
    assert value == {}
    assert error == None
    value, error = validate_yaml("{", validator)
    assert value == None
    assert error.code == "parse_error"
    value, error = validate_yaml("[", validator)
    assert value == None
    assert error.code == "parse_error"
    value, error = validate_yaml("#", validator)
    assert value == None
    assert error.code