

# Generated at 2022-06-14 06:35:47.916891
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Builder(object):

        def __init__(self):
            self.called = 0

        @lazyclassproperty
        def property(clazz):
            self.called += 1
            return 'test'

    class TestClass(object):

        builder = Builder()

    a = TestClass()
    b = TestClass()

    assert a.builder.called == 0

    assert a.builder.property == 'test'
    assert a.builder.called == 1

    assert b.builder.called == 0
    assert b.builder.property == 'test'
    assert b.builder.called == 1
    assert a.builder.called == 1

    assert a.builder.property == 'test'
    assert a.builder.called == 1
    assert b.builder.called == 1

    a.builder.property = 'something else'

# Generated at 2022-06-14 06:36:01.690186
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        a = 0

        @lazyperclassproperty
        def b(cls):
            cls.a += 1
            return cls.a

    class X(Base):
        pass

    class Y(X):
        pass

    # Test lazy-creation of property
    assert not hasattr(Base, '_Base_lazy_b')
    assert not hasattr(X, '_X_lazy_b')
    assert Base.b == 1
    assert X.b == 1
    assert hasattr(Base, '_Base_lazy_b')
    assert hasattr(X, '_X_lazy_b')
    assert Base.b == 1
    assert X.b == 1

    # Test lazyness for inheritors

# Generated at 2022-06-14 06:36:04.643795
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def test(cls):
            return 5
    class B(A):
        pass
    assert A.test == B.test == 5


# Generated at 2022-06-14 06:36:18.263135
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # given
    class Base(object):
        @lazyperclassproperty
        def x(cls):
            print('Base.x')
            return 'Base.x'

    class Subclass1(Base):
        @lazyperclassproperty
        def y(cls):
            print('Subclass1.y')
            return 'Subclass1.y'

    class Subclass11(Subclass1):
        pass

    class Subclass2(Base):
        @lazyperclassproperty
        def y(cls):
            print('Subclass1.y')
            return 'Subclass2.y'

    class Subclass3(object):
        pass

    def x(cls):
        print('Subclass1.z')
        return 'Subclass1.z'


# Generated at 2022-06-14 06:36:24.809540
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            return "foo"

    class B(A):
        pass

    class C(A):
        pass
        
    A.foo = "bar"

    assert A.foo == "bar"
    assert B.foo == "foo"
    assert C.foo == "foo"

    B.foo = "baz"
    assert A.foo == "bar"
    assert B.foo == "baz"
    assert C.foo == "foo"



# Generated at 2022-06-14 06:36:30.511614
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return cls.__name__

    class B(A):
        """
        Class B has its own foo
        """

    assert A.foo == "A"
    assert B.foo == "B"



# Generated at 2022-06-14 06:36:41.303931
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        def __init__(self):
            self.name = 'Base'
        @lazyperclassproperty
        def test(cls):
            return cls.name

    class DerivedA(Base):
        def __init__(self):
            self.name = 'DerivedA'
        @lazyperclassproperty
        def test(cls):
            return cls.name

    class DerivedB(Base):
        def __init__(self):
            self.name = 'DerivedB'
        @lazyperclassproperty
        def test(cls):
            return cls.name

    BaseA = DerivedA()
    BaseB = DerivedB()
    BaseC = Base()
    BaseD = Base()
    print(BaseA.test)

# Generated at 2022-06-14 06:36:50.394152
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Type1(object):
        def __init__(self):
            self.foo = 1
            self.bar = 2
        @lazyperclassproperty
        def baz(cls):
            return cls.foo + cls.bar

    class Type2(Type1):
        def __init__(self):
            super(Type2, self).__init__()
            self.foo = 3
            self.bar = 4

    a = Type1()
    assert a.baz == 3



# Generated at 2022-06-14 06:37:00.918221
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Test1:
        @lazyperclassproperty
        def foo(cls):
            # print("Test1 foo")
            return 100

    class Test2:
        @lazyperclassproperty
        def foo(cls):
            # print("Test2 foo")
            return 200

    class Test3:
        @lazyperclassproperty
        def foo(cls):
            # print("Test3 foo")
            return 300

    class Test4(Test1):
        pass

    # print("Test1 foo", Test1.foo)
    # print("Test2 foo", Test2.foo)
    # print("Test3 foo", Test3.foo)
    # print("Test1 foo", Test1.foo)

    assert Test1.foo == 100
    assert Test2.foo == 200
    assert Test3.foo == 300

