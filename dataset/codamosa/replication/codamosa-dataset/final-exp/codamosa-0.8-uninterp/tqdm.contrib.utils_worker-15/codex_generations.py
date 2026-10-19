

# Generated at 2022-06-14 13:42:52.688773
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep, time
    from random import randint
    from os import getpid
    import pickle
    from multiprocessing import Process

    def sleeper(i):
        sleep(float(i) / 4)
        return i

    def f():
        try:
            mw = MonoWorker()
            l = []
            for i in range(10):
                # print i, getpid()
                l.append(mw.submit(sleeper, i))
        except Exception as e:
            print(str(e))
        else:
            return l

    t0 = time()
    l = f()
    l = [p.result() for p in l]
    print(l)

    assert l == list(range(10))

    t1 = time()

    p = Process(target=f)


# Generated at 2022-06-14 13:43:01.818378
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> test_MonoWorker_submit()
    """
    from time import sleep
    from random import random

    def print_wait_random(exp, wait_range=(0.0, 1.0)):
        sleep(random() * (wait_range[1] - wait_range[0]) + wait_range[0])
        print(exp)

    worker = MonoWorker()
    worker.submit(print_wait_random, 'a')
    sleep(0.5)
    worker.submit(print_wait_random, 'b')
    sleep(0.1)
    worker.submit(print_wait_random, 'c', wait_range=(0.0, 0.1))
    sleep(0.5)
    worker.submit(print_wait_random, 'd')


# Generated at 2022-06-14 13:43:12.800259
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from concurrent.futures import as_completed
    from threading import Thread, Event

    def task(dur, msg):
        time.sleep(dur)
        tqdm_auto.write(msg)

    n = 3
    w0 = MonoWorker()
    dur = 0.1
    w0.submit(task, dur, "1")
    w0.submit(task, dur, "2")
    for i in tqdm_auto.trange(n, desc='#futures'):
        f = w0.submit(task, dur, str(i+3))
        time.sleep(dur/2)
    for f in as_completed(w0.futures):
        f.result()
    w0.shutdown()


# Generated at 2022-06-14 13:43:20.622826
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from random import randrange
    from time import sleep
    mw = MonoWorker()
    d = {}

    def count(i):
        sleep(randrange(0, 2))
        d[i] = True

    for i in range(10):
        mw.submit(count, i)
    assert len(d) <= 1, "Futures discarded: {}".format(
        [k for k, v in d.items() if not v])


if __name__ == '__main__':
    from .__main__ import main  # noqa
    main()

# Generated at 2022-06-14 13:43:27.938942
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from multiprocessing import TimeoutError

    def _test_MonoWorker_submit(
            throws_exception=False,
            background_exception=False,
            cancel_future=False,
            cancel_future_after_done=False,
            cancellation_exception=False,
            timeout=None
    ):  # pragma: no cover
        import time
        import random
        import errno
        import functools

        def raise_timeout_error(*args, **kwargs):
            raise TimeoutError(errno.ETIMEDOUT, 'Operation timed out')

        if random.random() < 0.5:
            raise_exception = raise_timeout_error
        else:
            raise_exception = IOError


# Generated at 2022-06-14 13:43:39.199910
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def spam(n):
        sleep(n)
        return n

    def ham(n):
        sleep(n)
        return -n

    # test waiting clears if new task is submitted
    mw = MonoWorker()
    mw.submit(spam, 1)
    mw.submit(ham, 3)

    mw.submit(ham, 2)
    assert mw.futures[0].cancelled()

    mw.submit(ham, 4)
    assert mw.futures[0].done()

    mw.futures[0].result() == -4

    # test running resubmits if no waiting
    mw = MonoWorker()
    mw.submit(spam, 1)
    mw.submit(ham, 3)
    waiting = m

# Generated at 2022-06-14 13:43:46.884071
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time  # NOQA
    mw = MonoWorker()
    # submit job 1
    job1 = mw.submit(time.sleep, 1)
    assert job1.done() is False
    # submit job 2
    job2 = mw.submit(time.sleep, 0)
    assert job1.done() is False
    time.sleep(0.1)
    assert job1.done() is False
    assert job2.done() is True
    time.sleep(1)
    assert job1.done() is True

# Generated at 2022-06-14 13:43:55.085749
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from concurrent.futures import Future
    from tqdm import tqdm
    from time import sleep
    from random import random
    from unittest import TestCase

    def do_something(n):
        sleep(random())
        return n ** 2

    class Test(TestCase):
        def assertFuturesEqual(self, a, b):
            assert isinstance(a, Future)
            assert isinstance(b, Future)
            self.assertEqual(a.result(), b.result())

        def test_submit(self):
            worker = MonoWorker()
            f0 = worker.submit(do_something, 3)
            f1 = worker.submit(do_something, 4)
            with tqdm(desc='test_submit') as t:
                while True:
                    t.update()
                    # NOTE

# Generated at 2022-06-14 13:44:02.209456
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    #  print ("initiating unit test for method: test_MonoWorker_submit()")
    import time

    def f(t):
        time.sleep(t)
        return t

    mw = MonoWorker()
    t0 = 0.2
    v0 = mw.submit(f, t0)
    t1 = 0.3
    v1 = mw.submit(f, t1)
    t1b = v1.result()
    t2 = mw.submit(f, 0.1).result()
    assert t1 == t1b == t2
    t0b = v0.result()
    assert t0 == t0b < t1

# Generated at 2022-06-14 13:44:09.679803
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from nose import tools
    from time import sleep


    def wait_a_sec():
        sleep(1)
        return 0


    def fast_func():
        sleep(0.5)
        return 1


    def faster_func():
        sleep(0.1)
        return 2


    mw = MonoWorker()
    pool = mw.pool
    futures = mw.futures

    # Check constant
    tools.assert_equal(futures.maxlen, 2)

    # Check add jobs
    f1 = mw.submit(wait_a_sec)
    tools.assert_equal(len(futures), 1)
    f2 = mw.submit(wait_a_sec)
    tools.assert_equal(len(futures), 2)

# Generated at 2022-06-14 13:44:21.992467
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from unittest import TestCase
    from unittest.mock import Mock

    class TestMonoWorkerSubmit(TestCase):

        def setUp(self):
            self.mock = Mock()
            self.m = MonoWorker()

        def tearDown(self):
            for future in self.m.futures:
                future.cancel()

        def test_submit(self):
            self.m.submit(self.mock, 0.1)
            sleep(0.2)
            self.assertTrue(self.m.futures[-1].done())
            self.assertTrue(self.mock.called)
            self.m.submit(self.mock, 0.1)
            self.assertFalse(self.mock.called)

# Generated at 2022-06-14 13:44:31.221179
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def slow_inc_1(x):
        sleep(0.5)
        return x + 1
    def slow_inc_2(x, n=1):
        sleep(0.5)
        return x + n

    mw = MonoWorker()

    # Calling submit twice (without waiting) will give calling order (first, second)
    first = mw.submit(slow_inc_1, 1)
    second = mw.submit(slow_inc_1, 2)
    assert first.result() == 2
    assert second.result() == 3

    # Calling submit with more arguments will still work
    third = mw.submit(slow_inc_2, 3, n=2)
    assert third.result() == 5

    # Calling submit with different arguments will replace previous (second) call

# Generated at 2022-06-14 13:44:42.014293
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:44:51.971835
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import Pool

    def f(x):
        sleep(1)
        return x

    def test_submit(mono_worker, pool):
        status = []

        def g(x):
            sleep(1)
            status.append(1)

        mono_worker.submit(g, 0)
        mono_worker.submit(g, 1)
        pool.apply_async(g, (0, ))
        pool.apply_async(g, (0, ))
        assert status == []
        sleep(3)
        assert status == [1]

        status.clear()
        mono_worker.submit(g, 0)
        mono_worker.submit(g, 1)
        pool.apply_async(g, (0, ))

# Generated at 2022-06-14 13:44:59.346147
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    import tqdm.contrib.concurrency
    from tqdm.contrib.concurrency import MonoWorker

    def run_task(duration, name):
        tqdm.tqdm.write(name)
        tqdm.tqdm.write('sleeping {0}s'.format(duration))
        time.sleep(duration)
        tqdm.tqdm.write('slept {0}s'.format(duration))

    tqdm.tqdm.write('Starting')
    worker = MonoWorker()

    tqdm.tqdm.write('submit 1')
    worker.submit(run_task, 1, 1)
    tqdm.tqdm.write('submit 2')
    worker.submit(run_task, 1, 2)
    tqdm.tqdm

# Generated at 2022-06-14 13:45:10.591283
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def func_test(t, n='test'):
        time.sleep(t)
        return n

    # Test: len(futures) < futures.maxlen
    mw = MonoWorker()
    f1 = mw.submit(func_test, t=0.5, n='1')
    f2 = mw.submit(func_test, t=0.5, n='2')
    f3 = mw.submit(func_test, t=0.5, n='3')
    assert f1.result() == '1'
    assert f2.result() == '2'
    assert f3.result() == '3'

    # Test: len(futures) == futures.maxlen
    mw = MonoWorker()

# Generated at 2022-06-14 13:45:19.599946
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:45:22.459502
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from functools import partial
    mywait = partial(time.sleep, 0.2)
    m = MonoWorker()
    for i in tqdm_auto.trange(4):
        m.submit(mywait)
    # TODO: add assertions

# Generated at 2022-06-14 13:45:34.468269
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():  # pragma: no cover
    import time
    import threading
    from tqdm.autonotebook import tqdm

    def slow_fib(n):
        """Return the nth fibonacci number"""
        if n < 2:
            return n
        return slow_fib(n - 1) + slow_fib(n - 2)

    def fib(n):
        """Return the nth fibonacci number"""
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    fibs = [MonoWorker().submit(fib, i) for i in tqdm(range(100))]
    assert all(f.done() for f in fibs)

# Generated at 2022-06-14 13:45:43.793323
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def identity(x):
        return x

    def submit(x):
        return MW.submit(identity, x)

    def sleep_submit(x):
        return MW.submit(sleep, x)

    MW = MonoWorker()

    assert submit(10).result() == 10
    assert submit(20).result() == 20  # replaced
    assert len(MW.futures) == 1

    Fut = submit(20)
    assert len(MW.futures) == 2
    assert Fut.result() == 20

    Fut = sleep_submit(1)
    Fut2 = submit(20)  # replaced
    sleep(0.1)
    assert len(MW.futures) == 2
    try:
        Fut.result()
    except Exception as e:
        assert str(e).split

# Generated at 2022-06-14 13:45:54.948464
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, random
    size = 10  # Number of tasks to test
    r = random.Random(42)
    def sleeprand(i):
        time.sleep(r.random() / float(size))
        return i
    with tqdm_auto.tqdm(total=size, unit='test') as P:
        wp = MonoWorker()
        for i in range(size):
            wp.submit(sleeprand, i)
            P.update()



# Generated at 2022-06-14 13:46:00.262401
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def func(x, y):
        return x + y

    m = MonoWorker()
    for i in tqdm_auto.tqdm(range(10)):
        m.submit(func, i, i)
        sleep(0.01)

# Generated at 2022-06-14 13:46:09.250743
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys, random, time
    from ..pandas import tqdm_pandas  # NOQA

    def prt(s):
        print(s, file=sys.stderr)

    def get_data():
        """Prepare DataFrame with random data, and then sleep a while."""
        df = tqdm_pandas(map(lambda n: n + random.random(), range(10)))
        time.sleep(1)
        return df

    def save_data(df):
        """Save DataFrame to a file, and then sleep a while."""
        df.to_csv('data.snp', sep='\t')
        time.sleep(1)

    def load_data():
        """Load DataFrame from a file, and then sleep a while."""
        df = tqdm_pand

# Generated at 2022-06-14 13:46:18.992497
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from os import getpid
    from threading import Thread

    def func(t):
        sleep(t)
        return getpid()

    def test(expect, t):
        w = MonoWorker()
        p = w.submit(func, t)
        q = w.submit(func, t * 2)
        q = w.submit(func, t * 4)
        assert p.done()
        assert not q.done()
        assert q.result() == expect
        # q.done() is True here

    t = 0.1
    test(getpid(), t)
    t = 0.3
    test(getpid(), t)
    t = 0.5
    test(getpid(), t)

    # test concurrency
    w = MonoWorker()

# Generated at 2022-06-14 13:46:27.214049
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import Queue

    def foo(arg):
        sleep(1)
        queue.put(arg)

    queue = Queue()
    mono = MonoWorker()
    # Test no discard
    mono.submit(foo, 1)
    sleep(0.5)
    mono.submit(foo, 2)
    assert queue.get(timeout=5) == 1
    assert queue.get(timeout=5) == 2
    # Test discard waiting task
    mono.submit(foo, 3)
    sleep(0.5)
    mono.submit(foo, 4)
    sleep(0.5)
    mono.submit(foo, 5)
    assert queue.get(timeout=5) == 3
    assert queue.get(timeout=5) == 5
    # Test discard running task
   

# Generated at 2022-06-14 13:46:37.359501
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from collections import Counter
    from numpy.random import randn

    class SleepyWorker(object):
        def __init__(self):
            self.id = id(self)

        def work(self, i):
            time.sleep(0.05 * randn())
            return self.id, i

    results = Counter()
    worker = SleepyWorker()
    monoworker = MonoWorker()
    for i in range(10):
        results.update(monoworker.submit(worker.work, i).result())
    assert len(results) == 1
    assert results[worker.id] == 10
    assert monoworker.pool._threads._semlock._is_owned()  # pylint: disable=protected-access,invalid-name

# Generated at 2022-06-14 13:46:44.944527
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import tqdm
    pool = MonoWorker()

    def sleepy(*args, **kwargs):
        time.sleep(random.randint(1, 5))
        return args, kwargs

    with tqdm.tqdm(total=10) as pbar:
        for _ in range(10):
            time.sleep(random.randint(1, 2) / 100.0)
            pool.submit(sleepy, 'first', 'second', third='third').add_done_callback(
                pbar.update)

# Generated at 2022-06-14 13:46:52.213708
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import unittest

    class SampleTests(unittest.TestCase):
        """Test case for submit method of class MonoWorker"""
        def test_submit(self):
            """Test the method submit of class MonoWorker"""
            worker = MonoWorker()
            test_list = ['func1', 'func1', 'func2', 'func3', 'func4', 'func5']
            result_list = []
            for func_name in test_list:
                result_list.append(worker.submit(self.call_func, func_name))
            for result in result_list:
                self.assertEqual(result.result(), "done")

        def call_func(self, func_name):
            """Function to call by the method submit of class MonoWorker"""
            time.sleep

# Generated at 2022-06-14 13:47:02.740853
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from concurrent.futures import CancelledError
    from ..utils import _range

    worker = MonoWorker()
    for _ in _range(4):
        worker.submit(sleep, 10**8)
    # Should have popped the first two tasks
    # which are still running
    futures = worker.futures
    assert len(futures) == 2
    assert not futures[0].done()
    assert not futures[1].done()
    try:
        worker.submit(sleep, 10)
    except Exception as e:
        tqdm_auto.write(str(e))
    else:
        # Should have cancelled the first waiting task
        # and inserted the new one
        assert len(futures) == 2
        assert not futures[0].done()
        assert futures[0].cance

# Generated at 2022-06-14 13:47:12.367077
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep, time
    from threading import Lock
    mw = MonoWorker()
    lock = Lock()

    def func(x):  # Function to run
        with lock:
            tqdm_auto.write("func(%s)" % x)
        sleep(0.5)  # Simulate hard computation
        return x + 1
    def func2(x):  # Function to run
        with lock:
            tqdm_auto.write("func2(%s)" % x)
        sleep(0.5)  # Simulate hard computation
        return x + 2
    def func3(x):  # Function to run
        with lock:
            tqdm_auto.write("func3(%s)" % x)
        sleep(0.5)  # Simulate hard computation
        return x + 3



# Generated at 2022-06-14 13:47:27.062734
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def wtf(n):
        """Does nothing (but print)."""
        tqdm_auto.write(str(n))

    mw = MonoWorker()
    assert mw.submit(wtf, 1)
    assert mw.submit(wtf, 2)
    assert mw.submit(wtf, 3)
    assert mw.submit(wtf, 4)
    assert len(mw.futures) == 1
    assert mw.futures[0].result() is None
    tqdm_auto.write('ok')

# Generated at 2022-06-14 13:47:34.422213
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test the behaviour of the method submit of class MonoWorker.
    """
    import time
    worker = MonoWorker()

    def _sleep(dur):
        time.sleep(dur)
    try:
        worker.submit(_sleep, 0.3)
        worker.submit(_sleep, 0.2)
        worker.submit(_sleep, 0.1)
        worker.submit(_sleep, 0.5)
        worker.submit(_sleep, 0.4)
        worker.submit(_sleep, 0.6)
    except KeyboardInterrupt:
        pass  # No need for clean-up, KeyboardInterrupt doesn't spawn new threads



