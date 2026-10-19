

# Generated at 2022-06-13 16:35:56.109296
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    tlock = threading.Lock()
    @lock_decorator(lock=tlock)
    def func_lock(x):
        return x + 1
    assert func_lock(1) == 2
    class CTest:
        @lock_decorator(attr='_lock')
        def func_attr(self, x):
            return x + 1
    ct = CTest()
    ct._lock = tlock
    assert ct.func_attr(1) == 2
    # No lock
    @lock_decorator()
    def func_none(x):
        return x + 1
    assert func_none(1) == 2
    # No lock
    class CTest:
        @lock_decorator()
        def func_attr(self, x):
            return x + 1

# Generated at 2022-06-13 16:36:04.780186
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import unit_tests.support as support
    from unit_tests.support import _stderr_fd
    import sys
    import random

    class TestClass(object):
        @lock_decorator(attr='_lock')
        def test_method(self):
            self.test_attr += 1

    class TestClassUsingLockObject(object):
        def __init__(self):
            self._lock = mock.Mock()

        @lock_decorator(lock=self._lock)
        def test_method(self):
            self.test_attr += 1

    # Test with a simple lock object
    tc = TestClass()
    tc._lock = mock.Mock()

# Generated at 2022-06-13 16:36:11.798282
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    mylock = threading.Lock()
    class A(object):
        def __init__(self):
            self._internal_lock = mylock

    a = A()
    @lock_decorator(attr='_internal_lock')
    def test_method(self):
        print('test method')
        assert self == a
    test_method(a)

    @lock_decorator(lock=mylock)
    def test_function(self):
        print('test function')
        assert self == a
    test_function(a)

