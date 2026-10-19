

# Generated at 2022-06-13 20:43:09.474349
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import deque
    d = deque()
    has_any_callables(d, 'append', 'pop')
    assert has_any_callables(d, 'append', 'pop') == True
    

# Generated at 2022-06-13 20:43:22.723541
# Unit test for function has_any_callables
def test_has_any_callables():
    import collections
    from flutils.objutils import has_any_callables
    test_tuple = ("A","B","C")
    test_set = set(["A","B","C"])
    test_dict = {
        "A": {1:1},
        "B": {2:2},
        "C": {3:3},
    }
    test_list = [
        {
            "A": {1:1},
            "B": {2:2},
            "C": {3:3},
        },
        {
            "A": {1:1},
            "B": {2:2},
            "C": {3:3},
        }
    ]
    assert has_any_callables(test_tuple, "__iter__", "__next__") == True
   

# Generated at 2022-06-13 20:43:26.051417
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(),'get','keys','items','values','something') == True


# Generated at 2022-06-13 20:43:34.225247
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables"""
    import sys
    import os
    import re
    import collections
    import unittest
    from flutils.objutils import has_any_callables

    class TestObjutils(unittest.TestCase):
        """Test object utility functions"""

        module_name = "flutils.objutils"

        # noinspection PyUnusedLocal
        def test_has_any_callables(self):
            """Test function has_any_callables"""
            self.assertTrue(has_any_callables(list(), "append", "pop"))
            self.assertTrue(has_any_callables(dict(), "keys", "pop"))
            self.assertTrue(has_any_callables(collections.OrderedDict(), "popitem"))

# Generated at 2022-06-13 20:43:42.992664
# Unit test for function has_callables
def test_has_callables():
    """Call function has_callables.
    """
    assert has_callables(dict, 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict, 'get', 'keys', 'items', 'va') is False
    assert has_callables(dict, 'get', 'keys', 'items', 'va', 'pop') is False
    assert has_callables(dict.__class__, 'get', 'keys', 'items', 'values') is True



# Generated at 2022-06-13 20:43:48.791031
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo','something') == True
    assert has_any_callables(dict(),'get','keys','items','values', 'foo') == True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') == True
    

# Generated at 2022-06-13 20:43:52.236638
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:43:53.435577
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')

# Generated at 2022-06-13 20:43:54.457614
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')



# Generated at 2022-06-13 20:43:57.977596
# Unit test for function has_callables
def test_has_callables():
    """
    Test function has_callables
    """
    class Test:
        """
        Class used to test has_callables
        """
        def method(self):
            """
            Method to test has_callables
            """
            pass

    test = Test()
    assert has_callables(test, 'method') == True

# Generated at 2022-06-13 20:44:12.593890
# Unit test for function has_any_attrs
def test_has_any_attrs():
    # obj is a dict()
    obj = dict(a=1, b=2)
    # obj has all of the following attrs
    attrs = ['items', 'keys', 'values', 'get']
    assert has_any_attrs(obj, *attrs) is True
    # add another attr that does not exist in obj
    attrs.append('foo')
    assert has_any_attrs(obj, *attrs) is True
    # obj is a str
    obj = 'hello'
    # obj has all of the following attrs
    attrs = ['find', 'strip', 'title']
    assert has_any_attrs(obj, *attrs) is True
    # add another attr that does not exist in obj
    attrs.append('foo')

# Generated at 2022-06-13 20:44:15.628350
# Unit test for function has_attrs
def test_has_attrs():
    assert has_attrs(dict(),'get','keys','items','values') is True


# Generated at 2022-06-13 20:44:19.539562
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(),'get','keys','items','values','something') is True
    assert has_any_attrs(dict(),'foo','bar') is False


# Generated at 2022-06-13 20:44:30.244425
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), '__len__', '__iter__', '__setitem__', '__str__', '__delitem__') is True
    assert has_any_callables(dict(), '__doc__', '__reversed__', '__repr__', 'pop', 'popitem') is True


# Generated at 2022-06-13 20:44:33.270169
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(
        dict(),
        'get',
        'keys',
        'items',
        'values',
        'foo'
    ) is True



# Generated at 2022-06-13 20:44:42.210151
# Unit test for function has_any_callables
def test_has_any_callables():
    class Foo:
        foo = ''

        def bar(self):
            """This is the docstring for bar."""

    obj = Foo()
    attrs = ('foo', 'bar', 'baz')
    assert has_any_callables(obj, *attrs) is True
    attrs = ('foo', 'baz')
    assert has_any_callables(obj, *attrs) is False
    attrs = ()
    assert has_any_callables(obj, *attrs) is False


# Generated at 2022-06-13 20:44:45.360240
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:44:48.225384
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True



# Generated at 2022-06-13 20:44:54.105143
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables([], 'foo', 'bar') is False
    assert has_any_callables([], 'foo', '__len__') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_attrs(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False

# Generated at 2022-06-13 20:44:58.101541
# Unit test for function has_attrs
def test_has_attrs():
    assert has_attrs(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_attrs(dict(), 'foo', 'bar', 'baz') is False



# Generated at 2022-06-13 20:45:13.754167
# Unit test for function has_any_callables
def test_has_any_callables():

    class Foo():

        def __init__(self):
            self.a = True
            self.b = False
            self.c = None
            self.d = 'foo'
            self.e = dict()
            self.f = lambda: None
            self.g = None
            self.h = None
            self.i = None
            self.j = None
            self.k = dict()

        def __call__(self, x):
            return x

    foo = Foo()
    #  exists and callable
    assert has_any_callables(foo, '__init__')
    assert has_any_callables(foo, 'a')
    assert has_any_callables(foo, 'b')
    assert has_any_callables(foo, 'c')

# Generated at 2022-06-13 20:45:16.132416
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'bar') is True


# Generated at 2022-06-13 20:45:23.254180
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'foo')
    assert has_any_callables(dict(), 'foo', 'bar') is False
    assert has_any_callables(dict(), 'get', 'keys', 'copy', '__copy__')


# Generated at 2022-06-13 20:45:32.153613
# Unit test for function has_callables
def test_has_callables():
    '''
    Unit test for the function has_callables
    '''
    class TestClass:
        '''
        Test class for testing the function has_callables
        '''
        def function1(self, arg1: str):
            '''
            Test function for testing the function has_callables
            '''
            return arg1

        def function2(self, arg1: str):
            '''
            Test function for testing the function has_callables
            '''
            return arg1

        def function3(self, arg1: str):
            '''
            Test function for testing the function has_callables
            '''
            return arg1

    assert has_callables(TestClass(), 'function1', 'function2', 'function3')

# Generated at 2022-06-13 20:45:38.186300
# Unit test for function has_any_callables
def test_has_any_callables():
    # Make sure the function returns the correct type
    return_type_test = has_any_callables(dict(),'get','keys','items','values','foo')
    assert isinstance(return_type_test, bool) == True
    # Make sure the function returns the correct value
    return_test = has_any_callables(dict(),'get','keys','items','values','foo')
    assert return_test == True

# Generated at 2022-06-13 20:45:43.044360
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') == True
    assert has_callables(dict(),'get','keys','items','values','foo') == False
    assert has_callables(dict(),'get','keys','items') == False
    assert has_callables({}, 'get', 'keys', 'items', 'values') == True
    assert has_callables({}, 'get', 'keys', 'items', 'values', 'foo') == False
    assert has_callables({}, 'get', 'keys', 'items') == False


# Generated at 2022-06-13 20:45:56.907081
# Unit test for function has_any_callables
def test_has_any_callables():
    class test_obj():
        def __init__(self):
            self.abc = 1 
            self.defg = "1"
            self.hijk = lambda: 1

    print(has_any_callables(test_obj(), "abc", "defg", "hijk", "lmno"))
    print(has_callables(test_obj(), "abc", "defg", "hijk", "lmno"))
    print(has_any_attrs(test_obj(), "abc", "defg", "hijk", "lmno"))
    print(has_attrs(test_obj(), "abc", "defg", "hijk", "lmno"))


# Generated at 2022-06-13 20:46:08.607145
# Unit test for function has_any_callables
def test_has_any_callables():
    assert callable(has_any_callables)
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(),'items','values','foo')
    assert has_any_callables(dict(),'foo')
    assert has_any_callables(dict(),'get','keys','items')
    assert has_any_callables(dict(),'get','keys')
    assert not has_any_callables(dict(),'bar')
    assert has_any_callables(dict())
    assert not has_any_callables(dict(),'bar','baz')
    assert not has_any_callables(dict(),'bar','get')
    assert has_any_callables(dict(),'keys','get')

# Generated at 2022-06-13 20:46:12.281071
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(dict(),'get','keys','items','values','foo') == True)


# Generated at 2022-06-13 20:46:14.865631
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')

# Generated at 2022-06-13 20:46:26.394344
# Unit test for function has_callables
def test_has_callables():
    # Create a dummy class and set up an instance
    class Foo:
        def bar(self):
            print("Hello")
    
    # Create the instance and check that it has the attribute
    foo = Foo()
    assert has_callables(foo, "bar") is True


# Generated at 2022-06-13 20:46:41.309854
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo', 'bar', 'baz') is False
    assert has_any_callables(dict(), 'foo') is False
    assert has_any_callables(set(), 'add', 'clear', 'difference') is True
    assert has_any_callables(set(), 'foo', 'bar', 'baz') is False
    assert has_any_callables(frozenset(), 'add', 'clear', 'difference') is False
    assert has_any_callables(frozenset(), 'foo', 'bar', 'baz') is False
    assert has_any_callables(tuple(), 'add', 'clear', 'difference') is False

# Generated at 2022-06-13 20:46:49.623795
# Unit test for function has_callables
def test_has_callables():
    from collections import UserList
    from collections.abc import ValuesView, KeysView, Iterator

    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'items', 'values') is True
    assert has_callables(obj, 'get', 'keys', 'items', 'foo') is False

    assert has_callables(obj.keys(), '__iter__', '__contains__') is True
    assert has_callables(obj.keys(), '__iter__', '__contains__', 'foo') is False

    assert has_callables(obj.items(), '__iter__', '__contains__') is True

# Generated at 2022-06-13 20:47:00.585562
# Unit test for function has_callables
def test_has_callables():
    class TestClass(object):
        def get(self):
            pass
        def items(self):
            pass
        def keys(self):
            pass
        def values(self):
            pass
    test_obj = TestClass()
    assert has_callables(test_obj, 'items', 'keys', 'values') == True
    assert has_callables(test_obj, 'get', 'keys', 'values') == True
    assert has_callables(test_obj, 'get', 'items', 'values') == True
    assert has_callables(test_obj, 'get', 'items', 'keys') == True
    assert has_callables(test_obj, 'get', 'keys') == False
    assert has_callables(test_obj, 'get', 'values') == False

# Generated at 2022-06-13 20:47:04.351818
# Unit test for function has_any_callables
def test_has_any_callables():
    # noinspection PyUnresolvedReferences
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    # noinspection PyUnresolvedReferences
    assert has_any_callables(dict(),'has_key','contains') is False



# Generated at 2022-06-13 20:47:14.674003
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(str(), 'join') == True
    assert has_any_callables(str(), 'join') == True
    assert has_callables(str(), 'join', 'lower') == True
    assert has_any_callables(str(), 'join', 'lower') == True
    assert has_callables(str(), 'join', 'lower', 'foo') == False
    assert has_any_callables(str(), 'join', 'lower', 'foo') == True
    assert has_callables(str(), 'foo') == False
    assert has_any_callables(str(), 'foo') == False
    assert has_callables(dict(), 'get') == True
    assert has_any_callables(dict(), 'get') == True
    assert has_callables(dict(), 'get', 'keys') == True
    assert has

# Generated at 2022-06-13 20:47:18.039209
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(a=1),'get','keys','items','values','foo')


# Generated at 2022-06-13 20:47:23.113278
# Unit test for function has_callables
def test_has_callables():
    obj = {"foo": "bar"}
    assert has_callables(obj, "items", "keys", "values") == True


# Generated at 2022-06-13 20:47:25.063397
# Unit test for function has_any_callables
def test_has_any_callables():
    """

    """
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')


# Generated at 2022-06-13 20:47:29.904235
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    assert has_callables(obj,'get','keys','items') is True
    assert has_callables(obj,'get','keys','items','foo') is False

# Generated at 2022-06-13 20:47:39.908994
# Unit test for function has_any_callables
def test_has_any_callables():
    from unittest import TestCase

    class Test(TestCase):
        obj = dict(a=1, b=2, c=3)

        def test_not_callable(self):
            self.assertFalse(has_any_callables(self.obj, 'items', 'clear'))

        def test_callable(self):
            self.assertTrue(has_any_callables(self.obj, 'items', 'clear'))
    return Test()


# Generated at 2022-06-13 20:47:44.112888
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo') is False



# Generated at 2022-06-13 20:47:54.084367
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables([], 'foo') == False
    assert has_any_callables([], 'foo', 'extend') == True
    assert has_any_callables(dict(), 'get') == True
    assert has_any_callables(dict(), 'get', 'foo') == True
    assert has_any_callables(set(), 'intersection') == True
    assert has_any_callables(set(), 'foo', 'intersection') == True
    assert has_any_callables(frozenset(), 'foo') == False



# Generated at 2022-06-13 20:47:57.319664
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict, 'get', 'keys', 'items', 'values') is False



# Generated at 2022-06-13 20:48:09.431597
# Unit test for function has_any_callables
def test_has_any_callables():
    def foo():
        pass

    def bar():
        pass

    def baz():
        pass

    d = {
        'foo': foo,
        'bar': bar,
        'baz': baz
    }

    assert has_any_callables(d, 'foo', 'bar', 'baz') is True

    del d['bar']

    assert has_any_callables(d, 'foo', 'bar', 'baz') is True

    del d['foo']

    assert has_any_callables(d, 'foo', 'bar', 'baz') is True

    del d['baz']

    assert has_any_callables(d, 'foo', 'bar', 'baz') is False


# Generated at 2022-06-13 20:48:21.051261
# Unit test for function has_callables
def test_has_callables():
    """Test the function has_callables.

    Example:
        >>> from flutils.objutils import has_callables
        >>> obj = dict()
        >>> has_callables(obj, "items")
        True
        >>> has_callables(obj, "get", "str")
        False
    """
    class TestObj:
        def __init__(self):
            self.callme = lambda: None

    obj = TestObj()
    assert has_callables(obj, "callme") is True
    assert has_callables(obj, "callme", "callme") is True
    assert has_callables(obj, "callme", "callme2") is False
    assert has_callables(obj, "callme2") is False



# Generated at 2022-06-13 20:48:26.072567
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(),'get','keys','items','values','__class__')



# Generated at 2022-06-13 20:48:30.585882
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()

    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(obj, 'something', 'else', 'entirely') is False



# Generated at 2022-06-13 20:48:35.193553
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables."""
    from collections import UserList

    assert has_any_callables({}, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(UserList(), 'get', 'keys', 'items', 'values') is False


# Generated at 2022-06-13 20:48:39.690557
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables({}, 'keys', 'items')
    assert not has_any_callables({}, 'key', 'item')


# Generated at 2022-06-13 20:48:49.321038
# Unit test for function has_callables
def test_has_callables():
    """Test for function has_callables.
    """
    assert has_callables({}, 'items', '__contains__') is True
    assert has_callables({}, 'foo', 'bar') is False


# Generated at 2022-06-13 20:48:52.444591
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables."""
    import sys

    assert has_any_callables(sys, 'getrecursionlimit', 'path', 'exc_info') is True



# Generated at 2022-06-13 20:49:00.775924
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables.

    This function tests the function has_any_callables.
    """
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_any_callables(dict(), 'foo', 'bar')
    assert has_any_callables(dict(), 'foo', 'items')
    assert has_any_callables(dict(), 'foo', 'bar', 'items')
    assert has_any_callables(dict(), 'items', 'bar', 'foo')


# Generated at 2022-06-13 20:49:12.086042
# Unit test for function has_callables
def test_has_callables():
    '''
    Unit test for function has_callables
    '''

    from flutils.objutils import has_callables

    d_callables = dict(
        keys=dict.keys,
        items=dict.items,
        values=dict.values,
        update=dict.update
        )
    # Check the has_callables function
    assert has_callables(d_callables, 'keys') is True
    assert has_callables(d_callables, 'keys', 'values') is True
    assert has_callables(d_callables, 'keys', 'values', 'items') is True
    assert has_callables(d_callables, 'items', 'update') is True
    assert has_callables(d_callables, 'keys', 'update') is True

# Generated at 2022-06-13 20:49:16.038638
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert not has_any_callables(dict(),'foo')
    assert has_any_callables(dict(),'foo', 'values')
    assert not has_any_callables(dict(),'foo1')


# Generated at 2022-06-13 20:49:19.827784
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'items', 'values') is True
    assert has_callables(obj, 'get', 'keys', 'items', 'values', 'something') is False
    assert has_callables(obj, 'get', 'keys', 'items') is False


