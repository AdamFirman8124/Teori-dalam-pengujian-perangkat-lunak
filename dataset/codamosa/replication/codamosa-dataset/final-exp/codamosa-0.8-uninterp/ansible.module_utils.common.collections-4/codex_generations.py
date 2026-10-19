

# Generated at 2022-06-12 22:56:10.420268
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test method __eq__ of class ImmutableDict"""
    a = ImmutableDict({1: 2})
    b = ImmutableDict({1: 2, 3: 4})
    c = ImmutableDict({3: 4, 1: 2})

    if not (a.__hash__() == b.__hash__() == c.__hash__() == hash(((1, 2),))):
        raise Exception('Failure in __eq__ of ImmutableDict')
    if not (a == b == c):
        raise Exception('Failure in __eq__ of ImmutableDict')



# Generated at 2022-06-12 22:56:20.132064
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable."""
    assert is_iterable(None) is False
    assert is_iterable(3) is False
    assert is_iterable('foo') is False
    assert is_iterable(u'foo') is False
    assert is_iterable(b'foo') is False
    assert is_iterable(set()) is True
    assert is_iterable(tuple()) is True
    assert is_iterable(list()) is True
    assert is_iterable({'a': 'a'}) is True

    assert is_iterable(None, include_strings=True) is False
    assert is_iterable(3, include_strings=True) is False
    assert is_iterable('foo', include_strings=True) is True

# Generated at 2022-06-12 22:56:25.067119
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    imd1 = ImmutableDict(a=1, b=2)
    imd2 = ImmutableDict(c=1, d=2)
    imd3 = ImmutableDict(a=1, b=2)
    assert(imd1 == imd3)
    assert(not imd1 == imd2)


