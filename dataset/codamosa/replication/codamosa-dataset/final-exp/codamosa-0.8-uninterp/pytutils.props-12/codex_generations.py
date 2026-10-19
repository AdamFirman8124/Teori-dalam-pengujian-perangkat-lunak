

# Generated at 2022-06-14 06:35:48.911930
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class TestClass(object):
        def __init__(self):
            self.y = 'test_y'

        @lazyclassproperty
        def x(cls):
            print('TestClass.x getter called')
            return cls.y

        @classmethod
        def x_getter(cls):
            print('TestClass.x_getter called')
            return cls.x

        @x.setter
        def x(cls, value):
            print('TestClass.x setter called')
            return cls.y

    # 1st access
    print('TestClass.x = %s' % TestClass.x)
    print('TestClass.x = %s' % TestClass.x)
    # 1st getter called, 2nd getter not called

    # Setter
    TestClass

# Generated at 2022-06-14 06:35:57.307865
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def a(cls):
            return 'A'

        @lazyclassproperty
        def b(cls):
            return 'B'

    class B(A):
        @lazyclassproperty
        def b(cls):
            return 'd'

    assert A.a == 'A'
    assert A.b == 'B'
    assert B.a == 'A'
    assert B.b == 'd'



# Generated at 2022-06-14 06:36:00.072071
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C:
        @lazyclassproperty
        def f(cls):
            return 'foo'

    assert C.f == 'foo'
    assert C.__dict__['_lazy_f'] == 'foo'


# Generated at 2022-06-14 06:36:06.195485
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:36:11.830604
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        @lazyperclassproperty
        def foo(self):
            return self.__class__.__name__

    class B(A):
        pass

    """
    Now we instantiate 2 classes that share the same property 'foo' BUT are are different classes, so there will be NO
    shared data (no collision).
    """

    a = A()
    b = B()
    assert a.foo == "A"
    assert b.foo == "B"



# Generated at 2022-06-14 06:36:19.885287
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return cls.__name__

    assert Foo.bar == 'Foo'
    assert Foo._lazy_bar == 'Foo'

    # the property is cached
    del Foo._lazy_bar

    assert Foo.bar == 'Foo'
    assert Foo._lazy_bar == 'Foo'



# Generated at 2022-06-14 06:36:25.690667
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        @lazyperclassproperty
        def foo(cls):
            return 24

    class B(A):
        @lazyperclassproperty
        def foo(cls):
            return 42

    class C(B):
        pass

    class D(C):
        @lazyperclassproperty
        def foo(cls):
            return 12

    assert A.foo == 24
    assert B.foo == 42
    assert C.foo == 42
    assert D.foo == 12


# Generated at 2022-06-14 06:36:31.226361
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def prop(cls):
            print(cls.__name__)
            return cls.__name__

    class B(A):
        pass

    assert A.prop == "A"
    assert B.prop == "B"



# Generated at 2022-06-14 06:36:41.854511
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def _foo(cls):
            return 'A'


    class B(A):
        @lazyperclassproperty
        def _foo(cls):
            return 'B'

    assert A()._foo == 'A'
    assert B()._foo == 'B'
    assert A._foo == 'A'
    assert B._foo == 'B'
    assert A._A__foo == 'A'
    assert B._B__foo == 'B'
    assert A()._A__foo == 'A'
    assert B()._B__foo == 'B'
    assert A()._foo == 'A'
    assert B()._foo == 'B'
    assert A()._foo == 'A'
    assert B()._foo == 'B'


# Generated at 2022-06-14 06:36:50.817959
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Test(object):
        def __init__(self):
            self.x = 1000

        @lazyperclassproperty
        def run_once(cls):
            print("run once for %s" % cls.__name__)
            return cls.x

    t1 = Test()
    t2 = Test()
    t2.x = 2000

    assert Test.run_once == 1000
    assert t1.run_once == 1000
    assert t2.run_once == 2000



# Generated at 2022-06-14 06:37:00.209924
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def a(cls):
            print("A.a")
            return cls

    class B(A):
        @lazyperclassproperty
        def b(cls):
            print("B.b")
            return cls

    A.a is B.a == A
    B.a is B
    A.b == B.b is B



# Generated at 2022-06-14 06:37:03.636716
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo:

        @lazyperclassproperty
        def bar(cls):
            return cls.__name__

    class FooSubclass(Foo):
        pass

    assert Foo.bar == 'Foo'
    assert FooSubclass.bar == 'FooSubclass'



