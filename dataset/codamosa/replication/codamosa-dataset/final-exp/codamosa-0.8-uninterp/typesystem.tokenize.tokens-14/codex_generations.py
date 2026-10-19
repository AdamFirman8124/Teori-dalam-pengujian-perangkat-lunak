

# Generated at 2022-06-14 14:56:24.178885
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Setup
    value = 3
    start_index = 2
    end_index = 5
    content = "test"
    token = Token(value, start_index, end_index, content)

    # Exercise
    eq_result = token._get_value() == value and token._start_index == start_index and token._end_index == end_index
    result = token.__eq__(eq_result)

    # Verify
    assert result


# Generated at 2022-06-14 14:56:32.133063
# Unit test for constructor of class DictToken
def test_DictToken():
    d = { "skills": "c++", "class": "csci-1100" }
    d1 = DictToken(d,0,7,"skills = c++\nclass = csci-1100")
    # test the length of constructed DictToken
    assert len(d1._value) == 2
    # test the index of the keys
    assert d1._child_keys["skills"]._start_index == 0
    assert d1._child_keys["skills"]._end_index == 6
    assert d1._child_keys["class"]._start_index == 9
    assert d1._child_keys["class"]._end_index == 17
    # test the keys

# Generated at 2022-06-14 14:56:43.670302
# Unit test for constructor of class DictToken
def test_DictToken():
    a = {"startIndex": 0, "endIndex": 1, "value": "a"}
    b = {"startIndex": 2, "endIndex": 3, "value": "b"}
    c = {"startIndex": 4, "endIndex": 5, "value": "c"}
    d = {"startIndex": 6, "endIndex": 7, "value": "d"}
    v = {a["value"]: b, c["value"]: d}
    t = DictToken(v, 0, 7, "abcdefg")
    assert t._child_keys == {a["value"]: a, c["value"]: c}
    assert t._child_tokens == {a["value"]: b, c["value"]: d}
    assert t.string == "abcdefg"

# Generated at 2022-06-14 14:56:50.136767
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert (ScalarToken("value", 0, 1, None) == ScalarToken("value", 0, 1, None)) is True
    assert (ScalarToken("value", 0, 1, None) == ScalarToken("value2", 0, 1, None)) is False
    assert (ScalarToken("value", 0, 1, None) == ScalarToken("value", 0, 2, None)) is False
    assert (ScalarToken("value", 0, 1, None) == ScalarToken("value", 1, 1, None)) is False

# Generated at 2022-06-14 14:56:58.786999
# Unit test for constructor of class DictToken
def test_DictToken():
    dt1 = DictToken({}, 0, 0, content="")
    assert dt1._child_keys == {}
    assert dt1._child_tokens == {}
    assert dt1._content == ""
    assert dt1.end == Position(1, 1, 0)
    assert dt1.lookup([]) == dt1
    assert dt1.lookup_key([0]) == None
    assert dt1.start == Position(1, 1, 0)
    assert dt1.string == ""
    assert dt1.value == {}


# Generated at 2022-06-14 14:57:06.350825
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = "a-string-literal"
    t = ScalarToken("a-string-literal", 0, len(content) - 1, content)
    t2 = ScalarToken("a-string-literal", 0, len(content) - 1, content)
    t3 = ScalarToken("a-string-literal2", 0, len(content) - 1, content)
    assert t.value == t2.value
    assert t.value != t3.value
    assert t == t2
    assert not (t == t3)


# Generated at 2022-06-14 14:57:08.719767
# Unit test for constructor of class DictToken
def test_DictToken():
    test = DictToken("test_value", 0, 10, "test_context")
    #print(test.value)



# Generated at 2022-06-14 14:57:12.628870
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(1, 0, 10, content="foo=bar,baz=bar")
    assert token.__repr__() == "DictToken(\"foo=bar,baz=bar\")"
    assert token.__eq__(2) is False

test_DictToken()


# Generated at 2022-06-14 14:57:19.119096
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1,2,3) == Token(1,2,3)
    assert not Token(1,2,3) == Token(1,2,4)
    assert not Token(1,2,3) == Token(1,3,3)
    assert not Token(1,2,3) == Token(2,2,3)
    assert not Token(1,2,3) == "hello"

# Generated at 2022-06-14 14:57:19.748416
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass

# Generated at 2022-06-14 14:57:28.021677
# Unit test for constructor of class DictToken
def test_DictToken():
    test_dict = {
        0: 3,
        1: 5,
        2: 7,
    }
    dict_token = DictToken(test_dict, 0, 3, "test")
    assert dict_token.value == test_dict


