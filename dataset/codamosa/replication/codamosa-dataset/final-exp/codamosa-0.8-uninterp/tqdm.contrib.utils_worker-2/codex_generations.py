

# Generated at 2022-06-14 13:42:41.954448
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    # simulate time-consuming job
    def long_job(i, secs):
        time.sleep(secs)
        return secs

    mw = MonoWorker()
    tqdm_auto.write("mw = MonoWorker()\n")
    for i, secs in enumerate([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
                              0.01, 0.01, 0.01, 0.05, 0.05, 0.1, 0.1, 0.1, 0.1]):
        mw.submit(func=long_job, i=i, secs=secs)
        time.sleep(random.uniform(0.0, 0.5))

# Generated at 2022-06-14 13:42:51.892657
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, threading
    def worker(arg1, arg2, sleep_time=0, throws=False):
        time.sleep(sleep_time)
        if throws:
            raise Exception(str(locals()))
        return arg1, arg2
    mw = MonoWorker()
    main_thread = threading.current_thread()
    assert main_thread.ident != mw.submit(worker, 1, 2, sleep_time=0.5).result()[0]
    t = mw.submit(worker, 1, 2, sleep_time=0.5)
    assert t.result() == (1, 2)
    t = mw.submit(worker, 3, 4, sleep_time=0.5)
    assert t.result() == (3, 4)
    time.sleep(0.1)


# Generated at 2022-06-14 13:43:01.229743
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    import multiprocessing
    import sys
    import os

    message_log = []

    def tqdm_worker():
        """Worker that writes to tqdm."""
        time.sleep(0.01)
        tqdm_auto.write('.')
        message_log.append('.')

    def print_worker():
        """Worker that writes to stdout."""
        sys.stdout.write('.')
        sys.stdout.flush()
        message_log.append('.')

    def queue_worker(q):
        """Worker that writes to a queue."""
        q.put('.')
        message_log.append('.')


# Generated at 2022-06-14 13:43:10.078880
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    It is OK if no error message is generated.
    """
    import time

    def sleep_then_print(n_seconds):
        time.sleep(n_seconds)
        print('Hi!')

    w = MonoWorker()
    w.submit(sleep_then_print, 0.1)
    time.sleep(0.2)
    w.submit(sleep_then_print, 0.1)
    time.sleep(0.3)
    w.submit(sleep_then_print, 0.1)
    time.sleep(0.4)
    assert len(w.futures) == 1

# Generated at 2022-06-14 13:43:17.190521
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from nose.tools import assert_equal, assert_false
    from time import sleep

    def raise_error():
        sleep(3)
        raise Exception('error')

    def wait_for_task():
        sleep(5)

    mono_worker = MonoWorker()
    error_running = mono_worker.submit(raise_error)
    wait_running = mono_worker.submit(wait_for_task)
    sleep(4)
    mono_worker.submit(wait_for_task)
    assert_false(wait_running.done())
    assert_false(error_running.done())
    sleep(2)
    assert_false(wait_running.done())
    assert_equal(error_running.exception(), Exception('error'))

# Generated at 2022-06-14 13:43:23.928898
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from multiprocessing import Lock

    def one_task(counter, lock):
        """Prints its arguments and increments counter."""
        with lock:
            print(counter, "acquired")
        time.sleep(1)
        with lock:
            print(counter, "released")
        return counter + 1

    lock = Lock()
    counter = 0
    w = MonoWorker()
    for i in range(3):
        w.submit(one_task, counter, lock)
        counter = w.futures[-1].result()

# Generated at 2022-06-14 13:43:29.757808
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from multiprocessing import Process, Queue
    from time import sleep
    from itertools import product
    from random import shuffle

    def in_process(func, *args, **kwargs):
        """Wrapper for function to run within process."""
        def proxy(queue):
            queue.put(func(*args, **kwargs))
        queue = Queue()
        p = Process(target=proxy, args=(queue,))
        p.start()
        ret = queue.get()
        p.join(0.01)  # timeout
        p.terminate()
        p.join()
        return ret

    def throw(exception=ValueError, *args, **kwargs):
        """Throw an exception."""
        raise exception(*args, **kwargs)


# Generated at 2022-06-14 13:43:41.050721
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:43:46.015325
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test that calling submit() 1 to 2 times works"""
    def dummy():
        return 'dummy'

    mono = MonoWorker()
    assert mono.submit(dummy).result() == 'dummy'
    assert mono.submit(dummy).result() == 'dummy'


