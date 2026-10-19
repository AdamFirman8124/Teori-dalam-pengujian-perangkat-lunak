

# Generated at 2022-06-12 22:56:10.974489
# Unit test for method __eq__ of class ImmutableDict

# Generated at 2022-06-12 22:56:18.318022
# Unit test for function is_iterable
def test_is_iterable():
    """Test function is_iterable()."""
    class MyIterable(object):
        def __iter__(self):
            return self

    assert is_iterable(1) is False
    assert is_iterable("str") is True
    assert is_iterable("str", include_strings=False) is False
    assert is_iterable(MyIterable()) is True
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable({1, 2, 3}) is True
    assert is_iterable({1: 2, 3: 4}) is True



# Generated at 2022-06-12 22:56:27.427714
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test for __eq__ in the same class
    original_immutable_dict = ImmutableDict({'a': 1, 'b': 2})
    copy_immutable_dict = ImmutableDict({'a': 1, 'b': 2})
    assert original_immutable_dict == copy_immutable_dict
    # Test for __eq__ with regular dictionary
    regular_dict = {'a': 1, 'b': 2}
    assert original_immutable_dict == regular_dict
    # Test for __eq__ with different original ImmutableDict
    assert original_immutable_dict != ImmutableDict({'a': 1, 'b': 4})


# Generated at 2022-06-12 22:56:32.323463
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    map1 = ImmutableDict({'hash': 'value'})
    map2 = ImmutableDict({'hash': 'value'})
    assert(map1 == map2)
    map3 = ImmutableDict({'hash': 'mismatch'})
    assert(map1 != map3)
    assert(map2 != map3)



# Generated at 2022-06-12 22:56:37.698716
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(dict())
    assert is_iterable(set())
    assert not is_iterable(object())
    assert not is_iterable(1)
    assert is_iterable('')
    assert is_iterable('str')
    assert is_iterable(u'unicode')
    assert is_iterable(b'bytes')
    assert is_iterable(tuple())
    assert is_iterable(xrange(0))


# Generated at 2022-06-12 22:56:47.822253
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1])
    assert is_iterable({'a': 1})
    assert is_iterable(set((1, 2)))
    assert is_iterable((x for x in range(3)))
    assert is_iterable(['a'])
    assert is_iterable(('b',))
    assert is_iterable(range(1))
    assert is_iterable(1) is False
    assert is_iterable(None) is False
    assert is_iterable(1) is False

    # check string with include_strings = True
    assert is_iterable('a', include_strings=True) is True

    # check string with include_strings = False
    assert is_iterable('a', include_strings=False) is False



# Generated at 2022-06-12 22:56:54.639784
# Unit test for function is_iterable
def test_is_iterable():
    def string_gen():
        yield 'string'

    assert is_iterable('string') is False
    assert is_iterable(b'byte') is False
    assert is_iterable(['string']) is True
    assert is_iterable(('string',)) is True
    assert is_iterable({'key': 'value'}) is True
    assert is_iterable(string_gen()) is True
    assert is_iterable(None) is False



# Generated at 2022-06-12 22:57:03.048775
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 'b'}) == ImmutableDict({'a': 'b'})
    assert ImmutableDict({'a': 'b'}) == {'a': 'b'}
    assert ImmutableDict({'a': 'b', 'c': 'd'}) == {'a': 'b', 'c': 'd'}
    assert ImmutableDict({'a': 'b'}) == ImmutableDict({'a': 'b', 'd': 'e'})
    assert ImmutableDict({'a': 'b'}) == ImmutableDict({'c': 'd'})
    assert ImmutableDict({'a': 'b'}) != {'a': 'c'}
    assert ImmutableDict({'a': 'b'}) != 'foo'
    assert ImmutableDict

