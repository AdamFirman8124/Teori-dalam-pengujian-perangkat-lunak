

# Generated at 2022-06-14 13:01:59.065400
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_replace(args, kwargs, replace_arg, replace_value, expected_args,
                     expected_kwargs, expected_old_value):
        a = ArgReplacer(test_replace, replace_arg)
        old_value, result_args, result_kwargs = a.replace(replace_value, args,
                                                          kwargs)
        assert result_args == expected_args
        assert result_kwargs == expected_kwargs
        assert old_value == expected_old_value

    test_replace((1, 2), {'a': 3, 'b': 4}, 'b', 5, (1, 2), {'a': 3, 'b': 5}, 4)

# Generated at 2022-06-14 13:02:07.795930
# Unit test for function import_object
def test_import_object():
    class MyClass(object):
       pass
    def my_function():
        pass
    class MyOuterClass(object):
        my_inner_class = MyClass
        class MyInnerClass(object):
            pass
    import sys
    sys.modules[__name__] = MyOuterClass
    assert(import_object('MyClass') is MyClass)
    assert(import_object('my_function') is my_function)
    assert(import_object('MyOuterClass') is MyOuterClass)
    assert(import_object('MyOuterClass.my_inner_class') is MyClass)
    assert(import_object('MyOuterClass.MyInnerClass') is MyOuterClass.MyInnerClass)
    assert(import_object('tornado.MyClass') is MyClass)

# Generated at 2022-06-14 13:02:17.766130
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    Configurable = None
    # That's mostly just a test that it doesn't crash.
    # The implementation details are just too much to test
    # reliably here.
    class MyConfigurable(Configurable):
        pass
    class MyConfigurableChild(MyConfigurable):
        pass
    class MyConfigurableChildChild(MyConfigurableChild):
        pass
    class MyConfigurableImpl(MyConfigurable):
        pass
    class MyConfigurableImpl2(MyConfigurable):
        pass
    class MyConfigurableImplChild(MyConfigurableImpl):
        pass
    class MyConfigurableImplChildChild(MyConfigurableImplChild):
        pass
    MyConfigurable.configure(MyConfigurableImpl)
    MyConfigurableChild.configure(MyConfigurableImplChild)
    MyConfigurableChildChild.configure(MyConfigurableImplChildChild)



# Generated at 2022-06-14 13:02:19.904370
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from unittest import TestCase
    from unittest import mock

    class BaseConfigurable(Configurable):
        def initialize(self):
            pass


# Generated at 2022-06-14 13:02:21.993285
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type(Configurable().configurable_base()) == type(Configurable)
    pass


# Generated at 2022-06-14 13:02:30.370558
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Base(Configurable):
        '''doc string'''
        def __init__(self):
            pass
        def configurable_base(self):
            return Base
        def configurable_default(self):
            return Base
        
        def initialize(self):
            pass
    class SubBase(Base):
        def __init__(self):
            pass
        
    base = Base()
    sub = SubBase()
    assert(base.__class__==Base)
    assert(sub.__class__==SubBase)

# Generated at 2022-06-14 13:02:33.975014
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from unittest.mock import Mock
    import tornado

    ERR_MSG = "Configurable.initialize() takes from 1 to 2 positional arguments but 3 were given"
    assert Mock(tornado.util.Configurable).initialize.__doc__ == ERR_MSG

# Generated at 2022-06-14 13:02:40.343513
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test(*args, **kwargs):
        pass
    # Test replacement of non-existent argument
    assert ArgReplacer(test, "foo").replace(1, (), {}) == (None, (), {"foo": 1})
    # Test replacement of positional argument
    assert ArgReplacer(test, "foo").replace(1, (2,), {}) == (2, (1,), {})
    # Test replacement of kwarg
    assert ArgReplacer(test, "foo").replace(1, (), {"foo": 2}) == (2, (), {"foo": 1})

