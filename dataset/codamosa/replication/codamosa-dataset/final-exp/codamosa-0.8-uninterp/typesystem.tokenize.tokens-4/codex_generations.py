

# Generated at 2022-06-14 14:56:25.050064
# Unit test for constructor of class DictToken
def test_DictToken():
    '''
    _start_index = 0
    _end_index = 1
    _content = "{"
    _child_keys = {'k': 0}
    _child_tokens = {'k1': None}
    '''
    a = DictToken({"k": 0, "k1": None}, 0, 1, "{")
    assert a._child_keys == {'k': 0}
    assert a._child_tokens == {'k': 0, 'k1': None}

# Generated at 2022-06-14 14:56:28.567771
# Unit test for constructor of class DictToken
def test_DictToken():
    # test case: constructor of class DictToken
    print("test case: constructor of class DictToken")
    dict = {1: 2, 'a': 'b'}
    dicttoken = DictToken(dict, 0, 10, '{"a": "b", 1: 2}')
    print(dicttoken)


# Generated at 2022-06-14 14:56:32.853766
# Unit test for constructor of class DictToken
def test_DictToken():
    # Base test
    dt1 = DictToken({"a": "b"}, 1, 3)
    assert dt1._child_keys == {"a": ('a', 1, 1)}
    assert dt1._child_tokens == {"a": 'b'}

    dt2 = ListToken(ListToken(2), 3, 7)
    assert dt2._value == 2


# Generated at 2022-06-14 14:56:44.572330
# Unit test for constructor of class DictToken
def test_DictToken():
    def test_ok1():
        # OK
        a = DictToken({"a": 1, "b": 2}, 1, 5)
        print(repr(a._value))
        print(repr(a.value))
        assert repr(a._value) == repr(a.value)
        # repr(a.value)
        # assert repr(a.value) == "{'a': 1, 'b': 2}"

    test_ok1()

    def test_ok2():
        # OK
        def dict_token(a: dict, b: int, c: int) -> DictToken:
            return DictToken(a, b, c)
        a = dict_token({"a": 1, "b": 2}, 1, 5)
        assert repr(a._value) == repr(a.value)

    test

# Generated at 2022-06-14 14:56:49.857181
# Unit test for constructor of class DictToken
def test_DictToken():
    # create token objects
    key_token = ScalarToken('a', 1, 2)
    value_token = ScalarToken('b', 3, 4)
    # create a dict token
    token = DictToken({key_token: value_token}, 5, 6)
    # compare the dict token to the expected result
    expected = DictToken({key_token: value_token}, 5, 6)
    assert token == expected


# Generated at 2022-06-14 14:56:52.304773
# Unit test for constructor of class DictToken
def test_DictToken():
    a = DictToken(**{'value': {'b': 'c'}, 'start_index': 0, 'end_index': 1, 'content': ''})
    print(a.value)

test_DictToken()

# Generated at 2022-06-14 14:56:58.708381
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(value=None,start_index=None,end_index=None,content=None)==Token(value=None,start_index=None,end_index=None,content=None)
    assert not Token(value=None,start_index=None,end_index=None,content=None)==Token(value=None,start_index=None,end_index=None,content="")
    assert not Token(value=None,start_index=None,end_index=None,content=None)==Token(value=None,start_index=None,end_index=None)


# Generated at 2022-06-14 14:57:07.213605
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    line_0 = ("{", 0, 0)
    line_1 = ("}", 4, 4)
    line_2 = (" ", 1, 2)
    line_3 = ("-", 3, 3)
    line_4 = (" ", 1, 2)
    line_5 = ("-", 3, 3)
    line_list = [line_0, line_1, line_2, line_3, line_4, line_5]
    content = content = "{\n  -\n  -\n}"
    start_index = line_0[1]
    end_index = line_1[2]
    value = value = {"": [{"": []}, {"": []}]}

    token = Token(value, start_index, end_index, content)

