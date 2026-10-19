

# Generated at 2022-06-14 14:45:29.430128
# Unit test for function tokenize_json
def test_tokenize_json():
    """Validate that tokenize json with a valid json string returns a token object."""
    json_string = '{ "a": 3, "b": "test" }'
    token_tree = tokenize_json(json_string)
    assert isinstance(token_tree, DictToken)


# Generated at 2022-06-14 14:45:33.391942
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "foo": {
            "bar": [
                1,
                2
            ]
        },
        "a": "b"
    }
    """
    t = tokenize_json(content)
    assert t.value["foo"]["bar"][1].value == 2


# Generated at 2022-06-14 14:45:39.643007
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json('{"foo": "bar"}') == DictToken(
        {"foo": ScalarToken("bar", 7, 11, '{"foo": "bar"}')}, 0, 13, '{"foo": "bar"}'
    )
    with pytest.raises(ParseError):
        tokenize_json("")



# Generated at 2022-06-14 14:45:46.741830
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo": "bar", "baz": [1, 2, 3]}'
    result = tokenize_json(content)
    assert isinstance(result, DictToken)
    assert isinstance(result[0].value, ScalarToken)
    assert result[0].value.value == "bar"
    assert result[1].value[0].value == 1
    assert result[1].value[1].value == 2



# Generated at 2022-06-14 14:45:52.159340
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test valid json
    valid_json_string = '[1, 2, 3]'
    assert tokenize_json(valid_json_string) == [1, 2, 3]

    # Test invalid json
    invalid_json_string = '[1, 2, 3'
    with pytest.raises(ParseError):
        tokenize_json(invalid_json_string)


# Generated at 2022-06-14 14:45:56.925539
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test whitespace - 1
    data = """
    {
        "hello": "world"
    }
    """
    expected = "{'hello': 'world'}"

    try:
        token = tokenize_json(data)
    except ParseError as e:
        if e.code == "parse_error":
            pass
        else:
            assert False, "Unexpected ParseError raised with unexpected code."
    else:
        assert expected == token[0], "Unexpected output."

    # Test whitespace - 2
    data = '{"hello": "world"}'
    expected = "{'hello': 'world'}"

    try:
        token = tokenize_json(data)
    except ParseError as e:
        if e.code == "parse_error":
            pass

# Generated at 2022-06-14 14:46:08.401019
# Unit test for function tokenize_json
def test_tokenize_json():
    print('Running unit test for function tokenize_json')

# Generated at 2022-06-14 14:46:10.991288
# Unit test for function tokenize_json
def test_tokenize_json():
    expected_output = {"name": "typesystem", "version": "0.9.0"}
    assert expected_output == tokenize_json('{"name":"typesystem","version":"0.9.0"}')


# Generated at 2022-06-14 14:46:21.484236
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('"test"') == ScalarToken('test', 0, 5, '"test"')
    assert tokenize_json('{"test": "value"}') == DictToken(
        {ScalarToken('test', 1, 6, '"test"'): ScalarToken('value', 9, 16, '"value"')},
        0, 18, '{"test": "value"}'
    )
    assert tokenize_json('[{"test": "value"}]') == ListToken(
        [DictToken({ScalarToken('test', 2, 7, '"test"'): ScalarToken('value', 10, 17, '"value"')}, 1, 19, '{"test": "value"}')],
        0, 21, '[{"test": "value"}]'
    )

# Generated at 2022-06-14 14:46:29.959452
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test with empty string
    assert tokenize_json("") == ScalarToken(None, 0, 0, "")

    # Test with empty string
    assert tokenize_json(" ") == ScalarToken(None, 1, 1, " ")

    # Test with null
    assert tokenize_json('"null"') == ScalarToken("null", 0, 5, '"null"')

    # Test with boolean (true)
    assert tokenize_json('"true"') == ScalarToken("true", 0, 5, '"true"')

    # Test with boolean (false)
    assert tokenize_json('"false"') == ScalarToken("false", 0, 6, '"false"')

    # Test with number (1)

# Generated at 2022-06-14 14:46:51.619999
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == ScalarToken(None, 0, 0, "")

# Generated at 2022-06-14 14:47:00.080432
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test empty string case.
    try:
        tokenize_json("")
        assert False, (
            "Expected ParseError, but did not raise.",
        )  # pragma: no cover
    except ParseError as exc:
        assert exc.code == "no_content", (
            "Expected error code no_content, actual: {}.".format(exc.code),
        )
        assert exc.text == "No content.", (
            "Expected error text no_content, actual: {}.".format(exc.text),
        )
        assert exc.position == Position(
            column_no=1, line_no=1, char_index=0
        ), "Expected error position (1, 1, 0), actual: {}.".format(exc.position)

    # Test string parsing.
    token = token

# Generated at 2022-06-14 14:47:02.303551
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a": 1}') == DictToken({"a": ScalarToken(1)})



# Generated at 2022-06-14 14:47:11.381164
# Unit test for function tokenize_json
def test_tokenize_json():
    test_json = "{\"foo\": 1}"
    token = tokenize_json(test_json)
    assert isinstance(token, DictToken)
    assert token.keys() == ["foo"]
    assert token["foo"] == 1

    invalid_json = "{\"foo\": 1"
    try:
        token = tokenize_json(invalid_json)
    except ParseError as err:
        assert err.code == "parse_error"
        assert err.position.column_no == 10

    empty_json = ""
    try:
        token = tokenize_json(empty_json)
    except ParseError as err:
        assert err.code == "no_content"

# Generated at 2022-06-14 14:47:17.158630
# Unit test for function tokenize_json
def test_tokenize_json():
    result = tokenize_json('{"a":123,"b":456}')

    assert isinstance(result, Token)
    assert isinstance(result, DictToken)
    assert result.value == {'a': 123, 'b': 456}
    assert result.start_position == (1, 1)
    assert result.end_position == (1, 21)
    assert result.content == '{"a":123,"b":456}'


# Generated at 2022-06-14 14:47:27.992059
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:47:39.678818
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    Fs = FileSystem()
    with Fs.open("/test", "r") as f:
        content = f.read()

# Generated at 2022-06-14 14:47:44.290670
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test parse error (empty string)
    with pytest.raises(ParseError):
        tokenize_json("")

    # Test parse error (non-json)
    with pytest.raises(ParseError):
        tokenize_json("notJSON")

    # Test parse error (missing trailing quote)
    with pytest.raises(ParseError):
        tokenize_json("{")

    # Test basic tokenization
    token_output = tokenize_json("{'a': 'b'}")
    assert token_output.start == 0
    assert token_output.end == 8
    assert token_output.items == {'a': 'b'}

    # Test basic tokenization with positions
    token_output = tokenize_json("{'a': 'b'}")

# Generated at 2022-06-14 14:47:55.419162
# Unit test for function tokenize_json
def test_tokenize_json():
    # String
    assert tokenize_json('"foo"') == ScalarToken("foo", 0, 5, '"foo"')
    # Integer
    assert tokenize_json("123") == ScalarToken(123, 0, 3, "123")
    # Float
    assert tokenize_json("123.456") == ScalarToken(123.456, 0, 7, "123.456")
    # Boolean
    assert tokenize_json("true") == ScalarToken(True, 0, 4, "true")
    # Null
    assert tokenize_json("null") == ScalarToken(None, 0, 4, "null")
    # Bytestring
    assert tokenize_json(b'"foo"') == ScalarToken("foo", 0, 5, '"foo"')
    # Empty string

# Generated at 2022-06-14 14:48:01.856862
# Unit test for function tokenize_json
def test_tokenize_json():
    # Given
    content = """{"name": "John"}"""

    # When
    actual = tokenize_json(content)

    # Then
    assert actual == DictToken(
        {ScalarToken("name", 1, 5, content): ScalarToken("John", 9, 14, content)}, 0, 15, content
    )



# Generated at 2022-06-14 14:48:19.746758
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """{"data": [{"id": 1, "name": "foo"},{"id": 2, "name": "bar"}]}"""
    token = tokenize_json(content)
    assert token.start_index == 0
    assert token.end_index == 89
    assert isinstance(token, DictToken)
    assert token.value["data"].start_index == 6
    assert token.value["data"].end_index == 84
    assert isinstance(token.value["data"], ListToken)
    assert token.value["data"].value[0].start_index == 12
    assert token.value["data"].value[0].end_index == 50
    assert isinstance(token.value["data"].value[0], DictToken)
    assert token.value["data"].value[0].value["id"].start_

# Generated at 2022-06-14 14:48:29.937779
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('') == None
    assert tokenize_json('{}') == DictToken({}, 0, 1, "{}")
    assert tokenize_json('{ "test": 3.14159 }') == DictToken(
        { ScalarToken("test", 2, 7, '"test"'): ScalarToken(3.14159, 12, 19, '3.14159') }, 0, 20, '{ "test": 3.14159 }'
    )
    assert tokenize_json('{ "test": true }') == DictToken(
        { ScalarToken("test", 2, 7, '"test"'): ScalarToken(True, 12, 16, 'true') }, 0, 17, '{ "test": true }'
    )

# Generated at 2022-06-14 14:48:39.773395
# Unit test for function tokenize_json
def test_tokenize_json():
    result = tokenize_json("{}")
    assert isinstance(result, Token)
    assert result.value == {}

    result = tokenize_json("{\"a\": 1, \"b\": \"c\"}")
    assert isinstance(result, Token)
    assert result.value == {"a":1, "b":"c"}

    result = tokenize_json("[1, [2], {\"a\": 3}]")
    assert isinstance(result, Token)
    assert result.value == [1, [2], {"a": 3}]

    result = tokenize_json("null")
    assert isinstance(result, Token)
    assert result.value is None


# Generated at 2022-06-14 14:48:43.789920
# Unit test for function tokenize_json
def test_tokenize_json():
    import typesystem
    token = tokenize_json('{"age": 3}')
    assert(isinstance(token, DictToken))
    assert(isinstance(token.value["age"], ScalarToken))
    assert(token.value["age"].value == 3)


# Generated at 2022-06-14 14:48:52.523713
# Unit test for function tokenize_json
def test_tokenize_json():
    # invalid json
    invalid_json = "{invalid_json:True}"
    with pytest.raises(ParseError):
        tokenize_json(invalid_json)

    # null value
    null_value = '{"a":null}'
    tokenized_null_value = tokenize_json(null_value)
    assert tokenized_null_value.as_dict() == {"a": None}

    # single key value
    single_key_value = '{"a": 1}'
    tokenized_single_key_value = tokenize_json(single_key_value)
    assert tokenized_single_key_value.as_dict() == {"a": 1}

    # double key value
    double_key_value = '{"a": 1, "b": 2}'
    tokenized_double_key_

# Generated at 2022-06-14 14:48:58.799426
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"key1": "value1"}') == DictToken(
        {ScalarToken('key1', 1, 7, '{"key1": "value1"}'): ScalarToken('value1', 10, 18, '{"key1": "value1"}')},
        0, 18, '{"key1": "value1"}'
    )


# Generated at 2022-06-14 14:49:06.908117
# Unit test for function tokenize_json
def test_tokenize_json():
    content = ""
    token = tokenize_json(content)
    assert token == ListToken([], 0, 0, content)

    content = '[{"1":2,"three":null}]'
    token = tokenize_json(content)
    assert token == ListToken(
        [DictToken({ScalarToken('1', 2, 2, content): ScalarToken(2, 6, 6, content),
                    ScalarToken('three', 11, 16, content): ScalarToken(None, 20, 23, content)},
                   1, 24, content)],
        0, 25, content
    )

    content = '["a", "b", 1, "c", false, {"1": 2}, {"3": null}]'
    token = tokenize_json(content)

# Generated at 2022-06-14 14:49:18.957100
# Unit test for function tokenize_json
def test_tokenize_json():
    simple_json = '{"name": "Bob", "age": 20}'
    result, result_end = _TokenizingJSONObject(
        s_and_end=(simple_json, 0),
        strict=True,
        scan_once=_make_scanner(None, simple_json),
        memo={},
        content=simple_json,
    )
    assert result == {"name": "Bob", "age": 20}
    assert result_end == len(simple_json)

    simple_json_with_spaces = '{"name": "Bob", "age": 20 }'

# Generated at 2022-06-14 14:49:21.883295
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"name": "Ankita"}') == {'name': 'Ankita'}


# Generated at 2022-06-14 14:49:27.904223
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
{
    "name": "Dunder Mifflin Paper Company",
    "employees": ["Michael Scott", "Jim Halpert", "Dwight Schrute"],
    "headquarters": {
        "city": "Scranton, PA",
        "state": "Pennsylvania"
    }
}
    """
    token = tokenize_json(content)
    validate_json(content, token)



