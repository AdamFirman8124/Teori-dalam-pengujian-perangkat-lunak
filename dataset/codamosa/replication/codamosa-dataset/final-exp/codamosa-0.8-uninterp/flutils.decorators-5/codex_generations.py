

# Generated at 2022-06-13 20:32:42.288837
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test with non-coroutine decorated method
    class A:

        @cached_property
        def foo(self):
            return 5

    a = A()
    assert a.foo == 5
    assert a.__dict__ == {'foo': 5}
    a.foo = 6
    assert a.foo == 6
    assert a.__dict__ == {'foo': 6}

    # Test with coroutine decorated method
    class B:

        @cached_property
        @asyncio.coroutine
        def bar(self):
            return 10

    b = B()
    assert asyncio.iscoroutinefunction(B.bar.func)

    async def coro():
        return b.bar

    coro_result = asyncio.get_event_loop().run_until_complete(coro())
    assert coro

# Generated at 2022-06-13 20:32:53.772131
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property.
    """

    class AClass:
        """A class to test cached_property.__get__
        """

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    # Test the case where obj is not None
    a_obj = AClass(5)
    assert callable(a_obj.y)
    assert a_obj.y == 6
    assert a_obj.__dict__ == {'x': 5, 'y': 6}

    # Test the case where obj is None and cls is not None
    a_cls = AClass
    assert isinstance(a_cls.y, cached_property)

    # Test the case where obj is None

# Generated at 2022-06-13 20:33:03.252995
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method `cached_property.__get__`."""

    class TestClass:

        @cached_property
        def cached_property_test(self):
            return 1

    obj = TestClass()
    assert obj.cached_property_test == 1
    obj.__dict__['cached_property_test'] = 5
    assert obj.cached_property_test == 5
    del obj.__dict__['cached_property_test']
    assert obj.cached_property_test == 1
    assert obj.__dict__ == {'cached_property_test': 1}


# Generated at 2022-06-13 20:33:13.326422
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of cached_property."""
    from sys import version_info as py_version_info

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Dummy doc."""
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    assert obj.y.__class__.__name__ == 'int'
    assert isinstance(obj.y, int)
    assert isinstance(obj.__dict__['y'], int)

    if py_version_info.major >= 3 and py_version_info.minor >= 8:
        assert obj.y is obj.__dict__['y']



# Generated at 2022-06-13 20:33:20.427897
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class C:
        def __init__(self, v):
            self.x = v

        @cached_property
        def y(self):
            return self.x + 1
    obj = C(5)
    assert(obj.y == 6)
    assert(obj.__dict__ == {'x': 5, 'y': 6})



# Generated at 2022-06-13 20:33:23.529395
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



# Generated at 2022-06-13 20:33:29.841526
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
    value = obj.y
    assert value == 6
    value = obj.y
    assert value == 6



# Generated at 2022-06-13 20:33:37.548982
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
    assert foo.x == 5

    # noinspection PyStatementEffect
    foo.x
    assert foo.x == 5

# Generated at 2022-06-13 20:33:44.536888
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from collections import namedtuple
    from urllib.request import urlopen

    class MyClass:

        def __init__(self, url):
            self.url = url

        @cached_property
        def web_page(self):
            return urlopen(self.url)

    obj = MyClass('https://bit.ly/2mCg9hx')
    assert isinstance(obj.web_page, urlopen)
    assert id(obj.web_page) == id(obj.web_page)



