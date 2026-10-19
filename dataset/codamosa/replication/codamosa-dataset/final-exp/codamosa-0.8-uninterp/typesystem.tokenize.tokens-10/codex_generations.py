

# Generated at 2022-06-14 14:56:29.444847
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(value=0, start_index=0, end_index=0) == Token(value=0, start_index=0, end_index=0)
    assert Token(value=0, start_index=0, end_index=0) != Token(value=0, start_index=0, end_index=1)
    assert Token(value=0, start_index=0, end_index=0) != Token(value=0, start_index=1, end_index=0)
    assert Token(value=0, start_index=0, end_index=0) != Token(value=1, start_index=0, end_index=0)
    assert Token(value="", start_index=0, end_index=0) != Token(value=0, start_index=0, end_index=0)


# Generated at 2022-06-14 14:56:35.295489
# Unit test for constructor of class DictToken
def test_DictToken():
    # Given
    class A:
        def __init__(self, value):
            self.value = value
    a = A("test")
    b = A("test2")
    # When
    token_dict = DictToken({a:b}, 0, 0)
    # Then
    assert token_dict._value == {a:b}
    assert token_dict._start_index == 0
    assert token_dict._end_index == 0
    assert token_dict._child_keys == {a:a}
    assert token_dict._child_tokens == {a:b}


# Generated at 2022-06-14 14:56:37.900757
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken(None, 1, 2) == ScalarToken(None, 1, 2)
    assert ScalarToken(None, 1, 2) != ScalarToken(None, 1, 2)
    assert ScalarToken(None, 1, 2) != ScalarToken(None, 1, 2)


# Generated at 2022-06-14 14:56:39.410068
# Unit test for constructor of class DictToken
def test_DictToken():
    o = DictToken({}, 0, 0)
    return o


# Generated at 2022-06-14 14:56:40.010887
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    print(Token.__eq__)



# Generated at 2022-06-14 14:56:41.145865
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    Token(value="", start_index=0, end_index=0, content="")



# Generated at 2022-06-14 14:56:45.869262
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    content = "123456789"
    token1 = Token(1, 2, 4, content)
    token2 = Token(2, 3, 5, content)
    assert token1 != token2
    token3 = Token(1, 2, 4, content)
    assert token1 == token3

# Generated at 2022-06-14 14:56:48.990859
# Unit test for constructor of class DictToken
def test_DictToken():
    a=DictToken((1,2,3,4,5,"a","b","c"),3,5)
    assert(a._get_value()==3 and a._start_index==1 and a._end_index==2)

# Generated at 2022-06-14 14:56:53.187160
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({"a":3, "b":4}, 0, 1, "this works")
    assert dt._child_tokens == {"a":3, "b":4}
    assert dt._child_keys == {"a":3, "b":4}


# Generated at 2022-06-14 14:56:58.533607
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1, 1, 1) == Token(1, 1, 1)
    assert not Token(1, 1, 1) == Token(2, 1, 1)
    assert not Token(1, 1, 1) == Token(1, 2, 1)
    assert not Token(1, 1, 1) == Token(1, 1, 2)
    assert not Token(1, 1, 1) == Token(1, 1, 1, "abc")
    assert not Token(1, 1, 1) == object


# Generated at 2022-06-14 14:57:09.186440
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Variable to store the result of the test
    res = None
    # Expected value
    expected = True

    # Call the function to test
    obj_test = Token(None, None, None)
    obj_other = Token(None, None, None)
    res = obj_test == obj_other

    # Compare the expected result with the result returned by the function
    assert res == expected



# Generated at 2022-06-14 14:57:11.620999
# Unit test for constructor of class DictToken
def test_DictToken():
    # test non-token input
    # test integer
    actual = DictToken(5, 0, 1)
    assert actual._value == 5


# Generated at 2022-06-14 14:57:22.950358
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(value=None, start_index=None, end_index=None) == Token(value=None, start_index=None, end_index=None)
    assert Token(value=None, start_index=None, end_index=None) != None
    assert Token(value=None, start_index=None, end_index=None) != 1
    assert Token(value=None, start_index=None, end_index=None) != "String"
    assert Token(value=None, start_index=None, end_index=None) != []
    assert Token(value=None, start_index=None, end_index=None) != ()
    assert Token(value=None, start_index=None, end_index=None) != {}

# Generated at 2022-06-14 14:57:26.413913
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    obj = Token(int(), int(), int())
    obj.__eq__(int())
    obj.__eq__(None)
    obj.__eq__(Token(int(), int(), int()))


