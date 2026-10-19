

# Generated at 2022-06-13 20:32:51.731533
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method `__get__` of class `cached_property`."""

    # Case: object argument is None
    assert cached_property(lambda x: 5).__get__(None) is not None

    # Case: object has not been computed
    obj = MyClass()
    _ = obj.non_cached_property_value
    assert obj.non_cached_property_value == 5

    # Case: cached property has not been computed
    _ = obj._cached_property_value
    assert obj._cached_property_value == 6

    # Case: cached property has been computed
    _ = obj._cached_property_value
    assert obj._cached_property_value == 6

    # Case: delete cached property and compute again
    del obj._cached_property_value
    _ = obj._cached_

# Generated at 2022-06-13 20:33:04.093133
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import patch

    from flutils.decorators import cached_property

    # noinspection PyShadowingNames
    class TestClass:

        @cached_property
        def x(self):
            return 42

    class MockDict(dict):
        def __setitem__(self, key, value):
            self.key = key
            self.value = value
            return super().__setitem__(key, value)

    # Test with a method that is not a coroutine
    obj = TestClass()
    with patch('flutils.decorators.cached_property.__get__',
               wraps=cached_property.__get__) as mock_get:
        result = cached_property.__get__(TestClass.x, obj, TestClass)
    assert mock_get.called is True

# Generated at 2022-06-13 20:33:09.195828
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self, y=1):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(y=7)
    assert obj.y == 6



# Generated at 2022-06-13 20:33:21.682805
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """A property for testing :obj:`~flutils.decorators.cached_property`."""
            return self.x + 1

    # Test that calling __get__ twice works as expected
    obj = MyClass()
    assert obj.y == 6
    assert obj.y == 6

    # Test that the property documentation is available
    assert obj.y.__doc__ == 'A property for testing :obj:`~flutils.decorators.cached_property`.'

    # Test that a property that is implemented as a coroutine works as expected
    # Reset the class object
    MyClass = None


# Generated at 2022-06-13 20:33:33.664210
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    interface = 0
    obj = object()
    cls = type(obj)
    prop = cached_property(None)
    prop.__dict__['func'] = 'func'
    prop2 = prop.__get__(obj, cls)
    assert prop2 == 'func'

    prop.__dict__['func'] = lambda x: x
    prop2 = prop.__get__(obj, cls)
    assert prop2 == obj
    assert obj.__dict__['func'] == obj

    obj = type('obj', (), {'foo': 'bar'})()
    prop2 = prop.__get__(obj, cls)
    assert prop2 is obj.foo



# Generated at 2022-06-13 20:33:45.266558
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property
    """

    import sys

    import pytest

    if sys.version_info >= (3, 8):
        pytest.skip('Method not available with Python 3.8 or greater')

    import asyncio

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    obj2 = MyClass()
    assert obj2.y == 6

    from unittest.mock import patch, MagicMock

    async def mock_async_func(*args):
        return MagicMock()


# Generated at 2022-06-13 20:33:55.680829
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""
    class Test:
        def __init__(self, x: int = 5):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x + 2

    test = Test()
    assert test.y == test.x + 1
    assert test.z == test.x + 2

    test.x = 10
    assert test.y == test.x + 1
    assert test.z == test.x + 2

# Generated at 2022-06-13 20:34:06.375423
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    import unittest

    class PropertyTest(unittest.TestCase):

        def setUp(self):
            self.obj = MyClass()
            self.name = 'y'

        def test_retrieve_value(self):
            self.assertEqual(getattr(self.obj, self.name), 6)

        def test_update_value_invokes_func(self):
            self.assertEqual(self.obj.x, 5)
            self.obj.x = 10
            self.assertEqual(getattr(self.obj, self.name), 11)

        def test_delete_attribute(self):
            self.assertEqual(getattr(self.obj, self.name), 6)
            del self.obj.y

# Generated at 2022-06-13 20:34:15.483687
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for :obj:`cached_property.__get__` method.

    *New in version 0.2.0*

    """

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    async def async_fn(obj):
        await asyncio.sleep(0)
        return obj.x + 1

    class MyAsyncClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return async_fn(self)

    obj1 = MyAsyncClass()
    assert asyncio.iscoroutinefunction(obj1.y)

# Generated at 2022-06-13 20:34:24.674680
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.

    :return: No return.
    :rtype: None
    """

    class MyClass:

        @cached_property
        def x(self):
            return 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.x == 5
    assert obj.y == 6
    assert obj.__dict__["x"] == 5
    assert obj.__dict__["y"] == 6
    assert cached_property.__get__(MyClass.x, obj, MyClass) == 5
    assert cached_property.__get__(MyClass.y, obj, MyClass) == 6
    assert cached_property.__get__(MyClass.x, obj, None) is MyClass

