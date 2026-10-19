

# Generated at 2022-06-13 20:32:43.400606
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:

        def __init__(self):
            self.count = 0

        @cached_property
        def value(self):
            self.count += 1
            return 1

    test_obj = TestClass()

    # First access to @cached_property should evaluate @cached_property.func()
    # and store the result in __dict__
    assert test_obj.value == 1
    assert len(test_obj.__dict__) == 2
    assert test_obj.__dict__['value'] == 1
    assert test_obj.__dict__['count'] == 1

    # Second access to @cached_property should return the value stored in
    # __dict__; this time invoking @cached_property.func() should not occur
    assert test_obj.value == 1

# Generated at 2022-06-13 20:32:49.510752
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D103
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6  # noqa: E712,E721

# Generated at 2022-06-13 20:32:56.348074
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Test that getter function is only called once
    class Obj:
        def __init__(self, i):
            self.__i = i
            self.j = 0

        def __repr__(self):
            return f"Obj({self.__i}, {self.j}, {self.k})"

        # noinspection PyUnusedLocal
        @cached_property
        def k(self):
            self.j += 1
            return self.__i

    obj = Obj(1)
    assert obj.j == 0
    assert obj.k == 1
    assert obj.j == 1

    # Test that getter function is always called if the
    # cached property is deleted
    del obj.k
    assert obj.__dict__["k"] == 1
    assert obj.k == 1

# Generated at 2022-06-13 20:33:02.045745
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from typing import Any

    # noinspection PyUnusedLocal
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    value: Any = obj.y
    assert value == 6



# Generated at 2022-06-13 20:33:11.425260
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def y(self):
            yield from asyncio.sleep(1)
            return self.x + 1

    obj = MyClass()
    coro = obj.y
    assert isinstance(coro, asyncio.Future)
    assert not coro.done()
    assert obj.y == 6
    assert not coro.done()


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:33:20.962401
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    # Test with Python 3.8
    if sys.version_info[1] < 8:
        return

    from functools import cached_property

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # Prepare
    obj.x = 5

    # Test
    value = obj.y

    # Verify
    assert value == 6



# Generated at 2022-06-13 20:33:24.265526
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self):
            pass

        @cached_property
        def test(self):
            return 'test'

    instance = TestClass()
    assert isinstance(instance.test, str) is True
    assert instance.test == 'test'


# Generated at 2022-06-13 20:33:35.747034
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    class MyClass:

        def __init__(self, x: int = 5):
            self.x = x
            self._coroutine_ran = False

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        @asyncio.coroutine
        def z(self):
            self._coroutine_ran = True

    obj = MyClass()
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6

    loop = asyncio.get_event_loop()
    loop.run_until_complete(obj.z)
    assert obj.z == obj.z
    assert obj._coroutine_ran

    obj = MyClass(x=10)

# Generated at 2022-06-13 20:33:38.884323
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    from flutils.decorators import cached_property

    class _Test:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = _Test()
    assert obj.y == 6
    assert obj.x == 5
    obj.x = 7
    assert obj.y == 6
    obj.y = 13
    assert obj.y == 13



# Generated at 2022-06-13 20:33:44.058282
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return

    obj = MyClass()
    assert obj.y is None
    assert obj.__dict__['y'] is None

    # Test register path
    obj = MyClass()
    val = obj.y
    assert obj.y is val



# Generated at 2022-06-13 20:33:53.186216
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method cached_property.__get__"""

    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:33:54.605294
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    obj = MyClass()
    assert obj.y == 6


# Generated at 2022-06-13 20:33:58.065355
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

# Generated at 2022-06-13 20:34:04.352157
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from flutils.decorators import cached_property

    class Base:

        def __init__(self):
            pass

        @cached_property
        def y(self):
            return self.x + 1

    assert Base.y.__doc__ is None

    class Sub(Base):

        def __init__(self):
            self.x = 5

        @cached_property
        def z(self):
            return self.y + 1

    obj = Sub()
    assert obj.y == 6
    assert obj.z == 7
    assert isinstance(obj.y, asyncio.Future) is False

    # test property reset
    del obj.y
    assert obj.y == 6
    assert obj.z == 7

    class Base:

        def __init__(self):
            pass

       

# Generated at 2022-06-13 20:34:10.130774
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    logger = logging.getLogger()
    logger.setLevel('DEBUG')
    logger.addHandler(logging.NullHandler())

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:34:11.486099
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Currently this is tested in the test for class Resource
    return



# Generated at 2022-06-13 20:34:20.505290
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property

    :return: True if successful, False otherwise

    *New in version 0.7.0*
    """

    def ret_value(inst):
        return 5

    ck = cached_property(ret_value)

    class TestClass:
        pass

    test_class = TestClass()
    ck.__get__(test_class, TestClass)
    assert test_class.ret_value == 5

    return True



