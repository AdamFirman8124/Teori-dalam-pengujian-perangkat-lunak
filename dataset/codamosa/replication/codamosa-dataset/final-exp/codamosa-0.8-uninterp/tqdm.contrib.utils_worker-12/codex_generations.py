

# Generated at 2022-06-14 13:42:52.589273
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    info = []
    def f(x):
        info.append(x)
        return x
    mw = MonoWorker()
    mw.submit(f, 1)  # in-progress
    mw.submit(f, 2)  # queued
    mw.submit(f, 3)  # waiting + queued
    mw.submit(f, 4)  # queued
    # running :: in-progress
    assert (mw.futures[0].done() is False)
    assert info == [1]
    # waiting :: queued
    assert (mw.futures[1].done() is False)
    assert info == [1]
    # queued :: waiting + queued
    assert (mw.futures[2].done() is False)
    assert info == [1]


# Generated at 2022-06-14 13:42:59.171014
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import uniform
    from ..trange import tqdm
    def dummy_func(x):
        sleep(uniform(0, x))
        return (x if x < 5 else dummy_func(x - 5))
    with MonoWorker() as mono:
        tasks = [mono.submit(dummy_func, i) for i in range(10)]
        # waiting should always be the most recently submitted task
        for task in tqdm(tasks, dynamic_ncols=True):
            task.result()

# Generated at 2022-06-14 13:43:11.352276
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import string
    import sys
    import threading
    import concurrent.futures

    alphanum = string.ascii_letters + string.digits

    # make the worker, which will run functions (see below)
    worker = MonoWorker()

    # define functions
    def random_fail():
        if random.random() < 0.5:
            raise Exception('Failed randomly')
        else:
            print('succeeded')

    def random_time():
        time.sleep(random.random() + 0.5)

    def random_string():
        return ''.join(random.choice(alphanum) for _ in range(20))

    # run functions in main thread
    main_thread = threading.current_thread()

