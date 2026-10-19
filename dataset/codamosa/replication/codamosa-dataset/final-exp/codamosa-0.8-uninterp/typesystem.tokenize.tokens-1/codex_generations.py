

# Generated at 2022-06-14 14:56:18.373497
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(value = {}, start_index = 0, end_index = 0, content = "")

# Generated at 2022-06-14 14:56:26.170789
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    my_token1 = ScalarToken([1, 2, 3], 1, 3)
    my_token2 = ScalarToken([1, 2, 3], 1, 3)
    my_token3 = ScalarToken([1, 2, 3, 4], 1, 3)
    my_token4 = ScalarToken([1, 2, 3], 0, 3)
    my_token5 = ScalarToken([1, 2, 3], 1, 4)
    assert (my_token1 == my_token2)
    assert not (my_token1 == my_token3)
    assert not (my_token1 == my_token4)
    assert not (my_token1 == my_token5)


# Generated at 2022-06-14 14:56:30.291392
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({'key': 'value'}, 0, 3, '{key:value}')
    assert token._value['key']._value == 'value'
    value = token._get_value()
    assert value['key'] == 'value'
    assert token._child_tokens['key']._value == 'value'
    assert token._child_keys['key']._value == 'key'

# Generated at 2022-06-14 14:56:37.373812
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({"a": 1, "b": 2}, 0, 0, "") == DictToken({"a": 1, "b": 2}, 0, 0, "")
    assert DictToken({"a": 1, "b": 2}, 0, 0, "") != DictToken({"a": 2, "b": 2}, 0, 0, "")
    assert DictToken({"a": 1, "b": 2}, 0, 0, "") != DictToken({"a": 1, "b": 2}, 1, 0, "")
    assert DictToken({"a": 1, "b": 2}, 0, 0, "") != DictToken({"a": 1, "b": 2}, 0, 1, "")

# Generated at 2022-06-14 14:56:48.561622
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_1 = Token("value", 0, 5, "string")
    token_2 = Token("value", 0, 5, "string")
    token_3 = Token("value1", 0, 5, "string")
    token_4 = Token("value", 1, 5, "string")
    token_5 = Token("value", 0, 6, "string")
    token_6 = Token("value", 0, 5, "string1")
    assert token_1 == token_2, "test_Token___eq__: method __eq__ is failed"
    assert token_1 != token_3, "test_Token___eq__: method __eq__ is failed"
    assert token_1 != token_4, "test_Token___eq__: method __eq__ is failed"

# Generated at 2022-06-14 14:56:56.399067
# Unit test for constructor of class DictToken
def test_DictToken():
    a = ScalarToken('1', 1, 2)
    b = ScalarToken('2', 3, 4)
    c = ScalarToken('3', 5, 6)
    d = ScalarToken('4', 7, 8)
    ab = DictToken({a:b, c:d}, 0, 9, '1 2\n3 4')
    assert ab._child_keys[a._value] == a
    assert ab._child_tokens[a._value] == b
    assert ab._child_keys[c._value] == c
    assert ab._child_tokens[c._value] == d
    


# Generated at 2022-06-14 14:57:01.400857
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(3, 2, 5)
    assert token == token
    assert not (token != token)
    other_token = Token(3, 2, 5)
    assert token == other_token
    assert not (token != other_token)

    def setUp(self):
        pass
    pass



# Generated at 2022-06-14 14:57:02.282087
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass



# Generated at 2022-06-14 14:57:08.078722
# Unit test for constructor of class DictToken
def test_DictToken():
    # try:
    d = {'a': 1, 'b': 2}
    dt = DictToken(d, 0, 1)
    assert isinstance(dt, DictToken)
    assert len(dt._child_keys) == 2
    assert len(dt._child_tokens) == 2
    # except:
    #     print('test_DictToken() failed!')
    


# Generated at 2022-06-14 14:57:11.706906
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(value={}, start_index=0, end_index=0, content="")
    assert token._value == {}
    assert token._start_index == 0
    assert token._end_index == 0
    assert token._content == ""