# Generated at 2022-06-14 14:57:37.855382
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken(value={}, start_index=0, end_index=0, content="").value == {}
    assert DictToken(value={}, start_index=0, end_index=0, content="").start_index == 0
    assert DictToken(value={}, start_index=0, end_index=0, content="").end_index == 0
    assert DictToken(value={}, start_index=0, end_index=0, content="").content == ""
    assert DictToken(value={}, start_index=1, end_index=0, content="").value == {}
    assert DictToken(value={}, start_index=1, end_index=0, content="").start_index == 1
    assert DictToken(value={}, start_index=1, end_index=0, content="").end

# Generated at 2022-06-14 14:57:40.911732
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken(10, 10, 20, 'hello')
    assert d._value==10
    assert d._start_index==10
    assert d._end_index==20
    assert d._content=='hello'


# Generated at 2022-06-14 14:57:49.970423
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.parser.tokenizer import Tokenizer
    tokenizer = Tokenizer()
    # Init a sample dict to be tokenized
    sample_dict = {1:1}
    # `tokenize()` -> return a token object
    token_obj = tokenizer.tokenize(sample_dict)
    # Test if the token object is indeed a DictToken object
    assert isinstance(token_obj, DictToken)
    # Test the attributes of the token object
    assert token_obj._value == {1: 1}
    assert token_obj._child_keys == {1: 1}
    assert token_obj._child_tokens == {1: 1}


# Generated at 2022-06-14 14:57:52.789354
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {'x': 0, 'y': 7}
    assert DictToken(d, 0, 3, '{x:0, y:7}') == {'x': 0, 'y': 7}


# Generated at 2022-06-14 14:58:03.335052
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    Token_instance = Token(1, 2, 3)
    assert Token_instance == Token(1, 2, 3)
    assert not Token_instance == Token(1, 3, 4)
    assert Token_instance == ScalarToken(1, 2, 3)
    assert not Token_instance == ScalarToken(2, 2, 3)
    assert Token_instance == ListToken([], 2, 3)
    assert not Token_instance == ListToken([ScalarToken(2, 2, 3)], 2, 3)
    assert Token_instance == DictToken({}, 2, 3)
    assert not Token_instance == DictToken({ScalarToken(1, 2, 3): ScalarToken(2, 2, 3)}, 2, 3)

# Generated at 2022-06-14 14:58:06.301351
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token(1, 2, 3, "456")
    token2 = Token(1, 2, 3, "456")
    assert token1 == token2

# Generated at 2022-06-14 14:58:17.357581
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    a = ScalarToken(1, 0, 1)
    #
    # Call method __eq__ of class Token
    #
    # Create a new instance of class Token
    b = ScalarToken(2, 0, 1)
    # Call method __eq__ of class Token
    c = a.__eq__(b)
    # The return value of method __eq__ of class Token
    # is stored in variable c
    #
    # The value of variable c after calling method __eq__ of class Token 
    # is False
    assert c == False

# Generated at 2022-06-14 14:58:24.769909
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem.base import get_token_class
    from typesystem.base import Position

    Token = get_token_class()
    start_position = Position(1, 3, 3)
    end_position = Position(1, 4, 4)
    token = Token({}, start_position, end_position)
    assert token == token
    assert token != 1
    assert token != Token([], start_position, end_position)
    assert token != Token({}, Position(1, 2, 2), end_position)
    assert token != Token({}, start_position, Position(1, 5, 5))

# Generated at 2022-06-14 14:58:28.733367
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken({'hello':'world'}, 0, 0, 'hello')
    assert token._value == {'hello':'world'}
    assert token._start_index == 0
    assert token._end_index == 0
    assert token._content == 'hello'
    return None


# Generated at 2022-06-14 14:58:35.604458
# Unit test for method __eq__ of class Token
def test_Token___eq__():

    import unittest

    class TestToken___eq__(unittest.TestCase):

        def test_Token___eq__(self):
            a_token = Token("", 0, 3, "")
            self.assertTrue(a_token == a_token)
            self.assertFalse(a_token == 1)
            self.assertFalse(a_token == "")



# Generated at 2022-06-14 14:58:37.803377
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(0, 0, 1) == Token(0, 0, 1)
    


# Generated at 2022-06-14 14:58:44.157554
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    string = '{"key":"value"}'
    start_index = 0
    end_index = len(string) - 1
    token = Token(string, start_index, end_index)
    other_token = Token(string, start_index, end_index)
    assert token == other_token
    string = '{"key":"value"}'
    start_index = 0
    end_index = len(string) - 1
    token = Token(string, start_index, end_index)
    string = '{"key":"valu"}'
    start_index = 0
    end_index = len(string) - 1
    other_token = Token(string, start_index, end_index)
    assert token != other_token
    string = '{"key":"value"}'
    start_index = 1
    end_index = len

