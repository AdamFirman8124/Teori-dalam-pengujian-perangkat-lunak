

# Generated at 2022-06-13 16:46:43.413337
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTester(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.index = 0

        def increase_index(self):
            self.index += 1

    # check the instance of SingletonTester is singleton
    assert id(SingletonTester()) == id(SingletonTester())

    # check the instance of SingletonTester is singleton
    st1 = SingletonTester()
    st2 = SingletonTester()
    st1.increase_index()
    assert st1.index == st2.index



# Generated at 2022-06-13 16:46:46.661906
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Class(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    a = Class(42)
    b = Class(0)
    assert a is b

# Generated at 2022-06-13 16:46:51.350670
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TmpClass(metaclass=Singleton):
        pass

    first = TmpClass()
    second = TmpClass()
    assert(id(first) == id(second))

# Generated at 2022-06-13 16:46:55.877570
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self, value):
            self.value = value

        def get_value(self):
            return self.value

    a = A(1)
    b = A(2)
    assert a.get_value() == 1
    assert b.get_value() == 1
    assert a is b

# Generated at 2022-06-13 16:47:00.612388
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Unit test for method __call__ of class Singleton"""
    class Test(metaclass=Singleton):
        def __init__(self, a=0, b=0):
            self.a = a
            self.b = b

    test1 = Test(1,2)
    test2 = Test()
    assert id(test1) == id(test2)
    assert test1.a == test2.a == 1
    assert test1.b == test2.b == 2



# Generated at 2022-06-13 16:47:03.143943
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    ts1 = TestSingleton()
    ts2 = TestSingleton()

    assert ts1 is ts2
    assert ts1 == ts2

# Generated at 2022-06-13 16:47:08.128839
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

    class Bar(object):
        __metaclass__ = Singleton

    f = Foo()
    f2 = Foo()
    b = Bar()
    assert (f is f2)
    assert (f is not b)



# Metaclass for classes that describe Ansible base objects.
# unit test for constructor of class AnsibleBase when init_with_kwargs = False


# Generated at 2022-06-13 16:47:14.673538
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSg(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.var = 42

    instance1 = TestSg()
    assert instance1.var == 42

    instance2 = TestSg()
    assert instance2.var == 42
    instance2.var = 1729
    assert instance1.var == 1729
    assert instance2.var == 1729

    assert id(instance1) == id(instance2)

# Generated at 2022-06-13 16:47:18.592829
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(metaclass=Singleton):
        def __init__(self):
            self.name = "Huawei"

    test = SingletonTest()
    print (test.name)
    test2 = SingletonTest()
    print (test2.name)

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:47:21.371960
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo():
        __metaclass__ = Singleton

    # Instantiate two Foo objects
    foo = Foo()
    bar = Foo()

    # Verify they are the same object
    assert(foo is bar)


# Generated at 2022-06-13 16:47:27.951349
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo:
        def __init__(self, foo):
            self.foo = foo

    class SingletonFoo(Foo):
        __metaclass__ = Singleton

    ret = SingletonFoo("hello")
    assert ret.foo == "hello"

    ret2 = SingletonFoo("world")
    assert ret2.foo == "hello"

# Generated at 2022-06-13 16:47:34.803725
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    a = A(1)

    # a1 and a2 should reference to the same object
    a1 = A(2)
    assert a1.value == 1
    assert id(a) == id(a1)

    a2 = A(3)
    assert a2.value == 1
    assert id(a) == id(a2)

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:47:40.183868
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, val):
            self.val = val

    a1 = A(1)
    a2 = A(2)
    assert a1.val == 1
    assert a2.val == 1



# Generated at 2022-06-13 16:47:46.875386
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, arg1):
            self.a = arg1

    obj1 = Test(1)
    obj2 = Test(2)
    obj3 = Test(3)
    assert(obj1 == obj2 == obj3)
    assert(obj1.a == 1)
    assert(obj2.a == 1)
    assert(obj3.a == 1)

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:47:48.649125
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()

    assert a is b

    class B(object):
        __metaclass__ = Singleton
        pass

    c = B()
    d = B()

    assert c is d

# Generated at 2022-06-13 16:47:54.168044
# Unit test for constructor of class Singleton
def test_Singleton():    
    class C(object):
        __metaclass__ = Singleton
        def __init__(self, num):
            # simulate an expensive constructor
            print("init %d" % num)
            from time import sleep
            sleep(num)

    # At most one instance will be created
    c1 = C(1)
    c2 = C(2)
    print("It's working!")
    assert c1 == c2


# Generated at 2022-06-13 16:47:57.595966
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    a = TestSingleton()
    b = TestSingleton()
    assert a == b



# Generated at 2022-06-13 16:48:00.213872
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, num):
            self.num = num

    assert Test(1) == Test(2)
    assert Test(1).num == 2

# Generated at 2022-06-13 16:48:01.536670
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(Singleton):
        def __init__(self):
            pass

    assert(TestClass is TestClass())

# Generated at 2022-06-13 16:48:08.948522
# Unit test for constructor of class Singleton
def test_Singleton():
    class_name = 'MyTestClass'

    class MyTestClass(Singleton):
        def __init__(cls):
            cls.name = class_name

    # call __init__ on the class, not singleton instance
    assert MyTestClass().name == class_name

    # check that singleton instance is created
    assert MyTestClass.__instance is not None

    # all instances are the same
    assert MyTestClass() is MyTestClass()

# Generated at 2022-06-13 16:48:16.494290
# Unit test for constructor of class Singleton
def test_Singleton():
    class foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass
        def bar(self):
            return 'bar'

    f1 = foo()
    f2 = foo()
    assert f1 is f2
    assert f1.bar() == 'bar'
    assert f2.bar() == 'bar'

if __name__ == '__main__':
    import sys
    import unittest

    class TestSingleton(unittest.TestCase):
        def test_constructor(self):
            test_Singleton()

    sys.exit(unittest.main())

# Generated at 2022-06-13 16:48:21.101786
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    s = TestSingleton()
    assert s.__class__.__instance is None

    s1 = TestSingleton()
    assert s1.__class__.__instance is s

# Generated at 2022-06-13 16:48:26.276732
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    # Each call should return the same instance
    f1 = Foo()
    f2 = Foo()
    assert f1 is f2

    # Check that Foo's constructor doesn't run
    assert not hasattr(Foo, "__init__")

# Generated at 2022-06-13 16:48:31.677283
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, arg1, arg2):
            self.a = arg1
            self.b = arg2
    
    a = A(2, 3)
    b = A(4, 5)
    assert a is b
    assert a.a == 2
    assert b.a == 2

# Generated at 2022-06-13 16:48:42.259182
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class One(object):
        __metaclass__ = Singleton
        value = 1

    one1 = One()
    one2 = One()

    assert(one1 == one2)
    assert(one1.value == one2.value)
    assert(id(one1) == id(one2))
    assert(id(one1) == id(One()))

    one2.value = 2
    assert(one1.value == 2)

    one1.value = 1
    assert(one1.value == one2.value)

    class Two(object):
        __metaclass__ = Singleton
        value = 2

    two1 = Two()
    two2 = Two()
    assert(two1 == two2)
    assert(two1.value == two2.value)

# Generated at 2022-06-13 16:48:45.935943
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self):
            self.count = 0

        def add(self):
            self.count += 1

    assert isinstance(A(), A)

# Test that Singleton can be a base class of another class

# Generated at 2022-06-13 16:48:48.298825
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = 'calvin'
    a1 = A()
    assert a1.name == 'calvin'
    a2 = A()
    assert a1 is a2

# Generated at 2022-06-13 16:48:51.387430
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, name):
            self.name = name
    foo = Foo('bar')
    assert id(foo) == id(Foo())



# Generated at 2022-06-13 16:48:56.999103
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.__val = 0

        def __set__(self, v):
            self.__val = v

        def __get__(self):
            return self.__val

    t0 = TestSingleton()
    t1 = TestSingleton()
    t0.__set__(12)
    assert t0.__get__() == t1.__get__()

# Generated at 2022-06-13 16:49:05.785281
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest

    from yaml.composer import Composer
    from yaml.parser import Parser

    ''' Unit tests for the Singleton metaclass __call__ method '''

    class TestObject(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.testval = 'testval'

    class TestObjectTwo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.testval = 'testval'

    class TestObjectThree(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.testval = 'testval'

    class singleton___call__Tests(unittest.TestCase):

        def setUp(self):
            self.parser = Parser()
           

# Generated at 2022-06-13 16:49:12.083454
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.module_utils.six import with_metaclass

    class SingletonC(with_metaclass(Singleton, object)):
        def __init__(self, value=None):
            self.value = value

    s = SingletonC(1)
    assert s.value == 1

    s = SingletonC(2)
    assert s.value == 1

# Generated at 2022-06-13 16:49:19.402329
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self, *args):
            self.args = args

    test_instance = TestClass()
    assert test_instance is TestClass()

    args = ('bar', 'baz')
    test_instance_args = TestClass(*args)
    assert test_instance_args is TestClass(*args)
    assert test_instance_args is Singleton.__call__(*args)
    assert test_instance_args is not test_instance
    assert test_instance_args.args == args
    assert test_instance.args != args
    assert test_instance.args == ()

# Generated at 2022-06-13 16:49:30.690174
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    print(">>Start test_Singleton___call__")
    class SingletonTestClass1(object):
        __metaclass__ = Singleton
        def __init__(self,a,b):
            self.a = a
            self.b = b


    class SingletonTestClass2(object):
        __metaclass__ = Singleton
        def __init__(self,a,b):
            self.a = a
            self.b = b

    t1 = SingletonTestClass1(a=1,b=1)
    t2 = SingletonTestClass1(a=2,b=2)
    print("t1==t2?", t1==t2)

    t3 = SingletonTestClass2(a=3,b=3)

# Generated at 2022-06-13 16:49:34.093482
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self):
            self.val = 3
    assert A().val == 3
    assert A().val == 3



# Generated at 2022-06-13 16:49:37.756395
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x

    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 is f2

    assert f1.x == f2.x

# Generated at 2022-06-13 16:49:42.550919
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = "foo"

    foo1 = Foo()
    # If __instance is None, then Foo() is called
    assert foo1.name == "foo"
    # Subsequent calls to Foo() return the same object
    foo2 = Foo()
    assert foo1 == foo2
    assert foo1 is foo2
    # Attributes of the object can be changed
    foo2.name = "bar"
    assert foo1.name == "bar"

# Generated at 2022-06-13 16:49:50.340131
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test:
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x

    # Create object for class Test
    t1 = Test(5)

    # Check whether new object t2 is same as object t1
    t2 = Test(7)
    assert t1 is t2
    assert t1.x == 7
    assert t2.x == 7
    # assert(False, "Test Failed")

# Remove this line to run the unit test
test_Singleton()

# Generated at 2022-06-13 16:49:56.696269
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    global counter
    counter = 0

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, n):
            global counter
            counter += n

    obj1 = TestSingleton(1)
    obj2 = TestSingleton(2)
    assert counter == 1, "Singleton has been initialized more than once"



# Generated at 2022-06-13 16:49:59.841094
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    assert(foo1 is foo2)



# Generated at 2022-06-13 16:50:05.028863
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, val):
            self.val = val
    t1 = Test(1)
    t2 = Test(2)
    print(t1.val)
    print(t2.val)
    assert t1 == t2
    assert t1.val == 1
    assert t2.val == 1

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:50:17.188901
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, name):
            self.name = name

    def worker():
        counter = dict()
        name = 'worker'
        for i in range(100):
            p = Test(name)
            counter[p.name] = counter.get(p.name, 0) + 1

            if p.name not in counter:
                counter[p.name] = 1
            else:
                counter[p.name] += 1
            assert(counter[p.name] == 1), counter

    import threading
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=worker))

    for t in threads:
        t.start()

    for t in threads:
        t.join()



# Generated at 2022-06-13 16:50:24.759226
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import multiprocessing
    counter = 0
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            nonlocal counter
            counter += 1
    process_1 = multiprocessing.Process(target=TestSingleton)
    process_2 = multiprocessing.Process(target=TestSingleton)
    process_1.start()
    process_2.start()
    process_1.join()
    process_2.join()
    assert counter == 1

# Generated at 2022-06-13 16:50:30.417659
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import pytest

    class TestClass(metaclass=Singleton):
        """Test class for method __call__ of class Singleton."""
        def __init__(self):
            self.count = 0

        def inc(self):
            self.count += 1

    t1 = TestClass()
    t1.inc()
    t2 = TestClass()

    assert t1 is t2
    assert t1.count == t2.count == 1


# Test class for method __call__ of class Singleton

# Generated at 2022-06-13 16:50:31.850842
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

# Generated at 2022-06-13 16:50:36.397494
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 10

    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2

    foo1.value = 100
    assert foo2.value == 100

# Generated at 2022-06-13 16:50:37.958573
# Unit test for constructor of class Singleton
def test_Singleton():
  import doctest
  failedTestCount, _ = doctest.testmod()
  assert failedTestCount == 0

# Generated at 2022-06-13 16:50:40.403368
# Unit test for constructor of class Singleton
def test_Singleton():

    class A(object):
        __metaclass__ = Singleton

    class B(A):
        pass

    a = A()
    b = B()
    assert id(a) == id(b)

# Generated at 2022-06-13 16:50:46.326445
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Class(object):
        __metaclass__ = Singleton
        def __init__(self, p1, p2):
            self.p1 = p1
            self.p2 = p2

    o1 = Class(1, 2)
    o2 = Class(2, 3)

    assert o1 is o2
    assert o1.p1 == 1
    assert o1.p2 == 2
    assert o2.p1 == 1
    assert o2.p2 == 2


if __name__ == '__main__':
    from unittest import main
    main()

# Generated at 2022-06-13 16:50:48.700270
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton:
        __metaclass__ = Singleton

    assert id(TestSingleton()) == id(TestSingleton())

# Generated at 2022-06-13 16:50:51.620981
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.foo = 1

    x = Foo()
    y = Foo()
    assert x is y
    assert x.foo is y.foo
    assert x.foo == 1


# Generated at 2022-06-13 16:50:58.642194
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    t1 = Test()
    assert t1 is Test()

# Generated at 2022-06-13 16:51:05.817732
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingletonA(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

    class TestSingletonB(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

    a = TestSingletonA('singleton_a')
    b = TestSingletonB('singleton_b')
    assert a == TestSingletonA('singleton_a')
    assert a == TestSingletonA('another_a')
    assert b == TestSingletonB('singleton_b')
    assert b == TestSingletonB('another_b')
    assert a != b

# Generated at 2022-06-13 16:51:11.672575
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # test class
    class A(metaclass=Singleton):
        pass

    # Before the first instantiation, the attribute __instance is set to None
    assert A.__instance is None

    # After the first instantiation, attribute __instance is set to an instance object
    # and the value of __instance is returned in subsequent instantiations
    assert id(A()) == id(A())


# Generated at 2022-06-13 16:51:18.410943
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        pass

    class B(metaclass=Singleton):
        pass

    assert id(A()) == id(A())  # pylint: disable=protected-access
    assert id(B()) == id(B())  # pylint: disable=protected-access

    assert id(A()) != id(B())  # pylint: disable=protected-access

# Generated at 2022-06-13 16:51:22.356236
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.plugins.loader import AnsiblePluginLoader

    # Instance of class AnsiblePluginLoader
    plugin_loader = AnsiblePluginLoader()

    # Instance of class AnsiblePluginLoader
    plugin_loader_2 = AnsiblePluginLoader()

    # Assert
    assert plugin_loader == plugin_loader_2
    assert id(plugin_loader) == id(plugin_loader_2)

# Generated at 2022-06-13 16:51:29.488317
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = None

        def set_a(self, a):
            self.a = a

    a = A()
    a.set_a(1)
    b = A()
    assert a.a == b.a == 1

    b.set_a(2)
    assert a.a == b.a == 2



# Generated at 2022-06-13 16:51:33.413548
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        pass
    # The first instantiation will work
    s1 = TestSingleton()
    # The second will be ignored
    s2 = TestSingleton()
    # Verify that s1 and s2 are the same
    assert s1 is s2

# Generated at 2022-06-13 16:51:40.871308
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import sys
    import io

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name
            self.fd = io.StringIO()

        def write(self, s):
            self.fd.write(s)

        def getout(self):
            return self.fd.getvalue()

        def getname(self):
            return self.name

    # Overwrite stdout and stderr
    sys.stdout = TestSingleton('stdout')
    sys.stderr = TestSingleton('stderr')

    assert sys.stderr.getname() == 'stderr'
    assert sys.stdout.getname() == 'stdout'

    # Write stdout and stderr
    import __main__
   

# Generated at 2022-06-13 16:51:43.452217
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    a = TestSingleton()
    b = TestSingleton()


# Generated at 2022-06-13 16:51:46.434288
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    assert a is A()

    class B(object):
        __metaclass__ = Singleton

    b = B()
    assert b is B()
    assert b is not A()

# Generated at 2022-06-13 16:52:02.363768
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, foo=None):
            self.foo = foo
    a1 = A('Foo')
    a2 = A('Bar')
    assert(a1 is a2)
    assert(a1.foo==a2.foo)

    class B(object):
        __metaclass__ = Singleton
        def __init__(self, foo=None):
            self.foo = foo
    b = B('Bar')
    assert(b is not a1)
    assert(b.foo is not a1.foo)


# Generated at 2022-06-13 16:52:06.988640
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    '''It's a test'''
    class SingletonTest(object):
        '''It's a Singleton'''
        __metaclass__ = Singleton

        def __init__(self):
            '''It's a __init__'''
            self.name = 'Instance'

        def echo(self, message):
            '''It's a test echo method'''
            return message

    assert SingletonTest() is SingletonTest()
    assert SingletonTest().echo('Hello world') == 'Hello world'

# Generated at 2022-06-13 16:52:12.313765
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest

    class SingletonTest(object):
        __metaclass__ = Singleton

    class TestSingleton(unittest.TestCase):

        def test_Singleton(self):
            s1 = SingletonTest()
            s2 = SingletonTest()
            self.assertTrue(s1 is s2)

    __unittest = unittest.main(exit=False)

# Generated at 2022-06-13 16:52:16.426188
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self):
            pass

    class B(metaclass=Singleton):
        def __init__(self):
            pass

    assert A() is A()
    assert B() is B()
    assert A() is not B()

# Generated at 2022-06-13 16:52:20.290416
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

    a = MySingleton(1)
    assert a.x == 1
    b = MySingleton(2)
    assert a is b
    assert b.x == 1
    b.x = 3
    assert a.x == b.x

# Generated at 2022-06-13 16:52:23.413971
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(metaclass=Singleton):
        def __init__(self, args=None, kwargs=None):
            self.args = args
            self.kwargs = kwargs

    assert TestSingleton('args', kwargs='kwargs') == TestSingleton()
    assert TestSingleton.__instance.args == 'args'
    assert TestSingleton.__instance.kwargs == 'kwargs'

# Generated at 2022-06-13 16:52:30.437471
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class X(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1
            self.b = 2
    # Should return new instance
    assert(X() != X.__instance)
    # Should return last instance
    assert(X() == X.__instance)
    # Test members of instance
    instance = X()
    assert(instance.a == 1)
    assert(instance.b == 2)


# Generated at 2022-06-13 16:52:34.000263
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    assert a1 is A()


# Generated at 2022-06-13 16:52:36.716813
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object): pass

    instance1 = A()
    instance2 = A()

    assert id(instance1) == id(instance2)

#Unit test for using class Singleton

# Generated at 2022-06-13 16:52:44.953806
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        def __init__(self, some_param):
            self.some_param = some_param
    class TestSingleton(Test):
        __metaclass__ = Singleton
        def __init__(self, some_param):
            super(TestSingleton, self).__init__(some_param)

    assert TestSingleton(1).some_param == 1
    assert TestSingleton(2).some_param == 1
    assert TestSingleton(3).some_param == 1

    test = Test(1)
    test_s = TestSingleton(2)
    assert test.some_param == 1
    assert test_s.some_param == 1


# vim: set fileencoding=utf-8 :

# Generated at 2022-06-13 16:52:59.510932
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        def __init__(self, id):
            self.id = id

    test_object1 = TestClass(id=1)
    test_object2 = TestClass(id=2)

    class MockClass:
        def __init__(self):
            pass

    with MockClass():
        assert id(test_object1) == id(test_object2)
        test_object3 = TestClass(id=3)
        assert id(test_object1) == id(test_object3)


# Generated at 2022-06-13 16:53:06.084657
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.count = 0

        def add(self):
            self.count += 1

    # Creating instances
    t1 = Test()
    t2 = Test()

    # Checking if they are the same
    assert t1 is t2

    # Changing member data
    t1.add()
    assert t1.count == 1
    assert t2.count == 1

# Generated at 2022-06-13 16:53:11.517696
# Unit test for constructor of class Singleton
def test_Singleton():
    from pytest import raises

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, value=None):
            self.value = value

    t1 = TestSingleton(1)
    t2 = TestSingleton(2)
    assert t1 is t2
    assert t1.value == 1
    t3 = TestSingleton(3)
    assert t2 is t3
    assert t2.value == 1



# Generated at 2022-06-13 16:53:15.488661
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x
    a = A(10)
    assert(a.x == 10)
    b = A(20)
    assert(a.x == 10 and a == b)



# Generated at 2022-06-13 16:53:18.475029
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton
    obj1 = SingletonTest()
    obj2 = SingletonTest()
    assert obj1 is obj2


# Generated at 2022-06-13 16:53:25.724829
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest2 as unittest

    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, foo='foo'):
            self.foo = foo

    class TestFooSingleton(unittest.TestCase):

        def test_instance_exists(self):
            foo1 = Foo('bar')
            foo2 = Foo()
            self.assertTrue(foo1 is foo2)
            self.assertEqual('bar', foo1.foo, "foo1 should have been set to 'bar'")
            self.assertEqual('bar', foo2.foo, "foo2 should have been set to 'bar'")

    unittest.main()


if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:53:28.057968
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest:
        __metaclass__ = Singleton

    # Test constructor
    singleton1 = SingletonTest()
    singleton2 = SingletonTest()
    assert(singleton1 == singleton2)
    assert(singleton1 is singleton2)

# Generated at 2022-06-13 16:53:30.484998
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    foo3 = Foo()
    assert foo1 is foo2 is foo3

# Generated at 2022-06-13 16:53:37.088015
# Unit test for constructor of class Singleton
def test_Singleton():
    from ansible.module_utils.facts.system.distribution import DistributionFactCollector
    from ansible.module_utils.facts.system import DistributionFactRetriever
    from ansible.module_utils.facts.system import DistributionSingleton
    from ansible.module_utils.facts.system import LinuxDistribution
    from ansible.module_utils.facts.system import PlatformFactCollector
    from ansible.module_utils.facts.system import PlatformFactRetriever
    from ansible.module_utils.facts.system import PlatformSingleton
    from ansible.module_utils.facts.system import NetworkFactsCollector
    from ansible.module_utils.facts.system import NetworkFactsRetriever
    from ansible.module_utils.facts.system import NetworkSingleton
    from ansible.module_utils.facts.system import HWF

# Generated at 2022-06-13 16:53:43.389620
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 42

        def get_x(self):
            return self.x

    foo = Foo()
    assert foo.x == 42

    bar = Foo()
    assert bar.x == 42

    assert foo == bar and foo is bar

    assert foo.get_x() == 42

# Generated at 2022-06-13 16:53:59.719179
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(metaclass=Singleton):
        def __init__(self, arg):
            self.arg = arg
    assert Singleton.__instance is None
    ts1 = TestSingleton(1)
    assert Singleton.__instance is ts1
    ts2 = TestSingleton(3)
    assert Singleton.__instance is ts1

# Generated at 2022-06-13 16:54:09.568961
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from collections import Counter

    from six import add_metaclass

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.counter = Counter()
            self.counter['__init__'] += 1

        def add(self, a, b):
            self.counter['add'] += 1
            return a + b

        def multiply(self, a, b):
            self.counter['multiply'] += 1
            return a * b

    t1 = TestSingleton()
    t2 = TestSingleton()

    assert t1 is t2
    assert {'__init__': 1, 'add': 0, 'multiply': 0} == t1.counter
    assert {'__init__': 1, 'add': 0, 'multiply': 0} == t1

# Generated at 2022-06-13 16:54:12.446253
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(metaclass=Singleton):
        pass
    foo_1 = Foo()
    foo_2 = Foo()
    assert foo_1 is foo_2


# Generated at 2022-06-13 16:54:17.222818
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(metaclass=Singleton):
        def __init__(self, x):
            self.x = x

    # Initialize an instance of class Foo and make it Singleton
    f = Foo(42)

    # Initialize another instance of class Foo and make it Singleton
    f2 = Foo(42)

    # Verify that the singleton is working -- f2 is same instance as f
    ae_test.assert_equal(f is f2, True, "Singleton constructor returned new instance.")


# Generated at 2022-06-13 16:54:19.758028
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    # Check that A is a subclass of Singleton
    assert issubclass(A, Singleton) is True

    a1 = A()
    a2 = A()
    assert a1 is a2

# Generated at 2022-06-13 16:54:21.556000
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Unit test for method __call__ of class Singleton."""
    assert Singleton.__call__("test", 1,2) == None


# Generated at 2022-06-13 16:54:23.509622
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert id(a1) == id(a2)

# Generated at 2022-06-13 16:54:28.317509
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Test case 1: no instance created yet
    class A(object):
        __metaclass__ = Singleton

    a = A()
    assert(isinstance(a, A))
    # Test case 2: instance has been instantiated in previous call
    b = A()
    assert(isinstance(a, A))
    assert(b == a)

# Generated at 2022-06-13 16:54:30.007177
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert a1 is a2

# Generated at 2022-06-13 16:54:37.166497
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from twill import commands
    from twill import browser
    from twill.browser import TwillBrowser

    assert isinstance(TwillBrowser(), browser.BrowserState)
    assert isinstance(TwillBrowser(), commands.StateInterface)

    # Verify that all the function exist in browser.BrowserState

# Generated at 2022-06-13 16:55:00.284007
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

    a = MySingleton('a')
    b = MySingleton('b')

    assert(a is b)


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:55:04.773646
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object, metaclass=Singleton):
        def __init__(self, a):
            self.a = a

    class B(object, metaclass=Singleton):
        def __init__(self, b):
            self.b = b

    a = A(3)
    a1 = A("hello")

    assert a == a1

    b = B("world")
    b1 = B("world")

    assert b == b1

    assert a != b


