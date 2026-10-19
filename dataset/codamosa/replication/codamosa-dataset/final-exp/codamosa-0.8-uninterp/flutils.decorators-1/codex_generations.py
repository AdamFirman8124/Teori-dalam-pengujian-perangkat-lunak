

# Generated at 2022-06-13 20:32:40.934585
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        # The following method is not properties or cached properties and
        # should not be part of the tests
        def z(self):
            return self.x + 2

    # Get the value
    obj = MyClass()
    assert obj.y == 6

    # Delete the cached attribute and make sure it is recalculated
    del obj.y
    assert obj.y == 6

    # Remove the attribute and check for KeyError
    class TestException(Exception):
        pass

    with unittest.mock.patch(
        'asyncio.iscoroutinefunction', return_value=True
    ):
        obj = MyClass()
       

# Generated at 2022-06-13 20:32:51.970994
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property
    """

    from flutils.decorators import cached_property

    class A:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    assert A(1).y == 2
    assert A(1).y == 2
    assert A(2).y == 3

    a = A(1)
    a.y

    try:
        a.y = 'a'
    except AttributeError:
        pass

    try:
        del a.y
    except AttributeError:
        pass

    assert a.y == 2



# Generated at 2022-06-13 20:33:00.312712
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property
    """
    class _TestClass:
        @cached_property
        def x(self):
            return 5

    test_inst = _TestClass()
    # test that it returns the proper value
    assert test_inst.x == 5
    # test that the value did get cached
    assert test_inst.__dict__.get("x") == 5
    del test_inst.x
    with pytest.raises(AttributeError):
        test_inst.x

# Generated at 2022-06-13 20:33:11.229263
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def init(self):
            self.x = 5

        @cached_property
        def y(self):
            self.z = self.x + 1
            return self.z

    obj = MyClass()
    assert isinstance(obj, MyClass)
    assert hasattr(obj, 'x')
    assert hasattr(obj, 'y')
    assert hasattr(obj, 'init')
    assert not hasattr(obj, 'z')
    obj.init()
    assert obj.x == 5
    assert obj.y == 6
    assert obj.z == 6
    del obj.y
    assert obj.y == 6
    assert obj.z == 6

# Generated at 2022-06-13 20:33:23.038399
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit testing for method :meth:`cached_property.__get__`."""
    from datetime import datetime
    from unittest.mock import patch
    from .cached_property import cached_property  # to avoid recursion!

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    with patch(
        "flutils.decorators.cached_property.asyncio.iscoroutinefunction"
    ) as mock_iscoroutinefunction:
        # Must not be a coroutine function
        mock_iscoroutinefunction.return_value = False
        assert obj.y == 6

    # Must be a coroutine function

# Generated at 2022-06-13 20:33:29.448723
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
    assert obj.y == 6



# Generated at 2022-06-13 20:33:43.022588
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.tests.helpers import capture_stdout

    _expect_result = """
    ex_cached_property_test
    No output.
    """

    @cached_property
    def ex_cached_property_test(self):
        self._ex_cached_property_test = 'test value'
        return None

    class TestClass:
        def __init__(self):
            self._ex_cached_property_test = None

    # noinspection PyProtectedMember
    with capture_stdout() as cap:
        test_class = TestClass()
        ex_cached_property_test(test_class)
        print('No output.')
        print(test_class._ex_cached_property_test)

    print(cap.out)

    assert cap.out.strip()

# Generated at 2022-06-13 20:33:46.245812
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    assert MyClass().y == 6



# Generated at 2022-06-13 20:33:58.880535
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    def class_under_test():
        class ClassUnderTest:
            @cached_property
            def y(self):
                return "pre-cached"

            def __init__(self):
                pass

        return ClassUnderTest()


    def class_under_test_del_y():
        class ClassUnderTest:
            @cached_property
            def y(self):
                return "pre-cached"

            def __init__(self):
                pass

        obj = ClassUnderTest()
        del obj.y
        return obj

    def class_under_test_del_y_in_descriptor():
        class ClassUnderTest:
            @cached_property
            def y(self):
                return "pre-cached"

            def __init__(self):
                pass

        obj = ClassUnderTest

# Generated at 2022-06-13 20:34:02.583041
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    assert MyClass().y == 6



# Generated at 2022-06-13 20:34:11.149921
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            return self.x + 2

    _t = TestClass()
    _t.y
    _t.z
    assert 'z' in _t.__dict__
    assert 'y' in _t.__dict__



# Generated at 2022-06-13 20:34:17.760522
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MethodCallCounter:
        def __init__(self):
            self.mock = Mock()
            self.method_call_count = 0

        def __call__(self, *args, **kwargs):
            self.method_call_count += 1
            self.mock(*args, **kwargs)

    obj = MethodCallCounter()
    class TestClass(object):
        @cached_property
        def method(self):
            return obj
    instance = TestClass()
    assert not obj.method_call_count
    assert instance.method == obj
    assert obj.method_call_count == 1
    assert not obj.method_call_count
    assert instance.method == obj
    assert obj.method_call_count == 1


# Generated at 2022-06-13 20:34:23.303891
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property"""

    # noinspection PyUnresolvedReferences
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(x=5)
    assert obj.y == 6

    obj = MyClass(x=10)
    assert obj.y == 11

