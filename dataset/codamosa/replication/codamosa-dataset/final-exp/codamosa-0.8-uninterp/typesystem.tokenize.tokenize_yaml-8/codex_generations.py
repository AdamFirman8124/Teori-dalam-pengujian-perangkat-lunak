

# Generated at 2022-06-14 14:56:26.099450
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    test_inputs = ["{}", "{a: 1}", "[1, 2, 3]", 'a: "b"', "a: {}"]
    for i in test_inputs:
        token = tokenize_yaml(i)
        validator = Field(name="")
        errors = []
        try:
            _ = validator.validate(token)
        except ValidationError as e:
            errors = e.messages
        assert len(errors) == 0

# Generated at 2022-06-14 14:56:34.419223
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('') == []
    assert tokenize_yaml('---') == []
    assert tokenize_yaml('---\n- test') == ['test']
    assert tokenize_yaml('---\n- test\n- test2') == ['test', 'test2']
    assert tokenize_yaml('---\n- test\n- test2\n- 3') == [3]
    assert tokenize_yaml('---\n- test\n- test2\n- 3\n- "test4"') == ['test4']
    assert tokenize_yaml('---\n- test\n- test2\n- 3\n- "test4"\n- - test5') == [['test5']]

# Generated at 2022-06-14 14:56:40.315468
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""
    key: value
    """)
    assert token.value == {"key": "value"}
    assert token.start == 0
    assert token.end == 14
    assert token.content == "    key: value\n    "
    assert token.get_position(4) == Position(line_no=2, column_no=5, char_index=4)


# Generated at 2022-06-14 14:56:50.780439
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    name: john
    age: 10
    friends:
    - a
    - b
    - c
    """
    assert tokenize_yaml(content) == {
        "name": "john",
        "age": 10,
        "friends": ["a", "b", "c"],
    }

    content = ""
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(content)
    assert exc_info.value.text == "No content."
    assert exc_info.value.position.line_no == 1
    assert exc_info.value.position.column_no == 1
    assert exc_info.value.position.char_index == 0
    assert exc_info.value.code == "no_content"


# Generated at 2022-06-14 14:56:58.234760
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml(
        """---
        foo: bar
        baz:
          - dogs: cats
        """
    ) == {
        "foo": "bar",
        "baz": [{"dogs": "cats"}],
    }

    # Alias for None
    assert tokenize_yaml("foo: ~") == {"foo": None}

    # Integers are considered strings, as is this case
    assert tokenize_yaml("foo: 123") == {"foo": "123"}



# Generated at 2022-06-14 14:57:06.994524
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(fields=[
        Field(name="name", type="string"),
        Field(name="age", type="integer")
    ])
    value, error_messages = validate_yaml("""
    name: Sam
    age: 32
    """, schema)
    assert value == {"name": "Sam", "age": 32}
    assert error_messages == []

    value, error_messages = validate_yaml("""
    name: Sam
    """, schema)
    assert value == {"name": "Sam"}
    assert isinstance(error_messages[0], Message)
    assert error_messages[0].text == "Missing required field."
    assert error_messages[0].code == "missing_field"
    assert error_messages[0].position.line_no == 3

# Generated at 2022-06-14 14:57:17.870369
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # simple cases
    assert tokenize_yaml("42") == 42
    assert tokenize_yaml("""foo: bar""") == {"foo": "bar"}
    assert tokenize_yaml("""- foo""") == ["foo"]
    assert tokenize_yaml("""["foo"]""") == ["foo"]

    # position annotation
    assert isinstance(tokenize_yaml("""{"foo": "bar"}"""), DictToken)
    assert tokenize_yaml("""{"foo": "bar"}""").start == 0
    assert tokenize_yaml("""{"foo": "bar"}""").end == 12
    
    # unicode

# Generated at 2022-06-14 14:57:28.784079
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml(b"True")
    assert token.content == "True"

    token = tokenize_yaml(b"True")
    assert token.value == True

    token = tokenize_yaml(b"-123")
    assert token.value == -123

    token = tokenize_yaml(b"12.3")
    assert token.value == 12.3

    token = tokenize_yaml(b"12.3")
    assert token.content == "12.3"

    token = tokenize_yaml(b'""')
    assert token.value == ""

    token = tokenize_yaml(b'"hello"')
    assert token.value == "hello"

    token = tokenize_yaml(b"{}")
    assert token.value == {}

    token = tokenize_

# Generated at 2022-06-14 14:57:32.723319
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = '''\
name: "Foo"
age: 25
'''
    token = tokenize_yaml(content)
    assert token.mapping == {'name': 'Foo', 'age': 25}

