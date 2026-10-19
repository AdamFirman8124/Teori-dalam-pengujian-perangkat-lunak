

# Generated at 2022-06-14 06:35:41.254224
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:35:46.102206
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        pass
    class B(A):
        pass
    class C(B):
        @lazyperclassproperty
        def x(cls):
            return cls.__name__

    print(A.x)
    print(B.x)
    print(C.x)



# Generated at 2022-06-14 06:35:54.348827
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):

        @lazyperclassproperty
        def some_property(cls):
            return {"hello": "world"}

    class B(A):
        pass

    class C(A):
        pass

    a = A()
    b = B()
    c = C()

    assert a.some_property == b.some_property == c.some_property == {"hello": "world"}
    a.some_property["foo"] = "bar"
    assert a.some_property == {"hello": "world", "foo": "bar"}
    assert b.some_property == c.some_property == {"hello": "world"}



# Generated at 2022-06-14 06:35:57.429757
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def func(cls):
            return lambda : "hello"

    class B(A):
        @lazyperclassproperty
        def func(cls):
            return lambda : "world"

    assert A().func() == "hello"
    assert B().func() == "world"



# Generated at 2022-06-14 06:36:01.690008
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        @lazyperclassproperty
        def bar(cls):
            return cls.__name__

    class Foo2(Foo):
        pass

    class Foo3(Foo):
        pass

    assert Foo.bar == 'Foo'
    assert Foo2.bar == 'Foo2'
    assert Foo3.bar == 'Foo3'



# Generated at 2022-06-14 06:36:11.206265
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:36:19.512921
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @classproperty
        def prop(cls):
            return 'base'

    class A(Base):
        pass

    class B(Base):
        pass

    assert A.prop == 'base'
    assert B.prop == 'base'

    @lazyperclassproperty
    def prop(cls):
        return 'hit'

    assert A.prop == 'hit'
    assert B.prop == 'hit'



# Generated at 2022-06-14 06:36:25.224929
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    assert not hasattr(A, "_lazy_name")
    assert A.name == "A"
    assert hasattr(A, "_lazy_name")

    assert not hasattr(B, "_lazy_name")
    assert B.name == "B"
    assert hasattr(B, "_lazy_name")

    assert not hasattr(C, "_lazy_name")
    assert C.name == "C"
    assert hasattr(C, "_lazy_name")


# Generated at 2022-06-14 06:36:37.652437
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self, name):
            self.name = name

        @lazyperclassproperty
        def f(cls):
            print('Calling f for {}'.format(cls.__name__))
            return cls

    class B(A):
        @lazyperclassproperty
        def f(cls):
            print('Calling f for {}'.format(cls.__name__))
            return cls

    a1 = A('a1')
    a2 = A('a2')
    b1 = B('b1')
    b2 = B('b2')
    print('Test lazyperclassproperty:')
    assert(a1.f() is A)
    assert(a2.f() is A)
    assert(b1.f() is B)

# Generated at 2022-06-14 06:36:46.553813
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print("A: foo = 1")
            return 1

    class B(A):
        pass

    class C(A):
        @lazyclassproperty
        def foo(cls):
            print("C: foo = 2")
            return 2

    class D(C):
        pass

    # Test case 1
    # A.foo should print "A: foo = 1"
    # and return 1
    print("A.foo = %s" % (A.foo,))

    # Test case 2
    # B.foo should return 1
    # and not print anything
    print("B.foo = %s" % (B.foo,))

    # Test case 3
    # C.foo should print "C: foo = 2"
   

# Generated at 2022-06-14 06:36:59.297297
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            return 'foo'

    class B(A):
        pass

    class C(A):
        pass

    assert A.x == 'foo'
    assert B.x == 'foo'
    assert C.x == 'foo'

    A.x = 'bar'
    # A and B should have different x's.
    assert A.x == 'bar'
    assert B.x == 'foo'
    assert C.x == 'foo'

    del A.x
    # A and B should have different x's.
    assert A.x == 'foo'
    assert B.x == 'foo'
    assert C.x == 'foo'

    # These should be the exact same object.
    assert A.x is A.x
   

