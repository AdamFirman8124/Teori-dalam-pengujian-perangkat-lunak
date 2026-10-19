

# Generated at 2022-06-14 14:56:35.313456
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test for validate_yaml
    Validation of a correct yaml string and one with error in it.
    """
    TEST_CONTENT = b"""
    title: Test title
    """
    # Test a valid yaml string
    validator = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
        },
    }
    value, error_messages = validate_yaml(TEST_CONTENT, validator)
    assert value == {
        "title": "Test title",
    }
    assert error_messages == []

    # Test an invalid yaml string
    INVALID_CONTENT = b"""
    title:
    """
    value, error_messages = validate_yaml(INVALID_CONTENT, validator)
    assert value

# Generated at 2022-06-14 14:56:46.855854
# Unit test for function validate_yaml
def test_validate_yaml():
    # Example schema
    class MySchema(Schema):
        name = Field(str)
        age = Field(int)
        active = Field(bool)

    # Basic success
    content = """name: Charlie age: 26 active: True"""
    value, errors = validate_yaml(content, MySchema)
    assert len(errors) == 0

    # Multiple errors
    content = """name: Charlie age: 26.5 active: True"""
    value, errors = validate_yaml(content, MySchema)
    assert len(errors) == 2
    assert errors[0].code == "expected_int"
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no == 18
    assert errors[1].code == "invalid_value"
    assert errors[1].position.line

# Generated at 2022-06-14 14:56:56.360425
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("123") == ScalarToken(value=123, start=0, end=2, content="123")
    assert tokenize_yaml("null") == ScalarToken(value=None, start=0, end=3, content="null")
    assert tokenize_yaml("true") == ScalarToken(value=True, start=0, end=3, content="true")
    assert tokenize_yaml("false") == ScalarToken(value=False, start=0, end=4, content="false")
    assert tokenize_yaml("123.5") == ScalarToken(value=123.5, start=0, end=4, content="123.5")

# Generated at 2022-06-14 14:57:02.785865
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # ScalarToken
    assert tokenize_yaml("foo") == ScalarToken("foo", 0, 2, content='foo')

    # ListToken
    assert tokenize_yaml("- foo") == ListToken(["foo"], 0, 5, content='- foo')

    # DictToken
    assert tokenize_yaml("foo: bar") == DictToken({"foo": "bar"}, 0, 8, content='foo: bar')


# Generated at 2022-06-14 14:57:13.188149
# Unit test for function validate_yaml
def test_validate_yaml():
    class FooSchema(Schema):
        bar = Field(type="string")
        baz = Field(type="integer")
    result = validate_yaml(content="# foo\nbar: hello\nbaz: 10", validator=FooSchema)
    assert isinstance(result[0], DictToken)
    assert not result[1]
    result = validate_yaml(content="# foo\nbar: hello\nbaz: 10", validator=FooSchema(strict=True))
    assert result[0] is None
    assert isinstance(result[1], ListToken)
    assert sorted(result[1][0].keys()) == sorted(["text", "code", "position"])
    assert result[1][0]["code"] == "missing_required"

# Generated at 2022-06-14 14:57:17.046062
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = yaml.load("""
        foo:
            - baz
            - qux
    """)
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert isinstance(token["foo"], ListToken)
    assert isinstance(token["foo"][0], ScalarToken)

# Unit tests for function validate_yaml

# Generated at 2022-06-14 14:57:19.341136
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("")
    assert yaml
    assert SafeLoader


# Unit tests for function validate_yaml

# Generated at 2022-06-14 14:57:26.159825
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Unit test for function tokenize_yaml
    """
    content = """
    # comment
    name: John Doe
    """

    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert len(token.items) == 1

    key, value = token.items[0]
    assert key == "name"
    assert value == "John Doe"
    assert value.content == content



# Generated at 2022-06-14 14:57:29.432486
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml(b'''{hello: world}''')
    assert isinstance(token, DictToken)
    assert isinstance(token[0], ScalarToken)
    assert token[0].value == 'hello'



# Generated at 2022-06-14 14:57:40.665843
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """\
    a:b
    c:
      d:e
    f:
      - g
      - h
    """
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.start_mark == 0
    assert token.end_mark == len(content) - 1
    assert token.value == {"a": "b", "c": {"d": "e"}, "f": ["g", "h"]}

    content = "true"
    token = tokenize_yaml(content)
    assert isinstance(token, ScalarToken)
    assert token.start_mark == 0
    assert token.end_mark == len(content) - 1

    content = "42"
    token = tokenize_yaml(content)