# Generated at 2022-06-13 20:49:28.987804
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables([], '__getitem__', '__iter__')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables({'a': 1, 'b': 2}, 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(dict, 'keys')
    assert not has_any_callables('foo', 'keys')
    assert not has_any_callables(['foo', 'bar'], 'keys')
    assert not has_any_callables(1, 'keys')
    assert not has_any_callables(False, 'keys')


# Generated at 2022-06-13 20:49:38.352506
# Unit test for function has_any_callables
def test_has_any_callables():
    if not has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo'):
        assert False
    if not has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo'):
        assert False
    if not has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo'):
        assert False
    if not has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo'):
        assert False
    assert True


# Generated at 2022-06-13 20:49:41.248052
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:49:49.756417
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    assert has_any_callables(dict(),'get','keys','items','values') is True
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'foo') is False
    assert has_any_callables('foo','foo') is True

# Generated at 2022-06-13 20:50:08.015842
# Unit test for function has_callables
def test_has_callables():
    from collections import OrderedDict
    from collections.abc import Mapping
    from flutils.objutils import has_callables
    obj = OrderedDict(a=1, b=2, c=3)
    assert has_callables(obj, 'keys', 'items', 'values') is True
    assert has_callables(obj, 'keys', 'items') is True
    assert has_callables(obj, 'keys') is True
    assert has_callables(obj) is False
    assert has_callables(Mapping) is False
    assert has_callables(Mapping, 'keys') is False
    assert has_callables(Mapping, 'a') is False
    assert has_callables(Mapping, 'keys', 'a') is False



