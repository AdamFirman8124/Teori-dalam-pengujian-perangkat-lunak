

# Generated at 2022-06-12 22:56:08.741425
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    i_dict = ImmutableDict({"a": "b", "c": "d", "e": "f"})
    diff_dict = i_dict.difference(["a", "e"])
    # check number of keys
    assert len(diff_dict.keys()) == 1
    # check the removed keys
    assert "e" not in diff_dict.keys()
    assert "a" not in diff_dict.keys()
    # check the remaining key
    assert "c" in diff_dict.keys()

# Generated at 2022-06-12 22:56:17.928099
# Unit test for function is_iterable
def test_is_iterable():
    # is_iterable does not include strings

    assert is_iterable('') is False
    assert is_iterable('A string') is False
    assert is_iterable(b'') is False
    assert is_iterable(b'A strin') is False

    assert is_iterable(['A', 'list']) is True
    assert is_iterable(set(['A', 'set', 'is', 'hashable'])) is True
    assert is_iterable(tuple(['A', 'tuple'])) is True
    assert is_iterable(ImmutableDict(A='dictionary')) is True

    assert is_iterable({'a': 'dictionary'}) is True
    # non-hashable
    assert is_iterable({1: 2, {}: 3}) is False

    assert is_iterable

# Generated at 2022-06-12 22:56:24.056805
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = ImmutableDict({'a': 1, 'b': 2})
    assert d == d
    assert d == {'a': 1, 'b': 2}
    assert d == ImmutableDict({'b': 2, 'a': 1})
    assert d != {'a': 1, 'c': 3}
    assert d != ImmutableDict(a=1, b=3)
    assert d != 42


# Generated at 2022-06-12 22:56:27.274335
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    a = ImmutableDict({1:1, 2:2, 3:3})
    b = a.difference([2, 3])
    assert b == {1:1}



# Generated at 2022-06-12 22:56:36.486369
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    immutable_dict = ImmutableDict(a=1, b=2, c=3, d=4)
    assert immutable_dict == immutable_dict.difference([])
    assert immutable_dict.difference([]) != immutable_dict.difference(['a'])
    assert immutable_dict.difference(['b']) == ImmutableDict(a=1, c=3, d=4)
    assert immutable_dict.difference(['b', 'c']) == ImmutableDict(a=1, d=4)
    assert immutable_dict.difference(['b', 'c', 'd']) == ImmutableDict(a=1)
    assert immutable_dict.difference(['a', 'b', 'c', 'd']) == ImmutableDict()

# Generated at 2022-06-12 22:56:40.643242
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = a.difference(('a',))
    assert a == ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert b == ImmutableDict({'b': 2, 'c': 3})


# Generated at 2022-06-12 22:56:52.030531
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():

    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = d1.difference(['a'])

    assert d1 == ImmutableDict({'a': 1, 'b': 2})
    assert d2 == ImmutableDict({'b': 2})
    assert d1 is not d2

    d1 = ImmutableDict({'a': 1, 'b': 2})
    d3 = d1.difference(['a', 'b'])

    assert d1 == ImmutableDict({'a': 1, 'b': 2})
    assert d3 == ImmutableDict()
    assert d1 is not d3
    assert d3 is not d2

    d2 = d1.difference(['a', 'd'])


# Generated at 2022-06-12 22:57:01.234408
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    """Unit test for method difference of class ImmutableDict."""
    original = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    expected_1 = ImmutableDict({'b': 2, 'c': 3})
    expected_2 = ImmutableDict({'a': 1, 'b': 2})
    expected_3 = ImmutableDict({'a': 1, 'c': 3})
    expected_4 = ImmutableDict({'a': 1})
    output_1 = original.difference(['a'])
    output_2 = original.difference(['c'])
    output_3 = original.difference(['a', 'c'])
    output_4 = original.difference(['a', 'b', 'c'])

# Generated at 2022-06-12 22:57:04.015781
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable(set((1, 2, 3)))
    assert is_iterable(1) is False


