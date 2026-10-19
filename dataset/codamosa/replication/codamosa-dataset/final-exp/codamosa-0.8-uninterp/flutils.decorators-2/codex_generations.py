

# Generated at 2022-06-13 20:32:43.521720
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1
    assert A().y == 6



# Generated at 2022-06-13 20:32:48.518902
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    @cached_property
    def y(self):
        return self.x + 1

    class MyClass:
        def __init__(self):
            self.x = 5

    obj = MyClass()
    assert y.__get__(obj, None) == 6


# Generated at 2022-06-13 20:32:55.297110
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        @cached_property
        def y(self):
            return self.x + 1

        def __init__(self):
            self.x = 5

    obj = MyClass()
    # Test expected result
    print('Test expected result: {0}'.format(obj.y))
    # Test __doc__ attribute
    print('Test __doc__ attribute: {0}'.format(obj.y.__doc__))
    del obj.y
    # Test reset of attribute
    assert not hasattr(obj, 'y')
    del obj.x


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:32:57.104356
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = A()
    assert obj.y == 6



# Generated at 2022-06-13 20:33:01.901136
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


# Unit for method _wrap_in_coroutine of class cached_property

# Generated at 2022-06-13 20:33:06.723337
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        pass

    obj = MyClass()

    def func():
        return obj

    decorator = cached_property(func)
    assert decorator.__get__(obj, MyClass) is obj

# Generated at 2022-06-13 20:33:07.933079
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass



# Generated at 2022-06-13 20:33:15.104176
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test :meth:`~cached_property.__get__`.

    **Test Condtions**:

    - Access object attribute that is a cached property.
    - Access class attribute that is a cached property.
    - Access class attribute that is a cached property wrapped in an
      :class:`asyncio.coroutine`.

    """
    class TestClass:
        def __init__(self):
            self.x = 3

        @cached_property
        def y(self):
            return self.x + 1

    @cached_property
    def cached_func():
        return TestClass

    @cached_property
    def cached_coro(self):
        return self

    obj = TestClass()
    assert obj.y == 4
    assert TestClass.y == TestClass

# Generated at 2022-06-13 20:33:22.647913
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Foo:
        def __init__(self, x):
            self.x = x

        @cached_property
        def bar(self):
            return self.x

    # Instance
    foo = Foo(5)

    # Make sure the property was computed
    assert foo.bar == 5

    # Make sure the property was cached
    assert foo.__dict__["bar"] == 5

    # Make sure the cached property can be deleted
    del foo.bar
    assert "bar" not in foo.__dict__

# Generated at 2022-06-13 20:33:29.954926
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self):
            self.test_value = 0

        @cached_property
        def test_method(self) -> int:
            self.test_value = self.test_value + 1
            return self.test_value

    obj = TestClass()
    assert obj.test_method == 1
    assert obj.test_method == 1



# Generated at 2022-06-13 20:33:34.425286
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import doctest
    import flutils.decorators

    doctest.testmod(flutils.decorators, verbose=True)

# Generated at 2022-06-13 20:33:42.723983
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.
    """

    from flutils.decorators import cached_property

    class C:

        @cached_property
        def a(self):
            return 3

    c = C()
    assert c.a == 3
    assert c.__dict__ == {'a': 3}

    c.__dict__['a'] = 7
    assert c.a == 7

    del c.a
    assert c.a == 3

# Generated at 2022-06-13 20:33:49.787926
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    from asyncio import coroutine

    from flutils.decorators import cached_property

    def _func():
        return 5

    def _func2():
        return "test"

    def _func3():
        return False

    def _func4():
        return [1, 2, 3]

    def _func5():
        raise Exception

    # noinspection PyPep8Naming
    class TestClass:

        # noinspection PyPep8Naming
        @cached_property
        def test_func(self):
            return _func()

        # noinspection PyPep8Naming
        @cached_property
        def test_func2(self):
            return _func2()

        # noinspection PyPep8Naming

