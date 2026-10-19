

# Generated at 2022-06-13 16:46:34.363637
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    cls = type("TestClass", (object,), {'__metaclass__': Singleton})
    c1 = cls()
    c2 = cls()
    c3 = cls()
    assert c1 is c2 is c3

# Generated at 2022-06-13 16:46:42.181445
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    a = A(1, 2, 3, name='foo')
    b = A(4, 5, 6, name='bar')
    print(b is a)
    print(a.args)
    print(a.kwargs)

# Generated at 2022-06-13 16:46:50.907255
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from threading import Thread
    from time import sleep

    globals()['Singleton'] = Singleton

    class Test(object):
        __metaclass__ = Singleton

    class TestMethod(Thread):
        def __init__(self, method, *args):
            super(TestMethod, self).__init__()

            self.method = method
            self.args = args
            self.stopped = False
            self.result = None

        def run(self):
            self.result = getattr(Test(), self.method)(*self.args)

        def stop(self, timeout=None):
            self.stopped = True
            Thread.join(self, timeout)

    assert Test() is Test()
    assert Test() is not Test.__new__(Test)
    assert Test() is not Test.__new__(Test)

# Generated at 2022-06-13 16:46:53.616389
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    foo1 = Foo(1)
    foo2 = Foo(2)
    assert foo1 is foo2



# Generated at 2022-06-13 16:46:58.112010
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self):
            self.x = 0

    a1 = A()
    a2 = A()
    # Make sure only one instance is created
    assert a1 == a2
    a1.x = 1
    # Make sure changes to the instance are reflected in all references
    assert a2.x == 1



# Generated at 2022-06-13 16:47:02.738128
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self):
            self.test = "test"

    a1 = A()
    a2 = A()
    assert id(a1) == id(a2), "We expect the same object reference"


# Generated at 2022-06-13 16:47:07.015611
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import test_data.test_ansible_module.test_module_utils.test_singleton as s

    a = s.A()
    b = s.A()

    assert id(a) == id(b)



# Generated at 2022-06-13 16:47:10.675698
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    assert None is TestSingleton('test value').value

# Generated at 2022-06-13 16:47:16.252352
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class FooA(object):
        __metaclass__ = Singleton

    class FooB(FooA):
        pass

    fa1 = FooA()
    fb1 = FooB()

    assert id(fa1) == id(fb1)
    assert isinstance(fa1, FooA)
    assert isinstance(fb1, FooB)
    assert not isinstance(fb1, FooA)

