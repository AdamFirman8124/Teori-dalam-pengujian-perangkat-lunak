

# Generated at 2022-06-14 13:01:53.929294
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Foo(Configurable):
        def configurable_base(self):
            return Foo
        def configurable_default(self):
            return Foo
        def _initialize(self):
            self.a = 'b'

    Foo.configure('test.test_utils.Foo', a='d')
    assert Foo().a == 'd'

# Generated at 2022-06-14 13:02:02.937979
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None

    def check_class(cls):
        # type: (Type[Configurable]) -> None
        class impl(cls):
            pass
        assert impl is cls.configured_class()
        instance = cls()
        assert isinstance(instance, impl)

    def check_class_and_kwargs(cls, **kwargs):
        # type: (Type[Configurable], **Any) -> None
        class impl(cls):
            pass
        cls.configure(impl, **kwargs)
        assert impl is cls.configured_class()
        instance = cls(**kwargs)
        assert isinstance(instance, impl)


# Generated at 2022-06-14 13:02:11.200795
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(x, y):
        return x + y

    a = ArgReplacer(func, 'x')
    assert a.arg_pos == 0
    assert a.get_old_value((1,2), {}) == 1
    old_value, args, kwargs = a.replace(2, (1,2), {})
    assert old_value == 1
    assert args == (2,2)
    assert kwargs == {}
    old_value, args, kwargs = a.replace(2, (1,), {'y':5})
    assert old_value is None
    assert args == (1,)
    assert kwargs == {'y':5, 'x':2}



# Generated at 2022-06-14 13:02:20.295404
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():

    def func(x, y, z=None):
        pass

    arep = ArgReplacer(func, 'y')
    assert arep.arg_pos == 1
    assert not 'y' in func.__code__.co_varnames
    assert 'z' in func.__code__.co_varnames

    # y is passed as a positional argument, replace it
    assert arep.replace(1, (2, 3), {}) == (3, (2, 1), {})
    # y is passed as a keyword argument, replace it
    assert arep.replace(1, (), {'y': 2}) == (2, (), {'y': 1})
    # y is passed as a positional and keyword argument, replace the positional one

# Generated at 2022-06-14 13:02:22.400739
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    o = ObjectDict(a=1)
    assert o.a == o['a']

# Generated at 2022-06-14 13:02:30.265831
# Unit test for function import_object
def test_import_object():
    # assert import_object("cStringIO") is cStringIO
    assert import_object("datetime") is datetime
    assert (import_object("collections.deque") is collections.deque)
    with pytest.raises(ImportError):
        import_object("tornado.missing_module")
    assert import_object("tornado") is tornado
    assert import_object("tornado.escape") is tornado.escape
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8



# Generated at 2022-06-14 13:02:39.169298
# Unit test for function import_object
def test_import_object():
    from tornado.options import define, options, parse_config_file
    import tornado.escape

    define('x', import_object('tornado.escape'))
    define('y', import_object('tornado.escape.utf8'))
    define('z', import_object('tornado'))
    parse_config_file('tornado/test/options_test.conf')
    assert options.x is tornado.escape
    assert options.y is tornado.escape.utf8
    assert options.z is tornado


# Fake unicode literal support:  Python 3.2 doesn't have the u'' marker for
# literal strings, and alternative solutions like "from __future__" break
# at least one tool that detects 2/3 compatibility.  u() can be applied
# to ascii strings that include \u escapes (but they must not contain
# literal non

# Generated at 2022-06-14 13:02:49.406328
# Unit test for function errno_from_exception
def test_errno_from_exception():
    class TestException(Exception):
        pass
    try:
        raise TestException()
    except Exception as e:
        assert errno_from_exception(e) is None

    errno_err = TestException("just a string")
    try:
        raise errno_err
    except Exception as e:
        assert errno_from_exception(e) is None

    errno_err = TestException("just a string")
    errno_err.errno = 42
    try:
        raise errno_err
    except Exception as e:
        assert errno_from_exception(e) == 42

    errno_err = TestException(42)
    try:
        raise errno_err
    except Exception as e:
        assert errno_from_exception(e) == 42



