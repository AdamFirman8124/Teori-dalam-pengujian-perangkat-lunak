

# Generated at 2022-06-14 14:45:39.388230
# Unit test for function tokenize_json
def test_tokenize_json():
  token = tokenize_json("[0, 0, 0]")
  assert isinstance(token, ListToken)
  assert len(token.value) == 3
  assert token.value[0] == 0
  assert token.value[1] == 0
  assert token.value[2] == 0


# Generated at 2022-06-14 14:45:41.952547
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("{}")
    assert isinstance(token, DictToken)
    assert token.value == {}



# Generated at 2022-06-14 14:45:53.087361
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"type": "string"}') == DictToken({'type': ScalarToken('string', 9, 17, '{"type": "string"}')}, 0, 18, '{"type": "string"}')
    assert tokenize_json('"hello"') == ScalarToken('hello', 0, 6, '"hello"')
    assert tokenize_json('[1, 2, 3]') == ListToken([ScalarToken(1, 1, 2, '[1, 2, 3]'), ScalarToken(2, 4, 5, '[1, 2, 3]'), ScalarToken(3, 7, 8, '[1, 2, 3]')], 0, 11, '[1, 2, 3]')
    assert tokenize_json('true') == ScalarToken(True, 0, 4, 'true')
    assert tokenize_

# Generated at 2022-06-14 14:45:57.842445
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:46:08.444658
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"count": 10}') == DictToken({ScalarToken('count', 0, 7, '{"count": 10}'): ScalarToken(10, 9, 12, '{"count": 10}')}, 0, 13, '{"count": 10}')
    assert tokenize_json('{"count": 10.0}') == DictToken({ScalarToken('count', 0, 7, '{"count": 10.0}'): ScalarToken(10.0, 9, 14, '{"count": 10.0}')}, 0, 15, '{"count": 10.0}')

# Generated at 2022-06-14 14:46:18.463239
# Unit test for function tokenize_json
def test_tokenize_json():
    data = '''
{
    "text": "hello world",
    "is_active": true,
    "count": 1,
    "nested": {
        "a": 1,
        "b": 2
    },
    "items": [
        {
            "id": 1
        },
        {
            "id": 2
        }
    ]
}
'''

    token = tokenize_json(data)

    assert token.type == "dict"

    assert token.value["text"].type == "scalar"
    assert token.value["text"].value == "hello world"
    assert token.value["text"].span.start == 16
    assert token.value["text"].span.stop == 29
    assert token.value["text"].span.line_no == 3

# Generated at 2022-06-14 14:46:25.958610
# Unit test for function tokenize_json
def test_tokenize_json():
    json_str = '''{
        "key1": "value1",
        "key2": 2,
        "key3": true,
        "key4": false,
        "key5": null,
        "key6": {
            "key7": "value7"
        },
        "key8": ["item1", "item2", "item3"],
        "key9": 3.14,
        "key10": [
            {
                "key11": "value11"
            },
            {
                "key12": "value12"
            }
        ],
        "key13": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    }'''
    token = tokenize_json(json_str)
    assert token

# Generated at 2022-06-14 14:46:34.524431
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"beer": "coors", "dog": "doberman"}')
    print(token)
    assert type(token) == DictToken
    assert len(token._tokens) == 2
    assert type(token._tokens) == list
    assert token._tokens[0][0].data == "beer"
    assert token._tokens[0][1].data == "coors"
    assert token._tokens[1][0].data == "dog"
    assert token._tokens[1][1].data == "doberman"


# Generated at 2022-06-14 14:46:38.562470
# Unit test for function tokenize_json
def test_tokenize_json():
    dict_token = tokenize_json('{"a": "b"}')
    assert isinstance(dict_token, DictToken)


# Tests for function validate_json (and by extension, tokenize_json and validate_with_position).

# Generated at 2022-06-14 14:46:46.225262
# Unit test for function tokenize_json
def test_tokenize_json():
    with pytest.raises(ParseError, match="No content."):
        tokenize_json("")

    with pytest.raises(ParseError, match="Unexpected character ']' found."):
        tokenize_json("]")

    with pytest.raises(ParseError, match="Unexpected character '@' found."):
        tokenize_json("@")

    with pytest.raises(ParseError, match="Expecting value"):
        tokenize_json("{")

    with pytest.raises(ParseError, match="Unterminated string starting"):
        tokenize_json('{"foo": "bar')

    with pytest.raises(ParseError, match="Not enough digit characters."):
        tokenize_json("1.123e1.+1")


