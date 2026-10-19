

# Generated at 2022-06-13 20:43:16.240193
# Unit test for function has_any_callables
def test_has_any_callables():
    """
    Unit test for function has_any_callables
    """
    # print('{}...'.format(sys._getframe().f_code.co_name))
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(obj, 'get', 'foo', 'bar') is True
    assert has_any_callables(obj, 'get') is True
    assert has_any_callables(obj, 'foo', 'bar') is False



# Generated at 2022-06-13 20:43:19.186222
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:43:21.052378
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:43:23.028414
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(),'get','keys','items','values') == True
    assert has_any_attrs(dict(),'foo') == False


# Generated at 2022-06-13 20:43:26.672311
# Unit test for function has_any_attrs
def test_has_any_attrs():
    obj = dict(a=1, b=2, c=3)
    assert has_any_attrs(obj, 'get', 'keys', 'items', 'values', 'something')
    assert has_any_attrs(obj, '__doc__') is False
    assert has_any_attrs(obj, 'something') is False



# Generated at 2022-06-13 20:43:42.692892
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict()
    assert(has_any_callables(d,'get','keys','items','values','foo')
           == True)
    assert(has_any_callables(d,'get','keys','items','values','foo','bar')
           == True)
    assert(has_any_callables(d,'get','keys','items','values','foo','bar',
                             'foobar') == True)
    assert(has_any_callables(d,'get','keys','items','values','foo','bar',
                             'foobar','__getattribute__') == True)
    assert(has_any_callables(d,'get','keys','items','values','foo','bar',
                             'foobar','__getattribute__','__call__') == True)

# Generated at 2022-06-13 20:43:44.443719
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:43:50.127190
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'foo')
    assert has_any_callables(dict(), 'foo', 'get')
    assert not has_any_callables(dict(), 'foo', 'bar')
    assert not has_any_callables(123, 'foo', 'bar')


# Generated at 2022-06-13 20:43:52.538120
# Unit test for function has_any_callables
def test_has_any_callables():
    expected_results = True
    test_input = True
    assert has_any_callables(expected_results, 'get') == test_input

# Generated at 2022-06-13 20:43:55.755231
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items','values','foo') == True
    assert has_any_callables(dict(), 'foo', 'bar', 'baz','boz','bizzle') == False



# Generated at 2022-06-13 20:44:06.844181
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_attrs(dict(), 'keys', 'items', 'values') is True
    assert has_any_attrs(dict(), 'get', 'keys', 'values') is True
    assert has_any_attrs(dict(), 'get', 'items', 'values') is True
    assert has_any_attrs(dict(), 'get', 'keys', 'items') is True
    assert has_any_attrs(dict(), 'get') is True
    assert has_any_attrs(dict(), 'keys') is True
    assert has_any_attrs(dict(), 'items') is True
   

# Generated at 2022-06-13 20:44:09.855414
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'foo') is False


# Generated at 2022-06-13 20:44:13.514160
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert(has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'something'))
    assert(not has_any_attrs(None, 'get', 'keys', 'items', 'values', 'something'))


# Generated at 2022-06-13 20:44:18.101584
# Unit test for function has_attrs
def test_has_attrs():
    import unittest

    # Setup
    d = {'a': 1, 'b': 2, 'c': 3}

    # Run the tests
    class TestHasAttrs(unittest.TestCase):

        def test_has_all_attrs(self):
            self.assertTrue(has_attrs(d, '__getitem__', 'items', 'values'))

        def test_has_no_attrs(self):
            self.assertFalse(has_attrs(d, '__getitem__', 'foo', 'bar'))

        def test_has_some_attrs(self):
            self.assertFalse(has_attrs(d, '__getitem__', 'keys', 'bar'))


# Generated at 2022-06-13 20:44:22.786155
# Unit test for function has_any_attrs
def test_has_any_attrs():
    obj = dict(a=1, b=2)
    assert has_any_attrs(obj, 'get', 'keys', 'items', 'values', 'foo')
    obj = 'hello'
    assert has_any_attrs(obj, 'upper', 'swapcase', 'foo')


