

# Generated at 2022-06-12 22:56:12.399345
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    DIC = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    TUPLE = ('b', 'd')
    SET = {'d', 'b'}
    LIST = ['b', 'd']
    DIC_KEYS = {'d': 'foo', 'b': 'bar'}

    assert DIC.difference(TUPLE) == ImmutableDict({'a': 1, 'c': 3})
    assert DIC.difference(SET) == ImmutableDict({'a': 1, 'c': 3})
    assert DIC.difference(LIST) == ImmutableDict({'a': 1, 'c': 3})
    assert DIC.difference(DIC_KEYS) == ImmutableDict({'a': 1, 'c': 3})

# Generated at 2022-06-12 22:56:22.553964
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    origin = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
    initial = ImmutableDict(origin)
    # Test removal of existing key
    result = initial.difference(('a',))
    assert result == ImmutableDict({'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
    # Test removal of non-existing key
    result = initial.difference(('g',))
    assert result == ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
    # Test union with non-iterable

# Generated at 2022-06-12 22:56:32.933087
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():

    # create a MutableDict
    orig_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
    }

    # create an ImmutableDict object from the MutableDict
    orig_immutable_dict = ImmutableDict(orig_dict)

    # create a Mutable list of keys to be removed
    subtractive_list = ['a', 'b', 'd', 'e']

    # create an ImmutableDict object from the ImmutableDict object without keys in the subtractive_list
    final_immutable_dict = orig_immutable_dict.difference(subtractive_list)

    # compare the result
    assert final_immutable_dict == {'c': 3}

# Generated at 2022-06-12 22:56:41.813908
# Unit test for function is_iterable
def test_is_iterable():
    """
    Unit test for is_iterable
    """
    # Check for iterable objects
    for obj_type in (list(), (1, 2), set(), frozenset(), dict(), ImmutableDict()):
        assert is_iterable(obj_type) is True, "{} is an iterable".format(obj_type)

    # Check for non-iterable objects
    for obj_type in (1, 1.0, [1, 2], 'string', (1, 2), set((1, 2)), tuple((1, 2)), dict(([1, 2], [3, 4])), ImmutableDict(a=1), True):
        assert is_iterable(obj_type) is False, "{} is not an iterable".format(obj_type)

    # Unit tests for string-like types

# Generated at 2022-06-12 22:56:53.200008
# Unit test for function is_iterable
def test_is_iterable():
    # test a list
    test_list = []
    assert is_iterable(test_list)
    assert is_sequence(test_list)
    assert not is_string(test_list)
    # test a list with an element
    test_list = [1]
    assert is_iterable(test_list)
    assert is_sequence(test_list)
    assert not is_string(test_list)
    # test a string
    test_string = 'string'
    assert not is_iterable(test_string)
    assert not is_sequence(test_string)
    assert is_string(test_string)
    # test a string with include_strings set to True
    assert is_iterable(test_string, include_strings=True)
    assert is_sequence(test_string, include_strings=True)

# Generated at 2022-06-12 22:57:02.111329
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Testing ImmutableDict equality method.
    In order to check if two dictionaries are equal, the following equation should
    be true:
    hash(dict1) == hash(dict2)
    """
    # Create two different ImmutableDicts
    dict1 = ImmutableDict(foo='bar')
    dict2 = ImmutableDict(bar='foo')

    # Test that they are different
    assert dict1 != dict2

    # Test that they have different hashes
    assert dict1.__hash__() != dict2.__hash__()

    # Create another ImmutableDict
    dict3 = ImmutableDict(foo='bar')

    # Test that the ImmutableDict is the same
    assert dict1 == dict3

    # Test that the ImmutableDict hash is the same
    assert dict1.__hash__()

# Generated at 2022-06-12 22:57:06.984194
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict([('a', 17), ('b', 23)])
    b = ImmutableDict([('b', 23), ('a', 17)])
    assert not a == [('a', 17), ('b', 23)]
    assert not a == 17
    assert a == b
    assert not b != a



# Generated at 2022-06-12 22:57:14.038117
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""
    try:
        x = {'a': 1, 'b': 2, 'c': 3}
        y = ImmutableDict(x)
        z = ImmutableDict(x)

        assert x == x
        assert y == z
        assert x == y
        assert y != {'a': 1, 'b': 2, 'd': 4}
    except AssertionError as e:
        print(e)


# Generated at 2022-06-12 22:57:18.806418
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 'a', 'b']) == True
    assert is_iterable((1, 2, 'a', 'b')) == True
    assert is_iterable({1, 2, 'a', 'b'}) == True
    assert is_iterable({'a': 1, 'b': 2}) == True
    assert is_iterable(1) == False
    assert is_iterable(1.0) == False


# Generated at 2022-06-12 22:57:25.634319
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    test_dict = ImmutableDict(dict(a=1, b=2))
    type_throwing_dict = {}
    assert test_dict == test_dict

    assert not test_dict == type_throwing_dict

    assert not test_dict == ImmutableDict(dict(a=1, b=2, c=4))
    assert test_dict == ImmutableDict(dict(a=1, b=2))
    assert test_dict == ImmutableDict(dict(b=2, a=1))



# Generated at 2022-06-12 22:57:35.894324
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict( {'key1': 'value1'})
    d2 = ImmutableDict( {'key2': 'value2'})
    d3 = ImmutableDict( {'key1': 'value1'})
    d4 = ImmutableDict( {'key1': 'value1'})
    #
    assert d1 == {}
    assert d2 == {}
    assert d3 == {}
    assert d4 == {}
    assert d1 == d4
    #
    assert not d1 == d2
    assert not d1 == d3
    assert not d2 == d3
    assert not d2 == d4
    assert not d3 == d4


# Generated at 2022-06-12 22:57:42.559005
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a=1)
    assert d1 == d1
    assert d1 == {'a': 1}
    assert d1 == ImmutableDict(a=1)
    d2 = ImmutableDict(a=2)
    assert d1 != d2
    assert d1 != {'b': 2}
    assert d1 != ImmutableDict(b=1)
    assert d1 != 'hello'
    assert d1 != [{'a': 1}]
    assert d1 != 123
    assert d1 != None


# Generated at 2022-06-12 22:57:50.926649
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    idict1 = ImmutableDict({'a': 3, 'b': 7})
    idict2 = ImmutableDict({'a': 3, 'b': 7})
    assert idict1.__eq__(idict2)
    idict3 = ImmutableDict({'a': 3, 'b': 7, 'c': 1})
    assert not idict1.__eq__(idict3)
    idict3 = ImmutableDict({'a': 3, 'c': 1})
    assert not idict1.__eq__(idict3)
    idict3 = ImmutableDict({'a': 3, 'b': 7})
    assert idict1.__eq__(idict3)
    idict3 = ImmutableDict({'a': 3, 'b': 8})
    assert not idict1

# Generated at 2022-06-12 22:57:55.290145
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Assert that ImmutableDict is equal to own copy
    """
    d1 = ImmutableDict(d1_dict={'a': 1, 'b': 2})
    d2 = ImmutableDict(d1_dict={'a': 1, 'b': 2})
    assert d1 == d2


# Generated at 2022-06-12 22:58:01.109559
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    x = ImmutableDict(a=1, b=2, c=3)
    y = x.difference([])
    assert y == x

    y = x.difference(('a',))
    assert y == ImmutableDict(b=2, c=3)

    y = x.difference(['b'])
    assert y == ImmutableDict(a=1, c=3)



# Generated at 2022-06-12 22:58:10.407729
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Check that ImmutableDict.__eq__ works correctly

    """
    assert ImmutableDict(dict(a=1)) == ImmutableDict(dict(a=1))
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict(a=1) == ImmutableDict(a=1)
    assert ImmutableDict(a=1) != ImmutableDict(a=2)
    assert ImmutableDict(a=1) != ImmutableDict(a=1, b=2)
    assert ImmutableDict(a=1) != ImmutableDict(b=1)
    assert ImmutableDict(a=1) != ImmutableDict()
    assert ImmutableDict(a=1) != None
    assert ImmutableDict(a=1) != 1
    assert Imm

# Generated at 2022-06-12 22:58:20.187788
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict_a = ImmutableDict({"a": 1, "b": 2, "c": 3})
    test_dict_b = ImmutableDict({"a": 1, "b": 2, "c": 3})
    test_dict_c = ImmutableDict({"a": 1, "b": 2, "c": 4})
    assert test_dict_a == test_dict_b
    assert test_dict_b == test_dict_a
    assert test_dict_a != test_dict_c
    assert test_dict_b != test_dict_c
    assert test_dict_c != test_dict_a
    assert test_dict_c != test_dict_b


# Generated at 2022-06-12 22:58:30.243085
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Testing equality when the same key is specified multiple times in both objects
    test_dict = ImmutableDict(dict(a=1, b=2, c=3))
    other_dict = ImmutableDict(dict(a=1, b=2, c=3))
    assert test_dict == other_dict

    # Testing equality when the same key is specified multiple times in one object and once only in the other
    test_dict = ImmutableDict(dict(a=1, b=2, c=3, d=4))
    other_dict = ImmutableDict(dict(a=1, b=2, c=3))
    assert test_dict == other_dict

    # Testing equality when the same key is specified multiple times in one object and once only in the other

# Generated at 2022-06-12 22:58:38.544947
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    The method __eq__ has to work for equal and not equal values.

    The method __eq__ has to work fine for equal and not equal values,
    not just for same dicts from the same class, but also for other
    dictionaries (built-in, from other classes) and other objects which
    cannot be hashable or equal.
    """
    dict1 = ImmutableDict({'key1': 'value1'})
    dict2 = ImmutableDict({'key1': 'value1'})

    # Equal dictionaries of the same class
    assert dict1 == dict2

    # Equal dictionaries of other classes
    dict3 = dict((k, v) for k, v in dict1.items())
    assert dict1 == dict3

    # Not equal dictionaries of other classes

# Generated at 2022-06-12 22:58:47.600063
# Unit test for function is_iterable
def test_is_iterable():
    """Test for the is_iterable function."""
    assert not is_iterable(None)
    assert is_iterable('')
    assert is_iterable('abc')
    assert is_iterable(b'abc')
    assert not is_iterable(b'abc', include_strings=False)
    assert is_iterable(b'abc', include_strings=True)
    assert is_iterable({})
    assert is_iterable([])
    assert is_iterable((1, 2))
    assert is_iterable(set())
    assert not is_iterable(1)
    assert not is_iterable(abs)


# Generated at 2022-06-12 22:58:55.752019
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable((1,2,3))
    assert is_iterable([1,2,3])
    assert is_iterable(set((1,2,3)))
    assert is_iterable({'a':1, 'b':2, 'c':3})

    assert not is_iterable(1)
    assert not is_iterable('abc')
    assert not is_iterable(1.0)
    assert not is_iterable(True)


# Generated at 2022-06-12 22:58:58.496874
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict(a=1, b=2, c=3)
    result = original.difference(['a'])
    assert result == ImmutableDict(b=2, c=3)

# Generated at 2022-06-12 22:59:05.611264
# Unit test for function is_iterable
def test_is_iterable():
    iterable_object = [1, 2, 3]
    non_iterable_object = 5
    string = 'some string'
    assert is_iterable(iterable_object) is True
    assert is_iterable(non_iterable_object) is False
    assert is_iterable(string) is True
    assert is_iterable(string, include_strings=False) is False


# Generated at 2022-06-12 22:59:15.315606
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    def assert_ImmutableDict_equality(immutable_dicts_and_expected_values):
        for immutable_dicts, expected_equality in immutable_dicts_and_expected_values:
            assert immutable_dicts[0] == immutable_dicts[1] == expected_equality

    assert_ImmutableDict_equality([
        ([ImmutableDict({'a': 1}), ImmutableDict({'b': 1}), False],),
        ([ImmutableDict({'a': 1}), ImmutableDict({'a': 2}), False],),
        ([ImmutableDict({'a': 1}), ImmutableDict({'a': 1}), True],),
    ])

    # Despite the fact that in a normal dict, the order of keys does not matter,
    # in ImmutableDict the order of keys is

# Generated at 2022-06-12 22:59:19.120006
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    immut1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    immut2 = immut1.difference(['a', 'c'])
    assert immut2 == {'b': 2}, 'difference of ImmutableDict failed.'



# Generated at 2022-06-12 22:59:25.851401
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    a = ImmutableDict({u'key1': u'value1', u'key2': u'value2', u'key3': u'value3'})
    b = ImmutableDict(a.difference([u'key1', u'key2']))
    assert u'key1' not in b
    assert u'key2' not in b
    assert u'key3' in b
    assert u'key3' in a



# Generated at 2022-06-12 22:59:30.704215
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = ImmutableDict({'a': 1, 'b': 2})
    assert d == {'a': 1, 'b': 2}
    assert d != {'a': 1, 'b': 2, 'c': 3}
    assert d != ['a', 'b', 'c']
    assert d != 'd'


# Generated at 2022-06-12 22:59:33.423868
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(42)
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())



