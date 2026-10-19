

# Generated at 2022-06-13 16:35:51.093922
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={
            'fail_on_lock': dict(type='bool', default=False),
        }
    )

    class MyClass:
        def __init__(self, *args, **kwargs):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def my_method(self):
            return True

    mc = MyClass()
    assert mc.my_method() is True

    # Now, with a lock
    fail_on_lock = module.params['fail_on_lock']
    lock = threading.Lock()


# Generated at 2022-06-13 16:36:00.739424
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep

    from ansible_collections.notstdlib.moveitallout.tests.unit.compat import unittest

    def set_and_return(self, x, y):
        if x is not None:
            if isinstance(x, str) and x.lower() == 'sleep':
                self._attempt_to_sleep = self._attempt_to_sleep + 1
                sleep(1)
            else:
                self.x = x
        if y is not None:
            if isinstance(y, str) and y.lower() == 'sleep':
                self._attempt_to_sleep = self._attempt_to_sleep + 1
                sleep(1)
            else:
                self.y = y
        return self.x, self.y


# Generated at 2022-06-13 16:36:07.443141
# Unit test for function lock_decorator
def test_lock_decorator():
    class Test(object):
        def __init__(self):
            self.lock_called = False
            self.lock = None

        @lock_decorator(attr='_lock')
        def foo(self):
            return

    class TestLock(object):
        def __init__(self):
            self.lock_called = False

        def __enter__(self):
            self.lock_called = True

        def __exit__(self, *args):
            self.lock_called = False

    test = Test()
    test.foo()
    assert not test._lock.lock_called

    lock = TestLock()
    test.foo = lock_decorator(lock=lock)(test.foo)
    test.foo()
    assert lock.lock_called

# Generated at 2022-06-13 16:36:18.782201
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading

    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._count = 0

        @lock_decorator(attr='_lock')
        def __call__(self):
            self._count += 1

    @lock_decorator(lock=threading.Lock())
    def increment(count):
        count += 1

    foo = Foo()
    count = 0

    def foo_runner():
        for _ in range(1000):
            foo()

    def increment_runner():
        nonlocal count
        for _ in range(1000):
            increment(count)


# Generated at 2022-06-13 16:36:26.553708
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep

    class Test():
        lock = threading.Lock()

        @lock_decorator()
        def _test_method(self, num):
            print('Starting thread %s' % num)
            sleep(2)
            print('Finished thread %s' % num)

        @lock_decorator(attr='lock')
        def _test_method_attr(self, num):
            print('Starting thread %s' % num)
            sleep(2)
            print('Finished thread %s' % num)

        @lock_decorator(lock=Test.lock)
        def _test_method_lock(self, num):
            print('Starting thread %s' % num)
            sleep(2)
            print('Finished thread %s' % num)

    t = Test

# Generated at 2022-06-13 16:36:36.685676
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread

    # To use this within the thread
    class TestClass():
        def __init__(self):
            self.test_val = 0
            self.lock_val = 0
            self.lock = Lock()

        @lock_decorator(lock=None)
        def add(self):
            self.lock_val += 1
            self.test_val += 1

        def sub(self):
            self.test_val -= 1

    # Run this many tests at the same time
    run_count = 100

    # Create our class instance
    tc = TestClass()
    # Create a thread with our function to be run
    threads = [Thread(target=tc.add) for x in range(run_count)]
    # Start all the threads
    [x.start() for x in threads]
   

# Generated at 2022-06-13 16:36:46.194432
# Unit test for function lock_decorator
def test_lock_decorator():
    from time import sleep

    class TestLock(object):
        def __init__(self):
            self.counter = 0
            import threading
            self._lock = threading.Lock()

        @property
        def lock(self):
            return self._lock

        @lock_decorator(lock=None)
        def test_lock_decorator_attr(self):
            self.counter += 10
            sleep(0.1)
            self.counter += 20
            sleep(0.1)
            self.counter += 30

        @lock_decorator(lock=lambda x: x.lock)
        def test_lock_decorator_lambda(self):
            self.counter += 10
            sleep(0.1)
            self.counter += 20
            sleep(0.1)
            self.counter += 30

   

