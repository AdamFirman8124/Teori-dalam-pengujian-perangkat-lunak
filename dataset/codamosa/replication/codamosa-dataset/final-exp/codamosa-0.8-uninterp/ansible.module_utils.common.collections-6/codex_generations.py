

# Generated at 2022-06-12 22:56:17.134858
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    element = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 4, 'key5': 5}
    dummy_element = {'key3': 4, 'key4': 5, 'key5': 6}
    set_element = set(['key3', 'key4'])
    test_dict1 = ImmutableDict(element)
    test_dict2 = ImmutableDict(element, **dummy_element)

    expected_result = ImmutableDict(element)

    assert test_dict1.difference(set_element) == expected_result
    assert test_dict2.difference(set_element) == expected_result

# Generated at 2022-06-12 22:56:27.868280
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    from ansible.module_utils.common.collections import ImmutableDict

    original_immut_dict = ImmutableDict(
        {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5, "key6": 6, "key7": 7}
    )

    assert original_immut_dict.difference(("key1", "key2"))._store == {'key3': 3, 'key4': 4, 'key5': 5, 'key6': 6, 'key7': 7}
    assert original_immut_dict.difference(("key1", "key2", "key3", "key4", "key5", "key6", "key7"))._store == {}

# Generated at 2022-06-12 22:56:36.867433
# Unit test for function is_iterable
def test_is_iterable():
    def fails_with(message, *args, **kwargs):
        try:
            is_iterable(*args, **kwargs)
        except:
            return
        raise AssertionError('Expected to fail but actually passed with ' + message)


# Generated at 2022-06-12 22:56:44.279795
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    dict1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    dict2 = dict1.difference(['a', 'b'])
    assert(len(dict2) == 2)
    assert(dict2['c'] == 3)
    assert(dict2['d'] == 4)
    dict3 = dict1.difference(['a', 'b', 'x'])
    assert(len(dict3) == 2)
    assert(dict3['c'] == 3)
    assert(dict3['d'] == 4)

# Generated at 2022-06-12 22:56:55.292626
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    mutable_dict = dict(a=1, b=2)
    immutable_dict = ImmutableDict(mutable_dict)
    assert immutable_dict == ImmutableDict(mutable_dict)
    assert immutable_dict == mutable_dict
    assert immutable_dict == dict(a=1, b=2)
    assert immutable_dict != dict(x=1, y=1)
    assert immutable_dict != dict(a=1, y=1)
    assert immutable_dict != dict(a=2, b=2)
    assert immutable_dict != dict(b=2, a=1)
    assert immutable_dict != dict(b=2)
    assert immutable_dict != dict(a=1)
    assert immutable_dict != dict()
    assert immutable_dict != object()


# Generated at 2022-06-12 22:56:58.753353
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    dict1 = dict(a=1, b=2, c=3, d=4)
    keys = ['a', 'd']
    expected = dict(b=2, c=3)

    assert ImmutableDict(dict1).difference(keys) == ImmutableDict(expected)

# Generated at 2022-06-12 22:57:02.354751
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    """Identifies the removal of keys from an ImmutableDict"""
    mapping = ImmutableDict({'a': 'ACGT', 'b': 'CAAT'})
    removal = 'a'
    result = mapping.difference(removal)
    expected = ImmutableDict({'b': 'CAAT'})

    assert result == expected

# Generated at 2022-06-12 22:57:11.799402
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a='1',b='2')
    d2 = ImmutableDict(a='1',b='2')
    d3 = ImmutableDict(a='1',b='3')
    d4 = MutableMapping(a='1',b='2')
    # __eq__ should be symmetric
    assert d1 == d2
    assert d2 == d1
    # __eq__ handles hash collisions
    assert not d1 == d3
    assert not d3 == d1
    # __eq__ does not work for classes with different __eq__ implementations
    assert not d1 == d4
    assert not d4 == d1



