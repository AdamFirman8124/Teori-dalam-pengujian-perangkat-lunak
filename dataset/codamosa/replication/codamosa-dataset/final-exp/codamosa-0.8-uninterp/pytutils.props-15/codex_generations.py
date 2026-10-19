

# Generated at 2022-06-14 06:35:39.710277
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def msg(self):
            print('hello world')
            return 'hello world'

    assert A.msg == 'hello world'
    A.msg
    A.msg
    A.msg



# Generated at 2022-06-14 06:35:47.624806
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def prop(cls):
            return 'some_value'

    class Derived(Base):
        pass

    class Derived2(Base):
        pass

    assert Base._Base_lazy_prop == 'some_value'
    assert Base.prop == 'some_value'
    assert Derived._Derived_lazy_prop == 'some_value'
    assert Derived.prop == 'some_value'
    assert Derived2._Derived2_lazy_prop == 'some_value'
    assert Derived2.prop == 'some_value'



# Generated at 2022-06-14 06:35:55.776647
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:36:02.980775
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from unittest import TestCase
    class Test(TestCase):
        @lazyclassproperty
        def x(cls):
            return 'x'
        @lazyclassproperty
        def y(cls):
            return 'y'
        def test_same(self):
            self.assertEqual(Test.x, Test.x)
            self.assertEqual(Test.x, 'x')
            self.assertEqual(Test.y, Test.y)
            self.assertEqual(Test.y, 'y')

    Test().test_same()


# Generated at 2022-06-14 06:36:11.882741
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # Test the property using a single class
    class DummyClass(object):
        @lazyperclassproperty
        def my_prop(cls):
            print("my_prop ran for %s" % cls.__name__)
            return 1

    dummy1 = DummyClass()
    dummy2 = DummyClass()

    print(dummy1.my_prop)  # my_prop ran for DummyClass
    print(dummy2.my_prop)  # Output: 1

    # Test the property using inheritance
    class InheritedDummyClass(DummyClass):
        pass

    inher1 = InheritedDummyClass()
    inher2 = InheritedDummyClass()

    print(inher1.my_prop)  # my_prop ran for InheritedDummyClass
    print(inher2.my_prop)

# Generated at 2022-06-14 06:36:18.958981
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return id(cls)
    class B(A):
        pass
    class C(A):
        pass

    assert A.a != B.a
    assert A.a != C.a
    assert B.a != C.a


# Generated at 2022-06-14 06:36:24.011933
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            """This is the doc string for prop."""
            print("Initializing prop")
            return 1

    assert A.prop.__doc__ == "This is the doc string for prop."
    assert A.prop == 1
    assert A.prop == 1
    #print(A.__dict__)



# Generated at 2022-06-14 06:36:36.939226
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:36:41.821070
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def b(cls):
            return {'a': 1}
    a = A()
    assert a.b['a'] == 1
    assert a.b == A.b
    assert a.b is A.b



# Generated at 2022-06-14 06:36:54.760686
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Create class with lazy class variable
    @lazyclassproperty
    def lazy_var(cls):
        return "lazy_var"

    # Example of using
    class A(object):
        pass

    a = A()

    # Calling before use
    try:
        print(a.lazy_var)
    except AttributeError:
        pass

    # Getting value
    b = A()
    print(b.lazy_var)
    # Assigning new value
    b.lazy_var = "new value"
    print(b.lazy_var)
    # Getting value for another instance. Should be the same, because cached
    print(a.lazy_var)


if __name__ == "__main__":
    test_lazyclassproperty()

# Generated at 2022-06-14 06:37:03.549556
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 1

    assert Foo.bar == 1

    # Subclassing
    class Bar(Foo):
        pass

    assert Bar.bar == 1

    # Set Foo.bar to a new value, Bar.bar should stay the same
    Foo.bar = 2
    assert Bar.bar == 1

# Generated at 2022-06-14 06:37:11.273503
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            print("Computing x")
            return 1

    class B(A):
        pass

    class C(A):
        @lazyclassproperty
        def x(cls):
            print("Computing x")
            return 2

    assert A.x == 1
    assert B.x == 1
    assert C.x == 2