# Generated at 2022-06-13 20:34:00.509834
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        @cached_property
        def x(self):
            return 5

        @cached_property
        async def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.x == 5
    assert obj.__dict__ == {'x': 5}

    assert asyncio.iscoroutine(obj.y)

    assert obj.y.__class__ is asyncio.Future
    assert not obj.y.cancelled()
    assert not obj.y.done()
    assert obj.y.running()
    obj.y.result()
    assert obj.__dict__ == {'x': 5, 'y': asyncio.Future()}

    obj = MyClass()
    assert obj.y.__class__ is asyncio.Future
    assert not obj.y.c

# Generated at 2022-06-13 20:34:10.525246
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.
    """

    # Test a regular property.
    class TestClass:
        @property
        def prop(self):
            return 1

    assert TestClass().prop == 1

    # Test a regular property.
    class TestClass:
        @cached_property
        def prop(self):
            return 1

    assert TestClass().prop == 1

    # Test a coroutine property.
    class TestClass:
        @cached_property
        async def prop(self):
            return 1

    async def async_main():
        assert await TestClass().prop == 1

    asyncio.run(async_main())
##

# Generated at 2022-06-13 20:34:13.250446
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:
        @cached_property
        def x(self):
            return "x"

    obj = TestClass()
    assert obj.x == "x"
    assert obj.x == "x"



# Generated at 2022-06-13 20:34:23.838972
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""
    import os
    import tempfile
    temp_dir = tempfile.TemporaryDirectory()

    # noinspection PyPep8Naming,PyMissingOrEmptyDocstring
    class TestClass:
        def __init__(self, path):
            self.path = path

        @cached_property
        def test_prop_1(self):
            return os.path.join(self.path, 'test_1')

        @cached_property
        def test_prop_2(self):
            return os.path.join(self.path, 'test_2')

    obj = TestClass(temp_dir.name)
    assert not hasattr(obj, 'test_prop_1')

# Generated at 2022-06-13 20:34:36.164820
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        @asyncio.coroutine
        def z(self):
            yield from asyncio.sleep(1)
            return self.x + 1

    obj = MyClass()
    # Test that ordinary function works.
    assert obj.y == 6
    # Test that the method is cached.
    assert 'y' in obj.__dict__

    @asyncio.coroutine
    def test_coroutine():
        # Test that coroutine function works.
        await asyncio.sleep(2)
        assert obj.z == 6
        # Test that the coroutine is cached.
        assert 'z' in obj.__dict__

# Generated at 2022-06-13 20:34:44.449642
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self):
            self.a = 1
            self.b = 3

        @cached_property
        def p(self):
            return self.a + self.b

    tc = TestClass()
    assert tc.p == 4
    assert 'p' in tc.__dict__
    assert tc.__dict__['p'] == 4
    tc.a = 3
    tc.b = 5
    assert tc.p == 4

    del tc.p
    assert 'p' not in tc.__dict__
    assert tc.p == 8

# Generated at 2022-06-13 20:34:58.067135
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test a coroutine
    async def coro():
        return 'flutils'

    cp = cached_property(coro)
    assert asyncio.iscoroutinefunction(cp.func)
    assert cp.__get__(None, None) == cp  # get function
    assert cp.__get__(cp, None) == cp  # get function
    assert asyncio.iscoroutine(cp.__get__(cp, None))  # get coroutine
    assert asyncio.iscoroutine(cp.__get__(cp, None))  # get coroutine, not cached
    assert asyncio.iscoroutine(cp.__get__(cp, None))  # get coroutine, cached, then reset cache

    # Test a non coroutine
    def func():
        return 'flutils'

    cp = cached_property(func)


# Generated at 2022-06-13 20:35:04.694530
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # MyClass
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # test
    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:35:15.027510
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
    assert obj.__dict__ == {'x': 5, 'y': 6}


# Asyncio unit test for method __get__ of class cached_property
async def test_cached_property___get__async():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            await asyncio.sleep(0.1)
            return self.x + 1

    obj = MyClass()
    assert await obj.y == 6

# Generated at 2022-06-13 20:35:27.458137
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    def test_function(the_self, test_arg=None):
        return the_self.test_arg + 1

    class TestClass:
        test_arg = 5

        @cached_property
        def test_property(tc):
            return test_function(tc)

    test_instance = TestClass()
    assert test_instance.test_property == 6
    assert test_instance.__dict__["test_property"] == 6
    del test_instance.test_property
    assert "test_property" not in test_instance.__dict__
    assert test_instance.test_property == 6
    assert test_instance.__dict__["test_property"] == 6

# Generated at 2022-06-13 20:35:30.662116
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class A:
        def __init__(self):
            self.x = 5

    def func():
        return 2

    result = cached_property(func).__get__(A())
    assert result == 2



# Generated at 2022-06-13 20:35:33.623407
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

# Generated at 2022-06-13 20:35:34.537947
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass # TODO: Implement test

# Generated at 2022-06-13 20:35:44.620709
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test that the cached_property method __get__ as expected"""

    # noinspection PyUnusedLocal
    class _CachedPropertyTester:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    async def _test_async_cached_property_get():
        class _AsyncCachedPropertyTester:

            def __init__(self):
                self.x = 5

            @cached_property
            async def y(self):
                return self.x + 1

        obj = _AsyncCachedPropertyTester()
        await obj.y

    obj = _CachedPropertyTester()
    assert obj.y == 6

    # Confirm that it is a cached_property

