

# Generated at 2022-06-14 14:56:20.776538
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken(value={"name": "salim"}, start_index=0, end_index=1)
    assert dict_token._value["name"] == "salim"


# Generated at 2022-06-14 14:56:27.237059
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1=Token([1,2,3],0,2)
    token2=Token([1,2,3],0,2)
    assert token1==token2
    token2=Token([0,0,0],0,2)
    assert token1!=token2
    token2=Token([],0,2)
    assert token1!=token2
    token2=Token([1,2,3],1,2)
    assert token1!=token2
    token2=Token([1,2,3],0,1)
    assert token1!=token2


# Generated at 2022-06-14 14:56:32.890678
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t = Token("a", 1, 2)
    assert t == Token("a", 1, 2)
    assert not t == Token("b", 1, 2)
    assert not t == Token("a", 2, 3)
    assert not t == Token("a", 1, 3)
    assert not t == 3
    assert not t == None
    assert not t == Token("a", 1, 2, "ab")
    assert not t == DictToken({"a": "a"}, 1, 2)


# Generated at 2022-06-14 14:56:38.020215
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_0 = Token(object(),0,0,"")
    # Call method __eq__
    assert(token_0.__eq__(token_0))
    token_1 = Token(object(),0,0,"")
    # Call method __eq__
    assert(token_1.__eq__(token_1))


# Generated at 2022-06-14 14:56:43.477484
# Unit test for constructor of class DictToken
def test_DictToken():
    tok = DictToken()
    assert(tok._child_keys == {})
    assert(tok._child_tokens == {})
    assert(tok.__dict__ == {})

    tok = DictToken(1,2,3,4)
    assert(tok._child_keys == {})
    assert(tok._child_tokens == {})
    #assert(tok.__dict__ == {'_value': 1})

    # Not sure if the code that called this constructor makes any sense
    # tok = DictToken(1,2,3,4,5,6,7,8,9)
    # assert(tok._child_keys == {})
    # assert(tok._child_tokens == {})
    # assert(tok.__dict__ == {

# Generated at 2022-06-14 14:56:47.885372
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(value = "value", start_index = 1, end_index = 1, content = "content")
    other = 1
    assert token._get_value() == other._get_value()
    assert token._start_index == other._start_index
    assert token._end_index == other._end_index

# Generated at 2022-06-14 14:56:49.816824
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = ScalarToken(str, 1, 5)
    other = ScalarToken(str, 1, 5)
    assert token == other

# Generated at 2022-06-14 14:56:56.774753
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Create Token object 'token_1'
    token_1 = Token()
    # Create Token object 'token_2'
    token_2 = Token()
    # Compare 'token_1' and 'token_2'
    result = token_1 == token_2
    # Ensure that result is 'False'
    assert result == False
    # Create Token object 'token_3'
    token_3 = Token()
    # Compare 'token_1' and 'token_3'
    result = token_1 == token_3
    # Ensure that result is 'True'
    assert result == True

# Generated at 2022-06-14 14:57:00.522329
# Unit test for constructor of class DictToken
def test_DictToken():
    value = dict()
    start_index = 0
    end_index = 10
    content = ""
    a = DictToken(value, start_index, end_index, content)


# Generated at 2022-06-14 14:57:06.187041
# Unit test for constructor of class DictToken
def test_DictToken():
    d=DictToken((1,2,3,4,5), content='helloworld')
    assert d.lookup([0])==d._get_child_token([0])
    assert d.lookup_key([0,1])==d._get_key_token([0,1])
    assert d.start==d._get_position(0)
    assert d.end==d._get_position(4)
    assert d.string==d._content[0:5]
    assert d.value=='h'
    

# Generated at 2022-06-14 14:57:14.225203
# Unit test for constructor of class DictToken
def test_DictToken():
    with pytest.raises(NotImplementedError):
        DictToken()._get_value()

    token = DictToken()
    assert token._get_value() is None

