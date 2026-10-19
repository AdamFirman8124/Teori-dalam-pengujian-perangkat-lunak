

# Generated at 2022-06-14 14:56:25.127949
# Unit test for constructor of class DictToken
def test_DictToken():
    content_dict_token = dict()
    value_dict_token = dict()
    key_token1 = ScalarToken(1, 1, 2)
    value_token1 = ScalarToken(2, 2, 4)
    key_token2 = ScalarToken(2, 4, 5)
    value_token2 = ScalarToken(3, 6, 7)
    key_token3 = ScalarToken(3, 8, 10)
    value_token3 = ScalarToken(4, 10, 11)
    value_dict_token[key_token1] = value_token1
    value_dict_token[key_token2] = value_token2
    value_dict_token[key_token3] = value_token3
    content_dict_token[1] = ScalarToken(1, 1, 2)
    content

# Generated at 2022-06-14 14:56:26.880553
# Unit test for method __eq__ of class Token
def test_Token___eq__():
  try:
    Token.__eq__(Token)
  except:
    return 1
  else:
    return 0


# Generated at 2022-06-14 14:56:28.260807
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken(value = None, start_index = None, end_index = None, content = None) is not None

# Generated at 2022-06-14 14:56:35.756278
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import copy
    import typing
    import unittest

    from typesystem.parser import Token, DictToken

    class FakeDictToken(DictToken):
        def _get_value(self) -> dict:
            return self._value

    class FakeToken(Token):
        def _get_value(self) -> typing.Any:
            return self._value

    class TokenTestCase(unittest.TestCase):
        def test_eq(self):
            token = FakeToken("", 0, 0)
            self.assertEqual(token, token)
            self.assertEqual(token, copy.copy(token))
            self.assertNotEqual(token, FakeToken("", 100, 100))

# Generated at 2022-06-14 14:56:47.306033
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.compat import OrderedDict
    from typesystem.base import String, Number
    from typesystem.enums import StringFormat, StringTypes
    e = OrderedDict()
    e["a"] = String("", StringTypes.STRING,StringFormat.ANY)
    e["b"] = Number("",1,2.0)
    d = DictToken(e, 0, 1,u'{"a":"1","b":1}')
    assert d.start == Position(1,1,0)
    assert d.end == Position(1,14,1)
    assert d_get_value() == {"a":1,"b":1}
    assert d._get_child_token("a") == d._value["a"]
    assert d._get_child_token("b") == d._value["b"]

# Generated at 2022-06-14 14:56:56.776267
# Unit test for constructor of class DictToken
def test_DictToken():
    input_ = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    expected_ = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    assert DictToken(0, 0, {}) == DictToken(0, 0, {})
    assert DictToken(0, 0, input_)._value == expected_
    assert DictToken(0, 0, input_).string == ''
    assert DictToken(0, 0, input_).start == Position(1, 1, 0)
    assert DictToken(0, 0, input_).end == Position(1, 1, 0)
    #assert DictToken(0, 0, input_).lookup([0, 0, 0]) == DictToken(0, 0

# Generated at 2022-06-14 14:57:06.311258
# Unit test for constructor of class DictToken
def test_DictToken():
    # test for Token class
    token=Token("1",2,3,"")
    assert token.start.column==1
    assert token.start.index==2
    assert token.start.line==1
    assert token.end.column==1
    assert token.end.index==3
    assert token.end.line==1
    assert token.string=="1"
    assert token.value=="1"
    # test for ScalarToken class
    scalar_token=ScalarToken("1",2,3,"")
    assert scalar_token.start.column==1
    assert scalar_token.start.index==2
    assert scalar_token.start.line==1
    assert scalar_token.end.column==1
    assert scalar_token.end.index==3
    assert scalar_token

# Generated at 2022-06-14 14:57:09.497117
# Unit test for constructor of class DictToken
def test_DictToken():
    data= {"key1": "value1", "key2": "value2"}
    my_dict_token = DictToken(data, 0,1)
    assert my_dict_token is not None


# Generated at 2022-06-14 14:57:17.967752
# Unit test for constructor of class DictToken
def test_DictToken():
    a = ScalarToken('a', 1, 2)
    value_token = ScalarToken('a', 1, 2)
    dict_token = DictToken(dict(a=value_token), 1, 2)
    assert dict_token._value['a'] == value_token

    b = ScalarToken('b', 1, 2)
    value_token2 = ScalarToken('b', 1, 2)
    dict_token2 = DictToken(dict(b=value_token2), 1, 2)
    assert dict_token2._value['b'] == value_token2



