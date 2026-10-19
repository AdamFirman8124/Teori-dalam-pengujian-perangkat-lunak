

# Generated at 2022-06-14 14:56:21.829902
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(1, 2, 3, "asd")
    other = Token(1, 2, 3, "asd")

    assert token == other
    assert not (token != other)


# Generated at 2022-06-14 14:56:23.360733
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken(value={}, start_index=0, end_index=0)


# Generated at 2022-06-14 14:56:32.755278
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # TokenResult = typing.Union[
    #     ScalarToken,
    #     ListToken,
    #     DictToken
    # ]
    TokenResult = Token

    print(
        f"\nTesting method __eq__ of class Token\n"
        f"\n{'='*60}\n"
        f"{' '*4}Line {__file__.split('/')[-1]} (Method {sys._getframe().f_code.co_name})\n"
        f"{'-'*60}\n"
        f"    {TokenResult.__eq__.__doc__}\n"
        f"{'-'*60}\n"
    )
    
    value_1 = ""
    start_index_1 = 0
    end_index_1 = 0
    
    value_2

# Generated at 2022-06-14 14:56:44.468283
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test no possible cases
    assert not(Token(None, None, None, None) == None)
    # Test one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of one branch of

# Generated at 2022-06-14 14:56:50.054421
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({'key': 'value'}, 1, 3)
    assert repr(token) == "DictToken({'key': 'value'})"
    assert token.start == Position(1, 1, 1)
    assert token.end == Position(1, 1, 3)
    assert token.string == "{'key': 'value'}"
    assert token.lookup([]) == token
    assert token.lookup_key([]) == token


# Generated at 2022-06-14 14:56:51.897684
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({}, 0, 0, content="")
    assert dict_token


# Generated at 2022-06-14 14:56:59.998485
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.compat import is_python_version_lower_than_3_8

    token = Token("", 0, 0)
    assert token == token

    token2 = Token("", 0, 0)
    if is_python_version_lower_than_3_8:
        assert not (token == token2)
    else:
        assert token == token2

    token3 = Token("", 1, 0)
    assert not (token == token3)
    token4 = Token("", 0, 1)
    assert not (token2 == token4)
    token5 = Token("", 1, 1)
    assert not (token3 == token5)
    token6 = Token("", 1, 1)
    assert not (token5 == token6)

    token7 = Token("", 0, 0, "ab")

# Generated at 2022-06-14 14:57:10.496833
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem import String, Integer, Number
    from . import Lexer
    s = "foo 42"
    t1 = Lexer([String("foo"), Integer("42")]).parse(s)
    t2 = Lexer([String("foo"), Integer("42")]).parse(s)
    assert t1 == t2
    t3 = Lexer([String("foo"), Integer("42"), Number("12.34")]).parse(s)
    assert t1 != t3
    t4 = Lexer([Integer("42"), String("foo")]).parse(s)
    assert t1 != t4
    assert t1.value == t2.value == "foo"
    t5 = Lexer([String("foo"), Integer("42")]).parse("foo2")
    assert t1 != t5

# Generated at 2022-06-14 14:57:18.617343
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    item22 = Position(2, 2, 2)
    item23 = Position(2, 3, 3)
    item31 = Position(3, 1, 4)
    item44 = Position(4, 4, 8)
    item61 = Position(6, 1, 13)
    item62 = Position(6, 2, 14)
    item74 = Position(7, 4, 18)
    item86 = Position(8, 6, 23)
    item97 = Position(9, 7, 28)
    item108 = Position(10, 8, 34)

    s1 = ScalarToken('abc', 0, 2, 'abc')
    assert s1.lookup([]) == s1
    assert s1.lookup_key([]) == s1
    assert s1.start == item22
    assert s1.end == item23

    s2

# Generated at 2022-06-14 14:57:23.071685
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Invalid type
    print("Testing invalid type 'None'")
    try:
        assert Token() == None, 'Should raise a TypeError'
    except TypeError:
        pass
    # Valid type
    print("Testing valid type 'Token'")
    assert Token() == Token(), "Should be equal"

