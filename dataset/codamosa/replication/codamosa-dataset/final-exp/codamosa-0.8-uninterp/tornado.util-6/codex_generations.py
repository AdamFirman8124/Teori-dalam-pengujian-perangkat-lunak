

# Generated at 2022-06-14 13:01:58.127914
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # type: () -> None
    def func(a, b, c=3, d=4):
        pass

    def arg_is_replaced_correctly(name, value, expected_result):
        # type: (str, Any, Any) -> None
        a = ArgReplacer(func, name)
        args = (1, 2)
        kwargs = {"b": 1, "c": 2, "d": 3}
        _, args, kwargs = a.replace(value, args, kwargs)
        if a.arg_pos is not None:
            assert args[a.arg_pos] == expected_result
        else:
            assert kwargs[name] == expected_result


# Generated at 2022-06-14 13:02:06.787909
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Base(Configurable):
        def initialize(self, **kwargs):
            return super().initialize(**kwargs)

    class Sub(Base):
        def initialize(self, **kwargs):
            return super().initialize(**kwargs)

    class A(Sub):
        pass

    class B(Sub):
        pass

    a = A()
    assert isinstance(a, A)

    Sub.configure(impl=B)
    b = Sub()
    assert isinstance(b, B)

    Sub.configure(impl=None)
    with pytest.raises(ValueError):
        Sub()

    Sub.configure(impl=A)
    a = Sub()
    assert isinstance(a, A)


# Generated at 2022-06-14 13:02:12.851108
# Unit test for function import_object
def test_import_object():
    import sys
    assert import_object("sys") is sys
    assert import_object("sys.modules") is sys.modules

    with pytest.raises(ImportError):
        import_object("sys.nonexisting_module")

    with pytest.raises(ImportError):
        import_object("nonexisting_module")

    assert import_object("struct") is struct
    assert import_object("struct.Struct") is struct.Struct



# Generated at 2022-06-14 13:02:21.299049
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    # Simple case with positional arguments
    def func(a, b):
        pass

    r = ArgReplacer(func, "a")
    assert r.get_old_value((1, 2), {}) == 1
    assert r.replace(3, (1, 2), {}) == (1, (3, 2), {})

    # Non-existent argument
    assert r.get_old_value((1, 2), {}, 6) == 6
    assert r.replace(3, (1, 2), {}, 6) == (6, (3, 2), {})

    # Positional argument with defaults
    def func(a, b=4):
        pass

    r = ArgReplacer(func, "b")
    assert r.get_old_value((1,), {}) == 4

# Generated at 2022-06-14 13:02:33.019135
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(a, b, c):
        pass
    args = ['a', 'b', 'c']
    kwargs = {'c': 'c'}
    rep = ArgReplacer(foo, 'b')
    old_value, args, kwargs = rep.replace('d', args, kwargs)
    assert old_value == 'b'
    assert args == ['a', 'd', 'c']
    assert kwargs == {'c': 'c'}
    rep = ArgReplacer(foo, 'c')
    old_value, args, kwargs = rep.replace('e', args, kwargs)
    assert old_value == 'c'
    assert args == ['a', 'd', 'e']
    assert kwargs == {'c': 'c'}
    rep = ArgReplacer

# Generated at 2022-06-14 13:02:42.363554
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
  def test_func(arg1, arg2, arg3=3):
    pass
  replacer = ArgReplacer(test_func, "arg2")
  assert replacer.get_old_value((1, 2,), {}) == 2
  assert replacer.get_old_value((1, 2, 3), {}) == 2
  assert replacer.get_old_value((1, 2, 3), {"arg2": 4}) == 2
  assert replacer.get_old_value((1,), {"arg2": 2}) == 2
  assert replacer.get_old_value((1,), {"arg2": 2, "arg3": 3}) == 2
  assert replacer.get_old_value((1,), {}, 30) == 30


# Generated at 2022-06-14 13:02:44.878336
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class T(Configurable):
        def _initialize(self, name, x=None):
            self.name = name
            self.x = x

        def configurable_base(cls):
            return "T"

        def configurable_default(cls):
            return "T"

    T("bob")



