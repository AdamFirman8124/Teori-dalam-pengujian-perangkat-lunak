

# Generated at 2022-06-14 14:56:36.873022
# Unit test for function validate_yaml
def test_validate_yaml():
    class AuthorSchema(Schema):
        name = Field(type="string", required=True)
        age = Field(type="integer", required=True)
        favourite_colour = Field(type="string", required=True)

        class Meta:
            strict = True

    class BookSchema(Schema):
        title = Field(type="string", required=True)
        author = Field(type="object", required=True, schema_cls=AuthorSchema)

        class Meta:
            strict = True

    schema = BookSchema()

    valid_data = """
    title: "The Prince"
    author:
        name: "Niccolò Machiavelli"
        age: 64
        favourite_colour: 'green'
    """


# Generated at 2022-06-14 14:56:48.234069
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(
        {
            "title": "Example Schema",
            "type": "object",
            "properties": {
                "firstName": {
                    "type": "string"
                },
                "lastName": {
                    "type": "string"
                },
                "age": {
                    "description": "Age in years",
                    "type": "integer",
                    "minimum": 0
                }
            },
            "required": ["firstName", "lastName"]
        }
    )

    data = """
        firstName: John
        lastName: Doe
        age: 21
    """
    value, error_messages = validate_yaml(data, schema)
    print(value)
    print(error_messages)

# Generated at 2022-06-14 14:56:57.556754
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("hello") == "hello"
    assert tokenize_yaml(b"hello") == "hello"
    assert tokenize_yaml("1") == 1
    assert tokenize_yaml("1.0") == 1.0
    assert tokenize_yaml("true") is True
    assert tokenize_yaml("false") is False
    assert tokenize_yaml("null") is None
    assert tokenize_yaml("1\n2\n3") == [1, 2, 3]
    assert tokenize_yaml("{ a: 1 }") == {"a": 1}
    token = tokenize_yaml("[{ a: 1 }]")
    assert isinstance(token, list)
    assert isinstance(token[0], dict)


# Generated at 2022-06-14 14:57:05.216952
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    expected_tokens = {
        "empty": "",
        "string": "hello",
        "int": 1,
        "float": 1.1,
        "bool": "true",
        "null": "null",
        "dict": "{a: 1}",
        "list": "[1, 2]",
    }
    for t in expected_tokens:
        tokens = tokenize_yaml(expected_tokens[t])
        if t == "empty":
            assert len(tokens) == 0
        else:
            assert tokens.content == expected_tokens[t]



# Generated at 2022-06-14 14:57:10.078155
# Unit test for function validate_yaml
def test_validate_yaml():
    result = validate_yaml(content = '6', validator = Field(name = 'helloworld', type_ = int))
    assert result[0] == Message(value = '6', position = Position(line_no = 1, column_no = 1, char_index = 0))
    assert not result[1]



# Generated at 2022-06-14 14:57:21.093798
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("test: 1234") == DictToken({'test': int(1234)}, 0, 10, content='test: 1234')
    assert tokenize_yaml("- 1234") == ListToken([int(1234)], 0, 5, content='- 1234')
    assert tokenize_yaml("1234") == ScalarToken(1234, 0, 4, content='1234')
    assert tokenize_yaml("- 1234\n- 2345") == \
           ListToken([int(1234), int(2345)], 0, 13, content='- 1234\n- 2345')

# Generated at 2022-06-14 14:57:27.236910
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    from typesystem import String, Integer, Schema

    content = """
    name: Alex
    age: 25
    """

    value, error_messages = validate_yaml(
        content, Schema({"name": String(max_length=10), "age": Integer()})
    )
    assert error_messages == []

# Generated at 2022-06-14 14:57:34.490159
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String(max_length=100)
        age = Integer()

    content = """
    name: "Foo Bar"
    age: 30
    """

    value, errors = validate_yaml(content, Person)
    assert value == {"name": "Foo Bar", "age": 30}
    assert errors == []

    content = """
    name: "Foo Bar"
    age: "invalid"
    """
    value, errors = validate_yaml(content, Person)
    assert errors == [
        Message('Invalid value supplied. Expected an integer.', 'invalid_type', {'name': 'age'}, Position(12, 5, 36))
    ]

    content = """
    name: "Foo Bar"
    age: "invalid"
    """

    content