# Generated at 2022-06-13 20:34:37.177769
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""
    import sys

    sys.path.append("..")
    from flutils.decorators import cached_property

    sys.path.pop()

    class TestCachedProp(object):
        def __init__(self):
            self._x = None

        @cached_property
        def x(self):
            print("x was called.")
            return 42

    t = TestCachedProp()
    assert t.x == 42
    assert t.x == 42
    assert t._x == 42
    t._x = 50
    assert t.x == 50


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-13 20:34:40.526752
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import random

    class MyClass:
        def __init__(self):
            self.x = random.randint(0, 100)

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 101

# Generated at 2022-06-13 20:34:44.825145
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:34:55.316422
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from docutils.statemachine import ViewList
    from docutils.transforms.universal import SmartQuotes

    # class Mock:
    #     x = 5
    #
    #     @cached_property
    #     def y(self):
    #         return self.x + 1
    #
    #     @cached_property
    #     async def z(self):
    #         return self.x + 1
    #
    #     @cached_property
    #     def zz(self):
    #         return self.x + 1
    #
    # obj = Mock()
    # print(obj.y)
    # print(obj.z)
    # print(obj.zz)

    vl = ViewList()
    # for line in ["""``'``", """"``'``""", """``"'

# Generated at 2022-06-13 20:35:09.484758
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property

    """
    from contextlib import contextmanager

    class MyTestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    @contextmanager
    def test_obj():
        obj = MyTestClass()
        try:
            yield obj
        finally:
            del obj

    with test_obj() as obj:
        # The first time, we expect the property to be computed:
        assert obj.y == 6
        # The second time, we expect the value to be taken directly from obj.__dict__
        # pylint: disable=protected-access
        assert obj.__dict__["y"] == 6



# Generated at 2022-06-13 20:35:13.686557
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:35:28.437760
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        @cached_property
        def cached_attr(self):
            return 5

        async def async_cached_attr(self):
            return 5

    obj = MyClass()
    assert not hasattr(obj, 'cached_attr')
    assert obj.cached_attr == 5
    assert hasattr(obj, 'cached_attr')
    del obj.cached_attr
    assert not hasattr(obj, 'cached_attr')
    assert obj.cached_attr == 5
    assert hasattr(obj, 'cached_attr')

    assert not hasattr(obj, 'async_cached_attr')
    assert asyncio.iscoroutine(obj.async_cached_attr)
    assert not hasattr(obj, 'async_cached_attr')
    obj.__

# Generated at 2022-06-13 20:35:34.579670
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Unit test for method __get__ of class cached_property """
    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert isinstance(obj.y, int)
    assert obj.y == 6

# Generated at 2022-06-13 20:35:35.951803
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass


# Generated at 2022-06-13 20:35:45.305532
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import mock

    # Test where obj is None
    cp = cached_property(mock.MagicMock())
    assert cp == cp.__get__(None, None)

    # Test where self.func is a coroutine function
    cp = cached_property(mock.MagicMock(side_effect=asyncio.iscoroutinefunction))
    cp.func.__name__ = 'some_function'
    cp.func.__dict__['__qualname__'] = 'some_module.some_function'
    cp.func.__dict__['__module__'] = 'some_module'
    obj = mock.MagicMock()
    obj.__dict__ = {}
    assert isinstance(cp.__get__(obj, None), asyncio.coroutine)

    # Test where self.func is not a cor

# Generated at 2022-06-13 20:35:53.912184
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        async def z(self):
            return self.x + 1

    m = MyClass()
    assert m.y == m.__dict__['y']
    assert m.y == 6

    m.x = 10
    assert m.y == 6

    assert not asyncio.iscoroutinefunction(m.y)
    assert asyncio.iscoroutinefunction(m.z)



# Generated at 2022-06-13 20:36:02.186438
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # <obj>.y (no value in <obj>.__dict__)
    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6

    # <obj>.y again
    assert obj.y == 6
    assert obj.__dict__['y'] == 6

    # delete <obj>.y
    del obj.y
    assert 'y' not in obj.__dict__
    assert obj.y == 6


# Generated at 2022-06-13 20:36:08.841846
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6


# Generated at 2022-06-13 20:36:14.652101
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property
    """

    def func(obj):
        return obj.x + 1

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return func(self)

    obj = MyClass()
    assert obj.y == func(obj)

# Generated at 2022-06-13 20:36:17.850867
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached_property.__get__"""

    class Test:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    assert Test().y == 6



