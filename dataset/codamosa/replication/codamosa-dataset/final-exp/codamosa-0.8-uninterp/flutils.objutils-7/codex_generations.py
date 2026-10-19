

# Generated at 2022-06-13 20:43:19.679731
# Unit test for function has_any_attrs
def test_has_any_attrs():
    # Define the function we want to test
    #TO DO: not implemented
    function_name="has_any_attrs"
    return_success=True
    return_value=True
    exception_expected=False
    # Define the parameters we want to test
    inputs = dict()
    inputs["obj"] = dict()
    inputs["*attrs"] = ['get','keys','items','values','something']
    expected_results = dict()
    expected_results["obj"] = dict()
    expected_results["*attrs"] = ['get','keys','items','values','something']
    expected_results["return"], expected_results["exception"] = return_success, exception_expected
    
    # Run the unit test
    return unit_test_function(function_name,inputs,expected_results)


# Generated at 2022-06-13 20:43:25.876832
# Unit test for function has_callables
def test_has_callables():
    """Test the has_callables function.

    Returns:
        None. Raises an exception if the test fails.
    """
    test_obj1 = dict()
    test_obj2 = list()
    test_obj3 = list()

    assert has_callables(test_obj1, 'get') is True
    assert has_callables(test_obj1, 'get', 'keys') is True
    assert has_callables(test_obj1, 'get', 'keys', 'items') is True
    assert has_callables(test_obj1, 'get', 'keys', 'items', 'values') is True
    assert has_callables(test_obj1, 'get', 'keys', 'items', 'values', 'clear') \
        is True

    assert has_callables(test_obj2, 'append') is True


# Generated at 2022-06-13 20:43:29.827522
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()
    attrs = ['get', 'items', 'keys', 'something', 'values']
    assert has_any_callables(obj, *attrs) is True


# Unit tests for the function has_any_attrs

# Generated at 2022-06-13 20:43:41.148786
# Unit test for function has_any_callables
def test_has_any_callables():
    cls_dict = {
        'get': lambda: 'get',
        'test': lambda: 'test',
        'test2': lambda: 'test2',
    }
    cls = type('Test', (object,), cls_dict)
    assert has_any_callables(cls, 'get', 'test', 'test2') == True
    assert has_any_callables(cls, 'get', 'test', 'foo') == True
    assert has_any_callables(cls, 'foo', 'bar') == False

# Generated at 2022-06-13 20:43:43.383392
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(a=1, b=2), 'get', 'items', 'keys') is True


# Generated at 2022-06-13 20:43:45.153638
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo',) == True


# Generated at 2022-06-13 20:43:56.334265
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'get','keys','items','values','__class__') == True
    assert has_any_callables(dict(),'get','keys','items','values') == True
    assert has_any_callables(dict(),'get','keys','items') == True
    assert has_any_callables(dict(),'get','keys') == True
    assert has_any_callables(dict(),'keys','items','values') == True
    assert has_any_callables(dict(),'keys','items') == True
    assert has_any_callables(dict(),'keys') == True
    assert has_any_callables(dict(),'items','values','__class__') == True
    assert has_

# Generated at 2022-06-13 20:43:58.673429
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


if __name__ == '__main__':
    print('Testing objutils.py...')
    test_has_callables()
    print('Done.')

# Generated at 2022-06-13 20:44:05.684436
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(10, 'bit_length', 'conjugate') is False
    assert has_any_callables((10, 20, 30), '__getitem__', '__len__') is True
    assert has_any_callables(dict(a=0, b=0), 'get', 'keys') is True
    assert has_any_callables((10, 20, 30), '__getitem__', '__len__') is True
    assert has_any_callables(range(4), '__getitem__', '__len__') is True
    assert has_any_callables(reversed(range(4)), '__getitem__', '__len__') is True

if __name__ == "__main__":
    test_has_any_callables()

# Generated at 2022-06-13 20:44:07.831203
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') == True


