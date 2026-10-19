

# Generated at 2022-06-12 22:56:10.529732
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    a = ImmutableDict(test=1, foo=2)
    b = a.difference((b'test',))
    assert('test' not in b)
    assert('foo' in b)

# Generated at 2022-06-12 22:56:20.121905
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    def test_ImmutableDict_against_itself(expected_result, dict_obj1, dict_obj2):
        if dict_obj1.__eq__(dict_obj2):
            assert expected_result == True
        else:
            assert expected_result == False

    test_ImmutableDict_against_itself(expected_result=True, dict_obj1=ImmutableDict({}), dict_obj2=ImmutableDict({}))
    test_ImmutableDict_against_itself(expected_result=True, dict_obj1=ImmutableDict({'key': 'value'}), dict_obj2=ImmutableDict({'key': 'value'}))

# Generated at 2022-06-12 22:56:30.815336
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict()
    b = ImmutableDict()

    assert a == b

    a = ImmutableDict({'a':1})
    b = ImmutableDict({'a':1})

    assert a == b

    a = ImmutableDict({'a':1, 'b':2})
    b = ImmutableDict({'a':1, 'b':2})

    assert a == b

    a = ImmutableDict({'a':1, 'b':2})
    b = ImmutableDict({'b':2, 'a':1})

    assert a == b

    a = ImmutableDict({'a':1, 'b':2})
    b = ImmutableDict({'b':2, 'a':1, 'c':3})

    assert a != b

    a = Imm

# Generated at 2022-06-12 22:56:38.686700
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({1: 2, 3: 4}) == ImmutableDict({1: 2, 3: 4})
    assert not ImmutableDict({1: 2, 3: 4}) == ImmutableDict({2: 3, 3: 4})
    assert not ImmutableDict({1: 2, 3: 4}) == ImmutableDict({1: 2, 4: 5})
    assert not ImmutableDict({1: 2, 3: 4}) == ImmutableDict({1: 2})
    assert not ImmutableDict({1: 2, 3: 4}) == ImmutableDict({1: 2, 3: 4, 5: 6})
    assert not ImmutableDict({1: 2, 3: 4}) == ImmutableDict({1: 3, 3: 4})

# Generated at 2022-06-12 22:56:49.515856
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    emp_dict = ImmutableDict()
    dict_with_one_elem = ImmutableDict({'one': 'one_item'})
    dict_with_two_elem = ImmutableDict({'one': 'one_item', 'two': 'second_item'})
    dict_with_three_elem = ImmutableDict({'one': 'one_item', 'two': 'second_item', 'three': 'third_item'})
    assert(dict_with_one_elem.difference([]) == ImmutableDict({'one': 'one_item'}))
    assert(dict_with_three_elem.difference(['one', 'three']) == ImmutableDict({'two': 'second_item'}))

# Generated at 2022-06-12 22:56:57.620045
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    orig = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert orig.difference(['b']) == ImmutableDict({'a': 1, 'c': 3})
    assert orig.difference('b') == ImmutableDict({'a': 1, 'c': 3})
    assert orig.difference(['z']) == ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert orig.difference('z') == ImmutableDict({'a': 1, 'b': 2, 'c': 3})