# Generated at 2022-06-14 13:47:41.822388
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    timeouts = [0.1, 0.2, 0.3, 0.4]
    worker = MonoWorker()
    for t in timeouts:
        worker.submit(time.sleep, t)
        time.sleep(0.05)
    for f in worker.futures:
        assert f.done()
    assert len(worker.futures) == 1
    assert worker.futures[0].result() < 0.42
    assert worker.futures[0].result() > 0.38


# Generated at 2022-06-14 13:47:52.520515
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from . import bar
    mw = MonoWorker()

    def func():
        time.sleep(1)

    mw.submit(func)
    mw.submit(func)

    # wait for 1st func
    mw.futures[0].result()
    assert len(mw.futures) == 1

    # submit a 3rd func while 2nd is waiting
    mw.submit(func)

    # wait for 1st and 2nd func: 2nd will get discarded, 3rd will run
    mw.futures[0].result()
    mw.futures[1].result()

    # mw.futures is empty
    assert len(mw.futures) == 0

    # try a 4th func and make sure only 3rd got lost

# Generated at 2022-06-14 13:48:03.290465
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """tqdm.contrib.MonoWorker.submit()"""
    from time import sleep
    from unittest import TestCase
    try:
        from unittest.mock import patch
    except ImportError:
        from mock import patch
    with patch('tqdm_contrib.write') as write:
        write.return_value = None
        mw = MonoWorker()
        with mw.pool:  # clear the executor
            pass
        mw.submit(sleep)
        mw.submit(sleep)
        sleep(0.5)
        mw.submit(sleep)
        mw.submit(sleep)
        mw.submit(sleep)


