

# Generated at 2022-06-14 14:45:32.219816
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo": "bar", "baz": true, "a": 1.0, "b": [1, 2, 3]}'
    with pytest.raises(ParseError):
        token = tokenize_json(content)
        print(token)



# Generated at 2022-06-14 14:45:38.981394
# Unit test for function tokenize_json
def test_tokenize_json():
    content = {
        "title" : "a title",
        "body_text" : "some long body text with no meaning",
        "publish_date" : "2012-04-23T18:25:43.511Z",
        "hidden" : False,
        "numbers" : [1, 2, 3, 4, 5],
        "author" : {
            "id" : "123456789",
            "full_name" : "Simon Willison",
            "date_joined" : "2012-04-23T18:25:43.511Z",
            "is_admin" : False
        }
    }
    j = json.dumps(content)
    j = tokenize_json(j)
    f = open("out.json","w")
    f.write(j)

# Generated at 2022-06-14 14:45:50.750652
# Unit test for function tokenize_json
def test_tokenize_json():
    full_json = """
[{"id":1,"title":"title1","description":"description1","score":1.0},
{"id":2,"title":"title2","description":"description2","score":2.0},
{"id":3,"title":"title3","description":"description3","score":3.0}]"""

    def test_tokenize_json_item(content: str, expected: Token) -> None:
        actual = tokenize_json(content)
        assert actual == expected

    class DummyField(Field):
        def validate(self, value: typing.Any) -> typing.Any:
            return value

    json_schema = Schema(
        fields={"id": DummyField(), "title": DummyField(), "description": DummyField()}
    )
    assert json_schema._fields["id"] == D

# Generated at 2022-06-14 14:45:58.554597
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '''{
    "a": "hello",
    "b": "goodbye",
    "array": [1, 2, 3],
    "dict": {"hello": "world", "goodbye": "moon"}
}'''

    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value["a"] == "hello"
    assert token.value["b"] == "goodbye"
    assert token.value["array"] == ListToken([1, 2, 3], position_from=37, position_to=54)
    assert token.value["dict"] == DictToken(
        {"hello": "world", "goodbye": "moon"},
        position_from=55,
        position_to=95,
    )


# Set up a basic schema to validate against

# Generated at 2022-06-14 14:46:08.760283
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")
    assert tokenize_json("false") == ScalarToken(False, 0, 4, "false")
    assert tokenize_json("123") == ScalarToken(123, 0, 2, "123")
    assert tokenize_json("-123") == ScalarToken(-123, 0, 3, "-123")
    assert tokenize_json("0.1") == ScalarToken(0.1, 0, 3, "0.1")

# Generated at 2022-06-14 14:46:11.696135
# Unit test for function tokenize_json
def test_tokenize_json():
    test_string = '{"test": "string"}'
    token_test_string = tokenize_json(test_string)
    assert token_test_string.value == {'test': 'string'}


# Generated at 2022-06-14 14:46:22.013970
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test invalid JSON
    with pytest.raises(ParseError):
        tokenize_json("{")

    # Test empty JSON
    with pytest.raises(ParseError):
        tokenize_json("")

    # Test empty array
    token = tokenize_json("[]")
    assert isinstance(token, ListToken)
    assert token.value == []
    assert token.start == 0
    assert token.end == 1

    # Test empty object
    token = tokenize_json("{}")
    assert isinstance(token, DictToken)
    assert token.value == {}
    assert token.start == 0
    assert token.end == 1

    # Test scalar token
    token = tokenize_json('"abc"')
    assert isinstance(token, ScalarToken)

