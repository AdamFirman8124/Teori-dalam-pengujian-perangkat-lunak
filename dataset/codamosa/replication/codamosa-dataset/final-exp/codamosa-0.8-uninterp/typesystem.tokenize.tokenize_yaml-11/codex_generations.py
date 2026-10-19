

# Generated at 2022-06-14 14:56:31.988489
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('') == [], "empty string returns empty list"
    assert tokenize_yaml('\n') == [], "newline character returns empty list"
    assert tokenize_yaml('\r') == [], "carriage return character returns empty list"
    assert tokenize_yaml('\n\r') == [], "carriage return followed by newline character returns empty list"
    assert tokenize_yaml(' ') == [], "space character returns empty list"
    assert tokenize_yaml('123') == ScalarToken(123, 0, 2, content='123'), "string with numbers returns token object"
    assert tokenize_yaml('bob') == ScalarToken('bob', 0, 2, content='bob'), "string with letters returns token object"

# Generated at 2022-06-14 14:56:33.332275
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
   assert tokenize_yaml("bla") == "bla"


# Generated at 2022-06-14 14:56:44.752929
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Test validate_yaml() function
    """
    # test case with valid YAML syntax
    yaml_string = """
    - valid
    - python
    - code
    """
    token = tokenize_yaml(yaml_string)
    assert isinstance(token, DictToken)
    assert token.children == [DictToken([], 0, -1, content=yaml_string)]

    # test case with value error
    yaml_string = """
    - valid
    - python
    - code
    """
    token = tokenize_yaml(yaml_string)
    assert isinstance(token, DictToken)
    assert token.children == [DictToken([], 0, -1, content=yaml_string)]

# Generated at 2022-06-14 14:56:48.479147
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("{}")
    assert tokenize_yaml("[]")
    assert tokenize_yaml("""
    a: 1
    b:
      - 1
      - 2
      - 3
    c: true
    d: null
    """)



# Generated at 2022-06-14 14:56:55.695353
# Unit test for function validate_yaml
def test_validate_yaml():
    class test_schema(Schema):
        name = fields.String(required=True)
        age = fields.Integer(required=True)
    yaml_str = "name: Mark\nage: 18"
    result = validate_yaml(yaml_str, validator=test_schema)
    assert result[1] == []
    yaml_str = "age: 18"
    result = validate_yaml(yaml_str, validator=test_schema)
    assert result[0] == None
    assert len(result[1]) == 1


# Generated at 2022-06-14 14:57:00.670938
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "aaa: 1"
    validator = Field(name="aaa", type_="string")
    value, error_messages = validate_yaml(content, validator)
    assert value == None
    assert error_messages[0].text == "Must be of type 'string'."

# Generated at 2022-06-14 14:57:06.013141
# Unit test for function validate_yaml
def test_validate_yaml():
    # define schema
    class MySchema(Schema):
        name = String()
        age = Integer()

    # define sample content
    content = """
    name: Anurag
    age: 21
    """

    # validate the content in the context of a schema
    value, errors = validate_yaml(content=content, validator=MySchema)
    expected_value = {"name": "Anurag", "age": 21}
    assert errors == []
    assert value == expected_value


# Generated at 2022-06-14 14:57:17.057294
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String, Number, Object, Array

    class TestSchema(Schema):
        name = String()
        age = Number()
        address = Object(fields={"city": String(), "postcode": String()})
        emails = Array(items=String())

    content = """
        name: "John"
        age: 32
        address:
          city: "London"
        emails: [one@example.com, two@example.com]
    """

    value, errors = validate_yaml(content, validator=TestSchema)

    assert value == dict(
        name="John",
        age=32,
        address=dict(city="London"),
        emails=["one@example.com", "two@example.com"],
    )


# Generated at 2022-06-14 14:57:21.958835
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
        name: Joe Blogs
        address:
            street: 123 Normal Street
            suburb: Normalville
        hobbies:
            - programming
            - blogging
            - sleep
        active: true
        """
    value, errors = validate_yaml(content, User.as_field())
    print(value)
    print(errors)


# Generated at 2022-06-14 14:57:25.921322
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """Check if the dictionary is parsed correctly"""

    # Test case 1
    result = tokenize_yaml("")
    assert result == '\nNo content'

    # Test case 2
    result = tokenize_yaml({'Hello': 1, 'World': 'Test'})
    assert result == {'Hello': 1, 'World': 'Test'}



