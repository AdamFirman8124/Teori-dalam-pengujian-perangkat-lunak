

# Generated at 2022-06-13 20:43:21.634479
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import deque
    from collections.abc import KeysView, ValuesView, UserList
    from flutils.objutils import (
        has_any_callables
    )
    dq = deque([1, 2, 3])
    assert has_any_callables(dq, 'append', 'pop')
    assert has_any_callables(dq, 'popleft', 'appendleft')
    assert has_any_callables(dq, 'remove')
    assert has_any_callables(dq, 'get')

    assert not has_any_callables(dq, 'foo')
    assert not has_any_callables(dq, 'foo', 'bar')

    assert has_any_callables([1, 2, 3], 'append', 'pop')


# Generated at 2022-06-13 20:43:31.717308
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_any_callables(dict(), 'keys', 'items', 'values')
    assert has_any_callables(dict(), 'items', 'values')
    assert has_any_callables(dict(), 'values')
    assert has_any_callables(dict(), 'values') is False
    assert has_any_callables(dict(), 'items') is False



# Generated at 2022-06-13 20:43:41.659752
# Unit test for function has_attrs
def test_has_attrs():
    import pytest
    from . import objutils

    assert has_attrs(dict(),'get','keys','items','values') is True
    assert has_attrs(dict(),'get','keys','items','values','something') is False
    assert has_attrs(1,'__add__') is True
    assert has_attrs(1,'__add__','__sub__') is False
    assert has_attrs(dict(),'aaa','bbb','ccc') is False



# Generated at 2022-06-13 20:43:53.275914
# Unit test for function has_callables
def test_has_callables():
    assert has_callables('string', 'split') is True
    assert has_callables('string', 'split', 'join') is True
    assert has_callables('string', 'split', 'join', 'foo') is False
    assert has_callables('string', 'foo', 'bar') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_callables(dict(), 'foo', 'bar') is False
    assert has_callables({}, 'get', 'keys', 'items', 'values') is False
    assert has_callables([], 'get', 'keys', 'items', 'values') is False

# Generated at 2022-06-13 20:43:57.063994
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'keys', 'values', 'items') == True
    assert has_any_callables('this is a string', 'something') == False
    assert has_any_callables(None, 'some_method') == False
    assert has_any_callables(1, 'some_method') == False


# Generated at 2022-06-13 20:44:01.222359
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True


# Generated at 2022-06-13 20:44:06.032984
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'update') is False



# Generated at 2022-06-13 20:44:15.701632
# Unit test for function has_callables
def test_has_callables():
    import unittest
    from collections import (
        ChainMap,
        Counter,
        OrderedDict,
        UserDict,
        UserString,
    )
    from typing import (
        NoReturn,
        Type,
        Union,
        Tuple,
        List,
        Iterable,
    )
    from datetime import (
        datetime,
        timedelta,
    )
    from decimal import Decimal
    from collections import UserList
    from collections.abc import (
        Iterator,
        KeysView,
        ValuesView,
    )
    from dataclasses import dataclass

    @dataclass
    class PersonClass:
        name: str
        age: int

    class PersonClass:
        def __init__(self, name: str, age: int):
            self._name = name

# Generated at 2022-06-13 20:44:24.515281
# Unit test for function has_callables
def test_has_callables():
    assert has_callables({}, 'items') is True
    assert has_callables({}, 'get') is True
    assert has_callables({}, 'items') is True
    assert has_callables({}, 'keys') is True
    assert has_callables({}, 'pop') is True
    assert has_callables({}, 'popitem') is True
    assert has_callables({}, 'setdefault') is True
    assert has_callables({}, 'update') is True
    assert has_callables({}, 'values') is True


if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    from pytest import main
    main([__file__])

# Generated at 2022-06-13 20:44:30.966449
# Unit test for function has_attrs
def test_has_attrs():
    obj = dict(foo='bar')
    assert has_attrs(obj, 'get', 'keys', 'items', 'values') is True
    assert has_attrs(obj, 'get', 'frobnicate', 'items', 'values') is False
    return


