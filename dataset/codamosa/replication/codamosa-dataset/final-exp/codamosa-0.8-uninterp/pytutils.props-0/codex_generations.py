

# Generated at 2022-06-14 06:35:47.984144
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    global TEST_COUNT

    class Foo(object):

        def __init__(self):
            self.counter = 0

        def increment_counter(self):
            self.counter += 1
            return self.counter

        @lazyclassproperty
        def a(self):
            return self.increment_counter()

        @lazyclassproperty
        def b(self):
            return self.increment_counter()

    class Bar(Foo):

        @lazyclassproperty
        def a(self):
            return self.increment_counter()

    class BarBar(Bar):
        pass

    TEST_COUNT += 1
    assert Foo().a == 1
    TEST_COUNT += 1
    assert Foo().b == 1
    TEST_COUNT += 1
    assert Bar().a == 1
    TEST_COUNT += 1


# Generated at 2022-06-14 06:35:59.703991
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class ClassA(object):
        @lazyclassproperty
        def TEST(cls):
            ClassA.TESTNUM += 1
            return cls

    ClassA.TESTNUM = 0
    assert ClassA.TESTNUM == 0
    assert ClassA.TEST is ClassA
    assert ClassA.TESTNUM == 1
    assert ClassA.TEST is ClassA
    assert ClassA.TESTNUM == 1

    class ClassB(ClassA):
        pass

    assert ClassB.TEST is ClassB
    assert ClassA.TESTNUM == 2
    assert ClassB.TEST is ClassB
    assert ClassA.TESTNUM == 2



# Generated at 2022-06-14 06:36:06.515234
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        def __init__(self):
            self.a = 1
            self.b = 1

        @lazyclassproperty
        def c(cls):
            return 3

        @lazyclassproperty
        def d(cls):
            return cls.a + cls.b

    c1, c2 = C(), C()
    c1.a = 2
    c1.b = 2
    c2.a = 3
    c2.b = 3

    assert c1.c == 3
    assert c2.c == 3
    assert c1.d == c1.a + c1.b
    assert c2.d == c2.a + c2.b
    assert c1.__dict__ == {'a': 2, 'b': 2}
    assert c2.__

# Generated at 2022-06-14 06:36:11.497751
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    print("\nUnit test for function lazyperclassproperty")

    class TestCase:
        @lazyperclassproperty
        def TestProperty(cls):
            print("Calculating value for TestProperty")
            return cls.__name__ + "TestProperty"

    class TestCaseSubClass(TestCase):
        pass

    assert TestCase.TestProperty == TestCaseSubClass.TestProperty == "TestCaseTestProperty"



# Generated at 2022-06-14 06:36:17.518168
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class TestClass(object):

        @lazyclassproperty
        def someattr(cls):
            return 'Some value'

    assert TestClass.someattr == 'Some value'
    assert TestClass.someattr == 'Some value'
    assert TestClass.__dict__['_lazy_someattr'] == 'Some value'



# Generated at 2022-06-14 06:36:23.047535
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 1
    class B(A):
        pass
    assert A.prop == 1
    assert B.prop == 1
    assert A.prop == B.prop == 1


# Generated at 2022-06-14 06:36:28.867584
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:36:36.084834
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class FooTest(object):
        _x = None

        @lazyclassproperty
        def x(cls):
            cls._x = 1
            return cls._x

    class BarTest(FooTest):
        def test(self):
            return self.x

    assert FooTest.x == 1
    assert BarTest.x == 1
    assert BarTest().test() == 1
    assert FooTest.x == 1
    assert BarTest.x == 1


# Generated at 2022-06-14 06:36:45.407943
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:36:50.512767
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print("calculating...")
            return 42
    class B(A):
        pass

    print(A.foo)
    print(A.foo)
    print(B.foo)
    print(B.foo)

# Generated at 2022-06-14 06:36:59.218037
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return cls.__name__

    class B(A):
        pass

    assert A.x == 'A'
    assert B.x == 'B'
    A.x = 'c'
    assert A.x == 'c'
    assert B.x == 'B'



# Generated at 2022-06-14 06:37:02.684349
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def prop(cls):
            return 1
    assert C.prop == 1
    assert C.prop == 1


# Generated at 2022-06-14 06:37:07.067686
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self):
            self.a = 'A'

        @lazyperclassproperty
        def O(cls):
            return cls()

    class B(A):
        def __init__(self):
            self.a = 'B'

    assert A().O.a == 'A'
    assert B().O.a == 'B'



