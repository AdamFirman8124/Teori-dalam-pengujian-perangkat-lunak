

# Generated at 2022-06-14 14:45:49.888025
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json('"test"') == ScalarToken("test", 0, 5, '"test"')
    assert tokenize_json("{}") == tokenize_json("\n{}\n")
    assert tokenize_json('{"foo": "bar"}') == DictToken(
        {"foo": ScalarToken("bar", 10, 15, '{"foo": "bar"}')}, 0, 16, '{"foo": "bar"}'
    )
    assert tokenize_json("null") == ScalarToken(None, 0, 4, "null")

# Generated at 2022-06-14 14:45:51.908475
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"firstName": "john", "lastName": "doe"}') == {'firstName': 'john', 'lastName': 'doe'}


# Generated at 2022-06-14 14:45:56.643909
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"name":"test","age":28}') == {
        "name": ScalarToken("test", 2, 11, '{"name":"test","age":28}'),
        "age": ScalarToken(28, 18, 21, '{"name":"test","age":28}'),
    }
    assert tokenize_json('[3,7]') == [
        ScalarToken(3, 1, 2, '[3,7]'),
        ScalarToken(7, 4, 5, '[3,7]'),
    ]

# Generated at 2022-06-14 14:46:03.893769
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "numbers": [1, 2, -3],
        "bools": [true, false],
        "null": null,
        "nested": {
            "string": "Hello world",
            "string_escapes": "\\"Wow\\"",
            "unicode": "\\u00fc",
            "int": 123,
            "float": 123.45,
            "exp": 1.23e+10
        }
    }
    """
    token = tokenize_json(content)

# Generated at 2022-06-14 14:46:07.386566
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": 123.0, "age": 18}'  # type: str
    token = tokenize_json(content)    
    assert isinstance(token, DictToken)
    assert len(token.value) == 2

# Generated at 2022-06-14 14:46:12.110489
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": "b"}'
    expected = Token("a", "b")  
    #
    got = tokenize_json(content)
    assert str(got) == str(expected)
    #
    content = "{'a': 'b'}"
    expected = Token("a", "b")  
    #
    got = tokenize_json(content)
    assert str(got) == str(expected)

# Generated at 2022-06-14 14:46:20.423972
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"key": "value"}'
    token = tokenize_json(content)
    assert token.__class__.__name__ == 'DictToken'
    assert token.key_value_pairs[0][0].__class__.__name__ == 'ScalarToken'
    assert token.key_value_pairs[0][0].value == 'key'
    assert token.key_value_pairs[0][1].__class__.__name__ == 'ScalarToken'
    assert token.key_value_pairs[0][1].value == 'value'


# Generated at 2022-06-14 14:46:26.268197
# Unit test for function tokenize_json
def test_tokenize_json():
    test_cases = [
        ('{"b": 1}', DictToken({"b": ScalarToken(1)})),
        ('{"b": ["a", 2, {"a": "hello"}]}', DictToken({"b": ListToken(["a", ScalarToken(2), DictToken({"a": "hello"})])})),
    ]

    for test_case, expected in test_cases:
        result = tokenize_json(test_case)
        assert result == expected

# Generated at 2022-06-14 14:46:37.478904
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{}') == {}
    assert tokenize_json(b'{"foo": "bar"}') == {"foo": "bar"}
    assert tokenize_json(b'{"foo": "bar", "baz": true}') == {"foo": "bar", "baz": True}
    assert tokenize_json(b'[1,2,3,4]') == [1, 2, 3, 4]

    with pytest.raises(ParseError) as exc:
        tokenize_json(b'')
    assert exc.value.position == Position(column_no=1, char_index=0, line_no=1)
    assert exc.value.text == "No content."
    assert exc.value.code == "no_content"


# Generated at 2022-06-14 14:46:41.948785
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name":"jose","shoes":null}'
    token = tokenize_json(content)
    assert token.type == "dict"
    assert token.value == {"name": "jose", "shoes": None}
    assert not token.has_errors()
    

# Unit tests for function validate_json

# Generated at 2022-06-14 14:46:59.628473
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json("{}"), DictToken)
    assert isinstance(tokenize_json("[]"), ListToken)
    assert isinstance(tokenize_json("null"), ScalarToken)
    assert isinstance(tokenize_json("true"), ScalarToken)
    assert isinstance(tokenize_json("false"), ScalarToken)
    assert isinstance(tokenize_json("1"), ScalarToken)
    assert isinstance(tokenize_json("1.1"), ScalarToken)
    assert isinstance(tokenize_json("1e2"), ScalarToken)
    assert isinstance(tokenize_json('"asdf"'), ScalarToken)
    assert isinstance(tokenize_json("  \n \t{}"), DictToken)

# Generated at 2022-06-14 14:47:09.792972
# Unit test for function tokenize_json
def test_tokenize_json():
    text = """
    {
      "name": "Django REST framework",
      "url": "http://www.django-rest-framework.org/",
      "a": [1, 2, 3],
      "b": {
        "c": {
          "d": "two"
        }
      },
      "license": "BSD",
      "author": "Tom Christie"
    }
    """
    json_data = tokenize_json(text)
    assert isinstance(json_data, DictToken)
    assert json_data.value['a'] == [1, 2, 3]
    assert json_data.value['b'] == {'c': {'d': 'two'}}


# Generated at 2022-06-14 14:47:16.872851
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tokens import Token
    from typesystem.exceptions import ValidationError
    from typesystem import Boolean, Integer, PositiveInteger, String, Array, Object

    simple_json = b'{"foo": "bar", "name": "typesystem", "enabled": true}'
    complex_json = (
        b'{"foo": 1, "bar": "baz", "nested": {"foo": "bar", "name": "typesystem", "enabled": true, "list": [1, 2, 3]}}'
    )

    class Device(Schema):
        name = String()
        type = String()

    class Data(Schema):
        device = Device()
        data = Object(properties={"value": PositiveInteger()})

    class Message(Schema):
        timestamp = Integer()

# Generated at 2022-06-14 14:47:21.261601
# Unit test for function tokenize_json
def test_tokenize_json():
    data = '{"a": 1, "b": "string"}'
    output = {'a': ScalarToken(1, 2, 3, data), 'b': ScalarToken('string', 10, 16, data)}
    assert tokenize_json(data) == output

# Generated at 2022-06-14 14:47:29.798513
# Unit test for function tokenize_json
def test_tokenize_json():
    # Create a json file
    with open("./test.json", "w+") as write_file:
        json.dump({"name": "Bob", "languages": ["Python", "Java"]}, write_file)

    # Open the file and get its content
    with open("./test.json", "r") as read_file:
        content = read_file.read()
    
    token = tokenize_json(content)

    # Test the cases of content as str or bytes
    assert(isinstance(tokenize_json(b'{"foo" : "bar"}'), DictToken))
    assert(isinstance(tokenize_json('{"foo" : "bar"}'), DictToken))


# Generated at 2022-06-14 14:47:41.428177
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "[1, 2, 3]"
    token = tokenize_json(content)
    assert token.value == [1, 2, 3]
    assert token.start_position.line_no == 1
    assert token.start_position.column_no == 1
    assert token.start_position.char_index == 0

    assert token.end_position.line_no == 1
    assert token.end_position.column_no == 8
    assert token.end_position.char_index == 7

    content = "[]"
    token = tokenize_json(content)
    assert token.value == []
    assert token.start_position.line_no == 1
    assert token.start_position.column_no == 1
    assert token.start_position.char_index == 0


# Generated at 2022-06-14 14:47:53.566285
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:48:05.840033
# Unit test for function tokenize_json
def test_tokenize_json():
    from typing import Dict, List

    from typesystem.fields import Integer, Map, Text, Dict, List
    from typesystem.types import Record, RecordType
    from typesystem.types import Array
    from typesystem.tokenize.tokens import ScalarToken, ListToken, DictToken
    
    assert tokenize_json("") == {}
    assert tokenize_json("null: null") == {}
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("hello") == ScalarToken("hello", 0, 4, "hello")

# Generated at 2022-06-14 14:48:18.211276
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == None
    assert tokenize_json(" ") == None
    assert tokenize_json("[") == None
    assert tokenize_json("]") == None
    assert tokenize_json("{") == None
    assert tokenize_json("}") == None
    assert tokenize_json(None) == None
    assert tokenize_json(0) == None
    assert tokenize_json(b"") == None
    assert tokenize_json(b" ") == None
    assert tokenize_json(b"[") == None
    assert tokenize_json(b"]") == None
    assert tokenize_json(b"{") == None
    assert tokenize_json(b"}") == None

    assert isinstance(tokenize_json("{}"), DictToken)

# Generated at 2022-06-14 14:48:28.001678
# Unit test for function tokenize_json
def test_tokenize_json():
    # Empty string
    with pytest.raises(ValueError):
        tokenize_json("")
    # Unexpected character
    with pytest.raises(ValueError):
        tokenize_json("{")
    # End of input
    with pytest.raises(ValueError):
        tokenize_json("true")
    # Trailing comma
    with pytest.raises(ValueError):
        tokenize_json('{"a": 1,}')
    # Trailing commas
    with pytest.raises(ValueError):
        tokenize_json('[1, 2, 3,]')
    # Leading comma
    with pytest.raises(ValueError):
        tokenize_json('{, "a": 1}')


# Generated at 2022-06-14 14:48:45.131702
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test empty string case
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("")

    assert exc_info.match("No content\.")

    # Test basic decoding
    token = tokenize_json(r'{"a": "b", "c": 1, "d": {"e": ["f", 2]}}')
    assert type(token) is DictToken

# Generated at 2022-06-14 14:48:57.535178
# Unit test for function tokenize_json
def test_tokenize_json():
    # Tests for tokenize_json function

    # Test for an empty string
    try:
        tokenize_json("")
    except ParseError:
        pass
    else:
        raise AssertionError("ParseError not caught")

    # Test for an invalid JSON string
    try:
        tokenize_json('{"a": [ true, false, null }')
    except ParseError:
        pass
    else:
        raise AssertionError("ParseError not caught")

    # Test for valid JSON string

# Generated at 2022-06-14 14:49:03.962826
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == {}, tokenize_json("")
    assert tokenize_json('{"a":1}') == {"a": 1}, tokenize_json('{"a":1}')
    assert tokenize_json('{"a":[1,2]}') == {"a": [1, 2]}, tokenize_json('{"a":[1,2]}')
    assert (
        tokenize_json('{"a":1, "b":2}') == {"a": 1, "b": 2}, tokenize_json('{"a":1, "b":2}')
    )



# Generated at 2022-06-14 14:49:08.345300
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": "1"}'
    token = tokenize_json(content)
    assert type(token) is DictToken
    assert len(token.value) == 1
    assert token.value["a"].value == "1"
    assert token.value["a"].line_no == 1
    assert token.value["a"].column_no == 6
    assert token.value["a"].char_index == 5



# Generated at 2022-06-14 14:49:11.491818
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a":1,"b":2}')
    assert order_insensitive_string_equality(token.to_native(), {'a': 1, 'b': 2})


# Generated at 2022-06-14 14:49:23.906289
# Unit test for function tokenize_json
def test_tokenize_json():
    validator = Field(type="string")
    tokenized_obj = tokenize_json("{\"foo\":\"bar\"}")
    assert isinstance(tokenized_obj, DictToken)
    value, error_messages = validate_with_positions(
        token=tokenized_obj, validator=validator
    )
    assert value == {"foo": "bar"}
    assert error_messages == []

    text_input = '{"foo":33}'
    tokenized_obj = tokenize_json(text_input)
    value, errors = validate_json(text_input, validator)
    assert value == {"foo": "33"}
    assert errors[0].text == "Must be of type 'string'."
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no

# Generated at 2022-06-14 14:49:26.240490
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(u'{"name": "Tom"}')
    assert isinstance(token, DictToken)



# Generated at 2022-06-14 14:49:36.129343
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:49:45.487040
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"foo": "bar"}') == \
        DictToken({ScalarToken('foo', 1, 5, '{"foo": "bar"}'): ScalarToken('bar', 9, 14, '{"foo": "bar"}')},0, 15, '{"foo": "bar"}')
    assert tokenize_json('["foo", "bar"]') == \
        ListToken([ScalarToken('foo', 2, 6, '["foo", "bar"]'), ScalarToken('bar', 10, 15, '["foo", "bar"]')], 0, 16, '["foo", "bar"]')

# Generated at 2022-06-14 14:49:49.232073
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{'a': 'b', 'c': 'd'}"
    expected = {'a': 'b', 'c': 'd'}
    assert tokenize_json(content) == expected


# Generated at 2022-06-14 14:50:02.566695
# Unit test for function tokenize_json
def test_tokenize_json():  
    # Test data
    content1 = '{"a": 1, "b":2}'
    content2 = '{"a": 1, "b":[2, 3, 4]}'
    content3 = '{"a": 1, "b": {"c": 2}}'
    content4 = '{"a": 1, "b": {"c": [2, 3]}}'
    content5 = '{"a": 1, "b": {"c": [2, 3], "d": [7, 8]}}'

    # Unit test
    print("Content: {}. Expected: <DictToken with 2 key-value pairs>".format(content1))
    assert(isinstance(tokenize_json(content1), DictToken))
    assert(tokenize_json(content1).length() == 2)

# Generated at 2022-06-14 14:50:10.181660
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"field1": "2112", "field2": ["data1", "data2"]}') == DictToken({
        'field1': ScalarToken('2112'),
        'field2': ListToken(['data1', 'data2'])
    }, 0, 33, '{"field1": "2112", "field2": ["data1", "data2"]}')

if __name__ == "__main__":
    test_tokenize_json()

# Generated at 2022-06-14 14:50:18.255328
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('["foo", "bar", {"baz": 123}]')
    assert token.to_python() == ['foo', 'bar', {'baz': 123}]
    invalid_content_empty_string = ''
    with pytest.raises(ParseError, match=''):
        tokenize_json(invalid_content_empty_string)
    invalid_content_missing_quote = '{"foo": "bar'
    with pytest.raises(ParseError, match=''):
        tokenize_json(invalid_content_missing_quote)
    invalid_content_unexpected_eof = '{"foo": "bar"'
    with pytest.raises(ParseError, match=''):
        tokenize_json(invalid_content_unexpected_eof)


# Unit test

# Generated at 2022-06-14 14:50:28.162115
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test empty string.
    with pytest.raises(ParseError):
        tokenize_json("")
    # Test whitespace only string.
    with pytest.raises(ParseError):
        tokenize_json("                 ")
    # Test string with bogus data.
    with pytest.raises(ParseError):
        tokenize_json("abc")
    # Test string with JSON parse errors.
    with pytest.raises(ParseError):
        tokenize_json("{")
    with pytest.raises(ParseError):
        tokenize_json("[1,2,3")
    with pytest.raises(ParseError):
        tokenize_json("[1,2,3]xyz")

    # Test string with valid JSON.
    assert tokenize_json("{}")

# Generated at 2022-06-14 14:50:39.898905
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("null") == ScalarToken(
        value=None, start=0, end=3)
    assert tokenize_json("1") == ScalarToken(value=1, start=0, end=0)
    assert tokenize_json("1.1") == ScalarToken(
        value=1.1, start=0, end=2)
    assert tokenize_json("-1.1") == ScalarToken(
        value=-1.1, start=0, end=3)
    assert tokenize_json("-1.1e2") == ScalarToken(
        value=-1.1e2, start=0, end=5)
    assert tokenize_json("\"1.1\"") == ScalarToken(
        value="1.1", start=0, end=4)
    assert token

# Generated at 2022-06-14 14:50:50.705500
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a":1}'
    token = tokenize_json(content)
    assert token.start_pos.line_no == 1
    assert token.start_pos.column_no == 1
    assert token.end_pos.line_no == 1
    assert token.end_pos.column_no == 7

    assert isinstance(token, DictToken)
    assert len(token.items) == 1
    k, v = token.items[0]
    assert isinstance(k, ScalarToken)
    assert k.value == 'a'
    assert isinstance(v, ScalarToken)
    assert v.value == 1


# Generated at 2022-06-14 14:50:56.401610
# Unit test for function tokenize_json
def test_tokenize_json():
    json_str = '{"key": {"name":"value"}}'
    obj_dict = tokenize_json(json_str).value
    assert type(obj_dict) == dict
    assert type(obj_dict["key"]) == DictToken
    assert obj_dict["key"].value["name"].value == "value"



# Generated at 2022-06-14 14:51:02.230602
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = """{
            "key_1": [1.2, 3.4],
            "key_2": true,
            "key_3": null
        }"""
    token = tokenize_json(json_string)
    assert len(token.element) == 3
    assert "key_2" in token.element
    assert token.element["key_2"].value == True



# Generated at 2022-06-14 14:51:15.230980
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(
        b'{"child-key":{"child-array":[1,2,3],"child-dict":{"child-key":"child-val"}}'
    )
    assert token.as_dict() == {
        "child-key": {
            "child-array": [1, 2, 3],
            "child-dict": {"child-key": "child-val"},
        }
    }
    assert token.as_json() == b'{"child-key":{"child-array":[1,2,3],"child-dict":{"child-key":"child-val"}}}'

    assert token["child-key"]["child-dict"]["child-key"].value == "child-val"

# Generated at 2022-06-14 14:51:18.950782
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{\"foo\":\"bar\"}"
    result = tokenize_json(content)
    assert isinstance(result, DictToken)
    assert result.as_dict() == {"foo": "bar"}



# Generated at 2022-06-14 14:51:29.072891
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"key": [2, 3, 5]}'
    res = tokenize_json(content)
    assert isinstance(res, DictToken)
    assert isinstance(res.data, dict)
    assert isinstance(res.data["key"], ListToken)
    assert isinstance(res.data["key"].data, list)
    assert res.data["key"].data == [2, 3, 5]

# Generated at 2022-06-14 14:51:39.209144
# Unit test for function tokenize_json
def test_tokenize_json():
    class CharField(Field):
        coerce_value = str

    schema = CharField(min_length=1, max_length=10)

    # Test parse error case.
    json_1 = """
    {
      "title": "JSON Schema is awesome",
      "content": "Here's a json schema that supports comments",
      "description": "It's also a draft v4 schema",
      "asset": {
        "title": "Draft v4",
        "href": "https://json-schema.org/specification.html"
      }
    }
    #
    """
    _, errors = validate_json(json_1, schema)
    assert len(errors) == 1
    line_no, column_no = errors[0].position.line_no, errors[0].position.column_no
   

# Generated at 2022-06-14 14:51:45.158633
# Unit test for function tokenize_json
def test_tokenize_json():
    empty = '''
'''
    empty_tok = DictToken({}, 1, 1, empty)
    assert empty_tok == tokenize_json(empty)

    d = '''
{
    "a": 1,
    "b": {
        "c": 2
    },
    "d": [1, 2, 3],
    "e": ["a", "b", "c"]
}
'''

# Generated at 2022-06-14 14:51:56.629401
# Unit test for function tokenize_json
def test_tokenize_json():
    result = tokenize_json("""{
        "coffee": [
            {"name": "Lavazza", "grade": 8},
            {"name": "Moccona", "grade": 7}
        ]
    }""")
    assert result.value == {
        "coffee": [{"name": "Lavazza", "grade": 8}, {"name": "Moccona", "grade": 7}]
    }
    assert result.start == 0
    assert result.end == 199

    assert isinstance(result, DictToken)
    assert result.value == {
        "coffee": [{"name": "Lavazza", "grade": 8}, {"name": "Moccona", "grade": 7}]
    }
    assert result.start == 0
    assert result.end == 199
    assert result

# Generated at 2022-06-14 14:52:07.006526
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{ "name": "John", "age": 24, "cars": { "car1": "Ford", "car2": "BMW", "car3": "Fiat" } }'
    content_bytes = b'{ "name": "John", "age": 24, "cars": { "car1": "Ford", "car2": "BMW", "car3": "Fiat" } }'
    token = tokenize_json(content)

    assert isinstance(token, DictToken)
    assert token.value["name"].value == "John"
    assert token.value["age"].value == 24

    token_bytes = tokenize_json(content_bytes)
    assert isinstance(token_bytes, DictToken)
    assert token_bytes.value["name"].value == "John"
    assert token_bytes

# Generated at 2022-06-14 14:52:14.657607
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
        {
            "foo": "bar"
        }
    """
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value.keys() == {"foo": ScalarToken("foo", position=Position(char_index=10, column_no=4, line_no=3))}
    assert token.position == Position(char_index=0, column_no=1, line_no=2)
    assert token.end_position == Position(char_index=29, column_no=1, line_no=6)