# Generated at 2022-06-14 06:37:09.772856
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        @lazyclassproperty
        def x(self):
            return 5

    class B(A):
        pass

    a = A()
    b = B()

    # class property should be available
    assert A.x == 5

    # properties should be distinct for different inheritors
    assert A.x is a.x
    assert B.x is b.x
    assert A.x is not B.x

    # property should not be callable
    assert not callable(A.x)
    assert not callable(B.x)

    # setting should be blocked
    def setter(self):
        self.x = 3
    a.setter = setter
    pytest.raises(AttributeError, lambda: a.setter())

# Generated at 2022-06-14 06:37:19.724005
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class a(object):
        #@lazyclassproperty
        @lazyperclassproperty
        def pri(cls):
            print("pri")
            return 'a'

    class b(a):
        pass

    print("a")
    print(a.pri)
    print("b")
    print(b.pri)
    print("a")
    print(a.pri)

# test_lazyclassproperty()

# Generated at 2022-06-14 06:37:28.174544
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def prop(cls):
            return cls.__name__

    class Derived(Base):
        pass

    BaseProp = lazyperclassproperty(lambda cls: cls.__name__)

    class Base(object):
        prop = BaseProp

    class Derived(Base):
        pass

    assert Base.prop == 'Base'
    assert Derived.prop == 'Derived'

    #assert BaseProp.__class__.__name__ == 'lazyperclassproperty'



# Generated at 2022-06-14 06:37:32.634215
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        i = 0
        @lazyperclassproperty
        def p(cls):
            cls.i += 1
            return cls.i
    assert A.p == 1
    class B(A):
        pass
    assert B.p == 1
    assert A.p == 2



# Generated at 2022-06-14 06:37:41.755969
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Base(object):
        my_prop = lazyclassproperty(lambda cls: 'value')

    class A(Base):
        pass

    class B(Base):
        pass

    assert A.my_prop == Base.my_prop == 'value'

    B.my_prop = 'value2'
    assert A.my_prop == 'value'
    assert B.my_prop == Base.my_prop == 'value2'

    del A.my_prop
    assert A.my_prop == B.my_prop == Base.my_prop == 'value2'


# Generated at 2022-06-14 06:37:49.553684
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    import time


# Generated at 2022-06-14 06:38:02.028780
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base:
        @lazyperclassproperty
        def prop(cls):
            return 1

    class Child(Base):
        pass

    # Check data
    assert Child.prop == 1
    assert Base.prop == 1
    assert Child._Base_lazy_prop == 1

    # Check type
    assert isinstance(Child.prop, int)
    assert isinstance(Base.prop, int)
    assert isinstance(Child._Base_lazy_prop, int)

    # Check that there's indeed no cross-talk
    Base.prop = 2
    assert Child.prop == 1 and Base.prop == 2
    assert isinstance(Child.prop, int) and isinstance(Base.prop, int)

# Generated at 2022-06-14 06:38:06.085292
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        def f(cls):
            return 42
        g = lazyclassproperty(f)

    assert C.g == 42
    assert C.g == 42

# Generated at 2022-06-14 06:38:13.449772
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return 'foo'

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def foo(cls):
            return 'bar'

    assert A.foo == B.foo == 'foo'
    assert C.foo == 'bar'
    assert A().foo == B().foo == 'foo'
    assert C().foo == 'bar'



# Generated at 2022-06-14 06:38:26.134068
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Test class
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 1

    assert Foo.bar == 1
    assert Foo.bar == 1  # property should only be called once

    # Test metaclass
    class Meta(type):
        @lazyclassproperty
        def bar(cls):
            return 1

    class Foo(object):
        __metaclass__ = Meta

    assert Foo.bar == 1
    assert Foo.bar == 1  # property should only be called once

    # Test inheritance
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 1

    class Baz(Foo):
        pass

    assert Baz.bar == 1
    assert Baz.bar == 1  # property should only be called once

# Generated at 2022-06-14 06:38:35.320351
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class TestClass:
        @lazyperclassproperty
        def a(cls):
            print('a is called')
            return 'a'

        @lazyperclassproperty
        def b(cls):
            print('b is called')
            return 'b'

    class TestClassA(TestClass):
        pass

    class TestClassB(TestClass):
        pass

    print(TestClass.a)
    print(TestClassA.a)
    print(TestClassB.a)
    print(TestClass.b)
    print(TestClassA.b)
    print(TestClassB.b)


# Generated at 2022-06-14 06:38:49.006056
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            print("Calculating foo")
            return 1

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def foo(cls):
            print("Calculating foo")
            return 2

    assert A.foo == 1
    assert A.foo == 1
    assert B.foo == 1
    assert B.foo == 1
    assert C.foo == 2
    assert C.foo == 2



