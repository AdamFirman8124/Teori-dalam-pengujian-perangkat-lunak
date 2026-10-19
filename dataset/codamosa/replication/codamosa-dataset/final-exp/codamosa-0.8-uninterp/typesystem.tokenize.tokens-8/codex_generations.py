

# Generated at 2022-06-14 14:56:19.256840
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(value = "", start_index = 0, end_index = 0, content = "")
    other = Token(value = "", start_index = 0, end_index = 0, content = "")
    assert token.__eq__(other) == True

# Generated at 2022-06-14 14:56:27.756834
# Unit test for constructor of class DictToken
def test_DictToken():
    dict1={"a":1}
    assert(DictToken(dict1, 3, 2, "test") == DictToken(dict1, 3, 2, "test"))
    dict2={"b":1}
    assert(DictToken(dict1, 3, 2, "test") != DictToken(dict2, 3, 2, "test"))
    assert(DictToken(dict1, 4, 2, "test") != DictToken(dict1, 3, 2, "test"))
    assert(DictToken(dict1, 3, 3, "test") != DictToken(dict1, 3, 2, "test"))
    assert("" == DictToken(dict1, 3, 2, "test")._content)
    assert("test" == DictToken(dict1, 3, 2, "test").string)
   

# Generated at 2022-06-14 14:56:37.847806
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    value_0 = [
        {
            "a": "a",
            "b": "b",
            "c": "c",
        },
        {
            "d": "d",
            "e": "e",
            "f": "f",
        },
        {
            "g": "g",
            "h": "h",
            "i": "i",
        },
    ]

    value_1 = [
        {
            "a": "A",
            "b": "B",
            "c": "C",
        },
        {
            "d": "D",
            "e": "E",
            "f": "F",
        },
        {
            "g": "G",
            "h": "H",
            "i": "I",
        },
    ]

# Generated at 2022-06-14 14:56:45.615377
# Unit test for method __eq__ of class Token
def test_Token___eq__():
	t1 = Token([''],'','','abc')
	t1._value = 'abc'
	t1._start_index = 0
	t1._end_index = 2
	t1._content = 'abc'
	t2 = Token([''],'','','abc')
	t2._value = 'abc'
	t2._start_index = 0
	t2._end_index = 2
	t2._content = 'abc'
	assert (t1 == t2) == True



# Generated at 2022-06-14 14:56:48.150049
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    """
    Test __eq__ method
    """

    # Case 1: OK
    assert Token(None, 0, 0) == Token(None, 0, 0)



# Generated at 2022-06-14 14:56:57.490804
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import String
    from typesystem.base import Number
    from typesystem.base import Integer
    from typesystem.base import Boolean

    from typesystem.base import Field
    from typesystem.base import Enum

    content = "{\n  \"name\": \"a\",\n  \"age\": 19,\n  \"cool\": true\n}"
    parser = get_parser("__main__", content)
    tokens = parser.run()

    assert isinstance(tokens[0], DictToken)
    assert tokens[0].value == {"name": "a", "age": 19, "cool": True}
    assert tokens[0].string == content
    assert tokens[0].start == Position(1, 1, 0)
    assert tokens[0].end == Position(5, 2, len(content))
    assert tokens

# Generated at 2022-06-14 14:57:03.319825
# Unit test for constructor of class DictToken
def test_DictToken():
    from pytest import raises
    from unittest.mock import Mock

    token = DictToken(value={'a': 'b'})
    assert repr(token) == "DictToken({'a': 'b'})"
    assert token.start is None
    assert token.end is None
    assert token.string == '{a: b}'
    with raises(AttributeError):
        token._value = Mock()



# Generated at 2022-06-14 14:57:10.902936
# Unit test for constructor of class DictToken
def test_DictToken():
    token_d=DictToken({ 1 : 2, 2 : 3 } )
    assert token_d._child_keys == { 1 : 2, 2 : 3 }
    assert token_d._child_tokens == { 1 : 2, 2 : 3 }
    token_l=DictToken({ 1 : 2, 2 : 3 } )
    assert token_l._child_keys == { 1 : 2, 2 : 3 }
    assert token_l._child_tokens == { 1 : 2, 2 : 3 }
        

# Generated at 2022-06-14 14:57:12.241041
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1,2,3,4) == Token(1,2,3,4)


