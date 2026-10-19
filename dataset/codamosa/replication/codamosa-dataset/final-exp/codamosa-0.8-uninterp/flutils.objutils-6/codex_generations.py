

# Generated at 2022-06-13 20:43:07.530057
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')
    assert not has_callables(dict(),'get','keys','items','values','foo')



# Generated at 2022-06-13 20:43:11.436401
# Unit test for function has_callables
def test_has_callables():
    d = dict(a=1, b=2)
    assert has_callables(d, "keys", 'items') == True
    assert has_callables(d, "foo") == False


# Generated at 2022-06-13 20:43:20.110814
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    assert has_callables(obj, "clear", "fromkeys") is True
    assert has_callables(obj, "foo") is False
    assert has_callables(None, "foo") is False
    assert has_callables("The quick brown fox jumps over the lazy dog", "startswith") is True
    assert has_callables("The quick brown fox jumps over the lazy dog", "foo") is False



# Generated at 2022-06-13 20:43:22.433281
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1,b=2)
    assert has_callables(obj, 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:43:26.726015
# Unit test for function has_any_attrs
def test_has_any_attrs():
    x = dict()
    assert has_any_attrs(x, 'clear', 'update', 'copy', 'setdefault') == True


# Generated at 2022-06-13 20:43:30.420594
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'values', 'items')



# Generated at 2022-06-13 20:43:43.781739
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables([1, 2, 3, 4], 'index', 'count', 'count', 'reverse') is True
    assert has_callables(set([1, 2, 3, 4]), 'index', 'count', 'count', 'reverse') is False
    assert has_callables({'a': 1, 'b': 2, 'c': 3}, 'get', 'keys', 'items', 'values') is True
    assert has_callables({'a': 1, 'b': 2, 'c': 3}, 'get', 'keys', 'items', 'values') is True
    assert has_callables({'a': 1, 'b': 2, 'c': 3}, 'get', 'keys', 'items', 'values', 'pop') is False

# Generated at 2022-06-13 20:43:55.187178
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserString,
    )
    from collections.abc import (
        Iterable,
        Iterator,
    )
    from decimal import Decimal
    import struct
    import sys
    import time
    import types

    if sys.version_info[0] > 2:
        # bytes
        assert has_any_callables(bytes(), '__iter__') is True

        # bytearray
        assert has_any_callables(bytearray(), '__iter__') is True

    # ChainMap
    assert has_any_callables(ChainMap(), '__iter__') is True

    # Counter
    assert has_any_callables(Counter(), 'most_common') is True

    # dict
   

# Generated at 2022-06-13 20:43:57.216294
# Unit test for function has_any_callables
def test_has_any_callables():
    """Check function has_any_callables"""
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:44:01.546997
# Unit test for function has_any_callables
def test_has_any_callables():
    assert True == has_any_callables(
        dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert False == has_any_callables(
        dict(), 'get', 'keys', 'items', 'values', 'something')



# Generated at 2022-06-13 20:44:10.766580
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(a=1, b=2),'get') == True
    assert has_any_callables(dict(a=1, b=2),'foo') == False



# Generated at 2022-06-13 20:44:14.089645
# Unit test for function has_any_callables
def test_has_any_callables():
    # Test case 1
    assert (has_any_callables(dict(),'get','keys','items','values','foo') == True)
    # Test case 2
    assert (has_any_callables(dict(),'get','keys','items','values','foo') == True)


# Generated at 2022-06-13 20:44:17.417256
# Unit test for function has_any_callables
def test_has_any_callables():
    # test a dictionary
    d = {'a': 1, 'b': 2}
    assert has_any_callables(d, 'keys', 'values', 'items', 'foo') is True



# Generated at 2022-06-13 20:44:20.146210
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(),'get','keys','items','values','something') is True


# Generated at 2022-06-13 20:44:32.638199
# Unit test for function has_callables
def test_has_callables():

    from collections import ChainMap

    assert has_callables({}, 'get', 'pop')
    assert not has_callables({}, 'get', 'pop', 'setdefault')

    assert has_callables(ChainMap(), 'get', 'pop', 'keys', 'values')
    assert not has_callables(ChainMap(), 'get', 'pop', 'setdefault')

    assert has_callables([], 'pop', 'remove')
    assert not has_callables([], 'pop', 'remove', 'sort')

    assert has_callables(tuple(), 'count')
    assert not has_callables(tuple(), 'count', 'pop')

    assert has_callables(set(), 'add')
    assert not has_callables(set(), 'add', 'difference')


