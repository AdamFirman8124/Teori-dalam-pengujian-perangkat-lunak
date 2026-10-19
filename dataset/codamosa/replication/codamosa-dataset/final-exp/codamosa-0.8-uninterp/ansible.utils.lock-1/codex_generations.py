

# Generated at 2022-06-13 16:36:02.114295
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    if sys.version_info[0] > 2:
        import builtins
        exec_ = getattr(builtins, 'exec')
    else:
        def exec_(_code_, _globs_=None, _locs_=None):
            """Execute code in a namespace."""
            if _globs_ is None:
                frame = sys._getframe(1)
                _globs_ = frame.f_globals
                if _locs_ is None:
                    _locs_ = frame.f_locals
                del frame
            elif _locs_ is None:
                _locs_ = _globs_
            exec("""exec _code_ in _globs_, _locs_""")

    from copy import copy
    from tempfile import mkstemp

# Generated at 2022-06-13 16:36:13.347490
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from threading import Lock

    class TestClass(object):
        def __init__(self):
            self.lock_attr = Lock()
            self.lock_arg = Lock()
            self.twice = 0

        @lock_decorator(attr='lock_attr')
        def inc_with_lock_attr(self):
            self.twice += 1

        @lock_decorator(lock=self.lock_arg)
        def inc_with_lock_arg(self):
            self.twice += 1

    obj = TestClass()
    assert obj.twice == 0
    obj.inc_with_lock_attr()
    assert obj.twice == 1
    obj.inc_with_lock_arg()
    assert obj.twice == 2

    obj_2 = TestClass()
   

# Generated at 2022-06-13 16:36:23.567634
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import random

    class Foo(object):
        def __init__(self):
            self.value = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def update_value(self):
            # this is the real method
            self.value += 1

        @lock_decorator(lock=threading.Lock())
        def update_value_2(self):
            # this method requires the lock to be explicitly passed
            self.value += 1

    foo = Foo()
    # simulate multiple threads updating the values at the same time
    def test_thread(lock):
        for _ in range(100000):
            with lock:
                foo.update_value()

# Generated at 2022-06-13 16:36:33.174553
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    def lock_decorator_test():
        foo_lock = threading.Lock()

        class Foo(object):
            @lock_decorator(attr='_foo_lock')
            def foo(self, value):
                return value

            def bar(self, value):
                return value

            @lock_decorator(lock=foo_lock)
            def baz(self, value):
                return value

        foo1 = Foo()
        foo2 = Foo()

        assert foo1.foo('foo1') == 'foo1'
        assert foo2.foo('foo2') == 'foo2'

        assert foo1.bar('bar1') == 'bar1'
        assert foo2.bar('bar2') == 'bar2'


# Generated at 2022-06-13 16:36:44.428567
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    import threading

    class TestLockDecoratorThread(threading.Thread):
        def __init__(self, obj, method, _lock):
            super(TestLockDecoratorThread, self).__init__()
            self.obj = obj
            self.method = method
            self.data = []
            self.lock = _lock

        def run(self):
            with self.lock:
                for i in range(5):
                    retval = self.method(self.obj, i)
                    self.data.append(retval)

    class LockTests(unittest.TestCase):
        def test_lock_decorator(self):
            _lock = threading.Lock()

            @lock_decorator(lock=_lock)
            def this(obj, data):
                return

# Generated at 2022-06-13 16:36:54.329893
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading
    import sys
    if sys.version_info < (3,):
        from Queue import Queue
    else:
        from queue import Queue

    class LockableObject(object):
        '''A simple class that has an attribute that is a lock'''
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def withlock(self):
            return True

        @lock_decorator(lock=threading.Lock())
        def withlock2(self):
            return True

        def __repr__(self):
            return 'LockableObject'

    # Verify the lock decorator works as a standalone
    lockable = LockableObject()
    assert lockable.withlock()

