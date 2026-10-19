

# Generated at 2022-06-13 20:43:06.731835
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')

# Generated at 2022-06-13 20:43:20.834401
# Unit test for function has_any_attrs
def test_has_any_attrs():
    from unittest.mock import MagicMock

    def test_has_any_1() -> bool:
        class Test:
            def data(self):
                return self.data
            def field(self):
                return self.field
        obj = Test()
        assert has_any_attrs(obj, 'data', 'field') is True
        assert has_any_attrs(obj, 'data', 'field1') is True
        assert has_any_attrs(obj, 'data1', 'field') is True
        assert has_any_attrs(obj, 'data1', 'field1') is False
        a = MagicMock()
        a.has_any_attrs.return_value = True
        assert a.has_any_attrs(obj, 'data1', 'field1') is True
        return True

# Generated at 2022-06-13 20:43:23.381944
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True


# Generated at 2022-06-13 20:43:27.849579
# Unit test for function has_any_callables
def test_has_any_callables():
    '''True: does the function return TRUE if obj has any callable attrs'''
    obj = dict()
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values')



# Generated at 2022-06-13 20:43:31.967770
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test function has_any_callables.
    """
    from collections import UserDict

    assert has_any_callables(dict(), 'get','keys','items','something') is True
    assert has_any_callables(dict(), 'something') is False
    assert has_any_callables(UserDict(), 'something') is False



# Generated at 2022-06-13 20:43:43.014218
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs("", "title", "encode", "compose") == False
    assert has_any_attrs("", "title", "encode") == False
    assert has_any_attrs("", "title") == False
    assert has_any_attrs("Hello","title", "encode", "compose") == True
    assert has_any_attrs("Hello","title", "encode") == True
    assert has_any_attrs("Hello","title") == True
    assert has_any_attrs(dict(),'get','keys','items','values','something') == True
    assert has_any_attrs(dict(),'get','keys','items','values') == True
    assert has_any_attrs(dict(),'get','keys','items') == True

# Generated at 2022-06-13 20:43:46.830906
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo') == True


# Unit test function has_any_callables

# Generated at 2022-06-13 20:43:50.021793
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    result = has_callables(obj, 'get', 'keys', 'values', 'items')
    assert result is True


# Generated at 2022-06-13 20:43:51.112969
# Unit test for function has_attrs
def test_has_attrs():
    d = dict(a=1,b=2)
    assert(has_attrs(d,'get','keys'))


# Generated at 2022-06-13 20:43:54.220985
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_callables(dict(), 'get', 'keys', 'items')



# Generated at 2022-06-13 20:44:05.532170
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo', 'bar') is False



# Generated at 2022-06-13 20:44:07.660453
# Unit test for function has_callables
def test_has_callables():
    assert(has_callables(dict(),'get','keys','items','values') == True)


# Generated at 2022-06-13 20:44:09.649716
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')



# Generated at 2022-06-13 20:44:10.873228
# Unit test for function has_any_attrs
def test_has_any_attrs():
    pass



# Generated at 2022-06-13 20:44:18.088907
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(a=1, b=2, c=3), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'key', 'item', 'value') is False
    assert has_callables(dict(a=1, b=2, c=3), 'get', 'key', 'item', 'value') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_callables(dict(a=1, b=2, c=3), 'get', 'keys', 'items', 'values', 'foo') is False
    # noinspection PyTypeChecker
    assert has

# Generated at 2022-06-13 20:44:21.773953
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something') == True
    assert has_any_callables(dict(),'foo','bar') == False


# Generated at 2022-06-13 20:44:34.280449
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(),'get','keys','items','values')
    assert has_any_callables(dict(),'get','keys','items','foo')
    assert has_any_callables(dict(),'get','keys','items','__init__','keys')
    assert not has_any_callables(dict(),'get','keys','items','__init__','foo')
    assert not has_any_callables(dict(),'get','keys','items','__init__')
    assert not has_any_callables(dict(),'get','keys','items')
    assert not has_any_callables(dict(),'get','keys','foo')
    assert not has_any_callables(dict(),'get','keys')
   

# Generated at 2022-06-13 20:44:38.512001
# Unit test for function has_any_attrs
def test_has_any_attrs():
    obj = dict(a=1)
    expected = True
    actual = has_any_attrs(obj, 'get','values','keys','items','clear')
    assert actual == expected



# Generated at 2022-06-13 20:44:43.106675
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict(), '__iter__', '__sizeof__', '__eq__', '__ne__')
    # assert has_callables(dict(), '__get__')


# Generated at 2022-06-13 20:44:50.821486
# Unit test for function has_any_callables
def test_has_any_callables():

    # Setup
    class Foo:
        def __init__(self):
            self.one = 'one'
            self.two = lambda: None
            self.three = 'three'
            self.four = lambda: None

    # Exercise
    obj = Foo()
    result = has_any_callables(obj, 'one', 'two', 'three', 'four')

    # Verify
    assert result is True



# Generated at 2022-06-13 20:45:07.728692
# Unit test for function has_any_callables
def test_has_any_callables():
    class FakeClass(object):
        def __init__(self):
            self.mycallable = lambda: None
            self.myothercallable = lambda: None
            self.myuncallable = None
    assert has_any_callables(FakeClass(), 'mycallable', 'myothercallable', 'myuncallable') is True


# Generated at 2022-06-13 20:45:19.110315
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables([], 'append', 'extend', 'pop', 'remove', 'clear') is True
    assert has_any_callables([], 'reverse', 'copy', 'count', 'index', 'sort', 'clear') is False
    assert has_any_callables({'test': 1}, 'get', 'items', 'keys', 'values', 'clear') is True
    assert has_any_callables({'test': 1}, 'reverse', 'copy', 'count', 'index', 'sort', 'clear') is False
    assert has_any_callables(frozenset(), 'isdisjoint', 'intersection', 'difference', 'issubset', 'issuperset', 'update') is True

# Generated at 2022-06-13 20:45:24.051974
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'values', 'keys', 'items', 'foo') == True

if __name__ == '__main__':
    test_has_any_callables()

# Generated at 2022-06-13 20:45:29.672406
# Unit test for function has_callables
def test_has_callables():
    import unittest

    class TestHasCallables(unittest.TestCase):
        """Test the function has_callables."""

        def test_has_callables(self):
            self.assertTrue(has_callables(dict(), 'get', 'keys',
                                          'items', 'values'))
            self.assertFalse(has_callables(dict(), 'foo', 'bar',
                                           'baz', 'qux'))

    unittest.main()

# Generated at 2022-06-13 20:45:32.279574
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'items', 'get', 'values') is True
    assert has_any_callables(obj, 'foo', 'bar') is False


# Generated at 2022-06-13 20:45:41.473277
# Unit test for function has_any_callables
def test_has_any_callables():
    dict1 = dict(a=1, b=2)
    dict2 = dict(c=1, d=2)
    assert has_any_callables(dict1, 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict2, 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict1, 'foo', 'boo', 'moo') is False
    assert has_any_callables(dict2, 'foo', 'boo', 'moo') is False



# Generated at 2022-06-13 20:45:45.880158
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True



# Generated at 2022-06-13 20:45:54.285545
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values') is True
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'get','keys','items','values','foo','bar') is False


# Generated at 2022-06-13 20:45:57.280756
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True


# Generated at 2022-06-13 20:46:02.353337
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') == True
    assert has_any_callables(dict(), 'foo', 'keys', 'items', 'values') == False


# Generated at 2022-06-13 20:46:20.722733
# Unit test for function has_callables
def test_has_callables():
    data = [
        ('  ', False),
        ('ABC', True),
        (1, False),
        (False, False),
        ([1, 2, 3], True),
        (dict(a=1, b=2), True),
        (int, False),
        (list, True),
        (object, False),
        (str, False),
        (tuple, True)
    ]

    for obj, expected in data:
        assert has_callables(obj, 'append', 'remove', 'get', 'keys') == expected


# Generated at 2022-06-13 20:46:32.131314
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = [1,2,3,4,5]
    assert has_any_callables(obj, '__iter__','__getitem__') is True
    obj = dict(a=1,b=2)
    assert has_any_callables(obj,'get','keys') is True
    assert has_any_callables(obj,'foo','bar') is False
    obj = (1,2,3,4)
    assert has_any_callables(obj,'__getitem__') is True
    obj = 'str'
    assert has_any_callables(obj,'__getitem__') is True
    assert has_any_callables(obj,'join') is False
    # Unit test for function has_any_attrs

# Generated at 2022-06-13 20:46:45.075926
# Unit test for function has_any_callables
def test_has_any_callables():
    print('Testing is_list_like for a list')
    test_obj=dict(a=1,b=2)
    print(has_any_callables(test_obj,'get','keys','items','values'))
    print(has_any_callables(test_obj,'getf','keys','items','values'))
    print(has_any_callables(test_obj,'get','keysf','items','values'))
    print(has_any_callables(test_obj,'get','keys','itemsf','values'))
    print(has_any_callables(test_obj,'get','keys','items','valuesf'))


test_has_any_callables()

# Generated at 2022-06-13 20:46:45.976811
# Unit test for function has_callables
def test_has_callables():
    pass


# Generated at 2022-06-13 20:46:58.557795
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get') is True
    assert has_any_callables(dict(), 'foo') is False
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'something') is True
    assert has_attrs(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get') is True
    assert has_callables(dict(), 'foo') is False
    assert is_list_like([1, 2, 3]) is True

# Generated at 2022-06-13 20:47:01.744540
# Unit test for function has_any_attrs
def test_has_any_attrs():
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_attrs(dict(), 'foo') is False


# Generated at 2022-06-13 20:47:05.208941
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')

# Generated at 2022-06-13 20:47:10.455033
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test function to check if object has any callable attributes."""
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'a') == True, 'has_any_callables() failed.'



