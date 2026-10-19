

# Generated at 2022-06-12 22:56:07.668537
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict().union({1: 2})
    b = ImmutableDict()
    b = b.union({1: 2})
    assert a.__eq__(b)
    assert not a.__eq__(None)
    assert not a.__eq__({1: 2})
    b = ImmutableDict()
    b = b.union({2: 1})
    assert not a.__eq__(b)


# Generated at 2022-06-12 22:56:12.603389
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test the method ImmutableDict.__eq__.

    This method compares if two ImmutableDict objects have the same items. This test checks
    several possible scenarios where two ImmutableDict objects have or have not the same items.
    """
    immutable_dict_1 = ImmutableDict({'key1': 1, 'key2': 2, 'key3': 3})
    immutable_dict_2 = ImmutableDict({'key1': 1, 'key2': 2})
    immutable_dict_3 = ImmutableDict({'key1': 1, 'key3': 3})
    immutable_dict_4 = ImmutableDict({'key2': 1, 'key1': 2})
    immutable_dict_5 = ImmutableDict({'key1': 1, 'key2': 2, 'key3': 3})
    immutable_dict

# Generated at 2022-06-12 22:56:22.768139
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test for method ImmutableDict.__eq__."""

    equal1 = ImmutableDict()
    equal2 = ImmutableDict()
    equal3 = ImmutableDict(a=1, b=2)
    equal4 = ImmutableDict(b=2, a=1)
    equal5 = ImmutableDict({'b': 2, 'a': 1})
    equal6 = ImmutableDict(**{'a': 1, 'b': 2})

    not_equal1 = ImmutableDict(b=2, a=1, c=3)
    not_equal2 = ImmutableDict(b=2, a=10)
    not_equal3 = ImmutableDict(a=1, b=2, c=None)

# Generated at 2022-06-12 22:56:28.110689
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = ImmutableDict({'a': 'a'})
    other_d = ImmutableDict({'a': 'b'})
    assert d == d
    assert d != other_d
    assert d != {'a': 'a'}
    # test another object of different type
    import collections
    assert d != collections.namedtuple('Dummy', 'a')('a')

# Generated at 2022-06-12 22:56:37.037310
# Unit test for function is_iterable
def test_is_iterable():
    from itertools import chain
    from .six import StringIO

    class TestClass:
        def __iter__(self):
            return chain([1, 2])

    class TestClass2:
        def __getitem__(self, idx):
            return idx

    assert is_iterable('abc'), 'Single string is iterable'
    assert is_iterable(['a', 'b', 'c']), 'List is iterable'
    assert is_iterable(('a', 'b', 'c')), 'Tuple is iterable'
    assert is_iterable(TestClass())
    assert is_iterable(TestClass2())
    assert not is_iterable(1), 'Single integer is not iterable'

# Generated at 2022-06-12 22:56:42.065935
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict = ImmutableDict({'a': 1, 'b': 3, 'c': 5})
    test_dict2 = ImmutableDict({'a': 1, 'b': 3, 'c': 5})
    test_dict3 = ImmutableDict({'a': 1, 'b': 3, 'c': 6})
    assert test_dict == test_dict2
    assert test_dict != test_dict3

# Generated at 2022-06-12 22:56:51.059017
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'x': 'A'})
    d2 = ImmutableDict({'x': 'A', 'y': 'B'})
    d3 = ImmutableDict({'x': 'A', 'y': 'B'})
    d4 = ImmutableDict({'x': 'A', 'y': 'Z'})
    d5 = {'x': 'A', 'y': 'B'}
    assert(d1 != d2)
    assert(d2 == d3)
    assert(d3 != d4)
    assert(d4 != d5)

# Generated at 2022-06-12 22:56:57.577530
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable('a')
    assert is_iterable(['a','b'])
    assert is_iterable((('a','b'),('c','d')))
    assert is_iterable('ab')
    assert is_iterable(['a','b'], include_strings=True)
    assert is_iterable((('a','b'),('c','d')), include_strings=True)
    assert is_iterable('ab', include_strings=True)