# Generated at 2022-06-14 13:02:52.469852
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.ioloop
    c = tornado.ioloop.IOLoop.configured_class()
    assert isinstance(c(), tornado.ioloop.IOLoop)
    old_impl, old_kwargs = tornado.ioloop.IOLoop._save_configuration()
    old_impl2, old_kwargs2 = tornado.ioloop.IOLoop._save_configuration()
    assert old_impl is old_impl2
    assert old_kwargs is old_kwargs2

# Generated at 2022-06-14 13:03:03.494694
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    """Test Configurable.__new__.

    The Configurable constructor is a little unusual and we want to
    make sure it works in all the ways we expect it to.
    """

    class _Concrete(Configurable):
        @classmethod
        def configurable_base(cls):
            return _Concrete

        @classmethod
        def configurable_default(cls):
            return _Concrete

        def _initialize(self):
            self.args = None  # type: Optional[Tuple[int, ...]]
            self.kwargs = None  # type: Optional[Dict[str, str]]

        initialize = _initialize

    _Concrete.configure(None)

    instance = _Concrete(1, x=2)
    assert isinstance(instance, _Concrete)


# Generated at 2022-06-14 13:03:10.910059
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import numbers
    import splunk.clilib.cli_common.testlib.asserts as asserts
    import splunk.clilib.cli_common.testlib.tempdir as tempdir
    import typeguard
    #
    # write_scratch_test_file
    #
    # This function writes a test file that contains the
    # following class:
    #
    # from tornado.util import Configurable
    #
    # class TestConfigurable(Configurable):
    #     def initialize(self, name, **kwargs):
    #         self.name = name
    #         self.__dict__.update(kwargs)
    #
    #     @classmethod
    #     def configurable_base(cls):
    #         return TestConfigurable
    #
    #     @classmethod
    #     def configurable_

# Generated at 2022-06-14 13:03:26.914520
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Test(Configurable):
        @classmethod
        def configurable_base(cls):
            return Test
        @classmethod
        def configurable_default(cls):
            return Test

    Test.configure(None)

    t = Test(a = 'abc')
    assert t.a == 'abc', "Property 'a' of object 't' was not initialized."


# Generated at 2022-06-14 13:03:37.322642
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def add(a: int, b: int) -> int:
        return a + b
    replacer = ArgReplacer(add, 'a')
    old_value, args, kwargs = replacer.replace(None, (1,), {'b':2})
    assert args == (None,), args
    assert kwargs == {'b':2}, kwargs
    assert old_value == 1, old_value
    old_value, args, kwargs = replacer.replace(None, (), {'a':1, 'b':2})
    assert args == (), args
    assert kwargs == {'a': None, 'b':2}, kwargs
    assert old_value == 1, old_value

# Generated at 2022-06-14 13:03:39.834848
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    assert issubclass(Configurable, object)



# Generated at 2022-06-14 13:03:45.485856
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """Test case for method __new__ of class Configurable

    """
    cls = Configurable
    base = cls.configurable_base()
    args = [] # type: List
    kwargs = {} # type: Dict
    obj = cls.__new__(cls, *args, **kwargs)
    return obj



# Generated at 2022-06-14 13:03:55.612161
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.stack_context

    class Configurable_obj(Configurable):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

    Configurable_obj.configure(Configurable_obj, a=1, b=2)
    with tornado.stack_context.NullContext():
        obj = Configurable_obj(3, 4, c=5, d=6)
        assert obj.args == (3, 4)
        assert obj.kwargs == {"c": 5, "d": 6, "a": 1, "b": 2}



# Generated at 2022-06-14 13:04:00.852796
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(*args, **kwargs):
        pass

    foo1 = ArgReplacer(foo, 'a')
    try:
        foo1.get_old_value([], {}, 'default')
    except Exception as e:
        print(e)