# Generated at 2022-06-14 13:02:44.351014
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    obj = ObjectDict()
    obj.nimblestr = "string"
    assert obj.nimblestr == "string"
    assert obj["nimblestr"] == "string"



# Generated at 2022-06-14 13:02:50.577442
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c=3, d=4):
        return a, b, c, d
    
    arg_replacer = ArgReplacer(func, 'c')
    old_value, args, kwargs = arg_replacer.replace(2, [1, 2], {'d': 4})
    assert old_value == 3
    assert args == [1, 2]
    assert kwargs == {'d': 4}

    old_value, args, kwargs = arg_replacer.replace(2, [1, 2], {'c': 4})
    assert old_value == 4
    assert args == [1, 2]
    assert kwargs == {'c': 2}

# Generated at 2022-06-14 13:03:05.269816
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c, d=None):
        pass
    argr = ArgReplacer(func, 'd')
    assert argr.get_old_value(('a', 'b', 'c'), {'d':'d'})=='d'
    assert argr.get_old_value(('a', 'b', 'c'), {'d1':'d1'})==None
    assert argr.get_old_value(('a', 'b', 'c'), {'d1':'d1'}, 'd')=='d'

# Generated at 2022-06-14 13:03:06.722418
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """Test Configurable.__new__."""
    # TODO: test Configurable.__new__



# Generated at 2022-06-14 13:03:10.672218
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # __new__ should call __new__ of super class under normal case
    base = Configurable()
    base.__new__(base)
    # __new__ should raise TypeError if impl is not a subclass of cls
    impl = Configurable()
    with pytest.raises(ValueError):
        base.configure("", impl)
    # __new__ should return a correct instance if impl is a subclass of cls



# Generated at 2022-06-14 13:03:23.945350
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
  # setUp
  class A():
    pass
  class B():
    pass
  # representation: (cls: A, *args: Any, **kwargs: Any) -> Any
  def mock_new(cls, *args, **kwargs):
    return mock_new.return_value
  mock_new.return_value = A()
  mock_new_real = Configurable.__new__
  Configurable.__new__ = mock_new
  # test
  a = Configurable(1, a=2)
  # assert
  assert_equal(a, mock_new.return_value)
  # representation: (self: A, *args: Any, **kwargs: Any) -> None

# Generated at 2022-06-14 13:03:26.027474
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    configurable_base = Configurable.configurable_base
    configurable_base()



# Generated at 2022-06-14 13:03:37.008056
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    import threading
    from datetime import timedelta

    class Loop(Configurable):
        __impl_class = None

        @classmethod
        def configure(cls, impl, **kwargs):
            Configurable.configure(cls, impl, **kwargs)

        @staticmethod
        def configurable_default():
            return Loop

        @staticmethod
        def configurable_base():
            return Loop

        def initialize(self, impl, **kwargs):
            print(
                "{} initilizing with impl {} {}".format(
                    self.__class__.__name__, impl, kwargs
                )
            )

        def start(self):
            pass

        @staticmethod
        def instance():
            return Loop()

    # default
    loop = Loop()

# Generated at 2022-06-14 13:03:44.184054
# Unit test for function import_object
def test_import_object():
    import tornado.escape
    assert import_object('tornado.escape') is tornado.escape
    assert import_object('tornado.escape.utf8') is tornado.escape.utf8
    assert import_object('tornado') is tornado
    try:
        import_object('tornado.missing_module')
    except ImportError:
        pass
    else:
        assert False, 'expected ImportError'



# Generated at 2022-06-14 13:03:54.464916
# Unit test for function import_object
def test_import_object():
    def assert_import(name, expected):
        actual = import_object(name)
        if actual is not expected:
            raise AssertionError(
                "import_object(%r) is not %r" % (name, expected)
            )
    assert_import("os", os)
    assert_import("os.path", os.path)
    assert_import("tornado.escape", tornado.escape)
    assert_import("tornado.escape.utf8", tornado.escape.utf8)
    assert_import("tornado", tornado)
    try:
        import_object("tornado.missing_module")
    except ImportError:
        pass
    else:
        raise AssertionError("import_object(missing_module) did not fail")