# Generated at 2022-06-14 06:37:07.520666
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:37:18.997128
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def string(cls):
            return cls.__name__

    assert Base.string == 'Base'
    assert Base().string == 'Base'

    class Foo(Base):
        pass

    assert Foo.string == 'Foo'
    assert Foo().string == 'Foo'
    assert Base.string == 'Base'
    assert Base().string == 'Base'

    class Bar(Base):
        pass

    assert Bar.string == 'Bar'
    assert Bar().string == 'Bar'
    assert Foo.string == 'Foo'
    assert Foo().string == 'Foo'
    assert Base.string == 'Base'
    assert Base().string == 'Base'



# Generated at 2022-06-14 06:37:24.661994
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            return 1

    class B(A):
        pass

    class C(B):
        @lazyperclassproperty
        def a(cls):
            return 2

    assert A.a == 1
    assert B.a == 1
    assert C.a == 2


# Generated at 2022-06-14 06:37:36.210480
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    # Define a class
    class C(object):
        # Define a 'normal' class property
        @classmethod
        def cls_meth1(cls):
            return 10

        # Define a 'lazy' class property using lazyclassproperty
        @lazyclassproperty
        def cls_meth2(cls):
            return 'lazy'

    # creating an instance
    c = C()
    assert c.cls_meth1 == 10
    assert c.cls_meth2 == 'lazy'
    assert C.cls_meth1 == 10
    assert C.cls_meth2 == 'lazy'

    # redefine the 'lazy' class property
    def cls_meth2(cls):
        return 'lazy2'

    C.cls_

# Generated at 2022-06-14 06:37:39.372886
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class S(object):
        @lazyperclassproperty
        def value(cls):
            return 1

    class T(S): pass


# Generated at 2022-06-14 06:37:46.540783
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class base(object):
        @lazyperclassproperty
        def foo(cls_):
            print("Called base.foo")
            return "base.foo"

    class d1(base):
        pass

    class d2(base):
        pass

    assert d1.foo == d2.foo == base.foo == "base.foo"
    d1.foo = "bar"
    assert d1.foo == "bar"
    assert d2.foo == base.foo == "base.foo"


# Generated at 2022-06-14 06:37:59.139885
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return "bar"

    assert Foo.bar == 'bar'
    try:
        del Foo.bar
    except AttributeError:
        assert True
    else:
        assert False
    assert Foo.bar == 'bar'
    assert Foo.bar is Foo.bar

    class Spam(Foo):
        pass

    assert Spam.bar == 'bar'
    assert Spam.bar is Spam.bar
    assert Foo.bar is Spam.bar

    try:
        del Foo.bar
    except AttributeError:
        assert True
    else:
        assert False
    try:
        del Spam.bar
    except AttributeError:
        assert True
    else:
        assert False


# Generated at 2022-06-14 06:38:04.746563
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def value(cls):
            return cls.__name__ + "value"

    assert A.value == "Avalue"
    assert A.__dict__["_lazy_value"] == "Avalue"

    class B(A):
        pass

    assert B.value == "Bvalue"
    assert B.__dict__["_lazy_value"] == "Bvalue"
    assert A.__dict__["_lazy_value"] == "Avalue"


if __name__ == '__main__':
    test_lazyclassproperty()

# Generated at 2022-06-14 06:38:14.098633
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def hello(cls):
            return 'Hello %s' % cls.__name__

    class B(A):
        pass

    assert A.hello == 'Hello A'
    assert B.hello == 'Hello B'



# Generated at 2022-06-14 06:38:19.518124
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        @lazyclassproperty
        def x(cls):
            print("Calling x()")
            return 1
    assert MyClass.x == 1
    assert MyClass.x == 1
    del MyClass.x
    assert MyClass.x == 1



# Generated at 2022-06-14 06:38:23.986145
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def fn(cls):
            return 1

    class B(A):
        pass

    assert A.fn == 1
    assert B.fn == 1



# Generated at 2022-06-14 06:38:32.956914
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 'a'

    class B(A):
        @lazyclassproperty
        def b(cls):
            return 'b'

    class C(B):
        pass

    assert(A.a == 'a')
    assert(B.a == 'a')
    assert(C.a == 'a')
    assert(A.b == 'b')
    assert(B.b == 'b')
    assert(C.b == 'b')



# Generated at 2022-06-14 06:38:39.877413
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            o = object()

# Generated at 2022-06-14 06:38:44.967306
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestLazyClassProperty:

        @lazyclassproperty
        def class_property(cls):
            return "Lazy class property"

    test_object = TestLazyClassProperty()
    assert TestLazyClassProperty.class_property == "Lazy class property"