# Generated at 2022-06-14 14:57:22.057527
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    a = ScalarToken(value='hi', start_index=3, end_index=7, content='')
    b = ScalarToken(value='hi', start_index=3, end_index=7, content='')
    assert a == b

test_Token___eq__()

# Generated at 2022-06-14 14:57:28.111841
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(None, None, None) == Token(None, None, None)



# Generated at 2022-06-14 14:57:37.804403
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.tokenizer import _Dict, _List, _Scalar
    from typesystem.tokenizer import TokenType

    dict_token = DictToken(
        {
            _Dict(
                {
                    _Scalar("a", TokenType.INT): 10,
                    _Scalar("b", TokenType.STR): "str",
                },
                start_index=0,
                end_index=1,
            ): 20,
            _Scalar("a", TokenType.INT): 10,
        },
        start_index=0,
        end_index=2,
        content="",
    )
    print(dict_token)
    

# Generated at 2022-06-14 14:57:40.741519
# Unit test for constructor of class DictToken
def test_DictToken():
    my_dict = DictToken({"a" : "b"}, 1, 2)
    my_dict2 = DictToken({"a" : "b"}, 1, 2)
    my_dict3 = DictToken({"a" : "c"}, 1, 2)
    assert my_dict == my_dict2
    assert my_dict != my_dict3
    my_dict4 = DictToken({"a" : "b"}, 2, 1)
    assert my_dict != my_dict4


# Generated at 2022-06-14 14:57:50.116138
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 10
    content = "key1: 123, key2: 456"
    token = DictToken({start_index: "key1", end_index: "key2"}, start_index, end_index, content)
    assert token.string == "key1: 123, key2: 456"
    assert token.value == {start_index: end_index}
    assert token.start == Position(1, 5, 0)
    assert token.end == Position(1, 18, 10)
    assert token.lookup(start_index)
    assert token.lookup_key(start_index)
    assert token == DictToken
    assert hash(token)


# Generated at 2022-06-14 14:57:51.887670
# Unit test for constructor of class DictToken
def test_DictToken():
	print(DictToken({"a": 1}, 10, 12, content = "123"))


# Generated at 2022-06-14 14:57:56.082053
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken('value1', 0, 1)
    token2 = ScalarToken('value2', 0, 1)
    assert(token1 == token2)
    token3 = ScalarToken('value2', 2, 3)
    assert(not (token2 == token3))
test_Token___eq__()

# Generated at 2022-06-14 14:58:01.171747
# Unit test for constructor of class DictToken
def test_DictToken():
    obj = DictToken({}, 0, 3)
    assert obj._value == {}
    assert obj._start_index == 0
    assert obj._end_index == 3
    assert obj._content == ""
    assert str(obj) == "DictToken({})"
    assert obj == DictToken({}, 0, 3)

# Generated at 2022-06-14 14:58:03.841272
# Unit test for constructor of class DictToken
def test_DictToken():
    assert isinstance(DictToken, object)
    assert issubclass(DictToken, dict)
    assert issubclass(DictToken, Token)



# Generated at 2022-06-14 14:58:06.771722
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(None, 0, 0)
    token2 = Token(None, 0, 0)
    assert (token1 == token2) == True


# Generated at 2022-06-14 14:58:09.930426
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(None, 1, 2)
    token2 = Token(None, 1, 3)

    assert token1 != token2
    # Ensure class invariant
    assert not operator.is_(token1, token2)

# Generated at 2022-06-14 14:58:27.418264
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {
        "name": ScalarToken("name", 0, 1),
        "age": ScalarToken("age", 3, 4),
    }
    token = DictToken(d, 0, 10, "name")
    assert token.value == {"name": "name", "age": "age"}
    assert token.start.line == 1
    assert token.start.column == 1
    assert token.start.index == 0
    assert token.end.line == 1
    assert token.end.column == 10
    assert token.end.index == 10
    assert token.string == "name"
    assert token.lookup([]) is token
    assert token.lookup_key([]) is token
    assert token.lookup([0]) is d["name"]
    assert token.lookup([1]) is d["age"]
   

# Generated at 2022-06-14 14:58:39.321348
# Unit test for constructor of class DictToken
def test_DictToken():
    value = {"key1" : "val1"}
    start_index = 10
    end_index = 20
    content = "This is the content"
    token = DictToken(value, start_index, end_index, content)
    assert token.string == "This is the content"
    assert token.value == {"key1" : "val1"}
    assert token.start == Position(2, 3, 10)
    assert token.end == Position(2, 13, 20)
    assert token.lookup(["key1"]).string == "val1"
    assert token.lookup_key(["key1"]).string == "key1"
    assert str(token) == "DictToken({'key1': 'val1'})"
    assert token == DictToken(value, start_index, end_index, content)

