

# Generated at 2022-06-13 16:35:57.697061
# Unit test for function lock_decorator
def test_lock_decorator():
    import random
    import threading
    class Foo:
        _lock = None
        def __init__(self):
            self._lock = threading.Lock()
            self._counter = 0

        def __str__(self):
            return str(self._counter)

        @lock_decorator(attr='_lock')
        def add(self):
            self._counter += 1
            return self._counter

    def add(foo):
        foo.add()

    def random_add(foo, max_count):
        thread_counter = 0
        while thread_counter < max_count:
            if thread_counter == random.randint(0, max_count):
                thread_counter += 1
            foo.add()

    foo = Foo()
    threads = []
    for i in range(10):
        thread = threading

# Generated at 2022-06-13 16:36:07.785735
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    # Define a dummy class that contains a callback and a method
    class Foo:
        def __init__(self, callback=None):
            self._callback = callback
            self._my_lock = threading.Lock()
            self.x = 0

        @lock_decorator(attr='_my_lock')
        def increment(self):
            self.x += 1

        @lock_decorator('_my_lock')
        def decrement(self):
            self.x -= 1

        @lock_decorator(lock=threading.Lock())
        def increment_and_call(slf):
            slf.x += 1
            if callable(slf._callback):
                slf._callback()

    # Create an instance, with a callback
    cb_called = [False]
   

# Generated at 2022-06-13 16:36:19.271274
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    test_lock = threading.Lock()
    # Test with explicit lock
    @lock_decorator(lock=test_lock)
    def some_method(arg):
        return arg

    # Test with lock from instance attr
    class Thing:
        def __init__(self):
            self._callback_lock = test_lock

        @lock_decorator(attr='_callback_lock')
        def some_method(self, arg):
            return arg

    # Assert if the lock is not acquired, then an exception is thrown
    try:
        some_method(True)
    except RuntimeError as e:
        assert 'cannot release un-acquired lock' in str(e)

    # If the lock is acquired the method returns the argument

# Generated at 2022-06-13 16:36:26.794791
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread
    from Queue import Queue
    from time import sleep
    class TestThreading(object):

        def __init__(self, n):
            self.n = n
            self.q = Queue()
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def add_to_q(self):
            # Without the use of the lock,
            # we could get unexpected additions
            sleep(0.01)
            self.q.put(self.n)

        @lock_decorator(attr='lock')
        def get_q(self):
            sleep(0.01)
            return self.q.get()


# Generated at 2022-06-13 16:36:36.881945
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Bar(object):
        counter = 0
        lock = threading.Lock()

        @lock_decorator(attr='lock')
        def increment(self):
            time.sleep(0.1)
            self.counter += 1

        @lock_decorator(attr='lock')
        def decrement(self):
            time.sleep(0.1)
            self.counter -= 1

        @lock_decorator(lock=threading.Lock())
        def set(self, value):
            time.sleep(0.1)
            self.counter = value

    # Define a function to use as a closure to pass to threading.Thread
    def run_thread(foo):
        for i in range(0, 100):
            foo.increment()

    # Define some instances

# Generated at 2022-06-13 16:36:46.044951
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Event, Thread

    class TestObject(object):
        def __init__(self):
            self.counter = 0
            self.lock = Lock()

        @lock_decorator(attr='lock')
        def inc(self):
            self.counter += 1

    t = TestObject()
    e = Event()
    def tt():
        while not e.wait(0):
            t.inc()
    t1 = Thread(target=tt)
    t2 = Thread(target=tt)
    t3 = Thread(target=tt)
    t1.start()
    t2.start()
    t3.start()
    import time
    time.sleep(5)
    e.set()
    assert t.counter == 15, t.counter

# Generated at 2022-06-13 16:36:55.159816
# Unit test for function lock_decorator
def test_lock_decorator():
    def _test_no_lock(self, a, b, c=None, d=None, e=None):
        return (a, b, c, d, e)

    def _test_lock(self, a, b, c=None, d=None, e=None):
        return (a, b, c, d, e)

    def _test_no_lock_no_self(a, b, c=None, d=None, e=None):
        return (a, b, c, d, e)

    def _test_lock_no_self(a, b, c=None, d=None, e=None):
        return (a, b, c, d, e)

    class TestClass(object):
        def __init__(self):
            self._lock = threading.Lock()


