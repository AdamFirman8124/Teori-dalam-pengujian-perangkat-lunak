

# Generated at 2022-06-14 14:45:54.176941
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json('["a"]') == ListToken(
        [ScalarToken("a", 1, 2, '["a"]')], 0, 5, '["a"]'
    )
    assert tokenize_json('{"a": 1}') == DictToken(
        {"a": ScalarToken(1, 5, 6, '{"a": 1}')}, 0, 9, '{"a": 1}'
    )

# Generated at 2022-06-14 14:45:56.662742
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(b'{"name":"lbliu","age":18}')
    assert isinstance(token, DictToken)
    assert token.value['name'].value == 'lbliu'
    assert token.value['age'].value == 18

if __name__ == "__main__":
    test_tokenize_json()

# Generated at 2022-06-14 14:46:08.356533
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.schemas import Schema
    from typesystem.fields import String

    class ExampleSchema(Schema):
        name = String()
        age = String()

    regular_json = """
    {"name": "John", "age": "21"}
    """

    regular_json_with_space = """

    {"name": "Jane", "age": "22"}

    """

    regular_json_with_tab = """
    {"name": "Jane", "age": "22"}
		
    """

    regular_json_with_newline = """

    {"name": "Jane", "age": "22"}

    """

    regular_json_with_mix_space_and_newline = """

    {"name": "Jane", "age": "22"}

    """

    regular_json_with_mix_

# Generated at 2022-06-14 14:46:16.282313
# Unit test for function tokenize_json
def test_tokenize_json():
    test_strs = [
        """
        {
            "key": {
                "key2": "value"
            },
            "arr": [
                "value",
                "value2"
            ]
        }
        """,
        "{}",
        "{\"foo\": \"bar\"}",
    ]

    for test_str in test_strs:
        token = tokenize_json(test_str)
        assert isinstance(token, (DictToken, ScalarToken))
        if isinstance(token, ScalarToken):
            assert token.value == {}



# Generated at 2022-06-14 14:46:21.772268
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    import random
    import string

    def json_equal(a: typing.Any, b: typing.Any) -> bool:
        # Given that we're dealing with JSON documents we need to convert them
        # to dicts before we test them for equality.
        assert isinstance(a, Token)
        assert isinstance(b, dict)

        a = a.to_dict()
        return json.dumps(a) == jso

# Generated at 2022-06-14 14:46:27.598055
# Unit test for function tokenize_json
def test_tokenize_json():
    data = """
    {
        "name" : "John Smith",
        "age" : 25,
        "address" : {
            "street" : "2701 Le Conte Avenue",
            "city" : "Berkeley",
            "state" : "California",
            "zip" : "94709"
        },
        "interests" : [ "skiing", "hiking", "travel" ],
        "permissions" : null,
        "github_username" : "js123",
        "is_active" : true
    }
    """

# Generated at 2022-06-14 14:46:33.225337
# Unit test for function tokenize_json
def test_tokenize_json(): 
    s = '{"name": "test_name","age": 20, "address": {"state": "CA", "city": "San Francisco"}}'
    assert tokenize_json(s) == DictToken({'name': 'test_name', 'age': 20, 'address': {'state': 'CA', 'city': 'San Francisco'}}, 0, len(s)-1, s)


# Generated at 2022-06-14 14:46:43.296481
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(b'"abc"')
    assert token.value == "abc"
    assert token.start_pos.line_no == 1
    assert token.start_pos.column_no == 1
    assert token.start_pos.char_index == 0
    assert token.end_pos.line_no == 1
    assert token.end_pos.column_no == 5
    assert token.end_pos.char_index == 4

    token = tokenize_json(b'{"key1":"abc","key2":[1,3,4]}')
    assert token.value == {"key1": "abc", "key2": [1, 3, 4]}
    assert token.value["key2"][2].start_pos.line_no == 1
    assert token.value["key2"][2].start_pos.column