# Generated at 2022-06-14 13:03:01.527467
# Unit test for method initialize of class Configurable

# Generated at 2022-06-14 13:03:05.963914
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # prepare the data
    test_func = lambda x, y, z="z": (x, y, z)
    args = (1, 2, 3)
    kwargs = {"z": 4}
    ex_value = (2, 3, 4)
    # run the test
    replacer = ArgReplacer(test_func, "y")
    old_value, new_args, new_kwargs = replacer.replace(
        test_func(x=1, y=3, z=4), args=args, kwargs=kwargs
    )
    # extract the actual value
    (x, y, z) = test_func(*new_args, **new_kwargs)
    # check the actual value
    assert x == 1
    assert y == 3
    assert z == 4
    assert old_value == 2

# Generated at 2022-06-14 13:03:27.297187
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    '''
    test for two functions (with two inputs) and class ArgReplacer
    '''
    def func1(x, y):
        '''
        func1 has two inputs
        '''
        return x + y
    def func2(x, y, z):
        '''
        func2 has three inputs
        '''
        return x + y + z
    args1 = (1, 2)
    args2 = (1, 2, 3)
    test_obj_1 = ArgReplacer(func1, "x")
    test_obj_2 = ArgReplacer(func2, "x")
    assert test_obj_1.get_old_value(args1, {}) == 1
    assert test_obj_2.get_old_value(args2, {}) == 1
test_ArgReplacer_get

# Generated at 2022-06-14 13:03:37.639161
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f1(a, b, c = 'c'):
        pass

    assert ArgReplacer(f1, 'a').get_old_value(('a', 'b', 'c'), {}) == 'a'
    assert ArgReplacer(f1, 'b').get_old_value(('a', 'b', 'c'), {}) == 'b'
    assert ArgReplacer(f1, 'c').get_old_value(('a', 'b', 'c'), {}) == 'c'
    assert ArgReplacer(f1, 'a').get_old_value(('a', 'b'), {'c': 'c'}) == 'a'
    assert ArgReplacer(f1, 'c').get_old_value(('a', 'b'), {'c': 'c'}) == 'c'

    assert ArgRepl

# Generated at 2022-06-14 13:03:50.488028
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class a1(Configurable):
        def configurable_base(self):
            # type: () -> Type[Configurable]
            return a1

        def configurable_default(self):
            # type: () -> Type[Configurable]
            return a2

    class a2(a1):
        pass

    assert isinstance(a1(), a2)
    a1.configure(a1)
    assert isinstance(a1(), a1)

    class b1(Configurable):
        def configurable_base(self):
            # type: () -> Type[Configurable]
            return b1

        def configurable_default(self):
            # type: () -> Type[Configurable]
            return b2


# Generated at 2022-06-14 13:04:00.554010
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.web
    import tornado.platform.asyncio
    import tornado.platform.twisted

    Configurable.configure("tornado.platform.asyncio.AsyncIOMainLoop")
    server = tornado.httpserver.HTTPServer(tornado.web.Application())
    assert isinstance(server.ioloop, tornado.platform.asyncio.AsyncIOLoop)
    Configurable.configure("tornado.platform.twisted.TwistedIOLoop")
    server = tornado.httpserver.HTTPServer(tornado.web.Application())
    assert isinstance(server.ioloop, tornado.platform.twisted.TwistedIOLoop)
    Configurable.configure("tornado.platform.asyncio.AsyncIOMainLoop")

# Generated at 2022-06-14 13:04:03.877843
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def initialize(self, *args, **kwargs):
            pass
    assert A.configured_class() is A
    assert A.configure(None) is None

# Generated at 2022-06-14 13:04:05.138507
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    a = Configurable()
# Class tests for method initialize of class Configurable