# Generated at 2022-06-14 14:57:43.155092
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(type="integer")
    yaml_invalid = "|\n" + "  [\n" + "  0,\n" + "  a,\n" + "  ]\n" # bytestring
    value, error = validate_yaml(yaml_invalid, validator)
    assert error
    assert isinstance(error, ListToken)
    assert len(error) == 2
    assert error[0].code == "invalid_type"
    assert error[0].position.line_no == 3
    assert error[0].position.column_no == 2
    assert error[0].position.char_index == 7
    assert error[1].code == "invalid_type"
    assert error[1].position.line_no == 4
    assert error[1].position.column_no

# Generated at 2022-06-14 14:57:56.417610
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test with a string
    content = """
        products:
          - id: 1
            name: Foo
            price: 2.20
          - id: 2
            name: Bar
            price: 3.30
    """
    class ProductSchema(Schema):
        id = fields.Integer(required=True)
        name = fields.String(required=True)
        price = fields.Number(required=True)
    value, errors = validate_yaml(content, validator=ProductSchema)
    assert value == {
        "products": [
            {"id": 1, "name": "Foo", "price": 2.2},
            {"id": 2, "name": "Bar", "price": 3.3},
        ]
    }
    assert errors == []

    # Test with bytestring (same test as above)

# Generated at 2022-06-14 14:58:08.146703
# Unit test for function validate_yaml
def test_validate_yaml():
    class Inner(Schema):
        a = Field(type="string", required=True)

    class InnerValidator(Schema):
        a = Field(type="string", required=False)

    class Outer(Schema):
        a = Field(type="number", required=True)
        c = Field(type="inner", required=True)
        d = Field(type="inner-validator", required=False)

    class OuterValidator(Schema):
        a = Field(type="string", required=True)
        b = Field(type="string")
        e = Field(type="string")


# Generated at 2022-06-14 14:58:18.925472
# Unit test for function validate_yaml
def test_validate_yaml():
    tokenize = tokenize_yaml("1:")
    
    tokenize = tokenize_yaml("- hello\n")
    assert type(tokenize) is ListToken, "tokenize is not ListToken"
    
    tokenize = tokenize_yaml("- world")
    assert type(tokenize) is ListToken, "tokenize is not ListToken"
    
    tokenize = tokenize_yaml("- world\n")
    assert type(tokenize) is ListToken, "tokenize is not ListToken"
    
    tokenize = tokenize_yaml("name: hello")
    assert type(tokenize) is DictToken, "tokenize is not DictToken"
    
    tokenize = tokenize_yaml("name: hello\n")

# Generated at 2022-06-14 14:58:27.912980
# Unit test for function validate_yaml
def test_validate_yaml():
    test_schema = Schema([
        {"name": "age", "type": "integer", "minValue": 0},
        {"name": "first_name", "type": "string", "maxLength": 40},
        {"name": "last_name", "type": "string", "maxLength": 40},
    ])
    content = '{"age": 123}'
    value, error_messages = validate_yaml(content, test_schema)
    assert error_messages == []
    assert value == {"age": 123}

    content = '{"age": "123"}'
    value, error_messages = validate_yaml(content, test_schema)
    assert len(error_messages) == 1
    assert error_messages[0].text == "\"123\" is not an integer."
    assert error_mess

# Generated at 2022-06-14 14:58:31.488433
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("foo") == "foo"
    with pytest.raises(ParseError):
        tokenize_yaml("")


# Generated at 2022-06-14 14:58:41.862177
# Unit test for function validate_yaml
def test_validate_yaml():
    # Define a schema for testing
    class MyValidSchema(Schema):
        name = "foo"
        id = "bar"

    class MyInvalidSchema(Schema):
        name = "foo"
        id = "bar"
        phone = "baz"

    for test_string, expected in [
        ('{"name": "foo", "id": "bar"}', MyValidSchema),  # type: ignore
        ('{"name": "foo", "id": "bar", "phone": "baz"}', MyInvalidSchema),  # type: ignore
    ]:
        assert validate_yaml(content=test_string, validator=MyValidSchema)[0] == expected(name='foo', id='bar')
        # Note schema is only defined as a type, not instantiated

# Generated at 2022-06-14 14:58:53.106688
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.tokenize.tokens import ListToken, ScalarToken, Token
    from typesystem.types import Array, Boolean, Number, Object, String
    from typesystem.validators import MaxLength, MinLength, OneOf

    content = """
    a:
      b: "test"
    c: [1, 2, 3]
    """

    token = tokenize_yaml(content)

    assert isinstance(token, Token)
    assert isinstance(token, DictToken)
    assert token.content == "a:\n  b: test\nc:\n- 1\n- 2\n- 3\n"
    assert token.start == 0
    assert token.end == token.content.find("\n", 0)