# Generated at 2022-06-14 14:58:40.804666
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(1, 2, 3)
    token2 = Token(1, 2, 3)
    assert token1 == token2

# Generated at 2022-06-14 14:58:52.141473
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t = Token(value = 1, start_index = 1, end_index = 1, content = "")
    t2 = Token(value = 1, start_index = 1, end_index = 1, content = "")
    assert t == t2
    t3 = Token(value = 2, start_index = 1, end_index = 1, content = "")
    assert not (t == t3)
    t4 = Token(value = 1, start_index = 2, end_index = 1, content = "")
    assert not (t == t4)
    t5 = Token(value = 1, start_index = 1, end_index = 2, content = "")
    assert not (t == t5)


# Generated at 2022-06-14 14:59:04.088808
# Unit test for constructor of class DictToken
def test_DictToken():
    class DictTokenTest(DictToken):
        def __init__(self, value: typing.Any, start_index: int, end_index: int, content: str = "") -> None:
            super().__init__(value, start_index, end_index, content)
            self._value = value
            self._start_index = start_index
            self._end_index = end_index
            self._content = content
    # test for DictToken.__init__(self, value: typing.Any, start_index: int, end_index: int, content: str = "") -> None
    # __init__ is a non-public method, user cannot use it directly.
    Test_1 = DictTokenTest({}, 1, 3)
    Test_2 = DictTokenTest({'a':1}, 1, 3)

# Generated at 2022-06-14 14:59:12.224395
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    value = "abcd"
    start_index = 0
    end_index = len(value) - 1
    content = value
    token1 = Token(value, start_index, end_index, content)
    token2 = Token(value, start_index, end_index, content)
    token3 = Token(None, start_index, end_index, content)
    assert token1 == token2
    assert token1 != token3

if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 14:59:15.449394
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({}) == DictToken({})
    assert [DictToken({})] == [DictToken({})]
    assert DictToken({}) in [DictToken({})]


# Generated at 2022-06-14 14:59:21.805182
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem import Scalar, Dict
    DictToken([0, 0], 0, 9)
    DictToken([0, 0], 0, 9)
    d = {'a': 1}
    dt1 = DictToken([0, 0], 0, 9)
    dt2 = DictToken([0, 0], 0, 9)
    assert dt1.__eq__(dt2) == True
    assert dt1.__eq__(1) == False


# Generated at 2022-06-14 14:59:23.389393
# Unit test for constructor of class DictToken
def test_DictToken():
    assert [1, 2] in [1, 2, 3]

# Generated at 2022-06-14 14:59:28.017059
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.testing.fixtures import token

    class A:
        _value = 0
        _start_index = 1
        _end_index = 2

    assert token._Token.__eq__(token.token, A()) == False
    assert token._Token.__eq__(token.token, token.token) == True

# Generated at 2022-06-14 14:59:42.806705
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    ### START CODE HERE ###
    token = Token(1, 4, 7, "hello")
    other = Token(1, 4, 7, "hello")
    
    assert token.__eq__(other) == True
    ### END CODE HERE ###


# Generated at 2022-06-14 14:59:48.193076
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class TokenTest(Token):
        def __init__(self):
            self._value = "test"
            self._start_index = 0
            self._end_index = 0
            self._content = ""

        def _get_value(self):
            return self._value

    t1 = TokenTest()
    t2 = TokenTest()

    assert t1 == t2

# Generated at 2022-06-14 15:00:00.208500
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # arrange
    string = "test"
    start_index = 0
    end_index = len(string) - 1
    content = ""
    value = "test"
    token_1 = Token(value, start_index, end_index, content)
    token_2 = Token(value, start_index, end_index, content)
    token_3 = Token(value, start_index + 1, end_index, content)
    token_4 = Token(value, start_index, end_index + 1, content)
    token_5 = Token(value + "1", start_index, end_index, content)
    token_6 = "other"
    
    # act
    actual_result_1 = token_1 == token_1
    actual_result_2 = token_1 == token_2
    actual_result_

# Generated at 2022-06-14 15:00:04.552699
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    tok1=Token(1,2,3,"")
    tok2=Token(2,3,4,"")
    tok3=Token(1,2,3,"")
    assert tok1==tok3
    assert tok1!=tok2