if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:43:53.580536
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Increase the worker timeout to avoid failures on slow systems
    worker = MonoWorker()
    for i in range(4):
        worker.submit(tqdm_auto.sleep, 1)
    for _ in worker.futures:
        for j in range(4):
            worker.submit(tqdm_auto.sleep, 1)
        tqdm_auto.sleep(2)
    for _ in worker.futures:
        tqdm_auto.sleep(2)

    class TestException(Exception):
        pass

    def raise_exc(i, exc=TestException):
        raise exc(i)
    assert worker.submit(raise_exc, 1).exception()
    assert worker.submit(raise_exc, 2, exc=RuntimeError).exception()

# Generated at 2022-06-14 13:44:04.168916
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import multiprocessing
    import os
    import time

    def f(x):
        time.sleep(1)
        return x

    def g(x):
        a = [x] * 10000000
        return os.getpid()

    def h(x):
        time.sleep(1)
        raise ZeroDivisionError(x)

    num_worker = multiprocessing.cpu_count()
    # one running, one waiting:
    mw = MonoWorker()
    assert len(mw.pool._pool) == min(mw.pool._max_workers, num_worker)
    assert len(mw.futures) == 0

    future1 = mw.submit(f, 1)
    assert len(mw.futures) == 1
    assert future1.running()


# Generated at 2022-06-14 13:44:12.583715
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """ Unit tests """
    import time

    def func(x):
        """ Simple function that waits x seconds and returns x*x """
        time.sleep(x)
        return x*x

    tqdm_auto.tqdm = lambda x: x
    # create MonoWorker
    mw = MonoWorker()
    # submit sequential jobs
    # assert(len(mw.futures) == 0)
    assert(mw.futures.maxlen == 2)
    future_5 = mw.submit(func, 5)
    assert(mw.futures.maxlen == 2)
    assert(len(mw.futures) == 1)
    assert(mw.futures[0] == future_5)
    # assert(future_5.result() == 25) # NOT done yet

# Generated at 2022-06-14 13:44:21.535284
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    worker = MonoWorker()
    f1 = worker.submit(time.sleep, 0.5)
    f2 = worker.submit(time.sleep, 0.5)  # will not run
    f2_result = worker.submit(time.sleep, 0.5)  # should not run
    assert f1.done()
    assert not f2.done()
    assert f2 == f2_result
    assert not f2.done()
    f2.cancel()
    f2 = worker.submit(time.sleep, 0.5)  # should run
    assert not f2.done()
    time.sleep(1)
    assert f2.done()

# Generated at 2022-06-14 13:44:31.012228
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import pytest
    from concurrent.futures import CancelledError
    from .signals import tqdm_handler

    # Prevent CTRL+C from causing KeyboardInterrupt error
    # which may cause this unit test failed
    tqdm_handler(signum=0, frame=None)

    def worker(i, t):
        """worker to test MonoWorker"""
        time.sleep(t)
        return i

    # test one worker
    mono_woker = MonoWorker()
    assert mono_woker.submit(worker, 1, 3) is None
    time.sleep(1)
    assert mono_woker.submit(worker, 2, 5) is None
    time.sleep(1)
    assert mono_woker.submit(worker, 3, 7) is None
    assert mono_woker.f

# Generated at 2022-06-14 13:44:41.770045
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    worker = MonoWorker()
    # test no task running
    worker.submit(lambda: 1)
    assert len(worker.futures) == 1
    # test one running task and one waiting task
    worker.submit(lambda: 2)
    assert len(worker.futures) == 2
    # test one running task and one running task
    worker.submit(lambda: 3)
    assert len(worker.futures) == 1
    assert list(worker.futures) == [worker.submit(lambda: 3)]
    # test one running task and one running task and one waiting task
    worker.submit(lambda: 4)
    assert len(worker.futures) == 2
    assert list(worker.futures) == [worker.submit(lambda: 4),
                                    worker.submit(lambda: 3)]
    #