# Generated at 2022-06-13 20:36:29.738646
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    def test_regular():
        obj = MyClass()
        assert obj.y == 6
        for _ in range(100):
            assert obj.y == 6

    def test_regular_with_deletion():
        obj = MyClass()
        assert obj.y == 6
        for _ in range(100):
            assert obj.y == 6
        del obj.y
        del obj.y
        assert obj.y == 6

    def test_coroutine():
        obj = MyClass()
        coroutine = test_cached_property___get__.test_coroutine

# Generated at 2022-06-13 20:36:35.064976
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test(object):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    test = Test()
    assert test.y == 6



# Generated at 2022-06-13 20:36:41.433893
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    import pytest
    from flutils import decorators

    class TestClass:

        def __init__(self):
            self.x = 5

        @decorators.cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6

    del obj.y
    assert obj.y == 6

    obj.x = 7
    assert obj.y == 8



# Generated at 2022-06-13 20:36:44.295309
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6


# Generated at 2022-06-13 20:36:53.123150
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for :obj:`~flutils.decorators.cached_property.__get__`."""
    class Class:
        @cached_property
        def prop(self):
            """Test property."""
            return 42
    assert Class.prop.__doc__ == "Test property."
    assert Class.prop.__name__ == "prop"
    obj = Class()
    assert obj.prop == 42
    obj.prop = 24
    assert obj.prop == 24
    del obj.prop
    assert obj.prop == 42


if __name__ == "__main__":
    try:
        import pytest
    except ImportError:
        print("PyTest is not installed.  Unable to run unit tests.")
    else:
        pytest.main(__file__)

# Generated at 2022-06-13 20:36:59.478845
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:37:11.695984
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    import re

    from flutils.decorators import cached_property


    class MyClass:

        def __init__(self):
            self.value = 5

        @cached_property
        def y(self):
            return self.value + 1

    obj = MyClass()

    # value = obj.__dict__[self.func.__name__] = self.func(obj)
    # return value
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    assert obj.__dict__[MyClass.y.__name__] == 6
    assert obj.__dict__[re.compile(r'\d+').search(obj.__dict__).group()] == 6

    # The property cannot be set on the obj
    obj.y = 10
    assert obj.y == 6

# Generated at 2022-06-13 20:37:17.864892
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass(object):
        x = 5

        @cached_property
        def y(self):
            """Test property."""
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    obj.x += 1
    assert obj.y == 6
    del obj.y
    assert obj.y == 7

    obj = MyClass()
    assert obj.y == 6
    assert MyClass.y.__doc__ == 'Test property.'

# Generated at 2022-06-13 20:37:24.541147
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    decorated_method_name = "y"
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    original_method_value = obj.x + 1
    decorated_method = cached_property.__get__(None, MyClass)
    assert getattr(MyClass, decorated_method_name) is decorated_method
    assertMyClass = getattr(obj, decorated_method_name)
    assert decorated_method(obj) == original_method_value
    assertMyClass = getattr(obj, decorated_method_name)
    assert isinstance(obj.__dict__[decorated_method_name], asyncio.Future)
    delattr(obj, decorated_method_name)

# Generated at 2022-06-13 20:37:31.089433
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Tests for method __get__ of class cached_property
    """
    print()

    def test():
        class MyClass:

            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj = MyClass()
        assert obj.y == 6
        obj.x = 10
        assert obj.y == 6

    test()

# Generated at 2022-06-13 20:37:38.175923
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    method = find_attr_of_class(cached_property, '__get__')
    assert method is not None

    class Test:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Test()
    assert obj.y == 6


# Generated at 2022-06-13 20:37:42.527331
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:37:47.330024
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    '''
    Unit test for method __get__ of class cached_property
    '''
    @cached_property
    def y(self):
        return self.x + 1

    x = 5
    # Passing a class as well as a value
    assert y.__get__(x, int) == 6

# Generated at 2022-06-13 20:37:52.846033
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6


# Generated at 2022-06-13 20:37:57.909233
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # noinspection PyShadowingBuiltins
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    res = obj.y

    assert res == 6
    assert obj.x == 5
    assert obj.y == 6

# Generated at 2022-06-13 20:38:03.303488
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass


