

# Generated at 2022-06-14 13:01:46.689116
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    obj = ObjectDict()
    obj['a'] = 'abc'
    obj['c'] = 'xyz'
    print(obj.a)
    print(obj.c)
    print(obj.d)

test_ObjectDict___getattr__()


# Generated at 2022-06-14 13:01:51.387625
# Unit test for function import_object
def test_import_object():
    from tornado.escape import utf8
    assert import_object('tornado.escape') is tornado.escape
    assert import_object('tornado.escape.utf8') is utf8
    assert import_object('tornado') is tornado
    try:
        import_object('tornado.missing_module')
    except ImportError:
        pass
    else:
        assert False, "expected ImportError"



# Generated at 2022-06-14 13:02:00.856552
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import pytest
    from tornado.test.util import unittest


    class MyClass(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return MyClass

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return MyClass

        def initialize(self, a, b, c=1):
            self.a = a
            self.b = b
            self.c = c

    @gen.coroutine
    def test_config_args():
        # type: () -> None
        MyClass.configure(None, c=2)
        instance = MyClass(a=1, b=2)
        assert instance.a == 1
        assert instance.b == 2
       

# Generated at 2022-06-14 13:02:10.007104
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    import inspect
    import functools
    def test_function(a = 10, b = 40, c = 50):
        pass
    arg_replacer = ArgReplacer(test_function, 'b')

    valid = (
        ((10, 40, 50), {}),
        ((10,), {'b': 40}),
        ((), {'a': 10, 'b': 40}),
    )
    invalid = (
        ((10,), {},),
        ((), {'a': 10},),
        ((), {'c': 50},)
    )
    for args, kwargs in valid:
        args = list(args)
        kwargs = dict(kwargs)
        new_value_1 = 60
        new_value_2 = 70
        old_value_1, args, kwargs = arg

# Generated at 2022-06-14 13:02:11.189516
# Unit test for constructor of class ArgReplacer

# Generated at 2022-06-14 13:02:15.282865
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise TypeError
    except TypeError as e:
        assert errno_from_exception(e) is None
    try:
        raise OSError
    except OSError as e:
        assert errno_from_exception(e) == errno.ENOENT



# Generated at 2022-06-14 13:02:22.775604
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def func(a, b, c): pass
    r = ArgReplacer(func, "b")
    assert r.arg_pos == 1
    assert r.get_old_value((1, 2, 3), {}) == 2
    assert r.get_old_value((1, 2, 3), {}, default=4) == 2
    assert r.get_old_value((1, 3), {"b": 2}) == 2
    assert r.get_old_value((1, 3), {"b": 2}, default=4) == 2
    assert r.replace(4, (1, 2, 3), {}) == (2, (1, 4, 3), {})
    assert r.replace(4, (1, 2, 3), {"b": 2}) == (2, (1, 4, 3), {})
    assert r.replace

# Generated at 2022-06-14 13:02:33.935106
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    _, args, kwargs = ArgReplacer(test_ArgReplacer_replace, "a").replace(
        100, (a, b, c), {"d": d, "e": e, "f": f}
    )
    assert a == 100
    assert args == (a, b, c)
    assert kwargs == {"d": d, "e": e, "f": f}

    _, args, kwargs = ArgReplacer(test_ArgReplacer_replace, "b").replace(
        200, (a, b, c), {"d": d, "e": e, "f": f}
    )
    assert b == 200
    assert args == (a, b, c)

# Generated at 2022-06-14 13:02:43.717563
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():

    from unittest import TestCase, mock

    @add_metaclass(ConfigurableMeta)
    class Base(object):

        def __init__(self, *args, **kwargs):
            """Initialize a `Base` subclass instance.

            Configurable classes should use `initialize` instead of `__init__`.
            """
            pass

        @classmethod
        def configurable_base(cls):
            """Returns the base class of a configurable hierarchy.

            This will normally return the class in which it is defined
            (which is *not* necessarily the same as the ``cls`` classmethod
            parameter).

            """
            return cls

        @classmethod
        def configurable_default(cls):
            """Returns the implementation class to be used if none is
            configured.
            """
            return cls

    #

# Generated at 2022-06-14 13:02:48.391399
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(*args, **kwargs): pass
    arg_replacer = ArgReplacer(func, 'y')
    assert arg_replacer.replace('1', (1, 2, 3), {'y':'2','x': '3'}) == ('2', (1,2,3), {'y':'1','x':'3'})
# PUT YOUR TEST UNDER THIS LINE

# Q4.4

# Generated at 2022-06-14 13:03:06.833983
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(*args, **kwargs): return args, kwargs
    arg_replacer = ArgReplacer(func, 'test')
    args, kwargs = arg_replacer.replace('value', (2, 3), {'test': None})
    assert args == (2, 3)
    assert kwargs == {'test': 'value'}

    args, kwargs = arg_replacer.replace('value', (2, 3, 'test'), {'test': None})
    assert args == (2, 3, 'value')
    assert kwargs == {}

    args, kwargs = arg_replacer.replace('value', (2, 3, 'test2'), {'test1': None})
    assert args == (2, 3, 'test2')

# Generated at 2022-06-14 13:03:14.178202
# Unit test for function raise_exc_info
def test_raise_exc_info():
    import io
    import sys

# Generated at 2022-06-14 13:03:27.171399
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class A(Configurable):
        def initialize(self, w, x=None, y=0, z=0.0):
            # type: (str, Optional[str], int, float) -> None
            self.w = w
            self.x = x
            self.y = y
            self.z = z

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[A]
            return A

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[A]
            return A

    a = A("w1")
    assert a.w == "w1"
    assert a.x is None
    assert a.y == 0
    assert a.z == 0.0

# Generated at 2022-06-14 13:03:37.571073
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func1(a,b,c,d):
        return a + b + c + d
    def func2(a,b,c,d=1):
        return a + b + c + d
    def func3(a,b=1,c=2,d=3):
        return a + b + c + d
    def func4(*args):
        sum = 0
        for i in args:
            sum = sum + i
        return sum
    def func5(a=1,*args):
        sum = a
        for i in args:
            sum = sum + i
        return sum
    def func6(a=1,b=2,*args):
        sum = a + b
        for i in args:
            sum = sum + i
        return sum

# Generated at 2022-06-14 13:03:47.427999
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class C(Configurable):
        @classmethod
        def configurable_base(cls):
            return C

        @classmethod
        def configurable_default(cls):
            return D


    class D(C):
        def initialize(self, a):
            self.a = a


    C().configure(None)
    assert isinstance(C()(), D)

    class E(C):
        def initialize(self, a):
            self.a = a


    C().configure(E)
    assert isinstance(C()(), E)



# Generated at 2022-06-14 13:03:56.744822
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import re

    class A(Configurable):
        @classmethod
        def configurable_default(cls):
            return A

        @classmethod
        def configurable_base(cls):
            return A

        def initialize(self, a, b=0):
            self.a = a
            self.b = b

    class B(A):
        @classmethod
        def configurable_default(cls):
            return B

        def initialize(self, c, b=0):
            self.c = c
            super(B, self).initialize(c, b=b)

    A.configure(A, b=10)
    assert A(1).a == 1
    assert A(1).b == 10
    assert A(1, b=99).b == 99


# Generated at 2022-06-14 13:04:06.744447
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(x, y, z):
        return x, y, z

    arg_replacer = ArgReplacer(foo, 'z')
    assert arg_replacer.replace("new_z", ("x","y"), {}) == (None, ("x","y"), {"z":"new_z"})

    # Replace an argument that is not passed
    assert arg_replacer.replace("new_z", (), {}) == (None, (), {"z":"new_z"})

    # Replace an argument that was passed positionally
    assert arg_replacer.replace("new_z", ("x", "y", "z"), {}) == (
        "z",
        ("x", "y", "new_z"),
        {},
    )

    # Replace an argument that was passed by keyword

# Generated at 2022-06-14 13:04:16.933633
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Super(Configurable):
            def configurable_base(self):
                return Super
            def configurable_default(self):
                return Sub
            def initialize(self, x):
                self.x = x
                super(Super, self).initialize()
            def set_x(self, x):
                self.x = x
    class Sub(Super):
        pass
    class SubSub(Sub):
        pass
    Sub.configure(None)
    assert isinstance(Sub(), Sub)
    assert isinstance(Sub(x=3), Sub)
    assert isinstance(Sub(x=3).x, int)
    assert Sub(x=3).x == 3
    assert isinstance(SubSub(), Sub)
    assert isinstance(SubSub(x=3), Sub)

# Generated at 2022-06-14 13:04:21.741934
# Unit test for function raise_exc_info
def test_raise_exc_info():
    def inner(exc_info: Tuple[Optional[type], Optional[BaseException], Optional[TracebackType]]):
        try:
            raise_exc_info(exc_info)
        except ValueError as e:
            assert e.args[0] == "a"
            assert len(e.args) == 1
            raise
    try:
        inner((ValueError, ValueError("a"), None))
    except BaseException:
        pass



# Generated at 2022-06-14 13:04:27.158350
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def arg_function(self, a, b, c=None):
        pass
    args = ArgReplacer(arg_function, "c")
    old_value, new_args, new_kwargs = args.replace("d", [1, 2], {"c": None})
    print(old_value)
    print(new_args)
    print(new_kwargs)


# Generated at 2022-06-14 13:05:02.098079
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class MyClass(Configurable):
        def __init__(self, a, b=7, **kwargs):
            print(a, b, kwargs)

    MyClass(1)
    print()
    MyClass(1, 5)
    print()
    MyClass(5, a=5)


test_Configurable_initialize()


# Generated at 2022-06-14 13:05:14.559898
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.httpclient import AsyncHTTPClient

    # 1. Impl is a string
    try:
        Configurable.configure("some.missing.modulename")
        raise Exception("should have raised an ImportError")
    except ImportError:
        pass

    # 2. Impl is a subclass of Configurable
    old_impl = Configurable.configured_class()
    old_kwargs = Configurable.__impl_kwargs

    class Impl(Configurable):
        @classmethod
        def configurable_base(cls):
            return AsyncHTTPClient

        @classmethod
        def configurable_default(cls):
            return AsyncHTTPClient

        def initialize(self, *args, **kwargs):
            pass

    saved = Configurable._save_configuration()
    Configurable.configure(Impl)

# Generated at 2022-06-14 13:05:15.330097
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    pass



# Generated at 2022-06-14 13:05:26.050065
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from _pytest.monkeypatch import MonkeyPatch
    from typing import Any, Dict, Optional

    m = MonkeyPatch()
    m.setattr(tornado.util, 'import_object', lambda obj: obj)

    saved_class = None
    saved_kwargs = None

    class a(tornado.util.Configurable):
        @classmethod
        def configurable_base(cls):
            return a

        @classmethod
        def configurable_default(cls):
            return b

        @classmethod
        def configure(cls, impl, **kwargs):
            nonlocal saved_class
            nonlocal saved_kwargs
            saved_class = impl
            saved_kwargs = kwargs

        @classmethod
        def configure(cls, impl, **kwargs):
            nonlocal saved_class
            non

# Generated at 2022-06-14 13:05:29.274576
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func_contains_argument(a,b,c,d):
        pass
    assert not ArgReplacer(func_contains_argument, 'e').get_old_value([1,2,3,4], dict(), 5)



# Generated at 2022-06-14 13:05:37.480543
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a,b,c):
        pass

    argr = ArgReplacer(f, "a")
    old_value, args, kwargs = argr.replace(1, (0,1,2), {})
    assert old_value == 0
    assert args == (1,1,2)
    assert len(kwargs) == 0

    argr = ArgReplacer(f, "b")
    old_value, args, kwargs = argr.replace(1, (0,2), {})
    assert old_value == 2
    assert args == (0,1)
    assert len(kwargs) == 0

    argr = ArgReplacer(f, "c")
    old_value, args, kwargs = argr.replace(1, (0,1), {})
    assert old_value

