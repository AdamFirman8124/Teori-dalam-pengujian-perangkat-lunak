

# Generated at 2022-06-14 13:01:40.284535
# Unit test for function import_object
def test_import_object():
    from unittest import mock
    orig_import = __import__
    try:
        __import__ = mock.Mock(side_effect=lambda *args:
                               "foo" if args[0] == "foo" else
                               orig_import(*args))
        assert import_object("foo") == "foo"
        assert import_object("foo.bar") == "foo"
        assert __import__.call_args_list == [
            mock.call("foo"),
            mock.call("foo.bar", fromlist=["bar"])]
    finally:
        __import__ = orig_import



# Generated at 2022-06-14 13:01:50.051813
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    from tornado.ioloop import IOLoop

    import sys
    from collections import namedtuple

    if sys.platform == "win32":
        from tornado import platform

        platform.impl = platform.WinsocketIOLoop  # type: ignore

        # type: ignore
        saved = namedtuple("saved", ("impl", "impl_kwargs"))(None, {})
        try:
            saved = (
                platform.impl,
                platform.__impl_kwargs,
            )
            platform.__impl_kwargs = {}
            sub_ioloop = IOLoop()
            assert isinstance(sub_ioloop, platform.WinsocketIOLoop)
        finally:
            platform.impl = saved.impl
            platform.__impl_kwargs = saved.impl_kwargs

# Generated at 2022-06-14 13:01:55.995497
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise Exception(42, "foo")
    except Exception as e:
        assert errno_from_exception(e) == 42
    try:
        raise Exception("foo")
    except Exception as e:
        assert errno_from_exception(e) == "foo"



# Generated at 2022-06-14 13:02:04.815298
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return A

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return A1

        def initialize(self, x: int, y: int = 0) -> None:
            self.x = x
            self.y = y

        def __repr__(self):
            # type: () -> str
            return "%s(x=%s, y=%s)" % (self.__class__.__name__, self.x, self.y)

    class A1(A):
        pass

    class A2(A):
        pass

    A.configure(None)

# Generated at 2022-06-14 13:02:13.536445
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b):
        pass
    ar = ArgReplacer(f, 'b')
    old, args, kwargs = ar.replace(10, [1, 2], {})
    assert args == [1, 10]
    assert kwargs == {}
    assert old == 2

    old, args, kwargs = ar.replace(20, [1], {'b': 2})
    assert args == [1]
    assert kwargs == {'b': 20}
    assert old == 2

    old, args, kwargs = ar.replace(20, [1], {})
    assert args == [1]
    assert kwargs == {'b': 20}
    assert old is None



# Generated at 2022-06-14 13:02:21.057096
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    import unittest
    import unittest.mock

    class Foo(Configurable):

        def initialize(self):
            print("initialize called")

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Foo

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return Foo

    f = Foo()
    with unittest.mock.patch("builtins.print") as mprint:
        mprint.return_value = None
        f.initialize()
        assert mprint.call_count == 1



# Generated at 2022-06-14 13:02:32.808841
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():

    class MyConfigurable(Configurable):

        def configurable_base(self):
            return MyConfigurable

        def configurable_default(self):
            return Config1

        def initialize(self, name):
            self.name = name


    class Config1(MyConfigurable):

        def __init__(self, name):
            self.name = name


    class Config2(MyConfigurable):

        def __init__(self, name):
            self.name = name


    MyConfigurable.configure(Config2)
    assert MyConfigurable("hello").name == "hello"
    MyConfigurable.configure(Config1)
    assert MyConfigurable("hello").name == "hello"
    assert isinstance(MyConfigurable("hello"), Config1)
    assert isinstance(MyConfigurable("hello"), Config2)
   

# Generated at 2022-06-14 13:02:37.552867
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f1(a, b):
        return a, b
    assert ArgReplacer(f1, 'a').replace(11, [1, 2], {}) == (1, [11, 2], {})
    assert ArgReplacer(f1, 'b').replace(22, [1, 2], {}) == (2, [1, 22], {})
    def f2(a, b):
        return a, b
    assert ArgReplacer(f2, 'b').replace(22, [1], {}) == (None, [1], {'b': 22})
    def f3(a):
        return a
    assert ArgReplacer(f3, 'a').replace(11, [1], {}) == (1, [11], {})
    def f4(*, a, b):
        return a, b