# Generated at 2022-06-14 14:47:06.891562
# Unit test for function tokenize_json
def test_tokenize_json():
    # Basic dict
    content = b'{"key": "value"}'
    expected = {
        "type": "dict",
        "children": [
            {
                "type": "scalar",
                "key": "key",
                "start": 2,
                "end": 7,
                "content": '{"key": "value"}',
            },
            {"type": "scalar", "key": "value", "start": 10, "end": 17, "content": '{"key": "value"}'},
        ],
        "start": 1,
        "end": 18,
        "content": '{"key": "value"}',
    }
    assert tokenize_json(content) == expected

    # Basic list
    content = b'["value", "value"]'

# Generated at 2022-06-14 14:47:15.365253
# Unit test for function tokenize_json
def test_tokenize_json():
    typesystem.register_schema(TestSchema)
    root_token = tokenize_json(json_string)
    assert isinstance(root_token, DictToken)
    assert root_token.content == json_string
    assert root_token.line_no == 1
    assert root_token.column_no == 1
    assert root_token.char_index == 0
    assert root_token.end_line_no == 38
    assert root_token.end_column_no == 28
    assert root_token.end_char_index == len(json_string) - 1
    assert root_token.start == 0
    assert root_token.end == len(json_string) - 1

# Generated at 2022-06-14 14:47:26.873650
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(b'{"test": true}')
    assert type(token) is DictToken, "should be a DictToken but is not"
    assert token.start_position.column_no == 0, "should be 0 but is %d" % token.start_position.column_no
    assert token.end_position.column_no == 15, "should be 15 but is %d" % token.end_position.column_no
    assert token.start_position.line_no == 1, "should be 1 but is %d" % token.start_position.line_no
    assert token.start_position.char_index == 0, "should be 0 but is %d" % token.start_position.char_index
    assert token.end_position.line_no == 1, "should be 1 but is %d"

# Generated at 2022-06-14 14:47:31.713169
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "John Doe", "age": 18}'
    expected = DictToken({
        "name": ScalarToken("John Doe", 11, 20, content),
        "age": ScalarToken(18, 25, 27, content)
    }, 0, 28, content)
    actual = tokenize_json(content)
    assert actual == expected


# Generated at 2022-06-14 14:47:43.016837
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": 1, "b": [2, 3, 4]}')
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1, "b": [2, 3, 4]}

    token = tokenize_json('{"a": 1, "b": [2, 3, 4], "c": {"d": 5}}')
    assert isinstance(token, DictToken)
    assert token.value == {"a": 1, "b": [2, 3, 4], "c": {"d": 5}}

    token = tokenize_json('{"a": 1, "b": [2, 3, 4], "c": [{"d": 5}, {"e": 6}]}')
    assert isinstance(token, DictToken)

# Generated at 2022-06-14 14:47:54.733965
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo": "bar"}'
    expected_token = DictToken(
        value={
            ScalarToken(value="foo", start=1, end=5, content=content): ScalarToken(
                value="bar", start=9, end=14, content=content
            )
        },
        start=0,
        end=15,
        content=content,
    )
    assert tokenize_json(content) == expected_token

    # test with no content
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("")

    assert exc_info.value.code == "no_content"

    # test with an integer field
    content = '{"foo": 42}'

# Generated at 2022-06-14 14:48:05.592952
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    data = {
        "name": "Peter",
        "age": "23",
        "address": "paris",
        "phone": "0033-38-40-40-40",
        "email": "peter@example.com",
        "favorite_food": ["steak", "fries", "pasta"],
        "favorite_drinks": {"coffee": 4, "milk": 3},
    }
    json_data = json.dumps(data)
    data_from_json = tokenize_json(json_data)
    print(data_from_json.to_dict())
    


if __name__ == "__main__":
    test_tokenize_json()