# Generated at 2022-06-14 14:57:54.339488
# Unit test for function validate_yaml
def test_validate_yaml():
    class Color(Schema):
        name = "string"
        value = "string"
    class Box(Schema):
        name = "string"
        color = "Color"
    
    content = """
    - name: green apple
      value: green
    """
    validator = List(Color)
    value = validate_yaml(content, validator)
    
    print("\n")
    error_message = value
    print(error_message)
    print("\n")
    #assert len(error_message) == 0
    #assert value == [
    #    Color(name="green apple", value="green"),
    #]
    
    
    
    
    content = """
    name: red apple
    value: red
    """
    validator = Color

# Generated at 2022-06-14 14:58:06.196702
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String
    from typesystem.schemas import Schema

    class Author(Schema):
        name = String()
        age = Integer(minimum=0)

    class Book(Schema):
        title = String()
        author = Author(required=True)
        readers = Integer()

    # test a valid yaml
    yaml_input = '''
title: The Lord of the Rings
author:
  name: J. R. R. Tolkien
  age: null
readers: 1
    '''
    value, error_messages = validate_yaml(yaml_input, Book())

# Generated at 2022-06-14 14:58:10.126893
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        name = "string"
        age = "integer"
        fave_color = "string"

    errors = validate_yaml("""
    name: George
    age: 40
    fave_color: blue
    """, MySchema)

    assert errors == []



# Generated at 2022-06-14 14:58:21.181567
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema()

# Generated at 2022-06-14 14:58:29.142207
# Unit test for function validate_yaml
def test_validate_yaml():
    try:
        from typesystem import types, validators
        from typesystem import schemas # type: ignore
    except ImportError:  # pragma: no cover
        return # skip unit test if PyYAML is not installed
    import pytest
    
    schema = schemas.Schema(
        [
            types.String(name='name'),
            types.Integer(name='age', validators=[validators.Min(18)]),
        ]
    )
    valid_input = """
    -
        name: Thomas
        age: 32
    -
        name: Edmond
        age: 20
    """

    invalid_input = """
    -
        name: Thomas
        age: 19
    -
        name: Edmond
        age: 16
    """

# Generated at 2022-06-14 14:58:40.883813
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String
    from typesystem.schema import RootSchema
    class InvalidSchema(RootSchema):
        non_existant = Integer()
    class ValidSchema(RootSchema):
        my_field = String(max_length=5)
    valid_content = b"my_field: 'hello'"
    invalid_content = b"non_existant: 5"
    invalid_schema_errors = validate_yaml(
        content=invalid_content, validator=InvalidSchema
    )[1]
    assert len(invalid_schema_errors) == 1
    assert invalid_schema_errors[0].code == "invalid_key"
    assert invalid_schema_errors[0].position.column_no == 1
    assert invalid_schema_errors[0].position

# Generated at 2022-06-14 14:58:52.215285
# Unit test for function validate_yaml
def test_validate_yaml():

    class UserSchema(Schema):
        name = String(max_length=100)

    assert validate_yaml('name: John Doe', UserSchema) == (
        {"name": "John Doe"},
        # expected output:
        # [],  # type: ignore
    )

    assert validate_yaml('"name": John Doe', UserSchema) == (
        # expected output:
        # None,
        [
            ValidationError(
                text="Must be a dict",
                code="type_mismatch",
                type="dict",
                value='"name": John Doe',
                position=Position(line_no=1, column_no=1, char_index=0),
            )
        ],
    )

# Generated at 2022-06-14 14:59:04.178598
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        first_name = String(max_length=255)
        last_name = String(max_length=255)
        count = Integer(minimum=0)
        date = Date()

    yaml_str = """
    first_name: Ada
    last_name: Lovelace
    count: 1
    """
    value, error_messages = validate_yaml(yaml_str, MySchema)
    assert isinstance(error_messages, list)
    assert len(error_messages) == 1
    assert value == {"first_name": "Ada", "last_name": "Lovelace", "count": 1}
    assert error_messages[0].code == "required_field"

