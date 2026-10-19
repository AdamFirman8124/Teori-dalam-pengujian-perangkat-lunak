

# Generated at 2022-06-14 06:35:44.400802
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Unit test for function lazyclassproperty.
    """

    for itype in [
        # Basic cases
        "", "...",
        # Newline delimited string cases
        "a\nb\nc\n", "a\nb\nc\n\n", "\na\nb\nc", "\na\nb\nc\n",
        # Special cases
        " ", "  ", "   "
    ]:
        class Test(object):
            @lazyclassproperty
            def a(cls):
                return itype

        t = Test()
        assert t.a == itype

# Generated at 2022-06-14 06:35:47.612489
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:36:01.446923
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Example(object):
        @lazyclassproperty
        def foo(cls):
            raise Exception('This should not be raised')
        @lazyclassproperty
        def bar(cls):
            return 'baz'
    assert not hasattr(Example, '_lazy_foo')
    assert Example.foo == Example.foo
    assert hasattr(Example, '_lazy_foo')

    assert Example.bar == 'baz'
    assert hasattr(Example, '_lazy_bar')

    class ExampleSubclass(Example):
        pass

    assert ExampleSubclass.foo == Example.foo
    assert not hasattr(ExampleSubclass, '_lazy_foo')
    assert ExampleSubclass.bar == 'baz'
    assert not hasattr(ExampleSubclass, '_lazy_bar')

# Unit test

# Generated at 2022-06-14 06:36:07.428151
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def d(cls): return {'k': 1}
        @lazyclassproperty
        def f(cls): return {'k': 2}
    assert C.d is C.d
    assert C.f is C.f
    assert C.d is not C.f
    assert C.d['k'] == 1
    assert C.f['k'] == 2



# Generated at 2022-06-14 06:36:10.784881
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Example:
        @lazyclassproperty
        def t(cls):
            print("t is used")
            return 5

    assert Example.t == 5
    assert Example.t == 5  # Make sure it's cached

    assert Example() is not Example()



# Generated at 2022-06-14 06:36:19.455748
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def x(cls):
            print(" I'm x")
            return 5

    class Bar(Foo):
        pass

    f = Foo()
    assert f.x == 5  # First usage
    assert Foo.x == 5  # Second usage
    assert Bar.x == 5  # Inheritance from Foo

    b = Bar()
    assert b.x == 5

# End unit test for function lazyclassproperty



# Generated at 2022-06-14 06:36:27.230197
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self, value):
            self.value = value

        @lazyclassproperty
        def prop1(cls):
            return cls(42)  # prop1 is cached

        @lazyperclassproperty
        def prop2(cls):
            return cls(43)  # prop2 is cached per inheritor

    class B(A):
        @lazyperclassproperty
        def prop2(cls):
            return cls(44)  # prop2 is cached per inheritor

    a = A(0)
    b = B(0)

    assert a.prop1.value == 42
    assert b.prop1.value == 42  # prop1 is cached as class property
    assert A.prop1.value == 42  # prop1 is cached as class property


# Generated at 2022-06-14 06:36:32.611401
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print("CALL: foo")
            return 1
    assert A.foo == 1
    A.foo = 2
    assert A.foo == 2

    # test cached
    class B(A):
        pass
    assert B.foo == 2


# Generated at 2022-06-14 06:36:37.274047
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    cls = type('Test', (object,), {})

# Generated at 2022-06-14 06:36:40.856509
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print("A.foo run")
            return 1

    class B(A):
        pass

    print(A.foo)
    print(A.foo)
    print(B.foo)
    print(B.foo)



# Generated at 2022-06-14 06:36:51.227420
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:36:58.204034
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test:
        @lazyclassproperty
        def foo(cls):
            print ('Call foo()')
            return 42

        @lazyclassproperty
        def bar(cls):
            print ('Call bar()')
            return cls.foo + 1

    assert Test.foo == 42
    assert Test.foo == 42
    assert Test.bar == 43
    assert Test.bar == 43



# Generated at 2022-06-14 06:37:05.888409
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:37:07.894851
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test:
        @lazyclassproperty
        def a(cls):
            print("its working")
            return 35
    assert Test.a == 35


# Generated at 2022-06-14 06:37:15.639896
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def foo(cls):
            return []

        def bar(self):
            self.foo.append(self)

    assert not hasattr(Foo, '_lazy_foo')
    assert not hasattr(Foo, '_foo')
    assert not hasattr(Foo, 'foo')

    foo1 = Foo()
    foo2 = Foo()

    Foo.foo
    assert Foo.foo is Foo.foo
    assert hasattr(Foo, '_lazy_foo')
    assert Foo._lazy_foo is Foo.foo
    assert Foo._lazy_foo is not Foo.foo

    assert foo1.foo is foo2.foo
    assert foo1.foo is Foo.foo

    foo1.bar()


# Generated at 2022-06-14 06:37:20.664729
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:37:27.759453
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:37:31.632005
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        n = 3

        @lazyperclassproperty
        def x(cls):
            return cls.n * 2

    class B(A):
        n = 4

    assert A.x == 6
    assert B.x == 8



# Generated at 2022-06-14 06:37:40.917231
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class TestClass(object):
        @lazyperclassproperty
        def test(self):
            return 'test'

        @lazyperclassproperty
        def test2(self):
            return 'test2'

    class TestClassInheritor(TestClass):
        pass

    print(TestClass._test_lazy_test)
    print(TestClass._test2_lazy_test2)
    print(TestClassInheritor._test_lazy_test)
    print(TestClassInheritor._test2_lazy_test2)


# Generated at 2022-06-14 06:37:45.572238
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def class_attrib(cls):
            return 'Base'

    class ChildA(Base):
        pass

    class ChildB(Base):
        pass

    assert Base.class_attrib == 'Base'
    assert ChildA.class_attrib == 'Base'
    assert ChildB.class_attrib == 'Base'

# Generated at 2022-06-14 06:38:00.136398
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    from types import FunctionType
    from inspect import signature

    class Foo(object):
        @lazyperclassproperty
        def foo(cls):
            return cls.__name__

    class Bar(Foo):
        pass

    assert isinstance(Foo.foo, FunctionType)
    assert Foo.foo.__doc__ == Foo.__name__
    assert Bar.foo.__doc__ == Bar.__name__

    assert Bar.foo is not Foo.foo
    assert Foo.foo() == Foo.__name__
    assert Bar.foo() == Bar.__name__


# Generated at 2022-06-14 06:38:05.305690
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def value(cls):
            print("lazyclassproperty")
            return 10

    class B(A):
        @lazyclassproperty
        def value(cls):
            print("lazyclassproperty")
            return 20

    a = A()
    b = B()
    assert a.value == 10
    assert b.value == 20
    assert a.value == 10
    assert b.value == 20



# Generated at 2022-06-14 06:38:09.340849
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            print('class_prop executed')
            return 'value of class prop'

    class B(A):
        pass

    class C(B):
        pass

    assert A.prop == 'value of class prop'
    assert B.prop == 'value of class prop'
    assert C.prop == 'value of class prop'
    # print(A.__dict__.keys())
    # print(B.__dict__.keys())
    # print(C.__dict__.keys())

# Generated at 2022-06-14 06:38:14.428550
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    def f(cls):
        return cls._counter

    class Foo:
        _counter = 1

        lp = lazyperclassproperty(f)

    class Bar(Foo):
        _counter = 2

    assert Foo.lp == 1
    assert Bar.lp == 2
    assert Foo.lp == 1


# Generated at 2022-06-14 06:38:25.333758
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def test(self):
            return 'a'

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def test(self):
            return 'c'

    class D(C):
        pass

    assert A().test == 'a'
    assert B().test == 'a'
    assert C().test == 'c'
    assert D().test == 'c'
    assert isinstance(A.test, roclassproperty)
    assert isinstance(B.test, roclassproperty)
    assert isinstance(C.test, roclassproperty)
    assert isinstance(D.test, roclassproperty)

# Generated at 2022-06-14 06:38:29.385548
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return cls.__name__ + 'bar'

    assert Foo.bar == 'Foobar'



# Generated at 2022-06-14 06:38:32.797079
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(self):
            print('first evaluation')
            return 42

    assert Foo.bar == 42
    assert Foo.bar == 42



# Generated at 2022-06-14 06:38:39.767113
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):

        def test_fn(self):
            return "Hello World!"

        @lazyclassproperty
        def prop_test(cls):
            return cls.test_fn()

        @lazyclassproperty
        def prop_test2(cls):
            return cls.test_fn()

        @lazyperclassproperty
        def prop_test3(cls):
            return cls.test_fn()

    a = MyClass()
    print(a.prop_test)
    print(a.prop_test2)

    class MySubClass(MyClass):
        pass

    b = MySubClass()
    print(b.prop_test3)



# Generated at 2022-06-14 06:38:46.163793
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            print('a', cls)
            return cls

    class B(A):
        pass

    class C(A):
        pass

    assert A().x is A
    assert B().x is B
    assert C().x is C



# Generated at 2022-06-14 06:38:57.201491
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def prop(cls):
            return 'bar'

    class Bar(Foo):
        pass

    class Baz(Foo):
        @lazyclassproperty
        def prop(cls):
            return 'baz'

    assert Foo.prop == 'bar'
    assert Bar.prop == 'bar'
    assert Baz.prop == 'baz'


# def _(val):
#     if _.__getattribute__("_" + val.__class__.__name__) is not None:
#         return _.__getattribute__("_" + val.__class__.__name__)(val)
#     else:
#         return val


# class _int(_int):
#     @staticmethod
#     def __new__(cls, val):

# Generated at 2022-06-14 06:39:17.062701
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        x = 0
        def __init__(self):
            self.y = 0
        @lazyclassproperty
        def z(cls):
            cls.x += 1
            return cls.x
        @lazyclassproperty
        def w(cls):
            self.y += 1
            return self.y
    a = A()
    assert (a.z == 1)
    assert (A.z == 1)
    assert (a.z == 1)
    assert (a.w == 1)
    assert (a.w == 1)
    a.w = 2
    assert (a.w == 2)



# Generated at 2022-06-14 06:39:22.777368
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Foo(object):
        @lazyperclassproperty
        def foo(cls):
            print('foo')
            return 1

    class Bar(Foo):
        pass

    assert Foo.foo == 1
    assert Bar.foo == 1
    Foo.foo = 2
    assert Foo.foo == 2
    assert Bar.foo == 1
    Bar.foo = 3
    assert Foo.foo == 2
    assert Bar.foo == 3


# Generated at 2022-06-14 06:39:34.283701
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def prop(cls):
            return 'BaseClass'

    class DerivedA(Base):
        pass

    class DerivedB(Base):
        pass

    # Per-class properties are not overwritten by inheritors
    assert Base.prop == 'BaseClass'
    assert DerivedA.prop == 'BaseClass'
    assert DerivedB.prop == 'BaseClass'

    # Neither is overwritten by a different per-class property
    DerivedA.prop = 'DerivedA'
    assert Base.prop == 'BaseClass'
    assert DerivedA.prop == 'DerivedA'
    assert DerivedB.prop == 'BaseClass'

    DerivedB.prop = 'DerivedB'
    assert Base.prop == 'BaseClass'
    assert DerivedA

# Generated at 2022-06-14 06:39:45.891497
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class BaseClass(object):
        val = 1
        def fn(cls):
            return cls.val

    class SubClass(BaseClass):
        val = 2

    @lazyperclassproperty
    def lazy(cls):
        return cls.fn()

    assert lazy.__get__(None, BaseClass) == 1
    assert lazy.__get__(None, SubClass) == 2
    BaseClass.val = 3
    assert lazy.__get__(None, BaseClass) == 3
    assert not hasattr(BaseClass, '_BaseClass_lazy_fn')
    assert lazy.__get__(None, SubClass) == 2
    assert not hasattr(SubClass, '_SubClass_lazy_fn')
    assert SubClass.__dict__.get('_lazy_fn') == 2

   

# Generated at 2022-06-14 06:39:50.581303
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def my_property(cls):
            return "value"

    a = A()
    assert A.my_property == 'value'
    assert a.my_property == 'value'
    assert A.my_property == 'value'



# Generated at 2022-06-14 06:39:59.178383
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class TestLazyClassProperty(object):
        def __init__(self):
            self.value = ''

        @lazyclassproperty
        def property(cls):
            return cls.value

        @property.setter
        def property(self, value):
            self.value = value

    t1 = TestLazyClassProperty()
    t2 = TestLazyClassProperty()

    assert TestLazyClassProperty.property is t1.property is t2.property == ''
    t1.property = 'value 1'
    assert TestLazyClassProperty.property is t1.property is t2.property == 'value 1'
    t2.property = 'value 2'
    assert TestLazyClassProperty.property is t1.property is t2.property == 'value 2'
    assert 'property' in TestLazyClassProperty

# Generated at 2022-06-14 06:40:11.428769
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Test caching
    class Foo(object):
        @lazyclassproperty
        def cached_property(self):
            print("CachedProperty: Calculating cached_property")
            return "CachedProperty value"

        @lazyclassproperty
        def cached_property_with_parameters(self, param1):
            print("CachedPropertyWithParameters: Calculating cached_property_with_parameters")
            return "CachedPropertyWithParameters value with parameter {}".format(param1)

    class Bar(Foo):
        pass

    class UnrelatedClass(object):
        pass

    assert Foo.cached_property == "CachedProperty value"
    assert Bar.cached_property == "CachedProperty value"
    assert hasattr(Foo, '_lazy_cached_property') == True

# Generated at 2022-06-14 06:40:14.976204
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return cls.__name__
    class B(A):
        pass
    assert A.foo == 'A'
    assert B.foo == 'B'


# Generated at 2022-06-14 06:40:25.840911
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:40:35.397500
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def foo(self):
            print("Function was called")
            return 42
    
    class B(A):
        pass
    
    print('Test begin')
    
    # First call of property foo
    counter = 0

    a = A()
    b = B()

    print(a.foo)
    print(a.foo)
    print(b.foo)
    print(b.foo)
    print(a.foo)

    print('Test end')

if __name__ == '__main__':
    test_lazyperclassproperty()

# Generated at 2022-06-14 06:40:56.226712
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A():
        @lazyperclassproperty
        def prop(cls):
            return cls()

    class B(A):
        def __init__(self):
            pass

    assert A.prop.__class__ == A
    assert B.prop.__class__ == B

# Generated at 2022-06-14 06:41:03.770877
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    import pytest
    from unittest import mock

    @lazyperclassproperty
    def test():
        return object()

    class TestClass(object):
        pass

    class InheritedClass(TestClass):
        pass

    assert TestClass.test is not InheritedClass.test
    assert test.__get__(TestClass, TestClass) is TestClass.test
    assert TestClass.test is not TestClass.test
    assert TestClass.test is not InheritedClass.test

    with mock.patch('tests.utils.object') as mocked:
        test_obj = TestClass.test
        assert mocked.called

    assert test_obj is TestClass.test
    assert test_obj is not InheritedClass.test


# Generated at 2022-06-14 06:41:09.168304
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def something(cls):
            return cls.__name__
    class B(A): pass
    class C(A): pass
    assert A.something == 'A'
    assert B.something == 'B'
    assert C.something == 'C'



# Generated at 2022-06-14 06:41:18.228165
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A():
        @lazyclassproperty
        def fee(cls):
            return cls.__name__

    class B(A):
        pass

    class C(A):
        pass

    assert A.fee == 'A'
    assert B.fee == 'A'
    assert C.fee == 'A'

    A.fee = 'D'
    assert A.fee == 'D'
    assert B.fee == 'A'
    assert C.fee == 'A'
    return True



# Generated at 2022-06-14 06:41:25.503422
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def val(cls):
            return 1

    a = A()
    b = A()
    assert a.val == 1
    assert b.val == 1

    a.val = 4
    assert a.val == 4
    assert b.val == 1
    assert A.val == 4



# Generated at 2022-06-14 06:41:31.931693
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Base:
        @lazyperclassproperty
        def x(cls):
            print('{} x got'.format(cls.__name__))
            return 1

    class Derived(Base):
        pass

    class Derived2(Base):
        pass

    assert Base.x == 1
    assert Derived.x == 1
    assert Derived2.x == 1



# Generated at 2022-06-14 06:41:42.485998
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def x(cls):
            return 1

    assert A.x == 1
    assert A.__dict__['_lazy_x'] == 1
    assert A.__dict__['_lazy_x'] is A.__dict__['_lazy_x']
    assert ('_lazy_x' in A.__dict__) is True

    class B(A):
        pass

    assert B.x == 1
    assert B.__dict__['_lazy_x'] == 1
    assert B.__dict__['_lazy_x'] is B.__dict__['_lazy_x']
    assert ('_lazy_x' in B.__dict__) is True

    assert A.x is B.x

# Generated at 2022-06-14 06:41:52.859081
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        @lazyclassproperty
        def lazyproperty(cls):
            return cls.__name__

        @lazyperclassproperty
        def lazyperproperty(cls):
            return cls.__name__
    print
    'Class MyClass tests for lazyclassproperty:'
    print
    'MyClass.lazyproperty:', MyClass.lazyproperty
    print
    'MyClass.lazyperproperty:', MyClass.lazyperproperty
    class MyClassChild(MyClass):
        pass
    print
    'Class MyClassChild tests for lazyclassproperty:'
    print
    'MyClassChild.lazyproperty:', MyClassChild.lazyproperty
    print
    'MyClassChild.lazyperproperty:', MyClassChild.lazyperproperty



# Generated at 2022-06-14 06:42:01.472160
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return list()

    class B(A):
        pass

    class C(A):
        pass

    print(A.x, B.x, C.x)
    A.x.append(1)
    B.x.append(2)
    C.x.append(3)
    print(A.x, B.x, C.x)



# Generated at 2022-06-14 06:42:05.772368
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    def fn(cls):
        return "simple"

    class Test(object):
        p = lazyclassproperty(fn)

    assert Test.p == "simple"

    Test.p = None
    assert Test.p is None



# Generated at 2022-06-14 06:42:47.596782
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        @lazyclassproperty
        def foo(cls):
            print("setting foo")
            return 1

    class B(A):
        pass

    class C(A):
        @lazyclassproperty
        def foo(cls):
            print("setting foo")
            return 3

    class D(B, C):
        pass

    print(A.foo)
    print(B.foo)
    print(C.foo)
    print(D.foo)


# Generated at 2022-06-14 06:42:50.523255
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 3

    class B(A):
        pass

    assert A.prop == B.prop == 3



# Generated at 2022-06-14 06:43:03.035145
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def bob(cls):
            # Just an example of setting a class property
            A.bob = 3
            return A.bob

        @lazyperclassproperty
        def foo(cls):
            # This checks that the return value is per class
            # and that child classes will have different return
            # values.
            return cls.__name__

    class B(A):
        pass

    # Create an instance of each class
    a = A()
    b = B()

    # No value should be set yet
    assert not hasattr(A, '_A_lazy_bob')
    assert not hasattr(B, '_B_lazy_bob')
    assert not hasattr(A, '_A_lazy_foo')
   

# Generated at 2022-06-14 06:43:16.022459
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def attr1(cls):
            return cls.attr2

        @lazyclassproperty
        def attr2(cls):
            return cls.attr1 + 1

        @lazyclassproperty
        def attr3(cls):
            return cls.attr1 + 1

    class TestSub(Test):
        pass

    @add_metaclass(lazyclassproperty)
    class TestMeta(object):
        attr1 = 1
        attr2 = 2
        attr3 = 3

    # - Only first accessed lazy class property should be evaluated.
    assert Test.attr1 == 3

    # - Order of class definition does not matter.
    # - Inherited properties are cached as separate instances.
    assert TestSub.attr1 == 3
   

# Generated at 2022-06-14 06:43:26.023227
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 'foo ' + cls.__name__

    class Bar(Foo):
        pass

    foo = Foo()
    # Test if attributes are correctly assigned in the different classes
    assert Foo.bar == 'foo Foo'
    assert Bar.bar == 'foo Bar'
    # Test if caching works correctly
    assert Foo.bar is Foo.bar
    assert Bar.bar is Bar.bar
    # Test if cached values are the same in the different classes
    assert Foo.bar is Bar.bar

# Generated at 2022-06-14 06:43:36.550270
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return "a"

        @lazyperclassproperty
        def b(cls):
            return "b"

    class B(A):
        @lazyperclassproperty
        def b(cls):
            return "B"

    class C(A):
        @lazyperclassproperty
        def a(cls):
            return "C"

    class D(B):
        @lazyperclassproperty
        def a(cls):
            return "C"

    class E(C, D):
        pass

    assert A.a == "a"
    assert A.b == "b"
    assert B.a == "a"
    assert B.b == "B"
    assert C.a == "C"

# Generated at 2022-06-14 06:43:43.944784
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def aprop(cls):
            print("aprop getter called")
            return 1

    assert A.aprop == 1
    assert A.aprop == 1

    # Clear cache
    delattr(A, "_lazy_aprop")

    assert A.aprop == 1

    class B(A):
        pass

    assert B.aprop == 1



# Generated at 2022-06-14 06:43:50.118383
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Alpha():
        cnt = 0
        @lazyclassproperty
        def count(cls):
            cls.cnt += 1
            return cls.cnt

    class Beta(Alpha):
        pass

    class Gamma(Alpha):
        pass

    assert Alpha.cnt == 0
    assert Alpha.count == 1
    assert Alpha.count == 1

# Generated at 2022-06-14 06:43:57.117469
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        @lazyclassproperty
        def prop(cls):
            return 'value'

    print(MyClass)
    print(MyClass.prop)
    print(MyClass.prop)
    assert MyClass.prop == 'value'
    MyClass.prop = 'value2'
    assert MyClass.prop == 'value2'
    class MyClass2(MyClass):
        pass
    print(MyClass2)
    print(MyClass2.prop)
    print(MyClass2.prop)
    assert MyClass2.prop == 'value'



# Generated at 2022-06-14 06:44:02.793538
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    import unittest

    class C(object):
        @lazyclassproperty
        def val(cls):
            return 'Val'

    class Test(unittest.TestCase):
        def test_lazyclassproperty(self):
            self.assertEquals('Val', C.val)

    unittest.main()

