

# Generated at 2022-06-14 13:42:50.400476
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from collections import deque
    from threading import Event
    from tqdm.contrib import MonoWorker

    def f(x, completed=None):
        time.sleep(0.1)
        # print('f({})'.format(x))
        if completed is not None:
            completed.set()
        return x * x

    for _ in range(2):
        # Test length
        completeds = deque([Event() for _ in range(3)], 3)
        worker = MonoWorker()

        # Test multi-threading
        results = deque(
            worker.submit(f, x, completed).result()
            for x, completed in enumerate(completeds))

        # Test serial
        results.append(worker.submit(f, 8).result())

        # Test execution order
        results

# Generated at 2022-06-14 13:43:00.544425
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import Manager, Process
    from threading import Thread
    import os
    import sys

    # Manager is needed for python 2.7/3.2
    p = Process(target=Manager().list)
    p.start()

    def f(x):
        """
        Try to run twice to test for forked processes
        """
        sleep(0.01 + x)
        if os.name == "nt":  # i.e. Python 2.7/3.2.2/3.2.3 (which are broken)
            sys.__stdout__.write("y")
        else:
            # STDERR output will cause Python 3.2.2 to fail on Windows
            print(x)  # , file=sys.__stderr__)
        return x

    m = Mono

# Generated at 2022-06-14 13:43:11.849835
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from concurrent.futures import CancelledError
    from time import sleep

    class TestTask(object):
        def __init__(self, worker, t, _id):
            self.worker = worker
            self.t = t
            self.id = _id
            self.alive = False
            self.task = None

        def start(self):
            self.alive = True
            self.task = self.worker.submit(self.run)

        def run(self):
            sleep(self.t)
            try:
                self.alive = False
            except Exception as e:
                tqdm_auto.write(str(e))

    # init
    worker = MonoWorker()
    tasks = [TestTask(worker, i % 3, i) for i in range(10)]
    # start

# Generated at 2022-06-14 13:43:22.583158
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from io import StringIO

    me = MonoWorker()
    stdout = StringIO()
    tqdm_auto.write = stdout.write
    job = me.submit(time.sleep, .5)

    # Allow for cancelling to work (due to threading)
    time.sleep(.1)

    assert stdout.getvalue() == ''
    assert not job.done()

    job = me.submit(time.sleep, .5)
    assert job.done()
    assert stdout.getvalue() != ''
    errmsg = stdout.getvalue()
    assert 'Cancelled' in errmsg or 'Canceled' in errmsg or 'Cancled' in errmsg
    assert 'B' not in errmsg
    stdout.truncate(0)


# Generated at 2022-06-14 13:43:30.229045
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def func(*args, **kwargs):
        time.sleep(1)
        return args[0]

    def assert_order(*args, **kwargs):
        assert len(args) == 1
        return args[0]

    mw = MonoWorker()

    assert mw.submit(func, 0) == 0
    assert mw.submit(func, 1) == None
    assert mw.submit(func, 2) == None
    assert mw.submit(func, 3).result() == 0
    assert mw.submit(func, 4) == None
    assert mw.submit(func, 5).result() is None

# Generated at 2022-06-14 13:43:41.562526
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    from concurrent.futures import Future
    from contextlib import contextmanager

    class FutureMock(object):
        def __init__(self):
            self.done = False
            self.cancelled = False

        def set_running_or_notify_cancel(self):
            self.done = False
            self.cancelled = False

        def set_result(self, result):
            self.done = True
            self.cancelled = False

        def set_exception(self, exception):
            self.done = True
            self.cancelled = False

        def cancel(self):
            self.cancelled = True
            self.done = False

        @contextmanager
        def __call__(self, *args, **kwargs):
            self.set_running

# Generated at 2022-06-14 13:43:51.049235
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .utils import get_time
    from time import sleep
    from os import getpid
    from collections import deque
    from concurrent.futures import as_completed
    import traceback

    class TestFunc(object):
        def __init__(self):
            self.results = deque([], 2)
        def __call__(self, args):
            self.results.append((
                get_time() - args[0],  # diff tstamps
                getpid(),  # diff pids
                args[1],  # test input value
            ))
            sleep(0.1)  # test "delays"

    test_func = TestFunc()
    mono_worker = MonoWorker()

    # submit 10 jobs to 2 slots
    tstamp = get_time()

