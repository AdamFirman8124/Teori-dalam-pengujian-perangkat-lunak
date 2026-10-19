

# Generated at 2022-06-12 22:56:05.874192
# Unit test for function is_iterable
def test_is_iterable():
    """Test is_iterable()."""
    assert is_iterable([])
    assert is_iterable(())
    assert not is_iterable(1)
    assert not is_iterable('f')
    assert is_iterable('f', include_strings=True)
    assert is_iterable(b'f', include_strings=True)



# Generated at 2022-06-12 22:56:11.182624
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict."""
    test_mapping = ImmutableDict(dict(one=1, two=2))
    assert test_mapping.__eq__(dict(one=1, two=2)) is True
    assert test_mapping.__eq__(dict(two=2, one=1)) is True
    assert test_mapping.__eq__(dict(Two=2, One=1)) is True
    assert test_mapping.__eq__(dict(two=2, one=1, three=3)) is False
    assert test_mapping.__eq__(dict(two=2, One=1)) is False
    assert test_mapping.__eq__(dict(two=3, One=1)) is False

# Generated at 2022-06-12 22:56:21.046518
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict() == ImmutableDict()

    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'b': 2, 'a': 1})

    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'b': 3})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'b': 2, 'c': 3})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({})


# Generated at 2022-06-12 22:56:28.595841
# Unit test for function is_iterable
def test_is_iterable():

    class Foo:
        pass

    # Argument is not iterable
    assert not is_iterable(None)
    assert not is_iterable(1)

    # Argument is iterable
    assert is_iterable([])
    assert is_iterable('')
    assert is_iterable(b'')
    assert is_iterable(())
    assert is_iterable(set())
    assert is_iterable({})
    assert is_iterable(Foo)  # A class can be iterated through its instances



# Generated at 2022-06-12 22:56:35.983216
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(range(10))
    assert is_iterable(set(range(10)))
    assert is_iterable(tuple(range(10)))
    assert is_iterable(dict(zip(range(10), range(10))))
    assert not is_iterable(1)
    assert not is_iterable(complex(1))
    assert not is_iterable(Exception)
    assert not is_iterable(Exception())
    assert not is_iterable(None)
    assert not is_iterable(object)
    assert not is_iterable(range)
    assert not is_iterable(xrange)



# Generated at 2022-06-12 22:56:45.238952
# Unit test for function is_iterable
def test_is_iterable():
    # pylint: disable=unused-argument
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(tuple())
    assert is_iterable(xrange(0))
    assert is_iterable('', include_strings=True)
    assert is_iterable(u'', include_strings=True)
    assert is_iterable(r'', include_strings=True)
    assert not is_iterable(0)
    assert not is_iterable(0.0)
    assert not is_iterable('')
    assert not is_iterable(u'')
    assert not is_iterable(r'')



# Generated at 2022-06-12 22:56:56.188519
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for ImmutableDict.__eq__."""
    immutableDict1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    immutableDict2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    immutableDict3 = ImmutableDict({'x': 4, 'y': 5, 'z': 6})
    immutableDict4 = ImmutableDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
    immutableDict5 = ImmutableDict({'b': 2, 'c': 3, 'd': 4, 'a': 1})
    immutableDict6 = ImmutableDict({'b': 2, 'c': 3, 'd': 4})

# Generated at 2022-06-12 22:57:01.568259
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d = dict()
    d1 = dict()
    d["" + text_type(u"foo")] = text_type(u"bar")
    d["" + text_type(u"abc")] = text_type(u"xyz")
    d1["" + text_type(u"foo")] = text_type(u"bar")
    d1["" + text_type(u"abc")] = text_type(u"xyz")
    if ImmutableDict(d) != ImmutableDict(d1):
        raise AssertionError()
    d2 = dict()
    d2["" + text_type(u"abc")] = text_type(u"xyz")
    d2["" + text_type(u"foo")] = text_type(u"bar")
   