# Generated at 2022-06-14 14:49:41.208930
# Unit test for function tokenize_json
def test_tokenize_json():
    def asserts(test, expected=None) -> None:
        result = tokenize_json(test)
        if expected is not None:
            assert result == expected
        assert type(result) == type(expected)

    asserts(b"123")
    asserts(b'{"abc": 123, "def": 456}')
    asserts(b'["abc", 123, 456, {"a": "b", "c": "d"}]')
    asserts(b"[[], [1, 2, 3]]")
    asserts(b'{"a": {"b": {"c": {"d": {"e": {"f": {"g": {"h": {"i": "j"}}}}}}}}}')
    asserts(b"{}")
    asserts('["a", "b", "c"]')

# Generated at 2022-06-14 14:49:44.545842
# Unit test for function tokenize_json
def test_tokenize_json():
    json_str = '{"name": "stefan", "age": 42}'
    token = tokenize_json(json_str)
    assert token.value['name'].value == 'stefan'
    assert token.value['age'].value == 42


# Generated at 2022-06-14 14:49:46.881078
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('["foo"]') == ListToken(["foo"], 0, 8, '["foo"]')


# Unit-test for function validate_json

# Generated at 2022-06-14 14:49:52.575092
# Unit test for function tokenize_json
def test_tokenize_json():
    example_dict = {'key1': 'value1', 'key2': 'value2'}
    example_dict_string = '{"key1": "value1", "key2": "value2"}'
    assert tokenize_json(example_dict_string) == example_dict