# Generated at 2022-06-14 13:43:18.234101
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Tests `tqdm.contrib.MonoWorker.submit`"""
    from tqdm._utils import _term_move_up
    from time import sleep
    from random import randint
    import sys
    import os

    N = 12
    M = 2
    sleeptime = 0.1

    # Clear output
    sys.stdout.write(_term_move_up() * (M + 1))
    sys.stdout.flush()

    # Initiate the `MonoWorker`
    mono_worker = MonoWorker()

    # Write lines to output
    for i in tqdm_auto.trange(N, desc='outer'):

        # Submit a new task
        task = mono_worker.submit(
            sleep,
            sleeptime * randint(1, 6))

        # Clear line

# Generated at 2022-06-14 13:43:27.278248
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from contextlib import contextmanager
    from functools import partial
    @contextmanager
    def context():
        tqdm_auto.write("before yield")
        yield
        tqdm_auto.write("before return")

    def func(arg):
        with context() as null:
            sleep(1)
        return arg

    with MonoWorker() as pool:
        pool.submit(partial(func, 0))
        pool.submit(partial(func, 1))
        sleep(1)

if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:43:38.459321
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Lock
    import gc

    class I(object):
        """
        Used to distinguish between object instances.
        """
        __slots__ = ('i',)

        def __init__(self, i):
            self.i = i

        def __repr__(self):
            return '{}_{}'.format(self.__class__.__name__, self.i)

    class F(object):
        """
        Used to test method submit of class MonoWorker.
        """
        __slots__ = ('i', 'l')

        def __init__(self):
            self.i = 0
            self.l = []
            self.lk = Lock()


# Generated at 2022-06-14 13:43:49.747908
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import format_sizeof

    def wait_and_return(x):
        time.sleep(x)
        return x

    def wait_sizeof_and_return(x, y):
        time.sleep(x)
        return format_sizeof(y)

    def job_sizeof_wait_and_return(x, y):
        time.sleep(x)
        return (format_sizeof(y), x)

    worker = MonoWorker()

    with tqdm_auto.tqdm() as t:
        f1 = worker.submit(wait_and_return, 2)
        f2 = worker.submit(wait_and_return, 3)
        f3 = worker.submit(wait_and_return, 4)
        t.update(f1.result())

# Generated at 2022-06-14 13:44:00.116108
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import ShortenTo as ST
    from .prange import prange
    from .test import pretest

    def func(n):
        print(ST(2)('func({}) started'.format(n)))
        time.sleep(1)
        print(ST(2)('func({}) ended'.format(n)))
        return

    pretest('MonoWorker')
    with MonoWorker() as mw:
        _ = prange(5, desc='prange', ncols=90, unit='arb')
        _ = mw.submit(func, _)
        time.sleep(2)  # wait 2 first jobs to finish
        _ = prange(5, desc='prange', ncols=90, unit='arb')
        _ = mw.submit(func, _)
        time

# Generated at 2022-06-14 13:44:07.989515
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def wait(i, secs=1):
        time.sleep(secs)
    from threading import Thread
    from queue import Queue
    T = Queue()
    def t(i, secs):
        wait(i, secs)
        T.put(i)
    mw = MonoWorker()
    T.put(0)
    for i in tqdm_auto.trange(10):
        # t(i, 0.1 * (1 + i % 10))
        Thread(target=t, args=(i, 0.1 * (1 + i % 10))).start()
        tqdm_auto.tqdm.write("{:.3f} {}".format(
            (i + 1) / 10, mw.submit(wait, i, 0)))

# Generated at 2022-06-14 13:44:16.094839
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import unittest

    # ===========================================================>
    class TestCase(unittest.TestCase):
        def slow_add(self, a, b):
            time.sleep(0.5)
            return a + b

        def test_async(self):
            tqdm_auto.write('test_async')
            worker = MonoWorker()

            future = worker.submit(self.slow_add, 1, 1)
            future = worker.submit(self.slow_add, 2, 2)
            time.sleep(0.2)
            future = worker.submit(self.slow_add, 3, 3)
            time.sleep(0.75)
            self.assertEqual(future.result(), 6)

# Generated at 2022-06-14 13:44:29.819918
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random
    from collections import namedtuple

    STATUS = namedtuple('STATUS', 'running waiting')

    def delayed_identity(x):
        sleep(random())
        return x

    def worker_func(worker, n, delay=.5):
        global status
        status = STATUS(True, False)
        f1 = worker.submit(delayed_identity, n)
        sleep(delay)
        status = STATUS(False, True)
        f2 = worker.submit(delayed_identity, n)
        status = STATUS(False, False)
        assert f1.result(timeout=0) == f2.result(timeout=0) == n


# Generated at 2022-06-14 13:44:40.459194
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from operator import mul
    from itertools import repeat

    # Test 1: if len(futures)==0
    mw = MonoWorker()
    assert mw.submit(mul, 2, 3).result() == 6
    assert not mw.futures

    # Test 2: if len(futures)==1
    mw = MonoWorker()
    mw.futures.append(mw.pool.submit(mul, 2, 3))
    assert mw.submit(mul, 2, 5).result() == 10
    assert mw.futures[0].result() == 6
    assert len(mw.futures) == 1

    # Test 3: if len(futures)==2
    mw = MonoWorker()

# Generated at 2022-06-14 13:44:50.800561
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test with some concurrent printing.
    """
    from time import sleep
    import os
    import sys
    import shutil
    sys.stdout.write("\x1b[?1049h")

    def print_delay(string, delay=0.5):
        sleep(delay)
        tqdm_auto.write(string)

    os.mkdir("test_MonoWorker_submit")

# Generated at 2022-06-14 13:44:58.542707
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Event

    class Foo(object):
        def __init__(self):
            self.prompt = Event()
            self.done = Event()
            self.count = 0

        def increment(self):
            self.prompt.wait()
            self.count += 1
            self.done.set()

    foo = Foo()
    worker = MonoWorker()
    f1 = worker.submit(foo.increment)
    f2 = worker.submit(foo.increment)
    foo.prompt.set()
    worker.submit(foo.increment)
    foo.done.wait()
    assert foo.count == 1
    f1.result()  # raises exception if cancelled
    time.sleep(1)
    assert foo.count == 1

# Generated at 2022-06-14 13:45:09.783165
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import sys

    def s(x):
        sleep(x)
        return x

    # Create a new MonoWorker instance
    t = MonoWorker()
    # Submit 3 tasks
    f1 = t.submit(s, 1)
    f2 = t.submit(s, 10)
    f3 = t.submit(s, 1)
    # f2 should have been discarded
    assert len(t.futures) == 2
    assert f1.done() is False
    assert f3.done() is False
    try:
        f2.done()
    except RuntimeError:
        pass
    else:
        sys.exit('AssertionError: f2 should not be done.')

    # Wait for task 3 to finish
    assert f3.result() == 1

