

# Generated at 2022-06-13 16:46:39.267296
# Unit test for constructor of class Singleton
def test_Singleton():
    obj = Singleton()
    # should not be allowed to instantiate the metaclass
    try:
        obj2 = Singleton()
    except:
        assert True
    else:
        assert False


# Generated at 2022-06-13 16:46:46.728656
# Unit test for constructor of class Singleton
def test_Singleton():
    class Bar(object):
        __metaclass__ = Singleton
        def __init__(self, val=None):
            self.val = val
        def getVal(self):
            return self.val
        def setVal(self, val):
            self.val = val

    # Create first instance of Bar, set the value
    b1 = Bar()
    b1.setVal('test')

    # Create second instance of Bar, get the value
    b2 = Bar()
    assert b2.getVal() == 'test'

# Generated at 2022-06-13 16:46:50.124772
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
    assert A() == A()

# Generated at 2022-06-13 16:46:57.201077
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x

    a = A(3)
    assert a.x == 3

    b = A(4)
    assert b.x == 3

# We can not use the usual ansible_unittest.TestCase here because we
# need to see if a singleton class actually creates a singleton.  The
# ansible_unittest.TestCase code is not going to be rerun, so any test
# harness based on it will not get valid results.
test_Singleton()

# Generated at 2022-06-13 16:47:01.023153
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TmpClass(object):
        __metaclass__ = Singleton
        ''' Class for Unit test for method __call__ of class Singleton '''
        def __init__(self, y):
            self.x = y

    tc1 = TmpClass(5)
    assert(tc1.x == 5)

    tc2 = TmpClass(7)
    assert(tc2.x == 5)



# Generated at 2022-06-13 16:47:05.199349
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'A'

    a1 = A()
    a2 = A()
    assert a1 == a2



# Generated at 2022-06-13 16:47:09.722906
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class MyClass(object):
        __metaclass__ = Singleton

    # Instantiate MyClass 
    instance1 = MyClass()

    # Instantiate MyClass again
    instance2 = MyClass()

    # The two instances are the same
    assert( instance1 == instance2 )

# Generated at 2022-06-13 16:47:15.005235
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class singleton(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    s1 = singleton(1)
    s2 = singleton(2)
    assert s1.value == s2.value == 1


# Generated at 2022-06-13 16:47:22.999484
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 0
        def addX(self):
            self.x = self.x + 1

    obj1 = SingletonTest()
    obj2 = SingletonTest()
    obj1.addX()
    obj2.addX()
    assert(obj1.x == 2)
    assert(obj1 is obj2)

    class SingletonTest2(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x
        def addX(self):
            self.x = self.x + 1

    obj1 = SingletonTest2(1)
    obj2 = SingletonTest2(2)
    obj1.addX()
   

# Generated at 2022-06-13 16:47:27.307747
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.x = "hello"

    s = TestSingleton()
    assert isinstance(s, TestSingleton)
    assert s.x == "hello"
    s = TestSingleton()
    assert s.x == "hello"

# Generated at 2022-06-13 16:47:32.602883
# Unit test for constructor of class Singleton
def test_Singleton():
    class test1(metaclass=Singleton):
        def __init__(self, a):
            self.a = a
    class test2(metaclass=Singleton):
        def __init__(self, a):
            self.a = a
    t = test1('abc')
    u = test1('def')
    assert t.a == 'abc'
    assert u.a == 'abc'
    v = test2('ghi')
    assert t.a == 'abc'
    assert u.a == 'abc'
    assert v.a == 'ghi'

# Generated at 2022-06-13 16:47:38.145184
# Unit test for constructor of class Singleton
def test_Singleton():
    class test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 1

    a = test()
    n = 1
    while n < 10:
        b = test()
        assert id(b) == id(a)
        n += 1
    print("SUCCESS")


# test_Singleton()

# Generated at 2022-06-13 16:47:41.469267
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    a1 = A()
    a2 = A()
    assert a1 == a2



# Generated at 2022-06-13 16:47:45.852205
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingle(object):
        __metaclass__ = Singleton

    md1 = MySingle()
    md2 = MySingle()
    assert md1 is md2

test_Singleton.unittest = ['.meta']

if __name__ == "__main__":
    import run_tests
    run_tests.main([__file__])

# Generated at 2022-06-13 16:47:49.032293
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object, metaclass=Singleton):
        pass
    obj1 = TestSingleton()
    obj2 = TestSingleton()
    assert obj1 is obj2

# Generated at 2022-06-13 16:47:52.404438
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

    # Init
    a = SingletonTest()

    # Test
    b = SingletonTest()

    # Assert
    assert (a is b)

# Generated at 2022-06-13 16:47:56.413152
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    assert a is A()
    assert id(a) == id(A())

# Simple singleton class

# Generated at 2022-06-13 16:47:58.584498
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(metaclass=Singleton):
        pass
    assert isinstance(Test(), Test)
    assert Test() == Test()

# Generated at 2022-06-13 16:48:03.724430
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a, b):
            self.a = a
            self.b = b

    a = A(1, 2)
    assert a.a == 1
    assert a.b == 2
    a1 = A(3, 4)
    assert a1.a == 1
    assert a1.b == 2

    with pytest.raises(TypeError) as excinfo:
        a1 = A()
    assert '__init__()' in str(excinfo.value)