# Generated at 2022-06-14 13:44:00.853181
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    '''
    Simple tests of MonoWorker#submit.
    '''
    import time
    import sys
    import threading

    def _(n, bar=True):
        """return number of secs to sleep and function to use a tqdm bar"""
        if bar:
            pbar = tqdm_auto.tqdm(total=n, desc=str(n))
            def closure():
                for i in range(n):
                    time.sleep(1)
                    pbar.update()
        else:
            time.sleep(n)
            def closure():
                pass
        # time.sleep(n)
        return n, closure

    def submit(func, *args, **kwargs):
        """non-blocking `MonoWorker.submit` with tqdm pre-/post-hooks"""
        p

# Generated at 2022-06-14 13:44:08.655116
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import concurrent.futures
    import time
    import sys
    try:
        tqdm_auto.write = sys.stdout.write
    except AttributeError:  # pragma: no cover
        tqdm_auto.write = sys.stdout.buffer.write
    submitter = MonoWorker()

    def spam(sleep=0):
        time.sleep(sleep)
        tqdm_auto.write(str(sleep))
        return sleep

    def test(args):
        # tqdm_auto.write(str(args))
        submitter.submit(spam, *args)
        time.sleep(0.5)

# Generated at 2022-06-14 13:44:17.130642
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import tqdm
    from .recursion_wrapper import recursion_wrapper

    class _TestException(Exception):
        pass

    @recursion_wrapper()
    def _recursion_wrapper_test_func1(n):
        time.sleep(1)
        if n:
            _recursion_wrapper_test_func1(n - 1)

    # just sleep
    def _test_func1(n):
        time.sleep(1)

    # just raise
    def _test_func_raise(_):
        raise _TestException()

    # just wait
    def _test_func_wait(_):
        time.sleep(2)  # will be cancelled

    with tqdm.external_write_mode() as tqdm_auto:
        mono_worker = MonoWorker()

# Generated at 2022-06-14 13:44:22.241538
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    worker = MonoWorker()

    def dummy(i):
        time.sleep(1)
        return i

    for i in range(4):
        worker.submit(dummy, i)
        time.sleep(0.5)
        print(i)

# Example of method submit of class MonoWorker

# Generated at 2022-06-14 13:44:31.383146
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:44:37.603776
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    mono = MonoWorker()
    t1 = mono.submit(time.sleep, 2)
    t1.result()

    t2 = mono.submit(time.sleep, 3)
    t2.result()

    t3 = mono.submit(time.sleep, 1)
    t3.result()
    assert t1.cancelled()
    assert not t2.cancelled()


