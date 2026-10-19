

# Generated at 2022-06-14 13:01:49.346559
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    import typing

    class configurable_base_impl(Configurable):
        @classmethod
        def configurable_base(cls):
            return configurable_base_impl

        @classmethod
        def configurable_default(cls):
            return configurable_base_impl

        def _initialize(self):
            pass


    class configurable_impl(configurable_base_impl):
        def __init__(self, kwargs):
            pass


    class configurable_callable_impl(configurable_base_impl):
        def __init__(self, kwargs):
            pass

        def __call__(self):
            pass


    def CreateConfigurableByString():
        configurable_base_impl.configure("tornado.util_test.configurable_impl")
       

# Generated at 2022-06-14 13:01:59.188263
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a: str, *, b: str) -> None:
        pass
    r = ArgReplacer(f, 'a')
    assert(r.get_old_value(('old_a', ), {'b': 'old_b'}, None) == 'old_a')
    assert(r.get_old_value(('old_a', ), {'b': 'old_b'}, 'default') == 'old_a')
    assert(r.get_old_value((), {'a': 'old_a'}, None) == 'old_a')
    assert(r.get_old_value((), {'a': 'old_a'}, 'default') == 'old_a')
    assert(r.get_old_value((), {}, None) is None)

# Generated at 2022-06-14 13:02:07.956998
# Unit test for function import_object
def test_import_object():
    # This is horrible, we should probably just use mock or something
    import sys
    import types  # noqa: F401

    class FakeModule(types.ModuleType):
        def __init__(self, name, *args, **kwargs):
            super().__init__(name, *args, **kwargs)
            self.__name__ = name

        def __getattr__(self, name):
            obj = FakeModule(self.__name__ + "." + name)
            setattr(self, name, obj)
            return obj

    def fake_import(name, *args, **kwargs):
        if name in sys.modules:
            return sys.modules[name]
        obj = FakeModule(name)
        sys.modules[name] = obj
        return obj

    orig_import = __import__
    __import

# Generated at 2022-06-14 13:02:14.688104
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c=None):
        pass
    replacer = ArgReplacer(func, "c")
    assert replacer.get_old_value((1, 2), {}) is None
    assert replacer.get_old_value((1, 2), {"c": 10}) == 10
    assert replacer.get_old_value((1, 2, 3), {}) == 3
    assert replacer.get_old_value((1, 2, 3), {"c": 10}) == 3


# Generated at 2022-06-14 13:02:19.976619
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
      # __init__ and get_old_value is private, but it is still useful
      # to test them as they are used in decorator add_auth.
      a = ArgReplacer(RequestHandler.__init__, "kwargs")

# Generated at 2022-06-14 13:02:23.967087
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c=None, d=None):
        pass

    a = ArgReplacer(func, 'c')
    print(a.get_old_value(('a', 'b'), {}))



# Generated at 2022-06-14 13:02:34.751983
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class MyConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return MyConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return MyConfigurable

        def initialize(self, a, b, c=3, **kwargs):
            self.a = a
            self.b = b
            self.c = c
            self.kwargs = kwargs

    MyConfigurable.configure(None, c=2)
    inst = MyConfigurable(1, 2, d=4)
    assert inst.a == 1
    assert inst.b == 2
    assert inst.c == 2

# Generated at 2022-06-14 13:02:41.258321
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
  def f(x, y, z):
    pass
  args = (1, 2, 3)
  kwargs = {'z': 3}
  argr = ArgReplacer(f, 'z')
  old, args_new, kwargs_new = argr.replace(99, args, kwargs)
  assert old == 3
  assert args_new == (1, 2, 99)
  assert kwargs_new == {'z': 99}
  # Unit test for method get_old_value of class ArgReplacer

# Generated at 2022-06-14 13:02:50.543494
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurableImpl

        def initialize(self):
            pass

    class TestConfigurableImpl(TestConfigurable):
        def initialize(self):
            pass
    TestConfigurable.configure(None)
    TestConfigurable.configure(impl=None)
    TestConfigurable.configure(impl=TestConfigurableImpl)
    TestConfigurable.configure(impl=TestConfigurableImpl, a=1, b=2)
    TestConfigurable.configure(impl=None, a=1, b=2)
    TestConfigurable.configure(impl=TestConfigurable, a=1, b=2)



