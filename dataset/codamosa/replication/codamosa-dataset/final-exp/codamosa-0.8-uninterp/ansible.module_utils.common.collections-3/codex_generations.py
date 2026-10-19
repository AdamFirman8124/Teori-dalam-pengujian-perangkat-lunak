

# Generated at 2022-06-12 22:56:08.681051
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    """This function tests the difference method of ImmutableDict class"""
    source_dict = {1: "one", 2: "two", 3: "three"}
    test_immutable_dict = ImmutableDict(source_dict)
    assert test_immutable_dict.difference([1, 3])._store == {2: 'two'}



# Generated at 2022-06-12 22:56:12.351276
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable({1, 2})
    assert is_iterable(set([1, 2]))
    assert is_iterable(list([1, 2]))
    assert is_iterable(tuple((1, 2)))
    assert is_iterable(dict())
    assert is_iterable(dict([(1, 2), (3, 4)]))
    assert is_iterable(1) is False
    assert is_iterable("test") is True
    assert is_iterable("test", include_strings=False) is False



# Generated at 2022-06-12 22:56:19.104531
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """ Unit test of ImmutableDict __eq__
    This method is not covered by default since the code requires a mockup class
    """
    # case 1: equality
    a = ImmutableDict(a=1, b=2)
    b = ImmutableDict(b=2, a=1)
    assert a == b
    # case 2: inequality
    a = ImmutableDict(a=1, b=2)
    b = ImmutableDict(b=2, a=2)
    assert not (a == b)


# Generated at 2022-06-12 22:56:24.358372
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict = {'test': 'dict'}
    immutable_test_dict = ImmutableDict(test_dict)
    assert immutable_test_dict == immutable_test_dict
    assert immutable_test_dict == test_dict
    assert immutable_test_dict != {'test': 'non-equal'}
    assert immutable_test_dict != 'test'


# Generated at 2022-06-12 22:56:29.952890
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({1: 1})
    assert is_iterable((1, 2))
    assert is_iterable(range(1, 5))
    assert is_iterable(u"abc")
    assert is_iterable(b"abc")

    assert not is_iterable(1)
    assert not is_iterable(1.1)



# Generated at 2022-06-12 22:56:38.194874
# Unit test for function is_iterable
def test_is_iterable():
    class NotIterable1(object):
        pass
    class NotIterable2(object):
        def __iter__(self):
            raise TypeError()
    class Iterable(object):
        def __iter__(self):
            return iter([])

    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(NotIterable1()) is False
    assert is_iterable(NotIterable2()) is False
    assert is_iterable(Iterable())
    assert is_iterable('abc')
    assert is_iterable(u'abc')
    assert is_iterable(b'abc')
    assert is_iterable(None) is False

# Unit tests for function is_sequence

# Generated at 2022-06-12 22:56:48.809787
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable((1, 2))
    assert is_iterable((1, 2,))
    assert is_iterable([1, 2])
    assert is_iterable([1, 2,])
    assert is_iterable({1: 2})
    assert is_iterable(set([1, 2]))
    assert is_iterable(x for x in [1, 2])
    assert is_iterable(u'unicode string')
    assert is_iterable(b'strings are iterable too')
    assert is_iterable(u'by \u2764')
    assert is_iterable(u'by \u2764'.encode('utf-8'))
    assert is_iterable('by \xe2\x9d\xa4'.decode('utf-8'))
    assert is_iterable

# Generated at 2022-06-12 22:56:59.113578
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'a': 1, 'b': 3, 'c': 3})
    c = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    d = ImmutableDict({'a': 1, 'b': 2, 'd': 3})

    assert(a == b) == False
    assert(b == c) == False
    assert(a == c) == True
    assert(c == a) == True
    assert(c == ImmutableDict({'a': 1, 'b': 2, 'c': 3})) == True
    assert(a == ImmutableDict({'a': 1, 'b': 2, 'c': 3})) == True


# Generated at 2022-06-12 22:57:01.227974
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict({"k1":"v1", "k2":"v2", "k3":"v3"})
    expected = ImmutableDict({"k1":"v1", "k3":"v3"})
    actual = original.difference({"k2"})
    assert(actual == expected)

