

# Generated at 2022-06-13 20:43:10.442251
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')


# Generated at 2022-06-13 20:43:16.634371
# Unit test for function has_any_callables
def test_has_any_callables():
    #doctest: +ELLIPSIS
    """

    >>> from flutils.objutils import has_any_callables
    >>> has_any_callables(dict(), "get", "keys", "items", "values")
    True

    """


##
# The end.

# Generated at 2022-06-13 20:43:21.222676
# Unit test for function has_any_callables
def test_has_any_callables():
    s = set()
    assert has_any_callables(s,'add','remove','clear','something')
    assert has_any_callables(s,'add','clear','something')
    assert has_any_callables(s,'something') is False


# Generated at 2022-06-13 20:43:24.148776
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), "get", "keys", "items", "values") is True
    assert has_callables(dict(), "get", "keys", "items", "foo") is False
    assert has_callables(dict(), "get", "keys", "items", "None") is False

test_has_callables()


# Generated at 2022-06-13 20:43:30.150829
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(),'get','keys','items','values','something')
    assert has_any_attrs(dict(),'get','keys','items','values','__setitem__')
    assert has_any_attrs(str(),'get','keys','items','values','__setitem__')


# Generated at 2022-06-13 20:43:35.075516
# Unit test for function has_any_attrs
def test_has_any_attrs():
    obj = dict(a=1, b=2)
    assert has_any_attrs(obj, "keys", "get", "items") is True
    assert has_any_attrs(obj, "foo", "bar", "baz") is False


# Generated at 2022-06-13 20:43:37.378661
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'foo') is True

# Generated at 2022-06-13 20:43:46.084732
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = {
        'get': lambda: True,
        'keys': lambda: True,
        'items': lambda: True,
        'values': lambda: True,
        'something': lambda: True,
    }
    obj2 = {
        'get': lambda: True,
        'keys': lambda: True,
        'items': lambda: True,
        'values': lambda: True,
        'something': 'something'
    }
    obj3 = {
        'get': lambda: True,
        'keys': lambda: True,
        'items': lambda: True,
        'values': lambda: True,
        'something': None
    }
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')

# Generated at 2022-06-13 20:43:55.554863
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(list(), 'extend', 'append', 'insert') is True
    assert has_any_callables(list(), 'extend', 'append', 'foo') is True
    assert has_any_callables('foo', 'extend', 'append', 'insert') is False
    assert has_any_callables(0, 'extend', 'append', 'insert') is False
    assert has_any_callables(None, 'extend', 'append', 'insert') is False
    assert has_any_callables([], 'extend', 'append', 'insert') is True
    assert has_any_callables([], 'foo', 'extend', 'append') is False



