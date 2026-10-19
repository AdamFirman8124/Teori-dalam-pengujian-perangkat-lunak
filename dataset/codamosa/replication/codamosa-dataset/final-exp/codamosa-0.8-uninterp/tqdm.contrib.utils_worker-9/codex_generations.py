

# Generated at 2022-06-14 13:42:42.475754
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    from threading import Lock

    class SlowThread:
        def __init__(self, n, delay=1):
            self.n = n
            self.delay = delay
            self.lock = Lock()
            self.calls = 0

        def run(self):
            with self.lock:
                self.calls += 1
            time.sleep(self.delay + random.random())
            return self.n

    cm = MonoWorker()
    st = SlowThread(3)
    st.delay = 1
    st.calls = 0
    cm.submit(st.run)
    time.sleep(0.5)
    assert st.calls == 1, "Test 1: wrong number of calls"
    time.sleep(0.5)
    cm.submit(st.run)


# Generated at 2022-06-14 13:42:51.040674
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randint
    from threading import Lock
    from itertools import count

    def dummy_future(sec, name=None):
        sleep(sec)
        global self
        with self.lock:
            if name:
                self.results.add(name)

    lock = Lock()
    self = {'lock': lock, 'results': set()}
    with tqdm_auto.trange(20) as t:
        for _ in t:
            MonoWorker().submit(dummy_future, randint(0, 1), str(next(count)))
            with lock:
                t.set_postfix(results=self['results'])

# Generated at 2022-06-14 13:43:00.903080
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def is_running():
        return len(futures) == 2 and not futures[0].done()

    def is_waiting():
        return len(futures) == 2 and not futures[1].done()

    def is_done():
        return len(futures) == 1 and futures[0].done()

    futures = worker.futures
    # Test: 2 simultaneously submitted tasks
    worker.submit(lambda: sleep(0) or 1)
    worker.submit(lambda: sleep(1) or 2)
    assert is_running() and is_waiting()
    # Test: replace waiting task with a new one
    worker.submit(lambda: sleep(0) or 3)
    assert is_running() and is_waiting()
    futures.pop().result()
    assert is_waiting() and is_done()

# Generated at 2022-06-14 13:43:12.155719
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import timeit

    def raise_(e=None):
        if e:
            raise e

    def f(x, y=1):
        return x + y

    mw = MonoWorker()

    assert mw.submit(f, 1, y=2).result() == 3
    assert mw.submit(f, 4, y=5).result() == 9

    start = timeit.default_timer()
    for i in range(3):
        try:
            mw.submit(raise_)
        except Exception:
            pass
    for i in range(3):
        try:
            mw.submit(raise_)
        except Exception as e:
            mw.submit(raise_, e)
    for i in range(3):
        mw.submit(f, i)

# Generated at 2022-06-14 13:43:22.666049
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from subprocess import Popen, PIPE

    def test_sleep(t):
        sleep(t)

    def test_ls_l(*args, **kwargs):
        with Popen(['ls', '-l'] + list(args), stdout=PIPE) as p:
            print(p.stdout.read().decode('utf-8'))

    # test sleeping
    mw = MonoWorker()
    mw.submit(test_sleep, 1)  # 1 sec
    mw.submit(test_sleep, 2)  # 2 sec
    mw.submit(test_sleep, 2)  # 2 sec
    mw.submit(test_sleep, 3)  # 3 sec
    mw.submit(test_sleep, 1)  # 1 sec

# Generated at 2022-06-14 13:43:29.158015
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import tqdm.contrib.testlab
    tlt = tqdm.contrib.testlab.Tlt()
    tlt.start_timer()
    mw = MonoWorker()
    mw.submit(time.sleep, 2)
    mw.submit(time.sleep, 2)
    mw.submit(time.sleep, 0.3)
    mw.submit(time.sleep, 2)
    assert tlt.stop_timer(3.3) < 1, str(tlt)
    tlt = tqdm.contrib.testlab.Tlt()
    tlt.start_timer()
    mw.submit(time.sleep, 3)
    assert tlt.stop_timer(3.3) < 1, str(tlt)
    tlt = tqdm.cont

