

# Generated at 2022-06-12 22:56:12.543909
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""
    dict1 = ImmutableDict({"a": 1, "b": 2})
    dict2 = ImmutableDict({"a": 1, "b": 2})
    dict3 = ImmutableDict({"a": 1})
    dict4 = ImmutableDict({"a": 1, "b": 3})
    dict5 = ImmutableDict({"c": 3, "b": 2})
    dict6 = ImmutableDict({"b": 2, "a": 1})
    dict7 = dict({"a": 1, "b": 2})
    dict8 = dict({"a": 1})

    assert dict1 == dict2
    assert not dict1 == dict3
    assert dict1 == dict6
    assert not dict1 == dict4
    assert not dict

# Generated at 2022-06-12 22:56:16.978343
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert not is_iterable(1)
    assert is_iterable((1, 2, 3))
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable('abc')
    assert is_iterable(b'abc')



# Generated at 2022-06-12 22:56:23.858680
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = ImmutableDict({'a': 3, 'b': 1, 'c': 2})
    dict2 = {'a': 3, 'b': 1, 'c': 2}
    dict3 = ImmutableDict({'a': 3, 'b': 2, 'c': 3})
    dict4 = ImmutableDict({'a': 3, 'b': 1, 'c': 2})

    assert dict1 == dict2
    assert dict1 != dict3
    assert dict1 == dict4


# Generated at 2022-06-12 22:56:33.988377
# Unit test for function is_iterable
def test_is_iterable():
    # Test with lists
    assert is_iterable([1, 2, 3])
    assert is_iterable([])
    # Test with dictionaries
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable({})
    # Test with tuples
    assert is_iterable((1, 2, 3))
    assert is_iterable(())
    # Test with sets
    assert is_iterable(set(range(10)))
    assert is_iterable(set())
    # Test with strings
    assert is_iterable('123')
    assert is_iterable('')
    # Test with bytes
    assert is_iterable(b'123')
    assert is_iterable(b'')
    # Test with generators
    assert is_iterable(x for x in range(10))