# Generated at 2022-06-14 13:02:48.120443
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    call_args = ("a",)
    call_kwargs = {"name": "b", "age": 24}
    # test for key word
    assert ArgReplacer(test_ArgReplacer_replace, "name").\
        replace("TEST", call_args, call_kwargs) == (
            'b', ('a',), {'age': 24, 'name': 'TEST'})
    # test for position
    assert ArgReplacer(test_ArgReplacer_replace, "a").\
        replace("TEST", call_args, call_kwargs) == (
            'a', ('TEST',), {'age': 24, 'name': 'b'})
    # old_value not exist

# Generated at 2022-06-14 13:02:54.550842
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test(a, b):
        return a, b
    # test with positional argument a
    result = ArgReplacer(test, "a").replace(3, (1, 2), {})
    assert result == (1, (3, 2), {})
    # test with positional argument b
    result = ArgReplacer(test, "b").replace(3, (1,), {})
    assert result == (None, (1, 3), {})
    # test with kwarg a
    result = ArgReplacer(test, "a").replace(3, (), {"a": 1})
    assert result == (1, (), {"a": 3})
    # test with kwarg b
    result = ArgReplacer(test, "b").replace(3, (), {"b": 2})
    assert result == (2, (), {"b": 3})

# Generated at 2022-06-14 13:03:15.274776
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # test_Configurable_initialize_rejected_positional_argument
    class ConfigurableClass(Configurable):
        def configurable_base(self):
            return ConfigurableClass

        def configurable_default(self):
            return None

        def initialize(self, *args, **kwargs):
            if len(args) > 0:
                raise AssertionError("__init__ got unexpected positional arguments: %r" % args)
            super(ConfigurableClass, self).initialize(**kwargs)

    c = ConfigurableClass()  # no positional arguments are allowed

    # test_Configurable_initialize_accepted_positional_argument
    class ConfigurableClass(Configurable):
        def configurable_base(self):
            return ConfigurableClass

        def configurable_default(self):
            return None


# Generated at 2022-06-14 13:03:27.583311
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    class Sample(object):
        def wrap(self, arg_a, arg_b, arg_c=None, arg_d=None, *args, **kwargs):
            return arg_a, arg_b, arg_c, arg_d, args, kwargs
        def wrap_multi(self, arg_a, arg_b, arg_c=None, arg_d=None, *args, **kwargs):
            return arg_a, arg_b, arg_c, arg_d, args, kwargs

    def test_case(object_arg, method_arg, args, kwargs, new_value, expect_output):
        a, b, c, d, rest_args, rest_kwargs = getattr(object_arg, method_arg)(*args, **kwargs)

# Generated at 2022-06-14 13:03:36.362596
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable

        def initialize(self, a, b, c=None):
            pass

    TestConfigurable.configure(impl=None, d=1, e=2)
    instance = TestConfigurable(a=3, b=4, c=5)
    assert instance.a == 3
    assert instance.b == 4
    assert instance.c == 5
    assert instance.d == 1
    assert instance.e == 2



# Generated at 2022-06-14 13:03:49.229424
# Unit test for function import_object
def test_import_object():
    assert import_object("os") is os
    assert import_object("os.path") is os.path
    assert import_object("os.path.basename") is os.path.basename
    try:
        import_object("os.missing_module")
        assert False, "expected exception"  # type: ignore
    except ImportError:
        pass


# Even though metaclasses are deprecated in Python 3, they are still
# commonly used to provide a hook for customizing class creation.
# If we see metaclass= in the attributes, we can use it to store
# a dictionary of interface methods that must be provided.
# For example, when subclassing IOLoop, you might specify:
# class MyLoop(IOLoop):
#   __metaclass__ = IOLoop.ConfigurableMetaclass
#   config = {}  #

# Generated at 2022-06-14 13:03:57.866108
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(a, b, c):
        pass
    arg = ArgReplacer(foo, "a")
    assert arg.get_old_value((1, 2, 3), {}) == 1
    assert arg.get_old_value((1, 2, 3), {}, None) == 1
    assert arg.get_old_value((1, 2), {}, None) is None
    assert arg.get_old_value((1, 2), {}, "default") == "default"
    assert arg.get_old_value((1, 2), {"a": "A"}, None) == "A"
    assert arg.get_old_value((1, 2), {"a": "A"}, "default") == "A"
    arg = ArgReplacer(foo, "b")