# Generated at 2022-06-14 06:37:04.353120
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class ATester(object):
        @lazyperclassproperty
        def a_lazy_prop(cls):
            return cls.__name__

    class BTester(ATester):
        pass


# Generated at 2022-06-14 06:37:14.522615
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class B(object):
        def __init__(self):
            self.i = 1

    class D(B):
        def __init__(self):
            super().__init__()
            self.i = 2
            self.L = []

    @lazyclassproperty
    def i(cls):
        return cls().i

    @lazyclassproperty
    def L(cls):
        L = cls().L
        L.append('foo')
        return L

    assert i == 1
    assert i == 1  # use cached value

    assert D.i == 2
    assert D.L == ['foo']

    assert D.i == 2  # use cached value
    assert D.L == ['foo']  # use cached value
    assert not hasattr(B, '_lazy_i')

# Generated at 2022-06-14 06:37:25.204895
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class TestA(object):
        a = 0
        b = 0

        @lazyperclassproperty
        def random_value(self):
            return randint(1, 100)

    class TestB(TestA):
        a = 10

    a = TestA()
    b = TestB()

    assert isinstance(a.random_value, int)
    assert isinstance(b.random_value, int)

    a_random_value = a.random_value
    b_random_value = b.random_value

    a.a = 1
    b.a = 1

    assert a.random_value == a_random_value
    assert b.random_value == b_random_value


# Generated at 2022-06-14 06:37:31.090674
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class Foo(object):

        @lazyclassproperty
        def bar(cls):
            return {"foo": "bar"}

    assert Foo.bar == {"foo": "bar"}
    assert Foo().bar == {"foo": "bar"}

    class FooChild(Foo):
        pass

    assert FooChild.bar == {"foo": "bar"}
    assert FooChild().bar == {"foo": "bar"}



# Generated at 2022-06-14 06:37:37.215448
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Test(object):
        class A(object):
            pass

        class B(object):
            pass

        @lazyperclassproperty
        def lazy(cls):
            return object()

    assert Test.A.lazy is Test.B.lazy is not Test.lazy
    assert Test.lazy is Test.lazy



# Generated at 2022-06-14 06:37:45.637048
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self, x):
            self._x = x

        @lazyclassproperty
        def x(cls):
            return cls._x

    class B(A):
        _x = 10

    class C(A):
        _x = -10

    assert B.x == 10
    assert C.x == -10
    assert A.x == 0
    assert B().x == 10
    assert C().x == -10
    assert A(0).x == 0


# Generated at 2022-06-14 06:37:55.566186
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def prop_1(cls):
            return 1
        @lazyclassproperty
        def prop_2(cls):
            return 2

    class B(A):
        @lazyclassproperty
        def prop_3(cls):
            return 3
        @lazyclassproperty
        def prop_4(cls):
            return 4

    assert A.prop_1 == 1
    assert A.prop_2 == 2
    assert B.prop_1 == 1
    assert B.prop_2 == 2
    assert B.prop_3 == 3
    assert B.prop_4 == 4



# Generated at 2022-06-14 06:38:00.685824
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    "Unit test for method lazyclassproperty"
    class Test(object):
        @lazyclassproperty
        def Test(cls):
            Test.var += 1
            return Test.var

    Test.var = 0
    assert Test.Test == 1
    assert Test.Test == 1

# Generated at 2022-06-14 06:38:10.890643
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from time import sleep

    @lazyclassproperty
    def class_prop(cls):
        print('finding class prop')
        sleep(1)
        return 'yay'

    @lazyclassproperty
    def class_prop_with_args(cls, a, b):
        return a + b

    @lazyclassproperty
    def class_prop_with_kwargs(cls, a, b=1):
        return a + b

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    a = A()
    b = B()
    c = C()
    d = D()

    assert A.class_prop == 'yay'

