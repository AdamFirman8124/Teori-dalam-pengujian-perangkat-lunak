

# Generated at 2022-06-14 14:45:58.065052
# Unit test for function tokenize_json
def test_tokenize_json():
    json_content = '{"Line1":"Line1 Val","Line2":"Line2 Val","Line3":"Line3 Val","Line4":"Line4 Val"}'
    token = tokenize_json(json_content)
    assert isinstance(token, Token)
    assert token.key == "Line1"
    assert token.value == "Line1 Val"
    assert token.context == json_content
    assert token.start_position.column_no == 2
    assert token.start_position.char_index == 1
    assert token.start_position.line_no == 1
    assert token.end_position.column_no == 32
    assert token.end_position.char_index == 31
    assert token.end_position.line_no == 1


# Generated at 2022-06-14 14:46:08.488347
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "a": "b",
        "c": [1, 2, false],
        "d": [
            {
                "e": {"f": 1},
                "g": "h",
                "i": true
            }
        ]
    }
    """
    token = tokenize_json(content)
    assert token.children == {"a", "c", "d"}
    a = token.children["a"]
    assert isinstance(a, ScalarToken)
    assert a.value == "b"
    assert a.start == 9
    assert a.end == 14
    assert a.content is content
    c = token.children["c"]
    assert isinstance(c, ListToken)
    assert c.children == [1, 2, False]

# Generated at 2022-06-14 14:46:19.141512
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tokens import ListToken, ScalarToken

    def parse_object(content: str):
        return tokenize_json(content)

    def parse_array(content: str):
        return parse_object(content)["items"]

    assert parse_object('{"name": "joe"}') == {
        "name": ScalarToken('"joe"', content="joe")
    }

    assert parse_array('["joe", 1, true]') == [
        ScalarToken('"joe"', content="joe"),
        ScalarToken('1', content="1"),
        ScalarToken('true', content=True),
    ]


# Generated at 2022-06-14 14:46:28.294673
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json('"null"') == ScalarToken("null", 0, 6, '"null"')
    assert tokenize_json('"true"') == ScalarToken("true", 0, 6, '"true"')
    assert tokenize_json('"false"') == ScalarToken("false", 0, 7, '"false"')
    assert tokenize_json('"1"') == ScalarToken("1", 0, 3, '"1"')
    assert tokenize_json('"1.1"') == ScalarToken("1.1", 0, 5, '"1.1"')

# Generated at 2022-06-14 14:46:39.634431
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('"test"') == ScalarToken('test', 0, 5, content='"test"')
    assert tokenize_json('[1, 2, 3]') == ListToken([1, 2, 3], 0, 7, content='[1, 2, 3]')
    assert tokenize_json('{"a": 1, "b": "c"}') == DictToken({'a': 1, 'b': 'c'}, 0, 15, content='{"a": 1, "b": "c"}')

    with pytest.raises(ParseError) as excinfo:
        tokenize_json('')
    assert excinfo.value.text == 'No content.'
    assert excinfo.value.code == 'no_content'

# Generated at 2022-06-14 14:46:44.274955
# Unit test for function tokenize_json
def test_tokenize_json():
    data = """{"hello": [1, 2.5, "text", true, null, false]}"""
    token, error_messages = validate_json(data, Field())

    assert isinstance(token, dict)
    assert error_messages == []


# Generated at 2022-06-14 14:46:54.982088
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
      "firstName": "John",
      "lastName": "Smith",
      "isAlive": true,
      "age": 25,
      "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
      },
      "phoneNumbers": [
        {
          "type": "home",
          "number": "212 555-1234"
        },
        {
          "type": "office",
          "number": "646 555-4567"
        }
      ],
      "children": [],
      "spouse": null
    }
    """

    token = tokenize_json(content)

    assert isinstance(token, DictToken)


# Generated at 2022-06-14 14:47:02.347869
# Unit test for function tokenize_json
def test_tokenize_json():
    json_input = '[{"a":{},"b":[]}]'
    token = tokenize_json(json_input)
    assert token.type == "list"
    assert len(token.value) == 1
    dict_token = token.value[0]
    assert dict_token.value["a"].type == "dict"
    assert dict_token.value["a"].value == {}
    assert dict_token.value["b"].type == "list"
    assert dict_token.value["b"].value == []