# Generated at 2022-06-12 22:57:06.635138
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert not is_iterable(True)
    assert not is_iterable(False)
    assert not is_iterable(1)
    assert not is_iterable(1.1)

    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable({'key': 'value'})
    assert is_iterable(set())
    assert is_iterable('')
    assert is_iterable('ansible')

    class SomeClass(object):
        pass

    assert not is_iterable(SomeClass)
    assert not is_iterable(SomeClass())



# Generated at 2022-06-12 22:57:18.594372
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Different types are equal only if the hash is equal
    assert ImmutableDict({'a': 'b'}).__eq__('a string') is False
    assert ImmutableDict({'a': 'b'}).__eq__({'a': 'b'}) is False
    assert ImmutableDict({'a': 'b'}).__eq__((1, 2)) is False
    assert ImmutableDict({'a': 'b'}).__eq__([3, 4]) is False
    assert ImmutableDict({'a': 'b'}).__eq__(set([3, 4])) is False

    # Different values are not equal
    assert ImmutableDict({'a': 'b'}).__eq__(ImmutableDict({'a': 'c'})) is False

# Generated at 2022-06-12 22:57:28.692776
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Two ImmutableDicts with the same elements
    d1 = ImmutableDict(
        {'a': 1, 'b': 2, 'c': 3},
        foo=42,
        answer=47,
        bar=True,
    )
    d2 = ImmutableDict(
        {'c': 3, 'b': 2, 'a': 1},
        answer=47,
        bar=True,
        foo=42,
    )

    assert d1 == d2, 'Expected two ImmutableDicts with the same elements that have the same hash'
    assert not (d1 == ImmutableDict()), 'Expected two ImmutableDicts with different elements that have different hash'
    assert not (d1 == dict()), 'Expected two ImmutableDict and dict with different elements that have different hash'

# Generated at 2022-06-12 22:57:32.234250
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable((1,2,3)) == True
    assert is_iterable([1,2,3]) == True
    assert is_iterable({1:"a", 2:"b"}) == True
    assert is_iterable(1) == False

# Generated at 2022-06-12 22:57:41.634562
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import copy
    import random
    original = {}
    for i in range(0, 10):
        number = random.randint(0, 100)
        original[i] = number
    original = ImmutableDict(original)
    a = copy.deepcopy(original)
    b = ImmutableDict(a)
    c = ImmutableDict(a)
    if hash(b) != hash(c):
        raise Exception('Hashcode for different instances of {0} is not equal'.format(
            ImmutableDict.__name__
        ))
    if a != b or a != c or b != c:
        raise Exception('Different instances of {0} are not equal'.format(
            ImmutableDict.__name__
        ))
    del a[0]

# Generated at 2022-06-12 22:57:46.028196
# Unit test for function is_iterable
def test_is_iterable():
    class notAnIterable(object):
        pass

    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({'a': 'b'})
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable('abc')
    assert not is_iterable(notAnIterable())


# Generated at 2022-06-12 22:57:48.585777
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict_a = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    dict_b = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

    assert dict_a == dict_b



# Generated at 2022-06-12 22:57:58.620267
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id1 = ImmutableDict({'a': 1, 'b': {1,2}, 'c': (1,2)})
    id2 = ImmutableDict({'a': 1, 'b': {1,2}, 'c': (1,2)})
    id3 = ImmutableDict({'a': 1, 'b': {1,2}})
    id4 = ImmutableDict({'a': 1, 'b': {1,2}, 'c': {1,2}})
    id5 = ImmutableDict({'a': 1, 'b': {1,2}, 'c': {1,2}})

    assert id1 == id2
    assert id1 != id3
    assert id1 != id4
    assert id4 == id5
    assert id1 != 'hello'
    # We are using python

# Generated at 2022-06-12 22:58:06.730221
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immutable1 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    immutable2 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    immutable3 = ImmutableDict({'key1': 'value1'})
    immutable4 = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    immutable5 = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key2': 'value2'})
    immutable6 = ImmutableDict()
    immutable7 = None

    assert immutable1 == immutable2
    assert immutable1 != immutable3
    assert immutable1 != immutable4
    assert immutable1 != immutable5
    assert immutable1 != immutable7