# Generated at 2022-06-12 22:59:41.495388
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Unit test for testing method __eq__ of class ImmutableDict.
    """
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    d3 = ImmutableDict({'a': 3, 'b': 4})
    d4 = {'x': 1, 'y': 2, 'z': 3}
    assert d1 == d1
    assert d1 == d2
    assert d2 == d1
    assert d1 == d4
    assert d4 == d1
    assert d1 != d3
    assert d3 != d1
    assert d1 != d4
    assert d4 != d1

# Generated at 2022-06-12 22:59:48.949117
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict(dict(first=1, second=2, third=3))
    removed_first_key = original.difference(['first'])
    removed_first_and_third_keys = original.difference(['first', 'third'])
    removed_non_existing_key = original.difference(['non_existing_key'])
    assert removed_first_key.difference(['second']) == removed_first_key
    assert removed_first_key.difference(['first']) == removed_first_and_third_keys
    assert removed_first_key.difference(['non_existing_key']) == removed_first_key
    assert removed_first_key.difference(['third']) == removed_first_key
    assert removed_first_key == removed_first_key

# Generated at 2022-06-12 22:59:58.997842
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""
    arg1 = ImmutableDict(a=1, b=2)
    arg2 = dict(a=1, b=2)
    result = (arg1 == arg2)
    assert result



# Generated at 2022-06-12 23:00:01.754265
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Arrange
    immutabledict = ImmutableDict({'key': 'value'})
    # Act
    result = (1 == immutabledict)
    # Assert
    assert result == False


# Generated at 2022-06-12 23:00:12.637153
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immdict1 = ImmutableDict(a=1,b=2,c=3)
    immdict2 = ImmutableDict(d=1,e=2,f=3)
    immdict3 = ImmutableDict(a=1,b=2,c=3)
    immdict4 = ImmutableDict(a=1,b=2,c=4)
    immdict5 = ImmutableDict(a=2,b=2,c=3)
    immdict6 = ImmutableDict(b=2,c=3,d=3)
    immdict7 = ImmutableDict(a=1,b=2,c=3)
    immdict8 = ImmutableDict(a=1,b=2,c=3)

# Generated at 2022-06-12 23:00:22.229894
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == {}
    assert ImmutableDict() == ImmutableDict()
    assert not ImmutableDict() == 'a'
    assert not ImmutableDict() == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1}) == {'a': 1}
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert not ImmutableDict({'a': 1}) == ImmutableDict({'b': 1})
    assert not ImmutableDict({'a': 1}) == ImmutableDict({'a': 2})
    assert not ImmutableDict({'a': 1}) == ImmutableDict({'a': 1, 'b': 2})

# Generated at 2022-06-12 23:00:28.298028
# Unit test for function is_iterable
def test_is_iterable():
    class Test():
        def __init__(self):
            self.iterator = iter(range(3))
        def __iter__(self):
            return self.iterator

    assert is_iterable('hello world')
    assert not is_iterable('hello world', include_strings=False)
    assert is_iterable(Test())
    assert not is_iterable(Test(), include_strings=False)

    assert is_iterable([1, 2, 3])
    assert not is_iterable([1, 2, 3], include_strings=False)
    assert is_iterable((1, 2, 3))
    assert not is_iterable((1, 2, 3), include_strings=False)
    assert is_iterable({'one': 1, 'two': 2, 'three': 3})

# Generated at 2022-06-12 23:00:39.019079
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test 1: Both ImmutableDict's are non-empty
    dic1 = {'1': 'one', '2': 'two', '3': 'three'}
    imm_dic1 = ImmutableDict(dic1)
    imm_dic2 = ImmutableDict(dic1)
    assert imm_dic1 == imm_dic2

    # Test 2: One of the ImmutableDict is empty
    dic1 = {'1': 'one', '2': 'two', '3': 'three'}
    imm_dic1 = ImmutableDict(dic1)
    imm_dic2 = ImmutableDict()
    assert imm_dic1 != imm_dic2

    # Test 3: ImmutableDict with equal number of elements, but different values

# Generated at 2022-06-12 23:00:43.212545
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2)
    assert ImmutableDict(a=1, b=2) != {1: 3, 4: 5}
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=3)
    return None


# Generated at 2022-06-12 23:00:54.649141
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a':1, 'b':2})
    b = ImmutableDict({'a':1, 'b':2})
    c = ImmutableDict({'a':1, 'b':3})
    d = ImmutableDict({'a':1, 'b':2}, c=3)
    # Test values with no extra arguments
    assert a.__eq__(b)
    assert not a.__eq__(c)
    # Test values with extra arguments
    assert not a.__eq__(d)
    # Test exceptions
    try:
        a.__eq__({})
    except TypeError as e:
        assert e.args[0] == "'>' not supported between instances of 'ImmutableDict' and 'dict'"
        return

# Generated at 2022-06-12 23:01:00.648647
# Unit test for function is_iterable
def test_is_iterable():
    seq1 = (1, 2, 3)
    assert is_iterable(seq1)
    seq2 = {1, 2, 3}
    assert is_iterable(seq2)
    seq3 = 'abcd'
    assert is_iterable(seq3)
    seq4 = b'\xe5'
    assert is_iterable(seq4)
    assert not is_iterable(1)


# Generated at 2022-06-12 23:01:08.933720
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test case 1
    # Test for equality of two ImmutableDicts
    test_dict = ImmutableDict({'a':0, 'b': 1})
    other_dict = ImmutableDict({'a':0, 'b': 1})
    assert test_dict == other_dict, "Two ImmutableDicts with the same key-value pairs should be equal"
 
    # Test case 2
    # Test for inequality of two ImmutableDicts
    test_dict = ImmutableDict({'a':0, 'b': 1})
    other_dict = ImmutableDict({'a':0, 'b': 2})
    assert test_dict != other_dict, "Two ImmutableDicts with different key-value pairs should not be equal"

    # Test case 3
    # Test for equality of a regular dict and an ImmutableDict

# Generated at 2022-06-12 23:01:28.991287
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id1 = ImmutableDict({'a': 'b'})
    id2 = ImmutableDict({'a': 'b'})
    id3 = ImmutableDict({'a': 'd'})
    id4 = ImmutableDict({'a': 'b', 'b': 'c'})

    assert id1 == id2
    assert id1 != id3
    assert id1 != id4
    assert id1 != {'a': 'b'}


# Generated at 2022-06-12 23:01:36.910776
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() == dict()
    assert ImmutableDict() == {}
    assert ImmutableDict() == {'foo': 'bar'}.keys()
    assert ImmutableDict() == set()
    assert ImmutableDict() == frozenset()
    assert ImmutableDict() == tuple()
    assert ImmutableDict() == ()
    assert ImmutableDict() == list()
    assert ImmutableDict() == []
    assert ImmutableDict({'foo': 'bar'}) == {'foo': 'bar'}
    assert ImmutableDict({'foo': 'bar'}) == frozenset({'foo': 'bar'}.items())
    assert ImmutableDict({'foo': 'bar'}) == {'foo': 'bar'}.items()


# Generated at 2022-06-12 23:01:46.436148
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Ensure ImmutableDict comparison of like objects works as expected
    """
    id = ImmutableDict(a=1,b=2,c=3)
    # object of class ImmutableDict
    assert id == id
    # object of class ImmutableDict with same contents
    assert id == ImmutableDict(a=1,b=2,c=3)
    # object of class ImmutableDict with same contents and different order
    assert id == ImmutableDict(c=3,b=2,a=1)
    # object of class dict with same contents
    assert id == dict(a=1,b=2,c=3)
    # object of class dict with same contents and different order
    assert id == dict(c=3,b=2,a=1)
    # ImmutableDict and dict

