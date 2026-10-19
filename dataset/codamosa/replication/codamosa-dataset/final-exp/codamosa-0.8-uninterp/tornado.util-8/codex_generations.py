

# Generated at 2022-06-14 13:01:37.776486
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError()
    except IOError as e:
        assert None == errno_from_exception(e)
    try:
        raise IOError(2)
    except IOError as e:
        assert 2 == errno_from_exception(e)



# Generated at 2022-06-14 13:01:41.802905
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # import 
    from tornado.util import ObjectDict
    # call
    assert ObjectDict().__getattr__('hi') == 'hi'


# Generated at 2022-06-14 13:01:51.013059
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    global class_Configurable_func_configurable_base, class_Configurable_func_initialize, class_Configurable_func_configured_class

    class class_Configurable_func_configurable_base(Configurable):
        def __init__(self):
            pass
        def configurable_base(cls):
            return class_Configurable_func_configurable_base
        def configurable_default(cls):
            return class_Configurable_func_configurable_default
    class class_Configurable_func_configurable_default(class_Configurable_func_configurable_base):
        def __init__(self):
            pass
    class_Configurable_func_configurable_base.configure(class_Configurable_func_configurable_default)
    class_Configurable_func_impl = class_Configurable_

# Generated at 2022-06-14 13:02:00.567618
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    # type: () -> None
    def f(a, b):
        # type: (Any, Any) -> None
        pass
    ar = ArgReplacer(f, "b")
    # Basic usage
    assert ar.get_old_value((1, 2), {}) == 2
    assert ar.replace(3, (1, 2), {}) == (2, (1, 3), {})
    # Omitted argument
    assert ar.get_old_value((1,), {}) == None
    assert ar.replace(3, (1,), {}) == (None, (1,), {"b": 3})
    # Keyword argument
    assert ar.get_old_value((1,), {"b": 2}) == 2

# Generated at 2022-06-14 13:02:09.668414
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():  # pragma: no cover
    # pylint: disable=missing-docstring,unused-argument

    def func(a, b, c, d=None, e=None):
        pass

    r = ArgReplacer(func, "b")
    assert r.arg_pos == 1
    r = ArgReplacer(func, "e")
    assert r.arg_pos is None
    assert r.get_old_value(("a", "b"), {"d": "d"}) is None
    assert r.get_old_value(("a", "b"), {"e": "e"}) == "e"
    assert r.get_old_value(("a", "b"), {"e": "e"}, "e") == "e"

# Generated at 2022-06-14 13:02:18.300692
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.ioloop
    import tornado.process
    import tornado.web
    # a class that is not subclass of Configurable
    import io
    import os
    import socket
    import time
    import random
    # attribute __impl_class
    tornado.ioloop.IOLoop.__impl_class
    tornado.process.Subprocess.__impl_class
    tornado.web.RequestHandler.__impl_class
    io.TextIOWrapper.__impl_class
    os.PathLike.__impl_class
    os.PathLike.__impl_class
    socket.socket.__impl_class
    time.time.__impl_class
    random.random.__impl_class
    

# Generated at 2022-06-14 13:02:24.716991
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a, b, c, d=5):
        pass
    argr = ArgReplacer(func, 'c')
    old_val = argr.get_old_value((1,2,3), {})
    assert old_val == 3
    old_val = argr.get_old_value((1,2), {'d': 5})
    assert old_val == None


# Generated at 2022-06-14 13:02:35.261385
# Unit test for function errno_from_exception
def test_errno_from_exception():  # type: () -> None
    # no errno provided
    def test_no_errno():  # type: () -> None
        try:
            raise Exception
        except Exception as e:
            errno = errno_from_exception(e)
            assert errno is None, errno
    test_no_errno()
    # errno provided as attribute
    def test_errno_as_attribute():  # type: () -> None
        try:
            raise Exception(None, "x", "y")
        except Exception as e:
            errno = errno_from_exception(e)
            assert errno == "x", errno
    test_errno_as_attribute()
    # errno provided as argument