# Generated at 2022-06-14 14:57:19.890980
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    s = ScalarToken(1, 0, 0)
    assert s.__eq__(ScalarToken(1, 0, 0)) == True
    assert s.__eq__(ScalarToken(1, 1, 0)) == False
    assert s.__eq__(ScalarToken(1, 0, 1)) == False
    assert s.__eq__(ScalarToken(2, 0, 0)) == False
    assert s.__eq__(DictToken({}, 0, 0)) == False

# Generated at 2022-06-14 14:57:29.634789
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken(None, None, None)._value == None
    assert DictToken(None, None, None)._end_index == None
    assert DictToken(None, None, None)._child_tokens == None
    assert DictToken(None, None, None)._child_keys == None
    assert DictToken(None, None, None)._start_index == None
    assert DictToken(None, None, None)._content == None


# Generated at 2022-06-14 14:57:34.041239
# Unit test for constructor of class DictToken
def test_DictToken():
    value = {
            "Key": "Value"
        }

    token = DictToken(value, 1, 1)
    assert (token._child_tokens["Key"].string == "Value")
    assert (token._child_keys["Key"].string == "Key")

# Generated at 2022-06-14 14:57:36.431352
# Unit test for constructor of class DictToken
def test_DictToken():
    x = dict(a=1, b=2)
    k = DictToken(x, 0, 0)
    assert k._get_value() == x

# Generated at 2022-06-14 14:57:40.429552
# Unit test for constructor of class DictToken
def test_DictToken():
    d1 = {'one': 1}
    d2 = {'two': 2}
    d3 = {**d1, **d2}
    foo = DictToken(d3, 0, 1, 'd3:', )
    return foo

# Generated at 2022-06-14 14:57:42.672215
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({'hello': 'world'}, 0, 4, '{"hello": "world"}')
    assert dt.string == '{"hello": "world"}'

# Generated at 2022-06-14 14:57:48.387033
# Unit test for constructor of class DictToken
def test_DictToken():
	class A:
		def __init__(self):
			self.uid = 1
			self.name = 'A'
	a = A()
	b = A()
	keys = [a,b]
	values = [1,2]
	dict = dict(zip(keys, values))
	d = DictToken(dict, 1, 2, '')
	print(d._get_value())

# Generated at 2022-06-14 14:57:57.363193
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken(content='abc', start_index=1, end_index=2, value={})
    assert dt.string == 'bc'
    assert isinstance(dt.value, dict)
    assert dt.start.line_no == 1
    assert dt.start.column_no == 2
    assert dt.start.index == 1
    assert dt.end.line_no == 1
    assert dt.end.column_no == 3
    assert dt.end.index == 2
    assert isinstance(dt.lookup([0]), Token)
    assert isinstance(dt.lookup_key([0, 0]), Token)
    assert dt._get_position(index=1).index == 1
    assert repr(dt) == "DictToken('bc')"
    assert dt == dt

# Generated at 2022-06-14 14:58:07.772269
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({}, 0, 0)
    assert type(d) is DictToken
    assert d._get_value() == {}
    assert d._value == {}
    assert d._child_keys == {}
    assert d._child_tokens == {}

    d = DictToken({'a': 1}, 0, 0, "a 1")
    assert type(d) is DictToken
    assert d._get_value() == {'a': 1}
    assert d._value == {}
    assert d._child_keys == {'a': None}
    assert d._child_tokens == {'a': None}
    print("Class DictToken constructor test is passed!")


# Generated at 2022-06-14 14:58:09.721167
# Unit test for constructor of class DictToken
def test_DictToken():
    tk = DictToken({"a":1},0,1,content="hello")
    assert tk._get_value() == {"a":1}

# Generated at 2022-06-14 14:58:18.268526
# Unit test for constructor of class DictToken
def test_DictToken():
    token_1 = ScalarToken('car', 0, 1)
    token_2 = ScalarToken(1, 2, 3)
    dict_token = DictToken({token_1: token_2}, 0, 3)
    assert dict_token._value == {token_1: token_2}
    assert dict_token._start_index == 0
    assert dict_token._end_index == 3
    assert dict_token._content == ''
    assert dict_token._child_keys == {'car': token_1}
    assert dict_token._child_tokens == {'car': token_2}


# Generated at 2022-06-14 14:58:25.401885
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken.__init__(DictToken('abc'), 10, 20, 'abc') == None


# Generated at 2022-06-14 14:58:28.254605
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({}, 0, 2, "")
    assert token._value == {}
    assert token._start_index == 0
    assert token._end_index == 2
    assert token._content == ""