# Generated at 2022-06-14 14:57:10.903343
# Unit test for constructor of class DictToken
def test_DictToken():
    d = {"a": "1"}
    t = DictToken(d, 0, 1, "")
    assert t.value == d
    assert t.start == Position(1, 1, 0)
    assert t.end == Position(1, 1, 0)

# Generated at 2022-06-14 14:57:14.838947
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Since Token is an abstract class, we will test it
    # by creating a subclass.
    class SubToken(Token):
        def __init__(self, x):
            super().__init__(x, 4, 9, 'test_string')

    t1 = SubToken(4)
    t2 = SubToken(4)

    assert t1 == t2

# Generated at 2022-06-14 14:57:22.499950
# Unit test for constructor of class DictToken
def test_DictToken():
    # DictToken -> Token -> object
    x = DictToken(value = {'key': 'value'}, start_index = 5, end_index = 9, content = 'content')
    assert(x._get_value() == {'key': 'value'})

 

# Generated at 2022-06-14 14:57:29.432589
# Unit test for constructor of class DictToken
def test_DictToken():
    a = {
        ScalarToken(1, 0, 0): ScalarToken(1, 0, 0),
        ScalarToken(2, 0, 0): ScalarToken(2, 0, 0),
    }
    assert DictToken(a, 0, 0)._value == {
        ScalarToken(1, 0, 0): ScalarToken(1, 0, 0),
        ScalarToken(2, 0, 0): ScalarToken(2, 0, 0),
    }


# Generated at 2022-06-14 14:57:40.666388
# Unit test for constructor of class DictToken
def test_DictToken():
    ex1 = {'a':2}
    ex2 = {'b':3}
    ex3 = {'c':4}
    ex4 = {'d':5}
    tk1 = DictToken(value=ex1,start_index=1,end_index=2)
    tk2 = DictToken(value=ex2,start_index=1,end_index=2)
    tk3 = DictToken(value=ex3,start_index=1,end_index=2)
    tk4 = DictToken(value=ex4,start_index=1,end_index=2)
    tk5 = DictToken(value={tk1:tk2,tk3:tk4},start_index=1,end_index=2)


# Generated at 2022-06-14 14:57:51.151233
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Token.
    value1 = 1
    start_index1 = 2
    end_index1 = 3
    content1 = "12345"
    token1 = Token(
        value=value1, start_index=start_index1, end_index=end_index1, content=content1
    )
    value2 = 1
    start_index2 = 2
    end_index2 = 3
    content2 = "12345"
    token2 = Token(
        value=value2, start_index=start_index2, end_index=end_index2, content=content2
    )
    assert token1 == token2

    # ScalarToken.
    value3 = 1
    start_index3 = 2
    end_index3 = 3
    content3 = "12345"

# Generated at 2022-06-14 14:57:55.290464
# Unit test for constructor of class DictToken
def test_DictToken():
    content = "{'a': 1, 'b': 2}"
    token = DictToken("value", 0, len(content), content)
    assert token._start_index == 0 and token._end_index == len(content)
    assert token._content == content
    assert token._value == "{'a': 1, 'b': 2}"


# Generated at 2022-06-14 14:58:03.836169
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    print('how to get coverage for a function that has not been called yet?')
    import sys
    cls = sys.modules[__name__]
    for name, obj in cls.__dict__.items():
        if isinstance(obj, type):
            print(name)
            token = obj(None, None, None)
            token2 = None
            try:
                token == token2
            except NotImplementedError:
                pass
            else:
                assert False, 'unexpectedly equal!'


# unit test for method __hash__ of class ScalarToken

# Generated at 2022-06-14 14:58:13.724969
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    not_self_0 = ScalarToken(1234, 1, 2)
    not_self_1 = ScalarToken(1234, 2, 3)
    not_self_2 = ScalarToken(1234, 3, 4)
    self_0 = ScalarToken(1234, 1, 2)
    self_1 = ScalarToken(1234, 2, 3)
    self_2 = ScalarToken(1234, 3, 4)
    assert not_self_0 == self_0
    assert not_self_1 == self_1
    assert not_self_2 == self_2
    assert not (not_self_0 != self_0)
    assert not (not_self_1 != self_1)
    assert not (not_self_2 != self_2)
