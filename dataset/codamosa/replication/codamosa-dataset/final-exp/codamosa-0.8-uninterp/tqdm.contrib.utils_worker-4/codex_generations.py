

# Generated at 2022-06-14 13:42:50.389222
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import nose.tools

    class Failing(Exception):
        pass

    def fire_and_forget(x):
        tqdm_auto.write('submitted: {}'.format(x))
    def fire_and_wait(x, y=1):
        tqdm_auto.write('submitted: {} {}'.format(x, y))
        return x + y
    def fire_and_crash(x):
        tqdm_auto.write('submitted: {}'.format(x))
        raise Failing

    # test run & wait
    wkr = MonoWorker()
    wkr.submit(fire_and_forget, 1)
    wkr.submit(fire_and_wait, 2)
    wkr.submit(fire_and_crash, 3)
    wkr.submit

# Generated at 2022-06-14 13:43:00.501013
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def do_work(work, slp):
        time.sleep(slp)
        return work

    def do_work_err(work, slp):
        time.sleep(slp)
        raise RuntimeError('foo')

    def test_MonoWorker_submit(do_work):
        from threading import Thread, Event
        from concurrent.futures import wait

        def _test_MonoWorker_submit(do_work, slps, exp, desc=''):
            mw = MonoWorker()
            for slp in slps:
                mw.submit(do_work, slp, slp)
                mw.submit(do_work, slp, slp)
            try:
                wait(mw.futures)
            except RuntimeError:
                pass
            res

# Generated at 2022-06-14 13:43:11.798596
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from itertools import islice

    def log_func(value):
        sleep(1)
        return value

    worker = MonoWorker()

    def submit_tasks(i, n):
        i = iter(range(n))
        j = 0
        while j < n:
            if worker.submit(log_func, next(i)):
                j += 1

    submit_tasks(0, 1)
    assert len(worker.futures) == 1
    assert worker.futures[0].running()
    assert not worker.futures[0].done()

    submit_tasks(1, 3)
    assert len(worker.futures) == 1
    assert worker.futures[0].running()
    assert not worker.futures[0].done()

# Generated at 2022-06-14 13:43:20.101006
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    with MonoWorker() as worker:
        def worker_func(n):
            time.sleep(random.random() * n * 0.1)

        def test_func(n):
            worker.submit(worker_func, n)

        # only last worker_func should be named "1"
        # only last worker_func should be named "2"
        # only last worker_func should be named "3"
        for _ in range(3):
            for n in range(3):
                test_func(n)
            time.sleep(0.2)

# Generated at 2022-06-14 13:43:27.596902
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import warnings

    # Disable deprecation warnings
    warnings.simplefilter('ignore')
    # Create the worker handler
    mw = MonoWorker()

    # Create a job that takes 5 seconds to run
    def job1():
        time.sleep(5)
        return 1

    # Create a job that takes 1 second to run
    def job2():
        time.sleep(1)
        return 2

    # Create a job that takes 10 seconds to run
    def job3():
        time.sleep(10)
        return 3

    # Submit the job1 and job2
    job1_future = mw.submit(job1)
    job2_future = mw.submit(job2)
    # Check if job1 is running and job2 is waiting
    assert len(mw.futures) == 2


# Generated at 2022-06-14 13:43:38.759206
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    monoworker = MonoWorker()
    # Test that it can run a task
    assert monoworker.submit(time.sleep, .25).result() is None
    # Test that it runs the newest task
    for i in range(4):
        sleep_event = threading.Event()
        wait_event = threading.Event()
        tasks = []
        for j in range(4):
            task = monoworker.submit(wait_event.wait)
            wait_event.set()
            tasks.append(task)
        assert all(task.result() is None for task in tasks)
        assert len(monoworker.futures) == 1
    # Test that it doesn't run a cancelled task
    # But only after it has started running