# Generated at 2022-06-14 14:57:21.044393
# Unit test for constructor of class DictToken
def test_DictToken():
    """
    Try to construct a DictToken object with some arbitrary arguments.
    """
    dict_token = DictToken(
        {
            ScalarToken(1, 0, 0): ScalarToken(2, 1, 1),
            ScalarToken(3, 2, 2): ScalarToken(4, 3, 3),
        },
        4,
        5,
        content="1234",
    )

# Generated at 2022-06-14 14:57:29.393273
# Unit test for constructor of class DictToken
def test_DictToken():
    """
    Check that DictToken constructor creates an object
    """
    # test class content
    token_value = {'a': 'b', 'c': 'd'}
    # test indices
    start_index = 0
    end_index = 2
    # test content
    content = 'abcdefg'
    new_token = DictToken(value = token_value, start_index = start_index, end_index = end_index,
                          content = content)
    # check initial value is the same as one passed to constructor
    assert new_token._child_tokens == token_value


# Generated at 2022-06-14 14:57:31.607148
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem import Structure, Text
    from typesystem.components import Dictionary, Keys

    class Structure(Structure):
        name = Text()
        data = Dictionary(Structure, Keys.KEYS)
    

# Generated at 2022-06-14 14:57:35.442456
# Unit test for constructor of class DictToken
def test_DictToken():
    dic = DictToken({}, 0, 0)
    assert dic._child_keys == {}
    assert dic._child_tokens == {}
    assert dic._start_index == 0
    assert dic._end_index == 0

# Generated at 2022-06-14 14:57:44.581769
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(value=1, start_index=1, end_index=2, content="") == Token(value=1, start_index=1, end_index=2, content="")
    assert Token(value=1, start_index=1, end_index=2, content="") != Token(value=2, start_index=1, end_index=2, content="")
    assert Token(value=1, start_index=1, end_index=2, content="") != Token(value=1, start_index=2, end_index=2, content="")
    assert Token(value=1, start_index=1, end_index=2, content="") != Token(value=1, start_index=1, end_index=3, content="")


# Generated at 2022-06-14 14:57:54.155257
# Unit test for constructor of class DictToken
def test_DictToken():
    my_dict_token= DictToken({"a":1,"b":2,"c":3},0,6,"abc abc")
    assert my_dict_token.value == {"a":1,"b":2,"c":3}
    assert my_dict_token.start == {"a":1,"b":2,"c":3}
    assert my_dict_token.end == {"a":1,"b":2,"c":3}
    assert my_dict_token.string == "abc"
    assert my_dict_token._get_value == {"a":1,"b":2,"c":3}
    assert my_dict_token.lookup == "a"
    assert my_dict_token.lookup_key == "a"



# Generated at 2022-06-14 14:58:05.981597
# Unit test for constructor of class DictToken
def test_DictToken():
    # Define token for testing
    key_tokens = {'one':1, 'two':2, 'three':3}
    value_tokens = {'one':1, 'two':2, 'three':3}

    # Define mock object for the class
    mock_DictToken = mock.Mock(spec=DictToken)
    mock_DictToken.value = key_tokens
    mock_DictToken.child_keys = {k._value: k for k in value_tokens.keys()}
    mock_DictToken.child_tokens = {k._value: v for k, v in value_tokens.items()}
    mock_DictToken.return_value = mock_DictToken

    # Test the method
    mock_DictToken._get_value()



# Generated at 2022-06-14 14:58:14.206396
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from tokens import ListToken
    from tokens import DictToken
    from tokens import ScalarToken
    assert Token(None, None, None) == Token(None, None, None)
    assert not Token(None, None, None) == None
    assert not Token(None, None, None) == Token([], None, None)
    assert ListToken([], None, None) == ListToken([], None, None)
    assert not ListToken([], None, None) == ListToken([1], None, None)
    assert not ListToken([], None, None) == ListToken([None], None, None)
    assert not ListToken([], None, None) == None
    assert ListToken([ScalarToken(None, None, None)], None, None) == ListToken([ScalarToken(None, None, None)], None, None)

# Generated at 2022-06-14 14:58:22.800584
# Unit test for constructor of class DictToken
def test_DictToken():
    '''
    Unit test for constructor of class DictToken
    '''
    value = {"1": 1, "2": 2}
    start_index = 0
    end_index = 1
    content = ""
    d = DictToken(value, start_index, end_index, content)
    print("_get_value: " + str(d._get_value()))
    print("_get_child_token: " + str(d._get_child_token("1")))
    print("_get_key_token: " + str(d._get_key_token("1")))


