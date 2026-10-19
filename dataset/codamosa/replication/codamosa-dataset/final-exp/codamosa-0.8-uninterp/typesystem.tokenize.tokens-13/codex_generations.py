

# Generated at 2022-06-14 14:56:22.428307
# Unit test for constructor of class DictToken
def test_DictToken():
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        super().__init__(*args, **kwargs)
        self._child_keys = {k._value: k for k in self._value.keys()}
        self._child_tokens = {k._value: v for k, v in self._value.items()}


# Generated at 2022-06-14 14:56:28.870423
# Unit test for constructor of class DictToken
def test_DictToken():
    
    t = Token(value = 2, start_index = 0, end_index = 2)
    d = {t : 0}
    D = DictToken(value = d, start_index = 0, end_index = 6)
    
    
    assert D._child_keys[t._value] == t
    assert D._child_tokens[t._value] == 0
    assert D._child_keys[t._value]._value == t._value
    assert D._child_keys[t._value]._get_value() == t._get_value()
    assert D._child_tokens[t._value]._get_value() == 0

# Generated at 2022-06-14 14:56:36.363073
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({'a':1, 'b':2}, 0, 5, 'aaa bbb')
    assert a._value['a']._value == 'a'
    assert  a._value['b']._value == 'b'
    assert a._child_keys['a']._value == 'a'
    assert a._child_tokens['a']._value == 1
    assert a._child_keys['b']._value == 'b'
    assert a._child_tokens['b']._value == 2
    assert a._child_tokens['a'].string == 'a'
    assert a._child_tokens['a']._start_index == 0
    assert a._child_tokens['a']._content == 'aaa bbb'
    assert a.lookup

# Generated at 2022-06-14 14:56:44.521974
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class TokenChild(Token):
        def __init__(self, value: typing.Any, start_index: int, end_index: int, content: str = "") -> None:
            super().__init__(value, start_index, end_index, content)

        def _get_value(self) -> typing.Any:
            return self._value

    token1 = TokenChild("hello", 0, 0, "hello")
    token2 = TokenChild("hello", 0, 10, "hello")
    assert token1 == token2


# Generated at 2022-06-14 14:56:46.018852
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({"a":1}, 1, 2)



# Generated at 2022-06-14 14:56:54.372758
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert (
        ScalarToken(value='scalar', start_index=0, end_index=3)
        == ScalarToken(value='scalar', start_index=0, end_index=3)
    )
    assert (
        DictToken(
            value={'hello': ScalarToken(value='world', start_index=1, end_index=2)},
            start_index=5,
            end_index=5,
            content="",
        )
        == DictToken(
            value={'hello': ScalarToken(value='world', start_index=1, end_index=2)},
            start_index=5,
            end_index=5,
            content="",
        )
    )

# Generated at 2022-06-14 14:57:01.177322
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    c = ScalarToken(1, 2, 3)
    d = ScalarToken(1, 2, 3)
    t_eq = c == d
    assert t_eq == True
    c = ScalarToken(1, 2, 3)
    d = ScalarToken(2, 3, 4)
    t_eq = c == d
    assert t_eq == False


# Generated at 2022-06-14 14:57:08.359944
# Unit test for constructor of class DictToken
def test_DictToken():
    token_1 = ScalarToken("apple", 1, 5, "apple pie")
    token_2 = ScalarToken("pie", 6, 9, "apple pie")
    dic = {token_1: token_2}
    j = DictToken(dic, 0, 9, "apple pie")
    assert j._value == dic
    assert j._child_keys == {token_1._value: token_1}
    assert j._child_tokens == {token_1._value: token_2}
    assert j.start.line_no == 1
    assert j.start.column_no == 1
    assert j.start.index == 0
    assert j.end.line_no == 1
    assert j.end.column_no == 9
    assert j.end.index == 9

# Generated at 2022-06-14 14:57:10.489198
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken(3, 0, 1)
    token2 = ScalarToken(3, 0, 1)
    assert token1 == token2
    token3 = ScalarToken(5, 0, 1)
    assert token1 != token3


# Generated at 2022-06-14 14:57:13.897654
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(0, 0, 0)
    t2 = Token(0, 0, 0)
    t3 = Token(0, 1, 1)
    assert t1 == t1
    assert t1 == t2
    assert t1 != t3


# Generated at 2022-06-14 14:57:24.332648
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({1:2}, 3, 4, content = 'content')
    assert token.start == 1
    assert token.end == 2
    assert token.string == 'content'
    assert token.value == {1:2}
    assert token.lookup([1]) == {2}
    assert token.lookup_key([1, 2]) == {3, 4}
    assert token._get_position(3) == (3, 4)
    assert str(token) == 'DictToken({1:2})'


