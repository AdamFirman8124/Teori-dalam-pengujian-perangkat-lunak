

# Generated at 2022-06-14 13:01:46.954453
# Unit test for function import_object
def test_import_object():
    import tornado.escape
    import tornado.httpserver
    assert import_object("tornado.escape") is tornado.escape
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8
    assert import_object("tornado") is tornado
    assert import_object("tornado.httpserver") is tornado.httpserver
    try:
        import_object("tornado.missing_module")
        assert False
    except ImportError:
        pass



# Generated at 2022-06-14 13:01:57.442719
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    from functools import wraps
    from typing import Callable

    # signature is "func(a, b=None, c=None, /, d=None, e='bar')"
    def func(a, b=None, c=None, *, d=None, e="bar"):
        pass

    def make_func(active_args: List[str]) -> Callable:
        """Returns a function with the given args actually used."""

        @wraps(func)
        def wrapper(*args, **kwargs):
            if "a" in active_args:
                assert args[0] is not None
                del args[0]
            if "b" in active_args:
                assert kwargs.pop("b")
            if "c" in active_args:
                assert kwargs.pop("c")

# Generated at 2022-06-14 13:02:02.938869
# Unit test for function import_object
def test_import_object():
    import sys
    import tornado.escape
    assert import_object("tornado.escape") is tornado.escape
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8
    assert import_object("tornado") is tornado
    assert import_object("sys") is sys
    try:
        import_object("tornado.missing_module")
    except ImportError:
        pass
    else:
        assert False, "expected ImportError"



# Generated at 2022-06-14 13:02:11.930576
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    base_class_name = "base_class_name"
    # Test a normal class
    TestClass = type(base_class_name, (object,), {})
    assert TestClass is not None
    TestClass_instance = TestClass()
    assert TestClass_instance is not None
    assert isinstance(TestClass_instance, TestClass)
    # Test a configurable class
    class TestConfigurable(Configurable):
        __impl_class = None
        __impl_kwargs = None
        def configurable_base(cls):
            return TestConfigurable
        def configurable_default(cls):
            return TestConfigurable
        @staticmethod
        def initialize(*args, **kwargs):
            pass
    assert TestConfigurable is not None
    TestConfigurable_instance = TestConfigurable()
    assert TestConfigurable_instance

# Generated at 2022-06-14 13:02:17.372025
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError
    except Exception as e:
        assert errno_from_exception(e) == 0

    try:
        raise IOError(42, 'foo')
    except Exception as e:
        assert errno_from_exception(e) == 42

    try:
        raise IOError('foo')
    except Exception as e:
        assert errno_from_exception(e) == 'foo'



# Generated at 2022-06-14 13:02:29.265914
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.ioloop import IOLoop
    from tornado.platform.auto import AutoIOLoop

    def bad_impl():
        # type: () -> Error
        class BadImpl(IOLoop):
            def initialize(self):
                pass

        return BadImpl

    def good_impl():
        # type: () -> IOLoop
        class GoodImpl(IOLoop):
            def initialize(self):
                pass

        return GoodImpl

    # By default, returns the type specified in configurable_default.
    IOLoop.configure(None)
    assert IOLoop() is AutoIOLoop()

    # Different IOLoop subclasses can be configured for different bases.
    IOLoop.configure(good_impl())
    assert IOLoop() is not AutoIOLoop()

    # The class must be a subclass of the

# Generated at 2022-06-14 13:02:34.751596
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception(22, "myexception")
    except Exception as e:
        assert errno_from_exception(e) == 22
    try:
        raise Exception(None)
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise Exception()
    except Exception as e:
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:02:40.262214
# Unit test for function raise_exc_info
def test_raise_exc_info():
    try:
        raise ValueError
    except:
        import sys
        etype, exc, tb = sys.exc_info()
        raise_exc_info((etype, exc, tb))

_reraise_exceptions = frozenset(
    [SyntaxError, ValueError, TypeError]
)  # type: Tuple[Type[Exception], ...]