# Generated at 2022-06-14 13:04:09.282789
# Unit test for function import_object
def test_import_object():
    # Because we can't use setUp in a generator, here is a test helper
    # to work around sys.modules contamination.
    mod_name = "tornado.test.util_test"
    mod_obj = object()
    old_mod = sys.modules.pop(mod_name, None)
    try:
        import_object(mod_name)
        raise Exception("import_object should have failed")
    except ImportError:
        pass

    sys.modules[mod_name] = mod_obj
    assert import_object(mod_name) is mod_obj

    import tornado.test
    sys.modules['tornado.test'] = mod_obj
    try:
        assert import_object("tornado.test.util_test") is mod_obj
    finally:
        del sys.modules['tornado.test']


# Generated at 2022-06-14 13:04:19.033214
# Unit test for function import_object
def test_import_object():
    # Ensure that functions imported by import_object are what we are expecting
    from tornado.escape import utf8, native_str
    assert import_object("tornado.escape.utf8") is utf8
    assert import_object("tornado.escape.native_str") is native_str
    # Ensure that the built-in exception ImportError is raised if the import fails
    try:
        import_object("tornado.escape.nonexistent_object")
        raise Exception("Expected ImportError")
    except ImportError:
        pass
    # Ensure that a module is returned if the name has no dots
    import json
    assert import_object("json") is json
    # Ensure that a relative import works
    from .escape import xhtml_escape
    assert import_object(".escape.xhtml_escape") is xhtml_escape
    # Ensure

# Generated at 2022-06-14 13:04:30.373721
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_func(arg_1, arg_2, arg_3 = 'default'):
        pass
    # Test cases

# Generated at 2022-06-14 13:04:36.737227
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test(a:int, b: int, c: int)->str:
        return "test passed"
    a, args, kwargs = ArgReplacer(test, 'b').replace(4, [1,2,3], {})
    result = test(*args, **kwargs)
    print(result)


# Generated at 2022-06-14 13:05:01.517118
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # pylint: disable=unused-variable
    ##########
    # PASS 1 #
    ##########
    class SubConfigurable(Configurable):
        def configurable_base(cls):
            return SubConfigurable

        def configurable_default(cls):
            return SubConfigurableDefault

    class SubConfigurableDefault(SubConfigurable):
        def _initialize(self):
            super(SubConfigurableDefault, self)._initialize()

    a = SubConfigurableDefault()
    # pylint: disable=no-member
    a.initialize()
    ##########
    # PASS 2 #
    ##########
    class SubConfigurableOverride(SubConfigurable):
        def _initialize(self):
            super(SubConfigurableOverride, self)._initialize()


# Generated at 2022-06-14 13:05:14.404974
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(w: str, x: str, y: str, z: str) -> None:
        pass

    args = ("w", "x", "y", "z")
    kwargs = {}
    arg = ArgReplacer(func, "w")
    old_value = arg.get_old_value(args, kwargs)
    assert old_value == "w"
    old_value = arg.get_old_value(args, kwargs, "error")
    assert old_value == "w"
    arg = ArgReplacer(func, "y")
    old_value = arg.get_old_value(args, kwargs)
    assert old_value == "y"
    old_value = arg.get_old_value(args, kwargs, "error")

# Generated at 2022-06-14 13:05:25.413713
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f1(a):
        return a
    def f2(a, b):
        return a, b
    def f3(a, b, c):
        return a, b, c
    def f4(a, b, c, d):
        return a, b, c, d
    def f5(a, b, c, d, e):
        return a, b, c, d, e
    def f6(a, b, c, d, e, f):
        return a, b, c, d, e, f
    def f7(a, b, c, d, e, f, g):
        return a, b, c, d, e, f, g
    def f8(a, b, c, d, e, f, g, h):
        return a, b, c, d

# Generated at 2022-06-14 13:05:33.587018
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(foo, bar=42):
        pass

    assert ArgReplacer(f, "foo").get_old_value((1,), {}) == 1
    assert ArgReplacer(f, "foo").get_old_value((), {}) is None
    assert ArgReplacer(f, "foo").get_old_value((), {}, default=3) == 3
    assert ArgReplacer(f, "bar").get_old_value((), {}) == 42
    assert ArgReplacer(f, "bar").get_old_value((), {}, default=3) == 42
    assert ArgReplacer(f, "bar").get_old_value((), {"bar": 2}) == 2


