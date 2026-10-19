

# Generated at 2022-06-14 14:45:32.443075
# Unit test for function tokenize_json
def test_tokenize_json():
    def parse_error(text: str) -> ParseError:
        def err(*args, **kwargs):
            raise ParseError(text=text) from None

        return err

    invalid_json = {
        # No content
        "": parse_error("No content."),
        # Invalid JSON
        "[1,]": parse_error("Expecting value"),
        "--2": parse_error("Expecting value"),
        "[1, 2, 3] 4": parse_error("Expecting value"),
        "\"\\u\": 1": parse_error("Invalid \\uXXXX escape"),
        "\"\\u0": parse_error("Invalid \\uXXXX escape"),
    }
    # These should not error

# Generated at 2022-06-14 14:45:38.522519
# Unit test for function tokenize_json
def test_tokenize_json():
    schema = Schema(
        fields={
            "username": {"type": str},
            "password": {"type": str},
            "age": {"type": int},
            "gender": {"type": str},
        }
    )
    # print(tokenize_json('{"username": "johnsmith", "age": 25, "gender": "male", "password": "pass"}'))
    # print(tokenize_json('{"username": "johnsmith", "age": 25, "gender": "male", "password": "pass"}') is schema.from_json)
    print(validate_json('{"username": "johnsmith", "age": 25, "gender": "male", "password": "pass"}', schema))

# Generated at 2022-06-14 14:45:50.390413
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:45:58.237287
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tokens import ScalarToken
    from typesystem.tokenize.tokens import ListToken
    from typesystem.tokenize.tokens import DictToken
    from typesystem.tokenize.tokens import Token    
    
    # Test case for None
    result = tokenize_json('null')
    assert isinstance(result, ScalarToken)
    assert result.start == 0
    assert result.end == 4
    
    # Test case for empty array
    result = tokenize_json('[]')
    assert isinstance(result, ListToken)
    assert isinstance(result.value, list)
    
    # Test case for array
    result = tokenize_json('[1, 2, 3]')
    assert isinstance(result, ListToken)

# Generated at 2022-06-14 14:45:59.946642
# Unit test for function tokenize_json
def test_tokenize_json():
    data = tokenize_json('{"x": 1, "y": 2}')
    assert data.data == {'x': 1, 'y': 2}

# Generated at 2022-06-14 14:46:02.718753
# Unit test for function tokenize_json
def test_tokenize_json():
    actual = tokenize_json('null')
    expected = ScalarToken(None, 0, 3, content='null')
    assert actual == expected
# end unit test for function tokenize_json


# Generated at 2022-06-14 14:46:11.772814
# Unit test for function tokenize_json
def test_tokenize_json():
    json_token = tokenize_json("[{'a': 4}, {'b': 5}, {'b': 6}]")
    assert json_token.type == "list"
    assert len(json_token.children) == 3
    assert json_token.children[0].children[0].type == "scalar"
    assert json_token.children[0].children[0].value == 4
    assert json_token.children[1].children[0].type == "scalar"
    assert json_token.children[1].children[0].value == 5
    assert json_token.children[2].children[0].type == "scalar"
    assert json_token.children[2].children[0].value == 6