# Generated at 2022-06-14 13:43:49.738022
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test function"""
    from time import sleep
    f1 = f2 = f3 = f4 = f5 = f6 = None

    def test_f1():
        """Test function"""
        sleep(3)

    def test_f2():
        """Test function"""
        sleep(3)

    def test_f3():
        """Test function"""
        sleep(3)

    def test_f4():
        """Test function"""
        sleep(3)

    def test_f5():
        """Test function"""
        sleep(3)

    def test_f6():
        """Test function"""
        sleep(3)

    mw = MonoWorker()

    f1 = mw.submit(test_f1)

    sleep(0.7)
    f2 = mw.submit(test_f2)

# Generated at 2022-06-14 13:44:00.115563
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Method submit of class MonoWorker unit test."""
    from .threading import tqdm
    import time

    def func(name):
        """Sleep function"""
        time.sleep(0.2)
        return name

    def thread_sleep(name, sleep=0.1, verbose=False):
        """Add a sleep command to threads"""
        if verbose:
            tqdm_auto.write("[%s] start" % (name))
        time.sleep(sleep)
        if verbose:
            tqdm_auto.write("[%s] done" % (name))
        return func(name)

    def thread(name, mw, sleep=0.1, verbose=False):
        """Thread function"""
        thread_sleep(name + " before", sleep=sleep, verbose=verbose)

# Generated at 2022-06-14 13:44:02.939865
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    print('testing MonoWorker.submit')
    mw = MonoWorker()
    mw.submit(time.sleep, 1)
    mw.submit(time.sleep, 1)
    print('test passed')

# Generated at 2022-06-14 13:44:10.257404
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .utils import ipy_sleep

    def f(x, y=0, sleep=sleep):
        sleep(y)
        return x, y

    # Test single argument
    mw = MonoWorker()
    x = mw.submit(f, 1)
    assert x.result() == (1, 0)
    assert mw.futures[0].result() == (1, 0)

    # Test kwarg
    mw = MonoWorker()
    x = mw.submit(f, 1, y=2)
    assert x.result() == (1, 2)
    assert mw.futures[0].result() == (1, 2)

    # Test that old task is killed
    mw = MonoWorker()

# Generated at 2022-06-14 13:44:24.054420
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    import time

    def slow_factory(x):
        def slow_square(y):
            time.sleep(y/100)
            return x ** 2
        return slow_square
    t = MonoWorker()
    t.submit(slow_factory(2), 0.01)
    t.submit(slow_factory(3), 0.02)
    t.submit(slow_factory(4), 0.03)
    t.submit(slow_factory(5), 0.04)
    t.submit(slow_factory(6), 0.05)
    t.submit(slow_factory(7), 0.06)
    t.submit(slow_factory(8), 0.07)
    t.submit(slow_factory(9), 0.08)

# Generated at 2022-06-14 13:44:25.853647
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from . import _test_MonoWorker_submit
    _test_MonoWorker_submit(MonoWorker)

# Generated at 2022-06-14 13:44:32.727207
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    class Tracer:
        def __init__(self, i, t):
            self.i = i
            self.t = t
        def __call__(self):
            time.sleep(self.t)
            return self.i
    # tracer 2 takes a long time, tracer 1 is expected to be dropped
    mw.submit(Tracer(1, 1).__call__)
    time.sleep(0.2)
    mw.submit(Tracer(2, 1).__call__)
    time.sleep(0.2)
    mw.submit(Tracer(3, 0.1).__call__)
    time.sleep(0.5)
    assert mw.futures[0].result() is 3

