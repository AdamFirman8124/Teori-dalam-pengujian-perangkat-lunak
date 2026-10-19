

# Generated at 2022-06-14 14:45:35.018240
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(
        '{ "test": { "test": { "test": [ { "test": 123 } ] } } }'
    )
    assert isinstance(token, DictToken)
    assert token.token_type == "dict"
    assert isinstance(token.value, dict)
    key_token = token.value.keys()
    assert key_token and isinstance(key_token, ScalarToken)
    assert key_token.value == "test"
    value_token = token.value.values()
    assert value_token and isinstance(value_token, DictToken)
    assert isinstance(value_token.value, dict)
    nested_key_token = value_token.value.keys()
    assert nested_key_token and isinstance(nested_key_token, ScalarToken)

# Generated at 2022-06-14 14:45:46.580495
# Unit test for function tokenize_json
def test_tokenize_json():
    test = '{"last_name": "Doe", "age": 30, "first_name": "John", "gender": null}'

# Generated at 2022-06-14 14:45:56.026587
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test empty string
    try:
        tokenize_json("")
        assert False
    except ParseError as exc:
        assert exc.reason == "No content."

    # Test wrong format
    try:
        tokenize_json("{")
        assert False
    except ParseError as exc:
        assert exc.reason == "Expecting value."

    # Test wrong format
    try:
        tokenize_json("[]")
        assert False
    except ParseError as exc:
        assert exc.reason == "Expecting value."

    # Test wrong format
    try:
        tokenize_json("[1, 2, 3,]")
        assert False
    except ParseError as exc:
        assert exc.reason == "Expecting value."

    # Test wrong format

# Generated at 2022-06-14 14:46:03.400975
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('"hello"') == ScalarToken(value='hello', start=0, end=6, content='"hello"')
    assert tokenize_json('true') == ScalarToken(value=True, start=0, end=4, content='true')
    assert tokenize_json('false') == ScalarToken(value=False, start=0, end=5, content='false')
    assert tokenize_json('[]') == ListToken(value=[], start=0, end=1, content='[]')
    assert tokenize_json('{}') == DictToken(value={}, start=0, end=1, content='{}')
    assert tokenize_json('null') == ScalarToken(value=None, start=0, end=4, content='null')

# Generated at 2022-06-14 14:46:08.008855
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"foo": "Test"}') == DictToken({
        ScalarToken('foo', 1, 3, '{"foo": "Test"}'): ScalarToken('Test', 10, 14,
                                                                  '{"foo": "Test"}')
    }, 0, 14, '{"foo": "Test"}')

# Generated at 2022-06-14 14:46:18.043629
# Unit test for function tokenize_json
def test_tokenize_json():
    # String
    assert isinstance(tokenize_json("\"2019-09-17 02:35:14.639\""), ScalarToken)
    # Null/empty string
    assert isinstance(tokenize_json("null"), ScalarToken)
    assert isinstance(tokenize_json(""), ScalarToken)
    try:
        tokenize_json("")
    except ParseError as err:
        assert err.text == "No content."
        assert err.code == "no_content"
        assert err.position.column_no == 1
        assert err.position.line_no == 1
        assert err.position.char_index == 0
    # Float
    assert isinstance(tokenize_json("1.0"), ScalarToken)
    # Dict

# Generated at 2022-06-14 14:46:19.923412
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{ "name": "foo" }'
    token = tokenize_json(content)

# Generated at 2022-06-14 14:46:28.884984
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a": 1}') == DictToken({ScalarToken('a', 1, 2): ScalarToken(1, 5, 5)}, 0, 9, '{"a": 1}')
    assert tokenize_json(b'{"a": 1}') == DictToken({ScalarToken('a', 1, 2): ScalarToken(1, 5, 5)}, 0, 9, '{"a": 1}')
    assert tokenize_json('{"a": 1.1}') == DictToken({ScalarToken('a', 1, 2): ScalarToken(1.1, 5, 7)}, 0, 10, '{"a": 1.1}')

# Generated at 2022-06-14 14:46:33.586928
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a":1, "b": 2 }') == {
        'a': ScalarToken(1, 2, 3, '{"a":1, "b": 2 }'),
        'b': ScalarToken(2, 9, 10, '{"a":1, "b": 2 }'),
    }