# test_Token___eq__()

# Generated at 2022-06-14 14:58:24.525397
# Unit test for constructor of class DictToken
def test_DictToken():
    from typesystem.base import String, Integer, Object, Array
    identity_schema = Object(
        properties={
            "first_name": String(max_length=30),
            "last_name": String(max_length=30),
            "age": Integer(minimum=0),
            "children": Array(items=Object(properties={"name": String(max_length=30)}))
        }
    )
    content = '''{
    "first_name": "Jane",
    "last_name": "Doe",
    "age": 35,
    "children": [
        {"name": "Jane Jr"},
        {"name": "Junior"}
    ]
}'''
    token = identity_schema.deserialize(content)
    assert isinstance(token, DictToken)
    assert token.lookup

# Generated at 2022-06-14 14:58:30.292943
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Setup
    value1 = 'the_value1'
    start_index = 0
    end_index = len(value1) - 1
    content = "the_value1 the_value2"
    token1 = Token(value1, start_index, end_index, content)
    value2 = 'the_value1'
    start_index = 0
    end_index = len(value2) - 1
    content = "the_value1 the_value2"
    token2 = Token(value2, start_index, end_index, content)
    expected = True
    # Exercise
    result = token1.__eq__(token2)
    # Verify
    assert result == expected



# Generated at 2022-06-14 14:58:40.422885
# Unit test for constructor of class DictToken
def test_DictToken():
    # set up test variables
    key_token1 = Token("a", 0, 0, content="a")
    key_token2 = Token("b", 0, 0, content="a")
    value_token1 = Token("a", 0, 0, content="a")
    value_token2 = Token("b", 0, 0, content="a")
    key_value_pair1 = (key_token1, value_token1)
    key_value_pair2 = (key_token2, value_token2)
    iterable = [key_value_pair1, key_value_pair2]
    # create the object
    a = DictToken(dict(), 0, 0, "a")
    # compare current result with expected result
    assert a

# Generated at 2022-06-14 14:58:55.205351
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(1, 2, 3)
    t2 = Token(2, 3, 4)
    t3 = Token(1, 2, 3)
    assert not (t1 == t2)
    assert (t1 == t3)


# Generated at 2022-06-14 14:59:07.515785
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import typesystem
    import typesystem.base

    # Make scalar tokens
    t1 = typesystem.scalar_token("a-string", 0, 8)
    t2 = typesystem.scalar_token("another-string", 0, 14)
    t3 = typesystem.scalar_token(True, 0, 4)
    t4 = typesystem.scalar_token(1, 0, 1)
    t5 = typesystem.scalar_token(1.2, 0, 3)
    t6 = typesystem.scalar_token(typesystem.base.Position(1, 1, 1), 0, 4)
    t7 = typesystem.scalar_token(None, 0, 2)

    # Try equality of different types
    assert t1 == t1

# Generated at 2022-06-14 14:59:13.794470
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken(_value=123, start_index=2, end_index=3, content="")
    print(token1.__class__)
    print(token1.__class__.__name__)
    print(repr(token1))
    print(repr(token1.string))
    print(token1.value)
    print(token1.start)
    print(token1.end)
    print(token1._get_value())
    print(token1._value)
    print(token1._start_index)
    print(token1._end_index)
    print(token1._content)
    print(token1.__class__.__name__)


test_Token___eq__()

# Generated at 2022-06-14 14:59:17.567468
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token(value = "test", start_index = 1, end_index = 2)
    other = Token(value = "test", start_index = 1, end_index = 2)
    result = token.__eq__(other)
    assert result is True