# Generated at 2022-06-14 06:38:58.900747
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    """
    >>> class Foo(object):
    ...     @lazyclassproperty
    ...     def bar(cls):
    ...         print 'bar was called'
    ...         return 'bar'
    >>> class Baz(Foo):
    ...     pass
    >>> foo = Foo()
    >>> foo.bar
    bar was called
    'bar'
    >>> baz = Baz()
    >>> baz.bar
    bar was called
    'bar'
    >>> Foo.bar
    bar was called
    'bar'
    >>> Baz.bar
    bar was called
    'bar'
    >>> Foo.bar = 'not bar'
    >>> Foo.bar
    'not bar'
    >>> Baz.bar
    bar was called
    'bar'
    >>> foo.bar
    'not bar'
    """



# Generated at 2022-06-14 06:39:07.443916
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        def __init__(self,a,b):
            self.a = a
            self.b = b
        @lazyclassproperty
        def lazy(cls):
            print ('lazy')
            return cls.a*cls.b
    class Bar(Foo):
        pass

    foo = Foo(1,2)
    bar = Bar(10,20)
    for obj in foo,bar:
        print (obj.__class__.__name__, obj.lazy)
        print (obj.__class__.__name__, obj.lazy)

#test_lazyclassproperty()

# Generated at 2022-06-14 06:39:14.839501
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def myproperty(cls):
            print("myproperty: %s" % cls.__name__)
            return "myproperty: %s" % cls.__name__

    class Child(Base):
        pass

    class OtherChild(Base):
        pass

    assert Base().myproperty == "myproperty: Base"
    assert Child().myproperty == "myproperty: Child"
    assert OtherChild().myproperty == "myproperty: OtherChild"


# Generated at 2022-06-14 06:39:23.258437
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        @lazyperclassproperty
        def value(cls):
            return cls.__name__


