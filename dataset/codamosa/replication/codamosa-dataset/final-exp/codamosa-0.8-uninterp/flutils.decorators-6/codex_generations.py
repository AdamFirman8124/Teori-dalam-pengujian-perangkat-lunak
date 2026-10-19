

# Generated at 2022-06-13 20:32:43.293916
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import logging
    import sys

    logger = logging.getLogger(__name__)
    log_handler = logging.StreamHandler(sys.stdout)
    log_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)

    class MyClass:
        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            logger.info("Calling the y() function for self={!r}".format(self))
            self.x += 1
            return self.x


# Generated at 2022-06-13 20:32:54.033380
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property

    Version: 2020-09-24

    Since version number: 0.2.0

    """
    import sys

    from flutils.decorators import cached_property

    if sys.version_info.major != 3 or sys.version_info.minor < 8:
        return

    class TestClass:

        def __init__(self):
            self.a = 5
            self.b = 2

        @cached_property
        def addition(self):
            return self.a + self.b

        @cached_property
        def subtraction(self):
            return self.a - self.b

    def test_attr(attr):
        test_obj = TestClass()

        result = attr.__get__(test_obj, TestClass)
       

# Generated at 2022-06-13 20:33:05.154740
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import mock
    import logging

    _cls = type('cls', (object,), {})
    _prop_name = 'x'
    _prop_value = 'x_value'

    def _side_effect(*args, **kwargs):
        return _prop_value

    _cls.x = mock.Mock(side_effect=_side_effect, __name__=_prop_name)
    _cls.x.__func__ = _cls.x

    _obj = mock.Mock()
    _cp = cached_property(_cls.x)
    _p = _cp.__get__(_obj, _cls)

    assert _p == _prop_value
    _cls.x.assert_called_once_with(_obj)

# Generated at 2022-06-13 20:33:07.241533
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method ``__get__`` of class :class:`cached_property`
    """

    # noinspection PyUnusedLocal
    class TestClass:

        @cached_property
        def cached_property(self):
            return 5

    tc = TestClass()
    assert tc.cached_property == 5
    assert tc.__dict__['cached_property'] == 5

# Generated at 2022-06-13 20:33:13.550346
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock

    class C:
        @cached_property
        def prop(self):
            return MagicMock()

    def test(obj):
        """Test

        :param obj:
        """
        obj.prop()
        obj.prop()
        assert obj.prop is obj.prop
        assert obj.prop.call_count == 1

    test(C())

# Generated at 2022-06-13 20:33:18.252693
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass(object):

        @cached_property
        def y(self):
            return 2

    obj = MyClass()
    assert obj.y == 2
    assert obj.y == 2



# Generated at 2022-06-13 20:33:23.075940
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 7

        @cached_property
        def y(self):
            return self.x + 2

    obj = MyClass()
    assert obj.y == 9
    obj.x = 6
    assert obj.y == 9
    del obj.y
    assert obj.y == 8


# Generated at 2022-06-13 20:33:27.534833
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class _Test:

        @cached_property
        def prop(self):
            return 'value'

    test = _Test()
    assert test.prop == 'value'



# Generated at 2022-06-13 20:33:32.880022
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        @cached_property
        def y(self):
            return 5

    m = MyClass()

    @asyncio.coroutine
    def test():
        return m.y

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(test())
    assert result == 5

# Generated at 2022-06-13 20:33:36.824861
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass(object):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.y

    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}


# Generated at 2022-06-13 20:33:40.571199
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests for method __get__ of class cached_property
    """
    return



# Generated at 2022-06-13 20:33:44.434426
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # type: () -> None
    from flutils.decorators import cached_property

    class MyClass(object):

        def __init__(self):
            # type: () -> None
            self.x = 5

        @cached_property
        def y(self):
            # type: () -> int
            return self.x + 1

    obj = MyClass()
    v = obj.y
    if v != 6:
        raise AssertionError("cached_property.__get__(obj) failed.")

# Generated at 2022-06-13 20:33:57.969420
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import mock
    from unittest.mock import MagicMock, sentinel

    the_func = MagicMock()
    cp = cached_property(the_func)
    obj = MagicMock(spec_set=object)

    # obj is None
    assert cp.__get__(None, None) is cp

    # obj is not none
    assert cp.__get__(obj, None) is the_func.return_value

    the_func.return_value = sentinel.return_value
    obj.__dict__ = {'key': sentinel.key}

    def _assert_call_args(func, kwargs):
        expected_call_args = (obj, None)
        assert func.call_args == mock.call(*expected_call_args, **kwargs)


# Generated at 2022-06-13 20:34:04.304460
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property

    Returns:

    """

    def test_coroutine(obj):
        return obj

    def test_function(obj):
        return obj

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):  # pylint: disable=E0213
            return self.x + 1

        @cached_property
        def z(self):  # pylint: disable=E0213
            return test_function(self)

        @cached_property
        def a(self):  # pylint: disable=E0213
            return test_coroutine(self)

    my_class = MyClass()
    assert my_class.y == 6
    assert my_class.z