# Generated at 2022-06-14 13:02:45.149425
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import unittest
    class C(Configurable):
        @classmethod
        def configurable_base(cls):
            return C

        @classmethod
        def configurable_default(cls):
            return C
    class D(C):
        pass
    class E(C):
        def initialize(self, a, b=None):
            self.a = a
            self.b = b

    class TestConfigurable(unittest.TestCase):
        def test_configurable(self):
            d = D()
            self.assertTrue(isinstance(d, D))
            C.configure(E, b=10)
            c = C(1)
            self.assertTrue(isinstance(c, E))
            self.assertEqual(c.a, 1)

# Generated at 2022-06-14 13:02:51.808416
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def f(a, b, c=None, d=None):
        pass

    r = ArgReplacer(f, "d")
    assert r.get_old_value((1, 2), {}) is None
    assert r.get_old_value((1, 2), {"d": 9}) == 9
    assert r.replace(4, (1, 2), {"d": 9}) == (9, (1, 2), {"d": 4})
    assert r.get_old_value((1, 2, 3), {}) == 3
    assert r.replace(4, (1, 2, 3), {}) == (3, (1, 2, 4), {})



# Generated at 2022-06-14 13:03:00.326296
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(a, b=None, c=None):
        print(a)
        print(b)
        print(c)
    p = ArgReplacer(foo, 'b')
    lst = [1, 2, 3]
    lst = p.replace(123, lst, {})
    print(lst[0])



# Generated at 2022-06-14 13:03:08.870867
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    """Test the method replace in class ArgReplacer
    """

    def func_1(a, b, c=3):
        """Test function 1:
        """
        return (a, b, c)

    def func_2(a, b=2, c=3):
        """Test function 2:
        """
        return (a, b, c)

    def func_3(a=1, b=2, c=3):
        """Test function 3:
        """
        return (a, b, c)

    def func_4(a,b,c,d=None,e=None,f=None):
        """Test function 4
        """
        return (a,b,c,d,e,f)

    def func_5(*args):
        """Test function 5
        """
        return args

   

# Generated at 2022-06-14 13:03:20.965262
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_func3(a, b, c):
      pass

    def test_func4(a=1, b=2, c=3):
      pass

    # test_func3 replace c with 1
    argreplacer_test = ArgReplacer(test_func3, 'c')
    old_value, args, kwargs = argreplacer_test.replace(1, (1, 2, 3), {})
    assert old_value == 3
    assert args == (1, 2, 1)
    assert kwargs == {}

    # test_func3 replace c with 1 and c is passed by keyword
    argreplacer_test = ArgReplacer(test_func3, 'c')
    old_value, args, kwargs = argreplacer_test.replace(1, [], {'c': 3})

# Generated at 2022-06-14 13:03:25.548271
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func_call_with_args(arg_list, kwarg_dict):
        # This function mimics a function call and provides a checkable
        # value for the test to pass.
        return arg_list, kwarg_dict

    # Test for the function with arguments passed positionally
    arg_list = ['positional_arg']
    kwarg_dict = {'keyword_arg': 'keyword_arg'}
    arg_replacer = ArgReplacer(func_call_with_args, 'positional_arg')
    # The passed in argument list and keyword arguments should not be mutated.
    assert arg_replacer.get_old_value(arg_list, kwarg_dict) == 'positional_arg'
    assert arg_list == ['positional_arg']

# Generated at 2022-06-14 13:03:35.960290
# Unit test for function import_object
def test_import_object():
    class mock_import(object):

        def __init__(self, _):
            pass

        def __getattr__(self, _):
            return mock_import(_)

        def __call__(self, _):
            return mock_import(_)

    # monkey patch the import
    import sys
    import __builtin__
    real_import = __builtin__.__import__
    try:
        __builtin__.__import__ = mock_import
        mod_name = 'a.b.c.d'
        m = import_object(mod_name)
        assert m == mock_import(mod_name)

    finally:
        __builtin__.__import__ = real_import



