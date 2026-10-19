

# Generated at 2022-06-14 06:35:43.779684
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 'the result'

    assert A.prop == 'the result'
    assert A().prop == 'the result'


if __name__ == '__main__':
    test_lazyclassproperty()

# Generated at 2022-06-14 06:35:54.534060
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    the_value_for_a = 'foo'
    the_value_for_b = 'bar'

    class Foo(object):
        @lazyclassproperty
        def a(cls):
            print('lazy-generating a')
            return the_value_for_a
    class Bar(Foo):
        @lazyclassproperty
        def b(cls):
            print('lazy-generating b')
            return the_value_for_b

    class Quux(Bar):
        pass

    assert Foo.a == the_value_for_a
    assert Bar.a == the_value_for_a
    assert Foo.b == the_value_for_b
    assert Bar.b == the_value_for_b
    assert Quux.a == the_value_for_a
    assert Quux

# Generated at 2022-06-14 06:35:57.370408
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Class(object):
        @lazyclassproperty
        def prop(cls):
            print('val')
            return 'val'

    # This should print val.
    assert Class.prop == 'val'

    # This should not print anything.
    assert Class.prop == 'val'



# Generated at 2022-06-14 06:36:02.752307
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    def fn(cls):
        return None

    _lazyclassprop = lazyclassproperty(fn)
    assert lazyclassproperty.func == fn
    assert _lazyclassprop.__doc__ == fn.__doc__
    assert _lazyclassprop.__name__ == '_lazy_fn'



# Generated at 2022-06-14 06:36:10.297416
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        def foo(self):
            return 'foo'

    class Child(Base):
        pass

    class GrandChild(Child):
        pass

    assert Base.foo() == 'foo'
    assert Child.foo() == 'foo'
    assert GrandChild.foo() == 'foo'

    Base.foo = lazyperclassproperty(Base.foo)
    Child.foo = lazyperclassproperty(Child.foo)

    assert Base.foo() == 'foo'
    assert Child.foo() == 'foo'
    assert GrandChild.foo() == 'foo'


# Generated at 2022-06-14 06:36:17.315323
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            return 1
    assert A.x == 1
    class B(A):
        @lazyclassproperty
        def y(cls):
            return 2
    assert B.x == 1
    assert B.y == 2
    assert A.x == 1
    assert not hasattr(A, "y")


# Generated at 2022-06-14 06:36:24.332180
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        pass

    @lazyclassproperty
    def test(cls):
        return 'test'
    A.test

    class B(A):
        pass

    B.test

    # Check classes don't share the value
    assert A.test is not B.test
    # Check the value is cached in the classes
    assert A.test is A.test
    assert B.test is B.test
    # Check one of the values is the expected result
    assert A.test == 'test'



# Generated at 2022-06-14 06:36:37.183046
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        def __init__(self):
            self.test_attr = 0
            self.test_class_static_attr = 0
        @lazyclassproperty
        def test_class_attr(cls):
            cls.test_class_static_attr += 1
            return cls.test_class_static_attr
    t1 = Test()
    t2 = Test()
    assert t1.test_class_attr == t2.test_class_attr == 1
    t1.test_class_attr += 1
    assert t1.test_class_attr == t2.test_class_attr == 2
    del t1.test_class_attr
    assert t1.test_class_attr == t2.test_class_attr == 2
    t1.test_class_attr += 1


# Generated at 2022-06-14 06:36:44.512652
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base:
        @lazyperclassproperty
        def base_prop(self):
            return "Base property"

    class Inheritor(Base):
        pass

    class Inheritor2(Base):
        @lazyperclassproperty
        def base_prop(self):
            return "Base property overridden in Inheritor2"

    assert Base.base_prop == "Base property"
    assert Inheritor.base_prop == "Base property"
    assert Inheritor2.base_prop == "Base property overridden in Inheritor2"



# Generated at 2022-06-14 06:36:49.228696
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self):
            self._x = 1

        def _f(self):
            return self._x

        x = lazyclassproperty(_f)

    a = A()
    assert a.x == 1


# Generated at 2022-06-14 06:37:02.474563
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # This is some dummy code for testing purposes only.

    class Base(object):
        @lazyperclassproperty
        def static_list(cls):
            print("static_list")
            return [1,2,3]

        @lazyperclassproperty
        def static_dict(cls):
            print("static_dict")
            return {k : v for k, v in enumerate("abcdefghi")}

    class A(Base):
        pass
    class B(Base):
        pass

    a = A()
    b = B()
    a.static_dict
    a.static_list
    b.static_dict
    b.static_list
    A.static_dict
    A.static_list
    B.static_dict
    B.static_list

    # You should expect this output:

# Generated at 2022-06-14 06:37:05.633481
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        @lazyperclassproperty
        def test(cls):
            return cls.__name__

    class B(A):
        pass

    assert A.test == 'A'
    assert B.test == 'B'



# Generated at 2022-06-14 06:37:08.218851
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:37:19.457956
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def test(self):
            return 1
    class B(A):
        @lazyperclassproperty
        def test(self):
            return 2
    class C(B):
        pass

    assert A._A_lazy_test == A._lazy_test == A.test == 1
    assert B._B_lazy_test == B._lazy_test == B.test == 2
    assert C._B_lazy_test == C._lazy_test == C.test == 2
    assert not hasattr(C, '_A_lazy_test')
    assert not hasattr(C, '_B_lazy_test')
    assert not hasattr(C, '_lazy_test')



# Generated at 2022-06-14 06:37:23.798249
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        def __init__(self):
            self.foo = 1

        @lazyclassproperty
        def foo(cls):
            return cls

    class B(A):
        pass

    assert B.foo is not A.foo



# Generated at 2022-06-14 06:37:29.713077
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            print('Calculating x')
            return 1

    print(A.x)
    print(A.x)
    print(A().x)
    print(A().x)

    class B(A):
        pass

    print(B.x)
    print(B().x)



# Generated at 2022-06-14 06:37:37.869530
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class Test(object):
        @lazyclassproperty
        def prop(cls):
            print("Evaluating Test.prop")
            return 42

    assert Test.prop == 42
    assert Test.__dict__['_lazy_prop'] == 42

    class Derived(Test):
        pass

    assert Derived.prop == 42
    assert Derived.__dict__['_lazy_prop'] == 42


# Unit tests for function lazyperclassproperty

# Generated at 2022-06-14 06:37:44.489232
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class PropertyClass(object):

        @lazyclassproperty
        def test(cls):
            return 'inside'

    assert hasattr(PropertyClass, '_lazy_test') is False
    assert PropertyClass.test == 'inside'
    assert hasattr(PropertyClass, '_lazy_test') is True
    assert getattr(PropertyClass, '_lazy_test') == 'inside'
    assert PropertyClass.test == 'inside'



# Generated at 2022-06-14 06:37:56.772073
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop1(cls):
            return 'A'
    class B(A):
        pass
    class C(A):
        @lazyperclassproperty
        def prop1(cls):
            return 'C'
    class D(B, C):
        pass

    # Check that the results are unique
    assert A.prop1 is B.prop1 is C.prop1 is 'A'
    assert A.prop1 is not D.prop1 is 'A'
    assert C.prop1 is not D.prop1 is 'C'

    # Check that the attributes are on the right classes
    assert hasattr(A, '_A_lazy_prop1')
    assert hasattr(B, '_B_lazy_prop1')
    assert not hasattr

# Generated at 2022-06-14 06:38:01.902750
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class C(object):
        @lazyperclassproperty
        def f(cls):
            return cls.__name__ + '.prop'

    class D(C):
        pass

    assert C.f == 'C.prop'
    assert D.f == 'D.prop'
    assert C.f is not D.f



# Generated at 2022-06-14 06:38:16.109204
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self, a):
            self.a = a


# Generated at 2022-06-14 06:38:23.539661
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class X(object):
        __metaclass__ = abc.ABCMeta

        @lazyclassproperty
        def a(cls):
            return "herp"

    class Y(X):
        pass

    class Z(X):
        pass

    assert X.a == Y.a == "herp"
    X.a = "derp"
    assert X.a == "derp"
    assert Y.a == "herp"



# Generated at 2022-06-14 06:38:35.422924
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base():
        @lazyperclassproperty
        def prop(cls):
            return 'prop' + '_' + cls.__name__

    class SubClass1(Base):
        pass

    class SubClass2(Base):
        pass

    # Check that there is an instance of Base for Base, SubClass1, and SubClass2
    assert(Base.prop == 'prop_Base')
    assert(SubClass1.prop == 'prop_SubClass1')
    assert(SubClass2.prop == 'prop_SubClass2')
    # Make sure that they are different instances
    assert(Base() != SubClass1())
    assert(Base() != SubClass2())
    assert(SubClass1() != SubClass2())
    # Make sure that the lazy property is a class property and not a global property