# Generated at 2022-06-14 13:43:40.520289
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import threading, time
    import numpy as np
    num_threads = 2
    num_seconds = 2
    verbose = 0

    def wait():
        """Wait `num_seconds` seconds, then return its thread index."""
        time.sleep(num_seconds)
        return threading.current_thread().ident

    threads = [None] * num_threads
    with MonoWorker() as p:
        for i in range(num_threads):
            threads[i] = p.submit(wait)

    # Collect results
    for i, t in enumerate(threads):
        if t is None:
            continue
        if verbose:
            print("threads[{:d}]: {}".format(i, t))

# Generated at 2022-06-14 13:43:50.246856
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def check_call(i, expected_out, expected_err, out, err):
        assert out == expected_out, \
            "Expected out '{}' but got '{}'".format(expected_out, out)
        assert err == expected_err, \
            "Expected err '{}' but got '{}'".format(expected_err, err)

    tasks = [
        (1, '', '', ['1']),
        (2, '', '', ['2']),
        (3, '', '', ['3']),
        (4, '', '', ['4']),
        (5, '', '', ['5']),
        (6, '', '', ['6']),
    ]
    out = []
    err = []
    done = []


# Generated at 2022-06-14 13:43:59.340401
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test against:
    - running a newer task in place of an older waiting task
    - not running a newer task if older task is running
    """
    import time

    def test_func(*args):
        time.sleep(1)
        print(*args)
        return args[0]

    mono_worker = MonoWorker()

    for i in range(4):
        mono_worker.submit(test_func, i)
        time.sleep(0.7)

    time.sleep(1.3)
    for i in range(4, 7):
        mono_worker.submit(test_func, i)
        time.sleep(0.7)

    time.sleep(1.3)



# Generated at 2022-06-14 13:44:07.633759
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test the submit method of the MonoWorker class.
    """
    import time
    import random
    import threading
    import multiprocessing
    import itertools

    def _method_tester(method, max_=10, wait_=1):
        """
        Helper method for the test_MonoWorker_submit test
        """
        mw = MonoWorker()

        # Test that only two simulations are running simultaneously
        running = []
        sims = [
            mw.submit(
                method,
                idx,
                name='sim{}'.format(idx),
                random_wait=random.gauss(wait_, wait_ / 10)
            ) for idx in range(max_)
        ]

# Generated at 2022-06-14 13:44:19.890781
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from os import getpid
    from threading import Lock, Thread
    from unittest.case import TestCase
    from ..utils import ThreadPoolExecutor4Mockup

    pid_lock = Lock()
    pid = []

    def print_pid():
        """Print process ID and time and wait."""
        with pid_lock:
            pid.append(getpid())
        tqdm_auto.write(str(time.time()))
        time.sleep(1)

    class TestMonoWorker(TestCase):
        def setUp(self):
            self.m = MonoWorker()

        def test_one(self):
            # Test if only one subprocess is running at a time
            for _ in range(10):
                self.m.submit(print_pid)

# Generated at 2022-06-14 13:44:29.748172
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:44:33.095464
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    mw = MonoWorker()
    total = 0
    for k in range(5):
        sleep(0)
        total += mw.submit(sleep, 0.1).result()
    assert total == 0.5

# Generated at 2022-06-14 13:44:42.062095
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from time import time as now
    worker = MonoWorker()

    def func(x):
        sleep(x)
        return now() - int(x)
    #                             0.0 0.1 0.2 0.3 0.4
    results = [worker.submit(func, x) for x in range(5)]
    correct = [None, 1.0, 2.0, 3.0, 4.0]

    assert len(results) == 5
    for r, c in zip(results, correct):
        assert (r is None) == (c is None)
        if c is not None:
            assert c < r.result() < c + 1

