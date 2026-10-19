

# Generated at 2022-06-13 16:46:39.640407
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    ins1 = TestSingleton()
    ins2 = TestSingleton()
    assert ins1 is ins2

# Generated at 2022-06-13 16:46:41.745660
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Testing(object):
        __metaclass__ = Singleton

    assert Testing() is Testing()


# Generated at 2022-06-13 16:46:48.465689
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingletonBase(with_metaclass(Singleton, object)):
        pass

    class TestSingleton(TestSingletonBase):
        pass

    class TestSingletonSub(TestSingleton):
        pass

    ts1 = TestSingleton()
    ts2 = TestSingleton()
    assert ts1 == ts2
    assert ts1 is ts2

    tss1 = TestSingletonSub()
    tss2 = TestSingletonSub()
    assert tss1 == tss2
    assert tss1 is tss2


# Generated at 2022-06-13 16:46:51.245703
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):

        __metaclass__ = Singleton

        def __init__(self, item='test'):
            self.item = item

    a = MySingleton('a')
    b = MySingleton('b')

    assert a.item == b.item == 'a'

# Generated at 2022-06-13 16:46:54.008388
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a
    t1 = TestSingleton(1)
    t2 = TestSingleton(2)
    assert t1.a == 1
    assert t2.a == 1

# Generated at 2022-06-13 16:46:58.147597
# Unit test for constructor of class Singleton
def test_Singleton():
    class dummy(object):
        __metaclass__ = Singleton
    d = dummy()
    print(d.__metaclass__.__instance)
    d1 = dummy()
    print(d1.__metaclass__.__instance)


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:47:01.470434
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert(a is b)

# Generated at 2022-06-13 16:47:03.705449
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class S(object):
        __metaclass__ = Singleton

    s1 = S()
    s2 = S()
    assert s1 is s2



# Generated at 2022-06-13 16:47:08.716351
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 10

        def __repr__(self):
            return "MySingleton(%r)" % self.a

    a = MySingleton()
    b = MySingleton()
    assert a is b
    assert repr(a) == repr(b)
    a.a = 20
    assert repr(a) == repr(b)

# Generated at 2022-06-13 16:47:16.825177
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.v = 0

    t1 = SingletonTestClass()
    t2 = SingletonTestClass()
    assert t1 is t2
    assert t1.v is t2.v
    assert t1.v == 0
    assert t2.v == 0

    t1.v = 1
    assert t1.v is t2.v
    assert t1.v == 1
    assert t2.v == 1

    t2.v = 2
    assert t1.v is t2.v
    assert t1.v == 2
    assert t2.v == 2

# Generated at 2022-06-13 16:47:24.969282
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test1(object):
        __metaclass__ = Singleton

    class Test2(object):
        __metaclass__ = Singleton

    assert Test1() is Test1()
    assert Test2() is Test2()
    assert Test1() is not Test2()

if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:47:34.224524
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x

    from threading import Thread

    results = {}

    def get_A(x):
        results[x] = A(x)

    for i in xrange(10):
        Thread(target=get_A, args=(i,)).start()

    # wait for all threads to finish
    from time import sleep
    sleep(2)


    # check that we have only one instance
    first_x = results[0].x
    for instance in results.values():
        assert first_x == instance.x


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:47:37.013798
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    assert id(Foo()) == id(Foo())

# Generated at 2022-06-13 16:47:47.172462
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        # This is a singleton class
        __metaclass__ = Singleton

        def __init__(self, name=''):
            self.name = name

    instance1 = MySingleton('foo')
    instance2 = MySingleton('bar')
    if instance1.name != 'foo' or instance2.name != 'foo':
        raise AssertionError()

    class MySingletonWithArgs(object):
        # This is a singleton class
        __metaclass__ = Singleton

        def __init__(self, name='', age=0):
            self.name = name
            self.age = age

    instance1 = MySingletonWithArgs('foo')
    instance2 = MySingletonWithArgs(age=123)