# Generated at 2022-06-14 13:03:44.881665
# Unit test for function import_object
def test_import_object():
    import_object_1 = import_object('tornado.escape')
    import_object_2 = import_object('tornado')
    import_object_3 = import_object('tornado.escape.utf8')

# Generated at 2022-06-14 13:03:48.376438
# Unit test for function import_object
def test_import_object():
    import_object('unittest')


_BYTE_MASK = (1 << 8) - 1
_error_codes = dict((k, v) for k, v in zlib.errorcode.items())



# Generated at 2022-06-14 13:03:49.487602
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # assert something about Configurable.initialize
    assert True

# Generated at 2022-06-14 13:03:50.847744
# Unit test for function import_object
def test_import_object():
    import_object('unittest')
    import_object('unittest.TestCase')



# Generated at 2022-06-14 13:03:56.696248
# Unit test for function import_object
def test_import_object():
    import tornado.escape
    assert import_object("tornado.escape") is tornado.escape
    assert import_object("tornado.escape.utf8") is tornado.escape.utf8
    assert import_object("tornado") is tornado
    try:
        import_object("tornado.missing_module")
    except ImportError:
        pass
    else:
        assert False, "expected ImportError"



# Generated at 2022-06-14 13:04:05.200688
# Unit test for function import_object
def test_import_object():
    import_object('tornado.test_utils')



# Generated at 2022-06-14 13:04:11.089454
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise OSError(5)
    except OSError as e:
        assert errno_from_exception(e) == 5

    try:
        raise Exception
    except Exception as e:
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:04:11.674845
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass

# Generated at 2022-06-14 13:04:21.971837
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return B

        def initialize(self, **kwargs):
            pass

    class B(A):
        def initialize(self, **kwargs):
            pass

    class C(A):
        def initialize(self, **kwargs):
            pass

    A.configure(impl=C)
    assert(isinstance(A(), C))
    assert(not isinstance(A(), B))
    assert(isinstance(A(), A))

    A.configure(impl=None)
    assert(isinstance(A(), B))
    assert(isinstance(A(), A))
    assert(not isinstance(A(), C))

    A.configure

# Generated at 2022-06-14 13:04:33.797162
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import typing
    import unittest
    from tornado.util import Configurable
    C = Configurable
    class A(C):
        def configurable_base(self):
            return A
        def configurable_default(self):
            return B
        
        def initialize(self, *args, **kwargs):
            pass
        
        def __init__(self, *args, **kwargs):
            raise Exception('should not be called')
        
        pass
    
    class B(C):
        def configurable_base(self):
            return A
        def configurable_default(self):
            raise Exception('B should not be the default')
        
        def initialize(self, *args, **kwargs):
            pass
        

# Generated at 2022-06-14 13:04:34.899683
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    a = Configurable()
    assert a is not None

# Generated at 2022-06-14 13:04:43.851478
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func1(arg1):
        pass

    def func2(arg1, arg2):
        pass

    def func3(arg1, arg2=None):
        pass 

    def func4(arg1=None, arg2=None):
        pass

    a1 = ArgReplacer(func1, "arg1")
    assert a1.get_old_value((1,), {}) == 1
    assert a1.get_old_value((1,), {}) != 2

    a2 = ArgReplacer(func2, "arg1")
    assert a2.get_old_value((1,2), {}) == 1
    assert a2.get_old_value((1,2), {}) != 2

    a3 = ArgReplacer(func2, "arg2")
    assert a3.get_old_

# Generated at 2022-06-14 13:04:55.508952
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # A configurable class
    class Upper(Configurable):
        @classmethod
        def configurable_base(cls):
            return Upper

        @classmethod
        def configurable_default(cls):
            return UpperImpl

        def initialize(self, x=None):
            pass

    # A couple of implementations
    class UpperImpl(Upper):
        def __init__(self, x=None):
            pass

    class UpperImpl2(Upper):
        def __init__(self, x=None):
            pass

    # Undecorated use case
    u = Upper()
    assert isinstance(u, UpperImpl)
    assert not isinstance(u, UpperImpl2)

    # Decorated use case
    Upper.configure(UpperImpl2)
    u = Upper()