# Generated at 2022-06-13 20:33:57.969106
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method ``__get__`` of class ``cached_property``

    Source:
        https://bit.ly/2PF8ZgW
        http://bit.ly/31SbOGY

    """

    from flutils.misc import random_string

    def A():
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    def B():
        def __init__(self, x):
            self.x = x

        @cached_property
        async def y(self):
            await asyncio.sleep(0.1)
            return self.x + 1

    def test_case(cls):
        obj = cls(5)
        assert obj.y == 6

# Generated at 2022-06-13 20:34:11.320886
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    def test_with_coroutine(func):
        @cached_property
        def fn(self):
            """Coroutine function."""
            return func(self)

        class Foo:
            @fn
            async def bar(self):
                """Coroutine function."""
                return 1

        foo = Foo()
        assert foo.bar == 1

        foo.bar = 2
        assert foo.bar == 2

    def test_without_coroutine(func):
        @cached_property
        def fn(self):
            """Coroutine function."""
            return func(self)

        class Foo:
            @fn
            def bar(self):
                """Coroutine function."""
                return 1

        foo = Foo()
        assert foo.bar == 1

        foo.bar = 2
        assert foo.bar == 2


# Generated at 2022-06-13 20:34:22.914984
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6

    # Test function marked as coroutine
    async def silly_coroutine(value):
        await asyncio.sleep(0.01)
        return value

    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return silly_coroutine(100)

    obj = TestClass()
    assert isinstance(obj.y, asyncio.Future)
    assert obj.y.done() is False
    assert obj.y.result() == 100

# Generated at 2022-06-13 20:34:29.926881
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5
            self.y = 5

        @cached_property
        def z(self):
            self.y = self.y + 1
            return self.x + self.y

    obj = MyClass()
    z = obj.z

    # The attribute cached_property is set
    assert obj.__dict__ == {'x': 5, 'y': 6, 'z': 11}

    # The attribute cached_property is replaced with a standard attribute
    assert obj.z == 11

    # The cached_property attribute is not updated
    obj.x = 10
    assert obj.z == 11

    # The cached_property attribute can be reset
    del obj.z
    assert obj.__dict__ == {'x': 10, 'y': 6}

   

# Generated at 2022-06-13 20:34:39.575285
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    import unittest.mock

    sys = unittest.mock.MagicMock()
    sys.__doc__ = 'mock sys.__doc__'
    sys.__name__ = 'mock sys.__name__'
    sys.version = 'mock sys.version'

    class MockModule(unittest.mock.MagicMock):
        __spec__ = 'mock module spec'
        __package__ = 'mock module pkg'
        __path__ = 'mock module path'


# Generated at 2022-06-13 20:34:45.266514
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Unit test for method __get__ of class cached_property
    """

    from types import FunctionType

    def func(obj):
        ...

    obj = cached_property(func)
    assert isinstance(obj.__get__(None, type), FunctionType)

    assert isinstance(obj.__get__(object, type), cached_property)

# Generated at 2022-06-13 20:34:55.701894
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Method must return self when obj is None
    m = cached_property(lambda _: None)
    assert m == m.__get__(None, None)

    # Method must return self.func.__name__ from obj.__dict__ when available
    def func(obj):
        return obj.__dict__['key']

    obj = type('MyClass', (), {})()
    obj.__dict__['key'] = 'value'
    m = cached_property(func)
    assert obj.__dict__['key'] == m.__get__(obj, None)

    # Method must return self.func(obj) when obj.__dict__ does not contain
    # self.func.__name__
    obj = type('MyClass', (), {})()
    m = cached_property(func)

# Generated at 2022-06-13 20:34:58.822379
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    cprop = cached_property(None)
    assert cprop.__get__(cprop, None) is cprop


if __name__ == '__main__':
    pytest.main([__file__])

# Generated at 2022-06-13 20:35:00.757953
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    log.warning("Won't be able to test method __get__() of class "
                "cached_property")

# Generated at 2022-06-13 20:35:11.415792
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from pytest import raises

    # Test class _MyClass
    class _MyClass:
        @cached_property
        def x(self):
            return 5

    # Test a standard call
    obj = _MyClass()
    result = obj.x
    assert result == 5

    # Test repeated call
    result = obj.x
    assert result == 5

    # Test on same instance with different name
    obj.x1 = 5
    result = obj.x1
    assert result == 5

    # Verify that property is only executed once
    with raises(AttributeError):
        obj.__dict__['x'] = 7