# Generated at 2022-06-12 22:57:02.617401
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test a returning value of method ImmutableDict.__eq__ (aka '==' operator)"""

    def test(id, other, expected_result=True):
        """Generic test function"""
        result = id == other
        assert result == expected_result, 'Test {0} failed: {1} == {2} has returned a wrong value, {3}'.format(
            test.counter, id, other, result)
        test.counter += 1

    test.counter = 1

    # test 1: self and other are the same instance
    id1 = ImmutableDict([(1, 2), (3, 4), (5, 6)])
    test(id1, id1, True)

    # test 2: self and other are immutable dicts that contain the same keys and values

# Generated at 2022-06-12 22:57:07.821654
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import copy

    d = ImmutableDict({'a': 1, 'b': 2})
    assert d == ImmutableDict({'a': 1, 'b': 2})
    assert d == {'a': 1, 'b': 2}
    assert d == ImmutableDict(copy.copy(d))



# Generated at 2022-06-12 22:57:14.124321
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    test_dict = ImmutableDict({'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd'})
    assert test_dict.difference(['a']) == ImmutableDict({'b': 'b', 'c': 'c', 'd': 'd'})
    assert test_dict.difference(['a', 'd']) == ImmutableDict({'b': 'b', 'c': 'c'})


# Generated at 2022-06-12 22:57:16.988510
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable('abc')
    assert is_iterable(1)
    assert not is_iterable(1, include_strings=True)


# Generated at 2022-06-12 22:57:26.686067
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    We test __eq__ method of class ImmutableDict
    """
    test_dict = ImmutableDict(a=1, b=2)
    test_dict2 = ImmutableDict(a=1, b=2)
    test_dict.__eq__(test_dict2)
    assert (test_dict) == (test_dict2)



# Generated at 2022-06-12 22:57:36.643223
# Unit test for function is_iterable
def test_is_iterable():
    from collections import OrderedDict, namedtuple

    # Order is important.
    # Since bytes inherits from Sequence, this should come before Sequence.
    # Since bytes is considered "string" even on python3, this should come before string.
    stuff = (
        Mapping,
        MutableMapping,
        Sequence,
        # AnsibleVaultEncryptedUnicode inherits from Sequence, but is expected to be a string like object
        # which is an iterable
        str,
        # bytes is considered "string" and an iterable
        bytes,
        OrderedDict,
        namedtuple('Mock', ['a', 'b']),
        lambda x: x,
        object(),
    )

    for thing in stuff:
        assert is_iterable(thing(range(5)))


# Generated at 2022-06-12 22:57:44.876471
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Arrange
    i_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    i_dict_same = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    i_dict_different = ImmutableDict({'a': 1, 'b': 2, 'c': 4})
    another_dict = {'a': 1, 'b': 2, 'c': 3}
    list_ = ['a', 'b', 'c']

    # Act
    # Assert
    assert i_dict == i_dict_same
    assert not i_dict == i_dict_different
    assert not i_dict == another_dict
    assert not i_dict == 1
    assert not i_dict == list_

# Generated at 2022-06-12 22:57:51.836542
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    # Positive tests
    _dict1 = ImmutableDict({1: 'a', 2: 'b'})
    _dict2 = ImmutableDict({1: 'a', 2: 'b'})
    assert(_dict1.__eq__(_dict2) == True)

    _dict1 = ImmutableDict({1: ['a', 'b'], 2: 'c'})
    _dict2 = ImmutableDict({1: ['a', 'b'], 2: 'c'})
    assert(_dict1.__eq__(_dict2) == True)

    _dict1 = ImmutableDict({'a': {1: ['a', 'b'], 2: 'c'}, 2: 'e'})

# Generated at 2022-06-12 22:57:56.408449
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(0) == False
    assert is_iterable(True) == False
    assert is_iterable(None) == False
    assert is_iterable('hello') == True
    assert is_iterable({'a':'b'}) == True
    assert is_iterable([1,2,3]) == True

# Generated at 2022-06-12 22:57:59.012726
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    first  = ImmutableDict({'a': 1})
    second = ImmutableDict({'a': 1})
    assert first == second


# Generated at 2022-06-12 22:58:06.010558
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['a', 'b', 'c']) is True
    assert is_iterable(('a', 'b', 'c')) is True
    assert is_iterable(set(['a', 'b', 'c'])) is True
    assert is_iterable({'a': 1, 'b': 2, 'c': 3}) is True

    assert is_iterable('abc') is False
    assert is_iterable('abc', include_strings=True) is True
    assert is_iterable(100) is False
    assert is_iterable(100.0) is False
    assert is_iterable(Exception('test')) is False



