

# Generated at 2022-06-14 13:01:53.095469
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass


# Generated at 2022-06-14 13:02:02.243948
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    orig_async_cls = AsyncHTTPClient.configured_class()
    AsyncHTTPClient.configure(TestAsyncHTTPClient)
    self.assertTrue(isinstance(AsyncHTTPClient(), TestAsyncHTTPClient))
    AsyncHTTPClient.configure(orig_async_cls)
    self.assertTrue(isinstance(AsyncHTTPClient(), orig_async_cls))
    # test configurable with kwargs
    orig_httputil_cls = HTTPConnection.configured_class()
    HTTPConnection.configure(TestHTTPConnection, foo='bar')
    self.assertTrue(isinstance(HTTPConnection(), TestHTTPConnection))
    self.assertTrue(HTTPConnection().foo, 'bar')
    HTTPConnection.configure(orig_httputil_cls)

# Generated at 2022-06-14 13:02:07.278324
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """This test checks that type annotations are not lost for Configurable.__new__
    """

    assert Configurable.__new__.__annotations__ == {
        'cls': typing.Type['Configurable'],
        '*args': typing.Any,
        '**kwargs': typing.Any,
        'return': typing.Any,
    }



# Generated at 2022-06-14 13:02:13.626278
# Unit test for function import_object
def test_import_object():
    import tornado.escape
    assert import_object("tornado.escape") is tornado.escape
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8
    assert import_object("tornado") is tornado
    try:
        import_object("tornado.missing_module")
        assert False
    except ImportError:
        pass


_BYTE_MASK = (1 << 8) - 1
_VERSION_MASK = ~_BYTE_MASK



# Generated at 2022-06-14 13:02:24.501658
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class TestConfigurable(Configurable):
        __impl_class = None  # type: Optional[Type[Configurable]]
        __impl_kwargs = None  # type: Dict[str, Any]
        def __init__(self):
            B = type("B", (object, ), {})  # type: Type[Configurable]
            impl = self.configurable_default
            instance = super(Configurable, B).__new__(impl)
            # initialize vs __init__ chosen for compatibility with AsyncHTTPClient
            # singleton magic.  If we get rid of that we can switch to __init__
            # here too.
            instance.initialize()
            return instance

# Generated at 2022-06-14 13:02:31.731202
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # INITIALIZATION
    class A(Configurable):
        def configurable_base(self):
            return A
        def configurable_default(self):
            return A
        def initialize(self):
            pass

    class B(A):
        def initialize(self):
            pass

    A.configure(None)
    a = A()
    assert(a.__class__ == A)
    b = B()
    assert(b.__class__ == B)



# Generated at 2022-06-14 13:02:38.464427
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import pytest

    class TestClass(Configurable):
        def initialize(self, a, b, c, d=1, e=2, f=3):
            assert a == 10, "Value of a is not equal to 10"
            assert b == 20, "Value of b is not equal to 20"
            assert c == 30, "Value of c is not equal to 30"
            assert d == 1, "Value of d is not equal to 1"
            assert e == 2, "Value of e is not equal to 2"
            assert f == 3, "Value of f is not equal to 3"

    TestClass(10, 20, 30)

# Generated at 2022-06-14 13:02:43.139946
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Test(Configurable):
        @classmethod
        def configurable_base(self):
            return Test
        @classmethod
        def configurable_default(self):
            return Test
    t = Test()
    t.initialize()


# Generated at 2022-06-14 13:02:47.162322
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError(5)
    except Exception as e:
        assert e.errno == 5
        assert errno_from_exception(e) == 5

    try:
        raise IOError
    except Exception as e:
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:02:52.420239
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from tornado.ioloop import IOLoop

    class FakeIOLoop(IOLoop):

        initialize = IOLoop.initialize  # type: Callable[..., None]

    old_default = IOLoop.configured_class()
    try:
        IOLoop.configure(FakeIOLoop)
        saved = IOLoop.configured_class()._save_configuration()
        # This will call FakeIOLoop.initialize
        IOLoop._restore_configuration(saved)
    finally:
        IOLoop.configure(old_default)



