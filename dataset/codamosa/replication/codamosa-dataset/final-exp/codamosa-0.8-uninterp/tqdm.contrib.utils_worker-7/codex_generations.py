

# Generated at 2022-06-14 13:42:43.792671
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test the submition, cancellation and get of MonoWorker"""
    mw = MonoWorker()
    def add_5(x):
        return x + 5
    from time import sleep
    import unittest
    from operator import add

    class TestMonoWorker(unittest.TestCase):
        def test_submit_get(self):
            # Test that the method submits a task correctly
            self.assertEqual(10, mw.submit(add, 5, 5).result())

        def test_submit_cancel(self):
            # Test that the method submits a task correctly
            self.assertRaises(Exception, mw.submit(sleep, 1).result)


# Generated at 2022-06-14 13:42:52.750590
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from multiprocessing import Value
    from . import count

    def f(x, v):
        v.inc()
        time.sleep(x)
        v.dec()
        return v.value

    mw = MonoWorker()
    v = Value('i', 0)
    f1 = mw.submit(f, 1, v)
    time.sleep(0.9)
    f2 = mw.submit(f, 1, v)  # should replace f1
    time.sleep(0.9)
    f3 = mw.submit(f, 1, v)
    time.sleep(0.5)
    f4 = mw.submit(f, 1, v)  # should replace the last 2
    time.sleep(0.5)

# Generated at 2022-06-14 13:43:01.851986
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import operator
    import functools

    def log(s):
        tqdm_auto.write(s)

    def task(n, t):
        log('Running task %s' % n)
        time.sleep(t)
        return n

    def reduce_task(n, w, t):
        log('Running reduce task %s' % n)
        time.sleep(t)
        return w.result() + n

    def test(mw, tasks):
        for n, t in tasks:
            time.sleep(0.1)
            mw.submit(task, n, t)
        mw.submit(task, 0, 0)
        time.sleep(0.1)

    log('Test 1:')
    mw = MonoWorker()

# Generated at 2022-06-14 13:43:07.910311
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def f(n):
        time.sleep(n)
        return n
    import random
    worker = MonoWorker()
    ps = [worker.submit(f, random.random() / 2) for _ in range(5)]
    for p in ps:
        try:
            p.result()
        except Exception as e:
            print(e)
    print('All tasks completed')

# Generated at 2022-06-14 13:43:16.544589
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from sys import stderr
    from os.path import getsize
    from tempfile import NamedTemporaryFile

    def touch(path):
        sleep(0.5)  # simulate real file I/O
        with open(path, 'a+') as f:
            f.write('\n')

    f = NamedTemporaryFile(delete=False)
    f.close()  # we close manually so it won't disappear after exiting
    touch(f.name)

    mw = MonoWorker()
    with tqdm_auto.tqdm(unit='B', unit_scale=True,
                        total=getsize(f.name), file=stderr) as t:
        for i in range(3):
            size = getsize(f.name)

# Generated at 2022-06-14 13:43:26.988342
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import sys
    import time

    def func(x, y, z):
        time.sleep(random.random())
        return x + y + z
    args = (1, 2, 3)

    tqdm_auto.write('Running MonoWorker test...')
    mw = MonoWorker()
    result = mw.submit(func, *args).result()
    assert result == sum(args)
    assert len(mw.futures) == 1
    for _ in tqdm_auto.trange(100):
        result = mw.submit(func, *args).result()
        assert result == sum(args)
        assert len(mw.futures) == 1
    tqdm_auto.write('MonoWorker test passed')
    sys.exit(0)


# Generated at 2022-06-14 13:43:38.191531
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    worker = MonoWorker()

    # test the MonoWorker queue length of 2
    for _ in range(10):
        worker.submit(random.random)
        assert len(worker.futures) == 2

    # test the MonoWorker running tasks priority
    start_time = time.time()
    worker.submit(lambda: time.sleep(0.3))
    worker.submit(lambda: time.sleep(0.1))
    time.sleep(0.2)
    assert len(worker.futures) == 1
    assert not worker.futures[0].done()
    time.sleep(0.2)
    assert len(worker.futures) == 1
    assert worker.futures[0].done()
    assert time.time() - start_time < 0.

# Generated at 2022-06-14 13:43:46.834220
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from tqdm.auto import tqdm

    def _test_MonoWorker_submit():
        mw = MonoWorker()
        time.sleep(2)
        mw.submit(tqdm_auto.write, "Test")
        time.sleep(3)
        mw.submit(tqdm_auto.write, "Test2")
        time.sleep(3)
        mw.submit(tqdm_auto.write, "Test3")

    _test_MonoWorker_submit()



# Generated at 2022-06-14 13:43:51.899813
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    assert len(mw.futures) == 0
    mw.submit(time.sleep, 0.1)
    assert len(mw.futures) == 1
    mw.submit(time.sleep, 0.1)
    assert len(mw.futures) == 1
    mw.submit(time.sleep, 0.1)
    assert len(mw.futures) == 1

# Generated at 2022-06-14 13:44:01.448360
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from functools import partial
    from sys import version_info
    import time

    # safe_print = partial(print, file=__import__('sys').stderr)
    print = lambda msg: tqdm_auto.write(msg, file=__import__('sys').stderr)
    safe_reversed = reversed if version_info.major >= 3 else lambda x: list(reversed(x))

    mono = MonoWorker()
    t = time.time()
    for task_id in safe_reversed(range(5)):
        mono.submit(time.sleep, 0.1)
        print("Submitted task {} ({}s)".format(task_id, time.time() - t))

# Generated at 2022-06-14 13:44:10.639784
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Unit test for method submit of class MonoWorker.
    """
    import threading

    class MyWorker(MonoWorker):
        """
        Subclassing to enable introspection of self.futures
        """
        def __init__(self):
            super(MyWorker, self).__init__()
            self.cb = []
        def submit(self, func, *args, **kwargs):
            fut = super(MyWorker, self).submit(func, *args, **kwargs)
            self.cb.append(lambda: fut.result())
            return fut

    def get_results(worker):
        """
        Unblock all futures and return their results.
        """
        res = []
        for cb in worker.cb:
            res.append(cb())
        return res

    #