# Generated at 2022-06-14 14:59:14.907365
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test validate_yaml
    """
    my_str = '''
        a: 1
        b:
          - 2
          - 3
        c:
          c1: 4
          c2: 5
    '''

    # ValueError if validator is not a Field instance or Schema class defined
    try:
        validate_yaml(my_str, 'validator')
    except ValueError:
        pass
    else:
        assert False, "Expected to raise ValueError"

    # Validate a valid YAML string.
    value, error_messages = validate_yaml(my_str, {'a': int, 'b': [int], 'c': {'c1': int, 'c2': int}})

# Generated at 2022-06-14 14:59:20.801388
# Unit test for function validate_yaml
def test_validate_yaml():
    content = (
        b"""
    id: 1
    field1:
        - 1
        - 2
        """
    )
    field_value = Field(required=False, default=2)
    schema = Schema({"field1": field_value})
    value, error_messages = validate_yaml(content, schema)
    assert value == {"id": 1, "field_1": [1,2]}
    assert error_messages == []
    
    content = (
        b"""
    id: 1
    field1:
        - 1
        - 2
        """
    )
    field_value = Field(required=False, default=2)
    schema = Schema({"field2": field_value})
    value, error_messages = validate_yaml(content, schema)

# Generated at 2022-06-14 14:59:33.804336
# Unit test for function validate_yaml
def test_validate_yaml():
    # validate_yaml is a wrapper for validate_with_positions
    # and also testes pass in of a Field instance to validate_with_positions
    from typesystem.fields import Integer
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import DictToken, ScalarToken

    class MySchema(Schema):
        child_id = Integer(required=True)

    class MySchema2(Schema):
        child_name = String(required=True)

    class MySchema3(Schema):
        id = Integer()

    class MySchema4(Schema):
        id = Integer()

    # valid YAML
    content = """
    child_id: 1234
    """

    token = tokenize_yaml(content)
    value, errors = validate_

# Generated at 2022-06-14 14:59:35.920835
# Unit test for function validate_yaml
def test_validate_yaml():
    # TODO: Write a unit test for this function
    pass

# Generated at 2022-06-14 14:59:47.390160
# Unit test for function validate_yaml
def test_validate_yaml():

    class CatSchema(Schema):
        age = fields.IntegerField()
        name = fields.StringField()

    content = """
    - age: 10
      name: "Bob"
    - age: "bad"
      name: "Alice"
    """

    expected_errors = [
        Message(
            text="Ensure this value is less than or equal to 10.",
            code="max_value",
            position=Position(column_no=6, line_no=2, char_index=14),
        ),
        Message(
            text="A valid integer is required.",
            code="invalid",
            position=Position(column_no=6, line_no=4, char_index=14),
        ),
    ]


# Generated at 2022-06-14 14:59:50.553001
# Unit test for function validate_yaml
def test_validate_yaml():
    v = validate_yaml("a: 1", {"a": "integer"})
    assert v[0] == {"a": 1}

# Generated at 2022-06-14 14:59:55.670665
# Unit test for function validate_yaml
def test_validate_yaml():
    content1 = "a: 1"
    content2 = "{a: 1"

    class TestSchema(Schema):
        a = int

    token = tokenize_yaml(content1)
    value, error_messages = validate_with_positions(token=token, validator=TestSchema)
    assert value == {"a": 1}

    token = tokenize_yaml(content2)
    value, error_messages = validate_with_positions(token=token, validator=TestSchema)
    assert len(error_messages) == 1
    assert error_messages[0].position.char_index == 0



# Generated at 2022-06-14 15:00:04.002424
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Schema.of({"key": Field.of(type=int)})
    content = "key: 'value'"
    result = validate_yaml(content, validator)
    assert result[0] == "key"
    assert result[1] == [Message(
        text="A valid integer is required.",
        code="type_error.integer",
        type="integer",
        expected_type="int",
        position=Position(column_no=5, char_index=5, line_no=1),
    )]

    content = "0: 'value'"
    result = validate_yaml(content, validator)
    assert result[0] == "0"

# Generated at 2022-06-14 15:00:15.350819
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    name: John
    age: 42
    """
    errors = validate_yaml(content, User)
    assert errors is None, "Expected no errors"

    content = """
    name: John
    """
    errors = validate_yaml(content, User)
    assert errors == [(
        Message(text="This field is required.", code="required",),
        Position(line_no=2, column_no=5, char_index=11))
    ], "Should have a 'required' error"

    content = """
    age: "25"
    """
    errors = validate_yaml(content, User)