# Generated at 2022-06-14 15:00:15.044078
# Unit test for constructor of class DictToken
def test_DictToken():
    print("Start testing...")
    print("Testing constructor of class DictToken")
    startIndex = 0
    endIndex = 0
    content = "test"
    args = [{'a': 1}, 0, 0, "test"]
    kwargs = {}
    testClass = DictToken(*args, **kwargs)
    assert testClass._value.keys() == {'a': 1}
    assert testClass._child_keys == {'a': 1}
    assert testClass._child_tokens == {'a': 1}
    assert testClass._start_index == 0
    assert testClass._end_index == 0
    assert testClass._content == "test"
    print("Finish testing...")


# Generated at 2022-06-14 15:00:25.388126
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken(1, 0, 2, "1").__eq__(ScalarToken(1, 0, 2, "1")), "__eq__() did not return the expected value."
    assert not ScalarToken(1, 0, 2, "1").__eq__(ScalarToken(2, 0, 2, "2")), "__eq__() did not return the expected value."
    assert not ScalarToken(1, 0, 2, "1").__eq__(ScalarToken(1, 1, 3, "1")), "__eq__() did not return the expected value."
    assert not ScalarToken(1, 0, 2, "1").__eq__(ScalarToken(1, 0, 3, "1")), "__eq__() did not return the expected value."

# Generated at 2022-06-14 15:00:31.224837
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Check if two identical tokens are considered equal
    t1 = Token(
        value = 'a',
        start_index = 0,
        end_index = 0,
        content = 'a',
    )
    t2 = Token(
        value = 'a',
        start_index = 0,
        end_index = 0,
        content = 'a',
    )
    assert (t1 == t2) == True, "__eq__ should return True because the two tokens have the same value."

    # Check if two different tokens are considered equal
    t1 = Token(
        value = 'a',
        start_index = 0,
        end_index = 1,
        content = 'a',
    )

# Generated at 2022-06-14 15:00:34.565582
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken(None, 0, 0)
    token2 = ScalarToken(None, 0, 0)
    assert token1 == token2


# Generated at 2022-06-14 15:00:44.984177
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 2
    content = "abcd"
    token_1 = ScalarToken("val", start_index, end_index, content)
    token_2 = ScalarToken("val1", start_index, end_index, content)
    val = {token_1: token_2}
    d = DictToken(val, start_index, end_index, content)
    assert d._get_value() == {'val': 'val1'}
    assert d._get_child_token('val') == token_2
    assert d._get_key_token('val') == token_1


# Generated at 2022-06-14 15:00:52.944282
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index_value_0=0
    end_index_value_0=1
    class_0=Token
    assert Token(None,start_index_value_0,end_index_value_0)==class_0(None,start_index_value_0,end_index_value_0)
    assert not Token(None,start_index_value_0,end_index_value_0)==class_0(None,start_index_value_0+1,end_index_value_0)
    assert not Token(None,start_index_value_0,end_index_value_0)==class_0(None,start_index_value_0,end_index_value_0+1)
    assert not Token(None,start_index_value_0,end_index_value_0)==class_

# Generated at 2022-06-14 15:01:03.012257
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({}, 0, 0)
    assert token is not None


# Generated at 2022-06-14 15:01:05.768844
# Unit test for constructor of class DictToken
def test_DictToken():
    """
    Create an instance of DictToken
    """
    obj = DictToken(value=None,start_index=None, end_index=None, content=None)
    # Assert type of created instance
    assert isinstance(obj, DictToken)


# Generated at 2022-06-14 15:01:08.817028
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({(1):'one',(2):'two'},0,1,2)
    assert t._child_keys == {(1): (1), (2): (2)}

# Generated at 2022-06-14 15:01:13.554713
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 0
    content = ""
    token = Token(value = 'value', start_index = start_index, end_index = end_index, content = content)


# Generated at 2022-06-14 15:01:22.391998
# Unit test for constructor of class DictToken
def test_DictToken():
    # Case 1: A single level dictionary with no keys
    content = '{""}'
    from typesystem.parser.lexer import lexer
    from typesystem.parser.parser import dictionary_parser
    from ply.lex import LexToken
    from typesystem.parser.position import Position
    from typesystem.parser.parser import DictionaryParser
    from typesystem.parser.parser import DictionaryParser
    from typesystem.parser.token_factory import token_factory

    tokenized_content = [tok for tok in lexer.lex(content)]
    assert tokenized_content == [LexToken('LBRACE', '{', Position(1, 1, 0)),
                                 LexToken('STRING', '', Position(1, 2, 1)),
                                 LexToken('RBRACE', '}', Position(1, 2, 2))]

    dictionary