# Generated at 2022-06-14 13:44:43.348537
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test: MonoWorker.submit"""
    from time import sleep
    import sys

    class Printer(object):
        """Print on call."""
        def __init__(self, name):
            self.name = name

        def __call__(self, *args):
            print("{}({})".format(self.name, args))

    mono = MonoWorker()
    print("=" * 80)
    mono.submit(Printer("refused"), "refused")
    mono.submit(Printer("started"), "started")
    print("=" * 80)
    sleep(1)
    print("=" * 80)
    mono.submit(Printer("started"), "started")
    mono.submit(Printer("refused"), "refused")
    mono.submit(Printer("started"), "started")

# Generated at 2022-06-14 13:44:52.963987
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Lock, current_thread
    from . import trange
    from .async_ import AsyncProgressBar

    class TestObj(object):
        """A dummy class to test MonoWorker.submit"""
        def __init__(self, manager, input_iterator):
            self.manager = manager
            self.input_iterator = input_iterator
            self.lock = Lock()
            self.result = []
            self.pb = AsyncProgressBar(trange(10), desc='TestObj',
                                       leave=False,
                                       disable=True).__enter__()
            self.in_progress = False

        def run_progress(self):
            self.in_progress = True
            for i in self.pb:
                sleep(0.01)
            self.in_progress = False
           

# Generated at 2022-06-14 13:45:04.638763
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    mw = MonoWorker()
    d = {'func': 0}
    assert d['func'] == 0
    _ = mw.submit(lambda x: d.__setitem__('func', x), 42)
    time.sleep(0.1)
    assert d['func'] != 0
    assert d['func'] != 42
    d['func'] = 0  # should be overwritten by next call
    _ = mw.submit(lambda x: d.__setitem__('func', x), 100)
    time.sleep(0.1)
    assert d['func'] != 0
    assert d['func'] != 42
    assert d['func'] != 100
    d['func'] = 0  # should be overwritten by next call
    threads = []

# Generated at 2022-06-14 13:45:15.056465
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Test in case of error
    x = MonoWorker()
    with tqdm_auto.wrapattr(sys.stdout, "buffer", "") as stdout:
        assert (x.submit(None) is None)
        assert (stdout.getvalue() == "\n")

    import time
    import traceback
    def f_0():
        time.sleep(0.01)
        return "1"
    def f_1():
        time.sleep(0.01)
        traceback.print_stack()
        raise Exception("2")
    def f_2():
        time.sleep(0.01)
        raise Exception("3")
    def f_3():
        time.sleep(0.01)
        return "4"
    def f_4():
        time.sleep(0.01)
       

# Generated at 2022-06-14 13:45:20.671529
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import sys

    def func(x):
        sleep(0.5)
        return x

    mw = MonoWorker()
    if sys.version_info.major >= 3:
        futures = [mw.submit(func, i) for i in range(4)]
    else:
        futures = [mw.submit(func, long(i)) for i in range(4)]

    for future in futures:  # Should be sorted by time
        assert future.result() == 0

# Generated at 2022-06-14 13:45:30.882223
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test the MonoWorker.submit method
    """
    import time
    import threading

    def print_and_sleep(s, sec):
        time.sleep(sec)
        tqdm_auto.write(s)

    mw = MonoWorker()
    start_time = time.time()
    num_threads = 0
    while time.time() - start_time <= 5:
        num_threads += 1
        waiting = mw.submit(
            print_and_sleep, 'worker ' + str(num_threads), num_threads)
        if num_threads % 2 == 1:
            waiting.cancel()
    time.sleep(0.1)
    for t in threading.enumerate():
        if t.name.startswith('worker'):
            tqdm

# Generated at 2022-06-14 13:45:41.030070
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from sys import stdout
    from time import sleep
    from os import linesep

    worker = MonoWorker()
    # submit 2 jobs
    print('submitting 2 jobs:')
    worker.submit(sleep, 0.5)
    worker.submit(sleep, 0.5)
    # submit 2 jobs and keep the latest
    print('submitting 2 jobs and keeping the latest:')
    worker.submit(sleep, 0, 0.5)
    worker.submit(sleep, 1, 0.5)
    stdout.flush()
    sleep(1.0)
    print(linesep,
          'submitting 1 job after the previous 2 jobs have ran successfully:')
    worker.submit(sleep, 0.5)
    sleep(1.0)