# Generated at 2022-06-14 13:05:49.024088
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():

    def test_args_f1(arg1, arg2, arg3, arg4):
        pass

    def test_args_f2(arg1, arg2, arg3=None, arg4=None):
        pass

    def test_args_f3(arg1, arg2, *arg3):
        pass


# Generated at 2022-06-14 13:05:52.348050
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Config(Configurable):
        def configurable_base(self):
            return Config
        def configurable_default(self):
            return Config
        
    c = Config()
    assert isinstance(c,Config)


# Generated at 2022-06-14 13:05:59.036487
# Unit test for function errno_from_exception
def test_errno_from_exception():
    # type: () -> None
    try:
        raise Exception(None)
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        e = OSError()
        e.errno = 42
        raise e
    except OSError as e:
        assert errno_from_exception(e) == 42
    try:
        raise OSError(42)
    except OSError as e:
        assert errno_from_exception(e) == 42



# Generated at 2022-06-14 13:06:08.725266
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_func(a, b):
        pass

    a, b, c = (1, 2, 3)
    args = (a, b)
    kwargs = {'b': b, 'c': c}
    replacer = ArgReplacer(test_func, 'b')
    old_value = replacer.get_old_value(args, kwargs)
    replacer.replace(100, args, kwargs)
    assert old_value == b
    assert kwargs['b'] == 100
    assert kwargs['c'] == c