# Generated at 2022-06-14 14:59:25.612358
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken('a', 0, 0, 'a') == ScalarToken('a', 0, 0, 'a') is True
    assert DictToken({}, 0, 0, '{}') == DictToken({}, 0, 0, '{}') is True
    assert ListToken([], 0, 0, '[]') == ListToken([], 0, 0, '[]') is True
    assert ScalarToken('a', 0, 0, 'a') == ScalarToken('b', 1, 1, 'b') is False
    assert DictToken({}, 0, 0, '{}') == DictToken({'a': 1}, 0, 0, '{a: 1}') is False
    assert ListToken([], 0, 0, '[]') == ListToken(['a'], 0, 0, '["a"]') is False

# Generated at 2022-06-14 14:59:30.757873
# Unit test for constructor of class DictToken
def test_DictToken():
    json_dict = {'name': 'zhangsan', 'age': 35}
    token = DictToken(value=json_dict)
    assert isinstance(token, DictToken)
    print("test_DictToken OK")

if __name__ == '__main__':
    test_DictToken()

# Generated at 2022-06-14 14:59:43.160540
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token("", 0, 0) == Token("", 0, 0)
    assert Token("", 1, 2) == Token("", 1, 2)
    assert not Token("", 1, 2) == Token("", 2, 1)
    assert not Token("", 1, 2) == Token("", 2, 2)
    assert not Token("", 1, 2) == Token("", 1, 1)
    assert Token("foo", 0, 2) == Token("foo", 0, 2)
    assert not Token("foo", 1, 2) == Token("foo", 0, 2)
    assert not Token("foo", 1, 2) == Token("foo", 1, 3)
    assert not Token("foo", 1, 2) == Token("foo", 0, 3)
    assert not Token("foo", 1, 2) == Token("foo", 1, 1)

# Generated at 2022-06-14 14:59:51.816293
# Unit test for method __eq__ of class Token

# Generated at 2022-06-14 14:59:54.635859
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(None,0,0) == Token(None,0,0)
    assert not Token(None,0,0) == Token(None,1,1)

# Generated at 2022-06-14 14:59:57.005495
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token("a", 1, 2, "abc")
    assert token._get_position(1) == Position(1, 1, 1)

# Generated at 2022-06-14 15:00:15.605634
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 0
    end_index = 0
    content = "Hello"
    value = 'A'
    value1 = 'A'
    value2 = 'B'
    token = Token(value, start_index, end_index, content)
    token1 = Token(value1, start_index, end_index, content)
    token2 = Token(value2, start_index, end_index, content)
    print(repr(token) == repr(token1), repr(token), repr(token1))
    print(repr(token) == repr(token2), repr(token), repr(token2))

# Generated at 2022-06-14 15:00:19.211679
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    input_string = "Test"
    t = ScalarToken(input_string, 0, len(input_string) - 1, content = input_string)
    assert(t == t)



# Generated at 2022-06-14 15:00:23.210137
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    value = 42
    start_index = 23
    end_index = 23
    t1 = ScalarToken(value, start_index, end_index)
    t2 = ScalarToken(value, start_index, end_index)
    assert (t1 == t2)



# Generated at 2022-06-14 15:00:27.945510
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(
        value="abc", start_index=1, end_index=3
    ) == Token(
        value="abc", start_index=1, end_index=3
    )
    assert Token(
        value="abc", start_index=1, end_index=3
    ) == Token(
        value="abc", start_index=1, end_index=3, content="a"
    )

test_Token___eq__()

# Generated at 2022-06-14 15:00:29.204532
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass


# Generated at 2022-06-14 15:00:39.595446
# Unit test for method __eq__ of class Token
def test_Token___eq__():

    from typesystem import Token, ScalarToken, ListToken, DictToken

    instance_1 = ScalarToken(value=1, start_index=0, end_index=1, content="2")
    instance_2 = ScalarToken(value=1, start_index=0, end_index=1, content="2")
    assert instance_1 == instance_2

    instance_1 = ScalarToken(value=1, start_index=0, end_index=1, content="2")
    instance_2 = ScalarToken(value=2, start_index=0, end_index=1, content="2")
    assert instance_1 != instance_2

    instance_1 = ScalarToken(value=1, start_index=0, end_index=1, content="2")