# Generated at 2022-06-14 14:58:48.004295
# Unit test for constructor of class DictToken
def test_DictToken():
    print("DictToken")
    x = dict()
    x[1] = 2
    dt = DictToken(x,1,2,3)
    assert dt is not None


# Generated at 2022-06-14 14:58:50.128414
# Unit test for constructor of class DictToken
def test_DictToken():
    dict_token = DictToken()
    assert isinstance(dict_token, DictToken)


# Generated at 2022-06-14 14:58:58.619279
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(
        value=42,
        start_index=0,
        end_index=1,
        content="42",
    ) == Token(
        value=42,
        start_index=0,
        end_index=1,
        content="42",
    )
    assert Token(
        value=42,
        start_index=0,
        end_index=1,
        content="42",
    ) != Token(
        value=1,
        start_index=0,
        end_index=1,
        content="42",
    )

# Generated at 2022-06-14 14:59:03.655264
# Unit test for constructor of class DictToken
def test_DictToken():
    assert(DictToken({"hello"}, 0, 0)._value == {"hello"})
    assert(DictToken({"hello"}, 0, 0, "he")._value == {"hello"})
    assert(DictToken({"hello"}, 0, 0, "hello")._value == {"hello"})



# Generated at 2022-06-14 14:59:17.652848
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken({'a':1},1,4)
    assert(repr(a)=="DictToken({'a': 1})")
    assert(a.start == Position(1,1,1))
    assert(a.end == Position(1,4,4))
    assert(a.lookup_key(['a'])==1)
    assert(a.lookup(['a'])==1)
    b = DictToken({"c":2},5,5)
    assert(a._get_value()=={'a': 1})
    assert(b._get_value()=={'c': 2})
    c = DictToken({'a':1, 'b':2, 'c':3},1,4)

# Generated at 2022-06-14 14:59:21.635496
# Unit test for constructor of class DictToken
def test_DictToken():
    class DummyThing:
        def __init__(self, key, value):
            self._value = key
            self._child_tokens = {k._value: v for k, v in value.items()}
    DictToken(DummyThing(2, {2: 3}))

# Generated at 2022-06-14 14:59:22.774580
# Unit test for constructor of class DictToken
def test_DictToken():
	assert_equal(1,1)

# Generated at 2022-06-14 14:59:26.249800
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {}
    e = DictToken(d,0,0)
    c = e.start
    a = e.end
    b = e.string
    f = e.value
    return


# Generated at 2022-06-14 14:59:31.888421
# Unit test for constructor of class DictToken
def test_DictToken():
    dic = {'a':1, 'b':2}
    t = DictToken(dic, 0,0, '')
    assert type(t.start) == Position
    assert type(t.end) == Position
    assert type(t.string) == str
    assert type(t._get_value()) == dict
    assert type(t._get_position(1)) == Position


# Generated at 2022-06-14 14:59:44.598310
# Unit test for constructor of class DictToken
def test_DictToken():
    line = '{"date1":"2020-04-01","date2":"2020-04-02"}'
    token1 = DictToken({"date1":"2020-04-01","date2":"2020-04-02"}, 0, 5, line)
    token2 = DictToken({"date1":"2020-04-01","date2":"2020-04-02"}, 0, 5, line)
    line = '{"date1":"2020-04-01","date2":"2020-04-02"}'
    token3 = DictToken({"date1":"2020-04-01","date2":"2020-04-02"}, 0, 5, line)
    line = '{"date1":"2020-04-01"}'
    token4 = DictToken({"date1":"2020-04-01"}, 0, 5, line)


# Generated at 2022-06-14 14:59:49.278861
# Unit test for constructor of class DictToken
def test_DictToken():
    key1 = ScalarToken('Class', 0, 5)
    value1 = ScalarToken('Student', 7, 13)
    value2 = ScalarToken('Teacher', 15, 21)
    token = DictToken({key1: value1, key2: value2}, 0, 21)
    return token.string == 'Class\nStudent\nTeacher'