# Generated at 2022-06-12 22:58:15.352587
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for the __eq__ function of ImmutableDict."""
    original_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert original_dict == ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert original_dict == {'a': 1, 'b': 2, 'c': 3}
    assert not original_dict == {'a': 1, 'b': 2}
    assert not original_dict == {'a': 1, 'b': 2, 'c': 4}
    assert not original_dict == 1


# Generated at 2022-06-12 22:58:26.452564
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import MutableMapping
    basic.fail_json = lambda msg: msg
    # Test valid inputs
    # Test when equal
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict(a)
    assert a == b
    b.update({'b': 2, 'c': 4})
    assert a != b
    # Test when different and not hashable
    b = ['a', 'b', 'c']
    try:
        a == b
    except TypeError:
        pass
    else:
        raise Exception('ImmutableDict failed to raise TypeError when comparing to unhashable object')
    # Test when different and hashable

# Generated at 2022-06-12 22:58:39.139963
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    oid = ImmutableDict(a=1, b=2)
    assert oid == ImmutableDict(a=1, b=2)
    assert oid != ImmutableDict(a=1, b=3)
    assert oid != ImmutableDict(a=1, b=2, c=3)
    assert oid != dict(a=1, b=2)
    assert oid != list((1, 2))
    assert oid != (1, 2)

# Generated at 2022-06-12 22:58:45.142225
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a=1, b=2)
    d2 = ImmutableDict(a=1, b=2)
    d3 = ImmutableDict(a=2, b=2)
    assert d1 == d2
    assert not d1 == d3
    assert not d1 == dict(a=1, b=2)
    assert not d1 == 42


# Generated at 2022-06-12 22:58:54.740114
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict()
    b = ImmutableDict()
    assert a == b
    assert a == {}
    assert {} == a

    a = ImmutableDict(immutabledict__test_key='immutabledict__test_value')
    b = ImmutableDict(immutabledict__test_key='immutabledict__test_value')
    assert a == b

    a = ImmutableDict(immutabledict__test_key='immutabledict__test_value')
    assert a != {}

    a = ImmutableDict(immutabledict__test_key='immutabledict__test_value')
    b = ImmutableDict(immutabledict__test_key='immutabledict__other_value')
    assert a != b



# Generated at 2022-06-12 22:59:00.919061
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Tests for equality in ImmutableDict class."""
    import collections
    d1 = ImmutableDict({1: 2, 3: 4})
    d2 = ImmutableDict({3: 4, 1: 2})
    d3 = {1: 2, 3: 4}
    d4 = collections.OrderedDict({1: 2, 3: 4})

    assert d1 == d2
    assert not d1 == d3
    assert not d1 == d4



# Generated at 2022-06-12 22:59:12.380545
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict(a=1, b=ImmutableDict(d=4, e=5)) == ImmutableDict(b=ImmutableDict(d=4, e=5), a=1)
    assert ImmutableDict(a=1, b=ImmutableDict(d=4, e=5)) == ImmutableDict(b=ImmutableDict(e=5, d=4), a=1)
    assert ImmutableDict(a=1, b=ImmutableDict(d=4, e=5)) == ImmutableDict(b=MutableMapping(d=4, e=5), a=1)

# Generated at 2022-06-12 22:59:20.478658
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    c = ImmutableDict({'c': 3, 'b': 2, 'a': 1})
    d = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    e = ImmutableDict({'a': 1, 'b': 2, 'c': 4})
    f = {'a': 1, 'b': 2, 'c': 3}
    g = [1, 2, 3, 4]

    assert a == b
    assert a == c
    assert a != d
    assert a != e
    assert a != f
    assert a != g

# Generated at 2022-06-12 22:59:31.380843
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([], True) == True
    assert is_iterable((), True) == True
    assert is_iterable({}, True) == True
    assert is_iterable(set(), True) == True
    assert is_iterable(text_type(), True) == True
    assert is_iterable(binary_type(), True) == True

    assert is_iterable([]) == True
    assert is_iterable(()) == True
    assert is_iterable({}) == True
    assert is_iterable(set()) == True
    assert is_iterable(text_type()) == True
    assert is_iterable(binary_type()) == True

    assert is_iterable([], False) == True
    assert is_iterable((), False) == True
    assert is_iterable({}, False) == True

# Generated at 2022-06-12 22:59:34.930784
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """It should validate equal dictionaries."""
    expected = ImmutableDict({'a': 1, 'b': 2})
    actual = ImmutableDict({'a': 1, 'b': 2})
    assert expected == actual