# Generated at 2022-06-14 14:48:17.730969
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("")
    assert type(token) is ScalarToken
    assert token.value == ""
    assert token.start_position == Position(column_no=0, line_no=0, char_index=0)
    assert token.end_position == Position(column_no=0, line_no=0, char_index=0)

    token = tokenize_json("[]")
    assert type(token) is ListToken
    assert token.value == []
    assert token.start_position == Position(column_no=0, line_no=0, char_index=0)
    assert token.end_position == Position(column_no=2, line_no=0, char_index=2)

    token = tokenize_json("{}")
    assert type(token) is DictToken

# Generated at 2022-06-14 14:48:28.501799
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test for empty string
    token = tokenize_json("")
    assert token == None

    # Test for a single string
    token = tokenize_json("\"abcd\"")
    assert isinstance(token, ScalarToken)
    assert token.value == "abcd"

    # Test for a single integer
    token = tokenize_json("10")
    assert isinstance(token, ScalarToken)
    assert token.value == 10

    # Test for a single boolean
    token = tokenize_json("true")
    assert isinstance(token, ScalarToken)
    assert token.value == True

    # Test for a single null
    token = tokenize_json("null")
    assert isinstance(token, ScalarToken)
    assert token.value == None

    # Test for a single float
    token = tokenize_

# Generated at 2022-06-14 14:48:32.609780
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{    "foo": 1234, "bar": [1, 2, 3] }')
    assert isinstance(token, dict)
    assert isinstance(token['foo'], int)
    assert isinstance(token['bar'], list)
    assert token['bar'][0] == 1


# Generated at 2022-06-14 14:48:47.204158
# Unit test for function tokenize_json
def test_tokenize_json():
    assert (tokenize_json('{"a":1}') ==
        DictToken({'a': ScalarToken(1, 2, 3, '{"a":1}')}, 0, 6, '{"a":1}')
    )
    assert (tokenize_json('[1,2,3]') ==
        ListToken([ScalarToken(1, 1, 2, '[1,2,3]'), ScalarToken(2, 4, 5, '[1,2,3]'), ScalarToken(3, 7, 8, '[1,2,3]')], 0, 10, '[1,2,3]')
    )

# Generated at 2022-06-14 14:48:58.799782
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "name": "John Smith",
        "age": 56,
        "height": 1.72,
        "friends": [
            "Alice",
            "Bob",
            "Eve"
        ]
    }
    """
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value["name"] == "John Smith"
    assert token.value["age"] == 56
    assert token.value["height"] == 1.72
    assert isinstance(token.value["friends"], ListToken)
    assert token.value["friends"].value == [
        "Alice",
        "Bob",
        "Eve",
    ]


# Generated at 2022-06-14 14:49:03.700875
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"name":"abc","age":24}') == DictToken({"name":"abc","age":24}, 0, 23, '{"name":"abc","age":24}')
    with pytest.raises(ParseError):
        tokenize_json('{name":"abc","age":24}')
    with pytest.raises(ParseError):
        tokenize_json('')



# Generated at 2022-06-14 14:49:10.715177
# Unit test for function tokenize_json
def test_tokenize_json():
    test_str = """
    {
        "a": [1, 2, 3],
        "b": "Hello World"
    }
    """
    token = tokenize_json(test_str)
    assert isinstance(token, DictToken)
    assert token.source == test_str
    assert token.start_mark == Position(line_no=2, column_no=3, char_index=11)
    assert token.end_mark == Position(line_no=4, column_no=4, char_index=59)

    assert isinstance(token.value['a'], ListToken)
    assert token.value['a'].source == test_str
    assert token.value['a'].start_mark == Position(line_no=3, column_no=11, char_index=20)

# Generated at 2022-06-14 14:49:18.597264
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
    "hello": "world",
    "foo": {
      "bar": [
        1,
        2,
        3
      ]
    }
    }
    """
    expected = {
        "hello": "world",
        "foo": {
            "bar": [
                1,
                2,
                3
            ]
        }
    }

    token = tokenize_json(content)
    assert token.to_json() == expected