# Generated at 2022-06-14 14:57:40.482750
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = 'string'
        age = {'type': 'integer', 'minimum': 0}
        married = 'boolean'

    content = '''
        name: Ryan
        age: "31"
        married: yes
    '''

    expected_value = {'name': 'Ryan', 'age': 31, 'married': True}

    try:
        value = validate_yaml(content, PersonSchema)
    except ValidationError as e:
        pytest.fail('Value did not validate when it should have: {}'.format(str(e)))
    assert value[0] == expected_value

    content = '''
        name: Ryan
        age: -27
        married: yes
    '''


# Generated at 2022-06-14 14:57:46.164980
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    str_content = "test: 123"
    result = tokenize_yaml(str_content)
    assert isinstance(result, DictToken)
    assert result.value == {"test": 123}
    assert result.start == 0
    assert result.end == len(str_content)
    assert result.char_index_pair == (0, len(str_content))



# Generated at 2022-06-14 14:57:56.001942
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None
    content = """
    name: Alice
    skills:
    - Rust
    - Python
    - Clojure
    friends:
    - name: Bob
      skills:
      - Python
      - Java
      - Clojure
      friends:
      - name: Carol
        skills:
        - Python
        - Clojure
        friends:
        - Bob
        - Alice
    - name: Dave
      skills:
      - Clojure
      friends:
      - Bob
      - Alice
    """


# Generated at 2022-06-14 14:58:07.716262
# Unit test for function validate_yaml
def test_validate_yaml():
    class CarSchema(Schema):
        name = Text(required=True)
        year = Integer(min_value=1900, max_value=datetime.datetime.now().year)

    assert validate_yaml("name: Bugatti Veyron", CarSchema) == (
        {"name": "Bugatti Veyron"},
        {},
    )

    class CarSchema(Schema):
        name = Text(required=True)
        year = Integer(min_value=1900, max_value=datetime.datetime.now().year)

    content = """
      name: Bugatti Veyron
      year: 2010
    """
    assert validate_yaml(content, CarSchema) == (
        {"name": "Bugatti Veyron", "year": 2010},
        {},
    )


# Generated at 2022-06-14 14:58:18.395206
# Unit test for function validate_yaml
def test_validate_yaml():
    from pytest import raises

    from typesystem import Schema, Text, Integer

    class MySchema(Schema):
        name = Text()
        age = Integer(minimum=1)

    # Test good case
    person = MySchema.validate_yaml(b"name: Alice\nage: 42")
    assert person.value == {"name": "Alice", "age": 42}
    assert person.errors == []

    # Test bad case
    person = MySchema.validate_yaml(b"name: Alice\nage: -1")
    assert person.value == {"name": "Alice", "age": -1}
    assert len(person.errors) == 1
    assert person.errors[0].code == "minimum"
    assert person.errors[0].path == ("age",)

# Generated at 2022-06-14 14:58:22.852502
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""
    foo:
        - baz
        - bar
    """)
    assert isinstance(token, DictToken)
    assert token.mapping == {"foo": [ScalarToken("baz"), ScalarToken("bar")]}


# Generated at 2022-06-14 14:58:24.482799
# Unit test for function validate_yaml
def test_validate_yaml():
    tokenize_yaml("key: value")

# Generated at 2022-06-14 14:58:31.228763
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(type="string", pattern="^[0-9]{3}-[0-9]{2}-[0-9]{4}$")
    value, errors = validate_yaml(
            content="""
            social: 555-12-1234
            dob: 19961120""",
            validator=field,
        )
    assert value == "19961120"
    assert len(errors) == 1
    assert errors[0].text == "String does not match pattern '^[0-9]{3}-[0-9]{2}-[0-9]{4}$'"

# Generated at 2022-06-14 14:58:39.148916
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("test: test")
    assert token.text == "test: test"
    assert token.start == 0
    assert token.end == 9
    assert token.type == "MappingNode"

    assert token.mapping_token['test'].type == "ScalarNode"
    assert token.mapping_token['test'].text == "test"
    assert token.mapping_token['test'].start == 5
    assert token.mapping_token['test'].end == 8



# Generated at 2022-06-14 14:58:46.304515
# Unit test for function validate_yaml
def test_validate_yaml():
    schema_class = schema({"age": Field(int)})
    assert validate_yaml("", schema_class) == (
        {"age": None},
        [Message(text="Missing value.", code="required", position=Position(1, 1, 0))],
    )
    assert validate_yaml("age: 1", schema_class) == ({"age": 1}, [])
    assert validate_yaml("age: '1'", schema_class) == (
        {"age": "1"},
        [
            Message(
                text="Value is not an int.",
                code="invalid_type",
                position=Position(1, 6, 5),
            )
        ],
    )

# Generated at 2022-06-14 14:58:53.779896
# Unit test for function validate_yaml
def test_validate_yaml():
    # Validate with the given YAML schema
    content = (
        "name: John Doe\n"
        "age: 43\n"
        "spouse: \n"
        "  name: Jane Doe\n"
    )

    class Person(Schema):
        name = String(max_length=30)
        age = Integer(minimum=1)

    class Family(Schema):
        person = Person()
        spouse = Person()

    value, errors = validate_yaml(content, Family)
    assert errors == []
    assert value == {
        "person": {"name": "John Doe", "age": 43},
        "spouse": {"name": "Jane Doe", "age": None},
    }

# Generated at 2022-06-14 14:58:58.418146
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("a: b")
    assert isinstance(token, DictToken)
    assert token.value == {"a": "b"}
    assert token.content == "a: b"
    assert token.start_index == 0
    assert token.end_index == 3


# Generated at 2022-06-14 14:59:10.824411
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Test tokenize_yaml function
    """
    try:
        assert yaml is not None, "'pyyaml' must be installed."
    except AssertionError:
        return
    with pytest.raises(ParseError):
        tokenize_yaml("")
    test_token = tokenize_yaml('{key0:value0, key1:[value1,value2], key2:value3}')
    assert isinstance(test_token, DictToken) == True
    test_token = tokenize_yaml('[value1,value2]')
    assert isinstance(test_token, ListToken) == True
    test_token = tokenize_yaml('value1')
    assert isinstance(test_token, ScalarToken) == True

