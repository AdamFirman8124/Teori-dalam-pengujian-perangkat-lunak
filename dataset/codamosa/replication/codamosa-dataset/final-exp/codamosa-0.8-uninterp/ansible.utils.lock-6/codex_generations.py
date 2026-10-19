

# Generated at 2022-06-13 16:36:03.183171
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class MyClass(object):
        def __init__(self):
            self._lock_attr = threading.Lock()

        @lock_decorator(attr='_lock_attr')
        def lock_attr_func(self, value):
            return value

        @lock_decorator(lock=threading.Lock())
        def lock_as_arg_func(self, value):
            return value

    inst = MyClass()
    # Test using lock as instance attribute
    assert inst.lock_attr_func(42) == 42
    assert inst.lock_attr_func(None) is None
    # Test using lock as explicit argument
    assert inst.lock_as_arg_func(42) == 42
    assert inst.lock_as_arg_func(None) is None

# Generated at 2022-06-13 16:36:13.445057
# Unit test for function lock_decorator
def test_lock_decorator():
    import types
    from threading import Lock, Thread
    from time import sleep

    class LockObject(object):
        def __init__(self, lock_attribute):
            self.counter = 0
            self.lock_attribute = lock_attribute
            setattr(self, lock_attribute, Lock())

        @lock_decorator(attr=None)
        def increment_counter(self, lock):
            # Increments self.counter by 1
            self.counter += 1

        @lock_decorator(lock=None)
        def increment_counter_from_attribute(self):
            # Increments self.counter by 1
            self.counter += 1


# Generated at 2022-06-13 16:36:23.602808
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class MyThread(threading.Thread):
        def __init__(self, *args, **kwargs):
            self.count = 0
            self._callback_lock = threading.Lock()
            super(MyThread, self).__init__(*args, **kwargs)

        @lock_decorator(attr='_callback_lock')
        def do_something(self):
            self.count = 1

    t = MyThread()
    t.start()
    t.do_something()
    assert t.count == 1
    t.join()

    # Test using explicit lock
    class MyThread(threading.Thread):
        def __init__(self, *args, **kwargs):
            self.count = 0
            super(MyThread, self).__init__(*args, **kwargs)

       

# Generated at 2022-06-13 16:36:33.209713
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    lock = threading.Lock()
    l = []
    @lock_decorator(lock=lock)
    def foo():
        time.sleep(.1)
        l.append(1)
    t1 = threading.Thread(target=foo)
    t2 = threading.Thread(target=foo)
    t3 = threading.Thread(target=foo)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    assert len(l) == 1

    lock = threading.Lock()
    l = []
    @lock_decorator(lock=lock)
    def bar(a, b, c=2, d=3):
        l.append

# Generated at 2022-06-13 16:36:44.427392
# Unit test for function lock_decorator
def test_lock_decorator():
    from ansible.module_utils._text import to_text

    class Test(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='lock')
        def add(self):
            self.value += 1

        @lock_decorator(lock=self.lock)
        def subtract(self):
            self.value -= 1

    import threading
    t = threading.Thread(target=add, args=(t,))
    t.daemon = True
    t.start()
    t.join()
    assert to_text(t.value) == '1'

    t = threading.Thread(target=subtract, args=(t,))
    t.daemon = True
    t.start()
    t

# Generated at 2022-06-13 16:36:54.327438
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread
    import sys

    class TestObject(object):
        '''Simple test class to test the lock_decorator'''
        def __init__(self):
            self._blah = 0
            self._foo = 2
            self._lock = Lock()

        @lock_decorator(attr='_lock')
        def blah(self):  # pylint: disable=no-self-use
            '''Decorated method using a lock'''
            self._blah += 1
            print(self._blah)
            return self._blah

        @lock_decorator()
        def foo(self, bar=None):  # pylint: disable=no-self-use
            '''Decorated method using the default lock'''
            if bar is not None:
                return bar

