

# Generated at 2022-06-13 16:46:33.241833
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
    assert A() is A()


# Generated at 2022-06-13 16:46:44.602882
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self, val):
            self._val = val

        def __repr__(self):
            return unicode(self._val)

    # test_1 __call__ return a new Test instance
    test1 = Test(1)
    assert(isinstance(test1, Test))

    # test_2 __call__ return the same Test instance
    test2 = Test(1)
    assert(test1 is test2)

    # test_3 __call__ return the same Test instance
    test3 = Test(2)
    assert(test1 is test2 is test3)



# Generated at 2022-06-13 16:46:47.771732
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(metaclass=Singleton):
        def __init__(self):
            pass
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2
    assert id(m1) == id(m2)

test_Singleton()

# Generated at 2022-06-13 16:46:53.543754
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self, test):
            self.test = test
            print('initialization')

    a = MySingleton('test')
    print(a.test)
    b = MySingleton('test')
    print(a is b)  # True

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:46:55.358733
# Unit test for constructor of class Singleton
def test_Singleton():

    s = Singleton('test',(object,),{})
    assert issubclass(s,object)

# Generated at 2022-06-13 16:46:59.529421
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    class Bar(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    foo = Foo()
    bar = Bar()

    assert foo == Foo()
    assert bar == Bar()
    assert foo != bar
    assert Bar() != Foo()



# Generated at 2022-06-13 16:47:01.889897
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            print('Test object')
    a = Test()
    assert ((a is Test()),'The instance created should be the instance returned')
    print ('Test constructor of class Singleton')


# Generated at 2022-06-13 16:47:04.232041
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    test_instance = TestSingleton()
    assert TestSingleton() == test_instance

# Generated at 2022-06-13 16:47:06.061402
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton
        pass
    
    one_instance = SingletonTest()
    assert one_instance is SingletonTest()
    assert one_instance is not SingletonTest() 

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:47:11.273191
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 1

    s1 = SingletonTest()
    s2 = SingletonTest()
    s2.value = 2

    assert s2.value == s1.value, "S1 value is not equal to S2 value"

# Generated at 2022-06-13 16:47:21.056629
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test1(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = "Test1"

    class Test2(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = "Test2"

    test1_instance1 = Test1()
    test1_instance2 = Test1()
    test2_instance1 = Test2()
    test2_instance2 = Test2()

    assert test1_instance1 is test1_instance2
    assert test2_instance1 is test2_instance2
    assert test1_instance1 is not test2_instance1


# Generated at 2022-06-13 16:47:30.098396
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonClass(object):
        """Sample class that inherits from object and uses Singleton
        as Metaclass.

        Attributes:
            _value: Private variable that is updated in every call.
        """
        __metaclass__ = Singleton

        def __init__(self, value=None):
            """Constructor for SingletonClass.

            Args:
                value: Value to initialize private variable _value.
            """
            self._value = value

        def get_value(self):
            """Return _value."""
            return self._value

        def set_value(self, value):
            """Set _value to value."""
            self._value = value

    # Instance 1
    instance1 = SingletonClass(1)
    assert instance1.get_value() == 1

# Generated at 2022-06-13 16:47:34.092322
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self):
            pass
    a1 = A()
    a2 = A()
    assert type(A) == Singleton
    assert a1 == a1
    assert a1 == a2
    assert a2 == a1

# Generated at 2022-06-13 16:47:37.250215
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            # First init
            pass

    a = A()
    print(a)
    b = A()
    print(b)
    print(id(a) == id(b))  # True

# Generated at 2022-06-13 16:47:40.073196
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SampleClass(object):
        __metaclass__ = Singleton
        pass

    assert SampleClass() is SampleClass()  # check if it returns the same instance


# Generated at 2022-06-13 16:47:42.460372
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    o1 = A()
    o2 = A()
    assert o1 == o2

# Generated at 2022-06-13 16:47:45.866458
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, x=None):
            self.x = x

    a = A(123)
    # print(a.x)
    assert a.x == 123
    b = A()
    # print(b.x)
    assert b.x == 123
    assert a == b
    b.x = 999
    # print(a.x)
    # print(b.x)
    assert a.x == 999
    assert b.x == 999

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:47:50.713539
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

    a = Test(1)
    b = Test(2)

    assert a.x == b.x
    assert id(a) == id(b)
    assert a == b

# Generated at 2022-06-13 16:47:59.403560
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest
    import inspect

    class Foo:
        __metaclass__ = Singleton

    class Bar:
        __metaclass__ = Singleton

    class Bar2:
        __metaclass__ = Singleton

    class TestSingleton(unittest.TestCase):
        def test_only_one_instance_exists(self):
            foo = Foo()
            bar = Bar()

            self.assertTrue(inspect.ismethod(foo.__call__))
            self.assertTrue(inspect.ismethod(bar.__call__))
            self.assertTrue(foo is Foo())
            self.assertTrue(bar is Bar())
            self.assertFalse(foo is bar)

    if __name__ == '__main__':
        unittest.main()



# Generated at 2022-06-13 16:48:02.048683
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = "test"

    obj1 = TestSingleton()
    obj2 = TestSingleton()
    assert obj1 is obj2

# Generated at 2022-06-13 16:48:11.013098
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Test Singleton.__call__
    test that Singleton.__call__ instanciate a class only once"""
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 0

    x = TestClass()
    y = TestClass()

    assert x is not None
    assert y is not None
    assert x is y
    assert x.x == y.x == 0

    x.x = 1
    y.x = 2

    assert y.x == x.x == 2

# Generated at 2022-06-13 16:48:12.841411
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(metaclass=Singleton):
        def __init__(self, name):
            self.name = name

    a = Test('test1')
    b = Test('test2')
    assert a is b
    assert a.name == 'test2'

# Generated at 2022-06-13 16:48:14.086903
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    a = TestSingleton()
    b = TestSingleton()
    assert a == b

# Generated at 2022-06-13 16:48:16.459758
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(Singleton):
        pass

    a1 = A()
    a2 = A()
    assert a1 == a2

# Generated at 2022-06-13 16:48:20.108209
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert a is b


# Generated at 2022-06-13 16:48:26.220310
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass1(object):
        __metaclass__ = Singleton

    test_class_1 = TestClass1()
    assert test_class_1 == TestClass1()

    class TestClass2(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.some_attr = True

    assert TestClass2().some_attr



# Generated at 2022-06-13 16:48:35.124263
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import unittest
    from threading import Thread
    import time

    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 1

        def test(self):
            print('test')
            for i in range(3):
                time.sleep(1)
                self.value += 1

    class TestThread(Thread):
        def __init__(self, name, singleton):
            Thread.__init__(self, name=name)
            self.singleton = singleton

        def run(self):
            self.singleton.test()

    class TestSingleton(unittest.TestCase):
        def setUp(self):
            self.TestSingleton = TestSingleton()
            pass

        def tearDown(self):
            pass

       

# Generated at 2022-06-13 16:48:38.969607
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
    a = A()
    b = A()
    assert a is b, "Did not reuse instance"


# Generated at 2022-06-13 16:48:40.452617
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

    assert SingletonTest() is SingletonTest()

# Generated at 2022-06-13 16:48:45.827533
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.var = 0

    def f():
        for i in range(10):
            foo = Foo()
            assert foo.var == i

    import threading

    threads = [threading.Thread(target=f) for i in range(10)]

    for t in threads:
        t.start()
        t.join()

# Generated at 2022-06-13 16:48:52.454059
# Unit test for constructor of class Singleton
def test_Singleton():
    class B(metaclass=Singleton):
        def __init__(self, x):
            self.x = x
    b1 = B(1)
    b2 = B(2)
    assert(id(b1) == id(b2))
    assert(b1.x == 1)
    assert(b2.x == 1)

# Generated at 2022-06-13 16:49:00.166775
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(metaclass=Singleton):
        name = 'Bartek'
        age = 33
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def get_name(self):
            return self.name
        def get_age(self):
            return self.age

    a = MySingleton('Jan', 23)
    b = MySingleton('Adam', 22)
    c = MySingleton('Kamil', 81)
    d = MySingleton('Kamil', 30)

    assert a.get_name() == c.get_name() == b.get_name() == 'Jan'
    assert a.get_age() == c.get_age() == b.get_age() == 23

# Generated at 2022-06-13 16:49:05.392366
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    a2 = A()
    assert a1 is a2, 'Singleton class is not really singleton'


# Generated at 2022-06-13 16:49:13.280633
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    """Test for the method __call__ of class Singleton
    """
    from ansible.parsing.ajson import AnsibleJSONDecoder
    from ansible.parsing.ajson import AnsibleJSONEncoder
    from ansible.parsing.ajson import AnsibleJSONEncoderBase
    from ansible.parsing.ajson import AnsibleJSONDecoderBase
    from ansible.parsing.ajson import AnsibleJSONDecoderForRFC8601
    from ansible.parsing.ajson import AnsibleJSONDecoderError


    ansible_decoder_1 = AnsibleJSONDecoder()
    ansible_decoder_2 = AnsibleJSONDecoder()

    assert(ansible_decoder_1 == ansible_decoder_2)

    ansible_encoder_1 = AnsibleJSONEncoder

# Generated at 2022-06-13 16:49:15.210475
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert A() is A()

# Generated at 2022-06-13 16:49:20.881834
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object, metaclass=Singleton):
        def __init__(self, arg_1, arg_2):
            self.__arg_1 = arg_1
            self.__arg_2 = arg_2

        @property
        def arg_1(self):
            return self.__arg_1

        @property
        def arg_2(self):
            return self.__arg_2

    assert MyClass.__instance is None
    instance = MyClass('first arg', 'second arg')
    assert isinstance(instance, MyClass)
    assert instance.arg_1 == 'first arg'
    assert instance.arg_2 == 'second arg'
    assert MyClass.__instance is None

    instance_1 = MyClass('other first arg', 'other second arg')

# Generated at 2022-06-13 16:49:25.412778
# Unit test for constructor of class Singleton
def test_Singleton():
    print('Test Singleton')

    class Person(metaclass=Singleton):
        def __init__(self, name):
            self.name = name
            self.age = 18

    person1 = Person('Zhang San')
    print('person1: %s' % person1)
    person1.age = 22
    person2 = Person('Lisi')
    print('person2: %s' % person2)

    person1 is person2
    person1.age == person2.age


if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:49:30.243961
# Unit test for constructor of class Singleton
def test_Singleton():
    class B(object):
        __metaclass__ = Singleton
        def __init__(self):
            print('called')

    # B is singleton, the second time it's called it should be instantiated
    a = B()
    b = B()
    assert a is b


# Generated at 2022-06-13 16:49:39.804834
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonClass(object):
        __metaclass__ = Singleton
        def __init__(self, arg1, arg2, arg3):
            self.__id = arg1
            self.__name = arg2
            self.__address = arg3

        def get_id(self):
            return self.__id
        def set_id(self, id):
            self.__id = id
        def del_id(self):
            del self.__id
        id = property(get_id, set_id, del_id)  # Note: @id.setter and @id.deleter are not supported by python 2.6
        def get_name(self):
            return self.__name
        def set_name(self, name):
            self.__name = name

# Generated at 2022-06-13 16:49:51.017470
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest:
        def __init__(self):
            self.value = 0

        def increment(self):
            self.value += 1

    singleton_test_class = type('SingletonTest', (SingletonTest,), {'__metaclass__': Singleton})

    test_instance_one = singleton_test_class()
    test_instance_two = singleton_test_class()

    assert test_instance_one.value == 0
    assert test_instance_two.value == 0

    test_instance_one.increment()

    assert test_instance_one.value == 1
    assert test_instance_two.value == 1

    test_instance_two.increment()

    assert test_instance_one.value == 2
    assert test_instance_two.value == 2

# Generated at 2022-06-13 16:49:57.489033
# Unit test for constructor of class Singleton
def test_Singleton():

    class TestSingleton(object):
        __metaclass__ = Singleton

    x = TestSingleton()
    y = TestSingleton()

    assert x is y

# Generated at 2022-06-13 16:50:05.296425
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Since Singleton class is an metaclass and is not instantiated,
    # An intermediate class is needed for testing purpose
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, test_arg):
            self.test_arg = test_arg

    assert TestSingleton('arg1') is TestSingleton('arg2')

    # Try to instantiate TestSingleton with a no-arg constructor,
    # It should raise exception as Singleton() is called.
    try:
        TestSingleton()
    except TypeError:
        print('Expected exception is raised!')
    else:
        assert False, 'Expected exception not raised!'

# Generated at 2022-06-13 16:50:11.292949
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    class B(object):
        __metaclass__ = Singleton

    class C(object):
        __metaclass__ = Singleton

    assert C() is C()
    assert A() is not B()
    assert B() is B()



# Generated at 2022-06-13 16:50:13.539711
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    a = Test()
    b = Test()
    assert a is b


# Generated at 2022-06-13 16:50:17.814686
# Unit test for constructor of class Singleton
def test_Singleton():
    class FakePlugin(object):
        __metaclass__ = Singleton
    assert isinstance(FakePlugin(), FakePlugin)

# Used to store the default callback.

# Generated at 2022-06-13 16:50:21.523373
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

        def do_something(self):
            pass

    assert Foo() is Foo()
    assert Foo().do_something() is None

# Generated at 2022-06-13 16:50:25.859710
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'A'

    class B(A):
        pass

    a = A()
    b = B()
    assert a == b


# Generated at 2022-06-13 16:50:28.888006
# Unit test for constructor of class Singleton
def test_Singleton():
    ansible = Singleton("Ansible")
    assert ansible is Singleton("Ansible")
    assert isinstance(ansible, Singleton)

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:50:35.428076
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1
            self.b = 2

    a1 = A()
    assert a1.a == 1
    assert a1.b == 2

    a1.a = 3
    a1.b = 4

    a2 = A()
    assert a2.a == 3
    assert a2.b == 4

# Generated at 2022-06-13 16:50:38.478269
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

    test_singleton1 = TestSingleton()
    test_singleton2 = TestSingleton()

    assert id(test_singleton1) == id(test_singleton2)

# Generated at 2022-06-13 16:50:46.294105
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingletonClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.some_attr = "some value"

    inst1 = TestSingletonClass()
    inst2 = TestSingletonClass()
    assert id(inst1) == id(inst2)

test_Singleton___call__()

# Generated at 2022-06-13 16:50:53.072690
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object, metaclass=Singleton):
        def __init__(self, *args, **kwargs):
            super(S, self).__init__()
            self.args = args
            self.kwargs = kwargs

    s = S('a', 'b', c='C', d='D')
    t = S('a', 'b', c='C')

    assert s == t
    assert s.args == ('a', 'b')
    assert s.kwargs == {'c': 'C', 'd': 'D'}



# Generated at 2022-06-13 16:50:54.277866
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest:
        __metaclass__ = Singleton
    assert SingletonTest() is SingletonTest()

# Generated at 2022-06-13 16:51:02.261858
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.number = None

    class B(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.number = None

    a1 = A()
    a1.number = 1
    a2 = A()
    assert a2.number == a1.number
    b1 = B()
    b1.number = 2
    b2 = B()
    assert b2.number == b1.number
    assert a2.number != b2.number



# Generated at 2022-06-13 16:51:04.061368
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    a1 = A()
    assert a1 is A()
    a2 = A()
    assert a2 is a1

# Generated at 2022-06-13 16:51:07.809111
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test(object):
        __metaclass__ = Singleton

    t1 = Test()
    t2 = Test()
    assert t1 is t2

# Generated at 2022-06-13 16:51:13.665627
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Declare a new class with metaclass Singleton
    class OnlyOne:
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 1 + 3

    # create two instances
    one = OnlyOne()
    two = OnlyOne()

    # check if both instances are the same
    assert one is two

    one.x = 3 + 6

    # check if one.x == two.x
    assert one.x == two.x


if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:51:17.849675
# Unit test for constructor of class Singleton
def test_Singleton():
    s1 = Singleton()
    assert id(s1) == id(Singleton())
    assert id(s1) == id(singleton())

# Class to test Singleton Metaclass

# Generated at 2022-06-13 16:51:22.828845
# Unit test for constructor of class Singleton
def test_Singleton():
    from collections import OrderedDict

    class Dummy(object, metaclass=Singleton):
        def __init__(self, x=0, y=0):
            self.x = x
            self.y = y

    assert Dummy(1,2) == Dummy(2,2) == Dummy(x=2,y=2)
    assert Dummy(1,2) != Dummy(1,1) != Dummy(x=1,y=1)

# Generated at 2022-06-13 16:51:30.479417
# Unit test for constructor of class Singleton
def test_Singleton():
    class Base(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    class Derived(Base):
        def __init__(self):
            Base.__init__(self)

    a = Base()
    b = Base()
    c = Derived()
    d = Derived()
    assert a is b
    assert a is c
    assert c is d

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:51:43.856502
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, bar):
            self.bar = bar

    instance1 = TestSingleton(bar='foo')
    instance2 = TestSingleton(bar='baz')

    assert instance1 == instance2
    assert instance1.bar == 'foo'
    assert instance2.bar == 'foo'


# Generated at 2022-06-13 16:51:47.410493
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        pass

    a1 = A()
    a2 = A()
    assert a1 is a2, 'failed to implement singleton'

    b1 = A()
    assert a1 is b1, 'instance should be same'


# Generated at 2022-06-13 16:51:53.788737
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.test = None

        def set_test(self, value):
            self.test = value

        def get_test(self):
            return self.test

    class MySingletonSubclass(MySingleton):
        pass

    ins1 = MySingleton()
    ins2 = MySingleton()
    assert ins1 is ins2
    assert ins1.get_test() == ins2.get_test()
    assert ins1.get_test() is None

    ins1.set_test('foo')
    assert ins1.get_test() == ins2.get_test()
    assert ins1.get_test() == 'foo'
    assert ins2.get_test() == 'foo'

    ins

# Generated at 2022-06-13 16:51:56.274335
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(metaclass=Singleton):
        def __init__(self):
            self.a = 1

    a = TestClass()
    b = TestClass()
    assert(a.a == b.a)

# Generated at 2022-06-13 16:51:59.790043
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingletonClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.name = 'Test'

    test_instance1 = TestSingletonClass()
    test_instance2 = TestSingletonClass()
    assert test_instance1 == test_instance2



# Generated at 2022-06-13 16:52:04.130842
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object, metaclass=Singleton):
        _foo = None
        def __init__(self, foo):
            self._foo = foo

    ts1 = TestSingleton('bar')
    ts2 = TestSingleton('baz')

    assert ts1._foo == ts2._foo



# Generated at 2022-06-13 16:52:11.203215
# Unit test for constructor of class Singleton
def test_Singleton():
    # Create a new class based on Singleton
    class ExampleSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, arg1):
            self.arg1 = arg1

    # Create two instances of ExampleSingleton
    example1 = ExampleSingleton(1)
    example2 = ExampleSingleton(2)

    # Check that both instances are the same
    assert hash(example1) == hash(example2)


if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:52:16.478211
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        __metaclass__ = Singleton

        def __init__(self, arg):
            self.arg = arg

        def __eq__(self, other):
            return self.arg == other.arg

    assert SingletonTest("Argument") == SingletonTest("Argument")
    assert id(SingletonTest("Argument")) == id(SingletonTest("Argument"))


# Generated at 2022-06-13 16:52:18.873280
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    a = TestClass()
    b = TestClass()
    #assert id(a) == id(b)

# Generated at 2022-06-13 16:52:24.747743
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    _instance_count = 0

    class Foo(object):
        __metaclass__ = Singleton
        def __init__(self, name):
            global _instance_count
            self._name = name
            _instance_count += 1
            if _instance_count > 1:
                raise Exception("An instance should be created")

        def __str__(self):
            return self._name

    class Bar(Foo):
        pass

    foo_1 = Foo('foo 1')
    foo_2 = Foo('foo 2')
    bar_1 = Bar('bar 1')
    bar_2 = Bar('bar 2')

    assert(foo_1 == foo_2)
    assert(bar_1 == bar_2)
    assert(bar_1 == foo_1)


# Example of how to use Singleton

# Generated at 2022-06-13 16:52:38.204178
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from shutil import rmtree
    from tempfile import mkdtemp

    def _remove_tmp_dir(tmp_dir):
        try:
            rmtree(tmp_dir)
        except OSError:
            pass

    tmp_dir = mkdtemp(prefix="yan_singleton_test_")

# Generated at 2022-06-13 16:52:45.497088
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class RandomClass(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

        def increment(self):
            self.value += 1

    # Set the value of the instance
    instance1 = RandomClass(1)
    # The instance can be modified
    instance1.increment()
    assert(instance1.value == 2)

    # Retrieve another instance of the class
    instance2 = RandomClass(3)
    # The instances shall be the same
    assert(instance1 is instance2)
    # The value can be modified again
    instance2.increment()
    assert(instance2.value == 3)

test_Singleton___call__()

# Generated at 2022-06-13 16:52:51.631636
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class cls(object):
        __metaclass__ = Singleton

        def __init__(self, arg1):
            self.arg1 = arg1

        def __str__(self):
            return "I am the instance of class %s, " \
                "my argument is %s" % (self.__class__.__name__,
                                      self.arg1)

    cls1 = cls("1")
    assert str(cls1) == "I am the instance of class cls, " \
        "my argument is 1"

    cls2 = cls("2")
    assert cls1 is cls2
    assert str(cls1) == str(cls2)
    assert cls1 == cls2

# Generated at 2022-06-13 16:52:52.533723
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert A() is A()



# Generated at 2022-06-13 16:52:55.590246
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.a = 'something'

    a = A()
    a.a = 'changed'
    a1 = A()
    assert a1.a == 'changed'

# Generated at 2022-06-13 16:52:58.025067
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 10

    obj1 = MySingleton()
    obj2 = MySingleton()

    assert obj1.value == obj2.value
    obj1.value = 20

    assert obj2.value == obj1.value


if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:53:04.195511
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSinglton(object):
        __metaclass__ = Singleton

    s1 = TestSinglton()
    s2 = TestSinglton()
    if s1 != s2:
        raise RuntimeError('Instance is not Singleton')

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:53:12.502813
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Creating the first instance
    class TestSingleton(object):
        """Class using Singleton metaclass"""
        __metaclass__ = Singleton
        instance_count = 0

        def __init__(self):
            type(self).instance_count += 1

    # Creating the second instance
    class TestSingleton2(TestSingleton):
        pass

    # Checking that they are the same instance
    assert TestSingleton() is TestSingleton()

    # Checking that they are the same instance
    assert TestSingleton2() is TestSingleton2()

    # Checking that they are the different instances
    assert TestSingleton() is not TestSingleton2()

    # One instance created for each Singleton-derived class
    assert TestSingleton.instance_count == 1 and TestSingleton2.instance_count == 1

# Generated at 2022-06-13 16:53:17.753672
# Unit test for constructor of class Singleton
def test_Singleton():
    class C(object):
        __metaclass__ = Singleton

        def __init__(self):
            super(C, self).__init__()
            self.arg = None
            self.kw = None

        def __call__(self, arg=None, **kw):
            self.arg = arg
            self.kw = kw
            return arg, kw

    c = C(arg=1, kw=2)
    assert c.arg == 1
    assert c.kw == 2

    c2 = C(kw=3)
    assert c2 is not None
    assert c2.arg == c.arg
    assert c2.kw == 3

    c3 = C()
    assert c3 is not None
    assert c3.arg == c.arg
    assert c3.kw == c2.kw

   

# Generated at 2022-06-13 16:53:25.565609
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        def __init__(self, val):
            self.val = val
        def get_val(self):
            return self.val
    class B:
        def __init__(self, val):
            self.val = val
        def get_val(self):
            return self.val
    def assert_instance_equals(a, b):
        assert a.get_val() == b.get_val()
        assert a is b
    instance_a = A(42)
    instance_b = A(42)
    instance_c = B(42)
    assert_instance_equals(instance_a, instance_b)
    assert instance_a is not instance_c
    assert instance_b is not instance_c
    instance_b.val = "hello"


# Generated at 2022-06-13 16:53:36.466280
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    assert TestClass() == TestClass()


# Generated at 2022-06-13 16:53:41.958636
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 0
    a1 = A()
    a2 = A()
    assert a1 == a2
    a1.x = 1
    assert a2.x == 1

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:53:46.961554
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.foo = 'bar'

    a = MyClass()
    b = MyClass()

    # a and b should point to the same object
    assert id(a) == id(b)

    # Both objects should have the same 'foo' variable
    assert a.foo == b.foo

# Generated at 2022-06-13 16:53:48.215335
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Fruit(object):
        __metaclass__ = Singleton

    assert Fruit() is Fruit()


# Generated at 2022-06-13 16:53:54.718531
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton

        def __init__(self, my_param):
            self.__my_param = my_param

        def get_param(self):
            return self.__my_param

    inst1 = MyClass('value')
    inst2 = MyClass('other_value')

    assert(inst1 == inst2)
    assert(inst1.get_param() == 'value')
    assert(inst2.get_param() == 'value')

# Generated at 2022-06-13 16:53:59.797961
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    res1 = SingletonClass()
    res2 = SingletonClass()
    assert res1 is res2, "Every call to SingletonClass should return the same object, but it doesn't"



# Generated at 2022-06-13 16:54:05.029315
# Unit test for constructor of class Singleton
def test_Singleton():
    class A():
        __metaclass__ = Singleton

        def __init__(self, name):
            self._name = name

    a1 = A('a1')
    a2 = A('a2')

    assert(a1._name == 'a1')
    assert(a2._name == 'a1')

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:54:12.723890
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        def __repr__(self):
            return repr(self.a) + repr(self.b) + repr(self.c)

    assert A(1, 2, 3) == A(4, 5, 6) == A(1, 2, 3)
    assert A(1, 2, 3) is A(1, 2, 3)
    assert A(1, 2, 3) is A(A(1, 2, 3))
    assert A(1, 2, 3) is A(4, 5, 6)
    assert A(1, 2, 3) is A()


# Generated at 2022-06-13 16:54:13.774208
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton

    assert MyClass is MyClass()



# Generated at 2022-06-13 16:54:16.524460
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class DummyClass(object):
        __metaclass__ = Singleton

    dummy_instance = DummyClass()
    dummy_instance_2 = DummyClass()

    assert dummy_instance is dummy_instance_2

# Generated at 2022-06-13 16:54:42.235547
# Unit test for constructor of class Singleton
def test_Singleton():
    class Single(object):
        __metaclass__ = Singleton # making Singleton a metaclass

        def __init__(self, value=None):
            self.value = value

    class Test(Single):
        def __init__(self, value=None):
            super(Test, self).__init__(value) # Call's Single.__init__()

    a = Test("x")
    b = Test("y")
    assert a.value == "x"
    assert b.value == "x" # because b and a are the same object
    assert a is b

    c = Test()
    assert c.value == "x"
    assert c is b

    class Other(Single):
        def __init__(self, value=None):
            super(Other, self).__init__(value) # Call's Single.

# Generated at 2022-06-13 16:54:47.343616
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            super(A, self).__init__()

    a = A()
    b = A()
    assert(a == b)


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:54:57.287008
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Single1(object):
        __metaclass__ = Singleton

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    class Single2(object):
        __metaclass__ = Singleton

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2

    single1 = Single1('a', 'b')
    single2 = Single1('c', 'd')
    assert single1 is single2
    assert single1.arg1 == 'c'
    assert single1.arg2 == 'd'

    print("Test passed")

#if __name__ == '__main__':
#    test_Singleton___call__()

# Generated at 2022-06-13 16:55:01.451525
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    # Create first instance
    instance1 = TestSingleton()
    # Create second instance
    instance2 = TestSingleton()

    assert instance1 is instance2

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:55:03.569905
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    obj1 = TestClass()
    obj2 = TestClass()

    assert id(obj1) == id(obj2), "Failure: Both objects are not same"

# Generated at 2022-06-13 16:55:06.157624
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test1(metaclass=Singleton):
        pass

    class Test2(Test1):
        pass

    class Test3(metaclass=Singleton):
        pass

    assert Test1() == Test2()
    assert Test1() == Test3()
    assert Test2() == Test3()


# Generated at 2022-06-13 16:55:08.661149
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class FredCls(object):
        __metaclass__ = Singleton

        def __init__(self):
            print('in constructor')

    a = FredCls()
    b = FredCls()
    c = FredCls()
    assert a is b is c

# Singleton for the purpose of mocking out ansible

# Generated at 2022-06-13 16:55:11.325607
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(object):
        """This class implements Singleton interface.
        """
        __metaclass__ = Singleton
        def __init__(self):
            """Always print 'initializing'
            """
            print('initializing')

    one = MySingleton()
    two = MySingleton()

    assert one is two, "MySingleton should be a singleton"



# Generated at 2022-06-13 16:55:13.065585
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(metaclass=Singleton): pass
    my_class1 = MyClass()
    my_class2 = MyClass()
    assert my_class1 == my_class2

# Generated at 2022-06-13 16:55:16.461301
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
    t1 = TestSingleton()
    t2 = TestSingleton()
    assert t1 == t2 and t1 is t2

# Generated at 2022-06-13 16:55:58.128032
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

    a = Foo()
    b = Foo()
    assert a is b

# Generated at 2022-06-13 16:56:00.603923
# Unit test for constructor of class Singleton
def test_Singleton():
    class SomeClass(object):
        __metaclass__ = Singleton

    # Singleton should be instantiated by calling the constructor.
    obj1 = SomeClass()
    obj2 = SomeClass()

    assert obj1 is obj2

test_Singleton()

# Generated at 2022-06-13 16:56:03.017002
# Unit test for constructor of class Singleton
def test_Singleton():
    class Example(metaclass=Singleton):
        def __init__(self):
            self.x = int(input())
    a = Example()
    b = Example()
    print("Sum is ", a.x+b.x)

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:56:08.873071
# Unit test for constructor of class Singleton
def test_Singleton():
    """
    >>> from collections import OrderedDict
    >>> class Test:
    ...     __metaclass__ = Singleton
    ...     def __init__(self, *args, **kwargs):
    ...         self.args = args
    ...         self.kwargs = kwargs
    ...     def getstate(self):
    ...         return self.args, self.kwargs
    >>> x = Test(1, 2, 3, 4, a=5, b=6)
    >>> y = Test()
    >>> x is y
    True
    >>> x.getstate() == (1, 2, 3, 4), OrderedDict((('a', 5), ('b', 6)))
    True
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:56:11.333310
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton


    class Bar(Foo):
        pass

    # Ensure only one instance of Foo
    assert Foo() == Foo()

    # Ensure that Bar is a Singleton of Foo
    assert Bar() == Foo() == Bar()

    # Ensure that Foo is not a Singleton of Bar
    assert Foo() != Bar()


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:56:14.369912
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            print("A")

    class B(A):
        def __init__(self):
            print("B")

        def __new__(cls):
            return object.__new__(cls)

    a = A()
    b = B()

    assert a is b


# Generated at 2022-06-13 16:56:18.411171
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, value):
            self.value = value

    a = TestClass(1)
    b = TestClass(2)
    assert a.value == 1
    assert b.value == 1

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:56:21.235761
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    assert id(TestClass()) == id(TestClass())


# Generated at 2022-06-13 16:56:28.800413
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Singleton(object):
        """Metaclass for classes that wish to implement Singleton
        functionality.  If an instance of the class exists, it's returned,
        otherwise a single instance is instantiated and returned.
        """
        __instance = None
        def __new__(cls, *args, **kw):
            if cls.__instance is not None:
                return cls.__instance
            else:
                cls.__instance = super(Singleton, cls).__new__(cls)
                return cls.__instance

    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, val):
            self.val = val

    obj1 = TestClass(1)
    obj2 = TestClass(2)