# Generated at 2022-06-12 22:56:34.960543
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for __eq__ method of ImmutableDict class"""
    # Define one immutable dictionary
    immutable_dict_1={'a':1, 'b':2, 'c':3}
    # Define another immutable dictionary
    immutable_dict_2={'a':1, 'b':2, 'c':3}
    # Create the immutable dictionary with the first dictionary
    immutable_dict_3=ImmutableDict(immutable_dict_1)
    # Create the immutable dictionary with the second dictionary
    immutable_dict_4=ImmutableDict(immutable_dict_2)

    #Test the __eq__ method
    #Compare the two immutable dictionaries created from dictionaries as inputs
    assert (immutable_dict_3 == immutable_dict_4) is True
    #Compare the two immutable dictionaries created from dictionaries as inputs


# Generated at 2022-06-12 22:56:40.806777
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Two ImmutableDict objects with the same content must be equal
    iDict1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    iDict2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert iDict1 == iDict2

    # ImmutableDict objects whose content differ must not be equal
    # (even if the content are equal as in case of MutableMapping)
    iDict1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    boo = {'a': 1, 'b': 2, 'c': 3}
    iDict2 = ImmutableDict(boo)
    assert iDict1 != iDict2

# Generated at 2022-06-12 22:56:52.188781
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1})
    b = ImmutableDict({'a': 1})
    c = ImmutableDict({'a': 1, 'b': 2})
    d = ImmutableDict({'b': 2, 'a': 1})
    e = ImmutableDict({'a': 2})
    f = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    g = ImmutableDict({'a': 1, 'b': 2, 'd': 3})
    h = {'a': 1}
    i = {'a': 1, 'b': 2}
    j = 42
    assert a != b
    assert a == c
    assert a != d
    assert a != e
    assert c != f
    assert c != g
    assert c != h

# Generated at 2022-06-12 22:57:01.385994
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 'b', 'c': 'd'}) == {'a': 'b', 'c': 'd'}
    assert ImmutableDict({'a': 'b', 'c': 'd'}) == ImmutableDict({'a': 'b', 'c': 'd'})
    assert not (ImmutableDict({'a': 'b', 'c': 'd'}) == ['a', 'b', 'c'])
    assert not (ImmutableDict({'a': 'b', 'c': 'd'}) == ('a', 'b', 'c'))
    assert not (ImmutableDict({'a': 'b', 'c': 'd'}) == 'abc')
    assert not (ImmutableDict({'a': 'b', 'c': 'd'}) == 1)

# Generated at 2022-06-12 22:57:06.758400
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(key1="val1", key2="val2")
    b = ImmutableDict(key1="val1", key2="val2")
    c = ImmutableDict(key2="val2", key1="val1")
    d = ImmutableDict(key1="val1", key2="val2", key3="val3")
    e = ImmutableDict(key1="val1", key2="val2", key3="val3", key4="val4")
    f = dict(key1="val1", key2="val2")

    assert a == b
    assert a == c
    assert a != d
    assert d != e
    assert a != f

# Generated at 2022-06-12 22:57:14.503906
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable("")
    assert is_iterable("") == is_iterable(u"")
    assert is_iterable("") != is_iterable(b"")
    assert is_iterable("") != is_iterable(u"")
    assert is_iterable("") != is_iterable(b"", include_strings=True)

    assert is_iterable(())
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable(range(0))
    assert is_iterable([])



# Generated at 2022-06-12 22:57:18.121640
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict1 = ImmutableDict({'one': 1})
    test_dict2 = ImmutableDict({'one': 1})
    test_dict3 = ImmutableDict({'two': 2})
    assert test_dict1 == test_dict2
    assert test_dict1 != test_dict3


# Generated at 2022-06-12 22:57:25.420160
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    data = dict(a=1, b=2, c=3)
    dut = ImmutableDict(data)

    assert dut.__eq__(data)
    assert dut.__eq__(dut)
    assert dut.__eq__(ImmutableDict(data))


# Generated at 2022-06-12 22:57:32.624139
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Equal objects
    a = ImmutableDict(key1=1, key2=2, key3=3)
    b = ImmutableDict(key2=2, key3=3, key1=1)
    assert (a == b)

    # Non-equal objects
    c = ImmutableDict(key1=1, key2=2, key3=3)
    d = ImmutableDict(key3=3, key1=1, key2=42)
    assert (c != d)


# Generated at 2022-06-12 22:57:34.627783
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({1: 2, 3: 4}) == ImmutableDict({3: 4, 1: 2})



# Generated at 2022-06-12 22:57:43.642414
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1) == ImmutableDict(a=1)
    assert ImmutableDict(a=1, c=2) == ImmutableDict(a=1, c=2)
    assert not ImmutableDict(a=1) == ImmutableDict(a=1, c=2)
    assert not ImmutableDict(a=1) == ImmutableDict(a=2)
    assert not ImmutableDict(a=1) == ImmutableDict(b=1)
    assert not ImmutableDict(a=1) == ImmutableDict(a=1, b=2)
    assert not ImmutableDict(a=1) == ImmutableDict(b=1, c=2)

# Generated at 2022-06-12 22:57:51.782143
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    test method __eq__ of class ImmutableDict
    """

    # test case 1:
    # Different items, same order
    immutable_dict_1 = ImmutableDict({'item1': 1, 'item2': 2, 'item3': 3})
    immutable_dict_2 = ImmutableDict({'item1': 1, 'item2': 2, 'item3': 3})
    assert immutable_dict_1 == immutable_dict_2

    # test case 2:
    # Same items, different order
    immutable_dict_1 = ImmutableDict({'item1': 1, 'item2': 2, 'item3': 3})
    immutable_dict_2 = ImmutableDict({'item1': 1, 'item3': 3, 'item2': 2})
    assert immutable_dict_1 == immutable_dict_

# Generated at 2022-06-12 22:58:01.709049
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict({'x': 0}) == ImmutableDict({'x': 0})
    assert ImmutableDict() != ImmutableDict({'x': 0})
    assert ImmutableDict({'x': 0}) != ImmutableDict({'x': 1})
    assert ImmutableDict({'x': 0}) != ImmutableDict({'y': 0})
    assert ImmutableDict({'x': 0}) != ImmutableDict({'x': 0, 'y': 1})
    assert ImmutableDict({'x': 0}) != ImmutableDict({'y': 0, 'x': 1})
    assert ImmutableDict({'x': 0}) != ImmutableDict({'x': 1, 'y': 0})