# Generated at 2022-06-13 16:37:05.478788
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class C(object):
        @lock_decorator(attr='_callback_lock')
        def send_callback(self, x):
            return x

    class D(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, x):
            return x

    class E(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(lock=self._callback_lock)
        def send_callback(self, x):
            return x

    c = C()
    assert c.send_callback('test') == 'test'

    d = D()

# Generated at 2022-06-13 16:37:13.751048
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    # Example class
    class Test(object):
        def __init__(self):
            self._lock = Lock()

        @lock_decorator(attr='_lock')
        def foo(self):
            return self._lock

        @lock_decorator(lock=Lock())
        def bar(self):
            return self._lock

    t = Test()
    # Ensure ``foo`` method's lock is the same as ``bar``
    assert t.foo() is t.bar()
    # Ensure ``foo`` method's lock is the same as ``_lock`` attribute
    assert t.foo() is t._lock

# Generated at 2022-06-13 16:37:21.710242
# Unit test for function lock_decorator
def test_lock_decorator():
    class Test:
        def __init__(self):
            self.lock = threading.Lock()
            self.test_lock = threading.Lock()
            self.test_lock_value = 0

        @lock_decorator(attr='lock', lock=None)
        def test_lock(self):
            self.test_lock_value += 1
            return self.test_lock_value

    test = Test()
    assert test.test_lock() == 1

# vim: set sts=4 sw=4 et :

# Generated at 2022-06-13 16:37:28.206082
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import unittest

    class TestLock(unittest.TestCase):
        _test_lock = threading.Lock()
        _test_lock_attr = threading.Lock()

        def test_implicit_lock(self):
            # This test ensures that for implicit locks (passing attr=...),
            # that the actual lock is different for each instance

            @lock_decorator(attr='_test_lock_attr')
            def _inner_lock(self, test_val=None):
                return test_val

            # This will get the lock from the class and
            # lock it, then unlock and return None
            # note that self._test_lock and
            # self._test_lock_attr are different
            self.assertEqual(_inner_lock(self), None)
            # This will get

# Generated at 2022-06-13 16:37:40.856553
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    from threading import Lock
    lock = Lock()
    mock_lock = mock.MagicMock()

    @lock_decorator(attr='attr')
    def test_attr(*args, **kwargs):
        return args, kwargs

    @lock_decorator(lock=lock)
    def test_lock(*args, **kwargs):
        return args, kwargs

    @lock_decorator(lock=mock_lock)
    def test_mock_lock(*args, **kwargs):
        return args, kwargs

    object_attr = object()
    object_lock = object()
    object_mock_lock = object()

    class Test(object):
        attr = lock

    assert test_attr(object_attr) == ((object_attr,), {})

# Generated at 2022-06-13 16:37:52.205993
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class MyClass(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def lock_test_method(self, seconds):
            import time
            time.sleep(seconds)

    class MyOtherClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._other_lock = threading.Lock()

        def run_threads(self):
            threads = []
            for seconds in range(10):
                t = threading.Thread(target=self.lock_test_method, args=(seconds,))
                t.start()
                threads.append(t)
            return threads

        # @lock_decorator(lock=self._other_lock)
       

# Generated at 2022-06-13 16:38:02.500659
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread

    class TestClass(object):
        def __init__(self):
            self.data = None
            self.shared = 0

        @lock_decorator(attr='_lock')
        def set_data(self, data):
            self.data = data

        @lock_decorator(lock=Lock())
        def add_to_shared(self, value):
            self.shared += value

    def thread_func(cls):
        # Ensure that the lock is working. We'll send some data
        # to ``set_data`` and confirm that it was written
        # successfully.
        cls.set_data('foobar')
        cls.add_to_shared(2)

    c = TestClass()
    # create a thread

# Generated at 2022-06-13 16:38:09.974839
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Unit test for lock_decorator'''
    import threading
    from collections import defaultdict
    from time import sleep

    # Some usage examples
    class _using_pre_defined_lock(object):
        _lock = threading.Lock()
        _counters = defaultdict(int)

        @lock_decorator(attr='_lock')
        def increment(self, key):
            self._counters[key] += 1
    # Create the class object
    udpl1 = _using_pre_defined_lock()


    class _using_explicit_lock(object):
        _counters = defaultdict(int)

        @lock_decorator(lock=threading.Lock())
        def increment(self, key):
            self._counters[key] += 1

    # Create the class object
   

# Generated at 2022-06-13 16:38:18.896786
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading
    # Python3.3+ has mock builtin
    from ansible.module_utils.six.moves import mock
    class LockDecoratorTests(unittest.TestCase):
        def test_attr(self):
            # Create an attribute on the fly
            setattr(self, '_test_lock', threading.Lock())
            @lock_decorator(attr='_test_lock')
            def test_method(self):
                self._test_method_call_count += 1

            # mock out ``self._test_lock.__enter__`` and ``self._test_lock.__exit__``
            # so that we can see if they are called
            # ``self._test_lock.__exit__`` will be called even when ``self._test_lock.__enter__``

# Generated at 2022-06-13 16:38:30.063211
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading
    import time

    class TestClass(object):
        def __init__(self):
            # Use a lock defined on the class
            self._lock = threading.Lock()

        def test_method(self):
            '''This method should always return True.'''
            with self._lock:
                # Return True if our class has the lock
                return threading.currentThread().name in self._lock._owned

        @lock_decorator(attr='_lock')
        def test_method2(self):
            '''This method should always return True.'''
            # Return True if our class has the lock
            return threading.currentThread().name in self._lock._owned

    def run_test_method(test_obj):
        '''Test that the method is thread-safe.'''
        thread

# Generated at 2022-06-13 16:38:37.490949
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):

        def __init__(self):
            self._callback_lock = threading.Lock()
            self.result = []

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, result):
            self.result.append(result)

    foo = Foo()

    # Without lock, threading is not gaurenteed to work
    from threading import Thread

    threads = [Thread(target=foo.send_callback, args=[i]) for i in range(100)]
    [t.start() for t in threads]
    [t.join() for t in threads]
    assert all(isinstance(result, int) for result in foo.result), 'Values should be valid integers'

# Generated at 2022-06-13 16:38:47.550185
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    class TestExample(unittest.TestCase):
        def test_attr_lock(self):
            class TestLocker(object):
                @lock_decorator(attr='lock')
                def locked_method(self):
                    self.lock_acquired = True

            # Test that the lock was acquired
            tl = TestLocker()
            tl.lock_acquired = False
            tl.lock = threading.Lock()
            tl.lock.acquire()
            tl.locked_method()
            self.assertTrue(tl.lock_acquired)

            # Test that the lock was released
            tl.lock_acquired = False
            tl.locked_method()
            self.assertFalse(tl.lock_acquired)


# Generated at 2022-06-13 16:38:56.705098
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestLock:
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.counter = 0

        @lock_decorator(attr='_callback_lock')
        def counter_inc(self):
            self.counter += 1

        @lock_decorator(lock=threading.Lock())
        def counter_dec(self):
            self.counter -= 1

    t = TestLock()

    threads = []

    for i in range(10):
        t = threading.Thread(target=t.counter_inc)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    assert t.counter == 10, 'TestLock.counter_inc failed to lock'

    threads = []


# Generated at 2022-06-13 16:39:01.200521
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestLock(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.shared_variable = ''
            self.thread_has_lock = False

        @lock_decorator(attr='lock')
        def do_work(self):
            print("%s: holding the lock" % threading.current_thread().name)
            self.thread_has_lock = True
            time.sleep(0.1)
            print("%s: releasing the lock" % threading.current_thread().name)
            self.thread_has_lock = False

    def thread_with_explicit_lock():
        t = TestLock()

# Generated at 2022-06-13 16:39:15.421911
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import sys

    class SynchronizedTestClass:

        _lock = threading.RLock()

        @lock_decorator(attr='_lock')
        def test_method(self):
            sys.stdout.write('method start\n')
            for i in range(1, 4):
                time.sleep(1)
                sys.stdout.write('method-{}\n'.format(i))

    class LockTestClass:

        @lock_decorator(lock=threading.RLock())
        def test_method(self):
            sys.stdout.write('method start\n')
            for i in range(1, 4):
                time.sleep(1)
                sys.stdout.write('method-{}\n'.format(i))


# Generated at 2022-06-13 16:39:20.695901
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    class Foo(object):
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator(lock=self.lock)
        def bar(self):
            return ''

        @lock_decorator(attr='lock')
        def baz(self):
            return ''

    foo = Foo()
    bar = foo.bar
    baz = foo.baz



# Generated at 2022-06-13 16:39:31.314547
# Unit test for function lock_decorator
def test_lock_decorator():
    from ansible.utils.lock import lock_decorator
    import threading

    # generic lock
    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def some_method(x):
        return x

    assert some_method(1) == 1

    # class lock
    class TestLock(object):
        def __init__(self):
            self.lock = threading.Lock()

        def some_method(self, x):
            return x

    # class lock attribute
    tl1 = TestLock()
    tl1.some_method(1) == 1  # return will be passed through
    tl1.some_method = lock_decorator(attr='lock')(tl1.some_method)
    # now we have a lock
    assert tl1.some_

# Generated at 2022-06-13 16:39:41.947155
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    _lock = threading.Lock()
    _session = mock_session()
    _session._callback_lock = _lock
    _session._callback = False
    def send_callback():
        assert not _session._callback_lock.locked()
        _session._callback = True
        _session._callback_lock.acquire()
        assert _session._callback_lock.locked()
    _session._send_callback = lock_decorator(attr='_callback_lock')(send_callback)
    def assert_callback():
        assert _session._callback_lock.locked()
        assert _session._callback
    _session._assert_callback = lock_decorator(attr='_callback_lock')(assert_callback)
    _session._send_callback()
    _session._assert_callback()
    # Note that the lock

# Generated at 2022-06-13 16:39:53.993747
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        '''A test class for the lock_decorator'''
        def __init__(self):
            self._locked = False

        def get_lock_status(self):
            '''Return the current lock state on the test object'''
            return self._locked

        @lock_decorator(attr='_lock')
        def my_method(self):
            '''This method is decorated with lock_decorator'''
            self._locked = True

        @staticmethod
        @lock_decorator(lock=threading.Lock())
        def my_static_method():
            '''This static method is decorated with lock_decorator'''
            pass

    # Create a test object and a lock for it
    test_obj = TestClass()
    test_obj._

# Generated at 2022-06-13 16:40:02.849677
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    # pylint: disable=R0903
    class _Mock(object):
        _callback_lock = threading.RLock()

        @lock_decorator(attr='_callback_lock')
        def callback(self, value):
            return value

    mock = _Mock()

    # Apparently RLock() doesn't work with threading.Thread, so
    # for this simple test we'll use a plain old threading.Lock()
    lock = threading.Lock()

    def do_some_stuff(value):
        with lock:
            return mock.callback(value)

    def do_some_other_stuff(value):
        with lock:
            return mock.callback(value)

    # This is generally bad practice, but I'm trying to test that
    # the decorator is using a lock by using

# Generated at 2022-06-13 16:40:11.595458
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import unittest

    def get_sleep_time(i):
        if i == 2:
            return 2
        return 0.05

    class TestClass(object):

        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def _callback(self, i):
            time.sleep(get_sleep_time(i))

        def _iterator(self, iterator):
            for i in iterator:
                self._callback(i)
            return True

    start_time = time.time()
    tc = TestClass()
    tc._iterator(range(4))
    time_diff = time.time() - start_time

# Generated at 2022-06-13 16:40:21.141489
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading

    counter = 0

    class LockUser(object):
        def __init__(self):
            self._lock = threading.Lock()

        @property
        def val(self):
            return counter

        @lock_decorator()
        def increment(self):
            global counter
            time.sleep(0.01)
            counter += 1

    users = [LockUser() for _ in range(100)]

    def do_increment(user):
        user.increment()

    threads = [threading.Thread(target=do_increment, args=(user,)) for user in users]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert counter == len(users)

# Generated at 2022-06-13 16:40:30.104893
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.state = 0

        @lock_decorator(attr='_lock')
        def method_with_lock(self):
            self.state += 1

    class TestClassDecorator(object):
        def __init__(self):
            self.state = 0

        @lock_decorator(lock=threading.Lock())
        def method_with_lock(self):
            self.state += 1

    tc = TestClass()
    tcd = TestClassDecorator()

    def do(self):
        self.method_with_lock()

    t = threading.Thread(target=do, args=(tc,))
    t.start()
    tc.method_with_

# Generated at 2022-06-13 16:40:40.722147
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class Test(unittest.TestCase):
        def test_self_attr(self):
            _lock = threading.Lock()

            class X(object):
                def __init__(self, _lock):
                    self._lock = _lock
                    self.lock_count = 0

                @lock_decorator(attr='_lock')
                def locked(self):
                    self.lock_count += 1

            x = X(_lock)

            x.locked()
            x.locked()

            self.assertEqual(x.lock_count, 2)

        def test_explicit_lock(self):
            _lock = threading.Lock()

            class X(object):
                def __init__(self, _lock):
                    self.lock_count = 0


# Generated at 2022-06-13 16:40:54.436938
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    l = threading.Lock()
    lock_decorator(lock=l)

    @lock_decorator(attr='lock')
    def test(obj):
        obj.test = 'pass'

    obj = mock.Mock()
    obj.lock = l

    with mock.patch('%s.threading.Lock' % __name__, new=mock.Mock(return_value=l)) as lock:
        assert lock.call_count == 0
        test(obj)
        assert lock.call_count == 0
        assert obj.test == 'pass'

# Generated at 2022-06-13 16:40:59.043196
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class ExampleClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._test = 'foo'

        @lock_decorator(attr='_lock')
        def method(self):
            return self._test

    example = ExampleClass()

    assert example.method() == 'foo'

# Generated at 2022-06-13 16:41:05.939368
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestLockDecorator(object):
        def __init__(self, lock_attr=False):
            self._callback_lock = threading.Lock()
            self.lock_attr = lock_attr

        @lock_decorator()
        def send_callback_no_lock_attr(self):
            pass

        @lock_decorator(attr='_callback_lock')
        def send_callback_with_lock_attr(self):
            pass

        @lock_decorator(lock=threading.Lock())
        def send_callback_with_lock_object(self):
            pass

    # We are assuming that the other uses of lock_decorator, outside of this
    # unit test, are all using ``lock_decorator(attr=...)`` and thus we only
    # need to test

# Generated at 2022-06-13 16:41:12.286139
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo:
        def __init__(self):
            self.lock = threading.Lock()
            self.count = 0

        @lock_decorator(attr='lock')
        def add_one(self):
            self.count += 1

        @lock_decorator(lock=threading.Lock())
        def sub_one(self):
            self.count -= 1

    foo = Foo()
    # Create our threads
    threads = [threading.Thread(target=foo.add_one) for _ in range(5)]
    threads.extend([threading.Thread(target=foo.sub_one) for _ in range(5)])
    # Start threads
    for t in threads:
        t.start()
    # Wait until all threads complete

# Generated at 2022-06-13 16:41:19.638931
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self, callback):
            self._callback_lock = threading.Lock()

            self.callback = callback
            self.called = False

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            self.called = True
            self.callback()

    lock = threading.Lock()
    obj = Test(callback=lock.acquire)

    obj.send_callback()
    assert obj.called is True
    assert lock.locked() is True

# Generated at 2022-06-13 16:41:28.975102
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    class LockTest(unittest.TestCase):
        def test_lock_decorator_attr(self):
            class TestClass(object):
                def __init__(self):
                    self.lock = threading.Lock()
                    self.num_calls = 0

                @lock_decorator(attr='lock')
                def spawn_many_calls(self, inc=1):
                    self.num_calls += inc

            tc = TestClass()

            # We spawn some threads and make sure that the number
            # of calls is only 1 in the end
            threads = [
                threading.Thread(target=tc.spawn_many_calls, args=(2,))
                for _ in range(10)
            ]

            # Start the threads
            for t in threads:
                t.start

# Generated at 2022-06-13 16:41:34.988441
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Example(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def func1(self):
            return True

        @lock_decorator(lock=_lock)
        def func2(self):
            return True

    example = Example()
    assert example.func1() is True
    assert example.func2() is True

# Generated at 2022-06-13 16:41:41.261934
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test:
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def do_something_bad(self):
            self.lock.acquire()
            raise Exception('Hello World')

        @lock_decorator(lock=threading.Lock())
        def do_something_good(self):
            return True
    test = Test()
    assert test.lock.locked() == False
    try:
        test.do_something_bad()
    except Exception:
        pass
    assert test.lock.locked() == False
    assert test.do_something_good() == True

# Generated at 2022-06-13 16:41:45.640629
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Unit test for the lock_decorator util'''

    import shutil
    import tempfile
    import os
    import threading
    import time

    tmpdir = tempfile.mkdtemp()

    class A:
        def __init__(self):
            # Create a lock
            self._lock = threading.Lock()
            # Create a filepath to get locked
            self.path = os.path.join(tmpdir, 'test_lock_decorator.txt')

        @lock_decorator(attr='_lock')
        def write_to_file(self, text):
            with open(self.path, 'w') as f:
                f.write(text)


# Generated at 2022-06-13 16:41:56.787130
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test(object):
        def __init__(self):
            self.index = 0
            self.lock = threading.Lock()

        @lock_decorator(lock=self.lock)
        def increment_index(self, amount=1):
            self.index += amount

    class TestAttr(object):
        def __init__(self):
            self.index = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def increment_index(self, amount=1):
            self.index += amount

    test = Test()
    test_attr = TestAttr()

    def run(obj):
        for x in range(0, 100):
            obj.increment_index()
            time.sleep(0.01)

# Generated at 2022-06-13 16:42:22.506018
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()
    class DummyClass(object):
        @lock_decorator(attr='_lock_attr')
        def send_callback(self, foo, bar, baz):
            return (foo, bar, baz)

        @lock_decorator(lock=lock)
        def some_method(self, foo, bar, baz):
            return (foo, bar, baz)

    c = DummyClass()
    c._lock_attr = threading.Lock()
    assert c.send_callback('foo', 'bar', 'baz') == ('foo', 'bar', 'baz')
    assert c.some_method('foo', 'bar', 'baz') == ('foo', 'bar', 'baz')

# Generated at 2022-06-13 16:42:29.956480
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Foo(object):
        def __init__(self):
            self._lock = threading.RLock()
            self.counter = 0
        @lock_decorator(attr='_lock')
        def increment(self):
            self.counter += 1

    foo = Foo()
    from threading import Thread, RLock
    NUM_THREADS = 10
    NUM_ITERATIONS = 10
    threads = [
        Thread(target=foo.increment) for i in range(NUM_THREADS)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    assert foo.counter == NUM_THREADS*NUM_ITERATIONS

    # Test with no attr arg
    foo._lock = RLock()

# Generated at 2022-06-13 16:42:37.661387
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.foo_bar = None

        @lock_decorator()
        def foo_bar(self):
            self.foo_bar = None

        @lock_decorator(attr='_lock')
        def foo_baz(self):
            self.foo_baz = None

    foo = Foo()
    assert foo.foo_bar is None
    assert foo.foo_baz is None

    with mock.patch.object(Foo, 'foo_bar') as fb:
        foo.foo_bar()
        foo.foo_bar()
        fb.assert_called_once()


# Generated at 2022-06-13 16:42:46.762911
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import uuid
    import sys

    class MyClass:
        '''Create a class with a method that has a lock attribute,
        then call a method of the class from another thread.
        '''
        _lock = threading.Lock()

        def __init__(self):
            self.uuid = None

        @lock_decorator(attr='_lock')
        def my_method(self):
            time.sleep(1)
            self.uuid = str(uuid.uuid4())

    myclass = MyClass()
    assert myclass.uuid is None
    t = threading.Thread(target=myclass.my_method)
    t.start()
    t.join()
    assert myclass.uuid is not None

# Generated at 2022-06-13 16:42:58.073047
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from ansible.module_utils._text import to_bytes

    test_lock = threading.Lock()
    test_value = u'_test_lock_decorator'

    class TestClass(object):
        def __init__(self):
            self.some_value = u'some_value'

        @lock_decorator(attr='custom_lock')
        def some_method(self):
            self.some_value = test_value

        @lock_decorator(lock=test_lock)
        def some_other_method(self):
            self.some_value = test_value

    test_obj = TestClass()

    # Make sure some_method uses the internal lock
    test_obj.custom_lock = threading.Lock()

# Generated at 2022-06-13 16:43:06.244361
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading
    from time import sleep

    class LockDecoratorTest(object):

        def __init__(self):
            self.counter = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def test_method_attr(self):
            self.counter += 1
            sleep(1)
            self.counter += 1

        @lock_decorator(lock=threading.Lock())
        def test_method_lock(self):
            self.counter += 1
            sleep(1)
            self.counter += 1

    class P(threading.Thread):
        def __init__(self, obj, func):
            super(P, self).__init__()
            self.obj = obj
            self.func = func
            self.start()

# Generated at 2022-06-13 16:43:12.434485
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestLockDecorator(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            return 'callback'

    o = TestLockDecorator()
    assert o.send_callback() == 'callback'

    o = TestLockDecorator()
    assert o.send_callback() == 'callback'

    @lock_decorator(lock=threading.Lock())
    def some_method():
        return 'some_method'

    assert some_method() == 'some_method'

# Generated at 2022-06-13 16:43:18.871391
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class A(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def lock_method1(self):
            return True

        @lock_decorator(lock=threading.Lock())
        def lock_method2(self):
            return True

    a = A()
    assert a.lock_method1()
    assert a.lock_method2()

# Generated at 2022-06-13 16:43:24.386841
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import uuid
    import threading

    class LockDecoratorTests(unittest.TestCase):
        def test_lock_decorator(self):
            # Create a lock
            foo_lock = threading.Lock()

            # Create a set, to ensure duplicate results
            # aren't generated
            f = set()

            # Create a test object with a lock object
            class Foo(object):
                @lock_decorator(lock=foo_lock)
                def foo(self):
                    foo_uuid = uuid.uuid4().hex
                    f.add(foo_uuid)
                    return foo_uuid

            # Instantiate the Foo class 3 times
            foo_0 = Foo()
            foo_1 = Foo()
            foo_2 = Foo()

            # Test results of the

# Generated at 2022-06-13 16:43:32.441551
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestObj(object):
        """
        TestObject is used to test the lock_decorator
        """

        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, callback):
            """
            Example usage of the lock_decorator
            """
            callback()

    def test_callback_function():
        """
        This function is passed to the send_callback method.
        """
        test_obj.results.append(0)

    def test_callback_function_sleep():
        """
        This function is passed to the send_callback method.
        The purpose is to test the decorator by forcing
        a second call to send_callback to wait.
        """
        test

# Generated at 2022-06-13 16:44:15.956948
# Unit test for function lock_decorator
def test_lock_decorator():
    import random
    import threading
    import time

    class TestLock(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._count = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self._count += 1

        @lock_decorator(lock=threading.Lock())
        def decrement(self):
            self._count -= 1

    def thread_do_work(count, t_lock):
        for i in range(count):
            rand_int = random.randint(0, 1)
            if rand_int == 0:
                t_lock.increment()
            else:
                t_lock.decrement()

    count = 100
    t_lock = TestLock()

    threads = []

# Generated at 2022-06-13 16:44:20.039708
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading
    
    test_lock = threading.Lock()
    
    @lock_decorator(attr='_test_lock')
    def test_method_self(self):
        self.called = True
    
    @lock_decorator
    def test_method_lock(lock):
        lock.called = True
    
    class TestClass(object):
        _test_lock = test_lock
        called = False

    t = TestClass()
    test_method_lock(test_lock)
    assert test_lock.called
    assert not t.called
    test_method_self(t)
    assert t.called

# Generated at 2022-06-13 16:44:29.732176
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.count = 0

        @lock_decorator(attr='_lock')
        def method1(self):
            self.count += 1

        @lock_decorator(lock=self._lock)
        def method2(self):
            self.count += 1

    t = Test()
    assert t.count == 0

    t.method1()
    assert t.count == 1

    t.method2()
    assert t.count == 2

# Generated at 2022-06-13 16:44:38.610074
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.data = 0

        @lock_decorator(attr='_callback_lock')
        def method(self, data):
            self.data = data

    class TestClass2(object):
        @lock_decorator(lock=threading.Lock())
        def method(self, data):
            self.data = data

    t = TestClass()
    t.method(1)
    assert(t.data == 1)

    t = TestClass2()
    t.method(2)
    assert(t.data == 2)

    return True

# Generated at 2022-06-13 16:44:44.837598
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    # When using attr
    class C:
        def __init__(self):
            self._lock = lock
        @lock_decorator(attr='_lock')
        def f(self, a, b):
            return a, b
    c = C()
    assert c.f(1, 2) == (1, 2)

    # When using lock
    class D:
        @lock_decorator(lock=lock)
        def f(self, a, b):
            return a, b
    d = D()
    assert d.f(1, 2) == (1, 2)

# Generated at 2022-06-13 16:44:55.016898
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Foo(object):

        def __init__(self):
            self._callback_lock = threading.Lock()
            self.access_counter = 0

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, method, event_name, **kwargs):
            self.access_counter += 1

        @lock_decorator(lock=threading.Lock())
        def some_method(self, event_name, **kwargs):
            self.access_counter += 1

    foo = Foo()
    callback_lock = foo._callback_lock
    callback_lock.acquire()
    thread1 = threading.Thread(target=foo.send_callback, args=('get_callback',))

# Generated at 2022-06-13 16:45:03.918568
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class _Test(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            print('send_callback')

        @lock_decorator(lock=threading.Lock())
        def some_method(self):
            print('some_method')

    instance1_send_callback_expected_calls = [
        'send_callback',
    ]

    instance2_some_method_expected_calls = [
        'some_method',
    ]

    def _test_method_helper(t, l, e):
        calls = []
        while l:
            t()
            calls.append(e.pop(0))
            l -= 1


# Generated at 2022-06-13 16:45:08.852116
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    # Example usage of lock_decorator
    class Example(object):
        def __init__(self):
            self.lock = lock = threading.Lock()
            self.values = []

        @lock_decorator()
        def send_callback(self, item):
            self.values.append(item)

        @lock_decorator(lock=self.lock)
        def add_value(self, item):
            self.values.append(item)

        @lock_decorator(attr='lock')
        def add_value_with_attr(self, item):
            self.values.append(item)

    # instance of test class
    t = Example()

    # Add values to the values list sequentially
    t.add_value('a')
    t.add_value('b')

# Generated at 2022-06-13 16:45:16.051039
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    @lock_decorator()
    def fail():
        assert False, 'This function should not be called without a lock'

    @lock_decorator(lock=lock)
    def succeed(value):
        return value

    assert fail() is None, 'lock_decorator should return None without a lock'

    with lock:
        assert succeed(True) is True, 'lock_decorator should return result with a lock'

# Generated at 2022-06-13 16:45:24.695092
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class SomeClass(object):
        @lock_decorator(attr='lock')
        def attribute_lock(self):
            return True

        @lock_decorator(lock=threading.Lock())
        def explicit_lock(self):
            return True

    class OtherClass(object):
        @lock_decorator(attr='lock')
        @staticmethod
        def attribute_lock():
            return True

        @lock_decorator(lock=threading.Lock())
        @staticmethod
        def explicit_lock():
            return True

    assert SomeClass().attribute_lock()
    assert SomeClass().explicit_lock()

    assert OtherClass.attribute_lock()
    assert OtherClass.explicit_lock()