# Generated at 2022-06-14 13:04:12.605844
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    class Foo(object):
        @classmethod
        def func(cls, arg, arg_pos=None, **kwargs):
            pass
        
    foo = Foo()
    # Test case - 1
    foo.func(5, arg=5, kwargs={"arg": 5, "kwargs": "kwargs"})
    # Test case - 2
    foo.func(5, kwargs={"arg": 5, "kwargs": "kwargs"})
    # Test case - 3
    foo.func(5, 5, kwargs={"arg": 5, "kwargs": "kwargs"})
    # Test case - 4
    foo.func(5, arg_pos=5, kwargs={"arg": 5, "kwargs": "kwargs"})
    # Test case - 5

# Generated at 2022-06-14 13:04:16.258052
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import doctest
    from tornado.util import Configurable
    failures, _ = doctest.testmod(Configurable)
    assert failures == 0

# Generated at 2022-06-14 13:04:21.636856
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    assert ArgReplacer.get_old_value(args = (),kwargs = {"kwargs1":"kwargs1"},default = "default")
    assert ArgReplacer.get_old_value(args = ("arg1","arg2",),kwargs = {"kwargs1":"kwargs1"},default = "default")
    assert ArgReplacer.get_old_value(args = ("arg1","arg2",),kwargs = {},default = "default")
    assert ArgReplacer.get_old_value(args = ("arg1","arg2","arg3"),kwargs = {},default = "default")

# Generated at 2022-06-14 13:04:33.362462
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    a = ArgReplacer(test_ArgReplacer_replace, name="new_value")
    i = [0]

    def f1(new_value):
        i[0] += 1

    def f2(old_value, new_value):
        assert old_value == 2
        i[0] += 1

    def f3(new_value, old_value=3):
        assert old_value == 3
        i[0] += 1

    def f4(old_value=1, new_value=2):
        i[0] += 1

    def f5(old_value=1, new_value=2):
        i[0] += 1

    def f6(*a, **kw):
        assert a == (1, 2, 3)
        assert kw["new_value"] == 4
        assert k

# Generated at 2022-06-14 13:05:01.935745
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import types
    # Make sure __new__ is static
    assert isinstance(Configurable.__new__, staticmethod)
    # Make sure __new__ is overrides the original one
    assert Configurable.__new__ != object.__new__
    # Make sure __new__ returns the right class
    assert isinstance(Configurable.__new__(Configurable), Configurable)
    assert isinstance(Configurable.__new__(Exception), Configurable)
    # Unit test for method __new__ of class Configurable
    def test_Configurable___new__():
        import types
        # Make sure __new__ is static
        assert isinstance(Configurable.__new__, staticmethod)
        # Make sure __new__ is overrides the original one
        assert Configurable.__new__ != object.__new__
        # Make sure __new__

# Generated at 2022-06-14 13:05:13.299728
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class MyConfig(Configurable):
        @classmethod
        def configurable_base(self):
            # type: () -> Type[Configurable]
            return MyConfig

        @classmethod
        def configurable_default(self):
            # type: () -> Type[Configurable]
            return MyDefaultImpl

    class MyDefaultImpl(MyConfig):
        def initialize(self):
            # type: () -> None
            pass

    class MyAltImpl(MyConfig):
        def initialize(self):
            # type: () -> None
            pass

    MyConfig.configure(MyAltImpl)
    instance = MyConfig()
    assert isinstance(instance, MyAltImpl)



# Generated at 2022-06-14 13:05:24.537921
# Unit test for function import_object
def test_import_object():
    import tornado.escape
    assert import_object('tornado.escape') is tornado.escape
    assert import_object('tornado.escape.utf8') is tornado.escape.utf8
    assert import_object('tornado') is tornado
    import sys
    import types
    try:
        import_object('tornado.missing_module')
    except ImportError:
        exc_info = sys.exc_info()
        assert isinstance(exc_info[1], ImportError)
    else:
        raise AssertionError()
    del sys.modules['tornado.escape']
    try:
        import_object('tornado.escape')
    except ImportError:
        exc_info = sys.exc_info()
        assert isinstance(exc_info[1], ImportError)
    else:
        raise AssertionError()