# Generated at 2022-06-14 14:52:15.482813
# Unit test for function tokenize_json
def test_tokenize_json():
    tokenize_json("")

# Generated at 2022-06-14 14:52:25.635771
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"filter_by": []}')
    assert type(token) == DictToken
    assert token["filter_by"].type == ListToken

    token = tokenize_json('{"filter_by": ["FooBar"]}')
    assert type(token) == DictToken
    assert token["filter_by"].type == ListToken

    token = tokenize_json('{"filter_by": ["FooBar", "Foo", "bar"]}')
    assert type(token) == DictToken
    assert token["filter_by"].type == ListToken

    token = tokenize_json('{"filter_by": ["FooBar", "Foo", "bar", 8]}')
    assert type(token) == DictToken
    assert token["filter_by"].type == ListToken

    token = token

# Generated at 2022-06-14 14:52:36.576661
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"name": "fred", "age": 21}') == \
        DictToken(value={"name": "fred", "age": 21}, start_index=0, end_index=22, content='{"name": "fred", "age": 21}')

    assert tokenize_json('[{"age": 21}, {"age": 22}]') == \
        ListToken(value=[{"age": 21}, {"age": 22}], start_index=0, end_index=24, content='[{"age": 21}, {"age": 22}]')


# Generated at 2022-06-14 14:52:40.667421
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("{}")
    assert isinstance(token, DictToken)
    assert token.value == {}
    assert token.start_position == Position(1, 1, 0)
    assert token.end_position == Position(2, 1, 1)