# Generated at 2022-06-13 16:36:54.260793
# Unit test for function lock_decorator
def test_lock_decorator():
    class Test(object):
        _lock = None

        @lock_decorator(attr='_lock')
        def foo(self):
            print('foo')

    # Test support for the attr argument
    t = Test()
    t.foo()
    t._lock = {'foo': 'bar'}
    t.foo()

    class Test2(object):
        @lock_decorator(lock={'foo': 'bar'})
        def foo(self):
            print('foo')

    # Test support for the lock argument
    t = Test2()
    t.foo()
    t.bar = {'foo': 'baz'}
    t.foo()

# Generated at 2022-06-13 16:37:02.412823
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self.lock = threading.Lock()
        @lock_decorator(attr='lock')
        def test(self):
            self.data = 1
        @lock_decorator(lock=threading.Lock())
        def test2(self):
            self.data2 = 1

    t = Test()
    t.test()
    t.test2()
    assert t.data == 1
    assert t.data2 == 1

# Generated at 2022-06-13 16:37:11.789586
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    Tests for lock_decorator function
    '''
    import threading
    counter = 0

    # Decorate this function with a lock
    @lock_decorator(lock=threading.Lock())
    def test_function():
        global counter
        counter = counter + 1

    # Call from many threads and assert the value of counter
    threads = []
    for _ in range(100):
        thread = threading.Thread(target=test_function)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    assert counter == 1

# Generated at 2022-06-13 16:37:23.099571
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys
    import threading

    counter = 0
    lock = threading.Lock()

    @lock_decorator(lock=lock)
    def do_work():
        global counter
        counter += 1
        return counter

    threads = []
    for i in range(10):
        t = threading.Thread(target=do_work)
        t.daemon = True
        threads.append(t)
        t.start()

    # Give threads time to run
    import time
    time.sleep(0.01)

    if sys.version_info < (3,):
        assert counter == 1
    else:
        assert counter == 10

# Generated at 2022-06-13 16:37:35.119274
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import time
    import threading

    class Test(object):
        _lock = threading.Lock()

        '''Test lock_decorator'''
        # python -m pytest -s -v aws/utils/test_lock_decorator.py
        @lock_decorator(attr='_lock', lock=None)
        def test(self, val):
            self.val = val
            time.sleep(1)

        @lock_decorator(lock=threading.Lock())
        def test_lock(self, val):
            self.val = val
            time.sleep(1)

    class TestLockDecorator(unittest.TestCase):
        def test_lock_decorator(self):
            test = Test()

# Generated at 2022-06-13 16:37:43.999089
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    class Test(object):

        def __init__(self):
            self.call_count = 0
            self.callback_count = 0
            self.lock = Lock()

        @lock_decorator(attr='lock')
        def send_callback(self, callback):
            self.call_count += 1
            self.callback_count += callback()

        @lock_decorator(lock=Lock())
        def some_method(self):
            self.call_count += 1

    t = Test()
    assert t.call_count == 0
    assert t.callback_count == 0

    t.some_method()
    assert t.call_count == 1
    assert t.callback_count == 0

    t.send_callback(t.some_method)

# Generated at 2022-06-13 16:37:53.408074
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class Test(object):

        def __init__(self):
            self.attr_lock = threading.RLock()
            self.explicit_lock = threading.RLock()

        @lock_decorator(attr='attr_lock')
        def attr_test(self, index):
            print('%d should print first' % index)
            time.sleep(1)
            print('%d should print last' % index)

        @lock_decorator(lock=threading.RLock())
        def explicit_test(self, index):
            print('%d should print second' % index)
            time.sleep(1)
            print('%d should print second to last' % index)

    def run(index):
        test.attr_test(index)

# Generated at 2022-06-13 16:38:03.432077
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    if have_mock:
        @lock_decorator(attr='mock_lock')
        def some_method(self, a, b, c, d=0, e=1, f=2, g=3):
            return a, b, c, d, e, f, g

        with patch('threading.RLock') as mock_lock_class:
            lock = mock_lock_class.return_value
            m = MagicMock(spec=SomeClass)
            some_method(m, 'foo', 'bar', 'baz', d=4, e=5, g=6)
            mock_lock_class.assert_called_with()
            lock.__enter__.assert_called_with()
            lock.__exit__.assert_called_with(None, None, None)
           

# Generated at 2022-06-13 16:38:13.755288
# Unit test for function lock_decorator
def test_lock_decorator():
    class A(object):
        def __init__(self, lock=None):
            if lock:
                self._test_lock_decorator_lock = lock
            else:
                self._test_lock_decorator_lock = None
            self.value = 0

        @lock_decorator(attr='_test_lock_decorator_lock')
        def add(self):
            self.value += 1

    a = A()
    a.add()
    assert a.value == 1

    # No lock, should fail
    try:
        a = A()
        a.add()
    except Exception:
        pass
    else:
        assert False
    finally:
        assert a.value == 0

    # Now with a lock
    import threading
    lock = threading.Lock()
    a = A

# Generated at 2022-06-13 16:38:18.232981
# Unit test for function lock_decorator
def test_lock_decorator():
    import os
    import threading
    import time

    class Test(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.count = 0

        def count_up(self):
            with self.lock:
                self.count += 1
                print("Thread %s: Incremented count to: %d" % (threading.current_thread().name, self.count))

        def count_up_2(self):
            with lock_decorator(lock=self.lock)(self.count_up)() as count_up:
                time.sleep(1)
                count_up()

    @lock_decorator()
    def foo():
        return 'bar'

    assert foo() == 'bar'


# Generated at 2022-06-13 16:38:29.617698
# Unit test for function lock_decorator
def test_lock_decorator():
    class SomeObject(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.count = 0

        @lock_decorator(attr='lock')
        def increment(self):
            # This would throw ``RuntimeError`` if the lock wasn't
            # properly acquired
            self.count += 1

        @lock_decorator(attr='lock')
        def increment_other(self, x):
            # This would throw ``RuntimeError`` if the lock wasn't
            # properly acquired
            self.count += x

        @lock_decorator(lock=threading.Lock())
        def increment_by(self, x):
            # This would throw ``RuntimeError`` if the lock wasn't
            # properly acquired
            self.count += x


# Generated at 2022-06-13 16:38:37.089576
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading

    class LockClass(object):
        lock_attr = threading.Lock()

        @lock_decorator(attr='lock_attr')
        def lock_method(self):
            print("I ran")
            time.sleep(0.04)

    class NoLockClass(object):
        @lock_decorator(lock=threading.Lock())
        def lock_method(self):
            print("I ran")
            time.sleep(0.04)

    class NoLockClass1(object):
        @lock_decorator(lock=threading.Lock())
        def lock_method(self):
            print("I ran")
            time.sleep(0.04)


# Generated at 2022-06-13 16:38:47.382605
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        lock = None

        def __init__(self, lock=None):
            if not lock:
                self.lock = threading.Lock()
            else:
                self.lock = lock

        @lock_decorator(attr='lock')
        def method(self,):
            return True

        @lock_decorator(lock=threading.Lock())
        def static_method(self):
            return True

    # Make sure it works with a class method that uses attr
    assert TestClass().method()

    # Make sure it works with a static method that uses a hardcoded lock
    assert TestClass().static_method()

    # Make sure that a threading.Lock object can be passed in and that
    # a new object won't be created

# Generated at 2022-06-13 16:39:02.788489
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    class SomeClass(object):
        '''Simple class for test of lock_decorator'''
        def __init__(self):
            self._lock = Lock()
            self._value = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            '''Increment ``self._value`` by 1'''
            self._value += 1
            return self._value

        @lock_decorator(lock=Lock())
        def decrement(self):
            '''Decrement ``self._value`` by 1'''
            self._value -= 1
            return self._value

    obj = SomeClass()
    for i in range(10):
        assert obj.increment() == i + 1

# Generated at 2022-06-13 16:39:14.169703
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    NONLOCAL_LIST = []

    class TestClass:

        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def mutate_nonlocals(self, item):
            NONLOCAL_LIST.append(item)

    def test_thread(tc):
        for i in range(50):
            tc.mutate_nonlocals(i)

    t = TestClass()
    threads = []
    for i in range(10):
        t = threading.Thread(target=test_thread, args=(t,))
        t.start()
        threads.append(t)

    for thr in threads:
        thr.join()

    assert sorted(NONLOCAL_LIST) == list(range(50))

# Generated at 2022-06-13 16:39:18.986237
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class FakeObject(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.count = 0
        @lock_decorator(attr='lock')
        def increase(self):
            self.count += 1
        @lock_decorator(lock=threading.Lock())
        def decrease(self):
            self.count -= 1

    fake = FakeObject()
    fake.increase()
    assert fake.count == 1
    fake.decrease()
    assert fake.count == 0

# Generated at 2022-06-13 16:39:30.165502
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    from collections import namedtuple

    class TestLock(object):
        __slots__ = ('dummy', 'lock')

        def __init__(self):
            self.dummy = 1
            self.lock = threading.Lock()

    @lock_decorator(attr='lock')
    def test(self):
        time.sleep(0.01)
        self.dummy += 1
        return self.dummy

    @lock_decorator(lock=threading.Lock())
    def test2():
        time.sleep(0.01)
        return 1

    def func_no_lock(self):
        self.dummy += 1
        return self.dummy

    @wraps(func_no_lock)
    def func(self):
        return func_no_

# Generated at 2022-06-13 16:39:37.314785
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        def __init__(self):
            self.lock = threading.RLock()
            self._state = {}
            self._state_lock = threading.RLock()

        @lock_decorator(attr='_state_lock')
        def get(self, key):
            return self._state.get(key, None)

        @lock_decorator(attr='lock')
        def set(self, key, value):
            self._state[key] = value
            return value

    test_obj = TestClass()

    assert test_obj.get('foo') is None
    assert test_obj.set('foo', 'bar') == 'bar'
    assert test_obj.get('foo') == 'bar'

# Generated at 2022-06-13 16:39:48.495831
# Unit test for function lock_decorator
def test_lock_decorator():
    import types
    import threading
    import time

    class Test(object):
        def __init__(self):
            # create lock
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def method(self):
            # naive timer, just for the purpose of demonstrating
            # that values are not overwritten
            for i in range(0, 5):
                time.sleep(1)
                print(i)

    @lock_decorator(lock=threading.Lock())
    def func():
        for i in range(0, 5):
            time.sleep(1)
            print(i)

    test = Test()

    assert(isinstance(test, Test))
    assert(callable(test.method))
    assert(isinstance(func, types.FunctionType))

# Generated at 2022-06-13 16:39:58.661000
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        def __init__(self):
            self.data = dict()
            self._data_lock = threading.Lock()

        @lock_decorator(attr='_data_lock')
        def methodA(self, key):
            self.data[key] = 'foo'

        @lock_decorator(lock=threading.Lock())
        def methodB(self, key):
            self.data[key] = 'bar'

        @lock_decorator(attr='_data_lock')
        def methodC(self, key):
            return self.data[key]

    t = Test()
    t.methodA('A')
    assert t.data == {'A': 'foo'}
    t.methodB('B')

# Generated at 2022-06-13 16:40:06.562940
# Unit test for function lock_decorator
def test_lock_decorator():
    # pylint: disable=missing-docstring
    import threading
    import time
    import uuid

    class MyClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._rand = uuid.uuid4()

        @lock_decorator(attr='_lock')
        def do_stuff(self):
            time.sleep(0.1)
            return self._rand

    mc = MyClass()
    asserts = []

    def _do_stuff():
        # pylint: disable=missing-docstring, unused-variable
        res = mc.do_stuff()
        if res != mc._rand:
            asserts.append(False)

    threads = []

# Generated at 2022-06-13 16:40:18.274290
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread
    import time
    lock = Lock()
    l = [0]
    def increase1(times):
        for i in range(times):
            l[0] = l[0] + 1

    def increase2(times):
        for i in range(times):
            lock.acquire()
            l[0] = l[0] + 1
            lock.release()

    @lock_decorator(lock=lock)
    def increase3(times):
        for i in range(times):
            l[0] = l[0] + 1

    def run_test(func, times, num):
        threads = []
        for i in range(num):
            t = Thread(target=func, args=(times,))
            threads.append(t)
            t.start()
       

# Generated at 2022-06-13 16:40:28.544171
# Unit test for function lock_decorator
def test_lock_decorator():
    # Import here to avoid circular dependencies
    import threading
    import time

    class Test(object):
        def __init__(self):
            self.value = 0
            self.lock = threading.Lock()
            self.second_lock = threading.Lock()

        @lock_decorator(attr='lock')
        def add_one(self):
            self.value += 1

        @lock_decorator(attr='second_lock')
        def add_five(self):
            self.value += 5

        @lock_decorator(lock=threading.Lock())
        def add_ten(self):
            self.value += 10

        @lock_decorator(attr='missing_lock_attr')
        def add_twenty(self):
            self.value += 20


    test = Test()
   

# Generated at 2022-06-13 16:40:43.559604
# Unit test for function lock_decorator
def test_lock_decorator():
    '''This function tests the lock_decorator method
    '''
    import threading

    # Using a pre-defined instance attribute
    class TestClass(object):
        def __init__(self, lock=threading.Lock()):
            self._lock = lock

        @lock_decorator(attr='_lock')
        def locked(self):
            return 1

    test_instance = TestClass()

    # Using an explicitly passed lock
    class TestClass2(object):

        @lock_decorator(lock=threading.Lock())
        def locked(self):
            return 2

    test_instance2 = TestClass2()

    # Test case: lock with pre-defined instance attribute
    assert test_instance.locked() == 1

    # Test case: lock with an explicitly passed lock
    assert test_instance2.locked()

# Generated at 2022-06-13 16:40:53.205433
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    from time import sleep

    class MyClass(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._v = 0

        @lock_decorator(attr='_lock')
        def safe_increment_v1(self):
            self._v += 1

        @lock_decorator(lock=threading.Lock())
        def safe_increment_v2(self):
            self._v += 1

    obj = MyClass()

    assert obj._v == 0

    obj.safe_increment_v1()
    assert obj._v == 1

    obj.safe_increment_v2()
    assert obj._v == 2

    # Try to increment rapidly and make sure we are properly locked
    def increment_v1():
        obj.safe_incre

# Generated at 2022-06-13 16:41:02.691723
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    # Just to make sure we catch any issues with this decorator
    # we'll define a simple class that just has a method
    # which prints a counter, and then sleeps to slow down
    # the execution.
    lock = threading.Lock()

    class ClassMethod(object):
        def __init__(self):
            self._counter = 0

        @lock_decorator()
        def class_method(self):
            with lock:
                self._counter += 1
                print(self._counter)
                time.sleep(0.5)

    obj = ClassMethod()
    # Create a thread for each of the ClassMethod.class_method
    # functions, to try and race each other.
    threads = [threading.Thread(target=obj.class_method) for _ in range(5)]


# Generated at 2022-06-13 16:41:14.240359
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = 'missing_lock_attr'
    lock_ob = None

    def assert_lock(args):
        assert args[1] == lock
        assert args[2] == lock_ob

    class Test(object):
        def __init__(self):
            self.__lock = threading.Lock()
            self.lock = lock
            self.lock_ob = lock_ob

        @lock_decorator(attr='__lock')
        def test_attr(self, lock):
            assert_lock(self.__lock.__enter__.call_args[0])
            assert_lock(self.__lock.__exit__.call_args[0])


# Generated at 2022-06-13 16:41:25.213857
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass(object):
        def __init__(self):
            self._test_lock = threading.Lock()

        @lock_decorator(attr='_test_lock')
        def func_attr_lock(self, sleep=False):
            '''Function lock is assigned to _test_lock attribute'''
            if sleep:
                import time
                time.sleep(1)
            return

        @lock_decorator(lock=threading.Lock())
        def func_explicit_lock(self, sleep=False):
            '''Function lock is explicitly passed via lock keyword'''
            if sleep:
                import time
                time.sleep(1)
            return

    def test_method_execution_time(method, lock, expected_time):
        import time

# Generated at 2022-06-13 16:41:33.181626
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestCls():
        def __init__(self):
            self._lock = threading.Lock()
            self._val = 0

        @lock_decorator(attr='_lock')
        def with_attr_lock(self, val):
            self._val = val

        @lock_decorator(lock=threading.Lock())
        def with_new_lock(self, val):
            self._val = val

    class TestThread(threading.Thread):
        def __init__(self, target):
            super(TestThread, self).__init__()
            self._target = target

        def run(self):
            for i in range(10000):
                self._target.with_attr_lock(1)
                self._target.with_new_lock(1)

    test = Test

# Generated at 2022-06-13 16:41:41.089242
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    lock = threading.Lock()
    class A(object):
        def __init__(self):
            self.lock = lock
            self.i = 0

        @lock_decorator(attr='lock')
        def __inc(self):
            self.i += 1

        def inc(self):
            self.__inc()
            self.__inc()
            self.__inc()

    class B(object):
        def __init__(self):
            self.i = 0

        @lock_decorator(lock=lock)
        def inc(self):
            self.i += 1

    def run(cls):
        a = cls()
        threads = []
        for i in range(20):
            t = threading.Thread(target=a.inc)
           

# Generated at 2022-06-13 16:41:47.489847
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock, Thread
    from time import sleep
    from sys import version_info
    # Doing as little as possible here to avoid side effects
    # of other imports
    if version_info[0] == 2:
        from Queue import Queue
    else:
        from queue import Queue

    class Example(object):
        def __init__(self):
            self.lock = Lock()
            self.queue = Queue()

        @lock_decorator(attr='lock')
        def add(self, value):
            self.queue.put(value)
            sleep(1.0)

    ex = Example()

    # Ensure serial execution
    thd1 = Thread(target=ex.add, args=(1,))
    thd2 = Thread(target=ex.add, args=(2,))
    thd

# Generated at 2022-06-13 16:41:52.731102
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class SomeClass(object):
        def __init__(self):
            self.called_with = list()
            self.called_with_lock = threading.Lock()

        @lock_decorator(attr='called_with_lock')
        def remote(self, value):
            self.called_with.append(value)
            time.sleep(random.random())
            return 'OK'

    def worker():
        some_class.remote('somevalue')

    some_class = SomeClass()
    for _ in range(4):
        threading.Thread(target=worker).start()
    time.sleep(0.5)
    assert set(['somevalue']) == set(some_class.called_with)

# Generated at 2022-06-13 16:41:58.758980
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading
    import time

    # https://stackoverflow.com/a/27372334
    # This class would be the class that instructs the method
    # to use the lock
    class Mock(object):
        def __init__(self):
            self.lock = threading.Lock()

    class SomeClass(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            time.sleep(1)

        @lock_decorator(lock=Mock().lock)
        def some_method(self):
            time.sleep(1)


# Generated at 2022-06-13 16:42:24.033941
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    class A(object):
        def __init__(self):
            self._count = 0
            self._lock = threading.Lock()
            self._count2 = 0
            self._lock2 = threading.Lock()

        @lock_decorator(attr='_lock')
        def inc(self):
            self._count += 1

        @lock_decorator(lock=self._lock2)
        def inc2(self):
            self._count2 += 1

    def test_thread1(x):
        for i in range(100):
            x.inc()

    def test_thread2(x):
        for i in range(100):
            x.inc2()

    a = A()
    for i in range(100):
        a.inc()


# Generated at 2022-06-13 16:42:31.848929
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestLock(object):
        _lock_attr = threading.Lock()
        _lock_explicit = threading.Lock()

        @lock_decorator(attr='_lock_attr')
        def using_attr(self, text):
            return text

        @lock_decorator(lock=_lock_explicit)
        def using_explicit_lock(self, text):
            return text

    t = TestLock()
    assert t.using_attr('foo') == 'foo'
    assert t.using_explicit_lock('foo') == 'foo'



# Generated at 2022-06-13 16:42:37.148718
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    _lock = threading.Lock()

    class Dummy(object):
        @lock_decorator(lock=_lock)
        def method(self):
            return 'I have been called'

        @classmethod
        @lock_decorator(attr='_lock', lock=_lock)
        def classmethod(cls):
            return 'I have been called'

    dummy = Dummy()
    assert dummy.method() == 'I have been called'
    assert dummy.classmethod() == 'I have been called'

# Generated at 2022-06-13 16:42:46.487412
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Fake:
        def __init__(self):
            self.x = 1
            self.lock = threading.Lock()

        @lock_decorator(lock=threading.Lock())
        def locked_no_attr(self):
            self.x += 1
            return self.x

        @lock_decorator(attr='lock')
        def locked_with_attr(self):
            self.x += 1
            return self.x

        @lock_decorator(lock=threading.Lock())
        def locked_wrong_attr(self):
            self.x += 1
            return self.x

    f = Fake()
    f.locked_with_attr()
    f.locked_no_attr()

# Generated at 2022-06-13 16:42:57.945599
# Unit test for function lock_decorator
def test_lock_decorator():  # pragma: no cover
    from __future__ import print_function

    import threading
    import time
    import random
    import unittest

    class TestCase(unittest.TestCase):
        def test_missing_attr(self):
            class AttrMissing(object):
                @lock_decorator(attr='_no_such_attr')
                def some_meth(self):
                    pass

            self.assertRaises(AttributeError, AttrMissing().some_meth)

        def test_attr_lock(self):
            class AttrLock(object):
                _lock = threading.Lock()

                @lock_decorator(attr='_lock')
                def some_meth(self, wait=1):
                    time.sleep(wait)

            runs = 0


# Generated at 2022-06-13 16:43:06.158568
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self, value):
            self._value = value
            self._callback_lock = threading.Lock()
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def some_method(self, message):
            print('{} {}'.format(message, self._value))

        @lock_decorator(lock=threading.Lock())
        def send_callback(self, message):
            print('{} {}'.format(message, self._value))

        @lock_decorator()
        def test_failure(self):
            raise RuntimeError('failed')

    t = Test('foo')
    t.some_method('bar')
    t.send_callback('bar')


# Generated at 2022-06-13 16:43:13.537550
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    global lock_test
    lock_test = 0
    _lock = threading.Lock()

    @lock_decorator(lock=_lock)
    def test_lock_method(*args, **kwargs):
        global lock_test
        if lock_test:
            return False
        else:
            lock_test = 1
            return True
    
    class LockTest:
        # Use the class attribute to define the lock
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def test_lock(self, *args, **kwargs):
            global lock_test
            if lock_test:
                return False
            else:
                lock_test = 1
                return True


# Generated at 2022-06-13 16:43:22.788480
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except ImportError:
        raise SkipTest('threading not available')

    @lock_decorator(lock=threading.Lock())
    def test_func(name):
        return name

    class test_class_attr(object):
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def test_method(self, name):
            return name

    class test_class(object):
        @lock_decorator(lock=threading.Lock())
        def test_method(self, name):
            return name

    # Test function
    t = []
    def func(name):
        t.append(name)
        for i in range(0,100):
            test_func(i)
   

# Generated at 2022-06-13 16:43:30.432481
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Test AnsibleModuleBase.lock_decorator function'''

    import threading

    class Foo(object):

        def __init__(self):
            self._lock = threading.Lock()
            self.counter = 0

        @lock_decorator(attr='_lock')
        def count_up(self):
            self.counter += 1

        @lock_decorator(lock=threading.Lock())
        def count_down(self):
            self.counter -= 1

    foo = Foo()
    foo.count_up()
    assert foo.counter == 1
    foo.count_down()
    assert foo.counter == 0

