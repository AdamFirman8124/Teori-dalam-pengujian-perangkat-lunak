

# Generated at 2022-06-13 20:43:11.382743
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:43:23.494569
# Unit test for function has_callables
def test_has_callables():
    """
    Test that the has_callables function works as expected.
    """

    # Test with a required prop that is a function
    class TestA():

        def get_x(self):
            return True

    a = TestA()

    if not has_callables(a, 'get_x'):
        raise AssertionError()

    # Test with a required prop that is not a function
    class TestB():

        def __init__(self):
            self.x = 1

    b = TestB()

    if has_callables(b, 'x'):
        raise AssertionError()

    # Test with a required prop that does not exist
    class TestC():
        pass

    c = TestC()

    if has_callables(c, 'x'):
        raise AssertionError()

    #

# Generated at 2022-06-13 20:43:30.345162
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(), 'keys', 'values', 'items') is True
    assert has_any_attrs(dict(), 'keys', 'values', 'foo') is True
    assert has_any_attrs(dict(), 'foo', 'bar', 'baz') is False
    assert has_any_attrs(list(), 'append', 'insert', 'foo') is False
    return True



# Generated at 2022-06-13 20:43:39.459968
# Unit test for function has_any_callables
def test_has_any_callables():
    from unittest import TestCase
    from unittest.mock import MagicMock, patch, mock_open
    from collections import UserList

    class TestObj(UserList, object):
        def __init__(self, initlist=None):
            self.data = [1, 2]

        def foo(self, *args):
            return 'foo'

        def bar(self, *args):
            return 'bar'

    obj = TestObj()
    tc = TestCase()
    tc.assertTrue(has_any_callables(obj, 'foo', 'bar'))



