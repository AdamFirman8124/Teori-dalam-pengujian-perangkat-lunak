

# Generated at 2022-06-14 14:56:27.741893
# Unit test for constructor of class DictToken
def test_DictToken():

    # Create a couple of ScalarTokens as inputs to DictToken
    s1 = ScalarToken(1,0,0)
    s2 = ScalarToken(2,1,1)

    # Create a DictToken
    obj = DictToken({s1: s2}, 0, 2, "something")

    # Check the start and end positions
    assert obj.start.index == 0
    assert obj.end.index == 2

    # Check the value of the child_tokens and child_keys
    assert obj._child_keys == {1: s1}
    assert obj._child_tokens == {1: s2}

    # Check the value of the string
    assert obj.string == "something"


# Generated at 2022-06-14 14:56:33.266555
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    c = Token(object(), 0, 0)
    c1 = Token(object(), 0, 0)
    c2 = Token(object(), 0, 0)
    c3 = Token(object(), 0, 0)
    assert (c == c1)
    assert not (c == c2)
    assert not (c == c3)
    assert (c1 == c2)
    assert not (c1 == c3)
    assert (c2 == c3)


# Generated at 2022-06-14 14:56:45.142485
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.lexer import Token as TokenClass
    from typesystem.lexer import ScalarToken as ScalarTokenClass
    from typesystem.lexer import DictToken as DictTokenClass
    from typesystem.lexer import ListToken as ListTokenClass

    t1 = ScalarTokenClass("value", 0, 2)
    t2 = ScalarTokenClass("value", 3, 5)
    t3 = ScalarTokenClass("value", 0, 2)
    t4 = ScalarTokenClass("value", 0, 2, "value")

    assert not isinstance(t1, TokenClass)
    assert t1 != t2
    assert t1 == t3
    assert t1 == t4

    d1 = DictTokenClass({"key": t1}, 0, 2)

# Generated at 2022-06-14 14:56:48.105209
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(value = "This is a valid Token.", start_index = 6, end_index = 13, content = "This is a valid Token.")
    assert token == token
test_Token___eq__()

# Generated at 2022-06-14 14:56:51.492286
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(
        {}, 1, 2
    )
    assert token._value == {}
    assert token._start_index == 1
    assert token._end_index == 2
    assert token._content == ""


# Generated at 2022-06-14 14:56:56.167220
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(4,4,4)
    t2 = Token(4,4,4)
    t3 = Token(4,4,6)
    t4 = Token(5,4,4)
    
    print(t1==t2)
    print(t1==t3)
    print(t1==t4)


# Generated at 2022-06-14 14:57:03.035835
# Unit test for constructor of class DictToken
def test_DictToken():
    a = Token(3, 0, 1, "hello")
    b = Token(2, 1, 1, "hi")
    value = {a: b}
    x = DictToken(value,0,1, "test")
    assert x._child_keys[3] == a
    assert x._child_tokens[3] == b
    assert x._start_index == 0
    assert x._end_index == 1
    assert x._content == "test"


# Generated at 2022-06-14 14:57:13.553715
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    a = Token(1, 2, 3)
    b = Token(2, 3, 1)
    c = Token(1, 2, 3)
    a_ = ScalarToken(1, 2, 3)
    b_ = ScalarToken(2, 3, 1)
    c_ = ScalarToken(1, 2, 3)
    a_c_ = ListToken(1, 2, 3)
    b_c_ = ListToken(2, 3, 1)
    c_c_ = ListToken(1, 2, 3)
    # Different values
    assert not (a == b)
    assert not (b == a)
    assert not (b_ == a_)
    assert not (a_ == b_)
    # Different start index
    assert not (a == c_.start)

# Generated at 2022-06-14 14:57:20.087485
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1,2,3) == Token(1,2,3)
    assert not Token(1,2,3) == Token(1,2)
    assert not Token(1,2,3) == Token(1,2,4)
    assert not Token(1,2,3) == Token(2,2,3)
    assert not Token(1,2,3) == 'Token(1,2,3)'

