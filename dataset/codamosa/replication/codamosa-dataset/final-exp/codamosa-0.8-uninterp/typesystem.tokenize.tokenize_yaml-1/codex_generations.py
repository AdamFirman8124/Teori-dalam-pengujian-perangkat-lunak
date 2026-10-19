

# Generated at 2022-06-14 14:56:30.517847
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        id = Integer()
        name = String()

    content = """
    - id: 1
      name: Jane Doe
    - id: 2
      name: John Doe
    """

    errors = validate_yaml(content, validator=List(Person))
    assert errors == []

    content = "foo: bar"

    errors = validate_yaml(content, validator=Dict({}))
    assert errors == []

    content = "123"

    errors = validate_yaml(content, validator=Integer())
    assert errors == []

    content = "true"

    errors = validate_yaml(content, validator=Boolean())
    assert errors == []

    content = "123.456"

    errors = validate_yaml(content, validator=Float())
    assert errors == []

# Generated at 2022-06-14 14:56:38.377440
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test a valid document.
    assert validate_yaml(content="test: yaml", validator={"test": "string"}) == (
        {"test": "yaml"},
        [],
    )

    # Test a YAML parse error.
    try:
        validate_yaml(content="!! ", validator={})
    except ParseError as exc:
        assert exc.position.line_no == 1
        assert exc.position.column_no == 1
        assert exc.position.char_index == 0
        assert exc.text == "could not find expected ':'."
        assert exc.code == "parse_error"
    else:
        raise AssertionError("ParseError not raised.")

    # Test a validation error on a scalar value.

# Generated at 2022-06-14 14:56:49.362055
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(tokenize_yaml("{}"), DictToken)
    assert isinstance(tokenize_yaml("{a: 5}"), DictToken)
    assert isinstance(tokenize_yaml("[5,5]"), ListToken)
    assert isinstance(tokenize_yaml("5.5"), ScalarToken)
    assert isinstance(tokenize_yaml('"5"'), ScalarToken)
    assert isinstance(tokenize_yaml("True"), ScalarToken)
    assert isinstance(tokenize_yaml("null"), ScalarToken)
    assert isinstance(tokenize_yaml("null"), ScalarToken)
    assert isinstance(tokenize_yaml("{}"), DictToken)
    assert isinstance(tokenize_yaml("{a: 5}"), DictToken)

# Generated at 2022-06-14 14:56:58.395053
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content_yaml = """\
        a: 1
        b: 2
        c: 3
        d:
            e: 4
            f: 5
        """
    token = tokenize_yaml(content=content_yaml)

    assert isinstance(token, DictToken)
    assert token.value == {"a": 1, "b": 2, "c": 3, "d": {"e": 4, "f": 5}}
    assert token.start == 0
    assert token.end == len(content_yaml) - 1
    assert token.content == content_yaml

    # Test empty string tokenization
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml(content="")

    assert exc_info.value.position.char_index == 0

# Generated at 2022-06-14 14:57:07.070095
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Tests old_tokenize_yaml function
    """
    token = tokenize_yaml("key_string: value")
    assert type(token) == DictToken
    token = tokenize_yaml("- 1")
    assert type(token) == ListToken
    token = tokenize_yaml("- 1")
    assert type(token) == ListToken
    token = tokenize_yaml("1")
    assert type(token) == ScalarToken
    token = tokenize_yaml("key_int: 1")
    assert type(token) == DictToken
    token = tokenize_yaml("key_float: 1.2")
    assert type(token) == DictToken
    token = tokenize_yaml("key_bool: True")
    assert type(token) == DictToken

# Generated at 2022-06-14 14:57:17.968824
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    yaml_string = """\
a:
  b: true
  c: false
  d: null
  e: !!int '1234'
  f: !!float '1.234'
  g: 2019-11-12
  h: 12:00:00
  i: !!str 'hello'
k:
    - "a"
    - !!str "b"
    - !!str 'c'
    - !!str "d"
    - e
    - !!str f
    - g
    - h
    - 1
    - true
    - false
    - null
l:
  m:
    - !!str "a"
    - 1
    - true
    - false
    - null