# Generated at 2022-06-13 20:44:21.869540
# Unit test for function has_attrs
def test_has_attrs():
    assert has_attrs(dict(),'get','keys','items','values') is True
    assert has_attrs(dict(),'foo') is False
    assert has_attrs(list(),'append','insert','remove','pop') is True
    assert has_attrs(list(),'foo') is False
    assert has_attrs(tuple(),'index','count') is True
    assert has_attrs(tuple(),'foo') is False
    assert has_attrs('hello','count','rstrip') is True
    assert has_attrs('hello','foo') is False
    obj = list()
    assert has_attrs(obj,'append','insert','remove','pop') is True
    assert has_attrs(obj,'foo') is False


# Generated at 2022-06-13 20:44:27.672507
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_callables(dict(), 'foo')
    assert not has_callables(dict(), 'foo', 'bar')
    assert not has_callables(dict(), 'foo', 'bar', 'eggs')


# Generated at 2022-06-13 20:44:35.973871
# Unit test for function has_any_callables
def test_has_any_callables():
    f = 'flutils.objutils.test_has_any_callables'
    v = 'test_has_any_callables'
    attrs = 'get keys items values foo'.split()

    # Test dict
    d = dict(a=1, b=2)
    assert has_any_callables(d, *attrs) is True
    assert has_any_attrs(d, *attrs) is True

    # Test empty dict
    d = dict()
    assert has_any_callables(d, *attrs) is True
    assert has_any_attrs(d, *attrs) is True

    # Test frozenset
    s = frozenset(('a', 'b', 'c', 'd'))
    assert has_any_callables(s, *attrs) is True

# Generated at 2022-06-13 20:44:39.073223
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') == True


# Generated at 2022-06-13 20:44:48.903284
# Unit test for function has_callables
def test_has_callables():
    class CallableAttr:
        def callable(self):
            pass

    def some_func():
        pass

    obj = CallableAttr()
    attrs = ['callable']
    assert has_callables(obj, *attrs) == True

    class NoCallableAttr:
        pass

    obj = NoCallableAttr()
    attrs = ['callable']
    assert has_callables(obj, *attrs) == False

    obj = NoCallableAttr()
    attrs = ['callable', 'cal']
    assert has_callables(obj, *attrs) == False

    obj = NoCallableAttr()
    attrs = []
    assert has_callables(obj, *attrs) == False

    def some_func():
        pass

    obj = some_func
    att

# Generated at 2022-06-13 20:44:53.818617
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something')
    assert has_any_callables(dict(),'get','keys')



# Generated at 2022-06-13 20:45:04.640442
# Unit test for function has_callables
def test_has_callables():
    """Unit test for function has_callables"""
    # Test list

# Generated at 2022-06-13 20:45:09.009658
# Unit test for function has_attrs
def test_has_attrs():
    obj = dict(a=1, b=2)
    assert has_attrs(obj, 'keys', 'items', 'values') is True
    assert has_attrs(obj, 'get', 'keys', 'items', 'values') is False

# Generated at 2022-06-13 20:45:18.593409
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), '__getitem__', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', '__contains__')
    assert has_any_callables(dict(), '__contains__', '__setitem__', '__getitem__') is False
    assert has_any_callables(dict(), '__contains__', '__setitem__', '__getitem__') is False


# Generated at 2022-06-13 20:45:26.670542
# Unit test for function has_any_callables
def test_has_any_callables():
    dict_ = dict(a=1, b=2)
    is_true = has_any_callables(dict_, "get", "keys", "items", "values", 'foo')
    is_false = has_any_callables(dict_, "foo")
    assert is_true is True
    assert is_false is False

if __name__ == '__main__':
    # Run unit tests
    test_has_any_callables()

# Generated at 2022-06-13 20:45:32.476274
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:45:33.656128
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True



# Generated at 2022-06-13 20:45:40.969008
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','values','items','something')
    assert has_any_callables(dict(),'get','keys','values','items') is True
    assert has_any_callables(dict(),'get','foo','something') is True
    assert has_any_callables(dict(),'foo','something') is False
    return