# Generated at 2022-06-14 14:59:56.081027
# Unit test for constructor of class DictToken
def test_DictToken():
    pt = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    t = DictToken(pt, 3, 4, "abcd")
    assert t.value == {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert t.start == Position(1, 1, 3)
    assert t.end == Position(1, 5, 7)


# Generated at 2022-06-14 15:00:00.007105
# Unit test for constructor of class DictToken
def test_DictToken():
    class A:
        def __init__(self, a):
            self.a = a
    class B:
        def __init__(self, b):
            self.b = b
    d = DictToken(value = {A("hello"): B("world")}, start_index = 0, end_index = 100)
    assert(isinstance(d, DictToken))

# Generated at 2022-06-14 15:00:01.210809
# Unit test for constructor of class DictToken
def test_DictToken():
    assert DictToken.__init__ is not None



# Generated at 2022-06-14 15:00:09.998208
# Unit test for constructor of class Token
def test_Token():
    try:
        assert Token(True, 1, 2, 'string') == Token(True, 1, 2, 'string')
    except AssertionError:
        return False
    return True


# Generated at 2022-06-14 15:00:19.240592
# Unit test for constructor of class ListToken
def test_ListToken():

    l1 = ListToken(
        [
            ScalarToken(
                "Foo", start_index=0, end_index=2, content="Foo Bar"
            ),
            ScalarToken(
                "Bar", start_index=4, end_index=6, content="Foo Bar"
            ),
        ],
        start_index=0,
        end_index=6,
        content="Foo Bar"
    )
    assert l1._start_index == 0
    assert l1._end_index == 6
    assert l1._content == "Foo Bar"

# Generated at 2022-06-14 15:00:25.305381
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    token = ScalarToken(value = 10, start_index = 0, end_index = 0, content = "")
    assert repr(token) == "ScalarToken('10')"
    assert token.string == ''
    assert token.value == 10
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 1, 0)
    assert token.lookup([]) == token
    assert token.lookup_key([0]) == token


# Generated at 2022-06-14 15:00:27.971301
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    inst = ScalarToken(1, 1, 1)
    with pytest.raises(NotImplementedError) as err:
        inst.__hash__()
    assert not err.match(r"^.*is not implemented.*$")


# Generated at 2022-06-14 15:00:30.537638
# Unit test for constructor of class DictToken
def test_DictToken():
    # DictToken(1, 2, 3, 4)
    assert DictToken(1, 2, 3, 4)


# Generated at 2022-06-14 15:00:40.303338
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import MetadataToken
    from typesystem.types import String, Integer
    metadata = {"nullable": True}
    dictToken = DictToken({"name": ScalarToken("name", 3, 7), "age": ScalarToken(18, 9, 10)}, 0, 10, "name is 18")
    assert dictToken._value == {"name": ScalarToken("name", 3, 7), "age": ScalarToken(18, 9, 10)}
    assert dictToken._start_index == 0
    assert dictToken._end_index == 10
    assert dictToken._content == "name is 18"
    dictToken.lookup([0]) == ScalarToken("name", 3, 7)
    dictToken.lookup_key([0]) == ScalarToken("name", 3, 7)

# Generated at 2022-06-14 15:00:43.214487
# Unit test for constructor of class DictToken
def test_DictToken():
    dt = DictToken({"a":1}, 0, 10)
    assert dt.value == {"a":1}
    assert dt.string == "a"


# Generated at 2022-06-14 15:00:47.133288
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    """
    Method __hash__ of class ScalarToken return the object's hash value

    @return:
    """
    obj = ScalarToken(value=1, start_index=1, end_index=1)
    assert isinstance(hash(obj), int)



# Generated at 2022-06-14 15:00:54.364762
# Unit test for constructor of class Token
def test_Token():
    value = 'value'
    start_index = 1
    end_index = 1
    content = 'content'
    t = Token(value, start_index, end_index, content)
    assert t.string == value
    assert t.value == value
    assert isinstance(t.start,Position)
    assert isinstance(t.end,Position)
    assert t.lookup([]) == t
    assert t.lookup_key([]) == t


# Generated at 2022-06-14 15:01:05.139752
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    c1 = ListToken([1,2,3], 0, 7, '{"f1":[1,2,3]}')
    c2 = ListToken([1,2,3], 4, 6, '"f1":[1,2,3]')
    c3 = ScalarToken(1, 5, 5, '1,2,3')
    c4 = ScalarToken(2, 6, 6, '2,3')
    c5 = ScalarToken(3, 7, 7, '3')
    assert c1.lookup_key([0, 0]) == c3
    assert c1.lookup_key([0, 1]) == c4
    assert c1.lookup_key([0, 2]) == c5

# Generated at 2022-06-14 15:01:11.555190
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken(value = 1, start_index = 0, end_index = 3, content = "string")
    token2 = ScalarToken(value = 1, start_index = 0, end_index = 3, content = "string")
    assert token1.__eq__(token2), "Token.__eq__() method not working as intended"