# Generated at 2022-06-14 13:03:02.554904
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    assert ArgReplacer.replace(1, args=(1,), kwargs={}) == (1, (1,), {})
    assert ArgReplacer.replace(2, args=(1,), kwargs={}) == (None, (1,), {'a': 2})
    assert ArgReplacer.replace(3, args=(1, 2), kwargs={}) == (2, (1, 3), {})
    assert ArgReplacer.replace(4, args=(), kwargs={'a': 1, 'b': 2}) == (1, (), {'a': 4, 'b': 2})
    assert ArgReplacer.replace(5, args=(), kwargs={}) == (None, (), {'a': 5})

# Generated at 2022-06-14 13:03:23.580710
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    import tornado.ioloop
    from tornado import gen

    class FooImpl(Configurable):
        __impl_class = None
        __impl_kwargs = None

        @classmethod
        def configurable_base(self):
            # type: () -> Type[Configurable]
            return FooImpl

        @classmethod
        def configurable_default(self):
            # type: () -> Type[Configurable]
            return FooImpl

        def initialize(self):
            # type: () -> None
            pass

    @gen.coroutine
    def test_configure():
        FooImpl.configure(FooImpl)
        assert isinstance(FooImpl(), FooImpl)
        assert FooImpl.configured_class() is FooImpl
        io_loop = tornado.ioloop.IOLoop.instance()

# Generated at 2022-06-14 13:03:31.344519
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """
    >>> class TestConfigurableNew(Configurable):
    ...
    ...     @classmethod
    ...     def configurable_base(cls):
    ...         return TestConfigurableNew
    ...     @classmethod
    ...     def configurable_default(cls):
    ...         return TestConfigurableNew
    ...     def initialize(self, *args, **kwargs):
    ...         self.args = args
    ...         self.kwargs = kwargs
    >>> tc = TestConfigurableNew('a', b=1)
    >>> tc.args
    ('a',)
    >>> tc.kwargs
    {'b': 1}
    """



# Generated at 2022-06-14 13:03:40.559164
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class example(Configurable):
        @classmethod
        def configurable_base(cls):
            return example_base

        @classmethod
        def configurable_default(cls):
            return example_base.__impl_class

        def initialize(self, a, b):
            self.a = a
            self.b = b

    class example_base(Configurable):
        @classmethod
        def configurable_base(cls):
            return example

        @classmethod
        def configurable_default(cls):
            return example

    example.configure(None)
    try:
        instance = example(1, 2)
        assert isinstance(instance, example)
        assert instance.a == 1
        assert instance.b == 2
    finally:
        example.configure(None)