# Generated at 2022-06-14 14:46:54.284537
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo": null}'
    result = tokenize_json(content)
    dict_token = DictToken({'foo': None}, 0, 15, content)
    assert result == dict_token
    # Test validate_json with Field
    value, errors = validate_json(content, field.String())
    assert value is dict_token
    assert errors[0].text == 'Expected string, got `null` instead.'
    assert errors[0].code == 'type_error'
    assert errors[0].path == ['foo']
    assert errors[0].position.line_no == 1
    assert errors[0].position.column_no == 9
    assert errors[0].position.char_index == 8
    # Test validate_json with Schema
    class MySchema(Schema):
        foo = field.String()

# Generated at 2022-06-14 14:47:05.056845
# Unit test for function tokenize_json
def test_tokenize_json():
    print('Test json tokenize')
    content = '{"name":"derek", "age": 42.2, "birth":false, "height":[3,2,1]}'

    token = tokenize_json(content)

    json_append = token.append

    results = []
    results_append = results.append

    for child in token.children:
        if child.type is ScalarToken:
            results_append(child.value)
        else:
            for token in child.children:
                results_append(token.value)

    assert results[0] == "derek"
    assert results[1] == 42.2
    assert results[2] == False
    assert results[3] == 3
    assert results[4] == 2
    assert results[5] == 1


# Generated at 2022-06-14 14:47:25.278626
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('"foo"') == ScalarToken(value="foo", start=0, end=4, content='"foo"')
    assert tokenize_json('{"key": "value"}') == DictToken(value={"key": ScalarToken(value="value", start=7, end=13, content='"value"')}, start=0, end=14, content='{"key": "value"}')
    assert tokenize_json('[]') == ListToken(value=[], start=0, end=1, content='[]')
    assert tokenize_json('["value"]') == ListToken(value=[ScalarToken(value="value", start=2, end=8, content='"value"')], start=0, end=9, content='["value"]')


# Generated at 2022-06-14 14:47:34.954435
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo":"bar"}'
    token = tokenize_json(content)

    assert(hasattr(token, "children"))

    children = token.children

    assert(len(children) == 1)

    first_child = children[0]

    assert(isinstance(first_child, DictToken))

    assert(first_child.column_start == 0)

    assert(first_child.column_end == len(content))

    assert(first_child.line_start == 1)

    assert(first_child.line_end == 1)

    assert(isinstance(first_child.children[0], ScalarToken))

    assert(first_child.children[0].content == "foo")

    assert(isinstance(first_child.children[1], ScalarToken))


# Generated at 2022-06-14 14:47:40.518677
# Unit test for function tokenize_json
def test_tokenize_json():
    tokenize_json_result = tokenize_json(b"""{"a": "b"}""")
    assert tokenize_json_result.value == {"a": "b"}
    assert tokenize_json_result.start == 0
    assert tokenize_json_result.end == 8
    assert tokenize_json_result.content == """{"a": "b"}"""


# Generated at 2022-06-14 14:47:47.586600
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"foo": "bar"}') == DictToken({'foo': ScalarToken('bar', 0, 10, '{"foo": "bar"}')}, 0, 12, '{"foo": "bar"}')
    assert tokenize_json('[1.5, 2.5, 3.5]') == ListToken([ScalarToken(1.5, 0, 4, '[1.5, 2.5, 3.5]'), ScalarToken(2.5, 5, 9, '[1.5, 2.5, 3.5]'), ScalarToken(3.5, 10, 14, '[1.5, 2.5, 3.5]')], 0, 16, '[1.5, 2.5, 3.5]')


# Generated at 2022-06-14 14:47:55.604937
# Unit test for function tokenize_json
def test_tokenize_json():
    class SpecialSchema(Schema):

        class Meta:
            json_validator = validate_json

    class SpecialField(Field):

        type_ = SpecialSchema

    class SpecialSchema(Schema):
        arr = SpecialField()

    schema = SpecialSchema()
    input = b'{"arr": ["test"]}'
    err = ValidationError(
        message=Message(code="test", text="test text"),
        position=Position(1, 1, 0),
    )
    schema.set_validator(lambda x: err)
    result = schema.validate(input)
    assert result == [err]

