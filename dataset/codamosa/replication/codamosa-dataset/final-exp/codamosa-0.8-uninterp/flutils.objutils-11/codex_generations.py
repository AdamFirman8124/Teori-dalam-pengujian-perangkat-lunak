

# Generated at 2022-06-13 20:43:11.176735
# Unit test for function has_any_callables
def test_has_any_callables():
    # Verify positive result
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:43:19.549448
# Unit test for function has_callables
def test_has_callables():
    import pytest
    from flutils.objutils import has_callables
    assert has_callables({}, 'get') is False
    assert has_callables(set(), 'add') is True
    assert has_callables(int, 'bit_length') is True
    with pytest.raises(TypeError):
        assert has_callables('hello', 'add') is False


# Generated at 2022-06-13 20:43:21.991941
# Unit test for function has_callables
def test_has_callables():
    class TestClass:
        @staticmethod
        def func(*args):
            ...
    obj = TestClass()
    assert has_callables(obj, 'func') is True
    return True

# Generated at 2022-06-13 20:43:24.846948
# Unit test for function has_attrs
def test_has_attrs():
    assert has_attrs(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_attrs(dict(), 'get', 'keys', 'items', 'values', 'foo') is False



# Generated at 2022-06-13 20:43:33.999045
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(one=1, two=2, three=3), 'keys', 'items', 'values') is True
    assert has_any_callables(dict(one=1, two=2, three=3), 'append', 'get', 'items') is False
    assert has_any_callables(dict(a=1, b=2.3, c=3.14), 'keys', 'items', 'values') is True
    assert has_any_callables(dict(a=1, b=2.3, c=3.14), 'keys', 'items', 'anything') is True

# Generated at 2022-06-13 20:43:37.531847
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:43:46.145602
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import defaultdict
    from collections.abc import Sequence
    from collections import UserDict, ChainMap, OrderedDict
    from collections import Counter
    from collections import UserList, UserString
    from collections import deque
    from collections.abc import Iterator, KeysView, ValuesView
    from decimal import Decimal
    import math
    import enum

    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')

    obj = defaultdict(lambda: None)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')

    obj = ChainMap()
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')

    obj

# Generated at 2022-06-13 20:43:49.820426
# Unit test for function has_any_callables
def test_has_any_callables():
    pass
    # obj = "Hello"
    # # print(has_any_callables(obj,"foo","upper"))
    # print(has_any_callables(obj,"upper"))


# Generated at 2022-06-13 20:43:52.481678
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','foo','values') is True


# Generated at 2022-06-13 20:43:56.231078
# Unit test for function has_any_attrs
def test_has_any_attrs():
    # Test when there no attrs
    assert has_any_attrs(dict(),'aaaa') == False
    assert has_any_attrs(dict(), 'get','keys','items','values','something') == True
    assert has_any_attrs(dict(), 'foo','bar','baz') == False



# Generated at 2022-06-13 20:44:05.980386
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    keys = obj.keys()
    assert has_callables(keys, "copy", "__iter__", "__len__")
    assert has_callables(keys, "__reversed__", "__iter__", "__len__") is False
    assert has_callables(keys, "__reversed__", "__iter__", "__len__") is False
    assert has_callables(keys, "__reversed__", "__iter__", "__len__") is False
    assert has_callables(keys, "__reversed__", "__iter__", "__len__") is False
    assert has_callables(keys, "__reversed__", "__iter__", "__len__") is False

# Generated at 2022-06-13 20:44:15.669175
# Unit test for function has_callables
def test_has_callables():
    import pytest
    from collections import ChainMap, defaultdict

    assert has_callables(dict, 'get', 'keys', 'items', 'values')
    assert has_callables(list, 'sort', 'append', 'insert', 'extend')
    assert has_callables(set, 'add', 'clear', 'copy', 'difference')
    assert has_callables(tuple, 'count', 'index', '__getitem__')
    assert has_callables(str, 'isnumeric', 'islower', 'isupper', 'isalnum')
    assert has_callables(
        dict, 'get', 'keys', 'items', 'values', 'update', 'clear') is False
    assert has_callables(
        list, 'sort', 'append', 'insert', 'extend', 'clear', 'clear') is False
   