# Generated at 2022-06-12 22:56:42.743412
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # TODO: update this test when support for Python 2.6.6 is discontinued and
    #  `assertDictEqual` becomes available
    import operator
    import unittest

    class TestImmutableDict___eq__(unittest.TestCase):
        def test_ImmutableDict___eq__None(self):
            dict1 = {'a': 1, 'b': 2, 'c': 3}
            dict2 = None
            self.assertFalse(ImmutableDict(dict1) == dict2)
            self.assertEqual(len(operator.eq(ImmutableDict(dict1), dict2)), 0)

        def test_ImmutableDict___eq__True(self):
            dict1 = {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-12 22:56:52.176981
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Check the method ImmutableDict.__eq__()
    """
    a = ImmutableDict()
    b = ImmutableDict()
    a['foo'] = 'bar'
    b['foo'] = 'bar'
    assert a == b

    a = ImmutableDict()
    b = ImmutableDict()
    a['foo'] = 'bar'
    b['baz'] = 'bar'
    assert a != b

    a = ImmutableDict()
    b = ImmutableDict()
    a['foo'] = 'bar'
    b['foo'] = 'baz'
    assert a != b


# Generated at 2022-06-12 22:56:57.148015
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({"foo": "bar"})
    b = ImmutableDict({"foo": "bar"})
    c = ImmutableDict({"foo": "baz"})

    assert a == b
    assert a != c
    assert a != "something else"
    assert a != {"foo": "bar"}
    assert a != {"foo": "baz"}

# Generated at 2022-06-12 22:56:59.961899
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(a=1, c=3)
    b = ImmutableDict(a=1, b=2)
    assert a != b
    assert a == ImmutableDict(a=1, c=3)

# Generated at 2022-06-12 22:57:06.492113
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict({'one': 1}) == ImmutableDict({'one': 1})
    assert ImmutableDict({'one': 1, 'two': 2}) == ImmutableDict({'two': 2, 'one': 1})
    assert ImmutableDict({'one': 1}) != dict()
    assert ImmutableDict({'one': 1}) != ImmutableDict()
    assert ImmutableDict({'one': 1}) != ImmutableDict({'two': 2})
    assert ImmutableDict({'one': 1}).union({'two': 2}) == ImmutableDict({'one': 1, 'two': 2})
    assert ImmutableDict({'one': 1}).union({'two': 2}) != ImmutableDict({'one': 1})

# Generated at 2022-06-12 22:57:16.600316
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # test __eq__ returns True if compared to itself
    shallow_dict = ImmutableDict({'a': 1, 'b': 2})
    assert shallow_dict == shallow_dict

    # test __eq__ returns True if compared to equal hashable
    another_shallow_dict = ImmutableDict({'a': 1, 'b': 2})
    assert shallow_dict == another_shallow_dict

    # test __eq__ returns False if compared to a different hashable
    yet_another_shallow_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert not (shallow_dict == yet_another_shallow_dict)

    # test __eq__ returns True if compared to a nested hashable
    inner_dict = {'a': 1, 'b': 2}
    # Note that

# Generated at 2022-06-12 22:57:30.842201
# Unit test for function is_iterable
def test_is_iterable():
    import collections
    assert is_iterable('foo')
    assert is_iterable(['foo'])
    assert is_iterable((1, 2, 3))
    assert is_iterable({'foo': 'bar'})
    assert is_iterable(collections.deque(['foo', 'bar']))

    class Iterable(object):
        def __iter__(self):
            return iter('asdf')

    assert is_iterable(Iterable())
    assert is_iterable(xrange(10))
    assert not is_iterable({})

    class NotIterable(object):

        def __init__(self, number):
            self.number = number

        def __repr__(self):
            return 'Not Iterable'

    assert not is_iterable(NotIterable(10))

# Unit test

# Generated at 2022-06-12 22:57:35.176249
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('test')
    assert is_iterable([1, 2, 3])
    assert not is_iterable(None)
    assert is_iterable(1)
    assert not is_iterable(1, include_strings=False)
    assert is_iterable(b'123', include_strings=True)


# Generated at 2022-06-12 22:57:43.997805
# Unit test for function is_iterable
def test_is_iterable():
    # Test string
    assert is_iterable('string')
    assert not is_iterable('string', include_strings=False)

    # Test bytes
    assert is_iterable(b'bytes')
    assert not is_iterable(b'bytes', include_strings=False)

    # Test list
    assert is_iterable([1, 2, 3])

    # Test tuple
    assert is_iterable((1, 2, 3))

    # Test set
    assert is_iterable({1, 2, 3})

    # Test dictionary
    assert is_iterable({1: 'one', 2: 'two', 3: 'three'})

    # Test generator
    assert is_iterable((i * 2 for i in [1, 2, 3]))

    # Test number
    assert not is_iterable(1)

    #

# Generated at 2022-06-12 22:57:52.041939
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test __eq__ method functionality"""

    # If a and b both have the same hash, they must be equal
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'a': 1, 'c': 3, 'b': 2})
    assert hash(a) == hash(b)
    assert a == b

    # If the hashes don't match, the dicts can still be equal
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'a': 1, 'c': 3, 'b': 3})
    assert hash(a) != hash(b)
    assert a != b

    # If the type of a and b do not match, they cannot be equal
    a = Immutable

# Generated at 2022-06-12 22:57:54.164222
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})



# Generated at 2022-06-12 22:58:02.121054
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable((1, 2, 3))
    assert is_iterable({'a': 1})
    assert is_iterable('ciao')
    assert is_iterable(('a', 'b', 'c'))
    assert is_iterable({'a', 'b'})

    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(1.5)

    class Foo(object):
        """an object that is not iterable"""
        pass
    foo = Foo()
    assert not is_iterable(foo)



# Generated at 2022-06-12 22:58:12.107211
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils.basic import env_fallback

    # Verify that two different ImmutableDict instances with the same content are equal
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'b': 2, 'a': 1})

    # Verify that a dictionary and an ImmutableDict with the same content are not equal
    assert ImmutableDict({'a': 1, 'b': 2}) != {'a': 1, 'b': 2}

    # Verify that an ImmutableDict does not compare to a non-dictionary
    assert ImmutableDict({'a': 1, 'b': 2}) != 'a'

    # Verify that the ImmutableDict comparison works with nested dictionaries

# Generated at 2022-06-12 22:58:23.422761
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=2, b=3)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=3)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=1)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2, c=3)
    assert not ImmutableDict(a=1, b=2) == 'not a dict'
    assert not ImmutableDict(a=1, b=2) == None


# Unit