# Generated at 2022-06-14 14:48:07.526743
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test out the tokenizer.
    content = '''{
    "a": [1, 2, true, 4.5],
    "b": {
        "a": "b",
        "c": false
    }
}'''

    token = tokenize_json(content)
    assert token.data == {"a": [1, 2, True, 4.5], "b": {"a": "b", "c": False}}
    assert token.start_pos == (1, 1)
    assert token.end_pos == (8, 16)

    token = token.data["b"]
    assert token.start_pos == (5, 5)
    assert token.end_pos == (7, 16)

    token = token.data["a"]
    assert token.start_pos == (6, 11)

# Generated at 2022-06-14 14:48:19.849641
# Unit test for function tokenize_json
def test_tokenize_json():
    # Given the content of a JSON file
    content = '{"hello": "world", "foo": "bar"}'

    # When I tokenize the JSON
    token = tokenize_json(content)

    # Then I get a tokenized version of the JSON
    assert token.value == {"hello": "world", "foo": "bar"}

    # And I get positional information
    token_hello = token.value["hello"]
    assert token_hello.__class__ is ScalarToken
    assert token_hello.start_position.line_no == 1
    assert token_hello.start_position.column_no == 2
    assert token_hello.start_position.char_index == 1
    assert token_hello.end_position.line_no == 1
    assert token_hello.end_position.column_no == 11
    assert token_hello

# Generated at 2022-06-14 14:48:30.020683
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test that tokenize_json returns the correct token for various inputs.
    assert isinstance(tokenize_json("{}"), DictToken)
    assert isinstance(tokenize_json("[]"), ListToken)
    assert isinstance(tokenize_json("1.0"), ScalarToken)
    assert isinstance(tokenize_json('"hello"'), ScalarToken)
    assert isinstance(tokenize_json("null"), ScalarToken)
    assert isinstance(tokenize_json("true"), ScalarToken)
    assert isinstance(tokenize_json("false"), ScalarToken)

    # Test that tokenize_json throws a ParseError with the correct position
    # information when it encounters parsable JSON, but invalid JSON.

# Generated at 2022-06-14 14:48:41.207138
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": "b"}'
    assert tokenize_json(content) == {'a': 'b'}
    content = '{"a": "b", "c": "d"}'
    assert tokenize_json(content) == {'a': 'b', 'c': 'd'}
    content = '{"a": "b", "c": [1, 2, 3]}'
    assert tokenize_json(content) == {'a': 'b', 'c': [1, 2, 3]}
    content = '{"a": "b", "c": {"d": "e", "f": "g"}}'
    assert tokenize_json(content) == {'a': 'b', 'c': {'d': 'e', 'f': 'g'}}

# Generated at 2022-06-14 14:48:48.386362
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name":"John", "age": 30, "city": "New York"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)

# Generated at 2022-06-14 14:48:57.954468
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a":1, "b":2}')
    assert(token)
    assert(token["a"] == ScalarToken(1, 2, 3))
    assert(token["b"] == ScalarToken(2, 9, 10))


# Generated at 2022-06-14 14:49:06.118067
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('') == {"type": "dict", "value": {}}
    assert tokenize_json('{"foo": "bar"}') == {
        "type": "dict",
        "value": {
            "foo": {"type": "scalar", "value": "bar"},
        }
    }
    assert tokenize_json('{"foo": ["bar"]}') == {
        "type": "dict",
        "value": {
            "foo": {
                "type": "list",
                "value": [{"type": "scalar", "value": "bar"}],
            },
        }
    }