# Generated at 2022-06-14 14:46:43.496499
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"a": 1}') == {"a": 1}
    assert tokenize_json('{"a": [1,2,3], "b": [4,5,6]}') == {"a": [1, 2, 3], "b": [4, 5, 6]}
    assert tokenize_json('{"a": "hello", "b": true, "c": false, "d": null, "e": 1}') == {"a": "hello", "b": True, "c": False, "d": None, "e": 1}
    assert tokenize_json('{"a": 1.0}') == {"a": 1.0}
    assert tokenize_json('{"a": 1e-10}') == {"a": 1e-10}

# Generated at 2022-06-14 14:46:57.620263
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken
    # basic types
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")
    assert tokenize_json("123") == ScalarToken(123, 0, 2, "123")
    assert tokenize_json('"hello"') == ScalarToken("hello", 1, 6, '"hello"')
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    # list

# Generated at 2022-06-14 14:47:04.424284
# Unit test for function tokenize_json
def test_tokenize_json():
    assert (tokenize_json(b'') == "")
    assert (tokenize_json("") == "")
    assert (tokenize_json("{'name': 'John'}") == "")
    assert (tokenize_json(b"{'name': 'John'}") == "")
    assert (
        tokenize_json(
            b'{"name": "John", "age": 30, "city": "New York"}'
        )
        == "success"
    )



# Generated at 2022-06-14 14:47:08.876661
# Unit test for function tokenize_json
def test_tokenize_json():
    valid_json = '{"hello": "world"}'
    expected_token = DictToken({"hello": "world"}, 0, 21, valid_json)
    actual_token = tokenize_json(valid_json)
    assert actual_token == expected_token


# Generated at 2022-06-14 14:47:14.535116
# Unit test for function tokenize_json
def test_tokenize_json():
    # Arrange
    content = '{"pk":{"S":"mypk"}}'
    expected_items = [
        ("pk", {
            "S": "mypk"
            })
        ]

    # Act
    tokenized_content = tokenize_json(content)

    # Assert
    assert len(tokenized_content) == len(expected_items)
    assert tokenized_content == {
        "pk": {
            "S": "mypk"
            }
        }


# Generated at 2022-06-14 14:47:26.219077
# Unit test for function tokenize_json
def test_tokenize_json():
    test_content = """
        {
            "foo": "bar"
        }
        """

    try:
        token = tokenize_json(test_content)
    except ParseError as exc:
        assert exc.text == "Unexpected '}' in the middle of an object.", (
            "Unexpected exception."
        )
    else:
        assert False, "Exception not raised."

    test_content = """
        {
            "foo": "bar"
        }
        """
    try:
        token = tokenize_json(test_content)
    except ParseError as exc:
        assert exc.text == "Unexpected '}' in the middle of an object.", (
            "Unexpected exception."
        )
    else:
        assert False, "Exception not raised."


# Generated at 2022-06-14 14:47:27.502596
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")



# Generated at 2022-06-14 14:47:39.052455
# Unit test for function tokenize_json
def test_tokenize_json():
    value = 0
    assert tokenize_json("0").value == value

    value = ""
    assert tokenize_json('""').value == value

    value = True
    assert tokenize_json("true").value == value

    value = False
    assert tokenize_json("false").value == value

    value = None
    assert tokenize_json("null").value == value

    value = []
    assert tokenize_json("[]").value == value

    value = [1, 2, 3]
    assert tokenize_json("[1, 2, 3]").value == value

    value = {"a": 1, "b": 2}
    assert tokenize_json('{"a": 1, "b": 2}').value == value

    value = {"a": [1, 2, 3]}

# Generated at 2022-06-14 14:47:45.367548
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": "A", "b": "B"}'
    token = tokenize_json(content)
    assert token.value == {"a": "A", "b": "B"}
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.content == content
    assert token[0].value == 'a'
    assert token[1].value == 'A'
    assert token[2].value == 'b'
    assert token[3].value == 'B'
    assert token[4].value == '}'