# Generated at 2022-06-14 13:02:50.241162
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def foo(a, b):
        return (a, b)

    replacer = ArgReplacer(foo, 'b')
    assert replacer.name == 'b'
    assert replacer.arg_pos is None
    assert replacer.get_old_value(('a', 'b'), {}) is None
    assert replacer.get_old_value(('a', 'b'), {}, default=42) == 42
    assert replacer.get_old_value(('a', ), {'b': 'B'}) == 'B'
    assert replacer.get_old_value(('a', ), {}) is None
    assert replacer.get_old_value(('a', ), {}, default='default') == 'default'
    assert replacer.get_old_value(('a', 'b', 'c'), {}) is None

# Generated at 2022-06-14 13:03:02.417658
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import gc
    import os
    import socket
    import time
    import unittest
    from contextlib import contextmanager
    import errno
    import functools
    import threading
    import traceback
    from collections import deque, OrderedDict
    import ssl
    import random
    import string
    import warnings
    import stat
    import signal
    import types
    import sys
    import inspect
    import unittest
    import re
    import warnings
    import functools
    from datetime import datetime
    from contextlib import contextmanager
    from typing import Any
    from typing import Optional
    from typing import AsyncContextManager
    from typing import Callable
    from typing import TypeVar
    from typing import Generic
    from typing import Type
    from typing import Iterable
    from typing import Tuple
   

# Generated at 2022-06-14 13:03:14.635604
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Foo(Configurable):
        def initialize(self, a, b=1, c=2):
            self.initialize_args = (a, b, c)

    f = Foo(4, c=6)
    assert f.initialize_args == (4, 1, 6)



# Generated at 2022-06-14 13:03:17.577165
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    with pytest.raises(Exception):
        Configurable.__new__(object)

# Generated at 2022-06-14 13:03:28.965622
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(a, b, c, d, e='foo'):
        return a, b, c, d, e
    replacer = ArgReplacer(foo, 'e')
    assert replacer.get_old_value(('a', 'b', 'c', 'd',), {}, None), 'foo'
    assert replacer.get_old_value(('a', 'b', 'c', 'd',), {}, 'bar'), 'foo'
    assert replacer.get_old_value(('a', 'b', 'c', 'd',), {'e': 'bar'}, None), 'bar'
    assert replacer.get_old_value(('a', 'b', 'c', 'd',), {'e': 'bar'}, 'baz'), 'bar'

# Generated at 2022-06-14 13:03:38.707598
# Unit test for method replace of class ArgReplacer

# Generated at 2022-06-14 13:03:41.899839
# Unit test for function raise_exc_info
def test_raise_exc_info():
    # type: () -> None
    try:
        raise ValueError()
    except:
        raise_exc_info(sys.exc_info())



# Generated at 2022-06-14 13:03:49.128318
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class SubConfigurableTest(Configurable):
        pass
    #class ConfigurableTest(Configurable):
    #    @classmethod
    #    def configurable_base(cls):
    #        return ConfigurableTest
    #    @classmethod
    #    def configurable_default(cls):
    #        return SubConfigurableTest
    #    def _initialize(self, *args, **kwargs):
    #        pass
    #instance = ConfigurableTest()
    #instance.initialize()

# Generated at 2022-06-14 13:03:57.803907
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import asyncio
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A
        @classmethod
        def configurable_default(cls):
            return A_Impl1
        def __init__(self, *args, **kwargs):
            self.initialize(*args, **kwargs)
    class A_Impl1(A):
        def __init__(self, *args, **kwargs):
            super(A_Impl1, self).__init__(*args, **kwargs)
    class A_Impl2(A):
        def __init__(self, *args, **kwargs):
            super(A_Impl2, self).__init__(*args, **kwargs)
    a = A()
    assert type(a) is A_Impl1
    A