# Generated at 2022-06-14 06:37:18.830054
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def foo(cls):
            return "bar"


# Generated at 2022-06-14 06:37:26.527720
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C:
        @lazyclassproperty
        def x(cls):
            return 1
    assert C.x == 1

    class C2(C):
        pass
    assert C2.x == 1

    assert C2._lazy_x == 1
    assert C2._lazy_x is not C._lazy_x
    assert C.x == C2.x
    assert C.x is not C2.x
    assert C2.x is C2._lazy_x



# Generated at 2022-06-14 06:37:33.120885
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self):
            self.name = "A"

        @lazyperclassproperty
        def get_classname(cls):
            return cls.__name__

    class B(A):
        def __init__(self):
            self.name = "B"

    a = A()
    assert a.get_classname == "A"
    b = B()
    assert b.get_classname == "B"



# Generated at 2022-06-14 06:37:41.711387
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def prop(cls):
            return prop

        @lazyclassproperty
        def prop2(cls):
            return [prop2, prop]

    assert Test.prop is Test.prop
    assert Test.prop2 is Test.prop2
    assert Test.prop2[0] is Test.prop2[0]
    assert Test.prop2[1] is Test.prop2[1]
    assert Test.prop2[1] is not Test.prop2[0]



# Generated at 2022-06-14 06:37:49.443447
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def test_prop(cls):
            print("Assigning value 1 to A.test_prop")
            return 1

    class B(A):
        @lazyperclassproperty
        def test_prop(cls):
            print("Assigning value 2 to B.test_prop")
            return 2

    print("A.test_prop = ",A.test_prop)
    print("B.test_prop = ",B.test_prop)


# Generated at 2022-06-14 06:38:00.883494
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A:
        @lazyclassproperty
        def x(cls):
            print("in x")
            return 0

        @lazyclassproperty
        def y(cls):
            print("in y")
            return 1

    print("A.x =", A.x)
    print("A.y =", A.y)
    print("A.x =", A.x)
    print("A.y =", A.y)

    class B(A):
        pass
    print("B.x =", B.x)
    print("B.y =", B.y)
    print("B.x =", B.x)
    print("B.y =", B.y)


# Generated at 2022-06-14 06:38:06.405750
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:38:17.912413
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class MyClass():
        @lazyclassproperty
        def myclass_attr(cls):
            print("calculating myclass_attr")
            return 1

    class MyClass2(MyClass):
        pass

    assert MyClass.myclass_attr == 1
    assert MyClass.myclass_attr == 1
    assert MyClass.myclass_attr == 1
    assert MyClass.myclass_attr == 1
    assert MyClass2.myclass_attr == 1
    assert MyClass2.myclass_attr == 1
    assert MyClass2.myclass_attr == 1
    assert MyClass2.myclass_attr == 1

    @lazyclassproperty
    def app_settings(cls):
        return dict(a=1, b=2)

    class MyClass3():
        pass


# Generated at 2022-06-14 06:38:30.430312
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass:
        @lazyclassproperty
        def prop(cls):
            print("Executing original function")
            return "original value"

    print("Testing lazy class properties")
    print("Original property value of MyClass:", MyClass.prop)
    print("Changing property to 'new value'")
    MyClass.prop = "new value"
    print("New value of property", MyClass.prop)


# ===============
# Decorators
# ===============



# Generated at 2022-06-14 06:38:40.113297
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class C1:
        @lazyperclassproperty
        def p1(cls):
            return "C1"
        @lazyperclassproperty
        def p2(cls):
            return "C1 as well"

    class C2(C1):
        @lazyperclassproperty
        def p2(cls):
            return "C2"

    assert C1.p1 == 'C1'
    assert C1.p2 == 'C1 as well'

    assert C2.p1 == 'C1'
    assert C2.p2 == 'C2'


# Generated at 2022-06-14 06:38:53.346128
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def test_prop(cls):
            print('computing test_prop for %s' % cls.__name__)
            return 'computed'

    class Derived1(Base):
        pass

    class Derived2(Base):
        pass

    assert Base().test_prop == 'computed'
    assert Derived1().test_prop == 'computed'
    assert Derived2().test_prop == 'computed'

    # The @lazyperclassproperty decorator should have created a separate (cached)
    # property for each of the classes.
    assert hasattr(Base, '_Base_lazy_test_prop')
    assert hasattr(Derived1, '_Derived1_lazy_test_prop')

