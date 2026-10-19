

# Generated at 2022-06-13 16:35:58.966196
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestClass:
        def __init__(self):
            self.test_var = 10
            self.test_var_lock = threading.Lock()
            self.test_var_lock_attr = threading.Lock()

        @lock_decorator(attr='test_var_lock_attr')
        def test_func(self, x):
            self.test_var = x

        @lock_decorator(lock=threading.Lock())
        def test_func_lock(self, x):
            self.test_var = x

        @lock_decorator(lock=self.test_var_lock)
        def test_func_lock_attr(self, x):
            self.test_var = x

    import time
    import random
    import threading as thr


# Generated at 2022-06-13 16:36:06.742893
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Container:
        def __init__(self):
            self._lock = threading.Lock()
            self.num = 0

        @lock_decorator(attr='_lock')
        def __iadd__(self, x):
            self.num += 1

    container = Container()
    for _ in range(10):
        t = threading.Thread(target=lambda: container.__iadd__(1))
        t.start()

    container.num = 0
    for _ in range(10):
        t = threading.Thread(target=lambda: container.__iadd__(2))
        t.start()

    assert container.num == 20

    class Container:
        _lock = threading.Lock()
        num = 0


# Generated at 2022-06-13 16:36:18.063077
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    lock_value = 0

    @lock_decorator(lock=lock)
    def decorated_method(self):
        nonlocal lock_value
        lock_value += 1

    # Call the decorated method 20 times, in the same thread
    # Doing this should mean that lock_value is still 1
    # If the lock is not correctly, then lock_value would be 20
    for i in range(20):
        decorated_method(None)
    assert lock_value == 1, 'lock_value was %d, expected 1' % lock_value

    # Spawn 20 threads, each which will call decorated_method
    # Since we use a lock, the lock_value should still be 2 at the end
    # If the lock is not correctly, then lock_value would be 20
    # We need a

# Generated at 2022-06-13 16:36:27.795972
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except ImportError:
        import sys
        sys.stderr.write('Skipping test_lock_decorator, threading module not available\n')
        return

    # attribute based locking
    class LockTest(object):
        def __init__(self, lock=None):
            if lock is None:
                self._lock = threading.Lock()
            else:
                self._lock = lock
            self.called = 0

        @lock_decorator(attr='_lock')
        def lock_function(self):
            self.called += 1

    inst = LockTest()
    for i in range(100):
        inst.lock_function()
    assert inst.called == 1, 'Lock decorated method was called more than one time'


# Generated at 2022-06-13 16:36:37.423583
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    class FakeModule(object):
        def __init__(self):
            self.start = 0
            self.end = 0
            self.time_taken = 0
            self.counter = 0
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def faker_func(self):
            self.start = time.time()
            time.sleep(1)
            self.end = time.time()
            self.time_taken = self.end - self.start
            self.counter += 1

        @lock_decorator(lock=threading.Lock())
        def faker_func2(self):
            self.start = time.time()
            time.sleep(1)

# Generated at 2022-06-13 16:36:46.602749
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass(object):
        def __init__(self):
            self._lock = threading.Lock()

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        @lock_decorator(attr='_lock')
        def test_attr(self):
            assert self._lock.locked()

        @lock_decorator()
        def test_no_attr(self):
            assert not self._lock.locked()

        @lock_decorator(lock=threading.Lock())
        def test_lock(self):
            assert not self._lock.locked()

    with TestClass() as test:
        test.test_attr()
        test.test_no_attr()
        test.test_lock()


# Generated at 2022-06-13 16:36:55.451913
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Test(object):
        def __init__(self, val):
            self.val = val
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def add_one(self):
            self.val += 1

        @lock_decorator(lock=threading.Lock())
        def add_two(self):
            self.val += 2

        @lock_decorator()
        def add_three(self):
            self.val += 3

        @lock_decorator()
        def add_four(self):
            self.val += 4

        def add_five(self):
            self.val += 5


# Generated at 2022-06-13 16:37:05.948730
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    # Create a lock
    lock = threading.Lock()

    # Create a list and a count
    stuff = []
    count = 0

    # Create a test class
    class TestLockDecorator(object):
        # Create an attribute to hold the lock
        # This is used by @lock_decorator(attr=...)
        _the_lock = threading.Lock()

        # Creating a method that uses the lock directly
        def test_decorator(self):
            with self._the_lock:
                return self.stuff.append({'id': count + 1})

        # Another method that uses lock directly
        def test_direct_lock(self):
            with lock:
                return self.stuff.append({'id': count + 1})

        # A third method that uses @lock_decorator(attr

