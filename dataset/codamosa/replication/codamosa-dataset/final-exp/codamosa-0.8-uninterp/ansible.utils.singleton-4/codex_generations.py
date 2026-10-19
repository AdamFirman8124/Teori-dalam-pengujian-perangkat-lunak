

# Generated at 2022-06-13 16:46:40.094863
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
    instance_1 = TestSingleton()
    instance_2 = TestSingleton()
    try:
        assert instance_1 == instance_2
    except AssertionError:
        raise AssertionError("Singleton __call__ method failed: " +
                             "instance_1 is not equal instance_2")

# Generated at 2022-06-13 16:46:49.786545
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class BaseSingleton(object):
        __metaclass__ = Singleton
        pass

    class ChildSingleton(BaseSingleton):
        pass

    # there is no instance of BaseSingleton
    assert BaseSingleton.__instance is None
    # create an instance of BaseSingleton
    # there should be 1 instance of BaseSingleton
    bs1 = BaseSingleton()
    assert bs1 is BaseSingleton.__instance

    # there is no instance of ChildSingleton
    assert ChildSingleton.__instance is None
    # create an instance of ChildSingleton
    # there are 2 instances of bs1 and ChildSingleton
    cs1 = ChildSingleton()
    assert cs1 is ChildSingleton.__instance
    assert bs1 == cs1

    # there are 2 instances of bs1, bs2 and cs1, cs

# Generated at 2022-06-13 16:46:55.148738
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, value):
            self.value = value

    class B(A):
        pass

    a = A(42)
    a2 = A(100)
    b = B(43)
    b2 = B(101)

    assert a is a2
    assert b is b2
    assert a2 is not b2


# Generated at 2022-06-13 16:46:59.418511
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from random import randint
    from time import sleep

    class Foo(metaclass=Singleton):
        def __init__(self):
            self.value = randint(0, 10)

    foo1 = Foo()
    foo2 = Foo()

    assert(foo1.value == foo2.value)
    foo3 = Foo()
    assert(foo1.value == foo3.value)

# Generated at 2022-06-13 16:47:01.877350
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():

    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    a = A()
    assert(a == A())

# Generated at 2022-06-13 16:47:08.855037
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class FirstCall(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

        def __str__(self):
            return "FirstCall"

    assert(hash(FirstCall()) == hash(FirstCall()))

    class SecondCall(object):
        __metaclass__ = Singleton

        def __init__(self):
            pass

        def __str__(self):
            return "SecondCall"

    assert(hash(SecondCall()) == hash(SecondCall()))

    assert(hash(FirstCall()) != hash(SecondCall()))


if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:47:12.089445
# Unit test for constructor of class Singleton
def test_Singleton():
    class t:
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 5
    s = t()
    assert s.value == 5
    assert id(s) == id(t())

# Generated at 2022-06-13 16:47:14.326464
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

    assert(id(A()) == id(A()))


# Generated at 2022-06-13 16:47:17.397291
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        # class TestClass has no __init__
        __metaclass__ = Singleton

    c1 = TestClass()
    c2 = TestClass()
    assert (c1 is c2)


# Generated at 2022-06-13 16:47:26.532413
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a1, a2):
            self.a1 = a1
            self.a2 = a2

    a1 = A(1,2)
    a2 = A(3,4)
    assert(a1 == a2)
    assert(a1 is a2)
    assert(a1.a1 == 1)
    assert(a1.a2 == 2)
    assert(a2.a1 == 1)
    assert(a2.a2 == 2)


# Generated at 2022-06-13 16:47:34.724201
# Unit test for constructor of class Singleton
def test_Singleton():

    class A(metaclass=Singleton):

        def __init__(self):
            self.a = 1

    a = A()
    assert a.a == 1
    assert a is A()
    assert id(a) == id(A())

    class B(metaclass=Singleton):

        def __init__(self, y=2):
            self.y = y

    b = B()
    assert b.y == 2
    assert b is B()
    assert id(b) == id(B())
    c = B(y=3)
    assert c is b
    assert c.y == 3


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:47:38.721943
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    f1 = Foo()
    f2 = Foo()

    assert id(f1) == id(f2)
    assert f1 is f2

