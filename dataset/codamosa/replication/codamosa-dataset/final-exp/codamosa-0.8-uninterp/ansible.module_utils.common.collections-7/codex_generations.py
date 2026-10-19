

# Generated at 2022-06-12 22:56:12.628805
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """ImmutableDict.__eq__ behaving as expected"""

    # ImmutableDict.__eq__ returns False when comparing with an object of different class
    assert not ImmutableDict(x=1) == {'x': 1}

    # ImmutableDict.__eq__ returns True when comparing to an object of the same class with the same content
    assert ImmutableDict(x=1) == ImmutableDict(x=1)

    # ImmutableDict.__eq__ returns True when comparing to an object of the same class with different content
    assert not ImmutableDict(x=1) == ImmutableDict(x=2)

# Generated at 2022-06-12 22:56:22.817360
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    idict = ImmutableDict({'a': 1, 'b': 2})
    assert idict == idict
    assert idict == {'a': 1, 'b': 2}
    assert idict == ImmutableDict({'a': 1, 'b': 2})
    assert idict == ImmutableDict({'b': 2, 'a': 1})
    assert idict == {'b': 2, 'a': 1}
    assert idict == dict({'b': 2, 'a': 1})
    assert idict == dict([('b', 2), ('a', 1)])
    assert idict == dict(b=2, a=1)
    assert idict == MutableMapping({'b': 2, 'a': 1})
    assert idict != {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-12 22:56:26.494386
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())

    assert not is_iterable(1)
    assert not is_iterable('a')
    assert not is_iterable(object())



# Generated at 2022-06-12 22:56:35.945600
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # testing cases when both objects are ImmutableDict
    # testing when they are equal
    d1 = ImmutableDict({"k1": 1, "k2": 2})
    d2 = ImmutableDict({"k1": 1, "k2": 2})
    assert d1 == d2
    # testing when they are not equal, because of different key-value pairs
    d1 = ImmutableDict({"k1": 1, "k2": 2})
    d2 = ImmutableDict({"k1": 1, "k2": 3})
    assert d1 != d2
    d1 = ImmutableDict({"k1": 1, "k2": 2})
    d2 = ImmutableDict({"k1": 3, "k2": 2})
    assert d1 != d2
    # testing when they

# Generated at 2022-06-12 22:56:42.310472
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(1) is False
    assert is_iterable('str') is False
    assert is_iterable(u'str') is False
    assert is_iterable('str', True) is True
    assert is_iterable(u'str', True) is True
    assert is_iterable((1, 2))
    assert is_iterable((x for x in range(10)))
    assert is_iterable(xrange(10))


# Generated at 2022-06-12 22:56:53.764336
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """A few tests to ensure that ImmutableDict.__eq__ behaves correctly."""
    # Test equality with different types
    assert ImmutableDict(a=1, b=2) != {'a': 1, 'b': 2}

    # Test equality with sorted input
    assert ImmutableDict(a=1, b=2) != ImmutableDict(b=2, a=1)

    # Test equality with different equality operator
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=4)

    # Test equality with different keys
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=2, c=3)

    # Test equality with different size

# Generated at 2022-06-12 22:57:01.676384
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({1:2}) == ImmutableDict({1:2})
    assert ImmutableDict(a=1,b=2) == ImmutableDict(b=2,a=1)
    assert ImmutableDict({1:2}) != ImmutableDict({1:3})
    assert ImmutableDict({1:2}) != ImmutableDict({1:2,3:4})
    assert ImmutableDict({1:2,3:4}) != ImmutableDict({1:2,4:4})
    assert not ImmutableDict({1:2}) == 1
    assert not ImmutableDict({1:2}) == {1:2}


# Generated at 2022-06-12 22:57:12.589223
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) == True
    assert is_iterable([1, 2, 3]) == True
    assert is_iterable(None) == False
    assert is_iterable({1, 2, 3}) == True
    assert is_iterable({1: 2}) == True
    assert is_iterable(1) == False
    assert is_iterable(1.0) == False
    assert is_iterable(u'abc') == True
    assert is_iterable(b'abc') == False
    assert is_iterable(set()) == True
    assert is_iterable(set([1, 2, 3])) == True
    assert is_iterable(frozenset()) == True
    assert is_iterable(frozenset([1, 2, 3])) == True