# Generated at 2022-06-14 13:04:04.163928
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MD(Configurable):
        @classmethod
        def configurable_base(cls):
            return MD

        @classmethod
        def configurable_default(cls):
            return MD

        def initialize(self, *arg, **kwargs):
            pass

    MD.configure('TODO')
    c = MD()
    assert c.__class__.__name__ == 'MD'

    with pytest.raises(TypeError):
        MD()


# Generated at 2022-06-14 13:04:11.308566
# Unit test for function import_object
def test_import_object():
    import tornado.escape
    assert import_object('tornado.escape') is tornado.escape
    assert import_object('tornado.escape.utf8') is tornado.escape.utf8
    assert import_object('tornado') is tornado
    try:
        import_object('tornado.missing_module')
        raise Exception('Expected exception')
    except ImportError:
        pass




# Generated at 2022-06-14 13:04:17.307412
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception(None, 9)
    except Exception as e:
        assert errno_from_exception(e) == 9
    try:
        raise Exception(9)
    except Exception as e:
        assert errno_from_exception(e) == 9
    try:
        raise Exception(None)
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise Exception()
    except Exception as e:
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:04:31.970285
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():

    import unittest

    class Handler(Configurable):

        def initialize(self):
            print("init")

        @classmethod
        def configurable_base(cls):
            return Handler

        @classmethod
        def configurable_default(cls):
            return Handler

    class HandlerSubclass(Handler):
        pass

    class HandlerSubclass2(Handler):
        pass

    class TestConfigurable(unittest.TestCase):

        def test_global_configuration(self):
            # test global configuration

            self.assertIs(Handler.configured_class(), Handler)
            self.assertIsInstance(Handler(), Handler)
            self.assertRaises(TypeError, HandlerSubclass)

            Handler.configure(HandlerSubclass)
            self.assertIs(Handler.configured_class(), HandlerSubclass)

# Generated at 2022-06-14 13:04:33.533858
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    assert True


# Generated at 2022-06-14 13:04:43.224983
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
        # type: () -> None
        #
        class TestConfigurable(Configurable):
            @classmethod
            def configurable_base(cls):
                # type: () -> Type[Configurable]
                return TestConfigurable

            @classmethod
            def configurable_default(cls):
                # type: () -> Type[Configurable]
                return TestConfigurable

            def initialize(self):
                # type: () -> None
                pass

        #
        TestConfigurableSubclass = TestConfigurable  # type: Any

        #
        class TestConfigurableSubclass(TestConfigurable):
            @classmethod
            def configurable_base(cls):
                # type: () -> Type[Configurable]
                return TestConfigurable


# Generated at 2022-06-14 13:04:49.007728
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c):
        pass

    args = (1, 2)
    kwargs = {"c": 3}

    new_value = 4
    replacer = ArgReplacer(func, "c")
    old_value, args, kwargs = replacer.replace(new_value, args, kwargs)
    assert old_value == 3
    assert args == (1, 2)
    assert kwargs == {"c": 4}



# Generated at 2022-06-14 13:05:01.354587
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b=4, c=5):
        assert False
    replacer = ArgReplacer(f, "b")
    print(replacer.get_old_value((1,), {}, 2))
    print(replacer.replace(2, (1,), {}))


if hasattr(itertools, "accumulate"):
    accumulate = itertools.accumulate
else:
    def accumulate(iterable: Iterable[T], func: Callable[[T, T], T] = operator.add) -> Iterator[T]:
        """Return running totals
        ``accumulate([1,2,3,4,5]) --> 1 3 6 10 15
        accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
        """
        # repeat, takewhile,

# Generated at 2022-06-14 13:05:14.194641
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(foo, bar, baz):
        pass
    replacer = ArgReplacer(func, "bar")
    assert replacer.get_old_value((1,2,3), None, None) == 2
    assert replacer.get_old_value((1,2), None, None) == 2
    assert replacer.get_old_value((1,2), {}, None) == 2
    assert replacer.get_old_value((1,2), {}, 3) == 2
    assert replacer.get_old_value((1,2), {'bar':11}, None) == 11
    assert replacer.get_old_value((1,2), {'bar':11}, 3) == 11
    assert replacer.get_old_value((1,2), {'bar':11}, None, 13) == 11


