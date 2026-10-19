

# Generated at 2022-06-13 16:46:33.824258
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(metaclass=Singleton):
        pass

    a = TestSingleton()
    b = TestSingleton()

    assert a is b



# Generated at 2022-06-13 16:46:46.563996
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, val=0):
            self.val = val

    a = Foo(1)
    b = Foo()
    assert b == a
    assert b.val == a.val
    assert a.val == 1

    # make sure that we can have multiple singletons
    class Bar(object):
        __metaclass__ = Singleton
        def __init__(self, val=0):
            self.val = val

    c = Bar(2)
    d = Bar()
    assert d == c
    assert d.val == c.val
    assert a.val == 1
    assert c.val == 2


# Generated at 2022-06-13 16:46:48.409685
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    assert(foo1 == foo2)



# Generated at 2022-06-13 16:46:51.330411
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonBaseClass(object):
        pass

    class TestSingletonClass(SingletonBaseClass):
        def __init__(self):
            pass

    t_class = TestSingletonClass()
    assert(isinstance(t_class, TestSingletonClass))

# Generated at 2022-06-13 16:46:53.875059
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class ConcreteSingleton(object):
        __metaclass__ = Singleton
    assert type(ConcreteSingleton()) is ConcreteSingleton
    assert type(ConcreteSingleton()) is ConcreteSingleton

# Generated at 2022-06-13 16:46:59.140536
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, a, b):
            self.a = a
            self.b = b

    a = TestSingleton(1, 2)
    b = TestSingleton(3, 4)

    assert a.a == 1
    assert a.b == 2
    assert b.a == 1
    assert b.b == 2
    assert a is b


# Generated at 2022-06-13 16:47:05.317391
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # class X(metaclass=Singleton):
    class X(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3

    x1 = X()
    x2 = X()
    x3 = X()
    assert x1 is x2 is x3

    x1.a = 123
    assert x1.a == x2.a == x3.a == 123

# Generated at 2022-06-13 16:47:15.975007
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.test_args = []
            self.test_kwargs = []

        def function(self, *args, **kwargs):
            self.test_args.append(args)
            self.test_kwargs.append(kwargs)

    test1 = TestSingleton(1, 2, 3, a=1, b=2, c=3)
    test1.function('a', 'b', 'c', d=1, e=2, f=3)
    test2 = TestSingleton('a', 'b', 'c', a=1, b=2, c=3)


# Generated at 2022-06-13 16:47:17.837591
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
    o1 = Test()
    o2 = Test()
    assert o1 is o2

# Generated at 2022-06-13 16:47:28.537604
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import copy

    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    a = Foo()
    b = Foo()
    c = Foo()

    # a, b and c should refer to the same object
    assert a is b
    assert a is c

    # the object referred to by a, b and c should be a Foo instance
    assert isinstance(a, Foo)
    assert isinstance(b, Foo)
    assert isinstance(c, Foo)

    # and all three references should be shallow copies
    assert a == b
    assert a == c
    assert b == c

    # now let's make sure we can't instantiate Foo by any other method
    d = copy.copy(a)
    e = copy.deepcopy(a)
    f = Foo()



# Generated at 2022-06-13 16:47:34.181398
# Unit test for constructor of class Singleton
def test_Singleton():
    # New instance is created
    assert Singleton('Singleton', (object,), {'__init__': lambda self: None})()
    # Singleton instance remains the same
    assert Singleton('Singleton', (object,), {'__init__': lambda self: None})()



# Generated at 2022-06-13 16:47:36.204721
# Unit test for constructor of class Singleton
def test_Singleton():
    x = Singleton("Singleton", (), dict(i=123))
    y = Singleton("Singleton", (), dict(i=123))

    assert x == y

# Generated at 2022-06-13 16:47:37.986016
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    # Same objects
    assert TestSingleton() is TestSingleton()



# Generated at 2022-06-13 16:47:44.264332
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, n):
            self.n = n

    c1 = TestClass('c1')
    c2 = TestClass('c2')

    assert c1 == c2
    assert c1 is c2
    assert c1.n == c2.n == 'c1' and c1.n != 'c2'


# Generated at 2022-06-13 16:47:47.894276
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(metaclass=Singleton):
        # a simple class
        pass

    f1 = Foo()
    f2 = Foo()

    assert f1 is f2

