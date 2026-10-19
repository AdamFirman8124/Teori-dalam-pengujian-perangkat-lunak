

# Generated at 2022-06-14 13:01:47.430382
# Unit test for function import_object
def test_import_object():
    assert import_object("urllib.parse") is not None
    assert import_object("urllib") is not None
    assert import_object("urllib.missing_module") is None


# Fake byte literal for testing (python3.2 doesn't have a real b'' syntax).
_TEST_BYTES = "".encode("latin1")



# Generated at 2022-06-14 13:01:52.536722
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class ClassOne(Configurable):
        pass
    class ClassTwo(Configurable):
        pass
    class ClassThree(Configurable):
        pass
    ClassOne.configure(ClassTwo)
    ClassTwo.configure(ClassThree)
    assert isinstance(ClassOne(), ClassOne)


# Generated at 2022-06-14 13:02:01.771429
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c):
        pass
    arg_replacer = ArgReplacer(func, "b")
    old_value = arg_replacer.get_old_value((1, 2, 3), {}, default=4)
    assert old_value == 2
    old_value = arg_replacer.get_old_value((1, 2, 3), {}, default=5)
    assert old_value == 2
    old_value = arg_replacer.get_old_value((1, 2), {}, default=4)
    assert old_value == 4
    old_value = arg_replacer.get_old_value((), {"b":3}, default=4)
    assert old_value == 3

# Generated at 2022-06-14 13:02:11.047011
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def f(a, b, c=None):  # type: ignore
        return a, b, c

    args = (1, 2, 3)
    kwargs = {"a": 5, "c": 6}

    r = ArgReplacer(f, "a")
    answer = 5
    result = r.get_old_value(args, kwargs)
    assert result == answer

    result = r.get_old_value(args, kwargs, default=None)
    assert result == answer

    result = r.get_old_value(args, kwargs, default=7)
    assert result == answer

    r.replace(4, kwargs, args)
    assert kwargs == {"a": 4, "c": 6}

    # Reset func and args
    args = (1, 2, 3)

# Generated at 2022-06-14 13:02:14.826341
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f():
        return (1, 2)
    ar = ArgReplacer(f, 1)
    args = (1, 2, 3)
    kwargs = {}
    print(ar.replace("new_value", args, kwargs))
    pass


# Generated at 2022-06-14 13:02:23.700285
# Unit test for function raise_exc_info
def test_raise_exc_info():
    try:
        raise ValueError()
    except ValueError as e:
        raise_exc_info(sys.exc_info())


# Fake byte literal support:  In python 2.6+, you can say b"foo" to
# get a byte literal (str in 2.x, bytes in 3.x).  There's no way to do
# that in a way that supports 2.5, though, so we need a function
# wrapper to convert our string literals.  b() should only be applied
# to literal latin1 strings.  Once we drop support for 2.5, we can
# remove this function and just use byte literals.

# Generated at 2022-06-14 13:02:27.969936
# Unit test for function import_object
def test_import_object():
    assert import_object('os') is os
    assert import_object('os.path') is os.path
    assert import_object('tornado.escape') is escape
    assert import_object('tornado.escape.utf8') is escape.utf8


# Generated at 2022-06-14 13:02:37.218173
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import tornado.gen
    from tornado.httpserver import HTTPServer
    from tornado.iostream import IOStream
    from tornado.tcpserver import TCPServer
    from tornado.testing import AsyncTestCase, bind_unused_port

    class Func(Configurable, object):
        def configurable_base(cls):
            return Func

        def configurable_default(cls):
            return ReturnOne

        def initialize(self, num):
            self.num = num

        def test(self):
            return self.num

    class ReturnOne(Func):
        def initialize(self):
            super(ReturnOne, self).initialize(1)

    class ReturnTwo(Func):
        def initialize(self):
            super(ReturnTwo, self).initialize(2)

    Func.configure(ReturnTwo)

