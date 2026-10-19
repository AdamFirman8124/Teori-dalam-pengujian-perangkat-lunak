

# Generated at 2022-06-14 14:56:29.298159
# Unit test for function validate_yaml
def test_validate_yaml():
    with open(os.path.join(os.path.dirname(__file__), '../data/example1.yaml'), 'r') as f:
        yaml_file = f.read()
        # print(yaml_file)

    field = Field(
        name="my_field",
        type="number",
    )

    # errors, data = validate_yaml(yaml_file, field)
    # print(errors)
    # print(data)


# Generated at 2022-06-14 14:56:36.752476
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test the basic YAML types.
    assert tokenize_yaml("123") == ScalarToken(123, 0, 2, content="123")
    assert tokenize_yaml("'abc'") == ScalarToken("abc", 0, 5, content="'abc'")
    assert tokenize_yaml("true") == ScalarToken(True, 0, 4, content="true")
    assert tokenize_yaml("false") == ScalarToken(False, 0, 5, content="false")
    assert tokenize_yaml("null") == ScalarToken(None, 0, 4, content="null")
    assert (
        tokenize_yaml("1.23")
        == ScalarToken(1.23, 0, 4, content="1.23")
    )  # 1.23, but not 12.3 (int)



# Generated at 2022-06-14 14:56:48.150059
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer, Boolean, Date, Object
    from typesystem.base import ValidationError
    
    class Person(Schema):
        name = String(minlength=2)
        age = Integer(minimum=0)
        favourite_maths_theorist = String(enum=["Euler", "Lagrange", "Galois"])
        dead = Boolean()
        date_of_birth = Date()
        complex_object = Object(fields={"number_of_legs": Integer()})


# Generated at 2022-06-14 14:56:57.490779
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test valid YAML.
    yaml_str1 = ""
    obj1 = tokenize_yaml(yaml_str1)
    print(obj1)
    assert obj1 == DictToken({}, 0, -1, content=yaml_str1)

    yaml_str2 = "{}"
    obj2 = tokenize_yaml(yaml_str2)
    print(obj2)
    assert obj2 == DictToken({}, 0, 1, content=yaml_str2)

    yaml_str3 = "{a: 1}"
    obj3 = tokenize_yaml(yaml_str3)
    print(obj3)
    assert obj3 == DictToken({"a": 1}, 0, 5, content=yaml_str3)


# Generated at 2022-06-14 14:57:00.523930
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("- a") == ListToken([ScalarToken("a", 1, 2, content="- a")], 0, 3, content="- a")



# Generated at 2022-06-14 14:57:04.428762
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml('''
    test: value
    list:
    - item1
    - item2
    ''')

    assert token == {
        'test': 'value',
        'list': ['item1', 'item2'],
    }



# Generated at 2022-06-14 14:57:10.902600
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("""{
    "a": "foo",
    "b": "bar",
    "c": [1, 2, 3]
}""") == {
        "a": "foo",
        "b": "bar",
        "c": [1, 2, 3]
    }
    assert tokenize_yaml("""[1, 2, 3]""") == [1, 2, 3]


# Generated at 2022-06-14 14:57:16.619309
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    value = tokenize_yaml('{hello: world, greeting: "Hi"}')
    assert isinstance(value, DictToken)
    assert isinstance(value.value['hello'], ScalarToken)
    assert isinstance(value.value['greeting'], ScalarToken)
    assert value.value['hello'].value == 'world'


