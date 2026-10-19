

# Generated at 2022-06-14 14:56:28.395878
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    first_name: John
    last_name: Smith
    email: jsmith@example.com
    age: 22
    """
    from typesystem import Schema, fields

    class UserInfo(Schema):
        first_name = fields.String()
        last_name = fields.String()
        email = fields.Email()
        age = fields.Integer(minimum=18, maximum=65)

    value, errors = validate_yaml(content, UserInfo)
    assert errors[0].text == "Value must be between 18 and 65."

# Generated at 2022-06-14 14:56:33.681388
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('foo: bar') == {'foo': 'bar'}
    assert tokenize_yaml('[1, 2, 3]') == [1, 2, 3]
    assert tokenize_yaml('true') is True
    assert tokenize_yaml('false') is False
    assert tokenize_yaml('null') is None
    assert tokenize_yaml('1') == 1
    assert tokenize_yaml('1.0') == 1.0


# Generated at 2022-06-14 14:56:40.944490
# Unit test for function validate_yaml
def test_validate_yaml():

    import typesystem

    class Person(typesystem.Schema):
        name = typesystem.String()
        age = typesystem.Integer()
        weight = typesystem.Number()

    # Error response
    # Parse Error
    yaml_string = " name: yaml age: 24 weight: 56.55"
    value, error_messages = validate_yaml(yaml_string, Person)
    assert len(error_messages) == 1
    assert error_messages[0] == Message("No content.", code="no_content", line_no=1, column_no=1, char_index=0)

    # Validation Error
    yaml_string = "name: yaml \n weight: 56.55"
    value, error_messages = validate_yaml(yaml_string, Person)

# Generated at 2022-06-14 14:56:51.136361
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None
    class PersonSchema(Schema):
        name = fields.String(required=True)
        age = fields.Integer(required=True)
    # Testing a valid case
    person = """
    name: Mike
    age: 18
    """
    result = validate_yaml(person, PersonSchema)

    assert isinstance(result[0], DictToken)
    assert isinstance(result, tuple)
    assert result[0].value == {"name": "Mike", "age": 18}
    assert result[1] == []
    # Testing an invalid case
    invalid_person = """
    name: Mike
    ag: 18
    """
    result = validate_yaml(invalid_person, PersonSchema)
    assert result[0] is None
    assert result[1] != []
   

# Generated at 2022-06-14 14:56:59.840025
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.tokenize.positional_validation import Invalid

    class Person(Schema):
        name = fields.String(min_length=1)
        age = fields.Integer()
    
        class Meta:
            unknown = EXCLUDE

    content = """{
        name: '김선옥', 
        age: '28',
        height: '5.5'
    }"""

    value, errors = validate_yaml(content, validator=Person)

    assert errors[0].text == "'height' is an unexpected field."



# Generated at 2022-06-14 14:57:04.499187
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    yaml_string = """
    a: '1'
    b:
        c: 2
        d: '3'
    """    
    actual_token = tokenize_yaml(yaml_string)
    expected_token = DictToken({'a': '1','b': {'c': 2,'d': '3'}}, 0, 56, yaml_string)
    assert actual_token == expected_token

# Generated at 2022-06-14 14:57:10.902831
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test validate_yaml
    """
    content = "firstname: John\nlastname: Doe"
    schema = Schema(
        {"firstname": String(), "lastname": String()}, extra_fields="ignore"
    )
    value, error_messages = validate_yaml(content, schema)
    assert not error_messages
    assert value == {"firstname": "John", "lastname": "Doe"}



# Generated at 2022-06-14 14:57:18.648451
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
  test_str1 = '"string1"'
  test_str2 = 'string2'
  test_dict = '{"key1" : "value1", "key2" : "value2"}'
  test_list = '["string1", "string2"]'
  tokens = tokenize_yaml(test_str1)
  print("tokenize_yaml(" + test_str1 + ") -> " + str(type(tokens)))
  tokens = tokenize_yaml(test_str2)
  print("tokenize_yaml(" + test_str2 + ") -> " + str(type(tokens)))
  tokens = tokenize_yaml(test_dict)
  print("tokenize_yaml(" + test_dict + ") -> " + str(type(tokens)))
  tokens = token

