

# Generated at 2022-06-12 22:56:06.377929
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    common_dict = {"a": 1, "b": 2, "c": 3}
    common_dict2 = {"e": 5, "b": 7, "c": 5}

    dict1 = ImmutableDict(common_dict)
    dict2 = dict1.union(common_dict2)
    dict3 = dict2.difference(["a", "e"])
    assert dict1 == dict3

# Generated at 2022-06-12 22:56:09.385621
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) == True
    assert is_iterable(tuple()) == True
    assert is_iterable({}) == True
    assert is_iterable(set()) == True
    assert is_iterable(x for x in range(10)) == True
    assert is_iterable(1) == False
    assert is_iterable(None) == False


# Generated at 2022-06-12 22:56:16.882765
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():

    test_input = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert test_input.difference(['a']) == ImmutableDict({'b': 2, 'c': 3})
    assert test_input.difference(['b', 'c']) == ImmutableDict({'a': 1})
    assert test_input.difference(['d']) == test_input
    assert test_input.difference(['a', 'b', 'c', 'd']) == ImmutableDict()
    assert test_input.difference([]) == test_input



# Generated at 2022-06-12 22:56:25.840043
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    """Test that difference method returns a new immutable dictionary."""
    test_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert test_dict.difference(['c']) == ImmutableDict({'a': 1, 'b': 2})
    assert test_dict.difference(['b']) == ImmutableDict({'a': 1, 'c': 3})
    assert test_dict.difference(['a', 'b']) == ImmutableDict({'c': 3})
    assert test_dict.difference(['a', 'b', 'c']) == ImmutableDict({})



# Generated at 2022-06-12 22:56:32.050211
# Unit test for function is_iterable
def test_is_iterable():

    """Unit test for function is_iterable"""

    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable({})
    assert is_iterable((x for x in range(2)))
    assert is_iterable('abc')
    assert is_iterable(b'abc')
    assert not is_iterable(1)
    assert not is_iterable(object())
    assert not is_iterable(None)



# Generated at 2022-06-12 22:56:36.779583
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import sys

    sys.modules['ansible.module_utils.common._collections_compat'] = sys.modules['collections']

    # ImmutableDict objects equal to themselves
    print((ImmutableDict() == ImmutableDict()))
    print((ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})))

    # ImmutableDict objects equal to their counterparts
    print((ImmutableDict() == {}))
    print((ImmutableDict({'a': 1}) == {'a': 1}))

    # ImmutableDict objects not equal to the object of the different type with the same content
    print((ImmutableDict() == ()))
    print((ImmutableDict({'a': 1}) == ('a', 1)))

    # ImmutableDict objects not equal to the object of the

# Generated at 2022-06-12 22:56:40.598142
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    Dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    Dict_copy = Dict.difference({'c', 'd'})
    assert Dict_copy == {'a': 1, 'b': 2}



# Generated at 2022-06-12 22:56:47.821994
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    firstDict = ImmutableDict(firstDictKey1="firstDictValue1", firstDictKey2="firstDictValue2")
    secondDict = ImmutableDict(secondDictKey1="secondDictValue1", secondDictKey2="secondDictValue2")
    assert secondDict.difference([]) == secondDict.difference(())
    assert secondDict.difference({}) == secondDict.difference([])
    assert secondDict.difference(firstDict) == secon

# Generated at 2022-06-12 22:56:52.177400
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict({"a": 1, "b": 2, "c": 3, "d": 4})
    result = original.difference(("b", "c"))
    assert result == ImmutableDict({"a": 1, "d": 4})


# Generated at 2022-06-12 22:57:01.387017
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # case 1: two equal dicts
    dict1 = ImmutableDict({1: 'one', 2: 'two'})
    dict2 = ImmutableDict({1: 'one', 2: 'two'})
    assert dict1 == dict2, "Two equal dicts should be equal"

    # case 2: two not equal dicts
    dict1 = ImmutableDict({1: 'one', 2: 'two'})
    dict2 = ImmutableDict({1: 'one', 2: 'three'})
    assert dict1 != dict2, "Two not equal dicts should not be equal"

    # case 3: dict that is not a dict
    dict1 = ImmutableDict({1: 'one', 2: 'two'})
    not_a_dict = 'immutable'

