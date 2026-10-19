

# Generated at 2022-06-14 14:56:20.569224
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({})
    assert dict_token.__class__.__name__ == "DictToken"

# Generated at 2022-06-14 14:56:23.916708
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = ScalarToken("foo", 0, 2, content="bar")
    t2 = Token("foo", 0, 2, content="bar")
    assert t1 == t1
    assert not t1 == t2
    assert not t1 == "foo"


# Generated at 2022-06-14 14:56:28.033179
# Unit test for constructor of class DictToken
def test_DictToken():
    start_index = 0
    end_index = 1
    value = {2: 3}
    d = DictToken(value, start_index, end_index)
    assert d._start_index == start_index
    assert d._end_index == end_index
    assert d._value == value


# Generated at 2022-06-14 14:56:30.699437
# Unit test for constructor of class DictToken
def test_DictToken():
    value = {'name': 'ljf'}
    start_index = 0
    end_index = 2
    content = ""
    dt = DictToken(value, start_index, end_index)


# Generated at 2022-06-14 14:56:35.186342
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token('a', 1, 2, 'abc')
    token2 = Token('a', 1, 2, 'abc')
    token3 = Token('b', 1, 2, 'abc')
    token4 = Token('a', 0, 2, 'abc')
    token5 = Token('a', 1, 3, 'abc')
    assert token1 == token2
    assert token1 != token3
    assert token1 != token4
    assert token1 != token5

# Generated at 2022-06-14 14:56:37.937458
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    StringToken = ScalarToken("hey", 1, 3)
    StringToken2 = ScalarToken("hey", 1, 3)
    assert StringToken == StringToken2

# Generated at 2022-06-14 14:56:45.715622
# Unit test for constructor of class DictToken
def test_DictToken():
    # Check that DictToken correctly filters out keys and values from the dictionary.
    d = { ScalarToken(2, 3, 4): ScalarToken(2, 3, 4) }
    dt = DictToken(d, 3, 4)
    assert d == dt._value
    assert dt._child_keys[2] == ScalarToken(2, 3, 4)
    assert dt._child_tokens[2] == ScalarToken(2, 3, 4)



# Generated at 2022-06-14 14:56:49.178666
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(value=1, start_index=0, end_index=1)
    t2 = Token(value=2, start_index=0, end_index=1)
    assert t1 == t1 and t1 != t2



# Generated at 2022-06-14 14:56:58.279842
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.typing import Dict, String, Integer
    from typesystem.parser import parse
    import json
    # testStr = '{"a": 1, "b": 2}'
    # data = json.loads(testStr)
    # typeOfData = Dict(String(), Integer())
    # parser_result = parse(testStr, typeOfData)
    # print(parser_result)
    # with open('test.txt', 'w+') as f:
    #     json.dump(parser_result, f)
    # print(parser_result.value)

    # testStr = '{"a": 1, "b": 2}'
    # data = json.loads(testStr)
    # typeOfData = Dict(String(), Integer())
    # parser_result = parse(testStr, typeOfData)


# Generated at 2022-06-14 14:57:01.541150
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(1, 1, 2)
    assert token1._get_value == None

    token2 = Token(1, 1, 2)
    assert token1 == token2 == True


# Generated at 2022-06-14 14:57:09.496578
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(3,1,2)
    t2 = Token(3,1,2)
    assert(t1 == t2)


# Generated at 2022-06-14 14:57:13.101833
# Unit test for constructor of class DictToken
def test_DictToken():
    _value = {'a':'a','b':'b','c':'c'}
    _start_index = 0
    _end_index = 1
    a = DictToken(_value, _start_index, _end_index)
    assert a._value.keys() == {'a','b','c'}
    

# Generated at 2022-06-14 14:57:24.692094
# Unit test for constructor of class DictToken
def test_DictToken():
    content = "001[1]"
    start_index = 0
    end_index = 5
    #
    assert DictToken(
             value={
               ScalarToken(value=1, start_index=2, end_index=2, content=content):
               ScalarToken(value=1, start_index=4, end_index=4, content=content)
             }, start_index=start_index, end_index=end_index, content=content
           ) == DictToken(
             value={
               ScalarToken(value=1, start_index=2, end_index=2, content=content):
               ScalarToken(value=1, start_index=4, end_index=4, content=content)
             }, start_index=start_index, end_index=end_index, content=content
           )