# Generated at 2022-06-14 14:59:16.345970
# Unit test for function validate_yaml
def test_validate_yaml():
    assert(validate_yaml.__name__ == "validate_yaml")
    assert(validate_yaml(content=b"a: 1\nb: 2\n", validator=Schema([
        Field(name="a", required=True, type=int),
        Field(name="b", required=True, type=int)
    ])) == ([(True, None), (True, None)], []))

# Generated at 2022-06-14 14:59:24.920220
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    from collections import OrderedDict
    from typesystem.tokenize.tokens import DictToken, ScalarToken

    token = tokenize_yaml(b"a: b\nc: d\n")
    assert isinstance(token, DictToken)
    assert token.value == {"a": "b", "c": "d"}
    assert token.start == 0
    assert token.end == 9

    token = tokenize_yaml('a: b\nc: d\n')
    assert isinstance(token, DictToken)
    assert token.value == OrderedDict([('a', 'b'), ('c', 'd')])
    assert token.start == 0
    assert token.end == 9

    token = tokenize_yaml('{"a": "b", "c": "d"}')

# Generated at 2022-06-14 14:59:30.040900
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    yaml_str = """
    content: 
        data: hello
        data2: 45
    content2:
        - hello
        - 45
    """
    content = tokenize_yaml(yaml_str)
    assert content == {"content": {"data": "hello", "data2": 45}, "content2": ["hello", 45]}

# Generated at 2022-06-14 14:59:36.877087
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("") == None
    assert tokenize_yaml("""
        - [1, 2, 3, 4]
        - [1, 2, 3, 4]
        - [1, 2, 3, 4]
    """) == [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ]
    assert tokenize_yaml("""
        a: 1
        b: 2
        c: 3
        d: 4
        e: 5
    """) == {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5
    }

# Generated at 2022-06-14 14:59:48.152258
# Unit test for function validate_yaml
def test_validate_yaml():
    schema=Schema([
        Field('name', field_type=str),
        Field('email', field_type=str),
    ])
    data='''
    name: Test User
    email: test@example.com
    '''
    value, error_message=validate_yaml(data,schema)
    assert error_message==[]
    assert value=={'name': 'Test User', 'email': 'test@example.com'}
    data='''
    name: Test User
    email: test@example
    fig2: 3
    '''
    value, error_message=validate_yaml(data,schema)

# Generated at 2022-06-14 15:00:00.207847
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test expected behavior
    # Test scalars
    token_int = tokenize_yaml('1')
    token_float = tokenize_yaml('1.4')
    token_bool = tokenize_yaml('true')
    token_string = tokenize_yaml('"string"')
    token_null = tokenize_yaml('null')

    assert token_int.value == 1
    assert token_float.value == 1.4
    assert token_bool.value is True
    assert token_string.value == "string"
    assert token_null.value is None

    # Test lists
    token_list = tokenize_yaml('[1, "str", false, null, [1, 2, 3]]')
    assert len(token_list.value) == 5

    assert token_list.value[0].value