# Generated at 2022-06-12 22:57:10.431357
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 10, 'b': 20})
    d2 = ImmutableDict({'b': 20, 'a': 10})
    d3 = ImmutableDict({'b': 30, 'a': 10})
    d4 = {'b': 30, 'a': 10}

    assert d1 == d2
    assert d1 != d3
    assert d1 != d4


# Generated at 2022-06-12 22:57:18.771061
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test that two ImmutableDict instances with the same key-value pairs are evaluated as equal
    """
    a = ImmutableDict([('a', 1), ('b', 2)])
    b = ImmutableDict([('b', 2), ('a', 1)])
    assert a == b


# Generated at 2022-06-12 22:57:22.998295
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict(a=1, b=2) == ImmutableDict(b=2, a=1)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=2, b=2)

test_ImmutableDict___eq__()

# Generated at 2022-06-12 22:57:33.506254
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # test equality on empty dicts and dicts with one values
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() != ImmutableDict({'1':'1'})
    assert ImmutableDict({'1':'1'}) == ImmutableDict({'1':'1'})
    assert ImmutableDict({1:'1'}) != ImmutableDict({'1':'1'})
    # test equality on dict with 3 values
    assert ImmutableDict({1:'1',2:'2',3:'3'}) == \
    ImmutableDict({1:'1',2:'2',3:'3'})
    assert ImmutableDict({1:'1',2:'2',3:'3'}) != \
    ImmutableDict({3:'3',2:'2',1:'1'})

# Generated at 2022-06-12 22:57:42.445527
# Unit test for function is_iterable
def test_is_iterable():
    def test_type(type_):
        assert is_iterable(type_())
        assert not is_string(type_())
        assert is_iterable(type_, include_strings=True)
        assert not is_string(type_, include_strings=True)

    test_type(list)
    test_type(tuple)
    test_type(set)
    test_type(frozenset)
    test_type(dict)
    test_type(MutableMapping)
    test_type(ImmutableDict)
    test_type(float)
    test_type(int)
    test_type(complex)
    test_type(bytes)
    test_type(bytearray)
    test_type(text_type)



# Generated at 2022-06-12 22:57:50.825302
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test custom implementation of __eq__ of class ImmutableDict"""
    originalDict = ImmutableDict(a=1, b=2)
    equalDict = ImmutableDict(a=1, b=2)
    nonEqualDict = ImmutableDict(a=1, b=3)
    testDict = dict(a=1, b=2)
    testHash = hash(testDict)

    assert originalDict.__hash__() == testHash

    # Test equality
    assert originalDict == equalDict
    assert not originalDict == nonEqualDict

    # Test mutability
    try:
        originalDict['c'] = 2
        assert False, "It should not be possible to mutate ImmutableDict."
    except:
        assert True

    # Test equality with mutable

# Generated at 2022-06-12 22:58:00.755614
# Unit test for function is_iterable
def test_is_iterable():
    # Test with data types that can be iterable
    assert is_iterable([1, 2]) is True
    assert is_iterable(['a', 'b']) is True
    assert is_iterable([]) is True
    assert is_iterable(()) is True
    assert is_iterable({}) is True
    assert is_iterable(set([1, 2])) is True
    assert is_iterable({'a': 1, 'b': 2}) is True
    assert is_iterable(1) is False
    assert is_iterable('b') is True
    assert is_iterable('s') is True
    assert is_iterable(2.2) is False
    assert is_iterable(u'a') is True
    assert is_iterable(u'u') is True

# Generated at 2022-06-12 22:58:03.271509
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'b': 2, 'a': 1})
    assert not (ImmutableDict({'a': 1, 'b': 3}) == ImmutableDict({'b': 2, 'a': 1}))

# Generated at 2022-06-12 22:58:06.347890
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    A = ImmutableDict({'a': 1, 'b': 2})
    B = ImmutableDict({'a': 1, 'b': 2})
    assert A == B
    assert hash(A) == hash(B)



# Generated at 2022-06-12 22:58:17.542260
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({"a": 1, "b": 2})
    d2 = ImmutableDict({"a": 1, "b": 2})
    d3 = ImmutableDict({"b": 2, "a": 1})
    assert d1 == d2
    assert d1 == d3
    d4 = ImmutableDict({"a": 1, "b": 2, "c": 3})
    assert d1 != d4

    d5 = {"a": 1, "b": 2}
    assert d1 != d5

    d6 = {"a": 1, "b": 2, "c": 3}
    assert d1 != d6

    d7 = ImmutableDict({"a": 1, "b": 2, "c": 4})
    assert d1 != d7