# Generated at 2022-06-14 14:57:15.225876
# Unit test for constructor of class DictToken
def test_DictToken():
    pass

# Generated at 2022-06-14 14:57:23.556869
# Unit test for constructor of class DictToken
def test_DictToken():
    token_key = ScalarToken("ab",0,1)
    token_value = ScalarToken("cd",2,3)
    test_dict = {token_key:token_value}
    dt = DictToken(test_dict,4,5)
    assert dt._value == test_dict
    assert dt._start_index == 4
    assert dt._end_index == 5
    assert dt._child_keys == {'ab':token_key}
    assert dt._child_tokens == {'ab':token_value}


# Generated at 2022-06-14 14:57:32.699748
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import typesystem.tokens

    t1 = typesystem.tokens.ScalarToken(1, 0, 1)
    t2 = typesystem.tokens.ScalarToken(1, 0, 1)
    assert t1 == t2

    t3 = typesystem.tokens.ScalarToken(2, 0, 1)
    assert t1 != t3

    t4 = typesystem.tokens.DictToken({"a": t1, "b": t3}, 0, 1)
    t5 = typesystem.tokens.DictToken({"a": t1, "b": t3}, 0, 1)
    assert t4 == t5
    assert t4.lookup([]) == t5.lookup([])
    assert t4.lookup(["a"]) == t5

# Generated at 2022-06-14 14:57:38.816070
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = ScalarToken(1, 0, 0, "")
    t2 = ScalarToken(1, 0, 0, "")
    t3 = ScalarToken(2, 0, 0, "")
    assert t1 == t2
    assert t1 != t3
    assert t1 == t1
    assert t1 != None
    assert t1 != 1
    assert t1 != [1]



# Generated at 2022-06-14 14:57:47.873223
# Unit test for constructor of class DictToken
def test_DictToken():
    test_dict_token = DictToken(
        {}, value=1, start_index=0, end_index=1, content="{}"
    )
    assert test_dict_token.value == {}
    assert test_dict_token.start.line_no == 1
    assert test_dict_token.start.column_no == 1
    assert test_dict_token.start.index == 0
    assert test_dict_token.end.line_no == 1
    assert test_dict_token.end.column_no == 1
    assert test_dict_token.end.index == 1
    assert test_dict_token.string == "{}"


# Generated at 2022-06-14 14:57:51.503934
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({"x": "2"}, 1, 3, "dict")
    assert a._child_keys == {"x": "2"}
    assert a._child_tokens == {"x": "2"}


# Generated at 2022-06-14 14:57:57.819585
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test if equal.
    # test_if_equal_01
    t01 = Token(123, 1, 10)
    t11 = Token(123, 1, 10)
    assert t01.__eq__(t11) is True

    # Test if not equal.
    # test_if_not_equal_01
    t01 = Token(123, 1, 10)
    t12 = Token(123, 2, 10)
    t13 = Token(124, 1, 10)
    assert t01.__eq__(t12) is False
    assert t01.__eq__(t13) is False


# Generated at 2022-06-14 14:58:00.943104
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken("key", "value", 0, 1, content="content")
    assert str(token) == "DictToken('content')"


# Generated at 2022-06-14 14:58:03.786597
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({1:1}, 0, 10)
    print(d._value)
    print(isinstance(d, Token))


# Generated at 2022-06-14 14:58:18.269001
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import pytest
    from .fixtures import simple_dict_token_values, simple_list_token_values

    def check(left: Token, right: Token):
        assert left == right

    check(
        ScalarToken(1, 0, 0, "1"),
        ScalarToken(1, 0, 0, "1"),
    )

    check(
        ScalarToken(1, 10, 10, "0123456789"),
        ScalarToken(1, 10, 10, "0123456789"),
    )

    with pytest.raises(AssertionError):
        check(
            ScalarToken(1, 0, 0, "1"),
            ScalarToken(2, 0, 0, "2"),
        )