# Generated at 2022-06-14 14:49:17.773435
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test for empty string and no content
    assert tokenize_json("") == ScalarToken(None, 0, 0, "")
    # Test for a simple string
    assert tokenize_json('"hello world"') == ScalarToken("hello world", 0, 14, '"hello world"')
    # Test for a simple list
    assert tokenize_json("[1, 2, 3]") == ListToken([ScalarToken(1, 1, 2, "1"), ScalarToken(2, 4, 5, "2"), ScalarToken(3, 7, 8, "3")], 0, 10, "[1, 2, 3]")
    # Test for a simple list with whitespaces

# Generated at 2022-06-14 14:49:29.921716
# Unit test for function tokenize_json
def test_tokenize_json():
    # Simple object
    assert (
        tokenize_json('{"key": "value"}')
        == DictToken(
            {
                ScalarToken("key", 1, 4, '{"key": "value"}'): ScalarToken(
                    "value", 10, 15, '{"key": "value"}'
                )
            },
            0,
            16,
            '{"key": "value"}',
        )
    )

    # Simple array

# Generated at 2022-06-14 14:49:40.645123
# Unit test for function tokenize_json
def test_tokenize_json():
    result = tokenize_json(b'{"health":"wellness","disease":"depression"}')
    assert isinstance(result, Token)
    assert result.value == {"health":"wellness","disease":"depression"}
    assert len(result.children) == 2
    print(repr(result))
    assert str(result) ==  'DictToken({"health":"wellness","disease":"depression"}, 0, 37)'
    assert result.children[0] == ScalarToken('wellness', 14, 23, '{"health":"wellness","disease":"depression"}')
    assert result.children[1] == ScalarToken('depression', 28, 39, '{"health":"wellness","disease":"depression"}')

# Generated at 2022-06-14 14:49:46.628701
# Unit test for function tokenize_json
def test_tokenize_json():
    schema = Schema({"foo": int, "bar": {"baz": str}})
    contents = """
    {
        "foo": 4,
        "bar": {
            "baz": "hello world"
        }
    }
    """
    token = tokenize_json(contents)
    assert token.sample == {"foo": 4, "bar": {"baz": "hello world"}}
    errors = validate_with_positions(token, schema)
    assert not errors



# Generated at 2022-06-14 14:49:58.348260
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test empty string
    token = tokenize_json("")
    assert token.kind == "empty"
    assert token.value == ""
    assert token.start_pos == 0
    assert token.end_pos == 0

    # Test boolean true
    token = tokenize_json("true")
    assert token.kind == "scalar"
    assert token.value is True
    assert token.start_pos == 0
    assert token.end_pos == 3

    # Test boolean false
    token = tokenize_json("false")
    assert token.kind == "scalar"
    assert token.value is False
    assert token.start_pos == 0
    assert token.end_pos == 4

    # Test null
    token = tokenize_json("null")
    assert token.kind == "scalar"
    assert token

# Generated at 2022-06-14 14:50:00.719376
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"test": "hello"}'
    expected_token = DictToken({DictToken(str): DictToken("hello")})
    assert tokenize_json(content) == expected_token


# Generated at 2022-06-14 14:50:12.856680
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"key1":"value1"}') == DictToken({'key1': 'value1'}, 0, 16, '{"key1":"value1"}')
    assert tokenize_json(b'[{"key1":"value1"}]') == ListToken([DictToken({'key1': 'value1'}, 1, 17, '[{"key1":"value1"}]')], 0, 18, '[{"key1":"value1"}]')

# Generated at 2022-06-14 14:50:21.612304
# Unit test for function tokenize_json
def test_tokenize_json():
    test_str = '{"a": {"b": [1,2,3]}}'

    token=tokenize_json(test_str)

    test_string=''.join(test_str)

    assert token.possible_values()=={'a': {'b': [1, 2, 3]}}
    assert token.value() == 'a'
    assert token.start_index == 1
    assert token.end_index == 2
    assert token.start() == 0
    assert token.end() == 1
    assert token.associated_string()==test_string


