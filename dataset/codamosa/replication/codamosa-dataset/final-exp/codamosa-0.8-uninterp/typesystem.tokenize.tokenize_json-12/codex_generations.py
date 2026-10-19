

# Generated at 2022-06-14 14:45:30.036224
# Unit test for function tokenize_json
def test_tokenize_json():
    from pprint import pprint

    from typesystem.tokenize.expectation import (
        AndExpectationToken,
        IsExpectationToken,
        OrExpectationToken,
        WithConstraintExpectationToken,
    )

    field = Field(name="first_name", type="string", max_length=10)
    token, _ = validate_json(b'{"first_name": "badger"}', field)
    expected_token = DictToken(
        {
            "first_name": ScalarToken(
                "badger", 2, 13, '{"first_name": "badger"}'
            )
        },
        0,
        16,
        '{"first_name": "badger"}',
    )
    assert isinstance(token, DictToken)
    assert token == expected_

# Generated at 2022-06-14 14:45:32.989509
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"foo": "bar"}') == DictToken({ScalarToken('foo'): ScalarToken('bar')}, 0, len('{"foo": "bar"}') - 1, '{"foo": "bar"}')


# Generated at 2022-06-14 14:45:38.617966
# Unit test for function tokenize_json
def test_tokenize_json():
    with pytest.raises(ParseError, match=r"No content."):
        tokenize_json("")

    with pytest.raises(ParseError, match=r"Expecting value."):
        tokenize_json("{")

    with pytest.raises(ParseError, match=r"Expecting property name enclosed in double quotes."):
        tokenize_json("{")



# Generated at 2022-06-14 14:45:44.438073
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Carol", "age": 42}'
    token = tokenize_json(content)
    assert token.value[0].value == 'name'
    assert token.value[1].value == 'Carol'
    assert token.value[0].start.char_index == 1
    assert token.value[1].start.char_index == 9


# Generated at 2022-06-14 14:45:47.724633
# Unit test for function tokenize_json
def test_tokenize_json():
    s = '"abc"'
    _, end = _TokenizingJSONObject.__wrapped__((s, 1), False, None, None)
    assert end == len(s)

# Generated at 2022-06-14 14:45:56.651920
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test parsing a trivial JSON array
    result = tokenize_json('["a", "b", 123]')
    assert type(result)==ListToken
    assert result.value == ["a", "b", 123]

    # Test parsing a trivial JSON object 
    result = tokenize_json('{"a": "alpha", "beta": 2, "gama": [1, 2, 3]}')
    assert type(result)==DictToken
    assert result.value == {"a": "alpha", "beta": 2, "gama": [1, 2, 3]}
    
    # Test parsing a trivial JSON string
    result = tokenize_json('"Hello, You!"')
    assert type(result)==ScalarToken
    assert result.value == 'Hello, You!'

    # Test parsing a JSON string with a backslash
    result

# Generated at 2022-06-14 14:45:59.857180
# Unit test for function tokenize_json
def test_tokenize_json():
  assert type(tokenize_json('{"a":2}')) is DictToken


# Generated at 2022-06-14 14:46:09.926523
# Unit test for function tokenize_json
def test_tokenize_json():
    result = tokenize_json('{"a":1}')
    assert(result.value['a'] == 1)
    assert(result.value['a'].value == 1)
    assert(result.value['a'].start_char_pos == 5)
    assert(result.value['a'].end_char_pos == 5)
    assert(result.start_char_pos == 0)
    assert(result.end_char_pos == 6)
    assert(result.start_char_pos == result.value['a'].key.start_char_pos)
    assert(result.end_char_pos == result.value['a'].end_char_pos)

    token_a = result.value['a']
    assert(result['a'] == token_a)
    assert(result[0] == token_a)



# Generated at 2022-06-14 14:46:20.562257
# Unit test for function tokenize_json
def test_tokenize_json():
    # Testing empty object
    content = '{}'
    assert tokenize_json(content) == DictToken(value={}, start=0, end=1, content=content)

    # Testing scalar values
    content = '{ "str": "hello", "int": 1, "float": 1.0, "true": true, "false": false, "null": null }'

