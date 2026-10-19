

# Generated at 2022-06-12 22:56:10.677713
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict({'a': 1, 'b': 3, 'c': 5, 'd': 7, 'e': 9})
    removed_keys = ['e', 'a', 'b']

    difference = original.difference(removed_keys)

    assert hash(difference) not in [hash(original), hash(ImmutableDict(removed_keys))]
    assert len(difference) == len(original) - len(removed_keys)
    assert len(original) == 5
    assert len(removed_keys) == 3
    assert 'e' not in difference
    assert 'a' not in difference
    assert 'b' not in difference
    assert 'c' in difference
    assert 'd' in difference
    assert difference['c'] == 5
    assert difference['d'] == 7

# Generated at 2022-06-12 22:56:13.435317
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original_dict = ImmutableDict({'foo': 1, 'bar': 2})
    dict_difference = original_dict.difference(['foo'])
    assert dict_difference == {'bar': 2}

# Generated at 2022-06-12 22:56:18.925554
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    test_dict = ImmutableDict({'keys_in_both': 1, 'keys_only_in_original': 2})
    test_removal_list = ['keys_only_in_original', 'keys_not_in_original']
    test_assert = ImmutableDict({'keys_in_both': 1})
    assert test_dict.difference(test_removal_list) == test_assert



# Generated at 2022-06-12 22:56:24.617564
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    """Test that keys from the subtractive_iterable are removed from the ImmutableDict."""
    base_dict = ImmutableDict({'username': 'root', 'password': 'my_password'})
    new_dict = base_dict.difference(('password',))
    assert 'password' not in new_dict
    assert new_dict == ImmutableDict({'username': 'root'})


# Generated at 2022-06-12 22:56:34.638452
# Unit test for method difference of class ImmutableDict

# Generated at 2022-06-12 22:56:40.874467
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    test_dict = {'a': 1, 'b': 2, 'c': 3}
    test_immut_dict = ImmutableDict(test_dict)
    test_subtractive_iterable = ['a', 'b']
    test_neg_immut_dict = test_immut_dict.difference(test_subtractive_iterable)
    # Assert that ImmutableDict contains only c
    assert len(test_neg_immut_dict) == 1
    assert 'c' in test_neg_immut_dict


# Generated at 2022-06-12 22:56:46.862507
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict(original_key='original_value', shared_key='shared_value', original_key2='original_value2')
    expect = ImmutableDict(original_key='original_value', original_key2='original_value2')
    remove_keys = ['shared_key']
    result = original.difference(remove_keys)
    assert result == expect



# Generated at 2022-06-12 22:56:56.465944
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    d = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert d == ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert d.difference(['a', 'b']) == ImmutableDict({'c': 3})
    assert d.difference(['a', 'd']) == ImmutableDict({'b': 2, 'c': 3})
    assert d.difference(['a', 'd']) != ImmutableDict({'b': 2})
    assert d.difference(['a', 'd']) != ImmutableDict({'b': 2, 'c': 3, 'd': 4})


# Generated at 2022-06-12 22:57:00.327335
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    imm_dict1 = ImmutableDict({'a': 1, 'b': 2})
    imm_dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert imm_dict1 == imm_dict2
    assert imm_dict1.__hash__() == imm_dict2.__hash__()



# Generated at 2022-06-12 22:57:10.429673
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) == True
    assert is_iterable([1, 2]) == True
    assert is_iterable((1, 2)) == True
    assert is_iterable({}) == True
    assert is_iterable({1: 2}) == True
    assert is_iterable(set()) == True
    assert is_iterable(set((1, 2))) == True
    assert is_iterable((1, 2)) == True
    assert is_iterable(xrange(10)) == True
    assert is_iterable('test') == True

    assert is_iterable(None) == False
    assert is_iterable(1) == False
    assert is_iterable(False) == False
    assert is_iterable("") == False

