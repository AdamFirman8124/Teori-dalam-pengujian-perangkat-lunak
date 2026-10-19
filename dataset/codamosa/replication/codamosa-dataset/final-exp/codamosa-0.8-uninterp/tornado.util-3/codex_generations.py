

# Generated at 2022-06-14 13:02:01.351633
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MyClass(Configurable):
        @classmethod
        def __new__(self, *args, **kwargs):
            return super(MyClass, self).__new__(self, *args, **kwargs)

        @classmethod
        def configurable_base(self):
            return MyClass

        @classmethod
        def configurable_default(self):
            return MyClass

    # Test case 1
    instance = MyClass()
    assert isinstance(instance, MyClass)

    # Test case 2
    class Impl(MyClass):
        def _initialize(self):
            pass

    my_class = MyClass()
    assert isinstance(my_class, MyClass)  # type: ignore
    assert not isinstance(my_class, Impl)  # type: ignore

    MyClass.configure(Impl)
   

# Generated at 2022-06-14 13:02:06.890993
# Unit test for function import_object
def test_import_object():
    import unittest
    import tornado.escape
    class TestImportObject(unittest.TestCase):
        def test_import_object(self):
            self.assertTrue(import_object('tornado.escape') is tornado.escape)
            self.assertTrue(import_object('tornado.escape.utf8') is tornado.escape.utf8)
            self.assertTrue(import_object('tornado') is tornado)
            with self.assertRaises(ImportError):
                import_object('tornado.missing_module')
    unittest.main()



# Generated at 2022-06-14 13:02:13.355471
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c=2, d=4, *args, **kwargs):
        pass

    arg = ArgReplacer(func, 'c')
    value, args, kwargs = arg.replace('new value', (1, 2, 3, 4), {'x': 5})

    print(value)  # 2
    print(args)  # (1, 2, 'new value', 4)
    print(kwargs)  # {'x': 5}



# Generated at 2022-06-14 13:02:16.937777
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def f(a, b=None, c=None):
        pass

    argreplacer_instance = ArgReplacer(f, 'b')
    assert argreplacer_instance.get_old_value((1, 2, 3), {'d': 4}) == 2

# Generated at 2022-06-14 13:02:23.756888
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[A]
            return cls

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[A]
            return cls

        def _initialize(self, *args: Any, **kwargs: Any) -> None:
            pass

    class B(A):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[B]
            return cls

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[B]
            return cls


# Generated at 2022-06-14 13:02:34.630405
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def fun_arg_only(arg): pass
    fun = fun_arg_only
    arg_replacer = ArgReplacer(fun, 'arg')
    assert arg_replacer.get_old_value(args=(), kwargs=dict()) == None
    assert arg_replacer.get_old_value(args=('args',), kwargs=dict()) == 'args'
    assert arg_replacer.get_old_value(args=(), kwargs=dict(arg='kwargs')) == 'kwargs'
    def fun_args_kwargs(arg, *args, **kwargs): pass
    fun = fun_args_kwargs
    arg_replacer = ArgReplacer(fun, 'arg')
    assert arg_replacer.get_old_value(args=(), kwargs=dict()) == None

# Generated at 2022-06-14 13:02:36.735694
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        def initialize(self):
            ...

    t = TestConfigurable()
    assert isinstance(t, TestConfigurable)



# Generated at 2022-06-14 13:02:40.491215
# Unit test for function raise_exc_info
def test_raise_exc_info():
    try:
        raise ValueError('test')
    except ValueError as e:
        try:
            raise_exc_info(sys.exc_info())
        except ValueError:
            return
    # assert false
    raise ValueError('test failed')


# Generated at 2022-06-14 13:02:50.393019
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    assert issubclass(Configurable, object)
    assert hasattr(Configurable, '__new__')
    assert callable(Configurable.__new__)
    assert hasattr(Configurable, 'configurable_base')
    assert callable(Configurable.configurable_base)
    assert hasattr(Configurable, 'configurable_default')
    assert callable(Configurable.configurable_default)
    assert hasattr(Configurable, '_initialize')
    assert callable(Configurable._initialize)
    assert hasattr(Configurable, 'initialize')
    assert callable(Configurable.initialize)
    assert hasattr(Configurable, 'configure')
    assert callable(Configurable.configure)
    assert hasattr(Configurable, 'configured_class')

