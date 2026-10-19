

# Generated at 2022-06-13 20:43:21.312822
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(open, 'read', 'write')
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict, 'fromkeys')
    assert has_callables(dict, 'fromkeys', 'fromkeys')
    assert has_callables(dict, 'fromkeys', 'fromkeys', 'fromkeys')
    assert not has_callables(dict(), 'get', 'keys', 'items', 'values', 'xxx')
    assert not has_callables(dict, 'fromkeys', 'xxx')
    assert not has_callables(dict, 'fromkeys', 'fromkeys', 'xxx')
    assert not has_callables(dict, 'fromkeys', 'fromkeys', 'fromkeys', 'xxx')


# Generated at 2022-06-13 20:43:26.552940
# Unit test for function has_callables
def test_has_callables():
    # type: () -> None
    """
    A family of functions that test has_callables method

    """
    #
    # Given a input
    # When it is a list
    # Then it should return a True
    #
    o = [1,2]
    assert has_callables(o,'__iter__') == True

    #
    # Given a input
    # When it is a dictionary
    # Then it should return a True
    #
    o = {1:2}
    assert has_callables(o,'__iter__') == True

    #
    # Given a input
    # When it is a string
    # Then it should return a True
    #
    o = 'abcdef'
    assert has_callables(o,'__iter__') == True

    #
    # Given a input
    #

# Generated at 2022-06-13 20:43:32.165983
# Unit test for function has_callables
def test_has_callables():
    from flutils.objutils import (
        has_callables
    )
    class Foo():
        def bar():
            pass
    foo = Foo()
    assert has_callables(foo, 'bar') == True
    assert has_callables(foo, 'quz') == False
    assert has_callables(foo, 'bar', 'quz') == False
    assert has_callables(foo, 'bar', 'quz', 'something', 'other') == False


# Generated at 2022-06-13 20:43:39.299976
# Unit test for function has_callables
def test_has_callables():
    "Unit tests for function has_callables"
    class Foo(object):
        def __init__(self, i):
            self.i = i

        def __call__(self, x):
            return self.i + x

    f = Foo(3)

    assert has_callables(f, 'i', '__call__') is True
    assert has_callables(f, 'i', '__call__x') is False
    assert has_callables(f, 'foo', '__call__') is False

# Generated at 2022-06-13 20:43:46.455246
# Unit test for function has_attrs
def test_has_attrs():
    class TestClass:
        def __init__(self):
            self.test1 = "test1"
            self.test2 = "test2"

    test = TestClass()
    # test for actual 
    assert has_attrs(test, 'test1', 'test2') == True
    # test for missing one
    assert has_attrs(test, 'test1', 'test3') == False
    # test for missing both
    assert has_attrs(test, 'test3', 'test4') == False
    # test for not a class
    assert has_attrs('string', 'test1', 'test2') == False
    # test for not a class
    assert has_attrs(None, 'test1', 'test2') == False


# Generated at 2022-06-13 20:43:48.681488
# Unit test for function has_attrs
def test_has_attrs():
    assert has_attrs(deque, "append", "popleft")


# Generated at 2022-06-13 20:43:53.398698
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'values', 'foo') is False


# Generated at 2022-06-13 20:44:00.338019
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values',
                             'foo') is True
    assert has_any_callables(dict(), 'foo', 'bar') is False
    assert has_any_callables(dict(), 'foo', '__getitem__') is True


# Generated at 2022-06-13 20:44:03.259127
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True


# Generated at 2022-06-13 20:44:09.131165
# Unit test for function has_any_callables
def test_has_any_callables():
    import unittest
    import random
    import string

    class DummyClass:
        string = ''.join(random.choices(string.ascii_lowercase, k=8))
        _number = random.randrange(1, 10)

    dummy = DummyClass()

    class HasAnyCallablesTests(unittest.TestCase):
        def test_has_any_callables_false(self):
            self.assertFalse(has_any_callables(dummy, 'string', '_number'))

        def test_has_any_callables_true(self):
            self.assertTrue(has_any_callables(dummy, 'string', '_number'), callable(dummy.string))