# Generated at 2022-06-12 22:57:18.772172
# Unit test for function is_iterable
def test_is_iterable():
    class Foo:  # pylint: disable=too-few-public-methods
        pass

    assert is_iterable('foobar')
    assert is_iterable(b'foobar')
    assert is_iterable((1, 2))
    assert is_iterable([1, 2])
    assert is_iterable({'foo': 'bar'})
    assert is_iterable(set([1, 2]))
    assert is_iterable(Foo)
    assert is_iterable(Foo())

    assert not is_iterable(1)
    assert not is_iterable(1.0)
    assert not is_iterable(None)



# Generated at 2022-06-12 22:57:28.924351
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test method __eq__ of class ImmutableDict"""
    mydict = ImmutableDict(a='a', b='b', c='c')
    # Test equality with itself and another ImmutableDict created from a dict
    assert mydict == mydict
    assert mydict == ImmutableDict(mydict)
    # Test inequality with another ImmutableDict created from a dict with a different value
    assert not mydict == ImmutableDict(a='a', b='b', c='d')
    # Test inequality with objects that are not dict-like
    assert not mydict == ('a', 'b', 'c')
    assert not mydict == ['a', 'b', 'c']
    assert not mydict == set(['a', 'b', 'c'])
    # Test inequality with dict-like objects that are not ImmutableDicts

# Generated at 2022-06-12 22:57:40.587843
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    dict = ImmutableDict({"foo": "bar"})
    dict2 = ImmutableDict({"foo": "bar"})
    dict3 = ImmutableDict({"foo": "not_bar"})
    dict4 = {"foo": "bar"}

    assert dict2 == dict, 'dict2 and dict should be equal'
    assert dict3 != dict, 'dict3 and dict should not be equal'
    try:
        assert dict4 == dict, 'dict4 and dict should raise an exception'
    except TypeError:
        assert True
    except:
        assert False
    """
    pass

# Generated at 2022-06-12 22:57:47.383723
# Unit test for function is_iterable
def test_is_iterable():
    # Non-iterable objects
    non_iterables = [None, None, 1, True, 1.0]
    iterables = [
        [], (), {}, set(),
        (x for x in range(3))
    ]
    iterables_with_strings = [
        'a', u'b', b'c'
    ] + iterables

    for non_iterable in non_iterables:
        assert not is_iterable(non_iterable)
        assert not is_iterable(non_iterable, include_strings=True)
        assert not is_sequence(non_iterable)
        assert not is_sequence(non_iterable, include_strings=True)

    for iterable in iterables:
        assert is_iterable(iterable)

