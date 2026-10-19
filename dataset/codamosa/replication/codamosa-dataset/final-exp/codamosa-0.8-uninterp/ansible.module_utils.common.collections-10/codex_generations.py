

# Generated at 2022-06-12 22:56:08.136370
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    """Unit test for ImmutableDict.difference(subtractive_iterable)"""
    original_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    arg_removal_keys = ['b', 'c']

    calculated_dict = original_dict.difference(arg_removal_keys)

    expected_keys = frozenset(['a'])
    calculated_keys = frozenset(calculated_dict.keys())

    assert expected_keys == calculated_keys



# Generated at 2022-06-12 22:56:11.247245
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    test_dict = ImmutableDict({'one': 1, 'two': 2, 'three': 3})
    test_keys = ['one', 'three']
    expected_dict = ImmutableDict({'two': 2})
    actual_dict = test_dict.difference(test_keys)
    assert actual_dict == expected_dict

# Generated at 2022-06-12 22:56:21.095053
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    d1 = ImmutableDict(foo="bar")
    assert d1.difference("foo") == ImmutableDict()

    d2 = ImmutableDict(foo="bar", bar="baz")
    assert d2.difference("foo") == ImmutableDict(bar="baz")
    assert d2.difference("foo").difference("bar") == ImmutableDict()
    assert d2.difference("bar").difference("foo") == ImmutableDict()

    d3 = ImmutableDict(foo="bar", bar="baz", baz="foo")
    assert d3.difference("bar") == ImmutableDict(foo="bar", baz="foo")
    assert d3.difference("baz") == ImmutableDict(foo="bar", bar="baz")
    assert d3.diff

# Generated at 2022-06-12 22:56:27.428598
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = a.difference({'a'})
    assert b == {'b': 2, 'c': 3}
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = a.difference(['b', 'c'])
    assert b == {'a': 1}

# Generated at 2022-06-12 22:56:28.642710
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    immutable = ImmutableDict({'a': 1, 'b': 2})
    assert immutable.difference(['b']) == ImmutableDict({'a': 1})

# Generated at 2022-06-12 22:56:35.715829
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2})

    assert a == a
    assert a == {'a': 1, 'b': 2}
    assert a == ImmutableDict({'a': 1, 'b': 2})

    assert a != {'a': 1}
    assert a != {'a': 1, 'b': 2, 'c': 3}
    assert a != ImmutableDict({'a': 1, 'b': 3})
    assert a != [1, 2]
    assert a != 'abc'

# Test for ImmutableDict.union

# Generated at 2022-06-12 22:56:40.054427
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable(range(3))
    assert is_iterable((1, 2, 3))
    assert is_iterable(1) is False
    assert is_iterable('abc') is False
    assert is_iterable(b'abc') is False
    assert is_iterable({1, 2, 3, 'a'}) is False



# Generated at 2022-06-12 22:56:44.640374
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict(k1='v1', k2='v2', k3='v3', k4='v4')
    expected = ImmutableDict(k1='v1', k4='v4')
    result = original.difference(['k2', 'k3'])
    assert result == expected

# Generated at 2022-06-12 22:56:55.637857
# Unit test for function is_iterable
def test_is_iterable():
    """Test function is_iterable"""

    # Test iterable
    iterable = ['a', 'b', 'c']
    assert is_iterable(iterable)
    iterable = ('a', 'b', 'c', 'd')
    assert is_iterable(iterable)
    iterable = {'a': 1, 'b': 2, 'c': 3}
    assert is_iterable(iterable)

    # Test non iterable
    non_iterable = 1
    assert not is_iterable(non_iterable)

    # Test string
    str_test = 'abc'
    assert not is_iterable(str_test)
    str_test = b'abc'
    assert not is_iterable(str_test)

    # Test string with include_strings=True
    str_test = 'abc'

# Generated at 2022-06-12 22:56:59.519160
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    A = ImmutableDict(a=1, b=2, c=3)
    B = A.difference([])
    C = A.difference(['b'])
    D = A.difference(['c', 'a'])
    E = A.difference(['c', 'a', 'z'])
    assert A == B
    assert C == ImmutableDict(a=1, c=3)
    assert D == ImmutableDict(b=2)
    assert E == ImmutableDict(b=2)