# Generated at 2022-06-12 22:58:11.481355
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert is_iterable(iter([]))
    assert is_iterable(iter([1, 2, 3]))
    assert is_iterable(set())
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable(frozenset())
    assert is_iterable(frozenset([1, 2, 3]))
    assert is_iterable('abc')
    assert is_iterable(b'abc')
    assert not is_iterable(1)
    # Assert that we can not iterate over an Iterable template class
    assert is_iterable(Mapping)
    assert is_iterable(MutableMapping)
    assert is_iterable(Hashable)

# Generated at 2022-06-12 22:58:22.650242
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Two ImmutableDict objects are equal
    assert ImmutableDict({"a": 1}) == ImmutableDict({"a": 1})

    # Two ImmutableDict objects are not equal
    assert ImmutableDict({"a": 1}) != ImmutableDict({"a": 2})

    # An ImmutableDict object is not equal to a Mapping objects with equal key-values
    assert ImmutableDict({"a": 1}) != {"a": 1}

    # An ImmutableDict object is equal to a Hashable object with equal key-values
    class DummyHashable(Hashable):
        def __init__(self, my_dict):
            self.my_dict = my_dict

        def __eq__(self, other):
            return self.my_dict == other.my_dict


# Generated at 2022-06-12 22:58:30.389332
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(a="a", b="b")
    b = ImmutableDict(a="a", b="b")
    c = ImmutableDict(c="c", b="b")
    d = ImmutableDict()
    e = ImmutableDict(body="", status=0)
    f = ImmutableDict(status=0, body="")
    g = ImmutableDict(a="a", b="b", c="c")

    assert a == b
    assert not a == c
    assert not a == d
    assert not a == e
    assert e == f
    assert not a == g



# Generated at 2022-06-12 22:58:34.606452
# Unit test for function is_iterable
def test_is_iterable():
    class IterClass(object):
        def __iter__(self):
            pass

    class NonIterClass(object):
        pass

    class NonIterSeq(Sequence):
        pass

    assert is_iterable('test')
    assert is_iterable(['test'])
    assert is_iterable(IterClass())
    assert is_iterable(NonIterClass())
    assert not is_iterable(NonIterSeq())



# Generated at 2022-06-12 22:58:51.201329
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import collections
    import random

    def test_randomly(d1, d2):
        assert bool(d1 == d2) == bool(d1._store == d2._store)

    def test_scalar():
        d1 = ImmutableDict(a=random.randint(0, 10), b=random.randint(0, 10))
        d2 = ImmutableDict(d1)
        assert d1 == d2
        assert d1 != d2._store

    def test_dict_order():
        d1 = ImmutableDict(a=random.randint(0, 10), b=random.randint(0, 10))
        d2 = ImmutableDict(b=d1['b'], a=d1['a'])
        assert d1 == d2


# Generated at 2022-06-12 22:58:54.062498
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable('string')
    assert is_iterable(b'bytes')
    assert is_iterable(frozenset(set()))
    assert not is_iterable('string', include_strings=False)
    assert not is_iterable(1)
    assert not is_iterable(True)