# Generated at 2022-06-14 13:03:45.322433
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest

    class A(Configurable):
        def configurable_base(self):
            return A

        def configurable_default(self):
            return B

        def __init__(self, *args, **kwargs):
            pass

    class B(A):
        pass

    class C(Configurable):
        def configurable_base(self):
            return C

        def configurable_default(self):
            return D

        def __init__(self, *args, **kwargs):
            pass

    class D(C):
        pass

    class TestConfigurable(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_configure(self):
            A.configure(A)
            a = A()
            self

# Generated at 2022-06-14 13:03:55.463168
# Unit test for function errno_from_exception
def test_errno_from_exception():
    class AppError(OSError):
        pass

    class AppZeroDivisionError(ZeroDivisionError):
        pass

    assert errno_from_exception(AppError()) == 0
    assert errno_from_exception(AppError(404)) == 404
    assert errno_from_exception(AppError((404, "Not Found"))) == 404
    assert errno_from_exception(AppError(AppError(404)).__cause__) == 404
    assert errno_from_exception(OSError(404, "Not Found", "/tmp/foo")) == 404
    assert errno_from_exception(OSError(
        OSError(EINTR, "Interrupted system call"), "Not Found", "/tmp/foo")) == EINTR

# Generated at 2022-06-14 13:04:06.152398
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def f(foo=1, bar=2):
        pass

    assert ArgReplacer(f, "foo").name == "foo"
    assert ArgReplacer(f, "foo").get_old_value((), {}) == 1
    assert ArgReplacer(f, "foo").get_old_value((), {"foo": 10}) == 10
    assert ArgReplacer(f, "foo").replace(2, (), {}) == (1, (), {"foo": 2})
    assert ArgReplacer(f, "bar").name == "bar"
    assert ArgReplacer(f, "bar").get_old_value((), {}) == 2
    assert ArgReplacer(f, "bar").get_old_value((), {"bar": 10}) == 10

# Generated at 2022-06-14 13:04:13.364461
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func_1(name, age):
        return name, age
    def func_2(name, age=None):
        return name, age
    def func_3(age, name):
        return name, age
    def func_4(age=None, name=None):
        return name, age
    def func_5(name=None, age=None):
        return name, age

# Generated at 2022-06-14 13:04:23.414372
# Unit test for function import_object
def test_import_object():
    from tornado.escape import json_decode
    assert import_object("tornado.escape.json_decode") is json_decode
    assert import_object("json") is json
    assert import_object("sys") is sys
    assert import_object("sys.path") is sys.path
    assert import_object("tornado.missing_module")
from tornado.test.util_test import test_import_object


# Fake byte literal support:  In python 2.6+, you can say b"foo" to get
# a byte literal (str in 2.x, bytes in 3.x).  There's no way to do this
# in a way that supports 2.5, though, so we need a function wrapper
# to convert our string literals.  b() should only be applied to literal
# latin1 strings.  Once we drop support for 2

# Generated at 2022-06-14 13:04:28.708188
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    # Arrange
    argreplacer = ArgReplacer(test_ArgReplacer_get_old_value, "name")
    name = "test"

    # Act
    result = argreplacer.get_old_value(("test",), {}, "fail")

    # Assert
    assert result == name


# Generated at 2022-06-14 13:04:40.603298
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():

    # test method get_old_value in class ArgReplacer
    def foo(a, b, c=None):
        pass

    f = ArgReplacer(foo, 'c')
    assert f.get_old_value(('a', 'b', 'c'), {}) == 'c'
    assert f.get_old_value(('a', 'b'), {'c': 'c'}) == 'c'
    assert f.get_old_value(('a', 'b'), {}) is None
    assert f.get_old_value(('a', 'b'), {}, 'd') == 'd'

    # test method get_old_value in class ArgReplacer
    def foo(a, b, c, d=None):
        pass

    f = ArgReplacer(foo, 'd')
    assert f.get_old

# Generated at 2022-06-14 13:05:02.257610
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Tests the call signature of Configurable.__new__. This method
    # signature, and the `initialize` method signature, have changed
    # over the years (accepting positional arguments, accepting keyword
    # arguments, etc.) so need to be tested.
    class _TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return _TestConfigurable

        @classmethod
        def configurable_default(cls):
            raise NotImplementedError()

        def _initialize(self, foo=False, bar=False, *args, **kwargs):
            for k in ("foo", "bar"):
                if k in kwargs and kwargs[k] is not None:
                    raise TypeError("_initialize got an unexpected keyword argument: %s" % k)
            self.pos

# Generated at 2022-06-14 13:05:12.279056
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(*a, **k):
        pass

    ArgReplacer(f, "a").replace(3, (), {})
    ArgReplacer(f, "a").replace(3, (4,), {})
    ArgReplacer(f, "a").replace(3, (), {"a": 4})
    ArgReplacer(f, "a").replace(3, (4,), {"a": 4})
    ArgReplacer(f, "a").replace(3, (4, 5), {"a": 4})
    ArgReplacer(f, "a").replace(3, (4, 5), {"a": 4, "b": 5})



# Generated at 2022-06-14 13:05:23.845278
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    import tornado.test

    class Bar(Configurable):
        if hasattr(object, "__class__"):
            assert object.__class__ != Bar
        if hasattr(object, "__init__"):
            assert object.__init__ != Bar

        @classmethod
        def configurable_base(cls):
            return Bar

        @classmethod
        def configurable_default(cls):
            return Bar

        def initialize(self):
            if hasattr(self, "__class__"):
                assert self.__class__ == Baz

    class Baz(Bar):
        pass

    class Quux(Bar):
        pass

    class MyTestCase(unittest.TestCase):
        def setUp(self):
            Bar.configure(Quux)


# Generated at 2022-06-14 13:05:28.316880
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    """Test that the right value is returned by get_old_value of class ArgReplacer

    :return:
    """
    def foo(a, b=2):
        pass

    value = ArgReplacer(foo, "b").get_old_value((3,),{})

    assert value == 2


# Generated at 2022-06-14 13:05:36.796374
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    def _test_Configurable_initialize_eq(expected, *args, **kwargs):
        c = ConfigurableClass(*args, **kwargs)
        assert expected == c.initialize_args

    def _test_Configurable_initialize_raises(exc_type, exc_msg, *args, **kwargs):
        with pytest.raises(exc_type) as e:
            ConfigurableClass(*args, **kwargs)
        if exc_msg is not None:
            assert exc_msg in str(e.value)

    class ConfigurableClass(Configurable):
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            raise Exception(
                "Initializer called directly. "
                "Use Configurable.initialize instead."
            )

       

# Generated at 2022-06-14 13:05:39.972124
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class Foo(Configurable):
        def configurable_base(self):
            # type: () -> Type[Configurable]
            raise NotImplementedError()

        def configurable_default(self):
            # type: () -> Type[Configurable]
            raise NotImplementedError()

    foo = Foo()
    assert isinstance(foo, Foo)



# Generated at 2022-06-14 13:05:50.616894
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b, c, d=42):
        pass
    r = ArgReplacer(f, "d")
    assert r.replace(1, (1, 2, 3), {}) == (42, (1, 2, 3), {"d": 1})
    assert r.replace(
        1, (1, 2, 3), {"d": 2}
    ) == (2, (1, 2, 3), {"d": 1})
    assert r.replace(1, (1, 2, 3, 4), {}) == (4, (1, 2, 3, 1), {})
    assert r.replace(1, (1, 2, 3, 4), {"d": 2}) == (2, (1, 2, 3, 1), {})