# Generated at 2022-06-14 06:38:21.219390
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            print('called')
            return 1

    class B(A):
        pass

    assert A.prop == 1, 'first call'
    assert A.prop == 1, 'second call'
    assert B.prop == 1, 'first call'
    assert B.prop == 1, 'second call'



# Generated at 2022-06-14 06:38:32.797066
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass:

        @lazyclassproperty
        def test_prop_get(cls):
            return len(cls.__name__)

    class TestSubClass(TestClass):
        pass

    class TestSubSubClass(TestSubClass):
        pass

    assert TestClass.test_prop_get == len(TestClass.__name__)
    assert TestSubClass.test_prop_get == len(TestSubClass.__name__)
    assert TestSubSubClass.test_prop_get == len(TestSubSubClass.__name__)

    # Verify that the property value is cached
    assert TestClass._lazy_test_prop_get == len(TestClass.__name__)



# Generated at 2022-06-14 06:38:36.713944
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def x(cls):
            return 11
    class B(A):
        pass
    assert A.x == 11
    assert B.x == 11
    B.x = 12
    assert B.x == 12
    assert A.x == 11



# Generated at 2022-06-14 06:38:45.059481
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print("foo")
            return 1

        def bar(self):
            return self.foo

    class B(A):
        pass

    assert A.foo == 1
    assert B.foo == 1

    a = A()
    b = B()

    assert a.bar() == 1
    assert b.bar() == 1


# Generated at 2022-06-14 06:38:53.845951
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    def _fn(cls):
        return (cls.Foo, cls.Bar)

    class _cls1(object):
        Foo = 1
        Bar = 2
        c = lazyclassproperty(_fn)

    class _cls2(object):
        Foo = 10
        Bar = 20
        c = lazyclassproperty(_fn)

    c1 = _cls1()
    c2 = _cls2()
    assert c1.c == (1, 2)
    assert c2.c == (10, 20)



# Generated at 2022-06-14 06:39:01.313206
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    assert lazyclassproperty
    class C(object):
        @lazyclassproperty
        def foo(cls):
            #print "foo()"
            return 42

        @lazyclassproperty
        def foo2(cls):
            #print "foo2()"
            return 43

    assert C.foo == 42
    assert C.foo2 == 43
    assert C.foo == 42
    assert C.foo2 == 43
    assert C.foo == 42
    assert C.foo2 == 43

    class D(C):
        pass
    assert D.foo == 42
    assert D.foo2 == 43
    assert D.foo == 42
    assert D.foo2 == 43

    class E(D):
        pass
    assert E.foo == 42
    assert E.foo2 == 43
    assert E.foo == 42


# Generated at 2022-06-14 06:39:09.254691
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:13.194581
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test:
        @lazyclassproperty
        def foo(cls):
            print("lazy evaluation")
            return 'foo'

    assert Test.foo == 'foo'
    assert Test.foo == 'foo'



# Generated at 2022-06-14 06:39:18.447446
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self, v):
            self.v = v

        @lazyclassproperty
        def p(cls):
            return cls.v

    a = A(5)
    assert a.p == 5
    b = A(6)
    assert b.p == 6



# Generated at 2022-06-14 06:39:23.557312
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def f1(self):
            return 'hello'

        @lazyclassproperty
        def f2(self):
            return 'world'

    assert A.f1 == 'hello'
    assert A.f2 == 'world'
    assert A.f1 == 'hello'
    assert A.f2 == 'world'



# Generated at 2022-06-14 06:39:38.491197
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    from types import FunctionType
    from types import MethodType

    def _is_method(obj):
        return isinstance(obj, MethodType) or isinstance(obj, FunctionType)

    class Foo:
        @lazyperclassproperty
        def bar(cls):
            return 'bar %s' % cls

    assert Foo.bar == 'bar <class \'__main__.Foo\'>'
    assert _is_method(Foo.bar)

    class Bar:
        @lazyperclassproperty
        def bar(cls):
            return 'bar %s' % cls

    assert Bar.bar == 'bar <class \'__main__.Bar\'>'
    assert _is_method(Bar.bar)

    assert Foo.bar == 'bar <class \'__main__.Foo\'>'
    assert _is

