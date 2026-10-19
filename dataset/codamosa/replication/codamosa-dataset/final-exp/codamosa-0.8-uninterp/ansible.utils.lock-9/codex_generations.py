

# Generated at 2022-06-13 16:35:43.717786
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    if sys.version_info < (3, 0):
        import threading
        import mock

        class TestClass(object):

            def __init__(self):
                self._lock = threading.Lock()
                self._value = 0

            @lock_decorator(attr='_lock')
            def increment(self):
                '''increment value'''
                self._value += 1
                return self._value

        # Instantiate an instance of the test class
        t = TestClass()

        # assert value before increment
        assert t.increment() == 1

        # assert value after increment
        assert t.increment() == 2

        # set own instance to the increment method
        i_own = t.increment

        # check if instance lock is the same as class lock
        assert i_own._own_lock

# Generated at 2022-06-13 16:35:50.966507
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestObject(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='lock')
        def get_value(self):
            return self.value

        @lock_decorator(lock=threading.Lock())
        def set_value(self, value):
            self.value = value

    obj = TestObject()
    assert obj.get_value() == 0
    obj.set_value(1)
    assert obj.get_value() == 1

# Generated at 2022-06-13 16:36:00.611829
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread
    import time

    class Counter:
        def __init__(self, lock):
            self.lock = lock
            self.count = 0

        @lock_decorator(attr='lock')
        def increment(self):
            self.count += 1

        @lock_decorator(attr='lock')
        def get_value(self):
            return self.count

    counter = Counter(lock=lock_decorator.lock)

    # Start two threads and let them increment a shared resource
    # This should cause some contention and allow us to detect
    # race conditions.
    # Both threads need to be running concurrently in order to
    # detect race conditions, thus the sleep() calls are needed.
    def thread_task():
        counter.increment()
        time.sleep(0.1)

# Generated at 2022-06-13 16:36:11.799597
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass(object):
        def __init__(self):
            self._mylock = threading.Lock()

        @lock_decorator(attr='_mylock')
        def do_sum(self, x, y):
            return x + y

        @lock_decorator(lock=threading.Lock())
        def do_mul(self, x, y):
            return x * y

        @lock_decorator()
        def do_div(self, x, y):
            return x / y # This will raise a TypeError

    foo = TestClass()
    assert foo.do_sum(10, 100) == 110
    assert foo.do_mul(10, 100) == 1000

# Generated at 2022-06-13 16:36:22.586848
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    # This is the simplest usage, where we don't pass a lock,
    # but we expect a `_lock` to be defined on the instance
    class SomeClass(object):
        _lock = threading.Lock()
        @lock_decorator()
        def some_method(self):
            return True
    obj = SomeClass()
    assert obj.some_method()
    # Now we will explicitly set the lock, using the attr argument
    class SomeOtherClass(object):
        _lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def some_method(self):
            return True
    obj = SomeOtherClass()
    assert obj.some_method()
    # Now we will explicitly provide the lock, which will
    # override the attr value, if set
   

# Generated at 2022-06-13 16:36:32.508728
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading

    class TestLock(object):
        def __init__(self):
            self.count = 0

        @lock_decorator()
        def incr(self):
            self.count += 1

    class TestNoLock(object):
        def __init__(self):
            self.count = 0

        def incr(self):
            self.count += 1

    def test_shared_lock():
        test = TestLock()
        def run_incr(i):
            test.incr()
            print(i, 'finished')
        print('testing shared lock')
        threads = [threading.Thread(target=run_incr, args=(i,)) for i in range(100)]
        for t in threads:
            t.start()

# Generated at 2022-06-13 16:36:38.037470
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test:
        def __init__(self):
            self.attr_lock = threading.Lock()
        @lock_decorator('attr_lock')
        def foo(self):
            time.sleep(1)
            return True

        @lock_decorator(lock=threading.Lock())
        def bar(self):
            time.sleep(1)
            return True

    t = Test()
    start = time.time()
    t.foo()
    print(time.time() - start)
    start = time.time()
    t.foo()
    print(time.time() - start)
    start = time.time()
    t.bar()
    print(time.time() - start)
    start = time.time()
    t.bar()
   

