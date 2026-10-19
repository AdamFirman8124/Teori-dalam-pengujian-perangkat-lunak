

# Generated at 2022-06-14 14:56:26.149913
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        field1 = Field(type="integer")
        field2 = Field(type="string")

    TestSchema(fields=["field1", "field2"])

    s = "field1: 1\nfield2: '2'"
    value, error_messages = validate_yaml(s, TestSchema)

    assert value == {"field1": 1, "field2": "2"}
    assert isinstance(error_messages, list)
    assert len(error_messages) == 0



# Generated at 2022-06-14 14:56:32.648434
# Unit test for function validate_yaml
def test_validate_yaml():

    schema = Schema("testSchema", [("testField", Field(str))])

    assert validate_yaml("testField: 123\n", schema) == (None, [
      Message("testField is not of type 'str'.",
              path=["testField"],
              context="testSchema",
              code="invalid",
              position=Position(1, 11, 10)),
      Message("Unrecognised field.",
              path=[],
              context="testSchema",
              code="unknown_field",
              position=Position(1, 10, 9)),
    ])

# Generated at 2022-06-14 14:56:44.305048
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    -
    - 1
    - 'some text'
    - true
    - false
    - null
    """
    token = tokenize_yaml(content)
    assert isinstance(token, ListToken)
    assert isinstance(token.value[0], ListToken)
    assert isinstance(token.value[0].value[0], ScalarToken)
    assert isinstance(token.value[0].value[1], ScalarToken)
    assert isinstance(token.value[0].value[2], ScalarToken)
    assert isinstance(token.value[0].value[3], ScalarToken)
    assert isinstance(token.value[0].value[4], ScalarToken)
    assert isinstance(token.value[0].value[5], ScalarToken)

# Generated at 2022-06-14 14:56:48.150547
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = ValidateYamlSchema()
    mydoc = 'field1: "Hello, World!"\nfield2:\n- "hello, 1"\n- "hello, 2"'
    result = validate_yaml(mydoc, schema)
    assert isinstance(result, dict)

# Generated at 2022-06-14 14:56:57.490913
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b'{"report_date": "2019-07-01T00:00:00.000", "users": [{"first_name": "Joe", "last_name": "Doe", "status": "active", "email": "joe.doe@gmail.com"}, {"first_name": "Jane", "last_name": "Doe", "status": "inactive", "email": "jane.doe@gmail.com"}]}'
    validator = Schema(
        {
            "report_date": "datetime",
            "users": "list",
            "users.*.first_name": "string",
            "users.*.last_name": "string",
            "users.*.status": "string",
            "users.*.email": "string",
        },
    )
    value, errors = validate_y

# Generated at 2022-06-14 14:57:06.566091
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class Poll(Schema):
        title = String()

    try:
        Poll.validate_yaml(content=b"")
    except ParseError as exc:
        assert exc.text == "No content."
        assert exc.position.line_no == 1
        assert exc.position.char_index == 0
        assert exc.position.column_no == 1
        assert exc.code == "no_content"

    with pytest.raises(ValidationError) as exc_info:
        Poll.validate_yaml(content=b'{"title": 123}')
    assert "Expected a string." in exc_info.value.message
    assert exc_info.value.position.line_no == 1

# Generated at 2022-06-14 14:57:10.080020
# Unit test for function validate_yaml
def test_validate_yaml():
    class A(Schema):
        name = String()

    content = """
    - name: a
    - name: b
    """

    errors = validate_yaml(content, A())
    assert errors == []



# Generated at 2022-06-14 14:57:18.179365
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(type="list", items={"type": "string"})

    value, error_messages = validate_yaml(
        validator=validator, content=b"- 1\n- 2\n- 3"
    )
    assert value == ["1", "2", "3"]
    assert error_messages == []

    value, error_messages = validate_yaml(
        validator=validator, content=b"1"
    )
    assert value is None
    assert len(error_messages) == 1
    assert error_messages[0].code == "invalid-type"
    assert error_messages[0].position.char_index == 0
    assert error_messages[0].position.line_no == 1
    assert error_messages[0].position.column_no == 1

# Generated at 2022-06-14 14:57:29.033859
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    from typesystem import boolean, integer, string, number, object_, array

    schema = object_({
        'name': string(),
        'age': integer(),
        'is_alive': boolean(),
    })

    # Test with a YAML string
    value, errors = validate_yaml(
        '''
        name: John
        age: 25
        is_alive: true
        ''',
        schema
    )
    assert errors == []
    assert value == {
        'name': 'John',
        'age': 25,
        'is_alive': True,
    }

    # Test with a YAML bytestring

# Generated at 2022-06-14 14:57:40.482694
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """test tokenize_yaml"""
    # test simple string type
    yaml_data = "name: John"
    yaml_token = tokenize_yaml(yaml_data)
    assert yaml_token.value == {"name": "John"}
    assert yaml_token.start == 0
    assert yaml_token.end == 11
    assert yaml_token.content == yaml_data
    assert yaml_token.type == "dict"
    assert yaml_token.get_children() == [
        ScalarToken("John", start=7, content=yaml_data, end=11)
    ]

    # test int string type
    yaml_data = "id: 1"
    yaml_token = tokenize_yaml(yaml_data)

# Generated at 2022-06-14 14:57:55.893650
# Unit test for function validate_yaml
def test_validate_yaml():
    from string import ascii_letters, digits
    from random import choice, randint
    from typesystem import String, Integer
    from typesystem.schemas import Schema
    from typesystem.fields import Field

    for i in range(100):
        # Generate random YAML content
        content = "".join(choice(ascii_letters + digits) for _ in range(randint(1, 10)))
        # print("Random content generated: {}".format(content))
        # Verify content is successfully loaded as a string
        assert isinstance(content, str)
        # Verify value matches what we sent
        assert validate_yaml(content, String())[0] == content
        # Verify value matches what we sent when 
        assert validate_yaml(content, Integer())[0] == int(content)
        # Verify value is wrapped

# Generated at 2022-06-14 14:58:07.613468
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("string: foo") == DictToken({"string": "foo"}, 0, 12, content="string: foo")
    assert tokenize_yaml("- foo") == ListToken(["foo"], 0, 4, content="- foo")
    assert tokenize_yaml("123") == ScalarToken(123, 0, 2, content="123")
    assert tokenize_yaml("- foo\n- bar") == ListToken(["foo", "bar"], 0, 10, "- foo\n- bar")
    assert tokenize_yaml("- foo\n- bar\n  - baz") == ListToken(["foo", ["bar", "baz"]], 0, 19, "- foo\n- bar\n  - baz")
    assert tokenize_yaml("a: 1\nb: 2\nc: 3")

# Generated at 2022-06-14 14:58:10.281640
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    schema = {"foo": {"type": "string"}, "bar": {"type": "integer"}}
    token = tokenize_yaml(schema)
    assert isinstance(token, DictToken)



# Generated at 2022-06-14 14:58:21.442243
# Unit test for function validate_yaml
def test_validate_yaml():

    class PetSchema(Schema):
        name = CharField(max_length=100)
        age = IntField(minimum=0, maximum=30)

    class PersonSchema(Schema):
        name = CharField(max_length=100)
        pets = ListField(items=PetSchema)

    yaml_str = """
    name: Alice
    pets:
      - name: Kitty
        age: 5
      - name: Brick
        age: 10
    """
    value, messages = validate_yaml(
        content=yaml_str,
        validator=PersonSchema,

    )
    assert messages == []

    class PersonSchema(Schema):
        name = CharField(max_length=100)
        age = IntField(minimum=0, maximum=30)


# Generated at 2022-06-14 14:58:29.034305
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String, Array
    from typesystem.schemas import Schema
    from typesystem.errors import (
        ParseError,
        ValidationError,
        ErrorMessageList,
    )

    class TestSchema(Schema):
        # TestSchema defines two fields: name and children
        name = String()
        children = Array(items=String())

    # Test content is valid and returns the expected value.
    content = "name: Test\nchildren:\n  - Test1\n  - Test2"
    value, errors = validate_yaml(content, TestSchema)
    assert value == {
        "name": "Test",
        "children": ["Test1", "Test2"],
    }
    assert errors == []


# Generated at 2022-06-14 14:58:40.881296
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    yaml_content = '''
    - "value1"
    -
        key1: "value1"
        key2: "value2"
    '''
    tokens = tokenize_yaml(yaml_content)
    assert isinstance(tokens, ListToken)
    assert len(tokens) == 2

    assert isinstance(tokens[0], ScalarToken)
    assert tokens[0].start_position.char_index == 9
    assert tokens[0].end_position.char_index == 15

    tokens = tokens[1]
    assert isinstance(tokens, DictToken)
    assert len(tokens) == 2

    assert isinstance(tokens["key1"], ScalarToken)
    assert tokens["key1"].start_position.char_index == 26
    assert tokens

# Generated at 2022-06-14 14:58:50.137548
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    list:
    - 1
    - 2
    - 3
    """
    validator = typing.List[int]
    value, errors = validate_yaml(content=content, validator=validator)
    print(errors)
    assert len(errors) == 2
    assert errors[0].code == 'type_mismatch'
    assert errors[0].position.line_no == 2
    assert errors[1].code == 'type_mismatch'
    assert errors[1].position.line_no == 2



