

# Generated at 2022-06-14 14:56:25.115389
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    x = tokenize_yaml('patient: {type: patient, name: John}')
    assert x.value == {'patient': {'type': 'patient', 'name': 'John'}}, 'YAML string was not tokenized properly'

# Generated at 2022-06-14 14:56:32.504115
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml('''
        a: 1
        b: 2
        c: 3
    ''')
    assert token.dict() == {'a': 1, 'b': 2, 'c': 3}
    assert token.start == 0
    assert token.end == 32
    assert token.message() == "Invalid YAML."
    assert token.children[0].start == 2
    assert token.children[0].end == 7
    assert token.children[1].start == 9
    assert token.children[1].end == 14
    assert token.children[2].start == 16
    assert token.children[2].end == 21

# Generated at 2022-06-14 14:56:44.087250
# Unit test for function validate_yaml
def test_validate_yaml():
    def test_validate_yaml_positions():
        # A YAML string with a parse error
        content = """
        hello_world
        """
        field = Field(type=str, pattern="Hello World")

        # Validate the tokenized YAML.
        value, error_messages = validate_yaml(content, field)

        # Ensure an error was raised for the parse error.
        assert len(error_messages) == 1
        assert error_messages[0].code == "parse_error"
        assert error_messages[0].text == "did not find expected alphabetic or numeric character."
        assert error_messages[0].position.line_no == 2
        assert error_messages[0].position.column_no == 8

        # Ensure the correct value is returned.
        assert value is None

# Generated at 2022-06-14 14:56:52.156912
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    test_input1 = "hello: world"  # should generate a DictToken
    test_input2 = "hello: [1, 2, 3]"  # should generate a DictToken
    test_input3 = "[1, 2, 3]"  # should generate a ListToken
    test_input4 = "[1, 2, 3, hello: world]"  # should generate a ListToken

    assert isinstance(tokenize_yaml(test_input1), DictToken)
    assert isinstance(tokenize_yaml(test_input2), DictToken)
    assert isinstance(tokenize_yaml(test_input3), ListToken)
    assert isinstance(tokenize_yaml(test_input4), ListToken)



# Generated at 2022-06-14 14:56:56.151625
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert 'a' == tokenize_yaml(u'a')
    assert [u'a', u'b'] == tokenize_yaml(u'- a\n- b')
    assert {u'a': 1} == tokenize_yaml(u'a: 1')


# Generated at 2022-06-14 14:57:00.949477
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Tests that tokenize executes properly
    """
    test_content = '''
    test_dict:
        key: value
    '''
    assert tokenize_yaml(test_content).value == {'test_dict': {'key': 'value'}}

# Generated at 2022-06-14 14:57:03.238841
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('- a\n- b') == ListToken(['a', 'b'], 0, 7, content='- a\n- b')



# Generated at 2022-06-14 14:57:13.734468
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    from typesystem import types
    from typesystem.schema import Schema

    class AuthorSchema(Schema):
        first_name = types.String(max_length=255)
        last_name = types.String(max_length=255)
        date_of_birth = types.Date(format="%Y-%m-%d")

    class BookSchema(Schema):
        title = types.String(max_length=255)
        author = types.Schema(AuthorSchema)

    class RootSchema(Schema):
        books = types.Array(items=BookSchema)


# Generated at 2022-06-14 14:57:25.237223
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test with string
    s = "'' : 'hello'"
    assert tokenize_yaml(s) == DictToken({'' : 'hello'}, 0, len(s))

    # Test with bytestring
    s = "'' : 'hello'"
    assert tokenize_yaml(s) == DictToken({'' : 'hello'}, 0, len(s))

    # Test with empty string
    s = ""
    try:
        tokenize_yaml(s)
    except ParseError as e:
         assert str(e) == "No content."

    # Test with simple string
    s = "a: { b: { c: 'hello' } }"

# Generated at 2022-06-14 14:57:30.772015
# Unit test for function validate_yaml
def test_validate_yaml():
    # Given
    content = 'name: Tom\nage: 30\n'
    schema = Schema(fields={
        'name': String(),
        'age': Integer(),
    })

    # When
    value, error_messages = validate_yaml(content, schema)

    # Then
    assert value == {
        'name': 'Tom',
        'age': 30
    }

    assert error_messages == []



# Generated at 2022-06-14 14:57:44.677018
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # given
    content = """
    key: Value # comment
    key2: [1, 2, 3]
    """
    # when
    tokens = tokenize_yaml(content)
    # then
    nested_tokens = tokens.get_nested_tokens()
    assert len(nested_tokens) == 5
    assert tokens.start == 0
    assert tokens.end == len(content) - 1
    # and
    key_token = nested_tokens[0]
    assert key_token.start == content.index("key")
    assert key_token.end == content.index("Value # comment") - 1
    # and
    value_token = nested_tokens[1]
    assert value_token.start == content.index("Value # comment")
    assert value_token.end

# Generated at 2022-06-14 14:57:48.278019
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
        - a
        - b
        - c
    """.strip()
    token = tokenize_yaml(content)
    assert isinstance(token, ListToken)
    assert token.content == content


