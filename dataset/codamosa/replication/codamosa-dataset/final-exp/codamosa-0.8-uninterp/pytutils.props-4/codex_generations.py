

# Generated at 2022-06-14 06:35:46.670827
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):

        @lazyperclassproperty
        def foo(cls):
            return 'bar'

    class B(A):
        pass

    class C(B):
        pass

    assert A.foo == 'bar'
    assert B.foo == 'bar'
    assert C.foo == 'bar'
    assert A.foo is not B.foo
    assert A.foo is not C.foo
    assert B.foo is not C.foo



# Generated at 2022-06-14 06:35:55.791745
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def testprop(self):
            print("executing testprop ...")
            return "testprop"

        @lazyclassproperty
        def testpropa(self):
            print("executing testpropa ...")
            return "testpropa"

    t = Test()
    print("testprop: {}".format(t.testprop))
    print("testprop: {}".format(t.testprop))
    print("testpropa: {}".format(t.testpropa))
    print("testpropa: {}".format(t.testpropa))
    #
    # OUTPUT
    # -------
    # testprop ...
    # testprop: testprop
    # testprop: testprop
    # testpropa ...
    # testpropa: testpropa


# Generated at 2022-06-14 06:36:05.613582
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    # Tuples of expected values for class A, B, C and D for attributes a, b, c and d
    expected_attrs = ((10, 2), (20, 4))

    class A(object):
        def __init__(self):
            self.cur = 0

        @lazyclassproperty
        def a(cls):
            cls.cur += 1
            return 10 * cls.cur

        @lazyclassproperty
        def b(cls):
            return cls.a // 2

    class B(A, object):
        pass

    class C(object):
        def __init__(self):
            self.cur = 0

        @lazyclassproperty
        def c(cls):
            cls.cur += 1
            return 20 * cls.cur


# Generated at 2022-06-14 06:36:13.178907
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 1
    assert 1 == Foo.bar  # note the property is lazy and gets assigned once
    assert 1 == Foo.bar  # and a second time it returns the cached value
    Foo.bar = 2
    assert 2 == Foo.bar  # we also support assigning a value to the property
    assert 2 == Foo.bar  # and we're still cacheing the value
    assert 'bar' in Foo.__dict__  # we indeed save the value inside the class object
    Foo.__dict__['bar'] = 3  # for fun, you can also set it to the class object
    assert 3 == Foo.bar  # and the value will be returned from it
    assert '__dict__' in Foo.__dict__  # but we don't delete the original Foo.

# Generated at 2022-06-14 06:36:25.126466
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # Call the function with an empty class
    print('Calling function with EmptyClass')
    @lazyperclassproperty
    def function_per_class(EmptyClass):
        print('Inside function with EmptyClass')
        return EmptyClass()
    print(function_per_class)

    # Calling the function with a child class
    print('Calling function with ChildClass')

    class ChildClass(EmptyClass):
        @lazyperclassproperty
        def child_function(ChildClass):
            print('Inside child_function')
            return ChildClass()

    ChildClass().child_function

    # Calling the function with the parent class
    print('Calling function with ParentClass')

    class ParentClass(EmptyClass):
        @lazyperclassproperty
        def parent_function(ParentClass):
            print('Inside parent_function')
            return ParentClass()

   

# Generated at 2022-06-14 06:36:32.314895
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class X(object):
        pass

    class Y(object):
        pass

    x = X()
    y = Y()

    @lazyclassproperty
    def p(cls):
        print("called on class %s" % cls.__name__)
        return set()

    x.p.add(1)
    assert x.p == y.p == set([1])



# Generated at 2022-06-14 06:36:37.084308
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # lazyclassproperty
    class A(object):
        @lazyclassproperty
        def name(cls):
            return cls.__name__

    class B(A):
        pass

    assert A.name == 'A'
    assert B.name == 'B'



# Generated at 2022-06-14 06:36:43.009720
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:36:55.747441
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def foo(cls):
            return str(id(cls))

    class Derived(Base):
        pass

    class Derived2(Base):
        @lazyperclassproperty
        def foo(cls):  # pylint: disable=function-redefined
            return "Meta " + str(id(cls))

    assert Base.foo != Derived.foo
    assert Derived.foo == Derived.foo
    assert Base.__dict__["_Base_lazy_foo"] == Base.foo
    assert Derived.__dict__["_Derived_lazy_foo"] == Derived.foo
    assert str(id(Derived)) == Derived.foo
    assert Derived2.foo == Derived2.foo
    assert Derived2.__

