

# Generated at 2022-06-13 16:46:47.008796
# Unit test for constructor of class Singleton
def test_Singleton():
    import contextlib
    from threading import RLock
    from nose.tools import assert_raises, assert_true

    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.__init_obj = None
            self.__rlock = RLock()

        def init_obj(self, obj):
            with self.__rlock:
                if self.__init_obj:
                    raise RuntimeError("Cannot reinitialize!")
                self.__init_obj = obj

        def get_obj(self):
            return self.__init_obj

    # Test that an instance of the class can be created safely
    st1 = SingletonTest()
    assert_true(st1 is SingletonTest())
    assert_true(st1 is st1)
    assert_

# Generated at 2022-06-13 16:46:52.112097
# Unit test for constructor of class Singleton
def test_Singleton():
    class Testme(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x

    t1 = Testme(1)
    t2 = Testme(2)
    assert t2.x == t1.x

# Generated at 2022-06-13 16:47:00.270115
# Unit test for constructor of class Singleton
def test_Singleton():
    # Create the singleton class
    class SingletonA(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'Singleton A'

    # Instance of the class
    singleton_a = SingletonA()
    assert singleton_a.name == 'Singleton A'

    # Trying to instantiate another instance of the class - doesn't work
    singleton_a2 = SingletonA()
    assert singleton_a2.name == 'Singleton A'

    # SingletonA2 can't be instantiated again
    class SingletonA2(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'Singleton A2'


# Generated at 2022-06-13 16:47:07.740342
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Klass(object):
        __metaclass__ = Singleton

    # Test multiple instantiations of the class
    x = Klass()
    y = Klass()
    assert x is y

    # Test inheritance of the class
    class OtherClass(Klass):
        pass

    # Test that the subclass is not a Singleton (can be instantiated multiple times)
    z = OtherClass()
    m = OtherClass()
    assert z is not m

    # Test that the subclass inherits from the superclass
    class OtherClass(Klass):
        pass

    # Test that superclass is a Singleton
    a = Klass()
    b = Klass()
    assert a is b

# Generated at 2022-06-13 16:47:11.316375
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        """Test class for Singleton class"""

    instance1 = TestClass()
    instance2 = TestClass()

    assert instance1 is instance2


# Generated at 2022-06-13 16:47:15.990531
# Unit test for constructor of class Singleton
def test_Singleton():
    """
    Unit test for class Singleton
    """
    class A(object):
        __metaclass__ = Singleton
        pass
    class B(object): pass

    a = A()
    b = B()
    assert a is A()
    assert a == A()
    assert b is b
    assert a != b

# Generated at 2022-06-13 16:47:19.848897
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(metaclass=Singleton):
        def __init__(self, x):
            self.x = x

    mc1 = MyClass(42)
    mc2 = MyClass(99)

    assert mc1.x == mc2.x

# Generated at 2022-06-13 16:47:25.266144
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

    s1 = SingletonTest("test_name")
    s2 = SingletonTest("another_test_name")
    assert s1 is s2



# Generated at 2022-06-13 16:47:28.541160
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    test1 = TestSingleton()
    test2 = TestSingleton()
    assert test1 == test2


# Generated at 2022-06-13 16:47:32.635379
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(Singleton):
        def __init__(self, a):
            self.a = a

    foo1 = Foo(1)
    foo2 = Foo(2)
    assert foo1.a == 1
    assert foo2.a == 1
    assert foo1 is foo2

# Generated at 2022-06-13 16:47:45.997514
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import io
    import sys
    import types
    import unittest

    # Define a class to be subclassed, where instances are tested for equality
    class Foo(object):
        def __init__(self, value):
            self.value = value

        def __eq__(self, other):
            if isinstance(other, self.__class__):
                return self.__dict__ == other.__dict__
            return False

        def __ne__(self, other):
            return not self.__eq__(other)

    # Define a class to be subclassed, where equal instances are tested for
    # identity (same instance)
    class Bar(object):
        def __init__(self, value):
            self.value = value

    # Define a class which can't be subclassed

# Generated at 2022-06-13 16:47:51.864278
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

    class Bar(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    bar1 = Bar()
    bar2 = Bar()

    assert foo2 is foo1
    assert bar2 is bar1
    assert bar1 is not foo1
    assert bar2 is not foo2

# Generated at 2022-06-13 16:47:57.248862
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert(id(a) == id(b))
    return True

if __name__ == "__main__":
    assert(test_Singleton())
    print("Success.")

# Generated at 2022-06-13 16:48:01.999774
# Unit test for constructor of class Singleton
def test_Singleton():
    """Test Constructor Singleton"""
    class Foo(object):
        """Empty Class"""
        __metaclass__ = Singleton

    class Bar(Foo):
        """Empty Class"""

    assert Foo() is Foo()
    assert Bar() is Bar()
    assert Foo() is not Bar()

    class Baz(object):
        """Empty Class"""
        __metaclass__ = Singleton
        __instance = None

    assert Baz() is Baz()
    assert Baz() is Baz()

# Generated at 2022-06-13 16:48:04.877750
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    assert Test() is Test()

# Generated at 2022-06-13 16:48:09.482335
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonClass(object):
        __metaclass__ = Singleton
        def __init__(self, value=0):
            self.value = value

    instance1 = SingletonClass(1)
    instance2 = SingletonClass(2)
    assert(instance1.value == 1)
    assert(instance2.value == 1)

# Generated at 2022-06-13 16:48:12.315955
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    S1 = Test()
    S2 = Test()

    assert S1 is S2
    assert S1.__class__ is S2.__class__



# Generated at 2022-06-13 16:48:15.342687
# Unit test for constructor of class Singleton
def test_Singleton():
    class Klass(object):
        __metaclass__ = Singleton
        def __init__(self, name):
            self.name = name

    k = Klass("test")
    assert isinstance(k, Klass)

    k = Klass("test2")
    assert isinstance(k, Klass)

    assert k.name == "test"

# Generated at 2022-06-13 16:48:20.113236
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
    class Bar(object):
        __metaclass__ = Singleton

    assert Foo() is Foo()
    assert Bar() is Bar()
    assert Foo() is not Bar()
    assert Foo()

# Generated at 2022-06-13 16:48:31.444611
# Unit test for constructor of class Singleton
def test_Singleton():
    # Create a class
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 'bar'

    # Check if it is singleton
    first = MyClass()
    second = MyClass()
    assert first == second, "Not a singleton"
    assert first.foo == second.foo, "Not a singleton"

    # Check if init is called only once
    class MyClass2(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 'bar'
            self.init_called = 0

        def call_init(self):
            self.init_called += 1

    m = MyClass2()
    m.call_init()
    m.call_init()

    assert m.init_

# Generated at 2022-06-13 16:48:38.964300
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class DummyClass(object):

        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

    a = DummyClass("a")
    b = DummyClass("b")
    c = DummyClass("c")

    assert a is b
    assert a is c

# Generated at 2022-06-13 16:48:40.770033
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(Singleton):
        def __init__(self):
            pass
    assert(A() == A())


# Generated at 2022-06-13 16:48:44.162596
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self, arg):
            self.arg = arg

    a1 = A(1)
    a2 = A(2)
    assert a1 is a2
    assert a1.arg == a2.arg

# vi: ts=4 expandtab

# Generated at 2022-06-13 16:48:47.082733
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    assert MyClass() is MyClass()



# Generated at 2022-06-13 16:48:51.387932
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        def __init__(self):
            pass
    testclass_1 = TestClass()
    testclass_2 = TestClass()
    assert testclass_1 is testclass_2


# Unit test complete
test_Singleton___call__()

# Generated at 2022-06-13 16:48:52.933858
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton



# Generated at 2022-06-13 16:48:55.863408
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            super(TestSingleton, self).__init__()

    test_obj = TestSingleton()
    assert test_obj

# Generated at 2022-06-13 16:49:00.727394
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.DUMMY = 123

    a1 = A()
    assert a1.DUMMY == 123
    a2 = A()
    assert a2.DUMMY == 123
    assert a1 is a2


# Generated at 2022-06-13 16:49:08.971440
# Unit test for constructor of class Singleton
def test_Singleton():
    assert Singleton is not None

    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.var = None

    instance1 = TestClass()
    instance1.var = 'foo'
    instance2 = TestClass()
    instance2.var = 'bar'
    assert instance1 is instance2
    assert instance1.var == instance2.var == 'bar'
    assert instance2.var == 'bar'



# Generated at 2022-06-13 16:49:11.027168
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test:
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 10

    assert Test().x == 10
    assert Test() is Test()

# Generated at 2022-06-13 16:49:17.551937
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert a1 is a2


if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:49:24.659892
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):

        __metaclass__ = Singleton

        def __init__(self):
            self.i = 0

    test_singleton1 = TestSingleton()
    test_singleton1.i = 1

    test_singleton2 = TestSingleton()
    assert(test_singleton1 is test_singleton2)
    assert(test_singleton1.i == 1)

# Generated at 2022-06-13 16:49:29.531913
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            super(MySingleton, self).__init__()
            self.foo = 'bar'

    assert MySingleton() is MySingleton()
    assert MySingleton().foo == 'bar'

# Generated at 2022-06-13 16:49:33.696447
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest:
        __metaclass__ = Singleton

        def __init__(self):
            self.__value = 0

        def set_value(self, value):
            self.__value = value

        def get_value(self):
            return self.__value

    instance1 = SingletonTest()
    instance2 = SingletonTest()

    assert id(instance1) == id(instance2)

    instance1.set_value(1)
    assert instance2.get_value() == 1

# Generated at 2022-06-13 16:49:35.758061
# Unit test for constructor of class Singleton
def test_Singleton():
	class Foo(object):
		__metaclass__ = Singleton
		
	a = Foo()
	b = Foo()
	assert a == b

# Generated at 2022-06-13 16:49:37.897529
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
    s = TestSingleton()
    s2 = TestSingleton()
    assert(s is s2)

# Generated at 2022-06-13 16:49:43.440366
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    # Create a singleton instance
    inst = TestSingleton(1, 2)
    # Create another instance - should return the first instance
    inst2 = TestSingleton(3, 4)
    assert inst is inst2
    # Ensure the constructor arguments are the first ones
    assert inst.arg1 == 1
    assert inst.arg2 == 2
    # Ensure the constructor arguments are not the second ones
    assert inst.arg1 != 3
    assert inst.arg2 != 4

# Generated at 2022-06-13 16:49:47.759386
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    import sys

    foo = Foo()
    assert foo  is Foo()
    assert foo  is Foo()
    assert sys.getrefcount(foo) == 3


# Generated at 2022-06-13 16:49:50.465127
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'a'

    a = A()
    b = A()
    assert a is b

# Generated at 2022-06-13 16:49:53.149405
# Unit test for constructor of class Singleton
def test_Singleton():
    a = Singleton('name', 'bases', 'dct')
    print(a)
    # <class '__main__.Singleton'>


# Generated at 2022-06-13 16:50:08.555128
# Unit test for constructor of class Singleton
def test_Singleton():
  # Create class Bar with metaclass Singleton
  class Bar(object):
    __metaclass__ = Singleton
    def __init__(self,x):
        print("Constructing Object, x =",x)
        self.x = x

  # Create object of class Bar
  obj1 = Bar(1)

  # The same object should be returned, and not an new one
  obj2 = Bar(2)

  # Check that it is the same object
  assert id(obj1) == id(obj2)

  # Changing the value in the first object should change the second as well
  obj1.x = 3
  assert obj2.x == 3

  # Try to create another object
  obj3 = Bar(4)

  # Check that it is the same object as the previous two

# Generated at 2022-06-13 16:50:14.339001
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self, a):
            self.a = a

    class B(metaclass=Singleton):
        def __init__(self, b):
            self.b = b

    i1 = A(1)
    assert i1.a == 1

    i2 = A(2)
    assert i2.a == 1

    i3 = B(1)
    assert i3.b == 1



# Generated at 2022-06-13 16:50:18.666799
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    # Create first instance
    test = Test()

    # Return first instance
    test2 = Test()

    assert test is test2



# Generated at 2022-06-13 16:50:23.231180
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 10

    foo = Foo()
    assert id(foo) == id(Foo())

    foo.a = 20
    assert Foo().a == 20


# Generated at 2022-06-13 16:50:28.195972
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 'test'

    a = A()
    b = A()

    assert(a == b)
    assert(a.a == 'test')
    assert(b.a == 'test')



# Generated at 2022-06-13 16:50:39.073787
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __call__(self, *args, **kw):
            print("args: " + str(args))
            print("kw:   " + str(kw))

    s1 = TestSingleton()
    s2 = TestSingleton()
    s3 = TestSingleton(1, 2, a=3, b=4)
    assert s1 is s2
    assert s2 is s3
    assert s1 is s3
    assert s1 == s2
    assert s2 == s3
    assert s1 == s3
    assert repr(s1) == repr(s2)
    assert repr(s2) == repr(s3)
    assert repr(s1) == repr(s3)


# Generated at 2022-06-13 16:50:43.484265
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Sample(metaclass=Singleton):
        def __init__(self):
            self.count = 0

        def increase_count(self):
            self.count += 1

    sample1 = Sample()
    sample2 = Sample()
    sample3 = Sample()

    assert sample1 is sample2
    assert sample1 is sample3

    sample1.increase_count()
    sample2.increase_count()
    sample3.increase_count()

    assert sample1.count == 3

# Generated at 2022-06-13 16:50:47.974170
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 0

    import threading

    t1 = A()
    t2 = A()
    t1.value = 5
    assert(t2.value == 5)

    def target(a):
        a.value += 1
        return a

    t = threading.Thread(target=target, args=(t1,))
    t.start()
    t.join()
    assert(t2.value == 6)

# Generated at 2022-06-13 16:50:51.866288
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object, metaclass=Singleton):
        def __init__(self):
            print("initializing ...")
            self.name = "foo"

    a = Foo()
    b = Foo()
    assert(a is b)
    assert(a.name == b.name)



# Generated at 2022-06-13 16:50:57.890838
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 7
    a = A()
    assert a.x == 7

    # A should be a Singleton, so this should return the same instance.
    a2 = A()
    assert a is a2

    # Changing (mutable) members of A should be preserved.
    a.x = 12
    assert a.x == 12
    assert a2.x == 12

    # Changing immutable members of A should not have any effect
    # (!= does not work for classes in Python 3)
    a.y = 7
    assert hasattr(a, "y")
    assert not hasattr(a2, "y")

    a.y = 12
    assert a.y == 12

# Generated at 2022-06-13 16:51:19.378407
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    # Should return 1 instance
    assert TestSingleton() == TestSingleton()

    class TestSingleton2(object):
        __metaclass__ = Singleton

    # Should return another instance
    assert TestSingleton() != TestSingleton2()



# Generated at 2022-06-13 16:51:21.748500
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class Foo(metaclass=Singleton):
        pass

    assert Foo() == Foo(), "Foo() should be equal to itself."



# Generated at 2022-06-13 16:51:32.385007
# Unit test for constructor of class Singleton
def test_Singleton():
    # Check if Singleton doesn't exist in module
    assert not hasattr(test_Singleton, '_Singleton')

    # Define class to test singleton
    class _Singleton(object):
        __metaclass__ = Singleton

    # Test if there is only one instance
    assert _Singleton() is _Singleton()

    # Test if constructor has been called

# Generated at 2022-06-13 16:51:37.761803
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self, val):
            self.val = val

    class MyClass2(object):
        __metaclass__ = Singleton
        def __init__(self, val):
            self.val = val

    myInstance = MyClass(5)

    assert(myInstance.val == 5)
    assert(myInstance == MyClass(12))
    assert(myInstance == MyClass(13))
    assert(myInstance != MyClass2(5))

