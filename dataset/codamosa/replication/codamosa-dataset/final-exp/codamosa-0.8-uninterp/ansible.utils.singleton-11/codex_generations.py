

# Generated at 2022-06-13 16:46:39.319543
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

    instance1 = MySingleton()
    instance2 = MySingleton()

    assert instance1 is instance2

# Generated at 2022-06-13 16:46:45.017720
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self, x, y):
            self.x = x
            self.y = y

    try:
        assert A(1,2) == A(2,1)
    except AssertionError:
        print('Error: instances of class must be identical, but they are not')
    
test_Singleton()

# Generated at 2022-06-13 16:46:49.416815
# Unit test for constructor of class Singleton
def test_Singleton():
    class temp(object):
        __metaclass__ = Singleton
        def __init__(self, x, y):
            self.x = x
            self.y = y
    a = temp(1, 2)
    b = temp(3, 4)
    assert a.x == b.x
    assert a.y == b.y

if __name__ == "__main__":
    test_Singleton()
    print("Successful.")

# Generated at 2022-06-13 16:46:51.827553
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Single:
        __metaclass__ = Singleton

    class NotSingle:
        pass

    assert Single() is Single()
    assert NotSingle() is not NotSingle()


# Generated at 2022-06-13 16:46:56.733055
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self, param):
            self.param = param

    mc1 = MyClass('example')
    mc2 = MyClass('example2')

    assert id(mc2) == id(mc1)
    assert mc1.param == 'example'
    assert mc2.param == 'example'



# Generated at 2022-06-13 16:46:58.776539
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert a is b



# Generated at 2022-06-13 16:47:02.531347
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    assert TestSingleton(1).value == 1
    assert TestSingleton(2).value == 1

# Generated at 2022-06-13 16:47:05.519090
# Unit test for constructor of class Singleton
def test_Singleton():
    class YourClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    a = YourClass()
    b = YourClass()
    assert a == b

# Generated at 2022-06-13 16:47:09.932554
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(metaclass=Singleton):
        pass

    foo1 = Foo()
    foo2 = Foo()

    assert foo1 == foo2, "__call__ of class Singleton is not working."

# Run test
test_Singleton___call__()

# Generated at 2022-06-13 16:47:19.959726
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # test Singleton calls __call__ method on first call
    import tempfile
    fd, fpath = tempfile.mkstemp(prefix='test.Singleton.')
    os.close(fd)

# Generated at 2022-06-13 16:47:25.315329
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 1

    a = TestClass()
    b = TestClass()
    assert(a == b)



# Generated at 2022-06-13 16:47:28.946187
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

    a = TestSingleton("A")
    b = TestSingleton("B")

    assert a == b

