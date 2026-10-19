

# Generated at 2022-06-12 22:56:09.316749
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    """Unit test for method difference of class ImmutableDict"""
    original = ImmutableDict({'a':1, 'b':2, 'c':3})
    assert original == original.difference([])
    assert ImmutableDict({'a':1, 'c':3}) == original.difference(['b'])
    assert ImmutableDict({'a':1}) == original.difference(['b', 'c'])
    assert ImmutableDict({'c':3}) == original.difference(['a', 'b'])
    assert ImmutableDict({}) == original.difference(['a', 'b', 'c'])



# Generated at 2022-06-12 22:56:18.667189
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    b = a.difference(['a', 'c', 'f'])
    assert len(b) == 2, 'Expected b to be of length 2, got %d' % len(b)
    assert 'b' in b, 'Expected b to contain key b'
    assert b['b'] == 2, 'Expeced value of key b in b to be 2, got %s' % str(b['b'])
    assert 'd' in b, 'Expected b to contain key d'
    assert b['d'] == 4, 'Expeced value of key d in b to be 4, got %s' % str(b['d'])


# Generated at 2022-06-12 22:56:29.386211
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    list_of_dicts = [{"a": "A", "b": "B"}, {"c": "C", "d": "D"}, {"e": "E", "f": "F"}]
    immutable_dict1 = ImmutableDict(list_of_dicts[0])
    immutable_dict2 = immutable_dict1.union(list_of_dicts[1])
    immutable_dict3 = immutable_dict2.union(list_of_dicts[2])
    immutable_dict4 = immutable_dict1.difference(list_of_dicts[1])
    immutable_dict5 = immutable_dict3.difference(list_of_dicts[1])
    print(immutable_dict1)
    print(immutable_dict2)
    print(immutable_dict3)

# Generated at 2022-06-12 22:56:37.874401
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1}) != ImmutableDict({'a': 1, 'b': 1})
    assert ImmutableDict({'a': 1}) != {'a': 1}
    assert ImmutableDict({'a': 1, 'b': 2}) != {'a': 1, 'b': 2}
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'b': 2, 'a': 1})

# Generated at 2022-06-12 22:56:43.376497
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict(ab=1, cd=2, ef=3, gh=4)
    b = ImmutableDict(ab=1, cd=2, ef=3, gh=4)
    c = ImmutableDict(ab=2, cd=3, ef=4, gh=5)
    d = 'ab'

    assert a == b
    assert not a == c
    assert not a == d

# Generated at 2022-06-12 22:56:54.792123
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    # Test if the ImmutableDict.difference() works as expected
    # if subtractive_iterable is a normal list
    aDict = ImmutableDict({'a':1, 'b':2, 'c':3})
    aList = ['b', 'c']
    expected = ImmutableDict({'a':1})
    assert aDict.difference(aList) == expected

    # Test if the ImmutableDict.difference() works as expected
    # if subtractive_iterable is a normal list
    aDict = ImmutableDict({'a':1, 'b':2, 'c':3})
    aList = ['b', 'c', 'd']
    expected = ImmutableDict({'a':1})
    assert aDict.difference(aList) == expected

    # Test if

# Generated at 2022-06-12 22:56:59.577845
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    dictionary = ImmutableDict({'one': 1, 'two': 2, 'three': 3})
    one = dictionary.difference(['one'])
    assert one.__repr__() == 'ImmutableDict({\'two\': 2, \'three\': 3})'
    assert one.__eq__(ImmutableDict({'two': 2, 'three': 3}))



# Generated at 2022-06-12 22:57:02.081591
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from nose.tools import assert_true, assert_false
    d1 = ImmutableDict(attr=None, other=None)
    d2 = ImmutableDict(attr=None, other=None)
    assert_true(d1 == d2)
    d3 = ImmutableDict(attr=None, otherother=None)
    assert_false(d1 == d3)



