

# Generated at 2022-06-14 06:35:39.934801
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            return 9
    assert A.foo == 9

# Generated at 2022-06-14 06:35:48.763356
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    print('--------------------')
    print('test_lazyperclassproperty')
    class Super(object):
        @lazyperclassproperty
        def super_lazy(cls):
            print('super_lazy')
            return 1

    print('Super.super_lazy', Super.super_lazy)
    class Sub(Super):
        pass

    print('Sub.super_lazy', Sub.super_lazy)

    print('--------------------')
    # Unit test for function lazyclassproperty
    print('test_lazyclassproperty')
    class Super(object):
        @lazyclassproperty
        def super_lazy(cls):
            print('super_lazy')
            return 1

    print('Super.super_lazy', Super.super_lazy)

# Generated at 2022-06-14 06:35:59.830523
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        @lazyperclassproperty
        def foo(cls):
            return cls.__name__ + '_foo'

    class Bar(Foo):
        pass

    assert Foo.foo == 'Foo_foo'
    assert Bar.foo == 'Bar_foo'

    # Regular lazy class property will collide across subclasses
    class Foo(object):
        @lazyclassproperty
        def foo(cls):
            return cls.__name__ + '_foo'

    class Bar(Foo):
        pass

    assert Foo.foo == 'Bar_foo'
    assert Bar.foo == 'Bar_foo'



# Generated at 2022-06-14 06:36:02.562792
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo():
        @lazyclassproperty
        def bar(cls):
            return 'baz'


# Generated at 2022-06-14 06:36:11.669810
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def list(cls):
            return []

    class B(A):
        @lazyperclassproperty
        def list(cls):
            return [1,2,3]

    class C(A):
        pass

    class D(B):
        @lazyperclassproperty
        def list(cls):
            return [3,2,1]

    def test_object(obj):
        obj.list.append(obj.__name__)
        print(obj.list, obj.__name__)
        return obj.list

    print('\nA 1')
    print(test_object(A()))
    print('\nA 2')
    print(test_object(A()))
    print('\nB')

# Generated at 2022-06-14 06:36:20.152641
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        def __init__(self, x): self.x = x


# Generated at 2022-06-14 06:36:26.919678
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Parent(object):
        @lazyperclassproperty
        def foo(cls):
            return 'Parent foo'

    class Child(Parent):
        pass

    class Child2(Parent):
        @lazyperclassproperty
        def foo(cls):
            return 'Child2 foo'

    assert Parent.foo == 'Parent foo'
    assert Child.foo == 'Parent foo'
    assert Child2.foo == 'Child2 foo'

    # Check that it's cached
    Parent.foo = 'Parent foo 2'
    Child.foo = 'Child foo 2'
    Child2.foo = 'Child2 foo 2'
    assert Parent.foo == 'Parent foo 2'
    assert Child.foo == 'Parent foo 2'
    assert Child2.foo == 'Child2 foo 2'



# Generated at 2022-06-14 06:36:32.936643
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def b(cls):
            return 'A'

    class B(A):
        @lazyclassproperty
        def b(cls):
            return 'B'

    assert A.b == 'A'
    assert B.b == 'B'


# Generated at 2022-06-14 06:36:39.217114
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):

        @lazyclassproperty
        def hello(cls):
            """
            Dummy function
            """
            return 'Hello'

    assert A.hello == 'Hello'
    assert A.hello == 'Hello'
    assert A.hello == 'Hello'

    class B(A):
        pass

    assert B.hello == 'Hello'
    assert B.hello == 'Hello'
    assert B.hello == 'Hello'



# Generated at 2022-06-14 06:36:52.173837
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base:
        @lazyperclassproperty
        def foo(cls):
            print("Evaluating foo() as class {}".format(cls.__name__))
            return "foo_result"

    print("-- class Base --")
    print(Base.foo)
    print(Base.foo)

    class FirstInheritor(Base):
        pass

    print("-- class FirstInheritor --")
    print(FirstInheritor.foo)
    print(FirstInheritor.foo)

    class SecondInheritor(Base):
        @classproperty
        def foo(cls):
            print("Overwriting foo()")
            return "foo_overwritten"

    print("-- class SecondInheritor --")
    print(SecondInheritor.foo)
    print(SecondInheritor.foo)
   