# Generated at 2022-06-12 22:57:20.543724
# Unit test for function is_iterable
def test_is_iterable():
    """Unit tests for is_iterable function"""
    assert is_iterable([])
    assert is_iterable((x for x in xrange(5)))
    assert is_iterable(set())
    assert is_iterable({})
    assert not is_iterable(None)
    assert is_iterable([u"foo"])
    assert is_iterable([b"foo"])
    assert is_iterable(u"foo")
    assert is_iterable(b"foo")
    assert is_iterable({u"foo": u"bar"})
    assert is_iterable({b"foo": b"bar"})
    assert not is_iterable(list)
    assert not is_iterable(int)
    assert not is_iterable(1)

# Generated at 2022-06-12 22:57:31.228809
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Condition #1: Equivalent
    a = ImmutableDict({'A': 'foo', 'B': 'bar'})
    b = ImmutableDict({'B': 'bar', 'A': 'foo'})

    assert a == b

    # Condition #2: Not Equivalent
    a = ImmutableDict({'A': 'foo', 'B': 'bar'})
    b = ImmutableDict({'B': 'bar', 'A': 'bar'})
    assert a != b

    # Condition #3: Non Equivalent Type
    a = ImmutableDict({'A': 'foo', 'B': 'bar'})
    b = ['B', 'bar', 'A', 'foo']
    assert a != b

if __name__ == '__main__':
    test_ImmutableDict___eq__()

# Generated at 2022-06-12 22:57:38.565214
# Unit test for function is_iterable
def test_is_iterable():
    """Test is_iterable with all types of iterables and strings"""
    # Iterables
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable(set())
    assert is_iterable({})
    # Strings
    assert is_iterable('string')
    assert is_iterable(''.encode('utf-8'))
    # Non iterables
    assert not is_iterable(True)
    assert not is_iterable(123)
    assert not is_iterable(1.23)
    assert not is_iterable(None)


# Generated at 2022-06-12 22:57:43.937578
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'foo': 'bar'})
    b = ImmutableDict({'foo': 'bar'})
    assert a == b
    b = ImmutableDict({'foo': 'baz'})
    assert a != b

    d = ImmutableDict({'foo': ['bar', {'baz': 'qux'}]})
    e = ImmutableDict({'foo': ['bar', {'baz': 'qux'}]})
    assert d == e


# Generated at 2022-06-12 22:57:49.093191
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # pylint: disable=too-many-branches

    from random import randint, choice
    from string import ascii_letters, digits
    from itertools import chain

    ####################################################################################################################
    # Testing for equality of dictionaries
    ####################################################################################################################

    # Empty dictionaries are equal
    assert ImmutableDict() == ImmutableDict()

    # Dictionaries with different content are not equal
    assert ImmutableDict({'a': 1}) != ImmutableDict({'b': 1})

    # Dictionaries with the same content but different order are equal
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'b': 2, 'a': 1})

# Generated at 2022-06-12 22:57:54.656053
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable(range(5))
    assert is_iterable('ABC')
    assert is_iterable(u'ABC', True)
    assert is_iterable(b'ABC', True)
    assert is_iterable(1) is False
    assert is_iterable(object) is False
    assert is_iterable(None) is False
    assert is_iterable(Exception()) is False


# Generated at 2022-06-12 22:57:57.727999
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) == True
    assert is_iterable(1) == False
    assert is_iterable({}) == True
    assert is_iterable((3,)) == True


# Generated at 2022-06-12 22:58:02.358875
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """To test if two immutable dictionarys with same values are equal"""
    keyvalue = {'c': 2, 'b': 1, 'd': 3}
    test_immutable_dict = ImmutableDict(keyvalue)
    test_immutable_dict2 = ImmutableDict(keyvalue)
    assert test_immutable_dict == test_immutable_dict2


# Generated at 2022-06-12 22:58:08.896681
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    lhs_1 = ImmutableDict(a=1, b=2, c=3)
    lhs_2 = ImmutableDict(a=1, b=2, c=3)
    rhs_1 = ImmutableDict(a=1, b=2, c=3, d=4)
    rhs_2 = ImmutableDict(a=1, b=2, c=3, d=5)
    rhs_3 = ImmutableDict(a=2, b=2, c=3)
    rhs_4 = ImmutableDict(a=1, b=3, c=3)
    rhs_5 = ImmutableDict(a=1, b=2, c=4)

    assert lhs_1 == lhs_2
    assert lhs_1 != rhs_1

