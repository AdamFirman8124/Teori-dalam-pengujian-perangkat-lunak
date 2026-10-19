

# Generated at 2022-06-13 16:46:36.036697
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        foo = 1

        def __init__(self):
            self.foo = None

        def setFoo(self, foo):
            self.foo = foo

    # Only one instance of Foo
    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2
    # foo1.foo is None
    assert foo1.foo == foo2.foo

    # Set foo to 1 through foo1
    foo1.setFoo(1)
    # foo2.foo should also be 1
    assert foo2.foo == 1

# Generated at 2022-06-13 16:46:47.405338
# Unit test for constructor of class Singleton
def test_Singleton():
    # import modules for unit test
    import random

    # define class
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

        def result(self):
            return self.x

    # create an instance of SingletonTest1
    instance1 = SingletonTest(1234)
    # create another instance of SingletonTest
    instance2 = SingletonTest(5678)

    # check if these two instances are the same
    assert id(instance1) == id(instance2)

    # read instance1.x and instance2.x
    print("instance1.x =", instance1.x)
    print("instance2.x =", instance2.x)

    # update instance1.x and instance2.x

# Generated at 2022-06-13 16:46:49.457961
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton
        val = 0

    obj1 = TestClass()
    obj2 = TestClass()

    assert obj1 is obj2

    obj1.val += 1
    assert obj2.val == 1

if __name__ == '__main__':
    import pytest

    pytest.main(['-xrf'])

# Generated at 2022-06-13 16:46:52.403155
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    class TestSingleton2(object):
        __metaclass__ = Singleton

    assert TestSingleton() is TestSingleton()
    assert TestSingleton() is not TestSingleton2()

# Generated at 2022-06-13 16:46:55.577284
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object):
        __metaclass__ = Singleton

    s1 = S()
    s2 = S()
    s3 = S()
    assert id(s1) == id(s2) == id(s3)

# Generated at 2022-06-13 16:46:58.285132
# Unit test for constructor of class Singleton
def test_Singleton():
    class testClass:
        __metaclass__ = Singleton

        def __init__(self, val):
            self.val = val

    c1 = testClass(1)
    c2 = testClass(2)
    c1.val = 2
    assert c1.val == c2.val


# Meta Singleton

# Generated at 2022-06-13 16:46:59.984319
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    a = A()
    assert id(a) == id(A())

# Generated at 2022-06-13 16:47:05.677075
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        """Test class for class Singleton"""
        __metaclass__ = Singleton

        def __init__(self, A, B):
            self.A = A
            self.B = B

    T1 = TestClass(10, 20)

    assert T1.A == 10
    assert T1.B == 20
    assert T1.A == TestClass(30, 40).A
    assert T1.B == TestClass(30, 40).B

# Generated at 2022-06-13 16:47:08.865900
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()

    assert foo1 is foo2


# Generated at 2022-06-13 16:47:13.029994
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
    s = TestSingleton()
    return True

if __name__ == '__main__':
    if test_Singleton():
        print("Unit Test is successful.")
    else:
        print("Unit Test is failed.")

# Generated at 2022-06-13 16:47:23.228055
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(metaclass=Singleton):
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    class Test2(metaclass=Singleton):
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    t1 = Test('Hello', 'World')
    t2 = Test('Goodbye', [1, 2, 3])

    assert t1 is t2
    assert t1.arg1 == 'Goodbye'
    assert t2.arg2 == [1, 2, 3]

    t3 = Test2('Hello', 'World')
    t4 = Test2('Goodbye', [1, 2, 3])

    assert t3 is t4
    assert t

# Generated at 2022-06-13 16:47:27.536943
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object, metaclass=Singleton):
        def __init__(self):
            self.a = 'a'

    a = A()
    b = A()
    assert a is b
    assert a.a == b.a
    a.a = 'b'
    assert a.a == b.a


# Generated at 2022-06-13 16:47:30.325026
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class SingletonTest(object):
        __metaclass__ = Singleton

    assert id(SingletonTest()) == id(SingletonTest())

