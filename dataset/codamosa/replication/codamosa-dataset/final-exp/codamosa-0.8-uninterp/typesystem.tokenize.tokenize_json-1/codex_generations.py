

# Generated at 2022-06-14 14:45:34.088296
# Unit test for function tokenize_json
def test_tokenize_json():
    data = {
        "a": 1,
        "b": 2,
        "c": {"x": "y", "z": 3},
        "d": [1, 2, 3],
    }
    json_data = json.dumps(data)
    token = tokenize_json(json_data)
    assert isinstance(token, DictToken)
    assert token.as_dict() == data
    assert token.as_dict(deep=True) == data



# Generated at 2022-06-14 14:45:40.607359
# Unit test for function tokenize_json
def test_tokenize_json():
    data = {'a':1, 'b':2, 'c':3}
    json_data = json.dumps(data)
    token = tokenize_json(json_data)

    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == 12
    assert token.children is not None
    assert len(token.children) == 3
    assert token.to_str() == json_data



# Generated at 2022-06-14 14:45:52.018668
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test valid JSON.
    content = '{"a":[1,2,3], "c": {"b": 4}}'
    token = tokenize_json(content)
    assert type(token) == DictToken
    assert token.value == {'a': [1,2,3], "c": {"b": 4}}

    # Test invalid JSON.
    content = '{"a":[1,2,3], "c": {"b": 4}'
    try:
        tokenize_json(content)
    except ParseError as e:
        assert e.text == "Expecting value"
        assert e.code == "parse_error"
        assert e.position.char_index == 22

    # Test empty string.
    try:
        tokenize_json("")
    except ParseError as e:
        assert e.text

# Generated at 2022-06-14 14:45:54.507951
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": [1, "2"], "c": 3, "b": "bee"}'
    token = tokenize_json(content)
    assert isinstance(token, dict)
    assert isinstance(token['a'], list)
    assert token['b'] == 'bee'
    assert token['a'][0] == 1
    assert token['a'][1] == '2'


# Generated at 2022-06-14 14:46:01.555058
# Unit test for function tokenize_json
def test_tokenize_json():

    content1 = """
    {
      "foo": "bar",
      "bar": "foo",
      "baz": {
        "baz": "baz",
        "foo": false,
        "bar": true,
      },
      "qux": [
        { "qux": "qux" },
        null,
        false,
        true,
        "string1",
        "string2",
        "string3",
        1,
        2,
        3,
        -1
      ]
    }
    """

    content2 = """
    {"count":{"one":"un", "other":"#"}}
    """


# Generated at 2022-06-14 14:46:11.466191
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json("{}"), DictToken)

    token = tokenize_json("{}")
    assert token.start == 0
    assert token.end == 1
    assert token.value == {}

    token = tokenize_json("100")
    assert isinstance(token, ScalarToken)
    assert token.value == 100

    token = tokenize_json('""')
    assert isinstance(token, ScalarToken)
    assert token.value == ""

    with pytest.raises(ParseError):
        tokenize_json("foo")

    with pytest.raises(ParseError):
        tokenize_json("{")

    with pytest.raises(ParseError):
        tokenize_json('{"foo"')

    with pytest.raises(ParseError):
        token

# Generated at 2022-06-14 14:46:21.864682
# Unit test for function tokenize_json
def test_tokenize_json():
    import json

    input_0 = "hello"

    try:
        tokenize_json(input_0)
    except ParseError as exc:
        assert exc.position.line_no == 1
        assert exc.position.column_no == 1
        assert exc.position.char_index == 0

    input_1 = """
{
    "key-1": 1,
    "key-2": true
}
"""

    token = tokenize_json(input_1)
    assert isinstance(token, DictToken)
    assert token.value == {"key-1": 1, "key-2": True}
    assert token.start == 1
    assert token.end == len(input_1) - 1


# Generated at 2022-06-14 14:46:30.192380
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"name":"Lucy", "color": "green", "age": 20}')
    assert type(token) is DictToken
    assert token.value == {"name": "Lucy", "color": "green", "age": 20}
    assert token.positions[0] == (1, 1, 0)
    assert token.positions[3] == (1, 6, 0)
    token = tokenize_json('{"name":"Lucy", "color": "green", "age": 20]')
    assert type(token) is DictToken

