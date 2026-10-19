

# Generated at 2022-06-14 14:56:22.722887
# Unit test for constructor of class DictToken
def test_DictToken():
    key = ScalarToken(1, 0, 1)
    value = ScalarToken(2, 2, 3)
    d = {key: value}
    token = DictToken(d, 0, 3)
    assert repr(token) == "DictToken({1: 2})"
    assert token.start.index == 0
    assert token.string == "{1: 2}"
    assert token.value == {1: 2}
    assert token.lookup([1]).value == 2
    assert token.lookup_key([1]).string == "1"
    return token


# Generated at 2022-06-14 14:56:24.197799
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken("Yes", 1, 1).string == "Yes"

# Generated at 2022-06-14 14:56:32.356250
# Unit test for constructor of class DictToken
def test_DictToken():
    x = {"k":2}
    y = {"k2":3}
    x2 = {"k3":3}
    dictTest = DictToken(x, 2, 6)
    dictTest2 = DictToken(y, 2, 6)
    dictTest3 = DictToken(x2, 2, 6)
    assert dictTest._get_value() == x
    assert dictTest._value == x
    assert dictTest._value["k"]._value == 2
    assert dictTest._child_tokens["k"]._get_value() == 2
    assert dictTest2._value["k2"]._value == 3
    assert dictTest3._value["k3"]._value == 3


# Generated at 2022-06-14 14:56:33.638322
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({})
    assert dict_token._value == {}

# Generated at 2022-06-14 14:56:45.561562
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({"key": ScalarToken(1, 2, 3)}, 1, 3, "content")
    # test constructor
    assert isinstance(d, dict)
    assert isinstance(d, DictToken)
    assert isinstance(d._child_tokens, dict)
    assert isinstance(d._child_tokens["key"], ScalarToken)
    assert isinstance(d._child_tokens["key"]._value, int)
    assert isinstance(d._child_keys, dict)
    assert isinstance(d._child_keys["key"], ScalarToken)
    assert isinstance(d._child_keys["key"]._value, str)
    assert isinstance(d._value, dict)
    assert isinstance(d._value["key"], ScalarToken)

# Generated at 2022-06-14 14:56:49.645593
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(None, 0, 1, "") == Token(None, 0, 1, "")
    assert Token(None, 0, 1, "") != None
    assert Token(None, 0, 1, "") != Token(None, 0, 2, "")
    assert Token(None, 0, 1, "") != "a"


# Generated at 2022-06-14 14:56:53.456531
# Unit test for constructor of class DictToken
def test_DictToken():
  # Need to provide a dummy value for _get_value()
  class _TestDictToken(DictToken):
    def _get_value(self) -> typing.Any:
      return ''
  # Should not raise error
  _TestDictToken(**{})
  

# Generated at 2022-06-14 14:57:01.037923
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # + Token.__eq__
    a = ScalarToken(12, 0, 1)
    assert a == a
    assert a != "not a Token instance"
    assert a != ScalarToken(1, 0, 1)
    assert a != ScalarToken(12, 1, 1)
    assert a != ScalarToken(12, 0, 2)
    # - Token.__eq__

# Generated at 2022-06-14 14:57:04.267075
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # __eq__(self, other)

    # (1) positive case
    t = Token(0, 0, 0)
    assert t == t

    # (2) negative case
    f = Token(0, 0, 0)
    assert not (t == f)


# Generated at 2022-06-14 14:57:08.126826
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({"a": 4}, 0, 1, "")
    assert d._child_keys == {"a": "a"}
    assert d._child_tokens == {"a": 4}



# Generated at 2022-06-14 14:57:18.060454
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {}
    t = DictToken(d, 0, 2)
    assert t._value == {}
    assert t._start_index == 0
    assert t._end_index == 2
    assert t._child_tokens == {}
    assert t._child_keys == {}


# Generated at 2022-06-14 14:57:19.541961
# Unit test for constructor of class DictToken
def test_DictToken():
	d = DictToken(None, 1, 2, "a")