# Generated at 2022-06-12 22:58:28.355471
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    #check that hash values equal
    test_dict_one = ImmutableDict(one=1, two=2, three=3)
    test_dict_two = ImmutableDict(two=2, three=3, one=1)
    test_dict_three = ImmutableDict(one=1, two=2)
    test_dict_four = ImmutableDict(four=4, five=5)
    assert hash(test_dict_one) == hash(test_dict_two)
    assert hash(test_dict_two) != hash(test_dict_three)
    assert hash(test_dict_three) != hash(test_dict_four)
    #check that equal values in dicts of equal length return True
    assert test_dict_one == test_dict_two
    #check that unequal values in dicts of

# Generated at 2022-06-12 22:58:40.291448
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict([(1, 1), (2, 2)]) == ImmutableDict({1: 1, 2: 2})
    assert ImmutableDict([(1, 1), (2, 2)]) != ImmutableDict({1: 1, 2: 3})
    assert ImmutableDict([(1, 1), (2, 2)]) != ImmutableDict({1: 1, 2: 2, 3: 3})


# Generated at 2022-06-12 22:58:51.155630
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    D1 = ImmutableDict({1: 'A', 2: 'B', 3: 'C'})
    D2 = ImmutableDict({1: 'A', 2: 'B', 3: 'C'})
    assert (D1 == D2)
    D3 = ImmutableDict({1: 'A', 2: 'B', 3: 'D'})
    assert (not D1 == D3)
    I1 = {1: 'A', 2: 'B', 3: 'C'}
    D4 = ImmutableDict(I1)
    assert (D1 == D4)
    assert (D4 == D4)
    D5 = ImmutableDict({1: 'A', 2: 'B', 3: 'C', 4: 'D'})
    assert (not D1 == D5)
    I2

# Generated at 2022-06-12 22:58:53.629665
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert not is_iterable('foo')
    assert not is_iterable(False)
    assert not is_iterable(True)
    assert not is_iterable(object())

# Generated at 2022-06-12 22:59:03.008870
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    '''Test __eq__ method of ImmutableDict class'''
    d1 = ImmutableDict({'a':1, 'b':2})
    d2 = ImmutableDict({'a':1, 'b':2})
    assert d1 == d2

    d3 = ImmutableDict({'a':1, 'b':2})
    assert d1 != d3

    d4 = ImmutableDict({'a':1, 'b':3})
    assert d3 != d4

    d5 = {'a':1, 'b':2}
    assert d1 != d5

    d6 = ImmutableDict({})
    d7 = {}
    assert d6 != d7

# Generated at 2022-06-12 22:59:13.625705
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    # Test to assert that two ImmutableDicts are equal by checking the equality of their keys and values.
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})

    # Test to assert that two ImmutableDicts are not equal if their keys are not the same
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'c': 2})

    # Test to assert that two ImmutableDicts are not equal if their values are not the same
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 3})

    # Test to assert that two ImmutableDicts are not equal if one of them has more items

# Generated at 2022-06-12 22:59:23.156324
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    immutable_dict_1 = ImmutableDict({1:'test1'})
    immutable_dict_2 = ImmutableDict({1:'test1'})
    immutable_dict_3 = ImmutableDict({1:'test3'})
    immutable_dict_4 = ImmutableDict({2:'test2'})

    # Test case 1: Two ImmutableDicts have matching key, value
    assert immutable_dict_1 == immutable_dict_2

    # Test case 2: Two ImmutableDicts have same key, different values
    assert immutable_dict_1 != immutable_dict_3

    # Test case 3: Two ImmutableDicts have different keys, same value
    assert immutable_dict_1 != immutable_dict_4

    # Test case 4: One of the dicts to compare is not an ImmutableDict type
    assert immutable_dict_

