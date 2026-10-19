

# Generated at 2022-06-12 22:56:11.013057
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable(['foo', 'bar'])
    assert is_iterable((1, 2))
    assert is_iterable(x for x in range(1, 10))
    assert is_iterable(dict(a=1, b=2))
    assert is_iterable(set(['foo', 'bar']))
    assert is_iterable(u'foobar')
    assert not is_iterable('foobar')
    assert not is_iterable('foobar'.upper())
    assert not is_iterable(u'foobar'.upper())
    assert not is_iterable('foobar'.lower())
    assert not is_iterable(u'foobar'.lower())
    assert not is_iterable(1234)


# Generated at 2022-06-12 22:56:20.861972
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method ``__eq__`` of class :class:`ImmutableDict`."""
    # two empty ImmutableDicts are equal
    a = ImmutableDict()
    b = ImmutableDict()
    assert a == b

    # two dictionaries with the same keys and values are equal
    a = ImmutableDict({'a': 'b', 'c': 'd'})
    b = ImmutableDict({'c': 'd', 'a': 'b'})
    assert a == b

    # two dictionaries with the same keys and different values are not equal
    a = ImmutableDict({'a': 'b', 'c': 'd'})
    b = ImmutableDict({'a': '1', 'c': '2'})
    assert not (a == b)
    assert a != b



# Generated at 2022-06-12 22:56:29.190919
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # test_equals_to_hashable_non_iterable
    assert ImmutableDict() != 1
    # test_equals_to_hashable_iterable_not_dict
    assert ImmutableDict() != []
    # test_equals_to_immutabledict_not_equal
    assert ImmutableDict() != ImmutableDict({1: 1})
    # test_equals_to_immutabledict_equal
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict({1: 1}) == ImmutableDict({1: 1})


# Generated at 2022-06-12 22:56:33.900364
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({"a": 1, "b": 2})

    assert(d1 == d1)
    assert(d1 == ImmutableDict({'a': 1, 'b': 2}))
    assert(d1 != ImmutableDict({'a': 1, 'b': 3}))
    assert(d1 != 'notADict')

# Generated at 2022-06-12 22:56:42.708736
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test of ImmutableDict.__eq__.

    This unit test tests all possible conditions which may arise
    when the method __eq__ is called.
    """

    # Create an ImmutableDict (self) and a standard dict (other)
    self = ImmutableDict({'key1': 1, 'key2': 2})
    other = {'key1': 1, 'key2': 2}

    # Create a list (other)
    other = [1]

    # Create an ImmutableDict (other)
    other = ImmutableDict({'key1': 1, 'key2': 2})
    assert self.__eq__(other) is True

    # Create an ImmutableDict (other) with different values
    other = ImmutableDict({'key1': 2, 'key2': 2})
    assert self

# Generated at 2022-06-12 22:56:53.359084
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    ref_dict = ImmutableDict({1:2, 2:3})
    dict1 = ImmutableDict({1:2, 2:3})
    dict2 = ImmutableDict({1:2, 3:4})
    dict3 = dict2
    dict4 = dict({1:2, 3:4})
    dict5 = {1:2, 3:4}
    assert ref_dict == dict1
    assert ref_dict != dict2
    assert dict2 == dict3
    assert dict2 == dict4
    assert dict2 == dict5
    # ref_dict != dict1
    # ref_dict == dict2
    # dict2 == dict3
    # dict2 == dict4
    # dict2 == dict5


# Generated at 2022-06-12 22:56:55.990416
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable('Foo')
    assert is_iterable([])
    assert is_iterable({})
    assert not is_iterable(False)



# Generated at 2022-06-12 22:57:00.521456
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    init_dict = ImmutableDict({'a':'a_value', 'b':'b_value', 'c':'c_value', 'd':'d_value'})
    subt_dict = {'a', 'b', 'd'}
    diff_dict = init_dict.difference(subt_dict)
    assert diff_dict == {'c':'c_value'}

# Generated at 2022-06-12 22:57:06.808254
# Unit test for function is_iterable
def test_is_iterable():
    class IterableButNotSequence(object):
        def __iter__(self):
            return iter([])

    class NotIterable(object):
        pass

    assert is_iterable('')
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(iter([]))
    assert is_iterable(IterableButNotSequence())

    assert not is_iterable(NotIterable)
    assert not is_iterable(None)
    assert not is_iterable(5)
    assert not is_iterable(5.0)
    assert not is_iterable(NotIterable())

    assert is_iterable('')
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(iter([]))
    assert is_