# Generated at 2022-06-13 20:50:19.379259
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something') \
        is True
    from collections import ChainMap
    assert has_any_callables(ChainMap(),'get','keys','items','values','something') \
        is True
    assert has_any_callables(dict(a=1,b=2),'get','keys','items','values','something') \
        is True
    assert has_any_callables(dict(a=1,b=2),'get','keys','items','values','something',
                             'foo') is False
    assert has_any_callables(dict(a=1,b=2),'get','keys','items','values',
                             'something','update') is True

# Generated at 2022-06-13 20:50:22.989278
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'foo') == True
    assert has_any_callables(obj, 'foo') == False


# Generated at 2022-06-13 20:50:31.253882
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo', 'no_such_attr') is True
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'no_such_attr') is True
    assert has_any_callables(obj, 'get', 'foo', 'items', 'values', 'no_such_attr') is True
    assert has_any_callables(obj, 'foo') is False
    assert has_any_callables(obj, 'get', 'foo') is False

# Generated at 2022-06-13 20:50:33.911550
# Unit test for function has_any_callables
def test_has_any_callables():
    obj1 = dict(a=1, b=2)
    assert has_any_callables(obj1, 'clear', 'update') is True


# Generated at 2022-06-13 20:50:35.835330
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(bool(),'__eq__', 'foo', 'thing')