# Generated at 2022-06-14 14:57:57.299612
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    name: john
    age: 30

    hobbies:
        - swimming
        - running
    """
    assert isinstance(tokenize_yaml(content), DictToken)

    content = "john"
    assert isinstance(tokenize_yaml(content), ScalarToken)

    content = """
    - "1"
    - "2"
    - "3"
    """
    assert isinstance(tokenize_yaml(content), ListToken)

    content = "  "
    position = Position(column_no=1, line_no=1, char_index=0)
    with pytest.raises(ParseError) as exc:
        tokenize_yaml(content)

    assert exc.value.code == "no_content"
    assert exc.value.text == "No content."

# Generated at 2022-06-14 14:58:08.874689
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("{}") == {}
    assert tokenize_yaml("") == ""
    assert tokenize_yaml("'hello'") == "hello"
    assert tokenize_yaml("'hello' #sup") == "hello"
    assert tokenize_yaml("'hello' #sup\n") == "hello"
    assert tokenize_yaml("'hello' #sup\n  \n") == "hello"
    assert tokenize_yaml("1.0") == 1.0
    assert tokenize_yaml("1e3") == 1000.0
    assert tokenize_yaml("1.0e3") == 1000.0
    assert tokenize_yaml("1") == 1
    assert tokenize_yaml("-1y") == -1
    assert tokenize_yaml("false")

# Generated at 2022-06-14 14:58:18.977556
# Unit test for function validate_yaml
def test_validate_yaml():
    # Valid
    assert(validate_yaml("foo: bar", fields.Dict({})) == ({'foo': 'bar'}, None))
    assert(validate_yaml("foo: bar\nspam: eggs", fields.Dict({})) == ({'foo': 'bar', 'spam': 'eggs'}, None))

    # Invalid
    assert(type(validate_yaml("foo: \nbar: baz", fields.Dict({}))[1]) == list)

    # No content
    try:
        assert(validate_yaml("", fields.Dict({})) == None)
        assert False
    except ParseError as exc:
        assert (exc.text == "No content.")



# Generated at 2022-06-14 14:58:27.970756
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    from typesystem.tokenize import tokenize_yaml

    token = tokenize_yaml("[1, 2, 3]")
    assert isinstance(token, ListToken)
    assert token.value == [1, 2, 3]
    assert token.start == 0
    assert token.end == 8

    token = tokenize_yaml("[1, 2, 3]")
    assert isinstance(token, ListToken)
    assert token.value == [1, 2, 3]
    assert token.start == 0
    assert token.end == 8

    token = tokenize_yaml("{x: 1, y: 2}")
    assert isinstance(token, DictToken)
    assert token.value == {"x": 1, "y": 2}
    assert token.start == 0
    assert token.end == 12

    token

# Generated at 2022-06-14 14:58:39.869724
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    import yaml
    from functools import partial
    from typing import Dict, Any
    from yaml.loader import SafeLoader
    from typesystem.fields import Integer, String, Boolean

    assert yaml is not None, "'pyyaml' must be installed."

    class CustomSafeLoader(SafeLoader):
        pass

    def construct_mapping(loader: "yaml.Loader", node: "yaml.Node") -> Dict[str, Any]:
        mapping = loader.construct_mapping(node)
        return mapping

    def construct_sequence(loader: "yaml.Loader", node: "yaml.Node") -> Any:
        value = loader.construct_sequence(node)
        return value

    def construct_scalar(loader: "yaml.Loader", node: "yaml.Node") -> Any:
        value = loader

# Generated at 2022-06-14 14:58:45.586767
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml('{"key1":"string","key2":42,"key3":[4,2]}')
    assert token['key1'] == 'string'
    assert token['key2'] == 42
    assert token['key3'][0] == 4


# Generated at 2022-06-14 14:58:47.282771
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    result = tokenize_yaml("")
    assert result == {}

# Generated at 2022-06-14 14:58:55.937365
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("a: foo\n") == {'a': 'foo'}
    assert tokenize_yaml('[1, 2, 3]') == [1, 2, 3]
    assert tokenize_yaml('foo: "bar"') == {'foo': 'bar'}
    assert tokenize_yaml('{"a": 1}') == {'a': 1}
    assert tokenize_yaml('{"a": 1, "b": 2}') == {'a': 1, 'b': 2}
    assert tokenize_yaml('')["hello"] == "world"
    assert tokenize_yaml('["foo", "bar", "baz"]')[0] == "foo"
    assert tokenize_yaml('[1, 2, 3]')[2] == 3


# Generated at 2022-06-14 14:59:12.398907
# Unit test for function validate_yaml
def test_validate_yaml():
    basic_schema = fields.Schema(
        name=fields.String(required=True),
        age=fields.Integer(min_value=0, max_value=100),
    )

    class Same(Schema):
        one = fields.List(fields.String(required=True))
        two = fields.List(fields.String(required=True))

        def validate_same(self):
            if self.context["one"] != self.context["two"]:
                raise ValidationError("One must be equal to two.")

    class CaseSchema(Schema):
        field = fields.String(required=True)

        def validate_field(self):
            if not re.match(f"^{self.context['field']}$", "field"):
                raise ValidationError("Invalid case.")


# Generated at 2022-06-14 14:59:15.255155
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "foo: bar"
    field = Field(type="string")
    assert validate_yaml(content, field) == ("bar", [])



# Generated at 2022-06-14 14:59:24.223091
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer

    class ColorSchema(Schema):
        r = Integer(min_value=0, max_value=255)
        g = Integer(min_value=0, max_value=255)
        b = Integer(min_value=0, max_value=255)

    content = """
    r: -1
    g: 256
    b: 0
    """
    errors = validate_yaml(content, ColorSchema)

    assert len(errors) == 2

    # Min value error
    message = errors[0]
    assert message.code == "min_value"
    assert message.text == "Ensure this value is greater than or equal to 0."
    assert message.position == Position(line_no=2, column_no=7, char_index=20)

    # Max value error
   

# Generated at 2022-06-14 14:59:34.156564
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = Message(description="name")
        age = Message(description="age")

    content = 'name: "James"\nage: "27"'
    assert validate_yaml(content, TestSchema) == (
        {"name": "James", "age": "27"},
        None,
    )

    content = 'name: "John"\nage: "27"\nsomething: "extra"'
    assert validate_yaml(content, TestSchema) == (
        {"name": "John", "age": "27", "something": "extra"},
        [Message(text="Unrecognized field 'something'", code="unrecognized")],
    )

    content = 'name: "John"\nage: "27"\n'

# Generated at 2022-06-14 14:59:36.708895
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "test"
    assert isinstance(validate_yaml(content,""), tuple)



# Generated at 2022-06-14 14:59:47.683252
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("\n---\na: b")
    assert type(token) == DictToken
    assert token.value == {'a': 'b'}
    assert token.start == 3
    assert token.end == 5
    assert type(token.tokens[0]) == ScalarToken
    assert token.tokens[0].value == 'a'
    assert token.tokens[0].start == 3
    assert token.tokens[0].end == 3
    assert type(token.tokens[1]) == ScalarToken
    assert token.tokens[1].value == 'b'
    assert token.tokens[1].start == 5
    assert token.tokens[1].end == 5



# Generated at 2022-06-14 14:59:59.825482
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = (
        'foo: bar\n'
        'baz:\n'
        '  - "qux"\n'
        '  - "quux"\n'
        'hello: world\n'
    )
    tokens = tokenize_yaml(content)
    assert tokens == {
        'foo': 'bar',
        'baz': ['qux', 'quux'],
        'hello': 'world',
    }

# Generated at 2022-06-14 15:00:03.239942
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None
    try:
        value, errors = validate_yaml('name: Ahmed', fields.String())
        assert value == 'Ahmed'
        assert errors == []
    except ImportError:
        pass



# Generated at 2022-06-14 15:00:14.912000
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('---\n\n3\n') == ListToken([3], 1, 5)
    assert tokenize_yaml('---\n\n3.5\n') == ListToken([3.5], 1, 5)
    assert tokenize_yaml('---\n\ntrue\n') == ListToken([True], 1, 5)
    assert tokenize_yaml('---\n\nfalse\n') == ListToken([False], 1, 5)
    assert tokenize_yaml('---\n\nnull\n') == ListToken([None], 1, 5)
    assert tokenize_yaml('---\n\n- 1\n  - 2\n') == ListToken([1, 2], 1, 5)

# Generated at 2022-06-14 15:00:19.161836
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert type(tokenize_yaml('a: 1')) == DictToken
    assert type(tokenize_yaml('[1, 2]')) == ListToken
    assert type(tokenize_yaml('3')) == ScalarToken

# Generated at 2022-06-14 15:00:28.150748
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(
        fields=[
            Field(name="first_name", type="string"),
            Field(name="last_name", type="string", required=True),
            Field(name="age", type="integer"),
            Field(name="is_alive", type="boolean"),
        ]
    )

    content = """
    first_name: "Charles"
    last_name: "Dickens"
    age: 200
    """

    content = content.encode("utf-8")

    value, messages = validate_yaml(content=content, validator=schema)

    assert value == {
        "first_name": "Charles",
        "last_name": "Dickens",
        "age": 200,
    }

    assert len(messages) == 2

    assert messages[0].position.line

# Generated at 2022-06-14 15:00:33.764699
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml("12.3", float) == (12.3, [])
    assert validate_yaml("12.3", int) == (None,
                                          [Message(
                                              code="invalid_type",
                                              text="Value is not of type: int."
                                          )])



# Generated at 2022-06-14 15:00:41.292360
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(
        """
    test:
        -foo: 1
        -bar: 2
    """,
        Schema(
            {"test": ListField(DictField({"foo": IntField()}, allow_unknown=True))}
        ),
    ) == ([{"foo": 1}, {"bar": 2}], [])


# Generated at 2022-06-14 15:00:49.371627
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_schema = type("YAMLSchema", (Schema,), {"age": {"type": int}})

    good_data = "age: 23"
    assert validate_yaml(good_data, yaml_schema) == ({'age': 23}, [])

    bad_data = "age: fish"
    errors = [Message(
        code='invalid',
        message='Must be an integer.',
        position=Position(
            char_index=0,
            column_no=5,
            line_no=1))]
    assert validate_yaml(bad_data, yaml_schema) == ({}, errors)

# Generated at 2022-06-14 15:01:01.751464
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        str_field = Field(type="string")
        list_field = Field(type="array", items={"type": "string"})

    # Successful validation
    assert validate_yaml(
        content=dedent(
            """
            str_field: str
            list_field:
                - first
                - second
            """
        ),
        validator=TestSchema,
    ) == (
        {"str_field": "str", "list_field": ["first", "second"]},
        [],
    )

    # Failure to parse
    with pytest.raises(ParseError) as exc:
        validate_yaml(content="str_field: value", validator=TestSchema)

# Generated at 2022-06-14 15:01:04.825955
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema({"x": int})

    result, messages = validate_yaml("x: '1'", schema)

    assert len(messages) == 1
    message = messages[0]
    assert message.level == "error"
    assert message.code == "type_error"
    assert message.position.line_no == 1



# Generated at 2022-06-14 15:01:09.886700
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    person:
      name: James Joyce
      age: 63
    """

    class Person(Schema):
        name: str
        age: int

    value, messages = validate_yaml(content, Person)

    assert isinstance(value, Person)
    assert value.name == 'James Joyce'
    assert value.age == 63
    assert len(messages) == 0

