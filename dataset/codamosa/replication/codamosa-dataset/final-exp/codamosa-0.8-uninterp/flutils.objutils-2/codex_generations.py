

# Generated at 2022-06-13 20:43:21.555454
# Unit test for function has_callables
def test_has_callables():
    obj = object()
    assert has_callables(obj, "foo") == False
    assert has_callables(obj) == False
    assert has_callables(object(), "foo", "bar") == False

    class Foobar(object):
        @staticmethod
        def foo():
            pass

        @staticmethod
        def bar():
            pass

        @staticmethod
        def baz():
            pass

    foobar = Foobar()
    assert has_callables(foobar, "foo", "bar", "baz") == False
    assert has_callables(foobar, "foo") == False

    class Baz(object):
        @staticmethod
        def baz():
            pass

    baz = Baz()
    assert has_callables(baz, "baz") == True


# Generated at 2022-06-13 20:43:24.509008
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'keys', 'get') is True
    assert has_any_callables(dict(), 'keys', 'some_nonexistent_method') is False
    assert has_any_callables(1, 'keys', 'get') is False
    assert has_any_callables(dict(), 'foo', 'bar') is False


# Generated at 2022-06-13 20:43:28.400010
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(list(), 'index', 'count', 'append') == True
    return 0

if __name__ == "__main__":
    test_has_callables()

# Generated at 2022-06-13 20:43:30.573350
# Unit test for function has_any_callables
def test_has_any_callables():
    print(has_any_callables(dict(),'keys','items','values','foo'))

# Generated at 2022-06-13 20:43:34.057053
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:43:38.213044
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = {1, 2, 3}
    assert has_any_callables(obj, "pop", "add", "foo") is True
    assert has_any_callables(obj, "pop", "bar", "foo") is False



# Generated at 2022-06-13 20:43:41.148349
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(str(), 'startswith', 'isalnum', 'title') is True


# Generated at 2022-06-13 20:43:43.382563
# Unit test for function has_callables
def test_has_callables():
    a = dict()
    assert has_callables(a, "get", "keys", "items", "values") is True


# Generated at 2022-06-13 20:43:48.414653
# Unit test for function has_callables
def test_has_callables():
    _obj = dict(a=1,b=2)
    _expt_result = True
    _result = has_callables(_obj,'keys','items','values','pop','update','get','foo')
    assert _expt_result == _result


# Generated at 2022-06-13 20:43:52.402672
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')

# Generated at 2022-06-13 20:44:02.115145
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(list, 'get', 'keys', 'items', 'values') is False
    assert has_any_callables(list, 'append', 'extend', 'clear') is True


# Generated at 2022-06-13 20:44:13.825669
# Unit test for function has_callables
def test_has_callables():
    from collections import Counter, ChainMap
    dict1 = dict(a=1, b=2, c=3)
    dict2 = dict(d=4, e=5, f=6)
    dict3 = dict(g=7, h=8, i=9)
    cm = ChainMap(dict1, dict2, dict3)
    assert has_callables(dict1, "get", "keys", "items", "values", "keys")
    assert not has_callables(dict1, "get", "keys", "items", "values", "foo")
    assert has_callables(Counter(dict1), "get", "keys", "items", "values", "keys")
    assert not has_callables(Counter(dict1), "get", "keys", "items", "values", "foo")

# Generated at 2022-06-13 20:44:16.498246
# Unit test for function has_any_callables
def test_has_any_callables():
    f = has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert f is True

# Generated at 2022-06-13 20:44:24.761329
# Unit test for function has_callables
def test_has_callables():
    from flutils.objutils import has_callables
    from collections import UserList
    assert has_callables(UserList(), "append") is True
    assert has_callables(UserList(), "append", "extend") is True
    assert has_callables(UserList(), "append", "foo") is False
    assert has_callables(UserList(), "append", "foo", "bar") is False
    assert has_callables("hello", "upper") is True
    assert has_callables("hello", "upper", "strip") is True
    assert has_callables("hello", "upper", "foo") is False
    return


