

# Generated at 2022-06-13 16:35:57.916029
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class A(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='lock')
        def increment_value(self):
            time.sleep(2)
            self.value += 1


    # create an instance of class A
    a = A()

    import random

    # spawn 10 threads, each trying to increment the value once
    for i in range(10):
        t = threading.Thread(target=a.increment_value)
        t.start()

    # wait for all the threads to finish
    for t in threading.enumerate():
        if t is not threading.current_thread():
            t.join()

    print(a.value)

    # output

# Generated at 2022-06-13 16:36:07.786710
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class MockLock(object):
        def __init__(self):
            self.counter = 0
        def __enter__(self):
            self.counter += 1
        def __exit__(self, type, value, traceback):
            self.counter -= 1

    class MockLock2(object):
        def __init__(self):
            self.counter = 0
        def __enter__(self):
            self.counter += 1
            # Make sure we don't stay locked forever
            # by entering twice, and using two exits
            self.counter += 1
        def __exit__(self, type, value, traceback):
            self.counter -= 1
            self.counter -= 1

    class LockTester(object):
        def __init__(self):
            self._lock = MockLock()



# Generated at 2022-06-13 16:36:19.271085
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):
        def __init__(self):
            self.result = []

        @lock_decorator(attr='lock')
        def foo(self, arg):
            self.result.append(arg)

        def _get_lock(self):
            return self._lock

    foo = Foo()
    foo.lock = threading.Lock()

    threads = []
    for i in range(0, 10):
        threads.append(threading.Thread(target=foo.foo, args=(i,)))

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert len(foo.result) == len(set(foo.result))

    class Bar(object):
        def __init__(self):
            self.result = []

       

# Generated at 2022-06-13 16:36:29.622292
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    def generic_func():
        pass

    class GenericClass():
        def instance_method(self):
            pass

        @classmethod
        def class_method(cls):
            pass

        @staticmethod
        def static_method():
            pass

    def test_function():
        '''Tests the decorator on a standard function'''
        decorated = lock_decorator(lock=threading.Lock())(generic_func)

        with mock.patch.object(threading.Lock, '__enter__') as mock_enter:
            with mock.patch.object(threading.Lock, '__exit__') as mock_exit:
                decorated()

                assert mock_enter.call_count == 1
                assert mock_exit.call_count == 1


# Generated at 2022-06-13 16:36:37.064279
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def test():
        return True

    @lock_decorator(attr='lock')
    def test2(self):
        return True

    class TestObj(object):
        lock = threading.Lock()

        def test(self):
            return True

    test_obj = TestObj()

    # method not locked
    assert test()

    # While test is running, try and run test2
    _finished = threading.Event()

    def t2():
        _finished.wait()
        expected = True
        try:
            actual = test2(test_obj)
        except RuntimeError:
            print("test2 did not raise exception")
            return False
        return expected == actual

    t = threading.Thread

# Generated at 2022-06-13 16:36:46.332185
# Unit test for function lock_decorator
def test_lock_decorator():
    from io import StringIO
    import sys
    import threading

    temp_stdout = StringIO()
    old_stdout = sys.stdout
    sys.stdout = temp_stdout

    class Test(object):

        def __init__(self):
            self._lock = _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method_one(self):
            print('method_one')

        @lock_decorator(lock=threading.Lock())
        def method_two(self):
            print('method_two')

    expected = '''method_one
method_two
'''

    t = Test()
    t.method_one()
    t.method_two()
    assert temp_stdout.getvalue() == expected