# Generated at 2022-06-14 13:45:17.928273
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    worker = MonoWorker()

    # task
    def f():
        time.sleep(1)
        return 2

    # useless task
    def g():
        time.sleep(0.5)
        return 1

    # normal operation
    t = time.time()
    r = worker.submit(f)
    assert (r.result() == 2)
    assert (time.time() - t >= 1)

    # cancel ordered task
    t = time.time()
    r = worker.submit(f)
    assert (r.done() is False)
    r.cancel()
    assert (r.done() is True)
    assert (time.time() - t < 1)

    # cancel running task
    t = time.time()
    r = worker.submit(f)

# Generated at 2022-06-14 13:45:29.031812
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, sys
    if sys.version_info >= (3,):  # use first 0.5s in Python 3.x
        delay = 0.5
    else:  # use first 3s in Python 2.x
        delay = 3
    mw = MonoWorker()
    mw.submit(time.sleep, delay)
    assert mw.futures
    assert len(mw.futures) == 1
    time.sleep(delay)
    mw.submit(time.sleep, delay)
    assert len(mw.futures) == 1
    time.sleep(delay)
    assert mw.futures[0].done()
    mw.submit(time.sleep, delay)
    mw.submit(time.sleep, delay)
    mw.submit(time.sleep, delay)

# Generated at 2022-06-14 13:45:39.530815
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import pandas as pd
    from pandas.compat import range
    from .tqdm import tqdm

    def num_even(k):
        return sum([x % 2 == 0 for x in range(k)])

    # Worker with 2 tasks limit:
    wrk = MonoWorker()

    # Deque with length 2, append right
    dq = deque([], 2)
    dq.appendleft(1)  # [1]
    dq.append(2)  # [1, 2]
    dq.append(3)  # [2, 3]
    assert dq == deque([2, 3])

    # Submission of task in 4 processes:
    ds = pd.Series(range(4))
    for i in ds:
        ds.loc[i] = wrk

# Generated at 2022-06-14 13:45:51.665629
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ..utils import format_sizeof
    from ..utils import terminal_size as _ts
    from ..utils import _environ_cols_wrapper
    with _environ_cols_wrapper():
        wcols, _ = _ts()
        fout = open('/dev/tty', 'a')
    worker = MonoWorker()

    print('\n' * 3)  # let terminal scroll
    print('Start submitting...')

    def func1():
        sleep(3)

    def func2(i, j):
        sleep(1)
        return i * j

    worker.submit(func1)
    i = 1e8

# Generated at 2022-06-14 13:46:01.166253
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    mw = MonoWorker()

    # Random function that should be submitted
    def func(str):
        time.sleep(1)
        return random.random()

    # This list is used to test the behaviour of MonoWorker
    str_list = ["test1", "test2", "test3", "test4", "test5"]

    # Create a tqdm instance to iterate through the list
    for i in tqdm_auto.tqdm(range(10)):
        str = random.choice(str_list)
        res = mw.submit(func, str)
        if not res.done():
            tqdm_auto.write(str + " has been submitted")
        random.choice(str_list)  # Choose a random element
    mw.pool.shutdown()

# Generated at 2022-06-14 13:46:14.937384
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Create MonoWorker with one worker and a maximum of two tasks
    worker = MonoWorker()
    assert len(worker.futures) == 0
    # Test MonoWorker.submit
    assert worker.submit(lambda: None)
    assert isinstance(worker.futures[0], type(worker.submit(lambda: None)))
    assert len(worker.futures) == 1
    assert worker.submit(lambda: None)
    assert len(worker.futures) == 2

# Generated at 2022-06-14 13:46:24.044079
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import multiprocessing

    def random_sleep():
        """Dummy function to randomize minimum wait time of each task."""
        time.sleep(0.01 * random.random())

    def print_values(*args):
        """Print values and wait for values to be printed."""
        for arg in args:
            tqdm_auto.write("arg = %s" % arg)
        time.sleep(0.5)

    max_workers = multiprocessing.cpu_count()  # must be 1 for this test
    worker = MonoWorker(max_workers=max_workers)

    args_list = [1, 2, 3]
    for i, arg in enumerate(args_list):
        worker.submit(print_values, arg)
        random_sleep()
        # Must see