# Generated at 2022-06-13 16:47:51.338954
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

    instance_1 = SingletonTest()
    instance_2 = SingletonTest()
    assert instance_1 == instance_2

# Test definition for class Singleton

# Generated at 2022-06-13 16:47:58.266907
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1
    a1 = A()
    assert a1.a == 1
    a2 = A()
    assert a2.a == 1
    a2.a = 2
    assert a1.a == 2
    assert a2.a == 2



# Generated at 2022-06-13 16:48:00.531121
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestCls:
        __metaclass__ = Singleton

    ta = TestCls()
    tb = TestCls()
    assert id(ta) == id(tb)
    assert ta is tb

# Generated at 2022-06-13 16:48:06.949506
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton1(object):
        __metaclass__ = Singleton
        def __init__(self, a=1, b=2):
            self.a = a
            self.b = b

    class MySingleton2(object):
        __metaclass__ = Singleton
        def __init__(self, a=1, b=2):
            self.a = a
            self.b = b

    class MySingleton3(object):
        __metaclass__ = Singleton
        def __init__(self, a=1, b=2):
            self.a = a
            self.b = b

    instance1 = MySingleton1()
    instance2 = MySingleton2()
    instance3 = MySingleton3()


# Generated at 2022-06-13 16:48:10.324410
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from nose.tools import assert_equal

    class Dummy(object):
        __metaclass__ = Singleton

    instance1 = Dummy()
    instance2 = Dummy()
    assert_equal(instance1, instance2)

# Generated at 2022-06-13 16:48:18.013494
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x

    a1 = A(1)
    a2 = A(2)
    assert a1 is a2
    assert a1.x == 1
    assert a2.x == 1


# Generated at 2022-06-13 16:48:27.817194
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import types
    import pytest
    from ansible.module_utils.common._collections_compat import Mapping, Sequence
    from ansible.module_utils.common.json_dict import AnsibleJSONEncoder

    # Instantiate a class with function __call__
    class Test(object):
        def __call__(self, *args, **kwargs):
            return (args, kwargs)

    # Instantiate a class with a nested function __call__ (should not be detected by the metaclass)
    class TestParent(object):
        class TestChild(object):
            def __call__(self, *args, **kwargs):
                return (args, kwargs)

    # Test bad input

# Generated at 2022-06-13 16:48:30.071324
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2



# Generated at 2022-06-13 16:48:32.404825
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 'bar'

    test1 = Test()
    assert test1.foo == 'bar'

    test2 = Test()
    assert test1 is test2

# Generated at 2022-06-13 16:48:34.438808
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Thing(object):
        __metclass__ = Singleton

    a = Thing()
    b = Thing()

    assert a == b

# Generated at 2022-06-13 16:48:41.740145
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self, baz):
            self._baz = baz

    foo = Foo('flob')
    assert isinstance(foo, Foo)
    assert foo._baz == 'flob'

    foo_2 = Foo('cronk')
    assert isinstance(foo_2, Foo)
    assert foo_2._baz == 'flob'
    assert foo_2 is foo


# Generated at 2022-06-13 16:48:48.219314
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Some class hierarchy with Singleton metaclass
    class Base(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.b = 1

    class Derived(Base):
        pass

    # Instantiate Base class
    instance1 = Base()
    assert instance1.b == 1

    # Instantiate Base class again by using class name
    instance2 = Base()
    assert instance1 is instance2
    assert instance2.b == 1

    # Instantiate Base class again by using class name
    # with overriding __new__ method
    class Base2(Base):
        pass

    instance3 = Base2()
  

# Generated at 2022-06-13 16:48:57.387807
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Test class
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.test_field = 1
            self.mutable_field = [1, 2, 3]

    # Test 1st call
    test_class_1 = TestClass()
    if test_class_1.test_field != 1:
        raise AssertionError('test_class_1.test_field != 1')

    # Test 2nd call
    test_class_2 = TestClass()
    if test_class_2.test_field != 1:
        raise AssertionError('test_class_2.test_field != 1')
    if test_class_1 is not test_class_2:
        raise AssertionError('test_class_1 is not test_class_2')

# Generated at 2022-06-13 16:49:05.841953
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 5

    instance1 = MySingleton()
    instance2 = MySingleton()

    assert instance1.value == 5
    assert instance2.value == 5
    assert instance1 is instance2

    instance1.value = 10
    assert instance2.value == 10

    instance2.value = 15
    assert instance1.value == 15


# Generated at 2022-06-13 16:49:11.038706
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, value=None):
            self.__value = value
            self.__number_of_calls = 0

        def get_number_of_calls(self):
            return self.__number_of_calls

        def set_value(self, value):
            self.__value = value
            self.__number_of_calls += 1

        def get_value(self):
            return self.__value

    TestSingleton(1)
    TestSingleton(2)
    TestSingleton(3)
    TestSingleton(4)
    TestSingleton(5)
    TestSingleton(6)

    t = TestSingleton()
    print('TestSingleton(1)')