# Generated at 2022-06-12 22:59:33.774714
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # __eq__ should return True when compared to self
    test_dict = ImmutableDict({'a': 1, 'b': 2})
    assert test_dict == test_dict

    # __eq__ should return True if compared to ImmutableDict with same content
    test_dict2 = ImmutableDict({'a': 1, 'b': 2})
    assert test_dict == test_dict2

    # __eq__ should return False when compared to an equivalent MutableMapping
    test_dict2 = {'a': 1, 'b': 2}
    assert test_dict != test_dict2

    # __eq__ should return False when compared to something that's not a Mapping
    test_dict2 = 'foo'
    assert test_dict != test_dict2

    # __eq__ should return True when compared to ImmutableDict with

# Generated at 2022-06-12 22:59:42.305665
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict([('a', 1), ('b', 2)]) != ImmutableDict([('a', 1), ('b', 2)])
    assert ImmutableDict([('a', 1), ('b', 2)]) != ImmutableDict([('a', 1), ('b', 2)])
    assert ImmutableDict([('a', 1), ('b', 2)]) != ImmutableDict([('a', 1), ('b', 3)])
    assert ImmutableDict([('a', 1), ('b', 2)]) != ImmutableDict([('a', 1)])
    assert ImmutableDict([('a', 1), ('b', 2)]) != ImmutableDict([('a', 1), ('b', 2), ('c', 3)])

# Generated at 2022-06-12 22:59:49.373814
# Unit test for function is_iterable
def test_is_iterable():
    # Positional Arguments
    assert(is_iterable(None) is False)
    assert(is_iterable([]) is True)
    assert(is_iterable(()) is True)
    assert(is_iterable(MutableMapping()) is True)
    assert(is_iterable(str()) is False)
    assert(is_iterable(str()) is False)
    # Keyword Arguments
    assert(is_iterable(seq=None, include_strings=False) is False)
    assert(is_iterable(seq=[], include_strings=False) is True)
    assert(is_iterable(seq=(), include_strings=False) is True)
    assert(is_iterable(seq=MutableMapping(), include_strings=False) is True)

# Generated at 2022-06-12 22:59:58.763122
# Unit test for function is_iterable
def test_is_iterable():
    """Check that is_iterable works as expected"""
    class Test(object):
        def __iter__(self):
            yield 'A'
            yield 'B'
        def __getitem__(self, key):
            return None

    assert is_iterable(set([1, 2, 3]))
    assert is_iterable(['a', 'b', 'c'])
    assert is_iterable(Test())
    assert is_iterable(Test())
    assert is_iterable(ImmutableDict({'a': 1, 'b': 2, 'c': 3}))
    assert is_iterable('This is a string')

    assert not is_iterable(123)
    assert not is_iterable({ 'a' : 1, 'b' : 2})
    assert not is_iterable(True)

# Generated at 2022-06-12 23:00:18.690391
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(list())
    assert is_iterable(tuple())
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable(dict().keys())
    assert is_iterable(dict().values())
    assert is_iterable(dict().items())

    assert not is_iterable('')
    assert not is_iterable(1)
    assert not is_iterable(u'abc')
    assert not is_iterable(b'abc')
    assert not is_iterable(dict().iterkeys())



# Generated at 2022-06-12 23:00:21.627059
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    idict_1 = ImmutableDict({'a': 1, 'b': 2})
    idict_2 = ImmutableDict({'a': 1, 'b': 2})
    assert idict_1 == idict_2



# Generated at 2022-06-12 23:00:24.946065
# Unit test for function is_iterable
def test_is_iterable():

    assert is_iterable(['1', '2'])
    assert is_iterable((1, 2))
    assert is_iterable({'1': 1, '2': 2})
    assert is_iterable(set([1, 2]))
    assert not is_iterable(1)



# Generated at 2022-06-12 23:00:30.942554
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    x = ImmutableDict(a=1)
    assert x == ImmutableDict(a=1)
    assert x == {'a': 1}
    assert x != ImmutableDict(a=2)
    assert x != {'a': 2}
    assert x != {'a': 1, 'b': 2}
    assert x != ImmutableDict()
    assert x != {}
    assert x != 2
    assert x != [1]

