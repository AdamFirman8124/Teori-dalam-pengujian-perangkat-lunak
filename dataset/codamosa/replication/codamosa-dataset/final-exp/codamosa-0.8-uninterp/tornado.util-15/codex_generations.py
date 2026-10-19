

# Generated at 2022-06-14 13:01:37.656109
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise IOError(0)
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise IOError(0, "arg")
    except Exception as e:
        assert errno_from_exception(e) == 0
    try:
        e = IOError()
        e.errno = 1
        raise e
    except Exception as e:
        assert errno_from_exception(e) == 1
    try:
        e = IOError()
        e.args = (1, "arg")
        raise e
    except Exception as e:
        assert errno_from_exception(e) == 1


# Generated at 2022-06-14 13:01:48.856212
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    assert hasattr(Configurable, 'initialize') and callable(Configurable.initialize)
    configurable_base = Configurable.configurable_base
    Configurable.configurable_base = lambda cls: cls
    Configurable.configured_class = lambda cls: Configurable
    TestClass = Configurable.__new__(Configurable)
    args = (1, 2, 3)
    kwargs = {'a': 1, 'b': 2, 'c': 3}
    TestClass.initialize(*args, **kwargs)
    assert TestClass.initialize.__closure__[0].cell_contents is TestClass._initialize
    assert TestClass.__dict__['_args'] == args
    assert TestClass.__dict__['_kwargs'] == kwargs
    TestClass = Configurable.__new__

# Generated at 2022-06-14 13:01:58.690578
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    import unittest

    class MyClass(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return MyClass

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return DefaultClass

        def initialize(self, a, b=1, **kwargs):
            # type: (int,int,**Any) -> None
            self.a = a
            self.b = b
            self.kwargs = kwargs

    class DefaultClass(MyClass):
        pass

    class SpecializedClass(MyClass):
        pass

    class ConfiguredClass(MyClass):
        pass

    # Test the default class.

# Generated at 2022-06-14 13:01:59.281168
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    pass

# Generated at 2022-06-14 13:02:08.098973
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a: str, b: str = "str b"):
        return "a={} b={}".format(a, b)
    replacer = ArgReplacer(f, "a")
    assert "a=AA b=str b" == f("AA")
    assert "a=AA b=BB" == f("AA", "BB")
    assert replacer.get_old_value(args=("AA",), kwargs=dict()) == "AA"
    assert replacer.get_old_value(args=("AA",), kwargs={"b": "BB"}) == "AA"
    assert replacer.get_old_value(args=(), kwargs={"a": "AA", "b": "BB"}) == "AA"

# Generated at 2022-06-14 13:02:11.763114
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class ConcreteClass(Configurable):
        def _initialize(self):
            super()._initialize()
            self.initialize_called = True
    instance = ConcreteClass()
    assert instance.initialize_called

# Generated at 2022-06-14 13:02:20.655264
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(a, b):
        return a, b

    arg_replacer1 = ArgReplacer(foo, 'a')
    old_value1, args, kwargs = arg_replacer1.replace(1, [2], {})
    print(args)
    print(kwargs)
    print(old_value1)

    def bar(a, b, *, c=3):
        return a, b, c

    arg_replacer2 = ArgReplacer(bar, 'b')
    old_value2, args1, kwargs1 = arg_replacer2.replace(21, [2], {})
    print(args1)
    print(kwargs1)
    print(old_value2)

    def baz(a, b, c, **d):
        return a, b, c,

# Generated at 2022-06-14 13:02:32.456277
# Unit test for function import_object
def test_import_object():
    test_objects = {
        'os': os,
        'tornado.escape': typing.cast(
            ModuleType, sys.modules.get("tornado.escape", None)),
        'tornado.escape.xhtml_escape': tornado.escape.xhtml_escape,
    }
    for name, obj in test_objects.items():
        # it's important to use import_object in the test too,
        # because we want to test import_object itself.
        assert import_object(name) is obj
        assert import_object(name) is obj

    assertRaises(ImportError, import_object, "missing_module")

    # Overwrite an imported module to prove that import_object isn't
    # just getting it from sys.modules.
    sys.modules["os"] = None

