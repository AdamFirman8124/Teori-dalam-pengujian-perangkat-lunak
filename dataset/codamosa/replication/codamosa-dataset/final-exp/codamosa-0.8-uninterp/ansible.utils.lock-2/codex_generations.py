

# Generated at 2022-06-13 16:36:02.712087
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    class Test(object):
        def __init__(self):
            self.l = threading.Lock()
            self.v = 0
        @lock_decorator(attr='l')
        def locked_method(self):
            self.v += 1
            time.sleep(1)
            self.v += 1
        @lock_decorator(lock=threading.Lock())
        def locked_method_2(self):
            self.v -= 1
            time.sleep(1)
            self.v -= 1
    test = Test()
    threads = []
    for _ in range(10):
        t = threading.Thread(target=test.locked_method)
        t.start()
        threads.append(t)

# Generated at 2022-06-13 16:36:06.740295
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    # Make sure it works with a class
    class A:
        def __init__(self):
            self.a = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def add(self, val):
            self.a += val
            return self.a

    a = A()
    assert a.add(1) == 1
    assert a.add(3) == 4

    # Make sure it works with a class method
    class B:
        @lock_decorator(
            attr='_lock'
        )
        def __init__(self):
            self.a = 0
            self._lock = threading.Lock()

        def add(self, val):
            self.a += val
            return self.a

    b = B

# Generated at 2022-06-13 16:36:18.063395
# Unit test for function lock_decorator
def test_lock_decorator():
    shutdown = False
    class NotAContextManager(object):
        def __init__(self):
            self.acquired = 0
        def __enter__(self):
            self.acquired += 1
            # Tests that in-progress locks are respected
            assert self.acquired == 1
        def __exit__(self, exc_type, exc_value, traceback):
            self.acquired -= 1
            # Tests that ``__exit__`` is called
            assert self.acquired == 0
    class NoLock(object): pass
    class Lock(object):
        def __init__(self):
            self.acquired = 0
        def __enter__(self):
            self.acquired += 1
            while shutdown: pass
            # Tests that in-progress locks are respected
            assert self.acquired == 1

# Generated at 2022-06-13 16:36:27.732319
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass(object):
        @lock_decorator()
        def missing_lock_attr(self):
            return 'missing_lock_attr'

        @lock_decorator(attr='_callback_lock')
        def callback_lock_attr(self):
            return 'callback_lock_attr'

        @lock_decorator(lock=threading.Lock())
        def callback_lock(self):
            return 'callback_lock'

    lock = threading.Lock()
    test1 = TestClass()
    test2 = TestClass()
    test2._callback_lock = lock

    # Test in a single thread / process
    assert test1.missing_lock_attr() == 'missing_lock_attr'
    assert test1.callback_lock_attr() == 'callback_lock_attr'
   

# Generated at 2022-06-13 16:36:37.423190
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import sys
    import threading
    import time

    mocked_threading = {
        'Event': mock.Mock(),
        'Lock': mock.Mock(),
        'Thread': None,
    }

    class MockedThread(object):
        called = []
        def __init__(self, *args, **kwargs):
            MockedThread.called.append(1)
            mocked_threading['Thread'].__init__(*args, **kwargs)


# Generated at 2022-06-13 16:36:46.603817
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except ImportError:
        return
    lock = threading.Lock()
    class Foo:
        _lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def bar(self, x):
            return x + 1
        @lock_decorator(lock=lock)
        def fizz(self, x):
            return x + 1
    foo = Foo()
    assert foo.bar(1) == 2
    assert foo.fizz(2) == 3
    x = 0
    def increase():
        nonlocal x
        with lock:
            x += 1
    # lock_decorator uses contextlib, so this is an atomic operation
    threads = []
    for i in range(100):
        t = threading.Thread(target=increase)

# Generated at 2022-06-13 16:36:53.109740
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Example(object):

        def __init__(self):
            self._lock_attr = threading.Lock()

        @lock_decorator(attr='_lock_attr')
        def foo(self):
            print('Running with lock from attribute on self')

        @lock_decorator(lock=threading.Lock())
        def bar(self):
            print('Running with lock passed as a parameter')

    test = Example()
    test.foo()
    test.bar()