# Generated at 2022-06-14 13:06:00.407055
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class Test(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Test

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return cls

    t1 = Test()
    assert isinstance(t1, Test)
    @add_metaclass(ConfigurableMetaclass)
    class Test(object):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Test

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return cls

    t2 = Test()

# Generated at 2022-06-14 13:06:12.780976
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(x, y, z):
        pass
    assert ArgReplacer(foo, 'x').get_old_value((1,2,3), {}) == 1
    assert ArgReplacer(foo, 'y').get_old_value((1,2,3), {}) == 2
    assert ArgReplacer(foo, 'z').get_old_value((1,2,3), {}) == 3
    assert ArgReplacer(foo, 'x').get_old_value((1,2,3), {}, default=5) == 1
    assert ArgReplacer(foo, 'y').get_old_value((1,2,3), {}, default=5) == 2
    assert ArgReplacer(foo, 'z').get_old_value((1,2,3), {}, default=5) == 3
    assert ArgReplacer

# Generated at 2022-06-14 13:06:24.647925
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    from tornado.escape import native_str

    class Foo(Configurable):
        def _initialize(self, name):
            # type: (str) -> None
            self.name = name

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Foo

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return Foo

    class Bar(Foo):
        def _initialize(self, name, x):
            # type: (str, int) -> None
            super(Bar, self)._initialize(name)
            self.x = x


# Generated at 2022-06-14 13:06:45.058013
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_function(a, b, c):
        return a + b + c

    arg_replacer = ArgReplacer(test_function, 'a')
    old_value = arg_replacer.get_old_value((2, 3, 4), {})
    assert old_value == 2
    new_value = 5
    _, args, kwargs = arg_replacer.replace(new_value, (2, 3, 4), {})
    assert args == (5, 3, 4)

# Generated at 2022-06-14 13:06:50.988033
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import functools

    class StartupHandler(Configurable):
        def configurable_base(self):
            return StartupHandler  # type: ignore

        def configurable_default(self):
            return StartupHandler  # type: ignore

        def initialize(self, application):
            self.application = application

        # Ensure that class initialization happens exactly once per class
        # by storing a counter of the number of times each subclass is
        # seen.
        _class_counter = Counter()

        def __init__(self):
            # type: () -> None
            self._class_counter[type(self)] += 1

        @classmethod
        def num_instances_for_test(cls, class_):
            return cls._class_counter[class_]


# Generated at 2022-06-14 13:06:52.983478
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    d = ObjectDict()
    d.__getattr__('foo')

# Generated at 2022-06-14 13:06:56.885018
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    Configurable.configure("tornado.test.test_util.MockConfigurable1")
    b = Configurable()
    assert b.__class__ == MockConfigurable1
    x = MockConfigurable1()
    assert b == x



# Generated at 2022-06-14 13:07:02.349242
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class C(Configurable):
        @classmethod
        def configurable_base(cls):
            return C

        @classmethod
        def configurable_default(cls):
            return C

        def initialize(self, a: str, b: int) -> None:
            pass

    C.configure(None)
    c = C("a", 5)



# Generated at 2022-06-14 13:07:08.490561
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def dummy_function(a, b, c):
        pass
    a = ArgReplacer(dummy_function, "a")
    args = (1, 2, 3)
    # Replace the first positional argument
    old_value = a.get_old_value(args, {})
    assert old_value == 1
    # Check that the function works when the argument is not passed.
    old_value = a.get_old_value((1,), {"b": 2, "c": 3})
    assert old_value == 1

# Generated at 2022-06-14 13:07:17.830532
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import tornado.gen
    import tornado.httpserver
    import tornado.platform.twisted
    import tornado.platform.asyncio
    import tornado.platform.select
    tornado.httpserver.HTTPServer
    tornado.gen.IOLoop.configure(
        tornado.platform.twisted.TwistedIOLoop
    )
    tornado.ioloop.IOLoop.instance().close()
    tornado.httpserver.HTTPServer
    tornado.gen.IOLoop.configure(
        tornado.platform.asyncio.AsyncIOLoop
    )
    tornado.ioloop.IOLoop.instance().close()
    tornado.httpserver.HTTPServer
    tornado.gen.IOLoop.configure(
        tornado.platform.select.SelectIOLoop
    )
    tornado.ioloop.IOLoop.instance

# Generated at 2022-06-14 13:07:26.952496
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    YOUR_CONFIGURABLE_CLASS = Configurable()
    YOUR_IMPL_CLASS = Configurable()
    YOUR_CONFIGURABLE_CLASS = Configurable.configurable_base()
    YOUR_CONFIGURABLE_CLASS = Configurable.configurable_default()

# Generated at 2022-06-14 13:07:31.252791
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"

    def func(a, b=None, c=12, *args, **kwargs):
        pass

    arg_replacer = ArgReplacer(func, "c")
    assert arg_replacer.arg_pos == 2
    old_c, args, kwargs = arg_replacer.replace(c, func(a, b, d, e, f, c=c), e, f=f)
    assert old_c == 12
    assert args == (a, b, d, e, f)
    assert kwargs == {"c": c, "f": f}



# Generated at 2022-06-14 13:07:43.395048
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # Ensure that initialize() is called even if the __init__ method is
    # overridden.  This is necessary because the super() call in
    # Configurable.__new__ always calls initialize(), even though the
    # method it actually executes is not necessarily Configurable's
    # initialize().
    #
    # This test is also a test of _initialize() itself.

    def check_initialize(x):
        if not isinstance(x, Foo):
            raise AssertionError("expected Foo instance")
        if x.args != (3, 4):
            raise AssertionError("expected args=(3, 4)")

    class Foo(Configurable):
        @classmethod
        def configurable_base(cls):
            return FooBase

        @classmethod
        def configurable_default(cls):
            return Foo


# Generated at 2022-06-14 13:08:17.285417
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    """
    Test Configurable.__new__ method
    """
    class MyConfig(Configurable):
        def initialize(self, foo):
            # type: (str) -> None
            self.foo = foo

    MyConfig.configure("tornado.test.test_util.MyConfigImpl")

    assert type(MyConfig("foo")) == MyConfigImpl



# Generated at 2022-06-14 13:08:28.681871
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # Test Configurable.initialize
    class Impl1(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Impl1

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return Impl1

        def initialize(self, arg0, arg1, kwarg0=None, **kwargs):
            # type: (int, int, Optional[int], Any) -> None
            self.arg0 = arg0
            self.arg1 = arg1
            self.kwarg0 = kwarg0
            super().initialize(**kwargs)

    i = Impl1(0, 1)
    assert i.arg0 == 0
    assert i.arg1 == 1
    assert i

# Generated at 2022-06-14 13:08:39.538563
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        def initialize(self):
            pass

        def set_extra_param(self, extra_param):
            self.extra_param = extra_param

        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return A

    class B(A):
        def set_b_param(self, b_param):
            self.b_param = b_param

    class C(B):
        def set_c_param(self, c_param):
            self.c_param = c_param

    class D(Configurable):
        def initialize(self):
            pass

        @classmethod
        def configurable_base(cls):
            return D


# Generated at 2022-06-14 13:08:47.275350
# Unit test for method __new__ of class Configurable

# Generated at 2022-06-14 13:08:57.182030
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():   
    class TestConfigurable(Configurable):
        def __init__(self,thing):
            self.thing = thing
        def configurable_base(self):
            return TestConfigurable
        def configurable_default(self):
            return TestConfigurable
        def initialize(self,thing):
            self.thing = thing
        def get_thing(self):
            return self.thing
    class TestConfigurableTwo(TestConfigurable):
        def __init__(self,thing,two):
            self.thing = thing
            self.two = two
        def initialize(self,thing,two):
            self.thing = thing
            self.two = two
        def get_two(self):
            return self.two
    TestConfigurable.configure("TestConfigurableTwo",two=2)
    a = TestConfigurable("Test")


# Generated at 2022-06-14 13:09:09.212893
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Unconfigured(Configurable):
        def initialize(self):
            pass
        def __init__(self):
            pass
        @classmethod
        def configurable_base(cls):
            return cls
        @classmethod
        def configurable_default(cls):
            return None
    Unconfigured()
    Unconfigured.configure(None)
    class Configured(Unconfigured):
        def initialize(self, x):
            pass
        def __init__(self, x):
            pass
        @classmethod
        def configurable_default(cls):
            return cls
    Configured(1)

    # If a subclass is configured, it calls super() instead of cls()
    # (super() goes through the mro and finds Unconfigured).

# Generated at 2022-06-14 13:09:22.221285
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class DummyConfigurable(Configurable):
        def initialize(self, a, b=None, c=None):
            assert a == "a"
            assert b == "b"
            assert c == "c"

        @classmethod
        def configurable_base(cls):
            return DummyConfigurable

        @classmethod
        def configurable_default(cls):
            return DummyConfigurable

    DummyConfigurable.configure(impl=None)
    DummyConfigurable("a", b="b", c="c")
    DummyConfigurable(a="a", b="b", c="c")
    try:
        DummyConfigurable("a", "b", "c")
    except TypeError as e:
        assert isinstance(e, TypeError)

# Generated at 2022-06-14 13:09:28.365192
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class C (Configurable):
        @classmethod
        def configurable_base(cls):
            return C
        @classmethod
        def configurable_default(cls):
            return C
    c = C()
    assert c._initialize('a','b') == None
    assert hasattr(c,'a') == True
    assert hasattr(c,'b') == True
    assert hasattr(c,'args') == False

    class F (C):
        def __init__(self, *args, **kwargs):
            super(F,self).__init__(*args, **kwargs)
    f = F()
    assert f.initialize() == None


# Generated at 2022-06-14 13:09:35.928403
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    @ArgReplacer("name")
    def function(a, name=None):
        return "a", a, "name", name
    
    assert function.get_old_value((1,), {}, None) == None
    assert function.get_old_value((1,), {"name":2}, None) == 2
    assert function.get_old_value((1,2), {}, None) == 2
    assert function.get_old_value((1,2), {"name":3}, None) == 2



# Generated at 2022-06-14 13:09:42.979851
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class MyConfigurable(Configurable):
        def configurable_base():
            return MyConfigurable
        def configurable_default():
            return MySubclass

    class MySubclass(MyConfigurable):
        def initialize(self, init_arg):
            self.init_arg = init_arg

    assert issubclass(MySubclass, MyConfigurable)
    x = MyConfigurable(init_arg=1)
    assert isinstance(x, MyConfigurable)
    assert isinstance(x, MySubclass)
    assert x.init_arg == 1
    assert str(x) == "<MySubclass>"



# Generated at 2022-06-14 13:10:18.660102
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class MyConfigurable(Configurable):
        def configurable_base(self):
            # type: () -> Type[Configurable]
            return MyConfigurable
        def configurable_default(self):
            # type: () -> Type[Configurable]
            return MyDefaultConfigurable
        def initialize(self):
            # type: () -> None
            pass
    class MyDefaultConfigurable(MyConfigurable):
        pass
    class MyOtherConfigurable(MyConfigurable):
        pass
    MyConfigurable.configure(MyOtherConfigurable)
    assert MyConfigurable() is not None



# Generated at 2022-06-14 13:10:29.420477
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Test1(Configurable):
        def configurable_base(cls):
            return None

        def configurable_default(cls):
            return None

        def __init__(self):
            self.__init__

    try:
        Test1()
    except NotImplementedError:
        pass
    else:
        raise Exception("Failed")

    class Test2(Configurable):
        def configurable_base(cls):
            return None

        def configurable_default(cls):
            return None

    try:
        Test2()
    except NotImplementedError:
        pass
    else:
        raise Exception("Failed")


# Generated at 2022-06-14 13:10:35.910325
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from cortex.lib.types import (
        DecodeError,
        EncodeError,
        StreamClosedError,
        WebSocketError,
        WebSocketProtocolError,
    )

    configurable_base = Configurable.configurable_base
    assert configurable_base(DecodeError) is DecodeError
    assert configurable_base(EncodeError) is EncodeError
    assert configurable_base(StreamClosedError) is StreamClosedError
    assert configurable_base(WebSocketError) is WebSocketError
    assert configurable_base(WebSocketProtocolError) is WebSocketProtocolError



# Generated at 2022-06-14 13:10:43.566790
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Test(Configurable):
        @classmethod
        def configurable_base(cls):
            return Test

        @classmethod
        def configurable_default(cls):
            return Test

        def initialize(self, a=0, b=0):
            self.a = a
            self.b = b

    # Testing instance creation
    a = Test()
    assert a.a == a.b == 0
    a = Test(1, 2)
    assert a.a == 1 and a.b == 2

    # Testing configuration
    with pytest.raises(ValueError):

        class SubClass(Test):
            pass

        Test.configure(SubClass)

    class SubClass(Test):
        @classmethod
        def configurable_base(cls):
            return SubClass
    orig_impl_class,

# Generated at 2022-06-14 13:10:53.226737
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    #
    # In order to test the method replace of class ArgReplacer,
    # we need to build a simple function with some arguments
    # to pass to the ArgReplacer.
    #
    def foo(a, b, name="no name"):
        return a, b, name
    #
    # We will test the method with a few different values
    # in order to check the different cases
    #
    args1 = (1,2)
    kwargs1 = {"name": "none"}
    args2 = (1,)
    kwargs2 = {'b': 2, "name": "none"}
    args3 = (1,)
    kwargs3 = {}
    args4 = ()
    kwargs4 = {'b': 2, "name": "none"}
    

# Generated at 2022-06-14 13:11:03.926846
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    old = Configurable.configured_class()

    class Impl1(Configurable):
        def initialize(self, arg):
            pass

        @classmethod
        def configurable_base(cls):
            return Configurable

        @classmethod
        def configurable_default(cls):
            return ImplDefault

    class Impl2(Configurable):
        def initialize(self, arg):
            pass

        @classmethod
        def configurable_base(cls):
            return Configurable

        @classmethod
        def configurable_default(cls):
            return ImplDefault

    class ImplDefault(Configurable):
        def initialize(self, arg):
            pass

        @classmethod
        def configurable_base(cls):
            return Configurable

        @classmethod
        def configurable_default(cls):
            return Impl

# Generated at 2022-06-14 13:11:04.822759
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass


# Generated at 2022-06-14 13:11:08.664531
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    with mock.patch('tornado.util.Configurable.initialize') as mocked_initialize:
        mocked_initialize.return_value = None
        configurable = Configurable()
        assert configurable.initialize == mocked_initialize


# Generated at 2022-06-14 13:11:18.748647
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func_for_unit_test_ArgReplacer_replace(arg1, arg2, a: int = 0, b: int = 1):
        pass
    a_val_for_unit_test_ArgReplacer_replace, b_val_for_unit_test_ArgReplacer_replace = 2, 3
    args_for_unit_test_ArgReplacer_replace = (1, 2, 3)
    kwargs_for_unit_test_ArgReplacer_replace = {"a": a_val_for_unit_test_ArgReplacer_replace, "b": b_val_for_unit_test_ArgReplacer_replace}
    arg_replacer = ArgReplacer(func_for_unit_test_ArgReplacer_replace, "a")
    old_val, args, kwargs = arg_replacer.replace

# Generated at 2022-06-14 13:11:25.755659
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class ABC(Configurable):

        @classmethod
        def configurable_base(cls):
            return ABC

        @classmethod
        def configurable_default(cls):
            return ABCImpl

        def __init__(self, *args, **kwargs):
            pass

    class ABCImpl(ABC):
        pass

    ABCImpl.configure(ABCImpl)

    class ABCImpl2(ABC):
        pass

    ABC.configure(ABCImpl2, param1=1)
