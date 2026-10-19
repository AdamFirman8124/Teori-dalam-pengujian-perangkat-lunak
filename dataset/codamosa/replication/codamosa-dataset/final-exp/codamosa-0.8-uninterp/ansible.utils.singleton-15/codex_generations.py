

# Generated at 2022-06-13 16:46:46.436137
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # class to inherit from Singleton
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a

    # initializing different instances of A
    a = A(1)
    b = A(2)
    c = A(3)

    print(a.a)
    print(b.a)
    print(c.a)

    # checking that all instances are the same, which is not expected
    # for the Singleton metaclass to work properly
    print(a is b) # True
    print(b is c) # True
    print(c is a) # True


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:46:53.437479
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import traceback
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1

    class MyClass2(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 2

    a = MyClass()
    b = MyClass()
    assert a is b, 'Singleton failed to return same instance'

    c = MyClass2()
    d = MyClass2()
    assert c is d, 'Singleton failed to return same instance'

    # Sanity check to make sure we're not creating instances of MyClass2
    # accidently in our Singleton implementation above.
    e = MyClass()
    assert a is e, 'Singleton failed to return same instance'

# Generated at 2022-06-13 16:47:00.495379
# Unit test for constructor of class Singleton
def test_Singleton():
    lock = RLock()
    s = Singleton('s',(),{})
    s.__instance = "test instance"
    s.__rlock = lock

    assert s.__instance == "test instance"
    assert s.__rlock == lock

    # Purposely call __call__ from outside of the class, call __call__ within
    # the class with different values, and assert the values change
    with lock:
        s.__instance = "__call__ inside value"
        s.__rlock = RLock()

    assert s.__instance == "__call__ inside value"
    assert s.__rlock is not lock

    s2 = s()
    assert s2 == s.__instance

# Generated at 2022-06-13 16:47:04.202866
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.bar = 5

    foo1 = Foo()
    foo2 = Foo()

    assert foo1 is foo2
    assert foo1.bar == foo2.bar

test_Singleton()

# Generated at 2022-06-13 16:47:07.188846
# Unit test for constructor of class Singleton
def test_Singleton():
    class test_class(object):
        __metaclass__ = Singleton
        pass

    assert id(test_class()) == id(test_class())

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:47:12.170746
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    # Create the instance
    first_instance = Foo()
    assert first_instance is not None

    # If another instance is created, it should return the original one
    second_instance = Foo()
    assert second_instance is not None
    assert first_instance is second_instance



# Generated at 2022-06-13 16:47:19.177529
# Unit test for constructor of class Singleton
def test_Singleton():
    import copy
    cls1 = Singleton('S', (), {})
    cls2 = Singleton('S', (), {})
    if cls1 is not cls2:
        raise TypeError("Two class initialized with same name")

    obj1 = cls1(1)
    obj2 = cls2(2)
    if obj1 is not obj2:
        raise TypeError("Two object of same class have been created")

    cls3 = copy.deepcopy(cls1)
    if cls3 is not cls1:
        raise TypeError("Deepcopy of class is not original class")


# Generated at 2022-06-13 16:47:23.248477
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    a = TestClass()
    b = TestClass()
    assert(a == b)

# Generated at 2022-06-13 16:47:30.977552
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test = 1

    class SingletonBase(object):
        __metaclass__ = Singleton

    class A(SingletonBase):
        def __init__(self):
            self.test = 1

    class B(SingletonBase):
        def __init__(self):
            self.test = 2
    a = A()
    a1 = A()
    assert a is a1
    assert a.test == 1
    b = B()
    b1 = B()
    assert b is b1
    assert a is not b
    assert b.test == 2

# Generated at 2022-06-13 16:47:33.107897
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()

    assert a1 is a2

# Generated at 2022-06-13 16:47:37.996236
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert a is b, 'instance of Singleton is not unique'

# Generated at 2022-06-13 16:47:45.243888
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from .mock import Mock, call

    class MockSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.init_called = Mock()
            self.init_called()

    singleton = MockSingleton()
    assert singleton.init_called.call_count == 1
    singleton2 = MockSingleton()
    assert singleton2 == singleton
    assert singleton.init_called.call_count == 1
    assert singleton2.init_called.call_count == 1

# Generated at 2022-06-13 16:47:48.089326
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert A() is A()
    assert A() is not None



# Generated at 2022-06-13 16:47:52.628067
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton
        def __init__(self):
            print("SingletonTest init")

    t1 = SingletonTest()
    t2 = SingletonTest()
    print("t1 == t2:", t1 == t2, "\n")



# Generated at 2022-06-13 16:47:56.946544
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton1(object):
        __metaclass__ = Singleton

    inst1 = TestSingleton1()
    inst2 = TestSingleton1()

    assert id(inst1) == id(inst2)


# Generated at 2022-06-13 16:47:58.702788
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert A() is A()

# Generated at 2022-06-13 16:48:01.537525
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Single(object):
        __metaclass__ = Singleton
        def __init__(self, v):
            self.v = v

    single1 = Single(100)
    single2 = Single(200)
    assert single1.v == single2.v == 100

# Generated at 2022-06-13 16:48:03.507120
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    instance1 = TestClass()
    instance2 = TestClass()

    assert(instance1 == instance2)


# Generated at 2022-06-13 16:48:05.146995
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2


# Generated at 2022-06-13 16:48:07.511322
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    a = TestClass()
    b = TestClass()
    assert a == b



# Generated at 2022-06-13 16:48:10.426388
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    a = TestSingleton()
    b = TestSingleton()
    assert a is b

if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:48:16.023447
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from .compat.types import set

    class TestSingleton(object):
        __metaclass__ = Singleton

    # check __call__ returns the same instance
    a = TestSingleton()
    b = TestSingleton()
    assert(a is b)

    # check object is member of singleton class
    assert(TestSingleton in a.__class__.__mro__)
    assert(TestSingleton in b.__class__.__mro__)

    # check object is not member of any other classes
    assert(set(a.__class__.__mro__) == set(b.__class__.__mro__))

# Generated at 2022-06-13 16:48:25.068423
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self, n):
            self.name = n

    a1 = A('A')
    a2 = A('A')

    assert a1 == a2
    assert a1 is a2
    assert type(a1) == type(a2)    # A class() == A class()
    assert type(a1) is type(a2)    # A class() is A class()
    assert isinstance(a1, A)       # a1 is instance of A
    assert isinstance(a2, A)       # a2 is instance of A