# Generated at 2022-06-14 13:44:14.796840
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from multiprocessing import Pool
    from .data import N_RANGE
    from ..tqdm import tqdm

    def try_submit():
        def func(n):
            return n + 1
        worker = MonoWorker()
        tlist = []
        with Pool(2) as pool:
            for i in tqdm(N_RANGE):
                tlist.append(pool.apply_async(worker.submit,
                                              (func, i)))
        return [t.get() for t in tlist]

    assert try_submit() == [i + 1 for i in N_RANGE]

# Generated at 2022-06-14 13:44:20.481029
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from tests_tqdm import pretest_posttest
    from unittest import SkipTest
    from time import sleep

    with pretest_posttest() as (pt, _):
        with pt():
            raise SkipTest
        mw = MonoWorker()
        args = (0.1, 0.1, 0.1)
        mw.submit(sleep, *args)
        sleep(0.3)  # wait for submit to finish

# Generated at 2022-06-14 13:44:26.830272
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    import time

    def check_future(prompt, future, expected_result, expected_exception):
        if future.exception(timeout=0.01) is not None:
            assert expected_exception is not None, \
                (prompt + ', fast exception check fail.',
                 expected_result, future.exception())
        else:
            assert future.result(timeout=0.01) == expected_result, \
                (prompt + ', fast result check fail.',
                 expected_result, future.result())
        try:
            if expected_exception is not None:
                future.result()
                assert False, prompt + ', result check fail.'
            else:
                assert future.result() == expected_result, \
                    prompt + ', result check fail.'
        except Exception as e:
            assert type(e) == expected

# Generated at 2022-06-14 13:44:37.820015
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import functools
    import itertools
    from datetime import timedelta

    def slow_worker(t):
        """Simulate slow worker"""
        time.sleep(t)
        return t

    def fast_worker(t):
        """Simulate fast worker"""
        time.sleep(t)
        return t

    delay = 0.8
    delays = []
    mw = MonoWorker()
    for i in tqdm_auto.tqdm(itertools.count(), total=5, desc='test_MonoWorker_submit'):
        delays.append(mw.submit(functools.partial(slow_worker, delay)))
        delay = fast_worker(delay / 2)

    # Result
    slow = set([f.result() for f in delays[:3]])
   