# Generated at 2022-06-13 16:49:15.910566
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton

    assert MySingleton is MySingleton()
    assert MySingleton() is MySingleton()
    assert MySingleton() is MySingleton.__instance


# Generated at 2022-06-13 16:49:17.873229
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton


a = A()
b = A()
assert a is b

# Generated at 2022-06-13 16:49:23.379459
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test01(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    class Test02(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1
            self.b = 2
            self.z = [3, 4]

    t1 = Test01()
    assert t1 is Test01()
    assert t1 is Test01()
    assert t1 is Test01()

    t2 = Test02()
    assert t2 is Test02()
    assert t2 is Test02()
    assert t2 is Test02()


# Generated at 2022-06-13 16:49:30.530986
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test:
        __metaclass__ = Singleton

        def __init__(self, a=0):
            self.a = a

    # The first call should create an instance
    test1 = Test(a=1)
    assert test1.a == 1

    # The second call should return the same instance
    test2 = Test(a=2)
    assert test2.a == 1
    assert id(test1) == id(test2)

# Generated at 2022-06-13 16:49:35.673221
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Example:
        __metaclass__ = Singleton
        def __init__(self, arg):
            self.arg = arg

    e1 = Example('test')
    assert(e1.arg == 'test')

    e2 = Example('test2')
    assert(e2.arg == 'test')



# Generated at 2022-06-13 16:49:38.903369
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, bar):
            self.bar = bar

    foo_a = Foo("a")
    foo_b = Foo("b")
    assert foo_a is foo_b

# Generated at 2022-06-13 16:49:40.282018
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert A() is A()

# Generated at 2022-06-13 16:49:44.530542
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self._value = 0

        def _increment_value(self):
            self._value += 1

        def get_value(self):
            return self._value

    TestSingleton._increment_value()
    # Because TestSingleton is a singleton class,
    # so these two lines should get the same instance
    assert TestSingleton() == TestSingleton()
    TestSingleton._increment_value()
    assert TestSingleton.get_value() == 2


# Generated at 2022-06-13 16:49:48.044653
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyObject(object):
        __metaclass__ = Singleton
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def __eq__(self, other):
            return self.x == other.x and self.y == other.y

    obj1 = MyObject(1,2)
    obj2 = MyObject(1,2)
    assert obj1 == obj2
    assert id(obj1) == id(obj2)
    obj2 = MyObject(2,3)
    assert obj1 != obj2


# Generated at 2022-06-13 16:49:53.106985
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    # Test if singleton works
    a = Test(42)
    b = Test(43)
    assert a is b

# Generated at 2022-06-13 16:50:03.593328
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.test = 5

    a1 = A()
    a2 = A()
    a3 = A()

    assert(a1 == a2 == a3)
    assert(a1.test == a2.test == a3.test)
    a3.test = 6
    assert(a1.test == a2.test == a3.test)
    a1.test = 7
    assert(a1.test == a2.test == a3.test)

# Generated at 2022-06-13 16:50:06.810458
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object, metaclass=Singleton):
        def __init__(self):
            self.test = 'test'

    a1 = A()
    a2 = A()
    assert a1 == a2

    from ansible import constants as C
    C1 = C()
    C2 = C()
    assert C1 == C2

# Generated at 2022-06-13 16:50:10.606247
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    o1 = Test()
    o2 = Test()
    assert o1 is o2



# Generated at 2022-06-13 16:50:12.850015
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass
    TestSingleton()
    TestSingleton()

# Generated at 2022-06-13 16:50:20.915675
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import random # Otherwise the random numbers are the same every test
    class SingletonClass(metaclass=Singleton):
        def __init__(self):
            self.x = random.randint(1,1000)
        def test_method(self):
            return self.x

    sc1 = SingletonClass()
    sc2 = SingletonClass()
    assert sc1 is sc2
    assert sc1.test_method() == sc2.test_method()

