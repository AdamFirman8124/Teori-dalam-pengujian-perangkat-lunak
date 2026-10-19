

# Generated at 2022-06-14 13:01:54.270903
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class Foo(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Foo
        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return FooImpl
    class FooImpl(Foo):
        def initialize(self):
            pass
    f = Foo()
    assert isinstance(f, Foo)
    assert isinstance(f, FooImpl)
    class Bar(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Foo
        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return BarImpl

# Generated at 2022-06-14 13:01:59.192788
# Unit test for function import_object
def test_import_object():
    # See https://github.com/tornadoweb/tornado/pull/2294
    from tornado.escape import utf8
    assert import_object('tornado.escape.utf8') is utf8
    assert import_object('tornado.escape') is utf8.__self__
    assert import_object('tornado') is utf8.__module__.rpartition('.')[0]
    try:
        import_object('tornado.missing_module')
    except ImportError:
        pass
    else:  # pragma: no cover
        assert False, "import_object should have failed"



# Generated at 2022-06-14 13:02:03.299373
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():

    def get(**kwargs):
        var = 'default'
        arg_replacer = ArgReplacer(get, 'var')
        var = arg_replacer.get_old_value([], kwargs, var)
        return var

    assert get(var='foo') == 'foo'
    assert get() == 'default'


# Generated at 2022-06-14 13:02:12.220221
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class B(Configurable):

        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

        def _initialize(self, *args, **kwargs):
            self.args = args  # type: List[Any]
            self.kwargs = kwargs  # type: Dict[str, Any]

    class C(B):
        pass

    b = B(1, x=10)
    assert b.args == (1,)
    assert b.kwargs == {"x": 10}

    C.configure(None, y=20)
    c = C(2, x=11)
    assert c.args == (2,)
    assert c.kwargs == {"x": 11, "y": 20}

# Generated at 2022-06-14 13:02:15.415466
# Unit test for function raise_exc_info
def test_raise_exc_info():
    # type: () -> None
    try:
        try:
            raise ZeroDivisionError()
        except:
            raise_exc_info(sys.exc_info())
    except ZeroDivisionError:
        pass
    else:
        assert False, "failed to raise exception"


_rep_regex = re.compile(r"%\((.*?)\)s")



# Generated at 2022-06-14 13:02:27.011321
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    _base_cls = Configurable()
    test_impl_cls = Configurable()
    test_kwargs = {}
    test_args = {}
    test_input = 0
    # test if the implementation class given is a subclass of the base class
    def test_if_impl_is_subclass(impl_cls, base_cls, kwargs):
        if not issubclass(impl_cls, base_cls):
            raise ValueError("Invalid subclass of %s" % base_cls)
    def test_if_base_is_impl_class(base_cls, impl_cls):
        if base_cls is not impl_cls:
            raise NotImplementedError()
    # test if the implementation class given is a subclass of the base class
    test_if_impl_is_sub

# Generated at 2022-06-14 13:02:34.751071
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(x, y = 2):
        return x + y
    replacer = ArgReplacer(f, 'y')
    print(replacer.get_old_value((4,),{}))
    print(replacer.get_old_value((4,),{'y':9}))
    print(replacer.get_old_value((4,2),{}))
    print(replacer.get_old_value((4,2),{'y':9}))
    print(replacer.get_old_value((4,3),{'y':9}))


# Generated at 2022-06-14 13:02:44.599721
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.testing import AsyncTestCase, gen_test
    _MyBase = Configurable
    _MyBaseBase = Configurable
    _MyBaseBaseBase = Configurable
    _MyImpl = object
    _MyImplImpl = object
    _MyImplImplImpl = object
    _MyImplImplImpl._initialize = lambda self,*args, **kwargs : None
    _MyImplImpl._initialize = lambda self,*args, **kwargs : None
    _MyImpl._initialize = lambda self,*args, **kwargs : None
    _MyBase.configurable_base = classmethod(lambda self: _MyBaseBase)
    _MyBaseBase.configurable_base = classmethod(lambda self: _MyBaseBaseBase)
    _MyBaseBaseBase.configurable_base = classmethod(lambda self: _MyBaseBaseBase)

# Generated at 2022-06-14 13:02:47.831354
# Unit test for function raise_exc_info
def test_raise_exc_info():  # pragma: no cover
    # It's not obvious how to unit test this, so we just pretend
    # (with the help of pyflakes) that we used it somewhere.
    try:
        raise ValueError("foo")
    except:
        raise_exc_info(sys.exc_info())



# Generated at 2022-06-14 13:03:00.018330
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import inspect
    # Ensure `super().__new__` is called

    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            return Base

        @classmethod
        def configurable_default(cls):
            return BaseImpl

        def initialize(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class BaseImpl(Base):
        def __init__(self, *args, **kwargs):
            self.init_args = args
            self.init_kwargs = kwargs

    assert Base._save_configuration() == (None, None)
    assert Base()
    assert Base._save_configuration() == (None, None)
    assert Base(1, x=2)
    assert Base._save_configuration()

# Generated at 2022-06-14 13:03:21.948531
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable

        def initialize(self, *args, **kwargs):
            pass

    tc = TestConfigurable()
    assert isinstance(tc, TestConfigurable)

    # However, this does not work
    # class TestConfigurable2(Configurable):
    #    @classmethod
    #    def configurable_base(cls):
    #        return TestConfigurable2
    #
    #    @classmethod
    #    def configurable_default(cls):
    #        return TestConfigurable2
    #
    #    def __init__(self, *args, **kwargs):
    #        pass


# Generated at 2022-06-14 13:03:34.858051
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # py2 way
    # ImplA = type('ImplA', (Configurable, object), {'configurable_base': lambda self: cls, 'configurable_default': lambda self: ImplA})
    # ImplB = type('ImplB', (Configurable, object), {'configurable_base': lambda self: cls, 'configurable_default': lambda self: ImplB})
    # ImplC = type('ImplC', (Configurable, object), {'configurable_base': lambda self: cls, 'configurable_default': lambda self: ImplC})

    # py3 way:
    class ImplA(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls


# Generated at 2022-06-14 13:03:43.031720
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    def test_ObjectDict___getattr__(self):
        objd = ObjectDict(foo=4, bar=5)
        assert objd['foo'] == objd.foo == 4
        assert objd['bar'] == objd.bar == 5
        try:
            objd.foo  # noqa: F841
        except AttributeError:
            pass
        else:  # pragma: no cover
            raise AssertionError("did not get attribute error")

# Generated at 2022-06-14 13:03:53.924571
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.ioloop import IOLoop
    from tornado.httpserver import HTTPServer
    from tornado.netutil import bind_unix_socket
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.web import Application, RequestHandler
    async def do_test(impl=None, **kwargs):
        if impl is None:
            impl = 'tornado.testing.gen_test'
        HTTPServer.configure(impl, **kwargs)
        IOLoop.configure(impl, **kwargs)
        HTTPServer.configure('tornado.platform.asyncio.AsyncIOMainLoop', **kwargs)
        IOLoop.configure('tornado.platform.asyncio.AsyncIOMainLoop', **kwargs)

# Generated at 2022-06-14 13:04:03.932159
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(x=1, y=2, z=3):
        return

    arg_replacer_org = ArgReplacer(f, 'x')
    assert arg_replacer_org.get_old_value((1,2,3), {'y':2, 'z':3}) == 1
    assert arg_replacer_org.get_old_value((1,2,3), {'y':2, 'z':3}, 'default') == 1
    arg_replacer_org = ArgReplacer(f, 'y')
    assert arg_replacer_org.get_old_value((1,2,3), {'y':2, 'z':3}) == 2
    assert arg_replacer_org.get_old_value((1,2,3), {'y':2, 'z':3}, 'default')

# Generated at 2022-06-14 13:04:08.294668
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class ParentClass(Configurable):
        def __init__(self):
            super().__init__()
            self.name = "ParentClass"

    class ChildClass(ParentClass):
        def __init__(self):
            super().__init__()
            self.name += "ChildClass"

    class ConfigClass(Configurable):
        def __init__(self):
            super().__init__()
            self.name = "ConfigClass"

    ParentClass.configure(impl=ChildClass)
    assert isinstance(ParentClass(), ChildClass)
    ParentClass.configure(impl=ConfigClass)
    assert isinstance(ParentClass(), ConfigClass)



# Generated at 2022-06-14 13:04:14.832235
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(old, new=None):
        pass
    arg = ArgReplacer(foo, 'new')
    new_value = "new value"
    old_value = arg.get_old_value([None, None], {'new': new_value}, default='default')
    assert old_value == new_value
    old_value = arg.get_old_value([], {}, default='default')
    assert old_value == 'default'


# Generated at 2022-06-14 13:04:24.099293
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Test1Configurable(Configurable):
        def configurable_base(self):
            return Test1Configurable

        def configurable_default(self):
            return type(self)

    class Test1Child(Test1Configurable):
        def initialize(self, name):
            self._name = name

        def get_name(self):
            return self._name

    class Test2Configurable(Configurable):
        def configurable_base(self):
            return Test2Configurable

        def configurable_default(self):
            return type(self)

    class Test2Child(Test2Configurable):
        def initialize(self, name):
            self._name = name

        def get_name(self):
            return self._name

    class Base(Configurable):
        def configurable_base(self):
            return Base

       

# Generated at 2022-06-14 13:04:36.834631
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_func(arg1, arg2 = None, arg3 = 0):
        pass
    replacer = ArgReplacer(test_func, "arg1")
    assert replacer.get_old_value(test_func.__defaults__, None, None) == test_func.__defaults__[0]
    assert replacer.get_old_value(test_func.__defaults__, None) == test_func.__defaults__[0]
    assert replacer.get_old_value((1,), None, None) == 1
    assert replacer.get_old_value((1,), None) == 1
    assert replacer.get_old_value((None,), None) == None
    # Test error case with default value
    assert replacer.get_old_value((2,), None) == 1


# Generated at 2022-06-14 13:04:44.982717
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(*args, **kwargs):
        pass
    def test_arg(args: List[Any], kwargs: Dict[str, Any],
                 name: str, value: Any, default: Any) -> bool:
        arg_replacer = ArgReplacer(func, name)
        old_value = arg_replacer.get_old_value(args, kwargs, default)
        return old_value == value
    failed = []
    if not test_arg(["arg1", "arg2"], {}, "arg1", "arg1", None):
        failed.append(1)
    if not test_arg(["arg1", "arg2"], {}, "arg2", "arg2", None):
        failed.append(2)

# Generated at 2022-06-14 13:05:11.937228
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func1(a, b, *args, c=None, **kwargs):
        return a, b, c, args, kwargs

    def func2(*args):
        return args

    # a is replaced in args
    assert ArgReplacer(func1, "a").get_old_value((1, 2, 3), {}) == 1
    assert ArgReplacer(func1, "a").get_old_value(("a", "b", "c"), {}, "d") == "a"

    # b is replaced in args
    assert ArgReplacer(func1, "b").get_old_value(("a", 2, 3), {}) == 2
    assert ArgReplacer(func1, "b").get_old_value(("a", "b", "c"), {}, "d") == "b"

    # c

# Generated at 2022-06-14 13:05:22.263965
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a, b, c=1, d=2):
        pass
    ar = ArgReplacer(f, 'b')
    print(ar.get_old_value((1, 2, 3), {}))
    print(ar.get_old_value((1, 2, 3), {'c':2, 'd':3}))
    print(ar.get_old_value((1, 2, 3), {'c':2, 'b':0, 'd':3}))
    print(ar.get_old_value((1, 2, 3), {'c':2, 'd':3}, None))
test_ArgReplacer_get_old_value()


# Generated at 2022-06-14 13:05:25.575107
# Unit test for function raise_exc_info
def test_raise_exc_info():
    try:
        raise ValueError("error_message")
    except ValueError:
        exc_info = sys.exc_info()
        raise_exc_info(exc_info)
    # test that the exception was raised
    assert False



# Generated at 2022-06-14 13:05:34.664385
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f3(arg1, arg2, arg3):
        return arg1, arg2, arg3
    arg_replacer = ArgReplacer(f3, name='arg1')
    assert arg_replacer.get_old_value((1,2,3), {}) == 1
    assert arg_replacer.get_old_value(args=(1,2,3), kwargs={}) == 1
    assert arg_replacer.get_old_value(args=(), kwargs={'arg1':1}) == 1
    assert arg_replacer.get_old_value(args=(), kwargs={'arg1':1,'arg2':2}) == 1
    assert arg_replacer.get_old_value(args=(1,2), kwargs={'arg3':3}) == 1
    assert arg_replacer

# Generated at 2022-06-14 13:05:39.866907
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Dummy(Configurable):
        @classmethod
        def configurable_base(cls):
            return Dummy

        @classmethod
        def configurable_default(cls):
            return Dummy

        def _initialize(self):
            pass

    dummy = Dummy()
    assert isinstance(dummy, Dummy)

# Generated at 2022-06-14 13:05:47.968443
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b, c=10000, *args, **kwargs):
        pass
    replacer = ArgReplacer(f, 'a')
    old_value, args, kwargs = replacer.replace(1, (2,), {'b' : 3, 'c' : 4})
    assert old_value == 2
    assert args == (1,)
    assert kwargs == {'b' : 3, 'c' : 4}
test_ArgReplacer_replace()

# Generated at 2022-06-14 13:05:51.508175
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """Unit test for method ``__new__`` of class `Configurable`."""
    class MockConfigurable(Configurable):
        def __init__(self):
            pass
    assert MockConfigurable.__new__(MockConfigurable) is not None


# Generated at 2022-06-14 13:05:56.819787
# Unit test for function import_object
def test_import_object():
    import tornado.escape
    assert import_object("tornado.escape") is tornado.escape
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8
    assert import_object("tornado") is tornado
    # import_object raises an error with a descriptive message
    try:
        import_object("tornado.missing_module")
    except ImportError as e:
        assert str(e) == "No module named missing_module"
    else:
        raise Exception("expected ImportError")



# Generated at 2022-06-14 13:05:59.312000
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError(33, "test_errno_from_exception")
    except Exception as e:
        assert errno_from_exception(e) == 33



# Generated at 2022-06-14 13:06:08.620449
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    class Foo:
        def bar(self, _=None):
            pass
    foo = Foo()
    argreplacer = ArgReplacer(foo.bar, '_')
    assert argreplacer.get_old_value([], {}) == None
    assert argreplacer.get_old_value([], {'_': 1}) == 1
    assert argreplacer.get_old_value([1], {}) == 1
    assert argreplacer.get_old_value([1], {'_': None}) == 1


# Generated at 2022-06-14 13:06:44.604995
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    obj = ObjectDict({'a': 1})
    assert obj.a == 1
    try:
        assert obj.b == 1
        assert False, 'TypeError expected'
    except Exception as e:
        assert type(e) is AttributeError

# Generated at 2022-06-14 13:06:55.934046
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(a, b, c=None, d=None): pass

    # Test positional replacement
    replacer = ArgReplacer(foo, "c")
    old_value, args, kwargs = replacer.replace(
        "C", ("A", "B", "C1"), {"d": "D1"})

    assert args == ('A', 'B', "C", {'d': 'D1'})
    assert kwargs == {}
    assert old_value == "C1"

    # Test positional replacement with default
    replacer = ArgReplacer(foo, "c")
    old_value, args, kwargs = replacer.replace(
        "C", ("A", "B"), {"d": "D1"})


# Generated at 2022-06-14 13:07:06.370539
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    try:
        if True:
            class TestConfigurable(Configurable):
                def configurable_base(self):
                    return "while True:\n    pass"
                def configurable_default(self):
                    return None
            class TestConfigurable2(Configurable):
                def configurable_base(self):
                    return TestConfigurable
                def configurable_default(self):
                    return TestConfigurable
        TestConfigurable.configure(None)
        test_configurable_instance = TestConfigurable()
        assert test_configurable_instance.__class__.__base__ is TestConfigurable
        TestConfigurable2.configure(TestConfigurable)
        test_configurable_instance2 = TestConfigurable2()
        assert test_configurable_instance2.__class__.__base__ is TestConfigurable
    except:
        print

# Generated at 2022-06-14 13:07:16.733317
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class ClassOne(Configurable):
        def __init__(self):
            super().__init__()

        @classmethod
        def configurable_base(cls):
            return ClassOne

        @classmethod
        def configurable_default(cls):
            return ClassTwo

    class ClassTwo(ClassOne):
        def __init__(self):
            super().__init__()

    instance_one_1 = ClassOne()
    instance_one_2 = ClassOne(impl=ClassTwo)
    assert(isinstance(instance_one_1, ClassTwo))
    assert(isinstance(instance_one_2, ClassTwo))
    assert(isinstance(instance_one_1, ClassOne))
    assert(isinstance(instance_one_2, ClassOne))



# Generated at 2022-06-14 13:07:22.182408
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    o = ObjectDict()
    o.x = 1
    o.y = 2
    assert o.x == 1
    assert o.y == 2
    o["x"] = 3
    assert o.x == 3
    assert o["x"] == 3
    assert o.y == 2
    assert o["y"] == 2
    assert 42 == 42


# Generated at 2022-06-14 13:07:31.797239
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """
    Tests the __new__ method of the Configurable class.
    """
    import mock
    from unittest.mock import Mock, patch
    import collections
    from tornado import concurrent, gen, stack_context
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.testing import AsyncTestCase, gen_test
    from tornado.test.util import unittest


    class DummyTask(concurrent.Future):
        """
        A dummy Task to be used in the tests of the `execute` method.
        """

        def __init__(self, function, args=(), kwargs={}, key=None,
                     callback=None, **kw):
            super(DummyTask, self).__init__(**kw)

# Generated at 2022-06-14 13:07:43.880362
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Parent(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

        def initialize(self, a: str, b: str, c: int) -> None:
            self.a = a
            self.b = b
            self.c = c

    class Child1(Parent):
        pass

    class Child2(Parent):
        pass

    Child1.configure(None)
    Child2.configure(None)
    p = Parent('foo', 'bar', 2)  # type: ignore
    assert p.a == 'foo'
    assert p.b == 'bar'
    assert p.c == 2

    c1 = Child1('foo', 'bar', 2)  # type:

# Generated at 2022-06-14 13:07:50.622780
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Test(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Test
        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return Test
        def initialize(self):
            pass
    Test.configure(Test)
    Test()


# Generated at 2022-06-14 13:08:01.497184
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # Type annotations on this class are mostly done with comments
    # because they need to refer to Configurable, which isn't defined
    # until after the class definition block. These can use regular
    # annotations when our minimum python version is 3.7.
    #
    # There may be a clever way to use generics here to get more
    # precise types (i.e. for a particular Configurable subclass T,
    # all the types are subclasses of T, not just Configurable).
    __impl_class = None  # type: Optional[Type[Configurable]]
    __impl_kwargs = None  # type: Dict[str, Any]

    def __new__(cls, *args: Any, **kwargs: Any) -> Any:
        base = cls.configurable_base()
        init_kwargs = {}  # type: D

# Generated at 2022-06-14 13:08:13.846064
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():

    def method_initialize(self, *args, **kwargs):
        return super(type(self), self)._initialize(*args, **kwargs)

    from unittest.mock import patch
    mock_method_0 = patch.object(Configurable, "_initialize", autospec=True)
    mock_method_0.__name__ = '_initialize'
    mock_method_1 = patch.object(Configurable, "_initialize", autospec=True)
    mock_method_1.__name__ = '_initialize'

# Generated at 2022-06-14 13:08:56.080457
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(x, y):
        pass
    f_replacer = ArgReplacer(f, 'x')
    assert f_replacer.get_old_value((1, 2), {'y': 2}, 3) == 1
    assert f_replacer.get_old_value((1,), {'x': 2, 'y': 3}, 4) == 2
    assert f_replacer.get_old_value((1, 2), {'x': 2, 'y': 3}, 4) == 1

# Generated at 2022-06-14 13:09:06.625472
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class TestClass(Configurable):
        def __init__(self, a, b):
            print("init: a: {}, b: {}".format(a, b))
            self.a = a
            self.b = b
        def configurable_base(self):
            return TestClass
        def configurable_default(self):
            return TestClass
    TestClass.configure(None)
    print("TestClass: ", TestClass)
    t1 = TestClass(10, 20)
    print("t1: ", t1.a, ", ", t1.b)
    t2 = TestClass(30, 40)
    print("t2: ", t2.a, ", ", t2.b)

# Generated at 2022-06-14 13:09:15.336420
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c=None):
        return a, b, c

    r = ArgReplacer(func, "c")

    old_value, args, kwargs = r.replace(3, (1, 2), {})
    assert old_value is None
    assert args == (1, 2)
    assert kwargs == {"c": 3}

    old_value, args, kwargs = r.replace(4, (1, 2), {"c": 3})
    assert old_value == 3
    assert args == (1, 2)
    assert kwargs == {"c": 4}

    old_value, args, kwargs = r.replace(5, (1, 2, 3), {})
    assert old_value == 3
    assert args == (1, 2, 5)
    assert kwargs

# Generated at 2022-06-14 13:09:20.435562
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    @ArgReplacer.get_old_value(func = lambda x, y, z: None, name = 'y')
    def test(x, y, z):
        return None
    res = test(None, 'y', None)
    return res == 'y'



# Generated at 2022-06-14 13:09:26.051405
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    from functools import partial
    func = partial(int, base=2) # target func has some keyword args
    arg_replacer = ArgReplacer(func, 'base')
    old_value = arg_replacer.get_old_value((5,), {}, -1)
    if old_value != 2:
        raise Exception('old_value of "base" is %s' % (old_value,))


# Generated at 2022-06-14 13:09:27.189574
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    a = Configurable() 
    a.initialize()

# Generated at 2022-06-14 13:09:38.635001
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    import tornado.testing

    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return A

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return A

        def initialize(self):
            # type: () -> None
            self.initialized = True

    class B(A):
        def initialize(self):
            # type: () -> None
            super().initialize()
            self.is_b = True

    class C(B):
        def initialize(self):
            # type: () -> None
            super().initialize()
            self.is_c = True

    a = A()
    assert isinstance(a, A)

# Generated at 2022-06-14 13:09:43.582204
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """
    class test(Configurable):
        def configurable_default(self):
            return 1
        def configurable_base(self):
            return 1
        def _initialize(self):
            return 1
    """
    func = utils.Configurable.__new__(utils.Configurable)
    assert isinstance(func, utils.Configurable) is True


# Generated at 2022-06-14 13:09:52.904822
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception
    except Exception as e:
        nose.tools.assert_is(errno_from_exception(e), None)
    try:
        raise Exception(1, 2, 3)
    except Exception as e:
        nose.tools.assert_is(errno_from_exception(e), 1)
    try:
        e = Exception()
        e.errno = 1
        raise e
    except Exception as e:
        nose.tools.assert_is(errno_from_exception(e), 1)


# Fake byte literal support:  In python 2.6+, you can say b"foo" to get
# a byte literal (str in 2.x, bytes in 3.x).  There's no way to do this
# in a way that supports 2.5, though, so we need a function

# Generated at 2022-06-14 13:10:04.578491
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class C(Configurable):
        @classmethod
        def configurable_base(cls):
            return C

        @classmethod
        def configurable_default(cls):
            return C2

        def initialize(self, a, b):
            self.a = a
            self.b = b

    class C2(C):
        @classmethod
        def configurable_base(cls):
            return C

        @classmethod
        def configurable_default(cls):
            return C2

        def initialize(self, a, b):
            self.a = a * 2
            self.b = b * 3

    c = C(1, 2)
    assert c.a == 1
    assert c.b == 2

    # Check that we don't call __init__ twice

# Generated at 2022-06-14 13:11:17.067092
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, *args, c=None, **kwargs):
        pass
    arg = ArgReplacer(func, 'b')
    assert arg.get_old_value((1,2,3,4,5), {}, None) == 2
    assert arg.get_old_value((1,2,3,4,5), {'b': 3}) == 2
    assert arg.get_old_value((1,2,3,4,5), {}, None) == 2
    assert arg.get_old_value((1,2,3,4,5), {'c': 4}) == 2
    assert arg.get_old_value((1,2,3,4,5), {}, None) == 2

# Generated at 2022-06-14 13:11:21.887002
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise Exception(42, "test")
    except Exception as e:
        assert errno_from_exception(e) == 42
    try:
        raise Exception("test")
    except Exception as e:
        assert errno_from_exception(e) == "test"



# Generated at 2022-06-14 13:11:32.548443
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Base(Configurable):
        def __init__(self):
            super(Base,self).__init__()
        def configurable_default(cls):
            return self.__init__
        def configurable_base(cls):
            return self.__init__
        @classmethod
        def configure(cls, impl, **kwargs):
            _impl = impl
            _kwargs = kwargs
            super(Base,cls).configure(impl, **kwargs)
        _initialize = __init__
        initialize = __init__
        @classmethod
        def configured_class(cls):
            super(Base,cls).configured_class()
            return True
        @classmethod
        def _save_configuration(cls):
            super(Base,cls)._save_configuration()