if __name__ == "__main__":
    from .test_MonoWorker import test_MonoWorker_submit
    test_

# Generated at 2022-06-14 13:48:13.063555
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import pytest
    mworker = MonoWorker()

    def id_function(x):
        time.sleep(0.25)
        return x

    first_future = mworker.submit(id_function, 1)
    second_future = mworker.submit(id_function, 2)
    third_future = mworker.submit(id_function, 3)
    fourth_future = mworker.submit(id_function, 4)
    assert first_future.cancelled()
    assert second_future.cancelled()
    assert fourth_future.cancelled()

    assert third_future.result() == 3
    pytest.raises(Exception, first_future.result)
    pytest.raises(Exception, second_future.result)

# Generated at 2022-06-14 13:48:22.070523
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import time
    from time import sleep

    def f(i):
        sleep(3)
        return i*i

    mw = MonoWorker()
    print("submit(f, 1)")
    _ = mw.submit(f, 1)
    print("submit(f, 2)")
    _ = mw.submit(f, 2)
    print("submit(f, 3)")
    _ = mw.submit(f, 3)

    print("Result of submit(f, 1):", _.result(), "Expected: 1")
    # This will not block here:
    print("Result of submit(f, 2):", _.result(), "Expected: None")
    print("Result of submit(f, 3):", _.result(), "Expected: 4")
    # This will block here:
   