# Generated at 2022-06-13 20:35:19.941132
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method ``__get__`` of class ``cached_property``

    """

    import pytest
    import asyncio
    from functools import partial

    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    assert MyClass().y == 6

    def generation_func(x: int) -> int:
        return x + 1

    class MyAsyncClass:

        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def y(self):
            return generation_func(self.x)

    assert asyncio.run(MyAsyncClass().y)

# Generated at 2022-06-13 20:35:23.082437
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass


# vim: et:sw=4:syntax=python:ts=4:

# Generated at 2022-06-13 20:35:34.349750
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property
    """
    import math

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return math.sqrt(self.x)

    # This class should be instantiated w/out errors
    MyClass()

    obj = MyClass()
    # Test that y is being cached
    assert obj.y == math.sqrt(obj.x)

    obj.x = 2
    # Test that y is not being recomputed
    assert obj.y == math.sqrt(5)

    del obj.y
    # Test that y is being recomputed
    assert obj.y == math.sqrt(2)



# Generated at 2022-06-13 20:35:40.125618
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    # Setup
    class A:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = A()

    # Execute
    retval = obj.y

    # Verify
    assert retval == 6, "Test failed!"



# Generated at 2022-06-13 20:35:51.395754
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class C:
        counter = 0

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            C.counter += 1
            return C.counter + self.x

        @cached_property
        def z(self):
            C.counter += 1
            return C.counter + self.x

        @cached_property
        def w(self):
            C.counter += 1
            return C.counter + self.x

    obj = C()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    assert obj.y == 6
    assert obj.z == 7
    assert obj.__dict__['z'] == 7
    assert obj.w == 8
    assert obj.__dict__['w'] == 8
    assert obj

# Generated at 2022-06-13 20:36:02.521350
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    import asyncio
    from typing import Any, Optional

    class MyClass:
        pass

    @cached_property
    def test_method(obj):
        if hasattr(obj, 'x'):
            return 5 * obj.x
        else:
            return 10

    @pytest.mark.asyncio
    async def test_cached_property___get___async():
        class MyAsyncClass(MyClass):
            @cached_property
            async def test_method_async(obj):
                if hasattr(obj, 'x'):
                    return 5 * obj.x
                else:
                    return 10

        obj = MyAsyncClass()

        # assert not isinstance(obj.test_method_async, asyncio.Future)

# Generated at 2022-06-13 20:36:14.422682
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Get the value of y."""
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    assert obj.y.__doc__ == 'Get the value of y.'
    assert obj.__class__.y == cached_property
    assert MyClass.y == cached_property
    assert obj._MyClass__dict__['y'] == 6
    assert obj._MyClass__dict__['y'].__doc__ == 'Get the value of y.'


# Generated at 2022-06-13 20:36:18.994265
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils import decorators

    class MyClass:

        def __init__(self):
            self.x = 5

        @decorators.cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.x + 1 == 6
    assert obj.y == obj.x + 1
    assert obj.y == obj.y



# Generated at 2022-06-13 20:36:23.974049
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:36:29.494008
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Construct an object
    class Class:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Perform tests.
    obj = Class()
    assert obj.y == 6

    del obj.y
    assert obj.y == 6

# Generated at 2022-06-13 20:36:42.071398
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Shoe:

        # pylint: disable=R0201
        def __init__(self, weight):
            self.weight = weight
            self._some_attribute = None

        # @staticmethod
        def some_method(self):
            "test docstring"
            self._some_attribute = object()
            return self._some_attribute

        # @classmethod
        # def shoe_factory(cls, weight):
        #     return cls(weight)

        some_method = cached_property(some_method)

    shoe = Shoe(100.0)
    assert shoe.__dict__ == {'weight': 100.0}

    attr = shoe.some_method
    assert isinstance(attr, object)

# Generated at 2022-06-13 20:36:51.609574
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method `__get__` of class :obj:`cached_property`

    This unit test is not meant to be run as a standalone unit test.  It is a
    component of a larger test of the class.
    """

    @cached_property
    def foo(self):
        raise NotImplementedError

    obj = type('obj', (), {})()
    obj.__dict__['foo'] = 42

    assert foo.__get__(obj) == 42

    assert foo.__get__(obj) == 42

    assert foo.__get__(None) is foo