# Generated at 2022-06-14 13:44:52.011081
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, queue
    import numpy as np

    def long_func(t):
        time.sleep(t)
        return time.time()

    def short_func(t):
        return t

    class FakeTqdm(object):
        def __init__(self):
            self.bar = queue.Queue()
        def write(self, s):
            self.bar.put(s)
    ftqdm = FakeTqdm()

    mw = MonoWorker()
    results = []

    def short_func_wrapper(t):
        t1 = mw.submit(short_func, t).result()
        results.append(t1)

    try:
        mw.submit(long_func, 1e-1).result()
    except Exception:
        raise Exception("test 1 failed!")
   

# Generated at 2022-06-14 13:44:59.372542
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from math import sqrt
    from random import randint
    from itertools import islice
    from operator import itemgetter

    mw = MonoWorker()
    mw.submit(sqrt, randint(0, 100000))
    for i in range(9):
        sleep(0.4)
        mw.submit(sqrt, randint(0, 100000))
    # mw.submit(sqrt, randint(0, 100000))
    # mw.submit(sqrt, randint(0, 100000))
    # mw.submit(sqrt, randint(0, 100000))
    # mw.submit(sqrt, randint(0, 100000))
    # mw.submit(sqrt, randint(0, 100000))
    # mw

# Generated at 2022-06-14 13:45:10.590519
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from os import environ
    from ..auto import tqdm as tqdm_auto_
    from ..utils import format_sizeof
    environ['COLUMNS'] = "80"  # needed for unit tests with shutil.get_terminal_size()
    tqdm_auto_.tqdm_cls.default = 'tqdm'
    tqdm_auto_.tqdm_cls.monitor_interval = 0  # needed for tqdm.test()
    tqdm_auto_.tqdm_cls.mininterval = 1e-6  # needed for tqdm.test()
    tqdm_auto_.tqdm_cls.miniters = 1  # needed for tqdm.test()
    tqdm_auto_.tqdm_cls.asci

# Generated at 2022-06-14 13:45:18.455634
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from time import time

    def f(a, b):
        return a + b

    m = MonoWorker()
    assert m.submit(f, 1, b=2).result() == 3
    assert m.submit(f, 3, b=4).result() == 7
    t1 = time()
    assert m.submit(sleep, 0.5, b=4).result() is None
    assert time() - t1 >= 0.5
    t2 = time()
    assert m.submit(sleep, 0.5, b=4).result() is None
    assert time() - t1 >= 0.5
    assert time() - t2 < 0.5

    def g():
        raise ValueError("a")

# Generated at 2022-06-14 13:45:29.736944
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .perf_monitor import sample_monitor
    from threading import Event
    import time

    def func_loop(evt):
        evt.wait()
        for _ in range(5):
            time.sleep(.2)

    def test(func):
        w = MonoWorker()
        e1 = Event()
        e2 = Event()
        f1 = w.submit(func, e1)
        assert f1 is not None
        f2 = w.submit(func, e2)
        assert f2 is not None

        e1.set()
        time.sleep(0.1)
        e2.set()
        f1.result()
        f2.result()

    with sample_monitor(test) as stats:
        assert stats.cpu_pct < 2


# Test the performance of class

# Generated at 2022-06-14 13:45:38.162990
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    from .monitor import NonBlockingStreamReader

    class NBSR(NonBlockingStreamReader):
        def __init__(self, *args, **kwargs):
            super(NBSR, self).__init__(*args, **kwargs)
            self.flushed = threading.Event()

        def flush(self):
            super(NBSR, self).flush()
            self.flushed.set()

    def func(x):
        time.sleep(x)
        return x

    worker = MonoWorker()
    # basic
    f = worker.submit(func, 1)
    assert f.result() == 1
    # replace waiting with running
    worker.submit(func, .5)
    worker.submit(func, .8)

# Generated at 2022-06-14 13:45:51.712879
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def test_f(args, kwds):
        tqdm_auto.write("Wait", args, kwds)
        from time import sleep
        sleep(0.5)
        tqdm_auto.write("Done", args, kwds)
        return args, kwds
    mono = MonoWorker()
    mono.submit(test_f, ("a",), dict(kw="a"))
    mono.submit(test_f, ("b",), dict(kw="b"))
    mono.submit(test_f, ("c",), dict(kw="c"))
    mono.submit(test_f, ("d",), dict(kw="d"))
    mono.submit(test_f, ("e",), dict(kw="e"))