# Generated at 2022-06-14 14:57:44.227963
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    from typesystem.base import ParseError
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken, Token
    # Create the YAML input.
    yaml_input = """
    hello:
      - one
      - two
      - three
    """
    # Tokenize the YAML input.
    token = tokenize_yaml(yaml_input)
    # Assert that the tokenized output matches the structure of the YAML input.
    expected_dict_token = DictToken(
        {
            "hello": ListToken(
                [ScalarToken("one"), ScalarToken("two"), ScalarToken("three")]
            )
        },
        0,
        len(yaml_input) - 1,
        yaml_input,
    )

# Generated at 2022-06-14 14:57:54.293208
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
        dog:
          - name: Fido
            age: 3
        cat:
          - name: Fluffy
            age: 7
    """
    token = tokenize_yaml(content)
    assert len(token) == 2
    assert token.get("dog") and len(token["dog"]) == 1
    assert token.get("cat") and len(token["cat"]) == 1
    assert token["dog"][0].get("name") == "Fido"
    assert token["dog"][0].get("age") == 3
    assert token["cat"][0].get("name") == "Fluffy"
    assert token["cat"][0].get("age") == 7


if __name__ == "__main__":
    test_tokenize_yaml()

# Generated at 2022-06-14 14:58:02.415372
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(properties={"name": {"type": "string"}, "age": {"type": "integer"}})
    assert validate_yaml(content="""name: john\nage: 2\n""", validator=schema) == ({'name': 'john', 'age': 2}, None)

# Generated at 2022-06-14 14:58:12.105687
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer

    class ChildSchema(Schema):
        field_string = String()
        field_int = Integer()

    class ParentSchema(Schema):
        field_string = String()
        field_list = List[ChildSchema]()
        field_dict = Dict[String, ChildSchema]()

    # Valid YAML content
    valid_content = '''
            field_string: this is valid
            field_list:
              - field_string: valid 1
                field_int: 20
              - field_string: valid 2
                field_int: 30
            field_dict:
              one:
                field_string: valid 1
                field_int: 20
              two:
                field_string: valid 2
                field_int: 30
            '''

    _, errors = validate

# Generated at 2022-06-14 14:58:23.181800
# Unit test for function validate_yaml
def test_validate_yaml():
    # given
    content = """
    field1: '1'
    field2:
        -
            field3: '3'
            field4: '4'
        -
            field5: true
            field6: false
    """
    class TestSchema(Schema):
        field1 = Field(type="str", format_validators=["int"])
        field2 = Field(type="list", items=Field(type="dict", properties={"field3": "str"}))

    # when
    value, errors = validate_yaml(content=content, validator=TestSchema)

    # then
    assert len(errors) == 4

# Generated at 2022-06-14 14:58:31.977315
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema([
        Field(name='name', required=True, type_hint=str),
        Field(name='age', type_hint=int),
    ])

    value, error = validate_yaml('name: John\nage: 43', schema)
    assert error == []

    value, error = validate_yaml('name: John', schema)
    assert error == [Message(code="required", field_name="age", text="This field is required.")]

    value, error = validate_yaml('name: John\nage: 43', schema)
    assert error == []

    yaml = '''name: 
        first: Bob
        last: Smith
    age: 43'''
    value, error = validate_yaml(yaml, schema)

# Generated at 2022-06-14 14:58:35.373296
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
        id: 1
        title: Hello, World!
    """
    errors = validate_yaml(content,
        Schema([Field('id', str, required=True), Field('title', str)])
    )
    assert len(errors.messages) == 1
    assert errors.messages[0].code == 'type_error'
    assert errors.messages[0].position.line_no == 2
    assert errors.messages[0].position.column_no == 3


# Generated at 2022-06-14 14:58:43.250319
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema

    class PersonSchema(Schema):
        first_name = String()
        last_name = String()

    schema = PersonSchema()

    content = """
        first_name: Michael
        last_name: "Meyers-Crothers"
    """
    value, error_messages = validate_yaml(content=content, validator=schema)
    assert error_messages == []

    content = """
        first_name:
        last_name: Meyers-Crothers
    """
    value, error_messages = validate_yaml(content=content, validator=schema)
    assert len(error_messages) == 1
    assert error_messages[0].field_name == "first_name"


# Generated at 2022-06-14 14:58:53.541348
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from yaml.loader import SafeLoader
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class User(Schema):
        name = String(max_length=10)
        email = String()
        address = String()
        city = String()
        state = String()
        age = Int()
        zip = String()

    content = '''
    name: Josh
    email: josh@example.com
    address: 123 Main St
    city: Ann Arbor
    state: MI
    age: "40"
    zip: 48104
    '''
    value, errors = validate_yaml(content, User)

    User.validate(value)
    from pytest import raises
    with raises(ValidationError):
        User().validate(value)