# Generated at 2022-06-13 20:37:02.914764
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock
    from .mixins import AsyncMockMixin

    class MyClass:

        def __init__(self):
            self.x = 5
            self.mock_func = MagicMock()

        @cached_property
        def y(self):
            return self.mock_func()

    obj = MyClass()

    assert obj.y == 5
    assert obj.mock_func.call_count == 1
    assert obj.y == 5
    assert obj.mock_func.call_count == 1

    # Test that the property is cached
    del obj.y
    assert obj.y == 5
    assert obj.mock_func.call_count == 2
    assert obj.y == 5
    assert obj.mock_func.call_count == 2



# Generated at 2022-06-13 20:37:14.872108
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method cached_property.__get__"""

    # Setup test class MyClass
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Setup test class MyCoroutineClass
    class MyCoroutineClass:

        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def y(self):
            return self.x + 1

    # Setup point of execution
    obj = MyClass()

    # Execute test
    expected = 6
    actual = obj.y

    # Verify results
    assert expected == actual, 'Expected {}. Actual {}'.format(expected,
                                                               actual)

    # Tear

# Generated at 2022-06-13 20:37:23.261213
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import sys
    import functools
    # noinspection PyPep8Naming
    @cached_property
    def f(self):
        """Do something"""

    # noinspection PyPep8Naming
    class C(object):
        # noinspection PyPep8Naming
        @cached_property
        def f(self):
            """Do something"""

    # noinspection PyPep8Naming
    class D(object):
        # noinspection PyPep8Naming
        @cached_property
        def f(self):
            """Do something"""

            @asyncio.coroutine
            def g():
                return 'something'
            return g()

    assert f.__get__(None) is f

    if sys.version_info >= (3, 8):
        assert f

# Generated at 2022-06-13 20:37:30.685031
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Test for first call
    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6

    # Test for second call
    assert obj.y == 6

    # Test for deletion
    del obj.y
    assert obj.y == 6


# Generated at 2022-06-13 20:37:44.334232
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Needed because this decorator has a special method (__get__) and we
    want to test that it works correctly.
    """

    class Class:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Class()
    assert isinstance(obj.__dict__["y"], asyncio.Future)
    assert obj.__dict__["y"].done()

    a = obj.y
    assert isinstance(a, asyncio.Future)
    assert a.done()

    b = obj.y
    assert a == b
    assert id(a) == id(b)
    assert a.done()
    assert b.done()

    c = obj.__dict__["y"]

# Generated at 2022-06-13 20:37:51.251633
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test with synchronous method
    class A:
        @cached_property
        def x(self):
            return 5

    a = A()
    assert a.__dict__ == {}
    assert a.x == 5
    assert a.__dict__ == {'x': 5}

    # Test with asynchronous method
    class B:
        @cached_property
        def x(self):
            return asyncio.sleep(0)

    b = B()
    assert b.__dict__ == {}
    assert isinstance(b.x, asyncio.Future)
    assert b.__dict__ == {'x': b.x}

    # Test with asynchronous method that returns a value
    class C:
        @cached_property
        def x(self):
            return asyncio.sleep(0, value=5)

   

# Generated at 2022-06-13 20:37:57.742519
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test the method __get__ of class cached_property.
    """

    class Tcached_property:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Tcached_property()
    assert obj.y == 6


if __name__ == '__main__':
    import sys
    import pytest
    pytest.main(sys.argv)

# Generated at 2022-06-13 20:37:58.600552
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass



# Generated at 2022-06-13 20:38:10.477165
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method ``cached_property.__get__``."""
    from time import time
    from .timed_run import timed_run
    from types import FunctionType

    class Test:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Property y."""
            time()
            return self.x + 1

    obj = Test()
    assert obj.__dict__.get('y') is None
    assert obj.y == 6
    assert isinstance(obj.y, int)
    assert obj.__dict__.get('y') == 6
    assert isinstance(obj.y, int)
    assert Test.y.__doc__ == "Property y."
    assert Test.y.__annotations__ == {}


# Generated at 2022-06-13 20:38:18.631767
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from flutils.decorators import cached_property

    # Test __get__ with no object
    class MyClass:
        @cached_property
        def y(self):
            return "foo"

    test = MyClass()
    assert test.y == "foo"



# Generated at 2022-06-13 20:38:27.869513
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test method __get__ of class cached_property
    """
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # Cached property
    assert obj.y == 6

    # Now a regular attribute
    assert obj.y == 6

    # Deletion of cached property
    del obj.y
    assert not hasattr(obj, 'y')

    # Cached property again
    assert obj.y == 6