# Generated at 2022-06-13 20:43:59.575741
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test the ``has_any_callables`` function."""
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:44:11.874989
# Unit test for function has_callables
def test_has_callables():
    # case 1
    dict1 = dict(a=1, b=2)
    result = has_callables(dict1, 'get', 'keys', 'items', 'values', 'foo')
    assert result is True
    # case 2
    list1 = [1, 2, 3]
    result = has_callables(list1, 'append', 'insert', 'pop', 'remove', 'clear')
    assert result is True
    # case 3
    str1 = '1234'
    result = has_callables(str1, 'find', 'index', 'isalpha', 'isdigit', 'len')
    assert result is True



# Generated at 2022-06-13 20:44:16.546792
# Unit test for function has_callables
def test_has_callables():
    obj=dict()
    a=has_callables(obj,'get','keys','items','values')
    b=has_callables(obj,'foo','bar')
    assert a is True
    assert b is False


# Generated at 2022-06-13 20:44:21.608776
# Unit test for function has_any_callables
def test_has_any_callables():
    import collections
    assert has_any_callables(collections.deque(),'append','popleft')
    assert not has_any_callables(collections.deque(),'append','foobar' )
    assert not has_any_callables(collections.deque(),'foo','bar' )


# Generated at 2022-06-13 20:44:22.403462
# Unit test for function has_callables
def test_has_callables():
    assert has_callables({}, 'get', 'keys', 'items', 'values') == True

# Generated at 2022-06-13 20:44:26.047562
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict()
    assert has_any_callables(d,'items','keys','values','foo') == True
    assert has_any_callables(d,'foo') == False



# Generated at 2022-06-13 20:44:29.671525
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict, 'get', 'keys', 'items', 'values') is True
    return True


# Generated at 2022-06-13 20:44:36.441582
# Unit test for function has_callables
def test_has_callables():
    from flutils.objutils import has_callables
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserList,
        defaultdict,
    )
    if has_callables(1, 'e1', 'e2', 'e3') is False:
        print('Passed')
    else:
        print('Failed')
    if has_callables(list(), 'e1', 'e2', 'e3') is False:
        print('Passed')
    else:
        print('Failed')
    if has_callables(None, 'e1', 'e2', 'e3') is False:
        print('Passed')
    else:
        print('Failed')

# Generated at 2022-06-13 20:44:47.229289
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
    import decimal
    import os

    # noinspection PyUnresolvedReferences
    assert has_callables(list(), 'append', 'extend', 'pop', 'sort') is True
    # noinspection PyUnresolvedReferences
    assert has_callables(list(), 'append', 'extend', 'pop', 'foo') is False

    # noinspection PyUnresolvedReferences
    assert has_callables(dict(), 'clear', 'keys', 'items', 'update',
                         'setdefault') is True
    # noinspection PyUnresolvedReferences

# Generated at 2022-06-13 20:44:50.501711
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False



# Generated at 2022-06-13 20:45:01.869247
# Unit test for function has_callables
def test_has_callables():

    assert has_callables(dict(),'get','keys','items','values') is True
    assert has_callables(dict(),'get','keys','items','values','foo') is False
    assert has_callables(dict(),'get','keys','items','foo') is False
    assert has_callables(dict(),'foo', 'get','keys','items') is False
    assert has_callables(dict(),'get2','keys','items') is False
    assert has_callables(dict(),'get','keys2','items') is False
    assert has_callables(dict(),'get','keys','items2') is False



# Generated at 2022-06-13 20:45:14.040210
# Unit test for function has_callables
def test_has_callables():
    resource = {}
    assert not has_callables(resource, 'foo')
    resource['foo'] = 0
    assert not has_callables(resource, 'foo')
    resource['foo'] = lambda: None
    assert has_callables(resource, 'foo')
    assert not has_callables(resource, 'foo', 'bar')
    resource['bar'] = 0
    assert not has_callables(resource, 'foo', 'bar')
    resource['bar'] = lambda: None
    assert has_callables(resource, 'foo', 'bar')


# Generated at 2022-06-13 20:45:17.527040
# Unit test for function has_callables
def test_has_callables():

    from pprint import pprint as pp
    #pp(has_any_callables(list(range(10)),'append','insert'))
    pp(has_any_callables(dict(),'get','keys','items','values','something'))



# Generated at 2022-06-13 20:45:27.805319
# Unit test for function has_callables
def test_has_callables():
    from collections import (
        UserList,
        deque,
    )
    from collections.abc import (
        Iterator,
        KeysView,
        ValuesView,
    )
    _LIST_LIKE = (
        list,
        set,
        frozenset,
        tuple,
        deque,
        Iterator,
        ValuesView,
        KeysView,
        UserList
    )

    obj = dict()
    assert(has_callables(obj, 'get', 'keys', 'values'))
    obj = list()
    assert(has_callables(obj, 'append', 'count', 'index'))



# Generated at 2022-06-13 20:45:30.549245
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:45:38.483821
# Unit test for function has_callables
def test_has_callables():
    import unittest
    class TestHasCallables(unittest.TestCase):
        def test_is_list_like(self):
            # Verify that dict.keys is list-like
            obj = dict(a=1, b=2)
            self.assertTrue(has_callables(obj,'keys'))
            obj = dict(a=1, b=2)
            self.assertFalse(has_callables(obj,'something'))
    unittest.main(exit=False)


# Generated at 2022-06-13 20:45:40.458533
# Unit test for function has_callables
def test_has_callables():
    expected = True
    actual = has_callables(dict(),'get','keys','items','values')
    assert expected == actual



# Generated at 2022-06-13 20:45:45.789427
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') == True
    assert has_callables(dict(),'get','keys','items','foo') == False


# Generated at 2022-06-13 20:45:49.757659
# Unit test for function has_callables
def test_has_callables():
    assert has_callables({'a':1,'b':2}, 'get', 'keys', 'values') is True



# Generated at 2022-06-13 20:45:59.316603
# Unit test for function has_callables
def test_has_callables():
    """Testing has_callables() function with unittest
    """
    # Create a test class
    class nonListClass:
        """Sample non-list class
        """
        def __init__(self, data):
            self.data = data
        def iter(self):
            return iter(self.data)

    class ListClass(list):
        """Sample list class
        """
        def __init__(self, data):
            self.data = data

    class nonListClass(nonListClass):
        """Sample non-list class
        """
        def __init__(self, data):
            self.data = data
        def iter(self):
            return iter(self.data)

    def test_nonListClass():
        """Testing non-list class
        """

# Generated at 2022-06-13 20:46:04.951186
# Unit test for function has_callables
def test_has_callables():
    dict_ = dict()
    list_ = list()
    set_ = set()
    assert has_callables(dict_, 'get', 'keys', 'items') is True
    assert has_callables(list_, 'append', 'extend', 'copy') is True
    assert has_callables(set_, 'add', 'copy', 'pop') is True


# Generated at 2022-06-13 20:46:14.372173
# Unit test for function has_callables
def test_has_callables():
    assert has_callables([1,2,3], 'count') is True




# Generated at 2022-06-13 20:46:22.537903
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_any_callables(dict(), 'key', 'item', 'value', 'foo')
    assert has_any_callables(set(), 'add', 'keys', 'items', 'values')
    assert has_any_callables(list(), 'append', 'remove', 'items', 'values')
    assert has_any_callables(tuple(), 'count', 'index', 'items', 'values')
    assert not has_any_callables(tuple(), 'count', 'index', 'item', 'value')

# Generated at 2022-06-13 20:46:26.726832
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict._make, 'get', 'keys', 'items', 'values') is False



# Generated at 2022-06-13 20:46:41.794062
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(obj, 'keys', 'items', 'values', 'foo', '__getitem__') is True
    assert has_any_callables(obj, 'keys', 'items', 'values', 'foo', '__isub__') is False
    assert has_any_callables(obj, 'keys', 'items', 'values', 'foo', '__isub__', '__getitem__') is True
    assert has_any_callables(obj, 'keys', 'items', 'values', '__iadd__', '__getitem__') is True

# Generated at 2022-06-13 20:46:46.753463
# Unit test for function has_callables
def test_has_callables():
    """Check that has_callables function works as expected"""
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'items', 'values') is True
    assert has_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is False



# Generated at 2022-06-13 20:46:56.880300
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(a=1, b=2), 'get', 'keys', 'items')
    assert has_any_callables(dict(a=1, b=2), 'foo', 'bar', 'items')
    assert has_any_callables(dict(a=1, b=2), 'foo', 'bar', 'items') == False
    assert has_any_callables(dict(a=1, b=2), 'keys', 'foo', 'bar') == False
    assert has_any_callables(None, 'get', 'keys', 'items') == False


# Generated at 2022-06-13 20:47:04.108117
# Unit test for function has_any_callables
def test_has_any_callables():
    def add(a, b):
        return a + b

    class TestClass(object):
        def __init__(self):
            self.add = add

    a = TestClass()
    assert has_any_callables(a, 'add')
    assert has_any_callables(a, 'add', 'mul')
    assert has_any_callables(a, 'mul') is False
    assert has_any_callables(a, 'mul', 'add', 'div')


# Generated at 2022-06-13 20:47:09.472466
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'get','keys','items','valuesaaa','foo') is False
    assert has_any_callables(dict(),"keys","values") is True


# Generated at 2022-06-13 20:47:13.996848
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'foo') is True



# Generated at 2022-06-13 20:47:21.764434
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables({}, "get", "keys", "items", "values", "foo") is True
    assert has_any_callables(dict(), "__init__", "__call__") is False
    assert has_any_callables(dict(), "get", "foo", "bar") is True
    assert has_any_callables(dict(), "bar", "baz") is False
    assert has_any_callables(list(), "append", "extend", "foo") is True
    assert has_any_callables(list(), "foo", "bar", "baz") is False
    return True


# Generated at 2022-06-13 20:47:34.578806
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2, c=3)
    assert has_any_callables(obj, 'get', 'keys', 'values', 'has_any_callables') is True
    assert has_any_callables(obj, 'get', 'keys', 'values', 'foo') is False



# Generated at 2022-06-13 20:47:40.045479
# Unit test for function has_any_callables
def test_has_any_callables():
    try:
        from flutils.objutils import has_any_callables
    except ImportError:
        from flutils.objutils import has_any_callables

    obj = dict(a=1, b=2)

    assert has_any_callables(obj, 'items', 'foo') is True
    assert has_any_callables(obj, 'foo', 'bar') is False



# Generated at 2022-06-13 20:47:41.998053
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:47:47.677429
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test function has_any_callables"""
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'foo') is True
    assert has_any_callables(dict(), 'foo', 'bar') is False
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values',
                             'foo') is True