# Generated at 2022-06-13 20:45:46.428276
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1,b=2)
    res = has_any_callables(obj,'get','values','items')
    assert res == True


# Generated at 2022-06-13 20:45:57.208070
# Unit test for function has_callables
def test_has_callables():
    from os import environ
    # Test passing normal dictionary class
    assert has_callables(dict(),'get','keys','items','values')
    # Test passing os.environ which is NOT normal dict class
    assert has_callables(environ,'get','keys','items','values')
    # Test passing os.environ which is NOT normal dict class, but function
    #  keys does not exists
    assert not has_callables(environ,'get','items','values')
    # Test passing dict class with a non-callable attribute
    assert not has_callables(dict(),'clear','__class__')


# Generated at 2022-06-13 20:46:08.811968
# Unit test for function has_callables
def test_has_callables():
    from collections import ChainMap
    from decimal import Decimal
    from functools import partial
    from io import StringIO
    from unittest.mock import Mock
    from ..objutils import has_callables
    from ..pycompat23 import int_types, str_types, urlparse

    dflt = dict(
        get=partial(1, 2),
        items=dict.items,
        keys=dict.keys,
        values=dict.values,
    )

    assert has_callables(dict(dflt), *dflt.keys()) is True
    assert has_callables(dict(), *dflt.keys()) is False
    assert has_callables(None, *dflt.keys()) is False
    assert has_callables(True, *dflt.keys()) is False

# Generated at 2022-06-13 20:46:21.481988
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()
    attrs = ('get', 'keys', 'items', 'values', 'foo')
    expected = True
    assert expected == has_any_callables(obj, *attrs), "expected %s" % expected
    #
    obj = dict()
    attrs = ('get', 'keys', 'items', 'values', '__repr__')
    expected = True
    assert expected == has_any_callables(obj, *attrs), "expected %s" % expected
    #
    obj = dict()
    attrs = ('get', 'keys', 'items', 'values', '__repr__', 'foo')
    expected = True
    assert expected == has_any_callables(obj, *attrs), "expected %s" % expected
    #
    obj = dict()

# Generated at 2022-06-13 20:46:23.094755
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:46:33.548734
# Unit test for function has_callables
def test_has_callables():
    import functools
    import collections

    def test(obj, *attrs):
        print("{:>12s} - {}".format("has_callables", " / ".join(attrs)))
        print("{:>12s} - {}".format("returns", has_callables(obj, *attrs)))

    # setup
    class Obj:
        pass

    obj = Obj()
    obj.foo = lambda: None
    obj.bar = None

    # tests
    test(obj, "foo", "bar")
    test(obj, "foo", "bar", "baz")

    obj.foo = None
    test(obj, "foo", "bar")

    obj.foo = "foo"
    test(obj, "foo", "bar")

    obj.bar = lambda: None

# Generated at 2022-06-13 20:46:46.506330
# Unit test for function has_any_callables
def test_has_any_callables():
    def func():
        pass

    class Foo:
        def bar(self):
            pass

    assert has_any_callables(dict(), 'foo') is False
    assert has_any_callables(dict, 'foo') is False
    assert has_any_callables(Foo(), 'foo') is False
    assert has_any_callables(Foo, 'foo') is False
    assert has_any_callables(Foo().bar, 'foo') is False
    assert has_any_callables(Foo.bar, 'foo') is False
    assert has_any_callables(func, 'foo') is False
    assert has_any_callables(func(), 'foo') is False

    assert has_any_callables(dict(), 'keys') is True

# Generated at 2022-06-13 20:46:55.141875
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')
    assert not has_callables(dict(),'get','keys','items','values','foo')
    assert not has_callables(dict(),'get','keys','items','foo')
    assert not has_callables(dict(),'get','foo','items')
    assert not has_callables(dict(),'get')