# Generated at 2022-06-14 14:49:56.824707
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": 1, "b": "c"}')
    assert isinstance(token, DictToken)
    assert isinstance(token[ScalarToken("a")], ScalarToken)
    assert token[ScalarToken("a")].value == 1
    assert isinstance(token[ScalarToken("b")], ScalarToken)
    assert token[ScalarToken("b")].value == "c"



# Generated at 2022-06-14 14:49:59.792932
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"foo": 1}')
    assert isinstance(token, DictToken)
    assert token.value == {"foo": ScalarToken(1, 8, 9, '{"foo": 1}')}


# Generated at 2022-06-14 14:50:12.192534
# Unit test for function tokenize_json
def test_tokenize_json():
    # Check that the tokenizer is tokenizing strings and numbers
    # correctly
    test_json = '{"test": {"value": 24}}'
    test_result = tokenize_json(test_json)
    assert test_result["test"]["value"] == 24
    assert isinstance(test_result["test"]["value"], ScalarToken)
    # Check that the tokenizer is handling empty strings and bytes
    # correctly
    test_json_2 = ""
    test_json_3 = b""
    tokenize_json(test_json_2)
    tokenize_json(test_json_3)
    # Check that the tokenizer is using the correct positions
    test_json_4 = '{"test": {"value": "1", "2":"hello"}}'