# Generated at 2022-06-14 14:50:31.669873
# Unit test for function tokenize_json
def test_tokenize_json():
    message = Message("""
    {
        "a": "b",
        "c": "d"
    }
    """)
    token = tokenize_json(message.text)
    assert type(token) is DictToken
    assert len(token) == 2
    assert token["a"] == ScalarToken("b", 2, 5, message.text)
    assert token["c"] == ScalarToken("d", 8, 11, message.text)
    assert token.start == 0
    assert token.end == 20
    assert token.position_range == (0, 20)

# Generated at 2022-06-14 14:50:36.927209
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(content='{"foo": "bar"}')
    assert token.value == {"foo": "bar"}
    assert token.start == 0
    assert token.end == 12
    assert token.content == '{"foo": "bar"}'
    assert token.children == []
    assert token.path == [""]


# Generated at 2022-06-14 14:50:45.316984
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:50:53.660315
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('[1,2,3]') == [1,2,3]
    assert tokenize_json('{"a":1, "b":2, "c":3}') == {"a":1, "b":2, "c":3}
    with pytest.raises(ParseError):
        tokenize_json('')
    with pytest.raises(ParseError):
        tokenize_json('{')
    with pytest.raises(ParseError):
        tokenize_json('{a:1}')
    with pytest.raises(ParseError):
        tokenize_json('{1:1}')


# Generated at 2022-06-14 14:51:04.310056
# Unit test for function tokenize_json
def test_tokenize_json():
    actual = tokenize_json('{"a": 1, "b" : 2}')
    assert actual.end == len('{"a": 1, "b" : 2}')
    assert actual.start == 0
    assert actual.value == {
        "a": ScalarToken(1, 5, 5, '{"a": 1, "b" : 2}'),
        "b": ScalarToken(2, 14, 14, '{"a": 1, "b" : 2}'),
    }
    assert actual.type_ == "dict"
    assert actual.content == '{"a": 1, "b" : 2}'

    actual = tokenize_json('"hello"')
    assert actual.end == len('"hello"')
    assert actual.start == 0
    assert actual.value == "hello"

# Generated at 2022-06-14 14:51:15.959146
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json("false") == ScalarToken(False, 0, 5, "false")
    assert tokenize_json("true") == ScalarToken(True, 0, 4, "true")
    assert tokenize_json("123") == ScalarToken(123, 0, 3, "123")
    assert tokenize_json("123.45") == ScalarToken(123.45, 0, 6, "123.45")
    assert tokenize_json("123e45") == ScalarToken(123e45, 0, 6, "123e45")
    assert tokenize_json('"foo"') == ScalarToken("foo", 0, 5, '"foo"')