# Generated at 2022-06-14 14:57:33.644878
# Unit test for constructor of class DictToken
def test_DictToken():
  dt = DictToken({'a':'b', 'c':'d'}, 0, 3, 'abc')
  assert dt.start == Position(1, 1, 0)
  assert dt.end == Position(1, 4, 3)
  assert dt.string == 'abc'
  assert dt.value == {'a':'b', 'c':'d'}
  assert dt.lookup([1]) == {'c':'d'}
  assert dt.lookup_key([1]) == 'c'
  assert dt.__eq__(dt)


# Generated at 2022-06-14 14:57:38.364188
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({}, 0, 0)
    t1 = DictToken({1: 1}, 0, 0)
    assert t.__hash__() == t.__hash__()
    assert t1.__hash__() == t1.__hash__()
    assert t.__eq__(t1) == False

# Generated at 2022-06-14 14:57:47.033405
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken("{}", 0, 1) == DictToken("{}", 0, 1)
    #assert DictToken("{}", 0, 1) == DictToken("{}", 0, 2)
    #assert DictToken("{}", 0, 1) == DictToken("{", 0, 1)
    assert DictToken("{}", 0, 1) != None
    assert DictToken("{}", 0, 1) != 4
    assert DictToken("{}", 0, 1) != Token("{}", 0, 1)
    assert DictToken("{}", 0, 1) != ScalarToken("{}", 0, 1)

# Generated at 2022-06-14 14:57:50.763680
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken(0,1,2,3)
    assert dt._value == 0
    assert dt._start_index == 1
    assert dt._end_index == 2
    assert dt._content == 3

# Generated at 2022-06-14 14:57:55.290540
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(
            {1:2, 3:4},
            start_index=0,
            end_index=100,
            content=""
        )
    assert token._value == {1: 2, 3: 4}
    assert token._start_index == 0
    assert token._end_index == 100
    assert token._content == ""


# Generated at 2022-06-14 14:58:06.985688
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import String
    from typesystem.base import Number

    # Arrange
    start_index = 0 
    end_index = 33
    content = '{ "name": "Max Meyers", "test": 39 }'

    value = {String(position=(1,1), name='name', required=False, default=None): ScalarToken(value='Max Meyers', start_index=9, end_index=20), String(position=(1,1), name='test', required=False, default=None): ScalarToken(value=39, start_index=27, end_index=29)}

    dtk = DictToken(value, start_index, end_index, content)

    # Act
    # Assert
    assert dtk._get_value() == value

# Generated at 2022-06-14 14:58:17.509984
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import String

    c = String(required=True)
    d = String(required=True)

    d1 = DictToken(
        {c: ScalarToken("asd", 1, 3, content="a"), d: ScalarToken("qwe", 5, 6, content="q")}, 0, 6, content="a q")
    d2 = DictToken(
        {c: ScalarToken("sdf", 1, 3, content="s"), d: ScalarToken("rty", 5, 6, content="r")}, 0, 6, content="s r")

    assert d1 != d2
    assert d1._get_value() == {c: "asd", d: "qwe"}
    assert d2._get_value() == {c: "sdf", d: "rty"}

# Generated at 2022-06-14 14:58:22.378737
# Unit test for constructor of class DictToken
def test_DictToken():
    dictionary = {
        int(1): int(2),
        int(2): int(3),
    }
    token = DictToken(dictionary, 0, 8, "")
    assert token.value == {1: 2, 2: 3}
    assert token.start.index == 0
    assert token.end.index == 8


# Generated at 2022-06-14 14:58:28.646867
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(
        {
            ScalarToken(1, 1, 4): ScalarToken(True, 5, 9),
            ScalarToken(2, 10, 13): ScalarToken(2, 14, 15),
            ScalarToken(3, 16, 19): ScalarToken(1, 20, 22),
        },
        1,
        22,
        "1:true 2:2 3:1 ",
    )
    assert token._get_value() == {1: True, 2: 2, 3: 1}
    assert token._get_position(22) == Position(1, 23, 22)


# Generated at 2022-06-14 14:58:43.533603
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken(
        {},
        0,
        0,
        "start_index = 0; end_index = 0; content = ''",
    )
    assert dict_token.string == "start_index = 0; end_index = 0; content = ''"
    assert dict_token.value is dict_token._get_value()
    assert dict_token.start is dict_token.start
    assert dict_token.end is dict_token.end
    assert dict_token.lookup([]) is dict_token.lookup([])
    assert dict_token.lookup_key([]) is dict_token.lookup_key([])
    assert dict_token._get_position(0) == dict_token._get_position(0)