# Generated at 2022-06-14 13:05:40.283394
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Foo(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return Bar

    class Bar(Foo):
        def initialize(self, x):
            self.x = x

    Foo.configure(Bar)
    f = Foo(x=5)
    assert isinstance(f, Bar)
    assert f.x == 5



# Generated at 2022-06-14 13:05:51.719075
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def _cc(func, name, newValue, *args, **kwargs):
        func.argreplacer = ArgReplacer(func, name)
        oldValue, newArgs, newKwargs = func.argreplacer.replace(newValue, args, kwargs)
        return oldValue, newArgs, newKwargs

    def test_kwargs(func, name, newValue, *args, **kwargs):
        oldValue, newArgs, newKwargs = _cc(func, name, newValue, *args, **kwargs)
        assert newValue == newKwargs[name]
        assert kwargs == newKwargs
        return oldValue, newArgs, newKwargs

    def test_args_1(func, name, newValue, *args, **kwargs):
        oldValue, newArgs, new

# Generated at 2022-06-14 13:05:59.278240
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class Bar(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Bar]
            return cls

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Bar]
            return cls

    class Foo(Bar):
        ...

    class Baz(Bar):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Baz]
            return cls

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Baz]
            return cls

    class Qux(Foo):
        ...


# Generated at 2022-06-14 13:06:12.138018
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    print("Test START: Configurable.__new__")
    def test_Configurable_impl():
        class Foo(Configurable):
            @classmethod
            def configurable_base(cls):
                return Foo

            @classmethod
            def configurable_default(cls):
                return Bar

        class Bar(Foo):
            def initialize(self, a, b):
                self.ab = (a, b)

        class Baz(Foo):
            def initialize(self, a, b, c):
                self.abc = (a, b, c)

        Foo.configure(Bar, b=1)
        foo = Foo()
        assert isinstance(foo, Bar)
        assert foo.ab == (None, 1)

        Foo.configure(None)
        foo2 = Foo(4, b=5)


# Generated at 2022-06-14 13:06:15.130772
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    class Dict(ObjectDict):
        pass

    d = Dict()
    d['foo'] = 'bar'
    assert d['foo'] == 'bar'
    assert d.foo == 'bar'



# Generated at 2022-06-14 13:06:26.735167
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    def test_Configurable_initialize(self):
        import sys
        import logging

        configurable_kwargs = {"foo": "bar"}

        class DummyConfigurable(Configurable):
            def initialize(self, **kwargs):
                # check additional kwargs
                self.kwargs = kwargs.copy()
                self.kwargs.update({"initialize_called": True})

            @classmethod
            def configurable_base(cls):
                return DummyConfigurable

            @classmethod
            def configurable_default(cls):
                return DummyConfigurable

        DummyConfigurable.configure(impl=DummyConfigurable, **configurable_kwargs)

        # check that the instance has been initialized correctly
        dummy_configurable = DummyConfigurable()

# Generated at 2022-06-14 13:07:00.863474
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class base(Configurable):
        def configurable_base(self):
            return 'base'

        def configurable_default(self):
            return 'configurable_default'

    class my_class(base):
        def configurable_base(self):
            return base

        def configurable_default(self):
            return 'configurable_default'


    instance = my_class('instance')
    assert instance.__class__ == instance.configurable_default()
    assert instance.__class__ == my_class.configurable_default()
    assert instance.configurable_base() == my_class.configurable_base()

    my_class.configure('my_class')
    instance = my_class('instance')
    assert instance.__class__ == my_class
    assert instance.configurable_base() == base


# Generated at 2022-06-14 13:07:09.575853
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_func(a, b, c):
        pass
    arg_replacer = ArgReplacer(test_func, "a")
    assert(arg_replacer.get_old_value((1, 2, 3), {"a": "test"}, default="default") == "test")
    assert(arg_replacer.get_old_value((1, 2), {"a": "test"}, default="default") == "test")
    assert(arg_replacer.get_old_value((1,), {"a": "test"}, default="default") == "test")
    assert(arg_replacer.get_old_value((), {"a": "test"}, default="default") == "test")
    assert(arg_replacer.get_old_value((1, 2, 3), {}, default="default") == 1)