# Generated at 2022-06-14 13:05:34.041434
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import pytest
    from tornado.ioloop import IOLoop

    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            return Base

        @classmethod
        def configurable_default(cls):
            return BaseImpl

    class BaseImpl(Base):
        def initialize(self):
            self.foo = "foo called"

    ioloop_type = IOLoop.configured_class()

    class DummyImpl(ioloop_type):
        pass

    dummy_impl = DummyImpl()

    IOLoop.configure(DummyImpl)
    ioloop = IOLoop()
    assert ioloop.__class__ == DummyImpl
    IOLoop._restore_configuration(IOLoop._save_configuration())
    ioloop = IOLoop()

# Generated at 2022-06-14 13:05:43.701525
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A
        @classmethod
        def configurable_default(cls):
            return A1
        def initialize(self,a,b,c,d):
            pass
    class A1(A):
        def initialize(self,a,b,c,d):
            print("A1")
    a=A(1,2,3,4) # A.__new__ -> A1.__new__ -> A1.initialize(1,2,3,4)
    assert True # to see what was printed

# Generated at 2022-06-14 13:05:51.229940
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c):
        return a, b, c
    def func1(a, b, c, d):
        return a, b, c, d
    argreplacer = ArgReplacer(func, 'b')
    old, args, kwargs = argreplacer.replace('x', [1, 2, 3], {})
    assert (old, args, kwargs) == (2, [1, 'x', 3], {})

    old, args, kwargs = argreplacer.replace('x', [1, 2, 3], {'b':2})
    assert (old, args, kwargs) == (2, [1, 2, 3], {'b': 'x'})


# Generated at 2022-06-14 13:05:53.528857
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    __tracebackhide__ = True
    a = ObjectDict()
    a["a"] = 1
    assert a.a == 1

# Generated at 2022-06-14 13:06:02.126413
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(a, b, c=5, *args, **kwargs):
        pass

    argr = ArgReplacer(foo, "a")
    assert argr.get_old_value((3, 1, 2, 4), {}, default="foo") == 3
    # the argument "a" is passed by position
    argr = ArgReplacer(foo, "b")
    assert argr.get_old_value((0, 1, 2), {}, default="foo") == 1
    # the argument "b" is passed by position
    argr = ArgReplacer(foo, "c")
    assert argr.get_old_value((0, 1), {}, default="foo") == 5
    # the argument "c" is passed by keyword with value 5

# Generated at 2022-06-14 13:06:13.295739
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(arg1, arg2, arg3, arg4=None):
        pass

    class ArgReplacerTest():
        def __init__(self, name, new_value, expected_value, expected_args, expected_kwargs):
            self.name = name
            self.new_value = new_value
            self.expected_value = expected_value
            self.expected_args = expected_args
            self.expected_kwargs = expected_kwargs


# Generated at 2022-06-14 13:06:22.362300
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A
        @classmethod
        def configurable_default(cls):
            return A
        def initialize(self):
            pass
    import pytest
    with pytest.raises(NotImplementedError):
        A.configurable_base()
    with pytest.raises(NotImplementedError):
        A.configurable_default()
    a = A()
    assert isinstance(a, A)
    assert a.initialize is a._initialize


# Generated at 2022-06-14 13:07:00.023457
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b=0, c=1):
        print('a: {}, b: {}, c: {}'.format(a, b, c))
    ArgReplacer(f, 'b').replace(1, (1,), {'c': 3})