# Test the custom metaclass Singleton

# Generated at 2022-06-13 16:47:32.534104
# Unit test for constructor of class Singleton
def test_Singleton():
    class _TestSingleton(metaclass=Singleton):
        pass
    assert(_TestSingleton() is _TestSingleton())

# Generated at 2022-06-13 16:47:37.413209
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 0

    o1 = Singleton.__call__(Foo)
    o2 = Singleton.__call__(Foo)
    o1.x += 1
    o3 = Singleton.__call__(Foo)
    assert o1 == o2 and o2 == o3
    assert o1.x == 2



# Generated at 2022-06-13 16:47:44.122817
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class A(object):
        __metaclass__ = Singleton

    class B(object):
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

    a1 = A()
    a2 = A()
    assert a1 == a2
    assert A() == a2

    b1 = B('1')
    b2 = B('2')
    assert b1 == b2
    assert b1.x == '1'

# Generated at 2022-06-13 16:47:49.304400
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton

    t1 = TestClass()
    t2 = TestClass()
    assert t1 == t2

    class TestSubclass(TestClass):
        pass
    t3 = TestSubclass()
    assert t1 == t2 == t3

# Generated at 2022-06-13 16:47:52.713016
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass
    a_1 = A()
    a_2 = A()
    assert a_1 is a_2



# Generated at 2022-06-13 16:48:03.016864
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import os
    import tempfile
    def my_test_class(cls):
        class MyClass(object):
            __metaclass__ = cls
            def __init__(self, prefix=None):
                if prefix is None:
                    self.prefix = tempfile.mkdtemp()
                else:
                    self.prefix = prefix

            def get_file(self, name):
                return os.path.join(self.prefix, name)
        return MyClass

    MyClass = my_test_class(Singleton)
    x = MyClass()

    f1 = x.get_file('foobar.txt')
    os.mknod(f1)

    y = MyClass()
    f2 = y.get_file('foobar.txt')
    assert(f1 == f2)

    y_prefix

# Generated at 2022-06-13 16:48:06.017206
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    assert Singleton.__call__ is not type.__call__
    assert Singleton.__call__.__doc__ == "Metaclass for classes that wish to implement Singleton\n\tfuntionality.  If an instance of the class exists, it's returned,\n\totherwise a single instance is instantiated and returned.\n\t"


# Generated at 2022-06-13 16:48:11.929888
# Unit test for constructor of class Singleton
def test_Singleton():
    class test(metaclass=Singleton):
        def __init__(self, i):
            self.num = i
            self.name = 'test'

    t1 = test(1)
    t2 = test(2)

    assert t1 == t2
    assert t1.num == 1

# Generated at 2022-06-13 16:48:15.492650
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    assert isinstance(TestSingleton(), TestSingleton)
    assert isinstance(TestSingleton(), TestSingleton)

# Generated at 2022-06-13 16:48:20.310606
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class One(object):
        __metaclass__ = Singleton

    class Two(One):
        pass

    class Three(One):
        pass

    one = One()
    two = Two()
    three = Three()

    assert one is two is three


# Generated at 2022-06-13 16:48:31.677408
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """This test how the metaclass Singleton works
    """
    from unittest import TestCase
    from collections import namedtuple

    class singleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = "singleton"

    class singleton_instance(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = "singleton_instance"

    class MyTestCase(TestCase):
        def test_singleton(self):
            s1 = singleton()
            s2 = singleton()
            self.assertIs(s1, s2)

        def test_singleton_instance(self):
            s1 = singleton_instance()
            s2 = singleton_instance()

# Generated at 2022-06-13 16:48:38.924196
# Unit test for constructor of class Singleton
def test_Singleton():
    # Create a dictionary to simulate locals()
    test_dict = {}
    # create a new Singleton instance
    test_singleton = Singleton('test_Singleton', (object,), test_dict)
    # Execute the constructor of test_Singleton
    test_singleton('testName', (object,), test_dict)
    print(test_singleton.__instance)
    # test_singleton is an instance of class Singleton
    assert isinstance(test_singleton, Singleton)

# Generated at 2022-06-13 16:48:41.181340
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, *args, **kw):
            pass

    assert isinstance(Test(), Test)