# Generated at 2022-06-12 22:57:16.865316
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    from ansible.module_utils.common._collections_compat import Mapping, MutableMapping

    def assert_not_included(original_mapping, subtractive_iterable):
        assert type(original_mapping) == ImmutableDict
        assert is_iterable(subtractive_iterable)
        for key in subtractive_iterable:
            assert key not in original_mapping

    def assert_included(original_mapping, subtractive_iterable):
        assert type(original_mapping) == ImmutableDict
        assert is_iterable(subtractive_iterable)
        for key in subtractive_iterable:
            assert key in original_mapping

    def assert_pairs_included(original_mapping, subtractive_iterable):
        assert type(original_mapping) == Imm

# Generated at 2022-06-12 22:57:21.707132
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'a': 1, 'b': 2, 'c': 3})

    assert(a == b)


# Generated at 2022-06-12 22:57:24.934771
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    dict1 = ImmutableDict({'A': 1, 'B': 2, 'C': 3})
    dict2 = dict1.difference(['A', 'B'])
    assert dict2 == {'C': 3}

# Generated at 2022-06-12 22:57:35.130730
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    # Test the case when given hashable not ImmutableDict
    # and Exception should be raised
    assert ImmutableDict({}).__eq__(0) == False

    # Test the case when given ImmutableDict
    # and hash should be equal
    a = ImmutableDict({1:1, 2:2})
    b = ImmutableDict({1:1, 2:2})
    assert (a.__eq__(b) == True)

    # Test the case when given hashable not ImmutableDict
    # and hash should not be equal
    a = ImmutableDict({1:1, 2:2})
    b = ImmutableDict({1:'a', 2:'b'})
    assert (a.__eq__(b) == True)

    # Test the case when exception should be raised
    # as hash

# Generated at 2022-06-12 22:57:41.948624
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert not is_iterable([])
    assert is_iterable((1, 2, 3))
    assert not is_iterable((1,)) # A tuple with one element is not iterable
    assert is_iterable([1, 2, 3], include_strings=True)
    assert is_iterable((1, 2, 3), include_strings=True)
    assert is_iterable('abc', include_strings=True)
    assert is_iterable(b'abc', include_strings=True)


# Generated at 2022-06-12 22:57:50.331852
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    # hashing of lists, tuples and dicts is defined in python 2.7, but python 2.6 did not have it implemented.
    # This is a minimum implementation that passes the tests for a list, tuple and dict.
    # See: https://stackoverflow.com/questions/39492682/cant-use-hashing-in-python-2-6
    class MinimalHashableMapping(Mapping, Hashable):
        def __init__(self, *args, **kwargs):
            self._store = dict(*args, **kwargs)

        def __getitem__(self, key):
            return self._store[key]

        def __iter__(self):
            return self._store.__iter__()

        def __len__(self):
            return self._store.__len__()


# Generated at 2022-06-12 22:58:00.202107
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.module_utils.six import PY3
    # Test __eq__ of ImmutableDict
    assert ImmutableDict({1: 'item'}) == {1: 'item'}
    assert ImmutableDict({1: 'item'}) == ImmutableDict({1: 'item'})
    assert ImmutableDict({1: 'item'}) != ImmutableDict({1: 'item1'})
    assert ImmutableDict({1: 'item'}) != ImmutableDict({1: 'item', 2: 'item'})
    assert ImmutableDict({1: 'item'}) != ImmutableDict({3: 'item'})
    assert ImmutableDict({1: 'item'}) != {1: 'item1'}

# Generated at 2022-06-12 22:58:04.952129
# Unit test for function is_iterable
def test_is_iterable():
    seq = [1, 2, 3, 'str', 'str2']
    assert is_iterable(seq) is True
    assert is_iterable('str') is False

    seq.append(seq)
    assert is_iterable(seq) is True

    assert is_iterable(2) is False

    seq = ImmutableDict({"a": 1, "b": 2})
    assert is_iterable(seq) is True