# Generated at 2022-06-14 15:00:24.896674
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.base import String

    field = String(min_length=2)
    value, error_messages = validate_yaml(content="test", validator=field)

    assert value == "test"
    assert not error_messages

    content = "- one" "\n" "- two"
    value, error_messages = validate_yaml(content=content, validator=field)

    assert not value
    assert error_messages

    error = error_messages[0]
    assert isinstance(error, ValidationError)
    assert error.text == "'one' is too short."
    assert error.position.line_no == 2
    assert error.position.column_no == 4
    assert error.position.char_index == 5

# Generated at 2022-06-14 15:00:30.373691
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    assert validate_yaml(content="", validator=None) == (None, [])
    with pytest.raises(ParseError, match="No content."):
        validate_yaml(content="", validator=Field())
    with pytest.raises(ValidationError, match="Boolean value expected."):
        validate_yaml(content="1", validator=Field(type="boolean"))
    with pytest.raises(ValidationError, match="Integer value expected."):
        validate_yaml(content="1.1", validator=Field(type="integer"))
    with pytest.raises(ValidationError, match="Number value expected."):
        validate_yaml(content="foo", validator=Field(type="number"))
   

# Generated at 2022-06-14 15:00:40.270045
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer, Float

    class Address(Schema):
        street = String(required=True)
        city = String(required=True)
        zipcode = Integer(min_length=4)

    class Person(Schema):
        name = String(required=True)
        age = Integer(min_value=18, max_value=120)
        favorite_foods = String(repeated=True)
        address = Address()

    data = """
    name: John Doe
    age: 50
    address:
        street: University Street
        city: Boston
        zipcode: 12345
    favorite_foods:
    - Pizza
    - Pasta
    - Bacon
    """

    token = tokenize_yaml(data)

# Generated at 2022-06-14 15:00:49.729440
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = String(min_length=2, max_length=8)
        age = Integer(min_value=1, max_value=150)
        is_cool = Boolean()

    data = """
    name: test1
    age: 3
    is_cool: Y
    """

    output = validate_yaml(data, TestSchema)

    assert output[0]["name"] == "test1"
    assert output[0]["age"] == 3
    assert output[0]["is_cool"] is True


# Generated at 2022-06-14 15:00:58.460408
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        int_1 = fields.Integer()
        bool_2 = fields.Boolean()
    content = "int_1: hello\nbool_2: True"
    result, error_messages = validate_yaml(content, MySchema)
    assert error_messages == [
        Message(
            message="Must be an integer.",
            code="invalid",
            position=Position(
                char_index=6, column_no=7, line_no=1
            ),
            pointer="int_1",
            schema=MySchema,
        )
    ]

# Generated at 2022-06-14 15:01:10.049583
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml("a: 1", Field(type="integer")) == (
        {"a": 1},
        [],
    )

    assert validate_yaml("a: abc", Field(type="integer")) == (
        {},
        [
            Message(
                text="Value type 'str' does not match field type 'integer'.",
                code="type_error.integer",
                position=Position(line_no=1, column_no=4, char_index=3),
            )
        ],
    )

    assert validate_yaml(
        """{
            # Comment
            a: 1,
            b: 2
        }""",
        Field(type="integer"),
    ) == ({"a": 1, "b": 2}, [])

    # Test that we don't blow up on invalid YAML.

# Generated at 2022-06-14 15:01:20.466477
# Unit test for function validate_yaml
def test_validate_yaml():
    from datetime import datetime
    from typesystem import DateTime, fields
    from typesystem.schemas import Schema

    class UserSchema(Schema):
        name = fields.String()
        age = fields.Integer()
        birth_date = fields.DateTime()

    class RecursiveToken(Token):
        start: int
        end: int
        content: str

        def __init__(self, value: typing.Any, start: int, end: int, content: str):
            self.start = start
            self.end = end
            self.content = content
            super().__init__(value)

        def _value(self):
            raise NotImplementedError

        def _run_validator(self, validator, **kwargs):
            if isinstance(validator, Schema):
                return validate_

