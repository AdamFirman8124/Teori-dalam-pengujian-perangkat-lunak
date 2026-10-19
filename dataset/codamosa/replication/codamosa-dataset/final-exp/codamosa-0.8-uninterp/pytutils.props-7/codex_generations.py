

# Generated at 2022-06-14 06:35:41.551614
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class LazyClass(object):
        @lazyclassproperty
        def foo(cls):
            return cls.__name__

    assert LazyClass.foo == 'LazyClass'



# Generated at 2022-06-14 06:35:48.085764
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class C(object):
        @lazyperclassproperty
        def x(cls):
            return 'x'

    class D(C):
        pass

    class E(C):
        pass

    assert C.x == 'x'
    assert D.x == 'x'
    assert E.x == 'x'
    assert C.x is not D.x
    assert C.x is not E.x
    assert D.x is not E.x



# Generated at 2022-06-14 06:35:58.178646
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Cls(object):
        def __init__(self):
            self.n = 0

        @lazyclassproperty
        def f(cls):
            cls.n += 1
            print(cls.n)
            return 2

    cls1 = Cls()
    cls2 = Cls()

    # First call will call the function
    assert cls1.f == 2
    # Second call will use the cached value
    assert cls1.f == 2
    # Third call will use the cached value
    assert cls2.f == 2


# Generated at 2022-06-14 06:36:03.636828
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return pow(2, 3)

    assert A.prop == 8

    assert A.__dict__['_lazy_prop'] == 8
    # Should not re-evaluate when accessing the same property
    assert A.__dict__['_lazy_prop'] == A.prop

    # Should not re-evaluate when accessing the same property again
    assert A.__dict__['_lazy_prop'] == A.prop

    class B(A):
        pass

    assert B.prop == 8



# Generated at 2022-06-14 06:36:13.106394
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def hungry(cls):
            return 'open mouth'

    class B(A):
        pass

    assert A.hungry == 'open mouth'
    assert B.hungry == 'open mouth'
    A.hungry = 'eating'
    assert A.hungry == 'eating'
    assert B.hungry == 'open mouth'
    B.hungry = 'full'
    assert A.hungry == 'eating'
    assert B.hungry == 'full'



# Generated at 2022-06-14 06:36:20.646438
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    def get_value(cls):
        return cls.__name__

    class A():
        lazy_value = lazyclassproperty(get_value)

    class B(A):
        pass

    class C(B):
        pass

    assert A.lazy_value == 'A'
    assert B.lazy_value == 'B'
    assert C.lazy_value == 'C'



# Generated at 2022-06-14 06:36:22.597495
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def x(cls):
            return 1
    assert C.x == 1



# Generated at 2022-06-14 06:36:35.942136
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A():
        @lazyperclassproperty
        def test_lazy_per_class(cls):
            print("A.test_lazy_per_class")
            return 1

    class B(A):
        @lazyperclassproperty
        def test_lazy_per_class(cls):
            print("B.test_lazy_per_class")
            return 2

    class C(A):
        @lazyperclassproperty
        def test_lazy_per_class(cls):
            print("C.test_lazy_per_class")
            return 3

    class D(B, C):
        @lazyperclassproperty
        def test_lazy_per_class(cls):
            print("D.test_lazy_per_class")
            return 4


# Generated at 2022-06-14 06:36:42.011053
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def test(cls):
            print ("test called")
            return "value"

    # test called
    print (A.test)
    # value
    print (A.test)
    # value
    print (A.test)


########################################
# Bunch, from Alex Martelli's Python Cookbook



# Generated at 2022-06-14 06:36:46.998382
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        l = lazyclassproperty(lambda c: len(c.__mro__))

    class D(C):
        pass

    assert C.l == 2
    assert D.l == 2