# Generated at 2022-06-14 14:50:24.171209
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken
    import json
    import re

    # Invalid JSON
    invalid_json_strings = [
        '{"test":',
        '{"test":,}',
        '{"test": 5',
        '{"test": 5,}',
        '{"test": "junk"}',
        '{"test": "junk",}',
        '{"test": 5.5',
        '{"test": 5.5,}',
        '[{"test": 5.5,]',
        '[5,5,5,5]',
        '[1,2,3,4,5]',
    ]


# Generated at 2022-06-14 14:50:30.922126
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25,
  "address": {
    "streetAddress": "21 2nd Street",
    "city": "New York",
    "state": "NY",
    "postalCode": 10021
  },
  "phoneNumbers": [
    {
      "type": "home",
      "number": "212 555-1234"
    },
    {
      "type": "fax",
      "number": "646 555-4567"
    }
  ]
}
"""
    token = tokenize_json(content)
    assert token.start_position == Position(column_no=1, line_no=2, char_index=0)

# Generated at 2022-06-14 14:50:38.841367
# Unit test for function tokenize_json
def test_tokenize_json():
    # Check for empty strings
    with pytest.raises(ParseError) as excinfo:
        tokenize_json(b"")
        assert "No content." in str(excinfo.value)

    # Check for invalid strings
    with pytest.raises(ParseError) as excinfo:
        tokenize_json(b"garbage string")
        assert "parse_error" in str(excinfo.value)

    # Test valid json
    assert tokenize_json(b'"foo"') == "foo"



# Generated at 2022-06-14 14:50:51.038009
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test case for function tokenize_json
    """
    data = '{"name": "New York", "state" : "NY", "coordinates": [-74.0059, 40.7127]}'
    token = tokenize_json(data)
    assert token.value == {
            'name': 'New York',
            'state': 'NY',
            'coordinates': [-74.0059, 40.7127],
        }