# Generated at 2022-06-14 13:44:51.739211
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Lock
    from random import choice
    from string import ascii_letters
    from copy import copy

    q = MonoWorker()
    lock = Lock()
    output = []

    def concurrent_append(x):
        sleep(0.02)
        with lock:
            output.append(x)

    for _ in tqdm_auto.trange(1000, desc='testing'):
        r = ''.join(choice(ascii_letters) for _ in range(100))
        concurrent_append(r)
        q.submit(concurrent_append, copy(r))
        assert len(output) in (1, 2)

    q.pool.shutdown(wait=True)  # to avoid ResourceWarning upon exit

    assert len(output) == 1000

# Generated at 2022-06-14 13:44:59.320482
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Tests the method submit of class MonoWorker."""
    import time
    from threading import Lock
    assert MonoWorker.__doc__  # Don't remove this line!

    lock = Lock()
    def func(i):
        # time.sleep(0.1)
        lock.acquire()
        try:
            print("{}".format(i))
        finally:
            lock.release()
        return i

    m = MonoWorker()
    assert not m.futures

    # Test 1
    m.submit(func, 0)
    assert len(m.futures) == 1
    assert m.futures[0].result() == 0

    # Test 2
    m.submit(func, 1)
    assert len(m.futures) == 1
    assert m.futures

# Generated at 2022-06-14 13:45:10.540004
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def _test(func, *args, **kwargs):
        """Test `MonoWorker.submit()` and expected side effects."""
        def _printed_elsewhere(nlines):
            """Return if printed by a worker."""
            return len(tqdm_auto.verified_printed.splitlines()) >= nlines

        tqdm_auto.verified_printed = ""
        assert not tqdm_auto.verified_printed
        mw = MonoWorker()
        prevlines = len(tqdm_auto.verified_printed.splitlines())
        r = mw.submit(func, *args, **kwargs)
        assert r and not r.done()
        assert _printed_elsewhere(prevlines)

        mw.futures.clear()

# Generated at 2022-06-14 13:45:19.561666
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Thread
    from tqdm.contrib.concurrency import MonoWorker, DummyTqdmFile

    def print_thread_info(worker):
        """Helper for test_MonoWorker_submit"""
        with DummyTqdmFile() as dummy:
            t = Thread(target=worker.submit,
                       args=(lambda dummy=dummy: dummy.write('asdf'),))
            t.start()
            t.join()

    worker = MonoWorker()
    print_thread_info(worker)

    # Test the one task at a time limit
    t = Thread(target=print_thread_info, args=(worker,))
    t.start()
    assert t.is_alive()
    time.sleep(0.5)
    print_thread_info(worker)  #

# Generated at 2022-06-14 13:45:30.255638
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from random import random
    from time import sleep
    import multiprocessing
    from .utils import get_exception
    NUM_PROCESSES = 10
    worker = MonoWorker()
    results = [worker.submit(sleep, random() / 10) for _ in range(NUM_PROCESSES)]
    for r in results:
        r.cancel()
    # Should now have a running task and a waiting task (the most recent)
    # Plus NUM_PROCESSES - 2 cancelled tasks
    # But we need to allow a little time for NUM_PROCESSES - 1 processes to complete
    sleep(2)
    # Ensure that NUM_PROCESSES - 1 processes actually completed
    assert {r.done() for r in results} == {True, False}
    # Ensure that the running task is not cancelled

# Generated at 2022-06-14 13:45:41.114083
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import threading
    import time
    from .threading import ThreadingBar, tqdm

    def this(msg):
        time.sleep(1)
        tqdm_auto.write(msg)
        return msg

    bar = ThreadingBar('MonoWorker', position=5)
    worker = MonoWorker()
    try:
        for i in tqdm(range(10)):
            worker.submit(this, "MonoWorker %d" % i)
    finally:
        bar.close()



# Generated at 2022-06-14 13:45:52.004241
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def f(x):
        time.sleep(1)
        return x

    mw = MonoWorker()
    assert mw.submit(f, 1).result() == 1  # passes
    assert mw.submit(f, 2).result() == 1  # cancels previous
    assert mw.submit(f, 3).result() == 3  # passes
    assert mw.submit(f, 4).result() == 3  # cancels previous
    assert mw.submit(f, 5).result() == 5  # passes
    try:
        mw.submit(f, 6).result()
    except Exception as e:
        assert str(e) == "Worker was killed: live: 1, dead: 0"  # cancelled

# Generated at 2022-06-14 13:46:00.817588
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def _test_submit(mw):
        def f(i):
            import time
            time.sleep(1)
            return i
        f1 = mw.submit(f, 1)
        f2 = mw.submit(f, 2)
        f3 = mw.submit(f, 3)
        f4 = mw.submit(f, 4)
        assert f1.result() == 2
        assert f2.cancelled()
        assert f3.cancelled()
        assert f4.cancelled()

    # Test with a MonoWorker
    mw = MonoWorker()
    try:
        _test_submit(mw)
    finally:
        mw.pool.shutdown(wait=True)

# Generated at 2022-06-14 13:46:09.471454
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test for `MonoWorker.submit`."""
    from time import sleep, time
    from .misc import loops
    from .tqdm_gui import tqdm_gui

    def wait_for(n):
        sleep(n)
        return n

    def do_submit():
        nonlocal worker
        for n in loops(5, 1, 'submit'):
            worker.submit(wait_for, n)

    worker = MonoWorker()

    monitor = tqdm_auto(total=0, dynamic_ncols=True, unit='job',
                        desc='test_MonoWorker_submit',
                        bar_format='{desc}: {postfix}')

