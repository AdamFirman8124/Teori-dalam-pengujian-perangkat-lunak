

# Generated at 2022-06-13 16:46:35.361669
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self._value = value
    a = Test('foo')
    b = Test('bar')
    assert a is b  # Test objects are equal
    assert a._value == 'foo'  # Test object changes as per initialisation
    assert b._value == 'foo'

# Generated at 2022-06-13 16:46:43.518514
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    # create two instance of class A
    a1 = A(1)
    a2 = A(2)

    # ensure they have the same __instance
    assert a1 is a2
    assert a1.value == a2.value == 1


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:46:47.244460
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class X:
        __metaclass__ = Singleton

    assert X() is X()
    assert X() is X()
    x = X()
    assert x is X()
    x1 = X()
    assert x is x1
    assert x1 is x
    assert X() is X()



# Generated at 2022-06-13 16:46:50.703372
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(Singleton):
        def __init__(self, value=0):
            self.value = value
    inst0 = TestSingleton(0)
    inst1 = TestSingleton()
    inst2 = TestSingleton(2)
    assert inst0.value == inst1.value == inst2.value
    assert inst0.value == 0


# Generated at 2022-06-13 16:46:54.411132
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    with Singleton.__rlock:
       # Singleton.__instance already exists, so __call__ returns __instance
       assert(Singleton() == Singleton())
       # assert that __call__ does not instantiate _instance
       Singleton.__instance = None
       # __instance does not exist, so __call__ instantiates __instance
       Singleton()
       assert(Singleton.__instance is not None)
    pass

# Generated at 2022-06-13 16:46:58.001609
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object, metaclass=Singleton):
        def hello_world(self):
            return "Hello World"

        def __init__(self, v=None):
            if v:
                self.val = v

    s1 = MySingleton()
    s2 = MySingleton()
    assert s1 is s2

    s1 = MySingleton(100)
    s2 = MySingleton()
    assert s2.val == 100

# Generated at 2022-06-13 16:47:01.428842
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    assert A() == A()

# Generated at 2022-06-13 16:47:03.665067
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert a1 is a2



# Generated at 2022-06-13 16:47:06.221374
# Unit test for constructor of class Singleton
def test_Singleton():
    class myclass(object):
        __metaclass__ = Singleton

    obj1 = myclass()
    obj2 = myclass()
    assert obj1 is obj2



# Generated at 2022-06-13 16:47:09.455476
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    a = Foo()
    b = Foo()
    assert a is b


# Generated at 2022-06-13 16:47:16.339849
# Unit test for constructor of class Singleton
def test_Singleton():

    class SingletonTest(object):
        """This Class inherits from the Singleton metaclass"""
        __metaclass__ = Singleton
        value = 1

        def __init__(self, value):
            self.value = value

    assert SingletonTest(7).value == 7
    assert SingletonTest(10).value == 7

# Generated at 2022-06-13 16:47:22.463476
# Unit test for constructor of class Singleton
def test_Singleton():
    class obj(object, metaclass=Singleton):
        def __init__(self):
            self.str = 'test string'
    assert isinstance(obj, type)
    assert hasattr(obj, "__instance")
    assert hasattr(obj, "__rlock")
    assert not hasattr(obj, "str")
    obj1 = obj()
    assert hasattr(obj1, "str")
    assert isinstance(obj1, obj)
    assert obj1.str == 'test string'
    obj2 = obj()
    assert obj2.str == 'test string'

test_Singleton()