# Generated at 2022-06-12 22:57:13.139926
# Unit test for function is_iterable
def test_is_iterable():
    class DummyList(list):
        pass

    class DummyA(object):
        __len__ = None

        def __iter__(self):
            return iter([1, 2, 3])

    class DummyD(dict):
        pass

    class DummyT(tuple):
        pass

    assert is_iterable([]) is True
    assert is_iterable(dict()) is True
    assert is_iterable((x for x in range(0, 10))) is True
    assert is_iterable(DummyList()) is True
    assert is_iterable(DummyA()) is True
    assert is_iterable(DummyD()) is True
    assert is_iterable(DummyT()) is True
    assert is_iterable('xxx') is True
    assert is_iterable(1) is False

# Generated at 2022-06-12 22:57:20.659150
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(ImmutableDict())

    assert is_iterable('abc')
    assert is_iterable(bytearray(b'abc'))

    assert is_iterable('abc', include_strings=True)
    assert is_iterable(bytearray(b'abc'), include_strings=True)

    # Sequence doesn't count
    assert not is_iterable(range(10))

    # String doesn't count by default
    assert not is_iterable(b'abc')

    # String doesn't count
    assert not is_iterable(u'abc')

    # String counts if explicitly requested
    assert is_iterable(u'abc', include_strings=True)

    # Bytearray counts
    assert is_

# Generated at 2022-06-12 22:57:29.688102
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable({'a': 1, 'b': 2}) is True
    assert is_iterable({1, 2, 3}) is True
    assert is_iterable(tuple([1, 2, 3])) is True
    assert is_iterable(((i for i in [1, 2, 3]))) is True
    assert is_iterable('hello') is True
    assert is_iterable(b'hello') is True

    assert is_iterable(1) is False
    assert is_iterable(True) is False
    assert is_iterable(None) is False



# Generated at 2022-06-12 22:57:39.438153
# Unit test for function is_iterable
def test_is_iterable():
    def isiterable():
        for x in (2, 'abc', [1, 2, 3], {'a', 'b', 'c'}, (1, 2), {'a': 1, 'b': 2},
                  frozenset({'d', 'e', 'f'}), set({1, 2}), ImmutableDict({4: 'a'}),
                  MutableMapping(), u'można', u'нельзя', b'\xcf\xd0\xd1\xd2', u'일본어'):
            yield x, is_iterable(x, include_strings=True)
            if not isinstance(x, (text_type, binary_type)):
                yield x, is_iterable(x)


# Generated at 2022-06-12 22:57:47.939497
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # case: both dicts are the same
    original_dict = ImmutableDict({'a': '1', 'b': '2'})
    other_dict = original_dict
    assert original_dict == ImmutableDict(original_dict)
    assert original_dict == original_dict
    assert original_dict == other_dict
    assert other_dict == original_dict
    # case: the dicts have the same keys and values, but different class
    normal_dict = dict(original_dict)
    assert original_dict == normal_dict
    assert normal_dict == original_dict
    # case: different dicts
    assert not original_dict == ImmutableDict({'a': '1', 'b': '4'})

# Generated at 2022-06-12 22:57:57.890351
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict(foo=1) == ImmutableDict(foo=1)
    assert ImmutableDict(foo=1) == ImmutableDict(foo=1, bar=2)
    assert ImmutableDict(foo=1) != ImmutableDict(foo=2)
    assert ImmutableDict(foo=1) != ImmutableDict(foo=1, bar=2, baz=3)
    assert ImmutableDict(foo=1) != ImmutableDict(foo=1, bar=[], baz=3)
    assert ImmutableDict(foo=[1, 2, 3]) != ImmutableDict(foo=[1, 2, 3])
    assert ImmutableDict(foo=1) != ImmutableDict(bar=1)

