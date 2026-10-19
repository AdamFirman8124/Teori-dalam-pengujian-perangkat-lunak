

# Generated at 2022-06-14 13:02:02.202346
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    def foo(m, n, o):
        pass
    replacer = ArgReplacer(foo, "m")
    assert replacer.get_old_value(("one", 2, 3), {}) == "one"
    assert replacer.get_old_value(("one", 2, 3), {}, default=10) == "one"
    replacer = ArgReplacer(foo, "n")
    assert replacer.get_old_value(("one", 2, 3), {}) == 2
    assert replacer.get_old_value(("one", 2, 3), {}, default=10) == 2
    replacer = ArgReplacer(foo, "o")
    assert replacer.get_old_value(("one", 2, 3), {}) == 3

# Generated at 2022-06-14 13:02:09.781635
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    import functools  # module to use functools.wraps
    import unittest   # module to run tests
    import random     # module to generate random numbers

    def method(*args, **kwargs):
        """Method to test ArgReplacer.get_old_value."""
        obj = ArgReplacer(method, 'q')
        old_value = obj.get_old_value(args, kwargs)
        return old_value

    # Function to get random value of type type_
    def rand_value():
        # Get random value
        p = random.randint(1, 2)
        if p == 1:
            old_value = random.random()

# Generated at 2022-06-14 13:02:19.396780
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from types import ModuleType
    from unittest.mock import Mock
    from tornado.ioloop import PollIOLoop
    class PollIOLoopTest(Configurable, IOLoop):
        def configurable_base(self):
            return 'PollIOLoopTest'
        def configurable_default(self):
            return IOLoop
    # replace the class attribute of PollIOLoopTest
    PollIOLoopTest._module = ModuleType(PollIOLoopTest.__module__)
    PollIOLoopTest._module.PollIOLoopTest = PollIOLoopTest
    # user defined function
    def initialize(*args, **kwargs):
        pass
    PollIOLoopTest.initialize = initialize
    # mock object
    mock_impl = Mock(spec=IOLoop, wraps=IOLoop)
    mock_

# Generated at 2022-06-14 13:02:31.277090
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Tests the constructor of Configurable
    # type: () -> None
    class Simple(Configurable):
        def configurable_base(self):
            # type: () -> Type[Configurable]
            return Simple

        def configurable_default(self):
            # type: () -> Type[Configurable]
            return Simple

        def initialize(self):
            # type: () -> None
            pass

    Simple.configure(None)
    s = Simple()
    assert isinstance(s, Simple)

    class Subclass(Simple):
        def configurable_base(self):
            # type: () -> Type[Configurable]
            return Simple

        def configurable_default(self):
            # type: () -> Type[Configurable]
            return Subclass

        def initialize(self):
            # type: () -> None
            pass



# Generated at 2022-06-14 13:02:33.380878
# Unit test for function import_object
def test_import_object():
    import_object('sys')
    try:
        import_object('sys.fake')
        assert False
    except ImportError:
        pass



# Generated at 2022-06-14 13:02:43.185313
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class BaseTest(Configurable):
        def configurable_base(self):
            return BaseTest
        def configurable_default(self):
            return BaseTest
        def initialize(self, a, b, c=0, d=""):
            self.init_args = a, b, c, d
    class SubTest(BaseTest):
        pass
    BaseTest.configure(SubTest, d="abc")
    assert BaseTest().init_args == (None, None, 0, "abc")
    assert SubTest().init_args == (None, None, 0, "abc")
    BaseTest.configure(SubTest, d="123")
    assert BaseTest().init_args == (None, None, 0, "123")
    assert SubTest().init_args == (None, None, 0, "123")
    BaseTest.config

# Generated at 2022-06-14 13:02:48.963769
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # type: () -> None
    args = (1, 2)
    kwargs = {"a":1, "b":2}

    def f(*, q=3):
        return q

    taken = ArgReplacer(f, "q")
    taken.replace(8, args, kwargs)
    print(kwargs)
    f(a=1, b=2)
    #return kwargs
test_ArgReplacer_replace()
print(2)