# Generated at 2022-06-12 22:59:05.202545
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict

    Purpose of this test is to cover the cases when the compared objects are different type
    of instances.

    In the first test case we try to compare the ImmutableDict with a MutableMapping class instance.
    The expected result is False and the test is passed if the __eq__ returns False.

    In the second test case we try to compare the ImmutableDict with an object which is not an
    instance of the Mapping class. The expected result is False and the test is passed if the
    __eq__ returns False.
    """
    # pylint: disable=undefined-variable,reimported,unused-variable
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.common.validation import check_

# Generated at 2022-06-12 22:59:14.983795
# Unit test for method __eq__ of class ImmutableDict

# Generated at 2022-06-12 22:59:25.227919
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    # Test that two ImmutableDicts with the same key-value pairs are equal
    d1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    d2 = ImmutableDict({'c': 3, 'b': 2, 'a': 1})
    assert d1 == d2

    # Test that two ImmutableDicts with different items are not equal
    d1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    d2 = ImmutableDict({'c': 3, 'b': 2, 'a': 3})
    assert not d1 == d2

    # Test that an ImmutableDict and a regular dict with the same items
    # are not equal

# Generated at 2022-06-12 22:59:35.732228
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(x=1) == ImmutableDict(x=1)
    assert ImmutableDict(x=1, y=2) == ImmutableDict(y=2, x=1)
    assert ImmutableDict(x=1, y=2) != ImmutableDict(y=2, x=2)
    assert ImmutableDict(x=1, y=2) != ImmutableDict(y=3, x=1)
    assert ImmutableDict(x=1, y=2) != ImmutableDict(x=1, y=3)
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict(x=1) != ImmutableDict(x=2)

# Generated at 2022-06-12 22:59:38.389230
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a='bcd')
    d2 = ImmutableDict(a='bcd')
    assert d1 == d2
    assert not d1 == 'a'



# Generated at 2022-06-12 22:59:45.265816
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    e1 = ImmutableDict({1: 1, 2: 2})
    e2 = ImmutableDict({1: 1, 2: 2})
    assert e1 == e2
    assert hash(e1) == hash(e2)

    e1 = ImmutableDict({1: 1, 2: 2})
    e2 = ImmutableDict({1: 1, 2: 2, 3: 3})
    assert e1 != e2
    assert hash(e1) != hash(e2)

    e1 = ImmutableDict({1: 1, 2: 2})
    e2 = ImmutableDict({1: 1, 2: 2, 3: 2})
    assert e1 != e2
    assert hash(e1) != hash(e2)

# Generated at 2022-06-12 22:59:54.436669
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test 1: Empty Dictionaries are equal
    d1 = ImmutableDict()
    d2 = ImmutableDict()
    assert d1 == d2

    # Test 2: Dictionaries are equal if their contents are equal and ignoring the order
    d1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    d2 = ImmutableDict({'c': 3, 'b': 2, 'a': 1})
    assert d1 == d2

    # Test 3: Dictionaries are not equal if their contents are different
    d1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    d2 = ImmutableDict({'c': 3, 'b': 2, 'a': 4})
    assert d1 != d2

    # Test 4: D

# Generated at 2022-06-12 23:00:02.267008
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    first = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    second = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert(first == second)

    third = ImmutableDict({'b': 2, 'c': 3, 'a': 1})
    assert(first == third)

    fourth = ImmutableDict({'a': 1, 'b': 2})
    assert(first != fourth)

    fifth = ImmutableDict({'a': 1})
    assert(first != fifth)

    sixth = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    assert(first != sixth)

    # a non-ImmutableDict that has the same keys and values as first

# Generated at 2022-06-12 23:00:16.574424
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immutable_dict = ImmutableDict({'key': 'value'})
    assert immutable_dict == {'key': 'value'}


# Generated at 2022-06-12 23:00:20.837601
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable((x for x in range(10)))
    assert is_iterable('abc')
    assert is_iterable({})
    assert is_iterable(ImmutableDict())
    assert is_iterable(True)
    assert not is_iterable(None)


# Generated at 2022-06-12 23:00:29.865301
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    idict = ImmutableDict({"one": 1, "two": 2, "three": 3})
    assert not idict == [1, 2, 3]
    assert not idict != [1, 2, 3]

    assert not idict == ("one", "two", "three")
    assert not idict != ("one", "two", "three")

    assert not idict == {"one": 1, "two": 2, "three": 3}
    assert not idict != {"one": 1, "two": 2, "three": 3}

    assert idict == ImmutableDict({"two": 2, "three": 3, "one": 1})
    assert not idict != ImmutableDict({"two": 2, "three": 3, "one": 1})


# Generated at 2022-06-12 23:00:37.372748
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(foo=1, bar=2)
    b = ImmutableDict(foo=1, bar=2)
    c = ImmutableDict(foo=1, bar=3)
    d = ImmutableDict(bar=2, foo=1)
    e = ImmutableDict(foo=1)
    f = ImmutableDict(foo=1)

    assert a == a
    assert a == b
    assert a != c
    assert a == d
    assert a != e
    assert e == f

# Generated at 2022-06-12 23:00:45.893452
# Unit test for function is_iterable
def test_is_iterable():
    """Verify is_iterable function"""
    # pylint: disable=redefined-outer-name
    not_iterable = [
        True,
        None,
        Ellipsis,
        set(),
        frozenset(),
        3.14,
        5,
        object(),
    ]
    for value in not_iterable:
        assert not is_iterable(value)
    assert is_iterable(dict())
    assert is_iterable(dict().keys())
    assert is_iterable(dict().values())
    assert is_iterable(dict().items())
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable('string')
    assert is_iterable(b'bytes')

# Generated at 2022-06-12 23:00:51.115297
# Unit test for function is_iterable
def test_is_iterable():

    assert not is_iterable(1)
    assert not is_iterable(True)

    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable((i for i in range(10)))



# Generated at 2022-06-12 23:00:59.532786
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    # assert is_iterable(1)  # Python >= 2.6 raises Exception and makes doctest fail
    assert is_iterable((x for x in range(10)))
    assert not is_iterable('abc')
    assert not is_iterable(u'abc')
    assert not is_iterable(b'abc')
    assert is_iterable('abc', include_strings=True)
    assert is_iterable(u'abc', include_strings=True)
    assert is_iterable(b'abc', include_strings=True)


# Generated at 2022-06-12 23:01:07.432742
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({"k1": 1, "k2": 2})
    d2 = ImmutableDict({"k1": 1, "k2": 2})
    d3 = ImmutableDict({"k2": 2, "k1": 1})
    d4 = ImmutableDict({"k1": 2, "k2": 3})
    assert d1 == d2
    assert d1 == d3
    assert d2 != d4

    assert d1 == {"k1": 1, "k2": 2}
    assert d1 == [("k1", 1), ("k2", 2)]
    assert d1 == (("k1", 1), ("k2", 2))


# Generated at 2022-06-12 23:01:17.646194
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import random

    def test_ImmutableDict_equality_against_same_dict(a):
        should_be_equal = (a == a)
        assert should_be_equal

    def test_ImmutableDict_equality_against_equal_dict(a, b):
        should_be_equal = (a == b)
        assert should_be_equal

    def test_ImmutableDict_inequality_against_different_dict(a, b):
        should_be_different = (a != b)
        assert should_be_different

    def random_dict_comparison(a, b):
        test_ImmutableDict_equality_against_same_dict(a)
        test_ImmutableDict_equality_against_same_dict(b)

        if a == b:
            test_ImmutableDict

# Generated at 2022-06-12 23:01:21.230477
# Unit test for function is_iterable
def test_is_iterable():
    class Iterable(object):
        def __iter__(self):
            return iter([])

    class NotIterable(object):
        pass

    assert is_iterable(Iterable())
    assert not is_iterable(NotIterable())



# Generated at 2022-06-12 23:01:53.772637
# Unit test for function is_iterable
def test_is_iterable():
    def assert_is_iterable(a, expected):
        assert is_iterable(a) == expected, 'Expected {} to be iterable: {}'.format(
            a, is_iterable(a))

    assert_is_iterable('hello', True)
    assert_is_iterable(u'hello', True)
    assert_is_iterable([], True)
    assert_is_iterable({}, True)
    assert_is_iterable((), True)
    assert_is_iterable(set(), True)
    assert_is_iterable((x for x in range(10)), True)
    assert_is_iterable({(x, y): x + y for x, y in [(1, 2), (3, 4)]}, True)

# Generated at 2022-06-12 23:02:02.262972
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id = ImmutableDict({'k1': 'v1', 'k2': 'v2'})
    assert id == id
    assert id != 'somestring'
    assert id != {'k1': 'v1', 'k2': 'v2'}
    # test for unexpected exceptions, as per hash(bad_object) - catch any and all
    bad_object = object()
    try:
        id == bad_object
    except Exception:
        assert True
    else:
        assert False
    # test for unexpected exceptions, as per hash(bad_object) - catch any and all
    bad_object = {'k1': 'v2'}
    try:
        id == bad_object
    except Exception:
        assert True
    else:
        assert False



# Generated at 2022-06-12 23:02:12.878493
# Unit test for function is_iterable
def test_is_iterable():
    class Dummy(object):
        def __iter__(self):
            for i in range(10):
                yield i

    class DummyNonIterable(object):
        pass

    assert(not is_iterable('abc'))
    assert(not is_iterable(u'abc'))
    assert(not is_iterable(1))
    assert(not is_iterable(None))

    assert(is_iterable(Dummy()))
    assert(is_iterable(['a', 'b', 'c']))
    assert(is_iterable(set([1, 2, 3])))
    assert(is_iterable({'k1':'v1', 'k2':'v2'}))
    assert(is_iterable(('a', 'b', 'c')))

# Generated at 2022-06-12 23:02:23.981138
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id1 = ImmutableDict({'a': 1, 'b': 2})
    id2 = ImmutableDict({'a': 1, 'b': 2})
    id3 = ImmutableDict({'a': 1, 'b': 3})
    id4 = ImmutableDict({'a': 1})
    # check that equals to itself
    assert id1 == id1
    # check that is equal to copy
    assert id1 == id2
    # check that is not equal when value differs
    assert id1 != id3
    # check that is not equal with dict
    assert id1 != dict(a=1, b=2)
    # check that is not equal with sequence
    assert id1 != ('a', 'b')
    # check that is not equal with Mapping class
    assert id1 != Mapping()
    # check

# Generated at 2022-06-12 23:02:33.812087
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test that method __eq__ of class ImmutableDict works as expected.

    Test that method __eq__ defines the same ImmutableDict as equal to itself. Test that
    it also defines equal ImmutableDicts as equal to each other. Finally test that
    it defines non-equal ImmutableDicts as non-equal to each other.
    """
    test_dicts = [
        ImmutableDict(testkey='testvalue1'),
        ImmutableDict(testkey='testvalue2'),
        ImmutableDict(testkey='testvalue3')
    ]

    # Test that method __eq__ defines the same ImmutableDict as equal to itself
    assert test_dicts[0] == test_dicts[0]

    # Test that it also defines equal ImmutableDicts as equal to each other