# Generated at 2022-06-14 13:07:08.957556
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # type: () -> None
    """Test the method replace of class ArgReplacer"""
    args = (1, 2, 3)
    kwargs = {"kwarg1": None, "kwarg2": None}

    # Test the case when the argument is passed by position
    def f_pos_arg(argpos, kwarg1, kwarg2):
        # type: (int, str, str) -> None
        pass

    replacer = ArgReplacer(f_pos_arg, "argpos")
    old_value, args, kwargs = replacer.replace(
        4, args, kwargs
    )
    assert old_value == 1
    assert args == (4, 2, 3)
    assert kwargs == {"kwarg1": None, "kwarg2": None}

    # Test the case when

# Generated at 2022-06-14 13:07:18.139085
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    # test_arg_replacer_get_old_value
    def test(x, y=4):
        pass

    ar = ArgReplacer(test, "y")

    assert ar.get_old_value((1, ), {}) is None
    assert ar.get_old_value((1, ), {}, None) is None
    assert ar.get_old_value((2, 3), {}) == 3
    assert ar.get_old_value((2, 3), {}, None) == 3
    assert ar.get_old_value((2, ), {"y": 3}) == 3
    assert ar.get_old_value((2, ), {"y": 3}, None) == 3
    assert ar.get_old_value((2, ), {}, 5) == 5

# Generated at 2022-06-14 13:07:21.150280
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    def exec_in_func():
        x = 2
    exec_in(compile('x=3', '<string>', 'exec'), {}, {'x': 1})
    exec_in_func()

# Generated at 2022-06-14 13:07:26.822579
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Impl(Configurable):
        @classmethod
        def configurable_base(cls):
            return Impl

        @classmethod
        def configurable_default(cls):
            return Impl

        def initialize(self, *args, **kwargs):
            print('initialize')


    Impl.configure(Impl, a=1)
    impl = Impl('t')


# Generated at 2022-06-14 13:07:32.506345
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import pytest
    from _pytest.monkeypatch import MonkeyPatch

    monkeypatch = MonkeyPatch()
    try:
        # Initialise type to have an empty __impl_class
        Configurable.__dict__["_Configurable__impl_class"] = None
        # Test that no exceptions have been raised
        assert Configurable.__new__(Configurable)
    except Exception:
        pytest.fail("No exception expected!")
    finally:
        monkeypatch.undo()



# Generated at 2022-06-14 13:07:44.290465
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Impl1(Configurable):
        pass

    class Impl2(Configurable):
        pass

    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            return Base

        @classmethod
        def configurable_default(cls):
            return Impl1

    class Derived(Base):
        pass

    assert Base().__class__ is Impl1
    assert Derived().__class__ is Impl1
    Base.configure(Impl2)
    assert Base().__class__ is Impl2
    assert Derived().__class__ is Impl2
    Base.configure(None)
    assert Base().__class__ is Impl1
    assert Derived().__class__ is Impl1
    Derived.configure(Impl2)
    assert Base().__class__ is Impl1

# Generated at 2022-06-14 13:07:54.786037
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # type: () -> None
    ArgReplacer(lambda x, y=1, z=2, **kwargs: None, 'x').replace(0, (1,), {})
    ArgReplacer(lambda x, y=1, z=2, **kwargs: None, 'y').replace(0, (1,), {})
    ArgReplacer(lambda x, y=1, z=2, **kwargs: None, 'z').replace(0, (1,), {})
    # Keyword arguments
    ArgReplacer(lambda x, y=1, z=2, **kwargs: None, 'x').replace(0, (), {'x':1})
    ArgReplacer(lambda x, y=1, z=2, **kwargs: None, 'y').replace(0, (), {'y':1})
    ArgRepl

# Generated at 2022-06-14 13:07:56.316239
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
        pass