# Generated at 2022-06-13 16:47:48.453741
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object, metaclass=Singleton):
        def __init__(self):
            self.a = 1
            self.b = 2
            print("Singleton constructor called")

    foo = Foo()
    print("foo a: %s, b: %s" % (foo.a, foo.b))
    assert(foo.a == 1)
    assert(foo.b == 2)
    foo1 = Foo()
    print("foo1 a: %s, b: %s" % (foo1.a, foo1.b))
    assert(foo1.a == 1)
    assert(foo1.b == 2)
    assert foo is foo1

# python3 -m ansible.utils.singleton
if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:47:52.972295
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 1

    x = TestSingleton()
    y = TestSingleton()
    assert x == y
    assert x.value == 1
    y.value = 2
    assert y.value == x.value

# Generated at 2022-06-13 16:47:59.884776
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Dog:
        __metaclass__ = Singleton

    d1 = Dog()
    d2 = Dog()

    d1.name = "Dogo"
    d2.name = "Rex"

    print("d1 = %s" % d1)
    print("d2 = %s" % d2)

    assert d1==d2
    assert d1.name==d2.name=="Rex"


# Generated at 2022-06-13 16:48:03.890600
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import mock

    class SampleSingleton(object):
        __metaclass__ = Singleton

    with mock.patch.object(SampleSingleton, '__call__', return_value=555) as mock_obj:
        singleton = SampleSingleton()
        assert singleton == 555
        mock_obj.assert_called_once_with()

        res = mock_obj()
        assert res == 555



# Generated at 2022-06-13 16:48:07.556678
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton

    x1 = TestClass()
    x2 = TestClass()
    assert x1 == x2

if __name__ == "__main__":
    test_Singleton___call__()

# Generated at 2022-06-13 16:48:11.576364
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Class(object):
        __metaclass__ = Singleton

    assert(Class() == Class())
    assert(Class.__instance is not None)
    assert(Class() is Class.__instance)
    assert(Class() is Class())
    assert(Class.__instance is Class())



# Generated at 2022-06-13 16:48:12.999950
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton

    assert Test() is Test()

# Generated at 2022-06-13 16:48:17.046188
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class MyClass(object):
        __metaclass__ = Singleton
    instance = MyClass()
    instance2 = MyClass()
    assert instance is instance2

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:48:23.922383
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(object):
        __metaclass__ = Singleton

    x = Foo()
    y = Foo()
    assert x is y



# Generated at 2022-06-13 16:48:33.775517
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonA(metaclass=Singleton):
        def __init__(self, *args, **kwargs):
            self.A = 'a'
            self.B = 'b'
            self.args = args
            self.kwargs = kwargs

    class SingletonB(SingletonA):
        def __init__(self, *args, **kwargs):
            super(SingletonB, self).__init__(*args, **kwargs)
            self.C = 'c'

    a = SingletonA('aa', 'bb')
    aa = SingletonA('aa', 'bb')
    b = SingletonB('bb', 'cc')
    bb = SingletonB('bb', 'cc')
    assert id(a) == id(aa)
    assert id(a) != id(b)


# Generated at 2022-06-13 16:48:37.755975
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, a):
            self.a = a

    assert A(1) is A(1)



# Generated at 2022-06-13 16:48:46.756575
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import sys
    import subprocess
    import os
    os.chdir('/'.join(__file__.split('/')[:-1]))

    # We will use this function to run unit tests and check the output
    def run_unit_test(test_name, result_value, result_type):
        command = '%s %s' % (sys.executable, test_name)
        p = subprocess.Popen([command],
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             shell=True)
        out, err = p.communicate()
        sys.stdout.write(out)

        if p.returncode == 0:
            if result_type == 'str':
                assert(str(out.strip()) == result_value)

# Generated at 2022-06-13 16:48:50.422736
# Unit test for constructor of class Singleton
def test_Singleton():
    class MySingleton(metaclass=Singleton):
        def __init__(self):
            pass

    assert not MySingleton() is None
    assert MySingleton() is MySingleton()
    assert MySingleton() is MySingleton()
    assert MySingleton() is MySingleton()
    assert MySingleton() is MySingleton()
    assert MySingleton() is MySingleton()


# Generated at 2022-06-13 16:48:53.150114
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton
    t1 = TestSingleton()
    t2 = TestSingleton()
    assert t1 is t2