# Generated at 2022-06-12 22:57:02.600627
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    # Test 1:
    # method __eq__ returns True when __hash__ values of two ImmutableDicts are equal
    d1 = ImmutableDict({'key1': 'val1', 'key2': 'val2'})
    d2 = ImmutableDict({'key2': 'val2', 'key1': 'val1'})
    assert d1 == d2

    # Test 2:
    # method __eq__ returns True when __hash__ values of two ImmutableDicts are equal
    d1 = ImmutableDict({'key1': 'val1'})
    d2 = ImmutableDict({'key1': 'val1'})
    assert d1 == d2

    # Test 3:
    # method __eq__ returns True when __hash__ values of two ImmutableDicts are equal
    d1 = ImmutableD

# Generated at 2022-06-12 22:57:10.127409
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(1.0)
    assert not is_iterable(True)
    assert is_iterable([])
    assert is_iterable(()), 'Tuple is not iterable'
    assert is_iterable((x for x in range(3)))
    assert is_iterable(MutableMapping())
    assert is_iterable(ImmutableDict())


# Generated at 2022-06-12 22:57:21.403366
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(dict(x=None))
    d2 = ImmutableDict(dict(x=None))
    assert d1 == d2

    d1 = ImmutableDict(dict(x=None, y=None))
    d2 = ImmutableDict(dict(x=None, y=None))
    assert d1 == d2

    d1 = ImmutableDict(dict(x=None))
    d2 = ImmutableDict(dict(y=None))
    assert d1 != d2

    d1 = ImmutableDict(dict(x=None, y=None))
    d2 = ImmutableDict(dict())
    assert d1 != d2

    d1 = ImmutableDict(dict(x=None, y=None))

# Generated at 2022-06-12 22:57:24.185424
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1})
    d2 = ImmutableDict({'a': 1})
    assert d1 == d2


# Generated at 2022-06-12 22:57:34.495390
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Example data
    keys = ['a', 'b', 'c']
    values_1 = ['1', '2', '3']
    values_2 = ['5', '2', '3']

    # Equal dicts
    dict_1_1 = ImmutableDict(zip(keys, values_1))
    dict_1_2 = dict_1_1
    dict_1_3 = ImmutableDict(zip(keys, values_1))
    dict_1_4 = ImmutableDict(zip(keys, values_1))

    # Non equal dicts
    dict_2_1 = ImmutableDict(zip(keys, values_2))
    dict_2_2 = ImmutableDict(zip(keys, values_2))

    # Test equality inside the same group
    assert dict_1_1 == dict_1

