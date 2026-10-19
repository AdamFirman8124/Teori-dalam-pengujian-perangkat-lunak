

# Generated at 2022-06-13 20:43:21.955226
# Unit test for function has_any_attrs
def test_has_any_attrs():
    # Check a dictionary
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_attrs(dict(), 'foo', 'bar') is False

    # Check a list
    assert has_any_attrs([], 'append', 'reverse', 'insert', 'foo') is True
    assert has_any_attrs([], 'foo', 'bar') is False

    # Check a class
    class TestClass:
        def append(self):
            pass
        def get(self):
            pass
    assert has_any_attrs(TestClass(), 'append', 'reverse', 'insert', 'foo') is True
    assert has_any_attrs(TestClass(), 'foo', 'bar') is False

# Generated at 2022-06-13 20:43:29.145321
# Unit test for function has_callables
def test_has_callables():
    print("test_has_callables: ", end='')
    assert has_callables(dict(),'get','keys','items','values') == True
    assert has_callables(dict(),'get','keys','items','values','foo') == False
    assert has_callables(dict(),'foo') == False
    print("complete")

# Generated at 2022-06-13 20:43:35.026508
# Unit test for function has_callables
def test_has_callables():
    from flutils import objutils
    from collections import OrderedDict
    dict = OrderedDict()
    dict['foo'] = 0
    dict['bar'] = 1
    dict['qux'] = 2
    result = objutils.has_callables(dict, 'keys', 'values', 'items')
    assert result == True


# Generated at 2022-06-13 20:43:39.166065
# Unit test for function has_any_attrs
def test_has_any_attrs():
   obj = {'key': 'value'}
   assert has_any_attrs(obj,'get','keys','items','values','something') == True


# Generated at 2022-06-13 20:43:44.139943
# Unit test for function has_any_callables
def test_has_any_callables():
    print('Test function has_any_callables')
    print('- Test with a dict')
    obj = dict()
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'something') is True
    print('- Test with a set')
    obj = set()
    assert has_any_callables(obj, 'add', 'remove') is True

# Generated at 2022-06-13 20:43:51.693074
# Unit test for function has_any_callables
def test_has_any_callables():
    dict
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert not has_any_callables(dict(),'get','keys','items','values','foo','log')
    assert has_any_callables(dict(),'log','keys','items','values','foo','log')
    assert not has_any_callables(dict(),'','keys','items','values','foo','log')


# Generated at 2022-06-13 20:43:54.366873
# Unit test for function has_any_callables
def test_has_any_callables():
    # Setup
    obj = dict(a=1, b=2)
    correct = True

    # Exercise
    result = has_any_callables(obj, 'keys', 'values', 'foo')

    # Verify
    assert result == correct

# Generated at 2022-06-13 20:43:59.201139
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import Counter

    from flutils.objutils import has_any_callables
    assert has_any_callables(Counter(a=1, b=2, c=2), 'most_common', 'keys') is True
    assert has_any_callables(Counter(a=1, b=2, c=2), 'keys') is False
    assert has_any_callables(Counter(a=1, b=2, c=2), 'keys', 'foo') is False


# Generated at 2022-06-13 20:44:01.027949
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:44:10.514202
# Unit test for function has_any_callables
def test_has_any_callables():
    result = has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert result == True
    result = has_any_callables(dict(), 'get', 'keys', 'items', 'values', '__doc__')
    assert result == True
    result = has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert result == True
    result = has_any_callables(dict(), 'foo', 'bar', 'baz', 'qux')
    assert result == False



# Generated at 2022-06-13 20:44:26.241002
# Unit test for function has_any_callables
def test_has_any_callables():
    """test_has_any_callables()"""
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:44:28.522831
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(str, 'join')



# Generated at 2022-06-13 20:44:35.657647
# Unit test for function has_callables
def test_has_callables():
    import os
    assert has_callables(os, 'path', 'sep', 'foo') is True  # Exists and callable
    assert has_callables(os, 'path', 'sep', 'foo', 'bar') is False  # One is not callable
    assert has_callables(os, 'path', 'sep', 'foo', 'bar', 'baz') is False  # One is not callable
    assert has_callables(os, 'bar') is False  # None exist
    assert has_callables(os, 'bar', 'baz') is False  # None exist
    assert has_callables(os, 'bar', 'baz', 'qux') is False  # None exist