# Generated at 2022-06-14 13:02:59.612326
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(a, b, c): pass
    assert ArgReplacer(foo, "b").replace(
        1, (2, 3, 4), {"c": 5}) == (3, (2, 1, 4), {"c": 5})
    assert ArgReplacer(foo, "c").replace(
        1, (2, 3), {"c": 4}) == (4, (2, 3), {"c": 1})
    assert ArgReplacer(foo, "c").replace(
        1, (2, 3)) == (None, (2, 3), {"c": 1})



# Generated at 2022-06-14 13:03:14.153485
# Unit test for function raise_exc_info
def test_raise_exc_info():

    def _raise_exc_info(exc_info):
        raise_exc_info(exc_info)

    def _raise_custom_error():
        class CustomError(Exception):
            pass

        raise CustomError()

    # Test that the correct exception information is raised.
    try:
        try:
            _raise_custom_error()
        except Exception:
            exc_info = sys.exc_info()
            _raise_exc_info(exc_info)
    except CustomError:
        pass
    else:
        raise AssertionError("The correct exception was not raised")

    # Test that the exception traceback is properly transferred.
    exc_info = None
    try:
        _raise_custom_error()
    except Exception:
        exc_info = sys.exc_info()

# Generated at 2022-06-14 13:03:23.208562
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b, c="c", *args):
        pass

    args = (1, 2)
    kwargs = {"d": 4, "c": 3}
    replacer = ArgReplacer(f, "c")
    assert replacer.arg_pos is None
    assert replacer.get_old_value(args, kwargs) == 3
    assert replacer.replace(10, args, kwargs) == (3, (1, 2), {"d": 4, "c": 10})



# Generated at 2022-06-14 13:03:26.957971
# Unit test for function raise_exc_info
def test_raise_exc_info():
    # type: () -> None
    try:
        raise TypeError("foo")
    except TypeError:
        raise_exc_info(sys.exc_info())
raise_exc_info(None)  # type: ignore



# Generated at 2022-06-14 13:03:32.854566
# Unit test for function raise_exc_info
def test_raise_exc_info():
    def f():
        raise Exception("foobar")

    def g():
        try:
            f()
        except Exception:
            raise_exc_info(sys.exc_info())

    with pytest.raises(Exception) as ex:
        g()
    assert "foobar" in str(ex.value)


# Empty exception raised by `with_timeout`. It is intentionally
# not defined at the top level of this module so that it does not
# conflict with user code. (Although Python's exception mechanism makes
# this difficult since there is no way to prevent users from
# creating their own exceptions with the same name.)

# Generated at 2022-06-14 13:03:44.234222
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def append_a_to_b(a, b=[]):
        b.append(a)
        return b

    replacer = ArgReplacer(append_a_to_b, "b")
    assert replacer.get_old_value((1,), {}) == []
    assert replacer.get_old_value((1, 2), {}) == 2
    assert replacer.get_old_value((1,), {"b": 3}) == 3
    assert replacer.get_old_value((1,), {}) == []
    assert replacer.get_old_value((1,), {"b": 3}) == 3
    assert replacer.get_old_value((1,), {"b": None}, default=9) == 9



# Generated at 2022-06-14 13:03:54.912507
# Unit test for function raise_exc_info
def test_raise_exc_info():
    # type: () -> None
    def inner():
        # type: () -> typing.NoReturn
        try:
            raise ZeroDivisionError
        except ZeroDivisionError:
            raise_exc_info(sys.exc_info())

    # Raises an error if the function doesn't actually raise an
    # exception (e.g. if it runs successfully)
    with pytest.raises(ZeroDivisionError):
        inner()


# Fake byte literal support:  In python 2.6+, you can say b"foo" to get
# a byte literal (str in 2.x, bytes in 3.x).  There's no way to do this
# in a way that supports 2.5, though, so we need a function wrapper
# to convert our string literals.  b() should only be applied to literal
# latin1 strings.  Once

# Generated at 2022-06-14 13:04:04.448871
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # we have to use the base class by name since we have not defined any
    # subclasses
    from tornado.iostream import IOStream
    from tornado.netutil import bind_sockets
    from tornado.simple_httpclient import SimpleAsyncHTTPClient
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncHTTPTestCase, get_unused_port


    class TestIOStream(IOStream):
        def initialize(self, *args, **kwargs):
            super().initialize(*args, **kwargs)


    class TestClient(SimpleAsyncHTTPClient):
        def initialize(self, *args, **kwargs):
            super().initialize(*args, **kwargs)