# Generated at 2022-06-14 14:57:33.384377
# Unit test for constructor of class DictToken
def test_DictToken():
    token_dict = DictToken({"key1": "value1", "key2": "value2"}, 2, 4, "Content")
    
    # check whether the value stored in instance variable _value is a dictionary
    assert isinstance(token_dict._value, dict)
    
    # check whether the value stored in instance variable _child_keys is a dictionary
    assert isinstance(token_dict._child_keys, dict)
    assert isinstance(token_dict._child_keys["key1"], type(token_dict)) # check the value of _child_keys is of type DictToken
    assert isinstance(token_dict._child_keys["key2"], type(token_dict))
    
    # check whether the value stored in instance variable _child_tokens is a dictionary

# Generated at 2022-06-14 14:57:43.662109
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(value = "hello", start_index = 0, end_index = 4, content = "hello")
    token2 = Token(value = "hello", start_index = 0, end_index = 4, content = "hello")
    token3 = Token(value = "salut", start_index = 0, end_index = 4, content = "salut")
    token4 = Token(value = "salut", start_index = 1, end_index = 4, content = "salut")

    assert token1 == token2, "test_Token___eq__ : token1 should equal token2."
    assert not(token1 == token3), "test_Token___eq__ : token1 should not equal token3."
    assert not(token1 == token4), "test_Token___eq__ : token1 should not equal token4."
   

# Generated at 2022-06-14 14:57:48.277750
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken(
        {1: 1, 2: 2}, start_index=0, end_index=0, content=""
    )
    assert dt == DictToken({1: 1, 2: 2}, start_index=0, end_index=0, content="")


# Generated at 2022-06-14 14:57:55.675443
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Setup
    token = Token(
        value = {'a': 1, 'b': 2},
        start_index = 0,
        end_index = 1,
        content = {'a': 1, 'b': 2},
    )
    other = Token(
        value = {'a': 1, 'b': 2},
        start_index = 0,
        end_index = 1,
        content = {'a': 1, 'b': 2},
    )
    # Exercise
    actual = token == other
    # Verify
    assert actual == True
    # Cleanup - none necessary



# Generated at 2022-06-14 14:58:01.172664
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    obj = Token(1, 2, 3, 4)
    assert obj == 1
    assert obj == obj
    assert not (obj == None)
    assert not (obj == "")
    assert not (obj == [])
    assert not (obj == ())
    assert not (obj == {})
    assert not (obj == set())



# Generated at 2022-06-14 14:58:03.090508
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1, 2, 3) == Token(1, 2, 3)


# Generated at 2022-06-14 14:58:05.713805
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({'apple':'red'})
    assert token == DictToken({'apple':'red'})


# Generated at 2022-06-14 14:58:32.277907
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(None, 0, 0, content='')
    t2 = Token(None, 0, 0, content='')
    t3 = Token(None, 1, 1, content='')
    t4 = Token(None, 2, 2, content='')
    assert t1 == t2
    assert t1 != t3
    assert t1 != t4

# Generated at 2022-06-14 14:58:34.696946
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken(True, 0, 1, 'yes')
    token2 = ScalarToken(True, 0, 1, 'yes')
    assert token1 == token2


# Generated at 2022-06-14 14:58:37.537907
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1,1,1) == Token(1,1,1)
    assert Token(2,2,2) != Token(2,2,2)


# Generated at 2022-06-14 14:58:44.054803
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = ScalarToken(None, 1, 2, "ab")
    t2 = ScalarToken(None, 3, 3, "ab")
    expect = False
    assert t1.__eq__(t2) == expect
    assert t1 == t2 == expect

    t1 = ScalarToken(1, 1, 2, "ab")
    t2 = ScalarToken(1, 1, 2, "ab")
    expect = True
    assert t1.__eq__(t2) == expect
    assert t1 == t2 == expect

    t1 = ListToken([ScalarToken(1, 1, 2, "ab")], 1, 2, "ab")
    t2 = ListToken([ScalarToken(1, 1, 2, "ab")], 1, 2, "ab")
    expect = True

# Generated at 2022-06-14 14:58:46.345255
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken()
    assert a.__class__.__name__ == "DictToken"


# Generated at 2022-06-14 14:58:48.967047
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token("", 0, 0)
    token2 = Token("", 0, 0)
    assert(token1 == token2)


