

# Generated at 2022-06-13 20:43:07.980508
# Unit test for function has_any_callables
def test_has_any_callables():
    pass



# Generated at 2022-06-13 20:43:15.793670
# Unit test for function has_attrs
def test_has_attrs():
    from types import SimpleNamespace
    obj = SimpleNamespace(a='a', b='b')
    assert has_any_attrs(obj,'a','b','c') is True
    assert has_any_attrs(obj,'c','d') is False
    assert has_attrs(obj,'a','b') is True
    assert has_attrs(obj,'c') is False


# Generated at 2022-06-13 20:43:19.806969
# Unit test for function has_callables
def test_has_callables():
    # Given
    attrs = 'get','keys','items','values'
    # When
    obj = dict()
    # Then
    assert has_callables(obj,*attrs) == True


# Generated at 2022-06-13 20:43:21.877086
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values','foo') is True

# Generated at 2022-06-13 20:43:26.343570
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    assert has_callables(obj, 'get', 'keys', 'items', 'values') is True

# Generated at 2022-06-13 20:43:29.382762
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()
    attrs = ('get', 'keys', 'items', 'values')
    assert has_any_callables(obj,*attrs) is True


# Generated at 2022-06-13 20:43:33.321175
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:43:42.926731
# Unit test for function has_callables
def test_has_callables():
    class U:
        def __init__(self, **kwargs):
            self.kwargs = kwargs

        def __getattr__(self, attr):
            return self.kwargs.get(attr)

    assert has_callables(U(foo=lambda: None), 'foo') is True
    assert has_callables(U(foo=lambda: None), 'foobar') is False
    assert has_callables(U(), 'foobar') is False
    assert has_callables(None, 'foobar') is False



# Generated at 2022-06-13 20:43:46.161597
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'foo') is False


# Generated at 2022-06-13 20:43:49.401956
# Unit test for function has_any_attrs
def test_has_any_attrs():
    obj = dict()
    assert has_any_attrs(
        obj, 'get', 'keys', 'items', 'values', 'something'
    ) is True



# Generated at 2022-06-13 20:44:01.927419
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import (
        UserList,
        deque,
    )
    from collections.abc import (
        Iterator,
        KeysView,
        ValuesView,
    )
    from typing import (
        Any
    )
    from unittest import (
        TestCase,
        main as unit_test_main,
    )

    class TempClass(object):
        __slots__ = [
            'foo',
            'bar',
        ]
        def __init__(self):
            self.foo = 'Bar'
            self.bar = 1

        def __repr__(self):
            return f'{self.__class__.__name__}()'


# Generated at 2022-06-13 20:44:08.247667
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1,b=2)
    assert has_any_callables(d,'get','keys','items','values')==True
    assert has_any_callables(d,'get','keys','items','values','foo')==True
    assert has_any_callables(d,'foo','bar')==False


# Generated at 2022-06-13 20:44:17.237449
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1,b=2)
    assert has_any_callables(d,'get')
    assert has_any_callables(d,'keys')
    assert has_any_callables(d,'items')
    assert has_any_callables(d,'values')
    assert has_any_callables(d,'get','keys','values','items')
    assert has_any_callables(d,'get','keys','items','foo','values','something')
    assert has_any_callables(d,'get','keys','values','something') is False


# Generated at 2022-06-13 20:44:26.140725
# Unit test for function has_any_callables
def test_has_any_callables():
    # Dictionary
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(a=1), 'get', 'keys', 'items', 'values')
    assert has_any_callables(dict(a=1), 'get', 'keys', '__subclasscheck__')
    assert has_any_callables(dict(a=1), 'get', 'keys', '__subclasscheck__', 'bar')
    assert has_any_callables(dict(a=1), 'get', 'keys', '__subclasscheck__', 'bar') is not False
    assert has_any_callables(dict(a=1), 'get', 'keys', '__subclasscheck__', 'bar') is not object
    # List
    assert has_any

# Generated at 2022-06-13 20:44:27.760877
# Unit test for function has_callables
def test_has_callables():
    return 'foo'


# Generated at 2022-06-13 20:44:32.489635
# Unit test for function has_callables
def test_has_callables():
    assert has_callables("", "lower") is True, \
        "lower method is not callable for string"


if __name__ == "__main__":
    test_has_callables()