# Generated at 2022-06-14 14:46:29.321927
# Unit test for function tokenize_json
def test_tokenize_json():
    error1 = "Cannot have key2, key3. key2 must be one of key1. "
    error2 = "Cannot have key3. key3 must be one of key1. "
    error3 = "key3 must be of type str. "
    error4 = "Expected str. got int."
    error5 = "Expected str. got float."
    error6 = "Expected str. got bool."

    print("Basic validation")
    my_schema = Schema(fields={"key1": Field(type=str),
                               "key2": Field(type=str, enum=["key1"])})
    content = '''{
        "key1": "str_value",
        "key2": "key1"
    }'''

    token = tokenize_json(content)

# Generated at 2022-06-14 14:46:44.226745
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")
    assert tokenize_json("false") == ScalarToken(False, 0, 4, "false")
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json("3") == ScalarToken(3, 0, 1, "3")
    assert tokenize_json("3.14") == ScalarToken(3.14, 0, 4, "3.14")

# Generated at 2022-06-14 14:46:54.947442
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('["foo", {"bar":["baz", null, 1.0, 2]}]') == [
        "foo",
        {"bar": ["baz", None, 1.0, 2]},
    ]
    assert tokenize_json('["foo", {"bar":["baz"]}]') == ["foo", {"bar": ["baz"]}]
    assert tokenize_json('{"foo": "bar", "baz": {"bing": "bam"}}') == {
        "foo": "bar",
        "baz": {"bing": "bam"},
    }
    assert tokenize_json('{"foo": "bar", "baz": {"bing": "bam"}},  ') == {
        "foo": "bar",
        "baz": {"bing": "bam"},
    }
    assert token

# Generated at 2022-06-14 14:47:05.502937
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Peter"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    token_value = token.value
    assert isinstance(token_value, dict)
    assert len(token_value) == 1
    assert set(token_value.keys()) == set([ScalarToken("name", 1, 6, content)])
    assert isinstance(token_value[ScalarToken("name", 1, 6, content)], ScalarToken)
    assert token_value[ScalarToken("name", 1, 6, content)].value == "Peter"

    content = '["Peter", "Paul", "Mary"]'
    token = tokenize_json(content)
    assert isinstance(token, ListToken)
    token_value = token.value

# Generated at 2022-06-14 14:47:14.909281
# Unit test for function tokenize_json
def test_tokenize_json():
    # Simple test to ensure that this function is capable discerning between
    # strings, list and dicts.
    content = '[2, 3, "Hello world."]'
    token = tokenize_json(content)
    assert isinstance(token, ListToken)
    assert token.start_pos.line_no == 1
    assert token.end_pos.line_no == 1

    content = '{"key1": "value1", "key2": "value2"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.start_pos.line_no == 1
    assert token.end_pos.line_no == 1


# Generated at 2022-06-14 14:47:26.440492
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:47:28.061297
# Unit test for function tokenize_json
def test_tokenize_json():
    content='{"foo":"bar"}'
    res=tokenize_json(content)
    assert res == {"foo": "bar"}

# Generated at 2022-06-14 14:47:39.779936
# Unit test for function tokenize_json
def test_tokenize_json():
    content_invalid_1 = """ {"name": "Fred", "age": 42 } """
    content_invalid_2 = """ {"name": "Fred", "age": "42" } """
    content_valid_1 = """ { "name": "Fred", "age": 42 } """
    content_valid_2 = """ { "name": "Fred", "age": "42" } """

# Generated at 2022-06-14 14:47:52.209805
# Unit test for function tokenize_json
def test_tokenize_json():
    class PersonSchema(Schema):
        name = Field(type="string")

    # Test successful JSON parsing and corresponding token
    test_content = '{"name": "Bob"}'
    token = tokenize_json(test_content)
    assert token.value == {"name": "Bob"}
    assert isinstance(token, DictToken)
    assert token.start_position == Position(line_no=1, column_no=1, char_index=0)
    assert token.end_position == Position(line_no=1, column_no=16, char_index=15)

    # Test unsuccessful JSON parsing

# Generated at 2022-06-14 14:48:03.656638
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("1") == ScalarToken(1, 0, 0, "1")
    assert tokenize_json("1.1") == ScalarToken(1.1, 0, 2, "1.1")
    assert tokenize_json("1e1") == ScalarToken(10, 0, 2, "1e1")
    assert tokenize_json("'a'") == ScalarToken("a", 0, 3, "'a'")
    assert tokenize_json('"a"') == ScalarToken("a", 0, 3, '"a"')
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")