# Generated at 2022-06-13 16:51:39.113638
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    test = Test()
    assert(test == Test())

# Generated at 2022-06-13 16:51:45.787940
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class EmptySingleton(object):
        __metaclass__ = Singleton

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, value=None):
            self.value = value

    empty_singleton = EmptySingleton()
    assert empty_singleton is EmptySingleton()

    test_singleton_1 = TestSingleton()
    assert test_singleton_1 is TestSingleton()

    test_singleton_2 = TestSingleton(value=1)
    assert test_singleton_2 is TestSingleton()



# Generated at 2022-06-13 16:51:48.227523
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    instance_one = Test()
    instance_two = Test()
    assert instance_one is instance_two


# Generated at 2022-06-13 16:51:53.241577
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a

    a1 = A('first')
    a2 = A('second')
    a3 = A(3)

    assert a1 == a2
    assert a1 == a3
    assert a2 == a3
    assert a1.a == 'first'
    assert a2.a == 'second'
    assert a3.a == 3
    assert a1 is a2
    assert a1 is a3
    assert a2 is a3


# Generated at 2022-06-13 16:51:58.076872
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
    class B(A):
        pass
    a1 = A()
    a2 = A()
    b1 = B()
    b2 = B()
    assert a1 is a2, 'Singleton class A not same'
    assert b1 is b2, 'Singleton class B not same'
    assert a1 is not b1, 'Singleton class A and B are the same'