# Generated at 2022-06-14 15:01:16.551073
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer
    content = "name: zainab\nage: 19"
    class Person(Schema):
        name = String(max_length=10)
        age = Integer(minimum=0, maximum=100)

    validator = Person()
    value, errors = validate_yaml(content, validator)
    assert errors['age'][0]['code'] == 'validator_error.minimum'
    print(errors)

# Generated at 2022-06-14 15:01:23.328649
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema([
        Field(name="name", required=True, type="string"),
        Field(name="age", required=True, type="integer"),
    ])

    content = """
    name: "John Doe"
    age: "42"
    """
    results = validate_yaml(content, schema)
    assert results == (
        {"name": "John Doe", "age": 42},
        [
            Message(
                code="invalid_integer",
                message="Must be an integer",
                text='"42"',
                position=Position(column_no=22, line_no=3, char_index=41),
            )
        ],
    )



# Generated at 2022-06-14 15:01:34.356197
# Unit test for function validate_yaml
def test_validate_yaml():
    class ObjectSchema(Schema):
        a = Field(type="string")

    errors = validate_yaml("a: true", validator=ObjectSchema)
    assert errors == [
        ValidationError(
            text="'true' is not a valid 'string'.",
            code="type_error.string",
            position=Position(char_index=0, column_no=6, line_no=1),
        )
    ]
    assert errors[0].to_json() == {
        "code": "type_error.string",
        "message": "'true' is not a valid 'string'.",
        "position": {"column_no": 6, "char_index": 0, "line_no": 1},
    }
    content = "a: true\nb: 3"