# Generated at 2022-06-14 14:58:27.033570
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(None,0,1,"some_string") == Token(None,0,1,"some_string")
    assert Token(None,0,1,"some_string") != Token(None,10,1,"some_string")

# Generated at 2022-06-14 14:58:40.860140
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # type: () -> None
    class MyToken(Token):
        pass

    token1 = MyToken(1, 2, 3, "a")
    token2 = MyToken(1, 2, 3, "a")
    token3 = MyToken(1, 2, 3, "b")

    assert token1 == token2
    assert not token1 == token3
    assert not token1 == "token1"

# Generated at 2022-06-14 14:58:52.741748
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Create new instance of a class
    class1_instance1 = Token("value", 0, 1, "content")
    class1_instance2 = Token("value", 0, 1, "content")
    assert class1_instance1.__eq__(class1_instance2) == isinstance(class1_instance2, Token) and (class1_instance1._get_value() == class1_instance2._get_value() and class1_instance1._start_index == class1_instance2._start_index and class1_instance1._end_index == class1_instance2._end_index)
    # Create new instance of a class
    class2_instance1 = Token("value", 0, 1)
    class2_instance2 = Token("value", 0, 1)

# Generated at 2022-06-14 14:59:05.046316
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = ScalarToken(1, 1, 1)
    t2 = ScalarToken(1, 1, 1)
    result = t1 == t2
    assert result == True
    t1 = ScalarToken(1, 2, 1)
    result = t1 == t2
    assert result == False
    t1 = ScalarToken(1, 1, 2)
    result = t1 == t2
    assert result == False
    t1 = ScalarToken(2, 1, 1)
    result = t1 == t2
    assert result == False
    t1 = ListToken([t2], 1, 1)
    result = t1 == t2
    assert result == False
    t1 = DictToken({t2: t2}, 1, 1)
    result = t1 == t2
    assert result == False


# Generated at 2022-06-14 14:59:13.739608
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(value=None, start_index=None, end_index=None)
    t2 = Token(value=None, start_index=None, end_index=None)
    assert t1 == t2
    t3 = Token(value=None, start_index=None, end_index=None, content=None)
    assert t1 == t3
    assert t2 == t3
    t4 = Token(value=None, start_index=None, end_index=None, content="test")
    assert t4 != t1
    assert t4 != t2
    assert t4 != t3


# Generated at 2022-06-14 14:59:22.342722
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = "abcdef"
    token1 = Token(1, 1, 2, content)
    token2 = Token(2, 3, 4, content)
    token3 = Token(1, 1, 2, content)
    assert token1 == token3
    assert token1 != token2
    # test with other object types
    assert token1 != 1
    assert token1 != "abc"
    assert token1 != ["abc", "cde"]
    # test index
    content = "abc\nabcdefghijklm"
    token1 = Token(1, 1, 2, content)
    token2 = Token(1, 1, 2, content)
    assert token1 == token2



# Generated at 2022-06-14 14:59:29.066684
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    A = '""a"}'
    B = '{"a"'
    C = '""a"}'
    token_a = generate_token(A)
    token_b = generate_token(B)
    token_c = generate_token(C)
    result_a = token_a.__eq__(token_b)
    result_b = token_a.__eq__(token_c)
    assert result_a!=result_b

# Generated at 2022-06-14 14:59:31.317601
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(1,1,1)
    token2 = Token(2,2,2)
    assert token1!=token2
    assert token1!=1


# Generated at 2022-06-14 14:59:38.576764
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(0, 1, 2)
    assert token == token

    token1 = Token(0, 1, 2)
    assert token == token1

    token2 = Token(1, 1, 2)
    assert token != token2

    token3 = Token(0, 2, 2)
    assert token != token3

    token4 = Token(0, 1, 3)
    assert token != token4

# Generated at 2022-06-14 14:59:40.609655
# Unit test for method __eq__ of class Token
def test_Token___eq__():
	# token is an instance of class Token
	token = None
	token.__eq__(other)