# Generated at 2022-06-14 06:37:10.856073
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:37:23.747605
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        @lazyperclassproperty
        def prop(self):
            return {'self': str(self)}

    class B(A):
        pass

    class C(A):
        pass

    a1 = A()
    a2 = A()
    b1 = B()
    b2 = B()
    c1 = C()
    c2 = C()

    prop1 = a1.prop
    prop2 = a2.prop
    prop3 = b1.prop
    prop4 = b2.prop
    prop5 = c1.prop
    prop6 = c2.prop

    assert a1.prop == {'self': '<__main__.A object at 0x00DEAD>'}
    assert a1.prop is prop1

# Generated at 2022-06-14 06:37:35.552633
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:37:43.368957
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    pass
    # class A:
    #     def __init__(self, **kwargs):
    #         self.__dict__.update(kwargs)
    #
    #     @lazyperclassproperty
    #     def prop(cls):
    #         return '%s.prop' % cls
    #
    # class B(A): pass
    #
    # assert A().prop == 'A.prop'
    # assert B().prop == 'B.prop'



# Generated at 2022-06-14 06:37:48.412687
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class f(object):
        @lazyperclassproperty
        def a(cls):
            return cls

    class g(f):
        pass
    assert f.a is f
    assert f.a is not g.a
    assert g.a is g



# Generated at 2022-06-14 06:37:56.471266
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:37:59.062615
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        @lazyclassproperty
        def func(cls):
            return 100

    assert MyClass.func == 100



# Generated at 2022-06-14 06:38:15.380259
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from time import sleep
    from unittest import TestCase, main

    class TestClass1(object):
        def __init__(self, seed):
            self.seed = seed

        @lazyclassproperty
        def class_attr(cls):
            sleep(self.seed)
            return "Created at %s" % self.seed

    class TestClass2(TestClass1):
        def __init__(self, seed):
            super(TestClass2, self).__init__(seed)

    class TestLazyClassProperty(TestCase):
        def test_lazyclassproperty(self):
            instance1 = TestClass1(0.5)
            instance2 = TestClass1(1)

            self.assertEqual(TestClass1.class_attr, "Created at 1")

            instance3 = TestClass2(2)