# Generated at 2022-06-12 22:57:12.636311
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    A dictionary that cannot be updated
    :return:
    """
    # Create a ImmutableDict from a regular dict
    d = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    e = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    f = ImmutableDict({'key1': 'value1'})

    # Test different comparison
    assert(d == e)
    assert(d != f)

    # Other type of dictionary
    g = {'key1': 'value1', 'key2': 'value2'}

    # Comparison with different type
    assert(d != g)



# Generated at 2022-06-12 22:57:16.937557
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(foo='bar') == ImmutableDict(foo='bar')
    assert not (ImmutableDict(foo='bar') == ImmutableDict(foo='baz'))
    assert not (ImmutableDict(foo='bar') == {'foo': 'bar'})
    assert not (ImmutableDict(foo='bar') == 'foo')


# Generated at 2022-06-12 22:57:23.932818
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1) == ImmutableDict(a=1)
    assert ImmutableDict(a=1) != ImmutableDict(a=2)
    assert ImmutableDict(a=1) != {'a': 1}

# Generated at 2022-06-12 22:57:33.551895
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Tests that ImmutableDict objects compare equal when they are equal in content.

    A hash is populated with the following items:

    {'a': 0, 'b': 'abc', 'c': ('d', 0)}

    The issue was that if another hash was populated with the same keys and values
    but in a different order, the hashes were considered unequal.  This was fixed
    by comparing the hash contents with a hash of the contents (frozenset).
    """

    d = ImmutableDict({'a': 0, 'b': 'abc', 'c': ('d', 0)})
    d2 = ImmutableDict({'c': ('d', 0), 'a': 0, 'b': 'abc'})

    assert d == d2

# Generated at 2022-06-12 22:57:42.180299
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable((x for x in range(3)))
    assert is_iterable(set([1, 2, 3]))
    # Test bytes in Python3
    if hasattr(__builtins__, 'bytes'):
        assert is_iterable(b'')
        assert is_iterable(b'foo')
        assert is_iterable((b'foo', b'bar'))
    assert not is_iterable('foo')
    assert not is_iterable('foo')
    assert not is_iterable(1)
    assert not is_iterable(object())



# Generated at 2022-06-12 22:57:48.163067
# Unit test for function is_iterable
def test_is_iterable():
    """Tests for the is_iterable function"""
    assert is_iterable([1, 2, 3])
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable(1)
    assert is_iterable(3.14)
    assert is_iterable(dict())
    assert is_iterable('foo')
    assert is_iterable(u'foo')
    assert is_iterable(b'foo')
    assert not is_iterable(1, True)
    assert not is_iterable(3.14, True)
    assert not is_iterable(dict(), True)
    assert is_iterable('foo', True)
    assert is_iterable(u'foo', True)
    assert is_

# Generated at 2022-06-12 22:57:58.116349
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test __eq__ method of class ImmutableDict.
    """
    dict1 = ImmutableDict({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
    dict2 = ImmutableDict({3: 'c', 1: 'a', 2: 'b', 4: 'd'})
    dict3 = ImmutableDict({4: 'd', 1: 'a', 2: 'b', 3: 'c'})
    dict4 = ImmutableDict({4: 'd', 1: 'a', 2: 'b'})
    dict5 = ImmutableDict({4: 'd', 1: 'a', 2: 'c', 3: 'c'})
    dict6 = ImmutableDict({4: 'd', 1: 'a'})

    assert dict1 == dict2


# Generated at 2022-06-12 22:58:03.709083
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict_1 = ImmutableDict({'first': 'name', 'second': 'last_name'})
    test_dict_2 = ImmutableDict({'first': 'name', 'second': 'last_name'})
    test_dict_3 = ImmutableDict({'second': 'last_name', 'first': 'name'})
    assert test_dict_1 == test_dict_2
    assert not test_dict_1 == test_dict_3


# Generated at 2022-06-12 22:58:09.369941
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable(xrange(10))
    assert is_iterable((1, 2, 3))
    assert is_iterable("hello")
    assert is_iterable(1)
    assert is_iterable(u'hi')
    assert not is_iterable(None)


# Generated at 2022-06-12 22:58:16.183987
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Unit test for method __eq__ of class ImmutableDict
    """
    id1 = ImmutableDict({'a':1})
    id2 = ImmutableDict({'a':1})
    id3 = id1.union({'b':2})

    assert(id1 == id2)
    assert(id1 != id3)
    assert(id1 != {'a':1})
    assert(id1 != 'a')