# Generated at 2022-06-14 14:57:30.450614
# Unit test for constructor of class DictToken
def test_DictToken():
    class TokenStub:
        def __init__(self, value: typing.Any, start_index: int, end_index: int, content: str = ""):
            self._value = value
            self._start_index = start_index
            self._end_index = end_index
            self._content = content
        def __eq__(self, other: typing.Any) -> bool:
            return isinstance(other, Token) and (
                self._value == other._value
                and self._start_index == other._start_index
                and self._end_index == other._end_index
            )
    def dict_token_instance(*args: typing.Any, **kwargs: typing.Any):
        return DictToken(*args, **kwargs)

# Generated at 2022-06-14 14:57:37.956764
# Unit test for constructor of class DictToken
def test_DictToken():
    values = {'a': 2, 'b': 3}
    keys = {'a': (1,1,1), 'b': (2,2,2)}
    dt = DictToken(values, keys)


# Generated at 2022-06-14 14:57:44.192206
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    mock_Token = mocker.Mock(spec=Token)
    mock_Token._get_value.return_value = 1
    mock_Token2 = mocker.Mock(spec=Token)
    mock_Token2._get_value.return_value = 1
    mock_Token3 = mocker.Mock(spec=Token)
    mock_Token3._get_value.return_value = 2

    assert Token._get_position(mock_Token, mock_Token) == Position(1, 1, 1)


# Generated at 2022-06-14 14:57:46.986257
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = DictToken('a', 0, 1 )
    token2 = DictToken('a', 0, 1 )
    assert(token1 == token2)

# Generated at 2022-06-14 14:57:50.326166
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({"Dog": 1}, start_index=1, end_index=3)
    assert d._child_keys == {"Dog": None}
    assert d._child_tokens == {"Dog": 1}

# Generated at 2022-06-14 14:57:53.557677
# Unit test for constructor of class DictToken
def test_DictToken():
    Token = DictToken()
    assert Token._get_value() == {key_token._get_value(): value_token._get_value() for key_token, value_token
                                  in Token._value.items()}


# Generated at 2022-06-14 14:58:03.455476
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.types import String, Integer
    from typesystem.schemas import Schema
    from typesystem.parser import _make_token

    schema = Schema({"string": String, "integer": Integer})
    value = {"string": "one", "integer": 1}
    token = _make_token(schema, value)

    assert isinstance(token, DictToken)
    assert token.string == u'{"string": "one", "integer": 1}'
    assert token.value == {"string": "one", "integer": 1}
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 32, 31)


# Generated at 2022-06-14 14:58:12.722907
# Unit test for constructor of class DictToken
def test_DictToken():
    # Create a Token instance with initial value '{"a":1,"b":2}', content '{"a":1,"b":2}'
    # and _start_index = 0 and _end_index = 11
    d = DictToken({"a": 1, "b": 2}, 0, 11, '{"a":1,"b":2}')
    # Create a Token instance with initial value '{"a":1,"b":2}', content '{"a":1,"b":2}'
    # and _start_index = 0 and _end_index = 11
    e = DictToken({"a": 1, "b": 2}, 0, 11, '{"a":1,"b":2}')

    # The following statement should return True
    assert e == d
    # The following statement should return False

# Generated at 2022-06-14 14:58:13.826635
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass #TODO: Implement function


# Generated at 2022-06-14 14:58:15.588638
# Unit test for constructor of class DictToken
def test_DictToken():
    # arrange
    t = DictToken("{}")
    # act
    pass
    # assert
    assert isinstance(t, Token)


# Generated at 2022-06-14 14:58:19.926806
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    obj = Token('value', 1, 2)
    assert not obj.__eq__(None)
    assert not obj.__eq__('value')
    assert not obj.__eq__('')
    assert not obj.__eq__(True)
    assert not obj.__eq__(1)
    assert obj.__eq__(obj)