# Generated at 2022-06-14 13:44:48.408320
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import unittest
    import threading
    import concurrent.futures

    def slow_str(s):
        time.sleep(0.1)
        return str(s)

    def slow_exception():
        time.sleep(0.1)
        raise Exception('bleh!')

    def slow_return():
        time.sleep(0.1)
        return 42

    def slow_result(s):
        time.sleep(0.1)
        return (s, 42)

    class TestThreadPoolExecutor(concurrent.futures.ThreadPoolExecutor):
        """
        Derived class to ensure that all worker threads are closed immediately
        without waiting for all tasks to finish.
        """

# Generated at 2022-06-14 13:44:57.939723
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from .tests import get_bar

    def waitjust(i):
        time.sleep(i)
        return i

    with get_bar() as (worker, bar, bar2, bar3):
        f1 = worker.submit(waitjust, 1)
        f2 = worker.submit(waitjust, 1)
        f3 = worker.submit(waitjust, 1)
        f1.result()
        f2.result()
        f3.result()
        assert f1.done() and f1.result() == 1
        assert f2.done() and f2.result() is None
        assert f3.done() and f3.result() == 1

        f4 = worker.submit(waitjust, 1)
        f4.cancel()
        f4.result()
        assert f4.done()

# Generated at 2022-06-14 13:45:03.171634
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def func_wait(x, t=0.1, msg=""):
        """Sleep `t` seconds, then return `x`."""
        time.sleep(t)
        return x

    # Create a worker
    worker = MonoWorker()

    # Submit a task and wait for it to finish
 

# Generated at 2022-06-14 13:45:10.904172
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def test_function(id, delay):
        time.sleep(delay)
        return id

    mw = MonoWorker()
    assert len(mw.futures) == 0

    # submit first one
    future1 = mw.submit(test_function, '1st', 0.5)
    assert len(mw.futures) == 1
    assert future1.running()

    # submit second one (should block until 1st is done and drop waiting 2nd)
    future2 = mw.submit(test_function, '2nd', 0.1)
    assert len(mw.futures) == 1
    assert future2.cancelled()

    # wait for 1st to be done and submit third one (will replace 1st)

# Generated at 2022-06-14 13:45:11.825090
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random, time

# Generated at 2022-06-14 13:45:22.042097
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from random import randint

    p = MonoWorker()
    assert p.futures == deque([], 2)
    x = p.submit(lambda x: time.sleep(randint(1, 9) / 10), 'done 0')
    time.sleep(0.05)
    assert len(p.futures) == 1
    assert p.futures[0] is x
    y = p.submit(lambda x: time.sleep(randint(1, 9) / 100), 'done 1')
    time.sleep(0.01)
    assert len(p.futures) == 2
    assert p.futures[0] is x
    assert p.futures[1] is y

# Generated at 2022-06-14 13:45:31.230908
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def fun(x):
        time.sleep(x)
        return x

    mw = MonoWorker()
    f1 = mw.submit(fun, 1)
    f2 = mw.submit(fun, 2)
    time.sleep(1.5)
    assert f1.done()
    assert f2.done()
    assert f1.result() == 1
    assert f2.result() == 2

    f3 = mw.submit(fun, 1)
    time.sleep(1)
    assert f1.done()
    assert f2.done()
    assert f3.done()
    assert f1.result() == 1
    assert f2.result() == 2
    assert f3.result() == 1

# Generated at 2022-06-14 13:45:41.278460
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test method submit of class MonoWorker"""

    def sleeper(seconds, retrn=None):
        import time
        time.sleep(seconds)
        return retrn

    worker = MonoWorker()

    # submit two functions in parallel
    # they will remain active until they are completed
    long = worker.submit(sleeper, 2)
    short = worker.submit(sleeper, 1, 1)

    # finish the first submitted function
    long.result()
    # submit another function in the meantime
    worker.submit(sleeper, 3)

    # ensure that only the second submitted function is active
    # the first submitted function is now discarded
    assert not long.done()
    assert not long.cancel()
    assert not long.cancelled()
    assert short.done()
    assert short.result() == 1
    # the worker

# Generated at 2022-06-14 13:45:52.882256
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Unit test for method submit of class MonoWorker"""
    import time
    import threading
    from itertools import count

    class Log(object):
        """Logger-like class to keep track of calls to a function."""
        def __init__(self):
            self._calls = []
            self.count = count()

        def call(self):
            self._calls.append(next(self.count))

        def __str__(self):
            return str(self._calls)

    def do_work(log):
        """Do some work and call the log"""
        time.sleep(1)
        log.call()

    log = Log()
    mono_worker = MonoWorker()
    # First submit
    main_start_time = time.time()