# Generated at 2022-06-14 14:58:29.125045
# Unit test for constructor of class DictToken
def test_DictToken():
    pass


# Generated at 2022-06-14 14:58:35.441094
# Unit test for constructor of class DictToken
def test_DictToken():
    a = '''{
    "a": 1,
    "b": 2
}'''
    
    d = DictToken({"a":1, "b":2}, 0, len(a)-1, a )
    assert d._get_value() ==  {"a":1, "b":2}



# Generated at 2022-06-14 14:58:38.216643
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({}, 0, 1, content="{}")
    assert t.__repr__() == 'DictToken({})'


# Generated at 2022-06-14 14:58:41.458489
# Unit test for constructor of class DictToken
def test_DictToken():
    assert token._get_value() == 'foo'
    assert token.value == 'foo'
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 4, 3)
    assert token.string == "foo"
    
    

# Generated at 2022-06-14 14:58:47.219231
# Unit test for constructor of class DictToken

# Generated at 2022-06-14 14:58:48.860624
# Unit test for constructor of class DictToken
def test_DictToken():
    print()
    print(DictToken)
    print()


# Generated at 2022-06-14 14:58:50.531604
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({"a": 1})
    assert t


# Generated at 2022-06-14 14:58:53.129135
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken()
    assert dt._child_keys == {}
    assert dt._child_tokens == {}


# Generated at 2022-06-14 14:59:00.448290
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem import Token, DictToken
    d_temp = {'a': 1}
    d_token = DictToken(d_temp, 0, 1)

# Generated at 2022-06-14 14:59:09.077288
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({'abc':'abc'}, 0, 3)
    assert t.value == {'abc':'abc'}
    assert t.string == "{'abc':'abc'}"
    assert t.start == Position(1, 7, 6)
    assert t.end == Position(1, 7, 6)
    assert t.lookup([]).string == "{'abc':'abc'}"
    assert t.lookup_key([]).string == "{'abc':'abc'}"


# Generated at 2022-06-14 14:59:10.150280
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken


# Generated at 2022-06-14 14:59:16.039058
# Unit test for constructor of class DictToken
def test_DictToken():
    d = dict()
    d['start_index'] = 1
    d['end_index'] = 2
    d['content'] = "content"
    d['child_keys'] = {'keys':'values'}
    d['child_tokens'] = {'tokens': 'values'}
    d1 = DictToken()
    assert isinstance(d1, DictToken) == True
    assert d1 == d1


# Generated at 2022-06-14 14:59:23.664499
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({"a": ScalarToken(10, 1, 5)}, 2, 10, "1234567890")
    assert dt.string == "123456789"
    assert dt.value == {"a": 10}
    assert dt.start == Position(1, 3, 2)
    assert dt.end == Position(1, 12, 10)
    assert dt.lookup([]) == dt
    assert dt.lookup(["a"]).value == ScalarToken(10, 1, 5).value
    #assert dt.lookup_key(["a"]).value == ScalarToken("a", 2, 6).value

# Generated at 2022-06-14 14:59:27.065779
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({"a": "b"}, 1, 2)
    assert token._value == {"a": "b"}
    assert token._start_index == 1
    assert token._end_index == 2

# Generated at 2022-06-14 14:59:35.669503
# Unit test for constructor of class DictToken
def test_DictToken():
    d1 = DictToken({"name": "key"}, 0, 1, content="key")
    assert d1.string == "{"

    d2 = DictToken({"name": "key"}, 0, 1, content="key")
    d2.string == "{"

    d3 = DictToken({"key": "test"}, 0, 1, content="test")
    assert d3.string == "{"

    d4 = DictToken({"key": "test"}, 0, 1, content="test")
    assert d4.string == "{"

    d5 = DictToken({"key": 2}, 0, 1, content="2")
    assert d5.string == "{"

    d6 = DictToken({"key": 2}, 0, 1, content="2")
    assert d6.string == "{"


# Generated at 2022-06-14 14:59:43.501818
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.token import DictToken
    from typesystem.token import ScalarToken
    token = DictToken({'name': 'DictToken'}, 0, 10)
    assert isinstance(token, DictToken)
    assert token._get_value() == {'name': 'DictToken'}
    assert token._value == {ScalarToken('name', 0, 4): ScalarToken('DictToken', 5, 12)}
    assert token._child_keys == {'name': ScalarToken('name', 0, 4)}