# Generated at 2022-06-13 20:34:26.986107
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
    assert hasattr(obj, 'y')
    assert obj.y == 6


# Generated at 2022-06-13 20:34:29.089442
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method cached_property.__get__

        Placeholder

    """
    pass

# Generated at 2022-06-13 20:34:35.791504
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Execute the cached_property.__get__ method.

    """
    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self):
            pass

        @cached_property
        def x(self):
            return 5

    obj = MyClass()
    assert obj.x == 5

    obj.x = 7
    assert obj.x == 7



# Generated at 2022-06-13 20:34:40.951975
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Foo:

        def __init__(self, idx):
            self.idx = idx

        @cached_property
        def odd_or_even(self):
            return 'odd' if self.idx % 2 else 'even'

    foo = Foo(2)
    assert foo.odd_or_even == 'even'
    foo.idx = 7
    assert foo.odd_or_even == 'even'

    foo = Foo(3)
    assert foo.odd_or_even == 'odd'
    foo.idx = 10
    assert foo.odd_or_even == 'odd'



# Generated at 2022-06-13 20:34:48.873541
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    This first test ensures that:

    1) The return value of the decorated method is returned
    2) The method is only called once

    """

    class Test:
        x = 5

        @cached_property
        def y(self):
            self.x += 1
            return self.x

    obj = Test()
    assert obj.y == 6
    assert obj.y == 6



# Generated at 2022-06-13 20:34:57.998051
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property.

    :return: No return.
    :rtype: None
    """

    import os
    import sys
    import unittest
    from functools import reduce
    from shutil import rmtree
    from tempfile import mkdtemp

    from flutils.decorators import cached_property

    class CachingTest(unittest.TestCase):
        """Test class for cached_property class.

        """

        def setUp(self):
            """setup for tests.

            """

            # calc members for testing
            self.base_dir = mkdtemp()
            self.dir = os.path.join(self.base_dir, "test")
            self.sub_dir_1 = os.path.join(self.dir, "sub_dir_1")

# Generated at 2022-06-13 20:35:09.352134
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    @cached_property
    def func(self):
        return 1

    # Create an object and verify that the cached_property's __get__ method
    # returns the value returned by the method the cached_property is
    # decorating
    obj = object
    assert func.__get__(obj, type(obj)) == 1

    # Test that the cached_property's __get__ method returns a coroutine
    # when the method the cached_property is decorating is a coroutine
    @cached_property
    def func2(self):
        return asyncio.ensure_future(asyncio.sleep(1))

    assert isinstance(func2.__get__(obj, type(obj)), asyncio.coroutines.CoroWrapper)

# Generated at 2022-06-13 20:35:16.971958
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Return x+1"""
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

# Generated at 2022-06-13 20:35:23.189307
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached_property.__get__."""

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """The cached method."""
            return self.x + 1

    obj = MyClass()
    expected = 6
    actual = obj.y
    assert actual == expected