# Generated at 2022-06-14 14:49:30.403911
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tests.test_python import TestBase, FieldTestBase

    class TestSchema(Schema, TestBase):
        hello = FieldTestBase(required=True)
        goodbye = FieldTestBase(required=True)

    class Test(Schema, TestBase):
        a = FieldTestBase(required=True, choices=["a", "b", "c"])
        b = FieldTestBase(required=False)
        c = FieldTestBase(required=False, validators=[TestSchema])

    content = '{"a": "b"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value == {"a": "b"}
    assert token.content == content
    assert token.positions[0].char_index == 0

# Generated at 2022-06-14 14:49:31.332424
# Unit test for function tokenize_json
def test_tokenize_json():
    pass


# Generated at 2022-06-14 14:49:41.326590
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json('{"foo": "bar"}') == DictToken(
        {"foo": ScalarToken("bar", 5, 9, '{"foo": "bar"}')}, 0, 14, '{"foo": "bar"}'
    )
    assert tokenize_json('{"foo": ["bar"]}') == DictToken(
        {
            "foo": ListToken(
                [ScalarToken("bar", 8, 11, '{"foo": ["bar"]}')],
                6,
                13,
                '{"foo": ["bar"]}',
            )
        },
        0,
        16,
        '{"foo": ["bar"]}',
    )

# Generated at 2022-06-14 14:49:49.867281
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test string serialization.
    #
    # FIXME: add test for non-ascii string

    # Test number serialization.
    json = "1"
    expected = ScalarToken(value=1, start=0, end=0, content=json)
    assert tokenize_json(json) == expected

    json = "1.0"
    assert tokenize_json(json) == expected

    json = "1.1e1"
    expected = ScalarToken(value=11, start=0, end=4, content=json)
    assert tokenize_json(json) == expected

    # Test integer edge cases
    json = "18446744073709551615"
    expected = ScalarToken(value=18446744073709551615, start=0, end=19, content=json)


# Generated at 2022-06-14 14:49:55.648771
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("[1, 2, 3]")
    assert token == [1, 2, 3]
    assert isinstance(token, ListToken)

    token = tokenize_json("{'foo': 'bar'}")
    assert token == {"foo": "bar"}
    assert isinstance(token, DictToken)



# Generated at 2022-06-14 14:50:09.228681
# Unit test for function tokenize_json
def test_tokenize_json():
    json_str = '{"a": 3, "b": [1, 2, 3], "c": {"d": 2}}'
    json_token = tokenize_json(json_str)
    assert isinstance(json_token, Token)
    assert isinstance(json_token, DictToken)
    assert json_token.value == {"a": 3, "b": [1, 2, 3], "c": {"d": 2}}
    assert json_token.start == 0
    assert json_token.end == len(json_str) - 1
    assert json_token.content == json_str
    assert len(json_token.children) == 3
    assert isinstance(json_token.children[0], ScalarToken)
    assert json_token.children[0].value == 3

# Generated at 2022-06-14 14:50:15.481124
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Alan Turing", "age": 41}'
    try:
        tokenize_json(content)
    except ParseError as e:
        assert False, "This should not produce an error"
    
    content = '{ name: "Alan Turing", age: 41}'
    try:
        tokenize_json(content)
        assert False, "This should produce an error"
    except ParseError as e:
        assert True, "This should produce an error"


# Generated at 2022-06-14 14:50:26.465083
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": "test", "b": {"c": "cat"}, "d": [1, 2, 3]}'
    token = tokenize_json(content)
    assert token.type == "DICT"
    assert token.value == {"a": "test", "b": {"c": "cat"}, "d": [1, 2, 3]}

    assert token.value["a"].type == "SCALAR"
    assert token.value["a"].value == "test"

    assert token.value["b"].type == "DICT"
    assert token.value["b"].value == {"c": "cat"}

    assert token.value["b"].value["c"].type == "SCALAR"
    assert token.value["b"].value["c"].value == "cat"


# Generated at 2022-06-14 14:50:29.255475
# Unit test for function tokenize_json
def test_tokenize_json():
    valid_json = '{"hello": "world"}'
    error_json = '{"hello": "world"'  # unclosed string

    assert isinstance(tokenize_json(valid_json), DictToken)

    with pytest.raises(ParseError):
        tokenize_json(error_json)