# Generated at 2022-06-14 13:48:26.915635
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(n):
        import time
        time.sleep(n)
        return n

    # simple test
    mw = MonoWorker()
    assert mw.submit(func, 0.7)
    assert mw.submit(func, 0.5)
    import time
    time.sleep(1.0)
    assert mw.futures[0].done()
    assert mw.futures[0].result() == 0.5

# Generated at 2022-06-14 13:48:36.918865
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from . import ipy_compat

    def compute_result(secs):
        sleep(secs)
        return secs

    def run_submit_thread(secs, ncalls, nworkers):
        def get_next_result():
            """Get next result, if any"""
            sleep(.5)
            try:
                return futures.popleft().result()
            except IndexError:
                pass

        futures = deque()
        for _ in range(ncalls):
            futures.append(worker.submit(compute_result, secs))
            print(get_next_result())
        for _ in range(nworkers):
            print(get_next_result())

    nworkers = 1
    ncalls = 5
    secs = 1

    ipy_compat.setup

# Generated at 2022-06-14 13:48:43.337099
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep, time
    start = time()
    mw = MonoWorker()
    assert mw.submit(sleep, 0.02) is None  # func may be discarded
    assert mw.submit(sleep, 0.02) is None  # func may be discarded
    assert (time() - start) < 0.04
    assert mw.submit(sleep, 0.04) is None  # func may be discarded
    assert mw.submit(sleep, 0.02) is None  # func must be executed
    assert (time() - start) > 0.04
    # time.sleep(0.1)