# Generated at 2022-06-14 13:05:05.100183
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.concurrent
    import tornado.ioloop
    import tornado.locks

    future = tornado.concurrent.Future()
    future_io_loop = tornado.ioloop.IOLoop()
    future_io_loop.make_current()
    future.set_result('foo')

    future_cb = lambda future: future.result()

    tornado.concurrent.Configurable.configure('tornado.concurrent.Future')
    future_obj = tornado.concurrent.Configurable()
    assert future_obj == tornado.concurrent.configurable_default()

    tornado.concurrent.Configurable.configure(future)
    future_obj = tornado.concurrent.Configurable()
    assert future_obj == future

    tornado.concurrent.Configurable.configure(None)
    future_obj = tornado.concurrent.Configurable

# Generated at 2022-06-14 13:05:18.008591
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from typing import cast, Type, TypeVar
    # Checks that the documentation example code is valid
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return cls
        @classmethod
        def configurable_default(cls):
            return cast(Type[Configurable], cls)
        def initialize(self):
            pass
    class B(A):
        pass
    class C(A):
        pass
    A.configure(B)
    a = A()
    assert isinstance(a, A)
    assert isinstance(a, B)
    assert not isinstance(a, C)
    A.configure(C)
    a = A()
    assert isinstance(a, A)
    assert not isinstance(a, B)

# Generated at 2022-06-14 13:05:36.545913
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Base(Configurable):
        def configurable_base(self):
            return Base

        def configurable_default(self):
            return Derived

        def initialize(self, arg):
            self.arg = arg

    class Derived(Base):
        pass

    Base.configure(Derived, arg="default")
    assert Base().arg == "default"
    Base.configure(None)
    assert Base().arg == "default"
    Base.configure(Derived, arg="other")
    assert Base().arg == "other"



# Generated at 2022-06-14 13:05:46.772621
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    from inspect import signature, Parameter
    from typing import Any


    def assert_dict_and_object_equivalent(d: Mapping[Any, Any]) -> None:
        assert d == d.dict
        return


    assert_getargs = signature(assert_dict_and_object_equivalent).bind
    assert_dict_and_object_equivalent(assert_getargs(dict={"foo":"bar"}))
    od = ObjectDict({"foo":"bar"})
    od.__dict__["dict"] = od
    assert_dict_and_object_equivalent(assert_getargs(dict=od))
    assert_getargs(dict=od)
    return

# Generated at 2022-06-14 13:05:50.294410
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class SubConfigurable(Configurable):
        def configurable_base(self):
            return self

        def configurable_default(self):
            return self

    assert issubclass(SubConfigurable, Configurable)
    assert SubConfigurable().__class__ == SubConfigurable



# Generated at 2022-06-14 13:05:58.357446
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b=None, c=2):
        return a, b, c

    ar = ArgReplacer(func, "b")
    arg1 = (1, 2, 3)
    arg2 = dict(a=4, b=5, c=6)
    assert ar.replace(33, arg1, arg2) == (2, (1, 33, 3), dict(a=4, b=33, c=6))
    ar.get_old_value((), dict(b=3, c=4)) == 3
    # test whether old value is None and new value is added to kwargs
    ar = ArgReplacer(func, "d")

# Generated at 2022-06-14 13:06:10.778479
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.netutil import Resolver
    import unittest

    class Foo(Configurable):
        @classmethod
        def configurable_base(cls):
            return Foo

        @classmethod
        def configurable_default(cls):
            return DefaultFoo

        def initialize(self, a=None, b=None):
            pass

    class DefaultFoo(Foo):
        pass

    class TestFoo(Foo):
        pass

    class TestConfigurable(unittest.TestCase):
        def setUp(self):
            self.saved = Foo._save_configuration()

        def tearDown(self):
            Foo._restore_configuration(self.saved)

        def test_default(self):
            self.assertIs(Foo.configured_class(), DefaultFoo)
            self