# Generated at 2022-06-14 14:58:57.305025
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('---\n') == Token(None)
    assert tokenize_yaml('') == Token(None)
    assert tokenize_yaml('[]') == ListToken(
        [], 0, 1, content='[]'
    )
    assert tokenize_yaml('iamstring') == ScalarToken(
        'iamstring', 0, 8, content='iamstring'
    )
    assert tokenize_yaml(
        '''
name: string
'''
    ) == DictToken(
        {'name': 'string'}, 0, 18, content='\nname: string\n'
    )

# Generated at 2022-06-14 14:59:09.941876
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(
        {
            "name": String(max_length=10, description="name of the person"),
            "age": Integer(minimum=0, maximum=130, description="age of the person"),
        },
        description="details of a person",
    )
    schema_instance = schema()
    content = ("name: good\nage: 18")
    value, error_messages = validate_yaml(content, validator=schema_instance)
    assert error_messages == []
    assert value == {"name": "good", "age": 18}
    content = ("name: too_long\nage: 18")
    value, error_messages = validate_yaml(content, validator=schema_instance)
    assert error_messages != []

# Generated at 2022-06-14 14:59:17.852914
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert (
        tokenize_yaml('{"field1": "value1", "field2": "value2"}') ==
        {'field1': 'value1', 'field2': 'value2'}
    )
    assert (
        tokenize_yaml('["value1", "value2"]') ==
        ["value1", "value2"]
    )
    assert (
        tokenize_yaml("string") ==
        "string"
    )
    assert (
        tokenize_yaml("123") ==
        123
    )
    assert (
        tokenize_yaml("123.45") ==
        123.45
    )
    assert (
        tokenize_yaml("true") ==
        True
    )
    assert (
        tokenize_yaml("null") ==
        None
    )

# Generated at 2022-06-14 14:59:31.765583
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml({}, validator={}) == ({}, [])
    assert validate_yaml({}, validator={"name": str}) == ({}, [])

    yaml_string = """
    name: Bob
    age: 12
    """

    assert validate_yaml(
        yaml_string,
        validator={
            "name": str,
            "age": int,
        },
    ) == ({"name": "Bob", "age": 12}, [])

    try:
        assert validate_yaml(
            yaml_string,
            validator={
                "name": str,
                "age": float,
            },
        )
    except ValidationError as error:
        assert error.code == "integer_is_required"
        assert error.text == "Must be of type float."

# Generated at 2022-06-14 14:59:42.006300
# Unit test for function validate_yaml
def test_validate_yaml():
    s = Schema(fields={"name": String()})
    value, errors = validate_yaml("name: 12", s)
    assert value == {"name": "12"}
    assert isinstance(errors, ErrorList)
    assert len(errors) == 1
    error = errors[0]
    assert error.code == "format_error"
    assert error.position.line_no == 1
    assert error.position.column_no == 5
    assert error.position.char_index == 6
    assert error.data == {"field": "name", "validator": String()}
    assert error.text == "Must be a string."



# Generated at 2022-06-14 14:59:45.253979
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String(min_length=2)
        age = Integer(minimum=0)

    s = """\
name: John
age: 50
"""
    value, errors = validate_yaml(s, Person)
    assert value
    assert not errors
    s = """\
name: Alice
age: -10
"""
    value, errors = validate_yaml(s, Person)
    assert not value
    assert len(errors) == 1
    error_text = str(errors[0])
    assert "minimum" in error_text



# Generated at 2022-06-14 14:59:52.636224
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test for the function validate_yaml. Upper case string must fail
    """
    # pylint: disable=line-too-long
    from typesystem import Schema

    class SimpleSchema(Schema):
        name = fields.String(title="Name")

        class Meta:
            strict = True

    content = '{"name": "Chris"}'
    (value, error_messages) = validate_yaml(content, validator=SimpleSchema)
    assert value == {"name": "Chris"}
    assert len(error_messages) == 0
    
    content = '{"name": "CHRIS"}'
    (value, error_messages) = validate_yaml(content, validator=SimpleSchema)
    assert value == None
    assert len(error_messages) == 1

# Generated at 2022-06-14 15:00:02.507519
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer, Array, validator, message
    from typesystem.errors import InvalidType, MissingValue
    BaseSchema = validator(
        {
            "title": String(max_length=50, required=True),
            "body": String(),
            "author": String(max_length=50),
        }
    )

    class BlogPost(BaseSchema):
        tags = Array(String(max_length=50))

    class ImagePost(BaseSchema):
        image_url = String(format="url")
        author = None

    class Post(BaseSchema):
        type = String(choices=["blog", "image"])
        body = String(required=False)
        author = String(required=False)


# Generated at 2022-06-14 15:00:09.829018
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""
    hello: world
    evil:
      - true
      - false
    """)
    assert isinstance(token, typing.Dict)
    assert token.content == """
    hello: world
    evil:
      - true
      - false
    """
    assert token.content[token.start] == "h"
    assert token.content[token.end] == "\n"