o: "value"
"""
    tokens = tokenize_yaml(yaml_string)

# Generated at 2022-06-14 14:57:20.635083
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    with open('test_data/pet.yaml', 'r') as myfile:
        data=myfile.read()
    token = tokenize_yaml(data)


# Generated at 2022-06-14 14:57:26.260025
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = validator = type("MyValidator", (Schema,), {"name": str, "age": int})
    content = b"""
        name: bob
        age: 22
    """
    value, error_messages = validate_yaml(content, schema)
    assert value == {"name": "bob", "age": 22}
    assert error_messages == []



# Generated at 2022-06-14 14:57:37.750724
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test that a missing integer field is correctly parsed
    content = """
    name: John Smith
    age: 
    """
    validator = Schema([Field(name="name"), Field(name="age", type="integer")])
    value, error_messages = validate_yaml(content, validator)
    solution = (
        {
            "name": "John Smith",
            "age": None,
        },
        [
            ValidationError(
                text='Value '' is not of type "integer"',
                code="invalid_type",
                fields=["age"],
                position=Position(
                    line_no=3, column_no=5, char_index=content.index("")
                ),
            )
        ],
    )
    assert value == solution[0]
    assert error_messages == solution

# Generated at 2022-06-14 14:57:44.336518
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        first = Field(str)
        last = Field(str)
    
    content = "first: Dave\nlast: Heywood"
    value, messages = validate_yaml(content, Person)
    message = messages[0]
    assert "parse_error" == message.code
    assert 3 == message.position.line_no
    assert 6 == message.position.column_no
    assert 13 == message.position.char_index
    assert "'Dave'" == message.token
    assert "\"last\" is a required field." == message.text



# Generated at 2022-06-14 14:57:56.175263
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    token = tokenize_yaml("""---
name: John Doe
age: 42
"""
    )
    validator = Schema(
        fields = {
            "name": Field(type="string"),
            "age": Field(type="integer")
        }
    )
    assert validate(token, validator) == [{'name': 'John Doe', 'age': 42}]
    
    validator = Schema(
        fields = {
            "name": Field(type="string"),
            "age": Field(type="integer"),
            "address": Field(type="string")
        }
    )
    assert validate(token, validator) == 'NOT VALID'

# Generated at 2022-06-14 14:58:07.913021
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, fields, types
    from typesystem.datetime import Date
    import yaml
    from typesystem.exceptions import ValidationError


# Generated at 2022-06-14 14:58:18.159172
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = Field(type="string")

    values, errors = validate_yaml(
        """
        name: Mike
        """.strip(),
        PersonSchema,
    )

    assert len(errors) == 0

    values, errors = validate_yaml(
        """
        name: {}
        """.strip(),
        PersonSchema,
    )

    assert len(errors) == 1
    assert errors == [
        ValidationError(
            message=Message(
                text="Must be a string.",
                code="type_error.string",
                position=Position(line_no=2, column_no=4, char_index=10),
            ),
            field_name="name",
            data={},
        )
    ]

# Generated at 2022-06-14 14:58:27.487550
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, Object
    from typesystem.schemas import Schema

    validator = Object.of({"a": Integer(), "b": Integer()})
    content = "a: 1"  # Missing "b".

    value, error_messages = validate_yaml(content, validator)
    assert value is None
    assert error_messages == [Message("Missing value.", code="missing", position=Position(line_no=1, column_no=3, char_index=2))]

    content = "a: 1\nb: true"  # Field "b" is not an Integer.
    value, error_messages = validate_yaml(content, validator)
    assert value is None

# Generated at 2022-06-14 14:58:39.407985
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema, fields
    from typesystem.validators import max_length
    from typesystem.utils.string_utils import to_camel_case


    class PersonSchema(Schema):
        """
        Example schema with validation and positional error messages.
        """

        first_name = fields.String(
            validate=max_length(10),
            default_validators=["not_blank"],
        )
        last_name = fields.String(
            validate=max_length(10),
            default_validators=["not_blank"],
        )


    schema = PersonSchema()
    content = """
        first_name: "Anthony"
        last_name: "Byrne"
    """
    value, error_messages = validate_yaml(content, schema)

# Generated at 2022-06-14 14:58:52.361177
# Unit test for function validate_yaml
def test_validate_yaml():
    assert (
        validate_yaml(
            "validate_yaml",
            Field(deserialize_from=["validate_yaml"], validators=[]),
        )[0]
        is not None
    )
    assert validate_yaml(
        "validate_yaml", Field(deserialize_from=["validate_yam"], validators=[])
    )[1][0].position.column_no == 12
    assert validate_yaml(
        {"validator": "validate_yaml"}, Schema(fields={"validator": []})
    )[0]["validator"] == "validate_yaml"
    assert validate_yaml({"validator": "validate_yaml"}, Schema(fields={"validateu": []}))[
        1
    ][0].position

# Generated at 2022-06-14 14:59:04.694869
# Unit test for function validate_yaml
def test_validate_yaml():
    # unit test for validate_yaml

    class MySchema(Schema):
        name = "string"
        age = "integer"
        active = "boolean"

    class MySchemaWithOptional(Schema):
        name = "string"
        age = "integer"
        active = "boolean"
        optional_value = "string()"

    yaml_data_ok_no_optional = "name: John Doe\nage: 45\nactive: true"
    yaml_data_ok_with_whitespace = "  name: John Doe   \n   age: 45 \n  active: true   "
    yaml_data_ok_with_optional = (
        "name: John Doe\nage: 45\nactive: true\noptional_value: cool_word"
    )
    yaml_

# Generated at 2022-06-14 14:59:11.030179
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer

    content = """
    - 1
    - 2
    """
    schema = Integer()
    parsed_result, error_messages = validate_yaml(content=content, validator=schema)
    assert parsed_result == [1, 2]
    assert isinstance(error_messages, list)
    assert isinstance(error_messages[0], ValidationError)

# Generated at 2022-06-14 14:59:20.105061
# Unit test for function validate_yaml
def test_validate_yaml():
    print('test_validate_yaml')
    content = '''
        name: foo
        location:
            x: 0
            y: 0
            z: 0
    '''
    class PointSchema(Schema):
        x = Integer(required=True)
        y = Integer(required=True)
        z = Integer(required=True)

    class PlaceSchema(Schema):
        name = String(required=True)
        location = PointSchema(required=True)

    # Validates and fails with positional error messages
    value, messages = validate_yaml(content, validator=PlaceSchema)
    print('value:', value)
    print('messages:', messages)



# Generated at 2022-06-14 14:59:30.941930
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "name: 'x'\n"
    validator = Schema({'name': str})

    value, messages = validate_yaml(content, validator)
    # Expected the value is {'name': 'x'}, and error message is empty
    assert value == {'name': 'x'}
    assert len(messages) == 0

    content = "name: 123\n"
    validator = Schema({'name': str})

    value, messages = validate_yaml(content, validator)
    # Expected the value is None, and error message is not empty.
    assert not value
    assert len(messages) != 0
    # The error message is str type
    assert isinstance(messages[0].text, str)

# Generated at 2022-06-14 14:59:45.826782
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    schema = Schema({"name": {"type": "string"}})
    expect_error_message = Message(
        text="No content.",
        code="no_content",
        position=Position(
            line_no=1,
            column_no=1,
            char_index=0,
        ),
    )
    error_messages = validate_yaml(content="", validator=schema)

    assert error_messages == [expect_error_message]
    error_messages = validate_yaml(content="---\n", validator=schema)

    assert error_messages == [expect_error_message]
    value, error_messages = validate_yaml(content="--- {}", validator=schema)



# Generated at 2022-06-14 14:59:57.565478
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    class YAMLDocSchema(Schema):
        name = "YAMLDocSchema"
        description = "A YAML document representation for unit testing."

# Generated at 2022-06-14 15:00:04.800398
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test the `validate_yaml` function.

    """
    import typing
    import typesystem
    from datetime import date
    from typesystem import date as typesystem_date
    from typesystem import required
    from typesystem.schemas import Schema
    from typesystem.tokenize.positional_validation import validate_with_positions
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken, Token

    # Example schema to validate against.
    class UserSchema(Schema):
        name = typesystem.String(max_length=40)
        email = typesystem.String(format="email")
        items = typesystem.Array(items=typesystem.String(max_length=100))

    # Example YAML and expected output.

