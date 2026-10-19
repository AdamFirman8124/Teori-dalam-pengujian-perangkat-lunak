

# Generated at 2022-06-14 14:56:20.281658
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1, 2, 3, 4) != Token(1, 2, 3, 5)
    assert Token(1, 2, 3, 4) != Object(6, 7, 8, 9)
    assert Token(1, 2, 3, 4) != str


# Generated at 2022-06-14 14:56:28.637045
# Unit test for constructor of class DictToken
def test_DictToken():
    key1 = "key1"
    key2 = "key2"
    value1 = "value1"
    value2 = "value2"
    list_value = [value1, value2]
    kwargs = {'_value': {key1: value1, key2: value2}, '_start_index': 0,
              '_end_index': 6, '_content': "content"}
    result = DictToken(**kwargs)
    expected = {key1: value1, key2: value2}
    assert result.value == expected
    assert result._get_child_token(key1).value == value1
    assert result._get_child_token(key2).value == value2
    assert result.lookup([key1]).value == value1
    assert result.lookup([key2]).value == value

# Generated at 2022-06-14 14:56:36.141623
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"hello": 123}'
    keys_start = 1
    values_start = 8
    start = Position(1, 1, 0)
    end = Position(1, 16, 15)
    hello = ScalarToken("hello", keys_start, keys_start + 4)
    end_index = values_start + 2
    value_token = ScalarToken(123, values_start, end_index)
    val1 = DictToken({hello: value_token}, 0, end_index, content)
    assert val1.value == {"hello": 123}
    assert val1.start == start
    assert val1.end == end
    assert val1.string == content
    assert str(val1) == "DictToken('{\"hello\": 123}')"

# Generated at 2022-06-14 14:56:39.607193
# Unit test for constructor of class DictToken
def test_DictToken():
    value = {"a":{"b":"c"}}
    start_index = 0
    end_index = 5
    content = ""
    D = DictToken(value, start_index, end_index, content)
    assert D._get_value() == {"a":{"b":"c"}}


# Generated at 2022-06-14 14:56:47.708171
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({ScalarToken(1, 0, 0): ScalarToken(2, 0, 0)}, 1, 2)
    assert t._child_keys == {1: ScalarToken(1, 0, 0)}
    assert t._child_tokens == {1: ScalarToken(2, 0, 0)}
    assert t._get_child_token(1) == ScalarToken(2, 0, 0)
    assert t._get_key_token(1) == ScalarToken(1, 0, 0)


# Generated at 2022-06-14 14:56:53.172046
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {"1": 1, "2": 2, "3": 3}
    d_token = DictToken(d, 0, 10)
    #print(d_token._value)
    #print(d_token._start_index)
    #print(d_token._end_index)

    #print(d_token._child_keys)
    #print(d_token._child_tokens)



# Generated at 2022-06-14 14:57:01.806302
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({"a": "b", "c": "d"}, start_index=1, end_index=3, content="abcd")
    assert DictToken({ScalarToken("a", 1, 2): ScalarToken("b", 2, 3)}, start_index=1, end_index=3, content="abcd")
    assert DictToken({ScalarToken("a", 1, 2): ScalarToken("b", 2, 3)}, start_index=1, end_index=3, content="abcd")
    assert DictToken({ScalarToken("a", 1, 2): ScalarToken("b", 2, 3)}, start_index=1, end_index=3, content="abcd")

# Generated at 2022-06-14 14:57:12.249426
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({"a" : 1, "b" : 2}, 0, 10, "abcdefghijk")
    assert isinstance(t, DictToken)
    assert t._get_value() == t.value == {"a" : 1, "b" : 2}
    assert t._value == {"a" : 1, "b" : 2}
    assert t._child_keys == {"a": "a", "b": "b"}
    assert t._child_tokens == {"a": 1, "b": 2}
    assert t._start_index == 0
    assert t._end_index == 10
    assert t._content == "abcdefghijk"
    assert t.string == "abcdefghijk"
    assert t.lookup_key(["a"]).string == "a"
    assert t.look

# Generated at 2022-06-14 14:57:23.697080
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test Token class
    import typesystem


# Generated at 2022-06-14 14:57:28.433278
# Unit test for method __eq__ of class Token
def test_Token___eq__():

    # Call __eq__ of class Token, return the result
    token_01 = Token('01', 1, 2)
    token_02 = Token('01', 1, 2)

    result = token_01.__eq__(token_02)

    # Assert the result
    assert result is True