# Generated at 2022-06-14 14:57:30.084117
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import io
    import os
    import unittest


    class Token___eq__Test(unittest.TestCase):
        def test(self):
            self.assertEqual(
                Token(
                    ScalarToken(1, 0, 1, "1"), 0, 1, "ScalarToken(1)"
                ),
                Token(ScalarToken(1, 0, 1, "1"), 0, 1, "ScalarToken(1)"),
            )

# Generated at 2022-06-14 14:57:31.978533
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({"a":"1"}, 0, 4, "hello")


# Generated at 2022-06-14 14:57:38.056780
# Unit test for constructor of class DictToken
def test_DictToken():
    a={"1":1, "2":2}
    b={"1":1, "2":2}
    c={"1":1, "2":2}
    dict1 = DictToken(a, 0, 2, b)
    dict2 = DictToken(a, 0, 2, c)
    assert dict1 != dict2

#Unit test for constructor of class ListToken

# Generated at 2022-06-14 14:57:48.224046
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import typesystem.parse as parse

    v = parse.parse_expression('{"test": 1}')
    assert repr(v) == "DictToken({'test': ScalarToken(1)})"
    w = parse.parse_expression('{"test": 1}')
    assert repr(w) == "DictToken({'test': ScalarToken(1)})"
    assert v == w
    w = parse.parse_expression('{"test": 2}')
    assert repr(w) == "DictToken({'test': ScalarToken(2)})"
    assert v != w
    w = parse.parse_expression('{"test": 1, "test2": 1}')
    assert repr(w) == "DictToken({'test': ScalarToken(1), 'test2': ScalarToken(1)})"
    assert v != w


# Generated at 2022-06-14 14:57:51.794494
# Unit test for constructor of class DictToken
def test_DictToken():
    key_token = ScalarToken("key",0,2)
    value_token = ScalarToken("value",5,9)
    DictToken({key_token:value_token},0,9)
    

# Generated at 2022-06-14 14:57:58.916420
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken('abc', 0, 2)
    token2 = ScalarToken('abc', 0, 2)
    token3 = ScalarToken('cde', 0, 2)
    token4 = ScalarToken('abc', 1, 2)
    token5 = ScalarToken('abc', 0, 3)
    token6 = ScalarToken('abc', 5, 6)
    token7 = ScalarToken('abc', 5, 10)
    # assert that the two tokens are equal
    assert(token1 == token2)
    # assert that the two tokens are not equal
    assert(token1 != token3)
    assert(token1 != token4)
    assert(token1 != token5)
    assert(token1 != token6)
    assert(token1 != token7)


# Generated at 2022-06-14 14:58:04.212463
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(None, 0, 1, "")
    assert token == token
    assert not (token != token)
    assert token.__eq__(token)
    assert not token.__eq__(None)
    assert token.__eq__(token)
    assert not token.__eq__(None)
    assert token != None # noqa

# Generated at 2022-06-14 14:58:09.042004
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.tokenizer import DictToken
    dct = {"a": 1, "b": 2, "c": 3}
    dct_token = DictToken(dct, 0, 1, "")
    assert dct_token.value == {'a': 1, 'b': 2, 'c': 3}


# Generated at 2022-06-14 14:58:21.230343
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.exceptions import TokenizationError
    from typesystem.tokenizers import JSONTokenizer
    content = '{"a": 1, "b": 2, "c": 3}'
    tokenizer = JSONTokenizer(content)
    token = tokenizer.load()
    token2 = tokenizer.load()
    assert (token == token2) == True
    tokenizer.load()
    try:
        tokenizer.load()
    except TokenizationError as e:
        assert "Unconsumed" in str(e)

# Generated at 2022-06-14 14:58:24.854122
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(value = {'a':'b'}, start_index = 2, end_index = 3, content = 'hi')
    assert token._child_keys == {'a': 'b'}
    assert token._child_tokens == {'a': 'b'}

# Generated at 2022-06-14 14:58:27.487014
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {"key1": "value1"}
    dt = DictToken(d, 0, 1)
    assert isinstance(dt, DictToken)
    assert dt.value == {'key1': 'value1'}


# Generated at 2022-06-14 14:58:31.359468
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(None, 2, 15, content="first line\nsecond line")
    t2 = Token(None, 2, 15, content="first line\nsecond line")
    assert t1 == t2