# Generated at 2022-06-12 22:58:06.318242
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.common._collections_compat import Mapping, MutableMapping, Sequence

    # Create a test ImmutableDict
    test_dict = ImmutableDict({'foo': 'bar', 'nested': {1: 'one', 2: 'two'}})

    # Test equality comparison to other ImmutableDicts
    assert test_dict == ImmutableDict({'foo': 'bar', 'nested': {1: 'one', 2: 'two'}})
    assert test_dict != ImmutableDict({'foo': 'bar', 'nested': {1: 'one', 2: 'two', 3: 'three'}})

# Generated at 2022-06-12 22:58:15.352704
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    ad = ImmutableDict(a=1)
    bd = ImmutableDict(b=2)
    cd1 = ImmutableDict(a=1, b=2)
    cd2 = ImmutableDict(b=2, a=1)
    assert ad != bd
    assert ad == ad
    assert bd == bd
    assert cd1 == cd2
    assert cd1 == {'a':1, 'b':2}
    assert cd1 != {'a':1}
    assert cd1 != {'a':1, 'b':2, 'c':3}
    assert cd1 != 'a'

# Generated at 2022-06-12 22:58:26.452542
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict(a=1, b=2) == {'a': 1, 'b': 2}
    assert ImmutableDict(a=1, b=2) == {'b': 2, 'a': 1}

    assert ImmutableDict(a=1, b=2) != {'b': 2, 'a': 3}
    assert ImmutableDict(a=1, b=2) != ImmutableDict(b=4, a=1)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(b=2)
    assert ImmutableDict(a=1, b=2) != ImmutableDict()



# Generated at 2022-06-12 22:58:34.314037
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils import collections
    import types
    a = collections.ImmutableDict({1:2, 3:4})
    assert(a == a)
    assert(not (a == types.NoneType()))
    assert(not (a == 1))
    assert(not (a == '1'))
    assert(not (a == {'1':2}))
    assert(a == collections.ImmutableDict({1:2, 3:4}))
    assert(a != collections.ImmutableDict({1:2, 3:5}))
    assert(a != collections.ImmutableDict({1:2, 3:4, 5:6}))
    assert(a != collections.ImmutableDict({1:2}))

# Generated at 2022-06-12 22:58:46.429676
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(1) is False
    assert is_iterable('string') is True
    assert is_iterable('string', include_strings=False) is False
    assert is_iterable('string', include_strings=True) is True
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable(range(3)) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable(dict({'a': 1, 'b': 2, 'c': 3})) is True


# Generated at 2022-06-12 22:58:55.555935
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict(a=1, b=2) == dict(b=2, a=1)
    assert ImmutableDict(a=1, b=2) == {'a': 1, 'b': 2}
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=3)
    assert not ImmutableDict(a=1, b=2) == ImmutableDict(a=1)
    assert not ImmutableDict(a=1, b=2) == {'a': 1}
    assert not ImmutableDict(a=1, b=2) == object()