# Generated at 2022-06-14 14:57:36.968298
# Unit test for constructor of class DictToken
def test_DictToken():
    test = DictToken("hello",0,3,"hello")
    assert test.start == Position(1,1,0)
    test = DictToken("hello",0,4,"hello,")
    assert test.end == Position(1,2,4)


# Generated at 2022-06-14 14:57:45.658662
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from c2cwsgiutils import json_token

    # Without argument
    t1 = json_token.Token(None, None, None)
    assert not t1.__eq__(None)
    assert not t1 == ''

    # With value of None
    t1 = json_token.Token(None, 0, 0)
    t2 = json_token.Token(None, 0, 0)
    assert t1.__eq__(t2) and t2.__eq__(t1)

    t1 = json_token.Token(None, 0, 1)
    t2 = json_token.Token(None, 1, 0)
    assert t1.__eq__(t2) and t2.__eq__(t1)

    t1 = json_token.Token(None, 0, 1)
    t2

# Generated at 2022-06-14 14:57:55.674253
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.types import String, Number, Dict

    x = Dict(properties={
        "foo": Number(name="foo"),
        "bar": String(name="bar"),
        "baz": Number(name="baz")
    })
    #print(x.errors({"foo": 1, "bar": "hello", "baz": 3.1415926}))

    #print(x.validate({"foo": 1, "bar": "hello", "baz": 3.1415926}).errors)

    #print(x.validate({"foo": "1", "bar": "hello", "baz": 3.1415926}).errors)

    #print(x.validate({"foo": "1", "bar": "hello", "baz": "3.1415926"}).errors)

    #

# Generated at 2022-06-14 14:57:56.659228
# Unit test for constructor of class DictToken
def test_DictToken():
    Token("", "", "")
    assert True

# Generated at 2022-06-14 14:57:57.314692
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass

# Generated at 2022-06-14 14:58:03.736090
# Unit test for constructor of class DictToken
def test_DictToken():
    print('TESTING DictToken')
    token = DictToken('some value', 0, 15, content='{"key": "value"}')
    assert token is not None
    assert token._value == '{"key": "value"}'
    assert token._start_index == 0
    assert token._end_index == 15
    assert token._content == '{"key": "value"}'


# Generated at 2022-06-14 14:58:12.346511
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(
        {"a": 1}, 0, 3, '{"a": 1}'
    )
    assert repr(token) == "DictToken('{\"a\": 1}')"
    assert token.value == {"a": 1}
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 8, 7)
    assert token.string == '{"a": 1}'
    assert token.lookup([0]) == token._child_tokens['a']
    assert token.lookup_key([0]) == token._child_keys['a']
    assert token == DictToken(
        {"a": 1}, 0, 3, '{"a": 1}'
    )

# Generated at 2022-06-14 14:58:15.847816
# Unit test for constructor of class DictToken
def test_DictToken():
    input = """{
    "name": "red",
    "quantity": 10
}
"""
    output = DictToken(1,2,3)
    assert input == output

# Generated at 2022-06-14 14:58:24.275980
# Unit test for constructor of class DictToken
def test_DictToken():
    # test empty dict
    t = DictToken(None, 0, 1, None)
    assert t._get_value() == {}
    # test normal dict
    test_dict = {'a': 'b'}
    t = DictToken(test_dict, 0, 1, None)
    assert t._get_value() == test_dict
    # test key not in dict
    t = DictToken(None, 0, 1, None)
    assert t._get_child_token("error_key") == None
    # test normal return of key
    assert t._get_key_token("error_key") == None


# Generated at 2022-06-14 14:58:26.254046
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({"x": "y"}, 1, 2, "abc")


# Generated at 2022-06-14 14:58:53.108020
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1_1 = ScalarToken(value="hi", start_index=0, end_index=1)
    token1_2 = ScalarToken(value="hi", start_index=0, end_index=1)
    token1_3 = ScalarToken(value="hI", start_index=0, end_index=1)
    token1_4 = ScalarToken(value="hi", start_index=0, end_index=2)
    token1_5 = ScalarToken(value="hi", start_index=0, end_index=2)

    token2_1 = DictToken(value={"a": ScalarToken(value="", start_index=0, end_index=0)}, start_index=0, end_index=1)

# Generated at 2022-06-14 14:58:54.083097
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({})
    assert dt._value == {}