# Generated at 2022-06-14 13:45:57.049878
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def f(x):
        time.sleep(x)
        return x

    mw = MonoWorker()
    # Submit 3 tasks in 1, 2, 3 seconds
    a = mw.submit(f, 1)
    b = mw.submit(f, 2)
    c = mw.submit(f, 3)
    assert a == c  # b was discarded, c is running

# Generated at 2022-06-14 13:46:07.701630
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    from ..utils import _term_move_up

    def task(i):
        time.sleep(random.randrange(0, 4))
        tqdm_auto.write("%s %s" % ("running" if i < 3 else "finished", i))

    workers = MonoWorker()
    for i in range(5):
        workers.submit(task, i)
    workers.pool.shutdown(wait=True)

    tqdm_auto.write("\n" + '-' * 80)
    tqdm_auto.write("\n" + "Testing cancel")
    tqdm_auto.write("\n" + '-' * 80)
    workers = MonoWorker()
    for i in range(5):
        workers.submit(task, i)

# Generated at 2022-06-14 13:46:18.124508
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    global running_name
    running_name = ""

    class Task(object):
        def __init__(self, name):
            self.name = name

        def __call__(self):
            global running_name
            running_name = self.name

# Generated at 2022-06-14 13:46:26.593247
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:46:36.792064
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Tests `MonoWorker.submit`."""
    import time
    from multiprocessing import Value
    from ..auto import trange

    def test_func(i, running, waiting, timeout):
        time.sleep(timeout)
        with running.get_lock():
            running.value += 1
        if timeout > 0:
            with waiting.get_lock():
                waiting.value += 1

    for i in trange(20, desc="test_MonoWorker", ncols=120):
        running = Value('i')
        waiting = Value('i')
        waiting.value = 0
        mw = MonoWorker()
        mw.submit(test_func, i, running, waiting, 0.5)
        mw.submit(test_func, i + 0.1, running, waiting, 0)


# Generated at 2022-06-14 13:46:46.137170
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    import time
    from threading import Thread
    mw = MonoWorker()
    assert mw.futures.maxlen == 2
    assert not mw.futures
    assert mw.submit(time.sleep, 2)
    assert len(mw.futures) == 1
    assert mw.submit(time.sleep, 2)
    assert len(mw.futures) == 2
    assert mw.submit(time.sleep, 2)
    assert len(mw.futures) == 2
    time.sleep(3)
    mw.futures.clear()


# Generated at 2022-06-14 13:46:52.992388
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    def foo():
        while threading.current_thread().is_alive():
            time.sleep(0.01)
    monoworker = MonoWorker()
    monoworker.submit(foo)
    time.sleep(0.1)
    assert len(monoworker.futures) == 1
    monoworker.submit(foo)
    time.sleep(0.1)
    assert len(monoworker.futures) == 1
    monoworker.futures[0].cancel()
    time.sleep(0.1)
    assert len(monoworker.futures) == 0
    monoworker.futures.append(monoworker.pool.submit(foo))
    time.sleep(0.1)

# Generated at 2022-06-14 13:47:03.324493
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import tempfile
    fname = tempfile.mktemp()
    with open(fname, "wt") as f:
        f.write("")

    def double_sleep():
        time.sleep(2)
        return 2

    def sleep_and_write():
        time.sleep(1)
        with open(fname, "rt") as f:
            val = int(f.read().strip())
        with open(fname, "wt") as f:
            f.write("{:d}".format(val * 2))
        return val

    # Test empty case
    mono = MonoWorker()
    time.sleep(.5)  # let time to flush thread
    assert mono.futures == deque([], maxlen=2)

    # Test one running, no waiting
    mono.submit

# Generated at 2022-06-14 13:47:09.257812
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event
    import random

    def task(n, pause=0.01, step=None):
        sleep(pause)
        if step:
            step.set()
        return n

    step = Event()
    worker = MonoWorker()
    for i in range(10):
        worker.submit(task, random.random(), step=step)
        step.wait()
        step.clear()

# Generated at 2022-06-14 13:47:19.080816
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # MonoWorker._submit_example_1
    import time
    f = MonoWorker()
    g = f.submit(time.sleep, 3)
    h = f.submit(time.sleep, 3)
    i = f.submit(time.sleep, 3)
    assert not g.done()
    assert h.done()
    assert i.done()
    g.result()

# Generated at 2022-06-14 13:47:27.965489
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    X = MonoWorker()
    assert X.pool._maximum_workers == 1
    assert X.futures.maxlen == 2
    assert not X.futures
    X.submit(time.sleep, 1)
    assert len(X.futures) == 1
    X.submit(time.sleep, 2)
    assert len(X.futures) == 2
    for future in X.futures:
        assert not future.done()
    X.submit(time.sleep, 3)
    assert len(X.futures) == 2
    for future in X.futures:
        assert not future.done()
        future.cancel()
    del X

# Generated at 2022-06-14 13:47:32.191804
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def dummy(*args, **kwargs):
        return (args, kwargs)

    mw = MonoWorker()
    assert mw.submit(dummy, 1, 2) == mw.submit(dummy, 3, 4)
    assert mw.submit(dummy, 5, 6) != mw.submit(dummy, 7, 8)



# Generated at 2022-06-14 13:47:43.162386
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def func_0():
        time.sleep(2)
        return 0

    def func_1():
        time.sleep(2)
        return 1

    def func_2():
        time.sleep(2)
        return 2

    def func_x():
        time.sleep(2)
        raise Exception

    m = MonoWorker()
    assert m.submit(func_0) == 0
    assert m.submit(func_1) == 1
    assert m.submit(func_2) == 0
    assert m.submit(func_x) is None
    assert m.submit(func_1) == 1
    assert m.submit(func_2) == 0



# Generated at 2022-06-14 13:47:48.647587
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    o = MonoWorker()
    results = []
    # Test that the first task is always running
    f1 = o.submit(time.sleep, 0.2)
    f2 = o.submit(results.append, 2)
    f3 = o.submit(results.append, 3)
    f3.result(timeout=0.1)


# Generated at 2022-06-14 13:47:57.047422
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from os import getpid

    def worker(name):
        sleep(1)
        return "worker{}".format(name), getpid()

    workers = MonoWorker()
    for i in tqdm_auto(range(5)):
        try:
            w = workers.submit(worker, i)
            print(w.result())
        except Exception as e:
            print('Got exception: {}'.format(e))


if __name__ == '__main__':
    test_worker = MonoWorker()

# Generated at 2022-06-14 13:48:07.762653
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test `MonoWorker` method `submit`.
    """
    import time

    def slow_square(x):
        """ [x] -> [x**2]"""
        time.sleep(1)
        return x ** 2

    import unittest
    import io
    import sys

    def capture_stdout():
        """ Helper function to capture stdout. """
        stdout_ = sys.stdout
        sys.stdout = io.StringIO()
        try:
            yield lambda: sys.stdout.getvalue()
        finally:
            sys.stdout = stdout_

    class MonoWorkerTests(unittest.TestCase):
        """ Tests for `MonoWorker` class. """

        def setUp(self):
            self.worker = MonoWorker()