# Generated at 2022-06-12 22:58:08.017071
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    test_dict = ImmutableDict({"a": "1", "b": "2", "c": "3"})
    test_dict_2 = test_dict.difference(["b"])
    assert test_dict_2 == ImmutableDict({"a": "1", "c": "3"})
    assert len(test_dict_2) == 2


# Generated at 2022-06-12 22:58:17.207624
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    input_dict = {'a': 1, 'b': 2, 'c': 3}
    test_set = ImmutableDict(input_dict).difference(['a'])
    expected_set = {'b': 2, 'c': 3}
    assert test_set == expected_set

    input_dict = {'a': 1, 'b': 2, 'c': 3}
    test_set = ImmutableDict(input_dict).difference(['d'])
    expected_set = {'a': 1, 'b': 2, 'c': 3}
    assert test_set == expected_set


# Generated at 2022-06-12 22:58:28.098437
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    # A class for testing the ImmutableDict.difference method.
    # Arguments:
    #   test_id (int): ID number of the test.
    #   original_dict (dict): Dictionary that is used to create an ImmutableDict object.
    #   subtract_items (dict/list/tuple): Item/s that will be removed from the ImmutableDict object.
    #   expected_dict (dict): Expected result of the ImmutableDict.difference method.
    # Return:
    #   None
    # Exception:
    #   If the difference between the expected result and the actual result is not an empty dictionary
    #   raise an exception
    class TestDifference:
        def __init__(self, test_id, original_dict, subtract_items, expected_dict):
            self.test_id = test_

# Generated at 2022-06-12 22:58:33.932512
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a':1,'b':2})
    b = ImmutableDict({'a':1,'b':2})
    c = ImmutableDict({'a':1,'b':2,'c': 3})
    d = ImmutableDict()
    e = dict()

    assert a == b
    assert not a == c
    assert not a == d
    assert not a == e

# Generated at 2022-06-12 22:58:37.783491
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict(key1="some_value", key2="other_value")
    expected = ImmutableDict(key1="some_value")
    result = original.difference(["key2"])
    assert len(result) == len(expected)
    assert result == expected


# Generated at 2022-06-12 22:58:48.897475
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = ImmutableDict({'a': 1, 'b': 2})
    dict2 = ImmutableDict({'a': 1, 'b': 2})
    dict3 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    dict4 = ImmutableDict({'a': 2, 'b': 1})
    dict5 = {'a': 1, 'b': 2}
    # First test that python's built-in hash function works as expected
    assert hash(dict1) == hash(dict2)
    assert hash(dict1) != hash(dict4)
    # Now test that this class overrides the __eq__ method
    assert dict1 == dict2
    assert dict1 != dict3
    assert dict1 != dict4
    assert dict1 != dict5

# Generated at 2022-06-12 22:58:54.404940
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    test_dict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    test_diff_element = test_dict.difference('a')
    assert test_diff_element=={'b':2, 'c': 3}, "single element difference failed"
    test_diff_iterable = test_dict.difference(['a', 'c'])
    assert test_diff_iterable=={'b': 2}, "iterable difference failed"



# Generated at 2022-06-12 22:58:59.534030
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    test_dict = ImmutableDict({
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    })

    def test_difference(original, subtractive_iterable, expected):
        result = test_dict.difference(subtractive_iterable)
        assert list(result.items()) == expected

    # Test of iterable of different type
    test_difference(
        test_dict,
        [
            'a',
            'c'
        ],
        [
            ('b', 2),
            ('d', 4)
        ]
    )

    # Test of iterable of same type

# Generated at 2022-06-12 22:59:11.708309
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    '''
    Test cases of __eq__ method of ImmutableDict class.
    '''

    def run_case(first_d1, first_d2, second_d):
        '''
        Run a test case of __eq__ method of ImmutableDict class.

        :arg first_d1: The first dict for the first comparison.
        :arg first_d2: The second dict for the first comparison.
        :arg second_d: The dict for the second comparison.
        :return: None
        '''
        imm_d1 = ImmutableDict(first_d1)
        imm_d2 = ImmutableDict(first_d2)
        assert imm_d1 == imm_d2
        imm_d3 = ImmutableDict(second_d)
        assert not imm_d1 == imm_d