# Generated at 2022-06-13 20:44:34.897501
# Unit test for function has_callables
def test_has_callables():
    '''Unit test has_callables'''
    assert has_callables(dict(),'get','keys','items','values')


# Generated at 2022-06-13 20:44:37.521481
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables({}, 'values', 'items', 'keys', 'get')



# Generated at 2022-06-13 20:44:41.556052
# Unit test for function has_callables
def test_has_callables():
    class A(object):
        @staticmethod
        def func1():
            return True

        def func2(self):
            return False
    a = A()
    k = has_callables(a,'func1','func2')
    assert k is True

# Generated at 2022-06-13 20:44:44.756668
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:44:49.425248
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True


# Generated at 2022-06-13 20:44:54.446467
# Unit test for function has_callables
def test_has_callables():
    """Unit test for function has_callables function.
    """
    import doctest
    doctest.testmod(verbose=True, extraglobs=None)

# Generated at 2022-06-13 20:45:00.652465
# Unit test for function has_any_callables
def test_has_any_callables():
    d = dict(a=1, b=2)
    assert has_any_callables(d, 'get', 'keys', 'values') is True
    assert has_any_callables(d, 'get', 'keys', 'foo', 'Bar') is False
    assert has_any_callables(d, 'foo', 'Bar') is False



# Generated at 2022-06-13 20:45:05.563689
# Unit test for function has_callables
def test_has_callables():
    assert (has_callables(dict(), 'get', 'keys', 'items', 'values') == True)
    assert (has_callables(dict(), 'items', 'keys', 'values', 'get', 'something') == False)



# Generated at 2022-06-13 20:45:11.546389
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    # This function returns True if any of the named methods exist
    # and are callable.
    assert has_any_callables(dict(), 'foo', 'bar', 'values') is False
    assert has_any_callables(dict(), 'foo', 'bar', 'values', 'items') is True



# Generated at 2022-06-13 20:45:20.351076
# Unit test for function has_any_callables
def test_has_any_callables():
    from functools import partial
    from collections import deque
    class Dummy:
        foo = 'bar'
    assert has_any_callables(Dummy, 'foo', 'bar') is False
    assert has_any_callables(Dummy, 'foo', 'bar', '__class__', '__doc__') is False
    assert has_any_callables(deque, 'foo', 'bar') is False
    assert has_any_callables(Dummy, 'foo', 'bar', 'pop') is False
    assert has_any_callables({}, 'get', 'keys', 'values') is True
    assert has_any_callables({}, 'foo', 'bar') is False
    assert has_any_callables({}, 'foo', 'bar', '__class__', '__doc__') is False
    assert has_

# Generated at 2022-06-13 20:45:30.440005
# Unit test for function has_callables
def test_has_callables():
    assert has_callables('foo', 'upper', 'lower') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items') is True
    assert has_callables(dict(), 'get', 'keys') is True
    assert has_callables(dict(), 'get') is True
    assert has_callables(dict(), 'something') is False
    assert has_callables(dict(), 'lower') is False



# Generated at 2022-06-13 20:45:33.496786
# Unit test for function has_any_callables
def test_has_any_callables():
    assert not has_any_callables(dict(), 'foo')
    assert has_any_callables(dict(), 'get')



# Generated at 2022-06-13 20:45:41.359382
# Unit test for function has_callables
def test_has_callables():
    # noinspection PyUnresolvedReferences
    from collections import ChainMap
    obj = ChainMap(dict(a=1, b=2))
    assert has_callables(obj, 'get', 'keys', 'values', 'items', 'update') is True
    assert has_callables(obj, 'get', 'keys', 'values', 'items', 'something') is False
    assert has_callables(obj, 'get', 'keys', 'values', 'update', 'something') is False