# Generated at 2022-06-14 14:59:00.395396
# Unit test for constructor of class DictToken
def test_DictToken():
    dt=DictToken({'1':1, '2':2}, 3, 5, '{12}')
    dt_dict_token=dt._child_keys
    dt_dict_value=dt._child_tokens
    assert dt_dict_token == {1: '1', 2: '2'}
    assert dt_dict_value == {'1': 1, '2': 2}


# Generated at 2022-06-14 14:59:12.571377
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken( {'a': 1}, 0, 0, content="")
    assert DictToken( {'a': 1}, 0, 0, content="a")
    assert DictToken( {'a': 1}, 0, 0, content="aa")
    assert DictToken( {'a': 1}, 0, 0, content="aaa")
    assert DictToken( {'a': 1}, 0, 0, content="aaaa")
    assert DictToken( {'a': 1}, 0, 0, content="aaaaa")
    assert DictToken( {'a': 1}, 0, 0, content="aaaaaa")
    assert DictToken( {'a': 1}, 0, 0, content="aaaaaaa")
    assert DictToken( {'a': 1}, 0, 0, content="aaaaaaaa")

# Generated at 2022-06-14 14:59:22.258882
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    Token(1,1,3, content='123').__eq__(Token(1,1,3, content='123'))
    Token(1,2,3, content='123').__eq__(Token(1,1,3, content='123'))
    Token(1,1,4, content='123').__eq__(Token(1,1,3, content='123'))
    Token(1,1,3, content='123').__eq__(Token(1,1,3, content='12'))
    Token(1,1,3, content='123').__eq__(Token(1,1,3, content='124'))
    Token(1,1,3, content='123').__eq__(Token(2,1,3, content='123'))

# Generated at 2022-06-14 14:59:31.294584
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    source = b"abc" * 1000
    token_1 = Token(
        b"abc", start_index=0, end_index=2, content=source.decode("utf-8")
    )
    token_2 = Token(
        b"abc", start_index=0, end_index=2, content=source.decode("utf-8")
    )
    token_3 = Token(
        b"def", start_index=0, end_index=2, content=source.decode("utf-8")
    )
    assert token_1 == token_2
    assert not (token_1 == token_3)



# Generated at 2022-06-14 14:59:43.008097
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken(10, 0, 1) == ScalarToken(10, 0, 1)
    assert ScalarToken(10, 0, 1) != ScalarToken(9, 0, 1)
    assert ScalarToken(10, 0, 1) != ScalarToken(10, 1, 1)
    assert ScalarToken(10, 0, 1) != ScalarToken(10, 0, 2)
    assert ScalarToken(10, 0, 1) != DictToken("",0,0)
    assert DictToken("",0,0) != DictToken("",0,0)
    assert DictToken("",0,0) != ListToken("",0,0)
    assert ListToken("",0,0) == ListToken("",0,0)

# Generated at 2022-06-14 14:59:47.348691
# Unit test for constructor of class DictToken
def test_DictToken():
    x = DictToken({1:2}, 0, 1, "123")
    assert x._get_value() == {1:2}
    assert x._start_index == 0
    assert x._end_index == 1
    assert x._content == "123"


# Generated at 2022-06-14 14:59:52.670657
# Unit test for constructor of class DictToken
def test_DictToken():
    # A simple test to see if the constructor works
    value = {'a': 1, 'b': 2, 'c': 3}
    start_index = 0
    end_index = 20
    token = DictToken(value, start_index, end_index)


# Generated at 2022-06-14 14:59:59.482624
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({"1": "2"}, 0, 3)
    assert dict_token.string == ""
    assert dict_token.value == {"1": "2"}
    assert dict_token.start == Position(1, 1, 0)
    assert dict_token.end == Position(1, 1, 0)
    assert dict_token.lookup([]) == dict_token
    assert dict_token.lookup_key([]) == dict_token


# Generated at 2022-06-14 15:00:46.568437
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import Position
    from typesystem.types import String
    token = Token(String(), 0, 2, content='3')
    other = Token(String(), 0, 2, content='3')
    assert(token == other)

# Generated at 2022-06-14 15:00:53.760498
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    values = [1,2,3,4]
    length = len(values)
    for i in range(length):
        for j in range(length):
            list_token = ListToken(values, i, j)
            for k in range(length):
                for m in range(length):
                    list_token_ = ListToken(values, k, m)
                    if [i,j] == [k,m]:
                        assert list_token.lookup_key([i,j]) == list_token_
                    else:
                        assert list_token.lookup_key([i,j]) != list_token_

    keys = list(range(length))