# Generated at 2022-06-12 22:58:16.338108
# Unit test for function is_iterable
def test_is_iterable():
    """Unit tests for function is_iterable"""
    # Basic test of the function
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert is_iterable('abc')
    assert not is_iterable(123)

    # Test if the function takes into account the include_strings parameter
    assert is_iterable(123, include_strings=True)

    # Test if the function works on files
    test_file = open('tests/unit/utils/test_file')
    assert is_iterable(test_file)

    test_file = open('tests/unit/utils/test_file')
    test_file.close()
    assert not is_iterable(test_file)


# Generated at 2022-06-12 22:58:27.310453
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict([('a',1)]) == ImmutableDict([('a',1)])
    assert ImmutableDict([('a', 1), ('b', 2)]) == ImmutableDict([('b', 2), ('a', 1)])
    assert ImmutableDict([('a', 1), ('a', 2)]) == ImmutableDict([('a', 1), ('a', 2)])
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict(a='test') == ImmutableDict(a='test')
    assert ImmutableDict(a='test', b='test2') == ImmutableDict(b='test2', a='test')
    assert ImmutableDict(a='test', a='test2') == ImmutableDict(a='test', a='test2')
   

# Generated at 2022-06-12 22:58:30.388896
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['foo', 'bar', 'baz']) == True
    assert is_iterable('foo') == True
    assert is_iterable('foo', include_strings=False) == False
    assert is_iterable(42) == False


# Generated at 2022-06-12 22:58:45.560213
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immutable_dict_1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    immutable_dict_2 = ImmutableDict({'c': 3, 'a': 1, 'b': 2})
    assert immutable_dict_1 == immutable_dict_2
    assert immutable_dict_1 != [1,2,3]
    assert immutable_dict_1 != {'c': 3, 'a': 1, 'b': 2}



# Generated at 2022-06-12 22:58:55.030178
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Comparing to itself
    idict = ImmutableDict(dict(a=1, b=2, c=3))
    assert idict == idict

    # Comparing to the same dict
    assert not idict == dict(a=1, b=2, c=3)

    # Comparing to the same ImmutableDict
    assert idict == ImmutableDict(dict(c=3, b=2, a=1))

    # Comparing to an ImmutableDict with different contents
    assert not idict == ImmutableDict(dict(a=1, b=2, c=4))

    # Comparing with a non-dict
    assert not idict == None
    assert not idict == 1
    assert not idict == "a"
    assert not idict == (1, 2, 3)

# Unit

# Generated at 2022-06-12 22:59:06.517735
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    mapping = {'blue': 1, 'red': 2, 'green': 3}

    # ImmutableDict equality
    # positive case
    immutable_dict_eq_immutable_dict = ImmutableDict(mapping) == ImmutableDict(mapping)
    assert immutable_dict_eq_immutable_dict

    # negative case
    immutable_dict_neq_immutable_dict = ImmutableDict(mapping) != ImmutableDict(mapping)
    assert not immutable_dict_neq_immutable_dict

    # ImmutableDict equality with another Mapping
    # positive case
    immutable_dict_eq_mapping = ImmutableDict(mapping) == mapping
    assert immutable_dict_eq_mapping

    # negative case

# Generated at 2022-06-12 22:59:14.754797
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=3)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1, c=3)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1, c=2)
    assert not ImmutableDict(a=1, b=2) == ['any', 'other', 'object']



# Generated at 2022-06-12 22:59:21.865904
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict(x=1) == ImmutableDict(x=1)
    assert ImmutableDict(x=1) == ImmutableDict(x=1, y=2)
    assert ImmutableDict(x=1, y=2) == ImmutableDict(x=1)
    assert not ImmutableDict(x=1) == ImmutableDict(x=None)
    assert not ImmutableDict(x=1) == ImmutableDict(y=1)


# Generated at 2022-06-12 22:59:30.495729
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable(()) is True
    assert is_iterable({}) is True
    assert is_iterable(set()) is True
    assert is_iterable(frozenset()) is True
    assert is_iterable(dict()) is True
    assert is_iterable(ImmutableDict()) is True
    assert is_iterable(None) is False
    assert is_iterable(False) is False
    assert is_iterable(-1) is False
    assert is_iterable('') is False
    assert is_iterable('abcd') is True