# Generated at 2022-06-14 06:38:47.830092
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    calls = []
    class C(object):
        @lazyclassproperty
        def prop(cls):
            calls.append(cls)
            return len(calls)

    assert len(calls) == 0
    assert C.prop == 1
    assert len(calls) == 1
    assert C.prop == 1
    assert len(calls) == 1
    class D(C):
        pass
    assert len(calls) == 2
    assert D.prop == 2
    assert len(calls) == 2
    assert D.prop == 2
    assert len(calls) == 2
    assert C.prop == 1
    assert len(calls) == 2
    assert C().prop == 1
    assert len(calls) == 2


# Generated at 2022-06-14 06:39:00.740652
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        @lazyclassproperty
        def class_attribute(cls):
            print('Generating class attribute')
            return 'value'

    print(MyClass.class_attribute)
    print(MyClass.__dict__)
    print(MyClass.class_attribute)
    print(MyClass.__dict__)

    # The output is:
    # Generating class attribute
    # value
    # {'__doc__': None, '_lazy_class_attribute': 'value', '__module__': '__main__', 'class_attribute': <property object at 0x1006f4948>, '__dict__': <attribute '__dict__' of 'MyClass' objects>, '__weakref__': <attribute '__weakref__' of 'MyClass' objects>}
    # value
    #

# Generated at 2022-06-14 06:39:05.558381
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print('foo')
            return 'foo'

    assert not hasattr(A, '_lazy_foo')
    assert A.foo == 'foo'
    assert hasattr(A, '_lazy_foo')


# Generated at 2022-06-14 06:39:18.744422
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:22.031309
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:39:33.554412
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:39:39.489099
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    from collections import Counter
    class Foo:
        @lazyperclassproperty
        def myprop(cls):
            return Counter()

    class Bar(Foo):
        pass

    assert Foo.myprop is not Bar.myprop

    f1 = Foo()
    f2 = Foo()
    b1 = Bar()
    b2 = Bar()

    assert isinstance(f1.myprop, Counter)
    assert isinstance(f2.myprop, Counter)
    assert isinstance(b1.myprop, Counter)
    assert isinstance(b2.myprop, Counter)

    assert f1.myprop is f2.myprop
    assert b1.myprop is b2.myprop
    assert f1.myprop is not b1.myprop



# Generated at 2022-06-14 06:39:52.996830
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    def fn(cls):
        return cls.__name__
    result1 = lazyperclassproperty(fn)
    assert result1.__name__ == '_lazyclassprop'
    result2 = lazyperclassproperty(fn)
    assert result2.__name__ == '_lazyclassprop'

# Generated at 2022-06-14 06:40:01.327290
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:40:12.861615
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A:
        def __init__(self):
            self._x = "foo"

        @lazyclassproperty
        def some_cache(cls):
            print("Generating cache for A")
            return "cache for A"

        @lazyclassproperty
        def some_other_cache(cls):
            print("Generating cache for A")
            return "cache for A"

    class B(A):
        def __init__(self):
            super(B, self).__init__()
            self._x = "bar"

        @lazyclassproperty
        def some_cache(cls):
            print("Generating cache for B")
            return "cache for B"

    print("Accessing property A._lazy_some_cache")

# Generated at 2022-06-14 06:40:23.503716
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        def _init(self):
            self.called = False

        @lazyclassproperty
        def p(cls):
            self = cls()
            self._init()
            self.called = True
            return self

    assert C.p.called == False
    assert C.p.called == True

    assert C.p is C.p

    assert hasattr(C, "_lazy_p")
    assert "_lazy_p" in C.__dict__

if __name__ == '__main__':
    test_lazyclassproperty()

# Generated at 2022-06-14 06:40:28.784131
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def pr(cls):
            print("A.pr")
            return "A"

    class B(A):
        pass

    class C(A):
        pass

    assert A.pr == "A"
    assert B.pr == "A"
    assert C.pr == "A"

# Generated at 2022-06-14 06:40:34.159540
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:40:45.811072
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    lazyclassproperty_executed = False

    class A():
        @lazyclassproperty
        def b(cls):
            nonlocal lazyclassproperty_executed
            lazyclassproperty_executed = True
            return 5

    # Property 'b' not yet executed
    assert lazyclassproperty_executed is False

    assert A.b == 5

    # Property 'b' has been executed
    assert lazyclassproperty_executed is True

    # Property 'b' has been cached and will not be executed again
    lazyclassproperty_executed = False
    assert A.b == 5
    assert lazyclassproperty_executed is False

    # Calling the function directly will execute it again
    assert _lazyclassprop(A) == 5
    assert lazyclassproperty_executed is True