# Generated at 2022-06-14 13:02:37.191185
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    class A(object):
        def foo(self, a, b, c, x=1, y=2, z=3):
            return a, b, c, x, y, z

        @staticmethod
        def static(a, b, c, x=1, y=2, z=3):
            return a, b, c, x, y, z

    ar = ArgReplacer(A.foo, "y")
    assert ar.replace(100, (1, 2, 3), {"z": 4}) == (2, (1, 2, 3), {"z": 4})
    assert ar.replace(100, (1, 2, 3), {"z": 4, "t": 5}) == (2, (1, 2, 3), {"z": 4, "t": 5})

# Generated at 2022-06-14 13:02:47.683407
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    # 1, keyword argument
    def f(a,b,c):
        pass
    argr = ArgReplacer(f,"a")
    assert argr.get_old_value((1,2,3),{"a":5,"b":6,"c":7})==5
    assert argr.get_old_value((1,2,3),{"b":6,"c":7})==1
    assert argr.get_old_value((1,2,3),{"b":6,"c":7},default=None)==1
    # 2, positional argument
    def g(a:int,b:int,c:int):
        pass
    argr = ArgReplacer(g,"b")
    assert argr.get_old_value((1,2,3),{"a":5,"b":6,"c":7})

# Generated at 2022-06-14 13:03:05.074806
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest

    class A(Configurable):
        
        def __new__(cls):
            return object.__new__(cls)
    class B(A):
        pass
    class C(B):
        pass
    class D(Configurable):
        pass
    class E(Configurable):
        pass
    #C.configure(D)
    #print(C.configured_class())
    #if we dont call configure we will get an error
    #b = B()
    #print(b.__class__)  # <class '__main__.A'>
    #d = D()
    #print(d.__class__)  # <class '__main__.D'>
    # A.configure(D)
    #e = D()
    #print(e)
    #

# Generated at 2022-06-14 13:03:11.020980
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_function_1(arg1, kwarg1=None):
        return

    ar = ArgReplacer(test_function_1, "arg1")
    args = (123,)
    kwargs = {}
    assert ar.get_old_value(args, kwargs) == 123

    # If the argument is not present, get_old_value returns the default
    assert ar.get_old_value(args, kwargs, 123) == 123

    def test_function_2(arg1, kwarg1=None):
        return

    ar = ArgReplacer(test_function_2, "kwarg1")
    args = (123,)
    kwargs = {}
    assert ar.get_old_value(args, kwargs) is None



# Generated at 2022-06-14 13:03:24.200109
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def foo(a):
        pass
    def bar(a,b):
        pass

    replacer_foo = ArgReplacer(foo, "a")
    assert replacer_foo.arg_pos == 0

    replacer_bar = ArgReplacer(bar, "b")
    assert replacer_bar.arg_pos == 1

    assert replacer_foo.get_old_value((1,),{},None) == 1
    assert replacer_foo.get_old_value([1],[],None) == 1

    assert replacer_foo.get_old_value((1,),{},2) == 1
    assert replacer_foo.get_old_value([1],[],2) == 1

    assert replacer_foo.get_old_value((),{"a":1},None) == 1

# Generated at 2022-06-14 13:03:32.317766
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    type_name, method_name = "Configurable", "__new__"
    print("Testing %s.%s ..." % (type_name, method_name))
    test_obj = Configurable()
    try:
        test_obj.configurable_base()
    except NotImplementedError:
        print("%s.%s passed" % (type_name, method_name))
    else:
        print("%s.%s failed" % (type_name, method_name))

# Generated at 2022-06-14 13:03:41.350602
# Unit test for method __new__ of class Configurable

# Generated at 2022-06-14 13:03:43.145689
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    try:
        ObjectDict.__getattr__(ObjectDict(), 'a')
    except AttributeError as e:
        assert e.args == ('a',)