# Generated at 2022-06-12 22:57:43.540651
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit tests for method __eq__ of class ImmutableDict.

    Verify that instances of ImmutableDict are considered equal if and only if their
    contents are the same.
    """
    test_cases = [
        ({}, {}),
        ({'a': 1}, {'a': 1}),
        ({'a': 1}, {'a': 1.0}),
        ({'a': 1, 'b': 2}, {'b': 2, 'a': 1}),
        ({'a': 1, 'b': 2}, {'a': 1}),
        ({}, {'a': 1}),
        ({'a': 1}, ImmutableDict({'a': 1})),
        ({'a': 1}, {'a': 1}),
    ]

# Generated at 2022-06-12 22:57:51.721362
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(u'foo') is False
    assert is_iterable(b'foo') is False
    assert is_iterable(b'foo', include_strings=True) is True
    assert is_iterable([]) is True
    assert is_iterable((1,)) is True
    assert is_iterable({'foo': 'bar'}) is True
    assert is_iterable({}) is True
    assert is_iterable(1) is False
    assert is_iterable(True) is False
    assert is_iterable(None) is False
    assert is_iterable(set()) is True
    assert is_iterable(frozenset()) is True

    class Iterable(object):
        def __iter__(self):
            return iter([])

    class NonIterable(object):
        pass

   

# Generated at 2022-06-12 22:57:56.663396
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('abc')
    assert is_iterable(u'abc')
    assert is_iterable([])
    assert is_iterable([1, 2])
    assert is_iterable(set())
    assert is_iterable(set([1, 2]))
    assert is_iterable({})
    assert is_iterable({'k': 'v'})



# Generated at 2022-06-12 22:58:05.499231
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Check that ImmutableDict does not recognize it as equal to equivalent dictionaries
    x1 = ImmutableDict({'a': 4, 'b': [1, 2, 3], 'c': 'd', 'e': {'f': 'g'}, 'h': '', 'i': None})
    x2 = ImmutableDict({'a': 4, 'b': [1, 2, 3], 'c': 'd', 'e': {'f': 'g'}, 'h': '', 'i': None})
    assert x1 != x2
    assert x1 != {'a': 4, 'b': [1, 2, 3], 'c': 'd', 'e': {'f': 'g'}, 'h': '', 'i': None}

    # Check that ImmutableDict does not recognize it as equal to equivalent dictionaries with

# Generated at 2022-06-12 22:58:13.418629
# Unit test for function is_iterable
def test_is_iterable():
    # Positive test cases
    positive_test_cases = [
        'test',
        5,
        ['test'],
        ('test1', 'test2'),
        {'test1': 5},
    ]
    for test_case in positive_test_cases:
        assert is_iterable(test_case) is True
    # Negative test cases
    negative_test_cases = [
        None,
        _is_iterable
    ]
    for test_case in negative_test_cases:
        assert is_iterable(test_case) is False


# Generated at 2022-06-12 22:58:18.946645
# Unit test for function is_iterable
def test_is_iterable():
    for item in [
        '',
        u'',
        b'',
        [],
        {},
        (),
        set()
    ]:
        assert is_iterable(item)

    for item in [
        None,
        1,
        2.73,
        True,
        False
    ]:
        assert not is_iterable(item)



# Generated at 2022-06-12 22:58:29.369873
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    idict0 = ImmutableDict({'a' : 1, 'b' : 2})
    idict1 = ImmutableDict({'a' : 1, 'b' : 2})
    idict2 = ImmutableDict({'a' : 0, 'b' : 2})
    idict3 = ImmutableDict({'a' : 1, 'b' : 2, 'c' : 1})
    idict4 = ImmutableDict({'a' : 1, 'c' : 1, 'b' : 2})

    assert idict0 == idict1
    assert idict0 == {'a' : 1, 'b' : 2}
    assert idict1 == idict0
    assert idict1 == {'a' : 1, 'b' : 2}
    assert idict0 != idict2

# Generated at 2022-06-12 22:58:43.152398
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a=1, b=2)
    d2 = ImmutableDict(a=1, b=2)
    d3 = ImmutableDict(a=1, b=3)
    d4 = {'a': 1, 'b': 2}

    assert d1 == d2
    assert not d1 == d3
    assert not d1 == d4
    assert not d1 == ('a', 1)
    assert not d1 == None



# Generated at 2022-06-12 22:58:53.313452
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(())
    assert is_iterable([])
    assert not is_iterable('')
    assert is_iterable(u'')
    assert not is_iterable(0)
    assert not is_iterable(False)
    assert not is_iterable(True)
    assert not is_iterable(None)
    assert not is_iterable({})
    assert not is_iterable(set())
    assert is_iterable((x for x in range(10)))
    assert is_iterable(range(10))
    assert is_iterable((x for x in range(10)))
    assert not is_iterable(__file__)
    assert is_iterable({'a': 'b'})
    assert is_iterable({'a': 'b'}.items())
    assert is_iter

# Generated at 2022-06-12 22:59:02.030726
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable({'1': '2'})
    assert is_iterable({'1': 2})

    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(1.0)

    assert not is_iterable('', False)
    assert is_iterable('', True)
    assert is_iterable(u'', True)



# Generated at 2022-06-12 22:59:11.983078
# Unit test for function is_iterable
def test_is_iterable():
    """Sanity check for function is_iterable"""
    class iterable(object):
        def __iter__(self):
            pass
    class sequence(object):
        def __getitem__(self):
            pass
    class sequence_iterable(object):
        def __iter__(self):
            pass
        def __getitem__(self):
            pass
    assert is_iterable([1,2,3])
    assert is_iterable(iterable())
    assert not is_iterable(sequence())
    assert is_iterable(sequence_iterable())

    # Non iterable objects should return False
    assert not is_iterable(3)
    assert not is_iterable('3')


# Generated at 2022-06-12 22:59:18.395138
# Unit test for function is_iterable
def test_is_iterable():
    '''Verify function is_iterable returns correct values for basic data types'''
    assert is_iterable([], False) is True
    assert is_iterable((), False) is True
    # assert is_iterable({}, False) is True

    assert is_iterable(set(), False) is True
    assert is_iterable(dict(), False) is True

    assert is_iterable(text_type, False) is False
    assert is_iterable(binary_type, False) is False
    assert is_iterable(int, False) is False
    assert is_iterable(float, False) is False
    assert is_iterable(bool, False) is False



# Generated at 2022-06-12 22:59:26.362328
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable((1, 2, 3))
    assert is_iterable({1: 2})
    assert is_iterable(set())
    assert not is_iterable(None)
    assert not is_iterable(1)  # even though int is iterable in python 3
    assert not is_iterable('foo')
    assert is_iterable('foo', include_strings=True)
    assert not is_iterable(b'foo')
    assert is_iterable(b'foo', include_strings=True)


# Generated at 2022-06-12 22:59:34.933086
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable({'a': 'b', 'c': 'd'})
    assert is_iterable(xrange(1, 4))
    assert is_iterable(ImmutableDict({'a': 'b', 'c': 'd'}))
    assert is_iterable('abc')
    assert not is_iterable(5)
    assert is_iterable(5, True)
    assert is_iterable(None, True)
    assert is_iterable(None)


# Generated at 2022-06-12 22:59:37.625941
# Unit test for function is_iterable
def test_is_iterable():
    class A(object):
        def __iter__(self):
            pass

    class B(object):
        pass

    assert is_iterable(A())
    assert not is_iterable(B())


# Generated at 2022-06-12 22:59:44.411694
# Unit test for function is_iterable
def test_is_iterable():
    test_cases = [
        (is_iterable('a'), False),
        (is_iterable(b'a'), False),
        (is_iterable(1), False),
        (is_iterable(['a']), True),
        (is_iterable(('a',)), True),
        (is_iterable(set('a')), True),
        (is_iterable({'a': 1}), True),
        (is_iterable(dict(a=1)), True)
    ]

    for test_case, expected_result in test_cases:
        assert test_case == expected_result, 'Call to is_iterable failed for test case: %s' % test_case


# Generated at 2022-06-12 22:59:52.400842
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import unittest
    class ImmutableDict__eq__Test(unittest.TestCase):
        """ImmutableDict.__eq__ tests"""

        def test_eq_hash_equal(self):
            self.assertTrue(ImmutableDict({'a': 1}) == ImmutableDict({'a': 1}))

        def test_eq_hash_not_equal(self):
            self.assertFalse(ImmutableDict({'a': 1}) == ImmutableDict({'a': 2}))

        def test_eq_no_hash(self):
            self.assertFalse(ImmutableDict({'a': 1}) == [])

    unittest.main(module='unit_test_ImmutableDict___eq__', exit=False)

# Generated at 2022-06-12 23:00:14.468458
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([True, False])
    assert is_iterable(x for x in [1, 2])
    assert is_iterable((t for t in [1, 1, 2]))
    assert is_iterable({'k1': 1, 'k2': 2})
    assert is_iterable(['test', 123])
    assert is_iterable(set(['a', 'b', 'c', 'a']))
    assert is_iterable(object())

    assert not is_iterable('test')
    assert not is_iterable(123)
    assert not is_iterable(None)



# Generated at 2022-06-12 23:00:20.141405
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable({'a': 'b', 'b': 'c'})
    assert is_iterable(StringEq('test'))
    assert is_iterable(set([5, 6, 7]))
    assert not is_iterable('abc')
    assert not is_iterable(123)
    assert not is_iterable(None)



# Generated at 2022-06-12 23:00:28.936526
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict({1: 2}) == ImmutableDict({1: 2})
    assert ImmutableDict({1: 2, 3: {4: 5}}) == ImmutableDict({1: 2, 3: {4: 5}})
    assert not ImmutableDict() == ImmutableDict({1: 2})
    assert not ImmutableDict({1: 2}) == ImmutableDict({2: 1})
    assert not ImmutableDict({1: 2}) == ImmutableDict({1: 2, 3: {4: 5}})
    assert not ImmutableDict({1: 2, 3: {4: 5}}) == ImmutableDict({1: 2})

# Generated at 2022-06-12 23:00:39.528327
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # test for class ImmutableDict with it self
    # test for class ImmutableDict with a dict
    data1 = {'a': 1, 'b': 2}
    data2 = {'a': 1, 'b': 2}
    data3 = {'a': 1, 'b': 3}
    dict1 = ImmutableDict(data1)
    dict2 = ImmutableDict(data2)
    dict3 = ImmutableDict(data3)
    # test for a dict with a dict
    assert data1 == data2
    assert data1 != data3
    # test for a dict with a ImmutableDict
    assert data1 == dict2
    assert data1 != dict3

    # test for class ImmutableDict with it self
    assert dict1 == dict2
    assert dict1 != dict3

    #

# Generated at 2022-06-12 23:00:44.872581
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict(a=1) == ImmutableDict(a=1)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1)
    assert ImmutableDict(a=1) != ImmutableDict(a=2)
    assert ImmutableDict(a=1) != {'a': 1}



# Generated at 2022-06-12 23:00:49.071238
# Unit test for function is_iterable
def test_is_iterable():
    foo = "foo bar"
    assert is_iterable(foo) is True
    assert is_iterable(foo, include_strings=True) is True
    assert is_iterable(foo, include_strings=False) is False


# Generated at 2022-06-12 23:00:58.953590
# Unit test for function is_iterable
def test_is_iterable():
    class Foo(object):
        pass

    f = Foo()
    assert is_iterable('foo')
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable({'one': 1, 'two': 2})
    assert is_iterable(f)
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert not is_iterable(False)
    assert not is_iterable(True)
    assert not is_iterable(1.1)
    assert not is_iterable(1 + 2j)



# Generated at 2022-06-12 23:01:05.847831
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 0, 'b': 1, 'c': 2})
    d2 = ImmutableDict({'a': 0, 'b': 1, 'c': 2})
    d3 = {'a': 0, 'b': 1, 'c': 2}
    d4 = ImmutableDict({'a': 0, 'b': 1, 'c': 3})
    assert d1 == d2
    assert d1 != d3
    assert d3 != d1
    assert d1 != d4
    assert d3 != d4


# Generated at 2022-06-12 23:01:10.393764
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a=1, b=2, c=3)
    d2 = ImmutableDict(a=1, b=2, c=3)
    assert d1 == d2
    d3 = ImmutableDict(a=1, b=2, c=4)
    assert d1 != d3


# Generated at 2022-06-12 23:01:20.801307
# Unit test for function is_iterable
def test_is_iterable():
    iterable_list = ['a', 'b', 'c']
    iterable_dict = {'a': 1, 'b': 2}
    iterable_tuple = ('a', 'b', 'c')
    iterable_string = 'abc'
    iterable_bytes = b'abc'
    iterable_set = set(['a', 'b', 'c'])
    iterable_frozenset = frozenset(['a', 'b', 'c'])
    non_iterable_string = 'abc'
    non_iterable_int = 123
    non_iterable_boolean = True

    assert is_iterable(iterable_list)
    assert is_iterable(iterable_dict)
    assert is_iterable(iterable_tuple)

# Generated at 2022-06-12 23:01:51.022422
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2})
    b = ImmutableDict({'a': 1, 'b': 2})

    assert a == b



# Generated at 2022-06-12 23:02:00.122355
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Unit test for class method __eq__ of class ImmutableDict

    This is not a real unit test, this test is only run if this module
    is called as a script.

    Expected Results:
    - two ImmutableDicts with the same key-value pairs are equal to each other
    - two ImmutableDicts with different key-value pairs are not equal to each other
    - a ImmutableDict is not equal to a dict
    - a ImmutableDict is not equal to a list
    - a ImmutableDict is not equal to a string
    - a ImmutableDict is not equal to any other thing that cannot be hashed
    """

    d1 = ImmutableDict(a=1, b=2, c=3)
    d2 = ImmutableDict(a=1, b=2, c=3)