# Generated at 2022-06-14 14:58:28.538833
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({1: 2, 3: 4}, 0, 1, "")
    assert token._child_keys == {1: 2, 3: 4}
    assert token._child_tokens == {1: 2, 3: 4}



# Generated at 2022-06-14 14:58:32.439336
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_1 = Token(1, 1, 5)
    token_2 = Token(1, 1, 5)

    assert(token_1 == token_2)

# Generated at 2022-06-14 14:58:36.919056
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert (Token(1, 0, 1) == Token(1, 0, 1)) == True
    assert (Token(1, 0, 2) == Token(1, 1, 2)) == False
    assert (Token(2, 0, 1) == Token(1, 0, 1)) == False

# Generated at 2022-06-14 14:58:44.956895
# Unit test for constructor of class DictToken
def test_DictToken():
    d1 = {"1": 1, "2": 2}
    d2 = {"3": 3, "4": 4}
    d1_token = DictToken(d1, 0, 6, "test_string")
    d2_token = DictToken(d2, 7, 12, "test_string")
    assert d1_token._value == {"1": 1, "2": 2}
    assert d2_token._value == {"3": 3, "4": 4}
    assert d1_token._start_index == 0
    assert d2_token._start_index == 7
    assert d1_token._end_index == 6
    assert d2_token._end_index == 12
    assert d1_token._content == "test_string"
    assert d2_token._content == "test_string"
   

# Generated at 2022-06-14 14:58:51.511131
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import Token
    from typesystem.types import String
    import typing

    def _get_token(string: str) -> Token:
        schema = String()
        schema.validate(string)
        return schema.errors[0][0]

    assert _get_token("test") == _get_token("test")
    assert not _get_token("test") == _get_token("another")



# Generated at 2022-06-14 14:58:55.466033
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    instance1 = Token(1, 2, 3)
    instance2 = Token(4, 5, 6)
    assert instance1 == instance1
    assert instance2 == instance2
    assert not instance1 == instance2


# Generated at 2022-06-14 14:58:57.370433
# Unit test for constructor of class DictToken

# Generated at 2022-06-14 14:59:03.916280
# Unit test for constructor of class DictToken
def test_DictToken():
    class DictToken_Node:
        def __init__(self, **kwargs: int):
            self._value = DictToken(kwargs)
            self._start_index = '1'
            self._end_index = '3'
            self._content = '4-6'

    node = DictToken_Node()

    assert node._get_value() == DictToken

assert DictToken

# Generated at 2022-06-14 14:59:14.790379
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from copy import copy
    from typesystem import Scalar

    class MyToken(Token):
        def __init__(self, value, start_index, end_index):
            super().__init__(value, start_index, end_index)

    class_dict = copy(MyToken.__dict__)
    class_dict.update({"_get_value": lambda self: self._value})

    MyToken2 = type("MyToken2", (MyToken,), class_dict)

    token1 = MyToken(1, 1, 2)
    token2 = MyToken2(1, 1, 2)
    token3 = MyToken2(2, 1, 2)
    token4 = MyToken2(1, 2, 2)
    token5 = MyToken2(1, 1, 3)

    assert token1 == token1
   

# Generated at 2022-06-14 14:59:23.938823
# Unit test for constructor of class DictToken
def test_DictToken():
    # Unit test for constructor of class DictToken
    class Position:
        def __init__(self, line_no, column_no, index):
            self.line_no = line_no
            self.column_no = column_no
            self.index = index
    data = {0: Position(1, 1, 0), 1: Position(5, 8, 12)}
    kwargs = {'value':data, 'start_index':0, 'end_index':12, 'content':'test content'}
    dict_token = DictToken(**kwargs)
    dic = {0:Position(1, 1, 0), 1:Position(5, 8, 12)}
    assert dict_token._value == dic
    assert dict_token._start_index == 0
    assert dict_token._end_index == 12


# Generated at 2022-06-14 14:59:30.712061
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken(1,2,3) == ScalarToken(1,2,3)