# Generated at 2022-06-13 20:35:48.570994
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    x = obj.y
    assert x == 6



# Generated at 2022-06-13 20:35:52.476134
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Test cached_property.__get__. """

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.y

    assert obj.y == 6


# Generated at 2022-06-13 20:35:57.345513
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    instance = MyClass()
    assert instance.y == 6

# Generated at 2022-06-13 20:36:14.272073
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for cached_property.__get__
    """
    import asyncio
    import unittest

    # noinspection PyPep8Naming
    class MyClass:

        @cached_property
        def y(self):
            return self.x + 1

    class TestCachedProperty(unittest.TestCase):

        def setUp(self):
            self.obj = MyClass()

        def test_class_attribute_returns_value(self):
            self.obj.x = 4
            self.assertEqual(self.obj.y, 5)

        def test_class_attribute_returns_same_value(self):
            self.obj.x = 5
            self.assertEqual(self.obj.y, 6)


# Generated at 2022-06-13 20:36:21.297728
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self):
            self.a = 1

        @cached_property
        def b(self):
            return self.a + 1

    a = A()
    assert a.b == 2

    class B:
        def __init__(self):
            self.a = 1

        @cached_property
        def b(self):
            return self.a + 1

        @b.setter
        def b(self, n):
            self.b = n

    b = B()
    assert b.b == 2

    class C:
        def __init__(self):
            self.a = 1

        @cached_property
        def b(self):
            return self.a + 1