# Generated at 2022-06-12 22:58:19.975458
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit testing for ImmutableDict.__eq__() method."""
    dict_a = ImmutableDict({"a": 1, "b": 2})
    dict_b = ImmutableDict({"b": 2, "a": 1})
    dict_c = ImmutableDict({"a": 1})
    dict_d = ImmutableDict({"b": 3})
    dict_e = dict_a.union({"b": 2, "a": 1})
    dict_f = dict_a.union({"d": 4, "c": 3, "a": 1})
    dict_g = dict_a.difference(["b"])

    eq_tests = [
        dict_a,
        dict_b,
        dict_e
    ]

# Generated at 2022-06-12 22:58:25.585493
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 'b', 'c': 'd'}) == ImmutableDict({'a': 'b', 'c': 'd'})


# Generated at 2022-06-12 22:58:29.109771
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'one': 1, 'two': 2}) == ImmutableDict({'one': 1, 'two': 2})
    assert ImmutableDict({'one': 1, 'two': 2}) != ImmutableDict({'one': 1, 'three': 3})

# Generated at 2022-06-12 22:58:32.145109
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit tests for the ImmutableDict.__eq__() method"""
    a = ImmutableDict(foo=1, bar=2, baz=3)
    b = ImmutableDict(baz=3, bar=2, foo=1)
    assert a == b



