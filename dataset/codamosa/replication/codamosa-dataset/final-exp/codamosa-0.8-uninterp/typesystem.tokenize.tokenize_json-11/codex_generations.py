

# Generated at 2022-06-14 14:45:47.255003
# Unit test for function validate_json
def test_validate_json():
    assert validate_json(b'{"int": "1"}', "int") == (1, [])
    assert validate_json(b'{"int": "1"}', "str") == ("1", [])
    assert validate_json(b'{"int": "1"}', "float") == (1.0, [])

    assert validate_json(b'{"int": "1", "str": "2"}', "dict") == (
        {"int": 1, "str": "2"}, []
    )

    assert validate_json(b'{"int": "1", "str": "2"}', ["int", "str"]) == (
        {"int": 1, "str": "2"}, []
    )


# Generated at 2022-06-14 14:45:56.376647
# Unit test for function validate_json
def test_validate_json():
    content = "8.0"
    validator = Field(type="float")
    (value, errors) = validate_json(content, validator)
    assert len(errors) == 0
    assert value == 8.0

    content = "8"
    validator = Field(type="float")
    (value, errors) = validate_json(content, validator)
    assert len(errors) == 0
    assert value == 8.0

    content = "foo"
    validator = Field(type="float")
    (value, errors) = validate_json(content, validator)
    assert len(errors) == 1
    assert errors[0].code == "invalid_type"

    content = "8.0"
    validator = Field(type="int")

# Generated at 2022-06-14 14:46:00.461034
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")
    assert tokenize_json("[1, \"foo\"]") == ListToken([1, "foo"], 0, 12, "[1, \"foo\"]")
    assert tokenize_json("{\"foo\": 1}") == DictToken({"foo": 1}, 0, 10, "{\"foo\": 1}")



# Generated at 2022-06-14 14:46:04.868933
# Unit test for function validate_json
def test_validate_json():
    validator = Field(type="string")
    with pytest.raises(ValidationError) as exc:
        validate_json("[]", validator)

    assert exc.value.code == "type_error"
    assert isinstance(exc.value.messages, list)
    assert len(exc.value.messages) == 2

# Generated at 2022-06-14 14:46:15.528175
# Unit test for function validate_json
def test_validate_json():
    content = '{"x": 5}'
    validator = {"x": int}
    validation_output = validate_json(content, validator)
    assert type(validation_output) == tuple
    assert validation_output[0] == {"x": 5}
    assert type(validation_output[1]) == list
    assert len(validation_output[1]) == 0

    content = '{"x": "hello"}'
    validator = {"x": int}
    validation_output = validate_json(content, validator)
    assert type(validation_output) == tuple
    assert validation_output[0] == {}
    assert type(validation_output[1]) == list
    assert len(validation_output[1]) == 1
    assert type(validation_output[1][0]) == ValidationError

# Generated at 2022-06-14 14:46:21.483746
# Unit test for function validate_json
def test_validate_json():

    @dataclass
    class Movie(Schema):
        """A movie."""

        # The title (string)
        title: str
        # The year the movie was released (integer)
        year: int

    s = '{"title": "Avengers: Endgame", "year": 2019}'

    value, messages = validate_json(s, Movie)

    assert messages == []
    assert value.title == value.title
    assert value.year == 2019



# Generated at 2022-06-14 14:46:26.605984
# Unit test for function validate_json
def test_validate_json():
    a_dict = {'a': 1, 'b': 2}
    a_string = """{"a": 1, "b": 2}"""
    a_unicode_string = """{"a": 1, "b": 2}"""
    error_string = """{"a"}"""
    a_bytes_string = b"""{"a": 1, "b": 2}"""

    validate_json(a_dict, {})

    validate_json(a_string, {})

    validate_json(a_unicode_string, {})

    validate_json(error_string, {})

    validate_json(a_bytes_string, {})

# Generated at 2022-06-14 14:46:33.943016
# Unit test for function validate_json
def test_validate_json():
    import json
    import pytest
    content = json.dumps({'foo': 'bar'})

    from typesystem.types import String

    field = String(max_length=3)

    value, error_messages = validate_json(content, field)

    assert error_messages == [
        Message(
            text="Must be less than or equal to 3 characters.",
            code="max_length",
            position=Position(1, 1, 0),
        )
    ]
    assert value == 'bar'


