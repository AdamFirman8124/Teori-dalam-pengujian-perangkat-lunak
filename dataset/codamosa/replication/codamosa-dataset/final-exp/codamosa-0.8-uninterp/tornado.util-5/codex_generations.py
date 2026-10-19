

# Generated at 2022-06-14 13:01:39.219060
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def myfunc(a, b, c=1, d=2, *args, **kwargs):
        return a, b, c, d, args, kwargs
    replacer = ArgReplacer(myfunc, 'c')
    assert replacer.replace('c_new', (1,2), {'a':3,'b':4,'d':5}) == \
        (1, (1, 2), {'a':3,'b':4,'d':5,'c':'c_new'})
    assert replacer.get_old_value((1,2), {'a':3,'b':4,'c':5}) == 5
    replacer = ArgReplacer(myfunc, 'b')

# Generated at 2022-06-14 13:01:45.238673
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c):
        pass

    func_replacer = ArgReplacer(func, "a")
    args = (1, 2, 3)
    kwargs = {"a": 3}
    old_value, args, kwargs = func_replacer.replace(4, args, kwargs)
    assert old_value == args[0] == 1



# Generated at 2022-06-14 13:01:52.708414
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class A(Configurable):
        def __init__(self, arg):
            self.arg = arg

        def configurable_base(self):
            return A

        def configurable_default(self):
            return B

    class B(A):
        def __init__(self, arg):
            self.arg = arg

    A.configure(A)
    a = A(0)
    assert isinstance(a, A)

    A.configure(B)
    a = A(1)
    assert isinstance(a, B)
    assert a.arg == 1


# Generated at 2022-06-14 13:02:01.901740
# Unit test for function errno_from_exception
def test_errno_from_exception():
    errno_errors = [
        IOError(0, "x"),
        IOError(1, "x"),
        IOError(2, "x"),
        OSError(0, "x"),
        OSError(1, "x"),
        OSError(2, "x"),
        MyError(0, "x"),
        MyError(1, "x"),
        MyError(2, "x"),
    ]

    for err in errno_errors:
        assert errno_from_exception(err) == err.args[0]  # type: ignore


# Generated at 2022-06-14 13:02:09.704573
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c, *args, **kwargs):
        pass
    
    arg_replacer = ArgReplacer(func, 'a')
    old_value, args, kwargs = arg_replacer.replace(10,(20,30,40,50), {})
    assert args == (10,30,40,50)
    assert kwargs == {}
    assert old_value == 20
    
    old_value, args, kwargs = arg_replacer.replace(100,(200,300,400,500), {'a':600})
    assert args == (200,300,400,500)
    assert kwargs == {'a':100}
    assert old_value == 600



# Generated at 2022-06-14 13:02:19.321161
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def aaa(self, xxx, yyy):
        pass

    aa = ArgReplacer(aaa, "xxx")
    bb = ArgReplacer(aaa, "yyy")

    assert aa.arg_pos == 1
    assert aa.get_old_value((1, 2), {}) == 1
    assert aa.get_old_value((), {"xxx": 2}) == 2
    assert aa.get_old_value((), {"xxx": 2}) == 2
    assert aa.get_old_value(args=(), kwargs={"xxx": 2}) == 2
    assert aa.get_old_value(args=(), kwargs={"xxx": 2}, default=None) == 2

# Generated at 2022-06-14 13:02:31.225286
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(self, a, b=2, c=3):
        # type: (int, int, int) -> int
        return a+b+c

    f = ArgReplacer(func, 'b')
    assert f.get_old_value([1],dict()) == 2
    assert f.get_old_value([1,2], dict()) == 2
    assert f.get_old_value([1,2,3], dict()) == 2
    assert f.get_old_value([1], {'b': 6}) == 6
    assert f.get_old_value([1,2], {'b': 6}) == 2
    assert f.get_old_value([1,2,3], {'b': 6}) == 2
    assert f.get_old_value([1], {'c': 6}) == 2


# Generated at 2022-06-14 13:02:36.507083
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class ABC(Configurable):
        @classmethod
        def configurable_base(cls):
            return ABC

        @classmethod
        def configurable_default(cls):
            pass
    class D(ABC):
        pass
    class E(ABC):
        pass
    D.configure(E)
    a = D()  # type: ABC

    assert isinstance(a, D)
    assert not isinstance(a, E)


