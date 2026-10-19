

# Generated at 2022-06-13 16:35:57.240812
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    _lock = threading.Lock()

    class TestClass:
        def __init__(self):
            self._lock = _lock
            self.calls = 0

        @lock_decorator(attr='_lock')
        def foo(self, value):
            self.calls += value

        @lock_decorator(lock=_lock)
        def bar(self, value):
            self.calls += value

    tc = TestClass()
    for _ in range(1000):
        tc.foo(1)
        tc.bar(1)
    assert tc.calls == 2000

# Generated at 2022-06-13 16:36:07.438965
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    attr = '_callback_lock'
    test_dict = {}
    def test_method(*args, **kwargs):
        test_dict['called'] = True
    decorated_callback = lock_decorator(attr=attr)(test_method)
    # No value in ``test_dict`` shows that it was not called
    assert test_dict.get('called', None) is None
    # When the code is called, and ``lock`` is not acquired, an
    # exception should be raised
    try:
        decorated_callback()
    except AssertionError as e:
        assert "Did not acquire lock" in str(e)
    # When the code is called, and ``lock`` is acquired, it's called
    with lock:
        decorated_callback()
    assert test

# Generated at 2022-06-13 16:36:18.780913
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass:
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_lock_decorator_with_attr(self):
            # This should succeed and not raise an Exception because
            # the decorator will use the lock on self
            pass

    test_lock_decorator_with_attr_fails = False
    try:
        TestClass().test_lock_decorator_with_attr()
    except Exception:
        test_lock_decorator_with_attr_fails = True
    assert test_lock_decorator_with_attr_fails is False

    test_lock_decorator_with_attr_fails = True

# Generated at 2022-06-13 16:36:29.191479
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class test:
        _l = None

        @lock_decorator(attr='_l')
        def a(self):
            print('a: ' + self._l)

        @lock_decorator(lock=threading.Lock())
        def b(self):
            print('b')

    t = test()
    assert isinstance(t._l, threading.Lock)

    def thread_test():
        print('starting thread_test')
        t.a()
        print('thread_test a() complete')
        t.b()
        print('thread_test b() complete')

    threading.Thread(target=thread_test).start()
    print('thread spawned')
    t.b()
    print('main thread b() complete')
    t.a()

# Generated at 2022-06-13 16:36:37.680229
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        from threading import Lock
    except ImportError:
        pass
    else:
        lock = Lock()

        class Foobar(object):
            def __init__(self, foo, bar):
                self.foo = foo
                self.bar = bar
                self.lock = Lock()

            @lock_decorator(attr='')
            def method_missing_lock(self):
                return self.foo

            @lock_decorator(attr='lock_doesnt_exist')
            def method_invalid_lock(self):
                return self.foo

            @lock_decorator(lock=lock)
            def method1(self):
                return self.foo

            @lock_decorator()
            def method2(self):
                return self.bar

        f = Foobar(1, 2)

# Generated at 2022-06-13 16:36:46.782449
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import json
    import time

    class NotThreadSafe(object):
        def __init__(self):
            self.counter = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def count(self):
            self.counter += 1
            return self.counter

        @lock_decorator(lock=threading.Lock())
        def count_l(self):
            self.counter += 1
            return self.counter

    def run_threads(ns):
        def _run(ns):
            try:
                ns.count()
                ns.count_l()
            except:
                pass

        threads = [threading.Thread(target=_run, args=(ns,))
                   for i in range(2)]

# Generated at 2022-06-13 16:36:55.572794
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from nose.tools import assert_raises

    class Test():
        def __init__(self):
            self.lock = threading.Lock()
            self.counter = 0

        @lock_decorator(lock=self.lock)
        def locked(self):
            self.counter += 1

    # Create object with lock
    testobj = Test()

    # Check if lock works by launching two threads and
    # making sure counter increases at least twice.
    def runthread():
        """A thread that runs and increments counter"""
        testobj.locked()

    # Last count before we start
    last_count = testobj.counter

    # Run two threads in parallel
    t1 = threading.Thread(target=runthread)
    t2 = threading.Thread(target=runthread)
    t1.start