# Generated at 2022-06-14 06:36:56.232396
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        counter = 0
        @lazyperclassproperty
        def incc(cls):
            cls.counter += 1
            return cls.counter


    class B(A):
        pass

    class C(A):
        pass

    assert A.incc == 1
    assert B.incc == 2
    assert C.incc == 3
    assert A.incc == 1
    assert B.incc == 2
    assert C.incc == 3



# Generated at 2022-06-14 06:37:05.455973
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Base:
        def __init__(self):
            self._x = None

        @lazyperclassproperty
        def x(cls):
            x = cls._x
            if x is None:
                x = cls._x = []
            return x

    class Derived(Base):
        def __init__(self):
            Base.__init__(self)
            self._y = None

        @lazyperclassproperty
        def y(cls):
            y = cls._y
            if y is None:
                y = cls._y = []
            return y

    d = Derived()
    d.x.append(42)
    d.y.append(42)
    assert d.x == [42]
    assert d.y == [42]
    b = Base()
   

# Generated at 2022-06-14 06:37:11.467629
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def b(self):
            return A.B
        B = lazyperclassproperty(b)

    class C(A):
        def d(self):
            return C.D
        D = lazyperclassproperty(d)

    A_Instance = A()
    C_Instance = C()

    assert A_Instance.b is A.B
    assert A_Instance.B is A.B

    assert C_Instance.b is C.B
    assert C_Instance.B is C.B

    assert C_Instance.d is C.D
    assert C_Instance.D is C.D

    assert A_Instance.d is None
    assert A_Instance.D is None


# Generated at 2022-06-14 06:37:24.662356
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return 'foo'

        @lazyperclassproperty
        def bar(cls):
            return 'bar'

    class B(A):
        pass

    assert A.foo == 'foo'
    assert 'foo' not in B.__dict__
    assert B.foo == 'foo'
    assert hasattr(B, '_B_lazy_foo')
    assert B.bar == 'bar'
    assert hasattr(B, '_B_lazy_bar')
    assert 'bar' not in A.__dict__

    class C(B):
        pass

    assert C.foo == 'foo'
    assert hasattr(C, '_C_lazy_foo')
    assert C.bar == 'bar'
   

# Generated at 2022-06-14 06:37:36.209916
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:37:45.436774
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self, x):
            self.x = x

        @lazyperclassproperty
        def f(cls):
            print(cls, 'called')
            return 1

    class B(A):
        pass

    a = A(1)
    a2 = A(2)
    b = B(3)

    assert a.f == 1
    assert a.f == 1
    assert b.f == 1
    assert b.f == 1
    assert a2.f == 1
    assert a2.f == 1
    assert a2.f == a.f
    assert b.f != a2.f



# Generated at 2022-06-14 06:37:51.346386
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def f(cls):
            return 1

    class B(A):
        pass

    class C(A):
        @lazyclassproperty
        def f(cls):
            return 2

    assert A.f == 1
    assert B.f == 1
    assert C.f == 2


# Generated at 2022-06-14 06:38:03.157372
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            return 1

        @lazyclassproperty
        def y(cls):
            return 2

    # Check that separate instances of the class have separate properties
    class B(A):
        pass

    assert A.x == 1
    assert B.x == 1

    assert A.y == 2
    assert B.y == 2

    # Check that the lazy property is calculated only once
    class A(object):
        def ___init__(self):
            pass

        @lazyclassproperty
        def x(cls):
            cls.x = cls.x + 1
            return cls.x

        x = 0

    A()
    assert A.x == 1
    A()
    assert A.x == 1
    A()