# Generated at 2022-06-14 14:52:50.061657
# Unit test for function tokenize_json
def test_tokenize_json():
    content: str = '{"answer": 42}'
    root = tokenize_json(content=content)
    value = root.value
    assert isinstance(root, DictToken)
    assert isinstance(value, dict)
    assert len(value) == 1
    assert isinstance(value.get("answer"), ScalarToken)
    assert value.get("answer").value == 42


# Generated at 2022-06-14 14:53:00.554744
# Unit test for function tokenize_json
def test_tokenize_json():
    # no content
    token = tokenize_json('')
    assert isinstance(token, ScalarToken)

    # empty list
    token = tokenize_json('[ ]')
    assert isinstance(token, ListToken)
    assert token.value == []

    # empty dict
    token = tokenize_json('{ }')
    assert isinstance(token, DictToken)
    assert token.value == {}

    # dict
    token = tokenize_json('{ "foo": "bar" }')
    assert isinstance(token, DictToken)
    assert token.value == {"foo": "bar"}

    # list
    token = tokenize_json('[ "foo", "bar" ]')
    assert isinstance(token, ListToken)
    assert token.value == ["foo", "bar"]

    # dict in list

# Generated at 2022-06-14 14:53:04.632709
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"n": "123", "b": true, "s": "hello"}')
    assert isinstance(token, dict)
    assert token == {'n': '123', 'b': True, 's': 'hello'}