# Generated at 2022-06-13 16:36:59.360239
# Unit test for function lock_decorator
def test_lock_decorator():

    import random
    import threading
    import time

    ret = []
    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def append_to_limited_list(x):
        for i in range(10):
            ret.append(x)
            time.sleep(0.1)

    def worker():
        append_to_limited_list(random.randint(1, 11))

    threads = []
    for x in range(50):
        threads.append(threading.Thread(target=worker))

    for x in threads:
        x.start()

    for x in threads:
        x.join()

    assert len(ret) == 500

# Generated at 2022-06-13 16:37:04.750083
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        from threading import Lock
    except ImportError:
        return
    class Foo(object):
        def __init__(self):
            self._my_lock = Lock()

        @lock_decorator(attr='_my_lock')
        def bar(self):
            assert self._my_lock.locked()

    foo = Foo()
    foo.bar()

    # TODO: Test with lock=

# Generated at 2022-06-13 16:37:14.791628
# Unit test for function lock_decorator
def test_lock_decorator():
    '''It's hard to unit test the lock_decorator.
    The test only tries to validate that ``lock_decorator`` doesn't
    raise any exceptions, and outputs the correct "decorated function"
    behavior.
    The next step of testing should be to try with a real, working
    lock object.
    '''
    import threading
    lock = threading.Lock()
    @lock_decorator(lock=lock)
    def lock_func(x, y):
        return x, y

    assert lock_func('a', 'b') == ('a', 'b')

    @lock_decorator(attr='fake')
    def lock_func_attr(self, x, y):
        return x, y

# Generated at 2022-06-13 16:37:25.879037
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    class TestLockedObj(object):
        def __init__(self):
            self._value = 0
            self._lock = threading.Lock()
            # Callback value and lock
            self._cb_value = None
            self._cb_lock = threading.Lock()
            # A lock to use with the decorator
            self._decorator_lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def update_value(self):
            time.sleep(1)
            self._value += 1
            self.send_callback()

        @lock_decorator()
        def send_callback(self):
            time.sleep(1)
            with self._cb_lock:
                self._cb_value = self._value


# Generated at 2022-06-13 16:37:37.801073
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()

    class dummy_obj(object):
        def __init__(self, lock=lock):
            self.my_lock = lock

        @lock_decorator(attr='my_lock')
        def dummy_method(self, wait=0.2):
            import time
            time.sleep(wait)

    a = dummy_obj()

    import time
    start = time.time()
    a.dummy_method()
    end = time.time()
    assert end - start > 0.2

    import random
    import itertools

    wait = 0.2
    start = time.time()

# Generated at 2022-06-13 16:37:46.350535
# Unit test for function lock_decorator
def test_lock_decorator():
    import os
    import sys
    import unittest

    from shutil import rmtree

    from contextlib import contextmanager
    from threading import Lock
    from tempfile import mkdtemp

    if sys.version_info[0] < 3 or sys.version_info[1] < 3:
        # The test below for ``lock_decorator`` uses context managers
        # in the implementation. Since context managers were only added
        # in python 3.3, this will not work in 2.x, so test the decorator
        # TODO: Remove this once we drop support for Python 2.x
        class TestLockDecorator(unittest.TestCase):
            def test_lock_decorator(self):
                # This test uses a custom context manager
                # to verify that the lock is being used
                lock = Lock()

               

# Generated at 2022-06-13 16:37:52.437193
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    attr = threading.Lock()
    lock = threading.Lock()
    increment_num = 0

    class A(object):
        def __init__(self):
            self.num = 0

        @lock_decorator(attr=attr)
        def increment(self):
            self.num += 1

        @lock_decorator(lock=lock)
        def increment(self):
            global increment_num
            increment_num += 1

test_lock_decorator()

# Generated at 2022-06-13 16:38:02.621178
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import concurrent.futures
    import time

    class SomeClass:
        def __init__(self):
            self._lock = threading.Lock()
            self.v = 0

        @lock_decorator()
        def some_method(self):
            self.v += 1

        @lock_decorator(lock=self._lock)
        def some_other_method(self):
            self.v -= 1

    obj = SomeClass()

    def test_one():
        obj.some_method()

    def test_two():
        obj.some_other_method()

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        for num in range(1, 10):
            executor.submit(test_one)