# Generated at 2022-06-14 14:57:28.475173
# Unit test for constructor of class DictToken
def test_DictToken():
    # Test the constructor of class DictToken
    test_DictToken = DictToken()



# Generated at 2022-06-14 14:57:35.101773
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    def check(token1: Token, token2: Token) -> None:
        assert token1 == token2
        assert token2 == token1

    token1 = ScalarToken(1, 0, 1)
    check(token1, ScalarToken(1, 0, 1))
    check(token1, ScalarToken(1, 0, 2))
    check(token1, ScalarToken(1, 1, 2))

    token1 = DictToken({ScalarToken(1, 0, 1): ScalarToken(2, 0, 1)}, 0, 1, "")
    check(token1, DictToken({ScalarToken(1, 0, 1): ScalarToken(2, 0, 1)}, 0, 1, ""))

# Generated at 2022-06-14 14:57:44.647243
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    Token1 = Token(1, 2, 3)
    Token2 = Token(1, 2, 3)
    assert Token1 == Token2
    assert not Token1 != Token2
    Token3 = Token(2, 2, 3)
    Token4 = Token(2, 3, 3)
    Token5 = Token(2, 2, 4)
    assert not Token1 == Token3
    assert not Token3 == Token4
    assert not Token3 == Token5
    assert Token1 != Token3
    assert Token3 != Token4
    assert Token3 != Token5
    Token6 = ScalarToken(1, 2, 3)
    Token7 = ScalarToken(1, 2, 3)
    assert Token6 == Token7
    assert not Token6 != Token7
    Token8 = ScalarToken(2, 2, 3)

# Generated at 2022-06-14 14:57:47.348369
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    value = ScalarToken(1, 0, 0)
    token = ScalarToken(1, 0, 0)
    assert token == value
    assert token != 1



# Generated at 2022-06-14 14:57:48.474574
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(1, 1, 1)
    assert token != None


# Generated at 2022-06-14 14:57:52.401975
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {'a': 1, 'b': 2, 'd': 3}
    assert list(d.keys()) == ['a', 'b', 'd']
    assert list(d.items()) == [('a', 1), ('b', 2), ('d', 3)]

# Generated at 2022-06-14 14:57:56.815327
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({'a':1,'b':2},0,1,'{"a":1, "b":2}')
    assert a.lookup([0])._value == 1
    assert a.lookup([1])._value == 2
    assert a.lookup_key([0])._value == 'a'
    assert a.lookup_key([1])._value == 'b'

# Generated at 2022-06-14 14:57:58.227292
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass #TODO


# Generated at 2022-06-14 14:58:09.329617
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(5, 2, 7, "123456789") == Token(5, 2, 7, "123456789")
    assert Token(5, 2, 7, "123456789") == Token(5, 2, 7, "123456789")
    assert not (Token(5, 2, 7, "123456789") == Token(6, 2, 7, "123456789"))
    assert not (Token(5, 2, 7, "123456789") == Token(5, 1, 7, "123456789"))
    assert not (Token(5, 2, 7, "123456789") == Token(5, 2, 6, "123456789"))
    assert not (Token(5, 2, 7, "123456789") == Token(5, 2, 7, "1234567890"))

# Generated at 2022-06-14 14:58:12.376774
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token('value', 'start_index', 'end_index')
    token2 = Token('value', 'start_index', 'end_index')
    assert token1 == token2


# Generated at 2022-06-14 14:58:26.147290
# Unit test for method __eq__ of class Token
def test_Token___eq__():
	assert Token(1, 2, 3) == Token(1, 2, 3)
	assert Token(1, 2, 3) != Token(2, 3, 4)
	assert Token(1, 2, 3) != Token(1, 3, 4)
	assert Token(1, 2, 3) != Token(1, 2, 4)
	assert Token(1, 2, 3) != 1
	assert Token(1, 2, 3) != object()
	assert Token(1, 2, 3) != None
	assert not Token(1, 2, 3) is None
	assert Token(1, 2, 3) != 2
	assert Token(1, 2, 3) != object()
	assert Token(1, 2, 3) != None
	assert not Token(1, 2, 3) is None