# Generated at 2022-06-14 13:02:39.546928
# Unit test for function import_object
def test_import_object():
    #import_object('t.z')
    from tornado.escape import utf8
    print(import_object('tornado.escape.utf8'))


# Generated at 2022-06-14 13:02:49.743275
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def testfn(foo=None):
        pass

    fn = ArgReplacer(testfn, "foo")
    old, args, kwargs = fn.replace("b", (), {})
    assert old == None
    assert args == ()
    assert kwargs == {'foo': 'b'}

    fn = ArgReplacer(testfn, "foo")
    old, args, kwargs = fn.replace("b", (1,), {})
    assert old == None
    assert args == (1,)
    assert kwargs == {'foo': 'b'}

    fn = ArgReplacer(testfn, "foo")
    old, args, kwargs = fn.replace("b", (1,2), {})
    assert old == None
    assert args == (1,2)

# Generated at 2022-06-14 13:03:00.983022
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class SampleClass(Configurable):
        def configurable_base(self):
            return SampleClass

        def configurable_default(self):
            return SampleClass

    sampleClass = SampleClass()
    assert sampleClass.initialize == sampleClass._initialize
    assert sampleClass.initialize == SampleClass._initialize



# Generated at 2022-06-14 13:03:05.355793
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.ioloop import IOLoop

    class BaseIOLoop(Configurable):
        def configurable_base(self):
            return IOLoop

        def configurable_default(self):
            return IOLoop

    class CustomIOLoop(BaseIOLoop):
        pass

    IOLoop.configure(None)
    assert isinstance(IOLoop(), IOLoop)
    IOLoop.configure("tornado.ioloop.IOLoop")
    assert isinstance(IOLoop(), IOLoop)
    IOLoop.configure("tests.test_util.CustomIOLoop")
    assert isinstance(IOLoop(), CustomIOLoop)

    class NewBaseIOLoop(Configurable):
        def configurable_base(self):
            return NewBaseIOLoop


# Generated at 2022-06-14 13:03:11.224464
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class MyClass(Configurable):
        def __init__(self, *args, **kwargs):
            super()._initialize(*args, **kwargs)
    obj = MyClass(1, 2, 3)
    assert obj.args == (1, 2, 3)
    obj = MyClass(a=1, b=2)
    assert obj.args == ()
    assert obj.kwargs == {'a': 1, 'b': 2}
    obj = MyClass(1, 2, a=3, b=4)
    assert obj.args == (1, 2)
    assert obj.kwargs == {'a': 3, 'b': 4}

# Generated at 2022-06-14 13:03:12.354036
# Unit test for function import_object
def test_import_object():
    import_object('tornado.escape')


# Generated at 2022-06-14 13:03:25.619634
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def foo(a: int, b: int = 3, *c: Any, **d: Any):
        pass

    def bar(arg: int):
        pass

    f = ArgReplacer(foo, "b")
    assert f.get_old_value((1,), {}) == 3
    assert f.get_old_value((1,), {}, default=5) == 5
    assert f.get_old_value((1, 2,), {}) == 2
    assert f.get_old_value((1, 2,), {"b": 3}) == 2
    assert f.replace(5, (1,), {}) == (3, (1,), {"b": 5})
    assert f.replace(5, (1,), {"b": 3}) == (3, (1,), {"b": 5})

# Generated at 2022-06-14 13:03:27.839995
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    obj = Configurable()
    assert obj._initialize() == None


# Generated at 2022-06-14 13:03:34.846745
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # unit tests are in ioloop_test

    # __new__ method of class Configurable
    # Testing with class Configurable
    assert callable(Configurable.__new__)
    assert isinstance(Configurable.__new__, classmethod)
    assert Configurable.__new__.__module__ == 'tornado.util'
    assert Configurable.__new__.__qualname__ == 'Configurable.__new__'
    return None



# Generated at 2022-06-14 13:03:40.873985
# Unit test for function import_object
def test_import_object():
    # This is separate from the above docstring test because it
    # requires an import.
    import_object('tornado.escape')
    import_object('tornado.escape.utf8')
    import_object('tornado')
    try:
        import_object('tornado.missing_module')
    except ImportError:
        pass