# Generated at 2022-06-12 22:57:12.500399
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Tests the method __eq__ of the class ImmutableDict"""

    # Create a couple of instances of ImmutableDict with the same key value pairs and check that
    # they are equal (method __eq__ should return True)
    d1 = ImmutableDict({'a': 1, 1: 'a'})
    d2 = ImmutableDict(a=1, _1='a')
    assert d1 == d2

    # Create a couple of instances of ImmutableDict with the same keys, but different value pairs
    # and check that they are not equal (method __eq__ should return False)
    d1 = ImmutableDict({'a': 1, 1: 'a'})
    d2 = ImmutableDict(a=2, _1='a')
    assert not d1 == d2

    # Create a couple of

# Generated at 2022-06-12 22:57:16.559704
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test for the correct operation of ImmutableDict.__eq__ method."""
    sample_dict = ImmutableDict({"arg1": "val1"})
    sample_dict_copy = ImmutableDict(sample_dict)
    assert sample_dict == sample_dict_copy
    assert not sample_dict == "not_dictionary"


# Generated at 2022-06-12 22:57:31.785597
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test equality with different instantiation methods and input types
    d_one = ImmutableDict(a=1, b=2)
    d_two = ImmutableDict(dict(a=1, b=2))
    assert d_one == d_two

    # Test inequality when contents are different
    d_one = ImmutableDict(a=1, b=2)
    d_two = ImmutableDict(a=1, b=3)
    assert d_one != d_two

    # Test inequality when order is different
    d_one = ImmutableDict(a=1, b=2)
    d_two = ImmutableDict(b=2, a=1)
    assert d_one != d_two

    # Test inequality when sizes are different

# Generated at 2022-06-12 22:57:36.009957
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(())
    assert is_iterable(set())
    assert is_iterable(range(10))
    assert is_iterable('string')
    assert is_iterable(b'bytes')
    assert not is_iterable(None)



# Generated at 2022-06-12 22:57:44.669593
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Exception 1: non-immutable objects are not equal
    d1 = ImmutableDict()
    not_immutable = {}
    assert d1 != not_immutable

    # Exception 2: different objects are not equal
    d1 = ImmutableDict()
    d2 = ImmutableDict()
    assert d1 != d2

    # Exception 3: objects with different keys are not equal
    d1 = ImmutableDict({'key1': 1})
    d2 = ImmutableDict({'key2': 1})
    assert d1 != d2

    # Exception 4: objects with different values are not equal
    d1 = ImmutableDict({'key1': 1})
    d2 = ImmutableDict({'key1': 2})
    assert d1 != d2

    # Exception 5: objects with different number of elements are

# Generated at 2022-06-12 22:57:51.358044
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""
    # Both arguments are ImmutableDict
    a = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    b = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    c = ImmutableDict({'a': 1, 'b': 2, 'c': 4})
    d = ImmutableDict({'a': 1, 'b': 2})

    # test for equal objects
    assert a == b

    # test for non equal objects
    assert a != c
    assert a != d
    assert c != d
    # First argument is not ImmutableDict
    # test for int
    assert a != 1

    # test for string
    assert a != 'hello, world'

    # test