# Generated at 2022-06-14 13:03:54.009690
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # test ArgReplacer.replace by calling it on the function we're wrapping
    import functools
    import mock
    import tornado.testing
    
    def func(foo=None, bar=None):
        # here is a function with mixed positional and keyword args.
        # callable is a keyword-only argument
        return foo, bar
    func = functools.partial(func, "original_foo")

    replacer = ArgReplacer(func, "bar")
    old_value, args, kwargs = replacer.replace("new_bar", (), {})
    assert old_value is None
    assert args == ("original_foo",)
    assert kwargs == {"bar": "new_bar"}

    old_value, args, kwargs = replacer.replace("new_bar", ("new_foo",), {})
   

# Generated at 2022-06-14 13:04:05.929529
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c, d):
        pass
    arg = ArgReplacer(func, "c")
    assert arg.get_old_value(("a1","b1","c3","d3"),{"e":"e1","a":"a2","b":"b2"}) == "c3", "ArgReplacer get_old_value: assert1"
    assert arg.get_old_value(("a1","b1","c3","d3"),{"e":"e1","a":"a2","b":"b2"}, "default") == "c3", "ArgReplacer get_old_value: assert2"

# Generated at 2022-06-14 13:04:09.602794
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    a = Configurable()

    print(a.__class__.configurable_base())
    print(a.__class__.configurable_default())




# Generated at 2022-06-14 13:04:21.091677
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Check that we can instantiate a configurable class

    class Base(Configurable):
        def configurable_base(self):
            return Base

        def configurable_default(self):
            return Base

    base = Base()  # type: ignore
    assert isinstance(base, Base)

    # Check that we can call configure.
    # TODO: check that it works and actually configures something.
    class Configured(Base):
        pass

    Base.configure(Configured, arg='value')

    # Check that we can configure a subclass.
    # TODO: check that we actually instantiate a Configured instance.
    class SubBase(Base):
        pass

    subbase = SubBase()  # type: ignore
    assert isinstance(subbase, SubBase)

# Generated at 2022-06-14 13:04:57.435010
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A1(Configurable):  # type: ignore
        Configurable_configured_class = None  # type: Optional[Type[Configurable]]
        Configurable_configurable_base = None
        Configurable_configurable_default = None
        def __init__(self, *args: Any, **kwargs: Any):
            pass  # pragma: nocover
        def initialize(self, *args: Any, **kwargs: Any) -> None:
            pass
        def configurable_base(cls: Type[Configurable]) -> Type[Configurable]:
            return cls
        def configurable_default(cls: Type[Configurable]) -> Type[Configurable]:
            return cls
        def class_method(cls: Type[Configurable], arg: Any) -> Any:
            pass

# Generated at 2022-06-14 13:05:06.079532
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f1(a, b: str, c='default_c') -> int:
        return int(a) + int(b)


# Generated at 2022-06-14 13:05:09.031026
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    test = ObjectDict()
    test['test'] = 1
    assert test.test == 1


# Generated at 2022-06-14 13:05:20.963270
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def fun(a,b,c=3,d=4,e=5):
        pass
    argreplacer = ArgReplacer(fun, 'e')
    # test case #1
    (old_value, args, kwargs) = argreplacer.replace(99, (1, 2), {'e':55, 'f':66})
    assert old_value == 55
    assert args == (1, 2)
    assert kwargs == {'e':99, 'f':66}
    # test case #2
    (old_value, args, kwargs) = argreplacer.replace(99, (1, 2, 3), {'e':55, 'f':66})
    assert old_value == 55
    assert args == (1, 2, 3)

# Generated at 2022-06-14 13:05:23.937677
# Unit test for function import_object
def test_import_object():
    # For examples, see docstring
    assert import_object("os") is os
    assert import_object("os.path") is os.path
    assert import_object("tornado.escape") is tornado.escape



# Generated at 2022-06-14 13:05:27.670048
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a, b, c, d=4):
        pass

    func = ArgReplacer(f,"b")
    assert func.get_old_value((1,2,3),{})==2