# Generated at 2022-06-14 15:01:46.117787
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema

    class UserSchema(Schema):
        name = "string"
        age = "integer"

    for content in [
        '{"name": "Anna", "age": 23}',
        '{"name": "Anna", "age": "23"}',
        '{"name": "Anna", "age": 23, "likes": ["eat", "sleep"]}',
        '{"name": "Anna", "age": "23", "likes": ["eat", "sleep"]}',
        '{"name": "Anna", "age": 23, "likes": "eat"}',
    ]:
        assert validate_yaml(content, UserSchema) == (
            {"name": "Anna", "age": 23},
            [],
        )


# Generated at 2022-06-14 15:01:53.347125
# Unit test for function validate_yaml
def test_validate_yaml():
    '''
    Inp: A YAML string or bytestring, and a Field instance or Schema class to validate against.
    Out: A two-tuple of (value, error_messages)
    '''
    content = "test"
    validator = Field(name="foo")
    value, message = validate_yaml(content, validator)
    assert (value, message) == ("test", None)


# Generated at 2022-06-14 15:02:01.073239
# Unit test for function validate_yaml
def test_validate_yaml():
    content = content='''
    name: Mike
    age: 14
    years:
    - 2017
    - 2018
    '''
    validator = Schema({"name": str, "age": int, "years": [int]})
    msg = Message(text='Expected an integer', position=Position(line_no=6, column_no=0, char_index=28))
    assert validate_yaml(content,validator) == (None,[msg])