# Generated at 2022-06-14 13:46:15.707629
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from functools import partial
    from random import random
    from ..auto import tqdm, trange

    def sleep_random(t):
        sleep(t * random())
        return 0

    with tqdm(total=100, leave=False) as t:
        mw = MonoWorker()
        for i in trange(10, desc='Submit task', leave=False):
            mw.submit(partial(sleep_random, 10))
            t.update()

# Generated at 2022-06-14 13:46:24.836169
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from concurrent.futures import TimeoutError
    from collections import Counter
    from .utils import ThreadsafeCounter

    def _test(mono_worker, c, n, wait=None):
        def f():
            if wait:
                time.sleep(wait)
            c.value += 1
            return c.value

        for i in range(n):
            assert mono_worker.submit(f) is None

        assert c.value == n
        assert mono_worker.futures[0].result() == n

    mono_worker = MonoWorker()
    _test(mono_worker, Counter(), n=1, wait=0.01)
    _test(mono_worker, ThreadsafeCounter(), n=100, wait=0.01)

# Generated at 2022-06-14 13:46:36.240159
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def f(x):
        time.sleep(x)
        return x

    worker = MonoWorker()

    print('\nSubmit long running task')
    worker.submit(f, 2)
    time.sleep(1)

    print('\nSubmit a task that will be cancelled')
    worker.submit(f, 2)
    time.sleep(1)

    print('\nSubmit another task that should be cancelled')
    worker.submit(f, 2)
    time.sleep(1)

    print('\nSubmit task that should be run')
    x = worker.submit(f, 0.5)
    x.result()  # wait for completion
    time.sleep(1)

    print('\nSubmit task that should be run')
    x = worker.submit(f, 0.5)
    x

# Generated at 2022-06-14 13:46:46.334519
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from unittest import TestCase

    class MockFuture(object):
        """Mock a concurrent.futures.Future, with a fake attribute `done`."""
        def __init__(self, done):
            self.done = done

        def cancel(self):
            pass

    def mock_submit(func, *args, **kwargs):
        """
        Mock a concurrent.futures.Executor.submit.
        Returns a MockFuture based on func's id.
        """
        # Odd `func`'s id's are "not done", even ones are "done"
        return MockFuture(False if id(func) % 2 else True)

    class TestMonoWorker(TestCase):
        """Test class `MonoWorker`."""