# Generated at 2022-06-13 20:47:51.266479
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True
    assert has_callables(dict(),'get','keys','items','values','foo') is False


# Generated at 2022-06-13 20:47:55.919248
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') == True
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'a') == False


# Generated at 2022-06-13 20:47:57.672821
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True



# Generated at 2022-06-13 20:48:10.151512
# Unit test for function has_callables
def test_has_callables():
    """Tests for function has_callables"""
    from collections import ChainMap
    from decimal import Decimal
    obj = dict(a=1, b=2)
    assert (has_callables(obj, 'get', 'keys', 'items', 'values') is True)
    assert (has_callables(obj, 'get', 'keys', 'items', 'something') is True)
    assert (has_callables(deque([1, 2]), 'pop', 'pop', 'pop') is True)
    assert (has_callables(obj, 'pop', 'pop', 'pop') is False)
    assert (has_callables(set([1, 2]), 'pop', 'pop', 'pop') is True)
    assert (has_callables(frozenset([1, 2]), 'pop', 'pop', 'pop') is False)

# Generated at 2022-06-13 20:48:12.434228
# Unit test for function has_any_callables
def test_has_any_callables():
    class MyDict(dict):
        def get(self, key=None):
            return self[key]

    md = MyDict(a=1, b=2)
    assert has_any_callables(md, 'get', 'keys', 'items', 'values')



