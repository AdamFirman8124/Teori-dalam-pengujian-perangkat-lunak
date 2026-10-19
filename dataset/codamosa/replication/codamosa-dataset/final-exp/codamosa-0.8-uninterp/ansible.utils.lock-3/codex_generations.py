

# Generated at 2022-06-13 16:35:59.977057
# Unit test for function lock_decorator
def test_lock_decorator():
    class LockClass(object):
        def __init__(self, lock_object=None):
            if lock_object is None:
                import threading
                lock_object = threading.Lock()
            self.lock_object = lock_object

        @lock_decorator(attr='lock_object')
        def locked_method(self):
            return True

    assert LockClass().locked_method()

    @lock_decorator(lock=LockClass().lock_object)
    def global_func():
        return True

    assert global_func()

# Generated at 2022-06-13 16:36:07.202758
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    Test case for function lock_decorator
    '''
    import threading
    class _Test(object):
        '''Test class'''
        def __init__(self):
            # Lock attr
            self.lock_attr = threading.Lock()
        @lock_decorator()
        def no_attr(self):
            '''No lock attribute'''
        @lock_decorator(lock=threading.Lock())
        def no_self(self):
            '''No self'''
        @lock_decorator(attr='lock_attr')
        def lock_attr(self):
            '''Lock attribute'''
    _test = _Test()
    _test.no_attr()
    _test.no_self()
    _test.lock_attr()
    assert True

# Generated at 2022-06-13 16:36:18.475182
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    try:
        import unittest.mock
        mockfixture = True
    except ImportError:
        import mock
        mockfixture = False
    import threading
    import queue

    class MockLock(object):
        def __enter__(self):
            pass

        def __exit__(self, *args):
            pass

    class TestLockDecorator(unittest.TestCase):
        def build_mock_func(self, attr):
            if mockfixture:
                return unittest.mock.MagicMock(return_value=attr)
            else:
                return mock.MagicMock(return_value=attr)


# Generated at 2022-06-13 16:36:28.703030
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestLock():
        """Lock implementation for testing"""

        def __init__(self):
            self.acquire_count = 0
            self.release_count = 0

        def __enter__(self):
            self.acquire_count += 1

        def __exit__(self, exc_type, exc_val, exc_tb):
            self.release_count += 1


    class TestClass():
        """Class with methods that use lock_decorator"""

        def __init__(self):
            self._lock = TestLock()
            self._l = threading.Lock()
            self.count = 0

        @lock_decorator(lock=self._l)
        def some_method(self):
            self.count += 1
            time.sleep(0.25)


# Generated at 2022-06-13 16:36:37.498580
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from threading import Semaphore

    class A(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._sem = Semaphore(1)
            self._val = None

        @lock_decorator('_lock')
        def method(self, val):
            self._val = val

        @lock_decorator(lock=threading.Lock())
        def method_default(self, val):
            self._val = val

        @lock_decorator(lock=self._sem)
        def method_passed(self, val):
            self._val = val

    def verify(obj, val):
        # This should take long enough for threads to pile up
        import time
        time.sleep(0.05)
        assert obj._val == val

# Generated at 2022-06-13 16:36:46.664846
# Unit test for function lock_decorator
def test_lock_decorator():

    class TestLockDecorator(object):
        def __init__(self):
            # This lock is used globally in all instances of this class
            self.global_lock = lock = threading.Lock()
            self.global_counter = 0

            # This lock is used as an instance attribute
            self._counter_lock = lock = threading.Lock()
            self.counter = 0

            @lock_decorator(attr='_counter_lock')
            def _count(self):
                # This lock is only used in this method
                with threading.Lock():
                    self.counter += 1

            @lock_decorator()
            def _count_default(self):
                # This lock is only used in this method
                with threading.Lock():
                    self.counter += 1


# Generated at 2022-06-13 16:36:52.262137
# Unit test for function lock_decorator
def test_lock_decorator():
    class Test(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method(self):
            pass

    t = Test()
    assert t.method.__name__ == 'method'
    assert t.method.__doc__ == 'decorated method'
    assert t.method.__module__ == 'test_lock_decorator'

# Generated at 2022-06-13 16:36:59.557933
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Test the lock decorator

    This is used in the unit tests for ``module_utils.basic``.

    This test is not intended to test the entire code path for
    the decorator, just to provide sample usage and to ensure
    that it can be used as expected.
    '''
    import threading
    from threading import Lock, Thread
    import time

    # Create a lock object to pass to the decorator
    lock = Lock()

    class TestThread(Thread):
        '''Create a class that extends ``Thread`` for testing the
        decorator
        '''
        def __init__(self, *args, **kwargs):
            self._lock = Lock()
            super(TestThread, self).__init__(*args, **kwargs)