# Generated at 2022-06-14 14:46:25.120659
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Assert that tokenize json returns a Token object.
    """
    content = '{ "test": "mytest" }'
    assert type(tokenize_json(content)) == DictToken

# Generated at 2022-06-14 14:46:36.213374
# Unit test for function tokenize_json
def test_tokenize_json():
    json = b"""{
        "name": "Kenneth Reitz1",
        "occupation": "Pythonista",
        "age": 38,
        "height": null,
        "children": ["Ronald", "Ernest", "Edwin", "Thomas"],
        "hometown": {
            "name": "Fells Point",
            "latitude": 39.284,
            "longitude": 76.603,
        },
    }"""
    obj = tokenize_json(json)
    assert obj.get("name") == "Kenneth Reitz1"
    assert obj.get("occupation") == "Pythonista"
    assert obj.get("height") is None
    # Set up a simple schema with a few values
    class User(Schema):
        id = Field(type="integer")

# Generated at 2022-06-14 14:46:43.567123
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json("[1, 2, {\"a\": 3}]") == ListToken(
        [ScalarToken(1, 1, 1, "[1, 2, {\"a\": 3}]"), ScalarToken(2, 3, 3, "[1, 2, {\"a\": 3}]"), DictToken({"a": ScalarToken(3, 17, 17, "[1, 2, {\"a\": 3}]")}, 9, 18, "[1, 2, {\"a\": 3}]")], 0, 19, "[1, 2, {\"a\": 3}]"
    )

# Generated at 2022-06-14 14:47:05.069892
# Unit test for function tokenize_json
def test_tokenize_json():
    valid = "{}"
    token = tokenize_json(valid)
    assert type(token) == DictToken
    assert token.value == {}

    valid = "{\"abc\": 123}"
    token = tokenize_json(valid)
    assert type(token) == DictToken
    assert token.value == {"abc": 123}

    valid = "{\"abc\": [{\"def\": 456}]}"
    token = tokenize_json(valid)
    assert type(token) == DictToken
    assert token.value == {"abc": [{"def": 456}]}

    invalid = "{"
    with pytest.raises(ParseError):
        tokenize_json(invalid)



# Generated at 2022-06-14 14:47:12.308923
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '''
    {
        "foo": "bar",
        "hello": "world",
        "baz": null,
        "hi": "1234",
        "list": [
            "bob",
            "sam"
        ]
    }'''
    expected = {
        "foo": "bar",
        "hello": "world",
        "baz": None,
        "hi": "1234",
        "list": ["bob", "sam"],
    }
    assert expected == tokenize_json(content)



# Generated at 2022-06-14 14:47:23.490195
# Unit test for function tokenize_json
def test_tokenize_json():

    valid_json = """{"key": "value"}"""
    expected_token = DictToken({ScalarToken('key'): ScalarToken('value')}, 0, 18)


# Generated at 2022-06-14 14:47:32.115203
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Tests the tokenize_json function
    """
    from typesystem.constraints import MinLength, MaxLength, Equals
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken

    # Tests the parsing of a JSON object
    json_obj_string = '{"key": "value", "key2": "value2"}'
    tokens = tokenize_json(json_obj_string)
    assert isinstance(tokens, DictToken)
    assert tokens.parse_string == '{"key": "value", "key2": "value2"}'

    # Tests the parsing of a JSON array
    json_array_string = '["item", "item2", {"key": "value"}]'
   

# Generated at 2022-06-14 14:47:43.367376
# Unit test for function tokenize_json
def test_tokenize_json():
    json_str = '{"firstName": "John", "lastName": "Smith", "age": 25, "address": {"streetAddress": "21 2nd Street", "city": "New York", "state": "NY", "postalCode": "10021"}}'
    token = tokenize_json(json_str)
    assert token.position.char_index == 0
    assert token.end_position.char_index == len(json_str) - 1

    assert len(token.children) == 4
    assert token.children[0].value == "firstName"

    assert token.children[1].type == ScalarToken
    assert token.children[1].value == "John"

    assert token.children[2].value == "lastName"

    assert token.children[3].type == ScalarToken

# Generated at 2022-06-14 14:47:54.926950
# Unit test for function tokenize_json
def test_tokenize_json():
    def func_test(*args):
        token = tokenize_json(*args)
        assert token == DictToken(
            {
                ScalarToken("name", 0, 4, args[0]): ScalarToken("Alice", 7, 12, args[0]),
                ScalarToken("age", 14, 17, args[0]): ScalarToken(20, 20, 21, args[0]),
                ScalarToken("friends", 23, 30, args[0]): ListToken(
                    [
                        ScalarToken("Bob", 37, 40, args[0]),
                        ScalarToken("Emily", 44, 49, args[0]),
                    ],
                    33,
                    50,
                    args[0],
                ),
            },
            0,
            50,
            args[0],
        )


# Generated at 2022-06-14 14:48:06.887314
# Unit test for function tokenize_json
def test_tokenize_json():
    from json import loads
    from operator import eq
    token = tokenize_json(
        b'{"status": "active", "itemCount": [7, 11], "list": []}'
    )
    assert type(token) == DictToken
    value = token.value
    assert len(value) == 3
    assert (
        value["status"].value == "active"
        and type(value["status"]) == ScalarToken
    )
    assert (
        value["itemCount"].value == [7, 11] and type(value["itemCount"]) == ListToken
    )
    assert value["list"].value == [] and type(value["list"]) == ListToken
    assert token.start == 0 and token.end == 34