# Generated at 2022-06-13 20:44:39.547842
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')
    assert not has_callables(dict(),'get','keys','items','values','foo')


# Generated at 2022-06-13 20:44:49.198309
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables."""
    import unittest
    import os

    class TestHasAnyCallablesMethods(unittest.TestCase):
        obj = dict(a=1, b=2, c=3)

        def test_does_not_exist(self):
            self.assertFalse(
                has_any_callables(
                    self.obj,
                    'popitem',
                    'foo',
                    'bar',
                    'baz'
                )
            )

        def test_does_exist(self):
            self.assertTrue(
                has_any_callables(
                    self.obj,
                    'popitem',
                    'foo',
                    'bar',
                    'update'
                )
            )


# Generated at 2022-06-13 20:44:55.523945
# Unit test for function has_any_callables
def test_has_any_callables():
    def foo(): pass
    obj = dict(a=1, b=2, foo=foo)

    assert has_any_callables(obj, 'foo', 'bar') is True
    assert has_any_callables(obj, 'bar', 'something') is False



# Generated at 2022-06-13 20:45:00.809249
# Unit test for function has_any_callables
def test_has_any_callables():
    print('Testing function has_any_callables...')
    assert has_any_callables(dict(),'get','keys','items','values','something')
    assert has_any_callables(dict(),'get','keys','items','values','foo')

    # Unit test for function has_attrs

# Generated at 2022-06-13 20:45:07.515678
# Unit test for function has_callables
def test_has_callables():
    obj = dict
    attrs = 'get', 'keys', 'items', 'values'
    assert has_callables(obj, *attrs) is True

    obj = 'bongo'
    attrs = 'get', 'keys', 'items', 'values'
    assert has_callables(obj, *attrs) is False



# Generated at 2022-06-13 20:45:12.095888
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function ``has_any_callables``."""
    assert has_any_callables(dict(), 'items', 'keys', 'get', 'values') is True
    assert has_any_callables(object(), 'items', 'keys', 'get', 'values') is False



# Generated at 2022-06-13 20:45:20.420051
# Unit test for function has_callables
def test_has_callables():
    input_dict = dict(a=1, b=2, c=3)
    assert has_callables(input_dict, 'get', 'keys', 'items', 'values') is True
    assert has_callables(input_dict, 'get', 'keys', 'items') is True
    assert has_callables(input_dict, 'get', 'keys') is True
    assert has_callables(input_dict, 'keys') is True
    assert has_callables(input_dict, 'get') is True
    assert has_callables(input_dict, 'get', 'keys', 'values', 'foo') is False
    assert has_callables(input_dict, 'foo') is False
    assert has_callables(input_dict, 'keys', 'foo') is False

# Generated at 2022-06-13 20:45:26.892358
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:45:29.168881
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:45:42.376543
# Unit test for function has_callables
def test_has_callables():
    import inspect
    import operator
    class X(object):
        def __lt__(self, other):
            return True
        def __lt__(self):
            return True
        def __add__(self, other):
            return True
        def __and__(self, other):
            return True
        def __call__(self, *args, **kwargs):
            return True
        def __coerce__(self, other):
            return (True, True)
        def __complex__(self):
            return 1j
        def __contains__(self, other):
            return True
        def __delattr__(self, name):
            return True
        def __delitem__(self, key):
            return True
        def __dir__(self):
            return True

# Generated at 2022-06-13 20:45:52.787103
# Unit test for function has_callables
def test_has_callables():
    """Test the function has_callables.
    """
    import collections.abc
    import collections
    import pytest

    obj = dict(a=1, b=2)
    attrs_true = dict(
        get='get', keys='keys', items='items', values='values',
        iterkeys='keys', iteritems='items', itervalues='values'
    )
    attrs_false = dict(
        get='no_such_thing', keys='no_such_thing', items='no_such_thing',
        values='no_such_thing'
    )

    assert isinstance(obj.keys(), collections.abc.KeysView)
    assert isinstance(obj.values(), collections.abc.ValuesView)
    assert isinstance(obj.items(), collections.abc.ItemsView)