# Generated at 2022-06-13 16:48:05.748238
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    '''
        Test that __call__ of the Singleton class correctly returns a single instance of the subclass.
    '''
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, a):
            self.a = a
    assert id(TestClass(1)) == id(TestClass(1))



# Generated at 2022-06-13 16:48:14.631239
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 1
            self.y = 2

    t1 = TestSingleton()
    t2 = TestSingleton()

    assert t1 == t2
    assert t1.x == t2.x == 1
    assert t1.y == t2.y == 2

    t1.x = 3
    assert t1.x == t2.x == 3



# Generated at 2022-06-13 16:48:20.448973
# Unit test for constructor of class Singleton
def test_Singleton():

    class SingletonClass(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    instance1 = SingletonClass(1)
    instance2 = SingletonClass(2)

    assert instance1 == instance2
    assert instance1.value == 2
    assert instance2.value == 2

# Generated at 2022-06-13 16:48:23.601899
# Unit test for constructor of class Singleton
def test_Singleton():
    """
    >>> test = Singleton('test', (object,), {})
    >>> assert isinstance(test, Singleton)
    """



# Generated at 2022-06-13 16:48:29.056396
# Unit test for constructor of class Singleton
def test_Singleton():
    class Spam(object):
        __metaclass__ = Singleton
        def __init__(self, *args):
            self.args = args

    a = Spam('a')
    b = Spam('b')
    assert a == b
    assert a.args == ('a',)
    assert b.args == ('a',)

# Generated at 2022-06-13 16:48:33.398713
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from threading import Thread

    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    test = Test()
    t1 = Thread(target=Test)
    t2 = Thread(target=Test)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    assert test is Test() is Test()

# Generated at 2022-06-13 16:48:38.556569
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a

    a = A('a')
    assert a == A('b')
    assert a.a == 'a'

# Generated at 2022-06-13 16:48:42.728625
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class MyClass(metaclass=Singleton):
        """docstring for MyClass"""

        def __init__(self, a):
            self.a = a

    i1 = MyClass(3)
    i2 = MyClass(5)

    assert id(i1) == id(i2)
    assert i1.a == 5
    assert i2.a == 5

# Generated at 2022-06-13 16:48:46.556375
# Unit test for constructor of class Singleton
def test_Singleton():
    from Singleton import Singleton
    class Foo(object):
        __metaclass__ = Singleton

    a = Foo()
    b = Foo()

    if a is not b:
        raise ValueError("Error! Different instances are created!")

    print("Single instance created with two diffrent references")

# Generated at 2022-06-13 16:48:52.121101
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.foo = 0

    a = TestSingleton()
    assert a == TestSingleton()
    assert a.foo == 0

    a.foo = 1

    b = TestSingleton()
    assert a == b
    assert a.foo == b.foo == 1

# Generated at 2022-06-13 16:48:55.323429
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class test(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

        def __eq__(self, other):
            return True

    a = test()
    b = test()
    assert a == b

# Generated at 2022-06-13 16:49:01.284963
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    obj1 = TestClass()
    obj2 = TestClass()
    assert obj1 == obj2



# Generated at 2022-06-13 16:49:08.245831
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = '1'
            pass
    class B(A):
        def __init__(self):
            self.a = '2'
            pass
    assert id(A()) == id(A()) == id(B()) == id(B())


# Generated at 2022-06-13 16:49:10.736798
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    __test__ = {}   # for pytest

    # test
    class Foo(object):
        __metaclass__ = Singleton

    assert Foo() is Foo()
    assert Foo() is not None

# Generated at 2022-06-13 16:49:13.457949
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    assert foo1 is foo2


# Generated at 2022-06-13 16:49:21.708921
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.num = 0
        def __str__(self):
            return "num = %d"%(self.num)
    
    print("Testing ___call__ of class Singleton;")
    print("Creating instance of class A:")
    print("a = A()")
    a = A()
    print("a = %s"%str(a))
    print("Creating another instance of class A:")
    print("b = A()")
    b = A()
    print("a = %s"%str(a))
    print("b = %s"%str(b))
    print("Changing value of b.num to be 1:")
    print("b.num = 1")
    b.num = 1

# Generated at 2022-06-13 16:49:25.856454
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    a1 = A()
    a2 = A()
    assert a1 == a2

# Generated at 2022-06-13 16:49:28.660574
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(metaclass=Singleton):
        pass

    instance1 = SingletonTest()
    instance2 = SingletonTest()

    assert instance1 is instance2
    assert type(instance1) is type(instance2)

# Generated at 2022-06-13 16:49:31.273463
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass
        def foo(self):
            return 'foo'

    a1 = A()
    a2 = A()

    print(id(a1), id(a2))
    print(a1.foo())
    print(a2.foo())

#test_Singleton()

# Generated at 2022-06-13 16:49:35.068647
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    a = TestSingleton()
    b = TestSingleton()
    assert id(a) == id(b)


# Generated at 2022-06-13 16:49:37.897390
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class S(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    s1 = S()
    s2 = S()
    assert(s1 == s2)



# Generated at 2022-06-13 16:49:46.444035
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest

    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 0

        def set_value(self, value):
            self.value = value

        def get_value(self):
            return self.value

    class TestSingleton(unittest.TestCase):
        def test_same_instance(self):
            obj = MyClass()
            self.assertTrue(obj, MyClass())

        def test_same_value(self):
            obj = MyClass()
            obj.set_value(666)
            self.assertEqual(obj.get_value(), MyClass().get_value())

    unittest.main()

# Generated at 2022-06-13 16:49:48.238269
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    a = Test()
    assert a == Test()

# Generated at 2022-06-13 16:49:52.519668
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, val):
            self.__val = val
        def __str__(self):
            return str(self.__val)

    a = Test(4)
    b = Test(5)

    assert a is b
    assert str(a) == '4'
    assert str(b) == '4'

# Generated at 2022-06-13 16:50:00.587964
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass:
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 1

    m = MyClass()

    # test that m is the same object as m2
    m2 = MyClass()
    assert m2 == m

    # test that m is a MyClass object
    assert isinstance(m, MyClass)

    # test the value of m
    assert m.a == 1


test_Singleton()

# Generated at 2022-06-13 16:50:05.330253
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Unit test for method __call__ of class Singleton

    class MySingleton(object):
        __metaclass__ = Singleton

    # Test initialization
    o1 = MySingleton()
    assert o1, "FAIL"

    # Test that it's a singleton
    o2 = MySingleton()
    assert o2, "FAIL"
    assert o1 is o2, "FAIL"



# Generated at 2022-06-13 16:50:10.963254
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton:
        __metaclass__ = Singleton

        def __init__(self):
            pass

    t1 = TestSingleton()
    t2 = TestSingleton()
    assert (t1 == t2), "The same instance should be returned"

# Generated at 2022-06-13 16:50:15.639800
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 0

    t1 = Test()
    t2 = Test()
    t3 = Test()
    assert t1 is t2
    assert t2 is t3
    t1.a = 1
    assert t1.a == 1
    assert t2.a == 1
    assert t3.a == 1

# Generated at 2022-06-13 16:50:26.070866
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    __instance = None
    __rlock = RLock()
    def __init__(cls, name, bases, dct):
        super(Singleton, cls).__init__(name, bases, dct)
        cls.__instance = None
        cls.__rlock = RLock()

    def __call__(cls, *args, **kw):
        if cls.__instance is not None:
            return cls.__instance

        with cls.__rlock:
            if cls.__instance is None:
                cls.__instance = super(Singleton, cls).__call__(*args, **kw)

        return cls.__instance
    return __instance, __rlock

# Generated at 2022-06-13 16:50:33.703137
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyType(metaclass=Singleton):
        def __init__(self):
            if not hasattr(self, 'data'):
                self.data = []

        def add(self, data):
            self.data.append(data)

    # Create the first MyType instance
    myt1 = MyType()
    # Create the second MyType instance
    myt2 = MyType()

    # Add data to myt1
    myt1.add('myt1')
    # Add data to myt2
    myt2.add('myt2')

    # Now, only myt1 and myt2 are instances of MyType
    assert isinstance(myt1, MyType)
    assert isinstance(myt2, MyType)

    # Now, myt1 and myt2 are the same object


# Generated at 2022-06-13 16:50:36.477888
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()

    assert a1 is a2


# Generated at 2022-06-13 16:50:47.804998
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    class _Rosetta(AnsibleUnsafeText):
        __metaclass__ = Singleton

        def __init__(self, word):
            super(_Rosetta, self).__init__(word)

    stone = _Rosetta("stone")
    stone_copy = _Rosetta("stone")
    assert stone is stone_copy
    assert id(stone) == id(stone_copy)
    assert isinstance(stone, AnsibleUnsafeText)

    pyramide = _Rosetta("pyramide")
    pyramide_copy = _Rosetta("pyramide")
    assert pyramide is pyramide_copy
    assert id(pyramide) == id(pyramide_copy)

# Generated at 2022-06-13 16:50:51.995798
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    tc1 = TestClass("abc")
    tc2 = TestClass("def")

    assert tc1.value == "abc"
    assert tc2.value == "abc"
    assert tc1 is tc2

# Generated at 2022-06-13 16:50:55.704856
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

    foo1 = MyClass()
    foo2 = MyClass()

    assert foo1 is foo2

# Generated at 2022-06-13 16:51:04.643379
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Myclass(object):
        __metaclass__ = Singleton

        PARAM = None

        def __init__(self, name):
            self.__name = name

        @property
        def name(self):
            return self.__name

    class1 = Myclass('class1')
    class2 = Myclass('class2')

    assert class1.name ==  'class1'
    assert class1 == class2

from ansible.utils.color import stringc
from ansible.module_utils._text import to_text, to_native

from ansible_collections.community.general.plugins.module_utils.compat import ipaddress

from ansible_collections.notstdlib.moveitallout.plugins.module_utils.parsing.convert_bool import BOOLEANS_TRUE

# Generated at 2022-06-13 16:51:08.763945
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    TestSingleton1 = TestSingleton()
    TestSingleton2 = TestSingleton()

    assert TestSingleton1 is TestSingleton2

# Generated at 2022-06-13 16:51:15.005811
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from collections import namedtuple
    from threading import Thread
    from time import sleep

    class ThreadObject(object):
        """An object which has its own thread for execution."""
        def __init__(self, obj_name, timeout=30000):
            """Init variables and create the thread."""
            self.obj_name = obj_name
            self.thread = Thread(target=self.run)
            self.timeout = timeout

        def start(self):
            """Start thread object."""
            self.thread.start()

        def run(self):
            """Get the Singleton."""
            while self.timeout > 0:
                SingletonInstance.id('TEST')
                sleep(1)
                self.timeout -= 1

    class SingletonInstance(namedtuple('SingletonInstance', [])):
        __metaclass

# Generated at 2022-06-13 16:51:19.495930
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    print('Testing Singleton.__call__()')

    class TestSingleton(object):
        __metaclass__ = Singleton

    t1 = TestSingleton()
    t2 = TestSingleton()

    if t1 is not t2:
        raise AssertionError('Singleton.__call__() test failed')


# Generated at 2022-06-13 16:51:20.653170
# Unit test for constructor of class Singleton
def test_Singleton():
    from unittest import T

# Generated at 2022-06-13 16:51:22.682349
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()
    assert(foo1 is foo2)



# Generated at 2022-06-13 16:51:28.901982
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, x):
            self.x = x

    tc1 = TestClass(1)
    tc2 = TestClass(2)

    assert(tc1 is tc2)
    assert(tc1.x == 1)
    assert(tc2.x == 1)

# Generated at 2022-06-13 16:51:35.752301
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    f1 = Foo()
    f2 = Foo()
    # First time call should create new instance
    assert f1 is not None
    # Second time call should return the same instance
    assert f1 is f2


# Generated at 2022-06-13 16:51:42.334638
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        def __init__(self):
            self.a = 10
            self.b = 20

    # First instance
    assert(TestClass.__instance is None)
    o1 = TestClass()
    assert(isinstance(o1, TestClass))
    assert(TestClass.__instance is o1)

    o2 = TestClass()
    assert(o1 is o2)
    assert(TestClass.__instance is o1)

    assert(o1.a == 10)
    assert(o1.b == 20)
    assert(o2.a == 10)
    assert(o2.b == 20)



# Generated at 2022-06-13 16:51:45.052614
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

    c1 = MyClass()
    c2 = MyClass()
    assert c1 == c2


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:51:47.556175
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    # Test instance
    obj_1 = Test()
    obj_2 = Test()
    assert obj_1 is obj_2

# Generated at 2022-06-13 16:51:51.066932
# Unit test for constructor of class Singleton
def test_Singleton():
	class Singleton_Tester(object):
		__metaclass__ = Singleton

	singleton = Singleton_Tester()

	assert singleton == Singleton_Tester()
	assert singleton is Singleton_Tester()
	assert not (singleton != Singleton_Tester())
	assert not (singleton is not Singleton_Tester())


# Generated at 2022-06-13 16:51:58.776737
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class S(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.num = 0

    class S2(object):
        __metaclass__ = Singleton

    # get the singleton instance
    s = S()
    s.num = 10
    assert s.num == 10
    s2 = S()
    assert s2.num == 10
    assert s == s2
    s3 = S2()
    assert s != s3
    try:
        s4 = S2()
    except TypeError:
        pass
    else:
        raise AssertionError('Singleton cannot be instantiated twice')

# Generated at 2022-06-13 16:52:02.282970
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Create a mock class and then create two instances.
    class Mock(metaclass=Singleton):
        def __init__(self):
            self.a = 0
    instance1 = Mock()
    instance2 = Mock()
    assert instance1 is instance2

# Generated at 2022-06-13 16:52:05.265172
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        pass

    class B(object):
        __metaclass__ = Singleton
        pass

    assert A() is A()
    assert B() is B()
    assert A() is not B()


# Generated at 2022-06-13 16:52:08.158392
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
    a = Test()
    assert a is Test()


# Generated at 2022-06-13 16:52:10.689044
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class S(object):
        __metaclass__ = Singleton

    s1 = S()
    s2 = S()

    assert s1 is s2


# Generated at 2022-06-13 16:52:23.709741
# Unit test for constructor of class Singleton
def test_Singleton():
    # Create a new class that implements Singleton
    class SingletonTestMetaclass(metaclass=Singleton):
        """This is a dummy class that uses Singleton MetaClass.
        """
        def __init__(self, foo):
            self.__foo = foo

        # should be print out 1
        def get_foo(self):
            return self.__foo

    # Test if classes that implement Singleton MetaClass
    class1 = SingletonTestMetaclass(1)
    class2 = SingletonTestMetaclass(2)

    # Test if both class1 and class2 are equal
    assert class1 is class2
    assert class1.get_foo() == 1
    assert class2.get_foo() == 1
    assert class1.get_foo() == class2.get_foo()


# Generated at 2022-06-13 16:52:31.748306
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self, one, two, three=None):
            self.one = one
            self.two = two
            self.three = three
    class MyClass2(object):
        __metaclass__ = Singleton
        def __init__(self, one, two, three=None):
            self.one = one
            self.two = two
            self.three = three

    assert MyClass(1, 2) == MyClass(1, 2)
    assert MyClass2(1, 2) != MyClass2(1, 3)

# Generated at 2022-06-13 16:52:37.229860
# Unit test for constructor of class Singleton
def test_Singleton():
    class Singleton_Test:
        __metaclass__ = Singleton
        def __init__(self, singleton):
            self.singleton = singleton

    instance1 = Singleton_Test("singleton1")
    instance2 = Singleton_Test("singleton2")
    assert instance1.singleton == "singleton1"
    assert instance1 is instance2

# Generated at 2022-06-13 16:52:39.909404
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    a = TestSingleton()
    b = TestSingleton()
    assert id(a) == id(b)
    assert a == b

# Generated at 2022-06-13 16:52:45.556827
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test_sub_class = 'test_sub_class'

    test = Test()
    assert test.test_sub_class == 'test_sub_class'
    test_re = Test()
    assert test is test_re
    assert test_re.test_sub_class == 'test_sub_class'
    test_sub = test_re.__class__()
    assert test_sub is not test_re

# Generated at 2022-06-13 16:52:53.350231
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self, a, b):
            pass

    try:
        A(1, 2)
    except TypeError:
        # Can't call A directly - there should be only one instance of this
        # class.
        pass

    a = A.__call__(1, 2)
    b = A.__call__(1, 2)

    assert a is b
    assert type(a) is A
    assert type(b) is A