# Generated at 2022-06-12 22:57:13.055466
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(['1', '2'])
    assert is_iterable((1, 2))
    assert is_iterable((e for e in range(10)))
    assert is_iterable({})
    assert is_iterable({'key': 'value'})
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert not is_iterable(True)
    assert is_iterable('string') is False
    assert is_iterable('string', include_strings=True) is True
    assert is_iterable(u'string') is False
    assert is_iterable(u'string', include_strings=True) is True
    assert is_iterable(bytes()) is False

# Generated at 2022-06-12 22:57:20.710952
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    base = ImmutableDict({'a':1, 'b':2, 'c':3, 'd':4})
    # On set subtraction, the key 'd' will get removed
    removed = base.difference(set(['a','c','d']))
    if not removed == ImmutableDict({'b':2}):
        raise AssertionError('Expected %s, Got %s' % (ImmutableDict({'b':2}), removed))

    # On list subtraction, the key 'c' will get removed
    removed = base.difference(['a','c','d'])

# Generated at 2022-06-12 22:57:29.413108
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict({'a': '1', 'b': '2', 'c': '3', 'd': '4'})
    removed = original.difference(['a', 'c'])
    assert removed == {'b': '2', 'd': '4'}



# Generated at 2022-06-12 22:57:39.161538
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    from ansible.module_utils.common._collections_compat import Mapping
    from copy import deepcopy
    # Init a simple dict
    test_dict = Mapping({'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3', 'key_4': 'value_4'})
    # Difference should return dict with key_1, key_2 and key_3 if subtractive_iterable is [key_4]
    subtractive_iterable = ['key_4']
    test_dict_difference = deepcopy(test_dict)
    test_dict_difference = ImmutableDict(test_dict_difference).difference(subtractive_iterable)
    assert len(test_dict_difference) == 3

# Generated at 2022-06-12 22:57:42.412750
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    """Check if ImmutableDict.difference is working correctly."""

    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}).difference(['a', 'b']) == ImmutableDict({'c': 3})



# Generated at 2022-06-12 22:57:45.588368
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    dictionary = ImmutableDict(a=1, b=2, c=3)
    to_remove = ('b', 'd')

    dictionary = dictionary.difference(to_remove)
    assert dictionary == ImmutableDict(a=1, c=3)

# Generated at 2022-06-12 22:57:50.892556
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict([('key1', 'val1'), ('key2', 'val2')])
    d2 = ImmutableDict([('key2', 'val2'), ('key1', 'val1')])
    d3 = ImmutableDict([('key1', 'val1')])
    d4 = ImmutableDict([('key1', 'val2'), ('key2', 'val2')])
    assert d1 == d2
    assert d1 != d3
    assert d1 != d4
    assert d2 != d3
    assert d3 != d4

# Generated at 2022-06-12 22:57:56.088109
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(list())
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable((x for x in range(10)))
    assert is_iterable(xrange(10))
    assert is_iterable([1, 2])
    assert not is_iterable(0)


# Generated at 2022-06-12 22:58:00.300842
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    a = ImmutableDict(one=1, two=2, three=3, four=4, five=5)
    b = a.difference(['one', 'four'])
    c = ImmutableDict(two=2, three=3, five=5)
    assert b == c

# Generated at 2022-06-12 22:58:05.023707
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable("a") is True
    assert is_iterable("a", include_strings=False) is False
    assert is_iterable("a", include_strings=True) is True

    assert is_iterable([1]) is True
    assert is_iterable({1:1}) is True

    assert is_iterable(1) is False

    assert is_iterable(is_iterable) is False
    assert is_iterable(is_iterable, include_strings=True) is False


# Generated at 2022-06-12 22:58:15.927629
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id1 = ImmutableDict(a='1', b='2', c='3')
    id2 = ImmutableDict(a='1', b='2', c='3')
    assert id1 == id2
    # Compare ImmutableDict with a MutableDict
    id3 = ImmutableDict(a=1, b='2', c='3')
    md1 = {'a': 1, 'b': '2', 'c': '3'}
    assert id3 == md1
    # Compare ImmutableDict with a dict
    dict1 = dict(a=1, b='2', c='3')
    assert id3 == dict1
    # Compare ImmutableDict with a list
    list1 = ['a', 'b', 'c']