# Generated at 2022-06-13 16:36:17.423203
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    lock_decorator used with a threading Lock.
    '''

    import threading
    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def a_func(val):
        return val

    # a_func returns value sent to function
    assert(a_func(1) == 1)



# Generated at 2022-06-13 16:36:25.833837
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestLock(object):

        def __init__(self):
            self._lock = threading.Lock()
            self.test_list = []

        @lock_decorator(attr='_lock')
        def test(self):
            # This should lock ``self._lock``
            self.test_list.append('test1')
            time.sleep(1)
            self.test_list.append('test2')

    t = TestLock()

    ts = []

    def thread_test():
        t.test()

    for i in range(3):
        temp = threading.Thread(target=thread_test)
        ts.append(temp)
        temp.start()

    for t in ts:
        t.join()


# Generated at 2022-06-13 16:36:34.664779
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    import threading
    class Class(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='lock')
        def method1(self):
            self.value += 1

        @lock_decorator(lock=threading.Lock())
        def method2(self):
            self.value -= 1

    obj = Class()

# Generated at 2022-06-13 16:36:45.331440
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class L(object):
        _l = threading.Lock()
        def f(self):
            return 0
        def g(self):
            return 1

        @lock_decorator(attr='_l')
        def h(self):
            return 2

        @lock_decorator(lock=threading.Lock())
        def i(self):
            return 3

    l = L()
    # Function f not decorated, should not have a lock
    assert not hasattr(l.f, '_lock')

    # Function g not decorated, should not have a lock
    assert not hasattr(l.g, '_lock')

    # Function h has lock decorator, should have a lock
    assert hasattr(l.h, '_lock')

# Generated at 2022-06-13 16:36:54.870588
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    lock = threading.Lock()
    order = []

    class Foo:
        def __init__(self, lock):
            self.lock = lock

        @lock_decorator(attr='lock')
        def func(self):
            # time.sleep(1)
            order.append('func')
            assert True

        @lock_decorator(lock=lock)
        def func2(self):
            # time.sleep(1)
            order.append('func2')
            assert True

    foo = Foo(lock)

    threads = [
        threading.Thread(target=foo.func),
        threading.Thread(target=foo.func),
        threading.Thread(target=foo.func2),
        threading.Thread(target=foo.func2),
    ]

# Generated at 2022-06-13 16:37:05.562106
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo:
        _lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def test(self, val):
            print(val)

    class Bar:
        @lock_decorator(lock=threading.Lock())
        def test(self, val):
            print(val)

    for cls in (Foo, Bar):
        foo1 = cls()
        foo2 = cls()
        foo1.test('foo1')
        foo2.test('foo2')
        # If locking is working no exception will be raised.
        # This is essentially a test that lock_decorator does
        # not deadlock.
        for f in (foo1, foo2):
            f.test('foo1')


# Generated at 2022-06-13 16:37:15.318947
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    lock = threading.Lock()
    class LockDecorator(object):
        def __init__(self):
            self.foo = 0
            self.bar_lock = threading.Lock()
        @lock_decorator(lock=lock)
        def test(self):
            time.sleep(0.2)
            self.foo += 1
        @lock_decorator(attr='bar_lock')
        def test_attr(self):
            time.sleep(0.2)
            self.bar += 1

    # Test class-level lock
    foo1 = LockDecorator()
    foo2 = LockDecorator()
    bar1 = LockDecorator()
    bar2 = LockDecorator()
    threads = []
    for _ in range(10):
        threads

# Generated at 2022-06-13 16:37:26.091901
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    global_lock = threading.Lock()

    class TestLock():

        def __init__(self):
            self.lock1 = threading.Lock()
            self.lock2 = threading.Lock()

        @lock_decorator(attr='lock1')
        def test1(self, data):
            return data

        @lock_decorator(lock=global_lock)
        def test2(self, data):
            return data

        @lock_decorator(attr='missing_lock_attr')
        def test3(self, data):
            return data

    test = TestLock()

    assert test.test1(1) == 1
    assert test.test2(2) == 2

# Generated at 2022-06-13 16:37:38.032401
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    class Foobar(object):
        @lock_decorator(attr='_foobar_lock')
        def foo(self):
            return 1
    o = Foobar()
    o._foobar_lock = lock
    assert o.foo() == 1
    assert o._foobar_lock
    assert lock is o._foobar_lock
    # if lock copied, it cannot be acquired
    try:
        with lock:
            pass
    except:
        raise AssertionError('Lock is not working')
    class Baz(object):
        @lock_decorator(attr='_baz_lock')
        def bar(self):
            return 2
        @lock_decorator(lock=threading.Lock())
        def baz(self):
            return 3


# Generated at 2022-06-13 16:37:46.510178
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread, Lock
    import time
    import random

    lock = Lock()
    lock_attr = Lock()

    def target(name, lock, lock_attr, num, delay):
        print('Thread %s started' % name)
        time.sleep(delay)
        with lock:
            print(name, num, time.time())
        time.sleep(delay)
        with lock_attr:
            print(name, num, time.time())
        print('Thread %s finished' % name)

    threads = []
    for i in range(10):
        name = 'Thread-%d' % i
        # Thread will sleep between 0 and 5 seconds
        delay = random.randint(0, 5)

# Generated at 2022-06-13 16:37:55.222063
# Unit test for function lock_decorator
def test_lock_decorator():
    from ansible.module_utils.facts.utils.lock_decorator import Lock
    import threading

    class DummyClass():
        _lock1 = Lock()
        _lock2 = threading.Lock()

        @lock_decorator(attr='_lock1')
        def method1(self):
            pass

        @lock_decorator(lock=_lock2)
        def method2(self):
            pass

    dummy_obj = DummyClass()
    assert hasattr(dummy_obj._lock1, '__enter__')
    assert hasattr(dummy_obj._lock1, '__exit__')
    assert hasattr(dummy_obj._lock2, '__enter__')
    assert hasattr(dummy_obj._lock2, '__exit__')

# Generated at 2022-06-13 16:38:04.821153
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except (ImportError, SyntaxError):
        import unittest
        raise unittest.SkipTest('lock_decorator unit test requires threading')
    import threading
    import random
    import time
    import logging

    logger = logging.getLogger()

    class Mock(object):

        def __init__(self, *args, **kwargs):
            self.iterations = kwargs.pop('iterations', None)
            self.num_threads = kwargs.pop('num_threads', None)
            if self.iterations is None:
                self.iterations = random.randint(1, 10)
            if self.num_threads is None:
                self.num_threads = random.randint(1, 8)

# Generated at 2022-06-13 16:38:15.067002
# Unit test for function lock_decorator
def test_lock_decorator():
    from ansible.utils.sentinel import Sentinel
    import threading
    lock = threading.Lock()
    new_lock = threading.Lock()
    sentinel = Sentinel()
    sentinel_lock = Sentinel()
    inner_call_value = Sentinel()

    class MyClass(object):
        _missing_lock_attr = threading.Lock()
        first_attr = threading.Lock()
        second_attr = threading.Lock()

        @lock_decorator(attr='first_attr')
        def first_method(self, arg):
            assert self.first_attr is not None
            assert self.first_attr is not self.second_attr
            return inner_call_value

        @lock_decorator(attr='second_attr')
        def second_method(self, arg):
            assert self.second_

# Generated at 2022-06-13 16:38:21.318972
# Unit test for function lock_decorator
def test_lock_decorator():

    from threading import Lock, RLock
    import time
    import pytest

    class Foo(object):

        def __init__(self, lock_class, attr):
            self.lock_class = lock_class
            self.attr = attr
            object.__setattr__(self, attr, self.lock_class())
            self.counter = 0

        def __setattr__(self, name, value):
            if name == self.attr:
                # This is a horrible hack but I can't
                # figure out a better way to validate
                # that the lock is used.
                self.counter += 1
            return object.__setattr__(self, name, value)


# Generated at 2022-06-13 16:38:28.210668
# Unit test for function lock_decorator
def test_lock_decorator():
    class A:
        def __init__(self):
            self._lock = None

        @lock_decorator(attr='_lock')
        def a1(self):
            pass

    with A() as a:
        # Assert that the internal lock is not yet set
        assert a._lock is None

        # Assert that when calling a1(), the lock gets created
        a.a1()
        assert a._lock is not None


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:38:36.045076
# Unit test for function lock_decorator
def test_lock_decorator():
    import os
    import threading
    import tempfile
    import unittest

    class Test(object):
        def __init__(self):
            self.path = None

        @lock_decorator(lock=threading.Lock())
        def test1(self):
            self.path = self._make_file()
            return

        @lock_decorator(attr='_lock')
        def test2(self):
            self.path = self._make_file()
            return

        def _lock(self):
            return threading.Lock()

        def _make_file(self):
            path = tempfile.mktemp()
            with open(path, 'w') as f:
                f.write('foo')
            return path


# Generated at 2022-06-13 16:38:46.998700
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass():
        def __init__(self):
            self._callback_lock = threading.Lock()

        # Add the lock using attr
        @lock_decorator(attr='_callback_lock')
        def callback1(self, text):
            # Should be locked
            print('callback1: {0}: {1}'.format(threading.current_thread().ident, text))
            threading.current_thread().callback1 = text

        # Add the lock explicitly
        @lock_decorator(lock=threading.Lock())
        def callback2(self, text):
            # Should be locked
            print('callback2: {0}: {1}'.format(threading.current_thread().ident, text))
            threading.current_thread().callback2 = text


# Generated at 2022-06-13 16:38:58.587113
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    class SampleClass(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def lock_attr(self, *args, **kwargs):
            return (args, kwargs)

        @lock_decorator()
        def lock_no_attr(self, *args, **kwargs):
            return (args, kwargs)

    sample = SampleClass()

    with mock.patch('threading.Lock.acquire', autospec=True) as mock_lock_acquire:
        sample.lock_attr(1, 2, 3)

    mock_lock_acquire.assert_called_once()


# Generated at 2022-06-13 16:39:03.286667
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Unit test for function ``lock_decorator``
    '''
    import threading
    global test_lock_decorator_result
    lock = threading.Lock()
    test_lock_decorator_result = 0

    @lock_decorator(attr='missing_lock_attr')
    def func1(self):
        global test_lock_decorator_result
        test_lock_decorator_result += 1

    @lock_decorator(lock=lock)
    def func2():
        global test_lock_decorator_result
        test_lock_decorator_result += 1

    # func1 should raise an exception when the attr is missing
    try:
        func1(object())
    except AttributeError:
        pass