# Generated at 2022-06-13 16:37:04.378454
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        def __init__(self):
            self.l = 0
            self.l2 = 0
            self.l3 = 0

        @lock_decorator(attr='_lock')
        def locked(self):
            self.l += 1
            return self.l

        @lock_decorator(lock=threading.Lock())
        def locked2(self):
            self.l2 += 1
            return self.l2

    test = Test()
    test._lock = threading.Lock()

    for i in range(10):
        a = threading.Thread(target=test.locked)
        a.start()

    for i in range(10):
        b = threading.Thread(target=test.locked2)
        b.start()


# Generated at 2022-06-13 16:37:10.324330
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import mock
    from threading import Lock

    class A(object):
        def __init__(self):
            self._lock = Lock()

    class A2(A):
        @lock_decorator(attr='_lock')
        def method(self):
            return 42

    class A3(object):
        @lock_decorator(lock=Lock())
        def method(self):
            return 42

    with mock.patch('threading.Lock'):
        lock_decorator()

    with unittest.TestCase(A2().method()):
        self.assertEqual(A2().method(), 42)

    with unittest.TestCase(A3().method()):
        self.assertEqual(A2().method(), 42)

# Generated at 2022-06-13 16:37:24.545569
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class Obj(object):
        def __init__(self):
            self.counter = 0
            self.num_threads = 20
            self.threads = []
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def increment_counter(self):
            self.counter += 1

        def run(self):
            # Start threads
            for _ in range(self.num_threads):
                t = threading.Thread(target=self.increment_counter)
                t.daemon = True
                t.start()
                self.threads.append(t)

            # Wait for threads to finish
            for t in self.threads:
                t.join()

    obj = Obj()
    obj.run()


# Generated at 2022-06-13 16:37:35.735536
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep

    class TestClass(object):
        def __init__(self, lock=None):
            self._lock = threading.Lock() if lock is None else lock
            self._callback_lock = threading.Lock()

        def __repr__(self):
            return '<TestClass(x={}, y={})>'.format(self.x, self.y)

        @lock_decorator(lock=threading.Lock())
        def some_function(self):
            self.x += 1

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            self.y += 1

        @property
        def x(self):
            with self._lock:
                return self._x


# Generated at 2022-06-13 16:37:39.781633
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    if sys.version_info[0] == 2:
        import thread
        import threading

        class A(threading.Thread):
            def __init__(self):
                super(A, self).__init__()
                self.lock = threading.Lock()
                self.counter = 0

            @lock_decorator(attr="lock")
            def increase(self):
                self.counter += 1

            def run(self):
                for i in range(5):
                    self.increase()

        a = A()
        b = A()

        for t in (a, b):
            t.start()

        for t in (a, b):
            t.join()

        assert a.counter == b.counter == 5


# Generated at 2022-06-13 16:37:45.957841
# Unit test for function lock_decorator
def test_lock_decorator():
    # Basic (positive) test
    class Foo(object):
        _lock = None

        def __init__(self):
            self._lock = lock_decorator(attr='_lock')

        @_lock
        def some_method(self):
            return 'test'

    foo = Foo()
    assert foo.some_method() == 'test'

    # Basic (negative) test
    foo = Foo()
    class Bar(object):
        pass

    with pytest.raises(AttributeError):
        bar = Bar()
        bar.some_method()

