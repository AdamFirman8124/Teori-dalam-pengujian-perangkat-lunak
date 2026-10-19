

# Generated at 2022-06-14 06:35:47.880288
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def base_attr(cls):
            return cls.__name__
            # return cls


    class Child(Base):
        @lazyperclassproperty
        def child_attr(cls):
            return cls.__name__

    assert Base._Base_lazy_base_attr == 'Base'
    assert Base._Base_lazy_child_attr == 'Child'
    assert Child._Base_lazy_base_attr == 'Base'
    assert Child._Base_lazy_child_attr == 'Child'




# Generated at 2022-06-14 06:35:52.724628
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:35:55.629882
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test:
        @lazyclassproperty
        def foo(cls):
            return cls

    assert Test is Test.foo



# Generated at 2022-06-14 06:36:05.391330
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        def __init__(self):
            self._foo = None

# Generated at 2022-06-14 06:36:18.955611
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @staticmethod
        def lazyprop_static(cls):
            return "A.lazyprop_static"

        @lazyperclassproperty
        def lazyprop_perclass(cls):
            return "A.lazyprop_perclass"

        @lazyclassproperty
        def lazyprop_class(cls):
            return "A.lazyprop_class"

        @property
        def lazyprop_specified(self):
            return "A.lazyprop_specified"

    class B(A):
        @lazyperclassproperty
        def lazyprop_perclass(cls):
            return "B.lazyprop_perclass"

        @lazyclassproperty
        def lazyprop_class(cls):
            return "B.lazyprop_class"