# Generated at 2022-06-12 22:59:37.329616
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert (ImmutableDict() == ImmutableDict() is True)
    assert (ImmutableDict({'a': 1}) == ImmutableDict({'a': 1}) is True)
    assert (ImmutableDict({'a': ImmutableDict({'b': 1})}) == ImmutableDict({'a': ImmutableDict({'b': 1})}) is True)
    assert (ImmutableDict({'a': 1}) == dict({'a': 1}) is False)


# Test function union of class ImmutableDict

# Generated at 2022-06-12 22:59:41.110453
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    exampleDict = ImmutableDict({'a': 1})

    # 1. A similar dictionary is equal
    assert exampleDict == ImmutableDict({'a': 1})
    # 2. A dictionary with different keys is not equal
    assert exampleDict != ImmutableDict({'a': 1, 'b': 2})
    # 3. A dictionary with different value is not equal
    assert exampleDict != ImmutableDict({'a': 2})
    # 4. A dictionary that is not a dictionary is not equal
    assert exampleDict != 2

# Generated at 2022-06-12 22:59:48.676481
# Unit test for function is_iterable
def test_is_iterable():
    """Test is_iterable using assert statements.

    Test with the following objects:
    - a list
    - a string
    - a dictionary
    - a singleton tuple
    - a singleton list
    - a singleton set
    - a singleton dictionary
    - a singleton string
    - a number
    - None
    """
    assert is_iterable([1, 2, 3])
    assert is_iterable("string")
    assert is_iterable({1: 'a', 2: 'b', 3: 'c'})
    assert is_iterable((1,))
    assert is_iterable([1])
    assert is_iterable({1})
    assert is_iterable({1: 1})
    assert is_iterable("1")
    assert not is_iterable(1)
    assert not is_

# Generated at 2022-06-12 22:59:53.071586
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a=1, b=2, c=3)
    d2 = ImmutableDict(a=1, b=2, c=3)
    d3 = Hashable(a=1, b=2, c=3)
    assert d1 == d2
    assert d1 != d3

# Generated at 2022-06-12 23:00:12.037312
# Unit test for function is_iterable
def test_is_iterable():
    """Unit tests for function is_iterable"""
    assert is_iterable(tuple()) is True
    assert is_iterable(list()) is True
    assert is_iterable(set()) is True
    assert is_iterable(dict()) is True
    assert is_iterable(int()) is False
    assert is_iterable(str()) is False
    assert is_iterable(object()) is False


# Generated at 2022-06-12 23:00:18.265754
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Iterable not convertible to an ImmutableDict
    assert (ImmutableDict([('test', 1)]) == ['test']) == False

    # Dictionaries are not the same
    assert (ImmutableDict([('test', 1)]) == ImmutableDict([('test', 2)])) == False

    # Dictionaries are the same
    assert (ImmutableDict([('test', 1)]) == ImmutableDict([('test', 1)])) == True

# Generated at 2022-06-12 23:00:23.216680
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(range(10)) is True
    assert is_iterable('123') is True
    assert is_iterable(()) is True
    assert is_iterable(set()) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable(set(['a', 'b', 'c'])) is True

    assert is_iterable(1) is False



# Generated at 2022-06-12 23:00:25.771798
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict(key=value) == ImmutableDict(key=value)
    assert ImmutableDict() == dict()


# Generated at 2022-06-12 23:00:32.115266
# Unit test for function is_iterable
def test_is_iterable():
    # assert is_iterable('test')
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert is_iterable(set())
    assert is_iterable(set([1, 2]))
    assert is_iterable((1, 2, 3))
    assert is_iterable({})
    assert is_iterable({'a': 1, 'b': 2})


# Generated at 2022-06-12 23:00:41.145707
# Unit test for function is_iterable
def test_is_iterable():
    '''
    Test is_iterable
    '''

    class NotIterable(object):
        '''
        Test is_iterable
        '''

    assert is_iterable(['a','b','c'])
    assert is_iterable((1,2,3))
    assert not is_iterable(NotIterable())
    assert not is_iterable('not_iterable')
    assert is_iterable(dict(a='A', b='B'))
    assert is_iterable(dict(a='A', b='B').values())
    assert is_iterable(dict(a='A', b='B').keys())
    assert is_iterable(dict(a='A', b='B').items())