# Generated at 2022-06-13 20:35:34.429318
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class TestClass:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            async def async_z():
                r = await asyncio.sleep(0.001, result=(self.x + 1))
                return r

            return async_z  # make sure method cached_property___get__ is able to
                            # detect that method z returns an async callable

    test_obj = TestClass(1)
    assert test_obj.__dict__ == {'x': 1}

    test_obj.__dict__.pop('y')
    test_obj.y
    assert test_obj.__dict__ == {'x': 1, 'y': 2}

   

# Generated at 2022-06-13 20:35:44.520699
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    from flutils.decorators import cached_property

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            """Get the value of y."""
            return self.x + 1

    class AsyncClass:
        def __init__(self):
            self.x = 5

        @cached_property
        async def y(self):
            """Get the value of y."""
            return self.x + 1

    obj = MyClass()
    assert getattr(obj, '_y', None) is None
    y = obj.y
    assert y == 6
    assert obj._y == 6
    assert obj.y == 6
    assert obj.__doc__ == 'Get the value of y.'


# Generated at 2022-06-13 20:35:48.963513
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class Robot:

        @cached_property
        def name(self):
            return "Marvin"

    r = Robot()

    assert r.name == "Marvin"


if __name__ == '__main__':
    pytest.main([__file__])

# Generated at 2022-06-13 20:35:55.253013
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    import unittest

    from flutils.decorators import cached_property
    from flutils.decorators import CachedProperty

    class TestCachedProperty(unittest.TestCase):

        def test_cached_property__get__(self):
            """Unit test for method ``__get__`` of class
            ``CachedProperty``.

            Notes:
             * Tested with Python 3.6.3, 3.6.4, 3.7.0, 3.7.1, and 3.7.2.
             * This test was added after discovering that the code originally
               used to determine the class the property was accessed from was
               not working in all cases.

            """

            class TestObj:

                def __init__(self):
                    self.x

# Generated at 2022-06-13 20:36:02.042448
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Create a new class for testing
    class Interpreter:
        __slots__ = ["parser"]

        def __init__(self, parser):
            self.parser = parser

        @cached_property
        def arg_names(self):
            return self.parser.args[:]

    # Create a new Interpreter object
    interp = Interpreter("parser")

    # Make sure that the arg_names property returns a list of arguments
    assert interp.arg_names == ["parser"]



# Generated at 2022-06-13 20:36:08.331934
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.debugging import test_mode

    with test_mode():

        class Test:

            def __init__(self):
                self.x = 5

            @cached_property
            def y(self):
                return self.x + 1

        obj = Test()
        assert obj.y == 6



# Generated at 2022-06-13 20:36:18.294804
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method `__get__` of class :class:`cached_property`.

    See Also:
        * :func:`cached_property.__get__`

    """
    import unittest
    from unittest.mock import Mock

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class TestCachedProperty(unittest.TestCase):

        def setUp(self):
            self.obj = MyClass()
            self.obj_dict = self.obj.__dict__


# Generated at 2022-06-13 20:36:30.057917
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import functools
    import types
    import pytest
    from flutils.decorators import cached_property

    @functools.total_ordering
    class MyClass:

        def __init__(self, x: int = 5):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            raise ValueError("Error!")

    obj = MyClass()

    # get the value
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    # reset the value
    del obj.y
    assert 'y' not in obj.__dict__
    # get the value
    assert obj.y == 6
    assert obj.__dict__['y'] == 6

    #

# Generated at 2022-06-13 20:36:42.654111
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
    assert obj.__dict__['y'] == 6
    assert obj.y == 6

# Generated at 2022-06-13 20:36:47.736471
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
    # Ensure object attribute is set
    assert obj.__dict__['y'] == 6
    # Ensure cached property is set
    assert MyClass.y.__dict__['func'](obj) == 6



# Generated at 2022-06-13 20:36:48.252391
# Unit test for method __get__ of class cached_property
def test_cached_property___get__(): return


# Generated at 2022-06-13 20:36:49.392023
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Unit test for method __get__ of class cached_property
    """



# Generated at 2022-06-13 20:36:53.647172
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property

    class Simple:
        @cached_property
        def x(self):
            return 1

    simple = Simple()
    assert simple.x == 1