# Generated at 2022-06-12 23:01:51.202361
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dicts = [ImmutableDict({'a': 1, 'b': 2}), ImmutableDict({'b': 2, 'a': 1}),
                  ImmutableDict([('b', 2), ('a', 1)]), ImmutableDict(a=1, b=2)]
    for element in test_dicts:
        assert element == ImmutableDict({'a': 1, 'b': 2})


# Generated at 2022-06-12 23:01:57.687367
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable('test'), 'String is not iterable'
    assert not is_iterable(b'test'), 'Bytes are not iterable'
    assert is_iterable(['test']), 'List of strings is iterable'
    assert is_iterable((b'test',)), 'Tuple of bytes is iterable'
    assert is_iterable({'test': 'test'}), 'Dictionary is iterable'
    assert is_iterable('test'.split()), 'String split() is iterable'



# Generated at 2022-06-12 23:02:04.936136
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    empty_immutable_dict = ImmutableDict()
    assert not empty_immutable_dict == {'a': 1}
    dict1 = ImmutableDict(a=1, c=3, b=2)
    dict2 = ImmutableDict(a=1, c=3, b=2)
    assert dict1 == dict2
    dict3 = ImmutableDict(dict1, d=4)
    dict4 = dict1.union(dict(d=4))
    assert dict4 == dict3
    assert dict4 == dict4

    # Different number of keys
    assert not dict4 == dict2

    # Different keys
    assert not dict4 == dict(a=1, c=3, b=2)

    # Different order of keys (in dict1 and dict2)