# Generated at 2022-06-12 23:00:52.102336
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immutableDict1 = ImmutableDict({"key1": "value1", "key2": "value2"})
    immutableDict2 = ImmutableDict({"key1": "value1", "key2": "value2"})
    immutableDict3 = ImmutableDict({"key1": "value1", "key2": "value3"})
    mutableDict1 = {"key1": "value1", "key2": "value2"}
    mutableDict2 = {"key1": "value1", "key2": "value2"}
    mutableDict3 = {"key1": "value1", "key2": "value3"}
    assert immutableDict1 == immutableDict1
    assert immutableDict1 == immutableDict2
    assert immutableDict2 == immutableDict1
    assert immutableD

# Generated at 2022-06-12 23:01:00.127714
# Unit test for function is_iterable
def test_is_iterable():
    """Unit tests for the is_iterable function."""
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(tuple())
    assert is_iterable(range(4))
    assert is_iterable(filter(None, [0, 1, 2, 3]))
    assert is_iterable(x for x in range(4))

    assert not is_iterable('abc')
    assert not is_iterable(u'abc')
    assert not is_iterable(1)



# Generated at 2022-06-12 23:01:08.716786
# Unit test for function is_iterable
def test_is_iterable():
    """Unit tests for function is_iterable"""
    assert is_iterable(object) == False
    assert is_iterable(1) == False
    assert is_iterable([]) == True
    assert is_iterable([1, 2, 3]) == True
    assert is_iterable('abc') == True
    assert is_iterable(b'abc') == True
    assert is_iterable({}) == True
    assert is_iterable({'a': '1'}) == True
    assert is_iterable(set([])) == True
    assert is_iterable(set([1, 2, 3])) == True
    import collections
    assert is_iterable(collections.deque([])) == True
    assert is_iterable(collections.deque([1, 2, 3])) == True
    assert is_

# Generated at 2022-06-12 23:01:16.257184
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable(()) is True
    assert is_iterable({}) is True
    assert is_iterable(set()) is True
    assert is_iterable('') is False
    assert is_iterable('abc') is False
    assert is_iterable(b'abc') is False
    assert is_iterable(1) is False
    assert is_iterable(1.0) is False
    assert is_iterable(True) is False
    assert is_iterable(Exception()) is False



# Generated at 2022-06-12 23:01:58.920880
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test if the method __eq__ works properly if the other object is not ImmutableDict
    assert ImmutableDict({'x': 1}) != None
    assert ImmutableDict({'x': 1}) != 'any_string'
    assert ImmutableDict({'x': 1}) != [1, 2, 3]
    assert ImmutableDict({'x': 1}) != (1, 2, 3)
    assert ImmutableDict({'x': 1}) != {'x': 1}

    # Test if the method __eq__ works properly if the other object is ImmutableDict
    assert ImmutableDict({'x': 1}) == ImmutableDict({'x': 1})
    assert ImmutableDict({'x': 1, 'y': 2}) == ImmutableDict({'y': 2, 'x': 1})

# Generated at 2022-06-12 23:02:07.486903
# Unit test for function is_iterable
def test_is_iterable():
    """ Unit test for function is_iterable """
    assert is_iterable([]) is True
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable(set()) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable(dict()) is True
    assert is_iterable(dict([('a', 1), ('b', 2), ('c', 3)])) is True
    assert is_iterable('abc') is True
    assert is_iterable('abc'.split()) is True
    assert is_iterable(1) is False
    assert is_iterable(1.0) is False
    assert is_iterable(object()) is False