# Generated at 2022-06-13 16:43:39.022659
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    # Define a Class providing locks
    class A:
        def __init__(self):
            self.lock = threading.Lock()
            self.attr_lock = threading.Lock()

        @lock_decorator(lock=self.lock)
        def lock_method(self):
            self.do_stuff

        @lock_decorator(attr='attr_lock')
        def attr_lock_method(self):
            self.do_stuff

        def do_stuff(self):
            pass

    # Create and instance and call the lock_method
    A().lock_method()

    # Create and instance and call the attr_lock_method
    A().attr_lock_method()

# Generated at 2022-06-13 16:44:17.749973
# Unit test for function lock_decorator

# Generated at 2022-06-13 16:44:23.087555
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Lock

    class MyClass(object):
        _lock = Lock()

        @lock_decorator(attr='_lock')
        def some_method(self, a, b):
            return a + b

    obj = MyClass()
    exp = obj.some_method(1, 2)
    assert exp == 3

# Generated at 2022-06-13 16:44:27.121508
# Unit test for function lock_decorator
def test_lock_decorator():
    # We're making a mock type here, because if
    # we just create an instance of ``object``,
    # we can't add the lock to it
    class obj:
        pass

    o = obj()

    # Create a lock
    import threading
    l = threading.Lock()

    # Create a decorator using an attribute called
    # ``_callback_lock`` on the object.
    @lock_decorator(attr='_callback_lock')
    def foo(self):
        return 'foo'

    # Create a decorator using the lock
    @lock_decorator(lock=l)
    def bar(self):
        return 'bar'

    # Assert that we get an excpetion because ``_callback_lock``
    # doesn't exist on the object yet
    import pytest