# Generated at 2022-06-14 14:46:39.763665
# Unit test for function tokenize_json
def test_tokenize_json():
    content = bytes('{"foo": "bar", "baz": [1, 2, 3]}', 'utf-8')
    token = tokenize_json(content)
    assert token.value['foo'] == 'bar'
    assert token.value['baz'][0] == 1
    s = '{"foo": "bar"}'
    assert tokenize_json(s) == token



# Generated at 2022-06-14 14:46:45.880991
# Unit test for function validate_json
def test_validate_json():
    field = Field(type="string")
    assert validate_json('"Name"', field) == ("Name", [])
    assert validate_json("Name", field) == (None, [{'code': 'type_error', 'position': {'line_no': 1, 'column_no': 1, 'char_index': 0}, 'text': 'Expected string', 'field': 'root'}])
    assert validate_json('', field) == (None, [{'code': 'no_content', 'position': {'line_no': 1, 'column_no': 1, 'char_index': 0}, 'text': 'No content.', 'field': 'root'}])

# Generated at 2022-06-14 14:47:09.410002
# Unit test for function tokenize_json
def test_tokenize_json():
    good_json = """
        {
          "name": "Leonard Hofstadter",
          "occupation": "Experimental Physicist"
        }
    """
    dict_token = DictToken(
        scalars={
            ScalarToken(
                "Leonard Hofstadter", start=16, end=32, content=good_json
            ): ScalarToken(
                "name", start=10, end=14, content=good_json
            ),
            ScalarToken(
                "Experimental Physicist", start=54, end=78, content=good_json
            ): ScalarToken(
                "occupation", start=47, end=56, content=good_json
            ),
        },
        start=1,
        end=83,
        content=good_json,
    )
    assert tokenize_json

# Generated at 2022-06-14 14:47:16.674515
# Unit test for function tokenize_json
def test_tokenize_json():
    # Empty string case
    with pytest.raises(ParseError) as excinfo:
        tokenize_json("")  # type: ignore
    assert excinfo.value.text == 'No content.'
    assert excinfo.value.code == 'no_content'
    assert excinfo.value.position.column_no == 1
    assert excinfo.value.position.line_no == 1
    assert excinfo.value.position.char_index == 0

    # String case. String tokens are offset by one position to the right,
    # so the first char in the string is at position 2.
    assert tokenize_json('"foo"') == ScalarToken('foo', 1, 4, '"foo"')

    # True case
    assert tokenize_json("true") == ScalarToken(True, 1, 4, "true")



# Generated at 2022-06-14 14:47:23.644648
# Unit test for function tokenize_json
def test_tokenize_json():
    test_json = '{"key": "value"}'
    token = tokenize_json(test_json)
    assert isinstance(token, Token)
    assert token.token_type == "dict"
    assert token.children[0].token_type == "scalar"
    assert token.children[1].token_type == "scalar"
    assert token.children[0].value == "key"
    assert token.children[1].value == "value"


# Generated at 2022-06-14 14:47:29.241026
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("{}")
    assert type(token) == DictToken
    token = tokenize_json("{}")
    assert type(token) == DictToken
    token = tokenize_json("{}")
    assert type(token) == DictToken
    token = tokenize_json("{}")
    assert type(token) == DictToken
    token = tokenize_json("{}")
    assert type(token) == DictToken
    token = tokenize_json("{}")
    assert type(token) == DictToken
    token = tokenize_json("{}")
    assert type(token) == DictToken



# Generated at 2022-06-14 14:47:40.962712
# Unit test for function tokenize_json
def test_tokenize_json():

    # Testing empty string case
    with pytest.raises(ParseError):
        tokenize_json("")

    # Testing invalid JSON string
    with pytest.raises(ParseError):
        tokenize_json('{"name": "Test"} }')

    # Testing invalid JSON string
    with pytest.raises(ParseError):
        tokenize_json('{"name": "Test" }')

    # Testing valid JSON string
    token = tokenize_json('{"name": "Test"}')
    assert isinstance(token, Token)

    # Testing valid JSON string with multiple word strings
    token = tokenize_json('{"name": "Test Test"}')
    assert isinstance(token, Token)

    # Testing valid JSON string with numbers
    token = tokenize_json('{"age": 25}')

