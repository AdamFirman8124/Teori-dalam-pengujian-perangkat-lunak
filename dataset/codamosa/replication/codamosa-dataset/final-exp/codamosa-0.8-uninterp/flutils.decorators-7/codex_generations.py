

# Generated at 2022-06-13 20:32:39.580061
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # TODO: Find a way to test this method and use the test_decorators test
    # suite to unit test it.
    assert True

# Generated at 2022-06-13 20:32:50.182616
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from datetime import datetime
    from unittest import mock

    class Test(object):

        @cached_property
        def x(self):
            return 'x'

        @cached_property
        def y(self):
            return 'y'

    def side_effect(object, name):
        if name == 'x':
            return datetime.now()
        if name == 'y':
            return object.x
        return object

    obj = Test()
    with mock.patch.object(obj.y, '__get__', side_effect=side_effect):
        assert obj.y == obj.x

# Generated at 2022-06-13 20:32:56.316166
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Create the class to be decorated with the descriptor
    class MyClass:

        def __init__(self):
            self.x = 1

        @cached_property
        def y(self):
            return self.x + 1

    # Create the decorated class instance
    obj = MyClass()

    # Test that the descriptor is set on the class instance
    assert obj.y == 2 and obj.__dict__['y'] == 2

    # Test that the descriptor is not set on the class
    assert not hasattr(MyClass, 'y')

    # Test that the descriptor can be deleted from the class instance
    del obj.y
    assert not hasattr(obj, 'y') and 'y' not in obj.__dict__



# Generated at 2022-06-13 20:33:02.414093
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # noinspection PyTypeChecker
    def cached_method(self):
        return id(self)

    class TestClass:
        # noinspection PyUnresolvedReferences
        @cached_property
        def cached_method(self):
            return cached_method(self)

    obj = TestClass()

    print(obj.cached_method)
    print(obj.cached_method)


# Generated at 2022-06-13 20:33:09.856970
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    value = obj.y
    assert value == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}
    assert obj.y == value
    assert obj.__dict__ == {'x': 5, 'y': 6}



# Generated at 2022-06-13 20:33:22.211385
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method `cached_property.__get__`

    Test plan:
    - Test __get__ method of class cached_property

    """

    # Tests for class cached_property

    def _func(obj):
        obj.counter += 1
        return obj.counter

    # Create class MyClass with method func
    class MyClass:
        counter = 0

    MyClass.func = cached_property(_func)
    obj = MyClass()

    # Test __get__ method of class cached_property
    #  - Get func, should return 1
    assert obj.func == 1

    #  - Get func again, should return 1
    assert obj.func == 1

    #  - Delete func attribute,
    #  - Get func, should return 2
    del obj.func
    assert obj.func == 2

# Generated at 2022-06-13 20:33:27.838333
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



# Generated at 2022-06-13 20:33:30.927447
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1
    obj = MyClass(5)
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}



# Generated at 2022-06-13 20:33:36.252606
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

# Generated at 2022-06-13 20:33:42.107798
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    class MyClass:

        @cached_property
        def x(self):
            return 'x'

        @cached_property
        def y(self):
            return 'y'

    obj = MyClass()
    assert obj.x == 'x'
    assert obj.y == 'y'



# Generated at 2022-06-13 20:33:47.117130
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:

        def __init__(self):
            self.__x = 5

        @cached_property
        def y(self):
            return self.__x + 1

    obj = TestClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:33:59.502111
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class :class:`cached_property`"""
    # Test expected behavior
    class Test:
        @cached_property
        def x(self):
            return 1

        @cached_property
        def y(self):
            return 2

    obj = Test()
    assert obj.x == 1
    assert obj.y == 2
    obj2 = Test()
    assert obj2.x == 1
    assert obj2.y == 2
    # Test for deletion
    del obj.x
    assert obj.x == 1
    assert obj.y == 2
    del obj2.y
    assert obj2.x == 1
    assert obj2.y == 2
    # Test for caching
    assert obj.x == 1
    assert obj.y == 2
    assert obj2.x == 1