# Generated at 2022-06-14 15:00:15.891878
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Boolean, Integer

    class MySchema(Schema):
        foo = Integer(minimum=1)
        # this validation rule should cause an error in the YAML
        bar = Integer(maximum=1)
        baz = Boolean()

    # yaml_validate_yaml
    #
    # Validate YAML data against a schema, catching and analyzing error output.

    # First test that a valid YAML document parses and validates
    yaml_content = "- 1"
    value, errors = validate_yaml(yaml_content, validator=MySchema)
    assert value == [1]  # type: ignore
    assert errors == []

    # Now test that invalid YAML causes a parse error
    # This is defined outside the function because it is too long for a test docstring
    bad_

# Generated at 2022-06-14 15:00:25.946577
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem.fields import String

    # test both string and bytes
    for content in [
        b"foo: bar\n",
        'foo: bar\n',
    ]:
        value, messages = validate_yaml(content, String())
        assert value == 'bar'
        assert len(messages) == 0

    # test error messaging
    content = b"foo: [1, 2"
    try:
        value, messages = validate_yaml(content, String())
    except ParseError as exc:
        assert exc.position.line_no == 1
        assert exc.position.column_no == 10
    else:
        assert False, "Expected ParseError"

    # test error messaging with nested dictionaries
    content = b"foo: \n  - bar"