# Generated at 2022-06-13 16:37:15.442189
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import unittest

    class LockDecoratorTests(unittest.TestCase):
        def setUp(self):
            self.counter = 0
            self.lock = threading.Lock()
            self.threads = []
            self.threads_completed = 0

            @lock_decorator(lock=self.lock)
            def increment_counter(i):
                time.sleep(0.1)
                self.counter += i
                self.threads_completed += 1

            self.increment_counter = increment_counter

        def test_lock_decorator(self):
            '''
            Test that the lock decorator works to prevent multiple threads from
            running the same function at the same time
            '''
            for i in range(100):
                t = thread

# Generated at 2022-06-13 16:37:23.433087
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class LocalLock(object):
        '''Class for testing lock_decorator'''

        def __init__(self):
            self._lock = threading.Lock()

        def take_lock(self):
            '''Method using lock_decorator'''
            with self._lock:
                return True

        @lock_decorator(attr='_lock')
        def return_lock(self):
            '''Method using lock_decorator'''
            return True

    local = LocalLock()
    assert local.take_lock() is True
    assert local.return_lock() is True

# Generated at 2022-06-13 16:37:37.444264
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    # This state is shared
    state = [0]

    class C:
        def __init__(self, lock=None):
            if lock:
                self.lock = lock
            else:
                self.lock = threading.Lock()
        @lock_decorator(attr='lock')
        def use_attr_lock(self):
            # example that uses the lock found on
            # the instance
            add_to_state(state, 1)

    @lock_decorator(lock=lock)
    def use_explicit_lock():
        # example that uses an explicitly passed
        # lock
        add_to_state(state, 2)


# Generated at 2022-06-13 16:37:46.067571
# Unit test for function lock_decorator
def test_lock_decorator():
    import sys, threading
    if sys.version_info[0] == 2:
        import __builtin__ as builtins
    else:
        import builtins

    class Nowhere(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def locked_method(self):
            self.__class__.call_count += 1

        @lock_decorator(lock=threading.Lock())
        def overridden_method(self):
            self.__class__.call_count += 1

    Nowhere.call_count = 0
    nowhere = Nowhere()

    # Create a list of "threads" (actually functions)
    threads = [builtins.function(nowhere.locked_method)] * 100
    threads.extend

# Generated at 2022-06-13 16:37:55.221990
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading

    class TestDummyClass(object):
        def __init__(self):
            self._callback_lock = threading.Lock()
            self.somevar = 0

    class TestLockClass(unittest.TestCase):
        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            self.somevar += 5

        @lock_decorator(lock=threading.Lock())
        def send_callback2(self):
            self.somevar += 5

        def test_send_callback(self):
            tdc = TestDummyClass()
            # Send 4 callbacks
            tdc.send_callback()
            tdc.send_callback()
            tdc.send_callback()
            tdc.send_callback()

# Generated at 2022-06-13 16:38:04.199433
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class FakeLockObj:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

    class FakeClass:
        def __init__(self):
            self._lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def send_callback(self):
            return True

    class FakeClass2:
        def __init__(self):
            self._lock = threading.Lock()
        @lock_decorator(lock=FakeLockObj())
        def send_callback(self):
            return True

    fake = FakeClass()
    assert fake.send_callback()

    fake = FakeClass2()
    assert fake.send_callback()

# Generated at 2022-06-13 16:38:12.810747
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class MockLock():
        def __enter__(self):
            return self

        def __exit__(self, exc_type, exc_val, exc_tb):
            return False

        def acquire(self):
            return False

        def release(self):
            return False

    class Mock():
        def __init__(self):
            self.lock = MockLock()

        @lock_decorator(attr='lock')
        def method_with_attr(self):
            return None

        @lock_decorator(lock=MockLock())
        def method_with_lock(self):
            return None

    with Mock() as mock:
        assert mock.method_with_attr() is None
        assert mock.method_with_lock() is None

# Function to print an error message before raising an exception

# Generated at 2022-06-13 16:38:20.118268
# Unit test for function lock_decorator
def test_lock_decorator():
    from ansible.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import lock_decorator

    module = AnsibleModule({'ANSIBLE_MODULE_ARGS': {'test': 'lock_decorator'}})

    # Testing with an instance attribute
    class LockDecoratorClass(object):
        def __init__(self, module):
            self._callback_lock = module.lock()
            self.result = None
            self.cb_invoked = False

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, result=None, **kwargs):
            self.result = result
            self.cb_invoked = True


    with module.connection_lock:
        obj

