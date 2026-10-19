

# Generated at 2022-06-13 20:32:42.582810
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class A:
        @cached_property
        def foo(self):
            return 'foo'

    a = A()
    assert a.foo == 'foo'

    if sys.version_info[:2] == (3, 7):
        a.foo.__class__ == asyncio.futures._GatheringFuture
    else:
        a.foo.__class__ == asyncio.futures.Future

# Generated at 2022-06-13 20:32:53.804120
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock

    obj = MagicMock()

    @cached_property
    def y(self):
        return self.x * 2

    def sync(self):
        return self.x * 2

    async def async_(self):
        return self.x * 2

    sync.__name__ = 'y'
    y.func = sync

    obj.__dict__ = {'x': 20}
    assert y.__get__(obj) == 40

    def test_get_sync():
        assert y.__get__(obj) == 40
        assert len(obj.mock_calls) == 0

    def test_get_async():
        async def test_get_async_():
            assert (await y.__get__(obj)) == 40

# Generated at 2022-06-13 20:32:54.630570
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:33:03.083823
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:
        _a = 5

        @cached_property
        def a(self):
            return self._a

    obj = MyClass()

    assert obj.a == obj.a == obj.a == obj.a == obj.a == obj._a

    assert isinstance(obj.a, int)

    obj.__dict__.pop("a")

    assert obj.a == obj.a == obj.a == obj.a == obj.a == obj._a



# Generated at 2022-06-13 20:33:08.977547
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


# Generated at 2022-06-13 20:33:12.664711
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    class TestClass:

        # pylint: disable=unused-variable
        @cached_property
        def val(self):
            return 0

    test_obj = TestClass()
    assert test_obj.val == 0

# Generated at 2022-06-13 20:33:20.476333
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # class MyClass:
    #
    #     def __init__(self, x=''):
    #         self.x = x
    #
    #     @cached_property
    #     def y(self):
    #         return self.x + 'bar'
    #
    # my_obj = MyClass('foo')
    #
    # assert my_obj.y == 'foobar'
    assert True

# Generated at 2022-06-13 20:33:21.722371
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass  # For now, see test_cached_property()



# Generated at 2022-06-13 20:33:29.332995
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # noinspection PyMissingOrEmptyDocstring
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}



# Generated at 2022-06-13 20:33:32.767603
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import TestCase, mock
    from flutils.decorators import cached_property


    class Mock:

        @cached_property
        def value(self):
            return self.x + 1


    obj = Mock()
    obj.x = 5

    assert obj.value == 6  # always called
    obj.__dict__['value'] = None
    assert obj.value == 6  # cached



# Generated at 2022-06-13 20:33:40.572266
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D103
    class C:  # noqa: D101
        @cached_property
        def prop(self):
            raise NotImplementedError()

    c = C()

    with pytest.raises(NotImplementedError):
        c.prop



# Generated at 2022-06-13 20:33:43.577979
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test docstring attributes."""

    class Test:

        def __init__(self):
            self._x = None

        @cached_property
        def x(self):
            return self._x

    t = Test()
    print(dir(t.x))
    t.x


if __name__ == "__main__":
    test_cached_property___get__()

# Generated at 2022-06-13 20:33:47.245722
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class C:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = C()
    assert obj.y
    assert obj.__dict__['y'] == obj.y



# Generated at 2022-06-13 20:33:54.936690
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test the __get__ method."""

    from flutils.decorators import cached_property

    class MyClass:
        @cached_property
        def y(self):
            return 6

    obj = MyClass()
    y = obj.y
    assert y == 6
    assert obj.__dict__['y'] == 6
    assert obj.__dict__ == {'y': 6}



# Generated at 2022-06-13 20:34:02.839135
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.get import _get
    from flutils.objects import Dr
    events = []
    class MyClass:
        def __init__(self):
            self.x = 5
        @cached_property
        def y(self):
            events.append('y')
            return self.x + 1

    obj = MyClass()
    drt = Dr((obj, 'y'), ctx=events)
    drt.assertIsInstance(_get(obj, 'y'), int)
    drt.assertItemsEqual(events, ['y'])
    drt.assertIsInstance(obj.y, int)
    drt.assertItemsEqual(events, ['y'])

    drt = Dr('cached_property.__get__')

