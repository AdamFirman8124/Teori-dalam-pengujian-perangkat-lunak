

# Generated at 2022-06-13 20:32:42.070483
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
    assert "y" in obj.__dict__
    assert obj.__dict__["y"] == 6

    obj = MyClass()
    assert obj.y == 6
    assert "y" in obj.__dict__
    assert obj.__dict__["y"] == 6


if __name__ == "__main__":
    import pytest

    pytest.main()

# Generated at 2022-06-13 20:32:53.605700
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from types import MethodType as method
    from unittest import TestCase

    class Test_cached_property___get___test_0(TestCase):
        def test_0(self):
            class Test:

                def __init__(self):
                    self.x = 5

                @cached_property
                def y(self):
                    return self.x + 1

            obj = Test()
            self.assertEqual(obj.y, 6)

    class Test_cached_property___get___test_1(TestCase):
        def test_0(self):
            class Test:
                def __init__(self):
                    self.x = 5

                @cached_property
                def y(self):
                    return self.x + 1

            obj = Test()

# Generated at 2022-06-13 20:33:04.925234
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from copy import copy
    import pytest

    from unittest.mock import Mock
    from unittest.mock import patch

    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    assert obj.y == 6, "obj.y is not 6"

    # Test without instance
    prop = cached_property(lambda x: x + 1)
    assert prop.__doc__ is None, "prop.__doc__ is not None"
    assert prop.func(obj) == 7, "prop.func(obj) is not 7"


# Generated at 2022-06-13 20:33:09.985869
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


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:33:18.644202
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Create a class that has `x` as a cached_property.
    class Foo:

        # noinspection PyAttributeOutsideInit
        def __init__(self):
            self.x = 3

        @cached_property
        def x(self):
            return 5

    # Create an instance of Foo.
    foo = Foo()

    # Assert that the `x` attribute has been cached.
    assert foo.x == 5
    assert foo.__dict__['x'] == 5



# Generated at 2022-06-13 20:33:26.812297
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from sys import version_info
    from unittest import TestCase, main

    class _MyClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    class _Test(TestCase):
        def test_get(self):
            obj = _MyClass(5)
            self.assertEqual(obj.y, 6)

        def test_get_async(self):
            obj = _MyClass(5)

            @asyncio.coroutine
            def _async():
                yield from asyncio.sleep(0.01)
                return obj.x + 1

            @asyncio.coroutine
            def _test():
                r = yield from obj.y

# Generated at 2022-06-13 20:33:33.001551
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from functools import partial
    from .utils import get_coroutine_result

    class MyClass(object):

        def __init__(self, function, *args, **kwargs):
            self.__args = args
            self.__kwargs = kwargs
            self.function = function

        @cached_property
        def y(self):
            return self.function(*self.__args, **self.__kwargs)

    # With a non-coroutine function
    @asyncio.coroutine
    def noop_blocking(*args, **kwargs):
        yield from asyncio.sleep(0.1)
        return args, kwargs


# Generated at 2022-06-13 20:33:38.160091
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

# Generated at 2022-06-13 20:33:42.062901
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


# Generated at 2022-06-13 20:33:44.737630
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:
        def __init__(self):
            pass

        @cached_property
        def y(self):
            print("This one should print")
            return 1

    obj = MyClass()
    assert obj.y == 1
    assert obj.y == 1