# Generated at 2022-06-14 14:47:12.685784
# Unit test for function tokenize_json
def test_tokenize_json():
    class MySchema(Schema):
        foo = Field(type="string")
        bar = Field(type="integer")

    validator = MySchema()

    content = b'{"foo": "abc", "bar": 123}'
    value, errors = validate_json(content, validator)
    assert value.foo == "abc"
    assert value.bar == 123

    content = b"invalid json"
    with pytest.raises(ParseError) as exc:
        validate_json(content, validator)
    assert exc.value.text == "Expecting value."

    content = b'{"foo": 123, "bar": "abc"}'
    value, errors = validate_json(content, validator)
    assert len(errors) == 2
    assert errors[0].text == "Must be of type 'string'."

# Generated at 2022-06-14 14:47:24.062971
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test invalid JSON
    invalid_json = '''
    {
        "name": "Steve",
        "age": "old",
        "address": {
            "street": "some street",
            "city": {
                "id": 1,
                "name": "Sofia"
            }
        }
    }'''
    try:
        tokenize_json(invalid_json)
    except ParseError as exc:
        position = exc.position
        assert position.line_no == 4
        assert position.column_no == 12
        assert position.char_index == 86
    else:
        assert False, "Expected to receive a validation error."
    # Test error message

# Generated at 2022-06-14 14:47:42.486296
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == {"": {}}
    assert tokenize_json("{\"a\": 1}") == {"a": 1}
    assert tokenize_json("[1, 2]") == [1, 2]

    try:
        tokenize_json("{")
    except ParseError as exc:
        assert exc.text == "Expecting value."
        assert exc.code == "parse_error"
        assert exc.position == Position(line_no=1, column_no=2, char_index=1)

    try:
        tokenize_json("{\"a\": 1")
    except ParseError as exc:
        assert exc.text == "Expecting value."
        assert exc.code == "parse_error"

# Generated at 2022-06-14 14:47:52.614853
# Unit test for function tokenize_json
def test_tokenize_json():

    # Test a valid schema
    json = r'{"field1": "this works", "field2":{"field3": 5}}'
    token = tokenize_json(json)

    assert(
        isinstance(token, DictToken)
        and isinstance(token.value["field1"], ScalarToken)
        and isinstance(token.value["field2"], DictToken)
        and isinstance(token.value["field2"].value["field3"], ScalarToken)
    )

    # Test an empty string
    # This should not throw an exception
    tokenize_json("")

# Unit tests for function validate_json

# Generated at 2022-06-14 14:47:55.547164
# Unit test for function tokenize_json
def test_tokenize_json():
    assert (
        tokenize_json('{"a": 1}')
        == DictToken({ScalarToken('a'): ScalarToken(1)}, 0, 7, '{"a": 1}')
    )



# Generated at 2022-06-14 14:48:04.130248
# Unit test for function tokenize_json
def test_tokenize_json():

    content = """
    {
        "name": "John",
        "age": 20,
        "active": true,
        "salary": 23.50,
        "pets": ["cat", "dog"]
    }
    """
    token = tokenize_json(content)
    assert token == {
        "name": "John",
        "age": 20,
        "active": True,
        "salary": 23.50,
        "pets": ["cat", "dog"],
    }



# Generated at 2022-06-14 14:48:11.612314
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"a" : true}') == DictToken({'a': True}, 0, 17, '{"a" : true}')
    assert tokenize_json(b'{"a" : true, "b" : false, "c" : 1.0}') == \
        DictToken({'a': True, 'b': False, 'c': 1.0}, 0, 36, '{"a" : true, "b" : false, "c" : 1.0}')
    assert tokenize_json(b'{"a" : [1, 2, 3]}') == \
        DictToken({'a': [1, 2, 3]}, 0, 18, '{"a" : [1, 2, 3]}')

# Generated at 2022-06-14 14:48:16.660010
# Unit test for function tokenize_json
def test_tokenize_json():
    """Test JSON tokenization."""
    # Basic tests
    assert tokenize_json('"Hello"') == ScalarToken("Hello", 0, 7, '"Hello"')
    assert tokenize_json("42") == ScalarToken(42, 0, 2, '42')
    assert tokenize_json("[1,2,3]") == ListToken([ScalarToken(1, 1, 2, '1'), ScalarToken(2, 4, 5, '2'), ScalarToken(3, 7, 8, '3')], 0, 9, '[1,2,3]')