# Generated at 2022-06-13 16:50:24.533300
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SomeClass(metaclass=Singleton):
        pass

    o1 = SomeClass()
    o2 = SomeClass()
    assert o1 == o2
    assert id(o1) == id(o2)

# Generated at 2022-06-13 16:50:32.724321
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest
    class TestSingletonMeta(object):
        __metaclass__ = Singleton

    class SingletonTest(unittest.TestCase):
        def test_Singleton___call__(self):
            test_singleton_meta_object_1 = TestSingletonMeta()
            test_singleton_meta_object_2 = TestSingletonMeta()

            self.assertEqual(test_singleton_meta_object_1, test_singleton_meta_object_2)
            self.assertEqual(test_singleton_meta_object_1.__class__, test_singleton_meta_object_2.__class__)

    suite = unittest.TestLoader().loadTestsFromTestCase(SingletonTest)
    unittest.TextTestRunner(verbosity=2).run(suite)


# Generated at 2022-06-13 16:50:35.187034
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    instance_one = Singleton()
    instance_two = Singleton()
    assert instance_one == instance_two


# Generated at 2022-06-13 16:50:43.025778
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Create two instances for singleton class, instance s1
    # and instance s2 should be same
    class SingletonTest(object):
        __metaclass__ = Singleton
    s1 = SingletonTest()
    s2 = SingletonTest()
    assert hasattr(s1, '__instance')
    assert hasattr(s2, '__instance')
    assert s1 is s2
    assert id(s1) == id(s2)

    # Create two instances for singleton class, instance s3
    # and instance s4 should be same
    class SingletonTest2(object):
        def __init__(self):
            self.foo = 'bar'
        __metaclass__ = Singleton
    s3 = SingletonTest2()
    s4 = SingletonTest2()

# Generated at 2022-06-13 16:50:44.487559
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    assert Test() is Test()