# Generated at 2022-06-14 14:46:41.186836
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json('"foo"') == ScalarToken("foo", 0, 4, '"foo"')
    assert tokenize_json("1.234") == ScalarToken(1.234, 0, 5, "1.234")
    assert tokenize_json("[{}, [], null]") == ListToken(
        [DictToken({}, 1, 2, "[{}, [], null]"), ListToken([], 4, 5, "[{}, [], null]"), ScalarToken(None, 8, 12, "[{}, [], null]")],
        0,
        16,
        "[{}, [], null]",
    )

# Generated at 2022-06-14 14:46:48.043284
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("""
      [
        {
          "name": "foo",
          "age": 1
        },
        {
          "name": "bar",
          "age": 2
        }
      ]
    """)
    assert token.serialize() == [{"name": "foo", "age": 1}, {"name": "bar", "age": 2}]



# Generated at 2022-06-14 14:46:58.651340
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{'name': 'Peter', 'age': 34}"
    token = tokenize_json(content)
    assert token.start_pos == 0
    assert token.end_pos == len(content) - 1



# Generated at 2022-06-14 14:47:01.033749
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": {"b": ["c"]}}'
    assert isinstance(tokenize_json(content), DictToken)

# Generated at 2022-06-14 14:47:11.627863
# Unit test for function tokenize_json
def test_tokenize_json():
    test_json_string = "{" \
                       "   \"test_string\": \"Hello World\"," \
                       "   \"test_boolean\": true," \
                       "   \"test_int\": 12345," \
                       "   \"test_float\": -7.2," \
                       "   \"test_null\": null," \
                       "   \"test_dict\": {" \
                       "       \"sub_item\": 23," \
                       "       \"sub_sub_item\": null" \
                       "   }," \
                       "   \"test_list\": [" \
                       "       1, 2, 3" \
                       "   ]," \
                       "   \"test_invalid_json\": \"\\n\"" \
                       "}"
    top_level_dict = tokenize_json(test_json_string)

# Generated at 2022-06-14 14:47:22.460479
# Unit test for function tokenize_json
def test_tokenize_json():
    data = {
        "name": "bob",
        "address": {"street_name": "First", "house": "101"},
        "likes": ["abc,def", "ghi"],
        "active": True,
        "ids": [1, 2, 3],
        "score": 1.23,
    }
    json_content = json.dumps(data, indent=4)
    token = tokenize_json(json_content)
    assert token.content == json_content
    assert token.value == data
    assert token.start == Position(column_no=1, line_no=1, char_index=0)
    assert token.end == Position(column_no=6, line_no=11, char_index=159)
    assert isinstance(token, DictToken)

# Generated at 2022-06-14 14:47:31.536822
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"key1": "value1", "key2": 2, "key3": false, "key4": {"key5": "value5", "key6": "value6"}}')
    assert token.keys[0].value == "key1"
    assert token.keys[0].start_index == 2
    assert token.keys[0].end_index == 7
    assert token.keys[0].start_column == 2
    assert token.keys[0].end_column == 8
    assert token.keys[0].start_line == 1
    assert token.keys[0].end_line == 1
    assert token.children[0].value == "value1"
    assert token.children[0].start_index == 9
    assert token.children[0].end_index == 16

# Generated at 2022-06-14 14:47:42.857145
# Unit test for function tokenize_json
def test_tokenize_json():
    # Valid JSON
    assert tokenize_json('{}') == DictToken({}, 0, 1, '{}')
    assert tokenize_json('[]') == ListToken([], 0, 1, '[]')
    assert tokenize_json('null') == ScalarToken(None, 0, 3, 'null')
    assert tokenize_json('true') == ScalarToken(True, 0, 3, 'true')
    assert tokenize_json('false') == ScalarToken(False, 0, 4, 'false')
    assert tokenize_json('123.456') == ScalarToken(123.456, 0, 6, '123.456')
    assert tokenize_json('"foo"') == ScalarToken('foo', 0, 4, '"foo"')

    # Invalid JSON - empty string