# Generated at 2022-06-13 16:37:03.435793
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self.x = 0
            self.lock = threading.Lock()

        @lock_decorator(lock=self.lock)
        def add_one(self):
            self.x += 1

        @lock_decorator(attr='lock')
        def add_two(self):
            self.x += 2

    t = Test()
    t.add_one()
    assert t.x == 1
    t.add_two()
    assert t.x == 3

# Generated at 2022-06-13 16:37:13.672256
# Unit test for function lock_decorator
def test_lock_decorator():

    import sys
    import threading

    # Simulate import of ansible module_utils
    class MyAnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.called = False
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def test_method(self, *args, **kwargs):
            self.called = True

        @lock_decorator(lock=threading.Lock())
        def test_method2(self, *args, **kwargs):
            self.called = True

    sys.modules['ansible'] = MyAnsibleModule()

if __name__ == '__main__':
    test_lock_decorator()

# Generated at 2022-06-13 16:37:23.398537
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test:
        def __init__(self):
            setattr(self, 'lock_attr', threading.Lock())
            self.count = 0

        @lock_decorator(attr='lock_attr')
        def method(self):
            time.sleep(.25)
            self.count += 1

    t = Test()
    assert t.count == 0
    t1 = threading.Thread(target=t.method)
    t2 = threading.Thread(target=t.method)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    assert t.count == 2

# Generated at 2022-06-13 16:37:37.300326
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Unit test for function lock_decorator'''

    import threading

    def mutable_dict(value=None):
        '''Function to control when a decorator is used

        :kwarg value: value to return when used to test lock_decorator
        '''
        _d = dict()


# Generated at 2022-06-13 16:37:45.958177
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import inspect
    import time

    class Test(object):
        @lock_decorator(attr='lock')
        def method(self):
            self.method_called += 1
            time.sleep(0.2)

        def __init__(self):
            self.lock = threading.Lock()
            self.method_called = 0

    t = Test()
    for x in range(12):
        t.method()
    assert t.method_called, 12
    assert inspect.getargspec(t.method).args[0] == 'self'

    class Test2(object):
        @lock_decorator(lock=threading.Lock())
        def method(self):
            self.method_called += 1
            time.sleep(0.2)


# Generated at 2022-06-13 16:37:54.823686
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    global lock_used
    lock_used = False
    def assert_locking_works(func):
        @wraps(func)
        def inner(*args, **kwargs):
            global lock_used
            lock_used = True
            assert lock.locked()
            return func(*args, **kwargs)
        return inner
    try:
        @lock_decorator(lock=lock)
        @assert_locking_works
        def test_lock_decorator_with_explicit_lock():
            pass
        with lock:
            test_lock_decorator_with_explicit_lock()
        assert lock_used
    finally:
        del lock_used

# Generated at 2022-06-13 16:38:03.912374
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread
    from time import sleep
    
    class Test():
        def __init__(self, sleep_time=2):
            self._lock = Lock()
            self.sleep_time = sleep_time

        @lock_decorator(attr='_lock')
        def my_method(self, text):
            print(text, end='')
            sleep(self.sleep_time)
            print('[DONE]')

        def my_method_decorator(self, text):
            self.my_method(text)
            
    #create an array of threads
    class Th():
        def __init__(self, target, text):
            self.thread = Thread(target=target, args=(text,))

        def start(self):
            self.thread.start()


# Generated at 2022-06-13 16:38:12.540886
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    Unit test function for function lock_decorator
    '''
    import threading

    class Example:
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def example(self):
            self.a = 10

        @lock_decorator(lock=threading.Lock())
        def example2(self):
            self.b = 20

    # Test to ensure the lock_decorator is working.
    # Both ``a`` and ``b`` should be ``10``.
    # If the decorator is NOT working, then ``b`` will be ``20``.
    test_obj = Example()
    t1 = threading.Thread(target=test_obj.example)