# Generated at 2022-06-14 13:44:48.073224
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test:
        submit of class MonoWorker
    """
    import time
    import functools

    def wait(delay):
        """
        sleep for a while and return current time
        """
        time.sleep(delay)  # "work"
        return time.time()  # result

    # Now test

    mw = MonoWorker()

    # Empty
    assert not mw.futures

    # Single submit
    start = time.time()
    mw.submit(wait, 0.5)
    assert len(mw.futures) == 1
    assert not mw.futures[0].done()
    time.sleep(0.6)
    assert mw.futures[0].done()
    end = time.time()

# Generated at 2022-06-14 13:44:57.939536
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from multiprocessing.dummy import Pool as ThreadPool

    def waiting_func(arg):
        time.sleep(1)
        return arg

    pool = MonoWorker()

    t0 = time.time()
    pool.submit(waiting_func, 0)
    pool.submit(waiting_func, 1)
    pool.submit(waiting_func, 2)
    pool.submit(waiting_func, 3)
    assert time.time() - t0 < 2  # Last waiting_func should be cancelled

    pool.submit(waiting_func, 0)
    t0 = time.time()
    pool.submit(waiting_func, 0)
    assert time.time() - t0 > 0.9  # Last waiting_func should not be cancelled


# Generated at 2022-06-14 13:45:04.765577
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    pool = MonoWorker()

    def long_func(i, sleep=0.1):
        time.sleep(sleep)
        return 2*i

    tasks = [pool.submit(long_func, i) for i in range(5)]
    assert tasks[0].result() == 0 and tasks[1].result() == 2 and \
        tasks[2].result() == 4 and tasks[4].result() == 8

# Generated at 2022-06-14 13:45:15.203346
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # pylint: disable=protected-access
    import time
    import random
    from ..pandas import tqdm

    def worker(wait_sec):
        """Task function."""
        time.sleep(wait_sec)
        return wait_sec

    def test(maxlen, maxworkers):
        """Unit test."""
        mw = MonoWorker()
        mw.futures = deque([], maxlen)
        mw.pool = ThreadPoolExecutor(max_workers=maxworkers)

        t = tqdm(range(100))
        for i in t:
            wait_sec = random.random() / 2
            future = mw.submit(worker, wait_sec)
            if future:
                wait_sec = future.result()

# Generated at 2022-06-14 13:45:21.543079
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    tqdm_auto.write('submit slow')
    mw.submit(time.sleep, 3)
    tqdm_auto.write('submit fast')
    mw.submit(time.sleep, 1)
    tqdm_auto.write('submit faster')
    mw.submit(time.sleep, 0.5)
    tqdm_auto.write('submit fastest')
    mw.submit(time.sleep, 0.5)


if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:45:33.406052
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randrange
    from unittest import main

    def f(a, b, c=None):  # pragma: no cover
        sleep(randrange(1, 10))
        return a + b + (c or 0)

    def f_err(*args, **kwargs):  # pragma: no cover
        raise ValueError('Error')

    mw = MonoWorker()
    future = mw.submit(f, 1, 2)  # returns a concurrent.futures.Future object
    assert future.result() == 3
    future = mw.submit(f, 1, 2, 3)
    assert future.result() == 6
    future = mw.submit(f, 1, 2)  # replaces currently waiting task
    assert future.result() == 3
    assert mw.f

# Generated at 2022-06-14 13:45:43.002342
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from random import random

    def f(arg, sleep=0.1):
        time.sleep(sleep)
        return arg

    m = MonoWorker()
    f1 = m.submit(f, 1)
    f2 = m.submit(f, 2.1)
    f2.cancel()
    f3 = m.submit(f, 3, sleep=0.2)
    f4 = m.submit(f, 4, sleep=0.3)
    f4.cancel()
    f5 = m.submit(f, 5, sleep=0.05)
    f6 = m.submit(f, 6, sleep=0.2)
    # f6 should be replaced by f7
    f7 = m.submit(f, 7, sleep=0.1)

# Generated at 2022-06-14 13:45:57.609728
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import string
    import time
    import unittest

    random.seed(123)
    letters = string.ascii_letters

    def foo():
        time.sleep(1)
        return ''.join([random.choice(letters) for _ in range(20)])

    def bar():
        time.sleep(3)
        return ''.join([random.choice(letters) for _ in range(20)])

    def baz():
        time.sleep(5)
        return ''.join([random.choice(letters) for _ in range(20)])

    m = MonoWorker()
    start = time.time()
    assert m.futures == deque([], 2)
    assert m.submit(foo).result() == foo()
    assert time.time() - start > 1
    assert m

# Generated at 2022-06-14 13:46:06.035541
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    def worker(i, q):
        time.sleep(i / 100.)
        q.put((threading.get_ident(), i))

    mw = MonoWorker()

    import queue
    q = queue.Queue()

    for i in range(5):
        mw.submit(worker, i, q)

    # results should be ordered by worker index
    result = []
    while q.qsize():
        result.append(q.get())

    assert result == [(result[0][0], i) for i in range(5)]



# Generated at 2022-06-14 13:46:16.300088
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def dummy_func(name, sleep):
        time.sleep(sleep)
        return name

    def callback(future):
        result = future.result()
        if result is not None:
            tqdm_auto.write(str(result))

    tqdm_auto.write('\nTest when nothing running and nothing waiting:')
    mono = MonoWorker()

    tqdm_auto.write('\nTest when nothing running and waiting:')
    mono.submit(dummy_func, 'name', 0.5)

    tqdm_auto.write('\nTest when nothing running and waiting, plus one more:')
    mono.submit(dummy_func, 'name2', 0.3)

    tqdm_auto.write('\nStart running:')

# Generated at 2022-06-14 13:46:21.445773
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def f(i):
        from time import sleep
        sleep(0.5)
        return i * i + 1
    worker = MonoWorker()
    jobs = [worker.submit(f, i) for i in range(5)]
    for job in jobs:
        assert job.result() == f(job._args[0]) == (job._args[0] * job._args[0] + 1)

# Generated at 2022-06-14 13:46:30.958502
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event
    from contextlib import contextmanager

    @contextmanager
    def timer(t, e):
        sleep(t)
        e.set()

    e1 = Event()
    e2 = Event()
    w = MonoWorker()
    w.submit(timer, 0.1, e1)
    w.submit(timer, 0.3, e2)
    assert not e1.is_set()  # e1 is waiting
    assert not e2.is_set()  # e2 is running
    e2.wait()  # e2 has finished running
    assert not e1.is_set()  # e1 is still waiting
    w.submit(timer, 0.1, e1)
    assert not e1.is_set()  # e1 is running
    w

# Generated at 2022-06-14 13:46:40.993999
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event
    from concurrent.futures import TimeoutError

    def f(i, e):
        sleep(i * 0.1)
        e.wait()
        return i

    mw = MonoWorker()

    e = Event()
    a = mw.submit(f, 0, e)
    b = mw.submit(f, 1, e)  # a is not running
    e.set()  # run a and b
    assert b.result() == 1 and a.result() == 0

    e = Event()
    a = mw.submit(f, 0, e)
    b = mw.submit(f, 1, e)  # a is running
    e.set()  # run a and b
    assert b.result() == 1 and a.result()

# Generated at 2022-06-14 13:46:49.427334
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, random
    mw = MonoWorker()
    n, m = 10, 5
    assert len(mw.futures) == 0
    funcs_args_kwargs = []
    for i in tqdm_auto.trange(n, desc='test_MonoWorker_submit: i'):
        funcs_args_kwargs.append((str, i, 'The quick brown fox jumps over the lazy dog',
                                  dict(
                                      sep=' ',
                                      end='\n',
                                      file=tqdm_auto.sys.stdout)))
    for j in tqdm_auto.trange(m, desc='test_MonoWorker_submit: j'):
        func, args, kwargs = random.choice(funcs_args_kwargs)

# Generated at 2022-06-14 13:47:01.626468
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # input data
    task_execution_delay = 0.1
    tqdm_auto.write('task_execution_delay = ' + str(task_execution_delay))
    order_of_function_calls = []
    task_execution_time = []
    # use similar parameters to the default
    mw = MonoWorker()
    tasks = range(1000)
    # define tasks
    def task(id):
        tqdm_auto.write('task {} started'.format(id))
        order_of_function_calls.append(id)
        task_start_time = tqdm_auto.default_timer()
        tqdm_auto.sleep(task_execution_delay)
        task_end_time = tqdm_auto.default_timer()

# Generated at 2022-06-14 13:47:10.164389
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def dummy(*args, **kwargs):
        print(*args)
        return args[0]

    class MockThreadPoolExecutor(object):
        def __init__(self, *args, **kwargs):
            self.args = args
            self.kwargs = kwargs
            self.exceptions = []
        def submit(self, func, *args, **kwargs):
            self.next_args = args
            self.next_kwargs = kwargs
            raise self.exceptions.pop(0)
        def __repr__(self):
            return "MockThreadPoolExecutor(args={}, kwargs={})" \
                .format(self.args, self.kwargs)

    m = MonoWorker()
    m.pool = MockThreadPoolExecutor(max_workers=1)

# Generated at 2022-06-14 13:47:21.485007
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .async_.mp_pool import barrier, BarrierTimeout
    from time import sleep

    def long(n):
        sleep(n)
        if n > 0.5:
            raise Exception

    def short(n):
        sleep(n)

    with barrier:
        # create a worker and submit two tasks
        worker = MonoWorker()
        worker.submit(long, 1)
        worker.submit(short, 0.1)

        # try to submit another task
        with tqdm_auto.disable_range():
            # the new task fails if it is executed before the first task
            with tqdm_auto.experimental.nested(leave=False) as t:
                t.write("if output from here, the first task was not cancelled")
                # the new task is executed if a timeout occurs
                raise BarrierTimeout

# Generated at 2022-06-14 13:47:40.522845
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from collections import namedtuple

    def run_sample(sleep_time):
        time.sleep(sleep_time)
        return None

    result = namedtuple('result', ['start_time', 'end_time'])
    results = []
    worker = MonoWorker()

    # submit one task
    start = time.monotonic()
    worker.submit(run_sample, 1)
    end = time.monotonic()
    results.append(result(start, end))

    # submit a second task which replaces the first
    start = time.monotonic()
    worker.submit(run_sample, 5)
    end = time.monotonic()
    results.append(result(start, end))

    # the currently running task should finish first

# Generated at 2022-06-14 13:47:51.292945
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    mw = MonoWorker()
    tqdm_auto.write('Test')
    sleep_times = [1.1, 0.2, 1.0]
    for s in sleep_times:
        tqdm_auto.write('Submitting ' + str(s))
        mw.submit(time.sleep, s)
    for i in tqdm_auto.trange(2, desc='Test 2'):
        pass
    for s in sleep_times:
        tqdm_auto.write('Submitting ' + str(s))
        mw.submit(time.sleep, s)
    for i in tqdm_auto.trange(2, desc='Test 3'):
        tqdm_auto.write('Sleep time: ' + str(random.choice(sleep_times)))

# Generated at 2022-06-14 13:48:00.766580
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep, time
    from random import random

    def factory(sec):
        def wait(i):
            sleep((random() + 1.0) * sec)
            return i
        return wait

    demo_worker = MonoWorker()
    start = time()
    with tqdm_auto.tqdm(total=5) as t:
        for y in tqdm_auto.trange(2):
            for i in range(5):
                demo_worker.submit(factory(y*2 + 1.3)(i))
                t.update()
    assert time() - start < 6.0

# Generated at 2022-06-14 13:48:05.900930
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def _run(a, b):
        return a + b

    mono = MonoWorker()
    assert mono.submit(_run, 1, 3).result() == 4
    assert mono.submit(_run, 3, 2).result() == 5
    assert mono.submit(_run, 4, 2).result() == 6
    assert mono.submit(_run, 2, 1).result() == 3

# Generated at 2022-06-14 13:48:15.662015
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def foo(a, b, c=0, d=0):
        if d:
            raise Exception("d is nonzero")
        sleep(1)
        return a + b + c
    mw = MonoWorker()
    assert mw.futures.maxlen == 2  # isinstance(mw.futures, deque) == True
    assert len(mw.futures) == 0
    f1 = mw.submit(foo, 1, 2, c=3)
    assert len(mw.futures) == 1
    f2 = mw.submit(foo, 1, 2, c=5)
    assert len(mw.futures) == 1
    assert f2.result() == 8
    assert f1.result() == 6
    f3 = m

# Generated at 2022-06-14 13:48:26.032351
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .tests_tqdm import fname
    import time
    import os

    # Test `mw.submit(func)`
    def func():
        import os
        import time
        with open(fname, 'a') as f:
            f.write('func-start %s\n' % os.getpid())
        time.sleep(0.02)
        with open(fname, 'a') as f:
            f.write('func-end %s\n' % os.getpid())

    with open(fname, 'w') as f:
        f.write('test-pid %s\n' % os.getpid())
    mw = MonoWorker()
    mw.submit(func)
    time.sleep(0.03)
    assert set(open(fname, 'r'))

# Generated at 2022-06-14 13:48:35.150671
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from .tests_tqdm import with_setup

    def submit_check(mw, n, exec_time, wait_time, exp_n_append, exp_n_cancel):
        """Submit to `mw`, `n` times, and check that there have been
        `exp_n_append` times `mw.futures.append` and `exp_n_cancel` times
        `futures.cancel`"""
        with tqdm_auto.disable_tqdm(smoothing=0) as tqdm_instances:
            tqdm_instances.append(tqdm_auto)
            for i in tqdm_instances[0](range(n)):
                if i == 1:
                    # To allow to test that running is not canceled
                    time.sleep

# Generated at 2022-06-14 13:48:43.653879
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mono_worker = MonoWorker()
    for i in range(5):
        for j in range(i):
            mono_worker.submit(lambda: time.sleep(0.05),
                               i=i, j=j)
        mono_worker.submit(lambda: time.sleep(0.05),
                           i=i, j=-1)
        mono_worker.submit(lambda: time.sleep(0.05),
                           i=i, j=-2)
        mono_worker.submit(lambda: time.sleep(0.05),
                           i=i, j=-3)
        # time.sleep(0.01)
    time.sleep(0.1)  # get the 0.05 sleep out of the way

# Generated at 2022-06-14 13:48:52.514435
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import collections
    import time
    mw = MonoWorker()

    @tqdm_auto.track
    def func(x, a=None, b=None):
        time.sleep(x)
        return (a, b)

    mw.submit(func, 0.5, b=2)
    mw.submit(func, 1, a=1, b=4)
    for i in [2, 3, 4]:
        mw.submit(func, i, b=i ** 2)
    mw.submit(func, 0)

    waited = False
    for _ in range(10):
        time.sleep(0.3)
        if len(mw.futures) == 1:
            break
    else:
        waited = True

    assert len(mw.futures) == 1


# Generated at 2022-06-14 13:48:59.654584
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func():
        import time
        time.sleep(2)

    mono_worker = MonoWorker()
    first = mono_worker.submit(func)

    time.sleep(1)
    second = mono_worker.submit(func)

    time.sleep(1)
    third = mono_worker.submit(func)

    first.result()
    second.result()
    third.result()

# Generated at 2022-06-14 13:49:23.363963
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def a(x):
        time.sleep(x)
        return 1 / x

    def b(x):
        time.sleep(x)
        return 1 / (x - 2)

    mw = MonoWorker()
    tqdm_auto.write('a(2) + b(2)')
    r1 = mw.submit(a, 2)
    r2 = mw.submit(b, 2)
    tqdm_auto.write('a(2) + b(4)')
    r3 = mw.submit(a, 2)
    r4 = mw.submit(b, 4)

# Generated at 2022-06-14 13:49:33.726546
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from random import random

    # Make sure that only one task is running and that the waiting task
    # is a most recent submitted task.

    # Make sure that the waiting task gets executed if the running
    # task takes too long.
    expected_time = 5

    # The waiting task takes longer than the running task,
    # and should not be executed.
    running_task_time = 2

    def print_and_sleep(i):
        time.sleep(i)
        tqdm_auto.write(i)

    worker = MonoWorker()

    for _ in range(4):
        worker.submit(print_and_sleep, running_task_time)
    assert len(worker.futures) == 1  # Only one task is running.

    # Submit waiting task.
    # Should replace the waiting task as it

# Generated at 2022-06-14 13:49:44.600738
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .timer import sleep
    from .stats import Stats
    from .external_write_mode import external_write, external_flush

    def do_test(blen, alen, bsleep, asleep, **kwargs):
        mw = MonoWorker()
        with tqdm_auto(total=alen, desc="submitting", **kwargs) as pbar_submitting:
            with tqdm_auto(total=alen, desc="running", **kwargs) as pbar_running:
                while True:
                    num_submitted = len(mw.futures)
                    pbar_submitting.update(num_submitted)
                    num_running = len([f for f in mw.futures if not f.done()])
                    pbar_running.update(num_running)

# Generated at 2022-06-14 13:49:53.440892
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import threading

    lock = threading.Lock()
    done_count = list(range(5))
    with tqdm_auto.tqdm(total=len(done_count), desc='main') as pbar:
        with MonoWorker() as mw:
            # lock is used to prevent out of order print
            def background_task(i):
                time.sleep(random.uniform(0.3, 1.0))
                with lock:
                    pbar.write('task {0} done'.format(i))
                    done_count.remove(i)
                    pbar.update()
            for i in range(5):
                mw.submit(background_task, i)  # may replace current waiting task
                time.sleep(0.05)

# Generated at 2022-06-14 13:50:01.703862
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    class test(object):
        def __init__(self):
            self.f = MonoWorker()
            self.x = 0
            self.calls = 0

        def increment(self):
            time.sleep(0.2)
            self.calls += 1
            self.x += 1

    t = test()

    a = t.f.submit(t.increment)
    time.sleep(0.01)
    b = t.f.submit(t.increment)
    c = t.f.submit(t.increment)
    d = t.f.submit(t.increment)
    e = t.f.submit(t.increment)
    f = t.f.submit(t.increment)

    time.sleep(0.3)
    assert a.result()

# Generated at 2022-06-14 13:50:08.242091
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import concurrent.futures as futures
    class TqdmDummy:
        def update(self, *args, **kwargs):
            pass
    tqdm_auto.tqdm = TqdmDummy

    def task(delay, *args):
        time.sleep(delay)
        return delay

    # No task to wait
    with MonoWorker() as mw:
        fut = mw.submit(task, 1, 2)
        assert fut.result() == 1
    # Two tasks, the first finishe first
    with MonoWorker() as mw:
        mw.submit(task, 1, 2)
        fut = mw.submit(task, 1, 3)
        assert fut.result() == 1
    # Two tasks, the first finishe last

# Generated at 2022-06-14 13:50:17.952592
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    from ..utils import _term_move_up
    from ..utils import _range

    def running_task(duration):
        sleep(duration)
        tqdm_auto.write(
            'Ran for {:.0f}s, this line should be overprinted'.format(duration))

    def waiting_task(duration, cancel_running=False):
        sleep(duration)
        if cancel_running:
            # Cancel running task
            mworker.futures.popleft().cancel()
        tqdm_auto.write(
            'Waited for {:.0f}s, this line should be overprinted'.format(
                duration))

    mworker = MonoWorker()

    # Create a tqdm progress bar to ensure the terminal is in a known state

# Generated at 2022-06-14 13:50:27.679925
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Event

    # import multiprocessing  # for nice output in IPython notebook
    # multiprocessing.set_start_method('spawn')

    from ..auto import tqdm as tqdm_auto
    from .tqdm_ext_threads import tqdm as tqdm_ext_threads

    def wait(seconds, event=None):
        with tqdm_auto(total=seconds, file=tqdm_auto.get_write_attr(),
                       desc=str(seconds), ascii=True) as t:
            while t.n < t.total and not (event and event.is_set()):
                time.sleep(1)
                t.update()
            return t.n


# Generated at 2022-06-14 13:50:39.273020
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from collections import OrderedDict
    import time

    def wait_and_print(time_sec):
        time.sleep(time_sec)
        return time_sec, time.asctime()

    tqdm_auto.write('5 running, 1 waiting, most recent submitted runs first.')
    mw = MonoWorker()
    for time_sec in range(6):
        time_sec, time_str = mw.submit(wait_and_print, time_sec).result()
        tqdm_auto.write('{0}: {1}'.format(time_sec, time_str))

    tqdm_auto.write('0 running, 1 running, 1 waiting, most recent submitted runs first.')
    mw = MonoWorker()

# Generated at 2022-06-14 13:50:47.560029
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> import time
    >>> def wait(n):
    ...     time.sleep(n)
    >>> mw = MonoWorker()
    >>> running = mw.submit(wait, 3)
    >>> running.done()
    False
    >>> for i in range(10):
    ...     time.sleep(1)
    ...     if running.done():
    ...         break
    >>> running.done()
    True
    >>> def wait_raise(n):
    ...     time.sleep(n)
    ...     raise Exception('Exception')
    >>> running = mw.submit(wait_raise, 3)
    Exception
    >>> mw.submit(wait, 3)
    <Future at ...>
    """
    pass