# Generated at 2022-06-13 20:46:01.053117
# Unit test for function has_callables
def test_has_callables():
    assert not has_callables(dict(), 'foo')
    assert has_callables(dict(), 'get')
    assert has_callables(dict(), 'get', 'foo')
    assert has_callables(dict(), 'get', 'foo', 'bar')
    assert has_callables(dict(), 'foo', 'get')
    assert has_callables(dict(), 'foo', 'bar', 'get')


# Generated at 2022-06-13 20:46:08.029892
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables({'get': 'get'}, 'get', 'keys', 'items', 'values') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'something') is False
    assert has_callables(dict(), 'get', 'foo') is False


# Generated at 2022-06-13 20:46:20.921752
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import Counter
    from collections.abc import Iterator
    from functools import partial
    from typing import (
        Any,
        Callable,
        Dict,
        Iterable,
        List,
        Mapping,
        MutableMapping,
        Optional,
        Sequence,
        Tuple,
    )

    def test_func(obj: Any) -> bool:
        attrs = ('keys', 'values', 'items', 'get', '__setitem__')
        return has_any_callables(obj, *attrs)

    dict_ = dict(a=1, b=2, c=[1, 2, 3])
    assert test_func(dict_) is True
    assert test_func(dict_.keys()) is False
    assert test_func(dict_.values()) is False
    assert test_func

# Generated at 2022-06-13 20:46:32.865933
# Unit test for function has_any_callables
def test_has_any_callables():
    # Test if we can find any of the given attributes and are callable
    from collections import defaultdict
    from collections.abc import Mapping

    dd = defaultdict(str)
    callables = ('__missing__', '__getitem__')
    # dd contains __missing__ and __getitem__
    assert has_any_callables(dd, *callables) is True
    # dd is an instance of Mapping and Mapping has get and items
    assert has_any_callables(dd, 'get', 'items') is True
    # dd is an instance of Mapping and Mapping has get, keys, and items
    assert has_any_callables(dd, 'get', 'keys', 'items') is True
    # dd is an instance of Mapping and Mapping has has_any_callables, keys, and
    # items

# Generated at 2022-06-13 20:46:42.641593
# Unit test for function has_any_callables
def test_has_any_callables():
    test_obj = {
        'foo' : 'bar',
        'baz' : 1,
    }
    assert has_any_callables(test_obj, 'foo', 'baz') is False
    assert has_callables(test_obj, 'foo', 'baz') is False
    assert has_any_attrs(test_obj, 'foo', 'baz') is True
    assert has_attrs(test_obj, 'foo', 'baz') is True

# Generated at 2022-06-13 20:46:48.980463
# Unit test for function has_callables
def test_has_callables():
    class Dummy:
        def a(self):
            pass

        def b(self):
            pass

    d = Dummy()
    assert has_callables(d, 'a', 'b') == True
    assert has_callables(d, 'a') == True
    assert has_callables(d, 'b') == True
    assert has_callables(d, 'c') == False
    assert has_callables(d, 'a', 'c') == False
    assert has_callables(d, 'a', 'b', 'c') == False
    assert has_callables(d, 'c', 'a', 'b') == False



# Generated at 2022-06-13 20:47:04.986142
# Unit test for function has_callables
def test_has_callables():
    """Unit test for function has_callables"""
    import unittest
    import os
    import sys
    import shutil
    import flutils.logutils as lu

    logger = lu.logjson()

    class Test(unittest.TestCase):
        """Class for unit testing"""

        def setUp(self):
            """Setup"""
            self.tmp = tempfile.mkdtemp()
            lu.set_stream_handler(level='debug')
            lu.set_file_handler(
                filename=os.path.join(self.tmp, 'has_callables.json'),
                level='debug')

        def tearDown(self):
            """Tear Down"""
            lu.disable_stream_handler()
            lu.disable_file_handler()