# Generated at 2022-06-14 14:57:23.929075
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Test tokenize_yaml function.
    """
    content = """
    ---
    a:
        b: 1
        c: 2
    """
    result = tokenize_yaml(content)
    assert result.start == 4
    assert result.end == 55
    assert result.content == content
    assert result.items == [
        ("a", {"b": ScalarToken("1", 32, 33, content), "c": ScalarToken("2", 40, 41, content)})
    ]



# Generated at 2022-06-14 14:57:28.298939
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(tokenize_yaml('{"a": 1}'), DictToken)
    assert isinstance(tokenize_yaml('[{"a": 1}, 2]'), ListToken)
    assert isinstance(tokenize_yaml('2'), ScalarToken)



# Generated at 2022-06-14 14:57:35.953762
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "foo: bar"
    validator = Field(type="string")
    value, error_messages = validate_yaml(content=content, validator=validator)
    assert value == "bar"
    assert error_messages == []



# Generated at 2022-06-14 14:57:45.110527
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class UserSchema(Schema):
        name = String()

    # Good
    value, errors = validate_yaml("name: James\n", UserSchema)
    assert value == {"name": "James"}
    assert errors is None

    # Bad
    try:
        value, errors = validate_yaml("error: James\n", UserSchema)
    except ValidationError as e:
        error = e
    else:
        assert False, "ValidationError expected"
    assert len(error.messages) == 1
    assert isinstance(error.messages[0], Message)
    assert error.messages[0].text == "Unknown field name."

# Generated at 2022-06-14 14:57:55.252497
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    from typesystem.fields import String
    from tests.utils import noop_encoder

    class Profile(typesystem.Schema):
        name = String(max_length=20)

    content = """
    {
        name: "Joh"
    }
    """
    value, errs = validate_yaml(content, Profile)
    assert value is None
    assert len(errs) == 1
    assert isinstance(errs[0], ValidationError)
    assert errs[0].messages == [
        "value is too long (maximum is 20 characters)."
    ]
    assert errs[0].code == "too_long"
    assert errs[0].value == "Joh"
    assert errs[0].field.name == "name"

# Generated at 2022-06-14 14:58:01.220161
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "name: John"
    validator = Field(name="name", type="string")
    value, error_messages = validate_yaml(content=content, validator=validator)
    assert value == "John"
    assert len(error_messages) == 0

if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 14:58:10.840895
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.types import String, Dict
    # Empty content
    str_content = ''
    with pytest.raises(ParseError):
        validate_yaml(str_content, 'a')
    # int validator
    str_content = '1'
    assert validate_yaml(str_content, 1) == (1, [])
    str_content = '2'
    assert validate_yaml(str_content, 2) == (2, [])
    str_content = '3'
    assert validate_yaml(str_content, 2) == (3, [ValidationError('3', code='invalid_type')])
    # str validator
    str_content = 'cat'
    assert validate_yaml(str_content, 'cat') == ('cat', [])
    # list validator


# Generated at 2022-06-14 14:58:19.198422
# Unit test for function validate_yaml
def test_validate_yaml():
    # Example Schema for testing
    class PointSchema(Schema):
        x = fields.Integer(required=True)
        y = fields.Integer(required=True)

    # Test success
    content = 'x: 10\ny: 20'
    schema = PointSchema()
    _, errors = validate_yaml(content, schema)
    assert len(errors) == 0

    # Test failure
    content = 'x: 10\ny: "s"'
    schema = PointSchema()
    _, errors = validate_yaml(content, schema)
    assert len(errors) == 1

# Generated at 2022-06-14 14:58:26.416298
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    yaml_string = """
name: John
email: john@example.com
age: 28
    """
    class User(Schema):
        name = String(max_length=100)
        email = Email(max_length=100)
        age = Integer(minimum=1)

    user, messages = validate_yaml(yaml_string, User)
    assert user == {
        "name": "John",
        "email": "john@example.com",
        "age": 28
    }
    assert messages == []

# Generated at 2022-06-14 14:58:36.088698
# Unit test for function validate_yaml
def test_validate_yaml():
    yml = "foo: bar"
    value, errors = validate_yaml(yml, {"foo": str})
    assert errors is None
    assert value == {"foo": "bar"}

    yml = "foo: 1"
    value, errors = validate_yaml(yml, {"foo": int})
    assert isinstance(errors, typing.List)
    assert len(errors) == 1
    assert errors[0].text == "Not a valid integer."
    assert errors[0].code == "type_error"
    assert errors[0].position == Position(line_no=1, column_no=5, char_index=4)



# Generated at 2022-06-14 14:58:41.460780
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class CommentSchema(Schema):
        class Meta:
            strict = False

        body = String(max_length=100)

    input = "---\nbody: Hello world!\n"
    errors = validate_yaml(input, CommentSchema)
    assert isinstance(errors, list)
    assert len(errors) == 0



# Generated at 2022-06-14 14:58:53.020242
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Dict, Integer, String
    from typesystem.schemas import Schema

    class FooSchema(Schema):
        bar = Integer()
        spam = String()

    schema = FooSchema()
    yaml_str = "bar: 4\nspam: eggs"

    result, errors = validate_yaml(yaml_str, schema)
    assert errors == []

    yaml_str = "bar: 4\nspam: eggs\nfoo: 42"
    result, errors = validate_yaml(yaml_str, schema)

    assert [str(error) for error in errors] == [
        "Unrecognised field name: \"foo\"."
    ]

    # Test a more complete schema with a nested dict.
    class FooSchema(Schema):
        bar = Integer()


# Generated at 2022-06-14 14:59:08.456234
# Unit test for function validate_yaml
def test_validate_yaml():
    from unittest.mock import Mock

    from typesystem.base import ValidationError
    from typesystem.fields import Array, Boolean, Integer, Number, String
    from typesystem.schemas import Schema

    class Address(Schema):
        line1 = String(max_length=255)
        line2 = String(max_length=255, required=False, allow_blank=True)
        zip_code = String(max_length=10)
        city = String(max_length=255)

    class Employee(Schema):
        name = String(max_length=255)
        position = String(max_length=255)
        address = Address()
        hired = Boolean()
        age = Integer(min_value=18)
        score = Number(min_value=0)


# Generated at 2022-06-14 14:59:17.054805
# Unit test for function validate_yaml
def test_validate_yaml():
    title_schema = Schema(
        {"title": String(max_length=100)},
        unknown_fields="raise",
        missing_fields="raise",
    )
    data = """{
        "title": "Hello",
        "title2": "Hello"
    }"""
    try:
        validate_yaml(data, title_schema)
    except ValidationError as e:
        # print(e.error_message.text)
        assert e.error_message.text == "Unknown field in the data."
        assert isinstance(e.error_message, Message)
        assert e.error_message.position.line_no == 3 
        assert e.error_message.position.column_no == 12
        assert e.error_message.position.char_index == 52
    except:
        raise Assert

# Generated at 2022-06-14 14:59:22.234668
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Schema, Number, Boolean

    class UserSchema(Schema):
        name = String(required=True)
        age = Number()
        admin = Boolean(default=False)

    # Test valid YAML
    content = """name: "joe"
    age: 27
    admin: False
    """
    assert validate_yaml(content, UserSchema) == (
        {"name": "joe", "age": 27, "admin": False},
        [],
    )

    # Test parse error
    try:
        content = 'name: "joe"\n    age: 27\n    '
        validate_yaml(content, UserSchema)
    except ParseError as e:
        assert e.code == "parse_error"

# Generated at 2022-06-14 14:59:31.295047
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = "key: value"
    token = tokenize_yaml(content)
    assert token.get_value() == {'key': 'value'}
    assert token.start == 0
    assert token.end == 9
    assert token.content == "key: value"
    assert isinstance(token, DictToken)
    assert token[0].key == 'key'
    assert token[0].value == 'value'
    assert token[0].start == 0
    assert token[0].end == 9
    assert token[0].content == "key: value"
    assert isinstance(token[0], ScalarToken)


# Generated at 2022-06-14 14:59:43.813564
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test if it can pass a regular YAML file, and return value and empty list of error messages.
    YAML_FILE_CONTENT = """
        location:
            country: Germany
            city: Düsseldorf
        """
    from typesystem import Schema
    from typesystem import fields

    class TestSchema(Schema):
        location = fields.Dict(
            {
                "country": fields.String(max_length=100),
                "city": fields.String(max_length=100),
            }
        )

    value, error_messages = validate_yaml(YAML_FILE_CONTENT, TestSchema)
    # Error_messages should be an empty list
    assert not error_messages

    # Test if it can handle a YAML file with a parse error,  and return

# Generated at 2022-06-14 14:59:52.080500
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test if the schema is not valid
    import yaml
    from yaml.loader import SafeLoader

    class CustomSafeLoader(SafeLoader):
        pass

    class MySchema(Schema):
        firstname = Field(str, required=True)
        lastname = Field(str, required=False)
        age = Field(int, required=True)
        is_happy = Field(bool, required=False)

    content = yaml.load(
        """