# Generated at 2022-06-12 23:02:10.182701
# Unit test for function is_iterable
def test_is_iterable():
    ansible_string = 'This is a string'
    ansible_bytes = b'This is bytes'
    ansible_list = [1, 2, 3, 4]
    ansible_set = set([1, 2, 3, 4])
    ansible_tuple = (1, 2, 3, 4)
    ansible_dict = {'a': 1, 'b': 2, 'c': 3}
    ansible_iter = iter(ansible_list)
    assert is_iterable(ansible_string) is True
    assert is_iterable(ansible_bytes) is True
    assert is_iterable(ansible_list) is True
    assert is_iterable(ansible_tuple) is True
    assert is_iterable(ansible_set) is True

# Generated at 2022-06-12 23:02:21.278155
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable({1, 2, 3})
    assert is_iterable(iter([]))
    assert is_iterable(iter(()))
    assert is_iterable(iter({}))
    assert is_iterable(iter({1, 2, 3}))
    assert is_iterable(xrange(10))
    assert is_iterable(text_type())
    assert is_iterable(set())
    assert is_iterable(frozenset())

    assert not is_iterable(text_type(''))
    assert not is_iterable(binary_type(b''))
    assert not is_iterable(10)
    assert not is_iterable(3.14)

# Generated at 2022-06-12 23:02:31.838743
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a':'1', 'b':'2', 'c':'3'}) == ImmutableDict({'a':'1', 'b':'2', 'c':'3'})
    assert ImmutableDict({'a':'1', 'b':'2', 'c':'3'}) == {'a':'1', 'b':'2', 'c':'3'}
    assert not ImmutableDict({'a':'1', 'b':'2', 'c':'3'}) == ImmutableDict({'a':'1', 'b':'2', 'd':'3'})
    assert not ImmutableDict({'a':'1', 'b':'2', 'c':'3'}) == 'foobar'