# Generated at 2022-06-14 15:02:08.737489
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    import sys

    class TestSchema(typesystem.Schema):
        name = typesystem.String(max_length=100)

    content_string = """
        name: "Joe Black"
    """
    value, errors = validate_yaml(content_string, TestSchema)
    
    assert value == {"name": "Joe Black"}
    assert errors == []
    print(errors)
    print(value)

    if __name__ == "__main__":
        test_validate_yaml()

# Generated at 2022-06-14 15:02:13.433902
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
- - 1
  - 2
  - 3
- - "foo"
  - "bar"
  - "baz"
    """
    errors = validate_yaml(content, ListField(ListField(IntField())))
    assert not errors



# Generated at 2022-06-14 15:02:22.874144
# Unit test for function validate_yaml
def test_validate_yaml():
    import sys
    import pytest
    from typesystem import Schema, fields
    from typesystem.tokenize import tokenize_yaml
    from typesystem.tokenize.positional_validation import validate_with_positions

    from .yaml import validate_yaml

    # validators
    class PersonSchema(Schema):
        name = fields.String(max_length=100)
        age = fields.Integer(minimum=18, maximum=100)
        height = fields.Number(minimum=0.0, maximum=3.0)
        # Other fields

    class PetSchema(Schema):
        name = fields.String(max_length=100)
        type = fields.String(max_length=100, enum=["cat", "dog", "fish"])


# Generated at 2022-06-14 15:02:30.130181
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(
        {
            "name": {"type": "string"},
            "age": {"type": "number"},
            "height": {"type": "number"},
        }
    )
    assert validate_yaml(
        """
        name: John
        age: "32"
        height: 5.10
        """,
        schema,
    ) == (
        {"name": "John", "age": 32, "height": 5.1},
        [],
    )

# Generated at 2022-06-14 15:02:42.369462
# Unit test for function validate_yaml
def test_validate_yaml():
    class SimpleSchema(Schema):
        foo = Field(str)

    simple_schema = SimpleSchema()

    # Parse error:
    content = "foo: !bar\n"
    _, error_messages = validate_yaml(content, simple_schema)
    assert error_messages[0].position.line_no == 1
    assert error_messages[0].position.column_no == 6

    # Validation error:
    content = "foo: !!int 1\n"
    _, error_messages = validate_yaml(content, simple_schema)
    assert error_messages[0].position.line_no == 1
    assert error_messages[0].position.column_no == 6

    # Success:
    content = "foo: 'bar'\n"
    value,

# Generated at 2022-06-14 15:02:53.619201
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    from typesystem import fields, schemas
    import pytest

    class PatientSchema(schemas.Schema):
        name = fields.String(required=True, pattern="^[A-Za-z]+$")
        age = fields.Integer(required=True)
        address = fields.String()

    content = """
    name: john
    age: 23
    address: Sunnyvale
    """

    (_, error_messages) = validate_yaml(content, PatientSchema)
    assert len(error_messages) == 0

    content = """
    name: john
    age: 23.2
    address: Sunnyvale
    """
    (_, error_message) = validate_yaml(content, PatientSchema)
    assert len(error_message) == 1

# Generated at 2022-06-14 15:03:02.362512
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "a:b"
    validator = Field(name="root", key="a", value=Field(name="a", key="b"))
    value, errors = validate_yaml(content, validator)
    assert not errors
    assert value == {"a": "b"}

    content = "a: b"
    validator = Field(name="root", key="a", value=Field(name="a", key="b"))
    value, errors = validate_yaml(content, validator)
    assert errors
    assert len(errors) == 2
    assert str(errors[0]) == 'Missing value for key "a".'

    content = "a: b"
    validator = Field(name="root", key="a", value=Field(name=None, key="b"))

# Generated at 2022-06-14 15:03:13.536633
# Unit test for function validate_yaml
def test_validate_yaml():
    class ExampleSchema(Schema):
        name = Field(str)
        age = Field(int)

    content = "name: 'John Smith'"
    value, errors = validate_yaml(content, ExampleSchema())
    assert errors[0].code == "required_field"
    assert errors[0].text == "Field 'age' is required."


# Generated at 2022-06-14 15:03:20.202243
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = "string"

    content = """\