# Generated at 2022-06-13 16:47:54.114317
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.val = 10

    class MyClass2(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.val = 20

    a = MyClass()
    b = MyClass()
    c = MyClass2()

    # instance variables are independent
    assert a.val != b.val != c.val

    # MyClass and MyClass2 are independent
    assert a != b != c

# Generated at 2022-06-13 16:47:56.780756
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert a1 is a2


# Generated at 2022-06-13 16:48:01.339895
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value
    a1 = A(42)
    a2 = A(43)
    assert a1.value == 42 and a2.value == 42
    a2.value = 45
    assert a1.value == 45 and a2.value == 45


# Unit tests for class Singleton

# Generated at 2022-06-13 16:48:03.569325
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        @staticmethod
        def foo():
            return True

    a = A()
    b = A()

    assert a.foo() == b.foo()



# Generated at 2022-06-13 16:48:06.077358
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    a = Test()
    b = Test()
    assert (a is b)
    a.foo = 1
    b.bar = 2
    assert (a.foo == b.foo)
    assert (a.bar == b.bar)



# Generated at 2022-06-13 16:48:12.860632
# Unit test for constructor of class Singleton
def test_Singleton():
    """
    >>> from ansible.utils.singleton import *
    >>> class TestSingleton(object):
    ...    __metaclass__ = Singleton
    ...    def __init__(self):
    ...        self.test = 1
    ...
    >>> a = TestSingleton()
    >>> b = TestSingleton()
    >>> a.test
    1
    >>> b.test
    1
    >>> b.test = 2
    >>> a.test
    2
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:48:23.736146
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass
    class Bar(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass
    foo1 = Foo()
    foo2 = Foo()
    bar1 = Bar()
    bar2 = Bar()
    assert foo1 is foo2
    assert bar1 is bar2
    assert foo1 is not bar1
    assert foo1 is not bar2
    assert foo2 is not bar1
    assert foo2 is not bar2

# Generated at 2022-06-13 16:48:33.042547
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test_Singleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            #print "constructor called"
            self.state = 1

        def setState(self, state):
            self.state = state

        def getState(self):
            return self.state


    testS = Test_Singleton()
    testS.setState(2)
    print(testS.getState())

    testS1 = Test_Singleton()
    print(testS1.getState())
    testS1.setState(3)
    print(testS1.getState())

    print(testS.getState())

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:48:39.606874
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self, test_arg):
            self.test_arg = test_arg

    t1 = TestClass('test1')
    t2 = TestClass('test2')

    assert t1 is t2
    assert t1.test_arg == t2.test_arg == 'test1'


# Generated at 2022-06-13 16:48:42.804498
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class TestSingleton(object):
        __metaclass__ = Singleton

    # Create an instance of the class
    x = TestSingleton()

    # Assert that the instance is created only once
    assert id(x) == id(TestSingleton())



# Generated at 2022-06-13 16:48:45.980400
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()

    assert(a is b)
    assert(a is not None)
    assert(b is not None)


# Generated at 2022-06-13 16:48:49.168241
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
    
    a = A()
    b = A()
    assert a == b


# Generated at 2022-06-13 16:48:51.795747
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2



# Generated at 2022-06-13 16:48:56.227179
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, a=0):
            self.a = a
    assert A(1).a == 1
    assert A().a == 1
    assert A().a == A().a
    assert A(1).a == A().a
    assert A() == A()



# Generated at 2022-06-13 16:49:04.534312
# Unit test for constructor of class Singleton
def test_Singleton():
    import mock
    from ansible.config.singleton import Singleton

    mock_callback = mock.MagicMock()
    mock_callback.return_value = 42

    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self, callback):
            self.cb = callback

        def call_cb(self):
            return self.cb()

    test1 = TestClass(mock_callback)
    assert test1.call_cb() == 42

    test2 = TestClass(mock_callback)
    assert test1 == test2
    assert test2.call_cb() == 42

    mock_callback.assert_called_once_with()

# Generated at 2022-06-13 16:49:08.337339
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.initialized = True

    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2
    assert foo1.initialized
    assert foo2.initialized


from collections import defaultdict
import operator
from ansible.errors import AnsibleError



# Generated at 2022-06-13 16:49:14.783587
# Unit test for constructor of class Singleton
def test_Singleton():
    """Test that the Singleton constructor only instantiates one single
    class.
    """
    # pylint: disable=too-few-public-methods
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 0

    first = TestClass()
    second = TestClass()
    assert id(first) == id(second)
    assert first.foo == 0
    first.foo = 1
    assert first.foo == second.foo



# Generated at 2022-06-13 16:49:17.433526
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a
    s1 = S(1)
    s2 = S(2)
    assert s1 is s2
    assert s1.a == 1
    assert s2.a == 1



# Generated at 2022-06-13 16:49:17.956731
# Unit test for constructor of class Singleton
def test_Singleton():
    pass

# Generated at 2022-06-13 16:49:22.740211
# Unit test for constructor of class Singleton
def test_Singleton():
    class S1(object):
        __metaclass__ = Singleton
        def __init__(self):
            super(S1, self).__init__()
            self._a = True

    class S2(object):
        __metaclass__ = Singleton
        def __init__(self):
            super(S2, self).__init__()
            self._a = False

    # example test code
    assert (S1() is S1()) is True
    assert (S1() is S2()) is False


test_Singleton()

# Generated at 2022-06-13 16:49:25.503346
# Unit test for constructor of class Singleton
def test_Singleton():
	s = Singleton("name", "bases", "dct")

# Generated at 2022-06-13 16:49:26.229584
# Unit test for constructor of class Singleton

# Generated at 2022-06-13 16:49:30.033836
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # class Foo is a Singleton so Foo() always returns the same instance
    class Foo(object):
        __metaclass__ = Singleton

    f1 = Foo()
    f2 = Foo()
    assert f1 is f2

# Generated at 2022-06-13 16:49:34.393663
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest
    from six import add_metaclass

    class TestCase(unittest.TestCase):
        def test__call__(self):
            @add_metaclass(Singleton)
            class foo:
                pass

            bar = foo()
            self.assertEqual(bar, foo())

# Generated at 2022-06-13 16:49:37.722161
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1
    o = foo()
    o1 = foo()
    o.a = "hello"
    assert o1.a == "hello"



# Generated at 2022-06-13 16:49:41.229017
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Declare test class
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test = 1

        def add(self):
            self.test += 1
    # Test Singleton behavior
    assert TestSingleton().test == 1
    TestSingleton().add()
    assert TestSingleton().test == 2
    TestSingleton().test = 0
    assert TestSingleton().test == 0

# Generated at 2022-06-13 16:49:48.391112
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Create a subclass of Singleton
    class Test(object):
        __metaclass__ = Singleton

    # Attempt to instantiate singleton
    first_instance = Test()

    # Make sure we are getting the same instance
    second_instance = Test()
    assert first_instance is second_instance

# Generated at 2022-06-13 16:49:50.382026
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    a = TestSingleton()
    assert a == TestSingleton()

# Generated at 2022-06-13 16:49:55.965874
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class C(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 1

    a = C()
    b = C()
    assert a is b
    assert a.value == b.value

    a.value = 2
    assert a.value == b.value


# Generated at 2022-06-13 16:50:03.012385
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(metaclass=Singleton):
        def __init__(self):
            self.num = 0
        def inc(self):
            self.num += 1
    t1 = TestSingleton()
    t2 = TestSingleton()
    t1.inc()
    assert t1.num == 1
    assert t2.num == 1
    t2.inc()
    assert t1.num == 2
    assert t2.num == 2
    assert t1 is t2
    return True

# Generated at 2022-06-13 16:50:04.845265
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(metaclass=Singleton):
        pass

    a = TestSingleton()
    b = TestSingleton()

    assert a == b

# Generated at 2022-06-13 16:50:15.960284
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    from ansible.parsing.vault import VaultLib, VaultSecret

    class VaultLibForTest(VaultLib):
        __metaclass__ = Singleton

        def __init__(self, password=None, **kwargs):
            super(VaultLibForTest, self).__init__(password, **kwargs)

        # This method is copied from VaultLib class
        def encrypt(self, filename, data, **kwargs):
            # type: (str, str, **Any) -> Union[str, bytes]
            if not self.is_encrypted(filename, data):
                try:
                    with open(filename, 'r') as f:
                        old_data = f.read()
                except IOError:
                    old_data = u''

               

# Generated at 2022-06-13 16:50:19.312058
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object):
        __metaclass__ = Singleton
    assert S() is S()
    class T(object):
        __metaclass__ = Singleton
    assert T() is not S()



# Generated at 2022-06-13 16:50:26.070190
# Unit test for constructor of class Singleton
def test_Singleton():

    class SingletonClass(object):
        __metaclass__ = Singleton

    class AClass(SingletonClass):
        def __init__(self):
            self.a = 1
        def get_data(self):
            return self.a

    instance1 = AClass()
    instance2 = AClass()
    assert instance1 == instance2
    assert instance1.a == 1
    assert instance1.get_data() == 1

# Generated at 2022-06-13 16:50:27.942280
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(metaclass=Singleton):
        def __init__(self):
            self.bar = 'baz'

    foo1 = Foo()
    foo2 = Foo()

    assert foo1 is foo2
    assert foo1.bar == foo2.bar == 'baz'



# Generated at 2022-06-13 16:50:30.968218
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

    obj = MyClass()
    assert obj is MyClass()



# Generated at 2022-06-13 16:50:42.397078
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        # Singleton should be a metaclass
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a

        def get_a(self):
            return self.a

    # Create two instances
    singleton_a = A(1)
    singleton_b = A(2)

    # Check that their IDs are the same
    ids_are_the_same = id(singleton_a) == id(singleton_b)
    assert ids_are_the_same is True

    # Check that their values are the same
    values_are_the_same = singleton_a.a == singleton_b.a
    assert values_are_the_same is True

# Generated at 2022-06-13 16:50:46.646323
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(metaclass=Singleton):
        def __init__(self):
            self._elem = None
        def set_elem(self, value):
            self._elem = value
        @property
        def value(self):
            return self._elem

    a = TestSingleton()
    a.set_elem(5)
    b = TestSingleton()
    assert a.value == b.value == 5

# Generated at 2022-06-13 16:50:51.962016
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Class1(object):
        __metaclass__ = Singleton

    assert id(Class1()) == id(Class1())
    assert id(Class1()) == id(Class1())
    # test object method __call__
    assert id(Class1().__call__()) == id(Class1())
    assert id(Class1().__call__()) == id(Class1())



# Generated at 2022-06-13 16:50:54.277839
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    _a1 = A()
    _a2 = A()

    assert(_a1 == _a2)



# Generated at 2022-06-13 16:51:00.650637
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(metaclass=Singleton):
        pass

    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2

    class Bar(metaclass=Singleton):
        def __init__(self):
            self.a = 1

    bar1 = Bar()
    bar2 = Bar()
    assert bar1 is bar2
    assert bar1.a == 1
    assert bar2.a == 1

# Generated at 2022-06-13 16:51:03.336962
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(metaclass=Singleton):
        pass
    test_instance = TestSingleton()
    assert test_instance is TestSingleton()
    test_instance.foo = 'bar'
    assert TestSingleton().foo == 'bar'

# Generated at 2022-06-13 16:51:11.601265
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    global __singleton_count
    result = []
    __singleton_count = 0

    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self):
            global __singleton_count
            result.append(__singleton_count)
            __singleton_count += 1

    a = SingletonTest()
    b = SingletonTest()
    assert a is b
    assert [__singleton_count, 0] == result



# Generated at 2022-06-13 16:51:20.572069
# Unit test for constructor of class Singleton
def test_Singleton():
    """Test constructor of class Singleton"""
    from ansible.utils.singleton import Singleton

    class TestSingleton:
        """Class TestSingleton with Metaclass Singleton"""
        __metaclass__ = Singleton

        def __init__(self):
            self.id = 0

        def set_id(self, idn):
            self.id = idn

        def get_id(self):
            return self.id

    test = TestSingleton()
    test.set_id(1)
    assert test.get_id() == 1

    test1 = TestSingleton()
    assert test1.get_id() == 1

# Generated at 2022-06-13 16:51:23.539270
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    ts1 = TestSingleton()
    ts2 = TestSingleton()
    assert ts1 is ts2
    ts3 = TestSingleton()
    assert ts3 is ts2

# Generated at 2022-06-13 16:51:27.885302
# Unit test for constructor of class Singleton
def test_Singleton():
    class SomeClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 10

    a = SomeClass()
    b = SomeClass()

    assert a.x == b.x

# Generated at 2022-06-13 16:51:39.690299
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test1(object):
        __metaclass__ = Singleton

    class Test2(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 'bar'

    assert Test1() == Test1()
    assert Test2() == Test2()

    instance = Test2()
    assert instance.foo == 'bar'


# Generated at 2022-06-13 16:51:43.377439
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Simple(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 5

    a = Simple()
    b = Simple()

    assert a is b
    assert a.x == 5



# Generated at 2022-06-13 16:51:49.754626
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class test(object):
        def __init__(self, a):
            self.a = a

    class test_single(test):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a

    t1_1 = test(1)
    t1_2 = test(2)
    t2_1 = test_single(1)
    t2_2 = test_single(2)

    assert t1_1.a != t1_2.a
    assert t2_1.a != t2_2.a
    assert t2_1 == t2_2


# Generated at 2022-06-13 16:51:52.147801
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        pass

    class B(A):
        pass

    # Test metaclass
    a_inst = A()
    b_inst = B()

    assert a_inst == b_inst
    assert a_inst is b_inst

# Generated at 2022-06-13 16:51:53.941334
# Unit test for constructor of class Singleton
def test_Singleton():
    assert Singleton.__call__ is Singleton.__call__


# Generated at 2022-06-13 16:51:57.923760
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x

    a = TestSingleton(1)
    b = TestSingleton(2)
    assert a.x == 1
    assert b.x == 1

test_Singleton___call__.__test__ = False



# Generated at 2022-06-13 16:52:00.390712
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """
    Tests Singleton.__call__
    """

    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.s = 'hello world'

    assert A().s == 'hello world'
    a = A()
    assert a.s == 'hello world'
    assert A() is a
    assert A() is a



# Generated at 2022-06-13 16:52:02.802361
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    assert Test() == Test()
    assert Test.__instance is not None

# Generated at 2022-06-13 16:52:09.486407
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, data = None):
            try:
                self.__data
            except AttributeError:
                self.__data = data

        def test(self, data = None):
            self.__data = data

    class B(object):
        __metaclass__ = Singleton

        def __init__(self, data = None):
            try:
                self.__data
            except AttributeError:
                self.__data = data

        def test(self, data = None):
            self.__data = data

    a = A()
    b = B()

    a.test("test1")
    b.test("test2")

    assert a.__data == "test1"

# Generated at 2022-06-13 16:52:18.709565
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    def test_equal_to_same():
        a = TestSingleton()
        a2 = TestSingleton()
        assert a is a2

    def test_equal_to_same_arg():
        a = TestSingleton()
        a2 = TestSingleton()
        assert a is a2

    def test_equal_to_diff():
        class TestSingleton2(object):
            __metaclass__ = Singleton

        a = TestSingleton()
        a2 = TestSingleton2()
        assert a is not a2

    def test_equal_to_diff_arg():
        class TestSingleton2(object):
            __metaclass__ = Singleton

        a = TestSingleton()
        a2 = TestSingleton2()


# Generated at 2022-06-13 16:52:37.839232
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self, val):
            self.val = val

    inst1 = Test(10)
    inst2 = Test(20)

    assert inst1.val == 10
    assert inst2.val == 10
    assert inst1 is inst2

# Generated at 2022-06-13 16:52:40.025044
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 11
    assert Test() is Test()



# Generated at 2022-06-13 16:52:45.066427
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self, a, b):
            self.a = a
            self.b = b

    obj1 = Foo(1, 2)
    obj2 = Foo(3, 4)
    assert obj1 == obj2
    assert obj1.a == 1
    assert obj2.b == 2

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:52:49.611591
# Unit test for constructor of class Singleton
def test_Singleton():

    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def value(self):
            return self.x, self.y

    a = SingletonTest(1,2)

    b = SingletonTest(3,4)

    assert a is b
    assert a.value() == (1,2)


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:52:55.799614
# Unit test for constructor of class Singleton
def test_Singleton():
    try:
        class TestSingleton(object):
            __metaclass__ = Singleton

            def __init__(self):
                raise ValueError("This is a test.")

        TestSingleton()
    except ValueError as e:
        assert isinstance(e, ValueError)

    try:
        class TestSingleton(object):
            __metaclass__ = Singleton

            def __init__(self):
                pass

    except ValueError as e:
        assert not isinstance(e, ValueError)

    assert TestSingleton() == TestSingleton()

# Generated at 2022-06-13 16:52:57.508199
# Unit test for constructor of class Singleton
def test_Singleton():
    class foo(object):
        __metaclass__ = Singleton

    class bar(object):
        __metaclass__ = Singleton

    foo1 = foo()
    foo2 = foo()
    bar1 = bar()
    bar2 = bar()
    assert foo1 is foo2
    assert bar1 is bar2

# Generated at 2022-06-13 16:53:03.714926
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(metaclass=Singleton):
        def __init__(self):
            self.name = 'test'

    test1 = TestSingleton()
    assert test1.name == 'test'

    test2 = TestSingleton()
    assert test2 is test1
    assert test2.name == 'test'

# Generated at 2022-06-13 16:53:08.188247
# Unit test for constructor of class Singleton
def test_Singleton():
    class Dummy(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 10

    # Create two instances of class Dummy
    dummy1 = Dummy()
    dummy2 = Dummy()

    # Check if it is the same object
    assert dummy1 is dummy2

    dummy1.x = 20
    assert dummy2.x == 20

# Generated at 2022-06-13 16:53:11.157588
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 'a'

    a_obj = A()

    assert a_obj.a == 'a', "Singleton class doesn't work"

# Generated at 2022-06-13 16:53:14.806160
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton

    singleton_obj = MySingleton()
    assert singleton_obj == MySingleton()
    assert singleton_obj.__doc__ == MySingleton.__doc__


# Generated at 2022-06-13 16:53:50.345272
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # __init__ creates an instance of class A.  The instance is stored as
    # __instance.  When trying to instantiate another object of class A, it
    # is discovered that __instance is set.  So, the original instance of
    # class A is returned instead.
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.foo = 1

    a = A()
    b = A()
    c = A()

    assert a is b is c

# Generated at 2022-06-13 16:53:53.153891
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    t1 = Test()
    t2 = Test()
    assert t1 == t2

# Generated at 2022-06-13 16:54:02.630736
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

    class MySingleton2(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    import pytest
    mys1 = MySingleton()
    mys2 = MySingleton()
    mys3 = MySingleton2()
    mys4 = MySingleton2(stuff="True")
    assert mys1 is mys2
    assert mys3 is not mys4
    with pytest.raises(TypeError):
        mys4 = MySingleton2()

# Generated at 2022-06-13 16:54:08.213627
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(metaclass=Singleton):
        def __init__(self, a):
            self.a = a

    A = MyClass(5)
    B = MyClass(10)
    assert A.a == 5
    assert B.a == 5
    assert A == B
    assert id(A) == id(B)


# Generated at 2022-06-13 16:54:14.122155
# Unit test for constructor of class Singleton
def test_Singleton():
    class Single(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 0
            self.b = 0

    obj1 = Single()
    obj2 = Single()

    obj1.a = 1
    obj1.b = 2

    obj2.a = 3
    obj2.b = 4

    assert(obj1.a == obj2.a)
    assert(obj1.b == obj2.b)
    assert(obj1 is obj2)

    print("test_Singleton() completed")

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:54:16.715294
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    a = TestSingleton()
    b = TestSingleton()
    assert a is b

# Generated at 2022-06-13 16:54:19.758015
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Unit test for method __call__ of class Singleton."""

    class TestClass(metaclass=Singleton):
        def __init__(self):
             self.foo = 1

    instance1 = TestClass()
    instance2 = TestClass()

    assert instance1 is instance2
    assert instance1.foo == 1
    assert instance2.foo == 1

# Generated at 2022-06-13 16:54:22.639803
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    a1 = Test()
    a2 = Test()
    assert id(a1) == id(a2)

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:54:23.730865
# Unit test for constructor of class Singleton
def test_Singleton():
    class C(metaclass=Singleton):
        pass

    assert C() is C()

# Generated at 2022-06-13 16:54:26.479211
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestFoo(object):
        __metaclass__ = Singleton

    a = TestFoo()
    b = TestFoo()
    assert a is b

# Generated at 2022-06-13 16:55:34.823981
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Bar(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.data = 0

    instance1 = Bar()
    instance1.data = 1

    instance2 = Bar()
    instance2.data = 2

    assert(instance1.data == instance2.data)

# Generated at 2022-06-13 16:55:36.707893
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        pass

    a = A()
    b = A()
    assert(a is b)



# Generated at 2022-06-13 16:55:46.683918
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Singleton_test(object):
        __metaclass__ = Singleton

        def __init__(self, param=None):
            self.param = param

    class Singleton_test2(object):
        __metaclass__ = Singleton

        def __init__(self, param=None):
            self.param = param

    assert Singleton_test()
    assert Singleton_test2()

    assert id(Singleton_test()) == id(Singleton_test())
    assert id(Singleton_test2()) == id(Singleton_test2())

    assert id(Singleton_test()) != id(Singleton_test2())

    assert Singleton_test(1)
    assert Singleton_test2(1)

    assert id(Singleton_test(1)) == id(Singleton_test(1))
   

# Generated at 2022-06-13 16:55:51.798394
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from lib.singleton import Singleton

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1

    assert TestSingleton() == TestSingleton()
    assert TestSingleton().a == 1



# Generated at 2022-06-13 16:55:54.052290
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    assert foo() is foo()


# Generated at 2022-06-13 16:55:59.186658
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    # All instances of MyClass will return the same value, as MyClass
    # has only a single instance.
    inst1 = MyClass(1)
    inst2 = MyClass(1)
    assert inst1 is inst2

# Generated at 2022-06-13 16:56:03.186734
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, foo, bar=None):
            self.foo = foo
            self.bar = bar

    test0 = TestSingleton("foo")
    test1 = TestSingleton("bar")
    test2 = TestSingleton("bar")
    test3 = TestSingleton("foo")

    assert test0 is test1
    assert test1 is test2
    assert test2 is test3


# Generated at 2022-06-13 16:56:07.376573
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class DummySingleton(object):
        __metaclass__ = Singleton
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2
    d1 = DummySingleton("value1", "value2")
    d2 = DummySingleton("value3", "value4")
    assert d1.arg1 == "value1"
    assert d1.arg2 == "value2"
    assert d1 == d2

test_Singleton___call__()

# Generated at 2022-06-13 16:56:11.042125
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        def __init__(self, msg):
            self.msg = msg

        def __str__(self):
            return self.msg

    a = TestClass('Hello, World!')
    b = TestClass('Hello, World!')
    print(a)
    assert a == b


# Generated at 2022-06-13 16:56:13.539717
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    a3 = A()

    assert id(a1) == id(a2) == id(a3)