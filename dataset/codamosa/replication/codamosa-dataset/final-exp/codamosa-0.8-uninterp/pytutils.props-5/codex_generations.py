

# Generated at 2022-06-14 06:35:43.482002
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        pass

    class Bar(Foo):
        pass

    classtest = {Foo: 0, Bar: 0}

    def increment_counter(cls):
        classtest[cls] += 1
        return classtest[cls]

    @lazyperclassproperty
    def counter(cls):
        return increment_counter(cls)

    print(Foo.counter)
    print(Bar.counter)
    print(Foo.counter)
    print(Bar.counter)



# Generated at 2022-06-14 06:35:54.534469
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class BaseClass:

        @lazyperclassproperty
        def foo(cls):
            return "foo from %s" % cls.__name__

        @lazyperclassproperty
        def bar(cls):
            return "bar from %s" % cls.__name__

    class Child1Class(BaseClass):
        pass

    class Child2Class(BaseClass):
        pass

    class Child3Class(Child2Class):
        pass

    class GrandChild1Class(Child1Class):
        pass

    class GrandChild3Class(Child3Class):
        pass

    assert BaseClass.foo == "foo from BaseClass"
    assert BaseClass.bar == "bar from BaseClass"
    assert Child1Class.foo == "foo from Child1Class"
    assert Child1Class.bar == "bar from Child1Class"

# Generated at 2022-06-14 06:35:59.350374
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            print('calling bar()')
            return 42

    assert Foo.bar == 42
    Foo.bar = 99
    assert Foo.bar == 99
    del Foo.bar
    assert Foo.bar == 42

    class Baz(object):
        @lazyclassproperty
        def bar(cls):
            print('calling bar()')
            return 42

    Baz.bar = 99
    assert Baz.bar == 99
    assert Foo.bar == 42


# Generated at 2022-06-14 06:36:05.882847
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E(A):
        @staticmethod
        def f(cls):
            return 'value for {}'.format(cls.__name__)

        g = lazyperclassproperty(f)

    class F(A):
        @staticmethod
        def f(cls):
            return 'value for {}'.format(cls.__name__)

        g = lazyperclassproperty(f)

    class G(E, F):
        pass

    class H(D, G):
        pass

    assert E.g == 'value for E'
    assert E().g == 'value for E'
    assert F.g == 'value for F'
   

# Generated at 2022-06-14 06:36:13.309532
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def no_params(cls):
            return 42

        @lazyperclassproperty
        def params(cls):
            return cls.no_params + 10

    class B(A):
        @lazyperclassproperty
        def no_params(cls):
            return 100

        @lazyperclassproperty
        def params(cls):
            return cls.no_params + 20

    assert A.no_params == 42
    assert B.no_params == 100
    assert A.params == 52
    assert B.params == 120

    A.no_params = 10
    A.params = 20
    assert A.no_params == 42
    assert B.no_params == 100
    assert A.params == 52
    assert B.params == 120

# Generated at 2022-06-14 06:36:20.043822
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Define the main class
    class A(object):
        @lazyclassproperty
        def attribute(cls):
            return 42

    assert A.attribute == 42

    # Define a sub class
    class B(A):
        pass

    assert B.attribute == 42



# Generated at 2022-06-14 06:36:27.480513
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo1(object):
        def __init__(self):
            super(Foo1, self).__init__()

        @lazyperclassproperty
        def myperclassprop(self):
            return set()

    class Foo2(Foo1):
        def __init__(self):
            super(Foo2, self).__init__()

    class Foo3(Foo1):
        def __init__(self):
            super(Foo3, self).__init__()

        @lazyperclassproperty
        def myperclassprop(self):
            return set()

    class Foo4(Foo2):
        def __init__(self):
            super(Foo4, self).__init__()
            pass

    f1 = Foo1()
    f2 = Foo2()

# Generated at 2022-06-14 06:36:32.934333
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def hello(cls):
            print("calculating value")
            return "hello"

    print("accessing")
    print(A.hello)
    print("after first access")
    print(A.hello)
    print(A.hello)



# Generated at 2022-06-14 06:36:35.512126
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def a(self):
            print('hi')
            return 5

    class B(A):
        pass

    assert A().a == 5
    assert B().a == 5