# Generated at 2022-06-14 14:53:14.237264
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == {"token": DictToken, "position": Position(1, 1, 0), "value": {}}
    assert tokenize_json("{}") == {"token": DictToken, "position": Position(1, 1, 0), "value": {}}
    assert tokenize_json("{}") == {"token": DictToken, "position": Position(1, 1, 0), "value": {}}
    assert tokenize_json("[]") == {"token": ListToken, "position": Position(1, 1, 0), "value": []}
    assert tokenize_json(r'"foo"') == {"token": ScalarToken, "position": Position(1, 1, 0), "value": "foo"}

# Generated at 2022-06-14 14:53:19.837664
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
{
    "foo": [
        "bar",
        "baz"
    ]
}"""
    token = tokenize_json(content)

    # assert token.validate({"foo": ["bar", "baz"]})
    assert token.validate({"foo": {"bar": True}})



# Generated at 2022-06-14 14:53:31.217220
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:53:40.605416
# Unit test for function tokenize_json
def test_tokenize_json():
    json_dict = tokenize_json("{'test':1}")
    assert isinstance(json_dict,DictToken)
    json_list = tokenize_json("[1,2,3]")
    assert isinstance(json_list,ListToken)
    json_scalar = tokenize_json("1")
    assert isinstance(json_scalar,ScalarToken)
    json_string = tokenize_json("'test'")
    assert isinstance(json_string,ScalarToken)
    assert tokenize_json(" ") == DictToken({}, 0, 0, " ")
    assert tokenize_json("null") == ScalarToken(None,0,4,"null")
    assert tokenize_json("true") == ScalarToken(True,0,4,"true")
    assert tokenize

# Generated at 2022-06-14 14:53:47.034254
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.fields import String
    from typesystem.schemas import Schema

    token = tokenize_json('{"test": "value"}')
    
    assert token.value == {'test': 'value'}
    assert isinstance(token, DictToken)
    assert token._children == [Token(key='test', value='value')]
    

# Generated at 2022-06-14 14:53:50.575582
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": "foo", "b": [1, 2, 3]}'
    token = tokenize_json(content)
    assert token.value['a'] == "foo"
    assert token.value['b'] == [1, 2, 3]
    

# Generated at 2022-06-14 14:53:57.966696
# Unit test for function tokenize_json
def test_tokenize_json():
    value = {
        "field": "value",
        "nested": {
            "field": "value"
        },
        "array": [
            "a",
            "b"
        ]
    }

    json = """
    {
        "field": "value",
        "nested": {
            "field": "value"
        },
        "array": [
            "a",
            "b"
        ]
    }
    """
    assert tokenize_json(json) == value



# Generated at 2022-06-14 14:54:05.847734
# Unit test for function tokenize_json
def test_tokenize_json():
    data = {
        "test1": [1, 2, 3],
        "test2": "hello world",
        "test3": None
    }
    data_str = json.dumps(data)
    token = tokenize_json(data_str)
    assert token == {
        "test1": [1, 2, 3],
        "test2": "hello world",
        "test3": None,
    }



# Generated at 2022-06-14 14:54:11.801692
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({})
    assert tokenize_json("[]") == ListToken([])
    assert tokenize_json("[1, 2]") == ListToken([ScalarToken(1), ScalarToken(2)])
    assert tokenize_json('{"key": "value"}') == DictToken(
        {"key": ScalarToken("value")}
    )



# Generated at 2022-06-14 14:54:22.924410
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo": "bar", "baz": 42.1}'
    token = tokenize_json(content)
    assert token.content == content
    assert isinstance(token, DictToken)
    assert isinstance(token.content, str)
    assert isinstance(token.value, dict)
    assert token.value == {"foo": "bar", "baz": 42.1}

    content = '[1,2,3]'
    token = tokenize_json(content)
    assert isinstance(token, ListToken)
    assert isinstance(token.value, list)
    assert token.value == [1,2,3]

    content = '{"foo": "bar"}'
    token = tokenize_json(content)
    assert token.content == content
    assert isinstance(token, DictToken)
   

# Generated at 2022-06-14 14:54:26.600358
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("{'fruits':['apple', 'banana']}")
    assert isinstance(token, DictToken)
    assert token.data['fruits'].data == ['apple','banana']


# Generated at 2022-06-14 14:54:29.427821
# Unit test for function tokenize_json
def test_tokenize_json():
    content = u'{"name": "John", "age": 20}'
    token = tokenize_json(content)
    assert token.raw_data == {'name': 'John', 'age': 20}


# Generated at 2022-06-14 14:54:38.747330
# Unit test for function tokenize_json
def test_tokenize_json():
    # Check the tokenize_json function works for content that is valid JSON.
    valid_content = """
        {
            "favourite_food": "chips",
            "favourite_pet_name": "Fido",
            "favourite_pet_species": "dog",
            "favourite_numbers": [5, 18, 15],
            "favourite_xmas_movie": null,
            "favourite_ice_cream_brand": true,
            "favourite_ice_cream_flavour": false,
            "favourite_garden_furniture_material": "cedar"
        }
    """
    json_tokens = tokenize_json(valid_content)
    assert type(json_tokens) == DictToken
    assert json_tokens.start

# Generated at 2022-06-14 14:54:45.119291
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
      "name": "test",
      "value": 10.1
    }
    """
    token = tokenize_json(content)
    assert token.end == len(content)
    assert token.start == 1
    assert len(token.children) == 2
    assert isinstance(token.children[0], ScalarToken)
    assert isinstance(token.children[1], ScalarToken)

    value, errors = validate_json(content, validator=Schema({"name": str, "value": float}))
    assert len(errors) == 0
    assert value == {"name": "test", "value": 10.1}