# Generated at 2022-06-14 14:57:30.230909
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {"a": 5}
    x = DictToken(d, 0, 1, "ab")
    assert x._child_keys["a"].string == "a"
    assert x._child_tokens["a"].string == "b"
    assert x._value == d
    assert x.start == Position(1, 1, 0)
    assert x.end == Position(1, 2, 1)
    assert x.string == "ab"

# Generated at 2022-06-14 14:57:31.289474
# Unit test for constructor of class DictToken
def test_DictToken():
    Token(dict(), 0, 1, "")

# Generated at 2022-06-14 14:57:41.968933
# Unit test for constructor of class DictToken
def test_DictToken():
    t1 = ScalarToken(1, 0, 2, '123')
    t2 = ScalarToken(2, 3, 5, '123')
    test1 = {t1: t2}
    test1 = DictToken(test1, 0, 5)
    assert test1.string == '123'
    assert test1.value == {1: 2}
    assert test1.start == Position(line_no = 1, column_no = 1, index = 0)
    assert test1.end == Position(line_no = 1, column_no = 3, index = 5)

    t3 = ScalarToken(3, 7, 9, '123\n456\n789')
    t4 = ScalarToken(4, 10, 12, '123\n456\n789')
    test2 = {t3: t4}

# Generated at 2022-06-14 14:57:46.164765
# Unit test for constructor of class DictToken
def test_DictToken():
    
    dict_token = DictToken({"aa":1},0,0)
    assert type(dict_token) is DictToken
    assert dict_token._value == {"aa":1}
    assert dict_token._start_index == 0
    assert dict_token._end_index == 0
    

# Generated at 2022-06-14 14:57:47.590691
# Unit test for constructor of class DictToken
def test_DictToken():
    tok = DictToken()
    assert tok is not None

# Generated at 2022-06-14 14:57:52.065920
# Unit test for constructor of class DictToken
def test_DictToken():
    print('DictToken constructor')
    _value = {}
    _start_index = 0
    _end_index = 0
    _content = ""
    dict_token = DictToken(_value, _start_index, _end_index, _content)
    assert dict_token is not None



# Generated at 2022-06-14 14:57:56.280495
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {"a": 10}
    dt = DictToken(d, 0, 1, "test")
    assert dt.value == d
    assert dt._child_keys == {'a': dt._child_keys['a']}
    assert dt._child_tokens == {'a': dt._child_tokens['a']}


# Generated at 2022-06-14 14:58:03.142346
# Unit test for constructor of class DictToken
def test_DictToken():
    import sys
    import io
    import traceback
    import unittest

    DictToken.__init__("*args", "**kwargs")
    ##print("  File \"", __file__, "\", line ", sys._getframe().f_lineno - 1, sep='', end='', flush=True)
    ##print("", sep='', end='', flush=True)

    ##print("")




# Generated at 2022-06-14 14:58:11.342652
# Unit test for constructor of class DictToken
def test_DictToken():
    # Type: DictToken
    k1 = ScalarToken(1, 0, 2)
    v1 = ScalarToken(2, 0, 2)
    # Type: Dict[ScalarToken, ScalarToken]
    d = {k1: v1}
    # Type: DictToken
    dt = DictToken(d, 0, 3)
    # Type: DictToken
    dt2 = DictToken(d, 0, 3)
    assert dt == dt2
    assert dt != 1
    # Type: DictToken
    dt3 = DictToken({k1: v1}, 0, 3)
    assert dt3 == dt2


# Generated at 2022-06-14 14:58:18.316200
# Unit test for constructor of class DictToken
def test_DictToken():
    assert 1==1
    

# Generated at 2022-06-14 14:58:27.585194
# Unit test for constructor of class DictToken
def test_DictToken():
    # Test 1:
    var1 = '{"a": -1}'
    var2 = Token(start_index=0, end_index=4)
    var3 = '{"a": -1}'
    var4 = {"a": -1}
    var5 = {'a': -1}
    var6 = DictToken(var4, var1, var2, content=var3)
    assert var6._value == var4
    assert var6._get_value() == var5
    # Test 2:
    var7 = '[{"a": -1, "b": 2}]'
    var8 = Token(start_index=0, end_index=3)
    var9 = [Token(start_index=1, end_index=2)]
    var10 = {'a': -1, 'b': 2}