# Generated at 2022-06-12 22:58:01.324651
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    :raises TestFailure: Whenever a result of test is not as expected
    """
    import types
    from functools import partial
    from ansible.module_utils.basic import TestFailure
    from ansible.module_utils.six.moves import cStringIO, StringIO

    def get_test_data():
        """
        Returns the test data, represented by a tuple of tuples:
            (((data1_iter, data2_iter), expected_result), description)

        Each test case consists of two iterators and an expected result of comparison.
        If expected result of comparison is True, the iterators are expected to be equal.
        If expected result of comparison is False, the iterators are expected to be unequal.

        :return: The test data
        :rtype: tuple
        """

# Generated at 2022-06-12 22:58:09.471498
# Unit test for function is_iterable
def test_is_iterable():
    from collections import namedtuple
    class C(object):
        def __iter__(self):
            return iter([1,2,3])
    class D(object):
        pass

    assert is_iterable(C())
    assert is_iterable([1,2,3])
    assert is_iterable((1,2,3))
    assert is_iterable(iter([1,2,3]))
    assert is_iterable(dict(a=1, b=2, c=3))
    assert not is_iterable(D())
    assert not is_iterable(5)
    assert not is_iterable(True)
    assert not is_iterable(None)



# Generated at 2022-06-12 22:58:20.561435
# Unit test for function is_iterable
def test_is_iterable():
    from collections import Iterable, Sequence, Hashable, Sized
    class TestClass(Iterable):
        pass
    class TestClass2(Sequence):
        pass
    class TestClass3(Hashable):
        pass
    class TestClass4(Sized):
        pass

    assert is_iterable(range(5)) is True
    assert is_iterable(TestClass) is False
    assert is_iterable(TestClass2) is False
    assert is_iterable(TestClass3) is False
    assert is_iterable(TestClass4) is False

    test_object = TestClass()
    assert is_iterable(test_object) is True

    test_object2 = TestClass2()
    assert is_iterable(test_object2) is True

    test_object3 = TestClass3()
    assert is_

# Generated at 2022-06-12 22:58:30.465298
# Unit test for function is_iterable
def test_is_iterable():
    """Return None if test DOES NOT PASS or else return 'Test is successful' message."""
    class NotIterable(object):
        pass
    not_iterable = NotIterable()
    assert not is_iterable(not_iterable)
    assert is_iterable([1, 2, 3])
    assert is_iterable((1, 2, 3))
    assert is_iterable({1, 2, 3})
    assert is_iterable({'a': 'a', 'b': 'b', 'c': 'c'})
    assert is_iterable(((1, 2), (3, 4)))
    assert is_iterable([(1, 2), (3, 4)])
    assert is_iterable((i for i in range(10)))
    assert is_iterable('a string')

# Generated at 2022-06-12 22:58:34.368626
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) and is_iterable({}) and is_iterable(set()) and is_iterable((x for x in range(3)))
    assert is_iterable('abc') and is_iterable(b'abc') and is_iterable(bytearray(b'abc'))
    assert not is_iterable(2)
    assert not is_iterable(object)


# Generated at 2022-06-12 22:58:44.922939
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    This is a collection of unit tests for the ImmutableDict class.

    See https://docs.python.org/2/library/unittest.html for details on how to implement unit
    tests.
    """
    import unittest

    class TestImmutableDictMethods(unittest.TestCase):

        _IMMUTABLE_DICT_TEST_DATA = ImmutableDict({"a": 1, "b": 2})

        def test_ImmutableDict___eq__(self):
            first_immutable_dict = ImmutableDict({"a": 1, "b": 2})
            second_immutable_dict = ImmutableDict({"a": 1, "b": 3})

            self.assertTrue(self._IMMUTABLE_DICT_TEST_DATA == first_immutable_dict)

# Generated at 2022-06-12 22:58:58.103191
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable(ImmutableDict(a=1))
    assert is_iterable(x for x in range(4))
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert not is_iterable('a')


# Generated at 2022-06-12 22:59:00.180718
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({1: 2}) == ImmutableDict({1: 2})



# Generated at 2022-06-12 22:59:11.981535
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = ImmutableDict({'A': 'a', 'B': 'b', 'C': 'c'})
    dict2 = ImmutableDict({'A': 'a', 'B': 'b', 'C': 'c'})
    dict3 = ImmutableDict({'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'})
    dict4 = ImmutableDict({'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd'})
    dict5 = ImmutableDict({'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e'})

    # Two identical dicts are equal
    assert dict1 == dict2

    # Two dicts containing the same keys with the same values

# Generated at 2022-06-12 22:59:17.616153
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Test __eq__ with same object
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1})

    # Test __eq__ with different object, same data
    assert ImmutableDict({'a': 1}) == ImmutableDict({'a': 1, 'b': 2})

    # Test __eq__ with similar object, different data
    assert not ImmutableDict({'a': 1}) == ImmutableDict({'b': 2})

    # Test __eq__ with different object, different data
    assert not ImmutableDict({'a': 1}) == 2