# Generated at 2022-06-12 22:58:26.932142
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(1)
    assert not is_iterable(dict())
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(dict().keys())
    assert is_iterable(dict().values())
    assert is_iterable(dict().items())
    assert is_iterable((i for i in range(3)))
    assert is_iterable(iter([1, 2, 3]))
    assert is_iterable("abc")
    #
    assert not is_iterable(1, include_strings=True)
    assert not is_iterable(dict(), include_strings=True)
    assert is_iterable([], include_strings=True)
    assert is_iterable(set(), include_strings=True)

# Generated at 2022-06-12 22:58:45.303069
# Unit test for function is_iterable
def test_is_iterable():
    """Test function is_iterable"""
    # Tests for is_iterable
    assert is_iterable([]) == True  # Test for list
    assert is_iterable(()) == True  # Test for tuple
    assert is_iterable(set()) == True  # Test for set
    assert is_iterable(dict()) == True  # Test for dict
    assert is_iterable('abc') == False  # Test for string
    assert is_iterable(b'abc') == False  # Test for bytes
    assert is_iterable(u'abc') == False  # Test for unicode
    assert is_iterable(1) == False  # Test for int


# Generated at 2022-06-12 22:58:54.848655
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'apple': 1, 'pear': 2, 'orange': 3, 'grape': 4})

    assert a == a
    assert a == {'apple': 1, 'pear': 2, 'orange': 3, 'grape': 4}
    assert a == dict(zip(['apple', 'pear', 'orange', 'grape'], [1, 2, 3, 4]))
    assert not a == {'pear': 2, 'apple': 1, 'orange': 3, 'grape': 4}
    assert not a == {'apple': 1, 'pear': 2, 'orange': 3, 'grape': 4, 'banana': 5}
    assert a != 'apple'
    assert a != 123
    assert a != [1, 2, 3]

# Generated at 2022-06-12 22:59:01.166391
# Unit test for function is_iterable
def test_is_iterable():

    class TestNotIterable(object):
        pass

    class TestIterable(object):
        def __iter__(self):
            pass

    assert is_iterable([]) is True
    assert is_iterable(TestIterable()) is True

    assert is_iterable(None) is False
    assert is_iterable(123) is False
    assert is_iterable(set()) is False
    assert is_iterable(TestNotIterable()) is False



# Generated at 2022-06-12 22:59:11.800322
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    imm_a = ImmutableDict({"a": 1})
    imm_b = ImmutableDict({"a": 1})
    imm_c = ImmutableDict({"a": 2})
    imm_d = ImmutableDict({"b": 1})
    imm_e = ImmutableDict()
    imm_f = ImmutableDict({"a": 2, "b": 1})
    assert (imm_a == imm_b)
    assert (imm_a == imm_b)
    assert (not (imm_a == imm_c))
    assert (not (imm_a == imm_d))
    assert (not (imm_a == imm_e))
    assert (not (imm_a == imm_f))


# Generated at 2022-06-12 22:59:19.081197
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict([('a', 1), ('b', 2)])
    b = ImmutableDict([('b', 2), ('a', 1)])
    assert a == b
    assert hash(a) == hash(b)
    assert a == a
    assert hash(a) == hash(a)
    assert a == dict([('a', 1), ('b', 2)])
    assert a != dict([('a', 1), ('b', 3)])
    assert a != dict([('a', 1)])
    assert a != dict([('a', 1), ('b', 2), ('c', 3)])
    assert a != set(['a', 'b'])
    assert a != ['a', 'b']

    try:
        assert a == 1
    except TypeError:
        pass


# Generated at 2022-06-12 22:59:30.036909
# Unit test for function is_iterable
def test_is_iterable():
    """Test the is_iterable function."""
    import collections

    class NonIterable(object):
        pass

    class Iterable(collections.Iterator):
        pass

    class NotIterable(Iterable):
        def __iter__(self):
            raise AttributeError

    class Iterator(collections.Iterator):
        def __next__(self):
            raise StopIteration

    class IterableGenerator(object):
        def __iter__(self):
            yield True

    class IteratorGenerator(IterableGenerator):
        def __next__(self):
            raise StopIteration

    class IteratorGeneratorSequence(IterableGenerator):
        def __getitem__(self, x):
            raise StopIteration

    class Sequence(collections.Sequence):
        def __len__(self):
            return