# Generated at 2022-06-12 22:58:30.536828
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict_1 = ImmutableDict([('1', 1), ('2', 2), ('3', 3)])
    test_dict_2 = dict([('1', 1), ('2', 2), ('3', 3)])
    test_dict_3 = dict([('1', 1), ('2', 2), ('3', 1)])
    if test_dict_1 == test_dict_1:
        pass
    else:
        assert False

    if not test_dict_1 == test_dict_2:
        assert False

    if not test_dict_1 == test_dict_3:
        assert False

# Generated at 2022-06-12 22:58:36.798726
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id_1 = ImmutableDict({'a': 'b'})
    id_2 = ImmutableDict({'a': 'b'})
    assert(id_1 == id_2)

    id_1 = ImmutableDict({'a': 'b', 'c': 'd'})
    id_2 = ImmutableDict({'c': 'd', 'a': 'b'})
    assert(id_1 == id_2)

    id_1 = ImmutableDict({'a': 'b'})
    id_2 = ImmutableDict({'a': 'c'})
    assert(not id_1 == id_2)

    id_1 = ImmutableDict({'a': 'b', 'c': 'd'})
    id_2 = ImmutableDict({'c': 'd'})


# Generated at 2022-06-12 22:58:53.984727
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() == {}
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2)
    assert ImmutableDict(a=1, b=2) == {'a': 1, 'b': 2}
    assert ImmutableDict(a=1, b=2) != {'a': 1, 'b': 3}
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=2, c=3)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=2, b=3)

# Generated at 2022-06-12 22:58:58.155530
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(())
    assert not is_iterable(1)
    assert not is_iterable(True)
    assert not is_iterable(None)
    assert not is_iterable('abc')
    assert not is_iterable(b'abc')



# Generated at 2022-06-12 22:59:04.850762
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1})
    d2 = ImmutableDict({'a': 1})
    d3 = ImmutableDict({'a': 2})
    d4 = dict({'a': 1})
    assert d1 == d1
    assert d1 == d2
    assert d1 != d3
    assert d1 != d4


# Generated at 2022-06-12 22:59:10.596373
# Unit test for function is_iterable
def test_is_iterable():
    """Unit tests for function is_iterable"""
    for test_arg in [[], {}, set(), ()]:
        assert is_iterable(test_arg)
    for test_arg in [0, '', u'']:
        assert not is_iterable(test_arg)
    for test_arg in [0, '', u'']:
        assert is_iterable(test_arg, True)


# Generated at 2022-06-12 22:59:15.810139
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = ImmutableDict({"a": 1, "b": 2})
    assert (d == {"a": 1, "b": 2, "c": 3}) is False
    assert (d == 1) is False
    assert (d == {"a": 1, "b": 2}) is True
    l = [1, 2, 3]
    assert (d == l) is False
    assert (d == d) is True
    assert (d == {"a": 1, "b": 2}) is True

# Generated at 2022-06-12 22:59:21.172847
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import collections
    import random
    import string
    import operator
    from functools import reduce

    # Generate a random list
    random_list = lambda: [random.choice(string.printable) for i in range(100)]

    # Generate a random dictionary
    random_dict = lambda: dict((key, random.choice(string.printable)) for key in random_list())

    for i in range(100):
        # Generate two dictionaries that are equal
        d1 = random_dict()
        d2 = d1.copy()
        # Generate two dictionaries that are not equal
        d3 = random_dict()
        d4 = random_dict()

        # Make sure that the ImmutableDicts are hashes of the dictionaries
        # (Test the __hash__ function)

# Generated at 2022-06-12 22:59:24.607027
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'b': 2, 'a': 1})
    assert d1 == d2



# Generated at 2022-06-12 22:59:34.356306
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Equality with a matching instance of ImmutableDict
    first = ImmutableDict(first='one', second=2)
    second = ImmutableDict(first='one', second=2)
    assert first == second

    # None equality with different items
    first = ImmutableDict(first='one', second=2)
    second = ImmutableDict(first='two', second=2)
    assert first != second

    # None equality with empty dict
    first = ImmutableDict()
    assert first != {}

    # None equality with empty sequence
    first = ImmutableDict(first='one', second=2)
    second = (('first', 'one'), ('second', 'two'))
    assert first != second


# Generated at 2022-06-12 22:59:40.747158
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(10)
    assert not is_iterable('some string')
    assert is_iterable([1])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable((1,2,3))
    assert is_iterable(u'unicode string')
    assert not is_iterable(u'unicode string', include_strings=False)
    assert is_iterable(b'some bytes string')
    assert not is_iterable(b'some bytes string', include_strings=False)



