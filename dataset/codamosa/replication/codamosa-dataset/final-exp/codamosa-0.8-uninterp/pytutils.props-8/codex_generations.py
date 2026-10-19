

# Generated at 2022-06-14 06:35:48.539359
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    import unittest

    class TestLazyClassProperty(unittest.TestCase):
        def setUp(self):
            self.basesset = set([1, 2, 3])
            self.sub1sset = set([4, 5, 6])
            self.sub2sset = set([7, 8, 9])

            self.sub1set = None
            self.sub2set = None

        def call_times(self):
            if not hasattr(self.__class__, '_call_times'):
                self.__class__._call_times = 0
            self.__class__._call_times += 1
            return self.__class__._call_times

        @lazyclassproperty
        def basesprop(cls):
            return cls.basesset


# Generated at 2022-06-14 06:36:02.093223
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base:
        pass

    @lazyperclassproperty
    def base_dict(cls):
        return {'hahaha': 1}

    class Test(Base):
        def __init__(self):
            self.hahaha = 2

    class Test2(Base):
        def __init__(self):
            self.hahaha = 3

    test = Test()
    test2 = Test2()
    assert test.hahaha == 2
    assert test2.hahaha == 3
    assert Base.base_dict == {'hahaha': 1}
    assert Test.base_dict == {'hahaha': 1}
    assert Test2.base_dict == {'hahaha': 1}
    assert test._Test_lazy_base_dict == {'hahaha': 1}

# Generated at 2022-06-14 06:36:04.597932
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class T(object):
        @lazyclassproperty
        def t1(cls):
            return 'test'
    
    assert T.t1 == 'test'


# Generated at 2022-06-14 06:36:18.217111
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Vehicle(object):
        @classproperty
        def something(cls):
            # test case
            print("cls a is %s" % cls)
            return 10

    class Car(Vehicle):
        pass

    class Truck(Vehicle):
        pass

    class Van(Vehicle):
        @lazyperclassproperty
        def something(cls):
            # test case
            print("cls b is %s" % cls)
            return cls.something + 100

    Vehicle.Car = Car
    Vehicle.Truck = Truck
    Vehicle.Van = Van

    print("checking Car")
    print("Car.something is %s" % Car.something)
    print("Truck.something is %s" % Truck.something)
    print("Van.something is %s" % Van.something)



# Generated at 2022-06-14 06:36:21.171685
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):

        @lazyclassproperty
        def bar(cls):
            return 'baz'

    assert Foo.bar == 'baz'



# Generated at 2022-06-14 06:36:26.430341
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:36:31.947574
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def test(cls):
            return 10

        def add(cls, x):
            return cls.test + x

    assert Test.test == 10
    assert Test().add(10) == 20
    assert Test.test == 10

# Generated at 2022-06-14 06:36:36.789851
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class C(object):
        _x = 50
        @lazyperclassproperty
        def x(cls):
            return cls._x + 1

    class D(C):
        _x = 51

    assert C.x == 51
    assert D.x == 52



# Generated at 2022-06-14 06:36:42.386545
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def test_prop(cls):
            return cls.__name__

    class A(Base):
        pass

    class B(Base):
        pass

    assert A.test_prop == 'A'
    assert B.test_prop == 'B'



# Generated at 2022-06-14 06:36:54.087167
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:37:03.597158
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        def __init__(self):
            self._x = 0

        def _getx(self):
            return self._x

        def _setx(self, value):
            self._x = value

        @lazyclassproperty
        def x(cls):
            return property(cls._getx, cls._setx)

    c = C()
    c.x = 10
    assert c._x == 10
    assert C.x is C.x
    d = C()
    d.x = 20
    assert d._x == 20
    assert c._x == 10
    assert C.x is C.x