# Generated at 2022-06-13 20:38:10.949009
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            return self.x

        @cached_property
        def z(self):
            return "test"
    #
    obj = TestClass()
    assert 0 == obj.y
    assert 0 == obj.y
    obj.x = 1
    assert 0 == obj.y
    assert "test" == obj.z


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:38:21.791591
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    import asyncio

    class SomeClass:
        def __init__(self, y):
            self.y = y

        @cached_property
        def some_property(self):
            return self.y * 2

        @cached_property
        async def some_async_property(self):
            return self.y * 3

    c = SomeClass(2)
    # The following two lines are equivalent
    assert c.some_property == 4
    assert c.some_property == 4

    # Ditto for the following two lines
    loop = asyncio.get_event_loop()
    assert loop.run_until_complete(c.some_async_property) == 6
    assert loop.run_until_complete(c.some_async_property) == 6


# Generated at 2022-06-13 20:38:33.719414
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import sys
    from inspect import iscoroutinefunction
    from typing import Optional

    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

    class CachedProp(MyClass):

        @cached_property
        def y(self):
            return self.x + 1

        @property
        def z(self):
            return self.x + 1

    class AsyncCachedProp(MyClass):

        @cached_property
        async def y(self):
            return self.x + 1

        @property
        async def z(self):
            return self.x + 1

    class AsyncMethod(MyClass):

        async def y(self):
            return self.x + 1


# Generated at 2022-06-13 20:38:38.698503
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    obj = type('MockObject', (object,), {})()

    def _test_method(obj):
        obj.__dict__[test_cached_property___get__.__name__] = 42
        return 42

    obj.__dict__['test_cached_property___get__'] = test_cached_property(_test_method)

    # Assert method __get__ of class cached_property
    assert obj.test_cached_property___get__ == 42

# Generated at 2022-06-13 20:38:45.003415
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # GIVEN
    class X:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # WHEN
    obj = X()

    # THEN
    assert obj.y == 6


# Generated at 2022-06-13 20:38:48.920509
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self):
            self.a = 0

        @cached_property
        def add_one(self):
            self.a += 1
            return self.a

    a = A()
    assert a.add_one == 1
    assert a.add_one == 1


# Generated at 2022-06-13 20:38:55.488879
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    import inspect
    import time

    class MyClass:
        """My class."""

        def __init__(self):
            pass

        @cached_property
        def my_property(self):
            """My property."""

            return int(time.time())

    obj = MyClass()
    assert isinstance(obj, MyClass)

    property_value = obj.my_property

    assert property_value == obj.my_property

    # Attempt to delete the cached property.
    del obj.my_property

    assert property_value != obj.my_property

    # Check the doc string.
    assert inspect.getdoc(obj.__class__.my_property) == "My property."

    # Check the help string.

# Generated at 2022-06-13 20:39:01.844950
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        """Test class with a cached_property"""
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Test method"""
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6


# Generated at 2022-06-13 20:39:06.026672
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    This is a method to test `cached_property.__get__`.
    """
    from flutils.decorators import cached_property

    class ClassWithCachedProperty:

        @cached_property
        def method(self):
            return 5

    class_with_cached_property = ClassWithCachedProperty()
    assert class_with_cached_property.method == 5
    assert class_with_cached_property.method == 5



# Generated at 2022-06-13 20:39:20.639278
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:39:24.826051
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:39:39.163506
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from functools import partial

    class SomeClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 2

    my_obj = SomeClass(4)
    assert my_obj.x == 4
    assert my_obj.y == 6

    with pytest.raises(AttributeError):
        SomeClass.y

    # delete the cached property and set it to a new value
    del my_obj.y
    my_obj.y = 100
    assert my_obj.__dict__['y'] == 100

    # delete the cached property and set it to a new value using a partial
    del my_obj.y
    my_obj.__dict__[SomeClass.y.func.__name__]

# Generated at 2022-06-13 20:39:49.174213
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # arrange
    class Foo:
        def __init__(self):
            self._delay_func_ran = False

        @property
        def delay_func_ran(self):
            return self._delay_func_ran

        @cached_property
        def delay_func(self):
            self._delay_func_ran = True
            return 1

    obj = Foo()

    # act
    @asyncio.coroutine
    def run():
        return obj.delay_func

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())

    # assert
    assert obj.delay_func_ran is True

# Generated at 2022-06-13 20:40:04.031772
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Tests for method __get__ of class cached_property"""

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1
    class MyAsyncClass:
        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            return self.x + 1
    with pytest.raises(TypeError) as info:
        MyClass.y
    assert "cannot create 'weakref' of 'module' object" in str(info.value)

    obj1 = MyClass()
    assert obj1.y == 6
    assert obj1.y == 6

    obj2 = MyAsyncClass()
    loop = asyncio.get_event_loop()
   

# Generated at 2022-06-13 20:40:04.549436
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:40:08.244865
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Peak at class private method."""

    class MyClass:

        @cached_property
        def y(self):
            return 5

    obj = MyClass()
    assert isinstance(obj.__class__.y.__get__(obj, MyClass),
                      cached_property)