# Generated at 2022-06-14 14:58:49.822599
# Unit test for constructor of class DictToken
def test_DictToken():
    assert True

# Generated at 2022-06-14 14:58:53.833535
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token("value", 1,2,"content")
    assert token.__eq__(token) == True
    scalar_token = ScalarToken("value", 1,2,"content")
    assert token.__eq__(scalar_token) == False

# Generated at 2022-06-14 14:59:05.892484
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({}, 1, 2, '')
    b = DictToken({}, 1, 2, '')
    c = DictToken({}, 3, 4, '')
    d = DictToken({}, 1, 2, 'a')

    # test __eq__
    assert a == b
    assert a != c
    assert a != d
    assert a != 1
    assert a != {1: 2}
    assert a != {}

    # test __hash__
    assert hash(a) == hash(b)
    assert hash(a) != hash(c)

    # test _get_value
    assert a._get_value() == {}

    # test _get_child_token
    a._child_tokens = {1: 2, 3: 4}
    assert a._get_child_token(1)

# Generated at 2022-06-14 14:59:14.980131
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(None, 0, 0) == ScalarToken(None, 0, 0)
    assert Token(None, 0, 0) != None
    assert Token(None, 0, 0) != ScalarToken(None, 1, 1)
    assert Token(None, 0, 0) != ScalarToken(False, 0, 0)
    assert ScalarToken(False, 0, 0) == ScalarToken(False, 0, 0)
    assert ScalarToken(False, 0, 0) != ScalarToken(False, 1, 1)
    assert ScalarToken(False, 0, 0) != ScalarToken(True, 0, 0)
    assert ScalarToken(False, 0, 0) != ScalarToken(None, 0, 0)

# Generated at 2022-06-14 14:59:27.156196
# Unit test for constructor of class DictToken
def test_DictToken():
    item = {'a': 1, 'b': 2}
    token = DictToken(item, 0, 0, 'a: 1, b: 2')
    assert token._get_value() == item
    assert token.start == Position(1, 0, 0)
    assert token.end == Position(1, 0, 0)
    assert token.string == 'a: 1, b: 2'


# Generated at 2022-06-14 14:59:31.928027
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken('dict_token',0,5,content='lkjlkj')
    assert dict_token._value=='dict_token'
    assert dict_token._content=='lkjlkj'
    assert dict_token._start_index==0
    assert dict_token._end_index==5


# Generated at 2022-06-14 14:59:35.284360
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({'hello': 'world'}, 0, 5)
    assert DictToken
    assert isinstance(d, DictToken)

# Generated at 2022-06-14 14:59:38.327082
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({}, 0, 0, '')
    assert dict_token._child_keys == {}
    assert dict_token._child_tokens == {}

# Generated at 2022-06-14 14:59:49.097286
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {
        ScalarToken('ab',0,2,'ab'): ScalarToken(1,1,1,'1'),
        ScalarToken('cd',2,4,'abcd'): ScalarToken(2,1,1,'2'),
    }
    dt = DictToken(d,0,5,'ab1cd2')
    assert d == dt._get_value()
    assert dt._get_child_token('ab') == d[ScalarToken('ab',0,2,'ab')]
    assert dt._get_key_token('cd') == ScalarToken('cd',2,4,'abcd')
    assert dt.start == Position(1,1,0)
    assert dt.end == Position(1,5,4)
    assert dt.string == 'ab1cd2'

# Generated at 2022-06-14 15:00:00.681558
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(
        {1:2, 3:4},
        0,
        len("{1:2, 3:4}"),
        "{1:2, 3:4}"
    )
    assert d.value == {1:2, 3:4}
    assert d.start.line_no == 1
    assert d.start.column_no == 1
    assert d.start.index == 0
    assert d.end.line_no == 1
    assert d.end.column_no == 8
    assert d.end.index == 7
    assert d.string == "{1:2, 3:4}"
    assert len(d.lookup([1]).string) == 2
    assert len(d.lookup_key([1, 1]).string) == 1


# Generated at 2022-06-14 15:00:12.632332
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_tok = {
        0: 'token0',
        1: 'token1',
        2: 'token2',
    }

    dt = DictToken(dict_tok, 0, 2, "token0token1token2")
    assert dt._value == dict_tok
    assert dt._start_index == 0
    assert dt._end_index == 2
    assert dt._content == "token0token1token2"
    assert dt._child_keys == {
        0: 'token0',
        1: 'token1',
        2: 'token2',
    }
    assert dt._child_tokens == {
        0: 'token0',
        1: 'token1',
        2: 'token2',
    }