# Generated at 2022-06-12 22:59:38.685710
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    assert d == {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    assert d == ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    assert d == ImmutableDict({'b': 2, 'a': 1, 'c': 3, 'd': 4})
    assert d == ImmutableDict({'b': 2, 'c': 3, 'a': 1, 'd': 4})
    assert d == ImmutableDict({'b': 2, 'c': 3, 'd': 4, 'a': 1})

# Generated at 2022-06-12 22:59:43.631268
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # the same dicts are equal:
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2)
    assert ImmutableDict(b=2, a=1) == ImmutableDict(a=1, b=2)

    # the same dicts are equal even if they have different content types:
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1.0, b=2)

    # different dicts are not equal:
    assert not (ImmutableDict(a=1, b=2) == ImmutableDict(c=9))

    # dict does not equal non-dict:
    assert not (ImmutableDict(a=1, b=2) == "a string")

# Generated at 2022-06-12 22:59:46.227529
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert not is_iterable(dict())
    assert is_iterable(dict().keys())



# Generated at 2022-06-12 22:59:51.811049
# Unit test for function is_iterable
def test_is_iterable():
    assert(is_iterable([1, 2, 3]) is True)
    assert(is_iterable({1, 2, 3}) is True)
    assert(is_iterable((1, 2, 3)) is True)
    assert(is_iterable(1) is False)
    assert(is_iterable(set()) is True)
    assert(is_iterable(frozenset()) is True)
    assert(is_iterable(dict()) is True)



# Generated at 2022-06-12 23:00:19.076664
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Create a dictionary to test equality
    original_dictionary = {'key1': "value1",
                           'key2': "value2"}

    # Create the ImmutableDict from the dictionary
    immutable_dictionary = ImmutableDict(original_dictionary)

    # Create a dictionary that is the same as original_dictionary for testing equality
    identical_dictionary = original_dictionary.copy()

    # Create a dictionary that is different than original_dictionary for testing non-equality
    different_dictionary = {'key1': "different value",
                            'key3': "value3"}

    # Confirm that the ImmutableDict is equal to a dictionary that is the same
    assert immutable_dictionary == identical_dictionary

    # Confirm that the ImmutableDict is not equal to a dictionary that is different
    assert immutable_

# Generated at 2022-06-12 23:00:24.213508
# Unit test for function is_iterable
def test_is_iterable():
    # Test different types of iterables
    class Test:
        def __init__(self, value=None):
            self.value = value

        def __iter__(self):
            return iter(self.value)

    t = Test(range(5))
    assert is_iterable(t)

    # Test non-iterables
    for i in (5, 5.5, {"a": "b"}):
        assert not is_iterable(i)



# Generated at 2022-06-12 23:00:34.688974
# Unit test for function is_iterable
def test_is_iterable():
    list1 = [1, 2, 3]
    list2 = []
    set1 = set([1, 2, 2, 3])
    tuple1 = (1, 2, 3)
    dict1 = {}
    dict2 = {'1': 1, '2': 2}
    string1 = 'abc'
    int1 = 1
    float1 = 1.0

    assert is_iterable(list1)
    assert is_iterable(list2)
    assert is_iterable(set1)
    assert is_iterable(tuple1)
    assert is_iterable(dict1)
    assert is_iterable(dict2)
    assert is_iterable(string1)
    assert not is_iterable(int1)
    assert not is_iterable(float1)



# Generated at 2022-06-12 23:00:42.405922
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable"""
    assert is_iterable([])
    assert is_iterable(dict())
    assert is_iterable(set())
    assert is_iterable((None,))
    assert is_iterable('')
    assert is_iterable(1)
    assert is_iterable(['a', 'b'])
    assert is_iterable({'a': 'b'})
    assert is_iterable(set(['a', 'b']))
    assert is_iterable((x for x in range(1)))

    assert not is_iterable('abc')
    assert not is_iterable(1)


# Generated at 2022-06-12 23:00:50.340875
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Basic unit test for method __eq__ of class ImmutableDict."""
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    assert d1 == d2

    d3 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert not d3 == d2

    d4 = ImmutableDict({'a': 1, 'b': 4})
    assert not d4 == d2