# Generated at 2022-06-14 14:48:17.185402
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """{ "name": "Foo"}"""
    assert tokenize_json(content).value == {'name': 'Foo'}
    content = '1'
    assert tokenize_json(content).value == 1
    content = '"string"'
    assert tokenize_json(content).value == 'string'
    content = '[1, 2, 3]'
    assert tokenize_json(content).value == [1, 2, 3]
    with pytest.raises(ParseError):
        tokenize_json('')
    with pytest.raises(ParseError):
        tokenize_json('{"name": "Foo"')


# Generated at 2022-06-14 14:48:22.261442
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = '{"id": "123456789abcd", "name": "test_name"}'

    value, _ = validate_json(json_string, Schema(fields={"name": "string"}))

    assert value["id"] == "123456789abcd"
    assert value["name"] == "test_name"



# Generated at 2022-06-14 14:48:28.080666
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == {}
    assert tokenize_json('{"a": 1, "b": "c"}') == \
        DictToken(
            {
                ScalarToken("a", 1, 2, '{"a": 1, "b": "c"}'): ScalarToken(1, 5, 6, '{"a": 1, "b": "c"}'),
                ScalarToken("b", 8, 9, '{"a": 1, "b": "c"}'): ScalarToken("c", 12, 13, '{"a": 1, "b": "c"}'),
            },
            0,
            19,
            '{"a": 1, "b": "c"}',
        )

# Generated at 2022-06-14 14:48:37.475946
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"hello":[],"world":null}') == {
        "hello": [],
        "world": None,
    }


# Unit tests for function validate_json

# Generated at 2022-06-14 14:48:48.144548
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('true') == ScalarToken(
        True, 0, 4, 'true'
    )
    assert tokenize_json('false') == ScalarToken(
        False, 0, 5, 'false'
    )
    assert tokenize_json('null') == ScalarToken(
        None, 0, 4, 'null'
    )
    assert tokenize_json('"a"') == ScalarToken(
        "a", 0, 3, '"a"'
    )
    assert tokenize_json('["a"]') == ListToken(
        [ScalarToken("a", 1, 3, '"a"')], 0, 5, '["a"]'
    )

# Generated at 2022-06-14 14:48:53.959575
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a":{"b":{"c":[1,2,3]}}}'
    token = tokenize_json(content)
    assert token.value == {"a":{"b":{"c":[1,2,3]}}}
    assert token.positions.end_column - token.positions.start_column == len(content)-1


# Generated at 2022-06-14 14:49:03.962712
# Unit test for function tokenize_json
def test_tokenize_json():
    obj1 = {"foo": 1}
    json_string1 = json.dumps(obj1)
    obj2 = tokenize_json(json_string1)
    assert isinstance(obj2, DictToken)
    assert isinstance(list(obj2.items())[0][0], ScalarToken)
    assert isinstance(list(obj2.items())[0][1], ScalarToken)
    assert obj2 == obj1

    obj3 = []
    json_string2 = json.dumps(obj3)
    obj4 = tokenize_json(json_string2)
    assert isinstance(obj4, ListToken)
    assert obj4 == obj3

    obj5 = [{"foo": 1}]
    json_string3 = json.dumps(obj5)

# Generated at 2022-06-14 14:49:06.692914
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"first name": "trio"}'
    assert tokenize_json(content).value == json.loads(content)


# Generated at 2022-06-14 14:49:18.702707
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:49:26.952340
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"title": "test", "done": true}')
    assert token == {
        Token('title', 0, 6, '{"title": "test", "done": true}'): Token(
            'test', 8, 13, '{"title": "test", "done": true}'
        ),
        Token('done', 15, 19, '{"title": "test", "done": true}'): Token(
            True, 21, 25, '{"title": "test", "done": true}'
        ),
    }