# Generated at 2022-06-14 15:01:28.883164
# Unit test for function validate_yaml
def test_validate_yaml():
    class User(Schema):
        name = types.String()

    assert validate_yaml('name: Josh', User) == (OrderedDict([('name', 'Josh')]), [])
    assert validate_yaml('name: Josh', User) == (
        OrderedDict([('name', 'Josh')]),
        [],
    )
    assert validate_yaml(b'name: Josh', User) == (
        OrderedDict([('name', 'Josh')]),
        [],
    )

# Generated at 2022-06-14 15:01:37.530284
# Unit test for function validate_yaml
def test_validate_yaml():
    class YAMLDoc(Schema):
        title = types.String()

    content = 'title: "yaml"'
    value, errors = validate_yaml(content, YAMLDoc)
    assert not errors
    assert value.title == 'yaml'

    content = 'notatitle: "yaml"'
    value, errors = validate_yaml(content, YAMLDoc)
    assert errors[0].text == 'Additional properties are not allowed (\'notatitle\' was unexpected).'

# Generated at 2022-06-14 15:01:44.326726
# Unit test for function validate_yaml
def test_validate_yaml():
    value, errors = validate_yaml(
        b'{"name": "bob", "age": "not 10"}',
        {"name": fields.String(), "age": fields.Integer()},
    )
    assert value == {"name": "bob", "age": "not 10"}
    assert errors == [
        ValidationError(
            field="age",
            message="'not 10' is not an integer.",
            code="invalid_type",
            position=Position(char_index=10, column_no=9, line_no=1),
        )
    ]



# Generated at 2022-06-14 15:01:55.664610
# Unit test for function validate_yaml
def test_validate_yaml():
    # Unit test can only be run if pyyaml is installed
    if yaml is not None:
        # Valid input
        yaml_str = '{"type": "foo"}'
        value, errors = validate_yaml(yaml_str, {"type": str})
        assert value == {"type": "foo"}
        assert errors == []

        # Invalid input
        yaml_str = '{"type": 12}'
        value, errors = validate_yaml(yaml_str, {"type": str})
        assert value is None
        assert len(errors) == 1
        assert errors[0] == Message(
            text="Expected a string.",
            code="type_error.string",
            position=Position(column_no=10, char_index=10, line_no=1),
        )

        # Invalid JSON (there