# Generated at 2022-06-12 22:57:13.271926
# Unit test for function is_iterable
def test_is_iterable():
    valid_in_iterability = [
        (),
        tuple(),
        [],
        [3, 4, 5],
        set(),
        {'a': 1, 'b': 2},
        {},
        '',
        'string',
        u'unicode',
        b'bytes'
    ]
    invalid_in_iterability = [
        1,
        'a',
        2.5,
        None
    ]

    # Test iterability
    for elem in valid_in_iterability:
        assert is_iterable(elem)
    # Test non-iterability
    for elem in invalid_in_iterability:
        assert not is_iterable(elem)

# Generated at 2022-06-12 22:57:20.933779
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of ImmutableDict class"""
    test_dict = ImmutableDict({'one': 1, 'two': 2})
    assert test_dict.__eq__({'one': 1, 'two': 2})
    assert test_dict.__eq__(ImmutableDict({'one': 1, 'two': 2}))
    assert test_dict.__eq__(MutableMapping([('one', 1), ('two', 2)]))
    assert test_dict.__eq__(MutableMapping({'one': 1, 'two': 2}))
    assert test_dict.__eq__({'two': 2, 'one': 1})
    assert test_dict.__eq__(ImmutableDict({'two': 2, 'one': 1}))

# Generated at 2022-06-12 22:57:29.147434
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    t = ImmutableDict({'a': 1, 'b': {'x': 5, 'y': 7}})
    # test when keys and values of t1 and t2 are equal
    t1 = ImmutableDict({'a': 1, 'b': {'x': 5, 'y': 7}})
    assert t == t1
    assert id(t) == id(t1)
    # test when keys and values of t2 are different
    t1 = ImmutableDict({'a': 1, 'b': {'x': 5, 'y': 9}})
    assert t != t1


# Generated at 2022-06-12 22:57:38.913931
# Unit test for method __eq__ of class ImmutableDict

# Generated at 2022-06-12 22:57:46.501244
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # comparison of ImmutableDict instances
    immutable_dict_1 = {1: '1', 2: '2', 3: '3'}
    immutable_dict_2 = {1: '1', 2: '2', 3: '3'}
    immutable_dict = ImmutableDict(immutable_dict_1)
    assert immutable_dict == immutable_dict
    assert immutable_dict != immutable_dict_1
    assert immutable_dict != immutable_dict_2
    assert immutable_dict != {1: '1', 2: '2', 3: '3'}
    assert immutable_dict != {1: '1', 2: '2', 3: '4'}
    # comparison of ImmutableDict and dict
    assert immutable_dict == {1: '1', 2: '2', 3: '3'}
    assert immutable_

# Generated at 2022-06-12 22:57:52.244762
# Unit test for function is_iterable
def test_is_iterable():
    """Test the is_iterable function.
    """

    assert is_iterable([True]) is True
    assert is_iterable({'key':'value'}) is True
    assert is_iterable((1,2,3)) is True
    assert is_iterable(1) is False
    assert is_iterable('this is a string') is True

    assert is_iterable('this is a string', include_strings=False) is False
    assert is_iterable('this is a string', include_strings=True) is True


# Generated at 2022-06-12 22:57:57.265290
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1}) == {'a': 1}
    assert ImmutableDict({'a': 1}) != ImmutableDict({'b': 2})
    assert ImmutableDict({'a': 1}) != {'b': 2}


# Generated at 2022-06-12 22:58:01.023062
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable((1, 2, 3))
    assert not is_iterable(2)
    assert not is_iterable('foo')



# Generated at 2022-06-12 22:58:07.827582
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2)
    assert not ImmutableDict(a=1, b=3) == ImmutableDict(a=1, b=2)
    assert not ImmutableDict(a=1, b=2) == dict(a=1, b=2)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=1)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2, c=3)


# Generated at 2022-06-12 22:58:12.106716
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict = ImmutableDict(test=1, foo=2)
    assert test_dict == test_dict
    assert not test_dict == {'test': 1, 'foo': 2}
    assert not test_dict == ImmutableDict(test=1, foo=3)

# Generated at 2022-06-12 22:58:26.215979
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test case 1: Two empty dictionaries are equal
    test_case_1_dict_a = ImmutableDict()
    test_case_1_dict_b = ImmutableDict()
    test_case_1_result = test_case_1_dict_a == test_case_1_dict_b
    assert test_case_1_result

    # Test case 2: Two non-empty dictionaries which contain the same key-value pairs are equal
    test_case_2_dict_a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    test_case_2_dict_b = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    test_case_2_result = test_case_2_dict_a == test_case_2_dict

# Generated at 2022-06-12 22:58:30.764048
# Unit test for function is_iterable
def test_is_iterable():
    from ansible.module_utils.common._collections_compat import defaultdict

    my_iter = ['foo', 'bar', 'baz']
    my_string = "foo"
    my_defaultdict = defaultdict(lambda: 'bar')

    assert is_iterable(my_iter)
    assert not is_iterable(my_string)
    assert is_iterable(my_defaultdict)


# Generated at 2022-06-12 22:58:32.781944
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(ImmutableDict())
    assert not is_iterable(None)
    assert not is_iterable(42)



# Generated at 2022-06-12 22:58:42.858209
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test method __eq__ of class ImmutableDict"""
    import pytest
    from collections import OrderedDict, Mapping

    ordered_dict = OrderedDict(a=1, b=2)