# Generated at 2022-06-13 20:46:59.222384
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit tests for function has_any_callables."""

    assert has_any_callables(object(), '__eq__') is False



# Generated at 2022-06-13 20:47:08.072957
# Unit test for function has_any_callables
def test_has_any_callables():
    """
        Test function has_any_callables
    """
    from .helpers import ensure_exception
    from .helpers import ensure_exception_msg
    from .helpers import ensure_illegal_value
    from .helpers import ensure_return_type

    # Should throw for a  missing 'obj'
    ensure_exception(has_any_callables, TypeError, "Expected argument, \'obj\'.",
                     )
    ensure_exception(has_any_callables, TypeError, "Expected argument, \'obj\'.",
                     attrs='foo')

    # Should throw for a missing attribute
    ensure_exception(has_any_callables, ValueError,
                     "Expected one or more attributes, but got 0.",
                     object())

    # Should return None for a missing attribute
    ensure_exception

# Generated at 2022-06-13 20:47:15.193532
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables."""
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'get','keys','items','values','foo','__init__') == True
    assert has_any_callables(dict(),'get','keys','items','values','foo','_foo') == False
    assert has_any_callables(dict(),'get','keys','items','values','foo','_foo','__foo') == False
    assert has_any_callables(dict(),'foo','__init__') == False


# Generated at 2022-06-13 20:47:24.294845
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test that has_any_callables checks which of the given attributes exist on
    the given object and are callable.

    :return: True if all tests pass; False otherwise.
    :rtype: bool
    """
    all_passed = True
    obj = dict()

    attr1 = 'get'
    attr2 = 'update'
    attr3 = 'foo'
    attr4 = 'bar'
    attr5 = 'baz'

    if has_any_callables(obj, attr1, attr2, attr3, attr4, attr5) is not True:
        print(
            f'Test failed: {attr1}, {attr2} are callables on given obj.')
        all_passed = False

# Generated at 2022-06-13 20:47:39.401982
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), "get", "keys", "items", "values", "foo")
    assert not has_any_callables(dict(), "get", "keys", "items", "values", "foo", "bar")
    assert not has_any_callables("baz", "get", "keys", "items", "values", "foo")
    assert not has_any_callables("baz", "get", "keys", "items", "values", "foo", "bar")
    assert not has_any_callables(None, "get", "keys", "items", "values", "foo")
    assert not has_any_callables(None, "get", "keys", "items", "values", "foo", "bar")
    

# Generated at 2022-06-13 20:47:43.747955
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1)
    assert has_any_callables(obj, "items", "values") is True
    assert has_any_callables(obj, "foo", "bar") is False
    assert has_any_callables(obj, "a") is False



# Generated at 2022-06-13 20:47:49.290188
# Unit test for function has_callables
def test_has_callables():
    assert (has_callables(dict(),'get','keys','items','values')) is True
    assert (has_callables(dict(),'get','keys','items','values','foo')) is False


# Generated at 2022-06-13 20:47:53.464665
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict(), 'get', 'keys', 'items') == False
    assert has_callables(dict(), 'keys', 'keys', 'items', 'values')



# Generated at 2022-06-13 20:48:01.146098
# Unit test for function has_any_callables

# Generated at 2022-06-13 20:48:05.848300
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')


# Generated at 2022-06-13 20:48:10.620225
# Unit test for function has_callables
def test_has_callables():
    call_dict = dict(a=1, b=2)
    assert(has_callables(call_dict, 'get', 'keys', 'items', 'values') == True)


# Generated at 2022-06-13 20:48:21.907865
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'foo', 'bar') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'bar', 'foo') is True
    assert has_any_callables(dict(), 'get', 'bar', 'keys', 'items', 'foo') is True
    assert has_any_callables(dict(), 'bar', 'get', 'keys', 'items', 'foo') is True

    assert has_any_callables(dict(), 'bar', 'baz', 'foo', 'qux', 'derp') is False

# Generated at 2022-06-13 20:48:26.824017
# Unit test for function has_any_callables
def test_has_any_callables():

    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(), 'get2', 'keys2', 'items2', 'values2', 'foo2') is False


# Generated at 2022-06-13 20:48:30.158639
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:48:37.285379
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import Counter
    from unittest import main, TestCase

    class _TestCase(TestCase):
        def setUp(self):
            self.obj = dict()

        def test_has_any_callables_with_none(self):
            self.assertEqual(
                has_any_callables(None, 'foo'),
                False
            )

        def test_has_any_callables_with_obj(self):
            self.assertEqual(
                has_any_callables(self.obj, 'get', 'items', 'keys', 'values'),
                True
            )

        def test_has_any_callables_with_obj_attr(self):
            self.assertEqual(
                has_any_callables(self.obj, 'get', 'foo'),
                True
            )



# Generated at 2022-06-13 20:48:41.672000
# Unit test for function has_callables
def test_has_callables():
    assert(has_callables(dict(),'get','keys','items','values'))
    assert(has_callables(list(),'append','pop','remove','insert','count'))
    
    

# Generated at 2022-06-13 20:48:48.075199
# Unit test for function has_callables
def test_has_callables():
    #from flutils.objutils import has_callables
    obj = dict()
    assert has_callables(obj,'get','keys','items','values') is True
    assert has_callables(obj,'get','keys','items','foo') is False


# Generated at 2022-06-13 20:48:50.995946
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys')
    assert not has_any_callables(dict(),'get','keys')


# Generated at 2022-06-13 20:48:52.670418
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:49:04.661242
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables.

    Returns:
        :obj:`bool`:
            * :obj:`True` if tests pass;
            * :obj:`False` otherwise.

    Example:
        >>> from flutils.objutils import test_has_any_callables
        >>> test_has_any_callables()
        True

    """
    import unittest

    class HasAnyCallables(unittest.TestCase):
        """Tests for function has_any_callables."""

        def test_has_any_callables(self):
            """Test for function has_any_callables."""
            import datetime
            import os
            obj = dict(get=1, keys=2)