# Generated at 2022-06-14 14:46:16.892391
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    A simple unit test to make sure tokenize_json works as expected.
    """
    content = '{"password": "f00b4r"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value["password"] == "f00b4r"


# Generated at 2022-06-14 14:46:18.848371
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tests import test_tokenize_json
    test_tokenize_json()

# Generated at 2022-06-14 14:46:25.740082
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '''
    {
        "first": "foo",
        "second": [
            1, 2, 3
        ],
        "third": {
            "child1": true,
            "child2": false
        }
    }
    '''
    tokens = tokenize_json(content)
    assert tokens.children[0][0].value == "first"
    assert tokens.children[1][0].value == "second"
    assert tokens.children[2][0].value == "third"
    assert tokens.children[0][1].value == "foo"
    assert tokens.children[2][1].children[0][1].value is True
    assert tokens.children[2][1].children[1][1].value is False

# Generated at 2022-06-14 14:46:44.789070
# Unit test for function tokenize_json
def test_tokenize_json():
    from pprint import pprint

    from typesystem import String
    from typesystem.schemas import Schema
    from typesystem.types import Dictionary, List, String

    class RecipeSchema(Schema):
        name = String(max_length=50)
        ingredients = List[String](max_length=10)
        instructions = String(required=False)

    schema = RecipeSchema()
    valid_content = '{"name": "foo", "ingredients": ["a", "b"]}'
    invalid_content = '{"name": "foo", "ingredients": 123}'
    invalid_content2 = '{"name": "foo", "ingredients": ["a", "b"]}'
    invalid_content3 = '{"name": "x" * 51, "ingredients": ["a", "b"]}'
    token = tokenize

# Generated at 2022-06-14 14:46:55.284433
# Unit test for function tokenize_json
def test_tokenize_json():
    assert list(tokenize_json('["123", "456"]')) == [
        ScalarToken(123, 1, 5, '["123", "456"]'),
        ScalarToken(456, 10, 14, '["123", "456"]'),
    ]

# Generated at 2022-06-14 14:47:03.757453
# Unit test for function tokenize_json
def test_tokenize_json():
    # Testing various cases to make sure parsing works on each.
    # TODO: expand this test to ensure parsing is as expected.
    assert isinstance(tokenize_json("[1,2,3]"), ListToken)
    assert isinstance(tokenize_json("[[],[],[]]"), ListToken)
    assert isinstance(tokenize_json('{"a":1}'), DictToken)
    assert isinstance(tokenize_json('{"a":"b"}'), DictToken)
    assert isinstance(tokenize_json('{"a":true}'), DictToken)
    assert isinstance(tokenize_json(''), Token)


# Generated at 2022-06-14 14:47:10.940870
# Unit test for function tokenize_json
def test_tokenize_json():
    sample_json = r'{"a": 123, "b": [1,2,3,true], "c": null, "d": "hello"}'
    expected_value = {"a": 123, "b": [1, 2, 3, True], "c": None, "d": "hello"}
    result = tokenize_json(sample_json)
    assert isinstance(result, DictToken)
    assert isinstance(result.value, dict)

    assert result.value == expected_value



# Generated at 2022-06-14 14:47:21.575162
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('') == ScalarToken(None, 0, 0, '')
    assert tokenize_json('{}') == DictToken({}, 0, 2, '{}')
    assert tokenize_json(' {"a": 1} ') == DictToken({'a': ScalarToken(1, 5, 5, '1')}, 0, 10, ' {"a": 1} ')
    assert tokenize_json('{"a": "test", "b": "test"}') == DictToken({'a': ScalarToken('test', 5, 12, '"test"'), 'b': ScalarToken('test', 19, 26, '"test"')}, 0, 31, '{"a": "test", "b": "test"}')

# Generated at 2022-06-14 14:47:25.433773
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{ "test": 1}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert isinstance(token.value, dict)
    assert token.value["test"] == 1


# Generated at 2022-06-14 14:47:33.197627
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"k1":"v1", "k2":123}'
    token = tokenize_json(content)
    assert token.kind == "dict"
    assert len(token.value) == 2
    assert isinstance(token.value[0], ScalarToken)
    assert str(token.value[0]) == '{"k1":"v1", "k2":123}'
    assert token.value[0].value == "v1"
    assert token.value[0].position == Position(column_no=3, line_no=1, char_index=3)
    assert isinstance(token.value[1], ScalarToken)
    assert str(token.value[1]) == '{"k1":"v1", "k2":123}'
    assert token.value[1].value == 123

# Generated at 2022-06-14 14:47:44.075087
# Unit test for function tokenize_json
def test_tokenize_json():
    result = tokenize_json('{"key": "value"}')
    assert result == DictToken({"key": ScalarToken("value")}, 0, 17)

    result = tokenize_json('{"key": ["value1", "value2"]}')
    assert result == DictToken(
        {
            "key": ListToken(
                [
                    ScalarToken("value1"),
                    ScalarToken("value2"),
                ],
                9,
                23,
            )
        },
        0,
        24,
    )

    result = tokenize_json('{"key1": ["value1", "value2"], "key2": {"key3": "value3"}}')

# Generated at 2022-06-14 14:47:55.285323
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('[1, 2]') == [1, 2]
    assert tokenize_json('["a", "b"]') == ['a', 'b']
    assert tokenize_json('[1, "a"]') == [1, 'a']
    assert tokenize_json('{"a": 1}') == {'a': 1}
    assert tokenize_json('{"a": [1, 2]}') == {'a': [1, 2]}
    assert tokenize_json('{"a": [1, 2], "b": [3, 4]}') == {'a': [1, 2], 'b': [3, 4]}
    assert tokenize_json('{"a": {"x": "y"}, "b": "c"}') == {'a': {'x': 'y'}, 'b': 'c'}


# Generated at 2022-06-14 14:48:00.731302
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("""{"a": 1}""") == DictToken(
        {"a": ScalarToken(1, 2, 5, """{"a": 1}""")}, 0, 6, """{"a": 1}"""
    )



# Generated at 2022-06-14 14:48:25.143233
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"x": "y"}') == DictToken({ScalarToken("x", 1, 2): ScalarToken("y", 7, 8)})
    assert tokenize_json('{"x": "y"}') == DictToken({ScalarToken("x", 1, 2): ScalarToken("y", 7, 8)})
    assert tokenize_json("[]") == ListToken([])
    assert tokenize_json("['x']") == ListToken([ScalarToken("x", 2, 3)])
    assert tokenize_json("[1]") == ListToken([ScalarToken(1, 2, 2)])
    assert tokenize_json("[1, 2]") == ListToken([ScalarToken(1, 2, 2), ScalarToken(2, 5, 5)])

# Generated at 2022-06-14 14:48:34.011136
# Unit test for function tokenize_json
def test_tokenize_json():
    # Test passing a bytes.
    json_bytes = b"{'name': 'Jane Doe'}"
    assert tokenize_json(json_bytes) == tokenize_json("{'name': 'Jane Doe'}")

    # Test a unicode character.
    json_bytes = b"{\'name\': \'A\\u2019\', \'age\': 25}"
    assert tokenize_json(json_bytes) == tokenize_json("{\'name\': \'A\\u2019\', \'age\': 25}")

    # Test a null.
    json_bytes = b"{\'name\': null}"
    assert tokenize_json(json_bytes) == tokenize_json("{\'name\': null}")

    # Test a boolean.

# Generated at 2022-06-14 14:48:41.087388
# Unit test for function tokenize_json
def test_tokenize_json():
    # we can also put the test source code in string format
    test_data = ["true", "false", "null", "1", "1.5", "[1,2,3]", "{\"a\":1}"]

    for data in test_data:
        token = tokenize_json(data)
        assert(type(token) != ScalarToken)
        assert(type(token) != DictToken)
        assert(type(token) != ListToken)


# Generated at 2022-06-14 14:48:48.915228
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json("""
        {
            "first_name": "John",
            "last_name": "Smith",
            "skills": ["html", "css", "js"],
            "contact": {
                "email": "john.smith@gmail.com"
            }
        }
    """)
    assert token.py_value() == {
        "first_name": "John",
        "last_name": "Smith",
        "skills": ["html", "css", "js"],
        "contact": {
            "email": "john.smith@gmail.com"
        }
    }

# Generated at 2022-06-14 14:48:58.197594
# Unit test for function tokenize_json
def test_tokenize_json():
    import typesystem
    from typesystem.tokenize.tokens import Token
    from typesystem.fields import String

    validator = String()
    errors = validate_json(content='{}', validator=validator)
    assert errors == ([ErrorMessage(text="Field is required.", code="required")], None)
    errors = validate_json(content='1', validator=validator)
    assert errors[0][0].text == "Must be a string."
    errors = validate_json(content='"1"', validator=validator)
    assert errors == ([], None)

# Generated at 2022-06-14 14:49:01.013775
# Unit test for function tokenize_json
def test_tokenize_json():
    content = json.dumps({"key": "value"})
    content = content.encode("utf-8", "ignore")
    token = tokenize_json(content)
    assert isinstance(token, DictToken)



# Generated at 2022-06-14 14:49:08.863392
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json('"null"') == ScalarToken("null", 0, 6, '"null"')
    assert tokenize_json("true") == ScalarToken(True, 0, 4, "true")
    assert tokenize_json("false") == ScalarToken(False, 0, 5, "false")
    assert tokenize_json("1") == ScalarToken(1, 0, 1, "1")
    assert tokenize_json("1.1") == ScalarToken(1.1, 0, 3, "1.1")
    assert tokenize_json("1.1e12") == ScalarToken(1.1e12, 0, 6, "1.1e12")

# Generated at 2022-06-14 14:49:20.658338
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("") == {}
    assert tokenize_json(" ") == {}
    assert tokenize_json("null") == None
    assert tokenize_json("[0, 1]") == [0, 1]
    assert tokenize_json("{}") == {}
    assert tokenize_json("[]") == []
    assert tokenize_json(" { } ") == {}
    assert tokenize_json("{ }") == {}
    assert tokenize_json("[] ") == []
    assert tokenize_json("{\"foo\": true}") == {"foo": True}
    assert tokenize_json(" {   \"foo\"    :    true} ") == {"foo": True}

# Generated at 2022-06-14 14:49:25.676916
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{ "a": 1, "b": "foo"}'
    token = tokenize_json(content)
    assert token.children[0].children[0].children[0].value == 1
    assert token.children[0].children[1].children[0].value == "foo"


# Generated at 2022-06-14 14:49:33.148464
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"foo": "bar"}'
    token = tokenize_json(content)
    assert(type(token) == DictToken)
    assert(token.start_index == 0)
    assert(token.end_index == 14)
    assert(token.items["foo"].value == "bar")
    assert(token.items["foo"].start_index == 5)
    assert(token.items["foo"].end_index == 13)
    assert(token.items["foo"].content == content)



# Generated at 2022-06-14 14:49:51.170404
# Unit test for function tokenize_json
def test_tokenize_json():
    def cmp_tokenize_json_result(actual_result, expected_result):
        assert actual_result.content == expected_result["content"]
        assert actual_result.start_line == expected_result["start_line"]
        assert actual_result.start_col == expected_result["start_col"]
        assert actual_result.end_line == expected_result["end_line"]
        assert actual_result.end_col == expected_result["end_col"]
        assert actual_result.token_type == expected_result["token_type"]
        if actual_result.token_type == Token.DICT:
            assert len(actual_result.value) == len(expected_result["value"])

# Generated at 2022-06-14 14:49:58.596435
# Unit test for function tokenize_json
def test_tokenize_json():
    expected = DictToken(
        {
            ScalarToken("foo", 1, 4, "foo"): ScalarToken("bar", 7, 10, "bar"),
            ScalarToken("baz", 13, 16, "baz"): ScalarToken("qux", 19, 24, "qux")
        },
        0,
        26,
        '{"foo":"bar","baz":{"qux":1}}',
    )
    assert tokenize_json('{"foo":"bar","baz":{"qux":1}}') == expected



# Generated at 2022-06-14 14:50:05.642869
# Unit test for function tokenize_json
def test_tokenize_json():
    data = """
    {
        "name": "paul",
        "age": 32,
        "likes": ["jogging", "hiking", "soccer"],
        "preferences": {
            "verbose": false
        }
    }
    """
    tokens = tokenize_json(data)

# Generated at 2022-06-14 14:50:15.949974
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '''
    {
        "bool": true,
        "int": 1,
        "float": 1.0,
        "string": "value",
        "list": [1, 2, 3],
        "dict": {"value": 1}
    }
    '''
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value["bool"] is True
    assert isinstance(token.value["bool"], ScalarToken)
    assert token.value["int"] == 1
    assert isinstance(token.value["int"], ScalarToken)
    assert token.value["float"] == 1.0
    assert isinstance(token.value["float"], ScalarToken)
    assert token.value["string"] == "value"

# Generated at 2022-06-14 14:50:26.726185
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = """{
        "key1": "value1",
        "key2": [1, 2, 3, 4],
        "key3": {
            "key31": "value31",
            "key32": "value32"
        }
    }"""


# Generated at 2022-06-14 14:50:29.713737
# Unit test for function tokenize_json
def test_tokenize_json():
     input_string = '{"key1":true}'
     token = tokenize_json(input_string)
     assert isinstance(token, DictToken)
     assert len(token.value) == 1
     assert isinstance(token.value['key1'], ScalarToken)
     assert token.value['key1'].value == True


# Generated at 2022-06-14 14:50:40.794505
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{\"A\":\"B\"}") == DictToken({"A": "B"}, 0, 9, "{\"A\":\"B\"}")
    assert tokenize_json("[1,2,3]") == ListToken([1, 2, 3], 0, 6, "[1,2,3]")
    assert tokenize_json("null") == ScalarToken(None, 0, 3, "null")
    assert tokenize_json("123") == ScalarToken(123, 0, 2, "123")
    assert tokenize_json("1.5") == ScalarToken(1.5, 0, 3, "1.5")
    assert tokenize_json("true") == ScalarToken(True, 0, 3, "true")

# Generated at 2022-06-14 14:50:53.038858
# Unit test for function tokenize_json
def test_tokenize_json():
    test_data = [
        (
            {"string": "hello world!", "dict": {"some": "data"}, "list": [1, "two"]},
            """{
    "string": "hello world!",
    "dict": {
        "some": "data"
    },
    "list": [
        1,
        "two"
    ]
}""",
        ),
        (
            [1, 2, {"three": 4}, [5, 6, {"seven": 8}]],
            """