# Generated at 2022-06-12 23:02:41.881231
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    original = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    equal = ImmutableDict({'key1': 'value1', 'key2': 'value2'})
    not_equal1 = ImmutableDict({'key1': 'value1'})
    not_equal2 = ImmutableDict({'key2': 'value2'})
    not_equal3 = ImmutableDict({'key3': 'value3'})

    # __eq__ should return False when comparing to None
    assert not original.__eq__(None)

    # __eq__ should return False when comparing to a dict
    assert not original.__eq__({'key1': 'value1', 'key2': 'value2'})

    # __eq__ should return False when comparing to self

# Generated at 2022-06-12 23:02:51.180991
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2, c=3) == ImmutableDict(a=1, b=2, c=3)
    assert ImmutableDict(a=1, b=2, c=3) != ImmutableDict(a=1, b=2, c=4)
    assert ImmutableDict(a=1, b=2, c=3) != ImmutableDict(a=1, b=2)
    assert ImmutableDict(a=1, b=2, c=3) != ImmutableDict(a=1, b=2, c=3, d=4)

# Generated at 2022-06-12 23:02:56.713052
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test equality of ImmutableDict objects
    """
    assert(ImmutableDict({'a': 2}) == ImmutableDict({'a': 2}))
    assert(ImmutableDict({'a': 2, 'b': 3}) == ImmutableDict({'b': 3, 'a': 2}))
    assert(not ImmutableDict({'a': 2}) == ImmutableDict({'b': 2}))


# Generated at 2022-06-12 23:03:06.963769
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test __eq__ of ImmutableDict"""
    # Trying to compare two ImmutableDict objects with same key/value pairs
    # and ensure that it returns True as expected
    first_object = ImmutableDict({'a': 1, 'b': 2, 'c': 'x'})
    second_object = ImmutableDict({'a': 1, 'b': 2, 'c': 'x'})
    assert first_object == second_object

    # Trying to compare two ImmutableDict objects with different key/value pairs
    # and ensure that it returns False as expected
    first_object = ImmutableDict({'a': 1, 'b': 2, 'c': 'x'})
    second_object = ImmutableDict({'a': 1, 'b': 2, 'c': 'y'})