# Generated at 2022-06-14 13:49:03.029569
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ..std.time import sleep as tqdm_sleep

    def func(*args, **kwargs):
        sleep(1)
    mw = MonoWorker()
    for i in tqdm_auto.trange(4):
        mw.submit(func)
        tqdm_sleep(0.3)



# Generated at 2022-06-14 13:49:14.505786
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def sleep_task(seconds):
        time.sleep(seconds)

    mw = MonoWorker()
    mw.submit(sleep_task, 5)
    mw.submit(sleep_task, 4)
    mw.submit(sleep_task, 3)
    mw.submit(sleep_task, 2)
    mw.submit(sleep_task, 1)
    assert mw.futures[0].done()  # 5s
    assert not mw.futures[1].done()  # 4s
    assert len(mw.futures) == 2

    mw2 = MonoWorker()
    mw2.submit(sleep_task, 5)
    mw2.submit(sleep_task, 4)
    mw2.submit(sleep_task, 3)
   

# Generated at 2022-06-14 13:49:23.097959
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    def busy_work(n, d):
        import time
        time.sleep(n)
        return d

    # Test: empty queue, one thread
    m = MonoWorker()
    assert len(m.futures) == 0
    assert m.futures.maxlen == 2
    assert len(m.pool._threads) == 1
    assert len(m.pool._work_queue) == 0
    assert m.pool._max_workers == 1

    # Test: submitting 1 task
    d = "a"
    ret = m.submit(busy_work, n=1, d=d)
    assert len(m.futures) == 1
    assert len(m.pool._threads) == 1
    assert len(m.pool._work_queue) == 0
    assert ret.running()