# Generated at 2022-06-13 20:44:25.443591
# Unit test for function has_any_callables
def test_has_any_callables():
    result = has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert result == True


# Generated at 2022-06-13 20:44:35.573064
# Unit test for function has_any_attrs
def test_has_any_attrs():
    from random import sample
    from flutils.objutils import has_any_attrs
    from flutils.randomutils import RandomString

    for i in range(1, 5):
        vals = sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', i)
        vals = ''.join(vals)
        assert len(vals) == i
        obj = {RandomString().get(): vals}
        assert has_any_attrs(obj, vals) is True
        assert has_any_attrs(obj, vals, 'Z') is True
        assert has_any_attrs(obj, 'Z') is False
        assert has_any_attrs(obj, *[]) is False
        assert has_any_attrs(obj, 'Z', *vals) is True



# Generated at 2022-06-13 20:44:38.393464
# Unit test for function has_any_callables
def test_has_any_callables():
    print(has_any_callables(dict(),'get','keys','items','values','foo'))


# Generated at 2022-06-13 20:44:41.039368
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:44:49.519553
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(
        dict(), 'get', 'keys', 'items', 'values', '__getitem__') is False
    assert has_any_callables(None, 'get', 'keys', 'items', 'values', '__getitem__') is False



# Generated at 2022-06-13 20:44:57.768548
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:45:03.328355
# Unit test for function has_attrs
def test_has_attrs():
    from flutils.objutils import has_attrs
    assert has_attrs(dict(), 'get') == True
    assert has_attrs(dict(), 'get', 'something') == False
    assert has_attrs(dict(), 'get', 'keys', 'items', 'values') == True
    assert has_attrs(dict(), 'get', 'keys', 'items', 'something', 'values') == False


# Generated at 2022-06-13 20:45:12.930947
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'foo')
    assert has_any_callables(dict(), 'keys', 'foo')
    assert has_any_callables(dict(), 'values', 'foo')
    assert has_any_callables(dict(), 'items', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items')
    assert not has_any_callables(dict(), 'foo')
    assert has_any_callables(dict(), 'foo', 'foo')
    assert has_any_callables(dict(), 'foo', 'foo', 'foo')



# Generated at 2022-06-13 20:45:20.635138
# Unit test for function has_any_callables
def test_has_any_callables():

    class TestClass0(object):

        def __init__(self):
            self.foo = lambda: 'hello'
            self.bar = 123

    assert has_any_callables(TestClass0(), 'foo', 'bar') is True
    assert has_any_callables(TestClass0(), 'foo', 'baz') is True
    assert has_any_callables(TestClass0(), 'baz') is False

    class TestClass1(object):

        def __init__(self):
            self.baz = 'hello'
            self.bar = 123

    assert has_any_callables(TestClass1(), 'baz', 'bar') is False
    assert has_any_callables(TestClass1(), 'baz', 'foo') is False


# Generated at 2022-06-13 20:45:25.578685
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'keys', 'items', 'values')
    assert not has_any_callables(obj, 'foo', 'foo2')



# Generated at 2022-06-13 20:45:38.775581
# Unit test for function has_callables
def test_has_callables():
    from pprint import pprint
    from collections import UserDict, Counter
    from decimal import Decimal
    from datetime import datetime
    from flutils.objutils import has_callables
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'items', 'values'), 'should return True'
    obj = UserDict(dict(a=1, b=2))
    assert has_callables(obj, 'get', 'keys', 'items', 'values'), 'should return True'
    obj = Counter(dict(a=1, b=2))
    assert has_callables(obj, 'get', 'keys', 'items', 'values'), 'should return True'
    obj = Decimal(123.45)