# Generated at 2022-06-14 13:03:52.550579
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def fun(a, b, c):
        pass
 
    a = ArgReplacer(fun, "a")
    assert a.get_old_value((1, 2, 3), {}) == 1
    assert a.get_old_value((1, 2, 3), {}, None) == 1
    assert a.get_old_value((1, 2, 3), {}, 0) == 1
    assert a.get_old_value((1,), {}) == 1
    assert a.get_old_value((), {}, 0) == 0
    assert a.get_old_value((), {}) == None
    b = ArgReplacer(fun, "b")
    assert b.get_old_value((1, 2, 3), {}) == 2

# Generated at 2022-06-14 13:03:57.985072
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func1(arg1, arg2):
        return arg1, arg2

    def func2_kwa(arg1, arg2=None, arg3=None):
        return arg1, arg2, arg3

    def func2_mixed():
        return 2

    ArgReplacer.get_old_value(func2_mixed, "arg1")


# Generated at 2022-06-14 13:04:09.994052
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    # Call ObjectDict.__getattr__
    # Call ObjectDict.__getattr__
    pass

# Generated at 2022-06-14 13:04:15.900531
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    import functools
    # The following uses functools.wraps because otherwise
    # the signature of the real_func would not be
    # preserved.
    def wrapper(real_func):
        arg_replacer = ArgReplacer(real_func, "arg")
        @functools.wraps(real_func)
        def inner_wrapper(*args, **kwargs):
            old_value, args, kwargs = arg_replacer.replace("new_value", args, kwargs)
            ret = real_func(*args, **kwargs)
            # The following is just to make sure that
            # the old value returned is the same as the new value.
            # Thus we can say the old value has been replaced with the
            # new value.
            assert old_value == "new_value"
            return ret
       

# Generated at 2022-06-14 13:04:25.000459
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Concrete1(Configurable):
        @classmethod
        def configurable_base(cls):
            return Concrete1

        @classmethod
        def configurable_default(cls):
            return Concrete1

        def initialize(self, a, b, c=None):
            pass

    # Method initialize of class Configurable is tested by the test for class Configurable
    # Unit test for method configure of class Configurable
    def test_Configurable_configure():
        class Concrete2(Configurable):
            @classmethod
            def configurable_base(cls):
                return Concrete2

            @classmethod
            def configurable_default(cls):
                return Concrete2

            def __init__(self, d=None, e=None):
                pass


# Generated at 2022-06-14 13:04:37.332183
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    """
    Unit test for ArgReplacer#get_old_value
    """
    @staticmethod
    def func(arg1, arg2=None):
        pass
    replacer = ArgReplacer(func, "arg1")
    assert None == replacer.get_old_value((), {})
    assert None == replacer.get_old_value((), {"arg2":"2"})
    assert "1" == replacer.get_old_value(("1",), {"arg2":"2"})
    assert "1" == replacer.get_old_value(("1",), {"arg2":"2", "arg1":"1"})
    assert None == replacer.get_old_value(("1",), {"arg2":"2", "arg1":"1"}, None)
    

# Generated at 2022-06-14 13:04:41.750491
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """Tests for the method __new__ of class Configurable
    """
    def __new__(cls, *args, **kwargs):
        pass
    __new___args = [
        (),
    ]
    __new___kwargs = [
        {},
    ]
    Configurable.__new__(*__new___args, **__new___kwargs)



# Generated at 2022-06-14 13:04:47.204346
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # example1
    class MyClass(Configurable):
        @classmethod
        def configurable_base(cls):
            return MyClass

        @classmethod
        def configurable_default(cls):
            return MyClass
    
    obj = MyClass()
    # example2
    obj = MyClass.configure(MyClass, foo=1)
    print(type(obj))  # Can be confirmed that obj is of class MyClass



# Generated at 2022-06-14 13:04:59.743076
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(a, b, c=1, **kwargs):
        pass

    arg_replacer = ArgReplacer(foo, 'a')
    assert arg_replacer.get_old_value((1, 2, 3), {'a': 15}) == 1
    assert arg_replacer.get_old_value((1, 2, 3), {'a': 15}, 0) == 1
    arg_replacer = ArgReplacer(foo, 'c')
    assert arg_replacer.get_old_value((1, 2, 3), {'a': 15}) == 1
    assert arg_replacer.get_old_value((1, 2, 3), {'a': 15}, 0) == 0
    assert arg_replacer.get_old_value((1, 2), {'c': 15}) == 15
    assert arg_repl