# Generated at 2022-06-14 14:58:38.460183
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {
        'key1': 1,
        'key2': 2,
        'key3': 3,
        'key4': 4,
    }
    token = DictToken(d, 0, 4, "key1:1,key2:2,key3:3,key4:4")
    assert token._child_keys == {
        'key1': 1,
        'key2': 2,
        'key3': 3,
        'key4': 4,
    }
    assert token._child_tokens == {
        'key1': 1,
        'key2': 2,
        'key3': 3,
        'key4': 4,
    }


# Generated at 2022-06-14 14:58:39.407398
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken()
    assert dt

# Generated at 2022-06-14 14:58:49.871250
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken(value = {1 : Token(1, 1, 2, "a")}, start_index = 1, end_index = 2)
    assert(a.string == "a")
    assert(a.value == {1: 1})
    assert(a.start.index == 1)
    assert(a.end.index == 2)
    assert(a.lookup([1]).string == "a")
    b = a.lookup_key([1])
    assert(b.start.index == 1)
    assert(b.end.index == 2)


# Generated at 2022-06-14 14:58:58.366769
# Unit test for constructor of class DictToken
def test_DictToken():
    my_token = DictToken("test_value", 0,1)
    assert my_token.string == "test_value"
    assert my_token.value == "test_value"
    assert my_token.start.line == 0
    assert my_token.start.column == 0
    assert my_token.end.line == 1
    assert my_token.end.column == 1
    assert repr(my_token) == "DictToken('test_value')"
    assert my_token == DictToken("test_value", 0,1)


# Generated at 2022-06-14 14:58:59.769220
# Unit test for constructor of class DictToken
def test_DictToken():
    a=DictToken({})
    print(a)


# Generated at 2022-06-14 14:59:05.783288
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.parser import tokenize, decode_string
    content = '{"a": 1}'
    tokens = tokenize(content)
    assert isinstance(tokens, dict)
    dict_token = DictToken(tokens, 0, len(tokens), content)
    assert isinstance(dict_token, DictToken)

# Generated at 2022-06-14 14:59:11.548494
# Unit test for constructor of class DictToken
def test_DictToken():
    print("Testing Constructor of DictToken")
    test = DictToken({"test": 2}, 0, 2, content="test")
    assert test._value == {"test": 2}
    assert test._start_index == 0
    assert test._end_index == 2
    assert test._content == "test"
    print("DictToken Passed Tests")


# Generated at 2022-06-14 14:59:18.022738
# Unit test for constructor of class DictToken
def test_DictToken():
    T = DictToken(
        {
            ScalarToken("A", 1, 3): ScalarToken("E", 2, 4),
            ScalarToken("B", 2, 4): ScalarToken("F", 3, 5)
        },
        1,
        5)
    print(T.start)
    print(T.end)
    print(T.lookup_key([0]))
    print(T.lookup([0]))


# Generated at 2022-06-14 14:59:46.634711
# Unit test for constructor of class DictToken
def test_DictToken():
    line1 = "a"
    line2 = "b"
    line3 = "c"
    token_value = {
        ScalarToken(line1,0,0,"abc"): ScalarToken(line1,0,0,"abc"),
        ScalarToken(line2,0,0,"abc"): ScalarToken(line2,0,0,"abc"),
        ScalarToken(line3,0,0,"abc"): ScalarToken(line3,0,0,"abc"),
    }
    token = DictToken(token_value,0,0,"abc")

    assert token._child_keys == {line1: ScalarToken(line1,0,0,"abc"),line2: ScalarToken(line2,0,0,"abc"), line3: ScalarToken(line3,0,0,"abc")}
   

# Generated at 2022-06-14 14:59:50.269662
# Unit test for constructor of class DictToken
def test_DictToken():
    test = DictToken({'a': 1, 'b': 2})
    assert(test._start_index == 0 and test._end_index == 0 and test._content == '')


# Generated at 2022-06-14 14:59:51.840162
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken()

# Generated at 2022-06-14 14:59:55.510392
# Unit test for constructor of class DictToken
def test_DictToken():
    x = DictToken({}, 0, 0, "aaa")
    print(x._value)
    print(x._start_index)
    print(x._end_index)
    print(x._content)


# Generated at 2022-06-14 15:00:01.080314
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken(value={}, start_index=0, end_index=10, content="")
    assert dict_token._child_keys == {}
    assert dict_token._child_tokens == {}
    assert dict_token._value == {}
    assert dict_token._start_index == 0
    assert dict_token._end_index == 10
    assert dict_token._content == ""