# Generated at 2022-06-12 22:58:53.111710
# Unit test for function is_iterable
def test_is_iterable():
    """Test is_iterable

    Verifies that is_iterable returns the correct values for common iterable and non
    iterable types.
    """

    assert is_iterable('')
    assert is_iterable('This is a test string')
    assert is_iterable(b'This is a test bytes')
    assert not is_iterable(b'This is a test bytes', include_strings=True)
    assert not is_iterable('This is a test string', include_strings=True)
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({'key1': 'value1', 'key2': 'value2'})
    assert is_iterable(set('1,2,3'))
    assert is_iterable(5)

# Generated at 2022-06-12 22:58:55.844042
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable('string')
    assert not is_iterable(1)
    assert is_iterable([1])
    assert is_iterable(dict())
    assert is_iterable('string', include_strings=True)


# Generated at 2022-06-12 22:59:07.789426
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from collections.abc import Mapping
    from collections import namedtuple

    # create some immutable objects
    immutable_dict = ImmutableDict(a=1, b=2)
    immutable_list = tuple([1, 2])
    immutable_tuple = (1, 2)

    # non-mappings
    assert immutable_dict != immutable_list
    assert immutable_dict != immutable_tuple

    # non-mapping immutables
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2)
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=2, b=2)

    # non-

# Generated at 2022-06-12 22:59:14.326590
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test ImmutableDict eq to ImmutableDict
    assert ImmutableDict({"a": 1, "b": 2}) == ImmutableDict({"a": 1, "b": 2})
    assert ImmutableDict({"a": 2, "b": 1}) != ImmutableDict({"a": 1, "b": 2})
    # Test ImmutableDict eq to non ImmutableDict
    assert ImmutableDict({"a": 1, "b": 2}) != {"a": 1, "b": 2}



# Generated at 2022-06-12 22:59:24.353201
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""
    test_dict_1 = ImmutableDict({1: 2, 3: 4})
    test_dict_2 = ImmutableDict({3: 4, 1: 2})
    assert test_dict_1 == test_dict_2
    assert test_dict_2 == test_dict_1
    test_dict_3 = ImmutableDict({1: 2, 3: 4, 5: 6})
    assert test_dict_3 != test_dict_2
    assert test_dict_2 != test_dict_3
    test_dict_4 = ImmutableDict({1: 2, 3: 4, 7: 6})
    assert test_dict_4 != test_dict_1
    assert test_dict_1 != test_dict_4
    test_dict_5