# Generated at 2022-06-14 14:59:50.426803
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    value = "value"
    start_index = 0
    end_index = 3
    content = "content"

    # With '0', '3', 'content' => Return False
    token1 = Token(value, start_index, end_index, content)
    token2 = Token(value, start_index, end_index, content)
    eq = token1.__eq__(token2)
    assert eq == False

    # With '0', '2', 'content' => Return False
    token1 = Token(value, start_index, end_index, content)
    token2 = Token(value, start_index, end_index - 1, content)
    eq = token1.__eq__(token2)
    assert eq == False

    # With '0', '4', 'content' => Return False
    token1 = Token

# Generated at 2022-06-14 14:59:56.080605
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken(dict(), 0, 2, "")

# Generated at 2022-06-14 15:00:02.041310
# Unit test for constructor of class DictToken
def test_DictToken():
    d_token = DictToken(value = {}, start_index = 0, end_index = 0, content = "")

    assert(d_token._value == {})
    assert(d_token._start_index == 0)
    assert(d_token._end_index == 0)
    assert(d_token._content == "")
    assert(d_token._child_keys == {})
    assert(d_token._child_tokens == {})


# Generated at 2022-06-14 15:00:06.957702
# Unit test for constructor of class DictToken
def test_DictToken():
    """
    Test for the constructor of the class DictToken.
    """
    from typesystem.base import Token
    DictToken('{n:n}', 1, 3, '{n:n}')


test_DictToken()


# Generated at 2022-06-14 15:00:08.824591
# Unit test for constructor of class DictToken
def test_DictToken():
    # Test valid
    t = DictToken({}, 0, 0)
    assert t.start == Position(1, 1, 0)
    assert t.end == Position(1, 1, 0)


# Generated at 2022-06-14 15:00:15.350086
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Token

    t1 = Token(1, 0, 1, 'abc')
    t2 = Token(2, 1, 2, 'abc')
    dt = DictToken({t1: t2}, 0, 2, 'abc')
    assert dt.start == Position(1, 1, 0)
    assert dt.end == Position(1, 2, 2)
    assert dt.lookup([1]).value == 2


# Generated at 2022-06-14 15:00:19.738740
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 1
    end_index = 2
    content = {'a':1, 'b':2}
    dict_token = DictToken(content, start_index, end_index)
    assert dict_token._get_value() == content, 'Error!'


# Generated at 2022-06-14 15:00:24.084240
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.integer import IntegerType
    from typesystem.string import StringType
    from typesystem.typing import DictionaryType

    StringType().validate("RAWR")
    IntegerType().validate(2)

    test = DictionaryType({
        StringType(): IntegerType()
    })

    test.validate({
        "RAWR": 2
    })

# Generated at 2022-06-14 15:00:30.331763
# Unit test for constructor of class DictToken
def test_DictToken():
    d1 = DictToken(None, 1, 2, content = 'first')
    d2 = DictToken(None, 2, 3, content = 'second')
    d3 = DictToken(None, 3, 4, content = 'third')
    d4 = DictToken(None, 4, 5, content = 'fourth')
    d5 = DictToken(None, 5, 6, content = 'fifth')
    d6 = DictToken(None, 6, 7, content = 'sixth')
    
    assert(d1.string == 'first')
    assert(d1.value == None)
    assert(d1.start == Position(1, 1, 1))
    assert(d1.end == Position(1, 6, 6))
    assert(hash(d1) == hash(None))

# Generated at 2022-06-14 15:00:33.270644
# Unit test for constructor of class DictToken
def test_DictToken():
  a=DictToken({'a':1})
  assert a._get_value()=={'a':1}


# Generated at 2022-06-14 15:00:37.517249
# Unit test for constructor of class DictToken
def test_DictToken():
    # should construct a DictToken object successfully
    a = DictToken({1:3, 2:4}, 0, 3, '{1:3,2:4}')
    assert a._value == ({1:3, 2:4}, 0, 3, '{1:3,2:4}')


# Generated at 2022-06-14 15:00:51.456974
# Unit test for constructor of class DictToken
def test_DictToken():
    value = {'a': 1, 'b': 2, 'c': 3}
    start_index = 1
    end_index = 2
    content = "{'a': 1, 'b': 2, 'c': 3}"
    token = DictToken(value, start_index, end_index, content)