# Generated at 2022-06-14 14:48:27.543252
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(
        '{"list_values": [1, 2, 3, 4], "tuple_values": [1, 2, 3, 4], "another_list": [1, 2, 3, 4]}'
    ) == {
        "another_list": [1, 2, 3, 4],
        "list_values": [1, 2, 3, 4],
        "tuple_values": [1, 2, 3, 4],
    }

# Generated at 2022-06-14 14:48:31.168144
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": 1, "b": 2}')
    print(token)
    assert isinstance(token, DictToken)
    assert isinstance(token.value.get("a"), ScalarToken)
    assert isinstance(token.value.get("b"), ScalarToken)


# Generated at 2022-06-14 14:48:43.082846
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.json_schema import JsonSchemaField
    from .test_schemas import Movie, MovieSchema
    from datetime import datetime

    token = tokenize_json(b'{"title": "Star Wars", "length": 120, "release_date": "1997-01-01"}')

# Generated at 2022-06-14 14:48:50.440449
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"hello":{"count":3,"fruits":{"grapes":2,"apples":4,"mangoes":2}}}}')
    assert isinstance(token, DictToken)

    token = tokenize_json('{"hello":{"count":3,"fruits":{ "grapes":2, "apples":4, "mangoes":2 } } }')
    assert isinstance(token, DictToken)

    token = tokenize_json('{"hello":{"fruits":{"apples":4,"mangoes":2,"grapes":2},"count":3}}')
    assert isinstance(token, DictToken)

# Generated at 2022-06-14 14:49:00.982665
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[]") == ListToken([], 0, 1, "[]")
    assert tokenize_json('"Some String"') == ScalarToken(
        "Some String", 0, 13, '"Some String"'
    )



# Generated at 2022-06-14 14:49:04.122149
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("[1,2,3]")
    assert isinstance(token, ListToken)
    assert all(isinstance(x, ScalarToken) for x in token.value)
    assert token.value[0].value == 1



# Generated at 2022-06-14 14:49:14.490034
# Unit test for function tokenize_json
def test_tokenize_json():
    # Passing a string returns a token
    assert isinstance(tokenize_json("{}"), DictToken)

    # Passing a bytestring returns a token
    assert isinstance(tokenize_json(b"{}"), DictToken)

    # Raise an error if no content is present
    with pytest.raises(ParseError) as error:
        tokenize_json("")
    assert error.value.code == "no_content"

    # Raise an error if any other parse error is present
    with pytest.raises(ParseError) as error:
        tokenize_json('{"key": "value"}:')
    assert error.value.code == "parse_error"



# Generated at 2022-06-14 14:49:26.767879
# Unit test for function tokenize_json
def test_tokenize_json():
    # This is a simple case to check that data is as expected
    # TODO: Add test for data of incorrect format
    test_data = tokenize_json("""
        {
            "type": "object",
            "properties": {
                "title": {"type": "string", "format": "uri"},
                "author": {"type": "string", "format": "uri"},
                "url": {"type": "string", "format": "uri"}
            }
        }
    """)
    assert test_data.__class__.__name__ == "DictToken"
    assert test_data.value.__class__.__name__ == "dict"
    assert test_data.value["type"].__class__.__name__ == "ScalarToken"

# Generated at 2022-06-14 14:49:36.501357
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '''
        {
            "users": [
                {
                    "name": "Peter",
                    "email": "peter@example.com",
                    "age": 42
                }
            ]
        }
    '''
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert isinstance(token.children[0], DictToken)
    assert isinstance(token.children[0].children[0], ScalarToken)
    assert token.children[0].children[0].value == "users"

    assert isinstance(token.children[0].children[1], ListToken)
    assert isinstance(token.children[0].children[1].children[0], DictToken)

# Generated at 2022-06-14 14:49:45.515669
# Unit test for function tokenize_json
def test_tokenize_json():
    token_dict = tokenize_json('{"b":1, "a": true}')
    assert type(token_dict) == DictToken
    assert token_dict.get_value() == {"b": 1, "a": True}
    assert token_dict.start_pos == 0
    assert token_dict.end_pos == 14

    token_scalar = tokenize_json('1')
    assert type(token_scalar) == ScalarToken
    assert token_scalar.get_value() == 1
    assert token_scalar.start_pos == 0
    assert token_scalar.end_pos == 0

    token_list = tokenize_json('[1, 2, 3]')
    assert type(token_list) == ListToken