# Generated at 2022-06-13 20:44:20.147011
# Unit test for function has_callables
def test_has_callables():
    assert has_callables('hello', 'lower') == True
    assert has_callables('hello', 'lower', 'upper') == True
    assert has_callables('hello', 'lower', 'upper', 'foo') == True
    assert has_callables('hello', 'foo') == False
    assert has_callables('hello', 'foo', 'bar', 'cat') == False
    assert has_callables('hello', 'lower', 'upper', 'foo', 'bar') == True


# Generated at 2022-06-13 20:44:27.970227
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    from collections import Counter
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(Counter(),'get','keys','items','values') is True
    assert has_any_callables(set(),'get','keys','items','values') is False


# Generated at 2022-06-13 20:44:30.888576
# Unit test for function has_attrs
def test_has_attrs():
    assert has_attrs(dict(), 'get', 'keys', 'items', 'values') is True



# Generated at 2022-06-13 20:44:32.860328
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:44:37.614245
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2, c=3)
    assert has_callables(obj, 'get', 'items', 'keys', 'values') is True
    assert has_callables(obj._get, 'get', 'items', 'keys', 'values') is False
    assert has_callables(obj.items, 'get', 'items', 'keys', 'values') is True



# Generated at 2022-06-13 20:44:42.015311
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2, c=3)
    assert has_any_callables(obj,'get','keys','items','something') == True
    assert has_any_callables(obj,'something', 'something else') == False


# Generated at 2022-06-13 20:44:44.090420
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(dict(),'get','keys','items','values','foo') == True)