# Generated at 2022-06-13 16:48:43.840758
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from .memory import MemoryConnection
    conn = MemoryConnection('test_host', 1, 2)
    assert conn is MemoryConnection('test_host', 1, 2)
    assert conn is MemoryConnection('test_host', 1, 2)



# Generated at 2022-06-13 16:48:45.234785
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton


# Generated at 2022-06-13 16:48:49.167469
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    assert Foo() == Foo()


from ansible.module_utils.six.moves import queue
from ansible.module_utils._text import to_bytes, to_text



# Generated at 2022-06-13 16:48:52.548308
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    assert Test() is Test()
    # now make sure the class that is returned is the class we expect it to be
    assert Test() is Test


# Generated at 2022-06-13 16:49:00.797266
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a

    obj_1 = A(1)
    obj_2 = A(2)
    assert obj_1.a == 1
    assert obj_2.a == 1
    assert obj_1 is obj_2

# Generated at 2022-06-13 16:49:08.970416
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    # Instantiate the class singleton
    foo = Foo('a')
    assert(foo.value == 'a')

    # Instantiate the class singleton and assert that the same instance is returned
    # and that the previous property value is still there.
    foo = Foo('b')
    assert(foo.value == 'a')

# Generated at 2022-06-13 16:49:10.273602
# Unit test for constructor of class Singleton
def test_Singleton():

    class Singleton(metaclass=Singleton):
        def __init__(self):
            pass

    a = Singleton()
    b = Singleton()
    assert(a is b)

# Generated at 2022-06-13 16:49:14.275986
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo:
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 'X'

    # call Singleton's __call__ method
    # (the Singleton method will call Foo's __init__ method)
    foo1 = Foo()
    foo2 = Foo()

    assert foo1 is foo2
    assert foo1.x == 'X'
    assert foo2.x == 'X'

# Generated at 2022-06-13 16:49:17.671890
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1

    a1 = A()
    a2 = A()
    assert(a1 is a2)
    assert(a1.a == a2.a)

# Generated at 2022-06-13 16:49:21.265985
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

    assert(isinstance(MySingleton(), MySingleton))


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:49:24.012682
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self, a=100):
            self.a = a

    a1 = A(10)
    assert a1.a == 10
    a2 = A(20)
    assert a1 == a2
    assert a1.a == a2.a == a1.a == 10



# Generated at 2022-06-13 16:49:28.443493
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo:
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 1

    foo1 = Foo()
    foo2 = Foo()

    assert foo1.x == 1
    foo1.x = 2
    assert foo2.x == 2

# Generated at 2022-06-13 16:49:32.695961
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, num=0, str=""):
            self.num=num
            self.str=str

    tc1 = TestClass(1, "1");
    tc2 = TestClass();
    assert(tc1.num == tc2.num)
    assert(tc1.str == tc2.str)

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:49:38.318197
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    with open('.test_Singleton___call__', 'w') as f:
        pass
    import os
    assert isinstance(Singleton(__file__)(), Singleton(__file__)())
    assert Singleton(__file__)().name == Singleton(__file__)().name
    assert Singleton(__file__)().name == os.path.realpath('.test_Singleton___call__')
    os.remove('.test_Singleton___call__')


# Generated at 2022-06-13 16:49:51.212360
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, num):
            self.num = num

    num = 20170525
    a = Test(num)
    b = Test(num)
    assert(a is b)
    assert(a.num == num and a.num == b.num)


# Generated at 2022-06-13 16:50:02.813444
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import os
    import tempfile

    tmpdir = tempfile.mkdtemp()

    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.filename = None
            self.handle = None

        def init_file(self, filename):
            self.filename = os.path.join(tmpdir, filename)
            self.handle = open(self.filename, 'w')

        def write_to_file(self, content):
            self.handle.write(content)

        def close_file(self):
            if self.handle:
                self.handle.close()

    def test_write_to_file():
        singleton_1 = MySingleton()
        singleton_2 = MySingleton()