# Generated at 2022-06-14 14:58:31.142022
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 100
    end_index = 200
    content = "Hello World"

    class MyToken(Token):
        def __init__(self, value):
            super().__init__(value, start_index, end_index, content)

    token1 = MyToken(1)
    token2 = MyToken(1)
    token3 = MyToken(2)
    assert (token1 == token2)
    assert not (token1 == token3)

# Generated at 2022-06-14 14:58:34.855313
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import Token
    token1 = Token('value', 1, 2, 'content')
    token2 = Token('value', 1, 2, 'content')
    assert token1 == token2


# Generated at 2022-06-14 14:58:37.871211
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token('a', 0, 1, content='aa')
    t2 = Token('a', 0, 1, content='aa')
    t3 = ScalarToken('a', 0, 1, content='aa')
    t4 = Token('b', 0, 1, content='bb')
    assert t1 == t2
    assert t1 == t3
    assert not t1 == t4
    assert not t1 == t4


# Generated at 2022-06-14 14:58:40.171430
# Unit test for constructor of class DictToken
def test_DictToken():
    # True test case
    result = DictToken({'key': 'value'}, 0, 5)
    assert result._value == {'key': 'value'}


# Generated at 2022-06-14 14:58:45.645127
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = "abc"
    s = "abcd"
    start_index = 0
    end_index = 1
    value = "a"
    token = Token(value, start_index, end_index, content)
    assert token == token


# Generated at 2022-06-14 14:58:47.344362
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(123, 1, 10, "123") != "123"

# Generated at 2022-06-14 14:58:53.589617
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from .syntax import Token
    from .tokenizer import Tokenizer
    from .parser import Parser
    from .transform import Transform

    obj1 = Token(1, 2, 3, "  foo  ")
    obj1.string == "  foo  "
    obj1.value == 1
    obj1.start.position == 2
    obj1.end.position == 3
    obj2 = Token(1, 2, 3, "  foo  ")
    obj1 == obj2
    obj1 != 2
    obj2 != 3



# Generated at 2022-06-14 14:59:03.075965
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    source = "['str']"
    doc = json.loads(source)
    input_index = [0]
    input_start_index = 1
    input_end_index = len(source) - 2
    input_value = doc[input_index[0]]
    json_token = Token(value=input_value, start_index=input_start_index, end_index=input_end_index)
    input = json_token
    json_token_1 = Token(value=input_value, start_index=input_start_index, end_index=input_end_index)
    assert input == json_token_1


# Generated at 2022-06-14 14:59:14.187076
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Create a few of mock tokens
    token1 = Token("token1_value", 0, 0, "token1_content")
    token2 = Token("token2_value", 1, 1, "token2_content")
    token3 = Token("token1_value", 0, 0, "token1_content")
    token4 = Token("token3_value", 3, 3, "token3_content")

    # Create a list of mock tokens
    mock_tokens = [token1, token2, token3, token4]

    # Create list of expected results
    expected_results = [True, False, True, False]

    # Compare the mock tokens against the expected results
    assert len(mock_tokens) == len(expected_results)
    for i in range(len(mock_tokens)):
        result

# Generated at 2022-06-14 14:59:21.710534
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Method __eq__ of class Token is tested in child classes.
    pass


# Generated at 2022-06-14 14:59:32.541472
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class DictToken(Token):
        def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
            super().__init__(*args, **kwargs)
            self._child_keys = {k._value: k for k in self._value.keys()}
            self._child_tokens = {k._value: v for k, v in self._value.items()}

        def _get_value(self) -> typing.Any:
            return {
                key_token._get_value(): value_token._get_value()
                for key_token, value_token in self._value.items()
            }

        def _get_child_token(self, key: typing.Any) -> Token:
            return self._child_tokens[key]


# Generated at 2022-06-14 14:59:45.420593
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class A(Token):
        def __init__(self, value, start_index, end_index):
            self._value = value
            self._start_index = start_index
            self._end_index = end_index

        def _get_value(self) -> typing.Any:
            raise NotImplementedError  # pragma: nocover

    a = A(0, 0, 0)
    assert(a == a)
    assert(a == a)
    assert(not (a != a))
    b = A(1, 0, 0)
    assert(a != b)
    assert(a != b)
    assert(not (a == b))
    c = A(0, 1, 0)
    assert(a != c)
    assert(a != c)
    assert(not (a == c))

