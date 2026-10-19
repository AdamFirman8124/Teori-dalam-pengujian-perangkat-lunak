

# Generated at 2022-06-13 20:32:43.404741
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    assert A().y == 6


# Generated at 2022-06-13 20:32:48.010989
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



# Generated at 2022-06-13 20:32:55.801577
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():


    import sys
    import unittest

    from unittest import mock

    from flutils.decorators import cached_property
    from flutils.decorators import cached_property

    from flutils.decorators import cached_property


    class test_cached_property__get__(unittest.TestCase):

        def test_get_as_non_coroutine_function(self):
            class Test:

                def __init__(self, *, x=5):
                    self.x = x

                @cached_property
                def y(self):
                    return self.x + 1

            test = Test()
            self.assertEqual(test.y, 6)


# Generated at 2022-06-13 20:33:00.455485
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # noinspection PyUnusedLocal
    @cached_property
    def prop(self):
        return 42

    class Foo:
        x = prop

    foo = Foo()

    # Perform the test
    foo.x
    foo.x
    assert foo.x == 42



# Generated at 2022-06-13 20:33:08.682176
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for :meth:`~flutils.decorators.cached_property.__get__` method.
    """

    class C:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = C()
    assert obj.y == 6
    obj.x = 6
    assert obj.y == 6


# Generated at 2022-06-13 20:33:12.417382
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import mock

    with mock.patch('flutils.decorators.cached_property.asyncio'):
        obj = mock.Mock()
        func = mock.Mock()
        decorator = cached_property(func=func)
        decorator.__get__(obj, None)

# Generated at 2022-06-13 20:33:23.568418
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test method __get__

    def get(self):
        return 2

    cp = cached_property(get)

    class C:
        def __init__(self):
            self.x = 5

        y = cp

    # Note that the attribute ``y`` has not been defined yet.
    obj = C()
    assert obj.y == 2
    assert obj.__dict__ == {"y": 2, "x": 5}

    # This should be a no-op.
    obj.y
    assert obj.__dict__ == {"y": 2, "x": 5}

    # This should be a no-op.
    obj.y = 100
    assert obj.__dict__ == {"y": 100, "x": 5}

# Generated at 2022-06-13 20:33:29.448326
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method ``__get__`` of class :obj:`cached_property`."""
    x = 5

    class ReturnX:
        @cached_property
        def x(self):
            return x

    rx = ReturnX()
    assert rx.x == x



# Generated at 2022-06-13 20:33:41.259290
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test the method __get__ of class cached_property.

    This unit test is a derivative work of the unit test for
    `cached_property <https://bit.ly/2R9U3Qa>`__ and is:

    `Copyright © 2015 Daniel Greenfeld; All Rights Reserved
    <https://bit.ly/2CwtJM1>`__

    """
    import pytest

    class C:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    c = C()
    assert c.y == 6



# Generated at 2022-06-13 20:33:49.015527
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    async def async_method(self):
        """

        :param self:
        :rtype:
        """
        self.x = 2
        await asyncio.sleep(1)
        self.x += 1
        return self.x

    class AsyncClass:

        def __init__(self, x):
            self.__dict__['x'] = x

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return async_method(self)

    x = AsyncClass(2)
    y = x.y
    assert y == 3
    z = x.z
    asyncio.get_event_loop().run_until_complete(z)
    assert z.result() == 4
    assert x.z.result()

# Generated at 2022-06-13 20:34:00.903183
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self, name):
            self.name = name
            self._other = 'some other property'

        @cached_property
        def other(self):
            return self._other

    obj = MyClass('custom object')
    assert obj.__dict__ == {'name': 'custom object', '_other': 'some other property'}
    assert obj.other == 'some other property'
    obj.__dict__ == {'name': 'custom object', '_other': 'some other property', 'other': 'some other property'}

    assert obj.__class__.other is MyClass.other

    try:
        del obj.other
    except AttributeError:
        pass
    else:
        assert False, "you must not be able to delete attribute 'other' via obj.other"



# Generated at 2022-06-13 20:34:09.128028
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.

    **Test conditions**
    * The method is called with obj = None and cls = None.
    * The method is called with obj = None and cls = int.

    **Expected results**
    * The method returns self.
    * The method returns self.

    """
    cp = cached_property(None)
    assert cp.__get__(None, None) is cp
    assert cp.__get__(None, int) is cp