# Generated at 2022-06-14 13:46:02.138985
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Unit test for method submit of class MonoWorker.
    """
    from time import sleep
    from ..utils import format_sizeof

    def a(data):
        print('  BuffA: {}'.format(format_sizeof(data)))
        sleep(0.5)
        return len(data)

    def b(data):
        print('  BuffB: {}'.format(format_sizeof(data)))
        sleep(2)
        return len(data)

    def c(data):
        print('  BuffC: {}'.format(format_sizeof(data)))
        sleep(2)
        return len(data)

    worker = MonoWorker()
    a_fut = worker.submit(a, b'a')
    b_fut = worker.submit(b, b'b')
    c_

# Generated at 2022-06-14 13:46:12.529981
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random as rand, choice
    from warnings import catch_warnings
    from concurrent.futures import CancelledError
    from os import name as os_name

    def warning(msg):
        tqdm_auto.write(msg)

    def snooze(timeout, exception):
        sleep(rand() * timeout)
        raise exception

    with catch_warnings(record=True) as ws:
        m = MonoWorker()
        try:
            m.pool.submit  # pylint: disable=pointless-statement
        except AttributeError:
            pass
        else:
            raise RuntimeError("ThreadPoolExecutor not yet instantiated")
        m.submit(snooze, timeout=0, exception=ValueError("no error"))
        # test warning

# Generated at 2022-06-14 13:46:19.636346
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def long_running_func():
        sleep(1)
        return 1

    def really_long_running_func():
        sleep(2)
        return 1

    mw = MonoWorker()
    mw.submit(long_running_func)
    for _ in range(1000):
        sleep(0.001)
        mw.submit(long_running_func)  # should be discarded

    mw.submit(really_long_running_func)
    sleep(1)
    assert all(f.done() for f in mw.futures)

# Generated at 2022-06-14 13:46:29.077680
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event
    from time import sleep
    from unittest import TestCase

    class TestMonoWorker(TestCase):
        @classmethod
        def setUpClass(cls):
            cls.start_event = Event()
            cls.f1_event = Event()
            cls.f2_event = Event()

            def f0():
                cls.start_event.set()
                sleep(1)

            def f1():
                cls.start_event.wait()
                cls.f1_event.set()
                sleep(1)

            def f2():
                cls.f1_event.wait()
                cls.f2_event.set()
                sleep(1)


# Generated at 2022-06-14 13:46:34.338675
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def proc_1():
        tqdm_auto.write('Process 1')

    def proc_2():
        tqdm_auto.write('Process 2')
        sleep(1)

    def proc_3():
        tqdm_auto.write('Process 3')
        sleep(1)

    mw = MonoWorker()
    mw.submit(proc_1)
    mw.submit(proc_2)
    mw.submit(proc_3)  # this should not be processed

# Generated at 2022-06-14 13:46:44.904499
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .wrappers import tqdm_pandas  # noqa, needed for mocking
    import time
    import sys

    def time_print(s):
        time.sleep(0.05)
        tqdm_auto.write(str(s))

    N = 5
    strs = list(map(str, range(N)))

    p = MonoWorker()

    # mock inside tqdm_pandas
    old_write = sys.stdout.write
    sys.stdout.write = tqdm_pandas.auto.tqdm_auto.write

# Generated at 2022-06-14 13:46:51.152626
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import multiprocessing
    from .threader import threader
    from .asyncio import reaso

# Generated at 2022-06-14 13:47:00.466225
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    try:
        import pytest
    except ImportError:
        raise SkipTest()
    import time
    import threading
    from tqdm.auto import tqdm_auto
    count = 0
    # Note: although this does work on Windows,
    # it requires minimal usage of the CPU to not delay tests
    count_max = 1000

    def inc(x):
        global count
        for i in tqdm_auto(range(x), desc='inc', leave=False):
            count += 1
            time.sleep(0.001)
        return True

    worker = MonoWorker()

    def submit_inc(duration=2):
        global count
        worker.submit(inc, count_max)
        # simulate the time a task would take to run
        time.sleep(duration)
        count = 0

    # Only one

# Generated at 2022-06-14 13:47:09.236995
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import shuffle
    def f(sleep_sec):
        sleep(sleep_sec)
        pass

    mw = MonoWorker()
    future = mw.submit(f, 0.1)
    assert len(mw.futures) == 1
    assert mw.futures[0].done() is False
    future.result()
    assert mw.futures[0].done() is True
    future = mw.submit(f, 0.1)
    assert len(mw.futures) == 1
    assert future is mw.futures[0]
    assert future.done() is False
    try:
        mw.submit(1/0)
        assert False
    except:
        assert True

# Generated at 2022-06-14 13:47:20.338623
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test the methods of `MonoWorker`."""
    import time

    def assert_futures_states(states, futures):
        """`states` is a list of strings representing expected future states."""
        assert len(states) == len(futures)
        for state, future in zip(states, futures):
            if state == 'CANCELLED':
                assert future.cancelled()
            elif state == 'DONE':
                assert future.done()
            elif state == 'PENDING':
                assert not future.done()
            else:
                assert False, "invalid state: {}".format(state)

    def assert_running(mw, future):
        """Make sure only the selected future is running."""