# Generated at 2022-06-14 13:48:17.087432
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def _slow_adder(x, y):
        time.sleep(1)
        return x + y

    def _fast_adder(x, y):
        return x + y

    def _failing_adder(x, y):
        raise Exception("Failed to add")

    mw = MonoWorker()
    slow_future = mw.submit(_slow_adder, 3, 7)
    fast_future = mw.submit(_fast_adder, 2, 5)
    assert slow_future.running()
    assert fast_future.running()

    fast_future.result()
    assert slow_future.running()
    assert fast_future.done()
    assert not slow_future.done()

    slow_future.result()
    assert slow_future.done()

    # Try to submit task again

# Generated at 2022-06-14 13:48:23.129948
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    m = MonoWorker()
    res = []

    def work(n):
        time.sleep(random.random())
        res.append(n)
    m.submit(work, 1)
    m.submit(work, 2)
    m.submit(work, 3)
    list(tqdm_auto.tqdm(m.futures))
    assert res == [3], res

# Generated at 2022-06-14 13:48:28.439581
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(i):
        return i

    mw = MonoWorker()
    import time
    time.sleep(1)
    mw.submit(func, 1)
    time.sleep(1)
    mw.submit(func, 2)
    assert mw.futures[0].result() == 2

    time.sleep(1)