# Generated at 2022-06-14 14:47:55.888245
# Unit test for function tokenize_json
def test_tokenize_json():
    input_json_string = """{
        "a": [
            1,
            2,
            3
        ],
        "b": {
            "b1": {
                "bb": true,
                "bbb": "hello"
            }
        }
    }"""
    token = tokenize_json(input_json_string)
    assert token.v == {
        "a": [1, 2, 3],
        "b": {"b1": {"bb": True, "bbb": "hello"}},
    }
    assert token.type == "dict"
    assert token.start_pos == (1, 0)
    assert token.end_pos == (11, 24)

    input_json_string2 = '{"a":"b"}'
    token2 = tokenize_json(input_json_string2)

# Generated at 2022-06-14 14:47:59.345970
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a":"b"}'
    token = tokenize_json(content)
    assert token == tokenize_json(content)


# Generated at 2022-06-14 14:48:08.290556
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": {"b": [1, 2, [3, 4]]}}'
    token = tokenize_json(content=content)
    expected_token = {
        'a': {
            'b': [
                1, 
                2, 
                [
                    3, 
                    4
                ]
            ]
        }
    }
    assert token == expected_token



# Generated at 2022-06-14 14:48:20.834527
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class SimpleSchema(Schema):
        name = String(max_length=10)

    schema = SimpleSchema()

    content = "Hello, World!"
    token = tokenize_json(content)
    assert token == {"name": "Hello, World!"}

    try:
        validate_json(content, schema)
    except ValidationError as exc:
        error_messages = exc.messages
        # Expected error to be unmatched Token object
        assert len(error_messages) == 1
        message = error_messages[0]

        assert message.code == "unmatched"
        assert message.text == "Unmatched JSON."