# Generated at 2022-06-14 13:05:25.267417
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b=None):
        return a, b

    replacer = ArgReplacer(f, "b")
    assert replacer.replace(5, (1,), {}) == (None, (1,), {"b": 5})
    assert replacer.replace(5, (), {"b": 2}) == (2, (), {"b": 5})
    assert replacer.replace(5, (1,), {"b": 2}) == (2, (1,), {"b": 5})
    assert replacer.replace(0, (), {"a": 1}) == (None, (), {"a": 1, "b": 0})
    # test the old_value functionality
    assert replacer.get_old_value((1,), {"b": 2}) == 2
    replacer.replace(5, (1,), {"b": 2})
   

# Generated at 2022-06-14 13:05:34.436878
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class A(Configurable):
        def __init__(self, *args, **kwargs):
            # type: (*Any, **Any) -> None
            self.args = args
            self.kwargs = kwargs
            self.initialize(*args, **kwargs)

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[A]
            return A

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[A]
            return A

    A.configure(None)

    a = A(1, foo=2)
    assert isinstance(a, A)
    assert a.args == (1,)
    assert a.kwargs == dict(foo=2)

# Generated at 2022-06-14 13:05:40.376180
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    # type: () -> None
    obj = ArgReplacer(test_ArgReplacer, "name")
    assert obj.arg_pos == 0
    assert obj.get_old_value(("e",), {}) == "e"
    assert obj.get_old_value((), {"name": "e"}) == "e"
    assert obj.get_old_value((), {"names": "e"}) is None


# Generated at 2022-06-14 13:05:47.739141
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Foo(Configurable):
        @classmethod
        def configurable_base(self):
            return self
        @classmethod
        def configurable_default(self):
            return self
        def initialize(self):
            pass
    # The true and false values of condition
    for the_input in [True, False]:
        # Check the type of returned value
        assert isinstance(Foo().initialize(), None)


# Generated at 2022-06-14 13:06:07.992956
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b=2, c=3):
        pass
    ArgReplacer_object = ArgReplacer(func, 'a')
    value = ArgReplacer_object.get_old_value((4,), {'b': 5}, default = None)
    assert value == 4
    value = ArgReplacer_object.get_old_value((), {'b': 5}, default = None)
    assert value == None


# Generated at 2022-06-14 13:06:17.451312
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    global __impl_class
    global __impl_kwargs

    __impl_class = None
    __impl_kwargs = None

    @add_metaclass(Configurable)
    class MyConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return MyConfigurable

        @classmethod
        def configurable_default(cls):
            return MyImpl

        def _initialize(self):
            pass

    class MyImpl(MyConfigurable):
        pass

    instance = MyConfigurable()
    assert isinstance(instance, MyImpl)
    assert instance.__class__ is MyImpl

    class MyImpl2(MyConfigurable):
        pass

    MyConfigurable.configure(MyImpl2)
    instance = MyConfigurable()
    assert isinstance(instance, MyImpl2)


# Generated at 2022-06-14 13:06:20.353435
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise ValueError
    except ValueError as e:
        assert errno_from_exception(e) is None
    try:
        raise ValueError(42)
    except ValueError as e:
        assert errno_from_exception(e) == 42



# Generated at 2022-06-14 13:06:32.144725
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func1(path):
        pass

    def func2(path, *args):
        pass

    def func3(path, *args, **kwargs):
        pass

    arg = ArgReplacer(func1, "path")
    assert None == arg.get_old_value(tuple(), {})

    arg = ArgReplacer(func2, "path")
    assert None == arg.get_old_value(tuple(), {})

    arg = ArgReplacer(func3, "path")
    assert None == arg.get_old_value(tuple(), {})

    arg = ArgReplacer(func1, "path")
    assert "path1" == arg.get_old_value(tuple(("path1",)), {})

    arg = ArgReplacer(func2, "path")
    assert "path1"