# Generated at 2022-06-14 13:45:56.472838
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Method submit of class MonoWorker

    Method submit of class MonoWorker
    """
    from time import sleep
    from threading import RLock
    from collections import deque

    class FauxPoolExecutor(object):
        """
        Supports one running task and one waiting task.
        The waiting task is the most recent submitted (others are discarded).
        """
        def __init__(self, _max_workers=1, _lock=RLock()):
            self._max_workers = _max_workers
            self._lock = _lock
            self._futures = deque([], 2)

        def submit(self, func, *args, **kwargs):
            """`func(*args, **kwargs)` may replace currently waiting task."""
            if self._max_workers:
                self._lock.acquire()

# Generated at 2022-06-14 13:46:07.302119
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    mw = MonoWorker()
    import time

    def print_wait(id, wait):
        time.sleep(wait)
        print(id)

    print('MonoWorker: only one task at a time')
    mw.submit(print_wait, 1, 1)
    mw.submit(print_wait, 2, 2)
    mw.submit(print_wait, 3, 3)
    ret = mw.submit(print_wait, 3, 3)
    if ret:
        ret.result()

    print('MonoWorker: only one waiting task at a time')
    mw.submit(print_wait, 1, 1)
    ret1 = mw.submit(print_wait, 2, 2)
    mw.submit(print_wait, 3, 3)

# Generated at 2022-06-14 13:46:17.201623
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random

    def func(prefix=''):
        sleep(random())
        return prefix

    m = MonoWorker()
    for i in range(3):
        m.submit(func, str(i))
    assert m.futures[0].result() == '2'
    assert m.futures[0].result() == '2'  # check caching
    sleep(0.1)  # ensure previous task finished, then submit new task
    assert m.futures[0].result() == '2'  # check if new task cancelled
    assert m.futures[1].result() == '2'  # check if new task cancelled
    m.submit(func, 'new')
    assert m.futures[0].result() == 'new'
    assert m.fut

# Generated at 2022-06-14 13:46:25.941845
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from concurrent.futures import TimeoutError
    import time
    m = MonoWorker()
    def wait(t, rep=0):
        if t > 0:
            time.sleep(t)
            return rep
        raise ValueError("Invalid args")
    tqdm_auto.write("submit(0)")
    f0 = m.submit(wait, 0.2, rep=0)
    tqdm_auto.write("submit(1)")
    f1 = m.submit(wait, 0.2, rep=1)
    tqdm_auto.write("submit(2)")
    f2 = m.submit(wait, 0.4, rep=2)
    tqdm_auto.write("submit(3)")
    f3 = m.submit(wait, 0.4, rep=3)


# Generated at 2022-06-14 13:46:33.362559
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def updown(i):
        tqdm_auto.write("%s: starting" % i)
        for _ in tqdm_auto.range(i, 0, -1):
            pass
        tqdm_auto.write("%s: done" % i)

    mono = MonoWorker()
    from concurrent.futures import ThreadPoolExecutor
    pool = ThreadPoolExecutor(max_workers=4)
    for i in range(4):
        pool.submit(mono.submit, updown, i)

# Generated at 2022-06-14 13:46:44.423490
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from traceback import format_exception
    import sys

    def sleep_n_func(*args, **kwargs):
        sleep(*args, **kwargs)
        return "sleep_n_func"

    try:
        from pytest import approx
    except:
        from numpy.testing import assert_allclose as approx

    import queue
    import unittest as ut

    class TestMonoWorker(ut.TestCase):
        def test_submit(self):
            """
            Run this test with
            python -m tqdm.contrib.test_MonoWorker_submit
            """
            mono = MonoWorker()

            # test: normal
            self.assertEqual(mono.submit(sleep_n_func, 0.5), None)
            sleep(0.4)
           

# Generated at 2022-06-14 13:46:51.762103
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def _submit(q, r, p, s):
        time.sleep(s)
        q.put((r, p))
    m = MonoWorker()
    import queue
    q = queue.Queue()
    n = 5
    for i in range(n):
        m.submit(_submit, q, i, n-i, n-i)
    for i in range(n):
        r, p = q.get()
        #print(r, p)
        assert i == r
        assert n-i == p

# Generated at 2022-06-14 13:47:02.476678
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import time
    import sys

    def dummy(a, b=0):
        time.sleep(a + random.random() + b)
        return a + b, a * b

    # Test that function is replaced when submit is called twice
    mw = MonoWorker()
    mw.submit(dummy, 2, b=3)
    start_time = time.time()
    mw.submit(dummy, 3, b=5)
    assert time.time() - start_time < 2.5

    # Test that calling cancel on waiting future actually cancels it
    mw = MonoWorker()
    mw.submit(dummy, 1, b=2)
    mw.submit(dummy, 1, b=3)
    start_time = time.time()

# Generated at 2022-06-14 13:47:10.782666
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test that MonoWorker.submit works"""
    import time
    import threading
    import random
    import unittest
    import concurrent.futures
    import multiprocessing
    multiprocessing.set_start_method("forkserver")
    class TestMonoWorker(unittest.TestCase):
        @staticmethod
        def worker(x):
            time.sleep(x)
            return x
        def test_mono_worker(self):
            worker = MonoWorker()
            results = []
            for _ in range(10):
                time.sleep(random.random() / 4)
                worker.submit(self.worker, random.random() / 2)
                worker.submit(self.worker, random.random() / 2)
                result = worker.futures[-1]
                results