# Generated at 2022-06-14 14:48:10.910855
# Unit test for function tokenize_json
def test_tokenize_json():
  json_content = '{"key":{"name":"value"}}'
  token = tokenize_json(json_content)
  assert isinstance(token,DictToken)
  assert token.start == 0
  assert token.end == 29
  assert {'key':{'name':'value'}} == token.value
  assert token.content == json_content
  assert token.positions == {
    ('key',): Position(column_no=2, line_no=1, char_index=0),
    ('key', 'name'): Position(column_no=6, line_no=1, char_index=4),
    ('key', 'name',): Position(column_no=6, line_no=1, char_index=4)
  }

# Generated at 2022-06-14 14:48:25.055240
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    import random
    import string
    random.seed(0)
    for i in range(0, 100):
        # We build a random JSON document and also a corresponding dictionary
        # for it which will be used for validation.
        dct = {}
        json_str = "{"
        json_str_split = [json_str]
        for j in range(0, random.randint(1, 5)):
            if dct:
                json_str += ","
            k = "".join(
                random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 10))
            )
            json_str += f'"{k}":'
            json_str_split.append(json_str)

# Generated at 2022-06-14 14:48:33.942426
# Unit test for function tokenize_json
def test_tokenize_json():
    class BookSchema(Schema):
        title = Field(str)
        published = Field(int)
        author = Field(str)
        characters = Field(list)

    book_data = '{"title": "Hamlet", "author": "Shakespeare", "published": 1603, "characters": ["Hamlet", "Polonius", "Ophelia"]}'

    book_token = tokenize_json(book_data)
    assert book_token
    assert book_token.pos_start.char_index == 0
    assert book_token.pos_end.char_index == 109
    assert book_token.content == book_data
    assert book_token.value == book_token.value


# Generated at 2022-06-14 14:48:39.086272
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": "the value", "b": [1,2,"some string"]}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value == {"a": "the value", "b": [1, 2, "some string"]}



# Generated at 2022-06-14 14:48:47.564945
# Unit test for function tokenize_json
def test_tokenize_json():
    print("Testing tokenizing JSON...")
    json_dict = {"foo": 1}
    json_string = json.dumps(json_dict)
    token = tokenize_json(json_string)
    assert token.type == DictToken.type, f"Token should be a DictToken."
    assert token.value == json_dict, f"Token value should be {json_dict}. Got: {token.value}"
    assert token.start == 0, f"Token start should be 0. Got: {token.start}"
    assert token.end == len(json_string), f"Token end should be {len(json_string)}."
    assert token.text == json_string, f"Token text should be {json_string}. Got: {token.text}"