# Generated at 2022-06-14 14:49:36.917384
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"hello": "world"}') == DictToken({"hello": "world"}, 0, 21, '{"hello": "world"}')
    assert tokenize_json(b'{"hello": "world"}') == tokenize_json(b'{"hello": "world"}')
    assert tokenize_json(b'{"hello": "world"}') != tokenize_json(b'{"hello": "gravity"}')
    assert tokenize_json(b'[1, 2, 3]') == ListToken([1, 2, 3], 0, 7, '[1, 2, 3]')
    assert tokenize_json(b'{"hi": 5}') == DictToken({"hi": 5}, 0, 8, '{"hi": 5}')

# Generated at 2022-06-14 14:49:45.546291
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test empty string
    try:
        token = tokenize_json("")
        assert False
    except ParseError as e:
        assert "No content." in str(e)
    assert token is None

    # Test invalid JSON string
    with pytest.raises(ParseError) as excinfo:
        tokenize_json('{"foo": "bar}')
    assert "Expecting value" in str(excinfo.value)

    # Test valid JSON string
    token = tokenize_json('{"foo": "bar"}')
    assert token.data == {"foo": "bar"}
    assert token.start_position.char_index == 0
    assert token.start_position.line_no == 1
    assert token.start_position.column_no == 1
    assert token.end_position.char_index == 13

# Generated at 2022-06-14 14:49:57.841497
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{\"a\":1,\"b\":2,\"c\":true,\"d\":false,\"e\":null,\"f\":[1,2,3]}"
    token = tokenize_json(content)

# Generated at 2022-06-14 14:50:05.074478
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('["hello", {"a": [1, 2, 3]}]')
    assert isinstance(token, ListToken)
    assert len(token.value) == 2


# Generated at 2022-06-14 14:50:10.175494
# Unit test for function tokenize_json
def test_tokenize_json():
    test_dict = {"name": "test_name"}
    test_dict = json.dumps(test_dict)
    test_data = tokenize_json(test_dict)
    print(test_data)
    print("FUNCTION tokenize_json TESTS PASSED.")


# Generated at 2022-06-14 14:50:21.030958
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("  {}  ") == DictToken({}, position=Position(1, 0, 2))
    assert tokenize_json("{}") == DictToken({}, position=Position(1, 0, 0))
    assert tokenize_json("42") == ScalarToken(42, position=Position(1, 0, 0))
    assert tokenize_json(b"42") == ScalarToken(42, position=Position(1, 0, 0))
    assert tokenize_json('{"a": "b"}') == DictToken(
        {"a": ScalarToken("b", position=Position(1, 3, 3))}, position=Position(1, 0, 0)
    )

# Generated at 2022-06-14 14:50:23.545466
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('[ {"hello": "world"} ]')
    assert not isinstance(token, Token)
    assert isinstance(token[0], Token)
    assert token[0][0].value == 'hello'
    assert token[0][1].value == 'world'
    assert token[0].start == 0
    assert token[0].end == 19
    assert token[0].content == '[ {"hello": "world"} ]'
    # TODO: test error case raising ParseError

# Generated at 2022-06-14 14:50:30.358477
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test simple cases
    assert tokenize_json('{"name": "peter"}') == {
        "name": "peter"
    }
    assert tokenize_json('["a", "b", "c"]') == ["a", "b", "c"]
    assert tokenize_json('{"a": ["b", "c"]}') == {"a": ["b", "c"]}
    assert tokenize_json(
        '{"a": ["b", ["c", "d"]]}'
    ) == {"a": ["b", ["c", "d"]]}
    assert tokenize_json(
        '{"a": ["b", {"c": "d"}]}'
    ) == {"a": ["b", {"c": "d"}]}

# Generated at 2022-06-14 14:50:41.279981
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.fields import String
    from typesystem.schemas import Schema
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken

    # Empty content string
    empty_content = ""
    with pytest.raises(ParseError, match="ParseError: No content."):
        tokenize_json(empty_content)

    # Empty object
    empty_object = "{}"
    token = tokenize_json(empty_object)
    assert token == DictToken({}, 0, 1, empty_object)

    # Empty list
    empty_list = "[]"
    token = tokenize_json(empty_list)
    assert token == ListToken([], 0, 1, empty_list)

    # Null value
    null_value = "null"
    token = tokenize_json

# Generated at 2022-06-14 14:50:53.360896
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tokens import Token
    from json import dumps

    # Simple scalar value tests.
    assert tokenize_json(dumps(True)) == Token(True)
    assert tokenize_json(dumps(12)) == Token(12)
    assert tokenize_json(dumps("hello")) == Token("hello")
    assert tokenize_json(dumps(12.3)) == Token(12.3)

    # Test a dictionary
    content = dumps({"a": 1, "b": 2})
    token = tokenize_json(content)
    assert isinstance(token, Token)
    assert token.token_type == "dict"
    assert token.token_value == {"a": Token(1), "b": Token(2)}

    # Test a list

# Generated at 2022-06-14 14:51:04.115376
# Unit test for function tokenize_json
def test_tokenize_json():
    #Test empty string
    assert tokenize_json("") is None
    #Test basic string
    assert tokenize_json("\"str\"") == "str"
    #Test basic integer
    assert tokenize_json("1") == 1
    #Test basic float
    assert tokenize_json("1.0") == 1.0
    #Test basic boolean
    assert tokenize_json("true") == True
    assert tokenize_json("false") == False
    #Test basic null
    assert tokenize_json("null") == None
    #Test basic list
    assert tokenize_json("[0,1,2,3]") == [0,1,2,3]
    #Test basic list
    assert tokenize_json("[\"0\",1,2,3]") == ["0",1,2,3]
    #Test

# Generated at 2022-06-14 14:51:13.853896
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("""
        {
            "hello": "world"
        }
    """).value == {"hello": "world"}

    with pytest.raises(ParseError) as exc_info:
        tokenize_json("""
            {
                "hello": "world",
            }
        """)
    assert exc_info.value.position == Position(
        column_no=31, line_no=4, char_index=74,
    )
    assert exc_info.value.text == 'Expecting "," delimiter.'
    assert exc_info.value.code == "parse_error"



# Generated at 2022-06-14 14:51:20.805633
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = "{}"
    token = tokenize_json(json_string)
    assert token.value == {}
    json_string = '{"key": "value"}'
    token = tokenize_json(json_string)
    assert token.value == {"key": "value"}
    json_string = '{"key": ["value0", "value1", "value2"]}'
    token = tokenize_json(json_string)
    assert token.value == {"key": ["value0", "value1", "value2"]}
    json_string = '{"key": {"key0": "value0", "key1": "value1", "key2": "value2"}}'
    token = tokenize_json(json_string)

# Generated at 2022-06-14 14:51:39.165168
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '["foo", {"bar":["baz", null, 1.0, 2]}]'
    token = tokenize_json(content)
    assert isinstance(token, ListToken)
    assert token.value[0] == ScalarToken('foo', 2, 5, content)
    assert token.value[1] == DictToken({ScalarToken('bar', 10, 13, content):ListToken([ScalarToken('baz', 16, 19, content), ScalarToken('None', 21, 25, content), ScalarToken('1.0', 27, 30, content), ScalarToken('2', 32, 33, content)], 15, 33, content)}, 9, 34, content)


# Generated at 2022-06-14 14:51:43.676963
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "Beethoven", "value": 0.99}'
    token = tokenize_json(content)
    assert token.children[0].children[0].value == 'Beethoven'
    assert token.children[0].children[1].value == 0.99