# Generated at 2022-06-14 13:47:21.873526
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Unit test for method submit of class MonoWorker"""
    import time
    from ..utils import _range  # NOQA

    # A function to test...
    def cb(i):
        """Callback function to test"""
        time.sleep(0.1)
        print(i)

    # ... with some dummy arguments
    dummy_args = [{'i': _} for _ in _range(10)]
    # And our MonoWorker
    mono_worker = MonoWorker()

    # ... which we can submit in a loop
    for i, dummy_arg in enumerate(dummy_args):
        mono_worker.submit(cb, **dummy_arg)

    # We have to wait for everything to complete
    mono_worker.pool.shutdown(wait=True)

# Generated at 2022-06-14 13:47:36.000391
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    futures = [mw.submit(time.sleep, i) for i in range(3)][::-1]
    while futures:
        time.sleep(0.001)
        done, futures = futures[-1].done(), futures[:-1]

# Generated at 2022-06-14 13:47:47.183961
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import threading

    def run():
        # this function sleeps for a random amount of time from 0.5 to 1.5 seconds.
        time.sleep(0.5 + random.random())
        return 42

    def thread_fun():
        worker = MonoWorker()
        a = worker.submit(run)
        b = worker.submit(run)
        threading.current_thread().a = a
        threading.current_thread().b = b

    def run_thread():
        thread = threading.Thread(target=thread_fun)
        thread.start()
        thread.join()
        return thread

    threads = [run_thread() for _ in range(20)]
    assert all(thread.b.cancelled() for thread in threads)

# Generated at 2022-06-14 13:47:56.008809
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def waiter(t):
        time.sleep(t)
        return t

    def test_submit(waiter):
        mw = MonoWorker()
        assert mw.futures == deque([], 2)
        assert mw.submit(waiter, 1) is not None
        assert mw.futures == deque([], 2)
        assert mw.submit(waiter, 2) is not None
        assert mw.futures == deque([], 2)
        assert mw.submit(waiter, 3) is not None
        assert mw.futures == deque([], 2)
        t = time.time()
        assert mw.submit(waiter, 4) is not None
        assert mw.futures == deque([], 2)
        assert time.time

# Generated at 2022-06-14 13:48:05.414969
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # 1
    import time
    import random
    import sys
    from unittest import TestCase
    from concurrent.futures import Future
    test_case = TestCase()
    (time_for_func, rand_sleep_for_func, rand_sleep_for_run)[:] = [
        lambda: random.randint(0, 5),
        lambda: random.randint(0, 3),
        lambda: random.randint(0, 9) / 10.0,
    ]
    func, args, kwargs = test_case.assertTrue, (True,), {}

    def is_future(f):
        return isinstance(f, Future)

    def is_true_future(f):
        return is_future(f) and f.done() and f.result()


# Generated at 2022-06-14 13:48:12.488907
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    worker = MonoWorker()
    import time
    def slow_add(x):
        time.sleep(1)
        return x + 1
    def slow_mul(x):
        time.sleep(2)
        return x * 2
    f1 = worker.submit(slow_add, 20)
    f2 = worker.submit(slow_mul, 20)
    f3 = worker.submit(slow_add, 40)
    f4 = worker.submit(slow_mul, 40)
    assert f2.result() == 40
    assert f4.result() == 80

# Generated at 2022-06-14 13:48:21.356028
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def task(n):  # takes n seconds
        time.sleep(n)
        return n

    worker = MonoWorker()

    # The following sequence of submissions:
    #   1) task(4)
    #   2) task(3)
    #   3) task(2)
    # will become:
    #   1) task(4)
    #   2) task(2) (i.e. waiting)
    #   3) task(2)

    n = 4
    future4 = worker.submit(task, n)
    assert future4.result() == n

    n = 3
    future3 = worker.submit(task, n)
    assert future3.result() == 2

    n = 2
    future2 = worker.submit(task, n)
    assert future2.result()

# Generated at 2022-06-14 13:48:29.730778
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, random

    def slow(x, delay=random.random()):
        time.sleep(delay)
        return x

    def quick(x, delay=0.001):
        time.sleep(delay)
        return x

    worker = MonoWorker()
    assert worker.futures.maxlen == 2
    assert len(worker.futures) == 0

    assert worker.submit(slow, 2) == worker.submit(slow, 3)
    assert len(worker.futures) == 1
    assert worker.futures[0].result() == 2
    assert len(worker.futures) == 0

    assert worker.submit(slow, 4) == worker.submit(slow, 5)
    assert len(worker.futures) == 1  # because other is done

# Generated at 2022-06-14 13:48:38.858626
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading as th
    import concurrent.futures as cf

    class TestWorker(MonoWorker):
        def __init__(self):
            super(TestWorker, self).__init__()
            self.test_lock = th.Lock()
            self.test_cnt = 0

        def test_submit_decorator(f):
            def test_submit_wrapper(self, *args, **kwargs):
                with self.test_lock:
                    self.test_cnt += 1
                return f(self, *args, **kwargs)

            return test_submit_wrapper

        @test_submit_decorator
        def submit(self, func):
            return super(TestWorker, self).submit(func)


# Generated at 2022-06-14 13:48:48.847931
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def _print_exc(exception_type, exception, traceback):
        """Handle exceptions during parallel running of _wait_n_print."""
        tqdm_auto.write(str(exception_type) + str(exception))

    import sys
    import threading
    from concurrent.futures import Future

    def _wait_n_print(i, t=4):
        """Helper function for testing MonoWorker.submit."""
        tqdm_auto.write('Start wait {}'.format(i))
        time.sleep(t)
        tqdm_auto.write('End wait {}'.format(i))
        # raise Exception('intentional raise {}'.format(i))


# Generated at 2022-06-14 13:48:57.655004
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from multiprocessing import Value
    import time
    from concurrent.futures import Future
    from .utils import get_tqdm_implementation_by_args
    tqdm = get_tqdm_implementation_by_args('test_MonoWorker_submit')

    def make_test_future(val, sleep_for):
        def test_func():
            time.sleep(sleep_for)
            val.value += 1
        return Future()

    # create a global var
    val = Value('i', 0)
    # create the MonoWorker
    mono_worker = MonoWorker()

    # Submit several jobs with varying completion times
    test_fut_1 = mono_worker.submit(make_test_future, val, 0.5)

# Generated at 2022-06-14 13:49:22.491573
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import time
    from threading import Event

    stopper = Event()

    def wait_randomly():
        for _ in range(100):
            if stopper.wait(0.01):
                break
            time.sleep(random.random()*0.001)
        return True

    mp = MonoWorker()
    futures = []
    for i in tqdm_auto.trange(10):
        futures.append(mp.submit(wait_randomly))
    stopper.set()
    # Check that all futures are done and returned True
    assert all(f.result() for f in futures)

# Generated at 2022-06-14 13:49:32.975605
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def sleep(n_seconds, msg=""):
        print("{}sleeping for {}s".format(msg, n_seconds))
        time.sleep(n_seconds)
        return n_seconds

    mono_worker = MonoWorker()

# Generated at 2022-06-14 13:49:40.890004
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def slow_work(s, e):
        time.sleep(s)
        return e

    worker = MonoWorker()
    def callback(result):
        print("callback", result)

    def test_submit(s, e, i):
        print("submit", i, s, e)
        future = worker.submit(slow_work, s, e)
        future.add_done_callback(callback)

    for i in range(10):
        test_submit(2, i, i)


# Generated at 2022-06-14 13:49:50.481114
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    $ nosetests --pdb test_MonoWorker_submit
    """
    from time import sleep
    from random import randrange
    from threading import current_thread

    def _test_thread(mw, i):
        print(current_thread(), 'test', i)
        four = 4
        while four > 0:
            four -= 1
            sleep(0.25)
        print(current_thread(), 'test', i, 'done')
        return i

    mw = MonoWorker()
    result = [mw.submit(_test_thread, mw, i) for i in range(5)]
    assert not mw.futures
    assert result == [mw.submit(_test_thread, mw, i) for i in range(5)]

    from contextlib import closing