# Generated at 2022-06-14 14:48:59.717152
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Tokenize a json string.
    """
    assert tokenize_json('{"a": 1, "b": 2}') == DictToken({'a': ScalarToken(1, 3, 3, '{"a": 1, "b": 2}'), 'b': ScalarToken(2, 11, 11, '{"a": 1, "b": 2}')}, 0, 16, '{"a": 1, "b": 2}')
    assert tokenize_json('[1, 2, 3]') == ListToken([ScalarToken(1, 1, 1, '[1, 2, 3]'), ScalarToken(2, 3, 3, '[1, 2, 3]'), ScalarToken(3, 5, 5, '[1, 2, 3]')], 0, 7, '[1, 2, 3]')
    assert tokenize_json

# Generated at 2022-06-14 14:49:07.241813
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json('{"foo": "bar"}') == DictToken(
        {"foo": ScalarToken("bar", 6, 11, '{"foo": "bar"}')}, 0, 14, '{"foo": "bar"}'
    )

# Generated at 2022-06-14 14:49:17.622593
# Unit test for function tokenize_json
def test_tokenize_json():
    test_json = r'{"name": "foo", "age": 2}'
    token = tokenize_json(test_json)
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.end == len(test_json) - 1
    assert token.content == test_json
    assert len(token.value) == 2
    assert isinstance(token.value[0], (ScalarToken, DictToken, ListToken))
    assert isinstance(token.value[1], (ScalarToken, DictToken, ListToken))
    assert token.value[0].value == "foo"
    assert token.value[1].value == 2


# Generated at 2022-06-14 14:49:26.664792
# Unit test for function tokenize_json
def test_tokenize_json():
    # For now only testing the position reporting of invalid json
    invalid_json = b"""
    {
      "key": "value",
      "key2": "value2,
      "key3": "value3"
    }
    """
    try:
        tokenize_json(invalid_json)
        assert False, "Expected a ValueError from tokenize.json"
    except ParseError as exc:
        assert exc.code == "parse_error"
        assert exc.position.line_no == 3
        assert exc.position.column_no == 22

# Generated at 2022-06-14 14:49:32.226646
# Unit test for function tokenize_json
def test_tokenize_json():
    result = tokenize_json(u'[{"hello": "world"}]')
    assert isinstance(result, ListToken)
    assert isinstance(result.value[0], DictToken)
    assert isinstance(result.value[0].value["hello"], ScalarToken)
    assert result.value[0].value["hello"].value == "world"


# Generated at 2022-06-14 14:49:35.003784
# Unit test for function tokenize_json
def test_tokenize_json():
    c = {"a": 1, "b": [1, 2]}
    assert tokenize_json(json.dumps(c)) == tokenize_json(c)



# Generated at 2022-06-14 14:49:37.945069
# Unit test for function tokenize_json
def test_tokenize_json():
	assert tokenize_json('{"test": "test"}') == {"test": "test"}


# Generated at 2022-06-14 14:49:45.901132
# Unit test for function tokenize_json
def test_tokenize_json():
    assert (
        tokenize_json(
            """
        {"name": "Angel"}
    """
        )
        == DictToken(
            {
                ScalarToken(
                    "name",
                    3,
                    14,
                    """
        {"name": "Angel"}
    """,
                ): ScalarToken(
                    "Angel",
                    19,
                    27,
                    """
        {"name": "Angel"}
    """,
                ),
            },
            0,
            28,
            """
        {"name": "Angel"}
    """,
        )
    )



# Generated at 2022-06-14 14:49:57.842935
# Unit test for function tokenize_json
def test_tokenize_json():
    class Persons(Schema):
        name = Field("name", str, required=True)
        age = Field("age", int, required=True)

    class Company(Schema):
        id = Field("id", int, required=True)
        name = Field("name", str, required=True)
        persons = Field("persons", [Persons], required=True)

    class Document(Schema):
        companies = Field("companies", [Company], required=True)


# Generated at 2022-06-14 14:50:00.111087
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test for function tokenize_json
    """
    assert isinstance(tokenize_json('{"test": 1}'), Token)



# Generated at 2022-06-14 14:50:10.446095
# Unit test for function tokenize_json
def test_tokenize_json():
    assert (
        tokenize_json('{"a": [{"b": "c"}, 1]}')
        == DictToken(
            {"a": ListToken([DictToken({"b": ScalarToken("c", 7, 11, '{"a": [{"b": "c"}, 1]}')}, 5, 13, '{"a": [{"b": "c"}, 1]}'), ScalarToken(1, 17, 18, '{"a": [{"b": "c"}, 1]}')], 15, 20, '{"a": [{"b": "c"}, 1]}')}, 0, 23, '{"a": [{"b": "c"}, 1]}')
    )


# Generated at 2022-06-14 14:50:18.404486
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:50:27.105259
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == None
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json('{"abc"}') == DictToken({"abc": None}, 0, 7, '{"abc"}')
    assert tokenize_json('{"abc":[]}') == DictToken({"abc":[]}, 0, 9, '{"abc":[]}')
    assert tokenize_json("[1,2]") == ListToken([1.0, 2.0], 0, 5, "[1,2]")
    assert tokenize_json("1") == ScalarToken(1,0,0, "1")


# Generated at 2022-06-14 14:50:29.875629
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '''{
        "name": "test",
        "age": 22,
        "values": [
            {
                "nested": "value"
            }
        ]
    }'''
    token = tokenize_json(content)
    assert isinstance(token, DictToken)