if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:55:06.106029
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert(a is b)



# Generated at 2022-06-13 16:55:06.959291
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    assert id(Singleton()) == id(Singleton())


# Generated at 2022-06-13 16:55:08.385002
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
    a1 = A()
    a2 = A()
    assert a1 is a2


# Generated at 2022-06-13 16:55:16.296084
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    def test_func(**kw):
        if s:
            return s

        s = SingletonFoo(**kw)
        return s

    assert test_func() is test_func()
    s = None

    assert test_func(x=1) is test_func(x=1)
    s = None

    assert test_func(x=2) is not test_func(x=1)
    s = None

    assert test_func(y=1) is not test_func(x=1)
    s = None

from ansible.module_utils.six import with_metaclass

# Singleton class Unit test

# Generated at 2022-06-13 16:55:26.003374
# Unit test for constructor of class Singleton
def test_Singleton():
    import types

    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self, a=0):
            self.a = a
            self.b = 0
            self.c = 0

        def __str__(self):
            return "Singleton(%s, %s, %s)" % (self.a, self.b, self.c)

        def __eq__(self, other):
            if not type(self) == type(other):
                return False
            if self.a != other.a:
                return False
            if self.b != other.b:
                return False
            if self.c != other.c:
                return False
            return True

        def __hash__(self):
            return hash(str(self))

    # Test default constructor
    single

