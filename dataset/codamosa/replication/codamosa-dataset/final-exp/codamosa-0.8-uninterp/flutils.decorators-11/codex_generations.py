

# Generated at 2022-06-13 20:32:52.712636
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Define a class
    class MyClass:
        # Define the cached_property decorator
        @cached_property
        # Define the property
        def y(self):
            return self.x + 1

        # Define the instance attribute x
        def __init__(self):
            self.x = 5

    # Instantiate the class
    obj = MyClass()

    # Demonstrate the property only executes once
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6

    # Demonstrate the property is not recalculated
    # if the instance attribute is reset
    obj.x = 10
    assert obj.y == 6
    obj.x = 15
    assert obj.y == 6

    # Demonstrate the property can be deleted
    # to force recal

# Generated at 2022-06-13 20:33:04.481579
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class :class:`~flutils.decorators.cached_property`."""

    from flutils.decorators import cached_property
    from unittest import mock

    # Setup
    obj = mock.MagicMock()
    expected = mock.MagicMock()
    obj.__dict__ = {'x': expected}
    obj.x = mock.PropertyMock(side_effect=obj.__dict__.setdefault)
    cls = mock.MagicMock()
    func = mock.MagicMock(__doc__='This is a docstring.')
    func.__name__ = 'x'
    func.__get__ = mock.MagicMock(return_value=func)
    cp = cached_property(func)

    # Execute
    result = cp.__

# Generated at 2022-06-13 20:33:09.679737
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    x = 5

    class MyClass:

        def __init__(self):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:33:17.092523
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio

    # Create test object
    class Test:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Run tests
    obj = Test()
    obj.y
    assert obj.__dict__['y'] == 6
    assert obj.y == 6



# Generated at 2022-06-13 20:33:26.079620
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock, NonCallableMock

    with_obj = Mock(spec=['__dict__', '__get__'])
    without_obj = Mock(spec=['__dict__', '__get__'])
    with_obj.__dict__ = {'__obj_key': '__obj_val'}
    without_obj.__dict__ = {'__cls_key': '__cls_val'}

    class TestClass:
        pass

    test_class_obj = TestClass()
    test_class_obj.__dict__ = {'test_val': 'test_val_val'}

    def test_func(obj):
        test_func_obj = obj

# Generated at 2022-06-13 20:33:31.333225
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """This is the doc string for y."""
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:33:38.293697
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    @cached_property
    def the_answer(self):
        return 42

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Test a property that returns an int
    obj = MyClass()
    assert the_answer(obj) == 42
    assert obj.y == 6

    # Test a property that returns a future
    import asyncio

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:33:47.562348
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from datetime import datetime
    from flutils.decorators import cached_property

    class TestClass:
        def __init__(self):
            self.x = 1

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        async def z(self):
            return self.x + 1

    # If a class is passed as the first argument
    test_class = TestClass()

    # Test method y is returned as expected
    assert test_class.y == 2

    # Test if result is cached as an attribute
    assert test_class.__dict__ == {'x': 1, 'y': 2}

    # Test if result is cached for subsequent calls
    assert test_class.y == 2

    # Test method z is returned as expected

# Generated at 2022-06-13 20:33:49.163223
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass
#############################################################################
# END

# Generated at 2022-06-13 20:34:00.443463
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test get in class scope

    class TestClass:
        @cached_property
        def dummy(self):
            return None

    TestClass.dummy

    # Test get in instance scope

    class TestClass:
        @cached_property
        def dummy(self):
            return None

    TestClass().dummy

    # Test get with a coroutine in class scope

    class TestClass:
        @cached_property
        async def dummy(self):
            return None

    TestClass.dummy

    # Test get with a coroutine in instance scope

    class TestClass:
        @cached_property
        async def dummy(self):
            return None

    TestClass().dummy

    # Test get with a coroutine in class scope


# Generated at 2022-06-13 20:34:07.429118
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from .helpers import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:34:15.551162
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    class MyClass:  # noqa: N801
        """Simple MyClass class for testing."""

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """docstring"""
            return self.x + 1

        @cached_property
        async def z(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x + 1

    assert MyClass.y.__doc__ == 'docstring'
    obj = MyClass()
    assert obj.y == 6
    assert isinstance(obj.z, asyncio.Future)
    assert isinstance(obj.z, asyncio.Future)

# Generated at 2022-06-13 20:34:20.885834
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # 1. Arrange
    class FooBar:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    # 2. Act
    x = FooBar(5)

    # 3. Assert
    assert x.y == 6
    assert x.y == 6



# Generated at 2022-06-13 20:34:29.371777
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest.mock
    from flutils.decorators import cached_property
    from unittest.mock import PropertyMock

    def func_coroutine_prop(self):
        return 1

    def func_prop(self):
        return 2

    class TestObj:
        @cached_property
        def prop_1(self):
            return 1

        @cached_property
        def prop_2(self):
            return 2

        @cached_property
        def prop_3(self):
            return 3

        @cached_property
        def prop_3(self):
            return 4

        @cached_property
        def prop_4(self):
            return 5

    obj_a = TestObj()

    assert obj_a.prop_1 == 1
    assert obj_a.prop_

# Generated at 2022-06-13 20:34:37.622514
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests method :meth:`cached_property.__get__`.
    """
    class Foo:
        """Class Foo.
        """
        _bar = None

        @cached_property
        def bar(self):
            """Property bar.
            """
            return self._bar

    obj = Foo()
    assert obj.bar is None

    obj._bar = True
    assert obj.bar is True
    obj._bar = False
    assert obj.bar is True

    del obj.bar
    assert obj.bar is False

    obj._bar = True
    assert obj.bar is True