# Generated at 2022-06-14 15:01:33.834840
# Unit test for constructor of class DictToken
def test_DictToken():
    key_token0 = ScalarToken(1,1,2,"key")
    value_token0 = ScalarToken(2,2,3,"value")
    key_token1 = ScalarToken(3,3,4,"key")
    value_token1 = ScalarToken(4,4,5,"value")
    args = ({key_token0:value_token0,key_token1:value_token1},1,6,"")
    kwargs = {}
    d = DictToken(*args,**kwargs)
    assert d._child_keys == {1:key_token0,3:key_token1}
    assert d._child_tokens == {1:value_token0,3:value_token1}
    assert d._start_index == 1
    assert d._end_index == 6

#

# Generated at 2022-06-14 15:01:35.636236
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({})

# Generated at 2022-06-14 15:01:37.341279
# Unit test for constructor of class DictToken
def test_DictToken():
    try:
        d = DictToken()
    except Exception:
        print("error")

# Generated at 2022-06-14 15:01:41.386544
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({1:2, 3:4}, start_index=0, end_index=0, content='abc')
    print(a)
    print(a.start)
    print(a.end)
    print(a.string)
    print(a.value)


# Generated at 2022-06-14 15:01:47.605341
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken(
        {
            ScalarToken(123, 0, 0): ScalarToken(456, 0, 0),
            ScalarToken(True, 0, 0): ScalarToken(False, 0, 0),
        },
        0,
        0,
    )
    assert dict_token._value == {
        ScalarToken(123, 0, 0): ScalarToken(456, 0, 0),
        ScalarToken(True, 0, 0): ScalarToken(False, 0, 0),
    }
    assert dict_token._start_index == 0
    assert dict_token._end_index == 0

# Generated at 2022-06-14 15:02:01.497465
# Unit test for constructor of class ListToken
def test_ListToken():
    token = ListToken(["a", "b", "c"], 1, 4, "abc")
    assert token.value == ["a", "b", "c"]
    assert token.start.line == 1
    assert token.start.column == 1
    assert token.start.index == 1
    assert token.end.line == 1
    assert token.end.column == 4
    assert token.end.index == 4
    assert token.string == "abc"


# Generated at 2022-06-14 15:02:11.626009
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    def token_generator(json):
        tokens = {}
        if type(json) is list:
            tokens["type"] = ListToken(
                [token_generator(item) for item in json],
                0,
                0,
                "",
            )
        elif type(json) is dict:
            tokens["type"] = DictToken(
                {
                    token_generator(key): token_generator(json[key])
                    for key in json
                },
                0,
                0,
                "",
            )
        else:
            tokens["type"] = ScalarToken(json, 0, 0, "")
        return tokens["type"]
    json={"name":"Bob","score":{"A":15,"B":20}}
    result=2
    token=token_generator(json)

# Generated at 2022-06-14 15:02:16.838944
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    _value = []
    _start_index = 1
    _end_index = 100
    instance = Token(_value, _start_index, _end_index, content="")
    other = Token(_value, _start_index, _end_index, content="")
    assert instance.__eq__(other)



# Generated at 2022-06-14 15:02:24.890425
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():

    class FakeToken(Token):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def _get_child_token(self, key: typing.Any) -> Token:
            return FakeToken(self._value + [key], self._start_index, self._end_index, self._content)

        def _get_key_token(self, key: typing.Any) -> Token:
            return FakeToken(self._value + [key], self._start_index, self._end_index, self._content)

        def _get_value(self) -> typing.Any:
            return self._value

    token = FakeToken(
        [1],
        0,
        0,
        '{"a": {"b": {"d": 2}}}'
    )


# Generated at 2022-06-14 15:02:28.113745
# Unit test for method __eq__ of class Token
def test_Token___eq__():

    # create Token object
    tok = Token(value=1, start_index=1, end_index=2)

    # check that Token object equal to itself
    assert tok == tok

# Generated at 2022-06-14 15:02:31.562132
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    token = ScalarToken(5, 10, 15, 'content')
    assert str(token.start) == '1, 6'
    assert token.string == '5'
    assert token._get_value() == 5


# Generated at 2022-06-14 15:02:34.563586
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    item = ScalarToken(1, 0, 0)
    result = hash(item)
    assert result is not None