# Generated at 2022-06-14 13:49:57.709805
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import time
    from .utils import pbar

    def t_print(i, sleep=0.3):
        from time import sleep
        sleep(sleep)
        tqdm_auto.write(i)

    mw = MonoWorker()
    d = time()
    mw.submit(t_print, 0)
    mw.submit(t_print, 1)
    for i in pbar(range(10)):
        mw.submit(t_print, i)
    assert (int(time() - d) == 7)

# Generated at 2022-06-14 13:50:03.741534
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def test_func(i, t):
        time.sleep(t)
        return i

    pool = MonoWorker()
    res = []
    for i in range(10):
        t = i % 3
        res.append(pool.submit(test_func, i, t))

    for i, r in enumerate(res):
        assert r.result() == 5


if __name__ == "__main__":
    from pytest import main
    main(["-v", __file__])

# Generated at 2022-06-14 13:50:15.307014
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    def identity(x):
        time.sleep(x)
        return x

    def test(*args, **kwargs):
        return MonoWorker().submit(identity, *args, **kwargs).result() == args[0]

    assert test(0.2)
    assert test(0.1)
    assert test(0.3)
    assert test(0.1, delay=0.5)
    assert test(0.2)
    assert test(0.1)
    assert test(0.3)

    worker = MonoWorker()
    assert worker.submit(time.sleep, 0.5).result() is None
    assert worker.submit(time.sleep, 1).result() is None
    assert worker.submit(time.sleep, 1).result() is None

    worker = Mono