# Generated at 2022-06-14 13:03:07.153938
# Unit test for function errno_from_exception
def test_errno_from_exception():
    e = OSError('error name')
    assert errno_from_exception(e) == None
    e = OSError('error name', OSError.errno)
    assert errno_from_exception(e) == OSError.errno


# Generated at 2022-06-14 13:03:08.147486
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    if hasattr(Configurable, 'initialize'):
        _test_Configurable_initialize()


# Generated at 2022-06-14 13:03:10.071572
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    print("Unit test for method __new__ of class Configurable")

# Generated at 2022-06-14 13:03:22.866452
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def unused(a, b=1, *c, d=2, **e):
        pass

    a = ArgReplacer(unused, "b")
    old_b = a.get_old_value([], {}, default=4)
    assert old_b == 4
    old_b = a.get_old_value([], {"b": 5}, default=4)
    assert old_b == 5
    old_b = a.get_old_value([5], {}, default=4)
    assert old_b == 5
    old_b = a.get_old_value([5], {"b": 6}, default=4)
    assert old_b == 5
    old_b = a.get_old_value([], {"b": 6}, default=4)
    assert old_b == 6



# Generated at 2022-06-14 13:03:34.999466
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    args = ["a", "b"]
    kwargs = {"c": 3}
    arg_replacer = ArgReplacer(lambda arg1, arg2, arg3=3: None, "arg2")
    old_value, new_args, new_kwargs = arg_replacer.replace("new_value", args, kwargs)
    assert old_value == "b"
    assert new_args == ["a", "new_value"]
    assert new_kwargs == {"c": 3}
    args = ["a"]
    kwargs = {"arg2": 2, "arg3": 3}
    old_value, new_args, new_kwargs = arg_replacer.replace("new_value", args, kwargs)
    assert old_value == 2
    assert new_args == ["a"]
    assert new_

# Generated at 2022-06-14 13:03:47.852485
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # setup
    class BaseConfigurable(Configurable):
        __impl_class = None  # type: Optional[Type[Configurable]]
        __impl_kwargs = None  # type: Dict[str, Any]

        def __new__(cls, *args: Any, **kwargs: Any) -> Any:
            base = cls.configurable_base()
            init_kwargs = {}  # type: Dict[str, Any]
            if cls is base:
                impl = cls.configured_class()
                if base.__impl_kwargs:
                    init_kwargs.update(base.__impl_kwargs)
            else:
                impl = cls
            init_kwargs.update(kwargs)

# Generated at 2022-06-14 13:03:57.037678
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import logging
    import warnings
    assert issubclass(logging.Logger, Configurable)
    assert logging.Logger.configurable_base() is logging.Logger
    assert logging.Logger.configurable_default() is logging.getLoggerClass()

    # Test that the default class can be instantiated and configured
    logger = logging.getLoggerClass()
    assert isinstance(logger(), logging.Logger)
    logging.setLoggerClass(logging.Logger)
    try:
        assert isinstance(logging.getLoggerClass()(), logging.Logger)
    finally:
        logging.setLoggerClass(logging.getLoggerClass())

    # Test that Logger is an instance of Logger
    assert isinstance(logging.Logger, logging.Logger)

    # A minimal impl class inher

# Generated at 2022-06-14 13:04:06.420236
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class DummyConfigurable(object):
        def __new__(cls, *args, **kwargs):
            # type: (Type[Configurable], Any, Any) -> Configurable
            return object.__new__(cls)

    class DummySubclass(DummyConfigurable):
        def initialize(self, *args, **kwargs):
            # type: (Any, Any) -> None
            pass

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[DummyConfigurable]
            return DummyConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[DummySubclass]
            return cls

    # This should not raise an error because of
    # https://github.com/python