# Generated at 2022-06-13 16:52:00.199155
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1

    a = A()
    assert a.a == 1
    a1 = A()
    assert a1 is a
    a1.a = 2
    assert a.a == 2



# Generated at 2022-06-13 16:52:37.624874
# Unit test for constructor of class Singleton
def test_Singleton():
    '''
    Simple unit test that demonstrates the use of the Singleton class
    '''
    class SingletonClass(object):
        __metaclass__ = Singleton

    instance1 = SingletonClass()
    instance2 = SingletonClass()

    assert id(instance1) == id(instance2)


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:52:41.736845
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, x, str1):
            self.x = x
            self.str1 = str1

    instance1 = TestClass(1, "1")
    instance2 = TestClass(2, "2")
    assert id(instance1) == id(instance2)


# Generated at 2022-06-13 16:52:45.448943
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.val = 1

    t1 = TestSingleton()
    t2 = TestSingleton()
    assert t1 is t2

    t1.val = 2
    assert t1.val == t2.val

# Generated at 2022-06-13 16:52:48.433550
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, v):
            self.v = v

    a1 = A(1)
    assert a1.v == 1
    a2 = A(2)
    assert a2.v == a1.v == 1

# Generated at 2022-06-13 16:52:49.882216
# Unit test for constructor of class Singleton
def test_Singleton():
    s = Singleton('Singleton', (object,), {})
    assert issubclass(s, object)