# Generated at 2022-06-14 14:59:49.580259
# Unit test for constructor of class DictToken
def test_DictToken():
    _dict = {1: 0, 2: 1, 3:2}
    token = DictToken(_dict, 0, 2, "")
    assert token._child_keys == {1: DictToken.__init__.__globals__["typing"]._VAR_}, token._child_keys
    assert token._child_tokens == {1: DictToken.__init__.__globals__["typing"]._VAR_}


# Generated at 2022-06-14 14:59:53.754888
# Unit test for constructor of class DictToken
def test_DictToken():
    test_dict = {
        'a': 1,
        'b': 2,
    }
    test_dict_token = DictToken(test_dict, 0, 0, '')
    assert test_dict_token


# Generated at 2022-06-14 15:00:02.366377
# Unit test for constructor of class DictToken
def test_DictToken():
	dict1={'a': 'b', 'c': 'd'}
	token1=DictToken(dict1, 0, 3)
	assert str(token1._get_value()) == "{'a':'b', 'c':'d'}"
	token1.__init__(dict1, 1, 4)
	assert str(token1._get_value()) == "{'a':'b', 'c':'d'}"


# Generated at 2022-06-14 15:00:03.813839
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken is not None
    return True

# Generated at 2022-06-14 15:00:07.456967
# Unit test for constructor of class DictToken
def test_DictToken():
    tokens = DictToken({'door': 'knob'}, 0, 10, '{"door": "knob"}')
    assert tokens._get_value() == {'door': 'knob'}


# Generated at 2022-06-14 15:00:12.733704
# Unit test for constructor of class DictToken
def test_DictToken():
  t = DictToken({'a':1,'b':2},1,2)
  assert t._child_keys == {'a': 'a', 'b': 'b'}
  assert t._child_tokens == {'a': 1, 'b': 2}
  assert isinstance(t, Token)
  

# Generated at 2022-06-14 15:00:21.311125
# Unit test for constructor of class DictToken
def test_DictToken():
    # Calling constructor of Token
    token = Token("test", 0, 1)
    # Calling constructor of ScalarToken
    sc_token = ScalarToken("test", 0, 1)
    # Calling constructor of DictToken
    dt = DictToken({"test": 3, "test2": 4}, 0, 1)
    # Calling constructor of ListToken
    lt = ListToken([1, 2, 3], 0, 1)
    # assertEqual(first, second, msg)
    assert token.__eq__(sc_token)

# Generated at 2022-06-14 15:00:22.558850
# Unit test for constructor of class DictToken
def test_DictToken():
    res = DictToken({}, 0, 0, "")
    assert res is not None

# Generated at 2022-06-14 15:00:24.051318
# Unit test for constructor of class DictToken
def test_DictToken():
    s = DictToken({'a': 'b'}, 0, 2)
    assert repr(s) == "'{}'"


# Generated at 2022-06-14 15:00:29.717631
# Unit test for constructor of class DictToken
def test_DictToken():
    key = ScalarToken(1, 0, 0, "1")
    value = ScalarToken(2, 2, 2, "2")
    tokens = {key: value}
    dict_token = DictToken(tokens, 0, 2, "1 2")
    assert dict_token._get_value() == {1: 2}
    assert dict_token._get_child_token(1) == ScalarToken(2, 2, 2, "2")
    assert dict_token._get_key_token(1) == ScalarToken(1, 0, 0, "1")
    assert dict_token.string == "1 2"
    assert dict_token.start == Position(1, 1, 0)
    assert dict_token.end == Position(1, 3, 2)

# Generated at 2022-06-14 15:00:39.630599
# Unit test for constructor of class DictToken
def test_DictToken():
    a = {
        "key1": "string1",
        "key2": 2,
        "key3": [3, 4],
        "key4": {
            "dictkey1": "dictvalue1",
            "dictkey2": 2,
            "dictkey3": [3, 4],
            "dictkey4": {
                "dictkey1": "dictvalue1",
                "dictkey2": 2,
                "dictkey3": [3, 4],
                "dictkey4": {
                    "dictkey1": "dictvalue1",
                    "dictkey2": 2,
                    "dictkey3": [3, 4],
                },
            },
        },
    }
    assert DictToken(a, 0, 1) != None