# Generated at 2022-06-14 15:01:15.070755
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.parser import Parser
    from typesystem.parser.tests.data.validation_data import dict_schema
    parser = Parser()
    assert DictToken(parser.parse(dict_schema))
    return True


# Generated at 2022-06-14 15:01:19.078256
# Unit test for constructor of class Token
def test_Token():
    # Create tokens
    test_value = "test"
    test_start_index = 0
    test_end_index = 1
    test_content = "test"
    Token(test_value, test_start_index, test_end_index, test_content)
    return True


# Generated at 2022-06-14 15:01:29.985113
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    token1 = ScalarToken(value = 1, start_index = 0, end_index = 0, content = '')
    assert token1.string == ''
    assert token1.value == 1
    assert token1.start == Position(1, 1, 0)
    assert token1.end == Position(1, 1, 0)
    assert token1.lookup(index = None) == token1
    assert token1.lookup_key(index = None) == token1
    assert token1.__eq__(other = token1) == True
    assert token1.__repr__() == "ScalarToken('')"
    assert token1.__hash__() == hash(1)


# Generated at 2022-06-14 15:01:34.670324
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    # fixture
    content = "content"
    repr_result = "Token(content)"
    # test
    token = Token(None, 1, 2, content)
    # asserts
    assert token.__repr__() == repr_result



# Generated at 2022-06-14 15:01:38.371884
# Unit test for constructor of class ListToken
def test_ListToken():
    class Token:
        def _get_value(self):
            return []
    lst = []
    token = ListToken(lst, 0, 0)
    assert token._get_value() == []


# Generated at 2022-06-14 15:01:41.248290
# Unit test for constructor of class ListToken
def test_ListToken():
    input = [1, 2, 3]
    t = ListToken(input, 
            start_index = 0, 
            end_index = 2, 
            content = "")
    assert t.value == input

# Generated at 2022-06-14 15:01:48.622741
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    t0 = Token("ab", 0, 2, content="abc")
    t1 = Token("bc", 1, 3, content="abc")
    assert t0.lookup_key([0]) == t0
    assert t1.lookup_key([0]) == t1
    s0 = ScalarToken("ab", 0, 2, content="abc")
    s1 = ScalarToken("bc", 1, 3, content="abc")
    assert s0.lookup_key([0]) == s0
    assert s1.lookup_key([0]) == s1
    l0 = ListToken([t0, t1], 0, 4, content="abc")
    l1 = ListToken([s0, s1], 0, 4, content="abc")
    assert l0.lookup_key([0]) == t0
    assert l

# Generated at 2022-06-14 15:01:55.028736
# Unit test for constructor of class DictToken
def test_DictToken():
    # Arrange
    start_index=0
    end_index=1
    content="a"
    value={'a': 'b'}
    # Act
    dict=DictToken(value,start_index,end_index,content)
    # Assert
    assert dict._value=={'a': 'b'} and dict._start_index==0 and dict._end_index==1 and dict._content=="a"


# Generated at 2022-06-14 15:02:04.215817
# Unit test for constructor of class Token
def test_Token():
    token = Token(value = 1, start_index = 1, end_index = 2, content = "")
    assert token._get_value() == 1
    assert token._start_index == 1
    assert token._end_index == 2
    assert token._content == ""

    token = Token(value = "a", start_index = 1, end_index = 2, content = "")
    assert token._get_value() == "a"
    assert token._start_index == 1
    assert token._end_index == 2
    assert token._content == ""


# Generated at 2022-06-14 15:02:14.867890
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    from collections import namedtuple
    from jsonschema import validate
    from typesystem.structures import Structure, Dict, List
    from typesystem.tokenizers import tokenize
    from typesystem.references import Reference, ReferenceResolver
    from tests.test_references import (
        resolver,
        schema_refspec_str,
        schema_refspec_str_list,
        schema_refspec_str_dict,
    )

    class Company(Structure):
        name = Reference(schema_refspec_str, resolver)
        employees = Reference(schema_refspec_str_list, resolver)
        turnover = Reference(schema_refspec_str_dict, resolver)

    token = tokenize(Company, {"name": "Charmander"})

# Generated at 2022-06-14 15:02:18.664034
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {'a':1}
    token = DictToken(d,1,1)
    assert token.__class__.__name__ == 'DictToken'
    assert repr(token) == "DictToken({'a': 1})"


# Generated at 2022-06-14 15:02:25.660664
# Unit test for method lookup of class Token
def test_Token_lookup():
    tmp=Token(value=0, start_index=0, end_index=1)
    with pytest.raises(NotImplementedError):
        tmp.lookup(index=[])
    with pytest.raises(NotImplementedError):
        tmp.lookup_key(index=[])
    