# Generated at 2022-06-14 06:38:09.151040
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    How to use lazy class property
    """
    class A:
        @lazyclassproperty
        def f(cls):
            print('Calculating')
            return 1
    a = A()
    b = A()
    assert a.f == 1
    assert b.f == 1
    assert A.f == 1
    assert a.f == 1



# Generated at 2022-06-14 06:38:15.295119
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A():
        @lazyclassproperty
        def foo(cls):
            return 'foo'

    assert A.foo == 'foo'
    assert A.foo == 'foo' # memoized

    class B(A):
        pass

    assert B.foo == 'foo'
    assert B.foo == 'foo' # memoized
    assert A.foo == 'foo'
    assert A.foo == 'foo' # memoized


# Generated at 2022-06-14 06:38:26.640704
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return 42

    class B(A):
        pass

    class C(A):
        pass

    a = A()
    a.x  # This is A's _lazy_x
    b = B()
    b.x  # This is B's _lazy_x

    b.x = 100
    a.x
    b.x
    C.x

# Generated at 2022-06-14 06:38:34.742951
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class FooClass(object):
        call_count = 0

        @lazyclassproperty
        def foo(cls):
            cls.call_count += 1
            return 'foo'

    assert FooClass.call_count == 0
    assert FooClass.foo == 'foo'
    assert FooClass.call_count == 1
    try:
        del FooClass.foo
    except AttributeError:
        pass
    else:
        assert False, 'cannot delete FooClass.foo'
    assert FooClass.foo == 'foo'
    assert FooClass.call_count == 2



# Generated at 2022-06-14 06:38:38.149587
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        num = 1

        @lazyclassproperty
        def get_num(cls):
            return cls.num + 1

    x = A()
    assert x.get_num == 2
    # Modification to class shouldn't affect the result
    A.num += 1
    assert x.get_num == 2



# Generated at 2022-06-14 06:38:50.021339
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Unit test for function lazyclassproperty.
    """
    class _TestA(object):

        @lazyclassproperty
        def _testprop(cls):
            return cls.__name__

    assert '_TestA' == _TestA._testprop
    _TestA._testprop = '_testprop_value'
    assert _TestA._testprop == '_testprop_value'

    class _TestB(_TestA):
        pass

    assert _TestA._testprop == '_testprop_value'
    assert _TestB._testprop == '_TestB'
    _TestB._testprop = '_testprop_value_B'
    assert _TestA._testprop == '_testprop_value'
    assert _TestB._testprop == '_testprop_value_B'




# Generated at 2022-06-14 06:38:55.969033
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:01.313159
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class TestClass(object):
        @lazyperclassproperty
        def x(clazz):
            return "x from class %s" % clazz.__name__

    class DerivedTestClass(TestClass):
        pass

    class AnotherTestClass(object):
        @lazyperclassproperty
        def x(clazz):
            return "x from class %s" % clazz.__name__

    assert TestClass.x == "x from class TestClass"
    assert DerivedTestClass.x == "x from class DerivedTestClass"
    assert AnotherTestClass.x == "x from class AnotherTestClass"

# Generated at 2022-06-14 06:39:06.368941
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        def __init__(self):
            self.i = 0

        @lazyclassproperty
        def bar(cls):
            return cls.i + 1

    assert Foo.bar == 1
    Foo.i = 1
    assert Foo.bar == 2
    Foo.i = 5
    assert Foo.bar == 5



# Generated at 2022-06-14 06:39:15.531014
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def func(cls):
            print('called A')
            return 'a'

    class D(C):
        @lazyclassproperty
        def func(cls):
            print('called B')
            return 'b'

    assert C.func == 'a'
    assert C.func == 'a'

    assert D.func == 'b'
    assert D.func == 'b'

    assert C.func == 'a'
    assert C.func == 'a'



# Generated at 2022-06-14 06:39:24.187146
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        @lazyperclassproperty
        def x(cls):
            return 'x'

    f = Foo()
    assert f.x == 'x'
    assert f.__class__.x == 'x'

    class Foo2(Foo):
        @lazyperclassproperty
        def x(cls):
            return 'x2'

    f = Foo2()
    assert f.x == 'x'
    assert f.__class__.x == 'x2'