# Generated at 2022-06-14 14:59:01.863883
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(b'["foo", "bar"]', List(items=String())) == (['foo','bar'], [])
    assert validate_yaml(b'["foo", 42]', List(items=String())) == (None, [Message(code='type',
                                                                                  message=f'Invalid List type, expected List[String]',
                                                                                  path=[1],
                                                                                  position=Position(char_index=12, column_no=4, line_no=1))])

# Generated at 2022-06-14 14:59:12.090172
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Unit test for function tokenize_yaml
    """
    print()
    print("*"*30)
    print()
    print("Unit test for function tokenize_yaml")
    print()
    print("*"*30)
    print()

    # Unit test on function tokenize_yaml
    test_yaml = """
    test_key: value
    test_key2:
      foo: bar
      bar: foo
    test_key3:
    - 1
    - 2
    - 3
    """

    token = tokenize_yaml(test_yaml)
    print(token.value)
    print()


# Generated at 2022-06-14 14:59:22.135319
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Tests for tokenize_yaml function
    """
    assert tokenize_yaml("") is None
    assert isinstance(tokenize_yaml("test"), ScalarToken) == True
    assert isinstance(tokenize_yaml("{}"), DictToken) == True
    assert isinstance(tokenize_yaml("[]"), ListToken) == True
    assert tokenize_yaml("").content == ""
    assert isinstance(tokenize_yaml("test"), ScalarToken) == True
    assert isinstance(tokenize_yaml("{}"), DictToken) == True
    assert isinstance(tokenize_yaml("[]"), ListToken) == True
    assert isinstance(tokenize_yaml("[1, 2, 3]"), ListToken) == True