# Generated at 2022-06-13 16:47:36.240906
# Unit test for constructor of class Singleton
def test_Singleton():
    class C(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.__x = 0

    a = C()
    assert(a.__x == 0)
    a.__x += 1

    b = Singleton('C', (object,), dict())
    assert(a.__x == b.__x)
    b.__x += 1

    c = Singleton('C', (object,), dict())
    assert(c.__x == b.__x)
    c.__x += 1

    assert(a.__x == b.__x and c.__x == b.__x)

# Generated at 2022-06-13 16:47:39.621155
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        pass
    
    a = A()
    b = A()
    assert id(a) == id(b)


# Generated at 2022-06-13 16:47:48.888982
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from _socket import gaierror
    from paramiko.ssh_exception import SSHException
    from ansible.errors import AnsibleError
    def side_effect(*args, **kw):
        raise Exception()
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.v = 1
    a = A()
    assert isinstance(a, A)
    a1 = A()
    assert a == a1
    assert a.v == 1
    assert a1.v == 1
    b = A()
    assert a == b
    assert b.v == 1
    c = A()
    assert a == c
    assert c.v == 1
    a.v = 2
    assert b.v == 2
    assert c.v == 2


# Generated at 2022-06-13 16:47:50.812116
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert A() is A()



# Generated at 2022-06-13 16:47:55.969390
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    global counter
    counter = 0
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            global counter
            counter += 1

    assert counter == 0
    print('initialization')
    MyClass()
    assert counter == 1
    print('Using the existing instance')
    MyClass()
    assert counter == 1

if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:48:00.214350
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 10

    sc = SingletonClass()
    assert sc.x == 10

    sc2 = SingletonClass()
    sc2.x = 20
    assert sc.x == 20

# Generated at 2022-06-13 16:48:03.924310
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 1

    o1 = S()
    o2 = S()
    assert o1 is o2
    assert o1.x == o2.x == 1
    o1.x += 1
    assert o1.x == o2.x == 2

# Generated at 2022-06-13 16:48:06.430577
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    assert TestSingleton() is TestSingleton()

# Generated at 2022-06-13 16:48:11.894086
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 10

    foo1 = Foo()
    foo2 = Foo()
    assert foo1.a == foo2.a


# Generated at 2022-06-13 16:48:13.565319
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    a = Foo()
    b = Foo()
    assert a is b

# Generated at 2022-06-13 16:48:25.045981
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    class NonSingletonTest(object):
        def __init__(self, value):
            self.value = value


# Generated at 2022-06-13 16:48:34.521651
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.errno import ANSIBLE_PRIVILEGE_ESCAPE_PATH, ANSIBLE_MODULE_UTILS_PATH

    # Ensures that only one instance of class A is returned
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert a1 is a2

    # Ensures that only one instance of class B is returned
    class B(A):
        pass

    b1 = B()
    b2 = B()
    assert b1 is b2
    assert b1 is a1

    # Ensures that class C is not a singleton class
    class C(object):
        pass

    c1 = C()
    c2 = C()
    assert c1 is not c2

    # Ensures that class D inherits the

# Generated at 2022-06-13 16:48:40.411528
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Tests for method __call__ of class Singleton"""
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    instance = Test()
    assert isinstance(instance, Test)

    instance_2 = Test()
    assert isinstance(instance_2, Test)

    assert instance is instance_2

# Generated at 2022-06-13 16:48:46.585673
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonClass(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            self.arg = arg

    obj = SingletonClass("hey")
    assert obj is SingletonClass("hey")
    assert obj.arg == "hey"

    obj2 = SingletonClass("arg2")
    assert obj2 is obj
    assert obj2.arg == "arg2"


if __name__ == '__main__':
    import pytest
    pytest.main(['-s', __file__])

# Generated at 2022-06-13 16:48:49.220293
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, i):
            self.i = i

    a1 = A(1)
    a2 = A(2)
    assert (a1 == a2) and (a1.i == 1)



# Generated at 2022-06-13 16:48:50.935321
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton():
        __metaclass__ = Singleton

    assert TestSingleton() is TestSingleton()

# Generated at 2022-06-13 16:48:59.561829
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class TestObj(object):
        __metaclass__ = Singleton
        def __init__(self, arg):
            self.arg = arg

        def __eq__(self, other):
            return (other is not None and
                    self.arg == other.arg)

    assert TestObj("same") is TestObj("same")
    assert TestObj("same") == TestObj("same")
    assert TestObj("same") is not TestObj("different")
    assert TestObj("same") != TestObj("different")

    # Make sure this test can be executed multiple times
    # without an error.
    assert TestObj("same") is TestObj("same")
    assert TestObj("same") == TestObj("same")
    assert TestObj("same") is not TestObj("different")
    assert TestObj("same") != TestObj("different")



# Generated at 2022-06-13 16:49:04.687965
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(metaclass=Singleton):
        def __init__(self):
            self.value = 'Foo'

    inst1 = MyClass()
    inst2 = MyClass()
    assert inst1 is inst2
    assert inst1.value == inst2.value
    inst1.value = 'Bar'
    assert inst1.value == inst2.value

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:49:10.141605
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test:
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 0

    # Since Metaclass will return the instance of the object,
    # these two objects should be the same.
    assert Test() == Test()

# Generated at 2022-06-13 16:49:13.702549
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self, test):
            self.test = test

    ts1 = TestSingleton("ts1")
    ts2 = TestSingleton("ts2")

    assert ts1 == ts2
    assert ts1.test == "ts2"
    assert ts2.test == "ts2"

# Generated at 2022-06-13 16:49:16.412639
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo:
        __metaclass__ = Singleton

    print("obj1: " + str(Foo()))
    print("obj2: " + str(Foo()))

# Generated at 2022-06-13 16:49:23.493962
# Unit test for constructor of class Singleton
def test_Singleton():
    # Class to test
    class TestClass(metaclass=Singleton):
        pass

    class TestClass2(metaclass=Singleton):
        pass

    # Test1: test on creating instance for TestClass
    test1 = TestClass()
    test2 = TestClass()

    assert id(test1) == id(test2), \
        "TestClass: instantiating 'TestClass()' more than once"

    # Test2: test on creating instance for TestClass2
    test3 = TestClass2()
    test4 = TestClass2()

    assert id(test3) == id(test4), \
        "TestClass: instantiating 'TestClass2()' more than once"

    # Test3: test on creating instance for differenct class
    test5 = TestClass()
    test6 = TestClass2()


# Generated at 2022-06-13 16:49:30.243582
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self):
            self.a = 0

        def inc(self):
            self.a += 1

    a = A()
    b = A()

    assert id(a) == id(b), 'Two instances should be identical'
    a.inc()
    assert b.a == 1, 'Changes to one class should be reflected in the other'

# Generated at 2022-06-13 16:49:36.565210
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 1

    t1 = Test()
    t2 = Test()

    assert id(t1) == id(t2)
    assert t1.x == 1
    t1.x += 1
    assert t2.x == 2


# Helper for Singleton with arguments.  See http://stackoverflow.com/a/6798042

# Generated at 2022-06-13 16:49:40.235630
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(metaclass=Singleton):
        def __init__(self, a, b):
            self.a = a
            self.b = b

    assert TestSingleton(1, "xyz") == TestSingleton(2, "abc")
    assert TestSingleton(1, "xyz").a == 1
    assert TestSingleton(1, "xyz").b == "xyz"



# Generated at 2022-06-13 16:49:48.051906
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.my_var = 'my_var_value'

    s1 = MySingleton()
    s1.my_var = 'my_var_value_changed'
    s2 = MySingleton()
    assert s1 is s2
    assert s1.my_var == s2.my_var
    assert s1.my_var == 'my_var_value_changed'



# Generated at 2022-06-13 16:49:50.027569
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test = "test"

    test1 = Test()
    test2 = Test()
    assert test1 is test2
    assert id(test1) == id(test2)
    assert test1.test == test2.test
    pass

# Generated at 2022-06-13 16:49:54.807101
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Unit test for method __call__ of class Singleton
    """
    import unittest

    class Foo(object):
        __metaclass__ = Singleton

    x = Foo()
    y = Foo()

    class Singleton_Test(unittest.TestCase):
        """Unit test for class Singleton
        """
        def test_Singleton___call__(self):
            self.assertEqual(x, y)

    unittest.main()


# Generated at 2022-06-13 16:50:06.952427
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import copy
    import json

    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 0

        def set_a(self, a):
            self.a = a

    a1 = A()
    assert(a1.a == 0)
    a1.set_a(1)
    assert(a1.a == 1)

    a2 = A()
    assert(a2.a == 1)
    a2.set_a(2)
    assert(a2.a == 2)

    assert(a1 is a2)

    b1 = copy.deepcopy(a1)
    assert(b1.a == 2)
    b2 = json.loads(json.dumps(a1))

# Generated at 2022-06-13 16:50:10.371210
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    from nose.tools import assert_equals

    assert_equals(A(), A())

# Generated at 2022-06-13 16:50:12.685310
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass
    TestSingleton()


# Generated at 2022-06-13 16:50:15.259365
# Unit test for constructor of class Singleton
def test_Singleton():
    class Self(metaclass=Singleton):
        def __init__(self):
            pass

    a = Self()
    b = Self()
    assert(a is b)

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:50:19.516111
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

    first_instance = MyClass()
    second_instance = MyClass()

    assert first_instance is second_instance
    assert first_instance.__class__ is second_instance.__class__ is MyClass

# Generated at 2022-06-13 16:50:25.607824
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    assert TestSingleton(10) == TestSingleton(20)
    assert TestSingleton(10).value == 20
    assert TestSingleton(20).value == 20
    assert TestSingleton(10).value == TestSingleton(20).value

# Generated at 2022-06-13 16:50:33.405595
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton1(object):
        __metaclass__ = Singleton

    class TestSingleton2(TestSingleton1):
        def __init__(self, msg):
            self.msg = msg

    t1 = TestSingleton1()                      # create an instance
    assert isinstance(t1, TestSingleton1)      # type of t1

    t2 = TestSingleton1()                      # could not create, get t1 from singleton
    assert isinstance(t2, TestSingleton1)      # type of t2

    assert t1 is t2                            # t1 and t2 are equal

    t3 = TestSingleton2('test singleton')      # create an instance
    assert isinstance(t3, TestSingleton2)      # type of t3

    t4 = TestSingleton2('test singleton 2')

# Generated at 2022-06-13 16:50:37.880685
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

    a = SingletonTest(5)
    b = SingletonTest(6)

    assert id(a) == id(b)
    assert a.x == 5
    assert b.x == 5

# Generated at 2022-06-13 16:50:40.005586
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
  class Test(object):
    __metaclass__ = Singleton

  o1 = Test()
  o2 = Test()
  assert o1 is o2


# Generated at 2022-06-13 16:50:42.140643
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(metaclass=Singleton):
        pass

    a = Foo()
    b = Foo()
    assert a is b

# Generated at 2022-06-13 16:50:52.542646
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    a = A()
    assert(a == A())

# Generated at 2022-06-13 16:50:56.734359
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

    assert SingletonTest()  is SingletonTest()
    assert SingletonTest() is not type(SingletonTest)

# Generated at 2022-06-13 16:51:00.612824
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonClass(metaclass=Singleton):
        def __init__(self):
            self.version = 1.0

    a = SingletonClass()
    b = SingletonClass()

    assert a == b
    assert id(a) == id(b)

# Generated at 2022-06-13 16:51:05.949726
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonChild(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = "Hello"

    child = SingletonChild()
    assert child.x == "Hello"

    child2 = SingletonChild()
    assert id(child2) == id(child)
    assert child2.x == "Hello"

    # test that the singleton is broken if we force it to create a new instance
    child2.__class__.__instance = None
    child3 = SingletonChild()
    assert id(child3) != id(child2)
    assert child3.x == "Hello"

# Generated at 2022-06-13 16:51:09.086442
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

    obj = MyClass()
    obj2 = MyClass()
    assert obj == obj2

# Generated at 2022-06-13 16:51:14.066967
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    t1 = TestSingleton('a', b='b')
    t2 = TestSingleton()
    t3 = TestSingleton()

    assert t1.args == ('a',)
    assert t1.kwargs == {'b': 'b'}
    assert t2 == t3
    assert t1 == t2

# Generated at 2022-06-13 16:51:21.166257
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from .module_utils import AnsibleModule

    class TestSingleton:
        __metaclass__ = Singleton

        def __init__(self, a, b):
            self.a = a
            self.b = b

    def main():
        module = AnsibleModule(argument_spec={})
        objs = []

        for i in range(25):
            objs.append(TestSingleton(i, i * 10 + 1))

        module.exit_json(changed=True, result=objs)

    main()

# Generated at 2022-06-13 16:51:24.994556
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingletonClass(metaclass=Singleton):
        def __init__(self):
            self.val = 42

    assert MySingletonClass().val == 42
    assert MySingletonClass().val == 42

# Generated at 2022-06-13 16:51:35.099152
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, a=1, b=2, c=3):
            self.a = a
            self.b = b
            self.c = c

        def __str__(self):
            return "a=%s b=%s c=%s" % (self.a, self.b, self.c)

    foo_1 = Foo(1, 2, 3)
    foo_2 = Foo(2, 3, 4)

    assert(foo_1 is foo_2)
    assert(foo_1.a == foo_2.a == 1)
    assert(foo_1.b == foo_2.b == 2)
    assert(foo_1.c == foo_2.c == 3)

# Generated at 2022-06-13 16:51:36.803755
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
    obj1 = A()
    obj2 = A()
    assert obj1 is obj2

# Generated at 2022-06-13 16:51:58.298640
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonClass(object):
        __metaclass__ = Singleton
        value = 0

    instance1 = SingletonClass()
    instance1.value = 1
    assert(instance1.value == 1)
    assert(isinstance(instance1, SingletonClass))

    instance2 = SingletonClass()
    assert(instance2.value == 1)
    assert(isinstance(instance2, SingletonClass))
    assert(instance2 == instance1)

# Generated at 2022-06-13 16:52:03.865127
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(metaclass=Singleton):
        def __init__(self,x):
            self.x = x
    foo1 = Foo('foo1')
    foo2 = Foo('foo2')
    assert isinstance(foo1,Foo)
    assert isinstance(foo2,Foo)
    assert foo1 is foo2
    foo1.x = 'foo1.x'
    assert foo1.x == foo2.x

# Generated at 2022-06-13 16:52:09.391328
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    class Bar(object):
        __metaclass__ = Singleton

    f1 = Foo()
    # f2 is actually f1
    f2 = Foo()
    f3 = Bar()

    assert(f1 == f2)
    assert(f1 != f3)
    assert(f2 != f3)

# Generated at 2022-06-13 16:52:13.785089
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a1):
            self.a1 = a1

    a1 = A(23)
    a2 = A(42)

    assert a1 is a2
    assert a1.a1 == 42
    assert a2.a1 == 42