# Generated at 2022-06-14 13:47:23.591631
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    mw = MonoWorker()
    f1 = mw.submit(sleep, 1)
    f2 = mw.submit(sleep, 2)
    assert f2.done()

# Generated at 2022-06-14 13:47:33.303634
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ..utils import format_sizeof
    import sys
    import os

    def mem_info(mem=sys.getsizeof):
        return format_sizeof(sum(mem(x) for x in MonoWorker.__dict__.values()), precision=2)

    print("Used memory:", mem_info())

    def info(msg=""):
        print(
            "{:28.28} >>> {:10.10} {:15.15} | {}".format(
                "Mem usage", str(os.getpid()), mem_info(), msg))

    def foo(a, b=None):
        import sys
        info(a)
        sleep(1)
        info(a)

    def foo2(a, b=None):
        import sys
        info(a)
        sleep(2)

# Generated at 2022-06-14 13:47:44.526799
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    f1 = f2 = f3 = f4 = f5 = f6 = None

    def wait(i):
        time.sleep(0.1 * i)

# Generated at 2022-06-14 13:47:54.172152
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test method submit of class MonoWorker."""
    import time
    from ..utils import _range
    def wait(duration):
        """Dummy function pretending to do something."""
        time.sleep(duration)
    mw = MonoWorker()
    run1 = mw.submit(wait, 1.)
    time.sleep(.25)
    run2 = mw.submit(wait, 1.)
    time.sleep(.25)
    run3 = mw.submit(wait, 1.)
    time.sleep(.25)
    assert len(mw.futures) == 1
    assert run3.done()
    assert not run2.done()
    assert not run1.done()
    time.sleep(.25)
    assert len(mw.futures) == 1
    assert run3.done

# Generated at 2022-06-14 13:48:04.352066
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def run_and_sleep(sleeptime):
        tqdm_auto.write("doing stuff " + str(sleeptime))
        time.sleep(sleeptime)
        return "done " + str(sleeptime)
    mw = MonoWorker()

    # submit first
    r1 = mw.submit(run_and_sleep, 1)
    assert not r1.done()
    # submit second before completion of first
    r2 = mw.submit(run_and_sleep, 2)
    assert r1.done()
    assert not r2.done()
    # submit third before completion of second
    r3 = mw.submit(run_and_sleep, 3)
    assert r2.done()
    assert not r3.done()

# Generated at 2022-06-14 13:48:13.989553
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ..utils import format_sizeof

    def test(sleep_time, filled_string, size=1):
        sleep(sleep_time)
        return filled_string * size

    filled_string = 'test'
    size = 1024 * 1024 * 8 // len(filled_string)
    sleep_time = 0.2
    test_threads = [(sleep_time, filled_string, size),
                    (sleep_time * 2, filled_string, size),
                    (sleep_time * 3, filled_string, size),
                    (sleep_time * 4, filled_string, size),
                    (sleep_time * 5, filled_string, size)]

# Generated at 2022-06-14 13:48:29.868949
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    pool = MonoWorker()

    def runner(x):
        time.sleep(x)
        return x * 2

    def test():
        durations = [random.random() / 10 for i in range(10)]
        tqdm_auto.write('\ntest_MonoWorker_submit')
        tqdm_auto.write(str(durations))
        results = []
        for duration in tqdm_auto.tqdm(durations, desc='Test'):
            result = pool.submit(runner, duration)
            results.append(result)
            time.sleep(duration / 2)
        tqdm_auto.write(str(results))
        for result in results:
            tqdm_auto.write(str(result.result()))

    test()
    test

# Generated at 2022-06-14 13:48:38.890168
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> import time
    >>> def func(a, b):
    ...     time.sleep(1)
    ...     return a+b
    >>> mw = MonoWorker()
    >>> f1 = mw.submit(func, 1, 2)
    >>> f2 = mw.submit(func, 3, 4)
    >>> f3 = mw.submit(func, 5, 6)
    >>> f1.result()
    Traceback (most recent call last):
    ...
    concurrent.futures._base.CancelledError
    >>> f2.result()
    Traceback (most recent call last):
    ...
    concurrent.futures._base.CancelledError
    >>> f3.result()
    11
    """
    pass

