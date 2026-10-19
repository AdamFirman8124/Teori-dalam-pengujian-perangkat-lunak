

# Generated at 2022-06-14 14:56:33.521199
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    yaml_string = """
    ---
    '''
    a: 1
    ...
    '''
    """
    token = tokenize_yaml(yaml_string)
    assert token.children[0].text == "a: 1"
    # list token:
    assert token.children[0].children[1].start == 7
    assert token.children[0].children[1].end == 7
    assert token.children[0].children[1].value == "1"
    # dict token:
    assert token.children[0].children[0].start == 0
    assert token.children[0].children[0].end == 7



# Generated at 2022-06-14 14:56:45.417753
# Unit test for function validate_yaml
def test_validate_yaml():
    class ExampleValidator(Schema):
        field1 = fields.String()

    result, messages = validate_yaml("field1: foo", ExampleValidator)
    assert result == {"field1": "foo"}
    assert messages == []

    result, messages = validate_yaml("field1: 1", ExampleValidator)
    assert result == {"field1": "1"}
    assert len(messages) == 1
    assert messages[0].text == "'1' is not a string."
    assert messages[0].code == "not_string"
    assert messages[0].position == Position(column_no=11, line_no=1, char_index=10)

    result, messages = validate_yaml("field2: foo", ExampleValidator)
    assert result == {"field2": "foo"}

# Generated at 2022-06-14 14:56:50.978360
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Given a YAML string
    content = """
a: 1
b:
  c: "d"
  e: - 1
  f: null
  """
    # When the string is tokenized
    token = tokenize_yaml(content)

    # Then the right result is obtained
    assert type(token) == DictToken
    assert token.raw_value == {"a": "1", "b": {"c": "d", "e": ["1"], "f": "null"}}



# Generated at 2022-06-14 14:57:02.251987
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.types import String, Integer 

    validator = Schema.of({"name": String(), "age": Integer()})

    value, error_messages = validate_yaml(b"name: john\nage: 42", validator)  # type: ignore
    assert value == {"name": "john", "age": 42}
    assert error_messages == []

    value, error_messages = validate_yaml(b"name: john\nage: not an integer", validator)  # type: ignore
    assert error_messages == [
        Message(
            text="Value must be of type 'integer'.",
            code="type_error.integer",
            position=Position(column_no=5, line_no=2, char_index=11),
        )
    ]

    value, error_messages

# Generated at 2022-06-14 14:57:06.302867
# Unit test for function validate_yaml
def test_validate_yaml():
    class UserSchema(Schema):
        name = String()

    content = "name: 'Jhon'"
    value, error_messages = validate_yaml(content, UserSchema)

    assert value['name'] == 'Jhon'


# Generated at 2022-06-14 14:57:17.312567
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # Test Valid YAML
    simple_dict = """
    first:
        - item: one
          name: Spam
        - item: two
          name: Eggs
    """
    assert tokenize_yaml(simple_dict) == {
        "first": [
            {"item": "one", "name": "Spam"},
            {"item": "two", "name": "Eggs"},
        ]
    }

    simple_dict = """
    - first:
        - item: one
          name: Spam
        - item: two
          name: Eggs
    """
    assert tokenize_yaml(simple_dict) == [
        {"first": [{"item": "one", "name": "Spam"}, {"item": "two", "name": "Eggs"}]}
    ]


# Generated at 2022-06-14 14:57:28.254498
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String
    content = """
      - one
      - two
      - three
    """
    value, errors = validate_yaml(content, String())
    msg = errors[0]
    assert msg.text == "Not a valid string."
    assert msg.position.line_no == 2
    assert msg.position.column_no == 2
    assert msg.position.char_index == 6
    assert msg.code == "type_error"

    # Make sure the position columns are correct when there are tabs.
    content = "\t- one\n\t- two\n\t- three\n"
    value, errors = validate_yaml(content, String())
    msg = errors[0]
    assert msg.position.line_no == 2
    assert msg.position.column_no == 1
   

# Generated at 2022-06-14 14:57:33.239667
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Field(
        type="integer",
        required=True,
        minimum=10,
        maximum=100,
    )
    value, error_messages = validate_yaml(
        "20",
        validator,
    )
    assert value == 20
    assert len(error_messages) == 0