# Generated at 2022-06-13 16:52:16.544062
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    test1 = Test()
    test2 = Test()

# Generated at 2022-06-13 16:52:19.463506
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.val = {}

    a = Test()
    a.val['a'] = 'a'
    assert a == Test()
    assert a.val == Test().val

# Generated at 2022-06-13 16:52:22.636633
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    try:
        instance1 = TestClass()
        instance2 = TestClass()
        assert instance1 == instance2

    except:
        print("[Test failed]")
        return False

    print("[Test OK]")
    return True


if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:52:24.652000
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class One(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'test_Singleton___call__'

    instanceA = One()
    instanceB = One()
    assert instanceA.name == instanceB.name


# Generated at 2022-06-13 16:52:33.436388
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Testing args and kw
    class Single(metaclass=Singleton):
        def __init__(self, arg, kw=1):
            super(Single, self).__init__()
            self.arg = arg
            self.kw = kw

    s = Single('test', kw=2)
    assert isinstance(s, Single)
    assert s.arg == 'test'
    assert s.kw == 2
    s2 = Single('test2', kw=3)
    assert s == s2

    # Testing args only
    class Single(metaclass=Singleton):
        def __init__(self, arg):
            super(Single, self).__init__()
            self.arg = arg
            self.kw = 1

    s = Single('test')
    assert isinstance(s, Single)


# Generated at 2022-06-13 16:52:37.746937
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self):
            self.a = 5
            self.b = 10

    a1 = A()
    a2 = A()
    a1.a = 20
    print(a2.a)
    assert a1 == a2
    assert a1.a == a2.a