# Generated at 2022-06-12 22:59:07.442408
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable"""
    assert is_iterable(list())
    assert is_iterable((x for x in range(0)))
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable([1, 2, 3, 4])
    assert is_iterable((1, 2, 3, 4))
    assert is_iterable({1, 2, 3, 4})
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable(iter([1, 2, 3, 4]))
    assert is_iterable(range(0))

    assert not is_iterable(object())
    assert not is_iterable(1)
    assert not is_iterable(1.0)

# Generated at 2022-06-12 22:59:16.402543
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test 1: Both ImmutableDicts are empty
    assert ImmutableDict() == ImmutableDict()

    # Test 2: Both ImmutableDicts are not empty and identical
    d = ImmutableDict({'a': 'b'})
    assert d == ImmutableDict({'a': 'b'})

    # Test 3: Both ImmutableDicts are not empty and different
    assert d != ImmutableDict({'a': 'c'})

    # Test 4: Both ImmutableDicts are not empty and have different number of elements
    assert d != ImmutableDict({'a': 'b', 'c': 'd'})

    # Test 5: Both ImmutableDicts are not empty and have the same number of elements but different values
    assert d != ImmutableDict({'a': 'b', 'e': 'f'})



# Generated at 2022-06-12 22:59:27.062051
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'foo': 'bar'}) == ImmutableDict({'foo': 'bar'})
    assert ImmutableDict({'foo': 'bar'}).__eq__({'foo': 'bar'}) is False
    assert ImmutableDict({'foo': 'bar'}) == {'foo': 'bar'}
    assert ImmutableDict({'foo': 'bar'}).__eq__({'foo': 'foo'}) is False
    assert ImmutableDict({'foo': 'bar'}) == ImmutableDict({'foo': 'foo'}) is False
    assert ImmutableDict({'foo': 'bar'}) == 'foobar' is False
    assert ImmutableDict({'foo': 'bar'}) == ['foo', 'bar'] is False

# Generated at 2022-06-12 22:59:37.324409
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict([('1', 'one'), ('2', 'two'), ('3', 'three')]) == ImmutableDict([('1', 'one'), ('2', 'two'), ('3', 'three')])
    assert ImmutableDict([('1', 'one'), ('2', 'two'), ('3', 'three')]) == ImmutableDict([('3', 'three'), ('1', 'one'), ('2', 'two')])
    assert ImmutableDict([('1', 'one'), ('2', 'two'), ('3', 'three')]) != ImmutableDict([('1', 'one'), ('2', 'two'), ('4', 'four')])

# Generated at 2022-06-12 22:59:44.985315
# Unit test for function is_iterable
def test_is_iterable():
    # Check a few non-iterable types
    assert not is_iterable(None)
    assert not is_iterable(42)
    assert not is_iterable(object)

    # Check a few iterable types
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set([]))
    assert is_iterable((i for i in range(10)))
    assert is_iterable(range(10))

    # Check a few iterable strings
    assert is_iterable(u'')
    assert is_iterable(u'abc')
    assert is_iterable(b'abc')

    # Check the exclude_strings flag
    assert not is_iterable(u'', include_strings=False)

# Generated at 2022-06-12 22:59:54.023164
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils.common._collections_compat import MutableMapping
    from os.path import join, dirname

    test_scenarios = ImmutableDict(join(dirname(__file__), '..', '..', 'unit', 'ansible_collections', 'tests', 'unit', 'utils', 'immutable_dict_equality_test.yml'))
    for case in test_scenarios.values():
        with case:
            dict_a = ImmutableDict(case.get('dict_a'))
            dict_b = ImmutableDict(case.get('dict_b'))
            result = case.get('result')
            assert dict_a == dict_b is result
            assert dict_a != dict_b is not result


# Generated at 2022-06-12 22:59:57.532091
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert not is_iterable('foo')
    assert is_iterable('foo', True)
    assert is_iterable(b'foo', True)



# Generated at 2022-06-12 23:00:03.550853
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test two empty dictionaries
    a = ImmutableDict()
    b = ImmutableDict()
    if a != b:
        raise Exception('Empty dictionaries are not equal.')

    # Test two dictionaries with the same content
    a = ImmutableDict({ 'a': 1, 'b': 2 })
    b = ImmutableDict({ 'b': 2, 'a': 1 })
    if a != b:
        raise Exception('Dictionaries containing the same content are not equal.')

    # Test two dictionaries with different content
    c = ImmutableDict({ 'a': 1, 'c': 3 })
    if a == c:
        raise Exception('Dictionaries containing different content are equal.')


# Generated at 2022-06-12 23:00:14.417850
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable({})
    assert is_iterable(dict())

    assert not is_iterable(5)
    assert not is_iterable("")



# Generated at 2022-06-12 23:00:20.098748
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(a=1, b=2)
    b = ImmutableDict(a=1, b=2)
    c = ImmutableDict(b=2, a=1)
    assert(a.__eq__(b))
    assert(b != c)
    assert(not a.__eq__(c))
    assert(not a.__eq__(dict(a=1, b=2)))

# Generated at 2022-06-12 23:00:28.940658
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""
    a = ImmutableDict({'a': 'same_a', 'b': 'different_b', 'c': 'exists_c'})
    b = ImmutableDict({'a': 'same_a', 'b': 'different_b', 'c': 'exists_c'})
    # the dictionaries are the same, so a == b should return True
    assert a == b
    # the dictionaries compare equal, so a != b should return False
    assert not (a != b)
    # the dictionaries are different, so a != b should return True
    assert a != {'a': 'same_a', 'b': 'different_b', 'c': 'exists_c'}
    b = 'no good'
    # the dictionaries are different,

# Generated at 2022-06-12 23:00:39.528451
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Check correctness of __eq__ method of class ImmutableDict
    """
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() == dict()
    assert not ImmutableDict() == 1
    assert not ImmutableDict() == []
    assert not ImmutableDict() == {}
    assert ImmutableDict({'key1': 'value1', 'key2': 1}) == ImmutableDict({'key1': 'value1', 'key2': 1})
    assert ImmutableDict({'key1': 'value1', 'key2': 1}) == dict({'key1': 'value1', 'key2': 1})