# Generated at 2022-06-14 13:46:33.023249
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:46:42.845699
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    def f(x):
        tqdm_auto.write("f {} sleeping".format(x))
        time.sleep(2)
        return x

    def g(x):
        tqdm_auto.write("g {} sleeping".format(x))
        time.sleep(1)
        raise Exception("exception for g {}".format(x))

    mw = MonoWorker()
    threads = [
        threading.Thread(
            target=lambda f=i: mw.submit(f, i)) for i in range(3)]
    threads2 = [
        threading.Thread(
            target=lambda f=i: mw.submit(g, i)) for i in range(3)]
    for t in threads + threads2:
        t.start()

# Generated at 2022-06-14 13:46:50.559340
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    import time

    class Future(object):
        "Simplified future. Doesn't support cancel()."
        def __init__(self, result):
            self._result = result
        def result(self):
            return self._result

    def execute(func, *args, **kwds):
        return Future(func(*args, **kwds))

    def f(i, s):
        sys.stdout.write('f({}, {})\n'.format(i, s))
        time.sleep(1)
        return i

    mw = MonoWorker()
    mw.pool.submit = execute
    assert mw.submit(f, 1, 'a')
    time.sleep(0.2)  # "running" f(1, 'a')
    # f(1, a) is running

# Generated at 2022-06-14 13:47:01.892683
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    tqdm_auto.write("Simple tests")

    mono_worker = MonoWorker()
    l1 = mono_worker.submit(lambda x: x, 1)
    time.sleep(1)
    assert l1.result() == 1
    time.sleep(2)
    l2 = mono_worker.submit(lambda x: x, 2)
    time.sleep(1)
    assert l2.result() == 2
    time.sleep(2)
    l3 = mono_worker.submit(lambda x: x, 3)
    time.sleep(1)
    assert l3.result() == 3
    time.sleep(2)
    l4 = mono_worker.submit(lambda x: x, 4)
    time.sleep(1)
    assert l4.result() == 4

# Generated at 2022-06-14 13:47:10.377085
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    assert all(not f.done() for f in mw.futures)
    waiting = mw.submit(time.sleep, 1)
    assert not waiting.done()  # shouldn't be done yet
    assert waiting == mw.futures[0]  # should be the first of the two
    running = mw.submit(time.sleep, 2)
    assert not running.done()  # shouldn't be done yet
    assert len(mw.futures) == 1  # should have erased the currently waiting
    assert running == mw.futures[0]  # should be the first of the two
    time.sleep(1.1)  # while running is sleeping
    assert running.done()

# Generated at 2022-06-14 13:47:21.768212
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import threading
    import collections
    import contextlib

    # Circular buffer with maxlen
    class CBuffer(deque):
        def __init__(self, iterable=(), maxlen=None):
            super(CBuffer, self).__init__(iterable, maxlen)

        def __getitem__(self, index):
            return super(CBuffer, self).__getitem__(index)

        def __setitem__(self, index, value):
            return super(CBuffer, self).__setitem__(index, value)

        def __len__(self):
            return super(CBuffer, self).__len__()

        def __delitem__(self, i):
            return super(CBuffer, self).__delitem__(i)


# Generated at 2022-06-14 13:47:30.540277
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import multiprocessing as mp
    mw = MonoWorker()
    mw.submit(mp.cpu_count)
    mw.submit(mp.cpu_count)
    mw.submit(mp.cpu_count)
    result_1, result_2, result_3 = (0, 0, 0)
    for f in mw.futures:
        try:
            result_1 += f.result()
        except:
            pass
    assert result_1 > 0
    mw.submit(mp.cpu_count)
    mw.submit(mp.cpu_count)
    mw.submit(mp.cpu_count)
    for f in mw.futures:
        try:
            result_2 += f.result()
        except:
            pass
    assert result_2 > result_

# Generated at 2022-06-14 13:47:40.283334
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import new_screen_length

    work = MonoWorker()
    with new_screen_length(30):
        print()
        with tqdm_auto.tqdm(total=3) as t:
            time.sleep(0.1)
            t.update()
            work.submit(time.sleep, 0.2)
            work.submit(time.sleep, 0.3)
            work.submit(time.sleep, 0.4)
            t.update()
            time.sleep(0.6)
            t.update()
    time.sleep(0.2)
    print()

# Generated at 2022-06-14 13:47:53.138073
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def my_func(x):
        return x

    worker = MonoWorker()
    for x in range(4):
        worker.submit(my_func, x)

    assert [my_func(x) for x in range(4)] == \
        [f.result() for f in worker.futures]