# Generated at 2022-06-14 14:57:29.433589
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema({"name": String(max_length=10), "number": Integer()})
    value, error_messages = validate_yaml(
        content=b"name: Peter\nnumber: 12", validator=schema
    )

    assert isinstance(value, dict)
    assert value == {"name": "Peter", "number": 12}
    assert error_messages == []

    value, error_messages = validate_yaml(
        content=b"name: too long\nnumber: 12", validator=schema
    )

    assert value is None
    assert len(error_messages) == 1

    error_message = error_messages[0]
    assert error_message.text == "Invalid value."
    assert error_message.code == "invalid"

# Generated at 2022-06-14 14:57:40.665535
# Unit test for function tokenize_yaml

# Generated at 2022-06-14 14:57:55.213802
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''
        test:
            field1: something
            field2: someother
            field3:
                - another
                - somethingelse
    '''
    class TestValidator(Schema):
        field1 = Field(type="string")

    value, errors = validate_yaml(content, TestValidator)
    assert errors == [
        Message(
            code='field_required',
            context={'field_name': 'field2'},
            position=Position(column_no=9, line_no=2, char_index=19),
        ),
        Message(
            code='field_required',
            context={'field_name': 'field3'},
            position=Position(column_no=4, line_no=4, char_index=39),
        ),
    ]


# Generated at 2022-06-14 14:58:06.986070
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema([
        Field('name', type='string'),
        Field('age', type='integer'),
        Field('married', type='boolean', required=False)
    ])

    assert validate_yaml("name: John Doe\nage: 42\nmarried: False", schema) == \
        ({'name': "John Doe", 'age': 42, 'married': False}, [])

    assert validate_yaml("name: John Doe\nage: 42\nmarried: hello", schema) == \
        ({'name': "John Doe", 'age': 42, 'married': False}, [])

    assert validate_yaml("name: John Doe\nage: 42\nmarried: False\n", schema) == \
        ({'name': "John Doe", 'age': 42, 'married': False}, [])

    assert validate_y

# Generated at 2022-06-14 14:58:17.510175
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String

    class WineForm(Schema):
        name = String(max_length=10)
        year = Integer()

    validator = WineForm()

    content = b'name: "Brunello"\nyear: 2009'
    value, messages = validate_yaml(content, validator)
    assert value == {"name": "Brunello", "year": 2009}, value
    assert messages == []

    content = b"name: This is a long name that goes beyond the allowed length"
    value, messages = validate_yaml(content, validator)
    assert value == {}, value

# Generated at 2022-06-14 14:58:26.444386
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(type="string")
    content = '''\
    foo: bar\
    '''

    result, errors = validate_yaml(content, field)
    assert not errors
    assert result == {"foo": "bar"}

    content = '''\
    .: .\
    '''

    result, errors = validate_yaml(content, field)
    assert errors
    assert result is None

    content = '''\
    foo: bar
    '''

    result, errors = validate_yaml(content, field)
    assert not errors
    assert result == {"foo": "bar"}

    result, errors = validate_yaml(b"", field)
    assert errors
    assert result is None



# Generated at 2022-06-14 14:58:38.218330
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(fields=[
        Field("name", required=False, type="string"),
        Field("age", required=False, type="integer"),
        Field("role", required="string", choices=["admin", "moderator", "user", "guest"]),
        Field("date", required="string", pattern="^[0-9]{4}-([0-9]{2}-){2}[0-9]{2}$")
    ])

    value, error_messages = validate_yaml("""
- name: "george"
  age: 20
  role: "user"
  date: "2019-01-01"
- name: "jack"
  age: 32
  role: "admin"
  date: "2019-09-29"
    """, schema)
    print(value)

# Generated at 2022-06-14 14:58:43.876850
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(type=int)
    content = "foo"

    assert validate_yaml(content, field) == (None, [
        Message(text="Value is not an integer.", code="invalid_type",
        position=Position(line_no=1, column_no=1, char_index=0))
    ])

    content = "123"

    assert validate_yaml(content, field) == (123, [])

    content = "123\n456"

    assert validate_yaml(content, field) == (123, [
        Message(text="Invalid value.", code="invalid",
        position=Position(line_no=2, column_no=1, char_index=4))
    ])


# Generated at 2022-06-14 14:58:50.481283
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String

    content = "123"
    token, errors = validate_yaml(content=content, validator=String())

    assert errors == [
        Message(
            text="Field must be a string.",
            code="invalid_type",
            position=Position(column_no=1, line_no=1, char_index=0),
        )
    ]



# Generated at 2022-06-14 14:58:55.725053
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(
        content="""
        - name: 1
          age: 10
        - name: 2
          age: 20
        """,
        validator=Schema(
            fields={
                "name": Field(type="string"),
                "age": Field(type="number"),
            }
        ),
    )

# Generated at 2022-06-14 14:59:08.072288
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String(max_length=10)
        age = Integer(minimum=10, maximum=50)
        salary = Decimal(minimum=1000)
    #bad format
    yaml_str = "nme: name1\nage: 12\nsalary: 1200\n"
    validator = Person()
    out = validate_yaml(yaml_str, validator)
    assert len(out[1]) == 1, "Unexpected number of errors"
    #key case
    yaml_str = "name: name1\nAge: 12\nsalary: 1200\n"
    validator = Person()
    out = validate_yaml(yaml_str, validator)
    assert len(out[1]) == 1, "Unexpected number of errors"
    #too short name

# Generated at 2022-06-14 14:59:16.938526
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_object = """\
foo:
  baz:
    - 10
    - 20
    - 30
  bar:
    - 10.5
    - 20.5
    - 30.5
  bing: 2003-01-21
  bong:
    - True
    - False
"""
    yaml_schema = Schema(fields={"foo": Field(fields={"bar": Field(type="float")})})
    yaml_object_bytes = bytes(yaml_object, "utf-8")
    yaml_schema_bytes = bytes(yaml_schema, "utf-8")
    object_value, object_errors = validate_yaml(yaml_object, yaml_schema)
    assert object_errors == []
    object_value_bytes, object_errors_bytes = validate

# Generated at 2022-06-14 14:59:33.108863
# Unit test for function validate_yaml
def test_validate_yaml():
    # test_empty_string
    try:
        validate_yaml("", str)
    except ParseError as exc:
        assert str(exc) == "Parse error at line 1, column 1 (char index 0): No content.", "Parse error at line 1, column 1 (char index 0): No content."
    except Exception as exc:
        assert type(exc) == AssertionError, str(exc)

    # test_parse_error_on_invalid_yaml

# Generated at 2022-06-14 14:59:45.827115
# Unit test for function validate_yaml
def test_validate_yaml():

    def test_validator_field() -> typing.Type[Field]:
        class TestField(Field):

            def validate(self, value: typing.Any) -> typing.Any:
                if value == 5:
                    return value
                else:
                    raise ValidationError(value=value, message="Value must be 5.")

        return TestField

    def test_validator_schema() -> typing.Type[Schema]:
        class TestSchema(Schema):
            field = test_validator_field()

        return TestSchema

    def test_validate(content: str, expected_value: typing.Any, expected_errors: list):

        def _test(validator: typing.Union[Field, typing.Type[Schema]]):
            value, error_messages = validate_yaml(content, validator)


# Generated at 2022-06-14 14:59:57.166479
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        first_name = "text"
        last_name = "text"
        friends = ["text"]

    content = """
    first_name: John
    last_name: Doe
    friends:
    - Jane
    - Jim
    """
    try:
        value, errors = validate_yaml(content, TestSchema)
        if errors:
            print("Got errors: {}".format(errors))
        print("Got value: {}".format(value))
    except ParseError as perr:
        print("Parse error: {}".format(perr))
    assert errors is None
    assert value == {"first_name": "John", "last_name": "Doe", "friends": ["Jane", "Jim"]}

# Generated at 2022-06-14 15:00:07.920764
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema(fields=[
        Field(name="id", type="integer", required=True),
        Field(name="title", type="string", required=True),
        Field(name="price", type="float", required=True),
        Field(name="taxable", type="boolean", required=False),
        Field(name="attributes", type="map", required=False)
    ])

    yaml_content = """
    id: 1
    title: "Pants"
    price: 29.95
    taxable: true
    attributes:
        color: "green"
        size: "small"
    """

    value, messages = validate_yaml(
        content=yaml_content, validator=schema
    )
    print(value)
    # {'attributes': {'color': 'green', 'size

# Generated at 2022-06-14 15:00:17.946518
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, fields

    class MySchema(Schema):
        name = fields.String(max_length=100)
        age = fields.Integer(minimum=1, maximum=100)

    content = "name: Sam\nage: 20"
    parsed_content, error_messages = validate_yaml(content=content, validator=MySchema)
    assert parsed_content["name"] == "Sam"
    assert parsed_content["age"] == 20
    assert error_messages == []

    content = "name: Sam\nage: 0"
    parsed_content, error_messages = validate_yaml(content=content, validator=MySchema)
    assert parsed_content is None

# Generated at 2022-06-14 15:00:23.648369
# Unit test for function validate_yaml
def test_validate_yaml():
    # ref: http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-email-support
    class User(Schema):
        email = Email(description="The user's email address")
        password = Password()

    data = """
    email: john.doe@example.com
    password: secret
    """

    # assert isinstance(data, str)

    (value, errors) = validate_yaml(data, User)
    assert value == {'email': 'john.doe@example.com', 'password': 'secret'}
    assert errors == []

# Generated at 2022-06-14 15:00:33.873741
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml(
        """
    first_name: ryan
    last_name: carlson
    addresses:
      - state: Washington
        city: Bellevue
        line_1: 10900 NE 8th St
        line_2: Ste 600
        postal_code: 98004
          """
    )
    assert token.value == {
        "first_name": "ryan",
        "last_name": "carlson",
        "addresses": [
            {"state": "Washington", "city": "Bellevue", "line_1": "10900 NE 8th St", "line_2": "Ste 600",
             "postal_code": "98004"}
        ],
    }
    assert isinstance(token.children[0], ScalarToken)

# Generated at 2022-06-14 15:00:36.183632
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml(b"{}", {}) == (
        {},
        {"errors": [], "warnings": []},
    )

# Generated at 2022-06-14 15:00:47.398146
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        name = Field(type=str)
        age = Field(type=int)

    s = """
    name: John Smith
    age: 22
    """
    value, error_messages = validate_yaml(s, UserSchema)
    assert error_messages == []
    assert value == {"name": "John Smith", "age": 22}

    s = """
    name: John Smith
    """
    value, error_messages = validate_yaml(s, UserSchema)
    assert error_messages == [
        Message(
            text="The field is required.",
            code="required",
            position=Position(line_no=3, column_no=6, char_index=19),
        )
    ]
    assert value == {"name": "John Smith"}



# Generated at 2022-06-14 15:00:59.303886
# Unit test for function validate_yaml
def test_validate_yaml():
    import yaml
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer
    from typesystem import errors
    from typesystem.tokenize.positional_validation import get_validator

    class MySchema(Schema):
        foo = String()
        bar = Integer()

    def yaml_parse_error(text, error_code, line_no, column_no):
        return errors.ParseError(
            text=text,
            code=error_code,
            position=errors.Position(
                line_no=line_no, column_no=column_no, char_index=0
            ),
        )

    validator = get_validator(MySchema)  # type: ignore


# Generated at 2022-06-14 15:01:14.682677
# Unit test for function validate_yaml
def test_validate_yaml():
    """ validate_yaml
    """
    import typesystem
    from typesystem import fields, schemas
    from typesystem.tokenize.tokens import Token

    def pytest_yaml(content: str, validator: typing.Union[Field, Schem]) -> Token:
        return validate_yaml(content, validator)

    class YamlSchema(schemas.Schema):

        name = fields.String(format="slug", max_length=10)
        location = fields.String(max_length=10)

    with pytest.raises(AssertionError) as exc_info:
        _ = validate_yaml({}, YamlSchema)

    assert exc_info.match("'pyyaml' must be installed.")


# Generated at 2022-06-14 15:01:23.144758
# Unit test for function validate_yaml
def test_validate_yaml():
    from .utils import FieldTestMixin, SchemaTestMixin
    from .yaml_validation import FieldTestSchema, SchemaTestSchema
    from .field_tests import test_base_field
    from .schema_tests import test_base_schema

    test_base_field(test_class=FieldTestMixin, constructor=FieldTestSchema())
    test_base_schema(test_class=SchemaTestMixin, constructor=SchemaTestSchema())

    assert (
        validate_yaml("test:", FieldTestSchema.fields["test"])[1]
        == [Message("Missing required field 'test'.", "missing", "test", 1, 6)]
    )

# Generated at 2022-06-14 15:01:34.284390
# Unit test for function validate_yaml
def test_validate_yaml():
    class TestSchema(Schema):
        name = fields.String()
        age = fields.Integer()

    class TestSchema2(Schema):
        is_foo = fields.Boolean()
        is_bar = fields.Boolean()

    # Validation fails
    message = "name is required"
    value, error_messages = validate_yaml("age: 24", TestSchema)
    assert len(error_messages) == 1
    assert error_messages[0].text == message

    # Validation passes
    message = "name is required"
    value, error_messages = validate_yaml("age: 24", TestSchema)
    assert len(error_messages) == 1
    assert error_messages[0].text == message

    # Validation passes
    value, error_messages = validate_

# Generated at 2022-06-14 15:01:44.643800
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Integer, Field, Schema

    class PostSchema(Schema):
        id = Integer()
        title = String(max_length=50)

    result, errors = validate_yaml(
        content="""id: 123
title: "Typesystem JSON Schema"
""",
        validator=Field(
            keys={"id": Integer(), "title": String(max_length=50)}
        ),
    )
    assert errors == []
    assert result["id"] == 123
    assert result["title"] == "Typesystem JSON Schema"

    result, errors = validate_yaml(
        content="""id: 123
title: "Typesystem JSON Schema"
""",
        validator=PostSchema,
    )
    assert errors == []
    assert result["id"] == 123
    assert result

# Generated at 2022-06-14 15:01:47.497011
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("{a: 1, b: 2}") == {'a': 1, 'b': 2}



# Generated at 2022-06-14 15:01:57.207392
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "# valid list\n- 2\n- 2"
    validator = Field(type="integer", min_length=1)

    #assert validate_yaml(content=content, validator=validator) == [2, 2]
    assert validate_yaml(content=content, validator=validator)[0] == [2, 2]
    assert validate_yaml(content=content, validator=validator)[1] == []

    # invalid list
    content = "# invalid list\n- 2\n- 2.2\n- 3"
    validator = Field(type="integer", min_length=1)

    #assert validate_yaml(content=content, validator=validator)[0] == [2, 3]

# Generated at 2022-06-14 15:02:03.721906
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''
    hello: world
    foo:
      - bar
      - baz
    '''
    value, errors = validate_yaml(
        content,
        {
            "hello": "string",
            "foo": ["string"],
        }
    )
    assert value == {'hello': 'world', 'foo': ['bar', 'baz']}
    assert errors == []

    content = '''
    foo:
      - bar
      - baz
    '''
    value, errors = validate_yaml(
        content,
        {
            "hello": "string",
            "foo": ["string"],
        }
    )
    assert value == {'hello': None, 'foo': ['bar', 'baz']}