# Generated at 2022-06-14 15:00:45.242649
# Unit test for constructor of class DictToken
def test_DictToken():
    import typesystem
    from typesystem.base import Schema
    class TestDictToken(typesystem.Dict):
        __types__ = {"key-1": str, "key-2": str}

    test_dict_schema = TestDictToken()
    # print(test_dict_schema)
    test_dict_schema.validate({"key-1": "value-1", "key-2": "value-2"})
    # print(test_dict_schema)
    test_dict_schema.validate({"key-1": "value-1", "key-2": "value-2", "key-3": "value-3"})
    # print(test_dict_schema)



# Generated at 2022-06-14 15:00:55.154216
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({ScalarToken(1, 1,2):ScalarToken(11,1,12)},1,12,"test")
    assert d._value[ScalarToken(1, 1,2)] == ScalarToken(11,1,12)


# Generated at 2022-06-14 15:00:57.888351
# Unit test for constructor of class DictToken
def test_DictToken():
    line = '{"key": "value"}'
    tokens = {'key': 'value'}
    dict_token = DictToken(tokens, 0, len(line), line)
    assert dict_token._value['key']._value == 'value'


# Generated at 2022-06-14 15:01:09.591014
# Unit test for constructor of class DictToken
def test_DictToken():
    # some dictionary
    a = {1: 2, 3: 4}
    b = DictToken(a, start_index=0, end_index=1)
    c = DictToken(a, end_index=1, start_index=0)
    assert(b == c)
    assert(b._value == c._value)
    assert(b._get_value() == c._get_value())
    assert(b._start_index == c._start_index)
    assert(b._end_index == c._end_index)
    assert(b.string == c.string)
    # a and b
    d = b._value
    e = {f:g for f, g in b._value.items()}
    assert(d == e)
    assert(d == b._get_value())

# Generated at 2022-06-14 15:01:14.128111
# Unit test for constructor of class DictToken
def test_DictToken():
    assert_equal(DictToken(0, 1, 2), DictToken(0, 1, 2))
    assert_equal(DictToken(0, 1, 2), DictToken(0, 1, 3))


# Generated at 2022-06-14 15:01:19.677144
# Unit test for constructor of class DictToken
def test_DictToken():
    # Create a dictionary of Tokens that represent the lexeme of an input
    def create_key_token(value, start_index, end_index, content):
        return ScalarToken(value, start_index, end_index, content)
    def create_value_token(value, start_index, end_index, content):
        return ScalarToken(value, start_index, end_index, content)
    input_str_1 = "{{1: 'hello'}}"
    keys_tokens = {}
    values_tokens = {}
    keys_tokens['1'] = create_key_token('1', 2, 2, input_str_1)
    values_tokens['1'] = create_value_token('hello', 4, 8, input_str_1)

# Generated at 2022-06-14 15:01:21.728622
# Unit test for constructor of class DictToken
def test_DictToken():
    assert(DictToken("k", 1, 1) != None)
    print("test_DictToken passed")


# Generated at 2022-06-14 15:01:29.396182
# Unit test for constructor of class DictToken
def test_DictToken():
    dic_var={}
    DT = DictToken(
        value=dic_var, start_index=0, end_index=0, content=""
    )
    assert DT._value=={}
    assert DT._child_keys=={}
    assert DT._child_tokens=={}
    assert DT._start_index==0
    assert DT._end_index==0
    assert DT._content==""


# Generated at 2022-06-14 15:01:35.170681
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({"a":1, "b":2}, 10, 20, '{"a": 1, "b": 2}')
    assert d._value == {"a":1, "b":2}
    assert d._start_index == 10
    assert d._end_index == 20
    assert d._content == '{"a": 1, "b": 2}'
    assert d._child_keys == {"a":1, "b":2}
    assert d._child_tokens == {"a":1, "b":2}


# Generated at 2022-06-14 15:01:37.339932
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken(1,2,3,4,5,6)
    

# Generated at 2022-06-14 15:01:39.853079
# Unit test for constructor of class DictToken
def test_DictToken():
    x = DictToken(1, 2, 3, 4, 5, 6)
    print(x)

if __name__ == '__main__':
    test_DictToken()

# Generated at 2022-06-14 15:01:52.718265
# Unit test for constructor of class DictToken
def test_DictToken():
   DictToken({"name" : "david", "age" : 40}, 1, 2)


# Generated at 2022-06-14 15:01:58.157933
# Unit test for constructor of class DictToken
def test_DictToken():
    tok = DictToken(value = {'key': 'val'}, start_index = 1)
    assert tok._value['key'] == 'val'
    assert tok._start_index == 1
    assert tok._get_value() == {'key': 'val'}