# Generated at 2022-06-13 20:34:13.156821
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property

    """
    from unittest import mock

    @cached_property
    def x(self):
        return self.y

    class MyClass:
        y = 5

    with mock.patch('flutils.decorators.cached_property.cached_property',
                    new=x):
        obj = MyClass()
        assert obj.y == 5

    obj = mock.MagicMock()
    value = obj.__dict__['y'] = x.func(obj)
    assert value == value


if __name__ == '__main__':
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])

# Generated at 2022-06-13 20:34:23.805609
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio
    from time import time

    if sys.version_info >= (3, 8):
        import functools
        print(functools.__file__)

    class Foo:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    foo = Foo(5)
    assert foo.y == 6
    assert foo.__dict__['y'] == 6

    foo.__dict__.pop('y')
    assert foo.y == 6
    assert foo.__dict__['y'] == 6

    foo.__dict__.pop('y')
    foo.x = 10
    assert foo.y == 11
    assert foo.__dict__['y'] == 11


# Generated at 2022-06-13 20:34:28.249266
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    obj = Mock()
    obj.__dict__['x'] = 5
    obj.__dict__['y'] = MagicMock(return_value = 6)
    cached = cached_property(obj.__dict__['y'])
    cached.__get__(obj, obj)
    result = obj.__dict__['y']
    assert isinstance(result, MagicMock)
    assert isinstance(result, MagicMock)
    assert result() == 6

# Generated at 2022-06-13 20:34:32.959110
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    y = obj.y  # noqa: F841


# Generated at 2022-06-13 20:34:34.880960
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass


if __name__ == '__main__':
    import nose

    nose.runmodule()

# Generated at 2022-06-13 20:34:47.375672
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit tests for method __get__ of class cached_property.

    Note:
        Please see the documentation for :class:`cached_property` for
        more information.
    """
    from unittest.mock import Mock

    class Foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Foo()
    obj.__get__ = Mock()
    obj.y
    obj.__get__.assert_not_called()
    obj.__get__ = Mock()
    del obj.y
    obj.__get__.assert_not_called()



# Generated at 2022-06-13 20:34:56.667253
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class CachedPropertyTestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = CachedPropertyTestClass()

    class CachedPropertyTest(unittest.TestCase):
        def test___get__(self):
            self.assertEqual(obj.y, 6)
            self.assertIn('y', obj.__dict__)

    unittest.main()



# Generated at 2022-06-13 20:35:05.756238
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock

    def testFunc():
        return True

    obj_ = cached_property(testFunc)

    cls = Mock()

    obj = Mock()
    obj.__dict__ = {}

    ret = obj_.__get__(obj, cls)
    assert ret is True
    assert obj.__dict__[testFunc.__name__] is True
    assert obj.__dict__[testFunc.__name__] is obj_.func(obj)

# Generated at 2022-06-13 20:35:17.083406
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # noinspection PyPropertyAccess
    assert MyClass.y.__doc__ == 'A property decorator that is only computed ' \
                                'once per instance and then\n        ' \
                                'replaces itself with an ordinary attribute.\n\n' \
                                '        Deleting the attribute resets the ' \
                                'property.\n\n        Note:\n            In ' \
                                'Python 3.8 the :obj:`functools.cached_property` ' \
                                'decorator was\n            added. It is ' \
                                'recommended to use the built-in\n            ' \
                

# Generated at 2022-06-13 20:35:21.920773
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    class Test:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = Test(5)
    assert obj.y == 6