# Generated at 2022-06-14 15:02:11.725727
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(tokenize_yaml("a"), ScalarToken)
    assert isinstance(tokenize_yaml("1"), ScalarToken)
    assert isinstance(tokenize_yaml("{}"), DictToken)
    assert isinstance(tokenize_yaml("[]"), ListToken)
    assert isinstance(tokenize_yaml("null"), ScalarToken)
    assert isinstance(tokenize_yaml("true"), ScalarToken)
    assert isinstance(tokenize_yaml("false"), ScalarToken)
    assert tokenize_yaml("a").value == "a"
    assert tokenize_yaml("1").value == 1
    assert tokenize_yaml("null").value == None
    assert tokenize_yaml("true").value == True
    assert tokenize_yaml("false").value == False
    

# Generated at 2022-06-14 15:02:22.325822
# Unit test for function validate_yaml
def test_validate_yaml():
    fields = [
        {"name": "first_name", "type": "string"},
        {"name": "last_name", "type": "string"},
        {"name": "pets", "type": "array", "items": {"type": "string"}},
    ]
    validator = {"type": "object", "properties": {f["name"]: f for f in fields}}
    content = "first_name: Matty\nlast_name: C\npets: [cat, dog]"
    value, errors = validate_yaml(content, validator)
    assert not errors
    assert value == {
        "first_name": "Matty",
        "last_name": "C",
        "pets": ["cat", "dog"],
    }