# Generated at 2022-06-14 14:50:40.946176
# Unit test for function tokenize_json
def test_tokenize_json():
    from hypothesis import given
    from hypothesis.strategies import from_type
    from .strategies import json_string
    from .assertions import assert_token_equals_expected


# Generated at 2022-06-14 14:50:49.407096
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"name": "John Smith"}') == {
        "name": "John Smith"
    }
    assert tokenize_json('{"name": ["John", "Smith"]}') == {
        "name": ["John", "Smith"]
    }
    with pytest.raises(ParseError):
        tokenize_json('')
    with pytest.raises(ParseError):
        tokenize_json('{')


# Generated at 2022-06-14 14:50:58.911140
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test for an empty string.
    with pytest.raises(ParseError):
        tokenize_json("")

    # Test for a non-empty string.
    assert tokenize_json('{"foo":"bar"}') == DictToken({ScalarToken("foo", 1, 5, '{"foo":"bar"}'): ScalarToken("bar", 10, 15, '{"foo":"bar"}')}, 0, 16, '{"foo":"bar"}')


# Unit tests for function validate_json

# Generated at 2022-06-14 14:51:07.803344
# Unit test for function tokenize_json
def test_tokenize_json():
    from pprint import pprint

    from typesystem import Schema, fields

    class BasicSchema(Schema):
        """
        Basic Schema Object for testing
        """

        data = fields.String()
        num = fields.Integer()

    schema = BasicSchema()
    value = {"data": "Some Test Data", "num": 4}
    # Successful case
    msg = validate_json(json.dumps(value), schema)
    assert msg == (value, [])
    # Invalid case
    value2 = {"data": 10, "num": 4}
    (v, msg) = validate_json(json.dumps(value2), schema)
    assert v == {}
    assert msg[0]["text"] == "Must be a string."
    assert msg[0]["code"] == "type_error"

# Generated at 2022-06-14 14:51:14.225692
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """{
        "a_string": "foo",
        "a_number": 1,
        "a_bool": true,
        "a_list": [ 1, 2, 3],
        "a_dict": { "hello": 1, "world": false },
        "a_null": null
    }"""
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.as_dict() == {
        "a_string": "foo",
        "a_number": 1,
        "a_bool": True,
        "a_list": [1, 2, 3],
        "a_dict": {"hello": 1, "world": False},
        "a_null": None,
    }

# Generated at 2022-06-14 14:51:21.009560
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test the tokenization of json content
    """
    # Test the error handling cases of the tokenizer.
    cases = [
        # No content.
        (b"", "parse_error"),
        # Bad JSON.
        (b"{1:2}", "parse_error"),
        (b"{1:2}", "parse_error"),
        # UTF-8 encoded JSON.
        (b"{\x01:1}", "parse_error"),
        (b"{1:\x01}", "parse_error"),
    ]

    for content, code in cases:
        with pytest.raises(ParseError) as exc_info:
            validate_json(content, Field())

        assert exc_info.value.code == code

    # Test various valid inputs.

# Generated at 2022-06-14 14:51:30.939252
# Unit test for function tokenize_json
def test_tokenize_json():
    # type: () -> None
    assert tokenize_json("") == ScalarToken(None, 0, 0, "")
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")
    assert tokenize_json("false") == ScalarToken(False, 0, 4, "false")
    assert tokenize_json('"string"') == ScalarToken("string", 0, 8, '"string"')
    assert tokenize_json("1") == ScalarToken(1, 0, 1, "1")
    assert tokenize_json("1.1") == ScalarToken(1.1, 0, 3, "1.1")
    assert tokenize_json("1e9") == ScalarToken

# Generated at 2022-06-14 14:51:40.420966
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a": "b"}') == DictToken({
        ScalarToken("a", 1, 3, '{"a": "b"}'): ScalarToken("b", 6, 8, '{"a": "b"}')
    }, 0, 9, '{"a": "b"}')

    assert tokenize_json('["a"]') == ListToken([
        ScalarToken("a", 1, 3, '["a"]')
    ], 0, 4, '["a"]')


# Generated at 2022-06-14 14:51:51.987364
# Unit test for function tokenize_json
def test_tokenize_json():
    content = \
'''
{
    "key1": [
        "value1",
        "value2",
        "value3",
    ],
    "key2": [
        "value4",
        "value5",
    ],
}
'''

    content = content.strip()
    token = tokenize_json(content)
    assert token.value == {
        "key1": [
            "value1",
            "value2",
            "value3",
        ],
        "key2": [
            "value4",
            "value5",
        ],
    }
    assert token.content == content
    assert isinstance(token, DictToken) and isinstance(token.items, list)
    assert len(token.items) == 2

# Generated at 2022-06-14 14:52:01.609970
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test that tokens match expected output
    """
    try:
        token = tokenize_json("{}")
    except:
        import traceback
        raise AssertionError("JSONDecodeError: {}", traceback.format_exc())
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.stop == 1
    assert token.children == []
    token = tokenize_json("{}")
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.stop == 1
    assert token.children == []

    token = tokenize_json('{"a" : 1}')
    assert isinstance(token, DictToken)
    assert token.start == 0
    assert token.stop == 5