# Generated at 2022-06-14 06:39:52.295534
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from nose.tools import assert_equal
    from random import randint

    class A(object):
        @lazyclassproperty
        def rand(cls):
            return randint(1, 100)

        @lazyclassproperty
        def rand_str(cls):
            return str(cls.rand)

    class B(A):
        pass

    assert_equal(A.rand_str, '%s' % A.rand)
    assert_equal(B.rand_str, '%s' % B.rand)

    A.rand = 5

    assert_equal(A.rand_str, '%s' % A.rand)
    assert_equal(B.rand_str, '%s' % B.rand)

    # Now A.rand should have value 5 and B.rand should have a new value got from rand

# Generated at 2022-06-14 06:39:57.258338
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo:
        @lazyclassproperty
        def prop1(cls):
            return 'Class Property 1'


# Generated at 2022-06-14 06:40:03.639779
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Test:
        x = 0
        @lazyperclassproperty
        def prop(cls):
            cls.x += 1
            return cls.x

    class Test2(Test):
        pass

    assert Test.prop == 1
    assert Test.prop == 1
    assert Test2.prop == 2
    assert Test2.prop == 2

# Generated at 2022-06-14 06:40:07.198315
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def fn(cls):
            return cls

    assert C.fn is C
    assert not hasattr(C, '_lazy_fn')



# Generated at 2022-06-14 06:40:15.530975
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def f(cls):
            n = cls.__name__

# Generated at 2022-06-14 06:40:27.618664
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def cached_property(cls):
            print("cached")
            return 'cached'

    class Sub1(Base):
        pass

    class Sub2(Base):
        pass

    assert Sub1.cached_property == 'cached'
    assert Sub2.cached_property == 'cached'

    Sub1.cached_property = 'overwritten'
    assert Sub1.cached_property == 'overwritten'
    assert Sub2.cached_property == 'cached'

    Sub2.cached_property = 'overwritten'
    assert Sub1.cached_property == 'overwritten'
    assert Sub2.cached_property == 'overwritten'



# Generated at 2022-06-14 06:40:36.233819
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        _value = False

        @lazyclassproperty
        def value(cls):
            cls._value = True
            return 42

    class MySubClass(MyClass):
        pass

    assert not MyClass._value
    assert not MySubClass._value
    assert isinstance(MyClass.value, int)
    assert isinstance(MySubClass.value, int)
    assert MyClass._value
    assert MySubClass._value
    assert MyClass.value == 42
    assert MySubClass.value == 42



# Generated at 2022-06-14 06:40:43.242652
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop(cls):
            return id(cls)

    class B(A):
        pass

    class C(A):
        pass

    assert A.prop == id(A)
    assert B.prop == id(B)
    assert C.prop == id(C)
    assert B.prop == id(B)
    assert A.prop == id(A)



# Generated at 2022-06-14 06:40:52.066895
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class foo(object):
        x = 1

        @lazyclassproperty
        def xplusone(cls):
            return cls.x + 1

        @lazyclassproperty
        def xplustwo(cls):
            return cls.x + 2

    class bar(foo):
        x = 2

    assert foo.xplusone == 2
    assert foo.xplustwo == 3

    assert bar.xplusone == 3
    assert bar.xplustwo == 4



# Generated at 2022-06-14 06:41:19.046674
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class BaseClass(object):
        @lazyperclassproperty
        def base_prop(cls):
            return cls.__name__

    class InheritClass(BaseClass):
        pass

    class InheritClass2(BaseClass):
        @lazyperclassproperty
        def inherit_prop(cls):
            return cls.__name__

    assert BaseClass.base_prop == 'BaseClass'
    assert InheritClass.base_prop == 'InheritClass'
    assert InheritClass2.base_prop == 'InheritClass2'
    assert InheritClass2.inherit_prop == 'InheritClass2'