# Generated at 2022-06-13 20:33:54.989803
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property."""

    class Parent:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    parent = Parent()
    parent.y

    assert parent.x == 5
    assert parent.y == 6

    # Test for cache
    parent.x = 6
    assert parent.x == 6
    assert parent.y == 6



# Generated at 2022-06-13 20:34:02.682858
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # create dummy class to use as test subject
    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # create dummy class to use as test subject
    class TestAsyncClass:
        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def y(self):
            return self.x + 1

    # run tests
    obj = TestClass()
    assert obj.y == 6

    obj = TestAsyncClass()
    assert asyncio.iscoroutinefunction(obj.y)

    assert asyncio.run(obj.y).result() == 6



# Generated at 2022-06-13 20:34:08.141646
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Generic:
        def __init__(self):
            pass

        @cached_property
        def y(self):
            return 'y'

    obj = Generic()
    assert obj.y == 'y'
    obj.y = 'z'
    assert obj.y == 'z'


# Generated at 2022-06-13 20:34:12.390758
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1
    obj = TestClass(5)
    assert obj.y == 6
    assert obj.__dict__['y'] == obj.y


# Generated at 2022-06-13 20:34:20.110434
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.__dict__.update({'x': 5})
    obj.y
    assert obj.y == 6



# Generated at 2022-06-13 20:34:24.910215
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class BaseClass:

        @cached_property
        def property(self):
            """Some property."""
            return 1

    base = BaseClass()
    assert base.__class__.property.__doc__ == """Some property."""
    assert base.property == 1
    assert base.property == 1



# Generated at 2022-06-13 20:34:25.503490
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:34:27.755168
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    assert True


# Generated at 2022-06-13 20:34:34.143672
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

    # Test that two properties are linked
    obj.x = 10
    # noinspection PyStatementEffect
    obj.y
    assert obj.y == 11



# Generated at 2022-06-13 20:34:37.515920
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



# Generated at 2022-06-13 20:34:47.375770
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # setup
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # exercise
    actual = obj.y

    # verify
    assert actual == 6



# Generated at 2022-06-13 20:34:53.704583
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



# Generated at 2022-06-13 20:35:00.090646
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import TestCase
    from unittest.mock import patch

    # noinspection PyUnresolvedReferences
    with patch(
        'flutils.decorators.cached_property.asyncio.iscoroutinefunction',
        side_effect=[False, True, True]
    ) as mock_iscoroutinefunction:

        # noinspection PyUnusedLocal
        @cached_property
        def my_cached_property(obj):
            raise NotImplementedError  # pragma: no cover

        test_case = TestCase()

        # In this case _wrap_in_coroutine should not be called
        test_case.assertEqual(my_cached_property.__get__(None, None), my_cached_property)

        # In this case _wrap_in_coroutine should be

# Generated at 2022-06-13 20:35:12.357689
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    For Python 3.6 and 3.7, this test verifies the method
    :meth:`cached_property.__get__` works as expected.
    """

    class MyClass:
        """
        A simple class used for testing.
        """

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """
            A property that is only computed once per instance and then
            replaces itself with an ordinary attribute.

            :return: The value of the property
            """
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    obj.x = 3
    assert obj.y == 6
    del obj.y
    assert not hasattr(obj, 'y')

# Generated at 2022-06-13 20:35:18.760197
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class test_class:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = test_class()
    assert obj.y == 6
    # second call - this time the value will be retrieved from __dict__
    assert obj.y == 6
    del obj.y
    assert obj.y == 6



# Generated at 2022-06-13 20:35:22.430162
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def test_prop(self):
        return 3.14159

    assert test_prop.__get__ is cached_property.__get__



# Generated at 2022-06-13 20:35:35.871155
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    def assert_equal(value, expect):
        # noinspection PyUnresolvedReferences
        from flutils.tests import ExecutionResult
        ExecutionResult(value=value, expect=expect, type_="assert_equal")

    def assert_is(value, expect):
        # noinspection PyUnresolvedReferences
        from flutils.tests import ExecutionResult
        ExecutionResult(value=value, expect=expect, type_="assert_is")

    def test_cached_property___get___with_method(self):

        @cached_property
        def foo(self):
            self.foo_called = True
            return 5

        assert_is(foo.__get__(self, self.__class__), foo)


# Generated at 2022-06-13 20:35:40.168442
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from .test_setup import Obj

    obj = Obj()

    @cached_property
    def y(self):
        return self.x + 11

    assert y.__doc__

    rv = y.__get__(obj, None)
    assert rv == 16



# Generated at 2022-06-13 20:35:46.250046
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock

    obj = MagicMock()
    obj.__dict__ = {}

    def func(obj):
        return 42

    cached_property(func).__get__(obj, 'cls')
    assert func.__name__ in obj.__dict__
    assert obj.__dict__[func.__name__] == 42


# Generated at 2022-06-13 20:35:51.276983
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.y = 0

        @cached_property
        def x(self):
            self.y += 1
            return self.y

    obj = MyClass()
    assert obj.x == 1
    assert obj.x == 1
    assert obj.y == 1
    assert obj.y == 1



# Generated at 2022-06-13 20:36:02.071540
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



# Generated at 2022-06-13 20:36:09.565227
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # noinspection PyPep8Naming
    class MyClass:
        def __init__(self, x=5):
            self.x = x
            self._y = None

        @cached_property
        def y(self):
            '''Return `x`'''
            return self.x

    obj = MyClass()
    assert obj.y == 5
    assert obj.y == 5