# Generated at 2022-06-12 22:57:19.938206
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """ImmutableDict compares for equality only with other ImmutableDict instances."""
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() != ImmutableDict({'x': 1})
    assert ImmutableDict({'x': 1}) == ImmutableDict({'x': 1})
    assert ImmutableDict({'x': 1}) != ImmutableDict({'x': 2})

    # dict is not equal to ImmutableDict, since ImmutableDict is not a dict
    assert ImmutableDict({'x': 1}) != {'x': 1}

    # hash is unique so they are the same
    assert ImmutableDict({'x': 1}) == ImmutableDict({'x': 1})

# Generated at 2022-06-12 22:57:28.359136
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Unit test for method __eq__ of class ImmutableDict.
    """
    # Test for equality of empty immutable dicts
    assert ImmutableDict() == ImmutableDict()
    # Test for equality of immutable dicts with values
    assert ImmutableDict({1: '1', 2: '2'}) == ImmutableDict({1: '1', 2: '2'})
    # Test for inequality of immutable dicts
    assert not ImmutableDict({1: '1', 2: '2'}) == ImmutableDict({1: '1', 2: '2', 3: '3'})



# Generated at 2022-06-12 22:57:42.502617
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(range(0))
    assert is_iterable(u'string')
    assert is_iterable(b'bytestring')
    assert is_iterable(('a', 'tuple', 1))
    assert is_iterable({'a', 'set'})
    assert is_iterable({'a': 1})
    assert is_iterable(1) is False
    assert is_iterable(True) is False



# Generated at 2022-06-12 22:57:50.862473
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert (ImmutableDict() == ImmutableDict() == {})
    assert (ImmutableDict({'a': 1}) == ImmutableDict({'a': 1}) == {'a': 1})
    assert (ImmutableDict({'a': 1}) != ImmutableDict({'a': 2}) == {'a': 2})
    assert (ImmutableDict({'a': 1}) != ImmutableDict({'b': 1}) == {'b': 1})
    assert (ImmutableDict({'a': 1}) != ImmutableDict({'a': 1, 'b': 2}) == {'a': 1, 'b': 2})
    assert (ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1}) == {'a': 1})


# Generated at 2022-06-12 22:57:59.257694
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    assert d1 == d2
    d3 = ImmutableDict({'a': 1, 'b': 3})
    assert not d1 == d3
    assert not d2 == d3
    # Test equality works with a hashable object
    assert d1 == {'a': 1, 'b': 2}
    d4 = {'a': 1, 'b': 2}
    assert not d1 == d4
    assert not d2 == d4
    assert not d3 == d4



# Generated at 2022-06-12 22:58:05.953113
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable([1]) is True
    assert is_iterable(u"") is True
    assert is_iterable(u"abc") is True
    assert is_iterable(b"") is True
    assert is_iterable(b"abc") is True
    assert is_iterable((1,)) is True
    assert is_iterable((1,2)) is True
    assert is_iterable(1) is False
    assert is_iterable(None) is False
    assert is_iterable(u"abc", include_strings=True) is True


# Generated at 2022-06-12 22:58:17.105735
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['a', 'b', 'c'])
    assert is_iterable((x for x in [1, 2, 3]))
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable(set(['a', 'b', 'c']))
    assert is_iterable(ImmutableDict({1: 'a', 2: 'b', 3: 'c'}))
    assert is_iterable(ImmutableDict({'a': 1, 'b': 2, 'c': 3}))
    assert is_iterable(u'abc')
    assert is_iterable(b'abc')

    assert not is_iterable('abc')
    assert not is_iterable(1)
    assert not is_iterable(None)


# Generated at 2022-06-12 22:58:22.520755
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
  assert ImmutableDict() == ImmutableDict()
  assert ImmutableDict(one=1) == ImmutableDict(one=1)
  assert ImmutableDict(one=1) == ImmutableDict(one=1, two=2)
  assert ImmutableDict(one=1) == ImmutableDict(two=2, one=1)


# Generated at 2022-06-12 22:58:28.842215
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable(range(0)) is True
    assert is_iterable(set()) is True
    assert is_iterable(tuple()) is True
    assert is_iterable(dict()) is True
    assert is_iterable('') is False
    assert is_iterable(1) is False
    assert is_iterable(object()) is False
    assert is_iterable(TestIsIterable()) is False


# Generated at 2022-06-12 22:58:34.975314
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Unit test for method __eq__ of class ImmutableDict
    """
    # test valid equality
    newdict = ImmutableDict({'a': 1, 'b': 2})
    olddict = ImmutableDict({'a': 1, 'b': 2})
    assert newdict == olddict

    # test valid inequality
    newdict = ImmutableDict({'a': 1, 'b': 2})
    olddict = ImmutableDict({'a': 1, 'b': 3})
    assert newdict != olddict

    # test equal to string
    newdict = ImmutableDict({'a': 1, 'b': 2})
    olddict = 'a'
    assert newdict != olddict