# Generated at 2022-06-14 14:47:44.088517
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"foo":"bar"}')
    assert isinstance(token, DictToken)
    assert token.as_python() == {"foo": "bar"}



# Generated at 2022-06-14 14:47:50.025720
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string="""{
        "name": "John",
        "age": 30,
        "cars": [
            {"name": "Toyota", "models": ["Corolla", "Highlander"]},
            {"name": "Honda", "models": ["Accord", "Civic"]}
        ]
    }"""
    token=tokenize_json(json_string)
    assert token.get_value()=={
    "name": "John",
    "age": 30,
    "cars": [
        {"name": "Toyota", "models": ["Corolla", "Highlander"]},
        {"name": "Honda", "models": ["Accord", "Civic"]}
    ]
    }
    assert token.get_children()[0].get_value()=="name"
    assert token.get_children()

# Generated at 2022-06-14 14:47:52.307489
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{}') == DictToken(value={}, start=0, end=1, content='{}')


# Generated at 2022-06-14 14:48:03.833707
# Unit test for function tokenize_json
def test_tokenize_json():
    json_input = """
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": 42,
        "address": {
            "city": "Chicago",
            "state": "Illinois"
        },
        "phone_numbers": [
            {
                "type": "work",
                "number": "555-1212"
            },
            {
                "type": "home",
                "number": "555-1234"
            }
        ]
    }
    """

# Generated at 2022-06-14 14:48:06.467357
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": 1, "b": 2, "c": 3}')
    assert isinstance(token, Token)


# Generated at 2022-06-14 14:48:28.458148
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.testing_utils import assert_tokens_equal, get_token

    assert_tokens_equal(
        get_token("null"),
        get_token("""{"foo": null}"""),
    )
    assert_tokens_equal(
        get_token("1"),
        get_token("""{"foo": 1}"""),
    )
    assert_tokens_equal(
        get_token("0"),
        get_token("""{"foo": 0}"""),
    )
    assert_tokens_equal(
        get_token("true"),
        get_token("""{"foo": true}"""),
    )
    assert_tokens_equal(
        get_token("false"),
        get_token("""{"foo": false}"""),
    )


# Generated at 2022-06-14 14:48:39.134014
# Unit test for function tokenize_json
def test_tokenize_json():
    # test no content
    content = "  "
    with pytest.raises(ParseError):
        tokenize_json(content)

    # test null
    content = "null"
    token = tokenize_json(content)
    assert token.value == None

    # test true
    content = "true"
    token = tokenize_json(content)
    assert token.value is True

    # test false
    content = "false"
    token = tokenize_json(content)
    assert token.value is False

    # test empty string
    content = "\"\""
    token = tokenize_json(content)
    assert token.value == ""

    # test string
    content = "\"initial\""
    token = tokenize_json(content)
    assert token.value == "initial"

    # test

# Generated at 2022-06-14 14:48:46.697831
# Unit test for function tokenize_json
def test_tokenize_json():
    #tests for tokenizing json
    str1 = '''
    {
    "a": [{"b": 1}, {"b": 2}],
    "c": {"a": "b"},
    "d": {"a": "b"},
    "e": {"a": [{"b": 1}]}
    }
    '''
    assert tokenize_json(str1) == {
        'a': [{'b': 1}, {'b': 2}],
        'c': {'a': 'b'},
        'd': {'a': 'b'},
        'e': {'a': [{'b': 1}]}
    }