# Generated at 2022-06-13 20:34:12.502506
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test that method __get__ of class cached_property works as expected.

    See also: :class:`flutils.decorators.cached_property`

    """
    from flutils.decorators import cached_property

    class Foo:

        def __init__(self):
            self._x = "foo"

        @cached_property
        def x(self):
            return self._x

    foo = Foo()

    # Test
    foo.x
    assert foo._x == "foo"

    # Test
    foo.x = "bar"
    assert foo._x == "foo"

# Generated at 2022-06-13 20:34:13.533682
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:34:23.936460
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test module flutils.decorators.cached_property."""
    import pytest
    from flutils.decorators import cached_property
    from flutils.decorators import pytest_plugin_helpers

    def test_invoke_cached_property():

        class MyClass:

            def __init__(self):
                self.a = 5

            @cached_property
            def property(self):
                return self.a + 1

        obj = MyClass()

        assert obj.property == 6
        obj.a = 1
        assert obj.property == 6

        obj.a = 1
        assert obj.property == 2

    test_invoke_cached_property.pytest_name = "invoke_cached_property"


# Generated at 2022-06-13 20:34:29.396499
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



# Generated at 2022-06-13 20:34:34.470418
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock, MagicMock
    class MyClass:
        x = 5
        @cached_property
        def y(self):
            """Return self.x"""
            return self.x
    obj = MyClass()
    assert obj.y == 5


# Generated at 2022-06-13 20:34:40.707832
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    ret = obj.y

    assert ret == 6
    assert type(ret) is int
    assert obj.y == 6

# Generated at 2022-06-13 20:34:50.854771
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    loop = asyncio.get_event_loop()

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    class MyAsyncClass:
        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            return self.x + 2

    obj = MyAsyncClass()
    loop.run_until_complete(obj.y)
    assert obj.y.result() == 7

# Generated at 2022-06-13 20:35:03.488530
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property

    Test Case 0:
        Test:  Case where obj is None
        Expect: The cached_property
    Test Case 1:
        Test:  Case where obj is not None but self.func is a coroutine function
        Expect: A coroutine function is returned that returns the future of
            self.func
    Test Case 2:
        Test:  Case where obj is not None and self.func is not a coroutine
            function
        Expect: self.func is evaluated and the result is returned

    """
    class DummyClass:
        def __init__(self):
            pass
    dummy_class = DummyClass()

    class DummyClass1:
        def __init__(self):
            pass

        @cached_property
        def x(self):
            return 5

   

# Generated at 2022-06-13 20:35:08.549457
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



# Generated at 2022-06-13 20:35:13.806524
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from asyncio import get_event_loop
    class MyClass():
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    loop = get_event_loop()
    assert loop.run_until_complete(obj.y) == 6
    assert obj.y == 6

# Generated at 2022-06-13 20:35:24.929880
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def foo(self):
        return self.x + 5

    class Object():
        x = 0

    obj = Object()
    assert foo.__get__(obj, type(obj)) == 5
    assert foo.__get__(obj, type(obj)) == 5
    obj.x = 10
    assert foo.__get__(obj, type(obj)) == 15
    assert foo.__get__(obj, type(obj)) == 15
    del obj.foo
    assert foo.__get__(obj, type(obj)) == 15


# Generated at 2022-06-13 20:35:36.860726
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio

    class TestCachedProperty:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestCachedProperty()
    assert obj.y == 6

    class TestCachedAsyncProperty:
        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            await asyncio.sleep(2)
            return self.x + 1

    loop = asyncio.get_event_loop()
    obj = TestCachedAsyncProperty()
    future = loop.run_until_complete(obj.y)
    assert future.result() == 6

# Generated at 2022-06-13 20:35:44.135311
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    from flutils.decorators import cached_property

    class TestClass:
        """Test class for cached_property"""

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Test property"""
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6
    assert obj.y == 6


if __name__ == '__main__':
    import pytest

    pytest.main([__file__, '-v'])

