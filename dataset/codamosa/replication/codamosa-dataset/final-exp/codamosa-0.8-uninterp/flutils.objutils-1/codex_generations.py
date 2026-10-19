

# Generated at 2022-06-13 20:43:14.173534
# Unit test for function has_callables
def test_has_callables():
    from collections import UserDict
    from flutils.objutils import has_callables
    assert has_callables(dict(),'get','keys','items','values')
    assert has_callables(UserDict(),'get','keys','items','values')



# Generated at 2022-06-13 20:43:18.765348
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test for function has_any_callables"""
    obj = dict(a=1,b=2,c=3)
    assert has_any_callables(obj, 'get', 'keys', 'update')


# Generated at 2022-06-13 20:43:21.140353
# Unit test for function has_attrs
def test_has_attrs():
    from flutils.objutils import has_attrs
    assert has_attrs(dict(), 'get', 'keys', 'items', 'values')



# Generated at 2022-06-13 20:43:23.910050
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo', 'bar') is False
    assert has_any_callables(dict(), 'keys', 'items', 'values', 'foo', 'bar') is True

# Generated at 2022-06-13 20:43:27.034909
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_attrs(dict(),'get','keys','items','values')


# Generated at 2022-06-13 20:43:33.813101
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'foo', 'foo') is True


# Generated at 2022-06-13 20:43:37.291324
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:43:44.592806
# Unit test for function has_callables
def test_has_callables():
    # Test case 1: dictionary with keys, items, values and get
    obj = dict()
    assert has_callables(obj, "get", "keys", "items", "values") == True
    # Test case 2: dictionary with get but not keys, items and values
    obj = dict()
    assert has_callables(obj, "get", "foo", "bar", "baz") == True
    # Test case 3: dictionary with foo but no keys, items and values
    obj = dict()
    assert has_callables(obj, "foo") == False


# Generated at 2022-06-13 20:43:49.454114
# Unit test for function has_any_callables
def test_has_any_callables():
    class Foo:
        pass

    f = Foo()
    f.a = lambda: None
    f.b = lambda: None
    assert has_any_callables(f, 'a', 'b') == True



# Generated at 2022-06-13 20:44:01.185596
# Unit test for function has_any_callables
def test_has_any_callables():
    # test a dict
    my_dict = {'a': 1, 'b': 2}
    assert has_any_callables(my_dict, 'get', 'keys', 'items', 'values', 'foo')
    # test a list
    my_list = [1, 2, 3]
    assert has_any_callables(my_list, 'append', 'index', 'count', 'foo')
    # test a set
    my_set = {1, 2, 3}
    assert has_any_callables(my_set, 'add', 'discard', 'pop', 'foo')
    # test a string
    my_string = 'hello'
    assert not has_any_callables(my_string, 'append', 'index', 'count', 'foo')



# Generated at 2022-06-13 20:44:13.939608
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'get','keys','items','values') == True
    assert has_any_callables(dict(),'get','keys','items') == True
    assert has_any_callables(dict(),'get','keys') == True
    assert has_any_callables(dict(),'get') == True
    assert has_any_callables(dict(),'foo') == False
    assert has_any_callables(dict(),) == False


# Generated at 2022-06-13 20:44:23.807256
# Unit test for function has_callables
def test_has_callables():
    def tester(obj, *attrs):
        return has_callables(obj, *attrs)
    assert tester(dict(), 'get', 'keys', 'items', 'values') is True
    assert tester(dict(), 'get', 'keys', 'items') is False
    assert tester(dict(), 'get', 'keys', 'items', 'foo') is False
    assert tester(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    assert tester(dict(), 'get', 'keys', 'items', 'values', 'foo',
                      'bar', 'baz') is False
    assert tester(dict(), 'get', 'bar', 'baz') is False

# Generated at 2022-06-13 20:44:31.520187
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:44:36.853993
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test the has_any_callables function"""
    from collections import (
        defaultdict,
        ChainMap,
        UserString,
        OrderedDict,
        UserDict,
    )

    assert has_any_callables(defaultdict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(ChainMap(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(OrderedDict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(UserDict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(UserString('foo'), 'get', 'keys', 'items', 'values', 'foo')
    assert has_

# Generated at 2022-06-13 20:44:38.563821
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    assert has_callables(obj, "get", "keys", "items", "values") is True



# Generated at 2022-06-13 20:44:41.310269
# Unit test for function has_callables
def test_has_callables():
    test_list=('add','append','clear','copy','count','extend','index','insert','pop','remove','reverse','sort')
    print('has_callables(list(obj,list[attrs]):',has_callables(list(),*test_list))
    print('has_callables(dict,list[attrs]):',has_callables(dict(),*test_list))

# Generated at 2022-06-13 20:44:44.756650
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:44:51.508838
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test the `has_any_callables` function.

    """
    print('Testing has_any_callables')
    obj = dict()
    res = has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')
    assert res is True
    res = has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo', 'data')
    assert res is False



# Generated at 2022-06-13 20:44:52.491257
# Unit test for function has_callables
def test_has_callables():
    # TODO: Needs tests
    pass



# Generated at 2022-06-13 20:44:57.861853
# Unit test for function has_callables
def test_has_callables():
    """."""
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'items', 'values') is True
    assert has_callables(obj, 'get', 'items', 'values', 'foo') is False



# Generated at 2022-06-13 20:45:13.587360
# Unit test for function has_callables
def test_has_callables():
    print('-' * 70)
    print('Testing function has_callables...')
    print('-' * 70)
    obj = dict(a=1, b=2)
    print(f'has_callables(obj, "get", "keys", "items", "values"): {has_callables(obj, "get", "keys", "items", "values")}')
    print(f'has_callables(obj, "set", "keys", "items", "values"): {has_callables(obj, "set", "keys", "items", "values")}')
    print(f'has_callables(obj, "get", "get", "items", "values"): {has_callables(obj, "get", "get", "items", "values")}')

# Generated at 2022-06-13 20:45:19.526738
# Unit test for function has_any_callables
def test_has_any_callables():
    assert not has_any_callables(3, 'foo')
    assert not has_any_callables({}, 'foo')
    assert not has_any_callables(list, 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables({'a': 1}, 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables({'get': 1}, 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:45:23.944016
# Unit test for function has_callables
def test_has_callables():
    """Test the has_callables function."""
    import re

    # noinspection PyUnresolvedReferences
    assert has_callables(re.match, 'group')



# Generated at 2022-06-13 20:45:32.553014
# Unit test for function has_any_callables
def test_has_any_callables():
    # Test with class Custom:
    class TestCustom(object):
        def __init__(self):
            self.name = 'test_custom'
        def foo(self): 
            pass
        def bar(self): 
            pass
           
    test_custom = TestCustom()
    assert (has_any_callables(test_custom, 'foo', 'bar') is True)
    assert (has_any_callables(test_custom, 'foo', 'bar', 'baz') is True)
    assert (has_any_callables(test_custom) is False)
    
    # Test with object dict:
    assert (has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True)

# Generated at 2022-06-13 20:45:45.359469
# Unit test for function has_callables
def test_has_callables():
    from dictknife import loading
    from dictknife import Accessor
    from dictknife.langhelpers import make_dict
    data = loading.loads(
        """[
            {"name": "foo"},
            {"name": "bar"},
            {"name": "baz"}
        ]"""
    )
    d = make_dict(Accessor(["name"]), data)
    assert has_callables(d, "keys")
    assert has_callables(d, "keys", "values")
    assert has_callables(d, "keys", "values", "items")
    assert has_callables(d, "get")
    assert has_callables(d, "keys", "values", "items", "get")
    assert not has_callables(d, "keys", "values", "items", "foo")

# Generated at 2022-06-13 20:45:48.602368
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') == True


# Generated at 2022-06-13 20:45:58.776628
# Unit test for function has_attrs
def test_has_attrs():
    from collections.abc import Iterable
    assert has_attrs(dict(),'get','keys','items','values')
    assert has_attrs('hello','isupper','islower','split')
    assert not has_attrs([1, 2, 3, 4], 'foo', 'bar', 'foobar')
    assert not has_attrs(dict(), 'foo', 'bar', 'foobar')
    assert not has_attrs('hello', 'foobar')
    assert has_attrs([1, 2, 3, 4], '__len__', '__iter__')
    assert has_attrs([1, 2, 3, 4, 5, 6], '__len__', '__iter__')
    assert has_attrs(Iterable, '__len__', '__iter__')



# Generated at 2022-06-13 20:46:02.796807
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values','some') is False
    assert has_callables(dict(),'get','keys','items','values','get') is True

# Generated at 2022-06-13 20:46:07.737432
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something')
    assert has_any_callables(dict(a=1, b=2),'get','keys','items','values')


# Generated at 2022-06-13 20:46:15.092486
# Unit test for function has_callables
def test_has_callables():
    from flutils.objutils import has_callables

    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'foo') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'something') is False



# Generated at 2022-06-13 20:46:25.485937
# Unit test for function has_callables
def test_has_callables():
    pass


# Generated at 2022-06-13 20:46:33.656680
# Unit test for function has_any_callables
def test_has_any_callables():
    # Make the dict
    obj = dict(a=1, b=2)
    # Make a function to check
    def foo(x):
        return not x
    # Add the function
    obj['foo'] = foo

    # Check the function
    assert has_any_callables(obj, 'foo', 'bar') is True
    assert has_any_callables(obj, 'bar', 'baz') is False


# Generated at 2022-06-13 20:46:37.969951
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


# Generated at 2022-06-13 20:46:45.462764
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo') is False
    assert has_any_callables({'foo': 'foo'}, 'foo') is False



# Generated at 2022-06-13 20:46:58.121150
# Unit test for function has_callables
def test_has_callables():
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserString,
        defaultdict,
    )
    from decimal import Decimal
    is_bool = has_callables(True, 'bit_length')
    is_bytes = has_callables(b'hello', 'split', 'upper')
    is_chainmap = has_callables(ChainMap(), 'keys', 'values')
    is_counter = has_callables(Counter(), 'most_common', 'get')
    is_defaultdict = has_callables(defaultdict(), 'get')
    is_dict = has_callables(dict(), 'keys', 'values', 'update')
    is_float = has_callables(3.14, 'hex')

# Generated at 2022-06-13 20:47:04.546048
# Unit test for function has_any_callables
def test_has_any_callables():
    class A():
        def b():
            pass

    assert has_any_callables(A(),"b")
    assert has_any_callables(A(),"b","c")
    assert has_any_callables(A(),"c","b")
    assert has_any_callables(A(),"c","b","d")
    assert not has_any_callables(A(),"c","d")
    assert not has_any_callables(A(),"c")


# Generated at 2022-06-13 20:47:07.112504
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(dict(),'get','keys','items','values','anything'))


# Generated at 2022-06-13 20:47:15.857609
# Unit test for function has_callables
def test_has_callables():
    from collections import (
        Counter,
    )
    from operator import (
        add,
    )
    from functools import (
        reduce,
    )
    obj = {
        'something': True,
        'add': add,
        'reduce': reduce,
        'Counter': Counter,
    }
    assert has_attrs(obj, 'something', 'add', 'reduce', 'Counter') is True
    assert has_attrs(obj, 'get', 'keys', 'items', 'values') is False
    assert has_attrs(obj, 'reduce', 'Counter', 'something') is True

    assert has_callables(obj, 'something', 'add', 'reduce', 'Counter') is False
    assert has_callables(obj, 'something', 'add', 'reduce') is True
    assert has

# Generated at 2022-06-13 20:47:22.161673
# Unit test for function has_any_callables
def test_has_any_callables():
    # Check builtins
    assert has_any_callables(list(), '__doc__')
    assert has_any_callables(list(), 'append')

    # Check callable and non-callable attributes
    assert has_any_callables(set(), '__doc__')
    assert has_any_callables(set(), 'add')

    # Check non-callable attributes
    assert has_any_callables(dict(), '__doc__')
    assert not has_any_callables(dict(), 'foo')


# Generated at 2022-06-13 20:47:24.392589
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True

    assert has_any_callables(dict(),'foo') is False



# Generated at 2022-06-13 20:47:32.465611
# Unit test for function has_callables
def test_has_callables():
    assert True == has_callables(dict(),'get','keys','items','values')


# Generated at 2022-06-13 20:47:40.975471
# Unit test for function has_callables
def test_has_callables():
    """
    :rtype:
        :obj:`bool`

        * :obj:`True` if all the given ``*attrs`` exist on the given ``obj``
          and all are callable;
        * :obj:`False` otherwise.

    Example:
        >>> from flutils.objutils import has_callables
        >>> has_callables(dict(),'get','keys','items','values')
        True
    """
    x = {
        'a': 1,
        'b': 2,
        'c': 3
    }
    assert has_callables(x, 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:47:44.576764
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True
    assert has_callables(dict(),'get', 'items', 'values') is False
    assert has_callables(dict(),'get','keys','items','foo') is False


# Generated at 2022-06-13 20:47:53.138487
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values','something') is False
    assert has_callables(dict(),'get','keys','items','values') is True
    #assert has_callables(dict(),'get','keys','items','values','foo') is False
    assert has_callables(Dummy(),'instfunc','clsfunc') is True
    assert has_callables(Dummy(),'instfunc','clsfunc','something') is False



# Generated at 2022-06-13 20:47:53.686078
# Unit test for function has_callables
def test_has_callables():
    pass

# Generated at 2022-06-13 20:47:58.620395
# Unit test for function has_callables
def test_has_callables():
    from collections import ChainMap
    assert has_callables(str, 'upper') is True
    assert not has_callables(str, 'foo') is True
    assert has_callables(ChainMap, 'maps') is True
    assert has_callables(ChainMap, 'get') is True
    assert not has_callables(ChainMap, 'foo') is True


# Generated at 2022-06-13 20:48:02.754198
# Unit test for function has_callables
def test_has_callables():
    """Ensure that has_callables() works correctly
    """
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:48:06.096612
# Unit test for function has_callables
def test_has_callables():
    '''
    Function to test has_callables
    '''
    assert has_callables(dict(),'get','keys','items','values')==True


# Generated at 2022-06-13 20:48:19.560681
# Unit test for function has_callables
def test_has_callables():
    class _TMP_CLASS:
        _TMP_OBJ = dict(a=1, b=2)

    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'qqq', 'keys', 'items', 'values') is False
    assert has_callables(_TMP_CLASS._TMP_OBJ, 'get', 'keys', 'items', 'values') is True
    assert has_callables([1, 2, 3], '__iter__', '__len__', '__add__') is True
    assert has_callables([1, 2, 3], '__qqq__', '__len__', '__add__') is False
    assert has_callables('hello', '__iter__', '__len__', '__add__') is True

# Generated at 2022-06-13 20:48:33.017860
# Unit test for function has_callables
def test_has_callables():
    """Test for function objectutils.has_callables."""
    from flutils.objutils import (
        has_callables
    )
    import collections

    obj = collections.defaultdict(list)
    assert has_callables(
        obj,
        'append',
        'clear',
        'copy',
        'default_factory',
        'fromkeys',
        'get',
        'items',
        'keys',
        'pop',
        'popitem',
        'setdefault',
        'update',
        'values'
    ) is True

# Generated at 2022-06-13 20:48:47.134468
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:48:53.455427
# Unit test for function has_callables
def test_has_callables():
    d = dict(a=1, b=2)
    assert (has_callables(d, 'items', 'keys') is True)
    assert (has_callables(d, 'foo') is False)
    assert (has_callables(d, 'foo', 'bar') is False)
    assert (has_callables(d, 'keys', 'bar') is False)
    assert (has_callables(d, 'keys', 'items', 'bar') is False)
    assert (has_callables(d) is False)


# Generated at 2022-06-13 20:48:55.250560
# Unit test for function has_callables
def test_has_callables():
    d=dict()
    assert has_callables(d,'get','keys','items','values') == True

# Generated at 2022-06-13 20:49:03.677826
# Unit test for function has_callables
def test_has_callables():
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserString
    )
    from collections.abc import Mapping
    from decimal import Decimal
    from flutils.objutils import has_callables
    import types
    import pickle
    import marshal
    import functools
    import copy_reg
    import os
    import pprint
    import sys
    import random
    import math
    import reprlib
    import doctest
    import zipimport
    import struct
    import fractions
    import abc
    import re
    import io
    import itertools
    import collections
    import contextlib
    import operator
    import bisect
    import heapq
    import pdb
    import warnings
    import token
    import tokenize
    import keyword
   

# Generated at 2022-06-13 20:49:13.456610
# Unit test for function has_callables
def test_has_callables():
    import sys
    import time
    import unittest

    from flutils.objutils import (
        has_callables,
        has_any_callables
    )

    from flutils.getters import (
        get_all_children
    )

    import types


    class Test(unittest.TestCase):
        def setUp(self):
            self.mod = sys.modules['flutils.objutils']
            self.objs = get_all_children(self.mod, types.ModuleType)


        def test_has_callables(self):
            funcs = has_callables(self.mod, *self.objs)
            self.assertIsInstance(funcs, list)
            self.assertEqual(len(funcs), 5)



# Generated at 2022-06-13 20:49:17.648416
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_callables(dict(), 'keys', 'items', 'values', 'foo') is False



# Generated at 2022-06-13 20:49:19.899572
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True

# Generated at 2022-06-13 20:49:24.625431
# Unit test for function has_callables
def test_has_callables():
    class Foo(object):
        def __call__(self):
            return 0


    assert has_callables(Foo(), '__call__') is True
    assert has_callables(Foo(), '__call__', '__class__', '__delattr__') is False
    assert has_callables(Foo(), '__call__', '__class__', '__init__') is False



# Generated at 2022-06-13 20:49:26.753555
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:49:35.469165
# Unit test for function has_callables
def test_has_callables():
    # flag = 0
    a = dict(a=1, b=2)
    if has_callables(a, 'values'):
        # flag = 1
        print("has_callables(dict(),'get','keys','items','values') return True")
    else:
        print("has_callables(dict(),'get','keys','items','values') return False")