# Generated at 2022-06-14 13:46:53.154540
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test the MonoWorker class."""
    from ..utils import _range
    from time import sleep
    from random import random

    def counting_sleep(time, *dummy_args, **dummy_kwargs):
        """Sleep for a second or two, then return the time slept."""
        sleep(time)
        return time

    # try a monoworker for random times
    mw = MonoWorker()
    for _ in _range(5):
        sleeptime = 0.5 + random()
        future = mw.submit(counting_sleep, sleeptime)
        # we should get back the correct time slept
        time_slept = future.result()
        assert time_slept == sleeptime

    # try a longer sleep on the monoworker
    mw = MonoWorker()
    future0

# Generated at 2022-06-14 13:46:59.280236
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from random import randint
    from time import sleep
    from concurrent.futures import wait
    mw = MonoWorker()
    def f(name, delay):
        sleep(delay)
        return name
    futs = [mw.submit(f, str(i), randint(0, 2)) for i in range(10)]
    names = [n.result() for n in futs]
    assert len(set(names)) == 1

# Generated at 2022-06-14 13:47:13.962219
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def f(x, y=1):
        time.sleep(x)
        return x + y

    mw = MonoWorker()
    with tqdm_auto.tqdm(total=5) as pbar:
        for i in range(5):
            mw.submit(f, i, y=i)
            pbar.update()
    time.sleep(0.5)  # wait for last future (TODO: use a join)
    assert mw.futures
    assert mw.futures[0].result() == 9


if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:47:24.967943
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import sys
    import time

    def waiting_func(wait, d):
        time.sleep(wait)
        d.append(wait)

    worker = MonoWorker()

    d = []

    worker.submit(waiting_func, 0.5, d)
    worker.submit(waiting_func, 1.5, d)
    worker.submit(waiting_func, 2.5, d)

    time.sleep(2)

    worker.submit(waiting_func, 0.1, d)

    for _ in range(4):
        if all(len(d) == i for i in range(1, 4)):
            print("test_MonoWorker_submit: Success")
            sys.stdout.flush()
            return

# Generated at 2022-06-14 13:47:34.390126
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from os import _exit
    from multiprocessing import Process

    def print_later(i, *args, **kwargs):
        val = args[0]
        sleep(2)
        print(i, val)

    def make_print_later(i):
        def print_later(*args, **kwargs):
            val = args[0]
            sleep(1)
            print(i, val)
        return print_later

    N = 3
    M = 1
    p = Process(target=lambda: [MonoWorker().submit(print_later, i, M)
                                for i in range(N)])

    def test_worker_with_closures():
        """Test submit with closures"""
        p.start()
        p.join()
        _exit(0)
   

# Generated at 2022-06-14 13:47:45.657818
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event, Lock
    from concurrent.futures import as_completed
    from itertools import chain

    # test default maxlen
    mw = MonoWorker()
    assert mw.futures.maxlen == 2
    assert len(mw.futures) == 0

    # test maxlen
    mw = MonoWorker(maxlen = 10)
    assert mw.futures.maxlen == 10
    assert len(mw.futures) == 0
    try:
        mw.futures.maxlen = 0
    except ValueError:
        pass
    else:
        assert False
    mw.futures.maxlen = 20
    assert mw.futures.maxlen == 20

# Generated at 2022-06-14 13:47:51.284313
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    print("\nstart")
    def sleep(n):
        time.sleep(n)
        print("done", n)
    m = MonoWorker()
    m.submit(sleep, 2)
    time.sleep(.5)
    m.submit(sleep, 1)
    time.sleep(.5)
    m.submit(sleep, .5)
    time.sleep(.5)
    m.submit(sleep, .25)
    print("end")
    # Note that `tqdm.write` is thread-safe.

# Generated at 2022-06-14 13:48:02.559082
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    #from tqdm import tqdm
    import random
    import time
    random.seed(1)
    num_tests = 100
    num_worker = 2
    num_job = 100
    sum_wait = 0
    sum_run = 0
    sum_delay = 0
    sum_dur = 0
    sum_max_dur = 0
    sum_max_delay = 0
    m = MonoWorker()
    for idx in tqdm_auto.tqdm(range(num_tests), desc='test'):
        num_job_in_worker = [0] * num_worker
        num_in_delay = [0] * num_worker
        start_time = [0] * num_worker
        max_delay = [0] * num_worker

# Generated at 2022-06-14 13:48:10.116568
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # pylint: disable=redefined-outer-name
    import time
    from nose.tools import assert_equal
    mw = MonoWorker()
    assert_equal(len(mw.futures), 0)
    def f():
        time.sleep(0.1)
        return 1
    assert_equal(mw.submit(f).result(), 1)
    assert_equal(len(mw.futures), 1)
    assert_equal(mw.submit(f).result(), 1)
    assert_equal(len(mw.futures), 2)
    t = mw.submit(f)
    time.sleep(0.1)
    assert_equal(t.cancelled(), True)
    assert_equal(len(mw.futures), 2)

# Generated at 2022-06-14 13:48:15.243839
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import time
    mono = MonoWorker()
    # run one task and submit some other tasks:
    mono.submit(random.randint, 0, 100)
    for i in range(100):
        mono.submit(time.sleep, 1)
    mono.submit(time.sleep, 30)  # should replace waiting task
    # wait to see  that two tasks ran concurrently
    time.sleep(2)

# Generated at 2022-06-14 13:48:25.411586
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import itertools

    def _pid():
        import os
        return os.getpid()

    def _sleep(i):
        time.sleep(0.1)
        return i

    mw = MonoWorker()
    # submit some tasks, check that only one is running at a time
    pid = set()
    for i in map(str, itertools.count()):
        worker = mw.submit(_pid)
        for p in pid:
            if p != worker.result():
                raise Exception("2 workers running")
        pid |= {worker.result()}
        tqdm_auto.write("pid " + i)
        time.sleep(0.01)
    # check that interrupting a waiting task replaces it
    mw2 = MonoWorker()
    tqdm_auto.write

# Generated at 2022-06-14 13:48:33.227272
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ..utils import timeit
    from .__init__ import tqdm

    class SleepingWorker(MonoWorker):
        """
        Example:
        >>> pool = SleepingWorker()
        >>> for i in tqdm(range(30), desc='sleeping'):
        ...     pool.submit(sleep, i)
        """
        def __init__(self):
            super(SleepingWorker, self).__init__()

    pool = SleepingWorker()
    for i in tqdm(range(30), desc='sleeping'):
        pool.submit(sleep, i)



# Generated at 2022-06-14 13:48:52.962193
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> import time
    >>> import tqdm
    >>> runner = tqdm.contrib.MonoWorker()
    >>> future1 = runner.submit(time.sleep, 0.5)
    >>> _ = future1.result()
    >>> runner.submit(time.sleep, 0.5)
    >>> _ = future1.result()

    >>> future1 = runner.submit(time.sleep, 0.5)
    >>> future2 = runner.submit(time.sleep, 0.5)
    >>> future2.cancel()
    >>> _ = future1.result()
    """