# Generated at 2022-06-14 06:38:58.239860
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def ap(cls):
            return type("A", (object,), {})

    class B(object):
        @lazyperclassproperty
        def bp(cls):
            return type("B", (object,), {})

    assert not A.ap is B.bp
    assert not A.ap is A.bp
    assert not B.ap is B.bp



# Generated at 2022-06-14 06:39:03.561519
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:15.531992
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Base(object):
        pass

    class A(Base):
        @lazyperclassproperty
        def foo(cls):
            return "foo from A"

    class B(Base):
        @lazyperclassproperty
        def foo(cls):
            return "foo from B"

    class C(Base):
        @lazyperclassproperty
        def foo(cls):
            return "foo from C"

    class D(C):
        pass

    assert A.foo == "foo from A"
    assert B.foo == "foo from B"
    assert C.foo == "foo from C"
    assert D.foo == "foo from C"


# Generated at 2022-06-14 06:39:18.796074
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(self):
            return 'prop'
    assert A.prop == 'prop'
    A.prop = 2
    assert A.prop == 2

# Generated at 2022-06-14 06:39:27.146646
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return None

    class B(A):
        pass

    class C(B):
        pass

    class D(A):
        pass

    assert A.x is B.x
    assert A.x is D.x
    assert A.x is not C.x
    assert B.x is not C.x
    assert C.x is D.x

    A.x = 'A'
    assert A.x == 'A'
    assert B.x == 'A'
    assert D.x == 'A'
    assert C.x is None

    C.x = 'C'
    assert A.x == 'A'
    assert B.x == 'A'
    assert D.x == 'A'

# Generated at 2022-06-14 06:39:35.174034
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    print('Run test_lazyclassproperty')
    class Foo(object):

        @lazyclassproperty
        def bar(cls):
            print('calling bar()')
            return "bar"

    class FooChild(Foo):
        pass

    print('test app')
    a_foo = Foo()
    a_foo_child = FooChild()
    print('a_foo.bar:', a_foo.bar)
    print('a_foo_child.bar:', a_foo_child.bar)
    print('Foo.bar:', Foo.bar)
    print('FooChild.bar:', FooChild.bar)


# Generated at 2022-06-14 06:39:42.576570
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self, x):
            self.x = x

    class B(A):
        pass

    class C(A):
        pass

    class Foo(object):
        @lazyperclassproperty
        def _per_class(self):
            return self.x

    assert A(1)._per_class == 1
    assert A(2)._per_class == 2
    assert B(1)._per_class == 1
    assert B(2)._per_class == 2
    assert C(1)._per_class == 1
    assert C(2)._per_class == 2



# Generated at 2022-06-14 06:39:56.528336
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    @lazyperclassproperty
    def lazy_class_data(cls):
        print('Called lazy_class_data')
        return object()

    class Base(object):
        x = lazy_class_data

    class A(Base):
        pass

    class B(Base):
        pass

    assert Base.x is not A.x
    assert Base.x is not B.x
    assert A.x is not B.x



# Generated at 2022-06-14 06:40:05.006699
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass(object):
        val = 0
        @lazyclassproperty
        def x(cls):
            cls.val += 1
            return cls.val
    assert TestClass.x == 1
    assert TestClass.x == 1

    class SubTestClass(TestClass):
        pass
    assert SubTestClass.x == 2
    assert SubTestClass.x == 2

    assert TestClass.x == 1
    assert TestClass.x == 1



# Generated at 2022-06-14 06:40:08.847207
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        foo = None

    class B(A):
        @lazyclassproperty
        def foo(cls):
            return "bar"

    assert B.foo == "bar"
    assert A.foo == None



# Generated at 2022-06-14 06:40:14.054961
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    def add_one(no):
        return no + 1

    class TestClass(object):
        @lazyclassproperty
        def add_one(self):
            return add_one(1)

    assert hasattr(TestClass, '_lazy_add_one')
    assert hasattr(TestClass, 'add_one')