# Generated at 2022-06-14 13:06:34.718586
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    d = ObjectDict({'foo': 'bar'})
    assert d.foo == 'bar'
    assert d['foo'] == 'bar'
    assert getattr(d, 'foo') == 'bar'

# Generated at 2022-06-14 13:06:39.117205
# Unit test for function raise_exc_info
def test_raise_exc_info():
    # type: () -> None
    try:
        raise_exc_info((None, None, None))
    except TypeError:
        pass
    try:
        raise_exc_info((None, ZeroDivisionError(), None))
    except ZeroDivisionError:
        pass



# Generated at 2022-06-14 13:06:47.921619
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_func(arg1, arg2, arg3=None, arg4='default_string'):
        pass

    arg_replacer = ArgReplacer(test_func, 'arg1')
    # Test for arg that is not passed
    assert arg_replacer.get_old_value((1, 2), {}) is None
    # Test for arg that is passed in kwargs
    assert arg_replacer.get_old_value((1, 2), {'arg1': 'new_value'}) == 'new_value'
    # Test for arg that is passed as positional
    assert arg_replacer.get_old_value((1, 2), {'arg3': 'new_value'}) == 1


# Generated at 2022-06-14 13:06:53.678558
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(*args, **kwargs):
        return args, kwargs
    a = ArgReplacer(func, 'a')
    assert a.get_old_value((1,), {'b': 2}) == None
    assert a.get_old_value((1, 2, 3), {'b': 2}) == 2


# Generated at 2022-06-14 13:06:59.228217
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MyConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return MyConfigurable

        @classmethod
        def configurable_default(cls):
            return MyConfigurableImpl

        def do_my_thing(self, v):
            return "MyConfigurable.do_my_thing(%r)" % (v,)



# Generated at 2022-06-14 13:07:03.483619
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(arg1, arg2=None):
        return (arg1, arg2)

    print(ArgReplacer(func, 'arg1').replace('new_arg1', (1,), {}))
    print(ArgReplacer(func, 'arg2').replace('new_arg2', (1,), {}))



# Generated at 2022-06-14 13:07:18.754582
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            return Base

        @classmethod
        def configurable_default(cls):
            return Base

    class Subclass(Base):
        initialized = False

        def initialize(self):
            self.initialized = True

    instance = Subclass()
    assert instance.initialized

    class Subclass(Base):
        def initialize(self, value):
            self.value = value

    instance = Subclass(42)
    assert instance.value == 42



# Generated at 2022-06-14 13:07:29.084592
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class C_C(Configurable):
        @classmethod
        def configurable_base(cls):
            return C_C

        @classmethod
        def configurable_default(cls):
            return C_C_1

        def initialize(self, x):
            self.x = x

    class C_C_1(C_C):
        def initialize(self, x, y=1):
            super().initialize(x)
            self.y = y

    class C_C_2(C_C):
        def initialize(self, x, y=2):
            super().initialize(x)
            self.y = y

    assert C_C(1).x == 1
    assert C_C(1).y == 1
    assert C_C(1, y=2).y == 2
    assert C

# Generated at 2022-06-14 13:07:36.131069
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_args(
        a, b=12, c='test', d=[1, 2, 3], e: int=123, f='test', g: str='test', h=[1, 2, 3]
    ) -> List[int]:
        pass
    # Test when the argument is present in args, but with default value
    args = (1, 2, 3, 4)
    kwargs = {'b': 13, 'd': [4, 5], 'e': 456, 'g': 'test123'}
    assert ArgReplacer(func=test_args, name='c').get_old_value(args, kwargs) == 'test'
    # Test when the argument is present in args with a non-default value

# Generated at 2022-06-14 13:07:38.268341
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    dict = ObjectDict()
    dict['key'] = 'value'
    assert dict.key == 'value'