# Generated at 2022-06-13 20:37:00.134555
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    obj = DummyCachedProperty()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    del obj.y
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    assert obj.z == 6
    assert obj.__dict__['z'] == 6
    del obj.z
    assert obj.z == 6
    assert obj.__dict__['z'] == 6



# Generated at 2022-06-13 20:37:12.140510
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from unittest.mock import patch


    class DummyObject:
        pass

    class DummyDescriptor:
        def __get__(self, obj, cls):
            return self


    # Method __get__ of class cached_property returns itself
    # if the object argument is None.
    ad = cached_property(lambda x: x)
    ae = cached_property(lambda x: x)
    assert ad.__get__(None, DummyObject) == ad
    assert ae.__get__(None, DummyObject) == ae
    assert ad == ae
    assert ad != DummyDescriptor()


    # Test of method __get__ of class cached_property
    # when the function being wrapped is not a coroutine function.

    # The patched instance method runs when __

# Generated at 2022-06-13 20:37:16.295216
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        @cached_property
        def x(self):
            return lambda: "x"

    instance = MyClass()
    assert isinstance(instance.x, asyncio.coroutines._CoroWrapper)
    assert instance.x() == "x"

# Generated at 2022-06-13 20:37:19.032923
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    assert MyClass().y == 6



# Generated at 2022-06-13 20:37:27.110963
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.pyutils import namedtuple
    from flutils.timeutils import now
    from flutils.decorators import cached_property

    Person = namedtuple('Person', ['spouse', 'name', 'dob'])

    class Person2(Person):
        @cached_property
        def age(self):
            return int((now() - self.dob).total_seconds() / 365.25 / 24 / 60 / 60)

    p: Person2 = Person2(None, 'John Doe', datetime(2000, 1, 1))
    assert hasattr(p, 'age')



# Generated at 2022-06-13 20:37:46.550066
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Author:
        Patrick R. Schmid
    """

    import pytest

    class Test:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Test()

    assert obj.y == 6
    assert asyncio.iscoroutinefunction(obj.y._wrapper)

    with pytest.raises(AttributeError):
        obj.y.wait()

# Generated at 2022-06-13 20:37:50.065765
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Unit test for method __get__ of class cached_property."""
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    obj.x = 0
    assert obj.y == 1
    del obj.y
    assert obj.y == 1

# Generated at 2022-06-13 20:38:00.038092
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Test cached_property.__get__()
    """
    import unittest
    import inspect

    from unittest.mock import Mock

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class Test_cached_property_A(unittest.TestCase):
        """
        Test cached_property.__get__()
        """

        def setUp(self):
            self.obj = MyClass()

        def test_cached_property___get__A(self):

            # Setup
            exp_val = 6

            # Test
            val = self.obj.y

            # Verify
            self.assertEqual(val, exp_val)


# Generated at 2022-06-13 20:38:07.144995
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock

    obj = Mock()
    func = Mock()
    obj.__dict__ = {}
    obj.__dict__[func.__name__] = func
    cached_property(func).__get__(obj, None)
    assert obj.__dict__[func.__name__] == func

# Generated at 2022-06-13 20:38:10.987146
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached_property.__get__()"""
    import pytest
    foo = Foo()
    with pytest.raises(AttributeError) as excinfo:
        foo.y
    assert (
        str(excinfo.value) ==
        'Foo has no attribute y (from cached_property.__get__())'
    )


# Generated at 2022-06-13 20:38:20.945622
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # noinspection PyPep8Naming
    class X:
        def __init__(self):
            self.data = None

        @cached_property
        def x(self):
            if self.data:
                return self.data + 1
            raise Exception

    x = X()
    x.data = 5
    assert x.x == 6
    x.data = 'foo'
    assert (x.x, x.data) == (6, 'foo')

    del x.x
    assert 'x' not in x.__dict__
    x.data = 'foo'
    assert x.x == 'foo1'


# noinspection PyPep8Naming

# Generated at 2022-06-13 20:38:25.526891
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