# Generated at 2022-06-14 14:50:55.719280
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '''
    {
        "a": 1,
        "b": "string"
    }
    '''
    assert tokenize_json(content) == {
        "a": 1,
        "b": "string",
    }



# Generated at 2022-06-14 14:50:59.516227
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{ "test": "hello" , "another": "goodbye" }'
    token = tokenize_json(content)
    assert isinstance(token.value, dict)
    assert token.value["test"] == "hello"

# Generated at 2022-06-14 14:51:07.492152
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "david", "age": 24, "languages": ["Python", "JavaScript"]}'
    token = tokenize_json(content)
    assert token == \
        DictToken({
            ScalarToken('name', 19, 24, content): ScalarToken('david', 34, 40, content),
            ScalarToken('age', 43, 46, content): ScalarToken(24, 52, 54, content),
            ScalarToken('languages', 57, 67, content): ListToken(
                [
                    ScalarToken('Python', 78, 84, content),
                    ScalarToken('JavaScript', 87, 98, content)
                ], 77, 99, content
            ),
        }, 0, 99, content)

# Generated at 2022-06-14 14:51:12.673959
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"field1": 4, "field2": "5", "field3": [6,7,8,9] }'
    assert tokenize_json(content) == {
        "field1": 4,
        "field2": "5",
        "field3": [6, 7, 8, 9],
    }



# Generated at 2022-06-14 14:51:20.201983
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    json_string = """\
{
    "a": 1,
    "b": {
        "ba": 11
    },
    "c": [1, 2.1, "3", true, false, null]
}
"""
    out_string = json.dumps(json.loads(json_string), indent=2)
    assert ('\n'.join([line.rstrip() for line in json_string.split('\n')])
            == '\n'.join([line.rstrip() for line in out_string.split('\n')]))
    tokens = json.dumps(tokenize_json(json_string), indent=2)

# Generated at 2022-06-14 14:51:29.660823
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json('{"foo": "bar"}'), DictToken)
    assert isinstance(tokenize_json('{"foo": 1}'), DictToken)
    assert isinstance(tokenize_json('{"foo": [1, "a"]}'), DictToken)
    assert isinstance(tokenize_json('["foo", 1]'), ListToken)
    assert isinstance(tokenize_json('[1, [1, 2]]'), ListToken)
    assert isinstance(tokenize_json('1.1'), ScalarToken)
    assert isinstance(tokenize_json('true'), ScalarToken)
    assert isinstance(tokenize_json('null'), ScalarToken)



# Generated at 2022-06-14 14:51:39.714470
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")
    assert tokenize_json("[true]") == ListToken([ScalarToken(True, 1, 4, "true")], 0, 5, "[true]")
    assert tokenize_json("[{}]") == ListToken([DictToken({}, 1, 2, "{}")], 0, 3, "[{}]")
    assert tokenize_json("[{}]") == ListToken([DictToken({}, 1, 2, "{}")], 0, 3, "[{}]")

# Generated at 2022-06-14 14:51:50.521219
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    This is a unit test for the function tokenize_json
    """
    token = tokenize_json('{"a":1, "b":2, "c":{"a" : 1, "b" : 2, "c" :{"a":3, "b":4}}}')
    assert token.to_dict() == {"a":1, "b":2, "c":{"a" : 1, "b" : 2, "c" :{"a":3, "b":4}}}

    token = tokenize_json('{"a":1, "b":2, "c":[1,2,3,4,5]}')
    assert token.to_dict() == {"a":1, "b":2, "c":[1,2,3,4,5]}

# Generated at 2022-06-14 14:52:00.561128
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:52:15.291838
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"key": "value"}') == {'key': 'value'}
    assert tokenize_json('{"key": "value"}') != {'key': 'value2'}
    assert tokenize_json('{"key": "value"}') != {'key': 'value', 'key2': 'value2'}
    assert tokenize_json('{"key": "value", "key2": "value2"}') == {'key': 'value', 'key2': 'value2'}
    assert tokenize_json('{"key": {"key2": "value2"}}') == {'key': {'key2': 'value2'}}
    assert tokenize_json('{"key": [{"key2": "value2"}]}') == {'key': [{'key2': 'value2'}]}
    assert token

# Generated at 2022-06-14 14:52:19.860860
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "foo"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert len(token.keys) == 1
    assert token.keys[0] == "name"
    assert isinstance(token.values[0], ScalarToken)
    assert token.values[0].value == "foo"



# Generated at 2022-06-14 14:52:24.617177
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    The unit test for function tokenize_json
    """
    try:
        tokenize_json('{"name": "John"}')
        print("unit test for function tokenize_json: passed")
    except:
        print("unit test for function tokenize_json: failed")