# Generated at 2022-06-14 13:04:03.322930
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def __init__(self, a=None, **kw):
            self.a = a
            self.kw = kw

    A.configure(None, a=1, b=2)
    a = A()
    assert a.a == 1
    assert a.kw == {'b': 2}

    a = A(3)
    assert a.a == 3
    assert a.kw == {'b': 2}

    a = A(a=4)
    assert a.a == 4
    assert a.kw == {'b': 2}

    a = A(5, b=6)
    assert a.a == 5
    assert a.kw == {'b': 6}



# Generated at 2022-06-14 13:04:11.204774
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise OSError(1, "error1")
    except OSError as e:
        assert 1 == errno_from_exception(e)

    try:
        raise IOError(2, "error2")
    except IOError as e:
        assert 2 == errno_from_exception(e)

    try:
        raise ValueError("error")
    except ValueError as e:
        assert None is errno_from_exception(e)

    try:
        raise Exception("error")
    except Exception as e:
        assert None is errno_from_exception(e)


_FILE_CACHE: Dict[str, str] = {}

# True if we're running on Google App Engine.

# Generated at 2022-06-14 13:04:20.245421
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    o = ObjectDict()
    o.name = 'value'
    assert o.name == 'value'
    assert o['name'] == 'value'



# Generated at 2022-06-14 13:04:25.267197
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # Test "__getattr__" method of class "ObjectDict"
    class TestClass(ObjectDict):
        def __init__(self):
            self.test_attribute = 42

    obj = TestClass()
    # Assertion
    assert obj.test_attribute == 42
    # Assertion
    assert obj["test_attribute"] == 42



# Generated at 2022-06-14 13:04:37.579782
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # type: () -> None
    def f(a, b, c=10, d=11, e=12):
        # type: (int, int, int, int, int) -> None
        pass

    a = ArgReplacer(f, "c")
    assert a.arg_pos is None

    # Replace a positional arg
    old_value, args, kwargs = a.replace(13, (1, 2, 3), {})
    assert old_value == 3
    assert args == (1, 2, 13)
    assert kwargs == {}

    # Replace a positional arg with a keyword arg
    old_value, args, kwargs = a.replace(13, (1, 2, 3), {"c":14})
    assert old_value == 3
    assert args == (1, 2, 13)
    assert k

# Generated at 2022-06-14 13:04:39.748329
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    '''
    def initialize(self, *args, **kwargs):
        pass
    '''
    # pass


# Generated at 2022-06-14 13:04:48.345194
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # test positional args
    class Foo(Configurable):
        def configurable_base(self):
            return Foo

        def configurable_default(self):
            return Foo

        def initialize(self, arg):
            self.arg = arg

    f = Foo(42)
    assert f.arg == 42
    # test keyword args
    class Bar(Configurable):
        def initialize(self, arg=None):
            self.arg = arg

        @classmethod
        def configurable_base(cls):
            return Bar

        @classmethod
        def configurable_default(cls):
            return Bar

    b = Bar()
    assert b.arg is None
    b = Bar(arg=42)
    assert b.arg == 42



# Generated at 2022-06-14 13:05:00.800522
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b, c, d):
        return a, b, c, d

    r = ArgReplacer(f, "c")
    old, args, kwargs = r.replace(10, (1, 2, 3, 4), {})
    assert old == 3
    assert args == (1, 2, 10, 4)
    assert kwargs == {}

    r = ArgReplacer(f, "b")
    old, args, kwargs = r.replace(10, (1, 2, 3, 4), {})
    assert old == 2
    assert args == (1, 10, 3, 4)
    assert kwargs == {}

    r = ArgReplacer(f, "d")
    old, args, kwargs = r.replace(10, (1, 2, 3), {})