# Generated at 2022-06-14 06:36:58.833107
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:37:10.307914
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Meta(type):
        pass

    class A(metaclass=Meta):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        @staticmethod
        def f(cls):
            print('f was called')
            return cls

        @lazyperclassproperty
        def g(cls):
            print('g was called')
            return cls

    # Testing the @lazyperclassproperty
    # print(D.f())
    # print(D.g)
    # print(B.g)
    # print(A.g)
    # print(C.g)



# Generated at 2022-06-14 06:37:16.298694
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            print('computed')
            return 42

    print(A.prop)
    print(A.prop)
    print(A.prop)

    print('\n')

    class B(A):
        pass

    print(B.prop)
    print(B.prop)
    print(B.prop)


# Generated at 2022-06-14 06:37:20.100311
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Lazytest:

        @lazyclassproperty
        def foo(cls):
            print('foo:', cls)
            return cls

    assert Lazytest.foo is Lazytest.foo is Lazytest
    Lazytest.foo = None
    assert Lazytest.foo is Lazytest.foo is Lazytest



# Generated at 2022-06-14 06:37:28.836251
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Meta(type):
        @lazyperclassproperty
        def prop(self):
            print(self)
            return 'a'

    class A(metaclass=Meta):
        pass

    class B(A):
        pass

    class C(A):
        pass

    a = A()
    a1 = A()
    b = B()
    c = C()
    print(a.prop)
    print(a1.prop)
    print(b.prop)
    print(a.prop)
    print(b.prop)



# Generated at 2022-06-14 06:37:42.102855
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:37:51.904157
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def lazyprop():
            print("Calling lazyprop in Test")
            return 'lazyprop Test'

    class Test2(Test):
        @lazyclassproperty
        def lazyprop():
            print("Calling lazyprop in Test2")
            return 'lazyprop Test2'

    assert Test.lazyprop == 'lazyprop Test'
    assert Test.lazyprop == 'lazyprop Test'
    assert Test2.lazyprop == 'lazyprop Test2'
    assert Test2.lazyprop == 'lazyprop Test2'
    assert Test.lazyprop == 'lazyprop Test'



# Generated at 2022-06-14 06:38:03.778921
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from collections import namedtuple

    class Test(object):
        @lazyclassproperty
        def foo(cls):
            return 'bar'

        @lazyclassproperty
        def fake(cls):
            return 'original'

    assert Test.foo == 'bar'
    assert Test.fake == 'original'

    class X(Test):
        pass

    assert Test.foo == 'bar'
    assert Test.fake == 'original'

    assert X.foo == 'bar'
    assert X.fake == 'original'

    Test.fake = 'replaced'

    assert Test.foo == 'bar'
    assert Test.fake == 'replaced'

    assert X.foo == 'bar'
    assert X.fake == 'original'

    @lazyclassproperty
    def foo(cls):
        return 'bar'



# Generated at 2022-06-14 06:38:15.750623
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        rng = random.Random()
        @lazyperclassproperty
        def r(cls):
            return cls.rng.randint(1, 10)

    class B(A):
        @lazyperclassproperty
        def s(cls):
            return cls.rng.randint(1, 10)

    class C(B):
        @lazyperclassproperty
        def t(cls):
            return cls.rng.randint(1, 10)

    assert all(x == A.r and x == B.r and x == C.r for x in [A.r, B.r, C.r])
    assert all(x == B.s and x == C.s for x in [B.s, C.s])
    assert A.t == C

# Generated at 2022-06-14 06:38:20.809497
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:38:30.822490
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            print("new instance of A.x")
            return 1
    class B(A):
        pass
    assert (A.x == 1)
    assert (B.x == 1)
    assert (A.x == B.x)


# Generated at 2022-06-14 06:38:36.075451
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):

        def test(self):
            return 'foo'

    class Bar(Foo):

        @lazyclassproperty
        def test(cls):
            return 'bar'

    assert Foo().test() == 'foo'
    assert Bar().test() == 'bar'



# Generated at 2022-06-14 06:38:48.919170
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from unittest import TestCase
    from unittest.mock import Mock

    fn = Mock()
    fn.__name__ = '__testprop__'
    fn.return_value = '__testvalue__'

    class TestClass(TestCase):
        __testprop__ = lazyclassproperty(fn)

    assert type(TestClass.__testprop__) is property
    assert fn.called == False

    # The property should only be initialized once.
    assert TestClass.__testprop__ == '__testvalue__'
    assert fn.called == True
    assert TestClass.__testprop__ == '__testvalue__'
    assert fn.called == True

    # The property should be the same for all inheritors of `TestClass`.
    class SubClass1(TestCase):
        pass