# Generated at 2022-06-13 16:52:58.555222
# Unit test for constructor of class Singleton
def test_Singleton():

    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self,x):
            self.bar = x

    a = Foo(1)
    assert a is not None

    b = Foo(2)
    assert b is not None
    assert a is b
    assert a.bar == 2 and b.bar == 2


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:53:01.984125
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

    s = SingletonTest()
    assert s is SingletonTest()



# Generated at 2022-06-13 16:53:04.122295
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    assert(TestSingleton() is TestSingleton())



# Generated at 2022-06-13 16:53:12.502236
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from nose.tools import assert_equals, assert_raises

    class C(metaclass=Singleton):
        pass

    # When a class has a singleton metaclass,
    # a new instance is created when the class is called.
    a, b = C(), C()

    # Calling a class with the singleton metaclass twice returns the
    # same instance.
    assert_equals(a, b)

    class X(object):
        @classmethod
        def __call__(cls):
            raise Exception()

    class Y(X):
        pass

    # A class that has a metaclass that is a subclass of
    # Singleton can only be instantiated once, but it's
    # __call__ method is called every time an instance is
    # requested

# Generated at 2022-06-13 16:53:15.864833
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    # create instances with different names
    t1 = Test()
    t2 = Test()

    # id() should be the same for both cases
    assert id(t1) == id(t2), "The id()s don't match, which means that the two instances are different"


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:53:19.293993
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    instance1 = TestClass()
    instance2 = TestClass()

    assert id(instance1) == id(instance2)