# Generated at 2022-06-14 15:02:30.999113
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(dtype=int)
    content = '''
        ---
        - 20
        - "40"
    '''
    data, errors = validate_yaml(content, validator)
    assert len(errors) == 1
    e = errors[0]
    assert e.type == "parse_error"
    assert e.text == "could not determine a constructor for the tag 'tag:yaml.org,2002:str'"
    assert e.position.line_no == 2
    assert e.position.column_no == 1
    assert e.position.char_index == 14

# Generated at 2022-06-14 15:02:46.118703
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Boolean, Float, Integer, String

    class PersonSchema(Schema):
        name = String()
        age = Integer()
        weight = Float()
        over_21 = Boolean(required=False)

    content = """
    name: Bob
    age: 30
    weight: 75.2
    over_21: True
    """

    value, messages = validate_yaml(content, PersonSchema)
    assert value == {
        "name": "Bob",
        "age": 30,
        "weight": 75.2,
        "over_21": True,
    }
    assert messages == []

    # Change the value of over_21 to a string.

# Generated at 2022-06-14 15:02:56.875368
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Validate YAML content.
    """
    from typesystem import Integer, String

    class Person(Schema):
        age = Integer(minimum=0)
        name = String()

    content = "age: x\nname: Alice"
    value, error_messages = validate_yaml(content, validator=Person)
    assert not value
    assert len(error_messages) == 1
    assert error_messages[0].position.column_no == 7
    assert error_messages[0].position.line_no == 1
    assert error_messages[0].position.char_index == 6
    assert error_messages[0].text == "Value is not an integer."
    assert error_messages[0].code == "type_error.integer"


# Generated at 2022-06-14 15:02:59.245150
# Unit test for function validate_yaml
def test_validate_yaml():
  with open('../data/data.yml', 'r') as stream:
    docs = yaml.load_all(stream)
    for doc in docs:
        print(doc)

# Generated at 2022-06-14 15:03:09.421952
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Test tokenize_yaml function.
    """
    assert tokenize_yaml('') == None
    assert tokenize_yaml('123') == ScalarToken(123, 0, 2)
    assert tokenize_yaml('.123') == ScalarToken(0.123, 0, 4)
    assert tokenize_yaml('123.123') == ScalarToken(123.123, 0, 6)
    assert tokenize_yaml('-123.123') == ScalarToken(-123.123, 0, 7)
    assert tokenize_yaml('-123') == ScalarToken(-123, 0, 3)
    assert tokenize_yaml('true') == ScalarToken(True, 0, 3)
    assert tokenize_yaml('false') == ScalarToken(False, 0, 4)
    assert token