# Generated at 2022-06-14 14:51:25.769162
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
      "name": "John Doe",
      "age": "20",
      "employed": true,
      "hobbies": [
        "rock climbing",
        "unicycling",
        "marshmallow swordfighting"
      ]
    }
    """
    expected = {
        "name": "John Doe",
        "age": "20",
        "employed": True,
        "hobbies": [
            "rock climbing",
            "unicycling",
            "marshmallow swordfighting",
        ],
    }
    token = tokenize_json(content)
    assert token.value == expected



# Generated at 2022-06-14 14:51:30.088948
# Unit test for function tokenize_json
def test_tokenize_json():
    a = {"text": "test1", "date": "2019-09-05"}
    b = {"text": "test2", "date": "2019-09-06"}
    c = {"text": "test3", "date": "2019-09-07"}
    content = [a, b, c]
    assert tokenize_json(content) == content


# Generated at 2022-06-14 14:51:38.571449
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '[{"foo":[1,2,3]},{"bar":true}]'
    token = tokenize_json(content=content)
    assert isinstance(token, ListToken)
    assert len(token.value) == 2
    assert len(token.value[0]) == 1
    assert len(token.value[1]) == 1
    assert token.value[0].get("foo").__class__ == ListToken
    assert len(token.value[0]["foo"].value) == 3
    assert token.value[1].get("bar").__class__ == ScalarToken
    assert token.value[1]["bar"].value == True



# Generated at 2022-06-14 14:51:44.595935
# Unit test for function tokenize_json
def test_tokenize_json():
    input_data = '''
    [
      {
        "id": 1,
        "name": "Apples",
        "price": 1.20
      },
      {
        "id": 2,
        "name": "Pears",
        "price": 2.30
      }
    ]
    '''
    # Parsing JSON should be successful
    assert tokenize_json(input_data)



# Generated at 2022-06-14 14:51:56.864949
# Unit test for function tokenize_json
def test_tokenize_json():
    assert type(tokenize_json('{"id": "1", "name": "John"}')) == DictToken
    assert type(tokenize_json('["1", "2", "3"]')) == ListToken
    assert type(tokenize_json('null')) == ScalarToken
    assert type(tokenize_json('"John"')) == ScalarToken
    assert type(tokenize_json('"John\""')) == ScalarToken
    assert type(tokenize_json('"John\\""')) == ScalarToken


# Generated at 2022-06-14 14:52:02.081526
# Unit test for function tokenize_json
def test_tokenize_json():
    field = Field(type="string", format="date-time")
    value, errors = validate_json(
        b'{"valid": "2018-01-01T00:00:00"}', field
    )
    assert errors == []
    value, errors = validate_json(
        b'{"invalid": "01/01/2018"}', field
    )
    assert len(errors) == 1
    assert isinstance(errors[0], ValidationError)



# Generated at 2022-06-14 14:52:07.052343
# Unit test for function tokenize_json
def test_tokenize_json():
    with open('test_json.json') as f:
        json_string = f.read()
        assert(tokenize_json(json_string))
        assert(ValidationError)


# Generated at 2022-06-14 14:52:10.548250
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == {}
    assert tokenize_json("{}") == {}
    assert tokenize_json('{"foo": "bar"}') == {"foo": "bar"}


# Generated at 2022-06-14 14:52:19.551454
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tests.fixtures import test_json_as_dict, test_json_as_list
    from typesystem.tokenize.tokens import DictToken, ListToken

    token = tokenize_json(test_json_as_dict)
    assert type(token) == DictToken
    assert token.end_column == 19
    assert token.end_line == 1
    assert token.end_index == 18
    assert token.start_column == 1
    assert token.start_line == 1
    assert token.start_index == 0

    token = tokenize_json(test_json_as_list)
    assert type(token) == ListToken
    assert token.end_column == 2
    assert token.end_line == 1
    assert token.end_index == 1
    assert token.start_

# Generated at 2022-06-14 14:52:28.989248
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"name":"value"}')
    assert isinstance(token, DictToken)
    assert token.value["name"] == "value"
    assert len(token.location.positions) > 0
    assert token.location.char_index_start <= len(token.location.content)
    assert token.location.char_index_end <= len(token.location.content)
    assert token.location.char_index_start <= token.location.char_index_end
    assert token.location.content[token.location.char_index_start:token.location.char_index_end+1] is not ''
    assert token.location.content[token.location.char_index_start:token.location.char_index_end+1] == '{"name":"value"}'

# Generated at 2022-06-14 14:52:40.565840
# Unit test for function tokenize_json
def test_tokenize_json():
    test_json_str = '{"key": "value"}'
    test_json_str_no_content = ""
    test_json_str_invalid = '{"key": "value'
    expected_tokens = [
        [{"key: value"}, "value"],
        [{"key": "value"}],
        [[{0, 1}], [{"key", 0}, {"value", 1}]],
        [{"key": "value"}, "value"],
    ]

# Generated at 2022-06-14 14:52:45.151106
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '[{"name": "First Name", "type": "string"}, {"name": "Last Name", "type": "string"}]'
    token = tokenize_json(content)
    assert isinstance(token, ListToken)
    assert token == [{"name": "First Name", "type": "string"}, {"name": "Last Name", "type": "string"}]


# Generated at 2022-06-14 14:52:56.326029
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test that we can parse a JSON document and that error messages are being
    raised as expected.
    """
    content = '{"x": "foo"}'
    result = tokenize_json(content)
    assert isinstance(result, DictToken)
    assert result.payload == {"x": "foo"}

    content = '{}'
    result = tokenize_json(content)
    assert isinstance(result, DictToken)
    assert result.payload == {}

    content = '42'
    result = tokenize_json(content)
    assert isinstance(result, ScalarToken)
    assert result.payload == 42

    content = '[]'
    result = tokenize_json(content)
    assert isinstance(result, ListToken)
    assert result.payload == []

    content = ' '