# Generated at 2022-06-13 16:53:22.502066
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, val):
            pass

    a = SingletonTest(7)
    b = SingletonTest(9)
    assert a is b
    assert a.__class__ is b.__class__

# Generated at 2022-06-13 16:53:29.449243
# Unit test for constructor of class Singleton
def test_Singleton():
    import os
    import sys

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.val = 0

        def set_value(self, val):
            self.val = val

        def get_value(self):
            return self.val

    class TestSingleton2(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.val = 0

        def set_value(self, val):
            self.val = val

        def get_value(self):
            return self.val

    t1 = TestSingleton()
    t2 = TestSingleton()

    print("id: t1 = %s" % (id(t1)))

# Generated at 2022-06-13 16:53:34.090483
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self,dummy):
            self.dummy = dummy

    a = A(1)
    assert a == A(1)
    assert a == A(2)
    assert a.dummy == 1
    b = A(3)
    assert b == A(4)
    assert b == a
    assert b.dummy == 1


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:53:43.192265
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText

    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = AnsibleUnsafeText(u'name')

    class MySubClass(MyClass):
        def __init__(self):
            super(MySubClass, self).__init__()
            self.value = 1111

    obj1 = MyClass()
    obj2 = MyClass()
    assert obj1 is obj2

    obj3 = MySubClass()
    obj4 = MySubClass()
    assert obj3 is obj4