# Generated at 2022-06-14 15:00:55.760141
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({})
    assert dict(dict_token._value) == {}



# Generated at 2022-06-14 15:00:57.603517
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    token = ScalarToken(value = "foo", start_index = 0, end_index = 2, content = "foo")
    assert hash(token) == hash("foo")


# Generated at 2022-06-14 15:01:01.902932
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import parse
    from typesystem.base import validate
    assert str(validate(parse("foo"), "int")) == "1:1 (line 1, column 1) expected an int"

# Generated at 2022-06-14 15:01:08.763573
# Unit test for constructor of class Token
def test_Token():
    token = Token(1, 0, 2, "123")
    assert token.string == "123"
    assert token.value == 1
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 3, 2)
    assert repr(token) == "Token(1)"
    assert token == Token(1, 0, 2, "123")
    token2 = Token(2, 0, 2, "123")
    assert not (token2 == token)


# Generated at 2022-06-14 15:01:20.084147
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():

    s = "abc,def"
    #create list tokens
    listToken = ListToken(value=(ScalarToken(value="abc", start_index=0, end_index=2, content=s), ScalarToken(value="def", start_index=4, end_index=6, content=s)), start_index=0, end_index=6, content=s)

    #create and test lookup_key
    assert listToken.lookup_key([0]) == ScalarToken(value="abc", start_index=0, end_index=2, content=s)
    assert listToken.lookup_key([1]) == ScalarToken(value="def", start_index=4, end_index=6, content=s)
    assert listToken.lookup_key([2]) == None



# Generated at 2022-06-14 15:01:22.196459
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    token = ScalarToken(123, 0, 3, "123")
    hash(token) == hash(123)


# Generated at 2022-06-14 15:01:24.032294
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    assert True # TODO: implement your test here


# Generated at 2022-06-14 15:01:27.219995
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    t = ScalarToken(1,0,0)
    assert hash(t) == hash(1)


# Generated at 2022-06-14 15:02:05.452695
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
	assert ScalarToken('c', 0, 1, content="c").start.line == 1
	assert ScalarToken('c', 0, 1, content="c").start.column == 1
	assert ScalarToken('c', 0, 1, content="c").start.index == 0
	assert ScalarToken('c', 0, 1, content="c").end.line == 1
	assert ScalarToken('c', 0, 1, content="c").end.column == 2
	assert ScalarToken('c', 0, 1, content="c").end.index == 1
	assert ScalarToken('c', 0, 1, content="c").value == 'c'
	assert ScalarToken('c', 0, 1, content="c").string == 'c'
	assert ScalarToken('c', 0, 1, content="c").lookup([]) == Scalar

# Generated at 2022-06-14 15:02:09.573177
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    testObj = ScalarToken("hello", 1, 2)
    assert testObj._value == "hello"
    assert testObj._start_index == 1
    assert testObj._end_index == 2
    assert testObj._content == ""
    assert testObj.string == "h"


# Generated at 2022-06-14 15:02:12.915236
# Unit test for method lookup of class Token
def test_Token_lookup():
    dict_token = DictToken({"value": "v"}, 0, 10, "test value")
    assert dict_token.lookup([0]).string == 'value'

# Generated at 2022-06-14 15:02:17.121728
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    x = ScalarToken(10, 0, 0, "10")
    assert x.string == "10"
    assert x.value == 10
    assert x.start == Position(1, 1, 0)
    assert x.end == Position(1, 1, 0)


# Generated at 2022-06-14 15:02:19.319796
# Unit test for constructor of class ListToken
def test_ListToken():
    token = ListToken([1,2,3], 1, 2, "123")
    assert token.value == [1, 2, 3]

# Generated at 2022-06-14 15:02:22.181463
# Unit test for constructor of class Token
def test_Token():
    token = Token('value', 1, 3, "content")
    assert token._value == 'value' and token._start_index == 1 \
        and token._end_index == 3 and token._content == 'content'


# Generated at 2022-06-14 15:02:24.756236
# Unit test for constructor of class Token
def test_Token():
    with pytest.raises(NotImplementedError):
        Token("value", 0, 1)


# Generated at 2022-06-14 15:02:27.028247
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    assert Token(None, '', '', '').__repr__() == "Token(None)"