# Generated at 2022-06-14 06:39:34.633021
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:49.439448
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    >>> @lazyclassproperty
    ... def fullname(self):
    ...     return self.__module__ + '.' + self.__name__
    ...
    >>> class A(object):
    ...     pass
    ...
    >>> class B(object):
    ...     pass
    ...
    >>> A.fullname
    '__main__.A'
    >>> B.fullname
    '__main__.B'
    """



# Generated at 2022-06-14 06:39:51.761214
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def value(cls):
            return "value"

    assert Test.value == "value"



# Generated at 2022-06-14 06:39:54.742532
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def a(cls):
            print("hi")
            return 1

    assert Test.a == 1
    assert Test.a == 1
    assert Test.a == 1



# Generated at 2022-06-14 06:40:01.135072
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def prop(cls):
            print('called for {}'.format(cls))
            return []

    class B(A):
        pass

    class C(A):
        pass

    a = A()
    b = B()
    c = C()

    a.prop.append('a')
    a.prop.append('b')

    b.prop.append('c')
    b.prop.append('d')

    print('A prop is {}'.format(a.prop))
    print('B prop is {}'.format(b.prop))
    print('C prop is {}'.format(c.prop))


# Generated at 2022-06-14 06:40:07.442750
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Parent(object):
        def __iter__(self):
            yield "1"
            yield "2"

    def get_iterator(cls):
        return iter(cls())

    @lazyperclassproperty
    def p(cls):
        return list(get_iterator(cls))

    class Child(Parent):
        pass

    assert p == ["1", "2"]
    assert Child.p == ["1", "2"]



# Generated at 2022-06-14 06:40:14.461085
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def num(cls):
            return 1

        @lazyperclassproperty
        def name(cls):
            return cls.__name__

    class B(A):
        @lazyperclassproperty
        def num(cls):
            return 2

    assert A.num == 1
    assert B.num == 2
    assert A.name == 'A'
    assert B.name == 'B'



# Generated at 2022-06-14 06:40:20.250468
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass(object):
        @lazyclassproperty
        def testproperty(cls):
            return 'this is a test'
    assert TestClass.testproperty == 'this is a test'
    assert getattr(TestClass, '_lazy_testproperty') == 'this is a test'



# Generated at 2022-06-14 06:40:31.908833
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Parent(object):
        def __init__(self):
            pass

        @lazyperclassproperty
        def foo(cls):
            print("foo eval: " + cls.__name__)
            return cls.__name__

    class Child(Parent):
        def __init__(self):
            Parent.__init__(self)


    print("")
    print("Parent.foo:")
    print(Parent.foo)
    print("Parent.foo:")
    print(Parent.foo)
    print("Child.foo:")
    print(Child.foo)
    print("Child.foo:")
    print(Child.foo)
    print("Parent.foo:")
    print(Parent.foo)



# Generated at 2022-06-14 06:40:45.064698
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A():
        @lazyperclassproperty
        def test(cls):
            return cls.__name__
        @lazyperclassproperty
        def test2(cls):
            return cls.__name__

    class B(A):
        pass

    class C(A):
        pass

    a = A()
    b = B()
    c = C()

    assert a.test is not b.test
    assert a.test is not c.test
    assert a.test is A.test
    assert b.test is B.test
    assert c.test is C.test
    assert b.test == C.test

    assert a.test2 is not b.test2
    assert a.test2 is not c.test2
    assert a.test2 is A.test2
    assert b.test

# Generated at 2022-06-14 06:40:52.294224
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):

        @lazyperclassproperty
        def var(cls):
            return "Base"

    class A(Base):
        pass

    class B(Base):

        @lazyperclassproperty
        def var(cls):
            return "B"

    assert A.var == "Base"
    assert B.var == "B"
    assert Base.var == "Base"



# Generated at 2022-06-14 06:41:17.368352
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        v = 1


# Generated at 2022-06-14 06:41:27.680007
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            return 'A'

    @add_metaclass(A)
    class B(object):
        pass
    assert A.x == 'A'
    assert B.x == 'A'

    class C(A):
        @lazyclassproperty
        def x(cls):
            return 'C'

    class D(C):
        pass

    assert C.x == 'C'
    assert D.x == 'C'



# Generated at 2022-06-14 06:41:39.385646
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        def __init__(self, value):
            self.value = value

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    class E(D):
        pass

    class F(E, B):
        pass

    @lazyperclassproperty
    def foo(cls):
        return cls.__name__

    assert F.foo == E.foo == D.foo == C.foo == 'C'
    assert B.foo == A.foo == 'A'

    assert F().foo == 'C'
    assert A('123').foo == 'A'
    assert B('123').foo == 'A'
    assert C('123').foo == 'C'
    assert D('123').foo == 'C'

# Generated at 2022-06-14 06:41:48.642992
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self):
            self.a = 25
        @lazyclassproperty
        def b(cls):
            cls.a += 1
            return cls.a

    class B(A):
        pass

    a = A()
    b = B()
    assert a.b == 26
    assert b.b == 26

    A.c = lazyclassproperty(lambda cls: cls.a + 100)
    class D(A):
        pass
    assert D.c == a.b + 100
    assert D.c == b.b + 100



# Generated at 2022-06-14 06:41:56.424644
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self, id):
            self.id = id

        @lazyperclassproperty
        def some_value(cls):
            return cls.__name__

        @lazyperclassproperty
        def another(cls):
            return cls.__name__ + '_another'
    a = A('A')
    b = A('B')
    print(a.some_value)
    print(b.some_value)
    print(a.another)
    print(b.another)

# Generated at 2022-06-14 06:42:07.984173
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def attr(cls):
            return 1

        @lazyclassproperty
        def attr_with_args(cls, a, b):
            return a + b

        @staticmethod
        def static_attr():
            return 1

        @staticmethod
        def static_attr_with_args(a, b):
            return a + b

    class B(A):
        @lazyclassproperty
        def attr_with_args(cls, a, b):
            return a - b

        @staticmethod
        def static_attr_with_args(a, b):
            return a - b

    assert A.attr == 1
    assert A.attr_with_args(1, 1) == 2
    assert A.static_attr() == 1
   

# Generated at 2022-06-14 06:42:12.130431
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def my_property(self):
            return 'my_property'

    assert A.my_property == 'my_property'



# Generated at 2022-06-14 06:42:25.397879
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    import unittest

    class MyClass(object):

        def __init__(self, name):
            self.name = name

        @lazyclassproperty
        def val(cls):
            print('Calculating')
            return 2

        @lazyclassproperty
        def val2(cls):
            print('Calculating')
            return 3

    class MyClass2(MyClass):
        pass

    class TestClassProperties(unittest.TestCase):

        def setUp(self):
            self.my = MyClass('test')
            self.my2 = MyClass2('test2')

        def test_classprop(self):
            self.assertEqual(self.my.val, 2)
            self.assertEqual(MyClass.val, 2)


# Generated at 2022-06-14 06:42:39.249835
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        @lazyperclassproperty
        def x(cls):
            print("* x() *")
            return 'lazy'

    class Bar(Foo):
        pass

    class Baz(Bar):
        pass

    # Check that everything works
    assert Foo.x == Bar.x == Baz.x == 'lazy'

    # Check that inheritance works
    foo = Foo()
    bar = Bar()
    baz = Baz()
    foo.x = 'foo'
    bar.x = 'bar'
    baz.x = 'baz'
    assert foo.x == 'foo'
    assert bar.x == 'bar'
    assert baz.x == 'baz'
    assert Foo.x == 'lazy'
    assert Bar.x == 'lazy'

# Generated at 2022-06-14 06:42:44.386651
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def foo(cls):
            print('calculating foo')
            return (1, 2)

    assert A.foo == (1, 2)
    assert A.foo == (1, 2)



# Generated at 2022-06-14 06:43:26.540995
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class ParentClass(object):
        @lazyperclassproperty
        def test(self):
            return 1

    class ChildClass(ParentClass):
        pass

    assert ParentClass().test == 1
    assert ChildClass().test == 1

    ParentClass.test = 2
    assert ChildClass().test == 1

# Generated at 2022-06-14 06:43:30.773866
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Testing lazyclassproperty.
    """
    class c:
        @lazyclassproperty
        def cprop(cls):
            return 1

    assert c.cprop == 1



