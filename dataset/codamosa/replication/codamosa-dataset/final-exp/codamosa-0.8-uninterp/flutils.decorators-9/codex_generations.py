

# Generated at 2022-06-13 20:32:44.047347
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    # Setup a basic class
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:32:49.957369
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



# Generated at 2022-06-13 20:32:51.809625
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class C:
        @cached_property
        def x(self):
            return 42
    assert C().x == 42


# Generated at 2022-06-13 20:33:04.131592
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D401
    from flutils.obj import get_attribute_names

    class Foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    foo = Foo()
    assert foo.y == 6
    # Check that y was added to Foo
    assert get_attribute_names(Foo) == {'__init__', 'x', 'y'}
    # Check that y was added to foo

# Generated at 2022-06-13 20:33:05.596416
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass



# Generated at 2022-06-13 20:33:09.986084
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    def func(self):
        return 5
    cprop = cached_property(func)
    class Class:
        method = cprop
        def __init__(self):
            pass
    obj = Class()
    assert obj.method == 5
    del obj.method
    assert obj.method == 5


# Generated at 2022-06-13 20:33:12.730810
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

# Generated at 2022-06-13 20:33:24.300404
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio
    from flutils.decorators import cached_property

    # Test caching for synchronous
    class MyClass:

        def __init__(self, x: int):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(5)
    assert obj.y == 6
    obj.x = 5.1
    assert obj.y == 6
    del obj.y
    obj.x = 5
    assert obj.y == 6
    obj.x = 5.1
    assert obj.y == 6

    # Test caching for coroutine function
    @asyncio.coroutine
    def get_x():
        return 5


# Generated at 2022-06-13 20:33:32.422567
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # this test is required to help mypy determine the types of cached_property
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6


if __name__ == "__main__":  # pragma: no branch
    from flutils.testhelpers import print_object

    print_object(cached_property)

# Generated at 2022-06-13 20:33:40.281346
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A(object):
        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            return self.x + 1

    a = A()
    assert a.y == 1
    assert a.__dict__['y'] == 1
    a.x = 1
    assert a.y == 1
    assert a.__dict__['y'] == 1



# Generated at 2022-06-13 20:33:49.413151
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class flutils.decorators.cached_property"""

    class Foo:

        def __init__(self):
            self.x = 5

        # noinspection PyUnusedLocal
        def _y(self):
            """Returns `x+1`"""
            return self.x + 1

        y = cached_property(_y)

        def __repr__(self):
            return '{{x = {x}, y = {y}}}'.format(x=self.x, y=self.y)

    # noinspection PyUnresolvedReferences
    # noinspection PyProtectedMember
    assert Foo.y.__doc__ == 'Returns `x+1`'
    foo1 = Foo()
    assert foo1.y == 6
    foo1.x = 10
    assert foo1

# Generated at 2022-06-13 20:33:54.668001
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
    return True



# Generated at 2022-06-13 20:33:56.331409
# Unit test for method __get__ of class cached_property

# Generated at 2022-06-13 20:34:03.575562
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import IsolatedAsyncioTestCase, main
    from unittest.mock import Mock, patch

    from flutils.decorators import cached_property
    from flutils.testing import BaseAsyncTestCase

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            try:
                self.loop.run_until_complete(asyncio.sleep(0.1))
            finally:
                return self.x + 1


# Generated at 2022-06-13 20:34:06.230558
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    def __get__(self, obj: Any, cls: type) -> Any:
        return self.__get__(obj, cls)



# Generated at 2022-06-13 20:34:13.250123
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Note: Some unit tests for cached_property must be written Python >= 3.8
    #       because tests using asyncio and async require Python >= 3.7

    # See: https://bit.ly/36Hg6U5
    if sys.version_info < (3, 7):
        return

    @cached_property
    def my_property():
        """A property."""
        return True

    obj = "my_property"

    ret = my_property.__get__(obj, None)
    assert ret is my_property



# Generated at 2022-06-13 20:34:19.440569
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class x:
        def __init__(self):
            self.x = 5
    class dummy:
        @cached_property
        def y(self):
            return self.x + 1
    a = x()
    b = dummy()
    b.x = a
    assert b.y == 6


# Generated at 2022-06-13 20:34:27.878450
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from random import randint
    import unittest


    class SomeClass:

        def __init__(self, seed=None):
            self.i = seed or randint(1, 10)

        @cached_property
        def y(self):
            return self.i + 1


    class Test_cached_property___get__(unittest.TestCase):

        def test_cached_property___get__(self):
            sc = SomeClass()
            self.assertEqual(sc.i + 1, sc.y)
            self.assertTrue(sc.y is sc.y)  # noqa: WPS609


    if __name__ == "__main__":
        unittest.main()

# Generated at 2022-06-13 20:34:32.188548
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

# Generated at 2022-06-13 20:34:39.463562
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test when obj is None
    class TestClass:
        @cached_property
        def func1(self):
            return True

    func = TestClass.__dict__['func1'].__get__(None, TestClass)
    assert isinstance(func, cached_property)

    # Test when obj is not None
    class TestClass:
        @cached_property
        def func1(self):
            return True

    ClassObj = TestClass()
    func = TestClass.__dict__['func1'].__get__(ClassObj, TestClass)
    assert ClassObj.__dict__['func1'] is True
    assert func is True



# Generated at 2022-06-13 20:34:54.107228
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for cached_property.__get__."""

    from typing import List, Dict

    mock_cls = type('MockClass', (object,), {})

    # noinspection PyUnusedLocal
    def func(self):  # type: (MockClass) -> None
        """Testing."""

    decorator = cached_property(func)

    obj = MockClass()

    # Test case 1: class method.
    expected_value = decorator
    actual_value = decorator.__get__(obj, MockClass)
    assert expected_value == actual_value

    # Test case 2: instance method.
    expected_value = None
    actual_value = decorator.__get__(obj, None)
    assert expected_value == actual_value