# Generated at 2022-06-14 14:58:35.009462
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    _token = Token(
        123,
        2,
        4,
        "--abcd--"
    )
    assert(_token.__eq__(123)==False)


# Generated at 2022-06-14 14:58:41.344142
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1, 2, 3, "abc") == Token(1, 2, 3, "abc")
    assert not Token(1, 2, 3, "abc") == Token(1, 2, 4, "abc")
    assert not Token(1, 2, 3, "abc") == Token(1, 2, 3, "abcd")
    assert not Token(1, 2, 3, "abc") == "1"
    assert not Token(1, 2, 3, "abc") == 1


# Generated at 2022-06-14 14:58:45.693766
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken(
        _value = 'hello',
        _start_index = 0,
        _end_index = 1,
        _content = "content",
        key = 1
    )

# Generated at 2022-06-14 14:58:48.801145
# Unit test for constructor of class DictToken
def test_DictToken():
	DictToken(
		dict(test=1, test2=2),
		1,
		5,
		"test\ntest2\ntest3"
	)

# Generated at 2022-06-14 14:58:51.269642
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken(value={}, start_index=0, end_index=0, content="")



# Generated at 2022-06-14 14:58:54.731663
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    T1 = Token("test1", 0, 4, "test1")
    T2 = Token("test2", 0, 4, "test1")
    assert T1 == T2

# Generated at 2022-06-14 14:59:09.730051
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert (ScalarToken(1, 0, 0) == ScalarToken(1, 0, 0))
    assert not (ScalarToken(1, 0, 0) != ScalarToken(1, 0, 0))

# Generated at 2022-06-14 14:59:14.677666
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    index_list = [1]
    token = Token(
        value=None, start_index=1, end_index=1, content=None
    )
    token_other = Token(
        value=None, start_index=1, end_index=1, content=None
    )
    assert token.__eq__(token_other) == True


# Generated at 2022-06-14 14:59:23.554205
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken(
        {"a": "b"}, 1, 2, content="{\"a\": \"b\"}"
    )
    assert dict_token.string == "{\"a\": \"b\"}"
    assert dict_token.value == {"a": "b"}
    assert dict_token.start == Position(1, 1, 0)
    assert dict_token.end == Position(1, 11, 10)
    assert dict_token.lookup([0]) == dict_token._get_key_token("a")
    assert dict_token.lookup([1]) == dict_token._get_child_token("a")
    assert dict_token.lookup_key([0, 0]) == dict_token._get_key_token("a")


# Generated at 2022-06-14 14:59:31.208967
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {1:2, 3:4}
    temp_dict = {k:v for k,v in d.items()}
    assert temp_dict == {1: 2, 3: 4}
    keys_dict = {k for k in d.keys()}
    assert keys_dict == {1, 3}
    child_dict = {k:v for k,v in d.items()}
    assert child_dict == {1: 2, 3: 4}
    d = DictToken(d, 0, 0, [])


# Generated at 2022-06-14 14:59:41.215105
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test no 1
    token1 = ScalarToken(2, 3, 4)
    token2 = ScalarToken(2, 3, 4)
    assert token1 == token2

    # Test no 2
    token3 = ScalarToken(3, 4, 5)
    assert not (token1 == token3)

    # Test no 3
    token4 = ScalarToken(2, 6, 5)
    assert not (token1 == token4)

    # Test no 4
    token5 = ScalarToken(2, 6, 5)
    assert not (token4 == token5)



# Generated at 2022-06-14 14:59:44.154370
# Unit test for constructor of class DictToken
def test_DictToken():
    value = {"Hi": "There"}
    assert DictToken(value, "", 0, 0).__class__.__name__ == "DictToken"



# Generated at 2022-06-14 14:59:50.365647
# Unit test for constructor of class DictToken
def test_DictToken():                 #line:18
    tok = DictToken({ 1 : "a" }, 0, 0) #line:19
    assert tok.string  == ""           #line:20
    assert tok.value == { 1 : "a" }    #line:21
    assert tok.start  == Position(1, 1, 0) #line:22
    assert tok.end    == Position(1, 1, 0) #line:23
    assert tok.lookup_key([ 0 ]) == {"1" : "a"}   #line:24