# Generated at 2022-06-13 20:34:43.300912
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Y:

        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            self.x += 1
            return self.x

    # Test: method __get__
    y = Y()
    assert y.y == 1
    assert y.y == 1
    assert y.x == 1



# Generated at 2022-06-13 20:34:53.985252
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Tests the cached_property.__get__ method.

    """

    import inspect
    import asyncio

    # noinspection PyUnusedLocal
    class Example:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = Example(5)
    assert obj.y == 6
    obj.x = 6
    assert obj.y == 6

    # noinspection PyUnusedLocal
    class Example:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = Example(5)
    assert obj.y == 6
    del obj.y
    obj.x = 6
   

# Generated at 2022-06-13 20:35:00.174033
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Unit test for method __get__ of class cached_property

    """

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6


# Generated at 2022-06-13 20:35:09.472988
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Dummy:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """A number."""
            return self.x + 1

    obj = Dummy()
    assert obj.y == 6
    assert obj.__dict__["y"] == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.__dict__["y"] == 6



# Generated at 2022-06-13 20:35:14.603108
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import sys
    import inspect

    # noinspection PyProtectedMember
    module = sys.modules[__name__]
    cls = cached_property
    # noinspection PyProtectedMember
    method = module._test_cached_property__get__

    sig = inspect.signature(method)
    assert len(sig.parameters) == 1
    assert 'obj' in sig.parameters



# Generated at 2022-06-13 20:35:21.473382
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-13 20:35:28.929333
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # type: () -> None
    from unittest.mock import MagicMock
    from flutils.decorators import cached_property

    class A():

        def func(self, obj):
            return obj

        @cached_property
        def attr(self):
            return self.func(self)

    a1 = A()

    assert a1.attr == a1
    assert a1.attr == a1.attr



# Generated at 2022-06-13 20:35:33.868713
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Foo()
    obj.y