# Generated at 2022-06-13 20:34:59.195386
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


# Generated at 2022-06-13 20:35:03.750509
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class A:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    assert A(5).y == 6



# Generated at 2022-06-13 20:35:10.310445
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest as pt

    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    x = TestClass()
    pt.assert_equal(x.y, 6)
    pt.assert_equal(x.__dict__.get('y'), 6)


# Unit test to ensure docstring is copied to the wrapper

# Generated at 2022-06-13 20:35:14.308438
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # noinspection PyPep8Naming
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:35:22.626004
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

    del obj.y
    assert obj.y == 11

# Generated at 2022-06-13 20:35:28.560704
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test to assert that __get__ of class cached_property returns the
    right value
    """
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:35:37.117306
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property

    Also tests the class docstring example.

    """

    import logging
    import pytest

    _logger = logging.getLogger(__name__)
    _logger.addHandler(logging.NullHandler())

    # setup _logger
    # -------------
    _logger.setLevel(logging.DEBUG)

    # Tests
    # -----
    _logger.info('Testing method __get__ of class cached_property')

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    assert obj.y == 6
    assert obj.__dict__['y'] == 6


# Generated at 2022-06-13 20:35:41.144270
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



# Generated at 2022-06-13 20:35:46.758702
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def power(self):
            return self.x ** 2

    obj = MyClass()
    assert obj.power == 25

    obj.x = 10
    assert obj.power == 25

    del obj.power
    assert obj.power == 100



# Generated at 2022-06-13 20:35:58.041547
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    obj = MyClass()
    obj.y

    assert obj.y == 6



# Generated at 2022-06-13 20:36:02.298517
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



# Generated at 2022-06-13 20:36:06.753199
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

# Generated at 2022-06-13 20:36:13.968022
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:

        def __init__(self):
            self.x = 7

        @cached_property
        def y(self):
            return self.x + 1

    test = Test()
    assert test.y == 8

    test.y = 5  # Change the object property
    test.x = 9  # Change the underlying property
    assert test.y == 8  # cached_property doesn't change when underlying
    # is changed

# Generated at 2022-06-13 20:36:19.168444
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from .cached_property import cached_property
    from .dataclass_abc import dataclass_abc
    from .str_mixin import StrMixin

    @dataclass_abc
    class MyClass(StrMixin):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6

# Generated at 2022-06-13 20:36:30.661172
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """

    :return:


    Code:

        from flutils.decorators import cached_property

        class A:
            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

    """

    class A:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    a = A()
    assert "y" not in a.__dict__
    assert a.y == 6
    assert "y" in a.__dict__


if __name__ == "__main__":

    import logging

    logger = logging.getLogger("flutils")
    logger.setLevel(logging.DEBUG)
    logger.prop

# Generated at 2022-06-13 20:36:42.351614
# Unit test for method __get__ of class cached_property

# Generated at 2022-06-13 20:36:48.011157
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class _C:
        def __init__(self, x):
            self.x = x
            self.y = 2 * x
            self.z = 3 * x

        @cached_property
        def a(self):
            return self.x + self.y

        @cached_property
        def b(self):
            return self.x + self.a

    c = _C(5)
    assert c.a == 15 == c.b == 20 == c.x + c.a == c.x + c.y