# Generated at 2022-06-13 16:37:54.445879
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class MyClass(object):
        def __init__(self, value):
            self.value = value
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def get_value(self):
            return self.value

    class MyClass2(object):
        def __init__(self, value):
            self.value = value
            self._lock = threading.Lock()

        @lock_decorator(lock=threading.Lock())
        def get_value(self):
            return self.value

    c1 = MyClass(5)
    assert c1.get_value() == 5

    c2 = MyClass2(25)
    assert c2.get_value() == 25

# Generated at 2022-06-13 16:38:04.432374
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    class Base(object):

        lock_attr = 'lock'

        def __init__(self):
            self.lock = 10
            self.count = 0

        @lock_decorator(attr=lock_attr)
        def increment(self):
            self.count += 1

    class Inherited(Base):

        def __init__(self):
            # Base.__init__ is *not* called here
            # so we don't have a "lock" attribute
            self.count = 0

        @lock_decorator(attr=lock_attr)
        def decrement(self):
            self.count -= 1

    class Explicit(object):
        '''This uses an explicit lock, instead of an
        instance attribute'''

        def __init__(self):
            self.lock = 10
            self

# Generated at 2022-06-13 16:38:13.045717
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading

    class TestClass(object):
        def __init__(self, attr_lock=False):
            self.calls = []
            if attr_lock:
                self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_attr_lock(self):
            self.calls.append(1)

        @lock_decorator(lock=threading.Lock())
        def test_passed_lock(self):
            self.calls.append(2)

    # Does it lock when using an attribute?
    fail = False
    test_obj = TestClass(attr_lock=True)
    for _ in range(100):
        t = threading.Thread(target=test_obj.test_attr_lock)
        t

# Generated at 2022-06-13 16:38:20.260028
# Unit test for function lock_decorator
def test_lock_decorator():

    # Start by creating a class for testing
    class TestLock(object):
        def __init__(self):
            self.expected = []

        def test_method(self, expected):
            actual = self.actual
            self.expected = []
            self.actual = []
            assert actual == expected, \
                "Lock decorator did not behave correctly " \
                "expected {0}, got {1}".format(expected, actual)

        @lock_decorator(attr='_lock', lock=None)
        def _test_method_a(self, arg):
            self.actual.append(arg)

        @lock_decorator(attr='_lock')
        def _test_method_b(self, arg):
            self.actual.append(arg)


# Generated at 2022-06-13 16:38:30.410816
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        lock = threading.Lock()

        @lock_decorator(attr='lock')
        def method_one(self):
            return True

        @lock_decorator(attr='lock')
        def method_two(self):
            return False

        @lock_decorator(lock=threading.Lock())
        def method_three(self):
            return True

        @lock_decorator(lock=threading.Lock())
        def method_four(self):
            return False

    t = Test()
    assert t.method_one()
    assert not t.method_two()
    assert t.method_three()
    assert not t.method_four()



# Generated at 2022-06-13 16:38:35.129287
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):
        _lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def foo(self):
            return True

    class Bar(object):
        _lock = threading.Lock()
        @lock_decorator(lock=Bar._lock)
        def bar(self):
            return True

    foo = Foo()
    bar = Bar()

    assert foo.foo()
    assert bar.bar()

# Generated at 2022-06-13 16:38:47.992798
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading

    # This is the test lock
    lock = threading.Lock()

    # the attachment point for the lock
    lock_attr = '_lock'

    # The locked method we are testing.
    @lock_decorator(attr='_lock')
    def locked_method_attr(self, value):
        '''Method that is locked.
        '''
        assert hasattr(self, lock_attr)
        return value

    # The locked method we are testing.
    @lock_decorator(lock=lock)
    def locked_method(value):
        '''Method that is locked.
        '''
        return value

    class LockedObject():
        def __init__(self):
            setattr(self, lock_attr, lock)