# Generated at 2022-06-13 20:47:14.149924
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')


# Generated at 2022-06-13 20:47:17.153702
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')


# Generated at 2022-06-13 20:47:36.931971
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values') is True
    assert has_any_callables(list(), 'get', 'keys', 'append', 'values') is True
    assert has_any_callables(list(), 'foo', 'bar') is False
    assert has_any_callables(dict(), 'get', 'keys', 'append', 'values') is False



# Generated at 2022-06-13 20:47:41.558441
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','something') == True
    assert has_any_callables(dict(),'a','b','c','d','e') == False


# Generated at 2022-06-13 20:47:50.345505
# Unit test for function has_any_callables
def test_has_any_callables():
    def func():
        pass

    class SampleClass:
        def __init__(self):
            self._a = 1

        def _add(self, a, b):
            return (a + b)

        @property
        def _prop(self):
            return self._a

        @_prop.setter
        def _prop(self, val):
            self._a = val

    obj = SampleClass()
    assert has_any_callables(obj, '_add') is True
    assert has_any_callables(obj, '_prop', '_add') is True
    assert has_any_callables(obj, '_prop', '_add', '_b') is True
    assert has_any_callables(obj, '_a', '_b', '_c') is False
    assert has_any_call

# Generated at 2022-06-13 20:47:57.180796
# Unit test for function has_any_callables
def test_has_any_callables():
    # objutils.has_any_callables(obj=dict,attrs=['get','keys','items','values','something'])
    # objutils.has_any_callables(obj=[],attrs=['get','keys','items','values','something'])
    assert has_any_callables(dict(),'get','keys','items','values','something') is True
    assert has_any_callables([], 'get', 'keys', 'items', 'values', 'something') is False