# Generated at 2022-06-13 20:38:35.379359
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method :meth:`cached_property.__get__`

    :return: ``None``
    :rtype: None

    """
    class Temp(object):
        @cached_property
        def x(self):
            return 1

    test_ = Temp()
    assert test_.x == 1
    assert test_.x == 1
    assert test_.x == 1

# Generated at 2022-06-13 20:38:36.720384
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Tested in :class:`tests.test_decorators.TestDecorators`
    """
    pass


# Generated at 2022-06-13 20:38:46.617718
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from random import randint
    from flutils.decorators import cached_property

    # Tests __get__

    class MyClass:
        def __init__(self, x: int) -> None:
            self.x = x

        @cached_property
        def y(self) -> int:
            return self.x + 1

    myobj = MyClass(randint(0, 100))
    assert myobj.y == myobj.x + 1

    myobj = MyClass(5)
    assert myobj.y == myobj.x + 1



# Generated at 2022-06-13 20:38:54.454119
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
            """Method Z."""
            return self.x + 1

        @cached_property
        async def a(self):
            await asyncio.sleep(1)
            return self.x + 1

    assert MyClass.__dict__['y'].__doc__ == MyClass.__dict__['z'].__doc__ == \
        MyClass.__dict__['a'].__doc__ is None

    assert MyClass.y.__doc__ == MyClass.z.__doc__ == \
        MyClass.a.__doc__ == "Method Z."

    assert MyClass.__dict