# Generated at 2022-06-14 13:50:25.307719
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Lock
    
    def f(x):
        time.sleep(x)
        return x

    mw = MonoWorker()
    def test_submit(mw, f, x, y, z): 
        mw.submit(f, x)
        mw.submit(f, y)
        mw.submit(f, z)
        return mw.futures
    
    assert test_submit(mw, f, 'x', 'y', 'z') == deque([
        ('x'), ('z')], maxlen=2)

    assert test_submit(mw, f, 'x', 'y', 'z') != test_submit(mw, f, 'x', 'y', 'x')


# Generated at 2022-06-14 13:50:31.371897
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import cpu_count
    from os import cpu_count as os_cpu_count
    from threading import Thread

    def dummy_func(seconds=1):
        "Dummy function to test MonoWorker"
        from time import sleep
        sleep(seconds)

    dummy_count = 2  # number of dummy functions to be executed in parallel
    dummy_args = [2, 1, 3]  # list of dummy seconds sleep
    for num_workers in list(range(1, cpu_count() + 1)) + [min(os_cpu_count(), 16), None]:
        mw = MonoWorker()
        threads = []
        for dummy_arg in dummy_args:
            threads.append(mw.submit(dummy_func, dummy_arg))
        for thread in threads:
            thread

# Generated at 2022-06-14 13:50:41.491313
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def ackermann(m, n):
        """Return ackermann(m,n)"""
        if m == 0:
            return n + 1
        if n == 0:
            return ackermann(m-1, 1)
        return ackermann(m-1, ackermann(m, n-1))

    # Test case: ackerman(3,3) = 61 as of 2015
    mw = MonoWorker()
    for i in range(4):
        print(i)
        mw.submit(ackermann, 3, 3 + i)
        time.sleep(1)

    # Should print [3,4,5,4]
    for i in range(4):
        print(i, mw.futures[i].result())



# Generated at 2022-06-14 13:51:36.397936
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    def f(*args):
        return args

    mono_worker = MonoWorker()

    # submit one task
    waiting = mono_worker.submit(f, 1, 2, 3)
    assert waiting.result() == (1, 2, 3)

    # submit another task
    waiting = mono_worker.submit(f, 4, 5, 6)
    assert waiting.result() == (4, 5, 6)

    # submit one more task (overwriting currently waiting task)
    mono_worker.submit(f, 7, 8, 9)
    assert waiting.result() == (7, 8, 9)

    # submit one more task (overwriting currently running task)
    waiting = mono_worker.submit(f, 10, 11, 12)
    assert waiting.result() == (10, 11, 12)

    # submit one more task (over

# Generated at 2022-06-14 13:51:43.691535
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    # A task that takes more than 5 seconds to complete
    def task_a(time_in_second=5):
        time.sleep(time_in_second)
        return "Task A"

    # A task that takes less than 1 second to complete
    def task_b(time_in_second=0.1):
        time.sleep(time_in_second)
        return "Task B"

    mono_worker = MonoWorker()
    # Create one thread to submit task_a and another to submit task_b
    t_a = threading.Thread(target=mono_worker.submit, args=(task_a,))
    t_b = threading.Thread(target=mono_worker.submit, args=(task_b,))
    t_a.start()
    t_b

# Generated at 2022-06-14 13:51:50.794488
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import remove_finished_iter_from_display

    def slow_print(wait_secs, msg):
        time.sleep(wait_secs)
        with open('output.txt', 'a') as outfile:
            outfile.write(msg)

    with open('output.txt', 'w') as outfile:
        pass

    worker = MonoWorker()
    t = tqdm_auto.tqdm(
        [2, 3, 4],
        file=None,
        leave=False,
        unit=' secs',
        unit_scale=True,
        postfix=False,
        desc='test_MonoWorker_submit')