# Generated at 2022-06-12 23:01:01.347162
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(EMPTY_DICT) is True
    assert is_iterable(EMPTY_LIST) is True
    assert is_iterable(EMPTY_SET) is True
    assert is_iterable(EMPTY_TUPLE) is True
    assert is_iterable(NON_EMPTY_DICT) is True
    assert is_iterable(NON_EMPTY_LIST) is True
    assert is_iterable(NON_EMPTY_SET) is True
    assert is_iterable(NON_EMPTY_TUPLE) is True
    assert is_iterable(STRING) is True
    assert is_iterable(INTEGER) is False
    assert is_iterable(BOOL) is False
    assert is_iterable(NONE) is False

# Generated at 2022-06-12 23:01:09.354851
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for the function is_iterable."""
    def test_positive(input_sequence):
        """Test the positive case"""
        # pylint: disable=unused-argument
        assert is_iterable(input_sequence)

    def test_negative(input_sequence):
        """Test the negative case"""
        # pylint: disable=unused-argument
        assert not is_iterable(input_sequence)

    # Lists
    test_positive([])
    test_positive([1, 2, 3])

    # Tuples
    test_positive(())
    test_positive((1, 2, 3))

    # Dictionaries
    test_positive({})
    test_positive({'A': 1, 'B': 2, 'C': 3})

    # Stringifyable
    test_positive(True)
   

# Generated at 2022-06-12 23:01:19.689919
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test the method ImmutableDict.__eq__."""
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'b': 2, 'a': 1})
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})

    # Comparison with Mapping
    assert ImmutableDict({'a': 1, 'b': 2}) == {'a': 1, 'b': 2}
    assert ImmutableDict({'a': 1, 'b': 2}) == {'b': 2, 'a': 1}

# Generated at 2022-06-12 23:01:26.642317
# Unit test for function is_iterable
def test_is_iterable():
    # This is a list
    assert(is_iterable([1, 2, 3, 4]))
    # This is a set
    assert(is_iterable({1, 2, 3, 4}))
    # This is a dictionary
    assert(is_iterable({1:2, 3:4}))
    # This is a string
    assert(is_iterable('1234'))
    # This is an integer
    assert(not is_iterable(1))


# Generated at 2022-06-12 23:01:33.665435
# Unit test for function is_iterable
def test_is_iterable():
    # is_iterable returns true on lists and tuples
    assert is_iterable(['a', 'b', 'c']) == True
    assert is_iterable(('a', 'b', 'c')) == True
    # is_iterable returns false on strings
    assert is_iterable('abcdef') == False
    assert is_iterable(u'abcdef') == False
    # is_iterable returns false on integers
    assert is_iterable(45) == False
    # is_iterable returns false on floats
    assert is_iterable(0.00023) == False


# Generated at 2022-06-12 23:02:15.348517
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert is_iterable([])
    assert is_iterable([1,2,3])
    assert is_iterable({})
    assert is_iterable({'a':'b'})
    assert is_iterable(set())
    assert is_iterable(set([1,2,3]))
    assert is_iterable(1)
    assert is_iterable(1.5)
    assert is_iterable(u'this is a string')
    assert is_iterable(b'bytes string')


# Generated at 2022-06-12 23:02:26.554386
# Unit test for function is_iterable
def test_is_iterable():
    seq1 = list()
    seq2 = [0]
    seq3 = set()
    seq4 = frozenset()
    seq5 = dict()
    seq6 = (True,)
    seq7 = 'string'
    seq8 = b'bytestring'
    seq9 = range(0)
    seq10 = range(5)
    seq11 = (x for x in range(5))
    seq12 = True
    seq13 = False
    seq14 = 123

    assert is_iterable(seq1) is True
    assert is_iterable(seq2) is True
    assert is_iterable(seq3) is True
    assert is_iterable(seq4) is True
    assert is_iterable(seq5) is True
    assert is_iterable(seq6) is True
    assert is_iterable