# Generated at 2022-06-13 20:39:02.054447
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property."""

    # Cache the property
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    # obj.y

    # Delete the cached property
    del obj.y
    # obj.y  # Should not cause a error.



# Generated at 2022-06-13 20:39:13.053713
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from flutils.decorators import cached_property_class

    class Foo:

        @cached_property
        def method(self):
            """This method returns the string bar."""
            return "bar"

    foo = Foo()
    assert foo.method == "bar"
    assert foo.method == "bar"
    assert foo.method == "bar"
    assert foo.method.__doc__ == "This method returns the string bar."
    foo.method = "baz"
    assert foo.method == "baz"
    assert foo.method.__doc__ == "This method returns the string bar."
    del foo.method
    assert foo.method == "bar"
    assert foo.method.__doc__ == "This method returns the string bar."


# Generated at 2022-06-13 20:39:20.844121
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # ------------------------------------------------------------------------------------------------------------------
    def testfunc(obj):
        return obj.x

    # ------------------------------------------------------------------------------------------------------------------
    class TestClass:
        # noinspection PyShadowingBuiltins
        def __init__(self):
            self.x = 7

        y = cached_property(testfunc)

    # ------------------------------------------------------------------------------------------------------------------
    obj = TestClass()
    assert obj.y == 7



# Generated at 2022-06-13 20:39:27.941587
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Class1:
        @cached_property
        def meth1(self):
            print('meth1')
            return 1

    obj1 = Class1()
    # print(obj1.meth1)
    # print(obj1.meth1)
    assert obj1.meth1 == 1
    assert obj1.meth1 == 1

    class Class2:
        @cached_property
        async def meth2(self):
            print('meth2')
            await asyncio.sleep(0.001)
            return 2

    obj2 = Class2()
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(print(obj2.meth2))
    # loop.run_until_complete(print(obj2.meth2))
    # loop.run

# Generated at 2022-06-13 20:39:41.822699
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

        @cached_property
        def x(self):
            return self.y + 1

    my_class = MyClass(y=5)
    assert my_class.x == 6
    assert my_class.__dict__['x'] == 6


test_cached_property___get__()

# Generated at 2022-06-13 20:39:49.051598
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class Foo:
        def __init__(self):
            self.x = 1

        @cached_property
        def y(self):
            return self.x + 1

    class TestCachedProperty(unittest.TestCase):
        def testProperty(self):
            f = Foo()
            self.assertEqual(f.y, 2)

    unittest.main()

# Generated at 2022-06-13 20:39:55.416835
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
    assert obj.y == 11


# Generated at 2022-06-13 20:40:02.136769
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test(object):
        pass

    test = Test()
    @cached_property
    def get(self):
        return self

    test.get


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-13 20:40:05.692152
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:40:12.926222
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

    obj.x = 10

    assert obj.y == 6
    assert obj.__dict__['y'].__class__ is asyncio.Future


# Generated at 2022-06-13 20:40:19.511587
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    value = Test().y
    print(value)
    assert value == 6



# Generated at 2022-06-13 20:40:24.329946
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock

    instance = Mock(spec_set=['x'])
    instance.x.__doc__ = "Test property"
    func = Mock()
    func.__name__ = 'myProperty'

    cp = cached_property(func)
    cp.__get__(instance, None)

    assert instance.__dict__[func.__name__] == func.return_value



# Generated at 2022-06-13 20:40:27.922509
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


# Generated at 2022-06-13 20:40:31.299491
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio

    class C1:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class C2:
        def __init__(self):
            self.x = 5

  

# Generated at 2022-06-13 20:40:54.804577
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    from flutils.decorators import cached_property

    class MyClass():

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    obj.y
    assert obj.__dict__['y'] == 6

    obj.x = 7
    obj.y
    assert obj.__dict__['y'] == 6

    del obj.y
    obj.y
    assert obj.__dict__['y'] == 8



# Generated at 2022-06-13 20:41:00.215294
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class T:

        @cached_property
        def f(self):
            return 'f'

        @cached_property
        def g(self):
            return 'g'

    t = T()
    assert t.f == 'f'
    assert t.g == 'g'



# Generated at 2022-06-13 20:41:10.263153
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    print("\n====== test_cached_property___get__ ======")

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    print(f"obj.y = {obj.y}")

    print(f"obj.__dict__ = {obj.__dict__}")

    # After first access the property is replaced by a normal data attribute.
    # This attribute holds the value of the original function though.
    obj.y = 5
    print(f"obj.y = {obj.y}")
    print(f"obj.__dict__ = {obj.__dict__}")

    # Deleting the data attribute allows the property to be computed again.
    del attr

# Generated at 2022-06-13 20:41:13.998204
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

# Generated at 2022-06-13 20:41:21.393797
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Expected Values
    class C(object):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    expected = 6

    # Tested Code
    c = C()
    result = c.y

    # Returned Results
    assert result == expected



# Generated at 2022-06-13 20:41:28.653085
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self, val):
            self.val = val

        @cached_property
        def property(self):
            return self.val + 5

    tc = TestClass(10)
    assert tc.property == 15
    assert tc.__dict__ == {'val': 10, 'property': 15}

    # Exercise cached property
    assert tc.property == 15



# Generated at 2022-06-13 20:41:42.754351
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit tests for method ``__get__`` of :class:`cached_property`."""
    from time import sleep
    import warnings
    import functools

    class TestClass:
        """Test class for :class:`cached_property`."""

        @cached_property
        def y(self):
            """Y."""
            return self.x + 1

        @cached_property
        def x(self):
            """X."""
            return 5

        @cached_property
        def z(self):
            """Z."""
            return asyncio.coroutine(lambda: self.x * 2)()

    instance = TestClass()
    assert instance.y == 6  # pylint: disable=no-member

    instance.x = 10
    assert instance.y == 11  # pylint:

# Generated at 2022-06-13 20:41:47.952495
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock
    from .cached_property import cached_property
    cp = cached_property(MagicMock())
    obj = MagicMock()
    cls = MagicMock()
    cp.__get__(obj, cls)
    obj.__dict__.update({cp.func.__name__: MagicMock()})
    cp.__get__(obj, cls)

# Generated at 2022-06-13 20:41:53.276870
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test for method __get__
    # of class flutils.decorators.cached_property
    #
    # @return
    #

    obj = cached_property('x')
    obj.__get__(None, None)
    obj.__get__(None, None)


# Generated at 2022-06-13 20:41:58.169298
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    test = TestClass(5)
    assert(test.y == 6)

    # Unit test to verify that the property is cached.
    test.x = 6
    assert(test.y == 6)