# Generated at 2022-06-14 13:04:05.118024
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    def method(input_mapping):
        # type: (Mapping[str, Any]) -> ObjectDict
        return ObjectDict(input_mapping)
    d = {"a": 1, "b": 2}  # type: Mapping[str, Any]
    assert method(d).a == 1
    assert method(d).b == 2
    assert hasattr(method(d), "a")
    assert hasattr(method(d), "b")
    assert not hasattr(method(d), "c")

# Generated at 2022-06-14 13:04:06.371323
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass



# Generated at 2022-06-14 13:04:16.816526
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):

        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable

        def initialize(self, *args: Any, **kwargs: Any) -> None:
            pass

    class SubTestConfigurable(TestConfigurable):
        pass

    SubTestConfigurable.configure(SubTestConfigurable)
    assert SubTestConfigurable().__class__ == SubTestConfigurable
    TestConfigurable.configure(SubTestConfigurable)
    assert SubTestConfigurable().__class__ == SubTestConfigurable
    #
    TestConfigurable.configure(None)
    assert SubTestConfigurable().__class__ == SubTestConfigurable

# Generated at 2022-06-14 13:04:23.888355
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def f(a, b, c=None, d=None):
        pass

    # Positional argument
    r = ArgReplacer(f, "b")
    assert r.get_old_value(("foo", "bar",), {}) == "bar"
    assert r.replace("baz", ("foo",), {}) == ("bar", ("foo", "baz",), {})
    # Default keyword argument
    r = ArgReplacer(f, "c")
    assert r.get_old_value(("foo",), {}) is None
    assert r.replace("baz", ("foo",), {}) == (None, ("foo",), {"c": "baz"})
    # Nonexistent argument
    r = ArgReplacer(f, "z")
    assert r.get_old_value(("foo",), {})

# Generated at 2022-06-14 13:04:36.539378
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    """Unit test for method replace of class ArgReplacer."""
    # ArgReplacer.replace: test with args, kwargs
    def f(a, b=0):
        return a, b

    def f2(a=0, **kwargs):
        return a, kwargs
    # test with positional arguments
    old_value, args, kwargs = ArgReplacer("b").replace(2, (1,), {})
    assert old_value == 0
    assert args == (1,)
    assert kwargs == {"b": 2}

    old_value, args, kwargs = ArgReplacer("a").replace(2, (1,), {})
    assert old_value == 1
    assert args == (2,)
    assert kwargs == {}

    old_value, args, kwargs = ArgReplacer

# Generated at 2022-06-14 13:04:55.974336
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f1(x, y, z=3, *args, **kwargs):
        pass

    def f2(a, b, c, *, d, e, **kwargs):
        pass
    
    def f3(*args):
        pass
    
    def f4(**kwargs):
        pass

    assert ArgReplacer(f1, 'x').get_old_value((2, 3), {'z': 7}) == 2
    assert ArgReplacer(f1, 'y').get_old_value((2, 3), {'z': 7}) == 3
    assert ArgReplacer(f1, 'z').get_old_value((2, 3), {'z': 7}) == 7

# Generated at 2022-06-14 13:05:03.991967
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func1(a, b, c, d=3, e=2):
        return a, b, c, d, e

    f = ArgReplacer(func1, 'd')
    r = f.replace(4, (1, 2, 3), {})
    assert r == (3, (1, 2, 3), {'d': 4})

    def func2(a=3, b=2, c=1):
        return a, b, c

    f = ArgReplacer(func2, 'c')
    r = f.replace(4, (), {})
    assert r == (1, (), {'c': 4})



# Generated at 2022-06-14 13:05:16.868094
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    from unittest import mock

    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable

    class TestConfigurableImpl(TestConfigurable):
        def __init__(self, a, b, c=None):
            self.a = a
            self.b = b
            self.c = c

    class TestConfigurableInitKwargs(TestConfigurable):
        def __init__(self, a, b, c=None):
            self.a = a
            self.b = b
            self.c = c


# Generated at 2022-06-14 13:05:24.423503
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():

    def test_func(arg_to_replace, other_arg=None):
        pass
    arg_replacer = ArgReplacer(test_func, 'arg_to_replace')

    assert arg_replacer.get_old_value((1, 2), {}, ) is None
    assert arg_replacer.get_old_value((1, 2), {'arg_to_replace': 3, }) == 3
    assert arg_replacer.get_old_value((5,), {'arg_to_replace': 3, }) == 5