# Generated at 2022-06-14 14:58:27.554338
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from .parser import Token as ParserToken

    token = ParserToken("b", 1, 1, "a")
    assert token._get_value() == "b"
    assert token._start_index == 1
    assert token._end_index == 1

    token = ParserToken("b", 1, 1, "a")
    assert token._get_value() == "b"
    assert token._start_index == 1
    assert token._end_index == 1
    token2 = ParserToken(
        {ParserToken("a", 1, 1, "a"): ParserToken("b", 2, 2, "a")}, 1, 2, "a"
    )
    assert token2._get_value() == {token: token}
    assert token2._start_index == 1
    assert token2._end_index == 2
   

# Generated at 2022-06-14 14:58:29.543665
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken(1, 3, 5) == ScalarToken(1, 3, 5)


# Generated at 2022-06-14 14:58:40.923301
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import get_type_from_python
    from typesystem.parser import parse_scalar
    from typesystem.parser import parse_dict
    from typesystem.parser import parse_list
    from typesystem.parser import parse_tuple
    from typesystem.parser import parse_enum
    from typesystem.parser import parse_union
    from typesystem.parser import parse_new_type
    from typesystem.parser import parse_type
    from typesystem.parser import parse_type_signature
    from typesystem.parser import parse_type_comment
    from typesystem.parser import parse_type_hint
    from typesystem.parser import parse_variable
    from typesystem.parser import parse_assignment
    from typesystem.parser import parse_expr
    from typesystem.parser import parse_import

# Generated at 2022-06-14 14:58:52.809576
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Create an instance of class Token with dummy values
    instance1 = Token(
        None,
        None,
        None,
        None,
    )
    instance1._get_value = lambda: None
    instance1._start_index = None
    instance1._end_index = None
    instance2 = Token(
        None,
        None,
        None,
        None,
    )
    instance2._get_value = lambda: None
    instance2._start_index = None
    instance2._end_index = None
    # Apply method __eq__ with the arguments

# Generated at 2022-06-14 14:59:03.393031
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(value="test_str", start_index=5, end_index=9)
    t2 = Token(value="test_str", start_index=5, end_index=9)
    assert t1 == t2
    t1_ = Token(value="test_str", start_index=6, end_index=9)
    assert not (t1 == t1_)
    t2_ = Token(value="test_str", start_index=5, end_index=8)
    assert not (t1 == t2_)
    t3_ = Token(value="test_str2", start_index=5, end_index=9)
    assert not (t1 == t3_)

# Generated at 2022-06-14 14:59:07.299089
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(1, 2, 3)
    assert False == (token == 1)
    assert not isinstance(token, type(1))
    assert True == (token == token)

# Generated at 2022-06-14 14:59:16.521279
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    text = "abcdef"
    token_a = ScalarToken(1, 2, 3, content=text)
    token_b = ScalarToken(1, 2, 3, content=text)
    token_c = ScalarToken(1, 2, 4, content=text)
    token_d = ScalarToken(1, 2, 5, content=text)

    assert token_a.__eq__(token_b)
    assert token_b.__eq__(token_a)

    assert not token_a.__eq__(token_c)
    assert not token_c.__eq__(token_a)

    assert not token_a.__eq__(token_d)
    assert not token_d.__eq__(token_a)

    assert token_c.__eq__(token_d)

# Generated at 2022-06-14 14:59:18.750114
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Calling the function returns something
    assert Token(1, 1, 2) == Token(1, 1, 2)



# Generated at 2022-06-14 14:59:26.195194
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Token object
    tk = Token(value = 12, start_index = 1, end_index = 2, content = "Hello, world!")
    assert tk == tk
    assert not (tk != tk)
    # ScalarToken object
    stk = ScalarToken(value = 12, start_index = 1, end_index = 2, content = "Hello, world!")
    assert stk == stk
    assert not (stk != stk)
    # DictToken object
    dtk = DictToken(value = 12, start_index = 1, end_index = 2, content = "Hello, world!")
    assert dtk == dtk
    assert not (dtk != dtk)
    # ListToken object