# Generated at 2022-06-14 14:47:54.618676
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    import pprint

    pp = pprint.PrettyPrinter(indent=4)
    test_json = '{"json_key": "json_value", "json_array": [1,2,3,4], "json_truth": true, "json_false": false, "json_null": null, "json_number": 1.23}'
    test_dict = json.loads(test_json)

    assert json.dumps(test_dict) == json.dumps(tokenize_json(test_json))
    assert json.dumps(test_dict, indent=4) == json.dumps(tokenize_json(test_json), indent=4)
    assert pp.pformat(test_dict, indent=4) == pp.pformat(tokenize_json(test_json), indent=4)
   

# Generated at 2022-06-14 14:48:06.594799
# Unit test for function tokenize_json
def test_tokenize_json():
    string_byte = tokenize_json('"world"')
    assert string_byte.value == "world"
    assert string_byte.start == 0
    assert string_byte.stop == 6

    string_byte = tokenize_json(b'"world"')
    assert string_byte.value == "world"
    assert string_byte.start == 0
    assert string_byte.stop == 6

    integer_byte = tokenize_json('123')
    assert integer_byte.value == 123
    assert integer_byte.start == 0
    assert integer_byte.stop == 3

    integer_byte = tokenize_json(b'123')
    assert integer_byte.value == 123
    assert integer_byte.start == 0
    assert integer_byte.stop == 3

    float_byte = tokenize_json('123.45')
   