# Generated at 2022-06-14 14:52:13.818763
# Unit test for function tokenize_json
def test_tokenize_json():
    print("hello from test_tokenize_json")
    print("Testing a simple JSON string containing a list")
    jsonExample = '[{"name":"john"},{"name":"bob"}]'
    tokens = tokenize_json(jsonExample)
    print(tokens)
    print(tokens.value)
    for t in tokens.value:
        print(t)
        print(t.value)
    print("Testing a simple JSON string that has been truncated")
    jsonExample = '[{"name":"john"}'
    try:
        tokens = tokenize_json(jsonExample)
    except ParseError as pe:
        print("Expected ParseError -  {}".format(pe))
    print("Testing a JSON string that is entirely whitespace")
    jsonExample = '\r\n  '

# Generated at 2022-06-14 14:52:16.484217
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('"hello"') == ScalarToken("hello", 0, 5, '"hello"')


# Unit tests for function validate_json

# Generated at 2022-06-14 14:52:23.975532
# Unit test for function tokenize_json
def test_tokenize_json():
    value, error_messages = validate_json(
        b'{"foo": [1, 2, 3], "bar": 4}',
        Schema(fields={"foo": ListField(items=IntegerField()), "bar": IntegerField()}),
    )
    assert value == {"foo": [1, 2, 3], "bar": 4}
    assert error_messages == []

# Generated at 2022-06-14 14:52:34.586267
# Unit test for function tokenize_json
def test_tokenize_json():
    # test various forms of empty strings

    # empty string should raise an error, as there is no content
    try:
        tokenize_json('')
        assert False
    except ParseError as err:
        assert err.text == "No content."
        assert err.code == "no_content"
        assert err.position.column_no == 1
        assert err.position.line_no == 1
        assert err.position.char_index == 0

    # empty string + whitespace should raise an error, as there is no content
    try:
        tokenize_json('   ')
        assert False
    except ParseError as err:
        assert err.text == "No content."
        assert err.code == "no_content"
        assert err.position.column_no == 1

# Generated at 2022-06-14 14:52:38.705920
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("{'hello': 'world'}")
    assert token.value == {ScalarToken("hello", 1, 6, "{'hello': 'world'}"): ScalarToken("world", 13, 18, "{'hello': 'world'}")}

# Generated at 2022-06-14 14:52:42.623385
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '[{"test":"test"}]'
    token = tokenize_json(content)
    assert token.value == [{"test": "test"}]
    assert token.start == 0
    assert token.end == 17
    assert token.content == content