# Generated at 2022-06-14 13:49:33.491523
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    def task(func, *args, **kwargs):
        time.sleep(.2)
        return func(*args, **kwargs) + 1

    mw = MonoWorker()
    assert not mw.futures

    mw.submit(task, sum, [1, 2])
    assert len(mw.futures) == 1

    mw.submit(task, sum, [3, 4, 5])
    assert len(mw.futures) == 2

    mw.submit(task, sum, [6, 7])
    assert len(mw.futures) == 1
    assert mw.futures[0].result() == 18

    mw.submit(task, sum, [8, 9])
    assert len(mw.futures)

# Generated at 2022-06-14 13:49:41.571794
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Worker.submit should run asynchronously a function with arguments
    and return a future that can be used outside the class.
    """
    import time
    from ..utils import _range

    def f1(x):
        time.sleep(2)

    def f2(x):
        time.sleep(1)

    def f3(x):
        time.sleep(4)

    Worker = MonoWorker()

    for i in _range(5):
        Worker.submit(f1, i)
        time.sleep(1)

    tqdm_auto.write("start")
    for i in _range(5):
        Worker.submit(f2, i)
    time.sleep(3)
    tqdm_auto.write("end")


# Generated at 2022-06-14 13:49:51.033519
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from ..auto import tqdm
    import time
    import random
    from threading import Thread
    from .thread import ThreadShim

    event = ThreadShim.Event()
    event.set()

    def sleep_and_print(time):
        """This function will be executed by the worker thread"""
        event.wait()  # wait for release
        tqdm.write("starting sleep for %s" % time, end=' ')
        time.sleep(time)
        tqdm.write("done!")

    worker = MonoWorker()
    thread = Thread(target=worker.submit, args=(sleep_and_print, 10))
    thread.start()
    event.clear()

# Generated at 2022-06-14 13:50:00.619126
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:50:06.983189
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def test_print(text, wait):
        sleep(wait)
        tqdm_auto.write(text)
    mono = MonoWorker()
    mono.submit(test_print, '1', 0.5)
    mono.submit(test_print, '?', 0.3)
    mono.submit(test_print, '2', 0.5)
    mono.submit(test_print, '?', 0.2)
    mono.submit(test_print, '3', 1)
    sleep(1)
    tqdm_auto.write('Should only see "1", "2", "3" in that order.')

# Generated at 2022-06-14 13:50:16.985927
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from .nullcontext import nullcontext
    from .iterablecontext import iterablecontext
    from .import_meta import import_meta

    _BasicException = import_meta('BaseException')
    _Threading = import_meta('threading')

    def function(x):
        time.sleep(0.1)
        return sum(x)

    with nullcontext() as null, \
            iterablecontext(range(2)) as progress:
        progress.set_description('test_iterable')
        progress.set_postfix(arg=3)
        progress.set_postfix(arg=4)
        progress.set_description('test_iterable2')
        progress.clear()


# Generated at 2022-06-14 13:50:27.178713
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from contextlib import closing
    from time import sleep
    from random import random
    import re
    from . import _range
    from .tty import text_type

    # create worker
    worker = MonoWorker()
    with closing(worker):
        # submit function
        def func(x):
            ##for _ in _range(1, 30): # like range but works on python 2/3
            ##    sleep(0.01 * random())
            sleep(x * random() / 10)
            return x * 10

        # create tqdm to track work done

# Generated at 2022-06-14 13:51:07.107577
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event
    from .compatibility import text_type
    from .utils import ThreadWithExc

    def is_running(pool):
        for thread in pool._threads.values():
            if isinstance(thread, ThreadWithExc):
                if not thread.exc and thread.is_alive():
                    return True
        return False

    def sleep_no_print(x):
        sleep(x)

    def exc():
        raise ValueError("MonoWorker")

    def eta(x):
        sleep(x)
        if x == 1:
            raise ValueError("MonoWorker")

    mw = MonoWorker()
    assert not is_running(mw.pool)

    # 1st waiting task

# Generated at 2022-06-14 13:51:15.371198
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from tqdm.contrib.test_utils import StringIO
    from concurrent.futures import ThreadPoolExecutor

    mw = MonoWorker()

    # submit first task
    t0 = time.time()
    assert mw.submit(time.sleep, 0.05).result() is None
    assert time.time() - t0 > 0.05

    # submit second task right after first is done
    t0 = time.time()
    assert mw.submit(time.sleep, 0.05).result() is None
    assert time.time() - t0 > 0.05

    # submit third task before second is done
    t0 = time.time()
    assert mw.submit(time.sleep, 0.05).result() is None
    assert time.time() - t0 > 0.05

   

# Generated at 2022-06-14 13:51:26.777912
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from multiprocessing.pool import ApplyResult
    from ..utils import FormatCustomTextExt
    from ..utils import nullcontext as nullcontext_py
    from ..contrib.concurrency import _supports_sendfile

    tqdm_auto.write("Testing MonoWorker.submit()...")
    tqdm_auto.write("Testing when no exception raised...")
    mw = MonoWorker()

    def mock_submit(func, *args, **kwargs):
        mock_submit.counter += 1
        if mock_submit.counter == 1:
            return ApplyResult(None, 42)
        elif mock_submit.counter == 2:
            return ApplyResult(None, "sentinel")
        else:
            raise Exception("mock_submit() called too many times")

    mock_submit.counter = 0
    mw.pool

# Generated at 2022-06-14 13:51:37.457457
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Testing method submit() of class MonoWorker.
    """
    import time
    import unittest

    class TestCases(unittest.TestCase):
        def setUp(self):
            self.mw = MonoWorker()
        def test_submit(self):
            def foo(n):
                time.sleep(1)
                return n
            def bar(n):
                time.sleep(1)
                return n + 1
            f = self.mw.submit(foo, 1)
            self.assertEqual(f.result(), 1)
            f = self.mw.submit(bar, 2)
            self.assertEqual(f.result(), 3)  # bar replaces foo
            f = self.mw.submit(foo, 3)