# Generated at 2022-06-12 22:58:45.715316
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert not ImmutableDict({'a': 1}) == ImmutableDict({'a': 2})
    assert ImmutableDict({'a': 1}) != ImmutableDict({'a': 2})
    assert not ImmutableDict({'a': 1}) != ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1}) == {'a': 1}
    assert not ImmutableDict({'a': 1}) == {'a': 2}
    assert ImmutableDict({'a': 1}) != {'a': 2}
    assert not ImmutableDict({'a': 1}) != {'a': 1}

# Generated at 2022-06-12 22:58:50.431383
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({"a": 1, "b": 2})
    b = ImmutableDict({"a": 1, "b": 2, "c": 3})
    assert (a != b)
    b = ImmutableDict({"a": 1, "b": 2})
    assert (a == b)


# Generated at 2022-06-12 22:59:11.754726
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import pytest
    d1 = ImmutableDict({'a': 1})
    d2 = ImmutableDict({'a': 1})
    d3 = ImmutableDict({'b': 1})
    d4 = {'a': 1}
    d5 = ImmutableDict({'a': 2})

    assert d1 == d1  # self equality
    assert d1 == d2  # two equal ImmutableDicts
    assert not d1 == d3  # different ImmutableDicts
    assert not d1 == d4  # ImmutableDict to dict
    assert not d1 == d4  # ImmutableDict to dict
    assert not d1 == d5  # same keys, different values

    with pytest.raises(TypeError):
        d1 == 1

# Generated at 2022-06-12 22:59:17.699008
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    data1 = ImmutableDict(kind='cat', name='Garfield')
    data2 = ImmutableDict(kind='cat', name='Garfield')
    data3 = ImmutableDict(kind='cat', name='Garfield', toys=['yarn', 'mice'])
    data4 = ImmutableDict(kind='dog', name='Odie')
    data5 = dict(kind='cat', name='Garfield')

    assert data1 == data2
    assert data1 != data3
    assert data1 != data4
    assert data1 != data5
    assert data1 != 'string'  # invalid comparison

# Generated at 2022-06-12 22:59:24.868507
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    first = ImmutableDict({'a': 1, 'b': 2})
    second = ImmutableDict({'b': 2, 'a': 1})
    third = ImmutableDict({'a': 2, 'b': 2})
    forth = ImmutableDict({'a': 1, 'b': 2, 'c': 3})

    assert first == second
    assert not first == third
    assert not first == forth
    assert not first == {'a': 1, 'b': 2}

# Generated at 2022-06-12 22:59:32.626798
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(())

    assert is_iterable(set())
    assert is_iterable(frozenset())

    assert not is_iterable(1)
    assert not is_iterable(1.0)
    assert not is_iterable(None)
    assert not is_iterable('a')

    class MockIterable(object):
        def __iter__(self):
            return iter([])
    assert is_iterable(MockIterable())



# Generated at 2022-06-12 22:59:35.196996
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a=1, b=2)
    d2 = ImmutableDict(b=2, a=1)
    assert d1 == d2

