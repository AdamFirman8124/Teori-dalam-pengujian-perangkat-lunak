

# Generated at 2022-06-14 06:35:45.784793
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base():
        @lazyperclassproperty
        def prop(cls):
            print("Base prop")
            return "Base prop"

    class A(Base):
        pass

    class B(Base):
        pass

    assert A.prop == "Base prop"
    assert B.prop == "Base prop"
    assert not A.prop is B.prop
    assert A.prop is A.prop

# Generated at 2022-06-14 06:35:55.238926
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # See these references for explanations on descriptors:
    # https://www.ianlewis.org/en/python-descriptors-implementing-property
    # https://www.python-course.eu/python3_properties.php
    # https://docs.python.org/3/howto/descriptor.html#descriptor-protocol
    # https://docs.python.org/3/reference/datamodel.html#specialnames
    # https://www.programiz.com/python-programming/property
    # https://stackoverflow.com/questions/17330160/python-property-versus-get-set-methods-for-variable-validation

    class Base(object):
        @lazyperclassproperty
        def lazy_class_property(cls):
            return 'Base'

# Generated at 2022-06-14 06:36:00.470643
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        x = lazyclassproperty(lambda c: 'foo')

    class B(A):
        pass

    class C(B):
        pass

    assert A.x == 'foo'
    assert B.x == 'foo'
    assert C.x == 'foo'

    A.x = 'bar'
    assert A.x == 'bar'

    assert B.x == 'foo'
    assert C.x == 'foo'



# Generated at 2022-06-14 06:36:09.739180
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            print('here')
            return 'baz'

    assert Foo.bar == 'baz'
    assert Foo.bar == 'baz'
    assert Foo().bar == 'baz'
    assert Foo().bar == 'baz'
    assert Foo.__dict__['_lazy_bar'] == 'baz'
    assert '_lazy_bar' in Foo.__dict__

    delattr(Foo, '_lazy_bar')
    assert Foo.bar == 'baz'
    assert Foo.__dict__['_lazy_bar'] == 'baz'



# Generated at 2022-06-14 06:36:23.114183
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        def __init__(self, a):
            self.a = a
        def __str__(self):
            return str(self.a)


# Generated at 2022-06-14 06:36:27.333305
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def prop(cls):
            return 1

    class B(A):
        pass


# Generated at 2022-06-14 06:36:38.952633
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Parent(object):
        def __init__(self, a, b=1):
            self.a = a
            self.b = b

    class Child(Parent):
        pass

    p, c = Parent(1), Child(2)

    assert p.a == 1
    assert c.a == 2
    assert p.b == 1
    assert c.b == 1

    @lazyperclassproperty
    def test(self):
        yield (self.a, self.b)
        yield self.__class__.__name__

    Parent.test = test
    Child.test = test

    assert next(p.test) == (1, 1)
    assert next(p.test) == 'Parent'
    assert next(c.test) == (2, 1)

# Generated at 2022-06-14 06:36:47.845507
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A: pass
    class B(A): pass
    class C(B): pass
    class D(C): pass

    @lazyclassproperty
    def prop(cls):
        print(f'called for {cls.__name__}')
        return f'{cls.__name__}'

    assert prop.__get__(A) == 'A'
    assert prop.__get__(B) == 'A'
    assert prop.__get__(C) == 'A'
    assert prop.__get__(D) == 'A'