# Generated at 2022-06-13 20:49:14.203524
# Unit test for function has_callables
def test_has_callables():
    from pprint import pprint
    from collections import deque
    from collections.abc import Iterator

    d = {'a': 1, 'b': 2, 'c': 3}
    p = deque(['a', 'b', 'c'])
    t = (1, 2, 3)
    s = set([1, 2, 3])
    z = zip(t, p, s)
    i = iter(s)

    obj = d
    attrs = 'keys', 'values', 'items', 'get'
    pprint(has_callables(obj, *attrs))

    obj = p
    attrs = 'pop', 'append', 'count'
    pprint(has_callables(obj, *attrs))

    obj = t
    attrs = 'count', 'index'

# Generated at 2022-06-13 20:49:21.149868
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'get','foo1','items','values','foo2') is True
    assert has_any_callables(dict(),'foo1','foo2','foo3','foo4','foo5') is False


# Generated at 2022-06-13 20:49:29.659467
# Unit test for function has_callables
def test_has_callables():
    assert has_callables({'a': 5}, 'keys', 'get') is True  # True
    assert has_callables({5, 2}, 'keys', 'get') is False  # False
    assert has_callables(2, 'keys', 'get') is False  # False
    assert has_callables(dict(), 'keys', 'get') is True  # True
    assert has_callables(list(), 'keys', 'get') is False  # False
    assert has_callables((1, 2, 3), 'keys', 'get') is False  # False
    assert has_callables(dict(a=1, b=2, c=3), 'keys', 'get') is True  # True


# Generated at 2022-06-13 20:49:33.521735
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    has = has_callables(obj,'get', 'keys', 'items', 'values')
    assert has == True


# Generated at 2022-06-13 20:49:42.580584
# Unit test for function has_any_callables
def test_has_any_callables():
    # Define dictionary
    obj = dict(a=1, b=2)

    # Test if function returns True for any of the following methods
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values') is True

    # Test if function returns False for all of the following methods
    assert has_any_callables(obj, 'foo', 'bar', 'baz', 'qux') is False