# Generated at 2022-06-12 22:59:40.822357
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2])
    assert is_iterable(MutableMapping(dict(one=1, two=2)))
    assert is_iterable('test')
    assert not is_iterable(1)
    assert not is_iterable(Exception)
    assert not is_iterable(ImmutableDict({'one': 1, 'two': 2}))
    assert is_iterable(ImmutableDict({'one': 1, 'two': 2}), include_strings=True)



# Generated at 2022-06-12 22:59:43.523752
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict = {'ImmutableDict': 'dict'}
    first = ImmutableDict(test_dict)
    second = ImmutableDict(test_dict)
    assert first == second
    assert second == first



# Generated at 2022-06-12 22:59:52.252712
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    original_dict = ImmutableDict(a=1, b=2, c=3)
    # Test for having the same key-value pairs
    different_dict1 = dict(a=1, b=2, c=3)
    assert original_dict == different_dict1
    # Test for having the same key-value pairs, but different order
    different_dict2 = dict(c=3, b=2, a=1)
    assert original_dict == different_dict2
    # Test for having different key-value pairs
    different_dict3 = dict(a=1, b=2, c=3, d=4)
    assert original_dict != different_dict3
    # Test for having different keys
    different_dict4 = dict(a=1, d=2, c=3)
    assert original_dict != different_

# Generated at 2022-06-12 23:00:00.859747
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from unittest import TestCase

    class TestImmutableDictEQ(TestCase):
        def test_ImmutableDict__eq__(self):
            i_d_1 = ImmutableDict({'a': 'b', 'c': 'd'})
            i_d_2 = ImmutableDict({'e': 'f', 'g': 'h'})
            d_1 = {'a': 'b', 'c': 'd'}
            self.assertFalse(i_d_1 == i_d_2)
            self.assertFalse(i_d_1 == d_1)
            self.assertFalse(i_d_2 == d_1)

            i_d_1 = ImmutableDict({'a': 'b', 'c': 'd'})
            i_d_2 = ImmutableD

# Generated at 2022-06-12 23:00:08.958444
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) == True
    assert is_iterable({}) == True
    assert is_iterable(set()) == True
    assert is_iterable(xrange(0)) == True

    assert is_iterable(123) == False
    assert is_iterable(False) == False
    assert is_iterable(None) == False

    class Iterable:
        def __iter__(self):
            return iter([])
    assert is_iterable(Iterable()) == True

    class NonIterable:
        pass
    assert is_iterable(NonIterable()) == False