# Generated at 2022-06-12 23:02:44.341928
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    obj_1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    obj_2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    obj_3 = ImmutableDict({'a': 1, 'b': 3, 'c': 3})
    obj_4 = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    obj_5 = ImmutableDict({'a': 1, 'b': 2, 'c': 4})
    # test difference keys
    assert obj_1 != obj_4, "Objects are not equal"
    assert obj_1 != obj_5, "Objects are not equal"
    # test difference values

# Generated at 2022-06-12 23:02:52.426145
# Unit test for function is_iterable
def test_is_iterable():
    """
    Tests for is_iterable function
    """
    # A simple iterable
    a = [1, 2, 3]
    assert is_iterable(a)

    # A simple string
    b = "foo"
    assert is_iterable(b) is False

    # A simple string inside an iterable
    c = [1, 2, 3, "foo"]
    assert is_iterable(c)

    # A simple string inside an iterable and not including strings
    d = [1, 2, 3, "foo"]
    assert is_iterable(d, False) is False

    # A simple dict
    e = {"foo": 1, "bar": 2}
    assert is_iterable(e)



# Generated at 2022-06-12 23:02:57.437362
# Unit test for function is_iterable
def test_is_iterable():
    """Verify the is_iterable function behaves correctly"""

    assert is_iterable(['one','two','three'])
    assert is_iterable(('one','two','three'))
    assert is_iterable({'one':1,'two':'two','three':3})
    assert not is_iterable(1)
    assert not is_iterable(1.1)