# Generated at 2022-06-12 22:58:21.552154
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'b': 2, 'a': 1})
    assert d1 == d2
    d3 = ImmutableDict({'b': 2})
    assert not d1 == d3
    assert not d3 == d1
    assert not d1 == None

# Generated at 2022-06-12 22:58:28.480032
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(dict())
    assert is_iterable(list())
    assert is_iterable(tuple())
    assert is_iterable(xrange(4))
    assert is_iterable({1, 2, 3})
    assert not is_iterable(0)
    assert not is_iterable(2.5)
    assert not is_iterable(True)
    assert not is_iterable(None)
    assert not is_iterable(set())


# Generated at 2022-06-12 22:58:43.572860
# Unit test for function is_iterable
def test_is_iterable():
    # Test a non iterable object
    assert is_iterable(123) == False
    # Test an empty string
    assert is_iterable('') == False
    # Test a string
    assert is_iterable('a string') == False
    # Test an empty list
    assert is_iterable([]) == True
    # Test a list
    assert is_iterable(['one', 'two']) == True
    # Test an empty hash
    assert is_iterable({}) == True
    # Test a hash
    assert is_iterable({'key': 'value'}) == True


# Generated at 2022-06-12 22:58:52.647132
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2]) is True
    assert is_iterable((1, 2)) is True
    assert is_iterable({1, 2}) is True
    assert is_iterable({1: 2, 3: 4}) is True
    assert is_iterable("hello world") is True
    assert is_iterable(u"hello world") is True
    assert is_iterable(b"hello world") is True
    assert is_iterable(bytearray(b"hello world")) is True
    assert is_iterable(1) is False
    assert is_iterable(1.0) is False
    assert is_iterable(object()) is False
    assert is_iterable(None) is False

# Generated at 2022-06-12 22:58:56.326723
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2})
    b = ImmutableDict({'a': 1, 'b': 2})
    c = ImmutableDict({'a': 1, 'b': 3})

    assert a == b
    assert not a == c
    assert not a == {'a': 1, 'b': 2}
    assert not a == 5

# Generated at 2022-06-12 22:59:08.429141
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Given
    d1 = ImmutableDict(a=1, b=2, c=3)
    d2 = ImmutableDict(a=1, b=2, c=3)
    d3 = ImmutableDict(a=1, b=2, d=3)
    d4 = ImmutableDict(a=1, b=2, c=3, d=4)
    d5 = ImmutableDict(a=1, b=2)
    d6 = ImmutableDict(a=1, c=3)
    d7 = ImmutableDict(b=2, c=3)
    d8 = ImmutableDict(a=1, b=2, c=4)

# Generated at 2022-06-12 22:59:14.523982
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(4) == False
    assert is_iterable(u'four') == False
    assert is_iterable(b'four') == False
    assert is_iterable('four') == False
    assert is_iterable([4]) == True
    assert is_iterable((4,)) == True
    assert is_iterable({4: 4}) == True
    assert is_iterable(set([4])) == True
    assert is_iterable(xrange(1, 2)) == True



# Generated at 2022-06-12 22:59:24.616932
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable((), include_strings=False)
    assert is_iterable(('',), include_strings=False)
    assert is_iterable(range(10), include_strings=False)
    assert is_iterable('', include_strings=True)
    assert is_iterable(b'', include_strings=True)

    class MyIterable:
        def __iter__(self):
            return iter([])

    assert is_iterable(MyIterable())
    assert is_iterable(MyIterable, include_strings=False)

    class MyNonIterable:
        pass

    assert not is_iterable(MyNonIterable())