# Generated at 2022-06-13 20:47:11.273728
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables('S', 'upper', 'lower', 'split') == True
    assert has_any_callables('S', 'upper', 'lower', 'split','something') == True
    assert has_any_callables('S', 'uni', 'lower', 'split') == False
    assert has_any_callables([1,2,3], 'upper', 'lower', 'split') == False


# Generated at 2022-06-13 20:47:19.529210
# Unit test for function has_any_callables
def test_has_any_callables():
    # True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    # False
    assert has_any_callables(dict(), 'get', 'foo', 'items', 'values', 'bar') == False
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'bar', 'baz') == False


# Generated at 2022-06-13 20:47:28.617067
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'bar') is False
    assert has_callables(dict(), 'get', 'key', 'item', 'value') is False
    assert has_callables(dict(), 'foo', 'key', 'item', 'value') is False


# Generated at 2022-06-13 20:47:39.230883
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'get')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'keys')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'items')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'values')


# Generated at 2022-06-13 20:47:43.582052
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(),'get','keys','items','values',)
    assert not has_any_callables(dict(), 'foo',)


# Generated at 2022-06-13 20:47:48.358265
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:47:51.677950
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_callables(dict(), 'something', 'keys', 'items', 'values')


# Generated at 2022-06-13 20:47:56.179122
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(),'keys','something') is True
    assert has_any_callables(dict(),'keys','something','is_subclass_of_any') is False


# Generated at 2022-06-13 20:48:06.877985
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert(has_callables(obj,'keys','items'))
    assert(has_callables(obj.keys(),'__contains__'))
    assert(has_callables(obj.values(),'__contains__'))

# Generated at 2022-06-13 20:48:21.735316
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_any_callables(dict(), 'foo', 'bar', 'baz')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(dict(), 'foo', 'bar', 'baz', 'something')
    d = {'foo': 'bar'}
    assert has_any_callables(d, 'get', 'keys', 'items', 'values')
    assert not has_any_callables(d, 'foo', 'bar', 'baz')
    assert has_any_callables(d, 'get', 'keys', 'items', 'values', 'foo')

# Generated at 2022-06-13 20:48:24.918679
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:48:34.819488
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    from types import SimpleNamespace
    obj = SimpleNamespace()
    assert has_any_callables(obj, 'foo', 'bar', 'baz') is False
    obj.foo = lambda: None
    assert has_any_callables(obj, 'foo', 'bar', 'baz') is True
    obj.bar = lambda: None
    assert has_any_callables(obj, 'foo', 'bar', 'baz') is True
    obj.baz = lambda: None
    assert has_any_callables(obj, 'foo', 'bar', 'baz') is True
    obj.foo = None
    assert has_any_callables(obj, 'foo', 'bar', 'baz') is True
    obj.bar = None
    assert has_any_