# Generated at 2022-06-14 13:04:12.065506
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.ioloop import IOLoop
    from tornado.util import Configurable
    assert isinstance(IOLoop().__new__(IOLoop), IOLoop)
    assert Configurable.configure(IOLoop)
    assert isinstance(IOLoop().__new__(IOLoop), IOLoop)

# Generated at 2022-06-14 13:04:21.837933
# Unit test for function errno_from_exception
def test_errno_from_exception():
    Tests = [
        IOError("[Errno 11] Resource temporarily unavailable"),
        IOError("[Errno 2]"),
        IOError("[Errno 2"),
        IOError("[Errno]"),
        IOError("Errno]"),
        IOError(""),
        IOError(),
        IOError((2, ("error", " [Errno 2] error"))),
    ]
    for test in Tests:
        assert errno_from_exception(test) == 2
    # Check the errno attribute

# Generated at 2022-06-14 13:04:39.997525
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    foo = ObjectDict()
    assert foo.name == foo["name"]
    foo.name = 10
    assert foo.name == foo["name"]
    with pytest.raises(AttributeError):
        print(foo.bar)


# Generated at 2022-06-14 13:04:49.460539
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b="foo"):
        return a + b

    assert ArgReplacer(test_ArgReplacer_replace, "a").replace(1, (), {}) == (
        None,
        (),
        {"a": 1},
    )
    assert ArgReplacer(test_ArgReplacer_replace, "a").replace(1, (1,), {}) == (
        1,
        (1,),
        {},
    )
    assert ArgReplacer(test_ArgReplacer_replace, "a").replace(1, (), {"a": 2}) == (
        2,
        (),
        {"a": 1},
    )

# Generated at 2022-06-14 13:05:01.728448
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    def test_initialize(obj, *args, **kwargs):
        # type: (Configurable, Any, Any) -> Dict[str, Any]
        """
        I can't really figure out how to create a Configurable with custom arguments
         from within this test, so @initialize.setter is just going to have to do for now
        """
        @functools.wraps(obj.initialize)
        def new_initializer(*args, **kwargs):
            obj._initialize(*args, **kwargs)
            return kwargs
        obj.initialize = new_initializer
        return obj.initialize(*args, **kwargs)

    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls


# Generated at 2022-06-14 13:05:14.455577
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_func(a, b, c=None):
        pass

    def test_func_with_one_default(a=None, b=None):
        pass

    a = ArgReplacer(test_func, "a")
    assert(a.get_old_value((1, 2, 3), {}) == 1)
    assert(a.get_old_value((1, 2, 3), {}, default=None) == 1)
    assert(a.get_old_value((), {"a": 1}) == 1)
    assert(a.get_old_value((), {}) == None)
    assert(a.get_old_value((), {}, default=None) == None)
    assert(a.get_old_value((1, 2, 3), {"a": 1}) == 1)

# Generated at 2022-06-14 13:05:25.451580
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from abc import ABCMeta, abstractmethod  # type: ignore

    class TestConfigClass(Configurable):

        @classmethod
        def configurable_base(cls):
            return TestConfigClass

        @classmethod
        def configurable_default(cls):
            return TestConfigDefaultImpl

        @classmethod
        def test_method(cls, a: str, b: str) -> None:
            # type: (...) -> None
            """Test class method"""
            print(a, b)

        def test_instance_method(self, c: str, d: int):
            # type: (...) -> None
            """Test instance method"""
            print(c, d)


# Generated at 2022-06-14 13:05:30.767231
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> Any
    import io

    class MockConfiguredObject(Configurable):
        def __new__(cls, *args, **kwargs):
            assert cls is MockConfiguredObject
            return io.StringIO()

    mockConfiguredObject = MockConfiguredObject()
    assert isinstance(mockConfiguredObject, io.StringIO)
    assert isinstance(mockConfiguredObject, MockConfiguredObject)