# Generated at 2022-06-13 16:54:10.436867
# Unit test for constructor of class Singleton
def test_Singleton():
    import unittest

    class MySingleton(metaclass=Singleton):
        def __init__(self):
            self.some_var = 1

    class MySingleton_derived(MySingleton):
        pass

    class MySingleton_derived_other(MySingleton):
        pass

    class MySingleton_derived_other2(MySingleton):
        pass

    class TestSingleton(unittest.TestCase):
        def test_singleton(self):
            instance_1 = MySingleton()
            instance_2 = MySingleton()
            self.assertIs(instance_1, instance_2)
            instance_1.some_var = 2
            self.assertEqual(instance_2.some_var, 2)
            instance_derived_1 = MySingleton_derived()
            instance_derived_2

# Generated at 2022-06-13 16:54:16.717656
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton
        def getX(self):
            return self.x

    x = MySingleton()
    x.x = 5
    y = MySingleton()
    y.x = 6
    z = MySingleton()
    z.x = 7

    assert(x.getX() == 5)
    assert(y.getX() == 5)
    assert(z.getX() == 5)


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:54:18.668728
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1

    assert isinstance(TestSingleton(), TestSingleton)



# Generated at 2022-06-13 16:54:19.345293
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    assert obj1 is obj2


# Generated at 2022-06-13 16:54:22.390664
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    ts_1 = TestSingleton()
    ts_2 = TestSingleton()
    assert ts_1 is ts_2
    assert ts_1.__class__ is TestSingleton

# Generated at 2022-06-13 16:54:24.408569
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

    foo = Foo()
    assert foo is Foo()
    assert Foo is Foo.__class__

# Generated at 2022-06-13 16:54:28.024684
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test1(object):
        __metaclass__ = Singleton

        def __init__(self, foo):
            self.foo = foo

    assert Test1(None) is Test1(None)


# Generated at 2022-06-13 16:54:32.655873
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, num):
            self.num = num

    assert SingletonTest.__instance is None

    instance_1 = SingletonTest(num=1)
    assert SingletonTest.__instance is instance_1

    instance_2 = SingletonTest(num=2)
    assert SingletonTest.__instance is instance_2
    assert instance_2.num == 2



# Generated at 2022-06-13 16:54:39.242195
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # test for normal operation
    class TestSingleton(metaclass=Singleton):
        @staticmethod
        def __init__():
            pass

    instance1 = TestSingleton()
    instance2 = TestSingleton()
    assert instance1 is instance2

    # test for error in initialization of singleton
    class TestSingleton2(metaclass=Singleton):
        @staticmethod
        def __init__():
            raise Exception("Intentional Error")

    def create_instance():
        TestSingleton2()

    try:
        create_instance()
    except Exception:
        assert True

    # test for error in __call__
    class TestSingleton3(metaclass=Singleton):
        @staticmethod
        def __init__():
            print("Init")