# Generated at 2022-06-14 13:02:41.033372
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    #Test class Configurable
    conf = Configurable()
    assert type(conf).__name__ == "Configurable"

    #Test function configure
    conf.configure(conf, **{})
    assert type(conf).__name__ == "Configurable"




# Generated at 2022-06-14 13:02:47.073282
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c, d=0, e=1): pass
    arg = ArgReplacer(func, 'c')
    ret = arg.replace(1, (0,0,'x'), {'d':2,'e':3})
    assert ret[0] == 'x'
    assert ret[1] == (0,0,1)
    assert ret[2] == {'d':2,'e':3}


# Generated at 2022-06-14 13:03:00.540961
# Unit test for function raise_exc_info
def test_raise_exc_info():
    try:
        raise ValueError()
    except ValueError:
        exc_info = sys.exc_info()
        generator = raise_exc_info(exc_info)
        next(generator)
        with pytest.raises(ValueError):
            next(generator)



# Generated at 2022-06-14 13:03:08.999316
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # test for case that the arg to replace is passed positionally

    def test_func(a, b, c):
        return (a, b, c)

    replacer = ArgReplacer(test_func, "b")
    old_value, args, kwargs = replacer.replace(4, (1, 2, 3), {})
    assert(old_value == 2)
    assert(args == (1, 4, 3))
    assert(kwargs == {})

    # test for case that the arg to replace is either omitted or passed by keyword
    def test_func(a=0, b=1, c=2):
        return (a, b, c)

    replacer = ArgReplacer(test_func, "b")
    old_value, args, kwargs = replacer.replace(4, (), {})


# Generated at 2022-06-14 13:03:21.138543
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def _test(arg1, arg2, arg3='', arg4=1, arg5=2):
        return arg1, arg2, arg3, arg4, arg5

    input1 = 'input1'
    input2 = 'input2'
    input3 = 'input3'
    input4 = 'input4'
    input5 = 'input5'

    old_value, args, kwargs = ArgReplacer(_test, 'arg2').replace(input2,
                                                                 (input1,),
                                                                 {'arg3': input3,
                                                                  'arg4': input4,
                                                                  'arg5': input5})
    assert old_value is None
    assert input1 == args[0]
    assert input2 == args[1]

# Generated at 2022-06-14 13:03:31.174569
# Unit test for function raise_exc_info
def test_raise_exc_info():
    try:
        raise ValueError()
    except ValueError:
        exc_info = sys.exc_info()

    assert isinstance(exc_info[1], ValueError)
    raise_exc_info(exc_info)


_MAXSIZE = 2 ** 31 - 1

if hasattr(int, "from_bytes"):  # python 3

    def _unsigned_to_signed(
        n: int, width: int
    ) -> int:  # type: ignore  # https://github.com/python/mypy/issues/3357
        signed_n = n - (1 << width)
        assert signed_n + (1 << width) == n
        return signed_n

    # On python 3.5+, we want to use the implementation from the
    # standard library.
    # Note that this is only for integers <= 2**

# Generated at 2022-06-14 13:03:40.435805
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            return Base
        @classmethod
        def configurable_default(cls):
            return Base
    class A(Base):
        @classmethod
        def configurable_base(cls):
            return A
        @classmethod
        def configurable_default(cls):
            return A
    A.configure(A)
    base = Base()
    assert base.__class__ is Base
    a = A()
    assert a.__class__ is A
    # Type check:
    Base.configure(impl=A)
    a = A()
    assert a.__class__ is A
    a = Base()
    assert a.__class__ is A

# Generated at 2022-06-14 13:03:46.270305
# Unit test for function raise_exc_info
def test_raise_exc_info():

    def raiser(x: int) -> int:
        if x < 3:
            raise_exc_info(raise_exc_info)
        else:
            return x

    try:
        raiser(0)
    except TypeError:
        pass
    else:
        raise Exception("did not raise TypeError")