# Generated at 2022-06-14 06:41:28.213962
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Fruit(object):
        @lazyperclassproperty
        def color(cls):
            return "Red"

    class Apple(Fruit):
        pass

    class Orange(Fruit):
        @lazyperclassproperty
        def color(cls):
            return "Orange"

    class Lemon(Orange):
        pass

    assert Fruit.color == "Red"
    assert Apple.color == "Red"
    assert Orange.color == "Orange"
    assert Lemon.color == "Orange"


# Generated at 2022-06-14 06:41:33.669147
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):

        @lazyperclassproperty
        def test_prop(cls):
            # print('evaluating test_prop')
            return 'value'

    class B(A):
        pass

    b = B()

    assert(b.test_prop == 'value')



# Generated at 2022-06-14 06:41:37.162692
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class BaseClass(object):
        @lazyperclassproperty
        def foo(cls):
            return "foo"

    class DerivedClass(BaseClass):
        pass

    assert BaseClass.foo == "foo"
    assert DerivedClass.foo == "foo"


# Generated at 2022-06-14 06:41:43.915548
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    >>> class A(object):
    ...     @lazyclassproperty
    ...     def a(cls):
    ...             print 'from lazy called'
    ...             return 1
    >>> A.a
    from lazy called
    1
    >>> A.a
    1
    >>> a = A()
    >>> a.a
    2
    >>> a.a
    2
    """



# Generated at 2022-06-14 06:41:52.464784
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def prop(cls):
            print("A")
            return "A"

    class B(A):
        @lazyperclassproperty
        def prop(cls):
            print("B")
            return "B"

    class C(B):
        pass

    class D(A):
        @lazyperclassproperty
        def prop(cls):
            print("D")
            return "D"

    assert A.prop == "A"
    assert B.prop == "B"
    assert C.prop == "B"
    assert D.prop == "D"



# Generated at 2022-06-14 06:42:00.071077
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class MyClass():
        _attr = 'original'

        @lazyperclassproperty
        def attr(cls):
            return cls._attr + '-changed'

    class MyClassInherited(MyClass):
        _attr = 'original-inherited'

    assert MyClass.attr == 'original-changed'
    assert MyClassInherited.attr == 'original-inherited-changed'

# Generated at 2022-06-14 06:42:06.492953
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class C(object):
        @lazyperclassproperty
        def a(cls):
            return 1

    class D(C):
        pass

    class E(C):
        @lazyperclassproperty
        def a(cls):
            return 2

    assert C.a == 1
    assert D.a == 1
    assert E.a == 2
# End of unit test


# Generated at 2022-06-14 06:42:18.033145
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from mozunit import main

    class C(object):
        @lazyclassproperty
        def value(cls):
            return cls.__name__

    class B(C):
        pass

    class D(C):
        pass

    def test_value():
        assert C.value == 'C'
        assert B.value == 'B'
        assert D.value == 'D'

    class Broken(C):
        @lazyclassproperty
        def value(cls):
            return cls.__name__.lower()

    def test_broken():
        try:
            Broken.value
        except AttributeError:
            pass
        else:
            assert False

    class NotBroken(C):
        @lazyclassproperty
        def value(cls):
            return cls.__name__.lower()

# Generated at 2022-06-14 06:42:25.280377
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test:
        def __init__(self):
            self._value = 0

        def set_value(self, value):
            self._value = value

        @lazyclassproperty
        def get_value(cls):
            return cls()

    assert Test.get_value._value == 0
    Test.get_value.set_value(1)
    assert Test.get_value._value == 1



# Generated at 2022-06-14 06:43:04.339255
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        @lazyperclassproperty
        def __prop__(cls):
            return cls.__name__

    class Bar(Foo):
        @lazyperclassproperty
        def __prop__(cls):
            return "Bar"

    assert (Bar.__prop__ == Bar.__prop__ == 'Bar')
    assert (Foo.__prop__ == Foo.__prop__ == 'Foo')
    assert Foo.__prop__ != Bar.__prop__



# Generated at 2022-06-14 06:43:10.093711
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestMe(object):
        @lazyclassproperty
        def foo(cls):
            return 'bar'

    assert TestMe.foo == 'bar'
    assert TestMe._lazy_foo == 'bar'

    class TestMe2(TestMe):
        pass

    assert TestMe2._lazy_foo == 'bar'


# Generated at 2022-06-14 06:43:18.899894
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop1(cls):
            print("prop1")
            return 1

    class B(A):
        @lazyclassproperty
        def prop2(cls):
            print("prop2")
            return 2

    assert A.prop1 == 1
    assert A.prop1 == 1
    assert B.prop1 == 1
    assert B.prop2 == 2
    assert B.prop2 == 2
    assert A.prop1 == 1
    assert B.prop1 == 1
    assert B.prop2 == 2
    assert B.prop2 == 2
    assert A.prop1 == 1



# Generated at 2022-06-14 06:43:28.200688
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def lazy_propery(cls):
            return 1

    assert hasattr(A, '_lazy_lazy_propery')
    assert A.lazy_propery == 1
    assert A.lazy_propery == 1
    assert A._lazy_lazy_propery == 1

    class B(A):
        pass
    assert hasattr(B, '_lazy_lazy_propery')
    assert B.lazy_propery == 1
    assert B.lazy_propery == 1
    assert B._lazy_lazy_propery == 1
    assert A._lazy_lazy_propery == 1


# Generated at 2022-06-14 06:43:35.356390
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class MyClass(object):
        @lazyperclassproperty
        def prop(self):
            print("I am the function which is called")
            return complex(1, 2)

    class MySubClass(MyClass):
        pass

    b = MyClass()
    c = MySubClass()

    print("b.prop:", b.prop)
    print("c.prop:", c.prop)
    if b.prop is c.prop:
        raise RuntimeError("Wrong behavior, b.prop and c.prop must not be the same")



# Generated at 2022-06-14 06:43:39.768705
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        def __init__(self, i):
            self.i = i

        @lazyclassproperty
        def test(cls):
            return cls.i

    assert Foo.test == Foo.test == Foo.i



# Generated at 2022-06-14 06:43:48.556692
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test1(object):
        a = 'a_static'

        @lazyclassproperty
        def b(cls):
            return cls.a

    assert Test1.b == 'a_static'

    class Test2(Test1):
        a = 'a_in_test2'

    assert Test2.b == 'a_in_test2'
    assert Test1.b == 'a_static'

    class Test3(object):
        @lazyclassproperty
        def b(cls):
            return cls.a

        a = 'a_static'

    assert Test3.b == 'a_static'



# Generated at 2022-06-14 06:43:53.052432
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def cache_me(cls):
            return cls.__name__

    assert C.cache_me == 'C', 'lazyclassproperty decorator is broken'



# Generated at 2022-06-14 06:43:59.965444
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop_a(cls):
            return 'a'

    class B(A):
        @lazyperclassproperty
        def prop_b(cls):
            return 'b'

    assert A.prop_a == 'a'
    assert B.prop_b == 'b'
    assert A.prop_b == 'a'
    assert B.prop_a == 'b'



# Generated at 2022-06-14 06:44:06.862832
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    def test(cls):
        print("test")
        return cls

    class A:
        @lazyperclassproperty
        def test(cls):
            print("test")
            return cls

    class B(A):
        pass

    a = A()
    b = B()

    print(A.test)
    print(B.test)
    print(a.test)
    print(b.test)



# Generated at 2022-06-14 06:45:40.738296
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def myproperty(cls):
            return cls.__name__

    class B(A):
        pass

    a = A()
    assert a.myproperty == 'A'
    a.myproperty = 'B'
    assert a.myproperty == 'B'
    del a.myproperty
    assert a.myproperty == 'A'

    b = B()
    assert b.myproperty == 'B'
    b.myproperty = 'C'
    assert b.myproperty == 'C'
    del b.myproperty
    assert b.myproperty == 'B'