# Generated at 2022-06-14 14:49:48.500163
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("[1, 2]") == ListToken([1, 2], 0, 6, "[1, 2]")



# Generated at 2022-06-14 14:49:59.712135
# Unit test for function tokenize_json
def test_tokenize_json():
    test_json = '{"test": "test", "test2": 3.14, "test3": true, "test4": null, "test5": {"test5.1": 5}, "test6": [1, 2, 3]}'
    result = tokenize_json(test_json)
    assert result.type == "dict"
    assert len(result.value) == 6

    test_json2 = '{"test": {"test2": [{"foo": [1, 2, 3]}, {"bar": "quux"}, {"baz": 3.14}]}}'
    result2 = tokenize_json(test_json2)
    assert result2.type == "dict"
    assert len(result2.value) == 1
    assert result2.value[ScalarToken("test")].type == "dict"

# Generated at 2022-06-14 14:50:04.011395
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"hello":"world"}') == DictToken({
        'hello': ScalarToken('world', 9, 18, '{"hello":"world"}')
    }, 0, 18, '{"hello":"world"}')



# Generated at 2022-06-14 14:50:15.037258
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b"null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json('""') == ScalarToken("", 0, 2, '""')
    assert tokenize_json('"\\""') == ScalarToken('"', 0, 4, '"\\""')
    assert tokenize_json('"\\b"') == ScalarToken("\b", 0, 4, '"\\b"')
    assert tokenize_json('"\\f"') == ScalarToken("\f", 0, 4, '"\\f"')
    assert tokenize_json('"\\n"') == ScalarToken("\n", 0, 4, '"\\n"')

# Generated at 2022-06-14 14:50:21.773443
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": 1, "b": [true]}'
    result = tokenize_json(content)
    assert isinstance(result, DictToken)
    assert result.to_native() == {"a": 1, "b": [True]}



# Generated at 2022-06-14 14:50:30.042318
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == {"children": [], "token_type": "dict"}
    assert tokenize_json("{\"key\":\"value\"}") == {
        "children": [("key", "value")],
        "token_type": "dict",
    }
    assert tokenize_json("{\"key\": \"value\"}") == {
        "children": [("key", "value")],
        "token_type": "dict",
    }
    assert tokenize_json("{\"key\": 1}") == {"children": [("key", 1)], "token_type": "dict"}
    assert tokenize_json("[1]") == {"children": [1], "token_type": "list"}
    assert tokenize_json("11") == 11
    assert tokenize_json("\"11\"")

# Generated at 2022-06-14 14:50:41.058572
# Unit test for function tokenize_json
def test_tokenize_json():
    valid_json = '''
    {
        "key": "value",
        "key-number": 1,
        "key-boolean": true,
        "key-float": 1.5,
        "key-null": null,
        "key-array": [1,2,3],
        "key-dict": {
            "sub-key": "sub-value"
        }
    }
    '''
    invalid_json = '''
    {
        "key": "value",
    }
    '''
    assert(DictToken == type(tokenize_json(valid_json)))
    assert(DictToken == type(tokenize_json(valid_json.encode("utf-8"))))

# Generated at 2022-06-14 14:50:48.771398
# Unit test for function tokenize_json
def test_tokenize_json():
    def check_token(token, validator):
        assert token.token == validator
        assert token.start == 0
        assert token.end == 12

    content = '{"field1": "hi"}'
    token = tokenize_json(content)
    validator = DictToken({
        ScalarToken("field1"): ScalarToken("hi")
    })
    check_token(token, validator)



# Generated at 2022-06-14 14:50:56.873212
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    from pprint import pprint
    from . import tokenize_json as tokenizer
    from . import validate_json as validator
    '''
    This is a unit test that serves two purposes:

    1. Verify that the tokenize_json function works.
    2. Test that the validate_json function works by checking that the
       _TokenizingDecoder JSONDecoder subclass works.
    '''
    # Test 1

# Generated at 2022-06-14 14:51:06.231107
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("true") == ScalarToken(
        value=True, start_char_index=0, end_char_index=3, source_text="true"
    )
    assert tokenize_json("123") == ScalarToken(
        value=123, start_char_index=0, end_char_index=2, source_text="123"
    )
    assert tokenize_json("123.4") == ScalarToken(
        value=123.4,
        start_char_index=0,
        end_char_index=4,
        source_text="123.4",
    )