# Generated at 2022-06-14 13:03:55.170957
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Example(Configurable):
        @classmethod
        def configurable_base(cls):
            return Example

        @classmethod
        def configurable_default(cls):
            return ExampleImpl

    class ExampleImpl(Example):
        def initialize(self, x: int, y: int) -> None:
            self.x = x
            self.y = y

    Example.configure(ExampleImpl)

    ex1 = Example(1, y=2)
    assert isinstance(ex1, Example)
    assert isinstance(ex1, ExampleImpl)
    assert ex1.x == 1
    assert ex1.y == 2



# Generated at 2022-06-14 13:04:04.643978
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class ConfigurableBase(Configurable):

        @classmethod
        def configurable_base(cls):
            return ConfigurableBase

        @classmethod
        def configurable_default(cls):
            return ConfigurableBase

        def initialize(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class DerivedClass(ConfigurableBase):
        pass

    class ConfiguredClass(ConfigurableBase):
        pass

    base = ConfigurableBase()
    derived = DerivedClass()
    ConfigurableBase.configure(None)
    assert(base.__class__.__dict__ == ConfigurableBase.__dict__)
    assert(base.__class__ == ConfigurableBase)
    assert(derived.__class__ == DerivedClass)

# Generated at 2022-06-14 13:04:15.959056
# Unit test for function import_object
def test_import_object():
    import_object("unittest")  # This is a built-in module
    self = import_object("tornado.util.test_import_object")
    assert self is test_import_object


# Fake byte literal support:  In python 2.6+, you can say b"foo" to get
# a byte literal (str in 2.x, bytes in 3.x).  There's no way to do this
# in a way that supports 2.5, though, so we need a function wrapper
# to convert our string literals.  b() should only be applied to literal
# latin1 strings.  Once we drop support for 2.5, we can remove this function
# and just use byte literals.

# Generated at 2022-06-14 13:04:20.360522
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    a = ArgReplacer(func = 'a', name = 1101)
    assert a.replace(new_value=1, args=[1,2,3], kwargs={'name':'1'}) == (1, [1,2,3], {'name':'1'})
    assert a.replace(new_value=2, args=[1,2,3], kwargs={}) == (None, [1,2,3], {1101:2})



# Generated at 2022-06-14 13:04:41.018703
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b):
        pass
    def g(c, d):
        pass
    arg = ArgReplacer(f, 'a')
    assert arg.replace(1, (1, 2), {}) == (1, (1, 2), {})
    arg = ArgReplacer(f, 'b')
    assert arg.replace(2, (1, 2), {}) == (2, (1, 2), {})
    arg = ArgReplacer(f, 'a')
    assert arg.replace(10, (1, 2), {'a':3}) == (3, (1, 2), {'a':3})
    arg = ArgReplacer(f, 'b')
    assert arg.replace(10, (1, 2), {'b':3}) == (3, (1, 2), {'b':3})

# Generated at 2022-06-14 13:04:45.812826
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class ConfigurableTest(Configurable):
        @classmethod
        def configurable_base(cls):
            return ConfigurableTest

        @classmethod
        def configurable_default(cls):
            return ConfigurableTest

        def initialize(self, a, b):
            self.result = a + b

    ConfigurableTest.configure(ConfigurableTest)
    test_instance = ConfigurableTest(a=2, b=3)
    assert test_instance.result == 5
    assert isinstance(test_instance, ConfigurableTest)



# Generated at 2022-06-14 13:04:58.127028
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_method(a, b='default', c='default', d='default'):
        print(a, b, c, d)
    arg_replacer_a = ArgReplacer(test_method, 'a')
    arg_replacer_b = ArgReplacer(test_method, 'b')
    arg_replacer_c = ArgReplacer(test_method, 'c')
    arg_replacer_d = ArgReplacer(test_method, 'd')
    test_method(1, 2, 3, 4)
    arg_replacer_a.replace('new a', args=[1, 2, 3], kwargs={})
    arg_replacer_b.replace('new b', args=[1], kwargs={'b': 2})