# Generated at 2022-06-13 20:44:36.359888
# Unit test for function has_callables
def test_has_callables():
    class Test(object):
        def a(self):
            pass
        def b(self):
            pass
        def c(self):
            pass

    t = Test()
    assert has_callables(t, 'a', 'b', 'c')
    assert has_callables(t, 'a', 'b')


# Generated at 2022-06-13 20:44:47.190900
# Unit test for function has_callables
def test_has_callables():
    class ExampleCallable(object):
        def do_something(self):
            return 'test'

        def _do_something_else(self):
            return 'test'

        @property
        def test_property(self):
            return 'test'

    example_callable = ExampleCallable()
    assert has_callables(example_callable, 'do_something', '_do_something_else') is True
    assert has_callables(example_callable, 'do_something', '_do_something_else', 'test_property') is False
    assert has_callables(example_callable, 'do_something', '_do_something_else', 'test_property', 'foo') is False
    assert has_callables(example_callable, 'foo') is False

    # Unit test for function has_any_callables

# Generated at 2022-06-13 20:44:53.954741
# Unit test for function has_any_callables
def test_has_any_callables():
    import pytest
    obj = None
    msg = 'Argument obj must be an object with at least one callable attribute'
    with pytest.raises(TypeError, match=msg):
        has_any_callables(obj)
    obj = 123
    msg = 'Argument obj must be an object with at least one callable attribute'
    with pytest.raises(TypeError, match=msg):
        has_any_callables(obj)
    obj = 'abc'
    msg = 'Argument obj must be an object with at least one callable attribute'
    with pytest.raises(TypeError, match=msg):
        has_any_callables(obj)
    obj = {}
    msg = 'Argument obj must be an object with at least one callable attribute'

# Generated at 2022-06-13 20:45:04.726589
# Unit test for function has_callables
def test_has_callables():
    # True if all of the attributes are callable
    obj = dict(a = 1, b = 2)
    assert has_callables(obj, 'clear')
    assert has_callables(obj, 'get')
    assert has_callables(obj, 'keys')
    assert has_callables(obj, 'values')
    assert has_callables(obj, 'items')
    assert has_callables(obj, 'copy')
    assert has_callables(obj.keys(), 'copy')
    assert has_callables(obj.values(), 'copy')
    assert has_callables(obj.items(), 'copy')
    assert has_callables(obj.keys(), '__getitem__')
    assert has_callables(obj.values(), '__getitem__')

# Generated at 2022-06-13 20:45:14.663607
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'items', 'values') is True,\
        "has_any_callables(obj, 'get', 'items', 'values') is not True."



# Generated at 2022-06-13 20:45:23.601438
# Unit test for function has_callables
def test_has_callables():
    
    # Test 1
    obj = dict(zip(range(1,10),range(100,110)))
    assert has_callables(obj,'get','keys','values') == True

    # Test 2
    assert has_callables(obj,'get','keys','values','foo') == False

    # Test 3
    assert has_callables(obj,'get','keys','values','foo','update') == True

    return


# Generated at 2022-06-13 20:45:29.972799
# Unit test for function has_callables
def test_has_callables():
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if ((i == 0) or (j == 0) or (k == 0) or (l == 0)):
                        assert has_callables(dict(), "get", "keys", "items",
                                             "values") is True
                    else:
                        assert has_callables(dict(), "get", "keys", "items",
                                             "values") is True



# Generated at 2022-06-13 20:45:32.553023
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2, c=3)
    assert has_callables(obj, 'get', 'keys', 'items', 'values') is True
    assert has_callables(obj, 'foo') is False



# Generated at 2022-06-13 20:45:41.176973
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import deque

    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(deque(), 'append', 'appendleft', 'foo')
    assert has_any_callables(set(), 'add', 'clear', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_any_callables(set(), 'add', 'clear')
    assert has_any_callables(deque(), 'append', 'appendleft')
    assert has_any_callables(frozenset(), 'foo') is False

# Generated at 2022-06-13 20:45:45.054138
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'foo') is True

