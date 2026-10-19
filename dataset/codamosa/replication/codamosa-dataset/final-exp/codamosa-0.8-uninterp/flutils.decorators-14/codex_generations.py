

# Generated at 2022-06-13 20:32:39.902240
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



# Generated at 2022-06-13 20:32:52.402696
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo:
        def __init__(self):
            self.x = 5

        # noinspection PyMethodParameters
        @asyncio.coroutine
        def __a_coroutine(self):
            yield from asyncio.sleep(0.1)  # pragma: no cover
            return self.x + 1

        @cached_property
        def a_coroutine(self):
            return self.__a_coroutine()

        @cached_property
        def a_property(self):
            return self.x + 1

    # noinspection PyStatementEffect
    asyncio.get_event_loop()

    foo = Foo()

    assert foo.a_property == 6
    assert foo.x == 5

    # noinspection PyStatementEffect
    asyncio.get_event_loop()

    foo = Foo()

# Generated at 2022-06-13 20:33:04.244311
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    def test_func():
        pass

    instance = cached_property(test_func)

    assert instance.__class__.__name__ == 'cached_property'
    assert instance.__doc__ == test_func.__doc__
    assert instance.func == test_func

    instance = instance.__get__(None, None)

    assert instance.__class__.__name__ == 'cached_property'
    assert instance.__doc__ == test_func.__doc__
    assert instance.func == test_func

    # noinspection PyMissingOrEmptyDocstring,PyMissingTypeHints
    class TestClass:
        def __init__(self):
            self.s = 'foo'

        # noinspection PyMissingOrEmptyDocstring,PyMethodMay

# Generated at 2022-06-13 20:33:12.490791
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from .testing import assert_function_returns

    class MyClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x

    result = MyClass(5).y
    assert_function_returns(result, 5)

    class MyClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    result = MyClass(5).y
    assert_function_returns(result, 6)



# Generated at 2022-06-13 20:33:19.460349
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Test()
    obj.y
    assert 'y' in obj.__dict__
    assert obj.__dict__['y'] == 6


# Generated at 2022-06-13 20:33:25.149989
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return 'y'

        def z(self):
            return 'z'

    obj = MyClass()
    assert obj.__dict__ == {'x': 5}
    assert obj.y == 'y'
    assert obj.__dict__['y'] == 'y'
    assert obj.z == 'z'
    assert obj.__dict__['z'] == 'z'



# Generated at 2022-06-13 20:33:29.273084
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self) -> int:
            return self.x + 1

    mc = MyClass()
    assert mc.y == 6

# Generated at 2022-06-13 20:33:37.881253
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property
    """
    # Synchronous
    class MyClass:

        def __init__(self):
            self.x = 5
            self.y = None

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    # Asynchronous
    class MyClass:

        def __init__(self):
            self.x = 5
            self.y = None

        @cached_property
        async def y(self):
            await asyncio.sleep(1)
            return self.x + 1

    async def main():
        obj = MyClass()
        assert await obj.y == 6

    loop = asyncio.get_event_loop()
    loop.run_until_

# Generated at 2022-06-13 20:33:47.335421
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from unittest.mock import Mock

    def func():
        return 42

    obj, cls = Mock(), Mock()

    attribute = cached_property(func)

    assert attribute.__doc__ is None
    assert attribute.func == func

    assert attribute.__get__(obj, cls) == 42
    assert attribute.__get__(None, None) is attribute

    # 'cached_property' function is a coroutinefunction
    attribute.func = Mock(return_value=42,
                          __name__='func',
                          __doc__=None,
                          __wrapped__=None)
    assert attribute.__get__(obj, cls) == 42

    # Test with __get__ raising an exception
    attribute.func = Mock(side_effect=Exception)

# Generated at 2022-06-13 20:33:53.819957
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self):
            pass

        @cached_property
        def attr(self):
            return 'value'

    obj1 = TestClass()
    obj2 = TestClass()

    assert obj1.attr == obj2.attr == 'value'



# Generated at 2022-06-13 20:34:06.181321
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    # Test Case 1: function decorator with no arguments.
    class TestClass1:
        def __init__(self, value):
            self._value = value
        @cached_property
        def value(self):
            return self._value * 2
        @value.setter
        def value(self, value):
            self._value = value
        @value.deleter
        def value(self):
            del self._value
    test1 = TestClass1(2)
    assert test1.value == 4
    assert test1._value == 2
    assert "_value" in vars(test1)
    test1._value = 3
    assert test1.value == 4
    assert test1._value == 3
    test1.value = 5

# Generated at 2022-06-13 20:34:13.489279
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
    obj.x = 10
    assert obj.y == 6
    del obj.y
    assert obj.y == 11
    assert type(obj.y) == int

if __name__ == '__main__':
    from pytest import main
    main(args=['-xrs', __file__.replace('.py', '.block')])

# Generated at 2022-06-13 20:34:23.072450
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Test method __get__ of class cached_property
    """

    # Define a class with a cached property
    class ExampleClass:
        """ Example class
        """

        def __init__(self):
            """ Constructor
            """
            self.x = 5

        @cached_property
        def y(self):
            """ Example cached property
            """
            return self.x + 1

    # Instantiate and use it
    obj = ExampleClass()
    y = obj.y

    # Make sure the value is returned
    assert y == 6

    # Make sure a new request returns the same value without recalculating it
    y = obj.y
    assert y == 6