# Generated at 2022-06-13 20:38:36.729011
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # type: () -> None
    """Unit test for method __get__ of class cached_property."""

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    y = obj.y
    assert y == 6

    # noinspection PyUnresolvedReferences
    assert id(y) == id(obj.y)
    obj.x = 6
    assert obj.y == 7
    del obj.y
    assert obj.y == 7
    return None


# Generated at 2022-06-13 20:38:42.389462
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


# Generated at 2022-06-13 20:38:47.961269
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    #. Create a class with a cached_property
    #. Create an instance of the class
    #. Assert that value of cached_property is calculated
    """
    from flutils.decorators import cached_property
    import random

    class Foo(object):

        def __init__(self):
            self._bar = None


# Generated at 2022-06-13 20:39:13.120435
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

# Generated at 2022-06-13 20:39:25.643171
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from types import FunctionType, MethodType, coroutine

    from flutils.decorators import cached_property

    class MyClass:

        def __init__(self, x: int) -> None:
            self._x = x

        @cached_property
        def y(self) -> int:
            return self._x + 1

        @cached_property
        async def z(self) -> int:
            await asyncio.sleep(0.25)
            return self._x + 2

    obj = MyClass(5)
    assert isinstance(obj.y, int)
    assert obj.y == 6
    assert isinstance(obj.z, coroutine)
    assert asyncio.iscoroutine(obj.z)

    obj_y = obj.__getattribute__('y')

# Generated at 2022-06-13 20:39:39.464599
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    def fib(n):
        return fib(n - 1) + fib(n - 2) if n > 1 else n

    class A(object):
        @cached_property
        def fib(self):
            return fib(10)

    a = A()
    # print(A.fib.__doc__)
    # print(a.fib.__doc__)
    assert a.fib == 55
    assert a.fib == 55

    def fib2(n):
        return fib2(n - 1) + fib2(n - 2) if n > 1 else n

    class B(object):
        @cached_property
        def fib2(self):
            return fib2(5)

    b = B()
    assert b.fib2 == 5
    assert b.fib2 == 5


# Generated at 2022-06-13 20:39:45.150134
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
    result = obj.y
    expected = 6
    assert result == expected


# Generated at 2022-06-13 20:39:54.418073
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from unittest.mock import MagicMock

    @cached_property
    def _mock(self):
        return 1

    class Mock:
        def __init__(self):
            self.x = 2

        mock = _mock

    obj = Mock()
    assert obj.mock == 1
    assert obj.__dict__ == {'x': 2, 'mock': 1}

    # Test that return value is always the same
    _mock.__get__ = MagicMock()

    obj.mock = 2
    assert obj.mock == 2
    assert _mock.__get__.call_count == 0



# Generated at 2022-06-13 20:40:03.937111
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class P:
        def __init__(self, x):
            self.x = x

        @cached_property
        def s(self):
            return self.x ** 2

    p = P(4)
    assert p.s == 16
    assert p.__dict__ == {'x': 4, 's': 16}
    p.x = -1
    assert p.s == 16
    assert p.__dict__ == {'x': -1, 's': 16}
    del p.s
    assert p.__dict__ == {'x': -1}
    assert p.s == 1
    assert p.__dict__ == {'x': -1, 's': 1}



# Generated at 2022-06-13 20:40:13.547498
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from flutils.decorators import cached_property

    class MyClass:
        @cached_property
        def foo(self):
            return 'test'

    class MyClass2(MyClass):
        """
        Test for when name is already stored as an attr
        """
        def __init__(self):
            self.foo = 'another test'

    obj = MyClass()
    assert obj.foo == 'test'
    assert isinstance(MyClass.foo, cached_property)
    assert isinstance(obj.foo, str)
    obj2 = MyClass2()
    assert obj2.foo == 'another test'



# Generated at 2022-06-13 20:40:21.491952
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


test_cached_property___get__()



# Generated at 2022-06-13 20:40:31.711926
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class B:
        def __init__(self, x):
            self.x = x

        def __repr__(self):
            return f'B({self.x})'

        @cached_property
        def foo(self):
            print(f'foo {self}')
            return self.x

    class C:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __repr__(self):
            return f'C({self.x}, {self.y})'

        def __getattr__(self, name):
            return getattr(self.x, name)

    b = B(5)
    print(b.foo)
    print(b.foo)
    print(b.foo)

    b2 = B(10)

# Generated at 2022-06-13 20:40:38.248436
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import mock
    from functools import partial

    # Create a decorator
    decorator = cached_property(partial(mock.Mock))

    # Create a class and instance
    instance = mock.Mock()
    instance.__dict__ = {'_attribute': mock.Mock()}

    # Create an attribute
    attribute = mock.Mock(__get__=mock.Mock())
    setattr(instance, '_attribute', attribute)

    # Test __get__
    decorator.__get__(instance)
    attribute.__get__.assert_called_once_with(instance, instance.__class__)

# Generated at 2022-06-13 20:41:27.473163
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import logging
    import unittest

    from flutils.logutils import BraceMessage as __

    logging.getLogger(__name__).addHandler(logging.NullHandler())

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        def z(self):
            from asyncio import sleep

            async def _coro():
                await sleep(.1)
                return self.x + 1

            return _coro()

    class Test(unittest.TestCase):
        def test__cached_property___get__(self):
            obj = MyClass()
            self.assertEqual(obj.y, 6)

# Generated at 2022-06-13 20:41:38.918093
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property."""

    from unittest.mock import MagicMock

    class CachedPropertyTestClass:

        # noinspection PyMissingOrEmptyDocstring
        @cached_property
        def method_under_test(self):
            return "Result of method_under_test"

    obj = CachedPropertyTestClass()

    assert obj.method_under_test == "Result of method_under_test"

    func = obj.method_under_test

    assert func == "Result of method_under_test"

    obj.method_under_test = "New value of method_under_test"

    assert obj.method_under_test == "New value of method_under_test"

    obj.method_under_test = MagicMock()

    assert obj.method_under_