# Generated at 2022-06-12 22:57:57.218061
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Verifies that class ImmutableDict implements method __eq__ properly

    To use, uncomment following snippet and run this file as python script
    if __name__ == '__main__':
        sys.exit(test_ImmutableDict___eq__())
    """
    from sys import exit
    from collections import Mapping
    from ansible.module_utils.six import string_types, binary_type

    try:
        from collections import OrderedDict
    except ImportError:
        from ansible.module_utils.basic import OrderedDict

    # Dictionary with string keys
    idict_1 = ImmutableDict({'test_key': 'test_value'})
    # Dictionary with numeric keys
    idict_2 = ImmutableDict({1: 'test_value2'})
    # Dictionary with multiple string keys


# Generated at 2022-06-12 22:58:05.877327
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 3})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 2}, c=3)

# Generated at 2022-06-12 22:58:16.184027
# Unit test for function is_iterable
def test_is_iterable():
    # is string iterable?
    assert is_iterable('abc')
    assert is_iterable(u'abc')
    assert is_iterable(b'abc')

    # is tuple iterable?
    assert is_iterable((1, 2, 3))

    # is dict iterable?
    assert is_iterable({'a': 1, 'b': 2})

    # is list iterable?
    assert is_iterable([1, 2, 3])

    # is set iterable?
    assert is_iterable(set([1, 2, 3]))

    # is does not fail on None
    assert is_iterable(None) is False

    # is does not fail on int
    assert is_iterable(5) is False



# Generated at 2022-06-12 22:58:18.946312
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable(1) is False
    assert is_iterable({}) is True
    assert is_iterable(()) is True

# Generated at 2022-06-12 22:58:27.733767
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""
    d1 = ImmutableDict({'a': 'A'})
    d2 = ImmutableDict({'a': 'A'})
    d3 = ImmutableDict({'a': 'A', 'b': 'B'})
    d4 = 'some other object'
    d5 = ImmutableDict({'a': 'other A'})

    assert (d1 == d2) == True
    assert (d1 == d3) == False
    assert (d1 == d4) == False
    assert (d1 == d5) == False


# Generated at 2022-06-12 22:58:31.304417
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['a', 'b', 'c'])
    assert is_iterable((1, 2, 3))
    assert is_iterable({'key1': 'value1', 'key2': 'value2'})

    assert not is_iterable(1)
    assert not is_iterable('abc')


# Generated at 2022-06-12 22:58:36.350109
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict_1 = ImmutableDict({'a': 1, 'b': 2})
    dict_2 = ImmutableDict({'a': 1, 'b': 2})
    dict_3 = ImmutableDict({'a': 1, 'b': 3})
    dict_4 = ImmutableDict({'a': 3, 'b': 2})
    dict_5 = ImmutableDict({'b': 2, 'a': 1})

    assert dict_1 == dict_1
    assert dict_1 == dict_2
    assert dict_1 == dict_5

    assert dict_1 != dict_3
    assert dict_1 != dict_4



# Generated at 2022-06-12 22:58:47.332321
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict1 = ImmutableDict({'k1':'v1', 'k2':'v2'})
    test_dict2 = ImmutableDict({'k1':'v1', 'k2':'v2'})
    test_dict3 = ImmutableDict({'k1':'v1', 'k2':'v2', 'k3':'v3'})
    test_dict4 = ImmutableDict({'k2':'v2', 'k1':'v1'})
    test_dict5 = ImmutableDict({'k4':'v4', 'k1':'v1'})

    test_list1 = ['v1', 'v2']
    test_list2 = ['v1', 'v2']

# Generated at 2022-06-12 22:59:08.039262
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Testing __eq__ function of ImmutableDict class
    """
    values = {"name": "Django Reinhardt", "instrument": "guitar"}
    immutable_dict = ImmutableDict(values)
    same_immutable_dict = ImmutableDict(values)
    different_immutable_dict = ImmutableDict({"name": "Charlie Christian", "instrument": "guitar"})
    assert immutable_dict == same_immutable_dict
    assert immutable_dict == values
    assert values == immutable_dict
    assert {'name': 'Django Reinhardt', 'instrument': 'guitar'} == immutable_dict
    assert immutable_dict != different_immutable_dict
    assert immutable_dict != "Random String"
    assert immutable_dict != ["Random String"]
    assert immutable_dict

# Generated at 2022-06-12 22:59:14.561653
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([0])
    assert is_iterable((0,))
    assert is_iterable({0: 0})
    assert is_iterable(range(10))
    assert is_iterable(1) == False
    assert is_iterable(None) == False
    assert is_iterable('string')
    assert is_iterable(b'bytes')
    assert is_iterable('string', include_strings=False) == False
    assert is_iterable(b'bytes', include_strings=False) == False



# Generated at 2022-06-12 22:59:22.085518
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert not is_iterable(3)
    assert is_iterable((1, 2, 3))
    assert is_iterable(range(3))
    assert is_iterable('abc', include_strings=True)
    assert not is_iterable('abc')
    assert is_iterable(u'abc', include_strings=True)
    assert not is_iterable(u'abc')
    assert is_iterable(b'abc', include_strings=True)
    assert not is_iterable(b'abc')



# Generated at 2022-06-12 22:59:27.646611
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict([('a', 1), ('b', 2), ('c', 3)])
    b = ImmutableDict([('b', 2), ('c', 3), ('a', 1)])
    assert a == b
    assert not a == {'a': 1, 'b': 2, 'c': 3}
    assert not a == []
    assert not a == None


# Generated at 2022-06-12 22:59:37.797091
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    iDict_left = ImmutableDict({1: 'a', 2: 'b', 3: 'c'})
    iDict_right = ImmutableDict({1: 'a', 2: 'b', 3: 'c'})
    iDict_different = ImmutableDict({1: 1, 2: 2, 3: 3})

    assert iDict_left == iDict_right
    assert iDict_left != iDict_different

    class iDict_different_class(Hashable):
        def __init__(self, dict_):
            self.dict_ = dict_

        def __eq__(self, other):
            try:
                if self.__hash__() == hash(other):
                    return True
            except TypeError:
                pass
            return False