# Generated at 2022-06-13 20:48:41.983334
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit tests for function has_any_callables"""
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(dict(), 'foo', 'bar', 'baz', 'bletch')



# Generated at 2022-06-13 20:48:52.081865
# Unit test for function has_any_callables
def test_has_any_callables():
    for s in (list, dict, tuple, set, frozenset, builtins.range):
        assert has_any_callables(s, 'start', 'stop', 'step') is True
    assert has_any_callables(s, 'start', 'stop', 'step', 'foo') is False
    assert has_any_callables(s, 'start', 'stop', 'foo') is False
    assert has_any_callables(s, 'start', 'foo') is False
    assert has_any_callables(s, 'foo') is False


# Generated at 2022-06-13 20:48:55.117988
# Unit test for function has_any_callables
def test_has_any_callables():
    obj_dict = dict({"yes": "this", "no": "that"})
    assert has_any_callables(obj_dict, *{"get", "keys", "items", "values", "something"})


# Generated at 2022-06-13 20:49:03.587850
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(list(),'get','keys','items','values','foo')
    assert has_any_callables(set(),'get','keys','items','values','foo')
    assert has_any_callables(frozenset(),'get','keys','items','values','foo')
    assert has_any_callables(tuple(),'get','keys','items','values','foo')
    assert has_any_callables(deque(),'get','keys','items','values','foo')
    assert has_any_callables(Filter(lambda x: x == 'a', 'abcd'),'get','keys','items','values','foo')

# Generated at 2022-06-13 20:49:10.956548
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = []
    result = has_any_callables(obj, 'append', 'insert')
    # if result is correct
    assert result == True
    # if it works if the object doesn't have that attribute
    obj = 12345
    result = has_any_callables(obj, 'append', 'insert')
    assert result == False
    # if it works if the attribute is not callable
    obj = []
    result = has_any_callables(obj, 'append', 'insert', 'clear')
    assert result == False



# Generated at 2022-06-13 20:49:18.801519
# Unit test for function has_callables
def test_has_callables():
    assert not has_callables({}, 'get')
    assert has_callables({}, 'get', 'keys')
    assert has_callables({}, 'get', 'keys', 'items')
    assert has_callables({1:"a", 2:"b"}, 'get', 'keys', 'items')
    assert has_callables([1,2,3], 'append', 'count')
    assert has_callables(dict(a=1,b=2,c=3), 'get', 'keys')
    assert has_callables(dict(a=1,b=2,c=3), 'pop', 'popitem', 'update')


# Generated at 2022-06-13 20:49:21.903363
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(list(), 'pop', 'append') == True
    assert has_callables(dict(), 'pop', 'keys') == False

#Unit test for function has_any_callables

# Generated at 2022-06-13 20:49:35.898252
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:49:45.108032
# Unit test for function has_callables
def test_has_callables():
    # noinspection PyCompatibility
    from collections import UserDict
    assert has_callables(
        dict(),
        'get',
        'keys',
        'items',
        'values',
    ) is True
    assert has_callables(
        UserDict(),
        'get',
        'keys',
        'items',
        'values',
    ) is True
    assert has_callables(
        dict(),
        'get',
        'keys',
        'items',
        'values',
        'something',
    ) is False
    assert has_callables(
        UserDict(),
        'get',
        'keys',
        'items',
        'values',
        'something',
    ) is False



# Generated at 2022-06-13 20:49:52.096321
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = {'foo': lambda x: x}
    assert has_any_callables(obj, 'bar', 'foo') is True, (
        'has_any_callables() returned False, expected True'
    )
    assert has_any_callables(obj, 'bar', 'baz') is False, (
        'has_any_callables() returned True, expected False'
    )



# Generated at 2022-06-13 20:49:55.568195
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'values', 'items', 'pop') is True



# Generated at 2022-06-13 20:50:06.538177
# Unit test for function has_callables
def test_has_callables():
    import unittest

    class Foo:
        def __init__(self):
            self.a = 1
            self.b = 2

        @staticmethod
        def foo():
            pass

        @classmethod
        def bar(cls):
            pass

    class Bar(Foo):
        pass

    class TestHasCallables(unittest.TestCase):
        def test_has_callables(self):
            self.assertTrue(has_callables(Foo, 'foo', 'bar'))
            self.assertTrue(has_callables(Bar, 'foo', 'bar'))

    unittest.main()


# Generated at 2022-06-13 20:50:18.556186
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables('', 'capitalize', '__getitem__') is True
    assert has_any_callables('', 'capitalize', '__setitem__') is True
    assert has_any_callables((1, 2, 3), '__add__', '__contains__') is True
    assert has_any_callables((1, 2, 3), '__add__', '__copy__') is True
    assert has_any_callables((1, 2, 3, 4), '__add__', '__contains__') is True
    assert has_any_callables((1, 2, 3, 4), '__add__', '__copy__') is True
    assert has_any_callables(dict(a=1), 'items') is True

# Generated at 2022-06-13 20:50:20.380188
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')

# Generated at 2022-06-13 20:50:29.761402
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','values') == True
    assert has_callables(dict(),'get','keys','values','foo') == True
    assert has_callables(dict(),'get','keys','values','foo','bar') == False
    assert has_callables(str(),'upper') == True
    assert has_callables(str(),'upper','lower') == True
    assert has_callables(str(),'upper','lower','title') == False
    assert has_callables(tuple(),'index') == True
    assert has_callables(tuple(),'index','count') == True
    assert has_callables(tuple(),'index','count','foo') == False
    assert has_callables(int(),'real','imag') == True

# Generated at 2022-06-13 20:50:37.437040
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    dict_obj = dict(a=1, b=2)
    assert has_any_callables(dict_obj, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict_obj, 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict_obj, 'foo', 'bar', 'baz', 'bam') is False
    assert has_any_callables(dict_obj, 'foo') is False


# Generated at 2022-06-13 20:50:41.504715
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values') == True
    assert has_any_callables(dict(),'foo','keys','items','values') == False


# Generated at 2022-06-13 20:51:04.806289
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import (
        Class,
        has_any_callables,
    )

    class Foo(Class):
        def __init__(self, foo: str = 'foo', bar: str = 'bar'):
            super().__init__()
            self._foo = foo
            self._bar = bar

        def foo(self) -> str:
            return self._foo

        def bar(self) -> str:
            return self._bar

    foo = Foo()
    assert has_any_callables(foo, 'foo', 'bar') is True
    assert has_any_callables(foo, 'foo', 'bar_missing') is True

    assert has_any_callables(foo, 'foobar', 'bar_missing') is False



# Generated at 2022-06-13 20:51:11.658869
# Unit test for function has_callables
def test_has_callables():
    # Test has_callables
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') == True
    # Test has_callables with an object that doesn't have all of the given
    # attributes
    assert has_callables(dict(), 'get', 'keys', 'items', 'foo') == False
    # Test has_callables with an object that has all of the given attributes,
    # but none are callable
    class MyClass(object):
        def __init__(self):
            self.foo = 'bar'
    assert has_callables(MyClass(), 'foo') == False


# Generated at 2022-06-13 20:51:19.787915
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict, 'get', 'keys', 'items', 'values')
    assert not has_callables(dict, '__really_not_a_thing__', '__really_not_a_thing__')
    assert not has_callables(dict(), '__really_not_a_thing__', '__really_not_a_thing__')
    assert has_callables(dict(), '__contains__', 'items', 'values')
    assert has_callables(dict, '__contains__', 'items', 'values')
    assert has_callables(list, 'copy', 'append', 'extend', 'clear', 'pop', 'index', 'insert', 'remove', 'reverse', 'sort')
    assert not has

# Generated at 2022-06-13 20:51:21.863706
# Unit test for function has_any_callables
def test_has_any_callables():
    assert callable(has_any_callables)



# Generated at 2022-06-13 20:51:23.950519
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')==True



# Generated at 2022-06-13 20:51:27.150147
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(set(), 'add', 'discard', 'pop')
    assert not has_callables(str(), 'find', 'index', 'join', 'rfind')



# Generated at 2022-06-13 20:51:34.970724
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'values') == True
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'this', 'values') == False
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'this', 'that', 'values') == False


# Generated at 2022-06-13 20:51:42.974935
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import (
        UserDict,
        UserList,
        UserString,
    )
    from typing import (
        Any as _Any,
        Callable as _Callable,
        Union as _Union,
    )
    func: _Callable[[int], int] = lambda x: x
    obj: _Union[
            _Callable[[int], int],
            UserDict,
            UserList,
            UserString,
            dict,
            float,
            int,
            list,
            str,
    ]

# Generated at 2022-06-13 20:51:51.656996
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True, \
        'has_callables: Failed to validate that a `dict` has all the' \
           ' specified attributes and are callable.'
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False, \
        'has_callables: Failed to validate that a `dict` does not have all' \
           ' the specified attributes.'


# Generated at 2022-06-13 20:52:02.293032
# Unit test for function has_callables
def test_has_callables():
    # obj is int
    obj = 1
    assert has_callables(obj,'real') == False

    # obj is str
    obj = 'Hello World'
    assert has_callables(obj, 'split') == False

    # obj is dict
    obj = dict(a=1)
    assert has_callables(obj, 'item','values','keys') == False

    # obj is list
    obj = [1,2,3,4]
    assert has_callables(obj, 'append', 'extend') == True

    # obj is OrderedDict
    obj = OrderedDict(a=1)
    assert has_callables(obj, 'item','values','keys') == True