# Generated at 2022-06-13 16:37:02.416249
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class LockTest(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.callback_called = 0

        @lock_decorator('_callback_lock')
        def send_callback(self):
            self.callback_called += 1

    lt = LockTest()
    lt.send_callback()
    assert lt.callback_called == 1
    lt.send_callback()
    assert lt.callback_called == 2

# Generated at 2022-06-13 16:37:09.334267
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread, Lock

    class Test(object):
        def __init__(self, *args, **kwargs):
            self._my_lock = Lock()
            self._counter = 0

        @lock_decorator(attr='_my_lock')
        def increment(self):
            '''This is a docstring'''
            self._counter += 1

        @property
        def counter(self):
            return self._counter

    class UpdateThread(Thread):
        def run(self):
            for x in range(10):
                obj.increment()

    obj = Test()
    threads = [UpdateThread() for x in range(10)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    # NOTE: The counter may be less than 100 because the lock

# Generated at 2022-06-13 16:37:17.712898
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class MockObject(object):
        def __init__(self):
            self.callback_called = False

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, value):
            if self.callback_called:
                raise Exception('Callback was called multiple times')
            self.callback_called = value

        @lock_decorator(lock=threading.Lock())
        def send_callback_lock(self, value):
            if self.callback_called:
                raise Exception('Callback was called multiple times')
            self.callback_called = value

    # Test using lock_decorator with attr
    mo = MockObject()
    mo.send_callback(True)
    assert mo.callback_called is True

    # Test using lock_decorator with lock
    mo

# Generated at 2022-06-13 16:37:24.464014
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo:
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator('_callback_lock')
        def send_callback(self):
            self.callback_lock.acquire()
            print("I have the lock!")

        @lock_decorator(lock=threading.Lock())
        def some_method(self):
            print("I have the lock!")

    f = Foo()
    f.send_callback()
    f.some_method()

# Generated at 2022-06-13 16:37:35.430766
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Callback(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            return 'done'

    c = Callback()
    assert c.send_callback() == 'done'

    @lock_decorator(lock=threading.Lock())
    def some_func():
        return 'done'

    assert some_func() == 'done'


if __name__ == '__main__':
    test_lock_decorator()

# Generated at 2022-06-13 16:37:44.250336
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class LockDecoratorTestCase(unittest.TestCase):
        def setUp(self):
            self.lock = lock = threading.Lock()
            self.value = 1

        @lock_decorator(attr='lock')
        def lock_method(self, value):
            self.value += value

        @lock_decorator(lock=threading.Lock())
        def other_method(self, value):
            self.value += value

    class TestThread(threading.Thread):
        def __init__(self, lock_decorator, value):
            super(TestThread, self).__init__()
            self.lock_decorator = lock_decorator
            self.value = value
            self.daemon = True


# Generated at 2022-06-13 16:37:53.612507
# Unit test for function lock_decorator
def test_lock_decorator():
    import os
    import threading
    import time
    import Queue
    import tempfile
    # Create a lock and the reference to the lock that we'll pass
    # to the test function
    locking = threading.Lock()
    # Create the test function that we'll wrap
    def write_to_file(path, done, lock):
        # Ensure that the lock is present and is a lock
        assert callable(getattr(lock, '__enter__', None))
        assert callable(getattr(lock, '__exit__', None))
        # If the path exists, use it, otherwise create a tmpfile
        if path:
            f = open(path, 'a+')
        else:
            f = tempfile.NamedTemporaryFile(delete=False)
            path = f.name
        # Loop until the done queue is

# Generated at 2022-06-13 16:37:58.716382
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class MyClass(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def my_method(self):
            pass

    @lock_decorator(lock=threading.Lock())
    def my_other_method():
        pass

# Generated at 2022-06-13 16:38:06.827535
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._time = None
            self._count = 0

        @lock_decorator(attr='_lock')
        def foo(self):
            time.sleep(1)
            self._time = time.time()
            self._count += 1

        @lock_decorator(lock=threading.Lock())
        def bar(self):
            time.sleep(1)
            self._time = time.time()
            self._count += 1

        @lock_decorator(lock=threading.Lock())
        def baz(self):
            time.sleep(1)
            self._time = time.time()
            self._count += 1

    t = Test()


# Generated at 2022-06-13 16:38:12.684335
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = None

    class Spam:
        def __init__(self):
            self.attribute = 0
            self._callback_lock = threading.Lock()

    def callback_lock(self):
        with self._callback_lock:
            self.attribute += 1

    def lock(self):
        with lock:
            self.attribute += 1

    spam = Spam()
    lock_decorator(lock=lock)(Spam.lock)(spam)
    lock_decorator(attr='_callback_lock')(Spam.callback_lock)(spam)

    assert spam.attribute == 2

# Generated at 2022-06-13 16:38:20.046678
# Unit test for function lock_decorator
def test_lock_decorator():
    ok_ = False

    class Test(object):
        def __init__(self):
            self._lock = False

        @lock_decorator(attr='_lock')
        def method1(self):
            global ok_
            ok_ = True

        @lock_decorator(lock=lock)
        def method2(self):
            global ok_
            ok_ = True

        @lock_decorator(attr='_lock')
        @classmethod
        def class_method1(cls):
            global ok_
            ok_ = True

        @lock_decorator(lock=lock)
        @classmethod
        def class_method2(cls):
            global ok_
            ok_ = True

    my_obj = Test()
    my_obj.method1()
    assert ok_ is True


# Generated at 2022-06-13 16:38:30.910913
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class LockTest(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.counter = 0
            self.checked = False

        @lock_decorator(attr='_lock')
        def locked(self, other):
            if other.counter != 2:
                raise Exception('counter should be 2 and was %s' % other.counter)
            self.checked = True

    other = LockTest()
    l = LockTest()

    def target():
        l.locked(other)

    t = threading.Thread(target=target)
    t.start()
    for i in range(3):
        other.counter += 1
    t.join()

    assert l.checked, "the method was not properly wrapped"

    l = LockTest()


# Generated at 2022-06-13 16:38:36.852756
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Tester(object):
        def __init__(self):
            self._test_lock = threading.Lock()
            self._test_var = 42

        @lock_decorator('_test_lock')
        def test_method(self):
            self._test_var -= 1
            return self._test_var

    t = Tester()
    t.test_method()
    assert t._test_var == 41

# Generated at 2022-06-13 16:38:47.209252
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    import threading
    lock_attr_name = '_callback_lock'
    lock_name = 'lock'

    class Test(object):
        def __init__(self):
            self.n = 0
            self.m = 0
            setattr(self, lock_attr_name, threading.Lock())
            setattr(self, lock_name, threading.Lock())

        @lock_decorator(attr=lock_attr_name)
        def incr_n(self):
            self.n += 1
            # set the thread's name in a thread-safe manner
            sys._current_frames.items()[0][1].f_locals['self'].name = 'incr_n'


# Generated at 2022-06-13 16:39:02.788385
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    result = []

    class Test(object):
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def decorator_lock(self, item):
            result.append(item)

        @lock_decorator(lock=self.lock)
        def decorator_instance_lock(self, item):
            result.append(item)

        def normal(self, item):
            result.append(item)

    t = Test()

    def test_thread(item):
        for i in range(0, 1000):
            t.decorator_lock(item)
            t.decorator_instance_lock(item)
            t.normal(item)


# Generated at 2022-06-13 16:39:14.169706
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep

    class Foo(object):
        count = 0

        def __init__(self, attr='_lock', lock=None):
            if lock is not None:
                self.attr = '_lock'
                setattr(self, self.attr, lock)
            else:
                self.attr = attr

        @lock_decorator(attr='attr')
        def increment(self):
            self.count += 1

        def test(self):
            self.increment()

    def foo(f):
        f.increment()

    l = threading.Lock()
    f = Foo()
    t = threading.Thread(target=foo, args=(f,))
    t.start()
    sleep(0.25)
    assert f.count == 0

    f = Foo

# Generated at 2022-06-13 16:39:21.747952
# Unit test for function lock_decorator
def test_lock_decorator():
    class A:
        def __init__(self):
            self.mesg = []
            self.lock = False

        @lock_decorator(attr='mesg')
        def add_to_mesg(self, mesg):
            self.mesg.append(mesg)

        @lock_decorator(lock=True)
        def set_lock(self, value=True):
            self.lock = value

    a = A()
    a.add_to_mesg(10)
    assert a.mesg == [10]
    a.set_lock()
    assert a.lock


if __name__ == '__main__':
    test_lock_decorator()

# Generated at 2022-06-13 16:39:31.933029
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    from threading import Thread

    class Base(object):
        def __init__(self):
            self.attr = 'attr'
            self.lock = threading.Lock()

    class Derived_1(Base):
        @lock_decorator(attr='lock')
        def derived_as_lock(self):
            self.attr = self.attr + 1
            return self.attr

    class Derived_2(Base):
        @lock_decorator(lock=threading.Lock())
        def derived_as_lock(self):
            self.attr = self.attr + 1
            return self.attr


# Generated at 2022-06-13 16:39:38.592547
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
        lock = threading.Lock()
        def some_method(lock=None):
            return lock is not None
        assert lock_decorator(lock=lock)(some_method)()
        assert lock_decorator(attr='_lock')(some_method)(lock=lock)
    except (ImportError, NameError):
        pass

# Generated at 2022-06-13 16:39:46.331574
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    @lock_decorator(attr='_lock')
    def method_threading(self):
        for i in range(10):
            print('method_threading: {}'.format(i))
            assert self._lock.acquire(blocking=False)

    class TestClass(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(lock=self._lock)
        def method_threading2(self):
            for i in range(10):
                print('method_threading2: {}'.format(i))
                assert self._lock.acquire(blocking=False)

    c = TestClass()
    assert c.method_threading() == None
    assert c.method_threading2() == None



# Generated at 2022-06-13 16:39:57.204802
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    # A simple class that has a lock attribute
    class LockObject:
        def __init__(self):
            self._lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def lock_method(self):
            return 2
        @lock_decorator(lock=self._lock)
        def lock_method2(self):
            return 3

    # A class that doesn't have a lock attribute
    class NoLockObject:
        @lock_decorator(lock=threading.Lock())
        def lock_method(self):
            return 2
        @lock_decorator(attr='lock')
        def lock_method2(self):
            return 3

    def test_method(obj):
        # Make sure the lock works as expected
        assert obj.lock_method

# Generated at 2022-06-13 16:40:05.673543
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import random
    import time

    # Test that the lock decorator works with a pre-defined
    # lock attribute on an instance.
    class TestLockAttr(object):
        def __init__(self):
            self._lock_attr = threading.Lock()
            self.data = 0

        @lock_decorator()
        def lock_attr_test(self):
            # Without a lock, this should sometimes raise an
            # exception when ``data`` isn't properly incremented
            # to ``1``.
            self.data += 1
            time.sleep(random.random())
            assert self.data == 1, 'self.data != 1'


    # Test that the lock decorator works with a pre-defined
    # lock attribute on a class.

# Generated at 2022-06-13 16:40:17.402539
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest  # noqa
    import threading  # noqa

    class _LockTests(unittest.TestCase):
        def setUp(self):
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def test_lock_decorator_as_method(self):
            self.assertTrue(self.lock.acquire(blocking=False))
            self.assertFalse(self.lock.acquire(blocking=False))

        @lock_decorator(lock=self.lock)
        def test_lock_decorator_with_lock(self):
            self.assertTrue(self.lock.acquire(blocking=False))
            self.assertFalse(self.lock.acquire(blocking=False))

    test = _LockTests()

# Generated at 2022-06-13 16:40:27.960092
# Unit test for function lock_decorator
def test_lock_decorator():
    from mock import Mock, sentinel
    from threading import Lock

    # mock class
    class Foo(object):
        def __init__(self):
            self.called = []
            self._callback_lock = Lock()

        @lock_decorator(attr='_callback_lock')
        def foo(self, a, b=None, **kwargs):
            self.called.append((a, b, kwargs))
            return sentinel.result

    foo = Foo()

    assert foo.called == []
    assert foo.foo(sentinel.arg1, b=sentinel.arg2, c=sentinel.arg3) == sentinel.result
    assert foo.called == [(sentinel.arg1, sentinel.arg2, {'c': sentinel.arg3})]

    # mock class

# Generated at 2022-06-13 16:40:43.459054
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class C:
        def __init__(self):
            self.counter = 0
            self.lock = threading.RLock()

    c = C()

    @lock_decorator(attr='lock')
    def worker(c):
        for i in range(100):
            c.counter += 1

    for i in range(100):
        t = threading.Thread(target=worker, args=(c, ))
        t.start()
        t.join()

    assert c.counter == 10000

    @lock_decorator(lock=c.lock)
    def worker2(c):
        for i in range(100):
            c.counter += 1

    for i in range(100):
        t = threading.Thread(target=worker2, args=(c, ))
        t.start()

# Generated at 2022-06-13 16:40:48.464379
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class A(object):
        counter = 0

        @lock_decorator(attr='_lock')
        def add(self):
            self.counter += 1

        def add_no_lock(self):
            self.counter += 1

        def setup(self):
            self._lock = threading.Lock()

    a = A()
    a.setup()

    def thread():
        for i in range(5):
            a.add()

    threads = [threading.Thread(target=thread) for i in range(2)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert a.counter == 10

    # Make sure the lock worked
    a = A()

# Generated at 2022-06-13 16:40:55.702986
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test(object):
        # In real life, add _lock to class, class instance will not have lock
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_function(self, result):
            time.sleep(0.1)
            result.append(True)

    result = []
    TEST_THREADS = 5
    threads = []
    for _ in range(TEST_THREADS):
        t = threading.Thread(target=Test().test_function, args=(result,))
        t.daemon = True
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

    assert len(result) == TEST_THREADS

# Generated at 2022-06-13 16:41:04.048830
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            # Do not call superclass __init__

        @lock_decorator(attr='_lock')
        def locked_method(self):
            return 'foo'

        @lock_decorator(lock=threading.Lock())
        def more_locked_method(self):
            return 'bar'

        def check_locked_method(self):
            with mock.patch('ansible.module_utils.common._ansible_module.AnsibleModule._lock') as _lock:
                self.locked_method()
            _lock.acquire.assert_called_once_with()


# Generated at 2022-06-13 16:41:08.261945
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._value = 0

        @lock_decorator(attr='_lock')
        def add(self, value):
            self._value += value

        @lock_decorator(lock=self._lock)
        def subtract(self, value):
            self._value -= value

    f = Foo()
    assert f._value == 0
    f.add(10)
    f.subtract(5)
    assert f._value == 5

# Generated at 2022-06-13 16:41:17.593827
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class LockWrapper:
        _lock = threading.Lock()
        _attr_lock = threading.Lock()

        @lock_decorator(attr='_attr_lock')
        def attr_lock(self, msg):
            print('{0} - attr_lock - start'.format(msg))
            time.sleep(1)
            print('{0} - attr_lock - end'.format(msg))

        @lock_decorator(lock=_lock)
        def lock(self, msg):
            print('{0} - lock - start'.format(msg))
            time.sleep(1)
            print('{0} - lock - end'.format(msg))

    wrapper = LockWrapper()
    for l in range(4):
        t = threading.Thread

# Generated at 2022-06-13 16:41:24.798651
# Unit test for function lock_decorator
def test_lock_decorator():
    class Test(object):
        __test__ = False  # This is not a test

        def __init__(self):
            self._lock = 0

        @lock_decorator(attr='_lock')
        def send_callback(self):
            # This method should be locked
            self._lock += 1
            return self._lock

        @lock_decorator()
        def some_method(self):
            # This method isn't locked
            self._lock += 1
            return self._lock

        @lock_decorator(lock=1)
        def some_other_method(self):
            # This method isn't locked
            self._lock += 1
            return self._lock

    test = Test()

    assert test.send_callback() == 1
    assert test.some_method() == 2
    assert test.some_

# Generated at 2022-06-13 16:41:33.026453
# Unit test for function lock_decorator
def test_lock_decorator():
    import os
    import random
    import sys
    import threading
    import time

    def thread_func(lock_val, test_val):
        time.sleep(random.random())
        with lock_val:
            test_val += 1

    class TestClass(object):
        def __init__(self, _lock):
            self._lock = _lock
            self.test_val = 0

        @lock_decorator(lock=_lock)
        def test_method(self):
            self.test_val += 1

        @lock_decorator(attr='_lock')
        def test_attr_method(self):
            self.test_val += 1

    _lock = threading.Lock()
    test = TestClass(_lock)

    # Create threads and start them
    threads = []

# Generated at 2022-06-13 16:41:41.012261
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    def thread_func(lock):
        with lock:
            time.sleep(1)
            print("Lock acquired")

    def main():
        lock = threading.Lock()
        t = threading.Thread(target=thread_func, args=(lock,))
        t.start()
        time.sleep(0.5)
        print("Lock acquired")
        with lock:
            print("Lock acquired")
        t.join()

    # Should print:
    # Lock acquired
    # Lock not acquired
    # Lock acquired
    main()
    time.sleep(0.5)

    def thread_func(lock):
        with lock:
            time.sleep(1)
            print("Lock acquired")

    def main():
        lock = threading.Lock()
        t = threading.Thread

# Generated at 2022-06-13 16:41:47.434463
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test(object):
        def __init__(self):
            self.lock = threading.Lock()
            self._count = 0
            self._lock_count = 0

        @lock_decorator(attr='lock')
        def func_count(self):
            time.sleep(.5)
            self._count += 1

        @lock_decorator(lock=threading.Lock())
        def lock_count(self):
            time.sleep(.5)
            self._lock_count += 1

    obj = Test()
    threads = []
    threads.append(threading.Thread(target=obj.func_count))
    threads.append(threading.Thread(target=obj.func_count))

# Generated at 2022-06-13 16:42:15.931386
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Test the lock_decorator function'''
    import threading
    class MyTest(object):
        def __init__(self):
            self.cnt = 0
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_with_lock(self, val):
            self.cnt += val

    mt1 = MyTest()
    mt2 = MyTest()
    assert mt1.cnt == 0
    assert mt2.cnt == 0

    for i in range(10):
        mt1.test_with_lock(i)
        mt2.test_with_lock(i * 2)

    assert mt1.cnt == sum(range(10))
    assert mt2.cnt == sum(range(20)) * 2
    assert mt1

# Generated at 2022-06-13 16:42:24.529504
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock
    from time import time

    class TestClass(object):
        def __init__(self, test_lock=None):
            if not test_lock:
                test_lock = Lock()
            self._test_lock = test_lock

        @lock_decorator(attr='_test_lock')
        def decorated_method(self, delay):
            time.sleep(delay)

    class TestBadClass(object):
        @lock_decorator(attr='_test_lock')
        def decorated_method(self, delay):
            time.sleep(delay)

    tc = TestClass()
    tbc = TestBadClass()

    assert hasattr(tc, '_test_lock')
    assert not hasattr(tbc, '_test_lock')


# Generated at 2022-06-13 16:42:34.288111
# Unit test for function lock_decorator
def test_lock_decorator():
    import munch
    import threading
    import time

    _lock = threading.Lock()

    class Test(object):
        @lock_decorator(attr='_lock')
        def _do_stuff(self):
            if not hasattr(self, 'counter'):
                self.counter = 0
            self.counter += 1
            time.sleep(0.1)

        def do_stuff(self):
            with _lock:
                self._do_stuff()

    t = Test()

    def go():
        for _ in range(100):
            t._do_stuff()

    threads = [threading.Thread(target=go) for _ in range(10)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    assert t.counter == 100


# Generated at 2022-06-13 16:42:45.258330
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from nose.tools import assert_equals

    LOCK = threading.Lock()
    FUNC = lambda *args, **kwargs: args[0] + kwargs.get('b', 0)

    class TestLock:
        def __init__(self):
            self.tlock = threading.Lock()

        def __call__(self, *args, **kwargs):
            with self.tlock:
                return args[0] + kwargs.get('b', 0)

    @lock_decorator(attr='tlock')
    def test_lock_decorator_instance_attr(a, b=0):
        return FUNC(a, b=b)


# Generated at 2022-06-13 16:42:54.177010
# Unit test for function lock_decorator
def test_lock_decorator():

    import sys
    if sys.version_info < (3, 0):
        import imp
        imp.reload(sys)
        sys.setdefaultencoding('utf-8')

    import threading
    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.my_dict = dict()

        @lock_decorator(attr='_lock')
        def bar(self, item):
            # This will fail without the lock
            if item in self.my_dict:
                self.my_dict[item] += 1
            else:
                self.my_dict[item] = 1

    foo = Foo()

# Generated at 2022-06-13 16:43:04.688403
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    from unittest import TestCase

    class FakeLock(object):
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    class TestLock(TestCase):
        def test_generic_lock(self):
            class TestObj(object):
                def __init__(self):
                    self._lock = FakeLock()

                @lock_decorator()
                def __call__(self):
                    self._lock
                    return True

            obj = TestObj()
            self.assertTrue(obj())

        def test_attr_lock(self):
            class TestObj(object):
                def __init__(self):
                    self._lock = FakeLock()


# Generated at 2022-06-13 16:43:09.621614
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    def sleep(timeout):
        time.sleep(timeout)
        return timeout

    class Sleepy(object):
        def __init__(self):
            self.lock = threading.Lock()

        def __repr__(self):
            return 'Sleepy'

        @lock_decorator(attr='lock')
        def test_a(self, timeout):
            return sleep(timeout)

        @lock_decorator(lock=threading.Lock())
        def test_c(self, timeout):
            return sleep(timeout)

        @lock_decorator()
        def test_d(self, timeout):
            return sleep(timeout)

    s = Sleepy()

    # make sure we can do a basic pass
    assert s.test_a(0.1) == 0.1

# Generated at 2022-06-13 16:43:20.645418
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestLock:
        def __init__(self):
            self.counter = 0
            self.lock = threading.Lock()
        @lock_decorator(attr='lock')
        def increment(self):
            self.counter += 1
        @lock_decorator(lock=threading.Lock())
        def decrement(self):
            self.counter -= 1
    test_obj = TestLock()
    threads = list()
    for i in range(0, 5):
        thread = threading.Thread(target=test_obj.increment)
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
    assert test_obj.counter == 5
    threads = list()
    for i in range(0, 5):
        thread = threading

# Generated at 2022-06-13 16:43:25.648582
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test:
        def __init__(self):
            self.l = []
            self.a = threading.Lock()
        @lock_decorator(lock=threading.Lock())
        def method1(self, v=None):
            self.l.append(v)
        @lock_decorator(attr='a')
        def method2(self, v=None):
            self.l.append(v)

    test = Test()
    v = ['1', '2', '3']
    test.method1(v[0])
    test.method2(v[1])
    with test.a:
        test.method2(v[2])
    assert test.l == v


# Generated at 2022-06-13 16:43:35.588838
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    x = []

    @lock_decorator(lock=lock)
    def test(i):
        x.append(i)

    # By definition, you cannot "prove" a lock works, so we're
    # going to try to force a failure by running the same thread
    # in two different threads, with the lock.
    threads = []
    for i in range(10):
        t = threading.Thread(target=test, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    assert x == range(10)

# Generated at 2022-06-13 16:44:18.458419
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Object:
        def __init__(self, lock=None):
            self._lock = threading.Lock()
            self.is_locked = False

        @lock_decorator()
        def no_lock(self):
            self.is_locked = True

        @lock_decorator(lock=None)
        def no_lock(self):
            self.is_locked = True

        @lock_decorator(attr=None)
        def default_lock(self):
            self.is_locked = True

        @lock_decorator(attr='_lock')
        def explicit_lock(self):
            self.is_locked = True


# Generated at 2022-06-13 16:44:30.542531
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass(object):
        def __init__(self):
            self._lock_attr = threading.Lock()

        @lock_decorator(attr='_lock_attr')
        def lock_attr_method(self):
            self.attr_value = 'lock attr method'

        @lock_decorator(lock=threading.Lock())
        def lock_method(self):
            self.lock_value = 'lock method'

    obj = TestClass()
    assert not hasattr(obj, 'attr_value')
    assert not hasattr(obj, 'lock_value')
    obj.lock_attr_method()
    obj.lock_method()
    assert obj.attr_value == 'lock attr method'
    assert obj.lock_value == 'lock method'

# Generated at 2022-06-13 16:44:38.404096
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Mock(object):
        _lock = threading.Lock()
        _test_attr = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self._test_attr += 1

    mock = Mock()

    def run_thread():
        for i in range(10000):
            mock.increment()

    threads = [threading.Thread(target=run_thread) for x in range(10)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    assert mock._test_attr == 100000

# Generated at 2022-06-13 16:44:45.632831
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    global foo
    foo = 0

    # Ensure that the class below gets a new object each time
    class Test(object):
        def __init__(self, lock):
            self._lock = lock
        @lock_decorator(attr='_lock')
        def test_method(self):
            global foo
            foo += 1

    lock = threading.Lock()
    test = Test(lock)
    assert foo == 0
    test.test_method()
    assert foo == 1

    # This will fail without the ``lock`` decorator
    threads = []
    for i in range(10):
        t = threading.Thread(target=test.test_method)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    assert foo == 11



# Generated at 2022-06-13 16:44:56.975638
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()

    # Test explicit lock
    @lock_decorator(lock=lock)
    def test_explicit_lock(arg):
        return arg

    assert test_explicit_lock('explicit') == 'explicit'

    # Test implicit lock
    class Test(object):
        def __init__(self):
            self._lock = lock

        @lock_decorator(attr='_lock')
        def test_implicit_lock(self, arg):
            return arg

    test = Test()
    assert test.test_implicit_lock('implicit') == 'implicit'

    # Test failure
    try:
        lock_decorator()
    except TypeError as e:
        assert str(e) == 'requires either attr or lock arguments'

# Generated at 2022-06-13 16:45:02.604725
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    l = threading.Lock()
    @lock_decorator(lock=l)
    def func(x, y):
        return x + y
    assert func(1, 2) == 3

    class Foo(object):
        pass
    f = Foo()
    f.l = threading.Lock()
    @lock_decorator(attr='l')
    def bar(x, y):
        return x + y
    assert bar(f, 1, 2) == 3

# Generated at 2022-06-13 16:45:12.554306
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    # pylint: disable=missing-docstring

    class Test(object):
        _lock = threading.Lock()

        def __init__(self):
            self.lock = threading.Lock()
            self.result = 'not set'

        @lock_decorator(attr='_lock')
        @classmethod
        def for_class(cls):
            cls.result = 'for_class'

        @lock_decorator(lock=Test._lock)
        @classmethod
        def for_class_2(cls):
            cls.result = 'for_class_2'

        @lock_decorator()
        def for_instance(self):
            self.result = 'for_instance'


# Generated at 2022-06-13 16:45:20.214838
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class A(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.x = 1
        @lock_decorator(attr='_callback_lock')
        def add_1(self):
            self.x = self.x + 1
        @lock_decorator(lock=threading.Lock())
        def add_2(self):
            self.x = self.x + 2

    a = A()
    assert a.x == 1
    a.add_1()
    a.add_2()
    assert a.x == 4

# Generated at 2022-06-13 16:45:26.509891
# Unit test for function lock_decorator
def test_lock_decorator():
    import ansible.module_utils.sensu_go as sg
    from ansible.module_utils.sensu_go.common.lock import lock_decorator

    @lock_decorator(attr='_lock')
    def my_func(self):
        return self._lock
    sg.AnsibleModule = False
    test_obj = sg.SensuGoModule(argument_spec={}, supports_check_mode=True)
    test_obj._lock = 'test'
    assert test_obj._lock == my_func(test_obj)

# Generated at 2022-06-13 16:45:29.372172
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    @lock_decorator(attr='_lock', lock=lock)
    def locked_method(lock):
        assert lock._is_owned(), "Lock was not owned!"

    # we are not passing the ``lock`` to the method
    locked_method(lock)