# Generated at 2022-06-13 16:36:47.067808
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestObject:
        @lock_decorator(attr='_lock')
        def some_method(self):
            return

    obj = TestObject()
    obj._lock = threading.Lock()

    lock = threading.Lock()
    @lock_decorator(lock=lock)
    def class_method():
        return

    try:
        @lock_decorator(lock=lock, attr='_lock')
        def test_method():
            return
    except ValueError:
        pass
    except Exception as e:
        raise SystemExit('lock_decorator should fail when trying to use lock and attr at the same time: %s' % type(e))
    else:
        raise SystemExit('lock_decorator should fail when trying to use lock and attr at the same time')

# Generated at 2022-06-13 16:36:55.689044
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep

    class Test(object):
        _lock = threading.Lock()

        @staticmethod
        @lock_decorator(attr='_lock')
        def static_method(label):
            print('{}: start'.format(label))
            sleep(1)
            print('{}: end'.format(label))

        @classmethod
        @lock_decorator(attr='_lock')
        def class_method(cls, label):
            print('{}: start'.format(label))
            sleep(1)
            print('{}: end'.format(label))

        @lock_decorator(attr='_lock')
        def instance_method(self, label):
            print('{}: start'.format(label))
            sleep(1)

# Generated at 2022-06-13 16:37:04.230959
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Foo(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, val):
            time.sleep(0.01)
            self.value = val

    foo = Foo()
    for v in range(20):
        thread = threading.Thread(target=foo.send_callback, args=(v,))
        thread.start()
        thread.join()

    assert foo.value == 19

# Generated at 2022-06-13 16:37:15.844602
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    # Use threading.Lock() to prevent data inconsistency
    class Data:
        def __init__(self):
            self.n = 0
            self.data = dict()
            self.data_lock = threading.Lock()

        @lock_decorator(attr='data_lock')
        def get_data(self):
            return len(self.data)

        @lock_decorator(attr='data_lock')
        def new_data(self, data):
            self.data[self.n] = data
            self.n += 1

    def thread_process(n, data):
        for _ in range(n):
            data.new_data(data.get_data())


# Generated at 2022-06-13 16:37:25.406384
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import unittest
    import time

    class MockLock(object):
        def __init__(self):
            self.locked = False
        def __enter__(self):
            self.locked = True
        def __exit__(self, exc_type, exc_value, traceback):
            self.locked = False

    class LockDecoratorUnitTest(unittest.TestCase):
        def setUp(self):
            self._lock = threading.Lock()
            self._mock_lock = MockLock()
            self._counter = 0
            self._counter_with_lock = 0

        @lock_decorator(attr='_lock')
        def increment_counter_with_lock(self):
            self._counter_with_lock += 1


# Generated at 2022-06-13 16:37:35.746728
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    class TestClass:
        def __init__(self):
            self._state = None

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, new_state):
            # Just update the state attribute
            self._state = new_state

        @lock_decorator(lock=lock)
        def some_method(self):
            # do something else
            pass

    testobj = TestClass()
    testobj.send_callback('new state')
    assert testobj._state == 'new state'

    testobj.some_method()

if __name__ == '__main__':
    
    test_lock_decorator()

# Generated at 2022-06-13 16:37:38.737666
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Mock(object):
        def __init__(self):
            self.counter = 0
            self.lock = threading.Lock()

        @lock_decorator(lock=None)
        def increment(self):
            self.counter += 1
            return self.counter

        @lock_decorator(lock=self.lock)
        def increment_lock(self):
            self.counter += 1
            return self.counter

    m = Mock()
    assert m.increment() == 1
    assert m.increment_lock() == 2

# Generated at 2022-06-13 16:37:46.960477
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread, current_thread
    from time import sleep

    class Test(object):
        def __init__(self):
            self.lock = Lock()
            self.with_attr_lock = Lock()
            self.without_lock = Lock()

        @lock_decorator()
        def no_lock_provided(self):
            self.without_lock.acquire()
            sleep(0.05)
            self.without_lock.release()

            return True

        @lock_decorator(attr='lock')
        def with_attr_lock(self):
            self.with_attr_lock.acquire()
            sleep(0.05)
            self.with_attr_lock.release()

            return True