if __name__ == "__main__":
    import doct

# Generated at 2022-06-14 13:48:48.847799
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from concurrent.futures import TimeoutError

    import time
    from .tests import TestTqdmContribIO, TestTqdmContrib

    class TestMonoWorker(TestTqdmContribIO):
        def test_submit(self):
            from threading import Event
            from requests import get as net_get

            def bg(timeout, url):
                try:
                    evt.set()  # signal background started

                    # (emulate) long-running computation
                    time.sleep(timeout)

                    # get some data online
                    return net_get(url).content.decode('utf-8')
                except TimeoutError:
                    return 'Timeout!'
                finally:
                    evt.set()  # signal background ended

            # task execution

# Generated at 2022-06-14 13:48:57.655219
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import sys

    def my_func(x):
        # print('my_func is sleeping %d seconds' % x)
        time.sleep(x)
        return x

    mw = MonoWorker()
    for _ in range(5):
        mw.submit(my_func, random.random() * 5)
        time.sleep(0.5)
        print('.', file=sys.stderr, end='')
        time.sleep(1)
    print('\n\n')
    for _ in range(3):
        mw.submit(my_func, random.random() * 5)
        time.sleep(0.5)
        print('.', file=sys.stderr, end='')
        time.sleep(1)

# Generated at 2022-06-14 13:49:03.610764
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..auto import tqdm
    n = 8
    mw = MonoWorker()
    with tqdm(total=n * 2, unit='it', leave=False) as t:
        for i in range(n):
            mw.submit(t.update, 1)
        for i in range(n):
            mw.submit(time.sleep, 0.1)
            mw.submit(t.update)
    assert t.n == t.total

# Generated at 2022-06-14 13:49:12.010270
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import Value
    from multiprocessing.sharedctypes import RawValue
    from threading import Lock, Thread
    from concurrent.futures import FIRST_EXCEPTION
    from . import _range
    from tqdm.contrib.concurrent import MonoWorker

    def reset(values):
        for v in values:
            v.value = 0

    def do_add(target, values):
        for i in range(target):
            for v in values:
                v.value += 1

    def do_sub(target, values):
        for i in range(target):
            for v in values:
                v.value -= 1

    check = 1e6
    # check = 20
    start_val = check / 2
    i = check / 2
    val = []
   

# Generated at 2022-06-14 13:49:15.668461
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from . import _test_MonoWorker_submit

    # we need to make sure that submit takes some time
    _test_MonoWorker_submit.submit = lambda func, *args, **kwargs: \
        tqdm_auto.sleep(1, dynamic_ncols=True).__next__()
    _test_MonoWorker_submit.main()

# Generated at 2022-06-14 13:49:22.354972
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    worker = MonoWorker()
    import time
    assert len(worker.futures) == 0
    for i in tqdm_auto.trange(3):
        worker.submit(time.sleep, max(1, 1 - i))
        time.sleep(0.2)
        assert len(worker.futures) == 1
    time.sleep(1)
    assert len(worker.futures) == 0

# Generated at 2022-06-14 13:49:32.853878
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys

    def print_msg(msg, delay=1):
        time.sleep(delay)
        sys.stdout.write(msg)