# Generated at 2022-06-14 13:04:12.071542
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b, c):
        pass
    arg = ArgReplacer(f, "b")
    new_value = "new_b"
    o, n_args, n_kwargs = arg.replace(new_value, (3, "old_b", 5), {"c": 7})
    assert o == "old_b"
    assert n_args == (3, new_value, 5)
    assert n_kwargs == {"c": 7}
    #
    o, n_args, n_kwargs = arg.replace(new_value, (3,), {"b": "old_b", "c": 7})
    assert o == "old_b"
    assert n_args == (3,)
    assert n_kwargs == {"b": new_value, "c": 7}
    #
    o

# Generated at 2022-06-14 13:04:18.579816
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception(1, 'error')
    except Exception as e:
        assert errno_from_exception(e) == 1
    try:
        raise Exception('error')
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise Exception()
    except Exception as e:
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:04:23.777814
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



# Generated at 2022-06-14 13:04:41.523961
# Unit test for function raise_exc_info
def test_raise_exc_info():
    # Emulate __exit__(*exc_info)
    def check_exc_info(
        e0,  # type: Union[Optional[Type[BaseException]], Optional[BaseException]]
        e1,  # type: Optional[BaseException]
        e2,  # type: Optional[TracebackType]
    ):
        # type: (...) -> bool
        raise_exc_info([type(e1), e1, e2])
        return False

    # Emulate try: ... except: ...

# Generated at 2022-06-14 13:04:43.422538
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # __new__ is tested in the unittest of subclass `GzipDecompressor` below
    pass



# Generated at 2022-06-14 13:04:54.944753
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def d(x=5, y=6):
        pass
    arg = ArgReplacer(d, "x")
    old_value, args, kwargs = arg.replace(10, (), {"y":2})
    assert args == ()
    assert kwargs == {"y": 2, "x": 10}
    assert old_value == 5
    # Test that args is not mutated
    old_value, args2, kwargs = arg.replace(20, (), {"y":2})
    assert args2 == ()
    assert kwargs == {"y": 2, "x": 20}
    assert args == ()
    # Test non-empty args
    old_value, args, kwargs = arg.replace(30, (1, 2, 3), {"y": 2})
    assert args == (1, 2, 3)
   

# Generated at 2022-06-14 13:04:58.394639
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Foo(Configurable):
        @classmethod
        def configurable_default(cls):
            pass
        def configurable_base(cls):
            pass
    f = Foo()



# Generated at 2022-06-14 13:05:06.544177
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Child(Configurable):
        @classmethod
        def configurable_base(cls):
            return Child

        @classmethod
        def configurable_default(cls):
            return cls

        def initialize(self):
            self.init_args = (1, 2)
            self.init_kwargs = {"x": 1, "y": 2}

    class Child2(Child):
        def initialize(self, *args, **kwargs):
            super(Child2, self).initialize(*args, **kwargs)
            self.child2_args = (1, 2, 3)
            self.child2_kwargs = {"x": 1, "y": 2, "z": 3}


# Generated at 2022-06-14 13:05:08.078009
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    pass

# Generated at 2022-06-14 13:05:09.753632
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    _test_Configurable___new__()



# Generated at 2022-06-14 13:05:10.466629
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass

# Generated at 2022-06-14 13:05:13.093857
# Unit test for function raise_exc_info
def test_raise_exc_info():
    try:
        raise Exception('error')
    except:
        raise_exc_info(sys.exc_info())



# Generated at 2022-06-14 13:05:24.413715
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    atexit.register(test_Configurable_initialize.cleanup)
    @configurable(ABC)
    class A(ABC):
        pass
    assert A.configured_class() is A
    A._save = A._save_configuration
    A._restore = A._restore_configuration
    assert A.configured_class() is A
    assert A._save() == (None, {})
    saved = A._save()
    A.configure(None)
    assert A.configured_class() is A
    assert A._save() == (None, {})
    A._restore(saved)
    assert A.configured_class() is A
    assert A._save() == (None, {})
    test_Configurable_initialize.cleanup()