# Generated at 2022-06-14 14:53:04.065599
# Unit test for function tokenize_json
def test_tokenize_json():
    original_json = """
    {
        "name": "foo.bar",
        "version": "1.0",
        "releases": [
            {
                "name": "baz"
            }
        ]
    }
    """
    token = tokenize_json(original_json)
    assert token is not None
    assert token.value == {"name":"foo.bar","version":"1.0","releases":[{"name":"baz"}]}
    assert token.values() == [
        'name',
        'foo.bar',
        'version',
        '1.0',
        'releases',
        [
            'name',
            'baz'
        ]
    ]

# Generated at 2022-06-14 14:53:11.704735
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"a": "b"}') == {"a": "b"}
    assert tokenize_json('[1, 2, 3]') == [1, 2, 3]


# Generated at 2022-06-14 14:53:18.191637
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test tokenize_json function
    :return: None
    """
    content1 = {'level1': [{'level2': 1}, {'level2': 2}]}
    content2 = '{"level1": [{"level2": 1}, {"level2": 2}]}'
    assert tokenize_json(content1) == tokenize_json(content2) is not None



# Generated at 2022-06-14 14:53:29.673812
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('') == ''
    assert tokenize_json(' ') == ''
    assert tokenize_json('{}') == DictToken({}, 0, 1, '{}')
    assert tokenize_json('[]') == ListToken([], 0, 1, '[]')
    assert tokenize_json('null') == ScalarToken(None, 0, 3, 'null')
    assert tokenize_json('true') == ScalarToken(True, 0, 3, 'true')
    assert tokenize_json('false') == ScalarToken(False, 0, 4, 'false')
    assert tokenize_json('{"a": 1}') == DictToken({'a': 1}, 0, 7, '{"a": 1}')

# Generated at 2022-06-14 14:53:39.526101
# Unit test for function tokenize_json
def test_tokenize_json():
    from json import loads
    from json.decoder import JSONDecodeError as JDE
    from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken

    def test_parse_error(content):
        try:
            tokenize_json(content)
            assert False
        except ParseError as pe:
            assert pe.position.line_no == 1
            assert pe.position.column_no == 1
            assert pe.position.char_index == 0
            assert type(pe.position) == Position
            assert "%s" % pe == "No content."
            assert pe.code == "no_content"

    def test_validation_error(content, validator):
        (parsed, errors) = validate_json(content, validator)

# Generated at 2022-06-14 14:53:44.143803
# Unit test for function tokenize_json
def test_tokenize_json():
    # This should work
    tokenize_json('{ "foo": 1 }')

    # This should raise an error
    try:
        tokenize_json('{ "foo": foobar }')
    except ParseError:
        pass
    else:
        assert False


# Generated at 2022-06-14 14:53:51.653628
# Unit test for function tokenize_json
def test_tokenize_json():
    data = tokenize_json(
        """
{
    "name": "Bruce",
    "age": 25,
    "is_bald": false,
    "children": [
        "Bob",
        "Jane",
        {
            "name": "Richard",
            "age": 3
        }
    ]
}
"""
    )
    assert data == {
        "name": "Bruce",
        "age": 25,
        "is_bald": False,
        "children": ["Bob", "Jane", {"name": "Richard", "age": 3}],
    }


# Generated at 2022-06-14 14:54:02.663532
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.fields import String
    from typesystem.schemas.base import validation_error_messages

    schema = String()

    # Happy path - no validation errors
    data = '{"foo": "bar"}'
    token = tokenize_json(data)
    value, error_messages = validate_json(data, schema)
    assert value == {'foo': 'bar'}
    assert len(error_messages) == 0

    # No content - exposed error message
    data = '     '
    token = tokenize_json(data)
    value, error_messages = validate_json(data, schema)
    assert len(error_messages) == 1

# Generated at 2022-06-14 14:54:13.821033
# Unit test for function tokenize_json
def test_tokenize_json():
    # test if it can return an object token
    object_token = tokenize_json("{}")
    assert isinstance(object_token, Token)
    assert isinstance(object_token, DictToken)
    assert object_token._value == {}
    # test if it can return a list token
    list_token = tokenize_json("[]")
    assert isinstance(list_token, Token)
    assert isinstance(list_token, ListToken)
    assert list_token._value == []
    # test if it can return an scalar token
    scalar_token = tokenize_json("1")
    assert isinstance(scalar_token, Token)
    assert isinstance(scalar_token, ScalarToken)
    assert scalar_token._value == 1
    # test if it can return an scalar token


# Generated at 2022-06-14 14:54:20.407785
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"foo":"bar"}') == DictToken({"foo": "bar"}, start=0, stop=12, content='{"foo":"bar"}')

    # Unit test for function tokenize_json when only whitespace content is provided.
    with pytest.raises(ParseError, match="No content."):
        tokenize_json("   ")



# Generated at 2022-06-14 14:54:26.193186
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{\"name\": \"John\", \"age\": 55}"
    token = tokenize_json(content)
    assert token.get_value() == {"name": "John", "age": 55}
    content = "[1, 2, 3, 4]"
    token = tokenize_json(content)
    assert token.get_value() == [1, 2, 3, 4]



# Generated at 2022-06-14 14:54:34.785020
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{'a': 5, 'b': [1, 5]}"
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value == {'a': 5, 'b': [1, 5]}



# Generated at 2022-06-14 14:54:39.727371
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"name": "Roy G Biv"}') == DictToken(
        {
            ScalarToken("name", 1, 7, '{"name": "Roy G Biv"}'): ScalarToken(
                "Roy G Biv", 12, 23, '{"name": "Roy G Biv"}'
            )
        },
        0,
        23,
        '{"name": "Roy G Biv"}',
    )



# Generated at 2022-06-14 14:54:52.664830
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json(
        """
        {
            "a": 1,
            "b": ["foo", "bar"],
            "c": {
                "c1": 2.3,
                "c2": true
            }
        }
        """
    )
    assert isinstance(token, DictToken)

# Generated at 2022-06-14 14:55:03.193990
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('1') == ScalarToken(1, 0, 0, '1')
    assert tokenize_json('true') == ScalarToken(True, 0, 3, 'true')
    assert tokenize_json('false') == ScalarToken(False, 0, 4, 'false')
    assert tokenize_json('null') == ScalarToken(None, 0, 3, 'null')
    assert tokenize_json('"Hi"') == ScalarToken('Hi', 1, 2, '"Hi"')
    assert tokenize_json('[1, 2, 3]') == ListToken([1, 2, 3], 1, 7, '[1, 2, 3]')

# Generated at 2022-06-14 14:55:14.656335
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test that our custom tokenizing decoder class produces the expected output
    for the following example input.

    {
      "firstName": "John",
      "lastName": "Smith",
      "age": 25,
      "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021"
      },
      "phoneNumber": [
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