# Generated at 2022-06-14 14:51:55.377622
# Unit test for function tokenize_json
def test_tokenize_json():
    json_str = '{"id": 1, "value": "red"}'
    parsed = tokenize_json(json_str)
    assert isinstance(parsed, DictToken) == True
    assert parsed.start == 0
    assert parsed.end == len(json_str)
    assert isinstance(parsed.value, dict) == True
    assert len(parsed.value) == 2
    assert parsed.value['id'] == ScalarToken(1, 8, 9, json_str)
    assert parsed.value['value'] == ScalarToken("red", 20, 23, json_str)

    json_str = '{"id": 1, "value": ["red", "blue", "green"]}'
    parsed = tokenize_json(json_str)

# Generated at 2022-06-14 14:52:03.477702
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('""') == ScalarToken('', 0, 1, '""')
    assert tokenize_json('"hi"') == ScalarToken('hi', 0, 3, '"hi"')
    assert tokenize_json('{}') == DictToken({}, 0, 1, '{}')
    assert tokenize_json('{"a":"b"}') == DictToken({ScalarToken('a', 1, 3, '"a"') : ScalarToken('b', 5, 7, '"b"')}, 0, 8, '{"a":"b"}')
    assert tokenize_json('[1]') == ListToken([ScalarToken(1, 1, 2, '1')], 0, 3, '[1]')