# Generated at 2022-06-14 06:36:59.266273
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class TestProperties:

        @lazyclassproperty
        def Foo(cls):
            print('Foo')
            return 'Bar'

    print(TestProperties.Foo)
    print(TestProperties.Foo)



# Generated at 2022-06-14 06:37:04.965249
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        @lazyperclassproperty
        def prop(cls):
            return cls.__name__

    class Bar(Foo):
        pass

    assert Foo.prop == Foo.__name__
    assert Bar.prop == Bar.__name__


# Generated at 2022-06-14 06:37:11.771744
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class C1(object):
        @lazyperclassproperty
        def C1_lazy_name(cls):
            return 'C1_lazy_name'

    class C2(C1):
        pass

    c1 = C1()
    c2 = C2()

    assert c1.C1_lazy_name == 'C1_lazy_name'
    assert c2.C1_lazy_name == 'C1_lazy_name'
    assert C1.C1_lazy_name == 'C1_lazy_name'
    assert C2.C1_lazy_name == 'C1_lazy_name'

    assert c1._C1_lazy_C1_lazy_name == 'C1_lazy_name'
    assert c2._C2_

# Generated at 2022-06-14 06:37:21.607138
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def b(cls):
            return 'b'

    assert A.b == 'b'

    class B1(A):
        pass

    class B2(A):
        pass

    assert B1.b == 'b'
    assert B2.b == 'b'
    assert B1.b is B2.b

    A.b = 'c'

    assert A.b == 'c'
    assert B1.b != 'c'
    assert B2.b != 'c'



# Generated at 2022-06-14 06:37:32.411698
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        # This should return base_a for Base and BaseV2, base_b for BaseV3, BaseV4 and BaseV5
        @lazyperclassproperty
        def a(cls):
            if(cls == Base):
                return "base_a"
            elif(cls == BaseV3):
                return "base_b"
            elif(cls == BaseV4):
                return "base_b"
            elif(cls == BaseV5):
                return "base_b"

    class BaseV2(Base):
        pass

    class BaseV3(Base):
        pass

    class BaseV4(BaseV3):
        pass

    class BaseV5(BaseV4):
        pass

    assert(Base.a == "base_a")

# Generated at 2022-06-14 06:37:42.393290
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:37:46.664932
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print('foo')
            return 'foo'

    assert A.foo == 'foo'
    assert A.foo == 'foo'



# Generated at 2022-06-14 06:37:59.234990
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        @lazyperclassproperty
        def prop(cls):
            return 'classprop_A'

    class B(A):
        @lazyperclassproperty
        def prop(cls):
            return 'classprop_B'

    class C(A):
        @lazyclassproperty
        def prop(cls):
            return 'classprop_C'

    a = A()
    b = B()
    c = C()
    assert a.prop == 'classprop_A'
    assert b.prop == 'classprop_B'
    assert a.prop == 'classprop_A'
    assert a.__class__.prop == 'classprop_A'
    assert b.__class__.prop == 'classprop_B'
    assert C.prop == 'classprop_C'


# Generated at 2022-06-14 06:38:02.218522
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return print('Do something expensive here!')

    Foo.bar()
    Foo.bar()
    Foo.bar()



# Generated at 2022-06-14 06:38:12.343583
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):

        @lazyclassproperty
        def x(cls):
            return 'hi'

        @lazyclassproperty
        def y(cls):
            return 'bye'

    assert A.x == 'hi'
    assert A.y == 'bye'

    class B(A):
        pass

    assert B.x == 'hi'
    assert B.y == 'bye'
    assert A.x == 'hi'
    assert A.y == 'bye'

    # Let's break it
    A.x = 'modified'
    assert B.x == 'hi'



# Generated at 2022-06-14 06:38:15.143917
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def test(cls):
            print("Ok, lazyclassproperty works")
            return 5

    assert A.test == 5



# Generated at 2022-06-14 06:38:29.511346
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A:

        @lazyperclassproperty
        def test(cls):
            return 'A'

    class B(A):

        @lazyperclassproperty
        def test(cls):
            return 'B'

    class C(A):

        def test(cls):
            return 'C'

    assert A.test == 'A'
    assert B.test == 'B'
    assert C.test == 'C'

    assert A().test == 'A'
    assert B().test == 'B'
    assert C().test == 'C'