# Generated at 2022-06-14 06:40:54.294646
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        a = lazyperclassproperty(lambda cls: 'A')
        b = lazyperclassproperty(lambda cls: 'B')

    class B(A):
        a = lazyperclassproperty(lambda cls: 'a')
        b = lazyperclassproperty(lambda cls: 'b')

    assert B.a == 'a'
    assert B.b == 'b'
    assert A.a == 'A'
    assert A.b == 'B'


# Generated at 2022-06-14 06:41:05.660609
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        def __init__(self, name):
            self.name = name

        @lazyperclassproperty
        def value(cls):
            # The very first time when it is called, the class of this function will be `Foo`.
            # The second time and so on, the class will be `FooChild`
            print("lazyperclassproperty is called for class {0}".format(cls.__name__))
            return cls.__name__[0]

    class FooChild(Foo):
        pass

    print("Foo.value={0}".format(Foo.value))  # will be called lazily, output: "lazyperclassproperty is called for class Foo"
    print("FooChild.value={0}".format(FooChild.value))  # will be called

# Generated at 2022-06-14 06:41:19.433574
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A1:
        @lazyclassproperty
        def prop(cls):
            print('creating A1.prop')
            return 'the A1.prop value'

    class A2(A1):
        pass

    class A3(A1):
        @lazyclassproperty
        def prop(cls):
            print('creating A3.prop')
            return 'the A3.prop value'

    class B(A3):
        pass

    a1 = A1()
    a2 = A2()
    a3 = A3()
    b = B()

    assert a1.prop == 'the A1.prop value'
    assert a1.prop == 'the A1.prop value'
    assert A1.prop == 'the A1.prop value'


# Generated at 2022-06-14 06:41:42.513605
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        counter = 0

        @lazyclassproperty
        def test(cls):
            cls.counter += 1
            return 5

    for i in xrange(100):
        assert A.counter == 0
        assert A.test == 5
        assert A.counter == 1

    assert A.counter == 1
    assert A.test == 5
    assert A.counter == 1



# Generated at 2022-06-14 06:41:49.727942
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def hello(cls):
            return 'hi'

        @lazyclassproperty
        def test(cls):
            return cls.__name__

    assert 'hi' == Test.hello
    assert 'Test' == Test.test

    class Test2(Test):
        pass

    assert 'hi' == Test2.hello
    assert 'Test' == Test.test
    assert 'Test2' == Test2.test



# Generated at 2022-06-14 06:41:59.117842
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base:
        def __init__(self, val):
            self.val = val

        @lazyperclassproperty
        def xml_tag_name(cls):
            return cls.__name__

        @lazyperclassproperty
        def val2(cls):
            return cls.val**2

    class Child1(Base):
        pass

    class Child2(Base):
        def __init__(self):
            super(Child2, self).__init__(1)

    class Child3(Child1):
        def __init__(self):
            super(Child3, self).__init__(1)

    b = Base(0)
    c = Child1(1)
    c2 = Child2()
    c3 = Child3()
    print(b.xml_tag_name)


# Generated at 2022-06-14 06:42:03.333015
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def Foo(cls):
            return object()

    class B(A):
        pass

    print(id(A.Foo))
    print(id(B.Foo))
    print(id(A.Foo) == id(B.Foo))



# Generated at 2022-06-14 06:42:09.107307
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from unittest import TestCase

    class Test(TestCase):
        @staticmethod
        def calculate():
            return 123

        @lazyclassproperty
        def value(self):
            return self.calculate()

        def test_function(self):
            assert Test.value == 123

    Test().run()

# Generated at 2022-06-14 06:42:15.730559
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return True

    assert(not hasattr(A, '_lazy_prop'))
    assert(A.prop)
    assert(hasattr(A, '_lazy_prop'))



# Generated at 2022-06-14 06:42:26.742244
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def foo(cls):
            return list()

        def a(self):
            self.foo.append("a")

    if __name__ == '__main__':
        b = Base()
        b.a()
        assert b.foo == ["a"]

        class Derived(Base):
            def b(self):
                self.foo.append("b")

            def c(self):
                self.foo.append("c")

        d = Derived()
        d.a()
        assert d.foo == ["a"]
        d.b()
        assert d.foo == ["a", "b"]
        d.c()
        assert d.foo == ["a", "b", "c"]

        e = Derived()
        e.a()
       

# Generated at 2022-06-14 06:42:38.603777
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        def __init__(self):
            self.val = 0

        @lazyperclassproperty
        def test(self):
            self.val += 1
            return self.val

    class DerivedA(Base):
        pass
    class DerivedB(Base):
        pass

    base = Base()
    deriveda = DerivedA()
    derivedb = DerivedB()

    assert base.test == 1
    assert base.test == 1
    assert deriveda.test == 1
    assert deriveda.test == 1
    assert derivedb.test == 1
    assert derivedb.test == 1
    assert base.test == 1