# Generated at 2022-06-14 14:52:09.327607
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{\"tests\":[{\"value\":1},{\"value\":2}]}"
    token = tokenize_json(content)
    assert token.value["tests"][0].value["value"].value == 1
    assert token.value["tests"][0].value["value"].position.char_index == 15


# Generated at 2022-06-14 14:52:11.160893
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json(content=b'{"key": "hello"}'), DictToken)



# Generated at 2022-06-14 14:52:21.180306
# Unit test for function tokenize_json
def test_tokenize_json():
    schema = {
        "type": "object",
        "properties": {
            "foo": {"type": "string"},
            "bar": {
                "type": "array",
                "items": {"type": "number"},
            },
        },
    }
    schema = Schema("Test", schema)
    content = b'{"foo": "Hello World!", "bar": [1, 2, 3]}'
    token = tokenize_json(content)
    assert token.as_python() == {'foo': 'Hello World!', 'bar': [1.0, 2.0, 3.0]}
    assert type(token) == DictToken
    assert type(token.get("foo")) == ScalarToken
    assert token.get("foo").as_python() == "Hello World!"
    assert type(token.get("bar"))

# Generated at 2022-06-14 14:52:23.975338
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "markdown", "version": "0.2.2", "title": "Markdown"}'
    tokenize_json(content)


# Generated at 2022-06-14 14:52:32.641332
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a": 1}') == {'a': 1}
    assert tokenize_json('{"a": 1, "b": 2}') == {'a': 1, 'b': 2}
    assert tokenize_json('[1, 2, 3]') == [1, 2, 3]
    assert tokenize_json('') == ''
    assert tokenize_json('1') == 1
    assert tokenize_json('null') is None
    assert tokenize_json('true') is True
    assert tokenize_json('false') is False

    with pytest.raises(ParseError):
        tokenize_json('{a: 1}')



# Generated at 2022-06-14 14:52:43.531068
# Unit test for function tokenize_json
def test_tokenize_json():
    from collections import OrderedDict
    test_content = r"""
{
  "key": "value",
  "key2": [1, 2, 3, true],
  "key3": {
    "nested": "value",
    "nested2": ["nested value", {"nested": "value"}]
  }
}
"""

# Generated at 2022-06-14 14:53:12.587179
# Unit test for function tokenize_json
def test_tokenize_json():
    from json import loads
    assert tokenize_json('{"hello": "world"}') == DictToken(value={"hello": "world"}, start=0, end=17, content='{"hello": "world"}')
    assert tokenize_json('{"hello": ["world", 2]}') == DictToken(value={"hello": ["world", 2]}, start=0, end=21, content='{"hello": ["world", 2]}')
    assert tokenize_json('{"hello": "world"}') == loads('{"hello": "world"}')
    assert tokenize_json('{"hello": "world"}') == DictToken(value={"hello": "world"}, start=0, end=17, content='{"hello": "world"}')

# Generated at 2022-06-14 14:53:19.787388
# Unit test for function tokenize_json
def test_tokenize_json():
    from copy import deepcopy
    from typesystem.tokenize.tokens import Token

    # Test basic tokens
    tokenize_json('"test"')
    tokenize_json('test')
    tokenize_json('{"test": false}')
    tokenize_json('[{"test": false}]')

    # Test errors
    try:
        tokenize_json('{"test": false}')
    except ParseError as e:
        return
    assert False



# Generated at 2022-06-14 14:53:31.165613
# Unit test for function tokenize_json
def test_tokenize_json():
    # Tokenization
    example = '{"message": "Hello", "number": 2}'
    tokens = tokenize_json(example)
    assert isinstance(tokens, DictToken)
    assert tokens.value == {
        'message': 'Hello',
        'number': 2
    }

    for key, value in tokens.value.items():
        token = tokens.value[key]
        assert isinstance(token, ScalarToken)
        assert token.value == value

        assert 0 < token.start_index <= token.end_index
        assert token.end_index <= len(example)

    # Collection tokenization
    example = "[1, 2, 3]"
    tokens = tokenize_json(example)
    assert isinstance(tokens, ListToken)

# Generated at 2022-06-14 14:53:36.663490
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": 1, "b": 2}'
    expected_result = DictToken(
        {"a": ScalarToken(1, 2, 3, content), "b": ScalarToken(2, 10, 11, content)},
        0,
        15,
        content
    )

    actual_result = tokenize_json(content)

    assert expected_result == actual_result