# Generated at 2022-06-14 13:02:53.608600
# Unit test for constructor of class ArgReplacer
def test_ArgReplacer():
    def f(a, b, c=1, d=2):
        pass
    assert ArgReplacer(f, "b").arg_pos == 1
    assert ArgReplacer(f, "c").arg_pos is None
    assert ArgReplacer(f, "d").arg_pos is None
    assert ArgReplacer(f, "e").arg_pos is None
    assert ArgReplacer(f, "a").get_old_value((1, 2), {"b": 3}) == 2
    assert ArgReplacer(f, "b").get_old_value((1,), {"b": 3}) == 3
    assert ArgReplacer(f, "c").get_old_value((), {}) is None
    assert ArgReplacer(f, "c").get_old_value((), {"c": 4}) == 4
    assert ArgReplacer

# Generated at 2022-06-14 13:02:54.427021
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    pass

# Generated at 2022-06-14 13:03:04.958038
# Unit test for method initialize of class Configurable

# Generated at 2022-06-14 13:03:26.869814
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f1(a,b):
        return a, b
    def f2(a,b,c=3):
        return a, b, c
    def f3(a,b,c=3,d=4):
        return a, b, c, d
    class MyArgReplacer(ArgReplacer):
        pass
    print(MyArgReplacer(f1, 'a').replace('test', (1,2), {}))
    print(MyArgReplacer(f1, 'b').replace('test', (1,2), {}))
    print(MyArgReplacer(f1, 'c').replace('test', (1,2), {}))
    print(MyArgReplacer(f2, 'a').replace('test', ('a','b'), {}))

# Generated at 2022-06-14 13:03:37.356882
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    import unittest
    import sys

    if sys.version_info < (3, 5):
        # The class doesn't get defined above.
        class Configurable(Configurable):
            pass

    class Example(Configurable):
        def __init__(self, a, b):
            self.initialize(a, b=b)
            self.initialized = True

        @classmethod
        def configurable_base(cls):
            return Example

        @classmethod
        def configurable_default(cls):
            return Example

    class SubExample(Example):
        pass

    class TestExample(unittest.TestCase):
        def test_init(self):
            example = Example(1, 2)
            self.assertEqual(1, example.a)
            self.assertEqual

# Generated at 2022-06-14 13:03:43.765710
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    base_class = Configurable
    import unittest
    from tornado.testing import AsyncTestCase, gen_test
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return base_class

    a = A()
    assert isinstance(a, A)


