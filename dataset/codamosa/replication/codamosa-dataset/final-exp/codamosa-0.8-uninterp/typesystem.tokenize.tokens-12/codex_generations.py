

# Generated at 2022-06-14 14:56:24.896241
# Unit test for constructor of class DictToken
def test_DictToken():
    from collections import OrderedDict
    from typesystem.base import Position
    from tokenizer import Tokenizer

    tokenizer = Tokenizer('{"a":1}')
    print(tokenizer.run())
    my_dict = tokenizer.run()
    my_token = DictToken(my_dict, 0, 5, content = '{"a":1}')
    assert my_token._child_tokens.keys() == ['a']
    assert my_token._child_tokens.values() == [ScalarToken(1, 4, 4, content = '{"a":1}')]
    assert my_token._child_keys.keys() == ['a']
    assert my_token._child_keys.values() == [ScalarToken('a', 2, 2, content = '{"a":1}')]

test

# Generated at 2022-06-14 14:56:30.702570
# Unit test for constructor of class DictToken
def test_DictToken():
    # Trailing comma
    a = {'a': 'a', 'b': 'b',}
    b = {'1': '1', '2': '2',}
    tokens = {'a': b, 'b': b,}
    typesystem_DictToken_obj = DictToken(a, 1, 8, tokens)
    assert typesystem_DictToken_obj._child_keys == {'b': b}
    assert typesystem_DictToken_obj._child_tokens == {'b': b}
    assert typesystem_DictTo

# Generated at 2022-06-14 14:56:32.434272
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Tests not written yet
    pass

# Generated at 2022-06-14 14:56:44.031782
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import Number
    from typesystem.base import Text
    from typesystem.base import Object
    from typesystem.base import Array

    number = Number()
    text = Text()
    object = Object({"foo": number, "bar": text})
    array = Array([number, text])

    assert ScalarToken(number, 0, 0) == ScalarToken(number, 0, 0)
    assert ScalarToken(number, 0, 0) != ScalarToken(number, 0, 1)
    assert ScalarToken(number, 0, 0) != ScalarToken(number, 1, 1)
    assert ScalarToken(number, 0, 0) != ScalarToken(text, 0, 0)

    # Dicts

# Generated at 2022-06-14 14:56:49.502835
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(0, 0, 0, "") == Token(0, 0, 0, "")
    assert Token(0, 0, 0, "") != 1
    assert Token(0, 0, 0, "") != Token(1, 0, 0, "")
    assert Token(0, 0, 0, "") != Token(0, 1, 0, "")
    assert Token(0, 0, 0, "") != Token(0, 0, 1, "")

# Generated at 2022-06-14 14:56:51.898362
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(None, 0, 0)
    token2 = Token(None, 0, 0)
    assert token == token2



# Generated at 2022-06-14 14:56:58.159853
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import random
    i = random.randrange(100)
    value = "value"
    class T(Token):
        def __init__(self, value: str, start_index: int, end_index: int, content: str = ""):
            super().__init__(value, start_index, end_index, content)
        def _get_value(self):
            return value
    for x in range(10000):
        t1 = T(value, i, i)
        t2 = T(value, i, i)
        assert t1 == t2

# Generated at 2022-06-14 14:57:02.827396
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    T1 = Token(3, 2, 5, "hello")
    assert(T1 == T1)
    assert(T1 == Token(3, 2, 5, "hello"))
    assert(T1 != Token(4, 2, 5, "hello"))
    assert(T1 != 1)
    assert(T1 != "hello")


# Generated at 2022-06-14 14:57:13.187469
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_1 = Token(None, 0, 0)
    # Same value, same start_index, same end_index
    assert token_1 == Token(token_1.value, token_1.start_index, token_1.end_index)
    # Different value, same start_index, same end_index
    assert not (token_1 == Token(not token_1.value, token_1.start_index, token_1.end_index))
    # Same value, different start_index, same end_index
    assert not (token_1 == Token(token_1.value, token_1.start_index + 1, token_1.end_index))
    # Same value, same start_index, different end_index