# Generated at 2022-06-13 16:44:36.047287
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Testee(object):
        def __init__(self):
            self.val = 0
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def add_one(self):
            self.val += 1

        @lock_decorator(lock=threading.Lock())
        def add_two(self):
            self.val += 2

    t = Testee()

    for x in range(100):
        thread = threading.Thread(target=t.add_one)
        thread.start()
    assert t.val == 100

    for x in range(50):
        thread = threading.Thread(target=t.add_two)
        thread.start()
    assert t.val == 150



# Generated at 2022-06-13 16:44:43.977472
# Unit test for function lock_decorator
def test_lock_decorator():
    '''This function is used to test lock_decorator

    Returns:
        None
    '''
    import threading
    class test():
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def func(self):
            return 'ok'

    class test2():
        _lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def func(self):
            return 'ok'

    class test3():
        def func(self):
            return 'ok'

        @classmethod
        @lock_decorator(attr='_lock')
        def func_cls(cls):
            return 'ok'


    # Test with an instance defined lock
    t = test()

# Generated at 2022-06-13 16:44:53.808280
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test1(object):
        def __init__(self):
            self.attr = 'attr'

        @lock_decorator(attr='attr')
        def method1(self):
            return

    class Test2(object):
        def __init__(self):
            self.attr = 'method2'

        @lock_decorator(attr='attr')
        def method2(self):
            return

    class Test3(object):
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator(lock=threading.Lock())
        def method3(self):
            return

    class Test4(object):
        def __init__(self):
            self.lock = threading.Lock()


