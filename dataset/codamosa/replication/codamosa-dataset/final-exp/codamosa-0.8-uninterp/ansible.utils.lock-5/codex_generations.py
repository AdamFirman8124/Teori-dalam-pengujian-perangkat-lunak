

# Generated at 2022-06-13 16:35:56.979186
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    class TestLock(object):
        def __init__(self):
            self.func_called = False
            self.func_arg = None
        @lock_decorator(attr='_lock', lock=lock)
        def test_func(self, arg):
            self.func_called = True
            self.func_arg = arg
    test = TestLock()
    test.test_func('test')
    assert test.func_called
    assert test.func_arg == 'test'

# Generated at 2022-06-13 16:36:03.373988
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.val = 0

        @lock_decorator(attr='_lock')
        def incr(self):
            sleep(1)
            self.val += 1

    t = Test()
    try:
        assert t.val == 0
        t.incr()
        assert t.val == 1
    except AssertionError:
        raise AssertionError('lock_decorator() unit test failed')

# Generated at 2022-06-13 16:36:07.899376
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    class Test(unittest.TestCase):

        def test_attr_lock(self):
            class TestClass(object):
                def __init__(self):
                    # Set a flag in here so we can verify that we've
                    # actually acquired the lock
                    self._flag = False

                @lock_decorator(attr='_lock')
                def some_method(self):
                    self._flag = True

                @property
                def flag(self):
                    return self._flag

            # Create a lock
            import threading
            my_lock = threading.Lock()
            # Now create an instance of the class
            # Do this *after* the lock is created
            # so that the decorator can get the lock
            test = TestClass()
            # Add the lock as a property