# Generated at 2022-06-13 16:52:55.556971
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from uuid import uuid4

    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.uuid = str(uuid4())
            self.name = "SingletonTest"

    s1 = SingletonTest()
    s2 = SingletonTest()
    assert s1 is s2
    assert s1.name == s2.name
    assert s1.uuid == s2.uuid



# Generated at 2022-06-13 16:53:01.681071
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, *args, **kw):
            self.args = args
            self.kw = kw

        def __str__(self):
            return '<A %s, %s>'%(self.args, self.kw)

    # creation
    a1 = A(0, 1, k=2)
    a2 = A(1, 2, k=3)
    assert a1 is a2, 'singleton failed'
    assert a1 != a2, 'singleton failed'
    a2.k = 4
    assert a1.kw == {'k': 4}, 'singleton failed'

    # other methods

# Generated at 2022-06-13 16:53:06.943729
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.initialized = True

    singleton = SingletonClass()
    assert singleton.initialized

    singleton.test = 'foo'
    singleton2 = SingletonClass()
    assert singleton2.test == 'foo'
    assert singleton2 is singleton

# vim: expandtab:tabstop=4:shiftwidth=4

# Generated at 2022-06-13 16:53:10.359684
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test = 'test'

    s1 = TestSingleton()
    s2 = TestSingleton()

    assert s1 is s2