# Generated at 2022-06-14 13:51:46.503966
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .utils import get_start_methods
    from ..utils import _environ_cols_wrapper
    from ..std import IterableMixin
    from ..std.monotonic import monotonic

    def worker(delay, task, i):
        with tqdm_auto.tqdm(desc=("task %d, " % i),
                            total=total, unit='B', unit_scale=True,
                            leave=False) as pbar:
            start_t = monotonic()
            sleep(delay)
            pbar.set_postfix(time=("%.1fs" % (monotonic() - start_t,)))
            print("\n", task.strip(), ("%d" % i), "finished\n", sep="")

    pool = MonoWorker()
    task

# Generated at 2022-06-14 13:51:52.463445
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    worker = MonoWorker()

    def print_func(x=None):
        time.sleep(.5)
        if x is not None:
            tqdm_auto.write(x)


    worker.submit(print_func, "1")
    worker.submit(print_func, "2")
    worker.submit(print_func, "3")
    worker.submit(print_func, "4")
    worker.submit(print_func, "5")
    worker.submit(print_func, "6")
    worker.submit(print_func, "7")
    worker.submit(print_func, "8")

if __name__ == "__main__":
    test_MonoWorker_submit()
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:52:03.323585
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    mw = MonoWorker()
    assert 0 < len(mw.futures) == mw.futures.maxlen
    mw.futures.clear()
    mw.submit(lambda: 1)
    assert 0 < len(mw.futures) == mw.futures.maxlen
    mw.futures.clear()
    mw.submit(lambda: 1)
    mw.submit(lambda: 1)
    assert 0 < len(mw.futures) == mw.futures.maxlen
    mw.futures.clear()
    mw.submit(lambda: 1)
    for _ in range(2):
        mw.submit(lambda: 1)