# Generated at 2022-06-13 16:50:54.248638
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    class Bar(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    bar1 = Bar()
    bar2 = Bar()

    assert foo1 is foo2
    assert bar1 is bar2
    assert foo1 is not bar1

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:50:56.041124
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
   class X(object):
      __metaclass__ = Singleton
      def __init__(self):
         print("INIT")

   a = X()
   assert(a is X())
   assert(a == X())

# Generated at 2022-06-13 16:50:58.993713
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    t1 = TestSingleton()
    t2 = TestSingleton()
    assert t1 is t2

# Generated at 2022-06-13 16:51:00.719991
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class a(metaclass=Singleton):
        def __init__(self):
            self.a = 1
    a1 = a()
    a2 = a()
    assert a1 == a2, 'Singleton class __call__ method failed'
    return True

# Generated at 2022-06-13 16:51:03.110649
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

    singleton1 = SingletonTest()
    singleton2 = SingletonTest()
    assert singleton1 is singleton2

# Generated at 2022-06-13 16:51:12.461560
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        def __init__(self):
            self.value = 42

    a = TestClass()
    assert isinstance(a, TestClass)
    assert a.value == 42
    b = TestClass()
    assert isinstance(b, TestClass)
    assert a.value == b.value  # test a == b
    assert id(a) == id(b)
    c = TestClass()
    assert id(c) == id(a)  # test a == c != b
    assert a is c  # test a == c != b
    assert b is c  # test b == c != a

# Generated at 2022-06-13 16:51:22.792943
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from mock import Mock, patch

    class MySingleton:
        __metaclass__ = Singleton
        pass

    with patch('__builtin__.super') as super_:
        with patch('__builtin__.type') as type_:
            type_.return_value = Mock()
            # Test case where we have no instance
            MySingleton.__instance = None
            MySingleton.__rlock = RLock()
            type_.return_value.__call__.return_value = Mock()
            MySingleton('1', '2')
            type_.assert_called_with('MySingleton', ('1', '2'), dict())
            type_.return_value.__call__.assert_called_with()
            super_.assert_called_with(MySingleton, MySingleton)
            # Test case where we already have an

# Generated at 2022-06-13 16:51:26.893403
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    a = TestClass()
    b = TestClass()

    assert a == b


# Generated at 2022-06-13 16:51:29.361502
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

    assert isinstance(SingletonTest(), SingletonTest)

# Generated at 2022-06-13 16:51:32.670422
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1
    a1 = A()
    a2 = A()
    assert a1 is a2



# Generated at 2022-06-13 16:51:50.421772
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 0

        def set_value(self, value):
            self.value = value

        def get_value(self):
            return self.value

    instance = TestClass()
    instance.set_value(1)

    assert isinstance(instance, TestClass)

    instance2 = TestClass()
    instance2.set_value(2)

    assert instance2 is instance
    assert instance2.get_value() == 2
    assert instance.get_value() == 2

# Generated at 2022-06-13 16:51:54.246026
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert(a1 is a2)



# Generated at 2022-06-13 16:51:59.441556
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(metaclass=Singleton):
        def __init__(self, i):
            self._i = i

        def get(self):
            return self._i
    a = Test(1)
    b = Test(2)
    assert a.get() == b.get() == a._i == 1

    # Create new instance
    c = Test(3)
    assert c.get() == 3
    d = Test(4)
    assert d.get() == 4

test_Singleton___call__()

# Generated at 2022-06-13 16:52:02.887745
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1

    a = A()
    b = A()

    assert a == b
    assert a.a == 1

# Generated at 2022-06-13 16:52:13.503021
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Test if two instance of the same class returns
    the same object.
    """
    from threading import Thread

    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

        def set_value(self, value):
            self.value = value

        def get_value(self):
            return self.value

    instance1 = TestClass()
    instance1.set_value("test value")

    assert instance1 == TestClass()
    assert instance1.get_value() == TestClass().get_value()

    def thread_get_value(thread_name):
        t_object = TestClass()
        t_object.get_value()

    def thread_set_value(thread_name):
        t_object = TestClass()
        t_object.set_

# Generated at 2022-06-13 16:52:18.191190
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(metaclass=Singleton):
        def __init__(self, val=None):
            self.val = val

        def __str__(self):
            return 'val:%s' % self.val

    assert TestSingleton('foo') is TestSingleton('bar')
    assert str(TestSingleton('foo')) == 'val:bar'

# Generated at 2022-06-13 16:52:19.971810
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert a is b



# Generated at 2022-06-13 16:52:22.920611
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a

    a1 = A('a')
    a2 = A('b')
    assert(a1 == a2)
    assert(a1.a == 'a')
    assert(a2.a == 'a')



# Generated at 2022-06-13 16:52:26.246825
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(metaclass=Singleton):
        def __init__(self):
            self.__value = None

        def set_value(self, value):
            self.__value = value

        def get_value(self):
            return self.__value

    new_instance1 = TestSingleton()
    new_instance2 = TestSingleton()

    assert new_instance1 == new_instance2

    new_instance1.set_value("test value")

    assert new_instance1.get_value() == new_instance2.get_value()

# Generated at 2022-06-13 16:52:32.660906
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    print("Test class Singleton and method __call__")
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            print("Initializing MyClass")

    myc1 = MyClass()
    print("myc1={0}".format(myc1))
    myc2 = MyClass()
    print("myc2={0}".format(myc2))
    assert myc1 == myc2


if __name__ == '__main__':
    print("Execute unit test for class Singleton")
    test_Singleton___call__()

# Generated at 2022-06-13 16:52:59.070662
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

    class MySubClass(MyClass):
        pass

    inst1 = MyClass()
    inst2 = MyClass()
    assert inst1 is inst2

    inst3 = MySubClass()
    inst4 = MySubClass()
    assert inst3 is inst4

    assert inst1 is not inst3

# Generated at 2022-06-13 16:53:01.536427
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(metaclass=Singleton):
        pass

    c1 = MyClass()
    c2 = MyClass()

    assert c1 is c2, "c1 and c2 are not the same instance"

    c3 = MyClass()

    assert c3 is c2, "c3 is not the same instance as c2"

# Generated at 2022-06-13 16:53:05.242922
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    a1 = A('a1')
    assert a1.value == 'a1'
    assert A('a2').value == 'a1'


# Generated at 2022-06-13 16:53:10.762853
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, *args, **kwargs):
            print('Foo __init__')
            self.name = kwargs['name']

    f = Foo(name = 'x')
    assert f.name == 'x'
    f2 = Foo(name = 'y')
    assert f.name == 'x'
    assert f2.name == 'x'
    assert f == f2


# Generated at 2022-06-13 16:53:12.893453
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class DummyClass(object):
        __metaclass__ = Singleton

    x = DummyClass()
    y = DummyClass()
    assert x == y


# Generated at 2022-06-13 16:53:14.666411
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    assert id(foo1) == id(foo2)


# Generated at 2022-06-13 16:53:23.510121
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    _decorated_classes = []

    def decorate_class_with_Singleton_metaclass(cls):
        _decorated_classes.append(cls)
        return Singleton(cls.__name__, cls.__bases__, dict(cls.__dict__))

    class Foo(object):
        __metaclass__ = decorate_class_with_Singleton_metaclass

    class Bar(object):
        __metaclass__ = decorate_class_with_Singleton_metaclass

    # check that returned instances are equal and that there is only one instance
    assert id(Foo()) == id(Foo())
    assert id(Bar()) == id(Bar())
    assert id(Foo()) != id(Bar())

    # check there is only one instance per class
    assert len

# Generated at 2022-06-13 16:53:28.676292
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, foo, bar=1):
            self.foo = foo
            self.bar = bar
    a1 = A(3)
    a2 = A(4)
    assert a1 is a2
    assert a1.foo == 3
    assert a1.bar == 1
    assert a2.foo == 3
    assert a2.bar == 1



# Generated at 2022-06-13 16:53:32.781283
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(metaclass=Singleton):
        def __init__(self, value=0):
            self.value = value
    a = MyClass(value=10)
    b = MyClass(value=20)
    if not a == b:
        raise AssertionError()
    if not a.value == 10:
        raise AssertionError()
    if not b.value == 10:
        raise AssertionError()


# Generated at 2022-06-13 16:53:33.790632
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()

    assert a1 == a2

# Generated at 2022-06-13 16:54:25.161244
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 0

        def get_value(self):
            return self.value

        def set_value(self, value):
            self.value = value

    my_instance_1 = MyClass()
    my_instance_1.set_value(9)
    my_instance_2 = MyClass()
    print(my_instance_2.get_value())


# Generated at 2022-06-13 16:54:27.426762
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()

    assert foo1 is foo2

# Generated at 2022-06-13 16:54:35.160196
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # create a class using Singleton as metaclass
    class ClassWithSingleton(object):
        __metaclass__ = Singleton

    # nb_instances will increase each time a new instance of the class is
    # created.
    nb_instances = 0
    def inc():
        global nb_instances
        nb_instances += 1

    # in the following loop:
    # - a new instance of the class is created
    # - the current value of nb_instances is recorded
    # - the instance is deleted
    # - a new instance of the class is created
    # - the new value of nb_instances is recorded
    # - the instance is deleted
    # - the values of both nb_instances are compared
    #
    # This loop ensures that there is a single instance of the class.

# Generated at 2022-06-13 16:54:36.599906
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

    a = SingletonTest()
    b = SingletonTest()
    assert a == b

# Generated at 2022-06-13 16:54:37.464015
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class S(object):
        __metaclass__ = Singleton

    assert S() is S()


# Generated at 2022-06-13 16:54:40.665735
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Dummy(with_metaclass(Singleton)):
        def __init__(self, value):
            self.value = value

    d1 = Dummy(1)
    d2 = Dummy(2)

    assert d1.value == 1
    assert d2.value == 1

# Generated at 2022-06-13 16:54:44.710424
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 0

    a = Test()
    b = Test()

    assert a == b
    assert id(a) == id(b)


# Generated at 2022-06-13 16:54:46.885862
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import threading

    class TestClass(metaclass=Singleton):
        pass

    test1 = TestClass()
    test2 = TestClass()
    assert test1 == test2

# Generated at 2022-06-13 16:54:56.920880
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    arg1 = 'foo'
    arg2 = 1
    kwarg1 = 'bar'
    kwarg2 = 2

    # Calling __call__ twice should return the same instance
    instance1 = TestSingleton(arg1, arg2, kwarg1=kwarg1, kwarg2=kwarg2)
    instance2 = TestSingleton()

    assert instance1 == instance2
    assert instance1.args == (arg1, arg2)
    assert instance1.kwargs == {kwarg1: kwarg1, kwarg2: kwarg2}

# Generated at 2022-06-13 16:54:59.106258
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, *args, **kwargs):
            pass

    a1 = A()
    a2 = A()
    assert(a1 is a2)

