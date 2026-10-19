

# Generated at 2022-06-14 06:35:43.964982
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:35:49.519190
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop(cls):
            return cls.__name__

    class B(A):
        pass

    class C(A):
        pass

    assert A.prop == 'A'
    assert B.prop == 'B'
    assert C.prop == 'C'



# Generated at 2022-06-14 06:35:55.844115
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        @lazyclassproperty
        def message(cls):
            return 'Hello World!'

    assert MyClass.message is MyClass.message # assert same object
    assert MyClass.message != MyClass.message # assert different object
    assert MyClass.message.upper() == 'HELLO WORLD!'


# Generated at 2022-06-14 06:36:03.652267
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Unit test for function lazyclassproperty
    """

    class Test(object):

        @lazyclassproperty
        def foo(self):
            return "this is foo property"

        @lazyclassproperty
        def bar(self):
            return "this is bar property"

        def print_foo(self):
            print(self.foo)

    print(Test.foo, Test.bar)

    test = Test()
    test.print_foo()



# Generated at 2022-06-14 06:36:17.327322
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Foo(object):

        @lazyperclassproperty
        def prop(cls):
            return cls.__name__

    class Bar(Foo):
        pass

    class Baz(Foo):
        pass

    assert Foo.prop == 'Foo'
    assert Bar.prop == 'Bar'
    assert Baz.prop == 'Baz'
    assert Foo.__dict__['_Foo_lazy_prop'] == 'Foo'
    assert Bar.__dict__['_Bar_lazy_prop'] == 'Bar'
    assert Baz.__dict__['_Baz_lazy_prop'] == 'Baz'
    assert 'prop' not in Foo.__dict__
    assert 'prop' not in Bar.__dict__
    assert 'prop' not in Baz.__dict__


# Generated at 2022-06-14 06:36:26.596556
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:36:36.739070
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base:
        @lazyperclassproperty
        def a(cls):
            return "from Base"

        @lazyperclassproperty
        def b(cls):
            return "from Base"

    class Derived(Base):
        pass

    assert Base.a == "from Base"
    assert Base.b == "from Base"
    assert Derived.a == "from Base"
    assert Derived.b == "from Base"
    assert Base.a == "from Base"
    assert Base.b == "from Base"
    assert Derived.a == "from Base"
    assert Derived.b == "from Base"



# Generated at 2022-06-14 06:36:44.786991
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self):
            self.counter = 0

        def __repr__(self):
            return 'A class instance'

        @lazyperclassproperty
        def a(cls):
            print("Creating A class instance")
            return A()

    class B(A):
        pass

    class C(A):
        pass

    a = A()
    b = B()
    c = C()

    assert A.a is not B.a
    assert A.a is not C.a
    assert B.a is C.a


# Generated at 2022-06-14 06:36:56.312260
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Test the correct behavior of lazyclassproperty.
    """
    class Foo(object):
        foo = "A"
        def get_foo(cls):
            return cls.foo
        lazy_foo = lazyclassproperty(get_foo)

    class Bar(Foo):
        foo = "B"

    class Qaz(Foo):
        foo = "C"

    assert Foo.lazy_foo == "A", "Foo.lazy_foo should return 'A'. Got {0} instead.".format(Foo.lazy_foo)
    assert Bar.lazy_foo == "B", "Bar.lazy_foo should return 'B'. Got {0} instead.".format(Bar.lazy_foo)

# Generated at 2022-06-14 06:37:03.549343
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(self):
            return 'foo'

        @lazyclassproperty
        def y(self):
            return 'foo'

    class B(A):
        pass

    assert A.x == B.x
    assert A.y == B.y
    assert A.x != B.y
    assert A.y != B.x



# Generated at 2022-06-14 06:37:08.878774
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass:
        @lazyclassproperty
        def a(cls):
            return 1

    assert hasattr(MyClass, '_lazy_a') is False
    assert MyClass.a == 1
    assert hasattr(MyClass, '_lazy_a') is True



# Generated at 2022-06-14 06:37:13.114867
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Test:
        @lazyperclassproperty
        def test(cls):
            return dict()

    class Test2(Test):
        pass

    assert Test.test is Test.test
    assert Test.test is not Test2.test