# Generated at 2022-06-13 16:45:03.403404
# Unit test for function lock_decorator
def test_lock_decorator():
    # Test that Lock works as expected
    import threading
    l = threading.Lock()
    with l:
        pass
    assert not l.locked()

    # Test that lock_decorator works when using a Lock
    @lock_decorator(lock=l)
    def lock_test_func():
        assert l.locked()
    lock_test_func()
    assert not l.locked()

    # Test that it works when attr is used
    class LockTester(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def lock_test_attr(self):
            assert self._callback_lock.locked()

    tester = LockTester()
    tester.lock_test_attr()

# Generated at 2022-06-13 16:45:09.571476
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
        def _locked(self):
            print('Getting lock')
            with self._lock:
                time.sleep(1)
                print('Got lock!')

    test = Test()
    test_thread = threading.Thread(target=test._locked)
    test_thread.start()
    test._locked()
    test_thread.join()

# Generated at 2022-06-13 16:45:20.071479
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass(object):
        _lock = threading.Lock()
        _value = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self._value += 1

        @lock_decorator(attr='_lock')
        def decrement(self):
            self._value -= 1

    inst = TestClass()

    threads = []
    for i in range(20):
        t = threading.Thread(target=inst.increment)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    assert inst._value == 20

    for i in range(20):
        t = threading.Thread(target=inst.decrement)
        t.start()
        threads.append(t)

   

# Generated at 2022-06-13 16:45:26.926711
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    _lock = threading.Lock()

    # lock_decorator needs to be the outermost decorator in order to work
    @lock_decorator(attr='_lock')
    class TestClass(object):
        def __init__(self, lock):
            self._lock = lock

        def lock_method(self):
            return True

    @lock_decorator(lock=_lock)
    def lock_function():
        return True

    assert TestClass(_lock).lock_method() is True
    assert lock_function() is True

if __name__ == "__main__":
    test_lock_decorator()