# Generated at 2022-06-14 13:05:11.041120
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def fun(a, b, c):
        pass
    ar = ArgReplacer(fun, 'b')
    assert ar.get_old_value(('hello', 'world', '!'), {'a':'a', 'b':'b', 'c':'c'}) == 'world'
    assert ar.get_old_value(('hello', 'world'), {'a':'a', 'b':'b', 'c':'c'}, 'orz') == 'world'
    assert ar.get_old_value(('hello', 'world', '!'), {'a':'a', 'c':'c'}, 'orz') == 'orz'

if __name__ == '__main__':
    test_ArgReplacer_get_old_value()

# Generated at 2022-06-14 13:05:22.924524
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f1(a, b):
        return a, b
    def f2(a, b, c):
        return a, b, c
    def f3(a, b, c, d):
        return a, b, c
    def f4(a, b, c, d):
        return a, b, c, d
    def f5(a, b, c, d, e):
        return a, b, c, d, e
    def f6(a, b, c, d, e, f):
        return a, b, c, d, e, f
    def f7(a, b, c, d, e, f, g):
        return a, b, c, d, e, f, g

# Generated at 2022-06-14 13:05:29.745239
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c):
        return a, b, c
    arg_replacer = ArgReplacer(func, "a")
    assert arg_replacer.get_old_value((1, 2, 3),{}) == 1
    assert arg_replacer.get_old_value((), {"a": 1}) == 1
    assert arg_replacer.get_old_value((), {"a": 1}, default=3) == 1
    assert arg_replacer.get_old_value((), {}, default=3) == 3


# Generated at 2022-06-14 13:05:39.765046
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def testfunc(a, b, *args, **kwargs):
        pass
    a = ArgReplacer(testfunc, "a")
    assert a.replace("new_value", ("a", "b", "args"), {"args": "args", "kwargs": "kwargs"}) == ("a", ("new_value", "b", "args"), {"args": "args", "kwargs": "kwargs"})


# Generated at 2022-06-14 13:05:51.208058
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from functools import wraps
    from types import FunctionType
    from types import MethodType
    from types import WrapperDescriptorType
    from types import _MethodDescriptorType
    import warnings

    @Configurable
    class zConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return zConfigurable

        @classmethod
        def configurable_default(cls):
            return zConfigurable

    def configurable_is_instance(x):
        return isinstance(zConfigurable.configured_class(), type(x))

    def configurable_is_subclass(x):
        return issubclass(zConfigurable.configured_class(), type(x))

    class zImpl(zConfigurable):
        x = 0


# Generated at 2022-06-14 13:06:00.440115
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import unittest
    from types import MethodType
    from types import FunctionType
    from types import BuiltinMethodType

    class Configurable(object):
        def __new__(cls, *args, **kwargs):
            instance = super(Configurable, cls).__new__(cls)
            instance.initialize(*args, **kwargs)
            return instance

        def initialize(self, *args, **kwargs):
            pass
    # End unit test class
    class A(Configurable):
        def __init__(self, *args, **kwargs):
            raise Exception("Configurable classes should use initialize instead of __init__")

        # Unit test for method initialize of class A
        def test_initialize(self):
            import unittest
            from types import MethodType
            from types import FunctionType

# Generated at 2022-06-14 13:06:05.896287
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    if not isinstance(Configurable.__new__, types.MethodType):
        raise AssertionError
    # AssertionError: No exception raised
    if not isinstance(Configurable.configurable_base, types.MethodType):
        raise AssertionError
    # AssertionError: No exception raised
    try:
        Configurable.configurable_base()
        raise AssertionError
    except NotImplementedError:
        pass
    else:
        raise AssertionError
    # AssertionError: No exception raised
    if not isinstance(Configurable.configurable_default, types.MethodType):
        raise AssertionError
    # AssertionError: No exception raised