# Generated at 2022-06-14 15:00:14.643875
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    content = "id: 123\nname: myname"
    schema = typesystem.Schema(id = typesystem.Integer, name = typesystem.String)
    value, error = validate_yaml(content, schema)
    print("value: %s, error: %s" % (value, error))


# Generated at 2022-06-14 15:00:20.011070
# Unit test for function validate_yaml
def test_validate_yaml():
    print(validate_yaml('name: "Dawson"', Field(type='string')))
    print(validate_yaml('name: "Dawson"', Field(type='integer')))
    print(validate_yaml('name: "Dawson"', Field(type='string', enum=['Dawson'])))



# Generated at 2022-06-14 15:00:25.223713
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String
    validator = String(max_length=10)
    value, error_messages = validate_yaml("goodbye", validator)
    assert value == "goodbye"
    assert error_messages == []

    value, error_messages = validate_yaml("badbye", validator)
    assert value == "badbye"
    assert error_messages == [
        Message(
            text="Value is too long.",
            code="max_length",
            position=Position(line_no=1, column_no=1, char_index=0)
        )
    ]

# Generated at 2022-06-14 15:00:31.298597
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    class ZipSchema(Schema):
        code = "zip_code"
        zip_code = fields.String(description="A zip code")
        city = fields.String(description="The city to which the zip code belongs")
        country = fields.String(description="The country to which the zip code belongs")

    schema = ZipSchema()
    input_data = """
---
zip_code: "12345"
city: "City"
country: "Country"
...
"""
    output_data, errors = validate_yaml(input_data, schema)

    assert not errors
    assert output_data == {"zip_code": "12345", "city": "City", "country": "Country"}

# Generated at 2022-06-14 15:00:39.631111
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class PersonSchema(Schema):
        name = String(required=True)

    content = """
            name: James
        """.strip()
    token = tokenize_yaml(content)
    assert token.get("name") == "James"
    value, messages = validate_yaml(content, validator=PersonSchema)
    assert value == {"name": "James"}
    assert messages == []