# Generated at 2022-06-14 13:47:59.308611
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    mw = MonoWorker()
    results = []

    def add_result(result):
        results.append(result)

    for _ in range(100):
        mw.submit(random.randint, 0, 100)
        time.sleep(0.1)

    assert all(x == results[0] for x in results), 'Results: {}'.format(results)

# Generated at 2022-06-14 13:48:03.807839
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event

    def print_num(num):
        print(num)
        sleep(0.5)

    with MonoWorker() as w:
        w.submit(print_num, 1)
        w.submit(print_num, 2)  # ignored
        e = Event()
        e.wait(1)

# Generated at 2022-06-14 13:48:13.600549
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import concurrent.futures
    from contextlib import redirect_stdout
    from io import StringIO
    from time import sleep
    from threading import Lock
    from queue import Queue
    from unittest.case import TestCase

    class TestMonoWorker(TestCase):
        def test(self):
            f = MonoWorker()
            execute_queue = Queue()
            result_queue = Queue()
            ready_flag = Lock()

            def execute():
                while True:
                    waiting, *params = execute_queue.get()
                    waiting.set(True)
                    ready_flag.acquire()
                    while not ready_flag.locked():
                        ready_flag.acquire()
                    result_queue.put(waiting.flag)
                    if params:
                        result_queue.put(f.submit(*params))

# Generated at 2022-06-14 13:48:14.638994
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # TODO: implement
    pass


# Generated at 2022-06-14 13:48:19.475481
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random

    def wait_rand():
        sleep(random() * 2)
        return random()

    mw = MonoWorker()
    results = []
    for i in range(10):
        results.append(mw.submit(wait_rand))
        sleep(random() / 2)
    for result in results:
        print(result.result())

if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:48:26.711877
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def f(x):
        """
        f(x) returns 2 if x is 2.
        """
        if x == 2:
            return 2
        raise ValueError('f(x) = x for x <> 2, not %s.' % (x,))

    from time import sleep
    m = MonoWorker()
    for x in tqdm_auto.trange(4):
        for i in [x, x]:
            assert m.submit(f, x).result() == 2
            sleep(1)
        sleep(0.5)

# Generated at 2022-06-14 13:48:30.768926
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def slow(n):
        time.sleep(n / 10)
        return 2 * n

    mono = MonoWorker()

    for i in range(5):
        mono.submit(slow, i)

    import gc
    gc.collect()  # TODO: sometimes this test fails due to memory issues

    assert [i.result() for i in mono.futures] == [8, 10]

# Generated at 2022-06-14 13:48:39.269279
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from contextlib import contextmanager
    from tempfile import NamedTemporaryFile

    @contextmanager
    def _dummy_source(n_lines, sleep_time=0.01):
        content = 'test\n'
        with NamedTemporaryFile() as f:
            for _ in range(n_lines):
                f.write(content)
            f.flush()
            sleep(sleep_time)
            i = 0
            while True:
                sleep(sleep_time)
                with open(f.name) as f:
                    yield i, f.read()
                i += 1

    @contextmanager
    def _dummy_func(source):
        with source as data:
            for i, text in data:
                yield i, text


# Generated at 2022-06-14 13:48:48.941100
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from unittest import TestCase
    from unittest import main

    class TestMonoWorker(TestCase):

        def test_submit(self):
            MAX_WAITING = 10
            MUTE = False  # if True, don't print result

            def t_worker(msg, t):
                time.sleep(t)
                return ("{} submitted {} got result {}"
                        " after {} seconds"
                        .format(self, msg, t, t))

            with MonoWorker() as w:
                fut2 = w.submit(t_worker, "A", t=2)
                fut3 = w.submit(t_worker, "B", t=3)
                fut4 = w.submit(t_worker, "C", t=4)

# Generated at 2022-06-14 13:49:11.865235
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def f(i):
        time.sleep(0.1)
        return i

    m = MonoWorker()
    futures = [m.submit(f, i) for i in range(8)]

    ret = [f.result() for f in futures]
    print('\n', futures)
    print(ret)