# Generated at 2022-06-12 23:00:50.241342
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id1 = ImmutableDict({'a': 1, 'b': 2})
    id2 = ImmutableDict({'b': 2, 'a': 1})
    id3_list = ImmutableDict({'a': 2, 'b': 2})
    id4_list = ImmutableDict({'b': 3, 'a': 1})
    # Test same object is equal
    assert id1.__eq__(id1)

    # Test equal dictionaries are equal
    assert id1.__eq__(id2)

    # Test different types are not equal
    assert not id1.__eq__('somedifferenttype')

    # Test unequal dictionaries are not equal
    assert not id1.__eq__(id3_list)
    assert not id1.__eq__(id4_list)

# Generated at 2022-06-12 23:00:56.779972
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(a=1, b=2)
    b = ImmutableDict(a=1, b=2)
    c = ImmutableDict(a=1, b=2)
    d = ImmutableDict(b=2, a=1)
    e = ImmutableDict(a=2, b=3)
    f = 1
    assert a == b == c == d
    assert a != e != f


# Generated at 2022-06-12 23:01:04.422791
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({'one': 1, 'two': 2})
    assert not is_iterable(1)
    # test string
    assert is_iterable('One', include_strings=True)
    assert not is_iterable('One')
    # test non-indexable things
    assert not is_iterable(set([1, 2, 3]))
    assert not is_iterable(range(1, 6))


# Generated at 2022-06-12 23:01:11.357943
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    seq_a = []
    seq_b = ['a', 'b', 'c']
    seq_c = ['a', 'b', 'c']
    seq_d = ['a', 'b', 'c', 'd']

    imm_a = ImmutableDict()
    imm_b = ImmutableDict(a='1', b='2', c='3')
    imm_c = ImmutableDict(a='1', b='2', c='3')
    imm_d = ImmutableDict(a='1', b='2', c='3', d='4')

    assert not(imm_a.__eq__(seq_a))
    assert not(imm_a.__eq__(seq_b))
    assert not(imm_a.__eq__(imm_b))


# Generated at 2022-06-12 23:01:16.106631
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable('')

    assert not is_iterable(1)
    assert not is_iterable(None)

    class Test:
        pass
    assert not is_iterable(Test())



# Generated at 2022-06-12 23:01:21.589416
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() != {"a": "b"}
    assert ImmutableDict() != ImmutableDict(a="b")
    assert ImmutableDict(a="b") == ImmutableDict(a="b")
    assert ImmutableDict(a="b", c="d") == ImmutableDict(c="d", a="b")

# Generated at 2022-06-12 23:01:44.525789
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Positive cases
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict(a=1) == ImmutableDict(a=1)
    assert ImmutableDict() == dict()
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'b': 2}) == ImmutableDict({'b': 2})

    # Negative cases
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=2, c=3)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=2, b=2)


# Generated at 2022-06-12 23:01:48.397659
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2})
    a2 = ImmutableDict({'a': 1, 'b': 2})
    b = ImmutableDict({'b': 2})

    assert a.__eq__(a2)
    assert not a.__eq__(b)
    assert not a.__eq__({'a': 1, 'b': 2})