# Generated at 2022-06-13 20:48:07.197953
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'foo') is True
    assert has_any_callables(dict(), 'foo') is False
    assert has_any_callables(lambda x: x, '__call__', 'something') is True
    assert has_any_callables(lambda x: x, 'something') is False
    assert has_any_callables(1, '__add__') is True
    assert has_any_callables(1, 'something') is False



# Generated at 2022-06-13 20:48:20.206853
# Unit test for function has_any_callables
def test_has_any_callables():
    import collections
    import datetime
    from pytest import raises
    from types import MethodType
    from flutils.objutils import has_any_callables

    # Test if a class has any callable attributes
    class A(object):
        x = 1
        y = 2
        def __init__(self):
            self.z = 3
        def __call__(self, *args, **kwargs):
            pass

    x = A()
    assert has_any_callables(x, '__init__', '__call__') == True
    assert has_any_callables(x, 'x', 'y', 'z') == False
    assert has_any_callables(x, 'x', 'y', 'z', '__call__') == True

    # Test if an object has any callable attributes
    x = dat

# Generated at 2022-06-13 20:48:28.547151
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'values', 'items') is True
    assert has_any_callables(obj, 'get', 'keys', 'values', 'items', 'foo') is True
    assert has_any_callables(obj, 'get', 'keys', 'values', 'items', 'foo', 'bar') is False