# Generated at 2022-06-14 15:03:14.613407
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(required=True, type="integer")
    value, errors = validate_yaml("123", field)
    assert value == 123
    assert not errors

    value, errors = validate_yaml("123.4", field)
    assert not value
    assert len(errors) == 1



# Generated at 2022-06-14 15:03:25.524585
# Unit test for function validate_yaml
def test_validate_yaml():
    string_content = """\
    metrics:
      - domain: api
        key: request_count
        value: 5
        unit: "count"
      - domain: api
        key: request_size
        value: 3.2
        unit: "kb"
    """

    bytes_content = string_content.encode("utf-8")

    schema = Schema(fields={"metrics": List(items=Metric)})

    value, errors = validate_yaml(string_content, schema)
    assert value == {
        "metrics": [
            {"domain": "api", "key": "request_count", "value": 5, "unit": "count"},
            {"domain": "api", "key": "request_size", "value": 3.2, "unit": "kb"},
        ]
    }

# Generated at 2022-06-14 15:03:35.882882
# Unit test for function validate_yaml
def test_validate_yaml():
    # Test when value is valid
    scheme_test_valid = Schema(fields={'test':Field(type="integer")})
    token_test_valid = tokenize_yaml(b'{test:123')
    value_test_valid, error_test_valid = validate_with_positions(token = token_test_valid, validator = scheme_test_valid)
    print(f'test_value = {value_test_valid}')
    print(f'error_test_valid = {error_test_valid}')
    assert value_test_valid == {'test':123}
    assert error_test_valid == []

    # Test when value is not valid
    scheme_test_not_valid = Schema(fields={'test':Field(type="integer")})
    token_test_not_valid = tokenize_