# Generated at 2022-06-12 22:59:47.576045
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(dict()) is True
    assert is_iterable(list()) is True
    assert is_iterable(tuple()) is True
    assert is_iterable('string') is False
    assert is_iterable(u'string') is False
    assert is_iterable(1) is False
    assert is_iterable(True) is False
    assert is_iterable(None) is False
    assert is_iterable(set()) is True
    assert is_iterable(b'bytes') is False
    assert is_iterable(dict({'a':1})) is True
    assert is_iterable([1,2,3]) is True
    assert is_iterable((1,2,3)) is True



# Generated at 2022-06-12 23:00:06.152906
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) == True
    assert is_iterable({}) == True
    assert is_iterable('foo') == False
    assert is_iterable('foo', True) == True
    assert is_iterable(63) == False

# Generated at 2022-06-12 23:00:16.575557
# Unit test for function is_iterable
def test_is_iterable():
    class Gen(object):
        def __init__(self, value):
            self.value = value

    def generator():
        for i in range(10):
            yield i

    i = 1
    assert is_iterable(range(10))
    assert is_iterable(xrange(10))
    assert is_iterable(set(range(10)))
    assert is_iterable(frozenset(range(10)))
    assert is_iterable({'key': 1})
    assert is_iterable((1, 2, 3))
    assert is_iterable(generator())
    assert is_iterable(Gen(5))
    assert is_iterable([i])
    assert is_iterable(iter(range(10)))

    assert not is_iterable(i)
    assert not is_iterable('string')

# Generated at 2022-06-12 23:00:24.689017
# Unit test for function is_iterable
def test_is_iterable():
    """Test the function is_iterable()."""
    examples = [
        ([1, 2, 3], True),
        ("asdf", True),
        ("", True),
        (1, False),
        ({"a": 1, "b": 2}, True),
        ({"a": 1, "b": 2}.keys(), True),
        ({"a": 1, "b": 2}.values(), True),
        ({"a": 1, "b": 2}.items(), True),
    ]
    for input, expected in examples:
        assert is_iterable(input, include_strings=True) == expected
        assert is_iterable(input, include_strings=False) == (isinstance(input, Sequence) or expected)



# Generated at 2022-06-12 23:00:28.066609
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('Hello')
    assert is_iterable(['Hello'])
    assert not is_iterable('Hello', include_strings=False)
    assert is_iterable('Hello', include_strings=True)



# Generated at 2022-06-12 23:00:38.801583
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import unittest
    import copy

    class TestImmutableDict___eq__(unittest.TestCase):

        def setUp(self):
            self.immutable_dict_a = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
            self.immutable_dict_b = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
            self.immutable_dict_c = ImmutableDict({'key1': 'value1', 'key3': 'value3'})

        def test_equality_with_another_ImmutableDict_type_with_same_keys_and_values(self):
            self.assertTrue(self.immutable_dict_a == self.immutable_dict_b)


# Generated at 2022-06-12 23:00:42.545931
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Arrange
    left = ImmutableDict(dict(foo='bar'))
    right = ImmutableDict(dict(foo='bar'))
    wrong = ImmutableDict(dict(foo='baz'))

    # Act
    # Assert
    assert left == right
    assert left != wrong
    assert left != 1

# Generated at 2022-06-12 23:00:47.012791
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({1: 'a'})
    assert not is_iterable(10)
    assert not is_iterable(None)


# Generated at 2022-06-12 23:00:53.998798
# Unit test for function is_iterable
def test_is_iterable():
    # Check that all Sequences are recognized
    assert is_iterable(range(10))
    assert is_iterable([1, 2, 3])
    assert is_iterable(set())
    assert is_iterable(())
    assert is_iterable('')
    assert is_iterable(b'')

    # Check that non-Sequences are rejected
    assert not is_iterable(1)
    assert not is_iterable(True)



# Generated at 2022-06-12 23:00:57.156163
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable('string')
    assert not is_iterable('string', include_strings=True)
    assert is_iterable('string', include_strings=True)


