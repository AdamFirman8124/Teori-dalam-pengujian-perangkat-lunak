

# Generated at 2022-06-13 20:43:13.289168
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'keys', 'values', 'get')
    assert has_any_callables(obj, 'keys', 'values', 'foo')
    assert has_any_callables(obj, 'keys', 'foo', 'bar')
    assert not has_any_callables(obj, 'keys', 'foo', 'bar', 'baz')

# Generated at 2022-06-13 20:43:20.464219
# Unit test for function has_any_callables
def test_has_any_callables():
    '''test for has_any_callables'''
    mydict = dict(a=1, b=2)
    assert has_any_callables(mydict, 'get', 'keys', 'items', 'values')
    assert not has_any_callables(mydict, 'does_not_exist')
    assert has_any_callables(mydict, 'does_not_exist', 'get')


# Generated at 2022-06-13 20:43:22.905796
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:43:26.051820
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(str,'__str__','capitalize','upper')



# Generated at 2022-06-13 20:43:30.580125
# Unit test for function has_attrs
def test_has_attrs():
    ''' Test that function has_attrs works correctly.
    '''
    # Test in case of error
    assert has_attrs(None, 'foo') == False
    # Test in case correct
    assert has_attrs(dict(), 'get', 'keys', 'items', 'values') == True


# Generated at 2022-06-13 20:43:36.738836
# Unit test for function has_any_attrs
def test_has_any_attrs():
    try:
        obj = dict()
        assert has_any_attrs(obj, 'get', 'keys', 'items', 'values',
                             'something') is True
    except AssertionError:
        print("Incorrect result")
    except Exception as e:
        print("Incorrect result")
        print(repr(e))


# Generated at 2022-06-13 20:43:39.457556
# Unit test for function has_any_attrs
def test_has_any_attrs():
    from flutils.objutils import has_any_attrs
    obj = dict(a=1, b=2)
    assert has_any_attrs(obj, 'update', 'clear')



# Generated at 2022-06-13 20:43:41.638922
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:43:44.174718
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'foo', 'bar') is False



# Generated at 2022-06-13 20:43:46.831057
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(),'get','keys','items','values','something')


# Generated at 2022-06-13 20:43:55.653440
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'foo','bar','baz') == False


# Generated at 2022-06-13 20:44:01.546790
# Unit test for function has_callables
def test_has_callables():
    from flutils.objutils import has_callables

    obj = {'a':1, 'b':2}
    assert has_callables(obj, 'get', 'keys') == True
    assert has_callables(obj, 'get', 'keys', 'foo') == False
    assert has_callables(obj, 'foo', 'bar') == False


# Generated at 2022-06-13 20:44:06.252265
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True
    assert has_any_callables(dict(), 'foo', 'bar', 'baz', 'bat') == False


# Generated at 2022-06-13 20:44:09.702810
# Unit test for function has_callables
def test_has_callables():
   #assert has_callables(dict(),'get','keys','items','values') == True
   assert has_callables(dict(),'get','keys','items','values') == True


# Generated at 2022-06-13 20:44:15.189493
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    test_dict = dict(a=1, b=2, c=3)
    assert has_any_callables(test_dict, 'keys', 'items', 'values', 'get')
    return True



# Generated at 2022-06-13 20:44:16.370619
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    

# Generated at 2022-06-13 20:44:25.359310
# Unit test for function has_callables
def test_has_callables():
    # Test expected successes
    assert has_callables(str, 'strip') == True
    assert has_callables(dict, 'get', 'keys', 'items', 'values') == True

    # Test expected failures
    assert has_callables(dict, 'get', 'foobar', 'items', 'values') == False
    assert has_callables(dict, 'get', 'keys', 'foobar', 'values') == False
    assert has_callables(dict, 'get', 'keys', 'items', 'foobar') == False
    assert has_callables(str, 'foobar') == False

    # Test unexpected successes and failures
    assert has_callables(dict, 'Foobar', 'get', 'keys', 'items') == False



# Generated at 2022-06-13 20:44:29.852241
# Unit test for function has_callables
def test_has_callables():
    func = dict(a=1, b=2, c=3).__class__
    assert has_callables(func, 'get', 'keys', 'items') == True