# Generated at 2022-06-13 16:38:57.833887
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    class TestClass(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_that_uses_attr(self):
            self.result = True

        @lock_decorator(lock=lock)
        def test_that_uses_explicit_lock(self):
            self.result = True

    def thread_test(instance):
        for i in range(100):
            with lock:
                instance.test_that_uses_attr()
                instance.test_that_uses_explicit_lock()

            assert instance.result

    instance = TestClass()
    instance.result = False

    threads = []

# Generated at 2022-06-13 16:39:07.114795
# Unit test for function lock_decorator
def test_lock_decorator():

    import pytest
    from threading import Lock

    class TestClass(object):
        def __init__(self, *args, **kwargs):
            self._lock = Lock()

        @lock_decorator(attr='_lock')
        def foo(*args, **kwargs):
            print('foo')

        @lock_decorator(lock=Lock())
        def bar(*args, **kwargs):
            print('bar')


    with pytest.raises(AttributeError):
        @lock_decorator(attr='missing_lock_attr')
        def missing_lock_attr(*args, **kwargs):
            print('foo')

    with pytest.raises(TypeError):
        @lock_decorator()
        def missing_lock_attr(*args, **kwargs):
            print('foo')

   

# Generated at 2022-06-13 16:39:16.579222
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo(object):
        def __init__(self, lock=None):
            if lock is None:
                self._lock = threading.RLock()
            else:
                self._lock = lock

        @lock_decorator(attr='_lock')
        def method(self, *args, **kwargs):
            pass

    f = Foo()

    # Supplied lock object
    lock = threading.Lock()
    f = Foo(lock=lock)
    assert f._lock is lock

    # Default lock instance
    assert isinstance(f._lock, threading.RLock)

    # Decorated method
    assert f.method is Foo.method

    # This method does nothing, but it is tested below
    class Foo(object):
        def __init__(self):
            self._lock = threading.RLock

# Generated at 2022-06-13 16:39:27.872816
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Unit test for function lock_decorator'''
    import threading
    from multiprocessing import Process
    from time import time

    class Test(object):
        def __init__(self):
            self._attr_lock = threading.Lock()
            self._attr_count = 0
            self._lock_count = 0
            self._lock = threading.Lock()

        @lock_decorator(attr='_attr_lock')
        @property
        def attr_count(self):
            self._attr_count += 1
            return self._attr_count

        @attr_count.setter
        @lock_decorator(attr='_attr_lock')
        def attr_count(self, value):
            self._attr_count = value


# Generated at 2022-06-13 16:39:33.417656
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class Foo(object):
        def __init__(self):
            self._queue_lock = threading.Lock()
            self._queue = []

        @lock_decorator(attr='_queue_lock')
        def queue(self, value):
            self._queue.append(value)

    foo_instance = Foo()
    foo_instance.queue('foo')

    assert foo_instance._queue == ['foo']

# Generated at 2022-06-13 16:39:42.787916
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    # This test is a bit non-traditional because it uses threads to
    # simulate concurrent access to the decorator.

    class LockTest(object):
        _lock_value_lock = threading.Lock()

        @lock_decorator(attr='_lock_value_lock')
        def get_lock_value(self):
            return self._lock_value

        def set_lock_value(self, value):
            with self._lock_value_lock:
                self._lock_value = value

    class Lock2Test(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(lock=self._lock)
        def get_lock_value(self):
            return self._lock_value


# Generated at 2022-06-13 16:39:55.337268
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test:
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator()
        def method1(self, a):
            return a

        @lock_decorator(attr='_lock')
        def method2(self, a):
            return a

        @lock_decorator(lock=threading.Lock())
        def method3(self, a):
            return a

        @lock_decorator(lock=threading.Lock())
        def method4(self, a):
            return a

        @property
        @lock_decorator()
        def prop1(self):
            return self._prop1

        @prop1.setter
        @lock_decorator()
        def prop1(self, value):
            self._

# Generated at 2022-06-13 16:39:58.409409
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()

    def dummy():
        lock.acquire()

    def test(lock):
        wrapped = lock_decorator(lock=lock)(dummy)
        wrapped()

    yield test, lock

# Generated at 2022-06-13 16:40:06.421248
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    lock_attr = threading.Lock()
    counter_attr = 0
    counter = 0

    class Foo(object):
        @lock_decorator(attr='lock')
        def add_self_1(self, count):
            self.lock_counter += count

        @lock_decorator(attr='missing_attr')
        def add_self_2(self, count):
            self.counter += count

        @lock_decorator(lock=lock_attr)
        def add_self_3(self, count):
            self.lock_counter += count

        @lock_decorator(lock=lock)
        def add_self_4(self, count):
            self.counter += count

        @property
        def counter(self):
            return self._

# Generated at 2022-06-13 16:40:24.789308
# Unit test for function lock_decorator
def test_lock_decorator():
    lock = threading.Lock()
    lock_attr = '_lock_attr'
    class Obj:
        def __init__(self):
            self.attr = None
            self.set_attr = lock_decorator(lock=lock)
            self.set_attr_lock = lock_decorator(attr=lock_attr)
            self._lock_attr = threading.Lock()
            self.no_lock = lock_decorator()
        @lock_decorator(lock=lock)
        def test1(self, a, b, c, d=None):
            return a, b, c, d
        @lock_decorator(attr=lock_attr)
        def test2(self, a, b, c, d=None):
            return a, b, c, d

# Generated at 2022-06-13 16:40:31.189082
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    cls = type('MyClass', (object,), {})
    cls.lock = threading.Lock()

    @lock_decorator(attr='lock')
    def test_method(self):
        '''Test lock_decorator'''
        cls.result = 'success'

    cls.result = 'fail'
    cls.test_method()
    assert(cls.result == 'success')

# Generated at 2022-06-13 16:40:37.974487
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class MyClass(object):
        lock = threading.Lock()

        @lock_decorator(lock=lock)
        def method(self):
            pass

        @classmethod
        @lock_decorator(lock=lock)
        def clsmethod(cls):
            pass

    inst = MyClass()
    assert inst.method() is None
    assert inst.clsmethod() is None

# Generated at 2022-06-13 16:40:44.319941
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading

    @lock_decorator(lock=threading.Lock())
    def locked_method(arg):
        return arg

    assert locked_method([]) == []

    class Test(object):

        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def locked_method(self, arg):
            return arg

        def __call__(self, arg):
            return self.locked_method(arg)

    t = Test()
    assert t([]) == [], 'Test class should work as expected'

    # Error case testing
    with pytest.raises(AttributeError):
        @lock_decorator(attr='_non_existent_lock')
        def shouldnt_work():
            pass


# Generated at 2022-06-13 16:40:50.787218
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        _lock = threading.Lock()
        _call_count = 0

        @lock_decorator(attr='_lock')
        def call_me(self):
            self._call_count += 1

    t1 = Test()
    t2 = Test()
    t1.call_me()
    assert t1._call_count == 1, 'function without lock failed'
    t2.call_me()
    assert t2._call_count == 1, 'function without lock failed'

# Generated at 2022-06-13 16:41:00.834622
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    def get_attr(self):
        return self._attr

    def set_attr(self, attr):
        self._attr = attr

    def noop(self):
        pass

    class TestClass(object):
        def __init__(self):
            self.lock = threading.Lock()
            self._attr = ''

        @lock_decorator(attr='lock')
        def use_attr_lock(self):
            pass

        @lock_decorator(lock=threading.Lock())
        def use_decorator_lock(self):
            pass

    tc = TestClass()
    assert lock_decorator(lock=tc.lock)(get_attr)(tc) == ''
    assert lock_decorator(lock=tc.lock)(set_attr)(tc, 'Hello!')

# Generated at 2022-06-13 16:41:07.426063
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        def __init__(self):
            self.a = 'original'
            self.lock = threading.Lock()
            self.b = 'original'

        @lock_decorator(attr='lock', )
        def change_a(self):
            self.a = 'changed'

        @lock_decorator(lock=threading.Lock())
        def change_b(self):
            self.b = 'changed'

    obj = TestClass()
    assert obj.a == 'original'
    assert obj.b == 'original'
    obj.change_a()
    obj.change_b()
    assert obj.a == 'changed'
    assert obj.b == 'changed'

# Generated at 2022-06-13 16:41:17.053987
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import nose

    class TestThread(threading.Thread):
        def __init__(self, lock, shared_data_dicts):
            super(TestThread, self).__init__()
            self.lock = lock
            self.shared_data_dicts = shared_data_dicts

        def run(self):
            with self.lock:
                self.shared_data_dicts['data']['time'] = time.time()
                self.shared_data_dicts['data']['thread'] = threading.currentThread().name

    shared_data_dicts = {
        'data': {
            'time': 0,
            'thread': None
        }
    }

    lock = threading.Lock()


# Generated at 2022-06-13 16:41:26.955043
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock
    from threading import Thread
    from time import time


    class Test(object):
        def __init__(self):
            self._lock = Lock()
            self.start = time()

        @lock_decorator(lock=Lock())
        def task_with_locally_defined_lock(self):
            print('One: %s' % (time() - self.start))

        @lock_decorator(attr='_lock')
        def task_with_instance_lock(self):
            print('Two: %s' % (time() - self.start))


    thread1 = Thread(target=Test().task_with_locally_defined_lock)
    thread2 = Thread(target=Test().task_with_locally_defined_lock)

# Generated at 2022-06-13 16:41:37.370837
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    if sys.version_info[0] > 2:
        from unittest.mock import Mock
    else:
        from mock import Mock
    from threading import Thread
    import time

    method = Mock()
    method.__name__ = 'method'

    class Host():
        def __init__(self):
            self._lock = 'lock'

        @lock_decorator(attr='_lock', lock=None)
        def decorated_method(self):
            return self._lock

    class Host2():
        @lock_decorator(attr='missing_lock_attr', lock=None)
        def decorated_method(self):
            return self._lock

    h = Host()
    assert h.decorated_method() == 'lock'

    h2 = Host2()

# Generated at 2022-06-13 16:41:58.840837
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    call_counter = 0

    # Check that it works with a lock object passed in
    @lock_decorator(lock=lock)
    def check_lock_object():
        nonlocal call_counter
        call_counter += 1

    check_lock_object()
    assert call_counter == 1

    # Check it works with an attribute passed in
    class LockableClass(object):
        _lock = threading.Lock()

    @lock_decorator(attr='_lock')
    def check_lock_attr(obj):
        nonlocal call_counter
        call_counter += 1

    obj = LockableClass()
    check_lock_attr(obj)
    assert call_counter == 2

# Generated at 2022-06-13 16:42:02.890073
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    # Make a class with a lock
    class T(object):
        def __init__(self):
            self.value = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def set_value(self):
            # Should be 1 when done
            self.value += 1

    obj = T()

    # Check function works before locking
    obj.set_value()
    assert obj.value == 1

    # Check that locking works
    # The ``set_value`` function currently has the ``lock_decorator``
    # on it, so it should always return 1, even if we call it multiple
    # times in multiple threads
    import multiprocessing.pool
    pool = multiprocessing.pool.ThreadPool(10)
    result = pool.map

# Generated at 2022-06-13 16:42:08.860533
# Unit test for function lock_decorator
def test_lock_decorator():

    class Dummy(object):
        lock = None

        @lock_decorator(attr='lock')
        def foo(self):
            return 'bar'

    class Dummy2(object):
        lock = None

        @lock_decorator(lock=Dummy.lock)
        def foo(self):
            return 'bar'

    dummy = Dummy()
    dummy.lock = threading.Lock()
    dummy2 = Dummy2()

    assert dummy.foo() == 'bar'
    assert dummy2.foo() == 'bar'

# Generated at 2022-06-13 16:42:18.975227
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class CallbackManager:
        def __init__(self, callback_lock=None):
            if callback_lock is None:
                callback_lock = threading.Lock()
            self._callback_lock = callback_lock
            self._cl = []

        @lock_decorator(attr='_callback_lock')
        def add_callback(self, callback, *args):
            self._cl.append((callback, args))

        @lock_decorator(attr='_callback_lock')
        def run_callbacks(self):
            for callback, args in self._cl:
                callback(*args)

    cl = CallbackManager()
    call_num = [0]

    def callback(n, x=None):
        call_num[0] += 1

# Generated at 2022-06-13 16:42:22.917567
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._counter = 0

        @lock_decorator(attr='_lock')
        def test_method(self):
            self._counter += 1

    t = Test()
    t.test_method()
    assert t._counter == 1



# Generated at 2022-06-13 16:42:32.940304
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._called_with = None
            self._call_count = 0

        @lock_decorator(attr='_lock')
        def foo(self, arg):
            self._called_with = arg
            self._call_count += 1

        # This is redundant, but allows us to test passing the lock explicitly
        @lock_decorator(lock=self._lock)
        def bar(self, arg):
            self._called_with = arg
            self._call_count += 1

    # Ensure that multiple threads don't trample variable values
    test = Test()

    from threading import Thread
    threads = []

# Generated at 2022-06-13 16:42:44.270618
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    def _new_lock_attribute():
        return threading.Lock()

    def _some_method(self):
        self._some_method_called = True
        return True

    def _some_method_with_mock_lock(self):
        self._some_method_called = True
        return True

    def _some_method_with_decorated_mock_lock(self):
        self._some_method_called = True
        return True

    def _some_method_with_decorated_inner_mock_lock(self):
        self._some_method_called = True
        return True

    class TestLockDecorator(unittest.TestCase):
        def setUp(self):
            self._some_method_called = False
            self._lock

# Generated at 2022-06-13 16:42:53.618970
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._counter = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self._counter += 1

    @lock_decorator(lock=threading.Lock())
    def increment():
        Test.increment()

    def run():
        t = Test()
        for _ in range(1000):
            t.increment()
        for _ in range(1000):
            increment()

    thread1 = threading.Thread(target=run)
    thread2 = threading.Thread(target=run)
    thread3 = threading.Thread(target=run)
    threads = []

# Generated at 2022-06-13 16:43:03.987421
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    # All of these examples use threading.Lock, but could be any lock
    # object that functions as a context manager.

    # Initialization
    lock = threading.Lock()


    @lock_decorator(lock=lock)
    def plain_method(value):
        print('plain_method got value: {}'.format(value))
        time.sleep(1)


    class A:
        def __init__(self):
            # This is defined on the class so it is shared across all instances
            self._lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def plain_method(self, value):
            print('plain_method got value: {}'.format(value))
            time.sleep(1)



# Generated at 2022-06-13 16:43:12.498344
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    counter = 0

    class Target(object):
        @property
        def lock(self):
            return self._lock

        @property
        def counter(self):
            return self._counter

        @lock_decorator(attr='_lock')
        def test(self):
            self._counter += 1

        def __init__(self, attr):
            self._lock = attr

    class Test(Target):
        def __init__(self, attr):
            super(Test, self).__init__(attr)
            self._counter = counter

    @lock_decorator(lock=threading.Lock())
    def test_decorator(lock):
        global counter
        with lock:
            counter += 1
            return counter


# Generated at 2022-06-13 16:43:54.489442
# Unit test for function lock_decorator
def test_lock_decorator():
    import random
    import threading

    class A(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator()
        def a(self):
            return 'a'

        @lock_decorator(attr='_lock')
        def b(self):
            return 'b'

    lock = threading.Lock()
    class B(object):
        @lock_decorator(lock=lock)
        def c(self):
            return 'c'

    a = A()
    b = B()
    d = [a.a, a.b, b.c]

    def loop(method):
        return method()

    threads = []
    for method in d:
        t = threading.Thread(target=loop, args=(method, ))
       

# Generated at 2022-06-13 16:43:58.257405
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class SomeClass(object):
        _lock = threading.Lock()
        def __init__(self):
            self.value = 42
        @lock_decorator(attr='_lock')
        def incr(self):
            self.value += 1
            return self.value
    obj = SomeClass()
    assert obj.value == 42
    assert obj.incr() == 43

if __name__ == '__main__':
    test_lock_decorator()

# Generated at 2022-06-13 16:44:10.305975
# Unit test for function lock_decorator
def test_lock_decorator():
    from importlib import import_module
    from os.path import dirname
    from tempfile import mkdtemp
    from shutil import rmtree
    import sys
    import copy
    import collections

    mock = import_module('mock')
    temp_path = mkdtemp(prefix='ansible-test-lock-decorator')

    if temp_path not in sys.path:
        sys.path.append(temp_path)

    # Create a fake ``ansible`` module so we can import plugins
    ansible_module = collections.namedtuple('FakeAnsibleModule', [
        'fail_json', 'exit_json', 'params', 'run_command'])


# Generated at 2022-06-13 16:44:16.492078
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test():
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback1(self):
            return 1

        @lock_decorator(lock=threading.Lock())
        def send_callback2(self):
            return 2

    t = Test()
    assert t.send_callback1() == 1
    assert t.send_callback2() == 2



# Generated at 2022-06-13 16:44:27.620946
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Basic self-tests for lock_decorator'''
    import threading

    class TestClass(object):
        def __init__(self):
            self._lock = None
            self._lock_attr = threading.Lock()
            self._lock_object = threading.Lock()
            self._called = 0

        @lock_decorator(attr='_lock')
        def foo(self):
            assert self._lock is None
            self._called += 1

        @lock_decorator(attr='_lock_attr')
        def bar(self):
            assert self._lock_attr
            self._called += 1

        @lock_decorator(lock=threading.Lock())
        def baz(self):
            assert self._lock_object
            self._called += 1

    obj = TestClass()
   

# Generated at 2022-06-13 16:44:38.301528
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep
    from collections import Counter

    class LockedClass(object):
        # Use a threading.Lock as our lock
        _lock = threading.Lock()

        def __init__(self):
            self.counter = Counter()

        @lock_decorator(attr='_lock')
        def increment(self, item):
            sleep(0.1)
            self.counter[item] += 1

    lc = LockedClass()
    lc.increment('a')
    assert lc.counter == Counter()

    # This should never finish, since we don't release the lock
    # lc._lock.acquire()
    # t = threading.Thread(target=lc.increment, args=('a',))
    # t.daemon = True
    # t.start()
   

# Generated at 2022-06-13 16:44:45.630029
# Unit test for function lock_decorator
def test_lock_decorator():
    import functools
    import threading
    import time

    class MyClass():
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, *args, **kwargs):
            print('Sending callback with lock')
            return

    obj = MyClass()

    # Thread 1 should NOT run until Thread 2 has released the lock
    t1 = threading.Thread(target=obj.send_callback, args=(), kwargs={})
    t1.daemon = True
    t2 = threading.Thread(target=obj.send_callback, args=(), kwargs={})
    t2.daemon = True
    t1.start()
    time.sleep(1)