# Generated at 2022-06-13 20:36:18.904668
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio

    class A:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        @asyncio.coroutine
        def z(self):
            yield from asyncio.sleep(.3)
            return self.x + 1

    b = A()
    assert isinstance(b.y, int) and b.y == 6
    assert isinstance(b.z, asyncio.Future) and not b.z.done()
    asyncio.get_event_loop().run_until_complete(b.z)
    assert isinstance(b.z, asyncio.Future) and b.z.done() and b.z.result() == 6



# Generated at 2022-06-13 20:36:26.007487
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    class MockClass:
        def __init__(self):
            self.foo = 'bar'

        @cached_property
        def bar(self):
            return self.foo

    obj = MockClass()
    assert obj.bar == 'bar'
    obj.bar = 'foo'
    assert obj.bar == 'foo'
    with pytest.raises(AttributeError):
        obj.bar = 2



# Generated at 2022-06-13 20:36:35.659093
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # test cached property is implemented correctly via __get__ method
    import os
    import sys

    import pytest

    from flutils.decorators import cached_property

    @cached_property
    def y(self):
        return self.x + 1

    class MyClass():
        def __init__(self):
            self.x = 5

    obj = MyClass()
    assert y.__get__(obj) == 6
    with pytest.raises(TypeError):
        y.__get__()

    def test_cached_property___get__():
    # test cached property is implemented correctly via __get__ method
        import os
        import sys

        import pytest

        from flutils.decorators import cached_property

        @cached_property
        def y(self):
            return self.x + 1



# Generated at 2022-06-13 20:36:40.299046
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6


# Generated at 2022-06-13 20:36:43.921660
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    def func(obj):
        return obj.x

    x = cached_property(func)

    class MyClass:
        def __init__(self):
            self.x = 5

    obj = MyClass()
    assert x.__get__(obj, MyClass) == 5



# Generated at 2022-06-13 20:36:49.795910
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # define a class with a cached_property
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # instantiate the class
    obj = MyClass()
    # call the property
    z = obj.y

    # test results
    assert z == 6


# Generated at 2022-06-13 20:36:52.725103
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.tests.helpers import runpytest

    runpytest('-q .', project='flutils')

# Generated at 2022-06-13 20:37:00.675570
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # -------------------------------------------------------------------------
    # Setup:
    # -------------------------------------------------------------------------
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # -------------------------------------------------------------------------
    # Exercise:
    # -------------------------------------------------------------------------
    obj = MyClass()
    assert obj.y == 6

    # -------------------------------------------------------------------------
    # Verify:
    # -------------------------------------------------------------------------
    obj.x = 6
    assert obj.y == 6

    # -------------------------------------------------------------------------
    # Cleanup:
    # -------------------------------------------------------------------------
    del obj

# Generated at 2022-06-13 20:37:22.753735
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo(object):
        @cached_property
        def foo(self):
            return 1

        @cached_property
        def bar(self):
            return 2

        def baz(self):
            return 3

    obj = Foo()
    if asyncio.iscoroutinefunction(obj.foo):
        obj.foo = asyncio.ensure_future(obj.foo)
    assert obj.foo == 1
    assert obj.bar == 2
    assert obj.baz() == 3
    obj.foo = 7
    assert obj.foo == 7
    del obj.foo
    if asyncio.iscoroutinefunction(obj.foo):
        obj.foo = asyncio.ensure_future(obj.foo)
    assert obj.foo == 1
    assert obj.bar == 2
    assert obj.baz() == 3