# Generated at 2022-06-12 22:59:26.762276
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) == True
    assert is_iterable(()) == True
    assert is_iterable({}) == True
    assert is_iterable(set([])) == True
    assert is_iterable('abc') == True
    assert is_iterable('abc'.encode('utf-8')) == True
    assert is_iterable(u'abc') == True
    assert is_iterable(b'abc') == True
    assert is_iterable(1) == False
    assert is_iterable(None) == False
    assert is_iterable(True) == False
    assert is_iterable(object()) == False


# Generated at 2022-06-12 22:59:34.931042
# Unit test for function is_iterable
def test_is_iterable():
    """Unit tests for the is_iterable function"""

    assert is_iterable([])
    assert is_iterable(())
    assert is_iterable({})
    assert is_iterable({'a': 'b'})
    assert is_iterable(xrange(1, 15))
    assert is_iterable(set([1, 2, 3]))
    assert not is_iterable(1)
    assert not is_iterable(object())
    assert not is_iterable(1.0)
    assert not is_iterable(True)
    assert not is_iterable(None)


# Generated at 2022-06-12 22:59:39.869610
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    d1 = ImmutableDict(a=1, b=2, c=3)
    # Test that ImutableDict compares equal to a dict with the same contents
    assert d1 == dict(a=1, b=2, c=3)
    # Test that ImmutableDict compares equal to itself
    assert d1 == d1
    d2 = ImmutableDict(a=1, b=2, c=3)
    # Test that two ImmutableDict's with the same content are equal
    assert d1 == d2
    assert d2 == d1
    d2 = ImmutableDict(a=1, b=2)
    # Test that ImmutableDict compares not equal to a dict with different contents
    assert d1 != d2
    assert d2 != d1

# Generated at 2022-06-12 22:59:47.434947
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['a', 'b', 'c'])
    assert is_iterable(('a', 'b', 'c'))
    assert is_iterable({'a': 1, 'b': 2, 'c': 3})
    assert is_iterable(['a', 'b', 'c'], include_strings=True)
    assert is_iterable(('a', 'b', 'c'), include_strings=True)
    assert is_iterable({'a': 1, 'b': 2, 'c': 3}, include_strings=True)
    assert is_iterable(1)
    assert is_iterable('abc')
    assert is_iterable('abc', include_strings=True)
    assert not is_iterable(1, include_strings=True)



# Generated at 2022-06-12 22:59:56.933220
# Unit test for function is_iterable
def test_is_iterable():
    # Test cases
    is_iterable('string')
    is_iterable('string with spaces')
    is_iterable("string with 'single quote'")
    is_iterable("string with 'single' and \"double\" quotes")
    is_iterable(['list', 'of', 'strings'])
    is_iterable(('tuple', 'of', 'strings'))
    is_iterable({'set', 'of', 'strings'})
    is_iterable({'mapping': 'of strings'})
    is_iterable(frozenset({'frozen', 'set', 'of', 'strings'}))

    # Expected to fail

# Generated at 2022-06-12 23:00:06.202893
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    # Tests for Immutability
    # 1) Check for read-only
    immutable_dict = ImmutableDict({'test': 1})
    try:
        immutable_dict['test'] = 2
        assert False, 'Object is mutable'
    except:
        pass

    # 2) Check for immutability of original dictionary
    dictionary = {'test': 1}
    immutable_dict = ImmutableDict(dictionary)
    try:
        immutable_dict['test'] = 2
        assert False, 'Object is mutable'
    except:
        pass

    # 3) Check for immutability after updating original dictionary
    dictionary['test'] = 2
    immutable_dict = ImmutableDict(dictionary)