# Generated at 2022-06-13 20:34:06.512311
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:

        def __init__(self):
            self.x = 5

        # @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()

    # from flutils.decorators import cached_property
    # cp = cached_property(obj.y)
    # print(cp)
    # print(obj.y)


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:34:11.968973
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            self.x += 1
            return self.x

    obj = MyClass()
    assert obj.y == 6
    assert obj.x == 6

    obj.x = 8

    assert obj.y == 9
    assert obj.x == 9

# Generated at 2022-06-13 20:34:20.999206
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    inst = MyClass()
    assert inst.y == 6

    # Check for recursion
    assert inst.y == 6

    # We can reset the 'y' property:
    del inst.y

    # and call 'y' again:
    assert inst.y == 6

    # and 'y' is cached:
    assert inst.y == 6

# Generated at 2022-06-13 20:34:26.515837
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

    obj.y

    assert obj.y == 6
    obj.x = 6
    assert obj.y == 6

    del obj.y

    assert obj.y == 7

# Generated at 2022-06-13 20:34:29.448400
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test :meth:`~flutils.decorators.cached_property.__get__`.
    """



# Generated at 2022-06-13 20:34:39.296960
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method :meth:`~flutils.decorators.cached_property.__get__`
    of class :class:`~flutils.decorators.cached_property.cached_property`.
    """
    import unittest
    import unittest.mock as mock

    class Test(unittest.TestCase):

        def setUp(self):
            self.cp = cached_property(mock.MagicMock())

        def test_get_with_none_instance(self):
            # Given
            instance = None

            # When
            result = self.cp.__get__(instance)

            # Then
            self.assertEqual(result, self.cp)

        def test_get_with_instance(self):
            # Given
            instance = mock.MagicMock

# Generated at 2022-06-13 20:34:51.630916
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class DummyClass:
        def __init__(self):
            self.data = 1

        @cached_property
        def prop(self):
            """Docstring."""
            return self.data

    obj = DummyClass()

    class TestCachedProperty(unittest.TestCase):
        def test_correct_descriptor(self):
            """The descriptor returns the function."""
            result = cached_property.__get__(None, DummyClass)
            self.assertIs(result, cached_property.__init__)

        def test_correct_property(self):
            """The property returns the correct property."""
            result = DummyClass.prop
            self.assertIs(result, obj.data)


# Generated at 2022-06-13 20:35:03.740469
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.testutils import ResultCollector, run_tests

    async def async_func(obj):
        return obj

    def func(obj):
        return 2 * obj

    class Test:
        pass

    test_list = [
        # Test1: test cached_property()
        Test(
            args=(
                Test(),
                cached_property(func),
                func,
                ),
            expected=2,
            expected_err=None,
            ),

        # Test2: test cached_property() on a coroutine
        Test(
            args=(
                Test(),
                cached_property(async_func),
                async_func,
                ),
            expected=None,
            expected_err=None,
            ),
        ]
    rc = ResultCollector()
    run_tests(test_list, rc)

# Generated at 2022-06-13 20:35:11.833748
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6
    assert obj.y == 6



# Generated at 2022-06-13 20:35:16.699886
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def test_attr(cls):
        pass
    # Instance method
    cls = type('TestClass', (object, ), {})
    assert test_attr.__get__(cls) is test_attr
    # Class method
    cls = type('TestClass', (object, ), {})
    assert test_attr.__get__(None, cls) is test_attr

# Generated at 2022-06-13 20:35:28.314672
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # This is a stub to test the __get__ method.

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}
    obj.x = 10
    assert obj.y == 6
    assert obj.__dict__ == {'x': 10, 'y': 6}
    del obj.y
    assert obj.__dict__ == {'x': 10}
    assert obj.y == 11