# Generated at 2022-06-14 14:57:43.546329
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    test to validate YAML
    """
    from bson import ObjectId
    from typesystem.fields import (
        Integer,
        String,
        DateTime,
        ObjectIdField,
        Dict,
        List,
        Boolean,
        Any,
    )
    from typesystem.schemas import Schema
    from copy import copy
    from datetime import datetime
    from datetime import date

    from dateutil.tz import UTC

    class MySchema(Schema):
        name = String(min_length=3, max_length=7)

    assert validate_yaml(b"", MySchema) == (
        {},
        [Message(error_code="no_content", text="No content.", position=Position(1, 1, 0))],
    )
    assert validate_yaml

# Generated at 2022-06-14 14:57:47.189531
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    foo: bar
    baz: [1, 2, 3]
    """
    assert tokenize_yaml(content) == {'foo': 'bar', 'baz': [1, 2, 3]}


# Generated at 2022-06-14 14:58:01.066451
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(tokenize_yaml("{}"), DictToken)
    assert isinstance(tokenize_yaml("[]"), ListToken)
    assert isinstance(tokenize_yaml("true"), ScalarToken)
    assert isinstance(tokenize_yaml("false"), ScalarToken)

    assert tokenize_yaml("{}").content == tokenize_yaml("{}").content
    assert tokenize_yaml("[]").content == tokenize_yaml("[]").content
    assert tokenize_yaml("true").content == tokenize_yaml("true").content
    assert tokenize_yaml("false").content == tokenize_yaml("false").content

    # Check case sensitive
    assert tokenize_yaml("True") != tokenize_yaml("true")

# Generated at 2022-06-14 14:58:05.377124
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "id: 123\nname: myname"
    validator = Schema(fields={"id":int,"name":str})
    value = validate_yaml(content,validator)
    assert value == ({'id': 123, 'name': 'myname'}, [])

# Generated at 2022-06-14 14:58:13.816666
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    phone_number:
        area_code: 819
        number: 5517583
    """
    schema = Schema(
        {
            "phone_number": Schema({"area_code": Field(type="string")})
            # Schema({"area_code": Field(type="string")})
            # This causes an error, since the correct schema is:
            # Schema({"area_code": Field(type="integer")})
        }
    )

    value, messages = validate_yaml(content, schema)
    assert messages[0].message == "Expected str but got int."
    assert isinstance(messages[0], ValidationError)
    assert messages[0].position.line_no == 3
    assert messages[0].position.column_no == 4
    assert messages[0].position

# Generated at 2022-06-14 14:58:24.607398
# Unit test for function validate_yaml
def test_validate_yaml():
    #test 2 valid cases
    yaml_str_1 = '''
    test-field_1: 1
    test-field_2: 2
    '''
    class ExampleSchema_1(Schema):
        test_field_1 = fields.Integer()
        test_field_2 = fields.Integer()
    value_1, error_messages_1 = validate_yaml(yaml_str_1, ExampleSchema_1)
    assert error_messages_1 == [], "No error messages should be returned"
    assert value_1['test_field_1'] == 1, "Expected integer value 1, but got {}".format(value_1['test_field_1'])

# Generated at 2022-06-14 14:58:30.903824
# Unit test for function validate_yaml
def test_validate_yaml():
    schema = Schema.from_dict({
        "string": String(),
        "integer": Integer(),
        "required": String(required=True),
    })
    valid, msgs = validate_yaml("""
string: 'foo'
integer: 42
""", schema)
    assert valid
    assert msgs == []

    valid, msgs = validate_yaml("""
string: 10
""", schema)
    assert not valid
    assert msgs == [
        Message(
            text="Incorrect type. Expected 'string' but got 'integer'.",
            code="incorrect_type",
            position=Position(char_index=9, column_no=2, line_no=2),
        )
    ]

    valid, msgs = validate_yaml("""