# Generated at 2022-06-14 06:43:37.104122
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def value(cls):
            return sorted([cls.a, cls.b])

        a = 1
        b = 2

    assert Test.value == [1,2]
    Test.a = 3
    Test.b = 4
    assert Test.value == [1, 2]

    class SubTest(Test):
        c = 5

    Test.a = 3
    Test.b = 4
    Test.c = 6
    assert Test.value == [1,2]
    assert SubTest.value == [3,4]





# Generated at 2022-06-14 06:43:48.556476
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def cached_number(cls):
            print('Calculating number for %r' % cls)
            return sum(range(1000))

    class Derived1(Base):
        pass

    class Derived2(Base):
        pass

    assert Base.cached_number == 999 * 1000 / 2
    assert Derived1.cached_number == 999 * 1000 / 2
    assert Derived2.cached_number == 999 * 1000 / 2
    assert Base.cached_number == 999 * 1000 / 2
    assert Derived1.cached_number == 999 * 1000 / 2
    assert Derived2.cached_number == 999 * 1000 / 2

    Base.cached_number = 'hello world!'
    assert Base.cached_number == 'hello world!'


# Generated at 2022-06-14 06:43:54.812816
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def value(self):
            print('value in class A')
            return 'A'
    class B(A):
        pass
    class C(B):
        pass
    a = A()
    b = B()
    c = C()

    print(a.value)
    print(b.value)
    print(c.value)