# Generated at 2022-06-14 13:51:27.429165
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from tempfile import TemporaryDirectory
    from time import sleep
    from os import listdir, remove
    from operator import add

    with TemporaryDirectory() as temp_dir:
        def test_func(x, f=temp_dir):
            sleep(1)
            with open(f + '/' + x, 'w') as fout:
                pass
        defer, add_ = [], add
        for i in range(8):
            defer.append(MonoWorker.submit(test_func, str(i)))
            sleep(0.5)
        assert len(listdir(temp_dir)) == 1
        sleep(1)
        assert len(listdir(temp_dir)) == 2
        sleep(1)
        assert len(listdir(temp_dir)) == 3

# Generated at 2022-06-14 13:51:38.064585
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    import contextlib

    m = MonoWorker()
    N = 4

    def sleep_and_write(t, k):
        time.sleep(t)
        tqdm_auto.write('{} {}'.format(t, k))

    @contextlib.contextmanager
    def executor_process(t, k):
        f = m.submit(sleep_and_write, t, k)
        time.sleep(t/2.0)
        yield
        f.result()

    for k in range(N):
        with executor_process(k, k):
            pass
        time.sleep(1)

    with executor_process(1, 1):
        threading.Thread(target=executor_process,
                         args=(3, 3), kwargs={}).start