# Generated at 2022-06-14 06:40:21.206495
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    assert not hasattr(Base, '_lazy_base')
    Base.base
    assert hasattr(Base, '_lazy_base')
    Inherited.base
    assert len([b for b in dir(Inherited) if b.startswith('_lazy_')]) == 1
    assert hasattr(Inherited, '_lazy_base')



# Generated at 2022-06-14 06:40:23.070382
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def prop(cls):
            # print 'fetching prop'
            return 42
    assert C.prop == 42



# Generated at 2022-06-14 06:40:26.394107
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def foo(cls):
            print("Foo assigned")
            return 12

    class B(A):
        @lazyperclassproperty
        def foo(cls):
            print("Foo assigned")
            return 13

    assert A.foo == 12
    assert B.foo == 13
    assert A.foo == 12
    assert B.foo == 13

# Generated at 2022-06-14 06:40:37.948865
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def val(cls):
            attr_name = '_%s_lazy_val' % cls.__name__
            print('%s: evaluating %s on %s' % (attr_name, cls.__name__, cls))
            setattr(cls, attr_name, 1)
            return 1
    class B(A):
        pass
    class C(A):
        pass
    print('A:', A.val)
    print('B:', B.val)
    print('C:', C.val)
    print('A:', A.val)
    print('B:', B.val)
    print('C:', C.val)


# Generated at 2022-06-14 06:40:41.617746
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Imports
    import doctest
    # Test
    print('Running doctests on function lazyclassproperty...')
    doctest.testmod(verbose=True)
    print('Done.')



# Generated at 2022-06-14 06:40:49.057822
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 'value'
    assert A.prop == 'value'
    assert A._lazy_prop == 'value'
    assert A.prop == 'value'
    assert A._lazy_prop == 'value'
    assert '_lazy_prop' in A.__dict__
    class B(A):
        @lazyclassproperty
        def prop(cls):
            return 'newvalue'
    assert A.prop == 'value'
    assert A._lazy_prop == 'value'
    assert B.prop == 'newvalue'
    assert B._lazy_prop == 'newvalue'
    assert '_lazy_prop' in B.__dict__
    class C(A):
        pass

# Generated at 2022-06-14 06:41:12.521808
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def a(cls):
            print('A init')
            return 1

    class B(A):
        pass

    assert A.a == 1
    assert B.a == 1
    print('---- test ----')
    assert A.a == 1



# Generated at 2022-06-14 06:41:19.540909
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class X():
        @lazyclassproperty
        def x(cls):
            return 1

        @lazyclassproperty
        def y(cls):
            return 2

    class Y(X):
        @lazyclassproperty
        def y(cls):
            return 3


# Generated at 2022-06-14 06:41:31.677243
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return 5

    class B(A):
        pass

    assert A().x == 5
    assert A().x == 5
    assert B().x == 5
    assert B().x == 5
    assert not hasattr(A, '_x')
    assert hasattr(A, '_A_lazy_x')
    assert not hasattr(B, '_x')
    assert hasattr(B, '_B_lazy_x')

    class C(A):
        @lazyperclassproperty
        def x(cls):
            return 10

    assert A().x == 5
    assert B().x == 5
    assert C().x == 10
    assert A().x == 5
    assert B().x == 5
    assert C

# Generated at 2022-06-14 06:41:37.239751
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop_a(cls):
            return "a"

    assert A.prop_a == "a"
    assert A._lazy_prop_a == "a"

    class B(A):
        pass

    assert B.prop_a == "a"
    assert not hasattr(B, "_lazy_prop_a")



# Generated at 2022-06-14 06:41:45.012341
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class MyClassA:
        @lazyperclassproperty
        def foo(cls):
            return "MyClassA"

    class MyClassB(MyClassA):
        pass

    assert MyClassA.foo == "MyClassA", "Lazy class property not working"
    assert MyClassB.foo == "MyClassA", "Lazy class property not working"
    assert MyClassA().__class__.foo == "MyClassA", "Lazy class property not working"
    assert MyClassB().__class__.foo == "MyClassA", "Lazy class property not working"