# Generated at 2022-06-14 14:50:40.513388
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")
    assert tokenize_json("[{}]") == ListToken([DictToken({}, 1, 2, "[{}]")], 0, 3, "[{}]")
    assert tokenize_json("[1, 2]") == ListToken(
        [ScalarToken(1, 1, 1, "[1, 2]"), ScalarToken(2, 4, 4, "[1, 2]")], 0, 5, "[1, 2]"
    )
    assert tokenize_json("i'm not json") == ScalarToken("i'm not json", 0, 12, "i'm not json")
    # ensure that we don't fail on non

# Generated at 2022-06-14 14:50:52.832647
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"a":1}') == \
        DictToken({ScalarToken(u"a", 0, 1, '{"a":1}'): ScalarToken(1, 4, 4, '{"a":1}')}, 0, 7, '{"a":1}')
    assert tokenize_json("[]") == ListToken([], 0, 1, '[]')

# Generated at 2022-06-14 14:51:03.791889
# Unit test for function tokenize_json
def test_tokenize_json():
    
    # Test string with newline character.
    test_json_string_with_newline = """{
        "foo": "bar"
    }"""
    assert tokenize_json(test_json_string_with_newline) == {
        'foo': 'bar'
    } 

    # Test string with escaped newline string
    test_json_string_with_escaped_newline_string = '''{
        "foo": "bar\\nbar"
    }'''
    assert tokenize_json(test_json_string_with_escaped_newline_string) == {
        'foo': 'bar\nbar'
    }

    # Test string with escaped tab string

# Generated at 2022-06-14 14:51:15.570750
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"id": null}') == DictToken(
        {ScalarToken("id", 2, 4, '{"id": null}'): ScalarToken(None, 8, 12, '{"id": null}')},
        0,
        13,
        '{"id": null}',
    )
    assert tokenize_json(b'{"id": 1}') == DictToken(
        {ScalarToken("id", 2, 4, '{"id": 1}'): ScalarToken(1, 8, 9, '{"id": 1}')},
        0,
        10,
        '{"id": 1}',
    )

# Generated at 2022-06-14 14:51:27.643023
# Unit test for function tokenize_json
def test_tokenize_json():
    content = r"""
{
  "name": "John Doe",
  "items": [
    "pencil", "pen", "paper", "eraser"
  ],
  "attributes": {
    "email": "johndoe@example.com",
    "age": 30
  },
  "isHappy": true,
  "account-balance": 100
}
"""
    token = tokenize_json(content)


# Generated at 2022-06-14 14:51:30.446620
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{'name': 'Charles', 'age': 56}"
    token = tokenize_json(content)
    assert {'name': 'Charles', 'age': 56} == token

# Generated at 2022-06-14 14:51:47.673415
# Unit test for function tokenize_json
def test_tokenize_json():
    str1 = '{"a":"b", "c":1}'
    str2 = "['this', 'is', 'an', 'array']"
    token1 = tokenize_json(str1)
    assert token1.type == "dict"
    assert token1.keys() == ["a", "c"]
    assert token1.values() == ["b", 1]
    assert isinstance(token1.keys()[0], ScalarToken)
    assert isinstance(token1.values()[0], ScalarToken)

    token2 = tokenize_json(str2)
    assert token2.type == "list"
    assert token2.values() == ['this', 'is', 'an', 'array']
    assert isinstance(token2.values()[0], ScalarToken)

# Generated at 2022-06-14 14:51:58.492510
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:52:00.971172
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a":1, "b":[1, 2]}')
    assert token.value == {'a': 1, 'b': [1, 2]}


# Generated at 2022-06-14 14:52:12.487057
# Unit test for function tokenize_json
def test_tokenize_json():
    valid_data = '{"key": "value"}'
    result = tokenize_json(valid_data)
    assert isinstance(result, DictToken)
    assert result.data == {ScalarToken("key"): ScalarToken("value")}
    assert result.start == 0
    assert result.end == len(valid_data) - 1
    assert result.content == valid_data
    # bad data
    invalid_data = '{"key: "value"}'
    try:
        tokenize_json(invalid_data)
        assert False, "should not be able to construct an invalid JSON object."
    except (ParseError, JSONDecodeError):
        pass