# Generated at 2022-06-14 15:00:49.806837
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from copy import deepcopy
    from typesystem.base import Error

    foo1 = Error("my string", "my value")
    foo2 = deepcopy(foo1)

    assert foo1 == foo1
    assert foo1 == foo2
    assert foo2 == foo1
    assert foo2 == foo2
    assert foo1.start_index == foo2.start_index
    assert foo1.end_index == foo2.end_index
    assert foo2.start_index == foo1.start_index
    assert foo2.end_index == foo1.end_index
    assert foo1.start_line == foo2.start_line
    assert foo1.start_column == foo2.start_column
    assert foo2.start_line == foo1.start_line
    assert foo2.start_column == foo1.start_

# Generated at 2022-06-14 15:01:02.188148
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken(1, 2, 3) == ScalarToken(1, 2, 3)
    assert ScalarToken(1, 2, 3) != ScalarToken(2, 2, 3)
    assert ScalarToken(1, 2, 3) != ScalarToken(1, 3, 3)
    assert ScalarToken(1, 2, 3) != ScalarToken(1, 2, 4)
    assert ScalarToken(1, 2, 3) != DictToken({}, 2, 3)
    assert ScalarToken(1, 2, 3) != ListToken([], 2, 3)
    assert DictToken({}, 2, 3) != ListToken([], 2, 3)
    assert not ScalarToken(1, 2, 3) == DictToken({}, 2, 3)
    assert not ScalarToken(1, 2, 3)

# Generated at 2022-06-14 15:01:04.181409
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = Token( 0.0, 0, 0, "" )
    if( not( token1.__eq__(token1) ) ):
        print('Failed test_Token___eq__')
        return



# Generated at 2022-06-14 15:01:11.073306
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    a = Token(1, 2, 3)
    b = Token(1, 2, 3)
    assert a == b # True
    a = Token(1, 2, 3)
    b = Token(2, 2, 3)
    assert a == b # False
    a = Token(1, 2, 3)
    b = Token(1, 3, 3)
    assert a == b # False
    a = Token(1, 2, 3)
    b = Token(1, 2, 4)
    assert a == b # False

# Generated at 2022-06-14 15:01:22.336264
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass


# Generated at 2022-06-14 15:01:23.034972
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass

# Generated at 2022-06-14 15:01:33.108398
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(0, 0, 0) == Token(0, 0, 0)
    assert not Token(0, 0, 0) == Token(0, 0, 1)
    assert not Token(0, 0, 0) == Token(0, 1, 0)
    assert not Token(0, 0, 0) == Token(1, 0, 0)
    assert not Token(0, 0, 0) == object()
    assert scalar_token == scalar_token
    assert scalar_token != not_scalar_token
    assert not_scalar_token == not_scalar_token
    assert not_scalar_token != scalar_token

# Generated at 2022-06-14 15:01:43.968753
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    obj = Token(None, 0, 0, "")
    assert obj == obj

    obj = Token(None, 0, 0, "")
    assert not obj == None
    assert not obj == 'String'
    assert not obj == (1, 2, 3)
    assert not obj == []
    assert not obj == {}
    assert not obj == object()

    obj = Token(None, 0, 0, "")
    assert not obj == Token(None, 0, 0, "")

    obj = Token(None, 1, 1, "")
    assert not obj == Token(None, 1, 1, "")

    obj = Token(None, 1, 2, "")
    assert not obj == Token(None, 1, 2, "")

    obj = Token(False, 0, 0, "")