# Generated at 2022-06-13 20:34:26.008306
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class _TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = _TestClass()
    assert obj.y == 6
    del obj.y
    assert obj.y == 6
    del obj.y
    obj.y = 7
    assert obj.y == 7



# Generated at 2022-06-13 20:34:32.190954
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



# Generated at 2022-06-13 20:34:36.631196
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""
    class CacheGetClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = CacheGetClass()
    assert obj.y == 6


# Generated at 2022-06-13 20:34:43.536213
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj1 = MyClass()
    obj2 = MyClass()

    assert obj1.y == 6
    assert obj2.y == 6

# Generated at 2022-06-13 20:34:54.226661
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
    obj.x = 7
    assert obj.y == 7

    class MyClass2:

        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def y(self):
            yield from asyncio.sleep(1)
            return self.x + 1

    obj2 = MyClass2()
    obj2.__dict__['y'] = 'foo'
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Generated at 2022-06-13 20:35:04.298093
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # pylint: disable=invalid-name
    """unit test for method __get__ of class cached_property
    """
    from unittest.mock import patch

    myclass = type("myclass", (), {})

    myproperty = cached_property(lambda *args, **kwargs: None)
    myclass.myproperty = myproperty
    myinstance = myclass()

    myinstance.__dict__ = {}  # reset object

    myproperty.__get__(myinstance, myclass)
    assert "myproperty" in myinstance.__dict__



# Generated at 2022-06-13 20:35:14.818917
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests for the ``__get__`` method of the :class:`cached_property`
    class.
    """
    # from
    # https://github.com/pallets/werkzeug/blob/9452c01/src/werkzeug/utils.py#L831-L864
    class C:
        def __init__(self):
            self._x = None

        @cached_property
        def x(self):
            return "foo"

    c = C()
    assert c.__dict__ == {}
    assert c.x == "foo"
    assert c.__dict__ == {"_x": "foo"}
    # now caching kicks in
    c.x == "foo"
    assert c.__dict__ == {"_x": "foo"}

    # test for subclassing,

# Generated at 2022-06-13 20:35:28.750442
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio
    from flutils.decorators import cached_property

    class MyClass2:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass2()
    assert obj.y == 6

    class MyClass3:

        def __init__(self, delay=0.1):
            self.delay = delay

        @asyncio.coroutine
        @cached_property
        def y(self):
            yield from asyncio.sleep(self.delay)
            return self.x + 1

    obj = MyClass3(0.3)
    obj.x = 7
    obj.y = 9
    assert obj.y == 9



# Generated at 2022-06-13 20:35:34.553174
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import TestCase
    from unittest.mock import patch, call

    class MyTestClass(TestCase):
        @cached_property
        def foo(self):
            return 42


    obj = MyTestClass()
    assert obj.foo == 42

    # Subsequent accesses to `foo` return 42 without
    # getting called a second time
    with patch.object(MyTestClass, "foo") as m:
        obj.foo
        assert m.mock_calls == []



# Generated at 2022-06-13 20:35:44.621584
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from functools import partial
    from concurrent.futures import Future

    class A:

        x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x + 2

        @cached_property
        def w(self):
            future = asyncio.ensure_future(self.a())
            self.__dict__['w'] = future
            return future

        @cached_property
        def q(self):
            future = asyncio.ensure_future(self.a())
            self.__dict__['q'] = future
            return future

        @asyncio.coroutine
        def a(self):
            return self.x + 3

    a = A()
    assert a.__

# Generated at 2022-06-13 20:35:48.963399
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest
    class Test_cached_property___get__(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test__cached_property___get__(self):
            pass

    unittest.main()

# Generated at 2022-06-13 20:35:51.699456
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""
    import doctest

    doctest.testmod()


if __name__ == '__main__':
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 20:35:57.405431
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
    assert a.y == 6  # check that the cached_property decorator works


# Generated at 2022-06-13 20:36:06.342796
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def zz(self):
            return self.x + 3

    for _ in range(4):
        obj = MyClass()
        # Test that the property is not computed after initialization
        assert 'zz' not in obj.__dict__
        # Test that the property is computed after access
        assert obj.__dict__['zz'] == 8

    # Test that the property can be deleted from the instance
    obj = MyClass()
    assert 'zz' not in obj.__dict__
    assert obj.__dict__['zz'] == 8
    del obj.__dict__['zz']
    assert 'zz' not in obj.__dict__
    assert obj.__dict__['zz'] == 8



# Generated at 2022-06-13 20:36:14.057400
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from random import randrange
    from unittest.mock import Mock

    class Cached:
        def __init__(self):
            self.x = randrange(100)

        @cached_property
        def y(self):
            return self.x + 1

    o = Cached()
    assert o.y == o.x + 1

    # noinspection PyProtectedMember
    assert o.__dict__['y'] == o.x + 1



# Generated at 2022-06-13 20:36:17.673944
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    return type(MyClass().y)



# Generated at 2022-06-13 20:36:22.936667
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property."""

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:36:24.364176
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass



# Generated at 2022-06-13 20:36:31.442063
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self, num):
            self.num = num

        @cached_property
        def y(self):
            return 2 * self.num

    my_instance = MyClass(5)
    my_instance.y
    assert my_instance.y == 10
    assert my_instance.__dict__['y'] == 10

    my_instance.num = 6
    my_instance.y
    assert my_instance.y == 12
    assert my_instance.__dict__['y'] == 12



# Generated at 2022-06-13 20:36:35.749855
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""
    # Test for class cached_property
    class TestClass:

        @cached_property
        def test_property(self):
            return 5

    assert TestClass().test_property == 5



# Generated at 2022-06-13 20:36:39.273080
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    global foo

    @cached_property
    def foo():
        return "foo"

    assert foo == "foo"
    assert foo.__doc__ is None



# Generated at 2022-06-13 20:36:47.978574
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Basic: get @cached_property is as expected
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    # Setter: it works
    obj.y = 10
    assert obj.y == 10

    # Deleter: it works
    del obj.y
    assert obj.y == 6

    # Test property is already set
    assert obj.y == 6

    # Test property is already set
    assert obj.y == 6

    # Test property is set to exception
    obj.y = Exception()
    assert obj.y == 6

    # Test property is set to exception and then deleted
    obj.y = Exception()

# Generated at 2022-06-13 20:36:53.355910
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self, x):
            self._x = x

        @cached_property
        def x(self):
            return self._x

    a = A(1)

    # cached_property __get__ should return cached value
    assert a.x == 1

    # modify __dict__ as one would do to clear cached_property's cache
    a.__dict__.pop('x')

    # normal attributes should still work
    assert a._x == 1

    # cached_property __get__ should return cached value
    assert a.x == 1

# Generated at 2022-06-13 20:37:06.212355
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method `cached_property.__get__`

    """
    class MyClass:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    from pdb import set_trace
    set_trace()



# Generated at 2022-06-13 20:37:06.822277
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:37:17.548435
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    class _Foo:

        def __init__(self):
            self.x = 5
            self.y = 7
            self.z = 11
            self.a = 13

        @cached_property
        def bar(self):
            return self.x + 1

        @cached_property
        def baz(self):
            return self.y + 1

        @cached_property
        def qux(self):
            return self.z + 1

        @cached_property
        def quux(self):
            return self.a + 1

    foo = _Foo()
    del foo.__dict__["z"]

    assert foo.bar == 6
    assert foo.__dict__["bar"] == 6

# Generated at 2022-06-13 20:37:21.297835
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached property getter"""

    class TestClass:

        @cached_property
        def test_attr(self):
            return "test_attr"

    obj = TestClass()
    assert obj.test_attr == "test_attr"



# Generated at 2022-06-13 20:37:32.175486
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    class MyClass:
        def __init__(self):
            pass

        @cached_property
        def attr(self):
            return 1

    obj1 = MyClass()
    obj2 = MyClass()

    assert obj1.__dict__ == {}
    assert obj2.__dict__ == {}

    assert obj1.attr == 1
    assert obj2.attr == 1

    assert obj1.__dict__ == {'attr': 1}
    assert obj2.__dict__ == {'attr': 1}

    with pytest.raises(AttributeError):
        obj1.attr = 2

    with pytest.raises(AttributeError):
        del obj1.attr

    assert obj1.__dict__ == {'attr': 1}

    assert obj1.attr == 1