# Generated at 2022-06-13 16:38:19.954348
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class ExampleClass:

        def __init__(self):
            # Lock implemented as an instance attribute
            self._lock = threading.Lock()
            # Shared counter across threads
            self.counter = 0

        @lock_decorator(attr='_lock')
        def incr(self):
            self.counter += 1

        @lock_decorator(lock=threading.Lock())
        def add(self, n):
            self.counter += n

    e = ExampleClass()

    def worker(n):
        for _ in range(n):
            e.incr()
            e.add(1)

    threads = []
    for _ in range(1000):
        t = threading.Thread(target=worker, args=(10,), daemon=True)
        t.start()


# Generated at 2022-06-13 16:38:24.156367
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def foo(self):
            return True

    foo = Foo()

    assert foo.foo() == True

# Generated at 2022-06-13 16:38:33.026715
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TargetClass(object):
        def __init__(self):
            self.foo = None
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def unsafe_set_foo(self, value):
            self.foo = value

    tc = TargetClass()
    assert tc is not None

    import time

    def run_thread():
        time.sleep(0.2)
        tc.unsafe_set_foo(True)

    thread = threading.Thread(target=run_thread)
    thread.start()
    tc.unsafe_set_foo(False)
    thread.join()
    assert tc.foo is True



# Generated at 2022-06-13 16:38:37.470380
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class LockObject(object):
        lock = threading.Lock()

    lock_obj = LockObject()

    @lock_decorator(lock=lock_obj.lock)
    def f_decorator(a, b, c):
        return a + b + c

    with lock_obj.lock:
        assert f_decorator(1, 2, 3) == 6



# Generated at 2022-06-13 16:38:45.508337
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import random

    class Foo:
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def bar(self):
            time.sleep(random.randint(0,3))
            print('bar')

    foo = Foo()
    threads = []
    for _ in range(5):
        t = threading.Thread(target=foo.bar)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

# Generated at 2022-06-13 16:38:54.187429
# Unit test for function lock_decorator
def test_lock_decorator():
    '''The purpose of this unit test is to just demonstrate
    the functionality of the ``lock_decorator`` function.

    Proper testing of this decorator should be done in each
    module that uses it.
    '''

    import threading
    import time

    class Caller(object):
        def __init__(self):
            self.value = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def increment(self):
            self.value += 1

    c = Caller()

    assert c.value == 0
    c.increment()
    assert c.value == 1

    start = time.time()
    threads = []
    while time.time() - start < 1:
        t = threading.Thread(target=c.increment)
        t.start()


# Generated at 2022-06-13 16:39:04.937822
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestLock(object):
        def __init__(self):
            self._attr_lock = threading.Lock()
            self._explicit_lock = threading.Lock()

        @lock_decorator(attr='_attr_lock')
        def attr_lock(self):
            # in fact, verify that we hold the lock
            assert self._attr_lock.locked()

        @lock_decorator(lock=self._explicit_lock)
        def explicit_lock(self):
            assert self._explicit_lock.locked()

    # run once, for real
    test = TestLock()
    test.attr_lock()
    test.explicit_lock()

    # now, launch another thread that will try to do the same thing
    def lock_tester():
        test.attr_lock

# Generated at 2022-06-13 16:39:15.433790
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Foo(object):
        @lock_decorator(attr='_lock')
        def lock(self):
            self.lock_count += 1

    foo = Foo()
    foo._lock = threading.Lock()

    foo.lock_count = 0
    foo.lock()
    assert foo.lock_count == 1

    foo.lock()
    assert foo.lock_count == 2

    class Bar(object):
        @lock_decorator(lock=threading.Lock())
        def lock2(self):
            self.lock2_count += 1

    bar = Bar()
    bar.lock2_count = 0
    bar.lock2()
    assert bar.lock2_count == 1

    bar.lock2()
    assert bar.lock2_count == 2