# Generated at 2022-06-13 20:49:54.691213
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict.fromkeys, 'get', 'keys') is True
    assert has_callables(dict.fromkeys, 'get', 'keys', 'items') is True
    assert has_callables(dict.fromkeys, 'get', 'keys', 'foo') is False
    assert has_callables(dict, 'fromkeys') is True
    assert has_callables(dict, 'foo', 'bar') is False
    assert has_callables(dict, 'fromkeys', 'get') is False
    assert has_callables(dict, 'fromkeys', 'get', 'keys') is True
    assert has_callables(dict().__class__, 'fromkeys', 'get', 'keys') is True
    assert has_callables(dict, 'fromkeys', 'get', 'keys', 'foo') is False


# Unit test

# Generated at 2022-06-13 20:50:01.373890
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'foo') is True
    assert has_any_callables(dict(), 'get', 'foo') is False
    assert has_any_callables(dict(a=1), 'get', 'items', 'foo') is True



# Generated at 2022-06-13 20:50:10.375275
# Unit test for function has_any_callables
def test_has_any_callables():
    f = open("test.txt", "a")
    assert has_any_callables(f, 'write', 'read', 'close') is True
    f.close()
    assert has_any_callables(f, 'write', 'read', 'close') is False
    assert has_any_callables("abcdef", 'find', 'upper', 'replace') is True
    assert has_any_callables("abcdef", 'find', 'upper', 'length') is False
    assert has_any_callables(dict(), 'keys', 'values', 'items') is True
    assert has_any_callables(dict(), 'keys', 'size', 'items') is False


# Generated at 2022-06-13 20:50:11.562039
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items', 'foo')



# Generated at 2022-06-13 20:50:22.228450
# Unit test for function has_callables
def test_has_callables():
    assert True == has_callables(dict(), 'get', 'keys', 'items', 'values')


# Generated at 2022-06-13 20:50:30.991269
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_any_callables(dict(), 'fuuuu', 'keys', 'items', 'values')
    assert not has_any_callables(dict(), 'fuuuu', 'keys', 'items', 'values', 'bar')
    assert not has_any_callables(dict(a=1, b=2), 'fuuuu', 'keys', 'items', 'values', 'bar')


# Generated at 2022-06-13 20:50:31.746776
# Unit test for function has_any_callables
def test_has_any_callables():
    pass



# Generated at 2022-06-13 20:50:36.038374
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(
        a=1,
        b=2,
        c=3,
        d=4,
        e=5,
    )
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'something') is True



# Generated at 2022-06-13 20:50:40.589234
# Unit test for function has_callables
def test_has_callables():
    """Test function has_callables."""
    assert has_callables(dict(),'get','keys','items','values') is True
    assert has_callables(dict(),'foo','bar') is False



# Generated at 2022-06-13 20:50:47.827304
# Unit test for function has_any_callables
def test_has_any_callables():
    assert True == has_any_callables(dict(),'get','keys','items','values','foo')
    assert True == has_any_callables(dict(),'get','keys','items','values','foo','__setitem__','__getitem__')
    assert False == has_any_callables(dict(),'foo','foo','foo','foo','foo')
    assert False == has_any_callables(dict(),'foo','bar','baz','quux','quuux')