# Generated at 2022-06-13 20:44:53.857765
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import ChainMap
    from flutils.objutils import has_any_callables
    assert has_any_callables(ChainMap({'a': 1, 'b': 2}), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(ChainMap({'a': 1, 'b': 2}), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(ChainMap({'a': 1, 'b': 2}), 'get', 'keys', 'items') is True
    assert has_any_callables(ChainMap({'a': 1, 'b': 2}), 'get', 'keys') is True
    assert has_any_callables(ChainMap({'a': 1, 'b': 2}), 'get') is True

# Generated at 2022-06-13 20:45:02.880435
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    obj2 = dict(a=1, b=2, c=3)
    assert has_any_callables(obj, 'keys', 'values') == True
    assert has_any_callables(obj, 'keys', 'values', 'foo') == False
    assert has_any_callables(obj2, 'keys', 'values', 'foo') == False
    assert has_any_callables(obj2, 'keys', 'values', 'items') == True
    assert has_any_callables(obj2, 'keys', 'values', 'items') == True


# Generated at 2022-06-13 20:45:03.614070
# Unit test for function has_callables
def test_has_callables():
    pass

# Generated at 2022-06-13 20:45:15.685258
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import OrderedDict
    d = OrderedDict([('a', 1), ('b', 2)])
    assert has_any_callables(d, 'get', 'copy')
    assert has_any_callables(d, 'keys', 'items')
    assert has_any_callables(d, 'values', 'copy')
    assert has_any_callables(d, 'foo', 'bar')
    assert has_any_callables(d, 'foo', 'bar', 'baz')
    assert has_any_callables(d, 'bar', 'baz', 'foo')
    assert not has_any_callables(d, 'foo')
    assert not has_any_callables(d, 'foo', 'baz')

# Generated at 2022-06-13 20:45:23.307408
# Unit test for function has_any_callables
def test_has_any_callables():
    test_obj = {'hi': 5, 'foo': 7}
    assert has_any_callables(test_obj, ['get', 'keys', 'values', 'foo']) == True
    assert has_any_callables(test_obj, ['get', 'keys', 'values', 'hi']) == True


# Generated at 2022-06-13 20:45:28.546614
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True, 'Dict callables test failed'
    assert has_callables(list(),'append','clear','copy','count','extend') is True, 'List callables test failed'
    assert has_callables(str(),'capitalize','casefold','center','count','encode') is True, 'Str callables test failed'


# Generated at 2022-06-13 20:45:42.011929
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test for function has_any_callables"""
    # Arrange
    import functools
    import operator
    import sys
    from flutils.objutils import has_any_callables
    from . import _TestChild, _TestParent

    # Act
    obj = dict()
    obj2 = _TestParent()
    obj3 = _TestChild()
    obj4 = _TestChild()
    obj5 = _TestChild()
    obj5.son = _TestChild()
    obj6 = _TestChild()
    obj6.son = _TestChild()
    obj6.son.son = _TestChild()
    obj7 = _TestChild()
    obj7.son = _TestChild()
    obj7.son.son = _TestChild()
    obj7.son.son.son = _TestChild()
    obj

# Generated at 2022-06-13 20:45:57.318601
# Unit test for function has_callables
def test_has_callables():
    class A:
        def __init__(self):
            self.a = 1
            self.b = 2
        def c(self):
            pass

    def d():
        pass

    obj = A()
    assert has_callables(obj, 'c') is True
    assert has_callables(obj, 'c', 'a') is False
    assert has_callables(obj, 'c', 'a', 'd') is False
    assert has_callables(obj, 'a', 'b', 'd') is False
    assert has_callables(obj.a, 'to_bytes', 'to_bytes') is False
    assert has_callables(obj.b, 'to_bytes', 'to_bytes') is False
    assert has_callables(obj.a, 'to_bytes', 'to_bytes', 'value')

# Generated at 2022-06-13 20:45:58.321323
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:46:05.986793
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get') is True
    assert has_any_callables(dict(), 'keys') is True
    assert has_any_callables(dict(), 'items') is True
    assert has_any_callables(dict(), 'values') is True
    assert has_any_callables(dict(), 'foo') is False
    assert has_any_callables(1, 'foo') is False
    assert has_any_callables('foo', 'foo') is False


# Generated at 2022-06-13 20:46:11.545289
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()
    assert has_any_callables(obj, 'keys', 'values', 'items')
    assert not has_any_callables(obj, 'keys', 'values', 'items', 'foobar')
    # Make sure the function works on an instance of a list.
    obj = list()
    assert has_any_callables(obj, 'append', 'pop', 'clear')
    assert not has_any_callables(obj, 'keys', 'values', 'items', 'foobar')

# Generated at 2022-06-13 20:46:21.825513
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    from collections import UserList
    from collections.abc import ValuesView
    from functools import partial
    assert has_any_callables([], 'copy') is True
    assert has_any_callables(UserList(), 'copy') is False
    assert has_any_callables(ValuesView(dict(a=1, b=2)), 'copy') is False
    assert has_any_callables(partial(lambda x: x), '__call__') is True
    assert has_any_callables(partial(lambda x: x), 'copy') is False
    assert has_any_callables(lambda x: x, '__call__') is True



# Generated at 2022-06-13 20:46:28.348869
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1)
    assert has_any_callables(obj, 'keys', 'values', 'items', 'update') is True
    assert has_any_callables(obj, 'keys', 'values', 'foo', 'bar') is True
    assert has_any_callables(obj, 'blah', 'blah2', 'foo', 'bar') is False


# Generated at 2022-06-13 20:46:44.099670
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables('hello', 'upper')
    assert not has_any_callables('hello', 'upper', 'foo')
    assert not has_any_callables('hello', 'foo')
    assert has_any_callables('hello', 'foo', 'upper')


if __name__ == '__main__':
    # Unit tests
    test_has_any_callables()

    # Doc tests
    import doctest
    doctest.testmod()

    print('Done.')

# Generated at 2022-06-13 20:46:47.214101
# Unit test for function has_callables
def test_has_callables():
    assert not has_callables(dict(), 'foo', 'bar')
    assert not has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')



# Generated at 2022-06-13 20:46:52.761544
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(),'get','keys','items','values')
    assert not has_any_callables(dict(),'foo')


# Generated at 2022-06-13 20:46:58.687255
# Unit test for function has_callables
def test_has_callables():
    assert has_callables("Hello",'upper') is True
    assert has_callables("Hello",'upper','lower','capitalize') is True
    assert has_callables("Hello",'lower','upper','lower','lower','lower') is False
    assert has_callables("Hello",'lower','upper','lower','lower','lower','split') is False
    assert has_callables("Hello",'upper','lower','capitalize','split') is True


# Generated at 2022-06-13 20:47:00.753016
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True

# Generated at 2022-06-13 20:47:10.954981
# Unit test for function has_callables
def test_has_callables():
    from collections import defaultdict, OrderedDict
    from collections.abc import Mapping
    from pathlib import Path
    class MyDict(Mapping):
        def __init__(self, name: str) -> None:
            self._name = name
        def __getitem__(self, key: str) -> int:
            return 1 + key.lower().count('a')
        def __iter__(self) -> iter:
            yield from 'abcd'
        def __len__(self) -> int:
            return 4
        def __repr__(self) -> str:
            return self._name
    assert has_callables(defaultdict(int), 'get', '__missing__')
    assert has_callables(OrderedDict(), 'get')
    assert has_callables({}, 'get')
    assert has_

# Generated at 2022-06-13 20:47:22.239854
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True
    assert has_callables(dict(),'get','keys','items','foo') is False
    assert has_callables(dict(),'get','keys','foo','values') is False
    assert has_callables(dict(),'get','foo','items','values') is False
    assert has_callables(dict(),'foo','keys','items','values') is False
    assert has_callables(dict(a=1),'get','keys','items','values') is True
    assert has_callables(dict(a=1),'get','keys','items','foo') is False
    assert has_callables(dict(a=1),'get','keys','foo','values') is False

# Generated at 2022-06-13 20:47:24.898391
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'something') is False


# Generated at 2022-06-13 20:47:29.118732
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    assert has_any_callables(dict(), 'get', 'foo') == True
    assert has_any_callables(dict(), 'foo') == False


# Generated at 2022-06-13 20:47:34.411849
# Unit test for function has_any_callables
def test_has_any_callables():
    class Foo():
        def foo(self):
            pass
    foo = Foo()
    assert has_any_callables(foo, 'foo') is True, "foo.foo should be callable"



# Generated at 2022-06-13 20:47:41.893138
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), "get", "keys", "foo")
    assert not has_any_callables(dict(), "foo", "bar", "baz")
    assert not has_any_callables("hello", "get", "items", "bar")


# Generated at 2022-06-13 20:47:46.635368
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo', 'values', 'items', 'keys', 'get') is True
    assert has_any_callables(dict(), 'foo', 'values', 'items', 'keys') is False


# Generated at 2022-06-13 20:47:50.954397
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables({}, 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:47:54.985752
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict, 'get', 'keys', 'items', 'values') == True, "Result Should be True"
    assert has_callables(dict, 'get', 'keys', 'items', 'none') == False, "Result Should be False"



# Generated at 2022-06-13 20:47:55.748864
# Unit test for function has_any_callables
def test_has_any_callables():
    pass

# Generated at 2022-06-13 20:47:59.374324
# Unit test for function has_any_callables
def test_has_any_callables():
    class MyClass:
        def __init__(self):
            pass
        def foobar(self):
            pass
        
        def call_back(self):
            pass
    
    obj = MyClass()
    assert has_any_callables(obj, 'foobar', 'call_back') == True

# Generated at 2022-06-13 20:48:02.841169
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    assert has_callables(obj,'get','keys','items','values') == True
    assert has_callables(obj,'get','keys','items','bar') == False
    assert has_callables(obj,'get','keys','bar','values') == False
    assert has_callables(obj,'get','bar','items','values') == False
    assert has_callables(obj,'bar','keys','items','values') == False


# Generated at 2022-06-13 20:48:10.580110
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import Counter
    from collections.abc import Counter as CounterABC

    assert has_any_callables(Counter(), 'elements', 'most_common', 'foo')
    assert has_any_callables(CounterABC(), 'elements', 'most_common', 'foo')
    assert has_any_callables(Counter(), 'most_common', 'foo') is False
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'foo', 'bar', 'baz') is False


# Generated at 2022-06-13 20:48:21.910335
# Unit test for function has_callables
def test_has_callables():
    """
    Tests the has_callables function of objutils.py

    """
    import unittest

    class Testclass(object):
        def __init__(self):
            self.method = lambda: True

    class Testclasstwo(object):
        def __init__(self):
            self.method = 'notcallable'

    class Testclassthree(object):
        def __init__(self):
            self.method = ''
    #This test ensures that has_callables returns true if all attributes requested are callable
    testone = Testclass()
    testtwo = Testclasstwo()
    testthree = Testclassthree()

    class test(unittest.TestCase):
        def test_has_callables_true(self):
            self.assertTrue(has_callables(testone,'method'))

# Generated at 2022-06-13 20:48:24.766218
# Unit test for function has_callables
def test_has_callables():
    # Setup
    initial_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
    }
    # Exercise
    test_dict = initial_dict.copy()
    result = has_callables(test_dict, 'get', 'keys', 'items', 'values')
    # Verify
    assert result is True
    # Cleanup - None



# Generated at 2022-06-13 20:48:44.903231
# Unit test for function has_callables
def test_has_callables():
    """Test function has_callables."""
    _obj = dict(a=[1, 2, 4])
    _attrs = 'get', 'keys', 'items', 'values'
    assert has_callables(_obj, *_attrs)
    _attrs = 'some_nonsense', 'keys', 'items', 'values'
    assert has_callables(_obj, *_attrs) is False
    _attrs = 'get', 'keys', 'items', 'values', 'some_nonsense'
    assert has_callables(_obj, *_attrs) is False


# Generated at 2022-06-13 20:48:49.883026
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(
        dict(), 'get', 'keys', 'items', 'values', 'foo', 'klass') is False
    assert has_any_callables(
        dict(), 'get', 'keys', 'items', 'values', 'foo', 'klass') is False
    assert has_any_callables(dict(), 'klass') is False
    assert has_any_callables(dict()) is False



# Generated at 2022-06-13 20:48:52.715136
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'foo','bar','baz','qux') is False


# Generated at 2022-06-13 20:48:54.600588
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    

# Generated at 2022-06-13 20:49:03.246779
# Unit test for function has_callables
def test_has_callables():
    """Tests the function has_callables.
    """
    from .test import strutils_dict
    from .test import strutils_obj
    from .test import strutils_str
    assert has_callables(strutils_dict, 'foo', 'bar') is False
    assert has_callables(strutils_dict, 'foo', 'center') is True
    assert has_callables(strutils_dict.keys(), 'join', 'asdf') is False
    assert has_callables(strutils_obj, 'foo', 'bar') is False
    assert has_callables(strutils_obj, 'foo', 'center') is True
    assert has_callables(strutils_str, 'foo', 'bar') is False
    assert has_callables(strutils_str, 'foo', 'center') is True
    return



# Generated at 2022-06-13 20:49:13.153903
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') == True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo', 'bar') == True
    assert has_any_callables(dict(), 'get', 'keys', 'foo', 'values', 'bar') == True
    assert has_any_callables(dict(), 'get', 'keys', 'bar', 'foo', 'values') == True
    assert has_any_callables(dict(), 'foo', 'bar', 'baz') == False
    assert has_any_callables('hello', 'split') == True

# Generated at 2022-06-13 20:49:16.354015
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict()) is True
    assert has_any_callables(dict, 'get', 'something') is True
    assert has_any_callables(dict, 'crap', 'something') is False


# Generated at 2022-06-13 20:49:26.060931
# Unit test for function has_callables
def test_has_callables():
    assert (has_callables(dict(), 'get', 'keys', 'items', 'values'))
    assert (not has_callables(dict(), 'foo'))
    assert (not has_callables({'foo': 1, 'bar': 2}, 'get', 'keys', 'items', 'values'))
    assert (not has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo'))
    assert (has_callables(dict(), 'get', 'foo', 'items', 'values'))



# Generated at 2022-06-13 20:49:33.924090
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'keys', 'values', 'items')
    assert not has_callables(obj, 'keys', 'values', 'items', 'foo')


# Generated at 2022-06-13 20:49:36.431361
# Unit test for function has_callables
def test_has_callables():
    import pytest
    from collections import UserList
    obj = UserList()
    obj.append = lambda x: 1
    assert has_callables(obj, 'append') is True

# Generated at 2022-06-13 20:50:02.929180
# Unit test for function has_callables
def test_has_callables():
    import collections
    
    assert has_callables(collections.OrderedDict(), 'popitem')==True
    assert has_callables(collections.OrderedDict(), 'popitem', 'pop')==True
    

# Generated at 2022-06-13 20:50:09.309614
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict(a=1, b=2), 'keys', 'values')
    assert has_callables(dict(a=1, b=2), 'items', 'values')
    assert not has_callables(dict(a=1, b=2), 'foo', 'bar')


# Generated at 2022-06-13 20:50:18.723907
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import UserList

    obj = UserList()

    # Check each attr that the given `obj` has
    assert has_any_callables(obj, 'reverse', 'pop', 'insert', 'remove') is True
    assert has_any_callables(obj, 'foo', 'bar') is False

    # Check all attrs that the given `obj` has
    assert has_callables(obj, 'reverse', 'pop', 'insert', 'remove') is True

    # Make sure that it doesn't work the other way around
    assert has_callables(obj, 'reverse', 'pop', 'insert', 'remove', 'foo') is False



# Generated at 2022-06-13 20:50:19.786352
# Unit test for function has_any_callables
def test_has_any_callables():
    from unittest import TestCase



# Generated at 2022-06-13 20:50:26.717257
# Unit test for function has_callables
def test_has_callables():
    from flask import Flask
    from flutils.objutils import has_callables

    assert has_callables(Flask, 'url_for')
    assert has_callables(Flask, 'url_for', 'config')
    assert not has_callables(Flask, 'not_a_callable')
    assert not has_callables(Flask, 'url_for', 'not_a_callable')
    assert not has_callables(Flask, 'not_a_callable', 'not_a_callable_either')



# Generated at 2022-06-13 20:50:37.389808
# Unit test for function has_callables
def test_has_callables():

    # Test a dictionary object

    # Create a dictionary object
    d = dict(a=1,b=2)

    # Check that the attributes get and items exist and are callable
    assert has_callables(d,'get','items')

    # Check that the attributes get, items and keys exist and are callable
    assert has_callables(d,'get','items','keys')

    # Check that the attributes get, items, keys and values exist and are callable
    assert has_callables(d,'get','items','keys','values')

    # Check that the attributes keys and values exist and are callable
    assert has_callables(d,'keys','values')

    # Check that the attributes keys and values, and the attribute foo exists and is callable
    assert has_callables(d,'keys','values','foo')

    # Check that the attributes keys

# Generated at 2022-06-13 20:50:43.222000
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(), 'foo', 'bar') is False


# Generated at 2022-06-13 20:50:50.949228
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1, b=2)
    assert has_any_callables(d, 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(d, 'get', 'foo', 'bar') is True
    assert has_any_callables(d, 'gblah', 'foo', 'bar') is False
    assert has_any_callables(d, '__init__') is False
    assert has_any_callables(None, '__init__') is False
    assert has_any_callables(None, '__init__', 'get') is False

# Generated at 2022-06-13 20:51:00.076182
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(a=1, b=2, c=3), 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(dict(a=1, b=2, c=3), 'get', 'keys', 'items', 'values', 'bar')



# Generated at 2022-06-13 20:51:06.553295
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') == True
    assert has_callables(dict(),'get','keys','items','values','foo') == False
    assert has_callables(dict(),'get','keys','items','values','__doc__') == True
    assert has_callables(dict(),'get','keys','items','values','__doc__','foo') == False


# Generated at 2022-06-13 20:51:56.799451
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') == True
    assert has_callables(dict(), 'get', 'keys', 'items', 'something') == False
    assert has_callables(dict(), 'get', 'foo', 'bar', 'something') == False
    assert has_callables(None, 'get', 'test', 'something') == False
    assert has_callables('hello', 'capitalize', 'swapcase', 'upper') == True
    assert has_callables([1, 2, 3], 'count', 'index', 'pop') == True
    assert has_callables(set([1, 2, 3]), 'copy', 'pop', 'add') == True
    assert has_callables(frozenset([1, 2, 3]), 'copy', 'pop', 'add') == False


# Generated at 2022-06-13 20:52:03.466094
# Unit test for function has_any_callables
def test_has_any_callables():
    # Test the doc string examples
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    # Test for an object with a few callables and non-callables
    dict_obj = dict(a=1, b=2)
    assert has_any_callables(dict_obj,'values','items','update','foo')
    # Test for an object with no callables
    assert not has_any_callables(dict_obj,'a','b','c','foo')


# Generated at 2022-06-13 20:52:07.531970
# Unit test for function has_any_callables
def test_has_any_callables():
    print(has_any_callables(dict(), 'copy', 'update'))
    assert has_any_callables(dict(), 'copy', 'update')
    print('Pass all tests.')



# Generated at 2022-06-13 20:52:17.343338
# Unit test for function has_callables
def test_has_callables():
    from collections import (UserDict, UserList, UserString, ChainMap,
                             Counter, OrderedDict, defaultdict)
    from decimal import Decimal
    from types import MappingProxyType

    obj = {obj.__name__ : obj for obj in [
        UserDict, UserList, UserString, ChainMap, Counter, OrderedDict,
        defaultdict, Decimal, MappingProxyType,
    ]}

    assert has_callables(obj, 'keys', 'values', 'items') is True


# Generated at 2022-06-13 20:52:21.688722
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'foo') is True,\
        'given obj has some of the attributes passed and some are callable'
    assert has_any_callables(obj, 'foo', 'bar') is False,\
        'given obj has none of the attributes passed'
    assert has_any_callables(obj, 'keys', 'a') is False,\
        'given obj has the attributes, but the attributes are NOT callable'



# Generated at 2022-06-13 20:52:33.183609
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables([1,2,3], 'copy', 'remove', 'replace') is False
    assert has_any_callables(dict(a=1, b=2, c=3), 'get', 'keys', 'values') is True
    assert has_any_callables(reversed('hello'), '__call__') is True
    assert has_any_callables(sorted('hello'), '__call__') is True
    assert has_any_callables([1,2,3], 'upper', 'lower') is False
    assert has_any_callables(list(), 'upper', 'lower') is False


# Generated at 2022-06-13 20:52:37.085602
# Unit test for function has_callables
def test_has_callables():
    """function to test has_callables
    """
    assert has_callables(dict(),'get','keys','items','values') == True




# Generated at 2022-06-13 20:52:41.357944
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(object(), 'to_dict') is False
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(), 'to_dict') is False
    
    

# Generated at 2022-06-13 20:52:45.194449
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo', 'bar')


# Generated at 2022-06-13 20:52:51.461325
# Unit test for function has_any_callables
def test_has_any_callables():
    """ Unit test for function has_any_callables."""
    from flutils.objutils import has_any_callables
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True