# Generated at 2022-06-14 13:05:33.774531
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # Replace only positional arguments
    def foo(a, b, c):
        print(a, b, c)

    def foo_new(x):
        print(x)

    arg_replacer = ArgReplacer(foo, "b")
    old_value, args, kwargs = arg_replacer.replace(
                                          foo_new,
                                          (1, foo, 3),
                                          {}
                                        )
    assert old_value == foo
    assert args == (1, foo_new, 3)
    assert kwargs == {}

    # Replace only keyword arguments
    def bar(a, b=2):
        print(a, b)

    def bar_new(x):
        print(x)

    arg_replacer = ArgReplacer(bar, "b")
    old_value, args

# Generated at 2022-06-14 13:05:45.806418
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(x, y, z):
        pass
    arg_replacer = ArgReplacer(f, "y")
    test_args = (1, 2, 3)
    test_kwargs = {"w": 1, "x": 2, "z": 3}
    test_default = "mydefault"

    # y is passed by position
    old_value = arg_replacer.get_old_value(test_args, test_kwargs)
    assert old_value == 2, "Failed to get old value passed by position"
    # y is passed by keyword
    old_value = arg_replacer.get_old_value((1, 3), test_kwargs)
    assert old_value == 2, "Failed to get old value passed by keyword"
    # y is omitted

# Generated at 2022-06-14 13:05:50.615442
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    class Test():
        def test(self, a, b, c):
            return a, b, c
    t = Test()
    args = (1, 2, 3)
    kwargs = {'d':4}
    p = ArgReplacer(t.test, 'b')
    assert p.replace(4, args, kwargs) == (2, (1, 4, 3), {'d': 4})
    assert p.replace(5, args, kwargs) == (2, (1, 5, 3), {'d': 4})

# Generated at 2022-06-14 13:05:56.668468
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c):
        pass

    argreplacer = ArgReplacer(func, 'c')
    args = ("test", 1, [1, 2, 3])
    kwargs = {'c': 'test2'}
    old_value = argreplacer.get_old_value(args, kwargs)
    assert old_value == "test2"


# Generated at 2022-06-14 13:06:22.637855
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError
    except IOError as e:
        assert errno_from_exception(e) is None
    try:
        raise IOError(1)
    except IOError as e:
        assert errno_from_exception(e) == 1



# Generated at 2022-06-14 13:06:33.367457
# Unit test for function import_object
def test_import_object():
    # common case: import a module
    import tornado.escape
    assert import_object("tornado.escape") is tornado.escape
    # import a module and then another object
    import tornado.escape
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8
    # import a function
    import tornado.escape
    assert import_object("tornado.escape.squeeze") is tornado.escape.squeeze
    # import a class
    import tornado.escape
    assert import_object("tornado.escape.RecursiveEncoder") is \
        tornado.escape.RecursiveEncoder
    # trailing dot is harmless
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8
    # import a module that's already loaded
    assert import_object("tornado") is tornado



# Generated at 2022-06-14 13:06:39.218161
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Impl(Configurable):
        def initialize(self, **kwargs):
            pass
        @classmethod
        def configurable_base(cls):
            return Impl
        @classmethod
        def configurable_default(cls):
            return Impl
    Impl.configure(None)
    assert isinstance(Impl(), Impl)
    



# Generated at 2022-06-14 13:06:41.220961
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass

# Generated at 2022-06-14 13:06:43.760886
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    class A(ObjectDict):
        def __getattr__(self, name: str) -> Any:
            return super().__getattr__(name)
    foo = A()
    foo['bar'] = True
    assert foo.bar

# Generated at 2022-06-14 13:06:50.538011
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise OSError(42, 'test')
    except OSError as e:
        assert errno_from_exception(e) == 42
    try:
        raise ValueError
    except ValueError as e:
        assert errno_from_exception(e) is None
    try:
        raise ValueError(42)
    except ValueError as e:
        assert errno_from_exception(e) == 42



# Generated at 2022-06-14 13:07:00.790596
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    set_log_level(logging.DEBUG)
    def a(a = None):
        assert a == 'a'
        return a + a
    def b(b = 'b'):
        assert b == 'b'
        return b + b
    def c(c):
        assert c == 'c'
        return c + c
    def d(d = 'd', e = None):
        assert d == 'd'
        assert e == 'e'
        return d + d + e + e
    def e(f, g = None):
        assert g == 'f'
        return f + g
    def f(g = None, h = None):
        assert g == 'g'
        assert h == 'h'
        return g + h