# Generated at 2022-06-13 16:47:26.490176
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Test for method Singleton.__call__"""
    class S(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 0
    s1 = S()
    s2 = S()
    s2.value += 1
    assert s1.value == 1

# Generated at 2022-06-13 16:47:31.226029
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    lock = RLock()
    instances = {}
    names = ['A', 'B', 'C']
    class C:
        __metaclass__ = Singleton

    for name in names:
        with lock:
            if name in instances:
                print('Error: expected only unique instances of class C')
                break
            instances[name] = C()

test_Singleton___call__()

# Generated at 2022-06-13 16:47:34.104315
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1

    assert TestClass().a == TestClass().a == 1

# Generated at 2022-06-13 16:47:40.128668
# Unit test for constructor of class Singleton
def test_Singleton():
    class testClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 1
            self.y = 2

    one = testClass()
    two = testClass()
    assert one.x == 1
    assert one.y == 2
    assert one == two


# Generated at 2022-06-13 16:47:46.113658
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.__value = value

        def getValue(self):
            return self.__value

    assert Test('foo') is Test('bar')
    assert Test('foo').getValue() == 'foo'
    assert Test('bar').getValue() == 'foo'

if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:47:56.062125
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

        @staticmethod
        def inst():
            return "instance returned"

    class S1(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    class S2(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    # Creating the instances for S, S1 and S2
    s = S()
    s1 = S1()
    s2 = S2()
    # Testing the functionality of constructor of class Singleton
    assert(s.inst() == "instance returned")
    assert(s1.__class__ is S1)
    assert(s2.__class__ is S2)

# Generated at 2022-06-13 16:47:59.382614
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.val = 10
    a = A()
    b = A()
    assert a is b

# Generated at 2022-06-13 16:48:01.334168
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(metaclass=Singleton):
        def __init__(self):
            pass

    a = MyClass()
    b = MyClass()
    assert a is b

# Generated at 2022-06-13 16:48:11.706386
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, a=1, b=2):
            self.a = a
            self.b = b

    a1 = A(a=2, b=3)
    a2 = A(a=4, b=5)

    assert a1.a == 2 and a1.b == 3 and a1.a == a2.a and a1.b == a2.b
    assert a1 == a2



# Generated at 2022-06-13 16:48:14.419732
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class __mock(metaclass=Singleton):
        def __init__(self, x):
            self.x = x

    obj1 = __mock(1)
    obj2 = __mock(2)

    assert obj1 is obj2
    assert obj2.x == 1

# Generated at 2022-06-13 16:48:20.640924
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value

    assert MySingleton('foo').get_value() == 'foo'
    assert MySingleton('bar').get_value() == 'foo'



# Generated at 2022-06-13 16:48:31.715015
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from copy import copy

    class Myclass(object):
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a

    class Myclass2(object):
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a

    v1 = Myclass(1)
    assert v1.a == 1

    v2 = Myclass(2)
    assert v2 is v1

    v3 = Myclass(3)
    assert v2 is v1
    assert v3 is v1

    v3 = Myclass2(3)
    assert v3.a == 1

    v4 = copy(v3)
    assert v4 is not v3



# Generated at 2022-06-13 16:48:38.924348
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass:
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 0

    test1 = TestClass()
    test2 = TestClass()

    assert test1 is test2
    assert test1.value == 0
    assert test2.value == 0

    test1.value = 1
    assert test1.value == test2.value == 1

    test2.value = 2
    assert test1.value == test2.value == 2

# Generated at 2022-06-13 16:48:43.363541
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self, str1):
            self.str1 = str1

    obj1 = MyClass('first_object')
    assert obj1.str1 == 'first_object'
    obj2 = MyClass('second_object')
    assert obj1 == obj2
    assert obj1.str1 == 'first_object'

# Generated at 2022-06-13 16:48:47.480642
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import random

    class TestSingleton: pass

    def run_task(class_):
        with class_() as instance:
            print("instance id:", id(instance))

    for __ in range(100):
        task = TestSingleton()
        thread = threading.Thread(target=run_task, args=(task,))
        thread.start()
        thread.join()

# Generated at 2022-06-13 16:48:49.421451
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()

    assert id(a) == id(b)
    assert a is b



# Generated at 2022-06-13 16:48:52.074973
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest:
        __metaclass__ = Singleton

    assert SingletonTest() is SingletonTest()
    assert SingletonTest() is not SingletonTest()

# Generated at 2022-06-13 16:48:55.467733
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # test singleton instances are the same
    class MyClass(object):
        __metaclass__ = Singleton

    a = MyClass()
    b = MyClass()
    assert a is b


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:49:06.861977
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self, x):
            self.x = x

    a1 = A(1)
    a2 = A(2)

    assert a1 == a2
    assert a1.x == 1
    assert a2.x == 1


# Generated at 2022-06-13 16:49:10.072628
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # create class with Singleton metaclass
    class Cube(object):
        __metaclass__ = Singleton

        def __init__(self, s):
            self.side = s

    c1 = Cube(3)
    c2 = Cube(4)

    # check that the instances are the same for both references
    assert(c1 is c2)
    # check that value of side is not changed by the call
    assert(3 == c2.side)

# Generated at 2022-06-13 16:49:12.008409
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(metaclass=Singleton):
        def __init__(self):
            self.created = True

    instance1 = TestClass()
    instance2 = TestClass()
    assert instance1 == instance2
    assert instance1.created == True
    assert instance2.created == True

test_Singleton()

# Generated at 2022-06-13 16:49:19.332916
# Unit test for constructor of class Singleton
def test_Singleton():
    class Adder(object, metaclass=Singleton):
        def __init__(self):
            self.data = 0

        def add(self, x):
            self.data += x

        def __str__(self):
            return str(self.data)

    a1 = Adder()
    a2 = Adder()
    assert a1 is a2
    a1.add(1)
    assert str(a1) == "1"
    assert str(a2) == "1"
    a2.add(2)
    assert str(a2) == "3"
    assert str(a1) == "3"

# Generated at 2022-06-13 16:49:22.434712
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 1

    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2, "Foo should implement Singleton"
    assert foo1.x == foo2.x == 1, "Foo should implement Singleton"

# Generated at 2022-06-13 16:49:24.190769
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object, metaclass=Singleton):
        pass

    a1 = A()
    a2 = A()
    assert a1 is a2, 'Instance of class A is not singleton'



# Generated at 2022-06-13 16:49:28.338435
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
  class SingletonTest(metaclass=Singleton):
      def __init__(self):
          self.foo = 'bar'
  instance1 = SingletonTest()
  assert instance1.foo == 'bar'

  instance2 = SingletonTest()
  assert instance1 == instance2
  assert instance1 is instance2
  assert instance1.__dict__ is instance2.__dict__
test_Singleton___call__()

# Generated at 2022-06-13 16:49:33.698079
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Unit test for method __call__ of class Singleton
    """

    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1

    my_obj1 = test_Singleton___call___MyClass()
    my_obj2 = test_Singleton___call___MyClass()

    assert my_obj1.a == 1
    assert my_obj2.a == 1

    my_obj1.a = 2
    assert my_obj2.a == 2

    my_obj2.a = 3
    assert my_obj1.a == 3