# Generated at 2022-06-14 13:05:38.469295
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class DefaultFooBar(Configurable):
        def __init__(self):
            super(DefaultFooBar, self).__init__()
            self.foobar = 123

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return FooBar

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return DefaultFooBar

    class SomeFooBar(Configurable):
        def __init__(self, some_arg):
            super(SomeFooBar, self).__init__()
            self.some_arg = some_arg

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return

# Generated at 2022-06-14 13:05:49.957868
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    assert ObjectDict(a=2, b=4).a == 2
    assert ObjectDict(a=2, b=4).b == 4
    assert ObjectDict(a=2, b=4)["a"] == 2
    assert ObjectDict(a=2, b=4)["b"] == 4
    try:
        ObjectDict(a=2, b=4).d
        raise Exception("should have raised exception")
    except (AttributeError, KeyError):
        pass
    try:
        ObjectDict(a=2, b=4)["d"]
        raise Exception("should have raised exception")
    except (AttributeError, KeyError):
        pass
    assert repr(ObjectDict(a=2, b=4)) == '{a: 2, b: 4}'

# Generated at 2022-06-14 13:05:50.963635
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    pass



# Generated at 2022-06-14 13:05:52.807384
# Unit test for function import_object
def test_import_object():
    assert import_object("os.path") is os.path
    assert import_object("os") is os
    assert import_object("") is None


# Generated at 2022-06-14 13:06:14.115767
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    import textwrap
    import unittest
    import sys

    class Base(Configurable):
        # type: ClassVar[List[str]]
        args = []  # type: ClassVar[List[str]]

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Base]
            return cls

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Base]
            return Impl

        def initialize(self, a=None, b=None):
            # type: (Optional[str], Optional[str]) -> None
            self.a = a
            self.b = b
            self.__class__.args.append((a, b))

    class Impl(Base):
        pass


# Generated at 2022-06-14 13:06:21.770108
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MockConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            pass
        @classmethod
        def configurable_default(cls):
            pass
        def initialize(self, *args, **kwargs):
            pass
    # See comments on Type[Configurable] above.
    instance = typing.cast(Configurable,
        MockConfigurable()
    )
    assert isinstance(instance, Configurable)
    assert isinstance(instance, MockConfigurable)



