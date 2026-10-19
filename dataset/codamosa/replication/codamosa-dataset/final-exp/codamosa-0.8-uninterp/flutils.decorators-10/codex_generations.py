

# Generated at 2022-06-13 20:32:39.578976
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MockClass:
        @cached_property
        def y(self):
            return self.x + 1

        def __init__(self):
            self.x = 5

    obj = MockClass()
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}



# Generated at 2022-06-13 20:32:52.130099
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Method __get__ of class cached_property.

    This method is intended to be used only internally by cached_property.
    """

    import asyncio

    class A:

        @cached_property
        def a(self):
            return 5

    a = A()
    assert a.a == 5
    a.a = 42
    assert a.a == 42

    class B:

        @asyncio.coroutine
        def b(self):
            yield from asyncio.sleep(1)
            return 5

        @cached_property
        def a(self):
            return self.b

    b = B()
    assert asyncio.iscoroutine(b.a)
    assert asyncio.iscoroutinefunction(b.a)
    # noinspection PyTypeChecker
    assert asyncio.iscor

# Generated at 2022-06-13 20:32:56.920299
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

# Generated at 2022-06-13 20:33:06.213477
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    import asyncio

    class MyClass:
        def __init__(self, x: int):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        async def z(self):
            await asyncio.sleep(1)
            return self.x + 1

    obj = MyClass(5)
    assert obj.y == 6
    assert type(obj.y) == int
    assert obj.__dict__ == {'x': 5, 'y': 6}
    obj = MyClass(10)
    assert obj.y == 11
    assert type(obj.y) == int
    assert obj.__dict__ == {'x': 10, 'y': 11}
    assert asyncio

# Generated at 2022-06-13 20:33:10.114463
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



# Generated at 2022-06-13 20:33:20.212231
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.

    :return: ``None``
    """
    import pytest

    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.y

    with pytest.raises(AttributeError):
        obj.x

    return


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:33:22.766024
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Set up test
    obj = NamedTemporaryFile(mode='w+')
    obj.name


if __name__ == "__main__":
    test_cached_property___get__()

# Generated at 2022-06-13 20:33:35.188288
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # pylint: disable=missing-class-docstring,missing-function-docstring,invalid-name
    class foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            print("I will be computed only once")
            return self.x + 1

    class bar(foo):
        pass

    obj = foo()
    obj.y
    delattr(obj, "y")
    assert not hasattr(obj, "y")
    obj.y
    obj.y
    assert obj.y == 6
    obj.x = 5
    obj.y
    assert obj.y == 6
    obj.x = 20
    obj.y
    assert obj.y == 6
    obj.x = 5
    obj.y
    assert obj.y

# Generated at 2022-06-13 20:33:44.670471
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class O:
        @cached_property
        def f(self):
            return 0

    o = O()
    assert o.__dict__ == {}
    assert o.f == 0
    assert o.__dict__ == {'f': 0}
    assert o.f == 0
    assert o.__dict__ == {'f': 0}

    del o.f
    assert o.__dict__ == {}
    assert o.f == 0
    assert o.__dict__ == {'f': 0}
    assert o.f == 0
    assert o.__dict__ == {'f': 0}


# Generated at 2022-06-13 20:33:46.411334
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass


# Generated at 2022-06-13 20:33:57.185539
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
    # ensure cached_property works with async
    if sys.version_info >= (3, 6, 0):
        # noinspection PyProtectedMember
        assert MyClass.y.__objclass__ is None



# Generated at 2022-06-13 20:34:01.410497
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D103
    class MyClass:
        def __init__(self):
            self.x = 5
            self.y = 0

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    obj.x = 10
    assert obj.y == 6
    del obj.y
    assert obj.y == 11

# Generated at 2022-06-13 20:34:11.569752
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    test_obj = cached_property(lambda x: x)
    # test case when obj is None
    test_cls = object()
    assert test_obj.__get__(obj=None, cls=test_cls) is test_obj
    # test case when obj is not None
    obj = object()
    prop_name = 'foo'
    value = 1
    test_obj = cached_property(lambda x: value)
    obj.__dict__[prop_name] = None
    assert test_obj.__get__(obj, cls=object) is value
    assert prop_name in obj.__dict__
    assert obj.__dict__[prop_name] is value