# Generated at 2022-06-14 14:52:54.228423
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test tokenize_json.
    """
    # pragma: no cover
    import json  # type: ignore
    from typesystem.tokenize.tokens import Token
    from typesystem.base import Position

    assert isinstance(tokenize_json(""), Token)
    assert tokenize_json("{}").type == "dict"
    assert tokenize_json("{}").value == {}
    assert tokenize_json("[]").type == "list"
    assert tokenize_json('{"hello": 1}').type == "dict"
    assert tokenize_json('{"hello": 1}').value == {"hello": 1}
    assert tokenize_json('{"hello": "world"}').value == {"hello": "world"}
    assert tokenize_json("true").value == True
    assert tokenize_json("true").type

# Generated at 2022-06-14 14:52:57.938815
# Unit test for function tokenize_json
def test_tokenize_json():
    content = ''
    token = tokenize_json(content)
    assert token is None
    content = '{"foo": "bar"}'
    token = tokenize_json(content)
    assert token is not None


# Generated at 2022-06-14 14:53:05.747780
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json('{"foo": "bar"}') == DictToken({"foo": "bar"}, 0, 13, '{"foo": "bar"}')
    assert tokenize_json("[42]") == ListToken([42], 0, 4, "[42]")
    assert tokenize_json('["foo", "bar"]') == ListToken(["foo", "bar"], 0, 13, '["foo", "bar"]')
    assert tokenize_json("null") == ScalarToken(None, 0, 4, "null")
    assert tokenize_json("true") == ScalarToken(True, 0, 4, "true")
    assert tokenize_json("false") == ScalarToken(False, 0, 5, "false")

# Generated at 2022-06-14 14:53:12.206257
# Unit test for function tokenize_json
def test_tokenize_json():
    expected = ListToken(
        [
            ScalarToken(1, 0, 0, "[1]"),
            ScalarToken(2, 2, 2, "[1,2]"),
            ScalarToken(3, 4, 4, "[1,2,3]"),
        ],
        0,
        8,
        "[1,2,3]",
    )
    actual = tokenize_json("[1,2,3]")
    assert expected == actual



# Generated at 2022-06-14 14:53:24.027071
# Unit test for function tokenize_json
def test_tokenize_json():
    # If the input is a bytestring, it should be decoded into unicode
    token = tokenize_json(b'{"a": 1}')
    assert token.is_dict

    # Invalid JSON should raise an error
    with pytest.raises(ParseError) as exc:
        tokenize_json('{"a": 1')
    assert exc.value.text == 'Expecting value'

    # An empty string should raise an error
    with pytest.raises(ParseError) as exc:
        tokenize_json('')
    assert exc.value.text == 'No content.'

    # Large values (over 10 characters long) should be stored as a string
    token = tokenize_json('{"a": 1234567890}')
    assert token.is_dict
    assert token["a"].is_string




# Generated at 2022-06-14 14:53:28.282090
# Unit test for function tokenize_json
def test_tokenize_json():
    try:
        tokenize_json(json.loads('{"hello": "world"}'))
    except Exception:
        assert False
    try:
        tokenize_json('{"hello": "world"')
    except ParseError:
        assert True



# Generated at 2022-06-14 14:53:41.162821
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(
        b'{"title":"Hello World","published":"2019-10-07T00:37:00Z","author":"Example Inc."}'
    ) == tokenize_json(
        b'{"title": "Hello World","published": "2019-10-07T00:37:00Z","author": "Example Inc."}'
    )
    assert tokenize_json(b"null") == ScalarToken(None, 0, 3, b"null")
    assert tokenize_json(b'{"foo": 1}') == DictToken({ScalarToken("foo", 1, 4, b'{"foo": 1}') : ScalarToken(1, 7, 8, b'{"foo": 1}')}, 0, 11, b'{"foo": 1}')

# Generated at 2022-06-14 14:53:52.059599
# Unit test for function tokenize_json
def test_tokenize_json():
    def tokenize_json(content):
        return validate_json(content, validator=Field())

    assert tokenize_json("") == (None, [])
    assert tokenize_json("null") == (None, [])
    assert tokenize_json("true") == (True, [])
    assert tokenize_json("false") == (False, [])
    assert tokenize_json("1") == (1, [])
    assert tokenize_json("2.5") == (2.5, [])
    assert tokenize_json("'foo'") == (None, [])
    assert tokenize_json(b"null") == (None, [])
    assert tokenize_json(b"true") == (True, [])
    assert tokenize_json(b"false") == (False, [])
    assert tokenize

# Generated at 2022-06-14 14:53:58.330448
# Unit test for function tokenize_json
def test_tokenize_json():
    errors = []
    field = Field(format="integer")
    try:
        validate_json(b"", field)
        assert False, "Expected ParseError."
    except ParseError as exc:
        errors.append(exc)

    assert (
        str(errors[0])
        == "Unable to parse JSON data. (No content. on line 1, character 0)"
    )



# Generated at 2022-06-14 14:54:06.183187
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3",
        "key4": [
            "item1",
            "item2",
            "item3",
            "item4"
        ],
        "key5": {
            "key6": "value4"
        }
    }
    """
    token = tokenize_json(content)
    assert token.start_position.column_no == 1
    assert token.start_position.line_no == 3
    assert token.start_position.char_index == 7
    assert token.end_position.column_no == 47
    assert token.end_position.line_no == 13
    assert token.end_position.char_index == 159