# Generated at 2022-06-14 15:01:55.600389
# Unit test for constructor of class DictToken
def test_DictToken():
    try:
        with pytest.raises(NotImplementedError):
            x = Token(1, 2, 3)
            x.__init__(1,2,3)
            x._get_value()
    except BaseException:
        pass
    try:
        with pytest.raises(NotImplementedError):
            x = Token(1, 2, 3)
            x.__init__(1,2,3)
            x._get_child_token(1)
    except BaseException:
        pass
    try:
        with pytest.raises(NotImplementedError):
            x = Token(1, 2, 3)
            x.__init__(1,2,3)
            x._get_key_token(1)
    except BaseException:
        pass


# Generated at 2022-06-14 15:01:57.218479
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token = Token('', 0, 0)
    assert token == token

# Generated at 2022-06-14 15:01:59.377221
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class TestToken(Token):
        pass
    token1 = TestToken('string', 0, 5, 'string')
    token2 = TestToken('string', 0, 5, 'string')
    assert token1 == token2

# Generated at 2022-06-14 15:02:02.617312
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(1, 1, 1) == Token(1, 1, 1)
    assert not Token(1, 1, 1) == Token(2, 1, 1)
    assert not Token(1, 1, 1) == Token(1, 1, 2)
    assert not Token(1, 1, 1) == Token(2, 1, 2)


# Generated at 2022-06-14 15:02:12.279603
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(1,1,1)
    t2 = Token(2,2,2)
    t3 = Token(1,1,1)
    t4 = Token(1,1,2)
    t5 = Token(1,2,2)
    t6 = Token(1,1,1)
    
    # case 1: self = other
    assert t1 == t1
    
    # case 2: self != other, other is an uninstantiated variable
    try:
        t1 == other
    except NameError:
        pass
    else:
        raise Exception('test failed')
    
    # case 3: self != other, self is an uninstantiated variable
    try:
        t == t1
    except NameError:
        pass
    else:
        raise Exception('test failed')


# Generated at 2022-06-14 15:02:12.986162
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    pass



# Generated at 2022-06-14 15:02:28.113722
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    value = "test"
    start_index = 0
    end_index = 4
    t1 = Token(value, start_index, end_index)
    t2 = Token(value, start_index, end_index)
    assert (t1 == t2)


# Generated at 2022-06-14 15:02:29.212201
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token(4, 5, 6) == Token(4, 5, 6)

# Generated at 2022-06-14 15:02:33.013554
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    x = Token(value = 10, start_index = 20, end_index = 30)
    y = Token(x.value, x.start_index, x.end_index)
    assert x == y

# Generated at 2022-06-14 15:02:44.420460
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # cas 1
    value = 'hello'
    start_index = 1
    end_index = 2
    content = ''
    token = Token(value, start_index, end_index, content)
    other = None
    assert token.__eq__(other) == NotImplemented, f'test_Token___eq__({repr(token)}, {repr(other)})'
    # cas 2
    value = 'hello'
    start_index = 1
    end_index = 2
    content = ''
    token = Token(value, start_index, end_index, content)
    other = 'hello'
    assert token.__eq__(other) == False, f'test_Token___eq__({repr(token)}, {repr(other)})'
    # cas 3
    value = 'hello'


# Generated at 2022-06-14 15:02:55.719378
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_0 = Token(value="b", start_index=1, end_index=2, content="abc")
    token_1 = Token(value="b", start_index=1, end_index=2, content="abc")
    token_2 = Token(value="c", start_index=1, end_index=2, content="abc")
    token_3 = Token(value="b", start_index=3, end_index=4, content="abc")
    token_4 = Token(value="b", start_index=1, end_index=4, content="abc")
    assert(token_0 == token_1)
    assert(token_0 != token_2)
    assert(token_0 != token_3)
    assert(token_0 != token_4)


# Generated at 2022-06-14 15:03:00.160323
# Unit test for constructor of class DictToken
def test_DictToken():
    t = DictToken({'foo':'bar', 'baz':'0'}, start_index='s', end_index='e', content='str')
    print(t._value)
    print(t._start_index)
    print(t._end_index)
    print(t._content)
    
test_DictToken()