# Generated at 2022-06-14 15:00:56.396069
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({"k":"v"})
    assert isinstance(dt._value, dict)
    # testing if DictToken._get_value() works as per spec
    assert isinstance(dt._get_value(), dict)
    assert dt._get_value() == {"k":"v"}


# Generated at 2022-06-14 15:01:03.158892
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_value = {'key': 'value'}
    token_key = ScalarToken('key', 1, 1, 'key')
    token_value = ScalarToken('value', 1, 1, 'value')
    dict_token = DictToken({token_key: token_value}, 1, 1, 'key')
    assert dict_token._get_value() == dict_value


# Generated at 2022-06-14 15:01:10.930548
# Unit test for constructor of class DictToken
def test_DictToken():
    a = Token(5,5,5)
    b = Token(5,5,5)
    d1 = {a: b}
    d2 = {a: b}
    token1 = DictToken(d1,5,5)
    token2 = DictToken(d2,5,5)
    assert token1._child_tokens == d1
    assert token1._child_keys == {a._value: a}
    assert token2._get_value() == {a._get_value(): b._get_value()}
    assert token1 == token2


# Generated at 2022-06-14 15:01:12.398330
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken.__init__

# Generated at 2022-06-14 15:01:21.575383
# Unit test for constructor of class DictToken
def test_DictToken():
    a = {1: 'a', 2: 'b'}
    t = DictToken(a, 0, 2, content = 'a')
    try:
        t.lookup(list([1]))
        assert t.lookup(list([1])) == t._value[1]
    except:
        print('Except: def _get_child_token(_self, key:typing.Any)->Token, key = 1.')
        assert True
    try:
        t.lookup(list([2]))
        assert t.lookup(list([2])) == t._value[2]
    except:
        print('Except: def _get_child_token(_self, key:typing.Any)->Token, key = 2.')
        assert True

# Generated at 2022-06-14 15:01:28.832688
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({
        ScalarToken(1, 0, 2): ScalarToken(2, 4, 6)
    }, 0, 10, "1: 2")
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 5, 4)
    assert token.lookup([0]).value == 2
    assert token.lookup_key([0]).value == 1



# Generated at 2022-06-14 15:01:36.760129
# Unit test for constructor of class DictToken
def test_DictToken():
    tok1 = ScalarToken("k1",0,3,"")
    tok2 = ScalarToken("v1",4,7,"")
    tok3 = ScalarToken("k2",8,11,"")
    tok4 = ScalarToken("v2",12,15,"")

    dt = DictToken({tok1: tok2, tok3: tok4},0,15)

    assert dt._value == {tok1: tok2, tok3: tok4}
    assert dt.string == ""
    assert dt.value == {"k1":"v1", "k2":"v2"}
    assert dt.start == Position(1,1,0)
    assert dt.end == Position(1,16,15) 
    assert dt.lookup([])

# Generated at 2022-06-14 15:01:38.265426
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken({"hello": "world"}, 0, 0)


# Generated at 2022-06-14 15:01:46.852742
# Unit test for constructor of class DictToken
def test_DictToken():
    a = """{"a": "a", "b": "b"}"""
    b = """{"a": "a", "b": "b"}"""
    c = """{"a": "a", "b": "b", "c": "c"}"""
    d = """{"a": "a", "b": "b", "c": "c", "d": "d"}"""
    
    assert DictToken(eval(a)) == DictToken(eval(b))
    assert DictToken(eval(a)) != DictToken(eval(c))
    assert DictToken(eval(a)) != DictToken(eval(d))
    assert DictToken(eval(b)) == DictToken(eval(c))
    assert DictToken(eval(b)) != DictToken(eval(d))

# Generated at 2022-06-14 15:02:13.336364
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({'foo': 'bar'}, 0, 5, content='{foo: bar}')
    b = DictToken({'foo': 'bar'}, 0, 5, content='{foo: bar}')
    c = DictToken({'fizz': 'buzz'}, 0, 5, content='{fizz: buzz}')
    d = DictToken({'foo': 'bar'}, 0, 4, content='{foo: bar}')
    e = DictToken({'fizz': 'buzz'}, 1, 5, content='{fizz: buzz}')
    f = DictToken({'fizz': 'buzz'}, 0, 5, content='{fizz: buzz1}')
    assert a == b
    assert a != c
    assert a != d
    assert a != e
    assert a