# Generated at 2022-06-14 14:48:59.023912
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:49:06.808948
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{\"age\": 29}"

    expected_token = DictToken(
        {
            ScalarToken("age", 1, 4, content): ScalarToken(
                "29",
                8,
                9,
                content,
            ),
        },
        0,
        10,
        content,
    )

    assert tokenize_json(content) == expected_token

    content = "[1, 2, 3]"

    expected_token = ListToken(
        [
            ScalarToken(1, 1, 1, content),
            ScalarToken(2, 3, 3, content),
            ScalarToken(3, 5, 5, content),
        ],
        0,
        7,
        content,
    )

    assert tokenize_json(content) == expected_token



# Generated at 2022-06-14 14:49:18.860581
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test tokenize_json with a valid json
    token = tokenize_json('{"a": "something", "b": 2}')
    assert type(token) == DictToken
    assert token.to_python() == {"a": "something", "b": 2}
    assert token.start == 0
    assert token.end == 25
    # Test tokenize_json with a valid json
    token = tokenize_json('[{"a": "something", "b": 2}, {"b": "something else", "c": false}]')
    assert type(token) == ListToken
    assert token.to_python() == [{"a": "something", "b": 2}, {"b": "something else", "c": False}]
    assert token.start == 0
    assert token.end == 83
    # Test tokenize_json with a valid

# Generated at 2022-06-14 14:49:20.271103
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": "b"}')
    assert token.contents["a"] == ScalarToken("b", 4, 6, '{"a": "b"}')


# Generated at 2022-06-14 14:49:31.988370
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"game": "football"}'
    token = tokenize_json(content)
    assert token
    assert token.type == DictToken
    assert token.value == {'game': 'football'}
    assert token.start_pos == 0
    assert token.end_pos == 21
    assert token.content == content

    content = '{"game": "football", "season" : "summer"}'
    token = tokenize_json(content)
    assert token
    assert token.type == DictToken
    assert token.value == {'game': 'football', 'season': 'summer'}
    assert token.start_pos == 0
    assert token.end_pos == 41
    assert token.content == content

    content = '["team1", "team2", "team3"]'
    token = tokenize_

# Generated at 2022-06-14 14:49:43.091104
# Unit test for function tokenize_json
def test_tokenize_json():
    from pprint import pprint
    from zencore.core.core_utils import pformat_attr
    from zencore.core.core_utils import pformat_attr_excel
    from zencore.core.core_utils import pformat_attr_excel_schema
    from zencore.core.core_utils import pformat_attr_excel_schema_json
    from zencore.core.core_utils import pformat_attr_excel_schema_yaml
    from zencore.core.core_utils import pformat_attr_json
    from zencore.core.core_utils import pformat_attr_yaml
    from zencore.core.core_utils import pformat_attr_excel_json
    from zencore.core.core_utils import pformat_attr_excel

# Generated at 2022-06-14 14:49:48.605821
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json('42') == ScalarToken(42, 0, 1, '42')
    assert tokenize_json('[1, 2, 3]') == ListToken([1, 2, 3], 0, 8, '[1, 2, 3]')
    assert tokenize_json('{"foo": 42, "bar": 43}') == DictToken({"foo": 42, "bar": 43}, 0, 18, '{"foo": 42, "bar": 43}')
    try:
        tokenize_json('42"')
    except ParseError as exc:
        assert str(exc) == "Unexpected character (position 43): error 'Unexpected character' at column 4"
        assert exc.code == 'parse_error'

# Generated at 2022-06-14 14:50:01.425174
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.parser import parse_json
    from typesystem.tokenize.tokens import DictToken, ListToken
    json_string = """{
        "input_string": "foo",
        "input_map": {
            "bar": ["baz", 123],
            "age": "",
            "unexpected": {
                "a": 1,
                "b": 2,
                "c": 3
            }
        },
        "input_bool": true,
        "input_int": 1234,
        "input_float": 1.2345
    }"""

    token = tokenize_json(json_string)
    assert isinstance(token, DictToken)

# Generated at 2022-06-14 14:50:11.524815
# Unit test for function tokenize_json
def test_tokenize_json():
    json_str = '''
    {
        "name": "Ericsson RBS6000",
        "items": [
            {
                "name": "Cell 1"
            },
            {
                "name": "Cell 2"
            }
        ]
    }
    '''

    # Create a decoder and call it
    decoder = _TokenizingDecoder(content=json_str)
    res = decoder.decode(json_str)
    print("Result:", res)
    for key in res:
        value = res[key]
        print("Key:", key, "\n", "Value:", value)