# Generated at 2022-06-13 20:36:26.288333
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.

    """
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.y

# Generated at 2022-06-13 20:36:36.011544
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    from unittest import mock

    from functools import update_wrapper

    class NewClass(object):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    new_class = NewClass()
    assert new_class.y == 6

    descr = NewClass.y
    func = descr.func
    assert not func.__doc__
    assert func.__name__ == "y"
    assert func.__module__ == __name__
    assert func.__code__.co_name == "y"

    assert isinstance(descr, cached_property)


# Generated at 2022-06-13 20:36:43.523703
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass():
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert MyClass.y == cached_property
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}
    assert MyClass.y == cached_property
    del obj.y
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}



# Generated at 2022-06-13 20:36:50.736988
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from .testutils import assert_dotted_list_contains

    def test_class():

        def __init__(self):
            self.x = 5

        # noinspection PyUnusedLocal
        @cached_property
        def y(self):
            return self.x + 1

    msg = "Method '__get__' of class 'cached_property' is not working"
    assert_dotted_list_contains(
        test_class.y, test_class.y.__dict__, msg=msg
    )

# Generated at 2022-06-13 20:37:02.200464
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # property exists
    assert hasattr(obj, 'y')

    # property is cached
    assert obj.__dict__.get('y', None) is None
    assert obj.y == 6
    assert obj.__dict__.get('y', None) == 6

    # cached property can be deleted
    del obj.y
    assert obj.__dict__.get('y', None) is None

    # an empty cached property will return None
    del obj.y
    assert obj.__dict__.get('y', None) is None

    # property is recomputed
    assert obj.y == 6

# Unit test

# Generated at 2022-06-13 20:37:11.440639
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test for method cached_property.__get__."""

    class C:

        @cached_property
        def cached_property_func(self):
            self.value = 1
            return self.value

        def cached_property_func_sync(self):
            self.value = 1
            return self.value

    obj = C()
    assert obj.cached_property_func_sync == 1
    assert obj.value == 1
    assert obj.cached_property_func == 1
    assert obj.__dict__ == {'value': 1, 'cached_property_func': 1}



# Generated at 2022-06-13 20:37:20.738262
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest
    from unittest.mock import Mock


    class TestCacheProperty(unittest.TestCase):

        def setUp(self):
            self.test_obj = Mock()

            self.test_obj.foo = 5
            self.test_obj.__dict__ = {"foo": 5}

            self.test_func_sync = Mock()
            self.test_func_sync.__name__ = "func_sync"
            self.test_func_sync.return_value = "sync"

            self.test_func_async = Mock()
            self.test_func_async.__name__ = "func_async"
            self.test_func_async.return_value = "async"

            self.cp_sync = cached_property(self.test_func_sync)


# Generated at 2022-06-13 20:37:24.931726
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def y(self):
        return self.x + 1

    class MyClass:
        """Class for testing."""

        def __init__(self):
            """Initialize class variables."""
            self.x = 5

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:37:47.898526
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    # Creating a class with a cached attribute
    class A:
        @cached_property
        def x(self):
            return 5

    # Creating an instance of the class
    a = A()

    # The attribute is not yet in the instance's attribute dictionary
    assert 'x' not in a.__dict__

    # The attribute value is computed and saved in the instance's attribute dictionary
    assert a.x == 5
    assert a.__dict__['x'] == 5

    # Deleting an attribute resets the cached property
    del a.x
    assert 'x' not in a.__dict__

    # If a coroutine is used to initialize an attribute, the attribute will not be
    # replaced with the coroutine until the coroutine has completed

# Generated at 2022-06-13 20:37:57.870179
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:
        def __init__(self):
            self.x = 1

        @cached_property
        def y(self):
            return self.x + 1

    assert Test.y.__doc__ == Test.y.func.__doc__
    assert Test.y.__name__ == 'y'
    assert Test.y.__module__ == 'tests.decorators'

    obj = Test()
    assert obj.y == 2
    assert obj.__dict__ == {'x': 1, 'y': 2}
    assert obj.y == 2
    assert obj.__dict__ == {'x': 1, 'y': 2}



# Generated at 2022-06-13 20:38:04.298957
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class DummyClass:

        def __init__(self, x: int):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    assertDictEqual = {
        "__doc__":
            None,
        "func":
            DummyClass.y,
    }

    # Check y is property object
    assert type(DummyClass.y) == cached_property

    # Check attributes
    for k, v in assertDictEqual.items():
        assert hasattr(DummyClass.y, k)
        assert getattr(DummyClass.y, k) == v

    # Check instance properties
    dummy_instance = DummyClass(5)

# Generated at 2022-06-13 20:38:09.039847
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
    assert obj.__dict__['y'] == 6

# Generated at 2022-06-13 20:38:15.017607
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.y
    assert obj.y == 6

# Generated at 2022-06-13 20:38:19.316620
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class X:

        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            return self.x + 1

    x = X()
    assert x.y == 1
    x.x = 5
    assert x.y == 6