# Generated at 2022-06-14 06:36:26.997708
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Test function lazyclassproperty
    """

    class TestLazyProperty(object):
        """
        Test class for function lazyclassproperty
        """
        @lazyclassproperty
        def random_class_property(self):
            """
            Test lazy class property.
            """
            return random.randint(0, 100)

        @lazyclassproperty
        def fixed_class_property(self):
            """
            Test lazy class property with static value.
            """
            return 7

    def test_random_class_property():
        """
        Test random class property.
        """
        for _ in xrange(100):
            assert TestLazyProperty.random_class_property == TestLazyProperty.random_class_property
        assert TestLazyProperty.random_class_property != TestLazyProperty.fixed_class_

# Generated at 2022-06-14 06:36:37.791133
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def lazy_property(cls):
            return 1

        @lazyclassproperty
        def lazy_property_class_dependent(cls):
            return cls

    assert A.lazy_property == 1
    assert A.lazy_property_class_dependent == A

    class B(A):
        pass

    assert B.lazy_property == 1
    assert B.lazy_property_class_dependent == B

    class C(A):

        @lazyclassproperty
        def lazy_property(cls):
            return 2

    assert C.lazy_property == 2
    assert C.lazy_property_class_dependent == C

# Generated at 2022-06-14 06:36:42.213591
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        i = 0
        @lazyclassproperty
        def inc(cls):
            # don't increment if i was already calculated
            if hasattr(cls, '_lazy_inc'): return
            cls.i += 1
            return cls.i

    class B(A):
        i = 0

    assert A.inc == 1
    assert A.inc == 1 # don't increment
    assert B.inc == 2
    assert B.inc == 2 # don't increment
    assert A.inc == 1
    assert B.i == 2



# Generated at 2022-06-14 06:36:52.919793
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A:
        @lazyclassproperty
        def foo(cls):
            print("function foo is called")
            return "bar"

    # first time foo is accessed, the function is executed, the result is cached in a variable
    # and is returned on the next access
    print(A.foo)
    print(A.foo)

    # this is a new class, so the cached result won't be there
    class B:
        @lazyclassproperty
        def foo(cls):
            print("function foo is called")
            return "bar"

    print(B.foo)
    print(B.foo)



# Generated at 2022-06-14 06:36:58.638782
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def A(self):
            print("A called")
            return 1

        @lazyclassproperty
        def B(self):
            print("B called")
            return 2

    assert Test.A == 1
    assert Test.B == 2

# Generated at 2022-06-14 06:37:10.755086
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            print('Fetching a')
            return 'A'

    class B(A):
        @lazyclassproperty
        def a(cls):
            print('Fetching a')
            return 'B'

    assert A.a == 'A'
    assert B.a == 'B'
    assert A().a == 'A'
    assert B().a == 'B'

if __name__ == '__main__':
    test_lazyclassproperty()



# Generated at 2022-06-14 06:37:13.306446
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def prop(cls):
            return cls.__name__

    class InheritorOne(Base):
        pass

    class InheritorTwo(Base):
        pass

    print(InheritorOne.prop)  # 'InheritorOne'
    print(InheritorTwo.prop)  # 'InheritorTwo'

# Generated at 2022-06-14 06:37:23.529474
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            print("calculating foo for class A")
            return 'foo A'

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def foo(cls):
            print("calculating foo for class C")
            return 'foo C'

    # A.foo and B.foo are not the same
    assert A.foo == 'foo A'
    assert B.foo == 'foo A'
    assert C.foo == 'foo C'

if __name__ == '__main__':
    test_lazyperclassproperty()

# Generated at 2022-06-14 06:37:30.075866
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return "A.a"

    class B(A):
        @lazyclassproperty
        def a(cls):
            return "B.a"

    assert A.a == "A.a"
    assert B.a == "B.a"
    assert A().a == "A.a"
    assert B().a == "B.a"



# Generated at 2022-06-14 06:37:38.065008
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        _counter = 0
        def _get_foo_value(cls):
            cls._counter += 1
            return cls._counter
        foo = lazyperclassproperty(_get_foo_value)

    class B(A):
        _counter = 100
        pass

    assert A.foo == 1
    assert A.foo == 1
    assert B.foo == 101
    assert B.foo == 101
    assert A.foo == 1



# Generated at 2022-06-14 06:37:49.641928
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            print("A.foo")
            return 'foo'

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def foo(cls):
            print("C.foo")
            return 'bar'

    class D(C):
        pass

    r = A.foo
    assert [r] == A.__dict__.values()
    assert r == 'foo'
    assert r == B.foo
    assert [r] == B.__dict__.values()

    r = C.foo
    assert [r] == C.__dict__.values()
    assert r == 'bar'
    assert r == D.foo
    assert [r] == D.__dict__.values()

# Generated at 2022-06-14 06:37:57.211564
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def B(cls):
            return 'test'

    assert A.B == 'test'
    # class A should have attribute '_lazy_B'
    assert hasattr(A, '_lazy_B')
    # class B should not have attribute '_lazy_B'
    assert not hasattr(A.__class__, '_lazy_B')


# Alternative implementation for lazyclassproperty

# Generated at 2022-06-14 06:38:01.275126
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def some_property(cls):
            return object()

    class Derived(Base):
        pass

    assert Base.some_property is not Derived.some_property



# Generated at 2022-06-14 06:38:08.013581
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def x(cls):
            return 1

    assert A.x == 1
    A.x = 2
    assert A.x == 1

    class B(A):
        pass

    assert B.x == 1
    B.x = 2
    assert B.x == 1

    for cls in [A, B]:
        if hasattr(cls, '_lazy_x'):
            del cls._lazy_x



# Generated at 2022-06-14 06:38:12.566724
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Parent(object):
        @lazyperclassproperty
        def foo(cls):
            return "bar " + cls.__name__
    class Child(Parent):
        pass
    assert Parent.foo == "bar Parent"

# Generated at 2022-06-14 06:38:22.734022
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    @lazyclassproperty
    def prop(cls):
        return 'prop'

    class A(object):
        pass

    a = A()
    assert a.prop == 'prop'
    a.prop = 'newprop'
    assert a.prop == 'newprop'
    del a.prop
    assert a.prop == 'prop'
    del A.prop



# Generated at 2022-06-14 06:38:30.543404
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop(cls):
            print("executing prop(%s)" % cls)
            return cls.__name__
    class B(A):
        pass
    class C(A):
        pass
    print("{0.prop!r} {1.prop!r} {2.prop!r}".format(A, B, C))


# Generated at 2022-06-14 06:38:38.192446
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return 'abc'

    # Lazy evaluation
    assert not hasattr(Foo, '_lazy_bar')
    # First evaluation
    assert Foo.bar == 'abc'
    assert hasattr(Foo, '_lazy_bar')
    # Cached
    assert Foo.bar == 'abc'
    # class property
    assert Foo().bar == 'abc'



# Generated at 2022-06-14 06:38:44.310314
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:38:48.440673
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class Test(object):
        @lazyclassproperty
        def lazyproperty(cls):
            return "Hello world"

    assert Test.lazyproperty == "Hello world"
    test_instance = Test()
    assert test_instance.lazyproperty == "Hello world"



# Generated at 2022-06-14 06:39:01.330073
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        pass

    class A(Base):
        @lazyperclassproperty
        def test(cls):
            return cls.__name__

    class B(Base):
        @lazyperclassproperty
        def test(cls):
            return cls.__name__

    class C(A):
        pass

    class D(A):
        pass

    # Now - should be like this
    assert len(Base._Base_lazy_test_cache) == 0
    assert len(A._A_lazy_test_cache) == 1
    assert len(B._B_lazy_test_cache) == 1
    assert len(C._C_lazy_test_cache) == 1
    assert len(D._D_lazy_test_cache) == 1

    # A second run should

# Generated at 2022-06-14 06:39:06.403305
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            return "bar"
    class B(A):
        pass
    assert A.foo == "bar"
    assert B.foo == "bar"
    A.foo = "asdf"
    assert A.foo == "asdf"
    assert B.foo == "bar"



# Generated at 2022-06-14 06:39:17.283028
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 111

    class B(A):
        @lazyclassproperty
        def prop(cls):
            return 222

    class C(B):
        pass

    class D(C, B):
        @lazyclassproperty
        def prop(cls):
            return 333

    assert A.prop == 111
    assert B.prop == 222
    assert C.prop == 222
    assert D.prop == 333
    A.prop = 1
    assert A.prop == 1
    B.prop = 2
    assert B.prop == 2
    C.prop = 3
    assert C.prop == 3
    D.prop = 3
    assert D.prop == 3


# Generated at 2022-06-14 06:39:26.263874
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A: pass
    class B(A): pass
    class C(A): pass

    @lazyperclassproperty
    def fn(cls):
        return cls.__name__

    assert hasattr(B, '_B_lazy_fn')
    assert hasattr(C, '_C_lazy_fn')
    assert not hasattr(A, '_A_lazy_fn')

    assert B._B_lazy_fn == 'B'
    assert C._C_lazy_fn == 'C'

    assert B.fn == 'B'
    assert C.fn == 'C'

    assert '_B_lazy_fn' in B.__dict__
    assert '_C_lazy_fn' in C.__dict__
    assert 'fn' in B.__dict__

# Generated at 2022-06-14 06:39:35.300451
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class _Test(object):
            @lazyclassproperty
            def value(cls):
                return 1

    class _Test2(_Test):
        @lazyclassproperty
        def value(cls):
            return 2

    assert _Test.value == 1
    assert _Test2.value == 2
    assert _Test.value == 1
    assert _Test2.value == 2
    _Test.value = 10
    assert _Test.value == 10
    assert _Test2.value == 2



# Generated at 2022-06-14 06:39:57.410883
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return cls.__name__ + '_x'
        @classmethod
        def y(cls):
            return cls.__name__ + '_y'
    print('A.x = ' + A.x)
    print('A.y = ' + A.y())
    class B(A):
        pass
    print('B.x = ' + B.x)
    print('B.y = ' + B.y())
    print('B.__base__ = ' + B.__base__.__name__)
    obj = A()
    print('obj.x = ' + obj.x)
    # This binds a the new attribute x to the instance, so the class property is lost.

# Generated at 2022-06-14 06:40:08.415434
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Parent(object):
        pass

    class Child(Parent):
        pass

    @lazyperclassproperty
    def foo(cls):
        print('Foo called: %s' % cls)
        return 42

    print('Parent foo: %s' % Parent.foo)
    print('Parent foo: %s' % Parent.foo)
    print('Child foo: %s' % Child.foo)
    print('Child foo: %s' % Child.foo)
    print('Parent foo: %s' % Parent.foo)
    print('Child foo: %s' % Child.foo)

    assert Child.foo != Parent.foo


# Generated at 2022-06-14 06:40:18.316330
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # Make a class with a lazy property
    class X(object):
        @lazyperclassproperty
        def prop(cls):
            return cls.name

        def testprop(self):
            """Return the value of the property."""
            return self.prop

    # Make a subclass of the above
    class Y(X):
        name = "Y"
        def __init__(self):
            # Make sure the property was calculated before this object was created
            assert hasattr(self.__class__, '_%s_lazy_prop' % self.__class__.__name__)

    # Test it
    x = X()
    assert x.prop is None
    x.name = "X"
    assert x.prop == "X"
    y = Y()
    assert y.prop == "Y"
   

# Generated at 2022-06-14 06:40:25.942171
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(self):
            return 'A'

    class B(A):
        pass

    class C(B):
        @lazyclassproperty
        def a(self):
            return 'C'

    a = A()
    b = B()
    c = C()

    assert a.a == 'A'
    assert b.a == 'A'
    assert c.a == 'C'



# Generated at 2022-06-14 06:40:30.014745
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def the_answer(cls):
            return 42

    assert A.the_answer == 42

    class B(A):
        pass

    assert B.the_answer == 42



# Generated at 2022-06-14 06:40:35.628381
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:40:40.442675
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def cached_property(cls):
            return cls

    class Derived(Base):
        pass

    assert Derived.cached_property is Derived
    assert Base.cached_property is Base



# Generated at 2022-06-14 06:40:45.612134
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def f(self):
            return dict()
    class B(A):
        pass
    a = A()
    b = B()
    assert a.f != b.f, "Unit test for lazyperclassproperty: AssertionError"
    return


# Generated at 2022-06-14 06:40:51.504025
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:00.572284
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Father(object):
        def __init__(self, father_number):
            self.father_number = father_number
        @lazyperclassproperty
        def father_number(self):
            return 0
        @lazyperclassproperty
        def son_number(self):
            return 1

    class Son(Father):
        pass

    father1 = Father(1)
    son1 = Son(2)
    father2 = Father(3)
    son2 = Son(4)

    assert father1.father_number == 1
    assert son1.son_number == 1
    assert Father.father_number == 0
    assert Father.son_number == 1
    assert father2.father_number == 3
    assert son2.son_number == 1
    assert Son.father_number == 0
    assert Son.son_

# Generated at 2022-06-14 06:41:21.502646
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def prop(self):
            return 42

    assert C.prop == 42
    assert C().prop == 42



# Generated at 2022-06-14 06:41:26.913955
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def foo(cls):
            return cls()

    class B(A):
        pass

    assert A.foo is not B.foo
    assert isinstance(A.foo, A)
    assert isinstance(B.foo, B)



# Generated at 2022-06-14 06:41:35.356418
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        pass

    class B(A):
        pass

    class C(A):
        pass

    @lazyperclassproperty
    def x(cls):
        import time
        print("Evaluating x in", cls)
        time.sleep(0.1)
        return "X" * 3

    assert A.x == "XXX"
    assert A.x == "XXX"
    assert B.x == "XXX"
    assert C.x == "XXX"
    assert A.x == "XXX"
    assert C.x == "XXX"
    print("OK")


# Generated at 2022-06-14 06:41:48.528202
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
  class A(object):
      @lazyperclassproperty
      def foo(cls):
          print('foo: %s' % cls)
          return cls.__name__

  class B(A):
      pass

  class C(A):
      pass

  print('A.foo: %s' % A.foo)
  print('B.foo: %s' % B.foo)
  print('C.foo: %s' % C.foo)
  print('A.__dict__: %s' % A.__dict__)
  print('B.__dict__: %s' % B.__dict__)
  print('C.__dict__: %s' % C.__dict__)

if __name__ == '__main__':
    test_lazyperclassproperty()


# Generated at 2022-06-14 06:41:54.771103
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        def __init__(self):
            self.x = 0
            self.y = 0

        @lazyclassproperty
        def z(cls):
            return cls.x+cls.y

    a = A()
    a.x = 1
    a.y = 4
    assert a.z == 5
    a.x = 2
    assert a.z == 5
    a.y = 100
    assert a.z == 102


# Generated at 2022-06-14 06:41:59.253158
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def x(cls):
            return 'x'
    assert Test.x == 'x'
    assert Test().x == 'x'


# Generated at 2022-06-14 06:42:08.888685
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    import copy

    class A(object):
        def __init__(self, a, b=None, c=None):
            self.a = a
            self.b = b
            self.c = c

        @lazyclassproperty
        def d(cls):
            return A(cls.a, cls.b, cls.c)

        @classproperty
        def e(cls):
            return cls(cls.a, cls.b, cls.c)

        @classproperty
        def f(cls):
            return cls.a

    class B(A):
        a = 1

        @classproperty
        def b(cls):
            return cls.a + 1

        c = 2

    assert copy.copy(B.d) == B(1)

    A.a

# Generated at 2022-06-14 06:42:23.015451
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        def func(self):
            return 'A'

        @lazyclassproperty
        def prop(cls):
            return cls().func()

    class B(A):
        def func(self):
            return 'B'

    assert getattr(A, '_lazy_prop') == 'A'
    assert A.prop == 'A'
    assert getattr(A, '_lazy_prop') == 'A'
    assert B.prop == 'B'
    assert getattr(B, '_lazy_prop') == 'B'
    assert getattr(A, '_lazy_prop') == 'A'

    #
    # We can also test the function lazyclassproperty() by using it to override the function lazyclassproperty
    #

# Generated at 2022-06-14 06:42:28.851239
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyclassproperty
        def value(cls):
            return "Base"
    class Assign(Base):
        pass
    class AssignOnce(Base):
        @lazyclassproperty
        def value(cls):
            return "AssignOnce"
    class AssignOnceAgain(Base):
        @lazyperclassproperty
        def value(cls):
            return "AssignOnceAgain"
    assert Base.value == "Base"
    assert Assign.value == "Base"
    assert AssignOnce.value == "AssignOnce"
    assert AssignOnceAgain.value == "AssignOnceAgain"

# Generated at 2022-06-14 06:42:34.609647
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 'hello world'

    assert A.a == 'hello world'
    assert type(A.a) is str

    class B(A):
        pass

    assert B.a == 'hello world'



# Generated at 2022-06-14 06:43:18.536395
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def x(cls):
            return 1

    class B(A):
        @lazyclassproperty
        def x(cls):
            return 2

    assert A.x == 1
    assert B.x == 2
    A.x = 3
    assert A.x == 3
    with pytest.raises(TypeError):
        B.x = 3
    assert B.x == 2



# Generated at 2022-06-14 06:43:23.571220
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def foo_classproperty(cls):
            return 'eureka'

    assert hasattr(Foo, '_lazy_foo_classproperty')
    assert Foo.foo_classproperty == 'eureka'



# Generated at 2022-06-14 06:43:28.866100
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class Test(object):

        @lazyclassproperty
        def value(cls):
            return 1

    Test.value += 1
    Test2 = type('Test2', (Test,), {})
    Test.value += 1
    Test2.value += 1

    assert Test.value == 3
    assert Test2.value == 4



# Generated at 2022-06-14 06:43:36.775325
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            print("Computed")
            return 42

    # first time to get the lazy property, it will be computed
    print(Foo.bar)

    # second time to get the lazy property, it will return the computed value without being recomputed
    print(Foo.bar)

    # create a new instance of Foo, and get the lazy property,
    # it will return the computed value also
    print(Foo().bar)

    # recompute the lazy property of class Foo
    Foo.bar = -1
    print(Foo.bar)



# Generated at 2022-06-14 06:43:43.724445
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def val(cls):
            return "A"

    class B(A):
        @lazyperclassproperty
        def val(cls):
            return "B"

    class C(A):
        pass

    assert A.val == "A"
    assert B.val == "B"
    assert C.val == "A"

# Generated at 2022-06-14 06:43:49.101537
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    def __init__(self, name):
        self.name = name

    class Person(object):
        name = "dummy"

        @lazyclassproperty
        def get_name(self):
            return self.name

    Person.name = 'John Doe'
    assert isinstance(Person.get_name, classproperty)
    assert isinstance(Person.get_name, lazyclassproperty)
    assert Person.get_name == 'John Doe'

# Generated at 2022-06-14 06:43:57.944705
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Test lazy class property 
    """
    class Foo(object):
        y = 3

        # defines a lazy class property
        @lazyclassproperty
        def x(cls):
            return cls.y + 5

    # check laziness
    assert not hasattr(Foo, '_lazy_x')

    # access first time
    assert Foo.x == 8

    # lazy class property is cached
    assert Foo.x == 8
    assert hasattr(Foo, '_lazy_x')

    # subclasses can access property but get their own cache
    class FooChild(Foo):
        y = 100

    assert FooChild.x == 105

    # subclasses have their own cache
    assert FooChild.x == 105
    assert not hasattr(FooChild, '_lazy_x')

   