# Generated at 2022-06-12 23:02:15.808307
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Both tokens are the same
    i_dict_1 = ImmutableDict({"key1": "value1", "key2": "value2"})
    i_dict_2 = ImmutableDict({"key1": "value1", "key2": "value2"})
    assert i_dict_1 == i_dict_2

    # Both tokens are different
    i_dict_1 = ImmutableDict({"key1": "value1", "key2": "value2"})
    i_dict_2 = ImmutableDict({"key1": "value1", "key2": "value3"})
    assert not i_dict_1 == i_dict_2

    # One token is different (additional key)

# Generated at 2022-06-12 23:02:23.065985
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Positive test
    dict_1 = ImmutableDict({1:1, 2:2})
    dict_2 = ImmutableDict([(1,1), (2,2)])
    assert dict_1.__eq__(dict_2) is True

    # Negative test
    dict_1 = ImmutableDict({1:1, 2:2})
    dict_2 = ImmutableDict([(1,1), (2,3)])
    assert dict_1.__eq__(dict_2) is False

# Generated at 2022-06-12 23:02:33.130371
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'a': 1, 'B': 2, 'C': 3})
    c = ImmutableDict({'A': 1, 'B': 2, 'C': 3})
    d = ImmutableDict([('a', 1), ('b', 2), ('c', 3)])
    assert(a == b)
    assert(a == d)
    assert(b == a)
    assert(b == d)
    assert(d == a)
    assert(d == b)
    assert(a != c)
    assert(b != c)
    assert(c != a)
    assert(c != b)
    assert(a != None)
    assert(a != 1)