# Generated at 2022-06-13 16:39:24.437755
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):

        def __init__(self, *args, **kwargs):
            self._test_lock = threading.Lock()
            self._test_data = []

        @lock_decorator(attr='_test_lock')
        def append_data(self, data, *args, **kwargs):
            self._test_data.append(data)

        @property
        def data(self):
            return self._test_data

    t = Test()
    t.append_data('foo')
    assert len(t.data) == 1
    assert t.data[0] == 'foo'

    t.append_data('bar')
    assert len(t.data) == 2
    assert t.data[1] == 'bar'

# Generated at 2022-06-13 16:39:34.053866
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from threading import Lock
    from types import ModuleType

    # Dummy self
    class AnsibleExecutor(object):
        def __init__(self):
            self.module_lock = Lock()

    # Create a mock module object
    module = ModuleType(__name__)
    module.AnsibleExecutor = AnsibleExecutor

    @lock_decorator(attr='module_lock')
    def test_lock_decorator_add(self, a, b):
        return a + b

    # Create an AnsibleExecutor and lock the results
    ae = AnsibleExecutor()
    ae.add = test_lock_decorator_add
    results = ae.add(1, 2)
    assert results == 3

    # Create a new AnsibleExecutor, use a lock from

# Generated at 2022-06-13 16:39:35.161803
# Unit test for function lock_decorator
def test_lock_decorator():
    # No functional tests (yet)
    assert True

# Generated at 2022-06-13 16:39:43.606724
# Unit test for function lock_decorator
def test_lock_decorator():
    from collections import defaultdict
    from threading import Event, Thread

    class Foo(object):
        def __init__(self):
            self._lock = Event()
            self._lock.set()
            self._counts = defaultdict(int)

        @lock_decorator(attr='_lock')
        def _count(self, name):
            self._counts[name] += 1

        def _count_thread(self, name, wait_event):
            wait_event.wait()
            self._count(name)

        def _count_thread2(self, name, wait_event):
            wait_event.wait()
            self._count(name)

        def _count_thread3(self, name, wait_event):
            wait_event.wait()
            self._lock.clear()

# Generated at 2022-06-13 16:39:52.850995
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self.attr_lock = threading.Lock()
            self.lock_lock = threading.Lock()

        @lock_decorator()
        def missing_lock(self):
            return True

        @lock_decorator(attr='attr_lock')
        def attr(self):
            return True

        @lock_decorator(lock=threading.Lock())
        def lock(self):
            return True

    obj = Test()
    assert obj.missing_lock()
    assert obj.attr()
    assert obj.lock()

# Generated at 2022-06-13 16:40:01.729821
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    import threading

    l = threading.Lock()
    if sys.version_info[0] == 2:
        lock_decorator = wraps(lock_decorator)(lock_decorator)
    @lock_decorator(lock=l)
    def f(i, j):
        return i + j
    @lock_decorator(attr='l')
    def g(self, i, j):
        return i + j
    class H:
        l = l
        @lock_decorator(attr='l')
        def h(self, i, j):
            return i + j
    assert f(1, 2) == 3
    assert g(H(), 1, 2) == 3
    assert H().h(1, 2) == 3

# Generated at 2022-06-13 16:40:10.891780
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()

    class Foo:
        @lock_decorator(attr='_lock', lock=lock)
        def bar1(self, *args, **kwargs):
            return args, kwargs

        @lock_decorator(lock=lock)
        def bar2(self, *args, **kwargs):
            return args, kwargs

    f = Foo()

    assert {
        'bar1': f.bar1, 'bar2': f.bar2
    } == {
        'bar1': lock_decorator(attr='_lock', lock=lock)(Foo.bar1),
        'bar2': lock_decorator(lock=lock)(Foo.bar2),
    }



# Generated at 2022-06-13 16:40:28.800118
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread
    from time import sleep

    class Test(object):
        def __init__(self):
            self._lock = 0
            self._mock_thread = None

        @lock_decorator(attr='_lock')
        def my_test(self):
            print('entered lock')
            sleep(0.1)
            print('exited lock')

        def start(self):
            self._mock_thread = Thread(target=self.my_test)
            self._mock_thread.start()

        def join(self):
            self._mock_thread.join()

    class TestWithExplicitLock(object):
        def __init__(self):
            self._lock = 0
            self._mock_thread = None
            # By assigning this here, we can prove that we aren't