# Generated at 2022-06-13 20:34:23.343420
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    dobj = MyClass()

    assert dobj.y == 6
    assert dobj.__dict__ == {'x': 5, 'y': 6}

    #
    # Test that the property is cached
    #
    dobj.x = 1
    assert dobj.y == 6
    assert dobj.__dict__ == {'x': 1, 'y': 6}

    #
    # Test that the cached value can be deleted, and the property
    # will be re-computed
    #
    del dobj.y
    assert not hasattr(dobj, 'y')
    assert dobj.y == 2

# Generated at 2022-06-13 20:34:30.169957
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock, patch

    from flutils.decorators import cached_property

    m = MagicMock()

    # Test for no object
    cp = cached_property(m)
    assert cp.__get__(None, None) == cp

    # Test for an object
    # noinspection PyArgumentList
    value = MagicMock()
    m.__name__ = 'y'
    m.return_value = value
    obj = MagicMock()
    assert cp.__get__(obj, None) is value
    assert m.called
    assert m.call_args == ((obj,),)
    assert obj.__dict__['y'] is value

    # Test for an async object
    m.reset_mock()
    m.return_value = asyncio.Future()


# Generated at 2022-06-13 20:34:39.267314
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from sys import version_info

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    if version_info >= (3, 8):
        assert isinstance(obj.y, int)
    else:
        assert isinstance(obj.y, asyncio.Future)

    assert obj.y == 6


if __name__ == '__main__':
    import os
    import sys
    pytest_dir = os.path.join(os.path.dirname(__file__), '../tests')
    sys.exit(pytest.main([pytest_dir]))

# Generated at 2022-06-13 20:34:50.333406
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest.mock as mock

    obj_mock = mock.MagicMock()
    func_mock = mock.MagicMock()

    expected_value = 'ReturnedValue'
    obj_mock.__dict__[func_mock.__name__] = expected_value
    func_mock.return_value = expected_value

    decorator = cached_property(func_mock)
    result = decorator.__get__(obj_mock, None)

    assert result == expected_value
    func_mock.assert_not_called()
    obj_mock.__dict__[func_mock.__name__] == expected_value


# Generated at 2022-06-13 20:34:54.345030
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached_property.__get__.
    """
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:34:58.617130
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from flutils.py23compat import IS_PYTHON_2

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    del obj.y
    assert obj.y == 6

# Generated at 2022-06-13 20:35:05.868213
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    def test_function(self):
        return 5

    test_instance = type('test_instance', (object,), {})()
    test_attr = "test_attr"
    expected_result = 5
    test_result = cached_property(test_function).__get__(test_instance, None)
    assert test_result == expected_result
    assert test_instance.__dict__[test_attr] == expected_result


# Generated at 2022-06-13 20:35:12.644528
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
    obj.x = 25
    assert obj.y == 6


# Generated at 2022-06-13 20:35:18.651907
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method ``__get__`` of class ``cached_property``.
    """

    class MyClass:

        def __init__(self, x=0):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    myclass = MyClass(x=5)

    assert myclass.y == 6