# Generated at 2022-06-12 23:02:43.415661
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert not is_iterable(5)
    assert not is_iterable(Exception)
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable('')
    assert is_iterable('a')
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(dict())
    assert not is_iterable(dict().keys())
    assert not is_iterable(set().union)
    assert is_iterable(dict().values())
    assert is_iterable(set().union)
    assert is_iterable(dict().items())
    assert is_iterable(x for x in range(10))

    assert is_iterable(Exception, True)

# Generated at 2022-06-12 23:03:18.424860
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Check that ImmutableDict instances that are equal are actually equal
    # when compared to each other
    immutable1 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    immutable2 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    assert immutable1 == immutable2

    # Check that ImmutableDict instances that are not equal are actually not
    # equal when compared to each other
    immutable1 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    immutable2 = ImmutableDict({'key1': 'value1', 'key3': 'value3'})
    assert not (immutable1 == immutable2)

    # Check that ImmutableDict instances that are equal are not actually equal
    # when compared

# Generated at 2022-06-12 23:03:24.182373
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict = ImmutableDict({'a': 1, 'b': 2})
    assert test_dict == ImmutableDict({'a': 1, 'b': 2})
    assert test_dict == {'a': 1, 'b': 2}
    assert test_dict != ImmutableDict({'a': 1, 'b': 3})
    assert test_dict != {'a': 1, 'b': 3}