# Generated at 2022-06-12 22:59:41.179863
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(1) is False
    assert is_iterable(object()) is False
    assert is_iterable(1.1) is False
    assert is_iterable(u'XXXX') is True
    assert is_iterable('XXXX') is True
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable({1: 'a', 2: 'b', 3: 'c'}) is True
    assert is_iterable({1, 2, 3}) is True


# Generated at 2022-06-12 22:59:45.809452
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable((i for i in range(10)))
    assert is_iterable(ImmutableDict(a='a', b='b', c='c'))
    assert is_iterable(u'abc')
    assert not is_iterable('abc')
    assert not is_iterable(object())



# Generated at 2022-06-12 23:00:09.209755
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    '''Test method __eq__'''
    # Test case when both ImmutableDict are identical (same order of items)
    d1 = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    d2 = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    assert d1 == d2

    # Test case when both ImmutableDict are identical (different order of items)
    d1 = ImmutableDict({'key1': 'value1', 'key2': 'value2', 'key3': 'value3'})
    d2 = ImmutableDict({'key3': 'value3', 'key1': 'value1', 'key2': 'value2'})

# Generated at 2022-06-12 23:00:14.015626
# Unit test for function is_iterable
def test_is_iterable():
    """Test for function is_iterable."""
    assert is_iterable([])
    assert is_iterable((i for i in range(5)))
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable('string')
    assert not is_iterable(1)



# Generated at 2022-06-12 23:00:23.403907
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict()
    d2 = ImmutableDict()
    assert d1 == d2

    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    assert d1 == d2

    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert not d1 == d2

    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    d2.update({'c': 3})
    assert not d1 == d2


# Generated at 2022-06-12 23:00:28.834243
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1}) == {'a': 1}
    assert not ImmutableDict({'a': 1}) == ImmutableDict({'b': 1})
    assert not ImmutableDict({'a': 1}) == MutableMapping
    assert not ImmutableDict({'a': 1}) == 'abc'



# Generated at 2022-06-12 23:00:36.129294
# Unit test for function is_iterable
def test_is_iterable():
    test_cases = [
        ([], True),
        (['a'], True),
        (['a', 'b'], True),
        ({}, True),
        ({'a': 1}, True),
        (set(), True),
        ({'a', 'b'}, True),
        (None, False),
        ('a', False),
        ('abc', False),
    ]
    for (seq, value) in test_cases:
        assert is_iterable(seq) == value


# Generated at 2022-06-12 23:00:37.268029
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2, c=3) == ImmutableDict(a=1, b=2, c=3)

# Generated at 2022-06-12 23:00:45.790379
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'b': 2, 'a': 1})
    assert ImmutableDict({'a': 1, 'b': 2}) == {'b': 2, 'a': 1}
    assert {'b': 2, 'a': 1} == ImmutableDict({'a': 1, 'b': 2})

    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) == ImmutableDict({'b': 2, 'a': 1, 'd': 3, 'c': 3})
    assert ImmutableDict({'b': 2, 'a': 1, 'd': 3, 'c': 3}) == ImmutableDict({'a': 1, 'b': 2, 'c': 3})


# Generated at 2022-06-12 23:00:53.896715
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable((1, 2)) is True
    assert is_iterable([1, 2]) is True
    assert is_iterable(set([1, 2])) is True
    assert is_iterable(dict(a=1, b=2)) is True
    assert is_iterable(1) is False
    assert is_iterable('hello') is False
    assert is_iterable('hello', include_strings=True) is True
    assert is_iterable(ImmutableDict(a=1, b=2)) is True


# Generated at 2022-06-12 23:01:04.463968
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test equality when both are ImmutableDict and contents are same
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert a == b
    assert b == a

    # Test equality when both are ImmutableDict and contents are different
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'d': 3, 'e': 2, 'f': 1})
    assert not a == b
    assert not b == a

    # Test equality when one of them is ImmutableDict and other is a dictionary
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b

# Generated at 2022-06-12 23:01:12.265150
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test equal instances
    a = ImmutableDict({'a': 1})
    b = ImmutableDict({'a': 1})
    assert a == b
    # Test non equal instances
    b['b'] = 2
    assert a != b
    # Test equal instances with different orders
    a = ImmutableDict({'a': 1, 'b': 2})
    b = ImmutableDict({'b': 2, 'a': 1})
    assert a == b
    # Test None value
    assert a != None
    # Test None value
    assert a != {'a':1}