# Generated at 2022-06-14 15:02:43.002083
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class ScalarToken_1(Token):
        def __hash__(self) -> typing.Any:
            return hash(self._value)

        def _get_value(self) -> typing.Any:
            return self._value

    token1 = ScalarToken_1("value1", 1, 1, "value1")
    token2 = ScalarToken_1("value2", 1, 1, "value2")
    assert token1 == token1
    assert token1 != token2
    assert token1 == ScalarToken_1("value1", 1, 1, "value1")

# Generated at 2022-06-14 15:02:49.438442
# Unit test for method lookup of class Token
def test_Token_lookup():
    token = Token(0, 0, 0, '')
    assert token._value is 0
    assert token.lookup([]) is token
    assert token.lookup_key([]) is token

test_token = Token(0, 0, 0, '')
test_token._get_value = lambda: None
test_token._get_child_token = lambda key: None
test_token._get_key_token = lambda key: None


# Generated at 2022-06-14 15:02:53.942041
# Unit test for method lookup of class Token
def test_Token_lookup():
    t = Token("\"[4, null, {\"a\": true}]\"", 0, 23)
    assert t.lookup([0, 0, 2])._get_value() == {'a' : True}
    assert t.lookup_key([1])._get_value() == 'a'



# Generated at 2022-06-14 15:03:05.978896
# Unit test for method lookup of class Token
def test_Token_lookup():
    from typesystem.parser import parse

    value = parse('{"foo": [1, 2, 3]}', content='{"foo": [1, 2, 3]}')
    assert value.lookup([0])._get_value() == 'foo'
    assert value.lookup([1])._get_value() == [1, 2, 3]
    assert value.lookup([1, 2])._get_value() == 3



# Generated at 2022-06-14 15:03:08.100597
# Unit test for constructor of class Token
def test_Token():
    v1 = "string"
    s_index = 5
    e_index = 10
    t1 = Token(v1, s_index, e_index)


# Generated at 2022-06-14 15:03:12.963368
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = Token(value='', start_index=0, end_index=0, content='')
    t = token.__repr__()
    assert(t == "Token('')"), "test_Token___repr__() failed"



# Generated at 2022-06-14 15:03:15.510131
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    t = ScalarToken(value=1, start_index=0, end_index=2)
    assert hash(t) == hash(1)

# Generated at 2022-06-14 15:03:21.701489
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = ScalarToken(42,0,42,"42")
    assert repr(token) == "ScalarToken('42')"
    token = DictToken({"42": 42},0,42,"42")
    assert repr(token) == "DictToken('42')"
    token = ListToken([42],0,42,"42")
    assert repr(token) == "ListToken('42')"

# Generated at 2022-06-14 15:03:26.473982
# Unit test for constructor of class Token
def test_Token():
    assert Token(3, 2, 4, 'abc').string == 'abc'
    assert Token(3, 2, 4, 'abc').value == 3
    assert Token(3, 2, 4, 'abc').start == Position(1, 1, 2)
    assert Token(3, 2, 4, 'abc').end == Position(1, 1, 4)


# Generated at 2022-06-14 15:03:31.393744
# Unit test for constructor of class Token
def test_Token():
    t = Token(5, 1, 2)
    print(t.__dict__)
    assert t.__dict__['_value'] == 5
    assert t.__dict__['_start_index'] == 1
    assert t.__dict__['_end_index'] == 2
    assert t.__dict__['_content'] == ''


# Generated at 2022-06-14 15:03:33.575639
# Unit test for constructor of class ListToken
def test_ListToken():
    obj = ListToken([Token({}, 0, 0, "")], 0, 0, "")
    assert isinstance(obj, ListToken)


# Generated at 2022-06-14 15:03:40.875702
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    # test ScalarToken
    token = ScalarToken(value=12.3, start_index=3, end_index=5, content='abcdefg')
    assert repr(token) == "ScalarToken('def')"
    # test ListToken
    token2 = ListToken(value=['ab','ef'], start_index=3, end_index=5, content='abcdefg')
    assert repr(token2) == "ListToken('def')"
    # test DictToken
    token3 = DictToken(value={'a':'b','c':'d'}, start_index=3, end_index=5, content='abcdefg')
    assert repr(token3) == "DictToken('def')"

# Generated at 2022-06-14 15:03:44.919144
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({0:0})._get_value() == {0:0}
    assert DictToken({1:1})._get_value() == {1:1}
    assert DictToken({0:0})._get_value() != {0:1}