# Generated at 2022-06-14 13:07:04.739255
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class testConfig(Configurable):
        def initialize(self, *args, **kwargs):
            pass
        def configurable_base(self):
            return testConfig
        def configurable_default(self):
            return testConfig
    assert(isinstance(testConfig(), testConfig))

import functools



# Generated at 2022-06-14 13:07:16.232248
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a=1, b=2, c=3):
        return a + b + c
    assert ArgReplacer(f, 'a').get_old_value((1,), {}, 0) == 1
    assert ArgReplacer(f, 'b').get_old_value((1,), {}, 0) == 2
    assert ArgReplacer(f, 'c').get_old_value((1,), {}, 0) == 3
    assert ArgReplacer(f, 'a').get_old_value((1, 2, 3), {}, 0) == 1
    assert ArgReplacer(f, 'b').get_old_value((1, 2, 3), {}, 0) == 2
    assert ArgReplacer(f, 'c').get_old_value((1, 2, 3), {}, 0) == 3
    assert Arg

# Generated at 2022-06-14 13:07:20.704901
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError(5)
    except Exception as e:
        assert errno_from_exception(e) == 5
    try:
        raise IOError("lorem")
    except Exception as e:
        assert errno_from_exception(e) == "lorem"



# Generated at 2022-06-14 13:07:41.518085
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    a = ArgReplacer(int, 'base')
    #args, kwargs are empty
    assert a.get_old_value((), {}, -1) == -1
    #arguments included key
    assert a.get_old_value((), {'base':10}, -1) == 10
    #arguments included key and position
    assert a.get_old_value((10,), {'base':20}, -1) == 10


# Generated at 2022-06-14 13:07:52.858457
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import types
    cls = types.ModuleType("cls")
    globals()['cls'] = cls
    globals()['args'] = 1
    globals()['kwargs'] = 2
    globals()['instance'] = 3
    cls.__new__ = types.FunctionType(
        _b("""
        def __new__(self, *args, **kwargs):
            self.__new___called = True
            self.args = args
            self.kwargs = kwargs
            return args, kwargs  # force non-return of an instance
        """),
        globals()
    )

# Generated at 2022-06-14 13:08:00.144613
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class DummyConfigurable(Configurable):
        def configurable_base(cls):
            return DummyConfigurable
        def configurable_default(cls):
            return 3
        def __new__(cls, *args, **kwargs):
            return 1
        def initialize(cls, *args, **kwargs):
            return 2
    a = DummyConfigurable(1,2,3)
    assert a == 1
    assert DummyConfigurable.initialize(1,2,3) == 2



# Generated at 2022-06-14 13:08:06.636130
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    import nose
    import nose.tools as nt

    def returns(a, b, c=3, *args, **kwargs):
        return (a, b, c, args, kwargs)

    def test(a, b, c=3, *args, **kwargs):
        # Test the default case: name is not in args or kwargs
        nt.assert_equal(ArgReplacer(test, "foo").get_old_value((a, b), kwargs), None)

        # Test when the name is passed by position
        nt.assert_equal(ArgReplacer(test, "a").get_old_value((a, b), kwargs), a)

        # Test when the name is passed by keyword
        kwargs["b"] = b

# Generated at 2022-06-14 13:08:16.713756
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None

    class MyClass(Configurable):
        @classmethod
        def configurable_base(kls):
            return kls

        @classmethod
        def configurable_default(kls):
            return kls

        def initialize(self, x):
            pass

        def __init__(self, x):
            pass

    def get_args(obj):
        # type: (Configurable) -> Tuple[Any, ...]
        if isinstance(obj, tuple):
            # CPython, PyPy
            return obj[0].__self__, obj[1]
        else:
            # Jython
            return obj[0].__self__, obj[1:]

    assert get_args(MyClass(1)) == (MyClass, 1)

    # Make sure configure works properly