# Generated at 2022-06-13 20:44:36.947803
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'keys','values','items','foo','copy','update') is True
    assert has_callables(obj, 'keys', 'values', 'items', 'foo', 'copy') is False
    assert has_callables(obj, 'nothing', 'foo', 'copy', 'update') is False

# Generated at 2022-06-13 20:44:39.841627
# Unit test for function has_attrs
def test_has_attrs():
    d = dict()
    assert has_attrs(d, 'get', 'items', 'keys', 'values') is True

# Generated at 2022-06-13 20:44:49.379620
# Unit test for function has_any_callables
def test_has_any_callables():
    from unittest import TestCase
    from types import FunctionType
    from collections import UserList
    class Class(object):
        a = 1
        def __init__(self):
            self.b = 2
    class Class1(object):
        def __init__(self):
            self.a = 1
            self.b = FunctionType(self)
        def b(self):
            pass
    class Test(TestCase):
        def test_has_any_callables(self):
            obj = Class1()
            self.assertTrue(has_any_callables(obj, 'a', 'b', 'c'))
            obj = Class()
            self.assertFalse(has_any_callables(obj, 'a', 'b', 'c'))
            obj = UserList()

# Generated at 2022-06-13 20:44:53.927152
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo1') == True


# Generated at 2022-06-13 20:44:57.906633
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1,b=2)
    attrs = ('get','keys','values','items')
    assert has_any_callables(obj, *attrs) is True


# Generated at 2022-06-13 20:45:04.019022
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')


# Generated at 2022-06-13 20:45:08.747869
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'items', 'values') == True
    assert has_callables(obj, 'get', 'keys', 'items', 'values', 'foo') == False


# Generated at 2022-06-13 20:45:12.341524
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') == True


# Generated at 2022-06-13 20:45:16.445087
# Unit test for function has_callables
def test_has_callables():
    """
    unit test for function has_callables
    """
    from flutils.objutils import has_callables
    assert has_callables(dict(), "get", "keys", "items", "values") is True



# Generated at 2022-06-13 20:45:29.221096
# Unit test for function has_any_callables
def test_has_any_callables():
    # Basic usage
    assert has_any_callables(2, 'bit_length') == True

    assert has_any_callables(2, 'bit_len') == False

    _dict = dict(a=1)
    assert has_any_callables(_dict, 'keys') == True

    assert has_any_callables(_dict, 'keys', 'items', 'values', 'foo') == True

    assert has_any_callables(_dict, 'keys', 'values', 'foo') == True

    assert has_any_callables(_dict, 'foo', 'bar', 'baz') == False

    _list = [1, 'a']
    assert has_any_callables(_list, 'index', 'append') == True

    assert has_any_callables(_list, 'index', 'append', 'foo') == True

   

# Generated at 2022-06-13 20:45:38.567908
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables
    """
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'setdefault') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'update') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'clear') is True


# Generated at 2022-06-13 20:45:40.815610
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'items', 'keys', 'values')



# Generated at 2022-06-13 20:45:49.129885
# Unit test for function has_any_callables
def test_has_any_callables():
    o = [1, 2, 3]
    assert has_any_callables(o, 'append') is True
    assert has_any_callables(o, 'foo') is False
    #
    o = ('foo', 'bar')
    assert has_any_callables(o, 'append') is False

# Generated at 2022-06-13 20:45:57.122395
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','values') is True
    obj_ = dict()
    assert has_any_callables(obj_,'get','values','foo') is True
    obj_.get = 'get'
    assert has_any_callables(obj_,'get','values','foo') is True
    obj_.foo = 'foo'
    assert has_any_callables(obj_,'get','values','foo') is False


# Generated at 2022-06-13 20:46:01.448481
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


if __name__ == '__main__':
    test_has_callables()

# Generated at 2022-06-13 20:46:21.305715
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test the function has_any_callables."""
    # noinspection SpellCheckingInspection
    oblist = [dict(a=1, b=2), dict(a=2, b=3), dict(a=3, b=4), dict(a=4, b=5)]
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'a', 'b', 'has_callables', 'foo') is False
    assert has_any_callables(oblist, 'append', 'pop', 'remove', 'insert', 'foo') is True
    assert has_any_callables(oblist, 'foo', 'bar', 'baz', 'foobar', 'barfoo') is False


# Generated at 2022-06-13 20:46:26.076452
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    result = has_any_callables(obj, 'keys', 'items', 'values', 'foo')
    assert result is True