# Generated at 2022-06-13 16:48:32.015902
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, idx):
            self.idx = idx

    s1 = SingletonTest(1)
    assert s1.idx == 1
    assert id(s1) == id(SingletonTest(1))

    s2 = SingletonTest(2)
    assert s2.idx == 1
    assert id(s2) == id(SingletonTest(1))


# Generated at 2022-06-13 16:48:39.810464
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Call the class which uses Singleton metaclass
    instance1 = ClsWithSingletonMetaclass()
    # Call the class again
    instance2 = ClsWithSingletonMetaclass()
    assert instance1 == instance2

# Method __call__ of Singleton class is called when an instance of a
# class with Singleton metaclass is created.
# The method checks if there is an existing instance, if not it creates one
# and returns it.
# Thus, the method is only called once for a given class, and always return the same instance

# Generated at 2022-06-13 16:48:42.056728
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object, metaclass=Singleton):
        pass

    x = MyClass()
    y = MyClass()
    assert(x == y)



# Generated at 2022-06-13 16:48:47.868883
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object, metaclass=Singleton):
        def __init__(self):
            self.var = "test"

    class Test2(object):
        def __init__(self):
            self.var = "test2"

    t1 = Test()
    t2 = Test()

    assert t1 is t2
    assert t2.var == "test"

    t3 = Test2()
    t4 = Test2()

    assert t3 is not t4
    assert t3.var == "test2"
    assert t4.var == "test2"