# Generated at 2022-06-13 16:49:41.741468
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest

    class A(object):
        __metaclass__ = Singleton

    class B(object):
        __metaclass__ = Singleton

    class C(A):
        pass

    class D(A):
        pass

    # Checking that:
    #   (1) for each class of the form class A(object):
    #         __metaclass__ = Singleton
    #       there is at most one instance of that class;
    #   (2) If a class C is a subclass of a class A, then all instances of
    #       class C are also instances of class A.
    a = A()
    b = B()
    c = C()
    d = D()

    assert(a is c)
    assert(a is d)
    assert(a is not b)

    # Comparing

# Generated at 2022-06-13 16:49:51.095673
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    for name, args in [('first', ('hello', 'world')), ('second', ('goodbye', 'world'))]:
        with SingletonTest.__rlock:
            instance = SingletonTest(*args)
            assert instance.arg1 == args[0]
            assert instance.arg2 == args[1]
            assert instance is SingletonTest(*args)
            assert instance is SingletonTest(*args)
            assert instance is SingletonTest.__instance

# Generated at 2022-06-13 16:50:05.877398
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo:
        __metaclass__ = Singleton
        def __init__(self, x, y):
            self.x = x
            self.y = y

            self.n_instance = 0

        def __str__(self):
            return str(self.x + self.y)

    f1 = Foo(1, 2)
    f2 = Foo(3, 4)
    assert f1 is f2
    assert f1.n_instance == 1 and f2.n_instance == 1
    assert str(f1) == str(f2) == '3'



# Generated at 2022-06-13 16:50:09.667332
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
    t1 = TestSingleton()
    t2 = TestSingleton()
    assert t1 is t2