# Generated at 2022-06-13 20:35:26.373022
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class X:

        def foo(self):
            return 42

        y = cached_property(foo)

    x = X()
    y1 = x.y
    y2 = x.y
    assert y1 is y2



# Generated at 2022-06-13 20:35:34.650620
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class test_cached_property___get___obj(object):

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    t = test_cached_property___get___obj()
    assert t.y == 6
    assert t.__dict__["y"] == 6
    assert test_cached_property___get___obj.y == test_cached_property___get__
    del t.y
    assert "y" not in t.__dict__
    assert t.y == 6
    assert t.__dict__["y"] == 6



# Generated at 2022-06-13 20:35:38.673024
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

# Generated at 2022-06-13 20:35:50.993057
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property.

    """
    class Foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            self.x += 1
            return self.x

        @cached_property
        def z(self):
            self.x += 1
            return self.x


    obj = Foo()

    # first call
    assert obj.y == 6
    assert obj.y == 6

    # set a new value for attribute x
    obj.x = 8
    # second call
    assert obj.y == 9
    assert obj.y == 9

    # Now let's set the value of y to be the same as the
    # original value of x
    obj.y = 5
    # third call
   

# Generated at 2022-06-13 20:35:55.670067
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def x(obj):
        return 1
    assert x.__class__.__name__ == 'cached_property'
    ins = x.__get__(None, None)
    assert ins is x, 'type expected to be cached_property'

# Generated at 2022-06-13 20:35:59.236435
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Base():

        @cached_property
        def prop(self):
            return 1

    assert Base.prop == cached_property(Base.prop.func)
    assert Base().prop == 1

# Generated at 2022-06-13 20:36:05.799858
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit tests for cached_property decorator.
    """
    import pytest
    from unittest.mock import Mock

    # Test 1
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    with pytest.raises(AttributeError):
        MyClass.y

    # Test 2
    obj = MyClass()
    assert obj.y == 6

    # Test 3
    assert obj.y == 6

    # Test 4
    class MyClass:
        """This is a sample class.

        *Note:* This is a sample note.
        """

        def __init__(self):
            self.x = 5


# Generated at 2022-06-13 20:36:12.783827
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Monkey:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

       # def z(self):
       #    return self.x + 1

    obj = Monkey()
    assert obj.y == 6
    assert obj.y == 6
#    assert obj.z == 6

# Generated at 2022-06-13 20:36:17.536190
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import doctest

    doctest.testmod()

# Generated at 2022-06-13 20:36:21.044651
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property."""
    # TODO: Modify to test all functionality
    from .test_decorators import test_cached_property__get__ as _test

    _test()

# Generated at 2022-06-13 20:36:26.431709
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property


    class MyClass:
        """Test class."""
        def __init__(self, x): self.x = x

        @cached_property
        def y(self): return self.x

    m = MyClass(5)
    assert m.y == m.y

# Generated at 2022-06-13 20:36:35.076177
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from flutils.helpers import MethodType

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    assert isinstance(obj.y, int)
    assert obj.y == 6
    assert isinstance(MyClass.y, cached_property)
    assert isinstance(obj.y, int)
    assert obj.y == 6
    assert obj.__dict__['y'] == 6

    obj.y = 10

    assert isinstance(obj.y, int)
    assert obj.y == 10
    assert isinstance(MyClass.y, cached_property)
    assert isinstance(obj.y, int)

# Generated at 2022-06-13 20:36:39.693079
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



# Generated at 2022-06-13 20:36:49.691125
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D103
    from typing import Optional
    import asyncio
    import functools
    import pytest
    from flutils.decorators import cached_property
    from .stubs import EvtProp

    # Test code
    class TestClass:

        def __init__(self, x: int = 0) -> None:
            self.x = x

        @cached_property
        def y(self) -> int:
            return self.x + 1

    # Unit tests
    obj = TestClass()
    assert obj.y == 1
    assert 'y' in obj.__dict__

    # When the func param is not callable
    def func1() -> None:
        return None


# Generated at 2022-06-13 20:37:02.047733
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import patch
    from unittest.mock import MagicMock
    from unittest import TestCase
    from unittest import mock

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    test_obj = MyClass()
    test_func = MyClass.y.__get__(None, test_obj)
    assert test_func.__name__ == "y"
    assert test_func.__doc__ is None

    test_func1 = MyClass.y.__get__(None, test_obj)
    test_func2 = MyClass.y.__get__(None, MyClass)
    assert test_obj.y == 6

# Generated at 2022-06-13 20:37:13.697174
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    #
    # class cached_property.__get__(self, obj: Any, cls)
    #
    # Return self.__dict__[self.func.__name__] if obj is None, otherwise
    # set self.__dict__[self.func.__name__] to the
    # result of self.func(obj) and return that result. If
    # self.func is a coroutine, the result is wrapped in
    # an asyncio.coroutine.
    #
    # Examples:
    #
    # >>> obj = MyClass()
    # >>> obj.y
    # 6
    #


    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = 5


# Generated at 2022-06-13 20:37:15.780026
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Tests :func:`cached_property.__get__`"""