# Generated at 2022-06-14 15:00:49.889279
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test that validate_yaml() works as expected.

    """
    # Simple YAML document with one key-value pair.
    yaml_string = '''
    foo: 42
    '''
    # We must use a Schema here because we need access to the fields.
    class YamlSchema(Schema):
        """
        Schema to validate a YAML document that contains a single key-value pair.

        """
        foo = Field(int)

    value, errors = validate_yaml(yaml_string, validator=YamlSchema)

    assert not errors

    assert value["foo"] == 42

    # Document with a 32-bit integer.
    yaml_string = '''
    foo: 2147483648
    '''

# Generated at 2022-06-14 15:00:55.149707
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml('int: 0 \nfloat: 0.0 \nstring: "a string"')
    assert token.children[0].children[1].value == 0
    assert token.children[1].children[1].value == 0.0
    assert token.children[2].children[1].value == "a string"

# Generated at 2022-06-14 15:01:07.074945
# Unit test for function validate_yaml
def test_validate_yaml():

    # Test for bad input
    # Test for bad YAML
    with pytest.raises(ParseError):
        validate_yaml(content="{ 'key': 'value' }", validator=Field(type=dict))

    # Test for bad schema
    with pytest.raises(ValidationError):
        validate_yaml(content="key: value", validator=Field())

    # Test for good input
    (value, errors) = validate_yaml(content="key: value", validator=Field(type=dict))
    assert isinstance(value, DictToken)
    assert len(errors) == 0

    (value, errors) = validate_yaml(content="key: value", validator=Field(type=str))
    assert isinstance(value, ScalarToken)
    assert len(errors) == 0

# Generated at 2022-06-14 15:01:15.345565
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        foo = ScalarToken["str"](required=True)
        bar = ScalarToken["str"](required=True)

    valid_yaml = """
    foo: hello
    bar: world
    """

    invalid_yaml = """
    foo: hello
    baz: world
    """

    errors = validate_yaml(invalid_yaml, TestSchema)

    expected_error = Message(
        text="Field 'bar' is required.",
        code="required",
        position=Position(line_no=3, column_no=5, char_index=24),
        pointer="/bar",
    )

    assert len(errors) == 1
    assert errors[-1] == expected_error

# Generated at 2022-06-14 15:01:23.562363
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    # Test valid YAML
    content = '''---
name: Alice
age: 30
...'''
    schema_cls = typing.TypeVar('schema_cls', bound='Schema')
    class Profile(Schema):
        age = Field(type=int)
        name = Field(type=str)

    value, errors = validate_yaml(content, Profile)

    assert value == {'name': 'Alice', 'age': 30}
    assert errors == []

    # Test invalid YAML
    content = '''{'''
    with pytest.raises(ParseError):
        validate_yaml(content, Profile)

    # Test invalid data

# Generated at 2022-06-14 15:01:34.491890
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String(max_length=10)

    class People(Schema):
        people = List[Person]
        
    class People2(Schema):
        people = Dict[str, Person]

    str_content = """
    people:
      - name: "Fred"
      - name: "Wilma"
    """

    str_content_not_list = """
    people:
      name: "Fred"
    """

    str_content_too_long = """
    people:
      - name: "This name is too long"
    """

    value, errors = validate_yaml(str_content, People)
    assert errors == []
    assert value == {
        "people": [{"name": "Fred"}, {"name": "Wilma"}]
    }

    value,

# Generated at 2022-06-14 15:01:41.653448
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = typing.List[str]


    content = 'name: [John, Eric, Paul]'
    value, error_messages = validate_yaml(content, validator=PersonSchema)
    assert isinstance(value, DictToken)
    assert value.content == content
    assert isinstance(error_messages, list)
    assert len(error_messages) > 0
    assert isinstance(error_messages[0], Message)

# Generated at 2022-06-14 15:01:42.598882
# Unit test for function validate_yaml
def test_validate_yaml():
    # this function is a unit test
    assert True

# Generated at 2022-06-14 15:01:48.134228
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        name = Field(required=True)
        address = Field(required=True)

    (value, errors) = validate_yaml(
        content="""
        name: John
        address:
          line1: 123 Main St
          city:  Anytown
          state: OR
          zip:   97222
        """,
        validator=MySchema(),
    )
    assert value == {"name": "John", "address": {"line1": "123 Main St", "city": "Anytown", "state": "OR", "zip": "97222"}}

# Generated at 2022-06-14 15:01:55.372891
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test that validate_yaml returns a value and error messages when a YAML
    string is passed
    """
    content = "name: Sarah"
    validator = types.String("name")
    value, error_messages = validate_yaml(content, validator)
    assert value == "Sarah"
    assert error_messages == []

# Generated at 2022-06-14 15:02:02.242100
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(
        """
        a: 1
        b: 2
        c: 3
        """,
        Schema({"a": int, "b": int, "c": int}),
    ) == ({
        "a": ScalarToken(1,4,5),
        "b": ScalarToken(2,11,12),
        "c": ScalarToken(3,18,19)
    }, [])


# Generated at 2022-06-14 15:02:08.321326
# Unit test for function validate_yaml
def test_validate_yaml():
    # Valid YAML
    valid_content = """
    name: 'John Smith'
    age: 23
    """
    valid_schema = """
    type: object
    properties:
      name:
        type: string
      age:
        type: integer
    """
    test_content = valid_content.encode('utf-8')
    test_schema = yaml.load(valid_schema)
    r = validate_yaml(content=test_content, validator=test_schema)
    assert r[0].value == {'name': 'John Smith', 'age': 23}
    assert len(r[1].errors) == 0

    # Invalid YAML
    invalid_content = """
    name: 'John Smith
    age: 23
    """

# Generated at 2022-06-14 15:02:19.315915
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String

    class PetSchema(Schema):
        name = String()
        age = Integer()

    data = """
    name: kitty
    age: 3
    """

    assert validate_yaml(data, PetSchema) == (
        {"name": "kitty", "age": 3},
        [],
    )

    data = """
    name: 3
    age: 3
    """

    errors = validate_yaml(data, PetSchema)[1]
    assert len(errors) == 1
    assert errors[0].position.column_no == 8

    data = """
    name: kitty
    """

    errors = validate_yaml(data, PetSchema)[1]
    assert len(errors) == 1