# Generated at 2022-06-14 15:02:01.177215
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(value = {1:2}, start_index = 3, end_index = 4, content = "test DictToken")
    print(d.start, d.end)

# Generated at 2022-06-14 15:02:04.269463
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({'a': 'b'}, 0, 1)
    assert d._child_tokens['a'] == 'b'


# Generated at 2022-06-14 15:02:06.181614
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({"foo": "bar"})
    assert token._value == {"foo": "bar"}

# Generated at 2022-06-14 15:02:09.129776
# Unit test for constructor of class DictToken
def test_DictToken():
    parent = Token(0, 0, 0)
    child = Token(0, 0, 0)
    empty_dict = {}
    dict_one_item = {parent: child}
    assert DictToken(dict_one_item, 0, 0, '{}')._value == empty_dict


# Generated at 2022-06-14 15:02:14.986481
# Unit test for constructor of class DictToken
def test_DictToken(): 
    a = DictToken({}, 1, 2, 3)
    assert a.start == Position(1, 1, 1)
    assert a.end == Position(2, 3, 3)
    assert repr(a) == 'DictToken({})'
    assert a.value == {}
    print("Success: DictToken")
    

# Generated at 2022-06-14 15:02:18.759021
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(value={}, start_index=0, end_index=0, content="")
    assert token._value == {}
    assert token._start_index == 0
    assert token._end_index == 0
    assert token._content == ""


# Generated at 2022-06-14 15:02:25.662113
# Unit test for constructor of class DictToken
def test_DictToken():
    value = {ScalarToken(1, 0, 0): ScalarToken(2, 0, 0)}
    dt = DictToken(value, 1, 4, 'abc')
    assert dt._value == value
    assert dt._start_index == 1
    assert dt._end_index == 4
    assert dt._content == 'abc'


# Generated at 2022-06-14 15:02:26.953477
# Unit test for constructor of class DictToken
def test_DictToken():
    my_d = DictToken(value = 1, start_index = 2, end_index = 3)
    assert(isinstance(my_d._value, dict))

# Generated at 2022-06-14 15:03:21.644208
# Unit test for constructor of class DictToken
def test_DictToken():
    # test constructor with scalar tokens
    test_dict_token = DictToken(
        value={
            ScalarToken(1, 1, 2): ScalarToken(2, 3, 4),
            ScalarToken(2, 5, 6): ScalarToken(3, 7, 8),
        },
        start_index=1,
        end_index=8
    )
    assert test_dict_token.value == {1: 2, 2: 3}
    assert test_dict_token.start == Position(1, 1, 1)
    assert test_dict_token.end == Position(1, 9, 8)
    assert test_dict_token.lookup([]).value == {1: 2, 2: 3}
    assert test_dict_token.lookup([1]).value == 3
    assert test_dict_token.look

# Generated at 2022-06-14 15:03:22.605315
# Unit test for constructor of class DictToken
def test_DictToken():
    Token("foo", 1, 2)

# Generated at 2022-06-14 15:03:24.621007
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken({"a":1, "b":2}, 2, 4, "a=1|b=2")



# Generated at 2022-06-14 15:03:27.945078
# Unit test for constructor of class DictToken
def test_DictToken():
    x = DictToken({1: 2}, 0, 0, "")
    assert x.value == {1: 2}
    assert x.start == Position(1, 1, 0)
    assert x.end == Position(1, 1, 0)
    assert x.string == ""
    assert x.lookup([1]) == x._child_tokens[1]
    assert x.lookup_key([1]) == x._child_keys[1]


# Generated at 2022-06-14 15:03:31.685202
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {"a": 1, "b": 2}
    token = DictToken(d)
    assert token._child_keys.keys() == d.keys()
    assert token._child_tokens.keys() == d.keys()


# Generated at 2022-06-14 15:03:34.786857
# Unit test for constructor of class DictToken
def test_DictToken():
    s = '{a: 1, b: 2}'
    a = ScalarToken(1, 0, 0, s)
    b = ScalarToken(2, 0, 0, s)
    d = DictToken({a: a, b: b}, 0, 0, s)
    assert d.string == s