# Generated at 2022-06-13 20:34:27.672581
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # pragma: no cover

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.x == 5
    assert obj.y == 6

    obj.x = 7
    assert obj.x == 7
    assert obj.y == 6

    obj.z = 9
    assert obj.z == 9



# Generated at 2022-06-13 20:34:35.994989
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    if sys.version_info >= (3, 8):
        return

    def method(self): pass

    attr = cached_property(method)

    cached_property_descriptor = dict(__get__=lambda *args, **kwargs: attr)
    args = (None, None)
    kwargs = {}

    assert attr.__get__(*args, **kwargs) is attr

    args = (object(), type)
    kwargs = {}

    assert attr.__get__(*args, **kwargs) is method


# Generated at 2022-06-13 20:34:37.062306
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:34:48.327010
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock
    import asyncio
    from flutils.decorators import cached_property

    # The class to test function __get__ of class cached_property on
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Create a mock object
    obj = Mock(spec=MyClass())
    obj.x = 5

    # Test function __get__ of class cached_property
    result = cached_property.__get__(None, MyClass)
    assert isinstance(result, cached_property)

    result = cached_property.__get__(obj, MyClass)
    assert not asyncio.iscoroutinefunction(result)
    assert result() == 6

    # Test function

# Generated at 2022-06-13 20:35:00.725700
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    This function tests the functionality of the method __get__ of the class
    cached_property.

    Returns
    -------
    int
        Error code; non-zero indicates test failure

    """

    from os import unlink
    from os.path import isfile
    from shutil import rmtree
    from tempfile import TemporaryDirectory

    class CachedPropertyTest:
        def __init__(self):
            self.dir = TemporaryDirectory(dir=dir)
            self.file = self.dir.name + "/test"

        @cached_property
        def test_file(self):
            with open(self.file, "w+"):
                pass
            return self.file

        def delete(self):
            self.dir.cleanup()

    obj = CachedPropertyTest()

# Generated at 2022-06-13 20:35:06.209156
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Obj:

        def __init__(self):
            self.x = 5

        def func(self):
            return self.x + 1

        y = cached_property(func)

    obj = Obj()
    print(obj.y)
    assert obj.y == 6



# Generated at 2022-06-13 20:35:11.958266
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Example:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = Example(5)
    obj.y  # I do not like this syntax... but it's the one used by the decorator
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:35:21.693317
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from nose.tools import assert_equals, assert_true, assert_is, assert_false

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert_equals(obj.y, 6)


# Generated at 2022-06-13 20:35:34.942364
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    def foo():
        pass

    instance = cached_property(foo)
    result = instance.__get__(None, object)
    assert result == instance

    class Bar(object):
        def __init__(self):
            self.x = 5

        @instance
        def y(self):
            return self.x + 1

    bar = Bar()
    assert bar.y == 6

    async def foo2():
        pass  # pragma: no cover

    instance2 = cached_property(foo2)
    result = instance2.__get__(None, object)
    assert result == instance2

    class Bar2(object):
        def __init__(self):
            self.x = 5

        @instance2
        def y(self):
            return self.x + 1

    bar = Bar2()

# Generated at 2022-06-13 20:35:42.063752
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    class MyClass:
        @cached_property
        def y(self):
            return self.x + 1

    obj1 = MyClass()
    obj2 = MyClass()
    obj1.x = 5
    obj2.x = 10

    assert obj1.y == 6
    assert obj2.y == 11

    obj1.x = 15
    obj2.x = 20

    assert obj1.y == 6
    assert obj2.y == 11


# Generated at 2022-06-13 20:35:47.236363
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Standard case
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    # Coroutine function case
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            await asyncio.sleep(0)
            return self.x + 1

    obj = MyClass()
    assert asyncio.get_event_loop().run_until_complete(obj.y) == 6

# Generated at 2022-06-13 20:35:52.085741
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
    assert obj.__dict__['y'] == 6
    assert obj.y == 6

# Generated at 2022-06-13 20:35:57.161491
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    @cached_property
    def y(self):
        return self.x + 1

    class MyClass:
        def __init__(self):
            self.x = 5

    obj = MyClass()
    assert obj.y == 6
    assert obj.y == 6



# Generated at 2022-06-13 20:36:02.228636
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # @cached_property
    # def y(self):
    #     return self.x + 1

    # class MyClass:
    #
    #     def __init__(self):
    #         self.x = 5
    #
    #
    # obj = MyClass()
    # assert obj.y == 6

    # assert y(self=obj) == obj.__dict__[self.func.__name__]
    # assert obj.y == obj.__dict__[self.func.__name__]
    pass

# Generated at 2022-06-13 20:36:14.768680
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from flutils.decorators import cached_property
    from .test_decorators import test_cached_property
    from .test_decorators import test_cached_property_async_loop
    from .test_decorators import test_cached_property_async_coroutine

    t = cached_property.__get__('self', test_cached_property)
    assert t() == 1

    with pytest.raises(AttributeError):
        cached_property.__get__(None, test_cached_property)

    t_async_loop = cached_property.__get__('self', test_cached_property_async_loop)
    assert isinstance(t_async_loop, asyncio.coroutines.CoroWrapper) is True

# Generated at 2022-06-13 20:36:18.750827
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

    obj = MyClass()
    assert obj.y == 6

    del obj.y
    assert obj.y == 6

# Generated at 2022-06-13 20:36:30.440243
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests :obj:`~flutils.decorators.cached_property.__get__` method of
    :class:`~flutils.decorators.cached_property.cached_property` decorator
    class.
    """

    import unittest

    class MyTest(unittest.TestCase):
        """Test :obj:`~flutils.decorators.cached_property.__get__` method of
        :class:`~flutils.decorators.cached_property.cached_property`
        decorator class.
        """

        def setUp(self):
            self.obj = CachedPropertyTest()


