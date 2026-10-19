

# Generated at 2022-06-13 16:35:58.554990
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock_decorator_results = []

    thread_count = 10
    total_iterations = 100

    def test_func(self, thread_name, lock):
        for iteration in range(0, total_iterations):
            with lock:
                lock_decorator_results.append((self, thread_name, iteration))

    # Test case to use a pre-defined instance attribute
    class TestClass(object):
        def __init__(self, thread_name, lock):
            self.thread_name = thread_name
            self._lock = lock

        @lock_decorator(attr='_lock')
        def test_method(self):
            test_func(self, self.thread_name, self._lock)


# Generated at 2022-06-13 16:36:03.822796
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class someclass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._attr = 'attr'

        @lock_decorator(attr='_lock')
        def locked_method(self, arg):
            self._attr = arg

    someobj = someclass()

    assert someobj._attr == 'attr'

    someobj.locked_method('someval')
    assert someobj._attr == 'someval'

# Generated at 2022-06-13 16:36:11.704650
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class SomeClass(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def locked_method(self, val):
            return val

        @lock_decorator(lock=threading.Lock())
        def some_other_method(self):
            pass

    def test_thread(val):
        instance.locked_method(val)

    instance = SomeClass()
    for _ in range(4):
        threading.Thread(target=test_thread, args=(_,)).start()
    for _ in range(4):
        instance.some_other_method()

# Generated at 2022-06-13 16:36:22.511895
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from threading import Event
    from time import sleep

    num_threads = 100
    num_iterations = 10
    lock_value = 0
    foo_value = 0
    bar_value = 0
    baz_value = 0

    def foo():
        global foo_value
        @lock_decorator(attr='_foo_lock')
        def foo_locked():
            nonlocal foo_value
            foo_value += 1
        for i in range(num_iterations):
            foo_locked()

    def bar():
        global bar_value
        @lock_decorator(attr='_bar_lock')
        def bar_locked():
            nonlocal bar_value
            bar_value += 1
        for i in range(num_iterations):
            bar_locked()


# Generated at 2022-06-13 16:36:32.508937
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Function ``lock_decorator`` unit test'''

    import threading

    class TestClass(object):
        '''Class used for testing lock decorator'''

        lock_attr = threading.Lock()
        lock_arg = threading.Lock()

        def __init__(self):
            self.lock_arg = threading.Lock()
            self.lock_dynamic = threading.Lock()

        @lock_decorator(attr='lock_attr')
        def lock_attr_method(self):
            '''Test method for lock decorator
            that locks by class attribute'''

            return 'Locked by class attr'


# Generated at 2022-06-13 16:36:40.363071
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class MyClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.test_value = 0

        @lock_decorator(attr='_lock')
        def change_test_value_attr(self, new_value):
            self.test_value = new_value

        @lock_decorator(lock=threading.Lock())
        def change_test_value_lock(self, new_value):
            self.test_value = new_value

    obj = MyClass()
    obj.change_test_value_attr(1)
    obj.change_test_value_lock(2)
    assert obj.test_value == 2

# Generated at 2022-06-13 16:36:48.373309
# Unit test for function lock_decorator
def test_lock_decorator():
    import inspect
    import threading

    # Run tests twice, once with the pre-defined lock attribute
    # and once with the lock passed to the decorator
    for lock in (None, threading.Lock()):
        class TestClass:
            attr = 0

            @lock_decorator(attr='_lock', lock=lock)
            def method(self):
                self.attr += 1
                return self.attr

        obj = TestClass()

        assert obj.method() == 1
        assert obj.method() == 2
        assert obj.method() == 3

        obj2 = TestClass()
        assert obj2.method() == 1

        # Check that the method retains expected attributes
        assert inspect.getargspec(obj.method) == inspect.getargspec(TestClass.method)

# Generated at 2022-06-13 16:36:56.150821
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestLockDecorator:

        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return self.name

        def __eq__(self, other):
            return self.name == other.name

        def __ne__(self, other):
            return not self.__eq__(other)

        @lock_decorator(attr='_lock')
        def test(self):
            return repr(self)

        @lock_decorator(lock=threading.Lock())
        def test_two(self):
            return repr(self)

    tld = TestLockDecorator('this')
    assert tld.test() == 'this'
    assert tld.test_two() == 'this'

# Generated at 2022-06-13 16:37:01.958390
# Unit test for function lock_decorator
def test_lock_decorator():
    import os
    import threading

    # create a test_lock and a function that uses it
    test_lock = threading.Lock()
    @lock_decorator(lock=test_lock)
    def write_file(filename, data):
        '''A very simple function that writes data to a file
        on disk. A basic example of a function that needs to
        be locked from concurrent access.
        '''
        with open(filename, 'w') as f:
            f.write(data)

    # create a hundred threads that all call write_file at once.
    threads = []
    for i in range(100):
        thread = threading.Thread(target=write_file, args=('test.txt', 'foo'))
        thread.start()
        threads.append(thread)

    # wait for all threads to finish

# Generated at 2022-06-13 16:37:12.969412
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test(object):
        _lock = None

        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method(self, value):
            time.sleep(1)
            self.value = value

        @lock_decorator(lock=threading.Lock())
        def method_using_lock(self, value):
            time.sleep(1)
            self.value = value

    t = Test()
    t.method(1)
    t.method_using_lock(2)
    t.method(3)

    assert t.value == 3

__all__ = (
    'lock_decorator',
)

# Generated at 2022-06-13 16:37:23.267048
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class WrapperTest(unittest.TestCase):
        class A:
            def __init__(self):
                self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def foo(self):
            assert self._lock.acquire(blocking=False)
            self._lock.release()

        @lock_decorator(lock=threading.Lock())
        def bar():
            pass


    wrapper_test = WrapperTest()
    wrapper_test.foo()
    wrapper_test.bar()

# Generated at 2022-06-13 16:37:35.277055
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class WorkerThread(threading.Thread):
        def __init__(self, thread_id, worker, lock_attr, lock_obj, *args, **kwargs):
            super(WorkerThread, self).__init__(*args, **kwargs)
            self.thread_id = thread_id
            self.worker = worker
            self.lock_attr = lock_attr
            self.lock_obj = lock_obj

        def run(self):
            self.worker(self.thread_id, self.lock_attr, self.lock_obj)

    class Test(object):
        def __init__(self, lock_attr=None, lock_obj=None):
            self.lock_attr = lock_attr
            self.lock_obj = lock_obj
            self.data = {}

       

# Generated at 2022-06-13 16:37:44.145733
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    # this is an example class
    class SampleClass:

        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_method(self):
            print('test')
            return True

        @lock_decorator(lock=threading.Lock())
        def another_method(self):
            print('another')
            return True

        @lock_decorator(lock=threading.Lock())
        def __non_method(self):
            print('non')
            return True

    s = SampleClass()
    assert s.test_method() is True
    assert s.another_method() is True


# Generated at 2022-06-13 16:37:53.535865
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.counter = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self.counter += 1

        @lock_decorator(lock=threading.Lock())
        def decrement(self):
            self.counter -= 1

    foo = Foo()
    import threading
    threads = []
    for _ in range(100):
        t = threading.Thread(target=foo.increment)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    assert foo.counter == 100

    threads = []

# Generated at 2022-06-13 16:38:03.573418
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    Unit test of ``lock_decorator``:
    tests both the ``attr`` and ``lock`` modes.
    '''
    import threading

    class A():
        '''Test class``A``'''
        # pylint: disable=attribute-defined-outside-init,no-self-use

        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            '''test method for ``lock_decorator``,
            uses already defined lock.
            '''
            return True

    class B():
        '''Test class``B``'''
        # pylint: disable=attribute-defined-outside-init


# Generated at 2022-06-13 16:38:12.193010
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    try:
        import mock
    except ImportError:
        from unittest import mock

    lock = threading.Lock()

    class Test(object):
        @lock_decorator(attr='_lock')
        def a(self):
            return self

        @lock_decorator(lock=lock)
        def b(self):
            return self

        def c(self):
            return self

        @lock_decorator(attr='_lock')
        @lock_decorator(lock=lock)
        def d(self):
            return self

    t = Test()


# Generated at 2022-06-13 16:38:18.772791
# Unit test for function lock_decorator
def test_lock_decorator():
    '''This test will simply run the decorator and make sure it
    does not throw an exception.
    '''
    import threading
    @lock_decorator(attr='_callback_lock')
    def send_callback(self, *args, **kwargs):
        return 'this'

    @lock_decorator(lock=threading.Lock())
    def some_method(self, *args, **kwargs):
        return 'that'

    class Test(object):
        _callback_lock = threading.Lock()
    test = Test()

    assert send_callback(test) == 'this'
    assert some_method(test) == 'that'

# Generated at 2022-06-13 16:38:30.028758
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest

    import threading

    class LockMock(object):
        def __init__(self, real_lock=False):
            if real_lock:
                self.lock = threading.Lock()
            else:
                self.lock = None
            self.enter_count = 0
            self.exit_count = 0

        @lock_decorator(attr='lock')
        def lock_attr(self):
            self.enter_count += 1
            self.exit_count += 1
            return self.enter_count

        @lock_decorator(lock=threading.Lock())
        def lock_local(self):
            self.enter_count += 1
            self.exit_count += 1
            return self.enter_count


# Generated at 2022-06-13 16:38:36.954699
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            # Define a lock in the instance
            self._lock = threading.Lock()

        @lock_decorator('_lock')
        def test_with_attr(self):
            return 'test_with_attr'

        @lock_decorator(lock=threading.Lock())
        def test_with_lock(self):
            return 'test_with_lock'

    t = Test()
    assert t.test_with_attr() == 'test_with_attr'
    assert t.test_with_lock() == 'test_with_lock'

if __name__ == '__main__':
    test_lock_decorator()

# Generated at 2022-06-13 16:38:47.278668
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    # Get instance of the lock decorator
    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def myfunc():
        pass

    assert myfunc.__name__ == 'myfunc'

    # Get instance of the lock decorator with a missing lock object
    lock._acquire()

    @lock_decorator(lock=lock)
    def myfunc_missing_lock():
        pass

    assert myfunc_missing_lock.__name__ == 'myfunc_missing_lock'

    # Get instance of the lock decorator with a missing attribute
    class MyClass():
        def __init__(self):
            pass

    myobj = MyClass()

    @lock_decorator(attr='_lock')
    def myfunc_missing_attr(self):
        pass



# Generated at 2022-06-13 16:38:54.188684
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading
    import time

    class TestLockDecorator(unittest.TestCase):
        def setUp(self):
            self.lock = threading.Lock()
            self.x = 0

        @lock_decorator(attr='lock')
        def incr_locked_self(self, n=1):
            self.x += n
            time.sleep(0.1)
            return self.x

        @lock_decorator(lock=self.lock)
        def incr_locked_param(self, n=1):
            self.x += n
            time.sleep(0.1)
            return self.x

        def incr(self, n=1):
            self.x += n
            time.sleep(0.1)
            return self.x

   

# Generated at 2022-06-13 16:39:04.936757
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        def __init__(self):
            self._cls_lock = threading.Lock()
            self._obj_lock = threading.Lock()
            self.cls_attr = 0
            self.obj_attr = 0

        @classmethod
        @lock_decorator(attr='_cls_lock')
        def incr_cls_attr(cls):
            cls.cls_attr += 1

        @lock_decorator(attr='_obj_lock')
        def incr_obj_attr(self):
            self.obj_attr += 1

    test = Test()
    threads = []
    for i in range(0, 100):
        threads.append(threading.Thread(target=test.incr_cls_attr))

# Generated at 2022-06-13 16:39:15.421349
# Unit test for function lock_decorator
def test_lock_decorator():

    import random

    from threading import Thread, Lock, current_thread

    lock = Lock()
    shared = []

    @lock_decorator(lock=lock)
    def add_to_list(item):
        shared.append(item)

    def worker():
        for _ in range(random.randint(1, 10)):
            item = current_thread().getName() + '-' + str(random.randint(1, 100))
            print(item)
            add_to_list(item)

    threads = []
    for _ in range(5):
        thread = Thread(target=worker)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    assert len(shared) == sum(len(shared) for _ in range(5))

# Generated at 2022-06-13 16:39:21.630997
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except ImportError:
        raise Exception('Unable to import threading')
    from ansible import errors
    from ansible.module_utils.urls import open_url

    class TestClass(object):
        def __init__(self):
            self._lock_attr = threading.Lock()

        @lock_decorator(attr='_lock_attr')
        def a_method(self):
            return 'some return value'

        @lock_decorator(lock=threading.Lock())
        def b_method(self):
            return 'some other return value'

    t = TestClass()
    assert t.a_method() == 'some return value'
    assert t.b_method() == 'some other return value'


# Generated at 2022-06-13 16:39:31.854161
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Verify function lock_decorator'''

    import threading

    # Define a class to use
    class TestClass:
        '''Some test class'''

        _lock = threading.Lock()

        # Define some methods
        value = 0

        def __init__(self):
            pass

        @lock_decorator(attr='_lock')
        def some_method(self):
            TestClass.value += 1
            return TestClass.value

        @lock_decorator(attr='some_attr')
        def some_other_method(self):
            TestClass.value += 1
            return TestClass.value

        @lock_decorator(lock=threading.Lock())
        def some_third_method(self):
            TestClass.value += 1
            return TestClass.value

   

# Generated at 2022-06-13 16:39:42.432321
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    @lock_decorator(attr='_callback_lock')
    def send_callback(self, *args, **kwargs):
        pass

    @lock_decorator(lock=threading.Lock())
    def some_method(*args, **kwargs):
        pass

    class MyClass:
        def __init__(self):
            self._callback_lock = threading.Lock()

    c = MyClass()
    assert c._callback_lock is not None
    with mock.patch('threading.Lock.__enter__') as mock_enter:
        with mock.patch('threading.Lock.__exit__') as mock_exit:
            send_callback(c)
            assert mock_enter.call_count == 1
            assert mock_exit.call_count == 1


# Generated at 2022-06-13 16:39:55.063799
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo:
        @lock_decorator(attr='missing_lock_attr')
        def some_method(self):
            return

    # Make sure we catch missing lock attr
    try:
        foo = Foo()
        foo.some_method()
    except AttributeError:
        pass
    else:
        assert False, "attr lock should raise AttributeError on missing"

    # Make sure we can define a lock attr
    class Foo:
        @lock_decorator(attr='lock_attr')
        def some_method(self):
            return

        def __init__(self):
            self.lock_attr = 4

    # Make sure we can define a lock attr
    try:
        foo = Foo()
        foo.some_method()
    except TypeError:
        pass

# Generated at 2022-06-13 16:40:02.470951
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    This test ensures that no ``NameError`` exception is raised.
    '''
    import threading

    # test using an instance attribute
    class Foo:
        @lock_decorator(attr='_callback_lock')
        def send_callback(self, *args, **kwargs):
            pass

        def __init__(self):
            self._callback_lock = threading.Lock()

    # test using a lock that is passed in
    class Bar:
        @lock_decorator(lock=threading.Lock())
        def send_callback(self, *args, **kwargs):
            pass

    foo = Foo()
    bar = Bar()

    return foo, bar

# Generated at 2022-06-13 16:40:11.408523
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()

    # Test basic functionality of lock_decorator
    @lock_decorator(lock=lock)
    def test_method():
        pass

    # Test that ``test_method`` has a lock, and that it functions
    assert hasattr(test_method, '__lock__')
    assert not lock.acquire(False)
    test_method()
    assert lock.acquire(False)

    # Test that lock_decorator can look for a lock on the instance
    class TestClass(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_method(self):
            pass

    t = TestClass()
    assert not t._lock.acquire(False)
    t.test_method()


# Generated at 2022-06-13 16:40:18.866063
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading, queue

    MAX_COUNT = 10
    lock = threading.Lock()
    q = queue.Queue()
    @lock_decorator(lock=lock)
    def foo(number):
        while q.qsize() < number:
            q.put(number)

    def run(number):
        foo(number)

    for n in range(MAX_COUNT):
        t = threading.Thread(target=run, args=(n,))
        t.start()
    for n in range(MAX_COUNT):
        assert q.get() == n

# Generated at 2022-06-13 16:40:33.017024
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Test if lock_decorator works'''
    import threading

    class FakeLock:
        def __init__(self):
            self.acquire()

        def acquire(self):
            pass

        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_value, exc_traceback):
            pass

    class Test:
        @lock_decorator(attr='_lock')
        def method(self, test_value):
            return test_value


# Generated at 2022-06-13 16:40:42.079433
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self._cb_calls = 0

        @lock_decorator(attr='_callback_lock')
        def cb_method(self, value=None):
            self._cb_calls += 1

        @lock_decorator(lock=threading.Lock())
        def thread_method(self):
            return threading.current_thread()

    c = Test()
    c.cb_method(10)
    c.cb_method(20)
    assert c._cb_calls == 2, c._cb_calls

    thread_lock = threading.Lock()

    @lock_decorator(lock=thread_lock)
    def thread_test():
        return thread

# Generated at 2022-06-13 16:40:51.354065
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    class Example(object):
        _lock = threading.Lock()
        def __init__(self):
            self._value = 0

        @lock_decorator(lock=lock)
        def _increment(self):
            self._value += 1

        @lock_decorator(attr='_lock')
        def _decrement(self):
            self._value -= 1

        def get_value(self):
            return self._value

    example = Example()
    assert example.get_value() == 0

    example._increment()
    assert example.get_value() == 1

    example._decrement()
    assert example.get_value() == 0

# Generated at 2022-06-13 16:41:01.424666
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    from time import sleep
    from random import randint
    import sys

    if sys.version_info[0] == 2:
        from Queue import Queue
    else:
        from queue import Queue

    # This class is used for testing only.
    class test_lock_decorator:

        def __init__(self):
            self.lock = threading.Lock()
            self.queue = Queue()
            self.results = []

        @lock_decorator(attr='lock')
        def test_attr_lock(self, arg):
            # This sleep is just to ensure that the lock works
            # without it, it is possible for the test to pass.
            sleep(0.01)
            self.results.append(arg)
            self.queue.get()


# Generated at 2022-06-13 16:41:07.030000
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    class A(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.time = 0
        @lock_decorator(attr='_callback_lock')
        def recalc_time(self):
            self.time += 1
    a = A()
    for x in range(100):
        t = threading.Thread(target=a.recalc_time)
        t.start()
    time.sleep(1)
    assert a.time == 1, 'Expected `a.time` to remain 1, but was ' + str(a.time)

# Generated at 2022-06-13 16:41:16.765747
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    l = []

    class TestClass(object):
        @lock_decorator(lock=lock)
        def test_method(self):
            l.extend(['test_method'])

    @lock_decorator(attr='_l')
    def test_method(self):
        self._l.extend(['test_method'])

    @lock_decorator(lock=lock)
    def test_function():
        l.extend(['test_function'])

    @lock_decorator(attr='_l')
    def test_function(self):
        self._l.extend(['test_function'])

    def worker():
        tc = TestClass()
        tc.test_method()

    def worker2():
        t

# Generated at 2022-06-13 16:41:26.708420
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    l = threading.RLock()
    val = 0
    def func():
        global val
        val += 1
        return val

    func = lock_decorator(lock=l)(func)

    # Run func in parallel and expect it to return all different values
    # because it's locked
    assert all(func() for _ in range(10)) == list(range(1, 11))

    # Create a class and run the same test
    class Test(object):
        def __init__(self):
            self.lock = threading.RLock()

        @lock_decorator(attr='lock')
        def func(self):
            global val
            val += 1
            return val

    t = Test()

# Generated at 2022-06-13 16:41:37.079038
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading
    import time

    class Foo(object):
        def __init__(self, name):
            self.name = name
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def bar(self, x, y):
            time.sleep(1)
            return x * y

    foos = [
        Foo(name='a'),
        Foo(name='b'),
        Foo(name='c'),
        Foo(name='d'),
    ]

    with mock.patch('__builtin__.print') as pr:
        threads = []
        for f in foos:
            t = threading.Thread(target=f.bar, args=(3, 4))
            t.start()
            threads.append(t)


# Generated at 2022-06-13 16:41:44.725709
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Foo(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.called = []

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, value):
            self.called.append(value)
            time.sleep(2)

    f = Foo()

    def first():
        f.send_callback('first')

    def second():
        f.send_callback('second')

    first_thread = threading.Thread(target=first)
    second_thread = threading.Thread(target=second)

    first_thread.start()
    time.sleep(1)
    second_thread.start()

    for thread in [first_thread, second_thread]:
        thread.join()

# Generated at 2022-06-13 16:41:56.676168
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    # Create a simple class to test
    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._count = 0

        @lock_decorator(attr='_lock')
        def _inc_count(self):
            self._count += 1

        def inc_count(self):
            self._inc_count()

        def get_count(self):
            return self._count

    # Create the instance of the class
    f = Foo()

    # Create a couple threads to change the state of the class
    def thread_func(times):
        for _ in range(times):
            f.inc_count()

    threads = []
    for t in range(10):
        t = threading.Thread(target=thread_func, args=(10,))

# Generated at 2022-06-13 16:42:16.381053
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    import logging
    import threading
    try:
        from unittest import mock
    except ImportError:
        import mock

    logging.config.dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s %(levelname)-8s %(thread)d %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'DEBUG',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    })
    logger = logging.getLogger(__name__)


# Generated at 2022-06-13 16:42:22.099170
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestLockDecorator(threading.Lock):
        @lock_decorator(attr='_lock')
        def spam(self):
            return True

        @lock_decorator(lock=threading.Lock())
        def eggs(self):
            return True

    t = TestLockDecorator()
    assert t.spam()
    assert t.eggs()

# Generated at 2022-06-13 16:42:29.318249
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading

    class TestLock(object):
        # Use a single lock for the entire class
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def with_class_lock(self, n):
            time.sleep(n)

        @lock_decorator(lock=threading.Lock())
        def with_explicit_lock(self, n):
            time.sleep(n)

        # this method will not be locked
        def no_lock(self, n):
            time.sleep(n)

    t = TestLock()
    for i in range(2):
        for func in [t.no_lock, t.with_class_lock, t.with_explicit_lock]:
            for j in range(2):
                start = time.time

# Generated at 2022-06-13 16:42:40.528083
# Unit test for function lock_decorator
def test_lock_decorator():
    '''This function runs unit tests on lock_decorator
    '''
    import threading
    import time

    test_num = 2

    # This class is used to ensure that the lock_decorator works
    # correctly, when a class method is being decorated
    class TestClass:

        def __init__(self, *args, **kwargs):
            self.test_num = test_num

        @lock_decorator(attr='_lock')
        def class_method(self, *args, **kwargs):
            for i in xrange(self.test_num):
                print(i)
                time.sleep(1)

        def run(self):
            for i in xrange(self.test_num):
                print(i)
                time.sleep(1)


    # This function is used to ensure

# Generated at 2022-06-13 16:42:50.645723
# Unit test for function lock_decorator
def test_lock_decorator():
    from __future__ import print_function
    from time import sleep

    import threading

    l = threading.Lock()

    class Foo:
        def __init__(self):
            self.value = 0
            self.lock = threading.Lock()

        @lock_decorator()
        def add_to_value(self, value):
            self.value += value

        @lock_decorator(attr='lock')
        def add_to_value_2(self, value):
            self.value += value

    def print_value(foo, value, sleep_time=1):
        with l:
            print('Started')
            foo.add_to_value(value)
            sleep(sleep_time)
            print(foo.value)


# Generated at 2022-06-13 16:43:01.885903
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread
    from time import sleep
    import sys
    import textwrap
    from six import StringIO
    from ansible.module_utils._text import to_text

    class Dummy(object):

        def __init__(self):
            self._counter = 0
            # This context manager will raise an exception if it's
            # not being used as a context manager
            self._lock = Lock()

        @lock_decorator(attr='_lock')
        def increment(self):
            self._counter += 1

    d = Dummy()

    # This should not block
    d.increment()
    assert d._counter == 1

    # Let's see what happens when we run a bunch of threads
    # at the same time

# Generated at 2022-06-13 16:43:10.886060
# Unit test for function lock_decorator
def test_lock_decorator():
    # Logic for tests are borrowed from test_threading.TestLock

    # Ensure that a newly created lock starts unlocked
    l = threading.Lock()
    assert not l.locked()

    # Ensure acquiring and releasing the lock works as expected
    l.acquire()
    assert l.locked()
    l.release()
    assert not l.locked()

    # Ensure that after the lock has been acquired, the same thread can
    # acquire it again not block, but any other thread will.
    l.acquire()
    assert l.acquire(0)

    # create an event that will be used to signal when the lock is
    # acquired by a separate thread
    evt = threading.Event()
    def f():
        l.acquire()
        evt.set()
        l.release()

# Generated at 2022-06-13 16:43:21.238674
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    class myclass(object):
        def __init__(self):
            self.someattr = 0
            self._someotherattr = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def somefunc(self):
            time.sleep(1)
            self.someattr += 1
            return self.someattr

    for _ in range(10):
        assert myclass().somefunc() == 1

    class myclass2(object):
        def __init__(self):
            self.someattr = 0
            self._someotherattr = 0
            self.lock = threading.Lock()

        @lock_decorator(lock=threading.Lock())
        def somefunc2(self):
            time.sleep(1)
            self

# Generated at 2022-06-13 16:43:26.419718
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    # Test with attr param
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def func(self):
            return threading.current_thread().name

    t1 = threading.Thread(target=Test().func)
    t2 = threading.Thread(target=Test().func)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    assert t1.result == t2.result

    # Test with lock param
    lock = threading.Lock()
    @lock_decorator(lock=lock)
    def func2():
        return threading.current_thread().name


# Generated at 2022-06-13 16:43:37.368349
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    class A(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.result = []

        @lock_decorator(attr='_lock')
        def foo(self, value):
            self.result.append(value)
            time.sleep(0.1)
            self.result.append(value)

        @lock_decorator(lock=threading.Lock())
        def bar(self, value):
            self.result.append(value)
            time.sleep(0.1)
            self.result.append(value)

    a = A()
    a.foo('foo')
    assert a.result == ['foo', 'foo']

    a.bar('bar')

# Generated at 2022-06-13 16:44:02.199683
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import sys

    class TestClass(object):
        def __init__(self):
            self.count = 0
            self.lock = threading.Lock()

        @lock_decorator()
        def test_method(self):
            self.count += 1
            time.sleep(1)

    def test_method_lock():
        test_class.test_method()

    test_class = TestClass()
    for i in range(3):
        th = threading.Thread(target=test_method_lock)
        th.daemon = True
        th.start()

    time.sleep(2)
    sys.exit(test_class.count - 3)

if __name__ == '__main__':
    sys.exit(test_lock_decorator())

# Generated at 2022-06-13 16:44:13.587546
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Demo(object):
        _lock = threading.Lock()
        _result = 0
        _threads = None

        @lock_decorator(attr='_lock')
        def threadsafe_increment(self, value=1):
            self._result += value

        def start_threads(self, threads=50):
            self._threads = [threading.Thread(target=self.threadsafe_increment) for _ in range(0, threads)]
            for thread in self._threads:
                thread.start()

        def wait_for_threads(self):
            for thread in self._threads:
                thread.join()

    d = Demo()
    d.start_threads()
    d.wait_for_threads()
    assert d._result == 50

# Generated at 2022-06-13 16:44:18.757385
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, sleep=None):
            print('Callback {}'.format(id(self)))
            if sleep:
                time.sleep(sleep)
            return True

    class Test2(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(lock=self._callback_lock)
        def send_callback(self, sleep=None):
            print('Callback {}'.format(id(self)))
            if sleep:
                time.sleep(sleep)
            return True


# Generated at 2022-06-13 16:44:30.954201
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import importlib.util
        import sys
        import threading
        spec = importlib.util.spec_from_file_location(
            'unit_test_lock_decorator',
            sys.modules[__name__].__file__)
        unit_test_lock_decorator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(unit_test_lock_decorator)
        unit_test_lock_decorator.main(threading.Lock())
    except ImportError:
        # Python 2
        import imp
        import threading
        unit_test_lock_decorator = imp.load_source(
            'unit_test_lock_decorator',
            __file__)

# Generated at 2022-06-13 16:44:38.708960
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    @lock_decorator(attr='_lock')
    def func(self):
        self.flag = True
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.flag = False
    t = Test()
    t.func = func
    t.func()
    assert t.flag

    @lock_decorator(lock=threading.Lock())
    def func2():
        t2.flag = True
    t2 = Test()
    t2.flag = False
    func2()
    assert t2.flag

# Generated at 2022-06-13 16:44:43.947662
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    from time import sleep

    class Something(object):

        _my_lock = threading.Lock()

        @lock_decorator(attr='_my_lock')
        def foo(self):
            sleep(0.5)

        @lock_decorator(attr='_my_lock')
        def bar(self):
            sleep(0.1)

        @lock_decorator(lock=threading.Lock())
        def foobar(self):
            sleep(0.1)

    import pytest

    @pytest.mark.parametrize('f', (Something.foo, Something.bar))
    def test_lock_decorator_attr(f):
        x = Something()
        y = Something()
        t1 = threading.Timer(0.1, lambda: x.foo())

# Generated at 2022-06-13 16:44:53.768041
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread
    import time

    # Note: under python2, you need to specify the __metaclass__
    # variable to use class Lock(object)
    class Lock(object):
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def foo(self):
            time.sleep(10)

        @lock_decorator(lock=threading.Lock())
        def bar(self):
            time.sleep(10)

    lock = Lock()
    t1 = Thread(target=lock.foo)
    t2 = Thread(target=lock.bar)
    t1.start()
    t2.start()
    time.sleep(1)
    assert t1.is_alive() is True

# Generated at 2022-06-13 16:45:02.402922
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    class MyClass(object):
        def __init__(self):
            self._callback_lock = Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, arg1, arg2, arg3):
            return arg1, arg2, arg3

        @lock_decorator(lock=Lock())
        def some_method(self, arg1, arg2, arg3):
            return arg1, arg2, arg3

    a = MyClass()
    assert a.send_callback(1, 2, 3) == (1, 2, 3)
    assert a.some_method(4, 5, 6) == (4, 5, 6)

# Generated at 2022-06-13 16:45:12.375214
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    test_lock = threading.Lock()
    test_attr = '_test_lock'

    class TestClass(object):
        def __init__(self):
            setattr(self, test_attr, threading.Lock())

        def test_method(self):
            pass

        @lock_decorator(lock=test_lock)
        def lock_decorated_method(self, lock=None):
            assert lock is not None
            assert lock is test_lock

        @lock_decorator(attr=test_attr)
        def attr_decorated_method(self, lock=None):
            assert lock is not None
            assert lock is getattr(self, test_attr)

    t = TestClass()
    t.lock_decorated_method()
    t

# Generated at 2022-06-13 16:45:18.309485
# Unit test for function lock_decorator
def test_lock_decorator():
    class SomeClass(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def some_method(self):
            return self._lock

        @lock_decorator(lock=threading.Lock())
        def some_other_method(self):
            return self._lock

    s = SomeClass()
    assert s.some_method() == s.some_other_method()