# Generated at 2022-06-13 20:35:37.008507
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """

    :return:
    """
    class Test(object):
        """
        """

        def __init__(self) -> None:
            self.calls = 0

        @cached_property
        def num(self):
            self.calls += 1
            return 42

    obj = Test()

    assert obj.__dict__ == {}, "__dict__ should be empty"
    assert obj.calls == 0, "calls should be 0"
    assert obj.num == 42, "num should be 42"
    assert obj.__dict__ == {"num": 42}, "__dict__ should be {'num': 42}"
    assert obj.calls == 1, "calls should be 1"

    del obj.num
    assert obj.__dict__ == {}, "__dict__ should be empty"

# Generated at 2022-06-13 20:35:45.748114
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test method __get__ of class cached_property
    """

    class Test1:
        @cached_property
        def y(self):
            return self.x + 1

        def __init__(self, x):
            self.x = x

    class Test2:
        @cached_property
        async def y(self):
            self.x = await self.get_x() + 1

        async def get_x(self):
            self.x = await self.get_x()
            return self.x

    # Test 1
    obj1 = Test1(5)
    assert obj1.y == 6
    delattr(obj1, 'y')
    assert not hasattr(obj1, 'y')
    assert obj1.y == 6

    # Test 2
    loop = asyncio.get_

# Generated at 2022-06-13 20:35:50.436859
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




# Generated at 2022-06-13 20:35:51.217709
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass



# Generated at 2022-06-13 20:35:57.633346
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.objects import MagicTestCase
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:36:01.013425
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Foo()
    assert obj.y == 6



# Generated at 2022-06-13 20:36:06.483213
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio

    from unittest import TestCase

    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """The cached property."""
            return self.x + 1

    class Test(TestCase):

        def test_cached_property___get__01(self):
            obj = MyClass()
            self.assertIsNone(obj.__dict__.get('y'))
            self.assertEqual(obj.y, 6)
            self.assertEqual(obj.__dict__['y'], 6)
            self.assertEqual(obj.__dict__['y'], obj.y)


# Generated at 2022-06-13 20:36:18.778527
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass():
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    print('type(MyClass):', type(MyClass))
    obj = MyClass()
    print('type(obj):', type(obj))
    print('obj.y:', obj.y)
    delattr(obj, 'y')
    print('obj.y:', obj.y)


# Generated at 2022-06-13 20:36:24.875524
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test for method __get__ of class cached_property
    """

    # noinspection PyUnusedLocal
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert(obj.y == 6)



# Generated at 2022-06-13 20:36:34.370410
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test the cached property decorator."""

    def funct(obj):
        print("I am funct")
        return obj

    class A:
        @cached_property
        def funct(self):
            print("I am a funct")
            return self

        @cached_property
        def other(self):
            print("I am other")
            return self

    a1 = A()
    assert funct is not A.funct
    assert a1.funct is A.funct
    assert a1.funct is a1.funct
    assert a1.other is not a1.funct
    assert a1.funct is a1.funct
    del a1.funct
    assert a1.funct is a1.funct
    assert a1.other is not a1.fun

# Generated at 2022-06-13 20:36:40.857274
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:

        x = 1

        @cached_property
        def y(self):
            MyClass.x += 1
            return MyClass.x

    obj = MyClass()

    assert obj.y == 2
    assert obj.y == 2
    obj.y += 1
    assert obj.y == 3

test_cached_property___get__()


# Generated at 2022-06-13 20:36:47.842671
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def foo(self):
            """A property that is only computed once per instance and then
            replaced with a ordinary attribute."""
            return self.x + 1

    assert Foo.foo.__doc__ == "A property that is only computed once per " \
        "instance and then replaced with a ordinary attribute."
    obj = Foo()
    assert obj.foo == 6
    assert Foo.foo.__doc__ == "A property that is only computed once per " \
        "instance and then replaced with a ordinary attribute."
    obj.x = 10
    assert obj.foo == 11

# Generated at 2022-06-13 20:36:54.763458
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method :meth:`flutils.decorators.cached_property.__get__`
    of class :class:`flutils.decorators.cached_property` using the following
    code:

    .. code-block:: python

        from flutils.decorators import cached_property

        class MyClass:

            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj = MyClass()
        obj.y

    """
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()


