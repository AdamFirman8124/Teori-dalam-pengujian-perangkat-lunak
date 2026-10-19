

# Generated at 2022-06-14 14:56:17.919086
# Unit test for constructor of class DictToken
def test_DictToken():
    x = DictToken(value = {}, start_index = 1, end_index = 2)
    assert x
    assert x._value == {}
    assert x._start_index == 1
    assert x._end_index == 2


# Generated at 2022-06-14 14:56:23.421183
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from .test_lexer import _make_token
    from .lexer_test_data import lexer_test_data
    token1 = _make_token(lexer_test_data[0][0])
    token2 = _make_token(lexer_test_data[0][0])
    token3 = _make_token(lexer_test_data[1][0])
    assert(token1 == token2)
    assert(token1 != token3)



# Generated at 2022-06-14 14:56:26.149731
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(value=None, start_index=None, end_index=None) == Token(value=None, start_index=None, end_index=None)


# Generated at 2022-06-14 14:56:31.158566
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Setup
    value = '1'
    start_index = 1
    end_index = 1
    content = '23'
    # Exercise
    token1 = Token(value, start_index, end_index, content)
    token2 = Token(value, start_index, end_index, content)
    # Verify
    result = token1.__eq__(token2)
    assert result == True



# Generated at 2022-06-14 14:56:34.525580
# Unit test for constructor of class DictToken
def test_DictToken():
    expected_value = {'key': 'value'}
    expected_start_index = 0
    expected_end_index = 5
    expected_content = "['key'~0:4]'value'~5:10]"
    assert DictToken(expected_value, expected_start_index, expected_end_index, expected_content)

# Generated at 2022-06-14 14:56:40.484963
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import String
    from typesystem.base import Structure

    string_token = ScalarToken(String("A"), 0, 0, "A")
    string_token2 = ScalarToken(String("A"), 0, 0, "A")
    assert string_token == string_token2

    dict_token = DictToken(
        {
            ScalarToken(String("A"), 0, 0, "A"): ScalarToken(String("B"), 0, 0, "B")
        },
        0,
        0,
        "A",
    )

# Generated at 2022-06-14 14:56:45.058708
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(1, 2, 3)
    token2 = Token(1, 2, 3)
    token3 = Token(2, 3, 4)
    assert token1 == token2
    assert not(token1 == token3)

# Generated at 2022-06-14 14:56:49.107202
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t = Token(
        value=1,
        start_index=0,
        end_index=0,
        content="1"
    )
    other = Token(
        value=1,
        start_index=0,
        end_index=0,
        content="1"
    )
    assert t == other



# Generated at 2022-06-14 14:56:56.588765
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(1, 1, 2, "content")
    token2 = Token(1, 1, 2, "content")
    assert token1 == token2
    token2._value = 2
    assert token1 != token2
    token2._value = 1
    assert token1 == token2
    token2._start_index = 2
    assert token1 != token2
    token2._start_index = 1
    assert token1 == token2
    token2._end_index = 3
    assert token1 != token2
    token2._end_index = 2
    assert token1 == token2

# Generated at 2022-06-14 14:57:05.106892
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    v1 = ScalarToken(1, 0, 1)
    v2 = ScalarToken(2, 0, 1)
    assert v1 is not v2
    assert v1 == v2
    assert not hash(v1) == hash(v2)

    dict_token = DictToken({v1: v2}, 0, 1)
    assert dict_token is not None

    list_token1 = ListToken([v1], 0, 1)
    assert list_token1 == list_token1

    list_token2 = ListToken([v2], 0, 1)
    assert list_token1 is not list_token2
    assert list_token1 == list_token2



# Generated at 2022-06-14 14:57:22.645052
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken(
        {
            ScalarToken('a', 0, 0): ScalarToken(2, 0, 0),
            ScalarToken('b', 1, 1): ListToken([ScalarToken(1, 1, 1)],
                                              1, 1),
            ScalarToken('c', 2, 2): ScalarToken(1, 2, 2)},
        0,
        2
    )
    assert dt._child_tokens['a'].string == 'a'
    assert dt._child_tokens['b'].string == '[1]'
    assert dt._child_tokens['c'].string == '1'
    assert dt._child_keys['a'].string == 'a'
    assert dt._child_keys['b'].string == 'b'
   