# Generated at 2022-06-14 15:00:12.110616
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = fields.String()
        age = fields.Integer()

    # Invalid content
    content = """
    name: 'Jim'
    age: five
    """
    value, messages = validate_yaml(content, PersonSchema)
    assert value is None
    assert len(messages) == 1
    message = messages[0]
    assert message.kind == "error"
    assert message.text.startswith("Must be a valid integer.")
    assert message.position.line_no == 3
    assert message.position.column_no == 4
    assert message.position.char_index == 11

    # Valid content
    content = """
    name: 'Jim'
    age: 31
    """
    value, messages = validate_yaml(content, PersonSchema)

# Generated at 2022-06-14 15:00:23.431331
# Unit test for function validate_yaml
def test_validate_yaml():
    # bytestring
    assert validate_yaml(b"{}", Schema)
    assert not validate_yaml(b"{}", "foo")

    # string
    assert validate_yaml("{}", Schema)
    assert not validate_yaml("{}", "foo")

    # error
    with pytest.raises(ParseError):
        validate_yaml("{", Schema)

    # validation
    with pytest.raises(ValidationError) as excinfo:
        validate_yaml("{}", Field(required=True))
    assert "This field is required." in str(excinfo.value)



# Generated at 2022-06-14 15:00:25.403783
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert (
        tokenize_yaml("name: string\n") == DictToken({"name": "string"}, 0, 13)
    )


# Generated at 2022-06-14 15:00:37.740413
# Unit test for function validate_yaml
def test_validate_yaml():
    # test success case
    # string
    input_str = '''
    number: 123
    string: "a string"
    '''
    class ExampleSchema(Schema):
        number = Field(type="integer")
        string = Field(type="string")

    value, messages = validate_yaml(input_str, ExampleSchema)
    assert value == {"number": 123, "string": "a string"}
    assert messages == []

    # bytes
    input_bytes = b'''
    number: 123
    string: "a string"
    '''
    class ExampleSchema(Schema):
        number = Field(type="integer")
        string = Field(type="string")

    value, messages = validate_yaml(input_bytes, ExampleSchema)

# Generated at 2022-06-14 15:00:43.735657
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.types import Integer, String
    class Person(Schema):
        name = String()
        age = Integer()
    class Group(Schema):
        name = String()
        members = Person[:]

    def assert_ok(content:str, schema:Schema):
        value, errors = validate_yaml(content, schema)
        assert value is not None
        assert not errors
    def assert_errors(content:str, schema:Schema, errors:int):
        value, errors = validate_yaml(content, schema)
        assert value is None
        assert errors
        assert len(errors) == errors
    assert_ok("""
        name: "Tom"
        age: 42
    """, Person)
    assert_ok("""
        name: "Group"
        members: []
    """, Group)


# Generated at 2022-06-14 15:00:49.883267
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None
    from typesystem.fields import Integer, String

    class Person(Schema):
        name = String()
        age = Integer()

    validator = Person()

    yaml_str = textwrap.dedent(
        """\
    name: Bob
    age: 12
    """
    )

    value, messages = validate_yaml(yaml_str, validator)
    assert value == {"name": "Bob", "age": 12}
    assert not messages



# Generated at 2022-06-14 15:01:02.232238
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import Integer, Text

    class Item(Schema):
        id = Text(max_length=50)
        price = Integer(minimum=5, maximum=100)

    class Cart(Schema):
        items = Item.array()

    validator = Cart()

    # Simulate various YAML input strings.
    content = """
    items:
    - id: foo
      price: 3
    - id: foo
      price: 101
    - id: bar
      price: 10
    """
    value, errors = validate_yaml(content, validator=validator)

# Generated at 2022-06-14 15:01:11.919558
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.base import Number
    from typesystem.base import String
    from typesystem.fields import Schema

    class Person(Schema):
        name = String()
        age = Number()

    # Expects that valid content validates and the error messages is empty
    validated_content, error_messages = validate_yaml(
        'name: John\nage: 30',
        Person,
    )
    assert validated_content['name'] == 'John'
    assert validated_content['age'] == 30
    assert error_messages == []

    # Expects that invalid content raises errors
    validated_content, error_messages = validate_yaml(
        'name: John\nage: notanumber',
        Person,
    )
    assert error_messages[0]['code'] == 'invalid_type'