# Generated at 2022-06-14 13:06:55.486975
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    import random
    def test_func(a, b, c):
        return a, b, c
    assert(ArgReplacer(test_func, "a").replace(0, [1, 2, 3], {}) == (1, [0, 2, 3], {}))
    assert(ArgReplacer(test_func, "b").replace(0, [1, 2, 3], {}) == (2, [1, 0, 3], {}))
    assert(ArgReplacer(test_func, "c").replace(0, [1, 2, 3], {}) == (3, [1, 2, 0], {}))
    assert(ArgReplacer(test_func, "d").replace(0, [1, 2, 3], {}) == (None, [1, 2, 3], {"d":0}))

# Generated at 2022-06-14 13:07:05.956354
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b, c=1, *args, **kwargs): return a * b * c * len(args) * len(kwargs)

    ar = ArgReplacer(f, "c")
    assert ar.arg_pos == 2
    assert ar.replace(2, (1, 2, 3, 4, 5), {"d": 1}) == (3, (1, 2, 2, 4, 5), {"d": 1})
    ar = ArgReplacer(f, "d")
    assert ar.arg_pos is None
    assert ar.replace(2, (1, 2, 3, 4, 5), {"d": 1}) == (1, (1, 2, 3, 4, 5), {"d": 2})

# Generated at 2022-06-14 13:07:12.855986
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.web

    class Foo(Configurable):
        @classmethod
        def configurable_base(cls):
            return Foo

        @classmethod
        def configurable_default(cls):
            return Bar

        def initialize(self, x):
            self.x = x

    class Bar(Foo):
        def initialize(self, x):
            super(Bar, self).initialize(x)
            self.y = x * 2

    assert issubclass(Bar, Foo)
    assert not issubclass(Bar, tornado.web.RequestHandler)

    Foo.configure(Bar)
    f = Foo(5)
    assert isinstance(f, Bar)
    assert isinstance(f, Foo)
    assert not isinstance(f, tornado.web.RequestHandler)
    assert f.x == 5
   