# Generated at 2022-06-14 06:41:50.251410
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    lazy = lazyclassproperty(lambda cls: cls.__name__.upper())
    class Foo:
        name = lazy
    assert Foo.name == 'FOO'


# Generated at 2022-06-14 06:41:57.201361
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class TestClass(object):
        @lazyclassproperty
        def test_prop(cls):
            return 'test'

        @lazyclassproperty
        def test_prop_with_args(cls):
            return 1 + 1

    test_1 = TestClass.test_prop
    test_2 = TestClass.test_prop_with_args

    assert test_1 == 'test'
    assert test_2 == 2
    assert TestClass.test_prop == 'test'
    assert TestClass.test_prop_with_args == 2



# Generated at 2022-06-14 06:42:04.052368
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:42:16.593696
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    global results
    results = []

    class Test(object):
        @lazyperclassproperty
        def test(cls):
            global results
            results.append('test')
            return 'test'

    class Test1(Test):
        pass

    class Test2(Test):
        pass

    # test the property

# Generated at 2022-06-14 06:42:20.809637
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            print('calling bar()')
            return 'bar'

    assert Foo.bar == 'bar'
    assert Foo.bar == 'bar'


# Generated at 2022-06-14 06:42:38.633305
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def myprop(cls):
            print("myprop is accessed")
            return 1.0
    a = A()
    print(a.myprop)
    print(a.myprop)
    b = A()
    print(b.myprop)

# Generated at 2022-06-14 06:42:42.331484
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 'baz'

    assert Foo.bar == 'baz'
    assert Foo.bar == 'baz'



# Generated at 2022-06-14 06:42:51.413074
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def func(cls):
            return "A func"

    class B(A):
        @lazyclassproperty
        def func(cls):
            return "B func"

        @lazyclassproperty
        def func2(cls):
            return "B func2"

    assert A.func == "A func"
    assert B.func == "B func"
    assert B.func2 == "B func2"

    assert A._lazy_func == "A func"
    assert B._lazy_func == "B func"
    assert B._lazy_func2 == "B func2"
    assert B._lazyclassprop == "B func"



# Generated at 2022-06-14 06:42:55.477387
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



# Generated at 2022-06-14 06:43:00.932740
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    @lazyperclassproperty
    def testprop(cls):
        return cls.__name__

    class TestClass1(object):
        pass

    class TestClass2(object):
        pass

    assert TestClass1.testprop == 'TestClass1'
    assert TestClass2.testprop == 'TestClass2'



# Generated at 2022-06-14 06:43:14.149913
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class First(object):

        @lazyperclassproperty
        def a(self):
            return random.random()

    class Second(First):

        @lazyperclassproperty
        def a(self):
            return random.random()

    f = First()
    s = Second()
    verif_a = []
    verif_b = []

    for k in range(5):
        if f.a == f.a:
            verif_a.append(True)
        else:
            verif_a.append(False)

        if s.a == s.a:
            verif_b.append(True)
        else:
            verif_b.append(False)

    assert True in verif_a
    assert True in verif_b

# Generated at 2022-06-14 06:43:17.949712
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def counter(cls):
            return 0

    class B(A):
        pass

    class C(A):
        pass

    for x in [A, A, B, A, C]:
        x.counter += 1
        assert x.counter == 1



# Generated at 2022-06-14 06:43:23.009917
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return cls

    class B(A):
        pass

    assert A.foo is A
    assert B.foo is B



# Generated at 2022-06-14 06:43:34.778633
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    """ Unit test for function lazyperclassproperty"""
    class A(object):
        @lazyperclassproperty
        def x(cls):
            cls.x = 'A'
            return cls.x

        @lazyperclassproperty
        def y(cls):
            cls.y = 'B'
            return cls.y

    a1 = A()
    assert a1.x == 'A'
    a2 = A()
    assert a2.x == 'A'

    class B(A):
        @lazyperclassproperty
        def x(cls):
            cls.x = 'C'
            return cls.x

        @lazyperclassproperty
        def y(cls):
            cls.y = 'D'
            return cls.y

    b1 = B