# Generated at 2022-06-14 15:00:35.583259
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        name = fields.String(max_length=100)
        age = fields.Integer(minimum=18)

        class Meta:
            strict = True

    content = "name: Mr Smith\nage: 42\n"
    value, errors = validate_yaml(content, MySchema)

    assert not errors
    assert isinstance(value, dict)
    assert value == {"name": "Mr Smith", "age": 42}


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 15:00:41.925402
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class Person(Schema):
        name = String()
        age = String()

    content = "name: Jim\nage: 25"
    expected = (
        '''name: Jim
age: 25''',
        [],
    )
    assert validate_yaml(content, Person) == expected



# Generated at 2022-06-14 15:00:45.631391
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(type='const', const='hello')
    data = "text: hello"
    value, error_messages = validate_yaml(data, field)
    assert error_messages == []
    

# Generated at 2022-06-14 15:00:53.290936
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
a:
  b:
    c: 1
    d: null
    e:
    f: 10
    g: -10
"""

    class MySchema(Schema):
        a = Field(dict, required=True, children={"b": {
            "c": Field(int, required=True, gte=0, lte=5),
            "d": Field(int, required=True),
            "e": Field(int, required=True),
            "f": Field(int, required=True, gte=0),
            "g": Field(int, required=True, lte=0),
        }})

    value, error_messages = validate_yaml(content, MySchema)
    assert len(error_messages) == 3

# Generated at 2022-06-14 15:01:05.346719
# Unit test for function validate_yaml
def test_validate_yaml():
    def _test_substitute_validation_error(content, field, expected_messages):
        """
        content: A YAML string or bytestring.
        field:  typesystem.Field to validate against.
        expected_messages: A list of typesystem.Message
        """

        value, messages = validate_yaml(content, field)
        assert not messages
        if isinstance(value, str):
            value = bytes(value, "utf-8")
        with raises(ValidationError) as exc_info:
            field.validate(value)
        assert exc_info.value.messages == expected_messages

    def _assert_error_messages_equal(messages, expected_messages):
        assert len(messages) == len(expected_messages)

# Generated at 2022-06-14 15:01:16.057316
# Unit test for function validate_yaml
def test_validate_yaml():
    from rdflib.term import BNode
    from rdflib import URIRef

    class MySchema(Schema):
        title = "Yahuu"
        title2 = "Lupu"
        bij = "Zee"
        links = "Zij"
        link = "Lik"
        subject = "Onderwerp"

        my_int = Field(
            name="my_int",
            required=True,
            type="integer",
            description="An integer.",
        )
        my_int1 = Field(name="my_int1", description="An integer.", type="integer")

        my_float = Field(
            name="my_float",
            required=True,
            type="number",
            description="A number.",
        )


# Generated at 2022-06-14 15:01:23.911815
# Unit test for function validate_yaml
def test_validate_yaml():
	import yaml
	from typesystem.base.validators import String, Integer, OneOf
	from typesystem.exceptions import ValidationError
	from typesystem.fields import Error, Field
	from typesystem.errors import ErrorTree
	from typesystem.tokenize.positional_validation import validate_with_positions
	from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken, Token
	
	test_schema = {
		"name": String(max_length=100),
		"age": Integer(),
		"gender": OneOf(choices=["male", "female"])
	}
	
	test_schema_class = type('test_schema_class', (object,), test_schema)
	
	# Test Valid data

# Generated at 2022-06-14 15:01:28.833164
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '{"name": "Jim"}'
    schema = Schema({"name": str})
    value, errors = validate_yaml(content, schema)
    assert value == {"name": "Jim"}
    assert errors == []


# Generated at 2022-06-14 15:01:36.735617
# Unit test for function validate_yaml
def test_validate_yaml():
    # print(validate_yaml("""a: 1""", schema))
    schema = Schema(properties={"a": fields.Integer(), "b": fields.Integer()})
    print(validate_yaml("""a: 1""", schema))

if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 15:01:45.893208
# Unit test for function validate_yaml
def test_validate_yaml():
    from .yaml_test import validate_yaml as yaml_test
    from .schema_test import validate_yaml as schema_test
    from .field_test import validate_yaml as field_test
    from .utils_test import validate_yaml as utils_test
    from .schema_list_test import validate_yaml as schema_list_test
    from .schema_dict_test import validate_yaml as schema_dict_test
    from .schema_any_of_test import validate_yaml as schema_any_of_test
    from .schema_one_of_test import validate_yaml as schema_one_of_test
    from .schema_all_of_test import validate_yaml as schema_all_of_test
    yaml_test()
    schema_test()
   

# Generated at 2022-06-14 15:01:54.181415
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''
        a: 1
        b:
            c: testing
            d: 2
            e: 3
    '''
    class MySchema(Schema):
        a = Int()
        b = Schema(fields=["c", "d", "e"])

    value, errors = validate_yaml(content, MySchema)
    assert value == {
        "a": 1,
        "b": {"c": "testing", "d": 2, "e": 3},
    }
    assert len(errors) == 0



# Generated at 2022-06-14 15:02:04.641727
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Tests function validate_yaml.
    """
    # Create valid string
    yaml_string = '{"first_name": "Bob", "last_name": "Jones", "age": 35}'
    # Create schema
    schema = Schema({"first_name": "string", "last_name": "string", "age": "integer"})
    # Run function
    value, error_message = validate_yaml(yaml_string, schema)
    # Check for no errors
    assert error_message == []
    # Check for correct return value
    assert value == {"first_name": "Bob", "last_name": "Jones", "age": 35}