# Generated at 2022-06-13 16:40:39.989719
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread
    from time import sleep

    # Reference counter
    counter = 0

    # Lock to protect counter
    lock = Lock()

    def increment(count):
        '''increment counter by count'''
        global counter, lock

        # Acquire lock to protect access to counter
        lock.acquire()

        # Increase counter value
        counter += count

        # Release lock
        lock.release()

    # Create decorator with lock
    decorator = lock_decorator(lock=lock)

    # Wrap the method to protect access to lock
    increment_with_lock = decorator(increment)

    # Create two threads
    t1 = Thread(target=increment_with_lock, args=(1,))
    t2 = Thread(target=increment_with_lock, args=(100,))

   

# Generated at 2022-06-13 16:40:43.755100
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo(object):
        name = None
        _lock = None

        def __init__(self, name):
            self.name = name
            self._lock = lock_decorator(attr='_lock')

        @_lock
        def set_name(self, name):
            self.name = name

    a = Foo('a')
    assert a.name == 'a'
    a.set_name('b')
    assert a.name == 'b'

# Generated at 2022-06-13 16:40:53.296032
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread

    class TestClass(object):
        def __init__(self):
            self._test_lock = lock_decorator(attr='_lock')

    class TestRunner(object):
        def __init__(self):
            self.test_object = TestClass()
            self.threads = []

        def start_test(self):
            # Create thread and start async
            t = Thread(target=self.test_object._test_lock(self.test_object.test_method))
            t.start()
            self.threads.append(t)

        def join(self):
            # Wait for all threads to finish
            for t in self.threads:
                t.join()

    # Create the class to test and instantiate the test runner

# Generated at 2022-06-13 16:41:02.758436
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Someclass(object):

        def __init__(self):
            self._callback_lock = threading.Lock()
            self.some_list = []

        @lock_decorator(attr='_callback_lock')
        def callback1(self, some_str):
            self.some_list.append(some_str)

        @lock_decorator(lock=threading.Lock())
        def callback2(self, some_str):
            self.some_list.append(some_str)

    @lock_decorator(lock=threading.Lock())
    def callback3(some_str):
        some_obj.some_list.append(some_str)

    some_obj = Someclass()

    some_obj.callback1('some_str')
    assert some_obj.some

# Generated at 2022-06-13 16:41:10.102002
# Unit test for function lock_decorator
def test_lock_decorator():
    class Test(object):  # noqa
        def __init__(self):
            self.lock = lock

        @lock_decorator(lock=lock)
        def foo(self):
            return 'foo'

        @lock_decorator(attr='lock')
        def bar(self):
            return 'bar'

    lock = threading.Lock()
    t = Test()
    assert t.foo() == 'foo'
    assert t.bar() == 'bar'

# Generated at 2022-06-13 16:41:14.489147
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def foo(self):
            # returns None
            pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-13 16:41:25.472299
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test(object):
        def __init__(self):
            self.value = None
            self.attr = '_lock'
            self.lock = threading.Lock()

        @lock_decorator(attr=attr)
        def first(self, value):
            self.value = value

        @lock_decorator(lock=self.lock)
        def second(self, value):
            self.value = value

    class OneThread(threading.Thread):
        def __init__(self, test, value):
            threading.Thread.__init__(self)
            self.test = test
            self.value = value

        def run(self):
            self.test.first(self.value)