# test for method __init__ of class Token

# Generated at 2022-06-14 15:02:29.691435
# Unit test for method lookup of class Token
def test_Token_lookup():
    token = Token(None, 0, 1)
    try:
        token.lookup(0)
    except Exception as e:
        print(e)
        print("Method lookup of Token is not implemented")
    else:
        print("Method lookup of Token is implemented")



# Generated at 2022-06-14 15:02:40.856740
# Unit test for constructor of class Token
def test_Token():
    token1 = Token(1, 2, 3)
    assert token1.string == ''
    assert token1.value == None
    assert token1.start == Position(1,1,2)
    assert token1.end == Position(1,1,3)
    assert token1._get_position(0) == Position(1, 1, 0)
    assert str(token1) == "Token('')"
    assert token1 == token1
    assert token1 != 1
    assert token1 != Token(1, 0, 0)
    assert token1 != Token(2, 2, 3)
    assert token1 != Token(1, 1, 3)
    assert token1 != Token(1, 2, 4)


# Generated at 2022-06-14 15:02:43.261598
# Unit test for constructor of class ListToken
def test_ListToken():
    list = ListToken([1,"2",3,"4"],3)
    assert (list._value == [1,"2",3,"4"])

# Generated at 2022-06-14 15:02:43.794946
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    pass

# Generated at 2022-06-14 15:02:45.476349
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    # TODO: need to implement
    assert True



# Generated at 2022-06-14 15:02:56.251513
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    from src.parser.parser import Parser
    from src.parser.tokenizer import Tokenizer
    from src.sql.tokenizer import SqlTokenizer
    from src.sql.parse_tree import SqlParseTree

    q = """
    CREATE TABLE `tbl_name` (
    `a` int
    );
    """

    # transfer the string query into tokens, which is an instance of type Token
    s = SqlTokenizer(q)
    token = s.tokenize()

    # transfer the tokens into a parse tree, which is an instance of type SqlParseTree
    parser = Parser(token)
    p = parser.parse()

    # convert the parse tree into a dictionary
    p.to_dict()

    # test using the method lookup_key of class Token

# Generated at 2022-06-14 15:03:00.641708
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token1 = ScalarToken(1, 1, 3)
    token2 = ScalarToken("abc", 4, 6)
    _1 = token1.__repr__()
    _2 = token2.__repr__()
    assert (_1 == "ScalarToken('1')")
    assert (_2 == "ScalarToken('abc')")


# Generated at 2022-06-14 15:03:09.340644
# Unit test for constructor of class DictToken
def test_DictToken():
    DictToken("one", "two", "three", "four", "five")

# Generated at 2022-06-14 15:03:16.349771
# Unit test for constructor of class ListToken
def test_ListToken():
    parent_index = 0
    parent_content = ''
    parent_value = [1, 2, 3]
    parent_class = ListToken(parent_value, parent_index, parent_index, parent_content)
    assert parent_class._value == parent_value
    assert parent_class._start_index == parent_index
    assert parent_class._end_index == parent_index
    assert parent_class._content == parent_content


# Generated at 2022-06-14 15:03:22.420669
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    sol_tok1 = ScalarToken(7, 1, 4)
    sol_tok2 = ScalarToken(7, 1, 4)
    assert hash(sol_tok1) == hash(sol_tok2)
    sol_tok3 = ScalarToken(8, 1, 4)
    assert hash(sol_tok1) != hash(sol_tok3)


# Generated at 2022-06-14 15:03:32.708656
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    print("test_Token_lookup_key")
    if True:
        # Working of method Token.lookup_key
        # with the example of a dictionary
        json_dict = {'a': 1, 'b': 2, 'c': 3}
        # The following list is a list of nested list.
        # The sublists represent the indices of a nested dictionary.
        list_indices = [['a'],['b'],['c']]
        # Looping over all the keys in the dictionary and then
        # calculating the position of the key

# Generated at 2022-06-14 15:03:39.160738
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    t = Token(None, None, None, content='abc')
    t._get_position = lambda i: Position(1, 1, i)
    t._get_value = lambda: None
    assert t.lookup_key([]) == t
    t._get_child_token = lambda i: Token(None, None, None, content='abc')
    t._get_key_token = lambda i: Token(None, None, None, content='abc')
    assert t.lookup_key([0]) == Token(None, None, None, content='abc')

# Generated at 2022-06-14 15:03:41.638423
# Unit test for constructor of class DictToken
def test_DictToken():
    d = DictToken({1: 1, 2: 2}, 0, 4, "")
    #assert token == token1
    return d