# Generated at 2022-06-14 06:38:50.186693
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def value(cls):
            return object()

    class B(A):
        pass

    assert A.value is not B.value
    assert A.value is A.value
    assert B.value is B.value


# Generated at 2022-06-14 06:38:55.862463
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def lazy_prop1(cls):
            print("lazy_prop1 evaluated")
            return "lazy_prop1 result"

    assert A.lazy_prop1 == "lazy_prop1 result"



# Generated at 2022-06-14 06:39:04.763291
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass:
        @lazyclassproperty
        def func(cls):
            print('generate value for TestClass.func')
            return 1

    class SubTestClass(TestClass):
        @lazyclassproperty
        def func(cls):
            print('generate value for SubTestClass.func')
            return 2

    print('TestClass.func value:', TestClass.func)
    print('SubTestClass.func value:', SubTestClass.func)
    print('SubTestClass.func value:', SubTestClass.func)

if __name__ == '__main__':
    test_lazyclassproperty()

# Generated at 2022-06-14 06:39:15.350739
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Base(object):

        @lazyperclassproperty
        def foo(cls):
            """ Docstring of foo """
            return 42

    class Derived(Base): pass

    assert Base.foo == 42
    assert Base.foo == 42 # Test we get the same value

    assert Derived.foo == 42  # Get the value of Base.foo
    assert Derived.foo == 42  # Test we get the same value

    assert Base.foo is not Derived.foo # Test we get different values

    assert Base.foo.__doc__ == fn.__doc__



# Generated at 2022-06-14 06:39:30.717110
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(cls):
            r = "foo"

# Generated at 2022-06-14 06:39:34.924861
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class DummyClass:

        @lazyclassproperty
        def eval_expr(cls):
            print('executing ' + cls.__name__)
            return 1

    d = DummyClass()
    assert d.eval_expr == 1
    # The method is not called again.
    assert d.eval_expr == 1



# Generated at 2022-06-14 06:39:41.509617
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    # Example of base class
    class Base(object):
        @lazyclassproperty
        def lazy_prop(cls):
            return 'original'

    # Example of "inheriting" class
    class Inheritor(Base):
        pass

    # Test
    assert Base.lazy_prop == "original"
    assert Inheritor.lazy_prop == "original"
    Base.lazy_prop = "modified"
    assert Base.lazy_prop == "modified"
    assert Inheritor.lazy_prop == "original"



# Generated at 2022-06-14 06:39:55.669172
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # pylint: disable=too-few-public-methods,too-many-ancestors,too-many-instance-attributes,too-many-arguments
    """Test lazyperclass property"""

    class Foo(object):
        """Class Foo"""
        def __init__(self, name):
            self.name = name

    class Bar(Foo):
        """Class Bar"""

    class Baz(Foo):
        """Class Baz"""

    @lazyperclassproperty
    def name(cls):
        """Lazy per class property for name"""
        return cls.__name__

    # Test
    assert Bar.name == 'Bar'
    assert Baz.name == 'Baz'

    # Test inheritance
    assert Foo.name == 'Foo'
    assert Bar.name == 'Bar'

    # Test

# Generated at 2022-06-14 06:39:58.910958
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Test(object):
        @lazyperclassproperty
        def test(cls):
            return cls.__name__

    class Test2(Test):
        pass

    assert Test.test == Test2.test == 'Test'


# Decorators

# Generated at 2022-06-14 06:40:11.331970
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:40:18.389343
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:40:21.483033
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def data(cls):
            print ("Constructing B.data")
            return 5

    assert A.data == 5

    class B(A):
        pass

    assert B.data == 5



# Generated at 2022-06-14 06:40:26.627430
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def a(self):
            x = self.__class__.__name__

# Generated at 2022-06-14 06:40:32.258325
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyClass(object):
        pass

    class MySubClass(MyClass):
        pass

    @lazyclassproperty
    def lazy_fn(cls):
        return cls

    assert MyClass.lazy_fn is MyClass
    assert MySubClass.lazy_fn is MyClass
    assert lazy_fn is l

# Generated at 2022-06-14 06:40:55.908177
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestClass(object):
        @lazyclassproperty
        def test_prop(cls):
            return {'test': 'test'}

    assert TestClass.test_prop is TestClass.test_prop is TestClass.test_prop

    class TestSubClass(TestClass):
        pass

    assert TestSubClass.test_prop is TestSubClass.test_prop is TestSubClass.test_prop

    assert TestClass.test_prop is not TestSubClass.test_prop