# Generated at 2022-06-14 15:03:46.204362
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema([
        Field(name="a", type="integer", required=True),
        Field(name="b", type="string")
    ])

    try:
        out, error_messages = validate_yaml(b"a: 123", schema)
    except Exception as e:
        print(str(e))
    assert out == {"a": 123}
    assert error_messages == []

    try:
        out, error_messages = validate_yaml(b"a: true", schema)
    except Exception as e:
        print(str(e))
    assert out == {"a": True}
    assert error_messages == []

    try:
        out, error_messages = validate_yaml(b"a: foo", schema)
    except Exception as e:
        print(str(e))


# Generated at 2022-06-14 15:03:55.278493
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.json_schema import JSONSchema

    # When YAML is valid.
    validator = JSONSchema.load({
            "properties": {
                "name": {"type": "string"},
                "age": {"type": "integer"},
            },
            "required": ["name"],
        })

    value, error_messages = validate_yaml(content="name: Bob", validator=validator)
    assert value == {"name": "Bob"}  # type: ignore
    assert not error_messages

    # When YAML is not valid
    value, error_messages = validate_yaml(content="age: Bob", validator=validator)
    assert value is None
    assert error_messages[0].text == '"Bob" is not a valid integer.'

# Generated at 2022-06-14 15:04:01.130698
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema({"name": String()})
    validator = Validator(schema)
    value, error_messages = validate_yaml(content="name: foo", validator=validator)
    assert value == {"name": "foo"}
    assert error_messages == []

    value, error_messages = validate_yaml(
        content="name: \n", validator=validator
    )
    assert error_messages[0].message == "This field is required."
    assert len(error_messages) == 1