# Generated at 2022-06-14 15:02:31.409110
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Verify that the result of calling "validate_yaml" with valid YAML returns
    a corresponding Python object and no error messages.

    This function is unit tested with Pytest.
    """
    content = '''
            - 9876543210
            - 9876543211
            - 9876543212
            - 9876543213
            - 9876543214
            - 9876543215
            - 9876543216
            - 9876543217
            - 9876543218
            - 9876543219
        '''
    value, error_messages = validate_yaml(content=content, validator=Field(type=int))

# Generated at 2022-06-14 15:02:36.317906
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert repr(tokenize_yaml("""{key: value}""")) == repr(
        DictToken({"key": ScalarToken("value", 4, 10, content="{key: value}")}, 0, 12, content="{key: value}")
    )


# Generated at 2022-06-14 15:02:46.117092
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        name = "str"
        age = "int"

    yaml_str = "name: Jane\nage: 20"
    my_schema, messages = validate_yaml(yaml_str, MySchema)
    assert my_schema == {"name": "Jane", "age": 20}
    assert messages == []

    bad_yaml_str = "name: Jane\nage: twenty"
    my_schema_val, messages = validate_yaml(bad_yaml_str, MySchema)
    assert my_schema_val == {}
    assert messages == [Message("'twenty' is not of type 'int'", code="type_error",
                                position=Position(3, 7, index=13))]


# Generated at 2022-06-14 15:02:50.318007
# Unit test for function validate_yaml
def test_validate_yaml():
    data = validate_yaml(
        """\
name: Eric Idle
age: 74
""",
        Schema({"name": "text", "age": "integer"}),
    )
    assert data[0] == {"name": "Eric Idle", "age": 74}



# Generated at 2022-06-14 15:03:00.159266
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test string containing valid data
    content = '''
    name: Jim Beam
    age: 42
    '''
    schema = Schema({'name': str, 'age': int})
    value, errors = validate_yaml(content, schema)
    print(value, errors)

    # Test string containing invalid data
    content = '''
    name: Jim Beam
    age: "forty two"
    '''
    schema = Schema({'name': str, 'age': int})
    value, errors = validate_yaml(content, schema)
    print(value, errors)

    # Test empty string
    content = ''
    schema = Schema({'name': str, 'age': int})
    value, errors = validate_yaml(content, schema)
    print(value, errors)

    # Test invalid input


# Generated at 2022-06-14 15:03:09.662343
# Unit test for function validate_yaml
def test_validate_yaml():

    err = ValidationError(code='unknown', path='', text='failed', position=Position(column_no=1, line_no=1, char_index=0))
    assert err.position == Position(column_no=1, line_no=1, char_index=0)

    # Test to ensure that empty string is handled correctly.
    with pytest.raises(ParseError):
        validate_yaml(content='', validator=Field(type=str, min_length=1))

    # Test to ensure that errors are handled correctly.
    [value, errors] = validate_yaml(content='test: "hello"', validator=Field(type=str, min_length=1))
    assert errors == []

    # Test to ensure that errors are handled correctly.

# Generated at 2022-06-14 15:03:17.164515
# Unit test for function validate_yaml
def test_validate_yaml():
    import json
    assert json.dumps(validate_yaml(b'1', 'int')) == "[1, []]"

# Generated at 2022-06-14 15:03:27.681300
# Unit test for function validate_yaml
def test_validate_yaml():
    f = Field(type=int)
    assert validate_yaml(b"1", f)[0] == 1
    assert validate_yaml(b"", f)[0] is None

    f = Field(type=int, required=False)
    assert validate_yaml(b"1", f)[0] == 1
    assert validate_yaml(b"", f)[0] is None

    f = Field(type=int, required=False, allow_null=True)
    assert validate_yaml(b"1", f)[0] == 1
    assert validate_yaml(b"", f)[0] is None
    assert validate_yaml(b"null", f)[0] is None

    f = Field(type=int)
    assert validate_yaml(b"string", f)[0] is None

    f = Field

# Generated at 2022-06-14 15:03:38.006537
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class PersonSchema(Schema):
        first_name = String()
        last_name = String()

    content = "first_name: James\nlast_name: Parry"
    schema = PersonSchema()
    value, errors = validate_yaml(content, schema)
    assert value == {"first_name": "James", "last_name": "Parry"}
    assert errors == []

    content = "first_name: James\nlast_name: Parry"
    schema = PersonSchema()
    schema.fields["last_name"].required = True
    value, errors = validate_yaml(content, schema)
    assert value == {"first_name": "James"}

# Generated at 2022-06-14 15:03:39.537060
# Unit test for function validate_yaml
def test_validate_yaml():

    assert(validate_yaml('hello', str) == ("hello", []))

# Generated at 2022-06-14 15:03:48.763799
# Unit test for function validate_yaml
def test_validate_yaml():
    # Arrange
    content = """
    name: Tyler
    age: 28
    """
    class PersonSchema(Schema):
        name = "Person"
        fields = {
            "name": Field(str),
            "age": Field(int),
        }
    # Act
    value, error_messages = validate_yaml(content, validator=PersonSchema)
    
    if error_messages:
        print(json.dumps(error_messages, indent=4))
    
    # Assert
    assert not error_messages
    assert value == {'age': 28, 'name': 'Tyler'}

test_validate_yaml()

# Generated at 2022-06-14 15:03:57.868173
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b"""
    - name: North America
      members:
        - United States
        - Canada
        - Mexico
    - name: South America
      members:
        - Argentina
        - Brazil
        - Chile
    """

    class Continent(Schema):
        name = String(required=True)
        members = List(String(), required=True)

    result = validate_yaml(content, Continent.as_field())

    assert len(result.error_messages) == 0
    assert type(result.value) is list
    assert len(result.value) == 2

    assert result.value[0]["name"] == "North America"
    assert type(result.value[0]["members"]) is list

# Generated at 2022-06-14 15:04:03.388553
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""
        name: userName
        age: 25
        job:
            title: Developer
            experience: 2
        skills: [Python, C]
        marital_status: Single
    """)
    assert token == {
        'name': 'userName',
        'age': 25,
        'job': {
            'title': 'Developer',
            'experience': 2,
        },
        'skills': ['Python', 'C'],
        'marital_status': 'Single'
    }