# Generated at 2022-06-14 14:58:44.894080
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken


# Generated at 2022-06-14 14:58:52.361055
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 10
    end_index = 13
    content = "hello"
    dicttoken = DictToken({}, start_index, end_index, content)
    print(dicttoken)
    print(dicttoken.value)
    print(dicttoken.start)
    print(dicttoken.end)
    print(dicttoken.string)
    print(dicttoken.lookup([]))
    print(dicttoken.lookup_key([2]))

if __name__ == "__main__":
    test_DictToken()

# Generated at 2022-06-14 14:59:02.326488
# Unit test for constructor of class DictToken
def test_DictToken():
    test_value = {
        "name": "hello",
        "is_cool": True,
        "favourite_number": 10
    }
    test_start_index = 0
    test_end_index = 10
    test_content = ""
    test_dict_token = DictToken(test_value, test_start_index, test_end_index, test_content)
    assert test_dict_token._value == test_value
    assert test_dict_token._start_index == test_start_index
    assert test_dict_token._end_index == test_end_index
    assert test_dict_token._content == test_content


# Generated at 2022-06-14 14:59:08.719226
# Unit test for constructor of class DictToken
def test_DictToken():
    """
    Given a DictToken instance, test the constructor of class DictToken.
    """
    d = {'a': 1, 'b': 2}
    # result = DictToken(d, 0, 1, 'x')
    # assert result._child_tokens['a'] == 1
    # assert result._child_tokens['b'] == 2


# Generated at 2022-06-14 14:59:10.720555
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken("token value", 1, 4)
    assert d._value == "token value"


# Generated at 2022-06-14 14:59:13.844022
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({"a": "b"}, 1,4, content = "")
    assert token._get_value() == {"a": "b"}
    assert token.string == ""



# Generated at 2022-06-14 14:59:16.039066
# Unit test for constructor of class DictToken
def test_DictToken():
    a＿ = {'a': 'a'}
    assert a＿ == {'a': 'a'}


# Generated at 2022-06-14 14:59:24.713802
# Unit test for constructor of class DictToken
def test_DictToken():
    # create a token with a dictionary
    some_dict = {"key1": 1, "key2": 2}
    token = DictToken(value = some_dict, start_index = 10, end_index = 20, content = "some content")
    # test if the value has been set correctly
    result = token._get_value()
    answer = {"key1": 1, "key2": 2}
    print(result)
    assert result == answer
    # test if the start index has been set correctly
    result = token._start_index
    answer = 10
    print(result)
    assert result == answer
    # test if the end index has been set correctly
    result = token._end_index
    answer = 20
    print(result)
    assert result == answer
    # test if the content has been set correctly
    result = token

# Generated at 2022-06-14 14:59:26.773774
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({}, 0, 0, content='content')
    assert isinstance(token, Token)

# Generated at 2022-06-14 14:59:43.060077
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {}
    k = d["A"] = 1
    v = d["B"] = 2
    dt = DictToken(d, 1, 2, content="123")



# Generated at 2022-06-14 14:59:47.732937
# Unit test for constructor of class DictToken
def test_DictToken():
    d=DictToken({"a":1},0,10, "abcdabcdab")
    assert d._value == {"a":1}
    assert d._start_index == 0
    assert d._end_index == 10
    assert d._content == "abcdabcdab"


# Generated at 2022-06-14 14:59:59.872038
# Unit test for constructor of class DictToken
def test_DictToken():
    from typing import Any, Dict, List, Tuple
    from typesystem.base import Token, DictToken
    import typesystem.parser as parser
    
    # initialize parser
    p = parser.Parser()

    # define some test cases

# Generated at 2022-06-14 15:00:06.533320
# Unit test for constructor of class DictToken
def test_DictToken():
	from typesystem.base import Token, DictToken
	from typesystem.types import Dict
	dt = DictToken({'a': 'b'}, 1, 9, "abcd")
	assert dt.value == {'a':'b'}
	assert dt.start == (1, 1, 1)
	assert dt.end == (1, 1, 9)
	assert dt.string == "abcd"