# Generated at 2022-06-14 13:05:13.509041
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_fn(arg1, arg2=None):
        return "OK"
    arg0 = ArgReplacer(test_fn, "arg1")
    # arg1 is passed positionally
    assert arg0.get_old_value((1,), {}, 0) == 1
    # arg1 is passed by keyword
    assert arg0.get_old_value((), {"arg1": 2}, 0) == 2
    # arg1 is omitted
    assert arg0.get_old_value((), {}, 0) == 0
    # arg1 is omitted and no default is provided
    assert arg0.get_old_value((), {}) is None
    assert arg0.get_old_value((), {}, None) is None
    arg1 = ArgReplacer(test_fn, "arg2")
    # arg2 is passed positionally

# Generated at 2022-06-14 13:05:24.744155
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # testing ordinary class
    class A(object):
        # impl class is A
        def __init__(self, x, y):
            pass
    
    class AnInterface(Configurable):
        def configurable_base(self):
            return AnInterface
        def configurable_default(self):
            return A
    
    an_interface = AnInterface(3, 4)
    assert isinstance(an_interface, A)
    
    # testing two levels of configurability
    class B(object):
        # impl class is B
        def __init__(self, x, y):
            pass
    
    class AnotherInterface(Configurable):
        def configurable_base(self):
            return AnInterface
        def configurable_default(self):
            return B
    

# Generated at 2022-06-14 13:05:29.795674
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, arg_pos=None):
        arg_pos=ArgReplacer(func, 'arg_pos')
        return arg_pos.get_old_value((a, b, 1, 2), {'arg_pos': 2})
    assert func(1, 1) == 2
    assert func(1, 2, 3) == 3
    assert func(2, 3, 4) == 4

# Generated at 2022-06-14 13:05:34.317297
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Example(Configurable):
        def __init__(self, **kwargs):
            super(Example, self).__init__(**kwargs)
        def configurable_base(self):
            return Example
        def configurable_default(self):
            return Example
    Example.configure(Example, name="value")
    example = Example()
    assert isinstance(example, Example)

# Generated at 2022-06-14 13:05:59.006186
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class SomeClass(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

        def _initialize(self, arg):
            self.arg = arg

        initialize = _initialize
    assert SomeClass(1).arg == 1
    assert SomeClass.configure(None, 2)
    assert SomeClass(3).arg == 2
    assert SomeClass.configure(None, 4)
    assert SomeClass().arg == 4
    assert SomeClass.configure(None)
    assert SomeClass().arg is None



# Generated at 2022-06-14 13:06:11.745202
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # XXX: test case is not full

    class ImplOne(Configurable):
        def initialize(self):
            self.data = 1

    class ImplTwo(Configurable):
        def initialize(self):
            self.data = 2


# Generated at 2022-06-14 13:06:16.759575
# Unit test for function import_object
def test_import_object():
    def test_import_basics():
        # basic import
        from tornado.test.util import ObjectDict
        assert import_object(ObjectDict.__module__ + '.' + ObjectDict.__name__) is ObjectDict
        # invalid queries
        for query in ('', 'foo', 'foo.bar.baz'):
            try:
                import_object(query)
                assert False, "import_object should fail on %r" % query
            except ImportError:
                pass

    def test_relative_import():
        # import from inside a package
        from tornado.web import url
        assert url == import_object('tornado.web.url')

    def test_import_package():
        # test that a package can be imported as an object
        import tornado
        assert tornado == import_object('tornado')

   

# Generated at 2022-06-14 13:06:22.138478
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(name, age, sex):
        return 'name: {}, age: {}, sex: {}'.format(name,age,sex)
    args = ('Alex','22','male')
    kwargs = {'sex':'female'}
    default = 'None'
    print(ArgReplacer(foo, 'sex').get_old_value(args, kwargs, default))
    # female
    kwargs = {}
    print(ArgReplacer(foo, 'sex').get_old_value(args, kwargs, default))
    # None


# Generated at 2022-06-14 13:06:24.596956
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    test_class = Configurable
    test_instance = test_class()
    test_instance.initialize()



# Generated at 2022-06-14 13:06:34.835222
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c, d=4):
        pass
    ar = ArgReplacer(func, 'd')
    test_args = (1, 2, 3)
    test_kwargs = {'d': 5}
    # test when the argument is not passed
    assert 4 == ar.get_old_value(test_args, {}, 4)
    # test when the argument is passed positionally
    assert 5 == ar.get_old_value(test_args, test_kwargs, 4)
    ar = ArgReplacer(func, 'a')
    # test when the argument is passed positionally
    assert 1 == ar.get_old_value(test_args, test_kwargs, 4)
    # test when the argument is omitted