# Generated at 2022-06-14 13:05:38.356092
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test(a, b=None, c=None):
        pass
    arg_replacer = ArgReplacer(func=test, name="b")
    assert arg_replacer.get_old_value(args=[2, 3], kwargs={}) == 3
    assert arg_replacer.get_old_value(args=[2], kwargs={"c": 3}) == 3
    assert arg_replacer.get_old_value(args=[2], kwargs={}) is None
    assert arg_replacer.get_old_value(args=[], kwargs={}) is None

    assert arg_replacer.replace(5, args=[2, 3], kwargs={}) == (3, [2, 5], {})

# Generated at 2022-06-14 13:05:49.851250
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def _func(a, b, c, d=0, e=0, f=0):
        pass
    name = 'd'
    new_value = 99
    args = (1, 2, 3)
    kwargs = {'f': 8, 'b': 2}
    replacer = ArgReplacer(_func, name)
    old_value, new_args, new_kwargs = replacer.replace(new_value, args, kwargs)
    assert old_value == 0
    assert new_args == (1, 2, 3)
    assert new_kwargs == {'f': 8, 'b': 2, 'd': 99}
    replacer = ArgReplacer(_func, 'b')

# Generated at 2022-06-14 13:05:58.038712
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    a = "a"
    b = "b"
    c = "c"
    d = "d"

    def test_func(x, y, z, w = "w"):
        print(x, y, z, w)

    (ret1, args, kwargs) = ArgReplacer(test_func, "w").replace(a, ("x", "y", "z"), {})
    assert(ret1 is None)
    assert(args == ("x", "y", "z"))
    assert(kwargs == {"w" : a})

    (ret1, args, kwargs) = ArgReplacer(test_func, "w").replace(a, "x", {"w" : b, "y" : "y", "z" : "z"})
    assert(ret1 == b)

# Generated at 2022-06-14 13:06:10.166439
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class C_with_new(Configurable):
        def __new__(cls, *args, **kwargs):
            # type: (Type[C_with_new], *Any, **Any) -> C_with_new
            return super().__new__(cls, *args, **kwargs)

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[C_with_new]
            return C_with_new

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[C_with_new]
            return C_with_new


# Generated at 2022-06-14 13:06:15.170693
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    """Unit test for method __getattr__ of class ObjectDict."""
    dates = ObjectDict(
        {"month": 3,
         "day": 5,
         "year": 2004})
    try:
        _ = dates.foo
    except AttributeError as e:
        pass
    else:
        raise AssertionError("AttributeError not raised")


# Generated at 2022-06-14 13:06:22.568623
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def aaa(a, b=5):
        return a, b

    aaaa = ArgReplacer(aaa, "a")
    aaa.a = aaaa
    aaa.aaa = aaa
    oov1 = aaaa.get_old_value((1, 2), {}, None)
    oov2 = aaaa.get_old_value((1, 2), {"a": 3}, None)
    oov3 = aaaa.get_old_value((1, 2), {"b": 4}, None)
    oov4 = aaaa.get_old_value((1, 2), {"a": 3, "b": 4}, None)
    assert(oov1 == 1)
    assert(oov2 == 3)
    assert(oov3 == None)
    assert(oov4 == 3)

# Unit

# Generated at 2022-06-14 13:06:26.637124
# Unit test for function raise_exc_info
def test_raise_exc_info():
    def run():
        raise Exception("hello")

    def func2(excinfo):
        raise_exc_info(excinfo)

    try:
        run()
    except Exception as e:
        func2(exc_info())



# Generated at 2022-06-14 13:06:36.022443
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    def _configurable_base(cls): # type: (Type[Any]) -> 'Configurable'
        return cls

    def _configurable_default(cls): # type: (Type[Any]) -> 'Configurable'
        return cls

    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls): # type: () -> Type[Configurable]
            return _configurable_base(cls)

        @classmethod
        def configurable_default(cls): # type: () -> Type[Configurable]
            return _configurable_default(cls)

        def __init__(self, *args, **kwargs): # type: (Any, Any) -> ()
            pass


# Generated at 2022-06-14 13:06:44.968696
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise OSError(5, "Some random error")
    except OSError as e:
        assert errno_from_exception(e) == 5
    try:
        raise OSError("Some random error")
    except OSError as e:
        assert errno_from_exception(e) == 0
    try:
        raise OSError()
    except OSError as e:
        assert errno_from_exception(e) == 0
    try:
        raise Exception
    except Exception as e:
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:06:51.112842
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(x, y, z):
        pass
    arg_replacer = ArgReplacer(foo, "y")
    assert arg_replacer.get_old_value((1, 2, 3), {}, 4) == 2
    assert arg_replacer.get_old_value((), {"y": 1}, 4) == 1
    assert arg_replacer.get_old_value((), {}, 4) == 4