# Generated at 2022-06-14 06:44:09.052250
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def f_per_class(cls):
            print('f_per_class')
            return cls.__name__

        @lazyclassproperty
        def f_global(cls):
            print('f_global')
            return cls.__name__

    assert (A.f_per_class == 'A')
    assert (A.f_global == 'A')

    class B(A):
        pass

    assert (B.f_per_class == 'B')
    assert (B.f_global == 'B')

    print('f_per_class' in vars(B))
    print('f_global' in vars(B))
    print('f_global' in vars(A))



# Generated at 2022-06-14 06:44:17.284677
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test:
        def __init__(self, x):
            self._x = x

        @lazyclassproperty
        def x(cls):
            # only called once
            print ("calling function x in class", cls)
            return cls(1)

    assert Test.x.__class__ is Test
    assert Test.x._x == 1
    assert Test.x._x == 1  # test that x is only called once


# Generated at 2022-06-14 06:44:24.496633
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    >>> class Dummy(object):
    ...    @lazyclassproperty
    ...    def test(cls):
    ...        print("I got called")
    ...        return 1
    >>> Dummy.test
    I got called
    1
    >>> Dummy.test
    1
    >>> class DummyB(Dummy):
    ...    pass
    >>> DummyB.test
    I got called
    1
    >>> DummyB.test
    1
    """
    pass