# Generated at 2022-06-13 16:36:19.403299
# Unit test for function lock_decorator
def test_lock_decorator():
    import functools
    import threading

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._attr = 0

        @lock_decorator(attr='_lock')
        def increment_attr(self):
            self._attr += 1

    class Bar(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._attr = 0

        @lock_decorator(lock=self._lock)
        def increment_attr(self):
            self._attr += 1

    class Baz(object):
        _lock = threading.Lock()

        @classmethod
        @lock_decorator(lock=_lock)
        def increment_attr(cls):
            cls._attr += 1


# Generated at 2022-06-13 16:36:29.698744
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep

    class A(object):
        '''Unit test for function lock_decorator'''
        def __init__(self):
            self.lock_attr = 'lock_attr'
            self._attr_lock = threading.Lock()

            self.lock_noattr = 'lock_noattr'
            self._no_lock = threading.Lock()

        @lock_decorator(attr='lock_attr')
        @lock_decorator(lock=self._no_lock)
        def _test_lock(self, lock_arg):
            '''Unit test for function lock_decorator'''
            sleep(1)
            return lock_arg


    # Instantiate class A
    a = A()

    import pytest
    from testinfra.host import Host
   

# Generated at 2022-06-13 16:36:35.933286
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    This function demonstrates how to use the ``lock_decorator``.
    '''
    class MyClass(object):
        def __init__(self):
            self._callback_lock = Lock()

        @lock_decorator(attr='_callback_lock')
        def decorated_method(self, *args, **kwargs):
            print('Inside decorated method')

        def not_decorated_method(self, *args, **kwargs):
            print('Inside not decorated method')

    obj = MyClass()
    obj.decorated_method()
    obj.not_decorated_method()

# Generated at 2022-06-13 16:36:44.343569
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._value = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self._value += 1

    t1 = Test()
    t2 = Test()
    assert t1._value == 0
    assert t2._value == 0

    import threading
    class IncrementerThread(threading.Thread):
        def __init__(self, t):
            self._t = t
            super(IncrementerThread, self).__init__()

        def run(self):
            for i in range(10):
                self._t.increment()

    for i in range(10):
        t1.increment()

# Generated at 2022-06-13 16:36:52.539048
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class example_class(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, data):
            print('{}: {}'.format(self.__class__.__name__, data))


    @lock_decorator(lock=threading.Lock())
    def some_method(data):
        print('function: {}'.format(data))

    ec = example_class()
    ec.send_callback('test')

    some_method('test')

# Generated at 2022-06-13 16:36:59.679240
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.value = 0
        @lock_decorator(attr='_lock')
        def add(self, value):
            self.value += value
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

    test = Test()
    assert test.value == 0
    test.add(1)
    assert test.value == 1
    # Test lock_decorator with a lock in a with statement
    with test:
        test.add(1)
    assert test.value == 2
    # Test lock_decorator via lock

# Generated at 2022-06-13 16:37:03.839835
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class TestClass(object):
        def __init__(self, lock=None):
            if lock is None:
                self._lock = threading.Lock()
            else:
                self._lock = lock

        @lock_decorator(attr='_lock')
        def foo_attr(self, x, sleep=0.5):
            print('foo %s going to sleep for %ss' % (x, sleep))
            time.sleep(sleep)
            return x

        @lock_decorator(lock=threading.Lock())
        def foo_lock(self, x, sleep=0.5):
            print('foo %s going to sleep for %ss' % (x, sleep))
            time.sleep(sleep)
            return x

    tc = TestClass()

    # Ensure same instance

# Generated at 2022-06-13 16:37:15.443496
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    class Foo(object):
        @lock_decorator(attr='some_lock')
        def bar(self):
            return True

    class Baz(object):
        def __init__(self):
            self.some_lock = Lock()

        @lock_decorator(attr='some_lock')
        def bar(self):
            return True

    mutex = Lock()
    class Boom(object):
        @lock_decorator(lock=mutex)
        def bar(self):
            return True

    foo = Foo()
    assert not hasattr(foo, 'some_lock')
    assert foo.bar() is True

    baz = Baz()
    assert baz.bar() is True
    assert baz.some_lock.locked()

    boom = Boom()

# Generated at 2022-06-13 16:37:25.286611
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading
    class TestLockDecorator(unittest.TestCase):
        def test_attr(self):
            class TestObject(object):
                x = 0

                @lock_decorator(attr='lock')
                def increment(self):
                    self.x += 1

                @lock_decorator(attr='lock')
                def get(self):
                    return self.x

                def __init__(self):
                    self.lock = threading.Lock()

            testobject = TestObject()
            testobject.increment()
            self.assertEquals(testobject.get(), 1)
            testobject.increment()
            self.assertEquals(testobject.get(), 2)

        def test_lock(self):
            class TestObject(object):
                x = 0

               

# Generated at 2022-06-13 16:37:37.213507
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import random

    # A common pattern in Ansible is to use a class method as a callback,
    # and while running multiple callbacks, they may attempt to modify
    # the same attributes on the same object.

    lock = threading.Lock()

    # This class has two class methods that are intended to be used as callbacks
    # in Ansible.
    class DummyClass:
        # One class method that is used for a callback plugin,
        # this class method will modify the ``result`` attribute
        # on the object, where the object is the same object
        # in each thread.
        @lock_decorator(attr='_lock')
        def callback(self, result):
            time.sleep(1)
            self.result = result

        # Another class method that is also used for a callback plugin,

# Generated at 2022-06-13 16:37:42.809028
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class foo(object):
        def __init__(self):
            self.bar = threading.Lock()

        @lock_decorator(attr='bar')
        def test(self, val):
            '''Docstring is preserved'''
            return val

        @lock_decorator(lock=threading.Lock())
        def test2(self, val):
            return val

    # Ensure docstring is preserved
    assert foo.test.__doc__ == 'Docstring is preserved'

    F = foo()

    assert F.test(val=2) == 2
    assert F.test2(val=2) == 2

# Generated at 2022-06-13 16:37:52.668007
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch


# Generated at 2022-06-13 16:38:02.821941
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import pytest

    class test_lock_decorator(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method1(self):
            return self._lock

        @lock_decorator(lock=threading.Lock())
        def method2(self):
            return self._lock

    t = test_lock_decorator()
    assert not t._lock.acquire(blocking=False)
    assert t.method1().acquire(blocking=False)
    assert t.method1().acquire(blocking=False)
    assert t.method2().acquire(blocking=False)
    assert t.method2().acquire(blocking=False)

# Generated at 2022-06-13 16:38:09.025779
# Unit test for function lock_decorator
def test_lock_decorator():  # pragma: no cover
    import threading
    _lock = threading.Lock()

    class Example:
        _lock = threading.Lock()

        def __init__(self):
            self.val = 0

        @lock_decorator()
        def run(self):
            self.val = 1

        @lock_decorator(attr='_lock')
        def another_run(self):
            self.val = 2

        @lock_decorator(lock=_lock)
        def run_with_lock(self):
            self.val = 3

    e = Example()
    e.run()
    assert e.val == 1

    e = Example()
    e.another_run()
    assert e.val == 2

    e = Example()
    e.run_with_lock()
    assert e

# Generated at 2022-06-13 16:38:16.374936
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    _test_lock = threading.Lock()

    def test_func():
        pass

    # Test using attr
    @lock_decorator(attr='_test_lock')
    def test_func_attr(self):
        pass

    assert test_func_attr._lock_function_decorator_original_fn == test_func
    test_func_attr._test_lock = _test_lock
    assert test_func_attr.__name__ == 'test_func_attr'
    assert test_func_attr.__module__ == 'ansible.utils.lock_decorator'
    assert test_func_attr.__wrapped__ == test_func

    # Test using explicit lock

# Generated at 2022-06-13 16:38:28.422488
# Unit test for function lock_decorator
def test_lock_decorator():
    from ansible_collections.ansible.community.plugins.module_utils import basic
    import pytest
    import random
    import threading

    class TestClass(object):
        @lock_decorator(attr='_callback_lock')
        def send_callback(self, event, data):
            assert self.expected_event == event
            assert self.expected_data == data
            self.callback_called += 1

        def send_callback2(self, event, data):
            assert self.expected_event == event
            assert self.expected_data == data
            self.callback_called += 1

    @pytest.fixture
    def test_class(request):
        test_class = TestClass()
        # use the fixture name to decide what to create
        test_class.expected_event = request.function.__name__


# Generated at 2022-06-13 16:38:38.369382
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    lock = threading.Lock()

    class TestLock(object):
        def __init__(self, *args, **kwargs):
            self._lock = threading.Lock()
            self._counter = 0
            self._locked = False
            self._start = None
            self._value = None

        def lock(self):
            self._lock.acquire()
            self._locked = True

        def unlock(self):
            self._lock.release()
            self._locked = False

        @lock_decorator(attr='_lock')
        def attr_lock(self, value=None):
            assert self._locked is True
            if value:
                self._value = value
            time.sleep(1)
            return self._counter


# Generated at 2022-06-13 16:38:48.911973
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    @lock_decorator(lock=threading.Lock())
    def foo_thread1(data):
        time.sleep(data)
        return data

    @lock_decorator(lock=threading.Lock())
    def foo_thread2(data):
        time.sleep(data)
        return data

    @lock_decorator(lock=threading.Lock())
    def foo_thread3(data):
        time.sleep(data)
        return data

    foo1 = []
    foo2 = []
    foo3 = []

    class Foo(object):
        _foo_lock = threading.Lock()

        @lock_decorator(attr='_foo_lock')
        def bar_thread1(self, data):
            time.sleep(data)
            return data

# Generated at 2022-06-13 16:38:58.416737
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    class TestClass(object):
        class_lock = threading.Lock()
        instance_lock = threading.Lock()

        @lock_decorator(attr='class_lock')
        def class_method(self):
            yield self.class_lock

        @classmethod
        @lock_decorator(attr='class_lock')
        def class_method_method(cls):
            yield cls.class_lock

        @lock_decorator(attr='instance_lock')
        def method(self):
            yield self.instance_lock

        @lock_decorator(lock=threading.Lock())
        def method_with_arg(self, lock):
            yield lock


# Generated at 2022-06-13 16:39:07.467760
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    from threading import Lock, Thread

    class Foo(object):
        _lock = Lock()

        @lock_decorator(attr='_lock')
        def bar(self):
            self.baz += 1

    class TestLockDecorator(unittest.TestCase):
        def setUp(self):
            self.foo = Foo()
            self.foo.baz = 0

        def test_decorator(self):
            for i in range(100):
                self.foo.bar()
            self.assertEqual(self.foo.baz, 100)
            self.assertEqual(Foo._lock._is_owned(), False)

        def test_threads(self):
            def run():
                for i in range(100):
                    self.foo.bar()

# Generated at 2022-06-13 16:39:11.698655
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class MyClass(object):
        def __init__(self):
            self._myattr = 0
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def increment(self):
            self._myattr += 1

    mc = MyClass()
    mc.increment()
    assert mc._myattr == 1

# Generated at 2022-06-13 16:39:19.873783
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading
    import time

    class TestLockDecorator(unittest.TestCase):
        def test_attr(self):
            class Test(object):
                _lock = threading.Lock()
                @lock_decorator(attr='_lock')
                def method(self):
                    time.sleep(1)

            instance = Test()
            instance.method()

        def test_lock(self):
            lock = threading.Lock()
            @lock_decorator(lock=lock)
            def method():
                time.sleep(1)
            method()

# Generated at 2022-06-13 16:39:30.678912
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading
    from six.moves import queue
    from six.moves import range

    # Test using a ``threading.Lock`` object
    class TestLock(object):

        lock = threading.Lock()
        value = 0

        @lock_decorator(lock=lock)
        def do_work(self, test_val):
            self.value += test_val

        @lock_decorator(lock=lock)
        def do_work_no_self(self, test_val):
            self.value += test_val

        @lock_decorator(lock=lock)
        def do_work_no_self_no_decorator(self, test_val):
            self.value += test_val

    test = TestLock()

    # Pass a lock object to the decorator


# Generated at 2022-06-13 16:39:39.778700
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    class FakeA:
        def __init__(self):
            self._fake_lock = Lock()

        @lock_decorator(attr='_fake_lock')
        def fake_method(self):
            return 'fake_method'

    class FakeB:
        @lock_decorator(lock=Lock())
        def fake_method(self):
            return 'fake_method'

    # Test attribute-based lock
    a = FakeA()
    assert a.fake_method() == 'fake_method'

    # Test passed lock
    b = FakeB()
    assert b.fake_method() == 'fake_method'

# Generated at 2022-06-13 16:39:45.984495
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    i = 0
    lock = threading.Lock()
    def inc_one(lock):
        nonlocal i
        with lock:
            i += 1
            return i
    def inc_three(lock):
        nonlocal i
        with lock:
            i += 3
            return i
    t1 = threading.Thread(target=inc_one, args=(lock,))
    t2 = threading.Thread(target=inc_three, args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    assert i == 4

# Generated at 2022-06-13 16:39:55.526414
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass:
        _callback_lock = threading.Lock()

        def __init__(self, value):
            self.value = value

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, value):
            self.value += value

        @lock_decorator(lock=threading.Lock())
        def some_method(self, value):
            self.value *= value


    obj = TestClass(1)
    obj.send_callback(1)
    assert obj.value == 2

    obj.some_method(2)
    assert obj.value == 4

# Generated at 2022-06-13 16:40:04.423481
# Unit test for function lock_decorator
def test_lock_decorator():
    import collections
    import threading
    import time
    import unittest

    class FakeLock(object):
        """
        A fake lock object to use for testing the lock decorator
        """
        def __enter__(self):
            pass

        def __exit__(self, exc_type, exc_val, exc_tb):
            pass

    class TestLockDecorator(unittest.TestCase):
        def setUp(self):
            self.lock = threading.Lock()
            self.fake_lock = FakeLock()
            self.func_counter = collections.Counter()
            self.func_obj = collections.Counter()

        def counter_func(self, arg):
            with self.lock:
                self.func_counter.update([arg])


# Generated at 2022-06-13 16:40:19.575065
# Unit test for function lock_decorator
def test_lock_decorator():
    import inspect
    import threading

    # Test using an explicit lock
    lock = threading.Lock()
    @lock_decorator(lock=lock)
    def foo():
        pass

    assert foo.__doc__ is None, foo.__doc__
    assert foo.__name__ == 'foo', foo.__name__
    assert inspect.isfunction(foo) is True, foo

    # Test using an object attribute for the lock
    class Example(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def meth(self):
            pass

    ex = Example()
    assert ex.meth.__doc__ is None, ex.meth.__doc__
    assert ex.meth.__name__ == 'meth', ex.meth.__name__
   

# Generated at 2022-06-13 16:40:28.512070
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except ImportError:
        import unittest
        raise unittest.SkipTest('python-threading not installed')
    import threading
    _lock = threading.Lock()
    @lock_decorator(lock=_lock)
    def _func():
        return 'foo'
    @lock_decorator(attr='_lock')
    def _func2(self):
        return 'bar'
    class _TestObj(object):
        _lock = _lock
        @_func2
        def _method2(self):
           pass
    assert _func() == 'foo'
    assert _TestObj()._method2 == 'bar'

# Generated at 2022-06-13 16:40:39.954952
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from six.moves import queue

    class Test(object):
        # Test as class decorator
        @classmethod
        @lock_decorator(attr='_lock')
        def foo(cls, q):
            q.put(1)

        @classmethod
        def bar(cls, q):
            q.put(2)

        def __init__(self):
            self._lock = threading.Lock()

        # Test as function decorator
        @lock_decorator(lock=threading.Lock())
        def baz(self, q):
            q.put(3)

        def mingo(self, q):
            q.put(4)

    q = queue.Queue(maxsize=4)

# Generated at 2022-06-13 16:40:50.864537
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from collections import deque

    class Test(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self._callbacks = deque()

        def register_callback(self, fn):
            self._callbacks.append(fn)

        def _run_callbacks(self):
            for callback in self._callbacks:
                callback()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            return self._run_callbacks()

    test = Test()
    test.register_callback(lambda: test.register_callback(lambda: None))

    try:
        test.send_callback()
    except RuntimeError:
        pass
    else:
        assert False, 'Failed to catch deadlock'

    test

# Generated at 2022-06-13 16:41:00.913817
# Unit test for function lock_decorator
def test_lock_decorator():
    import random
    import threading

    @lock_decorator()
    def test_func():
        return 'works'

    assert test_func() == 'works'

    class TestClass:
        def __init__(self):
            self.counter = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def add(self):
            self.counter += 1

        @lock_decorator(lock=self.lock)
        def sub(self):
            self.counter -= 1

    t = TestClass()
    assert t.counter == 0

    t.add()
    assert t.counter == 1

    t.sub()
    assert t.counter == 0

    lock = threading.Lock()
    t2 = TestClass()
    assert t2.counter == 0

# Generated at 2022-06-13 16:41:10.595917
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class MockedStuff:
        _some_lock = threading.Lock()
        _some_attr = 'this will be replaced'
        @lock_decorator(attr='_some_lock')
        def some_method(self, value):
            self._some_attr = value

        @lock_decorator(lock=threading.Lock())
        def some_other_method(self, value):
            self._some_attr = value

    m = MockedStuff()
    for i in range(4):
        m.some_method(i)
        m.some_other_method(i)
        assert m._some_attr == i

# Generated at 2022-06-13 16:41:17.355345
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except ImportError:
        raise AssertionError('You need threading to test this')

    lock = threading.Lock()

    class MyClass(object):
        def __init__(self):
            self._lock = lock

    mc = MyClass()

    @lock_decorator(attr='_lock')
    def my_method(self):
        return True
    assert my_method(mc) is True

    @lock_decorator(lock=lock)
    def my_method(self):
        return True
    assert my_method(mc) is True

# Generated at 2022-06-13 16:41:27.193632
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from random import randint

    _lock = threading.RLock()
    results = []

    @lock_decorator(attr='_lock')
    def _test(a, b):
        results.append(a + b)

    @lock_decorator(lock=_lock)
    def _test2():
        results.append(2000)

    threads = []
    for i in range(10):
        t = threading.Thread(target=_test, args=(randint(1, 10), randint(1, 10)))
        threads.append(t)
        t.start()

    t = threading.Thread(target=_test2)
    threads.append(t)
    t.start()

    for t in threads:
        t.join()


# Generated at 2022-06-13 16:41:36.241130
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class Foo(object):

        def __init__(self):
            self._lock = threading.Lock()
            self._value = 0
            self._index = 0

        @lock_decorator(attr='_lock')
        def set_value_locked(self, value):
            self._value = value

        @lock_decorator(lock=threading.Lock())
        def set_index_locked(self, index):
            self._index = index

    f = Foo()

    f.set_value_locked(10)
    f.set_index_locked(10)

    assert f._value == 10
    assert f._index == 10



# Generated at 2022-06-13 16:41:44.216295
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import random

    class Test(object):
        def __init__(self, sleep=0):
            self._lock = threading.Lock()
            self._sleep_time = sleep

        @lock_decorator(attr='_lock')
        def locked(self, *args):
            time.sleep(self._sleep_time)
            return True

    @lock_decorator()
    def not_locked(*args):
        pass

    @lock_decorator(lock=threading.Lock())
    def no_args_no_self(arg1, arg2):
        pass

    for _ in range(0, 10):
        s = random.randint(1, 5)
        t = Test(s)
        threads = []

# Generated at 2022-06-13 16:41:56.947664
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep
    from ansible.module_utils.six import PY3

    test_lock = threading.Lock()
    class_lock = threading.Lock()

    if PY3:
        class Generic:
            def __init__(self):
                self.method_lock = threading.Lock()
            @lock_decorator(lock=test_lock)
            def lock_test(self, msg):
                print('Test %s' % msg)
                sleep(1)
            @classmethod
            @lock_decorator(attr='method_lock')
            def class_lock_test(self, msg):
                print('Class %s' % msg)
                sleep(1)
    else:
        class Generic:
            method_lock = threading.Lock()

# Generated at 2022-06-13 16:42:07.442332
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class Test:
        def __init__(self):
            self._lock = threading.Lock()
            self._called = False
            self._count = 0

        @lock_decorator(attr='_lock')
        def test(self, delay=0):
            import time
            self._called = True
            time.sleep(delay)
            self._count += 1

    instance = Test()
    instance.test()
    assert instance._called is True
    assert instance._count == 1

    instance._called = False
    instance._count = 0

    threads = []
    for i in range(10):
        t = threading.Thread(target=instance.test, args=(0.2,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

# Generated at 2022-06-13 16:42:17.894101
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class TestLockDecorator(unittest.TestCase):
        def setUp(self):
            self.lock = threading.Lock()

        def tearDown(self):
            self.lock.release()

        @lock_decorator(attr='lock')
        def test_attr(self):
            self.lock.acquire()

        @lock_decorator(lock=threading.Lock())
        def test_explicit(self):
            self.lock.acquire()

    case = TestLockDecorator()
    case.assertRaises(AssertionError, case.test_attr)
    case.assertRaises(AssertionError, case.test_explicit)

if __name__ == '__main__':
    test_lock_decorator()

# Generated at 2022-06-13 16:42:26.716718
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    test_list = []
    @lock_decorator(lock=lock)
    def append_1():
        test_list.append(1)
    @lock_decorator(attr='attr_lock')
    def append_2(self):
        test_list.append(2)
    class DoubleAppend(object):
        attr_lock = lock
        def __init__(self):
            self._lock = threading.Lock()
        @lock_decorator(lock=lock)
        def append_11(self):
            test_list.append(11)
        @lock_decorator(attr='_lock')
        def append_22(self):
            test_list.append(22)
    obj = DoubleAppend()

# Generated at 2022-06-13 16:42:35.427945
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    # Create a class with a lock and a method to add to a list
    # once per second in a separate thread
    # There are two methods, one using the ``attr`` lock, and the other
    # using a direct lock. The tests should not change based on which
    # technique is used.
    class TestClass(object):
        def __init__(self):
            self._callback_lock = self._lock = threading.Lock()
            self.test_list = []
            self.thread_run = True

        @lock_decorator(attr='_callback_lock')
        def thread_method_1(self):
            while self.thread_run:
                # Add a new item to test_list
                self.test_list.append(1)
                time.sleep(1)


# Generated at 2022-06-13 16:42:45.909435
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class TestClass(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='lock')
        def alter_value(self):
            self.value += 1

    class TestClassLock(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.value = 0

        @lock_decorator()
        def alter_value(self):
            self.value += 1

    class TestClassLockObj(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 0

        @lock_decorator(lock=object())
        def alter_value(self):
            self.value

# Generated at 2022-06-13 16:42:55.642553
# Unit test for function lock_decorator
def test_lock_decorator():
    import os, time, threading
    from contextlib import contextmanager

    class MyClass(object):
        def __init__(self):
            # Threading.Lock() is already a context manager,
            # but requires explicit calls to ``.acquire()``
            # and ``.release()``.
            self.callback_lock = threading.Lock()

        @contextmanager
        def some_ctx_mgr(self):
            print('some_ctx_mgr entering')
            yield
            print('some_ctx_mgr exiting')

        @lock_decorator(attr='callback_lock')
        def send_callback(self, msg):
            print(msg)
            # Simulate a case where the lock is held for longer
            # than is necessary to perform the wrapped function.
            # Since the lock is a context manager, it will

# Generated at 2022-06-13 16:43:01.647437
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    _lock = threading.Lock()

    class TestClass(object):
        def __init__(self, lock):
            self._callback_lock = lock


# Generated at 2022-06-13 16:43:08.626691
# Unit test for function lock_decorator
def test_lock_decorator():
    import mock
    import threading
    class Test(object):
        def __init__(self):
            self._lock = None

        @lock_decorator(attr='_lock')
        def method1(self):
            pass

        @lock_decorator(lock=mock.Mock())
        def method2(self):
            pass

        @lock_decorator(lock=threading.Lock())
        def method3(self):
            pass

    t = Test()
    t.method1()
    t.method2()
    t.method3()

# Generated at 2022-06-13 16:43:20.186230
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading
    import time
    import random

    class TestClass():
        _lock = threading.Lock()
        variable = 0

        @lock_decorator(lock=_lock)
        def method(self):
            self.variable += 1
            time.sleep(random.random())

    test_object = TestClass()
    threads = []
    for i in range(10):
        t = threading.Thread(target=test_object.method)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    assert test_object.variable == 10

    test_object.variable = 0

    threads = []
    for i in range(10):
        t = threading.Thread(target=test_object.method)
        t.start()

# Generated at 2022-06-13 16:43:44.163821
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Mock():
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, *args, **kwargs):
            pass

        @lock_decorator(lock=threading.Lock())
        def some_method(self, *args, **kwargs):
            pass

    mock = Mock()
    mock.send_callback()
    mock.some_method()

# Generated at 2022-06-13 16:43:52.301487
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Ensure that the lock_decorator can be imported'''
    from threading import Lock
    lock = Lock()

    @lock_decorator(lock=lock)
    def test1():
        '''Testing function for lock_decorator'''
        pass

    @lock_decorator(attr='_lock')
    def test2(self):
        '''Testing function for lock_decorator'''


    class TestClass(object):
        '''Class used to test lock_decorator'''
        def __init__(self):
            self._lock = lock


        @lock_decorator(attr='_lock')
        def test3(self):
            '''Testing function for lock_decorator'''



# Generated at 2022-06-13 16:43:58.385119
# Unit test for function lock_decorator
def test_lock_decorator():
    import os
    import threading
    import time
    import unittest
    try:
        xrange
    except NameError:
        xrange = range
    # Creating directory "test_dir"
    try:
        os.mkdir('test_dir')
    except OSError:
        pass

    def read(filename):
        with open(filename) as f:
            return f.read()
    class Test(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.filename = 'test_dir/test_file'
            # Open a file for writing and close to reset it
            with open(self.filename, 'w') as f:
                pass

# Generated at 2022-06-13 16:44:10.406139
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading, time

    class Timer:
        lock = threading.Lock()

        @lock_decorator(attr='lock')
        def start(self):
            self.start_time = time.time()

        @lock_decorator(attr='lock')
        def stop(self):
            self.stop_time = time.time()

        @lock_decorator(attr='lock')
        def elapsed(self):
            return self.stop_time - self.start_time

    timer = Timer()

    def test_func(timer):
        timer.start()
        time.sleep(1)
        timer.stop()
        print(timer.elapsed())

    for i in range(4):
        thread = threading.Thread(target=test_func, args=(timer,))
        thread.start()

# Generated at 2022-06-13 16:44:19.329214
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._data = []

        def _append_data(self, data):
            self._data.append(data)
            # deliberately cause a pause to better test the lock
            import time
            time.sleep(1)

        @lock_decorator(attr='_lock')
        def append_data(self, data):
            # this method is annotated to use ``Foo._lock`` explicitly
            self._append_data(data)

        @classmethod
        @lock_decorator(lock=threading.Lock())
        def append_class_data(cls, data):
            # this class method is annotated to use a new Lock instance
            cls._append_data(data)

   

# Generated at 2022-06-13 16:44:30.362474
# Unit test for function lock_decorator
def test_lock_decorator():

    from threading import Lock, Thread
    from time import sleep

    class Foo(object):

        def __init__(self):
            self._some_lock = Lock()
            self._some_value = 0

        @lock_decorator(attr='_some_lock')
        def incr(self, num):
            sleep(1)
            self._some_value += num

    foo = Foo()

    thread = Thread(target=foo.incr, args=(1,))
    thread.start()
    sleep(.2)
    thread = Thread(target=foo.incr, args=(1,))
    thread.start()
    thread.join()

    assert foo._some_value == 1

# Generated at 2022-06-13 16:44:39.881557
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    class Simple(object):
        def __init__(self):
            self.unused_lock = Lock()
            self._callback_lock = Lock()
            self.count = 0

        def increment_count(self):
            self.count += 1

        def decrement_count(self):
            self.count -= 1

        @lock_decorator(attr='_callback_lock')
        def increment_count_with_lock(self):
            self.increment_count()

        @lock_decorator(attr='unused_lock')
        def decrement_count_with_lock(self):
            self.decrement_count()

        @lock_decorator(lock=Lock())
        def increment_count_with_lock_public(self):
            self.increment_count()



# Generated at 2022-06-13 16:44:47.153263
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class A(object):
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def foo(self):
            return 1

        @lock_decorator(lock=threading.Lock())
        def bar(self):
            return 1

    a = A()
    assert a.foo() == 1
    assert a.bar() == 1



# Generated at 2022-06-13 16:44:57.399207
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading

    def test_thread_lock(func, *args, **kwargs):
        def inner():
            func(*args, **kwargs)
        return inner

    class MockLockThread(threading.Thread):
        def __init__(self, target):
            self.target = target
            self.lock = threading.Lock()
            super(MockLockThread, self).__init__(target=self.target)

        def run(self):
            with self.lock:
                self.target()

    class TestObj(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.ctr = 0

        @lock_decorator(attr='lock')
        def test_method_attr(self):
            self.ctr += 1


# Generated at 2022-06-13 16:45:08.985244
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class MyObject(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='lock')
        def increment(self, value=1):
            self.value += value

    MyObject = MyObject()

    class MyThread(threading.Thread):
        # pylint: disable=unused-argument
        def __init__(self, *args, **kwargs):
            self.value = 0
            super(MyThread, self).__init__(*args, **kwargs)

        def run(self):
            super(MyThread, self).run()
            MyObject.increment(value=1)

    threads = []
    for _ in range(100):
        t = MyThread()

# Generated at 2022-06-13 16:45:54.510486
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    lock.acquire()
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method_with_attr(self):
            pass

        @lock_decorator(lock=lock)
        def method_with_lock(self):
            pass

    obj = Test()
    assert not obj._lock.acquire(blocking=False)
    obj.method_with_attr()
    assert obj._lock.acquire(blocking=False)
    obj._lock.release()
    assert obj._lock.acquire(blocking=False)
    assert lock.acquire(blocking=False)
    obj.method_with_lock()