# Generated at 2022-06-13 16:50:11.845115
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    instance1 = Singleton("test")
    instance2 = Singleton("test")
    assert instance1 is instance2


# Generated at 2022-06-13 16:50:14.879253
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    with DummySingleton() as dummy_singleton_1:
        pass

    with DummySingleton() as dummy_singleton_2:
        pass

    assert dummy_singleton_1 is dummy_singleton_2


# Dummy class for unit test

# Generated at 2022-06-13 16:50:19.097020
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    class B(object):
        __metaclass__ = Singleton

    assert A() == A()
    assert B() == B()
    assert A() != B()

# Generated at 2022-06-13 16:50:29.341802
# Unit test for constructor of class Singleton
def test_Singleton():
    class ExampleSingleton(object, metaclass=Singleton):
        def __init__(self):
            print('init')

    class ExampleSingletonOther(object, metaclass=Singleton):
        def __init__(self):
            print('initother')

    # first use of singleton
    instance1 = ExampleSingleton()
    instance1.test = 1
    instance2 = ExampleSingleton()
    assert instance1 == instance2
    assert hasattr(instance2, 'test')

    # other singleton
    instance3 = ExampleSingletonOther()
    instance3.test = 1
    instance4 = ExampleSingletonOther()
    assert instance3 == instance4
    assert hasattr(instance4, 'test')

    # the singletons are different
    assert not instance1 == instance4

# Generated at 2022-06-13 16:50:33.649484
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test = "test"
    one_instance = TestSingleton()
    two_instance = TestSingleton()
    assert one_instance.test == "test"
    assert one_instance == two_instance

# Generated at 2022-06-13 16:50:40.930925
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # This is the object used in the unit test
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, var=0):
            self.var = var

    # Create two instances of the class
    instance1 = TestClass(10)
    instance2 = TestClass(20)

    # Check that the instances are the same object
    assert instance1 == instance2
    # Check that the var is set to the value passed to the first call
    assert instance1.var == 10
    # Make sure that there is only one instance of the class
    assert len(TestClass.__dict__['_TestClass__instance']) == 1

# Generated at 2022-06-13 16:50:43.668143
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton

        def __new__(cls):
            return super(TestClass, cls).__new__(cls)

    assert TestClass() is TestClass()



# Generated at 2022-06-13 16:50:48.329682
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            self.arg = arg

    obj1 = MyClass(123)
    obj2 = MyClass(456)

    assert obj1 is obj2
    assert obj1.arg == obj2.arg == 123

# Generated at 2022-06-13 16:51:00.727695
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

    class SingletonTestSubclass(SingletonTest):
        pass

    assert SingletonTest() is SingletonTest()
    assert SingletonTestSubclass() is SingletonTestSubclass()



# Generated at 2022-06-13 16:51:11.571486
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # function:
    #     Singleton.__call__(*args, **kwargs)
    # in this case, args and kwargs are not used, for the purpose of test
    # __call__ function, we pass in invalid arguments, to test if the Singleton
    # class can handle invalid args and kwargs.
    class TestSingleton(metaclass=Singleton):
        """Test class for Singleton metaclass."""

        def __init__(self, test_args, test_kwargs):
            """Initialize class instance."""
            self.args = test_args
            self.kwargs = test_kwargs

        def get_args(self):
            return self.args

        def get_kwargs(self):
            return self.kwargs

    test_args = ('args', 'for', 'test')
    test

# Generated at 2022-06-13 16:51:21.166247
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a

    class B(object):
        __metaclass__ = Singleton
        def __init__(self, a, b):
            self.a = a
            self.b = b

    a = A(1)
    b = A(2)

    assert a is b
    assert a.a == 1
    assert b.a == 1

    c = B(2, 3)
    d = B(4, 5)

    assert c is d
    assert c.a == 2
    assert c.b == 3
    assert d.a == 2
    assert d.b == 3

# Generated at 2022-06-13 16:51:32.749483
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Neither is there an instance yet, nor is it instantiated yet
    class TestSingleton(object):
        __metaclass__ = Singleton

    # There is an instance, but not yet instantiated
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    # An instance already exists, but it's not initialized
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.initialized = True

    # An instance already exists, and it's initialized
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.initialized = True
        def __call__(self):
            return None

    # An instance already exists, and it's initialized,