# Generated at 2022-06-14 15:00:07.668797
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({"a": "b"}, 0, 2, "abc")
    assert dict_token.start.line == 1
    assert dict_token.start.column == 1
    assert dict_token.end.line == 1
    assert dict_token.end.column == 2
    assert dict_token.string == "{"
    assert dict_token.value == {"a": "b"}



# Generated at 2022-06-14 15:00:11.222416
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {1: "abc", 2: "def"}
    a = DictToken(d, 0, 10, "abcdef")
    assert isinstance(a, DictToken)

# Generated at 2022-06-14 15:00:16.725981
# Unit test for constructor of class DictToken
def test_DictToken():
    t_dict = DictToken(
        {"name": "asdf"}, 0, 4, content="{'name': 'asdf'}"
    )
    assert t_dict.string == "{'name': 'asdf'}"

# Generated at 2022-06-14 15:00:22.315447
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({"a":2, "b":"b"}, 0, 1, "ab")
    assert token._start_index == 0
    assert token._end_index == 1
    assert token._content == "ab"
    assert token._child_keys == {"a":2,"b":"b"}
    assert token._child_tokens == {"a":2,"b":"b"}


# Generated at 2022-06-14 15:00:26.104825
# Unit test for constructor of class DictToken
def test_DictToken():
    dictToken = DictToken({'a': 1}, 0, 3)
    assert dictToken.value == {'a': 1}
    assert dictToken.string == '{a}'
    assert dictToken.start == Position(1, 1, 0)
    assert dictToken.end == Position(1, 5, 3)

# Generated at 2022-06-14 15:01:14.128086
# Unit test for constructor of class DictToken
def test_DictToken():
    # Set up
    token = DictToken({}, 0, 0, content='hi')

    # Check
    assert token._content == 'hi'

# Generated at 2022-06-14 15:01:22.790787
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Token
    from typesystem.base import DictToken
    from typesystem.base import Position
    from typesystem.base import ScalarToken
    
    dictionaryToken = TestDictToken()
    assert dictionaryToken._value == TestDictToken._value
    assert dictionaryToken._value == {
        TestScalarToken._value: TestScalarToken._value
    }
    assert dictionaryToken._child_keys == {
        TestScalarToken._value: TestScalarToken
    }
    assert dictionaryToken._start_index == TestDictToken._start_index
    assert dictionaryToken._end_index == TestDictToken._end_index
    assert dictionaryToken.lookup([0]) == TestScalarToken
    assert dictionaryToken.lookup([0])._value == TestScalarToken._value
   

# Generated at 2022-06-14 15:01:29.591801
# Unit test for constructor of class DictToken
def test_DictToken():
    keys = [ScalarToken(1, 1, 4), ScalarToken(2, 1, 4)]
    values = [ScalarToken(3, 1, 4), ScalarToken(4, 1, 4)]
    d = {keys[0]: values[0], keys[1]: values[1]}
    DictToken(d, 1, 4)


# Generated at 2022-06-14 15:01:32.784724
# Unit test for constructor of class DictToken
def test_DictToken():
    t1 = {1: 1}
    t2 = DictToken(t1, 1, 1)
    assert t2._value == t1
    assert t2._start_index == 1
    assert t2._end_index == 1

# Generated at 2022-06-14 15:01:43.887143
# Unit test for constructor of class DictToken
def test_DictToken():
    a = Token(1, 2, 3)
    d = DictToken({a: "test"}, 4, 5)
    assert d.value == {1: "test"}
    assert d.start.index == 4
    assert d.end.index == 5
    assert d.start.line == 1
    assert d.start.column == 1
    assert d.end.line == 1
    assert d.end.column == 1
    d2 = d.lookup([])
    assert d2._get_value() == {1: "test"}
    d3 = d2._get_key_token(1)
    assert d3 == a
    assert d2._get_child_token(1) == a
    assert d == d2
    assert hash(d) == hash(d2)

# Generated at 2022-06-14 15:01:48.292744
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(1, 2, 3, 4, 5)
    assert token._value == 1
    assert token._start_index == 2
    assert token._end_index == 3
    assert token._content == 4


# Generated at 2022-06-14 15:01:54.436543
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = {'a': 1, 'b': 2, 'c': 3}
    dt_tok = DictToken(dt, 0, 2, "abc")
    assert dt_tok._value == dt
    assert dt_tok._start_index == 0
    assert dt_tok._end_index == 2
    assert dt_tok._content == "abc"
    

# Generated at 2022-06-14 15:01:58.796296
# Unit test for constructor of class DictToken
def test_DictToken():
    # This test might fail if the constructor of Token is ever changed.
    _ = DictToken( {'a': ScalarToken(1, 0, 1)}, 0, 3, content="{'a': 1}")