# Generated at 2022-06-13 16:55:29.471068
# Unit test for constructor of class Singleton
def test_Singleton():
    # noinspection PyUnusedLocal,PyPep8Naming
    class A(metaclass=Singleton):
        def __init__(self):
            self.a = 1

    # noinspection PyStatementEffect
    A()
    # noinspection PyStatementEffect
    A()


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:55:32.615190
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2
test_Singleton___call__()

# Generated at 2022-06-13 16:55:35.738319
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object, metaclass=Singleton):
        pass

    a = TestClass()
    b = TestClass()
    assert a is b
    print('test_Singleton: ok')


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:56:21.234669
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, **kw):
            self.__dict__.update(kw)

    t1 = Test(foo='bar')
    t2 = Test(bar='baz')
    assert t1 is t2
    assert t1.foo == t2.foo
    assert t1.bar == t2.bar



# Generated at 2022-06-13 16:56:27.146674
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 0

    a = TestClass()
    b = TestClass()

    assert a is b
    assert a.value == 0
    assert b.value == 0

    a.value = 1

    assert a.value == 1
    assert b.value == 1

    b.value = 2

    assert a.value == 2
    assert b.value == 2

if __name__ == '__main__':
    test_Singleton___call__()
    print('OK')

# Generated at 2022-06-13 16:56:28.222095
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(metaclass=Singleton):
        pass
    MyClass()

# Generated at 2022-06-13 16:56:33.340044
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Define the class to test
    class SingletonTestClass(object):
        __metaclass__ = Singleton

    # Instance the class and verify the returned object is the singleton instance
    singleton_test_class1 = SingletonTestClass()
    assert singleton_test_class1 == SingletonTestClass()