# Generated at 2022-06-12 22:59:34.932070
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable('str')
    assert not is_iterable(u'unicode')
    # bytes
    assert not is_iterable(b'bytes')

    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(dict())

    assert is_iterable(range(10))
    assert is_iterable(xrange(10))
    assert is_iterable(map(lambda x: x, range(10)))
    assert is_iterable(filter(lambda x: x, range(10)))
    assert is_iterable(yielded_range(10))

    assert is_iterable('str', include_strings=True)
    assert is_iterable(u'unicode', include_strings=True)

# Generated at 2022-06-12 22:59:48.447478
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict(a=1, b=2) == {'a': 1, 'b': 2}
    assert ImmutableDict(a=1, b=2) == {'b': 2, 'a': 1}
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=3)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=2, b=2)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(c=1, d=2)

# Generated at 2022-06-12 22:59:57.928257
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable(dict(a=1, b=2)) is True
    assert is_iterable(xrange(3)) is True
    assert is_iterable(MutableMapping()) is True
    assert is_iterable(None) is False
    assert is_iterable(1) is False
    assert is_iterable(Exception) is False
    assert is_iterable('abc') is False
    assert is_iterable(b'abc') is False
    assert is_iterable(set([1, 2, 3]), include_strings=True) is True


# Unit test function is_sequence

# Generated at 2022-06-12 23:00:07.424643
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert is_iterable(('a', 'b', 'c'))
    assert is_iterable({'a': 1, 'b': 2, 'c': 3})
    assert is_iterable({1, 2, 3})
    assert is_iterable(mappingproxy({'a': 1, 'b': 2, 'c': 3}))
    assert is_iterable(range(0))
    assert is_iterable(range(10))
    assert is_iterable(xrange(10))

    assert is_iterable(b'abc')
    assert is_iterable(bytearray(b'abc'))
    assert is_iterable(memoryview(bytearray(b'abc')))
    assert is_iter

# Generated at 2022-06-12 23:00:15.079124
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    k = ImmutableDict({'one': 1, 'two': 2})
    l = ImmutableDict({'one': 1, 'two': 2})
    m = ImmutableDict({'one': 1, 'two': 2})
    assert k == l, "ImmutableDict__eq__ fails"

    n = ImmutableDict({'one': 1, 'two': 2, 'three': 3})
    assert k != n, "ImmutableDict__eq__ fails"

    assert k == m, "ImmutableDict__eq__ fails"


# Generated at 2022-06-12 23:00:24.178839
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from pytest import raises, skip
    from ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock import MagicMock
    orig_dict = ImmutableDict({'foo': 'bar'})
    mock_dict = MagicMock()
    mock_dict.__iter__.return_value = 'foo', 'bar'
    mock_dict.__hash__.return_value = 42
    assert orig_dict != mock_dict
    with raises(TypeError):
        orig_dict == None
    skip("__eq__ behavior must be consistent with __hash__")
    assert orig_dict == orig_dict
    eq_dict_1 = ImmutableDict({'foo': 'bar'})
    eq_dict_2 = ImmutableDict({'foo': 'bar'})
    assert eq_dict