# Generated at 2022-06-14 14:52:33.700526
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("""
        {
            "foo": "bar",
            "answer": 42,
            "pi": 3.14,
            "list": [1, 2, 3],
            "subobj": {
                "sublist": [4, 5, 6]
            }
        }
    """)
    print(token)
    print(token.value)
    print(token.value["subobj"].value)
    print(token.value["subobj"].value["sublist"].value)
    assert isinstance(token, DictToken)
    assert token.value["subobj"].value["sublist"].value[2] == 6



# Generated at 2022-06-14 14:52:43.529973
# Unit test for function tokenize_json
def test_tokenize_json():
    """ An unittest for tokenize_json function
    """
    test_content = """
    {
        "string_field": "test string",
        "int_field": 0,
        "float_field": 0.0,
        "bool_field": true,
        "null_field": null
    }
    """
    # Expected Value
    expected_value = {
        "string_field": "test string",
        "int_field": 0,
        "float_field": 0.0,
        "bool_field": True,
        "null_field": None
    }
    # Actual result
    token = tokenize_json(test_content)
    actual_value = token.value
    assert expected_value == actual_value

# Generated at 2022-06-14 14:52:52.371671
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "name": "John",
        "age": 27,
        "is_human": true,
        "favourites": [
            "cheese",
            "burgers"
        ]
    }
    """
    token = tokenize_json(content)
    assert token.start == 0
    assert token.end == len(content)
    assert token.value["name"].value == "John"
    assert token.value["age"].value == 27
    assert token.value["is_human"].value == True
    assert token.value["favourites"].value == ["cheese", "burgers"]



# Generated at 2022-06-14 14:52:55.329563
# Unit test for function tokenize_json
def test_tokenize_json():
  from typesystem import String

  validation_result = validate_json("1234", String())
  assert(validation_result[0] == "1234")



# Generated at 2022-06-14 14:53:02.205699
# Unit test for function tokenize_json
def test_tokenize_json():
    with pytest.raises(ParseError):
        tokenize_json("")
    token = tokenize_json("{}")
    assert isinstance(token, DictToken)
    assert token.value == {}
    token = tokenize_json("[null]")
    assert isinstance(token, ListToken)
    assert token.value == [None]
    token = tokenize_json(r"""{"quotes": "\""}""")
    assert isinstance(token, DictToken)
    assert token.value == {"quotes": "\""}



# Generated at 2022-06-14 14:53:12.479469
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "name": "John Doe",
        "email": "",
        "age": 42,
        "job": null
    }
    """
    token = tokenize_json(content)

# Generated at 2022-06-14 14:53:17.923033
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a":1, "b":2.2, "c":[1,2,"a"], "d":4}'
    token = tokenize_json(content)
    assert token.kind == Token.DICT

# Generated at 2022-06-14 14:53:37.009231
# Unit test for function tokenize_json
def test_tokenize_json():
    json_content = "true"
    token = tokenize_json(json_content)
    assert isinstance(token, ScalarToken)
    assert token.get_value()
    assert token.start_offset == 0
    assert token.end_offset == 3
    assert token.content == "true"

    json_content = '{"test": true}'
    token = tokenize_json(json_content)
    assert isinstance(token, DictToken)
    assert len(token.items) == 1
    assert token.items[0][0].get_value() == "test"
    assert token.items[0][1].get_value()
    assert token.content == json_content
    assert token.start_offset == 0
    assert token.end_offset == 13

    json_content = '[1, 2]'
    token

# Generated at 2022-06-14 14:53:47.997138
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'"hello"') == ScalarToken('hello', 0, 6, '"hello"')

    assert tokenize_json(b'"hello"') == ScalarToken('hello', 0, 6, '"hello"')

    assert tokenize_json(b'"hello\\"world"') == ScalarToken('hello\\"world', 0, 14, '\\"hello\\\\\\"world\\"')

    assert tokenize_json(b'"hello\tworld"') == ScalarToken('hello\tworld', 0, 13, '"hello\\tworld"')

    assert tokenize_json(b'"hello\nworld"') == ScalarToken('hello\nworld', 0, 13, '"hello\\nworld"')