# Generated at 2022-06-13 16:53:00.316745
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 100
    class B(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 200
    class C(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 300

    a1 = A()
    a2 = A()
    assert a1 == a2
    assert a1.a == a2.a
    assert a1 is a2
    assert a1.a == 100

    b1 = B()
    b2 = B()
    assert b1 == b2
    assert b1.a == b2.a
    assert b1 is b2

# Generated at 2022-06-13 16:53:06.315751
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(metaclass=Singleton):
        def __init__(self):
            self._init_called_ = False

        def init(self):
            assert not self._init_called_
            self._init_called_ = True

    a = Foo()
    assert a == Foo()

    assert not a._init_called_
    a.init()
    assert a._init_called_
    b = Foo()
    assert b._init_called_

    # Make sure we test that someone cannot create a class that is a subclass of
    # a Singleton type.
    try:
        class bar(Foo):
            pass
        assert False
    except TypeError as e:
        assert "cannot create 'bar' because its base class " in str(e)

# Generated at 2022-06-13 16:53:13.893048
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            print("__init__ called")

    a = Test()
    a.i = 0
    b = Test()
    b.j = 1
    c = Test()
    print()
    print("a.i =", a.i)
    print("a.j =", getattr(a, 'j', None))
    print("b.i =", getattr(b, 'i', None))
    print("b.j =", b.j)
    print("c.i =", getattr(c, 'i', None))
    print("c.j =", getattr(c, 'j', None))


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:53:19.293887
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.tock = 1

    a = TestClass()
    assert a.tock == 1
    b = TestClass()
    assert a == b
    a.tock += 1
    assert a.tock == 2
    assert b.tock == 2

# Generated at 2022-06-13 16:53:40.425632
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass
    t = Test()
    assert t.__class__ == Test

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:53:42.758580
# Unit test for constructor of class Singleton
def test_Singleton():

    class TestA(object):
        __metaclass__ = Singleton

    class TestB(object):
        __metaclass__ = Singleton

    a1 = TestA()
    a2 = TestA()
    assert a1 is a2

    b1 = TestB()
    b2 = TestB()
    assert b1 is b2

    assert a1 is not b1

# Generated at 2022-06-13 16:53:44.671240
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()

    assert a is A()


# Used for testing

# Generated at 2022-06-13 16:53:47.530926
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object, metaclass=Singleton):
        def __init__(self):
            pass

    class B(object, metaclass=Singleton):
        def __init__(self):
            self.value = 10

    a = A()

# Generated at 2022-06-13 16:53:52.418016
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    # Test whether only one instance of the TestClass is created
    assert TestClass() is TestClass()

# Generated at 2022-06-13 16:53:56.489032
# Unit test for constructor of class Singleton
def test_Singleton():
    class ASingleton(object):
        __metaclass__ = Singleton

    a1 = ASingleton()
    a2 = ASingleton()
    assert a1 is a2

# Generated at 2022-06-13 16:54:03.578644
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class MyClass1(metaclass=Singleton):
        def __init__(self):
            pass

    class MyClass2(metaclass=Singleton):
        def __init__(self):
            pass

    obj1 = MyClass1()
    obj2 = MyClass1()
    obj3 = MyClass2()
    obj4 = MyClass2()

    assert obj1 is obj2
    assert obj3 is obj4
    assert obj1 is not obj3

# Generated at 2022-06-13 16:54:11.696111
# Unit test for constructor of class Singleton
def test_Singleton():
    import unittest
    class MySingletonClass(object):
        __metaclass__ = Singleton
        def __init__(self,a):
            self._a = a
        def get_a(self):
            return self._a
    myclass1 = MySingletonClass(1)
    myclass2 = MySingletonClass(2)
    class TestSingleton(unittest.TestCase):
        def setUp(self):
            self.cls = MySingletonClass(1)
        def test_init(self):
            self.assertIs(myclass1,myclass2)
            self.assertEqual(myclass1.get_a(),1)
            self.assertEqual(myclass2.get_a(),1)
        def tearDown(self):
            self.cls = None
    un

# Generated at 2022-06-13 16:54:17.098275
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 'test-value'

    test_instance = TestClass()

    # Check that we have a single instance
    assert test_instance is TestClass()

    # Check that the returned instances are equal
    assert test_instance == TestClass()

    # Check that the returned instances are not different
    assert id(test_instance) == id(TestClass())

    # Check that the value of the instance is kept
    assert test_instance.value == 'test-value'

# Generated at 2022-06-13 16:54:21.259416
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    class TestSingleton_Subclass(object):
        __metaclass__ = Singleton

    obj1 = TestSingleton()
    obj2 = TestSingleton()
    assert obj1 is obj2
    obj3 = TestSingleton_Subclass()
    obj4 = TestSingleton_Subclass()
    assert obj3 is obj4
    assert obj1 is not obj3

# Generated at 2022-06-13 16:54:57.783814
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    test1 = TestSingleton()
    test2 = TestSingleton()
    assert test1 is test2


if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:55:00.752525
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 10

    a1 = A()
    a2 = A()

    assert(a1 == a2)

# Generated at 2022-06-13 16:55:03.293013
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class S(object):
        __metaclass__ = Singleton
        x = 42
    s = S()
    s2 = S()
    assert s is s2
    assert s.x == 42
    s.x = 43
    assert s2.x == 43

__all__ = ["Singleton"]

# Generated at 2022-06-13 16:55:07.464939
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(Singleton):
        def __init__(self):
            self.a = 1
            self.b = 2

    o1 = TestSingleton()
    o2 = TestSingleton()
    assert o1 == o2
    assert o1.b == 2
    assert o2.a == 1
    o1.b = 5
    o2.a = 5
    assert o2.b == 5
    assert o1.a == 5

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:55:09.992256
# Unit test for constructor of class Singleton
def test_Singleton():
    class Testing(object):
        """Testing class for Singleton"""
        __metaclass__ = Singleton

        def __init__(self, name):
            self.name = name

    t1 = Testing('t1')
    t2 = Testing('t2')
    assert t1 is t2
    assert t1.name == 't2' and t2.name == 't2'

# Generated at 2022-06-13 16:55:15.353342
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(metaclass=Singleton):
        def __init__(self, x):
            self.x = x

    a = SingletonTest(1)
    b = SingletonTest(2)

    assert(a == b)
    assert(a is b)
    assert(a.x == b.x)

    # verify that the underlying __init__ was not actually called twice.
    assert(a.x == 1)
    assert(b.x == 1)

# Generated at 2022-06-13 16:55:20.252200
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object, metaclass=Singleton):
        pass

    class ChildSingleton(MySingleton):
        pass

    # Assert we can create multiple singletons that are not the same
    assert id(MySingleton()) != id(ChildSingleton())

    # Assert the same singleton is reused
    assert id(MySingleton()) == id(MySingleton())
    assert id(ChildSingleton()) == id(ChildSingleton())


test_Singleton()

# Generated at 2022-06-13 16:55:21.933485
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self, a):
            self.a = a

    assert A(1) == A(2)
    assert A(1).a == 1
    assert A(2).a == 1

# Generated at 2022-06-13 16:55:26.186468
# Unit test for constructor of class Singleton
def test_Singleton():
    from ansible.utils.singleton import Singleton
    class A(object):
        __metaclass__ = Singleton
    class B(object):
        __metaclass__ = Singleton

    assert A() is A()
    assert B() is B()
    assert A() is not B()

# Generated at 2022-06-13 16:55:34.138487
# Unit test for constructor of class Singleton
def test_Singleton():

    class S(Object):
        __metaclass__ = Singleton

        def __init__(self):
            self.res = 0

        def add(self,a,b):
            self.res = a + b
            return self.res

    s1 = S()
    s2 = S()
    assert id(s1) == id(s2)
    s1.add(1,2)
    assert s2.res == 3