# Generated at 2022-06-14 06:38:38.314960
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        @lazyperclassproperty
        def prop(cls):
            print("computing for A")
            return "AA"

    class B(A):
        @lazyperclassproperty
        def prop(cls):
            print("computing for B")
            return "BB"

    class C(A):
        @lazyperclassproperty
        def prop(cls):
            print("computing for C")
            return "CC"

    print("\nTesting lazyperclassproperty")
    print("A.prop: ", A.prop)
    print("B.prop: ", B.prop)
    print("C.prop: ", C.prop)

    print("\nTesting lazyperclassproperty with C")
    print("C.prop: ", C.prop)

# Generated at 2022-06-14 06:38:48.614679
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Base(object):
        counter = 0
        @lazyclassproperty
        def number(cls):
            cls.counter += 1
            return cls.counter
    class Sub1(Base):pass
    class Sub2(Base):pass
    assert Base.number == 1
    assert Sub1.number == 2
    assert Sub2.number == 3

    assert Base.number == 1
    assert Base.number == 1

    assert Sub1.number == 2
    assert Sub1.number == 2

    assert Sub2.number == 3
    assert Sub2.number == 3

    assert Base.number == 1
    assert Sub1.number == 2
    assert Sub2.number == 3



# Generated at 2022-06-14 06:39:01.483848
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:39:05.804046
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def value(cls):
            print('evaluating')
            return 42

    assert Test.value == 42
    assert Test.value == 42

    class Test2(Test):
        pass

    assert Test2.value == 42



# Generated at 2022-06-14 06:39:14.068009
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from time import time
    from random import randrange

    class X(object):
        def __init__(self, val):
            self._val = val
        @lazyclassproperty
        def randval(cls):
            """
            This returns a random value
            """
            return randrange(0, 1000)


    t1 = time()
    for i in range(50000):
        x = X(i)
        assert X.randval == x.randval
    t2 = time()
    assert t2-t1 < 0.6



# Generated at 2022-06-14 06:39:24.228106
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    """
    Test for function lazyperclassproperty.
    """

# Generated at 2022-06-14 06:39:31.010676
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:43.372351
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        pass

    class Derived(Base):
        pass

    class SomeClass(object):
        def __init__(self):
            print("SomeClass.__init__")
            self.data = {}

        def init(self):
            print("SomeClass.init")
            self.data["init"] = True

        @lazyperclassproperty
        def prop(cls):
            print("SomeClass.prop")
            res = SomeClass()
            res.init()
            return res

    # Test
    assert not hasattr(Base, "_Base_lazy_prop")
    assert not hasattr(Derived, "_Derived_lazy_prop")
    assert Base.prop.data == {}
    assert Base.prop.data == Derived.prop.data



# Generated at 2022-06-14 06:39:51.486248
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class SomeClass(object):
        @lazyclassproperty
        def some_prop(cls):
            return SomeClass.__name__

        @lazyclassproperty
        def some_other_prop(cls):
            return cls.__name__

    class SomeSubclass(SomeClass):
        pass

    o = SomeClass()
    o2 = SomeSubclass()

    assert o.some_prop == SomeClass.__name__
    assert o2.some_prop == SomeClass.__name__
    assert o2.some_other_prop == SomeSubclass.__name__



# Generated at 2022-06-14 06:40:05.987334
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:40:16.699055
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    global counter
    counter = 0

    class TestClass(object):
        @lazyclassproperty
        def testprop(cls):
            global counter
            counter += 1
            return counter

    assert not hasattr(TestClass, '_lazy_testprop')
    assert TestClass.testprop == 1
    assert hasattr(TestClass, '_lazy_testprop')
    assert TestClass.testprop == 1

    class AnotherTestClass(TestClass):
        pass

    assert not hasattr(AnotherTestClass, '_lazy_testprop')
    assert AnotherTestClass.testprop == 2
    assert hasattr(AnotherTestClass, '_lazy_testprop')
    assert AnotherTestClass.testprop == 2


# Generated at 2022-06-14 06:40:22.429282
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    """
       Simple test to check if the lazyperclassproperty works as expected
       There not are a lot of variations possible but this checks one important:
       that the lazyperclassproperty allows to extend the property with
       child classes without overriding the values of the parent
    """
    class Base:
        @lazyperclassproperty
        def myprop(cls):
            return 3

    class Child(Base):
        @lazyperclassproperty
        def myprop(cls):
            return 4

    assert Base.myprop == 3
    assert Child.myprop == 4



# Generated at 2022-06-14 06:40:27.611104
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    import unittest

    class Test(unittest.TestCase):
        def test_lazyperclassproperty(self):
            class A:
                @lazyperclassproperty
                def test(cls):
                    return cls.__name__

            class B(A):
                pass

            self.assertEqual(A.test, 'A')
            self.assertEqual(B.test, 'B')