# Generated at 2022-06-13 16:36:55.298328
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    from asynctest import TestCase, MagicMock

    class Dummy(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.thread_pool = []

        def start_thread(self, method, is_running):
            print('Starting thread with method name {methodname}...'.format(methodname=method.__name__))
            t = threading.Thread(target=method, args=(is_running,))
            t.start()
            self.thread_pool.append(t)

        @lock_decorator('lock')
        def locked_method(self, is_running):
            i = 0
            while is_running():
                print('{threadname} is running...'.format(threadname=threading.current_thread().name))
                i

# Generated at 2022-06-13 16:37:05.834334
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading
    import unittest

    class Test(unittest.TestCase):
        def setUp(self):
            self.l = []
            self.lock = threading.Lock()

        def test_lock_decorator_attr(self):
            @lock_decorator(attr='lock')
            def append_item(item):
                self.l.append(item)

            self.assertEqual(len(self.l), 0)
            self.assertEqual(append_item('test'), None)
            self.assertEqual(len(self.l), 1)


# Generated at 2022-06-13 16:37:15.339333
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class UnlockClass(object):
        '''A class used to test the @lock_decorator decorator using a
        pre-defined class attribute.
        '''
        def __init__(self, is_locked=False):
            self.is_locked = is_locked
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def lock_method(self):
            assert not self.is_locked, "lock_method() should not be called if 'is_locked' is True"

        def get_lock(self):
            return self._lock

    uc_no_lock = UnlockClass()
    uc_no_lock.lock_method()
    assert uc_no_lock.get_lock().locked() is False

    uc_lock = UnlockClass

# Generated at 2022-06-13 16:37:24.166659
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    global_var = 0
    class Test:
        def __init__(self):
            self.attr_lock = threading.Lock()

        @lock_decorator(attr='attr_lock')
        def attr_lock_test(self):
            global global_var
            global_var += 1
            assert global_var == 1

        @lock_decorator(attr='attr_lock')
        def attr_lock_test_return(self):
            global global_var
            global_var += 1
            assert global_var == 2
            return global_var

        @lock_decorator(lock=lock)
        def lock_test(self):
            global global_var
            global_var += 1
            assert global_var == 3


# Generated at 2022-06-13 16:37:37.939205
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Counter(object):
        """A simple counter to aid in testing the lock decorator"""
        _lock = threading.Lock()
        _counter = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self._counter += 1

        def get_counter(self):
            return self._counter

    counter = Counter()

    def thread_function(counter_obj):
        for _ in range(100):
            counter_obj.increment()

    for i in range(10):
        t = threading.Thread(target=thread_function, args=(counter,))
        t.start()

    # Wait for all threads to finish
    for i in range(10):
        t.join()

    assert counter.get_counter() == 1000

# Generated at 2022-06-13 16:37:46.448873
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        from threading import Lock
        from threading import current_thread
        from Queue import Queue
    except ImportError:
        return

    class Foo(object):

        def __init__(self):
            self._lock = Lock()

        @lock_decorator(attr='_lock')
        def bar(self, q):
            q.put(current_thread().name)

    # This test is primarily to make sure the decorator works at all
    q = Queue()

    foo = Foo()
    foo.bar(q)

    assert q.get() == 'MainThread'

    def another_bar(self, q):
        q.put(current_thread().name)

    # This is the real test
    q = Queue()

    # By default ``lock`` is None, so this will use ``attr

# Generated at 2022-06-13 16:37:55.555797
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    # Setup
    lock = threading.Lock()
    test_lock_attr = 'test_lock'
    named_lock = 'named_lock'
    test_counter = 0
    named_counter = 0

    # Create a test class with a lock attribute
    class TestClass:
        def __init__(self):
            # Set the object attribute for testing
            self.test_lock = threading.Lock()
            self.named_lock = threading.Lock()

        @lock_decorator(attr=test_lock_attr)
        def test_method(self):
            nonlocal test_counter
            test_counter = test_counter + 1
            time.sleep(0.5)
            return test_counter


# Generated at 2022-06-13 16:38:00.334670
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test:
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            pass

    t = Test()
    t.send_callback()

# Generated at 2022-06-13 16:38:08.208986
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    This unit test is designed to be ran in Python 2 and 3.
    '''
    from six.moves import _thread as thread

    import inspect
    import random
    import six

    import pytest

    # Create a class instance for test purposes
    class Foo(object):

        def __init__(self):
            self._lock = thread.allocate_lock()
            self.buffer = []
            self.result = ''

        @staticmethod
        @lock_decorator(attr='_lock')
        def static_append(inst, item):
            inst.buffer.append(item)

        @classmethod
        @lock_decorator(attr='_lock')
        def class_append(cls, inst, item):
            inst.buffer.append(item)


# Generated at 2022-06-13 16:38:14.747388
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        attr_lock = lock_decorator(attr='_lock')
        def __init__(self):
            self._lock = threading.RLock()
            self._n = 0

        @attr_lock
        def count_attr(self):
            self._n += 1

        explicit_lock = lock_decorator(lock=threading.RLock())

        @explicit_lock
        def count_explicit(self):
            self._n += 1

    # Confirm counts are the same and both paths work
    t = Test()
    t.count_attr()
    t.count_explicit()
    assert t._n == 2



# Generated at 2022-06-13 16:38:26.384542
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    mutex = threading.Lock()

    class Foo(object):
        def __init__(self):
            self._mutex = mutex

        @lock_decorator(attr='_mutex')
        def prevented_race(self):
            import time
            time.sleep(1)
            return 'bar'

        @lock_decorator(lock=mutex)
        def prevented_race_2(self):
            import time
            time.sleep(1)
            return 'foo'

    foo = Foo()

    import time
    start = time.time()
    prevented_race_threads = [
        threading.Thread(target=foo.prevented_race)
        for _ in range(10)
    ]

# Generated at 2022-06-13 16:38:35.344547
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test:
        lock = threading.Lock()

        def __init__(self):
            self._callbacks = []

        @lock_decorator(lock=lock)
        def send_callback(self, message):
            with self.lock:
                self._callbacks.append(message)
            return len(self._callbacks)

        @lock_decorator(attr='_lock')
        def _with_attr(self, message):
            with self._lock:
                self._callbacks.append(message)
            return len(self._callbacks)

    t = Test()

    def callback_thread(cb):
        for i in range(10):
            cb('Test %d' % i)
            time.sleep(1)

    threads = []

# Generated at 2022-06-13 16:38:45.865496
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    threading_lock = threading.Lock()
    def thread_function(function, lock):
        try:
            with lock:
                function()
        except RuntimeError as e:
            print(e)
    @lock_decorator(lock=threading_lock)
    def simple_method():
        print("simple_method called")
    simple_method()
    try:
        thread = threading.Thread(target=thread_function, args=(simple_method, threading_lock))
        thread.start()
        thread.join()
    except RuntimeError as e:
        print(e)

if __name__ == '__main__':
    test_lock_decorator()

# Generated at 2022-06-13 16:38:56.045494
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test:
        def __init__(self):
            self.test_attr = []

        @lock_decorator(attr='test_lock')
        def test_method(self):
            time.sleep(2)
            self.test_attr.append('test')

        @lock_decorator(lock=threading.Lock())
        def test_method2(self):
            time.sleep(2)
            self.test_attr.append('test')

    test = Test()
    test.test_lock = threading.Lock()

    t = threading.Thread(target=test.test_method)
    t.start()
    t2 = threading.Thread(target=test.test_method)
    t2.start()

    t.join()

# Generated at 2022-06-13 16:39:08.752070
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Dummy(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 1

        def increment_value(self):
            # The lock here is not thread-safe, but the decorator is
            self.lock.acquire()
            self.value += 1
            self.lock.release()

        @lock_decorator(attr='lock')
        def increment_value_decorated(self):
            # The decorator should automatically acquire and release
            # the instance lock
            self.value += 1

        @lock_decorator(lock=threading.Lock())
        def increment_value_lock(self):
            # Using a lock object should do the same
            self.value += 1

    from threading import Thread
    import time


# Generated at 2022-06-13 16:39:17.246295
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        @lock_decorator(attr='_self_lock')
        def self_locked(self, some_param):
            print('Hello, {}'.format(some_param))

        @lock_decorator(lock=threading.Lock())
        def explicit_lock(self, some_param):
            print('Hello, {}'.format(some_param))

    t = Test()
    t.self_locked('World!')
    t.explicit_lock('World!')

# Generated at 2022-06-13 16:39:29.005949
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._var = None
        @lock_decorator(attr='_lock')
        def method(self, value):
            time.sleep(1)
            self._var = value
    foo = Foo()
    class Bar(object):
        _lock = threading.Lock()
        _var = None
        @classmethod
        @lock_decorator(attr='_lock')
        def method(cls, value):
            time.sleep(1)
            cls._var = value
    bar = Bar()
    # Create a couple of threads and run the protected method
    threads = []

# Generated at 2022-06-13 16:39:37.028805
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import random

    lock = threading.Lock()

    class Test(object):
        def __init__(self):
            self.x = 0
            self.lock = lock

        @lock_decorator(lock=lock)
        def add(self, num):
            self.x += num

        @lock_decorator(attr='lock')
        def div(self, num):
            time.sleep(random.random())
            self.x /= num

    test = Test()
    threads = []
    for i in range(100):
        def func():
            test.add(1)
            test.div(2)
        t = threading.Thread(target=func)
        threads.append(t)
        t.start()


# Generated at 2022-06-13 16:39:45.559089
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo(object):

        def __init__(self, *args, **kwargs):
            self._lock = kwargs.pop('lock', None)

        @lock_decorator(attr='_lock')
        def locked_method(self):
            return True

    foo = Foo()
    assert foo.locked_method() is True

    class Bar(object):

        def __init__(self, *args, **kwargs):
            pass

        @lock_decorator(attr='_lock')
        def locked_method(self):
            return True

    bar = Bar()
    try:
        bar.locked_method()
    except AttributeError:
        assert True
    else:
        assert False, "No AttributeError raised"


# Generated at 2022-06-13 16:39:56.713585
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except ImportError:
        return
    import time
    import random

    class Foo:
        _lock = threading.Lock()
        _result = ''

        @lock_decorator(attr='_lock')
        def method(self, *args, **kwargs):
            time.sleep(random.randint(1, 100)/100)
            self._result += ''.join(args)

    foo = Foo()

    def threads():
        while True:
            foo.method(chr(random.randrange(ord('a'), ord('z'))))

    threads = [threading.Thread(target=threads) for _ in range(16)]
    for t in threads:
        t.daemon = True
        t.start()
    for t in threads:
        t.join()



# Generated at 2022-06-13 16:40:05.303093
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    Test lock_decorator functionality
    '''
    import threading
    _lock = threading.Lock()
    test_val = 0

    # Check to see if the lock decorator does what we expect.
    #
    # Send 1000 threads at an incrementing function.
    # If we don't have a lock, the results should
    # be between 1,000 and 10,000.
    #
    # If we do have a lock, the results should be exactly
    # equal to 1000.
    @lock_decorator(lock=_lock)
    def test_lock(n):
        global test_val
        test_val += n

    locks = [False, True]
    for use_lock in locks:
        # Reset the test_val
        test_val = 0

        # Create the list of threads


# Generated at 2022-06-13 16:40:17.225177
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading
    import unittest

    class Delay:
        def __init__(self, delay=None, lock=None):
            self.delay = delay or 0
            self.lock = lock or threading.Lock()

        def init_delay(self, delay=None):
            with self.lock:
                self._init_delay(delay)

        @lock_decorator(attr='lock')
        def _init_delay(self, delay=None):
            if delay:
                self.delay = delay

        @property
        @lock_decorator(attr='lock')
        def delay(self):
            return self._delay

        @delay.setter
        @lock_decorator(attr='lock')
        def delay(self, delay):
            self._delay = delay


# Generated at 2022-06-13 16:40:24.512019
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class SomeClass(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            pass

    assert isinstance(SomeClass().send_callback, type(SomeClass))

    @lock_decorator(lock=threading.Lock())
    def some_method():
        pass

    assert isinstance(some_method, type(SomeClass))

# Generated at 2022-06-13 16:40:30.386723
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Dummy(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, arg):
            return arg

    dummy = Dummy()

    assert dummy.send_callback('hello') == 'hello'

# Generated at 2022-06-13 16:40:49.928797
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestClass(object):

        def __init__(self):
            self._counter = 0
            self._lock = threading.Lock()

        def __str__(self):
            return str(self._counter)

        @lock_decorator(attr='_lock')
        def increment_attr_lock(self):
            for _ in range(0, 100):
                self._counter += 1
                time.sleep(0.00001)
            return self._counter

        @lock_decorator(lock=threading.Lock())
        def increment_argument_lock(self):
            for _ in range(0, 100):
                self._counter += 1
                time.sleep(0.00001)
            return self._counter

    test_class = TestClass()

    threads_attr_lock

# Generated at 2022-06-13 16:40:56.733968
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    # Uses a thread lock type
    class MyClass(object):
        def __init__(self):
            self.lock = threading.Lock()

            self.internet = 0
            self.satellites = 0

        @lock_decorator(attr='lock')
        def internet_surf_increase(self, count=1):
            self.internet += count

        @lock_decorator(lock=threading.Lock())
        def satellite_orbit_decrease(self, count=1):
            self.satellites -= count

    my_class = MyClass()

    # Test to make sure the lock is being applied.  We are mocking
    # the lock since we don't actually need it to be a real thread
    # lock

# Generated at 2022-06-13 16:41:04.466609
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass(object):
        def __init__(self, *args, **kwargs):
            self.lock = threading.Lock()
            self.counter = 0
        @lock_decorator(attr='lock')
        def increment(self):
            self.counter += 1
        @lock_decorator(lock=threading.Lock())
        def decrement(self):
            self.counter -= 1
    import multiprocessing
    class TestProcess(multiprocessing.Process):
        def __init__(self, testclass):
            self.testclass = testclass
            super(TestProcess, self).__init__()
        def run(self):
            self.testclass.increment()
            self.testclass.decrement()
    test = TestClass()
    threads = []

# Generated at 2022-06-13 16:41:15.244461
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Test for function lock_decorator'''
    import threading
    from threading import Lock

    class X(object):
        '''A test class that has a lock'''
        def __init__(self):
            self.x = 0
            self.inc_lock = Lock()

        @lock_decorator(attr='inc_lock')
        def inc(self):
            '''A test method that can use the lock'''
            self.x += 1

        def getx(self):
            '''A test method that can use the lock'''
            return self.x

        def setx(self, val):
            '''A test method that can use the lock'''
            self.x = val

    ROUNDS = 100
    x = X()

    # Test 1: Using self-defined attr


# Generated at 2022-06-13 16:41:23.143788
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._counter = 0

        @lock_decorator()
        def increment_counter(self):
            self._counter += 1

        @lock_decorator(attr='_lock')
        def update_counter(self, value):
            self._counter = value

    t = Test()
    t.increment_counter()
    t.update_counter(10)
    assert t._counter == 10

# Generated at 2022-06-13 16:41:29.287964
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestLocks(object):
        _lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def foo(self, num):
            return num % 2 == 0
        @lock_decorator(lock=threading.Lock())
        def bar(self, num):
            return num % 2 != 0
    tl = TestLocks()
    assert tl.foo(0)
    assert not tl.bar(0)
    assert not tl.foo(1)
    assert tl.bar(1)

# Generated at 2022-06-13 16:41:39.168703
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class LockDecoratorTestClass(object):
        def __init__(self):
            self.attr_lock = threading.Lock()
            self.attr = 0

        @lock_decorator(attr='attr_lock')
        def attr_test(self):
            self.attr += 1

        @lock_decorator(lock=threading.Lock())
        def lock_test(self):
            self.attr += 1

    ldt = LockDecoratorTestClass()

    threads = []
    for i in range(10):
        thread = threading.Thread(target=ldt.attr_test)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    assert ldt.attr == 10

    ldt.attr = 0
   

# Generated at 2022-06-13 16:41:45.611969
# Unit test for function lock_decorator
def test_lock_decorator():
    # Python3 syntax only
    class TestClass:
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator()
        def test_method(self):
            print('Hello World')

        @lock_decorator(lock=threading.Lock())
        def test_method_2(self):
            print('Goodbye World')

    t = TestClass()
    t.test_method()
    t.test_method_2()

if __name__ == '__main__':
    # This is the actual unit test when you run this file.
    # Must have threading module available
    import threading
    test_lock_decorator()

# Generated at 2022-06-13 16:41:54.183260
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        from threading import Lock
    except ImportError:
        import sys
        print('Skipping test_lock_decorator', file=sys.stderr)
        return

    class Test(object):
        _lock = Lock()

        @lock_decorator(attr='_lock')
        def test_attr(self):
            return 0

        @lock_decorator(lock=Lock())
        def test_lock(self):
            return 0

    test = Test()
    assert test.test_attr() == 0
    assert test.test_lock() == 0

# Generated at 2022-06-13 16:41:57.503329
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo:
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def do_stuff(self):
            '''Do stuff'''

    f = Foo()
    f.do_stuff()
    # Ensure docstring was not lost
    assert f.do_stuff.__doc__ == 'Do stuff'

# Generated at 2022-06-13 16:42:22.492887
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    l = threading.Lock()
    class SomeClass(object):
        def __init__(self):
            self._lock = l

        def _do_something(self):
            pass

        @lock_decorator(attr='_lock')
        def do_something(self):
            self._do_something()

    sc = SomeClass()

    class SomeOtherClass(object):
        def _do_something(self):
            pass

        @lock_decorator(lock=l)
        def do_something(self):
            self._do_something()

    soc = SomeOtherClass()

    assert sc.do_something() == soc.do_something() == None

# Generated at 2022-06-13 16:42:28.603265
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test:
        def __init__(self):
            self._lock = threading.Lock()
            self._val = 0

        @lock_decorator(attr='_lock')
        def inc(self):
            self._val += 1

    test = Test()

    assert test._val == 0
    test.inc()
    assert test._val == 1

    with threading.Lock():
        assert test._val == 0

# Generated at 2022-06-13 16:42:36.734148
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading, time, unittest

    class LockTest(unittest.TestCase):

        def __init__(self, *args, **kwargs):
            super(LockTest, self).__init__(*args, **kwargs)
            self.s = 0 # shared value
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def protected_increment(self):
            '''Increment ``s`` by 1'''
            self.s += 1
            return self.s

        @lock_decorator(lock=threading.Lock())
        def mutex_increment(self):
            '''Increment ``s`` by 1'''
            self.s += 1
            return self.s


# Generated at 2022-06-13 16:42:46.996826
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self, *args, **kwargs):
            pass

        __init__._lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def __init__(self, *args, **kwargs):
            pass

    class Test2(object):
        @lock_decorator(lock=threading.Lock())
        def some_method(self):
            pass

    assert hasattr(Test.__init__, '_lock')
    assert isinstance(Test.__init__._lock, threading.Lock)

    assert hasattr(Test2.some_method, '_lock')
    assert isinstance(Test2.some_method._lock, threading.Lock)

# Generated at 2022-06-13 16:42:58.201883
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    class Class1:
        def __init__(self):
            self._callback_lock = threading.Lock()
        @lock_decorator(attr='_callback_lock')
        def test_method(self):
            print("Class1: %s" % self._callback_lock)

    class Class2:
        def __init__(self, lock):
            self._callback_lock = lock
        @lock_decorator()
        def test_method(self):
            print("Class2: %s" % self._callback_lock)

    class Class3:
        @lock_decorator(lock=threading.Lock())
        def test_method(self):
            print("Class3: %s" % lock)

    class1 = Class1()

# Generated at 2022-06-13 16:43:05.872698
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    _lock = threading.Lock()

    class A(object):

        def __init__(self):
            self._var = 0
            self._lock = _lock

        @lock_decorator(lock=_lock)
        def _protected_method(self, value):
            self._var = value

        @lock_decorator(attr='_lock')
        def _protected_method2(self, value):
            self._var = value

    a = A()

    # Threading lock
    a._protected_method('Threading lock')
    assert(a._var == 'Threading lock')

    # Attr lock
    a._protected_method2('Attribute lock')
    assert(a._var == 'Attribute lock')


# Generated at 2022-06-13 16:43:11.033615
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._value = 0

        @lock_decorator(attr='_lock')
        def change_value(self, value):
            self._value = value

    foo = Foo()
    assert foo._value == 0
    foo.change_value(1)
    assert foo._value == 1
    foo.change_value(2)
    assert foo._value == 2

# Generated at 2022-06-13 16:43:19.167698
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    class Test(object):
        def __init__(self):
            self.lock = lock

        @lock_decorator(attr='lock')
        def test(self):
            return True

    t = Test()
    res = []
    for _ in range(20):
        t1 = threading.Thread(target=lambda: res.append(t.test()))
        t1.start()

    for _ in res:
        lock.acquire()
        lock.release()

    assert all(res)

# Generated at 2022-06-13 16:43:24.735884
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import multiprocessing

    # This is required for python2/3 compatibility
    from whichcraft import which

    class TestClass(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator()
        def missing_lock_attr(self):
            return 1

        def missing_lock_kwarg(self):
            return 2

        @lock_decorator(lock=self._lock)
        def use_existing_instance_attr(self):
            return 3

        @lock_decorator()
        def create_lock_attr(self):
            if not hasattr(self, '_call_lock'):
                self._call_lock = threading.Lock()
            return 4


# Generated at 2022-06-13 16:43:29.371226
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Blah(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.x = 0

        @lock_decorator(attr='_callback_lock')
        def add_one(self):
            self.x += 1

    b = Blah()
    b.add_one()
    assert b.x == 1

# Generated at 2022-06-13 16:44:15.993629
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    @lock_decorator(lock=lock)
    def send_callback_1(a, b, c):
        # simple dummy function
        return (a, b, c)
    assert send_callback_1(1, 2, 3) == (1, 2, 3)

    @lock_decorator(attr='_callback_lock')
    def send_callback_2(a, b, c):
        # simple dummy function
        return (a, b, c)

    class Test(object):
        _callback_lock = lock
        def __init__(self):
            self.i = 0

        def test_lock(self):
            self.i = self.i + 1
            send_callback_1(1, 2, 3)
            send_callback_2

# Generated at 2022-06-13 16:44:26.767747
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import sys
    class A:
        count = 0
        lock = threading.Lock()
        @lock_decorator(attr='lock')
        def func(self):
            self.count += 1
            return self.count
    class B:
        count = 0
        def func(self):
            self.count += 1
            return self.count
    class C:
        count = 0
        @lock_decorator(lock=threading.Lock())
        def func(self):
            self.count += 1
            return self.count
    # Python3 has threading.main_thread()
    # For Python2 threading.currentThread() is the main thread
    # threading.currentThread is a function
    # The main thread is the one that starts other threads
    main_thread = threading.current

# Generated at 2022-06-13 16:44:37.841660
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class Test:
        def __init__(self):
            self._counter = 0
            self._counter_lock = threading.Lock()
            self._second_counter = 0
            self._second_counter_lock = threading.Lock()
            self._third_counter = 0
            self._third_counter_lock = threading.Lock()
            self._threads = []

        @lock_decorator(attr='_counter_lock')
        def increment_counter(self, value=1):
            self._counter += value
            return self._counter

        @lock_decorator(lock=self._second_counter_lock)
        def increment_second_counter(self, value=1):
            self._second_counter += value
            return self._second_counter


# Generated at 2022-06-13 16:44:43.490428
# Unit test for function lock_decorator
def test_lock_decorator():
    class Tester(object):
        TEST_ATTR = '_callback_lock'

        def __init__(self):
            setattr(self, Tester.TEST_ATTR, threading.Lock())

        @lock_decorator(attr=TEST_ATTR)
        def test_attr_method(self):
            return True

        @lock_decorator(lock=threading.Lock())
        def test_lock_method(self):
            return True

    t = Tester()
    assert t.test_attr_method()
    assert t.test_lock_method()

# Generated at 2022-06-13 16:44:53.562128
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    class Example(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self._callback_calls = 0

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            time.sleep(0.2)
            self._callback_calls += 1



    # Calling send_callback from main thread, 2 times.
    e = Example()
    e.send_callback()
    e.send_callback()
    assert e._callback_calls == 2

    # Calling send_callback from a different thread, 5 times.
    def run_thread(e):
        for i in range(5):
            e.send_callback()


# Generated at 2022-06-13 16:45:03.175368
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Unit test for function lock_decorator'''

    import threading

    class TestClass:
        '''Test class for function lock_decorator'''

        def __init__(self):
            self.counter = 0
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def increment_counter(self):
            self.counter = self.counter + 1

    obj = TestClass()

    # Test that method works correctly with one thread
    obj.increment_counter()
    assert obj.counter == 1

    # Test that method works correctly with two threads
    def run():
        '''Helper function for threading'''
        obj.increment_counter()

    thread1 = threading.Thread(target=run)

# Generated at 2022-06-13 16:45:11.215924
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        from threading import Lock
        lock = Lock()
    except ImportError:
        return
    class A(object):
        def __init__(self):
            self._lock = lock
            self.calls = []

        @lock_decorator(attr='_lock')
        def method(self):
            self.calls.append(True)

        @lock_decorator(lock=lock)
        def method2(self):
            self.calls.append(True)

    a = A()
    a.method()
    a.method2()
    assert len(a.calls) == 2

# Generated at 2022-06-13 16:45:20.126501
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def foo():
        import time
        time.sleep(1)

    @lock_decorator()
    def bar():
        assert False, 'This should not be reached'

    def run():
        foo()

    # Run foo() in a subthread
    thread = threading.Thread(target=run)
    thread.start()

    # Wait long enough that foo() is blocked in its sleep
    # and then try to run bar()
    import time
    time.sleep(0.5)
    ret = bar()
    assert ret is None, 'bar() should have returned None'

    thread.join()

# Generated at 2022-06-13 16:45:28.296878
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading
    class TestLockDecorator(unittest.TestCase):
        def setUp(self):
            self.lock = threading.Lock()
            self.shared = []
            self.n = 1 << 10  # 10k
        def test_lock(self):
            class TestLock(object):
                lock = self.lock
                @lock_decorator(lock=lock)
                def append(self, value):
                    self.shared.append(value)
            for i in range(self.n):
                TestLock().append(i)
            self.assertEqual(len(self.shared), self.n)

# Generated at 2022-06-13 16:45:36.628859
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    import threading
    PY3 = sys.version_info[0] == 3
    if PY3:
        from contextlib import ExitStack
    else:
        from contextlib2 import ExitStack

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._shared = 0

        @lock_decorator(attr='_lock')
        def method1(self):
            self._shared += 1

        @lock_decorator(lock=threading.Lock())
        def method2(self):
            self._shared += 1

    def run():
        with ExitStack() as stack:
            for _ in range(0, 20):
                stack.enter_context(threading.Thread(target=t.method1))