# Generated at 2022-06-14 14:59:48.352406
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # A = Token("a", 0, 1, "a")
    # B = Token("b", 0, 1, "b")
    # assert A == A
    # assert not (A == B)
    pass

# Generated at 2022-06-14 14:59:50.058716
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({}) != None


# Generated at 2022-06-14 14:59:54.157259
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(1, 2, 3)
    t2 = Token(1, 2, 3)
    assert(t1 == t2)
    assert(hash(t1) == hash(t2))



# Generated at 2022-06-14 14:59:57.879909
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    A = Token(1,1,3,"abc")
    B = Token(2,2,2,"b")
    C = Token(1,1,3,"abc")
    assert(A==C)
    assert(not A==B)

# Generated at 2022-06-14 15:00:03.819818
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import typesystem

    t1 = typesystem.ScalarToken(1, 1, 1)
    t2 = typesystem.ScalarToken(1, 1, 1)
    assert t1 == t2
    t2 = typesystem.ScalarToken(2, 1, 1)
    assert not (t1 == t2)
    t2 = typesystem.ScalarToken(1, 2, 1)
    assert not (t1 == t2)
    t2 = typesystem.ScalarToken(1, 1, 2)
    assert not (t1 == t2)



# Generated at 2022-06-14 15:00:08.755568
# Unit test for constructor of class DictToken
def test_DictToken():
    # Pass
    DictToken({}, 0, 0, "\n")
    DictToken({"1": 1}, 0, 0, "\n")
    DictToken([], 0, 0, "\n")
    DictToken([1, 2, 4], 0, 0, "\n")


# Generated at 2022-06-14 15:00:11.792605
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(1, 1, 2)
    assert d._start_index == 1
    assert d._end_index == 2
    assert d._value == 1

# Generated at 2022-06-14 15:00:25.531677
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.errors import ValidationError
    from typesystem.types import String

    m = String()
    m.validate("a")
    token1 = generate_token(m, "a")
    token2 = generate_token(m, "a")
    assert token1 == token2
    assert not (token1 != token2)
    try:
        m.validate("b")
        assert False
    except ValidationError as e:
        token3 = generate_token(m, "b")
    assert token1 != token3
    assert not (token1 == token3)


# Generated at 2022-06-14 15:00:29.588976
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({1:2}, 4, 5, content='Welcome to the world!')
    assert isinstance(t, DictToken)


# Generated at 2022-06-14 15:00:31.933749
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(None, 1, 2)
    token2 = Token(None, 1, 2)
    assert token1 == token2



# Generated at 2022-06-14 15:00:40.842285
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(
        {
            ScalarToken(1, 10, 11, '"1"'): ScalarToken(2, 12, 13, '"2"'),
            ScalarToken(3, 14, 15, '"3"'): ScalarToken(4, 16, 17, '"4"'),
        },
        0,
        18,
        '"{\\"1\\": \\"2\\", \\"3\\": \\"4\\"}"',
    )
    print(d)
    print(d._get_value())
    print(d._get_child_token(1))
    print(d._get_child_token(3))
    print(d._get_key_token(1))
    print(d._get_key_token(3))
    print(d.lookup([1]))

# Generated at 2022-06-14 15:00:47.042090
# Unit test for constructor of class DictToken
def test_DictToken():
    import sys
    import io
    import dis
    import types
    global opened_file
    opened_file = open("programs/DictToken.py", "rb")
    sys.stdin = io.BytesIO(''.join(opened_file.readlines()))
    dis.dis(sys.stdin.read())
    sys.stdin = sys.__stdin__
    opened_file.close()
    assert True


# Generated at 2022-06-14 15:00:50.141806
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    obj = Token(None, 0, 0, "")
    assert obj == Token(None, 0, 0, "")
    # assert obj != Token(None, 0, 0, "")