# Generated at 2022-06-14 15:00:00.124062
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test__eq__ A
    # Test__eq__ A returns True
    # Test__eq__ B
    # Test__eq__ B returns True
    # Test__eq__ C
    # Test__eq__ C returns True
    # Test__eq__ D
    # Test__eq__ D returns True
    # Test__eq__ E
    # Test__eq__ E returns False
    # Test__eq__ F
    # Test__eq__ F returns False
    # Test__eq__ G
    # Test__eq__ G returns False
    # Test__eq__ H
    # Test__eq__ H returns False
    # Test__eq__ I
    # Test__eq__ I returns False
    pass

# Generated at 2022-06-14 15:00:11.951962
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import typesystem
    path = typesystem.Path(".")
    tokens = path.parse("[a, b, c]")
    # LHS and RHS are of the same class
    assert tokens[0] == tokens[0]
    # LHS and RHS are of different class
    assert not tokens[0] == 1
    # LHS and RHS are of the same class and value is same
    assert tokens[0].value == "a"
    assert tokens[1].value == "b"
    assert tokens[1] == tokens[1]
    # LHS and RHS are of the same class and value is not same
    assert tokens[0].value == "a"
    assert tokens[1].value == "b"
    assert not tokens[0] == tokens[1]
    assert not tokens[1] == tokens[0]


# Generated at 2022-06-14 15:00:17.742727
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({1:1}, 0, 1)
    assert token._value == {1:1}
    assert token._start_index == 0
    assert token._end_index == 1
    assert token._content == None


# Generated at 2022-06-14 15:00:29.074446
# Unit test for constructor of class DictToken
def test_DictToken():
    # Failure case
    try:
        a = DictToken("a", "b", "c", "d")
        raise Exception("DictToken did not show an error when expected")
    except TypeError:
        pass

    # Success case
    try:
        a = DictToken("a", 0, 0)
    except TypeError:
        raise Exception("DictToken showed an error when not expected")


# Generated at 2022-06-14 15:00:37.740628
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.types import Dict, String

    dict_a = Dict(String, String, name="dict_a")
    dict_b = Dict(String, String, name="dict_b")
    dict_c = Dict(String, String, name="dict_c")

    d = DictToken({dict_a: dict_b, dict_c: dict_a})
    assert d._child_keys == {dict_a: dict_a, dict_c: dict_c}
    assert d._child_tokens == {dict_a: dict_b, dict_c: dict_a}