# Generated at 2022-06-14 15:02:13.368275
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer
    from typesystem.schemas import Schema

    class TestSchema(Schema):
        count = Integer(minimum=0)

    # A valid YAML string.
    content = b"count: 100"
    result = validate_yaml(content, TestSchema)
    assert result == ({"count": 100}, [])

    # An invalid YAML string.
    content = b"count: -100"
    result = validate_yaml(content, TestSchema)
    (value, error_messages) = result

    assert value == {"count": -100}
    assert len(error_messages) == 1

# Generated at 2022-06-14 15:02:22.845970
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestValidator(Schema):
        name = Field(type=str)
        age = Field(type=int)

    content = """
    name: Bob
    age: 10
    """
    value, errors = validate_yaml(content, TestValidator)
    assert value == {
        'name': 'Bob',
        'age': 10
    }
    assert len(errors) == 0

    content = """
    name: Bob
    age: ten
    """
    value, errors = validate_yaml(content, TestValidator)
    assert value == {
        'name': 'Bob',
        'age': 'ten'
    }
    assert len(errors) == 1
    assert errors[0].code == 'type_error'
    assert errors[0].path == ['age']
    assert errors[0].position

# Generated at 2022-06-14 15:02:33.000114
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("hello: 123") == DictToken(dict(hello=123), 0, 10)
    assert tokenize_yaml("[1, 2, 3]") == ListToken([1, 2, 3], 0, 8)
    assert tokenize_yaml("123") == ScalarToken(123, 0, 3)

    # Type examples.
    assert tokenize_yaml("123").value == 123
    assert tokenize_yaml("123").start == 0
    assert tokenize_yaml("123").end == 3
    assert tokenize_yaml("123").content == "123"

    assert tokenize_yaml("hello: 123") == DictToken(dict(hello=123), 0, 10)
    assert tokenize_yaml("hello: 123").value == dict(hello=123)
    assert tokenize_