# Generated at 2022-06-13 20:44:31.284417
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), "get", "keys", "items", "values", "foo")
    assert has_any_callables(dict(), "get", "foo")
    assert not has_any_callables(dict(), "foo", "bar")



# Generated at 2022-06-13 20:44:39.370833
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(a=1,b=2),'get','keys','items','values','foo')
    assert has_any_callables('hello','upper','lower','capitalize','foo')
    assert has_any_callables(list(),'append','insert','remove','foo')
    assert has_any_callables(list([1,2,3]),'append','insert','remove','foo')
    assert has_any_callables(set(),'add','discard','foo')
    assert has_any_callables(set([1,2,3]),'add','discard','foo')
    assert has_any_callables(frozenset(),'foo')

# Generated at 2022-06-13 20:44:41.395626
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:44:52.979809
# Unit test for function has_callables
def test_has_callables():
    import unittest

    class TestHasCallables(unittest.TestCase):
        """Unit tests for function has_callables."""

        def test_has_callables(self):
            """Test has_callables with valid data."""
            self.assertTrue(has_callables(dict(), 'get', 'keys', 'items', 'values'))
            self.assertTrue(has_callables(dict(), 'get', 'update'))
            self.assertTrue(has_callables((), 'count'))

            self.assertFalse(has_callables({}, 'get', 'keys', 'items', 'values', 'something'))
            self.assertFalse(has_callables(dict(), 'get', 'keys', 'items', 'values', 'something'))

# Generated at 2022-06-13 20:45:04.305394
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = {'name':'lisa'}
    class C(dict):
        @staticmethod
        def clsmethod(cls):
            pass
        @classmethod
        def clsmethod1(cls):
            pass
        def method(self):
            pass

    obj1 = C()
    assert(has_any_callables(obj,'keys') == True)
    assert(has_any_callables(obj1,'keys','clsmethod','clsmethod1','method') == True)
    assert(has_any_callables(obj1,'keys','clsmethod','clsmethod1','method','name') == True)
    assert(has_any_callables(obj1,'keys','clsmethod','clsmethod1','method','name','gender') == False)

# Generated at 2022-06-13 20:45:08.338189
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True

    assert has_any_callables(dict(),'get','keys','items','values','something') == True


# Generated at 2022-06-13 20:45:20.634108
# Unit test for function has_callables
def test_has_callables():
    d = dict(a=1, b=2)
    assert has_callables(d, 'get', 'keys', 'items', 'values') is True
    assert has_callables(d, 'nonexistant', 'keys', 'items', 'values') is False
    assert has_callables(d, 'get', 'nonexistant', 'items', 'values') is False
    assert has_callables(d, 'get', 'keys', 'nonexistant', 'values') is False
    assert has_callables(d, 'get', 'keys', 'items', 'nonexistant') is False
    assert has_callables(d, 'nonexistant', 'nonexistant', 'nonexistant', 'nonexistant') is False



# Generated at 2022-06-13 20:45:31.254941
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(1) == False
    assert has_callables(1, 'bit_length') == False
    assert has_callables(['a', 'b'], 'sort') == True
    assert has_callables([], 'sort') == True
    assert has_callables(['a', 'b']) == False
    assert has_callables((1, 2, 3), 'append') == False
    assert has_callables({'a': 1, 'b': 2}, 'pop') == True
    assert has_callables(None, 'pop') == False
    assert has_callables(NotImplemented, 'pop') == False
    assert has_callables(True, 'pop') == False
    assert has_callables(False, 'pop') == False
    assert has_callables('', 'pop') == False


# Generated at 2022-06-13 20:45:39.834025
# Unit test for function has_callables
def test_has_callables():
    """Test function has_callables

    This function tests that has_callables function works properly
    """
    result = True
    if not has_callables(dict(), 'keys'):
        print("Test 1 failed: has_callables(dict(), 'keys')")
        result = False
    if not has_callables(dict(), 'get', 'keys'):
        print("Test 2 failed: has_callables(dict(), 'keys')")
        result = False
    if not has_callables(dict(), 'get', 'values', 'keys', 'items'):
        print("Test 3 failed: has_callables(dict(), 'keys')")
        result = False