# Generated at 2022-06-14 14:57:14.838910
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken()
    assert(type(token)) is DictToken


# Generated at 2022-06-14 14:57:21.627760
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    a = Token(None, 0, 1, content='')
    b = Token(None, 0, 1, content='')
    return [a == a, b == b, a == b]

# Generated at 2022-06-14 14:57:24.152138
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(value={}, start_index=0, end_index=0)
    assert token.value == {}


# Generated at 2022-06-14 14:57:33.063329
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_one = Token(0, 0, 0, "")
    token_two = Token(0, 0, 0, "")
    assert token_one == token_two
    a = Token(0, 0, 0, "")
    b = Token((0.0, 0.0), 0, 0, "")
    c = Token((0.0, 0.0), 1, 1, "")
    d = Token((0.0, 0.0), 1, 0, "")
    e = Token(0, 1, 0, "")
    f = Token((0, 0), 0, 0, "")
    g = Token(0, 0, 1, "")
    assert a == b == c == d == e == f == g
    assert a == b == c == d == e == f == g

# Generated at 2022-06-14 14:57:37.075961
# Unit test for constructor of class DictToken
def test_DictToken():
    k = ScalarToken(1, 0, 0, 'a')
    v = ScalarToken(2, 1, 1, 'b')
    n = DictToken({k: v}, 0, 1, 'a: b')
    return n

# Generated at 2022-06-14 14:57:37.807425
# Unit test for constructor of class DictToken
def test_DictToken():
    pass

# Generated at 2022-06-14 14:57:38.224808
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass

# Generated at 2022-06-14 14:57:45.140275
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import Position
    from typesystem.token import ScalarToken
    t1 = ScalarToken(23, 22, 33, "some string")
    t2 = ScalarToken(23, 22, 33, "some string")
    assert t1 == t2
    t1 = ScalarToken(12, 22, 33, "some string")
    assert t1 != t2
    t1 = ScalarToken(23, 11, 33, "some string")
    assert t1 != t2
    t1 = ScalarToken(23, 22, 44, "some string")
    assert t1 != t2


# Generated at 2022-06-14 14:57:50.905978
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 2
    content = "content"
    keys = {"a", "b"}
    token = DictToken(keys, start_index, end_index, content)
    assert token.value == keys
    assert token.start_index == start_index
    assert token.end_index == end_index
    assert token.content == content



# Generated at 2022-06-14 14:58:01.600609
# Unit test for constructor of class DictToken
def test_DictToken():
    # Test for DictToken with one argument
    print("\n### Test for DictToken with one argument:")
    value = {'name':'Apple', 'type':'fruit'}
    start_index = 0
    end_index = 50
    print("The value is: ")
    print(value)
    print("The start_index is: ")
    print(start_index)
    print("The end_index is: ")
    print(end_index)
    token = DictToken(value,start_index,end_index)
    print("The object of class DictToken is equal to: ")
    print(token)

    # Test for DictToken with one argument
    print("\n### Test for DictToken with zero argument:")
    token = DictToken()

# Generated at 2022-06-14 14:58:09.730351
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 0
    end_index = 0
    content = ""
    obj = Token("", start_index, end_index, content)
    assert obj == obj
    assert obj != "string"
    assert obj != None
    assert obj != 1
    assert obj != 1.1
    assert obj != False
    assert obj != True
    assert obj != (1,)
    assert obj != [1]
    assert obj != {"key": "value"}
    assert obj.string == ""
    assert obj.start_index == 0
    assert obj.end_index == 0
    assert obj.content == ""

# Generated at 2022-06-14 14:58:20.775600
# Unit test for constructor of class DictToken
def test_DictToken():
    assert 'src/typesystem/tokens.py' == __file__
    print('passed: test_DictToken')