# Generated at 2022-06-13 16:49:00.886963
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from threading import Thread
    import Queue

    class Base(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.counter = 0

        def add(self):
            self.counter += 1

    class A(Base):
        pass

    class B(Base):
        pass

    N = 10
    q = Queue.Queue()

    def worker():
        while True:
            i = q.get()
            if i is None:
                break
            a = A()
            a.add()
            b = B()
            b.add()
            q.task_done()

    threads = []
    for i in xrange(N):
        t = Thread(target=worker)
        t.start()
        threads.append(t)


# Generated at 2022-06-13 16:49:05.808156
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    test_instance_1 = TestSingleton()
    test_instance_2 = TestSingleton()
    assert test_instance_1 is test_instance_2

# Generated at 2022-06-13 16:49:06.295436
# Unit test for constructor of class Singleton
def test_Singleton():
    pass

# Generated at 2022-06-13 16:49:08.439748
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Foo(metaclass=Singleton):
        pass

    f1 = Foo()
    f2 = Foo()
    assert f1 is f2



# Generated at 2022-06-13 16:49:19.159920
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.arg = 0
            self.kw = 0

        def update(self, arg=0, kw=0):
            self.arg = arg
            self.kw = kw

    a = TestSingleton()
    b = TestSingleton()
    a.update(1, kw=1)
    if a.arg == b.arg and a.kw == b.kw:
        print('unit test passed')
    else:
        print('unit test failed')

# Generated at 2022-06-13 16:49:19.647408
# Unit test for constructor of class Singleton
def test_Singleton():
    pass

# Generated at 2022-06-13 16:49:26.337587
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch

    from ansible.errors import AnsibleConnectionFailure

    from ansible.plugins import connection
    from ansible.plugins.loader import connection_loader


# Generated at 2022-06-13 16:49:30.172606
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self, val):
            self.val = val

    a = A(1)
    assert a.val == 1

    b = A(2)
    assert a == b

    assert b.val == 1
    assert b.val == a.val


# Generated at 2022-06-13 16:49:33.899104
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()
    assert(a is b)


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:49:40.443895
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass1(object):
        __metaclass__ = Singleton
        pass

    class TestClass2(object):
        __metaclass__ = Singleton
        pass

    assert TestClass1() == TestClass1()
    assert TestClass1() != TestClass2()
    assert TestClass1() is not TestClass2()

    class TestClass3(TestClass1):
        pass

    class TestClass4(TestClass2):
        pass

    assert TestClass3() == TestClass1()
    assert TestClass4() == TestClass2()
    assert TestClass3() == TestClass4()



# Generated at 2022-06-13 16:49:42.682443
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    a = A()
    b = A()

    assert a is b


# If this file is named 'singleton.py', then it will be used by default
# as the metaclass definition instead of this file.

# Generated at 2022-06-13 16:49:49.344784
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    from inspect import isclass
    from ansible.utils.unsafe_proxy import AnsibleUnsafeText
    assert isclass(AnsibleUnsafeText)
    obj1 = AnsibleUnsafeText('here')
    obj2 = AnsibleUnsafeText('there')
    obj3 = AnsibleUnsafeText('where')
    assert obj1 is obj2
    assert obj1 is obj3
    assert obj2 is obj3


# Generated at 2022-06-13 16:49:51.212106
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object, metaclass=Singleton):
        pass

    assert A() == A()
    assert A() is A()

# Generated at 2022-06-13 16:49:55.447877
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton
    a = A()
    b = A()
    assert a is not None
    assert a is b

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:50:09.585933
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        """Implements Singleton functionality
        """
        __metaclass__ = Singleton
        __rlock = RLock()
        __instance = None

        def __init__(self):
            super(TestSingleton, self).__init__()

        def initialize(self, test_args, test_kwargs):
            with self.__rlock:
                self.test_args = test_args
                self.test_kwargs = test_kwargs
        def get_args(self, *args, **kwargs):
            return self.test_args
        def get_kwargs(self, *args, **kwargs):
            return self.test_kwargs
    test_args = ("arg1", "arg2", "arg3")

# Generated at 2022-06-13 16:50:11.769930
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo:
        __metaclass__ = Singleton

        def __init__(self):
            self.x = 1

    assert Foo().x == 1

# Generated at 2022-06-13 16:50:14.592979
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class testClass(object):
        __metaclass__ = Singleton
        def __init__(self):
            pass

    test_class1 = testClass()
    test_class2 = testClass()

    assert test_class1 == test_class2