# Generated at 2022-06-12 22:59:35.197798
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test that __eq__ properly compares dictionaries"""
    # Test that empty dicts are equal
    dict1 = ImmutableDict()
    dict2 = ImmutableDict()
    assert dict1.__eq__(dict2)

    # Test that dicts with different keys are not equal
    dict1 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    dict2 = ImmutableDict({'key1': 'value1', 'key3': 'value3'})
    assert not dict1.__eq__(dict2)

    # Test that dicts with different values are not equal
    dict1 = ImmutableDict({'key1': 'value1', 'key2': 'value2'})

# Generated at 2022-06-12 22:59:38.082662
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    m = ImmutableDict({"a": 1, "b": 2})
    m1 = ImmutableDict({"a": 1, "b": 2})
    m2 = ImmutableDict({"a": 1, "b": 2, "c": 3})

    assert m == m1
    assert m.__hash__() == m1.__hash__()
    assert m != m2
    assert m.__hash__() != m2.__hash__()

# Generated at 2022-06-12 22:59:40.830831
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1,2]) == True
    assert is_iterable([1,2]) == True
    assert is_iterable(set([1,2])) == True
    assert is_iterable({'key': 'value'}) == True
    assert is_iterable(1) == False
    assert is_iterable('string') == False


# Generated at 2022-06-12 22:59:48.470520
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    map1 = ImmutableDict({1: 'a', 2: 'b', 3: 'c'})
    map2 = ImmutableDict({1: 'a', 2: 'b', 3: 'c'})
    map3 = ImmutableDict({3: 'c', 2: 'b', 1: 'a'})
    map4 = ImmutableDict({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
    map5 = ImmutableDict({1: 'e', 2: 'b', 3: 'c'})
    map6 = ImmutableDict(map1)

    # Equivalent maps
    assert map1 == map2
    assert map1 == map3
    # Different
    assert not map1 == map4
    assert not map1 == map5
    assert map1 == map6

# Generated at 2022-06-12 23:00:06.779421
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({"a": 1, "b": 2})
    b = ImmutableDict({"b": 2, "a": 1})
    assert a == b
    assert not a == None
    assert not a == 1
    assert not a == {"a": 1, "b": 2}


# Generated at 2022-06-12 23:00:17.215771
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test for case when the object is not ImmutableDict
    raw_data = {1: 'a', 2: 'b'}
    immutable_dict = ImmutableDict(raw_data)
    not_immutable_dict = sorted(raw_data.keys())
    assert immutable_dict != not_immutable_dict
    # Test for case when the object is ImmutableDict
    immutable_dict_2 = ImmutableDict(raw_data)
    assert immutable_dict == immutable_dict_2
    # Test for case when the object is MutableMapping
    mutable_dict = MutableMapping(raw_data)
    assert immutable_dict == mutable_dict
    # Test for case when two dictionaries are not equal
    assert immutable_dict != ImmutableDict({1: 'b', 2: 'b'})

# Generated at 2022-06-12 23:00:24.564508
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable."""
    # Test the expected functionality of function is_iterable
    iterable_obj = [1, 2, 3, 4, 5]
    assert(is_iterable(iterable_obj))
    assert(is_iterable(iterable_obj, True))
    assert(is_iterable(iterable_obj, False))

    non_iterable_obj = 3
    assert(not is_iterable(non_iterable_obj))
    assert(not is_iterable(non_iterable_obj, True))
    assert(not is_iterable(non_iterable_obj, False))


# Generated at 2022-06-12 23:00:30.892290
# Unit test for function is_iterable
def test_is_iterable():
    test_iterable = ([1, 2, 3], (1, 2, 3), set([1, 2, 3]), {1: 'a', 2: 'b', 3: 'c'})
    test_not_iterable = (1, 2, 3, 4)

    for iterable in test_iterable:
        assert is_iterable(iterable)

    for not_iterable in test_not_iterable:
        assert not is_iterable(not_iterable)



# Generated at 2022-06-12 23:00:40.954335
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test method __eq__ of class ImmutableDict for different inputs.
    """

    # Test for two ImmutableDicts with same key/value pairs
    immutable_dict_1 = ImmutableDict({1: 'ansible'})
    immutable_dict_2 = ImmutableDict({1: 'ansible'})
    assert isinstance(immutable_dict_1, ImmutableDict)
    assert isinstance(immutable_dict_2, ImmutableDict)
    assert immutable_dict_1.__eq__(immutable_dict_2)

    # Test for two ImmutableDicts with different number of key/value pairs
    immutable_dict_1 = ImmutableDict({1: 'ansible', 2: 'redhat'})
    immutable_dict_2 = ImmutableDict({1: 'ansible'})


# Generated at 2022-06-12 23:00:44.347774
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test the __eq__ method of ImmutableDict"""

    id1 = ImmutableDict(a=1, b=2, c=3)
    id2 = ImmutableDict(a=1, b=2, c=3)
    assert id1 == id2



