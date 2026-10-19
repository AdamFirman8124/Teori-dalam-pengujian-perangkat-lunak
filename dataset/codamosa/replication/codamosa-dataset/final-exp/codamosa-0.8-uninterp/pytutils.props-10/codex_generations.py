

# Generated at 2022-06-14 06:35:48.943593
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    i = 0
    @lazyclassproperty
    def increment():
        nonlocal i
        i += 1
        return i

    assert increment == 1
    assert increment == 1

    @lazyclassproperty
    def increment_perclass():
        nonlocal i
        i += 1
        return i

    assert increment_perclass == 2

    class Cls:
        @lazyclassproperty
        def increment_perclass(cls):
            nonlocal i
            i += 1
            return i

    assert Cls.increment_perclass == 3
    assert Cls.increment_perclass == 3

    class SubCls(Cls):
        pass

    assert SubCls.increment_perclass == 4
    assert SubCls.increment_perclass == 4



# Generated at 2022-06-14 06:35:57.379705
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            x = getattr(cls, "x", 0)
            cls.x = x + 1
            return x
    a_x = A.x
    b_x = A.x
    assert a_x == b_x
    aa = A()
    aaa_x = aa.x
    assert a_x == aaa_x == b_x



# Generated at 2022-06-14 06:36:04.308764
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class TestClass(object):
        @lazyclassproperty
        def test_property(cls):
            print('test_property called')
            return 'test_property_result'

    # lazyclassproperty should call its associated function only once
    assert TestClass.test_property == 'test_property_result'
    assert TestClass.test_property == 'test_property_result'
    assert TestClass.test_property == 'test_property_result'

    # It should be classproperty
    TestClass.test_property = 'test_property_changed'
    assert TestClass.test_property == 'test_property_changed'

    # It should also work with subclasses
    class TestClassSub(TestClass):
        pass

    assert TestClassSub != TestClassSub.test_property


# Generated at 2022-06-14 06:36:17.771077
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A:
        @lazyclassproperty
        def test(self):
            return 1

    assert A.test == 1

    A.test = 2

    assert A.test == 2

    class B(A):
        pass

    assert B.test == 2
    assert B._lazy_test == 2

    B.test = 3
    assert B.test == 3
    assert B._lazy_test == 3
    assert A.test == 2
    assert A._lazy_test == 2

    class C(A):
        pass

    assert C.test == 2
    assert C._lazy_test == 2

    class D(A):
        @lazyclassproperty
        def test(self):
            return 4

    assert D.test == 4
    assert D._lazy_test == 4


# Generated at 2022-06-14 06:36:25.454327
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:36:35.837858
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class SomeClass(object):
        def __init__(self, value):
            self.value = value

        @lazyclassproperty
        def some_class_property(self):
            # We should call this function only once, on first access
            SomeClass.some_class_property.counter += 1
            return SomeClass.some_class_property.counter

        some_class_property.counter = 0

    class SomeSubclass(SomeClass):
        pass

    assert SomeClass.some_class_property == SomeClass.some_class_property == 1
    assert SomeSubclass.some_class_property == SomeSubclass.some_class_property == 2



# Generated at 2022-06-14 06:36:39.910956
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def f(cls):
            return cls.__name__

    assert Test.f == 'Test'
    assert Test.f == 'Test'



# Generated at 2022-06-14 06:36:53.012464
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    import unittest
    class Test(unittest.TestCase):
        @lazyclassproperty
        def a(cls):
            return 'foo'
        @lazyclassproperty
        def b(cls):
            return 'bar'

    t = Test()
    newclass = type('Test1', (Test,), {})
    t1 = newclass()
    assert t.a is Test.a
    assert t.a is not t1.a
    assert t.b is Test.b
    assert t.b is not t1.b
    assert Test.a == 'foo'
    assert Test.b == 'bar'
    assert t1.a == 'foo'
    assert t1.b == 'bar'