# Generated at 2022-06-14 06:36:45.567574
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class test(object):
        @lazyclassproperty
        def p(cls):
            return "{}_{}".format(cls.__name__, id(cls))

        @lazyclassproperty
        def q(cls):
            return "{}_{}".format(cls.__name__, id(cls))

        @classmethod
        def f(cls):
            return cls.q

    # check attributes
    def verify(cls):
        assert cls.q == cls.f()
        assert cls.__dict__['_lazy_q'] == cls.p
    verify(test)

    # check subclassed attributes
    class test2(test):
        def __init__(self):
            pass
    verify(test2)


# Generated at 2022-06-14 06:36:51.753848
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass(object):
        @lazyclassproperty
        def prop(cls):
            return cls.__name__

    assert TestClass.prop == 'TestClass'
    assert TestClass().prop == 'TestClass'



# Generated at 2022-06-14 06:36:56.717299
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return "hi"

    class B(A):
        pass

    assert A.prop == "hi"
    assert B.prop == "hi"



# Generated at 2022-06-14 06:37:01.829219
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def uniq_id(cls):
            return str(uuid.uuid4())

    class B(A):
        pass

    assert A.uniq_id == B.uniq_id



# Generated at 2022-06-14 06:37:13.598671
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def cached_property(cls):
            return 'static'

    class ChildA(Base):
        pass

    class ChildB(Base):
        pass

    assert Base.cached_property == 'static', 'cached value should be correct'
    assert ChildA.cached_property == 'static', 'cached value should be correct'
    assert ChildB.cached_property == 'static', 'cached value should be correct'

    ChildA.cached_property = 'cached'
    assert ChildA.cached_property == 'cached', 'cached value should be correct'

    assert Base.cached_property == 'static', 'cached value should be correct'
    assert ChildB.cached_property == 'static', 'cached value should be correct'




# Generated at 2022-06-14 06:37:15.036330
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def hello(cls):
            print ("hello")
            return 'hello'

    assert hasattr(Test, '_lazy_hello')
    assert getattr(Test, '_lazy_hello') == 'hello'



# Generated at 2022-06-14 06:37:20.012927
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def myproperty(cls):
            print("class A classproperty")
            return cls.__name__

    class B(A):
        pass

    assert A().myproperty == 'A'
    assert B().myproperty == 'B'

# Generated at 2022-06-14 06:37:25.067487
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def attr(cls):
            return "attr"

    class B(A):
        pass

    assert A.attr == "attr"
    assert B.attr == "attr"
    assert B.attr == A.attr



# Generated at 2022-06-14 06:37:36.790817
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def has_object(self):
            return True
    class Sub(Base):
        pass
    assert not hasattr(Base, '_Base_lazy_has_object')
    assert not hasattr(Sub, '_Sub_lazy_has_object')
    assert Base().has_object
    assert Sub().has_object
    assert hasattr(Base, '_Base_lazy_has_object')
    assert hasattr(Sub, '_Sub_lazy_has_object')
    assert Base().has_object is True
    assert Sub().has_object is True
    class SubSub(Sub):
        pass
    assert not hasattr(SubSub, '_Sub_lazy_has_object')
    assert SubSub().has_object

# Generated at 2022-06-14 06:37:46.402299
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        # this property is created and assigned on the first call
        # and is stored in the class
        @lazyclassproperty
        def prop(cls):
            return 1

    assert A.prop == 1
    assert A.prop == 1

    class B(A):
        # this property is different from the one in A
        @lazyclassproperty
        def prop(cls):
            return 2

    assert B.prop == 2
    assert B.prop == 2

    # but the property of class A is still the same
    assert A.prop == 1
    assert A.prop == 1

    class C(A):
        pass

    assert C.prop == 1
    assert C.prop == 1



# Generated at 2022-06-14 06:37:59.579815
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def data(cls):
            return 'data'

    class Bar(Foo):
        @lazyclassproperty
        def data(cls):
            return 'data'

    def test_foo():
        assert not hasattr(Foo, '_lazy_data')
        assert Foo.data == 'data'
        assert Foo._lazy_data == 'data'

    def test_foo_again():
        assert Foo.data == 'data'
        assert Foo._lazy_data == 'data'

    def test_bar():
        assert not hasattr(Bar, '_lazy_data')
        assert Bar.data == 'data'
        assert Bar._lazy_data == 'data'


# Generated at 2022-06-14 06:38:09.636505
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def first(cls):
            return 'first'

    class Test1(Test):
        @lazyclassproperty
        def second(cls):
            return 'second'

    assert Test.first == 'first'
    assert Test1.first == 'first'
    assert Test1.second == 'second'