# Generated at 2022-06-14 13:07:14.881373
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    #type: () -> None
    def test_method(self, a, b, c, d):
        pass

    class TestClass(object):
        test_method = test_method

    # Test that missing args return the default.
    assert ArgReplacer(test_method, "x").get_old_value((1, 2, 3), {}) is None

    # Test that args can be retrieved.
    assert ArgReplacer(test_method, "a").get_old_value((1, 2, 3), {}) == 1
    assert ArgReplacer(test_method, "d").get_old_value((1, 2, 3), {}) == 3

    # Test that args can be replaced.

# Generated at 2022-06-14 13:07:25.933420
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from tornado.concurrent import Future
    from tornado.concurrent import TracebackFuture
    from tornado.escape import to_unicode
    from tornado.escape import utf8
    from tornado.gen import coroutine
    from tornado.httpclient import AsyncHTTPClient
    from tornado.httpclient import HTTPClient
    from tornado.httpclient import HTTPRequest
    from tornado.httputil import HTTPHeaders
    from tornado.httputil import split_host_and_port
    from tornado.httputil import _split_port
    from tornado.iostream import IOStream
    from tornado.iostream import SSLIOStream
    from tornado.locks import Event
    from tornado.locks import Semaphore
    from tornado.locks import Condition
    from tornado.locks import BoundedSemaphore
    from tornado.netutil import Resolver

# Generated at 2022-06-14 13:07:29.488033
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    obj = ObjectDict()
    obj.a = 'A'
    assert obj.a == 'A'
    try:
        obj.b  # pylint: disable=pointless-statement
        raise AssertionError
    except AttributeError:
        pass



# Generated at 2022-06-14 13:07:32.194146
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    assert False, "Test not implemented"



# Generated at 2022-06-14 13:07:44.087562
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class C(Configurable):
        def configurable_base(self):
            return self
        def configurable_default(self):
            return self
    class D(Configurable):
        def configurable_base(self):
            return C
        def configurable_default(self):
            return self

    # Test that ordinary instances work
    c = C(a=1, b=2)  # type: C
    x = c._initialize()  # type: ignore
    assert c.a == x.a
    assert c.b == x.b
    d = D(c=3, d=4)  # type: D
    y = d._initialize()  # type: ignore
    assert d.c == y.c
    assert d.d == y.d
    # Test that configuration works

# Generated at 2022-06-14 13:07:54.709782
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    # Test class hierarchical configurable

    class HierarchicalConfigurable(Configurable):

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return HierarchicalConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return HierarchicalConfigurable

        def initialize(self):
            # type: () -> None
            pass

    class ChildClass(HierarchicalConfigurable):

        def initialize(self):
            # type: () -> None
            pass

    class GrandChildClass(ChildClass):

        def initialize(self):
            # type: () -> None
            pass

    HierarchicalConfigurable.configure(ChildClass)

# Generated at 2022-06-14 13:08:04.130476
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def get_old_value_test(func, name, *args):
        replacer = ArgReplacer(func, name)
        return replacer.get_old_value(args, {})

    def add(x, y):
        return x + y

    assert get_old_value_test(add, "x", 1, 2) == 1
    assert get_old_value_test(add, "y", 1, 2) == 2
    assert get_old_value_test(add, "x", (1, 2)) == 1
    assert get_old_value_test(add, "x", 1, 2, 3) == 1
    assert get_old_value_test(add, "x", y=2, x=1) == 1