# Generated at 2022-06-12 23:00:34.628401
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable."""
    from ansible.module_utils.six import string_types, integer_types, binary_type

    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(u"abc")
    assert is_iterable(b"abc")

    assert not is_iterable(5)
    assert not is_iterable(5.5)

    assert is_iterable((x for x in range(10)))

    assert is_iterable(string_types)
    assert is_iterable(integer_types)
    assert is_iterable(binary_type)

    assert not is_iterable(string_types, include_strings=False)
    assert not is_iterable

# Generated at 2022-06-12 23:00:43.140274
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert not is_iterable(42)
    assert not is_iterable(set())
    assert not is_iterable(1337j)
    assert not is_iterable(lambda: None)

    assert is_iterable('')
    assert is_iterable('42')
    assert is_iterable(b'')
    assert is_iterable(b'42')

    assert is_iterable([])
    assert is_iterable([42])
    assert is_iterable({})
    assert is_iterable({'42': 0})
    x = iter(range(42))
    assert is_iterable(x)
    assert is_iterable(x)  # multiple calls don't change it



# Generated at 2022-06-12 23:00:54.546448
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Checks the equality implementation of ImmutableDict
    """
    a = ImmutableDict(a=1, b=2)
    b = ImmutableDict(a=1, b=2)
    c = ImmutableDict(a=1, c=2)
    d = ImmutableDict()
    e = dict()

    assert a == a
    assert a == b
    assert b == a
    assert a != c
    assert c != a
    assert d == d
    assert d == e
    assert e == d
    assert d != a
    assert a != d

    assert a != 1
    assert a != 'a'
    assert a != tuple()
    assert a != dict()
    assert a != set()
    assert a != ImmutableDict(a=1, b=1)
    assert a

# Generated at 2022-06-12 23:01:00.017211
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a1 = ImmutableDict({'a': 1, 'b': 2})
    a2 = ImmutableDict({'a': 1, 'b': 2})
    assert a1 == a2, 'This test failed'
    b1 = ImmutableDict({'a': 2, 'b': 2})
    assert not (a1 == b1), 'This test failed'



# Generated at 2022-06-12 23:01:06.343778
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable({})
    assert is_iterable(range(10))
    assert is_iterable('')
    assert is_iterable(b'')
    assert is_iterable(b'foo')
    assert is_iterable('foo')
    assert is_iterable(2) is False
    assert is_iterable(open('.'))
    assert is_iterable(list([1, 2, 3]))



# Generated at 2022-06-12 23:01:28.641770
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immut_dict_1 = ImmutableDict({"key_1": "value_1", "key_2": "value_2"})
    immut_dict_2 = ImmutableDict({"key_1": "value_1", "key_2": "value_2"})
    immut_dict_3 = ImmutableDict({"key_1": "value_1", "key_2": "value_3"})
    immut_dict_4 = ImmutableDict({"key_1": "value_3", "key_2": "value_2"})
    immut_dict_5 = ImmutableDict({"key_2": "value_2", "key_1": "value_1"})

    assert immut_dict_1 == immut_dict_1
    assert immut_dict_1

# Generated at 2022-06-12 23:01:36.725884
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert not is_iterable(3)
    assert not is_iterable(3.14)
    assert is_iterable('test')
    assert is_iterable([]) # empty list
    assert is_iterable([1, 2, 3])
    assert is_iterable(tuple()) # empty tuple
    assert is_iterable(tuple([1, 2, 3]))
    assert is_iterable(set()) # empty set
    assert is_iterable({1, 2, 3}) # set
    assert is_iterable(range(5)) # range
    assert is_iterable({'key1': 'val1'})
    assert is_iterable(('key1', 'val1'))

    # Include string-like types

# Generated at 2022-06-12 23:01:46.363195
# Unit test for function is_iterable
def test_is_iterable():
    fail_list = [
        'string',
        123,
        None,
        True,
        False,
        b'str',
        bytearray(b'bytearray'),
    ]
    for item in fail_list:
        assert is_iterable(item, True) == False

    success_list = [
        {'foo': 'bar'},
        [1, 2, 3],
        ('foo', 'bar'),
        xrange(0, 10),
    ]
    for item in success_list:
        assert is_iterable(item, True) == True

    assert is_iterable('str', False) == False
    assert is_iterable('str', True) == True
    assert is_iterable(b'str', False) == False

# Generated at 2022-06-12 23:01:51.902990
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable({}) is True
    assert is_iterable(()) is True
    assert is_iterable(set()) is True

    class Iterable(object):
        def __iter__(self):
            return iter([])

    assert is_iterable(Iterable()) is True

    assert is_iterable(u'123') is False
    assert is_iterable(b'123') is False
    assert is_iterable(3) is False