data:
  firstname: 'Jane'
  lastname: 'Doe'
  age: '20'
  is_happy: true
"""
    )

    # Should return a valid value and error message
    token = tokenize_yaml(content)
    value, error_messages, valid_data = validate_with_positions(token, MySchema)

# Generated at 2022-06-14 15:00:02.222550
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        a = "integer"
        b = "string"
        c = "number"

    content = """
    a: 1
    b: "b"
    d: 2
    """
    value, error_messages = validate_yaml(content, TestSchema)
    assert error_messages == [
        Message(
            text="'c' is a required field.",
            code="missing_field",
            position=Position(column_no=5, line_no=3, char_index=12),
        ),
        Message(
            text="'d' is not a valid field.",
            code="invalid_field",
            position=Position(column_no=5, line_no=4, char_index=18),
        ),
    ]

# Generated at 2022-06-14 15:00:14.160620
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        name = fields.String(max_length=100)
        age = fields.Integer(min_value=0, max_value=100)
        joined = fields.DateTime()
        admin = fields.Boolean()

    content = """
{
  name: 'John Smith',
  age: 34,
  joined: '2019-09-16T13:29:13+00:00',
  admin: true
}
    """
    value, errors = validate_yaml(content, UserSchema)
    assert value == {
        'name': 'John Smith',
        'age': 34,
        'joined': datetime.datetime(2019, 9, 16, 13, 29, 13, tzinfo=datetime.timezone.utc),
        'admin': True,
    }, value

# Generated at 2022-06-14 15:00:19.497601
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.base import ValidationError
    from typesystem.fields import Integer, String

    content = """