# Generated at 2022-06-12 23:03:33.139868
# Unit test for function is_iterable
def test_is_iterable():
    class TestClass(object):

        def __init__(self, a=3):
            self.a = a

        def __iter__(self):
            while self.a > 0:
                yield self.a
                self.a -= 1

    assert is_iterable('string') is False
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable({'a': 1, 'b': 2}) is True
    assert is_iterable(TestClass()) is True
    assert is_iterable(0) is False
    assert is_iterable(is_iterable) is False
    assert is_iterable(is_string) is False


# Unit

# Generated at 2022-06-12 23:03:43.507062
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(True)
    assert not is_iterable('text')
    assert is_iterable(['text'])
    assert is_iterable(('text',))
    assert is_iterable(dict(name='text'))
    assert is_iterable(set(['text']))
    assert is_iterable(xrange(10))
    # Unit test for function is_sequence
    assert not is_sequence(None)
    assert not is_sequence(1)
    assert not is_sequence(True)
    assert not is_sequence('text')
    assert is_sequence(['text'])
    assert is_sequence(('text',))
    assert not is_sequence(dict(name='text'))

# Generated at 2022-06-12 23:03:53.006215
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    def test_equality(dict1, dict2, dict3, dict4):
        # Ensure that hashable objects can be compared
        assert dict1 == dict1
        assert dict1 == dict2
        assert dict1 != dict3
        assert dict1 != dict4
        assert dict1 != object()

        # Ensure that a hashable object can be compared to an unhashable one
        assert dict1 == dict2._store
        assert dict1 != dict3._store
        assert dict1._store != dict3

    dict1 = ImmutableDict({"key1": "value1", "key2": "value2"})
    dict2 = ImmutableDict({"key1": "value1", "key2": "value2"})
    dict3 = ImmutableDict({"key1": "value1", "key2": "value3"})