# Generated at 2022-06-14 06:38:27.485431
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:38:32.420173
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:38:40.185845
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Test lazyclassproperty using the following class structure:
        A
          B
          C
        D
          E
            F
          G
    """
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 'aa'

    class B(A):
        pass

    class C(A):
        pass

    class D(object):
        pass

    class E(D):
        pass

    class F(E):
        pass

    class G(D):
        pass

    assert A.a == 'aa'
    assert B.a == 'aa'
    assert C.a == 'aa'
    assert D.a == 'aa'
    assert E.a == 'aa'
    assert F.a == 'aa'
    assert G.a == 'aa'

    A

# Generated at 2022-06-14 06:38:53.432427
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        call_count = 0
        @lazyperclassproperty
        def prop(cls):
            cls.call_count += 1
            return 'a'
    class B(A):
        pass
    class C(A):
        @lazyperclassproperty
        def prop(cls):
            cls.call_count += 1
            return 'c'
    class D(B):
        pass
    assert A.prop == 'a'
    assert A.call_count == 1
    assert B.prop == 'a'
    assert A.call_count == 1
    assert C.prop == 'c'
    assert A.prop == 'a'
    assert A.call_count == 2
    assert C.call_count == 1
    assert D.prop == 'a'

# Generated at 2022-06-14 06:39:01.038285
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Base:

        @lazyperclassproperty
        def answer(cls):
            # this should be called once per cls
            print("Calculating answer for class {}".format(cls.__name__))
            return 42

    class Sub(Base):
        pass

    class SubSub(Sub):
        pass

    class Subb(Base):
        pass

    print(Base.answer)  # Calculating answer for class Base
    print(Sub.answer)   # Calculating answer for class Sub
    print(Base.answer)  #
    print(SubSub.answer)  # Calculating answer for class SubSub
    print(Sub.answer)
    print(Subb.answer)  # Calculating answer for class Subb
    print(Base.answer)
    print(Subb.answer)

# test_lazyper

# Generated at 2022-06-14 06:39:08.582471
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def property_a(self):
            return 'a'

    class B(A):
        pass

    # Tests
    a = A()
    b = B()
    assert a.property_a == b.property_a
    assert a.property_a != B.property_a
    assert A.property_a != B.property_a
    assert B.property_a == 'a'
    assert A.property_a == 'a'
    assert a.property_a == 'a'
    assert b.property_a == 'a'
    if __name__ == '__main__':
        print('Test passed.')



# Generated at 2022-06-14 06:39:11.534425
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        @lazyclassproperty
        def x(cls):
            return 'test'
    assert MyClass.x == 'test'



# Generated at 2022-06-14 06:39:21.795603
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 42

    class B(A):
        pass

    class C(A):
        pass

    assert A.prop == 42
    assert B.prop == 42
    assert C.prop == 42
    A.prop = 2
    assert A.prop == 2
    assert B.prop == 2
    assert C.prop == 2
    A.prop = 3
    assert A.prop == 3
    assert B.prop == 3
    assert C.prop == 3
    del A.prop
    assert A.prop == 42
    assert B.prop == 42
    assert C.prop == 42


# Generated at 2022-06-14 06:39:30.974401
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        def __init__(self):
            self._color = 'red'

        @lazyperclassproperty
        def color(cls):
            print('eval color for {0}'.format(cls))
            return cls._color

    class B(A):
        pass

    class C(A):
        _color = 'yellow'

    a = A()
    b = B()
    c = C()

    assert a.color == b.color
    assert c.color != b.color
    return True

# Generated at 2022-06-14 06:39:50.057982
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        def __init__(self):
            self._x = None

        def set_x(self, value):
            self._x = value

        @lazyperclassproperty
        def x(cls):
            instance = cls()
            cls.set_x(instance, 5)
            return instance

    class Inheritor(Base):
        @lazyperclassproperty
        def x(cls):
            instance = cls()
            cls.set_x(instance, 6)
            return instance

    assert Base.x._x == 5
    assert Inheritor.x._x == 6

# Generated at 2022-06-14 06:39:54.062329
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def f(cls):
            print("classmethod f called")
            return 1

        @lazyclassproperty
        def g(cls):
            return C.f+1

    assert lazyclassproperty(C.f) == 1
    assert lazyclassproperty(C.g) == 2

# Generated at 2022-06-14 06:40:00.421553
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def value(cls):
            print("Calculation for class A")
            return 1

    class B(A):
        @lazyperclassproperty
        def value(cls):
            print("Calculation for class B")
            return 2

    class C(A):
        @lazyperclassproperty
        def value(cls):
            print("Calculation for class C")
            return 3

    assert A.value == 1
    assert B.value == 2
    assert C.value == 3



# Generated at 2022-06-14 06:40:08.473304
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return 'a'

    class B(A):
        pass

    assert A.a == 'a'
    assert B.a == 'a'
    A.a = 'b'
    assert A.a == 'b'
    assert B.a == 'a'
    B.a = 'c'
    assert A.a == 'b'
    assert B.a == 'c'



# Generated at 2022-06-14 06:40:14.859387
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Person(object):
        _name = None

        @lazyclassproperty
        def name(cls):
            return cls._name

    class Student(Person):
        _name = 'Bob'

    assert Student.name == 'Bob'
    Person.name = 'Alisa'
    assert Student.name == 'Bob'

    class JuniorStudent(Student):
        pass

    assert JuniorStudent.name == 'Bob'



# Generated at 2022-06-14 06:40:18.822628
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class Base(object):

        @lazyclassproperty
        def something(cls):
            print('Computing class property')
            return 42

    class Derived(Base):
        pass

    assert Base.something == 42
    assert Base.something == 42
    assert Derived.something == 42
    assert Derived.something == 42

# end of Unit test for function lazyclassproperty



# Generated at 2022-06-14 06:40:25.942664
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        def __init__(self):
            self.count = 0

        def get_count(self):
            self.count += 1
            return self.count

        @lazyclassproperty
        def count_class(self):
            return self.get_count()

    test = Test()
    assert test.count_class == 1
    assert test.count_class == 1  # check cached
    assert Test.count_class == 1  # check cached
    assert Test.count_class == 1  # check cached

    test2 = Test()
    assert test2.count_class == 1  # check cached
    assert test2.count_class == 1  # check cached
    assert Test.count_class == 1  # check cached

    test.count_class  # increment the instance's count by 1

# Generated at 2022-06-14 06:40:31.004658
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def x(cls):
            print("calculating x")
            return 42

    class B(A):
        pass

    assert A.x == 42
    assert B.x == 42
    assert A.x == 42



# Generated at 2022-06-14 06:40:43.416262
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Bar(object):
        pass

    class Foo(object):
        @lazyperclassproperty
        def bar(self):
            return Bar()

    foo1 = Foo()
    foo2 = Foo()

    assert foo1.bar is foo1.bar
    assert foo2.bar is foo2.bar
    assert foo1.bar is not foo2.bar

    class FooChild(Foo):
        pass

    fooc1 = FooChild()
    fooc2 = FooChild()
    assert fooc1.bar is not foo1.bar
    assert fooc1.bar is fooc1.bar
    assert fooc2.bar is fooc2.bar
    assert fooc1.bar is not fooc2.bar



# Generated at 2022-06-14 06:40:53.143840
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def f(cls):
            return "Test1"

    class B(A):
        @lazyperclassproperty
        def f(cls):
            return "Test2"

    class C(A):
        @lazyperclassproperty
        def f(cls):
            return "Test3"

    assert A.f == "Test1"
    assert B.f == "Test2"
    assert C.f == "Test3"
    assert A.f == "Test1"


# Generated at 2022-06-14 06:41:21.033586
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass(object):
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

        @lazyclassproperty
        def lazy_func(cls):
            print('--> Called lazy_func on class %s' % cls.__name__)
            return cls.arg1 + cls.arg2

    class SubClass(TestClass):
        arg1 = 1
        arg2 = 2

    print('-- 1st call to SubClass.lazy_func')
    print(SubClass.lazy_func)
    print('-- 2nd call to SubClass.lazy_func')
    print(SubClass.lazy_func)



# Generated at 2022-06-14 06:41:32.103115
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self, x):
            self._x = x

        @lazyperclassproperty
        def y(cls):
            return cls._x ** 2

    class B(A):
        def __init__(self, x, y):
            super(B, self).__init__(x)
            self._y = y

        @lazyperclassproperty
        def y(cls):
            return cls._y ** 3

    a = A(2)
    b = B(1, 2)
    assert a.y == 4
    assert b.y == 8
    assert a.y == 4
    assert b.y == 8
    a._x = 3
    b._y = 3
    assert a.y == 9
    assert b.y == 27
    assert a

# Generated at 2022-06-14 06:41:37.965710
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
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



# Generated at 2022-06-14 06:41:47.313738
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Declaring a class attributes lazy
    class A:
        @lazyclassproperty
        def lazy_class_property(cls):
            print(cls.__name__)
            return cls.__name__

    e = A.lazy_class_property
    assert e == "A"
    # the function is called once, even if the attribute is called several times
    f = A.lazy_class_property
    assert f == "A"
    # Subclass inherits lazy attribute
    class B(A):
        pass
    assert B.lazy_class_property == "B"



# Generated at 2022-06-14 06:41:56.533632
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class Foo:

        @lazyclassproperty
        def bar(cls):
            return cls.__name__

    assert Foo.bar == 'Foo'
    assert Foo.__dict__['_lazy_bar'] == 'Foo'

    class Foob(Foo):
        pass

    assert Foob.bar == 'Foob'
    assert Foob.__dict__['_lazy_bar'] == 'Foob'

    try:
        Foob.bar = 'x'
    except AttributeError:
        pass
    else:
        assert False, 'Foob.bar should be read-only'



# Generated at 2022-06-14 06:42:00.830221
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        def __init__(self):
            self.a = 1

        @lazyclassproperty
        def b(cls):
            return self.a + 1

    assert Test.b == 2



# Generated at 2022-06-14 06:42:06.649343
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return 1

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def a(cls):
            return 2

    assert A.a == 1
    assert B.a == 1
    assert C.a == 2



# Generated at 2022-06-14 06:42:11.841863
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class C(object):
        @lazyclassproperty
        def prop(cls):
            """Class property"""
            return cls.__name__

    assert C.prop == 'C'
    assert C.prop == 'C'
    assert not hasattr(C, '_lazy_prop')


# Generated at 2022-06-14 06:42:21.051179
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return [1, 2, 3]

    class B(A):
        pass

    assert A.a is A.a
    assert A.a is not B.a
    assert B.a is B.a
    assert B.a.append(4) is None
    assert A.a == [1, 2, 3]
    assert B.a == [1, 2, 3, 4]



# Generated at 2022-06-14 06:42:31.242469
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Test all of the following:
    # 1) If a class has not yet called the lazyproperty, it should call the function.
    # 2) If a class has called the lazyproperty, it should use the cached result.
    # 3) If a subclass has NOT yet called the lazyproperty, it should use the cached result from the parent.
    # 4) If a subclass has called the lazyproperty, it should use its own cached result.
    class A(object):
        def __init__(self):
            self.n = 0

        @lazyclassproperty
        def n(cls):
            cls.n += 1
            return cls.n

    class B(A):
        pass

    class C(A):
        pass

    assert A.n == 1
    assert B.n == 1
    assert C.n == 1

# Generated at 2022-06-14 06:43:17.317265
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self):
            self.test = 'hello'

        @lazyclassproperty
        def test2(cls):
            test2 = [1, 2, 3]
            print(test2)
            return test2

    class B(A):
        pass

    a = A()
    b = B()

    assert len(b.test2) == len(a.test2)
    assert b.test2 is a.test2



# Generated at 2022-06-14 06:43:27.073857
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class BaseClass(object):
        @lazyperclassproperty
        def lazyprop(cls):
            return cls.__name__
    class DerivedClass(BaseClass):
        pass

    assert BaseClass.lazyprop == 'BaseClass'
    assert DerivedClass.lazyprop == 'DerivedClass'
    BaseClass._BaseClass_lazy_lazyprop = 'Overwritten BaseClass'
    assert BaseClass.lazyprop == 'Overwritten BaseClass'
    assert DerivedClass.lazyprop == 'DerivedClass'


# Generated at 2022-06-14 06:43:32.771051
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def foo(cls):
            return 'Base foo'

    class Sub(Base):
        @lazyperclassproperty
        def foo(cls):
            return 'Sub foo'

    assert Base.foo == 'Base foo'
    assert Sub.foo == 'Sub foo'
    Base.foo = 'Sideways'
    assert Base.foo == 'Sideways'
    assert Sub.foo == 'Sub foo'



# Generated at 2022-06-14 06:43:35.643529
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print("foo")
            return 1

    assert A.foo == 1
    assert A.foo == 1



# Generated at 2022-06-14 06:43:41.843267
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def my_prop(cls):
            return id(cls)

    class B(A):
        pass

    class C(A):
        pass

    assert A.my_prop != B.my_prop
    assert B.my_prop != C.my_prop
    assert A.my_prop != C.my_prop



# Generated at 2022-06-14 06:43:48.831426
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from nose.tools import assert_equals

    class First(object):
        @lazyclassproperty
        def x(cls):
            return 1

    class Second(First):
        @lazyclassproperty
        def x(cls):
            return 2
    
    assert_equals(First.x, 1)
    assert_equals(Second.x, 2)
    assert_equals(First().x, 1)
    assert_equals(Second().x, 2)


# Generated at 2022-06-14 06:43:55.622361
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class TestA(object):
        @lazyperclassproperty
        def d(self):
            return 'd'


    class TestB(TestA):
        pass

    assert TestA().d is TestA().d
    assert TestB().d is TestB().d

    assert TestA().d is TestA().d
    assert TestB().d is TestB().d

    assert TestA().d is TestA().d
    assert TestB().d is TestB().d

    assert TestA().d is not TestB().d



# Generated at 2022-06-14 06:44:02.009022
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def foo(cls):
            print('foo')
            return []

    class B(A):
        pass

    a = A()
    b = B()

    a.foo.append(1)
    assert a.foo == [1]
    assert b.foo == []



# Generated at 2022-06-14 06:44:09.057612
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return type(cls.__name__ + '.x', (object,), {})

    class B(A):
        pass

    assert A.x != B.x
    assert A.x() == A.x()  # x is instantiated only once per class
    assert B.x() == B.x()  # x is instantiated only once per class
    assert A.x() != B.x()



# Generated at 2022-06-14 06:44:16.348574
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class BaseClass(object):
        @lazyperclassproperty
        def prop(cls):
            print("init BaseClass.prop")
            return "BaseClass.prop"

    class DerivedClass(BaseClass):
        pass

    print(BaseClass.prop)
    print(BaseClass.prop)
    print(DerivedClass.prop)
    print(DerivedClass.prop)