# Generated at 2022-06-14 13:49:04.295952
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def f(x):
        tqdm_auto.write("f({})".format(x))
        return x * 2

    # ------ test of most recent task is always the waiting task ------
    mwork = MonoWorker()
    r1 = mwork.submit(f, 1)
    r2 = mwork.submit(f, 2)
    r3 = mwork.submit(f, 3)
    r1.result()
    tqdm_auto.write("")
    r2.result()
    tqdm_auto.write("")
    r3.result()
    tqdm_auto.write("")

    # ------ test of cancelled if waiting task was submitted ------
    tqdm_auto.write("")
    mwork = MonoWorker()
    r1 = mwork.submit(f, 1)
   

# Generated at 2022-06-14 13:49:15.610370
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    time.sleep(0.2)
    assert len(mw.futures) == 0
    assert mw.submit(time.sleep, 0.1)
    time.sleep(0.2)
    assert len(mw.futures) == 1
    assert mw.submit(time.sleep, 0.1)
    time.sleep(0.2)
    assert len(mw.futures) == 2
    assert mw.submit(time.sleep, 0.1)
    time.sleep(0.2)
    assert len(mw.futures) == 2
    assert mw.submit(time.sleep, 0.1)
    time.sleep(0.2)
    assert len(mw.futures) == 2

# Generated at 2022-06-14 13:49:23.968610
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def sleep(s):
        time.sleep(s)
    def test_helper(s, t):
        worker = MonoWorker()
        # submit task-1, immediately available
        t1 = worker.submit(sleep, s)
        # submit task-2, replaces task-1
        t2 = worker.submit(sleep, s)
        # sleep for delay, check task-1 executed
        time.sleep(t)
        assert not t1.done()
        # check task-2 not yet executed
        assert not t2.done()
        # wait for task-2
        t2.result()
        assert t2.done()
    test_helper(s=1, t=0.1)
    test_helper(s=0.1, t=1)

# Generated at 2022-06-14 13:49:34.061644
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def echo(s):
        sleep(0.01)
        return s

    mw = MonoWorker()
    mw.submit(sleep, 0.02)

    assert mw.submit(sleep, 0.1) is None
    # replace waiting task
    assert mw.submit(sleep, 0.1) is None

    assert mw.submit(sleep, 0.03) is None
    # kill waiting task and insert running
    assert mw.submit(sleep, 0.04) is None

    assert mw.submit(echo, "a") is None
    # sleep(0.04) + echo("a")
    assert mw.submit(echo, "b") is None
    # sleep(0.04) + echo("b")
    assert mw.submit(echo, "c") is None