# Generated at 2022-06-14 14:59:33.044082
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    name: YAML
    age: 23
    """
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert isinstance(token.value["name"], ScalarToken)
    assert isinstance(token.value["age"], ScalarToken)



# Generated at 2022-06-14 14:59:44.901868
# Unit test for function validate_yaml
def test_validate_yaml():
    class S(Schema):
        a = "string"
        b = "string"

    v, errs = validate_yaml(
        content="a: 1\nb:\n   1\n", validator=S
    )
    assert errs == [
        ValidationError(
            text="Value must be a string.",
            code="invalid",
            pointer="/a",
            position=Position(char_index=1, line_no=1, column_no=2),
        ),
        Message(
            text="Field 'b' is required.",
            code="required",
            pointer="/b",
            position=Position(char_index=1, line_no=2, column_no=2),
        ),
    ]

# Generated at 2022-06-14 14:59:48.916074
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml(content='''
    {
        "empty-line": ""
    }
    ''')

    assert isinstance(token, DictToken)
    assert token.value["empty-line"] == ""
    assert token.start == 2
    assert token.end == 26



# Generated at 2022-06-14 14:59:51.726687
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    tokenize_yaml("{'a':2}")



# Generated at 2022-06-14 14:59:57.220292
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '{ "eins": 1}'
    validator = Schema.from_dict({"eins": int})
    # The second element of the returned tuple can be either None or
    # a list of error messages.
    result = validate_yaml(content, validator)
    assert result[1] == None
    assert result[0] == {"eins": 1}


# Generated at 2022-06-14 15:00:02.904573
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    yaml_string = """
    # example schema
    url: https://www.example.com
    name: example.com
    description: >
      A website example.com.
    """
    expected = {
        "url": "https://www.example.com",
        "name": "example.com",
        "description": "A website example.com.",
    }
    actual = tokenize_yaml(yaml_string)
    assert expected == actual.value

# Generated at 2022-06-14 15:00:14.688539
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("true") == True
    assert tokenize_yaml("[1,2,3]") == [1,2,3]

# Generated at 2022-06-14 15:00:21.486759
# Unit test for function validate_yaml
def test_validate_yaml():
    print("\nTesting function: validate_yaml")
    # TODO: Test with string values, not bytes.
    content = b'a: 1\n'
    validator = Schema({"a": "integer"})
    value, error_messages = validate_yaml(content, validator)

    print("value:\n", value)
    print("error messages:\n", error_messages)
    # TODO: Verify that we're getting the results we expect.

# Generated at 2022-06-14 15:00:29.514660
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String

    field = String()
    value, errors = validate_yaml(b'foo', field)

    assert value == "foo"
    assert errors == []

    value, errors = validate_yaml(b'foo\n', field)
    assert value == "foo"
    assert errors == []

    value, errors = validate_yaml(b'foo\nbar', field)
    assert value == "foo"
    assert len(errors) == 1
    assert errors[0].text == "Extra characters found."

    value, errors = validate_yaml(b'', field)
    assert value == ""
    assert len(errors) == 1
    assert errors[0].text == "No content."

    value, errors = validate_yaml(b'foo:-', field)
    assert value == "foo"

# Generated at 2022-06-14 15:00:39.756715
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml("", "") == ('No content.', [])
    assert validate_yaml(" \n \n", "") == ('No content.', [])

# Generated at 2022-06-14 15:00:50.394128
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    data = """
hello:
  - name: Bob
    age: 18
  - name: Steve
    age: 25
    """
    token = tokenize_yaml(data)
    assert token


# Generated at 2022-06-14 15:01:02.716453
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    t = tokenize_yaml("123")
    assert isinstance(t, ScalarToken)
    assert t.content == "123"
    assert t.start == 0
    assert t.end == 2
    t = tokenize_yaml("123")
    assert isinstance(t, ScalarToken)
    assert t.content == "123"
    assert t.start == 0
    assert t.end == 2
    t = tokenize_yaml("123.4")
    assert isinstance(t, ScalarToken)
    assert t.content == "123.4"
    assert t.start == 0
    assert t.end == 4
    t = tokenize_yaml("true")
    assert isinstance(t, ScalarToken)
    assert t.content == "true"
    assert t.start == 0
    assert t

# Generated at 2022-06-14 15:01:10.288646
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""
    a: 1
    b: [true, false]
    c: 3
    d: blah blah
    e: null
    """)
    assert len(token.mapping) == 5
    assert token.mapping["a"].value == 1
    assert token.mapping["b"].value == [True, False]
    assert token.mapping["c"].value == 3
    assert token.mapping["d"].value == "blah blah"
    assert token.mapping["e"].value is None


