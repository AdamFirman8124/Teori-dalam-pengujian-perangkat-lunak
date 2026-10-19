

# Generated at 2022-06-13 20:32:44.661379
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:
        def __init__(self, val):
            self.val = val

        @cached_property
        def add(self):
            return self.val + 1

    test = Test(1)
    test.add()
    test.add()
    assert test.val == 1
    assert test.add == 2

    test = Test(2)
    test.add()
    test.add()
    assert test.val == 2
    assert test.add == 3



# Generated at 2022-06-13 20:32:50.681425
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    method = cached_property.__get__
    class Foo:
        pass

    obj = Foo()
    assert method(cached_property(lambda self: self.x), obj, Foo) is obj.x

    obj.x = 5
    assert method(cached_property(lambda self: self.x), obj, Foo) is obj.x


# Generated at 2022-06-13 20:32:54.089218
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
    y = obj.y
    assert y == 6



# Generated at 2022-06-13 20:32:59.799399
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
    assert obj.__dict__ == {'x': 5, 'y': 6}


# Generated at 2022-06-13 20:33:07.165885
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    t1 = Test(5)
    t2 = Test(6)

    assert t1.y == 6
    assert t2.y == 7



# Generated at 2022-06-13 20:33:12.734057
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Class1:  # noqa:P101

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    c = Class1(5)
    assert c.y == 6

    c = Class1(6)
    assert c.y == 7



# Generated at 2022-06-13 20:33:20.110567
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(5)
    assert obj.x == 5
    assert obj.y == 6
    assert obj.__dict__['y'] == 6



# Generated at 2022-06-13 20:33:20.697452
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    pass

# Generated at 2022-06-13 20:33:34.221692
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class TestCachedProperty(unittest.TestCase):

        def test_cached_property___get__(self):
            obj = MyClass()

            # Test class that has had a cached property
            self.assertEqual(getattr(obj, 'y'), 6)
            self.assertEqual(obj.__dict__['y'], 6)

            # Test class that has had a cached property removed
            del obj.__dict__['y']
            self.assertEqual(getattr(obj, 'y'), 6)
            self.assertEqual(obj.__dict__['y'], 6)

    unittest

# Generated at 2022-06-13 20:33:37.652077
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Verify __doc__ is present
    assert cached_property.__init__.__doc__ is not None