# Generated at 2022-06-12 23:01:54.370233
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(x=1, y=2, z=3)
    b = ImmutableDict(x=1, y=2, z=3)
    # same hash should imply equality
    assert a.__hash__() == b.__hash__()
    assert a == b
    c = ImmutableDict(x=1, y=2, z=4)
    # different hash should imply inequality
    assert not a.__hash__() == c.__hash__()
    assert a != c

# Generated at 2022-06-12 23:02:02.669418
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1}) == {'a': 1}
    assert ImmutableDict({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})
    assert ImmutableDict({'a': 1, 'b': 2}) != {'a': 1}
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({1: 1})
    assert ImmutableDict({'a': '1', 'b': '2'}) != {'a': 1, 'b': 2}
    assert ImmutableDict({'a': 1, 'b': 1}) != {'a': 1, 'b': 2}

# Generated at 2022-06-12 23:02:12.378366
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(first='first', second='second', third='third')
    d2 = ImmutableDict(first='first', second='second', third='third')
    d3 = ImmutableDict(first='first', second='second', third='third', fourth='fourth')
    assert d1 == d2
    assert not d1 == d3
    assert not d1 == {'first': 'first', 'second': 'second', 'third': 'third', 'fourth': 'fourth'}
    assert not d1 == {'first': 'first', 'second': 'second', 'third': 'third'}
    assert not d1 == ['first', 'second', 'third']
    assert not d1 == 'this is not a dict'


# Generated at 2022-06-12 23:02:23.434789
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1}), \
        "ImmutableDict({'a': 1}) should equal ImmutableDict({'a': 1})"

    assert ImmutableDict({'a': 1}) != ImmutableDict({'b': 1}), \
        "ImmutableDict({'a': 1}) should not equal ImmutableDict({'b': 1})"

    assert ImmutableDict({'a': 1}) != ImmutableDict({'a': 2}), \
        "ImmutableDict({'a': 1}) should not equal ImmutableDict({'a': 2})"


# Generated at 2022-06-12 23:02:33.417187
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test comparison with other mapping types
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = {'a': 1, 'b': 2}
    assert(d1 == d2)

    # Test different order
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'b': 2, 'a': 1})
    assert(d1 == d2)

    # Test different mapping
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 2})
    assert(not (d1 == d2))

    # Test comparison with non-mapping
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = 1

# Generated at 2022-06-12 23:02:43.910834
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from copy import deepcopy
    class DictWrapper(object):
        def __init__(self, wrapped_dict):
            self.wrapper = wrapped_dict

        def __getitem__(self, key):
            return self.wrapper.__getitem__(key)

    a = dict(a=1, b=2)
    b = dict(a=1, b=2)
    c = dict(a=1, b=3)

    a_immutable = ImmutableDict(a)
    b_immutable = ImmutableDict(b)
    c_immutable = ImmutableDict(c)

    a_immutable_from_b_immutable = ImmutableDict(b_immutable)

    a_immutable_from_a_dict_wrapper = ImmutableDict(DictWrapper(a))

# Generated at 2022-06-12 23:02:52.670197
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """ImmutableDict instances are equal when they have the same items"""
    test_mappings = [
        {'stringkey': 'stringvalue', 'integerkey': 1, 'floatkey': 1.0},
        {'stringkey': 'stringvalue', 'integerkey': 1, 'floatkey': 1.0, 'nonekey': None},
        {'stringkey': 'stringvalue', 'integerkey': 1, 'floatkey': 1.0},
        {'stringkey': 'stringvalue', 'integerkey': 1, 'floatkey': 1.0, 'mappingkey': {1: 1, 2: 2}}
    ]

    for test_mapping in test_mappings:
        mapping_1 = ImmutableDict(test_mapping)
        mapping_2 = ImmutableDict(test_mapping)
        mapping_3 = Imm