# Generated at 2022-06-14 14:58:27.554647
# Unit test for method __eq__ of class Token
def test_Token___eq__():

	#
	# Test 1
	#

	s = ScalarToken('s', 0, 0)
	s1 = ScalarToken('s', 0, 0)

	assert (s == s1)

	#
	# Test 2
	#

	d = DictToken('d', 0, 0)
	d1 = DictToken('d', 0, 0)

	assert (d == d1)

	#
	# Test 3
	#

	l = ListToken('l', 0, 0)
	l1 = ListToken('l1', 0, 0)

	assert (l != l1)

# Generated at 2022-06-14 14:58:28.801136
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(0, 0, 0)
    assert token == token


# Generated at 2022-06-14 14:58:32.276990
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    with pytest.raises(NotImplementedError):
        Token(None, None, None, None).__eq__(None)

# Generated at 2022-06-14 14:58:34.152417
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # The method __eq__ should return False when the two arguments have different types
    assert not Token(None, 0, 0).__eq__(1)


# Generated at 2022-06-14 14:58:38.629718
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(value = 'name', start_index = 1, end_index = 2, content = "hi")
    assert d._value == 'name'
    assert d._start_index == 1
    assert d._end_index == 2
    assert d._content == "hi"



# Generated at 2022-06-14 14:58:44.369379
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test that two tokens compare equal if the represented values compare equal
    value1 = ScalarToken(1, 0, 0)
    value2 = ScalarToken(1, 0, 0)
    assert value1 == value2

    # Test that two tokens compare equal if they have the same start/end indexes
    value1 = ScalarToken(1, 0, 0)
    value2 = ScalarToken(2, 0, 0)
    assert value1 == value2

    # Test that two tokens compare unequal if their start/end indexes differ
    value1 = ScalarToken(1, 0, 0)
    value2 = ScalarToken(1, 1, 1)
    assert value1 != value2

    # Test that two tokens compare unequal if their values differ
    value1 = ScalarToken(1, 0, 0)

# Generated at 2022-06-14 14:58:47.526189
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(1, 0, 0)
    token2 = Token(1, 0, 0)
    token3 = Token(2, 0, 0)
    token4 = Token(1, 1, 0)
    token5 = Token(1, 0, 1)
    assert token1 == token2
    assert token1 != token3
    assert token1 != token4
    assert token1 != token5


# Generated at 2022-06-14 14:58:50.877872
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken(1,2,3,4,5,5)
    assert dt._start_index == 2 and dt._end_index == 5 and dt._content == 5


# Generated at 2022-06-14 14:58:56.730208
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    """
    Test method __eq__ of class Token.
    """
    start_index = 1
    end_index = 2
    value = 1
    content = 'a'
    token = ScalarToken(value, start_index, end_index, content)
    token2 = ScalarToken(value, start_index, end_index, content)
    assert token == token2



# Generated at 2022-06-14 14:59:16.899783
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({1:1, 2:2}, 0, 0)
    assert a._get_value() == {1:1, 2:2}
    assert a._child_keys == {1:1, 2:2}
    assert a._child_tokens == {1:1, 2:2}

# Generated at 2022-06-14 14:59:25.274572
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test: isinstance(other, Token) == False
    assert Token(None, 0, 0, content="").__eq__(None) == False
    assert Token(None, 0, 0, content="").__eq__(5) == False

    # Test: self._get_value() != other._get_value()
    dict_token_1 = DictToken({}, 0, 0, content="")
    dict_token_2 = DictToken({}, 0, 0, content="")
    list_token_1 = ListToken([], 0, 0, content="")
    list_token_2 = ListToken([], 0, 0, content="")
    assert dict_token_1.__eq__(dict_token_2) == False
    assert dict_token_1.__eq__(list_token_1) == False
    assert dict

# Generated at 2022-06-14 14:59:33.901381
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(1, 2, 3, "1234")
    t2 = Token(1, 2, 3, "1234")
    t3 = Token(2, 1, 2, "1234")
    t4 = Token(1, 2, 3, "5678")
    assert t1 == t2, " __eq__ : " + str(t1) + "+ =/= " + str(t2)
    assert t1 != t3, " __eq__ : " + str(t1) + "+ =/= " + str(t3)
    assert t1 != t4, " __eq__ : " + str(t1) + "+ =/= " + str(t4)