name: John
age: 35
"""

    try:
        validate_yaml(content, String())
    except ValidationError as e:
        print(e.messages)


# Generated at 2022-06-14 15:00:26.157881
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml

    class Pet(Schema):
        name = "string"
        age = "number"

    class Person(Schema):
        first_name = Field("string")
        last_name = Field("string")
        pets = Field(Array[Pet])

    data = '{"first_name": "bob", "last_name": "smith", "pets": [{"name": "dog", "age": 5}]}'

    if not isinstance(data, bytes):
        data = data.encode("utf-8")


# Generated at 2022-06-14 15:00:30.489182
# Unit test for function validate_yaml
def test_validate_yaml():
    content = ""
    validator = Field()
    assert True



# Generated at 2022-06-14 15:00:39.595803
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b"""
        description: Just a description
        nested:
          some_number: 1
          list:
            - first
            - second
    """
    validator = Field({
        "description": Field(str),
        "nested": Field({
            "some_number": Field(int),
            "list": Field([str])
        })
    })

    value, error_messages = validate_yaml(content, validator)
    assert value == {
        'description': 'Just a description',
        'nested': {
            'some_number': 1,
            'list': ['first', 'second']
        }
    }
    assert error_messages == []



# Generated at 2022-06-14 15:00:48.571266
# Unit test for function validate_yaml
def test_validate_yaml():
    # validator test
    validator = Field(format="string")
    validator_test = lambda content:validate_yaml(content,validator)
    assert validator_test('"123"') == ('123', [])
    
    # content test
    content = '{"key1":"value1","key2":"value2"}'
    validator = Field(name="key3", format="string")
    test = lambda :validate_yaml(content, validator)
    assert test() == (None, [Message(text="Key 'key3' is required.", code="required", position=Position(char_index=0, column_no=1, line_no=1))])

# Generated at 2022-06-14 15:01:00.740309
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """\
    - one: uno
    - two: dos
    - three: tres
    """
    expected = [
        {"one": "uno"},
        {"two": "dos"},
        {"three": "tres"},
    ]
    (value, error_messages) = validate_yaml(content, List(Dict({"one": Text(), "two": Text(), "three": Text()})))
    assert value == expected
    assert error_messages == []

    content = """\
    ---
    - one: uno
    - two: dos
    - three: tres
    """
    expected = [
        {"one": "uno"},
        {"two": "dos"},
        {"three": "tres"},
    ]

# Generated at 2022-06-14 15:01:08.141675
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = (
        "# Sample YAML\n"
        "key: value\n"
        "list:\n"
        "  - a\n"
        "  - b\n"
        "more:\n"
        "  list:\n"
        "    - c\n"
    )
    assert tokenize_yaml(content) == {
        "key": "value",
        "list": ["a", "b"],
        "more": {"list": ["c"]},
    }



# Generated at 2022-06-14 15:01:11.918890
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String

    content = """
    slug: some-slug
    title: Some Title
    """

    errors = validate_yaml(content, String(max_length=10))
    assert len(errors) == 2
    assert errors[0].code == "max_length"
    assert errors[1].code == "max_length"

# Generated at 2022-06-14 15:01:21.307041
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_content = """
        - foo
        - 0
        - 3.14
        - null
        - false
        - true
    """

# Generated at 2022-06-14 15:01:33.108344
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, String
    from typesystem.schemas import Schema

    simple_schema = Schema({"a": Integer(), "b": String()})

    def test_case(content, expected_value, expected_errors):
        value, errors = validate_yaml(content, simple_schema)
        assert value == expected_value
        assert errors == expected_errors

    test_case(
        """
        a: 10
        b: hello
        """,
        {"a": 10, "b": "hello"},
        [],
    )

# Generated at 2022-06-14 15:01:43.637139
# Unit test for function validate_yaml
def test_validate_yaml():
    class ProductSchema(Schema):
        id = IntegerField()
        name = StringField()

    content = "id: 42\nname: \"Python\"\n"
    assert validate_yaml(content=content, validator=ProductSchema) == (
        {"id": 42, "name": "Python"},
        [],
    )

    content = "invalid-yaml"
    value, errors = validate_yaml(content=content, validator=ProductSchema)
    assert value is None
    assert errors == [
        Message(
            text="mapping values are not allowed here",
            code="parse_error",
            position=Position(
                char_index=0, line_no=1, column_no=0
            ),
        )
    ]

# Generated at 2022-06-14 15:01:54.597782
# Unit test for function validate_yaml
def test_validate_yaml():
    class ExampleSchema(Schema):
        title = Field(required=True)
        age = Field(validators=[lambda value: value >= 16])

    yaml_str = "title: John Doe\nage: 15"

    value, error_messages = validate_yaml(yaml_str, ExampleSchema)

    assert value is None
    assert len(error_messages) == 1
    assert error_messages[0].text == "Must be greater than or equal to 16."
    assert error_messages[0].position.line_no == 2
    assert error_messages[0].position.column_no == 5
    assert error_messages[0].position.char_index == 16



# Generated at 2022-06-14 15:02:00.856606
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''test: "string"'''
    token = tokenize_yaml(content)
    assert type(token) == DictToken
    results = validate_yaml(content, Schema)

# Generated at 2022-06-14 15:02:11.172610
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml("123", Field(name="yaml", type="integer")) == (123, [])
    assert validate_yaml("123", Field(name="yaml", type="string")) == (
        None,
        [
            Message(
                code="parse_error",
                level="error",
                position=Position(
                    line_no=1, column_no=1, char_index=0,
                ),
                text="Expected a string but got a number",
            )
        ],
    )

# Generated at 2022-06-14 15:02:21.966494
# Unit test for function validate_yaml
def test_validate_yaml():
    # Valid case
    valid = """
    name: "Test"
    age: 24
    """

    class Person(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0, maximum=100)

    schema = Person()
    assert validate_yaml(content=valid, validator=schema) == ({'name': 'Test', 'age': 24}, [])

    # Invalid case
    invalid = """
    name: "Test"
    age: 200
    """

    schema = Person()
    assert validate_yaml(content=invalid, validator=schema) == (None, [Message(text='Value is too large.', field='age', code='maximum', position=Position(column_no=7, line_no=3, char_index=14))])

# Generated at 2022-06-14 15:02:32.632960
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Tests the validate_yaml function in the tokenize module.
    """
    # Test no content
    content = ""  # type: str
    validator = Field(type=str)
    value, error_messages = validate_yaml(content, validator)
    assert value is None
    assert isinstance(error_messages, list)
    assert isinstance(error_messages[0], Message)
    assert len(error_messages) == 1
    assert error_messages[0].text == "No content."
    assert error_messages[0].code == "no_content"
    assert error_messages[0].position == Position(1, 1, 0)

    # Test invalid input
    content = "["  # type: str
    validator = Field(type=str)
    value, error_