# Generated at 2022-06-14 13:52:11.088964
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import concurrent.futures
    import time
    import random
    import string
    import sys

    if sys.version[0] == '2':
        range = xrange

    def func_sleep(n):
        time.sleep(n)
        return n

    def func_exception():
        raise Exception('Something')

    def do_test(MonoWorker):
        mw = MonoWorker()

        # Submit 2 tasks
        future_sleep1 = mw.submit(func_sleep, 1.5)
        future_sleep0 = mw.submit(func_sleep, 0.5)
        assert isinstance(future_sleep0, concurrent.futures.Future)
        time.sleep(0.25)
        assert not future_sleep0.done()
        assert future_sleep1.done()
        assert future

# Generated at 2022-06-14 13:52:19.983775
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from unittest import TestCase

    class Test_MonoWorker_submit(TestCase):
        def test_submit(self):
            def call(t):
                sleep(t)
                return t
            mw = MonoWorker()
            p1 = mw.submit(call, 1)
            p2 = mw.submit(call, 2)
            p3 = mw.submit(call, 3)
            ans = [1, 3]
            for i, p in enumerate(ans):
                self.assertEqual(p, p3.result())
                self.assertEqual(p, p3.result())
                self.assertEqual(p, p3.result())
                self.assertEqual(p, p3.result())

# Generated at 2022-06-14 13:52:29.641685
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import math
    import traceback
    from concurrent.futures import Future

    def tprint(*args):
        print('{:5.3f}'.format(time.time()), '|', *args)

    def sleep(n):
        tprint('sleep', n)
        time.sleep(n)
        tprint('woke')

    def exception():
        raise RuntimeError('generate exception')

    def tqdm(*, desc, chunksize, total, unit='items'):
        tprint('tqdm', 'start')