# Generated at 2022-06-14 15:01:17.701248
# Unit test for function validate_yaml
def test_validate_yaml():
  content = '''
        name: Mike
        age: 20
        pet:
          name: Sparky
          age: 1
        pets:
          - name: kitty
            age: 3
          - name: doggy
            age: 5
        '''
  validator = Schema([
      Field(name="username", validators=[validators.String()])
  ])
  assert validate_yaml(content, validator) == ({"username":"Mike"}, [])
  validator = Schema([
      Field(name="username", validators=[validators.String()])
  ])
  assert validate_yaml(content,validator) != ({"username":"Mike"}, [])

# Generated at 2022-06-14 15:01:21.547914
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.tests.schema_test import PersonSchema
    from typesystem.tests.messages import PersonMessage

    assert validate_yaml("123", PersonMessage) == (
        123,
        [],
    )
    assert validate_yaml("123", PersonSchema.name) == (
        123,
        [],
    )

    value, errors = validate_yaml("123", PersonSchema)
    assert errors == [
        ValidationError(
            text="Value must be greater than 100.", code="min_value", path=["name"]
        )
    ]



# Generated at 2022-06-14 15:01:28.432359
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Number
    from typesystem.schemas import Schema

    class MySchema(Schema):
        a = Number()

    yaml_str = "a: 123"
    value, error_msgs = validate_yaml(yaml_str, MySchema)
    assert value == {"a": 123}
    assert not error_msgs


# Generated at 2022-06-14 15:01:31.777570
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    pass

# Generated at 2022-06-14 15:01:43.125929
# Unit test for function validate_yaml
def test_validate_yaml():
    from typing import Any, List
    from typesystem.base import Value
    from typesystem.fields import IntegerField

    class PetSchema(Schema):
        age = IntegerField(minimum=0)

    value, error_messages = validate_yaml(
        """
        name: Fido
        age: 30
        """,
        PetSchema,
    )

    assert type(value) == dict
    assert value == {"name": "Fido", "age": 30}
    assert type(error_messages) == list
    assert len(error_messages) == 0

    _, error_messages = validate_yaml(
        """
        name: Fido
        age: -30
        """,
        PetSchema,
    )

    assert type(error_messages) == list

# Generated at 2022-06-14 15:01:46.175784
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer
    from typesystem.base import get_message
    field = Integer(max_value=100)
    result = validate_yaml(content="200", validator=field)
    assert result[-1] == [
        get_message(message="Must be less or equal than 100.", code="max_value")
    ]


# Generated at 2022-06-14 15:01:56.750841
# Unit test for function validate_yaml
def test_validate_yaml():
    def assert_raise_validation_error(content: str, validator: Field):
        with pytest.raises(ValidationError) as exc:
            validate_yaml(content, validator)

        # Make sure all errors are positional.
        if exc.value.errors:
            for error in exc.value.errors:
                assert any(
                    (
                        error.position.line_no,
                        error.position.column_no,
                        error.position.char_index,
                    )
                )

        return exc.value

    def assert_validation_error(content: str, validator: Field):
        valid, errors = validate_yaml(content, validator)
        assert not valid and errors

        return errors


# Generated at 2022-06-14 15:02:08.258485
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    from typesystem.structures import Structure

    class Str(Structure):
        f1 = String(max_length=7, min_length=1)

    value, errors = validate_yaml("f1: hello", validator=Str)
    assert value == {"f1": "hello"}
    assert errors == []

    value, errors = validate_yaml("f1: hello", validator=Str)
    assert value == {"f1": "hello"}
    assert errors == []

    value, errors = validate_yaml("f1: hello world", validator=Str)

# Generated at 2022-06-14 15:02:15.341895
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import String, Dict, Integer, Object, Root, List, fields

    class PhoneSchema(Object):
        number = String()

    class PersonSchema(Object):
        age = Integer()
        name = String()
        phone = fields.List(PhoneSchema())
        id = Integer()

    class PersonListSchema(Object):
        items = fields.List(PersonSchema())

    from typesystem import fields

    content = """
    age: 84
    name: John
    phone:
      - { number: '555-1212', type: home }
      - number: '555-1234'
    id: 15
    """

    def test_basic_validation():
        class Person(Schema):
            age = fields.Integer()
            name = fields.String()