# Generated at 2022-06-13 20:48:31.634810
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(),*['get','keys','items','values','foo'])


# Generated at 2022-06-13 20:48:34.816647
# Unit test for function has_callables
def test_has_callables():
    from flutils.objutils import has_callables
    from os import path

    assert has_callables(path, 'abspath', 'devnull', 'expanduser') is True
    assert has_callables(path, 'abspath', 'devnull', 'expanduser', 'foo') is False

# Generated at 2022-06-13 20:48:41.000239
# Unit test for function has_any_callables
def test_has_any_callables():
    test_dict = {'a': 1, 'b': 2}
    assert has_any_callables(test_dict, 'items', 'keys', 'values')
    assert not has_any_callables(test_dict, 'aa', 'bb', 'cc')

# Generated at 2022-06-13 20:48:56.156376
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables([1, 2, 3],'append', 'insert', 'remove', 'extend')
    assert has_any_callables(dict(a=1, b=2),'get', 'keys', 'items', 'values')
    assert has_any_callables((1, 2, 3),'append', 'insert', 'remove', 'extend')
    assert has_any_callables(reversed((1, 2, 3)), 'append', 'insert', 'remove', 'extend')
    assert has_any_callables(iter((1, 2, 3)), 'append', 'insert', 'remove', 'extend')

# Generated at 2022-06-13 20:48:58.747760
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert not has_any_callables(dict(),'get','keys','items','values','foo','f','g','h','i')
    assert not has_any_callables(dict(),'f','g','h','i')


# Generated at 2022-06-13 20:49:10.897997
# Unit test for function has_callables
def test_has_callables():
    obj = {'get': lambda self, item: self[item],
           'keys': lambda self: iter(self.keys()),
           'values': lambda self: iter(self.values()),
           'items': lambda self: iter(self.items()),
           }

    attrs = ('get', 'keys', 'values', 'items', 'something')
    assert has_callables(obj, *attrs) is True
    assert has_callables(obj, *attrs[:1]) is True
    assert has_callables(obj, *attrs[:-1]) is True
    assert has_callables(obj, *attrs[:-2]) is False
    assert has_callables(obj, *attrs[:-3]) is False
    assert has_callables(obj, *attrs[-4:4]) is True
   

# Generated at 2022-06-13 20:49:13.641665
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict()
    assert has_any_callables(d,'get','keys','items','values','foo') == True



# Generated at 2022-06-13 20:49:17.511665
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict, 'get') == True
    assert has_callables(dict, 'items') == True
    assert has_callables(dict, 'keys') == True
    assert has_callables(dict, 'values') == True
    assert has_callables(dict, 'get', 'items', 'keys', 'values') == True
    assert has_callables(dict, 'foo', 'bar', 'baz') == False


# Generated at 2022-06-13 20:49:28.672764
# Unit test for function has_callables
def test_has_callables():
    """Test for function has_callables"""
    a = dict(a=1, b=2)
    b = list(range(3))
    c = set(range(3))
    d = tuple(range(3))
    e = 'hello'
    f = reversed(range(3))
    g = ValuesView(a)
    h = KeysView(a)
    i = UserList(range(3))
    j = deque(range(3))
    assert has_callables(a, 'get', 'keys', 'items', 'values')
    assert has_callables(b, 'append', 'insert', 'remove', 'copy')
    assert has_callables(c, 'add', 'remove', 'update', 'difference')