# Generated at 2022-06-13 20:36:40.425708
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class :obj:`flutils.decorators.cached_property`.

    """
    # Method __get__ when obj is None
    assert cached_property.__get__(None, None)
    # Method __get__ when obj is not None
    class dummy:

        @cached_property
        def foo(self):
            return True

    assert dummy().foo



# Generated at 2022-06-13 20:36:48.887322
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        @cached_property
        def x(self):
            return 'x'

        @cached_property
        def y(self):
            return 'y'

    def test():
        obj = MyClass()
        assert obj.x == 'x'
        assert obj.y == 'y'
        obj.x = 'xxx'
        obj.y = 'yyy'
        assert obj.x == 'xxx'
        assert obj.y == 'yyy'
        del obj.x
        del obj.y
        assert obj.x == 'x'
        assert obj.y == 'y'
        obj.x = 'X'
        obj.y = 'Y'
        assert obj.x == 'X'
        assert obj.y == 'Y'

    test()
    test()

# Unit

# Generated at 2022-06-13 20:37:01.345662
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test 1
    class Class:
        @cached_property
        def prop(self):
            return 1

    assert Class.prop.__class__.__name__ == "cached_property"
    assert Class.prop.func.__name__ == "prop"
    assert Class().prop == 1

    # Test 2
    class Class:
        @cached_property
        def prop(self):
            return self.prop

    obj = Class()
    with pytest.raises(RuntimeError):
        obj.prop

    # Test 3
    class Class:
        @cached_property
        def prop(self):
            return 1

    assert Class().prop == 1
    obj = Class()
    obj.prop
    assert obj.__dict__["prop"] == 1

    # Test 4

# Generated at 2022-06-13 20:37:13.193377
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import sys
    import pytest

    from io import StringIO

    from flutils.decorators import cached_property

    # Mock class
    class MockClass:
        def __init__(self, x=5):
            self.x = x

        def y(self):
            return self.x + 1

    # Patch sys.stdout
    orig_stdout = sys.stdout
    sys.stdout = StringIO()

    # Instantiate mock class
    obj = MockClass()

    # Check cached_property
    cp = cached_property(obj.y)
    assert cp.func is obj.y
    assert cp.__doc__ == obj.y.__doc__
    assert cp.__get__(None, object) == cp
    assert cp.__get__(obj, MockClass) == 6

    # Unpatch sys

# Generated at 2022-06-13 20:37:17.426479
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # noinspection PyUnusedLocal
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.y
    assert obj.y == 6

# Generated at 2022-06-13 20:37:27.500702
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from types import MethodType
    import sys

    if sys.version_info < (3, 8, 0):
        obj = [None, None]

        def testfunc(self):
            return obj[0]

        testfunc = cached_property(testfunc)

        # test __get__ without obj
        assert type(testfunc) is cached_property
        assert obj[1] is None

        # test __get__ with obj
        obj[0] = '123'
        assert type(testfunc.__get__(self=obj, cls=None)) is MethodType
        assert obj[1] == '123'

        # test __get__ with obj after using cached value
        obj[1] = '456'

# Generated at 2022-06-13 20:37:36.041317
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test the __get__ method of the cached_property decorator class.

    Notes:
        1.  Add doctest or unit test that tests the __get__ method for both a
            regular property as well as a coroutine property.

    """
    class MyClass:

        def __init__(self):
            self.x = 5
            self.y = 7

        @cached_property
        def yprop(self):
            return self.x + 1

        @cached_property
        def ycoroprop(self):
            return self.x + 1

    obj = MyClass()

    # Test for a regular property
    assert obj.yprop == 6

    # Test for a coroutine property
    assert type(obj.ycoroprop) is asyncio.coroutines.CoroWrapper  # noqa