# Generated at 2022-06-13 16:37:06.063252
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class test_class(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._callback_lock = threading.Lock()
            self._lock_holder = 'nobody'

        @lock_decorator()
        def test_lock_context(self, lock_holder):
            self._lock_holder = lock_holder

        @lock_decorator(attr='_lock')
        def test_lock(self):
            pass

        @lock_decorator(lock=threading.Lock())
        def test_lock_object(self):
            pass

        @lock_decorator(attr='_callback_lock')
        def test_callback(self, lock_holder):
            self._lock_holder = lock_holder

    c = test_class()

   

# Generated at 2022-06-13 16:37:14.640180
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Unit test for lock_decorator'''
    import threading
    class TestLock(object):
        attr = None
        def __init__(self):
            if self.attr is None:
                raise TypeError
        @lock_decorator(attr='attr')
        def test_method(self):
            pass
        @lock_decorator(lock=threading.Lock())
        def test_method2(self):
            pass
    test = TestLock()
    import pytest
    with pytest.raises(TypeError):
        test.test_method()
    test.attr = threading.Lock()
    test.test_method()
    test.test_method2()

# Generated at 2022-06-13 16:37:24.942854
# Unit test for function lock_decorator
def test_lock_decorator():
    '''This function returns ``True`` when the lock_decorator
    function is working as expected.
    '''
    import threading
    import time

    l = threading.Lock()
    # Create an empty class
    class C:
        pass

    counter = 0

    @lock_decorator(lock=l)
    def increment():
        global counter
        counter += 1
        time.sleep(1)

    @lock_decorator(attr='_attr_lock')
    def increment_attr(self):
        global counter
        counter += 1
        time.sleep(1)

    obj = C()
    obj._attr_lock = threading.Lock()

    threads = [threading.Thread(target=increment) for i in range(5)]

# Generated at 2022-06-13 16:37:38.528361
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import sys

    class Example(object):

        _lock = threading.Lock()
        _data = []

        @lock_decorator()
        def add_data(self, item):
            self._data.append(item)
            time.sleep(1)

        @lock_decorator(attr='_lock')
        def add_data_no_args(self, item):
            self._data.append(item)
            time.sleep(1)

        @lock_decorator(lock=_lock)
        def add_data_no_self(self, item):
            self._data.append(item)
            time.sleep(1)

    example = Example()

    assert example._data == []


    # Call three ``add_data`` methods in 3 threads
    threads

# Generated at 2022-06-13 16:37:44.650932
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Unit test for function lock_decorator'''
    import threading
    import mock
    # Create a mock class with a thread lock, so we can mock out
    # the context manager
    class MyClass(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

    obj = MyClass()

    # Now using the lock_decorator, we have to mock out the method
    # being decorated, and we need to mock out the context manager
    # to avoid actually having the lock acquired, but we still want
    # to test that the decorator works as expected.

# Generated at 2022-06-13 16:37:53.952317
# Unit test for function lock_decorator
def test_lock_decorator():

    from threading import Lock

    # Class with a lock
    class MyClass(object):
        def __init__(self):
            self._lock = Lock()
            self.x = 0

        @lock_decorator(attr='_lock')
        def incr(self):
            self.x += 1

    m = MyClass()
    m.incr()
    assert m.x == 1

    # Class without a lock (lock is passed explicitly)
    class MyClass2(object):
        def __init__(self):
            self.x = 0
            self._lock = Lock()

        @lock_decorator(lock=self._lock)
        def incr(self):
            self.x += 1

    m = MyClass2()
    m.incr()
    assert m.x == 1

    # Class

# Generated at 2022-06-13 16:38:03.711546
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import random

    class NoLock:
        """A bare class to test that lock_decorator can be used
        without any locking context.
        """

    class HasLock:
        """A class with an instance attribute that is a threading.Lock()
        """

        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def some_method(self, msg):
            print(msg)

    class HasLockAndNoLock:
        """A class with two instance methods. The first method,
        has_lock(), is protected by lock_decorator using an instance
        attribute. The second method, no_lock(), is unprotected
        """

        def __init__(self):
            self._lock = threading.Lock()

# Generated at 2022-06-13 16:38:12.304757
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestLockDecorator(object):
        def __init__(self):
            self._test_value = 0
            self._test_lock_attr = threading.Lock()

        @lock_decorator(attr='_test_lock_attr')
        def _test_lock_attr_decorated(self):
            time.sleep(1)
            self._test_value += 1
            return self._test_value

    class TestLockDecoratorExplicit(object):
        def __init__(self):
            self._test_value = 0
            self._test_lock = threading.Lock()

        @lock_decorator(lock=object._test_lock)
        def _test_lock_decorated(self):
            time.sleep(1)
            self._test

# Generated at 2022-06-13 16:38:19.775376
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    _lock = threading.Lock()

    @lock_decorator(attr='_lock')
    def test_lock_decorator_lock_obj(self):
        self._lock.acquire()

    @lock_decorator(lock=lock)
    def test_lock_decorator_no_lock_obj(self):
        lock.acquire()

    class TestLockDecorator(object):
        _lock = _lock

        @lock_decorator(attr='_lock')
        def test_lock_decorator_lock_obj(self):
            self._lock.acquire()

        @lock_decorator(lock=lock)
        def test_lock_decorator_no_lock_obj(self):
            lock.acquire()

# Generated at 2022-06-13 16:38:26.732988
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def test(self):
            return 'test'
        @lock_decorator(lock=lock)
        def lock_test(self):
            return 'lock_test'
    t = Test()
    assert t.test() == 'test'
    assert t.lock_test() == 'lock_test'

# Generated at 2022-06-13 16:38:34.400342
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestingLock(object):
        def __init__(self):
            self.message = 'Found you!'
            self.lock = threading.Lock()

        @lock_decorator()
        def find_me(self):
            time.sleep(1)
            return self.message

        @lock_decorator(lock=threading.Lock())
        def find_me_too(self):
            time.sleep(1)
            return self.message

    testing_lock = TestingLock()

    assert testing_lock.find_me() == 'Found you!'
    assert testing_lock.find_me_too() == 'Found you!'

# Generated at 2022-06-13 16:38:45.392678
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from nose.tools import assert_equal, assert_in, assert_not_in

    # create a threading.Lock()
    lock = threading.Lock()
    class MyClass(object):
        def __init__(self):
            self.value = 0

        @lock_decorator(attr='_lock')
        def method1(self):
            self.value += 1

        @lock_decorator(lock=lock)
        def method2(self):
            self.value += 1

    o = MyClass()
    o.method1()
    assert_equal(o.value, 1)

    o.method2()
    assert_equal(o.value, 2)

    # Tests the lock is in effect
    t1 = threading.Thread(target=o.method1)
    t2

# Generated at 2022-06-13 16:38:55.933649
# Unit test for function lock_decorator
def test_lock_decorator():
    # pylint: disable=line-too-long
    '''function lock_decorator unit tests'''
    import threading
    class MyClass(object):  # pylint: disable=too-few-public-methods
        '''class used for unit testing lock_decorator'''
        def __init__(self):
            self._fl_lock = threading.Lock()
            self._fl_value = 0

        @lock_decorator(attr='_fl_lock')
        def lock_decorator_method(self):
            self._fl_value += 1
            return self._fl_value

    class MyClass2(object):  # pylint: disable=too-few-public-methods
        '''class used for unit testing lock_decorator'''

# Generated at 2022-06-13 16:39:08.719034
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    class MyClass(object):

        _lock = threading.Lock()
        _locked = False

        @lock_decorator(attr='_lock')
        def foo(self):
            self._locked = True
            time.sleep(2)
            self._locked = False

        @lock_decorator(lock=_lock)
        def bar(self):
            self._locked = True
            time.sleep(2)
            self._locked = False

        def _locked_status(self):
            return self._locked

        @lock_decorator(attr='_lock')
        def _set_locked(self, value):
            self._locked = value

        @lock_decorator(lock=_lock)
        def _set_locked_bar(self, value):
            self._

# Generated at 2022-06-13 16:39:20.011639
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    import threading

    if sys.version_info[0] >= 3:
        # Python3 doesn't require this
        from io import StringIO
    else:
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO

    # Build a class to hold the lock, and a method to use it
    class A(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.output = StringIO()

        @lock_decorator(attr='_lock')
        def use_lock(self, text_to_write):
            self.output.write(text_to_write + '\n')

    # Instantiate an object and call ``use_lock`` with a multi-threaded
    # context. This should produce a new

# Generated at 2022-06-13 16:39:30.764553
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    try:
        from unittest.mock import MagicMock
    except ImportError:
        from mock import MagicMock


    class Foo(object):
        def __init__(self):
            self.a = 0
            self.b = 0
            self.lock_a = threading.Lock()
            self.lock_b = threading.Lock()


        @lock_decorator()
        def increment(self):
            self.a += 1
            time.sleep(1)
            self.b += 1
            return

        def increment_a(self):
            with self.lock_a:
                self.a += 1

        def increment_b(self):
            with self.lock_b:
                self.b += 1


    f = Foo()
    assert f

# Generated at 2022-06-13 16:39:41.441544
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    called = []
    @lock_decorator(lock=lock)
    def f():
        called.append(True)
    @lock_decorator(attr='lock')
    def g(self):
        self.called.append(True)
    class Test(object):
        def __init__(self):
            self.lock = lock
            self.called = []
        g = lock_decorator(attr='lock')(g)
    t = Test()
    threads = []
    for i in range(10):
        threads.append(threading.Thread(target=f))
        threads.append(threading.Thread(target=g, args=(t,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread

# Generated at 2022-06-13 16:39:53.223236
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from threading import Lock
    # This is a test class for the lock_decorator
    class TestLock(object):
        # A lock
        lock = Lock()
        @lock_decorator(lock=lock)
        def a_method(self):
            return True
        @lock_decorator(attr='lock')
        def b_method(self):
            return True

    obj = TestLock()
    assert obj.a_method()
    assert obj.b_method()

    e_msg = ('You must supply either an instance attribute'
             ' or a lock object to the lock')

    try:
        @lock_decorator()
        def no_arg_method(self):
            pass
    except TypeError as e:
        assert e_msg in str(e)


# Generated at 2022-06-13 16:40:02.260333
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock
    from ansible.module_utils.six import print_
    from ansible.module_utils.six import StringIO

    class Test(object):
        def __init__(self, lock=None):
            self.data = StringIO()
            self.lock = lock or Lock()

        @lock_decorator(attr='lock')
        def _locked(self, data):
            print_(data, file=self.data)

        @lock_decorator(attr='missing_lock_attr')
        def _locked_missing(self, data):
            print_(data, file=self.data)

        @lock_decorator(attr='lock')
        def _locked_default(self, data='default'):
            print_(data, file=self.data)


# Generated at 2022-06-13 16:40:08.448723
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):

        _lock = threading.Lock()
        _attr_lock = threading.Lock()

        @lock_decorator('_lock')
        def method1(self, data):
            return data

        @lock_decorator(lock=_attr_lock)
        def method2(self, data):
            return data

    obj = Test()
    assert obj.method1('foo') == 'foo'
    assert obj.method2('bar') == 'bar'

# Generated at 2022-06-13 16:40:19.536235
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    class TestLockDecorator(unittest.TestCase):
        def setUp(self):
            import threading
            self._lock = threading.Lock()
            self._attr_lock = threading.Lock()

        @lock_decorator('_lock')
        def wrapped(self):
            return True

        @lock_decorator('_attr_lock')
        def wrapped_attr(self):
            return True

        @lock_decorator(lock=self._lock)
        def wrapped_lock(self):
            return True

        def test_wrapped(self):
            self.assertTrue(self.wrapped())

        def test_wrapped_attr(self):
            self.assertTrue(self.wrapped_attr())

        def test_wrapped_lock(self):
            self

# Generated at 2022-06-13 16:40:29.345149
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock
    from time import sleep
    from ansible.module_utils.basic import AnsibleModule

    def test(self, value, delay=0):
        sleep(delay)
        self.value = value

    class TestLockDecorator:
        def __init__(self):
            self._callback_lock = Lock()
            self.value = None

        @lock_decorator(attr='_callback_lock')
        def test_lock(self, value, delay=0):
            sleep(delay)
            self.value = value

        @lock_decorator(lock=Lock())
        def test_lock2(self, value, delay=0):
            sleep(delay)
            self.value = value

    module = AnsibleModule(argument_spec={})

    test_obj = TestLockDecorator()

# Generated at 2022-06-13 16:40:40.422914
# Unit test for function lock_decorator
def test_lock_decorator():
    '''assert lock_decorator is working'''
    import threading
    class Foo(object):
        def __init__(self):
            self._callback_lock = threading.RLock()
            self.callback_result = 0

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, lock):
            self.callback_result += 1

    # class-level lock
    foo = Foo()
    for _ in range(2):
        threading.Thread(target=foo.send_callback).start()
    assert foo.callback_result == 1
    # instance-level lock
    foo.callback_result = 0
    _lock = threading.Lock()

# Generated at 2022-06-13 16:40:57.588019
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    l = threading.Lock()
    def foo(lock=None):
        with lock:
            pass
    foo = lock_decorator(lock=l)(foo)
    assert isinstance(foo.__closure__, tuple)
    foo = lock_decorator(attr='_lock')(foo)
    assert len(foo.__closure__) == 1
    class bar(object):
        def foo(self, lock=None):
            with lock:
                pass
    b = bar()
    b.foo = lock_decorator(attr='_lock')(bar.foo)
    assert isinstance(b.foo.__closure__, tuple)

# Generated at 2022-06-13 16:41:08.766132
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    try:
        from unittest import mock
    except ImportError:
        import mock

    class TestLock(object):
        def __init__(self):
            self._lock = mock.MagicMock()

        def __call__(self, func):
            @lock_decorator(lock=self._lock)
            @wraps(func)
            def inner(*args, **kwargs):
                return func(*args, **kwargs)
            return inner

        def __enter__(self):
            self._lock.__enter__.return_value = None
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            self._lock.__exit__.return_value = None



# Generated at 2022-06-13 16:41:15.243118
# Unit test for function lock_decorator
def test_lock_decorator():
    class MockClass(object):
        _lock = None

        @lock_decorator(attr='_lock')
        def test_method(self):
            return 'got here'

    class NoAttrMockClass(object):
        @lock_decorator(attr='_lock')
        def test_method(self):
            return 'got here'

    assert MockClass().test_method() == 'got here'
    assert NoAttrMockClass().test_method() == 'got here'

# Generated at 2022-06-13 16:41:25.994496
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    my_lock = threading.Lock()
    test_list = []

    def test_function():
        test_list.append(1)

    @lock_decorator(lock=my_lock)
    def func_using_lock():
        test_function()

    def func_using_lock_wrapper():
        """Wrap the function with the lock_decorator at the function call
        level to ensure that the decorator works correctly.
        """

        @lock_decorator(lock=my_lock)
        def func_using_lock():
            test_function()

        func_using_lock()

    # Test the decorator
    assert not my_lock.locked(), "my_lock is already acquired"
    func_using_lock()

# Generated at 2022-06-13 16:41:36.437927
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    import os
    import shutil
    import tempfile
    import threading
    if sys.version_info[0] == 2:
        from cPickle import Pickler
    else:
        from pickle import Pickler

    lock = threading.Lock()

    class TestLock(object):
        # for some reason, this doesn't work with py3.8 if nonlocal _lock is used
        def __init__(self):
            self._lock = threading.Lock()
            self.value = None
            self.no_lock_value = None
            self.lock_value = None

        @lock_decorator(attr='_lock')
        def do_lock(self, value):
            self.value = value


# Generated at 2022-06-13 16:41:42.163097
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock_obj = threading.Lock()
    class Test(object):
        def __init__(self):
            self.lock_obj = lock_obj
        @lock_decorator(lock=lock_obj)
        def some_method(self):
            return True
        @lock_decorator(attr='lock_obj')
        def some_class_method(self):
            return True

    t = Test()
    assert t.some_method() == True
    assert t.some_class_method() == True

# Generated at 2022-06-13 16:41:43.145324
# Unit test for function lock_decorator
def test_lock_decorator():
    pass

# Generated at 2022-06-13 16:41:55.494054
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    assert lock_decorator is not None
    class aclass(object):
        _callback_lock = threading.Lock()
        def __init__(self):
            self._done = False

        @lock_decorator(attr='_callback_lock')
        def set_done(self):
            assert self._callback_lock.locked()
            self._done = True

        def get_done(self):
            return self._done

    @lock_decorator(lock=threading.Lock())
    def setit(value, a):
        assert a.locked()
        return value

    a = aclass()
    a.set_done()
    assert a.get_done()
    assert setit(True, aclass._callback_lock)

# Generated at 2022-06-13 16:42:00.900726
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class TestLockDecorator(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._shared_resource = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self._shared_resource += 1

    test_lock_decorator = TestLockDecorator()
    test_lock_decorator.increment()
    assert test_lock_decorator._shared_resource == 1

    class TestLockDecoratorLockPassed(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._lock2 = threading.Lock()
            self._shared_resource = 0

        @lock_decorator(lock=self._lock)
        def increment(self):
            self

# Generated at 2022-06-13 16:42:09.900861
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading

    values = []
    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def append_sleep(x):
        time.sleep(x)
        values.append(x)

    @lock_decorator(attr='lock')
    def append_sleep_v2(x):
        time.sleep(x)
        values.append(x)

    thread_1 = threading.Thread(target=append_sleep, args=[1], name='thread_1')
    thread_2 = threading.Thread(target=append_sleep, args=[2], name='thread_2')
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    assert sum(values) == 3

    values

# Generated at 2022-06-13 16:42:35.701607
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread, Lock
    class Test(object):
        def __init__(self):
            self._lock = Lock()
            self.i = 0

        @lock_decorator(attr='_lock')
        def test_lock_attr(self):
            self.i += 1

        @lock_decorator(lock=Lock())
        def test_lock_arg(self):
            self.i += 1

    t = Test()
    def thread(method):
        for _ in range(100):
            method()

    tp = []
    for _ in range(10):
        tp.append(Thread(target=thread, args=(t.test_lock_attr,)))
        tp.append(Thread(target=thread, args=(t.test_lock_arg,)))

# Generated at 2022-06-13 16:42:46.040581
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class LockDecoratorTest(unittest.TestCase):

        def test_lock_decorator(self):
            class Foo(object):
                _lock = threading.Lock()
                _counter = 0

                @lock_decorator(attr='_lock')
                def some_method(self):
                    self._counter += 1

                @lock_decorator(lock=threading.Lock())
                def some_other_method(self):
                    self._counter += 1

                @classmethod
                @lock_decorator(attr='_lock')
                def some_other_method_cls(cls):
                    cls._counter += 1


# Generated at 2022-06-13 16:42:52.666572
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Locker():
        def __init__(self):
            self.lock = threading.Lock()
            self.counter = 0

        @lock_decorator(attr='lock')
        def increment(self):
            self.counter = self.counter + 1

    locker = Locker()
    threads = []
    for _i in range(0, 100):
        threads.append(threading.Thread(target=locker.increment))
    for t in threads:
        t.run()
    for t in threads:
        t.join()
    assert locker.counter == 100

# Generated at 2022-06-13 16:42:56.815117
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass:
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_method(self):
            return

    test = TestClass()
    for i in range(100):
        test.test_method()

# Generated at 2022-06-13 16:43:05.432195
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    import threading

    class Test(object):
        # Create a threading.Lock object
        lock = threading.Lock()

        # Class-level lock attribute
        cls_lock = threading.Lock()

        def __init__(self, attr):
            # Instance-level lock attribute
            self.attr = attr

        # Function using the passed-in lock
        @lock_decorator(lock=lock)
        def lock_decorator_kwarg(self):
            return threading.current_thread().name

        # Function using the instance attribute for the lock
        @lock_decorator(attr='attr')
        def lock_decorator_attr(self):
            return threading.current_thread().name

        # Function using the class attribute for the lock

# Generated at 2022-06-13 16:43:12.497460
# Unit test for function lock_decorator
def test_lock_decorator():
    class MyClass(object):
        def __init__(self):
            self._lock = None

        @lock_decorator(attr='_lock')
        def some_method(self):
            return True

    my = MyClass()
    assert my.some_method() is True

    import threading
    my._lock = threading.Lock()
    assert my.some_method() is True

# Generated at 2022-06-13 16:43:22.198891
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        def __init__(self):
            self.attr = 0
            self.lock = threading.Lock()
            self.attr_lock = threading.Lock()

        @lock_decorator(lock=self.lock)
        def increment(self, num):
            self.attr += num

        @lock_decorator
        def increment_with_explicit_lock(self, num, lock):
            self.attr += num

        @lock_decorator(attr='attr_lock')
        def increment_with_attr_lock(self, num):
            self.attr += num

    # Use a lock on an instance method
    tc = TestClass()
    increment = tc.increment
    increment(1)
    assert tc.attr == 1
    increment(2)


# Generated at 2022-06-13 16:43:31.671994
# Unit test for function lock_decorator
def test_lock_decorator():
    '''This is intended to be the unit test for the `lock_decorator`.'''
    import mock
    import threading
    import contextlib
    class C(object):
        def __init__(self):
            self._test_lock = threading.Lock()

        @lock_decorator(attr='_test_lock')
        def method(self):
            # This call is mocked
            with contextlib.nested(
                mock.patch('threading.Lock.__enter__'),
                mock.patch('threading.Lock.__exit__'),
            ) as (enter, exit):
                # the lock should be an enterable context manager
                enter.assert_called_once_with()
                # the lock should be an exitable context manager
                exit.assert_called_once_with(None, None, None)

   

# Generated at 2022-06-13 16:43:41.778738
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestObj:
        def __init__(self):
            self._lock = threading.Lock()
            self._lock_attr = threading.Lock()

        @lock_decorator(attr='_lock_attr')
        def first_method(self):
            return

        @lock_decorator(lock=self._lock)
        def second_method(self):
            return

    obj = TestObj()
    assert '_lock' in dir(obj)
    assert 'first_method' in dir(obj)
    assert 'second_method' in dir(obj)
    assert obj._lock is not None
    assert obj._lock_attr is not None
    obj.first_method()
    obj.second_method()

# Generated at 2022-06-13 16:43:50.191266
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Example(object):
        def __init__(self, num):
            self._num = num
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def callback(self, num):
            self._num += num
            return self._num

    e = Example(0)
    assert e.callback(1) == 1
    assert e.callback(1) == 2

    class ExampleWithFunc(object):
        def __init__(self, num):
            self._num = num
            self._callback_lock = threading.Lock()

        @lock_decorator(lock=self._callback_lock)
        def callback(self, num):
            self._num += num
            return self._num

    e2 = ExampleWithFunc

# Generated at 2022-06-13 16:44:33.805655
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class A:

        def __init__(self):
            self._callback_lock = threading.Lock()
            self.cb_data = []

        @lock_decorator(attr='_callback_lock')
        def callback_data(self, data):
            self.cb_data.append(data)
            time.sleep(1)

    callback_data = set(['this', 'should', 'be', 'a', 'list'])

    a = A()
    threads = []
    for data in callback_data:
        thread = threading.Thread(target=a.callback_data, args=(data,))
        thread.daemon = True
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


# Generated at 2022-06-13 16:44:42.783277
# Unit test for function lock_decorator
def test_lock_decorator():
    from collections import defaultdict
    from threading import Lock, Thread

    class Test(object):
        def __init__(self):
            # We're using a defaultdict because we want the 'counter'
            # attribute to exist, even if its value is 0
            self._counter = defaultdict(int)
            self._lock = Lock()

        @lock_decorator(attr='_lock')
        def increment(self, key):
            self._counter[key] += 1

        def decrement(self, key):
            self._counter[key] -= 1

    counter = defaultdict(int)
    t = Test()
    for _ in range(100):
        t.increment('test')
    for _ in range(100):
        Thread(target=t.increment, args=('test',)).start()

# Generated at 2022-06-13 16:44:52.812416
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading

    class Foo(object):
        def __init__(self):
            # This is what we're testing
            self._lock = lock_decorator(attr='_lock')
            # We need a lock object
            self.lock = threading.Lock()
            # We need a class attribute to
            # indicate the decorator ran
            self.decorated = False

        @property
        def decorated(self):
            return self._decorated

        @decorated.setter
        def decorated(self, value):
            self._decorated = value

        @property
        def lock(self):
            return self._lock

        @lock.setter
        def lock(self, value):
            self._lock = value


# Generated at 2022-06-13 16:45:02.564846
# Unit test for function lock_decorator
def test_lock_decorator():
    # pylint: disable=unused-variable
    import threading

    class MockedThread(object):
        # pylint: disable=no-self-use
        def __init__(self, *args, **kwargs):
            pass

        def start(self):
            pass

        @staticmethod
        def join():
            pass

    class MockedLock(object):
        # pylint: disable=unused-variable
        def __init__(self, *args, **kwargs):
            pass

        def __enter__(self):
            pass

        def __exit__(self, *args, **kwargs):
            pass

    _called = []

    @lock_decorator(attr='lock')
    def func(self, val):
        _called.append(val)


# Generated at 2022-06-13 16:45:12.566287
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._counter = 0

        @lock_decorator(attr='_lock')
        def increment_counter(self):
            self._counter += 1

        @lock_decorator(lock=threading.Lock())
        def increment_counter_by(self, value):
            self._counter += value

    def threaded_increment(obj):
        for i in range(100):
            obj.increment_counter()

    def threaded_increment_by(obj):
        for i in range(100):
            obj.increment_counter_by(1)

    obj = TestClass()


# Generated at 2022-06-13 16:45:22.863441
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.msg = 'hello'

        @lock_decorator(attr='_lock')
        def get_msg(self):
            return self.msg

        @lock_decorator(lock=threading.Lock())
        def set_msg(self, msg):
            self.msg = msg

    f = Foo()

    def stage1():
        for i in range(50):
            print('msg: {0}'.format(f.get_msg()))
            time.sleep(0.01)
        print(f.get_msg())

    def stage2():
        for i in range(50):
            f.set_msg('world')

# Generated at 2022-06-13 16:45:29.993328
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self, value):
            # use a pre-defined instance attribute
            self._test_lock = threading.Lock()
            self.value = value

        @lock_decorator(attr='_test_lock')
        def test_lock(self, value):
            self.value += value

        # or explicitly supply the lock
        _explicit_lock = threading.Lock()
        @lock_decorator(lock=_explicit_lock)
        def explicit_lock(self, value):
            self.value += value

    t = Test(0)
    t.test_lock(1)
    assert t.value == 1
    t.explicit_lock(1)
    assert t.value == 2

# Generated at 2022-06-13 16:45:37.570294
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    class TestClass(object):
        def __init__(self):
            self.counter = 0
            self.callback_lock = False

        @lock_decorator(attr='callback_lock')
        def callback(self, message):
            self.counter += 1
            time.sleep(1)
            print(message)

    test_obj = TestClass()
    threads = []

    for i in range(10):
        thread = threading.Thread(target=test_obj.callback, args=("thread:%d" % i,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    assert test_obj.counter == 10

# Generated at 2022-06-13 16:45:44.357669
# Unit test for function lock_decorator
def test_lock_decorator():
    import inspect

    import pytest
    class FakeLock:
        def __init__(self):
            self.lock = False
        def __enter__(self):
            self.lock = True
        def __exit__(self, *args):
            self.lock = False

    class TestClass:
        @lock_decorator(lock=FakeLock())
        def locked_method(self):
            # This method should be locked
            assert self.lock.lock

        @lock_decorator(attr='_lock')
        def attr_locked_method(self):
            # This method should be locked
            assert self.lock.lock

    testobj = TestClass()
    testobj._lock = FakeLock()

    # Test function lock_decorator
    testobj.locked_method()
    # Test attr lock_decor

# Generated at 2022-06-13 16:45:54.373211
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading
    from ansible.plugins.loader import callback_loader

    assert hasattr(callback_loader, 'CallbacksBase')
    assert hasattr(callback_loader.CallbacksBase, 'v2_runner_on_ok')
    # Make sure it wasn't already decorated
    assert not hasattr(callback_loader.CallbacksBase, '_callback_lock')
    assert callback_loader.CallbacksBase.v2_runner_on_ok.__name__ == 'v2_runner_on_ok'

    # Do some magic to inject our lock decorator
    # No easy way to mock/patch a decorator