required: 10
""", schema)

# Generated at 2022-06-14 14:58:41.535298
# Unit test for function tokenize_yaml
def test_tokenize_yaml():

    token = tokenize_yaml("hi: 5")
    assert token.items() == [("hi", ScalarToken("5", 3, 3))]

    token = tokenize_yaml("hi: null")
    assert token.items() == [("hi", ScalarToken(None, 3, 7))]

    # We should just do this
    # assert validate_yaml("hi: 5", field.String) == ("hi: 5", None)

    value, error_messages = validate_yaml("hi: 5", field.String())

    assert error_messages == [
        Message("Expecting string at line 1, column 4.", "type_error", (1, 4))
    ]

    # Just to make sure we get the same error message for all invalid
    # scalars and not just strings.

# Generated at 2022-06-14 14:58:53.020947
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    # test scalar
    assert tokenize_yaml("foo") == ScalarToken(
        value="foo", start=0, end=2, content="foo"
    )
    assert tokenize_yaml("- foo") == ListToken(
        value=["foo"], start=0, end=5, content="- foo"
    )
    assert tokenize_yaml("foo: bar") == DictToken(
        value={"foo": "bar"}, start=0, end=7, content="foo: bar"
    )

    # test dict values
    assert tokenize_yaml("foo: bar") == DictToken(
        value={"foo": "bar"}, start=0, end=7, content="foo: bar"
    )

# Generated at 2022-06-14 14:58:58.673543
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = '{"title": "Hello world!"}'
    token = tokenize_yaml(content=content)
    assert token.start == 0
    assert token.end == 22
    assert token.content == '{"title": "Hello world!"}'
    assert len(token.data) == 1
    assert token.data["title"] == "Hello world!"



# Generated at 2022-06-14 14:59:11.079469
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    yaml_string = '''
    a: 12
    b: [1, 2, 3]
    c:
      - ca: "first"
      - cb: "second"
      - cc: "third"
    '''
    parsed = tokenize_yaml(yaml_string)
    assert isinstance(parsed, DictToken), (
        "tokenize_yaml should return a DictToken: %r" % parsed
    )
    assert len(parsed) == 3, "tokenize_yaml should parse a 3-key dictionary"
    assert parsed["a"] == ScalarToken(12, position_start=4, position_end=4, content=yaml_string)

# Generated at 2022-06-14 14:59:15.496232
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = "foo: bar"
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token["foo"] == "bar"
    assert token.start_index == 0
    assert token.end_index == 7


# Unit tests for function validate_yaml

# Generated at 2022-06-14 14:59:26.633384
# Unit test for function validate_yaml
def test_validate_yaml():
    # tests with strings
    assert validate_yaml("name: hubert", "name")[0] == "hubert"
    assert validate_yaml("{}", "name")[1][0].text == "Required field 'name'."
    assert validate_yaml("{}", "name")[1][0].code == "required"
    assert validate_yaml("{}", "name")[1][0].position == Position(1, 2, 1)
    assert validate_yaml("{}", "list")[0] == []
    assert validate_yaml("{}", "list")[1] == []
    assert validate_yaml("name: hubert", "[name]")[0] == ["hubert"]
    assert validate_yaml("name: hubert", "[name]")[1] == []
   

# Generated at 2022-06-14 14:59:35.441281
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
            -
                name: John
                age: "25"
                member: yes
                scores: [95, -1, 5, 91]
            -
                name: Ann
                age: "23"
                member: no
                scores: [90, 5, 91]
            -
                name: Dave
                age: "27"
                member: yes
                scores: [100, 27, 91]
                extra: foo
            -
                name: Mary
                age: "22"
                member: yes
                scores: [20, 27, 91]
                extra: bar
            """
    class Person(Schema):
        name = Field(str, required=True)
        age = Field(str, required=True)
        member = Field(str, required=True)

# Generated at 2022-06-14 14:59:41.634185
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    x: 2
    y: 1
    """

    class TestSchema(Schema):
        x = Field(type="integer")
        y = Field(type="integer")

    assert validate_yaml(content, validator=TestSchema) == (
        {u"x": 2, u"y": 1},
        [],  # No validation errors
    )



# Generated at 2022-06-14 14:59:46.031259
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    foo: bar
    """

    schema = Schema(properties={"foo": Field(type="string")})

    value, errors = validate_yaml(content, schema)
    assert value == {"foo": "bar"}
    assert errors == []



# Generated at 2022-06-14 14:59:46.638663
# Unit test for function validate_yaml
def test_validate_yaml():
    pass

# Generated at 2022-06-14 14:59:55.924963
# Unit test for function validate_yaml
def test_validate_yaml():
    try:
        import yaml
    except ImportError:  # pragma: no cover
        pytest.skip("pyyaml must be installed.")

    class User(Schema):
        name = Field(type="string")
        age = Field(type="integer")
        active = Field(type="boolean")

    content = """
    name: Paul
    age: 100
    active: true
    """

    value = validate_yaml(content, User)

    assert value == {
        "name": "Paul",
        "age": 100,
        "active": True,
    }



# Generated at 2022-06-14 15:00:04.150804
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml("{}") == DictToken(
        {}, start=0, end=1, content="{}"
    )
    assert tokenize_yaml("[]") == ListToken(
        [], start=0, end=1, content="[]"
    )
    assert tokenize_yaml("""\
a: 1
b: 2
""") == DictToken(
        {"a": ScalarToken(1, start=2, end=3, content="""\
a: 1
b: 2
"""),
         "b": ScalarToken(2, start=8, end=9, content="""\
a: 1
b: 2
""")},
        start=0,
        end=10,
        content="""\
a: 1
b: 2
""",
    )