# Generated at 2022-06-14 15:02:19.612121
# Unit test for constructor of class DictToken
def test_DictToken():
    key_token = ScalarToken(1,0,0)
    value_token = ScalarToken(2,0,0)
    token = DictToken({key_token:value_token},0,0)
    assert token.value == {1:2}
    assert token.lookup([]) == token
    assert token.lookup_key([]) == token
    assert token.lookup([0]) == value_token
    assert token.lookup_key([0]) == key_token

# Generated at 2022-06-14 15:02:31.734951
# Unit test for constructor of class DictToken
def test_DictToken():
    a = Position(1,2,3)
    b = Position(1,2,3)
    b._line_no = 2
    c = Position(1,1,1)
    d = Position(1,2,3)
    d._column_no = 4
    e = Position(1,2,4)
    
    _a = DictToken(1, 1, 1, "")
    _b = DictToken(1, 2, 3, "")
    _c = DictToken(1, 1, 3, "")
    _d = DictToken(1, 2, 4, "")
    _e = DictToken(1, 2, 4, "1")

    assert _a._value == 1
    assert _a._start_index == 1
    assert _a._end_index == 1

# Generated at 2022-06-14 15:02:42.905661
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Dict
    from typesystem.fields import String
    a = String()
    b = String()
    dic_field = Dict({"a": a, "b": b})
    list_field = List(a)
    list_token = ListToken([a, b], 1, 2)
    dict_token = DictToken({"a": list_token}, 1, 2)
    assert dict_token == DictToken({"a": list_token}, 1, 2)
    assert dict_token._get_value() == {"a": [a, b]}
    assert dict_token.lookup([0]) == dict_token._value["a"]
    assert dict_token.lookup([0, 1]) == b


# Generated at 2022-06-14 15:02:45.973405
# Unit test for constructor of class DictToken
def test_DictToken():
    # Write your code here
    d = DictToken(dict(a=1,b=2),0,0)
    assert d._value[1] == 2


# Generated at 2022-06-14 15:02:49.266215
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {'a':2,'b':3}
    a = {'a':2,'b':3}
    b = {'a':3,'b':3}
    assert d == a
    assert d != b

# Generated at 2022-06-14 15:02:54.565519
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import tokenize_string
    from io import StringIO

    data = '{"key1": "value1", "key2": "value2"}'
    content = StringIO(data)
    tokens = tokenize_string(content)
    assert tokens[0].value == {"key1" : "value1", "key2" : "value2"}

# Generated at 2022-06-14 15:03:00.241546
# Unit test for constructor of class DictToken
def test_DictToken():
    v = "v"
    start_index = 1
    end_index = 1
    content = "content"
    kwargs = {"value":v, "start_index":start_index, "end_index":end_index, "content":content}
    t = DictToken(**kwargs)
    assert t._value == v
    assert t._start_index == start_index
    assert t._end_index == end_index
    assert t._content == content


# Generated at 2022-06-14 15:03:09.690715
# Unit test for constructor of class DictToken
def test_DictToken():
    test_DictToken_dict = {'a':1,'b':2}
    # print(test_DictToken_dict)
    test_DictToken_keys = ['a', 'b']
    test_DictToken_values = [1, 2]
    # print(test_DictToken_keys)
    # print(test_DictToken_values)
    test_DictToken_Dict = DictToken(test_DictToken_dict, 0, 1, 'abc')
    # print(test_DictToken_Dict._get_value())
    assert isinstance(test_DictToken_Dict.value, dict)
    # print(test_DictToken_Dict.value)
    assert test_DictToken_Dict.lookup_key(['a']) == test_DictToken

# Generated at 2022-06-14 15:03:21.700425
# Unit test for constructor of class DictToken
def test_DictToken():
    list_of_tokens = [
        1,
        2,
        3
    ]
    d = {
        'one': 1,
        'two': 2,
        'three': 3
    }
    token_dict = DictToken(
        d,
        0,
        1,
        "one two three"
    )
    assert(token_dict._value == d)
    assert(token_dict._start_index == 0)
    assert(token_dict._end_index == 1)
    assert(token_dict._content == "one two three")
    assert(token_dict._child_keys == {'one': 1, 'two': 2, 'three': 3})
    assert(token_dict._child_tokens == {'one': 1, 'two': 2, 'three': 3})
   