# Generated at 2022-06-13 16:50:06.721747
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = 'TestSingleton'
    test_singleton1 = TestSingleton()
    test_singleton2 = TestSingleton()
    assert test_singleton1 is test_singleton2


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:50:14.774074
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton
        def __init__(self, a=1, b=2):
            self.a = a
            self.b = b
            print(self.a, self.b)

    obj1 = MySingleton(10, 20)
    obj2 = MySingleton(100, 200)
    print(obj1.a, obj1.b) # 10 20
    print(obj2.a, obj2.b) # 10 20

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:50:22.213419
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object, metaclass=Singleton):
        pass

    class B(object, metaclass=Singleton):
        pass

    a = A()
    b = B()

    assert a is A(), 'Calling singleton class should return the same instance'
    assert a != b and b != A() and b != a, \
        'Calling two different classes should return diffent instances'
    assert b is B(), 'Calling singleton class should return the same instance'

# Generated at 2022-06-13 16:50:27.794381
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            self.arg = arg

    s1 = SingletonTest(1)
    s2 = SingletonTest(2)
    assert s1 is s2
    assert s1.arg == 1


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:50:33.223748
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    # Check that multiple instances of the same class don't get created
    instance1 = SingletonTestClass()
    instance2 = SingletonTestClass()
    assert instance1 is instance2

# Generated at 2022-06-13 16:50:38.035117
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

    a = MySingleton()
    b = MySingleton()
    assert a is b


# The following example is equivalent to the code above.
# class MyClass(object):
#     __metaclass__ = Singleton


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:50:42.603227
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        """Class for testing __call__ of class Singleton"""
        __metaclass__ = Singleton
        def __init__(self):
            self.obj = 'test'

    s_obj1 = Test()
    assert(s_obj1.obj == 'test')
    s_obj2 = Test()
    assert(s_obj2.obj == 'test')
    assert(s_obj1 is s_obj2)

# Generated at 2022-06-13 16:50:44.374671
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    assert Test() is Test()
    assert Test() is not None

# Generated at 2022-06-13 16:51:03.271257
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test:
        __metaclass__ = Singleton

    test1 = Test()
    test2 = Test()

    assert test1 == test2



# Generated at 2022-06-13 16:51:08.813827
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    obj = TestClass(42)
    assert obj.value == 42
    assert id(obj) == id(TestClass(43))

# Generated at 2022-06-13 16:51:10.833398
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

    assert Foo() is Foo()

# Generated at 2022-06-13 16:51:18.859938
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, a, b):
            self.a = a
            self.b = b

    a = TestSingleton(1, 2)
    assert a.a == 1
    assert a.b == 2
    b = TestSingleton(3, 4)
    assert a.a == 1
    assert a.b == 2
    assert b.a == 1
    assert b.b == 2
    assert a is b

# Generated at 2022-06-13 16:51:22.806572
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonSubClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 1
    a = SingletonSubClass()
    b = SingletonSubClass()
    a.x = 2

# Generated at 2022-06-13 16:51:28.286146
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test = "init"

    ts1 = TestSingleton()
    assert ts1.test == "init"
    ts2 = TestSingleton()
    assert ts1 is ts2

# Generated at 2022-06-13 16:51:31.431313
# Unit test for constructor of class Singleton
def test_Singleton():
  class _TestSingleton(object):
    __metaclass__ = Singleton

  assert _TestSingleton() == _TestSingleton()
  assert _TestSingleton() is _TestSingleton()