# Generated at 2022-06-14 13:07:50.491043
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    class TestArgReplacer(ArgReplacer):
        def __init__(self, func, name):
            super().__init__(func, name)
            if self.arg_pos is None:
                raise ValueError("ArgReplacer does not support keyword-only arguments.")

        def test(self, args, kwargs, new_value):
            return super().replace(new_value, args, kwargs)

    def test_func(a, b, c):
        pass

    arg_replacer = TestArgReplacer(test_func, 'a')
    assert arg_replacer.test((1, 2, 3), {}, 4) == (1, (4, 2, 3), {})

# Generated at 2022-06-14 13:08:01.380559
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return A

        def initialize(self):
            self.x = 1
    assert isinstance(A(), A)
    assert A().x == 1
    A.configure(None)
    assert A() is not A()
    assert A.configure is not Configurable.configure
    assert A.configured_class() is A
    assert A._save_configuration() == (None, None)
    A._restore_configuration((None, None))
    A.configure(None)
    assert not A._save_configuration()[0]
    assert A().x == 1
    save = A._save_configuration()

# Generated at 2022-06-14 13:08:13.504097
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    counter = 0
    class MyConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[MyConfigurable]
            return cls
        @classmethod
        def configurable_default(cls):
            # type: () -> Type[MyConfigurable]
            return cls
        def initialize(self):
            # type: () -> None
            nonlocal counter
            counter += 1
    instance = MyConfigurable()
    assert counter == 1
    instance = typing.cast(MyConfigurable, instance)
    instance = MyConfigurable()
    assert counter == 2
    MyConfigurable.configure(None)
    counter = 0
    MyConfigurable()
    assert counter == 1


# Generated at 2022-06-14 13:08:16.616616
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    cls = Configurable
    #impl = cls.__impl_class
    #assert impl.initialize
    #assert impl.configurable_base
    #assert impl.configurable_default
    #assert impl.configured_class


# Generated at 2022-06-14 13:08:22.860352
# Unit test for function import_object
def test_import_object():
    import tornado.escape
    assert import_object("tornado.escape") is tornado.escape
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8
    assert import_object("tornado") is tornado
    try:
        import_object("tornado.missing_module")
    except ImportError:
        pass
    else:  # noqa
        assert False, "expected ImportError"



# Generated at 2022-06-14 13:08:34.465326
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(first, second=None, third=None):
        return first, second, third

    first_arg = ArgReplacer(foo, "first")
    assert first_arg.replace("one", ("before",), {"second": "two", "third": "three"}) == (
        "before",
        ("one",),
        {"second": "two", "third": "three"},
    )

    second_arg = ArgReplacer(foo, "second")
    assert second_arg.replace("two", ("one",), {"third": "three"}) == (
        None,
        ("one",),
        {"third": "three", "second": "two"},
    )

    third_arg = ArgReplacer(foo, "third")

# Generated at 2022-06-14 13:08:53.048426
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.httpserver
    # original: https://github.com/tornadoweb/tornado/blob/master/tornado/test/util_test.py#L46
    class FooConfigurable(Configurable):
        def configurable_base(self):
            return FooConfigurable
        def configurable_default(self):
            return Foo
        def initialize(self):
            pass

    class BarConfigurable(Configurable):
        def configurable_base(self):
            return FooConfigurable
        def configurable_default(self):
            return Bar
        def initialize(self):
            pass

    class Foo(FooConfigurable):
        pass

    class Bar(BarConfigurable):
        pass

    # Make sure we pick up the superclass's configurable_base()
    class Baz(Bar):
        pass


# Generated at 2022-06-14 13:09:00.997633
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Base(Configurable):
        def initialize(self): pass

        def configurable_base(self): return Base

        def configurable_default(self): return Base

    # Check that Base() works before it is configured
    Base()

    # Check that Base() works after it is configured
    Base.configure(None)
    Base()

    # Check that Base(foo=1) works before it is configured
    Base(foo=1)

    # Check that Base(foo=1) works after it is configured (the keyword
    # argument should not be passed to the implementation class)
    Base.configure(None)
    Base(foo=1)

    # Check that Base.configure(Impl) works
    class Impl(Configurable):
        def initialize(self, bar, **kwargs): pass  # type: ignore