# Generated at 2022-06-14 15:04:04.527506
# Unit test for constructor of class DictToken
def test_DictToken():
    t1 = DictToken({"key1": 1}, 0, 3, "k1: 1")
    assert t1 == DictToken({"key1": 1}, 0, 3, "k1: 1")
    t2 = DictToken({"key2": 2}, 0, 3, "k2: 2")
    assert t2 == DictToken({"key2": 2}, 0, 3, "k2: 2")
    t3 = DictToken({"key1": 1}, 0, 3, "k1: 1")
    assert t3 == DictToken({"key1": 1}, 0, 3, "k1: 1")
    t4 = DictToken({"key2": 2}, 0, 3, "k2: 2")

# Generated at 2022-06-14 15:04:07.977267
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken(1, 2, 3, 4, 1234)
    assert t.__init__(1, 2, 3, 4, 1234) is None, 'Default DictToken constructor test failed'


# Generated at 2022-06-14 15:04:13.296434
# Unit test for constructor of class DictToken
def test_DictToken():
    test_token = DictToken({"a": 0, "b": 1}, 0, 1, "ab")
    assert(test_token._child_keys == {"a": "a", "b": "b"})
    assert(test_token._child_tokens == {"a": 0, "b": 1})
    assert(test_token._value == {"a": 0, "b": 1})


# Generated at 2022-06-14 15:04:18.324649
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {'a': ScalarToken('a', 0, 0),'b': ScalarToken('b', 0, 0)}
    a = DictToken(d, 0, 1, "")
    assert a._get_value() == {'a': 'a', 'b': 'b'}



# Generated at 2022-06-14 15:04:27.928951
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({1:1,2:2},0,4,content='{"1":1,"2":2}')
    assert dict_token._value[1] == 1
    assert dict_token._value[2] == 2
    assert dict_token.string == '{"1":1,"2":2}'
    assert dict_token.value == {1:1,2:2}
    assert dict_token.start == Position(1,1,0)
    assert dict_token.end == Position(1,13,4)
    assert dict_token.lookup([1]) == 1
    assert dict_token.lookup([2]) == 2
    assert dict_token.lookup_key([1]) == 1
    assert dict_token.lookup_key([2]) == 2
    assert dict_token.__

# Generated at 2022-06-14 15:04:39.188027
# Unit test for constructor of class DictToken
def test_DictToken():
    token0 = ScalarToken(value=0, start_index=0, end_index=1)
    token1 = ScalarToken(value=1, start_index=2, end_index=3)

    token = DictToken(
        value={token0: token1}, start_index=0, end_index=3, content="0 1"
    )

    assert token._value == {token0: token1}
    assert token._child_keys == {0: token0}
    assert token._child_tokens == {0: token1}
    assert token._content == "0 1"
    assert token.string == "0 1"
    assert token.value == {0: 1}
    assert token.start == Position(line_no=1, column_no=1, index=0)

# Generated at 2022-06-14 15:04:40.163228
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken()



# Generated at 2022-06-14 15:04:44.781120
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {'key': 'value'}
    d1 = DictToken(d,1,3,'mockup')
    assert d1._value == d
    assert d1._start_index == 1
    assert d1._end_index == 3
    assert d1._content == 'mockup'


# Generated at 2022-06-14 15:04:48.393258
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {
        1: {
            2: 3
        }
    }
    a = DictToken(1, 2, 3, d)
    assert id(a) is not None

# Generated at 2022-06-14 15:04:51.031627
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token: DictToken = DictToken('key')
    assert dict_token.value == 'key'

# Generated at 2022-06-14 15:06:10.812860
# Unit test for constructor of class DictToken
def test_DictToken():
    tokenA = ScalarToken(1, 0, 0)
    tokenB = ScalarToken(2, 0, 0)
    input_dict = {tokenA : tokenB}
    input_dict[tokenB] = tokenA
    test_token = DictToken(input_dict, 0, 0)
    assert test_token._value == input_dict
    assert test_token._child_keys == {1: tokenA, 2: tokenB}
    assert test_token._child_tokens == {1: tokenB, 2: tokenA}
    assert test_token._get_value() == {1: 2, 2: 1}