# Generated at 2022-06-12 23:02:35.447583
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert not is_iterable("Ansible")
    assert not is_iterable("")
    assert not is_iterable(b"Ansible")
    assert not is_iterable(b"")
    assert not is_iterable(1)
    assert not is_iterable(0)
    assert is_iterable([1,2,3])
    assert is_iterable((1,2,3))
    assert is_iterable(set([1,2,3]))
    assert is_iterable({'a': 1, 'b': 2, 'c': 3})
    assert is_iterable(CountingWrapper())
    assert is_iterable('Ansible', include_strings=True)
    assert is_iterable('', include_strings=True)

# Generated at 2022-06-12 23:02:44.574816
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])  # This is true because [] is an iterable
    assert is_iterable({})  # This is true because {} is an iterable
    assert is_iterable("")  # This is true because "" is an iterable
    assert not is_iterable("")  # This is false because '' is an iterable
    assert is_iterable((1,))  # This is true because (1,) is an iterable
    assert is_iterable(x for x in range(5))  # This is true because generator is an iterable
    assert is_iterable(xrange(5))  # This is true because xrange is an iterable



# Generated at 2022-06-12 23:02:49.563485
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable((1, 2))
    assert not is_iterable(1)
    assert is_iterable([1, 2])
    assert not is_iterable([1, 2], include_strings=False)
    assert not is_iterable((1, 2), include_strings=False)
    assert is_iterable((1, 2), include_strings=True)


# Generated at 2022-06-12 23:02:57.293850
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([], include_strings=True)
    assert not is_iterable(None, include_strings=True)
    assert is_iterable({}, include_strings=True)
    assert is_iterable(set(), include_strings=True)
    assert is_iterable('test', include_strings=True)
    assert is_iterable(b'123', include_strings=True)
    assert not is_iterable(123, include_strings=True)
    assert not is_iterable(None, include_strings=False)
    assert is_iterable('test', include_strings=False)
    assert is_iterable(b'123', include_strings=False)



# Generated at 2022-06-12 23:03:05.370465
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({"a": 1, "b": 2, "c": 3})
    d2 = ImmutableDict({"a": 1, "b": 2, "c": 3})
    assert d1 == d2

    d2 = ImmutableDict({"a": 1, "b": 1, "c": 3})
    assert d1 != d2

    d2 = {"a": 1, "b": 2, "c": 3}
    assert d1 != d2

    d2 = frozenset(d2.items())
    assert d1 != d2



# Generated at 2022-06-12 23:03:08.794011
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('hello')
    assert is_iterable([1, 2])
    assert not is_iterable(1)
    assert is_iterable({'test': 'value'})
    assert not is_iterable(None)


# Generated at 2022-06-12 23:03:13.207274
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable((e for e in range(3)))
    assert is_iterable(set([3, 2, 1]))
    assert is_iterable(dict(a=1, b=2, c=3))
    assert is_iterable(range(3))
    assert not is_iterable(42)



# Generated at 2022-06-12 23:03:19.765176
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict_a = {'a': 1, 'b': 2, 'c': 3}
    dict_b = {'a': 1, 'b': 2, 'c': 3}
    dict_c = {'a': 1, 'b': 2}
    dict_d = {'a': 1, 'b': 2, 'c': 1}

    ImmutableDict_a = ImmutableDict(dict_a)
    ImmutableDict_b = ImmutableDict(dict_b)
    ImmutableDict_c = ImmutableDict(dict_c)
    ImmutableDict_d = ImmutableDict(dict_d)

    assert ImmutableDict_a == ImmutableDict_b
    assert ImmutableDict_a != ImmutableDict_c
    assert ImmutableDict_a != ImmutableD