# Generated at 2022-06-13 16:37:55.928999
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import unittest2 as unittest
    except ImportError:
        import unittest

    import threading
    try:
        import unittest.mock as mock
    except ImportError:
        import mock

    counter = [0]

    class TestClass(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            counter[0] += 1
            return counter[0]

        @lock_decorator(lock=threading.Lock())
        def some_method(self):
            counter[0] += 1
            return counter[0]

    test = TestClass()


# Generated at 2022-06-13 16:38:05.438892
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep
    from datetime import datetime, timedelta

    class Example(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method_one(self):
            return datetime.utcnow()

        @lock_decorator(lock=threading.Lock())
        def method_two(self):
            return datetime.utcnow()

    e = Example()
    start = datetime.utcnow()

    def _thread_one():
        while (datetime.utcnow() - start) < timedelta(seconds=5):
            e.method_one()
            sleep(0.1)


# Generated at 2022-06-13 16:38:15.523088
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import log_360_logging
    class Base(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator()
        def base_method(self, message):
            logger = log_360_logging.getLogger('test_lock_decorator.Base')
            logger.info(message)

        @lock_decorator(attr='_lock')
        def base_method_attr(self, message):
            logger = log_360_logging.getLogger('test_lock_decorator.Base')
            logger.info(message)

    class Derived(Base):
        def __init__(self):
            super(Derived, self).__init__()
            self._derived_lock = threading.Lock()


# Generated at 2022-06-13 16:38:27.148845
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    lock = threading.Lock()
    value = []

    class ThreadingTests:

        @lock_decorator(lock=lock)
        def lock_test(self):
            value.append(1)

        @lock_decorator(attr='_attr_lock')
        def attr_test(self):
            value.append(1)

        def __init__(self):
            self._attr_lock = lock

    tt = ThreadingTests()

    threads = []
    for i in range(5):
        t = threading.Thread(target=tt.lock_test)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    assert len(value) == 5
    value.clear()

    threads = []

# Generated at 2022-06-13 16:38:30.298408
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    data = {}
    def rec(d):
        # Ensure that recursion doesn't deadlock
        with lock:
            rec(d)
            d['count'] = d.get('count',0) + 1
    @lock_decorator(lock=lock)
    def test(d):
        try:
            rec(d)
        except RuntimeError:
            pass

    threading.Thread(target=test, args=(data,)).start()
    test(data)
    with lock:
        count = data.get('count',0)
    assert count==2

# Generated at 2022-06-13 16:38:38.557213
# Unit test for function lock_decorator
def test_lock_decorator():
    class Cls(object):
        def __init__(self):
            self._lock = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method1(self):
            self._lock += 1

        @lock_decorator(attr='lock')
        def method2(self):
            self.lock += 1

    c = Cls()
    c.method1()
    assert c._lock == 1

    try:
        c.method2()
        assert False, "method2 should have failed with AttributeError"
    except AttributeError:
        pass
    else:
        assert False, "method2 should have failed with AttributeError"

# Generated at 2022-06-13 16:38:47.839080
# Unit test for function lock_decorator
def test_lock_decorator():
    class MyClass(object):

        _class_lock = None
        _instance_lock = None

        @classmethod
        @lock_decorator(attr='_class_lock')
        def class_method(cls):
            assert cls._class_lock is not None

        @lock_decorator(attr='_instance_lock')
        def instance_method(self):
            assert self._instance_lock is not None

        @classmethod
        def new(cls):
            obj = object.__new__(cls)
            obj._instance_lock = obj._class_lock = None
            return obj

    obj = MyClass()
    obj.class_method()
    obj.instance_method()

    obj = MyClass.new()
    obj.class_method()
    obj.instance_method()


# Generated at 2022-06-13 16:38:56.905645
# Unit test for function lock_decorator
def test_lock_decorator():
    # Unit test for lock_decorator which is used to wrap
    # a method that should be executed in a lock.
    import threading
    import collections
    import time

    # Set up a lock and the data structure we will be using
    lock = threading.Lock()
    counter = collections.Counter()

    # A simple function to increment a counter for us
    @lock_decorator(lock=lock)
    def incr_counter(counter, key):
        counter[key] += 1
        return counter[key]

    # Delay to allow counter to increment a bunch of times
    # while we're waiting to acquire the lock.
    delay = 0.1
    # The number of times we will try to acquire the lock
    reps = 20
    # Create a bunch of threads that will acquire the lock
    # and delay.

# Generated at 2022-06-13 16:39:01.476235
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    # Make sure this raises an error
    try:
        @lock_decorator()
        def test_method():
            pass
        raise Exception('Should have raised exception')
    except TypeError as e:
        if not 'AttributeError' in str(e):
            raise Exception('Did not raise AttributeError')

    l = threading.Lock()
    # Make sure this works
    @lock_decorator(lock=l)
    def test_method2():
        pass

    # Mock class with a mock lock
    class Mock(object):
        _lock = lock=threading.Lock()

    m = Mock()

    @lock_decorator()
    def test_locked_method(self):
        assert self._lock._is_owned()

    test_locked_method(m)



# Generated at 2022-06-13 16:39:05.478962
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    class Test(object):
        def __init__(self):
            self._locked_called = False
            self._unlocked_called = False
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def locked(self):
            assert not self._locked_called
            assert not self._unlocked_called
            assert self._callback_lock.locked()
            self._locked_called = True

        @lock_decorator(lock=threading.Lock())
        def unlocked(self):
            assert self._locked_called
            assert not self._unlocked_called
            assert not self.unlocked_lock.locked()
            self._unlocked_called = True


# Generated at 2022-06-13 16:39:15.493962
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep
    from tests.lib.module_common import AnsibleModule

    # Use a shared lock to ensure serial execution of
    # decorated methods, and a shared counter to ensure
    # that the methods are indeed executed serially
    lock = threading.RLock()
    counter = 0

    class Test(object):
        def __init__(self):
            self._lock = lock

        @lock_decorator(attr='_lock')
        def method_without_args(self):
            global counter
            counter += 1
            sleep(0.2)
            assert counter == 1

        @lock_decorator()
        def method_with_lock_specified(self):
            global counter
            counter += 1
            sleep(0.2)
            assert counter == 2


# Generated at 2022-06-13 16:39:20.983698
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    @lock_decorator(lock=lock)
    def foo():
        return True
    @lock_decorator(attr='_lock')
    def foo2():
        return True

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
    f = Foo()

    assert foo() is True
    assert foo2() is True
    assert foo2(f) is True

# Generated at 2022-06-13 16:39:29.393822
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Fake(object):
        _callback_lock = threading.Lock()
        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            return True

    test = Fake()
    assert test.send_callback() == True

    class Fake2(object):
        callback_lock = threading.Lock()
        @lock_decorator(lock=callback_lock)
        def some_method(self):
            return True

    test2 = Fake2()
    assert test2.some_method() == True

# vim: set expandtab shiftwidth=0 tabstop=4 softtabstop=4:

# Generated at 2022-06-13 16:39:37.330669
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    # Create dummy class with a attribute called ``_lock``
    class Dummy(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def dummy_method(self):
            self._lock.acquire()
            self._lock.release()

    # Create instance of dummy class
    dummy = Dummy()

    # Check ``_lock`` is actually a threading.Lock
    assert isinstance(dummy._lock, threading.Lock)

    # Check that the lock is locked before calling dummy method
    dummy._lock.acquire()
    assert dummy._lock.locked()
    # Call dummy method
    dummy.dummy_method()
    # Check that the lock is released after the dummy method completes
    assert not dummy._lock

# Generated at 2022-06-13 16:39:48.542223
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class TestClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._counter = 0

        @lock_decorator(attr='_lock')
        def locked_method(self):
            self._counter += 1

        @lock_decorator(lock=threading.Lock())
        def explicit_lock_method(self):
            self._counter += 1

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.test_obj = TestClass()

        def test_attr_lock(self):
            self.test_obj.locked_method()
            self.assertEqual(self.test_obj._counter, 1)

        def test_explicit_lock(self):
            self.test

# Generated at 2022-06-13 16:40:01.925720
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self.called = False
            self.calls = 0

        @lock_decorator(attr='lock')
        def test(self):
            self.called = True
            self.calls += 1

        def __repr__(self):
            return "called=%s, calls=%s" % (self.called, self.calls)

    def _run_test(method):
        method.test()
        method.test()

    test = Test()

    # Test with a lock attr
    test.lock = threading.Lock()
    _run_test(test)
    assert test.called is True
    assert test.calls == 1

    # Test with a lock defined inline
    test.called = False

# Generated at 2022-06-13 16:40:11.215676
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()
    lock_attr='woot_a_lock'

    class Test(object):
        def __init__(self):
            self.success = False
            self.woot_a_lock = threading.Lock()
            self.dude = 'The Dude'
            self.lebowski = 'Lebowski'

        @lock_decorator(attr=lock_attr)
        def wrapped(self, another_arg):
            assert hasattr(self, lock_attr), '{} not found in {}'.format(lock_attr, self)
            # Do something to verify the lock was acquired
            self.success = True
            return '{} {}'.format(self.dude, another_arg)

    # First test the decorator with ``attr``
    t = Test()


# Generated at 2022-06-13 16:40:21.083957
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    attr = None
    lock = None
    # Test with class
    class TestA0(object):
        def __init__(self):
            self.test_count = 0
            self.fake_lock = threading.Lock()
        @lock_decorator(attr='fake_lock')
        def test_lock_decorator(self):
            self.test_count += 1
    class TestB0(TestA0):
        @lock_decorator(attr='fake_lock')
        def test_lock_decorator(self):
            self.test_count += 1
    class TestC0(TestA0):
        @lock_decorator(attr='fake_lock')
        def test_lock_decorator(self):
            self.test_count += 1
    # Create instance

# Generated at 2022-06-13 16:40:30.088874
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    # Test with a lock object
    obj = threading.Lock()
    decorator = lock_decorator(lock=obj)

    # Test the decorator on a plain method
    @decorator
    def plain_method():
        time.sleep(1)

    # Test the decorator on a class method
    class Foo(object):
        @decorator
        def method(self):
            time.sleep(1)

        @classmethod
        @decorator
        def clsmethod(cls):
            time.sleep(1)

        @staticmethod
        @decorator
        def stmethod():
            time.sleep(1)

    threads = []

# Generated at 2022-06-13 16:40:40.721610
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestThreading(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.log = []

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, msg):
            self.log.append(msg)

    # Create a fresh instance
    test = TestThreading()

    # Append a message without the lock
    test.log.append('Hello from the main thread')

    # Execute the send callback method in two threads
    def callback_1():
        test.send_callback('Hello from callback 1')

    def callback_2():
        test.send_callback('Hello from callback 2')

    t1 = threading.Thread(target=callback_1)

# Generated at 2022-06-13 16:40:51.205147
# Unit test for function lock_decorator
def test_lock_decorator():

    class Sample(object):

        def __init__(self):
            self._lock = threading.Lock()
            self._value = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self._value += 1

        @lock_decorator(lock=threading.Lock())
        def decrement(self):
            self._value -= 1

    class NeverIncrementSample(object):

        def __init__(self):
            self._lock = threading.Lock()
            self._value = 0


# Generated at 2022-06-13 16:41:01.269023
# Unit test for function lock_decorator
def test_lock_decorator():
    failed = False
    try:
        import threading
    except ImportError:
        failed = True
    if not failed:
        class SomeClass(object):
            _lock = threading.Lock()

            @lock_decorator(attr='_lock')
            def some_method(self):
                return True

            @classmethod
            @lock_decorator(lock=threading.Lock())
            def some_static_method(cls):
                return True

        some_class = SomeClass()

        assert some_class.some_method()

        try:
            assert not SomeClass.some_static_method()
        except AssertionError:
            # for some reason the ``@lock_decorator`` does not work with
            # ``@classmethod``.  This should probably be fixed.
            failed = True
   

# Generated at 2022-06-13 16:41:06.722224
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread, Lock
    from time import sleep

    count = 0
    lock = Lock()

    @lock_decorator(lock=lock)
    def add():
        nonlocal count
        count += 1
        sleep(0.5)

    threads = []
    for i in range(5):
        threads.append(Thread(target=add))

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    assert count == 5

# Generated at 2022-06-13 16:41:16.694302
# Unit test for function lock_decorator
def test_lock_decorator():

    # Python2 doesn't have ``NonCallableMock``
    try:
        from unittest.mock import NonCallableMock
    except ImportError:
        from mock import NonCallableMock

    class Example(object):
        _lock = NonCallableMock()

        @lock_decorator(attr='_lock')
        def method(self, a, b, c=1, d=1, e=2):
            return a + b + c + d + e

    inst = Example()
    assert inst.method(1, 1, c=1, d=1, e=2) == 6
    inst._lock.assert_called_once_with()


# Generated at 2022-06-13 16:41:26.626114
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading
    start_times = []
    end_times = []

    class MyLock(object):
        '''
        A fake lock object, implementing only a context manager
        '''
        def __enter__(self):
            return

        def __exit__(self, *args, **kwargs):
            return

    @lock_decorator(lock=MyLock())
    def sleep_func(index):
        start_times.append(time.time())
        time.sleep(60)
        end_times.append(time.time())

    sleep_threads = [
        threading.Thread(target=sleep_func, args=(number,))
        for number in range(0, 10)
    ]

    for thread in sleep_threads:
        thread.start()


# Generated at 2022-06-13 16:41:43.750376
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class A(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.shared = 0
            self.shared_list = []

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, val):
            self.shared += val
            self.shared_list.append(val)

        @lock_decorator(lock=threading.Lock())
        def send_callback2(self, val):
            self.shared += val
            self.shared_list.append(val)

    a = A()
    threads = []
    for i in range(1, 100):
        threads.append(threading.Thread(target=a.send_callback, args=(i,)))

# Generated at 2022-06-13 16:41:56.100055
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading
    class AnsibleVaultProxy(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def _change_password(self, password, old_password=None):
            return 'foo'

    avp = AnsibleVaultProxy()
    with mock.patch.object(avp, '_lock') as lock:
        assert avp._change_password('foo') == 'foo'
        lock.assert_called_once_with()

    class SomeObj(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(lock=self._lock)
        def some_method(self, foo):
            return 'foo'


# Generated at 2022-06-13 16:41:57.174605
# Unit test for function lock_decorator

# Generated at 2022-06-13 16:42:02.050547
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import random
    import string
    import time

    class SomeClass():
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.callback_called = 0

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, data):
            self.callback_called += 1
            time.sleep(random.random()/10)

    def some_method(data):
        test_lock_decorator.callback_called += 1
        time.sleep(random.random()/10)

    # Create a lock
    test_lock = threading.Lock()
    # create a class instance
    obj = SomeClass()
    # wrap the function
    wrapped = lock_decorator(lock=test_lock)(some_method)
    #

# Generated at 2022-06-13 16:42:10.249972
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class A:
        lock = lock_decorator('lock')
        @lock
        def method(self):
            from time import sleep
            sleep(1)
    a = A()
    a.lock = threading.Lock()
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as e:
        futures = [e.submit(a.method) for _ in range(2)]
        for r in concurrent.futures.as_completed(futures):
            assert r.result() is not None
    class B:
        lock = lock_decorator(lock="foo")
        @lock
        def method(self):
            pass
    b = B()

# Generated at 2022-06-13 16:42:15.929139
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.bar = None

        @lock_decorator(attr='lock')
        def set_bar(self, val):
            self.bar = val

    foo = Foo()
    foo.set_bar('bar')
    assert foo.bar == 'bar'
    foo.set_bar('baz')
    assert foo.bar == 'baz'


# Generated at 2022-06-13 16:42:24.528495
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from six.moves import queue
    global q
    q = queue.Queue()
    test_lock = threading.Lock()

    # The global q is a threadsafe queue that is used to check
    # the order in which the threads are executed
    global q

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def _foo(self):
            q.put(1)

        @lock_decorator(lock=test_lock)
        def _bar(self):
            q.put(2)

    def test_threaded():
        instance = Test()
        # Make sure we execute _foo and _bar on different threads
        # and that they start at the same time
        t_

# Generated at 2022-06-13 16:42:33.969718
# Unit test for function lock_decorator
def test_lock_decorator():

    from threading import Lock

    class TestLockDecClass(object):
        _lock = Lock()

        @lock_decorator()
        def no_kwargs(self):
            pass

        @lock_decorator(attr='_lock')
        def attr_kwarg(self):
            pass

        @lock_decorator(lock=Lock())
        def lock_kwarg(self):
            pass

    assert TestLockDecClass.__dict__['no_kwargs']._lock_attr == 'missing_lock_attr'
    assert TestLockDecClass.__dict__['attr_kwarg']._lock_attr == '_lock'
    assert TestLockDecClass.__dict__['lock_kwarg']._lock_attr == 'missing_lock_attr'

# Generated at 2022-06-13 16:42:45.108628
# Unit test for function lock_decorator
def test_lock_decorator():
    # just a hacky check to ensure turning on strict checking will
    # give us the errors we are looking for
    import pylint.utils
    pylint.utils.PY3 = False
    import pylint.lint
    linter = pylint.lint.Run(['--persistent=no', '--rcfile=.pylintrc', '--strict', 'lib/ansible/module_utils/basic/network/l3/lacp.py'], exit=False)
    pylint_stdout = linter.linter.reporter.out.getvalue()
    assert 'Undefined variable \'lock\'' in pylint_stdout
    assert 'Undefined variable \'missing_lock_attr\'' in pylint_stdout
    assert 'Undefined variable \'attr\'' in pylint_

# Generated at 2022-06-13 16:42:54.017819
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.RLock()
    class Test:
        def __init__(self):
            self._lock = lock
            self._value = 0
        def __increment(self, delta):
            self._value += delta
            return self._value
        @lock_decorator(attr='_lock')
        def increment(self, delta):
            return self.__increment(delta)
    t = Test()
    assert t.increment(1) == 1
    assert t.increment(2) == 3
    t2 = Test()
    assert t2.increment(3) == 3
    assert t2.increment(4) == 7
    t3 = Test()

# Generated at 2022-06-13 16:43:17.100327
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Dummy(object):
        _dummy_lock = threading.Lock()
        @lock_decorator(attr='_dummy_lock')
        def do_something(self):
            pass

        @lock_decorator(lock=threading.Lock())
        def do_something_else(self):
            pass
    dummy = Dummy()
    dummy.do_something()
    dummy.do_something_else()

# Generated at 2022-06-13 16:43:24.468097
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._count = 0

        @lock_decorator(attr='_lock')
        def count(self):
            self._count += 1
            return self._count

        def __iadd__(self, other):
            self.count()
            return self

    foo = Foo()
    assert foo.count() == 1
    assert foo.count() == 2
    assert foo + 1 == foo
    assert foo.count() == 3

    class Bar(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._count = 0

        @lock_decorator(lock=self._lock)
        def count(self):
            self._count += 1


# Generated at 2022-06-13 16:43:27.672825
# Unit test for function lock_decorator
def test_lock_decorator():
    # Basic test, we don't necessarily have a lock object, so we just
    # verify that the decorator runs.
    @lock_decorator()
    def _test1():
        return True

    assert _test1() is True

# Generated at 2022-06-13 16:43:34.177154
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    class Target(object):
        _lock = threading.Lock()
        @lock_decorator('_lock')
        def increment(self):
            time.sleep(1)
            self.count+=1
        def __init__(self):
            self.count = 0

    result = [None]
    def f():
        t = Target()
        t.increment()
        result[0] = t.count
        t.increment()
        result[0] += t.count

    threads = []
    for _ in xrange(100):
        t = threading.Thread(target=f)
        t.daemon = True
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    assert result[0] == 200

# Generated at 2022-06-13 16:43:44.405672
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    class TestClass(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.lock2 = threading.Lock()
            self.some_attr = 'foo'
            self.counter = 0

        @lock_decorator(attr='lock')
        def attr_method(self, num):
            self.counter += num

        @lock_decorator(lock=threading.Lock())
        def lock_method(self, num):
            self.counter += num

        @lock_decorator(attr='lock2')
        def attr_method2(self, num):
            self.counter += num


# Generated at 2022-06-13 16:43:52.953408
# Unit test for function lock_decorator
def test_lock_decorator():
    class SomeClass(object):
        def __init__(self):
            self._lock = False

        def __eq__(self, other):
            return self.__dict__ == other.__dict__

        @lock_decorator(attr='_lock')
        def test_attr(self):
            self._lock = True

        @lock_decorator(lock=True)
        def test_lock(self):
            self._lock = True

        @lock_decorator()
        def test_args(self, foo):
            return foo

    obj = SomeClass()
    obj.test_attr()
    assert obj == SomeClass.test_attr(obj)
    assert obj == SomeClass().test_attr()
    assert obj._lock is True

    obj = SomeClass()

# Generated at 2022-06-13 16:43:58.894476
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    calls = []
    # Example without pre-existing lock
    @lock_decorator()
    def with_no_lock(x, y):
        calls.append('with_no_lock')
        return x + y

    # Example with pre-existing lock
    class test_obj(object):
        _lock = None
        @lock_decorator(attr='_lock')
        def with_attr_lock(self, x, y):
            calls.append('with_attr_lock')
            return x + y

        @lock_decorator(lock=lock)
        def with_lock(self, x, y):
            calls.append('with_lock')
            return x + y

    obj = test_obj()

# Generated at 2022-06-13 16:44:10.744535
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    counter = 0
    assert counter == 0

    @lock_decorator(lock=lock)
    def increase_counter():
        global counter
        counter += 1
        return counter

    @lock_decorator(lock=lock)
    def decrease_counter():
        global counter
        counter -= 1
        return counter

    increase_counter()
    increase_counter()
    decrease_counter()
    increase_counter()

    assert counter == 2
    # Use the lock_decorator method to set instance attribute,
    # defining class lock.
    class cls:
        def __init__(self):
            self._cls_lock = threading.Lock()


# Generated at 2022-06-13 16:44:19.541554
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo:
        def __init__(self):
            self.lock = lock_decorator('_lock')
            self._lock = None
        def bar(self):
            return self._lock
        @lock_decorator(attr='_lock')
        def baz(self):
            return self._lock
        @lock_decorator(lock=lambda: 0)
        def qux(self):
            return self._lock
        @lock_decorator(lock=lambda: 'abc')
        @lock_decorator(lock=lambda: 'def')
        def quux(self):
            return self._lock

# Generated at 2022-06-13 16:44:28.215978
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Callback:
        def __init__(self):
            self.callback_done = False
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, time_to_sleep):
            time.sleep(time_to_sleep)
            self.callback_done = True

    callback = Callback()
    callback.send_callback(time_to_sleep=3)
    assert callback.callback_done

# Generated at 2022-06-13 16:45:07.892887
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    from threading import Lock

    class TestClass(object):
        def __init__(self):
            self._callback_lock = Lock()
            self._callback_lock.acquire = mock.MagicMock(return_value=None)
            self._callback_lock.release = mock.MagicMock(return_value=None)

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, *args, **kwargs):
            return True

        @lock_decorator(lock=Lock())
        def send_callback_explicit(self, *args, **kwargs):
            return True

    t = TestClass()
    assert t.send_callback()
    assert t._callback_lock.acquire.called
    assert t._callback_lock.release.called
    assert t

# Generated at 2022-06-13 16:45:15.183856
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Unit test for function lock_decorator'''
    import threading
    import time

    class Plugin:
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, name, value=None):
            '''Simulate a callback'''
            time.sleep(0.001)

    @lock_decorator(lock=threading.Lock())
    def some_method():
        pass

    plugin = Plugin()
    for i in range(10):
        threading.Thread(target=plugin.send_callback, args=('some_callback',)).start()

    for i in range(10):
        threading.Thread(target=some_method).start()



# Generated at 2022-06-13 16:45:24.534930
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestClass(object):
        def __init__(self):
            self.shared_state = 0
            self.attr_lock = threading.Lock()

        @lock_decorator(attr='attr_lock')
        def method_using_lock(self):
            self.shared_state += 1

        @lock_decorator(lock=threading.Lock())
        def method_using_lock2(self):
            self.shared_state += 1

    @lock_decorator(lock=threading.Lock())
    def function_using_lock():
        global shared_state
        shared_state += 1

    shared_state = 0
    threads = []
    lock = threading.Lock()
    test_class_obj = TestClass()

# Generated at 2022-06-13 16:45:31.533155
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Fake:
        def __init__(self):
            self.result = 1

        @lock_decorator(attr='lock')
        def method(self):
            self.result *= 2

        @lock_decorator(lock=threading.Lock())
        def method2(self):
            self.result *= 4

    f = Fake()
    f.lock = threading.Lock()
    assert f.result == 1

    f.method()
    assert f.result == 2

    f.method2()
    assert f.result == 8

# Generated at 2022-06-13 16:45:39.550563
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    l = threading.Lock()
    class A(object):
        def __init__(self, lock=l):
            self._lock = lock

        @lock_decorator(attr='_lock')
        def foo(self, delay=0.1):
            import time
            time.sleep(delay)

    a = A()
    a.foo()
    t = threading.Thread(target=a.foo, args=(0.1,))
    t.start()
    import time
    time.sleep(0.01)
    assert t.is_alive()
    t = threading.Thread(target=a.foo, args=(0.2,))
    t.start()
    time.sleep(0.1)
    assert not t.is_alive()
    t.join()