# Generated at 2022-06-13 16:51:38.680672
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(metaclass=Singleton):
        def __init__(self, name=None):
            if name is not None:
                self.name = name

    fido = MySingleton('Fido')
    assert fido.name == 'Fido'

    rex = MySingleton()
    assert rex.name == 'Fido'

    fido2 = MySingleton()
    assert fido2 is fido

    fido.name = 'Rex'
    assert rex.name == 'Rex'
    assert fido2.name == 'Rex'


# Generated at 2022-06-13 16:51:42.405737
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(metaclass=Singleton):
        def __init__(self):
            self.test_attr_1 = 1
        def test_function_1(self):
            pass

    import unittest
    class TestSingleton(unittest.TestCase):
        def test_is_singleton(self):
            s1 = Test()
            s2 = Test()
            self.assertEqual(id(s1), id(s2))

    unittest.main()

# Generated at 2022-06-13 16:51:46.007983
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

    a = TestClass("kaka")
    b = TestClass("bobo")
    c = TestClass("xxx")
    assert id(a) == id(b) == id(c)

# Generated at 2022-06-13 16:51:51.677575
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 'foo'

    foo1 = Foo()
    assert(Foo.__instance is foo1)

    foo2 = Foo()
    assert(Foo.__instance is foo1)
    assert(foo1 is foo2)
    assert(foo1.value == 'foo')
    assert(foo2.value == 'foo')

    foo1.value = 'bar'
    assert(foo1.value == 'bar')
    assert(foo2.value == 'bar')



# Generated at 2022-06-13 16:51:55.231131
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonClass(object):
        __metaclass__ = Singleton

    # Test that instantiating SingletonClass more than once returns the
    # same instance.
    s = SingletonClass()
    t = SingletonClass()
    assert s is t

# Generated at 2022-06-13 16:51:56.387381
# Unit test for constructor of class Singleton
def test_Singleton():
    assert Singleton is not None
    assert type(Singleton) == type

# Generated at 2022-06-13 16:52:15.444378
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class X:
        __metaclass__ = Singleton

    assert X() is X()



# Generated at 2022-06-13 16:52:19.463162
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            print("Foo __init__")
            self.x = "aha"

    assert Foo.__instance == None
    assert Foo.__rlock == None
    assert Foo().x == "aha"
    assert Foo.__instance == Foo()


# Generated at 2022-06-13 16:52:21.251005
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    t1 = TestClass()
    t2 = TestClass()
    assert t1 is t2

# Generated at 2022-06-13 16:52:25.906315
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self, x):
            self.x = x

    a = A(1)
    assert a.x == 1
    b = A(2)
    assert a is b

    class B(metaclass=Singleton):
        def __init__(self):
            self.x = []

    b = B()
    assert b.x == []
    c = B()
    assert b is c
    assert b.x is c.x
    b.x.append(1)
    assert b.x is c.x
    assert c.x == [1]

# Test for derived classes

# Generated at 2022-06-13 16:52:31.081159
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    a = A()
    del(A)  # deleting the class definition will remove the singleton instance
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    a1 = A()
    assert a1 == a



# Generated at 2022-06-13 16:52:34.763506
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class TestClass(object):
        __metaclass__ = Singleton

    s1 = TestClass()
    s2 = TestClass()
    assert s1 is s2


# Generated at 2022-06-13 16:52:36.787629
# Unit test for constructor of class Singleton
def test_Singleton():
    class Example(metaclass=Singleton):
        pass

    e1 = Example()
    e2 = Example()
    assert(e1 == e2)

# Generated at 2022-06-13 16:52:41.487166
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object):
        __metaclass__ = Singleton

        def __init__(self, *args):
            self.x = args

    a = S(1, 2, 3)
    assert a.x == (1, 2, 3)
    b = S(4, 5, 6)
    assert b.x == (1, 2, 3)
    assert a is b