# Generated at 2022-06-14 14:48:30.740275
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Tests the json decoder which is responsible for returning a tree of
    Token objects that can be validated by the typesystem.
    """
    assert tokenize_json("42") == ScalarToken(42, 0, 1, "42")
    assert tokenize_json('"banana"') == ScalarToken("banana", 0, 8, '"banana"')
    assert tokenize_json('["banana", "kiwi"]') == ListToken(
        [
            ScalarToken("banana", 1, 8, '"banana"'),
            ScalarToken("kiwi", 11, 16, '"kiwi"'),
        ],
        0,
        19,
        '["banana", "kiwi"]',
    )

# Generated at 2022-06-14 14:48:42.862217
# Unit test for function tokenize_json
def test_tokenize_json():
    assert dict(tokenize_json('{"foo": "bar"}')) == {"foo": "bar"}
    assert list(tokenize_json('[1, 2, 3]')) == [1, 2, 3]
    assert tokenize_json('null') == None
    assert tokenize_json('true') == True
    assert tokenize_json('false') == False
    assert tokenize_json('1.1') == 1.1
    assert tokenize_json('2.2e3') == 2.2e3
    assert tokenize_json('1.1e+3') == 1.1e3
    assert tokenize_json('1.1e-3') == 1.1e-3
    assert tokenize_json('-1') == -1
    assert tokenize_json('0') == 0


# Generated at 2022-06-14 14:48:46.181779
# Unit test for function tokenize_json
def test_tokenize_json():
    assert (
        tokenize_json('{"a":"b"}')
        == {'a': 'b'}
    )

# Unit tests for function validate_json

# Generated at 2022-06-14 14:48:58.701842
# Unit test for function tokenize_json
def test_tokenize_json():

    # Did not change anything here
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")
    assert tokenize_json('"foo"') == ScalarToken("foo", 0, 5, '"foo"')
    assert tokenize_json("42") == ScalarToken(42, 0, 2, "42")
    assert tokenize_json("3.14") == ScalarToken(3.14, 0, 4, "3.14")
    assert tokenize_json("[1]") == ListToken([ScalarToken(1, 1, 2, "1")], 0, 3, "[1]")

# Generated at 2022-06-14 14:49:06.837276
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:49:18.860277
# Unit test for function tokenize_json
def test_tokenize_json():
    def t(content: str, expected: str) -> None:
        token = tokenize_json(content)
        assert repr(token) == expected
    t('{"a": 1, "b":true}', 'DictToken([ScalarToken(True, 12, 16)], 1, 16)')
    t('{"a": 1, "b":true, "c":[1,2,3]}', 'DictToken([ScalarToken(True, 12, 16), ListToken([ScalarToken(3, 31, 32)], 23, 32)], 1, 32)')

# Generated at 2022-06-14 14:49:24.543785
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{\"name\": \"Saurabh\"}") == DictToken({
        'name': ScalarToken('Saurabh', 21, 29, '{\"name\": \"Saurabh\"}')
    }, 0, 29, '{\"name\": \"Saurabh\"}')



# Generated at 2022-06-14 14:49:29.736869
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{\"key\": [23, [\"item 1\", 42]]}"
    expected_token = DictToken(
        {
            ScalarToken("key", 1, 5, content): ListToken(
                [
                    ScalarToken(23, 11, 13, content),
                    ListToken(
                        [
                            ScalarToken("item 1", 17, 24, content),
                            ScalarToken(42, 26, 28, content),
                        ],
                        15,
                        29,
                        content,
                    ),
                ],
                8,
                30,
                content,
            )
        },
        0,
        31,
        content,
    )
    assert tokenize_json(content) == expected_token


# Generated at 2022-06-14 14:49:43.125996
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json("""{"foo": 1}""") == DictToken({"foo": 1}, 0, 9, """{"foo": 1}""")
    assert tokenize_json("""[1, 2, 3]""") == ListToken([1, 2, 3], 0, 9, """[1, 2, 3]""")
    assert tokenize_json("""{"foo": [1, 2, 3]}""") == DictToken(
        {"foo": [1, 2, 3]}, 0, 17, """{"foo": [1, 2, 3]}"""
    )


# Generated at 2022-06-14 14:49:48.629670
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a": 1, "b": 2}') == DictToken({ScalarToken('a', 0, 1, '{"a": 1, "b": 2}') : ScalarToken(1, 5, 5, '{"a": 1, "b": 2}'), ScalarToken('b', 8, 9, '{"a": 1, "b": 2}') : ScalarToken(2, 13, 13, '{"a": 1, "b": 2}')}, 0, 18, '{"a": 1, "b": 2}')

# Generated at 2022-06-14 14:49:59.788018
# Unit test for function tokenize_json
def test_tokenize_json():
    """test the json_schema_validation.tokenize_json function"""
    import json
    import pytest

    # Should raise a ParseError if no content is given.
    with pytest.raises(ParseError):
        tokenize_json("")

    # Test with a bad json string.
    with pytest.raises(ParseError) as exc_info:
        tokenize_json("[1,2,3")
    assert exc_info.value.code == "parse_error"

    # Test with a valid json string.
    result = tokenize_json("[1,2,3]")
    assert isinstance(result, ListToken)
    assert result.value == [1, 2, 3]

    # Test decoding with a unicode string.

# Generated at 2022-06-14 14:50:06.552803
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo": 42, "bar": "baz", "qux": null, "quux": ["corge", "grault"]}'
    token = tokenize_json(content)
    assert token.start == 0
    assert token.end == len(content) - 1
    assert token.get_value("foo").value == 42
    assert token.as_dict()["foo"] == 42

# Generated at 2022-06-14 14:50:16.390890
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken(
        value={}, position_start=0, position_end=1, content="{}"
    )
    assert tokenize_json("[]") == ListToken(
        value=[], position_start=0, position_end=1, content="[]"
    )
    assert tokenize_json("{a: true}") == DictToken(
        value={"a": True}, position_start=0, position_end=10, content="{a: true}"
    )
    assert tokenize_json("[1, 2.0, \"a\"]") == ListToken(
        value=[1, 2.0, "a"], position_start=0, position_end=14, content="[1, 2.0, \"a\"]"
    )
    assert tokenize_json

# Generated at 2022-06-14 14:50:20.132650
# Unit test for function tokenize_json
def test_tokenize_json():
    string = '{"key":"val"}'
    token_str = tokenize_json(string)
    assert token_str == DictToken({"key": ScalarToken("val", 3, 8, string)}, 0, 11, string)

# Generated at 2022-06-14 14:50:25.361736
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "age": 10,
        "name": "Alice",
        "cities": ["London", "San Francisco"]
    }
    """
    expected = {
        "age": 10,
        "name": "Alice",
        "cities": ["London", "San Francisco"],
    }
    assert tokenize_json(content) == expected