# Generated at 2022-06-14 15:02:02.958936
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    foo: 
        bar: baz
    """

    validator = Field(required=True)
    value, errors = validate_yaml(content, validator)
    assert errors == []

    content = """
    foo: 
        bar: baz
    """

    class MySchema(Schema):
        foo = Field(required=True)

    value, errors = validate_yaml(content, MySchema)
    assert errors == []



# Generated at 2022-06-14 15:02:12.438643
# Unit test for function validate_yaml
def test_validate_yaml():
    class Foo(Schema):
        bar = String(max_length=3)

    content = "bar: abc"
    result = validate_yaml(content, Foo)
    assert result.value == {"bar": "abc"}
    assert result.valid is True
    assert result.error_messages == []

    content = "bar: abcd"
    result = validate_yaml(content, Foo)
    assert result.value is None
    assert result.valid is False
    assert result.error_messages == [
        Message(
            text="Length must be no more than 3.",
            code="max_length",
            position=Position(column_no=8, line_no=1, char_index=7),
            raw_value="abcd",
            type="string",
        )
    ]


# Generated at 2022-06-14 15:02:21.766406
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('{"name": "张三丰"}') == {'name': '张三丰'}
    assert tokenize_yaml('["a", "b"]') == ['a', 'b']
    assert tokenize_yaml('19') == 19
    assert tokenize_yaml('19.82') == 19.82
    assert tokenize_yaml('true') == True
    assert tokenize_yaml('false') == False
    assert tokenize_yaml('null') == None
    try:
        tokenize_yaml('19.82.1')
    except ParseError as e:
        assert 'can not be represented as an integer' in str(e)


# Generated at 2022-06-14 15:02:29.168550
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(fields={"name": String()})
    assert validate_yaml("{name: 'not an int'}", schema) == ({'name': 'not an int'}, [])
    assert validate_yaml("{name: 123}", schema) == (None, [Message(text='This value should be of type string.', code='type_error', position=Position(column_no=8, line_no=1, char_index=7))])

# Generated at 2022-06-14 15:02:34.099638
# Unit test for function validate_yaml
def test_validate_yaml():
    class Root(Schema):
        name = String()

    content = "name: foo"
    value, error_messages = validate_yaml(content, validator=Root)

    assert value == {"name": "foo"}
    assert not error_messages



# Generated at 2022-06-14 15:02:44.968484
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, String, ValidationError
    from typesystem.schemas import Schema

    class User(Schema):
        age = Integer()
        name = String(max_length=10)

    content = "age: 21\nname: 'John'"
    value, error_messages = validate_yaml(content, User)
    assert value == {"age": 21, "name": "John"}
    assert error_messages == []

    content = "age: -21\nname: 'John'"
    value, error_messages = validate_yaml(content, User)
    assert value == {}
    assert len(error_messages) == 1
    assert isinstance(error_messages[0], ValidationError)
    assert error_messages[0].position.line_no == 1
    assert error_

# Generated at 2022-06-14 15:02:53.872178
# Unit test for function validate_yaml
def test_validate_yaml():
    with open(os.path.join(os.path.dirname(__file__), 'test_yaml_file.yml')) as f:
        content = f.read()
    validator = Schema(
        foo=Field(type="string"),
        bar=Field(type="array", items=Field(type="number")),
        baz=Field(type="object", properties={"a": Field(type="string")})
    )
    (value, error_messages) = validate_yaml(content,validator)
    assert len(error_messages) == 0, 'validate_yaml failed to validate correctly'



# Generated at 2022-06-14 15:03:01.601341
# Unit test for function validate_yaml
def test_validate_yaml():
    def validate_email(value):
        if '@' not in value:
            raise ValidationError('Not an email address')
        return value

    class User(Schema):
        name = String()
        email = String(validators=[validate_email])

    content = """
    name: Test User
    email: not_an_email
    """

    value, error_messages = validate_yaml(content, User)
    assert error_messages == [Message(
        text="Not an email address.",
        code="validation_error",
        pointer="/email",
        position=Position(column_no=10, line_no=3, char_index=28),
    )]

# Generated at 2022-06-14 15:03:09.024035
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        foo = Field(type="float")

    raw = b"foo: 1.0"
    (value, errors) = validate_yaml(raw, TestSchema)
    assert len(errors) == 0
    assert value == {"foo": 1.0}

    raw = b"foo: wrong"
    (value, errors) = validate_yaml(raw, TestSchema)
    assert len(errors) == 1
    assert errors[0].code == "invalid_type"
    assert isinstance(errors[0].position, Position)
    assert errors[0].position.char_index == 8



# Generated at 2022-06-14 15:03:17.818135
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml(
        b"""
a:
  -
    - [1, 2, 3]
    - "test"
    - 12345
  -
    - [1, 2, 3]
    - "test"
    - 12345
"""
    ) == {
        "a": [
            [
                [1, 2, 3],
                "test",
                12345,
            ],
            [
                [1, 2, 3],
                "test",
                12345,
            ],
        ]
    }



# Generated at 2022-06-14 15:03:28.159847
# Unit test for function validate_yaml
def test_validate_yaml():
    from datetime import date
    from typesystem import date as date_type

    class User(Schema):
        name = Field(type=str)
        birthday = Field(type=date_type)

    content = """
---
name: "Arthur Dent"
birthday: "1970-02-16"
"""
    value, messages = validate_yaml(content, validator=User)
    assert value["name"] == "Arthur Dent"
    assert value["birthday"] == date(1970, 2, 16)
    assert messages == []

    content = """