# Generated at 2022-06-14 14:53:49.201142
# Unit test for function tokenize_json
def test_tokenize_json():
    pass


# Generated at 2022-06-14 14:53:56.529547
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test tokenize_json function
    # Test cases
    json_str = "{\"integers\": [1, 2, 3]}"
    json_bytes = b"{\"integers\": [1, 2, 3]}"
    token = tokenize_json(json_str)
    print(token)
    # Test bytes input
    token = tokenize_json(json_bytes)
    print(token)


# Test the function tokenize_json
test_tokenize_json()



# Generated at 2022-06-14 14:54:05.424736
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "id": "1",
        "tenant_id": "1",
        "created_at": "2019-05-01T15:58:55.931955",
        "updated_at": "2019-05-01T15:58:55.931955",
        "version": 1,
        "deleted_at": null,
        "objects": {
            "foo": [
                "a",
                "b"
            ]
        },
        "more": {
            "nested": {
                "objects": [
                    "a",
                    "b"
                ]
            }
        }
    }
    """
    token = tokenize_json(content)
    assert token.value.get("id") == "1"

# Generated at 2022-06-14 14:54:15.734536
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("{}")
    assert isinstance(token, DictToken)
    assert token.value == {}

    token = tokenize_json('"foo"')
    assert isinstance(token, ScalarToken)
    assert token.value == "foo"

    token = tokenize_json("[1, 2, 3]")
    assert isinstance(token, ListToken)
    assert token.value == [1, 2, 3]

    token = tokenize_json("[true, false, null]")
    assert isinstance(token, ListToken)
    assert token.value == [True, False, None]

    token = tokenize_json("123.456")
    assert isinstance(token, ScalarToken)
    assert token.value == 123.456


# Generated at 2022-06-14 14:54:20.220081
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("[1, 2, 3]")
    assert isinstance(token, ListToken)
    assert len(token) == 3
    assert [item.value for item in token] == list(range(1, 4))



# Generated at 2022-06-14 14:54:31.207339
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("false") == ScalarToken("false", 0, 4, "false")
    assert tokenize_json("true") == ScalarToken("true", 0, 3, "true")
    assert tokenize_json("null") == ScalarToken("null", 0, 3, "null")
    assert tokenize_json("1") == ScalarToken(1, 0, 1, "1")
    assert tokenize_json("1.1") == ScalarToken(1.1, 0, 3, "1.1")
    assert tokenize_json("-1") == ScalarToken(-1, 0, 2, "-1")
    assert tokenize_json("-1.1") == ScalarToken(-1.1, 0, 4, "-1.1")

# Generated at 2022-06-14 14:54:35.829355
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json("[1]") == ListToken([ScalarToken(1, 1, 1, "[1]")], 0, 2, "[1]")

# Generated at 2022-06-14 14:54:44.582008
# Unit test for function tokenize_json
def test_tokenize_json():
    # invalid token
    with pytest.raises(ParseError) as exception:
        content = "[1, 2, 3,] "
        tokenize_json(content)
    assert str(exception) == (
        "ParseError: No content. parse_error @ line 1 column 10"
    )

    # invalid json
    with pytest.raises(ParseError) as exception:
        content = "[1, 2, 3, "
        tokenize_json(content)
    assert str(exception) == (
        "ParseError: Expecting ',' delimiter parse_error @ line 1 column 9"
    )

    # empty dict
    content = "{}"
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value == {}

    # simple dict


# Generated at 2022-06-14 14:55:12.175561
# Unit test for function tokenize_json
def test_tokenize_json():
    import sys
    raw_json = '''
{
  "a": [1, 2, 3],
  "b": "hello"
}
'''
    token_dict = tokenize_json(raw_json)
    assert type(token_dict) is DictToken
    assert len(token_dict) == 2
    token_list = token_dict["a"]
    assert type(token_list) is ListToken
    assert len(token_list) == 3
    assert token_list[1] == 2
    token_int = token_list[1]
    assert type(token_int) is ScalarToken
    assert token_int == 2
    token_string = token_dict["b"]
    assert type(token_string) is ScalarToken
    assert token_string == "hello"

    # validation