# Generated at 2022-06-13 20:37:41.954462
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    test_cached_property___get__

    *New in version 0.2.0*

    Test case for the instance method __get__ of class cached_property.

    """

    class MyClass:

        @cached_property
        def y(self):
            return self.x + 1

    assert MyClass().y == 6

# Generated at 2022-06-13 20:37:47.506467
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self, val):
            self.x = val

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(5)
    assert obj.y == 6

    obj2 = MyClass(10)
    assert obj2.y == 11

# Generated at 2022-06-13 20:37:52.602922
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    foo = Foo()
    assert foo.y == 6


# Generated at 2022-06-13 20:38:04.477494
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class Simple:

        @cached_property
        def x(self):
            return 1

    s = Simple()
    assert s.x == 1
    assert s.x == 1



# Generated at 2022-06-13 20:38:08.862682
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



# Generated at 2022-06-13 20:38:14.433016
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property
    """

    def foo(obj):
        return 'foo!'

    obj = cached_property(foo)
    assert 'foo!' == obj.__get__(None, None)

# Generated at 2022-06-13 20:38:19.755016
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property.

    .. versionadded:: 0.2.0
    """
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6  # noqa: S101



# Generated at 2022-06-13 20:38:26.032127
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClassGet(object):
        @cached_property
        def f(self):
            return "f"
    test = TestClassGet()
    assert test.f == "f"
    assert TestClassGet.f.__name__ == "f"
    assert TestClassGet.f.__doc__ == TestClassGet.f.func.__doc__


# Generated at 2022-06-13 20:38:34.357482
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Arrange
    # noinspection PyShadowingNames
    class MyClass:

        def __init__(self):
            self.x = 5

        # noinspection PyMethodMayBeStatic
        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # Act
    result = obj.y

    # Assert
    assert result == 6



# Generated at 2022-06-13 20:38:36.250198
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for the method __get__ of class cached_property."""

    _ = cached_property.__get__  # noqa: F841
    return

# Generated at 2022-06-13 20:38:48.047132
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    def method_a(obj):
        return "method_a"

    def method_b(obj):
        return "method_b"

    class MyClass:

        @cached_property
        def my_prop_a(self):
            return method_a(self)

        @cached_property
        def my_prop_b(self):
            return method_b(self)

    obj = MyClass()
    assert obj.my_prop_a == "method_a"
    assert obj.my_prop_b == "method_b"

    obj.my_prop_a = "inserted a"
    assert obj.my_prop_a == "inserted a"