# Generated at 2022-06-14 06:36:59.025508
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # Test class
    class A(object):
        @lazyperclassproperty
        def hello(cls):
            return "Hello!"

    # Test inheritance
    class B(A):
        pass

    # Testing
    assert A.hello is "Hello!"
    assert B.hello is "Hello!"
    assert A.hello is not B.hello



# Generated at 2022-06-14 06:37:12.320919
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A():
        @lazyclassproperty
        def x(cls):
            print('calculating x')
            return 1
        @lazyclassproperty
        def y(cls):
            print('calculating y')
            return 2
        @lazyclassproperty
        def z(cls):
            print('calculating z')
            return 3

    assert A.x == A.x
    assert A.y == A.y
    assert A.z == A.z
    assert A.x == A.x

    try:
        A.x = 2
    except Exception as e:
        assert isinstance(e, AttributeError)

    class B(A):
        pass

    assert B.x == B.x
    assert B.y == B.y
    assert B.z == B.z


# Generated at 2022-06-14 06:37:22.657360
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A:
        def __init__(self):
            self.x = "A"

    class B(A):
        def __init__(self):
            super(B, self).__init__()
            self.x = "B"

        @lazyperclassproperty
        def y(self):
            return self.x

    a = A()
    b = B()

    assert(a.y == "A")
    assert(b.y == "B")

    b.x = "C"

    assert(b.y == "C")

# Generated at 2022-06-14 06:37:29.259227
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:37:42.198512
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        def __init__(self, name):
            self.name = name
        
        @lazyperclassproperty
        def test(cls):
            return dict()

    foo1 = Foo('foo1')
    foo2 = Foo('foo2')
    foo3 = Foo('foo3')
    foo4 = Foo('foo4')

    foo1.test["bar1"] = "foobar"
    foo2.test["bar2"] = "foobar2"
    foo3.test["bar3"] = "foobar3"
    foo4.test["bar4"] = "foobar4"

    assert foo1.test["bar1"] == "foobar"
    assert foo2.test["bar2"] == "foobar2"

# Generated at 2022-06-14 06:37:49.911281
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A():
        @lazyperclassproperty
        def x(self):
            return []

    a = A()
    b = A()

    assert a.x is a.x
    assert b.x is b.x
    assert a.x is not b.x

    class B(A):
        @lazyperclassproperty
        def x(self):
            return [1]

    c = B()
    assert c.x == [1]
    assert c.x is c.x



# Generated at 2022-06-14 06:37:56.081132
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object): pass

    class AA(A): pass

    class B(object): pass

    class BB(B): pass

    class Foo(object):

        @lazyperclassproperty
        def bar(cls):
            return cls

    assert Foo.bar is Foo
    assert AA.bar is AA
    assert BB.bar is BB



# Generated at 2022-06-14 06:38:02.839111
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A:

        @lazyclassproperty
        def instance():
            return {}

        @lazyclassproperty
        def mutable(cls):
            return []

        @lazyclassproperty
        def mutable_copy(cls):
            return cls.mutable[:]

    class B(A):
        pass

    assert A.instance is B.instance
    assert A.mutable is B.mutable
    assert A.mutable_copy is not B.mutable_copy



# Generated at 2022-06-14 06:38:11.576533
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    @lazyclassproperty
    def foo(self):
        return 'foo'

    @lazyclassproperty
    def bar(cls):
        return 'bar'

    class TestClass(object):
        foo = foo
        bar = bar

    assert TestClass.foo == 'foo'
    assert TestClass.foo == 'foo'
    assert TestClass.bar == 'bar'
    assert TestClass.bar == 'bar'

    foo.__doc__ = 'foo'
    assert TestClass.foo.__doc__ == 'foo'