# Generated at 2022-06-14 14:59:38.173980
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(1, 1, 1, "abcd")
    t2 = Token(1, 3, 3, "efgh")
    t3 = Token(2, 3, 3, "efgh")
    t4 = Token(1, 1, 1, "abcd")
    assert t1 == t1
    assert t1 != t2
    assert t1 != t3
    assert t4 == t1
    assert t1 != "abcd"

# Generated at 2022-06-14 14:59:47.741089
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 1
    content = "token"
    value = {1:'one', 2:'two'}
    token = DictToken(value, start_index, end_index, content)
    assert isinstance(token, DictToken)
    assert token.string == 'token'
    assert token.value == {1:'one', 2:'two'}
    assert token.start == Position(1,1,0)
    assert token.end == Position(1,2,1)
    assert token.lookup([]) == token
    assert token.lookup_key([0]) == token._child_keys[1]


# Generated at 2022-06-14 14:59:59.873274
# Unit test for method __eq__ of class Token
def test_Token___eq__(): 
    # Token with class ScalarToken
    t1 = ScalarToken(True, 0, 0, "")
    t2 = ScalarToken(True, 0, 0, "")

    assert t1 == t2
    assert not t1 == False
    assert not t1 == None

    # Token with class DictToken
    t3 = DictToken({}, 0, 0, "")
    t4 = DictToken({}, 0, 0, "")
    assert t3 == t4
    assert not t3 == False
    assert not t3 == None

    # Token with class ListToken
    t5 = ListToken([], 0, 0, "")
    t6 = ListToken([], 0, 0, "")
    assert t5 == t6
    assert not t5 == False
    assert not t5 == None


# Generated at 2022-06-14 15:00:06.960854
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1, 1, 2, "abc").__eq__(Token(1, 1, 2, "aaa")) == True
    assert Token(1, 1, 2, "abc").__eq__(Token(1, 2, 3, "aaa")) == False
    assert Token(1, 1, 2, "abc").__eq__(Token("1", 1, 2, "aaa")) == False
    assert Token(1, 1, 2, "abc").__eq__("abc") == False

# Generated at 2022-06-14 15:00:11.461034
# Unit test for constructor of class DictToken
def test_DictToken():
    # Create a Token object for testing
    token = DictToken({'key1': 'Token1', 'key2': 'Token2'}, 99, 99, '')
    # Create a DictToken object for testing
    test_token = DictToken(
        {'key1': 'Token1', 'key2': 'Token2'}, 99, 99, ''
    )
    assert token._value is test_token._value
    assert token._start_index is test_token._start_index
    assert token._end_index is test_token._end_index
    assert token._content == test_token._content


# Generated at 2022-06-14 15:00:20.148274
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Given
    token1 = Token('abc', 1, 3)
    token2 = Token('abc', 1, 3)
    token3 = Token('abcd', 1, 3)
    token4 = Token(1, 1, 3)
    token5 = ScalarToken('abc', 1, 3)
    # When/Then
    assert token1 != token2
    assert token1 != token3
    assert token1 != token4
    assert token1 != token5

# Generated at 2022-06-14 15:00:25.468385
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({'a': 1}, 0, 1, content='abc')
    assert d._get_value() == {'a': 1}
    assert d._start_index == 0
    assert d._end_index == 1
    assert d._content == 'abc'
    assert d._child_keys == {'a': 'a'}
    assert d._child_tokens == {'a': 1}


# Generated at 2022-06-14 15:00:31.715703
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(None,0,0) == Token(None,0,0)
    assert not (Token(None,0,0) == Token(None,0,1))
    assert not (Token(None,0,0) == Token(None,1,0))
    assert not isinstance(Token(None,0,0) == 0, bool)

# Generated at 2022-06-14 15:00:40.765425
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({'a':1, 'b':2}, 0, 4, content = "")
    assert token.string == ""
    assert token.value == {'a': 1, 'b': 2}
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 1, 0)
    assert token.lookup([]) == token
    assert token.lookup_key([]) == token
    assert token.__repr__ == 'DictToken(None)'
    assert token.__eq__(token) == True
    assert token.__hash__() == -9223372036854775808
    assert token.child_keys == {'a': 1, 'b': 2}
    assert token.child_tokens == {'a': 1, 'b': 2}
   