# Generated at 2022-06-12 23:01:43.760936
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(dict(a=1, b=2))
    assert a == ImmutableDict(dict(a=1, b=2))
    assert a != ImmutableDict(dict(b=2, a=1))
    assert a != ImmutableDict(dict(a=1, b=2, c=3))

# Generated at 2022-06-12 23:01:50.540543
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from collections import OrderedDict

    idict1 = ImmutableDict()
    assert idict1.__eq__(idict1) == True
    assert idict1.__eq__(OrderedDict()) == True
    assert idict1.__eq__(ImmutableDict()) == True
    assert idict1.__eq__(dict()) == True
    assert idict1.__eq__(ImmutableDict({'a':1, 'b':2})) == False

    idict2 = ImmutableDict({'a':1, 'b':2, 'c':3})
    assert idict2.__eq__(idict2) == True
    assert idict2.__eq__(OrderedDict({'a':1, 'b':2, 'c':3})) == True
    assert idict2

# Generated at 2022-06-12 23:01:53.686235
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(42) is False
    assert is_iterable(is_iterable) is False
    assert is_iterable(dict()) is True
    assert is_iterable(set()) is True



# Generated at 2022-06-12 23:02:02.198908
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Task: Create two ImmutableDict objects, one from a list of tuples and one by providing kwargs
    # Result: The result of __eq__ should be False
    first_immutable_dict = ImmutableDict([("a", 1), ("b", 2), ("c", 3)])
    second_immutable_dict = ImmutableDict(a=1, b=2, c=3)
    assert first_immutable_dict.__eq__(second_immutable_dict) is False
    # Task: Create two ImmutableDict objects from list of tuples, a list of lists and a dictionary
    # Result: The result of __eq__ should be False
    # Note: The result should be False because the objects are of different types

# Generated at 2022-06-12 23:02:07.769425
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    testCase1 = ImmutableDict(a=1, b=2)
    testCase2 = ImmutableDict(b=2, a=1)
    testCase3 = {"a": 1, "b": 2}
    for testCase in testCase1, testCase2, testCase3:
        assert testCase1 == testCase
    assert testCase1 != testCase3
    assert testCase1 != {"a": 1, "b": 2}

# Generated at 2022-06-12 23:02:19.088823
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test for comparison of dictionary to dictionary
    dict1 = ImmutableDict(x=1, y=2)
    dict2 = ImmutableDict(x=1, y=2)
    dict3 = ImmutableDict(x=1, z=2)
    dict4 = dict(z=1, y=2)

    assert dict1 == dict1
    assert dict1 == dict2
    assert dict2 == dict2
    assert dict1 != dict3
    assert dict3 != dict3
    assert dict3 != dict4
    assert dict4 != dict4

    dict1 = ImmutableDict(dict1_x=1, dict1_y=2, dict1_z=3)
    dict2 = ImmutableDict(dict1_x=1, dict1_y=2, dict1_z=3)
    dict

# Generated at 2022-06-12 23:02:29.948389
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(None) is False
    assert is_iterable([]) is True
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable({}) is True
    assert is_iterable({'a': 1}) is True
    assert is_iterable(set()) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable(1) is False
    assert is_iterable(1.0) is False
    assert is_iterable('a') is False
    assert is_iterable(u'b') is False
    assert is_iterable(ImmutableDict(a=1)) is True

    assert is_iterable(None, True) is False

# Generated at 2022-06-12 23:02:35.808762
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict = ImmutableDict({'test': 'value'})
    assert test_dict == {'test': 'value'}
    assert test_dict == ImmutableDict({'test': 'value'})
    assert test_dict != 'test'
    assert test_dict != {}
    assert test_dict != {'other': 'value'}
    assert test_dict != ImmutableDict({'other': 'value'})
    assert test_dict != {'test': 'other'}
    assert test_dict != ImmutableDict({'test': 'other'})


# Generated at 2022-06-12 23:02:46.464228
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    d3 = dict({'a': 1, 'b': 2})
    d4 = {'a': 1, 'b': 2}
    d5 = ImmutableDict({'a': 2, 'b': 2})
    print ('test_ImmutableDict___eq__')
    assert d1 == d1
    assert d1 != d3
    assert d1 != d4
    assert d1 != d5
    assert d1 != (1, 2, 3)
    assert d1 == d2
    assert d1.__eq__(d3) == False
    assert d1.__eq__(d4) == False