# Generated at 2022-06-12 23:00:55.900093
# Unit test for function is_iterable
def test_is_iterable():
    class Iterable:
        def __iter__(self):
            pass

    assert is_iterable(Iterable())
    assert not is_iterable(object())
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable((i for i in range(10)))
    assert is_iterable(ImmutableDict())
    assert is_iterable(text_type(), include_strings=True)
    assert is_iterable(binary_type(), include_strings=True)

    # is_iterable should be agnostic to the type of the iterable
    class IterableSequence(Iterable, Sequence):
        pass
    assert is_iterable(IterableSequence())

    class IterableMapping(Iterable, Mapping):
        pass

# Generated at 2022-06-12 23:01:03.295043
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(xrange(0))
    assert is_iterable('abc')
    assert is_iterable(b'abc')

    assert not is_iterable('c', include_strings=False)
    assert not is_iterable(b'c', include_strings=False)
    assert not is_iterable(mapping_type=None)


# Generated at 2022-06-12 23:01:06.418609
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable"""
    assert is_iterable([])
    assert is_iterable('')
    assert is_iterable((x for x in range(3)))
    assert not is_iterable({})
    assert not is_iterable('abc')



# Generated at 2022-06-12 23:01:12.634425
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Method __eq__(self, other) should return True if the objects have the same keys and values
    and False otherwise"""
    immutable_dict1 = ImmutableDict({'key1': 'val1', 'key2': 'val2'})
    immutable_dict2 = ImmutableDict({'key3': 'val3', 'key2': 'val2'})
    immutable_dict3 = ImmutableDict({'key1': 'val1', 'key2': 'val2'})
    immutable_dict4 = ImmutableDict({'key2': 'val2', 'key1': 'val1'})
    immutable_dict5 = ImmutableDict(key1='val1', key2='val2')
    immutable_dict6 = ImmutableDict(key2='val2', key1='val1')
    immutable_dict7

# Generated at 2022-06-12 23:01:47.053600
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test1 = ImmutableDict({"a": 1, "b": 2})
    test2 = ImmutableDict({"a": 1, "b": 2})
    test3 = ImmutableDict({"b": 2, "a": 1})
    assert test1.__eq__(test2)
    assert test1.__eq__(test3)
    assert not test1.__eq__({"a": 1, "b": 2})
    assert not test1.__eq__({"a": 2, "b": 2})
    assert not test1.__eq__({"a": 1})


# Generated at 2022-06-12 23:01:56.216255
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable('string')
    assert not is_iterable(u'string')
    assert not is_iterable(1)
    assert not is_iterable(3.14)
    assert not is_iterable(True)
    assert not is_iterable(None)

    assert is_iterable(tuple())
    assert is_iterable([])
    assert is_iterable(dict())
    assert is_iterable(set())
    assert is_iterable(list(range(5)))
    assert is_iterable((1, 2, 3, 4))
    assert is_iterable([1, 2, 3, 4])
    assert is_iterable(set([1, 2, 3, 4]))
    assert is_iterable({'f': 1, 's': 2, 't': 3})



# Generated at 2022-06-12 23:02:02.867091
# Unit test for function is_iterable
def test_is_iterable():

    class A(object):

        def __init__(self, values):
            self.values = values
            self.count = 0

        def __iter__(self):
            while self.count < len(self.values):
                self.count += 1
                yield self.values[self.count - 1]

    a = A([1, 2])
    assert is_iterable(a)

    class B(object):

        def __init__(self, values):
            self.values = values
            self.count = 0

        def __getitem__(self, key):
            return self.values[key]

    b = B([1, 2])
    assert is_iterable(b)

    assert not is_iterable(1)