# Generated at 2022-06-14 14:59:34.061833
# Unit test for method __eq__ of class Token
def test_Token___eq__():
	t1 = Token(None, 1, 2, 3)
	assert t1.__eq__(t1)

# Generated at 2022-06-14 14:59:41.161254
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    token = ScalarToken(2, 3, 13, "Hello")
    assert token.string == "Hello"
    assert token.value == 2
    assert token.start.index == 3
    assert token.end.index == 13
    assert repr(token) == "ScalarToken('Hello')"
    assert token == ScalarToken(2, 3, 13, "Hello")
    assert token == ScalarToken(2, 3, 13)


# Generated at 2022-06-14 14:59:47.629800
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    start_index = 0
    end_index = 10
    token_value = 123
    string = str(token_value)
    token = ScalarToken(token_value, start_index, end_index, string)
    
    assert token.value == token_value
    assert token.start.index == start_index
    assert token.end.index == end_index
    assert token._value
    assert token.string == string



# Generated at 2022-06-14 14:59:50.211346
# Unit test for constructor of class ListToken
def test_ListToken():
    list_token = ListToken([], 0, 1, "")
    assert list_token.value == []


# Generated at 2022-06-14 14:59:50.957000
# Unit test for method lookup of class Token
def test_Token_lookup():
    assert 1 == 1

# Generated at 2022-06-14 14:59:55.310969
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    """
    Test method __hash__ of class ScalarToken
    """

    # Create a instance
    scalartoken_instance = ScalarToken(value, start_index, end_index)

    # Test the method
    scalartoken_instance.__hash__()

# Generated at 2022-06-14 15:00:00.247702
# Unit test for constructor of class ListToken
def test_ListToken():
    l=[Token(1), Token(2), Token(3), Token(4), Token(5)]
    l_t=ListToken(l, 0, len(l)-1)
    assert l_t._get_value() == [1,2,3,4,5]
    assert l_t.string == ''


# Generated at 2022-06-14 15:00:01.942957
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    token = ScalarToken(1,"1","2")
    print(token._get_value())


# Generated at 2022-06-14 15:00:06.852666
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    assert len({ScalarToken(1, 0, 1): 1, ScalarToken(2, 2, 3): 2}) == 2
    assert len({ScalarToken(1, 0, 1): 1, ScalarToken(1, 2, 3): 2}) == 1

# Generated at 2022-06-14 15:00:12.633288
# Unit test for constructor of class Token
def test_Token():
    string = "foo"
    start_index = 0
    end_index = 2
    new_token = Token(string, start_index, end_index)
    assert new_token.string == string
    assert new_token.value == string
    assert new_token.start == (1, 1, 0)
    assert new_token.end == (1, 4, 2)

# Generated at 2022-06-14 15:00:25.103139
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    """
    Unit test for method __hash__ of class ScalarToken
    """
    # Tested method is accessed through the class name
    assert ScalarToken.__hash__(None)



# Generated at 2022-06-14 15:00:28.581078
# Unit test for constructor of class Token
def test_Token():
    try:
        Token()
        assert False
    except NotImplementedError:
        assert True

    token = Token(1,2,3)
    assert token.start == Position(1,1,2)
    assert token.end == Position(1,1,3)
    assert token.string == ""


# Generated at 2022-06-14 15:00:39.246242
# Unit test for constructor of class DictToken
def test_DictToken():
    token_1 = ScalarToken(0, 0, 5)  # Initialize attributes of the class ScalarToken
    token_2 = ScalarToken(1, 5, 9)
    token_3 = ScalarToken(2, 10, 15)
    token_4 = ScalarToken(3, 15, 20)
    token_5 = ScalarToken(4, 20, 24)
    token_6 = ScalarToken(5, 25, 29)
    dict_1 = DictToken({token_1: token_2, token_3: token_4}, 0, 29, "0 True 2 False 3 True 4 False 5 True")  # Initialize attributes of the class DictToken
    assert isinstance(dict_1._value, dict)  # Check if dict_1._value is dict or not