# Generated at 2022-06-13 20:40:19.415933
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            self.x = self.x + 1
            return self.x

    obj = MyClass()
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    obj.x = 7
    assert obj.y == 7
    assert obj.y == 7
    assert obj.y == 7
    del obj.y
    assert obj.y == 8
    assert obj.y == 8
    assert obj.y == 8
    obj.x = 9
    assert obj.y == 9
    assert obj.y == 9
    assert obj.y == 9

    # noinspection PyDictCreation

# Generated at 2022-06-13 20:40:23.963789
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        __slots__ = ()

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    assert obj.y == 6


if __name__ == '__main__':
    test_cached_property___get__()  # pragma: no cover

# Generated at 2022-06-13 20:40:30.143928
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Test for asyncio.iscoroutinefunction
    class MyClass:

        @cached_property
        async def foo(self):
            await asyncio.sleep(1 / 10)
            return 1

        @cached_property
        def bar(self):
            return 2

    my_obj = MyClass()

    assert my_obj.foo == 1
    assert my_obj.bar == 2

if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:40:58.040951
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ This is a test of the method __get__ of the class cached_property """
    from .decorators import cached_property

    test_results = []

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    test_results.append(MyClass().y == 6)

    return all(test_results)

# Generated at 2022-06-13 20:41:06.280052
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    # print(obj.__dict__)
    # assert obj.__dict__ == {'x': 5}
    assert obj.y == 6
    # print(obj.__dict__)
    assert obj.__dict__ == {'x': 5, 'y': 6}



# Generated at 2022-06-13 20:41:10.042109
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    _cls = cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @_cls
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    obj.x = 20

    assert obj.y == 6
# EOF

# Generated at 2022-06-13 20:41:17.781940
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D103
    obj = object()

    class C:
        def __init__(self, value, raise_exc=False):
            self.value = value

        def get_value(self):
            return self.value

        def get_value_async(self):
            return asyncio.coroutine(self.get_value)()

        @cached_property
        def foo(self):
            return self.get_value()

        @cached_property
        def bar(self):
            return self.get_value_async()

    c = C(obj)
    assert c.foo is obj
    assert c.bar.done()
    assert c.bar.result() is obj

# Generated at 2022-06-13 20:41:23.553429
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    obj.x = 8
    assert obj.y == 6



# Generated at 2022-06-13 20:41:35.213031
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from pytest import raises

    from flutils.decorators import cached_property

    @cached_property
    def _cached_property_test(obj):
        return 1

    _cached_property_test.__name__ = "cached_property_test"

    # If obj is None
    assert _cached_property_test.__get__(None, 1) is _cached_property_test

    # If obj is not None
    class Test:
        pass

    test = Test()
    assert test.cached_property_test == 1
    raises(AttributeError, getattr, test, "cached_property_test")

# Generated at 2022-06-13 20:41:44.714746
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    # noinspection PyMissingTypeHints
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1, self.x + 2

    obj = MyClass()
    obj.__dict__['y'].set_result((1, 1))
    z = obj.y
    assert z is ((1, 1),)
# noinspection PyStatementEffect
test_cached_property___get__

# Generated at 2022-06-13 20:41:56.878009
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import mock

    class CachedProperty(cached_property):
        __doc__ = cached_property.__doc__

        def __init__(self, func):
            super().__init__(func)

        @staticmethod
        def __get__(obj: Any, cls):
            if obj is None:
                return cls

            if isinstance(obj, (type, property)):
                return cls

            if asyncio.iscoroutinefunction(cls.func):
                return cls._wrap_in_coroutine(obj)

            value = obj.__dict__[cls.func.__name__] = cls.func(obj)
            return value


# Generated at 2022-06-13 20:42:05.383453
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    # verify cached_property decorator behaves as expected
    obj.x = 10
    assert obj.y == 6

    # verify cached_property decorator can be deleted
    del obj.y
    assert obj.y == 11

# Generated at 2022-06-13 20:42:10.497392
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class __test:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = __test(5)

    # test decorated method
    assert obj.y == 6
    assert 'y' in obj.__dict__
    assert obj.__dict__['y'] == 6

    # test decorated method after deleting
    del obj.y
    assert obj.y == 6
    assert 'y' in obj.__dict__
    assert obj.__dict__['y'] == 6