# Generated at 2022-06-13 20:36:52.645132
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property
    """
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    from collections import ChainMap

    obj = MyClass()
    assert obj.y == 6
    assert isinstance(obj.__dict__, ChainMap)
    assert obj.__dict__['y'] == 6

# Generated at 2022-06-13 20:37:03.820494
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test for cached_property.__get__.

    """
    from flutils.decorators import cached_property

    class Testing(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x + 2

    # Test __get__
    obj = Testing()
    obj.y
    assert obj.y == 6
    obj.x = 10
    assert obj.y == 11
    delattr(obj, 'y')
    obj.z
    assert obj.z == 12
    obj.x = 15
    assert obj.z == 17
    obj.__dict__.pop('z')
    assert 'z' not in obj.__

# Generated at 2022-06-13 20:37:32.212449
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
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6 and obj.z == 6
    assert obj.__dict__ == {'x': 5, 'y': 6, 'z': 6}

if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:37:36.233257
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property
    """

    import doctest

    results = doctest.testmod()
    assert not results.failed

# Generated at 2022-06-13 20:37:48.835024
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from pytest import raises
    from flutils.decorators import cached_property

    class Foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Test that the property is computed once.
    obj = Foo()
    assert obj.y == 6
    assert obj.y == 6

    # Test that the property is reset upon attribute deletion.
    del obj.y
    assert obj.y == 6
    del obj.y
    assert obj.y == 6

    # Test with a coroutine function.
    @cached_property
    async def z(self):
        return self.x + 1

    assert raises(AttributeError, lambda: z)


# Generated at 2022-06-13 20:37:55.482355
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""
    class CachedPropClass:

        def __init__(self, x):
            self.x = x

        @cached_property
        def cached_prop(self):
            return self.x

    obj = CachedPropClass(1)
    assert obj.cached_prop == 1
    obj.x = 5
    assert obj.cached_prop == 1

# Generated at 2022-06-13 20:37:59.605790
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Prepare for the test
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Do the test
    obj = MyClass()

    # Do asserts
    assert obj.y == 6


# Generated at 2022-06-13 20:38:11.494173
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import sys
    import gc
    import asyncio

    # Test the case where obj is None
    class MyClass:

        def __init__(self):
            pass

        @cached_property
        def y(self):
            return 5

    obj = MyClass()
    assert isinstance(obj.y, cached_property)

    # Test the case where obj is not None

    # Test the case where func is not an asyncio coroutine
    class MyClass:

        def __init__(self):
            pass

        @cached_property
        def y(self):
            return 5

    obj = MyClass()
    assert isinstance(obj.y, int)
    assert obj.y == 5

    # Test the case where func is an asyncio coroutine

# Generated at 2022-06-13 20:38:18.793370
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method :func:`~flutils.decorators.cached_property.__get__`
    of class :obj:`~flutils.decorators.cached_property`
    """
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:38:31.215861
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    import unittest

    class TestCase(unittest.TestCase):

        def test_doc_string(self):
            self.assertTrue(cached_property.__doc__)

        def test_synchronous_method(self):

            class TestClass:

                def __init__(self):
                    self.attr = 0

                @cached_property
                def get_attr(self):
                    return self.attr

            test_obj = TestClass()

            attr_from_test_obj_1 = test_obj.get_attr

            self.assertEqual(0, attr_from_test_obj_1)

            attr_from_test_obj_2 = test_obj.get_attr


# Generated at 2022-06-13 20:38:39.640565
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D103
    class Test:

        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            self.x += 1
            return self.x

        @cached_property
        def z(self):
            self.x += 1
            return self.x

    test = Test()

    assert test.x == 0
    assert test.y == 1
    assert test.y == 1
    assert test.y == 1
    assert test.x == 1
    assert test.z == 2
    assert test.z == 2
    assert test.z == 2
    assert test.x == 2

    del test.y

    assert "y" not in test.__dict__
    assert test.x == 2
    assert test.z == 2


# Generated at 2022-06-13 20:38:50.479870
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

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            return await asyncio.sleep(0, self.x + 1)

    obj = MyClass()
    asyncio.get_event_loop().run_until_complete(obj.y)

    assert obj.y == 6




# Generated at 2022-06-13 20:39:37.376521
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.testhelpers import assert_equal

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert_equal(obj.y, 6)
    assert_equal(obj.y, 6)



# Generated at 2022-06-13 20:39:43.153020
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
    assert obj.__dict__[obj.y.__name__] == 6
    del obj.y
    assert obj.y == 6
    assert obj.__dict__[obj.y.__name__] == 6



# Generated at 2022-06-13 20:39:54.125252
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests: test_cached_property___get__

    """
    #
    # class MyClass:
    #     def __init__(self):
    #         self.x = 5
    #
    #     @cached_property
    #     def y(self):
    #         return self.x + 1
    #
    # obj = MyClass()
    #
    # # ---------------------------------------------------------
    #
    # assert obj.y == 6
    #
    # obj.x = 10
    #
    # assert obj.y == 6  # still 6 because obj.y is a cached_property
    #
    # # ---------------------------------------------------------
    #
    # obj.y = 20
    #
    # assert obj.y == 20  # now 20 because we've set it
    #
    # # ---------------------------------------------------------

# Generated at 2022-06-13 20:39:57.640565
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:
        @cached_property
        def foo(self):
            return 1729

    test = Test()
    assert test.foo == 1729
    test.foo = 42

    assert test.foo == 1729



# Generated at 2022-06-13 20:40:05.874555
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x

    obj = MyClass()
    assert obj.y == 5
    obj.x = 6
    assert obj.y == 5
    
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    obj.x = 6
    assert obj.y == 6

# Generated at 2022-06-13 20:40:16.030585
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method :meth:`cached_property.__get__` of class
    :class:`cached_property`.

    Purpose:
        Test that the value of a cached_property is evaluated only once.

    Return:
        ``None``

    """
    class Sample:
        def __init__(self, value):
            self.value = value

        @cached_property
        def compute_value(self):
            self.value += 1
            return self.value

    s = Sample(1)
    assert s.compute_value == 2
    # Second call will return the cached property, without calling the
    # compute_value method.
    assert s.compute_value == 2



# Generated at 2022-06-13 20:40:21.248743
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test the method __get__ of the class cached_property"""
    class MyClass:
        def __init__(self):
            self.x = 3

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 4
    delattr(obj, 'y')
    assert obj.y == 4

# Generated at 2022-06-13 20:40:30.761737
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached_property"""
    class C:
        @cached_property
        def x(self):
            return 5

    c = C()
    print(C.x)
    print(c.x)
    c.x = 4
    print(c.x)

    # Test that cache is deleted
    del c.x
    print(c.x)

    # Test that 

    class C2:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    c = C2(5)
    print(C2.y)
    print(c.y)



# Generated at 2022-06-13 20:40:38.839309
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Create class to test
    class MyClass(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            time.sleep(1)
            return self.x + 1

    # Test it

# Generated at 2022-06-13 20:40:46.357038
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import patch

    with patch('flutils.decorators.cached_property.asyncio.iscoroutinefunction') as m_iscrf:
        m_iscrf.return_value = False
        cp = cached_property(lambda obj: 5)
        class Obj:
            pass
        obj = Obj()
        cp_get = cp.__get__(obj, Obj)
        assert callable(cp_get)
        assert cp_get.__name__ == 'wrapper'
        assert cp_get.__doc__ == None
        cp_get()
        assert obj.__dict__['wrapper'] == 5

    with patch('flutils.decorators.cached_property.asyncio.iscoroutinefunction') as m_iscrf:
        m_iscrf.return_value = True


# Generated at 2022-06-13 20:42:14.344791
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property.

    """
    class C:

        @cached_property
        def prop(self):
            return True

    a = C()
    assert a.prop is True



# Generated at 2022-06-13 20:42:16.766415
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def x(self):
        return 5

    class MyClass:
        x = x

    assert MyClass().x == 5



# Generated at 2022-06-13 20:42:24.637506
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self):
            self.x = 5

        # noinspection PyMethodParameters
        @cached_property
        def y(self):
            return self.x + 1

    obj = A()
    obj.y
    obj.y
    assert 'y' in obj.__dict__
    del obj.__dict__['y']
    assert 'y' not in obj.__dict__


if __name__ == '__main__':
    import pytest

    pytest.main([__file__])

# Generated at 2022-06-13 20:42:27.667673
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

# Generated at 2022-06-13 20:42:39.927981
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import functools
    import asyncio

    class C(object):
        @cached_property
        def x(self):
            """I am the 'x' property."""
            print("x")
            return 42

        @cached_property
        def y(self):
            """I am the 'y' property."""
            return 2 * self.x

        @cached_property
        def z(self):
            """I am the 'z' property."""
            return self.z

        @cached_property
        def w(self):
            """I am the 'w' property."""
            raise RuntimeError('Oops')

    @cached_property
    def a(self):
        print("a")
        return 1

    @cached_property
    def b(self):
        print("b")