# Generated at 2022-06-14 15:00:19.877040
# Unit test for constructor of class DictToken
def test_DictToken():
    class TokenSchema(dict):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

    def test_DictToken1():
        try:
            DictToken({1: 1})._value
        except RuntimeError:
            pass
        else:
            assert False


# Generated at 2022-06-14 15:00:22.242184
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken_test = DictToken(1,2,3)
    assert DictToken_test.__init__(1,2,3)

# Generated at 2022-06-14 15:00:24.382692
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken(value = {}, start_index = 1, end_index = 2, content = "abc")
    assert t


# Generated at 2022-06-14 15:00:45.442678
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({"k1": "v1", "k2": "v2"}, 1, 3, "blah")
    assert isinstance(a, DictToken) == True
    assert isinstance(a._child_keys, dict) == True
    assert isinstance(a._child_tokens, dict) == True
    try:
        a._get_child_token([1])
        assert False
    except NotImplementedError:
        assert True
    try:
        a._get_key_token([1]) 
        assert False
    except NotImplementedError:
        assert True

#Unit test for built-in method __eq__

# Generated at 2022-06-14 15:00:51.152822
# Unit test for constructor of class DictToken
def test_DictToken():
    # Arrange
    key = Token(1, 2, 5, "ab")
    value = Token(1, 2, 5, "ab")
    # Act
    token = DictToken({key: value}, 0, 2, "abc")
    # Assert
    assert token._child_keys == {1: key}
    assert token._child_tokens == {1: value}

# Generated at 2022-06-14 15:00:52.985560
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken()
    assert t is not None


# Generated at 2022-06-14 15:01:05.044394
# Unit test for constructor of class DictToken
def test_DictToken():
    # Test for constructor
    a = DictToken({ScalarToken('a', 0, 1):ListToken([ScalarToken(1, 2, 3)], 2, 5)}, 0, 5)
    assert a._child_tokens == {'a':ListToken([ScalarToken(1, 2, 3)], 2, 5)}
    assert a._child_keys == {'a':ScalarToken('a', 0, 1)}
    assert a._value == {ScalarToken('a', 0, 1):ListToken([ScalarToken(1, 2, 3)], 2, 5)}
    assert a._content == ""
    assert a._start_index == 0
    assert a._end_index == 5
    
    # Test for _get_value

# Generated at 2022-06-14 15:01:06.570385
# Unit test for constructor of class DictToken
def test_DictToken():
    x = DictToken({})
    assert x


# Generated at 2022-06-14 15:01:10.248867
# Unit test for constructor of class DictToken
def test_DictToken():
    # given
    test_dict = {"a":"b"}
    token = DictToken(test_dict, 0, 10, "this is content")
    # when
    a = token._get_value()
    # then
    assert(a == {"a":"b"})


# Generated at 2022-06-14 15:01:16.776636
# Unit test for constructor of class DictToken
def test_DictToken():
    content = "test"
    _value = {"a":"b"}
    start_index = 1
    end_index = 4
    token = DictToken(_value=_value, start_index=start_index, end_index=end_index, content=content)
    assert token._content == content
    assert token._value == _value
    assert token._start_index == start_index
    assert token._end_index == end_index


# Generated at 2022-06-14 15:01:17.684351
# Unit test for constructor of class DictToken
def test_DictToken():
	pass


# Generated at 2022-06-14 15:01:24.639389
# Unit test for constructor of class DictToken
def test_DictToken():
    pos = Position(1, 1, 0)
    data_dict = {}
    data_dict[ScalarToken('key1', 1, 4, "key1 = value1")] = \
               ScalarToken('value1', 1, 11, 'key1 = value1')
    data_dict[ScalarToken('key2', 2, 4, "key2 = value2")] = \
               ScalarToken('value2', 2, 11, 'key2 = value2')
    # print(data_dict)
    t = DictToken(data_dict, pos, pos + len(data_dict) - 1, "key1 = value1\nkey2 = value2")
    assert repr(t) == "DictToken({'key1': 'value1', 'key2': 'value2'})"
    assert t.string