# Generated at 2022-06-14 06:38:55.687018
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        counter = 0
        @lazyclassproperty
        def foo(cls):
            cls.counter += 1
            return 'bar'

    assert Test.foo == 'bar', Test.foo
    assert Test.counter == 1, Test.counter
    assert Test.foo == 'bar', Test.foo
    assert Test.counter == 1, Test.counter
    assert Test().foo == 'bar', Test.foo
    assert Test.counter == 1, Test.counter



# Generated at 2022-06-14 06:39:06.709338
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return "A %s" % cls

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def x(cls):
            return "C %s" % cls

    assert A.x == "A <class 'A'>"
    assert B.x == "A <class 'B'>"
    assert C.x == "C <class 'C'>"
    assert A().x == "A <class 'A'>"
    assert B().x == "A <class 'B'>"
    assert C().x == "C <class 'C'>"



# Generated at 2022-06-14 06:39:14.153866
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def x(cls):
            return 100

    class B(A):
        pass

    class C(A):
        pass

    a = A()
    b = B()
    c = C()

    assert a.x == 100
    assert b.x == 100
    assert c.x == 100

    b.x = 10
    c.x = 20

    assert a.x == 100
    assert b.x == 10
    assert c.x == 20



# Generated at 2022-06-14 06:39:19.580187
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class C(object):
        @lazyperclassproperty
        def one(cls):
            return 1

    class D(C):
        pass

    assert C.one == 1
    assert D.one == 1

    C.one = 2

    assert C.one == 2
    assert D.one == 1



# Generated at 2022-06-14 06:39:25.967829
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            return cls.__name__

    class B(A):
        pass

    assert A.x == 'A'
    assert B.x == 'B'
    assert A.x == 'A', 'Lazy class property should be populated once'
    assert B.x == 'B'



# Generated at 2022-06-14 06:39:35.657984
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self, a):
            self.a = a

        @lazyperclassproperty
        def b(cls):
            return ''.join(reversed(cls.__name__))

    class B(A):
        pass

    class C(B):
        pass

    for cls in A, B:
        assert ''.join(reversed(cls.__name__)) == cls.b
    assert A.b == B.b == C.b
    assert A.b is not C.b
    a = A('foo')
    assert a.b == 'a'
    assert a.__dict__['b'] == 'a'
    assert 'b' not in A.__dict__



# Generated at 2022-06-14 06:39:43.188525
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Parent(object):
        def __init__(self, class_name):
            self.class_name = class_name

        @lazyperclassproperty
        def name(cls):
            return cls.__name__

    class ChildA(Parent):
        pass

    class ChildB(Parent):
        pass
    assert Parent('A').name == 'Parent'
    assert ChildA('A').name == 'ChildA'
    assert ChildB('B').name == 'ChildB'
    assert Parent('A').name == 'Parent'
    assert ChildA('A').name == 'ChildA'
    assert ChildB('B').name == 'ChildB'



# Generated at 2022-06-14 06:39:57.970042
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        attr = lazyperclassproperty(lambda c: list())

    class B(A):
        pass

    class C(A):
        pass

    assert A.attr == B.attr == C.attr
    A.attr.append('first')
    B.attr.append('second')
    C.attr.append('third')

    assert A.attr != B.attr != C.attr
    assert A.attr == ['first']
    assert B.attr == ['second']
    assert C.attr == ['third']



# Generated at 2022-06-14 06:40:10.719141
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    testclass = type("TestClass", (), {})

    def make_one():
        return 1

    def make_two():
        return 2

    test_prop = lazyclassproperty(make_one)
    assert test_prop.__doc__ is None, "No docstring found"
    assert test_prop.__name__ == "_lazy_make_one", "Incorrect decorator name"
    assert testclass._lazy_make_one is None, "Incorrect class attribute value set"
    assert testclass._lazy_make_one == 1, "Incorrect value returned"
    assert testclass._lazy_make_one == 1, "Value should have been cached"

    test_prop = lazyclassproperty(make_two)
    assert testclass._lazy_make_two is None, "Incorrect second class attribute value set"