# Generated at 2022-06-14 06:38:15.379452
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):

        @lazyclassproperty
        def val(cls):
            return 42

    class B(A):
        pass

    assert A.val == 42
    assert B.val == 42
    assert A.__dict__['_lazy_val'] == 42
    assert '_lazy_val' not in B.__dict__


# Generated at 2022-06-14 06:38:23.290348
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:38:30.151517
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:38:36.299697
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    @lazyclassproperty
    def lazy_prop(x):
        print("Calling {0!s}".format(x.__name__))
        return 'lazy_prop'

    class DummyClass(object):
        prop = lazy_prop

    assert DummyClass.prop == 'lazy_prop'
    assert DummyClass.prop == 'lazy_prop'



# Generated at 2022-06-14 06:38:43.018293
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 'abc'

    assert Foo.bar == 'abc'
    assert Foo.bar == 'abc'


try:
    from django.utils.functional import SimpleLazyObject as lazy_class
except ImportError:
    pass


# Generated at 2022-06-14 06:38:55.028176
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    from unittest import TestCase
    from unittest.mock import patch

    class Base(TestCase):
        def __init__(self):
            TestCase.__init__(self)

    class A(Base):
        @lazyperclassproperty
        def prop(cls):
            return 3
    
    class B(A):
        @lazyperclassproperty
        def prop(cls):
            return 4
    
    class C(B):
        @lazyperclassproperty
        def prop(cls):
            return 5

    test = A()
    test.assertEqual(A.prop, 3)
    test.assertEqual(B.prop, 4)
    test.assertEqual(C.prop, 5)



# Generated at 2022-06-14 06:38:59.369141
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:04.910986
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    @lazyclassproperty
    def value(cls):
        print('loading')
        return 123

    class Foo(object):
        pass

    class Bar(object):
        pass

    assert Foo.value == 123
    assert Foo.value == 123
    assert Bar.value == 123
    assert Bar.value == 123



# Generated at 2022-06-14 06:39:11.054635
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class Test(object):
        @lazyclassproperty
        def lazy_property():
            print("Initializing lazy_property")
            return True

        @property
        def property():
            return None

    assert Test.property is None
    assert Test.lazy_property is True



# Generated at 2022-06-14 06:39:27.138877
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # Define a class that has a subclass
    class A(object):
        pass

    class B(A):
        pass

    @lazyperclassproperty
    def prop(cls):
        return 'prop'

    # Test that prop is different for A and B
    a = A()
    b = B()

# Generated at 2022-06-14 06:39:32.072109
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass(object):
        @lazyclassproperty
        def foo(cls):
            print("Called")
            return "hello"

    # The foo property will be set in the first call
    assert TestClass.foo == "hello"
    # The foo property is set
    assert TestClass.foo == "hello"