# Generated at 2022-06-13 20:38:23.757516
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

# Generated at 2022-06-13 20:38:28.526552
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    _returned = MyClass().y
    assert _returned == 6

# Generated at 2022-06-13 20:38:38.926601
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    unit test for method __get__ of class cached_property

    """

    class Obj:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x * 2

    obj = Obj(1)
    assert obj.y == 2
    assert obj.__dict__['y'] == 2

    obj.__dict__['y'] = 3
    assert obj.y == 3
    assert obj.__dict__['y'] == 3

    del obj.__dict__['y']
    assert obj.y == 2
    assert obj.__dict__['y'] == 2

    obj = Obj(2)
    assert obj.y == 4
    assert obj.__dict__['y'] == 4

    obj.__dict__['y'] = 5

# Generated at 2022-06-13 20:38:44.306996
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

# Generated at 2022-06-13 20:39:16.464618
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    from .decorators import cached_property

    def test_case_0():
        # Test case with an ordinary function

        class C:
            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj = C()
        obj.y
        assert hasattr(obj, 'y')
        assert isinstance(obj.y, int)
        assert obj.y == 6

    def test_case_1():
        # Test case with an async function

        class C:
            def __init__(self):
                self.x = 5

            @cached_property
            async def y(self):
                return self.x + 1

        obj = C()
        obj.y

# Generated at 2022-06-13 20:39:22.341304
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test - cached_property___get__"""

    # noinspection PyAbstractClass
    class MyClass:
        """MyClass class for testing cached_property."""

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    obj.x = 3
    assert obj.y != 6



# Generated at 2022-06-13 20:39:27.971041
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class myclass(object):
        def __init__(self):
            self.i = 666

        @cached_property
        def x(self):
            return self.i

    a = myclass()
    assert a.x == 666
    assert a.__dict__ == {'i': 666, 'x': 666}

    del (a.x)
    assert a.x == 666
    assert a.__dict__ == {'i': 666, 'x': 666}
    assert cached_property.__get__(cached_property(lambda x: x), a, type(a)) == 666



# Generated at 2022-06-13 20:39:33.537240
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    a = A()

    assert a.y == 6
    assert a.__dict__["y"] == 6


# Generated at 2022-06-13 20:39:38.367837
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



# Generated at 2022-06-13 20:39:41.881246
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    obj = PythonVersionChecker('test')

    assert obj is not None

    assert obj.python_version_str == "3.7.2"
    assert obj.python_version_info == (3, 7, 2, 'final', 0)
    assert obj.is_python_36
    assert not obj.is_python_37