# Generated at 2022-06-12 23:01:57.043190
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(set())
    assert is_iterable(list())
    assert is_iterable(tuple())

    assert is_iterable(set([1, 2, 3]))
    assert is_iterable(list([1, 2, 3]))
    assert is_iterable(tuple([1, 2, 3]))

    assert is_iterable("")
    assert is_iterable("a")
    assert is_iterable("abc")

    assert is_iterable(bytearray("abc"))
    assert is_iterable(bytearray(""))

    assert not is_iterable({})
    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(0.5)
    # On Python 3, strings are a sequence, but not

# Generated at 2022-06-12 23:02:05.338996
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable"""
    assert is_iterable(list())
    assert is_iterable('')
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable(0)
    assert is_iterable(0.0)
    assert is_iterable(None)
    assert is_iterable((x for x in range(0)))
    assert is_iterable(['a', 1])
    assert is_iterable(('a', 1))

    assert not is_iterable(list(), include_strings=True)
    assert is_iterable('', include_strings=True)
    assert is_iterable(set(), include_strings=True)
    assert is_iterable(dict(), include_strings=True)

# Generated at 2022-06-12 23:02:14.144579
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # should return true if two immutable dictionaries have the same keys and values
    assert ImmutableDict(a='b', c='d') == ImmutableDict(a='b', c='d')
    # should return false if two immutable dictionaries don't have the same keys and values
    assert not ImmutableDict(a='b') == ImmutableDict(c='d')
    assert not ImmutableDict(a='b') == ImmutableDict(a='b', c='d')
    assert not ImmutableDict(a='b', c='d') == ImmutableDict(a='b', c='e')


# Generated at 2022-06-12 23:02:25.258291
# Unit test for function is_iterable
def test_is_iterable():
    class iterable_class:
        def __iter__(self):
            yield 1
    # object instance that is iterable
    assert(is_iterable(iterable_class()))
    # list
    assert(is_iterable([1, 2, 3]))
    # set
    assert(is_iterable({1, 2, 3}))
    # tuple
    assert(is_iterable((1, 2, 3)))
    # dict
    assert(is_iterable({1:2, 3:4}))
    # string
    assert(is_iterable('hello'))
    # string with include_string=True
    assert(is_iterable('hello', True))
    # int
    assert(not is_iterable(1))
    # float
    assert(not is_iterable(1.0))


# Generated at 2022-06-12 23:02:32.090336
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'A': 'B'}) == ImmutableDict({'A': 'B'})
    assert ImmutableDict({'A': 'B'}) != ImmutableDict({'A': 'C'})
    assert ImmutableDict({'A': 'C'}) != ImmutableDict({'A': 'B', 'C': 'D'})
    assert ImmutableDict({'A': 'B', 'C': 'D'}) != ImmutableDict({'A': 'B'})


# Generated at 2022-06-12 23:02:36.463094
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) == True
    assert is_iterable(xrange(0, 5)) == True
    assert is_iterable('test') == False
    assert is_iterable({'el1': 1, 'el2': 2}) == True
    assert is_iterable((1, 2, 3)) == True
    assert is_iterable(1) == False
    assert is_iterable(None) == False


# Generated at 2022-06-12 23:03:04.719421
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable(set()) is True
    assert is_iterable(tuple()) is True
    assert is_iterable(xrange(0)) is True
    assert is_iterable(1) is False
    assert is_iterable(None) is False



# Generated at 2022-06-12 23:03:13.953622
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})  # 1st object (1st object is equal to itself)
    b = ImmutableDict({'a': 1, 'b': 2, 'c': 3})  # 2nd object (2nd object is equal to itself)
    c = ImmutableDict({'1': 'a', '2': 'b', '3': 'c'})  # 3rd object (3rd object is not equal to 2nd)

    assert a == a  # 1st object is equal to itself
    assert a == b  # 1st and 2nd objects are equal
    assert b == a  # 2nd and 1st objects are equal
    assert b == b  # 2nd object is equal to itself
    assert not (a == c)  # 1st and 3rd objects are

# Generated at 2022-06-12 23:03:16.537826
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable({'a': 1}) is True
    assert is_iterable(1) is False
    assert is_iterable(()) is True
    assert is_iterable([]) is True



# Generated at 2022-06-12 23:03:26.373874
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""

    # Use dicts
    dict1 = dict(a=1, b=2)
    dict2 = dict1.copy()

    assert dict1 == dict2

    # Use ImmutableDict
    immutable_dict1 = ImmutableDict(a=1, b=2)
    immutable_dict2 = ImmutableDict(a=1, b=2)
    immutable_dict3 = ImmutableDict(a=1, c=2)

    assert immutable_dict1 == immutable_dict2
    assert immutable_dict1 != immutable_dict3

    # Use dicts and ImmutableDict
    assert dict1 == immutable_dict1
    assert dict2 == immutable_dict2

    # Use lists

# Generated at 2022-06-12 23:03:33.537334
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    tdict1 = ImmutableDict({1:'ABC', 2:'DEF', 3:'GHI'})
    tdict2 = ImmutableDict({1:'ABC', 2:'DEF', 3:'GHI'})
    tdict3 = ImmutableDict({1:'ABC', 3:'GHI', 2:'DEF'})
    tdict4 = ImmutableDict({1:'ABC', 2:'DEF', 3:'GHI', 4:'JKL'})
    tdict5 = ImmutableDict({1:'ABC', 3:'GHI'})
    tdict6 = ImmutableDict({'ABC':1, 2:'DEF', 3:'GHI'})
    tdict7 = ImmutableDict({1:'ABC', 2:'DEF', 3:'GHI'})
    tdict7._store[4] = 'JKL'

# Generated at 2022-06-12 23:03:44.038568
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test for __eq__ method of ImmutableDict class"""
    class CustomHashable(object):
        """Custom object that implements __hash__ method"""
        def __hash__(self):
            return id(self)