# Generated at 2022-06-14 13:49:44.645699
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from ..utils import _range
    from time import sleep

    mw = MonoWorker()

    def sl(secs):
        sleep(secs)
        return secs

    with tqdm_auto.tqdm(total=4) as t:
        for s in _range(4):
            sleep_future = mw.submit(sl, secs=s)
            assert sleep_future.result() == s
            t.update()

        # Waiting task is cancelled (3 -> 0)
        sleep_future = mw.submit(sl, secs=3)
        sleep_future = mw.submit(sl, secs=0)
        assert sleep_future.cancel()
        assert sleep_future.cancelled()
        assert sleep_future.done()
        assert not sleep_future.result()

        # Another

# Generated at 2022-06-14 13:49:53.473895
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from multiprocessing import Process

    def _print_time(wdgt):
        while 1:
            print(wdgt(), end='')
            time.sleep(0.01)

    def _worker(wdgt):
        import random
        import threading
        for i in range(1000):
            t = threading.Thread(target=time.sleep, args=(random.random(),))
            t.daemon = True
            t.start()
            t.join()
            wdgt()

    def dummyworker():
        time.sleep(0.1)

    mono = MonoWorker()
    text = "[{0:>10}]".format("dummyworker")

    proc = Process(target=_print_time, args=(lambda: text,))
    proc.start()


# Generated at 2022-06-14 13:49:58.391452
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from nose.tools import assert_true

    def long_task(*args, **kw):
        time.sleep(1)
        return True

    work = MonoWorker()
    t = time.time()
    work.submit(long_task)
    assert_true(time.time() - t < 1)
    work.submit(long_task)
    assert_true(time.time() - t >= 1)

# Generated at 2022-06-14 13:50:04.757547
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from sys import stdout
    from traceback import format_exc
    from threading import Thread

    r = None

    def f(x):
        global r
        sleep(x)
        return x

    def g(x):
        global r
        sleep(x)
        raise Exception(x)

    def assertEqual(x, y):
        if x != y:
            raise AssertionError("%r != %r" % (x, y))

    def output(x):
        tqdm_auto.write(x)
        stdout.flush()

    Mono = MonoWorker

    # Multiple basic submit
    mono = Mono()
    mono.submit(f, 1)
    mono.submit(f, 2)
    mono.submit(f, 3)

# Generated at 2022-06-14 13:50:15.130900
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def worker(x, sleep=0.001):
        time.sleep(sleep)
        return x

    def worker_exception(sleep=0.001):
        time.sleep(sleep)
        assert False, "Exception in worker"

    mono_worker = MonoWorker()
    for i in tqdm_auto.trange(10):
        mono_worker.submit(worker, i, sleep=0.01)
        time.sleep(0.001)  # force work to overlap
    for i in tqdm_auto.trange(10):
        mono_worker.submit(worker_exception, sleep=0.01)
        time.sleep(0.001)  # force work to overlap



# Generated at 2022-06-14 13:50:49.727802
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    time.sleep(0.2)
    assert not mw.submit(time.sleep, 0.1)
    time.sleep(0.2)
    assert not mw.submit(time.sleep, 0.1)
    time.sleep(0.2)
    assert not mw.submit(time.sleep, 0.1)

# Generated at 2022-06-14 13:50:58.141979
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()

    def wait(t):
        time.sleep(t)
        return t

    assert mw.pool._work_queue.qsize() == 0

    f = mw.submit(wait, 1)
    assert f in mw.futures
    assert f.done() is False

    f = mw.submit(wait, 1)  # new waiting task
    assert len(mw.futures) == 1
    assert f in mw.futures
    assert f.done() is False

    f = mw.submit(wait, 1)  # cancels waiting task
    assert len(mw.futures) == 1
    assert f in mw.futures
    assert f.done() is False

    f.result()  # finish task

# Generated at 2022-06-14 13:51:05.416477
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    worker = MonoWorker()
    # Submit a func that blocks itself
    waiting = worker.submit(lambda: worker.submit(lambda: 1/0))
    try:
        # Submit a func that blocks itself
        # should cancel waiting task
        waiting2 = worker.submit(lambda: worker.submit(lambda: 1/0))
    except Exception as e:
        # Should raise the exception of the cancelled waiting task
        assert "division by zero" in str(e)
    else:
        # This line should not be reached
        assert False