# Generated at 2022-06-14 13:07:09.543942
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise OSError(5, "Error")
    except Exception as e:
        errno = errno_from_exception(e)
        assert errno == 5



# Generated at 2022-06-14 13:07:14.024888
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class DummyConfigurable(Configurable):
        """Dummy implementation of Configurable"""
        configurable_base = lambda self: DummyConfigurable  # type: Callable
        configurable_default = lambda self: DummyConfigurable  # type: Callable
        def _initialize(self, *args, **kwargs):
            """ initialize method of class DummyConfigurable"""
            pass
    # check that the right exception is raised if there is no
    # configuration for a given class
    with pytest.raises(ValueError) as ve_ctx:
        DummyConfigurable()
    assert "configured class not found" in str(ve_ctx.value)

# Generated at 2022-06-14 13:07:19.987600
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.httpserver
    import tornado.httpclient

    tornado.httpserver.HTTPServer

    class MyHTTPClient(tornado.httpclient.AsyncHTTPClient):
        def initialize(self, *args: Any, **kwargs: Any) -> None:
            pass

    try:
        # Test that a subclass of a configurable class is also configurable
        MyHTTPClient.configure(MyHTTPClient)
        client = MyHTTPClient()
        assert isinstance(client, MyHTTPClient)
    finally:
        MyHTTPClient.configure(None)
        # Test that we can restore the original configuration after
        # we changed it.
        MyHTTPClient()



# Generated at 2022-06-14 13:07:28.101601
# Unit test for function errno_from_exception
def test_errno_from_exception():
    from errno import EACCES
    e = IOError("error message")
    assert errno_from_exception(e) == EACCES
    e = IOError()
    assert errno_from_exception(e) == EACCES
    e = IOError(EACCES)
    assert errno_from_exception(e) == EACCES
    e = IOError(EACCES, "error message")
    assert errno_from_exception(e) == EACCES
    e = Exception()
    assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:07:36.745038
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():  # noqa
    class A(Configurable):
        def initialize(self, x, y, z=5):
            pass

        def configurable_base(self):
            return self.__class__

        def configurable_default(self):
            return self.__class__
    assert issubclass(A, Configurable)
    assert isinstance(A(1, 2), A)
    assert isinstance(A(1, 2, 3), A)



# Generated at 2022-06-14 13:07:42.139171
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return A

        def initialize(self, a, b, c=None):
            pass

    A.configure(None, c=3)
    a = A(1, 2)



# Generated at 2022-06-14 13:07:46.368715
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class T(Configurable):
        @classmethod
        def configurable_base(cls):
            return T

        @classmethod
        def configurable_default(cls):
            return T

    t = T()
    return t



# Generated at 2022-06-14 13:07:54.197000
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(x, y, z):
        pass

    a = ArgReplacer(foo, "y")
    # value found (passed positionally)
    assert a.get_old_value(("x", "y", "z"), {}, None) == "y"
    # value found (passed by keyword)
    assert a.get_old_value(("x",), {"y": "y", "z": "z"}, None) == "y"
    # value not found
    assert a.get_old_value(("x",), {"z": "z"}, "default") == "default"



# Generated at 2022-06-14 13:08:03.776299
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_func_1(a, b, c):
        pass
    def test_func_2(a, b=0, c=0):
        pass

    replacer = ArgReplacer(test_func_1, 'a')
    old_value, new_args, new_kwargs = replacer.replace(1, (10, 20, 30), {})
    assert old_value == 10
    assert new_args == (1, 20, 30)
    assert new_kwargs == {}

    replacer = ArgReplacer(test_func_1, 'b')
    old_value, new_args, new_kwargs = replacer.replace(2, (10, 20, 30), {})
    assert old_value == 20
    assert new_args == (10, 2, 30)
    assert new_kwargs == {}

# Generated at 2022-06-14 13:08:15.094428
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class Conf(Configurable):
        @classmethod
        def configurable_default(cls):
            # type: () -> Any
            return "default"
        @classmethod
        def configurable_base(cls):
            # type: () -> Any
            return Conf
    # Test the default case
    assert isinstance(Conf(), str)
    # Test the configured case
    Conf.configure(impl=int)
    assert isinstance(Conf(), int)
    # Test the keyword argument case
    class SConf(Configurable):
        initialized = False
        def initialize(self, arg):
            # type: (Any) -> None
            self.arg = arg
            self.initialized = True