# Generated at 2022-06-14 14:50:32.803190
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json('{"field":"ok"}'), DictToken)
    assert isinstance(tokenize_json('["field","ok"]'), ListToken)
    assert isinstance(tokenize_json('{"field":null}'), DictToken)
    assert isinstance(tokenize_json('{"field":true}'), DictToken)
    assert isinstance(tokenize_json('{"field":false}'), DictToken)
    assert isinstance(tokenize_json('{"field":1.0}'), DictToken)
    assert isinstance(tokenize_json('{"field":1}'), DictToken)
    assert isinstance(tokenize_json('{"field":-1}'), DictToken)
    assert isinstance(tokenize_json('{"field":1.0E-2}'), DictToken)
    assert isinstance

# Generated at 2022-06-14 14:50:42.644677
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": 1, "b": [1, 2, 3]}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert isinstance(token.children[0], ScalarToken)
    assert token.children[0].value == 1
    assert isinstance(token.children[1], ListToken)
    assert token.children[1].children[0].value == 1
    assert token.children[1].children[1].value == 2
    assert token.children[1].children[2].value == 3

    content = '{"a": 1, "b": [1, 2, 3}'
    with pytest.raises(ParseError) as err:
        tokenize_json(content)

# Generated at 2022-06-14 14:50:46.415437
# Unit test for function tokenize_json
def test_tokenize_json():
    raw_json_string = '{"test_key":"test_value"}'
    token = tokenize_json(raw_json_string)
    assert isinstance(token, DictToken)
    assert token.value['test_key'].value == 'test_value'
    assert token.value['test_key'].start == 16
    assert token.value['test_key'].end == 29



# Generated at 2022-06-14 14:50:59.961274
# Unit test for function tokenize_json
def test_tokenize_json():
    def check_position(pos_str, line, col, char):
        assert pos_str.column_no == col
        assert pos_str.line_no == line
        assert pos_str.char_index == char

    # Test error codes
    json_str = ""
    try:
        token = tokenize_json(json_str)
    except ParseError as err:
        assert err.code == "no_content"
        check_position(err.position, 1, 1, 0)

    json_str = "'foobar'"
    try:
        token = tokenize_json(json_str)
    except ParseError as err:
        assert err.code == "parse_error"
        check_position(err.position, 1, 1, 1)

    # Test parsing

# Generated at 2022-06-14 14:51:04.309803
# Unit test for function tokenize_json
def test_tokenize_json():
    text='''{
        "name": "John"
    }'''
    tokenized=tokenize_json(text)
    # pprint.pprint(tokenized)
    print(tokenized)

    # print(tokenized.__dict__)
    # print(tokenized.value["name"])



# Generated at 2022-06-14 14:51:11.068084
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name":"Bob","age":34}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.position.char_index == 0
    assert token.end.char_index == 20
    assert token.value["name"] == "Bob"
    assert token.value["age"] == 34
    assert token.content == content



# Generated at 2022-06-14 14:51:16.151351
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": 1, "b": 2, "c": [3, 4, 5]}')

# Generated at 2022-06-14 14:51:16.849424
# Unit test for function tokenize_json
def test_tokenize_json():
    pass



# Generated at 2022-06-14 14:51:20.063434
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo":"bar","baz":2}'
    token = tokenize_json(content)
    assert type(token) is DictToken


# Generated at 2022-06-14 14:51:22.547015
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == {"": {}}
    assert tokenize_json("[]") == {"": []}



# Generated at 2022-06-14 14:51:24.840707
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"abc": "def"}') == DictToken({'abc': ScalarToken('def')})

# Generated at 2022-06-14 14:51:28.650966
# Unit test for function tokenize_json
def test_tokenize_json():
    res = tokenize_json('{"a":1}')
    assert res == {'a': 1}
    res = tokenize_json('{"a":[1,2,3]}')
    assert res == {'a': [1, 2, 3]}


# Generated at 2022-06-14 14:51:38.760930
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a": "b"}') == DictToken({'a': 'b'},0,9,'{"a": "b"}')
    assert tokenize_json('{"a": "b", "c": "d"}') == DictToken({'a': 'b', 'c': 'd'},0,19,'{"a": "b", "c": "d"}')
    assert tokenize_json('{"a": {"b": "c"}}') == DictToken({'a': DictToken({'b': 'c'},7,14,'{"b": "c"}')},0,16,'{"a": {"b": "c"}}')

# Generated at 2022-06-14 14:51:48.556657
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"test": 123}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert isinstance(token.items, list)
    assert len(token.items) == 1
    key_token, value_token = token.items[0]
    assert isinstance(key_token, ScalarToken)
    assert key_token.value == "test"
    assert isinstance(value_token, ScalarToken)
    assert value_token.value == 123