# Generated at 2022-06-14 15:00:44.358868
# Unit test for method lookup of class Token
def test_Token_lookup():
    document = ListToken(
        [ScalarToken(1, 0, 0)],
        0,
        0,
        "[1]\n"
    )
    assert document.lookup([0]) == document._value[0]
    assert document.lookup([0,]) == document._value[0]


# Generated at 2022-06-14 15:00:46.661647
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({}, 0, 0)
    assert token._child_keys == {}
    assert token._child_tokens == {}

# Generated at 2022-06-14 15:00:53.613806
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    assert ScalarToken(1, 0, 1, "abc").value == 1
    assert ScalarToken(None, 0, 1, "abc").value is None
    assert ScalarToken(1, 0, 1, "abc") == ScalarToken(1, 0, 1, "abc")
    assert ScalarToken(1, 0, 1, "abc") != ScalarToken(1, 0, 2, "abc")
    assert ScalarToken(2, 0, 1, "abc") != ScalarToken(1, 0, 1, "abc")
    assert ScalarToken(1, 1, 1, "abc") != ScalarToken(1, 0, 1, "abc")
    assert ScalarToken(1, 0, 1, "abc") != ScalarToken(2, 0, 1, "abc")

# Generated at 2022-06-14 15:01:05.731382
# Unit test for method lookup of class Token
def test_Token_lookup():
    token1 = Token(None, 1, 3)
    token2 = Token(None, 1, 3)
    token3 = Token(None, 1, 3)
    token4 = Token(None, 1, 3)
    token5 = Token(None, 1, 3)
    token6 = Token(None, 1, 3)
    token7 = Token(None, 1, 3)
    token8 = Token(None, 1, 3)
    token9 = Token(None, 1, 3)
    token10 = Token(None, 1, 3)
    token11 = Token(None, 1, 3)
    token12 = Token(None, 1, 3)
    token13 = Token(None, 1, 3)
    token14 = Token(None, 1, 3)
    token15 = Token(None, 1, 3)


# Generated at 2022-06-14 15:01:13.003090
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(5, 0, 1, "5.1") == Token(5, 0, 1, "5.2")
    assert Token(5, 0, 1, "5.1") != None
    assert Token(5, 0, 1, "5.1") != "5.1"
    assert Token(5, 0, 1, "5.1") != Token(5, 1, 2, "5.1")
    assert Token(5, 0, 1, "5.1") != Token(4, 0, 1, "5.1")
    assert Token(5, 0, 1, "5.1") != Token(5, 0, 1, "4.1")


# Generated at 2022-06-14 15:01:22.016200
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    def _(dummy_x1, dummy_y1, dummy_x2, dummy_y2):
        m = Token(dummy_x1, dummy_y1, dummy_x2, dummy_y2)
        return m
    m0 = _(1, 1, 1, "")
    m1 = m0
    m2 = _(2, 1, 1, "")
    m3 = _(1, 2, 1, "")
    m4 = _(1, 1, 2, "")
    m5 = _(1, 1, 1, "2")
    m6 = _(2, 1, 2, "2")
    m7 = _(1, 2, 2, "2")
    m8 = _(1, 1, 2, "3")

# Generated at 2022-06-14 15:01:23.810814
# Unit test for method lookup of class Token
def test_Token_lookup():
    assert Token.lookup(0) == 0


# Generated at 2022-06-14 15:01:39.382892
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    assert ScalarToken(value=5, start_index=5, end_index=10).__hash__() == hash(5)