# Generated at 2022-06-12 23:02:18.763665
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immutable_mapping = ImmutableDict({'a': 'b', 'c': 'd'})

    # Simply another ImmutableDict
    another_immutable_mapping = ImmutableDict({'a': 'b', 'c': 'd'})
    assert immutable_mapping == another_immutable_mapping
    assert not immutable_mapping != another_immutable_mapping

    # A dict
    assert immutable_mapping == {'a': 'b', 'c': 'd'}
    assert not immutable_mapping != {'a': 'b', 'c': 'd'}

    # A list
    assert not immutable_mapping == ['a', 'b', 'c', 'd']
    assert immutable_mapping != ['a', 'b', 'c', 'd']

    # A tuple
    assert immutable_m

# Generated at 2022-06-12 23:02:27.318524
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a=1, b=2)
    d2 = ImmutableDict(a=1, b=2)
    d3 = ImmutableDict(a=1, b=3)
    d4 = ImmutableDict(a=1, b=2, c=3)
    assert d1 == d2
    assert d1 != d3
    assert d1 != d4

    d5 = MutableMapping(a=1, b=2)
    assert d1 == d5
    d5['c'] = 3
    assert d1 != d5

# Generated at 2022-06-12 23:02:34.034669
# Unit test for function is_iterable
def test_is_iterable():
    test_dict = {'one': 1, 'two': 2, 'three': 3}
    assert is_iterable(test_dict)
    test_string = 'abc'
    assert is_iterable(test_string)
    test_string = 'abc'
    assert is_iterable(test_string)

    test_list = [1, 2, 3]
    assert is_iterable(test_list)
    assert is_iterable(test_list, include_strings=True)
    assert is_iterable(test_string, include_strings=True)



# Generated at 2022-06-12 23:02:44.537390
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    def assertImmutableDictEquals(immutableDict1, immutableDict2):
        assert immutableDict1 == immutableDict2
        assert hash(immutableDict1) == hash(immutableDict2)

    def assertImmutableDictNotEquals(immutableDict1, immutableDict2):
        assert immutableDict1 != immutableDict2
        assert hash(immutableDict1) != hash(immutableDict2)

    def assertImmutableDictEqualsRegularDict(immutableDict, regularDict):
        assert immutableDict == regularDict
        assert hash(immutableDict) == hash(regularDict)

    def assertRegularDictEqualsImmutableDict(regularDict, immutableDict):
        assert regularDict == immutableDict
        assert hash(regularDict)

# Generated at 2022-06-12 23:02:50.794605
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable('')
    assert is_iterable(u'')
    assert is_iterable(b'')
    assert is_iterable(xrange(0))
    assert is_iterable(range(0))
    assert is_iterable(0)
    assert is_iterable(0.0)
    assert is_iterable(False)
    assert not is_iterable(None)



# Generated at 2022-06-12 23:02:56.888835
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert is_iterable(())
    assert is_iterable((1, 2, 3))
    assert is_iterable({})
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable('abc')
    assert is_iterable(b'abc')
    assert not is_iterable(1)
    assert not is_iterable(None)



# Generated at 2022-06-12 23:03:07.135226
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    class FakeImmutableDict(ImmutableDict):
        pass

    class MismatchDict(Mapping):
        def __init__(self, *args, **kwargs):
            self._store = dict(*args, **kwargs)

        def __getitem__(self, key):
            return self._store[key]

        def __iter__(self):
            return self._store.__iter__()

        def __len__(self):
            return self._store.__len__()

    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    d3 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})

# Generated at 2022-06-12 23:03:11.302777
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) == True
    assert is_iterable(set()) == True
    assert is_iterable(tuple()) == True
    assert is_iterable(dict()) == True
    assert is_iterable(int()) == False
    assert is_iterable(str()) == True
    assert is_iterable("") == True

# Generated at 2022-06-12 23:04:30.431720
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = ImmutableDict({'a': 1, 'c':3})
    dict2 = ImmutableDict({'a': 1, 'c':3})
    dict3 = ImmutableDict({'a': 0, 'c':3})
    dict4 = {'a': 1, 'c':3}
    dict5 = ImmutableDict({'a': 1, 'c':3, 'd': 4})
    dict6 = ImmutableDict({'a': 1, 'c':3, 'd': 5})
    dict7 = ImmutableDict({'a': 1, 'c':3, 'e': [{'f': 1}, {'f': 2}]})