# Generated at 2022-06-14 15:02:44.192751
# Unit test for function validate_yaml
def test_validate_yaml():
    # Link for reference: https://github.com/Yelp/typesystem/blob/master/tests/test_tokenize/test_yaml.py
    class YAMLSchema(Schema):
        foo = "string"
        bar = "number"

    class YAMLSchema2(Schema):
        foo = "number"

    assert validate_yaml(content="", validator=YAMLSchema) == ({}, [])
    assert validate_yaml(content="\x1b", validator=YAMLSchema) == ({}, [])
    assert validate_yaml(content="\n", validator=YAMLSchema) == ({}, [])
    assert validate_yaml(content=" ", validator=YAMLSchema) == ({}, [])

# Generated at 2022-06-14 15:02:52.637552
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    yaml_str = '{"hello": 2}'
    value, errors = validate_yaml(yaml_str, {
        "hello": typing.List([typing.Dict({
            "id": typing.Str(),
            "name": typing.Str(),
            "age": typing.Int()
        })]),
        "world": "123"
    })
    print(value)
    print(errors)

if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 15:02:54.909599
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "000"
    validator = IntegerField()
    
    assert validate_yaml(content, validator) == ('0', [])

# Generated at 2022-06-14 15:03:01.103129
# Unit test for function validate_yaml
def test_validate_yaml():
    teststring = '''
        student_number: 42
        first_name: John
        last_name: Doe
        courses:
            - course_id: 12345
              course_name: "Data Science"
              semester: 1
              year: 2018
              credits: 7
            - course_id: 67890
              course_name: "Machine Learning"
              semester: 1
              year: 2018
              credits: 5'''

    ps = PersonSchema()
    ps.validate(teststring)
    assert ps.errors == []