# Generated at 2022-06-13 16:51:38.726622
# Unit test for constructor of class Singleton
def test_Singleton():
    from ansible import constants as C

    class TestSingleton(object):
        __metaclass__ = Singleton

    class TestSingleton2(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.some_attribute = "test"

    # First call should set the reference
    ts1 = TestSingleton()
    ts2 = TestSingleton2()

    assert ts1 == ts2
    assert ts1 is ts2

    # Second call should return the first reference
    ts3 = TestSingleton()
    ts4 = TestSingleton2()

    assert ts3 == ts4
    assert ts3 is ts4

    assert ts1 == ts3
    assert ts1 is ts3



# Generated at 2022-06-13 16:51:42.426853
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingletonClass(object):
        __metaclass__ = Singleton

    singleton_instance_1 = MySingletonClass()
    singleton_instance_2 = MySingletonClass()
    assert singleton_instance_1 is singleton_instance_2



# Generated at 2022-06-13 16:51:45.440863
# Unit test for constructor of class Singleton
def test_Singleton():
    class tester(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.i = 0

    t1 = tester()
    t1.i = 1

    t2 = tester()
    assert t2.i == 1

# Generated at 2022-06-13 16:52:20.145538
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

    assert MyClass() == MyClass()
    assert id(MyClass()) == id(MyClass())

# Generated at 2022-06-13 16:52:23.278495
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = "I'm a singleton"

        def get_value(self):
            return self.value

    def get_value():
        return MyClass().get_value()

    print(get_value())

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:52:28.032916
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self, *args, **kw):
            self.args = args
            self.kw = kw

    a = TestSingleton(1, 2, 3, a=1, b=2, c=3)
    b = TestSingleton(4, 5, 6, d=4, e=5, f=6)
    assert a == b
    assert a.args == (1, 2, 3)
    assert a.kw == {'a': 1, 'b': 2, 'c': 3}
    assert b.args == (1, 2, 3)
    assert b.kw == {'a': 1, 'b': 2, 'c': 3}


# Generated at 2022-06-13 16:52:33.532838
# Unit test for constructor of class Singleton
def test_Singleton():
    print("Unit test for constructor of class Singleton")
    from ansible_collections.sensu.sensu_go.plugins.module_utils.common.text.converters import to_text

    class A(metaclass=Singleton):
        def __init__(self, a):
            self.a = a

        def __str__(self):
            return to_text(self.a)

    a = A("aaaa")
    b = A("bbbb")
    print("a: %s, b: %s" % (a, b))
    assert a == b

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:52:41.356288
# Unit test for constructor of class Singleton
def test_Singleton():
    from nose_parameterized import parameterized
    from .test_utils import get_testcases_from_data_json

    testcases_data = get_testcases_from_data_json('try_conjur_singleton.json')

    for testcase_data in testcases_data:
        yield run_test_Singleton, testcase_data

    try:
        import pytest
        @pytest.mark.parametrize(
            'testcase_data',
            testcases_data,
            ids=[testcase_data['id'] for testcase_data in testcases_data]
        )
        def test_Singleton_pytest(testcase_data):
            run_test_Singleton(testcase_data)
    except ImportError:
        pass


# Generated at 2022-06-13 16:52:47.944801
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(metaclass=Singleton):

        def __init__(self, x=0):
            self.x = x

    o1 = MySingleton()
    o2 = MySingleton()
    o3 = MySingleton(x=1)

    assert o1 == o2
    assert o2 == o3
    assert o1.x == o2.x and o1.x == o3.x

    o1.x = 2
    assert o1.x == o2.x and o1.x == o3.x


if __name__ == '__main__':
    print('Start testing')
    test_Singleton()
    print('Done testing')

# Generated at 2022-06-13 16:52:49.277230
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(metaclass=Singleton):
        pass
    assert Test() is Test()

# Generated at 2022-06-13 16:52:55.872132
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(Singleton):
        """Test class for Singleton metaclass"""
        def __init__(self):
            self.data = 1
        def get_data(self):
            return self.data

    # Instantiate class first time
    assert MyClass().data == 1
    # Instantiate class second time
    assert MyClass().get_data() == 1
    # Instantiate class third time
    assert MyClass().get_data() == 1
    # Check whether every instance is the same
    a = MyClass()
    b = MyClass()
    assert a is b



# Generated at 2022-06-13 16:52:57.870548
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    class B(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    b1 = B()
    b2 = B()
    assert a1 is a2
    assert b1 is b2
    assert a1 is not b1



# Generated at 2022-06-13 16:52:59.340354
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class t(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 1
    a = t()
    b = t()
    assert a is b
    a.foo = 2
    assert a.foo == b.foo

# Generated at 2022-06-13 16:54:13.103837
# Unit test for constructor of class Singleton
def test_Singleton():
    '''
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self, val):
            self.val = val
    '''
    MyClass = type('MyClass', (object,), {
        '__metaclass__': Singleton,
        '__init__': lambda s, val: setattr(s, 'val', val)})

    assert MyClass.__rlock.get_owner() is None

    o1 = MyClass(1)
    assert o1.val == 1
    assert isinstance(o1, MyClass)
    assert MyClass.__rlock.get_owner() is None

    o2 = MyClass(2)
    assert o2.val == 1
    assert o2 is o1
    assert MyClass.__rlock.get_owner() is None

# Generated at 2022-06-13 16:54:15.753395
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    t = Test()
    t1 = Test()
    assert t is t1
    t2 = Test("foo", bar="baz")
    assert t2 is t1

# Generated at 2022-06-13 16:54:22.927932
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest1(object):
        __metaclass__ = Singleton

    class SingletonTest2(object):
        __metaclass__ = Singleton

    instance1 = SingletonTest1()
    instance2 = SingletonTest1()
    instance3 = SingletonTest2()

    print(id(instance1))
    print(id(instance2))
    print(id(instance3))
    print(id(SingletonTest1.__instance))
    print(id(SingletonTest2.__instance))

    assert(instance1 == instance2)
    assert(instance1 != instance3)
    assert(instance2 != instance3)

    assert(id(instance1) == id(instance2))
    assert(id(instance1) != id(instance3))
    assert(id(instance2) != id(instance3))

# Generated at 2022-06-13 16:54:30.338028
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.counter = 0

        def count(self):
            self.counter += 1

        def __repr__(self):
            return '<' + self.__class__.__name__ + '(' + str(self.counter) + ')>'

    obj1 = SingletonTestClass()
    obj1.count()
    print('obj1', obj1)

    obj2 = SingletonTestClass()
    obj2.count()
    print('obj2', obj2)

    assert obj1 is obj2


# Generated at 2022-06-13 16:54:37.442640
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from collections import Counter

    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a=0):
            self.a = a

    class B(object):
        __metaclass__ = Singleton

        def __init__(self, b=0):
            self.b = b

    a1, a2 = A(), A()
    b1, b2 = B(), B()

    assert a1 is a2
    assert b1 is b2

    assert a1.a == a2.a == 0
    assert b1.b == b2.b == 0

    a1.a = 2
    b1.b = 2

    assert a1.a == a2.a == 2
    assert b1.b == b2.b == 2


# Generated at 2022-06-13 16:54:38.655319
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    a = TestSingleton()
    b = TestSingleton()
    assert (a is b)

# Generated at 2022-06-13 16:54:40.429042
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.data = None

    a = Foo()
    b = Foo()

    a.data = 10
    if b.data != 10:
        raise Exception('Not same instance')

# Generated at 2022-06-13 16:54:42.360689
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonMock(object):
        __metaclass__ = Singleton

    mock1 = SingletonMock()
    mock2 = SingletonMock()
    assert mock1 is mock2

# Generated at 2022-06-13 16:54:46.342861
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    test_obj1 = TestClass()
    test_obj2 = TestClass()

    assert test_obj1 is test_obj2



# Generated at 2022-06-13 16:54:48.895803
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(metaclass=Singleton):
        def __init__(self, v):
            self.val = v

    t1 = SingletonTest(1)
    t2 = SingletonTest(2)

    assert t1.val == t2.val
    assert t1 is t2