# Generated at 2022-06-13 20:45:44.506635
# Unit test for function has_any_callables
def test_has_any_callables():
    # Tested functions should have callables (as per documentation)
    # dict, list and set have all required callables so should return True
    assert has_any_callables(dict, 'keys', 'items', 'values') == True
    assert has_any_callables(list, 'append', 'clear', 'copy') == True
    assert has_any_callables(set, 'add', 'clear', 'copy') == True
    # dict, list and set do not have all required callables so should return False
    assert has_any_callables(dict, 'keys', 'items', 'values', 'something') == True
    assert has_any_callables(list, 'append', 'clear', 'copy', 'foo') == True
    assert has_any_callables(set, 'add', 'clear', 'copy', 'bar') == True
   

# Generated at 2022-06-13 20:45:57.920985
# Unit test for function has_callables
def test_has_callables():
    """Test the function :func:`has_callables <flutils.objutils.has_callables>`
    ."""
    # Test dict.
    obj = dict(a=1, b=2, c=3)
    assert has_callables(obj, 'clear', 'copy', 'keys', 'values', 'items') is True
    assert has_callables(obj, 'clear', 'copy', 'keys', 'values', 'foo') is False

    # Test list.
    obj = [10, 20, 30, 40, 50]
    assert has_callables(obj, 'append', 'clear', 'copy', 'count', 'extend') is True
    assert has_callables(obj, 'append', 'clear', 'copy', 'count', 'foo') is False

    # Test str.

# Generated at 2022-06-13 20:46:02.507725
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(dict(), 'something', 'somethingagain')



# Generated at 2022-06-13 20:46:07.156970
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something') == True
    assert has_any_callables(dict(),'something','somethingelse') == False


# Generated at 2022-06-13 20:46:15.314366
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:46:19.963557
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_any_callables('N/A', 'strip', 'lower', 'upper')
    assert not has_any_callables('N/A', 'strip', 'lower', 'upper', 'foo')

# Generated at 2022-06-13 20:46:22.835709
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables({}, 'values', 'foo')



# Generated at 2022-06-13 20:46:33.464624
# Unit test for function has_callables
def test_has_callables():
    print("\n***** Running test for function has_callables *****")
    import unittest
    import copy

    class MyDict(dict):
        pass

    class FooBar:
        def __init__(self):
            self.__foo = 1
            self.bar = 1

    class Foo:
        def foo(self):
            pass

    class Bar:
        def bar(self):
            pass

    class FooBarInstance(Foo, Bar):
        pass

    class FooChild(Foo):
        pass

    class BarChild(Bar):
        pass

    class FooBarChild(FooChild, BarChild):
        pass

    class MyList(list):
        pass

    class FooList:
        def append(self):
            pass

    class BarList:
        def extend(self):
            pass

   

# Generated at 2022-06-13 20:46:39.330089
# Unit test for function has_any_callables
def test_has_any_callables():
    for cls in (list, dict, ValuesView, KeysView, UserList):
        for attr in ('append', 'update', 'copy', 'something'):
            if has_any_callables(cls(), attr):
                break
        else:
            assert False
    return True


# Generated at 2022-06-13 20:46:48.746291
# Unit test for function has_any_callables
def test_has_any_callables():
    print('Testing has_any_callables ...')
    print('Testing various data types:')
    l = [0, 1, 2, 3]
    s = {0, 1, 2, 3}
    d = {0: 1, 1: 2, 2: 3, 3: 4}
    it = iter(l)
    for x, val in enumerate([True, False, False, False]):
        assert has_any_callables(l, '__getitem__', '__iter__', '__contains_') == val
    for x, val in enumerate([True, True, False, False]):
        assert has_any_callables(s, '__getitem__', '__iter__', '__contains__') == val

# Generated at 2022-06-13 20:46:56.571105
# Unit test for function has_attrs
def test_has_attrs():
    assert has_attrs(dict(),'get','keys','items','values')
    assert hasattr({}, 'get') is True
    assert has_attrs({}, 'get', 'something') is False
    assert has_attrs({}, 'get', '__getitem__') is True
    assert hasattr({}, 'something') is False
    assert has_attrs('[a,b,c]', '__iter__', '__getitem__') is True


# Generated at 2022-06-13 20:47:09.130804
# Unit test for function has_callables

# Generated at 2022-06-13 20:47:12.285544
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),"get","keys","items","values") is True