# Generated at 2022-06-14 06:37:19.254649
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 'foo'

    class B(A):
        pass

    assert A.prop == 'foo'
    assert B.prop == 'foo'
    A.prop = 'bar'
    assert A.prop == 'bar'
    assert B.prop == 'foo'



# Generated at 2022-06-14 06:37:23.592445
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        @lazyclassproperty
        def foo(cls):
            return 'bar'

    assert A.foo() == 'bar'
    assert A().foo == 'bar'



# Generated at 2022-06-14 06:37:30.123182
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self):
            self.value = 0

        @lazyclassproperty
        def value_prop(cls):
            return cls.value

    class B(A):
        def __init__(self):
            super(B, self).__init__()
            self.value = 1

    assert A.value_prop == 0
    assert B.value_prop == 1



# Generated at 2022-06-14 06:37:36.769325
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test:
        @lazyclassproperty
        def prop1(cls):
            print('eval')
            return 'prop1'

        @lazyclassproperty
        def prop2(cls):
            print('eval')
            return 'prop2'

    assert Test.prop1 == 'prop1'
    assert Test.prop2 == 'prop2'


# Generated at 2022-06-14 06:37:43.121354
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def f(cls):
            return 1
    class B(A):
        pass
    class C(A):
        @lazyperclassproperty
        def f(cls):
            return super(C,cls).f
    
    assert A.f == 1
    assert B.f == 1
    assert C.f == 1


# Generated at 2022-06-14 06:37:56.195631
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        def __init__(self):
            self._x = None

        @lazyperclassproperty
        def x(cls):
            return 'x'

        @staticmethod
        def get_x(self):
            return self._x

        @staticmethod
        def set_x(self, value):
            self._x = value

        x = property(get_x, set_x)

    class A(Base):
        pass

    class B(Base):
        pass

    a = A()
    b = B()

    assert a.x == 'x'
    assert b.x == 'x'

    assert a.__dict__.get('_x') is not 'x'
    assert b.__dict__.get('_x') is not 'x'


# Generated at 2022-06-14 06:38:04.724087
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    import unittest
    import pickle

    class TestLCP(unittest.TestCase):
        def test_simple(self):
            class A:
                @lazyclassproperty
                def x(cls):
                    return 5

            self.assertEqual(A.x, 5)
            self.assertEqual(A().x, 5)
            A.x = 12
            self.assertEqual(A.x, 12)
            self.assertEqual(A().x, 12)

        def test_empty(self):
            class A:
                pass

            A.x = lazyclassproperty(lambda: 5)
            self.assertEqual(A.x, 5)
            self.assertEqual(A().x, 5)


# Generated at 2022-06-14 06:38:07.119184
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def a(cls):
            return 1

    assert Test.a == 1
    assert Test.a == 1

    Test.a = 2
    assert Test.a == 2


# Generated at 2022-06-14 06:38:13.942264
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def Bar(cls):
            return 1

    assert Foo.Bar == 1


# Generated at 2022-06-14 06:38:21.024252
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A: pass
    class B(A): pass

    @lazyperclassproperty
    def foo(cls):
        return object()

    a1 = A()
    a2 = A()
    assert a1.foo is a2.foo

    b1 = B()
    b2 = B()
    assert b1.foo is b2.foo

    assert a1.foo is not b1.foo