# Generated at 2022-06-14 15:02:46.637455
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(content="{}", validator=Schema) == ({}, [])
    assert validate_yaml(content="{}", validator=Field) == ({}, [])
    assert validate_yaml(content="{}", validator=Field(name="x", required=True)) == (
        None,
        [ValidationError(text="Value is required.", code="required", position=Position(column_no=1, line_no=1, char_index=0))]
    )
    assert validate_yaml(content="{}", validator=Field(name="x", type="integer")) == (None, [ValidationError(text="Value is required.", code="required", position=Position(column_no=1, line_no=1, char_index=0))])

# Generated at 2022-06-14 15:02:51.278505
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_str = """
    name: <str>
    age: <int>
    """
    value, error_messages = validate_yaml(yaml_str, Schema({"name": "string", "age": "integer"}))
    assert error_messages is None
    assert value is not None

# Generated at 2022-06-14 15:03:00.876748
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Tokenization should be able to create the correct type of tokens for all
    the valid YAML types and handle when the YAML is formatted incorrectly.
    """
    correct_yaml_types = {
        # Not all YAML types are supported, but we should still be able to parse
        # all the types that are supported.
        "string": "'string'",
        "int": "42",
        "float": "3.14",
        "list": "- string\n- 12\n- 3.14",
        "dict": "string: string\nint: 12\nfloat: 3.14",
        "null": "null",
        "bool": "True",
    }

# Generated at 2022-06-14 15:03:09.943460
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field()
    value, messages = validate_yaml("""
        foo: bar
        bar: true
    """, validator)
    assert value == {"foo": "bar", "bar": True}
    assert messages == []

    value, messages = validate_yaml("""
        foo: bar
        bar:
    """, validator)
    assert value == {"foo": "bar", "bar": None}
    assert messages == []

    value, messages = validate_yaml("""
        foo: bar
        bar: 10
    """, validator)
    assert value == {"foo": "bar", "bar": 10}
    assert messages == []

    value, messages = validate_yaml("""
        foo: bar
        bar: 10.5
    """, validator)

# Generated at 2022-06-14 15:03:12.309145
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer
    from typesystem.schemas import Schema



# Generated at 2022-06-14 15:03:22.513155
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, String

    class TestSchema(Schema):
        field_1 = String()
        field_2 = String()
        field_3 = Integer()

    messages = validate_yaml(
        content="""field_1: Hello
field_2: World
field_3: -3
""",
        validator=TestSchema,
    )

    assert len(messages) == 0

    messages = validate_yaml(
        content="""field_1: Hello
field_2: World
field_3: three
""",
        validator=TestSchema,
    )
    assert len(messages) == 1
    assert messages[0].text == "Must be an integer."

# Generated at 2022-06-14 15:03:32.800617
# Unit test for function validate_yaml
def test_validate_yaml():
  validator = Field(name="test", type="string")
  test = """
      foo: bar
  """
  assert validate_yaml(content=test, validator=validator) == ({"foo": "bar"}, [])
  test = """
      foo: "bar"
  """
  assert validate_yaml(content=test, validator=validator) == ({"foo": "bar"}, [])
  test = """
      foo: True
  """
  assert validate_yaml(content=test, validator=validator) == ({"foo": True}, [])
  test = """
      foo: 1
  """
  assert validate_yaml(content=test, validator=validator) == ({"foo": 1}, [])
  test = """
      foo: null
  """

# Generated at 2022-06-14 15:03:40.899832
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_str = """
    messages:
        greeting:
            english: Hello {{ recipient }}!
            spanish: Hola {{ recipient }}!
    """
    Greeting = Schema.of(
        fields={
            "recipient": Field.of(type=str, required=True)
        })()
    Language = Schema.of(fields={
        "english": Field.of(type=str, required=True),
        "spanish": Field.of(type=str, required=True),
    })()
    Result = Schema.of(fields={
        "greeting": Field.of(type=Language, required=True),
    })()

    result = validate_yaml(content=yaml_str, validator=Result)

# Generated at 2022-06-14 15:03:45.371243
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    with open(r"./test_yaml/input.yaml", "r") as f:
        content = f.read()
    result = tokenize_yaml(content)
    assert(result.value['greeting'] == 'Hello')
    assert(result.value['name'] == 'World')


# Generated at 2022-06-14 15:03:50.893762
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""
         - one
         - two
       """)
    assert isinstance(token, ListToken)
    assert len(token) == 2
    assert isinstance(token[0], ScalarToken)
    assert token[0].value == "one"
    assert isinstance(token[1], ScalarToken)
    assert token[1].value == "two"