# Generated at 2022-06-13 20:47:15.224074
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:47:23.317226
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:47:24.609218
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(set(), 'isdisjoint', 'add') == True

# Generated at 2022-06-13 20:47:39.774748
# Unit test for function has_callables
def test_has_callables():
    from collections import OrderedDict
    from datetime import date
    from decimal import Decimal
    from operator import itemgetter
    from operator import itemsetter
    from types import MethodType
    from types import SimpleNamespace
    from typing import NamedTuple
    from typing import Type

    # Iterator objects
    a = (1, 2, 3)
    b = [1, 2, 3]
    c = iter(b)
    d = map(str, b)
    e = reversed(b)
    f = list(filter(None, b))
    g = filter(None, c)
    h = KeysView({'a': 1, 'b': 2, 'c': 3})
    i = ValuesView({'a': 1, 'b': 2, 'c': 3})
    j = UserList(b)
    k

# Generated at 2022-06-13 20:47:48.890118
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables({}, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(has_any_callables, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(has_any_callables, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(has_any_callables, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(has_any_callables, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_

# Generated at 2022-06-13 20:47:59.128218
# Unit test for function has_callables
def test_has_callables():
    assert(has_callables(dict(a=1, b=2), 'keys', 'items', 'values', 'get') == True)
    assert(has_callables(dict(a=1, b=2), 'keys', 'items', 'values') == True)
    assert(has_callables(dict(a=1, b=2), 'key', 'items', 'values') == False)
    assert(has_callables(dict(a=1, b=2), 'key', 'items', 'values', 'get') == False)
    assert(has_callables(dict(a=1, b=2), 'key', 'items', 'values', 'foo') == False)
    assert(has_callables(dict(a=1, b=2), 'key', 'items', 'values', 'foo') == False)
   

# Generated at 2022-06-13 20:48:04.698868
# Unit test for function has_any_callables
def test_has_any_callables():
    """Verify that the objectutils.has_any_callables() is working correctly
    """
    import unittest
    import inspect
    from flutils.objutils import has_any_callables

    class TestObj:
        def __init__(self):
            self.x = "Hello, World!"

        def foo(self):
            return

    class Tester(unittest.TestCase):
        """Test the has_any_callables() function"""
        def test_empty_args(self):
            """Ensure that the has_any_callables() returns False when given
            and empty list of args.
            """

# Generated at 2022-06-13 20:48:11.664366
# Unit test for function has_callables
def test_has_callables():
    obj = dict(
        foobar='baz',
        foo={
            'bar': 'baz',
            'baz': 'foo',
            'foo': 'bar'
        }
    )
    assert has_callables(obj, 'get', 'items', 'keys', 'values') is True
    assert has_callables(obj, 'get', 'items', 'keys', 'values', '__setattr__') is True
    assert has_callables(obj, 'get', 'items', 'keys', 'values', 'foobar') is False
    assert has_callables(obj, 'get', 'items', 'keys', 'values', 'foo') is False



# Generated at 2022-06-13 20:48:13.673508
# Unit test for function has_any_callables
def test_has_any_callables():
    """
    :return: True if the function returns True when given a dictionary for the object and get or keys for the attributes, False otherwise
    """
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys') == True



# Generated at 2022-06-13 20:48:30.257849
# Unit test for function has_callables
def test_has_callables():
    from functools import partial
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserString,
    )
    from flutils.objutils import has_callables

    # Testing negative cases
    assert has_callables(None, '__getitem__') is False
    assert has_callables(True, '__getitem__') is False
    assert has_callables(False, '__getitem__') is False
    assert has_callables(1, '__getitem__') is False
    assert has_callables(1.0, '__getitem__') is False
    assert has_callables('', '__getitem__') is False
    assert has_callables(b'', '__getitem__') is False

# Generated at 2022-06-13 20:48:33.391505
# Unit test for function has_callables
def test_has_callables():
    assert(has_callables(dict(), 'get', 'keys', 'items', 'values') is True)
    assert(has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False)



# Generated at 2022-06-13 20:48:48.238121
# Unit test for function has_callables
def test_has_callables():
    from collections import defaultdict
    assert has_callables(defaultdict(int), 'get', 'keys', 'values', 'items') is True
    assert has_callables(defaultdict(int), 'get', 'keys', 'values') is False
    assert has_callables(defaultdict(int), 'get_', 'keys', 'values', 'items') is False
    assert has_callables(defaultdict(int), 'get', 'keys_', 'values', 'items') is False
    assert has_callables(defaultdict(int), 'get', 'keys', 'values_', 'items') is False
    assert has_callables(defaultdict(int), 'get', 'keys', 'values', 'items_') is False

# Generated at 2022-06-13 20:48:56.953263
# Unit test for function has_any_callables
def test_has_any_callables():
    dict1 = dict(a=1, b=2)
    dict2 = dict()
    ans = has_any_callables(dict1, "get", "keys", "items", "something")
    assert ans == True
    ans = has_any_callables(dict1, "something")
    assert ans == False
    ans = has_any_callables(dict2, "get", "keys", "items", "something")
    assert ans == False
    ans = has_any_callables(dict1, "get", "keys", "items", "something")
    assert ans == True
    ans = has_any_callables(dict1, "something")
    assert ans == False


# Generated at 2022-06-13 20:48:58.928602
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'keys', 'values')


# Generated at 2022-06-13 20:49:01.937620
# Unit test for function has_callables
def test_has_callables():
    """
    Test the has_callables function
    """
    obj0 = dict()
    attrs0 = {'get', 'items', 'keys', 'values'}
    assert has_callables(obj0, *attrs0) is True



# Generated at 2022-06-13 20:49:05.621914
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = [1,2,3]
    assert has_any_callables(obj, 'sort') == True
    assert has_any_callables(obj, 'foo') == False

test_has_any_callables()



# Generated at 2022-06-13 20:49:07.581388
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True


# Generated at 2022-06-13 20:49:18.959048
# Unit test for function has_callables
def test_has_callables():
    import pytest
    from collections import UserList

    class FooBar(UserList):
        """A class with 3 attributes.
        """
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        def foo(self, *args, **kwargs):
            return self

        def bar(self, *args, **kwargs):
            return self

        def foobar(self, *args, **kwargs):
            return self

    obj = FooBar()
    assert has_callables(obj, 'foo', 'bar', 'foobar', 'baz') is False
    assert has_callables(obj, 'foo', 'bar') is True
    assert has_callables(obj, 'foo') is True
    with pytest.raises(AttributeError):
        has_

# Generated at 2022-06-13 20:49:21.017111
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','random')


# Generated at 2022-06-13 20:49:28.452676
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'items', 'values') == True
    assert has_callables(obj, 'get', 'keys', 'items') == True
    assert has_callables(obj, 'get', 'keys') == True
    assert has_callables(obj, 'get') == True
    assert has_callables(obj, 'foo') == False
    assert has_callables(obj, 'foo', 'bar') == False


# Generated at 2022-06-13 20:49:40.725235
# Unit test for function has_callables
def test_has_callables():
    from collections import OrderedDict
    from collections.abc import Mapping
    assert has_callables(OrderedDict(), 'keys', 'get') is True
    assert has_callables(OrderedDict(), 'keys', 'get', 'something') is False
    assert has_callables(OrderedDict(), 'keys', 'values', 'something') is False
    assert has_callables(OrderedDict(), 'keys', 'items', 'something') is False
    assert has_callables(dict(), 'keys', 'items') is True
    assert has_callables(dict(), 'keys', 'items', 'something') is False
    assert has_callables(dict(), 'keys', 'something') is False
    assert has_callables(dict(), 'something') is False
    assert has_callables(Mapping, 'keys', 'something')

# Generated at 2022-06-13 20:49:50.837550
# Unit test for function has_any_callables
def test_has_any_callables():
    attrs = ['get','keys','items','values','foo']
    obj = dict()
    has_any_callables(obj, *attrs)
    assert True == has_any_callables(obj, *attrs)

# Generated at 2022-06-13 20:50:04.514940
# Unit test for function has_callables
def test_has_callables():
    """Test the has_callables function."""
    from collections import OrderedDict
    import decimal
    from datetime import datetime
    from flutils.objutils import has_callables
    from pydantic import BaseModel

    class TestModel(BaseModel):
        """Test class for has_callables function."""
        a: int
        b: int
        c: int

    assert has_callables(TestModel(a=1, b=2, c=3), 'a', 'b', 'c') is True
    assert has_callables(TestModel(a=1, b=2, c=3), 'a', 'b', 'c', 'd') is True

# Generated at 2022-06-13 20:50:15.447690
# Unit test for function has_callables
def test_has_callables():
    def foo():
        return True

    def bar():
        return False
    class Foo():
        def __init__(self):
            self.foo=foo
            self.foobar=bar
            self.bar=bar

    class Bar():
        def __init__(self):
            self.foo=foo
            self.foobar=bar
        def bar(self):
            return False

    assert has_callables(Foo(),'foo','foobar','bar') == True
    assert has_callables(Bar(),'foo','foobar','bar') == False
    assert has_callables(Foo(),'foo','') == False

# Generated at 2022-06-13 20:50:18.009474
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'foo') is False


# Generated at 2022-06-13 20:50:19.594716
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict, "items", "values") is True