# Generated at 2022-06-14 15:01:20.577183
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer
    from typesystem.exceptions import ValidationError as typesystem_ValidationError
    class Person(Schema):
        name = String(max_length=256)
        phone_number = Integer()
    content = '''{
        name: John
        phone_number: "123"
    }'''
    try:
        Person.validate(content)
    except typesystem_ValidationError as e:
        assert e.code == "error"
        assert e.text == "phone_number must be an integer."
        assert e.position == Position(column_no=11, line_no=4, char_index=67)
    else:
        assert False, "Unexpected pass"

# Generated at 2022-06-14 15:01:26.893002
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('"abc"') == 'abc'
    assert tokenize_yaml('42') == 42
    assert tokenize_yaml('hi: "hello"') == {"hi": "hello"}
    assert tokenize_yaml('[1, 2, 3]') == [1, 2, 3]


# Generated at 2022-06-14 15:01:32.993469
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # make sure tokenize_yaml function is working
    try:
        assert yaml is not None, "'pyyaml' must be installed."
    except AssertionError:
        pytest.skip("pyyaml is not installed")
    with open('test.yml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    token = tokenize_yaml(data)
    assert token.value == data


# Generated at 2022-06-14 15:01:42.552976
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = typing.cast(
        typing.Type[Schema], typing.cast(typing.Any, Schema).build({"x": "integer"})
    )
    assert validate_yaml("x: 1", validator) == (
        {'x': 1},
        [],
    )

    assert validate_yaml("a: 1", validator) == (
        {'x': None},
        [
            Message(
                text="The following field(s) are required: x.",
                code="required",
                line_no=2,
                column_no=2,
                char_index=3,
            ),
        ],
    )

# Generated at 2022-06-14 15:01:46.413837
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """Testing tokenize_yaml"""
    content = "first_name: John\nlast_name: Smith"
    token = tokenize_yaml(content)
    assert token.value["first_name"].value == "John"
    assert token.value["last_name"].value == "Smith"
    assert token.value[0][0].value == "John"



# Generated at 2022-06-14 15:01:56.901953
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Test tokenize_yaml function
    """
    assert tokenize_yaml(u'{"a":12, "b":["foo", "bar"]}') == {
        "a": 12,
        "b": ["foo", "bar"],
    }
    assert tokenize_yaml(u'{"a":12, "b":["foo", "bar"]}') == {
        "a": 12,
        "b": ["foo", "bar"],
    }
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(u"a:12, b")
    assert str(exc_info.value) == (
        "No content: 'a:12, b'. "
        "Location: line 1, column 1, character 0"
    )



# Generated at 2022-06-14 15:02:08.415013
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "5"
    validator = int
    value, _ = validate_yaml(content=content, validator=validator)
    assert value == 5

    content = "true"
    validator = bool
    value, _ = validate_yaml(content=content, validator=validator)
    assert value is True

    content = "['test']"
    validator = [str]
    value, _ = validate_yaml(content=content, validator=validator)
    assert value[0] == "test"

    content = "{'test': 5}"
    validator = {"test": int}
    value, _ = validate_yaml(content=content, validator=validator)
    assert value["test"] == 5

    content = "true"
    validator = int

# Generated at 2022-06-14 15:02:24.276182
# Unit test for function validate_yaml
def test_validate_yaml():

    # Test passing a valid YAML string.
    data = b"""
name: hello
"""
    schema = Schema({"name": {"type": "string", "min_length": 3}})
    value, error_messages = validate_yaml(data, schema)
    assert value == {"name": "hello"}
    assert error_messages == []

    # Test passing an invalid YAML string.
    data = b"""
name: fo
"""
    schema = Schema({"name": {"type": "string", "min_length": 3}})
    value, error_messages = validate_yaml(data, schema)
    assert value == {"name": "fo"}
    assert error_messages == [
        Message("Value must be at least 3 characters long.", code="min_length",),
    ]

# Generated at 2022-06-14 15:02:28.564783
# Unit test for function validate_yaml
def test_validate_yaml():
    class Movie(Schema):
        title = Field(validators=[str])
        duration = Field(validators=[int])
        release_date = Field(validators=[str])

    content = """
    title: "The Matrix"
    duration: 136
    release_date: 1999-03-31
    """
    value, error_messages = validate_yaml(content, validator=Movie)
    assert value["title"] == "The Matrix"
    assert value["duration"] == 136
    assert value["release_date"] == "1999-03-31"
    assert len(error_messages) == 0

    content = """
    title: "The Matrix"
    release_date: 1999-03-31
    """
    value, error_messages = validate_yaml(content, validator=Movie)

# Generated at 2022-06-14 15:02:40.852132
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "a: a"
    field = Field(str)
    value, errors = validate_yaml(content, field)
    assert value == "a"
    assert errors == [
        Message("Value of incorrect type.", code="type_error", position=Position(column_no=1, line_no=1, char_index=0))
    ]

    content = "a: 1"
    field = Field(int)
    value, errors = validate_yaml(content, field)
    assert value == 1
    assert errors == []

    content = "a:\n  b: 1"
    field = Field(int)
    value, errors = validate_yaml(content, field)
    assert value == 1

# Generated at 2022-06-14 15:02:48.161168
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.types import String, Integer
    from typesystem.fields import Field
    from typesystem.schemas import Schema

    class MySchema(Schema):
        name = Field(type=String)
        age = Field(type=Integer)

    # Validate valid input fields
    content = """
      name: Alice
      age: 25
    """
    data, error_messages = validate_yaml(content, validator=MySchema)
    print(error_messages)
    assert not error_messages
    assert data == {"name": "Alice", "age": 25}

    # Validate invalid input fields
    content = """
      name:
      age: 
    """
    data, error_messages = validate_yaml(content, validator=MySchema)

# Generated at 2022-06-14 15:02:58.568959
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    test_validate_yaml is a unit-test for validate_yaml.
    """
    import io
    import unittest
    import typesystem

    # define schema for unit test
    class Person(typesystem.Schema):
        """
        Define a Person class for unit test
        """
        name = typesystem.String(max_length=100)
        age = typesystem.Integer(minimum=0)
        height = typesystem.Float(maximum=200)

    # create test content
    person = {
        'name': 'John',
        'age': -1,
        'height': 201
    }
    content = io.StringIO()
    import yaml
    yaml.dump(person, content)

    # validate the content

# Generated at 2022-06-14 15:03:09.389945
# Unit test for function validate_yaml
def test_validate_yaml():
    text = """
    ---
    hello: World
    """
    value, error_messages = validate_yaml(
        text, Field(type="object", properties={"hello": {"type": "string"}})
    )
    assert value == {"hello": "World"}
    assert len(error_messages) == 0

    text = """
    ---
    hello: World
    """
    value, error_messages = validate_yaml(
        text, Field(type="object", properties={"hello": {"type": "integer"}})
    )
    assert value is None
    assert len(error_messages) == 1
    assert isinstance(error_messages[0], ValidationError)
    assert "hello" in error_messages[0].message
    assert error_messages[0].position.line_no

# Generated at 2022-06-14 15:03:21.352870
# Unit test for function validate_yaml
def test_validate_yaml():
    class DocumentSchema(Schema):
        """
        https://docs.djangoproject.com/en/3.0/topics/forms/media/#media-uploads-and-forms
        """
        title = "Document"
        description = "A document"

        class Options:
            fields = ("title", "authors", "path")

        def title(self, value: str) -> str:
            return value

        def authors(self, value: typing.List[str]) -> typing.List[str]:
            return value

        def path(self, value: str) -> str:
            return value

    def assert_valid(content: str, expected_value: str, expected_errors: typing.List[Message]):
        value, errors = validate_yaml(content=content, validator=DocumentSchema)

# Generated at 2022-06-14 15:03:27.299053
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Scenario 1: test tokenize_yaml with a valid yaml string
    content = '{"a": "b"}'
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value == {"a": "b"}

    # Scenario 2: test tokenize_yaml with multiple valid yaml strings
    content = '{"a": "b"}\n{"c": "d"}'
    token = tokenize_yaml(content)
    assert isinstance(token, ListToken)
    assert len(token.value) == 2
    assert isinstance(token.value[0], DictToken)
    assert isinstance(token.value[1], DictToken)

    # Scenario 3: test tokenize_yaml with empty string
    content = ''

# Generated at 2022-06-14 15:03:37.717501
# Unit test for function validate_yaml
def test_validate_yaml():
    # Happy path
    yaml_content = """
    title: Clean Code
    author: Robert C. Martin
    price: 11.99
    available: true
    """
    validator = Schema(
        {
            "title": Field(str),
            "author": Field(str),
            "price": Field(float),
            "available": Field(bool),
        }
    )
    value, errors = validate_yaml(content=yaml_content, validator=validator)
    assert not errors
    assert value == {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "price": 11.99,
        "available": True,
    }

    # Unhappy path

    # Missing fields

# Generated at 2022-06-14 15:03:42.441624
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    a: 0
    b: 1
    c: 2
    """
    schema = Schema({"a": int, "b": int, "c": int})
    assert validate_yaml(content, schema) == ({'a': 0, 'b': 1, 'c': 2}, [])

# Generated at 2022-06-14 15:03:59.530579
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''
    ---
    foo: bar
    key: value
    '''
    token = tokenize_yaml(content)
    error_messages = validate_with_positions(token=token, validator=Field)
    assert isinstance(error_messages, list)

    expected_result = [
        Message(
            text="Value is not valid",
            code="invalid",
            position=Position(
                line_no=3,
                column_no=4,
                char_index=13,
            ),
        ),
        Message(
            text="Value is not valid",
            code="invalid",
            position=Position(
                line_no=4,
                column_no=4,
                char_index=24,
            ),
        ),
    ]
    assert error_messages

# Generated at 2022-06-14 15:04:09.033077
# Unit test for function validate_yaml
def test_validate_yaml():
    sample_yaml = """
        a: 1
        b: x
        c: true
    """
    schema = Schema({"a": int, "b": str, "c": bool})
    value, errors = validate_yaml(sample_yaml, schema)

    assert value == {"a": 1, "b": "x", "c": True}
    assert errors == [
        ValidationError(
            text="Expected {} to be an int.".format("b"),
            code="invalid",
            position=Position(line_no=3, column_no=4, char_index=14),
        )
    ]

# Generated at 2022-06-14 15:04:19.977103
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    import sys
    import typesystem
    # no value
    class BasicSchema(typesystem.Schema):
        name = typesystem.String()
    validator = BasicSchema()
    value, error_messages = validate_yaml(content='', validator=validator)
    assert value is None
    assert isinstance(error_messages[0], typesystem.ValidationError)
    assert len(error_messages) == 1
    assert error_messages[0].code == 'required'
    assert error_messages[0].message == "This field is required."
    # additional properties
    class BasicSchema(typesystem.Schema):
        name = typesystem.String()
    validator = BasicSchema()
    value, error_mess

# Generated at 2022-06-14 15:04:28.618879
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer
    from typesystem.schemas import ExampleSchema
    from typesystem.tokenize.types import StringToken
    from typesystem.tokenize.positional_validation import ValidationError as PosValError

    def do_test(content, validator, expected):
        result, error_messages = validate_yaml(content, validator)
        assert result == expected
        assert error_messages == []

    # Valid content
    do_test('''
        foo: bar
        n: 123456
    ''', ExampleSchema, {'foo': 'bar', 'n': 123456})
    do_test('''
        foo: bar
        n: 123
    ''', ExampleSchema, {'foo': 'bar', 'n': 123})

# Generated at 2022-06-14 15:04:36.994483
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import schema

    class MySchema(schema.Schema):
        '''Docstring'''
        a = schema.String(description="a string", required=True)

    content = b"a: test1\nb: test2"
    value, errors = validate_yaml(content, MySchema)
    assert errors == [
        Message(
            text="Unexpected field: b.",
            code="unexpected_field",
            position=Position(column_no=1, line_no=2, char_index=9),
        )
    ]

# Generated at 2022-06-14 15:04:45.636560
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test validate_yaml
    """
    # Test parsing errors
    with pytest.raises(ParseError):
        validate_yaml("[1, a]", List[int])

    # Test validation errors
    value, errors = validate_yaml("[]", List[int])
    assert errors
    error_msg = "Expected list of type 'int' but got []. (line 1, column 1)"
    assert errors[0].messages[0] == Message(text=error_msg, code="type_error")

    # Test successful parse and validation
    value, errors = validate_yaml("[1]", List[int])
    assert value == [1]

# Generated at 2022-06-14 15:04:56.540247
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.base import Validator
    from typesystem.fields import Integer, Number
    from typesystem.schemas import Schema

    class MySchema(Schema):
        my_integer = Integer(minimum=10)

    integer, error_messages = validate_yaml(b"my_integer: 2", validator=MySchema)

    assert integer == {"my_integer": 2}
    assert len(error_messages) == 1
    assert isinstance(error_messages, list)
    assert error_messages[0]["code"] == "min_value"
    assert error_messages[0]["text"] == "Must be >= 10."
    assert error_messages[0]["field"] == "my_integer"
    assert error_messages[0]["position"].line_no == 1
   

# Generated at 2022-06-14 15:05:06.745542
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Text, DateTime

    class PostSchema(Schema):
        title = String()
        body = Text()
        created_at = DateTime()

    test_yaml = """
    title: 'Hello world'
    body: "This is a body with a 'quoted string' in it"
    created_at: '2019-05-16T20:28:12.454321'
    """

    value, errors = validate_yaml(test_yaml, PostSchema)

    assert not errors

# Generated at 2022-06-14 15:05:11.165818
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("") == None
    assert tokenize_yaml("#this is a test") == None
    assert tokenize_yaml('{ "this": { "is":[ 1,2,3,4,5] } }') == {'this': {'is': [1, 2, 3, 4, 5]}}



# Generated at 2022-06-14 15:05:23.313776
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String
    from typing import List

    yaml_string = """
        one: two
    """
    yaml_dict = {'one': 'two'}

    value, error_messages = validate_yaml(
        content=yaml_string,
        validator=String(keyword='one')
    )
    assert value == yaml_dict
    assert error_messages == []
    
    value, error_messages = validate_yaml(
        content=yaml_string,
        validator=String(keyword='one', required=True)
    )
    assert value == yaml_dict
    assert error_messages == []
    

# Generated at 2022-06-14 15:05:41.726675
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.base import ValidationError
    from typesystem.fields import String, Integer
    from typesystem import SchemaMeta
    from typesystem.schemas import Schema

    class MySchema(Schema, metaclass=SchemaMeta):
        number = Integer(minimum=1, maximum=10)
        name = String(max_length=10)

    content = "number: 5\nname: 'Aardvark'"
    token = tokenize_yaml(content)
    value, validation_errors = validate_with_positions(token, MySchema())
    assert value == {"number": 5, "name": "Aardvark"}
    assert validation_errors == []

    content = "number: 0\nname: 'Aardvark'"
    token = tokenize_yaml(content)
    value, validation

# Generated at 2022-06-14 15:05:48.589023
# Unit test for function validate_yaml
def test_validate_yaml():
    import typing
    
    import yaml
    from yaml.loader import SafeLoader
    from yaml.parser import ParserError
    from pytest import raises
    from typesystem.base import Message, ParseError, Position, ValidationError
    from typesystem.fields import Boolean, Integer, String
    
    
    content = "yes"
    validator = Boolean()
    token = tokenize_yaml(content)
    value, error_messages = validate_with_positions(token=token, validator=validator)
    assert type(value) == bool
    assert value
    assert len(error_messages) == 0

    
    content = "500"
    validator = Integer()
    token = tokenize_yaml(content)

# Generated at 2022-06-14 15:06:00.723637
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, Object, String

    class FooSchema(Schema):
        name = String()
        age = Integer()

    content = "name: Sam\nage: 30"
    value, errors = validate_yaml(content, validator=FooSchema)
    assert value == {"name": "Sam", "age": 30}
    assert errors == []

    content = "name:\n  Sam"
    value, errors = validate_yaml(content, validator=FooSchema)
    assert errors[0].code == "parse_error"

    class BarSchema(Schema):
        name = String(min_length=5)

    content = "name: Sam"
    value, errors = validate_yaml(content, validator=BarSchema)

# Generated at 2022-06-14 15:06:07.969080
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer, Float, Boolean, Array, Object, Schema
    from typesystem.fields import RootField
    from typesystem.exceptions import ValidationError

    schema = Schema(
        {
            "name": String(),
            "age": Integer,
            "height": Float,
            "registered": Boolean,
            "subjects": Array(String),
            "address": Object({"city": String(), "state": String()}),
        }
    )

    # Correct input
    data = """
name: John
age: 19
height: 5.8
registered: false
subjects:
    - Math
    - Physics
    - Biology
address:
    city: New York City
    state: NY
"""
    s, msgs = validate_yaml(data, schema)

    assert len(msgs)