# Generated at 2022-06-14 14:57:23.777293
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert(False)

# Generated at 2022-06-14 14:57:29.560369
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_obj = Token(["abc", "def"], 0, 3)
    token_obj1 = Token(["abc", "def"], 0, 3)
    assert token_obj == token_obj1
    assert not (token_obj != token_obj1)
    assert not token_obj == "abc"  # type: ignore
    assert token_obj != "abc"  # type: ignore





# Generated at 2022-06-14 14:57:34.948709
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1: Token = ScalarToken(value=1, start_index=0, end_index=1, content="1")
    t2: Token = ScalarToken(value=1, start_index=0, end_index=1, content="1")
    t3: Token = ScalarToken(value=2, start_index=0, end_index=1, content="1")
    assert t1 == t2
    assert t2 == t1
    assert not t1 == t3
    assert not t2 == t3
    assert not t3 == t1
    assert not t3 == t2
    assert not t1 == 1
    assert not t2 == 2



# Generated at 2022-06-14 14:57:43.969953
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t = Token('value', 1, 2)
    t2 = Token('different_value', 1, 2)
    t3 = Token('value', 2, 3)
    t4 = Token('value', 1, 2, 'content')
    assert t == t
    assert t != t2
    assert t != t3
    assert t != t4
    assert t2 != t
    assert t2 == t2
    assert t2 != t3
    assert t2 != t4
    assert t3 != t
    assert t3 != t2
    assert t3 == t3
    assert t3 != t4
    assert t4 != t
    assert t4 != t2
    assert t4 != t3
    assert t4 == t4

# Generated at 2022-06-14 14:57:54.381237
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(1, 10, 20)
    token2 = Token(1, 10, 20)
    token3 = Token(2, 10, 20)
    token4 = Token(1, 20, 30)
    token5 = Token(1, 10, 20, 'a')

    assert token1 == token2
    assert not token1 == token3
    assert not token1 == token4
    assert not token1 == token5
    assert hash(token1) == hash(token2)
    assert hash(token1) != hash(token3)
    assert hash(token1) != hash(token4)
    assert hash(token1) != hash(token5)
    assert not (token1 != token2)
    assert token1 != token3
    assert token1 != token4
    assert token1 != token5


# Generated at 2022-06-14 14:57:58.493247
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken(value=1, start_index=0, end_index=0)
    token2 = ScalarToken(value=1, start_index=0, end_index=0)
    assert token1 == token2

# Generated at 2022-06-14 14:58:02.770697
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 1
    end_index = 5
    value = 6
    content = "asdfg"
    token1 = Token(value, start_index, end_index, content)
    
    assert token1.__eq__(token1) == True
    

# Generated at 2022-06-14 14:58:07.554851
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index=0
    end_index=1
    value=[]
    token = Token(value,start_index,end_index)
    assert token._get_value() == value
    assert token._start_index == start_index
    assert token._end_index == end_index
    assert token == token

# Generated at 2022-06-14 14:58:15.173730
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class Object1:
        pass

    class Object2:
        pass

    class Object3:
        pass

    class Object4:
        pass

    obj1 = Object1()
    obj2 = Object2()
    obj3 = Object3()
    obj4 = Object4()

    token1 = Token(value=obj1, start_index=obj2, end_index=obj3, content=obj4)
    token2 = Token(value=obj1, start_index=obj2, end_index=obj3, content=obj4)


# Generated at 2022-06-14 14:58:25.016216
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    print(Token.__eq__.__doc__)
    t = Token(1,2,3)
    t1 = Token(1,2,3)
    t2 = Token(3,4,5)
    assert(t==t1)
    assert(t!=t2)