# Generated at 2022-06-13 20:35:41.217704
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass(object):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Docstring for method ``y`` of class ``MyClass``."""
            return self.x + 1

    myobj = MyClass()
    assert (
        myobj.__class__.__dict__["y"].__doc__
        == "Docstring for method ``y`` of class ``MyClass``."
    )
    assert myobj.y == 6

# Generated at 2022-06-13 20:35:51.848004
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():


    def is_cached_property(obj):
        return isinstance(obj, cached_property)


    class MyClass:
        """
        """

        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            self.x += 1
            obj = self

            def f():
                return obj

            return f()

        @cached_property
        def z(self):
            self.x += 1
            obj = self

            @asyncio.coroutine
            def f():
                return obj

            return f()


    def test_cached_property___get__():
        assert is_cached_property(MyClass.y)
        assert is_cached_property(MyClass().y)

        my_obj = MyClass()

        assert my

# Generated at 2022-06-13 20:35:55.489585
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class C:
        @cached_property
        def p(self):
            return 5

    c = C()
    assert c.p == 5
    assert c.__dict__['p'] == 5

# Generated at 2022-06-13 20:36:04.361463
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Obj:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Returns x + 1"""
            return self.x + 1

    obj = Obj()

    # Testing property of a class
    assert Obj.y == Obj.y
    assert Obj.y == Obj.__dict__['y']

    # Testing value of obj.y
    assert obj.y == 6
    assert obj.y == obj.__dict__['y']

    # Testing deletion of obj.y
    del obj.y
    assert obj.y == 6

    # Ensure property still works
    assert Obj.y == Obj.y
    assert Obj.y == Obj.__dict__['y']

    # Ensure property still works on obj
    assert obj.y == 6
    assert obj.y

# Generated at 2022-06-13 20:36:15.563286
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # noinspection PyPep8Naming
    class MyClass:
        def __init__(self):
            self.x = 5
            self.call_count = 0

        @cached_property
        def y(self):
            self.call_count += 1
            return self.x + 1

    obj = MyClass()
    assert obj.call_count == 0
    assert obj.y == 6
    assert obj.call_count == 1
    assert obj.y == 6
    assert obj.call_count == 1
    del obj.y
    assert obj.call_count == 1
    assert obj.y == 6
    assert obj.call_count == 2



# Generated at 2022-06-13 20:36:16.441823
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass



# Generated at 2022-06-13 20:36:21.230089
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class _property:
        @cached_property
        def x(self):
            return "x"

    property = _property()
    assert property.__dict__ == {}
    assert property.x == "x"
    assert "x" in property.__dict__
    assert property.__dict__["x"] == "x"



# Generated at 2022-06-13 20:36:32.457993
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass


# Generated at 2022-06-13 20:36:40.901178
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        @cached_property
        def y(self):
            return self.x + 1

        def __init__(self):
            self.x = 5

    def test_method_is_class_method():
        try:
            MyClass().y
            assert False
        except AttributeError as e:
            assert 'MyClass' in repr(e)
            assert "'NoneType' object has no attribute 'x'" in repr(e)

    def test_method_is_instance_method():
        assert MyClass().y == 6



# Generated at 2022-06-13 20:36:49.236813
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    import logging
    import pytest
    import time
    import unittest.mock

    from flutils.decorators import cached_property

    logger = logging.getLogger(__name__)

    @cached_property
    def foo():
        # If this raise is triggered, it will be caught by the base
        # exception in __get__().
        raise OSError('foo')

    class Test:
        foo = foo

    t = Test()

    with unittest.mock.patch.object(logging, 'exception') as patched:
        with pytest.raises(OSError):
            t.foo

    patched.assert_called_once()

    foo.__get__(t, Test)