# Generated at 2022-06-14 15:00:51.505942
# Unit test for constructor of class DictToken
def test_DictToken():
    # Arrange
    with pytest.raises(NotImplementedError):
        # Act
        DictToken()
        # Assert


# Generated at 2022-06-14 15:01:03.779693
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class A(Token):
        def __init__(self, value, start_index, end_index, content = ""):
            self._value = value
            self._start_index = start_index
            self._end_index = end_index
            self._content = content

    a = A(value=1, start_index=1, end_index=1)
    b = A(value=1, start_index=1, end_index=1)
    assert a == b
    class B(Token):
        def __init__(self, value, start_index, end_index, content = ""):
            self._value = value
            self._start_index = start_index
            self._end_index = end_index
            self._content = content

# Generated at 2022-06-14 15:01:05.400588
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({"a": 1, "b": 2})

# Generated at 2022-06-14 15:01:06.753598
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken("hello", "goodbye")
    b = DictToken("hello", "goodbye")
    return a == b

# Generated at 2022-06-14 15:01:12.381862
# Unit test for constructor of class DictToken
def test_DictToken():
    pos = Position(1, 1, 1)
    dict_token = DictToken(
        {
            ScalarToken("a", 1, 2, content="some content"): ScalarToken(
                1, 2, 3, content="some content"
            ),
            ScalarToken("b", 1, 2, content="some content"): ScalarToken(
                2, 2, 3, content="some content"
            ),
        },
        2, 3, "some content",
    )



# Generated at 2022-06-14 15:01:15.242399
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t = Token(None, None, None, content = "test_content")
    t2 = Token(None, None, None, content = "test_content")
    assert(t == t2)


# Generated at 2022-06-14 15:01:15.850381
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass

# Generated at 2022-06-14 15:01:16.913529
# Unit test for constructor of class DictToken
def test_DictToken():
    assert '__init__'


# Generated at 2022-06-14 15:01:17.866689
# Unit test for constructor of class DictToken
def test_DictToken():
    pass


# Generated at 2022-06-14 15:01:23.860107
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(value=3, start_index=1, end_index=2, content="") == Token(
        value=3, start_index=1, end_index=2, content=""
    )
    assert Token(value=3, start_index=1, end_index=2, content="") != Token(
        value=3, start_index=2, end_index=3, content=""
    )
    assert Token(value=3, start_index=1, end_index=2, content="") != Token(
        value=4, start_index=1, end_index=2, content=""
    )



# Generated at 2022-06-14 15:01:52.573089
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    """
    The method __eq__ of class Token always returns False if the other object is not a Token object.
    """
    assert Token(
        value=1, start_index=2, end_index=3, content="1234"
    ).__eq__(1) == False


# Generated at 2022-06-14 15:01:54.061608
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass



# Generated at 2022-06-14 15:02:06.183034
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class TokenSub(Token):
        def __init__(self, value: typing.Any, start_index: int, end_index: int, content: str = ""):
            super().__init__(value, start_index, end_index, content)

        def _get_value(self) -> typing.Any:
            return self._value

        def _get_child_token(self, key: typing.Any) -> Token:
            raise ValueError("Not implemented")

        def _get_key_token(self, key: typing.Any) -> Token:
            raise ValueError("Not implemented")

    t1 = TokenSub(1, 0, 10, "0123456789")
    t2 = TokenSub(1, 0, 10, "0123456789")

    assert t1 == t2
    assert not t1 != t

# Generated at 2022-06-14 15:02:12.245933
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert (ScalarToken(1, 0, 3) == ScalarToken(1, 0, 3))
    assert (not (ScalarToken(1, 0, 3) == list))
    assert (not (ScalarToken(1, 0, 3) == ScalarToken(2, 0, 3)))
    assert (not (ScalarToken(1, 1, 3) == ScalarToken(1, 0, 3)))
    assert (not (ScalarToken(1, 0, 4) == ScalarToken(1, 0, 3)))