# Generated at 2022-06-14 13:51:47.057856
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from operator import add

    # Start with an empty MonoWorker
    monowork = MonoWorker()
    assert tuple(monowork.futures) == ()

    # Submit a task
    future1 = monowork.submit(add, 2, 3)
    # Check that the task has been submitted to the pool
    assert monowork.pool._work_queue.qsize() == 1
    # Check that the task is in the future queue
    assert tuple(monowork.futures) == (future1, )
    # Wait for the task to be done
    sleep(0.01)
    # Check that the task has been removed from the pool
    assert monowork.pool._work_queue.qsize() == 0

    # Submit a second task

# Generated at 2022-06-14 13:51:52.957920
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    X = []

    def func(x):
        time.sleep(0.1 * x)
        X.append(x)
        return str(x)

    mw = MonoWorker()
    res = [mw.submit(func, x) for x in range(5)]
    assert all(r is None for r in res)
    time.sleep(0.3)
    assert X == [4]
    assert mw.futures[0].result() == '4'

    X = []
    res = [mw.submit(func, x) for x in range(5)]
    time.sleep(0.3)
    assert X == [4]
    assert mw.futures[0].result() == '4'

    X = []

# Generated at 2022-06-14 13:52:03.814784
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event
    from contextlib import contextmanager
    from time import sleep
    from random import random
    from numpy import histogram

    @contextmanager
    def check_task(name, wait, running, done):
        try:
            yield
        finally:
            # Check task is running during wait
            assert wait.wait(5), "Task '{}' did not start".format(name)
            running[name] = True
            # Check that task is done
            while not done[name]:
                sleep(0.1)
            sleep(0.1)
            assert not wait.is_set(), "Task '{}' took too long".format(name)

    # Test submission via MonoWorker