# Generated at 2022-06-14 14:51:53.594475
# Unit test for function tokenize_json
def test_tokenize_json():
    input = "{\"array\":[1,2,3],\"boolean\":true,\"null\":null,\"number\":123,\"object\":{\"a\":\"b\",\"c\":\"d\",\"e\":\"f\"},\"string\":\"Hello World\"}"
    output = tokenize_json(input)

# Generated at 2022-06-14 14:51:56.630500
# Unit test for function tokenize_json
def test_tokenize_json():
    try:
        tokenize_json("{}")
    except Exception:
        assert False
    try:
        tokenize_json("{}")
    except Exception:
        assert False



# Generated at 2022-06-14 14:52:04.187684
# Unit test for function tokenize_json
def test_tokenize_json():
    """Compares the tokens produced by tokenize_json against those produced by JSONDecoder
    """
    content = '{"name": "John Doe", "address": {"city": "", "state": "OR"}}'
    decoded_dict = json.loads(content)
    token_dict = tokenize_json(content)
    assert isinstance(token_dict, DictToken)
    assert decoded_dict == token_dict.value
    assert token_dict.inner[0].value == "name"
    assert token_dict.inner[1].value == "John Doe"
    assert isinstance(token_dict.inner[1], ScalarToken)
    assert token_dict.inner[2].value == "address"
    assert isinstance(token_dict.inner[2], ScalarToken)

# Generated at 2022-06-14 14:52:14.658430
# Unit test for function tokenize_json
def test_tokenize_json():
    # JSON content
    data = '{"is_online":false, "name":"John", "age":25, "car":{"make":"Ford", "model":"Fiesta"}}'

    # Content is string
    token = tokenize_json(data)

    # We can access JSON content as Python objects
    assert token.value == {
        "is_online": False,
        "name": "John",
        "age": 25,
        "car": {"make": "Ford", "model": "Fiesta"},
    }

    # Positional information is available on the Python object
    assert token.start_position == (1, 1, 0)
    assert token.end_position == (1, 119, 118)
    assert token.content == data

    # Content is bytes
    token = tokenize_json(data.encode("utf-8"))



# Generated at 2022-06-14 14:52:22.852811
# Unit test for function tokenize_json
def test_tokenize_json():
    # Assert on the token structure
    # Get a token from a json string
    json_string = '{"hello": "world", "price": "10.99"}'
    token = tokenize_json(json_string)
    # Ensure the token type is DictToken
    assert isinstance(token, DictToken)
    # Check the size of the token
    assert len(token) == 2
    # Check the keys of the token
    assert list(token.keys()) == ["hello", "price"]
    # Check the positions of each of the keys
    assert token["hello"].start_position() == Position(column_no=2, line_no=1, char_index=0)
    assert token["hello"].end_position() == Position(column_no=8, line_no=1, char_index=1)

# Generated at 2022-06-14 14:52:30.336948
# Unit test for function tokenize_json
def test_tokenize_json():
    tokenize_json("{}")
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    try:
        tokenize_json("")
    except ParseError as exc:
        assert exc.position.column_no == 1
        assert exc.position.line_no == 1
        assert exc.position.char_index == 0
        assert exc.code == "no_content"
        assert exc.text == "No content."
    else:
        assert False

    try:
        tokenize_json('{"foo": "bar", baz: "qux"}')
    except ParseError as exc:
        assert exc.position.column_no == 26
        assert exc.position.line_no == 1
        assert exc.position.char_index == 25

# Generated at 2022-06-14 14:52:37.036866
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test the tokenize_json function
    assert tokenize_json('{"foo": "bar"}') == DictToken(
        {
            ScalarToken(
                "foo", 0, 4, '{"foo": "bar"}'
            ): ScalarToken(
                "bar", 8, 12, '{"foo": "bar"}'
            )
        },
        0,
        12,
        '{"foo": "bar"}',
    )