# Generated at 2022-06-14 15:02:34.277971
# Unit test for constructor of class ListToken
def test_ListToken():
    from typesystem.compiler import Lexer
    from typesystem.compiler import Parser

    code = "[1, 2]"
    lexer = Lexer(code)
    parser = Parser(lexer)
    token = parser.parse()
    print(token)
    assert str(token) == "[1, 2]"
    assert token.value == [1, 2]
    assert token.string == "[1, 2]"
    assert token.start.line_no == 1
    assert token.start.column_no == 1
    assert token.start.index == 0
    assert token.end.line_no == 1
    assert token.end.column_no == 5
    assert token.end.index == 4

# Generated at 2022-06-14 15:02:39.991561
# Unit test for constructor of class ListToken
def test_ListToken():
    l = [1,2,3,4,5]
    tokenList = ListToken(l,0,5)
    assert tokenList._value == [1,2,3,4,5]
    assert tokenList._start_index == 0
    assert tokenList._end_index == 5
    assert tokenList._content == ""


# Generated at 2022-06-14 15:03:07.791840
# Unit test for constructor of class ListToken
def test_ListToken():
    t1 = ListToken([1, 2, 3], 0, 0, "123")
    assert t1._value == [1, 2, 3], "Error in ListToken"
    assert t1._start_index == 0, "Error in ListToken"
    assert t1._end_index == 0, "Error in ListToken"
    assert t1._content == "123", "Error in ListToken"


# Generated at 2022-06-14 15:03:14.939522
# Unit test for method lookup of class Token
def test_Token_lookup():
    # Test token = Token(value = None, start_index = 0, end_index = 0, content = "")
    token = Token(value = None, start_index = 0, end_index = 0, content = "")
    # Test token.lookup(index = [])
    token.lookup(index = [])
    # Test token.lookup_key(index = [])
    token.lookup_key(index = [])

# Generated at 2022-06-14 15:03:18.041344
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    assert ScalarToken(None, start_index=0, end_index=0) == ScalarToken(None, start_index=0, end_index=0)

# Generated at 2022-06-14 15:03:20.889042
# Unit test for constructor of class ListToken
def test_ListToken():
    token = ListToken([], 1, 2)
    assert token._value == []
    assert token._start_index == 1
    assert token._end_index == 2


# Generated at 2022-06-14 15:03:31.257169
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    from typesystem import String
    import pytest
    from os import path

    # Test for default constructor
    token = ScalarToken("Test", 0, 3)
    assert token._value == "Test"
    assert token._start_index == 0
    assert token._end_index == 3
    assert token._content == ""
    assert token.value == "Test"
    assert token.start._line_no == 1
    assert token.start._column_no == 1
    assert token.start._index == 0
    assert token.end._line_no == 1
    assert token.end._column_no == 4
    assert token.end._index == 3
    assert token.string == "Test"
    assert repr(token) == "ScalarToken('Test')"
    assert token == ScalarToken("Test", 0, 3)

# Generated at 2022-06-14 15:03:40.148165
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    print('Unit test for method __hash__ of class ScalarToken')
    obj = ScalarToken(
        value=0, start_index=0, end_index=0, content=""
    )
    assert hash(obj) == hash(0)

    obj = ScalarToken(
        value=1, start_index=0, end_index=0, content=""
    )
    assert hash(obj) == hash(1)

    obj = ScalarToken(
        value=1.0, start_index=0, end_index=0, content=""
    )
    assert hash(obj) == hash(1.0)

    obj = ScalarToken(
        value="hello", start_index=0, end_index=0, content=""
    )
    assert hash(obj) == hash("hello")

    obj = ScalarToken

# Generated at 2022-06-14 15:03:42.197548
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    try:
        token = Token(None, None, None)
        if token == None: pass
    except: pass

# Generated at 2022-06-14 15:03:49.920647
# Unit test for constructor of class Token
def test_Token():
    t1 = Token(1, 1, 1)
    assert t1.string == ''
    assert t1.value == 1
    assert t1.start == Position(1, 1, 1)
    assert t1.end == Position(1, 1, 1)
    assert repr(t1) == "Token(1)"
    assert t1 == Token(1, 1, 1)
    assert t1 != Token(2, 1, 1)
    assert t1 != Token(1, 2, 1)
    assert t1 != Token(1, 1, 2)
    

# Generated at 2022-06-14 15:03:58.715124
# Unit test for method lookup of class Token
def test_Token_lookup():
    from typesystem import types
    from typesystem.parser.tokenizer import Tokenizer
    from typesystem.parser.parser import Parser

    tokenizer = Tokenizer()
    parser = Parser(tokenizer)
    token = parser.parse(types.Array(types.String))
    assert token.lookup([0]).value == types.String
    token = parser.parse(types.Dict(types.String, types.String))
    assert token.lookup([0]).value == types.String
    assert token.lookup([1]).value == types.String
    token = parser.parse(types.Object({"x": types.String}))
    assert token.lookup([0]).value == types.String