# Generated at 2022-06-14 15:00:15.437018
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String

    content = "# No token here"
    validator = String()
    value, error = validate_yaml(content, validator)
    assert error == ["Expected a string."]
    assert value == None

    content = "one"
    validator = String()
    value, error = validate_yaml(content, validator)
    assert error == []
    assert value == "one"

    content = "one\ntwo"
    validator = String()
    value, error = validate_yaml(content, validator)
    assert error == []
    assert value == "one\ntwo"

    content = "# No token here\n---\n"
    validator = String()
    value, error = validate_yaml(content, validator)

# Generated at 2022-06-14 15:00:19.446520
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "name: something\n"
    validator = Field(type="string")
    value, error_messages = validate_yaml(content, validator)
    assert error_messages == []
    assert value == "something"

# Generated at 2022-06-14 15:00:28.202762
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml(b"abc") == ScalarToken("abc", 0, 2, content="abc")
    assert tokenize_yaml(b"- foo") == ListToken(["foo"], 0, 5, content="- foo")
    assert tokenize_yaml(b"- 1") == ListToken([1], 0, 3, content="- 1")
    assert tokenize_yaml(b"- 1.1") == ListToken([1.1], 0, 5, content="- 1.1")
    assert tokenize_yaml(b"- True") == ListToken([True], 0, 6, content="- True")
    assert tokenize_yaml(b"- Null") == ListToken([None], 0, 5, content="- Null")

# Generated at 2022-06-14 15:00:37.564114
# Unit test for function validate_yaml
def test_validate_yaml():
    content = b"foo: bar\nbaz: quux\n"
    fields = {
        "foo": {"type": "string"},
        "baz": {"type": "string"},
    }
    class TestSchema(Schema):
        fields = fields
    value, errors = validate_yaml(content, TestSchema)
    assert value == {'foo': 'bar', 'baz': 'quux'}
    assert errors == []



# Generated at 2022-06-14 15:00:48.417746
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = """
    foo:
        foo1:
            foo2:
                foo3: "foo4"
    """
    token = tokenize_yaml(content)
    assert isinstance(token, DictToken)
    assert token.value.keys() == {"foo"}
    assert isinstance(token.value["foo"], DictToken)
    assert token.value["foo"].value.keys() == {"foo1"}
    assert isinstance(token.value["foo"].value["foo1"], DictToken)
    assert token.value["foo"].value["foo1"].value.keys() == {"foo2"}
    assert isinstance(token.value["foo"].value["foo1"].value["foo2"], DictToken)

# Generated at 2022-06-14 15:00:59.404520
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "subject: The dog"
    field = Field(name="subject", required=False)
    value, error_messages = validate_yaml(content, field)
    assert value == "The dog"
    assert len(error_messages) == 0
    content = "subject: The dog\nage: 4"
    field = Field(name="subject", required=True)
    value, error_messages = validate_yaml(content, field)
    assert value == "The dog"
    assert len(error_messages) == 0
    content = ""
    field = Field(name="subject", required=True)
    value, error_messages = validate_yaml(content, field)
    assert value == ""
    assert error_messages[0].text == "No content."

# Generated at 2022-06-14 15:01:10.597465
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String()
        age = Integer()

    validator = Person()

    yaml = "name: George\nage: 30"
    value, errors = validate_yaml(yaml, validator)
    assert errors == []
    assert value == {"name": "George", "age": 30}

    # Test a non-matching value
    yaml = "name: George\nage: 30years"
    value, errors = validate_yaml(yaml, validator)
    assert errors == [
        ValidationError(
            field_name="age",
            text="Must be a valid integer.",
            code="invalid_type",
            position=Position(line_no=2, column_no=5, char_index=15),
        )
    ]

    # Make sure we can

# Generated at 2022-06-14 15:01:15.753695
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem import Integer

    class Person(Schema):
        name = [Integer(), "str"]
        age = Integer()

    content = b'name: "bob"\nage: 22'
    
    # Test for a valid yaml schema
    assert validate_yaml(content=content, validator=Person())



# Generated at 2022-06-14 15:01:23.145423
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    from typesystem import types

    class PersonSchema(Schema):
        name = types.String()
        age = types.Integer()

    errors = validate_yaml(
        content="name: foo age: not an int", validator=PersonSchema()
    )[1]

    assert len(errors) == 1
    assert errors[0].text == "must be an integer."
    assert errors[0].code == "type_error.integer"
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no == 13
    assert errors[0].position.char_index == 12



# Generated at 2022-06-14 15:01:25.848694
# Unit test for function validate_yaml
def test_validate_yaml():
    errors = validate_yaml(
    content='''
    incorrect: 
      name: "k"
      age: 
        value: "5"
        type: "int"
    ''',
    validator=Person,
    )
    assert len(errors) == 1, "Expected single error"
    err = errors[0]
    assert err.code == 'invalid' and err.text == "Value must be of type '<class 'str'>'", err.text