if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:49:20.072486
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Semaphore
    from collections import Counter

    n0, n1 = 0, 0
    nonlocal_args = (n0, n1)
    # threading.local() methods N/A to function inside `submit`:
    def worker0(n0, n1):
        """Increment `n0` atomically."""
        sleep(1)
        n0 += 1  # pylint: disable=W0201

    def worker1(n0, n1):
        """Increment `n1` atomically."""
        sleep(1)
        n1 += 1  # pylint: disable=W0201

    sync = Semaphore(value=0)

    mw = MonoWorker()


# Generated at 2022-06-14 13:49:27.093250
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from contextlib import closing
    with closing(MonoWorker()) as w:
        with tqdm_auto.tqdm(leave=True) as t:
            for i in tqdm_auto.trange(1, 10):
                tqdm_auto.write("submitting step #{}".format(i))
                w.submit(time.sleep, 2)
                t.update(1)
        assert len(w.futures) == 1

# Generated at 2022-06-14 13:49:37.582570
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    import signal

    signal.signal(signal.SIGALRM, lambda sig, frame: None)
    signaler = threading.Thread(
        target=lambda: [time.sleep(s) or signal.alarm(s)
                        for s in [.5, 2, .1]])
    signaler.daemon = True
    signaler.start()
    tqdm_auto.write('Expect [starting task 1, starting task 2]')
    mw = MonoWorker()
    futures = [
        mw.submit(_task, 1),
        mw.submit(_task, 2),
    ]
    time.sleep(.1)
    # task 1 should be running since task 2 replaced task 1

# Generated at 2022-06-14 13:49:44.501302
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def f(i):
        sleep(i)
        return i

    w = MonoWorker()
    for i in tqdm_auto.tqdm([0., .1, 1., .2, .3, 2., 3., 4., 5., 6., 7.]):
        w.submit(f, i)
    w.pool.shutdown()


if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:49:52.507656
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def _sleep(n=0, i=0):
        time.sleep(n)
        return i

    m = MonoWorker()
    _ = m.submit(_sleep, 0.1, i=0)
    _ = m.submit(_sleep, 0.2, i=1)
    assert 1 == m.futures[0].result()  # Discard old
    _ = m.submit(_sleep, 0.1, i=2)
    _ = m.submit(_sleep, 0.2, i=3)
    assert 2 == m.futures[0].result()  # Discard old
    assert 3 == m.futures[0].result()  # Discard old

# Generated at 2022-06-14 13:49:59.498671
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    from concurrent.futures import FIRST_COMPLETED

    iterator = [1, 2, 3, 4, 5, 6]
    lock = threading.Lock()

    def work(index):
        time.sleep(0.2)
        with lock:
            print("Doing work on {}".format(index))

    def submit(thread):
        print("Started thread {}".format(thread))
        worker.submit(work, thread)

    worker = MonoWorker()

    threads = [threading.Thread(target=submit, args=(i,))
               for i in range(1, 5)]
    for thread in threads:
        thread.start()

    # Wait on the first two running threads to complete.

# Generated at 2022-06-14 13:50:07.330046
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import format_sizeof

    # Test MonoWorker:
    from .utils import MonoWorker
    from .tqdm_printer import tqdm
    from .utils import (average_dicts, merge_dicts,
                        get_total_seconds, format_dicts)

    # Benchmark settings
    total = 100000  # total number of tasks
    # total = 2  # total number of tasks
    chunk = 100  # size of chunks to process
    # chunk = 2  # size of chunks to process
    timeout = 3 * 60 * 60  # max running time
    desc = "Benchmark: "

    mw = MonoWorker()

    # Create tasks
    task_kwargs = []
    expected_kwargs = {}

# Generated at 2022-06-14 13:50:14.518445
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    worker = MonoWorker()
    futures = []

    def dummy(x):
        import time
        import random
        time.sleep(random.random())
        return x

    def output(x):
        tqdm_auto.write(str(x))

    futures.append(worker.submit(dummy, 0))
    for x in range(1, 9):
        time.sleep(1)
        futures.append(worker.submit(dummy, x))
    for f in futures:
        f.add_done_callback(output)
    worker.pool.shutdown(wait=True)


# Generated at 2022-06-14 13:50:22.663366
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from os import path
    from subprocess import PIPE, Popen

    key = str(hash(__name__))
    tmp = "/tmp/{}.tmp".format(key)
    if path.isfile(tmp):
        raise IOError("temporary test file `{}` exists".format(tmp))

# Generated at 2022-06-14 13:51:08.644267
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    class TimeoutError(Exception):
        pass