# Generated at 2022-06-13 20:45:58.071964
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items', 'foo')
    assert has_any_callables(list(), 'append', 'remove', 'index', 'extend', 'foo')
    assert has_any_callables(set(), 'add', 'remove', 'copy', 'update', 'foo')
    assert has_any_callables(frozenset(), 'copy', 'union', 'isdisjoint', 'difference', 'foo')
    assert has_any_callables(tuple(), 'index', 'count', 'foo')
    assert has_any_callables(deque(), 'append', 'appendleft', 'extend', 'pop', 'foo')
    assert has_any_callables(ToCollection(), 'add', 'has', 'discard', 'pop', 'foo')


# Generated at 2022-06-13 20:46:01.339338
# Unit test for function has_callables
def test_has_callables():
    assert (has_callables(dict(),'get','keys','items','values') == True)



# Generated at 2022-06-13 20:46:08.187844
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo', 'frozenset') is False
    assert has_any_callables(frozenset, 'get', 'keys', 'items', 'values', 'foo') is False



# Generated at 2022-06-13 20:46:15.091688
# Unit test for function has_callables
def test_has_callables():
    assert not has_callables('not a list', 'append')
    assert not has_callables(1, 'append')
    assert not has_callables(None, 'append')
    assert not has_callables(dict(), 'append')
    assert has_callables([], 'append')
    assert has_callables({}, 'keys')


# Generated at 2022-06-13 20:46:27.448189
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import UserDict
    obj = UserDict()
    result = has_any_callables(obj, 'form', 'keys', 'values')
    assert result == False
    result = has_any_callables(obj, 'form', 'keys', 'values', '__setitem__')
    assert result == True



# Generated at 2022-06-13 20:46:36.411850
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get1', 'keys1', 'items', 'values') is False
    assert has_any_callables(dict(), 'get1', 'keys1', 'items1', 'values1') is False

# Generated at 2022-06-13 20:46:42.469614
# Unit test for function has_callables
def test_has_callables():
    # assert True
    assert has_callables(dict, 'get', 'keys') == True
    assert has_callables(dict, 'get', 'keys', 'get') == True
    assert has_callables(dict, 'get', 'keys', 'foo') == False


# Generated at 2022-06-13 20:46:47.019066
# Unit test for function has_callables
def test_has_callables():
    from copy import copy

    from flutils.objutils import has_callables

    assert (has_callables(copy, "copy", "deepcopy")) is True

    assert (has_callables(copy, "foo", "bar", "baz")) is False

    assert (has_callables(None, "copy", "deepcopy")) is False



# Generated at 2022-06-13 20:46:47.982502
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values') is True

# Generated at 2022-06-13 20:46:53.524659
# Unit test for function has_any_callables
def test_has_any_callables():
    # Test for valid return
    assert has_any_callables(dict(),'get','keys','items','values','foo')

    # Test for invalid return
    assert has_any_callables(dict(),'foo','bar','bogus') is not True


# Generated at 2022-06-13 20:46:55.400893
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables([1,2,3],'keys','items','values','something')


# Generated at 2022-06-13 20:47:06.016587
# Unit test for function has_callables
def test_has_callables():
    # Does it return True for callables that exist?
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'foo', 'bar') is True
    assert has_callables(dict(), 'keys', 'foo', 'bar') is True
    assert has_callables(dict(), 'items', 'foo', 'bar') is True
    assert has_callables(dict(), 'values', 'foo', 'bar') is True

    # Does it return False for missing callables?
    assert has_callables(dict(), 'foo', 'bar') is False
    assert has_callables(dict(), 'get', 'foo') is False
    assert has_callables(dict(), 'keys', 'foo') is False

# Generated at 2022-06-13 20:47:15.341876
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(
        dict(),
        'get',
        'keys',
        'items',
        'values',
        'foo',
    ) is True
    assert has_any_callables(
        dict(),
        'get',
        'keys',
        'items',
        'values',
        '__module__',
    ) is True
    assert has_any_callables(
        dict(),
        'get',
        'keys',
        'items',
        'values',
        '__module__',
        '__repr__',
    ) is True

# Generated at 2022-06-13 20:47:22.354173
# Unit test for function has_any_callables
def test_has_any_callables():
    from io import StringIO
    from collections import OrderedDict
    from contextlib import redirect_stdout
    from flutils.objutils import has_any_callables as hascall

    # Dictionary
    assert has_any_callables(dict(),'get','keys','items','values')

    # StringIO
    assert hascall(StringIO(),'write','read')

    # OrderedDict
    assert hascall(OrderedDict(),'clear','popitem','update')

    # redirect_stdout
    assert hascall(redirect_stdout(StringIO()),'write','write_nowrap')