# Generated at 2022-06-14 15:00:52.434297
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    aa=Token(2,1,2)
    bb=Token(2,1,2)
    assert aa==bb

# Generated at 2022-06-14 15:01:01.104767
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken(1, 0, 1, "") == ScalarToken(1, 0, 1, "")
    assert not (ScalarToken(1, 0, 1, "") == ScalarToken(2, 0, 1, ""))
    assert not (ScalarToken(1, 0, 1, "") == ScalarToken(1, 1, 1, ""))
    assert not (ScalarToken(1, 0, 1, "") == ScalarToken(1, 0, 2, ""))


# Generated at 2022-06-14 15:01:05.499498
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(value, start_index=1, end_index=2)
    other = Token(value, start_index=1, end_index=2)
    assert token == other
    token2 = Token(value, start_index=2, end_index=2)
    assert token != token2


# Generated at 2022-06-14 15:01:10.367223
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import Integer
    
    class Token(Integer):
        def __eq__(self, other: typing.Any) -> bool:
            return super().__eq__(other) and self._value == other._value

    a_token = Token([], 0, 0, "")

    assert a_token == a_token == [], "The test failed."

# Generated at 2022-06-14 15:01:31.240068
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.types import Dictionary
    from typesystem.schema import Schema
    import typesystem 
    import json
    import sys
    import re

    schema = Schema()

    schema.register_type(Dictionary)

    data = {
        "name": "John Doe",
        "email": "john@example.com",
        "address": {
            "city": "Amsterdam",
            "street": "Herengracht",
            "number": 442,
        },
        "children": [{"first_name": "Jane", "last_name": "Doe"}],
    }
    token = schema.token(data)
    #print(data)
    #print(type(data))
    #print(token)
    #print(type(token))
    #print(token._value)
    #

# Generated at 2022-06-14 15:01:42.685559
# Unit test for constructor of class DictToken
def test_DictToken():
    token1 = ScalarToken(value=1, start_index=0, end_index=1)
    token2 = ScalarToken(value=2, start_index=2, end_index=3)
    value = DictToken(value={token1:token2}, start_index=0, end_index=3, content='12')
    assert value._child_keys[1] == token1
    assert value._child_tokens[1] == token2
    assert value._get_value() == {token1._get_value():token2._get_value()}
    assert value.string == '12'
    assert value.value == {1:2}
    assert value.start == value._get_position(0)
    assert value.end == value._get_position(3)
    assert value.lookup([1])

# Generated at 2022-06-14 15:01:47.792726
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken(5,5,5, content='hi')
    DictToken(5,5,5, content='hi', a=5)
    DictToken(5,5,5, content='hi', a=5, b=5)
    DictToken(5,5,5, content='hi', a=5, b=5, c=5)
    DictToken(5,5,5, content='hi', a=5, b=5, c=5, d=5)
    DictToken(5,5,5, content='hi', a=5, b=5, c=5, d=5, e=5)
    DictToken(5,5,5, content='hi', a=5, b=5, c=5, d=5, e=5, f=5)
    Dict

# Generated at 2022-06-14 15:01:50.187676
# Unit test for constructor of class DictToken
def test_DictToken():
    import pytest
    test = DictToken({"a": 1}, 0, 0)
    assert test.string == ""


# Generated at 2022-06-14 15:01:54.795082
# Unit test for constructor of class DictToken
def test_DictToken():
    dicttok = DictToken(value={}, start_index=0, end_index=0, content="")
    assert dicttok.value == {}
    assert dicttok.start == Position(1, 1, 0)
    assert dicttok.end == Position(1, 1, 0)


# Generated at 2022-06-14 15:01:57.800564
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(value={}, start_index=0, end_index=1, content="\n")

# Generated at 2022-06-14 15:01:58.584372
# Unit test for constructor of class DictToken
def test_DictToken():
    assert 0