# Generated at 2022-06-14 14:58:32.256437
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token('value', 1, 2) == Token('value', 1, 2)
    assert not Token('value', 1, 2) == Token('value', 2, 3)
    assert not Token('value', 3, 4) == Token('value', 1, 2)
    assert not Token('value', 2, 3) == Token('value', 1, 2)
    assert not Token('value', 1, 2) == Token('value', 1, 2, 'abc')
    assert Token('value', 1, 2, 'abc') == Token('value', 1, 2, 'abc')
    assert not Token('value', 1, 2, 'abc') == Token('value', 1, 2, 'ab')
    assert not Token('value', 1, 2) == 123


# Generated at 2022-06-14 14:58:34.473055
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    value = None
    start_index = 1
    end_index = 2
    content = "pytest"
    token = Token(value, start_index, end_index, content)
    token_last_ = token.__eq__(value)
    assert token_last_ is False


# Generated at 2022-06-14 14:58:37.332697
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    obj = Token(object(), object(), object(), object())
    obj2 = Token(obj._value, obj._start_index, obj._end_index)
    assert obj == obj2

# Generated at 2022-06-14 14:58:40.135112
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    """
    Test method __eq__ of class Token
    """
    token = Token(value=None, start_index=None, end_index=None)
    assert not (token == None)


# Generated at 2022-06-14 14:58:43.613411
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token("a", 1, 2, "abc")
    assert(token == Token("a", 1, 2, "abc")) == True

# Generated at 2022-06-14 14:58:53.077784
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(
        None,
        start_index=0,
        end_index=0,
        content="",
    ) == Token(
        None,
        start_index=0,
        end_index=0,
        content="",
    )
    assert not Token(
        None,
        start_index=0,
        end_index=0,
        content="",
    ) == ""
    assert Token(
        "foo",
        start_index=0,
        end_index=2,
        content="foo",
    ) != Token(
        "bar",
        start_index=0,
        end_index=2,
        content="bar",
    )



# Generated at 2022-06-14 14:58:54.941983
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t = Token('abc',1,2,'abc')
    t1 = Token('abc',1,2,'abc')
    t2 = Token('abcd',1,2,'abcd')
    assert t==t1
    assert t != t2


# Generated at 2022-06-14 14:58:58.724914
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t = Token(b'[', 0, 0)
    t1 = Token(b'[', 0, 0)
    t2 = Token(b',', 0, 0)
    assert t == t1
    assert t != t2


# Generated at 2022-06-14 14:58:59.721938
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert True


# Generated at 2022-06-14 14:59:16.389949
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(1, 2, 3, "")
    assert token == token
    assert token == eval(repr(token))
    assert not (token != token)



# Generated at 2022-06-14 14:59:17.840871
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test positive cases.
    # Test negative cases.
    pass


# Generated at 2022-06-14 14:59:19.969052
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken(1, 0, 0)
    token2 = ScalarToken(1, 0, 0)
    assert token1 == token2

# Generated at 2022-06-14 14:59:24.229019
# Unit test for constructor of class DictToken
def test_DictToken():
    expected_token = "{'key1': 'value1'}"
    constructed_token = DictToken(expected_token, 0, 15)
    assert repr(expected_token) == repr(constructed_token)


# Generated at 2022-06-14 14:59:30.759786
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    bn = BufferNode(b"a")
    bn2 = BufferNode(b"a")
    bn3 = BufferNode(b"b")
    bn4 = BufferNode(b"b")
    assert bn is bn
    assert bn == bn2
    assert not bn == bn3
    assert not bn == bn4
    assert not bn == object()
    assert not bn == None

# Generated at 2022-06-14 14:59:37.743304
# Unit test for constructor of class DictToken
def test_DictToken():
    myDict = {1:1, 2:2, 3:3}
    start_index = 1
    end_index = 2
    content = ""
    myDicttoken = DictToken(myDict,start_index,end_index,content)
    print(myDicttoken)
    assert myDicttoken.__eq__(myDicttoken) == True
    
    