# Generated at 2022-06-13 20:37:46.003764
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from datetime import datetime
    from flutils.decorators import cached_property
    from pytest import mark, raises

    class SomeClass:

        def __init__(self):
            self._a = 0
            self._b = 1
            self._c = 2
            self._d = 3
            self._e = 4
            self._f = 5
            self._g = 6
            self._h = 7
            self._i = 8
            self._j = 9
            self._k = 10
            self._l = 11
            self._m = 12
            self._n = 13
            self._o = 14
            self._p = 15
            self._q = 16
            self._r = 17
            self._s = 18
            self._t = 19
            self._u = 20
            self._v = 21


# Generated at 2022-06-13 20:37:57.578993
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test for method __get__ of class cached_property

    This method tests attributes and methods of class cached_property.

    *New in version 0.2.0*
    """
    # Test decorated method is cached property
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    # noinspection PyStatementEffect
    obj.y
    assert obj.y == 6
    # Test decorated method is cached property
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5


# Generated at 2022-06-13 20:37:58.802773
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # TODO: write unit test
    pass


# Generated at 2022-06-13 20:38:10.687794
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import patch
    from flutils.logging import logger

    class FooBar:
        def __init__(self):
            self.x = 0

        @cached_property
        def foo(self):
            self.x += 1
            return self.x

    @patch.object(logger, "info")
    def test_it(log, mock_logger):
        fb = FooBar()
        assert fb.x == 0
        assert fb.foo == 1
        with pytest.raises(AttributeError):
            fb.__dict__.pop("foo")
            fb.foo
            mock_logger.assert_called_with(
                "Cannot retrieve attribute 'foo' in object <object of class "
                "'FooBar' at 0x000000000000>"
            )

# Generated at 2022-06-13 20:38:19.557128
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

if __name__ == "__main__":
    # Run all unit tests
    g = globals().copy()
    for k, v in g.items():
        if k.startswith("test_") and hasattr(v, "__call__"):
            v()

# Generated at 2022-06-13 20:38:40.188063
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import sys

    from flutils.decorators import cached_property

    # noinspection PyPep8Naming
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return asyncio.sleep(0.001, result=self.x + 2)

        @cached_property
        def a(self):
            return self.x + 3

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}
    del obj.y
   

# Generated at 2022-06-13 20:38:45.743901
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class C:

        def f(self):
            return 5

    obj = C()
    assert obj.f() == 5  # no cached_property

    obj.f = cached_property(obj.f)
    assert obj.f() == 5  # cached_property



# Generated at 2022-06-13 20:38:54.009471
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    #     async def async_call():
    #         print('async call')
    #         await asyncio.sleep(1)
    #         return 'compute result'

    class TestClass:
        @cached_property
        def no_async_call_method(self):
            return 'compute result'

        @cached_property
        def async_call_method(self):
            async def async_call():
                print('async call')
                await asyncio.sleep(1)
                return 'compute result'

            return asyncio.ensure_future(async_call())

    for i in range(3):
        test_obj = TestClass()
        print(test_obj.no_async_call_method)
        print(test_obj.async_call_method)

# Generated at 2022-06-13 20:38:54.798335
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:39:06.192606
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property

    """

    import unittest

    try:
        import asyncio
    except ImportError:
        asyncio = None

    class CachedPropertyTests(unittest.TestCase):

        @unittest.skipUnless(asyncio, "asyncio not available")
        def test_async_coroutine_method(self):

            class Foo:

                def __init__(self, a):
                    self.a = a

                @cached_property
                @asyncio.coroutine
                def barr(self):
                    return self.a

            coro = Foo(1).barr
            self.assertTrue(asyncio.iscoroutine(coro))

# Generated at 2022-06-13 20:39:11.368641
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



# Generated at 2022-06-13 20:39:22.307351
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import functools

    @functools.total_ordering
    class MyClass(object):

        # noinspection PyUnusedLocal
        def __init__(self):
            self.a = 1

        @cached_property
        def prop(self):
            return self.a

        def __eq__(self, other):
            return self.prop == other.prop

        def __lt__(self, other):
            return self.prop < other.prop

    assert MyClass().prop == 1
    assert MyClass() == MyClass()
    assert MyClass() != MyClass()


# Generated at 2022-06-13 20:39:25.833769
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import doctest

    doctest.run_docstring_examples(
        cached_property.__get__,
        globals(),
        name='cached_property.__get__',
        optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    )



# Generated at 2022-06-13 20:39:30.805882
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:39:37.313064
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
    a.x = 6
    assert a.y == 6
    del a.y
    assert a.y == 7