# Generated at 2022-06-14 15:03:05.604602
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
        a:
          c: 1
          d: 2
        b: 3
    """
    assert tokenize_yaml(content).to_primitive() == {
        "a": {"c": 1, "d": 2},
        "b": 3,
    }



# Generated at 2022-06-14 15:03:12.092263
# Unit test for function validate_yaml
def test_validate_yaml():

    class CaseSchema(Schema):
        numbers = Fields.List(Fields.Integer())
        title = Fields.String(required=True)

    class EventSchema(Schema):
        case = Fields.Schema(CaseSchema)
        date = Fields.String()

    yaml_str = """
    date: 2018-03-04
    case:
      title: "My Case"
      numbers: [1, 2, 3]
    """

    good_data = CaseSchema(
        {"title": "My Case", "numbers": [1, 2, 3]}, id="", model_name="", database=None
    )
    # print(good_data.to_primitive())
    assert validate_yaml(yaml_str, CaseSchema) == (good_data, [])

    # List field with bad

# Generated at 2022-06-14 15:03:25.858271
# Unit test for function validate_yaml
def test_validate_yaml():
    import json

    # Import test fixtures
    from .fixtures.yaml_serialization import (
        serialized_types,
        serialized_schema,
        serialized_partial_schema,
    )
    from .fixtures.yaml_errors import serialized_errors

    # Import fixtures
    from .fixtures.types import types
    from .fixtures.schema import schema
    from .fixtures.partial_schema import partial_schema

    errors = {}

    def make_token_error(token, field):
        return Message(
            text="Invalid value.",
            code="invalid",
            field=field,
            position=token.get_position(),
        )

    for type_name, type_validator in types.items():
        serialized_type = serialized_types[type_name]
       

# Generated at 2022-06-14 15:03:31.061945
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        name = String()
        age = Integer()

    content = """
    name: Jane
    age:  J
    """
    value, error_messages = validate_yaml(content=content, validator=UserSchema)
    assert value is None
    assert error_messages[0] == "Expected integer value."



# Generated at 2022-06-14 15:03:40.022709
# Unit test for function validate_yaml
def test_validate_yaml():
    def test_parse():
        assert validate_yaml("", typesystem.String()) == ("", [])
        assert validate_yaml("null", typesystem.Null()) == (None, [])
        assert validate_yaml("1", typesystem.Integer()) == (1, [])
        assert validate_yaml("1.1", typesystem.Number()) == (1.1, [])
        assert validate_yaml("true", typesystem.Boolean()) == (True, [])
        assert validate_yaml("false", typesystem.Boolean()) == (False, [])
        assert validate_yaml("1.1", typesystem.Boolean()) == (True, [])
        assert validate_yaml("hello", typesystem.Boolean()) == (False, [])

# Generated at 2022-06-14 15:03:49.603714
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    good_input = "hi: 'there'"
    expected_output = {'hi': "there"}
    output = tokenize_yaml(good_input)
    assert output == expected_output

    bad_input = "hi: there"
    with pytest.raises(ParseError) as excinfo:
        tokenize_yaml(bad_input)
    assert str(excinfo.value) == 'Unexpected end of YAML input.'

    another_bad_input = 'hi: "there"'
    with pytest.raises(ParseError) as excinfo:
        tokenize_yaml(another_bad_input)
    assert str(excinfo.value) == 'Unable to parse YAML content.'

# Generated at 2022-06-14 15:03:50.190017
# Unit test for function validate_yaml
def test_validate_yaml():
    pass

# Generated at 2022-06-14 15:03:58.804517
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem.fields import String, Integer, Array, Boolean

    def assert_valid_with_value(content: str, value: typing.Any):
        assert validate_yaml(content, String()) == (value, [])

    def assert_invalid_with_message(content: str, message: Message):
        assert validate_yaml(content, String())[1] == [message]

    def assert_valid_with_integer(content: str, value: int):
        assert validate_yaml(content, Integer()) == (value, [])

    def assert_valid_with_array(content: str, value: typing.List[str]):
        assert validate_yaml(content, Array(of=String())) == (value, [])


# Generated at 2022-06-14 15:04:09.949757
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import sys
    import os

    sys.path.append(os.path.dirname(__file__))

    from typesystem.tokenize import tokenize_yaml

    token = tokenize_yaml('{"name": "Michael"}')
    assert token.value == {'name': 'Michael'}

    token = tokenize_yaml('[1, 2, 3]')
    assert token.value == [1, 2, 3]

    token = tokenize_yaml('"Michael"')
    assert token.value == 'Michael'

    token = tokenize_yaml('100')
    assert token.value == 100

    token = tokenize_yaml('100.5')
    assert token.value == 100.5

    token = tokenize_yaml('true')
    assert token.value == True

    token = tokenize_

# Generated at 2022-06-14 15:04:20.068539
# Unit test for function validate_yaml
def test_validate_yaml():
    class Question(Schema):
        text = fields.String(required=True)

    class Survey(Schema):
        question = fields.Object(fields.Instance(Question), required=True)

    content = """
    {
        "question": {
            "text": 42
        }
    }
    """

    value, error_messages = validate_yaml(content, Survey)

    assert value is None
    assert error_messages == [
        Message(
            text="Value must be a string.",
            code="must_be_string",
            name="text",
            position=Position(
                line_no=4,
                column_no=21,
                char_index=63,
            ),
        ),
    ]

# Generated at 2022-06-14 15:04:25.436437
# Unit test for function validate_yaml
def test_validate_yaml():
    names = Field(type=str)
    schema = Schema(names=names)
    value, errors = validate_yaml(b"names: ['John', 'Doe']", schema)
    assert errors[0].position == Position(column_no=8, line_no=1, char_index=7)
    assert errors[0].code == 'expecting_primary_data_type'
    assert errors[0].text == 'Expecting primary data type.'



# Generated at 2022-06-14 15:04:32.526483
# Unit test for function validate_yaml
def test_validate_yaml():

    class TestSchema(Schema):
        name = "Test Schema"
        foo = Field(type="string")
        bar = Field(type="integer")

    assert TestSchema.validate(yaml="foo: bar\nbar: 1") == (
        {"foo": "bar", "bar": 1},
        [],
    )

    assert TestSchema.validate(yaml=b"foo: bar\nbar: 1") == (
        {"foo": "bar", "bar": 1},
        [],
    )


# Generated at 2022-06-14 15:04:43.558016
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    schema = yaml.load("""
    type: object
    properties:
      name: {type: string, max_length: 5}
    """, Loader=yaml.SafeLoader)
    with open('test/test_samples/invalid_config.yaml') as f:
        value, errors = validate_yaml(f, schema)
    assert len(errors) == 1
    error = errors[0]
    assert error.text == 'Ensure this value has at most 5 characters (it has 6).'
    assert error.position == Position(line_no=6, column_no=3, char_index=5)

# Generated at 2022-06-14 15:04:51.392301
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "hello: world"
    field = Field(description="description", name="name", type=["array", "null"])
    assert validate_yaml(content, field)  # type: ignore
    class TestSchema(Schema):
        name = Field(description="description", name="name", type=["array", "null"])
    assert validate_yaml(content, TestSchema)  # type: ignore



# Generated at 2022-06-14 15:04:56.418766
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String
    from typesystem.schemas import Schema

    def test_func():
        schema = Schema({"name": String()})
        yaml_str = """hello: world"""
        value, errors = validate_yaml(yaml_str, schema)

        assert value["name"] == "world"
        assert len(errors) == 0

    test_func()



# Generated at 2022-06-14 15:05:06.627016
# Unit test for function validate_yaml
def test_validate_yaml():
    class SimpleSchema(Schema):
        name = String()
        age = Integer()

    content = "name: Joe\nage: 40"

    result = validate_yaml(content=content, validator=SimpleSchema)
    assert result[0] == {"name": "Joe", "age": 40}

    errors = result[1]
    assert errors[0].text == "not a valid string."
    assert errors[0].code == "type"
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no == 5
    assert errors[0].position.char_index == 4

    content = """
    name: Joe
    age: not_an_integer
    """

    result = validate_yaml(content=content, validator=SimpleSchema)


# Generated at 2022-06-14 15:05:15.102337
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema

    class SimpleSchema(Schema):
        name = "string"

    schema = SimpleSchema()

    assert validate_yaml(b"name: foo", schema) == ({"name": "foo"}, [])
    assert validate_yaml(b"name: 1", schema) == (None, [])

    errors = validate_yaml(b"name: 1", schema)[1]
    assert isinstance(errors[0], ValidationError)
    assert errors[0].code == "type_error.string"

    simple_errors = [error for error in errors if not isinstance(error, Message)]
    assert len(simple_errors) == 1

    error = simple_errors[0]
    assert error.text == "Must be of type 'string'."

# Generated at 2022-06-14 15:05:25.512046
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None
    from typesystem.types import String

    validator = String()

    assert validate_yaml("test: value", validator) == (
        {"test": "value"},
        [],
    )

    errors = [
        Message(
            code="type_error",
            position=Position(column_no=4, char_index=4, line_no=1),
            text='Expected type "string" but got "null".',
        )
    ]

    assert validate_yaml("test: null", validator) == ({}, errors)

    errors = validate_yaml("test: null", validator)[1]
    assert errors[0].position.line_no == errors[0].position.column_no
    assert validate_yaml("test: null", validator) == ({}, errors)



# Generated at 2022-06-14 15:05:34.477727
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''name: "Stephanie"'''
    schema = '''
    name: {type: string, required: True}
    '''
    with open("schema.yml", "w") as f:
        f.write(schema)

    class TestSchema(Schema):
        pass

    schema = TestSchema.from_file("schema.yml")

    value, errors = validate_yaml(content, schema)
    assert not errors
    assert value["name"] == "Stephanie"



# Generated at 2022-06-14 15:05:45.511715
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("") == ScalarToken("", 0, 0, content="")
    assert tokenize_yaml("1") == ScalarToken("1", 0, 0, content="1")
    assert tokenize_yaml("1.1") == ScalarToken("1.1", 0, 3, content="1.1")
    assert tokenize_yaml("true") == ScalarToken("true", 0, 3, content="true")
    assert tokenize_yaml("null") == ScalarToken("null", 0, 3, content="null")
    assert tokenize_yaml("key: value") == DictToken(
        {"key": "value"}, start=0, end=9, content="key: value"
    )

# Generated at 2022-06-14 15:05:52.530135
# Unit test for function validate_yaml
def test_validate_yaml():
    try:
        from typesystem.fields import String, Integer, Boolean, Datetime, DateTime, Date
        from datetime import datetime
    except ImportError:  # pragma: no cover
        # Skip this test if the module isn't installed both in unit tests and in doc tests.
        return
    import pytest

    class TestSchema(Schema):
        name = String(max_length=10)
        age = Integer(minimum=0)
        is_employee = Boolean(default=True)
        last_visit = Date(default=datetime(2019, 1, 15))

    value, errors = validate_yaml(b'{"name": "John Doe", "age": 42}', TestSchema)


# Generated at 2022-06-14 15:06:03.720574
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(
        {
            "title": Field(str),
            "authors": Field([{'firstName': Field(str), 'lastName': Field(str)}]),
            "price": Field(int),
            "inStock": Field(bool, default=True)
        }
    )
    content = """
    ---
    title: Introduction to Algorithms
    authors:
      - firstName: Thomas
        lastName: Cormen
      - firstName: Charles
        lastName: Leiserson
      - firstName: Ronald
        lastName: Rivest
      - firstName: Clifford
        lastName: Stein
    price: 4.99
    inStock: true
    """
    result = validate_yaml(content, schema)
    assert result.errors == []