name: "Jane Doe"
spouse: "Jon Doe"
"""
    document, errors = validate_yaml(content, Person)
    assert document == {"name": "Jane Doe"}
    assert len(errors) == 1
    error = errors[0]
    assert error.field_name == "spouse"
    assert error.code == "invalid"

# Generated at 2022-06-14 15:03:26.391635
# Unit test for function validate_yaml
def test_validate_yaml():
    # We try to validate against a field of type String
    test_schema = Schema(
        {
            "name": String(required=True),
            "age": Integer(required=False),
        }
    )
    test_data = """name: John Doe
age: 25"""
    value, errors = validate_yaml(test_data, test_schema)
    assert value["name"] == "John Doe"
    assert value["age"] == 25
    assert not errors

# Generated at 2022-06-14 15:03:36.784056
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test validate_yaml function
    """
    import typesystem
    typ = typesystem.String()
    assert validate_yaml(b"hello", typ)[0] == "hello"

    try:
        _ = validate_yaml(b"hello", (1, 2, 3))
        assert False
    except TypeError:
        pass

    typ = typesystem.String()
    try:
        _ = validate_yaml(b"{1:2, 3:4}", typ)
        assert False
    except typesystem.ParseError:
        pass

    try:
        _ = validate_yaml(b"[1, 2, 3]", typ)
        assert False
    except typesystem.ParseError:
        pass


# Generated at 2022-06-14 15:03:47.728043
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b"""
    name: Barry Smith
    age: 19
    """
    validator = Schema(
        {
            "name": Field(type="string"),
            "age": Field(type="integer", minimum=18, maximum=65),
        }
    )
    value, error_messages = validate_yaml(content=content, validator=validator)
    assert isinstance(value, dict)
    assert value == {"name": "Barry Smith", "age": 19}
    assert isinstance(error_messages, list)
    assert not any(error_messages)

    content = b"""
    name: Barry Smith
    age: 75
    """
    value, error_messages = validate_yaml(content=content, validator=validator)
    assert isinstance(value, dict)