# Generated at 2022-06-14 14:59:05.592647
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("10").value == 10
    assert tokenize_yaml("10\n").value == 10  # tolerate newline at end
    assert tokenize_yaml("'foo'").value == "foo"
    assert tokenize_yaml("foo").value == "foo"
    assert tokenize_yaml("foo:bar").value == {"foo": "bar"}
    assert tokenize_yaml("10").position == (0, 1, 0)
    assert tokenize_yaml("10\n").position == (0, 2, 0)
    assert tokenize_yaml("foo:bar").position == (0, 4, 2)
    assert tokenize_yaml("foo:").position == (0, 3, 3)
    assert tokenize_yaml("foo: bar").position == (0, 6, 3)


# Generated at 2022-06-14 14:59:15.657527
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, Schema
    from typesystem.fields import Any
    from typesystem.schemas import Schema
    from typesystem.yaml.dataclass import dataclass
    from typesystem.yaml.load import load_yaml
    from typesystem.yaml.tokenize import tokenize_yaml, validate_yaml

    content = """
    - name: First entry
      value: 123
    - name: Second entry
      value: 456
    """

    schema = Schema([{"name": "name", "type": "string"}, {"name": "value", "type": "integer"}])

    value, errors = validate_yaml(content, schema)
    assert not errors