# Generated at 2022-06-14 13:08:24.898578
# Unit test for function errno_from_exception
def test_errno_from_exception():
    class MyError(Exception):
        def __init__(self, errno, strerror):
            self.args = (errno, strerror)
            self.errno = errno
            self.strerror = strerror
        def __str__(self):
            return 'MyError: %d, %s' % (self.errno, self.strerror)
    try:
        raise MyError(1, 'foo')
    except Exception as e:
        assert errno_from_exception(e) == 1



# Generated at 2022-06-14 13:08:36.151344
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    from typing import Dict, Any
    # Unit test for method __new__ of class Configurable(class)
    class MockConfigurable(typing.Generic[Any], Configurable):
        @classmethod
        def configurable_base(cls):
            return MockConfigurable
        @classmethod
        def configurable_default(cls):
            return MockConfigurable
        @classmethod
        def configure(cls, impl, **kwargs):
            pass
        @classmethod
        def configured_class(cls):
            return MockConfigurable
        @classmethod
        def _save_configuration(cls):
            return (None, {})
        @classmethod
        def _restore_configuration(cls, saved):
            pass

# Generated at 2022-06-14 13:08:44.962225
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test(a, b=3, *args, **kwargs):
        pass
    arg_replacer1 = ArgReplacer(test, 'a')
    assert arg_replacer1.get_old_value((1, 2,), {}) == 1
    assert arg_replacer1.get_old_value((), {'a':1}) == 1
    assert arg_replacer1.get_old_value((), {}) == None
    assert arg_replacer1.get_old_value((), {}, 0) == 0
    arg_replacer2 = ArgReplacer(test, 'b')
    assert arg_replacer2.get_old_value((1,), {}) == 3
    assert arg_replacer2.get_old_value((), {'b':2}) == 2

# Generated at 2022-06-14 13:08:55.628605
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    from unittest.mock import Mock
    class Foo(Configurable):
        @classmethod
        def configurable_base(cls):
            return Foo
        @classmethod
        def configurable_default(cls):
            return A
        def initialize(self):
            pass
        def do_stuff(self):
            pass
    class A(Foo):
        def do_stuff(self):
            return 1
    class B(Foo):
        def do_stuff(self):
            return 2
    class TestConfigurable(unittest.TestCase):
        def test_instance_is_correct_class(self):
            Foo.configure(impl=A)
            self.assertTrue(isinstance(Foo(), A))
            Foo.configure(impl=B)

# Generated at 2022-06-14 13:09:07.775016
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a, b, c=None, d=4, *args, **kwargs):
        pass
    r = ArgReplacer(f, "c")
    assert r.get_old_value((1,2), {}) == None
    assert r.get_old_value((1, 2, 3), {}) == 3
    assert r.get_old_value((1,2), {'c':3}) == 3
    assert r.get_old_value((1, 2, 3), {'c': 4}) == 3
    assert r.get_old_value((1, 2, 3, 4), {'d': 0}) == 3
    assert r.get_old_value((1, 2, 3), {'c': 4, 'd': 0}) == 3

# Generated at 2022-06-14 13:09:32.751105
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_func(foo, bar=1): pass
    arg_replacer = ArgReplacer(test_func, 'bar')

    foo_arg = object()
    result = arg_replacer.get_old_value((foo_arg, ), {}, 3)
    assert result == 1

    result = arg_replacer.get_old_value(('', ), {}, 3)
    assert result == 1

    result = arg_replacer.get_old_value((), {'bar': 1}, 3)
    assert result == 1

    result = arg_replacer.get_old_value((), {'bar': 4}, 3)
    assert result == 4

    result = arg_replacer.get_old_value(('', ), {}, 3)
    assert result == 1

    result = arg_replacer.get_old_value

# Generated at 2022-06-14 13:09:42.153706
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():

    def func(a, b, c=1, d=2):
        pass

    r = ArgReplacer(func, "a")
    assert r.get_old_value((1, 2, 3, 4), {}) == 1
    assert r.get_old_value((1, 2, 3, 4), {}, default=99) == 1
    assert r.get_old_value((1, 2, 3), {}, default=99) == 1
    assert r.get_old_value((1, 2, 3), {}) == 1
    assert r.get_old_value((1, 2, 3), {}, default=99) == 1
    assert r.get_old_value((1, 2, 3), {}, default=None) == 1