# Generated at 2022-06-14 15:03:43.469589
# Unit test for method __repr__ of class Token
def test_Token___repr__():
    token = Token(None, 10, 20)
    assert token.__repr__() == "Token('')"

# Generated at 2022-06-14 15:03:53.376248
# Unit test for constructor of class ListToken
def test_ListToken():
    from typesystem import String, ListOf
    from typesystem.base import Position
    list_of_string = ListOf(String())
    input = ['foo', 'bar', 'baz']
    result = list_of_string.validate(input)
    assert (result.is_valid() == True)
    assert (result.raw_tokens is not None)
    assert (len(result.raw_tokens) == 3)
    assert (type(result.raw_tokens[0]) == ScalarToken)
    assert (type(result.raw_tokens[1]) == ScalarToken)
    assert (type(result.raw_tokens[2]) == ScalarToken)
    assert (result.raw_tokens[0].value == 'foo')

# Generated at 2022-06-14 15:03:56.997441
# Unit test for constructor of class Token
def test_Token(): # pragma nocover
    t0 = Token(2, 3, 4, content='a')
    t1 = Token(3, 4, 5, content='b')
    assert t0.value == 2
    assert t1.string == 'b'

# Generated at 2022-06-14 15:04:07.925662
# Unit test for constructor of class ListToken
def test_ListToken():
    from typesystem.base import Token

    # create the children
    child_value = "Hello"
    child_start_index = 0
    child_end_index = 5
    child_content = "Hello"
    child_token = Token(
        child_value, child_start_index, child_end_index, child_content
    )

    # Test the parent
    parent_value = [child_token]

    parent_start_index = 0
    parent_end_index = 5
    parent_content = "Hello"

    parent = ListToken(
        parent_value, parent_start_index, parent_end_index, parent_content
    )

    assert parent.string == "Hello"
    assert parent.value == ["Hello"]
    assert parent.start.index == 0
    assert parent.end.index == 5

   

# Generated at 2022-06-14 15:04:28.697212
# Unit test for constructor of class ListToken
def test_ListToken():
    string = '123'
    start_index = 0
    end_index = 2
    content = 'abc'
    token = ListToken(string, start_index, end_index, content)
    assert token.string == string, f"token.string == '{token.string}', it should be '{string}'"
    assert token.start == start_index, f"token.start == '{token.start}', it should be '{start_index}'"
    assert token.end == end_index, f"token.end == '{token.end}', it should be '{end_index}'"
    print(token.value)


test_ListToken()

# Generated at 2022-06-14 15:04:32.985359
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    # Pass
    token = ScalarToken(value = None, start_index = 0, end_index = 0, content = None)
    # noinspection PyUnresolvedReferences
    assert hash(token) == hash(None)
    

# Generated at 2022-06-14 15:04:36.940163
# Unit test for constructor of class ListToken
def test_ListToken():
    value = ['a','b','c']
    start_index = 0
    end_index = 2
    content = ""
    def test():
        l_token = ListToken(value,start_index,end_index,content)
    test()
    return "pass"


# Generated at 2022-06-14 15:04:45.555919
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    def assertEqual(x, y):
        assert x == y
        print("Passed")
        return True

    test_cases = [
        ([1, 2, 3, 4], [(0, 1), (2, 3), (1, 2)]),
        ([(0, 1), (2, 3), (1, 2)], [(-1, 0), (0, 1), (1, 2)]),
    ]

    for x, y in test_cases:
        assertEqual(Token.lookup_key(x), y)

if __name__ == "__main__":
    print("Testing")
    test_Token_lookup_key()
    print("Done")

# Generated at 2022-06-14 15:04:47.710466
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    token = ScalarToken(1, 0, 0)
    assert token.__hash__() == 1


# Generated at 2022-06-14 15:04:55.417873
# Unit test for constructor of class ScalarToken
def test_ScalarToken():
    start_index = 0
    end_index = 1
    content = ""
    string = ""
    value = 0

    token = ScalarToken(value, start_index, end_index, content)
    print(token)

    assert token.string == string
    assert token.value == value
    assert token.start == Position(1, 1, 0)
    assert token.end  == Position(1, 2, 1)
    assert token.lookup([]) == token
    assert token.lookup_key([]) == token