# Generated at 2022-06-14 15:03:08.025241
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    import sys, os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # needed to import from the parent directory
    from typesystem_tokens import Token as OtherToken

    token1 = Token("aaa", 0, 2, content = "aaa")
    token2 = Token("aaa", 0, 2, content = "aaa")
    assert (token1 == token2)

    token3 = OtherToken("aaa", 0, 2, content = "aaa")
    assert (not (token1 == token3))



# Generated at 2022-06-14 15:03:13.865374
# Unit test for constructor of class DictToken
def test_DictToken():
    token = DictToken(1, 2, 3, value=4, start_index=5, end_index=6, content=7)
    expected_result = DictToken(1, 2, 3, value=4, start_index=5, end_index=6, content=7)
    assert token == expected_result


# Generated at 2022-06-14 15:03:20.096592
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    tok1 = Token(
        value=1,
        start_index=1,
        end_index=2,
        content="stub_content"
    )
    tok2 = Token(
        value=1,
        start_index=1,
        end_index=2,
        content="stub_content"
    )
    assert tok1 == tok2


# Generated at 2022-06-14 15:03:28.159544
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    class TestToken(Token):
        def __init__(self, value, start_index, end_index, content = ""):
            self._value = value
            self._start_index = start_index
            self._end_index = end_index
            self._content = content
    t1 = TestToken("t1", 0, 10, "t1 t1 t1")
    t2 = TestToken("t2", 1, 10, "t2 t2 t2")
    t3 = TestToken("t3", 1, 10, "t3 t3 t3")
    assert t1 != t2
    assert t2 == t3

# Generated at 2022-06-14 15:03:58.342133
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 0
    end_index = 2
    content = "hel"
    self = Token('hel',0,3)
    other = Token('hel',0,3)
    assert self == other
    self = Token('hel',0,3)
    other = Token(0,0,3)
    assert not(self == other)

# Generated at 2022-06-14 15:04:02.642930
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    start_index = 0
    end_index = 1
    value = 2
    content = "content"
    token = Token(value, start_index, end_index, content)
    assert token == token, "Different token object"
    assert token == Token(value, start_index, end_index, content), "Different token object"
    assert not token == None, "Different type value"



# Generated at 2022-06-14 15:04:05.470244
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token1 = ScalarToken(10, 1, 2)
    token2 = ScalarToken(10, 1, 2)
    assert token1 == token2


# Generated at 2022-06-14 15:04:09.410700
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    token_1 = Token("token.value", 0, 1, content="test")
    token_2 = Token("test", 0, 1, content="test")
    token_3 = Token("value", 0, 1, content="test")
    assert token_1 != token_2
    assert token_2 != token_3

# Generated at 2022-06-14 15:04:13.170678
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    value = None
    start_index = 0
    end_index = 0
    content = ""
    token = Token(value, start_index, end_index, content)
    assert token.__eq__(token)
    assert not token.__eq__(1)


# Generated at 2022-06-14 15:04:14.680229
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert Token.__eq__(Token(None,0,1),"") == False


# Generated at 2022-06-14 15:04:22.429713
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    # Test missing attributes
    t = Token()
    assert not (t == (Token()))
    # Test class differences
    t = DictToken()
    assert not (t == (Token()))
    # Test attribute differences
    t = Token(value=1, start_index=2, end_index=3)
    assert not (t == (Token(value=1, start_index=2, end_index=3)))
    # Test attribute equalities
    t = Token('x', 2, 3)
    assert t == Token('x', 2, 3)

# Generated at 2022-06-14 15:04:25.186515
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    assert ScalarToken(1, 0, 2, "abc") == ScalarToken(1, 0, 2, "abc")
    assert not (ScalarToken(1, 0, 2, "abc") == ScalarToken(2, 0, 2, "abc"))