# Generated at 2022-06-12 22:59:19.029031
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({"lunch": "hamburger", "supper": "hot dog"})
    d2 = ImmutableDict({"lunch": "hamburger", "supper": "hot dog"})
    d3 = ImmutableDict({"lunch": "hamburger", "supper": "hot dog", "dinner": "pizza"})
    d4 = ImmutableDict({"lunch": "hamburger", "supper": "steak"})
    assert d1 == d2
    assert d1.__hash__() == d2.__hash__()

    assert not d1 == d3
    assert not d1.__hash__() == d3.__hash__()

    assert not d1 == d4
    assert not d1.__hash__() == d4.__hash

# Generated at 2022-06-12 22:59:24.605885
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(tuple())
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable(float())
    assert is_iterable(int())
    assert is_iterable(str())
    assert not is_iterable(None)



# Generated at 2022-06-12 22:59:28.230233
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1})
    d2 = ImmutableDict({'a': 1})
    d3 = ImmutableDict({'b': 1})

    assert d1 == d2
    assert not d1 == d3

# Generated at 2022-06-12 22:59:32.228810
# Unit test for method difference of class ImmutableDict
def test_ImmutableDict_difference():
    original = ImmutableDict({'A': 1, 'B': 2, 'C': 3})
    subtracted = original.difference(['B'])
    assert subtracted == ImmutableDict({'A': 1, 'C': 3})



# Generated at 2022-06-12 22:59:45.927795
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable(tuple())
    assert is_iterable((1, 2, 3, 4))
    assert is_iterable([1, 2, 3, 4])
    assert is_iterable({1, 2, 3, 4})
    assert is_iterable({'one': 1, 'two': 2, 'three': 3, 'four': 4})
    assert is_iterable(set([1, 2, 3, 4]))
    assert not is_iterable(None)
    assert not is_iterable('one two three four')
    assert not is_iterable(1)



# Generated at 2022-06-12 22:59:55.305897
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Equal when their hash is equal
    a = ImmutableDict(a=1)
    b = ImmutableDict(a=1)
    assert a == b

    # Not equal when their hash is not equal
    a = ImmutableDict(a=1)
    b = ImmutableDict(a=2)
    assert a != b

    # Not equal when the other argument's hash cannot be calculated
    a = ImmutableDict(a=1)
    b = [1]
    assert a != b

    class MyTest():
        def __eq__(self, other):
            return super(MyTest, self).__eq__(a)

    # Not equal when the other argument's __eq__ implementation is not using hash
    # and raises an exception as it tries to compare hash of an ImmutableDict
    a = Immutable

# Generated at 2022-06-12 22:59:59.446256
# Unit test for function is_iterable
def test_is_iterable():
    class A(object):
        pass

    a = A()
    try:
        iter(a)
    except TypeError:
        pass
    assert not is_iterable(a)

    class B(object):
        def __iter__(self):
            return iter(list())

    a = B()
    assert is_iterable(a)



# Generated at 2022-06-12 23:00:02.990437
# Unit test for function is_iterable
def test_is_iterable():
    iterable_object = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert is_iterable(iterable_object, include_strings=False)
    assert is_iterable(iterable_object, include_strings=True)

    non_iterable_object = 123
    assert not is_iterable(non_iterable_object, include_strings=False)


# Generated at 2022-06-12 23:00:08.100066
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(('abc', '123'))
    assert is_iterable({1, 2, 3})
    assert is_iterable(ImmutableDict({'a': 1, 'b': 2}))
    assert is_iterable({'a': 1, 'b': 2})
    assert not is_iterable('abc')


# Generated at 2022-06-12 23:00:18.509924
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = ImmutableDict({'1': 'one', '2': 'two', '3': 'three'})
    e = ImmutableDict({'1': 'one'})
    f = ImmutableDict({'2': 'two'})
    g = ImmutableDict({'4': 'four'})
    h = ImmutableDict({'1': 'one', '2': 'two', '3': 'three'})
    assert d == h, "d should be equal with h"
    assert d != e, "d should not be equal with e"
    assert d != f, "d should not be equal with f"
    assert d != g, "d should not be equal with g"
    assert e != f, "e should not be equal with f"
    assert h != f, "h should not be equal with f"