# Generated at 2022-06-13 20:48:14.692155
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:48:29.653014
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    assert has_any_callables(dict(),'get','keys','items','values','foo')


# Generated at 2022-06-13 20:48:31.822639
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:48:38.185078
# Unit test for function has_any_callables
def test_has_any_callables():
    """ Unit test for function has_any_callables.
    """

    def foo():
        return "foo"

    class A:
        __slots__ = ['a', 'b', '__dict__']

        def __init__(self):
            self.a = 1
            self.b = 2

    class B(A):
        def __init__(self):
            super().__init__()
            self.c = 3

        def bar(self):
            return 'bar'

    l = list()
    d = dict()
    s = set()
    s2 = frozenset()
    t = tuple()
    it = iter(s)
    v = ValuesView(d)
    k = KeysView(d)
    u = UserList()
    a = A()
    b = B()


# Generated at 2022-06-13 20:48:42.434473
# Unit test for function has_any_callables
def test_has_any_callables():
    _map = dict()
    assert has_any_callables(_map, 'get', 'foo') is True
    assert has_any_callables(_map, 'foo') is False


# Generated at 2022-06-13 20:48:48.282514
# Unit test for function has_any_callables
def test_has_any_callables():
    item = {'get': lambda x: x, 'items': lambda x: x, 'values': lambda x: x, }
    assert has_any_callables(item, 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:48:55.599441
# Unit test for function has_callables
def test_has_callables():
    from collections import UserDict
    from flutils.objutils import has_callables
    try:
        import pandas as pd
    except ImportError:
        pd = None

    test_obj = UserDict()
    assert has_callables(test_obj, 'get', 'setdefault', 'items')

    if pd is not None:
        test_obj = pd.DataFrame()
        assert has_callables(test_obj, 'to_dict', 'drop_duplicates')

    test_obj = set()
    assert has_callables(test_obj, 'add', 'pop', 'remove')

# Generated at 2022-06-13 20:48:59.713249
# Unit test for function has_callables
def test_has_callables():
    """ Test cases for has_callables.
    Test Cases:
        """
    ret = has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert ret is True, "Function has_callables did not return the expected results on a dictionary"



# Generated at 2022-06-13 20:49:06.547335
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1, b=2)
    assert has_any_callables(d, 'get', 'has_key', 'keys', 'items', 'values',
        'foo')
    assert has_any_callables(d, 'foo', 'keys', 'items', 'values', 'something')
    assert not has_any_callables(d, 'something', 'foo', 'bars')