# Generated at 2022-06-14 15:02:21.553049
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
        random: 8
        id: 123
        name: 'foo'
        """
    class ExampleSchema(Schema):
        random = Field(validators=[])
        id = Field(validators=[])
        name = Field(validators=[])
    value, error_messages = validate_yaml(content, ExampleSchema())
    assert error_messages == None
    assert value['random'] == 8
    assert value['id'] == 123
    assert value['name'] == 'foo'


# Generated at 2022-06-14 15:02:32.502406
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    from typesystem.fields import String
    from typesystem.schema import Schema
    from typesystem.types import Integer

    class AddressSchema(Schema):
        city = String()
        street = String(required=False)

    class PersonSchema(Schema):
        name = String()
        age = Integer()
        address = AddressSchema()
        role = String(required=False)

    yaml_content = '''
        name: Benny
        age: 27
        address:
          city: London
          street: Baker St
          '''
    value, error_messages = validate_yaml(content=yaml_content, validator=PersonSchema)

# Generated at 2022-06-14 15:02:44.189228
# Unit test for function validate_yaml
def test_validate_yaml():
    data = """
    foo: 1
    bar: a
    baz: b
    """
    field = Field(type=str)
    class Schema(typesystem.Schema):
        foo = field
        bar = field

    result, error_messages = validate_yaml(data, Schema)
    print(result)
    assert result['foo'] == 1
    assert result['bar'] == "a"
    assert error_messages[0].position.line_no == 2
    assert error_messages[0].position.column_no == 7
    assert error_messages[0].position.char_index == 9
    assert error_messages[0].text == "Invalid type."
    assert error_messages[0].code == "invalid_type"
    assert error_messages[1].position.line_

# Generated at 2022-06-14 15:02:55.467566
# Unit test for function validate_yaml
def test_validate_yaml():
    xfield = fields.String()
    yfield = fields.Integer()
    class Point(Schema):
        x = xfield
        y = yfield

    output1 = validate_yaml(
        content="""
        x: 1.0
        y: 1.0
        """,
        validator=Point,
    )

    assert output1[0] == {"x": "1.0", "y": "1.0"}
    assert len(output1[1]) == 2
    assert output1[1][0].text == "Value must be of type 'integer'."
    assert output1[1][1].text == "Value must be of type 'integer'."
    assert output1[1][0].code == "type_error.integer"
    assert output1[1][1].code == "type_error.integer"
   

# Generated at 2022-06-14 15:03:09.293911
# Unit test for function validate_yaml
def test_validate_yaml():
    import re
    import typesystem

# Generated at 2022-06-14 15:03:21.254647
# Unit test for function validate_yaml
def test_validate_yaml():
    """Unit test the YAML tokenizer and validation"""

    validator = Field(type="integer")
    # test good input
    value, errors = validate_yaml('"10"', validator)
    assert value == 10
    assert len(errors) == 0

    # test bad input
    value, errors = validate_yaml('"abc"', validator)
    assert value == None
    assert len(errors) == 1
    assert errors[0].code == "bad_type"
    assert errors[0].position.column_no == 1
    assert errors[0].position.line_no == 1
    assert errors[0].position.char_index == 0
    assert errors[0].message == "Value must be of type 'integer'."
    
    # test empty string
    value, errors = validate_yaml('', validator)

# Generated at 2022-06-14 15:03:27.249149
# Unit test for function validate_yaml
def test_validate_yaml():
    def node_to_tuple(node):
        text = '{}: {}'.format(node.line_no, node.text)
        return (text, node.line_no)

    test_data = """\
    ---
    id: 1
    title: Hello World
    content:
      body: Hello world
    """
    PostSchema = Schema(
        title=Field(type="string", required=True),
        content=Field(type="object", required=True),
        id=Field(type="number", required=True),
    )
    PostSchema.compile(schema_name="Post")
    value, errors = validate_yaml(content=test_data, validator=PostSchema)
    assert not errors
    assert isinstance(value, DictToken)

# Generated at 2022-06-14 15:03:29.062029
# Unit test for function validate_yaml
def test_validate_yaml():
    assert isinstance(validate_yaml(b"", validator=Schema()), tuple)


# Generated at 2022-06-14 15:03:39.126581
# Unit test for function validate_yaml
def test_validate_yaml():
    class MyValidator(Schema):
        my_string = Field(type=str)
        my_int = Field(type=int)
        my_bool = Field(type=bool)

    sample_content = dedent(
        """\
        my_string: "hello world"
        my_int: 123
        my_bool: true
    """
    )
    value, _ = validate_yaml(content=sample_content, validator=MyValidator)
    assert value == {"my_string": "hello world", "my_int": 123, "my_bool": True}

    # Test using a bytestring instead of a string.
    value, _ = validate_yaml(content=sample_content.encode("utf-8"), validator=MyValidator)

# Generated at 2022-06-14 15:03:49.873965
# Unit test for function validate_yaml
def test_validate_yaml():
    field = Field(string=True)
    value, errors = validate_yaml("str", field)

    assert value == "str"
    assert len(errors) == 0

    field = Field(string=True)
    value, errors = validate_yaml("123", field)

    assert value == "123"
    assert len(errors) == 0

    class MySchema(Schema):
        first_name = Field(string=True)
        last_name = Field(string=True)
        age = Field(integer=True)

    validator = MySchema

    value, errors = validate_yaml(
        content="""
        first_name: Bob
        last_name: Jones
        age: 30
        """,
        validator=validator,
    )
    assert value["first_name"] == "Bob"


# Generated at 2022-06-14 15:03:54.106383
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class Person(Schema):
        name = String()

    content = """name: "John" """
    assert validate_yaml(content=content, validator=Person) == (
        {"name": "John"},
        [],
    )



# Generated at 2022-06-14 15:04:04.753757
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Valid YAML
    assert tokenize_yaml("1") == ScalarToken("1", 0, 0, content="1")
    assert tokenize_yaml("12") == ScalarToken("12", 0, 1, content="12")
    assert tokenize_yaml("12.3") == ScalarToken("12.3", 0, 3, content="12.3")
    assert tokenize_yaml("1.2e-3") == ScalarToken("1.2e-3", 0, 5, content="1.2e-3")
    assert tokenize_yaml("1.2e-3") == ScalarToken("1.2e-3", 0, 5, content="1.2e-3")

# Generated at 2022-06-14 15:04:13.305310
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Unit test for validate_yaml
    """
    import typesystem

    class CustomerSchema(typesystem.Schema):
        name = typesystem.String(max_length=100)
        age = typesystem.Integer(minimum=18)
        street = typesystem.String(max_length=100, required=False)
        city = typesystem.String(max_length=100, required=False)
        state = typesystem.String(max_length=100, required=False)
        zip = typesystem.String(max_length=100, required=False)
        enabled = typesystem.Boolean()

    test_yaml = """
    name: John
    age: '25'
    street: 123 Main Street
    city: Anytown
    state: ST
    zip: 12345
    enabled: false
    """