# Generated at 2022-06-13 16:38:07.954487
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except ImportError:
        raise AssertionError('can\'t run unit test without threading')
    lock = threading.Lock()
    class TestClass(object):
        def __init__(self):
            self.value = 0
            self.lock = lock
            self.values = []

        @lock_decorator('lock')
        def append(self, value):
            self.values.append(value)

    test = TestClass()
    test.append(1)
    assert(test.values == [1])
    test.append(2)
    assert(test.values == [1, 2])
    del test

# Generated at 2022-06-13 16:38:15.070170
# Unit test for function lock_decorator
def test_lock_decorator():
    # imports needed for this test
    import threading
    import time

    class TestClass(object):
        def __init__(self):
            self._attr = 0
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def locked_method(self, arg):
            # This function should always be called once
            self._attr += arg

    class TestClass2(object):
        def __init__(self):
            self._attr = 0
            self._lock = threading.Lock()

        @lock_decorator(lock=self._lock)
        def locked_method(self, arg):
            # This function should always be called once
            self._attr += arg

    # Create an instance of our test class.
    test_instance = TestClass()
    # Create the thread


# Generated at 2022-06-13 16:38:26.657828
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    lock = Lock()
    class TestLockDecorator(object):

        @lock_decorator(lock=lock)
        def test_dec(self):
            pass

        @lock_decorator(attr='lock')
        def test_dec_attr(self):
            pass

        def __init__(self):
            self.lock = Lock()

    t = TestLockDecorator()
    assert t.test_dec.__doc__ == 'Unit test for function lock_decorator'
    assert t.test_dec.__name__ == 'test_dec'
    assert t.test_dec_attr.__doc__ == 'Unit test for function lock_decorator'
    assert t.test_dec_attr.__name__ == 'test_dec_attr'



# Generated at 2022-06-13 16:38:31.049016
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Foo(object):
        @lock_decorator(lock=threading.Lock())
        def bar(self, val):
            return val
    assert not hasattr(Foo, 'bar_lock')
    foo = Foo()
    assert foo.bar(1) == 1

# Generated at 2022-06-13 16:38:37.776511
# Unit test for function lock_decorator
def test_lock_decorator():
    from collections import defaultdict
    from threading import Lock, Thread

    x = defaultdict(int)
    threads = []

    def fun(lock):
        for _ in xrange(10):
            with lock:
                x[1] += 1
                x[2] += 1

    for _ in xrange(10):
        threads.append(Thread(target=fun, args=(Lock(),)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    assert sum(x.values()) == 200


# Thanks to https://github.com/jimfulton/zope.interface/blob/4.0.1/src/zope/interface/advice.py#L28-L50

# Generated at 2022-06-13 16:38:44.397832
# Unit test for function lock_decorator
def test_lock_decorator():
    from __main__ import lock_decorator
    from threading import Lock

    @lock_decorator()
    def f(): pass

    @lock_decorator(attr='_lock')
    def g(): pass

    @lock_decorator(lock=Lock())
    def h(): pass



# Generated at 2022-06-13 16:38:55.154196
# Unit test for function lock_decorator
def test_lock_decorator():
    from ansibullbot.decorators.github import github_lock_decorator
    from ansibullbot.decorators.ansible_v2 import ansible_v2_lock_decorator

    class MockLock(object):
        def __init__(self):
            self.lockcount = 0

        def __enter__(self):
            self.lockcount += 1

        def __exit__(self, *args, **kwargs):
            self.lockcount -= 1

    class MockObject(object):
        pass

    mock_lock = MockLock()

    class DecoratorTest(object):
        @github_lock_decorator
        def github(self):
            return

        @ansible_v2_lock_decorator
        def ansible_v2(self):
            return


# Generated at 2022-06-13 16:39:05.968891
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import random

    class Test(object):

        def __init__(self):
            self._lock = threading.Lock()
            self._number = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            time.sleep(random.randint(0, 5))
            self._number += 1
            print('Thread %s has value %s' % (threading.current_thread().name, self._number))

    def thread():
        t = Test()
        t.increment()

    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=thread))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