# Generated at 2022-06-14 14:59:46.037067
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken("a",0,0,content="abcd") == ScalarToken("a",0,0,content="abcd")
    assert ListToken("abcd",0,0,content="abcd") == ListToken("abcd",0,0,content="abcd")
    assert DictToken("abcd",0,0,content="abcd") == DictToken("abcd",0,0,content="abcd")
    assert ScalarToken("a",0,0,content="abcd") != ListToken("abcd",0,0,content="abcd")
    assert ScalarToken("a",0,0,content="abcd") != DictToken("abcd",0,0,content="abcd")

# Generated at 2022-06-14 14:59:47.480011
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken(value=1, start_index=1, end_index=1)

# Generated at 2022-06-14 14:59:50.102885
# Unit test for method __eq__ of class Token
def test_Token___eq__():
	Token.__eq__(Token(value=0, start_index=0, end_index=0, content=""))

# Generated at 2022-06-14 14:59:57.731357
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 2
    value = {}
    test = DictToken(value, start_index, end_index)
    assert test._value == value
    assert test._start_index == start_index
    assert test._end_index == end_index
    assert test.string == ''
    assert test.value == value
    assert test.start == Position(1, 1, 0)
    assert test.end == Position(1, 1, 2)


# Generated at 2022-06-14 15:00:04.545631
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.schemas import Dict
    from typesystem.base import Token
    from typesystem import fields
    schema = Dict({
        "a": fields.String(),
        "b": fields.String()
    })
    data = {
        "a": "aaa",
        "b": "bbb"
    }

    token = schema.parse(data)
    test_tok = DictToken({
            "a": Token("aaa", 0, 2), 
            "b": Token("bbb", 0, 2)
        }, 
        0,
        2,
        "aaa bbb"
    )
    print(token)
    print(test_tok)
    assert token == test_tok

# Generated at 2022-06-14 15:00:06.651820
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.tokenizers import Tokenizer

    token = Tokenizer.parse('{"a":1}')
    assert token[0].string == '{"a":1}'
    assert token[0].value == {"a": 1}


# Generated at 2022-06-14 15:00:17.029777
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from pytest import raises
    from typesystem.base_support.exceptions import AssertionError as AE

    # case 1
    token1 = Token(value='value1', start_index=1, end_index=1000)
    token2 = Token(value='value1', start_index=1, end_index=1000)
    x = token1 == token2
    assert x == True

    # case 2
    token1 = Token(value=1, start_index=1, end_index=1000)
    token2 = Token(value='a', start_index=1, end_index=1000)
    x = token1 == token2
    assert x == False

    # case 3
    token1 = Token(value='value1', start_index=1, end_index=1000)

# Generated at 2022-06-14 15:00:40.207378
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # str
    a = ScalarToken("a", 0, 0)
    b = ScalarToken("a", 0, 0)
    assert a == b
    
    # int
    c = ScalarToken(1, 0, 0)
    d = ScalarToken(1, 0, 0)
    assert c == d
    
    # float
    e = ScalarToken(1.0, 0, 0)
    f = ScalarToken(1.0, 0, 0)
    assert e == f

    # dict
    g = DictToken({a: b}, 0, 0)
    h = DictToken({a: b}, 0, 0)
    assert g == h
    
    # list
    i = ListToken([a], 0, 0)
    j = ListToken([a], 0, 0)
    assert i

# Generated at 2022-06-14 15:00:50.140446
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken(1, 0, 2, content="123") == ScalarToken(1, 0, 2, content="123")
    assert ScalarToken(1, 0, 2, content="123") != ScalarToken(2, 0, 3, content="123")
    assert ScalarToken(1, 0, 2, content="123") != ScalarToken("1", 0, 2, content="123")
    assert ScalarToken(1, 0, 2, content="123") != ScalarToken(1, 1, 3, content="123")
    assert ScalarToken("1") != ScalarToken(1)
    assert ScalarToken(1, 0, 0) != ScalarToken(1, 0, 1)
    assert ScalarToken(1, 0, 1) == ScalarToken(1, 0, 1)