# Generated at 2022-06-12 22:59:42.508679
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable("hello world")
    assert not is_iterable("hello world", include_strings=False)

    assert is_iterable(("hello", "world"))
    assert is_iterable([1, 2, 3])
    assert is_iterable(range(10))
    assert is_iterable({1, 2, 3})
    assert is_iterable({1: 'one', 2: 'two'})
    assert is_iterable(ImmutableDict({1: 'one', 2: 'two'}))
    assert is_iterable(open("/dev/null"))

    assert not is_iterable(1)
    assert not is_iterable(1.0)


# Generated at 2022-06-12 22:59:47.885035
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    original = ImmutableDict([('first', 'answer'), ('second', 'question')])
    test1 = ImmutableDict([('first', 'answer'), ('second', 'question')])
    test2 = ImmutableDict([('second', 'question'), ('first', 'answer')])

    assert(original.__hash__() == test1.__hash__())
    assert(test1 == test2)
    assert(test1 == original)
    assert(test1.__hash__() == test2.__hash__())


# Generated at 2022-06-12 22:59:57.406107
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    d3 = {'a': 1, 'b': 2}
    d4 = ImmutableDict(a=1, b=2, c=3)
    d5 = ImmutableDict(a=1, b=2, c=3)
    d6 = {'a': 1, 'b': 2, 'c': 3}
    d7 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    d8 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert d1 == d2
    assert d1 != d3
    assert d4 == d5
    assert d4

# Generated at 2022-06-12 23:00:03.569529
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable("abc") == False
    assert is_iterable("abc", True) == True
    assert is_iterable(u"abc") == False
    assert is_iterable(u"abc", True) == True
    assert is_iterable([1, 2, 3]) == True
    assert is_iterable(range(3)) == True
    assert is_iterable({"a": 1, "b": 2}) == True
    assert is_iterable(x for x in range(3)) == True
    assert is_iterable(5) == False