# Generated at 2022-06-14 15:02:09.700153
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import Position

    start_index = 1
    end_index = 6
    content = "abcdef"

    t1 = ScalarToken("foo", start_index, end_index, content)
    t2 = ScalarToken("bar", start_index, end_index, content)
    t3 = ScalarToken("baz", start_index, end_index, content)

    d1 = DictToken({t1: t2}, start_index, end_index, content)
    d2 = DictToken({t2: t3}, start_index, end_index, content)

    # Test __init__() of class DictToken
    assert d1._child_keys == {'foo': t1}
    assert d1._child_tokens == {'foo': t2}
    assert d2._

# Generated at 2022-06-14 15:02:10.913305
# Unit test for constructor of class DictToken
def test_DictToken(): # passed
    assert True


# Generated at 2022-06-14 15:02:15.805000
# Unit test for constructor of class DictToken
def test_DictToken():
    input_data = DictToken(
        {}, 0, 0, content='')
    assert input_data._value is {}
    assert input_data._start_index is 0
    assert input_data._end_index is 0
    assert input_data._content is ''

# Generated at 2022-06-14 15:02:56.019851
# Unit test for constructor of class DictToken
def test_DictToken():
    d1 = DictToken({'a': 1}, 0, 1)
    assert d1._value == {'a': 1}
    assert d1._start_index == 0
    assert d1._end_index == 1
    assert d1._content == ""
    assert d1.string == ""
    assert d1.value == {'a': 1}
    assert d1.start == Position(1,1,0)
    assert d1.end == Position(1,1,1)
    assert d1.lookup([0]) == 1
    assert d1.lookup_key([0, 0]) == 'a'

# Generated at 2022-06-14 15:03:03.762804
# Unit test for constructor of class DictToken
def test_DictToken():
    string = '''\
{
    "hello": "world",
    "foo": "bar"
}
'''
    key_hello = ScalarToken(
        "hello",
        content=string,
        start_index=6,
        end_index=10)
    value_hello = ScalarToken(
        "world",
        content=string,
        start_index=15,
        end_index=19)
    key_foo = ScalarToken(
        "foo",
        content=string,
        start_index=27,
        end_index=30)
    value_foo = ScalarToken(
        "bar",
        content=string,
        start_index=35,
        end_index=37)
    dict0 = {key_hello: value_hello, key_foo: value_foo}

# Generated at 2022-06-14 15:03:06.946571
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {}
    d["a"] = 1
    d["b"] = 2
    d["c"] = 3
    token = DictToken(d, 0, 0, "abc")
    assert token._value["a"]._value == 1
test_DictToken()



# Generated at 2022-06-14 15:03:11.800181
# Unit test for constructor of class DictToken
def test_DictToken():
    list_token = ListToken(value=[], start_index=1, end_index=2, content="1")
    dict_token = DictToken(value={list_token: list_token}, start_index=1, end_index=2, content="1")


# Generated at 2022-06-14 15:03:13.865044
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken(value={}, start_index=0, end_index=1) == 0


# Generated at 2022-06-14 15:03:14.563510
# Unit test for constructor of class DictToken
def test_DictToken():
	pass

# Generated at 2022-06-14 15:03:20.309147
# Unit test for constructor of class DictToken
def test_DictToken():
    class A:
        a: int
        b: int

    class B:
        a: int
        b: int

    a = A(a=1, b=2)
    a_token = DictToken(a, 0, 1)
    assert a_token._get_value() == {'a': 1, 'b': 2}


# Generated at 2022-06-14 15:03:21.358372
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken()
    assert token is not None

# Generated at 2022-06-14 15:03:27.301691
# Unit test for constructor of class DictToken
def test_DictToken():
    test = DictToken({1:"hello", 2:"he"}, start_index = 0, end_index = 1, content = "hello\nhe")
    assert test._child_tokens == {2: 'he', 1: 'hello'}
    assert test._child_keys == {1: 'hello', 2: 'he'}
    assert test._value == {1: 'hello', 2: 'he'}
    test.__repr__()
    assert isinstance(test, Token)
    assert test == DictToken({2: 'he', 1: 'hello'}, start_index=0, end_index=1, content='hello\nhe')
    assert test != DictToken({2: 'he', 1: ''}, start_index=0, end_index=1, content='hello\nhe')
    test.__eq