# Generated at 2022-06-14 15:01:27.787220
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    token = tokenize_yaml("""
    test: 10
    """)
    assert isinstance(token, DictToken)
    assert token.keys() == ["test"]
    assert token.__getitem__("test") == 10



# Generated at 2022-06-14 15:01:36.150116
# Unit test for function validate_yaml
def test_validate_yaml():
    # Valid
    class Testy(Schema):
        name = String()
        age = Integer(minimum=1)

    content = """
        name: Mr Test
        age: 62
    """
    assert validate_yaml(content, Testy) == ({"name": "Mr Test", "age": 62}, [])
    content = """
        bar:
        - "foo"
        - "spam"
    """
    assert validate_yaml(content, Dict({"bar": List(String())})) == (
        {"bar": ["foo", "spam"]},
        [],
    )

    # Invalid
    content = """
        name: [1991, 2001]
        age: 62
    """
    errors = validate_yaml(content, Testy)[1]
    assert len(errors) == 1

# Generated at 2022-06-14 15:01:44.009793
# Unit test for function validate_yaml
def test_validate_yaml():
    class Person(Schema):
        name = String(max_length=6)
        age = Integer(maximum=100)

    content = """\
        name: Sam
        age: 1000
    """
    value, errors = validate_yaml(content, Person)

    assert value == {"name": "Sam", "age": 1000}
    assert len(errors) == 1
    assert errors[0].text == "Must be less than or equal to 100."
    assert errors[0].code == "max_value"
    assert errors[0].position == Position(line_no=4, column_no=10, char_index=13)



# Generated at 2022-06-14 15:01:56.901485
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import Integer, String, List
    from typesystem.schemas import Schema

    # Schema to validate against.
    class Schema1(Schema):
        name = String()
        age = Integer()

    class Schema2(Schema):
        list = List(items=Integer())

    content = """
    foo: bar
    amount: 50
    """

    # No errors.
    value, errors = validate_yaml(content, validator=Schema1)
    assert errors == []
    assert value == {"foo": "bar", "amount": 50}

    # Errors.
    content = """
    foo: bar
    amount: 50
    """

    value, errors = validate_yaml(content, validator=Schema2)
    assert len(errors) == 1

# Generated at 2022-06-14 15:02:02.242133
# Unit test for function validate_yaml
def test_validate_yaml():
    class PersonSchema(Schema):
        name = String()
        age = Integer()

    content = """
    name: Bob
    age: 10
    """

    value, messages = validate_yaml(content, PersonSchema)
    assert value == {"name": "Bob", "age": 10}
    assert len(messages) == 0



# Generated at 2022-06-14 15:02:08.321738
# Unit test for function validate_yaml
def test_validate_yaml():
    data = """
        username: john.doe
        email: john@example.com
        password:
            hash: SHA256:
            salt:
        full_name: John Doe
        about:
        age: 25
        admin: true
        interests:
            - programming
            - music
            - sports
    """
    class UserSchema(Schema): # noqa
    
        username = fields.String(max_length=32, min_length=4)
        email = fields.Email()
        password = fields.Dict({
            "hash": fields.String(max_length=64),
            "salt": fields.String(max_length=64),
        })
        full_name = fields.String(max_length=255, required=False)

# Generated at 2022-06-14 15:02:16.208502
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None
    content = """
    title: Hello world
    description: None
    """
    validator = Schema(
        fields={
            "title": Field(type="string"),
            # description is allowed to be null
            "description": Field(type="string")
        }
    )
    value, error_messages = validate_yaml(content=content, validator=validator)
    assert value == {'title': 'Hello world', 'description': None}
    assert error_messages == []


# Generated at 2022-06-14 15:02:21.019248
# Unit test for function validate_yaml
def test_validate_yaml():
    """Test validate_yaml function."""
    content = "name: Brian"
    fields = {"name": "string"}
    value, errors = validate_yaml(content, fields)
    assert value == {"name": "Brian"}
    assert len(errors) == 0

    class Person(Schema):
        name = "string"

    Person.validate_yaml(content)

# Generated at 2022-06-14 15:02:32.468684
# Unit test for function validate_yaml
def test_validate_yaml():
    validator = Schema({"name": Field(type="string"), "age": Field(type="integer")})
    content = "name: 'Tom'\nage: 23"
    (value, error_messages) = validate_yaml(content, validator)
    print(value)
    print(error_messages)
    # {'name': 'Tom', 'age': 23}
    # []
    content2 = "age: 23"
    (value, error_messages) = validate_yaml(content2, validator)
    print(value)
    print(error_messages)
    # {'age': 23}
    # [Message(text='Field is required.', code='required', position=Position(char_index=3, column_no=1, line_no=1))]