# Generated at 2022-06-13 20:50:21.655700
# Unit test for function has_any_callables
def test_has_any_callables():
    from inspect import signature, isfunction
    from flutils.objutils import has_any_callables



# Generated at 2022-06-13 20:50:26.762413
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(None,'get','keys','items','values','foo') is False
    assert has_any_callables(dict(),'get','keys','items','values','foo','pop')
    assert has_any_callables(dict(),'foo','bar') is False



# Generated at 2022-06-13 20:50:31.281453
# Unit test for function has_callables
def test_has_callables():
    mydict = {'a':1,'b':2}
    assert has_callables(mydict.keys(),"__iter__")
    assert has_callables(list(mydict.keys()),"__iter__")
    assert has_callables(mydict.keys(),"__iter__","__len__")
    assert not has_callables(mydict.keys(),"__len__")
    assert not has_callables(mydict.keys(),"__class__")

# Generated at 2022-06-13 20:50:33.964341
# Unit test for function has_callables
def test_has_callables():
    import flutils.objutils
    assert flutils.objutils.has_callables(dict(), 'get', 'keys', 'items', 'values') == True


# Generated at 2022-06-13 20:50:35.877512
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict, 'get', 'keys', 'items', 'values')



# Generated at 2022-06-13 20:50:50.771913
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import UserDict, OrderedDict, ChainMap, namedtuple

    kwargs = dict(
        a=1,
        b=2,
        c=3,
    )

    assert has_any_callables(UserDict(), *(kwargs.keys())) is True
    assert has_any_callables(OrderedDict(), *(kwargs.keys())) is True
    assert has_any_callables(ChainMap(), *(kwargs.keys())) is True

    Point = namedtuple('Point', 'x y')
    pt = Point(x=0, y=0)

    assert has_any_callables(pt, *(kwargs.keys())) is False