# Generated at 2022-06-14 14:59:24.507487
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''
        first: P1
        second: P2
    '''

    class MySchema(Schema):
        first = Field(max_length=2)
        second = Field(max_length=3)

    value, errors = validate_yaml(content, MySchema)
    assert not errors
    assert isinstance(value, dict)
    assert value["first"] == "P1"

    content = '''
        first: 12345
        second: P2
    '''

    value, errors = validate_yaml(content, MySchema)
    assert isinstance(errors, list)
    assert len(errors) == 1
    assert isinstance(errors[0], ValidationError)
    assert errors[0].code == "string_too_long"


# Generated at 2022-06-14 14:59:35.642921
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer, String, Schema

    class Person(Schema):
        name = String()
        age = Integer()

    schema = Person()

    content = """
name: John
age: 33
"""

    yaml_str = "name: John\nage: 33\n"

    value, error_messages = validate_yaml(content, schema)
    assert value == {"name": u"John", "age": 33}
    assert len(error_messages) == 0

    value, error_messages = validate_yaml(yaml_str, schema)
    assert value == {"name": u"John", "age": 33}
    assert len(error_messages) == 0

    content = """
name: John
age: foo
"""


# Generated at 2022-06-14 14:59:39.644524
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("{}") == DictToken({}, 0, 1, content="{}")
    assert tokenize_yaml("[]") == ListToken([], 0, 1, content="[]")
    assert tokenize_yaml("a") == ScalarToken("a", 0, 1, content="a")
    assert tokenize_yaml('"a"') == ScalarToken("a", 0, 3, content='"a"')
    assert tokenize_yaml('"a\\"b"') == ScalarToken('a"b', 0, 6, content='"a\\"b"')
    assert tokenize_yaml("1") == ScalarToken(1, 0, 1, content="1")

# Generated at 2022-06-14 14:59:49.963779
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        email = Email()
        age = Int()

    yaml_data = '''
    email: invalid
    age: "invalid"
    '''

    expected_errors = [
        Message(
            text="A valid email address is required.",
            code="invalid_format",
            position=Position(
                line_no=2, column_no=8, char_index=15
            ),
            type="email",
        ),
        Message(
            text="Must be an integer.",
            code="not_integer",
            position=Position(line_no=3, column_no=8, char_index=23),
            type="int",
        ),
    ]

    data, errors = validate_yaml(yaml_data, validator=UserSchema)

    assert data

# Generated at 2022-06-14 14:59:58.459257
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    title:     Typesystem
    author:
        name:  Josh
        email: josh@josh.com
    """

    class BookSchema(Schema):
        title = "text"
        author = {"name": "text", "email": "email"}

    result, messages = validate_yaml(content, BookSchema)
    assert result == {
        "title": "Typesystem",
        "author": {"name": "Josh", "email": "josh@josh.com"},
    }
    assert messages == []



# Generated at 2022-06-14 15:00:00.836731
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml('{"key": "value"}')
    assert isinstance(token, DictToken)
    assert token.raw_value == {"key": "value"}



# Generated at 2022-06-14 15:00:12.837257
# Unit test for function validate_yaml
def test_validate_yaml():

    from django.contrib.auth.hashers import PBKDF2PasswordHasher
    from typesystem.types import Array
    from typesystem.fields import Boolean, Integer, Number, Ref, SchemaField
    from typesystem.schemas import Schema

    class UserSchema(Schema):

        username = Ref("#/components/schemas/User/properties/username")
        password = Ref("#/components/schemas/User/properties/password")
        is_active = Ref("#/components/schemas/User/properties/is_active")

    class AuthTokenSchema(Schema):

        user_id = Ref("#/components/schemas/AuthToken/properties/user_id")
        token = Ref("#/components/schemas/AuthToken/properties/token")


# Generated at 2022-06-14 15:00:24.382281
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        foo = {"type": "string"}
        bar = {"type": "integer"}

    value, error = validate_yaml('{"foo": "hello", "bar": "world"}', TestSchema)
    expected_error = ValidationError(
        text="Value must be of type 'integer'.",
        code="invalid_type",
        position=Position(line_no=1, column_no=18, char_index=17),
    )
    assert error == expected_error

    value, error = validate_yaml('[{"foo": "hello"}]', TestSchema(many=True))

# Generated at 2022-06-14 15:00:29.318630
# Unit test for function validate_yaml
def test_validate_yaml():
    # Check that ParseErrors are raised normally
    with pytest.raises(ParseError) as excinfo:
        validate_yaml("1+2", Field())  # type: ignore

    # Check that validation errors are caught and that the position is
    # correctly marked
    errors = validate_yaml("1", IntegerType())[1]
    assert isinstance(errors[0], ValidationError)
    assert errors[0].position is not None
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no == 0
    assert errors[0].position.char_index == 0

# Generated at 2022-06-14 15:00:39.630327
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.tokenize.basic_tokens import BasicDictToken, BasicListToken, BasicScalarToken
    from typesystem.tokenize.enforced_tokens import EnforcedListToken, EnforcedDictToken
    from typesystem.tokenize.positional_validation import (
        create_validation_errors,
        get_validation_error_message,
        serialize_validation_error_message,
    )
    from typesystem.tokenize.tokens import Token

    class EmptySchema(Schema):
        pass

    class BasicField(Field):
        def _get_token_type(self) -> typing.Type[Token]:
            return BasicScalarToken

    class BasicListField(Field):
        def _get_token_type(self) -> typing.Type[Token]:
            return Basic

# Generated at 2022-06-14 15:00:49.846203
# Unit test for function validate_yaml
def test_validate_yaml():
    # Error Messages
    assert("error_list" in [t.code for t in validate_yaml("{}", Schema).messages])
    assert("error_list" in [t.code for t in validate_yaml("{}", "Schema").messages])
    assert("error_list" in [t.code for t in validate_yaml("{}", "String").messages])
    assert("error_list" in [t.code for t in validate_yaml("{}", "Integer").messages])
    assert("error_list" in [t.code for t in validate_yaml("{}", "Number").messages])
    assert("error_list" in [t.code for t in validate_yaml("{}", "Boolean").messages])

# Generated at 2022-06-14 15:00:56.507819
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    print("\nTest tokenize_yaml")
    assert tokenize_yaml("""\
    foo: bar
    baz: buzz
    """) == [{
        "baz": "buzz",
        "foo": "bar"
    }]


# Generated at 2022-06-14 15:01:08.366190
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        a = {"type": "string"}
        b = {"type": "string"}

    content = "a: hello\nb: world"
    actual_value, actual_messages = validate_yaml(content, TestSchema)
    expected_value = {"a": "hello", "b": "world"}
    expected_messages = []
    assert actual_value == expected_value
    assert actual_messages == expected_messages

    content = "a: hello\nb: world\nc: extra"
    actual_value, actual_messages = validate_yaml(content, TestSchema)
    expected_value = {"a": "hello", "b": "world", "c": "extra"}
    expected_messages = []
    assert actual_value == expected_value
    assert actual_mess

# Generated at 2022-06-14 15:01:14.845904
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import Integer, Text, Array

    class MessageSchema(Schema):
        nums = Array[Integer]
        name = Text()

    message = MessageSchema.validate_yaml("nums: [1, 2]\nname: test")
    print(f"message: {message}")
    assert message.errors == []
    assert message.value == {"nums": [1, 2], "name": "test"}

if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 15:01:22.557320
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("- 1\n- 2\n- 3")
    assert token.start == 0
    assert token.end == 8
    assert token.content == "- 1\n- 2\n- 3"
    assert token.extract() == ["1", "2", "3"]
    assert token.positions[0].line_no == 1
    assert token.positions[1].line_no == 2
    assert token.positions[2].line_no == 3
    assert token.positions[0].column_no == 2
    assert token.positions[1].column_no == 2
    assert token.positions[2].column_no == 2



# Generated at 2022-06-14 15:01:33.940059
# Unit test for function validate_yaml
def test_validate_yaml():
    if yaml is not None:
        from typesystem.fields import String
        from typesystem.schemas import Schema

        class Person(Schema):
            name = String(max_length=10)

        content = "name: John Doe"
        Person(name="John Doe")
        value, error_messages = validate_yaml(content, Person)
        assert value == {"name": "John Doe"}

        content = "name: " + "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        value, error_messages = validate_yaml(content, Person)
        position = Position(line_no=1, column_no=7, char_index=6)

# Generated at 2022-06-14 15:01:44.485899
# Unit test for function validate_yaml
def test_validate_yaml():
    import pytest
    content = """
    - a
    - b
    - c
    """
    response = validate_yaml(content, List(Integer))
    assert response[0] == [1, 2, 3]
    assert response[1] == []
    content = """
    - a
    - b
    - c
    """
    with pytest.raises(ValidationError) as exc_info:
        validate_yaml(content, List(String))
    assert exc_info.value.code == "invalid_value"
    assert exc_info.value.position == Position(
        line_no=2, column_no=5, char_index=5
    )

# Generated at 2022-06-14 15:01:55.733264
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b"""
    user:
        name: John Doe
        email: john.doe@example.com
        profile:
            sex: male
            age: 42
        favorites:
            - movie: Blade Runner 2049
              stars: 3
            - movie: Eternal Sunshine of the Spotless Mind
              stars: 4
            - movie: Spirited Away
              stars: 5
        website: https://example.com/john.doe
    """

# Generated at 2022-06-14 15:02:03.617838
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import fields
    from typesystem.schemas import Schema
    from typesystem.base import Type

    class UserSchema(Schema):
        name = fields.String(required=True)
        age = fields.Integer(required=True)


    class User(Type):
        schema = UserSchema


    user = User.from_content("""
    name: Bob
    age: 42
    """)

    assert user.data == {"name": "Bob", "age": 42}



# Generated at 2022-06-14 15:02:11.398160
# Unit test for function validate_yaml
def test_validate_yaml():
    class SchemaYaml(Schema):
        name = "string"
        favorite_number = "integer"

    content = "name: brian\nfavorite_number: 3"
    value, error_messages = validate_yaml(content, validator=SchemaYaml)
    assert value == {"name": "brian", "favorite_number": 3}
    assert not error_messages

    content = "name: 'brian'"
    value, error_messages = validate_yaml(content, validator=SchemaYaml)
    assert value == {"name": "brian"}
    assert not error_messages



# Generated at 2022-06-14 15:02:21.778913
# Unit test for function validate_yaml
def test_validate_yaml():
    # Invalid content
    content = '{"field": "value"}'
    validator = Field()
    value, errors = validate_yaml(content, validator)

    assert value == {}
    assert errors[0].text == "Invalid YAML."
    assert errors[0].code == "invalid_yaml"
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no == 1
    assert errors[0].position.char_index == 0

    # Valid content
    content = '{"field": "value"}'
    validator = Field(key="field", required=True)
    value, errors = validate_yaml(content, validator)

    assert value == {"field": "value"}
    assert errors == []



# Generated at 2022-06-14 15:02:26.499088
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    fruit: apples
    size: 1
    color: green
    """
    myschema = Schema(
        {
            "fruit": "str",
            "size": "int",
            "color": "str",
        }
    )
    result = validate_yaml(content, myschema)
    assert result[0]["size"] == 1



# Generated at 2022-06-14 15:02:34.668654
# Unit test for function validate_yaml
def test_validate_yaml():
    try:
        import yaml
    except ImportError:  # pragma: no cover
        pass  # type: ignore
    else:
        from typesystem import String, Integer

        class PetSchema(Schema):
            name = String(max_length=100)
            age = Integer(min_value=0)

        content = "name: Spot\nage: 3"
        value, errors = validate_yaml(content, validator=PetSchema)
        assert value == {"name": "Spot", "age": 3}
        assert errors == []

        content = "name: Spot\nage: -1"
        value, errors = validate_yaml(content, validator=PetSchema)
        assert value is None
        assert errors[0].text == "Ensure this value is greater than or equal to 0."
        assert errors

# Generated at 2022-06-14 15:02:45.319529
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.base import ValidationError
    from typesystem.tokenize.tokens import Token
    from typing import Mapping, Any
    import pytest

    class MySchema(Schema):
        name = String(required=True)

    _, msg = validate_yaml(b"{}", MySchema)
    assert isinstance(msg[0], ValidationError)
    assert "required" in msg[0].text

    _, msg = validate_yaml(b'{"name": "Finn"}', MySchema)
    assert msg == []

    _, msg = validate_yaml(b'{"name": 42}', MySchema)
    assert isinstance(msg[0], ValidationError)


# Generated at 2022-06-14 15:02:56.251427
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer
    from typesystem.schemas import Schema

    class MySchema(Schema):
        n = Integer(minimum=0, maximum=100)

    valid_yaml_data = b"""
    n: 10
    """

    invalid_yaml_data = b"""
    n: 110
    """

    (value, error_messages) = validate_yaml(valid_yaml_data, MySchema)
    assert value == {"n": 10}
    assert error_messages == []

    (value, error_messages) = validate_yaml(invalid_yaml_data, MySchema)
    assert value is None
    assert isinstance(error_messages[0], ValidationError)
    assert len(error_messages) == 1

# Generated at 2022-06-14 15:03:03.912342
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema()
    schema.add_field("name", str)
    schema.add_field("age", int, required=False)
    value, errors = validate_yaml(
        b"name: fred\n"
        b"age: 30",
        schema,
    )

    assert value == {"name": "fred", "age": 30}
    assert errors == []



# Generated at 2022-06-14 15:03:10.555003
# Unit test for function validate_yaml
def test_validate_yaml():
    # given
    class AccountSchema(Schema):
        id = fields.Integer()
        name = fields.String(title="Name of individual")
        roles = fields.List(fields.String)

    test_schema = AccountSchema(description="A schema for testing purposes.")

    # when
    content = """
id: 20
name: Jane
roles:
  - admin
"""
    (value, error_messages) = validate_yaml(content, test_schema)

    # then
    assert isinstance(value, dict)
    assert value == {'id': 20, 'name': 'Jane', 'roles': ['admin']}
    assert error_messages == []



# Generated at 2022-06-14 15:03:22.112627
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(properties={'foo': ValidationError('error')})
    content = 'foo: bar'
    value, messages = validate_yaml(content, schema)
    assert value == {}
    assert len(messages) == 1
    assert messages[0].text == 'error'
    assert messages[0].code == 'error'
    assert messages[0].position.column_no == 4
    assert messages[0].position.line_no == 1
    assert messages[0].position.char_index == 4

    schema = Schema(properties={'foo': 'foo'})
    content = 'foo: bar'
    value, messages = validate_yaml(content, schema)
    assert value == {'foo': 'bar'}
    assert len(messages) == 0


# Generated at 2022-06-14 15:03:26.807318
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = String()

    yaml_content = '{"name": "truc", "email": "truc@truc.com"}'
    value, error_messages = validate_yaml(yaml_content, PersonSchema)

if __name__ == "__main__":
    test_validate_yaml()

# Generated at 2022-06-14 15:03:37.257940
# Unit test for function validate_yaml
def test_validate_yaml():
    def assert_validation_error(validator, content, expected_error_message):
        value, error_messages = validate_yaml(content, validator=validator)
        assert value is None
        assert error_messages == [
            Message(
                text=expected_error_message,
                code="type_error",
                position=Position(
                    char_index=0,
                    column_no=1,
                    line_no=1,
                ),
            ),
        ]

    assert_validation_error(
        Integer(),
        "value: totebag",
        expected_error_message="Invalid type. Expected an integer.",
    )
    assert_validation_error(
        String(),
        "value:",
        expected_error_message="Invalid type. Expected a string.",
    )
   

# Generated at 2022-06-14 15:03:44.453066
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = String(max_length=100)
        age = Integer(minimum=0, maximum=100)

    yaml = """
    name: Foo
    age: 111
    """

    value, errors = validate_yaml(yaml, PersonSchema)
    assert errors[0].text == "Value must be less than or equal to 100."
    assert errors[0].position.column_no == 9
    assert errors[0].position.line_no == 3

# Generated at 2022-06-14 15:03:55.696087
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test that a simple YAML string validates successfully.
    assert validate_yaml(
        content='"string"', validator=Field(type="string")
    ) == ("string", None)

    # Test that a complex YAML string validates successfully.

# Generated at 2022-06-14 15:04:06.450755
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    content = "key: value"
    validator = Field()
    value, error_messages = validate_yaml(content, validator)
    assert {'key': 'value'} == value
    assert type(error_messages) == list
    content = "key: value\nkey: value1"
    validator = Field()
    value, error_messages = validate_yaml(content, validator)
    assert {'key': 'value1'} == value
    assert type(error_messages) == list
    content = "key: value\nkey: value1"
    validator = Field(max_length=5)
    value, error_messages = validate_yaml(content, validator)
    assert None == value
   

# Generated at 2022-06-14 15:04:16.431232
# Unit test for function validate_yaml
def test_validate_yaml():
    class PetSchema(Schema):
        name = Field(type=str)
        age = Field(type=int)

    assert validate_yaml('name: Spot\nage: 18', PetSchema) == ({'name': 'Spot', 'age': 18}, [])
    assert validate_yaml('name: Spot', PetSchema) == (None, [
    {'code': 'required', 'text': 'This field is required.', 'position': {'line_no': 2, 'column_no': 1, 'char_index': 10}}])

# Generated at 2022-06-14 15:04:26.201827
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
        name: "Will Smith"
        age: 28
        is_swimmer: false
    """
    validator = {
        "name": "string",
        "age": "integer",
        "is_swimmer": "boolean",
    }
    value, error_messages = validate_yaml(content, validator)
    assert len(error_messages) == 0
    assert value == {
        "name": "Will Smith",
        "age": 28,
        "is_swimmer": False
    }

    content = """
        name: "Will Smith"
        age: 28
        is_swimmer: true
        foo: "bar"
        baz: 100
    """
    value, error_messages = validate_yaml(content, validator)

# Generated at 2022-06-14 15:04:30.063616
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    first_name: "Jane"
    last_name:  "Doe"
    birth_year: 1930
    """
    class Person(Schema):
        first_name = fields.String()
        last_name = fields.String()
        birth_year = fields.Integer()

    Person().validate(content)


# Generated at 2022-06-14 15:04:41.481914
# Unit test for function validate_yaml
def test_validate_yaml():
    import os
    import json

    # Get current directory and parent directory
    current_dir = os.path.dirname(__file__)
    parent_dir = os.path.dirname(current_dir)
    # Set path to the YAML file
    file_path = os.path.join(parent_dir, "tests", "data", "countries.yaml")

    with open(file_path) as f:
        content = f.read()
        value, error_messages = validate_yaml(content, validator=Schema)
        assert not error_messages
        assert isinstance(value, Token)
        # Get the length of the parsed YAML file to make sure it is the same

# Generated at 2022-06-14 15:04:49.314464
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema

    class UserSchema(Schema):
        name = "string"
        age = "integer"

    # Simple YAML
    string = """
    name: hello
    age: 27
    """

    value, error_messages = validate_yaml(string, UserSchema)
    assert error_messages == []

    assert isinstance(value["name"], ScalarToken)
    assert value["name"].value == "hello"
    assert value["name"].start == 8
    assert value["name"].end == 13

    assert isinstance(value["age"], ScalarToken)
    assert value["age"].value == 27
    assert value["age"].start == 25
    assert value["age"].end == 27

    # Fail to parse

# Generated at 2022-06-14 15:04:58.653933
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    document = """
    a: Hello World
    b:
      - item 1
      - item 2
    c:
      c1: foo
      c2: bar
    """

    result = tokenize_yaml(document)


# Generated at 2022-06-14 15:05:03.301423
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
        Some content here
        hello: world
        i:
          - a
          - b
          - c
        x: 1
        """
    validator = typing.TypeVar('validator', bound=typing.Union[Field, typing.Type[Schema]])
    assert validate_yaml(content=content, validator=validator)

# Generated at 2022-06-14 15:05:10.654426
# Unit test for function validate_yaml
def test_validate_yaml():
    import tempfile
    from typesystem.tokenize.positional_validation import validate_with_positions
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken
    from typesystem.types import Boolean, Integer, Number, String as StringType

    def get_validator(
        validator: typing.Union[Field, typing.Type[Schema]],
        content: str,
    ) -> typing.Any:
        token = tokenize_yaml(content)
        return validate_with_positions(token, validator)


# Generated at 2022-06-14 15:05:21.521662
# Unit test for function validate_yaml
def test_validate_yaml():
        yaml_str = '''
        key1: val1
        key2: val2
        '''
        schema1 = Schema(field1=str, field2=str)
        value, errors = validate_yaml(yaml_str, schema1)
        assert errors is None, 'We have found a YAML error'
        assert value is not None, 'Value is not set'
        assert value.field1 == 'val1'
        assert value.field2 == 'val2'



# Generated at 2022-06-14 15:05:28.958975
# Unit test for function validate_yaml
def test_validate_yaml():
    #test data
    valid_yaml = '''
        people:
        - name: John
          age: 30
          gender: male
        - name: Jane
          age: 25
          gender: female
        - name: Bob
          age: 27
          gender: male
        '''

    invalid_yaml = '''
        people:
        - name: John
          age: 30
          gender: male
        - name: Jane
          age: 25
          gender: female
        - name: Bob
          age: "27"
          gender: male
        '''

    class Person(Schema):
        name = fields.String()
        age = fields.Integer()
        gender = fields.String(enum=["male", "female"])


# Generated at 2022-06-14 15:05:33.716919
# Unit test for function validate_yaml
def test_validate_yaml():
    with open("example.yaml") as f:
        token, errors = validate_yaml(f.read(), Schema)
    if errors:
        print(json.dumps(errors, indent=2))
    assert errors == None

# Generated at 2022-06-14 15:05:42.984208
# Unit test for function validate_yaml
def test_validate_yaml():
    d1 = """
    a: 1
    b: 'hello'
    """
    schema = Schema({'a': int, 'b': str})
    assert validate_yaml(d1, schema)[0] == {'a':1, 'b': 'hello'}
    assert validate_yaml(d1, schema)[1] == []

    schema2 = Schema({'a': int, 'b': int})
    assert validate_yaml(d1, schema2)[1] == [
        Message(
            text="'hello' is not a valid integer.",
            code="invalid_type",
            position=Position(
                line_no=3,
                column_no=7,
                char_index=len(d1)-8
            ),
            field="b"
        )
    ]

# Generated at 2022-06-14 15:05:51.039697
# Unit test for function validate_yaml
def test_validate_yaml():
    def test_validation_with_yaml_string(content, validator, errors_code, result=None):
        value, errors = validate_yaml(content, validator)
        error_codes = [err.code for err in errors]
        assert error_codes == errors_code
        assert result == value

    class PersonSchema(Schema):
        name = Field(type="string")
        age = Field(type="integer")

    test_validation_with_yaml_string(
        content=b"name: John\nage: 12",
        validator=PersonSchema,
        errors_code=[]
    )


# Generated at 2022-06-14 15:05:58.329370
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema({"a": int})
    value, errors = validate_yaml("a: foo", schema)
    assert errors == [
        Message(
            template="Invalid type.",
            code="invalid_type",
            path=["a"],
            position=Position(column_no=3, line_no=1, char_index=3),
            value="foo",
        )
    ]
    assert value is None

# Generated at 2022-06-14 15:06:05.074094
# Unit test for function validate_yaml
def test_validate_yaml():
    # test invalid yaml
    content = """
    key:value
    """

    validator = Field(name="key")
    expected_value = ParseError(
        text="found invalid syntax.",
        code="parse_error",
        position=Position(
            line_no=1, column_no=6, char_index=5
        ),
    )
    value, error_messages = validate_yaml(content, validator)
    assert value == expected_value
    assert not error_messages

    # test invalid yaml
    content = """
    key:
      """

    validator = Field(name="key")

# Generated at 2022-06-14 15:06:08.242063
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    bar: baz
    foo: bar
    """
    token = tokenize_yaml(content)
    assert token.value == {"bar": "baz", "foo": "bar"}


# Generated at 2022-06-14 15:06:19.308727
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer

    validator = Integer(minimum=0)

    content = """
    a: true
    b: false
    c: 1
    """

    assert validate_yaml(content, validator) == ({
        'a': True,
        'b': False,
        'c': 1
        },
        []
    )

    content = """
    a: true
    b: false
    c: -1
    """