# Generated at 2022-06-13 20:45:51.467398
# Unit test for function has_callables
def test_has_callables():
    _has_callables = has_callables
    assert (_has_callables(dict(a=1, b=2), 'get', 'keys', 'items', 'values'))
    assert (not _has_callables(dict(a=1, b=2), 'set', 'keys', 'items', 'values'))
    assert (not _has_callables(dict(a=1, b=2), 'get', 'set', 'items', 'values'))
    assert (not _has_callables(dict(a=1, b=2), 'get', 'keys', 'set', 'values'))
    assert (not _has_callables(dict(a=1, b=2), 'get', 'keys', 'items', 'set'))

# Generated at 2022-06-13 20:45:53.489905
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items', 'foo') == True



# Generated at 2022-06-13 20:45:57.146938
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections import UserList

    test_obj = UserList()
    assert has_any_callables(test_obj, 'append') == True


# Generated at 2022-06-13 20:46:01.506234
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict()
    obj.foo = lambda: True
    assert has_any_callables(obj,'get', 'keys', 'items', 'values', 'foo') == True


# Generated at 2022-06-13 20:46:06.562575
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo', '__dir__') is False


# Generated at 2022-06-13 20:46:15.468511
# Unit test for function has_callables
def test_has_callables():
    from collections import OrderedDict
    assert has_callables([], 'append', 'count') is True
    assert has_callables(user_list, 'append', 'count') is True
    assert has_callables(user_list, 'foo', 'bar') is False
    assert has_callables(user_dict, 'foo', 'bar') is False
    assert has_callables(OrderedDict(), 'keys', 'items') is True


test_has_callables()

# Generated at 2022-06-13 20:46:18.759725
# Unit test for function has_callables
def test_has_callables():
    obj = dict()
    assert(has_callables(obj, 'get','keys','items','values')) is True
    assert(has_callables(obj, 'get','keys','items','values','something')) is False



# Generated at 2022-06-13 20:46:26.289153
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True


# Generated at 2022-06-13 20:46:31.430063
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is False
    return None


# Generated at 2022-06-13 20:46:37.773692
# Unit test for function has_callables
def test_has_callables():
    """Tests function has_callables

    Examples:
        >>> from flutils.objutils import has_callables
        >>> has_callables(dict,'get','keys','items','values')
        True
    """
    assert has_callables(dict(),'get','keys','items','values') == True



# Generated at 2022-06-13 20:46:48.292881
# Unit test for function has_callables
def test_has_callables():
    class Callables:
        def __init__(self):
            self.val = None
        def get(self):
            """Retrieve the stored value."""
            return self.val
        def set(self, value):
            """Set the stored value."""
            self.val = value
    result = has_callables(Callables(), 'get', 'set')
    assert result is True, 'has_callables: {0}'.format(result)
    result = has_callables(Callables(), 'get', 'set', 'foo')
    assert result is False, 'has_callables: {0}'.format(result)
    result = has_callables(Callables(), 'set', 'foo')
    assert result is False, 'has_callables: {0}'.format(result)

# Generated at 2022-06-13 20:47:00.051594
# Unit test for function has_callables
def test_has_callables():
    from collections import deque
    from collections.abc import (
        Iterator,
        KeysView,
        ValuesView,
    )

    from flutils.tests.constants import (
        ONE,
        TWO,
    )

    from flutils.tests.test_fixture import (
        LiteralCallable,
        LiteralClass,
        LiteralSubclass,
    )


# Generated at 2022-06-13 20:47:06.374154
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict(), 'get', 'keys', 'items', 'foo') is False
    assert has_callables(dict(), 'foo', 'keys', 'items', 'values') is False
    assert has_callables(dict(), 'get', 'foo', 'items', 'values') is False
    assert has_callables(dict(), 'get', 'keys', 'foo', 'values') is False
    assert has_callables(dict(), 'get', 'keys', 'items', 'foo') is False


# Generated at 2022-06-13 20:47:10.568895
# Unit test for function has_any_callables
def test_has_any_callables():
    
    class X:
        @staticmethod
        def foo():
            pass
        def bar():
            pass
    
    assert has_any_callables(X, 'foo', 'bar')
    assert has_any_callables(X(), 'foo', 'bar')