# Generated at 2022-06-13 20:39:53.732149
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class :obj:`cached_property`

    This test method must be run with the ``pytest`` script.

    Example:

        To run this test module with pytest::

            cd flutils
            pytest flutils/tests/test_decorators.py -v

    """

    from flutils.decorators import cached_property

    def add_one(self):
        return self.x + 1

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return add_one(self)

    obj = MyClass()
    assert obj.y == 6
    obj.y
    assert add_one.__name__ not in obj.__dict__


# Generated at 2022-06-13 20:39:59.218573
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from pytest_mock import mocker

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    with pytest.raises(AttributeError):
        MyClass().y

    assert MyClass().y == 6



# Generated at 2022-06-13 20:40:06.378902
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    try:
        from types import MethodType
    except ImportError:
        from types import MethodType

    class MyClass:
        """Class for testing of __get__ method of the cached_property"""
        # noinspection PyMissingConstructor
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert isinstance(obj.y, MethodType)
    obj.__dict__["y"] = 6
    assert obj.y == 6



# Generated at 2022-06-13 20:40:17.872268
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    import asyncio
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(5)

    def helper():
        return obj.y

    # Assert class attribute exists
    assert hasattr(obj, 'y') is True

    # Assert class attribute has a value
    assert obj.y == 6

    # Assert class attribute is not a function
    assert isinstance(obj.y, int) is True

    # Assert class attribute can be deleted
    del obj.y

    # Assert class attribute exists
    assert hasattr(obj, 'y') is True

    # Assert class attribute has a value

# Generated at 2022-06-13 20:40:43.187554
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

# Generated at 2022-06-13 20:40:53.218298
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Test that the value is properly cached
    obj = MyClass()
    y = obj.y
    obj.x = 0
    assert y == obj.y

    # Test that the cached value is deleted when the property is deleted
    del obj.y
    assert obj.y != y

    # Test that None is returned when called on the class rather than on an
    # instance
    assert MyClass.y is None



# Generated at 2022-06-13 20:40:59.454797
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # decorator is not part of flutils
    class Test(object):

        @cached_property
        def y(self):
            return 5

    t = Test()
    assert t.y == 5

    # method __get__
    t.__dict__['y'] = 10
    assert t.y == 10
    assert t.__dict__['y'] == 10



# Generated at 2022-06-13 20:41:05.849072
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def xprop(self):
        return 5

    class Test:
        xprop = xprop

    test = Test()
    assert (test.xprop, test.__dict__) == (5, {'xprop': 5})
    assert ('xprop' in test.__dict__) is True
    assert ('yprop' not in test.__dict__) is True


# Generated at 2022-06-13 20:41:09.750403
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        @cached_property
        def prop(self):
            return 1

    obj = MyClass()
    property = obj.prop
    assert isinstance(property, asyncio.Future)
    assert not property.done()
    asyncio.run(property)
    assert property.done()
    assert property.result() == 1

# Generated at 2022-06-13 20:41:18.389040
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    def __get__(self, obj: Any, cls):
        if obj is None:
            return self

        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value

    func = __get__.__func__
    func.__doc__ = "Test property"
    cached_property.__get__.func_closure[0].cell_contents[0] = func

    class TestClass:
        def __init__(self):
            self.x = 10

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x - 1

    obj = TestClass()

    assert obj.y == 11
    assert obj.y == 11

# Generated at 2022-06-13 20:41:23.002023
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    class Test(object):

        @cached_property
        def test(self):
            return "test"

    assert Test().test == "test"
    assert Test().__dict__['test'] == "test"



# Generated at 2022-06-13 20:41:37.620927
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    cls = type("MyClass", (), {})

    assert cls.__dict__.get("x") is None
    assert cls.__dict__.get("y") is None

    def __init__(self):
        self.x = 5

    def y(self):
        return self.x + 1

    cls.__init__ = __init__
    cls.y = cached_property(y)

    assert cls.__dict__.get("x") is None
    assert cls.__dict__.get("y") is not None
    assert type(cls.__dict__.get("y")) is cached_property

    obj = cls()

    assert obj.y == 6

    assert obj.__dict__.get("x") == 5
    assert obj.__dict__.get("y") == 6

# Generated at 2022-06-13 20:41:42.836201
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class _C(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = _C()
    assert obj.y == 6
    assert obj.y == 6



# Generated at 2022-06-13 20:41:55.884755
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa:D104
    """
    Unit test for method __get__ of class cached_property

    Returns
    -------
    None : NoneType

    """

    # noinspection PyTypeChecker
    class _TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = _TestClass()
    assert obj.y == 6
    assert obj.x == 5
    assert obj.__dict__['y'] == 6
    del obj.y
    assert obj.y == 6
    assert obj.x == 5
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:42:42.912523
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    loop = asyncio.get_event_loop()

    class TestClass:

        def __init__(self, test_var):
            self.test_var = test_var

        @cached_property
        def cached_test_var(self):
            self.test_var += 1
            return self.test_var

    # Test with Python 3.8+
    if sys.version_info >= (3, 8):
        obj = TestClass(test_var=0)
        assert obj.cached_test_var == 1
        assert obj.cached_test_var == 1
        obj = TestClass(test_var=1)
        assert obj.cached_test_var == 2
        assert obj.cached_test_var == 2
    # Test with Python 3.6 and 3.7