# Generated at 2022-06-13 20:44:17.056329
# Unit test for function has_attrs
def test_has_attrs():
    assert has_attrs(dict(),'get','keys','items','values')

# Generated at 2022-06-13 20:44:20.663704
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'get', 'keys', 'items') is True


# Generated at 2022-06-13 20:44:32.859347
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables({}, 'get', 'keys', 'items', 'values')
    assert has_callables(str(), 'get', 'keys', 'items', 'values')
    assert has_callables(list(), 'get', 'keys', 'items', 'values')
    assert has_callables(set(), 'get', 'keys', 'items', 'values')
    assert has_callables(frozenset(), 'get', 'keys', 'items', 'values')
    assert has_callables(tuple(), 'get', 'keys', 'items', 'values')
    assert has_callables(deque(), 'get', 'keys', 'items', 'values')

# Generated at 2022-06-13 20:44:35.401411
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'keys','items','values','foo')


# Generated at 2022-06-13 20:44:42.680943
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    print('Are any (get, keys, items, values, count) callable:',
                has_any_callables(obj,'get','keys','items','values','count'))
    print('Are any (get, keys, items, values) callable:',
                has_any_callables(obj,'get','keys','items','values'))
    return


# Generated at 2022-06-13 20:44:47.634588
# Unit test for function has_any_attrs
def test_has_any_attrs():
    actual = has_any_attrs(dict(),'get','keys','items','values','something')
    expected = True
    assert actual == expected


# Generated at 2022-06-13 20:44:54.151321
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'something') is True
    assert has_any_attrs(dict(), 'foo', 'bar', 'baz') is False
    assert has_any_attrs(2, 'real', 'denominator', 'numerator', 'imag') is True
    assert has_any_attrs(2, 'real', 'denominator', 'imag') is False
    assert has_any_attrs(2, 'foo', 'bar', 'baz') is False
    assert has_any_attrs(True, '__int__', '__bool__', 'numerator') is True
    assert has_any_attrs(True, '__int__', '__bool__') is True

# Generated at 2022-06-13 20:45:04.575880
# Unit test for function has_any_callables
def test_has_any_callables():
    expected_results = [
        (dict(a=1, b=2), ['get', 'keys', 'items', 'values'], True),
        (dict(a=1, b=2), ['get', 'foo', 'items', 'values'], True),
        (dict(a=1, b=2), ['get', 'foo', 'bar', 'values'], False),
        (1, ['get', 'foo', 'bar', 'values'], False),
        (Exception('Test'), ['get', 'foo', 'bar', 'values'], False),
    ]

    for obj, attrs, expected in expected_results:
        result = has_any_callables(obj, *attrs)
        assert result == expected, (result, expected)


# Generated at 2022-06-13 20:45:14.661760
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')


# Generated at 2022-06-13 20:45:27.890538
# Unit test for function has_callables
def test_has_callables():
    assert has_callables('foo', '__len__', '__eq__') is True

    assert has_callables(None, '__len__', '__eq__') is False

    assert has_callables(1, '__len__', '__eq__') is False

    assert has_callables((1, 2, 3), '__len__', '__eq__') is True

    assert has_callables([1, 2, 3], '__len__', '__eq__') is True

    assert has_callables({'a': 1, 'b': 2}, '__len__', '__eq__') is True

    assert has_callables(dict(), '__len__', '__eq__') is True

    assert has_callables(set(), '__len__', '__eq__') is True


# Generated at 2022-06-13 20:45:30.981667
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something') \
        is True


# Generated at 2022-06-13 20:45:33.754174
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values') is True



# Generated at 2022-06-13 20:45:35.918284
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict, 'get', 'keys', 'items', 'values') == True
    assert has_callables(dict, 'get', 'keys', 'items', 'other') == False



# Generated at 2022-06-13 20:45:42.374790
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'foo','bar','__setitem__') is True
    assert has_any_callables(dict(),'foo') is False
    assert has_any_callables(dict(a=1),'foo','__setitem__') is True
    assert has_any_callables(dict(a=1),'foo') is False