# Generated at 2022-06-14 13:03:54.504919
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None

    class Subclass(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Configurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return cls

        def initialize(self):
            pass

        @classmethod
        def arg_test(cls, a, b, optional=True):
            print("a=%r, b=%r, optional=%r" % (a, b, optional))
            return (a, b, optional)

    Subclass.configure(None)
    assert isinstance(Subclass(), Subclass)
    Subclass.configure("tornado.util.Configurable")

# Generated at 2022-06-14 13:04:04.083870
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        def __init__(self, *args, **kwargs):
            print('self:', self)
            super().__init__(*args, **kwargs)

        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return TestConfigurable

    TestConfigurable.configure(None)
    TestConfigurable.configure(TestConfigurable, a=1)
 
    tc1 = TestConfigurable()
    tc2 = TestConfigurable(b=2)
    tc3 = TestConfigurable(a=3, b=4)
    tc4 = TestConfigurable(name='t4')
    tc5 = TestConfigurable(name='t5')

# Generated at 2022-06-14 13:04:11.785790
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def func(a, b): pass

    replacer = ArgReplacer(func, 'b')
    assert('b' in [name for name, _ in inspect.signature(func).parameters.items()])
    old, new_args, new_kwargs = replacer.replace(5, (1,), {})

# Generated at 2022-06-14 13:04:19.297307
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def method(a, b, c):
        pass
    arg_name = 'b'
    args = (1, 2, 3)
    kwargs = {}
    replacer = ArgReplacer(method, arg_name)
    _, args, kwargs = replacer.replace(4, args, kwargs)
    assert_equal(args, (1,4,3))
    assert_equal(kwargs, {})
    _, args, kwargs = replacer.replace(5, args, kwargs)
    assert_equal(args, (1,5,3))
    assert_equal(kwargs, {})


# Generated at 2022-06-14 13:04:30.699128
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    '''
    args no name
    '''
    a = ArgReplacer(test_ArgReplacer_replace,'b')
    #print(a.get_old_value((1,2),{'a':3}))
    #print(a.replace(1,(1,2),{'a':3}))
    '''
    kwargs has name
    '''
    #print(a.get_old_value((1,2),{'b':3}))
    #print(a.replace(1,(1,2),{'b':3}))
    '''
    kwargs has no name
    arg has name
    '''
    #print(a.get_old_value((1,2),{'a':3},'default'))
    #print(a.replace(1,(

# Generated at 2022-06-14 13:04:39.270597
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(arg1, arg2):
        return arg1, arg2
    r = ArgReplacer(f, "arg1")
    assert r.replace(1, (2, 3), {}) == (2, [1, 3], {})
    assert r.replace(1, (2,), {"arg2": 3}) == (2, [1], {"arg2": 3})
    assert r.replace(1, (), {"arg2": 3}) == (None, [], {"arg1": 1, "arg2": 3})



# Generated at 2022-06-14 13:04:40.959523
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    a = ObjectDict()
    a.name = 'sdfs'
    assert a.name == 'sdfs'


# Generated at 2022-06-14 13:05:04.722695
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class B(Configurable):
        @classmethod
        def configurable_base(cls):
            return B

        @classmethod
        def configurable_default(cls):
            return B

    class I(B):
        def initialize(self):
            pass

    assert isinstance(B(), B)
    assert issubclass(B.configured_class(), B)
    assert isinstance(B.configured_class()(), B)
    B.configure(I)
    assert not isinstance(B(), B)
    assert isinstance(B(), I)
    assert issubclass(B.configured_class(), I)
    assert isinstance(B.configured_class()(), I)


# Generated at 2022-06-14 13:05:17.642640
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def test_func(arg1, arg2=None, arg3=False):
        assert arg1 == "test1"
        assert arg2 == None
        assert arg3 == True

    args = ("test1",)
    kwargs = {}
    replacer = ArgReplacer(test_func, "arg3")
    old_value = replacer.get_old_value(args, kwargs)
    assert old_value == False
    new_value = True
    old_value, args, kwargs = replacer.replace(new_value, args, kwargs)
    assert old_value == False
    assert args == ("test1",)
    assert kwargs == {"arg3": True}
    test_func(*args, **kwargs)
    # Add another test case

# Generated at 2022-06-14 13:05:27.441500
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    def f(a, b, c, d=5):
        pass
    #
    # Test replacement of a positional argument.
    #
    repl = ArgReplacer(f, "b")
    value, args, kwargs = repl.replace("hello", (1, 2, 3), {})
    assert value == 2
    assert args == (1, "hello", 3)
    assert kwargs == {}
    # Check that we handle 1-element tuples correctly.
    value, args, kwargs = repl.replace("hello", (1,), {})
    assert value == None
    assert args == (1,)
    assert kwargs == {'b': 'hello'}
    #
    # Test replacement of a keyword argument.
    #
    repl = ArgReplacer(f, "c")
    value, args, k

# Generated at 2022-06-14 13:05:31.269626
# Unit test for function errno_from_exception
def test_errno_from_exception():
    errno = None
    try:
        os.set_inheritable(fd=-1, inheritable=True)
    except OSError as e:
        errno = errno_from_exception(e)
    assert errno == errno_map['EBADF']


# Generated at 2022-06-14 13:05:38.786502
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    # Test for a function that has a single optional argument
    def f(a,b=4):
        pass
    # Test for a function that has a variable number of arguments
    def g(*args):
        pass
    # Test for a function that has both optional argument and variable
    # number of arguments
    def h(a, b=3, *args):
        pass
    # Test for a function that has keyword argument
    def i(a, b=3, c=4):
        pass
    # Test for a function that has both keyword argument and variable
    # number of keyword arguments
    def j(a, b=3, c=4, **kws):
        pass

    # Test ArgReplacer attributes
    def test_arg_pos(f,argname,expected_value):
        fname = f.__name__
        replacer

# Generated at 2022-06-14 13:05:49.549049
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    class MyClass:
        @staticmethod
        def foo(a, b, c):
            pass
    import inspect
    arg_replacer = ArgReplacer(inspect.getfullargspec(MyClass.foo), 'b')
    import pytest
    with pytest.raises(IndexError):
        assert arg_replacer.get_old_value((1,), {'c': 3}) == 2
    assert arg_replacer.get_old_value((1, 2), {'c': 3}) == 2
    assert arg_replacer.get_old_value((1, 2, 3), {'c': 3}) == 2
    assert arg_replacer.get_old_value((1, 2, 3), {}) == 2


# Generated at 2022-06-14 13:05:56.508386
# Unit test for method replace of class ArgReplacer
def test_ArgReplacer_replace():
    # **arg is not valid in python < 3.5
    def f(a, b, **arg):
        pass
    replacer = ArgReplacer(f, 'b')
    old_value, args, kwargs = replacer.replace("new value", [], {})
    assert old_value == arg
    assert args == []
    assert kwargs == {'b': "new value"}
    old_value, args, kwargs = replacer.replace("new value", [1], {})
    assert old_value == 1
    assert args == [1]
    assert kwargs == {'b': "new value"}



# Generated at 2022-06-14 13:06:00.238069
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class B(Configurable):
        def configurable_base(self):
            return B

    class A(B):
        def configurable_default(self):
            return A

        def __init__(self):
            print("init A")

    B.configure(A, a=1)
    a = A()



# Generated at 2022-06-14 13:06:04.850374
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import tornado.web
    impl = tornado.web.Application([])
    tornado.web.RequestHandler.configure(impl)
    assert isinstance(tornado.web.RequestHandler(), tornado.web.Application)


# Generated at 2022-06-14 13:06:10.165164
# Unit test for method get_old_value of class ArgReplacer
def test_ArgReplacer_get_old_value():
    f = lambda x, y, z: x*y - z
    replacer = ArgReplacer(f, 'x')
    assert replacer.get_old_value((2, 3, 4), {}) == 2
    assert replacer.get_old_value((2, 3, 4), {'x': 7}) == 7


# Generated at 2022-06-14 13:06:47.715452
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    # type: () -> None
    obj = ObjectDict()  # type: ObjectDict
    obj.set_a = 1
    obj.get_b = 2
    assert obj.set_a == 1
    assert obj.get_b == 2
    try:
        print(obj.set_c)
        #Unreachable
        assert False
    except AttributeError:
        pass

    # Check that attribute access is not allowed if the name is not a string
    try:
        obj[object()] = 0
        print(obj[object()])
        #Unreachable
        assert False
    except AttributeError:
        pass



# Generated at 2022-06-14 13:06:58.699520
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # Test the correct constructor is called depending on the configuration
    class TestImpl(object):
        def __init__(self, foo):
            self.foo = foo

    class TestConfigurableClass(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurableClass

        @classmethod
        def configurable_default(cls):
            return TestImpl

        def initialize(self, foo=None):
            self.foo = foo

    impl = TestImpl("foo")
    TestConfigurableClass.configure(impl)
    assert isinstance(TestConfigurableClass(), TestImpl)
    # Make sure the init args work too
    impl = TestImpl("foo")
    TestConfigurableClass.configure(impl)
    assert isinstance(TestConfigurableClass(foo="bar"), TestImpl)
    # Make

# Generated at 2022-06-14 13:07:03.801203
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Foo(Configurable):
        def __init__(self, a, b=None, c=None):
            pass

        @classmethod
        def configurable_base(cls):
            return Foo

        @classmethod
        def configurable_default(cls):
            return Foo

    f = Foo(1, b=2, c=3)
    assert isinstance(f, Foo)



# Generated at 2022-06-14 13:07:09.543320
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable
        @classmethod
        def configurable_default(cls):
            return TestConfigurableImpl
    class TestConfigurableImpl(TestConfigurable):
        pass
    arg = [1, 2, 3]
    kwarg = {'test': 4}
    instance = TestConfigurable(*arg, **kwarg)
    assert isinstance(instance, TestConfigurable)
    assert isinstance(instance, TestConfigurableImpl)



# Generated at 2022-06-14 13:07:10.390302
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    pass


# Generated at 2022-06-14 13:07:18.903216
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import pytest  # type: ignore

    @add_metaclass(Configurable)
    class Foo(object):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return Foo

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return Bar

        def initialize(self):
            # type: () -> None
            pass

    class Bar(Foo):
        pass

    class Baz(Foo):
        pass

    Foo.configure(None)
    assert isinstance(Foo(), Bar)
    assert isinstance(Foo.configured_class(), Bar)

    Foo.configure(Bar)
    assert isinstance(Foo(), Bar)

# Generated at 2022-06-14 13:07:24.557724
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class Subclass(Configurable):
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
    Subclass()



# Generated at 2022-06-14 13:07:33.388441
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # Configurable is an abstract class, so we need to subclass it here.
    class TestConfigurable(Configurable):
        @classmethod
        def configurable_base(cls):
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            return DefaultTestImpl

    class DefaultTestImpl(TestConfigurable):
        initialized = False

        def initialize(self):
            self.initialized = True

        def meth(self, a):
            return a

    class TestImpl(TestConfigurable):
        def meth(self, a):
            return a + 1

    assert TestConfigurable().meth(1) == 2
    # Initializer isn't called until first use (similar to @property)
    # so the default class can configure itself at runtime.
    assert not DefaultTestImpl.initialized
    # Configuring the implementation

# Generated at 2022-06-14 13:07:45.280478
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class ConcreteConfigurable(Configurable):
        # type: () -> None
        def _initialize(self):
            pass

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return ConcreteConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return ConcreteConfigurable

    with ConfigClass(ConcreteConfigurable) as cc:
        cc.configure(ConcreteConfigurable, a=1)
        with ConfigClass(ConcreteConfigurable) as cc:
            cc.configure(ConcreteConfigurable, b=1)
            assert ConcreteConfigurable().initialize() == None


# Generated at 2022-06-14 13:07:54.670246
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class F(Configurable):
        @classmethod
        def configurable_base(cls):
            return F
        @classmethod
        def configurable_default(cls):
            return F
    class G(F):
        pass
    class H(G):
        def initialize(self):
            self.initialized = True
    class I(G):
        pass
    F.configure(H)
    assert isinstance(F(), H)
    assert isinstance(H(), H)
    assert not isinstance(I(), H)
    f = F()
    assert f.initialized
    F.configure(None)
    assert isinstance(F(), F)
    f = F()
    assert not hasattr(f, 'initialized')



# Generated at 2022-06-14 13:08:14.726888
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class ABC(Configurable):
        pass
    # Initialize the configuration of class ABC
    ABC.configure(None, a=1)
    ABC.configure(None, a=2)
    # Test the attribute `__impl_kwargs` of class ABC after configuration
    assert ABC.__impl_kwargs == {'a': 2}
    # Create an instance of class ABC
    _ABC = ABC()
    assert _ABC.__impl_kwargs == {'a': 2}
    while not ABC.__impl_class:
        break
    assert _ABC is ABC.__impl_class

# Generated at 2022-06-14 13:08:25.765437
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # type: () -> None
    class TestConfigurable(Configurable):
        _real_initialize = Configurable.initialize

        @classmethod
        def configurable_base(cls):
            # type: () -> Type[TestConfigurable]
            return TestConfigurable

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[TestConfigurable]
            return TestConfigurable

        def initialize(self):
            # type: () -> None
            self._real_initialize()

    class TestConfigurableImpl(TestConfigurable):
        pass

    TestConfigurable.configure(TestConfigurableImpl)

    class TestConfigurableImpl2(TestConfigurableImpl):
        pass

    TestConfigurable.configure(TestConfigurableImpl2)
    instance = TestConfigurable()

# Generated at 2022-06-14 13:08:36.951798
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    # The __impl_class and __impl_kwargs are not globally available, so
    # the test subclass must be defined in this function.
    class TestConfigurable(Configurable):
        def initialize(self):
            self._initialize_called = True

        def configurable_base(self):
            return TestConfigurable

        def configurable_default(self):
            return self

    # Test without configuration
    instance = TestConfigurable()
    assert isinstance(instance, TestConfigurable)
    assert hasattr(instance, "_initialize_called")
    assert instance._initialize_called

    # Test with configuration
    class AnotherTestConfigurable(TestConfigurable):
        pass

    TestConfigurable.configure(AnotherTestConfigurable)
    instance = TestConfigurable()
    assert isinstance(instance, AnotherTestConfigurable)
    assert hasattr

# Generated at 2022-06-14 13:08:38.360831
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class TestClassParent1(Configurable):
        pass
    



# Generated at 2022-06-14 13:08:46.501608
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    import inspect
    import unittest

    class Base1(Configurable):

        @classmethod
        def configurable_base(cls):
            return Base1

        @classmethod
        def configurable_default(cls):
            return Impl1

    class Base2(Configurable):

        @classmethod
        def configurable_base(cls):
            return Base2

        @classmethod
        def configurable_default(cls):
            return Impl2

    class Impl1(Base1):
        pass

    class Impl2(Base2):
        pass

    Base1.configure(Impl1)
    Base2.configure(Impl2)

    # Ensure we saved the configuration
    assert Base1.configured_class() == Impl1
    assert Base2.configured_class() == Impl2

    # Verify that the

# Generated at 2022-06-14 13:08:56.843354
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return C

        def initialize(self):
            print("A")

    class B(A):
        def initialize(self):
            print("B")

    class C(A):
        def initialize(self):
            print("C")

    class D(Configurable):
        @classmethod
        def configurable_base(cls):
            return D

        @classmethod
        def configurable_default(cls):
            return E

        def initialize(self):
            print("D")

    class E(D):
        def initialize(self):
            print("E")

    stack = [A()]
    assert type(stack[-1])

# Generated at 2022-06-14 13:09:08.889556
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    impl_class = Configurable
    class ConfigurableSubclass(Configurable):
        def initialize(self): pass
        @classmethod
        def configurable_base(cls):
            return impl_class
        @classmethod
        def configurable_default(cls):
            return impl_class

    class Impl(ConfigurableSubclass):
        pass

    impl_class.configure(Impl)
    # The real test is that Configurable.configure() accepts an instance
    # of a class that's not a subclass of the configured base class; the
    # rest of this just makes sure that configure() is doing something
    # reasonable.
    instance = ConfigurableSubclass()
    assert isinstance(instance, Configurable)
    assert isinstance(instance, ConfigurableSubclass)
    assert isinstance(instance, Impl)



# Generated at 2022-06-14 13:09:16.332244
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    from tornado.httpserver import HTTPServer
    HTTPServer._initialize()
    HTTPServer.initialize()


# Type annotation for the half open range of valid utf8 sequences.
# Our minimum python version is 3.5.2 so we can use this in annotations.
UTF8_VALID_HEADER = typing.Literal[0x00, 0x01, 0x04, 0x03, 0x08, 0x05, 0x02, 0x06, 0x0E, 0x0F, 0x0C, 0x0A, 0x07, 0x09, 0x0D, 0x0B, 0x10]
UTF8_HEAD = typing.Literal[0x00, 0x01, 0x02, 0x03, 0x04]
UTF8_VALID_EMIT = typing.Literal

# Generated at 2022-06-14 13:09:20.383920
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def configurable_base(self):
            pass
        def configurable_default(self):
            pass
        def initialize(self, *args, **kwargs):
            pass

# Generated at 2022-06-14 13:09:23.705881
# Unit test for function errno_from_exception
def test_errno_from_exception():
    try:
        raise OSError(5, "Test")
    except OSError as e:
        assert errno_from_exception(e) == 5



# Generated at 2022-06-14 13:10:01.998212
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from typing import List, TypeVar

    _AT = TypeVar("_AT")
    _BT = TypeVar("_BT")

    # Unit test for method __new__ of class Configurable
    class Base(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Base]
            return Base

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[BaseImpl]
            return BaseImpl

    class BaseImpl(Base):
        def initialize(self):
            # type: () -> None
            self.initialized = True

    class Impl(Base):
        def initialize(self):
            # type: () -> None
            self.initialized = True


# Generated at 2022-06-14 13:10:08.849239
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    import unittest
    from pprint import pprint

    class TestCase(unittest.TestCase):
        def setUp(self: unittest.TestCase) -> None:
            self.name = ObjectDict()

        def test_name__setattr__(self: unittest.TestCase) -> None:
            self.name.a = 1
            pprint(self.name)
            self.assertEqual(self.name.a, 1)

        def test_name__getattr__(self: unittest.TestCase) -> None:
            self.assertRaises(AttributeError, lambda : self.name.a)

    unittest.main()
test_ObjectDict___getattr__()
########################################################################################################################
# Interfaces and implementations
#-----------------------------------------------------------------------------------------------------------------------
# The following classes are included

# Generated at 2022-06-14 13:10:20.228722
# Unit test for method __new__ of class Configurable
def test_Configurable___new__():
    from pytest import raises

    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            return A

        @classmethod
        def configurable_default(cls):
            return B
    # class A(Configurable):
    #     @classmethod
    #     def configurable_base(cls):
    #         return A
    #     @classmethod
    #     def configurable_default(cls):
    #         return B
    #     def _initialize(self):
    #         raise NotImplementedError()

    class B(A):
        def _initialize(self):
            pass

    with raises(NotImplementedError):
        A1 = A()
    with raises(NotImplementedError):
        B1 = B()


# Generated at 2022-06-14 13:10:32.246715
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    # type: () -> None
    class A(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return A

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            assert False

    class B(Configurable):
        @classmethod
        def configurable_base(cls):
            # type: () -> Type[Configurable]
            return A

        @classmethod
        def configurable_default(cls):
            # type: () -> Type[Configurable]
            return B

    class C(Configurable):
        def __init__(self, a, b, c):
            # type: (Any, Any, Any) -> None
            self.a = a

# Generated at 2022-06-14 13:10:35.812689
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class A(Configurable):
        def initialize(self):
            pass
        @classmethod
        def configurable_base(cls):
            return A
        @classmethod
        def configurable_default(cls):
            return A
    a = A()
    klass = A.configured_class()
    assert klass == A




# Generated at 2022-06-14 13:10:37.762869
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    d = ObjectDict()
    assert d.__getattr__("asdfasdf")


# Generated at 2022-06-14 13:10:40.619546
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    o = {
        'key': 'value',
    }
    o = ObjectDict(o)
    assert o.key == 'value'

# Generated at 2022-06-14 13:10:47.704421
# Unit test for function errno_from_exception
def test_errno_from_exception():
    errno = 1
    try:
        raise IOError(errno)
    except IOError as e:
        assert errno == errno_from_exception(e)

    try:
        e = IOError()
        e.errno = 2
        raise e
    except IOError as e:
        assert errno_from_exception(e) == 2

    try:
        raise IOError()
    except IOError as e:
        assert errno_from_exception(e) is None



# Generated at 2022-06-14 13:10:55.227841
# Unit test for method initialize of class Configurable
def test_Configurable_initialize():
    class MyConfigurable(Configurable):
        def configurable_base(cls):
            return MyConfigurable

        def configurable_default(cls):
            return MyConfigurable

        def _initialize(self, x, y=1):
            self.x = x
            self.y = y

    configure = MyConfigurable.configure
    MyConfigurable.configure = lambda impl, **kwargs: None  # type: ignore

# Generated at 2022-06-14 13:10:57.148781
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    """Unit tests for method `__getattr__` of class `ObjectDict`."""



# Generated at 2022-06-14 13:11:25.609851
# Unit test for method __getattr__ of class ObjectDict
def test_ObjectDict___getattr__():
    obj = ObjectDict({"a": 1})
    assert obj["a"] == 1



# Generated at 2022-06-14 13:11:35.750409
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

        def initialize(self, bar):
            # type: (str) -> None
            self.bar = bar

    class FooImpl(Foo):
        pass

    f = Foo('testing')
    assert isinstance(f, Foo)
    assert isinstance(f, FooImpl)
    assert f.bar == 'testing'

    class FooSubclass(Foo):
        pass

    f = FooSubclass('testing')
    assert isinstance(f, FooSubclass)