# Generated at 2022-06-14 06:42:47.502001
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return 'A'

    class B(A):
        @lazyperclassproperty
        def a(cls):
            return 'B' + super(B, cls).a

    class C(A):
        @lazyperclassproperty
        def a(cls):
            return 'C' + super(C, cls).a

    assert A().a == 'A'
    assert B().a == 'BA'
    assert C().a == 'CA'


# Generated at 2022-06-14 06:42:54.305099
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def method(cls):
            return 'HELLO'

    class B(A):
        pass

    a = A()
    b = B()

    assert a.method == 'HELLO'
    assert b.method == 'HELLO'

    assert a.method == b.method

if __name__ == '__main__':
    test_lazyclassproperty()

# Generated at 2022-06-14 06:43:38.281994
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:43:42.090760
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def value(self):
            print('generate value')
            return 10

    class B(A):
        pass

    assert A.value == 10
    assert B.value == 10



# Generated at 2022-06-14 06:43:49.903782
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Define a new class
    class Foo(object):
        # Create a lazy class property
        @lazyclassproperty
        def bar(cls):
            return 'baz'

    assert Foo.bar == 'baz'
    Foo.bar = 'foobar'
    assert Foo.bar == 'foobar'

    # Define a new class inheriting from Foo
    class FooBar(Foo):
        pass

    assert FooBar.bar == 'baz'
    FooBar.bar = 'foobar'
    assert FooBar.bar == 'foobar'
    assert Foo.bar == 'baz'



# Generated at 2022-06-14 06:43:54.249309
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Tests class property to ensure that the correct value is returned.
    This test will fail if the lazyclassproperty is not working properly.
    """

    class Test:
        @lazyclassproperty
        def prop(cls):
            return "Test class property"

    assert Test.prop == "Test class property"



# Generated at 2022-06-14 06:44:00.174379
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    @lazyclassproperty
    def test_fn(cls):
        return 'value'

    assert hasattr(test_fn, '__name__')
    assert test_fn.__name__ == 'test_fn'
    assert test_fn == 'value'



# Generated at 2022-06-14 06:44:10.319769
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from .printing import AttrTable
    import datetime
    import random

    class TestClass(object):
        @lazyclassproperty
        def lazy_class_value(cls):
            print("Calculating lazy_class_value for %s" % cls.__name__)
            return datetime.datetime.now()

    print("\n==> Running unit test for lazyclassproperty")
    print("\nTestClass.lazy_class_value:\n", TestClass.lazy_class_value)
    print("\nTestClass.lazy_class_value:\n", TestClass.lazy_class_value)
    print("\nTestClass.lazy_class_value:\n", TestClass.lazy_class_value)

    # Now do the same but with a sub-class

# Generated at 2022-06-14 06:44:16.207751
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    """
    Test lazyperclassproperty.
    """
    class A(object):
        @lazyperclassproperty
        def test(cls):
            print("evaluating test()")
            return 42

    class B(A):
        pass

    a = A()
    b = B()

    # a's test prop is evaluated & cached
    assert a.test == 42
    # b's test prop is fresh
    assert b.test == 42
    # a's test prop is the same
    assert a.test == 42
    assert a.test == b.test


# Unit test code for function lazyclassproperty

# Generated at 2022-06-14 06:44:19.924116
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class MyClass(object):
        def __init__(self):
            self.__name = 'MyClass'

        @lazyperclassproperty
        def name(cls):
            return cls().__name

    class MyChildClass(MyClass):
        def __init__(self):
            self.__name = 'MyChildClass'

    assert MyClass().name == 'MyClass'
    assert MyChildClass().name == 'MyChildClass'
    # Test caching of class variable
    assert MyChildClass().name == 'MyChildClass'

    instance = MyChildClass()
    assert instance.name == 'MyChildClass'
    instance.__name = 'MyLifeClass'
    assert instance.name == 'MyChildClass'



# Generated at 2022-06-14 06:44:26.193955
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @functiontools.lazyclassproperty
        def value(self):
            return 7

    assert A.value == 7
    assert A.value == 7
    A.value = 9
    assert A.value == 9

    class B(A):
        pass

    assert B.value == 9
    A.value = 11
    assert B.value == 9
    assert A.value == 11

# Generated at 2022-06-14 06:44:33.590393
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 'property'

    class B(A):
        pass

    assert A.prop == 'property'
    assert B.prop == 'property'
    assert (id(A.prop) != id(B.prop))  # id of each instance is different