# Generated at 2022-06-13 20:45:49.569914
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(obj, 'get', 'something', 'items', 'values', 'foo')
    assert has_any_callables(obj, 'something', 'foo', 'bar')

# Generated at 2022-06-13 20:45:58.842925
# Unit test for function has_any_callables
def test_has_any_callables():
    from unittest import main, TestCase

    class TestHasAnyCallables(TestCase):

        def test_has_any_callables(self):
            class Foo(object):
                x = 2

                def __init__(self):
                    self.x = 2

                def __call__(self):
                    return 'call'

                def __repr__(self):
                    return 'repr'

                def __str__(self):
                    return 'str'

            obj = Foo()
            self.assertTrue(has_any_callables(obj, '__repr__', '__str__'))
            self.assertFalse(has_any_callables(obj, 'x', '__repr__'))

    main()


# Generated at 2022-06-13 20:46:03.175243
# Unit test for function has_callables
def test_has_callables():
    """Unit test for function has_callables."""
    from collections import Counter
    assert has_callables(Counter(), 'values', 'get', '__getitem__', 'most_common') is True


# Generated at 2022-06-13 20:46:11.482181
# Unit test for function has_any_callables
def test_has_any_callables():
    assert (has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo'))
    assert (has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True)
    assert (has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True)
    assert not (has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == False)
    assert not (has_any_attrs(dict(), 'get', 'keys', 'items', 'values') == True)



# Generated at 2022-06-13 20:46:19.593840
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test the module-level function has_any_callables."""

    from collections import ChainMap
    from flutils.objutils import has_any_callables
    from typing import Any

    obj = ChainMap(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(obj, 'foo', 'something_else')



# Generated at 2022-06-13 20:46:32.550382
# Unit test for function has_callables
def test_has_callables():
    from collections import Counter
    from collections.abc import ValuesView, KeysView, UserList
    from unittest import TestCase

    class TestObject:
        def foo(self):
            pass

        def bar(self):
            pass

    obj = TestObject()

    class TestHasCallables(TestCase):
        def test_with_single_callable_args(self):
            self.assertTrue(has_callables(obj, 'foo'))

        def test_with_single_non_callable_args(self):
            self.assertFalse(has_callables(obj, 'bar'))

        def test_with_non_existing_args(self):
            self.assertFalse(has_callables(obj, 'baz'))


# Generated at 2022-06-13 20:46:46.310653
# Unit test for function has_callables
def test_has_callables():
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserList,
        UserString,
        defaultdict,
    )
    import decimal
    import enum
    import re

    retval = has_callables(
        dict(),
        'get',
        'keys',
        'items',
        'values',
    )
    assert retval is True

    retval = has_callables(
        tuple(),
        'get',
        'keys',
        'items',
        'values',
    )
    assert retval is True
    retval = has_callables(
        list(),
        'get',
        'keys',
        'items',
        'values',
    )
    assert retval is True

# Generated at 2022-06-13 20:46:55.350319
# Unit test for function has_callables
def test_has_callables():
    assert True  == has_callables(dict(), 'clear', 'copy', 'fromkeys', 'get')
    assert False == has_callables(dict(), 'clear', 'copy', 'fromkeys', 'foo')


# Generated at 2022-06-13 20:47:03.046575
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import UserDict

    class MyClass(UserDict):
        @staticmethod
        def func():
            pass

    class NewClass(MyClass):
        def func(self):
            pass

    new_instance = NewClass()

    assert has_any_callables(new_instance, 'func') is True
    assert has_any_callables(new_instance, 'len') is True
    assert has_any_callables(new_instance, 'x', 'foo') is False

# Generated at 2022-06-13 20:47:06.714471
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = {}
    assert(has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo'))



# Generated at 2022-06-13 20:47:09.628907
# Unit test for function has_callables
def test_has_callables():
  assert has_callables(dict(),'keys','values')
  obj = dict(a=1)
  assert not has_callables(obj,'has_callables')


# Generated at 2022-06-13 20:47:17.551774
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'foo','bar','baz') is False
    assert has_any_callables('hello', 'join', 'split') is False
    assert has_any_callables(list(), 'append', 'remove') is True
    assert has_any_callables(list(), 'foo', 'bar') is False
    assert has_any_callables(sorted([1, 2, 3]), 'isalpha', 'isnumeric') is False
    assert has_any_callables(sorted([1, 2, 3]), 'sort', 'append') is True
    assert has_any_callables(set([1, 2, 3]), 'add', 'remove') is True

# Generated at 2022-06-13 20:47:24.447605
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True
    assert has_callables(dict(),'get','keys','items','values','foo') is True
    assert has_callables(dict(),'keys','items','values','foo') is False

# Generated at 2022-06-13 20:47:39.714403
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = 'hello'
    assert has_any_callables(obj, 'split', 'upper', 'foo') == True

    obj = 'hello'
    assert has_any_callables(obj, 'split', 'upper', 'lower') == True

    obj = 'hello'
    assert has_any_callables(obj, 'foo', 'bar', 'baz') == False

    obj = list(range(5))
    assert has_any_callables(obj, 'pop', 'index', 'insert') == True

    obj = list(range(5))
    assert has_any_callables(obj, 'pop', 'index', 'foo') == True

    obj = list(range(5))
    assert has_any_callables(obj, 'foo', 'bar', 'baz') == False


# Generated at 2022-06-13 20:47:45.384852
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    from collections import Counter
    assert has_callables(Counter(), 'get', 'keys', 'items', 'values') is False
    assert has_callables(Counter(), 'get', 'keys', 'items', 'values', 'foo') is False



# Generated at 2022-06-13 20:47:57.320015
# Unit test for function has_any_callables
def test_has_any_callables():
    import os
    osdict = os.__dict__

# Generated at 2022-06-13 20:48:01.262711
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True

# Generated at 2022-06-13 20:48:22.170381
# Unit test for function has_callables
def test_has_callables():
    class TestClass:
        def test_func_str():
            return "Hello there"

    obj = TestClass()
    assert has_callables(obj, 'test_func_str')



# Generated at 2022-06-13 20:48:23.452268
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:48:26.621979
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:48:32.303408
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1, b=2)
    assert has_any_callables(d, 'keys', 'values', 'items')
    assert has_any_callables(d, 'keys', 'values', 'items', 'clear')
    assert has_any_callables(d, 'keys', 'values', 'items', 'foo')


# Generated at 2022-06-13 20:48:34.070912
# Unit test for function has_callables
def test_has_callables():
    d = dict(foo=0)
    assert has_callables(d, 'get', 'keys', 'items', 'values') is True



# Generated at 2022-06-13 20:48:35.526830
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:48:47.040714
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys') is True
    assert has_callables(dict(), 'get') is True
    assert has_callables(dict(), 'foo') is False
    assert has_callables(dict(), 'foo', 'bar') is False
    assert has_callables(dict(), 'foo', 'get') is False
    assert has_callables(dict(), 'foo', 'bar', 'get') is False
    assert has_callables(dict(), 'foo', 'bar', 'get', 'keys') is False
    assert has_callables(dict(), 'foo', 'bar', 'get', 'keys', 'items') is False

# Generated at 2022-06-13 20:48:48.803435
# Unit test for function has_callables
def test_has_callables():
    """Test the callable of has_callables"""
    assert has_callables(dict(),'get','keys','items','values') == True



# Generated at 2022-06-13 20:48:51.935921
# Unit test for function has_callables
def test_has_callables():
    from collections import UserDict
    obj = UserDict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'items', 'values') is True



# Generated at 2022-06-13 20:49:02.848030
# Unit test for function has_any_callables
def test_has_any_callables():
    class foo(object):
        pass

    o = foo()
    o.get = lambda x: None
    o.get2 = lambda x: None
    o.get3 = lambda x: None
    o.get4 = lambda x: None
    assert has_any_callables(o, 'get', 'get2', 'get3', 'get4') is True
    assert has_any_callables(o, 'get', 'get2', 'get3', 'get4', 'bar') is True
    assert has_any_callables(o, 'bar', 'foo', 'bar2', 'get4') is False

    class bar(object):
        pass

    o = bar()
    assert has_any_callables(o, 'get', 'get2', 'get3', 'get4') is False
    assert has_any_

# Generated at 2022-06-13 20:49:27.551952
# Unit test for function has_callables
def test_has_callables():
    my_dict = {'foo': 42}
    assert has_callables(my_dict, 'get') == True
    assert has_callables(my_dict, 'get', 'pop') == True
    assert has_callables(my_dict, 'pop') == False
    assert has_callables(my_dict, 'pop', 'values') == False
    assert has_callables(my_dict, 'bar', 'foo') == False


# Generated at 2022-06-13 20:49:34.779738
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something') == True
    assert has_any_callables(dict(),'get','keys','items','values') == True
    assert has_any_callables(dict(),'get','keys','items','foo') == False


# Generated at 2022-06-13 20:49:43.682935
# Unit test for function has_callables
def test_has_callables():
    from collections import (
        deque,
        UserList,
    )
    from operator import (
        itemgetter,
        methodcaller,
        attrgetter,
    )
    from typing import (
        Any,
        Callable,
        CallableMeta,
    )

    assert has_callables(deque(range(10))) is False
    assert has_callables(UserList([1, 2, 3])) is False
    assert has_callables(methodcaller('upper')) is True
    assert has_callables(CallableMeta.__call__) is True
    assert has_callables(Callable[[Any, Any], int]) is True
    assert has_callables(itemgetter(1)) is True
    assert has_callables(attrgetter('upper')) is True
    assert has_

# Generated at 2022-06-13 20:49:52.174593
# Unit test for function has_any_callables
def test_has_any_callables():

    from flutils.objutils import has_any_callables

    assert has_any_callables(dict(),'get','keys','items','values','something')
    assert has_any_callables(dict(),'get','keys','items','values')
    assert has_any_callables(dict(),'get','keys')
    assert has_any_callables(dict(),'get')
    assert has_any_callables(True,'__bool__','__int__','__add__','something')


# Generated at 2022-06-13 20:49:57.413411
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False


# Unit tests for function has_attrs

# Generated at 2022-06-13 20:50:09.923497
# Unit test for function has_any_callables
def test_has_any_callables():
    print("> start of test_has_any_callables")
    print(">> start of test_has_any_callables: error handling")
    try:
        has_any_callables(object)
    except Exception as exc:
        assert isinstance(exc, TypeError)
        assert "obj" in str(exc)
    try:
        has_any_callables(dict())
    except Exception as exc:
        assert isinstance(exc, TypeError)
        assert "attrs" in str(exc)
    print(">> end of test_has_any_callables: error handling")
    print(">> start of test_has_any_callables: callables")
    obj = dict(a=1, b=2)
    attrs = ['get', 'keys', 'items', 'values', '__contains__']


# Generated at 2022-06-13 20:50:17.620115
# Unit test for function has_callables
def test_has_callables():
    """Unit test for function has_callables
    """
    obj = dict(a=1, b=2)
    assert has_callables(obj.keys(), '__iter__', '__next__')
    assert not has_callables(obj.keys(), 'keys')
    assert has_callables(obj, 'keys', 'items')
    assert has_callables(obj, 'items', 'keys')
    assert not has_callables(obj, 'foo', 'bar')

# Generated at 2022-06-13 20:50:23.866038
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something')
    assert not has_any_callables(dict(),'something','foo','bar','blah','fgdfg') 
    assert has_any_callables(dict(),'keys','items','values','som','ething')
    assert not has_any_callables(dict(),'something','fo','bar','blah','fgdfg')  


# Generated at 2022-06-13 20:50:27.406339
# Unit test for function has_callables
def test_has_callables():
    _obj = dict(a=1, b=2)
    _attrs = ('get', 'keys', 'items', 'values')
    _expected = True
    _actual = has_callables(_obj, *_attrs)
    assert _actual == _expected


# Generated at 2022-06-13 20:50:35.709484
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict, 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict, 'foo') is False
    assert has_any_callables(1, 'foo') is False
    assert has_any_callables(None, 'foo') is False


# Generated at 2022-06-13 20:51:14.413661
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
#

# Generated at 2022-06-13 20:51:18.848391
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'get','keys','foo','items','values') == True
    assert has_any_callables(dict(),'get','keys','items','values') == True
    assert has_any_callables(tuple(),'get','keys','foo','items','values') == False


# Generated at 2022-06-13 20:51:28.915103
# Unit test for function has_any_callables
def test_has_any_callables():
    from io import BytesIO
    from datetime import date
    from functools import partial, reduce
    from textwrap import dedent

    assert has_any_callables(list(), 'append', 'extend', 'something') is True
    assert has_any_callables(dict(), 'keys', 'values', 'something') is True
    assert has_any_callables(BytesIO(), 'tell', 'read', 'something') is True
    assert has_any_callables(reduce, '__call__', '__qualname__', 'something') is True
    assert has_any_callables(date.today, 'year', 'month', 'something') is True
    assert has_any_callables(partial, '__call__', '__qualname__', 'something') is True


# Generated at 2022-06-13 20:51:32.663467
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1, b=2)
    assert has_any_callables(d, 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:51:34.692700
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys','items','values') == True

# Generated at 2022-06-13 20:51:41.895016
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get') is True
    assert has_callables(dict(), 'something') is False
    assert has_callables(dict(), 'get', 'something') is False
    assert has_callables(dict(), 'get', 'keys') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_callables(list(), 'count', 'index', 'append') is True
    assert has_callables(list(), 'count', 'index', 'append', 'foo') is False
    assert has_callables(tuple(), 'count', 'index') is True

# Generated at 2022-06-13 20:51:54.511878
# Unit test for function has_callables
def test_has_callables():
    print('Testing function has_callables:', end='')
    assert has_callables(list(), 'append', 'pop', 'clear')
    assert has_callables(dict(), 'get', 'clear', 'update')
    assert has_callables('foo', 'join', 'split', 'upper')
    assert has_callables(bytes(), 'decode', 'replace', 'join')
    assert has_callables(set(), 'update', 'intersection', 'symmetric_difference')
    assert not has_callables(str(), 'lower', 'join', 'startswith', 'something')
    assert not has_callables(None, 'lower', 'join', 'startswith')
    assert not has_callables(dict, 'lower', 'join', 'startswith')
    print('passed')
    return


#

# Generated at 2022-06-13 20:52:00.125954
# Unit test for function has_any_callables
def test_has_any_callables():
  assert has_any_callables(dict(a=1, b=2), 'get', 'keys', 'items', 'values', 'foo') == True
  assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True
  assert has_any_callables(dict(a=1, b=2), 'has_any_callables', 'keys', 'items', 'values', 'foo') == False


# Generated at 2022-06-13 20:52:04.924278
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for the function: has_any_callables
    """
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:52:14.919779
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function ``has_any_callables``"""
    print('Testing has_any_callables')
    dct = dict(a=1, b=2, c=3)
    assert has_any_callables(dct, 'get', 'items', 'keys', 'values') is True
    assert has_any_callables(dct, 'get', 'items', 'bar', 'values') is True
    assert has_any_callables(dct, 'get', 'foo', 'bar', 'values') is False