# Generated at 2022-06-13 20:47:42.459129
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import Counter
    from collections.abc import Mapping
    from typing import Any

    my_dict: Mapping[str, str] = {'a': 'b'}
    my_counter: Counter[str] = Counter({'a': 1, 'b': 2, 'c': 3})
    my_counter_keys: KeysView[str] = my_counter.keys()
    my_string: Any = 'str'

    expected_result: bool = False
    result: bool = has_any_callables(my_dict, 'get', 'keys', 'values', 'items')
    assert result is expected_result

    expected_result: bool = True
    result: bool = has_any_callables(my_counter, 'get', 'keys', 'values', 'items')
    assert result is expected_result


# Generated at 2022-06-13 20:47:51.014328
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(list(), 'append', 'items', 'get')
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items')
    assert has_any_callables(dict(a=1, b=2), 'get', 'keys', 'values', 'items')
    assert has_any_callables(
        {'a': 1, 'b': 2}, 'get', 'keys', 'values', 'items'
    )
    assert has_any_callables(
        namedtuple('Test', ('a', 'b'))(1, 2), '_asdict'
    )
    assert has_any_callables(
        namedtuple('Test', ('a', 'b'))(1, 2), '_asdict', 'get'
    )
    assert has_any

# Generated at 2022-06-13 20:47:54.781434
# Unit test for function has_any_callables
def test_has_any_callables():
     assert has_any_callables(dict(),'get','keys','items','values','foo')==True
     assert has_any_callables(dict(),'get','keys','items','values')==True
     assert has_any_callables(dict(),'foo')==False


# Generated at 2022-06-13 20:48:01.651939
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True, \
        'has_callables - FAILED'
    assert has_callables(dict(), 'get', 'keys', 'items') is True, \
        'has_callables - FAILED'
    assert has_callables(dict(), 'keys', 'items') is True, \
        'has_callables - FAILED'
    assert has_callables(dict(), 'keys', 'items', 'values') is True, \
        'has_callables - FAILED'
    assert has_callables(dict(), 'keys') is True, 'has_callables - FAILED'
    assert has_callables(dict(), 'keys', 'foo') is False, \
        'has_callables - FAILED'
   

# Generated at 2022-06-13 20:48:06.456711
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert not has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo', '__add__')


# Generated at 2022-06-13 20:48:10.619329
# Unit test for function has_any_callables
def test_has_any_callables():
    class A:
        def __init__(self):
            pass
    a = A()
    assert has_any_callables(a,'foo', '__init__') is True

# Generated at 2022-06-13 20:48:15.323922
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'keys', 'values') is True
    assert has_any_callables(obj, 'foo', 'bar') is False


# Generated at 2022-06-13 20:48:20.045892
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(
        dict(),
        'get',
        'keys',
        'items',
        'values',
        'foo'
    )



# Generated at 2022-06-13 20:48:23.034918
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')



# Generated at 2022-06-13 20:48:25.958178
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True



# Generated at 2022-06-13 20:48:51.828818
# Unit test for function has_any_callables
def test_has_any_callables():
    lst = [4, 3, 2]
    assert has_any_callables(lst, 'sort', 'reverse')



# Generated at 2022-06-13 20:48:53.518761
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(),'get','keys','items','values')==True