# Generated at 2022-06-12 23:00:09.391360
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test that ImmutableDict.__eq__ works as expected
    """
    d1 = ImmutableDict({'key': 'value'})
    d2 = ImmutableDict({'key': 'value'})

    assert d1 == d2
    assert d1.__eq__(d2)
    assert d1.__eq__({'key': 'value'})



# Generated at 2022-06-12 23:00:36.572584
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'spam': 1, 'eggs': 2}, beans=3)
    b = ImmutableDict({'eggs': 2, 'beans': 3, 'spam': 1})
    c = ImmutableDict({'spam': 2, 'eggs': 2}, beans=3)
    d = ImmutableDict({'spam': 1, 'eggs': 2})
    e = ImmutableDict({'spam': 1})
    f = ImmutableDict()
    g = ImmutableDict([])

    assert a == b
    assert a != c
    assert a != d
    assert a != e
    assert a != f
    assert a != g



# Generated at 2022-06-12 23:00:43.463978
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = ImmutableDict({'hello': 'world'})
    dict1_ = ImmutableDict({'hello': 'world'})
    dict2 = ImmutableDict({'hello': 'moon'})
    dict3 = dict({'hello': 'world'})
    dict4 = dict({'hello': 'world'})
    dict5 = {'hello': 'world'}
    dict6 = {'hello': 'world'}

    assert dict1 == dict1_
    assert dict1 != dict2
    assert dict1 != dict3
    assert dict1 == dict4
    assert dict1 != dict5
    assert dict1 == dict6



# Generated at 2022-06-12 23:00:54.979728
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test0 = ImmutableDict()
    test1 = ImmutableDict({'a': 1})
    test2 = ImmutableDict({'b': 2})
    test3 = ImmutableDict({'a': 1, 'b': 2})
    test4 = ImmutableDict({'b': 2, 'a': 1})
    test5 = ImmutableDict({1: 'a'})
    test6 = ImmutableDict({'a': 2})
    test7 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert test0 == ImmutableDict()
    assert test1 == ImmutableDict({'a': 1})
    assert test1 == test1
    assert test1 != test2
    assert test3 == test4
    assert test6 != test1
    assert test7

# Generated at 2022-06-12 23:01:00.424984
# Unit test for function is_iterable
def test_is_iterable():
    """
     Function for testing function is_iterable
     Needs to be in a separate function for reasons of unittest
    """
    assert is_iterable(('a', 'b')) == True
    assert is_iterable('a') == True
    assert is_iterable(1) == False
    assert is_iterable({'a': 'b'}) == True



# Generated at 2022-06-12 23:01:04.707327
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable(u'abc')
    assert is_iterable(u'abc'.encode('utf-8'))
    assert not is_iterable({1, 2, 3})
    assert not is_iterable(1)

# Generated at 2022-06-12 23:01:06.456701
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    first = ImmutableDict(a=9)
    second = ImmutableDict(a=9)
    assert first == second


# Generated at 2022-06-12 23:01:12.658886
# Unit test for function is_iterable
def test_is_iterable():
    test_iter = (('text', True),
                 ('', True),
                 (1, False),
                 ({}, True),
                 ([], True),
                 (set(), True),
                 (None, False))

    for key, value in test_iter:
        if is_iterable(key) != value:
            raise Exception('test_is_iterable: Failed. is_iterable({0}) != {1}'.format(repr(key), repr(value)))

    string_test_iter = (('text', False),
                        ('', False),
                        (1, False),
                        ({}, True),
                        ([], True),
                        (set(), True),
                        (None, False))

    # Strings are not iterable unless include_strings is set to True

# Generated at 2022-06-12 23:01:23.263356
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils.common._collections_compat import Dict, List
    from ansible.module_utils.common.collections import ImmutableDict

    # Test equality of two ImmutableDicts
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})

    # Test equality of hashes of two ImmutableDicts with different order of the same items
    assert ImmutableDict({'b': 2, 'a': 1}) == ImmutableDict({'a': 1, 'b': 2})

    # Test equality of ImmutableDicts and non-ImmutableDict
    assert ImmutableDict({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}

    # Test equality of ImmutableDicts and non-

# Generated at 2022-06-12 23:01:33.330093
# Unit test for function is_iterable
def test_is_iterable():
    # is_iterable is a function that takes two arguments,
    # the first being an iterable and the second being a boolean
    # that determines whether to include strings and bytes in the iterable

    # Test array, string and other objects
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert not is_iterable([1, 2, 3]) if not is_string([1, 2, 3]) else True
    assert is_iterable("Hello, World!")
    assert not is_iterable("Hello, World!") if not is_string("Hello, World!") else True
    assert is_iterable(123)
    assert not is_iterable(123) if not is_string(123) else True

    # Test optional argument 'include_strings'

# Generated at 2022-06-12 23:01:42.024925
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(0)
    assert not is_iterable(False)
    assert is_iterable(range(0))
    assert is_iterable([])
    assert is_iterable({})
    assert not is_iterable(ImmutableDict())
    assert not is_iterable("")
    assert not is_iterable(b"")
    assert is_iterable(range(0), include_strings=True)
    assert is_iterable("", include_strings=True)
    assert is_iterable(b"", include_strings=True)


# Generated at 2022-06-12 23:02:27.318553
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    data1 = ImmutableDict(foo=1)
    data2 = ImmutableDict(foo=1)
    assert data1 == data2
    assert data2 == data1
    data2 = ImmutableDict(foo=2)
    assert data1 != data2
    data2 = ImmutableDict(foo=1, bar=2)
    assert data1 != data2
    data1 = ImmutableDict(foo=1, bar=2)
    assert data1 == data2
    data2 = ImmutableDict(bar=2, foo=1)
    assert data1 == data2
    data1 = ImmutableDict(foo=1, bar=2, baz=3)
    data2 = ImmutableDict(bar=2, foo=1, baz=3)
    assert data1 == data2
   

# Generated at 2022-06-12 23:02:30.563832
# Unit test for function is_iterable
def test_is_iterable():
    class A(object):
        pass

    a = A()
    assert is_iterable(a) is False

    a.__iter__ = lambda self: iter([])
    assert is_iterable(a) is True

    a.__iter__ = lambda self: 1
    assert is_iterable(a) is False

    a.__iter__ = lambda self: None
    assert is_iterable(a) is False

# Generated at 2022-06-12 23:02:36.946895
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    immutable_dict_1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    immutable_dict_2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    immutable_dict_3 = ImmutableDict({'a': 1})
    immutable_dict_4 = ImmutableDict({'a': 1, 'b': 2, 'c': 4})

    assert immutable_dict_1.__eq__(immutable_dict_2) == True
    assert immutable_dict_1.__eq__(immutable_dict_3) == False
    assert immutable_dict_1.__eq__(immutable_dict_4) == False

# Generated at 2022-06-12 23:02:45.621064
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test equality of ImmutableDict instances"""
    immutable_dict_1 = ImmutableDict(dict(key1='value1', key2='value2'))
    immutable_dict_2 = ImmutableDict(dict(key2='value2', key1='value1'))
    mutable_dict_1 = dict(key1='value1', key2='value2')
    non_dict = {}

    assert immutable_dict_1 == immutable_dict_2
    assert immutable_dict_2 == immutable_dict_1
    assert immutable_dict_1 != mutable_dict_1
    assert immutable_dict_1 != non_dict