# Generated at 2022-06-14 14:48:09.110141
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test that tokenize_json can read input as JSON and return a dictionary.
    """
    json_content = '{"key":"value"}'
    assert tokenize_json(json_content) == {'key': 'value'}


# Generated at 2022-06-14 14:48:14.862009
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": 1, "b": 2, "c": 3}'
    token = tokenize_json(content)
    assert token.value == {'a': 1, 'b': 2, 'c': 3}
    assert token.start == 0
    assert token.stop == 23


# Generated at 2022-06-14 14:48:20.381299
# Unit test for function tokenize_json
def test_tokenize_json():
    """Testing tokenize_json"""
    content = '{"field": "value"}'
    token = tokenize_json(content)
    assert isinstance(token, Token)
    assert token.content == content
    assert token.start == 0
    assert token.end == len(content)
    assert token.value == {"field": "value"}
    assert isinstance(token.value, dict)
    assert isinstance(token.value["field"], ScalarToken)



# Generated at 2022-06-14 14:48:30.464963
# Unit test for function tokenize_json
def test_tokenize_json():
	x = tokenize_json('{"name":"abc", "age":3}')
	assert isinstance(x, DictToken)
	assert x.name == "dict"
	assert isinstance(x.value, dict)
	assert len(x.value) == 2
	assert list(x.value.keys())[0].start_char == 2
	assert list(x.value.keys())[0].end_char == 6
	assert list(x.value.values())[1].start_char == 12
	assert list(x.value.values())[1].end_char == 13
	assert x.end_char == 16
	assert isinstance(x.value['name'], ScalarToken)
	assert isinstance(x.value['age'], ScalarToken)

# Generated at 2022-06-14 14:48:41.087665
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == ""
    assert tokenize_json("42") == 42
    assert tokenize_json("-1") == -1
    assert tokenize_json("1.5") == 1.5
    assert tokenize_json("true") == True
    assert tokenize_json("false") == False
    assert tokenize_json("null") == None
    assert tokenize_json('"hello"') == "hello"
    assert tokenize_json('["a", 1, {"b": "c"}]') == ["a", 1, {"b": "c"}]
    assert tokenize_json('{"a": 2, "b": {"c": 3}}') == {"a": 2, "b": {"c": 3}}

# Generated at 2022-06-14 14:48:50.602476
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json('"string"') == ScalarToken("string", 0, 7, '"string"')
    assert tokenize_json("123") == ScalarToken(123, 0, 3, "123")
    assert tokenize_json("null") == ScalarToken(None, 0, 4, "null")
    assert tokenize_json("true") == ScalarToken(True, 0, 4, "true")
    assert tokenize_json("false") == ScalarToken(False, 0, 5, "false")
    assert tokenize_json("1.5") == ScalarToken(1.5, 0, 3, "1.5")

# Generated at 2022-06-14 14:48:54.071186
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json("{}"), DictToken)
    assert isinstance(tokenize_json("[]"), ListToken)
    assert str(tokenize_json("null")) == "null"



# Generated at 2022-06-14 14:49:03.998136
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '''
    [
      {
        "key": "value",
        "key2": "value2",
        "key3": [
          1,
          2,
          3
        ]
      },
      {
        "key": "value",
        "key2": "value2",
        "key3": [
          1,
          2,
          3
        ]
      }
    ]
    '''
    token = tokenize_json(content)
    assert token.value == [{'key': 'value', 'key2': 'value2',
                            'key3': [1, 2, 3]},
                           {'key': 'value', 'key2': 'value2',
                            'key3': [1, 2, 3]}]
    assert token.start_pos.column_no

# Generated at 2022-06-14 14:49:13.111254
# Unit test for function tokenize_json
def test_tokenize_json():
    input_string = '{"name": "John", "age": 30, "both": [1, 2, 3]}'
    token = tokenize_json(input_string)
    assert token.data.get('name') == 'John'
    assert type(token.data.get('name')) == ScalarToken
    assert token.data.get('age') == 30
    assert type(token.data.get('age')) == ScalarToken
    assert token.data.get('both') == [1, 2, 3]
    assert type(token.data.get('both')) == ListToken



# Generated at 2022-06-14 14:49:25.522545
# Unit test for function tokenize_json
def test_tokenize_json():
    # Empty string
    assert str(tokenize_json("")) == "<Empty Token>"

    # Empty Object
    assert str(tokenize_json("{}")) == "<DictToken {}>"

    # Empty Array
    assert str(tokenize_json("[]")) == "<ListToken []>"

    # Null
    assert str(tokenize_json("null")) == "<ScalarToken None>"

    # Boolean
    assert str(tokenize_json("true")) == "<ScalarToken True>"
    assert str(tokenize_json("false")) == "<ScalarToken False>"

    # Number
    assert str(tokenize_json("0")) == "<ScalarToken 0>"
    assert str(tokenize_json("-0")) == "<ScalarToken 0>"

# Generated at 2022-06-14 14:49:32.362082
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo": "bar"}'
    res = tokenize_json(content)
    assert res.value == {"foo": "bar"}

    content = ""
    with pytest.raises(ParseError, match="No content"):
        res = tokenize_json(content)
    
    content = "{"
    with pytest.raises(ParseError, match="JSONDecodeError"):
        res = tokenize_json(content)


# Generated at 2022-06-14 14:49:43.373566
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('') == {}, 'Empty json should be translated to empty dict'
    assert tokenize_json('{}').value == {}, 'Empty json should be translated to empty dict'
    assert tokenize_json('"a"').value == 'a', 'A single string should be returned as a string'
    assert tokenize_json('true').value is True, 'True should be returned as boolean True'
    assert tokenize_json('1').value == 1, 'An integer should be returned as an int'
    assert tokenize_json('1.1').value == 1.1, 'An float should be returned as an float'
    assert tokenize_json('["a"]').value == ['a'], 'A simple array should be returned as an array'

# Generated at 2022-06-14 14:49:59.633158
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"status": 200, "message": "Ok"}'
    token = tokenize_json(content)
    assert(type(token) == DictToken)

    content = '{"status": 200, "message": "Ok'
    error = None
    try:
        token = tokenize_json(content)
    except ParseError as e:
        error = e
    assert(error is not None)
    assert(error.text == "Unterminated string starting at: line 1 column 42 (char 41).")
    assert(error.code == "parse_error")
    assert(error.position.line_no == 1)
    assert(error.position.column_no == 42)
    assert(error.position.char_index == 41)

    content = ''
    error = None

# Generated at 2022-06-14 14:50:05.591657
# Unit test for function tokenize_json
def test_tokenize_json():
    # Handles the empty string for clear error messages
    assert tokenize_json("") is None

    # Test a simple object
    token = tokenize_json("""
    {
        "foo": "bar"
    }
    """)
    assert isinstance(token, DictToken)

    # Test a simple list
    token = tokenize_json("""
    [
        "foo",
        "bar"
    ]
    """)
    assert isinstance(token, ListToken)

    # Test nested lists and objects
    token = tokenize_json("""
    [
        {
            "foo": [
                {
                    "bar": "baz"
                }
            ]
        }
    ]
    """)
    assert isinstance(token, ListToken)

    # Test a json string with quotes, colons,

# Generated at 2022-06-14 14:50:15.962834
# Unit test for function tokenize_json
def test_tokenize_json():
    instance = tokenize_json(
        '{\n'
        '  "I am a string": "I am a string",\n'
        '  "I am a string with a function call": upper("I am a string"),\n'
        '  "I am a number": 1,\n'
        '  "I am a list": [1, 2, 3],\n'
        '  "I am a dict": {"a": 1, "b": 2},\n'
        '}'
    )
    assert isinstance(instance, DictToken)
    assert isinstance(instance[0][1], ScalarToken)
    assert instance[0][1].value == "I am a string"
    assert isinstance(instance[1][1], ScalarToken)

# Generated at 2022-06-14 14:50:22.529158
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = '{"name":"John","age":30,"cars": {"car1":"Ford","car2":"BMW","car3":"Fiat"}}'
    token_json_string = tokenize_json(json_string)
    assert token_json_string.start == 0
    assert token_json_string.end == len(json_string) - 1
    assert token_json_string.content == json_string


# Generated at 2022-06-14 14:50:30.461454
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{}') == DictToken({}, 0, 1, '{}')
    assert tokenize_json('[]') == ListToken([], 0, 1, '[]')
    assert tokenize_json('"foo"') == ScalarToken('foo', 0, 4, '"foo"')
    assert tokenize_json('true') == ScalarToken(True, 0, 3, 'true')
    assert tokenize_json('false') == ScalarToken(False, 0, 4, 'false')
    assert tokenize_json('null') == ScalarToken(None, 0, 3, 'null')

# Generated at 2022-06-14 14:50:41.352679
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test case 1: Parsing a JSON string with a number
    json_string = '{"score": 100}'
    content = bytes(json_string, "utf-8")
    token = tokenize_json(content)
    assert token.value == {"score": 100}

    # Test case 2: Parsing a JSON string with a string
    json_string = '{"username": "Big Bird"}'
    content = bytes(json_string, "utf-8")
    token = tokenize_json(content)
    assert token.value == {"username": "Big Bird"}

    # Test case 3: Parsing a JSON string with a boolean
    json_string = '{"isAdmin": true}'
    content = bytes(json_string, "utf-8")
    token = tokenize_json(content)

# Generated at 2022-06-14 14:50:53.400383
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({})
    assert tokenize_json("[]") == ListToken([])
    assert tokenize_json('"string"') == ScalarToken("string")
    assert tokenize_json("1") == ScalarToken(1)
    assert tokenize_json("12.") == ScalarToken(12.0)
    assert tokenize_json("1.2") == ScalarToken(1.2)
    assert tokenize_json("1.2e3") == ScalarToken(1.2e3)
    assert tokenize_json("null") == ScalarToken(None)
    assert tokenize_json("true") == ScalarToken(True)
    assert tokenize_json("false") == ScalarToken(False)


# Generated at 2022-06-14 14:50:57.312652
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """{"string": "foo", "int": 1, "float": 1.1}"""
    token = tokenize_json(content)
    assert token.value == {"string":"foo", "int":1,"float":1.1}

# Generated at 2022-06-14 14:51:04.598970
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "string", "age": 1, "active": true, "data": {"a": 1, "b": 2, "c": 3}}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)

    content = '{"name": "string", "numbers": [1, 2, 3, 4, 5], "active": true, "data": {"a": 1, "b": 2, "c": 3}}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)



# Generated at 2022-06-14 14:51:10.508686
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"name":"Sachin Rana"}')
    new_dict = {"name": "Sachin Rana"}
    dict_token = DictToken(value=new_dict, start=0, end=22, content='{"name":"Sachin Rana"}')
    assert(token == dict_token)


# Generated at 2022-06-14 14:51:20.166156
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"name": "Prajwal"}')
    assert isinstance(token, DictToken)
    assert isinstance(token.value["name"], ScalarToken)
    assert token.value["name"].value=="Prajwal"


# Generated at 2022-06-14 14:51:30.392304
# Unit test for function tokenize_json
def test_tokenize_json():
    assert (tokenize_json('{') ==
        JSONDecodeError("Expecting property name enclosed in double quotes", '{', 0))
    assert (tokenize_json("") == ParseError("No content.", code="no_content", 
        position=Position(column_no=1, line_no=1, char_index=0)))
    assert (tokenize_json("{") == ParseError("Expecting property name enclosed in double quotes.", 
        code="parse_error", position=Position(column_no=1, line_no=1, char_index=0)))
    assert (tokenize_json("{}") == DictToken({}, 0, 1, "{}"))

# Generated at 2022-06-14 14:51:40.092068
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b"{}") == DictToken()
    assert tokenize_json('""') == ScalarToken("")
    assert tokenize_json('"string"') == ScalarToken("string")
    assert tokenize_json('"string\\n"') == ScalarToken("string\n")
    assert tokenize_json('[1,2]') == ListToken([1, 2])
    assert tokenize_json('{"a":[1,2]}') == DictToken({"a": [1, 2]})

    # Array with a single element
    assert tokenize_json('["string"]') == ListToken(["string"])

    # Array within dictionary
    assert tokenize_json('{"a":["string"]}') == DictToken({"a": ["string"]})

    # Array within array
    assert tokenize

# Generated at 2022-06-14 14:51:42.574592
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"name": "test"}')
    assert token.value["name"].value == "test"


# Generated at 2022-06-14 14:51:54.179018
# Unit test for function tokenize_json
def test_tokenize_json():
    sample_json_data = {
        "name": "john",
        "age": 22,
        "friends": ["mike", "johny"],
        "address": {
            "street": "9th Street",
            "city": "San Jose",
            "state": "CA",
            "zip_code": "95113",
        },
    }
    token = tokenize_json(json.dumps(sample_json_data))
    assert isinstance(token, DictToken)
    assert len(token) == 4
    assert token.get("name").value == "john"
    assert token.get("age").value == 22
    assert isinstance(token.get("friends"), ListToken)
    assert isinstance(token.get("address"), DictToken)

# Generated at 2022-06-14 14:52:00.937333
# Unit test for function tokenize_json
def test_tokenize_json():
    field = Field(type="string")
    schema = Schema(fields={"my_field": field})

    assert isinstance(tokenize_json(""), Token)
    assert isinstance(tokenize_json("[]"), ListToken)
    assert isinstance(tokenize_json("{}"), DictToken)
    assert isinstance(tokenize_json("123"), ScalarToken)
    assert isinstance(tokenize_json('"string"'), ScalarToken)
    assert isinstance(tokenize_json("true"), ScalarToken)
    assert isinstance(tokenize_json("null"), ScalarToken)
    assert isinstance(tokenize_json("  null "), ScalarToken)
    assert isinstance(tokenize_json("null\t"), ScalarToken)

# Generated at 2022-06-14 14:52:06.452903
# Unit test for function tokenize_json
def test_tokenize_json():
    a = {"a": 1}
    b = tokenize_json(json.dumps(a))
    assert isinstance(b, dict)
    assert "a" in b
    assert isinstance(b["a"], int)



# Generated at 2022-06-14 14:52:16.356321
# Unit test for function tokenize_json
def test_tokenize_json():
    validator = Field(type="string")
    content = '{"name":"Einstein"}'
    token = tokenize_json(content)
    assert token.value["name"].value == "Einstein"
    assert token.value["name"].raw_value == '"Einstein"'
    assert token.value["name"].position == Position(1, 1, 14)
    assert token.position == Position(1, 1, 0)

    result = validate_json(content, validator)
    assert result[0] == '"Einstein"'
    assert result[1] == []

    content = '{"name":42}'
    token = tokenize_json(content)
    assert token.value["name"].value == 42
    assert token.value["name"].raw_value == '42'

# Generated at 2022-06-14 14:52:19.494421
# Unit test for function tokenize_json
def test_tokenize_json():
    input_content = '{"key": "value"}'
    token = tokenize_json(input_content)
    value = token.value
    assert isinstance(value, dict)
    assert value["key"] == "value"



# Generated at 2022-06-14 14:52:28.956168
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test valid JSON.
    content = '{"name": "John", "age": 30, "city": "New York"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken), "JSON content not converted to dict token."
    assert token.value == {"name": "John", "age": 30, "city": "New York"}

    # Test invalid JSON.
    content = '{"name": "John", "age": 30, "city: "New York"}'
    try:
        tokenize_json(content)
        assert False, "Invalid JSON content did not raise ParseError."
    except ParseError as exc:
        assert isinstance(exc, ParseError)

# Generated at 2022-06-14 14:52:39.529663
# Unit test for function tokenize_json
def test_tokenize_json():
    json_dict = {"a": 1, "b": "foo"}
    tokens = tokenize_json(str(json_dict))
    assert str(json_dict) == str(tokens)



# Generated at 2022-06-14 14:52:48.346059
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"foo": "bar"}') == DictToken(
        {"foo": ScalarToken("bar", 5, 10, '{"foo": "bar"}')},
        0,
        13,
        '{"foo": "bar"}',
    )
    assert tokenize_json('{"foo": "bar"}, 10') == ListToken(
        [
            DictToken(
                {"foo": ScalarToken("bar", 5, 10, '{"foo": "bar"}')},
                0,
                13,
                '{"foo": "bar"}',
            ),
            ScalarToken(10, 14, 16, '{"foo": "bar"}, 10'),
        ],
        0,
        17,
        '{"foo": "bar"}, 10',
    )

# Generated at 2022-06-14 14:52:59.190208
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """{
    "name": "Bob",
    "age": 27,
    "foods": [
        "pizza",
        "bread",
        "cheese",
        "chinese"
    ],
    "other naaems": null
}"""
    top_level_dict = tokenize_json(content)
    assert isinstance(top_level_dict, DictToken)
    assert top_level_dict.key == "dict"

# Generated at 2022-06-14 14:53:04.925525
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    test cases for json parser, to ensure no regression.
    """
    content = '{"name": "Leo", "age": 99, "active": true}'
    token = tokenize_json(content)
    assert token.pos_start.column_no == 1
    assert token.pos_start.line_no == 1
    assert token.pos_start.char_index == 0
    assert token.pos_end.column_no == 43
    assert token.pos_end.line_no == 1
    assert token.pos_end.char_index == 42