# Generated at 2022-06-14 13:48:44.475181
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    mw = MonoWorker()

    # Test simple submit
    f1 = mw.submit(print, "1")
    assert mw.futures[0] == f1
    assert f1.result() is None

    # Test if one job is already running, subsequent jobs are still submitted
    f2 = mw.submit(print, "2")
    assert mw.futures[0] == f2
    assert f2.result() is None

    # Test if two jobs are submitted, only the second is executed
    f3 = mw.submit(print, "3")
    assert mw.futures[0] == f3
    assert f3.result() is None

# Generated at 2022-06-14 13:48:53.266499
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from multiprocessing import Manager
    from time import sleep
    from random import randrange
    from contextlib import closing

    output = Manager().list()
    count = 3
    m = MonoWorker()

    def add(a, b):
        sleep(randrange(1, 10)*0.01)
        output.append(a + b)

    submit = m.submit
    submit(add, 1, 2)
    submit(add, 2, 3)
    submit(add, 3, 4)
    sleep(0.1)
    submit(add, 1, 5)
    sleep(0.1)
    submit(add, 1, 6)
    sleep(0.1)
    submit(add, 1, 7)
    sleep(0.1)


# Generated at 2022-06-14 13:49:00.923736
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import os
    import time
    import shutil
    import tempfile
    from concurrent.futures import ThreadPoolExecutor
    from concurrent.futures import as_completed
    from nose.tools import assert_equal

    from .utils import check_file_sanity

    # Prepare

# Generated at 2022-06-14 13:49:09.943930
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .common import skipIf
    from concurrent.futures import CancelledError
    from distutils.version import LooseVersion
    from sys import version_info
    from unittest import TestCase


# Generated at 2022-06-14 13:49:18.288672
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    def sleeper(x):
        sleep(x)
        return x

    # Test
    mw = MonoWorker()
    r0 = mw.submit(sleeper, 3)
    assert not r0.done()
    r0 = mw.submit(sleeper, 4)  # replaced
    assert not r0.done()
    r0.cancel()
    r0 = mw.submit(sleeper, 6)  # replaced
    assert not r0.done()
    r0.result()
    r1 = mw.submit(sleeper, 5)  # queued
    assert not r1.done()
    r0.result()
    assert r1.done()
    r1.result()