# Generated at 2022-06-14 06:40:16.381591
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:40:24.055916
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        call_count = 0

        @lazyclassproperty
        def val(cls):
            cls.call_count += 1
            return 'val'

    class B(A):
        pass

    a = A()
    b = B()

    assert A.call_count == 0
    assert A.val == 'val'
    assert A.call_count == 1
    assert A.val == 'val'
    assert A.call_count == 1

    assert B.call_count == 0
    assert B.val == 'val'
    assert B.call_count == 1
    assert B.val == 'val'
    assert B.call_count == 1

    assert a.val == 'val'
    assert a.call_count == 1
    assert a.val == 'val'

# Generated at 2022-06-14 06:40:27.884697
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        @lazyperclassproperty
        def bar(cls):
            print('running foobar()')
            return 1

    class Bar(Foo):
        pass

    assert Foo.bar is not Bar.bar



# Generated at 2022-06-14 06:40:37.403418
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from unittest import TestCase
    from mock import patch

    class BaseTestClass(object):
        def one(self):
            return 1
        two = two = lazyclassproperty(lambda self: self.one() * 2)

    class TestClass(BaseTestClass):
        def one(self):
            return 2

    class AnotherTestClass(TestClass):
        pass

    testclass = TestClass()
    testclass2 = TestClass()
    anothertestclass = AnotherTestClass()
    anothertestclass2 = AnotherTestClass()

    class a(TestCase):
        def test_lazyclassproperty_with_parent_class(self):
            self.assertEqual(BaseTestClass.two, 2)
            self.assertEqual(BaseTestClass().two, 2)


# Generated at 2022-06-14 06:40:47.735359
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class MyClass:
        @lazyclassproperty
        def get_with_args(cls, a, b):
            return a + b

    # calling a,b with 2,3 returns 5 and stores this in the class
    print(MyClass.get_with_args, MyClass.get_with_args(2, 3))

    # calling a,b with 3,4 returns 7 and will update the class value
    print(MyClass.get_with_args, MyClass.get_with_args(3, 4))

    # calling a,b with 4,5 returns 9, but in this case we lose the previous setting
    # this is created as a new class property
    print(MyClass.get_with_args, MyClass.get_with_args(4, 5))

#test_lazyclassproperty()


# Generated at 2022-06-14 06:40:54.974990
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        a = 1

        @lazyclassproperty
        def b(cls):
            return cls.a * 2

        @lazyclassproperty
        def c(cls):
            return cls.b * 2

    class B(A):
        a = 2

    assert A.b == 2
    assert B.b == 4
    assert A.c == 4
    assert B.c == 8



# Generated at 2022-06-14 06:40:59.475944
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:05.216657
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:29.123438
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(self):
            print("Calculating foo")
            return 42
    class B(A):
        pass
    class C(A):
        pass
    a = A()
    b = B()
    c = C()
    print(a.foo)
    print(b.foo)
    print(c.foo)



# Generated at 2022-06-14 06:41:36.972242
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:49.466606
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    "Unit test for function lazyperclassproperty"

    class Base(object):
        @lazyperclassproperty
        def prop1(cls):
            print('Base.prop1')
            return 'Base.prop1'

    class Inherited(Base):
        @lazyperclassproperty
        def prop1(cls):
            print('Inherited.prop1')
            return 'Inherited.prop1'

        @lazyperclassproperty
        def prop2(cls):
            print('Inherited.prop2')
            return 'Inherited.prop2'

    assert Base().prop1 == 'Base.prop1'
    assert Inherited().prop1 == 'Inherited.prop1'
    assert Inherited().prop2 == 'Inherited.prop2'



# Generated at 2022-06-14 06:41:57.804210
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class testlazycls(object):
        @lazyclassproperty
        def lazyvalue(cls):
            print("Returning a new instance")
            return []

    class child1(testlazycls):
        pass

    class child2(testlazycls):
        pass

    child1inst = child1()
    child2inst = child2()
    assert child1.lazyvalue is child1.lazyvalue
    assert child1.lazyvalue is child1inst.lazyvalue
    assert child2.lazyvalue is child2inst.lazyvalue
    assert child2.lazyvalue is not child1.lazyvalue



# Generated at 2022-06-14 06:42:06.702149
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class a(object):
        @lazyperclassproperty
        def set_value(cls):
            return 10

    class b(a):
        pass