# Generated at 2022-06-14 14:59:48.151576
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    test_cases = [
        ("test_value", 0, 2, "test_content", True, False),
        ("test_value", 0, 2, "test_content", False, True),
        ("test_value", 0, 2, "test_content", False, False),
        ("test_value", 0, 2, "test_content", True, True),
    ]

    for kwargs, __, ___, ____, isinstance_other, expected in test_cases:
        with given:
            token = Token(**kwargs)
            other = object() if not isinstance_other else Token(**kwargs)
        with when:
            actual = token.__eq__(other)
        with then:
            actual.should.be.equal(expected)

# Generated at 2022-06-14 14:59:55.924969
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 0
    end_index = 1
    content = "2"
    string = "2"
    value = 2
    token1 = ScalarToken(value, start_index, end_index, content)
    token2 = ScalarToken(value, start_index, end_index, content)
    assert token1 == token2
    token3 = ScalarToken(value, start_index, end_index + 1, content)
    assert token1 != token3



# Generated at 2022-06-14 14:59:57.880976
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert (Token(1, 0, 0) == Token(1, 0, 0))


# Generated at 2022-06-14 15:00:01.515620
# Unit test for constructor of class DictToken
def test_DictToken():
    print('Testing constructor of class DictToken...', end='')
    token = DictToken(value={}, start_index=0, end_index=1, content='dd')
    assert(token._value=={})
    print('Passed!')


# Generated at 2022-06-14 15:00:40.070485
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Calls the __eq__ method of the class Token with a correct parameter
    assert Token(1, 0, 0) == Token(1, 0, 0)
    assert Token(1, 1, 1) == Token(1, 1, 1)
    assert Token(1, 0, 1) == Token(1, 0, 0)
    assert Token(1, 0, 1) == Token(1, 1, 1)
    assert Token(1, 0, 1) == Token(1, 0, 1)
    assert Token(1, 1, 0) == Token(1, 0, 0)
    assert Token(1, 1, 0) == Token(1, 1, 1)
    assert Token(1, 1, 0) == Token(1, 1, 0)
    assert Token(1, 0, 0) == Token(1, 0, 1)

# Generated at 2022-06-14 15:00:47.569084
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 10
    a = start_index + 3
    b = end_index - 3

    token = DictToken({"hello": "world"}, start_index, end_index, "helloworld")

    assert token._value == {"hello" : "world"}
    assert token._start_index == start_index
    assert token._end_index == end_index
    assert token._content == "helloworld"
    assert token.string == "helloworld"

#  Unit test for constructor of class ListToken

# Generated at 2022-06-14 15:00:59.406011
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(value=None, start_index=None, end_index=None, content=None)
    token2 = Token(value=None, start_index=None, end_index=None, content=None)
    token3 = Token(value=None, start_index=None, end_index=None, content=None)
    token4 = Token(value=None, start_index=None, end_index=None, content=None)
    token5 = Token(value=None, start_index=None, end_index=None, content=None)

    assert token1.__eq__(token2) is NotImplemented
    assert token1.__eq__(token3) is NotImplemented
    assert token1.__eq__(token4) is NotImplemented

# Generated at 2022-06-14 15:01:03.012293
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class TestToken(Token):
        def _get_value(self):
            return self._value
    assert TestToken("value", 0, 5) == TestToken("value", 0, 5)

# Generated at 2022-06-14 15:01:07.879833
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 0
    end_index = 5
    value = "hello"
    content = "hello world"
    t1 = Token(value, start_index, end_index, content)
    t2 = Token(value, start_index, end_index, content)
    assert t1 == t2



# Generated at 2022-06-14 15:01:13.355421
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    test_cases = [
        {"_value": "test_value", "_start_index": 0, "_end_index": 1, "expected_output": True},
        {"_value": "test_value", "_start_index": 1, "_end_index": 1, "expected_output": False},
        {"_value": "test_value", "_start_index": 1, "_end_index": 0, "expected_output": False},
        {"_value": None, "_start_index": 1, "_end_index": 0, "expected_output": False},
    ]
    for case in test_cases:
        token_1 = Token(case["_value"], case["_start_index"], case["_end_index"])
        token_2 = Token(case["_value"], case["_start_index"], case["_end_index"])

# Generated at 2022-06-14 15:01:14.689390
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # TODO: Write unit tests for this method.
    pass