# Generated at 2022-06-12 22:58:38.179509
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test method __eq__ of class ImmutableDict"""
    dic1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})

    # Test equal dictionaries
    dic2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert dic1 == dic2, 'Equal dictionaries do not compare equal'

    # Test equal dictionaries with additional keys
    dic2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
    assert dic1 == dic2, 'Equal dictionaries with additional keys do not compare equal'

    # Test equal dictionaries in different order

# Generated at 2022-06-12 22:58:47.675885
# Unit test for function is_iterable
def test_is_iterable():
    assert(is_iterable([1, 2, 3]))
    assert(is_iterable((1, 2, 3)))
    assert(is_iterable((x for x in range(10))))
    assert(is_iterable({1, 2, 3}))
    assert(is_iterable({'one': 1, 'two': 2, 'three': 3}))
    assert(is_iterable('123'))
    assert(is_iterable(b'123'))
    assert(not is_iterable(123))
    assert(is_iterable(ImmutableDict({'one': 1, 'two': 2, 'three': 3})))


# Generated at 2022-06-12 22:58:55.521768
# Unit test for function is_iterable
def test_is_iterable():
    is_iterable_test_cases = dict(
        empty_dict=dict(),
        dict={'a': 'A'},
        empty_list=[],
        list=[1, 1],
        empty_tuple=tuple(),
        tuple=('x', 'y'),
        empty_set=set(),
        set=set('xyz'),
        empty_string='',
        string='x',
        character='x',
        empty_bytes=binary_type(),
        bytes=binary_type('xyz'),
        number=4)

    for case in is_iterable_test_cases:
        assert is_iterable(is_iterable_test_cases[case])



# Generated at 2022-06-12 22:59:06.770012
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    def check(a, b, expected):
        assert (a == b) == expected

    d1 = ImmutableDict(a=1, b=2)
    d2 = ImmutableDict(a=1, b=2)
    check(d1, d2, True)

    d3 = ImmutableDict(a=1)
    check(d1, d3, False)

    d4 = ImmutableDict()
    check(d1, d4, False)
    check(d4, d4, True)

    check(d1, dict(a=1, b=2), False)
    check(d1, d1, True)
    check(d1, None, False)
    check(d1, 'bla', False)



# Generated at 2022-06-12 22:59:15.528791
# Unit test for function is_iterable
def test_is_iterable():
    class X(object):
        pass

    class Y(object):
        def __iter__(self):
            pass

    assert is_iterable([0, 1, 2]) is True
    assert is_iterable((0, 1, 2)) is True
    assert is_iterable(set([0, 1, 2])) is True
    assert is_iterable({'a': 0, 'b': 1, 'c': 2}) is True
    assert is_iterable(xrange(0, 3)) is True
    assert is_iterable(b'abc') is True
    assert is_iterable('abc') is True
    assert is_iterable(X()) is False
    assert is_iterable(Y()) is True


# Generated at 2022-06-12 22:59:24.299470
# Unit test for function is_iterable
def test_is_iterable():

    # is_iterable should return True for any iterable
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable(dict(a=1, b=2, c=3))

    # is_iterable should return False for non-iterable
    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(1.0)
    assert not is_iterable('abc')
    assert not is_iterable(b'abc')


# Generated at 2022-06-12 22:59:34.883968
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert not is_iterable(dict())
    assert not is_iterable(12.0)
    assert not is_iterable(True)
    assert not is_iterable(False)
    assert not is_iterable(set())
    assert not is_iterable([1])
    assert not is_iterable(tuple())
    assert is_iterable((x for x in [1]))
    assert is_iterable(((x for x in [1]),))
    assert is_iterable([(x for x in [1])])
    assert is_iterable(set([(x for x in [1])]))

# Generated at 2022-06-12 22:59:47.885025
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dictionary1 = ImmutableDict({'1':'one', '2':'two', '3':'three'})
    dictionary2 = ImmutableDict({'1':'one', '2':'two', '3':'three'})
    dictionary3 = ImmutableDict({'1':'one', '2':'two'})
    dictionary4 = ImmutableDict({'1':'one', '2':'two', '3':'thre'})
    dictionary5 = ImmutableDict({'1':'one', '2':'two', '4':'four'})
    dictionary6 = ImmutableDict({'2':'two', '1':'one', '3':'three'})
    dictionary7 = ImmutableDict({'2':'two', '1':'one'})
    dictionary8 = ImmutableD

# Generated at 2022-06-12 22:59:57.405988
# Unit test for function is_iterable
def test_is_iterable():
    class DummyIter(object):
        def __iter__(self):
            return
        # Dummy __getitem__ method so that the isinstance check for Sequence returns True
        def __getitem__(self):
            return

    assert is_iterable(DummyIter())
    assert is_iterable(DummyIter())
    assert is_iterable(set())
    assert is_iterable(frozenset())
    assert is_iterable(list())
    assert is_iterable(dict())
    assert is_iterable(tuple())
    assert is_iterable(type(x for x in range(0)))
    assert is_iterable(text_type('abc'))
    assert is_iterable(binary_type('abc'))
    assert not is_iterable(3)

# Generated at 2022-06-12 22:59:59.987520
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'test': 1})
    d2 = ImmutableDict({'test': 1})
    d3 = ImmutableDict({'test': 2})
    assert d1 == d2


# Generated at 2022-06-12 23:00:10.234375
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(name="old", type="cow") == ImmutableDict(name="old", type="cow")
    assert ImmutableDict(name="old", type="cow") != ImmutableDict(name="old", type="hen")
    assert ImmutableDict(name="old", type="cow") != ImmutableDict(name="milk", type="cow")
    assert ImmutableDict(name="old", type="cow") == ImmutableDict(name="old", type="cow", age=25)
    assert ImmutableDict({'name': 'old', 'type': 'cow'}) == ImmutableDict({'name': 'old', 'type': 'cow'})
    assert ImmutableDict({'name': 'old', 'type': 'cow'}) == ImmutableDict(name="old", type="cow")

# Generated at 2022-06-12 23:00:20.515432
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    def assert_equal(a, b):
        assert a == b
        assert hash(a) == hash(b)

    def assert_not_equal(a, b):
        assert a != b
        assert hash(a) != hash(b)

    # Test whether ImmutableDict really is immutable
    a = ImmutableDict()
    a['first'] = 1
    assert_not_equal(a, {})

    # Test __eq__ using dictionaries
    assert_equal(ImmutableDict(), {})
    assert_equal(ImmutableDict({'first': 1, 'second': 2}), {'first': 1, 'second': 2})
    assert_not_equal(ImmutableDict({'first': 1, 'second': 2}), {'first': 2, 'second': 1})

# Generated at 2022-06-12 23:00:29.430563
# Unit test for function is_iterable
def test_is_iterable():
    """Test for utility function is_iterable."""
    assert is_iterable('abc')
    assert is_iterable(['a', 'b'])
    assert is_iterable('abc')
    assert is_iterable(('a', 'b'))
    assert is_iterable({'a', 'b'})
    assert is_iterable({'a': 'b'})
    assert is_iterable(u'abc')
    assert is_iterable(xrange(10))
    assert is_iterable(range(10))
    assert is_iterable(dict.fromkeys(['a']))
    assert is_iterable(dict.fromkeys(('a',)).keys())
    assert is_iterable(dict.fromkeys(u'abc').keys())

# Generated at 2022-06-12 23:00:39.841607
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    '''Test for class ImmutableDict method __eq__'''
    from collections import OrderedDict

    # Dictionaries are equal
    dict1 = ImmutableDict(OrderedDict([('a', 'val1'), ('b', 'val2'), ('c', 'val3')]))
    dict2 = ImmutableDict(OrderedDict([('a', 'val1'), ('c', 'val3'), ('b', 'val2')]))
    assert dict1 == dict2

    # Dictionary keys are in different order dict1 is not equal to dict2
    dict1 = ImmutableDict(OrderedDict([('a', 'val1'), ('b', 'val2'), ('c', 'val3')]))

# Generated at 2022-06-12 23:00:44.659186
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(xrange(10))
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable({})
    assert is_iterable(1)
    assert is_iterable('')
    assert is_iterable(u'')
    assert not is_iterable(None)


# Generated at 2022-06-12 23:00:55.741404
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = ImmutableDict({'a':'b', 'c':'d'})
    assert d == ImmutableDict({'a':'b', 'c':'d'})
    assert d != ImmutableDict({'a':'b', 'c':'e'})
    assert d != ImmutableDict({'a':'b', 'c':'d', 'e':'f'})
    assert d != ImmutableDict({'a':'b', 'e':'f'})

    assert d != dict({'a':'b', 'c':'d'})
    assert d != MutableMapping({'a':'b', 'c':'d'})
    assert d != {'a':'b', 'c':'d'}


# Generated at 2022-06-12 23:01:03.158001
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2})
    b = ImmutableDict({'a': 1})
    c = ImmutableDict({'a': 1, 'b': 2})
    d = {'a': 1, 'b': 2}
    e = object()

    assert a != b
    assert a == c
    assert a != d
    assert a != e

    assert b != c
    assert b != d
    assert b != e

    assert c != d
    assert c != e

    assert d != e

# Generated at 2022-06-12 23:01:24.112079
# Unit test for function is_iterable
def test_is_iterable():
    class NonIterable:
        pass
    class Iterable:
        def __iter__(self):
            return iter(())
    assert is_iterable(1) is False
    assert is_iterable('string') is True
    assert is_iterable(u'string') is True
    assert is_iterable([1, 2, 3, 4]) is True
    assert is_iterable((1, 2, 3, 4)) is True
    assert is_iterable({1, 2, 3, 4}) is True
    assert is_iterable({'a': 1, 'b': 2}) is True
    assert is_iterable(NonIterable()) is False
    assert is_iterable(Iterable()) is True


# Generated at 2022-06-12 23:01:32.111956
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    b = ImmutableDict({'a': 1, 'b': 2})
    a = ImmutableDict({'a': 1, 'b': 2})
    assert a == b
    assert a == {'a': 1, 'b': 2}
    assert a == {'b': 2, 'a': 1}
    assert a == {'a': 1}
    assert a != 'a'
    assert a != ImmutableDict()
    assert a != {'b': 2, 'a': 2}
    assert a != {'b': 1, 'a': 2}
    assert a != {'b': 2, 'b': 2}


# Generated at 2022-06-12 23:01:36.976906
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test some basic equality
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1}) != ImmutableDict({'b': 1})
    # Test different order of arguments
    assert ImmutableDict({'a': 1, 'b': 1}, b=1, a=1) == ImmutableDict({'a': 1, 'b': 1}, b=1, a=1)
    assert ImmutableDict({'a': 1, 'b': 1}, b=1, a=1) != ImmutableDict({'b': 1, 'a': 1}, b=1, a=1)
    # Test unhashable value
    assert ImmutableDict({'a': [1]})

# Generated at 2022-06-12 23:01:46.471733
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=2, c=3)
    assert ImmutableDict(a=ImmutableDict(b=1)) == ImmutableDict(a=ImmutableDict(b=1), c=5)
    assert ImmutableDict(a=1, b=2) != None
    assert ImmutableDict(a=1, b=2) != str()
    assert ImmutableDict(a=1, b=2) != {}
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=3)

# Generated at 2022-06-12 23:01:55.448929
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test for method __eq__ of ImmutableDict class.
    """
    # Test equal dicts
    first_im_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    second_im_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert first_im_dict == second_im_dict

    # Test equal dicts with the same values in different order
    first_im_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    second_im_dict = ImmutableDict({'c': 3, 'a': 1, 'b': 2})
    assert first_im_dict == second_im_dict

    # Test not equal dicts
    first_im_dict = Immutable