# Generated at 2022-06-13 20:34:13.489722
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest
    import unittest.mock as mock


    class TestClass(object):
        def __init__(self):
            self.mock = mock.Mock()

        @cached_property
        def test_coroutine(self):
            return self.mock.p.execute()

        @cached_property
        def test_sync(self):
            return self.mock.p.execute()

    t = TestClass()

    async def async_test():
        t.test_coroutine
        t.test_coroutine

        t.test_sync
        t.test_sync

    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_test())

    assert t.mock.p.execute.call_count == 2



# Generated at 2022-06-13 20:34:14.538248
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:34:20.029191
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property.

    """

    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    ret = obj.y
    return


# Generated at 2022-06-13 20:34:28.980749
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Make sure that a future is returned, if a coroutine function is passed
    # in self.func

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def y(self):
            return self.x + 1

    obj = MyClass()
    future = obj.y
    assert isinstance(future, asyncio.Future)

    # Make sure that if a regular function is passed in self.func, a regular
    # value is returned

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    value = obj.y
    assert value == 6

# Generated at 2022-06-13 20:34:38.555072
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self, number: int = 5):
            self.x = number

        @cached_property
        def y(self):
            return self.x + 1

    # Check the cached value is returned
    obj = MyClass(number=5)
    assert obj.y == 6

    obj = MyClass(number=7)
    assert obj.y == 8

    # Check the property is cached
    assert obj.__dict__['y'] == obj.y

    # Check retrieved after delete cache
    del obj.__dict__['y']
    obj = MyClass(number=5)
    assert obj.y == 6



# Generated at 2022-06-13 20:34:48.221940
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class C:

        def __init__(self, x: int):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    c = C(5)
    assert c.y == 6
    c.x = 10
    assert c.y == 11

    assert c.__dict__['y'].__class__.__name__ == 'int'



# Generated at 2022-06-13 20:35:00.672531
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock, call
    from flutils.decorators import cached_property

    prop = cached_property(Mock(name="func"))

    # First call, the property is not in `obj.__dict__`
    obj = object()
    obj.__dict__ = dict()
    prop.__get__(obj, object)
    assert obj.__dict__ == {prop.func.__name__: prop.func.return_value}

    prop.func.assert_called_once_with(obj)
    prop.func.reset_mock()

    # Second call, the property is in `obj.__dict__`
    prop.__get__(obj, object)
    prop.func.assert_not_called()

    # Third call, the property is deleted from `obj.__dict__`


# Generated at 2022-06-13 20:35:05.895181
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        @cached_property
        def y(self):
            return self.x + 1

        def __init__(self):
            self.x = 5

    obj = MyClass()
    assert obj.y == obj.y



# Generated at 2022-06-13 20:35:18.394978
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # pragma: no cover
    class TestClass:
        x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()

    # Test __get__ is cached
    assert obj.__dict__.get('y') is None
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    assert obj.y == 6

    # Test __delete__ resets cached property
    del obj.y
    assert obj.y == 6

    # Test __get__ is cached for coroutine
    assert obj.__dict__.get('y') is None
    assert obj.y == 6
    assert isinstance(obj.__dict__['y'], asyncio.Future)
    assert obj.__dict__['y'].done()
    assert obj.y

# Generated at 2022-06-13 20:35:26.827334
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = A()
    y = obj.y
    assert y == 6

    # Make sure the property can be deleted
    del obj.y
    assert not hasattr(obj, 'y')

    # And recreated
    y = obj.y
    assert y == 6



# Generated at 2022-06-13 20:35:37.495347
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Create an object of MyClass
    obj = MyClass()
    assert obj.y == 6

    # Delete y property
    assert 'y' in obj.__dict__
    del obj.y
    assert 'y' not in obj.__dict__

    # y property is re-calculated
    assert obj.y == 6

    # Set x
    obj.x = 10
    # y is re-calculated
    assert obj.y == 11

# Generated at 2022-06-13 20:35:42.027311
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

    return



# Generated at 2022-06-13 20:35:52.191019
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Parrot:
        def __init__(self, name):
            self.name = name

        @cached_property
        def name_length(self):
            print('Calling self.name_length()')
            return len(self.name)

        @cached_property
        async def is_cool(self):
            print('Calling self.is_cool()')
            return await asyncio.sleep(1, True)

    # Test cached_property.__get__ with a normal method
    p = Parrot('Budgie')
    assert p.name_length == 7
    assert p.name_length == 7
    assert p.__dict__ == {'name': 'Budgie', 'name_length': 7}

    # Test cached_property.__get__ with a coroutine method

# Generated at 2022-06-13 20:36:02.791742
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    import unittest
    import typing

    class TestClass(unittest.TestCase):

        def test_get(self):
            class A:
                def __init__(self):
                    self.x = "foo"

                @cached_property
                def cached_property(self):
                    return self.x

            a = A()
            self.assertEqual(a.cached_property, "foo")
            a.x = 1
            self.assertEqual(a.cached_property, "foo")

        def test_del(self):
            class A:
                def __init__(self):
                    self.x = "foo"

                @cached_property
                def cached_property(self):
                    return self.x

            a = A()

# Generated at 2022-06-13 20:36:09.622479
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import mock
    from flutils.decorators import cached_property

    class _class:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = _class()
    assert obj.y == 6



# Generated at 2022-06-13 20:36:27.000099
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    from flutils.decorators import cached_property

    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    test_obj = TestClass()
    assert test_obj.y == 6

    class TestCoroClass:
        def __init__(self):
            self.x = 5

        @cached_property
        # noinspection PyMethodMayBeStatic
        async def y(self):
            return await asyncio.sleep(1, result=self.x + 1)

    # noinspection PyTypeChecker
    test_coro_obj = TestCoroClass()
    assert not test_coro_obj.y.done()

# Generated at 2022-06-13 20:36:34.780034
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
        class MyClass:
            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj = MyClass()
        assert obj.__dict__.keys() == dict_keys(['x'])
        assert obj.y == 6
        assert obj.__dict__.keys() == dict_keys(['x', 'y'])


if __name__ == '__main__':

    import sys
    import logging
    import pytest

    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    pytest.main(['--capture=sys', '-v', __file__])

# Generated at 2022-06-13 20:36:38.660443
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def x(self):
        return 1

    class TestClass:
        x = x

    assert TestClass().__dict__ == {'x': 1}



# Generated at 2022-06-13 20:36:42.264649
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x * 2

    tc = TestClass(5)
    assert tc.y == 10

# Generated at 2022-06-13 20:36:48.210067
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test for :obj:`flutils.decorators.cached_property.__get__` method."""

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    obj.y = None
    assert obj.y is None

    obj.y = 5
    assert obj.y == 5

    del obj.y
    assert obj.y == 6