# Generated at 2022-06-14 13:49:29.693747
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Thread
    import sys
    from ..utils import format_sizeof

    def test():
        from ..utils import format_sizeof

        def func(task, sleep_factor):
            """do --stuff-- and print a nice progress bar"""
            #from ..utils import format_sizeof
            print('task {} started'.format(task))
            #from time import sleep
            sleep(1. / sleep_factor)
            size = 1024**2
            with tqdm_auto.tqdm(total=size, unit='B', unit_scale=True,
                                desc='task {}'.format(task)) as t:
                for i in range(size // 4):
                    # sleep(0.0001)
                    t.update(4)

# Generated at 2022-06-14 13:49:35.539746
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    # put imports here
    def f(x):
        time.sleep(1)
        return x

    mw = MonoWorker()
    f1 = mw.submit(f, 1)
    f2 = mw.submit(f, 2)
    f3 = mw.submit(f, 3)
    f4 = mw.submit(f, 4)
    print(f1.result(), f2.result(), f3.result(), f4.result())

# Generated at 2022-06-14 13:49:46.297593
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from ..utils import timeit
    from time import sleep
    from random import seed, uniform
    from tempfile import TemporaryFile

    seed(0)
    tqdm_auto.write("Sent + recv on same process", file=TemporaryFile())

    # Total processing time should be be: 10+10+5=25 sec
    # (1+2+2+5+0.5+5=15.5 sec processing time)
    # but sometimes fails on travis at 15.6 or 15.7 sec because
    # processing time is ~0.1 sec longer than expected
    # (e.g. 0.5 instead of 0.3 sec for first call to sleep)
    # (e.g. 0.012 instead of 0.0107 sec for tqdm_auto.write)


# Generated at 2022-06-14 13:49:54.607839
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Params:
        -n: number of tasks
        -s: sleep between tasks
        -f: fraction of tasks to fail (prints traceback)
        -b: blocking flag
    """
    import argparse
    import time

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num", type=int, default=10)
    parser.add_argument("-s", "--sleep", type=int, default=1)
    parser.add_argument("-f", "--fail", type=float, default=0.0)
    parser.add_argument("-b", "--blocking", action="store_true")
    args = parser.parse_args()

    pbar = tqdm_auto.tqdm(total=args.num)  # progress bar

    mw

# Generated at 2022-06-14 13:50:02.525258
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test that only two tasks are ever in the ThreadPoolExecutor at a time.
    """
    from queue import Queue
    from threading import Event, Lock
    from time import sleep
    from tqdm.contrib.concurrent import MonoWorker

    def wait(q: 'Queue' = None, e: 'Event' = None, l: 'Lock' = None):
        """
        Internal function used by the test.
        """
        if q is not None:
            q.put('start')
        if e is not None:
            e.wait()
        if l is not None:
            with l:
                pass
        sleep(0.5)

    q = Queue()
    e = Event()
    l = Lock()
    mw = MonoWorker()


# Generated at 2022-06-14 13:50:25.083053
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randint

    def myfunc(a, b, middle=0.1, sleep=sleep, randint=randint):
        sleep(middle)
        return a + b

    with MonoWorker() as worker:
        ff = [worker.submit(myfunc, 2, 2) for i in range(1, 4)]
        for f in ff:
            f.result()

# Generated at 2022-06-14 13:50:34.815749
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Run the following to test `MonoWorker.submit()`:

        python -m tqdm.contrib.threading\\
            test_MonoWorker_submit 0.3 0.3

    """
    def func(sec):
        from time import sleep
        from sys import stdout
        from ..std import time
        stdout.write('sleeping for %s s\n' % time(sec))
        stdout.flush()
        sleep(sec)
        stdout.write('woke up\n')
        stdout.flush()
        return sec

    import sys
    if len(sys.argv) <= 1:
        print('Usage: python -m tqdm.contrib.threading\\')
        print('    test_MonoWorker_submit 0.3 0.3')
        print()

# Generated at 2022-06-14 13:50:44.887004
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import unittest

    class TestSequenceFunctions(unittest.TestCase):
        def setUp(self):
            self.seq = list(range(10))

        def test_submit(self):
            mono_worker = MonoWorker()
            for x in self.seq:
                mono_worker.submit(time.sleep, float(x) / 10)
                mono_worker.submit(tqdm_auto.write, str(x))
            mono_worker.submit(tqdm_auto.write, str(len(self.seq)))

        def test_submit2(self):
            mono_worker = MonoWorker()
            for x in self.seq:
                mono_worker.submit(time.sleep, float(x) / 10)

# Generated at 2022-06-14 13:50:55.932881
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    worker = MonoWorker()

    def sleeper(x):
        time.sleep(x)
        return x

    start = time.time()
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)
    worker.submit(sleeper, 1)

# Generated at 2022-06-14 13:51:06.756982
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """test_MonoWorker_submit

    Test `MonoWorker` class through the method `submit`.

    Test that:

    - new tasks replace old waiting ones and not running ones
    - if mono-thread executor is full, then new tasks are queued
    """
    test_tasks = [tqdm_auto.tqdm(range(10), desc=str(i)) for i in
                  range(100, 0, -1)]

    def test_func(*args):
        res = []
        for task in test_tasks:
            res.append(next(task))
        return res

    mw = MonoWorker()
    for i in range(5):
        mw.submit(test_func, i)

    # Check that waiting and running tasks are always the last and the first

# Generated at 2022-06-14 13:51:15.116369
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import traceback
    from multiprocessing import Process, Value

    counter = Value('i', 0)

    def inc_counter_by(count):
        time.sleep(0.05)
        with counter.get_lock():
            counter.value += count

    def test_process():
        try:
            mow = MonoWorker()
            for i in range(10):
                if i % 3:
                    mow.submit(inc_counter_by, i)
                else:
                    mow.submit(time.sleep, 1)
                time.sleep(0.01)
        except Exception as e:
            traceback.print_exc()

    t = Process(target=test_process)
    t.start()
    t.join()
    assert len(mow.futures) == 0


# Generated at 2022-06-14 13:51:22.465415
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test `MonoWorker.submit`."""
    from time import sleep
    mw = MonoWorker()

    def single_producer(mw, it):
        """Produce values in `it` with constant flow."""
        for i in it:
            sleep(0.1)
            mw.submit(lambda i: i, i)

    def constant_consumer(mw):
        """Consume values with constant flow."""
        for i in tqdm_auto.trange(10):
            f = mw.submit(lambda: None)
            try:
                f.result()
            except Exception as e:
                tqdm_auto.write(str(e))

    from multiprocessing import Process
    p1 = Process(target=single_producer, args=(mw, range(10)))


# Generated at 2022-06-14 13:51:33.865687
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys
    import threading
    from multiprocessing import cpu_count
    if cpu_count() <= 1:
        return
    from tqdm import tqdm

    cached_stdout = sys.stdout
    try:
        from cStringIO import StringIO
    except ImportError:
        from io import StringIO
    sys.stdout = StringIO()

    def worker(t):
        time.sleep(t)
        return 42

    mw = MonoWorker()

    # test submit returns future
    assert mw.submit(worker, 4) is not None

    # test async execution
    futures = [mw.submit(worker, 4) for _ in range(2)]
    assert futures[0].done() is False
    assert futures[1].done() is True

# Generated at 2022-06-14 13:51:42.315096
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Event
    from unittest import TestCase

    class _TestCase(TestCase):
        def setUp(self):
            self.m = MonoWorker()
            self.e = Event()
            self.s = ""

        def assertIntermediate(self, expected):
            self.assertEqual(self.s, expected)

        def assertEnd(self, expected):
            self.assertEqual(self.s, expected)
            self.e.set()

        def assertEndAborted(self, expected):
            self.assertGreaterEqual(self.s, expected)
            self.e.set()

        def test_basic(self):
            self.m.submit(lambda: self.assertEnd("0"))
            self.e.wait()


# Generated at 2022-06-14 13:51:49.714276
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event
    from random import sample

    def sleep_random(i, t_max=1):
        sleep(t_max * sample([0.2, 0.4, 0.6, 0.8], 1)[0])
        return i


    def test_wait(worker, tasks):
        """Test that worker runs tasks in order"""
        print('[MonoWorker test_wait]')
        start_msg = '[MonoWorker test_wait] Start task {!r}'
        done_msg = '[MonoWorker test_wait] Done task {!r}'

        results = []
        i = 0
        for task in tasks:
            i += 1
            print(start_msg.format(i))
            future = worker.submit(task, i)
            results.append

# Generated at 2022-06-14 13:52:31.197845
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event
    from time import sleep
    from unittest import TestCase
    from unittest.mock import Mock

    e1 = Event()
    e2 = Event()
    e3 = Event()

    def wait_e1_and_set_e2():
        e1.wait()
        e2.set()

    def wait_e2_and_set_e3(sleep_time):
        sleep(sleep_time)
        e2.wait()
        e3.set()

    mw = MonoWorker()
    mw.pool.submit = Mock()

    # 1st submit -> should call submit(wait_e1_and_set_e2)
    mw.submit(wait_e1_and_set_e2)