# Generated at 2022-06-13 16:38:28.421503
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class A:
        def __init__(self):
            self.lock_attr = threading.Lock()
            self._x = 0

        @lock_decorator(attr='lock_attr')
        def a(self):
            self._x += 1

        @lock_decorator(lock=threading.Lock())
        def b(self):
            self._x -= 1

    obj = A()
    assert obj._x == 0

    obj.a()
    obj.a()
    assert obj._x == 2

    obj.b()
    obj.b()
    assert obj._x == 0

# Generated at 2022-06-13 16:38:38.368570
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    import threading
    import time

    class LockObject(object):
        def __init__(self):
            self._lock = threading.Lock()
            self._n = 0

        @lock_decorator(attr='_lock')
        def increment(self):
            self._n += 1
            assert self._n == 1

        @lock_decorator(attr='_lock')
        def decrement(self):
            self._n -= 1
            assert self._n == -1

    obj = LockObject()

    # increment and decrement should run sequentially
    for _ in range(1000):
        obj.increment()
        obj.decrement()

    # Let's try to increment and decrement concurrently
    def run(method):
        for _ in range(1000):
            method()

    #

# Generated at 2022-06-13 16:38:47.710919
# Unit test for function lock_decorator
def test_lock_decorator():
    '''
    This unit test verifies that the lock_decorator() decorator works
    as expected.
    '''
    import threading
    from mock import patch

    # We are going to use a mock lock
    mock_lock = threading.Lock()

    # The following is a mock method that we will decorate
    @lock_decorator(attr='_pre_attr_lock')
    def pre_attr_lock_method(self):
        '''
        This methods sets a mock instance attribute
        value and returns the value
        '''
        self.pre_attr_lock_value = 'foo'
        return self.pre_attr_lock_value

    # The following is a mock method that sets a mock instance
    # attribute value.

# Generated at 2022-06-13 16:38:56.838671
# Unit test for function lock_decorator
def test_lock_decorator():
    '''Test lock_decorator using a simple class definition.'''
    import threading
    class Test():
        '''Test class to implement lock_decorator tests'''
        def __init__(self):
            self._obj_lock = threading.Lock()

        @lock_decorator(attr='_obj_lock')
        def method_with_attr(self, p1, p2):
            return p1 + p2

        @lock_decorator(lock=threading.Lock())
        def method_with_lock(self, p1, p2):
            return p1 + p2

        @lock_decorator()
        def method_with_nothing(self, p1, p2):
            '''This will raise an exception, since there is no lock to run
            with.
            '''
           

# Generated at 2022-06-13 16:39:09.091760
# Unit test for function lock_decorator
def test_lock_decorator():
    # Create mocks and stubs
    calls = []
    mock_func = lambda *args, **kwargs: calls.append(('func', args, kwargs))
    _lock = lambda: calls.append('lock context manager')
    _lock.acquire = lambda: calls.append('acquired lock')
    _lock.release = lambda: calls.append('released lock')
    _lock.__enter__ = lambda: calls.append('acquired lock')
    _lock.__exit__ = lambda exc, type, value, traceback: calls.append('released lock')
    wrapped = lock_decorator(lock=_lock)(mock_func)
    # Call wrapped method
    wrapped()
    # Did we acquire and release lock
    assert calls[0] == 'acquired lock'

# Generated at 2022-06-13 16:39:20.210964
# Unit test for function lock_decorator
def test_lock_decorator():
    import pytest
    from threading import Thread, Lock

    # Set up
    class Instance(object):
        '''Set up the bare minimum to use lock_decorator'''
        # Create two instances, to test cross Instance interactions
        _lock = Lock()

        # Create two methods, locking on same and different lock objects
        @lock_decorator(attr='_lock')
        def method_same_lock(self, i):
            '''Locking on ``self._lock``'''
            setattr(self, '_val_%d' % i, i)

        @lock_decorator(lock=Lock())
        def method_different_lock(self, i):
            '''Locking on a new lock object'''
            setattr(self, '_val_%d' % i, i)

    #