# Generated at 2022-06-14 15:04:13.127952
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String

    validator = String()
    value = validate_yaml(b"foo", validator)
    assert value == "foo"



# Generated at 2022-06-14 15:04:23.806742
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Schema, Integer

    schema = Schema({"foo": Integer()})
    result, error_messages = validate_yaml(b"foo:\n42\n", schema)
    assert result == {"foo": 42}
    assert not error_messages
    result, error_messages = validate_yaml(b"foo:\n42.0\n", schema)
    assert result == {"foo": None}
    assert error_messages == [
        ValidationError(
            text="Must be an integer.",
            code="must_be_integer",
            position=Position(line_no=2, column_no=1, char_index=5),
        )
    ]
    result, error_messages = validate_yaml(b"foo:\nabc\n", schema)

# Generated at 2022-06-14 15:04:28.501761
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_file = open('test.yaml', 'r')
    content = yaml_file.read()
    yaml_file.close()
    type_schema = ({"a": {"type": int}, "b": {"type": str}})  # type: ignore
    assert validate_yaml(content, type_schema) == {'a': 1, 'b': 'Hello'}

# YAML parser test

# Generated at 2022-06-14 15:04:39.838004
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """a: 1
b:
    - 2
    - 3
    """
    validator_schema = {'a': 'integer', 'b': ['integer']}
    schema = Schema(validator_schema)
    validator = schema
    value, error_messages = validate_yaml(content, validator)
    assert value == {'a': 1, 'b': [2, 3]}
    assert error_messages == []

    content = """
b: [1, true, null]
"""
    validator_schema = {'a': 'boolean', 'b': ['boolean']}
    schema = Schema(validator_schema)
    validator = schema
    value, error_messages = validate_yaml(content, validator)

# Generated at 2022-06-14 15:04:48.495716
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem as ts

    class PassageSchema(ts.Schema):
        number = ts.Integer(required=True)
        text = ts.String(required=True)

    class BookSchema(ts.Schema):
        name = ts.String(required=True)
        passages = ts.Array(element=PassageSchema, max_items=1, required=True)

    input = """
    name: The Brothers Karamazov
    passages:
    - number: 1
      text: The story begins with a legal dispute over a patrimony."""

    book, messages = validate_yaml(input, validator=BookSchema)
    assert not messages, messages
    assert book.name == "The Brothers Karamazov"
    assert book.passages[0].number == 1

# Generated at 2022-06-14 15:04:58.265010
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from tests.utils import validate_with_messages

    class PetSchema(Schema):
        name = String(min_length=3)

    # This is invalid because the `name` field should be at least three
    # characters long.
    content = """
    name: Fluffy
    species: Dog
    """

    value = validate_with_messages(
        content=content,
        validator=PetSchema,
        validate_function=validate_yaml,
    )

    # Validation should have failed.
    assert value is False