# Generated at 2022-06-14 15:04:21.031500
# Unit test for function validate_yaml
def test_validate_yaml():
    # Arrange
    content = """
    foo:
    - bar: hello
    - baz: goodbye
    """

    fields = {
        "foo": Field(required=True, list_type=Field(list_type=Field(required=True)))
    }
    schema = type("TestSchema", (Schema,), fields)

    # Act
    (result, errors) = validate_yaml(content, validator=schema)

    # Assert
    assert result is not None
    assert not errors



# Generated at 2022-06-14 15:04:32.716823
# Unit test for function validate_yaml
def test_validate_yaml():
        class TestSchema(Schema):
            name = "TestSchema"
            fields = {"size": Field(type_="string")}
        def test_basic_api():
            content = "size: 5"
            value, errors = validate_yaml(content, TestSchema)
            assert value == {"size": "5"}
            assert not errors
            content = "size: 5\n"
            value, errors = validate_yaml(content, TestSchema)
            assert value == {"size": "5"}
            assert not errors
            content = "size: "
            value, errors = validate_yaml(content, TestSchema)
            assert value is None

# Generated at 2022-06-14 15:04:41.659708
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    class Person(typesystem.Schema):
        name = typesystem.String()

    value, errors = validate_yaml(content="""{name: Me}""", validator=Person)

    assert value == {"name": "Me"}
    assert len(errors) == 1
    assert isinstance(errors[0], typesystem.ValidationError)
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no == 1
    assert errors[0].position.char_index == 0
    assert errors[0].code == "type_error.string"
    assert errors[0].field.name == "name"



# Generated at 2022-06-14 15:04:49.337311
# Unit test for function validate_yaml
def test_validate_yaml():

    def assert_parse_error(content):
        with pytest.raises(ParseError) as exc:
            validate_yaml(content, validator=str)
        assert exc.value.code == "parse_error"

    def assert_validation_error(content, field):
        with pytest.raises(ValidationError) as exc:
            validate_yaml(content, validator=field)
        assert exc.value.code == "invalid"

    def validate_yaml_success(content, validator):
        value, error_messages = validate_yaml(content, validator)
        assert not error_messages
        assert value == expected
        return value

    # Test bytes
    validate_yaml_success(b"Hello World", validator=str)

    # Test validators
    assert_validation

# Generated at 2022-06-14 15:04:52.796161
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(name="test")(validators=[])
    assert validate_yaml(content="", validator=validator) == (None, [])