# Generated at 2022-06-14 15:03:56.540885
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import IntegerField

    class PersonSchema(Schema):
        name = IntegerField(max_value=10)
        age = IntegerField(max_value=100)

    value, errors = validate_yaml("""
        name: 9
        age: 21
    """, PersonSchema())

    assert value == {"name": 9, "age": 21}

    value, errors = validate_yaml("""
        name: 1
        age: 21
    """, PersonSchema())

    assert value == {"name": 1, "age": 21}

    value, errors = validate_yaml("""
        name: 11
        age: 21
    """, PersonSchema())

    assert value == {"name": 11, "age": 21}

    assert len(errors)

# Generated at 2022-06-14 15:04:04.422527
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("[]") == ListToken([], start=0, end=1, content="[]")
    assert tokenize_yaml("{}") == DictToken({}, start=0, end=1, content="{}")
    assert tokenize_yaml("1") == ScalarToken(1, start=0, end=1, content="1")
    assert tokenize_yaml("1.2") == ScalarToken(1.2, start=0, end=3, content="1.2")
    assert tokenize_yaml("bar") == ScalarToken("bar", start=0, end=3, content="bar")
    assert tokenize_yaml("1:2") == DictToken({1: 2}, start=0, end=3, content="1:2")



# Generated at 2022-06-14 15:04:10.543378
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(content = "hello", validator = "string") == "hello"
    try:
        validate_yaml(content = "hello", validator = 5)
    except AssertionError as e:
        assert "must be an instance of 'Field'" in str(e)
    try:
        validate_yaml(content = "hello", validator = "boolean")
    except ValidationError as e:
        assert e.text == "Must be True or False."


# Generated at 2022-06-14 15:04:13.949756
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String

    errors = validate_yaml('name: "test"', String())
    assert len(errors) > 0

    errors = validate_yaml('{"name": "test"}', String())
    assert len(errors) == 0

# Generated at 2022-06-14 15:04:24.349810
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    validator = Field(name="testField", type="string")

    content = "test-str"
    token = tokenize_yaml(content)
    assert token.type == "string"
    assert token.value == "test-str"
    value, error_messages = validate_yaml(content, validator)
    assert value == "test-str"
    assert len(error_messages) == 0
    assert token.start == 0
    assert token.end == 8

    content2 = "test-int: 1"
    token2 = tokenize_yaml(content2)
    assert token2.type == "dict"
    value2, error_messages2 = validate_yaml(content2, validator)
    assert error_messages2[0]["text"] == "Expected a string."
    assert error

# Generated at 2022-06-14 15:04:40.317143
# Unit test for function validate_yaml
def test_validate_yaml():
    # Correct YAML content
    validator=Field(type="string")
    content='"Hello, World!"'
    assert validate_yaml(content, validator) == ('Hello, World!', None)

    # Empty YAML content
    content=''
    with pytest.raises(ParseError):
        validate_yaml(content, validator)

    # Invalid YAML content
    content='{"Invalid YAML"'
    with pytest.raises(ParseError):
        validate_yaml(content, validator)

    # YAML content with invalid data for the given validator
    content='{"Invalid data for a string"}'
    with pytest.raises(ParseError):
        validate_yaml(content, validator)

# Generated at 2022-06-14 15:04:48.747803
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        foo = Field(key=True)
        bar = Field(optional=True)

    value, errors = validate_yaml(
        b"""
        foo: a
        bar: b
        """,
        validator=TestSchema,
    )
    assert value == {"foo": "a", "bar": "b"}
    assert errors == []

    value, errors = validate_yaml(
        b"foo: a\nbar: b", validator=TestSchema
    )
    assert value == {"foo": "a", "bar": "b"}
    assert errors == []

    value, errors = validate_yaml(
        b"foo: b\nbar: b", validator=TestSchema
    )
    assert value is None
    assert len(errors) == 1
   

# Generated at 2022-06-14 15:04:56.499106
# Unit test for function validate_yaml
def test_validate_yaml():
    text = '''
    fname: John
    lname: Doe
    email:
    - john@doe.com
    - john@test.com
    '''
    value, messages = validate_yaml(text, UserSchema)
    assert value['fname'] == 'John'
    assert value['lname'] == 'Doe'
    assert value['email'] == ['john@doe.com', 'john@test.com']
    assert messages[0]['id'] == 'dickens'
    assert messages[0]['text'] == 'Required.'