# Generated at 2022-06-12 23:04:37.589526
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(dict())
    assert not is_iterable(3)
    assert not is_iterable('test')
    assert is_iterable('test', include_strings=True)
    assert not is_iterable(u'test')
    assert is_iterable(u'test', include_strings=True)
    assert not is_iterable(b'test')
    assert is_iterable(b'test', include_strings=True)



# Generated at 2022-06-12 23:04:40.349193
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert not is_iterable(object())
    assert is_iterable(1)
    assert is_iterable(True)


# Generated at 2022-06-12 23:04:48.146156
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict

    The method __eq__ returns True when an ImmutableDict is equal
    to another ImmutableDict or to a regular dict.
    """
    regular_dict = dict(test_key='test_value')
    immutable_dict = ImmutableDict(test_key='test_value')

    assert(regular_dict == immutable_dict)
    assert(immutable_dict == regular_dict)

    assert(not dict(test_key='test_value2') == immutable_dict)
    assert(not immutable_dict == dict(test_key='test_value2'))

    # Test with an object that is not a dict
    assert(not immutable_dict == 'test_value')

# Generated at 2022-06-12 23:04:55.930286
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test method __eq__ of class ImmutableDict"""
    def test_equal(first, second):
        assert (first == second) and (second == first)
    test_equal(ImmutableDict(), ImmutableDict())
    test_equal(ImmutableDict(foo='bar'), ImmutableDict(foo='bar'))
    test_equal(ImmutableDict(foo=42), ImmutableDict(foo=42))
    test_equal(ImmutableDict(foo={'a': 'b'}), ImmutableDict(foo={'a': 'b'}))
    test_equal(ImmutableDict(foo=['a', 'b']), ImmutableDict(foo=['a', 'b']))

# Generated at 2022-06-12 23:05:01.411606
# Unit test for function is_iterable
def test_is_iterable():
    """ Unit tests to ensure that the is_iterable function works as intended """
    assert is_iterable([1])
    assert is_iterable((1,))
    assert is_iterable({})
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert is_iterable('string') != is_iterable(b'bytes')



# Generated at 2022-06-12 23:05:10.580370
# Unit test for function is_iterable
def test_is_iterable():
    # on python 2 strings are iterable, on python 3 they are not, so we need to do the following
    # check to make sure the function returns the expected value
    seq = 'test'
    assert is_iterable(seq)

    seq = 'test'
    assert not is_iterable(seq, include_strings=False)

    seq = ['test']
    assert is_iterable(seq)

    seq = {'test': 'test'}
    assert is_iterable(seq)

    seq = 'test'
    assert not is_iterable(seq)

    class Test():
        pass
    seq = Test()
    assert not is_iterable(seq)

    seq = 1
    assert not is_iterable(seq)


# Generated at 2022-06-12 23:05:13.893272
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(foo='bar')
    b = ImmutableDict(foo='bar')
    c = ImmutableDict(bar='bar')
    # equal
    assert a == b
    # not equal
    assert a != c
    assert a != 'abc'


# Generated at 2022-06-12 23:05:18.185184
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable(42)
    assert is_iterable('foo')
    assert is_iterable(bytearray(b'foo'))
    assert not is_iterable(None)



# Generated at 2022-06-12 23:05:28.822505
# Unit test for function is_iterable
def test_is_iterable():
    """
    Function to test the functionality of function is_iterable().
    """
    # Test empty list
    if not is_iterable([]):
        raise Exception('List is not identified as an iterable')

    # Test non-empty list
    if not is_iterable([1]):
        raise Exception('List is not identified as an iterable')

    # Test string
    if is_iterable('Test String', include_strings=False):
        raise Exception('String is identified as an iterable')

    # Test empty dictionary
    if not is_iterable({}):
        raise Exception('Dictionary is not identified as an iterable')

    # Test non-empty dictionary
    if not is_iterable({'key': 'value'}):
        raise Exception('Dictionary is not identified as an iterable')

    # Test empty tuple
   