# Generated at 2022-06-13 20:49:12.752858
# Unit test for function has_callables
def test_has_callables():
    """Unit test for function ``has_callables``.

    Args:
        None

    :rtype:
        None

    """
    obj = dict(a=1, b=2, c=3)
    assert has_callables(obj, 'get', 'keys', 'values') is True
    assert has_callables(obj, 'get', 'keys', 'values', 'something') is False
    assert has_callables(obj, 'get', 'keys', 'values', 'items') is True



# Generated at 2022-06-13 20:49:20.981950
# Unit test for function has_callables
def test_has_callables():
    """Test function has_callables."""
    from collections import defaultdict
    dd = defaultdict(dict)
    assert has_callables(dd, 'get') is True
    assert has_callables(dd, 'items') is True
    assert has_callables(dd, 'keys') is True
    assert has_callables(dd, 'values') is True
    assert has_callables(dd, 'get', 'items') is True
    assert has_callables(dd, 'get', 'items', 'keys') is True
    assert has_callables(dd, 'get', 'items', 'keys', 'values') is True
    assert has_callables(dd, 'get', 'items', 'keys', 'values', 'foo') is False

# Generated at 2022-06-13 20:49:54.760400
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils import objutils
    from pprint import pprint
    import sys
    import types

    # Define the 'obj' to check
    _obj = dict(
        **{'__contains__': lambda: None,
            '__iter__': lambda: None,
            '__new__': lambda: None,
            '__reversed__': lambda: None,
            '__str__': lambda: None}
    )

    # Get the list of all the callable attributes of the 'obj' that is of type
    # 'types.FunctionType'
    _type_filter = lambda x: True if isinstance(
        getattr(_obj, x),
        types.FunctionType
    ) else False
    _list_callables = list(
        filter(_type_filter, dir(_obj))
    )

    # Check the

# Generated at 2022-06-13 20:50:00.915571
# Unit test for function has_any_callables
def test_has_any_callables():
    """ test for function has_any_callables
    """

    # print('objutils test_has_any_callables')
    assert has_any_callables(dict(),'get','keys','items','', 'values')
    assert has_any_callables(dict(),'get','keys','items','values')


# Generated at 2022-06-13 20:50:03.327106
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')