# Generated at 2022-06-13 16:39:30.934461
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    import types

    class SomeClass(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = None

        def setter(self, value):
            self.value = value

        @lock_decorator(lock=self.lock)
        def setter_lock(self, value):
            self.value = value

        @lock_decorator('lock')
        def setter_lock_attr(self, value):
            self.value = value

    @lock_decorator(lock=SomeClass().lock)
    def set_value(value):
        SomeClass().value = value


    def test_lock(lock):
        value = None

        def thread_1():
            nonlocal value

# Generated at 2022-06-13 16:39:40.700276
# Unit test for function lock_decorator
def test_lock_decorator():
    class Test(object):
        pass
    t = Test()
    t._callback_lock = lock = threading.Lock()
    lock.acquire = lambda: print("Acquired lock")
    lock.release = lambda: print("Released lock")

    @lock_decorator(attr="_callback_lock")
    def send_callback(a, b):
        return "Answer is {0}".format(a + b)

    send_callback(t, 1, 2)

    @lock_decorator(lock=threading.Lock())
    def send_callback(a, b):
        return "Answer is {0}".format(a + b)

    send_callback(None, 1, 2)

# Generated at 2022-06-13 16:39:47.348002
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    called = {'send_callback': 0}
    class Test(object):
        _callback_lock = threading.Lock()
        @lock_decorator(attr='_callback_lock')
        def send_callback(self, *args, **kwargs):
            called['send_callback'] += 1

        @lock_decorator()
        def no_args_method(self):
            pass

        @lock_decorator(lock=list())
        def broken_method(self):
            pass

    # Test that passing the lock as a kwarg to the decorator works
    class TestKwargs(object):
        @lock_decorator(lock=threading.Lock())
        def send_callback(self, *args, **kwargs):
            pass

    # Test that passing the lock as a k

# Generated at 2022-06-13 16:39:57.333241
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()
    counter = 0

    @lock_decorator(lock=lock)
    def update_counter():
        global counter
        counter += 1

    def _thread(thread_lock, thread_counter):
        for i in range(100):
            with thread_lock:
                thread_counter += 1

    threads = []
    for i in range(10):
        t = threading.Thread(target=_thread, args=(lock, counter))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    for i in range(100):
        update_counter()

    print(counter)
    assert counter == 1000



# Generated at 2022-06-13 16:40:05.757950
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest

    from threading import Lock, Thread

    class TestLockDecorator(unittest.TestCase):
        def test_attr(self):
            class Test(object):
                def __init__(self):
                    self._lock = Lock()

                    self._locked_value = False

                    self.result = 0

                @lock_decorator(attr='_lock')
                def method(self):
                    self._locked_value = True
                    self.result = 1

                @lock_decorator(attr='_lock')
                def locked(self):
                    return self._locked_value

            test = Test()
            self.assertEqual(test.locked(), False)

            self.assertEqual(test.result, 0)
            test.method()
            self.assertEqual(test.result, 1)

# Generated at 2022-06-13 16:40:13.386136
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    # These inner functions should pass the test
    # when compiled and executed under Python2 and 3
    class Foo(object):
        # fake lock
        _lock = threading.Lock()
        @lock_decorator(attr='_lock')
        def method_a(self):
            pass

        @lock_decorator(lock=threading.Lock())
        def method_b(self):
            pass
    assert True

# Generated at 2022-06-13 16:40:24.092040
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def wrap(self):
            assert self._lock.locked()

    class Test2(object):
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(lock=self._lock)
        def wrap(self):
            assert self._lock.locked()

    assert not Test.wrap.__name__ == 'wrap'
    assert not Test.wrap.__name__ == 'inner'

# Generated at 2022-06-13 16:40:33.929660
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading

    class M(object):
        def __init__(self):
            # Each instance needs its own lock because it is used
            # on class methods.
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        @classmethod
        def foo(cls):
            # Simulate something that verifies that it is locked
            # and needs a lock.
            assert cls._lock._is_owned()
            return True


    assert isinstance(M._lock, threading.Lock)

    m = M()
    assert m.foo()

    # Simulate a class method by passing the class
    assert M.foo()

    class ClassWithLock(object):
        def __init__(self):
            self.shared_lock = threading.Lock()

        # Instance

# Generated at 2022-06-13 16:40:51.055068
# Unit test for function lock_decorator
def test_lock_decorator():
    class Foo(object):

        _callback_lock = None

        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            # Some kind of callback
            pass

        @lock_decorator(lock=threading.Lock())
        def some_method(self):
            # Some kind of method
            pass

        @lock_decorator
        def some_method_without_lock(self):
            # Some kind of method
            pass

    f = Foo()
    f.send_callback()
    f.some_method()
    f.some_method_without_lock()

# Generated at 2022-06-13 16:41:01.112990
# Unit test for function lock_decorator
def test_lock_decorator():
    __tracebackhide__ = True
    import threading
    from ansible.module_utils._text import to_text

    class A:

        def __init__(self):
            # Require the instantiated lock to be on the object for
            # this test to ensure it isn't missed
            self._lock = threading.Lock()

        @lock_decorator(attr='_lock')
        def run(self):
            return 'Yay!'

    test_object = A()
    assert test_object.run() == 'Yay!'

    class B:
        @lock_decorator(lock=threading.Lock())
        def run(self):
            return 'Yay!'

    test_object = B()
    assert test_object.run() == 'Yay!'


# Generated at 2022-06-13 16:41:05.140070
# Unit test for function lock_decorator
def test_lock_decorator():

    from collections import defaultdict

    from threading import Thread, Lock

    class MyClass(object):
        # Simulate a lock at the instance level
        _func_lock = Lock()

        # Simulate a lock at the class level
        _class_lock = Lock()

        @lock_decorator(attr='_func_lock')
        def func_with_instance_lock(self, lst):
            lst.append(self)
            return lst

        @lock_decorator(attr='_class_lock')
        def func_with_class_lock(self, lst):
            lst.append(self)
            return lst

        @classmethod
        @lock_decorator(attr='_class_lock')
        def class_func_with_class_lock(cls, lst):
            lst

# Generated at 2022-06-13 16:41:15.801512
# Unit test for function lock_decorator
def test_lock_decorator():
    # define a test class
    class TestLock:
        def __init__(self):
            self._lock = 'original lock'

        @lock_decorator(attr='_lock')
        def test_attr_lock(self, lock):
            '''verify self._lock is the original lock'''
            return self._lock == lock

        @lock_decorator(lock='new lock')
        def test_supplied_lock(self, lock):
            '''verify self._lock is not the lock'''
            return self._lock != lock

    # instantiate the object
    test_obj = TestLock()
    # verify that the _lock attr is the original lock
    assert test_obj._lock == 'original lock'
    # verify the methods are calling the correct lock

# Generated at 2022-06-13 16:41:22.547532
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class TestClass(object):
        @lock_decorator(attr='_lock')
        def method(self):
            return 'method'

        @lock_decorator(lock=threading.Lock())
        def method2(self):
            return 'method2'

    t = TestClass()
    t._lock = threading.Lock()
    assert t.method() == 'method'
    assert t.method2() == 'method2'

# Generated at 2022-06-13 16:41:31.317201
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.value = 0

        @lock_decorator(attr='lock')
        def update_value(self, value):
            self.value += value

    test = Test()

    def test_thread(num):
        for _ in range(num):
            test.update_value(1)

    thread1 = threading.Thread(target=test_thread, args=(5,))
    thread2 = threading.Thread(target=test_thread, args=(5,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    assert test.value == 10


# pylint: disable=invalid-name,too-many-

# Generated at 2022-06-13 16:41:40.224221
# Unit test for function lock_decorator
def test_lock_decorator():
    from threading import Thread, Lock

    class CallbackBase(object):
        def __init__(self):
            self._callback_lock = Lock()
            self.notified_callback = False

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            # should not be called twice
            assert self.notified_callback is False
            self.notified_callback = True

    class CallbackReceiver(CallbackBase):
        def __init__(self):
            super(CallbackReceiver, self).__init__()

        def wait_for_callback(self):
            # Wait until the callback is called
            while self.notified_callback is False:
                pass


# Generated at 2022-06-13 16:41:45.133213
# Unit test for function lock_decorator
def test_lock_decorator():
    try:
        import threading
    except ImportError:
        return

    class LockTester(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, name, *args, **kwargs):
            pass

        @lock_decorator(lock=threading.Lock())
        def some_method(self, name, *args, **kwargs):
            pass

    LockTester()

# Generated at 2022-06-13 16:41:54.432641
# Unit test for function lock_decorator
def test_lock_decorator():

    class TestClass(object):
        def __init__(self):
            import threading
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self):
            # this is a dummy
            return

    obj = TestClass()

    @lock_decorator(lock=obj._callback_lock)
    def test_func():
        # this is a dummy
        return

    # Supposedly, this is race-free
    if obj.send_callback == test_func:
        raise Exception('Function decorator failed')

# Generated at 2022-06-13 16:42:01.420709
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    thread_lock = threading.Lock()

    class Example(object):
        def __init__(self, *args, **kwargs):
            self._lock = threading.Lock()

        @lock_decorator(lock=thread_lock)
        def thread_lock_example(self):
            return 'thread_lock_example'

        @lock_decorator(attr='_lock')
        def object_lock_example(self):
            return 'object_lock_example'

    e = Example()
    assert e.thread_lock_example() == 'thread_lock_example'
    assert e.object_lock_example() == 'object_lock_example'

# Generated at 2022-06-13 16:42:27.894675
# Unit test for function lock_decorator
def test_lock_decorator():
    import os
    import threading
    import tempfile
    import time

    class TestClass(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.some_global = 0
            self.missing_lock_attr = None
            self.test_file = tempfile.mktemp(dir=tempfile.gettempdir())

        @lock_decorator(lock=self.lock)
        def some_method(self):
            self.some_global += 1

        # Method has a side-effect of writing contents to a file.
        @lock_decorator(attr='lock')
        def method_with_file_side_effect(self, contents):
            with open(self.test_file, 'w') as fd:
                fd.write(contents)

    # instant

# Generated at 2022-06-13 16:42:32.904375
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo(object):
        _lock = threading.RLock()

        @lock_decorator(attr='_lock')
        def method1(self):
            print('method1')

        @lock_decorator(lock=threading.RLock())
        def method2(self):
            print('method2')

    foo = Foo()
    foo.method1()
    foo.method2()



# Generated at 2022-06-13 16:42:44.281484
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    lock = threading.Lock()

    class Test():
        def __init__(self, lock):
            self.lock = lock
            self.foo = 0
            self.bar = 0

        @lock_decorator(attr='lock')
        def test_method(self):
            self.foo += 1

        @lock_decorator(lock=lock)
        def test_method2(self):
            self.bar += 1

    test_instance = Test(lock)

    threads = []
    for x in range(100):
        threads.append(threading.Thread(target=test_instance.test_method))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    threads = []
    for x in range(100):
        threads.append

# Generated at 2022-06-13 16:42:53.606248
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    class Dummy(object):
        def __init__(self, lock=None):
            if lock is None:
                self._lock = threading.Lock()
            else:
                self._lock = lock
            self.counter = 0
            self.condition = threading.Condition()

        @lock_decorator(attr='_lock')
        def increment(self):
            self.counter += 1

        @lock_decorator(lock=threading.Lock())
        def increment2(self):
            self.counter += 1

        @lock_decorator(attr='condition')
        def increment3(self):
            self.counter += 1

    dummy = Dummy()
    dummy.increment()
    assert dummy.counter == 1


# Generated at 2022-06-13 16:43:03.050981
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class T():
        def __init__(self):
            self._lock = threading.Lock()
            self._data = 'foo'

        @lock_decorator(attr='_lock')
        def with_attr(self, value='bar'):
            self._data = value

        @lock_decorator(lock=threading.Lock())
        def with_lock(self, value='baz'):
            self._data = value

    t = T()
    assert t._data == 'foo'
    t.with_attr()
    assert t._data == 'bar'
    t._data = 'foo'
    t.with_lock()
    assert t._data == 'baz'

# Generated at 2022-06-13 16:43:11.760622
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Test(object):
        def __init__(self):
            self._callback_lock = threading.Lock()

        @lock_decorator(attr='_callback_lock')
        def send_callback(self, *args, **kwargs):
            self.some_var = 'Some value'

    class Test2(object):
        lock = threading.Lock()
        # Callable lock for testing
        def _is_locked(self):
            return self.lock.locked()

        @lock_decorator(lock=lock)
        def some_method(self, *args, **kwargs):
            self.some_var = 'Some value'

    t = Test()
    t2 = Test()
    t3 = Test2()

    # Ensure send_callback locks
    assert t.send_callback

# Generated at 2022-06-13 16:43:19.712614
# Unit test for function lock_decorator
def test_lock_decorator():

    class TestClass(object):
        def __init__(self):
            self.test_lock = 0

        @lock_decorator(attr='test_lock')
        def test_method(self):
            self.test_lock += 1

    t = TestClass()
    t.test_method()
    assert t.test_lock == 1

    @lock_decorator(lock=t.test_lock)
    def test_method_lock():
        t.test_lock += 1

    test_method_lock()
    assert t.test_lock == 2

# Generated at 2022-06-13 16:43:25.220900
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Foo(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.result = None

        def foo(self, result=None):
            with self._lock:
                self.result = 'set'

    class FooDecorate:
        def __init__(self):
            self._lock = threading.Lock()
            self.result = None

        @lock_decorator(attr='_lock')
        def foo(self, result=None):
            self.result = 'set'

    foo = Foo()
    foo_decorate = FooDecorate()
    foo2 = Foo()
    foo2_decorate = FooDecorate()
    thread = threading.Thread(target=foo.foo, args=(1,))

# Generated at 2022-06-13 16:43:29.230379
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time

    class L(object):
        def __init__(self):
            self.count = 0
            self.lock = threading.Lock()
            self.func_lock = lock_decorator(attr='lock')

        @lock_decorator(attr='lock')
        def count_up(self, amt=1):
            self.count += amt

        def count_up_func(self, amt=1):
            self.count += amt

        @lock_decorator(lock=threading.Lock())
        def count_up_lock(self, amt=1):
            self.count += amt

        def count_up_func_call(self, amt=1):
            self.count_up_func(amt)


# Generated at 2022-06-13 16:43:39.127376
# Unit test for function lock_decorator
def test_lock_decorator():

    import threading
    import time

    class TestA(object):
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator(attr='lock')
        def add(self, a, b):
            time.sleep(0.1)
            return a + b

    class TestB(object):
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator(lock=self.lock)
        def add(self, a, b):
            time.sleep(0.1)
            return a + b

    class TestC(object):
        def __init__(self):
            self.lock = threading.Lock()

        @lock_decorator()
        def add(self, a, b):
            time.sleep

# Generated at 2022-06-13 16:44:25.886594
# Unit test for function lock_decorator
def test_lock_decorator():
    import time
    import threading

    class Test(object):
        def __init__(self):
            self._lock = threading.Lock()
            self.messages = []

        @lock_decorator(attr='_lock')
        def append_message(self, message):
            time.sleep(0.02)
            self.messages.append(message)

    test_obj = Test()
    def t1():
        for i in range(100):
            test_obj.append_message('t1')

    def t2():
        for i in range(100):
            test_obj.append_message('t2')

    ts = [threading.Thread(target=t1), threading.Thread(target=t2)]
    for t in ts:
        t.start()

# Generated at 2022-06-13 16:44:37.176613
# Unit test for function lock_decorator
def test_lock_decorator():
    import unittest
    import threading
    import time

    class TestRunner(unittest.TestCase):
        # Define lock
        lock = threading.Lock()

        # Define class attribute
        test_class_attr = threading.Lock()

        @lock_decorator(attr='test_class_attr')
        def test_class_lock(self):
            # Use a 1 second timeout to attempt to lock
            # the thread will sleep for 2 seconds now
            # and the lock will fail, skipping the assert
            with self.lock.acquire_timeout(timeout=1):
                # Wait 2 seconds, to test the lock above
                time.sleep(2)

                # Assert that the global variable was incremented
                # this will only happen if we successfully locked it
                # and called the method
                self.assertEqual

# Generated at 2022-06-13 16:44:44.773076
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class TestModule(object):
        def __init__(self):
            self.test_lock1 = threading.Lock()
            self.test_lock2 = threading.Lock()

        @lock_decorator(attr='test_lock1')
        def method1(self):
            '''Test that the lock_decorator passes for a pre-defined instance lock.'''
            return

        @lock_decorator(lock=threading.Lock())
        def method2(self):
            '''Test that the lock_decorator passes for a passed in lock.'''
            return

        @lock_decorator(attr='test_lock2')
        def method3(self):
            '''Test that the lock_decorator passes for a pre-defined instance lock when expecting an exception.'''
            raise Exception

# Generated at 2022-06-13 16:44:54.967698
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    import time
    class MyThing(object):
        def __init__(self, value=0):
            self.lock = threading.Lock()
            self._value = value
        @lock_decorator(attr='lock')
        def setter(self, new_val):
            self._value += new_val
        @lock_decorator(attr='lock')
        def getter(self):
            return self._value
    thing = MyThing()
    assert thing.getter() == 0
    running = True
    def setter_once_every_second():
        time.sleep(0.2)
        thing.setter(1)
        time.sleep(0.2)
        running = False
    t = threading.Thread(target=setter_once_every_second)


# Generated at 2022-06-13 16:45:03.619997
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading

    class Foo:
        def __init__(self, value=None):
            self.value = value
            self.count = 0
            self._lock = threading.Lock()

        @lock_decorator
        def increment(self):
            self.count += 1
            return self.count

        @lock_decorator(attr='_lock')
        def change_value(self, new_value):
            self.value = new_value
            return self.value

    foo = Foo(value='old_value')

    assert foo.count == 0
    assert foo.value == 'old_value'

    foo.increment()
    assert foo.count == 1

    foo.change_value('new_value')
    assert foo.value == 'new_value'

# Generated at 2022-06-13 16:45:12.844216
# Unit test for function lock_decorator
def test_lock_decorator():
    # Imports
    from threading import Lock
    from time import sleep
    from unittest import TestCase

    # Unit test class
    class Test(object):
        def __init__(self):
            self._lock = Lock()

        @lock_decorator(attr='_lock')
        def test_with_instance_attr(self):
            # This code is not expected to conflict
            # with other threads
            sleep(1)

        @lock_decorator(lock=Lock())
        def test_with_explicit_lock(self):
            # This code is not expected to conflict
            # with other threads
            sleep(1)

    # Tests
    class TestLockDecorator(TestCase):
        def test_with_instance_attr(self):
            obj = Test()

# Generated at 2022-06-13 16:45:23.230804
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    mutex = threading.Lock()
    class Test():
        mutex = threading.Lock()
        def test_attr(self, var1, var2, var3):
            self.mutex.acquire()
            try:
                print('This is attribute mutex test')
            finally:
                self.mutex.release()
        @lock_decorator(attr='mutex')
        def test_attr_dec(self, var1, var2, var3):
            print('This is attribute mutex test with decorator')
        @lock_decorator(lock=mutex)
        def test_lock(self, var1, var2, var3):
            print('This is lock test with decorator')
    t = Test()
    t.test_attr(1,2,3)
   

# Generated at 2022-06-13 16:45:26.592728
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    class Foo:
        def __init__(self):
            self._lock = threading.Lock()

        @lock_decorator(lock=None)
        def do_thing(self):
            print(self._lock)

    x = Foo()
    x.do_thing()

# Generated at 2022-06-13 16:45:34.545584
# Unit test for function lock_decorator
def test_lock_decorator():
    import threading
    lock = threading.Lock()
    @lock_decorator(lock=lock)
    def test1(a, b=5):
        return a + b
    @lock_decorator(attr='_lock')
    def test2(self, a, b=5):
        return a + b

    class TestClass(object):
        def __init__(self):
            self._lock = threading.Lock()

        def test3(self, a, b=5):
            return a + b

    obj = TestClass()

    assert test1(1) == 6
    assert test2(obj, 1) == 6
    assert obj.test3(1) == 6

# Generated at 2022-06-13 16:45:42.984028
# Unit test for function lock_decorator
def test_lock_decorator():
    import ansible.module_utils.six as six
    if six.PY2:
        import __builtin__ as builtins
        lock = builtins.__dict__
    else:
        import builtins as builtins
        lock = builtins

    lock['attr'] = '_callback_lock'