# Generated at 2022-06-13 20:35:24.985736
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for :meth:`cached_property.__get__`"""

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:35:30.041516
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def func(self):
        return self.x + 1

    class myclass:
        def __init__(self):
            self.x = 5

    obj = myclass()
    func.__get__(obj, None) == 6



# Generated at 2022-06-13 20:35:41.877054
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test when property is not in the object's __dict__
    class Test(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    t = Test()
    assert t.y == 6
    assert t.__dict__ == {'x': 5, 'y': 6}

    # Test when property is already in the object's __dict__
    assert t.y == 6
    assert t.__dict__ == {'x': 5, 'y': 6}

    # Test when property is already in the object's __dict__ as a future
    t.__dict__['y'] = object()
    assert t.y == 6
    assert t.__dict__ == {'x': 5, 'y': 6}


# Unit

# Generated at 2022-06-13 20:35:52.120454
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    ck = obj.__dict__.get('y')
    assert ck is None

    obj.y
    ck = obj.__dict__.get('y')
    assert ck == 6

    obj.y
    assert ck == 6

    obj.x = 6

    obj.y
    assert ck == 6

    del obj.y
    ck = obj.__dict__.get('y')
    assert ck is None

# -----------------------------------------------------------------------------
# Copyright 2015 Daniel Greenfeld
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in

# Generated at 2022-06-13 20:35:58.582338
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:

        def __init__(self):
            """
            Args:
                x (int): The value of x to be added to
            """
            self.x = 5

        @cached_property
        def y(self):
            """The value of x plus 1"""
            return self.x + 1

    a = A()
    assert a.y == 6
    assert a.y == 6

# Generated at 2022-06-13 20:36:02.887836
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property


    class MyClass:
        """This is a test class for testing method __get__ of class cached_property
        """
        val = 5

        @cached_property
        def y(self):
            return self.val


    myobj = MyClass()
    assert myobj.y == 5



# Generated at 2022-06-13 20:36:10.012935
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class MyClass(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert 'y' in obj.__dict__



# Generated at 2022-06-13 20:36:11.905315
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

# Generated at 2022-06-13 20:36:19.518847
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

    obj.x += 1
    assert obj.y == 6

    del obj.y
    assert obj.y == 7


# Generated at 2022-06-13 20:36:30.895806
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Foo:
        def __init__(self):
            self.counter = 0

        @cached_property
        def foo(self):
            self.counter += 1
            return self.counter

    foo1 = Foo()

    assert foo1.foo == 1
    assert foo1.__dict__ == {"counter": 1, "foo": 1}

    assert foo1.foo == 1

    foo1.foo = 42

    assert foo1.__dict__ == {"counter": 1, "foo": 42}

    assert foo1.foo == 42

    del foo1.foo

    assert foo1.__dict__ == {"counter": 1}

    assert foo1.foo == 2

    foo1.__dict__["foo"] = 42

    assert foo1.foo == 42

# Generated at 2022-06-13 20:36:42.420421
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    import pytest

    from flutils.decorators import cached_property


    # Test that cached_property decorator functions properly.
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1


    expected = 6
    obj = MyClass()
    assert expected == obj.y

    # Test that an exception raised from the cached property is properly
    # handled.
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            raise ValueError


    obj = MyClass()
    with pytest.raises(ValueError):
        _ = obj.y

# Generated at 2022-06-13 20:36:52.591952
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""
    from flutils.decorators import cached_property


    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1


    obj = MyClass()

    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}
    del obj.y
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}

    import asyncio
    import async_timeout


# Generated at 2022-06-13 20:37:00.135290
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class Class(object):

        @cached_property
        def x(self):
            return 1

    class TestCachedProperty(unittest.TestCase):

        def test_cached_property___get__(self):
            class_ = Class()
            result = class_.x
            expected = 1
            self.assertEqual(result, expected)

    if __name__ == "__main__":
        unittest.main()

# Generated at 2022-06-13 20:37:05.667363
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property.
    """

    class SomeClass:
        @cached_property
        def x(self):
            return 5

    obj = SomeClass()

    assert obj.x == 5
    assert obj.__dict__['x'] == 5



# Generated at 2022-06-13 20:37:16.621247
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Class1:
        def __init__(self, value):
            self._value = value

        @cached_property
        def value(self):
            return self._value

        @cached_property
        def other_value(self):
            return self.value + 1

    class Class2:
        def __init__(self, value):
            self._value = value

        @cached_property
        async def value(self):
            return self._value

        @cached_property
        async def other_value(self):
            return self.value + 1

    def test_object_value(obj):
        assert obj.value == 1
        assert obj.other_value == 2
        assert obj.__dict__['value'] == 1
        assert obj.__dict__['other_value'] == 2
        assert Class1