# Generated at 2022-06-14 06:38:19.213009
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def foo(cls):
            return 'foo'

    class B(A):
        pass

    class C(B):
        pass

    a = A()
    b = B()
    c = C()

    # Testing the class property
    assert A.foo == 'foo'
    assert B.foo == 'foo'
    assert C.foo == 'foo'

    # Testing the instance properties must raise an exception
    with pytest.raises(AttributeError):
        a.foo
    with pytest.raises(AttributeError):
        b.foo
    with pytest.raises(AttributeError):
        c.foo


# Generated at 2022-06-14 06:38:28.456194
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def available_values(cls):
            return {'a': 1, 'b': 2}

    class B(A):
        pass

    class C(B):
        pass

    assert C.available_values['b'] == 2
    assert A.available_values['b'] == 2
    assert A.available_values['b'] is C.available_values['b']
    assert A.available_values is not B.available_values



# Generated at 2022-06-14 06:38:34.248418
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a_prop(self):
            return 1

    class B(A):
        @lazyperclassproperty
        def a_prop(self):
            return 2

    class C(A):
        pass
    assert A.a_prop == 1
    assert B.a_prop == 2
    assert C.a_prop == 1

# Generated at 2022-06-14 06:38:43.256460
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo:
        @lazyperclassproperty
        def a(cls):
            return 42

    class Bar(Foo):
        pass

    assert Foo().a == 42
    assert Bar().a == 42
    assert Foo().a is not Bar().a


# Generated at 2022-06-14 06:38:48.441858
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def foo(cls):
            cls._foo = 5
            return cls._foo

    class Test2(Test):
        pass

    Test._foo = 10

# Generated at 2022-06-14 06:38:52.335633
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class User(object):
        @lazyclassproperty
        def classes(cls):
            return 'lazy class'

    assert User.classes == 'lazy class'



# Generated at 2022-06-14 06:38:59.787484
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def rand(cls):
            return random.random()

    assert C.rand == C.rand, "Should be cached"
    assert C.rand != C().rand, "Should be different for the class and for the instance"

    class D(C):
        pass

    assert D.rand != C.rand, "Should be different for different classes"
    assert D.rand == D.rand, "Should be cached"



# Generated at 2022-06-14 06:39:05.191097
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def prop(cls):
            print("lazyclassproperty function")
            return "value"

    class SubTest(Test):
        pass

    assert Test.prop == "value"
    assert isinstance(Test.prop, str)
    assert Test.prop is SubTest.prop



# Generated at 2022-06-14 06:39:14.240425
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Test:
        @lazyperclassproperty
        def test(cls):
            return "test"

    class Test2(Test):
        pass

    t1 = Test()
    t2 = Test2()
    assert t1.test == "test"
    assert t2.test == "test"
    assert t1.test is not t2.test
    assert Test.test == "test"
    assert Test2.test == "test"


# Generated at 2022-06-14 06:39:19.632140
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            return 'bar'

    class B(A):
        pass

    class C(A):
        foo = 'baz'

    assert A.foo == 'bar'
    assert B.foo == 'bar'
    assert C.foo == 'baz'



# Generated at 2022-06-14 06:39:25.968789
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:35.387833
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        pass

    class B(A):
        @lazyperclassproperty
        def foo(cls):
            print('Calculate')
            return 2

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        @lazyperclassproperty
        def foo(cls):
            print('Calculate')
            return 3

    print(A.foo)
    print(A.foo)
    print(B.foo)
    print(B.foo)
    print(C.foo)
    print(C.foo)
    print(D.foo)
    print(D.foo)
    print(E.foo)
    print(E.foo)

# Generated at 2022-06-14 06:39:44.030912
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:56.715373
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        _cached_property = "old value"

        @lazyclassproperty
        def cached_property(cls):
            return "new value"

        @staticmethod
        def test():
            assert Foo.cached_property == "new value"
            assert Foo._cached_property == "old value"

    Foo.test()



# Generated at 2022-06-14 06:40:02.747539
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar_prop(self):
            return "bar"

        def __init__(self):
            self.bar = "foo"

    assert Foo.bar_prop == "bar"
    assert Foo().bar == "foo"