# Generated at 2022-06-13 16:48:52.743175
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self, x=None):
            self.x = x

    f1 = Foo()
    f2 = Foo(1)
    f3 = Foo(2)

    assert f1 is f3
    assert f1.x is None
    assert f3.x is 1

# Generated at 2022-06-13 16:48:58.609030
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self, data):
            self.data = data

    # Verify that multiple calls to MyClass() return
    # the same instance
    instance1 = MyClass(1)
    instance2 = MyClass(2)
    assert instance1 == instance2
    # Access instance1 and instance2 fields to make sure
    # previously stored data is accessible
    assert instance1.data == 1
    assert instance2.data == 1

"""
test_Singleton___call__()
"""

# Generated at 2022-06-13 16:49:03.100817
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class HelloWorld(object):
        __metaclass__ = Singleton
        def __init__(self,name="haha"):
            self.name = name

    a = HelloWorld()
    b = HelloWorld()

# Generated at 2022-06-13 16:49:06.044112
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    a = TestSingleton()
    b = TestSingleton()
    assert id(a) == id(b)

# Generated at 2022-06-13 16:49:09.874235
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Single(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 'Single'

    class Multi(object):
        def __init__(self):
            self.value = 'Multi'

    assert(Single() is Single())
    assert(Multi() is not Multi())


# Generated at 2022-06-13 16:49:11.587561
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert id(A()) == id(A())



# Generated at 2022-06-13 16:49:13.682309
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(metaclass=Singleton):
        pass

    a = Test()
    b = Test()
    assert a is b

# Generated at 2022-06-13 16:49:18.635369
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.module_utils.six import with_metaclass

    class A(with_metaclass(Singleton, object)):
        def __init__(self):
            self.a = 10

    a1 = A()
    a2 = A()
    assert a1 == a2
    assert a1.a == a2.a
    assert id(a1) == id(a2)



# Generated at 2022-06-13 16:49:25.244966
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Test for a singleton class
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            self.arg = arg

        def show(self):
            print(self.arg)

    # Test for two instances
    a = MySingleton('a')
    b = MySingleton('b')
    a.show()
    b.show()


# Generated at 2022-06-13 16:49:30.410243
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.module_utils.six import with_metaclass

    class SingletonTest(with_metaclass(Singleton, object)):
        pass

    a = SingletonTest()
    b = SingletonTest()

    try:
        assert b is a
        assert True
    except AssertionError:
        assert False


# Generated at 2022-06-13 16:49:33.175874
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton

    foo = MySingleton()

    assert foo is MySingleton()



# Generated at 2022-06-13 16:49:38.848378
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    '''
    Unit test for method __call__ of class Singleton.
    '''
    class TestSingleton(metaclass=Singleton):
        pass

    assert TestSingleton() == TestSingleton()
    assert len(TestSingleton.__mro__) == 2
    assert len(TestSingleton.__dict__) == 3
    # Verify that we can't extend the class
    try:
        class TestChildSingleton(TestSingleton):
            pass
    except TypeError:
        pass
    else:
        assert False

# Generated at 2022-06-13 16:49:44.553587
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class SomeClass(object):
        __metaclass__ = Singleton

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    class AnotherClass(object):
        __metaclass__ = Singleton

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    a = SomeClass(1, 2)
    b = SomeClass(3, 4)

    c = AnotherClass(1, 2)
    d = AnotherClass(3, 4)

    assert a is b
    assert c is d
    assert a is not c


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:49:49.509274
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, x=None):
            self.x = x

    a1 = A()
    a2 = A()
    assert a1 == a2