# Generated at 2022-06-13 16:50:26.686338
# Unit test for constructor of class Singleton
def test_Singleton():
    from collections import OrderedDict
    from ansible.module_utils import common as mod_utils
    class Test1(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.foo = 1
            self.bar = OrderedDict()
            self.bar['a'] = 1  # Test OrderedDict when using __eq__/__ne__
            return

        def increment_foo(self):
            self.foo += 1
        pass

    # Make sure we return the same instance rather than instantiate a new one:
    t1 = Test1()
    t2 = Test1()
    assert t1 is t2
    assert id(t1) == id(t2)

    # Make sure we can add arbitrary data to the instance:
    t2.increment_foo()

# Generated at 2022-06-13 16:50:28.258871
# Unit test for constructor of class Singleton
def test_Singleton():
        class A(object):
                __metaclass__ = Singleton

                def __init__(self):
                        print("init")

        a = A()
        b = A()
        assert(a is b)

if __name__ == "__main__":
        test_Singleton()

# Generated at 2022-06-13 16:50:37.000850
# Unit test for constructor of class Singleton
def test_Singleton():
    class MyClass(object):
        __metaclass__ = Singleton
        def __init__(self, msg):
            self._msg = msg

        def get_msg(self):
            return self._msg

    m1 = MyClass('hello')
    m2 = MyClass('world')

    assert m1 is m2
    assert m1.get_msg() == 'world'

    class MyClass2(MyClass):
        def __init__(self, msg):
            super(MyClass2, self).__init__(msg)

    m3 = MyClass2('world')
    assert m1 is m3

# Generated at 2022-06-13 16:50:41.002942
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = "test"

    testS = TestSingleton()
    assert testS.value == "test"

    testS2 = TestSingleton()
    assert testS2.value == "test"
    assert testS is testS2

# Generated at 2022-06-13 16:50:43.153180
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton
    instance1 = TestSingleton()
    instance2 = TestSingleton()
    assert instance1 is instance2

# Generated at 2022-06-13 16:50:50.069404
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(metaclass=Singleton):
        def __init__(self, *args, **kwargs):
            self.a = args
            self.kw = kwargs
            pass
        pass

    # Test __call__ by creating an instance
    a1 = TestClass(1, 2, c=3)

    # Check that the instance was created correctly
    assert a1.a == (1, 2)
    assert a1.kw == {'c': 3}

    # Test __call__ by creating a second instance
    a2 = TestClass(4, 5)

    # Check that the second instance is the same object as the first
    assert a1 == a2

    # Check that the second instance was created correctly
    assert a2.a == (4, 5)
    assert a2.kw == {}
    pass




# Generated at 2022-06-13 16:50:51.910265
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

    class B(A):
        pass

    a = A()
    b = B()
    assert a is b

# Generated at 2022-06-13 16:51:12.602800
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    assert Singleton.__instance is None

    class Demo(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.testing = 'testing'

    assert Singleton.__instance is None

    a = Demo()
    b = Demo()

    assert a is b
    assert a.testing == 'testing'
    assert b.testing == 'testing'
    assert Singleton.__instance is a

# Generated at 2022-06-13 16:51:19.845303
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestSingleton(object):
        __metaclass__ = Singleton

    test_singleton_obj1 = TestSingleton()
    test_singleton_obj2 = TestSingleton()

    assert test_singleton_obj1 == test_singleton_obj2
    assert id(test_singleton_obj1) == id(test_singleton_obj2)

    del(test_singleton_obj1)
    del(test_singleton_obj2)

# Generated at 2022-06-13 16:51:22.208842
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1

        def __call__(self):
            self.a += 1
            retu

# Generated at 2022-06-13 16:51:27.520956
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.name = 'class Test'
    t1 = Test()
    t2 = Test()
    assert t1 == t2
    assert t1.name == t2.name



# Generated at 2022-06-13 16:51:36.324326
# Unit test for constructor of class Singleton
def test_Singleton():
    class Test1(metaclass=Singleton):
        def __init__(self, x):
            self.x = x

    class Test2(metaclass=Singleton):
        pass

    a = Test1(10)
    b = Test1(20)
    print('a:', a.x, id(a))
    print('b:', b.x, id(b))
    assert a == b and a.x == 20 and id(a) == id(b)

    a = Test2()
    b = Test2()
    print('a:', id(a))
    print('b:', id(b))
    assert a == b and id(a) == id(b)


if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:51:42.069371
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Temp(object):
        __metaclass__ = Singleton

        def __init__(self, a, b, c=None):
            self.a = a
            self.b = b
            self.c = c

    # the arguments will be passed to the constructor
    # when the first instance is created
    t1 = Temp(1, '2')
    # we get the instance created above
    t2 = Temp(1, '2')
    assert(t1 == t2)
    # the arguments are not taken into consideration,
    # so it's the same instance
    t2 = Temp(1, '2', '3')
    assert(t1 == t2)

# Generated at 2022-06-13 16:51:43.820998
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(metaclass=Singleton):
        pass

    TestSingleton()
    TestSingleton()
    TestSingleton()

# Generated at 2022-06-13 16:51:46.262255
# Unit test for constructor of class Singleton
def test_Singleton():
    class First(metaclass=Singleton):
        pass

    class Second(object):
        __metaclass__ = Singleton

    first = First()
    second = Second()

    assert first is second

# Generated at 2022-06-13 16:51:52.810751
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Create a Singleton class and keep a reference to the instance
    MySingleton = Singleton('MySingleton', (object,), {})
    inst1 = MySingleton()

    # Now if we call MySingleton() again, the same instance, inst1, is returned
    inst2 = MySingleton()
    assert inst1 is inst2

    # Let's create a new Singleton class and prove that a new instance is returned
    MySingleton2 = Singleton('MySingleton2', (object,), {})
    inst3 = MySingleton2()
    assert inst3 is not inst1
    inst4 = MySingleton2()
    # Now we have yet another instance of MySingleton2
    assert inst4 is not inst1
    assert inst4 is inst3

# Generated at 2022-06-13 16:51:54.985368
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    a1 = Singleton()
    a2 = Singleton()
    a3 = a1
    assert a1 is a2 is a3


# Generated at 2022-06-13 16:52:30.011198
# Unit test for constructor of class Singleton
def test_Singleton():
    class S(object):
        __metaclass__ = Singleton

    assert S() is S()
    assert S() == S()

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:52:34.330512
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

    obj1 = Foo()
    obj2 = Foo()

    assert obj1 is obj2


# Generated at 2022-06-13 16:52:42.062705
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestSingleton(object):
        __metaclass__ = Singleton

        def __init__(self, param1):
            self.param1 = param1

    singleton1_0 = TestSingleton(0)
    singleton1_1 = TestSingleton(1)

    assert id(singleton1_0) == id(singleton1_1)
    assert singleton1_0.param1 == 0

    class TestSingleton2(object):
        __metaclass__ = Singleton

        def __init__(self, param2):
            self.param2 = param2

    singleton2_1 = TestSingleton2(1)
    singleton2_2 = TestSingleton2(2)

    assert id(singleton2_1) == id(singleton2_2)
    assert singleton2_1

# Generated at 2022-06-13 16:52:46.933171
# Unit test for constructor of class Singleton
def test_Singleton():
  class Dummy(metaclass=Singleton):
    def __init__(self):
      self.msg = 'test message'

  dummy1 = Dummy()
  dummy2 = Dummy()
  dummy1.msg = 'first message'
  if dummy2.msg != 'first message':
    print('Singleton not working')
  else:
    print('Singleton working')

#if __name__ == '__main__':
#  test_Singleton()

# Generated at 2022-06-13 16:52:49.225430
# Unit test for constructor of class Singleton
def test_Singleton():
    class SingletonTest(object):
        __metaclass__ = Singleton

    t1 = SingletonTest()
    t2 = SingletonTest()
    assert t1 is t2
    assert type(t1) is SingletonTest

# Generated at 2022-06-13 16:52:51.583614
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class Class1(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.x = 1

    obj1 = Class1()
    assert id(obj1) == id(Class1())

    assert obj1.x == 1


# Generated at 2022-06-13 16:52:53.646886
# Unit test for constructor of class Singleton
def test_Singleton():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, msg):
            self.msg = msg

    test_1 = TestClass('test_1')
    test_2 = TestClass('test_1')
    assert test_1 == test_2


# Generated at 2022-06-13 16:52:59.887531
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1
            self.b = 2
            self.c = 3
        def __eq__(self, other):
            if isinstance(other, A):
                return self.__dict__ == other.__dict__
            return NotImplemented
        def __ne__(self, other):
            result = self.__eq__(other)
            if result is NotImplemented:
                return result
            return not result

    assert A() == A()
    assert A().a == A().a

if __name__ == '__main__':
    test_Singleton()

# Generated at 2022-06-13 16:53:07.505688
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Dummy class that uses the Singleton metaclass
    class A(object):
        __metaclass__ = Singleton
        def __init__(self):
            self.value = 1
    # Instances of A should always be the same
    a1 = A()
    a2 = A()
    assert(a1 == a2)
    assert(id(a1) == id(a2))
    assert(a1.value == 1)
    a2.value = 2
    assert(a1.value == 2)

if __name__ == '__main__':
    test_Singleton___call__()

# Generated at 2022-06-13 16:53:11.302413
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.a = 1

    a1 = A()
    a2 = A()
    a1.a = 2
    assert a1 is a2
    assert a1.a == 2

# Generated at 2022-06-13 16:54:17.374565
# Unit test for constructor of class Singleton
def test_Singleton():
    class Foo(object):
        __metaclass__ = Singleton

    foo1 = Foo()
    foo2 = Foo()

    assert foo1 is foo2

# Generated at 2022-06-13 16:54:25.739809
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    import json
    from ansible.release import __version__ as ansible_version
    from ansible.plugins.loader import connection_loader

    class Instance(object):
        __metaclass__ = Singleton

    instance1 = Instance()
    instance2 = Instance()

    assert instance1 is instance2
    assert instance1.__class__ is instance2.__class__

    assert isinstance(Instance().ansible_info['version'], str) is True
    assert isinstance(Instance().ansible_info['connection_plugins'], dict) is True
    assert isinstance(Instance().ansible_info['connection_plugins']['ansible_connections'], list) is True
    assert isinstance(Instance().ansible_info['connection_plugins']['netcommon_connections'], list) is True

# Generated at 2022-06-13 16:54:28.097485
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class A(metaclass=Singleton):
        pass
    a = A()
    b = A()
    assert a is b


# Generated at 2022-06-13 16:54:32.444354
# Unit test for constructor of class Singleton
def test_Singleton():
    class A(metaclass=Singleton):
        pass

    class B(metaclass=Singleton):
        pass

    a1 = A()
    a2 = A()
    b1 = B()
    b2 = B()

    assert a1 is a2
    assert b1 is b2
    assert a1 is not b1
    assert a1 is not b2
    assert a2 is not b1
    assert a2 is not b2

# Generated at 2022-06-13 16:54:34.886005
# Unit test for constructor of class Singleton
def test_Singleton():
    class SomeClass(object):
        __metaclass__ = Singleton
        def __init__(self, s):
            self.s = s
    assert id(SomeClass('foo')) == id(SomeClass('bar'))

# Generated at 2022-06-13 16:54:38.344017
# Unit test for constructor of class Singleton
def test_Singleton():
    class X(object):
        __metaclass__ = Singleton

        def __init__(self, x):
            self.x = x

    a = X(300)
    b = X(100)
    assert id(a) == id(b)
    assert a.x == b.x == 100

if __name__ == "__main__":
    test_Singleton()

# Generated at 2022-06-13 16:54:43.249493
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    # Test that every call return the same object
    class Test(object):
        __metaclass__ = Singleton
        def __init__(self, tag):
            self._tag = tag
        def get_tag(self):
            return self._tag

    test1 = Test("hello")
    assert test1.get_tag() == "hello"
    assert test1.get_tag() == Test("hello").get_tag()
    test1._tag = "bye bye"
    assert test1.get_tag() == "bye bye"
    assert test1.get_tag() == Test("hello").get_tag()
    assert test1.get_tag() == Test("bye bye").get_tag()

# Generated at 2022-06-13 16:54:47.463889
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class SingletonTest(object):
        """Test singleton class
        """
        __metaclass__ = Singleton

        def __init__(self):
            self.test = True

    instance1 = SingletonTest()
    instance2 = SingletonTest()
    assert(id(instance1) == id(instance2))

# Generated at 2022-06-13 16:54:53.803817
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class X(object):
        __metaclass__ = Singleton

        def __init__(self):
            self.value = 17

    x1 = X()
    x2 = X()
    assert x1 is x2
    assert 17 == x1.value
    assert 17 == x2.value
    x1.value = 42
    assert 42 == x2.value



# Generated at 2022-06-13 16:55:01.544372
# Unit test for method __call__ of class Singleton
def test_Singleton___call__():
    class TestClass(object):
        __metaclass__ = Singleton
        def __init__(self, val):
            self.val = val

    # Testing that our singleton has the 'val' attribute set to 1
    obj1 = TestClass(1)
    assert obj1.val == 1

    # Testing that our singleton still has the 'val' attribute set to 1
    obj2 = TestClass(2)
    assert obj2.val == 1

# Testing that our singleton still has the 'val' attribute set to 1
test_Singleton___call__()