name: "Arthur Dent"
birthday: "1970-02-16"
"""
    _, messages = validate_yaml(content, validator=User)
    assert len(messages) == 1
    assert messages[0].code == "parse_error"

# Generated at 2022-06-14 15:03:38.400041
# Unit test for function validate_yaml
def test_validate_yaml():

    content = "a: b"
    field = Field(type="string")
    value, messages = validate_yaml(content, field)
    assert value == "b"
    assert len(messages) == 1
    assert messages[0].code == "type_error.string"
    assert messages[0].position.line_no == 1
    assert messages[0].position.column_no == 3
    assert messages[0].position.char_index == 2

    content = "1: 2"
    field = Field(type="string")
    with pytest.raises(ParseError):
        assert validate_yaml(content, field)

    content = " {a: b}"
    field = Field(type="string")
    with pytest.raises(ParseError):
        assert validate_yaml(content, field)



# Generated at 2022-06-14 15:03:52.754614
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml

    yaml_content = """
     ---
        flower:
          name: hollyhock
          color: pink
          season: summer
        tree:
          name: oak
          color: brown
          season: autumn
    """

    yaml_content_invalid = """
    ---
      flower:
        name: hollyhock
        color: pink
        season: summer
      tree:
      name: oak
      color: brown
      season: autumn
    """

    class Plant(Schema):
        name = Field(type="string")
        color = Field(type="string")
        season = Field(type="string")

    class Garden(Schema):
        flower = Field(type=Plant)
        tree = Field(type=Plant)

    # Test valid yaml
    value, errors = validate

# Generated at 2022-06-14 15:04:00.546541
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test handling of empty content.
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("")
    assert exc_info.value.text == "No content."
    assert exc_info.value.position == Position(column_no=1, line_no=1, char_index=0)

    # Test handling of parse error.
    with pytest.raises(ParseError) as exc_info:
        tokenize_yaml("{foo: 'bar'")
    assert exc_info.value.text == 'found unconstructed plain scalar.'
    assert exc_info.value.position == Position(column_no=9, line_no=1, char_index=8)



# Generated at 2022-06-14 15:04:06.852647
# Unit test for function validate_yaml
def test_validate_yaml():
    import json
    import typesystem
    schema = typesystem.Schema(
        properties={"name": typesystem.String(max_length=50)}
    )
    value, error_messages = validate_yaml(b"name: Bob", schema)
    expected_value = {
        "name": "Bob"
    }
    assert value == expected_value
    assert len(error_messages) == 0

# Generated at 2022-06-14 15:04:12.257819
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = validation.Schema(
        {"name": validation.String(), "value": validation.Integer()}
    )
    value, error_messages = validate_yaml(
        """
    name: dino
    value: 3.14
    """,
        validator,
    )

    assert not error_messages
    assert value == {"name": "dino", "value": 3}

# Generated at 2022-06-14 15:04:23.026022
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, fields
    from typesystem.exceptions import ValidationError
    schema = Schema(
        name=fields.String(min_length=1, max_length=1, name="name"),
        age=fields.Integer(),
        friends=fields.Array(items=fields.String()),
    )

    yaml_str = """
    name: A
    #
    # no: error
    #
    age: 27
    location: NY
    friends:
    - Jane
    - John
    """

    value, error_messages = validate_yaml(yaml_str, schema)

    assert len(error_messages) == 3
    assert error_messages[0].text == "Value is too long."
    assert error_messages[1].text == "Error resolving field: location"


# Generated at 2022-06-14 15:04:32.640082
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    # Test for empty string
    with pytest.raises(ParseError) as excinfo:
        validate_yaml('', validator=Field(type="string"))
    assert excinfo.types[0] == ParseError

    # Test for empty string - Schema
    with pytest.raises(ValidationError) as excinfo:
        validate_yaml('', Schema(fields={"name": Field(type="string")}))
    assert excinfo.types[0] == ValidationError

    # Test for string
    json_str = """
    foo: 'bar'
    """
    value, error_messages = validate_yaml(json_str, Field(type="string"))
    assert value == "'bar'"
    assert error_messages

# Generated at 2022-06-14 15:04:37.445507
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = String(required=True)
        age = Integer()

    content = """
    name: Alex
    age: 30
    """

    value, _ = validate_yaml(content, PersonSchema)

    assert value["name"] == "Alex"
    assert value["age"] == 30

# Generated at 2022-06-14 15:04:45.958857
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test validate_yaml
    """

    @typing.overload
    def _validate_yaml(
        content: typing.Union[str, bytes],
        validator: typing.Union[Field, typing.Type[Schema]],
    ) -> typing.Any:
        """
        Test _validate_yaml
        """
        pass

    errors = _validate_yaml("", "null")
    assert len(errors) == 1
    assert isinstance(errors.pop(), ParseError)

    errors = _validate_yaml("2", "string")
    assert len(errors) == 1
    assert isinstance(errors.pop(), ValidationError)

# Generated at 2022-06-14 15:04:54.019831
# Unit test for function validate_yaml
def test_validate_yaml():
    # Create the validator so we can generate the error messages
    validator = Schema({
        "name": String(),
        "age": Integer(),
        "tags": Array(String()),
    })

    # Parse and validate data as YAML
    value, errors = validate_yaml("""
    name: John
    age: 20
    tags:
        - Python
        - sports
        - food
    """, validator)

    print(errors)