# Generated at 2022-06-14 14:52:18.518027
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('[{"a": 1}, {"a": 2}]')
    assert isinstance(token, ListToken)
    assert len(token.value) == 2
    for item in token.value:
        assert isinstance(item, DictToken)
        assert len(item.value) == 1
        for key, value in item.value.items():
            assert key == "a"
            assert value.value == 1 or value.value == 2



# Generated at 2022-06-14 14:52:28.197234
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:52:34.347524
# Unit test for function tokenize_json
def test_tokenize_json():

    content = """
    {
        "type": "string",
        "format": "uri"
    }
    """

    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.to_native() == {
        "format": "uri",
        "type": "string",
    }

# Unit tests for _TokenizingJSONObject

# Generated at 2022-06-14 14:52:42.623360
# Unit test for function tokenize_json
def test_tokenize_json():
    test_schema = Schema([
            Field(name="name", required=True),
            Field(name="price", type="integer", description="Price in cents")])
    test_json_obj = {
        "name": "Foo",
        "price": "50"
    }
    test_json = json.dumps(test_json_obj)
    tokenized_json = tokenize_json(test_json)
    expected_result = tokenized_json.value
    actual_result = test_schema.validate(tokenized_json)
    assert expected_result == actual_result


# Generated at 2022-06-14 14:52:54.228969
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test empty string
    with pytest.raises(ParseError, match="No content"):
        tokenize_json("")

    # Test whitespace
    with pytest.raises(ParseError, match="No content"):
        tokenize_json("\n  ")

    # Test invalid json
    with pytest.raises(ParseError, match="Expecting value"):
        tokenize_json("nullnull")

    # Test valid json
    token = tokenize_json('{"alpha": "beta", "gamma": "delta"}')
    assert token.start_position.line_no == 1
    assert token.start_position.column_no == 1
    assert token.end_position.line_no == 1
    assert token.end_position.column_no == 35

    # Test json with comments


# Generated at 2022-06-14 14:53:03.462447
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a": 1}') == {'a': 1}
    assert tokenize_json(b'{"a": 1}') == {'a': 1}
    assert tokenize_json('{"a": 1.0}') == {'a': 1.0}
    assert tokenize_json('{"a": 1e10}') == {'a': 1e10}
    assert tokenize_json('{"a": null}') == {'a': None}
    assert tokenize_json('{"a": true}') == {'a': True}
    assert tokenize_json('{"a": false}') == {'a': False}

# Generated at 2022-06-14 14:53:12.336522
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name":"value"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value == {'name': 'value'}
    with pytest.raises(ParseError):
        content = '{"name":"value}'
        token = tokenize_json(content)


# Generated at 2022-06-14 14:53:24.448036
# Unit test for function tokenize_json
def test_tokenize_json():
    import sys
    import json

    def _test(jsonstr: str, content: str) -> None:
        sys.stdout.write("\n%s\n" % jsonstr)
        token = tokenize_json(jsonstr)
        value = token.value
        # Ensure that the embedded content is the same as the original input.
        assert token.content == content
        # Ensure that the tokenized value can be serialized back to a string.
        # This is the best way to test the parsing of the original JSON.
        expected = json.loads(jsonstr)
        jsonstr = json.dumps(value)
        assert json.loads(jsonstr) == expected


# Generated at 2022-06-14 14:53:32.200850
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.schemas import Schema, String, Integer
    from typesystem.errors import Error, ValidationError

    class MySchema(Schema):
        name          = String(min_length=1, max_length=20)
        occupation    = String()
        age           = Integer()

    json = '{"name":"Bob", "occupation":"Farmer", "age":32}'

    (result, errors) = validate_json(json, MySchema)

    assert isinstance(errors, list) and len(errors) == 0



# Generated at 2022-06-14 14:53:38.882578
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": true, "b": ["c", "d"], "e": {"k": 1}, "f": null}')
    assert isinstance(token, DictToken)
    assert token.value["a"].value is True
    assert token.value["b"].value[1].value == "d"
    assert isinstance(token.value["e"].value["k"], ScalarToken)
    assert token.value["e"].value["k"].value == 1
    assert token.value["f"].value is None