# Generated at 2022-06-14 15:00:53.187847
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    tk = Token(None, 0, 0)
    tk2 = Token(None, 0, 0)
    assert tk == tk2


# Generated at 2022-06-14 15:01:05.243893
# Unit test for constructor of class DictToken
def test_DictToken():
    import datetime

    dict = {
        "key1": "string",
        "key2": 1,
        "key3": True,
        "key4": [1, 2, 3],
        "key5": {"foo": 1, "bar": 2},
        "key6": datetime.date.today(),
    }
    dict2 = {
        "key1": "string",
        "key2": 1,
        "key3": True,
        "key4": [1, 2, 3],
        "key5": {"foo": 1, "bar": 2},
        "key6": datetime.date.today(),
    }
    dict_token = DictToken(dict, 1, 2, "")
    dict_token2 = DictToken(dict2, 1, 2, "")
    assert dict_token

# Generated at 2022-06-14 15:01:14.713982
# Unit test for constructor of class DictToken
def test_DictToken():
    a = ScalarToken("A", 0, 1)
    b = ScalarToken("B", 2, 3)
    c = ScalarToken("C", 4, 5)
    d = ScalarToken("D", 6, 7)

    obj = DictToken(
            {a:b, c:d}, 
            0, 
            8, 
            "A B\nC D"
            )
    assert len(obj._child_keys) == 2
    assert len(obj._child_tokens) == 2
    assert obj._child_keys[a._value] == a
    assert obj._child_keys[c._value] == c
    assert obj._child_tokens[a._value] == b
    assert obj._child_tokens[c._value] == d
    assert obj._child_tok

# Generated at 2022-06-14 15:01:23.200537
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    '''
    def __eq__(self, other: typing.Any) -> bool:
        return isinstance(other, Token) and (
            self._get_value() == other._get_value()
            and self._start_index == other._start_index
            and self._end_index == other._end_index
        )
    '''
    t1 = Token(1, 2, 3)
    t2 = Token(1, 2, 3)
    t3 = Token(2, 3, 4)
    t4 = Token(1, 3, 4)
    t5 = Token(1, 4, 5)
    t6 = Token(1, 2, 4)
    assert t1 == t1
    assert t1 == t2
    assert t2 == t1
    assert t3 != t1

# Generated at 2022-06-14 15:01:27.497190
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1, 1, 2) == Token(1, 1, 2)
    assert not (Token(1, 1, 2) != Token(1, 1, 2))


# Generated at 2022-06-14 15:01:30.081295
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    tk1 = Token(1,1,1,"a")
    tk2 = Token(1,1,1,"a")
    assert tk1 != tk2


# Generated at 2022-06-14 15:01:33.575748
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    string = "Hello world!'\n"
    obj = Token(string, 0, len(string) - 1, string)
    assert obj == obj
    assert obj != string



# Generated at 2022-06-14 15:01:35.419149
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass # TODO: implement your test here

# Generated at 2022-06-14 15:02:45.214513
# Unit test for constructor of class DictToken
def test_DictToken():
    from ipdb import set_trace
    set_trace()
    d1 = {'a': 1}
    t1 = Token(d1, 0, 0, content="testtt")
    print(t1)
    print(type(t1))
    print(t1.value)
    print(t1.string)
    print(t1.start)
    print(t1.end)
    print(t1.lookup([0]))

# Generated at 2022-06-14 15:02:48.600816
# Unit test for constructor of class DictToken
def test_DictToken():
    d1 = {'a':1}
    d2 = {'b':2}
    d = {**d1, **d2}
    dt = DictToken(d, 0, 0)