# Generated at 2022-06-14 13:05:05.512868
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Class for testing Configurable class
    class TestConfigurable(Configurable):
        def configurable_base(self):
            return 'base'

        def configurable_default(self):
            return 'default'

        def initialize(self):
            pass

    # Tests for method `__new__`
    # Case: When configuration is not set
    with pytest.raises(ValueError):
        TestConfigurable()
    # Case: When configuration is set
    TestConfigurable.configure('default', a=1)
    assert TestConfigurable().configurable_base() == 'base'
    assert TestConfigurable._save_configuration() == ('default', {'a': 1})



# Generated at 2022-06-14 13:05:18.374208
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Configurable_Base_A(Configurable):
        @classmethod
        def configurable_base(cls):
            return Configurable_Base_A
        @classmethod
        def configurable_default(cls):
            return Configurable_A_Impl_1
    class Configurable_A_Impl_1(Configurable_Base_A):
        def initialize(self):
            pass
    class Configurable_A_Impl_2(Configurable_Base_A):
        def initialize(self):
            pass
    class Configurable_Base_B(Configurable):
        @classmethod
        def configurable_base(cls):
            return Configurable_Base_B
        @classmethod
        def configurable_default(cls):
            return Configurable_B_Impl_1

# Generated at 2022-06-14 13:05:27.903326
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.httpserver
    import tornado.ioloop
    from tornado.options import options, define, parse_command_line

    # don't use a global variable for the context, as this test may be
    # invoked multiple times
    def get_ioloop(context):
        class FakeIOLoop(Configurable):
            @classmethod
            def configurable_base(cls):
                return FakeIOLoop

            @classmethod
            def configurable_default(cls):
                return tornado.ioloop.IOLoop

        parse_command_line()
        if context.get("ioloop_implementation"):
            FakeIOLoop.configure(context["ioloop_implementation"])
            if context.get("ioloop_configuration"):
                FakeIOLoop.configure(**context["ioloop_configuration"])

# Generated at 2022-06-14 13:05:37.199043
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    # type: () -> None
    def f(a, b=2):
        pass

    replacer = ArgReplacer(f, "b")
    assert replacer.get_old_value((1,), {}) == 2
    assert replacer.get_old_value((1,), {"b": 3}) == 3
    assert replacer.get_old_value((1,), {"b": 3}, default=4) == 3
    assert replacer.get_old_value((1,), {"c": 3}, default=4) == 4
    assert replacer.get_old_value((1,), {}, default=4) == 4



# Generated at 2022-06-14 13:05:47.969912
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def shuffle(x, y, z=None):
        return x, y, z

    arg_replacer = ArgReplacer(shuffle, 'x')

    assert arg_replacer.replace(2, (1, 3), {}) == (1, (2, 3), {})
    assert arg_replacer.replace(2, (1, 3, 4), {}) == (1, (2, 3, 4), {})

    assert arg_replacer.replace(2, (), {'x':1, 'y':3}) == (1, (), {'x':2, 'y':3})
    assert arg_replacer.replace(2, (), {'y':3}) == (None, (), {'x':2, 'y':3})



# Generated at 2022-06-14 13:05:51.752690
# Unit test for function raise_exc_info
def test_raise_exc_info():
    try:
        raise ValueError(1)
    except Exception as e:
        try:
            raise_exc_info(sys.exc_info())
        except Exception as e2:
            assert type(e2) is type(e)
            assert str(e2) == str(e)



# Generated at 2022-06-14 13:06:00.751977
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func1(a, b, c):
        pass
    
    def func2(a = 0, b = 1, c = 2):
        pass

    # test for function without default value
    arg_replacer = ArgReplacer(func1, "b")
    old_value, args, kwargs = arg_replacer.replace(10, [1, 2, 3], {})
    assert old_value == 2
    assert args == [1, 10, 3]
    assert kwargs is {}

    # test for function with default value
    arg_replacer = ArgReplacer(func2, "b")
    old_value, args, kwargs = arg_replacer.replace(10, [1, 2], {})
    assert old_value is None
    assert args == [1, 2]
    assert kwargs