# Generated at 2022-06-14 14:53:14.504011
# Unit test for function tokenize_json
def test_tokenize_json():
    # basic test
    content = '{"foo":"bar","baz": [{"id": 1}]}'
    tokens = tokenize_json(content)
    assert tokens.start_pos == 0
    assert tokens.end_pos == len(content)
    assert tokens.children[0].value == "foo"
    assert tokens.children[0].start_pos == 2
    assert tokens.children[0].end_pos == 6
    assert tokens.children[1].start_pos == 9
    assert tokens.children[1].end_pos == 13
    assert tokens.children[2].start_pos == 17
    assert tokens.children[2].end_pos == len(content)
    assert tokens.children[2].children[0].value == "id"
    assert tokens.children[2].children[0].start_pos == 20

# Generated at 2022-06-14 14:53:20.938340
# Unit test for function tokenize_json
def test_tokenize_json():
    structure = {
        'person': {
            'name': 'jordan',
            'age': 20,
            'hobbies': ['bmx', 'paintball', 'bass guitar']
        },
        'size': 'large',
        'enabled': True
    }
    json_str = json.dumps(structure)
    assert tokenize_json(json_str) == structure


# Generated at 2022-06-14 14:53:29.408794
# Unit test for function tokenize_json
def test_tokenize_json():
    c = tokenize_json('[1, {"name": "John Doe"}, true]')
    assert isinstance(c, ListToken)
    assert len(c.value) == 3
    assert isinstance(c.value[0], ScalarToken)
    assert c.value[0].value == 1
    assert isinstance(c.value[1], DictToken)
    assert c.value[1].value == {"name": "John Doe"}
    assert isinstance(c.value[2], ScalarToken)
    assert c.value[2].value == True