# Unit tests for class cached_property

# Generated at 2022-06-13 20:36:51.136060
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from .testdata import TestClass

    obj = TestClass()
    assert hasattr(obj, 'x') and obj.x == 5

    assert cached_property(obj.y).__get__(obj, "") == 6
    assert hasattr(obj, 'y') and obj.y == 6

# Generated at 2022-06-13 20:37:00.473464
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Tests the cached_property.__get__ method

    :return: None
    """
    import unittest.mock as mock

    class X:
        @cached_property
        def y(self):
            return self.x + 1

    obj = X()
    with mock.patch.object(X, 'y') as mock_y:
        # noinspection PyUnusedLocal
        def side_effect(x):
            return x.x + 1
        mock_y.side_effect = side_effect
        # noinspection PyStatementEffect
        obj.y

    assert obj.y == 6
    mock_y.assert_called_once()



# Generated at 2022-06-13 20:37:12.455738
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class CachedProperty(object):
        def __init__(self, obj):
            self.obj = obj
        @cached_property
        def number(self):
            return self.obj + 1
        def __repr__(self):
            return str(self.number)

    def r():
        print("r()")
        return 1
    class R(object):
        def r(self):
            print("r()")
            return 1

    cached_property_ = CachedProperty
    assert cached_property_.number == 2
    assert cached_property_.number == 2

    cached_property_ = CachedProperty(r())
    assert cached_property_.number == 2
    assert cached_property_.number == 2

    cached_property_ = CachedProperty(R())
    assert cached_property_.number == 2
    assert cached_

# Generated at 2022-06-13 20:37:19.070150
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # First call for attribute "y" of obj
    @cached_property
    def get_y():
        return 1

    obj = type('X', (), {'y': get_y})
    obj.y
    assert obj.__dict__['y'] == 1

    # Second call for attribute "y" of obj
    y = obj.y
    assert y == 1

    # Third call for attribute "y" of obj
    # ...no method is called again
    y = obj.y
    assert y == 1



# Generated at 2022-06-13 20:37:27.111236
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class foo:
        @cached_property
        def bar(self):
            yield 5
            yield 6
            yield 7
    obj = foo()
    gen = obj.bar
    assert next(gen) == 5
    assert next(gen) == 6
    assert next(gen) == 7
    _ = obj.bar
    _ = obj.bar
    try:
        _ = obj.bar
        assert False, "Shouldn't get here"
    except RuntimeError:
        pass


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-13 20:37:46.395393
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:
        def __init__(self):
            self.x = 5

        def y(self):
            return self.x + 1

    assert Test().y == 6



# Generated at 2022-06-13 20:37:50.560859
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
    assert obj.__dict__ == {'x': 5, 'y': 6}

    obj.x = 6

    assert obj.y == 7
    assert obj.y == 7
    assert obj.__dict__ == {'x': 6, 'y': 7}

# Generated at 2022-06-13 20:37:55.251420
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    import pytest

    from . import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    assert obj.y == 6

# Generated at 2022-06-13 20:38:02.698121
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property
    """

    def test(obj: object) -> int:
        """
        Simple test method

        :param obj:
        :return:
        """
        return 1

    class Test:
        """
        Simple class with one cached method property
        """

        @cached_property
        def test(self):
            return test(self)

    test_obj = Test()
    test_obj2 = Test()

    assert test_obj.test == test_obj.test
    assert test_obj2.test == test_obj2.test
    assert test_obj.test != test_obj2.test
    test_obj.test += 1
    assert test_obj.test != test_obj2.test