# Generated at 2022-06-14 15:04:11.038578
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = fields.String()
        age = fields.Number(minimum=0, maximum=130)

    try:
        content = ""
        token = tokenize_yaml(content)
        errors = validate_with_positions(
            token=token, validator=PersonSchema
        )
        assert len(errors) == 2
        assert errors[0].position.line_no == 1
        assert errors[0].position.column_no == 1
        assert errors[1].position.line_no == 1
        assert errors[1].position.column_no == 1
    except Exception as e:
        assert False


# Generated at 2022-06-14 15:04:22.055318
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    This tests that tokenize_yaml return a dict or list token
    """
    with pytest.raises(Exception) as raised:
        tokenize_yaml('')
    assert 'No content.' in str(raised.value)

    # testing for dictToken
    content = """
    title: This is a movie
    actors:
    - first actor
    - second actor
    """
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert len(token) == 2
    assert token['title'] == 'This is a movie'
    
    # testing for listToken
    token = tokenize_yaml('- name: John\n- name: Eric')
    assert isinstance(token, ListToken)
    assert len(token) == 2



# Generated at 2022-06-14 15:04:30.705368
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema({"foo": {"type": "string"}})
    assert validate_yaml(content="foo: bar", validator=schema) == ("foo: bar", [])
    value, error_messages = validate_yaml(content='foo: bar\nitems:\n  - 1', validator=schema)
    assert value == "foo: bar"
    assert error_messages == [
        Message(
            text="Additional properties are not allowed ('items' was unexpected)",
            code="additional_properties",
            position=Position(column_no=1, line_no=2, char_index=8),
        )
    ]
    value, error_messages = validate_yaml(content="foo: 1", validator=schema)
    assert value == "foo: 1"
    assert error_messages

# Generated at 2022-06-14 15:04:42.015679
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(type_name='float')
    content = b''
    value, error_messages = validate_yaml(content, validator)
    assert value is None
    assert error_messages == [Message(text='Expected a float.', code='type_error', position=Position(column_no=1, line_no=1, char_index=0), field_name=None)]

    validator = Field(type_name='integer', min_value=10, max_value=100)
    # test min
    content = b'1'
    value, error_messages = validate_yaml(content, validator)
    assert value is None

# Generated at 2022-06-14 15:04:45.919439
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(content='"hello"', validator=str) == ('hello', [])
    assert validate_yaml(content='hello', validator=str) == (None, [])
    assert validate_yaml(content='"hello"', validator=int) == (None, [])

# Generated at 2022-06-14 15:04:53.593570
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = type("TestSchema", (Schema,), {"a": Field(type="string")})
    results = validate_yaml(b"a: string\n", schema)
    value, messages = results
    assert value == {"a": "string"}
    assert len(messages) == 1
    assert messages[0].kind == "validation"
    assert str(messages[0]) == "a: string"

if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 15:05:00.077192
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""
    key:
      - 1
    b: 2
    """)
    expected = DictToken(
        {
            "key": ListToken([ScalarToken(1, 19, 20, content="  - 1\n")], 15, 20, content="      - 1\n"),
            "b": ScalarToken(2, 27, 28, content="  b: 2\n"),
        },
        0,
        29,
        content="\n    key:\n      - 1\n    b: 2\n    ",
    )
    assert token == expected # noqa: E716/E721