# Generated at 2022-06-14 15:00:16.951321
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"1": 1, "2": 2, "3": 3}'
    start_index = 0
    end_index = 5
    value = {"1": 1, "2": 2, "3": 3}
    test = DictToken(value, start_index, end_index, content)
    assert test._content == content
    assert test._value == value
    assert test._start_index == start_index
    assert test._end_index == end_index
    assert test.start == Position(1, 1, start_index)
    assert test.end == Position(1, 6, end_index)
    assert test.lookup_key([0]) == test.lookup([0])._get_child_token("1")
    assert test.lookup([0]) == test._get_child_token("1")
   

# Generated at 2022-06-14 15:00:21.400333
# Unit test for constructor of class DictToken
def test_DictToken():
    source_text = '{"a": 1}'
    t = rparser.load_json(source_text)
    t_dict = t._value
    assert t.value == {"a": 1}
    assert type(t_dict) == dict
    assert t_dict["a"].value == 1


# Generated at 2022-06-14 15:00:26.890152
# Unit test for constructor of class DictToken
def test_DictToken():

    d = {"a": "b"}
    token = DictToken(d, 0, 1)

    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 2, 1)
    assert token.value == d
    assert token.string == "{'a': 'b'}"
    assert token.lookup([0, "a"]) is not None
    assert token.lookup_key([0, "a"]) is not None


# Generated at 2022-06-14 15:00:37.696532
# Unit test for constructor of class DictToken
def test_DictToken():
    token_dict = {'a': 'a', 'b': 'b'}
    test_dict_token = DictToken(token_dict, 0, 1, content=token_dict)
    assert test_dict_token.value == token_dict
    assert test_dict_token.end == Position(1, 1, 1)
    assert test_dict_token.start == Position(1, 1, 0)
    assert test_dict_token.string == token_dict
    assert test_dict_token.value == token_dict
    assert test_dict_token.lookup(['a']) == 'a'
    assert test_dict_token.lookup_key(['a']) == 'a'


# Generated at 2022-06-14 15:00:42.464428
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({'k1':'v1'},1,2)
    assert dict_token._child_keys == {'k1': 'k1'}
    assert dict_token._child_tokens == {'k1': 'v1'}


# Generated at 2022-06-14 15:00:43.935415
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({"a": "b"}, 0, 1)

# Generated at 2022-06-14 15:01:45.144275
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    expected = -9223372036854775808
    returned = ScalarToken(expected, None, None).__hash__()
    assert expected == returned


# Generated at 2022-06-14 15:01:47.692799
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = Token("value", 0, 1, "content")
    assert repr(token) == "Token(value)"

# Generated at 2022-06-14 15:01:53.202979
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.tokens import DictToken
    token = DictToken({}, 0, 3, content="")
    assert token._child_keys == {}
    assert token._child_tokens == {}
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 4, 3)


# Generated at 2022-06-14 15:01:54.065090
# Unit test for method lookup of class Token
def test_Token_lookup():
    assert Token()

# Generated at 2022-06-14 15:02:06.235872
# Unit test for method lookup of class Token
def test_Token_lookup():

    class Token:
        def __init__(self, value, start_index, end_index, content):
            self._value = value
            self._start_index = start_index
            self._end_index = end_index
            self._content = content

        def _get_value(self):
            raise NotImplementedError  # pragma: nocover

        def _get_child_token(self, key: typing.Any) -> Token:
            raise NotImplementedError  # pragma: nocover

        def _get_key_token(self, key: typing.Any) -> Token:
            raise NotImplementedError  # pragma: nocover

        @property
        def string(self):
            return self._content[self._start_index : self._end_index + 1]


# Generated at 2022-06-14 15:02:08.098440
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    d = ScalarToken(
        value="hey", start_index=3, end_index=5, content="hello"
    )
    assert hash(d) == hash("hey")

# Generated at 2022-06-14 15:02:09.369696
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({}, 0, 2)
    assert dt


# Generated at 2022-06-14 15:02:17.552650
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    Test.assert_equals(repr(ScalarToken(123, 0, 2)), "ScalarToken('123')")
    Test.assert_equals(repr(ScalarToken('string', 0, 5)), "ScalarToken('string')")
    Test.assert_equals(repr(ScalarToken(True, 0, 3)), "ScalarToken('True')")
    Test.assert_equals(repr(ScalarToken(None, 0, 3)), "ScalarToken('None')")