# Generated at 2022-06-14 14:51:17.111766
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Verifies that tokenize_json properly computes the expected token.
    """

    # Verify behavior with non-string content types
    with pytest.raises(ParseError, match="No content."):
        tokenize_json(b"")

    # Verify behavior with str content
    tok = tokenize_json('{"foo":"bar"}')
    assert isinstance(tok, DictToken)
    assert tok.ast["foo"] == "bar"
    assert tok.position.line_no == 1
    assert tok.position.column_no == 1
    assert tok.position.char_index == 0
    assert tok.terminal_position.line_no == 1
    assert tok.terminal_position.column_no == 14
    assert tok.terminal_position.char_index == 13

# Generated at 2022-06-14 14:51:28.690998
# Unit test for function tokenize_json
def test_tokenize_json():
    fields = {
        "string": Field(required=True),
        "integer": Field(required=True),
        "float": Field(required=True),
        "boolean": Field(required=True),
        "null": Field(required=True),
        "array": Field(required=True, validators=[list]),
        "nested": Field({"hello": Field(int)}),
    }

    class MySchema(Schema):
        fields = fields

    content = """{
        "string": "foo",
        "integer": 1,
        "float": 1.0,
        "boolean": true,
        "null": null,
        "array": [],
        "nested": {"hello": 1}
    }"""
    token = tokenize_json(content)
    data, error_messages = validate_

# Generated at 2022-06-14 14:51:38.797255
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = '{"city": "New York", "state": "NY", "weather": "sunny"}'
    encoded_string = json_string.encode()
    token = tokenize_json(encoded_string)

# Generated at 2022-06-14 14:51:46.155361
# Unit test for function tokenize_json
def test_tokenize_json():
    data = """
    {"foo": ["bar", 1, true]}
    """
    expected_token = DictToken(
        {
            "foo": ListToken(
                [
                    ScalarToken("bar", 10, 13, data),
                    ScalarToken(1, 16, 17, data),
                    ScalarToken(True, 19, 23, data),
                ],
                4, 30,
                data,
            )
        },
        0, 33,
        data,
    )
    assert tokenize_json(data) == expected_token



# Generated at 2022-06-14 14:51:59.126147
# Unit test for function tokenize_json
def test_tokenize_json():
    raw_json = '[{"key1": "value1", "key2": "value2"},{"key3": "value3"}]'
    token = tokenize_json(raw_json)
    assert token.start_pos == 1
    assert token.end_pos == len(raw_json)
    assert token.content == raw_json
    assert isinstance(token, ListToken)
    assert token.values[0].content == '{"key1": "value1", "key2": "value2"}'
    assert token.values[0].start_pos == 2
    assert token.values[0].end_pos == raw_json.index('}')
    assert isinstance(token.values[0], DictToken)
    assert token.values[0].values[0].content == 'value1'

# Generated at 2022-06-14 14:52:11.314369
# Unit test for function tokenize_json
def test_tokenize_json():
    content = """
    {
        "a": "foo",
        "b": "bar"
    }
    """
    token = tokenize_json(content)
    assert token.value['a'].value == "foo"
    assert token.value['b'].value == "bar"

    content = "null"
    token = tokenize_json(content)
    assert token.value is None

    content = """
    {
        "a": "foo",
        "b": bar
    }
    """
    with pytest.raises(ParseError) as excinfo:
        token = tokenize_json(content)

    assert excinfo.value.position.line_no == 5
    
    content = "foo"
    with pytest.raises(ParseError) as excinfo:
        token = tokenize

# Generated at 2022-06-14 14:52:19.992006
# Unit test for function tokenize_json
def test_tokenize_json():
    valid_json = """
    {
        "name": "John Doe",
        "age": 28,
        "location": {"country": "US", "state": "New York"}
    }
    """
    token = tokenize_json(valid_json)
    assert str(token) == valid_json

    invalid_json = """{
        "name": "John Doe",
        "age": "28",
        "location": {"country": "US", "state": "New York"}
    }"""

    with pytest.raises(ParseError) as exc:
        token = tokenize_json(invalid_json)
    assert "Unexpected token" in str(exc)

# Generated at 2022-06-14 14:52:28.124416
# Unit test for function tokenize_json
def test_tokenize_json():
    a = {'foo': 123}

    try:
        token = tokenize_json("")
    except ParseError as e:
        assert e.position
        assert e.text == "No content."

    try:
        token = tokenize_json("{")
    except ParseError as e:
        assert e.position
        assert e.text == "Expecting value."

    assert tokenize_json('{"foo": 123}') == DictToken(a, 0, 12, '{"foo": 123}')
    assert tokenize_json("{foo: 123}") == DictToken(a, 0, 11, "{foo: 123}")


# Generated at 2022-06-14 14:52:29.453198
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:52:35.345832
# Unit test for function tokenize_json
def test_tokenize_json():
    tokenized_json = tokenize_json(b'{"coordinates": [[-76.10413, 39.2047], [-76.10429, 39.20492]]}')
    assert isinstance(tokenized_json, DictToken)
    assert tokenized_json.value["coordinates"].value[1].value[0].value == -76.10429



# Generated at 2022-06-14 14:52:45.433317
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken({}, 0, 1, "{}")
    assert tokenize_json("[1, \"a\", false]") == ListToken(
        [ScalarToken(1, 1, 1, "[1, \"a\", false]"), ScalarToken("a", 5, 7, "[1, \"a\", false]"), ScalarToken(False, 10, 15, "[1, \"a\", false]")],
        0,
        17,
        "[1, \"a\", false]",
    )

# Generated at 2022-06-14 14:52:49.354171
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    json_string = '{"a":"b","c":"d"}'
    token = tokenize_json(json_string)
    assert json_string == token.json()
    assert token == json.dumps(token.value)



# Generated at 2022-06-14 14:52:59.926669
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.utils import validate_key_order_in_dict

# Generated at 2022-06-14 14:53:05.657936
# Unit test for function tokenize_json
def test_tokenize_json(): 
    #Test 1
    file = open("./testcases/test1.json", "r")
    content = file.read()
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value['name'] == "John"
    assert token.value['age'] == 30
    assert token.value['married'] == True
    assert token.value['address'].value['house_number'] == 12
    assert token.value['address'].value['street'] == "Downing Street"
    assert token.value['address'].value['city'] == "London"
    assert token.value['address'].value['pin_code'] == 1234
    assert token.value['address'].value['states'].value[0] == "Bihar"

# Generated at 2022-06-14 14:53:15.979179
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.fields import Dict, List, String

    content = """
    {
        "name": "test",
        "age": 42,
        "options": [
            "a",
            "b",
            "c"
        ],
        "user_options": {
            "one": 1,
            "two": 2,
            "three": 3
        }
    }
    """

    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value == {
        "name": "test",
        "age": 42,
        "options": ["a", "b", "c"],
        "user_options": {"one": 1, "two": 2, "three": 3},
    }
    assert isinstance(token.value["name"], ScalarToken)


# Generated at 2022-06-14 14:53:24.377509
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"a": [1, 2], "b": ["hello", {"c": "hello"}]}'
    token = tokenize_json(content)
    assert token.value == {"a": [1, 2], "b": ["hello", {"c": "hello"}]}

    content = '{"a": [1, 2], "b": ["hello", {"c": "hello"}],}'
    token = tokenize_json(content)
    assert token.value == {"a": [1, 2], "b": ["hello", {"c": "hello"}]}



# Generated at 2022-06-14 14:53:31.683856
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"foo": 1}') == DictToken({"foo": ScalarToken(1, 8, 9, '{"foo": 1}')}, 0, 10, '{"foo": 1}')
    assert tokenize_json('{"foo": [1]}') == DictToken({"foo": ListToken([ScalarToken(1, 9, 10, '{"foo": [1]}')], 8, 11, '{"foo": [1]}')}, 0, 12, '{"foo": [1]}')


# Generated at 2022-06-14 14:53:40.925644
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"name": "John", "age": 30}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken), \
        "Tokenizer did not return dictionary token."
    assert token.content == content, \
        "Content attribute of token is incorrect."
    assert token.start_pos == 0, \
        "Start position of token is incorrect."
    assert token.end_pos == len(content)-1, \
        "End position of token is incorrect."
    assert isinstance(token.value, dict), \
        "Token value is not a dictionary."
    assert len(token.value) == 2, \
        "Dictionary token contains incorrect number of items."
    assert "name" in token.value, \
        "Dictionary token value is missing 'name' key."
    assert "age"

# Generated at 2022-06-14 14:53:51.863983
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Test cases for the JSON content tokenizing process
    """
    field = Field(validators=["integer"])
    schema = Schema([field])