# Generated at 2022-06-14 13:08:39.326615
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class DummyConfigurable(Configurable):
        def initialize(self, a, b=False):
            self.a = a
            self.b = b

        @classmethod
        def configurable_base(cls):
            return DummyConfigurable  # type: ignore

        @classmethod
        def configurable_default(cls):
            return DummyConfigurable  # type: ignore

    class Subclass(DummyConfigurable):
        pass

    # Configure it at the base
    DummyConfigurable.configure("tests.test_util.test_Configurable_initialize.Subclass", b=True)
    # A direct instantiation of the base class gives us an instance
    # of the configured class.
    instance = DummyConfigurable("a")
    assert isinstance(instance, Subclass)

    # The configured class is

# Generated at 2022-06-14 13:08:43.675583
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    base = Configurable

    impl = Configurable

    class C(Configurable):

        @classmethod
        def configurable_base(cls):
            return base

        @classmethod
        def configurable_default(cls):
            return impl

    class D(C):
        pass

    C.configure(D)
    assert C() is not None



# Generated at 2022-06-14 13:08:54.253969
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    from unittest import mock
    from typing import Any, Dict
    from tornado.util import Configurable
    from tornado.testing import AsyncTestCase
    class MyConfigurable(Configurable):
        @classmethod
        def configurable_base(self):
            # type: () -> Type[Configurable]
            return MyConfigurable
        @classmethod
        def configurable_default(self):
            # type: () -> Type[Configurable]
            return MyConfigurableImpl
    class MyConfigurableImpl(MyConfigurable):
        def initialize(self, a: int, b: str, c: float = 0.1, **kwargs: Any) -> None:
            # type: (...) -> None
            pass
        def _initialize(self) -> None:
            # type: (...) -> None
            pass

# Generated at 2022-06-14 13:09:01.234355
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(a, b, c=14, d=15, e=16):
        pass

    arg_replacer = ArgReplacer(foo, "b")
    assert arg_replacer.replace(1, (2, 3), {}) == (3, (2, 1), {})
    #
    arg_replacer = ArgReplacer(foo, "d")
    assert arg_replacer.replace(1, (2, 3), {}) == (None, (2, 3), {"d": 1})
    #
    arg_replacer = ArgReplacer(foo, "e")
    assert arg_replacer.replace(1, (2, 3), {}) == (None, (2, 3), {"e": 1})



# Generated at 2022-06-14 13:09:09.660385
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class Subclass(Configurable):
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Subclass

        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return Subclass

        def _initialize(self):
            # type: () -> None
            pass

    Subclass.configure(None)
    c = Subclass()
    assert c  # suppress pyflakes warning
test_Configurable___new__()



# Generated at 2022-06-14 13:09:16.362334
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return B

        def initialize(self):
            pass

    class B(A):
        def initialize(self):
            pass

    a = A()
    assert isinstance(a, B)
    assert not isinstance(a, A)



# Generated at 2022-06-14 13:09:18.572847
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    objectdict = ObjectDict()
    result = objectdict.__getattr__("test")


# Generated at 2022-06-14 13:09:24.657404
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    import mock

    class Dummy(object):
        pass

    # TODO: more complete testing
    class TestableConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestableConfigurable

        @classmethod
        def configurable_default(cls):
            return Dummy



# Generated at 2022-06-14 13:09:36.982564
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest

    class Potato(Configurable):
        @classmethod
        def configurable_base(cls):
            return Potato

        @classmethod
        def configurable_default(cls):
            return Potato

        def initialize(self, *args, **kwargs):
            pass

        def eat(self):
            self.ate = True

    class SweetPotato(Potato):
        def eat(self):
            self.ate = True

    class Yam(Potato):
        def eat(self):
            self.ate = True

    Potato.configure(SweetPotato)
    potato = Potato()
    potato.eat()
    assert potato.ate

    Potato.configure(Yam)
    potato = Potato()
    potato.eat()
    assert potato.ate

    Potato.configure(None)
    potato

# Generated at 2022-06-14 13:09:38.357553
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    configurable = Configurable()
    configurable.initialize()