# Generated at 2022-06-13 20:38:12.447224
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    import unittest
    from unittest.mock import Mock, call

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.mock_self = Mock()
            self.mock_self._self_cls = 42

        def test_input_None(self):
            obj = cached_property(self.mock_self)
            ret = obj.__get__(None, None)
            self.assertIs(ret, obj)
            self.assertEqual(self.mock_self.call_count, 0)

        def test_input_valid(self):
            obj = cached_property(self.mock_self)
            mock_current = Mock()
            ret = obj.__get__(mock_current, None)

# Generated at 2022-06-13 20:38:13.059820
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D103
    pass


# Generated at 2022-06-13 20:38:22.309840
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    from random import randint

    class A:

        def __init__(self, value):
            self.value = value
            self.rand = randint(1, 10)

        @cached_property
        def x(self):
            return self.value * self.rand

    a1 = A(1)
    a2 = A(2)
    a3 = A(3)
    a4 = A(4)
    a5 = A(5)
    a6 = A(6)

    assert a1.x == a1.rand
    assert a2.x == a2.rand * 2
    assert a3.x == a3.rand * 3
    assert a4.x == a4.rand * 4
    assert a5.x == a5.rand * 5

# Generated at 2022-06-13 20:38:31.165160
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    tests = [
        {
            "name": "Test #1",
            "inputs": {"obj": "value"},
            "expected_outputs": True,
        },
    ]

    for test in tests:
        print(test["name"])
        obj = cached_property(lambda: None)
        result = obj.__get__(**test["inputs"])
        assert result == test["expected_outputs"]

# Generated at 2022-06-13 20:38:39.618640
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import mock, TestCase

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class Test_cached_property___get__(TestCase):
        """Test for class cached_property method __get__."""

        def test_get_obj_is_None(self):
            """Test method __get__ when obj is None."""
            y = MyClass.y
            self.assertIsInstance(y, cached_property)
            self.assertEqual(y.func.__name__, 'y')

        def test_get_obj_is_not_None(self):
            """Test method __get__ when obj is not None."""
            my_obj = MyClass()
            self

# Generated at 2022-06-13 20:38:46.216120
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert isinstance(obj.y, int)
    assert obj.y == 6
    assert obj.__dict__['y'] == 6

# Generated at 2022-06-13 20:39:26.358756
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    assert (
        cached_property.__get__.__doc__
        == """\
        Method docstring placeholder.

        Returns:
            None: None.
        """
    )

# Generated at 2022-06-13 20:39:39.810809
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from collections import namedtuple

    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert isinstance(obj.y, int)
    del obj.y
    assert obj.y == 6

    try:
        res = obj.fake_prop
        assert False, 'Property expected to not exist.'
    except AttributeError:
        assert True
    else:
        assert False

    FakeClass = namedtuple('FakeClass', ['x'])
    fake_obj = FakeClass(5)