# Generated at 2022-06-14 13:49:41.154581
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Tests the method `submit` of class `MonoWorker`."""
    import sys
    import os
    import time
    import math
    from threading import Thread
    from random import random
    from . import test_MonoWorker_test_func

    # Testing the class `MonoWorker`
    tqdm_auto.write("Testing the class `MonoWorker`...")

    # Defining a sub-function for the same
    def test_MonoWorker_submit_sub(no_of_threads):
        # Creating an instance of the class `MonoWorker`
        obj = test_MonoWorker_test_func.MonoWorker()

        # Creating threads
        threadList = []

# Generated at 2022-06-14 13:50:06.210103
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import sys
    import traceback
    from concurrent.futures import TimeoutError

    def p(i, j):
        sleep(i)
        tqdm_auto.write(str(j))
        sys.stderr.write('\n')

    mw = MonoWorker()

    # Submit job with longer initial timeout
    timeout = 2
    future = mw.submit(p, 2, 0)
    try:
        future.result(timeout=timeout)
    except TimeoutError:
        # Cancel job
        future.cancel()
    timeout += 0.1

    # Submit another job with shorter timeout
    future = mw.submit(p, 3, 1)

# Generated at 2022-06-14 13:50:14.555901
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time as time_module

    def test_submit(MonoWorker_):
        def test_func():
            time_module.sleep(0.5)
        _ = MonoWorker_.submit(test_func)
        return _

    MonoWorker_ = MonoWorker()
    with tqdm_auto.trange(2, desc='MonoWorker_') as trange:
        for i in trange:
            _ = test_submit(MonoWorker_)
            time_module.sleep(0.5)
            _.result()
            trange.set_postfix(finished=_, result=_.result())



# Generated at 2022-06-14 13:50:23.677752
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def run_futures(wait_time):
        mw = MonoWorker()

        def f(i):
            # print(i)
            time.sleep(wait_time)
            return i

        try:
            mw.submit(f, 0)
            mw.submit(f, 1)
            mw.submit(f, 2)
            mw.submit(f, 3)
            export = [mw.submit(f, 4) for _ in range(10)]
            _ = [x.result() for x in export]
        except KeyboardInterrupt:
            pass

    assert(run_futures(wait_time=0) is None)

# Generated at 2022-06-14 13:50:33.424473
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # import time
    import sys
    # from shutil import rmtree
    from tempfile import gettempdir, mkdtemp

    # def touch(filename):
    #     with open(filename, 'w', encoding='utf-8') as f:
    #         f.write('')
    #         f.flush()

    # def ls(dir):
    #     print('ls %s' % dir)
    #     return sorted(os.listdir(dir))

    def make_files(dir, n):
        for i in n:
            with open(os.path.join(dir, str(i)), 'w', encoding='utf-8') as f:
                f.write('')
                f.flush()

    # def rm_files(dir, files):
    #     return [os.remove(os.path

# Generated at 2022-06-14 13:50:38.579048
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func1():
        import time
        time.sleep(1)
        return "Done"
    def func2():
        import time
        time.sleep(0.5)
        return "Replaced"

    worker = MonoWorker()
    f1 = worker.submit(func1)
    f2 = worker.submit(func2)
    assert f1 is None
    assert f2.result() == "Replaced"

# Generated at 2022-06-14 13:50:47.407444
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def printer(i):
        return i

    def sleep(i):
        time.sleep(1)
        return i

    mw = MonoWorker()

    # submit running task
    mw.submit(printer, 1)

    # submit waiting task
    mw.submit(sleep, 2)
    mw.submit(printer, 3)
    mw.submit(sleep, 4)

    assert mw.futures[-1].done()  # waiting task done
    assert len(mw.futures) == 1  # running task cleared
    assert mw.futures[0].result() == 4  # waiting task succeeded
    assert len(list(mw.futures[0].__dict__['_callbacks'])) == 0  # no listeners

# Generated at 2022-06-14 13:50:58.314138
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import format_sizeof

    def text_gen(size, wait=0.1):
        """generator of text of given size"""
        s = 0
        while s < size:
            time.sleep(wait)
            n = size - s
            s += 1
            if   n > 4: yield "abcd"
            elif n > 2: yield "ef"
            elif n > 1: yield "g"
            else:       yield ""

    mg = text_gen(16)  # main generator
    sg = text_gen(32)  # secondary generator
    wk = MonoWorker()  # worker
    print("Main:", next(mg))
    wk.submit(tqdm_auto.write, format_sizeof(1))

# Generated at 2022-06-14 13:51:09.021036
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import tqdm.contrib as tqdm_contrib

    class Foo(object):
        def __init__(self, i):
            self.i = i
            self.worker = tqdm_contrib.MonoWorker()
            self.future = None

        def func(self):
            time.sleep(1)
            return self.i

        def submit(self):
            if self.future is None or self.future.done():
                self.future = self.worker.submit(self.func)
            return self.future

        def wait(self):
            return self.future.result()

    foo = Foo(0)
    foo.submit()
    time.sleep(.5)
    expected = foo.wait()
    foo.submit()
    foo.submit()

# Generated at 2022-06-14 13:51:18.932453
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from datetime import datetime

    def print_now():
        for i in range(3):
            sleep(1)
            tqdm_auto.write(str(datetime.now()))

    worker = MonoWorker()
    worker.submit(print_now)
    sleep(1)
    worker.submit(print_now)
    sleep(1)
    worker.submit(print_now)
    sleep(1)
    worker.submit(print_now)
    sleep(1)
    worker.submit(print_now)
    sleep(1)
    worker.submit(print_now)
    sleep(1)
    worker.submit(print_now)
    sleep(1)
    worker.submit(print_now)
    sleep(1)
    worker.submit(print_now)

# Generated at 2022-06-14 13:51:30.358909
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def is_cancel(f):
        try:
            f.result()
        except Exception as e:
            return isinstance(e, concurrent.futures.CancelledError)
        raise Exception("Uncaught exception")

    class Test(object):
        def __init__(self):
            self.worker = MonoWorker()
            # Create a list of futures
            self.futures = []
            for i in range(10):
                f = self.worker.submit(time.sleep, 0.1)
                self.futures.append(f)
            # Wait for futures to complete
            for f in self.futures:
                f.result()
            # Check that all submitted futures except the last have been cancelled
            for f in self.futures[:-1]:
                assert is_

# Generated at 2022-06-14 13:52:09.131313
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import json
    import sys
    import os
    from contextlib import contextmanager
    from six.moves import cStringIO as StringIO
    from ..utils import _range as trange
    from ..std import iteritems as tqdm_iteritems

    @contextmanager
    def stdout_replaced():
        """
        Temporarily replace stdout and stderr by a StringIO object.
        """
        save_stdout, save_stderr = sys.stdout, sys.stderr
        try:
            yield StringIO(), StringIO()
        finally:
            sys.stdout, sys.stderr = save_stdout, save_stderr

    def log_process():
        time.sleep(.5)
        return ("process", os.getpid())


# Generated at 2022-06-14 13:52:15.575665
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .util_wrap import _get_running_future

    def test_submit(count=2, delay_loop=0, delay_submit=0, delay_done=0):
        from time import sleep

        def f(n):
            sleep(delay_done)
            return n

        test_mw = MonoWorker()
        futures = deque()
        for i in tqdm_auto.trange(count):
            sleep(delay_submit)
            futures.append(test_mw.submit(f, i))
            sleep(delay_loop)
        return tuple(_get_running_future(fut) for fut in futures)

    assert test_submit(count=2, delay_loop=0, delay_submit=0, delay_done=0) == (1,)

# Generated at 2022-06-14 13:52:25.859993
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..auto import trange
    from concurrent.futures import wait, FIRST_COMPLETED

    def wait_for(x):
        try:
            wait(x, return_when=FIRST_COMPLETED)
        except Exception:
            pass

    def sleeper(i, t):
        time.sleep(t)
        return i

    worker = MonoWorker()

    # 2-second task overwritten by 1-second
    worker.submit(sleeper, 1, 1)
    worker.submit(sleeper, 2, 2)
    assert worker.futures[0].result() == 1

    # 1-second task overwritten by 0.5-second
    worker.submit(sleeper, 3, 0.5)
    assert worker.futures[0].result() == 3

    # 2-second task running

# Generated at 2022-06-14 13:52:33.749586
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import cpu_count

    def on_exc(e):
        tqdm_auto.write(str(e))

    def on_done(f):
        tqdm_auto.write(f.result())

    workers = MonoWorker()

    for i in range(cpu_count()):
        workers.submit(lambda: "done", on_done, on_exc)
    sleep(1)

    n = 2
    tqdm_auto.write(str(n) + " should be done:")
    futures = [workers.submit(lambda: "done", on_done, on_exc) for _ in range(n)]
    for i in range(n):
        sleep(1)