# Generated at 2022-06-14 06:40:11.619799
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(object):
        pass

    class Test:
        @lazyperclassproperty
        def prop(cls):
            return 'test'

    assert Test.prop == 'test'
    assert A.prop == 'test'
    assert B.prop == 'test'
    assert C.prop == 'test'
    assert D.prop == 'test'
    assert Test.prop == A.prop == B.prop == C.prop == D.prop


# Generated at 2022-06-14 06:40:15.806609
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class B(object):
        @lazyperclassproperty
        def a(cls):
            """Test lazyperclassproperty"""
            print('first call')
            return 1

    class C(B):
        pass

    class D(B):
        pass

    b = B()
    c = C()
    d = D()
    # call property a in class B
    print(B.a)
    print(b.a)
    # call property a in class C
    print(C.a)
    print(c.a)
    # call property a in class D
    print(D.a)
    print(d.a)



# Generated at 2022-06-14 06:40:25.089625
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from DIRAC.Core.Utilities.ClassAd.ClassAdLight import ClassAd
    class A( object ):
        @lazyclassproperty
        def a( cls ):
            return 'I am a singleton'
        @classproperty
        def b( cls ):
            return 'I am a class constant'

    class B( A ):
        pass

    assert A.a is B.a
    assert A.b is B.b
    assert 'I am a singleton' == A.a
    assert 'I am a class constant' == A.b


# Generated at 2022-06-14 06:40:37.564860
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop(self):
            return 'I am class A'

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def prop(self):
            return 'I am class C'

    class D(A):
        @lazyperclassproperty
        def prop(self):
            return 'I am class D'

    class E(B):
        pass

    class F(C):
        pass

    assert A.prop == 'I am class A'
    assert B.prop == 'I am class A'
    assert C.prop == 'I am class C'
    assert D.prop == 'I am class D'
    assert E.prop == 'I am class A'

# Generated at 2022-06-14 06:40:47.203084
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            return 'bar'

    class B(A):
        pass

    # Check if the property is calculated only once per class
    assert A.foo == 'bar'
    assert B.foo == 'bar'
    # Check if the calculated value is stored in the class
    A.foo = 'not bar'
    assert A.foo == 'not bar'
    assert B.foo == 'bar'
    # Check if the classes do not store the same property
    B.foo = 'baz'
    assert A.foo == 'not bar'
    assert B.foo == 'baz'


# Taken from the `six` library

# Generated at 2022-06-14 06:40:58.601978
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return 1

        def __init__(self):
            self.a_inst = 2

        @property
        def a_prop(self):
            return 3

    class B(A):
        @lazyperclassproperty
        def a(cls):
            return 4

    class C(A):
        pass

    assert A.a == 1
    assert B.a == 4
    assert C.a == 1
    assert A().a_inst == 2
    assert B().a_inst == 2
    assert C().a_inst == 2
    assert A().a_prop == 3
    assert B().a_prop == 3
    assert C().a_prop == 3


# Generated at 2022-06-14 06:41:05.812854
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        a = 1
        @lazyclassproperty
        def c(cls):
            return cls.a + 1
    assert A.c == 2
    A.a = 2
    assert A.c == 3
    class B(A):
        pass
    assert B.c == 3
    B.a = 3
    assert B.c == 4


# Generated at 2022-06-14 06:41:15.722312
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:39.172791
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:48.872802
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self, value):
            self.value = value

        @lazyperclassproperty
        def foo(cls):
            return cls.value * 2

    class B(A):
        value = 2

    class C(A):
        value = 3

    a = A(1)
    b = B(1)
    c = C(1)
    assert a.foo == 2
    assert b.foo == 4
    assert c.foo == 6
    # Test that properties are stored per class
    assert A.foo == 2
    assert B.foo == 4
    assert C.foo == 6