# Generated at 2022-06-12 23:02:00.906578
# Unit test for function is_iterable
def test_is_iterable():

    assert(is_iterable([3, 2, 1]) == True)
    assert(is_iterable((3, 2, 1)) == True)
    assert(is_iterable({3, 2, 1}) == True)
    assert(is_iterable({'a': 1, 'b': 2}) == True)

    assert(is_iterable(1) == False)
    assert(is_iterable('1') == False)
    assert(is_iterable(None) == False)



# Generated at 2022-06-12 23:02:08.126978
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable([x for x in [1, 2, 3]])
    assert is_iterable((1, 2, 3))
    assert is_iterable(xrange(1, 4))

    assert not is_iterable(1)
    assert not is_iterable('str')
    assert not is_iterable('str'.split())
    assert not is_iterable(dict(a=1, b=2, c=3))



# Generated at 2022-06-12 23:02:16.717284
# Unit test for function is_iterable
def test_is_iterable():
    """Tests for the is_iterable function."""
    assert(is_iterable([]))
    assert(is_iterable(set()))
    assert(is_iterable(dict()))
    assert(is_iterable(tuple()))
    assert(is_iterable(generator()))

    assert(not is_iterable(list()))
    assert(not is_iterable(set()))
    assert(not is_iterable(dict()))
    assert(not is_iterable(tuple()))
    assert(not is_iterable(generator()))