# Generated at 2022-06-14 13:05:32.929734
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b, c=None):
        pass
    ra = ArgReplacer(f, 'b')
    assert ra.replace(23, (1,2,), {'c':None, 'd': None}) == (2, (1,23,), {'c':None, 'd': None})
    assert ra.replace(23, (1,2,3), {'d':None}) == (2, (1,23,3), {'d':None})
    assert ra.replace(23, (1,), {'b':2, 'd':None}) == (2, (1,), {'b':23,'d':None})

# End of unit test of method replace of class ArgReplacer


# Generated at 2022-06-14 13:05:38.919410
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    with ExitStack() as stack:
        Configurable.configure = stack.enter_context(mock.Mock())
        Configurable.configured_class = stack.enter_context(mock.Mock(return_value=Configurable))
        Configurable.configurable_base = stack.enter_context(mock.Mock(return_value=Configurable))
        Configurable.initialize = stack.enter_context(mock.Mock())
        Configurable.__init__ = stack.enter_context(mock.Mock())
        Configurable.__new__(Configurable, 'arg1', 'arg2', key1='value1', key2='value2')


# Generated at 2022-06-14 13:05:44.172339
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func1(a, b=0, c=0, *args, **kwargs):
        return a, b, c, args, kwargs
    def func2(a, b=0, c=0):
        return a, b, c

    argument = ArgReplacer(func1, 'b')
    assert argument.get_old_value((1, 2), {'c': 3}) == 2
    assert argument.get_old_value((1, 2, 3), {'c': 4}) == 2
    assert argument.get_old_value((1, ), {'c': 3, 'b': 2}) == 2
    assert argument.get_old_value((1, 2, 4, 5, 6), {'a': 2, 'c': 6}) == 2

# Generated at 2022-06-14 13:05:48.488848
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Foo(Configurable):
        def configurable_base(self):
            return Foo

        def configurable_default(self):
            return Foo

        def _initialize(self):
            self.args = []
            self.kwargs = {}
            self.initialized = True
    # Test that Foo() behaves like a normal class.
    foo = Foo()
    assert isinstance(foo, Foo)
    assert foo.initialized
    # Test that configure/configured_class works as expected.
    Bar = Configurable.configure(Foo, bar=True)
    assert Foo.configured_class() == Bar
    foo = Bar()
    assert foo.initialized
    assert foo.kwargs == {"bar": True}
    # Test the default implementation.
    Baz = Configurable.configure(None)
    assert Foo.configured_class

# Generated at 2022-06-14 13:05:56.594943
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    # type: () -> None
    def f(a, b, c):
        pass

    c = ArgReplacer(f, "c")
    assert c.get_old_value((1, 2, 3), {}, None) is not None
    assert c.replace("d", (1, 2, 3), {}) == (3, (1, 2, "d"), {})
    assert c.replace("d", (1, 2), {"c": 3}) == (3, (1, 2, "d"), {})
    assert c.replace("d", (1, 2), {}) == (None, (1, 2, "d"), {})



# Generated at 2022-06-14 13:05:59.958770
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Subclass(Configurable):
        @classmethod
        def configurable_base(cls):
            return Subclass

        @classmethod
        def configurable_default(cls):
            return Subclass
    Subclass.configure(None)
    assert isinstance(Subclass(), Subclass)
    assert isinstance(Subclass(), Configurable)



# Generated at 2022-06-14 13:06:27.872119
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class MyConfigurable(Configurable):
        def initialize(self, arg1=None, arg2=None):
            pass

        @classmethod
        def configurable_base(cls):
            return MyConfigurable

        @classmethod
        def configurable_default(cls):
            return MyConfigurable

    # test that we can call initialize
    my_configurable = MyConfigurable()
    my_configurable.initialize()


# Generated at 2022-06-14 13:06:36.751143
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def func(a, b, c=3, d=4):
        pass

    argreplacer = ArgReplacer(func, "c")
    assert argreplacer.get_old_value((1, 2), dict(d=10), None) is 3
    assert argreplacer.get_old_value((1, 2), dict(), None) is None
    assert argreplacer.get_old_value((1, 2), dict(), "missing") == "missing"

    assert argreplacer.replace("new", (1, 2), dict(d=10)) == (
        3,
        (1, 2),
        dict(d=10),
    )
    assert argreplacer.replace("new", (1, 2), dict()) == (
        None,
        (1, 2),
        dict(c="new"),
    )