# Generated at 2022-06-12 23:02:50.500949
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(1) is False
    assert is_iterable(u'test') is True
    assert is_iterable(b'test') is True
    assert is_iterable('test') is True
    assert is_iterable(['test']) is True
    assert is_iterable(set(['test'])) is True
    assert is_iterable(dict(test=1)) is True
    assert is_iterable(frozenset(['test'])) is True
    assert is_iterable(MutableMapping()) is True
    assert is_iterable(ImmutableDict()) is True
    assert is_iterable(lambda: 'test') is True  # Lambda functions are callable


# Generated at 2022-06-12 23:02:53.535212
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable((1,2,3))
    assert is_iterable(range(10))
    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable('string')


# Generated at 2022-06-12 23:03:03.715836
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test method __eq__ of class ImmutableDict"""
    first_dict = ImmutableDict({'a_string': 'value_string', 'a_number': 23, 'a_list': [1, 2]})
    second_dict = ImmutableDict({'a_string': 'value_string', 'a_number': 23, 'a_list': [1, 2]})
    third_dict = ImmutableDict({'a_string': 'value_string', 'a_number': 23})
    fourth_dict = ImmutableDict({'a_string': 'value_string', 'a_number': 23, 'a_list': [3, 4]})
    non_dict = {'a_list': [1, 2], 'a_number': 23, 'a_string': 'value_string'}
    assert first_

# Generated at 2022-06-12 23:03:08.464828
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set([]))
    assert is_iterable('')
    assert is_iterable(b'')
    assert is_iterable(tuple())
    assert is_iterable(None) is False
    assert is_iterable(5) is False


# Generated at 2022-06-12 23:03:13.915288
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test for check of equality of two immutable dicts
    assert ImmutableDict({'a': 42, 'b': [1, 2, 3]}) == ImmutableDict({'a': 42, 'b': [1, 2, 3]})
    # Test for check of equality of immutable and mutable dicts
    assert ImmutableDict({'a': 42, 'b': [1, 2, 3]}) == {'a': 42, 'b': [1, 2, 3]}



# Generated at 2022-06-12 23:03:20.202374
# Unit test for function is_iterable
def test_is_iterable():
    class _not_iterable(object):
        pass
    class _iterable(object):
        def __iter__(self):
            pass
    class _indexable(object):
        def __getitem__(self, key):
            pass
    class _indexable_but_not_iterable(_indexable):
        # This is the case of builtin types like str, bytes, bytearray, memoryview
        # and UserString.MutableString.
        pass
    class _indexable_and_iterable(_indexable, _iterable):
        pass

    assert not is_iterable(_not_iterable())
    assert is_iterable(_iterable())
    assert is_iterable(_indexable())
    assert is_iterable(_indexable_but_not_iterable())

# Generated at 2022-06-12 23:04:41.263974
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    # create some ImmutableDicts and non ImmutableDicts
    a = ImmutableDict({'a': 1, 'b': 2})
    b = ImmutableDict({'a': 1, 'b': 2})
    c = ImmutableDict({'a': 1, 'b': 3})
    d = dict({'a': 1, 'b': 2})

    # Test equality of ImmutableDicts
    # Test equal
    assert a == b
    # Test not equal
    assert a != c
    # Test comparing to dicts
    assert a != d

    # Test equality between ImmutableDicts and non ImmutableDicts
    # Test equal
    assert a != d
    # Test not equal
    assert a != d
    # Test comparing to dicts
    assert a != d

    # Test equality of ImmutableDicts with other

# Generated at 2022-06-12 23:04:45.792139
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1])
    assert is_iterable((1, 2))
    assert is_iterable({})
    assert is_iterable({1:2})
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert not is_iterable(object())


# Generated at 2022-06-12 23:04:50.770188
# Unit test for function is_iterable
def test_is_iterable():
    # Only list and tuple
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable(set())
    assert is_iterable({})
    assert is_iterable(xrange(1))
    assert is_iterable(u'')
    assert is_iterable(b'')

    assert not is_iterable(5)
    assert not is_iterable(None)
    assert not is_iterable('string')


# Generated at 2022-06-12 23:04:59.506968
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert not is_iterable(None)
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable('string')
    assert not is_iterable('string', include_strings=False)
    assert is_iterable('string', include_strings=True)
    assert is_iterable(b'bytes')
    assert not is_iterable(b'bytes', include_strings=False)
    assert is_iterable(b'bytes', include_strings=True)
    assert is_iterable(lambda: True)
    assert is_iterable(dict())
    assert not is_iterable(dict(), include_strings=True)
    assert is_iterable(dict().keys())


# Generated at 2022-06-12 23:05:09.705275
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test equality of ImmutableDict under different scenarios

    :return: True if the test passes, false otherwise
    :rtype: bool
    """
    # hashable object
    immutable_dict_a = ImmutableDict(a='a', b='b')
    immutable_dict_b = ImmutableDict(a='a', b='b')
    assert immutable_dict_a == immutable_dict_b

    # non-hashable object
    immutable_dict_c = ImmutableDict(a='a', b=set())
    immutable_dict_d = ImmutableDict(a='a', b=set())
    assert immutable_dict_c == immutable_dict_d

    # containing __eq__
    immutable_dict_e = ImmutableDict(a='a', b=ImmutableDict())
    immutable_dict