# Generated at 2022-06-14 13:51:14.307740
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, threading
    VALS = [10, 11, 12]

    class Foo(object):

        def __init__(self, val):
            self.val = val  # passed as a kwarg

        def __call__(self, bar=5):
            """bar will be passed as an arg"""
            return self.val + bar

    def test_thread(tc):
        time.sleep(0.25)
        tc.assertTrue(len(tc.mw.futures), 1)
        time.sleep(2)
        tc.assertTrue(len(tc.mw.futures), 0)
        tc.mw.futures[0].result()  # make sure exception is not raised

    def test_main(tc):
        tc.mw = MonoWorker()

# Generated at 2022-06-14 13:51:20.584803
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # import time
    import sys
    from io import StringIO

    def f(i, use_tqdm=False, tqdm_kwargs=None):
        if use_tqdm:
            with tqdm_auto.tqdm_notebook(**(tqdm_kwargs or {})) as t:
                tqdm_auto.write('{}'.format(i), file=sys.stdout)
                # time.sleep(.01)
        else:
            tqdm_auto.write('{}'.format(i), file=sys.stdout)
            # time.sleep(.01)

    worker = MonoWorker()

    # no-tqdm
    stdout = StringIO()
    sys.stdout = stdout

# Generated at 2022-06-14 13:51:32.109377
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import time
    from .ut import get_time1

    def func(x):
        time.sleep(x)
        return x
    ###############
    t1 = get_time1()
    M = MonoWorker()
    M.submit(func, 2.0)
    M.submit(func, 2.0)
    M.submit(func, 2.0)
    M.submit(func, 2.0)
    M.submit(func, 2.0)
    M.submit(func, 2.0)
    assert t1 + 10.0 < get_time1() < t1 + 20.0
    t1 = get_time1()
    M.submit(func, 2.0)
    M.submit(func, 2.0)
    M.submit(func, 2.0)


# Generated at 2022-06-14 13:51:41.344614
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def _test(func, args, kwargs):
        import time
        import sys
        import traceback
        while True:
            try:
                res = func(*args, **kwargs)
                break
            except Exception as e:
                print(str(e))
                traceback.print_exc()
                print()
                try:
                    print("AttrError:")
                    print(e.args)
                    print(e.args[0])
                except:
                    pass
                print()
                time.sleep(.1)
                continue
        print("{0}(\n  *{1}, \n  **{2}\n) returned {3}".format(
            func.__name__, args, kwargs, res))
        sys.stdout.flush()

    from multiprocessing import Process

# Generated at 2022-06-14 13:51:49.295408
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    w = MonoWorker()

    def test_func(a, b=2):
        sleep(0.2)
        return a ** b

    # submit the first task
    res = w.submit(test_func, 2, b=3)
    assert res.result() == 8

    # submit another task, which will be waiting
    res2 = w.submit(test_func, 3, b=4)
    assert len(w.futures) == 2

    # submit another task, which will replace the waiting task
    # and the replaced task should be removed
    res3 = w.submit(test_func, 4, b=5)
    assert res3
    assert len(w.futures) == 2

    # check if the waiting task is replaced
    assert res2.done() is True
   

# Generated at 2022-06-14 13:51:55.434229
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import threading
    import time
    from .utils import NullWriter
    from .utils import ThreadWithReturnValue
    from .utils import suppress_stderr
    from .utils import suppress_stdout

    # Callables for testing
    def wait(duration=0.5, add=1):
        time.sleep(duration)
        return duration + add

    def _test_submit_1():
        with suppress_stdout() as stdout, suppress_stderr() as stderr:
            with NullWriter(stdout, stderr):
                # Long running task
                w = MonoWorker()
                t1 = w.submit(wait, 1)
                assert t1.result() == 2
                # Too quick task (should be discarded)
                w.submit(wait, 0, 2)
                # Longer running task (should replace

# Generated at 2022-06-14 13:52:03.702579
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def foo(i):
        sleep(0.2**i)
        return i

    fut0 = fut1 = None
    unt = MonoWorker()
    for i in tqdm_auto.trange(4):
        if i % 2 == 0 and not fut0:
            fut0 = unt.submit(foo, i)
        if i % 2 == 1 and not fut1:
            fut1 = unt.submit(foo, i)
        sleep(0.05)
        print(i, "done")
    print([fut.result() for fut in (fut0, fut1)])