# Generated at 2022-06-14 06:40:37.209634
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:40:47.670238
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # Try this module
    assert hasattr(pydispatch.__class__, '_lazy_dispatcher_names')
    # Try a synthetic class
    class A:
        @lazyperclassproperty
        def foo(cls):
            return 5
    class B(A):
        pass
    class C:
        pass

    assert A._A_lazy_foo == 5
    assert B._B_lazy_foo == 5
    assert not hasattr(A, '_B_lazy_foo')
    assert not hasattr(B, '_A_lazy_foo')
    assert not hasattr(C, '_C_lazy_foo')
    assert not hasattr(C, '_A_lazy_foo')


if __name__ == "__main__":
    test_lazyperclass

# Generated at 2022-06-14 06:40:52.627361
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):

        @lazyperclassproperty
        def attr(cls):
            return cls.__name__

    class B(A):

        pass

    assert A.attr == 'A'
    assert B.attr == 'B'



# Generated at 2022-06-14 06:41:02.658101
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def x(cls):
            print('A.x')
            return 123

    class B(A):
        pass

    print(A.x)
    print(B.x)
    print(A.x)
    print(B.x)

    print(A._lazy_x)
    print(B._lazy_x)
    print(A._lazy_x)
    print(B._lazy_x)

    assert A.x == 123
    assert B.x == 123

    A._lazy_x = 1
    print(A.x)
    print(B.x)
    print(A.x)
    print(B.x)

    assert A.x == 1
    assert B.x == 123



# Generated at 2022-06-14 06:41:12.768556
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class ChildClass(SuperClass):
        @lazyperclassproperty
        def prop_func(cls):
            return {cls: "from a ChildClass instance"}

    class SuperClass(object):
        @lazyperclassproperty
        def prop_func(cls):
            return {cls: "from a SuperClass instance"}

    super_instance = SuperClass()
    child_instance = ChildClass()
    super_instance2 = SuperClass()
    child_instance2 = ChildClass()

    print(super_instance.prop_func)
    print(child_instance.prop_func)
    print(child_instance2.prop_func)
    print(super_instance2.prop_func)


# Generated at 2022-06-14 06:41:20.226177
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def dictProp(cls):
            print('Init Base')
            return {}


    class Derived(Base):
        @lazyperclassproperty
        def dictProp(cls):
            print('Init Derived')
            return {}


    assert Base.dictProp != Derived.dictProp
    Derived.dictProp['x'] = 1
    assert 'x' in Derived.dictProp
    assert 'x' not in Base.dictProp



# Generated at 2022-06-14 06:41:46.821422
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from time import time
    class A(object):
        @lazyclassproperty
        def time(self):
            return time()
    # Should return the same for any instance
    assert A().time == A().time
    class B(A): pass
    assert A().time == B().time
    # Check if cached
    t1 = A().time
    sleep(2)
    t2 = A().time
    assert t1 == t2
    # Check if lazy
    class C(A):
        @lazyclassproperty
        def time(self):
            return time()
    sleep(2)
    assert A().time == C().time



# Generated at 2022-06-14 06:41:54.232955
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    def get_x(obj):
        return 'x'

    @lazyclassproperty
    def x(cls):
        return get_x(cls)

    class A(object):
        pass

    class B(A):
        pass

    assert A.x == 'x'
    assert B.x == 'x'

    A.x = 'y'
    assert A.x == 'y'
    assert B.x == 'x'



# Generated at 2022-06-14 06:42:07.260090
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Test for class property
    @lazyclassproperty
    def lazyclass(cls):
        print("In lazyclass")
        return cls.__name__
    class A:
        def test_classprop(cls):
            assert cls.lazyclass == "A"
    A.test_classprop()
    # Test for instance property
    class A:
        @lazyclassproperty
        def lazyclass(cls):
            return cls.__name__
    a = A()
    assert a.lazyclass == "A"
    assert a.lazyclass == "A" # second access should not call the method

    # Test for inheritor
    class A:
        @lazyclassproperty
        def lazyclass(cls):
            return cls.__name__
    class B(A): pass
   

# Generated at 2022-06-14 06:42:11.895320
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo:
        @lazyclassproperty
        def prop(cls):
            print('called')
            return 'the result'


    obj = Foo()
    assert Foo.prop == 'the result'
    assert Foo.prop == 'the result'



# Generated at 2022-06-14 06:42:18.721909
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def prop(cls):
            return 'Base'

    class Inheritor1(Base):
        pass

    class Inheritor2(Base):
        @lazyperclassproperty
        def prop(cls):
            return 'Inheritor2'

    assert_equal(Base.prop, 'Base')
    assert_equal(Inheritor1.prop, 'Base')
    assert_equal(Inheritor2.prop, 'Inheritor2')