# Generated at 2022-06-12 23:03:07.718897
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """The __eq__ method should compare equal against a full copy of the ImmutableDict"""
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2)
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=2, b=1)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=2, b=2)

    # Tags
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=2, tags={'a': 1})
    assert ImmutableDict(a=1, b=2, tags={'a': 1}) != ImmutableDict(a=1, b=2, tags={'a': 2})

# Generated at 2022-06-12 23:03:16.207975
# Unit test for function is_iterable
def test_is_iterable():
    """Unit tests for function is_iterable

    Expected behavior:
    is_iterable(None) -> False
    is_iterable(1) -> False
    is_iterable('abcdef') -> True
    is_iterable(b'abcdef') -> True
    is_iterable(bytearray(b'abcdef')) -> True
    is_iterable(set([1, 2, 3])) -> True
    is_iterable(dict([('1', 1), ('2', 2)])) -> True
    is_iterable(['a', 'b', 'c']) -> True
    """
    assert not is_iterable(None)
    assert not is_iterable(1)
    assert is_iterable('abcdef')
    assert is_iterable(b'abcdef')
    assert is_iterable

# Generated at 2022-06-12 23:04:12.321397
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a=23, b=42)
    d2 = ImmutableDict(b=42, a=23)
    d3 = ImmutableDict(b=42)
    d4 = ImmutableDict(a=24, b=42)
    assert d1 == d2, "Same dictionary should compare equal"
    assert d1 != d3, "Different dictionaries should compare not equal"
    assert d1 != d4, "Different dictionaries should compare not equal"



