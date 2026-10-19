

# Generated at 2022-06-14 13:01:53.095395
# Unit test for function import_object
def test_import_object():
    from tornado.escape import utf8 as escape_utf8
    assert import_object("tornado.escape") is escape
    assert import_object("tornado.escape.utf8") is escape_utf8
    assert import_object("tornado") is tornado
    try:
        import_object("tornado.missing_module")
        raise AssertionError("expected failure")
    except ImportError:
        pass



# Generated at 2022-06-14 13:01:58.940594
# Unit test for function import_object
def test_import_object():
    import tornado.escape
    assert import_object('tornado.escape') is tornado.escape
    assert import_object('tornado.escape.utf8') is tornado.escape.utf8
    assert import_object('tornado') is tornado
    try:
        import_object('tornado.missing_module')
        assert False, "import_object did not throw when importing missing module"
    except ImportError:
        pass

_DEFAULT_TEMPLATE_LOADERS = {
    "tornado": "tornado.template.Loader",
    "jinja2": "tornado.template.Loader",
    "mako": "tornado.template.Loader",
}



# Generated at 2022-06-14 13:02:04.814956
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # test_conf.py
    from tornado.httpserver import HTTPServer

    class MyHTTP(HTTPServer):
        pass

    from unittest.mock import patch

    with patch.object(MyHTTP, "configured_class") as mock_configured_class:
        MyHTTP()
        assert mock_configured_class.called



# Generated at 2022-06-14 13:02:11.641529
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # Create an object of class ArgReplacer
    obj = ArgReplacer(test_ArgReplacer_replace, 'old_value')
    # Create a global variable for testing
    a = 10
    b = 20
    args = [a]
    kwargs = dict(old_value=b)
    # The function should return with the value of the replaced argument
    assert obj.replace(a + b, *args, **kwargs) == (b, [a + b], dict())
    # Test with positional argument
    c = 'a'
    d = 'b'
    args = [c, d]
    kwargs = dict(old_value=b)
    assert obj.replace(c + d, *args, **kwargs) == (b, [c + d, d], dict())



# Generated at 2022-06-14 13:02:20.047189
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    '''
    Replace second argument of a function call
    '''
    def given_func(first, second):
        return first, second

    # given
    args = ["one", "two"]
    # and
    kwargs = {}
    # and
    replace_arg_pos = 1
    # and
    replaced_value = "replaced"

    # when
    old_value, args, kwargs = ArgReplacer(given_func, "second").replace(replaced_value, args, kwargs)

    # then
    assert old_value == args[replace_arg_pos] == "two"
    assert args[replace_arg_pos - 1] == kwargs["first"] == "one"


# Generated at 2022-06-14 13:02:25.403542
# Unit test for function raise_exc_info
def test_raise_exc_info():
    # type: () -> None
    def f():
        # type: () -> typing.NoReturn
        raise ValueError("hello")
    def g():
        # type: () -> typing.NoReturn
        try:
            f()
        except:
            raise_exc_info(sys.exc_info())
    g()



# Generated at 2022-06-14 13:02:35.770740
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    # type: () -> None
    assert ArgReplacer(lambda: None, "foo").arg_pos is None
    assert ArgReplacer(lambda foo: None, "foo").arg_pos is None
    assert ArgReplacer(lambda foo=None: None, "foo").arg_pos is None
    assert ArgReplacer(lambda foo, bar: None, "foo").arg_pos == 0
    assert ArgReplacer(lambda foo, bar: None, "bar").arg_pos == 1
    assert ArgReplacer(lambda foo, bar, baz=None: None, "foo").arg_pos == 0
    assert ArgReplacer(lambda foo, bar, baz=None: None, "baz").arg_pos is None
    assert ArgReplacer(lambda foo, *args: None, "foo").arg_pos == 0

# Generated at 2022-06-14 13:02:44.737350
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from . import httputil

    with mock.patch.object(httputil.HTTPServerConnectionDelegate, "initialize") as m_initialize:
        with mock.patch.object(httputil, "ClientConnection"), mock.patch(
            "socket.socket",
        ):
            # Instantiate the configured class via the abstract base class.
            httputil.HTTPConnection(
                "localhost", 80, True, io_loop=mock.MagicMock()  # type: ignore
            )
            m_initialize.assert_called_once_with(  # type: ignore
                "localhost",
                80,
                True,
                io_loop=mock.ANY,
            )