# Generated at 2022-06-12 23:02:50.707296
# Unit test for function is_iterable
def test_is_iterable():
    # Basic types, not iterable
    assert not is_iterable(1)
    assert not is_iterable('a')
    assert not is_iterable(True)
    assert not is_iterable(None)
    assert not is_iterable(Exception('an exception'))
    # Containers
    assert is_iterable([])
    assert is_iterable({})
    # Include strings as iterables
    assert is_iterable('a', include_strings=True)
    assert is_iterable(b'a', include_strings=True)



# Generated at 2022-06-12 23:03:50.899055
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['1', '2'])
    assert is_iterable([1, 2, 3])
    assert is_iterable({1: 2, 3: 4})
    assert is_iterable((1, 2, 3))
    assert is_iterable(set([1, 2]))
    assert is_iterable('abc') is False
    assert is_iterable(1) is False



# Generated at 2022-06-12 23:03:53.329021
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(one='a', two='b')
    b = ImmutableDict(one='a', two='b')
    assert a == b


# Generated at 2022-06-12 23:03:59.520916
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) == ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) != {'a': 1, 'b': 2, 'c': 3}
    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) != ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})



# Generated at 2022-06-12 23:04:11.235026
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test the __eq__ method of class ImmutableDict."""
    # Case 1: Equality between two immutable dicts.
    immutable_dict_1 = ImmutableDict({'key_1': 'value_1', 'key_2': 'value_2'})
    immutable_dict_2 = ImmutableDict({'key_1': 'value_1', 'key_2': 'value_2'})
    assert immutable_dict_1 == immutable_dict_2

    # Case 2: Equality between two mutable dicts.
    mutable_dict_1 = {'key_1': 'value_1', 'key_2': 'value_2'}
    mutable_dict_2 = {'key_1': 'value_1', 'key_2': 'value_2'}
    assert immutable_dict_1 == mutable_

# Generated at 2022-06-12 23:04:18.393608
# Unit test for function is_iterable
def test_is_iterable():
    test_string = 'test_string'
    test_unicode = u'test_unicode'
    test_binary = b'test_binary'
    test_list = [1, 2, 3, 4]
    test_tuple = (1, 2, 3, 4)
    test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    test_set = set((1, 2, 3, 4))

    assert is_iterable(test_string) is True
    assert is_iterable(test_unicode) is True
    assert is_iterable(test_binary) is True
    assert is_iterable(test_list) is True
    assert is_iterable(test_tuple) is True
    assert is_iterable(test_dict) is True

# Generated at 2022-06-12 23:04:27.804633
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test equality of ImmutableDict objects."""
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict({}) == ImmutableDict()
    assert ImmutableDict({}) == {}
    assert ImmutableDict() == {}
    assert ImmutableDict({'a': 1}) == {'a': 1}
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})

# Generated at 2022-06-12 23:04:32.494413
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 'a'}) == ImmutableDict({'a': 'a'})
    assert ImmutableDict({'a': 'a'}) != ImmutableDict({'a': 'b'})
    assert ImmutableDict({'a': 'a'}) != ImmutableDict({'b': 'a'})



# Generated at 2022-06-12 23:04:40.459124
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable([1]) is True
    assert is_iterable(set()) is True
    assert is_iterable(set([1])) is True
    assert is_iterable("") is True
    assert is_iterable("1") is True
    assert is_iterable(u"") is True
    # For b_string and bu_string is_iterable() returns the same result:
    assert is_iterable(b"") == is_iterable(u"")
    assert is_iterable(1) is False
    assert is_iterable(3.14) is False
    assert is_iterable(True) is False


# Generated at 2022-06-12 23:04:44.945266
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable({})
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(())
    assert not is_iterable(1)
    assert not is_iterable(True)
    assert not is_iterable(None)
    assert not is_iterable('foo')
    assert not is_iterable(b'foo')



# Generated at 2022-06-12 23:04:49.909284
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['foo', 'bar'])
    assert is_iterable(('foo', 'bar'))
    assert is_iterable(set(['foo', 'bar']))
    assert is_iterable({'foo': 'bar'})
    assert is_iterable(ImmutableDict())

    assert not is_iterable('foobar')
    assert not is_iterable(6)
    assert not is_iterable(None)