# Generated at 2022-06-12 23:00:25.878825
# Unit test for function is_iterable
def test_is_iterable():
    class SequenceTest(object):
        def __getitem__(self, key):
            return key

    class NotSequenceTest(object):
        def __iter__(self):
            return iter(list(range(3)))

    def iterable_generator(stop):
        for i in range(stop):
            yield i

    assert is_iterable(list(range(4)))
    assert is_iterable(tuple(range(4)))
    assert is_iterable(SequenceTest())
    assert is_iterable(iterable_generator(4))
    assert not is_iterable(SequenceTest)
    assert not is_iterable(NotSequenceTest())
    assert not is_iterable(10)


# Generated at 2022-06-12 23:00:36.875601
# Unit test for function is_iterable
def test_is_iterable():
    class TestClass(object):
        pass

    assert not is_iterable(1)
    assert not is_iterable('str')
    assert not is_iterable(u'str')
    assert not is_iterable(b'str')
    assert not is_iterable(TestClass)

    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({'1':1, '2':2})
    assert is_iterable(set([1,2, 3]))

    assert is_iterable([1, 2, 3], include_strings=True)
    assert is_iterable((1, 2, 3), include_strings=True)
    assert is_iterable({'1':1, '2':2}, include_strings=True)
   

# Generated at 2022-06-12 23:00:42.034687
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({1: 2, 3: 4})
    assert is_iterable(set([1, 2, 3]))
    assert is_iterable("abc")
    assert is_iterable("abc", include_strings=True)
    assert is_iterable(u"abc")
    assert is_iterable(u"abc", include_strings=True)
    assert not is_iterable(None)


# Generated at 2022-06-12 23:00:51.949113
# Unit test for function is_iterable
def test_is_iterable():
    """Unit test for function is_iterable."""
    assert is_iterable(None) == False
    assert is_iterable('string') == False
    assert is_iterable('string', include_strings=True) == True
    assert is_iterable(u'unicode string') == False
    assert is_iterable(u'unicode string', include_strings=True) == True
    assert is_iterable([]) == True
    assert is_iterable(()) == True
    assert is_iterable({}) == True
    assert is_iterable(set([])) == True
    assert is_iterable(set(())) == True
    assert is_iterable(range(3)) == True


# Generated at 2022-06-12 23:01:07.641474
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    def check_false():
        """
        Asserts that ImmutableDict objects with same keys and values but different ordering
        are not equal.
        """
        id1 = ImmutableDict({1: 2, 3: 4})
        id2 = ImmutableDict({3: 4, 1: 2})
        assert id1 != id2, 'Expected not equal ImmutableDicts'

    def check_true():
        """
        Asserts that ImmutableDict objects with same keys and same values are equal
        """
        id1 = ImmutableDict({1: 2, 3: 4})
        id2 = ImmutableDict({3: 4, 1: 2})
        assert id1 == id2, 'Expected equal ImmutableDicts'

    check_false()
    check_true()

# Generated at 2022-06-12 23:01:13.280278
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable("abc")
    assert is_iterable(("a","b","c"))
    assert is_iterable({'a':'b'})
    assert is_iterable("abc",include_strings=True)
    assert is_iterable(("a","b","c"),include_strings=True)
    assert not is_iterable({'a':'b'},include_strings=True)



# Generated at 2022-06-12 23:01:17.250917
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(a=1, b=2) == ImmutableDict(a=1, b=2)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=2, b=1)


# Generated at 2022-06-12 23:01:28.083131
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # USAGE: test_ImmutableDict__eq__()
    dictionary1 = ImmutableDict({'a': 1, 'b': 2})
    dictionary2 = ImmutableDict({'a': 1, 'b': 2})
    dictionary3 = ImmutableDict({'a': 1, 'b': 3})
    dictionary4 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    dictionary5 = ImmutableDict({'a': 1, 'c': 2})
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'a': 1, 'b': 2}
    dict3 = {'a': 1, 'b': 3}
    dict4 = {'a': 1, 'b': 2, 'c': 3}