# Generated at 2022-06-12 23:04:16.291593
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Verify ImmutableDict __eq__ compatibility with a set"""

    import random
    s = set()
    a = dict()
    for i in range(100):
        key = random.randint(1, 100)
        s.add(key)
        a[key] = random.randint(1, 100)

    immutable_a = ImmutableDict(a)
    assert immutable_a == s

# Generated at 2022-06-12 23:04:21.236269
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Method __eq__ of class ImmutableDict compares a hash value of itself and the input
    :return: True if the hash value is the same, False otherwise
    """
    a = ImmutableDict({'a': 1, 'b': 2})
    b = ImmutableDict({'a': 1, 'b': 2})
    c = ImmutableDict({'a': 3, 'b': 2})
    assert a == b
    assert not (a == c)


# Generated at 2022-06-12 23:04:25.738335
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test equivalence of the same object
    obj = ImmutableDict({'a': 1, 'b': 2})
    assert obj == obj

    # Test equality of the same content
    assert obj == {'a': 1, 'b': 2}

    # Test inequality of different content
    assert not obj == {'a': 1}



# Generated at 2022-06-12 23:04:36.043700
# Unit test for function is_iterable
def test_is_iterable():
    # testing is_iterable
    assert is_iterable(None) is False
    assert is_iterable(1) is False
    assert is_iterable(True) is False
    assert is_iterable(dict()) is True
    assert is_iterable([]) is True
    assert is_iterable(tuple()) is True
    assert is_iterable(set()) is True
    assert is_iterable({}) is True
    assert is_iterable("") is True
    assert is_iterable(1, True) is True
    assert is_iterable('') is True
    assert is_iterable(None, True) is False
    assert is_iterable(str()) is True
    assert is_iterable(u'') is True
    assert is_iterable(b'') is True


# Generated at 2022-06-12 23:04:38.755037
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({"a": 123})
    b = ImmutableDict({"a": 123})
    c = ImmutableDict({"b": 123})
    assert a == b
    assert a != c

# Generated at 2022-06-12 23:04:46.122018
# Unit test for function is_iterable
def test_is_iterable():
    """A non-exhaustive test suite for function is_iterable()."""

    # Test non-iterable items
    assert not is_iterable(None)
    assert not is_iterable(42)

    # Test if strings are iterable
    assert is_iterable(u'unicode')
    assert is_iterable(b'bytes')

    # Test if tuples are iterable
    assert is_iterable(())
    assert is_iterable((1, 2, 3))

    # Test if lists are iterable
    assert is_iterable([])
    assert is_iterable([1, 2, 3])

    # Test if dicts are iterable
    assert is_iterable({})
    assert is_iterable({'a': 1, 'b': 2, 'c': 3})

    # Test if strings are not

# Generated at 2022-06-12 23:04:50.162373
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'1': 1, '2': 2, '3': 3})
    b = ImmutableDict({'1': 1, '2': 2, '3': 3})
    assert (a == b)
    b = ImmutableDict({'1': 1, '2': 2, '3': 4})
    assert (a != b)


# Generated at 2022-06-12 23:04:52.621463
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(14) and is_iterable([]) and is_iterable((x for x in range(10))) and is_iterable(set()) and is_iterable({}) and is_iterable('test')

# Generated at 2022-06-12 23:04:58.526761
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({1: 'a', 2: 'b', 3: 'c'}) == ImmutableDict({1: 'a', 2: 'b', 3: 'c'})

    assert not ImmutableDict({1: 'a', 2: 'b', 3: 'c'}) == {1: 'a', 2: 'b', 3: 'c'}
    assert not ImmutableDict({1: 'a', 2: 'b', 3: 'c'}) == ImmutableDict({1: 'a', 2: 'b'})
    assert not ImmutableDict({1: 'a', 2: 'b', 3: 'c'}) == ImmutableDict({1: 'a', 2: 'b', 4: 'd'})