# Generated at 2022-06-14 15:05:08.852351
# Unit test for function validate_yaml
def test_validate_yaml():
    class Page(Schema):
        title = Field(str)
        seen = Field(bool)

    class Book(Schema):
        pages = Field(list, items=Page)

    content = """
    pages:
      - title: Page 0
        seen: True
      - title: Page 1
        seen: False
      - title: Page 2
        seen: False
    """

    missing_title = """
    pages:
      - seen: True
      - title: Page 1
        seen: False
      - title: Page 2
        seen: False
    """

    book, messages = validate_yaml(content, validator=Book)
    assert messages == []
    assert book["pages"][0]["title"] == "Page 0"

    _, messages = validate_yaml(missing_title, validator=Book)
   

# Generated at 2022-06-14 15:05:16.564705
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(
        {"name": String(), "age": Integer(), "friends": Array(items=String())}
    )

    class Data(Schema):
        name = String()
        age = Integer()

    assert validate_yaml(
        """
        name: Jane Doe
        age: 35
        """,
        validator=schema,
    ) == ({'name': 'Jane Doe', 'age': 35}, [])

    assert validate_yaml(
        """
        name: Jane Doe
        age: ABC
        """,
        validator=schema,
    ) == (None, [Message(text="Must be a number.", code="type", position=Position(line_no=3, column_no=4, char_index=17))])


# Generated at 2022-06-14 15:05:26.514637
# Unit test for function validate_yaml
def test_validate_yaml():
    simple = Schema(
        {
            "item": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "price": {"type": "number"},
                    "in_stock": {"type": "boolean"},
                    "timestamp": {"type": "number"},
                },
                "description": "Product information.",
            }
        },
        description="A simple example.",
    )
    data = """
    item:
      id: 1
      name: "Foo"
      price: 1.02
      in_stock: true
      timestamp: 1234567890.68
    """
    value, errors = validate_yaml(data, validator=simple)
    assert errors == []

# Generated at 2022-06-14 15:05:45.469752
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(required=True, type='string')
    validator = field
    
    content = "hello"
    value, error_messages = validate_yaml(content, validator)
    print("test_validate_yaml_correct")
    print("value:"+str(value))
    print("error_messages:"+str(error_messages))

    content = 123
    value, error_messages = validate_yaml(content, validator)
    print("test_validate_yaml_error")
    print("value:"+str(value))
    print("error_messages:"+str(error_messages))


# Generated at 2022-06-14 15:05:52.507337
# Unit test for function validate_yaml
def test_validate_yaml():

    # If string is empty the function should return an error message.
    assert validate_yaml("", str) == (None, [
        Message(
            text="No content.",
            code="no_content",
            position=Position(column_no=1, line_no=1, char_index=0),
        )
    ])

    # If the string is not empty, it should return the value.
    assert validate_yaml('{"a": "b", "c": "d"}', Schema) == (
        {"a": "b", "c": "d"},
        []
    )

    # If the string is not empty, but is not a valid YAML file, return an error message.

# Generated at 2022-06-14 15:06:03.683276
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b'{"a": 1, "b": 2}'
    assert validate_yaml(content, Field(format="yaml", type="object")) == ({'a':1, 'b':2}, None)
    content = b'[1, 2]'
    assert validate_yaml(content, Field(format="yaml", type="array")) == ([1,2], None)
    content = b'"string"'
    assert validate_yaml(content, Field(format="yaml", type="string")) == ("string", None)
    content = b'{"a": 1, "b": 2}'

# Generated at 2022-06-14 15:06:14.040401
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema
    
    class MySchema(Schema):
        greeting = String()

    content = 'greeting: hi there'
    result = validate_yaml(content, MySchema)
    print(result)
    assert result.ok == True, "Expected successful validation."
    assert result.value == MySchema({"greeting": "hi there"}), \
        "Expected correct value"
    assert result.errors == [], "Expected no errors."

    class MySchema(Schema):
        greeting = String(min_length=5)

    content = 'greeting: hi there'
    result = validate_yaml(content, MySchema)
    assert result.ok == False, "Expected failed validation."
    assert result