# Generated at 2022-06-14 15:05:06.704967
# Unit test for function validate_yaml
def test_validate_yaml():
    #Given
    content = """
    - first_name: Peter
      last_name: Parker
      age: 15
      hobbies:
        - computer games
        - guitar
    - first_name: Bruce
      last_name: Wayne
      age:
        - 30
        - 40
    """
    validator = Schema(
        {
            "first_name": str,
            "last_name": str,
            "age": int,
            "hobbies": [str],
        },
    )

    #When
    value, errors = validate_yaml(content, validator)

    #Then
    assert type(errors) == list
    assert errors[0].text == "Not a valid integer."
    assert errors[0].position.line_no == 9
    assert errors[0].position.column_no == 12


# Generated at 2022-06-14 15:05:08.289430
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml("foobar", Field(type="string")) == ("foobar", [])


# Generated at 2022-06-14 15:05:11.659229
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b'name: Yaser'
    class Person(Schema):
        name = String()
    value, error_msgs = validate_yaml(content, validator=Person)
    assert isinstance(value, dict)

# Generated at 2022-06-14 15:05:23.706446
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = Field(type=str)
        age = Field(type=int)
        address = Field(type=str)
        is_admin = Field(type=bool)

    content = b"""
    name: Mary
    age: 30
    address: 'New York'
    is_admin: True
    """

    value, error_messages = validate_yaml(
        content=content, validator=PersonSchema
    )
    # print(value, error_messages)

    assert value == {
        "name": "Mary",
        "age": 30,
        "address": "New York",
        "is_admin": True,
    }
    assert len(error_messages) == 0


# Generated at 2022-06-14 15:05:36.464025
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String

    validator = String(name="name")

    data = """
    name: Don Draper
    phone_number: (212) 555-1212
    """

    parsed_value, error_messages = validate_yaml(data, validator)

    assert parsed_value == "Don Draper"
    assert len(error_messages) == 1
    assert error_messages[0].code == "invalid_field"
    assert error_messages[0].position == (
        Position(column_no=2, line_no=2, char_index=14),
        Position(column_no=22, line_no=2, char_index=34),
    )
    assert error_messages[0].text == '"phone_number" is not a valid field.'



# Generated at 2022-06-14 15:05:43.025463
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("{}") == DictToken({}, 0, 1)
    assert tokenize_yaml("{key: value}") == DictToken({"key": "value"}, 0, 14)
    assert tokenize_yaml("[1, 2, 3]") == ListToken([1, 2, 3], 0, 10)
    assert tokenize_yaml("item") == ScalarToken("item", 0, 4)

# Generated at 2022-06-14 15:05:51.068941
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String, Int, Bool, List, Dict
    class A(Schema):
        name = String(max_length=10)
        value = Int(minimum=0)
        a = Bool()
        b = Bool()
        c = Bool(required=False)
        d = List()
        e = List(items=Dict(properties={'a': String()}))

    valid_example = """
    name: aaaaa
    value: 10
    a: yes
    b: true
    d: [1,2,3]
    e: [{a: a}, {a: b}]
    """
    value, errors = validate_yaml(valid_example, A)
    assert not errors

# Generated at 2022-06-14 15:06:02.364442
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = fields.String(max_length=20)
        age = fields.Integer(minimum=0, maximum=100)

    content = "name: Paul\nage: 99\n"

    value, error_messages = validate_yaml(content, TestSchema)

    assert value == {'name': 'Paul', 'age': 99}
    assert error_messages == []

# Generated at 2022-06-14 15:06:07.004868
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String(max_length=50)
        age = Integer(minimum=0, maximum=150)

    content = """
    name: Steve
    age: 20
    """

    value, errors = validate_yaml(content, Person)

    assert value == {"name": "Steve", "age": 20}
    assert errors == []



# Generated at 2022-06-14 15:06:12.625177
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = StringField()
        age = StringField()

    content = """
    name: John
    age: "20"
    """
    value, error_messages = validate_yaml(content, PersonSchema)
    assert value == {'name': 'John', 'age': '20'}
    assert error_messages == []