# Generated at 2022-06-14 15:02:43.806240
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String, Integer

    schema = Schema([String("name"), Integer("age")])

    value, error = validate_yaml(
        """
        age: "not an integer"
        name: Josh
        """,
        schema,
    )
    assert error == [
        Message(
            code="invalid_type",
            text="Must be of type integer.",
            position=Position(
                line_no=2, column_no=1, char_index=16, full_text="age: 'not an integer'"
            ),
        )
    ]

    value, error = validate_yaml(
        """
        age: 10
        name: Josh
        """,
        schema,
    )
    assert error == []



# Generated at 2022-06-14 15:02:54.962579
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String, Integer, Boolean, Float
    from typesystem.schemas import Schema

    # Simple validation test
    class UserSchema(Schema):
        name = String(max_length=100)
        age = Integer()
        married = Boolean(default=False)

    token, errors = validate_yaml(
        """
        name: "John"
        age: 45
        married: true
        """,
        UserSchema,
    )
    assert isinstance(token, DictToken)
    assert len(errors) == 0

    # Test float
    class FloatSchema(Schema):
        name = Float()

    token, errors = validate_yaml("name: 45.0", FloatSchema)
    assert isinstance(token, DictToken)

# Generated at 2022-06-14 15:03:06.385077
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "pyyaml is not installed"
    from typesystem import Integer, String, Array, Boolean

    val = """[{"name": "John", "age": 28, "flag": false},
              {"name": "Jane", "age": 45, "flag": false},
              {"name": "Bob", "age": 12, "flag": true}]"""
    class Person(Schema):
        name = String()
        age = Integer()
        flag = Boolean(required=False)

    class People(Schema):
        people = Array(items=Person)

    value, error_messages = validate_yaml(val, Person)
    assert value is None

# Generated at 2022-06-14 15:03:12.153055
# Unit test for function validate_yaml
def test_validate_yaml():
    from typesystem.fields import String, Dict
    from typesystem.schemas import Schema

    class NameSchema(Schema):
        first_name = String(blank=False, max_length=10)
        last_name = String(blank=False, max_length=10)

    class PersonSchema(Schema):
        name = NameSchema()

    content = """
    name:
      first_name: "Bob"
      last_name:  "Dole"
    """

    value, errors = validate_yaml(content.encode(), validator=PersonSchema)

    assert errors is None
    assert value == {"name": {"first_name": "Bob", "last_name": "Dole"}}


# Generated at 2022-06-14 15:03:25.600554
# Unit test for function validate_yaml
def test_validate_yaml():
    content = r'''
    first_name: "Alice"
    last_name: "Bob"
    '''
    class TestSchema(Schema):
        first_name = fields.String()
        last_name = fields.String()

    schema = TestSchema()

    # Test basic parsing and validating of YAML
    value, error_messages = validate_yaml(content, schema)
    assert value == {
        'first_name': 'Alice',
        'last_name': 'Bob',
    }
    assert error_messages is None

    # Test basic parsing and invalidating of YAML
    content = r'''
    first_name: 'Alice'
    last_name: 'Bob'
    '''
    value, error_messages = validate_yaml(content, schema)
    assert value

# Generated at 2022-06-14 15:03:35.491327
# Unit test for function validate_yaml
def test_validate_yaml():
  content = """
  name: "John"
  age: 42
  location:
    latitude: 32.1234
    longitude: -96.1234
  """
  validator = Schema(
    fields={
      "name": Field(type="string"),
      "age": Field(type="number"),
      "location": Field(type="object", fields={
        "latitude": Field(type="number"),
        "longitude": Field(type="number")
      })
    }
  )
  assert validate_yaml(content, validator) == ({
    "name": "John",
    "age": 42.0,
    "location": {
      "latitude": 32.1234,
      "longitude": -96.1234
    }
  }, [])

# Generated at 2022-06-14 15:03:39.389866
# Unit test for function validate_yaml
def test_validate_yaml():
    class PetSchema(Schema):
        name = "string"
        age = "number"

    content = "name: Howard\nage: 99"
    value, error_messages = validate_yaml(content, PetSchema)
    assert error_messages == []
    assert value == {"name": "Howard", "age": 99}

# Generated at 2022-06-14 15:03:43.860804
# Unit test for function validate_yaml
def test_validate_yaml():
	content = """ 
person: 
	age: 23 
	name: john
"""
	
	# compiling schema
	Person = Schema("Person", [("name", String()), ("age", Integer())])
	
	values, errors = validate_yaml(content, Person)
	print(values, errors)