# Generated at 2022-06-14 13:06:31.895122
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestClass(Configurable):
        def initialize(self, a, b, c=3, d=4, e=None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d
            self.e = e
    inst = TestClass(1, 2)
    assert inst.a == 1
    assert inst.b == 2
    assert inst.c == 3
    assert inst.d == 4
    assert inst.e == None
    inst = TestClass(1, 2, d=5, e=6)
    assert inst.a == 1
    assert inst.b == 2
    assert inst.c == 3
    assert inst.d == 5
    assert inst.e == 6



# Generated at 2022-06-14 13:06:39.057631
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.testing import AsyncTestCase, gen_test

    # Configurable subclass that takes a single argument to its
    # constructor.
    class Test(Configurable):
        @classmethod
        def configurable_base(cls):
            return Test

        @classmethod
        def configurable_default(cls):
            return Impl

        def initialize(self, value):
            self.value = value

        def method(self):
            return self.value

    class Impl(Test):
        pass

    # Configurable subclass with a configurable subclass.
    class Test2(Configurable):
        @classmethod
        def configurable_base(cls):
            return Test2

        @classmethod
        def configurable_default(cls):
            return Test2Impl

        def initialize(self, value):
            pass


# Generated at 2022-06-14 13:06:49.291953
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from threading import Thread
    from tornado.ioloop import IOLoop

    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return A

        def initialize(self):
            pass

    class B(A):
        pass

    class C(A):
        def initialize(self):
            pass

    class D(A):
        def initialize(self):
            pass

    # Magic attribute `_initialize` is used if implemented
    class E(A):
        def _initialize(self):
            pass

    a = A()
    assert a.__class__ == A

    A.configure("tests.util.test_util.B")
    b = A()
    assert b.__class__

# Generated at 2022-06-14 13:06:50.160067
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass



# Generated at 2022-06-14 13:07:00.495559
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest

    class TestClass(Configurable):
        @classmethod
        def configurable_base(cls) -> Any:
            return cls

        @classmethod
        def configurable_default(cls) -> Any:
            return cls

        def initialize(self, *args: Any, **kwargs: Any) -> None:
            self.__args = args
            self.__kwargs = kwargs

    class TestImpl(TestClass):
        pass

    class TestSubclass(TestImpl):
        pass

    class TestConfigurableTest(unittest.TestCase):
        def setUp(self) -> None:
            self.__old_impl = TestClass.configured_class()
            assert self.__old_impl is TestClass

        def tearDown(self) -> None:
            TestClass.config

# Generated at 2022-06-14 13:07:09.329355
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MyConfigurable(Configurable):
        def initialize(self, x, y=2):
            self.args = (x, y)

        @classmethod
        def configurable_base(cls):
            return MyConfigurable

        @classmethod
        def configurable_default(cls):
            return MyConfigurableImpl

    class MyConfigurableImpl(MyConfigurable):
        pass

    MyConfigurable.configure(None)
    assert isinstance(MyConfigurable(1), MyConfigurableImpl)
    assert isinstance(MyConfigurable(1, y=3), MyConfigurableImpl)
    assert MyConfigurable(1).args == (1, 2)

    class MyUnrelatedConfigurable(Configurable):
        def initialize(self, a, b, c):
            pass


# Generated at 2022-06-14 13:07:14.506003
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b='b'):
        return a, b

    arg = ArgReplacer(f, 'b')
    old_value, args, kwargs = arg.replace('new_value', ('a', ), {})
    assert (old_value, args, kwargs) == ('b', ('a', ), {'b': 'new_value'})


# Generated at 2022-06-14 13:07:17.496305
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    try:
        Configurable()._initialize()
        Configurable()._initialize(0)
        Configurable()._initialize(1, 2)
    except NotImplementedError:
        pass