# Generated at 2022-06-14 15:02:58.865545
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(
        {"abcd": "1234"}, 0, 5, content="{'abcd': '1234'}"
    )
    assert token.string == "{'abcd': '1234'}"
    assert token.start.index == 0
    assert token.end.index == 5
    assert token.value == {'abcd': '1234'}
    assert token._value == {
        ScalarToken('abcd', 2, 5, content="{'abcd': '1234'}"): ScalarToken('1234', 10, 14, content="{'abcd': '1234'}")
        }
    assert token._child_keys == {'abcd': ScalarToken('abcd', 2, 5, content="{'abcd': '1234'}")}
    assert token._child_tok

# Generated at 2022-06-14 15:03:03.187873
# Unit test for constructor of class DictToken
def test_DictToken():
    parent_token = {
        "token1": "token1", 
        "token2": "token2", 
        "token3": "token3", 
        "token4": "token4"
    }
    token = DictToken(parent_token, 0, 10, "token1token2token3token4")
    assert token._get_value() == {"token1": "token1", "token2": "token2", "token3": "token3", "token4": "token4"}
    assert token._get_child_token("token1") == "token1"
    assert token._get_child_token("token2") == "token2"
    assert token._get_child_token("token3") == "token3"
    assert token._get_child_token("token4") == "token4"


#

# Generated at 2022-06-14 15:03:10.800485
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({'key': 'value'}, 10, 10, '{key: value}')
    b = DictToken({'key1': 'value1', 'key2': 'value2'}, 10, 10, '{key1: value1, \
                   key2: value2}')
    assert isinstance(a, Token)
    assert isinstance(b, Token)
    assert a._value == {'key': 'value'}
    assert b._value == {'key1': 'value1', 'key2': 'value2'}
    assert a._start_index == 10
    assert b._start_index == 10
    assert a._end_index == 10
    assert b._end_index == 10
    assert a._child_keys == {'key': 'key'}

# Generated at 2022-06-14 15:03:16.404695
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 100
    test_args = [0, 0, 100]
    test_kwargs = {"content":"test_contents"}
    case1 = DictToken(test_args, test_kwargs)
    case2 = DictToken(test_args, test_kwargs)
    assert case1 == case2


# Generated at 2022-06-14 15:03:25.939552
# Unit test for constructor of class DictToken
def test_DictToken():
	data = {'a':1, 'b':2}# data to test
	token = DictToken({}, 0, 5)# create a DictToken
	assert token._child_keys == {}# test _child_keys
	assert token._child_tokens == {}# test _child_tokens
	assert token._start_index == 0# test _start_index
	assert token._end_index == 5# test _end_index
	assert token._content == ''# test _content
	assert token.start == Position(1, 1, 0)# test start
	assert token.end == Position(1, 1, 5)# test end
	assert token.string == ''# test string
	

# Generated at 2022-06-14 15:03:36.279127
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import ScalarType
    from typesystem.enums import FieldType

    test_value = ScalarType("string", FieldType.STRING, "b")
    test_start_index = 1
    test_end_index = 1
    test_content = "a"

    result = DictToken(test_value, test_start_index, test_end_index, test_content)
    assert result._value == test_value
    assert result._start_index == test_start_index
    assert result._end_index == test_end_index
    assert result._content == test_content

    test_value = ScalarType("string", FieldType.STRING, "b")
    test_start_index = 1
    test_end_index = 1


# Generated at 2022-06-14 15:03:40.192092
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({'x':Token(100, 100, 200)}, 100, 200)
    assert dt._child_tokens['x'] == Token(100, 100, 200)
    assert dt._child_keys['x'] == Token(100, 100, 200)


# Generated at 2022-06-14 15:03:43.011273
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({"a": "b"}, 0, 1)
    assert repr(token) == '''DictToken({"a": "b"})'''

# Generated at 2022-06-14 15:04:26.303451
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {'a': 1, 'b': 2}
    dt = DictToken(d, 0, 10)
    print(dt._value)
    print(dt._get_value())
    print(dt.start)
    print(dt.end)


