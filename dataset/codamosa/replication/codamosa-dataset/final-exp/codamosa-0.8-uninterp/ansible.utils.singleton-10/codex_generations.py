

# Generated at 2022-06-13 16:46:40.578503
# Unit test for constructor of class Singleton
def test_Singleton():
    class A:
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

    a = A(10)
    assert a.x == 10

    b = A(20)
    assert b.x == 10

# Generated at 2022-06-13 16:46:48.996363
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, *args, **kwargs):
            import time
            time.sleep(0.01)
            self.args = args
            self.kwargs = kwargs

    import threading
    threads = []
    for i in range(2):
        threads.append(threading.Thread(target=TestSingleton))
        threads[i].start()

    test_singleton = TestSingleton()
    for i in range(2):
        threads[i].join()
        assert test_singleton == threads[i].target.__instance,\
            "Instances are not equal"

# Generated at 2022-06-13 16:46:51.213727
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Dummy(object):
        __metaclass__ = Singleton

    dummy1 = Dummy()
    dummy2 = Dummy()

    # dummy1 and dummy2 should be identical
    assert dummy1 is dummy2



# Generated at 2022-06-13 16:46:54.497449
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.num = 1

    t = Test()
    assert t.num == 1
    t.num = 5
    t2 = Test()
    assert t2.num == 5