# Generated at 2022-06-13 20:33:48.056721
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Testing method __get__ of class cached_property."""

    # test the first time the property is accesed it is computed
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    # test the second time the property is accesed it is not computed
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.y == 6

    # test deleting the property causes it to be recomputed

# Generated at 2022-06-13 20:33:54.747470
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
    assert obj.y == 6


# Generated at 2022-06-13 20:34:01.866763
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class Test(object):

        def __init__(self, x=0):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 2

        @cached_property
        def z(self):
            return self.x + 3

    test = Test()
    assert test.x == 0
    test.x = 3
    assert test.x == 3
    assert test.y == 5
    test.x = 5
    assert test.z == 8
    assert test.z == 8
    assert test.y == 5


if __name__ == "__main__":
    test_cached_property___get__()

# Generated at 2022-06-13 20:34:10.130703
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class C(object):
        def __init__(self):
            self.called = 0

        @cached_property
        def x(self):
            self.called += 1
            return 1

    c = C()
    assert c.x == 1
    assert not c.called
    assert c.x == 1
    assert not c.called

    c.x = 2
    assert c.called
    assert c.x == 2

    del c.x
    assert c.called
    assert c.x == 1



# Generated at 2022-06-13 20:34:14.793078
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Foo:

        def __init__(self, val):
            self.val = val

        def _get(self):
            return self.val

        @cached_property
        def get(self):
            return self._get()

    foo = Foo("bar")
    assert foo.get == "bar"
    foo.val = "baz"
    assert foo.get == "bar"
    del foo.get
    assert foo.get == "baz"


# Generated at 2022-06-13 20:34:24.479786
# Unit test for method __get__ of class cached_property

# Generated at 2022-06-13 20:34:31.000488
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from flutils.decorators import cached_property as built_in


# Generated at 2022-06-13 20:34:38.316926
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class MockInstance(object):
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class TestCachedProperty(unittest.TestCase):
        def test_cached_property___get__(self):
            # Test a cached_property with a non-coroutine attribute
            obj = MockInstance()
            attrib = obj.y
            self.assertEqual(6, attrib)

    unittest.main(verbosity=2)

# Generated at 2022-06-13 20:34:45.266884
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import unittest

    class Test(unittest.TestCase):
        class Demo:
            def __init__(self, x):
                self.x = x

            @cached_property
            def y(self):
                return self.x + 1

        def test(self):
            demo = self.Demo(5)
            self.assertEqual(demo.y, 6)

    test = Test()
    test.test()


# Generated at 2022-06-13 20:34:52.597481
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from pytest import raises

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.y == 6
    assert obj.y == 6
    with raises(AttributeError):
        obj.__dict__['y'] = 10
        del obj.y
        obj.y
    assert obj.y == 6



# Generated at 2022-06-13 20:35:08.203921
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # from flutils.decorators import cached_property
    import sys

    class Foo(object):

        @cached_property
        def foo(self):
            """The foo property."""
            return 'foo'

    foo = Foo()
    cached_property_descriptor_1 = foo.foo
    foo.foo = 'bar'
    cached_property_descriptor_2 = foo.foo

    print('cached_property_descriptor_1:', cached_property_descriptor_1)
    print('cached_property_descriptor_2:', cached_property_descriptor_2)
    """
    cached_property_descriptor_1: foo
    cached_property_descriptor_2: bar
    """

    print(foo.__dict__)

# Generated at 2022-06-13 20:35:13.209261
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # noinspection PyUnresolvedReferences
    """
    Test cached_property.__get__

    :return: None
    """

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:35:19.510180
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    The ``__get__`` method of class :obj:`flutils.decorators.cached_property`

    """

    class MyClass:

        def __init__(self):
            self.x = 5

        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert obj.__dict__ == {'x': 5, 'y': 6}

# Generated at 2022-06-13 20:35:24.259149
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

# Generated at 2022-06-13 20:35:33.009797
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import asyncio

    class TestClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @cached_property
        async def z(self):
            return self.x + 2

    obj = TestClass()
    assert obj.y == 6
    assert obj.__dict__["y"] == 6

    asyncio.get_event_loop().run_until_complete(obj.z)
    assert obj.__dict__["z"].result() == 7


# Generated at 2022-06-13 20:35:40.882365
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Foo:

        def __init__(self):
            self.x = 5
            self.y = 42

        @cached_property
        def z(self):
            """My z property"""
            return self.x + 1

    foo = Foo()
    assert foo.z == 6
    assert Foo.z.__doc__ == 'My z property'
    foo.x = 6
    assert foo.z == 6
    del foo.z
    assert not hasattr(foo, 'z')
    foo.z
    assert foo.z == 7

# Generated at 2022-06-13 20:35:51.717540
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test cached_property.__get__"""

    from inspect import isfunction

    from flutils.decorators import cached_property

    # ---------------------
    # Setup
    # ---------------------
    class C:
        def __init__(self, value: int = 0) -> None:
            self.value = value

        @cached_property
        def y(self) -> int:
            return self.value

    # ---------------------
    # Run
    # ---------------------
    obj = C(5)
    value = obj.y

    # ---------------------
    # Verify
    # ---------------------
    assert value == 5
    assert obj.__dict__['y'] == 5

    # y should be a function
    assert isfunction(C.y)
    # noinspection PyProtectedMember

# Generated at 2022-06-13 20:35:59.945671
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import TestCase, main
    from unittest.mock import Mock

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class cached_propertyTestCase(TestCase):

        def test_cached_property___get__(self):
            obj = MyClass()
            self.assertEqual(
                obj.y,
                6
            )

    main()



# Generated at 2022-06-13 20:36:05.758655
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

    # noinspection PyUnusedLocal
    def check_attributes(obj):
        # noinspection PyUnresolvedReferences
        assert obj.x == 5
        # noinspection PyUnresolvedReferences
        assert obj.y == 6

    check_attributes(obj)

    obj.x = 10
    # OBJECT INSTANCE DICT STILL CONTAINS
    # {'y': 6}
    # noinspection PyUnresolvedReferences
    assert obj.y == 6


# Generated at 2022-06-13 20:36:17.381768
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class myclass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

        @asyncio.coroutine
        @cached_property
        def z(self):
            return self.x + 1

        def w(self):
            return self.x + 1

    obj = myclass()
    assert obj.y == 6
    assert obj.__dict__['y'] == 6
    assert obj.y == 6

    loop = asyncio.get_event_loop()
    # noinspection PyCallingNonCallable
    loop.run_until_complete(obj.z)
    assert obj.__dict__['z'] == 6
    assert obj.z == 6

    assert obj.w() == 6
    assert 'w'

# Generated at 2022-06-13 20:36:24.922754
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit tests for cached_property decorator.
    """

    class MyClass:
        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass(5)
    assert obj.y == 6
    assert obj.y == 6