# Generated at 2022-06-13 20:37:31.273855
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method cached_property.__get__().

    """
    class MyClass:
        pass
    m = MyClass()
    def func_returns_3(instance):
        return 3
    cp = cached_property(func_returns_3)
    assert cp.__get__(m) == 3
    assert cp.__get__(m) == 3
    m.func_returns_3 = 4
    assert cp.__get__(m) == 4
    del m.func_returns_3


# Generated at 2022-06-13 20:37:45.002325
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # pylint: disable=protected-access,unused-variable
    # From class type
    cls = cached_property(lambda o: o)
    assert cls.__get__(None, type(cls)) is cls

    # From instance
    inst = cls(None)
    assert cls.__get__(inst, type(inst)) is not cls

    # Call function and check that function doesn't get called again
    n = 0

    def func():
        """This is the function."""
        nonlocal n
        n += 1

    inst = func  # pylint: disable=redefined-variable-type
    cp = cached_property(func)
    assert cp(None) is inst

    inst.__get__(None, type(inst))
    assert n == 1

# Generated at 2022-06-13 20:37:51.428738
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    import pytest
    from flutils.decorators import cached_property

    class A:
        call_count = 0

        @cached_property
        def x(self):
            self.call_count += 1
            return 5

    a = A()
    assert a.x == 5
    assert a.call_count == 1

    # Make sure the attribute is cached
    a = A()
    assert a.x == 5
    assert a.call_count == 1

    # Make sure the attribute can be deleted
    del a.x
    assert a.x == 5
    assert a.call_count == 2

    # Make sure __get__ works when called on class
    assert A.x is cached_property

    # Make sure __get__ works on instances

# Generated at 2022-06-13 20:37:58.922459
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x + 2

    my_obj = MyClass()

    assert my_obj.y == 6
    assert my_obj.z == 7
    my_obj.__dict__['y'] = 10
    my_obj.__dict__['z'] = 11
    assert my_obj.y == 10
    assert my_obj.z == 11

# Generated at 2022-06-13 20:38:10.833495
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests that the cached property decorator follows expected behavior
        for nested functions and methods.

    """

    import asyncio

    from copy import copy
    from flutils.decorators import cached_property

    @cached_property
    def this_is_a_function(this):
        return 'This is a function.'

    class ThisIsAClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def this_is_a_method(self):
            return 'This is a method.'

    class ThisIsAnAsyncClass:

        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def this_is_an_async_method(self):
            return 'This is an async method.'

   

# Generated at 2022-06-13 20:38:14.533645
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # noinspection PyProtectedMember
    assert cached_property.__get__ == cached_property.__get__


# Generated at 2022-06-13 20:38:19.516786
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.foo = 'bar'

        @cached_property
        def my_property(self):
            return "The " + self.foo + " property"

    obj = MyClass()
    assert obj.my_property == "The bar property"
    assert obj.foo == "bar"