# Generated at 2022-06-12 23:05:14.922282
# Unit test for function is_iterable
def test_is_iterable():

    def non_iterable():
        return 1

    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert not is_iterable(set())
    assert not is_iterable(non_iterable)
    assert not is_iterable(object)
    assert not is_iterable(True)
    assert is_iterable(1)
    assert is_iterable(None)


# Generated at 2022-06-12 23:05:23.138409
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    test_ImmutableDict___eq__()
    """
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'b': 2, 'a': 1})
    dict3 = ImmutableDict({'c': 2})

    assert dict1 == dict2
    assert dict1 != dict3
    assert dict1 != dict1.union({'a': 3})

    assert dict1 != ImmutableDict([('a', 1), ('b', 2)])
    assert dict1 != dict({'a': 1, 'b': 2})
    assert dict1 != {'a': 1, 'b': 2}
    assert dict1 != 3

# Generated at 2022-06-12 23:05:33.600479
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = ImmutableDict({'a': 'b'})
    d2 = ImmutableDict({'a': 'b'})
    d3 = ImmutableDict({'a': 'b', 'b': 'c'})
    a = 'a'
    b = ('a',)
    c = ('a', 'b')
    t = ('a', 'b', 'c')
    t2 = ('a', 'b', 'd')
    t3 = ('c', 'b', 'a')
    assert(d == d2)
    assert(d != d3)
    assert(d != a)
    assert(d != b)
    assert(d != c)
    assert(d != t)
    assert(d != t2)
    assert(d != t3)


# Generated at 2022-06-12 23:05:41.995633
# Unit test for function is_iterable
def test_is_iterable():
    # Test is_iterable function with different types of inputs

    # Testing with different iterables
    # True as expected
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable(range(3))
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable({1: "a", 2: "b", 3: "c"})
    assert is_iterable(frozenset([1, 2, 3]))
    assert is_iterable(ImmutableDict({"a": 1, "b": 2, "c": 3}))
    assert is_iterable(u'abcd')
    assert is_iterable(b'abcd')

    # False as expected
    assert is_iterable(2)

# Generated at 2022-06-12 23:05:51.010172
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable"""
    from collections import (MutableSequence, MutableSet, MutableMapping)

    def make_generator():
        for i in range(1, 5):
            yield i

    class MySeq(MutableSequence):
        """MutableSequence class used for testing is_iterable"""
        def __init__(self, iterable):
            self.data = list(iterable)

        def __getitem__(self, index):
            return self.data[index]

        def __setitem__(self, index, value):
            self.data[index] = value

        def __delitem__(self, index):
            del self.data[index]

        def __len__(self):
            return len(self.data)