# Generated at 2022-06-14 15:05:07.721882
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Boolean, String
    from typesystem.base import ValidationError
    from typesystem.schemas import Schema

    class MySchema(Schema):
        name = String()
        active = Boolean()

    yaml_good = """name: Tyler
active: true
"""
    value, errors = validate_yaml(yaml_good, MySchema)
    assert errors == []
    assert value == {"name": "Tyler", "active": True}

    yaml_bad = """name: Tyler
active: 1
"""
    value, errors = validate_yaml(yaml_bad, MySchema)
    assert len(errors) == 1
    assert isinstance(errors[0], ValidationError)
    assert errors[0].field_name == "active"

# Generated at 2022-06-14 15:05:15.881122
# Unit test for function validate_yaml
def test_validate_yaml():
    # basic valid
    input_data = "1"
    validator = Field(type="integer")
    assert validate_yaml(input_data, validator) == (1, None)

    # basic invalid
    input_data = "x"
    validator = Field(type="integer")
    assert validate_yaml(input_data, validator) == (
        None,
        [
            Message(code="invalid", text="Value is not a valid integer.", position=None),
            Message(
                code="invalid",
                text="Value is not of type 'integer'.",
                position=_get_position(content=input_data, index=0),
            ),
        ],
    )

    # valid with validator as type
    input_data = "1"

# Generated at 2022-06-14 15:05:25.977155
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String
    from typesystem.schemas import Schema

    class Person(Schema):
        first_name = String()
        last_name = String()
        age = Integer(allow_null=True)

    validator = Person()

    yaml_string_1 = """
    first_name: yu
    last_name: yu
    age: 1
    """
    yaml_string_2 = """
    first_name: yu
    last_name: yu
    age: "not an age"
    """
    yaml_string_3 = """
    first_name: yu
    last_name: yu
    age: null
    """

# Generated at 2022-06-14 15:05:34.433749
# Unit test for function validate_yaml
def test_validate_yaml():
    errors = validate_yaml(
        b"data: 1",
        schema.Structure(fields={"data": schema.String()}),
    )
    assert len(errors) == 1
    assert errors[0].code == "invalid_type"
    assert errors[0].message == "Field value must be of type 'string'."
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no == 7
    assert errors[0].position.char_index == 6

# Generated at 2022-06-14 15:05:46.966906
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    class TestSchema(Schema):
        foo = Field(type="string")
        bar = Field(type="string")

    data = """
    foo: foo
    bar: bar
    """

    errors = validate_yaml(data, TestSchema)
    assert not errors

# Generated at 2022-06-14 15:05:59.080700
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    from typesystem.fields import Boolean, Integer, String
    from typesystem.schemas import Schema

    from .utils import assert_validation_message

    class MySchema(Schema):
        name = String(required=True)
        age = Integer(minimum=0)
        enabled = Boolean(default=False)

    value, errors = validate_yaml(
        """
        name: Test Schema
        age: 42
        enabled: true
        """,
        validator=MySchema,
    )

    assert value == {"name": "Test Schema", "age": 42, "enabled": True}
    assert errors == []


# Generated at 2022-06-14 15:06:07.163526
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema({"a": int})
    try:
        value, messages = validate_yaml(content='["1"]', validator=schema)
    except ParseError as e:
        assert "list" in e.text
        assert "mapping" in e.text
        position = Position(line_no=1, column_no=1, char_index=0)
        assert e.position == position
    else:
        assert False, "Should raise ParseError."

    try:
        value, messages = validate_yaml(content='{a: 1}', validator=schema)
    except ValidationError as e:
        assert "expected type int" in e.text
        position = Position(line_no=1, column_no=4, char_index=3)
        assert e.position == position


# Generated at 2022-06-14 15:06:17.661438
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_content = """
    - foo: bar
      baz: qux
    """

    schema = Schema(fields={"foo": {"type": "string"}})  # type: ignore
    validator = schema.as_field()  # type: ignore
    _, error_messages = validate_yaml(yaml_content, validator)
    assert error_messages[0] == "baz: qux (at line: 2, column: 9)"

    yaml_content = """
    - wrong: "oops"
    """

    _, error_messages = validate_yaml(yaml_content, validator)
    assert error_messages[0] == "wrong: 'oops' (at line: 2, column: 9)"