# Generated at 2022-06-13 20:49:39.688389
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables({'get': str, 'keys': str, 'values': str}, 'get', 'keys', 'values', 'foo') is True
    assert has_any_callables({'get': str, 'keys': str, 'values': str}, 'get', 'keys', 'values') is False
    assert has_any_callables({'get': str, 'keys': str, 'values': str}, 'get', 'keys', 'values', 'foo', 'bar') is True
    assert has_any_callables({'get': str, 'keys': str, 'values': str}, 'get', 'keys', 'values', 'foo', 'bar', 'baz') is False


# Generated at 2022-06-13 20:49:41.919089
# Unit test for function has_callables
def test_has_callables():
    assert True is has_callables(dict(), 'get', 'keys', 'items', 'values')

# Generated at 2022-06-13 20:49:54.225465
# Unit test for function has_callables
def test_has_callables():
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserString,
        defaultdict
    )

    class MyClass(dict):
        pass

    chain_map = ChainMap()
    chain_map['a'] = 1
    chain_map['b'] = 2

    counter = Counter()
    counter['a'] = 1
    counter['b'] = 2

    ordered_dict = OrderedDict()
    ordered_dict['a'] = 1
    ordered_dict['b'] = 2

    user_dict = UserDict()
    user_dict['a'] = 1
    user_dict['b'] = 2

    user_string = UserString('foo')

    default_dict = defaultdict(None)
    default_dict['a'] = 1
    default_dict

# Generated at 2022-06-13 20:49:56.722802
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True



# Generated at 2022-06-13 20:50:11.166426
# Unit test for function has_any_callables
def test_has_any_callables():
    assert True == has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert False == has_any_callables(dict(), 'foo', 'bar', 'baz')


# Generated at 2022-06-13 20:50:13.273010
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') == True


# Generated at 2022-06-13 20:50:15.491627
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True
    assert has_callables(dict(),'get_keys','items','values') is False


# Generated at 2022-06-13 20:50:22.063979
# Unit test for function has_callables
def test_has_callables():
    from collections import OrderedDict
    test = OrderedDict(a=1, b=2)
    assert(has_callables(test,'items','pop'))
    assert(has_callables(test,'items'))
    assert(has_callables(test,'pop'))
    assert(has_callables(test,))
    assert not has_callables(test,'a')
    assert not has_callables(test,'keys','a')
    assert not has_callables([1,2,3], 'a')


# Generated at 2022-06-13 20:50:23.450242
# Unit test for function has_callables
def test_has_callables():
    test_obj = dict(a='12345')
    has_callables(test_obj, '__len__', '__getitem__')

# Generated at 2022-06-13 20:50:30.107772
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'foo') == False
    assert has_any_callables(dict(), 'foo', 'bar', 'baz') == False
    assert has_any_callables('', 'isupper', 'islower', 'isdigit')
    assert has_any_callables('', 'islower', 'isdigit') == False
    assert has_any_callables('', 'foo', 'bar', 'baz') == False


# Generated at 2022-06-13 20:50:39.185076
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(dict(),'get','keys','items','values','foo') is True)
    assert(has_any_callables(dict(), 'keys', 'foo') is True)
    assert(has_any_callables(list(), 'append', 'count') is True)
    assert(has_any_callables(list(), 'append', 'foo') is True)
    assert(has_any_callables(list(), 'count') is True)
    assert(has_any_callables(set(), 'add', 'foo') is True)
    assert(has_any_callables(set(), 'discard', 'remove') is True)
    assert(has_any_callables(frozenset(), 'foo') is False)
    assert(has_any_callables('foo', 'join') is True)
   

# Generated at 2022-06-13 20:50:44.161439
# Unit test for function has_callables
def test_has_callables():
    from collections import OrderedDict
    obj = OrderedDict([("a", 1), ("b", 2)])
    assert has_callables(obj, 'values', 'keys', 'items', 'popitem') is True