# Generated at 2022-06-14 14:54:12.492734
# Unit test for function tokenize_json
def test_tokenize_json():
    assert (
        DictToken(
            {
                ScalarToken("foo", 1, 9, '{"foo": "bar"}'): ScalarToken(
                    "bar", 11, 16, '{"foo": "bar"}'
                )
            },
            0,
            17,
            '{"foo": "bar"}',
        )
        == tokenize_json(r'{"foo": "bar"}')
    )



# Generated at 2022-06-14 14:54:16.865612
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo": 123}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value["foo"] == ScalarToken(123, 8, 10, content)



# Generated at 2022-06-14 14:54:19.030109
# Unit test for function tokenize_json
def test_tokenize_json():
    assert type(tokenize_json('{"key": "value"}')) is DictToken


# Generated at 2022-06-14 14:54:22.298073
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('') == None
    assert tokenize_json('{"a":1}') == DictToken({'a': ScalarToken(1, '{"a":1}', 5)}, '{"a":1}', 7)

# Generated at 2022-06-14 14:54:28.983136
# Unit test for function tokenize_json
def test_tokenize_json():
    with pytest.raises(typesystem.ParseError) as excinfo:
        tokenize_json('{"foo": "bar"')
    assert excinfo.value.code == "parse_error"
    assert excinfo.value.text == "Expecting ',' delimiter."
    assert excinfo.value.position.char_index == 12
    assert excinfo.value.position.line_no == 1
    assert excinfo.value.position.column_no == 13



# Generated at 2022-06-14 14:54:38.376977
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '''
    {
        "name": "Test",
        "boolean": false,
        "number": 1.4,
        "integer": 5,
        "array": [1, 2, 3],
        "dict": {"key": "value"}
    }
    '''
    result = tokenize_json(content)
    test_dict = {"key": "value"}
    test_dict_token = DictToken(test_dict, 97, 127, content)

# Generated at 2022-06-14 14:54:52.966731
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"key1":"value1", "key2":123, "key3":false, "key4":null, "key5":[1, "string"]}')
    # AssertionError: Expected: {'key1': 'value1', 'key2': 123, 'key3': False, 'key4': None, 'key5': [1, 'string']}
    # Actual: {ScalarToken(value='value1', start=3, end=11, content='{"key1":"value1", "key2":123, "key3":false, "key4":null, "key5":[1, "string"]}'): ScalarToken(value=123, start=23, end=27, content='{"key1":"value1", "key2":123, "key3":false, "key4":null,

# Generated at 2022-06-14 14:55:03.314096
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = '{"string" : "this is a string", "number": 5}'
    token = tokenize_json(json_string)
    assert token.as_dict == {"string": "this is a string", "number": 5}
    assert token.type == dict
    assert token.is_list_like is False
    assert token[1].as_dict == "this is a string"
    assert token[1].type == str
    assert token[1].is_list_like is False
    assert token[2].as_dict == 5
    assert token.as_list == [
        token[1].as_dict,
        token[2].as_dict,
    ]

    json_list = "[1, 2, 3]"
    token = tokenize_json(json_list)

# Generated at 2022-06-14 14:55:14.132870
# Unit test for function tokenize_json
def test_tokenize_json():
    EXAMPLE = '''
[
 {
  "foo": "bar"
 }
]
'''.strip()

    assert tokenize_json(EXAMPLE) == ListToken(
        [
            DictToken(
                value={
                    ScalarToken(value="foo", line_offset=3, char_offset=3, text=EXAMPLE): ScalarToken(
                        value="bar", line_offset=4, char_offset=4, text=EXAMPLE
                    )
                },
                line_offset=2,
                char_offset=2,
                text=EXAMPLE,
            )
        ],
        line_offset=1,
        char_offset=1,
        text=EXAMPLE,
    )