# Generated at 2022-06-14 13:06:15.766838
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
  # test_ArgReplacer_replace is a function
  # test_ArgReplacer_replace.__code__ is a code object
  ARGS_POS = list(test_ArgReplacer_replace.__code__.co_varnames[:test_ArgReplacer_replace.__code__.co_argcount])
  VALUE_REPLACE_1 = "FakeArgument"
  VALUE_REPLACE_2 = "FakeArgument2"
  VALUE_REPLACE_3 = "FakeArgument3"
  VALUE_REPLACE_4 = "FakeArgument4"
  ARGS_POS_REPLACE = list(ARGS_POS)
  ARGS_POS_REPLACE[0] = VALUE_REPLACE_1
  ARGS_POS_REPLACE[1] = VALUE_

# Generated at 2022-06-14 13:06:23.046222
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(x, y=None, z=None):
        pass
    arg_replacer = ArgReplacer(f, 'z')
    old_value, args, kwargs = arg_replacer.replace(None, (23, 70, 0), {'z':1})
    assert old_value == 1
    assert args == (23, 70, 0)
    assert kwargs == {'z':None}

    old_value, args, kwargs = arg_replacer.replace(None, (23, 70), {'z':1})
    assert old_value == 1
    assert args == (23, 70)
    assert kwargs == {'z':None}

    old_value, args, kwargs = arg_replacer.replace(None, (23, 70), {})
    assert old_value == None

# Generated at 2022-06-14 13:06:28.054952
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class Foo(Configurable):
        def initialize(self, arg=42):
            assert arg == 42

    f = Foo()
    assert f.initialize() == NotImplementedError  # type: ignore
    # Unit test for method configurable_base of class Configurable