# Generated at 2022-06-13 20:37:23.805018
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test when obj is None
    cp = cached_property(lambda x: x)
    assert cp is cp.__get__(None, None)
    # Test when obj is not None, and func is not a coroutine function
    cp = cached_property(lambda x: x)
    assert cp.__get__(0, None) == 0
    # Test when obj is not None, and func is a coroutine function
    cp = cached_property(lambda x: asyncio.sleep(0, result=x))
    assert cp.__get__(0, None) == 0


if __name__ == '__main__':
    pytest.main([__file__])

# Generated at 2022-06-13 20:37:34.177510
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    #
    # Test __get__
    #
    import pytest

    class TestClass:
        @cached_property
        def foo(self):
            """
            :return:
            """
            return 'foo'

        @cached_property
        def fubar(self):
            """
            :return:
            """
            return 'fubar'

    tc = TestClass()
    assert tc.foo == 'foo'
    assert tc.fubar == 'fubar'

    # Test for obj being None
    assert isinstance(TestClass.foo, cached_property)
    assert TestClass.foo.__doc__ == '\n    :return:\n    '

    with pytest.raises(AttributeError):
        assert TestClass.foo == 'foo'

    tc_2 = TestClass()
   

# Generated at 2022-06-13 20:37:42.590780
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    # Arrange
    @cached_property
    def x(self):
        return self.y * 10

    class Foo:
        y = 5

        def __init__(self):
            pass

    # Act
    foo = Foo()
    x = foo.x

    # Assert
    assert x == 50
    assert callable(foo.x) is False
    assert isinstance(foo.x, int) is True

# Generated at 2022-06-13 20:37:59.968730
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method `cached_property.__get__`"""

    @cached_property
    def my_cached_property_method(obj):
        """Returns ``42``."""
        return 42

    # Test property is not set initially
    obj = _CachedPropertyTestClass()
    assert 'my_cached_property_method' not in obj.__dict__
    # Test property is set
    # Note: Caching occurs in `__get__`
    assert obj.my_cached_property_method == 42
    # Test property is set
    assert 'my_cached_property_method' in obj.__dict__
    # Test property is the same as cached value
    assert obj.__dict__['my_cached_property_method'] == 42



# Generated at 2022-06-13 20:38:03.832153
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        pass

    assert cached_property.__get__(None, MyClass) is cached_property



# Generated at 2022-06-13 20:38:12.533258
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # pylint: disable=invalid-name,too-few-public-methods
    class TestClass:

        def __init__(self):
            self._list = [1, 2, 3]

        def _get(self) -> list:
            return self._list

        @cached_property
        def test_list(self) -> list:
            return self._get()

    test_obj = TestClass()
    assert test_obj.test_list == test_obj._list
    assert test_obj.test_list is test_obj._list

    assert test_obj.__dict__['test_list'] == test_obj.test_list
    assert test_obj.__dict__['test_list'] is test_obj.test_list

# Generated at 2022-06-13 20:38:22.137474
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit testing for method __get__ of class cached_property in
    decorators module

    References
    ----------
    see:

    - https://bit.ly/2F4koM4
    - https://bit.ly/2JBKxEw
    - https://bit.ly/2H3oyqq
    - https://bit.ly/2JjK0xH

    """
    # testing class
    class TestClass:
        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            self.x += 1
            return self.x

    # testing
    obj = TestClass()

    assert obj.y == 1
    assert obj.y == 1
    assert obj.x == 1

    del obj.y

    assert obj.y == 2

# Generated at 2022-06-13 20:38:36.757613
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # Verify the property is set to the expected value
    assert obj.y == 6
    # Verify the attribute was added to the object's __dict__
    assert "y" in obj.__dict__
    # Verify the attribute's value is the same as the property
    assert obj.__dict__["y"] == 6
    # Verify the property is unchanged by setting __dict__["y"]
    obj.__dict__["y"] = 2
    assert obj.y == 6
    # Verify the property is reset when deleting __dict__["y"]
    del obj.__dict__["y"]
    assert obj.y == 6


# Unit