# Generated at 2022-06-13 20:45:57.370394
# Unit test for function has_callables
def test_has_callables():
    from unittest import TestCase
    import datetime

    class Dummy(object):
        def __init__(self):
            self.a = datetime.datetime.now()

        def __call__(self):
            return

    class Dummy2(object):
        def __init__(self):
            self.a = datetime.datetime.now()

    class Dummy3(object):
        def __init__(self):
            self.a = datetime.datetime.now()

        def __call__(self):
            return

    # noinspection PyMethodMayBeStatic,PyTypeChecker
    class TestHasCallables(TestCase):

        def test_has_callables(self):
            self.assertTrue(has_callables(Dummy(), 'a'))

# Generated at 2022-06-13 20:46:01.561556
# Unit test for function has_callables
def test_has_callables():
    #assert has_callables('dict_obj', 'keys', 'values')
    assert has_callables('dict_obj', 'keys', 'values')


# Generated at 2022-06-13 20:46:04.165409
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True


# Generated at 2022-06-13 20:46:12.066295
# Unit test for function has_any_attrs
def test_has_any_attrs():
    from collections import deque
    d = dict(hello=1, world=2)
    assert has_any_attrs(d, 'hello', 'world')
    assert has_any_attrs(d, 'hello', 'world', 'pop')
    assert not has_any_attrs(d, 'hello', 'world', 'pop', 'something')
    assert has_any_attrs(deque('abc'), 'appendleft', 'append')
    assert has_any_attrs(deque('abc'), 'appendleft', 'append', 'something')
    assert not has_any_attrs(deque(), 'appendleft', 'append', 'something')


# Generated at 2022-06-13 20:46:23.737055
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:46:26.182920
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')

# Generated at 2022-06-13 20:46:41.105249
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(list(),'append'))
    assert(has_any_callables(dict(),'get','keys','values'))
    assert(has_any_callables(dict(),'keys','values','foo'))
    assert(has_any_callables(dict(),'keys','items','values'))
    assert(has_any_callables(dict(),'keys','items','values','foo'))
    assert(has_any_callables(dict(),'keys','items','values','get'))
    assert(has_any_callables(dict(),'get','keys','items','values','foo'))
    assert(has_any_callables(dict(),'keys','items','values','get','foo'))

# Generated at 2022-06-13 20:46:45.855613
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1, b=2)
    assert has_any_callables(d, 'get', 'keys', 'items', 'values')
    assert has_any_callables(d, 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:46:56.528699
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    attrs = ('get', 'keys', 'values', 'items', 'foo')
    assert has_any_callables(obj, *attrs) is True
    assert has_any_callables(obj.items(), *attrs) is True
    assert has_any_callables(obj.keys(), *attrs) is True
    assert has_any_callables(obj.values(), *attrs) is True
    assert has_any_callables(None, *attrs) is False
    assert has_any_callables(obj.keys(), None, *attrs) is True


# Generated at 2022-06-13 20:46:59.888181
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo','bar','baz','bat','bam','bab','bab') is False

# Generated at 2022-06-13 20:47:01.549064
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True



# Generated at 2022-06-13 20:47:13.708758
# Unit test for function has_any_callables
def test_has_any_callables():
    # Grab the function to test
    func = has_any_callables

    # Test data
    args = [
        (dict(), 'get', 'keys', 'items', 'values', 'something'),
        (dict(), 'get', 'keys', 'items', 'values'),
        (dict(), 'get', 'keys', 'items', 'foo'),
        (dict(), 'get', 'keys', 'items'),
        (dict(), 'get', 'keys', 'foo'),
        (dict(), 'get', 'keys'),
        (dict(), 'get', 'foo'),
        (dict(), 'get'),
        (dict(), 'foo'),
    ]
    answers = [True, True, True, True, True, True, True, True, False]

    # The test

# Generated at 2022-06-13 20:47:16.244832
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')



# Generated at 2022-06-13 20:47:19.730644
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()
    assert has_any_callables(obj, 'get','foo','bar','baz') is True