# Generated at 2022-06-14 15:02:15.611603
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    my_token = Token(0, 0, 0)
    result = my_token == Token(0, 0, 0)
    assert isinstance(result, bool)


# Generated at 2022-06-14 15:02:18.611270
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token('a', 0, 1, content='abc')
    token1 = Token('a', 0, 1, content='abc')
    assert token.__eq__(token1)



# Generated at 2022-06-14 15:02:23.546299
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 1
    end_index = 2
    content = "test"
    value = ""
    token = Token(
        value=value, start_index=start_index, end_index=end_index, content=content
    )
    other_token = Token(
        value=value, start_index=start_index, end_index=end_index, content=content
    )
    assert token == other_token
    assert token != "other_token"



# Generated at 2022-06-14 15:02:33.347290
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # mock the methods _get_value() and _get_child_token(key)
    Token._get_value = lambda self: self._value
    Token._get_child_token = lambda self, key: self._value[key]

    # create the dict _value of instance t1
    v1 = {(1, 2): 'my-value1', (3, 4): 'my-value2'}
    t1 = Token(value=v1, start_index=0, end_index=1)

    # create another dict v2 whose values are different from the dict v1
    v2 = {(1, 2): 'Wrong-value1', (3, 4): 'Wrong-value2'}
    t2 = Token(value=v2, start_index=0, end_index=1)

    # create another dict v

# Generated at 2022-06-14 15:02:41.241952
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_tok = DictToken({1: 2}, start_index=10, end_index=15, content="Hello")
    assert dict_tok._value == {1: 2}
    assert dict_tok._start_index == 10
    assert dict_tok._end_index == 15
    assert dict_tok._content == "Hello"

if __name__ == "__main__":
    import pytest
    pytest.main(["-v", "-s", "test_token.py"])

# Generated at 2022-06-14 15:02:43.411338
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_ = Token("value", 1, 2)

    assert token_ == token_
    assert token_ != "abc"


# Generated at 2022-06-14 15:03:08.208542
# Unit test for constructor of class DictToken
def test_DictToken():
    obj = DictToken(
        {1: 1, 2: 2}, 0, 0, content="{1: 1, 2: 2}"
    )
    assert obj._value == {1: 1, 2: 2}
    assert obj._start_index == 0
    assert obj._end_index == 0
    assert obj._content == "{1: 1, 2: 2}"
    assert obj._child_keys == {1: 1, 2: 2}
    assert obj._child_tokens == {1: 1, 2: 2}


# Generated at 2022-06-14 15:03:12.254406
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({'a':1},1,2,'123')
    equal(token._child_keys, {'a': 123}, 'DictToken._child_keys')



# Generated at 2022-06-14 15:03:22.836790
# Unit test for constructor of class DictToken
def test_DictToken():
	t1 = ScalarToken("a", 2, 3, content="abc")
	t2 = ScalarToken("b", 4, 5, content="abcd")
	t3 = ScalarToken("c", 1, 2, content="abc")
	t4 = ScalarToken("d", 0, 1, content="abcd")
	t5 = ScalarToken("e", 5, 6, content="abcde")
	d = DictToken({t4: t1, t2: t3}, 0, 5, content="abcde")
	assert list(d._child_keys.keys()) == ["d", "b"]
	assert list(d._child_tokens.keys()) == ["d", "b"]
	


# Generated at 2022-06-14 15:03:28.376571
# Unit test for constructor of class DictToken
def test_DictToken():
    from tokens import DictToken
    from .tokens_test import ScalarToken
    # test for constructor of DictToken
    import json
    content = json.load(open("tokens_test.json", "r"))
    dict_token = DictToken({ScalarToken("hello", 0, 0): ScalarToken("hi", 0, 0)}, 0, 0, content = content)
    assert (dict_token._get_value() == {"hello": "hi"})
    assert(dict_token.start.line == 1)
    assert(dict_token.start.column == 2)
    assert(dict_token.end.line == 1)
    assert(dict_token.end.column == 8)
    assert(dict_token.string == '{"hello": "hi"}')