# Generated at 2022-06-13 20:43:43.990151
# Unit test for function has_any_callables
def test_has_any_callables():
    myobject = {u'bar': u'foo', u'foo': u'bar'}
    assert has_any_callables(myobject, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(myobject, 'get', 'keys', 'items', 'values', 'foo', 'something') is True


# Generated at 2022-06-13 20:43:48.629473
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(open('foo.txt'), 'read', 'write', 'close')


# Generated at 2022-06-13 20:43:53.398705
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo') is False



# Generated at 2022-06-13 20:44:01.891175
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something')
    assert has_any_callables({'b':2}, 'get','keys','items','values')
    assert has_any_callables('hello', '__iter__','__contains__','__len__')
    assert not has_any_callables(dict(), 'something')
    assert not has_any_callables('hello', 'something')
    assert not has_any_callables(dict(), 'get', 'something')
    assert not has_any_callables('hello', '__iter__', 'something')


# Generated at 2022-06-13 20:44:05.307040
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables({'a', 'b', 'c'}, 'clear', 'add', 'remove', 'foo')



# Generated at 2022-06-13 20:44:07.982354
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')
    assert not has_callables(dict(),'get','keys','items','foo')

# Generated at 2022-06-13 20:44:14.565930
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(obj.keys(), 'get') is False
    assert has_any_callables(obj.keys(), 'get', 'foo') is False


# Generated at 2022-06-13 20:44:24.851858
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', '__add__') is False
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', '__init__') is False
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', '__int__') is False
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', '__class__') is False
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', '__doc__') is False

# Generated at 2022-06-13 20:44:32.517955
# Unit test for function has_any_callables
def test_has_any_callables():
    """
    >>> from flutils.objutils import has_any_callables
    >>> has_any_callables(dict(),'get','keys','items','values','foo')
    True
    >>> has_any_callables(dict(),'get','keys','items','values','foo_bar')
    False
    """


# Generated at 2022-06-13 20:44:36.551394
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo') is False

test_has_any_callables()

# Generated at 2022-06-13 20:44:39.253914
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:44:49.019948
# Unit test for function has_callables
def test_has_callables():
    if has_callables(dict(), 'get', 'keys', 'items', 'values') is False:
        assert False
    if has_callables(dict(), 'keys', 'items', 'values') is False:
        assert False
    if has_callables(dict(), 'keys', 'items') is False:
        assert False
    if has_callables(dict(), 'keys') is False:
        assert False
    if has_callables(dict(), 'foo', 'bar', 'baz') is True:
        assert False
    if has_callables(dict(a=1, b=2), 'get', 'keys', 'items', 'values') is False:
        assert False
    if has_callables(dict(a=1, b=2), 'keys', 'items', 'values') is False:
        assert False

# Generated at 2022-06-13 20:44:55.746036
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(obj, 'foo', 'bar', 'baz', 'blah') is False


# Generated at 2022-06-13 20:44:58.797626
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()
    assert has_any_callables(obj,'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:45:01.674379
# Unit test for function has_any_callables
def test_has_any_callables():
    d1 = dict()
    res = has_any_callables(d1, 'get', 'keys', 'items', 'values', 'foo')
    assert res



# Generated at 2022-06-13 20:45:11.721430
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(has_any_callables, '__call__', '__doc__') is True
    assert has_any_callables(dict(), 'get', 'foo') is True
    assert has_any_callables(dict(), 'foo') is False
    assert has_any_callables('str', 'upper', 'lower', 'join', 'format')
    assert has_any_callables('str', 'upper', 'lower', 'foo') is True
    assert has_any_callables('str', 'foo') is False
    assert has_any_callables('str', '__iter__') is False


# Generated at 2022-06-13 20:45:17.617431
# Unit test for function has_callables
def test_has_callables():
    d1 = dict(a=1, b=2)
    d2 = 'hello'
    assert has_callables(d1, 'get', 'values') == True
    assert has_callables(d2, 'get', 'values') == False


# Generated at 2022-06-13 20:45:23.999746
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_any_callables(dict(), 'get', 'keys', 'items', 'foo')
    assert not has_any_callables(dict(), 'get', 'keys', 'items')


# Generated at 2022-06-13 20:45:26.304541
# Unit test for function has_any_callables
def test_has_any_callables():
    ret=has_any_callables(dict(),'get','keys','items','values','foo')
    assert ret==True



# Generated at 2022-06-13 20:45:32.905445
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for ``has_any_callables``."""
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'something') is True


# Generated at 2022-06-13 20:45:45.638878
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import Callable, Iterator, ValuesView, KeysView, UserList
    import copy
    import types
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'get','keys','items','values') is True
    assert has_any_callables(dict(),'get','keys','items') is True
    assert has_any_callables((1,2,3),'sort','append','count') is True
    assert has_any_callables((1,2,3,4),'sort','append','reverse') is True
    assert has_any_callables(set(),'add','clear','copy','difference','issubset','remove','update') is True

# Generated at 2022-06-13 20:45:48.630020
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:45:55.493695
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import UserDict
    from collections.abc import UserList
    from typing import Counter

    assert has_any_callables('foo', 'lower', 'upper')
    assert has_any_callables(UserDict(), 'get', 'items', 'values')
    assert has_any_callables(UserList(), 'append', 'index')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_any_callables(Counter(), 'append', 'index')
    assert has_any_callables(23, 'bit_length', 'numerator')


# Generated at 2022-06-13 20:46:04.699326
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    from collections import OrderedDict
    from collections.abc import ValuesView, KeysView, UserDict
    obj = OrderedDict(a=1, b=2, c=3)
    assert has_any_callables(obj, 'values', 'keys', 'foo') is True
    assert has_any_callables(obj, 'a', 'b', 'c', 'foo') is False
    assert is_subclass_of_any(obj.keys(), ValuesView, KeysView, UserDict) is True

# Generated at 2022-06-13 20:46:09.990910
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(),'a') is True
    assert has_any_attrs(dict(),'foo') is False
    assert has_any_attrs(dict(),'get','keys','items','values','something') is True
    assert has_any_attrs(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:46:22.385382
# Unit test for function has_callables
def test_has_callables():
    assert has_callables({}, 'get', 'keys', 'items', 'values') is True
    assert has_callables({}, 'foo') is False
    assert has_callables({}, '__len__', 'copy') is True
    assert has_callables(lambda x: x, '__call__') is True
    assert has_callables(None, 'foo', 'bar') is False
    assert has_callables('foo', '__add__', 'upper') is True
    assert has_callables(True, '__bool__') is True
    assert has_callables(1, '__complex__', '__float__') is True
    assert has_callables(2.5, '__complex__', '__int__') is True
    assert has_callables(1 + 2j, '__abs__', '__bool__')

# Generated at 2022-06-13 20:46:45.866916
# Unit test for function has_any_callables
def test_has_any_callables():
    # Test 1: test that it correctly identifies that a dict has callables.
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    # Test 2: test that it correctly identifies that a dict does not have callables.
    assert has_any_callables(dict(),'get','keys','items','values','foo1') is False
    # Test 3: test that it correctly identifies that a list has callables.
    assert has_any_callables([1,2,3],'pop','append','sort','remove','foo') is True
    # Test 4: test that it correctly identifies that a list does not have callables.
    assert has_any_callables([1,2,3],'pop','append','sort','remove','foo1') is False
    # Test 5: test that it correctly identifies that a set

# Generated at 2022-06-13 20:46:58.428354
# Unit test for function has_any_callables
def test_has_any_callables():
    """Tests for function has_any_callables.
    """
    from flutils.objutils import has_any_callables

    data = []
    data.append((dict(), 'get', 'keys', 'items', 'values'))
    data.append((dict(), 'get', 'keys', 'items', 'values'))
    data.append((dict(a=1, b=2), 'get', 'keys', 'items', 'values'))
    data.append((dict(a=1, b=2), 'get', 'keys', 'items', 'values', 'foo'))
    data.append((dict(a=1, b=2), 'something', 'foo', 'anything'))
    data.append((None, 'something', 'foo', 'anything'))

# Generated at 2022-06-13 20:47:07.738995
# Unit test for function has_any_callables
def test_has_any_callables():
    # Test with different iterables and not iterables
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values',
                             'something')
    assert has_any_callables(["foo"], 'get', 'keys', 'items', 'values',
                             'something')
    assert has_any_callables({1, 2, 3}, 'get', 'keys', 'items', 'values',
                             'something')
    assert has_any_callables(tuple([1, 2, 3]), 'get', 'keys', 'items',
                             'values', 'something')
    assert has_any_callables(set(), 'get', 'keys', 'items', 'values',
                             'something')

# Generated at 2022-06-13 20:47:16.447093
# Unit test for function has_any_callables
def test_has_any_callables():
    # Test data
    data1 = dict()
    data2 = dict()
    data3 = 0, 1, 2
    data4 = 0, 1, 2, 3
    data5 = dict()
    data6 = dict()
    data7 = dict()
    data8 = dict()
    data9 = dict()
    data10 = dict()
    data11 = dict()
    data12 = dict()

    data1['name'] = 'Leon'
    data1['age'] = 52
    data2['name'] = 'Michelle'
    data2['age'] = 50
    data5['get'] = 'get'
    data5['keys'] = 'keys'
    data5['items'] = 'items'
    data5['values'] = 'values'
    data6['get'] = lambda *args, **kwargs: 'get'

# Generated at 2022-06-13 20:47:19.944294
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:47:31.172375
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'get','keys','items','values') is True
    assert has_any_callables(dict(),'get','keys','items') is True
    assert has_any_callables(dict(),'get','keys') is True
    assert has_any_callables(dict(),'get') is True
    assert has_any_callables(dict(),'foo') is False
    # EOF

# Generated at 2022-06-13 20:47:37.357660
# Unit test for function has_any_callables
def test_has_any_callables():

    class Test:

        def get(self):
            pass

        def keys(self):
            pass

        def items(self):
            pass

        def values(self):
            pass

    obj = Test()
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(obj, 'foo') is False



# Generated at 2022-06-13 20:47:45.243943
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import ChainMap, Counter, OrderedDict, UserDict, UserList, UserString, defaultdict
    from decimal import Decimal
    import threading
    threads = [threading.Thread(target=obj) for obj in [ChainMap, Counter, OrderedDict, UserDict, UserList, UserString, defaultdict, Decimal,
                                                        list, set, frozenset, tuple, deque, Iterator, ValuesView, KeysView, UserList]]
    [thread.start() for thread in threads]

# Generated at 2022-06-13 20:47:50.255474
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test the has_any_callables function."""
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:47:59.224272
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import defaultdict
    import json
    assert has_any_callables(defaultdict(int), '__setitem__', '__missing__', 'keys') is True
    assert has_any_callables(defaultdict(int), '__setitem__', '__missing__', 'foo') is False
    assert has_any_callables(json, 'load', 'loads', 'dumps') is True
    assert has_any_callables(json, 'load', 'loads', 'foo') is False
    assert has_any_callables(int, 'foo', 'bar', 'baz') is False
    assert has_any_callables(print, '__call__') is True
    assert has_any_callables(map, '__iter__') is True