# Generated at 2022-06-12 23:03:58.922416
# Unit test for method __eq__ of class ImmutableDict

# Generated at 2022-06-12 23:04:10.294067
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(set([]))
    assert is_iterable((x for x in range(10)))
    assert is_iterable(ImmutableDict())
    assert is_iterable({})
    assert is_iterable(u"test")
    assert not is_iterable(42)
    assert not is_iterable(set(42))
    assert is_iterable(set([42]))
    assert is_iterable(u"test", include_strings=True)
    assert is_iterable(b"test", include_strings=True)
    assert not is_iterable(b"test")
    assert not is_iterable(b"test".decode())


# Generated at 2022-06-12 23:04:15.992564
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import copy
    import random

    def _make_mapping():
        return ImmutableDict({i: random.random() for i in range(random.randint(0, 20))})

    mapping_a = _make_mapping()
    mapping_b = copy.deepcopy(mapping_a)
    mapping_c = _make_mapping()

    assert mapping_a == mapping_b
    assert not mapping_a == mapping_c
    assert not mapping_a == {}
    assert not mapping_a == object()
    assert not mapping_a == True



# Generated at 2022-06-12 23:04:18.073678
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict = ImmutableDict({"a":1, "b":2})
    test_dict_other = ImmutableDict({"a":1, "b":2})
    result = test_dict == test_dict_other
    assert result == True