# Generated at 2022-06-12 23:02:26.743780
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() == ImmutableDict
    assert ImmutableDict({1: 1, 2: 2}) == ImmutableDict({1: 1, 2: 2})
    assert ImmutableDict({1: 2, 2: 2}) != ImmutableDict({1: 1, 2: 2})
    assert ImmutableDict({1: 1, 2: 2}) != ImmutableDict({1: 1, 2: 2, 3: 3})
    assert ImmutableDict({1: 1, 2: 2}) != ImmutableDict({1: 1})
    assert ImmutableDict({1: 1, 2: 2}) != ImmutableDict

# Generated at 2022-06-12 23:02:35.542097
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test method ImmutableDict.__eq__()
    """
    id_1 = ImmutableDict({"first": 1, "second": 2})
    assert id_1 == id_1 and id_1 == ImmutableDict({"first": 1, "second": 2}) and id_1 == ImmutableDict(id_1) and id_1 == dict(id_1)
    assert id_1 != 1 and id_1 != False and id_1 != tuple(id_1) and id_1 != list(id_1)
    assert id_1 != ImmutableDict({"first": 1, "second": 3})
    assert id_1 != ImmutableDict({"first": 1}) and id_1 != ImmutableDict({"first": 1, "second": 2, "third": 3})

# Generated at 2022-06-12 23:03:05.929287
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # equal
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict([('b', 2), ('a', 1)])
    assert d1 == d2
    # same order but not equal
    d3 = ImmutableDict([('a', 2), ('b', 1)])
    assert d1 != d3
    # different order but not equal
    d4 = ImmutableDict({'a': 1, 'b': 3})
    assert d1 != d4
    # neither order nor equal
    d5 = ImmutableDict({'a': 2, 'b': 1})
    assert d1 != d5


# Generated at 2022-06-12 23:03:14.789674
# Unit test for function is_iterable
def test_is_iterable():
    """Exercise function is_iterable and validate results."""
    assert not is_iterable(None)

    # Validate for strings.
    assert is_iterable('')
    assert is_iterable('abc')
    assert not is_iterable('abc', include_strings=False)

    # Validate for b-strings.
    assert is_iterable('abc'.encode())
    assert not is_iterable('abc'.encode(), include_strings=False)

    # Validate for buffers.
    assert is_iterable(buffer(''))
    assert is_iterable(buffer('abc'))
    assert not is_iterable(buffer('abc'), include_strings=False)
    # We may need to rethink this.  In Python 2.6 buffers are iterable, but
    # in Python 3, they are not.


# Generated at 2022-06-12 23:03:23.079456
# Unit test for function is_iterable
def test_is_iterable():
    iterable_examples = ['string', bytearray('Test'), [{'key': 'value'}], ('tuple', 'tuple')]
    non_iterable_examples = ['', None, object(), 10, 1.0, ['List']]
    for iterable in iterable_examples:
        if not is_iterable(iterable, include_strings=True):
            raise AssertionError("'%s' should be iterable" % iterable)

    for non_iterable in non_iterable_examples:
        if is_iterable(non_iterable, include_strings=True):
            raise AssertionError("'%s' should not be iterable" % non_iterable)


# Generated at 2022-06-12 23:03:28.590284
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'name': 'yellow'})
    b = ImmutableDict({'name': 'yellow'})
    assert a == b
    b['name'] = 'red'
    assert a != b
    assert a != {'name': 'red'}
    assert a != 'this is not right'
    assert not a == {'name': 'red'}
    assert not a == 'this is not right'


# Generated at 2022-06-12 23:03:36.523748
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable(range(5)) is True
    assert is_iterable({'a': 0, 'b': 1}) is True
    assert is_iterable('abcdef') is True
    assert is_iterable(u'abcdef') is True
    assert is_iterable(b'abcdef') is True
    assert is_iterable(True) is False
    assert is_iterable(False) is False

    assert is_iterable('abcdef', include_strings=True) is True
    assert is_iterable(u'abcdef', include_strings=True) is True

# Generated at 2022-06-12 23:03:47.338911
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict."""
    dict_a = ImmutableDict({'key_equal': 'equal_value', 'key_unequal': 'unequal_value'})
    dict_b = ImmutableDict({'key_equal': 'equal_value', 'key_unequal': 'equal_value'})
    dict_c = dict(dict_a)
    dict_d = dict(dict_b)
    dict_e = ImmutableDict({'key_equal': 'equal_value', 'key_unequal': 'unequal_value', 'key_new': 'new_value'})
    dict_f = dict({})

    assert dict_a == dict_c
    assert dict_a != dict_b
    assert dict_c == dict_a
    assert dict_b != dict