# Generated at 2022-06-14 15:01:33.069002
# Unit test for constructor of class DictToken
def test_DictToken():
	value = dict()
	value[1] = 3
	value[2] = 4
	value[3] = 5
	start_index = 0
	end_index = 5
	content = ""
	a = DictToken(value, start_index, end_index, content)
	try:
		assert(len(a._child_keys) == 3 and len(a._child_tokens) == 3)
	except AssertionError:
		print("Error in test_DictToken(): Constructor of class DictToken")
		exit()

# Generated at 2022-06-14 15:01:53.881714
# Unit test for constructor of class DictToken
def test_DictToken():
    assert(True)


# Generated at 2022-06-14 15:02:06.031398
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({"a": 1},start_index=0,end_index=10)
    # Unit test for method _get_value
    def test__get_value():
        assert dict_token._get_value() == {"a": 1}
    # Unit test for method _get_child_token
    def test__get_child_token():
        assert dict_token._get_child_token("a") == 1
    # Unit test for method _get_key_token
    def test__get_key_token():
        assert dict_token._get_key_token("a") == "a"
    # Unit test for method __hash__
    def test___hash__():
        assert hash(dict_token) == -6804647826174478816
    # Unit test for method __eq__

# Generated at 2022-06-14 15:02:08.031107
# Unit test for constructor of class DictToken
def test_DictToken():
    token = Token(1,2,3)
    assert(token.value == 1)
    assert(token.start == 2)
    assert(token.end == 3)


# Generated at 2022-06-14 15:02:09.297678
# Unit test for constructor of class DictToken
def test_DictToken():
    #raise NotImplementedError()
    DictToken()
    assert True



# Generated at 2022-06-14 15:02:15.613056
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.parser import parse_schema
    schema_token = parse_schema("""
        type: object
        properties:
            name:
                type: string
        """)
    assert isinstance(schema_token, DictToken)
    assert isinstance(schema_token._get_child_token('properties'), DictToken)


# Generated at 2022-06-14 15:02:18.325201
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken({'key':'value'}, 0, 0, 'content')
    assert dict_token._value == {'key':'value'}
    assert dict_token._start_index == 0
    assert dict_token._end_index == 0
    assert dict_token._content == 'content'


# Generated at 2022-06-14 15:02:23.541910
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem import String, Integer
    from typesystem.dsl import Schema

    class PersonToken(DictToken):
        pass

    class PersonSchema(Schema):
        schema_cls = PersonToken
        first_name = String()
        last_name = String()
        age = Integer(minimum=0, maximum=120)
        country = String()

    p = PersonSchema({'first_name': 'Jing', 'age': '23', 'last_name': 'Wang', 'country': 'China'})
    assert p.value == {'first_name': 'Jing', 'age': 23, 'last_name': 'Wang', 'country': 'China'}
    assert p.errors == [{'field': 'age', 'code': 'invalid', 'value': '23'}]

# Generated at 2022-06-14 15:02:28.165223
# Unit test for constructor of class DictToken
def test_DictToken():
    token = {'a':1,'b':2}
    ans = DictToken(token, 1, 4)

    assert ans._value == token
    assert ans._child_keys == token
    assert ans._child_tokens == token

# Generated at 2022-06-14 15:02:30.706110
# Unit test for constructor of class DictToken
def test_DictToken():
	token = DictToken({"123": "321"}, 0, 1, "123")
	assert token.lookup([1]) == token._child_tokens[1]


# Generated at 2022-06-14 15:02:36.159610
# Unit test for constructor of class DictToken
def test_DictToken():
    token_dict = {"a": "A", "b": "B", "c": "C"}
    dt = DictToken(token_dict, 0, 2, content = "abc")
    assert set(dt._child_keys.keys()) == {"a", "b", "c"}
#pass


# Generated at 2022-06-14 15:03:25.158254
# Unit test for constructor of class DictToken
def test_DictToken():
    a = Token.DictToken('hello','world','123456','vvvvv')
    assert a.__dict__ == {'_value': 'hello', '_start_index': 'world', '_end_index': '123456', '_content': 'vvvvv'}

    b = Token.DictToken('1','2','3','4')
    assert b.__dict__ == {'_value': '1', '_start_index': '2', '_end_index': '3', '_content': '4'}

    c = Token.DictToken('a','b','c','d')
    assert c.__dict__ == {'_value': 'a', '_start_index': 'b', '_end_index': 'c', '_content': 'd'}