# Generated at 2022-06-13 20:38:51.410548
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



# Generated at 2022-06-13 20:39:03.070231
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class :obj:`cached_property`.

    Test Case #1:

    Test :obj:`cached_property` with a function that returns a regular
    value.

    Test Case #2:

    Test :obj:`cached_property` with a function that returns a coroutine
    object.

    Test Case #3:

    Test the results of the :obj:`cached_property` are coroutine objects.

    """
    from flutils.helpers import ignore_signals
    from flutils.decorators import cached_property
    import asyncio
    import time

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1


# Generated at 2022-06-13 20:39:17.611752
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:39:22.814406
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(5)
    assert obj.__dict__ == {'x': 5}
    # noinspection PyUnresolvedReferences
    assert obj.y == obj.y
    assert obj.__dict__ == {'x': 5, 'y': 6}



# Generated at 2022-06-13 20:39:29.385814
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method ``cached_property.__get__``

    These tests are primarily to increase code coverage.
    """
    import pickle

    # Test __doc__
    obj = cached_property(None)
    obj.__doc__ = 'Test'
    assert obj.__doc__ == 'Test'

    # Test func
    obj.func = 'Test'
    assert obj.func == 'Test'

    # Test return value
    obj.__class__ = type('Test', (), {})
    assert obj.__get__(None, None) is obj

    # Test obj is None
    obj.__class__ = type('Test', (), {})
    obj.__get__(None, None)

    # Test obj is not None

# Generated at 2022-06-13 20:39:42.208848
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D202
    """
    Tests that cached_property.get returns a coroutine if the wrapped function
    is a coroutine, in which case we need to wrap it in a coroutine.
    """

    @asyncio.coroutine
    def coro_future(obj):
        pass

    @cached_property
    def noncoro_future(obj):
        pass

    assert asyncio.iscoroutinefunction(coro_future)
    assert asyncio.iscoroutinefunction(noncoro_future) is False
    # test __get__ when func is a coroutine
    obj = cached_property(coro_future)
    assert asyncio.iscoroutinefunction(obj.__get__(None, None))
    # test __get__ when func is not a coroutine