# Generated at 2022-06-12 23:00:34.780107
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from numbers import Number

    from ansible.module_utils.six import PY3, binary_type, string_types
    from ansible.module_utils.six.moves import UserDict

    # We use sets to check if the results are correct
    orig = ImmutableDict({'a': 1, 'b': 2, 'c': 3})

    # Scalar checks
    assert orig != 1  # 1 is not an ImmutableDict
    assert orig != {'a': 1, 'b': 2}  # this one is a dict, same keys but different values
    assert orig != {'a': 1, 'c': 2}  # this one is a dict, different keys
    assert orig != ImmutableDict({'a': 1, 'b': 2})  # same keys but different values

# Generated at 2022-06-12 23:00:43.463766
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    d1 = ImmutableDict({'a': 1})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    d3 = ImmutableDict({'b': 2, 'a': 1})
    d4 = ImmutableDict({'c': 3, 'b': 2})
    d5 = ImmutableDict({'b': 1, 'a': 2})
    d6 = ImmutableDict({'b': 1, 'a': 2})

    # An ImmutableDict should be equal to itself
    assert d1 == d1
    assert d2 == d2
    assert d3 == d3

    # An ImmutableDict is equal to a matching dictionary
    assert d1 == {'a': 1}
    assert d2 == {'a': 1, 'b': 2}
    assert d3

# Generated at 2022-06-12 23:00:51.175446
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert not is_iterable(1)
    assert not is_iterable(1.5)
    assert not is_iterable(object())
    assert not is_iterable('abc')
    assert is_iterable(b'abc')
    assert is_iterable([])
    assert is_iterable(('a', 'b'))
    assert is_iterable({})
    assert is_iterable(dict())
    assert is_iterable(set())

# Generated at 2022-06-12 23:01:02.165412
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a':'b'}) == ImmutableDict({'a':'b'})
    assert ImmutableDict({'a':'b', 'z':{'a':'b'}}) == ImmutableDict({'a':'b', 'z':{'a':'b'}})

    assert ImmutableDict({'a': 'b'}) != {'a': 'b'}
    assert ImmutableDict({'a': 'b'}) != ImmutableDict({'a': 'c'})
    assert ImmutableDict({'a': 'b'}) != ImmutableDict({'a': 'b', 'z': {'a': 'b'}})
    assert ImmutableDict({'a': 'b', 'z': {'a': 'b'}}) != ImmutableDict

# Generated at 2022-06-12 23:01:08.650249
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """
    Test the __eq__ method of ImmutableDict to ensure correct handling of various comparisons.
    """
    # Test for validity of __eq__ method
    immutable_dict1 = ImmutableDict({"foo": "bar"})
    immutable_dict2 = ImmutableDict({"foo": "bar"})
    assert immutable_dict1 == immutable_dict2
    assert immutable_dict1 != {"foo": "bar"}
    assert immutable_dict1 != ("foo", "bar")
    # Test for hash comparison
    assert immutable_dict1.__hash__() == hash(frozenset(immutable_dict1.items()))

# Generated at 2022-06-12 23:01:18.855268
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    from ansible.parsing.dataloader import DataLoader
    from ansible.template import Templar
    from ansible.vars.manager import VariableManager
    from ansible.inventory.manager import InventoryManager

    stock_dict = {'hello': 'world'}
    immutable_dict1 = ImmutableDict({'hello': 'world'})
    immutable_dict2 = ImmutableDict(stock_dict)
    immutable_dict3 = ImmutableDict(stock_dict)
    string_dict = "hello"
    list_dict = ['hello', 'world']
    tuple_dict = ('hello', 'world')
    class_dict = DataLoader()
    templar_dict = Templar(VariableManager(), InventoryManager())

    assert immutable_dict1 == immutable_dict2
    assert immutable_dict2 == immutable_dict3
   

# Generated at 2022-06-12 23:01:25.668494
# Unit test for function is_iterable
def test_is_iterable():
    """Check whether is_iterable works as expected."""
    assert is_iterable(set())
    assert is_iterable([])
    assert is_iterable(dict())
    assert is_iterable('xy')
    assert is_iterable({1})
    # A generator is iterable
    assert is_iterable((x for x in range(3)))

    assert not is_iterable(1)
    assert not is_iterable(True)