# Generated at 2022-06-14 13:08:04.857546
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest

    class _Configurable(Configurable):
        pass

    class A(_Configurable):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(_Configurable):
        pass

    class E(D):
        pass

    class F(E):
        pass

    class G(F):
        pass

    class H(G):
        pass

    class I(H):
        pass

    class J(I):
        pass

    class K(J):
        pass

    class L(K):
        pass

    class M(L):
        pass

    class N(M):
        pass

    class O(_Configurable):
        pass

    class P(O):
        pass

    class Q(P):
        pass


# Generated at 2022-06-14 13:08:45.938073
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def initialize(self) -> None:
            pass
        def configurable_base():
            return A
        def configurable_default():
            return A
    a = A()
    assert isinstance(a, A)

# Generated at 2022-06-14 13:08:51.118212
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Test(Configurable):
        @classmethod
        def configurable_base(cls):
            raise NotImplementedError()

        @classmethod
        def configurable_default(cls):
            raise NotImplementedError()
        def initialize(self):
            pass

    assertTestCase(Test().initialize, None)



# Generated at 2022-06-14 13:08:59.943661
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from asyncio import events
    from tornado.queues import Queue
    from tornado.iostream import IOStream

    class A(Configurable):
        def configurable_base(self):
            return A

        def configurable_default(self):
            return B

    class B(A):
        pass

    A.configure(B)
    assert A.configured_class() is B
    assert A() is not None
    A.configure(B, foo="bar")
    with pytest.raises(ValueError):
        A.configure("tornado.ioloop.IOLoop")
    assert A(foo="baz") is not None
    assert A.configured_class() is B
    A.configure("tornado.testing.mock_ioloop.MockIOLoop")
    assert A.config

# Generated at 2022-06-14 13:09:05.972680
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestClass(Configurable):
        def configurable_base(cls):
            return TestClass

        def configurable_default(cls):
            return TestClass

        def initialize(self):
            pass

    class Sub(TestClass):
        def initialize(self):
            pass

    t = TestClass()
    Sub()
import collections


# Generated at 2022-06-14 13:09:10.577136
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    d = ObjectDict()
    d["x"] = 5
    value = d.x # type: int
    assert value == 5
    assert d["x"] == 5
    try:
        d.y
        assert False
    except AttributeError:
        pass



# Generated at 2022-06-14 13:09:12.853185
# Unit test for function errno_from_exception
def test_errno_from_exception():
    assert errno_from_exception(IOError(None)) is None
    assert errno_from_exception(IOError(42)) == 42



# Generated at 2022-06-14 13:09:25.103241
# Unit test for function import_object
def test_import_object():
    import types
    obj_types = set()  # type: Set[Type[Any]]
    for name in [
        "email.utils",
        "EmailMessage",
        "email.message.EmailMessage",
        "email.utils",
        "os.path",
        "os",
        "sys",
        "functools",
        "collections.namedtuple",
    ]:
        obj = import_object(name)
        obj_types.add(type(obj))
        if name == "os.path":
            assert obj.join == os.path.join
        elif name == "os":
            assert obj.path.join == os.path.join
        elif name == "sys":
            assert obj.version_info.major == sys.version_info.major