# Generated at 2022-06-14 13:06:26.783682
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class test_Configurable___new__0(Configurable):
        def __init__(self):
            raise AssertionError('Configurable.__init__() called')
        def initialize(self):
            pass
        @classmethod
        def configurable_base(cls):
            return test_Configurable___new__0
        @classmethod
        def configurable_default(cls):
            return test_Configurable___new__0

    class test_Configurable___new__1(test_Configurable___new__0):
        @classmethod
        def configurable_base(cls):
            return test_Configurable___new__0
        @classmethod
        def configurable_default(cls):
            return test_Configurable___new__0

# Generated at 2022-06-14 13:06:36.127349
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    from mock import Mock
    from mock import patch
    from unittest import TestCase
    from unittest.mock import call

    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return TestConfigurable

        # noinspection PyAbstractClassMethod
        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return TestConfigurable

    class TestConfigurableSubclass(TestConfigurable):
        pass

    class TestConfigurableSubSubclass(TestConfigurableSubclass):
        pass


# Generated at 2022-06-14 13:06:41.840266
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    foo = ObjectDict()
    foo["bar"] = 0
    # __getattr__
    assert foo.bar == 0
    try:
        foo.wrong  # type: ignore
        assert False
    except AttributeError:
        pass
    # __setattr__
    foo.bar = 1
    assert foo["bar"] == 1



# Generated at 2022-06-14 13:06:48.476072
# Unit test for function import_object
def test_import_object():
    # Call it a few different ways with and without dots.
    import tornado.escape

    assert import_object("tornado.escape") is tornado.escape
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8
    assert import_object("tornado") is tornado
    assert import_object("tornado.util") is tornado.util
    assert import_object("util") is tornado.util
    assert import_object("escape") is tornado.escape
    assert import_object("tornado.missing_module")

    # last dot
    with pytest.raises(ImportError):
        import_object("tornado.missing_module.")

    # trailing space
    with pytest.raises(ImportError):
        import_object("tornado.util ")



# Generated at 2022-06-14 13:06:53.372775
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    d = ObjectDict()
    d.first = 1
    d['second'] = 2
    assert d.first == 1
    assert d['second'] == 2
    try:
        d.doesnotexist
        assert False
    except AttributeError:
        pass



# Generated at 2022-06-14 13:07:00.300709
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(a, b, c=3, d=4):
        pass
    assert ArgReplacer(foo, "d").get_old_value((1, 2), {}, None) is None
    assert ArgReplacer(foo, "c").get_old_value((1, 2), {}, None) is None
    assert ArgReplacer(foo, "b").get_old_value((1, 2), {}, None) is 2
    assert ArgReplacer(foo, "a").get_old_value((1, 2), {}, None) is 1

# Generated at 2022-06-14 13:07:04.611362
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    """
    >>> def func(a, b, c):
    ...     pass
    >>> args='1',
    >>> kwargs={}
    >>> replacer = ArgReplacer(func, 'b')
    >>> replacer.replace('2', args, kwargs)
    (None, ('1',), {'b': '2'})
    """

# Generated at 2022-06-14 13:07:11.105210
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def simple_function(arg):
        pass
    arg_replacer = ArgReplacer(simple_function, 'arg')
    old_value, args, kwargs = arg_replacer.replace('X', (), {})
    assert old_value is None
    assert args == ('X',)
    assert kwargs == {}

# Generated at 2022-06-14 13:07:18.289591
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_func(a, b, c="default"):
        return a, b, c

    a = ArgReplacer(test_func, 'b')
    old_value, args, kwargs = a.replace('new_value', ("a", "b",), {"a": "a", "b": "b", "c": "default_c"})
    assert old_value == "b"
    assert args == ("a", "new_value",)
    assert kwargs == {"a": "a", "b": "b", "c": "default_c"}

    with pytest.raises(ValueError):
        ArgReplacer("invalid_func", "b")