# Generated at 2022-06-14 14:50:14.997802
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[1,2,3]") == ListToken([1, 2, 3], 0, 8, "[1,2,3]")



# Generated at 2022-06-14 14:50:19.767432
# Unit test for function tokenize_json
def test_tokenize_json():
    test_json = '''{
        "a": "1",
        "b": "2",
        "c": [
            {"a": "1"},
            {"b": "2"}
        ]
    }'''
    result = tokenize_json(test_json)
    print (result)


# Generated at 2022-06-14 14:50:29.058178
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:50:40.426332
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:50:50.943313
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class Product(Schema):
        name = String()
        price = String()

    json_data = {"name": "foo", "price": "100"}
    json_content = json.dumps(json_data)
    json_token = tokenize_json(json_content)

    assert(json_token.as_dict == json_data)

    message_list = validate_with_positions(token=json_token, validator=Product)
    # The tokenizer should not create any validation errors
    assert(len(message_list) == 0)



# Generated at 2022-06-14 14:51:02.520535
# Unit test for function tokenize_json
def test_tokenize_json():
    input_dict = {
        "a": [1],
        "b": [2, 3],
        "c": {1: "a", "2": "d"},
        "d": [{"a": 1, "b": "c"}],
        "e": "abcd",
        "f": None,
        "g": True,
        "h": False,
        # "i": "\\",
        # "j": "\"",
        "k": 1,
        "l": 1.0,
        "m": "1.0",
        "n": 1.0e10,
    }
    json_string = json.dumps(input_dict, sort_keys=True)
    json_dict = json.loads(json_string)
    token = tokenize_json(json_string)
    assert type

# Generated at 2022-06-14 14:51:09.412864
# Unit test for function tokenize_json
def test_tokenize_json():
    def validate_token(token: Token, expected_value: int) -> bool:
        return isinstance(token, DictToken) and token.value == expected_value

    test_content = '{"hello": "world"}'
    token = tokenize_json(test_content)
    assert validate_token(token, {"hello": "world"})



# Generated at 2022-06-14 14:51:12.626720
# Unit test for function tokenize_json
def test_tokenize_json():
    json_str = '{"key":"value"}'
    token = tokenize_json(json_str)
    assert isinstance(token, DictToken)
    assert token.value == {"key": "value"}


# Generated at 2022-06-14 14:51:17.869538
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"name": "Alex"}') == {'name': 'Alex'}



# Generated at 2022-06-14 14:51:29.216540
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem import fields
    import json
    import time
    import random

    # generate 10,000 random JSON documents
    # each JSON document is a list of random length
    # each item in the list is a dict of random length
    # with random keys and random values
    # keys and values are only strings

    def rand_char():
        return chr(random.randint(ord("a"), ord("z")))

    def rand_str(maxlen):
        s = [rand_char() for _ in range(random.randint(1, maxlen))]
        return "".join(s)

    def rand_dict():
        keys = [rand_str(10) for _ in range(random.randint(1, 15))]

# Generated at 2022-06-14 14:51:36.353468
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """{
      "foo": 1,
      "bar": "baz",
      "bam": [1, 2, 3],
      "baz": {"foo": true}
    }"""
    token = tokenize_json(content)
    assert token.as_dict() == {
        "foo": 1,
        "bar": "baz",
        "bam": [1, 2, 3],
        "baz": {"foo": True},
    }



# Generated at 2022-06-14 14:51:43.729373
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a": 1, "b": 2}') == DictToken({'a': 1, 'b': 2}, 0, 15, '{"a": 1, "b": 2}')
    assert tokenize_json('["a", "b"]') == ListToken(['a', 'b'], 0, 8, '["a", "b"]')
    assert tokenize_json('') == ScalarToken(None, 0, 0, '')
    assert type(tokenize_json('')) == ScalarToken


# Generated at 2022-06-14 14:51:55.422044
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:51:57.665830
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('[{"field": "value"}]')
    assert isinstance(token, ListToken)