# Generated at 2022-06-14 15:03:53.661089
# Unit test for function validate_yaml
def test_validate_yaml():
    field = typesystem.String(max_length=5)
    # test a valid value
    code = """
    "ab"
    """
    text, error_messages = validate_yaml(code, field)
    assert text == "ab"
    assert error_messages is None

    # test an invalid value
    code = """
    "abcde"
    """
    text, error_messages = validate_yaml(code, field)
    assert error_messages[0].text == "Must be max length of '5'."
    assert error_messages[0].code == "max_length"

    schema = typesystem.Schema(
        "ab",
        fields={
            "ab": typesystem.String(max_length=5)
        },
    )


# Generated at 2022-06-14 15:04:02.020435
# Unit test for function validate_yaml
def test_validate_yaml():
    import typesystem
    import typesystem_yaml
    from typesystem.schema import Schema
    from typesystem.fields import Integer, String, List
    import pytest

    class MySchema(Schema):
        name = String()
        age = Integer()
        items = List[String]()

    # No errors for a valid document
    content = b"""name: Bob
age: 35
items:
  - one
  - two
  - three
"""
    value, error_messages = typesystem_yaml.validate_yaml(
      content, validator=MySchema
    )
    assert len(error_messages) == 0
    assert value["name"] == "Bob"
    assert value["age"] == 35
    assert len(value["items"]) == 3

    # Invalid document syntax

# Generated at 2022-06-14 15:04:11.748431
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert tokenize_yaml('test: "test"\n') == DictToken({'test': 'test'}, 0, 9, content='test: "test"\n')
    assert tokenize_yaml('test:\n  - 123\n') == DictToken({'test': [123]}, 0, 8, content='test:\n  - 123\n')
    assert tokenize_yaml('- "1"\n- "2"\n') == ListToken(['1', '2'], 0, 8, content='- "1"\n- "2"\n')
    assert tokenize_yaml('"test"') == ScalarToken('test', 0, 5, content='"test"')
    assert tokenize_yaml('123') == ScalarToken(123, 0, 3, content='123')
    assert token

# Generated at 2022-06-14 15:04:18.315031
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    content = b"""
        john: doe
        age: 32
        height:
            unit: meters
            length: 2.1
        friends:
            - name: foo
              age: 10
            - name: bar
              age: 20
    """
    token = tokenize_yaml(content)
    assert token["john"] == ScalarToken("doe", 3, 10, content=content.decode("utf-8"))

# Generated at 2022-06-14 15:04:27.606604
# Unit test for function validate_yaml
def test_validate_yaml():
    content = '''
    application:
      dashboard:
        url: 'https://example.com/dashboard'
    '''
    from typesystem import Schema, String
    # Schema to validate against
    class MySchema(Schema):
        application = Schema.Field(type=Schema.Object(
            fields={
                'dashboard': Schema.Field(type=Schema.Object(
                    fields={
                        'url': Schema.Field(type=String)
                    }
                ))
            }
        ))
    # Validate
    value, error_messages = validate_yaml(content, MySchema)
    assert value == {'application': {'dashboard': {'url': 'https://example.com/dashboard'}}}
    assert error_messages == []

# Generated at 2022-06-14 15:04:29.956250
# Unit test for function validate_yaml
def test_validate_yaml():
    content = """
    - one
    - "two"
    - three
    """
    validator=ListField(items=StrField())
    validate_yaml(content,validator)

# Generated at 2022-06-14 15:04:42.114798
# Unit test for function validate_yaml
def test_validate_yaml():
    print('\n')
    print('Testing validate_yaml')
    content = "fruit: apple"
    validator = Field(type=str)
    
    value = validate_yaml(content, validator)
    print(value)
    assert value[0] == 'apple'

    content = "fruit: 2"
    validator = Field(type=str)
    
    
    value = validate_yaml(content, validator)
    print(value)
    assert value[0] == '2'

if __name__ == '__main__':
    # test_validate_yaml()
    print(validate_yaml("fruit: 2", Field(type=str)))

# Generated at 2022-06-14 15:04:46.319632
# Unit test for function validate_yaml
def test_validate_yaml():
    content = "hello: world"
    class MySchema(Schema):
        hello = Field(str)

    value, messages = validate_yaml(content, validator=MySchema)
    assert type(value) is dict
    assert value == {"hello": "world"}
    assert len(messages) == 0



# Generated at 2022-06-14 15:04:56.949102
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        name = fields.String()
        age = fields.Integer()
        is_active = fields.Boolean()
        last_login = fields.DateTime()
        favorite_numbers = fields.Array(fields.Integer())
    schema = MySchema()
    content = """
    name: Tom Riddle
    age: 20
    is_active: true
    last_login: 2035-01-01T01:02:03
    favorite_numbers: [1, 2, 3]
    """