# Generated at 2022-06-14 13:51:18.907516
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .monitor import inotify_poll

    m = MonoWorker()
    f = [None]
    for i in tqdm_auto.trange(4):
        f[0] = m.submit(inotify_poll, i)
        sleep(0.1)
        print("->", f[0].result())

    # Make sure we waited for the last one
    f[0].result()


if __name__ == '__main__':
    from .monitor import inotify_poll

    print("Testing MonoWorker")
    test_MonoWorker_submit()

    print("Testing inotify_poll")
    with tqdm_auto.tqdm() as t:
        for _ in inotify_poll("/tmp/dir", t):
            inotify_

# Generated at 2022-06-14 13:51:27.126019
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from random import shuffle
    from time import sleep
    from unittest import TestCase, main

    class TestMonoWorkerSubmit(TestCase):
        def test_submit(self):
            worker = MonoWorker()
            nums = list(range(10))
            shuffle(nums)
            for i in tqdm_auto.tqdm(nums):
                worker.submit(sleep, i / 100)
            sleep(0.5)  # ensure all finished

    main(module="test_MonoWorker_submit", verbosity=2, exit=False)

# Generated at 2022-06-14 13:51:37.780765
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    mw = MonoWorker()
    assert len(mw.futures) == 0

    def my_func(my_arg, my_kwarg=0):
        sleep(my_kwarg)
        return my_arg

    f1 = mw.submit(my_func, 1, 2)
    f2 = mw.submit(my_func, 2, 3)
    f3 = mw.submit(my_func, 3, 4)
    assert f1.done()
    assert not f2.done()
    assert not f3.done()

    assert len(mw.futures) == 1
    assert mw.futures[0] == f2

    mw.futures.clear()
    assert len(mw.futures) == 0

# Generated at 2022-06-14 13:51:46.573592
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import string
    def random_string(length=10):
        """Generate a random string of fixed length.
        Source: https://pythonspot.com/generate-a-random-string/"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    worker = MonoWorker()
    running_future = worker.submit(random_string, 5)

    # Test unique arguments
    assert running_future.result() == worker.submit(random_string, 5).result()

    # Test Future insertion
    for _ in range(deque.maxlen + 1):
        worker.submit(random_string, 5)

    assert len(worker.futures) == deque.maxlen

# Generated at 2022-06-14 13:51:50.552377
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys

    def slow_square(_, x):
        time.sleep(x)
        return x ** 2

    N = 10

    mw = MonoWorker()
    for n in range(N):
        mw.submit(slow_square, x=n)

        if n < N // 2:
            assert 2 == len(mw.futures)
        else:
            assert 1 == len(mw.futures)

# Generated at 2022-06-14 13:51:56.578305
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .utils import CustomSleep

    # Define and submit
    def do_task(n, sleep_func=sleep, delay=5.0, prefix='#'):
        print(prefix + 'Task', n, 'started')
        for i in tqdm_auto.tqdm(iterable=range(10), total=10):
            sleep_func(delay / 10)
        print(prefix + 'Task', n, 'finished')
        return '{}Task {} finished'.format(prefix, n)


# Generated at 2022-06-14 13:52:06.578408
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    import time
    import random

    def foo(x):
        time.sleep(random.uniform(0.001, 0.01))

    def bar(x):
        time.sleep(random.uniform(0.001, 0.1))

    mw = MonoWorker()
    for _ in range(10):
        mw.submit(foo, _)
    for _ in range(10):
        mw.submit(bar, _)

    time.sleep(0.1)

    with tqdm_auto.tqdm(total=15) as t:
        for _ in range(10):
            t.update(1)
            mw.submit(foo, _)
        for _ in range(10):
            t.update(1)
            mw.submit(bar, _)

    time.sleep

# Generated at 2022-06-14 13:52:07.214512
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import time
    import threading



# Generated at 2022-06-14 13:52:11.296011
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from os import getpid
    from random import random

    def func(ipid, n):
        # print("func %s %s" % (ipid, n))
        sleep(random())
        return (getpid(), ipid, n)

    mw = MonoWorker()

    res = []
    r = [mw.submit(func, getpid(), i) for i in range(10)]
    for i, f in enumerate(r):
        f.add_done_callback(lambda f, i=i: res.append((i, f.result())))
    print(repr(res))

    res = []
    r = [mw.submit(func, getpid(), i) for i in range(2)]
    for i, f in enumerate(r):
        f.add_done