# Generated at 2022-06-12 23:02:13.500570
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 'b', 'c': 'd'}) == ImmutableDict({'c': 'd', 'a': 'b'})
    assert ImmutableDict({'a': 'b', 'c': 'd'}) == ImmutableDict({'c': 'd', 'a': 'b', 'e': 'f'})
    assert ImmutableDict({'a': 'b', 'c': 'd'}) == {'c': 'd', 'a': 'b'}
    assert ImmutableDict({'a': 'b', 'c': 'd'}) == {'c': 'd', 'a': 'b', 'e': 'f'}

# Generated at 2022-06-12 23:02:22.235263
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable('2')
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable({})
    assert is_iterable(dict())
    assert is_iterable(object())
    assert is_iterable(ImmutableDict())

    assert not is_iterable(None)
    assert not is_iterable('2', include_strings=False)
    assert is_iterable('2', include_strings=True)

    class TestClass:
        def __iter__(self):
            return iter([])

    assert is_iterable(TestClass())



# Generated at 2022-06-12 23:02:29.074337
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 'b', 2: 3})
    b = ImmutableDict({'a': 'b', 2: 3})
    assert a == b
    b = ImmutableDict({'a': 'b', 2: 3, 'c': 'd'})
    assert a != b
    assert a != None
    assert a != {'a': 'b', 2: 3}
    assert a != ['a']
    assert a != 'a'

# Generated at 2022-06-12 23:02:38.204782
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test method __eq__ of class ImmutableDict"""
    # Test ImmutableDict objects of different lengths are not equal
    immutable_dict_1 = ImmutableDict(a=1)
    immutable_dict_2 = ImmutableDict(a=1, b=2)
    assert(immutable_dict_1 != immutable_dict_2)
    # Test ImmutableDict objects with different paths are not equal
    immutable_dict_3 = ImmutableDict(a=2)
    assert(immutable_dict_1 != immutable_dict_3)
    # Test ImmutableDict objects with same paths and values are equal
    immutable_dict_4 = ImmutableDict(a=1)
    assert(immutable_dict_1 == immutable_dict_4)
    # Test ImmutableDict objects are equal to dictionaries with same

# Generated at 2022-06-12 23:02:47.774366
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = ImmutableDict(dict(a=1, b=2))
    dict2 = ImmutableDict((('a', 1), ('b', 2)))
    dict3 = ImmutableDict(dict(a=1, b=2))
    dict4 = ImmutableDict(dict(a=10, b=20))
    dict5 = ImmutableDict(dict(a=1, b=2), a=10)
    dict6 = ImmutableDict(dict(a=1))
    dict7 = MutableMapping()

    assert dict1 == dict2
    assert dict1 != dict4
    assert dict1 != dict5
    assert dict1 != dict6
    assert dict1 != dict7
    assert dict1 == dict3
    assert dict4 != dict3

# Generated at 2022-06-12 23:02:50.521375
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = dict(a=1, b=2)
    d2 = dict(a=1, b=2)
    assert ImmutableDict(d1) == ImmutableDict(d2)



# Generated at 2022-06-12 23:02:59.927977
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test equality with ImmutableDict
    dict_1 = ImmutableDict({1: '1', 2: '2'})
    dict_2 = ImmutableDict({1: '1', 2: '2'})
    dict_3 = ImmutableDict({1: '1', 3: '2'})
    dict_4 = ImmutableDict({2: '2', 1: '1'})
    assert dict_1 == dict_1
    assert dict_1 == dict_2
    assert dict_1 == dict_4
    assert dict_1 != dict_3
    assert dict_2 != dict_3

    # Test equality with dict
    dict_1 = ImmutableDict({1: '1', 2: '2'})
    dict_2 = {1: '1', 2: '2'}
    dict_3

# Generated at 2022-06-12 23:04:06.432852
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    m1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    m2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert hash(m1) == hash(m2)
    assert m1 == m2
    m3 = ImmutableDict({'a': 4, 'b': 2, 'c': 3})
    assert m1 != m3
    assert hash(m1) != hash(m3)
    m4 = ImmutableDict({'a': 3.14, 'b': '2', 'c': text_type(3)})
    assert m1 != m4
    assert hash(m1) != hash(m4)


if __name__ == '__main__':
    test_ImmutableDict___eq__()

# Generated at 2022-06-12 23:04:11.815817
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable."""
    assert is_iterable(())
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable({})
    assert is_iterable("str")

    assert not is_iterable(0)
    assert not is_iterable("")
    assert not is_iterable(None)