# Generated at 2022-06-13 20:38:25.351933
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property
    """

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:38:36.650640
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Create an instance of CachedProperty
    from flutils.decorators import cached_property
    cp = cached_property(lambda self: None)

    obj = object()
    # Test if cp.__get__(obj) returns None
    x = cp.__get__(obj)
    assert x is None

    # Test if cp.__get__(obj, None) returns None
    z = cp.__get__(obj, None)
    assert z is None

    # Test if cp.__name__ is 'cached_property'
    y = cp.__name__
    assert y == 'cached_property'



# Generated at 2022-06-13 20:39:23.485840
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""
    import pytest
    from collections import namedtuple

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert isinstance(MyClass.y, cached_property)
    assert obj.y == 6
    assert obj.__dict__['y'] == 6

    obj.x = 10
    assert obj.y == 11
    assert obj.__dict__['y'] == 11

    # Test that the cached property is a coroutine function
    class MyClass2:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x

# Generated at 2022-06-13 20:39:25.977947
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.x = 5
    assert obj.y == 6



# Generated at 2022-06-13 20:39:39.441197
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    from unittest.mock import patch
    import pytest

    @cached_property
    def x(self):
        self.y += 1
        return self.x * 10

    class MyClass():
        def __init__(self, x, y):
            self.x = x
            self.y = y

    vals1 = [1, 2]
    vals2 = [3, 5]

    # testing patching __get__
    obj1 = MyClass(*vals1)
    obj2 = MyClass(*vals2)

    with patch.object(cached_property, '__get__', return_value=100):
        assert obj1.x == 100
        assert obj2.x == 100

    # testing the class
    assert obj1.x == 10
    assert obj1.y == 3
    assert obj

# Generated at 2022-06-13 20:39:44.089872
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    class MyClass:

        # noinspection PyUnusedLocal
        def __init__(self):
            pass

        @cached_property
        def prop(self):
            return 5

    assert MyClass().prop == 5

# Generated at 2022-06-13 20:39:51.858794
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio
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

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:39:56.755808
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    def mock_function():
        return 0

    cp = cached_property(mock_function)
    class Object:
        pass

    obj = Object()
    value = cp.__get__(obj)
    assert value == 0


@pytest.mark.asyncio
async def test_cached_property_coroutine_property():

    @asyncio.coroutine
    def mock_function():
        return 0

    cp = cached_property(mock_function)

    class Object:
        pass

    obj = Object()
    value = cp.__get__(obj)
    value = await value
    assert value == 0

# Generated at 2022-06-13 20:39:57.589739
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:40:08.000358
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # test for class cached_property
    class MyClass:
        @cached_property
        def x(self):
            return 'foo'

        @cached_property
        def y(self):
            return 'bar'

    obj = MyClass()

    assert obj.__dict__ == {}
    assert obj.x == 'foo'
    assert obj.__dict__ == {'x': 'foo'}
    assert obj.y == 'bar'
    assert obj.__dict__ == {'x': 'foo', 'y': 'bar'}
    assert obj.x == 'foo'
    assert obj.__dict__ == {'x': 'foo', 'y': 'bar'}
    assert obj.y == 'bar'
    assert obj.__dict__ == {'x': 'foo', 'y': 'bar'}
   

# Generated at 2022-06-13 20:40:19.195252
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from pytest import raises
    from unittest.mock import Mock, patch

    # When called with obj=None
    func = Mock()
    cached_property_class = cached_property(func)
    assert func == cached_property_class.__get__(None, None)
    assert func.call_count == 0

    # When called with obj!=None
    obj = Mock()
    cached_property_class.func = Mock(return_value=None)
    assert None is cached_property_class.__get__(obj, None)
    assert cached_property_class.func.call_count == 1
    assert obj.__dict__['func'] is None

    # When func is a coroutine function

# Generated at 2022-06-13 20:40:26.923726
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Get the current loop
    loop = asyncio.get_event_loop()

    class MyClass:

        count = 0

        def __init__(self):
            self.x = 5

        @asyncio.coroutine
        def count_up(self):
            self.count += 1
            return self.count

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.count_up()

    c = MyClass()
    assert c.y == 6

    # Fetch a coro that wraps the cached property
    coro = c.z

    # Run the coro once
    loop.run_until_complete(coro)

    # `count_up` coroutine is run once and then cached
    assert c

# Generated at 2022-06-13 20:41:49.296962
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    expected = 6
    actual = obj.y
    assert expected == actual
    assert isinstance(actual, int)

# Generated at 2022-06-13 20:41:53.791372
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    test = Test()
    assert test.y == 6

# Generated at 2022-06-13 20:41:58.133887
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:
        @cached_property
        def test_getter(self):
            return 4

    test_object = TestClass()
    test_object.test_getter
    assert isinstance(test_object.test_getter, asyncio.futures.Future)
    assert test_object.test_getter.result() == 4


# Generated at 2022-06-13 20:42:03.686549
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # noinspection PyTypeChecker
    assert obj.y == 6



# Generated at 2022-06-13 20:42:10.701896
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # Verify that the value is set and returned
    assert obj.y == 6

    # Delete the value and make sure that the cached property is reset
    del obj.y
    assert obj.y == 6



# Generated at 2022-06-13 20:42:21.061736
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestCachedProperty:
        a = 3
        b = 4

        @cached_property
        def c(self):
            return self.a + self.b

    # Should cache result
    t = TestCachedProperty()
    t.c
    assert t.c == 7
    assert t.c == 7

    # Should recalculate result when attribute is deleted
    delattr(t, 'c')
    assert t.c == 7
    assert t.c == 7

    t.a = 5
    t.b = 6

    # Should recalculate result when attribute is deleted
    delattr(t, 'c')
    assert t.c == 11

    # Should calculate result when attribute is overwritten
    t.c = 12
    assert t.c == 12

# Generated at 2022-06-13 20:42:29.976154
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method cached_property.__get__ of class cached_property."""

    import pytest

    from .decorators import cached_property

    class Foo:

        @cached_property
        def bar(self):
            return 'bat'

    class Boo:

        @cached_property
        @asyncio.coroutine
        async def baz(self):
            return 'baz'

    foo = Foo()
    boo = Boo()

    assert hasattr(foo, 'bar') is False
    assert hasattr(foo, '__dict__') is True
    assert hasattr(foo.__dict__, 'bar') is False
    assert foo.bar == 'bat'
    assert hasattr(foo, 'bar') is True
    assert hasattr(foo, '__dict__') is True

# Generated at 2022-06-13 20:42:38.509217
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    global var

    class Cls:

        @cached_property
        def prop(self):
            return 1

    obj = Cls()
    assert obj.prop == 1
    assert obj.__dict__ == {'prop': 1}

    class Cls2:

        @cached_property
        def prop(self):
            return var

    var = 1
    obj = Cls2()
    assert obj.prop == 1
    assert obj.__dict__ == {'prop': 1}

    var = 2
    assert obj.prop == 1