# Generated at 2022-06-13 20:50:53.402859
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test function has_any_callables."""
    obj = dict(a=1, b=2)
    assert has_any_callables(obj,'get','keys','items','values')



# Generated at 2022-06-13 20:50:56.523534
# Unit test for function has_callables
def test_has_callables():
    assert(has_callables(dict(),'get','keys','items','values'))

if __name__ == '__main__':
    test_has_callables()

# Generated at 2022-06-13 20:50:59.793611
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict()
    assert has_any_callables(d, 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:51:09.686800
# Unit test for function has_callables
def test_has_callables():
    def foo(self): return self

    class A:
        def callme(self): return self

    class B:
        def callme(self): return self
        @property
        def prop(self): return self

    class C(B):
        pass

    class D(A,C):
        pass

    class E(A,C):
        def __init__(self): self.prop = foo

    class F(B):
        def callme(self): return self
        def prop(self): return self

    assert(has_callables(D(),'callme','prop') == True)
    assert(has_callables(B(),'callme','prop') == True)
    assert(has_callables(C(),'callme','prop') == True)

# Generated at 2022-06-13 20:51:30.291441
# Unit test for function has_callables
def test_has_callables():
    from unittest import TestCase
    from flutils.objutils import has_callables

    class Dummy(object):
        def foo(self):
            return True

    class DummyCls(object):
        foo = staticmethod(lambda: True)

    assert has_callables(Dummy(), 'foo')
    assert has_callables(DummyCls, 'foo')
    assert has_callables(DummyCls(), 'foo')

    assert not has_callables(Dummy, 'foo')
    assert not has_callables((1, 2, 3), 'foo')

    test_case = TestCase()
    with test_case.assertRaises(AttributeError):
        assert has_callables(Dummy(), 'foo', 'bar')

    with test_case.assertRaises(AttributeError):
        assert has_

# Generated at 2022-06-13 20:51:34.910851
# Unit test for function has_callables
def test_has_callables():
    x = {'a':1,'b':2,'c':3,'d':4}
    actual = has_callables(x,'keys','pop','get','items')
    expected = True
    assert actual == expected


# Generated at 2022-06-13 20:51:37.805811
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables({}, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables({}, 'get', 'keys', 'items', 'values', 'keys') is True


# Generated at 2022-06-13 20:51:39.533223
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True



# Generated at 2022-06-13 20:51:47.462655
# Unit test for function has_any_callables
def test_has_any_callables():
    assert not has_any_callables(int,'foo')
    assert has_any_callables(str,'rfind')
    assert not has_any_callables(int,'rfind')
    assert has_any_callables(int,'bit_length')
    assert not has_any_callables(int,'bit_lengthbar')


# Generated at 2022-06-13 20:51:50.197470
# Unit test for function has_callables
def test_has_callables():
    args = (dict(), 'get', 'keys', 'values')
    assert has_callables(*args) is True


# Generated at 2022-06-13 20:51:55.415271
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert not has_any_callables(dict(),'foo','bar','baz')


# Generated at 2022-06-13 20:51:59.858024
# Unit test for function has_callables
def test_has_callables():
    """
    Test function 'has_callables'.
    """
    # Test 1
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'keys', 'items', 'values', 'pop') == True



# Generated at 2022-06-13 20:52:04.613375
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'something') is False



# Generated at 2022-06-13 20:52:13.581087
# Unit test for function has_callables
def test_has_callables():
    """
    The three constants passed to the test function for both tests should already exist as methods on the object and be callable.
    The first value should be a valid method and the second a valid attribute on the object.
    """
    # Pass two string constants that are valid attributes on the object
    assert has_callables(dict(), "get", "set")

    # Pass two string constants that are valid attributes on the object
    assert not has_callables(dict(), "get", "something")


# Generated at 2022-06-13 20:52:52.475141
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(list(),'__getitem__')
    assert has_any_callables(set(),'add')
    assert has_any_callables(frozenset(),'add')
    assert has_any_callables(tuple(),'__getitem__')
    assert has_any_callables(deque(),'append','appendleft','extend','extendleft','pop','popleft')

# Generated at 2022-06-13 20:53:02.848917
# Unit test for function has_any_callables
def test_has_any_callables():
    org = dict(a=1, b=2)
    builtin = type(dict())

    # has_any_callables(org, 'get', 'keys', 'items', 'values', 'foo') -> True
    assert has_any_callables(org, 'get', 'keys', 'items', 'values', 'foo') is True

    # has_any_callables(org, 'keys', 'values', 'items', 'pop') -> True
    assert has_any_callables(org, 'keys', 'values', 'items', 'pop') is True

    # has_any_callables(org, 'get', 'setdefault', 'pop') -> True
    assert has_any_callables(org, 'get', 'setdefault', 'pop') is True

    # has_any_callables(org, 'get', 'has_key