# Generated at 2022-06-13 20:41:42.931546
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        @cached_property
        def my_property(self):
            return 1

    obj = MyClass()
    assert obj.my_property == 1
    assert obj.__dict__['my_property'] == 1

# Generated at 2022-06-13 20:41:48.926580
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


# Generated at 2022-06-13 20:41:59.072774
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    import pytest
    from asyncio import ensure_future
    from asyncio import futures

    class MyClass:

        def __init__(self):
            self.x = 5
            self.y = cached_property(self._y)

        @asyncio.coroutine
        def _y(self):
            return self.x + 1

    obj = MyClass()
    f = obj.y
    assert isinstance(f, futures.Future)
    assert obj.x == 5
    assert obj.__dict__ == {'x': 5, 'y': f}

    @asyncio.coroutine
    def test_task():
        return obj.y

    f2 = ensure_future(test_task())
    assert f is f2
    pytest.helpers.run_briefly(obj.loop)
    assert f

# Generated at 2022-06-13 20:42:04.349195
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D103
    from unittest import TestCase, main

    from collections import namedtuple

    class MyClass:

        def __init__(self):
            self.x = 0
            self.y = 5

        @cached_property
        def my_property(self):
            self.x += 1
            return self.x

    class TestCachedProperty(TestCase):

        def test__get__(self):
            obj = MyClass()
            obj.my_property
            obj.my_property
            obj.my_property
            del obj.my_property
            obj.my_property
            self.assertEqual(obj.x, 2)

    main()

# Generated at 2022-06-13 20:42:08.013992
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import Mock

    obj = Mock()
    obj.__dict__ = {'x': 5}

    def y(self):
        return self.x + 1

    args = (obj, 'cls')
    ret = cached_property.__get__(cached_property(y), *args)

    assert ret == 6



# Generated at 2022-06-13 20:42:18.652493
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test for cached_property.__get__() method.
    """

    class SomeClass:
        @cached_property
        def x(self):
            return "foo"

    assert SomeClass().x == "foo"

    @cached_property
    def x():
        return "foo"

    assert x == "foo"


###############################################################################
# Copyright (c) 2019, Kenneth Reitz
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:


# Generated at 2022-06-13 20:42:24.904751
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Test that property is set on instance

    # Set up test variables
    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Make object
    obj = TestClass()

    # Get property
    _ = obj.y

    # Verify
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:42:28.485190
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
    assert obj.y == 6