# Generated at 2022-06-14 15:03:39.707951
# Unit test for constructor of class DictToken
def test_DictToken():
    key_token = Token(1, 4, 7, "hallo")
    value_token = Token(2, 0, 3, "du")
    # call to constructor
    d = DictToken({key_token: value_token}, 0, 7, "hallodu")
    assert d._child_keys == {1: key_token}
    assert d._child_tokens == {1: value_token}



# Generated at 2022-06-14 15:03:43.762986
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({'hello': 'world'}, 0, 3)
    assert isinstance(a, DictToken)
    assert isinstance(a._child_keys, dict)
    assert isinstance(a._child_tokens, dict)


# Generated at 2022-06-14 15:03:53.582291
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem import types, validators
    from typesystem.base import ValidationError
    from typesystem.compat import Type

    class Author(types.Dict):
        name = types.String()
        id = types.Integer()

    class Book(types.Dict):
        title = types.String()
        author = Author()
        id = types.Integer()
        tags = types.Array(types.String())
        related = types.Array(types.Dict)


# Generated at 2022-06-14 15:03:54.958059
# Unit test for constructor of class DictToken
def test_DictToken():
    assert(DictToken)
    return


# Generated at 2022-06-14 15:04:57.590373
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({'x': ScalarToken(1, 0, 0), 'y': ScalarToken(2, 0, 0)}, 0, 0, '')
    assert token._child_keys == {'x': ScalarToken(1, 0, 0), 'y': ScalarToken(2, 0, 0)}, '_child_keys are wrong'
    assert token._child_tokens == {'x': ScalarToken(1, 0, 0), 'y': ScalarToken(2, 0, 0)}, '_child_tokens are wrong'


# Generated at 2022-06-14 15:05:04.018358
# Unit test for constructor of class DictToken
def test_DictToken():
    def __init__(self, *args: typing.Any, **kwargs: typing.Any) -> None:
        super().__init__(*args, **kwargs)
        self._child_keys = {k._value: k for k in self._value.keys()}
        self._child_tokens = {k._value: v for k, v in self._value.items()}

    assert(__init__( 3,2,1))


# Generated at 2022-06-14 15:05:07.044716
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(value={'key': 'value'}, start_index=1, end_index=2, content='content')
    assert(d._value == {'key': 'value'}), 'initialization should work'

# Generated at 2022-06-14 15:05:13.336875
# Unit test for constructor of class DictToken
def test_DictToken():
    content = '{"a": 1, "b": [1]}'
    start_index = 0
    end_index = len(content)-1
    dt = DictToken({"a": ScalarToken(1,2,3)}, start_index, end_index)
    assert(dt.start == Position(1,1,0))
    assert(dt.end == Position(1,13,12))
    # test repr
    assert(repr(dt) == "DictToken('{\"a\": 1, \"b\": [1]}')")

# Generated at 2022-06-14 15:05:16.288972
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken(1,2,3)
    DictToken(1,2,3, content='This is some test content')


# Generated at 2022-06-14 15:05:17.867821
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken(1, 2, 3, x=1, y=2)

# Generated at 2022-06-14 15:05:26.159018
# Unit test for constructor of class DictToken
def test_DictToken():
    '''
    test case for the constructer of DictToken class
    '''
    start_index = 4
    end_index = 9
    content = "hello world!"
    dic = {1:2, 3:4}
    token = DictToken(dic, start_index, end_index, content)
    assert token.start.index == start_index
    assert token.end.index == end_index
    assert token._content == content
    assert token._value == dic
    assert token._child_keys == {1: 2, 3: 4}
    assert token._child_tokens == {1: 2, 3: 4}


# Generated at 2022-06-14 15:05:27.246852
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken()


# Generated at 2022-06-14 15:05:34.433691
# Unit test for constructor of class DictToken
def test_DictToken():
    try :
        token=DictToken({1:'a',2:'b'})
    except NotImplementedError:
        print("NotImplementedError")
    else :
        assert(True)
try:
    token=DictToken({"a":1})
except NotImplementedError:
    print("NotImplementedError")
else :
    assert(True)


# Generated at 2022-06-14 15:05:42.171707
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(
        value={}, start_index=0, end_index=0, content="test content"
    )
    assert repr(token) == "DictToken('')"
    assert token._child_keys == {}
    assert token._child_tokens == {}
    assert token.string == ""
    assert token.value == {}
    assert token.start.line == 1
    assert token.start.column == 1
    assert token.start.index == 0
    assert token.end.line == 1
    assert token.end.column == 1
    assert token.end.index == 0
    assert token.lookup([]) is token