# Generated at 2022-06-13 20:38:38.464911
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of cached_property."""



# Generated at 2022-06-13 20:38:50.584669
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Foo:
        _y = 0

        @cached_property
        def y(self):
            self._y += 1
            return self._y

    class Bar(Foo):
        pass

    foo = Foo()
    bar = Bar()

    assert Foo.__dict__['y'].__get__(foo) == 1
    assert Bar.__dict__['y'].__get__(bar) == 1
    assert foo.y == 1
    assert bar.y == 1
    assert foo._y == 1
    assert bar._y == 1

    assert Foo.__dict__['y'].__get__(foo) == 1
    assert Bar.__dict__['y'].__get__(bar) == 1
    assert foo.y == 1
    assert bar.y == 1
    assert foo._y == 1

# Generated at 2022-06-13 20:38:57.381091
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class TestClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    result = TestClass()
    assert result.y == 6
    assert result.__dict__['y'] == 6


# Generated at 2022-06-13 20:39:07.620815
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    x = 0

    class A:

        @cached_property
        def foo(self):
            nonlocal x
            x += 1
            return x

    a = A()
    with pytest.raises(TypeError, match="cached_property object is not callable"):
        a.foo()

    a.foo = 1
    assert a.foo == 1

    assert a.foo == 1
    b = A()
    assert b.foo == 2
    assert b.foo == 2

    # Test coroutine
    async def async_test():
        assert await a.foo == 1
        assert await b.foo == 2
        assert a.foo.done()
        assert b.foo.done()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_test())



# Generated at 2022-06-13 20:39:19.720385
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Unit test for method __get__ of class cached_property """

    import unittest

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class Test_cached_property(unittest.TestCase):

        def test_init(self):
            """
            Unit test for method __init__ of class cached_property
            """
            self.assertEqual(MyClass().y, 6)

        def test_get(self):
            """
            Unit test for method __get__ of class cached_property
            """
            self.assertEqual(MyClass().y, 6)


# Generated at 2022-06-13 20:39:46.206605
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property."""
    # noinspection PyUnusedLocal,PyStatementEffect
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}

# Generated at 2022-06-13 20:39:55.328989
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.testingutils import Runner
    from flutils.decorators import cached_property

    @cached_property
    def prop_cached(self):
        """ Cached property """
        return 4 + 2

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """ Cached property """
            return self.x + 1

    class Test(Runner):

        def setUp(self):
            self.obj = MyClass()

        def test_doc_string(self):
            """ test_doc_string
            Doc strings for cached properties copied through
            """
            self.assertEqual(prop_cached.__doc__, " Cached property ")

# Generated at 2022-06-13 20:40:01.706474
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test(object):
        i = 0
        @cached_property
        def foo(self):
            # __init__ is not called during __get__ when accessing static
            # members, so we have to make sure foo is called as a class method
            Test.i += 1
            return 'foo'
    assert Test().i == 1
    assert Test().foo == 'foo'
    assert Test.i == 1
    assert Test.foo == 'foo'
    assert Test().i == 2

# Generated at 2022-06-13 20:40:12.973955
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    import sys
    import pytest
    from subprocess import Popen, PIPE
    from typing import Any, Tuple, Optional

    python_version = sys.version_info

    if python_version >= (3, 8):

        @cached_property
        def x2(self):
            return self.x + 1

        class X:

            def __init__(self):
                self.x = 5
                self.y = x2

            @cached_property
            def y(self):
                return self.x + 2

        obj = X()
        y1 = obj.y
        y2 = obj.y
        assert y1 == y2
        assert y1 == 7
        assert obj.__dict__ == {'x': 5, 'y': 7}


# Generated at 2022-06-13 20:40:21.847932
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest.mock as mock
    from flutils.decorators import cached_property

    class A:
        @cached_property
        def test(self):
            return True

    a = A()
    assert a.test is True
    a.test = False
    assert a.test is False
    a.__dict__['test'] = mock.MagicMock(wraps=a.__dict__['test'])
    assert a.test.call_args is None

# Generated at 2022-06-13 20:40:31.060739
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """The class :class:`~flutils.decorators.cached_property` method
    :meth:`~flutils.decorators.cached_property.__get__` has 100% code
    coverage.
    """
    import pytest
    from flutils.decorators import cached_property

    class Test:

        @cached_property
        def prop(self):
            return self.x + 1

    obj = Test()
    obj.x = 5
    assert obj.prop == 6

    with pytest.raises(AttributeError):
        del obj.prop
    assert obj.prop == 6

    obj.prop = 5
    assert obj.prop == 5



# Generated at 2022-06-13 20:40:35.607617
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method ``__get__`` of class ``cached_property``."""

    class Test(object):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Test()
    assert obj.y == 6