# Generated at 2022-06-12 23:01:34.798893
# Unit test for function is_iterable

# Generated at 2022-06-12 23:01:45.002373
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():

    # Create two immuatble dict with the same key and value pairs
    d0 = ImmutableDict({'a': 0, 'b': 1})
    d1 = ImmutableDict({'a': 0, 'b': 1})
    assert d0 == d1

    # Equality testing against a standard dict will return False
    d2 = dict({'a': 0, 'b': 1})
    assert d0 != d2

    # Create two immutable dict with different key-value pairs
    d0 = ImmutableDict({'a': 0, 'b': 1})
    d1 = ImmutableDict({'a': 0, 'b': 2})
    assert d0 != d1

    # Create two dict with different key-value pairs
    d0 = dict({'a': 0, 'b': 1})

# Generated at 2022-06-12 23:01:52.793454
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    for equal in (ImmutableDict(), ImmutableDict(a=1, b=2), ImmutableDict(a=1, b=2), ImmutableDict(b=2, a=1)):
        assert equal == equal
        assert equal == ImmutableDict(equal)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=3)
    assert ImmutableDict(a=1, b=2) != ImmutableDict(a=1, b=2, c=3)
    assert ImmutableDict(a=1, b=2) != {'a': 1, 'b': 2}
    assert ImmutableDict(a=1, b=2) != (('a', 1), ('b', 2))

# Generated at 2022-06-12 23:02:37.949551
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([0, 1, 2])
    assert is_iterable((0, 1, 2))
    assert is_iterable({0, 1, 2})
    assert is_iterable(set([0, 1, 2]))
    assert is_iterable(range(3))
    assert is_iterable(xrange(3))
    assert is_iterable((x for x in range(3)))
    assert is_iterable((x for x in range(3)), True)
    assert is_iterable('123')
    assert is_iterable(b'123')
    assert not is_iterable(0)
    assert not is_iterable('123', True)
    assert not is_iterable(b'123', True)


# Generated at 2022-06-12 23:02:40.678116
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    assert ImmutableDict({'a': 1, 'b': 2}) == ImmutableDict({'a': 1, 'b': 2})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 1, 'b': 3})
    assert ImmutableDict({'a': 1, 'b': 2}) != ImmutableDict({'a': 2, 'b': 2})

# Generated at 2022-06-12 23:02:47.098184
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    dict1 = ImmutableDict({'one': 1, 'two': 2, 'three': 3})
    dict2 = ImmutableDict({'one': 1, 'two': 2, 'three': 3})
    dict3 = ImmutableDict({'two': 2, 'three': 3, 'four': 4})
    dict4 = dict({'two': 2, 'three': 3, 'four': 4})
    assert dict1 == dict2
    assert dict1 != dict3
    assert dict1 != dict4

# Generated at 2022-06-12 23:02:54.721665
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    left = ImmutableDict(a=1, b=2)
    right = dict(a=1, b=2)

    assert left == right, 'incorrect result of comparison of ImmutableDict and standard dict'

    right = ImmutableDict(a=1, b=2)
    assert left == right, 'incorrect result of comparison of two ImmutableDicts'

    right = ImmutableDict(a=1, b=3)
    assert left != right, 'incorrect result of comparison of two ImmutableDicts'

    right = dict(a=1, b=2, c=3)
    assert left != right, 'incorrect result of comparison of ImmutableDict and standard dict'

    right = ImmutableDict(a=1, b=2, c=3)

# Generated at 2022-06-12 23:03:04.922628
# Unit test for function is_iterable
def test_is_iterable():
    assert not is_iterable(None)
    assert is_iterable((1, 2, 3))
    assert is_iterable([1, 2, 3])
    assert is_iterable(True)
    assert is_iterable([False, True])
    assert is_iterable({'k1': 'v1', 'k2': 'v2'})
    assert is_iterable({'k1': 'v1', 'k2': 'v2'})
    assert is_iterable(('a', 1, True))
    assert is_iterable(set(['a', 1, True]))
    assert not is_iterable(set())
    assert not is_iterable('foo')
    assert is_iterable('foo', include_strings=True)
    assert not is_iterable(u'foo')
    assert is_