# Generated at 2022-06-14 13:07:22.836281
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    from functools import partial

    def f(a, b, c=3, d=4):
        pass

    # check that a TypeError is raised for non-function argument.
    with pytest.raises(TypeError):
        ArgReplacer(object(), "b")
    # check that a ValueError is raised for non-function argument.
    with pytest.raises(ValueError):
        ArgReplacer(partial(f, 1), "e")

    # Use ArgReplacer to find a named argument
    ar: ArgReplacer
    ar = ArgReplacer(f, "b")
    assert ar.name == "b"
    assert ar.arg_pos == 1
    assert ar.get_old_value((0, 1, 2, 3, 4), {}) == 1

# Generated at 2022-06-14 13:07:26.927282
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # type: () -> None

    def f(a, b, c=None):
        pass

    target = ArgReplacer(f, "c")
    assert target.replace("foo", (1, 2), {}) == (None, (1, 2), {"c": "foo"})
    assert target.replace("foo", (1, 2, 3), {}) == (3, (1, 2, "foo"), {})
    assert target.replace("foo", (), {"c": 3}) == (3, (), {"c": "foo"})



# Generated at 2022-06-14 13:07:30.744615
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    w1 = WebSocketConnectionClosedException()
    w2 = WebSocketConnectionClosedException(404, 'not found')
    w3 = WebSocketConnectionClosedException(567, '')


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# Generated at 2022-06-14 13:07:38.999390
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    @ArgReplacer("x", "y")
    def f(x, y, z):
        return x, y, z

    # function f only has two positional arguments
    assert f(1, 2, 3) == (1, 2, 3)
    assert f.get_old_value((1, 2, 3), {}) == 2
    assert f.get_old_value((1, 2, 3), {"x": 10, "y": 2, "z": 3}) == 2