# Generated at 2022-06-14 13:07:27.462532
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func1(self, arg1, arg2):
        pass

    args = ("my string", "my second string")
    kwargs = {}
    replacer = ArgReplacer(func1, "arg1")

    assert replacer.get_old_value(args, kwargs) == "my string"
    assert replacer.get_old_value(args, kwargs, "default string") == "my string"

    replacer = ArgReplacer(func1, "arg3")

    assert replacer.get_old_value(args, kwargs) is None
    assert replacer.get_old_value(args, kwargs, "default string") == "default string"


# Generated at 2022-06-14 13:07:49.181372
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # One arg passed positionally, one passed by keyword
    def fn(a, b):
        pass
    replacer = ArgReplacer(fn, "b")
    old, args, kwargs = replacer.replace("B", ("A",), {})
    assert args == ("A",)
    assert kwargs == {}
    assert old is None

    # Both args passed positionally
    old, args, kwargs = replacer.replace("B", ("A", "b"), {})
    assert args == ("A", "B")
    assert kwargs == {}
    assert old == "b"

    # Both args passed by keyword
    old, args, kwargs = replacer.replace("B", (), {"a": "A", "b": "b"})
    assert args == ()

# Generated at 2022-06-14 13:08:00.535338
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return TestConfigurable

        def initialize(self, a, b, c=None):
            # type: (Any, Any, Optional[Any]) -> None
            pass

    TestConfigurable._save_configuration()
    assert isinstance(TestConfigurable(), TestConfigurable)
    TestConfigurable.configure(TestConfigurable, a=10, b=20, c=30)
    assert isinstance(TestConfigurable(), TestConfigurable)
    TestConfigurable.configure(None)
    assert isinstance

# Generated at 2022-06-14 13:08:04.020318
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c=None):
        pass
    ar = ArgReplacer(func, "c")
    assert ar.get_old_value([1,2], {"b":2}) == None
    assert ar.replace(3, [1,2], {"b":2}) == (None, [1,2], {"b":2, "c":3})

# Generated at 2022-06-14 13:08:11.548437
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception
    except:
        assert errno_from_exception(sys.exc_info()[1]) is None
    try:
        raise Exception(42, "foo")
    except:
        assert errno_from_exception(sys.exc_info()[1]) == 42
    try:
        raise Exception("foo")
    except:
        assert errno_from_exception(sys.exc_info()[1]) == "foo"



# Generated at 2022-06-14 13:08:18.609057
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A
        @classmethod
        def configurable_default(cls):
            return A
        def initialize(self,foo=None):
            self.foo = foo
    class B(A):
        pass
    class C(A):
        pass
    # test default
    A.configure(None)
    a = A(foo="foo")
    assert isinstance(a,A)
    assert a.foo == "foo"
    # test configure subclass of default
    A.configure(B)
    a = A()
    assert isinstance(a,B)
    assert a.foo == None
    # test configure none
    A.configure(None)
    a = A(foo="foo")

# Generated at 2022-06-14 13:08:29.366409
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    import inspect
    import functools
    from tornado.testing import gen_test, AsyncTestCase
    @functools.wraps(inspect.getfullargspec)
    def getfullargspec(func):
        if hasattr(func, '__wrapped__'):
            return inspect.getfullargspec(func.__wrapped__)
        else:
            return inspect.getfullargspec(func)
    @functools.wraps(inspect.isgeneratorfunction)
    def isgeneratorfunction(func):
        if hasattr(func, '__wrapped__'):
            return inspect.isgeneratorfunction(func.__wrapped__)
        else:
            return inspect.isgeneratorfunction(func)

# Generated at 2022-06-14 13:08:39.424009
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test(x=None):
        pass
    test = ArgReplacer(test, "x")
    args = (1,)
    kwargs = {"x": 2}
    assert test.get_old_value(args, kwargs) == 1
    args = (2,)
    kwargs = {"x": 3}
    assert test.get_old_value(args, kwargs) == 2
    args = ()
    kwargs = {"x": 4, "y": 5}
    assert test.get_old_value(args, kwargs) == 4
    args = ()
    kwargs = {"y": 5}
    assert test.get_old_value(args, kwargs) == None