# Generated at 2022-06-13 20:36:32.865324
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from flutils.decorators import cached_property as cprop

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class MyClass2:
        def __init__(self):
            self.x = 5

        @cprop
        def y(self):
            return self.x + 1

    obj = MyClass()
    obj2 = MyClass2()

    assert obj.y == obj2.y



# Generated at 2022-06-13 20:36:43.300323
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import TestCase
    from unittest.mock import patch

    class Foo:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    class Test__get__(TestCase):

        @patch.object(Foo, 'y')
        def test_when_obj_exists_set_key_and_return_value(self, mock_y):
            mock_y.__get__ = lambda x, y: (x.x + 1)
            mock_y.__name__ = 'y'
            foo = Foo()
            result = foo.y
            self.assertEqual(6, result)
            self.assertIn('y', foo.__dict__)

# Generated at 2022-06-13 20:36:46.946295
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    def t():
        print()
        obj = MyClass()
        print(obj.y)

    t()



# Generated at 2022-06-13 20:36:52.850024
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            #: int: class var
            self.x = 5

        #: int: class var
        @cached_property
        def y(self):
            """A coroutine function property."""
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    assert repr(obj.__dict__['y']) == '<Future pending>'
    assert obj.y.result() == 6
    assert obj.__dict__['y'].result() == 6
    assert obj.y.result() == 6

# Generated at 2022-06-13 20:37:04.063262
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from time import sleep

    class A:

        def __init__(self):
            self._a = None

        @cached_property
        def a(self):
            sleep(2.5)
            return 5

    a = A()

    # Set the property to its initial value and time it.
    s = time.perf_counter()
    b = a.a
    e = time.perf_counter()

    # Check that the initial value of a is correct and it took 2.5 seconds.
    assert a.a == b
    assert e - s >= 2.5

    # Check that getting a the second time returns the initial value and
    # it took less than 1 second.
    s = time.perf_counter()
    c = a.a
    e = time.perf_counter()
    assert c == b