# Generated at 2022-06-13 16:53:16.145569
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            self.arg = arg

    a1 = A(1)
    a2 = A(2)
    a3 = A(3)

    assert a1.arg == 1
    assert a2.arg == 1
    assert a3.arg == 1
    assert a1 is a2
    assert a2 is a3
    assert a3 is a1


# Generated at 2022-06-13 16:54:26.993048
# Unit test for constructor of class Singleton
def test_Singleton():
  class C(metaclass=Singleton):
      def test(self):
          """ Test function in class C. """
          pass

  assert C() is C()
  assert C()

# Test for module Singleton
from ansiblelint.rules import RulesCollection


# Generated at 2022-06-13 16:54:30.420626
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton
    instance1 = TestClass()
    instance2 = TestClass()
    assert instance1 == instance2
    instance1.foo = 'bar'
    assert instance1.foo == instance2.foo

# Generated at 2022-06-13 16:54:34.481388
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self, bar):
            self.bar = bar

    foo1 = Foo('bar1')
    assert foo1.bar == 'bar1'

    foo2 = Foo('bar2')
    assert foo2.bar == 'bar1'
    assert foo1 is foo2

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:54:37.588168
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class ImSingleton(object):
        __metaclass__ = Singleton

    class TestSingleton(object):
        __metaclass__ = Singleton
        __instance = 1

    assert Singleton.__call__(TestSingleton, None) == 1
    assert Singleton.__call__(ImSingleton, None) is not None