# Generated at 2022-06-14 13:09:34.482639
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        def configurable_base(self):
            return TestConfigurable
        def configurable_default(self):
            return TestConfigurable
        def initialize(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
    TestConfigurable.configure(None)
    c = TestConfigurable(1, 2, a=10, b=20)
    assert c.args == (1, 2)
    assert c.kwargs == {"a": 10, "b": 20}


# Generated at 2022-06-14 13:09:43.415462
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import tornado.ioloop
    import tornado.httpserver
    import tornado.netutil
    # test_case 1:
    # test that _initialize is private
    # _initialize should be private and not present in Configurable's namespace

    # assert not hasattr(Configurable, "_initialize")

    # test_case 2:
    # test that initialize of class Configurable is a public method
    # initialize should be public and present in Configurable's namespace
    assert hasattr(Configurable, "initialize")

    # test_case 3:
    # test that initialize of class Configurable is callable
    # initialize should be a callable method
    assert callable(Configurable.initialize)

    # test_case 4:
    # test that initialize of class Configurable is appropriately overridden
    # initialize of class Configurable should be different than _initialize

# Generated at 2022-06-14 13:09:47.745420
# Unit test for function import_object
def test_import_object():
    # Unittest imports mock, which shadows import_object.  Mock is always
    # imported, so this must be an indirect import to verify that import
    # hook is working.
    if 'import_object' in globals():
        del globals()['import_object']
    import unittest.mock  # type: ignore
    assert import_object('unittest.mock') is unittest.mock



# Generated at 2022-06-14 13:10:32.208066
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Create a mock for class Configurable
    configurable_class = Mock()

    # Use a lambda to replace the __new__ method with a mock
    configurable_class.__new__ = Mock(side_effect=lambda *args, **kwargs: configurable_class)

    # Set the side effect of the mocked method configurable_base
    configurable_class.configurable_base.side_effect = lambda: configurable_class

    # Set the side effect of the mocked method configurable_default
    configurable_class.configurable_default.side_effect = lambda: configurable_class

    # Set the side effect of the mocked method configured_class
    configurable_class.configured_class.side_effect = lambda: configurable_class

    # Call method __new__ of class Configurable with args and kwargs

# Generated at 2022-06-14 13:10:40.451540
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    from tornado.ioloop import IOLoop
    from tornado.tcpserver import TCPServer
    from tornado.netutil import bind_sockets

    class TCPServer1(TCPServer):
        def initialize(self):
            pass
    sock, port = bind_sockets(None)
    TCPServer1._initialized_args = {'sockets': {sock.fileno(): sock}, 'io_loop': IOLoop()}
    server = TCPServer1()
    server.initialize()
    server.initialize(sockets={sock.fileno(): sock})
    server.initialize(sockets={sock.fileno(): sock}, io_loop=IOLoop())
    server.initialize(io_loop=IOLoop())


# Generated at 2022-06-14 13:10:43.398530
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    d = ObjectDict()
    d.name = 'mike'
    assert d.name == 'mike'
    assert not hasattr(d, 'age')


# Generated at 2022-06-14 13:10:52.952322
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class MyConfig(Configurable):
        @classmethod
        def configurable_base(cls):
            return MyConfig

        @classmethod
        def configurable_default(cls):
            return MyImpl

        def initialize(self):
            pass
    class MyImpl(MyConfig):
        def initialize(self, a, b):
            pass
    class MyImpl2(MyConfig):
        def initialize(self, a, b, c=None):
            pass
    MyConfig.configure(MyImpl2)
    _Config = MyConfig
    _Config.configure(MyImpl2)
    MyConfig.configure(None)
    assert(MyConfig().__class__ is MyImpl)
    assert(MyConfig(1, 2).__class__ is MyImpl)

# Generated at 2022-06-14 13:11:03.769655
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def __init__(self):
            self.init_args = ()
        def initialize(self, *args, **kwargs):
            self.init_args = (args, kwargs)

    a = A()
    assert a.init_args == ((), {})

    A.configure(None)
    a = A(1, value=1)
    assert a.init_args == ((1,), {'value': 1})

    class B(A):
        pass

    class C(B):
        pass

    C.configure(None, arg3=3)
    c = C(1, 2, value=2)
    assert c.init_args == ((1, 2), {'value': 2, 'arg3': 3})


# Generated at 2022-06-14 13:11:04.669526
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    assert 1


# Generated at 2022-06-14 13:11:15.570060
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from .idna import _decode_idna
    from . import idna
    from .idna import cached_idna
    from .idna import cached_idna_version
    from . import _idna_impl
    from ._idna_impl import _idna_impl_version
    from .old_idna import _decode_idna as old_decode_idna


# Generated at 2022-06-14 13:11:17.285526
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    test_obj = Configurable()
    # test init without param
    test_obj.initialize()