# Generated at 2022-06-14 13:06:15.973577
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def configurable_base(self):
            return A
        def configurable_default(self):
            return B
        def initialize(self, aa, bb=None):
            self.aa = aa
            self.bb = bb
    class B(A):
        pass
    class C(Configurable):
        def configurable_base(self):
            return C
        def configurable_default(self):
            return D
        def initialize(self, cc, dd=None):
            self.cc = cc
            self.dd = dd
    class D(C):
        pass
    A.configure(B, bb=1)
    C.configure(D, dd=2)
    x = A(3)
    assert isinstance(x, B)

# Generated at 2022-06-14 13:06:17.487756
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    a = Configurable()
    a.initialize()

# Generated at 2022-06-14 13:06:24.286921
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func0():
        pass
    assert ArgReplacer(func0, "a").get_old_value([], {}) == None
    def func1(a):
        pass
    assert ArgReplacer(func1, "a").get_old_value([1], {}) == 1
    assert ArgReplacer(func1, "b").get_old_value([1], {}) == None
    def func2(a, b):
        pass
    assert ArgReplacer(func2, "a").get_old_value([1], {}) == 1
    assert ArgReplacer(func2, "b").get_old_value([1], {}) == None
    assert ArgReplacer(func2, "a").get_old_value([1, 2], {}) == 1
    assert ArgReplacer(func2, "b").get_old

# Generated at 2022-06-14 13:06:34.598655
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a,b,c=3,d=4,e=5,*args,**kwargs): pass
    n1=1
    n2=2
    n3=3
    n4=4
    n5=5
    n6=6
    n7=7
    n8=8
    n9=9
    a = ArgReplacer(func,"d")
    print(a.replace(n1,(n1,n2,),{}))
    print(a.replace(n2,(n1,n2,),{"d":n9}))
    print(a.replace(n3,(n1,n2,),{"e":n9}))
    print(a.replace(n4,(n1,n2,),{"e":n5,"d":n9}))

# Generated at 2022-06-14 13:06:45.278845
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    class MockFunc(object):
        pass

    # wrap_func() will call ArgReplacer.replace() to replace 'arg' with 'new_value' in
    # args, kwargs of mock_func(*args, **kwargs).
    def wrap_func(mock_func: MockFunc, arg: str, new_value: Any) -> MockFunc:
        replacer = ArgReplacer(mock_func, arg)
        # mock_func.func_code is a dummy attribute that is not used by ArgReplacer.
        mock_func.func_code = None

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            old_value, args, kwargs = replacer.replace(new_value, args, kwargs)
            return mock_func(*args, **kwargs), old_value

# Generated at 2022-06-14 13:06:51.116730
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
            pass

    cfg = TestConfigurable()
    assert isinstance(cfg, TestConfigurable)

    cfg.configure(None)

    cfg = TestConfigurable()
    assert isinstance(cfg, TestConfigurable)

    cfg.configure("tornado.simple_httpclient.SimpleAsyncHTTPClient")
    assert cfg.configured_class() == simple_httpclient.SimpleAsyncHTTPClient
    assert cfg._save_configuration() == (
        simple_httpclient.SimpleAsyncHTTPClient,
        {},
    )

    cfg = TestConfigurable

# Generated at 2022-06-14 13:07:36.421341
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    obj = ObjectDict()  # type: ObjectDict

    obj.a = 1
    assert obj["a"] == 1
    assert obj.a == 1
    assert obj.b == AttributeError



# Generated at 2022-06-14 13:07:48.665929
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f1(a, b, c):
        pass
    def f2(a, *b):
        pass
    def f3(a, **b):
        pass
    def f4(a, b, c=3, d=4, e=5):
        pass
    def f5(a, b, c=3, *d):
        pass
    def f6(a, b, c=3, **d):
        pass
    args = ['x', 'y', 'z']
    kwargs = {'d': 'd', 'e': 'e'}
    # test ArgReplacer._getargnames
    assert ArgReplacer(f1, 'a')._getargnames(f1) == ['a', 'b', 'c']
    assert ArgReplacer(f2, 'a')._getargnames