# Generated at 2022-06-14 06:41:00.926734
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class TestLazyClassProperty(object):
        @lazyclassproperty
        def num(self):
            print("calculate")
            return 42

    t1 = TestLazyClassProperty()
    t2 = TestLazyClassProperty()

    assert t1.num == 42
    assert t2.num == 42



# Generated at 2022-06-14 06:41:10.824885
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class FooMeta(type):
        def __new__(cls, name, bases, attrs, **kwargs):
            return super().__new__(cls, name, bases, attrs)

        @lazyperclassproperty
        def class_foo(cls):
            return cls

    class Foo(object, metaclass=FooMeta):
        pass

    class Bar(Foo):
        pass

    class Baz(Foo):
        pass

    assert Foo.class_foo is Foo
    assert Bar.class_foo is Bar
    assert Baz.class_foo is Baz



# Generated at 2022-06-14 06:41:20.354951
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        def __init__(self, x):
            self.x = x

    class C1(Base):
        pass

    class C2(Base):
        pass

    @lazyperclassproperty
    def x(cls):
        return cls.__name__ + ':x'

    c1 = C1(x=None)
    c2 = C2(x=None)
    assert c1.x == 'C1:x'
    assert c2.x == 'C2:x'
    c1.x = 'updated'
    assert c1.x == 'updated'



# Generated at 2022-06-14 06:41:24.804583
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        def __init__(self):
            self.x = 0
        @lazyclassproperty
        def foo(cls):
            return cls().x

    assert Test.foo == 0


# Generated at 2022-06-14 06:41:29.882856
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:40.208470
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        @lazyperclassproperty
        def lazyprop(cls):
            print("lazyprop called")
            return cls.__name__ + "_value"

    class B(A):
        pass

    class C(A):
        pass

    class D(C):
        pass

    a = A()
    b = B()
    c = C()
    d = D()

    assert A.lazyprop == 'A_value'
    assert A.lazyprop == 'A_value'
    assert B.lazyprop == 'B_value'
    assert C.lazyprop == 'C_value'
    assert D.lazyprop == 'D_value'
    assert a.lazyprop == 'A_value'
    assert b.lazyprop == 'B_value'
   

# Generated at 2022-06-14 06:41:44.271861
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        _x = 1
        @lazyclassproperty
        def x(self):
            return A._x

    assert A.x == 1
    A._x = 2
    assert A.x == 2



# Generated at 2022-06-14 06:41:47.153401
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:53.536812
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return id(cls)

    class B(A):
        pass

    class C(object):
        @lazyperclassproperty
        def x(cls):
            return id(cls)

    assert A.x != B.x
    assert A.x != C.x



# Generated at 2022-06-14 06:42:40.522639
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        _some_data = None

        @lazyclassproperty
        def some_data(cls):
            """
            Lazy property which has different values in different inheriters.
            """
            return ['x'] * 3

        @classproperty
        def some_data2(cls):
            """
            Class property which has different values in different inheriters.
            """
            return ['y'] * 3

    class B(A):
        pass

    assert A.some_data is A.some_data
    assert B.some_data is B.some_data
    assert A.some_data is not B.some_data

    assert A.some_data2 is A.some_data2
    assert B.some_data2 is B.some_data2

# Generated at 2022-06-14 06:42:45.030951
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:42:51.189385
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):

        @lazyclassproperty
        def __classname(cls):
            return cls.__name__

    class B(A):
        pass

    class C(A):
        pass

    assert A.__classname == "A"
    assert B.__classname == "B"
    assert C.__classname == "C"
    assert A.__classname is B.__classname
    assert A.__classname is not C.__classname



# Generated at 2022-06-14 06:43:01.909611
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class BaseFoo(object):
        @lazyperclassproperty
        def baz(cls):
            print("baz:", cls)
            return cls.__name__

    class Foo(BaseFoo):
        pass


    class Bar(BaseFoo):
        pass

    print(BaseFoo.baz)
    print(Foo.baz)
    print(Bar.baz)
    # prints:
    # baz: &lt;class '__main__.BaseFoo'&gt;
    # BaseFoo
    # baz: &lt;class '__main__.Foo'&gt;
    # Foo
    # baz: &lt;class '__main__.Bar'&gt;
    # Bar