# Generated at 2022-06-13 20:40:42.426562
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method ``__get__`` of class ``cached_property``.
    """

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:40:48.536604
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests for method cached_property.__get__.

    """
    _prop = cached_property(lambda _: 'foo')

    _get = _prop.__get__
    assert _get(None, None) is _prop
    assert _get('foo', None) == 'foo'



# Generated at 2022-06-13 20:40:53.147373
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Setup:
    class MockClass:

        def __init__(self, my_attr):
            self.my_attr = my_attr

        @cached_property
        def my_prop(self):
            return self.my_attr

    # Setup:
    mock_class = MockClass(5)

    # Test
    assert mock_class.my_prop == 5

    # Test:
    mock_class.my_prop = 10

    # Test:
    assert mock_class.my_prop == 10

# Generated at 2022-06-13 20:41:46.145555
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    @cached_property
    def x(self):
        return 5

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return 5

    class MyOtherClass:
        x = x

    class Test(unittest.TestCase):

        def test_nonetype(self):

            self.assertEqual(x, 5)

        def test_MyClass(self):

            obj = MyClass()
            self.assertEqual(obj.y, 5)

        def test_MyOtherClass(self):

            self.assertEqual(MyOtherClass.x, 5)


if __name__ == '__main__':
    unittest.main()

# Generated at 2022-06-13 20:41:55.570435
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    result = object()

    # noinspection PyArgumentList
    class MyClass:

        def __init__(self):
            self.x = 5

        # If a function is a coroutine function, then return a coroutine.
        # This will avoid forcing the caller to do an extra await.
        @cached_property
        async def func(self):
            return result

    obj = MyClass()
    coro = obj.func
    assert asyncio.iscoroutine(coro)
    assert coro is not result
    assert result is await coro



# Generated at 2022-06-13 20:41:58.134030
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

# Generated at 2022-06-13 20:42:10.934321
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """This method tests the method :meth:`~flutils.decorators.cached_property.__get__`
    of the class :class:`~flutils.decorators.cached_property`.

    """
    try:
        import unittest
    except ImportError:
        import unittest2 as unittest

    from flutils.decorators import cached_property

    class TestClass(object):
        """Test class for :class:`~flutils.decorators.cached_property`.

        """

        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        @cached_property
        def z(self):
            return self.x + self.y


# Generated at 2022-06-13 20:42:14.811585
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



# Generated at 2022-06-13 20:42:23.293974
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest.mock as mock

    func = mock.Mock()
    return_val = object()
    func.return_value = return_val

    desc = cached_property(func)

    no_obj = desc.__get__(None, object)
    assert no_obj is desc
    assert func.call_count == 0

    obj = object()
    with_obj = desc.__get__(obj, object)
    assert with_obj is return_val
    assert func.call_count == 1
    assert func.call_args_list == [mock.call(obj)]

# Generated at 2022-06-13 20:42:31.093546
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from inspect import iscoroutinefunction
    from unittest import TestCase

    class MyClass(TestCase):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj.y
    assert obj.__dict__['y'] == 6
    assert iscoroutinefunction(obj.y)

    class MyClass(TestCase):

        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            await asyncio.sleep(0.1, loop=asyncio.get_event_loop())
            return self.x + 1

    obj = MyClass()
    obj.y
    assert obj.__dict__['y']

# Generated at 2022-06-13 20:42:31.744289
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:42:36.773663
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from .test_utils import create_test_object, assert_result
    test_object = create_test_object(cached_property)

    obj = test_object()
    result = obj.cached_property()
    assert_result(result=result, expected=8)