# Generated at 2022-06-13 16:47:20.770196
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 2

    a = A()
    b = A()
    assert a.value == 2
    assert b.value == 2
    a.value = 4
    assert a.value == 4
    assert b.value == 4

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:47:26.990354
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Check Singleton.__call__ works as expected.
    """
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    obj1 = TestSingleton()
    obj2 = TestSingleton()
    assert obj1 is obj2

# Generated at 2022-06-13 16:47:33.420572
# Unit test for constructor of class Singleton
def test_Singleton():
    class Dog(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

        def __str__(self):
            return "I'm a dog named {}".format(self.name)

    a = Dog("Rover")
    assert str(a) == "I'm a dog named Rover"

    b = Dog("Rover")
    assert str(b) == "I'm a dog named Rover"

    a.name = "Fluffy"
    assert str(a) == "I'm a dog named Fluffy"
    assert a is b


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:47:38.740521
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(metaclass=Singleton):
        def __init__(self):
            self.attrib = 1
    t1 = Test()
    assert isinstance(t1, Test)
    assert t1.attrib == 1
    t2 = Test()
    assert isinstance(t2, Test)
    assert t2.attrib == 1
    assert t1 == t2
    t1.attrib = 2
    assert t2.attrib == 2
    t2.attrib = 3
    assert t1.attrib == 3


# Generated at 2022-06-13 16:47:43.503861
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    # Instantiate the class
    f1 = Foo()

    # __call__ should only instantiate a single instance
    f2 = Foo()
    f3 = Foo()

    assert f1 == f2
    assert f1 == f3

# Generated at 2022-06-13 16:47:48.380350
# Unit test for constructor of class Singleton
def test_Singleton():
    assert issubclass(Singleton, type)
    assert Singleton.__doc__ == "Metaclass for classes that wish to implement Singleton\nfunctionality.  If an instance of the class exists, it's returned,\notherwise a single instance is instantiated and returned.\n"

# Generated at 2022-06-13 16:47:57.688702
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import collections

    class Test1(object):
        __metaclass__ = Singleton

    class Test2(collections.MutableMapping):
        __metaclass__ = Singleton

    class Test3(collections.Mapping):
        __metaclass__ = Singleton

    class Test4(object):
        pass

    class Test5(collections.MutableMapping):
        pass

    class Test6(collections.Mapping):
        pass

    def test_Test1(t):
        if not issubclass(t, collections.MutableMapping):
            return

        t.__setitem__('foo', 'bar')
        foo1 = t['foo']
        t.__delitem__('foo')


# Generated at 2022-06-13 16:48:00.274482
# Unit test for constructor of class Singleton
def test_Singleton():

    class Testcls(object):
        __metaclass__ = Singleton

    t = Testcls()
    assert t is Testcls()
    assert t is Testcls()
    assert t is Testcls()
    assert t is Testcls()

# Generated at 2022-06-13 16:48:04.254609
# Unit test for constructor of class Singleton
def test_Singleton():
    class Cls(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

    a = Cls("a")
    b = Cls("b")
    assert a.name == "a"
    assert b.name == "a"
    assert a is b


assert __name__ == '__main__'
test_Singleton()

# Generated at 2022-06-13 16:48:06.815033
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a1, a2 = A(), A()

    assert hash(a1) == hash(a2)

# Generated at 2022-06-13 16:48:08.863265
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    assert Foo() is Foo()

# Generated at 2022-06-13 16:48:18.291391
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self, foo):
            self.foo = foo

    assert MyClass.__instance is None

    a = MyClass('a')
    assert id(a) == id(MyClass('a'))
    assert a.foo == 'a'

    a.foo = 'b'
    assert id(a) == id(MyClass('a'))
    assert a.foo == 'b'

# Generated at 2022-06-13 16:48:23.818043
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Bar(object):
        __metaclass__ = Singleton

    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.bar = Bar()

    f = Foo()
    f1 = Foo()

    assert f is f1
    assert f.bar is f1.bar

# Generated at 2022-06-13 16:48:29.260180
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton:
        __metaclass__ = Singleton
        def __init__(self, arg1):
            self.arg1 = arg1

    t1 = TestSingleton('1')
    t2 = TestSingleton('2')
    assert t1 is t2
    assert t1.arg1 == '1'

# Generated at 2022-06-13 16:48:32.715772
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x

    assert A(1) == A(2)
    a = A(3)
    assert a == A(3)
    assert a == A(100)

# Generated at 2022-06-13 16:48:35.234426
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(metaclass=Singleton):
        def __init__(self):
            pass
    t1 = Test()
    assert t1 is Test()


# Generated at 2022-06-13 16:48:40.049213
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(metaclass=Singleton):
        pass

    my_ob1 = MyClass()
    my_ob2 = MyClass()

    assert my_ob1 == my_ob2
    assert id(my_ob1) == id(my_ob2)

# Generated at 2022-06-13 16:48:46.782292
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert id(A()) == id(A())
    assert id(A()) == id(A())
    assert id(A()) == id(A())
    assert id(A()) == id(A())
    assert id(A()) == id(A())
    assert id(A()) == id(A())
    assert id(A()) == id(A())
    assert id(A()) == id(A())
    assert id(A()) == id(A())

if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:48:54.418687
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        value = None

        def __init__(self, value):
            self.value = value

        def __str__(self):
            return str(self.__class__) + ": " + str(self.value)

    class Child(TestSingleton):
        pass

    a = TestSingleton("foo")
    b = TestSingleton("bar")

    assert(a.value == "foo")
    assert(b.value == "foo")
    assert(a is b)

    # this should fail, but it doesn't because of __call__
    a = TestSingleton("foo")
    b = TestSingleton("bar")

    # this proves that child classes are different singletons
    a = Child("foo")
    b = Child("bar")

# Generated at 2022-06-13 16:48:56.612983
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class CSingleton(object):
        __metaclass__ = Singleton

    cs1 = CSingleton()
    cs2 = CSingleton()

    assert cs1 is cs2

# Generated at 2022-06-13 16:48:59.346079
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(metaclass=Singleton):
        def __init__(self):
            pass

    a = Test()
    b = Test()
    assert a is b

# Generated at 2022-06-13 16:49:08.280360
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self):
            self.x = 0
            self.y = 1

    a = A()
    b = A()

    assert a is b
    assert a.x == 0
    assert a.y == 1
    assert b.x == 0
    assert b.y == 1



# Generated at 2022-06-13 16:49:13.822952
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, n):
            self.n = n
        def __str__(self):
            return "%s(%r)" % (self.__class__.__name__, self.n)

    a1 = A(1)
    a2 = A(2)
    a3 = A(3)
    assert id(a1) == id(a2) == id(a3)

    print(a1)
    print(a2)
    print(a3)


# Generated at 2022-06-13 16:49:16.543107
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert a is b



# Generated at 2022-06-13 16:49:25.692960
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, arg1):
            self.arg1 = arg1

    t1 = TestClass("foo")
    t2 = TestClass("bar")

    print("t1:", t1)
    print("t2:", t2)

    assert t1 == t2
    assert t1.arg1 == "bar"

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:49:27.518775
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    print(Test())
    print(Test())


# Generated at 2022-06-13 16:49:32.191576
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(s):
            s.a = 1

    a = A()
    assert(a.a == 1)

    # check that the singleton returns the same instance
    b = A()
    assert(a == b)

    # check that changing an attribute
    b.a = 2
    assert(a.a == 2)

if __name__ == "__main__":
    test_Singleton()
    print("tests passed")

# Generated at 2022-06-13 16:49:35.289380
# Unit test for constructor of class Singleton
def test_Singleton():
    class C(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 'foo'

    a = C()
    b = C()
    assert(a is b)

# Generated at 2022-06-13 16:49:38.865245
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(metaclass=Singleton):
        def __init__(self, a):
            self.a = a

    a = object()
    b = object()
    s1 = S(a)
    assert s1.a == a
    s2 = S(b)
    assert s2.a == a

# Generated at 2022-06-13 16:49:50.547079
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from unittest.mock import patch


# Generated at 2022-06-13 16:50:01.643830
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from nose.tools import assert_equal
    class MyClass(object):
        __metaclass__ = Singleton
        
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2
    
    obj1 = MyClass(arg1=5, arg2=6)
    obj2 = MyClass(arg1=1, arg2=2)
    
    assert_equal(obj1.arg1, 5)
    assert_equal(obj1.arg2, 6)
    assert_equal(obj2.arg1, 5)
    assert_equal(obj2.arg2, 6)
    assert_equal(obj1 is obj2, True)
    

# Generated at 2022-06-13 16:50:05.908929
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert id(a) == id(b)

# Generated at 2022-06-13 16:50:09.331929
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A():
        __metaclass__ = Singleton

    a = A()
    b = A()

    assert a is b



# Generated at 2022-06-13 16:50:14.774291
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.data = 0 

    s1 = TestSingleton()
    assert id(s1) == id(TestSingleton()), 'Singleton class expected to return same instance.'
    assert s1.data == 0, 'Singleton class expected to be initialised to zero.'


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:50:19.467173
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

    c1 = MyClass()
    c2 = MyClass()
    c3 = MyClass()

    assert id(c1) == id(c2)
    assert id(c2) == id(c3)

# Generated at 2022-06-13 16:50:22.378620
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    a = TestClass()
    b = TestClass()
    assert a is b


# Generated at 2022-06-13 16:50:26.391431
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 42

    a = Foo()
    b = Foo()

    assert a.foo == b.foo
    assert a is b

# Generated at 2022-06-13 16:50:33.964677
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.__test_lock = RLock()
            self.__test_var = 0

        def set_test_var(self, val):
            with self.__test_lock:
                self.__test_var = val

        def get_test_var(self):
            with self.__test_lock:
                return self.__test_var


    obj1 = TestSingleton()
    obj2 = TestSingleton()
    assert(obj1 is obj2)

    obj1.set_test_var(42)
    assert(obj2.get_test_var() == 42)

    print("Singleton tests passed.")

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:50:39.970123
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(metaclass=Singleton):
        def __init__(self):
            self.a = 1
    test_instance = Test()
    test_instance.a = 2
    assert test_instance.a == 2
    assert Test().a == 2

# A copy of the above, with a version of Singleton that uses __new__
# instead of __call__.  The current Singleton is the "correct"
# implementation, but this one is simpler and might be easier to
# understand.

# Generated at 2022-06-13 16:50:47.391601
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    # create class MyClass that has Singleton behavior
    class MyClass(object):
        __metaclass__ = Singleton

    # create two instances of MyClass
    instance1 = MyClass()
    instance2 = MyClass()

    # assert that objects of type MyClass are Singleton,
    # so the two instances are equal
    assert instance1 == instance2

    # create two instances of class MyClass that has Singleton
    # behavior, then assert that there are two instances
    class MyClass(object):
        __metaclass__ = Singleton

    instance1 = MyClass()
    instance2 = MyClass()
    assert isinstance(instance1, MyClass)
    assert isinstance(instance2, MyClass)

    # assert that the two instances are equal
    assert instance1 == instance2

# Generated at 2022-06-13 16:50:55.340451
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from tempfile import NamedTemporaryFile
    from multiprocessing import Pool
    from collections import defaultdict
    import re

    class TestSingleton(with_metaclass(Singleton, object)):
        def __init__(self):
            with NamedTemporaryFile(mode='w+t') as f:
                self.filename = f.name

        def log(self, msg):
            with open(self.filename, 'a') as f:
                f.write(msg + '\n')

    def f(action, text, d):
        if action == 'write':
            s = TestSingleton()
            s.log(text)
        else:
            with open(TestSingleton().filename, 'r') as f:
                lines = f.readlines()
                d[id(lines)] = lines

# Generated at 2022-06-13 16:51:03.467563
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

    o1 = MySingleton()
    o2 = MySingleton()
    print('1:', o1)
    print('2:', o2)
    assert o1 is o2

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:51:13.732969
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        """Test class definining a metaclass."""
        __metaclass__ = Singleton

        def __init__(self, value):
            """fake __init__"""
            self.value = value

    class Bar(object):
        """Test class not defining a metaclass."""

        def __init__(self, value):
            """fake __init__"""
            self.value = value

    foo_1 = Foo('one')
    foo_2 = Foo('two')
    assert foo_1 is foo_2
    assert foo_1.value == 'two'

    bar_1 = Bar('one')
    bar_2 = Bar('two')
    assert bar_1 is not bar_2
    assert bar_1.value == 'one'
    assert bar_2.value == 'two'

# Generated at 2022-06-13 16:51:19.259769
# Unit test for constructor of class Singleton
def test_Singleton():
    class Eins(object):
        __metaclass__ = Singleton
    class Zwei(object):
        __metaclass__ = Singleton
    eins = Eins()
    eins_1 = Eins()
    assert eins is eins_1
    zwei = Zwei()
    assert eins is not zwei

# Generated at 2022-06-13 16:51:24.708849
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest
    import random

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = random.randint(1, 101)

    class TestSingleton___call__(unittest.TestCase):

        def test_one_instance(self):
            s1 = TestSingleton()
            s2 = TestSingleton()

            self.assertEqual(s1.x, s2.x)
            self.assertIs(s1, s2)

    unittest.main()

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:51:30.943084
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x
    a = A(1)
    assert(a.x == 1)
    b = A(2)
    assert(b.x == 1)
    assert(a is b)
    a.x = 2
    assert(b.x == 2)



# Generated at 2022-06-13 16:51:33.763774
# Unit test for constructor of class Singleton
def test_Singleton():
    class C(object):
        __metaclass__ = Singleton

    class D(object):
        __metaclass__ = Singleton

    assert C() is C()
    assert D() is D()
    assert C() is not D()

# Generated at 2022-06-13 16:51:39.333495
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object):
        __metaclass__ = Singleton

        def __init__(self, x=''):
            self.x = x

    # check if instance is created and the same object is returned
    s1 = S()
    s2 = S('New')
    assert s1 is s2
    assert s1.x == ''
    assert s2.x == ''

    # check if the class is singleton
    class S1(S):
        pass

    assert S1() is S1()
    assert S1().x == ''
    assert S1().x == ''

# Generated at 2022-06-13 16:51:42.242500
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    b = A()
    c = A()

    # Assert that b and c refer to the same object
    assert(b is c)



# Generated at 2022-06-13 16:51:50.119326
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # test returns instance in __init__()
    class TestSingleton(object):
        __metaclass__ = Singleton
    class TestSingletonSubclass(TestSingleton):
        pass

    instance = TestSingleton()
    assert isinstance(instance, TestSingleton)
    assert isinstance(instance, TestSingletonSubclass)
    instance_subclass = TestSingletonSubclass()
    assert instance_subclass is instance

    # test returns instance from __call__()
    class TestSingleton2(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.foo = 'bar'
            self.baz = 'qux'
    class TestSingleton2Subclass(TestSingleton2):
        pass

    instance = TestSingleton2()

# Generated at 2022-06-13 16:51:56.000517
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 1

    instance1 = A()
    instance2 = A()
    assert(id(instance1) == id(instance2))
    assert(instance1.x == 1)
    assert(instance2.x == 1)
    assert(instance1 is instance2)

# Generated at 2022-06-13 16:52:09.392245
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert(a == b)

    class B(object):
        __metaclass__ = Singleton

    b = B()
    assert(a != b)

# Generated at 2022-06-13 16:52:12.813598
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    assert TestClass.__instance is None

    inst1 = TestClass()
    assert TestClass.__instance is inst1

    inst2 = TestClass()
    assert inst2 is inst1


# Generated at 2022-06-13 16:52:20.916412
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import sys
    import types

    module_name = '__ansible_builtin__'
    module_filename = None
    module_paths = ['']

    module_info = types.ModuleType(module_name)

    module_name = module_info.__name__
    module_filename = module_info.__file__
    module_paths = [module_info.__path__]

    # Declare test environment for module_loader
    test_module_name = '__test_module_loader__'
    test_module_name_module_info = types.ModuleType(test_module_name)
    sys.modules[test_module_name] = test_module_name_module_info

    # Declare test environment for NAMESPACE

# Generated at 2022-06-13 16:52:23.386868
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 1

    a = Test()
    b = Test()

    assert a is b
    assert a.value == 1
    a.value = 2
    assert b.value == 2



# Generated at 2022-06-13 16:52:28.638552
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    foo = Foo(1)
    foo2 = Foo(1)
    assert foo == foo2 and foo is foo2

# Generated at 2022-06-13 16:52:33.519879
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self, a, b):
            self.a = a
            self.b = b

    s1 = TestSingleton(1,2)
    assert s1.a == 1
    assert s1.b == 2

    s2 = TestSingleton(3,4)
    assert s1 is s2
    assert s2.a == 1
    assert s2.b == 2

    try:
        s3 = TestSingleton(5,6)
        assert False
    except Exception:
        pass

# Generated at 2022-06-13 16:52:40.434979
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.__lastName = None

        def setName(self, name):
            self.__lastName = name

        def getName(self):
            return self.__lastName

    a = TestClass()
    a.setName('alice')
    b = TestClass()
    print(b.getName())
    b.setName('bob')
    c = TestClass()
    print(c.getName())
    return

if __name__ == '__main__':
    test_Singleton___call__()
    print('Done')

# Generated at 2022-06-13 16:52:42.269368
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    t = Test()
    assert id(t) == id(Test())

# Generated at 2022-06-13 16:52:46.345691
# Unit test for constructor of class Singleton
def test_Singleton():
    class Sample(object):
        __metaclass__ = Singleton
        def __init__(self,n):
            super(Sample, self).__init__()
            self.n = n

    a = Sample(1)
    b = Sample(2)

    assert a.n == 1
    assert b.n == 1
    assert id(a) == id(b)

# Generated at 2022-06-13 16:52:50.688508
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Testing metaclass ability to manage same class's instances and not mix them
    class MySingleton(object):
        __metaclass__ = Singleton

    class NotMySingleton(object):
        __metaclass__ = Singleton

    m1 = MySingleton()
    m2 = MySingleton()
    n1 = NotMySingleton()
    n2 = NotMySingleton()
    assert m1 is m2
    assert m1 is not n1
    assert m1 is not n2

# Generated at 2022-06-13 16:53:15.382868
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonInit(object):
        def __init__(self, *args, **kwargs):
            self.called = False

    class TestSingleton(SingletonInit):
        __metaclass__ = Singleton

        def __init__(self, *args, **kwargs):
            if not self.called:
                SingletonInit.__init__(self, *args, **kwargs)
                self.called = True

        def get_id(self):
            return id(self)

    obj_1 = TestSingleton()
    obj_2 = TestSingleton()

    assert obj_1 is obj_2
    assert id(obj_1) == id(obj_2)

    assert obj_1.called is True
    assert obj_2.called is True

    assert obj_1.get_id() == obj_2

# Generated at 2022-06-13 16:53:19.961436
# Unit test for constructor of class Singleton
def test_Singleton():
    # Create a class whose metaclass is Singleton
    class MyClass(metaclass=Singleton):
        def foo(self):
            return 'bar'
    # Simply test if creating an instance of MyClass
    # has the same id.
    assert id(MyClass()) == id(MyClass())



# Generated at 2022-06-13 16:53:24.926986
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self._num = 0

        def inc(self):
            self._num += 1

        def dec(self):
            self._num -= 1

        def get(self):
            return self._num

    t1 = Test()
    t1.inc()
    assert t1.get() == 1
    t2 = Test()
    t2.dec()
    assert t2.get() == 0
    assert t1.get() == t2.get()

# Generated at 2022-06-13 16:53:27.714946
# Unit test for constructor of class Singleton
def test_Singleton():
    class ASingleton(object):
        __metaclass__ = Singleton

    a = ASingleton()
    # The second instantiated object shall be the same as a
    b = ASingleton()
    assert(a == b)


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:53:31.157525
# Unit test for constructor of class Singleton
def test_Singleton():
    class class_singleton(metaclass=Singleton):
        pass

    class_singleton_1 = class_singleton()
    class_singleton_2 = class_singleton()

    # 2 different instances of class_singleton must be the same one
    assert(class_singleton_1 is class_singleton_2)

# Generated at 2022-06-13 16:53:36.136062
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import pytest

    class A(object):
        __metaclass__ = Singleton

    class B(object):
        __metaclass__ = Singleton

    assert A() == A()
    assert id(A()) == id(A())
    assert B() == B()
    assert id(B()) == id(B())
    assert A() != B()
    assert id(A()) != id(B())
    with pytest.raises(TypeError):
        A("a", "b")
    with pytest.raises(TypeError):
        B("c", "d")

# Generated at 2022-06-13 16:53:38.656857
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class singleton_test(object):
        __metaclass__ = Singleton

    singleton_test_instance_01 = singleton_test()
    singleton_test_instance_02 = singleton_test()

    assert singleton_test_instance_01 == singleton_test_instance_02
    assert singleton_test_instance_01 is singleton_test_instance_02

# Generated at 2022-06-13 16:53:41.175709
# Unit test for constructor of class Singleton
def test_Singleton():
    class _Foo(object):
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

    foo1 = _Foo(1)
    foo2 = _Foo(2)
    assert foo1.x == 1
    assert foo2.x == 1
    assert foo1 is foo2

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:53:42.353116
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    ts1 = TestSingleton()
    ts2 = TestSingleton()

    assert ts1 is ts2

# Generated at 2022-06-13 16:53:45.907251
# Unit test for constructor of class Singleton
def test_Singleton():
    class singletonTest(metaclass=Singleton):
        def __init__(self):
            self.test = "test"

    test1 = singletonTest()
    test2 = singletonTest()

    assert test1 == test2
    assert test1.test == test2.test

# Generated at 2022-06-13 16:54:25.698699
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    class B(object):
        __metaclass__ = Singleton

    a1 = A()
    print(A())
    b = B()
    print(B())
    print(a1)


# Generated at 2022-06-13 16:54:30.152670
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class ConcreteClass(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            return self.value == other.value

    instance1 = ConcreteClass(1)
    instance2 = ConcreteClass(1)

    assert instance1 == instance2


# Generated at 2022-06-13 16:54:32.408538
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

    assert Foo() is Foo()
    assert Foo() is not Foo()

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:54:35.398577
# Unit test for constructor of class Singleton
def test_Singleton():
    from ansible.plugins.loader import connection_loader

    conn = connection_loader.get('local')
    assert isinstance(conn, connection_loader.get('local'))
    assert isinstance(conn, connection_loader.get('local'))
    assert isinstance(conn, connection_loader.get('local'))

# Generated at 2022-06-13 16:54:38.080085
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self):
            pass

        def __str__(self):
            return "A"

    a1 = A()
    a2 = A()
    assert(a1 == a2)
    assert(a1 is a2)



# Generated at 2022-06-13 16:54:47.103774
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 0

        # Declare static method in class so we can test
        # that this is still a class instance of Singleton
        @staticmethod
        def static_method():
            print('Static method.')

        def is_singleton(self):
            return type(self) == Singleton

    class MyClass2(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 0

    obj = MyClass()
    print('obj', type(obj), obj.__class__, dir(obj))
    assert obj.is_singleton()

    obj2 = MyClass2()

# Generated at 2022-06-13 16:54:51.769632
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    instance1 = Foo()
    instance2 = Foo()
    assert instance1 == instance2

# Generated at 2022-06-13 16:54:55.468455
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    t1 = Test(1)
    t2 = Test(2)
    t3 = Test(3)

    assert t1.value == t2.value == t3.value == 1

# Generated at 2022-06-13 16:55:03.774189
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.test.unit import TestCase
    from ansible.test.utils import mock
    from ansible.utils.singleton import Singleton

    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, var=None):
            self.var = var

    class TestClass2(object):
        __metaclass__ = Singleton
        def __init__(self, var=None):
            self.var = var

    class TestCase1(TestCase):
        def setUp(self):
            self.cls_1 = TestClass()
            self.cls_2 = TestClass()

        def tearDown(self):
            self.cls_1 = None
            self.cls_2 = None


# Generated at 2022-06-13 16:55:07.443496
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    design_patterns.singleton.__instance = None
    design_patterns.singleton.__rlock = RLock()

    # Test case when __instance does not equal to none
    design_patterns.singleton.__instance = 'test'
    result = design_patterns.singleton()
    assert result == 'test'

    # Test case when __instance equals to none
    design_patterns.singleton.__instance = None
    result = design_patterns.singleton()
    assert result == design_patterns.singleton.__instance

# Generated at 2022-06-13 16:56:26.044309
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    a = SingletonTest(1)
    b = SingletonTest(2)
    assert(a is b)

# Generated at 2022-06-13 16:56:28.959695
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a

    x = A(1)
    y = A(2)
    import pdb; pdb.set_trace()
    assert x is y
    assert x.a == 2

# Generated at 2022-06-13 16:56:35.163335
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    print('A() is A(): %s' % (A() is A()))  # should be True
    # It also works when we have arguments.
    class B(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    print('B(5) is B(7): %s' % (B(5) is B(7)))  # should be True

# test_Singleton__call__()