# Generated at 2022-06-14 13:06:47.685458
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    try:
        import unittest2 as unittest  # type: ignore
    except ImportError:
        import unittest
    try:
        from unittest import mock  # type: ignore
    except ImportError:
        import mock  # type: ignore


    class _ConfigurableTest(object):
        """Base class for tests of `Configurable`.

        The test class must define a nested `Implemented` class that
        implements `Configurable`.

        """

        class Implemented(Configurable):
            """Mock class for testing `Configurable`."""

            def __init__(self, value):
                # type: (Any) -> None
                self.value = value


# Generated at 2022-06-14 13:06:49.352883
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """Tests the method __new__ of class Configurable"""
    pass



# Generated at 2022-06-14 13:06:55.978594
# Unit test for function import_object
def test_import_object():
    # Just to make sure it works, import a module that only exists in the
    # environment where these tests are run.
    assert import_object("unittest") is unittest


# fake byte literal for 2.6.
b = b''

# Types for type hints
try:
    from typing import Protocol, runtime_checkable  # type: ignore  # noqa: F401
except ImportError:
    pass
else:
    class DelegateChar(Protocol):
        def __getitem__(self, key: int) -> str:
            pass

    class DelegateString(Protocol):
        def __getitem__(self, key: slice) -> str:
            pass

    class DelegateBytes(Protocol):
        def __getitem__(self, key: slice) -> bytes:
            pass



# Generated at 2022-06-14 13:06:59.315994
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    obj = ObjectDict(a='1')
    assert obj.a == '1'

# Testing method: __setattr__ of class ObjectDict

# Generated at 2022-06-14 13:07:05.364135
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    f = lambda x, y, z=1: (x,y,z)
    argr = ArgReplacer(f,'y')
    assert argr.get_old_value((1,2),{}),2
    assert argr.get_old_value((1,), {'y':3}),3
    assert argr.get_old_value((),{'y':3}),3
    assert argr.get_old_value((1,),{'z':2}),None


# Generated at 2022-06-14 13:07:16.654408
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    old_value = 3
    def test_func(arg1, arg2=None, arg3=None):
        return (arg1, arg2, arg3)
    # Test the case that the argument is passed positionally
    arg_replacer = ArgReplacer(test_func, "arg1")
    args = [old_value]
    kwargs = dict()
    assert arg_replacer.get_old_value(args, kwargs) == old_value
    # Test the case that the argument is passed by keyword
    arg_replacer = ArgReplacer(test_func, "arg2")
    args = []
    kwargs = {'arg2': old_value}
    assert arg_replacer.get_old_value(args, kwargs) == old_value
    # Test the case that the argument is not

# Generated at 2022-06-14 13:07:23.909038
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    expected_args = (1, 2, 3)
    expected_kwargs = {'test': 1}

    class ConfigurableInitializeTest(Configurable):
        def __init__(self, *args, **kwargs):
            raise RuntimeError('This should not have been called')

        def initialize(self, *args, **kwargs):
            assert args == expected_args
            assert kwargs == expected_kwargs

    ConfigurableInitializeTest(*expected_args, **expected_kwargs)


# Generated at 2022-06-14 13:07:32.898740
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.platform.auto import set_close_exec, Waker
    class AConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls
        @classmethod
        def configurable_default(cls):
            return TestFd1
    class TestFd(object):
        def __init__(self, fd):
            # type: (int) -> None
            self.fd = fd
        def fileno(self):
            # type: () -> int
            return self.fd
    class TestFd1(TestFd):
        pass
    class TestFd2(TestFd):
        pass
    # test_AFileWrapper_configure
    cfg = AConfigurable.configure

# Generated at 2022-06-14 13:07:55.860656
# Unit test for function import_object
def test_import_object():
    def f():
        pass

    def g():
        pass

    assert import_object("functools") is functools
    assert import_object("collections.defaultdict") is collections.defaultdict
    assert import_object("test.test_util.test_import_object.f") is f
    assert import_object("test.test_util.test_import_object.g") is g