# Generated at 2022-06-14 15:01:43.883003
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    tok = ScalarToken(42, 0, 1, "42")
    assert tok._value == 42
    assert tok._start_index == 0
    assert tok._end_index == 1
    assert tok.string == "4"
    assert tok.value == 42
    assert tok.start == Position(1, 1, 0)
    assert tok.end == Position(1, 2, 1)
    assert isinstance(tok, Token)



# Generated at 2022-06-14 15:01:46.909008
# Unit test for method lookup of class Token
def test_Token_lookup():
    x = Token(1, 2, 3, "test")
    assert(x.lookup([1,3]) == None)


# Generated at 2022-06-14 15:01:56.156860
# Unit test for method lookup of class Token
def test_Token_lookup():
    class TestToken(Token):
        def _get_child_token(self, key: typing.Any) -> Token:
            if key == "child":
                return TestToken2()
            else:
                return TestToken3()
    class TestToken2(Token):
        def _get_child_token(self, key: typing.Any) -> Token:
                return TestToken3()
    class TestToken3(Token):
        def _get_child_token(self, key: typing.Any) -> Token:
                return self
    t = TestToken()
    assert(t.lookup(["child"]) == TestToken2())
    assert(t.lookup(["child", "child", "child"]) == TestToken3())

# Generated at 2022-06-14 15:02:07.713434
# Unit test for constructor of class ListToken
def test_ListToken():
    tok = [
    {
        'token': 'DictToken',
        'value': {
            'b': 'ScalarToken',
            'a': 'ScalarToken'
        },
        'start_index': 3,
        'end_index': 15
    },
    {
        'token': 'DictToken',
        'value': {
            'b': 'ScalarToken',
            'a': 'ScalarToken'
        },
        'start_index': 3,
        'end_index': 15
    },
    {
        'token': 'DictToken',
        'value': {
            'b': 'ScalarToken',
            'a': 'ScalarToken'
        },
        'start_index': 3,
        'end_index': 15
    }
]

# Generated at 2022-06-14 15:02:09.741485
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    t = ScalarToken(1, 0, 2, "123")
    assert t.start.line == 1
    assert t._value == 1

# Generated at 2022-06-14 15:02:21.018222
# Unit test for method lookup of class Token
def test_Token_lookup():
    token = Token(
        value=["1", "2", "3", "4"],
        start_index=0,
        end_index=3,
        content= "1\n2\n3\n4\n"
    )
    assert token.lookup([1]).string == "2"
    assert token.lookup([0]).string == "1"
    assert token.lookup([0]).value == "1"
    assert token.lookup([1]).value == "2"
    assert token.lookup([2]).value == "3"
    assert token.lookup([3]).value == "4"
    assert token.lookup([0]).start.line == 1
    assert token.lookup([0]).start.column == 1
    assert token.lookup([0]).end.line == 1
    assert token.look

# Generated at 2022-06-14 15:02:32.471731
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_0 = ScalarToken(value=0, start_index=0, end_index=1)
    token_0_0 = ScalarToken(value=0, start_index=0, end_index=1)
    token_1 = ScalarToken(value=1, start_index=0, end_index=1)
    token_0_diff_start_index = ScalarToken(value=0, start_index=1, end_index=1)
    token_0_diff_end_index = ScalarToken(value=0, start_index=0, end_index=0)

    assert token_0 == token_0
    assert not token_0 == token_1
    assert token_0 == token_0_0
    assert not token_0 == token_0_diff_start_index
    assert not token_

# Generated at 2022-06-14 15:02:35.947809
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = Token(10,12,15, content = 'abcdefg')
    assert token.__repr__() == "Token('efg')"


# Generated at 2022-06-14 15:02:45.973281
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    import unittest
    import typesystem

    parser = typesystem.Parser()

    result = parser.parse_string("123")
    assert result == ScalarToken(123, 0, 2, "123")

    result = parser.parse_string("'''foo'''")
    assert result == ScalarToken("foo", 3, 6, "'''foo'''")

    result = parser.parse_string("123[0]")
    assert result == ScalarToken(1, 5, 6, "123[0]")

    result = parser.parse_string("123[1:]")
    assert result == ScalarToken([2, 3], 5, 8, "123[1:]")

    result = parser.parse_string("'foo'[0]")