# Generated at 2022-06-14 14:52:46.675483
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    json_data: typing.Dict[str, typing.Any] = {
        "one": 1,
        "two": {
            "three": [{"again": "yes"}, {"surprise": "me"}],
            "three3": "3",
            "three5": 3,
            "three7": 3.5,
            "three9": [3, 4, 5],
            "three11": [1, 2, 3.5],
        },
        "four": False,
    }

    json_data_json: str = json.dumps(json_data)

    token = tokenize_json(json_data_json)
    j = json_data
    assert token.value == j
    assert token.start == 0
    assert token.end == len(json_data_json) - 1
   

# Generated at 2022-06-14 14:52:56.580090
# Unit test for function tokenize_json
def test_tokenize_json():
    content = json.dumps({"test": 5})
    token = tokenize_json(content)
    expected_token = DictToken(
        {"test": ScalarToken(5, 17, 19, content)}, 0, 21, content
    )
    assert token == expected_token

    content = json.dumps([1, 2, 3])
    token = tokenize_json(content)

    expected_token = ListToken(
        [ScalarToken(1, 1, 2, content), ScalarToken(2, 4, 5, content), ScalarToken(3, 7, 8, content)],
        0, 10, content
    )
    assert token == expected_token


# Generated at 2022-06-14 14:53:02.589617
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = '{"name" : "Brian"}'
    assert type(tokenize_json(json_string)) == DictToken

# Generated at 2022-06-14 14:53:08.274403
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"a":[1,2,3], "b":2}') == {
        "a": [1, 2, 3],
        "b": 2,
    }

    assert tokenize_json('{"a":[1,2,3], "b":2}') == {
        "a": [1, 2, 3],
        "b": 2,
    }


# Generated at 2022-06-14 14:53:16.070541
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(b"{}")
    assert isinstance(token, DictToken)
    assert token.dict_value == {}

    token = tokenize_json(b"[]")
    assert isinstance(token, ListToken)
    assert token.list_value == []

    token = tokenize_json(b"null")
    assert isinstance(token, ScalarToken)
    assert token.scalar_value is None

    token = tokenize_json(b"1")
    assert isinstance(token, ScalarToken)
    assert token.scalar_value == 1

    token = tokenize_json(b"1.5")
    assert isinstance(token, ScalarToken)
    assert token.scalar_value == 1.5


# Generated at 2022-06-14 14:53:27.463734
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json('{"test":"test"}'), DictToken)
    assert isinstance(tokenize_json('{}'), DictToken)
    assert isinstance(tokenize_json('"string"'), ScalarToken)
    assert isinstance(tokenize_json('123'), ScalarToken)

    expected_err_msg = "Expecting property name enclosed in double quotes"
    with pytest.raises(ParseError) as exc_info:
        tokenize_json('{1: 1}')
    assert exc_info.value.text == expected_err_msg
    assert exc_info.value.position.column_no == 2
    assert exc_info.value.position.line_no == 1

    expected_err_msg = "No content."

# Generated at 2022-06-14 14:53:38.054111
# Unit test for function tokenize_json
def test_tokenize_json():
    print(tokenize_json('{"a": 1, "b": true, "c": "foo", "d": null}'))
    print(tokenize_json('{"a": 1.0}'))
    print(tokenize_json('[1,2,3]'))
    print(tokenize_json(''))
    print(tokenize_json('{"a": 1, "b": true, "c": "foo", "d": null,}'))
    print(tokenize_json('{"a": 1, "b": true, "c": "foo", "d": null,v}'))
    print(tokenize_json('{"a": 1, "b": true, "c": "foo", "d": null,}'))

# Generated at 2022-06-14 14:53:49.233988
# Unit test for function tokenize_json
def test_tokenize_json():
    content = json.loads(
        open("tests/data/example.json", "r").read()
    )  # type: typing.Dict[str, typing.Any]
    token = tokenize_json(content)  # type: Token
    assert token.value == {"sub1": {"subsub1": 1}}

    schema = Schema(
        {
            "sub1": {
                "subsub1": Field(type="integer"),
                "subsub2": Field(type="integer"),
            },
            "sub2": {"subsub1": Field(type="integer")},
        }
    )  # type: Schema

    value, error_messages = validate_json(content, schema)

# Generated at 2022-06-14 14:53:56.581964
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"thing":"stuff"}')
    assert type(token) == DictToken
    assert token.value == {"thing":"stuff"}
    assert token.start_position.line_no == 1
    assert token.start_position.column_no == 1
    assert token.start_position.char_index == 0
    assert token.end_position.line_no == 1
    assert token.end_position.column_no == 17
    assert token.end_position.char_index == 16