# Generated at 2022-06-14 06:36:57.187192
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:37:10.821273
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Tests the lazyclassproperty function.
    """
    class Test(object):
        __slots__ = ('a',)

        @staticmethod
        def geta(cls):
            return cls.a

        @lazyclassproperty
        def b(cls):
            return cls.geta(cls)

        @lazyclassproperty
        def c(cls):
            return cls.geta(cls) * 2

    Test.a = 5

    assert Test.b == 5
    assert Test.c == 10

    Test.b = 6
    assert Test.b == 5

    Test.c = 20

    assert Test.c == 10

    try:
        Test.b = 10
    except TypeError:
        pass

# Generated at 2022-06-14 06:37:22.490857
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        _lazyprop = 5

        @lazyperclassproperty
        def lazyprop(cls):
            return cls._lazyprop

    class B(A):
        _lazyprop = 10

    assert A.lazyprop == B.lazyprop == 5
    assert A().lazyprop == B().lazyprop == 5

    A._lazyprop = 20
    assert A.lazyprop == 20

    B._lazyprop = 25
    assert B.lazyprop == 25

    assert A.lazyprop == 20
    assert A().lazyprop == 20



# Generated at 2022-06-14 06:37:30.707621
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        no = 0
        def __init__(self):
            self.no = self.no + 1
        @lazyperclassproperty
        def foo(cls):
            return cls.no

    class Inheritor(Base):
        no = 0

    assert Base.foo == 1
    assert Inheritor.foo == 1

    Base()
    Inheritor()

    assert Base.foo == 1
    assert Inheritor.foo == 2

    Base()
    Inheritor()

    assert Base.foo == 1
    assert Inheritor.foo == 3

# Generated at 2022-06-14 06:37:43.391292
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self):
            self.value = 0
        @lazyclassproperty
        def x(cls):
            cls.x = 0
            return cls.x
        @lazyperclassproperty
        def y(cls):
            cls.y = 0
            return cls.y

    a = A()
    b = A()
    assert a.x == b.x == 0
    assert a.y == b.y == 0
    a.x += 1
    a.y += 1
    assert a.x == b.x == 1
    assert a.y == b.y == 0
    b.x += 1
    b.y += 1
    assert a.x == b.x == 2
    assert a.y == b.y == 1
    assert A

# Generated at 2022-06-14 06:37:49.781259
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 1

    assert A.prop == 1
    assert A.prop == 1

    class B(A):
        pass

    assert isinstance(A.prop, int)
    assert isinstance(B.prop, int)
    assert A.prop == 1
    assert B.prop == 1



# Generated at 2022-06-14 06:37:53.646480
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def lazy(self):
            print('Calculating...')
            return 42

    print(A.lazy)
    print(A.lazy)



# Generated at 2022-06-14 06:38:04.626262
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def f(self):
            return lambda x: x * 2

        @lazyclassproperty
        def f_with_params(cls):
            return lambda x, y, z: x * y * z

    assert A.f is A.f
    assert A.f_with_params is A.f_with_params
    assert A.f(5) == 10
    assert A.f_with_params(2, 3, 4) == 24

    class B(A):
        pass

    assert B.f is A.f
    assert B.f is B.f
    assert B.f_with_params is A.f_with_params
    assert B.f_with_params is B.f_with_params
    assert B.f(5) == 10


# Generated at 2022-06-14 06:38:10.218432
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:38:12.568206
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def a(self):
            return 'a'

    class B(A):
        pass

    a = A()
    b = B()

    assert a.a == 'a'
    assert b.a == 'a'
    assert a.a is not b.a



# Generated at 2022-06-14 06:38:17.503823
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo:
        @lazyclassproperty
        def foo(cls):
            return 'foo'

    class Bar(Foo):
        pass

    class Baz(Bar):
        pass

    assert Foo._lazy_foo == 'foo'
    assert Bar._lazy_foo == 'foo'
    assert Baz._lazy_foo == 'foo'
    assert Bar._lazy_foo is Foo._lazy_foo



# Generated at 2022-06-14 06:38:22.553497
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    """
    Test function lazyperclassproperty
    """
    class A(object):
        @lazyperclassproperty
        def fn(cls):
            print('in A.fn')
            return 'fn in A'

    class B(A):
        @lazyperclassproperty
        def fn(cls):
            print('in B.fn')
            return 'fn in B'

    a_attr_name = '_%s_lazy_%s' % ('A', 'fn')
    # print(a_attr_name)
    b_attr_name = '_%s_lazy_%s' % ('B', 'fn')
    # print(b_attr_name)

    assert A.fn == 'fn in A'
    assert hasattr(A, a_attr_name)

# Generated at 2022-06-14 06:38:35.320255
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def some_property(cls):
            return 1

    class A(Base):
        pass

    class B(Base):
        pass

    assert A.some_property == 1
    assert B.some_property == 1

    A.some_property = 2
    assert A.some_property == 2
    assert Base.some_property == 1
    assert B.some_property == 1

    B.some_property = 3
    assert A.some_property == 2
    assert Base.some_property == 1
    assert B.some_property == 3



# Generated at 2022-06-14 06:38:45.117032
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Test(object):
        _x = 0

        @lazyperclassproperty
        def x(cls):
            cls._x += 1
            return cls.y()

        @classmethod
        def y(cls):
            return cls._x

    class Test2(Test):
        pass

    class Test3(Test):
        pass


# Generated at 2022-06-14 06:38:49.890383
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:38:55.433340
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class X(object):
        test_value = None
        @lazyclassproperty
        def value(cls):
            cls.test_value = 'test'
            return cls.test_value
    x = X()
    assert x.value == 'test'
    assert X.test_value == 'test'
    assert X.value == 'test'


# Generated at 2022-06-14 06:38:58.800573
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        _lazy_attr = lazyclassproperty(lambda obj: 'bar')


# Generated at 2022-06-14 06:39:03.262683
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            return 'bar'
    class B(A):
        pass

    assert A.foo == 'bar'
    assert B.foo == 'bar'


# Generated at 2022-06-14 06:39:07.799572
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def callme(cls):
            return "test"
    a = A()

# Generated at 2022-06-14 06:39:14.959869
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base():
        x = 1
    
        @lazyperclassproperty
        def y(cls):
            return cls.x
        
        @lazyperclassproperty
        def z(cls):
            return cls.x * 2
    
    class Derived(Base):
        x = 2
    
    assert Base.y == 1
    assert Derived.y == 2
    assert Base.z == 2



# Generated at 2022-06-14 06:39:20.071919
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    def f(cls):
        return 'foo'
    assert lazyclassproperty(f) is type(3).__class__.__dict__['_lazy_f']
    assert lazyclassproperty(f)(int) == 'foo'
    assert int._lazy_f == 'foo'



# Generated at 2022-06-14 06:39:28.980692
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    print("\nFunction 'lazyclassproperty' test:\n-------------------------------------------------")

    class MyClass():
        ticks = 0

        @lazyclassproperty
        def var(cls):
            cls.ticks += 1
            return 1

    assert MyClass.ticks == 0
    assert MyClass.var == 1
    assert MyClass.ticks == 1
    assert MyClass.var == 1
    assert MyClass.ticks == 1

    class MyChildClass(MyClass):
        pass

    assert MyChildClass.var == 1
    assert MyClass.var == 1



# Generated at 2022-06-14 06:39:43.164882
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return 1
        @lazyperclassproperty
        def y(cls):
            return 2
    class B(A):
        @lazyperclassproperty
        def x(cls):
            return 3
    assert B.x != A.x != B.y != A.y


# Generated at 2022-06-14 06:39:49.103806
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class ClassA:
        @lazyperclassproperty
        def x(cls):
            return 'A'

    class ClassB(ClassA):
        @lazyperclassproperty
        def x(cls):
            return 'B'

    assert ClassA.x == 'A'
    assert ClassB.x == 'B'

    class ClassC(ClassA):
        pass

    assert ClassC.x == 'A'



# Generated at 2022-06-14 06:39:53.491604
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        @lazyclassproperty
        def foobar(cls):
            return 1

    class B(A):
        pass

    assert A.foobar == 1
    assert B.foobar == 1

    A.foobar = 2
    assert A.foobar == 2
    assert B.foobar == 1



# Generated at 2022-06-14 06:40:00.010985
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def b(cls):
            return cls.c

        c = 1

    assert A.b == 1

    class B(A):
        c = 2

    assert B.b == 2
    assert A.b == 1

    class C(A):
        c = 3

    assert C.b == 3
    assert B.b == 2
    assert A.b == 1


if __name__ == '__main__':
    test_lazyclassproperty()
    exit(0)

# Generated at 2022-06-14 06:40:07.692366
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def foo(cls):
            return []
    class Bar(Foo):
        pass
    assert Foo.foo is not Bar.foo
    assert len(Foo.foo) == 0
    assert len(Bar.foo) == 0
    Foo.foo.append('foo')
    Bar.foo.append('bar')
    assert Foo.foo == ['foo']
    assert Bar.foo == ['bar']



# Generated at 2022-06-14 06:40:12.489161
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test1(object):
        @lazyclassproperty
        def me(self):
            return 'test1'

    class Test2(Test1):
        pass

    assert Test1.me == 'test1'
    assert Test2.me == 'test1'



# Generated at 2022-06-14 06:40:14.322644
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def x(cls):
            print("x was called")
            return 'x'

    class B(A):
        pass

    assert A.x == B.x == "x"



# Generated at 2022-06-14 06:40:23.935190
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # define a function
    def some_class_method(cls):
        return(cls.__name__)
    # make it a class property
    klass_method = classproperty(some_class_method)
    # define 2 classes
    class A(object):
        pass
    class B:
        pass
    # show how different classes get different values from the same property
    assert klass_method.__get__(A, A) == 'A'
    assert klass_method.__get__(B, B) == 'B'

# Generated at 2022-06-14 06:40:30.464459
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class C(object):
        _x = 1
        @lazyperclassproperty
        def x(cls):
            return cls._x

    class D(C):
        _x = 2

    class E(C):
        _x = 3

    assert C.x == 1
    assert D.x == 2
    assert E.x == 3


# Generated at 2022-06-14 06:40:42.381773
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    # If a value has been assigned, it will keep returning the same value
    class X(object):
        @lazyperclassproperty
        def x(cls):
            return random.random()

    class Y(X):
        pass

    x1 = X.x
    y1 = Y.x
    x2 = X.x
    y2 = Y.x

    assert x1 is x2
    assert y1 is y2
    assert x1 is not y1

    # If a value has not been assigned, the lambda's return value will be assigned to the attribute on the first
    # access, so it will not be the same on the second access
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return random.random()

    class B(A):
        pass


# Generated at 2022-06-14 06:41:06.738113
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return cls.__name__

    class B(A):
        pass

    @lazyperclassproperty
    def bar(cls):
        return cls.__name__

    assert A.foo == "A"
    assert B.foo == "B"
    assert bar == "module"



# Generated at 2022-06-14 06:41:19.962758
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def x(self):
            # this function should be called twice:
            # once for class kA and once for class V
            return 1

    class B(A):
        pass

    class C(B):
        pass

    class D(B):
        @lazyperclassproperty
        def x(self):
            # this function should be called twice:
            # once for class kA and once for class V
            return 4

    class E(D):
        pass

    print(A.x, B.x, C.x, D.x, E.x)
    assert A.x != B.x != C.x != D.x != E.x


if __name__ == '__main__':
    test_lazyperclassproperty()
    import doctest


# Generated at 2022-06-14 06:41:29.792777
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:39.176887
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:43.424993
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def LIST(cls):
            return list()

    class B(A):
        pass

    assert A.LIST is not B.LIST
    A.LIST.append(1)

    assert len(A.LIST) == 1
    assert len(B.LIST) == 0



# Generated at 2022-06-14 06:41:47.024757
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def hi(cls):
            return "hi"

    class B(A):
        pass

    assert A.hi == B.hi == "hi"



# Generated at 2022-06-14 06:41:53.149869
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        f = lazyclassproperty(lambda cls: 'return')

    class B(A):
        pass

    class C(B):
        pass

    a = A()
    b = B()
    c = C()

    # All instance should have the same cached value
    assert a.f == b.f == c.f == 'return'



# Generated at 2022-06-14 06:42:02.358503
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:42:05.832474
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def mylazy(cls): return cls.__name__

    assert Test.mylazy == 'Test'



# Generated at 2022-06-14 06:42:11.141525
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            print('get property')
            return 42

    class B(A):
        pass

    assert A.prop == 42
    assert B.prop == 42

    """
    get property

    """



# Generated at 2022-06-14 06:42:53.396290
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def f(cls):
            return 1
    class B(A):
        pass
    class C(A):
        pass

    assert A.f == 1
    assert B.f == 1
    assert C.f == 1
    A.f = 2
    assert B.f == 1
    assert C.f == 1
    A.f = 3
    assert B.f == 1
    assert C.f == 1
    C.f = 4
    assert B.f == 1
    assert C.f == 4
    B.f = 5
    assert B.f == 5
    assert C.f == 4

# Generated at 2022-06-14 06:43:00.349486
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def x(cls): return 123

    class B(A):
        pass

    assert A.x == B.x == 123
    A.x = 456
    assert A.x == 456
    assert B.x == 123
    B.x = 789
    assert A.x == A.x == 456
    assert B.x == B.x == 789



# Generated at 2022-06-14 06:43:13.989217
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # Note that this test relies on non-public implementation details.
    # The implementation of lazyperclassproperty could change, and the test would need to change as well.
    # This test is here mostly to provide assurances that the function is working as intended.
    # It is not designed to be a comprehensive unit test.

    class Base(object):
        def __init__(self, value):
            self._value = value

    class A(Base):
        @lazyperclassproperty
        def prop(cls):
            return cls._value

    class B(Base):
        @lazyperclassproperty
        def prop(cls):
            return cls._value

    class C(A):
        pass

    class D(C):
        pass

    class E(D):
        pass

    base = Base(10)

# Generated at 2022-06-14 06:43:16.793672
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class X(object):
        @lazyclassproperty
        def y(cls):
            print('executing initialization')
            return 42

    assert X.y == 42
    assert X.y == 42



# Generated at 2022-06-14 06:43:28.358595
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyOwner(object):

        @lazyclassproperty
        def value(cls):
            return cls, id(cls)

    class InheritFromMyOwner(MyOwner):
        pass

    assert (MyOwner, id(MyOwner)) == MyOwner.value
    assert (InheritFromMyOwner, id(InheritFromMyOwner)) == InheritFromMyOwner.value
    assert (MyOwner, id(MyOwner)) == MyOwner.value
    assert (InheritFromMyOwner, id(InheritFromMyOwner)) == InheritFromMyOwner.value
    assert MyOwner.value is InheritFromMyOwner.value is MyOwner.value



# Generated at 2022-06-14 06:43:33.948065
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    class A(Test):
        @lazyclassproperty
        def prop(cls):
            return cls.x * cls.y

    class B(A):
        x = 2

    class C(B):
        y = 3

    assert C.prop == 6


# Generated at 2022-06-14 06:43:44.799827
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    @lazyperclassproperty
    def answer(cls):
        return 42

    class Foo(object):
        pass

    class Bar(Foo):
        pass

    class Baz(Foo):
        pass

    assert answer == 42
    assert Foo.answer == 42
    assert Bar.answer == 42
    assert Baz.answer == 42
    Foo.answer = 10
    assert Foo.answer == 10
    assert Bar.answer == 42
    assert Baz.answer == 42
    Bar.answer = 20
    assert Foo.answer == 10
    assert Bar.answer == 20
    assert Baz.answer == 42



# Generated at 2022-06-14 06:43:52.792519
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Base(object):
        @lazyperclassproperty
        def foo(cls):
            print('Running %s.foo method.' % cls.__name__)
            return 'foo'

    class A(Base):
        pass

    class B(Base):
        pass

    class C(B):
        pass

    a = A()
    b = B()
    c = C()
    assert a.foo == b.foo
    assert a.foo == c.foo
    assert a.foo != A.foo
    assert a.foo != B.foo
    assert a.foo != C.foo
    assert A.foo == b.foo
    assert A.foo == c.foo
    assert A.foo != B.foo
    assert A.foo != C.foo
    assert B.foo == c.foo
    assert B

# Generated at 2022-06-14 06:44:04.402366
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 1

    assert A.a == 1
    assert A.__dict__['_lazy_a'] == 1
    assert A().a == 1

    class B(A):
        pass

    assert B.a == 1
    assert B.__dict__['_lazy_a'] == 1
    assert B().a == 1

    class C(A):
        @lazyclassproperty
        def a(cls):
            return 2

    assert C.a == 2
    assert C.__dict__['_lazy_a'] == 2
    assert C().a == 2
    assert '_lazy_a' not in A.__dict__
    assert A.a == 1



# Generated at 2022-06-14 06:44:10.501598
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):

        @lazyclassproperty
        def foo(cls):
            return 'bar'

        @lazyclassproperty
        def bar(cls):
            return 'foo'

    class B(A):
        pass
    class C(B):
        pass

    assert A.foo == 'bar'
    assert A.bar == 'foo'
    assert B.foo == 'bar'
    assert B.bar == 'foo'
    assert C.foo == 'bar'
    assert C.bar == 'foo'