# Generated at 2022-06-13 20:37:12.845550
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for  method __get__ of class cached_property."""

    from flutils.decorators import cached_property

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
    assert obj.y == 6
    obj.x = 10
    assert obj.y == 6 and obj.z == 7



# Generated at 2022-06-13 20:37:17.142394
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class Foo:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = Foo()
    obj.y
    assert obj.__dict__ == {"x": 5, "y": 6}

# Generated at 2022-06-13 20:37:21.665036
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    '''Test that the property decorates the correc class and attribute'''
    class _MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    my_obj = _MyClass()
    my_obj.y
    assert my_obj.__dict__['x'] == 5
    assert my_obj.__dict__['y'] == 6

# Generated at 2022-06-13 20:37:25.611582
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

# Generated at 2022-06-13 20:37:36.485186
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    #
    # Test simple callable
    #

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property.__get__(None, MyClass)
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6

    #
    # Test callable with default kwargs
    #

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property.__get__(None, MyClass)
        def y(self, x=5):
            return x + 1

    obj = MyClass()
    assert obj.y == 6

    #
    # Test callable with default kwargs and other kwargs
    #


# Generated at 2022-06-13 20:37:40.890854
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

# Generated at 2022-06-13 20:37:50.035399
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    # Test case: successful test (non-coroutine)
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()

    assert obj.y == 6

    # Test case: successful test (coroutine)
    async def async_func():
        return 10

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return async_func()

    obj = MyClass()

    # Running the coroutine at the decorator level
    assert obj.y == 10

    # ## Test case: Exception (not a coroutine)

    # def test_cached_property___get___exc

# Generated at 2022-06-13 20:37:56.717945
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Unit test for method __get__ of class cached_property
    """

    class MyClass:
        called = 0

        #: @cached_property
        @cached_property
        def a(self):
            MyClass.called += 1
            return 5

    obj = MyClass()
    assert MyClass.called == 0
    assert obj.a == 5
    assert MyClass.called == 1
    assert obj.a == 5
    assert MyClass.called == 1