# Generated at 2022-06-14 14:52:01.743396
# Unit test for function tokenize_json
def test_tokenize_json():
    test_json = '{"bar": 1, "foo": [{"a": 1}, {"b": 2}, {"c": 3}]}'
    token = tokenize_json(test_json)
    result = token.to_python()
    assert result == {'bar': 1, 'foo': [{'a': 1}, {'b': 2}, {'c': 3}]}


# Generated at 2022-06-14 14:52:13.893591
# Unit test for function tokenize_json
def test_tokenize_json():
    valid_json = '{"title": "Example Schema", "type": "object", "properties": {"firstName": {"type": "string"}, "lastName": {"type": "string"}, "age": {"description": "Age in years", "type": "integer", "minimum": 0}}, "required": ["firstName", "lastName"]}'
    token = tokenize_json(valid_json)
    assert token['type'] == 'object'
    assert token['title'] == 'Example Schema'
    assert token['properties']['firstName']['type'] == 'string'
    assert token['properties']['lastName']['type'] == 'string'
    assert token['properties']['age']['type'] == 'integer'
    assert token['properties']['age']['description'] == 'Age in years'

# Generated at 2022-06-14 14:52:16.560077
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("[1,2,3]") == ListToken([1, 2, 3], 0, 7, "[1,2,3]")


# Generated at 2022-06-14 14:52:24.050415
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken([], 0, 1, content='{}') # noqa: E501
    assert tokenize_json('{"a": 1}') == DictToken([(ScalarToken('a', 1, 2, content='{"a": 1}'), ScalarToken(1, 6, 6, content='{"a": 1}'))], 0, 9, content='{"a": 1}') # noqa: E501
    assert tokenize_json('{"hello": "world"}') == DictToken([(ScalarToken('hello', 1, 6, content='{"hello": "world"}'), ScalarToken('world', 11, 16, content='{"hello": "world"}'))], 0, 17, content='{"hello": "world"}') # noqa: E501

# Generated at 2022-06-14 14:52:34.640883
# Unit test for function tokenize_json
def test_tokenize_json():
    json_text = """{
"foo": 1,
"bar": "baz",
"fizz": [
    "buzz",
    "fizzbuzz"
    ],
"nested": {
    "hello": "world"
    }
}"""
    message: Message = tokenize_json(json_text)
    assert message.foo == 1
    assert message.bar == "baz"
    assert message.fizz == ["buzz", "fizzbuzz"]
    assert message.nested.hello == "world"

# Generated at 2022-06-14 14:52:44.905212
# Unit test for function tokenize_json
def test_tokenize_json():
    # Pass
    token = tokenize_json("4")
    assert isinstance(token, ScalarToken)
    assert token.value == 4
    # Pass
    token = tokenize_json("[1, 2, 3]")
    assert isinstance(token, ListToken)
    assert len(token.value) == 3
    assert isinstance(token.value[0], ScalarToken)
    # Pass
    token = tokenize_json('{"name": "Sharon"}')
    assert isinstance(token, DictToken)
    assert isinstance(token.value["name"], ScalarToken)
    # Fail
    try:
        tokenize_json('{"name": "Sharon"')
    except ParseError as e:
        assert e.position.line_no == 1
        assert e.position.column_no == 18


# Generated at 2022-06-14 14:52:55.968947
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == None
    assert tokenize_json("{}") == DictToken(value={}, start=0, end=1, content="{}")
    assert tokenize_json("{\"test\": 1}") == DictToken(value={ ScalarToken("test",1,5, content="{\"test\": 1}") : ScalarToken(1,9,9, content="{\"test\": 1}") }, start=0, end=12, content="{\"test\": 1}")