# Generated at 2022-06-14 14:54:52.024248
# Unit test for function tokenize_json
def test_tokenize_json():
    input_string = '{ "lat": 40.741895, "lon": -73.989308 }'
    output = tokenize_json(input_string)

    assert isinstance(output, DictToken)
    assert isinstance(output.value[0], ScalarToken)
    assert output.value[0].value == "lat"
    assert isinstance(output.value[1], ScalarToken)
    assert output.value[1].value == 0.741895



# Generated at 2022-06-14 14:55:02.380397
# Unit test for function tokenize_json
def test_tokenize_json():
    tests = ["{}", '{"foo":"bar"}', '[1, 2]', "[]"]
    for t in tests:
        tokenize_json(t)

    # Invalid input should raise an exception.

    try:
        tokenize_json('{"foo":"bar"]')
        assert False, "Should have thrown an exception"
    except JSONDecodeError:
        pass

    try:
        tokenize_json("[1,2}")
        assert False, "Should have thrown an exception"
    except JSONDecodeError:
        pass

    try:
        tokenize_json("[1,2]  ")
        assert False, "Should have thrown an exception"
    except JSONDecodeError:
        pass



# Generated at 2022-06-14 14:55:13.061575
# Unit test for function tokenize_json
def test_tokenize_json():
    j = '{"c":[1,2,3],"b":2,"a":1}'
    assert(tokenize_json(j) == DictToken({
        ScalarToken("a", 2, 2, j): ScalarToken(1, 6, 6, j),
        ScalarToken("b", 9, 9, j): ScalarToken(2, 13, 13, j),
        ScalarToken("c", 16, 16, j): ListToken([
            ScalarToken(1, 19, 19, j),
            ScalarToken(2, 21, 21, j),
            ScalarToken(3, 23, 23, j)
        ], 18, 24, j)
    }, 0, 27, j))