# Generated at 2022-06-14 14:53:50.049739
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("[]") == [], "Tokenizes json to lists"
    assert tokenize_json("[true]") == [True], "Tokenizes json to lists of primitives"
    assert tokenize_json("[1]") == [1], "Tokenizes json to lists of primitives"
    assert tokenize_json("[1.1]") == [1.1], "Tokenizes json to lists of primitives"
    assert tokenize_json("[1.1e10]") == [1.1e10], "Tokenizes json to lists of primitives"
    assert tokenize_json("[null]") == [None], "Tokenizes json to lists of primitives"
    assert tokenize_json("{}") == {}, "Tokenizes json to dicts"

# Generated at 2022-06-14 14:53:53.491828
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{\"a\": 1, \"b\": {\"c\": 2}}") == tokenize_json(
        b"{\"a\": 1, \"b\": {\"c\": 2}}"
    )



# Generated at 2022-06-14 14:54:03.952864
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "name": "John Smith",
        "age": 21,
        "favorites": [
            "Cats",
            "Dogs",
            "Bunnies"
        ]
    }
    """
    token = tokenize_json(content)

    assert type(token) == DictToken
    assert token.start_pos.char_index == 4
    assert token.end_pos.char_index == 142

# Generated at 2022-06-14 14:54:10.051338
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json("[]"), ListToken)
    assert isinstance(tokenize_json("{}"), DictToken)
    assert tokenize_json('"foo"') == ScalarToken("foo", 0, 4, '"foo"')
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")



# Generated at 2022-06-14 14:54:22.027847
# Unit test for function tokenize_json
def test_tokenize_json():
    t = tokenize_json('[{"a":1}, {"b":2}]')
    assert isinstance(t, ListToken)
    assert len(t.value) == 2
    assert isinstance(t.value[0], DictToken)
    assert isinstance(t.value[1], DictToken)
    assert t.value[0].value.get("a") == 1
    assert t.value[1].value.get("b") == 2

    t = tokenize_json('[{"a":1}, {"a":2}]')
    errors = validate_with_positions(token=t, validator=List())
    assert isinstance(errors.value, list)
    assert len(errors.value) == 1
    assert isinstance(errors.value[0], ValidationError)

# Generated at 2022-06-14 14:54:33.123446
# Unit test for function tokenize_json
def test_tokenize_json():

    assert tokenize_json("no content").value == None
    assert tokenize_json("{}").kind == "dict"
    assert tokenize_json("[]").kind == "list"
    assert tokenize_json("42").kind == "scalar"
    assert tokenize_json('"hello"').kind == "scalar"
    assert tokenize_json("null").kind == "scalar"

    # Error cases
    try:
        tokenize_json("{x: 2}")
    except ParseError as exc:
        assert exc.position.line_no == 1
        assert exc.position.column_no == 3
    else:
        assert False, "JSONDecodeError not raised"


# Generated at 2022-06-14 14:54:39.319744
# Unit test for function tokenize_json
def test_tokenize_json():
    # Already tested through validate_json, not necessary to test
    ...

# Implemented by inspecting source code

# Generated at 2022-06-14 14:54:52.622307
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('[{"x": "abc", "y": "def"}]')
    assert isinstance(token, ListToken)

    token = tokenize_json('[{"x": "abc", "y": "def"}]')
    assert token.children[0].children[0].name == "x"
    assert token.children[0].children[0].children[0].value == "abc"
    assert token.children[0].children[1].name == "y"
    assert token.children[0].children[1].children[0].value == "def"

    # We can validate directly against the token
    validator = Field(name="my_field", type="string")
    value, error_messages = validator.validate(token.children[0].children[0])
    assert value == "abc"


# Generated at 2022-06-14 14:55:01.162750
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = """{
        "id": "a",
        "schema": [
            {
                "key": "a",
                "name": "a",
                "type": "number"
            }
        ],
        "rows": [
            {
                "a": 1
            }
        ]
    }"""
    token = tokenize_json(json_string)
    expect = {'id': 'a', 'schema': [{'key': 'a', 'name': 'a', 'type': 'number'}], 'rows': [{'a': 1}]}
    assert token.value == expect

# Generated at 2022-06-14 14:55:12.583242
# Unit test for function tokenize_json