# Generated at 2022-06-12 23:00:38.713203
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict()
    b = ImmutableDict()
    assert a == b

    a = ImmutableDict({'b': 2, 'a': 1})
    b = ImmutableDict({'a': 1, 'b': 2})
    c = ImmutableDict({'a': 1})
    d = ImmutableDict({'a': 2})
    e = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert a == b
    assert a != c
    assert a != d
    assert a != e

# Generated at 2022-06-12 23:00:45.414430
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2})
    b = ImmutableDict({'b': 2, 'a': 1})
    c = ImmutableDict({'a': 0, 'b': 2})
    d = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    e = {'a': 1, 'b': 2}
    f = a.union({'c': 3})
    g = a.difference({'a'})
    h = ImmutableDict({})
    i = 1

    assert a == b
    assert a != c
    assert a != d
    assert a != e
    assert d == f
    assert a != f
    assert a != g
    assert a != h
    assert a != i
    assert g != h

# Generated at 2022-06-12 23:00:56.110874
# Unit test for function is_iterable
def test_is_iterable():
    """
    Simple unit test to check is_iterable function
    """

    # check objects that can be iterated
    assert is_iterable([0, 1, 2])
    assert is_iterable((0, 1, 2))
    assert is_iterable({0, 1, 2})
    assert is_iterable({0: 0, 1: 1, 2: 2})
    assert is_iterable("012")

    # check objects that cannot be iterated
    assert not is_iterable(0)
    assert not is_iterable(None)
    assert not is_iterable(True)

    # check include_strings argument
    assert is_iterable("012", include_strings=True)
    assert not is_iterable("012")


# Generated at 2022-06-12 23:01:06.079965
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = ImmutableDict()
    dict2 = ImmutableDict()
    dict3 = ImmutableDict(key1="value1")
    dict4 = ImmutableDict(key1="value2")
    dict5 = ImmutableDict(key1="value1")
    dict6 = ImmutableDict(key1="value1")
    dict7 = ImmutableDict(key1="value2")
    dict8 = ImmutableDict(key2="value2")
    dict9 = dict()
    dict10 = dict(key1="value1")
    dict11 = dict(key1="value2")
    dict12 = {"key1": "value1"}

    assert dict1 == dict1
    assert dict2 == dict2
    assert dict3 == dict3
    assert dict4 == dict4

# Generated at 2022-06-12 23:01:16.305854
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    orig = ImmutableDict({'a': 'b', 'c': 'd'})
    same_dict = {'a': 'b', 'c': 'd'}
    same_ord_dict = {'c': 'd', 'a': 'b'}
    same_obj = ImmutableDict({'c': 'd', 'a': 'b'})
    diff_key = ImmutableDict({'a': 'b', 'c': 'e'})
    diff_key_type = ImmutableDict({'a': 'b', 5: 'd'})
    diff_val = ImmutableDict({'a': 'e', 'c': 'd'})
    diff_val_type = ImmutableDict({'a': 'b', 'c': 5})

# Generated at 2022-06-12 23:01:27.215537
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('abc') is False
    assert is_iterable(u'abc') is False
    assert is_iterable(b'abc') is False
    assert is_iterable(bytearray(b'abc')) is True
    assert is_iterable(['abc', 'def']) is True
    assert is_iterable(('abc', 'def')) is True
    assert is_iterable({'a': 'b', 'c': 'd'}) is True
    assert is_iterable(ImmutableDict(a='b', c='d')) is True
    assert is_iterable(set(['abc', 'def'])) is True
    assert is_iterable(range(1, 5)) is True
    assert is_iterable(iter(range(1, 5))) is True



# Generated at 2022-06-12 23:02:01.231419
# Unit test for function is_iterable
def test_is_iterable():
    test_objects = [
        '',
        'string',
        b'byte_string',
        [],
        ['element'],
        {},
        {'key': 'value'},
        (lambda a: a + 1),
        (lambda a: a + 1)(10),
        range(0),
        range(2),
    ]

    expected_results = [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        True,
        True
    ]

    actual_results = list(map(is_iterable, test_objects))
    assert expected_results == actual_results, "Expected: %s, Actual: %s" % (expected_results, actual_results)