# Generated at 2022-06-13 20:38:04.477840
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method __get__ of class cached_property
    """

    class C:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = C()
    obj.y
    assert obj.__dict__['y'] == 6
    # obj.y = 10 would raise an AttributeError as desired



# Generated at 2022-06-13 20:38:13.301617
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest
    from flutils.decorators import cached_property


    class C:
        def __init__(self):
            self.x = 5

        @cached_property
        def y_0(self):
            return self.x + 1

        @cached_property
        def y_1(self):
            yield self.x + 1

        @cached_property
        async def y_2(self):
            return self.x + 1

        @cached_property
        async def y_3(self):
            yield self.x + 1




    # Test of __get__ for cached_property when a regular function is decorated
    def test():
        c = C()
        y_0 = c.y_0
        assert y_0 == 6
        assert isinstance(y_0, int)

# Generated at 2022-06-13 20:38:22.419413
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    from flutils.decorators import cached_property
    from flutils.miscutils import get_random_string, get_random_bytes

    class TestCachedProperty:

        def __init__(self):
            self._x = get_random_string(32)

        @cached_property
        def x(self):
            return self._x

    obj = TestCachedProperty()

    # The first call to obj.x should return the value of _x
    assert obj.x == obj._x

    # Now _x has a new random value, so it should not equal obj.x
    obj._x = get_random_string(32)
    assert obj.x != obj._x

    # But, obj.x should still return the original value of _x
    assert obj.x == obj.__dict__['x']

    # A

# Generated at 2022-06-13 20:38:36.856247
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Create a class with a cached_property
    class Test_class:
        @cached_property
        def prop(self):
            return 4

    # Create a class with a cached_property with an async function
    class Test_class_async:
        @cached_property
        async def prop(self):
            return 4

    import pytest
    from flutils.decorators import cached_property

    # Test that method __get__ of class cached_property behaves properly
    # for Class Test_class when the cached_property is called for the first
    # time
    obj = Test_class()
    assert obj.prop == 4

    # Test that method __get__ of class cached_property behaves properly
    # for Class Test_class when the cached_property is called for the second
    # time (The value of the cached property should be the

# Generated at 2022-06-13 20:38:44.317588
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            print('running cached_property')
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6
    obj.x = 10
    assert obj.y == 6


# Generated at 2022-06-13 20:38:52.167507
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import random
    class mycls(object):
        @staticmethod
        def func(obj):
            return random.randint(1, 1000000)

    a = mycls()
    assert isinstance(a, mycls)
    assert isinstance(a.func, int)
    assert a.func == mycls.func(a)
    assert a.func == mycls.func(a)
    assert a.func == mycls.func(a)
    assert a.func == mycls.func(a)
    assert a.func == mycls.func(a)
    assert a.func == mycls.func(a)

# Generated at 2022-06-13 20:39:08.659304
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D103
    from unittest import mock
    from types import MethodType

    class Class:

        @cached_property
        def method(self):
            """Method docstring."""
            return "foobar"

    assert Class.method.__doc__ == "Method docstring."
    assert not Class.method.__name__ == "method"
    assert Class().method == "foobar"
    with mock.patch.object(Class, "method", autospec=True) as mock_method:
        mock_method.return_value = "foo"
        assert Class().method == "foo"

    # This is to ensure that the cached_property class is using
    # functools.wraps properly.
    assert isinstance(Class().method, MethodType)

# Generated at 2022-06-13 20:39:23.208816
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from flutils.decorators import cached_property
    from unittest.mock import patch

    class Test:
        def __init__(self):
            pass

        @property
        def property(self):
            return 5

        @cached_property
        def cached_property(self):
            return 6

    @patch.object(
        Test,
        "__dict__",
        {"property": property(lambda x: 5), "cached_property": cached_property(lambda x: 6)},
    )
    def _test_cached_property___get__(cls):
        assert not cls.__dict__["property"] == cls.property
        assert cls.__dict__["cached_property"] == cls.cached_property


# Generated at 2022-06-13 20:39:26.736194
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
    del obj.y  # Delete the existing cached property
    assert obj.y == 6



# Generated at 2022-06-13 20:39:40.011706
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    import pytest

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    def test_no_obj():
        cp = MyClass.y

        assert cp.__doc__ == 'x + 1'

    def test_with_obj():
        obj = MyClass()
        assert obj.y == 6

    def test_with_obj_again():
        obj = MyClass()
        assert obj.y == 6
        obj.x = 2
        assert obj.y == 6

    def test_del_obj_attr():
        obj = MyClass()
        assert obj.y == 6
        del obj.y
        assert obj.y == 7

    test_no_obj()
    test_with_obj

# Generated at 2022-06-13 20:39:52.369535
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():  # noqa: D202
    """Unit test for method __get__ of class cached_property.
    """

    class A:

        @cached_property
        def x(self):
            return [1, 2, 3]

        @cached_property
        def y(self):
            return self.x

        @cached_property
        async def z(self):
            return [4, 5, 6]

        @cached_property
        def w(self):
            return asyncio.ensure_future(self.z)

    # object A
    obj_a = A()

    # Test x
    assert obj_a.x == [1, 2, 3]

    # Change the value of x
    obj_a.x = 1

    # Test x, still equals 1 since it has been changed
    assert obj_a

# Generated at 2022-06-13 20:40:05.467325
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    # Simple use case for cached_property
    class Test:
        @cached_property
        def test_val(self):
            return 5

    # Test property exists and returns correct value
    t = Test()
    assert t.test_val == 5  # Test value
    assert isinstance(t.test_val, int)  # Test type
    assert Test.test_val.__doc__ == t.test_val.__doc__ == "test_val"  # Test __doc__

    # Test cache by changing value and seeing if new assignments work
    t.test_val = 6
    assert t.test_val == 6  # Test getter function is not called
    assert isinstance(t.test_val, int)  # Test type

    # Test reset by deleting cached value and trying assignment again
    del t.test_val
   

# Generated at 2022-06-13 20:40:15.913298
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    assert (
        repr(
            MyClass.y.__get__.__get__(MyClass.y, cached_property)(
                MyClass.y, MyClass
            )
        )
        == "<bound method cached_property.__get__ of <cached_property object at 0x7fbc4d4fce48>>"
    )
    assert (
        repr(MyClass.y.__get__(MyClass(), MyClass)) == "<bound method cached_property.__get__ of <cached_property object at 0x7fbc4d4fce48>>"
    )



# Generated at 2022-06-13 20:40:21.777065
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class myClass:

        def __init__(self, x):
            self.x = x

        @cached_property
        def y(self):
            return self.x + 1

    # noinspection PyUnusedLocal
    def t(x):
        obj = myClass(5)
        obj.y
        assert obj.y == obj.__dict__['y']
        assert obj.y == 6

    t(5)



# Generated at 2022-06-13 20:40:26.937306
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



# Generated at 2022-06-13 20:40:30.590930
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """Test for method `cached_property.__get__`

    """

    class MyClass:
        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:40:59.807234
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Method __get__ of class cached_property

    :return:
    """
    import pytest
    from flutils.decorators import cached_property

    class Test:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    capsys = pytest.importorskip("capsys")

    with capsys.disabled():
        assert Test().y == 6

    return