# Generated at 2022-06-13 20:50:47.136891
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'values', 'items') == True
    assert has_callables(dict(), 'get', 'foo', 'bar', 'baz') == False
    assert has_callables(UserList(), 'append', 'clear', 'copy', 'count') == True
    assert has_callables(UserList(), 'append', 'clear', 'copy', 'not_a_method') == False
    assert has_callables(list(), 'append', 'clear', 'copy', 'count') == True
    assert has_callables(list(), 'append', 'clear', 'copy', 'not_a_method') == False


# Generated at 2022-06-13 20:51:01.120363
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables({'a': 1, 'b': 2}, 'get', 'keys', 'items',
                             'values', 'foo') is True
    assert has_any_callables({'a': 1, 'b': 2}, 'get', 'keys', 'items',
                             'bar') is False
    assert has_any_callables(dict(a=1, b=2), 'get', 'keys', 'items',
                             'bar') is False
    assert has_any_callables({}, 'get', 'keys', 'items', 'something') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items',
                             'something') is True
    assert has_any_callables({'a': 1, 'b': 2}, 'get', 'keys',
                             'something')

# Generated at 2022-06-13 20:51:06.622803
# Unit test for function has_any_callables
def test_has_any_callables():
    list = [1, 2, 3, 4, 5]
    l = has_any_callables(list, 'append', 'count', 'index', 'foo')
    assert l is True
    d = dict()
    d = has_any_callables(d, ['get', 'keys', 'foo'])
    assert d is True
    st = 'abc'
    st = has_any_callables(st, ['count', 'find'])
    assert st is True