# Generated at 2022-06-14 13:51:56.767675
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from collections import Callable
    import time

    import pytest

    from . import _monkey_patch

    # Test 1
    with pytest.raises(ValueError):
        MonoWorker(0)

    # Test 2
    def double(x):
        time.sleep(0.4)
        return x * 2

    mw = MonoWorker()
    t0 = time.time()
    f1 = mw.submit(double, 4)
    f2 = mw.submit(double, 8)
    f3 = mw.submit(double, 16)
    f4 = mw.submit(double, 32)
    assert f1.result() == 8
    assert f2.result() == 16
    assert f3.result() == 32
    assert f4.result() == 64

# Generated at 2022-06-14 13:52:06.578968
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    worker = MonoWorker()

    def _f():
        """Interrupts every 3 seconds, takes 5 seconds to complete."""
        for _ in range(5):
            sleep(1)
            if not _f.stop.wait(0.5):
                return False
        return True

    _f.stop = threading.Event()
    _f.thread = None

    def _g():
        for _ in range(3):
            sleep(1)
            if not _g.stop.wait(0.5):
                return False
        return True

    _g.stop = threading.Event()
    _g.thread = None


# Generated at 2022-06-14 13:52:13.780995
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # pylint: disable=import-outside-toplevel
    import time
    import threading
    from ..utils import _term_move_up

    # Real-time printing
    class _NonBlockingStream(object):
        """a non-blocking stream (for real-time printing)"""
        def __init__(self, stream):
            self.stream = stream
            self.buf = []
            # self.lock = threading.RLock()

        def write(self, data):
            """Thread-safe writing without blocking"""
            # with self.lock:
            self.buf.append(data)
            if '\n' in data:
                self.flush()

        def flush(self):
            """Thread-safe flushing without blocking"""
            # with self.lock:
            stream = self.stream
            buf = self

# Generated at 2022-06-14 13:52:18.430883
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from concurrent.futures import _base

    def slow_add(x, y):
        time.sleep(1)
        return x + y

    # Single task
    mono_worker = MonoWorker()
    assert mono_worker.submit(slow_add, 3, 2) == 5
    time.sleep(20)
    assert mono_worker.submit(slow_add, 3, 2) == 5

    # Multiple tasks
    mono_worker = MonoWorker()
    for i in range(3):
        assert mono_worker.submit(slow_add, 3, i).result() == 3 + i
    time.sleep(20)
    for i in range(3):
        assert mono_worker.submit(slow_add, 3, i).result() == 3 + i

    # Canceled task is replaced
    mono_

# Generated at 2022-06-14 13:52:28.698419
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def work(n):
        sleep(2)
        return n

    worker = MonoWorker()
    # Start task 1
    future1 = worker.submit(work, 1)
    # Start task 2, should wait for task 1
    future2 = worker.submit(work, 2)
    assert future1.running()
    assert not future2.done()
    # Start task 3, should cancel task 2
    future3 = worker.submit(work, 3)
    assert future1.running()
    assert future2.cancelled()
    assert future3.running()
    # Start task 4, should cancel task 3
    future4 = worker.submit(work, 4)
    assert future1.running()
    assert future3.cancelled()
    assert future4.running()

# Generated at 2022-06-14 13:52:35.604931
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Thread
    from tqdm.contrib import MonoWorker

    def do(job_index, tqdm_index, sleep_time):
        sleep(sleep_time)
        return job_index

    def del_print_do(worker, job_index, tqdm_index, sleep_time):
        """delete the old print line, print a new line, do a job"""
        tqdm_auto.write('\033[F\033[K{}'.format(job_index))
        tqdm_auto.write('{}'.format(job_index), file=tqdm_index)
        return do(job_index, tqdm_index, sleep_time)

    print('main thread starting:', flush=True)
    tqdm_index = tqdm_

# Generated at 2022-06-14 13:52:46.510431
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from concurrent.futures import wait
    from operator import add

    def print_wait(x, y=0.1, z=0.1):
        sleep(y)
        tqdm_auto.write(str(x))
        sleep(z)
        return x

    # Wait for all tasks to complete
    mono_worker = MonoWorker()