# Generated at 2022-06-13 20:44:36.847221
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict(), 'values', 'keys', 'items', 'get')
    assert has_callables(dict(), 'keys', 'keys', 'items', 'get')
    assert has_callables(dict(), 'get', 'get', 'items', 'items')
    assert not has_callables(dict(), 'get', 'keys', 'items', 'bar')
    assert not has_callables(dict(), 'foo', 'keys', 'items', 'bar')


# Unit tests for function has_attrs

# Generated at 2022-06-13 20:44:46.968725
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import UserList, UserDict, UserString
    from collections.abc import ValuesView, KeysView, MutableSequence
    from flutils.objutils import has_any_callables
    assert has_any_callables(UserList, 'append', 'extend') is True
    assert has_any_callables(UserDict, '__setitem__', 'update') is True
    assert has_any_callables(UserString, '__add__', 'capitalize') is True
    assert has_any_callables(ValuesView, 'pop', 'remove') is True
    assert has_any_callables(KeysView, 'popitem', 'remove') is True
    assert has_any_callables(MutableSequence, 'insert', 'pop') is True



# Generated at 2022-06-13 20:44:54.671219
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get','keys','items','values') == True
    assert has_callables(dict(), 'get','keys','items','foo') == False


# Generated at 2022-06-13 20:45:00.442784
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'something') is False