# Generated at 2022-06-14 13:08:00.061626
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        @classmethod
        def configurable_base(cls): return cls
        @classmethod
        def configurable_default(cls): return B
        def initialize(self): self.name = 'A'
    class B(Configurable):
        @classmethod
        def configurable_base(cls): return cls
        @classmethod
        def configurable_default(cls): return C
        def initialize(self): self.name = 'B'
    class C(Configurable):
        @classmethod
        def configurable_base(cls): return cls
        @classmethod
        def configurable_default(cls): return D
        def initialize(self): self.name = 'C'

# Generated at 2022-06-14 13:08:07.022620
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # pylint: disable=missing-class-docstring
    # pylint: disable=missing-function-docstring
    # pylint: disable=unused-argument, unused-variable
    # pylint: disable=global-statement
    # pylint: disable=no-self-use

    class Default(Configurable):
        # pylint: disable=missing-class-docstring
        # pylint: disable=abstract-method

        def initialize(self, one, two, three=None, four=None):
            # type: (str, str, Optional[str], Optional[str]) -> None
            # pylint: disable=missing-function-docstring
            # pylint: disable=unused-argument, unused-variable
            pass


# Generated at 2022-06-14 13:08:12.340674
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MockConfigurable(Configurable):
        def __new__(cls, *args, **kwargs):
            return super(MockConfigurable, cls).__new__(cls, *args, **kwargs)

    c = MockConfigurable()
    c.configure("tornado.util")



# Generated at 2022-06-14 13:08:16.489559
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def my_func(a, b, c="d"):
        return a, b, c
    arg_replacer = ArgReplacer(my_func, "c")
    assert arg_replacer.get_old_value(("asd", "b"), {}) == "d"


# Generated at 2022-06-14 13:08:21.520763
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def configurable_base(self):
            return A
        def configurable_default(self):
            return A
    A.configure(A, an=5)
    a = A(1)
    assert a.an == 5
    assert a.x == 1



# Generated at 2022-06-14 13:08:32.984102
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a, b, c=3):
        pass

    # Test that it works properly with positional arguments
    arg_replacer = ArgReplacer(f, "a")
    assert arg_replacer.get_old_value((2, 3,), {}, default=1) == 2
    assert arg_replacer.get_old_value((2, 3,), {"b": 5}, default=1) == 2
    assert arg_replacer.get_old_value((2, 3,), {"a": 5}, default=1) == 2
    assert arg_replacer.get_old_value((2, 3,), {"c": 5}, default=1) == 2

    # Test that it works properly with keyword arguments
    arg_replacer = ArgReplacer(f, "c")
    assert arg_replacer.get_old_value

# Generated at 2022-06-14 13:08:35.795748
# Unit test for function errno_from_exception
def test_errno_from_exception():
    assert errno_from_exception(Exception("error")) == "error"
    assert errno_from_exception(Exception("error", "error")) == "error"



# Generated at 2022-06-14 13:08:44.673833
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    configurable_base = Configurable()

    def configurable_base_func(cls):
        return configurable_base

    def configurable_default_func(cls):
        return configurable_base

    # This is an interface class, we will set configurable_base() and
    # configurable_default() to be specified classes
    class ConfigurableInterface(Configurable):
        @classmethod
        def configurable_base(cls):
            return configurable_base_func(cls)

        @classmethod
        def configurable_default(cls):
            return configurable_default_func(cls)

    # This is a subclass of ConfigurableInterface.

# Generated at 2022-06-14 13:09:38.837470
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class X(Configurable):

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return X

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return X

        def initialize(self, foo):
            # type: (int) -> None
            pass

    # Check that the default impl works
    X(5)

    # Check that we have the right impl
    class Y(X):
        pass

    X.configure(Y)
    assert isinstance(X(5), Y)
    assert isinstance(X(), Y)
    assert isinstance(X(foo=5), Y)

    # Check that we can supply kwargs

# Generated at 2022-06-14 13:09:44.346741
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class C(Configurable):
        def initialize(self, x):
            self.x = x

    C.configure(None, x=1)
    c = C(2)
    assert c.x == 2

    c = C(x=3)
    assert c.x == 3

    C.configure(None, x=4)
    c = C(x=5)
    assert c.x == 5