# Generated at 2022-06-13 20:51:03.154675
# Unit test for function has_any_callables
def test_has_any_callables():
    tests = (
            (None, 'foo', 'bar', 'lorem', 'ipsum', 'dolor'),
            1,
            [1, 2, 3, 4],
            frozenset({'a', 'b', 'c', 'd'}),
            (1, 2, 3, 4, 5),
            bool,
            range(1, 6),
            'hello',
            dict(a=1, b=2),
            dict(zip(range(1, 6), range(1, 6))),
            (lambda x: x),
            {'a': 1, 'b': 2, 'c': 3, 'd': 4},
            {1, 2, 3, 4},
    )
    for test in tests:
        name = test.__class__.__name__
        assert name != 'dict'

# Generated at 2022-06-13 20:51:07.525551
# Unit test for function has_any_callables
def test_has_any_callables():

    assert(has_any_callables(dict(),'get','keys','items','values','foo') == True)

    assert(has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True)


# Generated at 2022-06-13 20:51:18.581236
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict(), 'get', 'keys', 'items', '__iter__')
    assert has_callables(dict(), 'get', 'keys', 'items', '__contains__')
    assert has_callables(dict(), 'get', 'keys', 'items', 'pop')
    assert has_callables(dict(), 'get', 'keys', 'items', 'popitem')
    assert has_callables(dict(), 'get', 'keys', 'items', 'setdefault')
    assert has_callables(dict(), 'get', 'keys', 'items', 'update')
    assert not has_callables(dict(), 'get', 'keys', 'items', '_abc')