# Generated at 2022-06-13 20:49:00.216019
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test that has_any_callables returns True if the object has at least one
    of the listed attributes and that attribute is callable.
    """
    d = dict()
    assert has_any_callables(d,'get','keys','items','values','foo') is True
    assert has_any_callables(d,'has_key','foo','bar') is False
    assert has_any_callables(d,'values','keys') is True
    assert has_any_callables(d,[1,2,3],'values') is False



# Generated at 2022-06-13 20:49:05.018504
# Unit test for function has_callables
def test_has_callables():
    """Unit test for function has_callables
    """
    msg = f'from flutils.objutils import has_callables'
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') == True, msg

# Generated at 2022-06-13 20:49:08.423349
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    assert has_callables(obj, 'get', 'keys', 'items', 'values') is True
    assert has_callables(obj, 'get', 'keys', 'items', 'values', 'updat') is False



# Generated at 2022-06-13 20:49:13.251196
# Unit test for function has_any_callables
def test_has_any_callables():
    assert (
        has_any_callables(
            dict(),
            'get',
            'keys',
            'values',
            'items',
            'foo'
        ) is True
    )



# Generated at 2022-06-13 20:49:15.343617
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'items', 'values') is False



# Generated at 2022-06-13 20:49:20.266232
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:49:29.762470
# Unit test for function has_any_callables
def test_has_any_callables():
    ''' Function which checks the functionality of the ``has_any_callables`` function
        of flutils.objutils.

        Returns:
            :data:`True <typing.True>` if the ``has_any_callables`` function of flutils.objutils
            is working; :data:`False <typing.False>` otherwise.
    '''

    from flutils.objutils import has_any_callables

    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')

    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')

    assert has_any_callables(obj, 'a', 'b')

    return True


# Generated at 2022-06-13 20:49:33.636302
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')


# Generated at 2022-06-13 20:50:27.256568
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values') is True
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'foo') is True
    assert has_any_callables(dict(), 'foo', 'foo', 'foo') is False
    assert has_any_callables(list(), 'append') is True
    assert has_any_callables(True) is False
    assert has_any_callables(1) is False
    assert has_any_callables('foo', 'upper') is True



# Generated at 2022-06-13 20:50:37.886043
# Unit test for function has_any_callables
def test_has_any_callables():
    from types import FunctionType
    def foo():
        pass

    class Foo:
        def bar(self):
            pass
    obj = dict(a=1, b=2)
    assert has_any_callables(obj,'get','keys','items','values','foo') is True
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values',foo) is True
    assert has_any_callables(obj,foo) is True
    assert has_any_callables(Foo,foo) is False
    assert has_any_callables(Foo(),foo) is True
    assert has_any_callables(Foo,'bar') is True

# Generated at 2022-06-13 20:50:45.871098
# Unit test for function has_callables
def test_has_callables():
    obj = dict(a=1, b=2)
    assert has_callables(obj, 'keys', 'items', 'values', 'get') is True
    assert has_callables(obj, 'keys', 'items', 'values', 'set') is False
    assert has_callables(obj, 'keys', 'items', 'values', 'foo') is False
    assert has_callables(obj, 'foo', 'bar', 'baz') is False


# Generated at 2022-06-13 20:50:50.949925
# Unit test for function has_any_callables
def test_has_any_callables():
    test_case = [
        (True, dict(), 'get', 'keys', 'items', 'values', 'foo'),
        (False, dict(), 'get', 'keys', 'items', 'values', 'foo2'),
        (False, {}, 'get', 'keys', 'items', 'values', 'foo')
    ]
    for case in test_case:
        assert has_any_callables(*case[1:]) == case[0]



# Generated at 2022-06-13 20:51:03.457697
# Unit test for function has_callables
def test_has_callables():
    """Unit test for function has_callables"""
    class Foo:
        def __init__(self, a, b):
            self.a = a
            self.b = b

        def test(self):
            pass

        def __str__(self):
            return 'a: %s, b: %s' % (self.a, self.b)

        def __repr__(self):
            return "<Foo: %s>" % self

    obj = Foo(1, 1)
    print(has_callables(obj, 'a', 'b'))
    print(has_callables(obj, 'test'))
    print(has_callables(obj, 'test', '__repr__'))
    print(has_callables(obj, 'test', '___repr__'))

# Generated at 2022-06-13 20:51:06.196027
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:51:07.797896
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')



# Generated at 2022-06-13 20:51:15.279069
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import ChainMap
    assert has_any_callables(dict(),'get','keys','items','values') == True
    assert has_any_callables(ChainMap(),'get','keys','items','values') == True
    assert has_any_callables(set(),'get','keys','items','values') == False
    assert has_any_callables(set(),'intersection','union','difference') == True


# Generated at 2022-06-13 20:51:27.537745
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test function has_any_callables."""
    from flutils.objutils import has_any_callables
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_any_callables(list(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(list(), 'get', 'keys', 'items', 'values')
    assert has_any_callables(set(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(set(), 'get', 'keys', 'items', 'values')


# Generated at 2022-06-13 20:51:32.371207
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo')
    assert not has_any_callables(dict(),'get','keys','items','values','foo','__setitem__')