# Generated at 2022-06-12 23:00:38.887980
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    is equal must return true when compared to the same ImmutableDict
    is equal must return true when compared to an ImmutableDict with the same key value pairs
    is equal must return false when compared to a different ImmutableDict
    is equal must return false when compared to an ImmutableDict with different key value pairs
    """
    d = ImmutableDict({"a":1, "b":2});
    assert(d == d)
    assert(d == ImmutableDict({"a":1, "b":2}))
    assert(d != 3)
    assert(d != ImmutableDict({"a":1, "b":3333}))
    print("test_ImmutableDict___eq__ passed")


# Generated at 2022-06-12 23:00:42.034392
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(u'')
    assert is_iterable(b'')

    assert not is_iterable(None)
    assert not is_iterable(0)



# Generated at 2022-06-12 23:00:49.292601
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert not is_iterable('')
    assert not is_iterable(())
    assert not is_iterable(.666)
    assert not is_iterable(None)
    assert is_iterable('', include_strings=True)
    assert not is_iterable((), include_strings=True)
    assert is_iterable('{}', include_strings=True)


# Generated at 2022-06-12 23:00:52.954825
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(range(0))
    assert is_iterable((x for x in range(0)))
    assert is_iterable(None) is False



# Generated at 2022-06-12 23:01:03.704743
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    first = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    second = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    third = ImmutableDict({'a': 1, 'c': 3, 'b': 2})
    fourth = ImmutableDict({'a': 1, 'b': 2})
    # Equality comparison with the same object is True
    assert first == first

    # Equality comparison with an ImmutableDict constructed using different order of items
    assert first == third

    # Equality comparison with an ImmutableDict with the same items but different types
    assert first == {'a': 1, 'b': 2, 'c': 3}

    # Equality comparison with a set - should be False
    assert first != set((1, 2, 3))

    # Equality comparisons

# Generated at 2022-06-12 23:01:08.998602
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    dict3 = ImmutableDict({'b': 2, 'a': 1})
    dict4 = ImmutableDict({'c': 1, 'a': 2})
    assert dict1 == dict2
    assert dict1 == dict3
    assert not dict1 == dict4


# Generated at 2022-06-12 23:01:11.633749
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'name': 'test'})
    d2 = ImmutableDict({'name': 'test'})
    assert d1 == d2



# Generated at 2022-06-12 23:01:16.400695
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('test')
    assert is_iterable(['test', 'test'])
    assert is_iterable(('test', 'test'))
    assert is_iterable({'test': 'test'})
    assert not is_iterable(5)
    assert is_iterable(5, include_strings=True)



# Generated at 2022-06-12 23:01:25.263888
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a='b', c='d') == ImmutableDict(c='d', a='b')
    assert ImmutableDict(a='b', c='d') == ImmutableDict(c='d', a='b')
    assert ImmutableDict(a='b', c='d') != ImmutableDict(c='d', a='B')
    assert ImmutableDict(a='b', c='d') != ImmutableDict(c='D', a='b')
    assert ImmutableDict(a='b', c='d') != ImmutableDict(c='d', a='b', e='f')


# Generated at 2022-06-12 23:01:34.485271
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['a', 'b'])
    assert is_iterable([])
    assert is_iterable(['a', 'b'], include_strings=True)
    assert is_iterable([], include_strings=True)
    assert is_iterable('abc')
    assert is_iterable('')
    assert is_iterable(b'abc')
    assert is_iterable(b'')
    assert is_iterable(set(('a', 'b')))
    assert is_iterable(set(()))
    assert is_iterable(set([1, 2, 3, 1]))
    assert is_iterable(tuple(('a', 'b')))
    assert is_iterable(tuple(()))
    assert is_iterable(iter(('a', 'b')))


# Generated at 2022-06-12 23:02:24.519581
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 'A', 'b': 'B', 'c': 'C'})
    d1_copy = ImmutableDict({'a': 'A', 'b': 'B', 'c': 'C'})
    d1_diff = ImmutableDict({'a': 'A', 'b': 'B', 'c': 'D'})

    assert (d1 == d1_copy)
    assert (not (d1 == d1_diff))

    for _ in (False, None, 2, 'string'):
        assert not (d1 == _)

# Generated at 2022-06-12 23:02:28.533513
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immutable_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert immutable_dict == immutable_dict
    assert immutable_dict == {'a': 1, 'b': 2, 'c': 3}
    assert immutable_dict == ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert immutable_dict == ['a', 'b', 'c']
    assert immutable_dict == ('a', 'b', 'c')
    assert not immutable_dict == ['a', 'b', 'c', 'd']
    assert not immutable_dict == ('a', 'b', 'c', 'd')



# Generated at 2022-06-12 23:02:30.267151
# Unit test for function is_iterable
def test_is_iterable():
    if hasattr([], 'iter'):
        return True
    else:
        return False


# Generated at 2022-06-12 23:02:32.621003
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dictionary1 = ImmutableDict({'a': 1, 'b': 2})
    dictionary2 = ImmutableDict({'a': 1})
    assert not (dictionary1 == dictionary2)



# Generated at 2022-06-12 23:02:41.627710
# Unit test for function is_iterable
def test_is_iterable():
    assert (not is_iterable(None))
    assert (not is_iterable(42))
    assert (not is_iterable(True))
    assert (not is_iterable('string'))
    assert (not is_iterable([]))
    assert (is_iterable([], include_strings=True))
    assert (is_iterable(()))
    assert (is_iterable({}))
    assert (is_iterable(dict()))
    assert (not is_iterable(dict().__iter__()))
    assert (is_iterable(dict().iteritems()))
    assert (is_iterable(dict().values()))


# Test case for function is_sequence

# Generated at 2022-06-12 23:02:50.989599
# Unit test for function is_iterable
def test_is_iterable():
    # Test that empty string is not iterable
    assert is_iterable('') is False

    # Test that empty tuple is iterable
    assert is_iterable(()) is True

    # Test that empty list is iterable
    assert is_iterable([]) is True

    # Test that empty dict is iterable
    assert is_iterable({}) is True

    # Test that non-empty string is iterable
    assert is_iterable('ABC') is True

    # Test that non-empty tuple is iterable
    assert is_iterable((2, 3, 4)) is True

    # Test that non-empty list is iterable
    assert is_iterable([2, 3, 4]) is True

    # Test that non-empty dict is iterable

# Generated at 2022-06-12 23:02:56.785371
# Unit test for function is_iterable
def test_is_iterable():

    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(xrange(5))
    assert is_iterable(iter(xrange(5)))
    assert is_iterable(5) is False
    assert is_iterable(5.0) is False
    assert is_iterable(dict())
    assert is_iterable(dict().keys())
    assert is_iterable(dict().items())
    assert is_iterable(dict().values())
    assert is_iterable([x for x in range(5)])
    assert is_iterable((x for x in range(5)))
    assert is_iterable({x for x in range(5)})

# Generated at 2022-06-12 23:03:07.007343
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]), 'is_iterable({}) returned False'.format([1, 2, 3])
    assert is_iterable((1, 2, 3)), 'is_iterable({}) returned False'.format((1, 2, 3))
    assert is_iterable(iter([1, 2, 3])), 'is_iterable(iter({})) returned False'.format([1, 2, 3])

    assert not is_iterable(1), 'is_iterable(1) returned True'
    assert not is_iterable(set([1, 2, 3])), 'is_iterable({}) returned True'.format(set([1, 2, 3]))

# Generated at 2022-06-12 23:03:15.652035
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # __eq__ is using python's hash function so we will test
    # with different python versions
    import sys

    if sys.version_info < (3, 3):
        assert ImmutableDict({'a': 1, 'b': 2}, c=3) == ImmutableDict({'b': 2, 'a': 1}, c=3)
        assert ImmutableDict({'a': 1, 'b': 2}, c=3) != ImmutableDict({'b': 2, 'a': 2}, c=3)
        assert ImmutableDict({'a': 1, 'b': 2}, c=3) != ImmutableDict({'b': 2, 'a': 1}, c=3, d=4)
        assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1})

# Generated at 2022-06-12 23:03:19.267859
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict()
    b = ImmutableDict()
    assert a == b

    c = ImmutableDict(dict(a=1, b=2, c=3))
    d = ImmutableDict(dict(c=3, b=2, a=1))
    assert c == d

# Generated at 2022-06-12 23:04:52.814853
# Unit test for function is_iterable
def test_is_iterable():
    # Make sure strings are not iterable
    assert not is_iterable(None)
    assert not is_iterable('')
    assert not is_iterable('hi')
    assert not is_iterable(u'')
    assert not is_iterable(u'hi')
    assert not is_iterable(b'')
    assert not is_iterable(b'hi')

    # Make sure is_iterable returns False for non iterable objects
    assert not is_iterable(5)
    assert not is_iterable(dict(a='a'))
    assert not is_iterable(['a'])
    assert not is_iterable(ImmutableDict(a='a'))

    # Make sure is_iterable returns True for iterable objects
    assert is_iterable([])

# Generated at 2022-06-12 23:05:00.446898
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""
    immutable_a = ImmutableDict(a=1, b=2)
    immutable_b = ImmutableDict(a=1, b=2)
    immutable_c = ImmutableDict(c=1, d=2)

    assert immutable_a == immutable_b
    assert immutable_a != immutable_c
    assert immutable_a == {'a': 1, 'b': 2}
    assert immutable_a != {'c': 1, 'd': 2}

# Generated at 2022-06-12 23:05:10.457922
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(dict(a=1, b=2, c=3)) == ImmutableDict(dict(c=3, a=1, b=2))
    assert ImmutableDict(dict(a=1, b=[1, 2, 3], c=3)) != ImmutableDict(dict(a=1, b=[3, 2, 1], c=3))
    assert ImmutableDict(dict(a=1, b=[1, 2, 3], c=3)) == ImmutableDict(dict(c=3, a=1, b=[1, 2, 3]))
    assert ImmutableDict(dict(a=1, b=[1, 2, 3], c=3)) != ImmutableDict(dict(c=3, a=1))

# Generated at 2022-06-12 23:05:14.356212
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import itertools
    for d1, d2 in itertools.permutations([ImmutableDict({}), ImmutableDict({"a": "b"})], 2):
        assert d1 == d2 == ImmutableDict(d1) == ImmutableDict(d2)
        assert False if d1 is d2 else True
        if d1 == d2:
            assert ImmutableDict(d1) is not ImmutableDict(d2)



# Generated at 2022-06-12 23:05:23.535718
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict()
    d2 = ImmutableDict()
    d3 = ImmutableDict({1:'one', 2:'two'})
    d4 = ImmutableDict({1:'one', 2:'two'})
    d5 = ImmutableDict({1:'one', 2:'two', 3:'three'})
    d6 = ImmutableDict({1:'one', 2:'two', 3:'two'})
    d7 = ImmutableDict({3:'three', 2:'two', 1:'one'})
    d8 = ImmutableDict({'one':1, 'two':2})

    assert d1 == d2 == d1
    assert d3 == d4 == d3
    assert d3 != d5 != d3
    assert d3 != d6 != d3

# Generated at 2022-06-12 23:05:33.918632
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit tests for method __eq__ of class ImmutableDict."""
    # Case 1: two ImmutableDict are equal, should return true
    dict1 = ImmutableDict(one=1, two=2, three=3)
    dict2 = ImmutableDict(one=1, two=2, three=3)
    assert dict1 == dict2

    # Case 2: two ImmutableDict are not equal, should return false
    dict3 = ImmutableDict(one=1, two=2, three=4)
    assert dict1 != dict3

    # Case 3: one ImmutableDict and one dict are equal, should return false
    dict4 = dict(one=1, two=2, three=3)
    assert dict1 != dict4

    # Case 4: one ImmutableDict and one dict are not equal,