# Generated at 2022-06-14 13:09:03.302627
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Foo(Configurable):
        def initialize(self):
            self.foo = 1
    assert Foo().foo == 1


# Generated at 2022-06-14 13:09:13.781878
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    import unittest
    import tornado.util
    import inspect

    class ArgReplacerTest(unittest.TestCase):
        def setUp(self):
            # type: () -> None
            self.tests = []  # type: List[Tuple[Callable, Sequence[Any], Dict[str, Any], Any, Any]]
            for func in (self.try_arg, self.try_varargs, self.try_kwarg, self.try_var_kwargs):
                for arg_name in ("x", "y", "z"):
                    self.tests.append((func, [], dict(x=1, y=2, z=3), arg_name, None))
                    # All of our functions accept 1-3 args

# Generated at 2022-06-14 13:09:23.740232
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class C(Configurable):
       @classmethod
       def configurable_base(cls):
           return C

       @classmethod
       def configurable_default(cls):
           return C

       @classmethod
       def configure(cls, impl, **kwargs):
           pass

       @classmethod
       def configured_class(cls):
           pass

       @classmethod
       def _save_configuration(cls):
           pass

       @classmethod
       def _restore_configuration(cls, saved):
           pass

    c = C()
    c.initialize()

# Generated at 2022-06-14 13:09:24.310259
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass

# Generated at 2022-06-14 13:09:36.664870
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # type: () -> None
    class User(object):
        def __init__(self, name):
            self.name = name
    def get_user(name):
        return User(name)
    def get_none(*args, **kwargs):
        return None
    def get_user_no_arg():
        return User('arg_none')
    def get_user_arg(name):
        return User(name)
    def get_user_kwargs(name='arg_none'):
        return User(name)
    def get_user_args_kwargs(name='arg_none', age=10):
        return User(name)
    def get_user_args_kwargs_more(*args, **kwargs):
        return None

    # The arg to replace is passed by position

# Generated at 2022-06-14 13:09:40.106674
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a, b=None):
        pass

    args = (1, 2)
    kwargs = {'b': 3}
    arg = ArgReplacer(f, 'b')
    print(arg.get_old_value(args, kwargs))


# Generated at 2022-06-14 13:09:48.845790
# Unit test for method __getattr__ of class ObjectDict

# Generated at 2022-06-14 13:09:49.786036
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    pass
test_Configurable___new__()



# Generated at 2022-06-14 13:10:07.607180
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    impl = Configurable()
    with pytest.raises(NotImplementedError):
        impl.configurable_base()
    with pytest.raises(NotImplementedError):
        impl.configurable_default()
    with pytest.raises(NotImplementedError):
        impl._initialize()
    with pytest.raises(NotImplementedError):
        impl.configure(None, **object())
    impl.configure(impl, **object())
    with pytest.raises(ValueError):
        impl.configure(impl, **object())
    with pytest.raises(ValueError):
        impl.configure(impl, **object())
    with pytest.raises(ValueError):
        impl.configure(impl, **object())

# Generated at 2022-06-14 13:10:15.276905
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    arg_replacer = ArgReplacer(lambda x, y = 5: None, 'y')
    assert arg_replacer.get_old_value((1, ), dict(), None) == 5
    assert arg_replacer.get_old_value((1, ), dict(y=7), None) == 7
    assert arg_replacer.get_old_value((1, ), dict(y=7), 10) == 7