_TIMEOUT_RE = re.compile(r"^([a-zA-Z]+)(?:\((\d+)\))?$")



# Generated at 2022-06-14 13:08:03.120124
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f1(a,b,c):
        pass
    def f2(a,b,*args):
        pass
    def f3(a,b,*args, **kwargs):
        pass
    def f4(a,b,**kwargs):
        pass
    def f5(a,b,c=100,d=100):
        pass
    def f6(a,b=100,c=100):
        pass
    def f7(a,b=100,c=100,**kwargs):
        pass
    def f8(a,b=100,c=100,**kwargs):
        pass
    r = ArgReplacer(f1,'c')
    assert ([1,2,3], {}, 3) == r.replace(33,(1,2,3),{})

# Generated at 2022-06-14 13:08:08.974347
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class MyConfigurable(Configurable):
        def initialize(self):
            pass
    with pytest.raises(NotImplementedError):
        MyConfigurable.configurable_base()
    with pytest.raises(NotImplementedError):
        MyConfigurable.configurable_default()

# Generated at 2022-06-14 13:08:11.038216
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    """Test of method __new__ of class Configurable"""




# Generated at 2022-06-14 13:08:18.398914
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest
    import functools

    import tornado.httputil
    import tornado.util

    class ConfigurableTestCase(unittest.TestCase):

        def test_reconfigure(self):
            # type: () -> None
            # Save the current configuration, reconfigure, and restore it
            saved = tornado.httputil.HTTPHeaders._save_configuration()
            try:
                tornado.httputil.HTTPHeaders.configure(
                    "tornado.httputil.HTTPHeaders",
                    default_user_agent="A")
                self.assertEqual(
                    tornado.httputil.HTTPHeaders().get("User-Agent"), "A")
            finally:
                tornado.httputil.HTTPHead

# Generated at 2022-06-14 13:08:29.159980
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    obj = object()
    assert Configurable.configured_class() is None
    assert Configurable.__new__(Configurable) is Configurable.__new__(
        Configurable
    )
    assert Configurable.configured_class() is Configurable

    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return A

    assert A.configured_class() is A

    class A2(A):
        pass

    assert A.configured_class() is A
    assert A2.configured_class() is A

    class B(Configurable):
        @classmethod
        def configurable_base(cls):
            return B


# Generated at 2022-06-14 13:08:39.940034
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():

    def assert_type(x, t):
        if not isinstance(x, t):
            raise ValueError('Unexpected type')

    class A(Configurable):
        def configurable_base(self):
            return A

        def configurable_default(self):
            return A

        def initialize(self, x):
            self.x = x

        def _initialize(self, x):
            self.x = x

        def __init__(self, x):
            self.x = x

    class B(A):
        def configurable_base(self):
            return A

        def configurable_default(self):
            return B

        def initialize(self, x):
            self.x = x

        def _initialize(self, x):
            self.x = x


# Generated at 2022-06-14 13:08:46.267540
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(a,b,c):
        pass
    a = ArgReplacer(foo,"b")
    print(a.replace(3,(1,2,3),{}))
    print(a.replace(3,(1,2,3),{"a":1}))
    print(a.replace(3,(1,),{"b":2}))
    print(a.replace(3,(1,),{"a":1,"b":2}))


# Generated at 2022-06-14 13:08:54.383690
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class CustomConfigurable(Configurable):
        def __init__(self):
            # type: () -> None
            raise Exception('__init__ should not be called')

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return CustomConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return CustomConfigurable

        def initialize(self):
            # type: () -> None
            pass

    CustomConfigurable()



# Generated at 2022-06-14 13:09:00.685082
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception()
    except Exception as e:
        assert errno_from_exception(e) is None

    try:
        raise Exception(42, "foo")
    except Exception as e:
        assert errno_from_exception(e) == 42

    try:
        raise Exception("foo")
    except Exception as e:
        assert errno_from_exception(e) == "foo"



# Generated at 2022-06-14 13:10:00.358251
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class SubConfigurable(Configurable):
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Configurable

        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return cls

        def initialize(self, arg1, arg2, **kwargs):
            # type: (str, str, Any) -> None
            self.arg1 = arg1
            self.arg2 = arg2
            self.kwargs = kwargs

    SubConfigurable.configure(None)
    instance = SubConfigurable("foo", "bar", spam="eggs")
    assert instance.arg1 == "foo"
    assert instance.arg2 == "bar"
    assert instance.kwargs["spam"] == "eggs"