# Generated at 2022-06-12 23:01:35.868338
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({'a': 'b'})
    assert not is_iterable(set())
    assert not is_iterable('123')
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert is_iterable(['1', '2', '3'])
    assert is_iterable(('1', '2', '3'))
    assert is_iterable(set(('1', '2', '3')))
    assert not is_iterable(object())
    assert is_iterable(('1', '2', '3'), include_strings=True)
    assert is_iterable('123', include_strings=True)



# Generated at 2022-06-12 23:01:45.674224
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test case for method __eq__ of class ImmutableDict

    Validate that __eq__ returns True for items with the same hash and False for items with different hash.

    The test covers conditions described in code of __eq__ method.
    """
    # Test case 1: items with the same hash
    dict1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    dict2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert dict1 == dict2

    # Test case 2: items with different hash
    dict1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    dict2 = ImmutableDict({'a': 1, 'b': 2, 'c': 4})
    assert dict1 != dict2

    #

# Generated at 2022-06-12 23:01:46.787253
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({"1": 1}) == ImmutableDict({"1": 1})

# Generated at 2022-06-12 23:01:51.759000
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable('abcd')
    assert not is_iterable(5)
    assert is_iterable(['a', 'b', 'c', 'd'])
    assert is_iterable(['a', 'b', 'c', 'd'], include_strings=True)
    assert is_iterable('abcd', include_strings=True)
    assert is_iterable((x for x in range(10)))



# Generated at 2022-06-12 23:01:56.803712
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable("ansible")
    assert not is_iterable("ansible", include_strings=False)
    assert is_iterable("ansible", include_strings=True)
    assert is_iterable([])
    assert is_iterable(set())
    assert is_iterable({'a': 'ansible'})
    assert is_iterable(1)


# Generated at 2022-06-12 23:02:04.332043
# Unit test for function is_iterable
def test_is_iterable():
    # These are all iterable
    assert(is_iterable([1, 2, 3]))
    assert(is_iterable({'x':1, 'y':2}))
    assert(is_iterable(set([1, 2, 3])))
    assert(is_iterable('abc'))
    assert(is_iterable(u'abc'))
    assert(is_iterable(b'abc'))
    assert(is_iterable(xrange(10)))
    assert(is_iterable(ImmutableDict({'x': 1})))

    # These are not iterable
    assert(not is_iterable(1))
    assert(not is_iterable(3.14))
    assert(not is_iterable(None))

    # These are iterable if we want strings to be considered iterable
   

# Generated at 2022-06-12 23:02:24.950124
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) == True
    assert is_iterable((1, 2, 3)) == True
    assert is_iterable(dict(a=1, b=2)) == True
    assert is_iterable({1, 2, 3}) == True
    assert is_iterable('123') == True
    assert is_iterable(123) == False


# Generated at 2022-06-12 23:02:34.434104
# Unit test for function is_iterable
def test_is_iterable():
    # Objects that are iterable
    class IterClass(object):
        def __iter__(self):
            yield 1
            yield 2
            yield 3

    class IterClass2(object):
        def __getitem__(self, y):
            return y**2

    class IterClass3(object):
        def __iter__(self):
            return self

        def next(self):
            return 1

        def __next__(self):
            return self.next()

    test_iter = [{}, [], set(), 'string', (1, 2), {'a': 1, 'b': 'test'}, IterClass(), IterClass2(), IterClass3()]
    for elem in test_iter:
        assert is_iterable(elem)

    # Objects that are NOT iterable

# Generated at 2022-06-12 23:02:45.026485
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Ensure the __eq__ method of ImmutableDict and __hash__ method return expected results"""

    # Create an ImmutableDict
    immutable_dict = ImmutableDict({'key': 'value'})

    # Test it against another ImmutableDict with the same contents and expect equality
    other_immutable_dict = ImmutableDict({'key': 'value'})
    assert immutable_dict == other_immutable_dict

    # Test it against a MutableMapping with the same content and expect inequality
    mutable_mapping = {'key': 'value'}
    assert immutable_dict != mutable_mapping

    # Create an ImmutableDict with an unhashable value

# Generated at 2022-06-12 23:02:53.380681
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})
    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) != ImmutableDict({'a': 1, 'b': 5, 'c': 3})
    assert ImmutableDict({'a': 1, 'b': 2, 'c': 3}) != ImmutableDict({'a': 1, 'b': 2})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert ImmutableDict({'a': 1, 'b': 1, 'c': 3}) == ImmutableDict({'c': 3, 'b': 1, 'a': 1})