# Generated at 2022-06-12 23:02:57.604072
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1})
    assert a == a
    assert a == ImmutableDict({'a': 1})
    assert a != ImmutableDict({'a': 2})
    b = ImmutableDict({'b': 1})
    c = ImmutableDict({'c': 1})
    assert a != [b, c]

# Generated at 2022-06-12 23:03:27.515915
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    t1 = ImmutableDict(a=1, b=2)
    t2 = ImmutableDict(a=1, b=2)
    t3 = ImmutableDict(a=1, b=3)

    assert t1 == t2
    assert not t1 == t3
    assert not t1 == 'abcd'


if __name__ == '__main__':
    test_ImmutableDict___eq__()

# Generated at 2022-06-12 23:03:35.751246
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(dict(key1='value1', key2='value2', key3='value3'))
    # Different order of the dictionary keys
    d2 = ImmutableDict(dict(key3='value3', key2='value2', key1='value1'))
    assert d1 == d2

    # Different type of the dictionary value
    d3 = ImmutableDict(dict(key1='value1', key2='value2', key3='value3'))
    d4 = ImmutableDict(dict(key1=1, key2='value2', key3='value3'))
    assert d3 != d4

    # Different type of the input
    d5 = ImmutableDict(dict(key1='value1', key2='value2', key3='value3'))
    assert d