# Generated at 2022-06-12 23:03:08.244531
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) == True
    assert is_iterable((x for x in range(5))) == True
    assert is_iterable({}) == True
    assert is_iterable(0) == False


# Generated at 2022-06-12 23:03:13.720085
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable((x for x in range(5)))
    assert is_iterable([1, 2])
    assert is_iterable(ImmutableDict({'a': 1, 'b': 2}))
    assert not is_iterable(1)
    assert not is_iterable('spam')
    assert is_iterable('spam', include_strings=True)


# Generated at 2022-06-12 23:03:21.177994
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Unit test for method __eq__ of class ImmutableDict"""
    # test equal when equal to self
    d = ImmutableDict({'a': 1, 'b': 2})
    assert d.__eq__(d)

    # test equal with same dictionary
    d2 = ImmutableDict({'a': 1, 'b': 2})
    assert d.__eq__(d2)

    # test unequal
    d3 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    assert not d.__eq__(d3)
    # test unequal when not ImmutableDict type
    assert not d.__eq__({'a': 1, 'b': 2})

# Generated at 2022-06-12 23:03:30.874070
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import collections

    a = ImmutableDict(x=1, y=2, z=3)
    # Same type
    b = ImmutableDict(x=1, y=2, z=3)
    assert (a == b) == True

    b = ImmutableDict(x=1, y=2, z=4)
    assert (a == b) == False

    # Different Types
    b = collections.OrderedDict(x=1, y=2, z=3)
    assert (a == b) == False

    b = dict(x=1, y=2, z=3)
    assert (a == b) == True

    # Wrong type provided
    b = "hello"
    try:
        a == b
    except TypeError:
        pass
    else:
        assert False


#

# Generated at 2022-06-12 23:03:37.912677
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([]) is True
    assert is_iterable((1, 2, 3)) is True
    assert is_iterable({}) is True
    assert is_iterable(set()) is True
    assert is_iterable("abc") is True
    assert is_iterable("") is True
    assert is_iterable(u"abc") is True
    assert is_iterable(u"") is True
    assert is_iterable(b"abc") is True
    assert is_iterable(b"") is True
    assert is_iterable(1) is False
    assert is_iterable(None) is False

    # Test for strings
    assert is_iterable("abc", include_strings=True) is True
    assert is_iterable("", include_strings=True) is True

# Generated at 2022-06-12 23:05:01.003909
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3]) == True
    assert is_iterable((1, 2, 3)) == True
    assert is_iterable({1: 2, 3: 4}) == True
    assert is_iterable(1) == False
    assert is_iterable(dict()) == True
    assert is_iterable('hello') == False
    assert is_iterable('hello', True) == True

if __name__ == '__main__':
    test_is_iterable()

# Generated at 2022-06-12 23:05:10.917643
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    container_1 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    container_2 = ImmutableDict({'a': 1, 'b': 2, 'c': 3})
    container_3 = ImmutableDict({'a': 1, 'b': 2})
    container_4 = ImmutableDict({'a': 1, 'b': 2, 'c': 4})
    container_5 = ImmutableDict({'a': 1, 'b': 2, 'd': 3})
    container_6 = ImmutableDict({'something': 3})
    container_7 = ImmutableDict({'something': 4})
    container_8 = ImmutableDict({'something': 4})

    assert container_1 == container_2
    assert container_2 == container_1
    assert not container_1

# Generated at 2022-06-12 23:05:15.998542
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    """Test ImmutableDict.__eq__"""
    d1 = ImmutableDict({'a': 1, 'b': 2})
    d2 = ImmutableDict({'a': 1, 'b': 2})
    assert d1 == d2
    d3 = ImmutableDict({'a': 1, 'b': 3})
    assert not d1 == d3
    assert not d1 == {'a': 1, 'b': 2}
    assert not d1 == 'stuff'

# Generated at 2022-06-12 23:05:22.386319
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable(['a'])
    assert is_iterable({'a': 1})
    assert is_iterable(set('a'))
    assert is_iterable(range(1))
    assert is_iterable('a')
    assert is_iterable(b'a')
    assert not is_iterable('a', include_strings=False)
    assert not is_iterable(b'a', include_strings=False)
    assert not is_iterable(1)


# Generated at 2022-06-12 23:05:31.187575
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([1, 2, 3])
    assert is_iterable([])
    assert is_iterable((1, 2, 3))
    assert is_iterable(())
    assert is_iterable({'a': 1, 'b': 2, 'c': 3})
    assert is_iterable({})
    assert is_iterable(xrange(6))
    assert is_iterable(xrange(0))
    assert is_iterable('abc')
    assert not is_iterable(1)
    assert not is_iterable(None)
    assert not is_iterable(dict)
    assert not is_iterable(is_iterable)



# Generated at 2022-06-12 23:05:40.283784
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    test_dict = ImmutableDict(key1='value1', key2='value2')
    # Compare ImmutableDicts with different content
    assert test_dict != ImmutableDict(key1='value1')
    # Compare ImmutableDict with a regular dict with the same content
    assert test_dict == dict(test_dict)
    assert test_dict != dict(key1='value1', key2='value2', key3='value3')
    # Compare ImmutableDict with a regular dict with different content
    assert test_dict != dict(key1='value1', key2='value2', key3='value3')
    # Compare ImmutableDict with a regular dict with the same content but different order
    assert test_dict == dict(key2='value2', key1='value1')

# Generated at 2022-06-12 23:05:46.673271
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    id1 = ImmutableDict({'k1': 'v1', 'k2': 'v2'})
    id2 = ImmutableDict({'k1': 'v1', 'k2': 'v2'})
    assert id1 == id2
    id3 = ImmutableDict({'k1': 'v1', 'k2': 'v2'})
    id4 = ImmutableDict({'k2': 'v2', 'k1': 'v1'})
    assert id3 == id4
    id5 = ImmutableDict({'k1': 'v1', 'k2': 'v2'})
    id6 = ImmutableDict({'k1': 'v1', 'k2': 'v2', 'k3': 'v3'})
    assert not id5 == id6

# Generated at 2022-06-12 23:05:53.190639
# Unit test for function is_iterable
def test_is_iterable():
    assert is_iterable([])
    assert is_iterable({})
    assert is_iterable(set())
    assert is_iterable(1)
    assert is_iterable(object)
    assert is_iterable('a') is False
    assert is_iterable(b'a') is False
    assert is_iterable(['a', 'b'])
    assert is_iterable(('a', 'b'))
    assert is_iterable({1, 2, 3})
    assert is_iterable({'a': 1, 'b': 2})



# Generated at 2022-06-12 23:05:57.296831
# Unit test for function is_iterable
def test_is_iterable():

    assert is_iterable('abc')
    assert is_iterable(['1', '2'])
    assert is_iterable((x for x in range(10)))
    assert is_iterable(ImmutableDict({'1': '2'}))

    assert not is_iterable(1)
    assert not is_iterable(datetime)


# Generated at 2022-06-12 23:06:05.762804
# Unit test for method __eq__ of class ImmutableDict
def test_ImmutableDict___eq__():
    import unittest2 as unittest
    class TestImmutableDict__eq__(unittest.TestCase):
        def test_eq_with_ImmutableDict(self):
            # GIVEN
            d1 = ImmutableDict({'a': 1, 'b': 2})
            d2 = ImmutableDict({'a': 1, 'b': 2})
            d3 = ImmutableDict({'b': 2, 'a': 1})
            d4 = ImmutableDict({'a': 1, 'b': 3})
            # WHEN
            result1 = d1 == d2
            result2 = d1 == d3
            result3 = d1 == d4
            # THEN
            self.assertEqual(result1, True)
            self.assertEqual(result2, True)