# Generated at 2022-06-14 15:00:40.179058
# Unit test for constructor of class DictToken
def test_DictToken():
    a = {'a': 1, 'b': 2, 'c': 3}
    b = DictToken(a, 1, 2, 'abc')
    assert b.value == {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-14 15:00:43.526778
# Unit test for constructor of class DictToken
def test_DictToken():
    expected_token = DictToken({})
    assert expected_token._child_keys == {}
    assert expected_token._child_tokens == {}
    assert expected_token._get_value() == {}


# Generated at 2022-06-14 15:00:48.406365
# Unit test for constructor of class DictToken
def test_DictToken():
    #Arrange
    t0 = Token(5, 5, 5, "")
    t1 = Token(6, 6, 6, "")
    test = DictToken({t0:t1}, 3, 3, "")
    #Act
    result = test._get_value()
    #Assert
    assert result == {5:6}


# Generated at 2022-06-14 15:00:52.279874
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({}, 0, 1)
    assert dict_token._get_value() == {}
    assert dict_token._start_index == 0
    assert dict_token._end_index == 1
    assert dict_token._content == ""


# Generated at 2022-06-14 15:00:53.732746
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken(1,2,3,4)

# Generated at 2022-06-14 15:01:03.527404
# Unit test for constructor of class DictToken
def test_DictToken():
    #assert False  # TODO: implement your test here
    dicttoken_1 = DictToken({"hello" : "world"}, 0, 6)
    assert dicttoken_1._child_keys.keys() == {"hello"}
    assert dicttoken_1._child_tokens.keys() == {"hello"}

    dicttoken_2 = DictToken({"hello" : "world", "me" : "too"}, 0, 6)
    assert dicttoken_2._child_keys.keys() == {"hello", "me"}
    assert dicttoken_2._child_tokens.keys() == {"hello", "me"}


# Generated at 2022-06-14 15:01:06.018495
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({"a": 0}, 1, 2, "foo")._value == {"a": 0}


# Generated at 2022-06-14 15:01:10.752398
# Unit test for constructor of class DictToken
def test_DictToken():
    object = DictToken({"a":1, "b":2}, 0, 0, "")
    assert object._child_keys == {"a":1, "b":2}
    assert object._child_tokens == {"a":1, "b":2}
    assert object._get_value() == {"a":1, "b":2}


# Generated at 2022-06-14 15:01:31.094129
# Unit test for constructor of class DictToken
def test_DictToken():
    d1 = DictToken({1:2})
    assert(d1.value == {1:2})
    assert(d1.start == (1,1,0))
    assert(d1.end == (1,3,2))
    assert(d1.string == "{1:2}")


if __name__ == '__main__':
    test_DictToken()

# Generated at 2022-06-14 15:01:32.614414
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken(dict(), 0, 2)
    assert t


# Generated at 2022-06-14 15:01:37.942296
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({'a': 1}, 0, 3, 'abc')._child_keys == {'a': 'a'}
    assert DictToken({'a': 1}, 0, 3, 'abc')._child_tokens == {'a': 1}


# Generated at 2022-06-14 15:01:40.887911
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {1:2,3:4}
    a = DictToken(d,0,5,'test')
    assert a.string == 'test'
    print(a.value)


# Generated at 2022-06-14 15:01:44.247627
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken(value={}, start_index = 0, end_index = 0, content = "")
    assert t._value == {}
    assert t._start_index == 0
    assert t._end_index == 0
    assert t._content == ""


# Generated at 2022-06-14 15:01:55.594770
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.compat import MutableMapping
    from typesystem.compat import Mapping
    from typesystem.compat import MutableSequence
    from typesystem.compat import Sequence
    from typesystem.compat import TYPE_CHECKING
    from typesystem.compat import TypingMeta
    from typesystem.compat import _generic_new

    mock_token = type("Token", (object,), {"__init__": lambda x, *args: None})
    # Unit test: constructor of class DictToken with empty dictionary
    test_empty_dict_token = DictToken(
        {}, 0, 0, content="", value=MutableMapping[str, mock_token]({})
    )
    assert test_empty_dict_token.value == {}
    assert test_empty_dict_token.string == ""
   

# Generated at 2022-06-14 15:02:07.314072
# Unit test for constructor of class DictToken
def test_DictToken():
    t1 = ScalarToken("kevin", 0, 4, content="kevin")
    t2 = ScalarToken("asdf", 5, 9, content="kevinasdf")
    t = DictToken({t1:t2}, 0, 9, content="kevinasdf")
    assert t._child_keys == {t1._value: t1}
    assert t._child_tokens == {t1._value: t2}
    assert t._get_value() == {"kevin":"asdf"}
    assert t._get_child_token("kevin") == t2
    assert t._get_key_token("kevin") == t1
    assert t.string == "kevinasdf"
    assert t.value == {"kevin":"asdf"}
    assert t.start == t1.start
    assert t

# Generated at 2022-06-14 15:02:17.069995
# Unit test for constructor of class DictToken
def test_DictToken():
    import typesystem
    import typesystem.types

    t = typesystem.Type("TestType", fields={"name": typesystem.String(), "age": typesystem.Integer()})
    dct = t()
    dct["name"] = "hello"
    dct["age"] = 12
    input = "{'a': 1, 'b': 2}"
    tk = DictToken(dct, 0, 0, input)
    assert tk.value == dct
    assert tk.start == Position(1, 1, 0)
    assert tk.end == Position(1, 1, 0)
    assert tk.string == input
    assert repr(tk) == "DictToken({'a': 1, 'b': 2})"


# Generated at 2022-06-14 15:02:20.418547
# Unit test for constructor of class DictToken
def test_DictToken():

    DictTokenInstance = DictToken('value','start_index','end_index','content')
    if DictTokenInstance._child_tokens is not None:
        assert True
    else:
        assert False


# Generated at 2022-06-14 15:02:30.608539
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({"a": 1, "b": 2}, 0, 10)
    assert(dict_token.start.line_no == 1)
    assert (dict_token.start.column_no == 1)
    assert (dict_token.start.index == 0)
    dict_token = DictToken({"a": 1, "b": 2}, 4, 10)
    assert (dict_token.start.line_no == 1)
    assert (dict_token.start.column_no == 5)
    assert (dict_token.start.index == 4)


# Generated at 2022-06-14 15:03:04.165352
# Unit test for constructor of class DictToken
def test_DictToken():
    # test case 1
    token = DictToken({}, 0, 0, "")
    if token.string != "":
        print("Error in DictToken constructor")


# Generated at 2022-06-14 15:03:11.280297
# Unit test for constructor of class DictToken
def test_DictToken():
    d1 = {'a': 1}
    d2 = {'b': 2}
    d3 = {'c': 3}
    dt1 = DictToken(d1, 0, 1, "a")
    dt2 = DictToken(d2, 1, 2, "b")
    dt3 = DictToken(d3, 2, 3, "c")
    print(dt1)
    dt_dict = {}
    dt_dict.update({dt1._value: dt1})
    dt_dict.update({dt2._value: dt2})
    dt_dict.update({dt3._value: dt3})
    dt4 = DictToken(dt_dict, 0, 3, "a\nb\nc")
    print(dt4)

# Generated at 2022-06-14 15:03:19.260741
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(
        {
            ScalarToken("hi", 0, 1): ScalarToken("hello", 2, 6),
            ScalarToken("one", 7, 10): ScalarToken("two", 11, 14),
        },
        0,
        14,
        "hihelloone",
    )
    assert token._child_keys["hi"].string == "hi"
    assert token._child_tokens["hi"].string == "hello"
    assert sorted(token._child_keys.keys()) == ["hi", "one"]

# Generated at 2022-06-14 15:03:23.593222
# Unit test for constructor of class DictToken
def test_DictToken():
    t1 = Token(1,0,1)
    t2 = Token(2,0,2)
    dic = DictToken({t1:t2},0,2)
    assert dic._child_keys == {1:t1}
    assert dic._child_tokens == {1:t2}

# Generated at 2022-06-14 15:03:24.533521
# Unit test for constructor of class DictToken
def test_DictToken():
    new_dict = DictToken


# Generated at 2022-06-14 15:03:31.062674
# Unit test for constructor of class DictToken
def test_DictToken():
    x = DictToken({
        'x':1,
        'y':2
    })
    assert x._get_value() == {'x':1,'y':2}
    assert x._get_child_token('x') == 1
    assert x._get_child_token('y') == 2
    assert x._get_key_token('x') == 'x'
    assert x._get_key_token('y') == 'y'
    return None


# Generated at 2022-06-14 15:03:33.674498
# Unit test for constructor of class DictToken
def test_DictToken():
    d = ({'a':'b'}, 0, 1)
    e = DictToken(*d)
    assert(e == DictToken(*d))



# Generated at 2022-06-14 15:03:35.220449
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(None, None, None, None)  # type: Token
    assert {} == token.value
    assert '{}' == token.string


# Generated at 2022-06-14 15:03:36.231429
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken()


# Generated at 2022-06-14 15:03:38.203175
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({0 : 0, 1 : 1}, 0, 1, content = "")
    assert token != None and token != ""


# Generated at 2022-06-14 15:04:11.563913
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.primitives import String
    from typesystem import Schema
    from typesystem.token import DictToken

    schema = Schema([String, String])
    token = DictToken({"abc": "def"}, 0, 6, "abc:def")
    assert token.string == "abc:def"
    assert token.value == {"abc": "def"}
    assert token.start.line == 1
    assert token.start.column == 1
    assert token.start.index == 0
    assert token.end.line == 1
    assert token.end.column == 7
    assert token.end.index == 6
    assert token.lookup([0]).string == "abc"
    assert token.lookup([1]).string == "def"
    assert token.lookup_key([0, 0]).string == "abc"

# Generated at 2022-06-14 15:04:14.943895
# Unit test for constructor of class DictToken
def test_DictToken():
    str1 = "test1"
    str2 = "test2"
    dict = {str1: str2}
    dict_token = DictToken(dict, 1, 2)
    assert isinstance(dict_token, DictToken)

# Generated at 2022-06-14 15:04:18.357832
# Unit test for constructor of class DictToken
def test_DictToken():
  token = DictToken({"a":"1", "b":"2"}, 0, 0)
  assert token == {"a":"1", "b":"2"}


# Generated at 2022-06-14 15:04:20.157010
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.tokens import Token
    def test_func(self):
        pass
    DictToken()

# Generated at 2022-06-14 15:04:26.094889
# Unit test for constructor of class DictToken
def test_DictToken():
    from collections import OrderedDict
    from .test_scanner import ScalarToken, test_content, test_start_index, test_end_index, test_value
    from . import test_DictToken

    t = ScalarToken(test_value, test_start_index, test_end_index, test_content)
    test_DictToken = DictToken(OrderedDict([('a', t), ('b', t)]), test_start_index, test_end_index, test_content)


# Generated at 2022-06-14 15:04:30.913497
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({1 : 1, 2 : 2}, 0, 50)
    # print(a._child_keys)
    # print(a._child_tokens)
    assert(a._child_keys[1] == 1)
    assert(a._child_tokens[1] == 1)
    assert(a._child_keys[2] == 2)
    assert(a._child_tokens[2] == 2)
test_DictToken()

# Generated at 2022-06-14 15:04:35.716561
# Unit test for constructor of class DictToken
def test_DictToken():
    content = "{{'first_key': 'first_value', 'second_key': 'second_value'}}"
    token = DictToken(
        {"first_key": "first_value", "second_key": "second_value"},
        0,
        len(content) - 1,
        content
    )
    assert token.string == content
    assert token.value == {"first_key": "first_value", "second_key": "second_value"}
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, len(content), len(content) - 1)
    assert token.lookup([0]).value == "first_value"
    assert token.lookup([0]).start == Position(1, 11, 10)