# Generated at 2022-06-14 15:03:06.938308
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    # int
    assert repr(ScalarToken(1, 1, 2)) == "ScalarToken('1')"
    assert repr(ScalarToken(10, 1, 4)) == "ScalarToken('10')"
    # float
    assert repr(ScalarToken(1.1, 1, 4)) == "ScalarToken('1.1')"
    assert repr(ScalarToken(1.10, 1, 5)) == "ScalarToken('1.10')"
    # string
    assert repr(ScalarToken("hello", 1, 7)) == "ScalarToken('hello')"
    assert repr(ScalarToken("hello world", 1, 13)) == "ScalarToken('hello world')"
    # dict
    key_token = ScalarToken("hello", 1, 7)
   

# Generated at 2022-06-14 15:03:12.607377
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    value = 1
    start_index = 0
    end_index = 0
    content = 0
    st = ScalarToken(value, start_index, end_index, content)
    assert st._value == 1
    assert st._start_index == 0
    assert st._end_index == 0
    assert st._content == 0


# Generated at 2022-06-14 15:03:15.241865
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    from typesystem import Integer

    assert Token(Integer(1), 0, 1).__repr__() == 'Token(1)'


# Generated at 2022-06-14 15:03:22.236190
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({"a": 1, "b": 2}, 0, 0)
    assert token._value == {"a": 1, "b": 2}
    assert token._start_index == 0
    assert token._end_index == 0
    assert token._content == ""
    assert token._child_keys == {'a': 'a', 'b': 'b'}
    assert token._child_tokens == {'a': 1, 'b': 2}


# Generated at 2022-06-14 15:03:24.996938
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # set up test data
    from typesystem.parser import Token
    t = Token(1, 1, 1)
    t2 = Token(1, 1, 1)
    assert t == t2


# Generated at 2022-06-14 15:03:33.524398
# Unit test for constructor of class ListToken
def test_ListToken():
    def f(x):
        return x
    t = ListToken([f], 0, 4, content="abcdefg")
    assert t._start_index == 0
    assert t._end_index == 4
    assert t._content == "abcdefg"
    assert t._value == [f]
    assert t.string == "abcde"
    assert t.start.line_no == 1
    assert t.start.column_no == 1
    assert t.start.index == 0
    assert t.end.line_no == 1
    assert t.end.column_no == 5
    assert t.start.index == 4


# Generated at 2022-06-14 15:03:37.586436
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    tok = ScalarToken('1', 0, 1, '123')
    assert tok.string == '1'
    assert tok.start == Position(1, 1, 0)
    assert tok.end == Position(1, 2, 1)
    assert tok._value == '1'


# Generated at 2022-06-14 15:03:41.890522
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    tk = Token(value = "", end_index = 78, start_index =1, content = "78")
    tk1 = Token(value = "", end_index = 78, start_index =1, content = "78")
    assert tk == tk1


# Generated at 2022-06-14 15:03:44.976341
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    test_token = ScalarToken(value=5, start_index=4, end_index=5)
    assert test_token.__repr__() == 'ScalarToken(5)'


# Generated at 2022-06-14 15:03:46.847872
# Unit test for method lookup of class Token
def test_Token_lookup():
    test_token = ListToken([DictToken({})], 0, 0, "")
    i = [0, 'a']
    assert test_token.lookup(i) == None



# Generated at 2022-06-14 15:04:25.324872
# Unit test for constructor of class Token
def test_Token():
    content = "hello world"
    token = Token(None, 0, len(content)-1, content)
    assert isinstance(token, Token)
    assert token.string == 'hello world'
    assert token.value == None
    assert token.start.line_no == 1
    assert token.start.column_no == 1
    assert token.start.index == 0
    assert token.end.line_no == 1
    assert token.end.column_no == 12
    assert token.end.index == len(content)-1
    assert token.lookup(None) == token
    assert token.lookup_key(None) == token
    assert token.__hash__() == None
    assert token.__eq__(token) == True