# Generated at 2022-06-14 13:06:36.877455
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class C(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type['C']
            return cls

        @classmethod
        def configurable_default(cls):
            # type: () -> Type['C']
            return cls

        def __init__(self):
            # type: () -> None
            pass

        def initialize(self, x):
            # type: (Any) -> None
            pass

    C.configure(None)

    with pytest.raises(TypeError):
        C()
    with pytest.raises(TypeError):
        C(x=1)
    with pytest.raises(TypeError):
        C(1)
    with pytest.raises(TypeError):
        C

# Generated at 2022-06-14 13:06:42.233690
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        import os
        os.read(-1, 10)
    except Exception as e:
        errno = errno_from_exception(e)
        assert errno == 22
    try:
        raise Exception
    except Exception as e:
        errno = errno_from_exception(e)
        assert errno is None



# Generated at 2022-06-14 13:07:04.151979
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def foo(first, second, third):
        pass
    ret = ArgReplacer(foo, 'first').replace('foo',(1,2,3),{})
    assert ret[0] == 1
    assert ret[1] == ('foo',2,3)
    assert ret[2] == {}
    ret = ArgReplacer(foo, 'third').replace(3,(1,2,3),{})
    assert ret[0] == 3
    assert ret[1] == (1,2,3)
    assert ret[2] == {}
    ret = ArgReplacer(foo, 'second').replace(2,(1,2,3),{})
    assert ret[0] == 2
    assert ret[1] == (1,2,3)
    assert ret[2] == {}

# Generated at 2022-06-14 13:07:11.767320
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado.test.util_test import configurable_default

    class impl():
        n = 100

    class configurable_base(Configurable):
        @classmethod
        def configurable_base(cls):
            return configurable_base

        @classmethod
        def configurable_default(cls):
            return configurable_default

    globals().update(locals())  # type: ignore
    #
    # Test case 1
    #
    impl = impl_()
    configurable_base.configure(impl)
    ins1 = configurable_base()
    print(ins1.n)
    assert ins1.n == 100
    #
    # Test case 2
    #
    impl = impl_()
    configurable_base.configure(None)
    ins1 = configurable_base()
    print

# Generated at 2022-06-14 13:07:19.837971
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise IOError(22, "fake error")
    except BaseException as e:
        assert errno_from_exception(e) == 22
        assert e.args[0] == 22
        e.errno = 11
        assert errno_from_exception(e) == 11
        e.args = tuple()
        assert errno_from_exception(e) is None
        try:
            raise Exception()
        except BaseException as e:
            assert errno_from_exception(e) is None
        try:
            raise Exception(22, 33)
        except BaseException as e:
            assert errno_from_exception(e) == 22



# Generated at 2022-06-14 13:07:29.002366
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():

    class MyFunc(object):
        def test_func(self, arg1=None, arg2=None):
            return arg1, arg2

    args = (1, 2, 3)
    kwargs = {'arg1': 20, 'arg2': 30}
    arg_replacer = ArgReplacer(MyFunc.test_func, 'arg1')
    old_value, args_new, kwargs_new = arg_replacer.replace(5, args=args, kwargs=kwargs)
    assert old_value == 20
    assert args_new == (1, 2, 3)
    assert kwargs_new == {'arg1': 5, 'arg2': 30}



# Generated at 2022-06-14 13:07:42.083624
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Base(Configurable):
        def __init__(self, a: int, b: int, c: int = 4) -> None:
            self.a = a
            self.b = b
            self.c = c

        @classmethod
        def configurable_base(cls):
            return cls

        @classmethod
        def configurable_default(cls):
            return cls

    class Impl(Base):
        def __init__(self, a: int, b: int, c: int = 4, d: int = 5) -> None:
            super(Impl, self).__init__(a, b, c)
            self.d = d

        @classmethod
        def configurable_base(cls):
            return Base

    Impl.configure(None, c=6)

# Generated at 2022-06-14 13:07:46.790233
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Test configurable logger
    logger = logging.getLogger("tornado.test")
    logger_impl_cls_old = logger.configured_class()
    assert logger_impl_cls_old is logging.Logger

    class CustomLogger(logging.Logger):
        pass

    logger.configure(CustomLogger)
    logger_impl_cls = logger.configured_class()

    assert logger_impl_cls is CustomLogger

    logger = logging.getLogger("tornado.test")
    assert logger.__class__ is CustomLogger

    logger.configure(logger_impl_cls_old)
    logger_impl_cls = logger.configured_class()
    assert logger_impl_cls is logger_impl_cls_old



# Generated at 2022-06-14 13:07:50.955433
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    global called
    called = False
    class A(Configurable):
        def initialize(self):
            global called
            called = True
    class B(A):
        pass
    a = A()
    assert called
    b = B()
    assert called is False



# Generated at 2022-06-14 13:07:57.917064
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(one, two = None, three = None):
        pass
    argreplacer = ArgReplacer(func, 'three')
    assert argreplacer.get_old_value((1, 2), {}, 3) == 3
    assert argreplacer.get_old_value((1, 2), {}, 'three') == 'three'
    assert argreplacer.get_old_value((1, 2), {}, None) == None


# Generated at 2022-06-14 13:08:05.795989
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():

    class A(Configurable):
        _impl_class = None  # type: Optional[Type[Configurable]]
        _impl_kwargs = None  # type: Dict[str, Any]

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return cls

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return cls

    class B(A):
        ...

    class C(B):
        ...

    class D(B):
        ...

    B._impl_class = None
    B._impl_kwargs = None
    C._impl_class = None
    C._impl_kwargs = None
    D._impl_class = None
    D._impl_kwargs = None

# Generated at 2022-06-14 13:08:16.249903
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class MyConfigurable(Configurable):
        pass

    class MyConfigurableClass(MyConfigurable):
        def __init__(self, param: str, **kwargs: Any) -> None:
            super(MyConfigurableClass, self).__init__(**kwargs)
            self.param = param

        @classmethod
        def configurable_base(cls):
            return MyConfigurable

        @classmethod
        def configurable_default(cls):
            return MyConfigurableClass

    MyConfigurable.configure(MyConfigurableClass, param="my_param")

    assert issubclass(MyConfigurable.configured_class(), MyConfigurable)
    assert MyConfigurable.configured_class() is MyConfigurableClass
    assert MyConfigurable().param == "my_param"



# Generated at 2022-06-14 13:08:55.173313
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test(p,q = 10,*args,**kwargs):
        '''test function'''
    foo = ArgReplacer(test,'p')
    print(foo.arg_pos)
    print(test(100,test=200,p=300,k=200,**{'a':222}))
    print(foo.get_old_value((100,200,300),{'test':200,'p':300,'k':200,'a':222}))
    print(foo.get_old_value((100,200,300),{'test':200,'k':200,'a':222}))
    print(foo.replace(777,(100,200,300),
                      {'test':200,'k':200,'a':222}))

# Generated at 2022-06-14 13:08:56.757952
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class base(Configurable):
        pass
    base.configure(None)
    assert base()



# Generated at 2022-06-14 13:09:08.841729
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    Impl1 = Configurable.configurable_base()
    Impl2 = Configurable.configurable_base()

    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            return Base

        @classmethod
        def configurable_default(cls):
            return Impl1

    Impl1.configure(Impl3, hello="world")
    assert isinstance(Base(), Impl3)
    assert Base().hello == "world"

    Impl1.configure(Impl4, hello="world")
    assert isinstance(Base(), Impl4)
    assert Base().hello == "world"

    Impl2.configure(Impl2, hello="world")
    assert isinstance(Base(), Impl1)
    assert Base().hello == "world"

    assert Base.configured_class() == Impl1


# Generated at 2022-06-14 13:09:15.017658
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func(a,b,c):
        pass
    arg_replacer = ArgReplacer(func, 'c')
    args = (1,2,3)
    kwargs = {'a':1, 'c':1}
    assert arg_replacer.get_old_value(args, kwargs) == 3
    assert arg_replacer.get_old_value((), kwargs) == 1
    assert arg_replacer.get_old_value((),{}) == None
    assert arg_replacer.get_old_value((),{},default=1) == 1


# Generated at 2022-06-14 13:09:19.291258
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(x, y):
        pass
    replacer = ArgReplacer(foo, 'x')
    res = replacer.get_old_value((1,2),{'y':2}, default = 3)
    assert res == 1


# Generated at 2022-06-14 13:09:26.668595
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    Configurable.configure(None, foo=1)
    my_class = type(
        "my_class",
        (Configurable,),
        {
            "initialize": classmethod(
                lambda cls, a, b, foo, bar=2: None
            ),
            "configurable_base": classmethod(
                lambda cls: Configurable
            ),
            "configurable_default": classmethod(
                lambda cls: Configurable
            )
        }
    )
    my_class(1, 2, bar=3)

# Generated at 2022-06-14 13:09:35.928918
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        def __init__(self, a, b, c=None):
            raise NotImplementedError

        initialize = __init__

        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable

    TestConfigurable.configure(None)
    assert TestConfigurable(3, "ab").initialize == (3, "ab")
    assert TestConfigurable(3, "ab", c=4).initialize == (3, "ab", 4)



# Generated at 2022-06-14 13:09:41.329551
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def my_callable(a_arg, b_arg=None):
        pass
    arg_replacer = ArgReplacer(my_callable, 'b_arg')
    old_value, args, kwargs = arg_replacer.replace('d', ('a',), {})
    assert old_value is None
    assert args == ('a',)
    assert kwargs == {'b_arg': 'd'}



# Generated at 2022-06-14 13:09:49.842485
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    test_args = [1, 2, 'hello']
    test_kwargs = {'arg3': 'hi', 'arg4': 'bye'}
    arg_replacer = ArgReplacer(lambda *args, **kwargs: None, 'arg1')
    test_new_value = 'new'
    arg_replacer.replace(test_new_value, test_args, test_kwargs)
    test_args_replaced = (test_new_value, 2, 'hello')
    test_kwargs_replaced = {'arg3': 'hi', 'arg4': 'bye'}
    assert test_args_replaced == test_args, 'test_args_replaced != test_args'
    assert test_kwargs_replaced == test_kwargs, 'test_kwargs_replaced != test_kwargs'

# Generated at 2022-06-14 13:10:02.043082
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def func0():
        pass

    def func1(p1):
        pass

    def func2(p1, p2):
        pass

    def func4(p1, p2, p3, p4):
        pass

    def func5(p1=1, p2=2, p3=3, p4=4, p5=5):
        pass

    def func6(p1=1, p2=2, p3=3, p4=4, p5=5, p6=6):
        pass

    def func_dict(**kwargs):
        pass

    def func_mix(*args, **kwargs):
        pass

    def func_mix2(p1=1, p2=2, p3=3, **kwargs):
        pass


# Generated at 2022-06-14 13:10:45.447529
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def initialize(self, a, b):
            self.x = a + b

        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return A


    a = A(1, 2)
    assert a.x == 3

    b = A(3, 4)
    assert b.x == 7


# Generated at 2022-06-14 13:10:56.309183
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    a = ArgReplacer(lambda x: x, "x")
    assert a.get_old_value((1,), {}) == 1
    assert a.get_old_value((), {"x": 2}) == 2
    assert a.get_old_value((), {}) == None

    f = lambda x, y=2: x
    a = ArgReplacer(f, "x")
    assert a.get_old_value((1,), {}) == 1
    assert a.get_old_value((), {"x": 2}) == 2
    assert a.get_old_value((), {}) == None
    assert a.get_old_value((), {}) == None

    a = ArgReplacer(f, "y")
    assert a.get_old_value((1,), {}) == 2
    assert a.get

# Generated at 2022-06-14 13:11:02.508373
# Unit test for function errno_from_exception
def test_errno_from_exception():
    class MyException(Exception):
        pass

    try:
        raise MyException(42, "My exception")
    except Exception as e:
        assert errno_from_exception(e) == 42
    try:
        raise MyException("My exception")
    except Exception as e:
        assert errno_from_exception(e) == "My exception"
    try:
        raise MyException()
    except Exception as e:
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:11:04.123432
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    assert Configurable.initialize is Configurable._initialize


# Generated at 2022-06-14 13:11:08.198357
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    """
    from tornado.util import ArgReplacer
    def foo(a, b, c=1):
        pass
    new_args = ArgReplacer.replace(1, foo, 1, {'a': 2}, {'b': 3}, c=3)
    """



# Generated at 2022-06-14 13:11:11.337933
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test(a,b,c,key='foo'):
        pass
    ar = ArgReplacer(test, 'b')
    assert ar.get_old_value((1,),{}) == None

# Generated at 2022-06-14 13:11:20.734759
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def test(a, b=0, *, c=0):
        ar = ArgReplacer(test, 'b')
        assert ar.get_old_value((a,), {}, 0) == 0
        assert ar.get_old_value((a,), {'b':1}, 0) == 1
        assert ar.get_old_value((a,), {'b':1, 'c':2}, 0) == 1
        assert ar.get_old_value((a,2), {'c':1}, 0) == 2
        assert ar.get_old_value((a,2), {'b':1}, 0) == 2
        ar2 = ArgReplacer(test, 'c')
        assert ar2.get_old_value((a,), {'c':1}, 0) == 0
        assert ar2.get_

# Generated at 2022-06-14 13:11:31.344331
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from tornado import escape, gen
    import tornado.escape
    import tornado.gen
    assert escape.utf8(b"foo") == b"foo"
    assert escape.native_str("foo") == "foo"
    assert escape.to_unicode("foo") == "foo"
    assert gen.maybe_future(123) == 123
    escape.Configurable.configure("tornado.escape")
    gen.Configurable.configure("tornado.gen")
    assert escape.utf8(b"foo") is tornado.escape.utf8(b"foo")
    assert escape.native_str("foo") is tornado.escape.native_str("foo")
    assert escape.to_unicode("foo") is tornado.escape.to_unicode("foo")
    assert gen.maybe_future(123) is tornado.gen.maybe_future