# Generated at 2022-06-13 20:51:21.864253
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'foo') is False
    assert has_any_callables(dict(), 'clear') is True



# Generated at 2022-06-13 20:51:24.313501
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values',
                             'something') is True



# Generated at 2022-06-13 20:51:30.209367
# Unit test for function has_callables
def test_has_callables():
    from collections import namedtuple
    Foo = namedtuple('Foo', ['values', 'keys'])
    obj1 = Foo({'a': 1, 'b': 2}, None)
    assert has_callables(obj1, 'values')



# Generated at 2022-06-13 20:51:36.514919
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys') == True
    assert has_callables(obj, 'some_iter', 'keys') == False
    assert has_callables(obj, 'some_iter', 'keys', 'a') == False


# Generated at 2022-06-13 20:51:39.654217
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert not has_any_callables(dict(),'foo','bar','foobar','foobarbaz')


# Generated at 2022-06-13 20:51:44.851167
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') == True
    assert has_callables(dict(),'something') == False


# Generated at 2022-06-13 20:52:01.300831
# Unit test for function has_any_callables
def test_has_any_callables():
    a = {1,2,3}
    b = []
    c = 'xyz'
    assert not has_any_callables(a,'remove','append')
    assert not has_any_callables(b,'remove','append')
    assert not has_any_callables(c,'remove','append')


# Generated at 2022-06-13 20:52:05.463894
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')


# Generated at 2022-06-13 20:52:18.136671
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), "keys", "items", "values")
    assert has_any_callables(dict(), "keys", "items", "values", "foo")
    assert has_any_callables(dict(), "keys", "items", "values", "get")
    assert has_any_callables(dict(), "keys", "items", "values", "foo", "get")
    assert not has_any_callables(dict(), "foo", "bar", "baz")
    assert has_any_callables("test", "strip", "split", "upper")
    assert not has_any_callables("test", "foo", "bar", "baz")


# Generated at 2022-06-13 20:52:26.419449
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True
    assert has_callables(dict(),'get','keys','items','values', 'foo') is False
    assert has_callables(dict(),'get') is True
    assert has_callables(dict(),'foobar') is False


# Generated at 2022-06-13 20:52:31.520106
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'items') is True, 'ValuesView is list-like'
    assert has_callables(obj, 'something') is False, 'Missing attr "something"'
    assert has_callables(obj, 'update') is True, '"update" is callable'



# Generated at 2022-06-13 20:52:37.134395
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo1')


# Generated at 2022-06-13 20:52:40.082060
# Unit test for function has_any_callables
def test_has_any_callables():
    list_obj = [1,2,3]
    assert has_any_callables(list_obj, 'append', 'pop') == True



# Generated at 2022-06-13 20:52:43.035840
# Unit test for function has_any_callables
def test_has_any_callables():
    expected= True
    assert has_any_callables(dict(),'get','keys','items','values','foo') == expected


# Generated at 2022-06-13 20:52:48.233525
# Unit test for function has_callables
def test_has_callables():
    """
    Check that function has_callables works as expected
    """
    assert has_callables(dict(),'get','keys','items','values') == True
    assert has_callables(dict(),'gett','keys','items','values') == False
    assert has_callables(dict(a=1,b=2),'get','keys','items','values') == True



# Generated at 2022-06-13 20:52:50.822032
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(dict(),'get','keys','items','values','something'))