# Generated at 2022-06-13 20:46:39.727093
# Unit test for function has_any_callables
def test_has_any_callables():
    # test that function does NOT return true for an object that does not have
    # any of the methods
    assert (has_any_callables(dict, 'test', 'foo', 'bar') is False)
    # test that function returns true for an object that has any of the methods
    assert (has_any_callables(dict, 'test', 'foo', 'items') is True)
    # test that function returns false for an object that has some, but not all
    # of the mehtods and not all of the methods are callable
    class Test:
        def test(self):
            pass

    test_obj = Test()
    assert (has_any_callables(test_obj, 'test', 'foo', 'items') is False)


# Generated at 2022-06-13 20:46:43.667807
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values')
    assert has_any_callables(dict(), 'get', 'items')



# Generated at 2022-06-13 20:46:45.551674
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items', 'foo')

# Generated at 2022-06-13 20:46:53.839769
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something')
    assert has_any_callables(dict(),'something') is False
    assert has_any_callables(dict(),'something', 'get')
    assert has_any_callables(dict(),'something', 'keys', 'items', 'values')
    assert has_any_callables(dict(),'something', 'keys', 'items', 'values')



# Generated at 2022-06-13 20:47:05.150332
# Unit test for function has_callables
def test_has_callables():
    import pytest
    from flutils.objutils import has_callables

    with pytest.raises(TypeError) as err:
        has_callables()

    assert 'missing 1 required positional argument' in str(err.value)

    with pytest.raises(TypeError) as err:
        has_callables(123)

    assert 'object is not iterable' in str(err.value)

    with pytest.raises(TypeError) as err:
        has_callables({})

    assert 'object is not iterable' in str(err.value)

    assert has_callables(
        dict(a=1, b=2),
        'get',
        'keys',
        'items',
        'values',
        'foo'
    ) == False

# Generated at 2022-06-13 20:47:15.042962
# Unit test for function has_any_callables

# Generated at 2022-06-13 20:47:17.492243
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:47:24.362685
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert (has_any_callables(dict(),'gsfgsg','ktey','item','values','foo') is
        False)



# Generated at 2022-06-13 20:47:38.595900
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')


# Generated at 2022-06-13 20:47:44.326763
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_callables('string', 'lower', 'upper') is True
    assert has_callables('string', 'lower', 'upper', 'foo') is False


# Generated at 2022-06-13 20:47:54.126596
# Unit test for function has_callables
def test_has_callables():
    test_obj = dict(k1='v1', k2='v2')
    attr_list = ['get', 'items', 'keys', 'values']
    for attr in attr_list:
        assert has_callables(test_obj, attr) is True
    assert has_callables(test_obj, 'get', 'items')
    assert has_callables(test_obj, 'keys')
    assert has_callables(test_obj, 'values')
    assert not has_callables(test_obj, 'foo')


# Generated at 2022-06-13 20:48:01.610704
# Unit test for function has_any_callables
def test_has_any_callables():
    list_to_test_against = [dict(),
                            list(),
                            set(),
                            tuple(),
                            frozenset(),
                            deque(),
                            Iterator,
                            ValuesView,
                            KeysView,
                            UserList]
    for obj in list_to_test_against:
        assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')

    assert has_any_callables(None, 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_any_callables(bool, 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_any_callables(bytes, 'get', 'keys', 'items', 'values', 'foo') is False

    # Using 'import collections'

# Generated at 2022-06-13 20:48:04.152848
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables({}, 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:48:12.267914
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict()
    assert has_any_callables(d, 'get', 'items') is True
    assert has_any_callables(d, 'get', 'items', 'foo') is True
    assert has_any_callables(d, 'get', 'items', 'foo', 'bar') is True
    assert has_any_callables(d, 'foo', 'bar') is False
    assert has_any_callables(d, 'foo') is False
    assert has_any_callables(d) is False

    def foo():
        pass

    assert has_any_callables(foo, '__call__', 'foo') is True
    assert has_any_callables(foo, 'foo') is False
    assert has_any_callables(foo) is False

    f = (i for i in range(10))

# Generated at 2022-06-13 20:48:19.907513
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict, 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict, 'get', 'keys', 'items', 'something') is False
    assert has_callables(dict, 'get', 'keys', 'bar', 'something') is False
    assert has_callables(list, 'append', 'insert', 'index', 'sort') is True
    assert has_callables(list, 'append', 'insert', 'index', 'something') is False



# Generated at 2022-06-13 20:48:24.917581
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo') is False



# Generated at 2022-06-13 20:48:26.824606
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') == True

# Generated at 2022-06-13 20:48:29.376955
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'foo')