# Generated at 2022-06-14 06:43:39.865909
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        foo = 'foo'

        @lazyperclassproperty
        def myproperty(cls):
            return cls.foo + 'result'

    class B(A):
        foo = 'bar'

    assert A.myproperty == 'fooresult'
    assert B.myproperty == 'barresult'


# Generated at 2022-06-14 06:44:12.255324
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class MyBaseClass(object):
        def __init__(self, value):
            self.value = value

    class MyClass(MyBaseClass):
        @lazyperclassproperty
        def lazy(cls):
            return cls.value * 10

    class MyOtherClass(MyBaseClass):
        @lazyperclassproperty
        def lazy(cls):
            return cls.value + 10

    class MyDerivedClass(MyClass, MyOtherClass):
        pass

    class MyOtherDerivedClass(MyOtherClass, MyClass):
        pass

    assert MyClass.lazy == 0
    assert MyOtherClass.lazy == 10
    assert MyDerivedClass.lazy == 0
    assert MyOtherDerivedClass.lazy == 10


# Generated at 2022-06-14 06:44:16.579797
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class T(object):
        @lazyclassproperty
        def prop(self):
            return "test"

    assert T.prop == "test"
    assert T.prop == "test"


# Generated at 2022-06-14 06:44:22.135749
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def lazy(cls):
            return cls

    assert Test.lazy is Test
    assert Test().lazy is Test

    # now change return value
    Test.lazy = Test()
    assert Test.lazy is Test()
    assert Test().lazy is Test()



# Generated at 2022-06-14 06:44:25.903578
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class TestLazyClassProperty(object):
        def __init__(self, name):
            self.name = name

        name = lazyclassproperty(lambda cls: 'LazyClassProperty')

    assert TestLazyClassProperty.name == 'LazyClassProperty'



# Generated at 2022-06-14 06:44:35.991298
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def x(cls):
            print("calling x in Base")
            return 'base'

    class Subclass(Base):
        @lazyperclassproperty
        def x(cls):
            print("calling x in Subclass")
            return 'subclass'

    print("Base.x", Base.x)
    print("Subclass.x", Subclass.x)

    assert Base.x == 'base'
    assert Subclass.x == 'subclass'



# Generated at 2022-06-14 06:44:38.696072
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:44:50.865285
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        pass

    class B(A):
        pass

    class C(B):
        pass

    class D(C):
        pass

    # Test lazyperclassproperty works as an assignment
    @lazyperclassproperty
    def a(cls):
        return 'a'

    def b(cls):
        return 'b'

    A.b = lazyperclassproperty(b)

    # Test lazyperclassproperty works as a decorator
    @lazyperclassproperty
    def c(cls):
        return 'c'

    assert A.a == 'a'
    assert B.a == 'a'
    assert C.a == 'a'
    assert D.a == 'a'

    assert A.b == 'b'
    assert B.b == 'b'
    assert C.b

# Generated at 2022-06-14 06:44:58.784984
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Test(object):
        @lazyperclassproperty
        def lazy(cls):
            return 'lazy'

    class SubTest(Test):
        pass

    assert Test.lazy == 'lazy'
    assert SubTest.lazy == 'lazy'

    Test.lazy = 'not lazy'
    assert Test.lazy == 'not lazy'
    assert SubTest.lazy == 'lazy'



# Generated at 2022-06-14 06:45:02.105569
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def funk(cls):
            return 'A'

    class B(A):
        @lazyperclassproperty
        def funk(cls):
            return 'B'

    class C(object):
        @lazyperclassproperty
        def funk(cls):
            return 'C'

    a = A()
    b = B()
    c = C()

    assert A.funk == 'A'
    assert B.funk == 'B'
    assert C.funk == 'C'
    assert a.funk == 'A'
    assert b.funk == 'B'
    assert c.funk == 'C'
    assert A().funk == 'A'
    assert B().funk == 'B'
    assert C().funk

# Generated at 2022-06-14 06:45:07.493462
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            print("A.x has been accessed")
            return 42

    class B(A):
        pass
    class C(A):
        pass

    assert(A.x == 42)
    assert(B.x == A.x)
    assert(C.x == A.x)