# Generated at 2022-06-13 20:39:52.305890
# Unit test for method __get__ of class cached_property

# Generated at 2022-06-13 20:39:59.552621
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @cached_property
        def first_and_last_name(self):
            return self.name.split(" ")

        @cached_property
        def full_name(self):
            return self.name

    person = Person("John Smith", 29)

    assert person.first_and_last_name == ["John", "Smith"]
    assert person.full_name == "John Smith"



# Generated at 2022-06-13 20:40:04.491540
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    assert cached_property.__get__(None, None) == cached_property
    assert cached_property.__get__(None, int) == cached_property
    assert cached_property.__get__(5, None) == cached_property
    assert cached_property.__get__(5, int) == 5



# Generated at 2022-06-13 20:40:07.887181
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        @cached_property
        def y(self):
            return 5

    o = MyClass()
    assert o.y == 5
    assert o.__dict__['y'] == 5



# Generated at 2022-06-13 20:40:15.080856
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    print(f"\n\n{'#' * 60}\n")

    obj = MyClass()
    assert obj.y == 6, "Test 1: FAILURE!"

    print(obj.__dict__)

    print(f"\n{'#' * 60}\n\n")


# Generated at 2022-06-13 20:40:20.214501
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Set up test environment
    class Test(object):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Run test
    test = Test()
    assert test.y == 6

# Generated at 2022-06-13 20:40:23.927578
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """cached_property.__get__(obj, cls)"""
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:40:32.646365
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """This method tests the cached_property __get__ method:

    * test when the method is called with obj of type None, it returns itself
    * test when the method is called with obj of any other type, the obj
      dictionary is populated with the result of the evaluation of the func
      and the result of the evaluation is returned

    """

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Test when the method is called with obj of type None, it returns itself
    test_obj1 = MyClass.y
    assert isinstance(test_obj1, cached_property)

    # Test when the method is called with obj of any other type, the obj
    # dictionary is populated with the result of the evaluation of the func and

# Generated at 2022-06-13 20:41:53.334703
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    assert cached_property.__get__


# Generated at 2022-06-13 20:42:00.135997
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # As a class attribute
    class A:
        @cached_property
        def a(self):
            print("a called")
            return 1

    assert A.a is A.a

    # As an instance attribute
    assert A().a is A().a

    # As a non-data descriptor
    class C:
        @cached_property
        def d(self):
            print("d called")
            return "d"

    class D(C):
        @cached_property
        def d(self):
            print("d called")
            return "D"

    c = C()
    d = D()
    assert c.d == "d"
    assert d.d == "D"



# Generated at 2022-06-13 20:42:08.085566
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class TestClass:
        def __init__(self, name):
            self.name = name

        @cached_property
        def greeting(self):
            return f"Hello, {self.name}!"

    test_class = TestClass("World")
    assert test_class.greeting == "Hello, World!"
    assert TestClass.greeting.__doc__ == TestClass.greeting.func.__doc__


# Generated at 2022-06-13 20:42:16.448319
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
    assert "y" in obj.__dict__
    # noinspection PyUnresolvedReferences
    assert obj.y == obj.__dict__["y"]
    # noinspection PyUnresolvedReferences
    assert obj.y == MyClass.__dict__["y"].__get__(obj, object)



# Generated at 2022-06-13 20:42:23.546677
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo:
        @cached_property
        def bar(self):
            return self.baz + 1
        baz = 5

    foo = Foo()
    assert foo.bar == 6
    foo.baz = 2
    assert foo.baz == 2
    assert foo.bar == 6
    del foo.bar
    assert foo.bar == 3
    assert foo.baz == 2
    foo.bar = 7
    assert foo.bar == 7


# Generated at 2022-06-13 20:42:27.123491
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



# Generated at 2022-06-13 20:42:36.371503
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from pytest import approx
    from time import time, sleep

    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Test cached property."""
            return self.x + 1

        @cached_property
        def z(self):
            """Test cached property."""
            return time()

    obj = TestClass()
    assert obj.y == 6
    assert obj.z == approx(time())
    sleep(1)
    assert obj.z == approx(time() - 1)