# Generated at 2022-06-12 23:04:40.012187
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) == ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) != ImmutableDict({'a': 1, 'b': 2})
    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) != ImmutableDict({'a': 1, 'c': 2, 'b': 3})
    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) != ImmutableDict({'a': 1, 'b': 2, 'c': 4})

# Generated at 2022-06-12 23:04:48.436497
# Unit test for function is_iterable
def test_is_iterable():

    # Lists
    assert is_iterable([]) is True
    assert is_iterable([1, 2, 3]) is True

    # Generators
    assert is_iterable(range(5)) is True
    assert is_iterable(xrange(5)) is True
    assert is_iterable(iter([1, 2, 3])) is True

    # Tuples
    assert is_iterable(()) is True
    assert is_iterable((1, 2, 3)) is True

    # Dictionaries
    assert is_iterable({}) is True
    assert is_iterable({1: 2, 3: 4}) is True

    # Sets
    assert is_iterable({1, 2, 3}) is True
    assert is_iterable(set()) is True

# Generated at 2022-06-12 23:04:55.754048
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    class Test(object):
        def __eq__(self, other):
            return True

    t = Test()
    d = {}
    d[t] = None
    assert d[t] == None
    d = ImmutableDict(d)
    # ImmutableDict with the same keys must be equal
    assert d[t] == d[t]
    assert d == d
    # ImmutableDict with different keys must not be equal
    assert d != ImmutableDict({t: None, 1: 2})
    # ImmutableDict must not be equal to other types
    assert d != {t: None}
    assert d != 1
    assert d != '123'
    assert d != True
    assert d != False
    assert d != None
    assert d != [1, 2]

# Generated at 2022-06-12 23:05:03.769872
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(tuple())
    assert is_iterable((x for x in range(3)))
    assert is_iterable(set())
    assert is_iterable('')
    assert not is_iterable(tuple(), include_strings=False)
    assert not is_iterable(set(), include_strings=False)
    assert is_iterable({'a': 1, 'b': 2})
    assert is_iterable(1)
    assert is_iterable(1.1)



# Generated at 2022-06-12 23:05:08.371810
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    d3 = ImmutableDict({'b': 2, 'a': 1})

    assert(d1 == d2)
    assert(d1 == d3)

# Generated at 2022-06-12 23:05:14.182044
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() != ImmutableDict(a=1)
    assert ImmutableDict(a=1) != ImmutableDict(a=2)
    assert ImmutableDict(b=1) != ImmutableDict(a=1)
    assert ImmutableDict(b=1) != ImmutableDict(a=1, b=2)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(b=1, a=2)
    assert ImmutableDict(a=1) == ImmutableDict(a=1)
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2)

# Generated at 2022-06-12 23:05:20.531416
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({1: 'a', 2: 'b'}) == {1: 'a', 2: 'b'}
    assert ImmutableDict({1: 'a', 2: 'b'}) == ImmutableDict({1: 'a', 2: 'b'})
    assert ImmutableDict({1: 'a', 2: 'b'}) == ImmutableDict({2: 'b', 1: 'a'})
    assert ImmutableDict({1: 'a', 2: 'b'}) != {1: 'a', 2: 'c'}
    assert ImmutableDict({1: 'a', 2: 'b'}) != ImmutableDict({1: 'c', 2: 'b'})

# Generated at 2022-06-12 23:05:28.571722
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    x = ImmutableDict({"a": 1})
    y = ImmutableDict({"a": 2})
    # Idempotence
    assert(x == x)
    # Reflexivity
    assert(x != y)
    assert(y != x)
    # Symmetry
    y = ImmutableDict({"a": 1})
    assert(x == y)
    assert(y == x)
    # Transitivity
    z = ImmutableDict({"a": 1})
    assert(x == z)
    assert(y == z)


# Generated at 2022-06-12 23:05:34.362076
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(1) is False
    assert is_iterable('str') is True
    assert is_iterable([1,2,3]) is True
    assert is_iterable((1,2,3)) is True
    assert is_iterable(set([1, 2, 3])) is True
    assert is_iterable({1: 'a', 2: 'b', 3: 'c'}) is True



# Generated at 2022-06-12 23:05:36.367449
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})