# Generated at 2022-06-12 23:03:55.232375
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Verifies that method ImmutableDict.__eq__ works as expected"""
    # Verify that ImmutableDict.__eq__ identifies any Mapping as equal to another
    d = ImmutableDict({'a': 'b'})
    assert d == {'a': 'b'}
    assert d == ImmutableDict({'a': 'b'})

    # Verify that ImmutableDict.__eq__ identifies different mappings as not equal
    assert d != ImmutableDict({'a': 'c'})
    assert d != {'b': 'a'}

    # Verify that ImmutableDict.__eq__ identifies a non-mapping as not equal
    assert d != 'a'

# Generated at 2022-06-12 23:03:57.788301
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 11})
    d2 = ImmutableDict({'a': 11})
    d3 = ImmutableDict({'b': 11})
    assert d1 == d1
    assert d1 == d2
    assert d1 != d3

# Generated at 2022-06-12 23:04:02.703187
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1}) == {'a': 1}
    assert {'a': 1} == ImmutableDict({'a': 1})

# Generated at 2022-06-12 23:04:05.871485
# Unit test for function is_iterable
def test_is_iterable():
    class myclass:
        def __iter__(self):
            return iter(())
        def __getitem__(self, item):
            raise TypeError()
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable(set())
    assert is_iterable('foo')
    assert is_iterable(myclass())
    assert not is_iterable(None)
    assert not is_iterable(1)



# Generated at 2022-06-12 23:04:54.038965
# Unit test for function is_iterable
def test_is_iterable():
    def f(): pass
    assert is_iterable([])
    assert is_iterable((i for i in range(5)))
    assert not is_iterable('')
    assert not is_iterable(5)
    assert not is_iterable(f)


# Generated at 2022-06-12 23:05:04.576276
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict_a = ImmutableDict({'key': 'value', 'key2': 'value2'})
    dict_b = ImmutableDict({'key': 'value', 'key2': 'value2'})
    dict_c = dict(key='value', key2='value2')
    dict_d = dict(key='value', key2='value2', key3='value3')
    dict_e = ImmutableDict({'key': 'value', 'key2': 'value3'})
    dict_f = ImmutableDict({'key': 'value3', 'key2': 'value2'})
    dict_g = ImmutableDict({'key': 'value', 'key2': 'value2'})
    dict_h = ImmutableDict({'key': 'value2', 'key2': 'value2'})

# Generated at 2022-06-12 23:05:13.895501
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'var': 'value'}) == ImmutableDict({'var': 'value'})
    assert not ImmutableDict({'var': 'value'}) == ImmutableDict({'var': 'value2'})
    assert not ImmutableDict({'var': 'value'}) == ImmutableDict({'var': 'value', 'var2': 'value2'})
    assert not ImmutableDict({'var': 'value'}) == ImmutableDict({'var2': 'value2'})
    assert not ImmutableDict({'var': 'value'}) == ImmutableDict({'var': 'value'}, var2='value2')
    assert not ImmutableDict({'var': 'value'}) == ImmutableDict()

# Generated at 2022-06-12 23:05:16.462668
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({"a":"b"})
    d2 = ImmutableDict({"a":"b"})
    h = hash(d1)
    assert d1 == d2

# Unit tests for method union of class ImmutableDict

# Generated at 2022-06-12 23:05:21.261469
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('hello')
    assert is_iterable([1, 2, 3])
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable(dict(a=1, b=2, c=3))
    assert not is_iterable(None)
    assert not is_iterable(45)



# Generated at 2022-06-12 23:05:31.913062
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict()
    b = ImmutableDict()
    assert a == b
    a = ImmutableDict(name='Joe')
    b = ImmutableDict(name='Joe')
    assert a == b
    a = ImmutableDict(name='Joe', age=12)
    b = ImmutableDict(name='Joe', age=12)
    assert a == b
    a = ImmutableDict(name='Joe', age=12)
    b = ImmutableDict(age=12, name='Joe')
    assert a == b
    a = ImmutableDict(name='Joe', age=12)
    b = ImmutableDict(name='Joe', age=12, size="M")
    assert a != b
    a = ImmutableDict(name='Joe', age=12)
    b

# Generated at 2022-06-12 23:05:38.401509
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 3})
    assert ImmutableDict({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert ImmutableDict({'a': 1, 'b': 2}) != {'a': 1, 'b': 3}

# Generated at 2022-06-12 23:05:45.311963
# Unit test for function is_iterable
def test_is_iterable():
    """Function to test is_iterable function.

    Tests the function for various scenarios and prints the failure message in case of any failures.
    """

# Generated at 2022-06-12 23:05:52.804193
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(range(1))
    assert is_iterable(xrange(1))
    assert is_iterable(iter(b''))
    assert is_iterable(iter(u''))
    assert is_iterable(u'')
    assert is_iterable(b'')
    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(1.0)
    assert not is_iterable(object())


# Generated at 2022-06-12 23:05:57.543772
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('abc')
    assert is_iterable(u'abc')
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable({'a': 1, 'b': 2, 'c': 3})
    assert is_iterable(1) is False