# Generated at 2022-06-14 15:03:32.947397
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {'a':1,'b':2}
    token = DictToken(value = d, start_index = 1, end_index = 2, content = "")
    index = 0
    assert(token._get_child_token(index) == token._value[index]._value)


# Generated at 2022-06-14 15:03:40.939891
# Unit test for constructor of class DictToken
def test_DictToken():
    # 1
    a = Position(1, 2, 3)
    b = Position(4, 5, 6)
    dict = {'a': 1, 'b': 2}
    token = DictToken(dict, 1, 2, "content")
    assert token._value == dict
    assert token._start_index == 1
    assert token._end_index == 2
    assert token._content == "content"
    assert token._child_keys == {'a': 'a', 'b': 'b'}
    assert token._child_tokens == {'a': 1, 'b': 2}
    # 2
    token2 = DictToken(dict, 1, 2, "")
    assert token2._content == ""
    # 3
    token3 = DictToken(dict, 1, 2, "abcd")
    assert token

# Generated at 2022-06-14 15:03:42.147224
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken is not None

# Generated at 2022-06-14 15:03:49.829684
# Unit test for constructor of class DictToken
def test_DictToken():
    to_dict = {'a':1, 'b':2}
    args = (to_dict, 1, 3, 'abc')
    token = DictToken(*args)
    assert token._value == {'a':1, 'b':2}
    assert token._start_index == 1
    assert token._end_index == 3
    assert token._content == 'abc'
# Initialize test parameters
to_dict = {'a':1, 'b':2}
args = (to_dict, 1, 3, 'abc')
token = DictToken(*args)


# Generated at 2022-06-14 15:03:54.683264
# Unit test for constructor of class DictToken
def test_DictToken():
    # TODO: Please change these test case strings
    assert DictToken({1:1}, 0, 1, content="{1:1}")
    assert DictToken({1:'a'}, 0, 2, content="{1:'a'}")
    assert DictToken({'a':'a', 'b':'b'}, 0, 5, content="{'a':'a', 'b':'b'}")


# Generated at 2022-06-14 15:03:58.681796
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(content = "", start_index = 0, end_index = 0, value = {})
    assert isinstance(d, Token)
    assert isinstance(d, DictToken)
    assert d.value == {}
    assert d.string == ""
    assert d.start == d.end
    assert d._get_value() == d.value


# Generated at 2022-06-14 15:04:21.679469
# Unit test for constructor of class DictToken
def test_DictToken():
    T = DictToken
    assert T.__init__ == (lambda self, *args: super().__init__(*args))

# Generated at 2022-06-14 15:04:24.195320
# Unit test for constructor of class DictToken
def test_DictToken():
    # test constructor of class DictToken
    # assert the constructor of class DictToken
    # function: __init__()
    assert ("_get_value" in dir(DictToken))


# Generated at 2022-06-14 15:04:25.081810
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken is not None


# Generated at 2022-06-14 15:04:27.883227
# Unit test for constructor of class DictToken
def test_DictToken():
    try:
        DictToken(1, 2, 3, 4)
    except TypeError:
        print('test_DictToken(): Passed')
    else:
        print('test_DictToken(): Failed')


# Generated at 2022-06-14 15:04:34.366781
# Unit test for constructor of class DictToken
def test_DictToken():
    # test init without start index
    with pytest.raises(TypeError):
        DictToken({},1,2)

    #test init without end index
    with pytest.raises(TypeError):
        DictToken({}, 1)

    #test init without value
    with pytest.raises(TypeError):
        DictToken(1,2)

    #test init with correct input
    #token = Token({},1,2)