# Generated at 2022-06-12 23:03:39.618273
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Base case (equality)"""
    d1 = ImmutableDict({'a': 1})
    d2 = ImmutableDict({'a': 1})
    assert d1 == d2


# Generated at 2022-06-12 23:03:47.486490
# Unit test for function is_iterable
def test_is_iterable():
    # Strings and bytes are not iterables
    assert not is_iterable(None)
    assert not is_iterable('Foo')
    assert not is_iterable(b'Foo')

    # Sequence types are iterables
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())

    # Non-indexable things are not iterables
    assert not is_iterable(object())
    assert not is_iterable(object, True)
    assert not is_iterable(is_iterable)



# Generated at 2022-06-12 23:03:56.008840
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = ImmutableDict({"key1": "value1", "key2": "value2"})
    # check positive case
    assert d == ImmutableDict({"key1": "value1", "key2": "value2"})
    assert d == ImmutableDict({"key2": "value2", "key1": "value1"})
    # check negative case
    assert not d == ImmutableDict({"key1": "value1", "key2": "value1"})
    assert not d == ImmutableDict({"key1": "value1"})
    assert not d == ImmutableDict({"key1": "value1", "key2": "value2", "key3": "value3"})


# Generated at 2022-06-12 23:03:59.415742
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable({}) is True
    assert is_iterable('hello') is True
    assert is_iterable(b'hello') is True
    assert is_iterable(u'hello') is True
    assert is_iterable(1) is False


# Generated at 2022-06-12 23:04:05.250201
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({"a": "b"}) == ImmutableDict({"a": "b"})
    assert ImmutableDict({"a": "b"}) == ImmutableDict({'a': 'b'})
    assert ImmutableDict({"a": "b"}) == ImmutableDict({"a": "b", "c": "d"})
    assert ImmutableDict({"a": "b"}) != ImmutableDict({"a": "a"})
    assert ImmutableDict({"a": "b"}) != ImmutableDict({"b": "b"})
    assert ImmutableDict({"a": "b"}) != ImmutableDict()
    assert ImmutableDict({"a": "b"}) != {"a": "b"}

# Generated at 2022-06-12 23:04:13.035287
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({}) == ImmutableDict({})
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1}) != ImmutableDict({'a': 2})
    assert ImmutableDict({'a': 1, 'b': 1}) == ImmutableDict({'b': 1, 'a': 1})
    assert ImmutableDict({'a': 1, 'b': 1}) != ImmutableDict({'b': 1, 'c': 1})
    assert ImmutableDict({'a': 1}) != {'a': 1}


# Generated at 2022-06-12 23:04:16.420309
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3, 4])
    assert is_iterable((1, 2, 3, 4))
    assert not is_iterable('abc')
    assert is_iterable('abc', True)
    assert is_iterable(range(3))
    assert not is_iterable(123)



# Generated at 2022-06-12 23:04:24.985196
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # ref to https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    # Equivalent to the __eq__ implementation in Python 3.4 collections.abc
    def eq(self, other):
        if isinstance(other, Mapping):
            other = MutableMapping.__iter__(other)
        else:
            return NotImplemented
        return len(self) == len(other) and all(
            p == q for p, q in zip(self.items(), other.items()))

    # Equivalent to the __eq__ implementation in Python 3.4 collections.abc
    def ne(self, other):
        equal = self.__eq__(other)
        if equal is NotImplemented:
            return NotImplemented


# Generated at 2022-06-12 23:05:17.549569
# Unit test for function is_iterable
def test_is_iterable():
    class Foo(object):
        def __iter__(self):
            pass

    class Bar(object):
        pass

    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())

    assert is_iterable(Foo())
    assert is_iterable(Bar())

    assert not is_iterable(1)
    assert not is_iterable(1.0)
    assert not is_iterable(True)
    assert not is_iterable(object())



# Generated at 2022-06-12 23:05:28.166863
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils.six import PY3
    if PY3:
        from collections.abc import Mapping
    else:
        from collections import Mapping

    class DictToCompare(Mapping):
        def __init__(self, mapping):
            self._mapping = dict(mapping)

        def __getitem__(self, key):
            return self._mapping[key]

        def __iter__(self):
            return self._mapping.__iter__()

        def __len__(self):
            return self._mapping.__len__()

        # __eq__ defined as:
        # def __eq__(self, other):
        #     if isinstance(other, DictToCompare):
        #         return len(self) == len(other) and other.keys() == self.keys()

# Generated at 2022-06-12 23:05:37.262763
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert not is_iterable(None)
    assert not is_iterable(100)
    assert is_iterable('foo'.encode('utf-8'))
    assert is_iterable('bar')
    assert not is_iterable('baz', include_strings=False)
    assert is_iterable('qux', include_strings=True)
    assert not is_iterable(ImmutableDict())
    assert is_iterable(ImmutableDict().items())
    assert is_iterable(ImmutableDict().values())
    assert not is_iterable(ImmutableDict().values(), include_strings=False)


# Generated at 2022-06-12 23:05:40.356592
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable('abc')
    assert is_iterable(0)
    assert not is_iterable(None)
    assert not is_iterable(1)


# Generated at 2022-06-12 23:05:48.940482
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable((), include_strings=True) is True
    assert is_iterable([], include_strings=True) is True
    assert is_iterable({}) is True
    assert is_iterable(set()) is True
    assert is_iterable(ImmutableDict()) is True
    assert is_iterable(True) is False
    assert is_iterable(1) is False
    assert is_iterable(1.5) is False
    assert is_iterable('abc', include_strings=True) is True
    assert is_iterable(b'abc', include_strings=True) is True
    assert is_iterable(u'abc') is False
    assert is_iterable(b'abc') is False


# Generated at 2022-06-12 23:05:52.370025
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2])
    assert is_iterable((1, 2))
    assert is_iterable({1, 2})
    assert is_iterable('hello')
    assert not is_iterable(42)
    assert not is_iterable(set)



# Generated at 2022-06-12 23:05:54.959723
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) and is_iterable({}) and is_iterable(())
    assert not is_iterable(0) and not is_iterable('foo')


# Generated at 2022-06-12 23:05:58.851797
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable({'a': 1})
    assert is_iterable('abc')
    assert is_iterable(u'abc')
    assert is_iterable(b'abc')
    assert is_iterable(1) is False
    assert is_iterable(None) is False


# Generated at 2022-06-12 23:06:02.248577
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test equality of ImmutableDict's with the same content"""
    dict1_1 = ImmutableDict({'foo': 'bar', 'baz': 'qux'})
    dict1_2 = ImmutableDict({'baz': 'qux', 'foo': 'bar'})
    dict2 = ImmutableDict({'egg': 'spam'})
    assert dict1_1 == dict1_2
    assert dict1_1 != dict2
    assert dict1_2 != dict2