# Generated at 2022-06-14 15:04:12.585217
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class MySchema(Schema):
        foo = String()

    valid, errors = validate_yaml(content="foo: bar", validator=MySchema)
    assert valid
    assert errors == []

    valid, errors = validate_yaml(content="foo: 1", validator=MySchema)
    assert not valid
    assert errors == [
        ValidationError(
            code="invalid_type",
            text="Is not a valid string.",
            position={
                "column_no": 7,
                "line_no": 1,
                "char_index": 6,
            },
        )
    ]

    valid, errors = validate_yaml(content="invalid", validator=MySchema)
    assert not valid


# Generated at 2022-06-14 15:04:19.618854
# Unit test for function validate_yaml
def test_validate_yaml():
    fields = {"foo": {"typesystem": str}}
    schema = Schema(fields)
    content = """\
    foo: 123
    """
    value, errors = validate_yaml(content, schema)
    assert value["foo"] == "123"
    assert isinstance(errors, list)
    assert len(errors) == 1
    error = errors[0]
    assert error.code == "type_error.str"
    assert error.pointer == "/foo"



# Generated at 2022-06-14 15:04:28.304413
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem.fields import String
    from typesystem.types.int import Int
    from typesystem.types.strict import StrictType

    class MyType(StrictType):
        field_1 = String()
        field_2 = Int()

    content = yaml.dump({"field_1": "value_1", "field_2": 2})
    value, errors = validate_yaml(content, MyType)
    assert not errors
    assert value == {"field_1": "value_1", "field_2": 2}
    content = yaml.dump({"field_1": "value_1", "field_2": "value_2"})
    value, errors = validate_yaml(content, MyType)
    assert errors
    assert errors[0].text == "Must be a valid integer."

# Generated at 2022-06-14 15:04:41.864714
# Unit test for function validate_yaml
def test_validate_yaml():
    try:
        import yaml
    except ImportError:
        raise unittest.SkipTest("Requires 'pyyaml' to be installed.")

    class PetSchema(Schema):
        name = Field(type=str, max_length=255)
        age = Field(type=int)

    value, messages = validate_yaml(
        b"""
        name: Cleo
        age: 8
        """,
        validator=PetSchema,
    )

    assert not isinstance(value, Token)
    assert value["name"] == "Cleo"
    assert value["age"] == 8
    assert messages == []



# Generated at 2022-06-14 15:04:49.428194
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "a: this is an example"
    validator = Field(name="a", kind="String")
    value, error_messages = validate_yaml(content, validator)
    assert error_messages == []
    assert value == {"a": "this is an example"}

    content = "a: this is an example\nb: this is another example"
    validator = Field(name="a", kind="String")
    value, error_messages = validate_yaml(content, validator)
    assert len(error_messages) == 1
    assert error_messages[0] == Message(
        message="Unrecognized property 'b'.",
        code="unrecognized_property",
        position=Position(column_no=3, line_no=1, char_index=16),
    )
    assert value