# Generated at 2022-06-13 16:49:55.942937
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Unit test for method __call__ of class Singleton."""
    class S1(object):
        __metaclass__ = Singleton

        def __init__(self, a=None, b=None):
            self.a = a if a is not None else 0
            self.b = b if b is not None else 0

    class S2(object):
        __metaclass__ = Singleton

    assert S1() is not None
    assert S2() is not None
    assert S1(1, 2) is not None
    assert S1(1, 2) is S1()


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:50:02.639379
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()

    class Bar(object):
        __metaclass__ = Singleton

    bar1 = Bar()

    assert foo1 is not None
    assert bar1 is not None

    foo2 = Foo()
    bar2 = Bar()

    assert foo2 is not None
    assert bar2 is not None

    assert foo1 is foo2
    assert bar1 is bar2


# Generated at 2022-06-13 16:50:06.133114
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.foo=True

    foo = Foo()
    assert foo.foo == True
    bar = Foo()
    assert foo.foo == True
    assert foo == bar
    assert id(foo) == id(bar)



# Generated at 2022-06-13 16:50:12.115278
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    x = TestSingleton()
    y = TestSingleton()
    assert id(x) == id(y)
    assert type(x) is TestSingleton, type(y) is TestSingleton

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:50:13.931288
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    a = Foo()
    b = Foo()
    assert a is b

# Generated at 2022-06-13 16:50:18.958745
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class s:
        __metaclass__ = Singleton
    import types
    assert type(s()) == types.InstanceType
    assert type(s()) == types.InstanceType
    assert s() == s()


# Generated at 2022-06-13 16:50:21.211889
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert A() is A()



# Generated at 2022-06-13 16:50:30.013277
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

    instance1 = Foo(1, 2, 3)
    instance2 = Foo(4, 5, 6)
    assert instance1 is not None
    assert instance2 is not None
    assert instance1 is instance2
    assert instance2.a == 1
    assert instance2.b == 2
    assert instance2.c == 3


if __name__ == '__main__':
    import nose
    nose.config.add_config_file('unittest.cfg')
    nose.runmodule()

# Generated at 2022-06-13 16:50:36.069665
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 0

    f1 = Foo()
    f1.x = 1

    f2 = Foo()
    assert f1 is f2
    assert f2.x == 1

    #f2.x = 2
    #assert f1.x == 1
    #assert f2.x == 2



# Generated at 2022-06-13 16:50:44.719572
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # - Create a singleton class
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.counter = 1

        def increment(self):
            self.counter += 1

    # - Call method __call__
    obj1 = TestSingleton()
    obj2 = TestSingleton()
    assert obj1 is obj2

    # - Call method increment
    obj1.increment()
    assert obj1.counter == 2
    assert obj2.counter == 2

    # - Call method __call__ again
    obj3 = TestSingleton()
    assert obj1 is obj3
    assert obj2 is obj3
    assert obj1 is obj2

    # - Call method increment again
    obj1.increment()
    assert obj1.counter == 3

# Generated at 2022-06-13 16:50:47.968411
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    assert TestSingleton(1) == TestSingleton(1)

# Generated at 2022-06-13 16:50:53.497197
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from unittest import TestCase
    class Class(object):
        __metaclass__ = Singleton
    class_instance1 = Class()  # create a Singleton object
    class_instance2 = Class()  # reference to the same object
    class_instance3 = Class()

    TestCase().assertEqual(class_instance1, class_instance2)
    TestCase().assertEqual(class_instance2, class_instance3)

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:50:55.565295
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        pass
    a1, a2 = A(), A()
    assert(a1 == a2)
    assert(id(a1) == id(a2))



# Generated at 2022-06-13 16:50:58.999817
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 100

    a = A()
    b = A()

    assert id(a) == id(b)
    assert a.value == b.value
    # It should be possible to
    # call the method __call__
    # of the class Singleton
    assert A.__call__() is a


if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:51:02.767154
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    # Define a class that is subclass of Singleton
    class SingletonTest(metaclass=Singleton):
        pass

    # Instantiate the class
    obj1 = SingletonTest()

    # Check if the object returned is the same as the one instantiated
    assert obj1 is SingletonTest()
    assert obj1 == SingletonTest()

# Generated at 2022-06-13 16:51:10.794959
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self, test_arg=None):
            self.test_arg = test_arg

    t1 = TestSingleton()
    t2 = TestSingleton()
    t3 = TestSingleton('test_arg')

    assert t1 is t2
    assert t2 is t3
    assert t3 is t1
    assert t3.test_arg == 'test_arg'



# Generated at 2022-06-13 16:51:18.205961
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.data = 0
    obj1 = TestSingleton()
    obj1.data += 1
    assert obj1.data == 1
    obj2 = TestSingleton()
    obj2.data += 1
    assert obj2.data == 2
    assert obj1 == obj2
    return True


# Generated at 2022-06-13 16:51:23.822150
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.instance = None

        def __call__(self, *args, **kw):
            if self.instance is not None:
                return self.instance

            with self.__rlock:
                if self.instance is None:
                    self.instance = super(Singleton, self).__call__(*args, **kw)

            return self.__instance

    ts1 = TestSingleton()
    ts2 = TestSingleton()
    assert ts1 is ts2



# Generated at 2022-06-13 16:51:30.390994
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class foo(object):
        __metaclass__ = Singleton
        def __init__(self, name):
            self.name = name

    # the first instance
    first = foo('instance1')
    assert first.name == 'instance1'

    # the second instance, same reference as first
    second = foo('instance2')
    assert second.name == 'instance1'



# Generated at 2022-06-13 16:51:40.306632
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class Other:
        pass

    class A(Other):
        __metaclass__ = Singleton
        def __init__(self, x, y):
            self.x = x
            self.y = y

    a1 = A(1, 2)
    a2 = A(3, 4)
    a3 = A(1, 2)

    assert a1 is a2
    assert a1 is a3

    assert a1.x == 1 and a1.y == 2
    assert a2.x == 1 and a2.y == 2
    assert a3.x == 1 and a3.y == 2

    assert a1.__class__ is A
    assert A.__instance is a2

    b = A(5, 6)
    assert b is a1

# Generated at 2022-06-13 16:51:48.858205
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansibullbot.utils.extractors.ansible import AnsibleExtractor
    from ansibullbot.utils.extractors.github import GitHubExtractor
    from ansibullbot.utils.extractors.redhat import RedHatExtractor
    from ansibullbot.utils.extractors.releases import ReleasesExtractor
    from ansibullbot.utils.extractors.upstream import UpstreamExtractor

    class AnsibleExtractorSingleton(AnsibleExtractor, metaclass=Singleton):
        pass

    class GitHubIssueExtractorSingleton(GitHubExtractor, metaclass=Singleton):
        pass

    class RedHatIssueExtractorSingleton(RedHatExtractor, metaclass=Singleton):
        pass


# Generated at 2022-06-13 16:51:51.393457
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a

    a1 = A(1)
    a2 = A(2)
    assert(a1 is a2)


# Generated at 2022-06-13 16:51:54.788148
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    assert Foo.__instance is None
    i1 = Foo()
    i2 = Foo()
    assert i1 is i2
    assert i1 is Foo.__instance
    assert i2 is Foo.__instance



# Generated at 2022-06-13 16:51:56.827963
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert a == b


# Generated at 2022-06-13 16:51:58.592978
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    assert TestClass() is TestClass()



# Generated at 2022-06-13 16:52:06.902189
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    class B(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.id = id(self)

    pass_count = 0
    fail_count = 0

    a1 = A()
    a2 = A()

    if a1 == a2 and id(a1) == id(a2):
        pass_count += 1
    else:
        fail_count += 1

    b1 = B()
    b2 = B()

    if b1 == b2 and b1.id == b2.id:
        pass_count += 1
    else:
        fail_count += 1

    if pass_count == 2:
        print("%s test OK!" % __name__)
    else:
        print

# Generated at 2022-06-13 16:52:09.317225
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    assert a is A()



# Generated at 2022-06-13 16:52:16.654209
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        """
        dummy class to test Singleton metaclass
        """
        __metaclass__ = Singleton
        def __init__(self, name):
            self.name = name

    # Test
    ts1 = TestSingleton("ts1")
    assert(ts1.name == "ts1")
    ts2 = TestSingleton("ts2")
    assert(ts2.name == "ts1") # even if "ts2" is set, it does not take effect.
    assert(ts1.name == "ts1") # the name of ts1 does not change.

# Generated at 2022-06-13 16:52:20.465038
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a
    x = Test(3)
    y = Test(5)
    assert x.a == 3
    assert y.a == 3
    assert x is y
    x.a = 4
    assert x.a == 4
    assert y.a == 4



# Generated at 2022-06-13 16:52:25.350239
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, val):
            self.val = val

    # test first instance
    a1 = A(1)
    assert a1.val == 1

    # test existing singleton instance
    a2 = A(2)
    assert a2.val == 1
    assert a1 is a2

# Generated at 2022-06-13 16:52:29.568751
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Example(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 'value'

    example = Example()
    assert example.value == 'value'



# Generated at 2022-06-13 16:52:36.006928
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    # Instantiate 3 instances of class TestClass
    instance_1 = TestClass()
    instance_2 = TestClass()
    instance_3 = TestClass()

    # Verify that all 3 instances are the same
    assert instance_1 is instance_2
    assert instance_2 is instance_3

# Generated at 2022-06-13 16:52:40.085640
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        pass

    a = A()
    a1 = A()
    assert a is a1

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:52:47.134772
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    class TestSingleton1(object):
        __metaclass__ = Singleton

    def TestSingleton2(object):
        __metaclass__ = Singleton

    class TestSingleton3(object):
        __metaclass__ = Singleton

    assert TestSingleton() is TestSingleton()
    assert TestSingleton1() is TestSingleton1()
    assert TestSingleton2() is TestSingleton2()
    assert TestSingleton3() is TestSingleton3()
    assert TestSingleton() is not TestSingleton1()
    assert TestSingleton2() is not TestSingleton3()

test_Singleton___call__()

# Generated at 2022-06-13 16:52:49.421282
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton


    # create A1, A2
    a1 = A()
    a2 = A()

    # a1 == a2
    assert a1 is a2



# Generated at 2022-06-13 16:52:51.122721
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    a = Singleton()
    b = Singleton()
    assert a is b


# Generated at 2022-06-13 16:52:55.627898
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self, val):
            self.val = val

    a = Foo(val=1)
    b = Foo(val=2)

    assert(a == b)
    assert(a.val == 1)
    assert(b.val == 1)
    assert(id(a) == id(b))


# Generated at 2022-06-13 16:52:57.937193
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

    a = MyClass()
    b = MyClass()
    if a is not b:
        raise AssertionError("a is not b")


# Generated at 2022-06-13 16:53:08.793047
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import sys
    sys.path.append('../')
    from lib.ansibullbot.utils.compat import PY3
    if not PY3:
        reload(sys)
        sys.setdefaultencoding('utf8')
    import unittest

    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.var = 0

    class SingletonTest(unittest.TestCase):
        def test_Singleton(self):
            a1 = A()
            a2 = A()
            a1.var = 1
            self.assertEqual(a1.var, 1)
            self.assertEqual(a2.var, 1)
            self.assertEqual(id(a1), id(a2))

# Generated at 2022-06-13 16:53:18.206998
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        """Singleton object class"""
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return str(self.name)

    assert A('test1') is A('test2')



# Generated at 2022-06-13 16:53:22.502616
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class c1(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.val = 0

        def inc(self):
            self.val += 1

    print(c1())
    print(c1())

    b = c1()
    print(b)
    b.inc()
    print(b)



# Generated at 2022-06-13 16:53:24.472529
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    instance1 = TestSingleton()
    instance2 = TestSingleton()

    assert id(instance1) == id(instance2)

# Generated at 2022-06-13 16:53:27.021760
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    i1 = Foo()
    i2 = Foo()
    assert id(i1) == id(i2)

# Generated at 2022-06-13 16:53:34.338553
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.errors import AnsibleError

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1
            self.b = 2

    assert TestSingleton() is TestSingleton()
    assert TestSingleton() is not False
    assert TestSingleton().a == 1
    assert TestSingleton().b == 2
    assert TestSingleton().b != 1
    assert TestSingleton().b != 3

    class TestSingleton2(object):
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a

    try:
        TestSingleton2()
    except AnsibleError as e:
        assert "TypeError: __init__() takes exactly 2 arguments (1 given)" in str(e)

# Generated at 2022-06-13 16:53:36.109288
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class S(object):
        __metaclass__ = Singleton
    s1 = S()
    s2 = S()
    assert s1 == s2
    assert s1 is s2



# Generated at 2022-06-13 16:53:38.452795
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Singleton_Example(object):
        """Example of a class that should be a Singleton."""

        __metaclass__ = Singleton
        # Enable Singleton implementation

    _instance1 = Singleton_Example()
    _instance2 = Singleton_Example()
    assert (_instance1 is _instance2)



# Generated at 2022-06-13 16:53:39.302931
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert A() is A()

# Generated at 2022-06-13 16:53:46.155400
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 1

    local_var_a = TestSingleton()
    local_var_a.value += 1

    local_var_b = TestSingleton()
    local_var_b.value += 1

    assert local_var_a.value == 3
    assert local_var_b.value == 3
    assert local_var_a == local_var_b
    assert id(local_var_a) == id(local_var_b)

# Generated at 2022-06-13 16:53:49.034421
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test:
        __metaclass__ = Singleton
        def __init__(self, value=0):
            self.value = value

    a = Test(1)
    b = Test(2)
    assert a == b
    assert a.value == b.value



# Generated at 2022-06-13 16:54:02.484568
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        def __init__(self):
            pass

    tc1 = TestClass()
    tc2 = TestClass()
    assert tc1 is tc2



# Generated at 2022-06-13 16:54:05.276930
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(Singleton):
        def __init__(self):
            pass

    a1 = A()
    a2 = A()
    assert(a1 is a2)



# Generated at 2022-06-13 16:54:08.054103
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    assert Test() is Test()



# Generated at 2022-06-13 16:54:10.463021
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert a1 is a2

    b1 = A()
    b2 = A()
    assert b1 is b2

    assert a1 is b1
    assert a2 is b2



# Generated at 2022-06-13 16:54:14.116680
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest:
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'SingletonTest'

    a = SingletonTest()
    b = SingletonTest()

    assert a == b
    assert a.name == b.name

# Generated at 2022-06-13 16:54:16.100353
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    assert TestSingleton() == TestSingleton()


# Generated at 2022-06-13 16:54:20.783322
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    # tests
    a1 = A()
    a2 = A()
    assert a1 is a2

    class B(object):
        __metaclass__ = Singleton
        def __new__(cls, *args, **kwargs):
            return super(B, cls).__new__(cls, *args, **kwargs)

    b1 = B()
    b2 = B()
    assert b1 is b2

# Generated at 2022-06-13 16:54:25.592260
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = "bar"
    obj1 = TestSingleton()
    obj2 = TestSingleton()
    # Test if the instance was created
    if (obj1 is None) or (obj2 is None):
        raise AssertionError()
    # Test if the instance is a Singleton
    if obj1 is not obj2:
        raise AssertionError()
    # Test if the init has been called once
    if obj1.foo != "bar":
        raise AssertionError()

# Generated at 2022-06-13 16:54:28.559944
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    print(a1, a2)
    assert a1 is a2

# Generated at 2022-06-13 16:54:32.585460
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(with_metaclass(Singleton)):
        def __init__(self, *args, **kwargs):
            self.args = args
        def __eq__(self, other):
            return self.args == other.args
    assert Foo is Foo()
    assert Foo(1) is not Foo()
    assert Foo(1) is Foo(1)
    assert Foo(1) == Foo(1)

# Generated at 2022-06-13 16:55:01.483604
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    name, bases, dct = "AClass", (), {"a": 1}

    class AClass: pass
    a1, a2 = Singleton(name, bases, dct)(), Singleton(name, bases, dct)()
    assert a1 is a2 and a1.a == 1 and a2.a == 1

    class BClass(AClass):
        a = 2
    a1, a2 = Singleton(name, bases, dct)(), Singleton(name, bases, dct)()
    assert a1 is a2 and a1.a == 2 and a2.a == 2

# Generated at 2022-06-13 16:55:07.066385
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class NewClass(metaclass=Singleton):
        def __init__(self):
            self.x = 'foo'

        def foo(self):
            return self.x

    from concurrencytest import ConcurrentTestSuite, fork_for_tests
    import unittest

    class NewClassTestCase(unittest.TestCase):
        def test_foo(self):
            instance = NewClass()
            self.assertEqual(instance.foo(), 'foo')

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(NewClassTestCase))
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(8))
    runner = unittest.TextTestRunner()
    runner.run(concurrent_suite)

# Generated at 2022-06-13 16:55:11.984338
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class First(object):
        __metaclass__ = Singleton

        def __init__(self, num):
            self.__num = num

        def get_num(self):
            return self.__num

    class Second(object):
        __metaclass__ = Singleton

        def __init__(self, num):
            self.__num = num

        def get_num(self):
            return self.__num

    a = First("Object 1")
    b = First("Object 2")
    c = Second("Object 3")
    d = Second("Object 4")

    assert a == b
    assert c == d
    assert a != c

    assert a.get_num() == "Object 1"
    assert b.get_num() == "Object 1"
    assert c.get_num() == "Object 3"

# Generated at 2022-06-13 16:55:18.130736
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 0

        def add(self):
            self.value += 1

    a1 = A()
    a2 = A()

    assert a1 == a2
    assert a1 is a2

    a1.add()
    a1.add()
    a1.add()
    assert a1.value == 3

    a2.add()
    assert a2.value == 4



# Generated at 2022-06-13 16:55:23.298917
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class AnEntity(object):
        __metaclass__ = Singleton
        def __init__(self, id_):
            self.id_ = id_
    first = AnEntity(1)
    second = AnEntity(2)
    third = AnEntity(3)
    assert first is second
    assert second is third
    assert third is first

# Generated at 2022-06-13 16:55:28.166700
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 5

        def get_a(self):
            return self.a

    # create an instance, this is the first instance of the class
    test()
    # create another instance
    test1 = test()
    # check if the two instances are the same
    assert test() is test1
    assert test().get_a() == 5


# Generated at 2022-06-13 16:55:32.576110
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Super(object):
        @classmethod
        def __call__(cls, *args, **kw):
            return cls
    class Sub(Super):
        __metaclass__ = Singleton
    assert Sub() is Sub()

# Generated at 2022-06-13 16:55:37.017587
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self, num):
            self.num = num

    t1 = Test(1)
    t2 = Test(2)
    print(t1, t2)
    assert t1.num == 1
    assert t2.num == 1

# unit test code
if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:55:40.246757
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    s1 = TestSingleton()
    s2 = TestSingleton()
    assert s1 is s2

# Generated at 2022-06-13 16:55:45.989550
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import random

    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            #self.name = name
            self.name = random.randint(0, 100)

    obj = MySingleton('Object 1')
    print(obj.name)

    obj1 = MySingleton('object 2')
    print(obj.name)

    print(obj1.name)