# Generated at 2022-06-13 20:41:05.805681
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class C:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    # Using C
    objc = C()
    assert objc.y == 6

    # Resetting cached value
    del objc.y
    assert objc.y == 6



# Generated at 2022-06-13 20:41:12.338405
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class SomeClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    a = SomeClass()

    # Base case
    assert a.y == 6

    # Check that the returned value is cached
    a.x = 10
    assert a.y == 6

    # Check that it is not implemented as a data descriptor
    assert SomeClass.y.__get__(a, SomeClass) == 6

    # Check that it is not implemented as a non-data descriptor
    assert SomeClass.y.__get__(None, SomeClass) == SomeClass.y

    # Check that the returned value is cached even when the object
    # does not have a __dict__
    del a.__dict__
    a.x = 100

# Generated at 2022-06-13 20:41:19.462993
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest.mock import patch, mock_open
    from asynctest import CoroutineMock
    from pathlib import Path
    import asyncio
    from flutils.decorators import cached_property

    class MyClass:
        @cached_property
        def value_of_x(self):
            return self.x

    obj = MyClass()
    obj.x = 5

    assert obj.value_of_x == 5

    obj.x = 10

    assert obj.value_of_x == 5

    # ########################################################################
    # Async
    # ########################################################################

    class MyClass:
        @cached_property
        async def value_of_x(self):
            return await self.x

    obj = MyClass()
    obj.x = CoroutineMock()
   

# Generated at 2022-06-13 20:41:24.224328
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:
        def __init__(self, value):
            self.value: int = value

        @cached_property
        def func(self):
            self.value += 1
            return self.value

    obj1 = MyClass(1)
    return


if __name__ == "__main__":  # pragma: no cover
    test_cached_property___get__()

# Generated at 2022-06-13 20:41:31.872748
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    from unittest import TestCase

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    testcase = TestCase()
    obj = MyClass()
    testcase.assertEqual(obj.y, 6)
    delattr(obj, 'y')
    testcase.assertEqual(obj.y, 6)


# Main
if __name__ == "__main__":
    test_cached_property___get__()

# Generated at 2022-06-13 20:41:34.840789
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """
    Unit test for method ``cached_property.__get__``.
    """

    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6



# Generated at 2022-06-13 20:41:40.094673
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    class MyClass:

        def __init__(self):
            self.x = 5

        @cached_property
        def y(self):
            return self.x + 1

    obj = MyClass()
    assert obj.y == 6, 'obj.y == 6'



# Generated at 2022-06-13 20:41:49.655209
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():
    """ Test that method __get__ of class cached_property returns:
        - the property if obj is None
        - the cached property if obj is not None
    """
    class MyClass:
        # This class is intentionally blank to simulate a class.
        pass

    def test_func(obj):
        return 2 * obj.x
    
    # Test that method __get__ of class cached_property returns the property if obj is None.
    prop = cached_property(test_func)
    assert prop is prop.__get__(None, MyClass)

    # Test that method __get__ of class cached_property returns the cached property if obj is not None.
    obj = MyClass()
    obj.x = 2

# Generated at 2022-06-13 20:41:59.273762
# Unit test for method __get__ of class cached_property
def test_cached_property___get__():

    # Given the following class
    class MyClass:

        def __init__(self, x):
            self.x = x

        @cached_property
        def f(self):
            return self.x + 1

    # When I create an instance of the class
    obj = MyClass(2)

    # Then the value of the attribute x
    obj.x
    # Should be 2
    assert obj.x == 2

    # And the value of the attribute f
    obj.f
    # Should be 3
    assert obj.f == 3

    # And the value of f
    obj.f
    # Should be 3
    assert obj.f == 3

    # And the value of the attribute x
    obj.x = 3
    # Should be 3
    assert obj.x == 3

    # And the value of f before deleting the