# Generated at 2022-06-14 13:52:11.487625
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    # pylint: disable=global-variable-undefined
    global output

    def _test_func(popen_args, *args, **kwargs):
        global output
        output = "Running: {} {} {}".format(
            popen_args, str(args), str(kwargs))
        time.sleep(0.3)
        return len(popen_args) * len(args) * len(kwargs)

    output = None
    mw = MonoWorker()

    assert mw.submit(_test_func, ["echo", "hello", "world"], 1, 2, 3)
    time.sleep(0.1)
    assert output == "Running: ['echo', 'hello', 'world'] (1, 2, 3) {}"


# Generated at 2022-06-14 13:52:17.126065
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def _side_effect(x):
        return x
    from time import sleep

    worker = MonoWorker()
    assert worker.submit(print, "A") == worker.submit(print, "B")
    assert worker.futures[0] != worker.futures[1]
    assert worker.submit(sleep, 0.2) == worker.submit(sleep, 0.2)
    assert len(worker.futures) == 2
    assert worker.futures[0].done()
    assert worker.futures[1].done()
    assert worker.futures[0].exception() == worker.futures[1].exception()
    assert worker.submit(print, "C") == worker.submit(print, "D")
    assert len(worker.futures) == 2
    assert worker.submit

# Generated at 2022-06-14 13:52:27.381483
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def func(futures, seconds):
        # print("running", seconds)
        sleep(seconds)
        futures.append(seconds)

    workers = MonoWorker()
    futures = []
    n = 3
    test_futures = []
    for i in range(n):
        test_futures.append(workers.submit(func, futures, i))
        sleep(0.1)

    failed = 0
    succeeded = 0
    for test_future in test_futures:
        try:
            test_future.result()
            succeeded += 1
        except Exception as e:
            failed += 1
        else:
            tqdm_auto.write('{} succeeded'.format(succeeded))
        sleep(0.1)

    # print("futures", futures)

# Generated at 2022-06-14 13:52:34.743153
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from unittest import TestCase, main

    class TestMonoWorker(TestCase):
        def test_monoworker_submit(self):
            def _do_nothing():
                sleep(0.1)  # for some IO time

            def _do_nothing_with_arg(a):
                sleep(0.1)  # for some IO time
                return a

            mw = MonoWorker()
            self.assertEqual(len(mw.futures), 0)
            res = []
            for i in tqdm_auto.tqdm(range(3)):
                res.append(mw.submit(_do_nothing))
                self.assertEqual(len(mw.futures), 1)

            # mw.futures[0].result()
           

# Generated at 2022-06-14 13:52:45.630157
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import concurrent.futures
    import time
    import threading

    # Sleep function that can interupted
    def sleeper(n):  # pragma: no cover
        import time
        import threading
        t = threading.currentThread()
        while getattr(t, "do_run", True) and n > 0:
            n -= 1
            time.sleep(1)

    # Configure both workers and sleepers
    mw1 = MonoWorker()
    mw2 = MonoWorker()
    t1 = threading.Thread(target=sleeper, args=(5,))
    t2 = threading.Thread(target=sleeper, args=(5,))
    t3 = threading.Thread(target=sleeper, args=(5,))