# Generated at 2022-06-13 20:40:11.574514
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # normal case
    class MyClass:
        def __init__(self):
            self.x = 5
        @cached_property
        def y(self):
            return self.x + 1
    obj = MyClass()
    assert obj.y == 6 # from cached_property

    # case where property is deleted and re-accessed
    del obj.y
    assert obj.y == 6 # from cached_property


# Generated at 2022-06-13 20:40:21.611968
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import mock

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Docstring"""
            return self.x + 1

    obj = MyClass()
    mock_func = mock.Mock()
    # obj.y is a method
    obj.y = mock_func
    # Execute cached_property.__get__
    cached_property(mock_func).__get__(obj, MyClass)
    # Verify mock_func was called
    assert mock_func.called is True
    mock_func.reset_mock()

    def leave_mock(self):
        return self.x + 1

    mock_func.side_effect = leave_mock
    # Execute cached_property.__get__

# Generated at 2022-06-13 20:40:27.137819
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test method __get__ of class cached_property.

    """
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:40:29.128696
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    def method(obj):
        return obj

    class MyClass:

        @cached_property
        def method(self):
            return method
    m = MyClass()
    assert m.method == method
    # noinspection PyUnresolvedReferences
    assert m.meth

# Generated at 2022-06-13 20:40:30.559290
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



# Generated at 2022-06-13 20:40:38.744672
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property
    """

    #######################################################################
    # Make a class that has a cached_property attribute
    #######################################################################
    class X:
        def __init__(self, x):
            self.x = x

        # noinspection PyUnusedLocal
        @cached_property
        def y(self):
            return self.x

    x = X(5)
    assert x.y == 5
    assert x.__dict__['y'] == 5

    #######################################################################
    # Make sure a cached_property attribute is only computed once
    #######################################################################
    x.__dict__['y'] = -1
    assert x.y == 5

    #######################################################################
    # Make sure a cached_property attribute is not computed unless accessed
    #################################

# Generated at 2022-06-13 20:40:43.499278
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest.mock

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    with unittest.mock.patch.object(MyClass, '__dict__', {'x': 5}):
        assert MyClass().y == 6



# Generated at 2022-06-13 20:40:47.723719
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

# Generated at 2022-06-13 20:40:54.855262
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Test method __get__ of class cached_property.
    """

    # Test with a class with a method.
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Cached property.
            """
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    # Test with a class with an asynchronous method.
    class MyClass2:

        def __init__(self, loop=None):
            self.x = 5
            self.loop = loop if loop else asyncio.new_event_loop()

        @cached_property
        async def y(self):
            """Cached property.
            """
            return self.x + 1

    obj = MyClass2()

# Generated at 2022-06-13 20:41:06.054817
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test to cover the cached_property decorator __get__
    method.  This tests that the cached_property decorator
    functions as intended.
    """
    from functools import partial
    from unittest import mock

    func = partial(max, 10)

# Generated at 2022-06-13 20:42:07.195083
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5
            self.y = cached_property(lambda x: x.x + 1)

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:42:07.813146
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:42:14.000171
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo:
        def __init__(self):
            self.a = 'foo'

        @cached_property
        def b(self):
            return self.a + 'bar'

    f = Foo()
    assert f.b == 'foobar'
    f.b = 'baz'
    assert f.b == 'baz'


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:42:17.158945
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Test:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Test()
    assert obj.y == 6



# Generated at 2022-06-13 20:42:27.869457
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    from .classes import PythonVersionFinder

    from .mockserver import Server

    from requests_mock import Mocker

    with Mocker() as mock:

        finder = PythonVersionFinder()

        # Test that the property is retrieved on initial access
        with Server():
            mock.get("http://docs.python.org/whatsnew/3.6.html", text='<h1>What\'s New In Python 3.6</h1>')
            assert finder.version == (3, 6)

        # Test that the property is still accessible
        mock.get("http://docs.python.org/whatsnew/3.6.html", text='<h1>What\'s New In Python 3.6</h1>')
        assert finder.version == (3, 6)

        # Test no requests

# Generated at 2022-06-13 20:42:32.755718
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    obj = cached_property(lambda self: self)
    assert obj.__get__(None, None) is obj
    assert obj.__get__(object(), None) is object()



# Generated at 2022-06-13 20:42:41.234633
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Provided you're using Python >= 3.8

    # noinspection PyPep8Naming
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    # Provided you're using Python 3.6 or 3.7

    # noinspection PyPep8Naming
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6