# Generated at 2022-06-12 23:03:15.617124
# Unit test for function is_iterable
def test_is_iterable():
    def func():
        pass

    my_dict = {'a': 1}
    my_set = set([1, 2, 3])
    my_tuple = (1, 2, 3)
    my_str = 'str'
    my_int = 1
    my_float = 1.0
    my_list = [1, 2, 3]
    my_class_instance = MyClass()
    my_generator = (x for x in range(3))

    assert is_iterable(func) == False
    assert is_iterable(my_dict) == True
    assert is_iterable(my_set) == True
    assert is_iterable(my_tuple) == True
    assert is_iterable(my_str) == True
    assert is_iterable(my_int) == False

# Generated at 2022-06-12 23:04:18.776700
# Unit test for function is_iterable
def test_is_iterable():
    # Test 1: empty strings and bytes
    assert is_iterable(b'')
    assert is_iterable('')
    assert is_iterable(u'')
    assert not is_iterable(b'', include_strings=True)
    assert not is_iterable('', include_strings=True)
    assert not is_iterable(u'', include_strings=True)

    # Test 2: non-empty strings and bytes
    assert is_iterable(b'abc')
    assert is_iterable(u'abc')
    assert is_iterable('abc')
    assert not is_iterable(b'abc', include_strings=True)
    assert not is_iterable(u'abc', include_strings=True)
    assert not is_iterable('abc', include_strings=True)

    # Test 3