# Generated at 2022-06-13 20:37:21.050302
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Foo:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    #  Verify that first call gets the attribute value
    obj = Foo()
    assert obj.y == 6

    #  Verify that second call gets the value from the attribute
    assert obj.y == 6

    #  Verify that deleting the attribute resets the property
    del obj.y
    assert obj.y == 6



# Generated at 2022-06-13 20:37:44.818140
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio
    import pathlib
    import tempfile
    import unittest.mock as mock

    from flutils.decorators import cached_property as cprop

    class MyClass:
        def __init__(self):
            self.x = 5

        @cprop
        def y(self):
            return self.x + 1

    class AsyncClass:
        def __init__(self):
            self.x = 5
            self.my_prop = "test"

        @cprop
        @asyncio.coroutine
        def y(self):
            self.my_prop = yield from self.my_mock()
            return self.x + 1

        @asyncio.coroutine
        def my_mock(self):
            return "my_mock"


# Generated at 2022-06-13 20:37:51.507504
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""
    from pathlib import Path
    from unittest.mock import Mock

    from flutils.decorators import cached_property

    # https://bit.ly/2CwtJM1
    class MyClass:

        @cached_property
        def x(self):
            return 5

    obj = MyClass()
    assert obj._x == 5

    # https://bit.ly/2JbYB5L
    class OtherClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = OtherClass()
    assert obj.y == 6

    # The __get__ has a check for obj being None.

# Generated at 2022-06-13 20:37:55.347372
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # * no arguments
    assert cached_property.__get__(None) is cached_property

    # * cls and obj
    assert isinstance(cached_property.__get__(cached_property, None), cached_property)

# Generated at 2022-06-13 20:38:02.077530
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class ExampleClass:
        @cached_property
        def example_property(self):
            return "example"

        @cached_property
        def another_property(self):
            return "another"

    a = ExampleClass()
    assert a.example_property == "example"
    assert a.__dict__["example_property"] == "example"
    assert "example_property" in a.__dict__
    assert a.another_property == "another"
    assert a.__dict__["another_property"] == "another"
    assert "another_property" in a.__dict__


if __name__ == "__main__":
    test_cached_property___get__()

# Generated at 2022-06-13 20:38:06.060619
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Class:

        @cached_property
        def y(self):
            return 5

    obj = Class()
    assert obj.y == 5
    assert obj.__dict__['y'] == 5


# Generated at 2022-06-13 20:38:07.334507
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    assert False, "Test not implemented."