# Generated at 2022-06-14 06:41:56.606682
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def foo(cls):
            print('foo called')
            return 42

    class B(A):
        pass

    class C(A):
        @lazyclassproperty
        def foo(cls):
            print('C.foo called')
            return -1

    assert A.foo == 42
    assert B.foo == 42
    assert C.foo == -1
    assert A.foo == 42
    assert B.foo == 42
    assert C.foo == -1
    assert A.foo == 42



# Generated at 2022-06-14 06:42:04.001584
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    from unittest import TestCase

    class C1(TestCase):
        value = 1

        @lazyperclassproperty
        def calc(cls):
            return cls.value + 1

    class C2(C1):
        value = 2

    class C3(C1):
        pass

    assert C1.calc == 2
    assert C2.calc == 3
    assert C3.calc == 2



# Generated at 2022-06-14 06:42:12.526645
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Dummy(object):
        def __init__(self):
            self._val = 0

        def set_val(self, val):
            self._val = val

        @lazyclassproperty
        def val(cls):
            cls._val = 1
            return cls

        @lazyclassproperty
        def self_val(self):
            self._val = 2
            return self

    Dummy.val
    Dummy.self_val  # will cause AttributeError



# Generated at 2022-06-14 06:42:20.197178
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        _test_value = 1

        @lazyperclassproperty
        def prop(cls):
            return cls._test_value

    class A(Base):
        _test_value = 2

    class B(Base):
        _test_value = 3

    a = A()
    b = B()
    assert a.prop == 2
    assert b.prop == 3


# Generated at 2022-06-14 06:42:31.146027
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def test(cls):
            print("A")
            return 1

    class B(A):
        @lazyclassproperty
        def test(cls):
            print("B")
            return 2

    class C(A):
        @lazyclassproperty
        def test(cls):
            print("C")
            return 3

    class D(B, C):
        @lazyclassproperty
        def test(cls):
            print("D")
            return 4

    class E(C, B):
        @lazyclassproperty
        def test(cls):
            print("E")
            return 5

    class F(D, E):
        @lazyclassproperty
        def test(cls):
            print("F")
            return 6


# Generated at 2022-06-14 06:42:35.975881
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def attr(cls):
            return cls.__name__

    class B(A):
        pass

    assert B.attr == 'B'
    assert A.attr == 'A'



# Generated at 2022-06-14 06:42:45.772314
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Base(object):
        def __init__(self):
            self.x = "dd"

        @lazyperclassproperty
        def foo(cls):
            print("Initializing foo")
            return cls.x

    class Derived(Base):
        def __init__(self):
            super(Derived, self).__init__()
            self.x = "ee"

    print("Base")
    print("Base.foo", Base.foo)
    print("Base.foo", Base.foo)
    print("Base.foo", Base.foo)
    print("")
    print("Derived")
    print("Derived.foo", Derived.foo)
    print("Derived.foo", Derived.foo)
    print("Derived.foo", Derived.foo)

    print("")

# Generated at 2022-06-14 06:42:54.503524
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Item(object):
        @lazyclassproperty
        def foo(cls):
            # print('lazyclassproperty called')
            return 42
    # check that property is created on first usage
    assert Item.__dict__.get('_lazy_foo', False) is False
    # check that it returns value
    assert Item.foo == 42
    # check that it is created
    assert isinstance(Item.__dict__.get('_lazy_foo', None), lazyclassproperty)
    # check that value is stored
    assert Item._lazy_foo == 42



# Generated at 2022-06-14 06:43:41.664265
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        @lazyclassproperty
        def prop(cls):
            print('Initializing class property')
            return []

    assert not hasattr(MyClass, '_lazy_prop')
    assert MyClass.prop == []
    assert MyClass.prop == []
    MyClass.prop.append(1)
    assert MyClass.prop == [1]
    assert MyClass._lazy_prop == [1]
    
    class MySubClass(MyClass):
        def __init__(self):
            self.prop2 = self.prop
    assert MySubClass.prop == [1]
    assert MySubClass().prop2 == [1]