# Generated at 2022-06-14 06:42:28.715625
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return "A"

    assert A.a == "A"
    assert "a" not in A.__dict__

    class B(A):
        @lazyperclassproperty
        def a(cls):
            return "B"

    assert A.a == "A"
    assert B.a == "B"
    assert "a" not in A.__dict__
    assert "a" not in B.__dict__

    assert A().a == "A"
    assert B().a == "B"

    del A.a
    assert "a" not in A.__dict__



# Generated at 2022-06-14 06:42:42.274520
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    def value(cls):
        print("value(%s)" % cls.__name__)
        return 1

    class A(object):
        a = 2

        @lazyperclassproperty
        def v1(cls):
            print("v1(%s)" % cls.__name__)
            return "v1(%s)" % cls.__name__

        @lazyperclassproperty
        def v2(cls):
            print("v2(%s)" % cls.__name__)
            return value(cls)

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass

    # A, B, C and D should have different internal attributes.

# Generated at 2022-06-14 06:42:48.336498
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:42:58.687953
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:43:03.132927
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        a = 1

        @lazyclassproperty
        def x(cls):
            return cls.a + 1

    assert A.__dict__ == {'__module__': __name__, 'a': 1, '_lazy_x': 2}


# Generated at 2022-06-14 06:43:45.431356
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        def __init__(self):
            self.called = False

        @lazyclassproperty
        def prop(cls):
            self = cls()
            self.called = True
            return self

    a = A()
    assert not a.called
    p = a.prop
    assert p.called
    p = a.prop
    assert p.called
    assert p is a.prop



# Generated at 2022-06-14 06:43:49.763232
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:43:56.570775
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class FooParent(object):
        @lazyperclassproperty
        def props(self):
            print("FooParent.props has been called")
            return ["test"]
    class FooChild(FooParent):
        pass

    foo_parent = FooParent()
    print(foo_parent.props) # ["test"]

    foo_parent2 = FooParent()
    print(foo_parent2.props) # ["test"]

    foo_child = FooChild()
    print(foo_child.props) # []



# Generated at 2022-06-14 06:44:03.415924
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        l = 1
        @lazyclassproperty
        def foo(cls):
            cls.l += 1
            return cls.l
    class B(A):
        pass
    assert A().foo == 2
    assert B.foo == 2
    assert A.foo == 2
    assert B().foo == 2
    assert A.foo == 2
    assert B.foo == 2

# Generated at 2022-06-14 06:44:08.963972
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def test(cls):
            return cls.__name__ + '_1'
    class B(A):
        @lazyperclassproperty
        def test(cls):
            return cls.__name__ + '_2'

    assert A.test == 'A_1'
    assert B.test == 'B_2'



# Generated at 2022-06-14 06:44:19.703970
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from unittest import TestCase

    class TestLazyClassProp(TestCase):

        @lazyclassproperty
        def prop(cls):
            return cls.__name__

        def test_lazyclassproperty(self):
            self.assertEqual(TestLazyClassProp.prop, 'TestLazyClassProp')

        class SubTestLazyClassProp(TestLazyClassProp):
            pass

        def test_lazyclassproperty_inherit(self):
            self.assertEqual(self.SubTestLazyClassProp.prop, 'SubTestLazyClassProp')



# Generated at 2022-06-14 06:44:29.073049
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Example on usage
    class A(object):
        @lazyclassproperty
        def xyz(cls):
            print('called')
            return "xyz"

    class B(A):
        pass

    assert A.xyz == B.xyz == "xyz"

    # Try it twice to see that the function is called once.
    # (Which means the property is lazy)
    assert A.xyz == B.xyz == "xyz"

    # Instances DO NOT have the property.
    assert not hasattr(A(), 'xyz')
    assert not hasattr(B(), 'xyz')



# Generated at 2022-06-14 06:44:37.213311
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:44:47.233549
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def _foo(cls):
            print('_foo called')
            return 'foo'

        foo = lazyclassproperty(_foo)

        def _bar(cls):
            print('_bar called')
            return 'bar'

        bar = lazyclassproperty(_bar)

    assert A.foo == 'foo'
    assert A.foo == 'foo'
    assert A.bar == 'bar'

    class B(A):
        pass

    assert B.foo == 'foo'
    assert B.bar == 'bar'
    


# Generated at 2022-06-14 06:44:53.162731
# Unit test for function lazyclassproperty