# Generated at 2022-06-14 15:04:29.362366
# Unit test for constructor of class DictToken
def test_DictToken():
    from class_token import DictToken
    assert DictToken(
        value = {1 : 2},
        start_index = 0,
        end_index = 2,
        content = "abcd"
    ).string == "abcd"

# Generated at 2022-06-14 15:04:34.011467
# Unit test for constructor of class DictToken
def test_DictToken():
    def test_constructor():
        t = DictToken({}, 0, 10)
        assert t._value == {}
        assert t._start_index == 0
        assert t._end_index == 10
        assert t._content == ""
    test_constructor()


# Generated at 2022-06-14 15:04:40.889807
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken("a", 1, 2, "a=1")
    assert dt.start.line_no == 1
    assert dt.start.column_no == 1
    assert dt.start.byte_no == 0
    assert dt.end.line_no == 1
    assert dt.end.column_no == 3
    assert dt.end.byte_no == 2
    assert dt.string == "a=1"
    assert dt.value == "a"


# Generated at 2022-06-14 15:04:51.609169
# Unit test for constructor of class DictToken
def test_DictToken():
    # Case 1: Value is not a dictionary
    with pytest.raises(AssertionError):
        DictToken(value = "hello", start_index = 0, end_index = 4, content = "Hello World")

    # Value is a dictionary
    value = DictToken(
        value = {"hello": ScalarToken(value = "world", start_index = 6, end_index = 10, content = "Hello World"), "name": ScalarToken(value = "Bob", start_index = 11, end_index = 13, content = "Hello World")},
        start_index = 0,
        end_index = 13,
        content = "Hello World",
    )

    DictToken(value = value._get_value(), start_index = 0, end_index = 13, content = value._content)

    assert value._child_

# Generated at 2022-06-14 15:04:58.235059
# Unit test for constructor of class DictToken
def test_DictToken():
    # test 1
    d = {1:2}
    di = DictToken(d, 1, 2)
    assert di._value == d
    assert di._start_index == 1
    assert di._end_index == 2
    assert di._content == ""

    # test 2
    d2 = {1:2}
    di2 = DictToken(d2, 1, 12, "content")
    assert di2._value == d
    assert di2._start_index == 1
    assert di2._end_index == 2
    assert di2._content == "content"


# Generated at 2022-06-14 15:05:00.145211
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken(
        {"key": 2}, 0, 2, content="{\"key\": 2}"
    )

# Generated at 2022-06-14 15:05:08.880533
# Unit test for constructor of class DictToken
def test_DictToken():
    a = ScalarToken("a", 1, 2)
    b_inner = ScalarToken("b", 3, 4)
    b = DictToken({"a": b_inner}, 1, 4, content="a: b")
    assert isinstance(b, DictToken)
    assert b.value == {"a": "b"}
    assert b.start == Position(1, 1, 1)
    assert b.end == Position(1, 4, 5)
    assert b.string == "a: b"
    assert b.lookup([0]) == b_inner
    assert b.lookup([]) == b
    assert b.lookup_key([0]) == a
    assert b.lookup_key([]) == b
    assert b.lookup_key([1]) == a


# Generated at 2022-06-14 15:05:11.900421
# Unit test for constructor of class DictToken
def test_DictToken():
	_dict = DictToken({1: 2, 3: 4}, 1, 2, "")
	assert _dict._get_value() == {1: 2, 3: 4}, 'AssertionError'


# Generated at 2022-06-14 15:05:23.938525
# Unit test for constructor of class DictToken
def test_DictToken():
    from validator.utils import Position
    # Constructor without arguments
    dic = DictToken(value={}, start_index=0, end_index=1, content='')
    assert isinstance(dic, DictToken)
    assert dic.start == Position(0, 0, 0)
    assert dic.end == Position(0, 0, 1)
    assert dic.string == ''
    assert dic.value == {}
    # Constructor with arguments
    dic = DictToken(value={'a': 1}, start_index=0, end_index=1, content='')
    assert isinstance(dic, DictToken)
    assert dic.start == Position(0, 0, 0)
    assert dic.end == Position(0, 0, 1)
    assert dic.string == ''