# Generated at 2022-06-14 15:05:06.138612
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem import Number, String
    from typesystem.parser import Token, JSONParser

    values = {
        "String": "abc",
        "Number": 123,
        "List of Strings": ["a", "b", "c"],
        "List of Numbers": [1, 2, 3],
        "List of Strings and Numbers": ["a", "b", 1, 2, 3],
        "Dictionary 1": {"a": 1, "b": 2},
        "Dictionary 2": {"a": 1, "b": "2"},
    }

    for key, value in values.items():
        tokens = JSONParser(String()).parse(json.dumps(value))
        assert tokens == tokens, key
        tokens2 = JSONParser(Number()).parse(json.dumps(value))
        assert tokens != tokens2, key


# Generated at 2022-06-14 15:05:10.869963
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    # Setup
    args = [
        None,
        0,
        0,
        0,
        ''
    ]
    s_token = ScalarToken(*args)
    expected_return = hash(args[0])

    # Exercise
    actual_return = s_token.__hash__()

    # Verify
    assert expected_return == actual_return



# Generated at 2022-06-14 15:05:14.650311
# Unit test for constructor of class ListToken
def test_ListToken():
    a = ListToken([1,2,3], 0, 5, "0 + 1 + 2 + 3")
    assert(a._get_value() == [1,2,3])


# Generated at 2022-06-14 15:05:17.331377
# Unit test for method lookup of class Token
def test_Token_lookup():
    t = Token(None, None, None)
    assert t.lookup([]).__class__ == Token


# Generated at 2022-06-14 15:05:35.073009
# Unit test for method __hash__ of class ScalarToken
def test_ScalarToken___hash__():
    _token_ = ScalarToken("value", "start_index", "end_index", "content")
    _value = _token_._get_value()
    _expected = hash(_value)
    _result = hash(_token_)
    assert _result == _expected, 'Got {0}, expecting {1}'.format(_result, _expected)


# Generated at 2022-06-14 15:05:43.993876
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(None, 0, 10).__eq__(Token(None, 0, 10)) == True
    assert Token(None, 1, 10).__eq__(Token(None, 0, 10)) == False
    assert Token(None, 0, 10).__eq__(Token(None, 1, 10)) == False
    assert Token(None, 0, 10).__eq__(Token(True, 0, 10)) == False
    assert Token(True, 0, 10).__eq__(Token(True, 1, 10)) == False
    assert Token(True, 1, 10).__eq__(Token(True, 0, 10)) == False
    assert Token(True, 0, 10).__eq__(Token(True, 0, 11)) == False
    assert Token(True, 0, 10).__eq__(Token(True, 0, 9)) == False

# Generated at 2022-06-14 15:05:48.867164
# Unit test for constructor of class Token
def test_Token():
    s = "hello"
    to = Token(value = s,start_index = 2,end_index = 3 ,content = s)
    assert(to._value == s)
    assert(to._start_index == 2)
    assert(to._end_index == 3)
    assert(to._content == s)
    assert(to.string == s[to._start_index : to._end_index + 1])


# Generated at 2022-06-14 15:05:50.288802
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(None, 0, 0) == Token(None, 0, 0)

# Generated at 2022-06-14 15:06:00.571111
# Unit test for constructor of class Token
def test_Token():
    # test constructor with different inputs
    token = Token(1, 0, 4, "hello")
    assert token._value == 1
    assert token._start_index == 0
    assert token._end_index == 4
    assert token._content == "hello"
    assert repr(token) == "Token(hello)"
    assert token == Token(1, 0, 4, "hello")
    assert not token == Token(1, 0, 4, "world")
    assert not token == Token(1, 1, 4, "hello")
    assert not token == Token(1, 0, 3, "hello")
    assert not token == Token(2, 0, 4, "hello")


# Generated at 2022-06-14 15:06:05.114513
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    dict_token = DictToken({'item': 'value'}, 0, 3, '{"item":"value"}')
    print(dict_token.lookup_key([0]))
    # Should print: Token(item)
    print(dict_token.lookup_key([0, 'item']))
    # Should print: ScalarToken(value)

test_Token_lookup_key()

# Generated at 2022-06-14 15:06:07.051635
# Unit test for constructor of class DictToken
def test_DictToken():
    dict = DictToken({}, -1, -1, '')
    assert dict.start == dict.end
    assert dict.string == ''

# Generated at 2022-06-14 15:06:16.425625
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    tk = Token(1, 1, 1)
    tk1 = Token(1, 1, 1)
    tk2 = Token(1, 1, 2)
    tk3 = Token(2, 1, 1)
    tk4 = Token(1, 2, 1)
    tk5 = Token(2, 2, 1)
    tk6 = Token(1, 1, 1, "")
    assert tk == tk1
    assert tk != tk2
    assert tk != tk3
    assert tk != tk4
    assert tk != tk5
    assert tk == tk6

test_Token___eq__()