# Generated at 2022-06-12 23:02:05.209367
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1])
    assert is_iterable((1,))
    assert is_iterable({1:2})
    assert is_iterable(set())
    assert is_iterable("")
    assert is_iterable("1")
    assert not is_iterable(1)

    assert is_iterable("", include_strings=True)
    assert is_iterable("1", include_strings=True)


# Generated at 2022-06-12 23:02:08.944020
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable([1, 2, 3])
    assert not is_iterable(1)
    assert not is_iterable('test')
    assert not is_iterable(None)
    assert not is_iterable(True)



# Generated at 2022-06-12 23:02:20.279730
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([0])
    assert is_iterable({'a': 1})
    assert is_iterable((0, 1))
    assert is_iterable(set([0, 1]))
    assert is_iterable(ImmutableDict(a=1))
    assert is_iterable(x for x in [0, 1])
    assert is_iterable(None) is False
    assert is_iterable(1) is False
    assert is_iterable(b'a') is False
    assert is_iterable(u'a') is False
    assert is_iterable([0], include_strings=True)
    assert is_iterable({'a': 1}, include_strings=True)
    assert is_iterable((0, 1), include_strings=True)

# Generated at 2022-06-12 23:02:28.777580
# Unit test for function is_iterable
def test_is_iterable():
    """Test cases for function is_iterable"""
    assert is_iterable([])
    assert is_iterable((1, 2))
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable(range(0, 10))
    assert is_iterable(text_type('test'))
    assert is_iterable(binary_type('test'))
    assert not is_iterable(1)
    assert not is_iterable('test')
    assert not is_iterable(object)
    assert not is_iterable(test_is_iterable)


# Generated at 2022-06-12 23:02:35.750115
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'key': 'value'}) == ImmutableDict({'key': 'value'})
    assert ImmutableDict({'key': 'value'}) == {'key': 'value'}
    assert {'key': 'value'} == ImmutableDict({'key': 'value'})
    assert ImmutableDict({'key': 'value'}) != {'key': 'value1'}
    assert ImmutableDict({'key': 'value'}) != {'key1': 'value'}
    assert ImmutableDict({'key': 'value'}) != 1
    assert ImmutableDict({'key': 'value'}) != None


# Generated at 2022-06-12 23:02:45.665688
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict()
    b = ImmutableDict({'a': 1, 'b': 2})
    c = ImmutableDict({'a': 3})
    d = ImmutableDict({'c': 3})
    e = ImmutableDict({'a': 1, 'b': 2})
    f = ImmutableDict({'b': 2, 'a': 1})
    g = {'c': 3}
    h = [1, 2, 3]

    assert a == ImmutableDict()
    assert b == e
    assert b == f
    assert not a == b
    assert not b == c
    assert not c == d
    assert not b == d
    assert not d == g
    assert not d == h