# Generated at 2022-06-14 14:53:04.665110
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test function tokenize_json().
    """
    s = "   [true, false, \"a\", \"b\", {\"c\": 1}, [\"f\"], []]"
    expected = [
        ScalarToken(True, 4, 7, s),
        ScalarToken(False, 9, 14, s),
        ScalarToken("a", 16, 18, s),
        ScalarToken("b", 20, 22, s),
        DictToken({"c": 1}, 24, 30, s),
        ListToken([ScalarToken("f", 33, 35, s)], 32, 36, s),
        ListToken([], 38, 39, s),
    ]

    result = tokenize_json(s)
    assert isinstance(result, ListToken)
    assert len(result) == len(expected)
   

# Generated at 2022-06-14 14:53:14.266114
# Unit test for function tokenize_json
def test_tokenize_json():
    content = b'{"foo": "bar"}'
    token = tokenize_json(content)
    expected = DictToken(
        value={
            ScalarToken(value="foo", position=1, end_position=11, content=content): ScalarToken(
                value="bar", position=14, end_position=22, content=content
            )
        },
        position=0,
        end_position=23,
        content=content,
    )
    assert token == expected

    content = b'{"foo": "bar", "baz": "quux"}'
    token = tokenize_json(content)

# Generated at 2022-06-14 14:53:15.993627
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Paul"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value == {"name": "Paul"}



# Generated at 2022-06-14 14:53:21.289555
# Unit test for function tokenize_json
def test_tokenize_json():
  token_content = tokenize_json('{ "name":"John", "age":30, "cars": [ "Ford", "BMW", "Fiat" ] }')
  assert(isinstance(token_content, DictToken))
  assert(isinstance(token_content, Token))
  assert(isinstance(token_content._value, dict))

  token_content_none = tokenize_json('{ }')
  assert(isinstance(token_content_none, DictToken))
  assert(isinstance(token_content_none, Token))
  assert(isinstance(token_content_none._value, dict))

  token_content_empty = tokenize_json('[ ]')
  assert(isinstance(token_content_empty, ListToken))
  assert(isinstance(token_content_empty, Token))

# Generated at 2022-06-14 14:53:32.652037
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"key": "value"}') == {
        "key": "value"
    }
    assert tokenize_json('{"key": "value", "key2": 123, "key3":true, "key4":false, "key5":null}') == {
        "key": "value",
        "key2": 123,
        "key3": True,
        "key4": False,
        "key5": None
    }
    assert tokenize_json('[{"key": "value"}]') == [{"key": "value"}]
    assert tokenize_json('{"key": 123}') == {"key": 123}
    assert tokenize_json('{"key": 123.5}') == {"key": 123.5}

# Generated at 2022-06-14 14:53:41.569694
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    import textwrap
    from collections import OrderedDict

    # Function tokenize_json should correctly tokenize the input json
    # string and returns a Token object.
    content = textwrap.dedent("""\
    {"foo": "bar", "bar": [{"egg": "spam"}, {"foo": "bar"}]}
    """)
    expected = json.loads(
        content,
        object_pairs_hook=OrderedDict,
    )
    token = tokenize_json(content)
    assert token.kind == "dict"
    assert token.value == expected

    # Function tokenize_json should correctly tokenize the input json
    # string and returns a Token object when the json string is empty.
    token = tokenize_json("")
    assert token is None

    # Function tokenize_json should raise

# Generated at 2022-06-14 14:53:47.243767
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("null")
    assert token
    token = tokenize_json("\"test\"")
    assert token
    token = tokenize_json("[1,2,3]")
    assert token
    token = tokenize_json("{\"key\": \"value\"}")
    assert token

# Generated at 2022-06-14 14:54:01.532483
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:54:12.954528
# Unit test for function tokenize_json
def test_tokenize_json():
    obj = tokenize_json(
        """
    {
        "foo": [{"bar": [1,2, 3.14e10, true, false, null]}],
        "baz": "qux"
    }"""
    )
    assert isinstance(obj, DictToken)
    assert len(obj) == 2
    assert obj[0][0].value == "foo"

    assert isinstance(obj[0][1], ListToken)
    assert len(obj[0][1]) == 1

    assert isinstance(obj[0][1][0], DictToken)
    assert len(obj[0][1][0]) == 1
    assert obj[0][1][0][0][0].value == "bar"

    assert isinstance(obj[0][1][0][0][1], ListToken)
    assert len

# Generated at 2022-06-14 14:54:20.065446
# Unit test for function tokenize_json
def test_tokenize_json():

    content = '''
    {
      "name": "Arun",
      "age": 25,
      "nested": {
        "occupation": "software developer",
        "office address": {
          "city": "San Francisco",
          "state": "CA",
          "zipcode": 94107
        }
      }
    }
    '''

    token = tokenize_json(content)

    assert isinstance(token, DictToken)
    assert len(token.keys) == 3
    assert token.keys[0].value == "name"
    assert token.keys[1].value == "age"
    assert token.keys[2].value == "nested"
    assert isinstance(token.values[0], ScalarToken)
    assert isinstance(token.values[1], ScalarToken)

# Generated at 2022-06-14 14:54:29.208745
# Unit test for function tokenize_json
def test_tokenize_json():
    source = '{"int": 1, "float": 1.23, "array": [1,2,3], "object": {"a": 1, "b": "two"}, "null": null, "true": true, "false": false}'
    expected = {
        'int': 1,
        'float': 1.23,
        'array': [1, 2, 3],
        'object': {
            'a': 1,
            'b': "two"
        },
        'null': None,
        'true': True,
        'false': False
    }
    token = tokenize_json(source)
    assert token.value == expected


# Generated at 2022-06-14 14:54:38.559075
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test for empty input
    content = ""
    try:
        token = tokenize_json(content)
    except ParseError as exc:
        assert exc.code == "no_content"
        assert exc.text == "No content."
        assert exc.position == Position(column_no=1, line_no=1, char_index=0)
    else:
        assert False

    # Test for unexpected ending
    content = '{"key1": "value1", "key2": "value2"}{"key3": "value3"}'
    try:
        token = tokenize_json(content)
    except ParseError as exc:
        assert exc.code == "parse_error"
        assert exc.text == "Expecting value"

# Generated at 2022-06-14 14:54:46.316593
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('') == ''
    assert tokenize_json(b'') == ''

    assert tokenize_json(b'{}') == {}
    assert tokenize_json('{}') == {}

    assert tokenize_json(b'{"a": 1}') == {'a': 1}
    assert tokenize_json('{"a": 1}') == {'a': 1}

    assert tokenize_json(b'{"a": {"b": [1, 2, 3]}}') == {'a': {'b': [1, 2, 3]}}
    assert tokenize_json('{"a": {"b": [1, 2, 3]}}') == {'a': {'b': [1, 2, 3]}}


# Generated at 2022-06-14 14:54:48.962011
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo":[1,2,3]}'
    token = tokenize_json(content)
    assert token.value == {"foo": [1, 2, 3]}

# Generated at 2022-06-14 14:54:55.988291
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": 1, "b": 2, "c": "hello"}'
    expected = DictToken(
        {ScalarToken('a', 1, 2, content): ScalarToken(1, 6, 6, content), 
        ScalarToken('b', 13, 13, content): ScalarToken(2, 17, 17, content), 
        ScalarToken('c', 24, 24, content): ScalarToken('hello', 28, 32, content)
        },
        0,
        34,
        content
    )
    token = tokenize_json(content)
    assert token == expected


# Generated at 2022-06-14 14:54:58.682250
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": 1}')
    assert type(token) == DictToken
    assert token.value == {ScalarToken('a', 1, 2, '{"a": 1}'): ScalarToken(1, 6, 7, '{"a": 1}')}

# Generated at 2022-06-14 14:55:01.742997
# Unit test for function tokenize_json
def test_tokenize_json():
    # Arrange
    content = '{"key1":"value1", "key2":"value2"}'

    # Act
    token = tokenize_json(content)
    token_value = token.value

    # Assert
    assert isinstance(token, DictToken)
    assert token_value["key1"].value == "value1"
    assert token_value["key2"].value == "value2"



# Generated at 2022-06-14 14:55:16.406695
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Simple formatting test for function `tokenize_json`.
    """
    assert tokenize_json("") == ListToken([], 0, 0, "")
    assert tokenize_json("[1, 2, 3]") == ListToken([1, 2, 3], 0, 10, "[1, 2, 3]")
    assert tokenize_json("[1, 2, 3,]") == ListToken([1, 2, 3], 0, 11, "[1, 2, 3,]")
    assert tokenize_json("[1, 2, ,3,]") == ListToken([1, 2, None, 3], 0, 13, "[1, 2, ,3,]")
    assert tokenize_json("[]") == ListToken([], 0, 2, "[]")