# Generated at 2022-06-14 14:54:02.809972
# Unit test for function tokenize_json
def test_tokenize_json():
    json_content = '{"name": "Rajat Garg", "age": 32, "zip": {"code": 232323, "address": "asadal"}}'
    token = tokenize_json(json_content)
    print("token", token)
    json_content = '{"name": "Rajat Garg", "age": 32, "zip": {"code": 232323, "address": "asadal"}}'
    validator = Schema()
    token = tokenize_json(json_content)
    result, error_messages = validate_with_positions(token=token, validator=validator)
    print("result", result)
    print("errors", error_messages)

# Generated at 2022-06-14 14:54:05.895173
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"foo":"bar"}')
    assert(token.dict_value['foo'].scalar_value == 'bar')


# Generated at 2022-06-14 14:54:12.637542
# Unit test for function tokenize_json
def test_tokenize_json():
    assert(tokenize_json('["foo", "bar"]') ==
        ListToken(
            [
                ScalarToken(
                    "foo",
                    0,
                    6,
                    '["foo", "bar"]'
                ),
                ScalarToken(
                    "bar",
                    9,
                    15,
                    '["foo", "bar"]'
                )
            ],
            0,
            15,
            '["foo", "bar"]'
          )
        )



# Generated at 2022-06-14 14:54:19.871069
# Unit test for function tokenize_json
def test_tokenize_json():
  # Test that tokenizing works on simple example
  content = '{"a": "hello", "b": 42, "c": 3.2, "d": null, "e": true, "f": false}'
  expected_result = DictToken(
    value={
      'a': ScalarToken('hello', 1, 10),
      'b': ScalarToken(42, 13, 15),
      'c': ScalarToken(3.2, 18, 21),
      'd': ScalarToken(None, 24, 27),
      'e': ScalarToken(True, 30, 33),
      'f': ScalarToken(False, 36, 41),
    },
    start=0,
    end=42,
  )
  actual_result = tokenize_json(content)
  assert actual_result == expected_result
  #