# Generated at 2022-06-14 13:06:45.540414
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class ABC(Configurable):
        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return A

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return ABC

        def initialize(self):
            # type: () -> None
            pass

    class A(ABC):
        def initialize(self, a=None):
            # type: () -> None
            self.a = a

    class B(ABC):
        def initialize(self, b=None):
            # type: () -> None
            self.b = b

    class C(ABC):
        def initialize(self, c=None):
            # type: () -> None
            self.c = c

    ABC

# Generated at 2022-06-14 13:06:53.628176
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception()
    except Exception as e:
        assert errno_from_exception(e) is None

    try:
        raise Exception(1)
    except Exception as e:
        assert errno_from_exception(e) == 1

    try:
        raise IOError()
    except IOError as e:
        assert errno_from_exception(e) is None

    try:
        raise IOError(2)
    except IOError as e:
        assert errno_from_exception(e) == 2



# Generated at 2022-06-14 13:07:00.417964
# Unit test for function import_object
def test_import_object():
    # test with a module
    assert import_object("sys") == sys
    # test with a module function
    assert import_object("sys.exit") == sys.exit
    # test with a class
    assert import_object("unittest.TestCase") == unittest.TestCase
    # test with a function
    assert import_object("functools.partial") == functools.partial
    # test with a method
    assert (
        import_object("unittest.TestCase.assertTrue") == unittest.TestCase.assertTrue
    )



# Generated at 2022-06-14 13:07:08.996350
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(first_arg, second_arg=None):
        return True
    arg_replacer = ArgReplacer(f, "second_arg")
    
    args = (1,)
    kwargs = {}
    output = arg_replacer.get_old_value(args, kwargs)
    print(output)
    
    args = (1, 2)
    kwargs = {}
    output = arg_replacer.get_old_value(args, kwargs, default=3)
    print(output)
    
    args = (1,)
    kwargs = {'second_arg': 2}
    output = arg_replacer.get_old_value(args, kwargs)
    print(output)


# Generated at 2022-06-14 13:07:52.200439
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_func(a, b, c, d=None, e=None):
        pass

    arg_replacer = ArgReplacer(test_func, "c")
    assert arg_replacer.get_old_value(
        args=(1, 2, 3, 4), kwargs={}, default=5
    ) == 3
    assert arg_replacer.get_old_value(
        args=(1, 2, 3), kwargs={}, default=5
    ) == 3
    assert arg_replacer.get_old_value(
        args=(1, 2, 3, 4), kwargs={"c": 6}, default=5
    ) == 6

    arg_replacer = ArgReplacer(test_func, "d")

# Generated at 2022-06-14 13:08:00.316562
# Unit test for function import_object
def test_import_object():
    assert import_object('sys') is sys
    assert import_object('sys.modules') is sys.modules
    assert import_object('tornado.escape') is escape
    assert import_object('tornado.escape.native_str') is escape.native_str
    assert import_object('tornado.escape.utf8') is escape.utf8
    try:
        import_object('tornado.missing_module')
        assert False, "should have received an exception"
    except ImportError as e:
        assert "No module named missing_module" in str(e)


# Generated at 2022-06-14 13:08:03.605513
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Foo(Configurable):
        def initialize(self, a, b=5, **kwargs):
            pass

        @classmethod
        def configurable_base(cls):
            return Foo

        @classmethod
        def configurable_default(cls):
            return Foo

    Foo().initialize(1, b=2)