# Generated at 2022-06-14 15:04:57.056502
# Unit test for function validate_yaml
def test_validate_yaml():
    def test_schema():
        class Person(Schema):
            name = String(max_length=3)
            age = Integer(minimum=13)
        return Person
    validator = test_schema()
    content = """
    name: "John"
    age: 24
    """
    assert validate_yaml(content, validator)


# Generated at 2022-06-14 15:05:07.044645
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Object

    content = """
      # This is an example schema
      name: Planet
      properties:
        name:
          type: string
          minLength: 1
        position:
          type: number
          minimum: 1
        classification:
          type: string
          enum:
            - terrestrial
            - gas giant
            - ice giant
    """

    class PlanetSchema(Schema):
        name = "Planet"

        name = Field(type="string", min_length=1)
        position = Field(type="number", minimum=1)
        classification = Field(type="string", enum=["terrestrial", "gas giant", "ice giant"])

    value, error_messages = validate_yaml(content, validator=PlanetSchema)
    assert error_messages is None

# Generated at 2022-06-14 15:05:15.412323
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    Unit test for validate_yaml
    """
    from typesystem import validate
    from typesystem.schemas import Schema
    from typesystem.fields import String, Integer

    class MySchema(Schema):
        name = String()
        age = Integer()

    content = """
        name: Mike
        about: me
        age: 37
    """
    result = validate_yaml(content, validator=MySchema)
    assert result[1] == [
        Message(
            text='Value "{}" is not valid.'.format("'me'"),
            code="invalid",
            position=Position(
                line_no=3, column_no=3, char_index=15,
            ),
        )
    ]


# Generated at 2022-06-14 15:05:25.660398
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    """
    Test tokenize_yaml by checking the YAML token structure
    """
    import typesystem.tokenize.tokens as tokens
    import typesystem.fields as fields

    yaml_content = """
        - title : Hello
          tagline: world
        - title : Hello again
          tagline: world
        """
    tokens = tokenize_yaml(yaml_content)
    assert isinstance(tokens, tokens.ListToken)
    assert len(tokens.value) == 2
    assert isinstance(tokens.value[0], tokens.DictToken)
    assert isinstance(tokens.value[1], tokens.DictToken)

    # create a fields.Schema object

# Generated at 2022-06-14 15:05:37.168749
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    This is a unit test for validate_yaml function
    """
    content = "apple"
    validator = String(max_length=5)
    assert validate_yaml(content, validator) == ("apple", [])
    content = "app"
    assert validate_yaml(content, validator) == ("app", [])
    content = "apple apples"
    assert validate_yaml(content, validator) == (
        "apple ",
        [
            Message(
                text="Value is too long.",
                code="max_length",
                position=Position(
                    char_index=5, column_no=6, line_no=1
                ),
            )
        ],
    )
    content = "orange"
    validator = String(choices=("apple", "banana", "orange"))

# Generated at 2022-06-14 15:05:40.432499
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
        foo:
            bar: 42
    """
    token = tokenize_yaml(content)
    assert token.to_python() == {"foo": {"bar": 42}}, token



# Generated at 2022-06-14 15:05:51.395267
# Unit test for function validate_yaml
def test_validate_yaml():
    # 'pyyaml' must be installed.
    pyyaml = importlib.util.find_spec("yaml")
    assert pyyaml

    class Test(Schema):
        name = String(max_length=100)

    # Parse and validate a YAML string, returning positionally marked error messages on parse or validation failures.
    content = "name: test"
    token = tokenize_yaml(content)
    value, error_messages = validate_with_positions(token=token, validator=Test)

    # Assertions
    assert value["name"] == "test"
    assert not error_messages

# Generated at 2022-06-14 15:06:03.263500
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.tokenize.positional_validation import validate_with_positions

    class MySchema(Schema):
        name = String()

    parse_exc = ParseError(
        text="No content.",
        code="no_content",
        position=Position(column_no=1, line_no=1, char_index=0),
    )

    with pytest.raises(ParseError):
        validate_yaml("", validator=MySchema)

    with pytest.raises(ParseError) as exc:
        validate_yaml(" \n", validator=MySchema)
    assert exc.value.text == parse_

# Generated at 2022-06-14 15:06:06.817535
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = Field(type="string")
        age = Field(type="integer")

    content = " name: Bob  \n age: 30"
    assert validate_yaml(content, Person) == ({'name': 'Bob', 'age': 30}, [])

# Generated at 2022-06-14 15:06:12.846080
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        name = String()
        age = Integer()

    content = """
    name: Joe
    age: not a number
    """

    result, errors = validate_yaml(content, UserSchema)

    assert result == {"name": "Joe"}
    assert len(errors) == 1
    assert errors[0].code == "invalid_type"