# Generated at 2022-06-14 13:09:57.148280
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b, c):
        pass

    rep = ArgReplacer(func, "b")
    old_value, args, kwargs = rep.replace(5, [10, 11, 12], {})
    assert old_value == 11
    assert args == [10, 5, 12]
    assert kwargs == {}



# Generated at 2022-06-14 13:10:03.248267
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class C(Configurable):

        def configurable_base(cls):
            return C

        def configurable_default(cls):
            return cls

        def initialize(self, a: int, b: float) -> None:
            pass

    C.configure(None)
    configurable = C(1, 2.0)
    assert configurable
    assert isinstance(configurable, C)



# Generated at 2022-06-14 13:10:08.007574
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    """Unit test for method ArgReplacer.get_old_value

    """

    def func(a, b=1, *c):
        pass

    arg = ArgReplacer(func, "b")
    assert arg.get_old_value((), {"b": 2}, default=3) == 2
    assert arg.get_old_value((), {}, default=3) == 3
    assert arg.get_old_value((4,), {}, default=3) == 1

# Generated at 2022-06-14 13:10:13.786211
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    this = ObjectDict({'foo': 'a'})
    # AssertionError: bar  !=  a
    assert this.foo  ==  this['foo']
    # AssertionError: AttributeError  !=  KeyError
    assert type(this.bar)  ==  AttributeError



# Generated at 2022-06-14 13:10:22.764385
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from typing import overload
    from tornado.httputil import HTTPRequest
    from tornado.test.test_httputil import HTTPHeaders
    #class HTTPServerRequest(HTTPRequest):
    #    @overload
    #    def initialize(self, *args, **kwargs):
    #        pass
    #    def initialize(self, protocol, **kwargs):
    #        ...
    #httpserverrequest_initialize_expected = """\
    #    def initialize(self, protocol, **kwargs):
    #        super(HTTPServerRequest, self).initialize(**kwargs)
    #        self.protocol = protocol
    #"""
    #print(inspect.getsource(HTTPServerRequest.initialize))
    #print(httpserverrequest_initialize_expected)
    #assert inspect.getsource(HTTPServer

# Generated at 2022-06-14 13:10:33.268469
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # -- Test cases -----------------------------------------------------------

    class C(Configurable):
        def configurable_base(self):
            return C
        def configurable_default(self):
            return C
        def initialize(self):
            return self
    class D(C):
        def configurable_base(self):
            return C
        def configurable_default(self):
            return C
        def initialize(self):
            return C

    # -- Execution ------------------------------------------------------------

    # Case: instantiate a subclass configured to be the default with no args
    assert D() is D()

    # Case: instantiate a subclass configured to be the default with args
    D.configure(None)
    assert D() is D()

    # Case: instantiate a subclass with no args, custom config
    assert D() is D()

    # Case: instantiate a subclass

# Generated at 2022-06-14 13:10:42.098463
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            super(A, self).__init__()
        def configurable_base(self):
            return A
        def configurable_default(self):
            return self
    a1 = A(1, 2, 3, a=4, b=5, c=6)
    assert a1.args == (1, 2, 3)
    assert a1.kwargs == dict(a=4, b=5, c=6)
    A.configure(None, a=1, b=2)
    a2 = A(3, 4, 5, b=6, c=7)
    assert a2.args == (3, 4, 5)

# Generated at 2022-06-14 13:10:44.745485
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Tests New function __new__ of the class Configurable
    # Unit test for method __new__ of class Configurable
    pass



# Generated at 2022-06-14 13:10:52.167738
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_func(a, b, c, d=4):
        pass

    func = ArgReplacer(test_func, "d")
    assert func.get_old_value((1,2,3), {"c": 3, "d": 4}, "default") == 4
    assert func.get_old_value((1,2,3), {"c": 3}, "default") == "default"
    assert func.get_old_value((1,2,3), {}, "default") == "default"
    assert func.get_old_value((1,2), {"c": 3}, "default") == "default"

# Generated at 2022-06-14 13:11:01.181756
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import inspect

    from tornado import ioloop
    from tornado.platform.asyncio import AsyncIOMainLoop

    class DemoConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return DemoConfigurable

        @classmethod
        def configurable_default(cls):
            return DemoConfigurableImpl

        def initialize(self):
            pass

    class DemoConfigurableImpl(DemoConfigurable):
        def initialize(self):
            pass

    DemoConfigurable.configure(DemoConfigurableImpl)
    DemoConfigurable("demo")