# Generated at 2022-06-13 16:54:47.807339
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, a, b):
            self.a = a
            self.b = b

    class Test2Class(object):
        __metaclass__ = Singleton
        def __init__(self, x, y):
            self.x = x
            self.y = y

    a = TestClass(1, 2)
    b = TestClass(3, 4)

    assert a.a == b.a, a.a
    assert a.b == b.b, a.b

    x = Test2Class(1, 2)
    y = Test2Class(3, 4)

    assert x.x == y.x, x.x
    assert x.y == y.y, x.y


# Generated at 2022-06-13 16:55:07.659568
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            pass
    assert SingletonTest('a') is SingletonTest('b')

# Generated at 2022-06-13 16:55:12.475754
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.count = 0

    # Instantiate the first one
    instance = TestSingleton()
    assert instance.count == 0

    # Instantiate the second one
    instance = TestSingleton()
    assert instance.count == 0

    # Instantiate the third one
    instance = TestSingleton()
    assert instance.count == 0

    # Advance the first one
    instance.count += 1
    assert instance.count == 1

    # Validate the second one is still at 0
    instance = TestSingleton()
    assert instance.count == 1
    instance.count += 1
    assert instance.count == 2

    # Validate the third one is still at 0
    instance = TestSingleton()
    assert instance.count == 2

# Generated at 2022-06-13 16:55:22.488169
# Unit test for constructor of class Singleton
def test_Singleton():

    class OrdinaryClass:
        pass

    class ClassWithSingleton(OrdinaryClass):
        __metaclass__ = Singleton

    # Ordinary class
    c1 = OrdinaryClass()
    c2 = OrdinaryClass()
    assert c1 is not c2

    # Class with Singleton
    s1 = ClassWithSingleton()
    s2 = ClassWithSingleton()
    assert s1 is s2

    # Test inheritance from ordinary class
    assert isinstance(s1, OrdinaryClass)
    assert isinstance(s2, OrdinaryClass)

    # Test inheritance from class with Singleton
    class Inherited(ClassWithSingleton):
        pass

    i1 = Inherited()
    i2 = Inherited()
    assert i1 is i2


if __name__ == '__main__':
    test_Singleton

# Generated at 2022-06-13 16:55:27.191033
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class mySingleton(metaclass=Singleton):
        def __init__(self, name="test"):
            self.name = name

    i1 = None
    i2 = None
    i1 = mySingleton("i1")
    i2 = mySingleton("i2")
    assert i1 is i2



if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:55:37.424469
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.index = 0

        def __str__(self):
            return 'index = %d' % self.index

        def __repr__(self):
            return self.__str__()

        def increase(self):
            self.index += 1

    # First instantiation
    a = Test()
    assert a is not None

    # Second instantiation
    b = Test()
    assert b is not None

    # Make sure both instances are in fact the same object
    assert a is b

    # Operations on a should be reflected in b
    a.increase()
    assert a.index == b.index
    b.increase()
    assert a.index == b.index

    # Make sure instances are distinct from previous

# Generated at 2022-06-13 16:55:41.144703
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = "Test"

    a = Test()
    b = Test()

    assert id(a) == id(b)

# Generated at 2022-06-13 16:55:48.370500
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(metaclass = Singleton):
        def __init__(self, value):
            self.value = value

    class Bar(metaclass = Singleton):
        def __init__(self, value):
            self.value = value

    # If a single instance of Foo exists, no new instances can be created
    foo = Foo('foo')
    print (foo.value)
    if foo == Foo('bar'):
        print ("Only a single instance of class Foo exists")

    # If a single instance of Bar exists, no new instances can be created
    bar = Bar('bar')
    print (bar.value)
    if bar == Bar('foo'):
        print ("Only a single instance of class Bar exists")

    # A new instance of Foo will not be created if one already exists

# Generated at 2022-06-13 16:55:53.806172
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = None

    obj1 = MySingleton()
    obj1.value = 'value1'

    obj2 = MySingleton()

    assert id(obj1) == id(obj2)
    assert obj1.value == 'value1'
    assert obj2.value == 'value1'

# Generated at 2022-06-13 16:55:55.628421
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 42

    assert MyClass().x == 42

# Generated at 2022-06-13 16:55:58.386126
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.plugins.loader import fragment_loader
    assert isinstance(fragment_loader, Singleton)
    assert id(fragment_loader) == id(fragment_loader)