# Generated at 2022-06-14 13:08:47.201034
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func():
        pass
    def func(*args):
        return args
    def func(*args, **kwargs):
        return args, kwargs
    def func(x, y, *args):
        return x, y, args
    def func(x, y, *args, **kwargs):
        return x, y, args, kwargs
    def func(*args, y):
        return args, y
    def func(*args, y, **kwargs):
        return args, y, kwargs
    def func(x, *args, y):
        return x, args, y
    def func(x, *args, y, **kwargs):
        return x, args, y, kwargs
    def func(*args, x, y):
        return args, x, y

# Generated at 2022-06-14 13:08:50.655559
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    with mock.patch('tornado.util.import_object') as mock_import_object:
        mock_import_object.return_value = mock.Mock()
        tornado.Auth()
        mock_import_object.assert_called()


# Generated at 2022-06-14 13:08:55.021348
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def f(a, b, c=None):
        pass

    r = ArgReplacer(f, "b")
    assert r.get_old_value((1, 2, 3), {}) == 2
    assert r.get_old_value((1,), {"b": 3}) == 3



# Generated at 2022-06-14 13:09:22.331572
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c):
        pass
    arg_replacer = ArgReplacer(func, 'b')
    args = (1,2,3)
    kwargs = {'b':2, 'c':3}
    old_value = arg_replacer.get_old_value(args, kwargs, None)
    assert old_value == 2


# Generated at 2022-06-14 13:09:29.184744
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class cls_1(Configurable):
        def __init__(self, *args: Any, **kwargs: Any) -> None:
            pass

        def initialize(self, *args: Any, **kwargs: Any) -> None:
            pass

        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

        @classmethod
        def configure(cls, impl, **kwargs):
            pass

        @classmethod
        def configured_class(cls):
            return cls
    class cls_2(cls_1):
        pass
    obj_0 = cls_1()
    obj_1 = cls_2()