# Generated at 2022-06-12 23:05:38.720936
# Unit test for function is_iterable
def test_is_iterable():

    assert is_iterable([1, 2, 3]) == True
    assert is_iterable((1, 2, 3)) == True
    assert is_iterable({'key1': 1, 'key2': 2}) == True
    assert is_iterable('ansible') == True

    assert is_iterable(1) == False
    assert is_iterable(None) == False



# Generated at 2022-06-12 23:05:46.936964
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('some string') is False
    assert is_iterable(u'\u2713 unicode string') is False
    assert is_iterable(['a', 'list']) is True
    assert is_iterable([1, 2]) is True
    assert is_iterable(set()) is True
    assert is_iterable(set(['a', 'set'])) is True
    assert is_iterable({'a' : 'dict'}) is True
    assert is_iterable((1, 2)) is True
    assert is_iterable((x for x in [1, 2, 3])) is True
    assert is_iterable(True) is False
    assert is_iterable(None) is False



# Generated at 2022-06-12 23:05:51.774757
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({6: 6}) == ImmutableDict({6: 6})
    assert ImmutableDict({1: 8}) != ImmutableDict({2: 6})
    assert ImmutableDict({6: 6}) != set([6, 6])
    assert ImmutableDict({6: 6, 7: 7}) != ImmutableDict({7: 7, 6: 6})


# Generated at 2022-06-12 23:05:57.264252
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """ Unit tests for method __eq__ of class ImmutableDict """
    idict = ImmutableDict({'a': 1, 'b': 2})
    assert idict == {'a': 1, 'b': 2}
    assert not idict == {'a': 1, 'b': 3}
    assert idict == idict
    assert not idict == ImmutableDict({})
    assert not idict == {'c': 3, 'd': 4}
    assert not idict == None