# Generated at 2022-06-14 15:05:07.047560
# Unit test for function validate_yaml
def test_validate_yaml():
    class MySchema(Schema):
        field1 = Field(string_types)
        field2 = Field(string_types)
        field3 = Field(string_types)

    value, msgs = validate_yaml("---\nfield1: 'hi'\n", MySchema)
    assert not msgs
    assert value == MySchema(field1='hi')

    value, msgs = validate_yaml("---\nfield1: 'hi'\nfield3: 'bye'\n", MySchema)

# Generated at 2022-06-14 15:05:10.779491
# Unit test for function tokenize_yaml
def test_tokenize_yaml():
    assert isinstance(tokenize_yaml(5), ScalarToken)
    assert isinstance(tokenize_yaml([5,5]), ListToken)
    assert isinstance(tokenize_yaml({'a':5}), DictToken)



# Generated at 2022-06-14 15:05:22.951751
# Unit test for function validate_yaml
def test_validate_yaml():

    class GoodSchema(Schema):
        foo = Field(type="string", max_length=5)
        bar = Field(type="integer", min_value=42)

    class BadSchema(Schema):
        foo = Field(type="string", max_length=5)
        bar = Field(type="integer", min_value=42)

    result1 = validate_yaml('{"foo": "1234", "bar": "42"}', GoodSchema)
    assert result1 == ({'foo': '1234', 'bar': 42}, None)
    
    result2 = validate_yaml('{"foo": "123456", "bar": "42"}', GoodSchema)

# Generated at 2022-06-14 15:05:36.425178
# Unit test for function validate_yaml
def test_validate_yaml():
    """
    This test is for validate_yaml function.
    """
    content = ""
    validator = "String"
    value, error_messages = validate_yaml(content, validator)
    assert error_messages.as_json() == [
        {
            "code": "no_content",
            "position": {"column_no": 1, "line_no": 1, "char_index": 0},
            "text": "No content.",
        }
    ]
    assert value == None

    content = "abc"
    validator = "String"
    value, error_messages = validate_yaml(content, validator)

# Generated at 2022-06-14 15:05:46.752870
# Unit test for function validate_yaml
def test_validate_yaml():
    assert validate_yaml("", int) == (0, [])
    assert validate_yaml("1", int) == (1, [])
    assert validate_yaml("1.1", float) == (1.1, [])
    assert validate_yaml("-1", int) == (-1, [])
    assert validate_yaml("a", str) == ("a", [])
    assert validate_yaml("true", bool) == (True, [])
    assert validate_yaml("false", bool) == (False, [])
    assert validate_yaml("null", type(None)) == (None, [])
    assert validate_yaml('"a"', str) == ("a", [])
    assert validate_yaml("[1, 2, 3]", List(int)) == ([1, 2, 3], [])

# Generated at 2022-06-14 15:05:51.700885
# Unit test for function validate_yaml
def test_validate_yaml():
    assert yaml is not None, "'pyyaml' must be installed."

    from typesystem import Integer, String

    class TestSchema(Schema):

        name = String()
        age = Integer()

    data = """
    name: Tester
    age: 25
    """
    content = TestSchema.validate(data)
    assert content == {"name":"Tester", "age": 25}
    assert content.errors == []

    invalid_data = """
    name: Tester
    age: 25
    weight: 70kg
    """
    content = TestSchema.validate(invalid_data)
    assert content == {"name": "Tester", "age": 25}
    assert content.errors[0].text == "Additional fields are not allowed."
    assert content.errors[0].code == "additional_fields"

# Generated at 2022-06-14 15:06:03.385937
# Unit test for function validate_yaml
def test_validate_yaml():
    class User(Schema):
        first_name = String(format='title')
        count = Integer()
        is_admin = Boolean()

    schema = User(format="yaml")

    try:
        value, error_messages = validate_yaml(
            "first_name: john\ncount: 5\nis_admin: true", schema
        )
    except ValidationError as exc:
        error_messages = exc.messages
    assert error_messages == [
        Message(text="Must be a valid title.", code="format")
    ]

    try:
        value, error_messages = validate_yaml(
            "first_name: John\ncount: five\nis_admin: true", schema
        )
    except ValidationError as exc:
        error_messages = exc.messages

# Generated at 2022-06-14 15:06:14.782566
# Unit test for function validate_yaml
def test_validate_yaml():
    yaml_content = """
        name: example
        age: 8
    """

    class ExampleSchema(Schema):
        name = Field(type="string", max_length=16)
        age = Field(type="integer", minimum=0, maximum=100)

    value, errors = validate_yaml(yaml_content, ExampleSchema)

    assert value == {"name": "example", "age": 8}
    assert errors == []