# Generated at 2022-06-14 14:54:29.383543
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("  null") == ScalarToken(None, 2, 5, "  null")
    assert tokenize_json('{"foo":1}') == DictToken({"foo": ScalarToken(1, 6, 7, '{"foo":1}')}, 0, 8, '{"foo":1}')
    assert tokenize_json('[1,2,3]') == ListToken([ScalarToken(1, 1, 2, '[1,2,3]'), ScalarToken(2, 3, 4, '[1,2,3]'), ScalarToken(3, 5, 6, '[1,2,3]')], 0, 7, '[1,2,3]')


# Generated at 2022-06-14 14:54:43.466762
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:54:54.056455
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json('{"abc": 123}'), DictToken)
    assert isinstance(tokenize_json('["abc", 123]'), ListToken)
    assert isinstance(tokenize_json('[123]'), ListToken)
    assert isinstance(tokenize_json('1.0'), ScalarToken)
    assert isinstance(tokenize_json('null'), ScalarToken)
    assert isinstance(tokenize_json('true'), ScalarToken)
    assert isinstance(tokenize_json('false'), ScalarToken)
    assert isinstance(tokenize_json('"abc"'), ScalarToken)
    assert isinstance(tokenize_json('"abc\\"abc"'), ScalarToken)
    assert isinstance(tokenize_json('\u1f48e'), ScalarToken)

# Generated at 2022-06-14 14:55:04.272233
# Unit test for function tokenize_json
def test_tokenize_json():
    import textwrap

    content = textwrap.dedent(
        """
    {
      "foo": {
        "bar": [null, 42, false, 0.1]
      }
    }
    """
    )
    token = tokenize_json(content)
    assert token.char_index == 0
    assert token.end_char_index == 63
    assert isinstance(token, DictToken)
    assert len(token.value) == 1

# Generated at 2022-06-14 14:55:14.253510
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"a": 1, "b":2, "c": [1,2,3], "d": {"inner": 7}}')
    print(token)
    # assert isinstance(token, DictToken)
    assert token.value == {"a": 1, "b":2, "c": [1,2,3], "d": {"inner": 7}}

# def test_validate_json():
#     token = tokenize_json('{"a": 1, "b":2, "c": [1,2,3], "d": {"inner": 7}}')
#     print(token)

if __name__ == '__main__':
    test_tokenize_json()