# Generated at 2022-06-13 16:41:36.201104
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestClass:

        _lock = threading.Lock()
        _results = []

        def __init__(self):
            self._results = []

        def add_result(self, result):
            self._results.append(result)

        @lock_decorator(attr='_lock')
        def no_lock(self, result):
            self.add_result(result)
            time.sleep(1)

    tc = TestClass()

    # Start 10 threads that should each run immediately after the
    # previous thread starts
    threads = []
    for i in range(10):
        t = threading.Thread(target=tc.no_lock, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# Generated at 2022-06-13 16:41:42.803893
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading
    import random
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.data = []
        @lock_decorator(attr='_lock')
        def append(self, el):
            self.data.append(el)
    l = Test()
    for _ in range(4):
        t = threading.Thread(target=l.append, args=(random.randint(1, 100),))
        t.daemon = True
        t.start()
        time.sleep(.1)
    assert len(l.data) == 4

# Generated at 2022-06-13 16:42:05.336352
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        def __init__(self):
            self.counter = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def test_method(self):
            self.counter += 1

        @lock_decorator(lock=threading.Lock())
        def test_method_2(self):
            self.counter += 2

        @lock_decorator(lock=self.lock)
        def test_method_3(self):
            self.counter += 3

    test = Test()
    threads = []
    for i in range(100):
        threads.append(threading.Thread(target=test.test_method))
        threads.append(threading.Thread(target=test.test_method_2))
        threads.append

# Generated at 2022-06-13 16:42:16.380502
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        from unittest import mock
    except ImportError:  # pragma: no cover
        # Python 2
        import mock

    # This will fail if the decorator does not function properly
    @lock_decorator(attr='_callback_lock')
    def send_callback(self, url, data):
        '''Send the callback'''

    mock_request = mock.Mock()
    mock_obj = mock.Mock()
    mock_obj.__name__ = 'SomeObject'
    mock_obj.__module__ = 'test_lock_decorator'
    mock_obj.send_callback.__doc__ = 'Send the callback'
    mock_obj.send_callback.__name__ = 'send_callback'

# Generated at 2022-06-13 16:42:24.792697
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestClass(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self._callback_count = 0
            self._callback_last_time = 0

        @lock_decorator(attr='_callback_lock')
        def add_callback(self, value):
            # Increment the count
            self._callback_count += 1
            # Update last time
            self._callback_last_time = time.time()

    class TestClassWithLock(TestClass):
        def __init__(self):
            super(TestClassWithLock, self).__init__()
            self._callback_lock = threading.Lock()


# Generated at 2022-06-13 16:42:34.521857
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from ansible_collections.ansible.netcommon.tests.unit.compat.mock import Mock

    class FakeTestObject(object):

        @lock_decorator(attr='_lock')
        def foo(self):
            self.some_attr = 'bar'

        @lock_decorator(lock=threading.Lock())
        def bar(self):
            self.some_attr = 'baz'

    obj = FakeTestObject()
    obj._lock = threading.Lock()

    thread1 = threading.Thread(target=obj.foo)
    thread2 = threading.Thread(target=obj.foo)
    thread3 = threading.Thread(target=obj.bar)
    thread4 = threading.Thread(target=obj.bar)

    thread1.start()
    thread

# Generated at 2022-06-13 16:42:45.407405
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading
    class LockTests(unittest.TestCase):
        class TestClass(object):
            def __init__(self):
                self._callback_lock = threading.Lock()

            @lock_decorator(attr='_callback_lock')
            def send_callback(self):
                return True

            @lock_decorator(lock=threading.Lock())
            def some_method(self):
                return True

        def test_class_attr(self):
            test_obj = self.TestClass()
            self.assertEqual(test_obj.send_callback(), True)

        def test_passed_lock(self):
            test_obj = self.TestClass()
            self.assertEqual(test_obj.some_method(), True)

    tests = unitt

# Generated at 2022-06-13 16:42:57.819779
# Unit test for function lock_decorator
def test_lock_decorator():
    # The code below does not really test the lock object, just
    # that it was called with the correct parameters.

    import threading

    class Test(object):
        def __init__(self):
            self.test_lock_decorator_lock = threading.Lock()

        @lock_decorator(attr='test_lock_decorator_lock')
        def _test(self):
            self.test_value = 'locked'

    test = Test()
    test.test_value = 'not-locked'

    test._test()
    assert test.test_value == 'locked'

    class TestNoAttr(object):
        def __init__(self):
            self.test_lock_decorator_lock = threading.Lock()


# Generated at 2022-06-13 16:43:06.068599
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    num_threads = 3

    # Some global resources
    global_list = []
    global_list_lock = threading.Lock()

    # A bucket - lock mode
    class Bucket():
        def __init__(self):
            self.value = 0
            self.value_lock = threading.Lock()

        @lock_decorator(attr='value_lock')
        def put(self, n):
            time.sleep(.5)
            self.value += n

        @lock_decorator(attr='value_lock')
        def get(self, n):
            time.sleep(.5)
            self.value -= n

        def get_value(self):
            with self.value_lock:
                return self.value

    # A bucket - explicit lock mode
   

# Generated at 2022-06-13 16:43:13.494582
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        '''This class is used to demonstrate the use of the
        lock_decorator.
        '''
        def __init__(self):
            self.lock1 = threading.Lock()
            self.lock2 = threading.Lock()
            self.lock3 = threading.Lock()
            self.lock4 = threading.Lock()

        @lock_decorator(attr='lock1')
        def method1(self, value):
            '''This method uses the ``attr`` arg to define the lock'''
            return value

        @lock_decorator(lock=self.lock2)
        def method2(self, value):
            '''This method uses the ``lock`` arg to define the lock'''
            return value


# Generated at 2022-06-13 16:43:22.756981
# Unit test for function lock_decorator
def test_lock_decorator():

    import sys
    if sys.version_info < (3, 3):
        import threading
        # example with lock attribute
        class Foo(object):
            def __init__(self):
                self._lock = threading.Lock()

            @lock_decorator(attr='_lock')
            def method(self):
                print('in method')

        foo = Foo()
        foo.method()
        # example with global lock
        _lock = threading.Lock()

        @lock_decorator(lock=_lock)
        def method2():
            print('in method2')

        method2()
    else:
        import unittest


# Generated at 2022-06-13 16:43:28.644004
# Unit test for function lock_decorator
def test_lock_decorator():
    class TestClass:
        def __init__(self, lock):
            self.lock = lock
            self.count = 0
        @lock_decorator(attr='lock')
        def incr(self):
            self.count += 1
    import threading
    lock = threading.Lock()
    tst = TestClass(lock)
    assert tst.count == 0
    tst.incr()
    assert tst.count == 1

# Generated at 2022-06-13 16:44:14.919537
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    class MyClass(object):
        def __init__(self, lock=None):
            if lock is None:
                self._lock = threading.Lock()
            else:
                self._lock = lock

        @lock_decorator(attr='_lock')
        def my_method(self, wrapper=False):
            if wrapper:
                time.sleep(1)
            return id(self._lock)

        @lock_decorator(lock=threading.Lock())
        def my_other_method(self, wrapper=False):
            if wrapper:
                time.sleep(1)
            return id(self._lock)

    t1 = threading.Thread(target=MyClass, args=().my_method, kwargs={'wrapper': True})

# Generated at 2022-06-13 16:44:18.338646
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class LockTest(object):
        def __init__(self):
            self._my_lock = threading.Lock()

        @lock_decorator(attr='_my_lock')
        def check_lock(self):
            self.assertTrue(self._my_lock.locked())

        @lock_decorator(lock=threading.Lock())
        def check_lock_2(self):
            pass
    LockTest().check_lock()
    LockTest().check_lock_2()

# Generated at 2022-06-13 16:44:30.365892
# Unit test for function lock_decorator
def test_lock_decorator():
    # Create a dummy lock with a list as a queue
    lock = []
    def _lock():
        lock.append(0)
    def _unlock():
        lock.pop()

    class Test(object):
        '''Simple class that represents an object to test the ``lock_decorator``
        decorator.
        '''
        def __init__(self, use_attr=False, use_lock=False, **kwargs):
            if not use_attr and not use_lock:
                raise ValueError('Need either `use_attr` or `use_lock` to be true')
            self.use_attr = use_attr
            self.use_lock = use_lock
            self.kwargs = kwargs
            self.lock = []


# Generated at 2022-06-13 16:44:37.990976
# Unit test for function lock_decorator
def test_lock_decorator():
    class Test(object):
        def __init__(self):
            self._lock = True

        @lock_decorator(attr='_lock')
        def test(self):
            self._lock = True

    a = Test()
    a.test()

    class Test(object):
        @lock_decorator(lock=True)
        def test(self):
            pass

    a = Test()
    a.test()

    class Test(object):
        @lock_decorator()
        def test(self):
            pass

    a = Test()
    a.test()

# Generated at 2022-06-13 16:44:45.406381
# Unit test for function lock_decorator
def test_lock_decorator():
    class SomeClass(object):
        def __init__(self):
            self._lock = self._lock1 = threading.Lock()
            self._lock2 = threading.Lock()

        @lock_decorator(lock=self._lock2)
        def some_method(self):
            pass
    import unittest
    import threading

    class SomeTestCase(unittest.TestCase):
        def test_class_method_lock_from_instance(self):
            some_class = SomeClass()
            getattr(SomeClass, 'some_method')(some_class)
            # `some_class._lock2` is locked:
            self.assertTrue(some_class._lock2.locked())
            # `some_class._lock` is unlocked:
            self.assertFalse(some_class._lock.locked())

# Generated at 2022-06-13 16:44:56.137362
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._test_value = 0

        @lock_decorator()
        def set_value(self, value):
            self._test_value = value

        @lock_decorator(lock=self._lock)
        def get_value(self):
            return self._test_value

        @lock_decorator(attr='_lock')
        def get_lock(self):
            return self._lock

    t = Test()

    t.set_value(42)
    assert t.get_value() == 42
    assert t.get_lock().locked()


# Generated at 2022-06-13 16:45:04.560630
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    class TestClass(object):
        def __init__(self):
            # Lock is class level to ensure that threads
            # that are created in the test case, share
            # the same lock.
            self._lock = threading.Lock()

            # A list that is used to determine the order
            # the threads completed in.
            self._completed = []

        @lock_decorator(attr='_lock')
        def append_one(self):
            time.sleep(.5)
            self._completed.append(1)

        @lock_decorator(attr='_lock')
        def append_two(self):
            time.sleep(.5)
            self._completed.append(2)

    testclass = TestClass()

# Generated at 2022-06-13 16:45:13.305243
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass:
        def __init__(self):
            self._callback_lock = threading.Lock()
            self._callback_cnt = 0

        @lock_decorator(attr='_callback_lock')
        def callback(self, val):
            self._callback_cnt += val
            return self._callback_cnt

    c = TestClass()
    assert c.callback(1) == 1
    assert c.callback(1) == 2
    assert c.callback(1) == 3
    assert c.callback(1) == 4
    assert c.callback(1) == 5

    # Note that we're not using functions to test the lock object
    # version of the decorator because it would prevent the
    # references to the lock from being garbage collected.

# Generated at 2022-06-13 16:45:23.323670
# Unit test for function lock_decorator
def test_lock_decorator():
    class TestLockDecorator(object):
        def __init__(self):
            import threading
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def use_instance_attribute(self):
            return 'using instance attribute'

        @lock_decorator(lock=lock_decorator.test_lock)
        def use_explicit_lock(self):
            return 'using explicit lock'

        # This will have nothing changed, as there is no specified ``lock`` attribute
        @lock_decorator()
        def no_lock_specified(self):
            return 'no lock specified'

    import threading
    lock_decorator.test_lock = threading.Lock()
    test = TestLockDecorator()

    # Unit test for instance attribute
    assert test

# Generated at 2022-06-13 16:45:30.522457
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self._test_lock = threading.Lock()
            self.test_attr = 'test_attr'

        @lock_decorator(attr='_test_lock')
        def test_method(self):
            '''
            A generic test method for lock_decorator, with no extra
            parameters
            '''
            self.test_attr = self.test_attr + 'a'
            time.sleep(0.01)
            return self.test_attr

    class Test2(object):
        def __init__(self):
            self.test_attr = 'test_attr'