if __name__ == "__main__":
    import pytest
    pytest.main(["-s", __file__])

# Generated at 2022-06-14 15:04:02.866423
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    t = ScalarToken(None, None, None)
    assert t.__hash__() is None
    t = ScalarToken(1, None, None)
    assert t.__hash__() == 1


# Generated at 2022-06-14 15:04:58.477345
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    value_1 = "key"
    start_index_1 = 1
    end_index_1 = 3
    content_1 = "key"
    token_1 = ScalarToken(value_1, start_index_1, end_index_1, content_1)
    assert(token_1._get_value() == value_1)
    assert(token_1._start_index == start_index_1)
    assert(token_1._end_index == end_index_1)
    assert(token_1._content == content_1)
    assert(token_1.string == content_1[start_index_1 : end_index_1 + 1])
    assert(token_1.value == value_1)
    assert(token_1.start._line_no == 1)

# Generated at 2022-06-14 15:05:02.402997
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    start_index = 1
    end_index = 5
    content = "hello"
    token = Token("value", start_index, end_index, content)
    assert repr(token) == "Token(%s)" % repr(token.string)


# Generated at 2022-06-14 15:05:09.925424
# Unit test for constructor of class DictToken
def test_DictToken():
    # Test cases
    dict_token1 = DictToken({'key': 'value'}, 0, 4, '{key}')
    dict_token2 = DictToken({'key': 'value'}, 0, 5, '{key}')
    dict_token3 = DictToken({'key': 'value'}, 1, 5, '{key}')
    dict_token4 = DictToken({'key': 'value'}, 0, 5, '{key}')
    # Assertions
    assert dict_token1 != dict_token2
    assert dict_token1 != dict_token3
    assert dict_token1 != dict_token4
    assert dict_token2 != dict_token3
    assert dict_token2 != dict_token4
    assert dict_token3 != dict_token4

# Generated at 2022-06-14 15:05:12.610268
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    token = ScalarToken("a", 1, 2)
    assert token.string == "a"
    assert token.start.index == 1
    assert token.end.index == 2



# Generated at 2022-06-14 15:05:20.090954
# Unit test for constructor of class ListToken
def test_ListToken():
    token_list = [1, 2, 3]
    start_index = 1
    end_index = 3
    cont = ""
    token = ListToken(token_list, start_index, end_index, cont)
    assert token._value == token_list
    assert token._start_index == start_index
    assert token._end_index == end_index
    assert token._content == cont


# Generated at 2022-06-14 15:05:22.282263
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    obj = ScalarToken(None, None, None, None)
    assert obj.__hash__() is None


# Generated at 2022-06-14 15:05:26.683967
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    a = ScalarToken('hello', 0, 5)
    assert a.__repr__() == "ScalarToken('hello')"
    b = ListToken([a], 0, 5)
    assert b.__repr__() == "ListToken('hello')"
    c = DictToken({'a': b}, 0, 5)
    assert c.__repr__() == "DictToken('hello')"


# Generated at 2022-06-14 15:05:34.934530
# Unit test for method lookup of class Token
def test_Token_lookup():
    content = '''
    {
        "schema": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string"
                    }
                }
            }
        }
    }
    '''
    token = JSONToken(content)
    assert token.lookup([0, 1, 0, 'properties', 'name', 'type']) == ScalarToken('string', 91, 97)


# Generated at 2022-06-14 15:05:40.342536
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    token = ScalarToken(1,1,1)
    assert token._get_value() == 1
    assert token.value == 1
    assert token.start.line == 1
    assert token.start.column == 1
    assert token.start.index == 1
    assert token.end.line == 1
    assert token.end.column == 1
    assert token.end.index == 1
    assert token.string == ""


# Generated at 2022-06-14 15:05:47.860256
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    start_index_value = 10
    end_index_value = 20
    content_value = "some_string"
    value = "a_value"
    token = Token(value, start_index_value, end_index_value, content_value)
    index = [1,2]
    new_token = Token(value, start_index_value, end_index_value, content_value)
    token._get_child_token = lambda self, key: new_token
    token._get_key_token = lambda self, key: new_token
    result = token.lookup_key(index)
    assert result == new_token