# Generated at 2022-06-14 15:03:53.171987
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from inspect import signature

    # Get the function under test
    func = Token.__eq__

    # Check the number of arguments
    args = signature(func).parameters
    assert len(args) == 2

    # Check the argument names
    assert list(args.keys()) == ['self', 'other']


# Generated at 2022-06-14 15:03:58.013240
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_ = dict()
    dict_["key1"] = "value1"
    dict_["key2"] = "value2"
    dict_["key3"] = "value3"
    dict_token = DictToken(dict_, 0, 1, "test_text")
    assert dict_token.value == dict_ and dict_token.start == (1, 1, 0) and dict_token.end == (1, 1, 1)

# Generated at 2022-06-14 15:03:59.256573
# Unit test for method lookup of class Token
def test_Token_lookup():

    assert Token.lookup(["abc"]) == "abc"

# Generated at 2022-06-14 15:04:06.004927
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 0
    end_index = 2
    content = "ab"
    value = "a"
    token1 = Token(value, start_index, end_index, content)
    start_index = 0
    end_index = 2
    content = "ab"
    value = "a"
    token2 = Token(value, start_index, end_index, content)
    assert token1.__eq__(token2) == True
    end_index = 3
    content = "ab"
    value = "a"
    token2 = Token(value, start_index, end_index, content)
    assert token1.__eq__(token2) == False
    start_index = 0
    end_index = 2
    content = "abc"
    value = "a"

# Generated at 2022-06-14 15:04:13.911725
# Unit test for constructor of class Token
def test_Token():
    obj = Token(value=5, start_index=3, end_index=5)
    assert obj.string == ""
    assert obj.value is None
    assert obj.start is None
    assert obj.end is None
    obj = Token(value=5, start_index=3, end_index=5, content="abcdef")
    assert obj.string == "de"
    assert obj.value is None
    assert obj.start == Position(1, 3, 3)
    assert obj.end == Position(1, 5, 5)
    obj = Token(value=None, start_index=0, end_index=0, content="abcdef")
    assert obj.lookup([0, 1]) is None
    assert obj.lookup_key([0, 1]) is None
    assert obj.value is None
    assert obj.start

# Generated at 2022-06-14 15:04:18.485138
# Unit test for constructor of class ListToken
def test_ListToken():
    t = ListToken([1,2,3], 10, 11)
    assert t._value == [1,2,3]
    assert t._start_index == 10
    assert t._end_index == 11
    assert t._content == ""


# Generated at 2022-06-14 15:04:23.254897
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 1
    end_index = 2
    _index = 0
    content = "content"
    dt = DictToken(_index, start_index, end_index, content)
    assert dt._start_index == start_index
    assert dt._end_index == end_index
    assert dt._content == content


# Generated at 2022-06-14 15:04:29.333119
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import Position

    # equal
    a = ScalarToken('a',0,0)
    b = ScalarToken('a',0,0)
    assert a == b

    # not equal
    c = ScalarToken('c',0,0)
    assert a != c
    assert b != c

    # unequal start_index
    b = ScalarToken('a',1,0)
    assert a != b

    # unequal end_index
    b = ScalarToken('a',0,1)
    assert a != b


# Generated at 2022-06-14 15:04:31.944873
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    st = ScalarToken('a', 50, 100)
    assert hash(st) == hash('a')


# Generated at 2022-06-14 15:04:35.046347
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Given
    token = Token((1, 2, 3), 3, 4, content='0123')

    # When
    results = token.__eq__(token)

    # Then
    assert results is True

# Generated at 2022-06-14 15:04:49.372173
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = Token(
        value="",
        start_index=0,
        end_index=0,
        content="",
    )
    assert token.__repr__() == "Token('')"


# Generated at 2022-06-14 15:04:58.729793
# Unit test for constructor of class DictToken
def test_DictToken():

    #Variable to pass in __init__
    dict_val = {'key_1': "val_1", 'key_2': "val_2"}
    #This is a sample value to check the value property of DictToken
    dict_val_token = {'key_1': "val_1", 'key_2': "val_2"}
    # Current implementation of classes is this way only, Token class and DictToken class and the variable is not changed
    # But if we had implemented in a better way, then this test would fail
    from typesystem.types import Object
    if(isinstance(dict_val, Object)):
        assert(True)
    else:
        assert(False)

    #Here we are passing the Object value
    dict_token_obj = DictToken(dict_val, 0, 1)

    #This is