test_Token()


# Generated at 2022-06-14 15:04:32.290334
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    test_str = "test string"
    token = ScalarToken(test_str, 0, len(test_str), content=test_str)
    assert token.string == test_str
    assert token.value == test_str
    assert token.start.line == 1
    assert token.start.column == 1
    assert token.start.index == 0
    assert token.end.line == 1
    assert token.end.column == len(test_str)
    assert token.end.index == len(test_str) - 1
    assert token.__repr__() == "ScalarToken('test string')"
    assert token.__eq__(ScalarToken(test_str, 0, len(test_str), content=test_str))


# Generated at 2022-06-14 15:04:34.162305
# Unit test for constructor of class ListToken
def test_ListToken():
    assert ListToken([0, 1, 2], 0, 4, "0, 1, 2")



# Generated at 2022-06-14 15:04:39.139143
# Unit test for constructor of class Token
def test_Token():
    tk = Token(1, 2, 3)

    assert tk._value == 1
    assert tk._start_index == 2
    assert tk._end_index == 3
    assert tk._content == ""

    tk = Token(1, 2, 3, "123")
    assert tk.string == "3"



# Generated at 2022-06-14 15:04:42.208805
# Unit test for method __repr__ of class Token
def test_Token___repr__():

    token = Token('', 1, 2, content="")
    print(str(token)[1:-1])

# Generated at 2022-06-14 15:04:47.476235
# Unit test for method lookup of class Token
def test_Token_lookup():
    #  Given
    class MyToken(Token):
        def _get_value(self):
            return 'value'
        def _get_child_token(self, key):
            return self._value[key]
        def _get_key_token(self, key):
            return self._value[key]

    token = MyToken(['value'], 0, 0)

    #  Then
    assert token.lookup([0])._get_value() == 'value'


# Generated at 2022-06-14 15:04:49.464539
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    """Unit test for method __eq__ of class Token"""
    assert True # TODO: implement your test here


# Generated at 2022-06-14 15:04:58.769128
# Unit test for method lookup of class Token
def test_Token_lookup():
    d = {"one": 123, "two": 456, "three": 789}
    output = {
        "one": ScalarToken(123, 6, 8, "123, \"two\": 456\n    }")
    }
    assert output == (
        DictToken(d, 0, 27, "{\n    \"one\": 123, \"two\": 456\n    }").lookup([0])
    )

    d = {"one": {"two": {"three": {"four": {"five": 789}, "six": 1011}}}},

# Generated at 2022-06-14 15:05:08.040804
# Unit test for method lookup of class Token
def test_Token_lookup():
    from .lexer import Lexer
    from .parser import ListParser, DictParser, ScalarParser
    from .base import BaseParser
    from . import Position
    l = Lexer("[\"foo\", \"bar\"]")
    t_list = DictParser(l)
    t_list.parse(l.get_token())
    t_list.create_token()
    # Test whether the method is called correctly
    assert t_list.lookup([0]) == t_list._children[0].lookup([])
    # Test whether the token is created successfully
    assert t_list.value == ["foo", "bar"]
    assert t_list.lookup([0]).value == ["foo"]
    assert t_list.start == Position(1, 1, 0)
    assert t_list.lookup([0]).start == Position

# Generated at 2022-06-14 15:05:13.593795
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    class Temp(Token):
        def _get_value(self):
            return 'a'

        def _get_child_token(self, key):
            return Temp()

        def _get_key_token(self, key):
            return Temp()

    result = Temp(value='a', start_index=1, end_index=1, content='a').lookup_key([0, 1])
    assert repr(result) == "Temp('a')"