# Generated at 2022-06-13 20:35:53.263790
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import flutils
    flutils.load_config(create=True)
    flutils.log.info('Change log level to DEBUG')
    flutils.log.setLevel(0)
    flutils.log.info('Initial log level: {}'.format(flutils.log.level))
    flutils.log.info('Initial log_level: {}'.format(flutils.log_level))
    flutils.log_level = 'DEBUG'
    flutils.log.info('Change log_level to DEBUG')
    flutils.log.info('Current log level: {}'.format(flutils.log.level))
    flutils.log.info('Current log_level: {}'.format(flutils.log_level))

    from flutils.decorators import cached_property


# Generated at 2022-06-13 20:35:57.034724
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self, val):
            self.x = val

        @cached_property
        def y(self):
            return self.x + 1

    assert MyClass(5).y == 6



# Generated at 2022-06-13 20:36:02.520890
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """:class:`cached_property` - Method test_cached_property___get__"""

    def func(obj):
        return obj.x + 1

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return func(self)

    obj = MyClass()
    # print(obj.y)
    assert obj.y == 6



# Generated at 2022-06-13 20:36:12.833970
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    class Person:

        def __init__(self):
            self.y = 0

        @cached_property
        def x(self):
            return self.y + 1

    obj = Person()
    assert 6 == obj.x
    obj.y = 5
    assert 6 == obj.x



# Generated at 2022-06-13 20:36:17.648348
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
    for _ in range(3):
        assert 'y' not in obj.__dict__
        assert obj.y == 6



# Generated at 2022-06-13 20:36:21.986787
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



# Generated at 2022-06-13 20:36:31.263770
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
            yield from asyncio.sleep(5)  # noqa: S311
            return self.x + 1

    obj = MyClass()

    assert obj.y == 6
    assert obj.y == 6

    assert asyncio.iscoroutine(obj.z)

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(obj.z)
    assert result == 6
    assert obj.z == 6

# Generated at 2022-06-13 20:36:36.432437
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    obj = MyClass()
    assert obj.y == "ycached_property"
    obj1 = MyClass1()
    assert obj1.y == "ycached_property"
    assert obj1.y1 == "y1cached_property"



# Generated at 2022-06-13 20:36:46.822482
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property as cprop

    class X:
        num = 1

        @cprop
        def cprop1(self):
            return self.num + 1

        @cprop
        def cprop2(self):
            return self.num + 2

        @cprop
        def cprop3(self):
            return self.num + 3

    x = X()
    assert x.cprop1 == 2
    assert x.cprop2 == 3
    assert x.cprop3 == 4

    x.num = 2
    assert x.cprop1 == 3
    assert x.cprop2 == 4
    assert x.cprop3 == 5


# Generated at 2022-06-13 20:36:52.714343
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class testClass:

        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            if self.x == 5:
                self.x = 0
                return True
            self.x += 1
            return False

    t = testClass()
    assert t.y is False
    assert t.y is False
    assert t.y is False
    assert t.y is True
    assert t.y is False
    assert t.y is False
    assert t.y is False
    assert t.y is True
    assert t.y is False



# Generated at 2022-06-13 20:36:56.857950
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



# Generated at 2022-06-13 20:37:02.915422
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo:

        @cached_property
        def bar(self):
            return 5

    foo = Foo()
    assert foo.bar == 5
    assert foo.__dict__['bar'] == 5

    foo.__dict__['bar'] = 99
    assert foo.bar == 99
    assert foo.__dict__['bar'] == 99
    assert foo.bar == 99



# Generated at 2022-06-13 20:37:11.284545
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method ``__get__`` of class :obj:`cached_property`.
    """
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    assert obj.__dict__['y'] == obj.__dict__['y']
    assert obj.y == obj.y



# Generated at 2022-06-13 20:37:22.225755
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property.
    """
    class MyClass:

        def __init__(self):
            self.__x = 5

        @cached_property
        def y(self):
            return self.__x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:37:27.073995
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


# Generated at 2022-06-13 20:37:33.087394
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # noinspection PyPep8Naming
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x
    obj = MyClass()
    assert obj.__dict__ == {'x': 5}
    assert obj.y == 5
    assert obj.__dict__ == {'x': 5, 'y': 5}

# Generated at 2022-06-13 20:37:38.756491
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



# Generated at 2022-06-13 20:37:43.089156
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

# Generated at 2022-06-13 20:37:45.360602
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property
    """



# Generated at 2022-06-13 20:37:54.122573
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Unit test for method __get__ of class cached_property."""

    class A:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        def reset(self):
            """ Reset the cache. """
            return delattr(self, 'y')

    obj = A()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    obj.reset()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6