# Generated at 2022-06-12 23:02:50.008465
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Unit test for method __eq__ of class ImmutableDict
    """
    a = ImmutableDict({"foo": "bar"})
    a_clone = ImmutableDict(a)
    a2 = ImmutableDict({"foo": "bar2"})
    a3 = ImmutableDict({"foo2": "bar"})
    a4 = MutableMapping({"foo": "bar"})

    assert(a == a_clone)
    assert(a == a4)
    assert(a != a2)
    assert(a != a3)
    assert(a == a4)

# Generated at 2022-06-12 23:02:53.403048
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    x = ImmutableDict({'a': 1, 'b': 2})
    y = ImmutableDict({'a': 1, 'b': 2})
    z = ImmutableDict({'a': 1, 'b': 3})
    assert (x == y)
    assert not (x == z)


# Generated at 2022-06-12 23:03:03.585547
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(('a', 'b'))
    assert is_iterable([1, 2, 3])
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable(dict(a=1, b=2, c=3))
    assert is_iterable(dict([('a', 1), ('b', 2), ('c', 3)]))
    assert is_iterable(dict(zip(['a', 'b', 'c'], [1, 2, 3])))
    assert is_iterable(zip(['a', 'b', 'c'], [1, 2, 3]))
    assert is_iterable(xrange(10))
    assert is_iterable(('a', 'b'))
    assert is_iterable('abc')


# Generated at 2022-06-12 23:04:04.175660
# Unit test for function is_iterable
def test_is_iterable():
    """
    Test if is_iterable returns True for iterables and False for non iterable
    :return:
    """
    list_iterable = [1, 2]
    set_iterable = set([1, 2])
    dict_iterable = {"a": 1, "b": 2}
    generator_iterable = (i for i in xrange(3))
    string_iterable = "abcd"
    int_iterable = 1
    assert is_iterable(list_iterable)
    assert is_iterable(set_iterable)
    assert is_iterable(dict_iterable)
    assert is_iterable(generator_iterable)
    assert is_iterable(string_iterable)
    assert not is_iterable(int_iterable)



# Generated at 2022-06-12 23:04:06.574540
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    a = ImmutableDict({1: 'a'})
    b = ImmutableDict({1: 'a'})
    assert a == b



# Generated at 2022-06-12 23:04:13.524294
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    c = ImmutableDict({'a': 1, 'b': 2})
    assert a == b
    assert b == a
    assert a != c
    assert c != a
    assert c == ImmutableDict({'b': 2, 'a': 1})
    assert c != ImmutableDict({'b': 2, 'a': 1, 'c': 1})

# Generated at 2022-06-12 23:04:16.390854
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a = 1, b = 2) == ImmutableDict(b = 2, a = 1)
    assert ImmutableDict(a = 1, b = 2) != ImmutableDict(a = 1, c = 2)

# Generated at 2022-06-12 23:04:19.934871
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable("abc")
    assert is_iterable(u"abc")
    assert is_iterable("abc".split(" "))
    assert is_iterable([1,2])
    assert is_iterable((1,2))
    assert is_iterable({'a':1})
    assert not is_iterable(1)


# Generated at 2022-06-12 23:04:30.150429
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    tests = (
        (ImmutableDict({'A': 1}), ImmutableDict({'A': 1}), True),
        (ImmutableDict({'A': 1}), ImmutableDict({'B': 1}), False),
        (ImmutableDict({'A': 1}), ImmutableDict({'A': 1, 'B': 1}), False),
        (ImmutableDict({'A': 1}), '1', False),
    )
    for idict, other, expected_result in tests:
        result = (idict == other)
        message = 'Expected the result of idict == other to be {0} but got {1}' \
                  '\nidict: {2}\nother: {3}'

# Generated at 2022-06-12 23:04:33.229287
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    x = ImmutableDict({'a': 1, 'b': 2})
    y = ImmutableDict({'a': 1, 'b': 2})
    assert x == y
    assert y == x


# Generated at 2022-06-12 23:04:39.158395
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('abc')
    assert is_iterable(b'abc')
    assert is_iterable(['a', 'b', 'c'])
    assert is_iterable(('a', 'b', 'c'))
    assert is_iterable({'a': 1, 'b': 2, 'c': 3})
    assert not is_iterable(1)
    assert not is_iterable(1.0)
    assert not is_iterable(None)


# Generated at 2022-06-12 23:04:43.196689
# Unit test for function is_iterable
def test_is_iterable():
    class MyIterable(object):
        def __iter__(self):
            pass

    class MyNonIterable(object):
        pass

    class MyStringIterable(object):
        def __iter__(self):
            pass

        def __str__(self):
            pass

    assert is_iterable(MyIterable())
    assert is_iterable(MyNonIterable()) is False
    assert is_iterable(MyStringIterable()) is False
    assert is_iterable(MyStringIterable(), include_strings=True)


# Generated at 2022-06-12 23:04:49.810492
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id1 = ImmutableDict(a=1)
    id2 = ImmutableDict(a=1)
    assert(id1 == id2)
    assert(not id1 != id2)
    assert(not id1 == dict(a=1))
    assert(id1 != dict(a=1))
    assert(not id1 == [1])
    assert(id1 != [1])
    assert(not id1 == 1)
    assert(id1 != 1)
    assert(not id1 == 'x')
    assert(id1 != 'x')
    assert(not id1 == None)
    assert(id1 != None)