# Generated at 2022-06-14 13:02:46.717013
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """Test case for method __new__ of class Configurable
    """
    # TODO: to implement



# Generated at 2022-06-14 13:02:50.055927
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test_func(a, b=list, c=2):
        pass
    replacer = ArgReplacer(test_func, 'b')
    assert replacer.get_old_value(('a',), {}, default=1) == list
    assert replacer.get_old_value(('a',), {}, default=1) == 1


# Generated at 2022-06-14 13:03:11.878150
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class BaseConfigurableClass(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return BaseConfigurableClass

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return DefaultConfigurableClass

    class DefaultConfigurableClass(BaseConfigurableClass):
        def __new__(cls, *args, **kwargs):
            # type: (Any, Any) -> Any
            return "instance"

    @classmethod
    def get_args(cls, *args, **kwargs):
        # type: (*Any, **Any) -> Tuple[Any, Any]
        return args, kwargs


# Generated at 2022-06-14 13:03:25.182159
# Unit test for function errno_from_exception
def test_errno_from_exception():
    class A(Exception):
        pass
    try:
        raise A()
    except A as e:
        errno=errno_from_exception(e)
        assert errno is None
    class B(Exception):
        def __init__(self, errno):
            super().__init__(errno)
            self.errno = errno
    try:
        raise B(3)
    except B as e:
        errno=errno_from_exception(e)
        assert errno == 3
    class C(Exception):
        def __init__(self, errno):
            super().__init__(errno)
    try:
        raise C(3)
    except C as e:
        errno=errno_from_exception(e)
        assert errno == 3


# Generated at 2022-06-14 13:03:36.596713
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f1(a1, a2, a3, a4):
        raise NotImplementedError()

    assert (None, (1,), {"a2":2, "a3":3, "a4":4}) == ArgReplacer(f1, "a1").replace(1, (), {"a2":2, "a3":3, "a4":4})
    assert (2, (1,), {"a2":1, "a3":3, "a4":4}) == ArgReplacer(f1, "a2").replace(1, (1,), {"a2":2, "a3":3, "a4":4})

# Generated at 2022-06-14 13:03:49.434093
# Unit test for function errno_from_exception
def test_errno_from_exception():
    import errno
    try:
        raise IOError(errno.EIO, os.strerror(errno.EIO))
    except Exception as e:
        assert e.errno == errno_from_exception(e)
    try:
        raise IOError()
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise IOError("foo")
    except Exception as e:
        assert errno_from_exception(e) == "foo"


# Re-raise a traceback (most likely from sys.exc_info()) with the last
# and original tb frames replaced with frames from `frames`.
# All other traceback frames are preserved.
# Patching the tb from sys.exc_info() directly is not allowed,
# so we use the _some_

# Generated at 2022-06-14 13:03:57.983503
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():

    import os
    import tempfile

    # Need non-ASCII characters that work in both python 2 and 3.
    # Doctest itself doesn't preserve enough state to run the test
    # twice in the same process.  It runs the test twice in two
    # separate processes, but the the two tests use different
    # temp directories and thus have different file contents.
    #
    # The explicit newline and carriage returns also seem to matter.

    char_file_content = '/tmp/こんにちは\nhello\r\n'
    byte_file_content = char_file_content.encode('utf-8')

    # python 2
    if sys.version_info[0] < 3:
        char_file_content = char_file_content.decode('utf-8')


# Generated at 2022-06-14 13:04:07.100021
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """Test for Configurable.__new__
    """
    # Test with a class that has its own __new__
    from tornado.httpserver import HTTPServer

    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfig

        def initialize(self, *args, **kwargs):
            pass

    class TestConfig(TestConfigurable):
        pass

    s = HTTPServer(TestConfigurable)
    assert isinstance(s, TestConfig)

    # Test with a class that doesn't have its own __new__
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable


# Generated at 2022-06-14 13:04:12.415451
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from types import MethodType
    from types import FunctionType

    class Inheritor(Configurable):
        def configurable_base(self):
            return Configurable

        def configurable_default(self):
            return Inheritor

        def initialize(self):
            print("initialize")

    i = Inheritor()
    i.initialize


# Generated at 2022-06-14 13:04:22.637595
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    from functools import partial
    args = (1, 2, 3)
    kwargs = {'y':4, 'z':4}
    new_value = 6
    def myFunc(*args, **kwargs):
        pass
    old_value, args, kwargs = ArgReplacer(myFunc, 'x').replace(new_value, args, kwargs)
    assert old_value == None
    assert args == (1, 2, 3)
    assert kwargs == {'y':4, 'z':4, 'x':6}
    old_value, args, kwargs = ArgReplacer(myFunc, 'y').replace(new_value, args, kwargs)
    assert old_value == 4
    assert args == (1, 2, 3)

# Generated at 2022-06-14 13:04:27.275570
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # type: () -> None
    def func(a, b=None):  # type: ignore
        pass
    cls = ArgReplacer(func, "a")
    assert cls.replace(999, (1, 2), {}) == (1, (999, 2), {})
    assert cls.replace(999, (), {"a": 1}) == (1, (), {"a": 999})
    assert cls.replace(999, (), {}) == (None, (), {"a": 999})
    cls = ArgReplacer(func, "b")
    assert cls.replace(999, (1, 2), {"b": 2}) == (2, (1, 2), {"b": 999})
    assert cls.replace(999, (), {"b": 1}) == (1, (), {"b": 999})

# Generated at 2022-06-14 13:04:39.446241
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A:
        
        def __init__(self, a1):
            self.a1 = a1
        def _initialize(self, a1):
            self.a1 = a1
        initialize = _initialize
    class B(A, Configurable):
        @classmethod
        def configurable_base(cls):
            return cls
        @classmethod
        def configurable_default(cls):
            return cls
    class C(B):
        @classmethod
        def configurable_base(cls):
            return B
    B.configure(None)
    assert isinstance(B(1), B)
    assert isinstance(C(2), C)
    assert C(2).a1 == 2
    B.configure(C)
    assert isinstance(B(3), C)

# Generated at 2022-06-14 13:05:10.454999
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from mock import Mock
    cls = Mock(
        configurable_base=Mock(return_value=1),
        configurable_default=Mock(return_value=2),
        configurable_base=Mock(side_effect=NotImplementedError()),
        configurable_default=Mock(side_effect=NotImplementedError()),
        __new__=Mock(return_value=3),
    )
    assert Configurable.__new__(cls) == 3

# Generated at 2022-06-14 13:05:16.370851
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class BaseTest(Configurable):
        def __init__(self):
            raise NotImplementedError("Don't call __init__")

        def initialize(self, a):
            self.a = a

    class SubTest1(BaseTest):
        pass

    class SubTest2(BaseTest):
        pass

    class SubTestNotA(BaseTest):
        pass


# Generated at 2022-06-14 13:05:23.734513
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MyConf(Configurable):
        def configurable_base(self):
            return MyConf
        def configurable_default(self):
            return MyConf
        def initialize(self):
            pass
    MyConf.configure(None)
    # I don't really know how to test this.
    # There is no such thing as an abstract class in Python.
    # So I just call these methods
    MyConf.configurable_base()
    MyConf.configurable_default()
    MyConf.initialize()



# Generated at 2022-06-14 13:05:33.242632
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class TestImplClass(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestImplClass

        @classmethod
        def configurable_default(cls):
            return TestImplClass

        def initialize(self, test_data: str = None):
            self.test_data = test_data

    TestImplClass.configure(TestImplClass)

    # empty arguments
    assert isinstance(TestImplClass(), TestImplClass)
    # keyword arguments only
    assert TestImplClass().test_data is None
    # keyword arguments only, defined
    assert TestImplClass(test_data='test').test_data == 'test'
    # keyword arguments only, not defined
    assert TestImplClass(test_data=None).test_data is None



# Generated at 2022-06-14 13:05:35.897649
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    obj = ObjectDict({'key1': 'value1', 'key2': 'value2'})
 
    assert obj.key1 == 'value1'
    assert obj.key2 == 'value2'
 

# Generated at 2022-06-14 13:05:45.859019
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class DerivedConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return DerivedConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return DerivedConfigurable

        def _initialize(self):
            # type: () -> None
            pass

    DerivedConfigurable.configure(None)
    assert isinstance(DerivedConfigurable(), DerivedConfigurable)
    assert isinstance(DerivedConfigurable(k=1, z=2), DerivedConfigurable)



# Generated at 2022-06-14 13:05:50.140945
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.escape import utf8
    from tornado.web import RequestHandler
    import tornado.ioloop

    class TestHandler(RequestHandler):
        def initialize(self, arg):
            self.arg = arg

        def get(self):
            self.write("data")

    old_impl = utf8.__impl_class
    old_kwargs = utf8.__impl_kwargs

# Generated at 2022-06-14 13:05:52.496693
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    o = ObjectDict()
    assert o.xxx is None
    o.xxx = 1
    assert o.xxx == 1
    assert o['xxx'] == 1

# Generated at 2022-06-14 13:05:56.918238
# Unit test for function errno_from_exception
def test_errno_from_exception():
    class TestErrnoException(Exception):
        pass
    assert errno_from_exception(TestErrnoException()) == None
    try:
        raise TestErrnoException(1)
    except TestErrnoException as e:
        assert errno_from_exception(e) == 1



# Generated at 2022-06-14 13:05:58.597605
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    assert Configurable.initialize({},1,2,3)==None
    assert Configurable.initialize({},a=1,b=2,c=3)==None


# Generated at 2022-06-14 13:06:13.818853
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class BaseClass(Configurable):
        def configurable_base(self):
            return BaseClass
        def configurable_default(self):
            return BaseClass
    class SubClass1(BaseClass):
        pass
    class SubClass2(BaseClass):
        pass
    class SubClass2_1(SubClass2):
        pass
    class SubClass2_2(SubClass2):
        pass

    # BaseClass is not configured.
    # class is SubClass1 and no args and kwargs
    assert isinstance(BaseClass(), SubClass1)
    assert isinstance(BaseClass(x='a'), SubClass1)
    assert isinstance(BaseClass(x=1), SubClass1)
    assert isinstance(BaseClass("abc"), SubClass1)
    assert isinstance(BaseClass(1,2), SubClass1)

# Generated at 2022-06-14 13:06:15.625390
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import pdb
    pdb.set_trace()
    pass



# Generated at 2022-06-14 13:06:27.454887
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class NewConfigurable(Configurable):
        @classmethod
        def configurable_base(self):
            return NewConfigurable
        @classmethod
        def configurable_default(self):
            return NewConfigurableImpl
    class NewConfigurableImpl(NewConfigurable):
        def _initialize(self):
            self._value = 1
    class NewConfigurableSubclass(NewConfigurable):
        pass
    obj = NewConfigurable()
    assert isinstance(obj, NewConfigurableImpl)
    assert obj._value == 1

    class NewConfigurableImpl2(NewConfigurable):
        def _initialize(self):
            self._value = 1
    NewConfigurable.configure(NewConfigurableImpl2)
    obj = NewConfigurable()
    assert isinstance(obj, NewConfigurableImpl2)
    assert obj._value == 1

# Generated at 2022-06-14 13:06:36.492170
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class Concrete(Configurable):

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Concrete

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return Concrete

        def initialize(self, x, y=1):
            # type: (int, int) -> None
            self.x = x
            self.y = y

    Concrete.configure("tests.util_test.Concrete")
    assert isinstance(Concrete(1), Concrete)
    assert Concrete(1, 2).x == 1
    assert Concrete(1, 2).y == 2

    class SubConcrete(Concrete):
        pass


# Generated at 2022-06-14 13:06:40.359712
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    d = ObjectDict()
    d.test = 1
    assert d.test == 1
    try:
        d.nonexistent
        assert False
    except AttributeError:
        pass

# Generated at 2022-06-14 13:06:43.127372
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class Obj(Configurable):
        def initialize(self):
            # type: () -> None
            self.foo = 'foo'

    assert Obj().foo == 'foo'



# Generated at 2022-06-14 13:06:54.825094
# Unit test for method __new__ of class Configurable

# Generated at 2022-06-14 13:07:00.123555
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Example(Configurable):
        pass

    Example.configure("mock.Mock")
    assert isinstance(Example(), _mock.Mock)

    Example.configure("mock.NonExistentClass")
    with pytest.raises(ImportError):
        Example()


# Generated at 2022-06-14 13:07:06.332488
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError(123)
    except IOError as e:
        assert e.errno == 123
        assert errno_from_exception(e) == 123
    try:
        raise IOError()
    except IOError as e:
        assert e.errno is None
        assert errno_from_exception(e) is None
    try:
        raise TypeError
    except TypeError as e:
        assert e.args == tuple()
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:07:11.574430
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # test_Configurable_initialize
    #
    #    def initialize(self, *args: Any, **kwargs: Any) -> None:
    #        pass

    class TestConfigurable(Configurable):
        def initialize(self, *args, **kwargs):
            pass

    def __init__(self, *args, **kwargs):
        pass

    TestConfigurable.configure(lambda x: TestConfigurable, **{})
    TestConfigurable.configure(lambda x: TestConfigurable, **{})



# Generated at 2022-06-14 13:07:28.666296
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class MyConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return MyConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return MyConfigurableImpl

        def initialize(self, a):
            # type: (str) -> None
            pass

    class MyConfigurableImpl(MyConfigurable):
        pass

    class SubConfigurable(MyConfigurableImpl):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return SubConfigurable


# Generated at 2022-06-14 13:07:41.993779
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    import_err = False
    try:
        from tornado.httpclient import HTTPRequest
    except ImportError:
        import_err = True
    if import_err:
        return
    # The following test case does not work without memoryview support, so we
    # catch the ImportError for later and skip the test.
    try:
        memoryview(b'x')
    except NameError:
        return
    class TestHTTPRequest(Configurable, HTTPRequest):
        @classmethod
        def configurable_base(cls):
            return HTTPRequest

        @classmethod
        def configurable_default(cls):
            return TestHTTPRequest

        @classmethod
        def initialize(cls, *args, **kwargs):
            super(TestHTTPRequest, cls).__init__(*args, **kwargs)

    request = TestHTTP

# Generated at 2022-06-14 13:07:50.913827
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise OSError()
    except OSError as e:
        assert errno_from_exception(e) == None
    try:
        raise OSError(0)
    except OSError as e:
        assert errno_from_exception(e) == 0
    try:
        e = OSError()
        e.errno = 1
        raise e
    except OSError as e:
        assert errno_from_exception(e) == 1
# end of test_errno_from_exception()



# Generated at 2022-06-14 13:08:01.765263
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class DummyImpl(Configurable):
        def __init__(self, a: str, b: str, **kwargs: Any) -> None:
            self.a = a
            self.b = b

        @classmethod
        def configurable_base(cls):
            return DummyImpl

        @classmethod
        def configurable_default(cls):
            return cls

    DummyImpl.configure(None, a='a', b='b')
    assert DummyImpl.__impl_class is None
    assert DummyImpl.__impl_kwargs == {'a': 'a', 'b': 'b'}

    instance = DummyImpl(a='1', b='2')
    assert isinstance(instance, DummyImpl)
    assert instance.a == '1'
    assert instance.b == '2'

# Generated at 2022-06-14 13:08:08.177090
# Unit test for function import_object
def test_import_object():
    try:
        __import__("runtests.test_import_object")
    except ImportError:
        pass
    else:
        raise ImportError("runtests.test_import_object should not exist")
    obj = import_object("runtests.test_import_object")
    assert obj.foobar() == "foobar"



# Generated at 2022-06-14 13:08:11.936038
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    a = ObjectDict({"a": 1})
    assert a.a == 1


# 这个类是用来做协程的超时处理的

# Generated at 2022-06-14 13:08:22.715406
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    class ObjectDict_sub(ObjectDict):
        pass
    OD = ObjectDict()  # type: ObjectDict
    OD.foo = 1
    OD['bar'] = 2
    OD['objectdict_sub'] = ObjectDict_sub()
    OD['objectdict_sub'].foo = 3
    OD['objectdict_sub'].bar = 4
    OD.readonly = 5
    try:
        del OD.readonly  # type: ignore
    except AttributeError:
        pass
    OD._name_ = 'l'
    l = OD.get('_name_')
    l = OD.keys()
    l = OD.values()
    l = OD.items()
    l = OD.__iter__()
    l = OD.__contains__('foo')


# Generated at 2022-06-14 13:08:23.718109
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    pass

# Generated at 2022-06-14 13:08:34.255814
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Item(Configurable):
        def __init__(self, *args, **kwargs):
            pass

        @classmethod
        def configurable_base(cls):
            return Item

        @classmethod
        def configurable_default(cls):
            return Item

    Item.configure(None)
    Item._initialize = Mock(return_value=None)

    # The next two should both result in _initialize being called
    Item(*[], **{})
    Item._initialize.assert_called_once_with()
    Item._initialize = Mock()
    Item(*[1, 2, 3], **{})
    Item._initialize.assert_called_once_with(1, 2, 3)



# Generated at 2022-06-14 13:08:43.484039
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

        def initialize(self, i):
            # type: (int) -> None
            self.i = i

        def __eq__(self, other):
            # type: (Any) -> bool
            return (isinstance(other, TestConfigurable) and
                    other.__class__ == self.__class__ and
                    other.i == self.i)

    # Ensure that __new__ calls __init__
    Configurable.configure(TestConfigurable)
    a = Test

# Generated at 2022-06-14 13:09:23.782167
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        def initialize(self, a=1, b=2, c=3):
            self.a = a
            self.b = b
            self.c = c
        @classmethod
        def configurable_base(cls):
            return TestConfigurable
        @classmethod
        def configurable_default(cls):
            return TestConfigurable

    assert TestConfigurable(1).a == 1
    #assert TestConfigurable.a == 1 #AttributeError: type object 'TestConfigurable' has no attribute 'a'
    assert TestConfigurable(a=10).a == 10
    #assert TestConfigurable.configure(10).a == 10 #AttributeError: type object 'TestConfigurable' has no attribute 'a'


# Generated at 2022-06-14 13:09:36.031696
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TC(Configurable):
        def configurable_base(self):
            return TC
        def configurable_default(self):
            return None
    try:
        TC()
        assert False, 'Not initialize when impl is not configured'
    except:
        assert True
    # following code configures TC.configurable_base with a class, it means that
    # TC class has been configured and now
    TC.configure(TC)
    t = TC()
    # try initialize and _initialize both with and without parameters
    try:
        t.initialize()
    except:
        assert False, 'initialize without parameters failed'
    try:
        t._initialize()
    except:
        assert False, '_initialize without parameters failed'


# Generated at 2022-06-14 13:09:44.458160
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from tornado.concurrent import Future
    from tornado.ioloop import IOLoop
    from tornado.iostream import IOStream
    from tornado.httpclient import HTTPRequest, HTTPResponse, AsyncHTTPClient

    # Unit test for method initialize of class Configurable
    def test_Configurable_initialize():
        # type: () -> None
        from tornado.concurrent import Future
        from tornado.ioloop import IOLoop
        from tornado.iostream import IOStream
        from tornado.httpclient import HTTPRequest, HTTPResponse, AsyncHTTPClient

        # These classes are defined here because they have a complicated
        # metaclass setup that needs the class body to be complete
        # before the class can be created.  This isn't really an issue
        # in real applications.


# Generated at 2022-06-14 13:09:45.050510
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass



# Generated at 2022-06-14 13:09:51.034965
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise Exception
    except Exception as e:
        assert errno_from_exception(e) is None
    try:
        raise IOError
    except IOError as e:
        assert errno_from_exception(e) == 0
    try:
        raise IOError(2)
    except IOError as e:
        assert errno_from_exception(e) == 2
    try:
        raise IOError(2, "Message")
    except IOError as e:
        assert errno_from_exception(e) == 2



# Generated at 2022-06-14 13:09:53.422609
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Child(Configurable):
        def __init__(self):
            pass

    Child.configure(Child)
    __ = Child()



# Generated at 2022-06-14 13:10:03.109845
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():

    class TestConfigurable(Configurable):
        def configurable_base(self):
            return TestConfigurable

        def configurable_default(self):
            return TestConfigurableDefault

    class TestConfigurableDefault():
        def initialize(self, h):
            pass

    TestConfigurable.configured_class()
    TestConfigurable.configure(None, h=1)
    TestConfigurable.configured_class()
    TestConfigurable.configure('tornado.util.TestConfigurableDefault')
    TestConfigurable.configured_class()
    TestConfigurable.configure(TestConfigurableDefault)
    TestConfigurable.configured_class()



# Generated at 2022-06-14 13:10:10.083810
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Object1(Configurable):
        def configurable_base(self):
            return Object1
        def configurable_default(self):
            return Object1
        
    class Object2(Configurable):
        def configurable_base(self):
            return Object1
        def configurable_default(self):
            return Object2
    
    class Object3(Object2):
        def configurable_base(self):
            return Object1
        def configurable_default(self):
            return Object3
            
    # test when impl=None
    Object2.configure(None)
    assert Object2() is Object1()
    assert Object3() is Object1()
    
    # test when impl is a class
    Object2.configure(Object2)
    assert Object2() is Object2()

# Generated at 2022-06-14 13:10:20.780907
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """
    When creating the instance of Configurable class, the __new__ method of
    Configurable class is called.
    """
    class MyConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return MyConfigurable

        @classmethod
        def configurable_default(cls):
            return MyConfigurable

        def __init__(self):
            self.initialized = True

    MyConfigurable()  # When creating the instance of Configurable class, the __new__ method of Configurable class is called.

# Generated at 2022-06-14 13:10:32.558475
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # The tests of Configurable itself are in ioloop_test, but here's
    # a test to prove that a subclass actually works.
    class Example(Configurable):
        @classmethod
        def configurable_base(cls):
            return Example

        @classmethod
        def configurable_default(cls):
            return ExampleImpl

        def method(self):
            return self.attr

        def initialize(self, attr):
            self.attr = attr

    class ExampleImpl(Example):
        def method(self):
            return super(ExampleImpl, self).method() + 1

    Example.configure(None)
    assert isinstance(Example(2), Example)
    assert isinstance(Example(2), ExampleImpl)
    assert Example(2).method() == 3
    assert Example().method() == 3

# Generated at 2022-06-14 13:10:55.226407
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return B

        def initialize(self, name):
            self.name = name

    class B(A):
        def initialize(self, name):
            self.name = name.upper()

    class C(A):
        pass

    # Test normal usage, including inheritance from a configurable class
    A.configure(B)
    assert A("foo").name == "FOO"
    assert B("bar").name == "BAR"
    assert C("baz").name == "baz"

    # Test what happens if there's no base class configured
    A.configure(None)
    assert A("foo").name == "FOO"
   

# Generated at 2022-06-14 13:10:59.922276
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class X(Configurable):
        def configurable_base(cls):
            return X

        def configurable_default(cls):
            return X

        def _initialize(self):
            # type: () -> None
            return

    a = X()
    assert isinstance(a, X)

# Generated at 2022-06-14 13:11:08.584020
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest

    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            return Base

        @classmethod
        def configurable_default(cls):
            return BaseImpl1

        def initialize(self, *args, **kwargs):
            pass

    class BaseImpl1(Base):
        pass

    class BaseImpl2(Base):
        pass

    class Sub(Base):
        @classmethod
        def configurable_base(cls):
            return Sub

        @classmethod
        def configurable_default(cls):
            return SubImpl1

    class SubImpl1(Sub):
        pass

    class SubImpl2(Sub):
        pass


# Generated at 2022-06-14 13:11:10.958114
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    from tornado.sockjs import router
    
    
    
    
    


# Generated at 2022-06-14 13:11:15.433665
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    type = Configurable
    def configurable_base(self):
        return TestConfigurable
    TestConfigurable.configurable_base = classmethod(configurable_base)
    TestConfigurable.configurable_default = classmethod(configurable_default)
    def configurable_default(self):
        return TestConfigurableDefault

# Generated at 2022-06-14 13:11:23.130949
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado import ioloop, platform
    class NewTestConfigurable(Configurable):
        def configurable_base(self):
            pass
        def configurable_default(self):
            pass
    class NewTestConfigurable_Implementation(NewTestConfigurable):
        pass
    NewTestConfigurable.configure(NewTestConfigurable_Implementation, test_kwarg="test_value")
    obj = NewTestConfigurable()
    assert obj is not None, "NewTestConfigurable.__new__ returns a valid object if it is configured"
    assert isinstance(obj, NewTestConfigurable_Implementation), "NewTestConfigurable.__new__ returns an object of the configured class"

# Generated at 2022-06-14 13:11:24.223553
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    x = Configurable() # Does not throw error



# Generated at 2022-06-14 13:11:25.512977
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    x= Configurable()
    print(x)

# Generated at 2022-06-14 13:11:30.851778
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class Dummy(Configurable):
        def configurable_base():
            return Dummy
        def configurable_default():
            return Dummy
        def initialize(self, **kwargs):
            self.dummy_kwargs = kwargs
    Dummy.configure(None, a=1, b=2)
    assert Dummy().dummy_kwargs == {'a': 1, 'b': 2}


# Generated at 2022-06-14 13:11:32.627274
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    """def __new__(self, *args, **kwargs):"""
    raise NotImplementedError()