# Generated at 2022-06-13 20:37:57.404780
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert(obj.y == 6)

# Generated at 2022-06-13 20:38:04.070006
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class C(object):
        def __init__(self, value):
            self.value = value

        @cached_property
        def cached_property(self):
            return self.value ** 2

    c = C(5)
    assert c.cached_property == 25
    c.value = 6
    assert c.cached_property == 25

    class B(object):
        def __init__(self, value):
            self.value = value

        @cached_property
        def cached_property(self):
            self.value += 1
            return self.value ** 2

    b = B(5)
    assert b.cached_property == 36
    b.value = 6
    assert b.cached_property == 36
    assert b.value == 7


# Generated at 2022-06-13 20:38:09.913082
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 1

        @cached_property
        def y(self):
            return self.x + 2

    obj = MyClass()
    assert obj.y == 3
    obj.x = 4
    obj.y
    assert obj.y == 3


# Generated at 2022-06-13 20:38:29.570080
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

# Generated at 2022-06-13 20:38:35.379554
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5
            self.y = None

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:38:40.800751
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    from unittest import TestCase
    from unittest.mock import Mock

    class TestCachedProperty(TestCase):

        def test__get__(self):

            class MyClass:

                def __init__(self, x):
                    self.x = x

                @cached_property
                def y(self):
                    return self.x + 1

            my_obj = MyClass(5)

            self.assertEqual(my_obj.y, 6)
            self.assertEqual(my_obj.__dict__, {'x': 5, 'y': 6})

        def test__get___with_coroutine(self):

            class MyClass:

                def __init__(self, x):
                    self.x = x

                @cached_property
                async def y(self):
                    return self.x

# Generated at 2022-06-13 20:38:43.713296
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""
    from pytest import raises

    from flutils.decorators import cached_property

    class Dummy:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    d = Dummy()
    d.x = 7
    assert d.y == 8
    d.x = 9
    assert d.y == 8



# Generated at 2022-06-13 20:38:47.963228
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property"""

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:38:55.064167
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:
        x = 5

        @cached_property
        def y(self):
            return self.x + 1

        # noinspection PyMethodMayBeStatic
        @asyncio.coroutine
        def z(self):
            yield from asyncio.sleep(0.5)
            return self.x + 1

    assert Test.y.__doc__ == Test.y.func.__doc__
    assert Test.z.__doc__ == Test.z.func.__doc__
    assert Test.y.__doc__ == Test.__init__.__doc__

    instance = Test()
    assert isinstance(instance.y, int)
    assert instance.y == 6
    assert instance.__dict__['y'] == 6

    loop = asyncio.get_event_loop()

# Generated at 2022-06-13 20:39:06.355280
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test to verify that method __get__ of class cached_property will set a
    property value or execute a coroutine to set the property value.

    """
    import sys
    import unittest

    from unittest.mock import patch

    mock_return_value = 'My Return Value'

    # Cached property
    class CachedProp(object):
        def __init__(self):
            self._value = None

        @cached_property
        def value(self):
            return mock_return_value

    # Coroutine property
    class CoroProp(object):
        def __init__(self):
            self._value = None

        @cached_property
        async def value(self):
            return mock_return_value


# Generated at 2022-06-13 20:39:18.666096
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.testutils import (
        AnnotatedMock as Mock,
        AsyncMock,
        MagicMock,
        patch,
    )
    from flutils.decorators import cached_property

    class Klass:

        @cached_property
        def prop(self):
            return 'value'

    mock_get = patch('flutils.decorators.cached_property.get').start()
    mock_get.return_value = 'new value'

    mock_obj = Mock(spec='flutils.decorators.Klass')
    mock_obj.__dict__ = {}

    # Case 1: method __get__ is called to retrieve a property value;
    # previously computed and cached.
    #
    # Expected behavior: 'new value' returned
    #
    mock_obj.__dict

# Generated at 2022-06-13 20:39:22.305385
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        @cached_property
        def x(self):
            return 5

    obj = MyClass()
    obj.x
    assert obj.__dict__ == {'x': 5}