# Generated at 2022-06-13 16:54:39.130322
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert a1 is a2


# Generated at 2022-06-13 16:54:45.458925
# Unit test for constructor of class Singleton
def test_Singleton():

    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = 'Test'

    class B(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = 'Test'

    a = A()
    b = B()

    assert id(a) == id(A())
    assert id(b) == id(B())

    assert id(A()) != id(B())

    print('test_Singleton passed.')

# Generated at 2022-06-13 16:54:49.440748
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest
    import types

    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a

    class TestCase(unittest.TestCase):
        def test_instance(self):
            self.assertEqual(Test(1), Test(2))

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

# Generated at 2022-06-13 16:54:53.462356
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Class(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value
    c1 = Class('v1')
    c2 = Class('v2')
    assert c1 is c2


# Generated at 2022-06-13 16:54:59.457060
# Unit test for constructor of class Singleton
def test_Singleton():
    from ansible.module_utils.six import with_metaclass

    class TestSingleton(with_metaclass(Singleton)):
        def __init__(self, arg):
            self.arg = arg

    class FakeSingleton(with_metaclass(Singleton)):
        def __init__(self, arg):
            self.arg = 'asd'

    assert TestSingleton('foo') == TestSingleton('bar')
    assert TestSingleton('foo') is TestSingleton('bar')
    assert TestSingleton('foo').arg == 'bar'
    assert TestSingleton('foo').arg == 'baz'
    assert FakeSingleton('foo').arg == 'asd'

# Generated at 2022-06-13 16:55:02.733353
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object, metaclass=Singleton):
        def __init__(self, bar=None):
            self.bar = bar

    # Test constructor of class Foo for singleton
    foo = Foo('test')
    assert foo.bar == 'test'
    foo2 = Foo()
    assert foo2.bar == 'test'