# Generated at 2022-06-13 20:37:01.570953
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    mc = MyClass()
    assert mc.y == 6
    assert mc.y == 6
    mc1 = MyClass()
    assert mc1.y == 6
    mc.x += 1
    assert mc.y == 7
    assert mc1.y == 6

# Generated at 2022-06-13 20:37:04.516668
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from random import random
    from functools import partial

    class A:

        def __init__(self):
            self.x = 123
            self.y = partial(self._y, random())

        @cached_property
        def y(self):
            return self._y(random())

        def _y(self, i):
            return i

    a = A()
    assert a.y == a.y

# Generated at 2022-06-13 20:37:09.035242
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



# Generated at 2022-06-13 20:37:19.360751
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from unittest.mock import MagicMock

    mock_cls = MagicMock()
    mock_cls.__name__ = 'Mock'

    mock_obj = MagicMock()
    mock_obj.__class__ = mock_cls
    mock_obj.__dict__ = dict()

    lru = dict()
    mock_obj.__dict__ = lru

    mocked = MagicMock()
    mocked.return_value = 42
    mocked.__name__ = 'Mocked'
    mocked.__doc__ = 'Mocked doc'

    c = cached_property(mocked)
    assert c.__doc__ == mocked.__doc__
    assert c.func == mocked

    result = c.__get__(mock_obj, mock_cls)
    mocked.assert_

# Generated at 2022-06-13 20:37:46.850705
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import logging
    import pytest

    from flutils.decorators import cached_property

    logging.getLogger(__name__).addHandler(logging.NullHandler())

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.y
    assert obj.__dict__ == {'x': 5, 'y': 6}

    class CoroMyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        @asyncio.coroutine
        def y(self):
            yield from asyncio.sleep(1)
            return self.x + 1

    obj = CoroMyClass()
    obj.y


# Generated at 2022-06-13 20:37:52.590072
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self, x: int):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(5)
    value = obj.y
    assert value == 6



# Generated at 2022-06-13 20:37:57.362663
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class Test:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + self.x

    obj = Test(x=5)
    assert obj.y == 10


# Generated at 2022-06-13 20:38:04.057387
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests a :obj:`~flutils.decorators.cached_property` is cached."""

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x + 2

    obj = MyClass()
    # noinspection PyStatementEffect
    obj.x
    # noinspection PyStatementEffect
    obj.y
    # noinspection PyStatementEffect
    obj.z
    assert not hasattr(obj, 'x')
    assert not hasattr(obj, 'y')
    assert not hasattr(obj, 'z')
    assert isinstance(obj.__dict__['y'], int)
    assert isinstance

# Generated at 2022-06-13 20:38:12.418150
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass(object):
        _x = 9
        _y = None

        @cached_property
        def y(self):
            return self._x + 1

        def __init__(self, x=1):
            self._x = x

    obj = MyClass(3)
    assert obj._x == 3
    assert obj._y is None
    assert obj.y == 4
    assert obj._y == 4
    # noinspection PyProtectedMember
    assert obj.__dict__['y']
    obj._x = 5
    assert obj.y == 6
    assert obj._y == 6


if __name__ == "__main__":
    test_cached_property___get__()

# Generated at 2022-06-13 20:38:14.109811
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached_property.__get__"""
    pass



# Generated at 2022-06-13 20:38:20.795791
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of cached_property

    This test is a derivative work of:

    `Copyright © 2011 Marcel Hellkamp <https://bit.ly/2ECEO0M>`__

    """

    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.y == 6
    assert obj.__dict__.get("y") == 6



# Generated at 2022-06-13 20:38:28.140123
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method ``__get__`` of class :obj:`cached_property`.
    """

    class MyClass:
        """MyClass"""

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """y"""
            return self.x + 1

    obj = MyClass()
    obj.y
    assert obj.__dict__ == {'x': 5, 'y': 6}