# Generated at 2022-06-14 06:39:43.372211
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:39:53.615630
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:58.661599
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Test the lazyclassproperty function wrapper
    """
    class TestClass(object):
        @lazyclassproperty
        def always_return_int(cls):
            return 5
    test_instance = TestClass()
    assert TestClass.always_return_int == 5
    assert test_instance.always_return_int == 5



# Generated at 2022-06-14 06:40:11.234129
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from nose.tools import assert_equals
    from nose.tools import assert_true

    class C(object):
        @lazyclassproperty
        def myprop(cls):
            return 10

    def test_1():
        assert_equals(C.myprop, 10)
        assert_equals(C._lazy_myprop, 10)
        assert_true(hasattr(C, "_lazy_myprop"))
        C.myprop = 20
        assert_equals(C.myprop, 20)
        assert_equals(C._lazy_myprop, 20)
        assert_true(hasattr(C, "_lazy_myprop"))

    def test_2():
        class D(C):
            pass
        assert_equals(D.myprop, 10)

# Generated at 2022-06-14 06:40:18.641151
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base:
        @lazyperclassproperty
        def a(cls):
            print("get %s.a" % cls.__name__)
            return sum([i for i in range(1000000)])

    class A(Base):
        pass

    class B(Base):
        pass

    print("BEGIN")
    print("Get A.a: %d" % A.a)
    print("Get A.a again: %d" % A.a)
    print("Get B.a: %d" % B.a)
    print("Get B.a again: %d" % B.a)
    print("END")


# Generated at 2022-06-14 06:40:25.830929
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):

        _cached_prop = None

        def __init__(self):
            pass

        @lazyclassproperty
        def cached_prop(cls):
            print("Running cached property")
            return 3

        @classmethod
        def reset(cls):
            cls._cached_prop = None

        @property
        def prop(self):
            print("Running non-cached property")
            return 4

    test1 = Test()
    test2 = Test()

    assert test1.prop == 4
    assert test2.prop == 4
    assert test1.cached_prop == 3
    assert test2.cached_prop == 3
    Test.reset()
    assert test1.cached_prop == 3
    assert test2.cached_prop == 3



# Generated at 2022-06-14 06:40:38.165995
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    
    class A:
        _a_var = 10
        _c_var = 10000

        @lazyperclassproperty
        def a_var(cls):
            return cls._a_var + 1
        
    class B(A):
        _a_var = 100
        _b_var = 1000

        @lazyperclassproperty
        def b_var(cls):
            return cls._b_var + 1

    class C(A):
        _a_var = 1000
        _c_var = 100000

        @lazyperclassproperty
        def c_var(cls):
            return cls._a_var + 1

    assert A.a_var == 11
    assert hasattr(A, '_A_lazy_a_var')
    assert B.b_var == 1001


# Generated at 2022-06-14 06:40:47.999126
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 1

        @lazyclassproperty
        def baz(cls):
            return 2

    assert Foo.bar == 1
    assert Foo.bar == 1
    assert Foo.baz == 2
    assert Foo.baz == 2

    class Bar(Foo):
        pass

    assert Bar.bar == 1
    assert Bar.bar == 1
    assert Bar.baz == 2
    assert Bar.baz == 2
    assert Bar.bar == 1
    assert Bar.bar == 1

    Foo.bar = Foo.bar + 1
    assert Foo.bar == 2
    assert Bar.bar == 2

    Bar.bar = Bar.bar + 1
    assert Foo.bar == 2
    assert Bar.bar == 3

# Generated at 2022-06-14 06:41:08.557208
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class a(object):
        @lazyclassproperty
        def prop(cls):
            return cls.__name__

    assert a.prop == 'a'
    assert a.prop is a.prop



# Generated at 2022-06-14 06:41:20.907468
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def p(cls):
            return 0

    class B(A):
        pass

    class C(A):
        pass

    class D(A):
        pass


# Generated at 2022-06-14 06:41:27.374049
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:41:34.820305
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return random.randint(0, 100)

    class B(A):
        @lazyperclassproperty
        def a(cls):
            return random.randint(0, 100)

    assert A.a == A.a
    assert B.a == B.a
    assert A.a != B.a



# Generated at 2022-06-14 06:41:44.499912
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def lazyperclassproperty(cls):
            return "Lazy per class property"

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass


# Generated at 2022-06-14 06:41:50.207634
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Test:
        @lazyperclassproperty
        def test(cls):
            return "test"
    class Test2(Test):
        pass
    assert Test.test is Test.test
    assert Test2.test is Test2.test
    assert Test.test is not Test2.test
    assert Test2.test == "test"



# Generated at 2022-06-14 06:41:55.925471
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop(cls):
            return 'A'

    class B(A):
        pass

    class C(B):
        @lazyperclassproperty
        def prop(cls):
            return 'C'

    assert A.prop == 'A'
    assert B.prop == 'A'
    assert C.prop == 'C'



# Generated at 2022-06-14 06:42:07.796997
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Can't be written as a class because it is used as a class decorator
    class PriorityQueue(object):

        @lazyclassproperty
        def comparator(cls):
            # cls is the class object
            def compare(a, b):
                return cls._element_priority(a) < cls._element_priority(b)

            return compare

        @staticmethod
        def _element_priority(a):
            return a[0]

    assert PriorityQueue.comparator(1, 2) is True
    assert PriorityQueue.comparator(2, 1) is False
    assert PriorityQueue.comparator(9, 9) is False

    class CustomPriorityQueue(PriorityQueue):
        @staticmethod
        def _element_priority(a):
            return a[1]

    assert CustomPriorityQueue.com

# Generated at 2022-06-14 06:42:12.495880
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def foo(cls):
            return 'foo'

        # Force @lazyclassproperty failure
        foo = 'not foo'
    assert A.foo == 'foo'



# Generated at 2022-06-14 06:42:21.174725
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:43:05.268581
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return dict(foo=True)

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def foo(cls):
            return dict(foo=False, bar=True)

    class D(C):
        pass

    assert A.foo is B.foo
    assert B.foo is A.foo
    assert A.foo is C.foo
    assert C.foo is A.foo
    assert D.foo is not A.foo
    assert D.foo is not C.foo

    assert isinstance(A.foo, dict)
    assert isinstance(B.foo, dict)
    assert isinstance(C.foo, dict)
    assert isinstance(D.foo, dict)

   

# Generated at 2022-06-14 06:43:15.698578
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def testPerClass(cls):
            print('testPerClass')
            return 1

    class Sub(Base):
        pass

    class Sub2(Base):
        pass

    assert Base.testPerClass == 1
    assert Sub.testPerClass == 1
    assert Sub2.testPerClass == 1

    Base.testPerClass = 2
    assert Base.testPerClass == 2
    assert Sub.testPerClass == 1
    assert Sub2.testPerClass == 1

    # should not pollute other classes
    class Sub(object):
        testPerClass = 3

    assert Sub.testPerClass == 3


# Generated at 2022-06-14 06:43:21.462451
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class MyBase(object):
        @lazyperclassproperty
        def foo(cls):
            # print "foo called"
            return random.randint(1,100)

    class MySub(MyBase):
        @lazyperclassproperty
        def foo(cls):
            # print "foo called"
            return random.randint(1,100)

    class MySubSub(MySub):
        @lazyperclassproperty
        def foo(cls):
            # print "foo called"
            return random.randint(1,100)

    foo_base = [MyBase.foo for _ in range(5)]
    foo_sub = [MySub.foo for _ in range(5)]
    foo_subsub = [MySubSub.foo for _ in range(5)]

# Generated at 2022-06-14 06:43:27.742031
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    @lazyperclassproperty
    def foo(cls):
        return cls.__name__

    assert foo.__doc__ is None
    assert A.foo == 'A'
    assert B.foo == 'B'
    assert C.foo == 'C'



# Generated at 2022-06-14 06:43:32.822510
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    assert(not hasattr(test_lazyclassproperty, '_lazy_foo'))
    class foo(object):
        @lazyclassproperty
        def bar(cls):
            return 'BAR'
    assert(foo.bar == 'BAR')
    assert(hasattr(foo, '_lazy_bar'))
    assert(foo._lazy_bar == 'BAR')



# Generated at 2022-06-14 06:43:42.045026
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    print("testing lazyclassproperty")
    c = 0
    class A:
        @lazyclassproperty
        def a(cls):
            nonlocal c
            c += 1
            return c
    print("A.a: %s, should be 1" % A.a)
    print("A.a: %s, should be 1" % A.a)
    print("A.a: %s, should be 1" % A.a)
    print("A.a: %s, should be 1" % A.a)
    print("A.a: %s, should be 1" % A.a)
    print("done testing lazyclassproperty")



# Generated at 2022-06-14 06:43:47.392755
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class LazyClass(object):
        @lazyclassproperty
        def foo(cls):
            print('foo called.')
            return 'bar'

    print(LazyClass.foo)
    print(LazyClass.foo)

    # Should output:
    # foo called.
    # bar
    # bar



# Generated at 2022-06-14 06:43:50.929614
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def foo(cls):
            return cls.__name__

    class B(A):
        pass

    class C(A):
        pass

    assert A.foo == 'A'
    assert B.foo == 'B'
    assert C.foo == 'C'

# Generated at 2022-06-14 06:43:58.303367
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass(object):
        # Demonstrate usage of lazyclassproperty
        @lazyclassproperty
        def func1(cls):
            return 1

        @lazyclassproperty
        def func2(cls):
            return cls.func3()

        @lazyclassproperty
        def func3(cls):
            return 3

        @lazyclassproperty
        def func4(cls):
            return 4

    # Test func1, func2 and func3
    assert TestClass.func1 == 1
    assert TestClass.func1 == 1  # Test if lazyclassproperty works
    assert TestClass.func2 == 3
    assert TestClass.func2 == 3  # Test if lazyclassproperty works
    assert TestClass.func3 == 3
    assert TestClass.func3 == 3  # Test if lazyclassproperty works



# Generated at 2022-06-14 06:44:07.980748
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    a = [1,2,3]
    print('Initial array: {}'.format(a))
    print('Length of initial array: {}'.format(len(a)))

    @lazyperclassproperty
    def length():
        print('Lazy length function called.')
        return len(a)

    print('Tenative length: {}'.format(length))
    print('Tenative length again: {}'.format(length))
    print('Tenative length again and again: {}'.format(length))
    print('Done.')


if __name__ == '__main__':
    test_lazyperclassproperty()