# Generated at 2022-06-14 13:07:51.155568
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    """
    This test case is manually written because the method initialize
    of class Configurable is not actually implemented in any class.
    """
    class TestConfigurable(Configurable):
        def initialize(self, a, b=1):
            self.a = a
            self.b = b

    class TestConfigurableSub(TestConfigurable):
        pass

    class TestConfigurableSubSub(TestConfigurableSub):
        pass

    # Unconfigured Configurable subclass
    tc1 = TestConfigurable(0)
    assert isinstance(tc1, TestConfigurable)
    assert isinstance(tc1, TestConfigurableSub)
    assert isinstance(tc1, TestConfigurableSubSub)

    assert tc1.a == 0
    assert tc1.b == 1

    # Unconfigured Configurable subclass with extra kwargs

# Generated at 2022-06-14 13:07:59.567961
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_func(parm1: str, parm2: str, parm3: str) -> None:
        pass
    a = ArgReplacer(test_func, "parm2")
    l = ["a", "b", "c"]
    d = {"parm3": "c"}
    old_value, args, kwargs = a.replace("b_new", l, d)
    assert old_value=="b"
    assert args == ["a", "b_new", "c"]
    assert kwargs == {"parm3": "c"}


# Generated at 2022-06-14 13:08:06.211504
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from unittest import TestCase, main
    import copy

    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return A

        def __init__(self, x, y=None):
            # This should never get called, so we just set some
            # attributes to make sure it doesn't.
            self.x = x
            self.y = y

        def initialize(self, x, y=None):
            # The purpose of this method is to test that it gets
            # called instead of __init__, so we just copy the arguments.
            self.x = x
            self.y = y

        def __eq__(self, other):
            if isinstance(other, A):
                return self

# Generated at 2022-06-14 13:09:13.121801
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    """A test to check that Configurable._initialize is not private"""
    from tornado.web import Application

    assert Application.initialize.__func__ is not Configurable._initialize.__func__



# Generated at 2022-06-14 13:09:25.200544
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class First(Configurable):
        """First class"""

        @classmethod
        def configurable_base(cls):
            return First

        @classmethod
        def configurable_default(cls):
            return First

        def initialize(self):
            self.name_ = 'First'
    
    class Second(Configurable):
        """Second class"""

        @classmethod
        def configurable_base(cls):
            return First

        @classmethod
        def configurable_default(cls):
            return Second

        def initialize(self):
            self.name_ = 'Second'
    
    # Test 1
    # Test 1.1
    first = First()
    assert first.name_ == 'First'
    # Test 1.2
    first.configure('tornado.util.Second')

# Generated at 2022-06-14 13:09:37.270815
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    # Prepare a test function with named arguments.
    def fun(a, b=2, *, c=3, d=4):
        pass
    # Retrieve the value for a positional argument.
    assert ArgReplacer(fun, 'a').get_old_value((1,), {}, default=0) == 1
    # Retrieve the value for a non-named argument.
    assert ArgReplacer(fun, 'b').get_old_value((), {}, default=0) == 2
    # Retrieve the value for a named argument.
    assert ArgReplacer(fun, 'c').get_old_value((), {}, default=0) == 3
    # Retrieve the default value for a named argument.
    assert ArgReplacer(fun, 'd').get_old_value((), {}, default=0) == 4
    # Ret