# Generated at 2022-06-13 16:52:48.334558
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import threading
    import time
    import signal

    class MySingleton(object):
        __metaclass__ = Singleton

    def _create_instance():
        for i in range(10):
            MySingleton()
            time.sleep(0.1)

    def _create_thread(func):
        th = threading.Thread(target=func)
        th.start()
        return th

    threads = []

    for i in range(5):
        threads.append(_create_thread(_create_instance))

    for th in threads:
        th.join()

    # in this case, class MySingleton should have only one instance
    assert MySingleton() is MySingleton()


# Example of usage

# Generated at 2022-06-13 16:52:50.013570
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    c1 = TestClass()
    c2 = TestClass()

    assert(c1 is c2)

# Generated at 2022-06-13 16:53:26.102124
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    a = Test()
    b = Test()

    assert a == b


# Generated at 2022-06-13 16:53:32.969046
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from threading import Thread

    class TestSingleton(object):
        __metaclass__ = Singleton

    # Make sure that the initial singleton instance is created
    assert TestSingleton()

    # Make sure that the initial singleton instance is reused
    assert TestSingleton() is TestSingleton()

    # Make sure that the singleton instance is thread-safe
    class ThreadTestSingleton(Thread):
        def run(self):
            assert TestSingleton() is TestSingleton()
    assert ThreadTestSingleton().start()

    # Create another singleton class to test metaclass inheritance
    class TestSingletonParent(object):
        __metaclass__ = Singleton

    class TestSingletonChild(TestSingletonParent):
        pass

    # Make sure that the initial singleton instance is created
    assert TestSingletonChild()

    # Make sure

# Generated at 2022-06-13 16:53:34.664787
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
    t = Test()
    assert t is Test()
    assert t is Test()

# Generated at 2022-06-13 16:53:37.255696
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Y(object):
        __metaclass__ = Singleton
        def __init__(self, x=1):
            self.x = x

    y1 = Y()
    y2 = Y()
    assert(y1 is y2)

    y1.x = 10
    assert(y2.x == 10)

# Generated at 2022-06-13 16:53:47.066635
# Unit test for constructor of class Singleton
def test_Singleton():
    class singleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = "foo"
            self.b = "bar"

    s = singleton()
    assert s.a == "foo"
    assert s.b == "bar"
    s2 = singleton()
    assert s2.a == "foo"
    assert s2.b == "bar"
    s3 = singleton()
    assert s3.a == "foo"
    assert s3.b == "bar"
    assert s is s2 and s is s3

    # see if subclassing works
    class singletonchild(singleton):
        def __init__(self):
            self.c = "bah"

    sc = singletonchild()
    assert sc.a == "foo"
   

# Generated at 2022-06-13 16:53:56.149778
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    x = 1
    y = 2

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, x, y):
            self.x = x
            self.y = y

    test_instance1 = TestSingleton(x, y)
    assert test_instance1.x == x and test_instance1.y == y, 'TestSingleton did not initialize properly'

    test_instance2 = TestSingleton(y, x)
    assert test_instance1 is not test_instance2, 'TestSingleton is not a singleton'
    assert test_instance2.x == x and test_instance2.y == y, 'TestSingleton did not initialize properly'


if __name__ == '__main__':

    test_Singleton___call__()

# Generated at 2022-06-13 16:54:01.108050
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    ### Given
    class SingletonTest(object):
        __metaclass__ = Singleton
    ### When
    singleton1 = SingletonTest()
    singleton2 = SingletonTest()
    ### Then
    assert singleton1 == singleton2

# Test Singleton class

# Generated at 2022-06-13 16:54:08.824411
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 'bar'
            print('initializing A')

    a1 = A()
    a2 = A()
    print(a1)
    print(a2)
    print(a1 is a2)
    print(a1.foo)
    print(a2.foo)
    a1.foo = 'baz'
    print(a1.foo)
    print(a2.foo)

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:54:16.812909
# Unit test for constructor of class Singleton
def test_Singleton():
    from ansible.module_utils.parsing.convert_bool import BOOLEANS_TRUE
    from ansible.module_utils.six import string_types

    my_exception = Exception("foo")

    class MyClass(metaclass=Singleton):

        def __init__(self):
            self.booleans_true = BOOLEANS_TRUE
            self.my_exception = my_exception

    instance = MyClass()
    assert isinstance(instance, MyClass)
    assert instance.booleans_true == BOOLEANS_TRUE
    assert instance.my_exception == my_exception

    other = MyClass()
    assert instance is other
    assert instance.booleans_true is other.booleans_true
    assert instance.my_exception is other.my_ex