# Generated at 2022-06-13 20:37:00.574329
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property

    *New in version 0.2.0*
    """

    # step 1: define a class
    class myClass:

        # step 1a: define a method
        def method_a(self, x):
            return x

    # step 2: instantiate the class
    obj = myClass()

    # step 3: create an instance of the cached_property descriptor
    desc = cached_property(obj.method_a)

    # step 4: simulate an attribute access, which calls __get__
    #         this should call the underlying method and return
    #         the value of x.
    desc.__get__(obj, str)
    assert obj.__dict__['method_a'] == 5

# Generated at 2022-06-13 20:37:12.585700
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from unittest.mock import patch
    from typing import Any

    # Define a function that is coroutine
    @asyncio.coroutine
    def coro(_: Any):
        return True

    # Define a class with a coroutine as a cached property
    class X(object):

        @cached_property
        def x(self):
            return coro(None)

    # A mock of the iscoroutinefunction method
    iscoroutinefunction = patch(
        "asyncio.iscoroutinefunction",
        side_effect=ValueError("iscoroutinefunction")
    ).start()

    # Define a class with a non coroutine function as a cached property
    class Y(object):
        @cached_property
        def y(self):
            return True

    # Make sure the cor

# Generated at 2022-06-13 20:37:21.593819
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:

        def __init__(self):
            self.a = 0

        @cached_property
        def b(self):
            return self.a + 1

    inst = TestClass()

    assert inst.b == 1
    assert inst.__dict__ == {'a': 0, 'b': 1}

    assert inst.b == 1
    assert inst.__dict__ == {'a': 0, 'b': 1}

    assert TestClass.b.__doc__ is None
    assert TestClass.b.func.__doc__ is None

    inst.a = 1

    assert inst.b == 2
    assert inst.__dict__ == {'a': 1, 'b': 2}

    assert TestClass.b.__doc__ is None
    assert TestClass.b.func.__doc__ is None

   

# Generated at 2022-06-13 20:37:28.418079
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests ``cached_property.__get__`` method.

    Test to verify that the ``__get__`` method returns a wrapped coroutine
    function if the ``func`` is an async function.

    """

    class TestClass:

        def __init__(self):
            self._y = 5

        @cached_property
        async def y(self):
            return self._y + 1

    TC = TestClass()
    assert isinstance(TC.y, types.CoroutineType)

# Generated at 2022-06-13 20:37:36.335692
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    assert MyClass().y == 6

    class MyClassAsync:

        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def y(self):
            yield from asyncio.sleep(1)
            return self.x + 1

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(MyClassAsync().y)
    assert result == 6

    # test for return value == self when obj is None
    assert cached_property(lambda obj: 6)(obj=None) == cached_property(lambda obj: 6)

# Generated at 2022-06-13 20:37:47.736986
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest
    from unittest.mock import patch, call

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    with patch('flutils.decorators.asyncio.ensure_future') as ens_fut:
        with patch('flutils.decorators.cached_property.func'):
            obj = MyClass()
            obj.y

    assert ens_fut.call_count == 1
    assert ens_fut.mock_calls == [call(MyClass.y.func)]

# Generated at 2022-06-13 20:37:57.534619
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Test that instance attribute is returned
    obj = MyClass()
    assert obj.y == 6
    assert isinstance(obj.y, int)

    # Test that class attribute is returned
    obj = MyClass
    assert obj.y == 6
    assert isinstance(obj.y, cached_property)

    # Test that instance attribute persists
    assert obj.x == 5
    assert MyClass().x == 5
    assert MyClass.x == 5



# Generated at 2022-06-13 20:38:23.141418
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit tests for method cached_property.__get__."""

    class Test:

        x = 5

        @cached_property
        def y(self):
            return self.x + 1

    test = Test()

    test.x = 2
    assert test.y == 3

# Generated at 2022-06-13 20:38:37.097458
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test of method __get__ of class cached_property."""

    import math

    class MyClass:
        def __init__(self, x=5):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def sqrt(self):
            return math.sqrt(self.x)

    obj1 = MyClass()
    obj2 = MyClass()
    obj3 = MyClass(4)
    obj4 = MyClass(4)

    assert obj1.y == obj2.y == 6
    assert obj3.sqrt == obj4.sqrt == 2.0

    obj1.x = 4
    assert obj1.y == obj2.y == 5
    assert obj1.sqrt == obj2.sqrt

# Generated at 2022-06-13 20:38:45.788514
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # test __get__
    class Foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # test class attribute and default value
    obj = Foo()
    assert obj.y == 6

    # test setting
    obj.x = 10
    assert obj.y == 11

    # test deletion
    del obj.y
    assert obj.y == 11



# Generated at 2022-06-13 20:38:49.965973
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert 6 == obj.y
    assert 6 == obj.__dict__['y']



# Generated at 2022-06-13 20:38:50.632720
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:38:57.425866
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Obj:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Obj()
    assert obj.y == 6
    obj.x = 10
    assert obj.y == 6
    delattr(obj, "y")
    assert obj.y == 11