# Generated at 2022-06-14 06:43:53.395423
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    """
    Unit test for the lazyperclassproperty decorator.
    """
    class Base(object):
        @lazyperclassproperty
        def test(cls):
            return [1, 2, 3]

    class Foo(Base):
        pass

    class Bar(Foo):
        pass

    assert Base.test is not Foo.test
    assert Base.test is not Bar.test
    assert Foo.test is not Bar.test

    # Verify that the getter function was called for each class.
    assert Base.test == [1, 2, 3]
    assert Foo.test == [1, 2, 3]
    assert Bar.test == [1, 2, 3]



# Generated at 2022-06-14 06:44:05.825115
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Example(object):

        @lazyclassproperty
        def a(cls):
            return 1

    assert Example.a == 1
    assert isinstance(Example.a, int)
    assert Example.a == 1

    Example.a = 2
    assert Example.a == 2

    class Example(object):
        pass
    assert Example.a == 1

    class Example(object):
        a = 3

    assert Example.a == 3

    class Example(object):
        @lazyclassproperty
        def a(cls):
            return 1

        a = 2

    assert Example.a == 2

    class Example(object):
        pass

    Example.a = 3
    assert Example.a == 3

if __name__ == "__main__":
    test_lazyclassproperty()

# Generated at 2022-06-14 06:44:10.529532
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:44:22.736042
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return "bar"

    class B(A):
        pass

    b = B()

    # Tests
    assert A().foo == "bar"
    assert b.foo == "bar"

    A.foo = "baz"
    assert A().foo == "baz"
    assert b.foo != "baz"
    assert b.foo == "bar"

    class C(A):
        @lazyperclassproperty
        def foo(cls):
            return "qux"

    assert C().foo == "qux"
    assert C().foo == A().foo
    assert b.foo != C().foo



# Generated at 2022-06-14 06:44:32.335607
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        counter = 0

        @lazyclassproperty
        def test_property(cls):
            cls.counter += 1
            return "a"

    assert A.test_property == "a"
    assert A.counter == 1

    # Test that A.test_property caches and doesn't re-run
    assert A.test_property == "a"
    assert A.counter == 1

    class B(A):
        @property
        def test_property(self):
            return "b"

    assert B.test_property == "a"
    assert A.test_property == "a"
    assert A.counter == 1 and B.counter == 1

    assert B.test_property == "a"
    assert A.test_property == "a"
    assert A.counter == 1 and B.counter

# Generated at 2022-06-14 06:44:36.594820
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            return random.random()

    class B(A):
        pass

    assert A.x == A.x
    assert A.x != B.x


# Generated at 2022-06-14 06:44:41.571948
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo:
        def __init__(self, n):
            self.n = n

        @lazyclassproperty
        def bar(cls):
            return 2 + cls.n

    class Baz(Foo):
        def __init__(self):
            super().__init__(3)

    f = Foo(1)
    assert f.bar == 3
    assert '_lazy_bar' in dir(Foo)
    assert '_lazy_bar' not in dir(f)
    assert '_lazy_bar' not in dir(Baz)
    assert '_lazy_bar' not in dir(Baz())

    b = Baz()
    assert b.bar == 5
    assert '_lazy_bar' in dir(Baz)

# Generated at 2022-06-14 06:44:51.618072
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return 'A'
    class B(A):
        @lazyperclassproperty
        def x(cls):
            return 'B'
    class C(A):
        pass
    class D(A):
        @lazyperclassproperty
        def x(cls):
            return 'D'
    class E(A):
        pass
    class F(A):
        pass

    assert A.x == 'A'
    assert B.x == 'B'
    assert C.x == 'A'
    assert D.x == 'D'
    assert E.x == 'A'
    assert F.x == 'A'

# Generated at 2022-06-14 06:44:59.013599
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 1
    class B(A):
        pass
    class C(A):
        pass
    assert A.a == 1
    assert B.a == 1
    assert not hasattr(A, '_lazy_a')
    assert not hasattr(B, '_lazy_a')