# Generated at 2022-06-14 13:07:43.137903
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from tornado.web import HTTPError
    print('start')
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        #@classmethod
        #def configurable_default(cls):
        #    return TestConfigurable

    class TestConfigurableB(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable


    def test1():
        TestConfigurable.configure(None)
        t = TestConfigurable()
        t.initialize('1', '2')

    def test2():
        TestConfigurable.configure(TestConfigurableB, a='1', b='2')
        t = TestConfig

# Generated at 2022-06-14 13:07:48.022276
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Foo(Configurable):
        def initialize(self, name):
            self.name = name

    f=Foo()
    f.initialize("name")
    print(f.name)


test_Configurable_initialize()


# Generated at 2022-06-14 13:07:59.201151
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Subclass(Configurable):
        @classmethod
        def configurable_base(cls):
            return Subclass

        @classmethod
        def configurable_default(cls):
            return Subclass

    class Impl(Subclass):
        def initialize(self, x, y, z=3):
            pass

    Subclass.configure(None)
    Subclass(x=1, y=2)
    Subclass(1, 2)
    Subclass(1, y=2)
    Subclass(x=1, y=2, z=4)
    try:
        Subclass(1, y=2, z=4)
    except TypeError:
        pass
    else:
        raise AssertionError("expected TypeError")
    Subclass.configure(Impl, z=3)

# Generated at 2022-06-14 13:08:05.909522
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import sys
    import os
    import re
    import json
    import logging
    import functools
    import collections
    import base64
    import urllib.parse
    import traceback
    import contextlib
    import threading
    import concurrent.futures
    import socket
    import ssl
    import typing
    import weakref
    import abc
    import pathlib
    import importlib.util
    import warnings
    import time
    import struct
    import copy
    import fcntl
    import itertools
    import selectors
    import subprocess
    import datetime
    import heapq
    import tempfile
    import random
    import typing
    from tornado import ioloop, options, web, escape, httputil, netutil, stack_context, locks, pipes, gen, concurrent, platform, simple

# Generated at 2022-06-14 13:08:14.301762
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MyConfigurable(Configurable):
        def initialize(self):
            pass
        @classmethod
        def configurable_base(cls):
            return MyConfigurable
        @classmethod
        def configurable_default(cls):
            return MyConfigurable
    c = MyConfigurable()
    assert isinstance(c, MyConfigurable)
    c = MyConfigurable()
    # assert_raises(ValueError, MyConfigurable.configure, None)
    # assert_raises(ValueError, MyConfigurable.configure, Dict)



# Generated at 2022-06-14 13:08:22.857249
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class MyClass(Configurable):
        def __init__(self, name, default='a'):
            self.name = name
            self.default = default

        def configurable_base(self):
            return MyClass

        def configurable_default(self):
            return MyClass

    a = MyClass(name='a')
    assert a.name=='a'
    assert a.default=='a'
    b = MyClass(name='b', default='b')
    assert b.name=='b'
    assert b.default=='b'
test_Configurable_initialize()


# Generated at 2022-06-14 13:08:26.754334
# Unit test for function import_object
def test_import_object():
    assert import_object("os.path") is os.path
    import tempfile
    assert import_object("tempfile") is tempfile
    assert import_object("tempfile.mkstemp") is tempfile.mkstemp
    with pytest.raises(ImportError):
        import_object("tempfile.nonexistent_function")



# Generated at 2022-06-14 13:08:35.079384
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable

        def _initialize(self):
            self.counter = 0

    TestConfigurable().counter = 1
    TestConfigurable.configure(None)
    TestConfigurable().counter = 2
    TestConfigurable.configure("tornado.util.Configurable")
    TestConfigurable().counter = 3



# Generated at 2022-06-14 13:08:44.087138
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Base(Configurable):
        def initialize(self, x):
            self.x = x

        @classmethod
        def configurable_base(cls):
            return Base

        @classmethod
        def configurable_default(cls):
            return Plain

    class Plain(Base):
        pass

    class WithArg(Base):
        def initialize(self, x, y):
            super(WithArg, self).initialize(x)
            self.y = y

    try:
        Base()
        assert False
    except Exception:
        pass

    Base.configure(None)
    assert isinstance(Base(), Plain)

    b = Base(42)
    assert isinstance(b, Plain)
    assert b.x == 42

    Base.configure(Plain, x=314)

# Generated at 2022-06-14 13:08:48.204125
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        def __init__(self, *args, **kwargs):
            super(TestConfigurable, self).__init__(*args, **kwargs)

    t = TestConfigurable()
    assert isinstance(t, TestConfigurable)


# Generated at 2022-06-14 13:09:27.218259
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Test Configurable.__new__ and Configurable.initialize

    class A:
        def __init__(self, x):
            self.x = x

        def f(self, y):
            return self.x + y

    class B(A):
        def g(self, y):
            return self.x + y

    class C:
        @staticmethod
        def initialize(self, x):
            self.x = x

        def f(self, y):
            return self.x + y

    class C1(C):
        pass

    class C2(C):
        pass

    # Basic single-level use
    c = C(5)
    c
    isinstance(c, C)
    c.f(6)

    # Configurable class with no configuration

# Generated at 2022-06-14 13:09:32.415523
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    objdict = ObjectDict(hello = "world")
    assert objdict.hello == "world"

    objdict["hello"] = "world"
    assert objdict.hello == "world"

    objdict.hello = "world"
    assert objdict.hello == "world"

# Generated at 2022-06-14 13:09:40.764167
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def configurable_base(self):
            return A

        def configurable_default(self):
            return A

    class B(A):
        def initialize(self):
            self.x = 1

    class C(B):
        def initialize(self, a=0):
            self.a = a
            self.y = 2
            super().initialize()

    assert isinstance(A(), A)
    assert isinstance(C(), A)
    assert A().x == 1
    assert C().a == 0
    assert C(a=3).a == 3
    assert C().x == 1
    assert C().y == 2

# Generated at 2022-06-14 13:09:49.330637
# Unit test for function import_object
def test_import_object():
    import os
    import tempfile
    import textwrap
    import types

    temp_file = tempfile.NamedTemporaryFile(mode="w",
                                            prefix="tornado_test_import_")
    temp_file.write(textwrap.dedent("""
        def f():
            return 5
        def g():
            return 6
        h = 7
    """))
    temp_file.flush()


# Generated at 2022-06-14 13:10:01.420901
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class T(Configurable):
        pass
    class T1(T):
        def initialize(self):
            print("initialize")
    class T2(T1):
        def initialize(self, x):
            super(T2, self).initialize()
            print(x)
    class T2a(T1):
        def initialize(self, x):
            super(T2a, self).initialize()
            print("T2a", x)
    class T2b(T2a):
        def initialize(self, x, y):
            T2a.initialize(self, x)
            print("T2b", y)
    class T3(T):
        def initialize(self, x, y=2):
            super(T3, self).initialize()
            print("T3", x, y)

# Generated at 2022-06-14 13:10:08.468844
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    d = {'d': 1}
    e = (1, 2)
    f = 3
    # new_value isn't in arguments, old_value will be None
    replaced = ArgReplacer(lambda a, b, c: None, 'c').replace(f, e, d)

    assert replaced[0] == None
    assert replaced[1] == e
    assert replaced[2] == {'c': f, 'd': 1}
    # new_value is in arguments, old_value will be the same with new_value
    replaced = ArgReplacer(lambda a, b, c: None, 'c').replace(1, e, d)

    assert replaced[0] == 1
    assert replaced[1] == (1, 2)
    assert replaced[2] == {'d': 1}



# Generated at 2022-06-14 13:10:17.050831
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class InheritedConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return InheritedConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return DerivedClass

    class DerivedClass(InheritedConfigurable):
        pass

    test_configurable = InheritedConfigurable()
    assert isinstance(test_configurable, DerivedClass)



# Generated at 2022-06-14 13:10:23.424522
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class FooConfigurableBase(Configurable):
        @classmethod
        def configurable_base(cls):
            return FooConfigurableBase

        @classmethod
        def configurable_default(cls):
            return None

    class FooConfigurable(FooConfigurableBase):
        @classmethod
        def configurable_base(cls):
            return FooConfigurableBase

        @classmethod
        def configurable_default(cls):
            return None

        def initialize(self, *args, **kwargs):
            pass

    # Calls Configurable.__new__
    # New object created
    obj = FooConfigurable()



# Generated at 2022-06-14 13:10:33.694795
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class ConfigurableClass(Configurable):
        def __init__(self, *args, **kwargs):
            self.__init_args = args
            self.__init_kwargs = kwargs
            self.initialize(*args, **kwargs)
        def initialize(self, *args, **kwargs):
            self.init_args = args
            self.init_kwargs = kwargs
        @classmethod
        def configurable_base(cls):
            return ConfigurableClass
        @classmethod
        def configurable_default(cls):
            return ConfigurableClass

    a = ConfigurableClass(1, b=2, c=3)
    assert a.init_args == (1,)
    assert a.init_kwargs == {'b': 2, 'c': 3}
    assert a.__init_

# Generated at 2022-06-14 13:10:42.358687
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import types
    import inspect
    _Configurable___new__ = Configurable.__new__
    class Test_Configurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return Test_Configurable
        @classmethod
        def configurable_default(cls):
            return Test_Configurable
        def initialize(self):
            pass
    def test_configuration(impl, *args, **kwargs):
        Test_Configurable.configure(impl)
        with pytest.raises(TypeError) as exc_info:
            _Configurable___new__(Test_Configurable, *args, **kwargs)
        err_msg = str(exc_info.value)
        exc_info.traceback = None