# Generated at 2022-06-14 13:09:50.481150
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def original_func(p, *, a=1, b=2):
        return p, a, b

    old_value, args, kwargs = ArgReplacer(original_func, 'a').replace(
        9, (1,), {'b':3})
    assert old_value==1
    assert args==(1,)
    assert kwargs=={'b': 3, 'a': 9}

    old_value, args, kwargs = ArgReplacer(original_func, 'a').replace(
        9, (1,), {'a':3})
    assert old_value==3
    assert args==(1,)
    assert kwargs=={'a': 9, 'b': 2}


# Generated at 2022-06-14 13:10:02.361514
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(a, b, c=3, d=4):
        pass

    args = [1, 2]
    kwargs = {"d": None}
    r = ArgReplacer(foo, "d")
    assert r.replace(5, args, kwargs) == (None, [1, 2], {"d": 5})
    assert r.replace(6, args, kwargs) == (5, [1, 2], {"d": 6})
    args = (7, )
    kwargs = {"b": 8, "d": None}
    r = ArgReplacer(foo, "c")
    assert r.replace(9, args, kwargs) == (3, [7], {"b": 8, "c": 9, "d": None})
    assert r.replace(10, args, kwargs)

# Generated at 2022-06-14 13:10:06.389958
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        def configurable_base(self):
            return A
        def configurable_default(self):
            return A
        def func(self):
            return None
    A.configure(None)
    a = A()
    assert isinstance(a, A)
    assert a.func() is None


# Generated at 2022-06-14 13:10:19.162564
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def initialize(self, *x):
            pass

    class B(A):
        def initialize(self, *x):
            pass

    # configure and configure_async.
    A.configure(None)
    B.configure(None)

    assert A is A.configured_class()
    assert B is B.configured_class()

    A().initialize()
    B().initialize()

    A.configure(A)
    assert A is A.configured_class()

    A.configure(B)
    assert B is A.configured_class()
    assert B is B.configured_class()

    # Can't configure an unrelated class.
    with pytest.raises(ValueError):
        A.configure(int)

    # Can't configure with a

# Generated at 2022-06-14 13:10:24.953957
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



# Generated at 2022-06-14 13:10:34.163637
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestInstance(Configurable):
        def __init__(self, foo, bar, **kwargs):
            assert foo == 'foo'
            assert bar == 'bar'
            super(TestInstance, self).__init__(**kwargs)

    class TestClass(TestInstance):
        def initialize(self, foo, bar):
            assert foo == 'foo'
            assert bar == 'bar'
            assert kwargs == {}

    class TestConfigurable(Configurable):
        def initialize(self, foo, bar, **kwargs):
            assert foo == 'foo'
            assert bar == 'bar'
            assert kwargs == {}

        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestInstance


# Generated at 2022-06-14 13:10:40.014537
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    import oss2
    import logging
    log = logging.getLogger(__name__)
    arg_replacer = ArgReplacer(oss2.DefaultRetryPolicy.__init__, 'retry_mode')
    retry_mode_value = arg_replacer.get_old_value(('a', 'b', 'c', 'd', 'e'), {'retry_mode': 'a'})
    assert retry_mode_value == 'a'


# Generated at 2022-06-14 13:10:50.112880
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(a, x, y=10, z=20):
        return (a, x, y, z)
    old_value, args, kwargs = ArgReplacer('y', foo).replace(5, (1, 2), {})
    assert old_value == 10
    assert args == (1, 2)
    assert kwargs == {'y': 5}
    old_value, args, kwargs = ArgReplacer('z', foo).replace(5, (1, 2), {})
    assert old_value == 20
    assert args == (1, 2)
    assert kwargs == {'z': 5}
    old_value, args, kwargs = ArgReplacer('x', foo).replace(5, (1,), {})
    assert old_value == None
    assert args == (1,)