# Generated at 2022-06-13 20:47:15.171878
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)
    assert has_any_callables(obj, 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:47:19.053258
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo', 'bar', 'baz') is True


# Generated at 2022-06-13 20:47:23.329402
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:47:39.434578
# Unit test for function has_callables
def test_has_callables():
    assert has_callables(dict(), 'get', 'keys', 'items', 'values') == True
    assert has_callables(set(), 'get', 'keys', 'items', 'values') == False
    assert has_callables(frozenset(), 'get', 'keys', 'items', 'values') == False


# Generated at 2022-06-13 20:47:48.748575
# Unit test for function has_callables
def test_has_callables():
    from collections import OrderedDict
    assert has_callables(dict, '__contains__', '__getitem__') is True
    assert has_callables(dict, 'get', 'keys', 'items', 'values') is True
    assert has_callables(OrderedDict, 'get', 'keys', 'items', 'values') is True
    assert has_callables(dict, '__contains__', '__getitem__', '') is False
    assert has_callables(dict, 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_callables(OrderedDict, 'get', 'keys', 'items', 'values', 'foo') is False
    assert has_callables([], 'count', 'append', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort')

# Generated at 2022-06-13 20:47:52.064031
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = get_configs()
    print(has_any_callables(obj, 'get', 'keys', 'values', 'items', 'generate_url'))

# Unit test has_attrs

# Generated at 2022-06-13 20:47:56.818699
# Unit test for function has_callables
def test_has_callables():
    # given
    obj = dict(a=1, b=2)

    # when
    has_callables_func = has_callables(
        obj,
        'get',
        'keys',
        'items',
        'values'
    )

    # then
    assert has_callables_func is True


# Generated at 2022-06-13 20:48:01.262747
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')



# Generated at 2022-06-13 20:48:06.784249
# Unit test for function has_callables
def test_has_callables():
    d = dict(a=1, b=2)
    assert has_any_callables(d, 'get', 'keys', 'items', 'values') is True
    assert has_callables(d, 'get', 'keys', 'items', 'values') is True
    assert has_callables(d, 'foo') is False



# Generated at 2022-06-13 20:48:18.009390
# Unit test for function has_callables
def test_has_callables():
    class Foo:
        def __init__(self):
            self.foo = True

        def __call__(self):
            return 'bar'

    obj = Foo()
    assert has_callables(obj, '__call__') is True, \
        'The function should return True.'
    assert has_callables(obj, 'foo') is False, \
        'The function should return False.'
    assert has_callables(obj, '__call__', 'foo') is False, \
        'The function should return False.'
    assert has_callables(obj, 'foo', '__call__') is True, \
        'The function should return True.'


# Generated at 2022-06-13 20:48:25.728572
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values')
    assert has_any_callables(dict(), 'foo') is False


# Unit test function has_any_attrs

# Generated at 2022-06-13 20:48:35.438143
# Unit test for function has_any_callables
def test_has_any_callables():
    """
    Unit test for function has_any_callables
    """
    import pytest
    setdict = {'1': 1,
               '2': 2}
    obj = dict()
    assert has_any_callables(obj, 'get') is True
    assert has_any_callables(obj, 'get', 'foo') is True
    assert has_any_callables(setdict, 'get') is True
    assert has_any_callables(setdict, 'get', 'foo') is True
    assert has_any_callables(100, 'get', 'foo') is False

    with pytest.raises(AttributeError):  # pragma: no cover
        has_any_callables(setdict, 'foo')
    with pytest.raises(AttributeError):  # pragma: no cover
        has_

# Generated at 2022-06-13 20:48:41.672341
# Unit test for function has_any_callables
def test_has_any_callables():
    if (has_any_callables(dict(),'get','keys','items','values','foo') == True):
        print("test_has_any_callables: passed")
    else:
        print("test_has_any_callables: failed")


# Generated at 2022-06-13 20:49:15.476460
# Unit test for function has_any_callables
def test_has_any_callables():
    """Test ``has_any_callables``."""
    assert has_any_callables(dict(), 'get', 'keys', 'items') is True
    assert has_any_callables(dict(), 'something', 'something else') is False
    assert has_any_callables(dict(), 'something', 'something else', 'foo') is False
    assert has_any_callables(dict(), 'something', 'something else', 'keys') is True
# end of test_has_any_callables


# Generated at 2022-06-13 20:49:20.402870
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(dict(),'foo') is False


# Generated at 2022-06-13 20:49:29.835981
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(dict(),'get','keys','items','values','foo')==True)
    assert(has_any_callables(dict(),'get','keys','items','values','foo','list')==False)
    assert(has_any_callables([1, 2, 3], 'pop', 'remove', 'sort', 'append', 'reverse') == True)
    assert(has_any_callables([1, 2, 3], 'pop', 'remove', 'sort', 'append', 'reverse', 'hi') == True)
    assert(has_any_callables([1, 2, 3], 'pop', 'remove', 'sort', 'append', 'reverse', 'hi', 'list') == False)

# Generated at 2022-06-13 20:49:41.441663
# Unit test for function has_callables
def test_has_callables():
    obj1 = {1,2,3}
    obj2 = [1,2,3]
    obj3 = (1,2,3)
    obj4 = "hello"
    assert has_callables(obj1,"difference","add","remove")
    assert has_callables(obj2,"extend","reverse","insert")
    assert has_callables(obj3,"count","index","__add__")
    assert not has_callables(obj4,"count","index","__add__")
    assert not has_callables(obj3, "foo", "bar")
    assert not has_callables(obj4, "foo", "bar")
    assert not has_callables(obj1, "foo", "bar")
    assert not has_callables(obj2, "foo", "bar")


# Generated at 2022-06-13 20:49:53.304828
# Unit test for function has_any_callables
def test_has_any_callables():
    from collections.abc import Mapping
    from collections import OrderedDict
    assert has_any_callables(dict(),'get','keys','items','values','foo') is True
    assert has_any_callables(OrderedDict(),'get','keys','items','values','foo') is True
    assert has_any_callables(Mapping,'get','keys','items','values','foo') is True
    assert has_any_callables(Mapping,'get','keys','items','values','foo') is True
    assert has_any_callables(Mapping.__subclasses__(),'__subclasses__','foo') is True
    assert has_any_callables(Mapping.__subclasses__(),'__subclasses__','__repr__') is True

# Generated at 2022-06-13 20:50:07.429348
# Unit test for function has_any_callables
def test_has_any_callables():
    """Unit tests for function has_any_callables."""
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo', 'bar') is True
    assert has_any_callables(dict(), 'getattr', 'keys', 'items', 'values', 'foo', 'bar') is True
    assert has_any_callables(dict(), 'getattr', 'keys', 'items', 'values', 'foo', 'bar', 'buz') is False



# Generated at 2022-06-13 20:50:13.697174
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables([], 'get', 'keys', 'items', 'values', 'append') is True
    assert has_any_callables(str(), 'get', 'keys', 'items', 'values', 'foo') is False



# Generated at 2022-06-13 20:50:23.146632
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(a=1), 'get', 'keys', 'items', 'values') is True
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', '__init__') is False
    assert has_any_callables(dict(), 'get', 'keys', 'items', 'values', '_dict__') is False
    assert has_any_callables(list(), 'append', 'insert', 'pop') is True
    assert has_any_callables(list(), 'append', 'insert', 'pop', 'foo') is True
    assert has

# Generated at 2022-06-13 20:50:25.268560
# Unit test for function has_any_callables
def test_has_any_callables():
    assert (has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo')
            is True)



# Generated at 2022-06-13 20:50:27.973319
# Unit test for function has_any_callables
def test_has_any_callables():
    from flutils.objutils import has_any_callables
    from collections import defaultdict
    obj = defaultdict(list)
    assert has_any_callables(obj, "append") is True


# Generated at 2022-06-13 20:51:44.609642
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(),'get','keys','items','values','foo') == True