# Generated at 2022-06-13 16:54:23.790515
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyTest(object):
        __metaclass__ = Singleton
        pass

    my_test1 = MyTest()
    my_test2 = MyTest()

    assert my_test1 == my_test2

    class MyTest(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    my_test1 = MyTest()
    my_test2 = MyTest()

    assert my_test1 == my_test2

    class MyTest(object):
        __metaclass__ = Singleton
        def __init__(self, arg):
            self.arg = arg

    my_test1 = MyTest(1)
    my_test2 = MyTest(2)

    assert my_test1 == my_test2
    assert my_test1.arg == 1

   

# Generated at 2022-06-13 16:55:36.327984
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    # test that the class TestSingleton has the method __call__ of class Singleton
    assert TestSingleton.__call__ == Singleton.__call__

    instance1 = TestSingleton()
    instance2 = TestSingleton()
    assert id(instance1) == id(instance2)

# Generated at 2022-06-13 16:55:39.683192
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert a is b



# Generated at 2022-06-13 16:55:46.019459
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo:
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1
    
    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2
    assert foo1.a == 1
    assert foo2.a == 1
    foo2.a = 2
    assert foo1.a == 2
    assert foo2.a == 2
    foo2.__init__()
    assert foo1.a == 1
    assert foo2.a == 1

# Generated at 2022-06-13 16:55:49.891158
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    ts = TestSingleton()
    assert ts is TestSingleton()
    assert ts is TestSingleton()
    assert ts is TestSingleton()



# Generated at 2022-06-13 16:55:55.693667
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Let's define class TestClass as a Singleton
    class TestClass(object):
        __metaclass__ = Singleton

    # The first call of TestClass returns an instance of class TestClass
    x = TestClass()
    assert isinstance(x, TestClass)

    # The second call of TestClass returns the same instance as before (Singleton)
    y = TestClass()
    assert isinstance(y, TestClass)

    # Check that x and y are the same instance
    assert x == y

# Generated at 2022-06-13 16:55:58.956883
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(metaclass=Singleton):
        def __init__(self, value):
            self.value = value

    instance = Test(value=1)
    assert instance.value == 1

    instance = Test(value=2)
    assert instance.value == 1

# Generated at 2022-06-13 16:56:04.912687
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Test Singleton metaclass to make sure we get only one instance
    # of a class regardless of how many times we instantiate it

    class TestClass(object):
        __metaclass__ = Singleton

    test_inst_1 = TestClass()
    test_inst_2 = TestClass()

    assert test_inst_1 is test_inst_2
    assert id(test_inst_1) == id(test_inst_2)

    # Test subclass inherits from Singleton
    class TestSubClass(TestClass):
        pass

    test_inst_1 = TestSubClass()
    test_inst_2 = TestSubClass()
    assert test_inst_1 is test_inst_2
    assert id(test_inst_1) == id(test_inst_2)



# Generated at 2022-06-13 16:56:08.641042
# Unit test for constructor of class Singleton
def test_Singleton():
    class Dummy(object):
        __metaclass__ = Singleton
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2
    d = Dummy('abc', '123')
    assert d.arg1 == 'abc'
    assert d.arg2 == '123'
    assert d == Dummy('abc', '123')
    assert hasattr(d, '__rlock')
    assert isinstance(d.__rlock, RLock)

# Generated at 2022-06-13 16:56:10.462795
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
    first_inst = Test()  # pylint: disable=invalid-name
    second_inst = Test()  # pylint: disable=invalid-name
    assert first_inst is second_inst

# Generated at 2022-06-13 16:56:15.550010
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            print("__init__() is called")

    class TestSingleton2(object):
        __metaclass__ = Singleton

        def __init__(self):
            print("__init__() is called")

    assert TestSingleton() is TestSingleton()
    assert TestSingleton2() is TestSingleton2()