# Generated at 2022-06-13 16:46:58.467142
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'S'

    class S2(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'S2'

    s1 = S()
    s2 = S()

    assert s1 is s2
    assert s1.name == s2.name

    s2 = S2()
    s3 = S2()

    assert s2 is s3



# Generated at 2022-06-13 16:47:04.313141
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        def __init__(self):
            self.a = 1
    a = A()
    b = A()
    assert a is b
    a.a = 2
    assert b.a == 2
    b.a = 3
    assert a.a == 3


if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:47:06.005395
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        pass

    a = A()
    b = A()
    assert a is b

if __name__ == '__main__':
    print('Executing unit tests for Singleton metaclass')
    test_Singleton()
    print('Done.')

# Generated at 2022-06-13 16:47:10.440957
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    a = Test(42)
    assert a.value == 42

    b = Test(10)
    assert b == a


# Generated at 2022-06-13 16:47:16.850729
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Test __call__ method of class Singleton
    """
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    obj1 = TestClass('value')
    assert isinstance(obj1, TestClass)
    assert obj1.value == 'value'
    obj2 = TestClass('value')
    assert isinstance(obj2, TestClass)
    assert obj1 is obj2

# Generated at 2022-06-13 16:47:22.589236
# Unit test for constructor of class Singleton
def test_Singleton():

    class TestSingleton(Singleton):
        def __init__(self):
            super(TestSingleton, self).__init__()
            self.foo = "bar"

    a = TestSingleton()
    b = TestSingleton()

    assert a is b
    assert a.foo == b.foo

# Generated at 2022-06-13 16:47:28.411373
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(Singleton):
        pass

    assert Foo() is Foo()
    assert isinstance(Foo(), Foo)

    class Bar(Foo):
        pass

    assert Foo() is Bar()
    assert isinstance(Bar(), Foo)

# Generated at 2022-06-13 16:47:35.222762
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, x=None):
            self.x = x

    test1 = Test()
    assert test1.x is None

    test2 = Test('test')
    assert test2.x == 'test'
    assert test2 is test1

    test3 = Test()
    assert test3.x == 'test'
    assert test3 is test1

    test4 = Test('test4')
    assert test4.x == 'test4'
    assert test4 is test1

# Generated at 2022-06-13 16:47:41.075811
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    s1 = SingletonTest("foo")
    s2 = SingletonTest("bar")
    assert id(s1) == id(s2)
    assert s1.value == s2.value == "foo"

# Generated at 2022-06-13 16:47:49.684695
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test_value = 0

    obj1 = MyClass()
    obj2 = MyClass()

    assert(obj1 is obj2)

    obj1.test_value = 1
    print('obj1.test_value =', obj1.test_value)
    print('obj2.test_value =', obj2.test_value)
    assert(obj1.test_value == obj2.test_value == 1)

    obj2.test_value = 2
    print('obj1.test_value =', obj1.test_value)
    print('obj2.test_value =', obj2.test_value)
    assert(obj1.test_value == obj2.test_value == 2)

   

# Generated at 2022-06-13 16:47:58.646226
# Unit test for constructor of class Singleton
def test_Singleton():
    from collections import namedtuple
    import copy

    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

    f = Foo(123)
    assert f.x == 123

    g = Foo(456)
    assert g.x == 123
    assert g is f

    f = Foo(789)
    assert g.x == 123
    assert f.x == 123
    assert f is g

    # don't allow subclasses to add args
    try:
        class Bar(Foo):
            def __init__(self, y):
                super(Bar, self).__init__(y)
    except TypeError:
        pass

    copy.copy(Foo(123))
    copy.deepcopy(Foo(123))

    global _


# Generated at 2022-06-13 16:48:02.258804
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class FOO(object, metaclass=Singleton):
        def __init__(self):
            self.data = 1

    f1 = FOO()
    assert isinstance(f1, FOO)
    f1.data = 2
    assert f1.data == 2
    f2 = FOO()
    assert f2.data == 2
    assert f1 is f2

# Generated at 2022-06-13 16:48:06.094135
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    __tracebackhide__ = True
    class A(object):
        __metaclass__ = Singleton
    a1 = A()
    a2 = A()
    assert a1 is a2

# Generated at 2022-06-13 16:48:12.848914
# Unit test for constructor of class Singleton
def test_Singleton():
    import mock

    class SingleA(object):
        __metaclass__ = Singleton

    a1 = SingleA()
    a2 = SingleA()
    assert a1 is a2

    with mock.patch.object(Singleton, '__call__', return_value='foo') as mock_call:
        s = Singleton('foo', (object,), {})
        s2 = Singleton('foo', (object,), {})
        assert s is s2
        mock_call.assert_called_once_with('foo', (object,), {})



# Generated at 2022-06-13 16:48:17.968768
# Unit test for constructor of class Singleton
def test_Singleton():
    class SomeClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.init_called = True

    x = SomeClass()
    y = SomeClass()
    assert x is y
    assert x.init_called is True
    assert y.init_called is True

# Generated at 2022-06-13 16:48:25.801468
# Unit test for constructor of class Singleton
def test_Singleton():
    # make sure we're not making anything non-singleton
    class TestClass(object):
        __metaclass__ = Singleton
    # verify that two instances are the same.
    x = TestClass()
    y = TestClass()
    assert x == y
    # verify that if we try to declare another singleton we get an error.
    try:
        class TestClass(object):
            __metaclass__ = Singleton
    except RuntimeError:
        pass
    else:
        raise Exception('RuntimeError not raised')


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:48:35.684843
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import threading
    from Queue import Queue

    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    # 4 threads are used to test the method
    q = Queue()
    n = 4

    def worker(q):
        obj = MyClass()

        # the four threads share the same instance of MyClass()
        assert q.full() or obj is MyClass()
        q.put_nowait(obj)

    # start threads
    threads = [threading.Thread(target=worker, args=(q,))
               for i in range(n)]
    [t.start() for t in threads]
    [t.join() for t in threads]

    # assert the four threads share the same instance of MyClass()

# Generated at 2022-06-13 16:48:43.548077
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, bar):
            self.bar = bar

    class Bar(object):
        __metaclass__ = Singleton
        def __init__(self, foo):
            self.foo = foo


    f1 = Foo(1)
    assert f1.bar == 1

    f2 = Foo(2)
    assert f1 is f2

    b1 = Bar(f1)
    assert b1.foo is f1

    b2 = Bar(f2)
    assert b1 is b2


# Generated at 2022-06-13 16:48:49.008182
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object, metaclass=Singleton):
        def __init__(self):
            pass

        def thetest(self):
            return True

    t1 = Test()
    t2 = Test()

    assert t1 == t2
    assert id(t1) == id(t2)
    assert t1.thetest() == t2.thetest()

# Generated at 2022-06-13 16:48:53.802628
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class test_Singleton_Class(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    a = test_Singleton_Class(1)
    a.value = 2

    b = test_Singleton_Class(1)
    b.value = 3

    assert a.value == b.value



# Generated at 2022-06-13 16:48:57.337618
# Unit test for constructor of class Singleton
def test_Singleton():
    with open('input.txt','r') as input:
        filename = input.readline()
        with open(filename, 'r') as input:
            line1 = input.readline().strip()
            line2 = input.readline().strip()
            line3 = input.readline().strip()

# Generated at 2022-06-13 16:49:05.220483
# Unit test for constructor of class Singleton
def test_Singleton():
    class Single(object):
        __metaclass__ = Singleton

        def __init__(self, val):
            self.val = val
    # assert that __init__ is called only once
    assert Single(val='a').val == 'a'
    assert Single(val='b').val == 'a'
    assert Single().val == 'a'

# Unit test that __call__ is called

# Generated at 2022-06-13 16:49:07.165042
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

    x = MyClass()
    y = MyClass()
    assert(x is y)

# Generated at 2022-06-13 16:49:11.027848
# Unit test for constructor of class Singleton
def test_Singleton():
    # Create a new class inheriting Singleton metaclass
    class Foo(metaclass=Singleton):
        def __init__(self,bar='baz'):
            self.bar = bar

    # Create two instances of the class
    a = Foo()
    b = Foo()

    # Assert that these are the same instance
    assert a is b

# Generated at 2022-06-13 16:49:15.400454
# Unit test for constructor of class Singleton
def test_Singleton():
    # test_class class has been created with class 'Singleton'
    class test_class(metaclass=Singleton):
        test_attribute = 'test'

    # there is no need to call test_class() as this will be done during class definition
    print(test_class.test_attribute)


# Generated at 2022-06-13 16:49:19.746191
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.val = 0

        def inc(self):
            self.val += 1

    a = A()
    a.inc()
    b = A()
    b.inc()
    print(a.val, b.val)


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:49:26.709667
# Unit test for constructor of class Singleton
def test_Singleton():
    class testClass(object):
        __metaclass__ = Singleton

    obj1 = testClass()
    obj2 = testClass()

    assert obj1 == obj2
    assert obj1 is obj2

# Generated at 2022-06-13 16:49:31.001021
# Unit test for constructor of class Singleton
def test_Singleton():
    class my_class(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = "my_class"

    obj1 = my_class()
    obj2 = my_class()

    assert obj1 == obj2
    assert obj1.name == "my_class"
    assert obj2.name == "my_class"

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:49:40.608350
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        """Test class to be used as a singleton"""
        __metaclass__ = Singleton

        def __init__(self, a, b):
            self.a = a
            self.b = b

    # First call to constructor
    test_1 = TestSingleton("a", "b")
    print("first:", test_1)
    print("first.a:", test_1.a)
    print("first.b:", test_1.b)

    # Second call to constructor should return the same object
    test_2 = TestSingleton("c", "d")
    print("second:", test_2)
    print("second.a:", test_2.a)
    print("second.b:", test_2.b)

    # We should have only one object now

# Generated at 2022-06-13 16:49:45.044142
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()

    return a is b

if __name__ == '__main__':
    assert test_Singleton() == True

# Generated at 2022-06-13 16:49:51.584365
# Unit test for constructor of class Singleton
def test_Singleton():
    try:
        import unittest2 as unittest
    except:
        import unittest
    from ansible.module_utils.six import with_metaclass

    class SingletonTest(with_metaclass(Singleton, object)):
        def __init__(self):
            self.foo = 1
    a = SingletonTest()
    b = SingletonTest()
    assert a.foo == 1
    assert b.foo == 1
    assert a is b
    a.foo = 2
    assert b.foo == 2

# Generated at 2022-06-13 16:49:58.982889
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
    assert a2 is not b2

# Generated at 2022-06-13 16:50:01.642832
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Singleton_Instance(object):
        __metaclass__ = Singleton

    s1 = Singleton_Instance()
    s2 = Singleton_Instance()
    assert(s1 == s2)

# Generated at 2022-06-13 16:50:02.853790
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    assert 'Singleton' in globals(), 'class Singleton not defined'



# Generated at 2022-06-13 16:50:07.227567
# Unit test for constructor of class Singleton
def test_Singleton():
    class Class1(metaclass=Singleton):
        def __init__(self):
            self.x = 0
            self.y = 0

    a = Class1()
    b = Class1()
    assert a is b
    assert a.x == b.x
    assert a.y == b.y
    a.x = 1
    b.y = 3
    assert a is b
    assert a.x == b.x
    assert a.y == b.y

# Generated at 2022-06-13 16:50:10.705546
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert a1 is a2

# Generated at 2022-06-13 16:50:18.299491
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(metaclass=Singleton):
        """ Test class
        """
        def __init__(self):
            print("Initialising Test class")

    t1 = Test()
    t2 = Test()
    assert t1 == t2

# Generated at 2022-06-13 16:50:20.959667
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass:
        __metaclass__ = Singleton

    assert MyClass() is MyClass()
    assert MyClass() is not MyClass()

# Generated at 2022-06-13 16:50:30.381045
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from collections import OrderedDict

    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert a is b

    class B(object):
        __metaclass__ = Singleton

    # We expect an ordered dict, where the order of the keys is
    # preserved, which is consistent with the order of definition
    # of the classes
    res = OrderedDict()
    res['A'] = A
    res['B'] = B

    # We expect that multiple instances of the same class returned
    # by __call__ are actually the same instance
    assert OrderedDict((n, c()) for n, c in res.items()) == OrderedDict((n, c()) for n, c in res.items())



# Generated at 2022-06-13 16:50:34.015639
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    a = Foo()
    b = Foo()
    c = Foo()
    assert id(a) == id(b) == id(c)


# Generated at 2022-06-13 16:50:40.041918
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__=Singleton
        def __init__(self):
            self.a = 10
        def test(self):
            self.a = 20


    t = Test()
    print("t.a = %d" %t.a)
    t.test()
    print("t.a = %d" %t.a)
    t2 = Test()
    print("t2.a = %d" %t2.a)


# Generated at 2022-06-13 16:50:42.835220
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self):
            pass
    a = A()
    b = A()
    assert id(a) == id(b)

# Generated at 2022-06-13 16:50:46.843355
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    assert Test('foo').value == 'foo'
    assert Test('bar').value == 'foo'

# Generated at 2022-06-13 16:50:50.652986
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass:
        __metaclass__ = Singleton

    t1 = TestClass()
    t2 = TestClass()

    assert(t1 is t2)


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:50:52.696670
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
    assert TestSingleton() is TestSingleton()

# Generated at 2022-06-13 16:50:58.942724
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonUser(Singleton):
        def __init__(self):
            print("__init__")

    # __init__ should only be called for one time
    assert(SingletonUser() == SingletonUser())

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:51:11.925614
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self._x = x
        def getX(self):
            return self._x
    a = A(4)
    a2 = A(5)
    print(a.getX())
    print(a2.getX())
    print(a == a2)
    print(id(a))
    print(id(a2))

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:51:15.377030
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(metaclass=Singleton):
        pass
    assert id(Test()) == id(Test())


# Generated at 2022-06-13 16:51:22.828160
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test1(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = None

    class Test2(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = None

    t1 = Test1()
    t1.x = True
    assert t1.x

    t2 = Test2()
    if t2.x is not None:
        raise AssertionError

    t3 = Test1()
    assert t3 is t1
    assert t3.x
    t3.x = False
    assert t1.x is False



# Generated at 2022-06-13 16:51:28.336247
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, foo):
            self.foo = foo

    s1 = SingletonTest('bar')
    s2 = SingletonTest('buzz')

    assert s1.foo == s2.foo



# Generated at 2022-06-13 16:51:34.676980
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class ClassA(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = "hello"
            self.b = "world"

    classA1 = ClassA()
    classA2 = ClassA()
    assert classA1.a == "hello"
    assert classA1.b == "world"
    assert classA2.a == "hello"
    assert classA2.b == "world"
    assert id(classA1) == id(classA2)



# Generated at 2022-06-13 16:51:39.888345
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 0

    a1 = A()
    a2 = A()
    assert a1 is a2

    a1.a = 1
    assert a2.a == 1

    try:
        a3 = A.__new__(A)
    except:
        pass
    except Exception as e:
        raise e
    else:
        raise AssertionError("A.__new__(A) should throw a TypeError")

# Generated at 2022-06-13 16:51:47.232820
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Test type __init__
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.data = 0

    # Test __call__ when instance is None
    assert Test() is Test()

    t1 = Test()
    assert t1 == Test()
    assert t1.data == 0

    # Test __call__ when instance is not None
    t2 = Test()
    assert t2 == Test()
    assert t1 is t2
    t2.data = 1

    # Make sure the singleton is actually a singleton
    assert t1.data == 1


# Generated at 2022-06-13 16:51:50.816403
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            print("init")

    instance1 = MySingleton()
    assert (instance1.__class__) == MySingleton

    instance2 = MySingleton()
    assert (instance2.__class__) == MySingleton

    assert instance1 == instance2

# Generated at 2022-06-13 16:51:55.577737
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 3

    a = A()
    b = A()
    assert(a == b)
    assert(a.x == 3)
    assert(b.x == 3)

# Generated at 2022-06-13 16:51:59.692003
# Unit test for constructor of class Singleton
def test_Singleton():
    class singleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            print("init")
            self.num = 1

    s1 = singleton()
    s2 = singleton()
    assert id(s1) == id(s2)

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:52:10.568629
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(metaclass=Singleton):
        pass

    assert TestClass() is TestClass()
    assert TestClass() is TestClass()

# Generated at 2022-06-13 16:52:18.675380
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class MyClass(metaclass=Singleton):
        def __init__(self, val = 0):
            self.prop = val

    def check_method_call(instance, val_expected):
        assert instance.prop == val_expected
        instance.prop += 1
 
    instance_1 = MyClass(1)
    check_method_call(instance_1, 1)
    instance_2 = MyClass(2)
    check_method_call(instance_2, 2)
    instance_3 = MyClass(3)
    check_method_call(instance_3, 3)

    assert instance_1 == instance_2 == instance_3 
    assert instance_1.prop == 4



# Generated at 2022-06-13 16:52:21.235260
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()

    assert a1 is a2



# Generated at 2022-06-13 16:52:24.558300
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self, *args, **kwargs):
            self.name = 'Test'

    test1 = Test('1', '2')
    test2 = Test('3', '4')
    test3 = Test('1', '2')
    print(test1.name)
    print(test2.name)
    print(test3.name)


# Generated at 2022-06-13 16:52:33.030259
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self, a, b=2):
            self.a = a
            self.b = b

    # test class is instance of Singleton
    assert isinstance(TestClass, Singleton)

    # get instance of TestClass
    instance = TestClass("test_a")

    # check result
    assert instance.a == "test_a"
    assert instance.b == 2

    # check getting the same instance
    instance2 = TestClass("test_a", 3)

    # check result
    assert instance2.a == "test_a"
    assert instance2.b == 2

    # check instance is the same
    assert instance is instance2


# Generated at 2022-06-13 16:52:41.381844
# Unit test for constructor of class Singleton
def test_Singleton():
    """Unit test for Singleton"""

    class TestSingleton(object):

        __metaclass__ = Singleton

    class TestSingleton1(object):

        __metaclass__ = Singleton

        def __init__(self):
            pass

    assert not TestSingleton == TestSingleton1

    assert Singleton.__init__ == TestSingleton.__init__
    assert Singleton.__init__ == TestSingleton1.__init__

    assert TestSingleton.__instance == None
    assert TestSingleton1.__instance == None

    # Instantiate Singleton objects
    obj1 = TestSingleton()
    obj2 = TestSingleton1()

    assert obj1 == obj2
    assert TestSingleton.__instance == obj1

    # __instance should have been reset to None
    # because class TestSingleton1 inherits __

# Generated at 2022-06-13 16:52:46.813595
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # if cls.__instance is not None:
    s = Singleton('MySingleton',tuple(),dict())
    s.__instance = 'test'
    assert s() == 'test'

    # if cls.__instance is None:
    s = Singleton('MySingleton',tuple(),dict())
    assert s.__instance is None
    assert s() is s

    # threading
    s = Singleton('MySingleton',tuple(),dict())
    assert s.__instance is None
    assert s() is s

# Generated at 2022-06-13 16:52:49.101290
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(metaclass=Singleton):
        pass

    t1 = Test()
    t2 = Test()
    assert t1 is t2

    t3 = Test()
    assert t2 is t3



# Generated at 2022-06-13 16:52:52.803585
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 42

    foo1 = Foo()
    foo2 = Foo()

    assert foo1 is foo2
    assert foo1.x == foo2.x == 42

# Generated at 2022-06-13 16:52:59.998678
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            self.arg = arg

        def __cmp__(self, other):
            return self.__class__ == other.__class__ and self.arg == other.arg

    class Test1(Test):
        pass

    class Test2(Test):
        pass

    a = Test(1)
    b = Test(1)
    c = Test(2)
    d = Test1(1)
    e = Test1(1)
    f = Test1(2)
    g = Test2(1)
    h = Test2(1)
    i = Test2(2)

    assert a is b
    assert a is not c
    assert b is not c

    assert d is e

# Generated at 2022-06-13 16:53:14.263229
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from unittest import TestCase, main
    from inspect import getdoc
    from random import random, seed

    class A(object):
        __metaclass__ = Singleton

    class B(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = random()

    class C(B):
        pass

    seed(42)

    class TestSingleton(TestCase):
        def test_000_docstring(self):
            self.assertTrue(len(getdoc(Singleton)) > 0)

        def test_010_instantiate_A(self):
            self.assertEqual(A(), A())

        def test_011_instantiate_A_with_args(self):
            with self.assertRaises(TypeError):
                A(1)


# Generated at 2022-06-13 16:53:20.138620
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import pytest
    from threading import RLock

    class Test(metaclass=Singleton):
        def __init__(self):
            pass

    t = Test()
    assert isinstance(t, Test)
    assert isinstance(t.__rlock, RLock)

    t1 = Test()
    assert t1 is t

    with pytest.raises(TypeError):
        Test() is t1



# Generated at 2022-06-13 16:53:23.949316
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    calls = []

    class A(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            calls.append(arg)

    instance1 = A('foo')
    instance2 = A('bar')
    assert len(calls) == 1, len(calls)
    assert calls == ['foo'], calls
    assert instance1 == instance2, instance2

# Generated at 2022-06-13 16:53:30.923634
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton

    # Instance created
    # Time 1: 10:00:00
    my_singleton = MySingleton()
    assert my_singleton is MySingleton()

    # Nothing happened
    # Time 2: 10:00:01
    assert my_singleton is MySingleton()

    # Instance destroyed
    # Time 3: 10:00:02
    my_singleton = None
    assert MySingleton() is MySingleton()

    # Class instance destroyed
    # Time 4: 10:00:03
    MySingleton = None
    assert MySingleton() is not MySingleton()

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:53:35.727570
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.lock = RLock()
            self.stack = []

        def test(self):
            with self.lock:
                self.stack.append("A")

    def test_Singleton__call__():
        # GIVEN
        test = Test()

        # WHEN
        test.test()

        # THEN
        expected = ["A"]
        assert test.stack == expected
        assert Test().stack == expected


# Generated at 2022-06-13 16:53:40.769285
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 10

    obj1 = TestClass()
    # check that only one object is created
    obj1.a = 20
    obj2 = TestClass()
    assert obj1.a == obj2.a

# Generated at 2022-06-13 16:53:49.302271
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.module_utils.six import with_metaclass
    from ansible.module_utils._text import to_bytes

    class A(with_metaclass(Singleton, object)):
        def __init__(self, x=0):
            self.x = x

        def add(self, y):
            self.x = self.x + y

    a = A()
    b = A()
    assert a is b
    a.add(5)
    assert a.x == 5
    assert b.x == 5

    class B(with_metaclass(Singleton, object)):
        def __init__(self, x=to_bytes('0', encoding='UTF-8')):
            self.x = x


# Generated at 2022-06-13 16:53:55.459696
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test = True

    s1 = TestSingleton()
    assert s1.test is True
    s2 = TestSingleton()
    assert s2.test is True

    # Test if we get the same object each time
    assert s1 is s2

    # Test if s2 has the same attribute as s1
    assert s1.test is s2.test


if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:54:06.627823
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            self.arg = arg

    a = A('value')

    assert a.arg == 'value'
    assert A('other value') == a
    assert a.arg == 'value'

    # The followings are not allowed
    # Bad example: Uncomment to see what happens
    #A()

    #assert A() == A()
    #assert A() == None
    #assert 'A()' == A()
    #assert None == A()
    #assert A() == 0
    #assert A() == '0'
    #assert A() == ''
    #assert A() == 'A()'


# Generated at 2022-06-13 16:54:09.043406
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class test_instance:
        pass

    class test_class(metaclass=Singleton):
        def __init__(self):
            self.instance = test_instance()

    assert isinstance(test_class(), test_class)
    assert test_class() == test_class()
    assert test_class() is test_class()
    assert test_class().instance is test_class().instance

# Generated at 2022-06-13 16:54:19.507156
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test_var = 1

    c1 = TestClass()
    c2 = TestClass()
    c3 = TestClass()

    c1.test_var += 1

    assert id(c1) == id(c2) == id(c3)
    assert c1.test_var == c2.test_var == c3.test_var == 2

# Generated at 2022-06-13 16:54:21.372313
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    obj1 = MySingleton("foo")
    obj2 = MySingleton("bar")
    assert obj1 is obj2


# Generated at 2022-06-13 16:54:24.444659
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 42

    assert TestSingleton() is TestSingleton()
    assert TestSingleton().value == 42
    assert TestSingleton().value == 42



# Generated at 2022-06-13 16:54:29.822365
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test_Singleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1
            self.b = 2

    a = Test_Singleton()
    b = Test_Singleton()

    assert(a is b)
    assert(a.a == b.a)
    assert(a.b == b.b)


# Generated at 2022-06-13 16:54:37.009615
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    '''
    Unit test for method __call__ of class Singleton.
    '''
    from threading import Thread

    class A(object):
        __metaclass__ = Singleton
        def __init__(self, rlock, flag):
            self.rlock = rlock
            self.flag = flag
            self.rlock.acquire()
            self.flag.append(True)
            self.rlock.release()

    flag = []
    rlock = RLock()
    instance1 = A(rlock, flag)
    t = Thread(target=A, args=(rlock, flag))
    t.start()
    t.join()

    assert instance1 is A(rlock, flag)
    assert len(flag) == 1

    class B(object):
        __metaclass__ = Singleton
       

# Generated at 2022-06-13 16:54:40.979757
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton

    mySingleton1 = MySingleton()
    mySingleton2 = MySingleton()

    assert mySingleton1 == mySingleton2
    assert id(mySingleton1) == id(mySingleton2)


if __name__ == '__main__':
    test_Singleton___call__()
    print('Test finished')

# Generated at 2022-06-13 16:54:47.808168
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # test for when __instance is set
    class Singleton_test(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value
            self.__instance = 'instance'

    assert Singleton_test(5).__instance == 'instance'
    # test for when __instance is not set
    class Singleton_test(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    assert Singleton_test(5).value == 5

# Generated at 2022-06-13 16:54:55.315232
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from unittest import TestCase, main as test_main

    class TestSingleton(object):
        __metaclass__ = Singleton

    class TestSingleton__call__(TestCase):
        def test_should_return_an_instance_of_TestSingleton(self):
            self.assertIsInstance(TestSingleton(), TestSingleton)

        def test_should_always_return_the_same_instance(self):
            self.assertIs(TestSingleton(), TestSingleton())

    test_main()

# Generated at 2022-06-13 16:54:59.748932
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        def __init__(self):
            self.val = 42

    obj1 = TestClass()
    obj2 = TestClass()
    assert obj1 is obj2
    assert obj1.val == obj2.val
    assert obj1.val == 42


# Generated at 2022-06-13 16:55:02.904358
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    def TestClass():
        pass

    TestClass=Singleton('TestClass', (object,), {'TestMethod': lambda: 42})

    for _ in range(10):
        assert TestClass() == TestClass()
    assert TestClass.TestMethod() == 42

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:55:11.487673
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        pass

    instance1 = TestClass()
    instance2 = TestClass()
    assert instance1 is instance2

# Generated at 2022-06-13 16:55:17.829546
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    sequence = []

    class Test(metaclass=Singleton):
        def __init__(self):
            self.name = 'name'
            sequence.append('Test.__init__')

        def __repr__(self):
            sequence.append('Test.__repr__')
            return 'Test(' + repr(self.name) + ')'

    a = Test()
    assert a.name == 'name'
    assert a is Test()
    assert sequence == ['Test.__init__', 'Test.__init__', 'Test.__repr__']



# Generated at 2022-06-13 16:55:26.459813
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SSingleton():
        __metaclass__ = Singleton

    cl1 = SSingleton()
    cl2 = SSingleton()
    assert cl1 is cl2

    from threading import Thread

    def thread_target():
        cl1 = SSingleton()
        assert cl1 is cl2

    threads = []
    for i in xrange(5):
        threads.append(Thread(target=thread_target))
        threads[-1].start()

    for i in xrange(5):
        threads[i].join()

    return True

if __name__ == '__main__':
    test_Singleton___call__()
    print('test ok')

# Generated at 2022-06-13 16:55:36.095207
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from .util.display import Display
    from .config.manager import ConfigManager

    # test if singleton returns a single instance of the class
    # first instance
    display = Display()
    # second instance
    display2 = Display()
    # check if both instances are equal
    assert display == display2

    # test if different singleton-based classes return a single
    # instance of that class
    # first instance
    config = ConfigManager()
    # second instance
    config2 = ConfigManager()
    # check if both instances are equal
    assert config == config2
    # check if they are different from the Display instance
    assert display != config
    assert display != config2

# Generated at 2022-06-13 16:55:40.797410
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class A(object):
        __metaclass__ = Singleton

    a = A()
    a1 = A()
    assert a == a1
    assert a is a1
    assert id(a) == id(a1)

    a.x = 5
    assert a1.x == 5


# Generated at 2022-06-13 16:55:47.226829
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs

    a1 = A(1, x=3)
    a2 = A(2, y=4)

    assert(a1 is a2)

    assert(a1.args == (1,))
    assert(a1.kwargs == {'x': 3})
    assert(a2.args == (1,))
    assert(a2.kwargs == {'x': 3})

# Generated at 2022-06-13 16:55:51.518683
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    test1 = Test()
    test2 = Test()

    assert test1 is test2


# Generated at 2022-06-13 16:55:53.988428
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Sample(object):
        __metaclass__ = Singleton

    s1 = Sample()
    s2 = Sample()

    assert s1 is s2, "Singleton class Sample returned different objects."


# Generated at 2022-06-13 16:55:56.356566
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
    a1 = A()
    a2 = A()
    assert a1 is a2
    b1 = A()
    assert b1 is a1


# Generated at 2022-06-13 16:56:00.130090
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 1

    a = A()
    assert a.value == 1

    a2 = A()
    assert a2 is a

    a2.value = 2
    assert a2.value == 2
    assert a.value == 2




# Generated at 2022-06-13 16:56:16.192452
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A():
        __metaclass__ = Singleton
    assert A() is A()
    class B():
        __metaclass__ = Singleton
    assert B() is B()
    assert A() is not B()


# Generated at 2022-06-13 16:56:23.906609
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        def __init__(self):
            self.x = "test"

    class SingletonTest1(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = "test"

    class SingletonTest2(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = "test"

    assert SingletonTest() is not SingletonTest()
    assert SingletonTest1() is SingletonTest1()
    assert SingletonTest2() is SingletonTest2()

# Generated at 2022-06-13 16:56:25.685368
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.i = 0

    a = MySingleton()
    b = MySingleton()

    assert(a == b)
    assert(a is b)

# Generated at 2022-06-13 16:56:32.325158
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test1(object, metaclass=Singleton):
        pass

    class Test2(object, metaclass=Singleton):
        def __init__(self):
            self.a = 0

        def test(self):
            return self.a

    class Test3(object, metaclass=Singleton):
        pass

    # Test when no arguments are passed
    instance1 = Test1()
    instance2 = Test1()
    assert instance1 is instance2

    # Test when an argument is passed
    instance3 = Test2()
    instance4 = Test2()
    assert instance3 is instance4
    assert instance3.test() == instance4.test()

    # Test when two arguments are passed
    instance5 = Test3(1, 2)
    instance6 = Test3(1, 2)
    assert instance5 is instance