# Generated at 2022-06-14 13:08:15.242649
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    from types import FunctionType, MethodType, BuiltinMethodType
    class Base(Configurable):
        def configurable_base(self):
            return Base
        def configurable_default(self):
            return Base
    class A(Base):
        pass
    class B(Base):
        pass
    class C(Base):
        pass
    class D(Base):
        pass
    class ATestCase(unittest.TestCase):
        def test_init_A(self):
            Base.configure(A)
            C.configure(B)
            d = D()
            self.assertIsInstance(d,D)
            Base.configure(None)
            b = B()
            self.assertIsInstance(b,B)
            self.assertIsInstance(d,D)
    AT

# Generated at 2022-06-14 13:08:47.439630
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import pytest
    from unittest.mock import MagicMock

    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable

        def initialize(self, *args, **kwargs):
            return

    with pytest.raises(NotImplementedError):
        TestConfigurable.configurable_base()

    with pytest.raises(NotImplementedError):
        TestConfigurable.configurable_default()

    assert TestConfigurable.configured_class() == TestConfigurable

    TestConfigurable.configure("tornado.testing.gen_test.callback_test_case")
    assert TestConfigurable.configured_class() == TestConfigurable

    Test

# Generated at 2022-06-14 13:08:53.541848
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_function(arg1, arg2, arg3):
        pass
    arg_replacer = ArgReplacer(test_function, 'arg1')
    args = ('arg1', 'arg2', 'arg3')
    kwargs = dict()
    assert arg_replacer.get_old_value(args, kwargs) == arg_replacer.get_old_value(args, kwargs, 0)


# Generated at 2022-06-14 13:09:05.136517
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func_with_pos_arg(pos):
        pass
    def func_with_kwargs(**kwargs):
        pass
    def func_with_pos_and_kwargs(pos, **kwargs):
        pass
    def func_with_pos_kwargs_and_def_arg(pos, kwarg=None):
        pass
    def func_with_pos_and_kwargs_and_def_arg(pos, kwarg=None, **kwargs):
        pass
    def func_with_pos_kwargs_and_kwargs_default(pos, kwarg={}, **kwargs):
        pass
    def func_with_pos_and_kwargs_and_kwargs_default(
        pos, kwarg={}, **kwargs
    ):
        pass


# Generated at 2022-06-14 13:09:14.556582
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # type: () -> None
    import typing
    import inspect
    import functools

    def test_function(a : typing.Optional[int]) -> None:
        pass
    def test_method(self, a : typing.Optional[int]) -> None:
        pass
    def test_function_default(a : typing.Optional[int] = None) -> None:
        pass
    def test_method_default(self, a : typing.Optional[int] = None) -> None:
        pass
    def test_method_custom(self, a : typing.Optional[int] = None, *args: Any, **kwargs: Any) -> None:
        pass

    first_arg_replacer = ArgReplacer(test_function, "a")
    assert first_arg_replacer.get_old_value((1,), {})

# Generated at 2022-06-14 13:09:19.293051
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception(1)
    except Exception as e:
        assert errno_from_exception(e) == 1

    try:
        raise Exception()
    except Exception as e:
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:09:28.338116
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    # Unit test for method __new__ of class Configurable
    class TestConfigurable(Configurable):

        def initialize(self):
            print(self.__class__)

        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return __init__

    class TestConfigurable1(TestConfigurable):
        pass

    class TestConfigurable2(TestConfigurable):
        pass

    TestConfigurable.configure(TestConfigurable1)
    assert isinstance(TestConfigurable(), TestConfigurable1)
    TestConfigurable.configure(TestConfigurable2)
    assert isinstance(TestConfigurable(), TestConfigurable2)

    configured_class = TestConfigurable.configured_class()
    assert configured

# Generated at 2022-06-14 13:09:39.259211
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b, c=1, *args, **kwds):
        pass

    arg = ArgReplacer(f, "b")
    assert (
        arg.replace(10, [1, 2, 3], {"c": 4, "d": 5}) == (2, [1, 10, 3], {"c": 4, "d": 5})
    )
    assert arg.replace(10, (1, 2, 3), {"c": 4, "d": 5}) == (2, (1, 10, 3), {"c": 4, "d": 5})