# Generated at 2022-06-14 14:53:34.220510
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Tokenize a JSON string.
    """
    content = """
    {"a": 2}
    """
    token = tokenize_json(content)
    assert token.get_value()["a"] == 2
    assert token.get_value(position=Position(line_no=1, column_no=5)) == 2



# Generated at 2022-06-14 14:53:42.453566
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:53:52.542914
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:54:06.302643
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tokens import (
        DictToken,
        ListToken,
        ScalarToken,
        Token,
    )

    content = """
    {
    "key": [1, 2],
    "key2": "asd"
    }
    """

    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert isinstance(token.value["key"], ListToken)
    assert isinstance(token.value["key2"], ScalarToken)

    content = ""
    position = Position(column_no=1, line_no=1, char_index=0)
    error_message = ParseError(text="No content.", code="no_content", position=position)

# Generated at 2022-06-14 14:54:16.168174
# Unit test for function tokenize_json
def test_tokenize_json():
    f = open("../input.json", "r")
    content = f.read()
    f.close()

    token = tokenize_json(content)

    assert token.sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tokens[0].sub_tok

# Generated at 2022-06-14 14:54:26.047927
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"test": [1,2,3]}')
    expected = {"test": [ScalarToken(1, 14, 15, '{"test": [1,2,3]}'),
                         ScalarToken(2, 17, 18, '{"test": [1,2,3]}'),
                         ScalarToken(3, 19, 20, '{"test": [1,2,3]}')]}
    assert token == expected

    token = tokenize_json('{"test": [1,2,3]}', )

# Generated at 2022-06-14 14:54:27.794088
# Unit test for function tokenize_json
def test_tokenize_json():
    result = tokenize_json("[]")
    assert result == ListToken([], 0, 1, "[]")

# Generated at 2022-06-14 14:54:36.440562
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:54:44.901634
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json('{"foo": "bar"}') == DictToken(
        {"foo": ScalarToken("bar", 6, 11, '{"foo": "bar"}')}, 0, 13, '{"foo": "bar"}'
    )
    assert tokenize_json('["foo", "bar"]') == ListToken(
        [ScalarToken("foo", 2, 5, '["foo", "bar"]'), ScalarToken("bar", 8, 11, '["foo", "bar"]')],
        0, 13,
        '["foo", "bar"]',
    )

# Generated at 2022-06-14 14:54:55.140526
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{\"a\": [1,2,3], \"b\": {\"c\": 1}}"
    result = tokenize_json(content)
    assert isinstance(result, DictToken)
    assert result.type == "dict"
    assert result.tokenized_content == content
    assert result.parent_token is None
    assert result.children["a"].type == "list"
    assert result.children["a"].tokenized_content == "[1,2,3]"
    assert result.children["a"].parent_token is result
    assert result.children["b"].type == "dict"
    assert result.children["b"].tokenized_content == "{\"c\": 1}"
    assert result.children["b"].children["c"].type == "scalar"
    assert result.children["b"].children

# Generated at 2022-06-14 14:55:01.624721
# Unit test for function tokenize_json
def test_tokenize_json():
    json_str = '{"foo":{"bar":[1,2,3]}}'
    expected_token = {
        "type": "DictToken",
        "value": {"foo": {"type": "DictToken", "value": {"bar": {"type": "ListToken", "value": [1, 2, 3]}}}},
    }
    result_token = tokenize_json(json_str)
    assert result_token == expected_token



# Generated at 2022-06-14 14:55:08.101229
# Unit test for function tokenize_json
def test_tokenize_json():
    import ast
    import json

    def check(string: str) -> Token:
        token = tokenize_json(string)
        assert ast.literal_eval(string) == token.to_python()
        assert json.loads(string) == token.to_python()
        return token

    null = 'null'
    true = 'true'
    false = 'false'
    integer = '42'
    float = '3.14159'
    string = '"hello"'
    array = '[]'
    array_of_scalars = '[null, true, 3.14, "hello"]'
    array_of_arrays = '[[], [], []]'

# Generated at 2022-06-14 14:55:13.365622
# Unit test for function tokenize_json
def test_tokenize_json():
    def get_position(token):
        position = token.position
        return (
            position.line_no,
            position.column_no,
            position.char_index,
            position.inner_start,
            position.inner_end,
        )

    # Parse a simple item
    token = tokenize_json('"foo"')

    assert isinstance(token, ScalarToken)
    assert token.value == "foo"
    assert get_position(token) == (1, 2, 1, 1, 5)

    # Parse a simple list
    token = tokenize_json('[1234]')

    assert isinstance(token, ListToken)
    assert token.value[0].value == 1234
    assert get_position(token) == (1, 2, 1, 0, 7)

    # Parse a