# Generated at 2022-06-13 16:39:15.780804
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class LockTarget(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.val = 0

        @lock_decorator
        def no_lock_attr(self):
            self.val += 1

        @lock_decorator(attr='lock')
        def with_lock_attr(self):
            self.val += 1

        @lock_decorator(lock=threading.Lock())
        def with_lock_object(self):
            self.val += 1

    lock_target = LockTarget()
    assert lock_target.val == 0

    import multiprocessing
    def incr_no_attr():
        lock_target.no_lock_attr()

    def incr_with_attr():
        lock_target.with_lock_attr

# Generated at 2022-06-13 16:39:21.324692
# Unit test for function lock_decorator
def test_lock_decorator():
    global _called

    class TestLock(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._called = False

        @lock_decorator(attr='_lock')
        def lock_it(self):
            self._called = True

        @lock_decorator(lock=threading.Lock())
        def some_func(self):
            self._called = True

    TestLock.lock_it()
    TestLock.some_func()
    assert _called



# Generated at 2022-06-13 16:39:31.777172
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    This is a unit test to ensure the lock_decorator works
    as expected in various scenarios.

    Note: This test uses ``threading.Lock()`` to simulate
    the use of this decorator.  It is NOT trying to test
    locking in a multi-threading environment.
    '''
    import threading

    class SomeClass(object):
        '''
        This is a class that we can use to test the ``lock_decorator``
        '''
        def __init__(self):
            # Setup the lock attirbute
            self.lock_attr = threading.Lock()
            # Setup the wacky attribute
            self.wacky_attr = 'Something'


# Generated at 2022-06-13 16:39:42.363364
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread, Lock
    from time import sleep

    lock = Lock()
    l = []

    class Foo:
        _lock = Lock()

        @lock_decorator(attr='_lock')
        def meth(self, i):
            l.append(i)
            sleep(0.1)

    @lock_decorator(lock=lock)
    def f(i):
        l.append(i)
        sleep(0.1)

    t1 = Thread(target=Foo().meth, args=(1,))
    t2 = Thread(target=Foo().meth, args=(2,))
    t3 = Thread(target=f, args=(3,))
    t4 = Thread(target=f, args=(4,))

    t1.start()
    t2.start()


# Generated at 2022-06-13 16:39:51.411973
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class ExampleClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.value = 1

        @lock_decorator(attr='_lock')
        def add_value(self):
            self.value += 1

        @lock_decorator(lock=threading.Lock())
        def del_value(self):
            self.value -= 1

    ExampleClass().add_value()
    assert ExampleClass().value == 2
    ExampleClass().del_value()
    assert ExampleClass().value == 1

# Generated at 2022-06-13 16:40:01.252029
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    class TestLock(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.yes = 0

        @lock_decorator(attr='_lock')
        def method_with_lock(self):
            self.yes += 1

        @lock_decorator(lock=lock)
        def method_with_decorator_lock(self):
            self.yes += 1

    test_lock = TestLock()
    test_lock.method_with_lock()
    test_lock.method_with_decorator_lock()
    assert test_lock.yes == 2
    t = threading.Thread(target=test_lock.method_with_lock)
    t.start()
    assert test_lock.yes == 2

# Generated at 2022-06-13 16:40:10.562593
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.lock = threading.Lock()

        @lock_decorator(lock=threading.Lock())
        def test_lock_passed(self):
            self.assertTrue(True)

        @lock_decorator(attr='lock')
        def test_attr_passed(self):
            self.assertTrue(True)

        @lock_decorator()
        def test_missing_args(self):
            self.assertTrue(True)

    # Define empty `TestCase` if not run as standalone
    unittest.main(module=__name__, exit=False)

# Generated at 2022-06-13 16:40:18.863056
# Unit test for function lock_decorator
def test_lock_decorator():
    # Fake class
    class FakeClass(object):
        def __init__(self):
            self.lock = True

        @lock_decorator(attr='lock')
        def method(self):
            self.lock = False
            return True

    fake = FakeClass()
    fake.method()
    assert fake.lock

# Generated at 2022-06-13 16:40:28.909793
# Unit test for function lock_decorator
def test_lock_decorator():

    import unittest
    import mock
    import threading
    import time

    class Worker(threading.Thread):
        def __init__(self, lock, cnt):
            threading.Thread.__init__(self)
            self.lock = lock
            self.cnt = cnt
            self.exit = False
            self.result = 0

        def run(self):
            while not self.exit:
                with self.lock:
                    self.result += 1
                    self.cnt -= 1
                    if self.cnt == 0:
                        self.exit = True
            self.result *= 2

    mocking_time = mock.patch('time.sleep', return_value=None)

# Generated at 2022-06-13 16:40:40.023876
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class C(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._data = 0

        # This is an attribute-based lock
        @lock_decorator(attr='_lock')
        def _increment(self):
            self._data += 1

        # This is an explicit lock
        @lock_decorator(lock=threading.Lock())
        def _print_data(self):
            print(self._data)

    c = C()

    def run():
        while True:
            c._increment()
            time.sleep(0)

    def read():
        while True:
            c._print_data()
            time.sleep(0)


# Generated at 2022-06-13 16:40:45.647015
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from ansible.module_utils.six.moves import _thread as thread
    from time import time

    class Foo(object):

        def __init__(self):
            self._timer = 0
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def callback_timer(self):
            start = time()
            print('start: %f' % start)
            w = threading.Event()
            w.wait(5)
            end = time()
            self._timer = end - start
            print('end: %f' % end)

    f = Foo()

    t1 = thread.start_new_thread(f.callback_timer, ())
    t2 = thread.start_new_thread(f.callback_timer, ())



# Generated at 2022-06-13 16:40:54.602487
# Unit test for function lock_decorator
def test_lock_decorator():
    class TestLock(object):
        lock = threading.Lock()

        @lock_decorator(attr='lock')
        def method_1(self):
            self.lock_state = self.lock.acquire(blocking=False)
            time.sleep(2)
            self.lock.release()

        @lock_decorator(lock=threading.Lock())
        def method_2(self):
            self.lock_state = self.lock.acquire(blocking=False)
            time.sleep(2)
            self.lock.release()

    test = TestLock()
    start_time = time.time()
    test.method_1()
    assert test.lock_state is True
    assert time.time() - start_time < 2
    start_time = time.time()
    test.method_2()

# Generated at 2022-06-13 16:41:03.406289
# Unit test for function lock_decorator
def test_lock_decorator():
    import inspect
    import threading

    class TestLockDecorator(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback_1(self):
            return inspect.currentframe().f_back.f_code.co_name

        @lock_decorator(lock=threading.Lock())
        def send_callback_2(self):
            return inspect.currentframe().f_back.f_code.co_name

        @lock_decorator(attr=None)
        def send_callback_3(self):
            return inspect.currentframe().f_back.f_code.co_name

    tld = TestLockDecorator()
    assert tld.send_callback_1()

# Generated at 2022-06-13 16:41:12.601233
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    _lock = threading.Lock()
    _lock_attr = '_callback_lock'

    class Test(object):

        def __init__(self):
            setattr(self, _lock_attr, _lock)

        @lock_decorator(attr=_lock_attr)
        def method(self):
            return 10

        @lock_decorator(lock=_lock)
        def method2(self):
            return 20

    t = Test()

    print(t.method(), t.method2())
    # Prints:
    # 10 20

# Generated at 2022-06-13 16:41:14.814080
# Unit test for function lock_decorator
def test_lock_decorator():
    def test_func():
        return
    assert lock_decorator('_lock')(test_func)
    assert lock_decorator(lock=1)(test_func)

# Generated at 2022-06-13 16:41:25.867696
# Unit test for function lock_decorator
def test_lock_decorator():
    # Make sure that the decorator raises an exception when used improperly.
    import pytest
    from threading import Lock
    with pytest.raises(Exception):
        @lock_decorator()
        def dummy():
            pass

    # Define a dummy class that has a lock and a method that uses it
    class Dummy(object):
        def __init__(self, lock=None):
            # Default lock is a threading lock
            if lock is None:
                self._lock = Lock()
            else:
                # Otherwise use the one passed in
                self._lock = lock
            # Set this to a large value so we can tell whether the
            # decorated method is using the lock correctly.
            self._counter = 999999
            # We will set this to something more useful later
            self._final_counter = None


# Generated at 2022-06-13 16:41:36.437932
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    class A(object):
        def __init__(self, lock=lock):
            self.lock = lock

        @lock_decorator(lock=lock)
        def some_method(self):
            print('some_method lock = stored object')

        @lock_decorator(attr='lock')
        def another_method(self):
            print('another_method lock = stored object')

        @lock_decorator(lock=lock)
        def bad_method(self):
            raise Exception('some_method exception')

        @lock_decorator(attr='lock')
        def bad_attr_method(self):
            raise Exception('another_method exception')

    class B(object):
        lock = lock


# Generated at 2022-06-13 16:41:47.204191
# Unit test for function lock_decorator
def test_lock_decorator():
    # There is no good way to test locks in a unit test context
    pass

# Generated at 2022-06-13 16:41:56.824742
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    class Context(object):
        def __enter__(self):
            # print('lock_decorator: enter')
            pass

        def __exit__(self, exc_type, exc_value, traceback):
            # print('lock_decorator: exit')
            pass

    class Test(object):
        def __init__(self):
            self.lock = Context()

        @lock_decorator(lock=Context())
        def method1(self):
            pass

        @lock_decorator(attr='lock')
        def method2(self):
            pass

        @lock_decorator
        def method3(self):
            pass

    Test()

# Generated at 2022-06-13 16:42:04.080373
# Unit test for function lock_decorator

# Generated at 2022-06-13 16:42:15.671933
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread

    class TestClass(object):
        def __init__(self):
            self.counter = 0
            self.lock = Lock()

        def increment_counter(self):
            self.counter += 1

        @lock_decorator(attr='lock')
        def increment_counter_lock_attr(self):
            self.increment_counter()

        @lock_decorator(lock=Lock())
        def increment_counter_lock_init(self):
            self.increment_counter()

    test = TestClass()
    thread_list = []
    for _ in range(10):
        t = Thread(target=test.increment_counter)
        thread_list.append(t)
        t.start()
    while thread_list:
        thread_list.pop().join()
   

# Generated at 2022-06-13 16:42:24.396076
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    _lock = threading.Lock()

    class Test(object):
        # Needed to keep the instance and the class in sync
        def _set_lock(self, lock):
            self._lock = lock

        # Uses a method instance attribute
        @lock_decorator(attr='_lock')
        def _method(self):
            pass

        # Explicitly uses a lock
        @lock_decorator(lock=_lock)
        def _class_method(cls):
            pass

    # Test the instance with ``_method``
    t = Test()
    t._set_lock(_lock)
    # This should succeed
    with _lock:
        t._method()
    # This should fail

# Generated at 2022-06-13 16:42:30.493797
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class SomeClass(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method_1(self):
            return 0

        @lock_decorator(lock=_lock)
        def method_2(self):
            return 1

    assert SomeClass().method_1() == 0
    assert SomeClass().method_2() == 1

# Generated at 2022-06-13 16:42:38.018840
# Unit test for function lock_decorator
def test_lock_decorator():
    # Unit test based on example in README
    import threading

    class Container:

        def __init__(self):
            self.results = []
            self._lock = threading.Lock()
            self.running = False

        # Note: since we are using an actual threading lock, we
        # need to ensure the container isn't deleted while the
        # lock is in use.
        @lock_decorator(attr='_lock')
        def add(self, item):
            self.results.append(item)

        def make_running(self):
            self.running = True

    lock = threading.Lock()
    results = []

    @lock_decorator(lock=lock)
    def test_lock():
        results.append('hi')

    threads = []
    container = Container()


# Generated at 2022-06-13 16:42:46.971115
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Lock decorator usage test'''
    import threading
    class Foo(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, *args, **kwargs):
            return args, kwargs

    f = Foo()
    assert f.send_callback('hello', 1, 2, 3) == (('hello', 1, 2, 3), {})
    assert f.send_callback(1, 2, 3, item='hello') == ((1, 2, 3), {'item': 'hello'})

    class Bar(object):
        @lock_decorator(lock=threading.Lock())
        def send_callback(self, *args, **kwargs):
            return args,

# Generated at 2022-06-13 16:42:58.200314
# Unit test for function lock_decorator
def test_lock_decorator():
    # Create 2 locks
    lock1 = threading.Lock()
    lock2 = threading.Lock()

    # Create an instance
    class Foo:
        def __init__(self, lock=None):
            self.lock = lock

        @lock_decorator()
        def l1(self):
            return self.lock

        @lock_decorator(attr='lock')
        def l2(self):
            return self.lock

        @lock_decorator(lock=lock2)
        def l3(self):
            return self.lock

    # Create a class
    class Bar:
        @lock_decorator()
        def l1(self):
            return self.lock

        @staticmethod
        @lock_decorator()
        def l2():
            return self.lock


# Generated at 2022-06-13 16:43:06.327458
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    test_lock = threading.Lock()
    test_counter = 0
    test_counter_lock = threading.Lock()

    @lock_decorator(attr='test_lock')
    def test_method(self):
        time.sleep(1)
        with test_counter_lock:
            global test_counter
            test_counter += 1

    @lock_decorator(lock=test_lock)
    def test_method_two(self):
        time.sleep(1)
        with test_counter_lock:
            global test_counter
            test_counter += 1

    class TestClass(object):
        def __init__(self):
            self.test_lock = test_lock

        test_method = test_method
        test_method_two = test_method_two

# Generated at 2022-06-13 16:43:26.294871
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    class Foo:
        @lock_decorator(attr='_lock')
        def foo1(self):
            pass

    

# Generated at 2022-06-13 16:43:33.372350
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import random

    def test_wrapper(num, lock_obj=None):
        @lock_decorator(lock=lock_obj)
        def some_function(num):
            time.sleep(random.random())
            print(num)

        return some_function

    def test_wrapper_no_lock(num):
        @lock_decorator
        def some_function(self, num):
            time.sleep(random.random())
            print(num)

        return some_function

    def threaded(fn):
        def wrapper():
            thread = threading.Thread(target=fn)
            thread.start()
            return thread

        return wrapper


# Generated at 2022-06-13 16:43:43.901954
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    try:
        from Queue import Empty as Empty  # pylint: disable=deprecated-module
    except ImportError:
        from queue import Empty

    class LockTestClass(object):
        '''A simple class to test lock_decorator'''
        def __init__(self):
            self.lock = threading.Lock()
            self.queue = []

        @lock_decorator(attr='lock')
        def put(self, item):
            '''Put an item on the queue'''
            self.queue.append(item)

        def get(self):
            '''Get an object off the queue'''
            try:
                return self.queue.pop(0)
            except IndexError:
                # the queue is empty
                raise Empty


# Generated at 2022-06-13 16:43:52.096072
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Tests for the lock_decorator function'''
    # Get a simple mock base class
    class MockedClass(object):
        '''Mocks a class'''
        def __init__(self):
            self._lock = None
            self._lock_is_acquired = False
            self._lock_is_released = False
            self._run_this_code = False

        @lock_decorator('_lock')
        def method(self):
            '''Code that should not be run more than once at a time'''
            self._lock_is_acquired = True
            if self._run_this_code:
                expected = True
            else:
                expected = False
            self._run_this_code = True
            self._lock_is_released = True
            return expected

    # Instantiate the

# Generated at 2022-06-13 16:43:58.258353
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Instance(object):
        _callback_lock = threading.Lock()
        callbacks = []

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, value):
            self.callbacks.append(value)

        def send_no_lock(self, value):
            self.callbacks.append(value)

    class Class(object):
        _callback_lock = threading.Lock()
        callbacks = []

        @lock_decorator(attr='_callback_lock')
        def send_callback(cls, value):
            cls.callbacks.append(value)

        def send_no_lock(cls, value):
            cls.callbacks.append(value)



# Generated at 2022-06-13 16:44:03.748968
# Unit test for function lock_decorator
def test_lock_decorator():
    def my_func(*args, **kwargs):
        return args, kwargs
    from threading import Lock
    my_lock = Lock()
    my_func = lock_decorator(attr='missing_lock_attr', lock=my_lock)(my_func)
    assert my_func(1) == ((1,), {})


# Generated at 2022-06-13 16:44:09.258319
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo(object):
        _lock = None

        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def foo(self, number):
            return number

    foo = Foo()
    assert foo.foo(10) == 10



# Generated at 2022-06-13 16:44:18.616459
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestLockObject(object):

        @lock_decorator(attr='_lock')
        def test_with_attr(self):
            return True

        @lock_decorator(lock=None)
        def test_with_no_lock(self):
            return True

        @lock_decorator(lock=threading.Lock())
        def test_with_lock(self):
            return True

    o = TestLockObject()

    # make sure we are testing the right thing
    assert not hasattr(o, '_lock')

    # we should never get a false
    assert o.test_with_attr() is True
    # we should not fail
    assert o.test_with_no_lock() is True
    # we should not fail
    assert o.test_with_lock() is True

# Generated at 2022-06-13 16:44:30.733481
# Unit test for function lock_decorator
def test_lock_decorator():
  import unittest
  from collections import defaultdict

  class TestClass(object):
    def __init__(self):
      self.counter = defaultdict(int)
      self.counter_lock = defaultdict(int)
      self.__callback_lock = defaultdict(int)
      self._lock = defaultdict(int)

    @lock_decorator(attr='__callback_lock')
    def test_send_callback(self, key, amount=1):
      self.counter[key] += 1

    @lock_decorator(lock=self.__callback_lock)
    def test_send_callback_2(self, key, amount=1):
      self.counter[key] += 1

    @lock_decorator()
    def test_send_callback_3(self, key, amount=1):
      self

# Generated at 2022-06-13 16:44:40.123239
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class MyClass(object):
        def __init__(self):
            self.x = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def do_something(self):
            self.x += 1
            time.sleep(0.1)

    lock = threading.Lock()
    a = MyClass()
    b = MyClass()
    c = MyClass()

    @lock_decorator(lock=a.lock)
    def _do_something():
        a.x += 1
        time.sleep(0.1)

    @lock_decorator(lock=b.lock)
    @lock_decorator(lock=c.lock)
    def _do_something1():
        b.x += 1


# Generated at 2022-06-13 16:45:24.169664
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class _TestLockDecorator(unittest.TestCase):
        def test_lock_attr(self):
            @lock_decorator(attr='_get_neg1_lock')
            def get_neg1(self):
                return -1

            class _Test(object):
                def __init__(self):
                    self._get_neg1_lock = threading.Lock()

            t = _Test()
            self.assertEqual(get_neg1(t), -1)

        def test_lock_explicit(self):
            @lock_decorator(lock=threading.Lock())
            def get_neg1_explicit():
                return -1
            self.assertEqual(get_neg1_explicit(), -1)

    # Run tests using

# Generated at 2022-06-13 16:45:33.779479
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.accessed = 0

        # Note that the attribute `_lock` can also be defined as an
        # attribute of the class, but to keep things simple for the
        # unit test, we will only instantiate a single object.
        @lock_decorator(attr='_lock')
        def method(self, sleep=0):
            time.sleep(sleep)
            self.accessed += 1

    obj = Test()
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=obj.method, args=(0.01,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join

# Generated at 2022-06-13 16:45:36.515968
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self._callback_lock = threading.RLock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            return 42

        @lock_decorator(lock=threading.RLock())
        def some_method(self):
            return 42

    assert Test().send_callback() == 42
    assert Test().some_method() == 42



# Generated at 2022-06-13 16:45:43.627279
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading
    import time

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def foo(self, sleep=0.0):
            if sleep:
                time.sleep(sleep)
            return 0

        @lock_decorator(lock=threading.Lock())
        def bar(self, sleep=0.0):
            if sleep:
                time.sleep(sleep)
            return 0

    _lock = threading.Lock()
    foo = lock_decorator(lock=_lock)(lambda: 0)

    with mock.patch('threading.Thread') as mock_thread:
        mock_thread.return_value.start = mock.Mock()

# Generated at 2022-06-13 16:45:53.846890
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class TestLockDecorator():

        _lock = threading.Lock()

        @lock_decorator()
        def test_method1(self, arg1, arg2):
            return arg1+arg2

        @lock_decorator(attr='_lock')
        def test_method2(self, arg1, arg2):
            return arg1+arg2

        @lock_decorator(lock=_lock)
        def test_method3(self, arg1, arg2):
            return arg1+arg2

    t = TestLockDecorator()

    assert t.test_method1(1, 2) == 3
    # _lock is missing, should fail
    try:
        t.test_method2(1, 2)
    except AttributeError:
        pass