# Generated at 2022-06-14 15:04:31.844547
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    expected = False
    actual = Token(0, 1, 2) == None
    assert expected == actual

    expected = False
    actual = Token(0, 1, 2) == 1
    assert expected == actual

    expected = False
    actual = Token(0, 1, 2) == Token(0, 1, 2, "abc")
    assert expected == actual

    expected = True
    actual = Token(0, 1, 2) == Token(0, 1, 2, "abc")
    assert expected == actual

# Generated at 2022-06-14 15:04:42.466764
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    from typesystem import Scalar, Dict, List
    from typesystem.base import Keyword, Number
    from typesystem.errors import ValidationError

    T = Dict({"foo": Scalar(Number())})

    # Test 1
    try:
        token = T({"foo": 1})
        assert token.lookup([]) == token
    except ValidationError:
        pass

    # Test 2
    try:
        token = T({"foo": 1})
        assert token.lookup([]) != T({"foo": 2})
    except ValidationError:
        pass

    # Test 3
    try:
        token = T({"foo": 1})
        assert token.lookup_key([]) == token._get_key_token("foo")
    except ValidationError:
        pass

    # Test 4

# Generated at 2022-06-14 15:05:32.620453
# Unit test for constructor of class DictToken
def test_DictToken():
    Token_d = DictToken({}, 0, 10, "", )
    assert Token_d._value == {}
    assert Token_d._start_index == 0
    assert Token_d._end_index == 10
    assert Token_d._content == ""
    # Test to ensure that object is of type DictToken
    assert isinstance(Token_d, DictToken)


# Generated at 2022-06-14 15:05:37.996432
# Unit test for constructor of class Token
def test_Token():
    t = Token(1, 1, 2, "123456")
    assert(t.start() == Position(1, 1, 1))
    assert(t.end() == Position(1, 2, 2))
    assert(t._value == 1)
    assert(t.string == "2")



# Generated at 2022-06-14 15:05:41.231922
# Unit test for method __eq__ of class Token
def test_Token___eq__():
    t1 = Token(value=None, start_index=None, end_index=None)
    t2 = Token(value=None, start_index=None, end_index=None)
    assert t1 == t2

# Generated at 2022-06-14 15:05:44.884869
# Unit test for constructor of class Token
def test_Token():
    token = Token("value", 0, 2, "content")
    assert token.string == "con"
    assert token.value == "value"
    assert token.start == Position(1, 1, 0)
    assert token.end == Position(1, 4, 3)

# Generated at 2022-06-14 15:05:51.125235
# Unit test for constructor of class DictToken
def test_DictToken():
    a = {}
    assert a == {}
    assert a == dict()
    assert a == dict(a=1, b=2, c=3)
    assert len(a) == 0
    a = {'a': 1, 'b': 2, 'c': 3}
    assert a == {'a': 1, 'b': 2, 'c': 3}
    assert len(a) == 3
    a = DictToken('')
    assert a._value == {''}
    assert a._child_keys == {'': ''}
    assert a._child_tokens == {'': {}}
    

# Generated at 2022-06-14 15:05:57.108643
# Unit test for constructor of class ListToken
def test_ListToken():
    def test_ListToken():
        # test_ListToken Expected: return [token._get_value() for token in self._value]
        items=[1,2]
        token=ListToken(items, 2, 0)
        return token._get_value()
    assert test_ListToken() == [1,2]


# Generated at 2022-06-14 15:06:00.031885
# Unit test for method lookup_key of class Token
def test_Token_lookup_key():
    token = ListToken(value=[], start_index=0, end_index=0)
    assert token.lookup_key([1]) == token


# Generated at 2022-06-14 15:06:01.964807
# Unit test for constructor of class ListToken
def test_ListToken():
    token = ListToken(["","",""])
    assert(token.value == ["","",""])


# Generated at 2022-06-14 15:06:03.828119
# Unit test for constructor of class Token
def test_Token():
    t = Token(1, 2, 3, "abc")
    assert t.string == "abc"
    assert t.value == 1



# Generated at 2022-06-14 15:06:04.667685
# Unit test for method lookup of class Token
def test_Token_lookup():
    assert 0