# Generated at 2022-06-13 16:39:10.318036
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread

    class Something(object):
        _lock = Lock()

        @lock_decorator()
        def foo(self):
            pass

        @lock_decorator(attr='_lock')
        def bar(self):
            pass

    foo_lock = Lock()
    bar_lock = Lock()

    @lock_decorator(lock=foo_lock)
    def foo():
        pass

    @lock_decorator(lock=bar_lock)
    def bar():
        pass

    def _foo(lock):
        lock.acquire()
        lock.release()

    def _bar(lock):
        lock.acquire()
        lock.release()

    s = Something()


# Generated at 2022-06-13 16:39:18.189828
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    This function tests the lock_decorator function
    '''
    import threading
    _lock = threading.Lock()
    _other_lock = threading.Lock()
    class NoLock(object):
        pass
    # When a lock is passed explicitly, it should work as expected
    @lock_decorator(lock=_lock)
    def with_explicit_lock(arg):
        return arg
    # When a pre-defined lock location is used, it should
    # also work as expected
    @lock_decorator(attr='lock')
    def with_defined_lock(arg):
        return arg
    # If a lock is not found, a ``RuntimeError`` should be raised
    # regardless of whether an attribute is defined or not

# Generated at 2022-06-13 16:39:29.537724
# Unit test for function lock_decorator
def test_lock_decorator():
    import random
    import threading

    class Cls(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.l = []

        @lock_decorator(attr='lock')
        def append(self):
            self.l.extend([random.randint(1, 10)])

    obj = Cls()

    def thread_1():
        for _ in range(100):
            obj.append()

    def thread_2():
        for _ in range(100):
            obj.append()

    for _ in range(100):
        t1 = threading.Thread(target=thread_1)
        t2 = threading.Thread(target=thread_2)
        t1.start()
        t2.start()
        t1.join()
        t2

# Generated at 2022-06-13 16:39:33.089803
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class SomeClass:
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method(self, val):
            print(val)

    obj = SomeClass()
    obj.method('hello')


# Generated at 2022-06-13 16:39:42.756950
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def some_function(a, b, c):
        assert lock._is_owned()
        return a * b * c

    a, b, c = some_function(1, 2, 3)
    assert a == 6

    lock2 = threading.Lock()
    @lock_decorator(attr='_lock', lock=lock2)
    class TestLock(object):
        def __init__(self):
            self._lock = lock2

        def some_method(self, a, b, c):
            assert lock2._is_owned()
            return a * b * c

    o = TestLock()
    a, b, c = o.some_method(4, 5, 6)

# Generated at 2022-06-13 16:39:55.337753
# Unit test for function lock_decorator
def test_lock_decorator():

    class Test:
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_attr(self, count):
            return count

        @lock_decorator(lock=threading.Lock())
        def test_lock(self, count):
            return count

    t = Test()

    n = 10
    with ProcessPoolExecutor(max_workers=n) as ex:
        futures = [ex.submit(t.test_attr, count) for count in range(n)]
        returned = list(f.result() for f in futures)
        assert returned == list(range(n))


# Generated at 2022-06-13 16:40:00.497808
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def some_method():
        return True

    @lock_decorator(attr='lock')
    def another_method(self):
        return True

    class TestClass(object):
        def __init__(self):
            self.lock = lock

    assert some_method()
    assert another_method(TestClass())

# Generated at 2022-06-13 16:40:06.999441
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo():
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator()
        def foo(self):
            pass

        @lock_decorator(attr='_lock')
        def bar(self):
            pass

        @lock_decorator(lock=threading.Lock())
        def baz(self):
            pass


# Generated at 2022-06-13 16:40:16.181248
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class X:
        def __init__(self):
            self.counter = 0
            self.lock = threading.Lock()

    f = lock_decorator('lock')(X.counter.__set__)

    x = X()

    f(x, 1)
    f(x, 2)

    assert x.counter == 2

# Generated at 2022-06-13 16:40:26.603781
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class FakeLock(object):
        def __init__(self):
            self.acquire_called = False
            self.release_called = False

        def __enter__(self):
            self.acquire_called = True

        def __exit__(self, type, value, tb):
            self.release_called = True

    class TestLockDecorator(unittest.TestCase):
        def test_lock_decorator(self):
            lock = FakeLock()
            class X(object):
                def __init__(self):
                    self._lock = lock

                @lock_decorator(attr='_lock')
                def method(self):
                    pass

            x = X()
            x.method()
            assert lock.acquire_called is True

# Generated at 2022-06-13 16:40:35.580899
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    d = {
        'lock': threading.Lock(),
    }
    @lock_decorator(lock=d['lock'])
    def test_lock(expected, result=None):
        assert(not d['lock'].acquire(False))
        if result is not None:
            return result
        return expected

    assert(test_lock('expected', 'result') == 'result')
    assert(test_lock('expected') == 'expected')

    class Test(object):
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def test_attr(self, expected, result=None):
            assert(not self.lock.acquire(False))
            if result is not None:
                return result
            return expected



# Generated at 2022-06-13 16:40:43.048638
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread
    from time import sleep
    class Dummy(object):
        def __init__(self):
            self._lock = Lock()
            self.value = 0

        @lock_decorator(attr='_lock')
        def incr(self):
            sleep(0.1)
            # to ensure the value is a multiple at the end
            self.value += 2

    data = [Dummy() for x in range(0, 20)]
    threads = [Thread(target=d.incr) for d in data]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    for d in data:
        assert d.value == 2, 'Did not get the expected value of 2, got %d instead' % d.value


# Generated at 2022-06-13 16:40:53.108918
# Unit test for function lock_decorator
def test_lock_decorator():
    # pylint: disable=too-few-public-methods,too-many-instance-attributes
    class TestLock(object):
        '''Test class with in place lock decorator'''
        lock = None

        def __init__(self, lock=None):
            self.lock = lock
            self.result = None

        @lock_decorator(attr='lock')
        def do_something(self):
            '''Test method'''
            self.result = 'something'

    # Test with no lock
    test = TestLock()
    test.do_something()
    assert test.result == 'something'

    # Test with a lock
    result = None
    test = TestLock(lock_decorator.lock_decorator.lock)
    test.do_something()

# Generated at 2022-06-13 16:41:01.462610
# Unit test for function lock_decorator
def test_lock_decorator():
    class Test():

        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def do_something(self, value):
            self.value = value

        @lock_decorator(lock=threading.Lock())
        def do_something_else(self, value):
            self.value = value

    # Test the simple case
    t = Test()
    t.do_something('foo')
    assert(t.value == 'foo')

    # Test the complex case
    t = Test()
    t.do_something_else('foo')
    assert(t.value == 'foo')

# Generated at 2022-06-13 16:41:08.390940
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import copy
    class A(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.attr = "foo"
            self.list = []

    @lock_decorator(attr="lock")
    def add_to_list(this, item):
        this.list.append(item)

    def modify_attr(this):
        this.attr = "bar"

    # Create an instance of A
    a1 = A()
    # Create a list of two threads
    threads1 = [
        threading.Thread(target=add_to_list, args=[a1, 1]),
        threading.Thread(target=add_to_list, args=[a1, 2])
    ]
    # start each thread
    for thread in threads1:
        thread

# Generated at 2022-06-13 16:41:13.828825
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    def success_decorator():
        class Test(object):
            def __init__(self):
                self._doit_lock = threading.Lock()

            @lock_decorator(attr='_doit_lock')
            def doit(self):
                return True

            @lock_decorator(lock=threading.Lock())
            def doit2(self):
                return True

        t = Test()
        assert t.doit() is True
        assert t.doit2() is True

    def failure_decorator():
        '''Confirm that we don't get exceptions when the lock isn't set
        '''
        class Test(object):
            def __init__(self):
                # simulate a lock not being set
                self._doit_lock = None


# Generated at 2022-06-13 16:41:24.768058
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading
    import functools
    import sys

    class MockObj(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_method(self):
            pass


    # Make sure that the first argument is self
    obj = MockObj()
    with mock.patch.object(MockObj, 'test_method') as m:
        obj.test_method()

    m.assert_called_once_with()

    # Make sure that the lock was used
    with mock.patch('threading.Lock.__enter__') as enter:
        with mock.patch.object(MockObj, 'test_method') as m:
            obj.test_method()

    # PY3 has _acquire() as a context manager method

# Generated at 2022-06-13 16:41:33.020848
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import _thread
    import time
    _MAX_THREADS = 10
    _MAX_INC = 1000

    class Counter():
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='lock')
        def inc(self):
            self.value += 1
            time.sleep(0.001)

    def thread_func(counter):
        for _ in range(_MAX_INC):
            counter.inc()

    counter = Counter()
    threads = []
    for i in range(_MAX_THREADS):
        threads.append(threading.Thread(target=thread_func,
                        args=(counter, )))
    for t in threads:
        t.start()
    for t in threads:
        t.join

# Generated at 2022-06-13 16:41:44.840737
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread, Lock
    import time

    class MyClass(object):
        def __init__(self):
            self._my_lock = Lock()
            self.my_list = []

        @lock_decorator(attr='_my_lock')
        def mod_list(self, item):
            self.my_list.append(item)

    my = MyClass()
    threads = []
    for i in range(5):
        t = Thread(target=my.mod_list, name=i, args=(i,))
        t.start()
        threads.append(t)

    # Wait for threads to finish
    time.sleep(1)

    assert len(my.my_list) == 5

# Generated at 2022-06-13 16:41:54.097530
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class Dummy(object):
        def __init__(self):
            self._my_lock = threading.Lock()

        @lock_decorator()
        def no_lock(self):
            return

        @lock_decorator(lock=threading.Lock())
        def with_lock(self):
            return

        @lock_decorator(attr='_my_lock')
        def with_attr(self):
            return

    dummy = Dummy()
    dummy.no_lock()
    dummy.with_lock()
    dummy.with_attr()

# Generated at 2022-06-13 16:41:59.983735
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    class Bar(object):

        def __init__(self):
            self.counter = 0
            self.lock = Lock()

        @lock_decorator(lock=Lock())
        def baz_1(self):
            self.counter += 1
            return self.counter

        @lock_decorator(attr='lock')
        def baz_2(self):
            self.counter += 1
            return self.counter

    b = Bar()
    print('b.counter && b.baz_1() && b.baz_2() == %s %s %s' % (b.counter, b.baz_1(), b.baz_2()))
    b.counter = 0

# Generated at 2022-06-13 16:42:06.621478
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Dummy(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.called = False

        @lock_decorator(attr='_lock')
        def send_callback(self):
            self.called = True

    d = Dummy()
    d.send_callback()
    assert d.called
    d.called = False
    d.send_callback()
    assert d.called

# Generated at 2022-06-13 16:42:17.402435
# Unit test for function lock_decorator
def test_lock_decorator():

    # Import here to prevent failure in Python versions without unittest
    import unittest

    class FakeLock(object):
        '''This is a fake lock for the decorator unit tests'''
        def __init__(self):
            self.exception = None

        def __enter__(self):
            pass

        def __exit__(self, type, value, tb):
            if value is not None:
                self.exception = value
                return True

    class TestLockDecorator(unittest.TestCase):
        '''Test the lock_decorator function'''

        def setUp(self):
            # Create a fake lock to test the decorator
            self.lock = FakeLock()
            self.lock_count = 0

            # Create a lock_decorated method to test

# Generated at 2022-06-13 16:42:26.318998
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import random
    import threading
    import queue
    import functools

    number_of_threads = 10
    queue_length = 10
    queue_timeout = 0.5

    class Worker(threading.Thread):
        def setup(self, func, q):
            self.func = func
            self.q = q
            return

        def run(self):
            while not self.q.empty():
                try:
                    i = self.q.get(timeout=queue_timeout)
                except queue.Empty:
                    break
                if random.random() > 0.5:
                    self.q.task_done()
                    continue
                self.func(i)
                self.q.task_done()
            return


# Generated at 2022-06-13 16:42:35.205817
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread

    class A(object):
        _lock = Lock()

        @lock_decorator(attr='_lock')
        def method1(self):
            self.count += 1

    class B(object):
        @lock_decorator(lock=Lock())
        def method2(self):
            self.count += 1

    A.count = 0
    a = A()
    threads = []
    for i in range(0, 4):
        t = Thread(target=a.method1)
        t.daemon = True
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    assert A.count == 4

    B.count = 0
    b = B()
    threads = []

# Generated at 2022-06-13 16:42:45.745651
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class MyClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self.value += 1
            print('From ', threading.current_thread().name, ':',
                  self.value)

    class Thread(threading.Thread):
        def __init__(self, name):
            super(Thread, self).__init__(name=name)
            self._running = True

        def run(self):
            while self._running:
                my.increment()

        def stop(self):
            self._running = False


    my = MyClass()
    thread1 = Thread('Thread1')
    thread2 = Thread('Thread2')


# Generated at 2022-06-13 16:42:53.022365
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Dummy(object):
        lock = threading.Lock()

        _mylock = False

        @lock_decorator()
        def dummy_method(self):
            return self

        @lock_decorator(attr='lock')
        def dummy_method2(self):
            return self

        @lock_decorator(lock=Dummy.lock)
        def dummy_method3(self):
            return self
    assert Dummy.dummy_method(Dummy()) is Dummy()
    assert Dummy.dummy_method2(Dummy()) is Dummy()
    assert Dummy.dummy_method3(Dummy()) is Dummy()

# Generated at 2022-06-13 16:43:03.448094
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import mock

    class TestClass(object):
        '''Helper class to test the lock decorator.
        '''
        def __init__(self):
            self._lock = None

        @lock_decorator(attr='_lock')
        def test_method(self):
            return True

    class Test(unittest.TestCase):
        '''Test the lock decorator
        '''

        @mock.patch.object(TestClass, 'test_method',
                           mock.MagicMock(
                               side_effect=TestClass.test_method))
        def test_lock_decorator_lock_not_set(self):
            '''Test that the lock is set before method execution.
            '''
            # Create the instance
            instance = TestClass()
            # The lock should

# Generated at 2022-06-13 16:43:29.941831
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class Test(object):
        # A lock attribute
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method(self):
            # This should always run as if it was the only thing executing
            # in a single thread/process
            print('Test.method')

        @lock_decorator(lock=threading.Lock())
        def method2(self):
            # Since lock is set, this should always run as if it was the only
            # thing executing in a single thread/process
            print('Test.method2')

    t = Test()
    t.method()
    t.method2()


if __name__ == '__main__':
    test_lock_decorator()

# Generated at 2022-06-13 16:43:40.403712
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class TestFoo(object):
        @lock_decorator(attr='_lock')
        def method1(self):
            self.result.append(1)

        @lock_decorator(lock=threading.Lock())
        def method2(self):
            self.result.append(2)

        @lock_decorator(attr='_lock')
        def method3(self, arg):
            self.result.append(arg)

        @lock_decorator(lock=threading.Lock())
        def method4(self, arg):
            self.result.append(arg)

    class LockDecoratorTests(unittest.TestCase):
        def test_with_attr(self):
            foo = TestFoo()
            foo._lock = None


# Generated at 2022-06-13 16:43:46.784296
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Something():
        @lock_decorator(attr='_lock')
        def _send_callback(self):
            self.num += 1

        def __init__(self):
            self.num = 0
            self._lock = threading.Lock()

    def do_work(something):
        # Do some work
        something._send_callback()

    something = Something()

    # Fire up a bunch of threads
    threads = [threading.Thread(target=do_work, args=(something,)) for i in range(500)]

    # Start all of the threads
    for t in threads:
        t.start()

    # Wait for all of the threads to complete
    for t in threads:
        t.join()

    # Make sure no one has clobbered the value
    assert something.num == len

# Generated at 2022-06-13 16:43:54.653082
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        def __init__(self):
            self.test_attr = threading.Lock()

        @lock_decorator(attr='test_attr')
        def locking_method(self, val):
            assert self.test_attr.locked()
            return val

        @lock_decorator(lock=threading.Lock())
        def locking_method_passed_lock(self, val):
            assert lock.locked()
            return val

    test = Test()

    assert not test.test_attr.locked()
    assert test.locking_method('foo') == 'foo'
    assert not test.test_attr.locked()

    lock = threading.Lock()
    assert not lock.locked()
    assert test.locking_method_passed_lock('bar') == 'bar'

# Generated at 2022-06-13 16:43:59.458152
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestLockDecorator(object):
        def __init__(self):
            self.some_attribute = None
            self.some_lock = threading.Lock()

        @lock_decorator()
        def test_missing_lock_arg(self):
            assert True

        @lock_decorator('some_lock')
        def test_lock_arg(self):
            assert True

        @lock_decorator(lock=threading.Lock())
        def test_lock_arg_lock(self):
            assert True

# Generated at 2022-06-13 16:44:11.147055
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread, Lock
    import time
    import sys

    if sys.version_info < (3,):
        # Lock.acquire() and Lock.release() didn't become context managers
        # until Python 3.
        return

    l = Lock()
    count = 0
    end_at = 10

    def sleeper():
        global count
        while True:
            with l:
                count += 1
                print("Count: {}".format(count))
                if count >= end_at:
                    break
            time.sleep(1)

    s = Thread(target=sleeper)
    s.daemon = True
    s.start()
    s.join()

    l = Lock()
    count = 0
    end_at = 10

    class Sleeper(object):
        _lock = Lock()


# Generated at 2022-06-13 16:44:19.801697
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    lock = threading.Lock()

    @lock_decorator(attr='_lock')
    def some_func(self, val):
        time.sleep(1)
        return val

    class Foo:
        def __init__(self):
            self._lock = lock

        def __call__(self, val):
            return some_func(self, val)

    expected = ['bar', 'baz', 'bat']
    def worker(foo):
        for val in expected:
            foo(val)

    foo = Foo()

    # Test with 2 threads updating the same object
    # to test that the lock works
    threads = []
    for i in range(2):
        threads.append(threading.Thread(target=worker, args=(foo,)))
        threads[-1].start

# Generated at 2022-06-13 16:44:32.109175
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass(object):
        def __init__(self):
            self.accessed = 0
            self.lock = threading.Lock()
            self.counter_lock = threading.Lock()

        @lock_decorator(attr='lock')
        def access(self):
            self.accessed += 1
            return self.accessed

    test_instance = TestClass()

    def run():
        i = 0
        while i < 10000:
            i += 1
            with test_instance.counter_lock:
                test_instance.accessed += 1

    threads = []
    for i in range(100):
        thr = threading.Thread(target=run)
        threads.append(thr)
        thr.start()

    for thr in threads:
        thr.join()

    assert test

# Generated at 2022-06-13 16:44:40.881342
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class Fake(object):

        _lock = None

        @lock_decorator(lock=threading.Lock())
        def method(self):
            if self._lock is None:
                self._lock = 1

    class Fake2(object):

        _lock = None

        @lock_decorator(attr='_lock')
        def method(self):
            if self._lock is None:
                self._lock = 1

    # See if we can add the method to a class
    f = Fake()
    assert f.method()
    # And expect it to have the right value
    assert f._lock == 1

    # Can we put it directly on the class?
    Fake.method()
    assert Fake._lock == 1

    # Does it work when specified attr is None?
    f = Fake2()


# Generated at 2022-06-13 16:44:51.467061
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread

    class Foo(object):
        def __init__(self, delay=1):
            self._lock = Lock()
            self.counter = 0
            self.delay = delay

        @lock_decorator(attr='_lock')
        def callback(self):
            import time
            # Simulate doing something that takes a long time
            time.sleep(self.delay)
            self.counter += 1

    foo = Foo(delay=1)
    thread1 = Thread(target=foo.callback)
    thread2 = Thread(target=foo.callback)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    assert foo.counter == 1

    thread1 = Thread(target=foo.callback)

# Generated at 2022-06-13 16:45:32.246871
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestLock(object):

        def __init__(self):
            self._lock = threading.Lock()
            self._data = 0

        @lock_decorator(attr='_lock')
        def do_something(self, wait=False):
            if wait:
                time.sleep(1)
            self._data += 1
            return self._data

        @lock_decorator(lock=threading.Lock())
        def do_something_else(self, wait=False):
            if wait:
                time.sleep(1)
            self._data += 1
            return self._data

    # Make sure that it works without going through the lock
    test = TestLock()
    test.do_something(wait=True)
    assert test._data == 2

    # Make sure that

# Generated at 2022-06-13 16:45:40.168510
# Unit test for function lock_decorator
def test_lock_decorator():

    # Python2 doesn't have ``nonlocal``
    import sys
    if sys.version_info[0] >= 3:
        from unittest import mock
        from threading import Lock
        import threading

        class test_lock_decorator(object):
            _callback_lock = Lock()

            def __init__(self):
                self.called = False

            def __call__(self, *args, **kwargs):
                self.args = args
                self.kwargs = kwargs

            @lock_decorator(attr='_callback_lock')
            def test_lock_with_attr(self, *args, **kwargs):
                self.called = True
                self.__call__(*args, **kwargs)


# Generated at 2022-06-13 16:45:45.757761
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import random

    class MyObj:
        class_lock = threading.Lock()

        def __init__(self):
            self.instance_lock = threading.Lock()
            self.total = 0
            self.class_total = 0

        @lock_decorator(attr='class_lock')
        def add_total_class(self, n):
            for i in range(n):
                self.class_total += 1
                time.sleep(random.random())
            return self.class_total

        @lock_decorator(attr='instance_lock')
        def add_total_instance(self, n):
            for i in range(n):
                self.total += 1
                time.sleep(random.random())
            return self.total


# Generated at 2022-06-13 16:45:51.030556
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()

    class Example(object):
        def __init__(self):
            self._callback_lock = lock
        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            pass

        @lock_decorator(lock=lock)
        def some_method(self):
            pass

    return Example()