# Generated at 2022-06-14 13:08:09.504417
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class MyConfig(Configurable):
        @classmethod
        def configurable_base(cls): return MyConfig

        @classmethod
        def configurable_default(cls): return MyConfig
        def initialize(self): pass
    a = MyConfig()
    b = MyConfig()
    assert a
    assert b


# Generated at 2022-06-14 13:08:14.507258
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import __main__
    glob = {'__file__': __main__.__file__}
    loc = {}
    docstr_template = """Docstring of {name} class."""
    if '__main__' not in glob:
        raise Exception("{} is not __main__".format(glob.get('__file__')))



# Generated at 2022-06-14 13:08:21.247150
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return B

    class B(A):
        def initialize(self):
            self.b = 2

    class C(A):
        def initialize(self, c):
            self.c = c
    assert A().b == 2
    assert C(c=3).c == 3


# Generated at 2022-06-14 13:08:32.163539
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class BaseClass(Configurable):
        @classmethod
        def configurable_base(cls):
            return BaseClass

        @classmethod
        def configurable_default(cls):
            return DefaultClass

        def initialize(self, *args, **kwargs):
            pass
    class DefaultClass(BaseClass):
        pass
    class SubClass1(BaseClass):
        pass
    class SubClass2(BaseClass):
        pass

    assert SubClass1() is not SubClass2()
    assert isinstance(SubClass1(), BaseClass)

    BaseClass.configure(SubClass2)
    assert SubClass1() is not SubClass2()
    assert isinstance(SubClass1(), BaseClass)

    BaseClass.configure(None)
    assert SubClass1() is not SubClass2()

# Generated at 2022-06-14 13:08:42.458637
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def demo_func1(arg1, arg2, arg3 = 'default_arg3'):
        pass

    func = demo_func1
    assert ArgReplacer(func, "arg1").get_old_value(['arg1_value', 'arg2_value'], {}) == 'arg1_value'
    assert ArgReplacer(func, "arg2").get_old_value(['arg1_value', 'arg2_value'], {}) == 'arg2_value'
    assert ArgReplacer(func, "arg3").get_old_value(['arg1_value', 'arg2_value'], {}) == 'default_arg3'

# Generated at 2022-06-14 13:08:46.309722
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MyClass(Configurable):
        def __new__(cls, *args, **kwargs):
            return object.__new__(cls)
        def __init__(self, *args, **kwargs):
            pass
    assert isinstance(MyClass(), MyClass)

# Generated at 2022-06-14 13:08:52.003441
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class DummyConfigurable(Configurable):
        def configurable_base(self):
            pass

        def configurable_default(self):
            pass

        def initialize(self, *args, **kwargs):
            pass

    try:
        DummyConfigurable(1, 2, 3)
        pass
    except Exception as e:
        raise e



# Generated at 2022-06-14 13:10:03.826468
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from mock import patch
    from unittest import TestCase

    class MockConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

        def initialize(self):
            pass

    class MockImpl(MockConfigurable):
        pass

    def mock_import_object(name):
        if name != "mock_impl":
            raise ImportError()
        return MockImpl

    @patch("tornado.util.import_object", side_effect=mock_import_object)
    def test_configure_str(mock_import_object):
        # type: (Mock) -> None
        MockConfigurable.configure("mock_impl")
        obj = MockConfigurable()


# Generated at 2022-06-14 13:10:07.933165
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return A

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return cls

        def initialize(self):
            # type: () -> None
            pass

    class B(A):
        def initialize(self):
            # type: () -> None
            pass

    assert type(A()) is A
    assert type(B()) is B

    A.configure("tornado.util.A")
    assert type(A()) is A
    assert type(B()) is A

    # Test the recursive nature of Configurable.
    class C(A):
        pass