# Generated at 2022-06-13 20:38:38.752252
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock
    from unittest.mock import patch

    with patch('flutils.decorators.cached_property.asyncio.iscoroutinefunction',
               Mock(return_value=False)):
        # Test that cls is returned
        mock_self = Mock()
        mock_cls = Mock()
        assert cached_property.__get__(mock_self, mock_cls) is mock_self

        # Test that the decorator '.func' method is called with the object
        # and that the the object dict is updated.
        mock_self = Mock(spec=asyncio.iscoroutinefunction)
        mock_self.func.return_value = 42
        obj = {}
        assert cached_property.__get__(mock_self, Mock) == 42
        mock_

# Generated at 2022-06-13 20:38:50.682975
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test for method __get__ of class cached_property
    """
    @cached_property
    def myproperty(self):
        return True

    class MyClass(object):
        def __init__(self):
            self.x = 5

        myproperty = myproperty

    # Test with a non-asyncio coroutine
    obj = MyClass()
    myproperty = obj.myproperty
    print(myproperty)
    assert "myproperty" in obj.__dict__

    # Test with an asyncio coroutine
    @cached_property
    def myproperty(self):
        return asyncio.sleep(0.1)

    class MyClass(object):
        def __init__(self):
            self.x = 5

        myproperty = myproperty

    obj = MyClass()

# Generated at 2022-06-13 20:39:27.021341
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock, patch

    def some_func():
        pass

    def some_coro():
        yield 1
        return 2

    obj = MagicMock()
    obj.__class__ = MagicMock()
    obj.__class__.__name__ = "obj.__class__"
    obj.__dict__ = {"some_func": 1}
    obj.some_func.__name__ = "some_func"

    coro_obj = MagicMock()
    coro_obj.__class__ = MagicMock()
    coro_obj.__class__.__name__ = "coro_obj.__class__"
    coro_obj.__dict__ = {"some_coro": 1}

# Generated at 2022-06-13 20:39:40.154052
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test of method __get__ of class cached_property

    Args:
        N/A

    Raises:
        AssertionError: if any unit test fails

    Returns:
        None
    """
    import unittest

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class TestCachedProperty(unittest.TestCase):
        def test_get_read_only(self):
            obj = {'_x': 5}

            # noinspection PyMissingOrEmptyDocstring
            @cached_property
            def x(self):
                return self._x

            # Python 2 and 3 compatible way of adding a class method

# Generated at 2022-06-13 20:39:52.434564
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import TestCase, main
    from flutils.decorators import cached_property

    # Define a class with a cached_property
    class MyClass:
        x = 5

        def __init__(self):
            self.y = 6

        # noinspection PyPep8Naming
        @cached_property
        def my_cached_property(self):
            return self.x + 1

        @asyncio.coroutine
        def my_async_cached_property(self):
            yield None
            return self.y + 1

    # Test that the cached_property returns a value
    obj = MyClass()
    assert obj.my_cached_property == 6

    # Test that the cached_property gets replaced by the value
    assert obj.__dict__['my_cached_property']

# Generated at 2022-06-13 20:39:57.813654
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class _TestClass:
        @cached_property
        def test_cached_property(self):
            return "original property value"

    obj = _TestClass()
    assert obj.test_cached_property == "original property value"

# Generated at 2022-06-13 20:40:03.591205
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    # Make sure we get a property
    assert isinstance(obj.y, property)
    # Make sure the property returns the right value
    assert obj.y == 6



# Generated at 2022-06-13 20:40:07.273768
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo(object):
        def __init__(self, x):
            self.x = x

        @cached_property
        def func(self):
            return self.x + 1

    obj = Foo(5)
    assert obj.func == 6