# Generated at 2022-06-14 15:04:39.324504
# Unit test for constructor of class DictToken
def test_DictToken():
    test_value = {'a': 2, 'b': 4}
    test_start_index = 0
    test_end_index = 2
    test_content = '{"a": 2, "b": 4}'
    DictToken(test_value, test_start_index, test_end_index, test_content)


# Generated at 2022-06-14 15:04:43.180443
# Unit test for constructor of class DictToken
def test_DictToken():
    d_token = DictToken({1:2, 3:4}, 1, 2)
    assert d_token._value == {1:2, 3:4}
    assert d_token._start_index == 1
    assert d_token._end_index == 2


# Generated at 2022-06-14 15:04:50.290952
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 0
    value = {"a":1, "b": 2, "c":3}
    content = "abc"
    token = DictToken(value, start_index, end_index, content)
    assert token.string == "abc"
    assert token.value == {"a":1, "b": 2, "c":3}
    assert token.start.index == 0
    assert token.end.index == 0

    start_index = 1
    end_index = 1
    value = {"a":1, "b": 2, "c":3}
    content = "abc"
    token = DictToken(value, start_index, end_index, content)
    assert token.string == "bc"

# Generated at 2022-06-14 15:04:51.752265
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({"key": "value"})
    assert isinstance(dt, DictToken)


# Generated at 2022-06-14 15:04:55.082495
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken(
        {"a": "b"}, 0, 0, content="{'a': 'b'}"
    )
    assert dict_token._child_keys == {'a': {'a': 'b'}}

# Generated at 2022-06-14 15:05:41.677518
# Unit test for constructor of class DictToken
def test_DictToken():
    d={"a":1,"b":2}
    a=DictToken(d,1,3,"a\nb")
    assert(a._value==d)
    assert(a._start_index==1)
    assert(a._end_index==3)
    assert(a._content=="a\nb")

# Generated at 2022-06-14 15:05:42.328802
# Unit test for constructor of class DictToken
def test_DictToken():
    pass

# Generated at 2022-06-14 15:05:45.385954
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({"a": 1}, 0, 3, "{'a': 1}")
    assert(dt._child_tokens == {"a": 1})
    assert(dt._child_keys == {"a": 1})

# Generated at 2022-06-14 15:05:48.251907
# Unit test for constructor of class DictToken
def test_DictToken():
    from collections import OrderedDict

    dic = OrderedDict()
    dic['int'] = 3
    dic['str'] = 'teacher'

    tk = DictToken(dic)
    print(tk)


# Generated at 2022-06-14 15:05:49.568083
# Unit test for constructor of class DictToken
def test_DictToken():
    pass

# Generated at 2022-06-14 15:05:56.503545
# Unit test for constructor of class DictToken
def test_DictToken():
    # construct DictToken, then test _get_value(), it should return a dict
    a = DictToken({'a':1}, 0, 1)
    assert a._get_value() == {'a':1}

    # construct DictToken, then test _get_value(), it should return a dict
    a = DictToken({'a':1}, 0, 1)
    assert a._get_value() == {'a':1}

# Generated at 2022-06-14 15:06:04.797057
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 1
    end_index = 4
    content = "abcde"
    d1 = {'a': 'a'}
    d2 = {'b': 'b'}
    value = {d1: d2}
    try:
        dt1 = DictToken(value, start_index, end_index, content)
    except BaseException:
        assert False
    assert dt1._value == value
    assert dt1._start_index == start_index
    assert dt1._end_index == end_index
    assert dt1._content == content
    if __name__ == '__main__':
        print("Pass")


# Generated at 2022-06-14 15:06:08.098198
# Unit test for constructor of class DictToken
def test_DictToken():
    # Create a Dictionary
    a = {
        "name": "Alice",
        "age": 18
    }

    assert DictToken(None, None, None, a) != DictToken(None, None, None, a)

# Generated at 2022-06-14 15:06:12.963689
# Unit test for constructor of class DictToken
def test_DictToken():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    assert DictToken({a: b, c: d}, e, f)._value == {a: b, c: d}
    print("passed test_DictToken")