# Generated at 2022-06-12 23:03:03.542237
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # check if ImmutableDict.__eq__(obj) returns True when obj is an ImmutableDict with
    # the same data as self
    # Unit test 1
    test_ImmutableDict = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    test_ImmutableDict_copy = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert test_ImmutableDict.__eq__(test_ImmutableDict_copy)
    # Unit test 2
    test_ImmutableDict = ImmutableDict({1: 'a', 2: 'b', 3: 'c'})
    test_ImmutableDict_copy = ImmutableDict({1: 'a', 2: 'b', 3: 'c'})
    assert test_ImmutableD

# Generated at 2022-06-12 23:03:09.733751
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Equal ImmutableDicts should hash to the same value
    dict_1 = ImmutableDict({'a': 1, 'b': 2})
    assert dict_1 == {'a': 1, 'b': 2}
    assert dict_1 == ImmutableDict({'b': 2, 'a': 1})
    assert dict_1 != {'a': 1}
    assert dict_1 != ImmutableDict({'b': 2, 'a': 2})
    assert dict_1 != 'some string'

# Generated at 2022-06-12 23:03:15.258386
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    a = ImmutableDict({'a': 1})
    b = ImmutableDict({'b': 1})
    c = ImmutableDict({'a': 1})
    d = ImmutableDict({'a': 1, 'b': 2})  # different length
    e = ImmutableDict({'a': 1, 'b': 1})  # different item
    assert a == a
    assert a == c
    assert not a == b
    assert not a == d
    assert not a == e

# Generated at 2022-06-12 23:03:24.677609
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict({'a': 1})
    d2 = ImmutableDict({'a': 1})
    d3 = ImmutableDict({'a': 1, 'b': 2})
    d4 = ImmutableDict({'b': 2, 'a': 1})
    d5 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    d6 = ImmutableDict({'a': 1, 'b': 2, 'c': 4})
    assert not d1.__eq__(True)
    assert not d1.__eq__(2)
    assert d1.__eq__(d1)
    assert d1.__eq__(d2)
    assert not d1.__eq__(d3)
    assert not d1.__eq__(d4)

# Generated at 2022-06-12 23:03:33.573261
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict([1, 2, 3]) == ImmutableDict([1, 2, 3])
    assert ImmutableDict([1, 2, 3]) == ImmutableDict({1: 1, 2: 2, 3: 3})
    assert ImmutableDict([1, 2, 3]) == {1: 21, 2: 25, 3: 9}
    assert ImmutableDict([1, 2, 3]) != ImmutableDict([3, 2, 1])
    assert ImmutableDict([1, 2, 3]) != ImmutableDict([1, 2, 4])
    assert ImmutableDict([1, 2, 3]) != ImmutableDict([1, 2, 3, 4])

# Generated at 2022-06-12 23:03:42.999944
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test against Hashable
    assert ImmutableDict() != set()
    assert ImmutableDict() == ImmutableDict()
    # Test against non-Hashable
    assert ImmutableDict() != dict()
    assert ImmutableDict() == ImmutableDict()
    assert ImmutableDict() != False
    assert ImmutableDict() == ImmutableDict()
    # Test against another ImmutableDict with same values
    assert ImmutableDict() == ImmutableDict()
    # Test against another ImmutableDict with different values
    assert ImmutableDict({1: 2}) != ImmutableDict()
    assert ImmutableDict({1: 2}) == ImmutableDict({1: 2})


# Generated at 2022-06-12 23:04:16.773901
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(range(3))
    assert is_iterable([0, 1, 2])
    assert is_iterable(0)
    assert not is_iterable('abc')
    assert not is_iterable(b'abc')



# Generated at 2022-06-12 23:04:19.490267
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict(first=1, second=2) == ImmutableDict(first=1, second=2)
    assert not ImmutableDict(first=1, second=2) == ImmutableDict(first=3, second=2)
    assert not ImmutableDict(first=1, second=2) == ImmutableDict(first=1, second=4)