# Generated at 2022-06-13 20:50:07.286086
# Unit test for function has_any_callables
def test_has_any_callables():
    class X:
        def foo(self, x):
            return x
    obj = X()
    assert has_any_callables(obj, 'foo', 'bar', 'baz')



# Generated at 2022-06-13 20:50:15.517707
# Unit test for function has_callables
def test_has_callables():
    assert has_callables({}, 'get', 'keys', 'items', 'values') is True
    assert has_callables([], 'append', 'reverse', 'sort', 'insert') is True
    assert has_callables(dict(foo=1), 'get') is False
    assert has_callables([1, 2, 3], 'append', 'reverse', 'sort', 'foo') is False
    assert has_callables(tuple(), 'append', 'reverse', 'sort', 'foo') is False



# Generated at 2022-06-13 20:50:16.818270
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values')



# Generated at 2022-06-13 20:50:19.834738
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:50:29.365398
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables({}, 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_any_callables(dict(a=1, b=2, c=3), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(a=1, b=2, c=3), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(a=1, b=2, c=3), 'setdefault', 'keys', 'items', 'values') is False

# Generated at 2022-06-13 20:50:31.416496
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:50:33.186275
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')


# Generated at 2022-06-13 20:51:23.406465
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2, something='foo', a_function=lambda x: x)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') == True



# Generated at 2022-06-13 20:51:25.048054
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True



# Generated at 2022-06-13 20:51:29.059555
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict, 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:51:40.789198
# Unit test for function has_any_callables
def test_has_any_callables():
    from types import BuiltinFunctionType

    class _Foo:

        def __init__(self):
            self.twisty = {
                'foo': 'bar',
            }

        def foo(self):
            pass

    class _Bar:

        def __init__(self):
            self.twisty = {
                'foo': 'bar',
            }

        def bar(self):
            pass

    foo = _Foo()
    bar = _Bar()

    assert has_any_callables(foo, 'foo') is True
    assert has_any_callables(bar, 'bar') is True
    assert has_any_callables(bar, 'foo') is False
    assert has_any_callables(bar, 'twisty') is False

# Generated at 2022-06-13 20:51:47.069356
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_callables(dict(), 'get', 'foo')
    assert not has_callables(dict(), 'something', 'foo')


# Generated at 2022-06-13 20:51:53.642130
# Unit test for function has_any_callables
def test_has_any_callables():
    import collections
    from flutils.objutils import has_any_callables

    assert has_any_callables(collections, "deque", "KeysView") is True
    assert has_any_callables(collections, "deque", "KeysView", "bar") is True
    assert has_any_callables(collections, "KeysView", "bar") is False
    assert has_any_callables(collections, "bar") is False



# Generated at 2022-06-13 20:51:55.540218
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')



# Generated at 2022-06-13 20:52:02.571163
# Unit test for function has_callables
def test_has_callables():
    '''Tests ``has_callables``.

    For example:
        >>> from flutils.objutils import has_callables
        >>> obj = dict(a=1, b=2)
        >>> has_callables(obj, 'get', 'items', 'values')
        True
    '''
    obj = dict(a=1, b=2)
    res = has_callables(obj, 'get', 'items', 'values')
    assert res is True


# Unit test function has_attrs

# Generated at 2022-06-13 20:52:05.081771
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys') is True



# Generated at 2022-06-13 20:52:18.683399
# Unit test for function has_any_callables
def test_has_any_callables():
    """
    Test has_any_callables
    """
    # step one, test input check
    with pytest.raises(TypeError):
        has_any_callables(1, "1", "2")

    # step two, test input check
    with pytest.raises(TypeError):
        has_any_callables("1", 1, 2)

    # step three, no input excepted obj
    assert has_any_callables("1") == False

    # step four, obj has all the attrs
    assert has_any_callables("1", "__add__", "__doc__") == True

    # step five, obj has some attrs but not all
    assert has_any_callables("1", "__add__", "__doc__", "__and__") == True

    # step six, obj