# Generated at 2022-06-14 13:09:48.503229
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def f1(a, b, c):
        pass
    r = ArgReplacer(f1, "c")
    assert r.arg_pos == 2
    assert r.get_old_value((1, 2, 3), {}) == 3
    assert r.get_old_value((1,), {"c": 3}) == 3
    assert r.get_old_value((), {"c": 3}) == 3
    assert r.get_old_value((), {}) is None
    assert r.replace(4, (1, 2, 3), {}) == (3, (1, 2, 4), {})
    assert r.replace(4, (1,), {"c": 3}) == (3, (1,), {"c": 4})

# Generated at 2022-06-14 13:09:50.173582
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    with pytest.raises(AttributeError):
        ObjectDict()



# Generated at 2022-06-14 13:09:55.346466
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError
    except Exception as e:
        assert errno_from_exception(e) is None

    try:
        raise IOError(22, "dummy message")
    except Exception as e:
        assert errno_from_exception(e) == 22



# Generated at 2022-06-14 13:10:53.804595
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise OSError(0, "test errno_from_exception")
    except Exception as e:
        assert errno_from_exception(e) == 0

    try:
        raise IOError("test errno_from_exception")
    except Exception as e:
        assert errno_from_exception(e) == None

    try:
        raise IOError
    except Exception as e:
        assert errno_from_exception(e) == None



# Generated at 2022-06-14 13:11:04.083169
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from unittest import mock


    class C(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

        def __init__(self, arg):
            pass

    class D(C):
        pass

    class E(D):
        pass

    C.configure("tests.test_util.D")
    x = C(1)
    assert isinstance(x, D)
    assert not isinstance(x, E)

    C.configure("tests.test_util.E")
    x = C(1)
    assert not isinstance(x, D)
    assert isinstance(x, E)


# Generated at 2022-06-14 13:11:07.334416
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
	# import
	from types import CodeType
	from types import FunctionType
	import __main__

	# init

	# test
	obj = Configurable()
	assert isinstance(obj, Configurable)



# Generated at 2022-06-14 13:11:17.674120
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(self, x, y):
        pass

    ar = ArgReplacer(func, "x")
    a, b, c = (1, 2), {}, []
    assert ar.get_old_value(a, b) == 1
    assert ar.get_old_value(a, b, default=3) == 1
    assert ar.get_old_value([1], b, default=3) == 1
    assert ar.get_old_value(b, b, default=3) == 3

    ar2 = ArgReplacer(func, "z")
    a, b, c = (1, 2), {}, []
    assert ar2.get_old_value(a, b) == None
    assert ar2.get_old_value(a, b, default=3) == 3


# Generated at 2022-06-14 13:11:23.636060
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_func(a, b=0, c=1):
        return a, b, c

    test_arg_replacer = ArgReplacer(test_func, "b")
    assert test_arg_replacer.get_old_value((1, ), {}, 99) == 99
    assert test_arg_replacer.get_old_value((1, ), {"b": 2}, 99) == 2
    assert test_arg_replacer.get_old_value((1, ), {"c": 2}, 99) == 99
    assert test_arg_replacer.get_old_value((1, ), {"b": 2, "c": 3}, 99) == 2

# Generated at 2022-06-14 13:11:33.791899
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return A
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return A
        def _initialize(self):
            pass
        initialize = _initialize
    A.configure(impl=A, a=4)
    a = A(a=1)
    assert(a.a == 1)
    A.configure(impl=A, a=5)
    a = A(a=1)
    assert(a.a == 1)
    A.configure(impl=None)
    A.configure(impl=A, a=6)
    a = A(a=1)
    assert(a.a == 6)
    #

# Generated at 2022-06-14 13:11:42.441809
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(a, b=3, c=4):
        pass
    arg_replacer = ArgReplacer(foo, 'b')
    assert arg_replacer.get_old_value((1, 2, 3), {'c': 5}) == 2
    assert arg_replacer.get_old_value((1, 2, 3), {'c': 5}, default=10) == 2
    assert arg_replacer.get_old_value((1, 2, 3), {'c': 5}, default=10) == 2
    assert arg_replacer.get_old_value((1, 2, 3), {'c': 5}, default=10) == 2