# Generated at 2022-06-12 23:04:24.138140
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test case with different arguments:
    if not ImmutableDict('foo', 'bar', 'baz') == ImmutableDict('foo', 'bar', 'baz'):
        raise Exception("Failed to test __eq__ on the same object with different arguments")

    # Test case with the same object:
    if not ImmutableDict('foo', 'bar', 'baz') == ImmutableDict('foo', 'bar', 'baz'):
        raise Exception("Failed to test __eq__ on the same object with the same arguments")

    # Test case with different object:
    if ImmutableDict('foo', 'bar', 'baz') == ImmutableDict('foo', 'bar', 'qux'):
        raise Exception("Failed to test __eq__ on different objects with different arguments")

    # Test case with different types of arguments:

# Generated at 2022-06-12 23:04:27.807620
# Unit test for function is_iterable
def test_is_iterable():
    # Testing for sequence types
    assert(is_iterable([1, 2, 3]) == True)
    assert(is_iterable((1, 2, 3)) == True)
    # Testing for non-sequence types
    assert(is_iterable(1) == False)
    assert(is_iterable("1") == True)
    assert(is_iterable("1", True) == True)
    assert(is_iterable("1", False) == False)
    assert(is_iterable(u"1") == True)
    assert(is_iterable(u"1", True) == True)
    assert(is_iterable(u"1", False) == False)
    assert(is_iterable({"a": 1}) == True)

# Generated at 2022-06-12 23:04:34.448239
# Unit test for function is_iterable
def test_is_iterable():
    class NotIterable:
        pass

    class Iterable(object):
        def __iter__(self):
            return iter(range(2))

    assert is_iterable(NotIterable) is False
    assert is_iterable(Iterable()) is True
    assert is_iterable(range(2)) is True
    assert is_iterable('string') is False
    assert is_iterable('string', include_strings=True) is True
    assert is_iterable(None) is False


# Generated at 2022-06-12 23:04:39.236050
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    hash_1 = ImmutableDict(dict(foo=1, bar=2)).__hash__()
    hash_2 = ImmutableDict(dict(bar=2, foo=1)).__hash__()
    assert hash_1 == hash_2

    hash_3 = ImmutableDict(dict(foo=2, bar=2)).__hash__()
    assert hash_1 != hash_3


# Generated at 2022-06-12 23:04:45.873150
# Unit test for function is_iterable
def test_is_iterable():
    # Test is_iterable
    def _is_iterable(obj):
        return 'iterable' if is_iterable(obj) else 'non-iterable'

    # Test string
    assert _is_iterable('abc') == 'iterable'

    # Test class that is not iterable
    class NotIterable:
        pass

    assert _is_iterable(NotIterable()) == 'non-iterable'

    # Test class that is iterable
    class Iterable(object):
        def __iter__(self):
            raise Exception()

    assert _is_iterable(Iterable()) == 'iterable'


# Generated at 2022-06-12 23:04:52.464960
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable((), include_strings=True)
    assert is_iterable(set())
    assert is_iterable(dict())
    assert is_iterable('')
    assert is_iterable(b'')
    assert is_iterable('abc')
    assert is_iterable(b'abc')
    assert not is_iterable(None)
    assert not is_iterable(1, include_strings=True)
    assert not is_iterable('', include_strings=False)
    assert not is_iterable(b'', include_strings=False)


# Generated at 2022-06-12 23:05:02.385148
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Tests equality of ImmutableDicts

    :return: None
    """
    # In case of string_type objects, equality is the same as the frozenset of string_type objects
    assert ImmutableDict({'a': 'b'}) == ImmutableDict({'a': 'b'})
    assert not ImmutableDict({'a': 'b'}) == ImmutableDict({'b': 'a'})

    # In case of non-string_type objects, equality is the same as frozenset({id(key), id(value)})
    assert ImmutableDict({1: []}) == ImmutableDict({1: []})
    assert not ImmutableDict({1: []}) == ImmutableDict({1: {}})

    # In case of string_type and non-string_type objects,
    #

# Generated at 2022-06-12 23:05:10.040599
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(frozenset())
    assert is_iterable(range(0))
    assert is_iterable(xrange(0))
    assert not is_iterable(None)
    assert not is_iterable(0)
    assert not is_iterable(0.0)
    assert not is_iterable('')
    assert not is_iterable(u'')
    assert not is_iterable(False)