# Generated at 2022-06-14 15:04:38.504232
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({1:2, 3:4}, 1, 3)
    assert token.value == {1:2, 3:4}


# Generated at 2022-06-14 15:04:41.202813
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({"ab" : "ab"}, 0, 1)
    assert dict_token._child_tokens == {"ab" : "ab"}

# Generated at 2022-06-14 15:04:47.387534
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Dict
    from ZODB.FileStorage.FileStorage import FileStorage
    from ZODB.DB import DB

    storage = FileStorage('zodb.fs')
    db = DB(storage)
    connection = db.open()
    root = connection.root()
    root['d1'] = Dict({'a': 1,'b': 2})
    connection.add(root['d1'])
    transaction.commit()
    connection.close()
    del db
    storage.close()



# Generated at 2022-06-14 15:05:54.831226
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    assert ScalarToken(1,1,1).__hash__() == hash(1)


# Generated at 2022-06-14 15:05:57.950267
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    token = ScalarToken(value="test", start_index=0, end_index=3, content="test")
    assert hash(token) == hash("test")

# Generated at 2022-06-14 15:05:59.534504
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    ScalarToken("3", 0, 0).__str__()


# Generated at 2022-06-14 15:06:07.379046
# Unit test for constructor of class DictToken
def test_DictToken():
    # Normal case
    assert DictToken({"a": 1}, 0, 0).__dict__ == {'_value': {'a': 1}, '_start_index': 0, '_end_index': 0, '_content': ''} == {'_value': {'a': 1}, '_start_index': 0, '_end_index': 0, '_content': ''}
    assert DictToken({"a": 1}, 0, 0, content="").__dict__ == {'_value': {'a': 1}, '_start_index': 0, '_end_index': 0, '_content': ''} == {'_value': {'a': 1}, '_start_index': 0, '_end_index': 0, '_content': ''}
    # Exception case