# Generated at 2022-06-14 13:09:45.294137
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.process

    def _test():
        if tornado.process.Subprocess.configured_class() is not tornado.process.Subprocess:
            raise AssertionError
        tornado.process.Subprocess.configure(None)
        if tornado.process.Subprocess.configured_class() is not tornado.process.Subprocess:
            raise AssertionError
        tornado.process.Subprocess.configure("tornado.process.Subprocess")
        if tornado.process.Subprocess.configured_class() is not tornado.process.Subprocess:
            raise AssertionError
        tornado.process.Subprocess.configure(None)
        if tornado.process.Subprocess.configured_class() is not tornado.process.Subprocess:
            raise AssertionError

# Generated at 2022-06-14 13:09:56.013358
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    """
    You need pytest for this test

    Usage:
    pytest util.py
    """
    import pytest

    class MyConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return MyConfigurable

        @classmethod
        def configurable_default(cls):
            return MyConfigurableImpl

        def initialize(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class MyConfigurableImpl(MyConfigurable):
        def initialize(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    args = (1, 2)
    kwargs = dict(a=1, b=2)
    impl = MyConfigurable(*args, **kwargs)


# Generated at 2022-06-14 13:10:06.356208
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a, b, c, d=5): pass
    # Test cases where function parameter is not specified
    replacer = ArgReplacer(f, 'c')
    args = (1,2,3)
    kwargs = {'d':4}
    default = -1
    assert replacer.get_old_value(args, kwargs, default) == 3
    assert replacer.get_old_value(args, {}, default) == default
    # Test cases where function parameter is specified as a function argument
    args = (1,2,3,4)
    kwargs = {}
    assert replacer.get_old_value(args, kwargs, default) == 3
    assert replacer.get_old_value(args, kwargs) == 3
    # Test cases where function parameter is specified as a

# Generated at 2022-06-14 13:10:19.164835
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Issue #146: cyclical import problem

    import tornado.gen  # type: ignore

    class A(Configurable):
        def configurable_base(self):
            return A

        def configurable_default(self):
            return B

    class B(Configurable):
        def configurable_base(self):
            return B

        def configurable_default(self):
            return C

    class C(Configurable):
        def configurable_base(self):
            return C

        def configurable_default(self):
            return A

    a = A()  # doesn't raise exception
    assert a.__class__ == C

    # Issue #793: make sure cyclical imports work.
    # Here we have a pair of classes A and B, where A is a subclass of B
    # and B is a subclass of A. When loaded

# Generated at 2022-06-14 13:10:24.951160
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError()
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise IOError(3)
    except Exception as e:
        assert errno_from_exception(e) == 3



# Generated at 2022-06-14 13:10:34.673868
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import numbers

    class ConcreteConfigurable(Configurable):
        def configurable_base(self):
            return ConcreteConfigurable

        def configurable_default(self):
            return ConcreteConfigurable

        def initialize(self, foo):
            self.foo = foo

    from tornado.platform.auto import AutoConfigurable as AutoConfigurable2

    assert issubclass(AutoConfigurable2, Configurable)

    ConcreteConfigurable.configure("tornado.util.AutoConfigurable")
    instance = ConcreteConfigurable("foo")
    assert isinstance(instance, AutoConfigurable2)

    ConcreteConfigurable.configure(ConcreteConfigurable, foo=2)
    # Check that the configuration specifies a default value.
    instance = ConcreteConfigurable("foo")
    assert isinstance(instance, ConcreteConfigurable)

# Generated at 2022-06-14 13:10:39.690694
# Unit test for function errno_from_exception
def test_errno_from_exception():  # pragma: no cover
    try:
        raise IOError
    except IOError as e:
        assert errno_from_exception(e) is None

    try:
        raise IOError(42, "Test")
    except IOError as e:
        assert errno_from_exception(e) == 42

    try:
        raise IOError("Test")
    except IOError as e:
        assert errno_from_exception(e) == "Test"