# Generated at 2022-06-14 13:10:08.701777
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    assert issubclass(Configurable, object)
    assert not issubclass(Configurable, type)
    assert not hasattr(Configurable, '__dict__')
    assert hasattr(Configurable, '__new__')
    assert callable(Configurable.__new__)
    assert not hasattr(Configurable, '__init__')
    assert hasattr(Configurable, '__impl_class')
    assert isinstance(Configurable.__impl_class, property)
    assert hasattr(Configurable, '__impl_kwargs')
    assert isinstance(Configurable.__impl_kwargs, property)
    assert hasattr(Configurable, 'configurable_base')
    assert callable(Configurable.configurable_base)
    assert not hasattr(Configurable, 'configurable_default')

# Generated at 2022-06-14 13:10:20.229905
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # Test for a subclass(Configurable) which does not implement the
    # required configurable_XXX methods
    class TestConfigurable(Configurable):
        def _initialize(self):
            pass
    # Test for a subclass(Configurable) which implements the required
    # configurable_XXX methods
    class TestConfigurable2(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

        def _initialize(self):
            pass

    # Test to call __new__ method of class Configurable
    with pytest.raises(NotImplementedError):
        TestConfigurable()

    # Test to call __new__ method of class Configurable

# Generated at 2022-06-14 13:10:32.246323
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class GoodTemplateConfiguration(Configurable):
        def configurable_base(self):
            return GoodTemplate

        def configurable_default(self):
            return template.SimpleTemplate

        def initialize(self, template_name, file_path, module_directory=None, **kwargs):
            self.template_name = template_name
            self.file_path = file_path
            self.module_directory = module_directory

    # class GoodTemplate(Configurable):
    class GoodTemplate(object):
        def render(self):
            return "result"

    GoodTemplate.configure("tornado.template.SimpleTemplate")
    GoodTemplate.configure(GoodTemplateConfiguration)
    my_template = GoodTemplate("template_name", "file_path", module_directory="module_directory")
    assert my_template.render() == "result"
   

# Generated at 2022-06-14 13:10:36.158687
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Foo(Configurable):
        @classmethod
        def configurable_base(cls):
            return Foo
        @classmethod
        def configurable_default(cls):
            return Foo
    Foo.configure(None)
    f = Foo()


# Generated at 2022-06-14 13:10:37.370239
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    obj = Configurable()


# Generated at 2022-06-14 13:10:48.351659
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            return Base

        @classmethod
        def configurable_default(cls):
            return Derived1
  
    class Derived1(Base):
        def initialize(self, a, b, c=None, d=None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    class Derived2(Base):
        def initialize(self, a, b, c=None, d=None):
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    obj = Base(1, 2)
    assert isinstance(obj, Derived1)
    assert obj.a == 1
    assert obj.b

# Generated at 2022-06-14 13:10:53.436838
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import unittest
    import unittest.mock
    class ConfigA(Configurable):
        def initialize(self, val):
            self.val = val
            # Access the superclass method, e.g. in tests where
            # the superclass is mocked out.
            super(ConfigA, self).initialize()
    class ConfigB(ConfigA):
        def initialize(self, val, multiplier=2):
            self.multiplier = multiplier
            super().initialize(val)
    ConfigA.configure(ConfigA, multiplier=3)
    a = ConfigA('a')
    assert a.val == 'a'
    assert a.multiplier == 3
    b = ConfigB('b')
    assert b.val == 'b'
    assert b.multiplier == 2
    # If a subclass is configured the superclass is

# Generated at 2022-06-14 13:10:56.772636
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    c = ObjectDict()
    c.test = True
    assert c.test
test_ObjectDict___getattr__()


# Generated at 2022-06-14 13:11:03.886142
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Child(Configurable):
        @classmethod
        def configurable_base(cls):
            return Child

        @classmethod
        def configurable_default(cls):
            return Child

        def initialize(self, a: int, b: int = 0) -> None:
            self._a = a
            self._b = b

    assert not hasattr(Child, "_a") and not hasattr(Child, "_b")
    Child(3)
    assert Child._a == 3 and Child._b == 0
    Child(3, 5)
    assert Child._a == 3 and Child._b == 5