# Generated at 2022-06-13 20:51:50.386097
# Unit test for function has_any_callables
def test_has_any_callables():
    class test_obj(object):
        def __init__(self):
            self.object = None
        def call(self):
            return "call"
    assert has_any_callables(test_obj, "object") == False
    assert has_any_callables(test_obj, "call") == True


# Generated at 2022-06-13 20:52:01.347432
# Unit test for function has_any_callables
def test_has_any_callables():
    obj = dict(a=1, b=2)

    assert has_any_callables(obj, 'keys', 'items', 'values', 'foo')
    assert has_any_callables(obj.keys(), '__next__', '__getitem__', 'foo')
    assert has_any_callables(obj.values(), '__next__', '__getitem__', 'foo')
    assert has_any_callables(obj.items(), '__next__', '__getitem__', 'foo')
    assert has_any_callables(obj.keys(), '__getitem__', 'items') is False


# Generated at 2022-06-13 20:52:11.976669
# Unit test for function has_any_callables
def test_has_any_callables():
    # Unit test for function has_callables
    assert has_any_callables('foobar', 'replace', 'rjust', 'rstrip')
    assert not has_any_callables('foobar', 'replace', 'rjust', 'rstrip', 'findall')

    assert has_any_callables(123, '__add__', '__mul__', '__rdiv__')
    assert not has_any_callables(123, '__add__', '__mul__', '__rdiv__', '__slash__')