# Generated at 2022-06-14 13:10:19.879357
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_func(a1, a2, k1=1):
        pass
    args = (0, 0)
    kwargs = {"k2": 2}
    obj = ArgReplacer(test_func, "k1")
    old_value, args, kwargs = obj.replace(2, args, kwargs)
    assert old_value == 1
    assert args == (0, 0)
    assert kwargs == {"k1": 2, "k2": 2}
    old_value, args, kwargs = obj.replace(3, args, kwargs)
    assert old_value == 2
    assert args == (0, 0)
    assert kwargs == {"k1": 3, "k2": 2}

# Generated at 2022-06-14 13:10:22.772558
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Unit test for method __new__ of class Configurable
    pass



# Generated at 2022-06-14 13:10:31.223201
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return cls

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return cls

    class A(Base):
        def initialize(self, a):
            # type: (Any) -> None
            self.a = a

    class B(Base):
        def initialize(self, b):
            # type: (Any) -> None
            self.b = b

    a_obj = A(1)
    assert isinstance(a_obj, A)
    assert a_obj.a == 1

    B.configure(A)
    b_obj = B(2)


# Generated at 2022-06-14 13:10:35.857247
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Foo(Configurable):
        x = 123

        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

        def initialize(self):
            pass

    assert Foo.__impl_class is None
    assert Foo().x == 123
    assert isinstance(Foo(), Foo)
    assert Foo.configured_class() is Foo



# Generated at 2022-06-14 13:10:43.341179
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Base(Configurable):
        def configurable_base(self):
            return Base

        def configurable_default(self):
            return Base

    class Impl(Base):
        pass

    # Test with no implementation set
    assert Base.__impl_class is None
    instance = Base()
    assert isinstance(instance, Base)
    assert not isinstance(instance, Impl)

    # Test with implementation set to Base
    Base.configure(Base)
    instance = Base()
    assert isinstance(instance, Base)
    assert not isinstance(instance, Impl)

    # Test with implementation set to Impl
    Base.configure(Impl)
    instance = Base()
    assert isinstance(instance, Base)
    assert isinstance(instance, Impl)



# Generated at 2022-06-14 13:10:50.616044
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b):
        pass
    r = ArgReplacer(func, 'a')
    assert r.get_old_value(('a','b'), {}) == 'a'
    assert r.get_old_value(('a','b'), {'a':'a_in_dict'}) == 'a'
    assert r.get_old_value(('a','b'), {'b':'b_in_dict'}) == None
    assert r.get_old_value(('a','b'), {'b':'b_in_dict'}, 'hello') == 'hello'

# Generated at 2022-06-14 13:10:55.089982
# Unit test for function errno_from_exception
def test_errno_from_exception():
    from errno import ENOENT  # type: ignore
    try:
        raise IOError(ENOENT, "No such file or directory")
    except Exception as e:
        assert errno_from_exception(e) == ENOENT

    try:
        raise IOError()
    except Exception as e:
        assert errno_from_exception(e) is None

    try:
        raise IOError(42, "No such file or directory")
    except Exception as e:
        assert errno_from_exception(e) == 42

    class CustomException(Exception):
        # exception with no args
        pass

    try:
        raise CustomException()
    except Exception as e:
        assert errno_from_exception(e) is None


# Generated at 2022-06-14 13:11:04.476731
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class ABC(Configurable):
        @classmethod
        def configurable_base(cls):
            return ABC

        @classmethod
        def configurable_default(cls):
            return ABCDefault

    class ABCDefault(ABC):
        def initialize(self):
            self.foo = "\nABCDefault\n"

    class ABCExtension(ABC):
        def initialize(self):
            self.foo = "\nABCExtension\n"

    assert isinstance(ABC(), ABC)
    assert isinstance(ABC(), ABCDefault)
    assert ABC().foo == "\nABCDefault\n"

    saved_kwargs = dict(ABC.configurable_base.__impl_kwargs)

    ABC.configure("tests.test_util.ABCExtension")
    assert isinstance(ABC(), ABC)