# Generated at 2022-06-13 20:38:14.265626
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method :meth:`cached_property.__get__` of class
    :class:`cached_property`"""
    object.__new__
    from datetime import datetime
    from mock import patch, Mock

    class Instance:
        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x + 1

    instance = Instance()

    def test_get_get_attribute_returns_val(instance):
        """Test that :func:`cached_property.__get__` returns the value."""
        instance.__dict__["y"] = "Set Value"
        assert cached_property.__get__(instance.y, instance) == "Set Value"


# Generated at 2022-06-13 20:38:20.257820
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

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6

    assert obj.y == 6
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:38:24.701270
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

# Generated at 2022-06-13 20:38:32.316566
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = A()
    assert obj.x == 5
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}


# Generated at 2022-06-13 20:39:01.123392
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    # noinspection PyProtectedMember
    @cached_property
    def myprop(self):
        return 10

    class Test:
        myprop = myprop  # type: ignore

    assert Test.myprop.__doc__ == myprop.__doc__
    assert Test.myprop.__get__(None, Test) == myprop

    obj = Test()
    assert obj.myprop == 10
    assert obj.__dict__['myprop'] == 10
    assert obj.myprop == 10

# Generated at 2022-06-13 20:39:06.061995
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
    print(obj.y)


if __name__ == '__main__':
    test_cached_property___get__()

# Generated at 2022-06-13 20:39:18.261797
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method cached_property.__get__
    """

    @cached_property
    def test_prop():
        """
        Test property.
        """
        return None

    test_val = 'test'

    class TestObj:
        """
        Test class.
        """

        def __init__(self):
            self.x = test_val

        @cached_property
        def y(self):
            return self.x

    tobj = TestObj()
    assert tobj.y == test_val

    # test cache
    tobj.x = 'test2'
    assert tobj.y == test_val

    # test reset
    del tobj.y
    assert tobj.y == 'test2'

    # test docstring

# Generated at 2022-06-13 20:39:27.199443
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test method __get__ of class cached_property"""

    import sys
    import pytest
    from flutils.async_utils import cached_property

    class TmpClass:

        def __init__(self, x=5):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    # Test missing obj
    obj = None
    if sys.version_info >= (3, 8):
        expected = cached_property
    else:
        expected = cached_property(TmpClass.y)

    actual = cached_property(TmpClass.y).__get__(obj)
    assert actual == expected

    # Test no obj
    obj = TmpClass()
    expected = 6

# Generated at 2022-06-13 20:39:31.039286
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Example:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Example()
    assert obj.y == 6

# Generated at 2022-06-13 20:39:35.508199
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import MagicMock

    func = MagicMock()
    instance = MagicMock()

    obj = cached_property(func)
    obj.__get__(instance, object)
    assert func.call_count == 1

# Generated at 2022-06-13 20:39:39.852840
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class MyClass:
        def __init__(self):
            self.x = 7

        @cached_property
        def y(self):
            return self.x

    _ = MyClass()

    assert _.y == 7

# Generated at 2022-06-13 20:39:52.296443
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import patch

    from flutils.decorators import cached_property

    # Test async function
    async def async_func():
        return 5

    class C:
        def __init__(self):
            self._func = async_func

        @cached_property
        def func(self):
            return self._func()

    with patch("flutils.decorators.asyncio.iscoroutinefunction") as m_iscoroutinefunction:
        with patch("flutils.decorators.asyncio.ensure_future") as m_ensure_future:
            m_iscoroutinefunction.return_value = True
            obj = C()
            obj.func
            m_ensure_future.assert_called_once_with(obj._func())

    # Test sync function

# Generated at 2022-06-13 20:39:59.602767
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Unit test for method __get__ of class cached_property """
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:40:04.492094
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class A:
        def __init__(self):
            self.x = 0

        @cached_property
        def y(self):
            return self.x + 1

    a = A()
    assert a.y == 1
    assert a.__dict__.get('y', None) == 1