# Generated at 2022-06-14 06:39:30.669534
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Tests the lazyclassproperty function.
    """
    class TestClass:
        pass

    @lazyclassproperty
    def testprop(cls):
        return 42

    assert not hasattr(TestClass, '_lazy_testprop')
    assert TestClass.testprop == 42
    assert TestClass.testprop == 42  # Check that we can access it the second time round
    assert hasattr(TestClass, '_lazy_testprop')



# Generated at 2022-06-14 06:39:33.950719
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            print("eval")
            return "evaluated"
    assert A.prop == "evaluated"
    assert A.prop == "evaluated"


# Generated at 2022-06-14 06:39:43.548410
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    def check(x, y):
        return x == y

    class C1(object):
        @lazyclassproperty
        def x(cls):
            return 'bar'

        @lazyclassproperty
        def y(cls):
            return 'bar'

        @lazyclassproperty
        def z(cls):
            return 'foo'

    class C2(C1):
        @lazyclassproperty
        def y(cls):
            return 'foo'

    c1 = C1()
    c2 = C2()

    if not check(C1.x, 'bar'): return
    if not check(C1.y, 'bar'): return
    if not check(C1.z, 'foo'): return
    if not check(C2.x, 'bar'): return

# Generated at 2022-06-14 06:39:46.356287
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 1

    assert Foo.bar == 1
    assert Foo().bar == 1



# Generated at 2022-06-14 06:39:56.417086
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):

        @lazyperclassproperty
        def a(cls):
            return {'a': cls}

    class B(A):

        @lazyperclassproperty
        def a(cls):
            return {'b': cls}

    assert A.a == {'a': A}
    assert B.a == {'b': B}
    assert A.__dict__ == {'a': {'a': A}}
    assert B.__dict__ == {'a': {'b': B}}

    class C(object):

        @lazyclassproperty
        def c(cls):
            return {'c': cls}

    class D(C):

        @lazyclassproperty
        def c(cls):
            return {'d': cls}

    assert C.c

# Generated at 2022-06-14 06:40:13.310621
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        def __init__(self):
            self.x = 0
        @lazyclassproperty
        def num(cls):
            return cls.x + 1
    class B(A):
        x = 10
    a = A()
    print(A.num)  # 1, prints 1
    print(a.num)  # 1
    b = B()
    print(B.num)  # 11, prints 11
    print(b.num)  # 11



# Generated at 2022-06-14 06:40:27.172993
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def prop(cls):
            return 'prop'

        @lazyclassproperty
        def prop2(cls):
            return 'prop2'

        @lazyperclassproperty
        def prop3(cls):
            return 'prop3'

    class Test2(Test):
        def __init__(self, *args, **kwargs):
            # Ensure _lazy_prop is not set on Test2
            assert not hasattr(Test2, '_lazy_prop')

    assert Test.prop == 'prop'
    assert Test.prop2 == 'prop2'
    assert Test.prop3 == 'prop3'

    assert Test2.prop == 'prop'
    assert Test2.prop2 == 'prop'

# Generated at 2022-06-14 06:40:36.898496
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:40:41.557070
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test:
        @lazyclassproperty
        def prop(cls):
            return 'test'

    print(Test.prop)
    print(Test.prop)

    Test2 = type('Test2', (Test,), {})
    print(Test2.prop)



# Generated at 2022-06-14 06:40:48.902553
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # BaseClass
    class BaseClass(object):
        @lazyclassproperty
        def prop(cls):  # should raise error when called with BaseClass
            return 'BaseClass'

        @lazyclassproperty
        def prop2(cls):  # should return 1 when called with BaseClass
            return cls.prop

    # First inheritor
    class First(BaseClass):
        @lazyclassproperty
        def prop(cls):  # should return First when called with First
            return cls.__name__

    # Test everything
    assert BaseClass.prop == 'BaseClass'

    assert BaseClass.prop2 == 'BaseClass'
    assert First.prop2 == 'First'


if __name__ == '__main__':
    test_lazyperclassproperty()

# Generated at 2022-06-14 06:40:56.528189
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    
    class A(object):
        @lazyperclassproperty
        def value(cls):
            print(cls.__name__)
            return cls.__name__

    class B(A):
        pass

    class C(B):
        pass

    assert A.value == "A"
    assert B.value == "B"
    assert C.value == "C"
    print("Test passed")


# Generated at 2022-06-14 06:41:02.375514
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def a(cls):
            print('Executed A.a')
            return []

    class B(A):
        pass

    a = A()
    b = B()
    a.a.append(1)
    b.a.append(2)
    a.a.append(3)
    b.a.append(4)
    assert a.a == [1, 3]
    assert b.a == [2, 4]



# Generated at 2022-06-14 06:41:08.416485
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def lazy_prop(self):
            return 'A'

    class B(A):
        @lazyperclassproperty
        def lazy_prop(self):
            return 'B'

    assert A.lazy_prop == 'A'
    assert B.lazy_prop == 'B'


# Generated at 2022-06-14 06:41:15.721372
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print('Calculating foo')
            return 42

    print(A.foo)
    print(A.foo)

    print(A().foo)
    print(A().foo)


if __name__ == '__main__':
    test_lazyclassproperty()

# Generated at 2022-06-14 06:41:29.170982
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    print(lazyperclassproperty.__doc__)
    class Foo(object):
        i = 1
        def __init__(self, i):
            self.__i = i
        @lazyperclassproperty
        def j(cls):
            print('lazyperclassproperty in %s' % cls.__name__)
            return cls.i + 10
        @lazyclassproperty
        def k(cls):
            print('lazyclassproperty in %s' % cls.__name__)
            return cls.i + 20
        @lazyperclassproperty
        def l(cls):
            print('lazyperclassproperty in %s' % cls.__name__)
            return cls.i + 30
        @lazyperclassproperty
        def m(cls):
            print

# Generated at 2022-06-14 06:41:53.948658
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestCls(object):
        @lazyclassproperty
        def lazyint(cls):
            return 5
        def __init__(self): self.lazyint = 5

    testobj = TestCls()

    assert(TestCls.lazyint.__doc__ is None)
    assert(TestCls.__dict__['_lazy_lazyint'].__doc__ is None)

    testobj = TestCls()
    assert(testobj.lazyint == 5)



# Generated at 2022-06-14 06:42:03.090375
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self, n):
            self.n = n

        @lazyperclassproperty
        def a(cls):
            return cls.n

    class B(A): pass
    class C(A): pass

    a = A(1)
    b = B(2)
    c = C(3)

    assert a.a == 1
    assert b.a == 2
    assert c.a == 3

    b.n = 4
    assert b.a == 2

# Generated at 2022-06-14 06:42:15.828691
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop1(cls):
            print('calculating lazyclassprop for A.prop1')
            return 'test'

        @lazyclassproperty
        def prop2(cls):
            print('calculating lazyclassprop for A.prop2')
            return 'test2'

        @lazyclassproperty
        def prop3(cls):
            print('calculating lazyclassprop for A.prop3')
            lst = []
            for i in range(1, 5):
                lst.append(str(i))
            return lst

    class B(A):
        pass

    assert A.prop1 == "test"
    assert A.prop2 == "test2"

# Generated at 2022-06-14 06:42:21.474506
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 1
    f = Foo()
    assert (Foo.bar, f.bar) == (1, 1)
    Foo.bar = 2
    assert (Foo.bar, f.bar) == (2, 2)



# Generated at 2022-06-14 06:42:31.590070
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    import unittest
    from unittest.mock import patch

    class TestClass1(object):
        @lazyclassproperty
        def lazy_property(cls):
            return 'lazy property for TestClass1'

    class TestClass2(object):
        @lazyclassproperty
        def lazy_property(cls):
            return 'lazy property for TestClass2'

    class TestLazyClassProperty(unittest.TestCase):
        def test_lazyclassproperty(self):
            with patch('lib.utils.lazyclassproperty._lazyclassprop',
                       new_callable=lazyclassproperty(lambda cls: 'class property')):
                self.assertEqual(TestClass1.lazy_property, 'class property')

# Generated at 2022-06-14 06:42:42.222524
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop(cls):
            return 'Class A'

    class B(A):
        @lazyperclassproperty
        def prop(cls):
            return 'Class B'

    class C(A):
        @lazyperclassproperty
        def prop(cls):
            return 'Class C'

    assert A.prop == 'Class A'
    assert B.prop == 'Class B'
    assert C.prop == 'Class C'

    assert A().prop == 'Class A'
    assert B().prop == 'Class B'
    assert C().prop == 'Class C'

# Generated at 2022-06-14 06:42:47.566183
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Blah(object):
        @lazyclassproperty
        def a(cls):
            return 10
    
    class Blah2(Blah): pass
    
    assert Blah.a == 10
    assert Blah2.a == 10

    Blah.a = 20
    assert Blah.a == 20
    assert Blah2.a == 20


# Generated at 2022-06-14 06:42:52.290228
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        test = 1
        @lazyclassproperty
        def prop(cls):
            return cls.test

    assert Test.prop == 1
    Test.test = 2
    # On second call, the previously stored value is returned
    assert Test.prop == 1


# Generated at 2022-06-14 06:42:56.549967
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A:
        @lazyclassproperty
        def prop(cls):
            print("Executing method")
            return 'result'

    assert A.prop == 'result'
    assert A.prop == 'result'



# Generated at 2022-06-14 06:43:05.791312
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            print('A.a')
            return 10

        @lazyperclassproperty
        def b(cls):
            print('A.b')
            return 10

    class B(A):
        @lazyperclassproperty
        def c(cls):
            print('B.c')
            return 10

        @lazyperclassproperty
        def b(cls):
            print('B.b')
            return 10

    class C(A):
        @lazyperclassproperty
        def c(cls):
            print('C.c')
            return 10

    assert A.a == 10
    assert B.a == 10
    assert C.a == 10
    assert A.b == 10

# Generated at 2022-06-14 06:43:45.874023
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:43:52.233619
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C:
        def __init__(self, attr):
            self.attr = attr

        @lazyclassproperty
        def value(cls):
            """ The value of the attribute """
            return cls.attr

        @value.setter
        def value(cls, value):
            """ Set the value of the attribute """
            cls.attr = value

    a = C(2)
    b = C(3)

# Generated at 2022-06-14 06:44:00.128939
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:44:03.477038
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            return 'bar'

    assert A.foo == 'bar'



# Generated at 2022-06-14 06:44:09.481771
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return "bar"

    class B(A):
        pass

    class C(B):
        pass

    assert A.foo == B.foo == C.foo == "bar"

    A.foo = "baz"

    assert A.foo == "baz"
    assert B.foo == "bar"
    assert C.foo == "bar"



# Generated at 2022-06-14 06:44:22.786769
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:44:26.291976
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:44:35.805128
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:44:41.987307
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def fn(cls):
            return "I'm lazy"

    assert Foo.fn == "I'm lazy"
    assert Foo.fn == "I'm lazy"
    assert Foo.fn == "I'm lazy"

    class Bar(Foo):
        pass

    assert Bar.fn == "I'm lazy"
    assert Bar.fn == "I'm lazy"
    assert Bar.fn == "I'm lazy"

# Generated at 2022-06-14 06:44:48.656496
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def bigdata(cls):
            return cls.__name__.lower()

    class B(A):
        pass

    assert A.bigdata == "a"
    assert B.bigdata == "b"

    A.bigdata = "A modified"

    assert A.bigdata == "A modified"
    assert B.bigdata == "b"