# Generated at 2022-06-14 15:04:56.653066
# Unit test for function validate_yaml
def test_validate_yaml():
    content = ""
    validator = Schema(
        {
            "name": "Person",
            "fields": {
                "name": {"type": "string"},
                "age": {"type": "number"},
            },
        }
    )

    value, errors = validate_yaml(content, validator)
    assert not value
    assert errors

    content = """
    name: Steve
    age: 14
    """

    value, errors = validate_yaml(content, validator)
    assert value
    assert not errors

# Generated at 2022-06-14 15:05:06.819433
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, fields
    from typesystem.tokenize.tokens import Token
    import yaml
    class Person(Schema):
        first_name = fields.String(required=True)
        last_name = fields.String(required=True)
        age = fields.Number(required=True)
        alive = fields.Boolean()
    yaml_text = 'first_name: "John"\nlast_name: "Doe"\nage: 45\nalive: true'
    assert validate_yaml(yaml_text, Person) == ({"first_name": "John", "last_name": "Doe", "age": 45.0, "alive": True}, None)
    yaml_text = 'first_name: {}'

# Generated at 2022-06-14 15:05:15.290080
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(content="hello", validator=Field(type="string")) == (
        "hello",
        [],
    )
    assert validate_yaml(content="42", validator=Field(type="integer")) == (42, [])
    assert validate_yaml(content="42.1", validator=Field(type="number")) == (
        42.1,
        [],
    )
    assert validate_yaml(content="true", validator=Field(type="boolean")) == (
        True,
        [],
    )
    assert validate_yaml(content="false", validator=Field(type="boolean")) == (
        False,
        [],
    )
    assert validate_yaml(content="null", validator=Field(type="null")) == (None, [])

# Generated at 2022-06-14 15:05:23.312417
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    test_content = '''
    test_content:
        key1: value1
        key2: value2
        key3:
            - one
            - two
            - three
        key4:
            key5: value5
            key6: value6
    '''
    test_token = tokenize_yaml(test_content)
    validator = Schema()
    assert validate_yaml(test_content, validator) == (test_token, None)

# Generated at 2022-06-14 15:05:36.463225
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    create a test schema and test it with the validate_yaml function
    """
    from typesystem import String, Integer, Schema
    from typesystem.validators import required

    class MySchema(Schema):
        name = String(validators=[required()])
        age = Integer(validators=[required()])

    content = """
    name: John
    age: 42
    """
    value, errors = validate_yaml(content, validator=MySchema)
    assert not errors
    assert value == {"name": "John", "age": 42}

    # ValidationError
    content = """
    name: John
    age: John
    """
    value, errors = validate_yaml(content, validator=MySchema)

# Generated at 2022-06-14 15:05:41.383390
# Unit test for function validate_yaml
def test_validate_yaml():
    class MovieSchema(Schema):
        title = String()
        year = Integer()

    movie_data = """
    title: Inception
    year: 2010
    """

    errors = validate_yaml(movie_data, MovieSchema)
    assert not errors, errors
    return


# Generated at 2022-06-14 15:05:49.511974
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class SomeSchema(Schema):
        some_field = String()

    content = b"some_field: foo"
    value, errors = validate_yaml(content, SomeSchema)

    assert value == {"some_field": "foo"}
    assert errors == []

    content = b"some_field: 123"
    value, errors = validate_yaml(content, SomeSchema)

    assert value == {"some_field": "123"}
    assert any("must be a string" in error.text for error in errors)
    assert any('mapping values are not allowed here' in error.text for error in errors)
    assert len(errors) == 2

# Generated at 2022-06-14 15:06:01.282521
# Unit test for function validate_yaml
def test_validate_yaml():
    # Make a copy of the YAML string, where we will incrementally remove characters
    # and observe the resulting position of the parse error. This is used to assert
    # that the position is updated correctly.
    content = """
    id: 123
    username: greg
    password: foobar
    """

    # Create a test User Schema with a custom validation method to trigger a
    # more user-friendly message in lieu of the default "invalid_type" message.
    class User(Schema):
        id = Integer()

        @validator(
            "password",
            message="Passwords must be at least eight characters in length.",
        )
        def validate_password_length(cls, v):
            return len(v) >= 8

    # Parse a valid User and assert that no error messages are raised.
    user, error_

# Generated at 2022-06-14 15:06:17.374933
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test a (working) validation.
    content = """
    first_name: "John"
    last_name: "Doe"
    """
    schema = Schema(fields={"first_name": String, "last_name": String})
    value, errors = validate_yaml(content, schema)
    assert not errors
    assert value["first_name"] == "John"
    assert value["last_name"] == "Doe"

    # Test a (failing) validation.
    content = """
    first_name: true
    last_name: 123
    """
    schema = Schema(fields={"first_name": String, "last_name": String})
    value, errors = validate_yaml(content, schema)