# Generated at 2022-06-14 15:01:17.069268
# Unit test for constructor of class DictToken
def test_DictToken():
    content = """
    {
        "a": 1,
        "b": 2
    }
    """
    dict_token = DictToken({}, 1, 4, content)
    assert dict_token.value == {}
    assert dict_token.start.index == 1
    assert dict_token.end.index == 4


# Generated at 2022-06-14 15:01:24.358892
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from jsonschema import validate
    from jsonschema.exceptions import ValidationError
    from pydantic import BaseModel
    from jsonschema.exceptions import ValidationError
    import json

    class ScalarToken_Pydantic_Model(BaseModel):
        value: typing.Any
        start_index: int
        end_index: int
        content: str

    class Token_Pydantic_Model(BaseModel):
        string: str
        value: typing.Any
        start: Position
        end: Position

    class Position_Pydantic_Model(BaseModel):
        line_no: int
        column_no: int
        index: int


# Generated at 2022-06-14 15:01:34.949747
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem import types

    schema = types.Schema(
        fields={"a": types.String(), "b": types.String(), "c": types.String()}
    )
    data = {"a": "1", "b": "2", "c": "3"}

    token_a = schema.token_class(value=data, start_index=0, end_index=0, content="")
    token_b = schema.token_class(value=data, start_index=0, end_index=0, content="")
    token_c = schema.token_class(value={"c": "3", "a": "1", "b": "2"}, start_index=0, end_index=0, content="")

    assert token_a == token_b
    assert not (token_a == token_c)



# Generated at 2022-06-14 15:02:04.378364
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Arbitrary instances
    token = Token
    assert token == token

# Generated at 2022-06-14 15:02:10.398873
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import json
    from hypihub.parser.tokenizer import tokenize

    original_text = """
      [
        {
          "key1": "value1",
          "key2": {
            "key3": "value3"
          }
        }
      ]
    """
    parsed = json.loads(original_text)
    token = tokenize(parsed, original_text)
    assert token == token
    assert not (token != token)



# Generated at 2022-06-14 15:02:14.568595
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = "a"
    t = Token(1, 0, 0, content)
    t2 = Token(1, 0, 0, content)
    assert t == t2



# Generated at 2022-06-14 15:02:17.552821
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    
    assert Token(None, 1, 2, "") == Token(None, 1, 2, "")
    
    assert Token(None, 1, 2, "") != Token(None, 1, 2, "")

# Generated at 2022-06-14 15:02:29.079798
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.token import Token
    from typesystem.token import ScalarToken
    from typesystem.token import DictToken
    from typesystem.token import ListToken
    from typesystem.base import Position

    token1 = ScalarToken('1', 0, 0)
    token2 = ScalarToken('1', 1, 1)
    assert(token1 == token2)

    token1 = ScalarToken('1', 0, 0)
    token2 = ScalarToken('2', 0, 0)
    assert(not (token1 == token2))

    token1 = ListToken([ScalarToken('1', 0, 0)], 0, 0)
    token2 = ListToken([ScalarToken('1', 0, 0)], 0, 0)
    assert(token1 == token2)


# Generated at 2022-06-14 15:02:41.535586
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import random
    for i in range(200):
        value_1 = random.randint(0, 1000)
        value_2 = random.randint(0, 1000)
        start_index_1 = random.randint(0, 1000)
        start_index_2 = random.randint(0, 1000)
        end_index_1 = random.randint(0, 1000)
        end_index_2 = random.randint(0, 1000)
        content_1 = ''
        content_2 = ''
        token_1 = Token(value_1, start_index_1, end_index_1, content_1)
        token_2 = Token(value_1, start_index_1, end_index_1, content_1)
        assert(token_1 == token_2)
        token_1 = Token

# Generated at 2022-06-14 15:02:48.455298
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from collections import OrderedDict
    from .string_parse import _Token
    from .nodes import Scalar

    # Create an object of class Token to test with
    value = Scalar('...', None, None)
    start_index = 0
    end_index = 2
    content = '...'
    token_obj = Token(value, start_index, end_index, content)

    # Create a token with different value
    value2 = Scalar('abc', None, None)
    different_value_token = _Token(value2, start_index, end_index, content)
    assert token_obj != different_value_token, "Compare token with different value should be False."

    # Create a token with different start_index
    start_index2 = 1