# Generated at 2022-06-14 13:10:23.625652
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class configurable_default_cls(Configurable):
        @classmethod
        def configurable_default(cls):
            return "configurable_default_cls"

        @classmethod
        def configurable_base(cls):
            return "configurable_base_cls"

    def test_case(impl, kwargs, result):
        configurable_default_cls.configure(impl, **kwargs)
        assert result == configurable_default_cls()

    test_case(impl=None, kwargs={"test": "configurable_default_cls"}, result="configurable_default_cls")
    test_case(impl="configurable_default_cls", kwargs={"test": "kwargs"}, result="configurable_default_cls")



# Generated at 2022-06-14 13:10:28.296336
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestClass(Configurable):
        def configurable_base(cls):
            return cls

        def configurable_default(cls):
            return cls

        def initialize(self):
            pass
    assert TestClass.configured_class() == TestClass
    assert TestClass.configure



# Generated at 2022-06-14 13:10:31.355557
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    o = ObjectDict()
    o.attr = "attr"
    o.key = "key"
    assert o.attr == o["attr"]
    assert o.key  == o["key"]


# Generated at 2022-06-14 13:10:38.540770
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class Temp(Configurable):
        def configurable_base(self):
            # type: () -> Type[Configurable]
            return Temp

        def configurable_default(self):
            # type: () -> Type[Configurable]
            return Temp

        def initialize(self):
            # type: () -> None
            pass

    Temp.configure(None, a=1)
    assert isinstance(Temp(), Temp)
    assert Temp.__impl_class is None
    assert Temp.__impl_kwargs == {"a": 1}

# Generated at 2022-06-14 13:10:49.408480
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Base:
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class Derived(Base, Configurable):
        @classmethod
        def configurable_base(cls):
            return Base

        @classmethod
        def configurable_default(cls):
            return Derived

        def initialize(self, *args, **kwargs):
            Base.__init__(self, *args, **kwargs)

    # Test that the class does not have a custom __new__ when no
    # configuration is set.
    assert Derived.__new__ is not Configurable.__new__

    # Test that a configured class does have a custom __new__ to
    # redirect to an implementation class.

# Generated at 2022-06-14 13:10:55.710616
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(*args, **kwargs):
        pass
    arg_replacer = ArgReplacer(func, "kwargs")
    old_value, args, kwargs = arg_replacer.replace({"replaced": True}, [], {})
    assert(old_value == None)
    assert(args == [])
    assert(kwargs == dict(kwargs={"replaced": True}))
    old_value, args, kwargs = arg_replacer.replace({"replaced": False}, [12], dict(kwargs={"replaced": True}))
    assert(old_value == {"replaced": True})
    assert(args == [12])
    assert(kwargs == {"replaced": False})



# Generated at 2022-06-14 13:11:04.296353
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(a, b):
        pass
    def foo1(a, b, c, d):
        pass
    arg_replacer_a = ArgReplacer(foo, 'a')
    arg_replacer_b = ArgReplacer(foo, 'b')
    arg_replacer_c = ArgReplacer(foo1, 'c')
    print(arg_replacer_a.get_old_value(('abcd', 'efgh'), dict()))
    print(arg_replacer_b.get_old_value(('abcd', 'efgh'), dict()))
    print(arg_replacer_c.get_old_value(('abcd', 'efgh', 'ijkl', 'mnop'), dict()))

# Generated at 2022-06-14 13:11:10.182227
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return A

        def __init__(self, a):
            # type: (int) -> None
            self.a = a

    a = A(1)  # type: ignore
    assert a.a == 1


# Generated at 2022-06-14 13:11:32.427357
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class C(Configurable):
        pass

    # Unconfigured
    assert issubclass(C, C.configurable_default())
    c = C()
    assert isinstance(c, C.configured_class())

    # Configured
    C.configure(object)
    c = C()
    assert isinstance(c, object)

    # subclass
    class D(C):
        pass
    assert issubclass(D, D.configurable_default())
    d = D()
    assert isinstance(d, D.configured_class())
    assert issubclass(d.__class__, D)
    assert issubclass(d.__class__, D.configured_class())

    # subclass
    class E(C):
        pass
    E.configure(str)
    e = E()
