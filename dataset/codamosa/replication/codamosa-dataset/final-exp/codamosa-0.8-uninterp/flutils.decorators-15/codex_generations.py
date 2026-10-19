

# Generated at 2022-06-13 20:32:46.105028
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""
    class MyClass(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:32:51.448181
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            self.x += 1
            return self.x

    obj = MyClass()
    assert obj.y == 1
    assert obj.y == 1
    assert obj.x == 1



# Generated at 2022-06-13 20:32:56.283165
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for cached_property"""

    # Test cached_property __get__ --obj is None
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    assert MyClass.y == MyClass.y

    # Test cached_property __get__-- obj is not None
    obj = MyClass()
    assert isinstance(obj.__dict__["y"], int)

    del obj.y
    assert isinstance(obj.__dict__["y"], int)

    return None


# Generated at 2022-06-13 20:33:02.744577
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


cached_property_object = cached_property(cached_property)
cached_property_class = type(cached_property)

# Generated at 2022-06-13 20:33:13.120320
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test cached_property decorator on a class with a blocking method.

    # Execute the following:
    # >>> obj = MyClass()
    # >>> obj.y
    # >>> obj.y

    @cached_property
    def y(self):
        return self.x + 1

    class MyClass:
        def __init__(self):
            self.x = 5

    obj = MyClass()
    assert y.__get__(obj, MyClass) == 6
    assert y.__get__(obj, MyClass) == 6

    # Test cached_property decorator on a class with an async method.
    # Execute the following:
    # >>> obj = MyClass()
    # >>> obj.y
    # >>> obj.y

    @cached_property
    async def y(self):
        return self.x

# Generated at 2022-06-13 20:33:21.348478
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Instantiate the class
    obj = MyClass()

    # Verify the property behaves as expected
    assert obj.y == 6

    # Reset the value of the cached property
    del obj.y

    # Re-run the test
    assert obj.y == 6


# Generated at 2022-06-13 20:33:27.051258
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



# Generated at 2022-06-13 20:33:35.221335
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import patch
    from collections import namedtuple

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1
    # it should return the value for property y
    assert MyClass().y == 6
    # it should return the description for property y
    assert MyClass.__dict__['y'].__doc__ == 'Second level doc string'
    # it should return the value for property y
    assert MyClass().y == 6


# Generated at 2022-06-13 20:33:42.065166
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    # Arrange
    import sys
    if sys.version_info < (3, 8):
        # Act
        # Assert
        assert True
    else:
        # Act
        # Assert
        assert False, "Unit test for method __get__ of class cached_property" \
                      " not implemented"


# Generated at 2022-06-13 20:33:46.324856
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



# Generated at 2022-06-13 20:34:00.065531
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property
    """
    print("\n\n<><><><><><><><><><>")
    print("<><>")
    print("<>   TEST UNIT TEST FOR METHOD __get__ OF CLASS cached_property")
    print("<>")
    print("<><>")
    print("<><><><><><><><><><>")

    class MyClass:

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.x = 5

    print(f"\n<><> obj.y: {obj.y}")

    print(f"\n<><> obj.__dict__: {obj.__dict__}")


# Generated at 2022-06-13 20:34:04.452495
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
    return



# Generated at 2022-06-13 20:34:08.159017
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.

    **Test case**

    #. Create mock object.
    #. Replace instance method 'func' on object to mock method.
    #. Call instance method 'func' with object as argument.
    #. Verify returned value of object __dict__ item 'func' is 5.
    #. Set object __dict__ item 'func' equal to 123.
    #. Call instance method 'func' with object as argument.
    #. Verify returned value of object __dict__ item 'func' is 123.
    """
    class MyClass:

        @cached_property
        def func(self):
            return 5

    obj = MyClass()
    obj.__dict__['func'] = mock.MagicMock(return_value=123)

# Generated at 2022-06-13 20:34:13.007416
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    class MyClass:

        # noinspection PyMissingConstructor
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    assert obj.y == 6
    assert 'y' in obj.__dict__



# Generated at 2022-06-13 20:34:18.915846
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Node:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = Node(5)
    assert obj.y == 6
    assert 'y' in obj.__dict__



# Generated at 2022-06-13 20:34:25.488435
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property

    Tests:

        * :meth:`cached_property.__get__`: Basic functionality

    *New in version 0.2.0*

    """

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:34:34.716089
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Unit test for method __get__ of class cached_property """

    from flutils.decorators import cached_property
    from flutils.misc import ts

    class Foo:

        def __init__(self):
            self._locked = False

        @cached_property
        def bar(self):
            # noinspection PyProtectedMember
            self._locked = True
            return ts()

    foo = Foo()
    foo.bar
    assert foo._locked
    foo.bar
    assert foo._locked



# Generated at 2022-06-13 20:34:40.992863
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached_property's __get__"""

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    res = obj.y
    assert res == 6



# Generated at 2022-06-13 20:34:46.951703
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



# Generated at 2022-06-13 20:34:56.795520
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property

    :return:
    """
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

    obj = MyClass()
    assert obj.y == 6
    del obj.y
    obj.x = 10
    assert obj.y == 11


# Generated at 2022-06-13 20:35:03.870551
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self, x: int):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(5)
    assert obj.y == 6

# Generated at 2022-06-13 20:35:07.763073
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        @cached_property
        def test_y(self):
            return self

    c = MyClass()
    assert c.test_y is c


# Generated at 2022-06-13 20:35:08.744100
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass


# Generated at 2022-06-13 20:35:14.001863
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method ``__get__`` of class ``cached_property``"""

    from flutils.decorators import cached_property


    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6


# Generated at 2022-06-13 20:35:28.623771
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio
    from unittest.mock import call, MagicMock

    @cached_property
    def f1(x):
        return x

    f1(3)
    assert f1.__get__(None) == f1

    mock_obj = MagicMock()
    mock_obj.__dict__ = {}
    f1.__get__(mock_obj)
    assert mock_obj.__dict__["f1"] == 3

    mock_func = MagicMock()
    mock_func.return_value = 42

    @cached_property
    def f2(x):
        return mock_func(x)

    f2(3)
    assert mock_obj.mock_calls == [call(3)]


# Generated at 2022-06-13 20:35:37.142517
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # This method is also tested in test_client.py. However, it's worth
    # mentioning that the cached_property decorator does not work as
    # described in `cached_property <https://bit.ly/2R9U3Qa>`__
    # when it comes to a coroutine function.
    # This test also covers class cached_property
    class TestClass:

        @cached_property
        def cached_property_async(self):
            return 5

        @cached_property
        def cached_property_sync(self):
            return 6

    obj = TestClass()
    obj.cached_property_async
    assert obj.cached_property_async._coro.__name__ == \
        'cached_property_async'

    obj.cached_property_sync
    assert obj

# Generated at 2022-06-13 20:35:45.804338
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass(object):
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x + 1

    obj = MyClass(5)
    assert obj.y == 6
    assert "y" in obj.__dict__
    assert obj.y == obj.__dict__["y"]
    # noinspection PyUnresolvedReferences
    assert obj.__dict__["y"] == obj.y
    assert obj.__dict__["z"] == obj.x + 1
    # noinspection PyUnresolvedReferences
    assert obj.__dict__["z"] == obj.z
    assert obj

# Generated at 2022-06-13 20:35:48.915846
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # GIVEN
    def _fn(arg):
        return arg

    # WHEN
    x = cached_property(_fn)

    # THEN
    assert x.func is _fn



# Generated at 2022-06-13 20:35:55.253158
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method :func:`cached_property.__get__`"""

    from unittest.mock import Mock
    from unittest import TestCase

    from unittest_data_provider import data_provider

    from flutils.decorators import cached_property

    from typing import Iterator, Any

    class TestClass(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1


    class TestClassWithCoroutine(object):
        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            return self.x + 1


    class TestCachedProperty(TestCase):
        provider_test_cached_property___get

# Generated at 2022-06-13 20:36:04.239264
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test that a property that is only computed once per instance and then
    replaces itself with an ordinary attribute

    """
    from flutils.decorators import cached_property
    import asyncio
    import random

    class TestClass:

        def __init__(self, value=None):
            self.value = value

        @cached_property
        def is_value_even(self):
            return self.value % 2 == 0

    # Test normal asynchronous property
    @asyncio.coroutine
    def async_test():
        value = random.randint(1, 99)
        test_obj = TestClass(value)
        assert test_obj.is_value_even is (value % 2 == 0)
        assert test_obj.__dict__['is_value_even'] is (value % 2 == 0)


# Generated at 2022-06-13 20:36:17.022652
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.utils import get_readonly_properties
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert isinstance(obj.__dict__['y'], int)

    # Make sure it doesn't show up in get_readonly_properties function
    assert 'y' not in get_readonly_properties(obj)


if __name__ == '__main__':
    import pytest

    pytest.main(['-rx', '-v', '--pdb', __file__])

# Generated at 2022-06-13 20:36:21.279998
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        _y = 5

        @cached_property
        def y(self):
            return self._y + 1

    obj = MyClass()
    assert obj.y == 6

    obj._y = 10
    assert obj.y == 6

# Generated at 2022-06-13 20:36:26.239768
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:36:28.975505
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Tests the method __get__ of class cached_property.

    *New in version 0.2.0*

    """
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:36:32.133159
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:

        @cached_property
        def test(self):
            """A test."""
            return 5

    assert Test().test == 5
    assert Test.test.__doc__ == Test().test.__doc__

# Generated at 2022-06-13 20:36:42.978439
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self, val):
            self.val = val
            self.call_count = 0

        @cached_property
        def prop(self):
            self.call_count += 1
            return self.val

    assert A(1).call_count == 0
    a = A(1)
    assert a.prop == 1
    assert a.call_count == 1
    assert a.prop == 1
    assert a.call_count == 1

    assert a.__dict__['prop'] == 1

    a.prop = 2
    assert a.__dict__['prop'] == 2
    assert a.call_count == 1

    del a.prop
    assert 'prop' not in a.__dict__
    assert a.call_count == 1

    assert a.prop == 1

# Generated at 2022-06-13 20:36:53.270292
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property.

    This test conciously does not use the
    :lambda:`flutils.decorators.cached_property` decorator in the
    :class:`MyClass` class. This allows the
    :meth:`flutils.decorators.cached_property.__get__` method to be
    tested without the
    :meth:`flutils.decorators.cached_property.__init__` method being
    invoked.

    """
    class MyClass:
        """."""

        def __init__(self):
            """."""
            self.x = 5

        def y(self):
            """."""
            return self.x + 1

    obj = MyClass()

# Generated at 2022-06-13 20:37:04.566074
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def cached_property_1(self):
            return self.x + 1

        @cached_property  # noqa: PVS-C0103
        def cached_property_2(self):  # noqa: PVS-C0103
            return self.x + 2

        @cached_property  # noqa: PVS-C0103
        def cached_property_3(self):  # noqa: PVS-C0103
            return self.x + 3

        @cached_property  # noqa: PVS-C0103
        def cached_property_4(self):  # noqa: PVS-C0103
            return self.x + 4


# Generated at 2022-06-13 20:37:16.325139
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from functools import partialmethod

    class TestDict(object):
        def __init__(self, value):
            self.value = value

        def __get__(self, instance, cls):
            return self.value

    class TestCls:
        @cached_property
        def func(self):
            # print(self)
            return "func"

        @cached_property
        def prop(self):
            return TestDict("prop")

        @cached_property
        def func2(self):
            return "func2"

        @cached_property
        def func3(self):
            return "func3"

        @cached_property
        def method(self):
            # print(self)
            return partialmethod(self.__class__.method_f, self)


# Generated at 2022-06-13 20:37:23.705235
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test for :meth:`flutils.decorators.cached_property.__get__`.

    Purpose:
        Test that :meth:`~flutils.decorators.cached_property.__get__`
        performs as expected.

    Assertions:
        - The method returns None if the instance is None.
        - The method returns the method being decorated if the instance is
          None.
        - The method returns the cached value if the instance is not None.
        - The method adds the `func.__name__` attribute to the instance dict.

    Returns:
        None: The six.assertRaises method raises an AssertionError if the
        asserts fail.

    """

# Generated at 2022-06-13 20:37:36.533136
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    # noinspection PyProtectedMember
    class TestCachedProperty:
        """Test class for cached_property."""

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = TestCachedProperty()
    # y is an ordinary attribute following the first call to __get__
    assert obj.y == 6
    obj.x = 1
    # calling y again returns the cached value despite the change to self.x
    assert obj.y == 6

    # the property can still be overwritten
    obj.y = 7
    assert obj.y == 7

    # deleting the property also deletes the cached value
    del obj.y
    # this causes the property to

# Generated at 2022-06-13 20:37:43.524528
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test case(s)
    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Verify that
    assert TestClass().y == 6



# Generated at 2022-06-13 20:37:51.001603
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import TestCase
    from unittest.mock import patch

    from flutils.decorators import cached_property

    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Test this property."""
            return self.x + 1

        @cached_property
        @asyncio.coroutine
        def z(self):
            """Test this coroutine property."""
            return self.x + 2

    class TestCachedProperty(TestCase):

        @patch('flutils.decorators.asyncio')
        def test_default(self, mock_asyncio):
            """Test the cached_property decorator."""
            mock_asyncio.iscoroutinefunction.return_value = False
           

# Generated at 2022-06-13 20:37:59.529449
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property.

    This test is to ensure the decorator :obj:`cached_property` works as
    expected.

    Built against:
        - Python 3.6.6
        - flutils 2.1.0

    :return: No return.
    :rtype: None

    """

    from flutils.decorators import cached_property

    class Base(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    base = Base()
    assert base.y == 6



# Generated at 2022-06-13 20:38:08.617011
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Create class and instance to test against
    class TestCachedProperty:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        @cached_property
        def z(self):
            return self.x + self.y

    test_property = TestCachedProperty(1, 2)

    # Test
    test_property.z

    assert test_property.z == 3  # noqa: WPS452
    assert isinstance(test_property.z, int)

# Generated at 2022-06-13 20:38:20.683153
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from dataclasses import dataclass
    from unittest.mock import Mock

    @dataclass
    class MyClass:
        x: int

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(x=5)
    assert obj.y == 6
    assert isinstance(obj, MyClass)

    obj2 = MyClass(x=15)
    assert obj2.y == 16
    assert isinstance(obj2, MyClass)

    obj.x = 10
    assert obj.y == 6
    assert isinstance(obj, MyClass)
    obj.__dict__[obj.y.__name__] = 10
    assert obj.y == 10
    assert isinstance(obj, MyClass)

    obj3 = MyClass(x=15)
   

# Generated at 2022-06-13 20:38:32.698820
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass(object):
        def __init__(self, value):
            self.value = value

        @cached_property
        def x(self):
            return self.y + 1

        @cached_property
        def y(self):
            return self.value + 1

    # The method __get__ returns the function object when accessed via the
    # class
    assert cached_property.__get__(None, MyClass) == cached_property
    assert MyClass.x == cached_property

    # The method __get__ returns a wrapper around the actual cached property
    # value when accessed via the class instance
    assert MyClass(1).x == 3
    assert MyClass(1).x == 3
    assert MyClass(2).x == 4
    assert MyClass(1).x == 3
    assert MyClass(2).x

# Generated at 2022-06-13 20:38:37.875709
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Setup
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self, value: int = 5):
            self.value = value

        @cached_property
        def prop(self):
            return self.value

    obj = MyClass()

    # Exercise
    result = obj.prop

    # Verify
    assert result == 5



# Generated at 2022-06-13 20:38:50.247525
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock

    # from flutils.decorators import cached_property
    # from flutils.decorators import cached_property

    obj = MagicMock(name='obj')
    cls = MagicMock(name='cls')
    cp = cached_property.__get__(obj=obj, cls=cls)
    cp.__doc__ = 'test'
    cp.func = MagicMock(name='func')
    assert cp.__doc__ == 'test'
    assert cp.func == MagicMock(name='func')
    assert cp.__get__(obj=obj, cls=cls) == MagicMock(name='func')
    obj.__dict__.__getitem__.side_effect = KeyError

# Generated at 2022-06-13 20:39:00.144403
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from itertools import count

    class MyClass:
        def __init__(self):
            self.x = count()

        @cached_property
        def y(self):
            return next(self.x)

    obj = MyClass()
    assert obj.y == 0
    assert obj.y == 0
    assert obj.y == 0
    del obj.y
    assert obj.y == 1
    assert obj.y == 1
    assert obj.y == 1
    del obj.y
    assert obj.y == 2
    assert obj.y == 2
    assert obj.y == 2



# Generated at 2022-06-13 20:39:19.000719
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class C:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    c = C(1)
    c.y
    assert c.y == 2
    assert c.__dict__['y'] == 2



# Generated at 2022-06-13 20:39:27.458686
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Asyncio version
    async def func():
        return 5

    async def func2():
        return 10

    class Obj:
        @cached_property
        def x(self):
            return func()

        @cached_property
        def y(self):
            return func2()

    obj = Obj()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(obj.x)

    assert obj.x == 5
    del obj.x
    assert not hasattr(obj, 'x')

    # Non-asyncio version
    class Obj:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Obj()

    assert obj.y == 6

# Generated at 2022-06-13 20:39:40.541518
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from itertools import count
    from unittest import TestCase

    class MyClass(object):

        def __init__(self):
            self.y = count()

        @cached_property
        def x(self):
            return next(self.y)

    class MySubClass(MyClass):
        pass

    class TestClass(TestCase):

        def setUp(self):
            self.my_class = MyClass()
            self.my_subclass = MySubClass()

        def test_cached_property_returns_correct_value(self):
            self.assertIs(self.my_class.x, 0)
            self.assertIs(self.my_class.x, 0)


# Generated at 2022-06-13 20:39:52.368335
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        def another_method(self):
            return self.x - 1

    obj = MyClass()

    assert obj.y == 6
    assert 'y' in obj.__dict__

    del obj.y
    assert 'y' not in obj.__dict__

    obj.x = 8
    assert obj.y == 9
    assert 'y' in obj.__dict__
    assert obj.another_method() == 7


if __name__ == '__main__':

    import pytest

    pytest.main(['--capture=sys', '--verbose', '-k', __file__])

# Generated at 2022-06-13 20:39:56.756039
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test for cached_property.__get__
    """

    # noinspection PyMethodMayBeStatic
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # Test that an attribute was added to the object
    assert hasattr(obj, 'y')

    # Test attribute value
    assert obj.y == 6

    # Test that an attribute was added to the object's dict
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:40:07.425007
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # pragma: no cover
    global results
    results = []

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            results.append(1)
            return self.x + 1

    obj = MyClass()
    # test cached behavior
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    assert results == [1]
    # test clearing cached
    del obj.y
    # test uncached behavior
    assert obj.y == 6
    assert obj

# Generated at 2022-06-13 20:40:11.752243
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # mock data
    class Class:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Class()

    # test
    assert obj.y == 6



# Generated at 2022-06-13 20:40:16.667696
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    result = obj.y
    assert result == 6

    obj.x = 100
    result = obj.y
    assert result == 6



# Generated at 2022-06-13 20:40:25.681085
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit tests for method flutils.decorators.cached_property.__get__
    """

    # noinspection PyUnusedLocal
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return asyncio.sleep(0.1)

    obj = MyClass()
    # noinspection PyTypeChecker
    assert obj.y == 6
    assert "y" in obj.__dict__
    del obj.y
    assert "y" not in obj.__dict__
    # noinspection PyTypeChecker
    assert obj.z == obj.z
    assert "z" in obj.__dict__

# Generated at 2022-06-13 20:40:33.168441
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from ..logging import TRACE

    TRACE()

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    obj.y += 5

    assert obj.y == 11

    del obj.y

    assert obj.y == 6

# Generated at 2022-06-13 20:41:00.424551
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Setup
    class TestObj:
        @cached_property
        def test_prop(self):
            return 42
    obj = TestObj()

    # Execute
    value = obj.test_prop
    value_again = obj.test_prop

    # Verify
    assert obj.test_prop == 42
    assert value == value_again

# Generated at 2022-06-13 20:41:04.776441
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

# Generated at 2022-06-13 20:41:11.239103
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.

    This method is responsible for returning the value of the
    :obj:`~flutils.decorators.cached_property` decorated property.

    """
    from flutils.decorators import cached_property

    from typing import Any

    class MyClass:

        """Sample class for testing."""

        def __init__(self):
            """Initialize instance."""
            self.x = 5

        @cached_property
        def y(self):
            """Sample property for testing."""
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:41:15.280373
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class AClass:
        def __init__(self, x: int):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    a = AClass(5)
    assert a.y == a.x + 1



# Generated at 2022-06-13 20:41:22.768089
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        @property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    obj.x = 10
    assert obj.y == 11



# Generated at 2022-06-13 20:41:37.331208
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    bloat = Bunch(__name__="bloat")

    class Bar:
        pass

    # Test for class attribute with function value
    def func():
        return 1

    assert cached_property.__get__(func, Bar) is func

    # Test for class attribute with property value
    bar = Bar()
    bar.quux = 'quux'

    # Test for class attribute with property value
    class Foo:
        quux = cached_property(lambda: 'quux')

        @classmethod
        def foo(cls):
            return 'foo'

    f = Foo()
    assert f.quux == 'quux'

    # Test for class method
    assert Foo.foo() == 'foo'

    # Test for cached property
    class Foo:
        @cached_property
        def bar(self):
            return

# Generated at 2022-06-13 20:41:42.740033
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from .decorators import cached_property

    class Test:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Test()
    assert obj.y == 6



# Generated at 2022-06-13 20:41:43.504440
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:41:53.683437
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Check that the property is cached
    obj = MyClass()
    first = obj.y
    second = obj.y
    assert first == second

    # Check that the property is reset after deletion
    del obj.y
    assert hasattr(obj, 'y') is False
    third = obj.y
    assert third != first



# Generated at 2022-06-13 20:41:58.554280
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class T(object):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """y docstring"""
            return self.x + 1

    obj = T()
    assert isinstance(obj.y, int)
    assert obj.y == 6
    assert obj.y == 6

    assert T.y.__doc__ == "y docstring"