# Generated at 2022-06-14 06:43:15.442886
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self):
            self.value = None

        @lazyperclassproperty
        def response(cls):
            cls.value = 'foo'
            return cls.value

    class B(A):
        pass

    a = A()
    assert A.value is None
    assert a.value is None
    assert B.value is None
    assert A.response is 'foo'
    assert B.response is 'foo'
    assert A.value is 'foo'
    assert B.value is 'foo'
    assert a.response is 'foo'
    assert a.value is 'foo'
    A.value = 'bar'
    assert a.response is 'foo'
    assert a.value is 'bar'

    b = B()

# Generated at 2022-06-14 06:43:18.539227
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class A(object):
        @lazyperclassproperty
        def meth(cls):
            return cls
    class B(A):
        pass

    assert A.meth == A
    assert B.meth == B

    a = A()
    assert a.meth == A



# Generated at 2022-06-14 06:43:25.017253
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def non_calculated_value(cls):
            print('Calculating non_calculated_value...')
            return 42

        calculated_value = 10

    class B(A):
        calculated_value = 15

    assert A.calculated_value == 10
    assert B.calculated_value == 15
    assert A.non_calculated_value == 42
    assert A.non_calculated_value == 42
    assert B.non_calculated_value == 42



# Generated at 2022-06-14 06:43:30.141352
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    class Parent(object):
        def __init__(self):
            self.prop = 'parent_prop'

    class Child(Parent):
        @lazyperclassproperty
        def test(cls):
            return getattr(cls, 'prop', None)

    class GrandChild(Child):
        prop = 'grand_child_prop'

    assert Child.test == 'parent_prop'
    assert GrandChild.test == 'grand_child_prop'



# Generated at 2022-06-14 06:43:38.158551
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def foo(cls):
            print("Assigning %s.foo" % cls.__name__)
            return 42

    assert A.foo == 42
    assert A.foo == 42
    assert A.foo == 42

    class B(A):
        pass

    assert B.foo == 42
    assert B.foo == 42
    assert B.foo == 42

    A.foo = 24
    assert A.foo == 24
    assert A.foo == 24
    assert A.foo == 24

    assert B.foo == 42
    assert B.foo == 42
    assert B.foo == 42

    del A.foo
    assert A.foo == 42
    assert A.foo == 42
    assert A.foo == 42

    del B.foo
    assert B.foo

# Generated at 2022-06-14 06:43:49.140469
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():

    # Test classes declaration
    class TestClassParent(object):

        def __init__(self, a):
            self.a = a

        @staticmethod
        def staticmethod(b):
            return TestClassParent.__name__+b

        @classmethod
        def classmethod(cls, b):
            return cls.__name__+b

        @lazyperclassproperty
        def lazyperclass(cls):
            return 1

        @lazyclassproperty
        def lazyclass(cls):
            return 1

    class TestClass1(TestClassParent):

        def __init__(self, a):
            super(TestClass1, self).__init__(a)

    class TestClass2(TestClassParent):

        def __init__(self, a):
            super(TestClass2, self).__init__

# Generated at 2022-06-14 06:45:12.950738
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            return cls.__name__

    class B(A): pass
    assert A.x == 'A', A.x
    assert B.x == 'B', B.x


# Generated at 2022-06-14 06:45:19.961029
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        count = 0

        @lazyperclassproperty
        def prop(cls):
            cls.count += 1
            return 'A'

    class B(A):
        pass

    assert A.prop == 'A'
    assert A.count == 1
    assert B.prop == 'A'
    assert B.count == 1


# Generated at 2022-06-14 06:45:28.720621
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop1(cls):
            print('Calculating prop1')
            return 1

        @lazyclassproperty
        def prop2(cls):
            print('Calculating prop2')
            return 2

    class B(A):
        @lazyclassproperty
        def prop1(cls):
            print('Calculating prop1')
            return 1

    a = A()
    b = B()

    print(a.prop1)
    print(a.prop1)
    print(a.prop2)
    print(a.prop2)

    print(b.prop1)
    print(b.prop1)
    print(b.prop2)
    print(b.prop2)



# Generated at 2022-06-14 06:45:42.371539
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class UpperClass(object):
        def __init__(self, value=None):
            self._value = value

        @lazyperclassproperty
        def value(cls):
            return cls._value

    class SubClass1(UpperClass):
        _value = 'static'

    class SubClass2(UpperClass):
        _value = 'static'

    sub1 = SubClass1()
    sub2 = SubClass2()

    # Test lazyperclassproperty
    assert sub1.value == 'static'
    assert sub2.value == 'static'
    assert sub1.value is sub2.value
    assert sub1.value is SubClass1.value

    # Test if lazyperclassproperty is per class
    sub1.value = 'dynamic'
    assert sub1.value == 'dynamic'