# Generated at 2022-06-12 23:03:51.365342
# Unit test for function is_iterable
def test_is_iterable():
    class Test(object):
        def __iter__(self):
            return iter(["item1", "item2"])

    string = "string"
    ints = 1
    list = ["item1", "item2"]
    tuple = ("item1", "item2")
    set = {"item1", "item2"}
    test = Test()

    assert is_iterable(string)
    assert is_iterable(ints)
    assert is_iterable(list)
    assert is_iterable(tuple)
    assert is_iterable(set)
    assert is_iterable(test)



# Generated at 2022-06-12 23:04:00.006400
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # test is not equal to none
    test1 = ImmutableDict({"test_key1": 1, "test_key2": 2, "test_key3": 3})
    assert test1 != None
    # test is equal to itself
    assert test1 == test1
    # test is equal to the same dict
    test2 = ImmutableDict({"test_key1": 1, "test_key2": 2, "test_key3": 3})
    assert test1 == test2
    # test is not equal to dict with different key-value pairs
    test3 = ImmutableDict({"test_key1": 1, "test_key2": 2, "test_key3": 4})
    assert test1 != test3
    # test is not equal to dict with different key-value pairs

# Generated at 2022-06-12 23:04:10.253587
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable."""
    assert is_iterable([]) == True
    assert is_iterable({}) == True
    assert is_iterable(set()) == True
    assert is_iterable(()) == True
    assert is_iterable(xrange(1, 10)) == True
    assert is_iterable('abc') == True
    assert is_iterable('abc' * 1000) == True
    assert is_iterable(b'abc') == True
    assert is_iterable(b'abc' * 1000) == True
    assert is_iterable(10) == False
    assert is_iterable(None) == False



# Generated at 2022-06-12 23:04:15.696410
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immutable_dict1 = ImmutableDict(dict(key1=1, key2=2))
    immutable_dict2 = ImmutableDict(dict(key1=1, key2=2))
    assert immutable_dict1 == immutable_dict2
    assert immutable_dict1 == dict(key1=1, key2=2)
    assert immutable_dict1 == dict(key2=2, key1=1)
    assert immutable_dict1 != dict(key2=2)
    assert immutable_dict1 != dict()



# Generated at 2022-06-12 23:05:13.974810
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immutable_dict = ImmutableDict()
    assert immutable_dict == {}
    assert immutable_dict == immutable_dict
    assert immutable_dict != None

    immutable_dict2 = ImmutableDict()
    assert immutable_dict == immutable_dict2

    immutable_dict_not_equal = ImmutableDict({'key': 'value'})
    assert immutable_dict != immutable_dict_not_equal

    immutable_dict_not_equal = ImmutableDict({'key': 'value', 'key2': 'value2'})
    assert immutable_dict != immutable_dict_not_equal

    immutable_dict2 = ImmutableDict({'key': 'value'})
    assert immutable_dict_not_equal == immutable_dict2


# Generated at 2022-06-12 23:05:22.935202
# Unit test for function is_iterable
def test_is_iterable():
    """Test identification of iterable items"""
    iterable_list = ['a', 'b', 'c']
    iterable_tuple = ('a', 'b', 'c')
    iterable_set = set(iterable_list)
    iterable_dict = {'a': 'b', 'c': 'd'}
    iterable_str = 'abc'
    iterable_bytes = b'abc'

    non_iterable_int = 42
    non_iterable_float = 3.14
    non_iterable_str = 'abc'
    non_iterable_bytes = b'abc'

    assert is_iterable(iterable_list) is True
    assert is_iterable(iterable_tuple) is True
    assert is_iterable(iterable_set) is True

# Generated at 2022-06-12 23:05:33.381986
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'d': 4, 'e': 5, 'f': 6})
    c = ImmutableDict(a, **b)

    # return false for different types
    assert a != []

    # return false for different contents
    assert a != {'a': 1, 'b': 2, 'c': 3}

    # return false for different contents
    assert a != {'a': 1, 'b': 2}

    # return false for different contents
    assert a != {'a': '1', 'b': 2, 'c': 3}

    # return true for same content
    assert a == {'a': 1, 'b': 2, 'c': 3}

    # return false for different content
    assert a

# Generated at 2022-06-12 23:05:40.961561
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict(foo='bar') == ImmutableDict(foo='bar')
    assert ImmutableDict(foo='bar') != ImmutableDict(foo='baz')
    assert ImmutableDict(foo='bar') != ImmutableDict(baz='bar')
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() != ImmutableDict(foo='bar')
    assert ImmutableDict(foo='bar') != ImmutableDict()
    assert ImmutableDict(1, foo='bar') != ImmutableDict(1, bar='foo')

# Generated at 2022-06-12 23:05:48.417937
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    >>> dictionary = ImmutableDict({'a': 123, 'b': 456})
    >>> dictionary2 = ImmutableDict({'a': 123, 'b': 456})
    >>> dictionary == dictionary2
    True
    >>> dictionary3 = ImmutableDict({'b': 456, 'a': 123})
    >>> dictionary == dictionary3
    True
    >>> dict_true_hashable = {('a', 1): 2}
    >>> dict_not_hashable = {([1, 2], 'a'): 2}
    >>> dictionary == dict_true_hashable
    True
    >>> dictionary == dict_not_hashable
    False
    """


# Generated at 2022-06-12 23:05:57.151359
# Unit test for function is_iterable
def test_is_iterable():
    string = 'This is a string'
    list_of_strings = ['This', 'is', 'a', 'list', 'of', 'strings']
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list_of_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    list_of_lists_of_tuples = [[(1, 2, 3), (4, 5, 6), (7, 8, 9)]]
    list_of_lists_of_lits = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
    list_of_dicts = [{'this': 'is', 'a': 'dict'}]
    list_of_lists_

# Generated at 2022-06-12 23:06:02.307099
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id1 = ImmutableDict({'a': 1, 'b': 2})
    assert id1 == id1

    id2 = ImmutableDict({'a': 1, 'b': 2})
    assert id1 == id2

    id3 = ImmutableDict({'a': 1, 'b': 3})
    assert id1 != id3

    assert id1 != [1, 2]