# Generated at 2022-06-14 15:02:09.828434
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({"key": "value"}, 0, 1, "content")
    assert token.value == {"key": "value"}
    assert token.start == Position(1, 0, 0)
    assert token.end == Position(1, 0, 1)
    assert token.string == "content"
    assert token == DictToken({"key": "value"}, 0, 1)
    assert token != DictToken({"key": "value"}, 0, 0)
    assert token != DictToken({"key": "value1"}, 0, 1)
    assert token != DictToken({"key1": "value"}, 0, 1)
    assert token.lookup([]) == DictToken({"key": "value"}, 0, 1)

# Generated at 2022-06-14 15:02:14.128319
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken(dict, 2, 4, dict())
    assert dt._value == dict()
    assert dt._start_index == 2
    assert dt._end_index == 4


# Generated at 2022-06-14 15:03:12.069143
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_a = dict()

    dict_a["a"] = 1
    dict_a["b"] = 2
    dict_a["c"] = 3

    dict_token = DictToken(dict_a, 0, len(str(dict_a)), str(dict_a))
    # test if dict_token's value is correct.
    dict_token_value = dict_token._get_value()
    assert dict_token_value == dict_a
    # test if dict_token's start is correct.
    assert dict_token.start.line_no == 1
    assert dict_token.start.column_no == 1
    assert dict_token.start.index == 0
    # test if dict_token's end is correct.
    assert dict_token.end.line_no == 1
    assert dict_token.end.column_

# Generated at 2022-06-14 15:03:14.142589
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({},0,0)
    assert token != None



# Generated at 2022-06-14 15:03:23.238561
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Token

    dict_token = DictToken({1:2, 3:4}, 0, 4, '{"1":2,"3":4}')
    assert dict_token._get_value() == {1: 2, 3: 4}
    assert dict_token._start_index == 0
    assert dict_token._end_index == 4
    assert dict_token._content == '{"1":2,"3":4}'
    assert dict_token._child_keys == {1: 1, 3: 3}
    assert dict_token._child_tokens == {1: 2, 3: 4}


# Generated at 2022-06-14 15:03:26.875930
# Unit test for constructor of class DictToken
def test_DictToken():
    content = "Smith, John (1980): Programming in Python 3. O\u2019Reilly."
    token = DictToken({
        ScalarToken("Smith, John (1980)", 2, 18, content) : ScalarToken("Programming in Python 3.", 19, 41, content),
        ScalarToken("O\u2019Reilly", 42, 49, content): ScalarToken(".", 50, 50, content),
    }, 2, 50, content)
    print(token)

# Generated at 2022-06-14 15:03:30.240533
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({'a':1}, 0, 10)
    assert t._get_value() == {'a': 1}
    assert t._get_child_token('a') == 1


# Generated at 2022-06-14 15:03:32.850932
# Unit test for constructor of class DictToken
def test_DictToken():
    a = dict(a = 1)
    b = dict(b = 2)
    c = {**a, **b}
    print(c)


# Generated at 2022-06-14 15:03:34.732553
# Unit test for constructor of class DictToken
def test_DictToken():
    assert repr(DictToken) == "<class 'typesystem.tokens.DictToken'>"
    assert issubclass(DictToken, Token)


# Generated at 2022-06-14 15:03:40.681940
# Unit test for constructor of class DictToken
def test_DictToken():
    a = Token(1,1,2)
    b = Token(2,2,5)
    c = Token(3,5,7)
    d = Token(4,7,8)
    dict1 = {a:b,c:d}
    dict_token = DictToken(dict1,0,8)
    assert dict_token._child_keys[1] == a
    assert dict_token._child_keys[3] == c
    assert dict_token._child_tokens[1] == b
    assert dict_token._child_tokens[3] == d


# Generated at 2022-06-14 15:03:44.284553
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken()
    assert t.__repr__() == 'DictToken({})'
    assert t.__hash__() == id(t)
    assert t.__eq__(t) == True


# Generated at 2022-06-14 15:03:52.004642
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {'a': 1, 'c': 2}
    d_token = DictToken(d, 0,0)
    assert d_token._value == d
    assert d_token._start_index == 0
    assert d_token._end_index == 0
    assert d_token._content == ''
    assert d_token.string == ''
    assert d_token.value == {'a': 1, 'c': 2}
    assert d_token.start == Position(1, 1, 0)
    assert d_token.end == Position(1, 1, 0)