# Generated at 2022-06-13 20:40:18.472571
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from . import cached_property
    from . import async_cached_property

    class MyClass:

        def __init__(self):
            self.x = 2
            self.y = 3
            self.z = 4

        @cached_property
        def a(self):
            return self.x + self.y
        # s = cached_property(lambda self: self.x + self.y)

        @async_cached_property
        def b(self):
            return self.x + self.y

        @async_cached_property
        def c(self):
            return self.x + self.y

    def test_initial_values(myobj=None):
        myobj = myobj or MyClass()
        assert myobj.x == 2

# Generated at 2022-06-13 20:40:25.267445
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method `~flutils.decorators.cached_property.__get__` of
    class :obj:`~flutils.decorators.cached_property`.

    """

    class Example:

        def __init__(self):
            self.x = 5

        results = []

        @cached_property
        def y(self):
            self.results.append(self.x + 1)  # pragma: no cover
            return self.x + 1

    obj = Example()

    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6



# Generated at 2022-06-13 20:40:33.220536
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            '''A property that is only computed once per instance and then
               replaces itself with an ordinary attribute.

               Deleting the attribute resets the property.
            '''
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    obj.x = 10
    obj.__dict__.pop('y')
    assert obj.y == 11
    assert obj.y == 11
    assert obj.y == 11
    assert obj.__doc__ == '''A property that is only computed once per instance and then
           replaces itself with an ordinary attribute.

           Deleting the attribute resets the property.'''

# Generated at 2022-06-13 20:40:36.927032
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

# Generated at 2022-06-13 20:41:46.236683
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.testing import loop_context

    @cached_property
    def y(self):  # pragma: no cover
        return self.x + 1

    class MyClass:  # pragma: no cover
        def __init__(self):
            self.x = 5

    # test __get__ of class cached_property
    with loop_context() as loop:
        obj = MyClass()
        future = loop.run_until_complete(asyncio.ensure_future(y.__get__(obj, None)))
        loop.run_until_complete(future)
        assert future.result() == 6



# Generated at 2022-06-13 20:41:53.215744
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    y = obj.y
    assert y == 6
    assert obj.y == 6  # noinspection PyStatementEffect
    del obj.y
    assert obj.y == 6


# Generated at 2022-06-13 20:41:58.136854
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()
    assert obj.__dict__ == {'x': 5}
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}



# Generated at 2022-06-13 20:42:05.691981
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Test that y gets cached
    obj = MyClass()
    y = obj.y
    assert y == 6

    # Test that y can be deleted and cached again
    del obj.y
    y = obj.y
    assert y == 6



# Generated at 2022-06-13 20:42:16.609371
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property
    """

    # Make sure that a Python function is not converted to a coroutine
    def func(self):
        return 'Hello World'

    obj = cached_property(func)
    assert asyncio.iscoroutinefunction(obj.func) is False

    # Make sure that a coroutine function is converted to a coroutine
    @asyncio.coroutine
    def func(self):
        return 'Hello World'

    obj = cached_property(func)
    assert asyncio.iscoroutinefunction(obj.func) is True

    # Make sure that a coroutine function is converted to a coroutine
    @asyncio.coroutine
    async def func(self):
        return 'Hello World'

    obj = cached_property(func)
    assert asyncio.iscoroutine

# Generated at 2022-06-13 20:42:23.259300
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
    assert not hasattr(obj, 'y')
    assert obj.y == 11


# Generated at 2022-06-13 20:42:27.825619
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestClass()

    obj.y

    assert isinstance(obj.y, dict)



# Generated at 2022-06-13 20:42:33.399077
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit tests for cached_property method __get__."""

    class Test:
        @cached_property
        def x(self):
            return 1

    test = Test()
    assert test.x == 1
    assert test.x == 1



# Generated at 2022-06-13 20:42:39.330922
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    class Object:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Object()
    assert obj.y == 6
    assert hasattr(obj, 'y')
    del obj.y
    assert not hasattr(obj, 'y')