# Generated at 2022-06-14 14:54:04.558080
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem import String
    from typesystem.schemas import Schema

    class UserSchema(Schema):
        name = String(max_length=10)

    content = '{"name": "Bob"}'
    token = tokenize_json(content)
    errors = UserSchema.validate(token)
    assert not errors
    assert token == {"name": "Bob"}

    content = '{"name": 1234}'
    token = tokenize_json(content)
    errors = UserSchema.validate(token)
    assert len(errors) == 1
    assert errors[0]["message"] == "Value must be a unicode or string."



# Generated at 2022-06-14 14:54:15.349881
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = '{ "foo": {"bar": [1,2,3]}}'
    token = tokenize_json(json_string)
    assert isinstance(token, DictToken)
    top_level_dict = token.value
    assert "foo" in top_level_dict
    second_level_dict = top_level_dict["foo"]
    assert isinstance(second_level_dict, DictToken)
    assert "bar" in second_level_dict.value
    bar = second_level_dict.value["bar"]
    assert isinstance(bar, ListToken)
    assert [1, 2, 3] == bar.value
    assert "bar" == bar.contents
    assert 15 == bar.start_index
    assert 17 == bar.end_index

# Generated at 2022-06-14 14:54:21.029381
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "name": "email",
        "type": "string"
    }
    """
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert isinstance(token[0], ScalarToken)
    assert isinstance(token[1], ScalarToken)


# Generated at 2022-06-14 14:54:34.322429
# Unit test for function tokenize_json
def test_tokenize_json():
    json_test_string = '{"test": "word", "test2": "word2"}'
    token = tokenize_json(json_test_string)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(json_test_string) - 1
    assert token.content == json_test_string
    assert token.value == {"test": "word", "test2": "word2"}

    json_test_string = '{"test": "word", "test2": "word2"}'
    token = tokenize_json(json_test_string)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(json_test_string) - 1
    assert token.content == json_test_string

# Generated at 2022-06-14 14:54:41.354423
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json('{"hello": "world"}') == DictToken({"hello": "world"}, 0, 19, '{"hello": "world"}')
    assert tokenize_json('{"hello": {"nested": "awesome"}}') == DictToken({"hello": {"nested": "awesome"}}, 0, 33, '{"hello": {"nested": "awesome"}}')
    assert tokenize_json('{"hello": [1,2,3]}') == DictToken({"hello": [1,2,3]}, 0, 19, '{"hello": [1,2,3]}')



# Generated at 2022-06-14 14:54:48.029082
# Unit test for function tokenize_json
def test_tokenize_json():
    assert (
        tokenize_json('{"a": ["b", "c"]}')
        == DictToken({"a": ListToken(["b", "c"])})  # type: ignore
    )
    assert tokenize_json("5") == ScalarToken(5)  # type: ignore
    assert tokenize_json("4.5") == ScalarToken(4.5)  # type: ignore

# Generated at 2022-06-14 14:54:57.345199
# Unit test for function tokenize_json
def test_tokenize_json():
    assert(tokenize_json('{"a":1}') == DictToken({ScalarToken('a'): ScalarToken(1)}, 0, 6))
    assert(tokenize_json('{"b":2}') == DictToken({ScalarToken('b'): ScalarToken(2)}, 0, 6))
    assert(tokenize_json('[1,2,3]') == ListToken([ScalarToken(1), ScalarToken(2), ScalarToken(3)], 0, 6))
    assert(tokenize_json('{"a":{"b": [1, 2]}}') == DictToken({ScalarToken('a'): DictToken({ScalarToken('b'): ListToken([ScalarToken(1), ScalarToken(2)], 8, 16)}, 4, 16)}, 0, 17))

# Generated at 2022-06-14 14:55:02.700061
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(
        content="""\
{
    "name": "Hello world",
    "numbers": [
        100,
        200
    ]
}
"""
    )
    assert token.value == {"name": "Hello world", "numbers": [100, 200]}
    assert token.children["name"].is_leaf
    assert token.children["numbers"].children[0].is_leaf



# Generated at 2022-06-14 14:55:14.277950
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.base import String
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken

    token = tokenize_json('{"a": [1, "b", [true, false]]}')
    assert isinstance(token, DictToken)