# Generated at 2022-06-14 06:37:10.627948
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo(object):
        @lazyperclassproperty
        def bar(cls):
            return 5

        @lazyperclassproperty
        def baz(cls):
            return 10

        def __init__(self, baz=None):
            self.baz = baz

    class Baz(Foo):
        @lazyperclassproperty
        def baz(cls):
            return 15

    foo = Foo()
    assert foo.bar == 5
    assert foo.bar == 5  # assert that it got cached
    assert foo.baz is None
    foo.baz = 20
    assert foo.baz == 20
    foo = Foo(baz=25)
    assert foo.baz == 25

    baz = Baz()
    assert baz.bar == 5
    assert baz.bar == 5

# Generated at 2022-06-14 06:37:14.865438
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A:
        @lazyperclassproperty
        def x(cls):
            return cls.__name__

    class B(A):
        pass

    assert A.x == 'A'
    assert B.x == 'B'



# Generated at 2022-06-14 06:37:23.584481
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    Unit test for lazyclassproperty
    """
    class A(object):
        @lazyclassproperty
        def lazyprop(cls):
            print("lazyprop called")
            return True

    class B(A):
        pass

    class C(A):
        pass

    def test():
        print(A.lazyprop)
        print(B.lazyprop)
        print(C.lazyprop)
        print(A.lazyprop)
        print(B.lazyprop)
        print(C.lazyprop)

    test()



# Generated at 2022-06-14 06:37:33.399254
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return 'value'

    assert A.prop == 'value'
    assert A.prop == 'value'
    assert A.prop == 'value'

    A.prop = 'value2'
    assert A.prop == 'value2'
    assert A.prop == 'value2'
    assert A.prop == 'value2'

    class B(A):
        pass

    assert A.prop == 'value2'
    assert B.prop == 'value'

    assert A().prop == 'value2'
    assert B().prop == 'value'

    A.prop = 'value3'
    assert A.prop == 'value3'
    assert B.prop == 'value'



# Generated at 2022-06-14 06:37:40.019922
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def x(cls):
            #print 'caching'
            return 1234

    class B(A):
        @lazyclassproperty
        def x(cls):
            #print 'override'
            return 5678

    assert A().x == 1234
    assert B().x == 5678
    assert A().x == 1234



# Generated at 2022-06-14 06:37:44.192790
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def attr(cls):
            return 10
    class B(A):
        pass
    assert A.attr == 10
    assert B.attr == 10



# Generated at 2022-06-14 06:37:49.552061
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def a(cls):
            return 'test'

    class B(A):
        pass

    class C(B):
        pass

    assert A.a == 'test'
    assert B.a == 'test'
    assert C.a == 'test'



# Generated at 2022-06-14 06:37:55.337358
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:38:02.922877
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:38:11.831745
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    # code from http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
    class A(object):
        @lazyperclassproperty
        def random_number(cls):
            return random.random()

    class B(A):
        pass
    # Unit test from:
    # http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
    a = A()
    b = B()
    assert a.random_number == b.random_number
    assert a.random_number == A.random_number
    assert b.random_number == B.random_number

# Generated at 2022-06-14 06:38:14.708540
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def prop(cls):
            return cls.__name__

    assert C.prop == "C"


# Generated at 2022-06-14 06:38:20.761167
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class MyObject:
        @lazyclassproperty
        def x(cls):
            print('Init x...')
            return "X X X"

    a = MyObject()
    b = MyObject()
    c = MyObject()
    print(a.x)
    print(b.x)
    print(a.x)
    print(c.x)


# Generated at 2022-06-14 06:38:27.405762
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        __test__ = False

        @lazyclassproperty
        def bar(cls):
            return 'bar'

    assert hasattr(Foo, "bar")
    assert hasattr(Foo, "_lazy_bar")
    assert not hasattr(Foo, "_Foo_lazy_bar")
    assert Foo.bar == "bar"



# Generated at 2022-06-14 06:38:32.004350
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def data(cls):
            return 1
    t1 = Test()
    t2 = Test()
    assert t1.data == t2.data == 1
    t1.data = 2
    assert t2.data == 1



# Generated at 2022-06-14 06:38:37.485477
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        x = 0

    class B(A):
        x = 1

    class C(object):
        y = 0

    @lazyperclassproperty
    def get_x(cls):
        return cls.x

    @lazyperclassproperty
    def get_y(cls):
        return cls.y

    assert get_x(A) == 0
    assert get_x(B) == 1
    assert get_x(C) == 0

    assert get_y(A) == 0
    assert get_y(B) == 0
    assert get_y(C) == 0

# Generated at 2022-06-14 06:38:48.182123
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        def _orig_property(cls):
            return "original property"

        _original_property = lazyclassproperty(_orig_property)

    class B(A):
        def _orig_property(cls):
            return "overridden property"

    # Set the property to a different value in class A
    A._original_property = "changed value"

    # Compare values
    assert A._original_property == B._original_property == "original property"
    assert A._original_property != "changed value"
    assert A._original_property != "overridden property"



# Generated at 2022-06-14 06:39:01.122970
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:39:06.262896
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class ClassA:
        @lazyperclassproperty
        def test(self):
            return random.randint(1, 100)

    class ClassB:
        @lazyperclassproperty
        def test(self):
            return random.randint(1, 100)

    test = ClassA().test
    test1 = ClassB().test

    assert test != test1



# Generated at 2022-06-14 06:39:15.459878
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    from unittest import TestCase
    from weakref import WeakKeyDictionary

    class TestC(TestCase):
        def test_lazyclassproperty(self):
            class A:
                def __init__(self):
                    self.b = B()

            class B(A):
                @lazyclassproperty
                def dict(cls):
                    return WeakKeyDictionary()

            a = A()
            a.b.dict['c'] = a
            self.assertIs(a.b.dict['c'], a)



# Generated at 2022-06-14 06:39:28.303498
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    """
    This test also demonstrates how to use the decorator.
    """
    class TestLazyClassProperty(object):
        @lazyclassproperty
        def prop(cls):
            print("cls: {}".format(cls))
            return "This is a class property"

    t = TestLazyClassProperty()
    print("t.prop: {}".format(t.prop))  # "cls: <class '__main__.TestLazyClassProperty'>\nt.prop: This is a class property"
    print("t.prop: {}".format(t.prop))  # "t.prop: This is a class property"
    print("t.prop: {}".format(t.prop))  # "t.prop: This is a class property"



# Generated at 2022-06-14 06:39:33.685774
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar(cls):
            return cls.baz()

        @classmethod
        def baz(cls):
            return 42

    class Foo2(Foo):
        pass

    assert Foo.bar == Foo.bar == 42
    assert Foo2.bar == Foo2.bar == 42
    assert Foo.bar == Foo2.bar


# Generated at 2022-06-14 06:39:38.753592
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def x(cls):
            return 3

    class B(A):
        @lazyclassproperty
        def x(cls):
            return 4

    assert A.x == 3
    assert B.x == 4
    assert A.x == 3



# Generated at 2022-06-14 06:39:42.275379
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def foo(cls):
            return "bar"

    assert Foo.foo == "bar"



# Generated at 2022-06-14 06:39:48.967809
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class A(object):
        @lazyclassproperty
        def foo(cls):
            print("class %s: calling foo()" % cls.__name__)
            return "foo"

    class B(A):
        pass

    print(A.foo)
    print(B.foo)
    print(A.foo)
    print(B.foo)



# Generated at 2022-06-14 06:39:53.813359
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            print('initializing A.prop')
            return 4
    class B(A):
        @lazyclassproperty
        def prop(cls):
            print('initializing B.prop')
            return 7
    assert A.prop == 4
    assert B.prop == 7



# Generated at 2022-06-14 06:40:01.223206
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return [cls]
    class B(A):
        pass
    class C(A):
        pass
    assert(A.x is not B.x)
    assert(A.x is not C.x)
    assert(B.x is not C.x)
    assert(A.x == [A])
    assert(B.x == [B])
    assert(C.x == [C])
    assert(A.x is A._A_lazy_x)
    assert(B.x is B._B_lazy_x)
    assert(C.x is C._C_lazy_x)


# Generated at 2022-06-14 06:40:03.958897
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    @lazyperclassproperty
    def test(self):
        print('Test')
        return 'Test'

    class Test1(object):
        test = test

    class Test2(object):
        test = test

    assert Test1.test == Test2.test == 'Test'

# Generated at 2022-06-14 06:40:12.204105
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def name(cls):
            return 'A'

    class B(A):
        pass

    class C(A):
        @lazyperclassproperty
        def name(cls):
            return 'C'

    class D(B):
        @lazyperclassproperty
        def name(cls):
            return 'D'

    assert A.name == 'A'
    assert B.name == 'A'
    assert C.name == 'C'
    assert D.name == 'D'



# Generated at 2022-06-14 06:40:15.276030
# Unit test for function lazyclassproperty
def test_lazyclassproperty():

    class Foo(object):
        a = 12
        @lazyclassproperty
        def b(cls):
            return cls.a*2

    assert Foo.b == 24, "lazy property failed"

    class Bar(Foo):
        a = 13
        @lazyclassproperty
        def b(cls):
            return cls.a*3

    assert Bar.b == 39, "lazy property with subclassing failed"


# Unit test of base class and derived class

# Generated at 2022-06-14 06:40:35.539160
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class C(object):
        @lazyclassproperty
        def foo(cls):
            print('foo')
            return 'bar'

    class D(C):
        pass

    class E(C):
        @lazyclassproperty
        def foo(cls):
            print('foo')
            return 'baz'

    # D and C share the same property.
    # E has its own property.
    print(C.foo)
    print(D.foo)
    print(E.foo)



# Generated at 2022-06-14 06:40:43.183766
# Unit test for function lazyperclassproperty

# Generated at 2022-06-14 06:40:56.067796
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def xyzzy(cls):
            return 'minor magic'
    assert A.xyzzy == 'minor magic'
    assert A.xyzzy == 'minor magic'
    assert A.xyzzy == 'minor magic'

    class B(object):
        @lazyclassproperty
        def xyzzy(cls):
            return 'major magic'

    class C(B):
        pass


    class D(B):
        @lazyclassproperty
        def xyzzy(cls):
            return 'minor magic'

    assert B.xyzzy == 'major magic'
    assert B.xyzzy == 'major magic'
    assert B.xyzzy == 'major magic'
    assert C.xyzzy == 'major magic'
    assert C.xyzzy

# Generated at 2022-06-14 06:41:02.934599
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo:
        def __init__(self):
            self.counter = 0
        @classproperty
        def _foo(cls):
            return "BAR"

        @lazyperclassproperty
        def _x(cls):
            self.counter += 1
            return "VALUE"+str(self.counter)

    class Bar(Foo):
        pass

    assert Foo._x == "VALUE1"
    assert Foo._x == "VALUE1"
    assert Bar._x == "VALUE2"
    assert Bar._x == "VALUE2"
    assert Foo._x == "VALUE1"



# Generated at 2022-06-14 06:41:07.085783
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(cls):
            return "hello"

    assert A.prop == "hello"
    assert A.prop == "hello"
    assert A("hello").prop == "hello"



# Generated at 2022-06-14 06:41:12.771800
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:21.499145
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Template:
        @lazyperclassproperty
        def value_template(cls):
            print("Evaluating value_template for {0}".format(cls.__name__))
            # do something expensive
            return "Value for {0}".format(cls.__name__)

    class A(Template):
        pass

    class B(Template):
        pass

    class C(A):
        pass

    class D(B):
        pass

    print("A.value_template: {0}".format(A.value_template))
    print("B.value_template: {0}".format(B.value_template))
    print("C.value_template: {0}".format(C.value_template))
    print("D.value_template: {0}".format(D.value_template))

# Generated at 2022-06-14 06:41:28.458379
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class TestParent(object):
        @lazyperclassproperty
        def Test(cls):
            return 'Parent'
    class TestChild(TestParent):
        @lazyperclassproperty
        def Test(cls):
            return 'Child'
    assert TestParent.Test == 'Parent'
    assert TestChild.Test == 'Child'
    assert TestParent.Test == 'Parent'



# Generated at 2022-06-14 06:41:33.491716
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:41:43.522382
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        def __init__(self):
            self._prop = None

        @lazyperclassproperty
        def prop(cls):
            print('property of class %s' % cls.__name__)
            return cls.__name__

    class B(A):
        pass

    assert A().prop == B().prop == 'A'
    assert A._prop is B._prop is None
    A().prop  # cached
    assert A._prop == 'A'
    assert B._prop is None
    B().prop  # cached
    assert B._prop == 'B'
    assert A._prop == 'A'

    class C(A):
        pass

    assert C().prop != B().prop != A().prop != 'C'
    assert C().prop == 'C'
    assert C._prop

# Generated at 2022-06-14 06:42:25.751346
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Base(object):
        @lazyperclassproperty
        def base_prop(self):
            print("base prop called")
            return 'base prop'

    class Inheritor1(Base):
        pass

    class Inheritor2(Base):
        @lazyperclassproperty
        def base_prop(self):
            print("inheritor2 prop called")
            return 'inheritor2 prop'

    print("Base:")
    b = Base()
    c = Base()
    print("b.base_prop", b.base_prop)
    print("c.base_prop", c.base_prop)
    print("Inheritor1:")
    i1 = Inheritor1()
    i2 = Inheritor1()
    print("i1.base_prop", i1.base_prop)

# Generated at 2022-06-14 06:42:29.895114
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A(object):
        @lazyclassproperty
        def prop(self):
            print("Calling prop.")
            return 42

    assert A.prop == 42
    assert A.prop == 42



# Generated at 2022-06-14 06:42:42.962282
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:42:53.479135
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            print('A: calculating foo')
            return cls, 'A'

    assert A.foo == (A, 'A')

    class B(A):
        @lazyperclassproperty
        def foo(cls):
            print('B: calculating foo')
            return cls, 'B'

    assert B.foo == (B, 'B')
    assert A.foo == (A, 'A')
    assert A().foo == (A, 'A')
    assert B().foo == (B, 'B')



# Generated at 2022-06-14 06:43:00.028740
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class A:
        @lazyclassproperty
        def p(cls):
            return 'A'

    class B(A):
        pass

    assert A.p == 'A'
    A.p = 'C'
    assert A.p == 'C'
    assert B.p == 'A'
    B.p = 'D'
    assert B.p == 'D'


# Generated at 2022-06-14 06:43:08.049781
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:43:15.595061
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def foo(cls):
            print("initializing class A.foo")
            return 'A'

    class B(A):
        @lazyperclassproperty
        def foo(cls):
            print("initializing class B.foo")
            return 'B'

    class C(A):
        pass

    assert A.foo == 'A'
    assert B.foo == 'B'
    assert C.foo == 'A'



# Generated at 2022-06-14 06:43:21.423895
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class OtherClass(object):
        @lazyperclassproperty
        def test_perclass(cls):
            return 'test_perclass_%s' % cls.__name__

        @lazyclassproperty
        def test_all(cls):
            return 'test_all_%s' % cls.__name__

    class TestClass(object):
        @lazyperclassproperty
        def test_perclass(cls):
            return 'test_perclass_%s' % cls.__name__

        @lazyclassproperty
        def test_all(cls):
            return 'test_all_%s' % cls.__name__

    assert TestClass.test_perclass == 'test_perclass_TestClass'
    assert TestClass.test_all == 'test_all_TestClass'

# Generated at 2022-06-14 06:43:30.778821
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Test(object):
        @lazyperclassproperty
        def test_prop(cls):
            return 1

    class Test2(Test):
        pass

    class Test3(Test2):
        pass

    assert Test.test_prop == 1
    assert Test2.test_prop == 1
    assert Test3.test_prop == 1
    Test.test_prop += 1
    Test3.test_prop += 1
    assert Test.test_prop == 2
    assert Test2.test_prop == 1
    assert Test3.test_prop == 2


# Generated at 2022-06-14 06:43:38.263149
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class Foo:
        def __init__(self):
            self.val = None

    class Bar(Foo):
        pass

    class Baz(Foo):
        pass

    @lazyperclassproperty
    def func(cls):
        return cls()

    assert isinstance(Foo.func, Foo)
    assert isinstance(Bar.func, Bar)
    assert isinstance(Baz.func, Baz)
    assert Foo.func is not Bar.func
    assert Foo.func is not Baz.func
    assert Bar.func is not Baz.func
    Foo.func.val = "I am Foo"
    Bar.func.val = "I am Bar"
    Baz.func.val = "I am Baz"
    assert Foo.func.val == "I am Foo"

# Generated at 2022-06-14 06:44:46.727727
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class a(object):
        @lazyperclassproperty
        def test_prop(cls):
            return cls.__name__

    class b(a):
        pass


# Generated at 2022-06-14 06:44:54.912377
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def test(cls):
            return 1

    class B(A):
        pass

    assert A.test == 1
    assert B.test == 1
    A.test = 2
    assert A.test == 2
    assert B.test == 1



# Generated at 2022-06-14 06:45:00.872218
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class B(object):
        @lazyperclassproperty
        def prop(cls):
            return random.random()

    class C1(B):
        pass

    class C2(B):
        pass

    print(B.prop)
    print(C1.prop)
    print(C1.prop)
    print(C2.prop)
    print(C2.prop)

# Generated at 2022-06-14 06:45:06.066969
# Unit test for function lazyclassproperty

# Generated at 2022-06-14 06:45:09.163189
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Test(object):
        @lazyclassproperty
        def test(cls):
            print('Creating a new lazy class property')
            return 42

    assert Test.test == 42
    assert Test.test == 42
    assert Test.test == 42



# Generated at 2022-06-14 06:45:22.148851
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    """
    docstring for test_lazyperclassproperty
    """

    class test_lazyperclassproperty_class(object):
        """
        docstring for test_lazyperclassproperty_class
        """

        @lazyperclassproperty
        def test_lazyperclassproperty_method(self):
            """
            docstring for test_lazyperclassproperty_method
            """
            return 0

    class test_lazyperclassproperty_class_inherited(test_lazyperclassproperty_class):
        """
        docstring for test_lazyperclassproperty_class_inherited
        """
        pass

    obj_base = test_lazyperclassproperty_class()
    obj_inherited = test_lazyperclassproperty_class_inherited()

    assert obj_base.test

# Generated at 2022-06-14 06:45:27.455148
# Unit test for function lazyclassproperty
def test_lazyclassproperty():
    class Foo(object):
        @lazyclassproperty
        def bar_lazy(self):
            return 5

        @lazyclassproperty
        def bar_nonlazy(cls):
            return 7

    assert Foo.bar_lazy == 5
    assert Foo.bar_nonlazy == 7


# Generated at 2022-06-14 06:45:38.110439
# Unit test for function lazyperclassproperty
def test_lazyperclassproperty():
    class A(object):
        @lazyperclassproperty
        def x(cls):
            return 'x per A'

    class B(A):
        @lazyperclassproperty
        def b(cls):
            return 'b per B'

    a = A()
    b = B()

    assert A.x == 'x per A'
    assert B.x == 'x per A'
    assert a.x == 'x per A'
    assert b.x == 'x per A'

    assert B.b == 'b per B'
    assert b.b == 'b per B'