# Generated at 2022-06-14 06:38:29.030988
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    >>> class Test(object):
    ...     @lazyclassproperty
    ...     def attr(cls):
    ...         print "Computing"
    ...         return 1
    ...
    >>> Test.attr
    Computing
    1
    >>> Test.attr
    1
    >>> class Test2(Test):
    ...     pass
    ...
    >>> Test2.attr
    Computing
    1

    """


# Generated at 2022-06-14 06:38:37.062476
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 1

    class B(A):
        pass

    # The lazyclassproperty is shared among objects of the same class
    assert A().a == 1
    assert B().a == 1
    A.a = 2
    assert A().a == 2
    assert B().a == 2

    # The lazyclassproperty is independent among objects of different classes
    class C(object):
        @lazyclassproperty
        def a(cls):
            return 3

    assert A().a == 2
    assert B().a == 2
    assert C().a == 3
    C.a = 4
    assert A().a == 2
    assert B().a == 2
    assert C().a == 4



# Generated at 2022-06-14 06:38:47.626146
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass(object):
        def __init__(self, name):
            self.name = name


# Generated at 2022-06-14 06:38:58.095726
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self, name):
            self.name = name
        @lazyclassproperty
        def message(cls):
            return 'hi from %s' % cls.__name__

    class B(A): pass
    a = A('foo')
    b = B('bar')
    assert a.message == 'hi from A'
    assert b.message == 'hi from B'
    # this should not have affected the class property
    a.message = 'hello'
    assert a.message == 'hello'
    assert b.message == 'hi from B'



# Generated at 2022-06-14 06:39:03.561933
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 1
    class B(A):
        pass
    assert(A.a == 1 and B.a == 1)
    A.a = 2
    assert(A.a == 2 and B.a == 1)




# Generated at 2022-06-14 06:39:10.132771
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 'baz'

    print(Foo.bar)
    # baz
    print(Foo.__dict__['bar'])
    # <property object at 0x7f0b324d8e58>

# Generated at 2022-06-14 06:39:22.159638
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # Test class
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return cls.__name__ + '-foo'

        @lazyperclassproperty
        def bar(cls):
            return cls.__name__ + '-bar'

        def get_foo(self):
            return self.__class__.foo

        def get_bar(self):
            return self.__class__.bar

    # Test class
    class B(A):
        @lazyperclassproperty
        def foo(cls):
            return cls.__name__ + '-foo'

        @lazyperclassproperty
        def bar(cls):
            return cls.__name__ + '-bar'


# Generated at 2022-06-14 06:39:27.449715
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return id(cls)

    class B(A):
        pass

    assert B.foo != A.foo
    assert A.foo == id(A)
    assert B.foo == id(B)



# Generated at 2022-06-14 06:39:41.183217
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        @lazyclassproperty
        def test(cls):
            return 'test'

    class B(A):
        pass

    class C(B):
        pass

    assert A.test == 'test'
    assert B.test == 'test'
    assert C.test == 'test'
    assert A.test == B.test
    assert A.test == C.test
    assert B.test == C.test



# Generated at 2022-06-14 06:39:47.329397
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Parent(object):
        @lazyperclassproperty
        def value(cls):
            return 1

    class Child(Parent):
        @lazyperclassproperty
        def value(cls):
            return 2

    p = Parent()
    c = Child()
    assert p.value == 1
    assert c.value == 2



# Generated at 2022-06-14 06:39:51.156186
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def b(cls):
            return [1]

    class B(A):
        pass

    assert A.b is B.b
    assert A.b is not B.b
    assert B.b is not A.b

# Generated at 2022-06-14 06:39:53.812845
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def value(cls):
            print('calculating value')
            return 10

    print(A.value)
    print(A.value)



# Generated at 2022-06-14 06:40:01.524510
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        pass

    class Bar(Foo):
        pass

    def f(cls):
        return len(cls.__name__)

    Foo.lazyprop = lazyclassproperty(f)

    # check that both objects of the same class as well as of different classes
    # share the same value
    assert Foo.lazyprop == 3
    assert Bar.lazyprop == 3

    # check that we get the value from the cache
    def g(cls):
        return -1

    Foo.lazyprop = lazyclassproperty(g)
    assert Foo.lazyprop == 3

    # check that we get the value from the cache if we don't set in to the class
    # but set it to the object
    foobar = Foo()
    foobar.lazyprop = 5

# Generated at 2022-06-14 06:40:07.002530
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            return cls
        foo._doc = "foo docstring"
    cls = A.foo
    assert cls is A
    assert A.__dict__.get('_lazy_foo') is cls
    assert A.foo._doc == "foo docstring"



# Generated at 2022-06-14 06:40:17.367635
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class TestClass(object):
        def __init__(self, a):
            self.a = a

        @lazyclassproperty
        def test_lazyclassmethod(cls):
            print("In TestClass.test_lazyclassmethod")
            return lambda x: x

    class TestSubclass(TestClass):
        pass

    t = TestClass(5)
    t.test_lazyclassmethod
    t.test_lazyclassmethod
    t.test_lazyclassmethod
    t.test_lazyclassmethod

    ts = TestSubclass(5)
    ts.test_lazyclassmethod
    ts.test_lazyclassmethod
    ts.test_lazyclassmethod
    ts.test_lazyclassmethod

    assert t.__class__ == TestClass

# Generated at 2022-06-14 06:40:20.445912
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Parent(object):
        @lazyperclassproperty
        def prop(cls):
            print("Parent:prop")
            return 1

    class Child(Parent):
        pass

    assert Parent.prop == 1
    assert Child.prop == 1



# Generated at 2022-06-14 06:40:23.210968
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return id(cls)

    class B(A):
        pass

    class C(A):
        pass

    assert A.x != B.x != C.x

# Generated at 2022-06-14 06:40:28.296500
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:40:49.961872
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            print('called')
            return 'something'

    assert Foo.bar == 'something'

    class Bar(Foo):
        pass

    assert Bar.bar == 'something'



# Generated at 2022-06-14 06:40:58.587845
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:11.180323
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def test(cls):
            return 5

    class Subclass(Base):
        pass

    assert Subclass.test == Base.test
    assert Subclass.test != 6
    assert Subclass.test != 5

    Base.test = 6

    assert Subclass.test == 5

    Subclass.test = 7

    assert Base.test == 6

    # Since the property is lazy, it should not be copied to the subclass
    assert not hasattr(Base, '_%s_lazy_test' % Subclass.__name__)
    assert hasattr(Base, '_Base_lazy_test')
    assert hasattr(Subclass, '_Subclass_lazy_test')



# Generated at 2022-06-14 06:41:21.762711
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def foo(cls):
            print("creating foo")
            return "foo"

    class B(A):
        pass

    class C(B):
        pass

    a1 = A()
    a2 = A()
    print(a1.foo)
    print(a2.foo)

    b1 = B()
    b2 = B()
    print(b1.foo)
    print(b2.foo)

    c1 = C()
    c2 = C()
    print(c1.foo)
    print(c2.foo)

    b1.foo = "bar"
    print(b1.foo)
    print(b2.foo)
    print(c1.foo)
    print(c2.foo)

    c

# Generated at 2022-06-14 06:41:29.556268
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def a(cls):
            return 1
    C.a = 2
    assert C.a == 2
    assert C().a == 2
    class C(C):
        pass
        # Cannot test it because a is already there
    # assert C.a == 1
    # assert C().a == 1
    del C.a
    assert C.a == 1
    assert C().a == 1


# Generated at 2022-06-14 06:41:40.902224
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop1(cls):
            return 'A'

    class B(A):
        pass

    assert A.prop1 == 'A'
    assert B.prop1 == 'A'  # A.prop1 and B.prop1 are different instances

    class C(A):
        @lazyperclassproperty
        def prop1(cls):
            return 'C'

    assert A.prop1 == 'A'
    assert B.prop1 == 'A'
    assert C.prop1 == 'C'

    class D(B, C):
        pass

    assert A.prop1 == 'A'
    assert B.prop1 == 'A'
    assert C.prop1 == 'C'
    assert D.prop1 == 'C'

# Generated at 2022-06-14 06:41:49.100628
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def name(cls):
            return 'base_' + str(cls.__name__)

    class A(Base):
        pass

    class B(Base):
        pass

    assert Base._lazyclassprop
    assert not Base.name
    assert A._lazyclassprop
    assert A._A_lazy_name
    assert A.name
    assert B._lazyclassprop
    assert B._B_lazy_name
    assert B.name



# Generated at 2022-06-14 06:41:58.740718
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def c(cls):
            print("Calculating c")
            return 1

        @lazyperclassproperty
        def d(cls):
            print("Calculating d")
            return 2

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        @lazyperclassproperty
        def d(cls):
            print("Calculating d")
            return 3

    class E(C):
        pass


# Generated at 2022-06-14 06:42:01.606034
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def attribute(cls):
            return cls
    assert A.attribute is A



# Generated at 2022-06-14 06:42:07.071868
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def Foo(cls):
            return 'foo'

    assert Test.Foo == 'foo'
    assert Test.Foo == 'foo'
    assert Test.Foo == 'foo'
    assert Test.Foo == 'foo'



# Generated at 2022-06-14 06:42:51.254721
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    def myfunc(cls):
        return {
            'cls': cls,
            'func': myfunc
        }

    class Base(object):
        @lazyperclassproperty
        def my_property(cls):
            return myfunc(cls)

    class SubOne(Base):
        pass

    class SubTwo(Base):
        pass

    assert Base.my_property['cls'] == Base
    assert Base.my_property['func'] == myfunc
    assert SubOne.my_property['cls'] == SubOne
    assert SubOne.my_property['func'] == myfunc
    assert SubTwo.my_property['cls'] == SubTwo
    assert SubTwo.my_property['func'] == myfunc
    assert Base.my_property is Base.my_property
    assert SubOne.my_

# Generated at 2022-06-14 06:43:02.187511
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    import types

    class A(object):
        # This works
        @lazyclassproperty
        def prop(cls):
            return 1

    class B(object):
        # This works
        @lazyclassproperty
        def prop(cls):
            return 2

    assert not hasattr(A, '_lazy_prop')
    assert not hasattr(B, '_lazy_prop')

    assert A.prop == 1
    assert B.prop == 2

    assert hasattr(A, '_lazy_prop')
    assert hasattr(B, '_lazy_prop')

    assert A._lazy_prop == 1
    assert B._lazy_prop == 2

    assert isinstance(A.__dict__['prop'], types.FunctionType)

# Generated at 2022-06-14 06:43:12.644895
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:43:20.392207
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base:
        def __init__(self):
            self.a = 1

        @lazyperclassproperty
        def prop(self):
            return self.a

    class Derived(Base):
        def __init__(self):
            super(Derived, self).__init__()
            self.a = 2

    b = Base()
    assert(not hasattr(Base, '_Base_lazy_prop'))
    assert(b.prop == 1)
    assert(hasattr(Base, '_Base_lazy_prop'))

    d = Derived()
    assert(not hasattr(Derived, '_Derived_lazy_prop'))
    assert(d.prop == 2)
    assert(hasattr(Derived, '_Derived_lazy_prop'))


# Generated at 2022-06-14 06:43:25.017299
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            print('a')
            return 'a'

    class B(A):
        @lazyclassproperty
        def b(cls):
            print('b')
            return 'b'

    assert A.a == 'a'
    assert B.a == 'a'
    assert B.b == 'b'



# Generated at 2022-06-14 06:43:34.591508
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        def __init__(self):
            self._stack = []

        def method_1(self):
            self._stack.append(1)
            return 1

        @lazyclassproperty
        def method_2(cls):
            return 2

        @lazyclassproperty
        def method_3(cls):
            return 3

        @lazyclassproperty
        def method_4(cls):
            return cls.method_3()

    @lazyclassproperty
    def method_5(cls):
        return 5

    foo = Foo()
    assert foo._stack == []
    assert foo.method_1() == 1
    assert foo._stack == [1]
    assert foo.method_1() == 1
    assert foo._stack == [1]

    assert Foo.method_2

# Generated at 2022-06-14 06:43:39.868404
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return cls.__name__

    class B(A):
        pass

    assert A.prop == 'A'
    assert B.prop == 'B'



# Generated at 2022-06-14 06:43:53.590566
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        @lazyperclassproperty
        def bar(cls):
            return [1,2]

        @classproperty
        def baz(cls):
            return [3,4]

    class Bar(Foo):
        pass

    assert Foo.baz is not Bar.baz

    assert Foo.bar is not Bar.bar
    assert Foo.bar == [1, 2]
    assert Bar.bar == [1, 2]
    assert Foo.bar is not Bar.bar

    # Modification test
    Foo.bar.append(3)
    assert Bar.bar == [1, 2, 3]
    Bar.bar.append(4)
    assert Bar.bar == [1, 2, 3, 4]
    assert Foo.bar == [1, 2, 3]


# Generated at 2022-06-14 06:43:59.595129
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:44:07.400936
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 'Hi'

    class B(A):
        pass

    class C(A):
        @lazyclassproperty
        def a(cls):
            return 'Hello'

    class D(C):
        pass

    assert A.a == 'Hi'
    assert B.a == 'Hi'
    assert C.a == 'Hello'
    assert D.a == 'Hello'