# Generated at 2022-06-13 20:39:53.761426
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Cached property should return the result of calling the method
    and replace it with an ordinary attribute.

    Also if the method is an asyncio coroutine the the result should be
    the result of the coroutine.

    """

    class Cls:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        async def z(self):
            await asyncio.sleep(0.1)
            return self.x + 1

    c = Cls()
    assert c.y == 6
    assert c.__dict__ == {'x': 5, 'y': 6}


# Generated at 2022-06-13 20:39:54.825647
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass


# Generated at 2022-06-13 20:40:05.437334
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa
    """Unit testing of method cached_property.__get__"""

    # noinspection PyUnusedLocal
    class _BaseTestClass:

        # noinspection PyUnusedLocal
        def __init__(self):
            pass

        def __init_subclass__(cls, **kwargs):
            return super().__init_subclass__(**kwargs)

        @cached_property
        def value(self):  # type: ignore
            return self._value

        @value.setter  # type: ignore
        def value(self, val):
            self._value = val

    class TestClass(_BaseTestClass):
        pass


# Generated at 2022-06-13 20:40:16.227348
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test cached_property on an instance method
    class A:
        def __init__(self, n: int) -> None:
            self.__n = n

        @cached_property
        def square(self) -> int:
            return self.__n * self.__n

        @staticmethod
        @cached_property
        def x() -> int:
            return 4

    a = A(10)
    assert a.square == 100
    assert A.x == 4
    new_square = a.__dict__.pop('square')
    assert new_square == 100
    assert a.square == 100

    # Test cached_property on an async instance method
    class B:
        def __init__(self, n: int) -> None:
            self.__n = n


# Generated at 2022-06-13 20:40:27.613448
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from flutils.system import timed
    from time import time

    def test():
        return time()

    class MyClass:
        @cached_property
        def y(self):
            return test()

    class MyClassCoro:
        @cached_property
        async def y(self):
            return test()

    obj = MyClass()
    obj2 = MyClass()
    obj3 = MyClassCoro()
    obj4 = MyClassCoro()

    _ = obj.y
    _ = obj2.y
    timed(obj.y)
    timed(obj2.y)

    _ = obj3.y
    _ = obj4.y
    timed(obj3.y)
    timed(obj4.y)



# Generated at 2022-06-13 20:40:35.797424
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    # noinspection PyMethodMayBeStatic
    class Test(unittest.TestCase):
        def test(self):
            def func():
                pass

            @cached_property
            def func2():
                pass

            # noinspection PyTypeChecker
            self.assertNotEqual(func, None)
            # noinspection PyTypeChecker
            self.assertNotEqual(func2, None)

    unittest.main()



# Generated at 2022-06-13 20:41:26.452836
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock, patch

    from .test import BenchmarkClass

    then = datetime.now()

    mock_obj = MagicMock(spec=BenchmarkClass)
    mock_obj.__dict__ = {}
    mock_obj.__class__ = BenchmarkClass

    with patch.object(BenchmarkClass, 'value', autospec=True):
        BenchmarkClass.value.return_value = then

        value = cached_property.__get__(None, mock_obj)

    now = datetime.now()
    assert value is then
    assert mock_obj.value == then
    assert mock_obj.timing.start <= then
    assert mock_obj.timing.stop >= now

# Generated at 2022-06-13 20:41:37.163707
# Unit test for method __get__ of class cached_property
def test_cached_property___get__(): # pragma: no cover
    """Unit test for method __get__ of class cached_property"""
    from inspect import signature
    from flutils.decorators import cached_property

    def mock_func(obj):
        return obj.x + 1

    mock_obj = type("obj", (object,), {})()
    mock_obj.x = 5

    obj = cached_property(mock_func)
    cls = type(obj)

    # Test that it returns self if obj is None
    assert obj is obj.__get__(None, cls)

    assert "obj" == mock_func.__name__
    assert "__get__" == mock_func.__qualname__

    # Test that the obj dict has been updated
    assert 6 == obj.__get__(mock_obj, cls)

# Generated at 2022-06-13 20:41:48.253717
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio
    from flutils.decorators import cached_property

    class MyTestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class MyTestClassAsync:

        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            await asyncio.sleep(1)
            return self.x + 1

    # Instantiating class:
    obj = MyTestClass()
    obj_async = MyTestClassAsync()
    assert obj.y == 6
    assert isinstance(obj.y, int)
    assert isinstance(obj_async.y, asyncio.Future)

# Generated at 2022-06-13 20:41:58.720441
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test method __get__ of cached_property.
    """
    # Test "cached_property" of a class.

    # Test: self.y is a cached_property.
    class TestClass:
        def __init__(self):
            self.x = 1

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.__dict__ == {}

    assert obj.y == 2
    assert obj.__dict__ == {'y': 2}
    assert obj.y == 2

    obj.x = 2
    assert obj.__dict__ == {'y': 2}
    assert obj.y == 2

    del obj.y
    assert obj.__dict__ == {}
    assert obj.y == 3

    # Test: Non-c

# Generated at 2022-06-13 20:42:03.487036
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self):
            self.y = self.x + 1

        @cached_property
        def x(self):
            return 5

    obj = TestClass()
    assert obj.x == 5



# Generated at 2022-06-13 20:42:11.290017
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def foo(self):
        return 2

    # Create a Class with the cached_property 'foo'
    class A:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    a = A()
    print(a.y)
    print(a.y)


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:42:21.980259
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test the method __get__ of class cached_property."""

    # Test with a regular method
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    # Test with an async method
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            await asyncio.sleep(.01)
            return self.x + 1

    obj = MyClass()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(obj.y)
    assert obj.y == 6

    # Test with a method that is not async

# Generated at 2022-06-13 20:42:30.632918
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self, x=0):
            self._x = x

        @cached_property
        def y(self):
            return self._x + 1

    obj = MyClass()
    assert obj.y == 1
    assert 'y' in obj.__dict__
    assert obj.__dict__['y'] == 1
    obj._x = 1
    assert obj.y == 2
    assert 'y' in obj.__dict__
    assert obj.__dict__['y'] == 2
    del obj.y
    obj._x = 0
    assert obj.y == 1
    assert 'y' in obj.__dict__
    assert obj.__dict__['y'] == 1
    assert MyClass().y == 1
    obj2 = MyClass(5)
    assert obj2.y

# Generated at 2022-06-13 20:42:36.519596
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # noinspection PyUnresolvedReferences,PyMissingOrEmptyDocstring,PyPep8Naming,PyMissingTypeHints
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