# Generated at 2022-06-12 23:04:27.122980
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(None) is False
    assert is_iterable(42) is False
    assert is_iterable(3.14) is False
    assert is_iterable(3.14j) is False
    assert is_iterable(u'x') is True
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable({}) is True
    assert is_iterable(()) is True
    assert is_iterable(set()) is True
    assert is_iterable(xrange(3)) is True
    assert is_iterable('abc') is False
    assert is_iterable(text_type(u'x')) is True
    assert is_iterable(binary_type(b'x')) is False



# Generated at 2022-06-12 23:05:33.071608
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import types
    d1 = ImmutableDict(a=1, b=2)
    assert d1.__eq__(d1) == True
    d2 = ImmutableDict(a=2, b=3)
    assert d1.__eq__(d2) == False
    d3 = ImmutableDict(a=1, b=2)
    assert d1.__eq__(d3) == True
    assert d1.__eq__(dict(a=1, b=2)) == True
    assert d1.__eq__(dict(b=2, a=1)) == True
    assert d1.__eq__(dict(b=2, a=2)) == False
    assert d1.__eq__(set([1, 2])) == False

# Generated at 2022-06-12 23:05:41.590073
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import inspect
    import itertools

    def test_ImmutableDict___eq___helper(first, second, expected_result):
        first_result = first == second
        second_result = second == first

        if first_result is not expected_result or second_result is not expected_result:
            print('\nFailed: first: {0}, second: {1}, expected_result: {2}'.format(
                  inspect.getsource(first), inspect.getsource(second), expected_result))
            print('first_result: {0}, second_result: {1}'.format(first_result, second_result))
            return False


# Generated at 2022-06-12 23:05:44.954973
# Unit test for function is_iterable
def test_is_iterable():
    a = list()

    assert is_iterable(a)

    b = set()
    assert is_iterable(b)

    c = dict()
    assert is_iterable(c)

    d = tuple()
    assert is_iterable(d)



# Generated at 2022-06-12 23:05:53.148481
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable([])
    assert is_iterable({1, 2, 3})
    assert is_iterable(set())
    assert is_iterable((1, 2, 3))
    assert is_iterable(range(10))
    assert is_iterable("abc")
    assert is_iterable("abc", include_strings=True)
    assert is_iterable("abc".encode("utf-8"), include_strings=True)
    assert is_iterable(1)
    assert not is_iterable(1, include_strings=True)
    assert not is_iterable(None)
    assert not is_iterable(None, include_strings=True)



# Generated at 2022-06-12 23:05:56.318447
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1}) != {'a': 1}
    assert ImmutableDict({'a': 1}) != ImmutableDict({'a': 2})

# Generated at 2022-06-12 23:06:02.067110
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'key1': 'value1'}) == ImmutableDict({'key1': 'value1'})
    assert ImmutableDict({'key1': 'value1'}) == dict({'key1': 'value1'})
    assert ImmutableDict({'key1': 'value1'}) != dict({'key1': 'value2'})
    assert ImmutableDict({'key1': 'value1'}) != dict({'key2': 'value1'})

# Generated at 2022-06-12 23:06:05.618686
# Unit test for function is_iterable
def test_is_iterable():
    assert(is_iterable([1, 2, 3]))
    assert(is_iterable((1, 2, 3)))
    assert(is_iterable(set('abc')))
    assert(is_iterable({'a': 'b'}))
    assert(is_iterable('abc'))
    assert(is_iterable(b'abc'))

    assert(not is_iterable(1))
    assert(not is_iterable(1.0))