# Generated at 2022-06-13 20:52:13.911307
# Unit test for function has_any_callables
def test_has_any_callables():
    pass


# Generated at 2022-06-13 20:52:21.742602
# Unit test for function has_any_callables
def test_has_any_callables():
    import collections
    import numbers
    import os
    import random
    import re
    import statistics
    import sys
    import time
    list_of_objs = [
        collections, collections.Counter, collections.OrderedDict,
        collections.UserDict, collections.UserList, collections.UserString,
        numbers.Rational, os.DirEntry, os.PathLike, os.fsencode, os.fsdecode,
        random.SystemRandom, random.WichmannHill, re.Match, re.Pattern,
        statistics.StatisticsError, sys.breakpointhook, sys.code_info, time
    ]
    for each_obj in list_of_objs:
        assert has_any_callables(each_obj, 'denominator', 'numerator', 'foo')

# Generated at 2022-06-13 20:52:28.748958
# Unit test for function has_any_callables
def test_has_any_callables():
    # Case 1: true
    obj1 = dict()
    assert has_any_callables(obj1,'get','keys','foo') == True
    
    # Case 2: false
    obj3 = str()
    assert has_any_callables(obj3,'get','keys','foo') == False



# Generated at 2022-06-13 20:52:34.835387
# Unit test for function has_any_callables
def test_has_any_callables():
    # Create a dummy class to test this function
    class dummy(object):
        def foo(self):
            pass
        def bar(self):
            pass
    # Create an instance of dummy
    d = dummy()
    # Create an iterable with the methods
    methods = ('foo', 'bar')
    for method in methods:
        # Check that has_any_callables return True if attribute exists
        # and is callable
        assert has_any_callables(d, method, 'baz') is True,\
            "has_any_callables should return True if any method is callable"


# Generated at 2022-06-13 20:52:37.653042
# Unit test for function has_any_callables
def test_has_any_callables():
    assert(has_any_callables(dict(), 'get', 'keys', 'items', 'values', 'foo') == True)


# Generated at 2022-06-13 20:52:46.339436
# Unit test for function has_any_callables
def test_has_any_callables():
    assert has_any_callables(dict(), 'get', 'keys', 'values', 'items', 'foo')
    assert has_any_callables(dict(),'get')
    assert has_any_callables(dict(),'items')
    assert has_any_callables(dict(),'keys')
    assert has_any_callables(dict(),'values')
    assert has_any_callables('','join')
    assert has_any_callables('','split')
    assert has_any_callables('','strip')
    assert has_any_callables('','upper')
    assert has_any_callables(dict(),'get', 'keys', 'values', 'items', 'foo')
    assert not has_any_callables('','foo')
    assert not has_any_callables('','foo','bar')