# Generated at 2022-06-14 13:09:52.114133
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test(x, y, z=0):
        pass
    a = ArgReplacer(test, "y")
    old_value, args, kwargs = a.replace("b", ("a",), {"z": 5})
    assert old_value == "a"
    assert args[0] == "a"
    assert args[1] == "b"
    assert len(args) == 2
    assert kwargs["z"] == 5

    a = ArgReplacer(test, "z")
    old_value, args, kwargs = a.replace("b", ("a",), {"z": 5})
    assert old_value == 5
    assert args[0] == "a"
    assert args[1] == "a"
    assert len(args) == 2
    assert kwargs == {"z": "b"}

# Generated at 2022-06-14 13:10:03.864763
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import copy
    import functools
    import importlib

    import tornado.platform.auto
    import tornado.platform.caresresolver
    import tornado.platform.twisted
    import tornado.platform.epoll
    import tornado.platform.select

    import tornado.util

    importlib.reload(tornado.platform.caresresolver)

    def check_configurable(configurable_type, configurable_base_type, impl_type):
        def test_configurable(self):
            self.assertIs(configurable_type, configurable_type.configurable_base())
            self.assertIs(impl_type, configurable_type.configurable_default())

            self.assertIs(impl_type, configurable_type())
            self.assertIs(impl_type, configurable_type.configured_class())

           

# Generated at 2022-06-14 13:10:07.060304
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    x = ObjectDict()
    x.__getattr__('None')
    x.__getattr__('None')
    x.__getattr__('None')
    x.__setattr__('str', None)
    x.__getattr__('str')
    x.__getattr__('str')
    x.__getattr__('str')

# Generated at 2022-06-14 13:10:16.326686
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a, b=1, c=2):
        pass
    self = ArgReplacer(f, "b")
    assert self.get_old_value((1,), {}) == 1
    assert self.get_old_value((), {}) == 1
    assert self.get_old_value((), {"b": 2}) == 2
    assert self.get_old_value((), {"z": 3}) is None
    assert self.get_old_value((), {}, default=4) == 4



# Generated at 2022-06-14 13:10:24.127739
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        def configurable_base(cls):
            return TestConfigurable

        def configurable_default(cls):
            return TestConfigurable

        def _initialize(self, value: Any) -> None:
            self.x = value

    class TestSubConfigurable(TestConfigurable):
        pass

    TestConfigurable.configure(None)
    assert isinstance(TestConfigurable(1), TestConfigurable)
    assert isinstance(TestConfigurable(1), TestConfigurable)
    assert not isinstance(TestConfigurable(1), TestSubConfigurable)
    assert TestConfigurable(1).x == 1
    # _initialize() is not called if the implementation class is
    # changed and the new implementation class is not a subclass of
    # the original implementation class.
    TestConfigurable.configure

# Generated at 2022-06-14 13:10:34.076539
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b=2, c=3): return a+b+c
    arg_replacer = ArgReplacer(func, "b")
    assert func(0, 4, 5) == 9
    assert arg_replacer.get_old_value((0, 4, 5), {}) == 4
    assert arg_replacer.get_old_value((0,), {"c": 5}) is None
    assert arg_replacer.get_old_value((), {"b": 4, "c": 5}) == 4
    assert arg_replacer.get_old_value((), {"b": 4, "c": 5}, "default") == 4
    assert arg_replacer.get_old_value((0,), {"c": 5}) is None
    assert arg_replacer.replace(6, (0, 4, 5), {})

# Generated at 2022-06-14 13:10:42.682991
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import unittest
    from tornado.httputil import *

    class MyHTTPConnection(HTTPConnection):
        def initialize(self, address, io_loop, client_connection_timeout, max_buffer_size = None, proxy_host = '',
                       proxy_port = None, proxy_username = '', proxy_password = '', proxy_auth_mode = None, **kwargs):
            super(MyHTTPConnection, self).initialize(address, io_loop, client_connection_timeout, max_buffer_size, proxy_host,
                                                     proxy_port, proxy_username, proxy_password, proxy_auth_mode, **kwargs)

    addr = HTTPConnection.address
    io_loop = HTTPConnection.io_loop
    client_connection_timeout = HTTPConnection.client_connection_timeout
    max_buffer_size = HTTPConnection.max

# Generated at 2022-06-14 13:10:44.395619
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    assert Configurable.initialize(Configurable, "arg1") == None