# Generated at 2022-06-14 15:05:04.545387
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    t = ScalarToken(value="a", start_index=1, end_index=1)
    assert t._get_value() == "a"
    assert t.value == "a"
    assert t.start == Position(line_no=1, column_no=2, index=1)
    assert t.end == Position(line_no=1, column_no=2, index=1)
    assert t.string == "a"

# Generated at 2022-06-14 15:05:06.000428
# Unit test for method lookup of class Token
def test_Token_lookup():
    token = ListToken(["Test"], 0, 7, "Test")
    assert token.lookup([]).string == "Test"

# Generated at 2022-06-14 15:05:11.496618
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import typesystem.token
    obj1 = typesystem.token.Token("abc", 1, 3)
    obj2 = typesystem.token.Token("abc", 1, 3)
    obj3 = typesystem.token.Token("def", 2, 4)
    obj4 = typesystem.token.DictToken({})
    assert(obj1 == obj2)
    assert(obj1 != obj3)
    assert(obj1 != obj4)


# Generated at 2022-06-14 15:05:14.468642
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    token = ScalarToken("bar", 2, 4)
    expected = hash("bar")
    assert token.__hash__() == expected


# Generated at 2022-06-14 15:05:20.894885
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    # Setup
    value_ = 'value'
    start_index_ = 0
    end_index_ = 1
    content_ = 'content'
    obj = Token(value_, start_index_, end_index_, content_)
    # Test
    assert obj.__repr__() == 'Token(\'value\')', "Test case failed!"


# Generated at 2022-06-14 15:05:23.589682
# Unit test for constructor of class ListToken
def test_ListToken():
    t = ListToken([], 0, 0)
    assert t._value == []
    assert t._start_index == 0
    assert t._end_index == 0
    assert t._content == ""

# Generated at 2022-06-14 15:05:26.301192
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    s = ScalarToken("test", 0, 0)
    return s


# Generated at 2022-06-14 15:05:33.952876
# Unit test for constructor of class DictToken
def test_DictToken():
    # Test 1: Test constructor with valid inputs
    tokens = {}
    results = DictToken(tokens, 0, 1, 'Hello,World')
    assert results._child_keys == {}
    assert results._child_tokens == {}

    # Test 2: Test constructor with invalid inputs
    try:
        DictToken("hi", 0, 1, 'Hello,World')
        assert False
    except:
        assert True



# Generated at 2022-06-14 15:05:44.495786
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    try:
        Token(None, None, None).__repr__()
        assert False
    except NotImplementedError:
        assert True



# Generated at 2022-06-14 15:05:45.745337
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({"a": 1}, 0, 1)._value == {"a": 1}


# Generated at 2022-06-14 15:05:52.670879
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    assert ScalarToken(None, 0, 0, '').__hash__() == None
    assert ScalarToken(0, 0, 0, '').__hash__() == 0
    assert ScalarToken(1, 0, 0, '').__hash__() == 1
    assert ScalarToken(1.1, 0, 0, '').__hash__() == hash(1.1)
    assert ScalarToken('a', 0, 0, '').__hash__() == 97
    assert ScalarToken('abc', 0, 0, '').__hash__() == 97 + 98*256 + 99*256*256
    assert ScalarToken(True, 0, 0, '').__hash__() == 1
    assert ScalarToken(False, 0, 0, '').__hash__() == 0

# Generated at 2022-06-14 15:05:54.506308
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.schema import Schema
    import typesystem
    test_DictToken = DictToken({'a':1,'b':2},0,3)
    assert(isinstance(test_DictToken,DictToken))


# Generated at 2022-06-14 15:05:58.481261
# Unit test for constructor of class Token
def test_Token():
    token = Token("content",1,2,content="content")
    assert token.value == "content"
    assert token.start == 1
    assert token.end == 2
    assert token.string == token.value


# Generated at 2022-06-14 15:06:06.623886
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test - Test for equality of two tokens that refer to the same value.
    token_1 = ScalarToken('The value of this token.', 20, 32)
    token_2 = ScalarToken('The value of this token.', 20, 32)
    assert token_1 == token_2
    # Test - Test for inequality of two tokens that are different.
    token_1 = ScalarToken('The value of this token.', 20, 32)
    token_2 = ScalarToken('The value of another token.', 20, 32)
    assert not token_1 == token_2
    # Test - Test for inequality of token and any other object.
    token_1 = ScalarToken('The value of this token.', 20, 32)
    assert not token_1 == 'Mock'

# Generated at 2022-06-14 15:06:10.040890
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    obj = Token(value=1, start_index=22, end_index=33, content='str')
    assert obj.__repr__() == "Token('str')"