if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 15:05:05.737794
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    # Test scalar types
    assert tokenize_yaml("10") == ScalarToken(10, 0, 1, content="10")
    assert tokenize_yaml("10.5") == ScalarToken(10.5, 0, 3, content="10.5")
    assert tokenize_yaml("true") == ScalarToken(True, 0, 3, content="true")
    assert tokenize_yaml("null") == ScalarToken(None, 0, 3, content="null")
    assert tokenize_yaml("""
    null
    """) == ScalarToken(None, 0, 6, content="""
    null
    """)
    # Test lists

# Generated at 2022-06-14 15:05:12.413876
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema({"x": Integer()})
    assert validate_yaml("x:1", schema) == ({'x': 1}, {})

# Generated at 2022-06-14 15:05:19.907439
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    assert Token is not None
    assert _get_position is not None
    assert ScalarToken is not None
    assert validate_with_positions is not None
    assert validate_yaml is not None
    assert yaml is not None
    assert yaml.scanner.ScannerError is not None
    assert yaml.parser.ParserError is not None

# Generated at 2022-06-14 15:05:28.004827
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = 'string(max_length=3)'

    name = validate_yaml("{name:hello}", TestSchema)
    assert name == 'hello'

    class AddressSchema(Schema):
        street = 'string()'
        city = 'string()'
        state = 'string(max_length=2)'
        zip_ = 'integer()'

    class HomeSchema(Schema):
        address = AddressSchema()

    yaml_str = """
    address:
      street: 123 Fake Street
      city: Springfield
      state: Missouri
      zip: 12345
    """

    home = validate_yaml(yaml_str, HomeSchema)

# Generated at 2022-06-14 15:05:39.069794
# Unit test for function validate_yaml
def test_validate_yaml():
    schema_file = "./data/yaml_schema_with_position.yml"
    content_file = "./data/yaml_content_with_position.yml"
    with open(schema_file) as reader:
        schema = yaml.load(reader, Loader=yaml.FullLoader)
    with open(content_file) as reader:
        content = yaml.load(reader, Loader=yaml.FullLoader)
    errors = validate_yaml(content, schema)
    print(errors)

    schema_file = "./data/yaml_schema_with_position.yml"
    content_file = "./data/yaml_content_without_position.yml"

# Generated at 2022-06-14 15:05:48.485308
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    text = """
    # A line comment
    key: value
    """
    token = tokenize_yaml(text)
    assert token.start == 0
    assert token.end == len(text) - 1
    assert isinstance(token, DictToken)
    assert token.get("key") == "value"
    text = """
    - foo
    - bar
    """
    token = tokenize_yaml(text)
    assert isinstance(token, ListToken)
    assert token.start == 0
    assert token.end == len(text) - 1
    assert token.get() == ["foo", "bar"]
    text = "123"
    token = tokenize_yaml(text)
    assert isinstance(token, ScalarToken)
    assert token.start == 0

# Generated at 2022-06-14 15:06:00.685061
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = Text(max_length=255)
        email = Email(max_length=255)

    def validate(yaml_content, expected_results):
        rets = validate_yaml(yaml_content, Person)
        assert rets == expected_results

    validate(b"---\nname: John Doe\nemail: john@example.com", ([], []))
    validate(
        b"---\nname: John Doe\nemail: john@example.com\n",
        ([{'code': 'parsing_error', 'position': Position(line_no=3, column_no=18, char_index=30), 'text': 'Unexpected field.'}], []),
    )


# Generated at 2022-06-14 15:06:04.663160
# Unit test for function validate_yaml
def test_validate_yaml():
    token = tokenize_yaml("""
    # This is a comment.
    name: John Smith
    birthdate: 1980-10-20
    favorite_colors: [red, green, blue]
    """)
    errors = validate_with_positions(token, PersonSchema())
    assert len(errors) == 0


# Generated at 2022-06-14 15:06:12.525572
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    >>> from typesystem.schemas import Schema
    >>> from typesystem.fields import String
    >>> from typesystem.tokenize.yaml_ import validate_yaml
    >>>
    >>> class MySchema(Schema):
    ...     name = String(max_length=10)
    ...
    >>> value, error_messages = validate_yaml("name: 'gautam'", MySchema)
    >>> value
    {'name': 'gautam'}
    >>> error_messages
    []
    """
    pass