# Generated at 2022-06-13 20:40:52.602622
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import sentinel

    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            self.x = sentinel.x

        @cached_property
        def y(self):
            return self.x

    obj = MyClass()
    obj.y

    assert obj.__dict__ == {"x": sentinel.x, "y": sentinel.x}

# Generated at 2022-06-13 20:41:02.461648
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class TestCachedProperty__get__(unittest.TestCase):

        def test__get__(self):
            self.assertIs(MyClass.y, cached_property(MyClass.y.func))

    return unittest.TestSuite([
        unittest.defaultTestLoader.loadTestsFromTestCase(
            TestCachedProperty__get__
        )
    ])



# Generated at 2022-06-13 20:41:10.967318
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    # NOTE:
    # Due to the way Python caches `@property` descriptors, the following
    # can only be done after creating an instance of the decorated class
    # and as such prevents testing it as part of a unit test.
    #
    # obj2 = MyClass()
    # obj2.x = 0
    # assert obj.y != obj2.y

    assert obj.y == obj.y
    del obj.y
    assert 'y' not in obj.__dict__
    assert obj.y == obj.y



# Generated at 2022-06-13 20:41:18.923862
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Initialize instance
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """A property."""
            return self.x + 1

    my_obj = MyClass()

    # Validate __doc__ is correct
    if not my_obj.y.__doc__ == 'A property.':
        raise ValueError('cached_property.__get__: \n\tExpected __doc__ to be equal to "A property.".')

    # Validate __name__ is correct
    if not my_obj.y.__name__ == 'y':
        raise ValueError('cached_property.__get__: \n\tExpected __name__ to be equal to "y".')

    # Validate __module__ is correct
   

# Generated at 2022-06-13 20:41:27.296875
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""
    import asyncio
    from flutils.decorators import cached_property

    @cached_property
    def test(self):
        """Return the attribute self.x + 1; for testing."""
        return self.x + 1

    class Test:
        """Class for testing cached_property."""

        def __init__(self, x):
            """Set self.x to argument x; for testing."""
            self.x = x

    obj1 = Test(1)
    obj2 = Test(2)

    assert isinstance(test, cached_property)

    assert test.func.__doc__ == f'test\n\n{test.func.__doc__}'


# Generated at 2022-06-13 20:41:31.574377
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



# Generated at 2022-06-13 20:41:36.872057
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from decimal import Decimal
    from random import randint
    from time import perf_counter
    from types import MethodType, FunctionType

    class TestExample:
        def __init__(self, x=1):
            self.value = 0
            self.x = x

        @cached_property
        def func_1(self):
            return self.value + 1

        @cached_property
        def func_2(self):
            return self.value + 2

        @cached_property
        def func_3(self):
            return self.value + 3

        @cached_property
        def func_4(self):
            return self.value + 4

        @cached_property
        def func_5(self):
            return self.value + 5

       

# Generated at 2022-06-13 20:41:48.055191
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test: method __get__ of class cached_property

    covered branches:
        if obj is None:
        if asyncio.iscoroutinefunction(self.func):
            return self._wrap_in_coroutine(obj)
        else:
            value = obj.__dict__[self.func.__name__] = self.func(obj)
            return value
    """
    from unittest.mock import Mock

    # obj is None, return self
    mock = Mock(spec=cached_property)
    mock.__get__.return_value = cached_property  # bypass comparison with cached_property class
    result = cached_property.__get__(mock)
    assert result == cached_property
    assert mock.__get__.call_count == 1  # verify that it calls cached_property.__get__

# Generated at 2022-06-13 20:41:55.732026
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        from functools import reduce

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])


    obj = MyClass()
    assert obj.y == 6
    assert obj.z == 15

# Generated at 2022-06-13 20:41:59.823142
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    from sys import version_info as sys_version_info

    class MyClass:
        x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    result = obj.y
    expected = 6

    assert result == expected
    assert isinstance(obj.__dict__["y"], int)

    unexpected = obj.x + 1

    assert result != unexpected
    assert obj.y == expected