# Generated at 2022-06-14 13:09:39.906277
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    """
    test the replace of class ArgReplacer
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            replacer = ArgReplacer(func, "arg_to_replace")
            old_value = replacer.get_old_value(args, kwargs)
            assert old_value == None
            new_value = "test"
            old_value, args, kwargs = replacer.replace(new_value, args, kwargs)
            assert old_value == None
            assert kwargs["arg_to_replace"] == "test"
            func(*args, **kwargs)

        return wrapper


    @decorator
    def test1(arg1, arg2, arg_to_replace=None):
        assert arg_to_replace

# Generated at 2022-06-14 13:09:48.807243
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def f():
        pass

    def g(x):
        pass

    def h(x, y):
        pass

    def j(x=1):
        pass

    def k(x, y=1):
        pass

    def m(x=1, y=2):
        pass

    def n(x=1, y=2, z=3):
        pass

    def p(x, y=1, z=2):
        pass

    def q(x, *args):
        pass

    def r(x, **kwargs):
        pass

    def s(x, *args, **kwargs):
        pass

    def t(**kwargs):
        pass

    def u(*args):
        pass

    def v(x, y=1, *args, **kwargs):
        pass


# Generated at 2022-06-14 13:09:53.009266
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception()
    except Exception as e:
        assert errno_from_exception(e) is None

    try:
        raise SocketError(22)
    except SocketError as e:
        assert errno_from_exception(e) == 22



# Generated at 2022-06-14 13:10:04.609080
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest

    class ConfigurableTest(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

    class ImplementationTest(ConfigurableTest):
        def initialize(self, a, b):
            self.a = a
            self.b = b

    class SubImplementationTest(ImplementationTest):
        pass

    class OtherImplementationTest(ConfigurableTest):
        def initialize(self, a, b):
            self.a = a
            self.b = b

    class ConfigurableTestCase(unittest.TestCase):
        class TestConfigurableTest(ConfigurableTest):
            pass

        def test_default_impl(self):
            impl = ConfigurableTest()
            self.assertIs

# Generated at 2022-06-14 13:10:15.375565
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def __init__(self, *args, **kwargs):
            print('A.__init__', args, kwargs)

    a = A(1, 2, a=3, b=4)
    a.initialize(3, 4, c=5, d=6)
    assert a.__init__ == A.__init__
    assert a.initialize == A.initialize
    b = A(1, 2, a=3, b=4)
    assert b.__init__ != A.__init__
    assert b.initialize != A.initialize



# Generated at 2022-06-14 13:10:23.681427
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    impl = str
    def configurable_base():
        return str
    def configurable_default():
        return impl
    def initialize(self):
        pass
    def _initialize(self):
        pass
    def configure(impl, **kwargs):
        pass
    def configured_class():
        return impl
    def _save_configuration():
        pass
    def _restore_configuration(saved):
        pass

# Generated at 2022-06-14 13:10:32.360686
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    args1 = [2, 3]
    kwargs1 = dict(a=3, b=5)
    argReplacer1 = ArgReplacer(lambda a,b,c,d:0, 'a')
    print(argReplacer1)
    argReplacer1.replace(10, args1, kwargs1)
    assert argReplacer1.get_old_value(args1, kwargs1) == 3
    args2 = [2, 3]
    kwargs2 = dict(a=3, b=5)
    argReplacer2 = ArgReplacer(lambda a,b,c,d:0, 'b')
    print(argReplacer2)
    argReplacer2.replace(10, args2, kwargs2)

# Generated at 2022-06-14 13:10:36.372828
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test(a, b):
        pass
    arg_replacer = ArgReplacer(test, 'a')
    args = None
    kwargs = {'a':1, 'b':2}
    default = 'default'
    old_value = arg_replacer.get_old_value(args, kwargs, default)
    print('old_value:', old_value)


# Generated at 2022-06-14 13:11:03.076030
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class Foo(Configurable):  # type: ignore
        pass

    assert Foo.__impl_class is None
    assert isinstance(Foo(), Foo)

    class Bar(Foo):
        pass

    assert Foo.__impl_class is None
    assert Bar.__impl_class is None
    assert isinstance(Bar(), Bar)

    class Baz(Configurable):
        __impl_class = Bar

    assert Foo.__impl_class is None
    assert Bar.__impl_class is None
    assert Baz.__impl_class is Bar
    assert isinstance(Baz(), Baz)
    assert isinstance(Baz(), Bar)


# Generated at 2022-06-14 13:11:10.528532
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    def test_ObjectDict():
        d = ObjectDict((("foo", "bar"),))
        assert d.foo == "bar"
        assert d["foo"] == "bar"
        assert d.get("foo") == "bar"
        assert d.bar is None
        try:
            d.bar
            assert False
        except AttributeError:
            pass
        d.foo = "baz"
        assert d["foo"] == "baz"
        d["foo"] = "bar"
        assert d.foo == "bar"

    test_ObjectDict()

# Generated at 2022-06-14 13:11:20.084078
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class TestableClass(Configurable):
        def __new__(cls, *args, **kwargs):
            return super(TestableClass, cls).__new__(cls)

        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    class ConfiguredClass(TestableClass):
        def __init__(self, *args, **kwargs):
            self._args = args
            self._kwargs = kwargs
            kwargs["hello"] = 123
            super(ConfiguredClass, self).__init__(*args, **kwargs)

    TestableClass.configure(ConfiguredClass)
    obj = TestableClass(1, 2, 3)
    assert obj.kwargs == {"hello": 123}

# Generated at 2022-06-14 13:11:20.724004
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    pass

# Generated at 2022-06-14 13:11:31.301858
# Unit test for method initialize of class Configurable
def test_Configurable_initialize(): # type: ignore
    import pytest
    import random
    import string

    class TestConfigurable(Configurable):
        # Type annotations on this class are done with comments
        # because they need to refer to Configurable, which isn't defined
        # until after the class definition block. These can use regular
        # annotations when our minimum python version is 3.7.
        __impl_class = None  # type: Optional[Type[Configurable]]
        __impl_kwargs = None  # type: Dict[str, Any]

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return TestConfigurable