# Generated at 2022-06-14 15:02:25.224160
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    from typesystem.base import Scalar, List, Dict

    value = {
            "a": 1,
            "b": {"c": 2, "d": {"e": 3}},
            "f": [4, 5, None],
            "g": None
        }

    content = """
    {
      "a": 1,
      "b": {
        "c": 2,
        "d": {
          "e": 3
        }
      },
      "f": [
        4,
        5,
        null
      ],
      "g": null
    }
    """

    root = DictToken(value, 0, 0, content)[0]
    assert root.lookup([]) == DictToken(value, 0, 0, content)[0]
    assert root.lookup([]) == DictToken

# Generated at 2022-06-14 15:02:30.764869
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class A(Token):
        def __init__(self, y) -> None:
            super().__init__(y, 2, 4)
        def _get_value(self) -> typing.Any:
            return self._value
    
    assert A(2) == A(2)
    assert A(3) != A(5)
    assert A(3) != Token(3, 2, 4)



# Generated at 2022-06-14 15:03:59.445310
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    print('test_Token___eq__')
    Token._get_value = lambda x: 5
    t1 = Token(None, None, None)
    Token._get_value = lambda x: 6
    t2 = Token(None, None, None)
    Token._get_value = lambda x: 5
    Token._start_index = 1
    t3 = Token(None, None, None)
    Token._get_value = lambda x: 5
    Token._start_index = 0
    Token._end_index = 1
    t4 = Token(None, None, None)
    Token._get_value = lambda x: 6
    Token._start_index = 0
    Token._end_index = 1
    t5 = Token(None, None, None)

    assert t1 == t1
    assert not t1 == t2
   

# Generated at 2022-06-14 15:04:01.289416
# Unit test for constructor of class ListToken
def test_ListToken():
    # Prevent coverage from missing test cases
    assert True

# Generated at 2022-06-14 15:04:04.409768
# Unit test for constructor of class ListToken
def test_ListToken():
    content = "content"
    value = "test value"
    start_index = 0
    end_index = 5
    Token(value, start_index, end_index, content)

# Generated at 2022-06-14 15:04:10.230357
# Unit test for constructor of class ListToken
def test_ListToken():
    token = ListToken([], 0, 10, "hello")
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 11, 10)
    assert token.string == "hello"
    assert token.lookup([]) == token
    assert token.lookup_key([]) == token
    assert token._get_child_token([]) == token
    assert token._get_key_token([]) == token


# Generated at 2022-06-14 15:04:13.479586
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    try:
        ScalarToken(value, start_index, end_index, content).__hash__()
    except NotImplementedError:
        pass
    else:
        no_exception_raised()


# Generated at 2022-06-14 15:04:19.755096
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    obj_ScalarToken_1 = ScalarToken(0, 0, 0)
    obj_ScalarToken_2 = ScalarToken(0, 0, 0)
    try:
        obj_ScalarToken_1.__hash__() == obj_ScalarToken_2.__hash__()
    except AssertionError:
        print("AssertionError")


# Generated at 2022-06-14 15:04:21.635840
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    assert Token(["value"], 0, 5, "string").__repr__() == "Token(['value'])"

# Generated at 2022-06-14 15:04:24.155403
# Unit test for constructor of class ListToken
def test_ListToken():
    d = ListToken(value=None, start_index=0, end_index=0, content="")
    assert d._get_value() == [token._get_value() for token in d._value]

# Generated at 2022-06-14 15:04:25.364867
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({}, 0, 1, "")

# Generated at 2022-06-14 15:04:32.487072
# Unit test for method lookup of class Token
def test_Token_lookup():
    class MyScalarToken(ScalarToken):
        _value = 1
        _start_index = 1
        _end_index = 2
        _content = '{"a": 2}'

    class MyListToken(ListToken):
        _value = [MyScalarToken()]
        _start_index = 1
        _end_index = 2
        _content = '{"a": 2}'

    class MyDictToken(DictToken):
        _value = {MyScalarToken(): MyListToken()}
        _start_index = 1
        _end_index = 2
        _content = '{"a": 2}'
        
    assert MyDictToken().lookup([0, 0])._get_value() == 1

# Generated at 2022-06-14 15:06:16.874568
# Unit test for constructor of class Token
def test_Token():
    t = Token(value = 10, start_index = 10, end_index = 12, content = "test")
    assert t._value == 10
    assert t._start_index == 10
    assert t._end_index == 12
    assert t._content == "test"
    assert t.string == "test"[10:13]
    assert t.value == 10
    p = t.start
    assert p.line_no == 1
    assert p.column_no == 1
    assert p.index == 10
    p = t.end
    assert p.line_no == 1
    assert p.column_no == 3
    assert p.index == 12