# Generated at 2022-06-12 23:04:17.257042
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    id1 = ImmutableDict(foo='bar', baz='qux')
    id2 = ImmutableDict(baz='qux', foo='bar')
    id3 = ImmutableDict(baz='qux', foo='bar', quuz='corge')

    assert (id1 == id1) is True
    assert (id1 == id2) is True
    assert (id1 == id3) is False
    assert (id2 == id1) is True
    assert (id2 == id2) is True
    assert (id2 == id3) is False
    assert (id3 == id1) is False
    assert (id3 == id2) is False
    assert (id3 == id3) is True



# Generated at 2022-06-12 23:04:22.450446
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import unittest

    class TestImmutableDict(unittest.TestCase):

        def test_equals(self):
            self.assertEqual(ImmutableDict({'a': 1, 'b': 2}), ImmutableDict({'a': 1, 'b': 2}))

        def test_not_equals_if_not_hashable(self):
            self.assertNotEqual(ImmutableDict({'a': 1, 'b': 2}), {'a': 1, 'b': 2})

        def test_not_equals_if_different_type(self):
            self.assertNotEqual(ImmutableDict({'a': 1, 'b': 2}), 'test')


# Generated at 2022-06-12 23:04:30.104350
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 2, 'b': 5.0}) == {'a': 2, 'b': 5.0}
    assert ImmutableDict({'a': 2, 'b': 5.0}) == ImmutableDict({'b': 5.0, 'a': 2})
    assert ImmutableDict({'a': 2, 'b': 5.0}) != {'a': 3, 'b': 5.0}
    assert ImmutableDict({'a': 2, 'b': 5.0}) != ImmutableDict({'b': 10, 'a': 2})

# Generated at 2022-06-12 23:04:39.585634
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable(iter([1, 2, 3]))
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable({1, 2, 3})
    assert is_iterable(dict({'a': 1, 'b': 2}))
    assert is_iterable(ImmutableDict(a=1, b=2))
    assert is_iterable(range(10))

    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(object())

    # Strings are iterable, but it is configurable
    assert is_iterable('abc')

# Generated at 2022-06-12 23:04:44.871239
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils.facts.dict_facts import cache
    dict_result = cache.copy()
    dict_result['distribution_version'] = '7'
    dict_result['distribution_major_version'] = '7'

    immutable_dict_result = ImmutableDict(dict_result)
    immutable_dict_result2 = ImmutableDict(dict_result)
    immutable_dict_result3 = ImmutableDict(dict_result)
    immutable_dict_result3['distribution_version'] = '6'
    immutable_dict_result3['distribution_major_version'] = '6'

    result = immutable_dict_result == immutable_dict_result2
    assert result

    result = immutable_dict_result == immutable_dict_result3
    assert not result

    result = immutable_dict_result

# Generated at 2022-06-12 23:04:48.516547
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable('abc') is True
    assert is_iterable(1) is False
    assert is_iterable(None) is False
    assert is_iterable([]) is True



# Generated at 2022-06-12 23:04:55.672501
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['1', '2', '3'])
    assert is_iterable(('1', '2', '3'))
    assert is_iterable({'1', '2', '3'})
    assert is_iterable({'a': '1', 'b': '2', 'c': '3'})
    assert is_iterable(None) is False
    assert is_iterable('test') is False
    #assert isinstance(ImmutableDict({'a': '1', 'b': '2', 'c': '3'}), Iterable)
    assert is_string(ImmutableDict({'a': '1', 'b': '2', 'c': '3'})) is False



# Generated at 2022-06-12 23:05:00.747350
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable([1, 2, 3])
    assert is_iterable('test')
    assert is_iterable(set([1, 2, 3]))
    assert not is_iterable(1)
    assert not is_iterable(None)