# Generated at 2022-06-14 15:02:51.338373
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token("", 0, 0) == Token("", 0, 0)
    assert not(Token("", 0, 0) != Token("", 0, 0))


# Generated at 2022-06-14 15:03:00.916030
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert not (ScalarToken(True, 0, 1) == ScalarToken(False, 0, 1))
    assert ScalarToken(True, 0, 1) == ScalarToken(True, 0, 1)
    assert not (ScalarToken(True, 0, 2) == ScalarToken(True, 0, 1))
    assert not (ScalarToken(True, 1, 1) == ScalarToken(True, 0, 1))

    assert not (ListToken([], 0, 1) == ListToken([], 0, 1))
    assert ListToken([ScalarToken(True, 0, 1)], 0, 1) == ListToken(
        [ScalarToken(True, 0, 1)], 0, 1
    )

# Generated at 2022-06-14 15:03:04.206652
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t = Token('a', 'b', 'c')
    t1 = Token('a', 'b', 'c')
    assert t == t1



# Generated at 2022-06-14 15:03:31.680805
# Unit test for constructor of class DictToken
def test_DictToken():
    DT = DictToken(value = {}, start_index = 1, end_index = 2)
    assert DT._value == {}
    assert DT._start_index == 1
    assert DT._end_index == 2
    assert DT._content == ""


# Generated at 2022-06-14 15:03:38.976679
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import ScalarToken
    from typesystem.base import StringToken
    from typesystem.base import Position
    from typesystem.base import DictToken

    start = Position(7,13,33)
    end = Position(9,9,45)

    a = ScalarToken(123, start, end)
    b = StringToken('abcde', start, end)
    content = '''
    {
        "a": 123,
        "b": "abcde"
    }
    '''
    token = DictToken({a:b}, start.index, end.index, content)

# Generated at 2022-06-14 15:03:48.247148
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.primitives import String
    from typesystem.structures import Dict
    from typesystem.utils import position
    test_dict = Dict({"one": String()}, position=position(1, 1))
    test_dict.validate("one", position(2, 3))
    assert DictToken({"one": ScalarToken(1, 0, 2)}, 1, 2, "one")._child_keys["one"].end == position(1, 1)
    assert DictToken({"one": ScalarToken(1, 0, 2)}, 1, 2, "one")._child_tokens["one"].start == position(1, 1)


# Generated at 2022-06-14 15:03:53.698906
# Unit test for constructor of class DictToken
def test_DictToken():
    keys = [ScalarToken(1, 0, 0), ScalarToken(2, 1, 1)]
    values = [ScalarToken(3, 0, 0), ScalarToken(4, 1, 1)]
    dic = {keys[0]: values[0], keys[1]: values[1]}
    a = DictToken(dic, 2, 2, "123")
    assert a._child_keys == {}
    assert a._child_tokens == {}


# Generated at 2022-06-14 15:03:58.566962
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({1:1}, 0, 1, '{"a": "b"}')
    assert t.value == {1:1}
    assert t.start.line == 1
    assert t.start.column == 1
    assert t.start.index == 0
    assert t.end.line == 1
    assert t.end.column == 8
    assert t.end.index == 7
    assert t.string == '{"a": "b"}'

# Generated at 2022-06-14 15:04:00.622875
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({}, 0, 0)
    assert d


# Generated at 2022-06-14 15:04:04.306024
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({}, 0, 0, "")
    assert DictToken({}, 0, 0, "") != {}
    assert DictToken({}, 0, 0, "") != Exception("")



# Generated at 2022-06-14 15:04:05.691607
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({}, 1, 2)
    assert token._start_index == 1
    assert token._end_index == 2
    assert token._value == dict()