# Generated at 2022-06-13 20:50:49.692102
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert has_any_callables(dict(),'get','keys','items','values')
    assert not has_any_callables(dict(),'get','keys','items','foo')
    assert not has_any_callables(dict(),'foo')
    assert not has_any_callables(None,'foo')


# Generated at 2022-06-13 20:50:51.514944
# Unit test for function has_callables
def test_has_callables():
    d = dict(a=1, b=2)
    assert has_callables(d, 'keys', 'items', 'values') == True



# Generated at 2022-06-13 20:51:13.982971
# Unit test for function has_any_callables
def test_has_any_callables():
    print(has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo'))



# Generated at 2022-06-13 20:51:20.822738
# Unit test for function has_any_callables
def test_has_any_callables():
    assert not has_any_callables('hello', 'foo', 'upper')
    assert has_any_callables('hello', 'foo', 'upper')
    assert not has_any_callables('hello', 'foo')
    assert has_any_callables('hello', 'foo', 'upper', 'replace')
    assert has_any_callables('hello', 'foo', 'upper', 'replace')
    assert has_any_callables('hello', 'upper', 'replace')
    assert not has_any_callables(1, 'foo', 'upper')
    assert not has_any_callables(1, 'foo')
    assert not has_any_callables(1, 'foo', 'upper', 'replace')
    assert not has_any_callables(1, 'foo', 'upper', 'replace')
    assert not has_any_

# Generated at 2022-06-13 20:51:24.789698
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is not False
    return

# Generated at 2022-06-13 20:51:34.597601
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_callables(dict(), 'get', 'keys', 'values')
    assert has_callables(dict(), 'get', 'keys')
    assert has_callables(dict(), 'keys')
    assert has_callables(dict(), 'items', 'keys')
    assert has_callables(dict(), '__len__')
    assert has_callables(dict(), '__getitem__')



# Generated at 2022-06-13 20:51:36.956347
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True



# Generated at 2022-06-13 20:51:42.879347
# Unit test for function has_callables
def test_has_callables():

    # use object from different module (dict)
    # use getattr to get the object's attr
    # check if the attr is callable

    # use function from the same module
    # use the function to check if the object is a subclass of any of the
    #   given classes
    # use the function to check if the given obj has all the given attrs

    # use function from different module
    # use the function to create a dictionary and get the object's attr

    from flutils.objutils import has_callables

    d = dict(a=1, b=2, c=3)

    cls = [dict, UserList]

    attrs = ['__len__', 'values']

    # True
    assert has_callables(d, *attrs)

    # True

# Generated at 2022-06-13 20:51:45.782764
# Unit test for function has_callables
def test_has_callables():
    class Test(object):
        def a(self):
            pass
        def b(self):
            pass

    assert has_callables(Test(), 'a', 'b') == True
    assert has_callables(Test(), 'a', 'c') == False


# Generated at 2022-06-13 20:51:50.527728
# Unit test for function has_callables
def test_has_callables():
    import subprocess
    assert has_callables(subprocess.Popen, 'communicate') == True
    assert has_callables(subprocess.Popen, 'communicate', 'foo') == False
    assert has_callables(subprocess.Popen, 'foo') == False

# Generated at 2022-06-13 20:51:59.340201
# Unit test for function has_callables
def test_has_callables():

    class Object:
        """Object Class"""
        def __init__(self, *args):
            self.var = args[0]

        def __call__(self):
            return 'var: {0}'.format(self.var)

    obj = Object('foo')
    assert has_callables(obj, 'var', '__call__')

    obj = Object(1)
    assert has_callables(obj, 'var', '__call__') is False



# Generated at 2022-06-13 20:52:05.829750
# Unit test for function has_callables
def test_has_callables():
    assert not has_callables(dict(), 'something')
    assert not has_callables(dict(), 'get', 'something')
    assert has_callables(dict(), 'get', 'keys')
    assert not has_callables(dict(), 'get', 'keys', 'something')