[
    1,
    2,
    {
        "three": 4
    },
    [
        5,
        6,
        {
            "seven": 8
        }
    ]
]
""",
        ),
    ]


# Generated at 2022-06-14 14:50:57.867931
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json(b'{"hello": "world"}') == DictToken({ScalarToken("hello", 0, 7, '{"hello": "world"}'): ScalarToken("world", 9, 18, '{"hello": "world"}')}, 0, 18, '{"hello": "world"}')

# Generated at 2022-06-14 14:51:01.528179
# Unit test for function tokenize_json
def test_tokenize_json():
    json_string = '{"a": 123, "b": "qwerty", "c": {"d": 123}, "e": [1, 2, 3]}'
    assert isinstance(tokenize_json(json_string), Token)



# Generated at 2022-06-14 14:51:16.203517
# Unit test for function tokenize_json
def test_tokenize_json():
    token = tokenize_json('{"foo": "bar"}')
    assert(isinstance(token, DictToken))
    assert({key.value: value.value for key, value in token.value.items()} == {'foo': 'bar'})


# Generated at 2022-06-14 14:51:28.032211
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:51:34.737577
# Unit test for function tokenize_json
def test_tokenize_json():
    test_inputs = [
        """
        {
            "foo": "bar",
            "baz": {
                "nested": "value"
            },
            "list": [1, 2, 3]
        }
        """
    ]
    for test_input in test_inputs:
        token = tokenize_json(test_input)
        assert isinstance(token, DictToken)
    print("tokenize_json test passed")


# Generated at 2022-06-14 14:51:42.625150
# Unit test for function tokenize_json
def test_tokenize_json():
    # args
    content = '{"prop1":"hi", "prop2":"hello", "prop3": [1,2,3]}'
    # expect

# Generated at 2022-06-14 14:51:53.125295
# Unit test for function tokenize_json
def test_tokenize_json():
    content = r'{"name": "Joe", "age": "42", "height": 1.8, "male": true, "none": null}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert token.value == {'name': 'Joe', 'age': '42', 'height': 1.8, 'male': True, 'none': None}
    assert token.start == 0
    assert token.end == 71
    assert token.content == content

    assert isinstance(token.value['name'], ScalarToken)
    name = token.value['name']
    assert name.value == 'Joe'
    assert name.start == 10
    assert name.end == 14
    assert name.content == content

# Generated at 2022-06-14 14:52:02.375982
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:52:14.334256
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:52:17.800981
# Unit test for function tokenize_json
def test_tokenize_json():
    input = """
    {"a":1,
         "b": [1, 2, 3]
    }
    """
    import json

    expected = json.loads(input)
    actual = tokenize_json(input)
    assert actual == expected


# Generated at 2022-06-14 14:52:24.732540
# Unit test for function tokenize_json
def test_tokenize_json():
    class Foo(Schema):
        a = 1
        b = 2

        def foo(self):
            if self.get_field("a").value == self.get_field("b").value:
                return True

    foo = Foo()

    assert foo.foo() == False

    content = '{"a": 1, "b": 2}'
    token = tokenize_json(content)

    try:
        # We don't have a token for this example, so we're just checking that
        # no exceptions are raised.
        validate_with_positions(token, foo)
    except ValidationError:
        pass

    assert isinstance(token, DictToken)
    assert isinstance(token.keys[0], ScalarToken) and token.keys[0].value == "a"

# Generated at 2022-06-14 14:52:28.005888
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"hello": "world"}'
    token = tokenize_json(content)
    assert token.kind == "dict"
    assert token.value == {"hello": "world"}
    assert hasattr(token, "position")



# Generated at 2022-06-14 14:52:46.966764
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json("{}") == DictToken(value={}, position=Position(0, 0, 0))
    assert tokenize_json("[]") == ListToken(value=[], position=Position(0, 0, 0))
    assert tokenize_json("null") == ScalarToken(value=None, position=Position(0, 0, 0))
    assert tokenize_json(
        '{"hello": "world"}'
    ) == DictToken(
        value={ScalarToken("hello", 4, 9, '{"hello": "world"}'): ScalarToken("world", 13, 19, '{"hello": "world"}')},
        position=Position(0, 0, 0),
    )

# Generated at 2022-06-14 14:52:53.069940
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"key": null}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    value = token.value
    assert "key" in value
    assert value["key"] is None
    assert token.start_position.char_index == 0
    assert token.end_position.char_index == len(content) - 1


# Generated at 2022-06-14 14:52:59.101763
# Unit test for function tokenize_json
def test_tokenize_json():
    import json
    content = """
    {"a": "b"}
    """
    token = tokenize_json(content)
    assert token == DictToken({ScalarToken("a", 3, 4, content): ScalarToken("b", 7, 8, content)}, 0, 10, content)

    expected_content = json.dumps({"a": "b"})
    assert expected_content == str(token)


# Generated at 2022-06-14 14:53:06.377516
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"key": "value"}') == DictToken({ScalarToken("key", 1, 6, '{"key": "value"}'): ScalarToken("value", 10, 19, '{"key": "value"}')}, 0, 18, '{"key": "value"}')

# Generated at 2022-06-14 14:53:10.165566
# Unit test for function tokenize_json
def test_tokenize_json():
    assert isinstance(tokenize_json('{"a": 123, "b": "string"}'), DictToken)
    assert isinstance(tokenize_json('{"a": 123, "b": "string"}')[0], ScalarToken)



# Generated at 2022-06-14 14:53:21.845658
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"key1": "val1", "key2": "val2"}'
    token = tokenize_json(content)
    assert isinstance(token, DictToken)
    assert tokenize_json("{}") == {}
    assert tokenize_json("[]") == []
    assert tokenize_json("1") == 1
    assert tokenize_json("true") is True
    assert tokenize_json("false") is False
    assert tokenize_json("null") is None
    assert tokenize_json("""{"foo": "bar"}""") == {"foo": "bar"}
    assert tokenize_json("""["foo"]""") == ["foo"]
    assert tokenize_json("""{"foo": null}""") == {"foo": None}

# Generated at 2022-06-14 14:53:33.245446
# Unit test for function tokenize_json
def test_tokenize_json():
    from typesystem.tokenize.tokens import TokenType


# Generated at 2022-06-14 14:53:39.986563
# Unit test for function tokenize_json
def test_tokenize_json():
    """
    Here you can test some test cases for the function.
    """

    assert tokenize_json('{"text": "This is a test!"}') == {"text": "This is a test!"}
    assert tokenize_json('{"text": "This is a test!"}') == {"text": "This is a test!"}
    assert tokenize_json('{"text": "This is a test!"}') == {"text": "This is a test!"}
    assert tokenize_json('{"text": "This is a test!"}') == {"text": "This is a test!"}

# Generated at 2022-06-14 14:53:51.041824
# Unit test for function tokenize_json
def test_tokenize_json():
    from hamcrest import *
    from hamcrest.core.core.isequal import equal_to
    import json
    # Use a lambda to take advantage of the is type matcher.
    is_token = lambda token: is_(instance_of(Token))

# Generated at 2022-06-14 14:54:01.443774
# Unit test for function tokenize_json
def test_tokenize_json():
    content = "{\"age\": 20}"
    result = tokenize_json(content)
    assert type(result) == DictToken
    assert result.value_dict.get("age").value == 20
    assert result.value_dict.get("age").position.char_index == 7
    assert result.value_dict.get("age").position.line_no == 1
    assert result.value_dict.get("age").position.column_no == 8
    invalid_content = "{\"age\": \"invalid\"}"
    with pytest.raises(ParseError):
        tokenize_json(invalid_content)
    empty_content = ""
    with pytest.raises(ParseError):
        tokenize_json(empty_content)



# Generated at 2022-06-14 14:54:22.818092
# Unit test for function tokenize_json
def test_tokenize_json():
    test_json_dict = {
        "key1": "val1",
        "key2": "val2",
        "key3": {"key4":"val4", "key5":"val5"},
        "key6": [1,2,3,4,5],
        "key7": 3.2,
        "key8": True,
        "key9": False,
        "key10": None
    }


# Generated at 2022-06-14 14:54:33.266970
# Unit test for function tokenize_json

# Generated at 2022-06-14 14:54:42.793840
# Unit test for function tokenize_json
def test_tokenize_json():
    schema = Schema(
        fields={"foo": Field(description="foo's description")},
        description="This is a test schema",
    )
    string = """{"foo": "baz"}"""
    token = tokenize_json(string)

    assert token.keys() == {"foo"}
    assert token.value["foo"].value == "baz"

    value, error_messages = validate_json(string, schema)
    assert value == dict(foo="baz")
    assert error_messages == []

    string = """{"foo": "baz", "bar": 3}"""
    value, error_messages = validate_json(string, schema)
    assert value == dict(foo="baz")

# Generated at 2022-06-14 14:54:53.621101
# Unit test for function tokenize_json
def test_tokenize_json():
    from copy import copy
    from json import loads as json_loads
    token = tokenize_json('{"cat": "meow", "dog": "woof"}')
    assert token == DictToken({
        ScalarToken("cat", 2, 5, '{"cat": "meow", "dog": "woof"}'):
            ScalarToken("meow", 11, 16, '{"cat": "meow", "dog": "woof"}'),
        ScalarToken("dog", 24, 27, '{"cat": "meow", "dog": "woof"}'):
            ScalarToken("woof", 33, 38, '{"cat": "meow", "dog": "woof"}')
    }, 0, 40, '{"cat": "meow", "dog": "woof"}')
    assert isinstance(token, DictToken)

# Generated at 2022-06-14 14:55:03.917234
# Unit test for function tokenize_json
def test_tokenize_json():
    assert tokenize_json('{"name": "bob"}') == DictToken(value={ScalarToken(value='name', start=1, end=1, content='{"name": "bob"}'): ScalarToken(value='bob', start=11, end=11, content='{"name": "bob"}')}, start=0, end=19, content='{"name": "bob"}')

# Generated at 2022-06-14 14:55:14.949525
# Unit test for function tokenize_json
def test_tokenize_json():
    content = '{"key": 3, "key2": "value"}'
    token = tokenize_json(content)
    assert token == {
        "key": ScalarToken(3, 3, 5, content),
        "key2": ScalarToken("value", 13, 19, content),
    }
    content = "null"
    token = tokenize_json(content)
    assert token == ScalarToken(None, 0, 3, content)
    content = "true"
    token = tokenize_json(content)
    assert token == ScalarToken(True, 0, 3, content)
    content = "false"
    token = tokenize_json(content)
    assert token == ScalarToken(False, 0, 3, content)
    content = "[3, 1]"
    token = tokenize_json(content)
   