# Generated at 2022-06-13 16:44:56.975969
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread
    import time

    l = Lock()
    lock_attr = '_lock'

    class Test:
        def __init__(self):
            setattr(self, lock_attr, l)
            self.value = 1

        def __getattr__(self, name):
            return self.value

        @lock_decorator(attr=lock_attr)
        def incr(self, value):
            time.sleep(1)
            self.value += value

    class Test2:
        def __init__(self):
            self.value = 1

        def __getattr__(self, name):
            return self.value

        @lock_decorator(lock=l)
        def incr(self, value):
            time.sleep(1)
            self.value += value



# Generated at 2022-06-13 16:45:02.604513
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        _test_lock = threading.Lock()

        @lock_decorator(attr='_test_lock')
        def method(self):
            return None

        @lock_decorator(lock=threading.Lock())
        def another_method(self):
            return None

    t = Test()

    t.method()
    t.another_method()


if __name__ == '__main__':
    test_lock_decorator()

# Generated at 2022-06-13 16:45:09.610849
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    lock_attr = '_lock_attr'

    mock_obj = MockClass()

    assert mock_obj.lock == 0
    lock_decorator(attr=lock_attr)(mock_obj.method)()
    assert mock_obj.lock == 1

    assert mock_obj.lock == 1
    lock_decorator(lock=lock)(mock_obj.method)()
    assert mock_obj.lock == 2