# Generated at 2022-06-12 23:04:28.358327
# Unit test for method __eq__ of class ImmutableDict

# Generated at 2022-06-12 23:04:30.599153
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(dict(a=1, b=2)) == ImmutableDict(dict(a=1, b=2))



# Generated at 2022-06-12 23:04:40.014881
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = dict(a=1, b=2)
    dict2 = dict(a=1, b=3)
    dict3 = dict(a=1, b=2, c=3)

    immutable_dict1 = ImmutableDict(a=1, b=2)
    immutable_dict2 = ImmutableDict(a=1, b=3)
    immutable_dict3 = ImmutableDict(a=1, b=2, c=3)

    dict1_mutable_copy = dict1.copy()
    dict2_mutable_copy = dict2.copy()
    dict3_mutable_copy = dict3.copy()

    # Comparing ImmutableDict with ImmutableDict
    assert immutable_dict1 == immutable_dict1
    assert immutable_dict1 != immutable_dict2
    assert immutable

# Generated at 2022-06-12 23:04:48.436548
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils.basic import jsonify
    a = ImmutableDict(a=1, b=2, c=3)
    b = ImmutableDict(a=1, b=2, c=3)
    c = ImmutableDict(a=1, b=2, c=3)

    # test equality with other ImmutableDict
    assert a == b
    assert a == c
    assert a.__eq__(b)

    # test equality with a dict
    assert a == a._store
    assert a.__eq__(a._store)

    # test non-equality with a tuple
    assert not a == (1, 2, 3)

    # test non-equality with a non-existent item
    assert not a == 'b'

    # test str to ImmutableDict equality

# Generated at 2022-06-12 23:04:56.113954
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable({'a': 1, 'b': 2}) is True
    assert is_iterable({1: 'a', 2: 'b'}) is True

    assert is_iterable('abc') is False
    assert is_iterable('abc'.encode('utf-8')) is False
    assert is_iterable(1) is False
    assert is_iterable(b'abc') is False

    assert is_iterable([1, 2, 3], include_strings=True) is True
    assert is_iterable((1, 2, 3), include_strings=True) is True
    assert is_iter

# Generated at 2022-06-12 23:04:59.713374
# Unit test for function is_iterable
def test_is_iterable():
    assert(is_iterable('abcdef'))
    assert(is_iterable([1, 2, 3]))
    assert(is_iterable((1, 2, 3)))
    assert(is_iterable({1: 2, 3: 4}))
    assert(is_iterable({1, 2, 3}))
    assert(is_iterable(1))
    assert(is_iterable(range(10)))
    assert(is_iterable(ImmutableDict()))
    assert(is_iterable(xrange(10)))
    assert(is_iterable(set()))
    assert(not is_iterable(None))



# Generated at 2022-06-12 23:05:09.916333
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test equality
    id_dict = ImmutableDict(dict(a='1', b='2', c='3'))
    id_dict2 = ImmutableDict(a='1', b='2', c='3')
    id_dict3 = ImmutableDict({'a': '1', 'b': '2', 'c': '3'})
    id_dict4 = ImmutableDict(a='3', b='2', c='1')
    assert id_dict == id_dict2
    assert id_dict2 == id_dict3
    assert id_dict == id_dict3
    assert id_dict2 == id_dict
    assert not id_dict == id_dict4
    assert not id_dict == [1, 2, 3]
    assert not id_dict == 1
    assert not id_dict == dict

# Generated at 2022-06-12 23:05:15.104708
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    d3 = ImmutableDict({'b': 2, 'a': 1})

    assert d1 == d1
    assert d1 == d2
    assert d2 == d1
    assert d1 == d3
    assert d2 == d3
    assert d3 == d1
    assert d3 == d2

# Generated at 2022-06-12 23:05:19.065302
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(text_type())
    assert is_iterable(binary_type())
    assert is_iterable(tuple())
    assert is_iterable(list())
    assert is_iterable(dict())
    assert is_iterable(set())
    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(1.2)
    assert not is_iterable(True)