# Generated at 2022-06-13 20:39:01.673589
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:39:07.497846
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class C:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1


    c = C()
    D = C.__dict__
    assert D['y'].__get__(c) == 6
    assert D['y'].__get__(c) == 6
    assert D['y'].__get__(c) == 6



# Generated at 2022-06-13 20:39:13.163598
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self, value: int):
            self.x = value

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(5)
    assert obj.y == 6
    del obj.y
    obj.x = 6
    assert obj.y == 7

# Generated at 2022-06-13 20:39:25.642722
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Setup
    class MyClassProp:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class MyClassAsyncProp:
        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def y(self):
            yield from asyncio.sleep(0.01)
            return self.x + 1

    # Exercice
    # Sync
    obj = MyClassProp()
    assert obj.__dict__ == {"x": 5}
    value = obj.y
    assert obj.__dict__ == {"x": 5, "y": 6}
    assert value == 6

    # Async
    obj = MyClassAsyncProp()

# Generated at 2022-06-13 20:40:16.187319
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""
    import inspect
    import time

    class MyClass:

        @cached_property
        def func(self):
            time.sleep(5)
            return "hi"

    obj = MyClass()
    start = time.perf_counter()
    assert obj.func == obj.func  # When using the same cached_property (i.e. obj.func)
    obj.func
    t1 = time.perf_counter() - start
    obj.func
    t2 = time.perf_counter() - start
    assert t1 == t2

    obj = MyClass()
    assert inspect.iscoroutine(obj.func)

# Generated at 2022-06-13 20:40:23.664440
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import TestCase, mock

    class CachedPropertyTestClass(TestCase):

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.test_obj = CachedProperty()

        def test_cached_property___get__(self):
            self.test_obj.mock = mock.Mock(name='mock method')
            self.test_obj.mock.return_value = 'mock return value'
            self.assertEqual(self.test_obj.mock, 'mock return value')

# Generated at 2022-06-13 20:40:27.960912
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

# Generated at 2022-06-13 20:40:29.406081
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class :any:`cached_property`"""
    import doctest

    print("Running tests for cached_property::__get__()")
    doctest.testmod(optionflags=doctest.ELLIPSIS)

# Generated at 2022-06-13 20:40:36.633511
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Base:

        def __init__(self, x=5):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = Base()
    obj.y

    assert obj.y == 6
    assert obj.__dict__['y'] == 6

    obj = Base(x=10)
    obj.y

    assert obj.y == 11
    assert obj.__dict__['y'] == 11

    assert Base.y.__get__(None)(obj) == 11



# Generated at 2022-06-13 20:40:42.266180
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
    assert obj.y == 6
    obj.x = 10
    assert obj.y == 6

# Generated at 2022-06-13 20:40:48.552558
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    @cached_property
    def b(self):
        return 'b'

    class Obj(object):
        a = b

    o = Obj()
    print(o.a)
    print(o.a)
    print(o.a)


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:40:55.427307
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from collections import namedtuple
    import asyncio
    from unittest.mock import MagicMock

    # Create class to cache values
    class MyClass:

        def __init__(self, x):
            self.x = x

        def y(self):
            return self.x + 1

    # Create a named tuple so that the dict() method can be called
    T = namedtuple('T', ['a', 'b'])

    # Create an object
    obj = T(1, 2)

    # Create a mock function
    mockfunc = MagicMock(return_value=3)

    # Create a mock coroutine function
    async def mockcorofunc():
        return 4

    # Create decorators
    dec1 = cached_property(mockfunc)
    dec2 = cached_property(mockcorofunc)

# Generated at 2022-06-13 20:41:07.641696
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached_property.__get__()"""
    class MyClass:

        def __init__(self, x=5):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    # https://realpython.com/python-mock-library/
    # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch
    # https://docs.python.org/3/library/unittest.mock.html#unittest.mock.PropertyMock
    with patch.object(MyClass, "__init__", return_value=None):
        with patch.object(MyClass, "y", new_callable=PropertyMock) as mock_y:
            mock_y.return_

# Generated at 2022-06-13 20:41:11.383794
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property.

    """

    # TODO: write unit test

    return True



# Generated at 2022-06-13 20:42:39.808082
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