# Generated at 2022-06-14 15:04:13.750600
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.primitives import Dictionary
    field = Dictionary(keys=ScalarToken(1, 0, 0), values=ScalarToken(2, 0, 0))
    d = DictToken({"a": 1, "b": 2}, 0, 0, content="abc")
    assert d.value == {"a": 1, "b": 2}
    assert d._child_keys == {"a": ScalarToken(1, 0, 0), "b": ScalarToken(2, 0, 0)}
    assert d._child_tokens == {1: ScalarToken(1, 0, 0), 2: ScalarToken(2, 0, 0)}

# Generated at 2022-06-14 15:04:15.404322
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(value, start_index, end_index, content)
    return d

# Generated at 2022-06-14 15:05:07.885217
# Unit test for constructor of class DictToken
def test_DictToken():
    args = (1, 2, 3, "a", "b", "c")
    kwargs = {"key1" : 1, "key2" : 2}
    dict_token = DictToken(args, kwargs)
    assert dict_token._get_value() == args
    assert dict_token._get_child_token(key) == kwargs[key]
    assert dict_token._get_key_token(key) == key

# Generated at 2022-06-14 15:05:11.900786
# Unit test for constructor of class DictToken
def test_DictToken():
    a = Token({"a": 1}, 1,1, "")
    assert a.value == {"a": 1}
    assert a.start == Position(1,1,1)
    assert a.end == Position(1,1,1)
    assert a.string == ""


# Generated at 2022-06-14 15:05:14.561980
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({1: 2})
    assert dt is not None


# Generated at 2022-06-14 15:05:16.291954
# Unit test for constructor of class DictToken
def test_DictToken():
	assert(DictToken({}, 0, 5)._end_index == 5)

# Generated at 2022-06-14 15:05:20.845861
# Unit test for constructor of class DictToken
def test_DictToken():
    x = {"a": "b", "c": "d"}
    y = DictToken(x, 0, 0)
    assert y._value["a"]._value == "b"
    assert y._value["c"]._value == "d"

# Generated at 2022-06-14 15:05:23.700063
# Unit test for constructor of class DictToken
def test_DictToken():
    d1 = {"A": 1}
    d2 = {"B": 2}
    ret1 = DictToken({"A": 1}, 0, 1)
    ret2 = DictToken({"B": 2}, 0, 1)
    if (ret1 == ret2):
        print("test DictToken(1) passed")
    else:
        print("test DictToken(1) failed")


# Generated at 2022-06-14 15:05:32.963209
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({'a':1, 'b':2}, 0, 1)
    dt1 = DictToken({'a':1, 'b':2}, 0, 1, 'abcdef')
    assert dt.start_index == 0 and dt.end_index == 1 and dt.content == ''
    assert dt1.start_index == 0 and dt1.end_index == 1 and dt1.content == 'abcdef'
    
    

# Generated at 2022-06-14 15:05:37.243382
# Unit test for constructor of class DictToken
def test_DictToken():
    dict = {1:2}
    dict_token = DictToken(dict, 0, 1, "")
    assert dict_token.string == "" and dict_token.start == Position(1, 1, 0) and dict_token.end == Position(1, 1, 0) and dict_token.value == dict and dict_token._get_value() == dict


# Generated at 2022-06-14 15:05:39.652283
# Unit test for constructor of class DictToken
def test_DictToken():
    # Arrange
    token = DictToken({'abc': 123})

    # Act
    result = token

    # Assert
    assert result!=None

# Generated at 2022-06-14 15:05:48.866426
# Unit test for constructor of class DictToken
def test_DictToken():
    import typesystem.base as base
    token = DictToken({}, 0, 1)
    assert token._value == {}
    assert token._start_index == 0
    assert token._end_index == 1
    assert token._get_value() == {}
    assert token.lookup([]) == token
    token = DictToken({base.ScalarToken(0, 0, 1): base.ScalarToken(1, 0, 1)}, 0, 1)
    assert token._value == {base.ScalarToken(0, 0, 1): base.ScalarToken(1, 0, 1)}
    assert token._start_index == 0
    assert token._end_index == 1
    assert token._get_value() == {0: 1}
    assert token.lookup([]) == token