# Generated at 2022-06-14 06:44:08.047975
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def test(cls):
            return cls.__name__
    class B(A):
        pass
    class C(B):
        pass

    # Initial state
    assert hasattr(A, '_lazy_test') is False
    assert hasattr(B, '_lazy_test') is False
    assert hasattr(C, '_lazy_test') is False

    # Accessing test property on each class will cause it to be created
    assert A.test == 'A'
    assert hasattr(A, '_lazy_test')
    assert B.test == 'B'
    assert hasattr(B, '_lazy_test')
    assert C.test == 'C'
    assert hasattr(C, '_lazy_test')

   

# Generated at 2022-06-14 06:44:14.371516
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            print('bar')
            return 42

    class Bar(Foo):
        pass

    print(Foo.bar)
    print(Foo.bar)
    print(Bar.bar)



# Generated at 2022-06-14 06:44:22.292931
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    lock = threading.Lock()
    executed = False
    class Test(object):
        @lazyclassproperty
        def test(cls):
            nonlocal lock, executed
            with lock:
                if not executed:
                    executed = True
                else:
                    raise Exception("Function 'lazyclassproperty' does not work")
                return "test"
    t1 = Test()
    t2 = Test()
    assert t1.test == t2.test # Runs the function only once



# Generated at 2022-06-14 06:44:27.089315
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        pass
    class B(A):
        pass

    # Define a class-level property with lazyperclassproperty

# Generated at 2022-06-14 06:44:36.043962
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            print('x is being created')
            return 'x'

    class B(A):
        pass
    class C(A):
        @lazyclassproperty
        def x(cls):
            print('x from c is being created')
            return 'xc'

    class D(B):
        pass
    a = A()
    b = B()
    c = C()
    d = D()

    assert A.x == 'x'
    assert B.x == 'x'
    assert C.x == 'xc'
    assert D.x == 'x'

    assert a.x == 'x'
    assert b.x == 'x'
    assert c.x == 'xc'
    assert d.x == 'x'