# Generated at 2022-06-13 20:45:09.884546
# Unit test for function has_callables
def test_has_callables():
    class A(dict):

        def get(self): return True

        def keys(self): return True

        def items(self): return True

        def values(self): return True

    assert has_callables(dict(),'get','keys','items','values') == True
    assert has_callables(dict(),'get','keys','items','values','foo') == True
    assert has_callables(A() ,'get','keys','items','values') == True
    assert has_callables(A() ,'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:45:14.191963
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')


# Generated at 2022-06-13 20:45:17.088064
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert not has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')


# Generated at 2022-06-13 20:45:26.209556
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test the function has_any_callables."""
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(obj, 'get', 'foo', 'bar', 'baz') is True
    assert has_any_callables(obj, 'foo', 'bar', 'baz', 'buz') is False
    return True



# Generated at 2022-06-13 20:45:39.258907
# Unit test for function has_any_callables
def test_has_any_callables():
    """
    :author:
        Joel Hedlund <joel.hedlund@iki.fi>
    :copyright:
        Copyright (c) 2020, Joel Hedlund.
    :license:
        MIT
    """
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_any_callables(sorted([1, 2, 3]), 'get', 'keys', 'items', 'values')
    assert has_any_callables(iter([1, 2, 3]), '__iter__', '__next__', 'get') is False
    assert has_any_callables([1, 2, 3], '__iter__', '__next__', 'get') is False
    assert has_any_callables(None, '__iter__', '__next__', 'get') is False



# Generated at 2022-06-13 20:45:46.279639
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1, b=2)
    assert has_any_callables(d, 'get', 'keys', 'values') is True
    assert has_any_callables(d, 'get', 'keys', 'values', 'foo') is True
    assert has_any_callables(d, 'keys', 'values', 'foo') is True



# Generated at 2022-06-13 20:45:58.393427
# Unit test for function has_callables
def test_has_callables():
    """Test has_callables."""

# Generated at 2022-06-13 20:46:09.737803
# Unit test for function has_callables
def test_has_callables():

    import re

    from more_itertools import collapse

    from flutils.objutils import has_callables
    from flutils.strutils import is_upper

    _example = [
        'a', 'b', 'c',
        ['d', 'e', 'f', 'g'],
        ['h', 'i', 'j', 'k'],
        ['l', 'm', 'n', 'o', ['p', 'q', 'r', 's']],
        't', 'u', 'v',
        [
            'w',
            ['x', 'y', 'Z'],
            'z'
        ]]

    # Check that iterables are not a list.
    # Check that the callables exist, return a list.
    # Check that the callables are not iterable.

# Generated at 2022-06-13 20:46:18.801104
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    attrs = ['get', 'keys', 'items', 'values']
    # print(f'has_callables(obj, *attrs): {has_callables(obj, *attrs)}')
    # assert has_callables(obj, *attrs) == True
    assert has_callables(obj, *attrs) is True


# Generated at 2022-06-13 20:46:20.382936
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:46:32.664045
# Unit test for function has_callables
def test_has_callables():
    import pytest

# Generated at 2022-06-13 20:46:46.312124
# Unit test for function has_any_callables
def test_has_any_callables():
    assert not has_any_callables('hello', '__add__')
    assert has_any_callables([], '__add__', '__iter__')
    assert not has_any_callables([], '__add__', '__iter__', '__foo__')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'something')
    assert not has_any_callables(dict(), 'something')
    assert has_any_callables((1,), '__add__', '__iter__', '__len__')
    assert not has_any_callables((1,), '__add__', '__iter__', '__len__', '__foo__')
    assert has_any_callables([1, 2], '__add__', '__iter__', '__len__')

# Generated at 2022-06-13 20:46:53.207292
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'values', 'keys') is True
    assert has_any_callables(obj, 'get', 'foo', 'keys') is True
    assert has_any_callables(obj, 'foo', 'bar') is False


# Generated at 2022-06-13 20:46:56.087287
# Unit test for function has_callables
def test_has_callables():
    assert has_callables([], "get", "keys", "items", "values")



# Generated at 2022-06-13 20:47:00.893299
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'_get','_keys','_items','_values','_foo') == False


# Generated at 2022-06-13 20:47:11.247474
# Unit test for function has_any_callables
def test_has_any_callables():
    # setup
    test_data = (
        ('a', 'b', 'c', False),
        ('a', 'b', 'c', True),
        ('a', 'b', 'c', 'd', True),
        ('a', 'b', 'c', 'd', False),
        ('a', 'b', 'c', 'd', True, False),
        ('a', 'b', 'c', 'd', False, True),
        ('a', 'b', 'c', 'd', True, True),
        ('a', 'b', 'c', 'd', False, False),
    )
    expected_results = (
        False,
        True,
        True,
        False,
        True,
        True,
        True,
        False,
    )
    # run tests

# Generated at 2022-06-13 20:47:19.823707
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    from flutils.objutils import has_callables
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True
    assert has_any_callables(dict(),'foo','bar','baz','qux','quux') == False
    assert has_callables(dict(),'get','keys','items','values') == True
    assert has_callables(dict(),'foo','bar','baz','qux','quux') == False


# Generated at 2022-06-13 20:47:30.323335
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is False
    assert has_callables(dict(), 'fromkeys') is False
    assert has_callables(dict(), 'get', 'fromkeys', 'keys', 'items', 'values') is False  # noqa
    assert has_callables(dict(a=1, b=2), 'get', 'fromkeys', 'keys', 'items', 'values') is True  # noqa



# Generated at 2022-06-13 20:47:38.651208
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something')
    assert has_any_callables(UserList(),'append','extend','insert','pop')
    assert has_any_callables(UserDict(),'clear','copy','pop','popitem','setdefault')

# Generated at 2022-06-13 20:47:47.621263
# Unit test for function has_any_callables
def test_has_any_callables():
    # Test get method of a dict is callable
    d = dict()
    assert has_any_callables(d, 'get')
    # Test keys method of a dict is callable
    d = dict()
    assert has_any_callables(d, 'keys')
    # Test items method of a dict is callable
    d = dict()
    assert has_any_callables(d, 'items')
    # Test values method of a dict is callable
    d = dict()
    assert has_any_callables(d, 'values')
    # Test something that is not a method
    d = dict()
    assert has_any_callables(d, 'something')

# Generated at 2022-06-13 20:47:53.281175
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:47:59.644296
# Unit test for function has_any_callables
def test_has_any_callables():
    import pytest
    # Tests expected to return True
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items')
    assert has_any_callables(dict(), 'items', 'foo')
    # Tests expected to return False
    assert not has_any_callables(dict(), 'foo', 'bar')
    assert not has_any_callables(dict(), 'foo')


# Generated at 2022-06-13 20:48:01.852434
# Unit test for function has_callables
def test_has_callables():
    import unittest
    class TestComponents(unittest.TestCase):
        def test_has_callables(self):
            assert has_callables(dict(),'get','keys','items','values')


# Generated at 2022-06-13 20:48:11.473255
# Unit test for function has_any_callables
def test_has_any_callables():
    print('Checking if has_any_callables passes')
    assert has_any_callables([], 'append','pop','foo','bar','__len__','__init__','__iter__') is True
    assert has_any_callables(tuple(), 'count','index','__len__','__contains__','__getitem__','__setitem__') is True
    assert has_any_callables({}, 'get','keys','items','values','__repr__','__setitem__') is True
    assert has_any_callables(range(5), 'count','index','__len__','__iter__','__getitem__','__setitem__') is True

# Generated at 2022-06-13 20:48:22.394047
# Unit test for function has_callables
def test_has_callables():
    from flutils.objutils import has_callables
    from collections import ValuesView, KeysView, UserList
    obj = dict(a=1, b=2)
    result = has_callables(obj, '__class__', 'keys', 'values', 'something')
    assert result is True

    result = has_callables(obj.keys(), '__class__', 'keys', 'values', 'something')
    assert result is False

    result = has_callables(obj.keys(), '__class__', 'keys', 'values')
    assert result is True

    result = has_callables(ValuesView, '__class__', 'keys', 'values')
    assert result is True

    result = has_callables(KeysView, '__class__', 'keys', 'values')
    assert result is True

    result = has_callables

# Generated at 2022-06-13 20:48:34.198195
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)

    assert has_callables(obj, 'get')
    assert has_callables(obj, 'get', 'items')
    assert has_callables(
        obj,
        '__contains__',
        '__contains__',
        '__contains__',
        '__contains__',
        '__contains__'
    )
    assert has_callables(obj, '__contains__') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_callables(dict(), 'get', 'keys', 'foo', 'items', 'values') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:48:38.707007
# Unit test for function has_callables
def test_has_callables():
    class A:
        def __init__(self):
            self.test = 'test'
            self.test2 = 'test2'

        def test3(self):
            pass

        @property
        def test4(self):
            return 'test4'

        def test5(self):
            pass

        @classmethod
        def test6(cls):
            pass

        @staticmethod
        def test7():
            pass

    a = A()
    assert has_callables(a, 'test', 'test2', 'test3', 'test4', 'test5', 'test6', 'test7') == True



# Generated at 2022-06-13 20:48:48.356186
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserList,
        UserString,
        defaultdict,
    )
    from decimal import Decimal

    assert has_any_callables(
        dict(), 'get', 'keys', 'items', 'values', 'foo'
    ) is True
    assert has_any_callables(
        dict(), 'get', 'keys', 'items', 'values', 'copy'
    ) is False

    assert has_any_callables(list(), 'get', 'keys', 'items', 'values', 'foo') \
        is False
    assert has_any_callables(list(), 'get', 'keys', 'items', 'values', 'copy') \
        is False


# Generated at 2022-06-13 20:49:02.174594
# Unit test for function has_any_callables
def test_has_any_callables():
    print('Testing has_any_callables...')
    print('obj = dict(a=1, b=2)')
    obj = dict(a=1, b=2)
    print('has_any_callables(obj,\'get\',\'keys\',\'something\')')
    print(has_any_callables(obj, 'get', 'keys', 'something'))
    print('has_any_callables(obj,\'something\')')
    print(has_any_callables(obj, 'something'))
    print('obj = list(dict(a=5, b=6).keys())')
    obj = list(dict(a=5, b=6).keys())
    print('has_any_callables(obj,\'sort\',\'index\',\'append\')')

# Generated at 2022-06-13 20:49:12.227210
# Unit test for function has_callables
def test_has_callables():
    import pytest
    from collections import UserList
    from decimal import Decimal

    obj = UserList()
    assert has_callables(obj, 'append', 'clear')

    obj = UserList((1, 2, 3))
    assert has_callables(obj, 'append', 'clear') is False

    obj = Decimal(1)
    assert has_callables(obj, 'append', 'clear') is False

    obj = Decimal(1)
    assert has_callables(obj, '__add__', '__str__')

    obj = b'foo'
    assert has_callables(obj, '__add__', '__str__') is False

    obj = 'foo'
    assert has_callables(obj, '__add__', '__str__')



# Generated at 2022-06-13 20:49:17.967423
# Unit test for function has_callables
def test_has_callables():
    from collections import defaultdict
    test_obj = defaultdict(int)
    assert has_callables(test_obj, 'get', 'keys', 'items', 'values', 'pop') == True
    assert has_callables(test_obj, 'get', 'keys', 'items', 'values', 'foo', 'pop') == True
    assert has_callables(test_obj, 'get', 'keys', 'items', 'values', 'foo', 'bar', 'pop') == False

# Generated at 2022-06-13 20:49:21.418944
# Unit test for function has_callables
def test_has_callables():
    assert not has_callables(dict(), 'get', 'keys', 'items', 'values', 'abc')
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')


# Generated at 2022-06-13 20:49:25.088454
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    attrs = ['get', 'items', 'keys', 'values']
    assert has_any_callables(obj, *attrs) is True



# Generated at 2022-06-13 20:49:27.770850
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')


# Generated at 2022-06-13 20:49:30.754045
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    result = has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')
    assert (result == True)


# Generated at 2022-06-13 20:49:46.537321
# Unit test for function has_callables
def test_has_callables():
    objs = (
        dict(),
        dict,
        dict().keys,
        dict().keys(),
        dict().values,
        dict().values(),
        dict().items,
        dict().items(),
        dict().fromkeys,
        dict().fromkeys(),
        dict().get,
        dict().get('foo'),
        dict().update,
        dict().update(),
    )

    for obj in objs:
        has_calls = has_callables(
            obj,
            'get',
            'keys',
            'items',
            'values',
            'fromkeys',
            'update',
        )
        if has_calls is True:
            print(
                f"{'PASS' if has_calls else 'FAIL'}: {obj} has all callables"
            )

# Unit test

# Generated at 2022-06-13 20:49:55.905260
# Unit test for function has_callables
def test_has_callables():
    """Test for has_callables.

    Note:
        This test is **not** 'doctest' compatible.
    """
    from flutils.textutils import check_random_samples
    from flutils.objutils import has_callables

    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'something') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'something') is True
    assert has_callables(dict(foo=1), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(foo=1), 'foo', 'keys', 'items', 'values') is True

# Generated at 2022-06-13 20:49:59.711758
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1, b=2)
    has_any_callables(d, 'get', 'values', 'foo')


# Generated at 2022-06-13 20:50:15.989131
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables([1,2,3,4], '__getitem__')
    assert has_any_callables(set([1,2,3,4]), '__iter__')
    assert not has_any_callables({1,2,3,4}, '__add__')
    assert has_any_callables(dict(a=1, b=2), 'get')


# Generated at 2022-06-13 20:50:18.805136
# Unit test for function has_any_callables
def test_has_any_callables():
    import sys
    assert has_any_callables(sys, 'foo', 'stdout', 'exit')
    assert not has_any_callables(sys, 'foo', 'stdin', 'exit')


# Generated at 2022-06-13 20:50:21.261916
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
test_has_callables()


# Generated at 2022-06-13 20:50:30.193658
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables
    """
    result = has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert result is True
    #
    result = has_any_callables(dict(), 'get', 'keys', 'items', 'values', '__hash__')
    assert result is True
    #
    result = has_any_callables(dict(), '__hash__', '__init__', '__setitem__', '__subclasshook__')
    assert result is False
    #
    result = has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert result is True
    #
    result = has_any_callables(dict(), 'get', 'keys', 'items')
    assert result is True


# Generated at 2022-06-13 20:50:39.209600
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit test for function has_any_callables.

    :rtype:
        :obj:`bool`

        * :obj:`True` if the unit tests were successful;
        * :obj:`False` otherwise.
    """
    class Foo:
        def __init__(self, **kwargs):
            self.foo = kwargs.get('foo', None)
            self.bar = kwargs.get('bar', None)

        # noinspection PyUnusedLocal
        def _call(self, *args, **kwargs):
            pass

        def __call__(self, *args, **kwargs):
            pass

    obj = Foo(foo='foo', bar='bar')
    assert has_any_callables(obj, 'bar', 'baz') is True

# Generated at 2022-06-13 20:50:50.260485
# Unit test for function has_any_callables
def test_has_any_callables():
    import operator
    import functools
    import itertools
    import collections
    import copy
    import types

    assert has_attrs(obj={}, attrs='get') is False
    assert has_attrs(obj=dict(), attrs='get') is True

    assert has_callables(obj=dict(), attrs='get') is True
    assert has_callables(obj=dict(), attrs='someattr') is False

# Generated at 2022-06-13 20:50:55.250058
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(dict(),'get','keys','items','values'))
    assert(has_any_callables(dict(),'get','keys','items'))
    assert(has_any_callables(dict(),'keys','values'))
    assert(has_any_callables(dict(),'keys'))
    assert(has_any_callables(dict(),'get'))
    assert(has_any_callables(dict(),'items'))
    assert(has_any_callables(dict(),'values'))
    assert(not has_any_callables(dict(),'foo'))
    assert(not has_any_callables(dict(),'bar'))


# Generated at 2022-06-13 20:50:58.973720
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something')


# Generated at 2022-06-13 20:51:03.070065
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo'))
    assert(has_any_callables(dict(), 'get', 'keys', 'items', 'values'))
    assert(not(has_any_callables(dict(), 'bar', 'foo', 'foobar')))


# Generated at 2022-06-13 20:51:08.878857
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(dict(), 'foo', 'bar')

if __name__ == '__main__':
    test_has_any_callables()

# Generated at 2022-06-13 20:51:37.013661
# Unit test for function has_callables
def test_has_callables():
    """Test for method has_callables"""
    # Extracted from flutils/testutils/test_objutils.py::test_has_callables
    from flutils.objutils import (
        has_callables,
    )

    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'some_attr')
    assert has_callables(dict(), 'get', 'keys', 'items', 'some_attr') is False



# Generated at 2022-06-13 20:51:40.216226
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'keys', 'values', 'items', 'foo')
    assert has_any_callables(obj, dict, str)
    assert not has_any_callables(obj, 'foo', 'bar')



# Generated at 2022-06-13 20:51:53.807276
# Unit test for function has_callables
def test_has_callables():
    from flutils.timeutils import timethis
    from flutils.jsontools import json_encode

    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'items', 'values')
    assert has_callables(obj, 'items', 'values')
    assert has_callables(obj, 'get', 'values')
    assert not has_callables(obj, 'foo', 'bar')

    obj = {'a': 1, 'b': 2}
    def test(obj):
        return isinstance(obj, dict)
    assert has_callables(obj, 'get', 'keys', test)
    assert not has_callables(obj, 'foo', test)


# Generated at 2022-06-13 20:52:04.030142
# Unit test for function has_callables
def test_has_callables():
    # Test with a dictionary
    obj = dict()

# Generated at 2022-06-13 20:52:18.303703
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserString
    )
    from collections.abc import (
        MutableMapping,
        MutableSequence,
        MutableSet,
        Sequence,
        Set,
        Sized,
    )
    from decimal import Decimal
    try:
        from collections.abc import Mapping
    except ImportError:
        from collections import Mapping

    # use a list to test the try/except block

# Generated at 2022-06-13 20:52:32.112409
# Unit test for function has_callables
def test_has_callables():
    a = 100
    b = 'str'
    c = list()
    d = dict()
    e = range(10)
    is_callable_a = has_any_callables(has_attrs, a)
    is_callable_b = has_any_callables(has_attrs, b)
    is_callable_c = has_any_callables(has_attrs, c)
    is_callable_d = has_any_callables(has_attrs, d)
    is_callable_e = has_any_callables(has_attrs, e)
    assert is_callable_a == False
    assert is_callable_b == False
    assert is_callable_c == True
    assert is_callable_d == True
    assert is_callable_e

# Generated at 2022-06-13 20:52:39.429866
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    assert has_any_callables(dict(),'get','keys','items','values','something')
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert not has_any_callables(dict(),'get','keys','items','values','foo', '__builtins__')


# Generated at 2022-06-13 20:52:45.997722
# Unit test for function has_callables
def test_has_callables():
    """
    Unit test for function has_callables.
    """
    import datetime
    now = datetime.datetime.now()
    assert has_callables(now, 'year', 'month', 'day') == True
    assert has_callables(now, 'foo', 'bar') == False
    assert has_callables(None, 'year', 'month', 'day') == False


# Generated at 2022-06-13 20:52:59.113774
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    assert has_any_callables(dict(),'get','keys','items','values')

    assert has_any_callables(dict(),'get','keys','items','values','foo')

    assert not has_any_callables(dict(),'foo','bar')

    assert not has_any_callables(dict(bar=1), 'foo', 'bar')

    assert has_any_callables(dict(foo=lambda: 1), 'foo', 'bar')

    # Test with tuples
    assert not has_any_callables((1, 2, 3), 'foo', 'bar')

    assert has_any_callables((1, lambda: 2, 3), 'foo', 'bar')

    # Test with frozenset

# Generated at 2022-06-13 20:53:05.411065
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1, b=2)
    assert has_any_callables(d, "keys", "items", "values", "get") is True
    assert has_any_callables(d, "keys", "items", "values", "foo") is False
    assert has_any_callables(d, "foo", "bar") is False
    assert has_any_callables(d, "bar") is False
    #  assert has_any_callables(1, "foo", "bar") is False