# Generated at 2022-06-13 20:39:29.103981
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    This function runs the tests for method __get__ of class cached_property.
    :return: None
    """

    from random import random

    # from functools import lru_cache
    from time import time
    from time import sleep

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            sleep(1)
            return self.x + 1

    # noinspection PyUnusedLocal,PyUnusedLocal
    @cached_property
    def random_num():
        return random()

    obj = MyClass()

    # Test that a cached property is returned.
    assert obj.y == 6

    # Test that the same cached

# Generated at 2022-06-13 20:40:11.908639
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from flutils.decorators import cached_property

    class _Test:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    x = _Test()
    y = x.y
    assert y == 6

    y = _Test().y
    assert y == 6



# Generated at 2022-06-13 20:40:21.929565
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.

    :return: (boolean) True if unit test successful, else False.

    .. versionadded:: 0.2.0
    .. versionchanged:: 0.4.0
    """

    import pytest
    from flutils.decorators import cached_property

    # noinspection PyPep8Naming,PyUnusedLocal
    class Example:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Example()
    assert obj.y == 6
    pytest.raises(AttributeError, lambda: cached_property.__get__(None, cls=None))

# Generated at 2022-06-13 20:40:31.939215
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit tests for method __get__ of class cached_property.

    """

    import os
    import tempfile
    from types import FunctionType
    from unittest.mock import patch

    from flutils.decorators import cached_property

    with patch.object(os, "getpid", return_value=123), patch.object(
        tempfile, "gettempdir", return_value="/"
    ):
        tempdir = "/tmp/123"

    file_1 = os.path.join(tempdir, "file_1.txt")
    file_2 = os.path.join(tempdir, "file_2.txt")

    @cached_property
    def test_1(self):
        with open(file_1, "w") as f:
            f.write("test_1")

# Generated at 2022-06-13 20:40:39.273107
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s :: %(asctime)s :: %(funcName)s :: %(message)s",
    )

    class TestClass0:
        def __init__(self):
            self.x = 7

        @cached_property
        def y(self):
            return self.x + 1

    test_instance0 = TestClass0()
    test_instance0.y
    test_instance0.y  # noqa: B004

    assert test_instance0.y == 8

    class TestClass1:
        def __init__(self):
            self.x = 10

        @cached_property
        def y(self):
            return self.x + 1

    test_instance1 = TestClass1()
    test

# Generated at 2022-06-13 20:40:43.568526
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock
    from flutils.decorators import cached_property

    class MyClass(Mock):
        # noinspection PyPep8Naming
        @cached_property
        def y(self):
            return self.x

    obj = MyClass()
    assert obj.y == obj
    assert obj.y == obj.x

# Generated at 2022-06-13 20:40:54.162331
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    obj = mock.Mock()
    func = mock.Mock()
    func.__name__ = "x"
    func.__doc__ = "y"
    wrapper = cached_property(func)
    assert wrapper.__doc__ == "y"
    assert wrapper.func.__name__ == "x"
    assert wrapper.__get__(obj, None) == func.return_value
    func.assert_called_once_with(obj)
    assert obj.__dict__[func.__name__] == func.return_value
    assert wrapper.__get__(obj, None) == obj.__dict__[func.__name__]



# Generated at 2022-06-13 20:41:02.228619
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa:N802
    class C:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            """Function y."""
            return self.x
    instance = C(3)
    assert instance.y == 3
    instance.__dict__['y'] = 'the value'
    assert instance.y == 'the value'
    del instance.__dict__['y']
    assert instance.y == 3


# Generated at 2022-06-13 20:41:09.868356
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def my_property(obj):
        return "value"

    class MyClass:
        def __init__(self):
            self.x = 5

    obj = MyClass()
    assert my_property.__get__(obj) == "value"
    assert my_property.__get__(obj) == "value"


cached_property = cached_property  # type: Any

if not hasattr(functools, "cached_property"):
    functools.cached_property = cached_property  # type: ignore

del Any, cached_property  # avoid namespace collision

# Generated at 2022-06-13 20:41:16.192725
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from time import time

    class C:
        def __init__(self):
            self.x = 5

        @cached_property
        def _y(self):
            return self.x + 1

    c = C()
    c._y
    t = time()
    c._y
    assert (time() - t) < 0.01
    c._y = 10
    t = time()
    c._y
    assert (time() - t) < 0.01



# Generated at 2022-06-13 20:41:25.647199
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    class MyClass:

        def __init__(self, value: int=5):
            self._myvalue = value

        @cached_property
        def myvalue(self) -> int:
            return self._myvalue

        @cached_property
        def myvalue_plusone(self) -> int:
            return self.myvalue + 1

    obj = MyClass()
    assert obj.myvalue == 5
    assert obj.myvalue_plusone == 6

    obj = MyClass(7)
    assert obj.myvalue == 7
    assert obj.myvalue_plusone == 8

    with pytest.raises(AttributeError):
        assert obj.huh