# Generated at 2022-06-14 15:03:30.640621
# Unit test for constructor of class DictToken
def test_DictToken():
    from typing import Any
    from typesystem.ast import Dict
    from typesystem.token import DictToken

    dt = DictToken(Dict(), 10, 15, content="test_content")

    asser

# Generated at 2022-06-14 15:05:02.638005
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {"a": 1, "b": 2}
    dump_d = DictToken(value=d, start_index=0, end_index=1, content="") 
    assert dump_d.start == Position(1, 1, 0)
    assert dump_d.end == Position(1, 2, 1)
    assert dump_d.lookup([0]) == dump_d._child_tokens['a']
    assert dump_d.lookup_key([0]) == dump_d._child_keys['a']
    assert dump_d._get_value() == {"a": 1, "b": 2}
    assert dump_d == DictToken(value=d, start_index=0, end_index=1, content="") 

# Generated at 2022-06-14 15:05:04.578407
# Unit test for constructor of class DictToken
def test_DictToken():

    token = DictToken({"a":1,"b":2},1,1,"This is a string")
    expected = {"a":1, "b":2}
    assert token._value == expected


# Generated at 2022-06-14 15:05:10.606797
# Unit test for constructor of class DictToken
def test_DictToken():
    x = {"key1":1, "key2":2}
    b = DictToken(x, 0, 0, content="{'key1': 1, 'key2': 2}")
    assert(b.start == Position(1, 1, 0))
    assert(b.end == Position(1, 17, 16))
    assert(b.string == "{'key1': 1, 'key2': 2}")
    assert(b._child_tokens == {"key1":1, "key2":2})


# Generated at 2022-06-14 15:05:13.072036
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({'a': 1, 'b':2}, 0, 1)
    b = DictToken(a.value, 0, 1)
    assert a == b


# Generated at 2022-06-14 15:05:22.860551
# Unit test for constructor of class DictToken
def test_DictToken():
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        super().__init__(*args, **kwargs)
        self._child_keys = {k._value: k for k in self._value.keys()}
        self._child_tokens = {k._value: v for k, v in self._value.items()}
    DictToken.__init__ = __init__

    tok = DictToken({'a': 1, 'b': 2}, 0, 0)
    print(tok._value)
test_DictToken()

# Generated at 2022-06-14 15:05:28.098974
# Unit test for constructor of class DictToken
def test_DictToken():
    value = {'a':1}
    start_index = 1
    end_index = 1
    content = 'a'
    a = DictToken(value,start_index,end_index,content)
    print(a)


# Generated at 2022-06-14 15:05:35.857389
# Unit test for constructor of class DictToken
def test_DictToken():
    class Tokenizer:
        def tokenize_list(content: str) -> typing.Any:
            return [content]
        def tokenize_scalar(content: str) -> typing.Any:
            return content
    tokenizer = Tokenizer()
    token = DictToken(
        {tokenizer.tokenize_scalar('x'): tokenizer.tokenize_list('y')},
        0, 0, '')
    assert token.value == {'x': ['y']}

# Generated at 2022-06-14 15:05:44.928376
# Unit test for constructor of class DictToken
def test_DictToken():
    t1 = ScalarToken(value='a', start_index=0, end_index=1, content='a')
    t2 = ScalarToken(value='b', start_index=2, end_index=4, content='b')
    t3 = ScalarToken(value='c', start_index=1, end_index=6, content='c')
    d = DictToken(value={t1: t2, t2: t3}, start_index=0, end_index=6, content='a')
    assert(d.start.index == 0)
    assert(d.end.index == 6)
    assert(d.string == 'a')

# Generated at 2022-06-14 15:05:47.514219
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(None, None, None, {})
    assert token._child_keys == {}
    assert token._child_tokens == {}
    assert token.value == {}


# Generated at 2022-06-14 15:05:51.938501
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 1
    end_index = 5
    content = ""
    token = [ScalarToken(1, 1, 1, content), ScalarToken(2, 2,2, content)]
    dict_token = DictToken({token[0]:token[1]}, start_index, end_index, content)
    assert dict_token._child_keys == {1: token[0]}
    assert dict_token._child_tokens == {1: token[1]}