# Generated at 2022-06-14 06:42:18.071467
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    """
    Unit tests for lazyperclassproperty function
    """
    class Base(object):
        def __init__(self):
            self.value = 0
    class A(Base):
        @lazyperclassproperty
        def x(klass):
            return klass.value
        @classmethod
        def set_x(klass,val):
            klass.value = val
    class B(Base):
        @lazyperclassproperty
        def x(klass):
            return klass.value
        @classmethod
        def set_x(klass,val):
            klass.value = val
    assert not hasattr(A,'_x')
    assert not hasattr(A,'_A_lazy_x')
    assert hasattr(B,'_B_lazy_x')
    assert A.x

# Generated at 2022-06-14 06:42:22.503452
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Bar(object):
        @lazyclassproperty
        def foo(cls):
            return "foo"

    assert Bar.foo is Bar.foo



# Generated at 2022-06-14 06:42:29.174000
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        def __init__(self, x):
            self.x = x

    class B(A):
        @lazyperclassproperty
        def y(cls):
            return cls.__name__ + '!!!'

    class C(A):
        pass

    assert A(5).y is A.y
    assert B(5).x == 5
    assert B(5).y == 'B!!!'
    assert C(5).x == 5
    assert C(5).y == 'C!!!'


# Generated at 2022-06-14 06:42:42.572915
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        def __init__(self):
            print("A")
    
    class B:
        def __init__(self):
            print("B")
    
    class C(A):
        @lazyperclassproperty
        def instance(cls):
            return cls()
    
    class D(B):
        @lazyperclassproperty
        def instance(cls):
            return cls()
    
    class E(C, D):
        @lazyperclassproperty
        def instance(cls):
            return cls()
    
    c1 = C.instance
    c2 = C.instance
    d1 = D.instance
    d2 = D.instance
    e1 = E.instance
    e2 = E.instance
    assert c1 is c2
    assert c1

# Generated at 2022-06-14 06:42:49.776795
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:43:30.544422
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            return 1
    class B(A):
        pass
    assert A.x == B.x == 1


# Generated at 2022-06-14 06:43:35.261011
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:43:41.705931
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(self):
            return id(self)

    a = A()
    b = A()
    assert a.foo != b.foo

    class B(A):
        pass

    c = B()
    assert a.foo != c.foo

    assert b.foo != c.foo


# Generated at 2022-06-14 06:43:46.688187
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 1
    class B(A):
        pass

    assert A.a == 1
    assert B.a == 1
    A.a = 2
    assert A.a == 2
    assert B.a == 1



# Generated at 2022-06-14 06:43:53.904807
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class C(object):

        @lazyclassproperty
        def value(cls):
            print("[%s]: Calculating value..." % cls.__name__)
            return 1 + 1

        @property
        def value_property(self):
            print("[%s]: Calculating value_property..." % self.__class__.__name__)
            return 1 + 1

    # Check class property
    assert C.value == 2
    assert C.value == 2
    # Same property for all classes/inheritors
    assert C.value == object.value

    # Check regular property
    c_instance = C()
    c_instance.value_property
    assert c_instance.value_property == 2
    assert c_instance.value_property == 2
    # Different property for each instance
    assert c_instance.value_

# Generated at 2022-06-14 06:43:58.083924
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop(cls):
            return cls.__name__

    class B(A):
        pass

    assert A.prop == 'A'
    assert B.prop == 'B'



# Generated at 2022-06-14 06:44:06.099479
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Base(object):
        @lazyperclassproperty
        def prop(cls):
            return 'Base'

    class Derived(Base):
        pass

    class Derived2(Base):
        @lazyperclassproperty
        def prop(cls):
            return 'Derived2'

    assert Base.prop == 'Base'
    assert Derived.prop == 'Base'
    assert Derived2.prop == 'Derived2'


# Generated at 2022-06-14 06:44:10.892896
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self):
            self.a = 1
            self.b = 2
    class B(A):
        def __init__(self):
            self.a = 3
            self.b = 4

    lazy_a_b_sum = lazyperclassproperty(lambda cls: cls().a + cls().b)
    assert A.lazy_a_b_sum == 3
    assert B.lazy_a_b_sum == 7



# Generated at 2022-06-14 06:44:15.529253
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:44:20.564891
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            print("computing prop")
            return sum(range(100))
    class B(A):
        pass
    class C(B):
        pass
    assert A.prop == B.prop == C.prop == 4950