# Generated at 2022-06-13 20:51:11.964731
# Unit test for function has_any_callables
def test_has_any_callables():
    '''
    Unit test for function has_any_callables
    '''
    assert True == has_any_callables(dict(),'get','items','keys','values')
    assert True == has_any_callables({'a':1,'b':2},'get','items','keys','values')
    assert False == has_any_callables(dict(),'attr1','attr2','attr3')
    assert False == has_any_callables({'a':1,'b':2},'attr1','attr2','attr3')


# Generated at 2022-06-13 20:51:28.479910
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test for function ``has_any_callables``."""
    from unittest.mock import Mock

    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    mock_obj = Mock()
    mock_obj.get = lambda *args, **kwargs: None
    assert has_any_callables(mock_obj, 'get', 'keys', 'items', 'values')
    assert not has_any_callables(mock_obj, 'foo', 'bar', 'baz', 'quux')

# Generated at 2022-06-13 20:51:33.167979
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') == True
    assert has_callables(dict(), 'get', 'keys', 'items', 'something') == False
    assert has_callables(dict(), 'get', 'keys', 'items', 'something') == False
    assert has_callables(dict(), 'get', 'keys', 'values', 'something') == False
    assert has_callables(dict(), 'keys', 'items', 'values', 'something') == True


# Generated at 2022-06-13 20:51:37.945144
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') == True
    assert has_callables(dict(),'get','keys','items','foo') == False
    assert has_callables(dict(),'get','keys','foo','bar') == False

# Generated at 2022-06-13 20:51:39.654120
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')

# Generated at 2022-06-13 20:51:45.777140
# Unit test for function has_callables
def test_has_callables():
    from collections import OrderedDict
    obj = OrderedDict(a=1, b=2)
    assert has_callables(obj, 'keys', 'items', 'values', 'update') is not False


# Generated at 2022-06-13 20:51:49.754231
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values','foo') == False
    assert has_callables(dict(),'get','keys','items','values') == True


# Generated at 2022-06-13 20:51:56.371048
# Unit test for function has_any_callables
def test_has_any_callables():
    print('Running function test_has_any_callables')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo1') is False


# Generated at 2022-06-13 20:52:05.206182
# Unit test for function has_callables
def test_has_callables():
    import warnings
    warnings.filterwarnings("ignore")

    obj = dict(a=1, b=2)
    assert has_callables(obj, 'keys', 'items')

    # make sure the order of attrs doesn't matter
    assert has_callables(obj, 'items', 'keys')

    # make sure the attr exists and is callable
    assert has_callables(obj, 'keys', 'items', 'get')

    # make sure it fails if attr doesn't exist
    assert not has_callables(obj, 'keys', 'items', 'foo')

    # make sure it fails if attr exists but isn't a method
    assert not has_callables(obj, 'keys', 'items', 'a')

    # make sure it fails if attr exists but isn't a method

# Generated at 2022-06-13 20:52:13.035555
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_any_callables(dict(), 'get', 'keys', 'items', 'foo')
    assert not has_any_callables(dict(), 'foo')



# Generated at 2022-06-13 20:52:17.078818
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_any_callables(dict(), 'foo', 'bar') is False