# Generated at 2022-06-14 14:53:46.932446
# Unit test for function tokenize_json
def test_tokenize_json():
    # The function throws an error if passed an empty string (by convention).
    with pytest.raises(ParseError, match="No content."):
        tokenize_json(content="")
    # Test a valid JSON string is tokenized correctly.
    token = tokenize_json(content='{"a": 1, "b": 2}')
    assert token.start_offset == 0
    assert token.end_offset == 16
    type(token).__name__ == "DictToken"
    assert token.value == {"a": 1, "b": 2}
    # Test that invalid JSON raises a ParseError.
    with pytest.raises(ParseError, match="parse error"):
        tokenize_json(content='{"a": 1, "b": 2,')

# Generated at 2022-06-14 14:53:55.204378
# Unit test for function tokenize_json
def test_tokenize_json():
    result = tokenize_json('{"key": "value", "name": ["Hans", "Peter"]}')

    assert len(result.keys) == 2
    assert set(result.keys) == {'key', 'name'}

    values = result.values

    assert isinstance(values[0], ScalarToken)
    assert values[0].value == 'value'

    assert isinstance(values[1], ListToken)
    assert len(values[1].values) == 2

    assert isinstance(values[1].values[0], ScalarToken)
    assert values[1].values[0].value == 'Hans'

    assert isinstance(values[1].values[1], ScalarToken)
    assert values[1].values[1].value == 'Peter'


# Generated at 2022-06-14 14:53:57.928998
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"hello": "world"}')
    assert [t.value for t in token] == ["world"]



# Generated at 2022-06-14 14:54:04.726729
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": 1, "b": 2}')
    assert isinstance(token, DictToken)
    assert token.name_value_pairs == [
        ("a", ScalarToken(1, 3, 3, '{"a": 1, "b": 2}')),
        ("b", ScalarToken(2, 11, 11, '{"a": 1, "b": 2}')),
    ]
    assert token.start_index == 0
    assert token.end_index == 17
    assert token.content == '{"a": 1, "b": 2}'


# Generated at 2022-06-14 14:54:15.389784
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:54:25.772477
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(content="{}") == DictToken({}, 0, 0, "{}")

# Generated at 2022-06-14 14:54:53.899891
# Unit test for function tokenize_json
def test_tokenize_json():
    tokenized = tokenize_json(
        """{
        "test": {
            "test": {
                "test": [
                    "test",
                    "test",
                    {
                        "test1": "test"
                    }
                ],
                "test2": "test"
            }
        }
    }"""
    )
    decoded = {
        "test": {
            "test": {
                "test": [
                    "test",
                    "test",
                    {
                        "test1": "test"
                    }
                ],
                "test2": "test"
            }
        }
    }
    assert tokenized == decoded

# Generated at 2022-06-14 14:55:01.790939
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")
    assert tokenize_json("false") == ScalarToken(False, 0, 4, "false")
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json("") == ScalarToken("", 0, 0, "")


# Generated at 2022-06-14 14:55:08.190237
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    import typesystem
    from typesystem.base import Position, ValidationError
    from typesystem.schemas import Schema

    data = {
        "name": "foo",
        "price": 42.5,
        "categories": ["all", "bar", "baz"],
    }
    json_string = json.dumps(data)
    token = tokenize_json(json_string)
    assert token == {"categories": ["all", "bar", "baz"], "name": "foo", "price": 42.5}

    # convert the tokenized json to the desired schema
    class ProductSchema(Schema):
        name = typesystem.String()
        price = typesystem.Float()
        categories = typesystem.Array(items=typesystem.String())

    schema = ProductSchema()
    #

# Generated at 2022-06-14 14:55:16.754121
# Unit test for function tokenize_json
def test_tokenize_json():
    # tokenize_json should accept a bytes object
    tokenize_json(b"{}")
    # tokenize_json should accept a string
    tokenize_json("{}")
    # tokenize_json should accept an empty string
    tokenize_json("")
    # tokenize_json should raise an error if there is no content
    with pytest.raises(ParseError):
        tokenize_json("   ")
    # tokenize_json should raise an error on a syntax error
    with pytest.raises(ParseError):
        tokenize_json("[1,2")
    # tokenize_json should return an empty dict if there is an empty dict
    token = tokenize_json("{}")
    assert isinstance(token, DictToken)
    assert token.value == {}
    # tokenize_