# Generated at 2022-06-14 15:03:27.215325
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({'a':0, 'b':1}) == DictToken({'a':0, 'b':1})


# Generated at 2022-06-14 15:03:37.633095
# Unit test for constructor of class DictToken
def test_DictToken():
    _value = {'item1': 'value1'}
    _start_index = 0
    _end_index = 0
    _content = ""

    token1 = DictToken(_value, _start_index, _end_index, _content)
    assert token1._value == {'item1': 'value1'}
    assert token1._start_index == 0
    assert token1._end_index == 0
    assert token1._content == ""

    _value = {'item2': 'value2'}
    _start_index = 1
    _end_index = 1
    _content = " "

    token2 = DictToken(_value, _start_index, _end_index, _content)
    assert token2._value == {'item2': 'value2'}

# Generated at 2022-06-14 15:03:47.958583
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({"a": "b"}, 1, 2, "abc")._content == "abc"
    assert DictToken({"a": "b"}, 1, 2, "abc")._start_index == 1
    assert DictToken({"a": "b"}, 1, 2, "abc")._end_index == 2
    assert DictToken({"a": "b"}, 1, 2, "abc")._value == {"a": "b"}
    assert DictToken({"a": "b"}, 1, 2, "abc")._child_keys == {"a": "b"}
    assert DictToken({"a": "b"}, 1, 2, "abc")._child_tokens == {"a": "b"}


# Generated at 2022-06-14 15:03:53.460234
# Unit test for constructor of class DictToken
def test_DictToken():
    import ast
    print("Testing constructor of class DictToken with an AST")
    token = DictToken(value={'a': 1, 'b': 2}, start_index=0, end_index=1, content='ab')
    assert token._value == {'a': 1, 'b': 2}
    assert token._start_index == 0
    assert token._end_index == 1
    assert token._content == 'ab'
    assert token.string == 'ab'



# Generated at 2022-06-14 15:03:56.295926
# Unit test for constructor of class DictToken
def test_DictToken():
	a = DictToken({})
	b = DictToken({},1,2,"")
	c = DictToken({},content="")
	d = DictToken({},1,"",content="")


# Generated at 2022-06-14 15:04:02.057876
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {}
    d[1] = 2
    d[3] = 4
    dt = DictToken(d, 0, 5, "12345")
    assert dt.value == {1:2, 3:4}
    assert dt.string == "12345"
    assert dt.start == Position(1, 1, 0)
    assert dt.end == Position(1, 6, 5)
    assert dt.lookup([1]) == 4
    assert dt.lookup_key([1]) == 3



# Generated at 2022-06-14 15:04:08.229368
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.exceptions import TypeSystemError
    from typesystem.parser import type_parser

    for s in [
        "",
        " ",
        "{ ",
        "{ foo: 5 }",
        "{ foo: 5, }",
        "{ foo: 5, bar: 6 } ",
    ]:
        try:
            type_parser.parse(s)
        except TypeSystemError:
            pass
        else:
            assert False



# Generated at 2022-06-14 15:04:16.424268
# Unit test for constructor of class DictToken
def test_DictToken():
    testToken = DictToken({'s': 'a', 'b': 2}, 0, 2, 's=a,b=2')
    assert type(testToken) is DictToken
    assert testToken._start_index == 0
    assert testToken._end_index == 2
    assert testToken._value == {'s': 'a', 'b': 2}
    assert testToken._content == 's=a,b=2'
    assert testToken._child_keys == {'b': 2, 's': 'a'}
    assert testToken._child_tokens == {'b': 2, 's': 'a'}


# Generated at 2022-06-14 15:04:26.166988
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"a":2}'
    start_index = 0
    end_index = len(content) - 1
    token1 = ScalarToken("a", 0, 2)
    token2 = ScalarToken(2, 4, 5)
    dictToken = DictToken({token1: token2}, start_index, end_index, content)
    assert dictToken._start_index == 0
    assert dictToken._end_index == 5
    assert dictToken._content[dictToken._start_index : dictToken._end_index + 1] == '{"a":2}'
    assert dictToken._get_value() == {"a":2}
    assert dictToken.value == {"a":2}
    assert dictToken.start.line_no == 1
    assert dictToken.end.line_no == 1