# Generated at 2022-06-12 23:01:06.750984
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test the ImmutableDict.__eq__ method
    """

    # Test equal dictionaries
    left_dict = ImmutableDict(dict(key='value'))
    right_dict = ImmutableDict(dict(key='value'))
    assert (True == (left_dict.__eq__(right_dict)))

    # Test different dictionaries with the same hash
    left_dict = ImmutableDict(dict(key='value'))
    right_dict = ImmutableDict(dict(key='other_value'))
    assert (False == (left_dict.__eq__(right_dict)))

    # Test dictionaries with different hashes
    left_dict = ImmutableDict(dict(key='value'))
    right_dict = ImmutableDict(dict(key='value', new_key='value'))

# Generated at 2022-06-12 23:01:45.129654
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({1: 2}) == ImmutableDict({1: 2})
    assert not (ImmutableDict({1: 2}) == ImmutableDict({2: 3}))
    assert not (ImmutableDict({1: 2}) == ImmutableDict({1: 3}))
    assert not (ImmutableDict({1: 2}) == {1: 2})
    assert not (ImmutableDict({1: 2}) == object())
    assert ImmutableDict({1: 2}) == ImmutableDict({1: 2})
    assert not (ImmutableDict({1: 2}) == MutableMapping({1: 2}))



# Generated at 2022-06-12 23:01:53.052584
# Unit test for function is_iterable
def test_is_iterable():

    assert(not is_iterable(False))
    assert(not is_iterable(42))
    assert(not is_iterable(None))
    assert(not is_iterable(Exception('testing')))
    assert(is_iterable(''))
    assert(is_iterable('abc'))
    assert(is_iterable([]))
    assert(is_iterable([1, 2, 3]))
    assert(is_iterable(tuple()))
    assert(is_iterable((1, 2, 3)))
    assert(is_iterable(set()))
    assert(is_iterable({1, 2, 3}))
    assert(is_iterable(xrange(3)))
    assert(is_iterable(dict()))

# Generated at 2022-06-12 23:02:00.539077
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({1, 2, 3})
    assert is_iterable({'a', 'b', 'c'})
    assert is_iterable(b'123')
    assert is_iterable(u'123')
    assert is_iterable(u'\u2713')
    assert is_iterable(set())
    assert not is_iterable(123)
    assert not is_iterable(1.23)
    assert not is_iterable(object())
    assert not is_iterable(None)


# Generated at 2022-06-12 23:02:09.753789
# Unit test for function is_iterable
def test_is_iterable():

    assert is_iterable([]) == True
    assert is_iterable([1, 2]) == True
    assert is_iterable("") == True
    assert is_iterable("ansible") == True
    assert is_iterable("") == True
    assert is_iterable("ansible") == True
    assert is_iterable("") == True
    assert is_iterable("ansible") == True
    assert is_iterable(5) == False
    assert is_iterable({'key': 'value'}) == True
    assert is_iterable(set(['foo'])) == True
    assert is_iterable(('foo')) == True
    assert is_iterable(frozenset(['foo'])) == True



# Generated at 2022-06-12 23:02:14.629109
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    u1 = ImmutableDict(a=1, b=2)
    u2 = ImmutableDict(a=1, b=22)
    u3 = ImmutableDict(a=1, b=2)

    assert u1 != u2
    assert u2 != u3
    assert u1 == u3

# Generated at 2022-06-12 23:02:23.980990
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})
    assert ImmutableDict({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert ImmutableDict({'a': 1, 'b': 2}) != {'a': 1, 'c': 2}
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 3})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 2, 'c': 3})

# Generated at 2022-06-12 23:02:33.812113
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})

    assert not ImmutableDict({'a': 1}) == ImmutableDict()
    assert not ImmutableDict() == ImmutableDict({'a': 1})

    assert not ImmutableDict({'a': 1}) == ImmutableDict({'a': 1, 'b': 2})
    assert not ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1})

    assert not ImmutableDict({'a': 1}) == ImmutableDict({'a': 2})

# Generated at 2022-06-12 23:02:38.927815
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable({})
    assert is_iterable(ImmutableDict())
    assert is_iterable('abc')
    assert not is_iterable(1)
    assert not is_iterable(False)
    assert not is_iterable(object())


# Generated at 2022-06-12 23:02:46.025623
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert not ImmutableDict({'a': 1}) == ImmutableDict({'a': 2})
    assert not ImmutableDict({'a': 1}) == ImmutableDict({'b': 1})
    assert not ImmutableDict({'a': 1}) == ImmutableDict({'a': 1, 'b': 2})
    assert not ImmutableDict({'a': 1}) == {'a': 1}


# Generated at 2022-06-12 23:02:48.666163
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(dict())
    assert is_iterable(list())
    assert is_iterable(tuple())
    assert is_iterable(set())
    assert is_iterable(1) is False
    assert is_iterable('foo') is False
    assert is_iterable(u'foo') is False


# Generated at 2022-06-12 23:03:56.850559
# Unit test for function is_iterable
def test_is_iterable():
    class Foo(object):
        def __iter__(self):
            pass

    assert is_iterable(Foo())
    assert is_iterable((1, 2))
    assert is_iterable(range(10))
    assert is_iterable({'1': 1})
    assert is_iterable(set())
    assert is_iterable(1) is False
    assert is_iterable(object()) is False
    assert is_iterable(None) is False
    assert is_iterable(type(None)) is False


# Generated at 2022-06-12 23:04:02.100352
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2])
    assert is_iterable((1, 2))
    assert is_iterable({1, 2})
    assert is_iterable({1: 'a', 2: 'b'})
    assert is_iterable('abc')
    assert is_iterable(b'abc')
    assert is_iterable((i for i in range(3)))
    assert is_iterable(enumerate(('a', 'b', 'c')))
    assert not is_iterable(None)
    assert not is_iterable(1)


# Generated at 2022-06-12 23:04:04.619121
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(dict(a=3, b=4)) == ImmutableDict(a=3, b=4)


# Generated at 2022-06-12 23:04:14.057107
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Both sides of equality are ImmutableDicts
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})

    # The left side of equality is an ImmutableDict, but the right side is not
    assert ImmutableDict({'a': 1, 'b': 2}) != {'a': 1, 'b': 2, 'c': 3}
    assert ImmutableDict({'a': 1, 'b': 2}) != MutableMapping({'a': 1, 'b': 2, 'c': 3})

    # The right side of equality is an ImmutableDict, but the left side is not

# Generated at 2022-06-12 23:04:19.031129
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=2, b=2)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=2)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=2, c=3)

# Generated at 2022-06-12 23:04:28.855914
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable({'key': 'value'}) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable(range(10)) is True
    assert is_iterable('abc') is True
    assert is_iterable(b'abc') is True
    assert is_iterable(1) is False
    assert is_iterable(None) is False

    # Test string-like types
    assert is_iterable('abc', include_strings=True) is True
    assert is_iterable(b'abc', include_strings=True) is True
    assert is_iterable([1, 2, 3], include_strings=True) is True

# Generated at 2022-06-12 23:04:38.592392
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from collections import OrderedDict, Mapping
    from random import randint

    # simple comparisons
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() == {}
    assert ImmutableDict() == OrderedDict()
    assert ImmutableDict() == Mapping()

    # basic comparisons different
    assert not ImmutableDict() == 4
    assert not ImmutableDict() == (1, 2)
    assert not ImmutableDict() == set([1, 2])

    # immutable dict vs dict
    assert ImmutableDict({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert ImmutableDict({'a': 1, 'b': 2}) == OrderedDict([('a', 1), ('b', 2)])
    assert ImmutableD

# Generated at 2022-06-12 23:04:42.063404
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable(range(0, 10))
    assert is_iterable('abc')
    assert is_iterable(b'abc')
    assert not is_iterable(1)
    assert not is_iterable(10.0)
    assert not is_iterable(None)


# Generated at 2022-06-12 23:04:49.781291
# Unit test for function is_iterable
def test_is_iterable():

    # Test non-iterables
    assert not is_iterable(object())
    assert not is_iterable(None)

    # Test strings
    assert not is_iterable('foo')
    assert is_iterable('foo', include_strings=True)
    assert is_iterable(u'foo', include_strings=True)

    # Test iterables (tuple, list, set, generator)
    assert is_iterable(tuple())
    assert is_iterable(tuple([1]))
    assert is_iterable(list())
    assert is_iterable(list([1]))
    assert is_iterable(set())
    assert is_iterable(set([1]))
    assert is_iterable((i for i in range(3)))



# Generated at 2022-06-12 23:04:57.134879
# Unit test for function is_iterable
def test_is_iterable():

    assert is_iterable([]) is True
    assert is_iterable([1,2,3]) is True
    assert is_iterable(([1,2,3])) is True
    assert is_iterable(set([1,2,3])) is True
    assert is_iterable({'k':'v'}) is True
    assert is_iterable('string') is True
    assert is_iterable(u'string') is True
    assert is_iterable(is_iterable) is True
    assert is_iterable(1) is False
    assert is_iterable(object()) is False
    assert is_iterable(None) is False

    assert is_iterable('string', include_strings=True) is True
    assert is_iterable(u'string', include_strings=True) is True
   