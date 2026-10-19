

# Generated at 2022-06-14 13:42:42.476052
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()  # init
    l = mw.futures
    assert len(l) == 0
    mw.submit(time.sleep, 0.1)  # func1
    assert len(l) == 1
    mw.submit(time.sleep, 0.1)  # func2
    assert len(l) == 1
    l[0].result()  # wait for completion
    assert len(l) == 0
    mw.submit(time.sleep, 0.1)  # func3
    assert len(l) == 1
    mw.submit(time.sleep, 0.1)  # func4
    assert len(l) == 1
    mw.submit(time.sleep, 2)  # func5
    assert len(l) == 2

# Generated at 2022-06-14 13:42:52.661017
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import threading
    import time

    class Helper(object):
        def __init__(self):
            self.lock = threading.Lock()
            self.x = 0

        def _call_and_lock(self, delay):
            with self.lock:
                time.sleep(delay)
                self.x += 1

        def call_n_lock(self, delay):
            # noinspection PyAttributeOutsideInit
            self.x += 0.5
            t = threading.Thread(
                target=self._call_and_lock, args=(delay,))
            t.daemon = True
            t.start()

    helper = Helper()
    worker = MonoWorker()
    worker.submit(helper.call_n_lock, 1)

# Generated at 2022-06-14 13:43:01.786716
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .tqdm_test_classes import PretendTiming

    def func(start, end):
        """Slow - to test async (submitted) execution."""
        for i in tqdm_auto(range(start, end + 1), leave=False,
                           total=1 + end - start, unit='x',
                           miniters=1, mininterval=0.1,
                           dynamic_ncols=True,
                           gui=True, file=PretendTiming()):
            sleep(0.15)
        return i

    a = 1
    b = 9
    # Testing simultaneous futures in a single thread
    monoworker = MonoWorker()
    print("Testing simultaneous submission")
    # 1st submit (1st to run)
    fut1 = monoworker

# Generated at 2022-06-14 13:43:06.869129
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def print_args(*a):
        print('Args:', a)
        sleep(5)

    worker = MonoWorker()
    for i in tqdm_auto.tqdm(range(2), ncols=80):
        worker.submit(print_args, 'test_' + str(i))


# Generated at 2022-06-14 13:43:16.064838
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test for `tqdm.contrib.MonoWorker.submit`."""
    from multiprocessing import Process, Manager
    from collections import defaultdict
    import time
    manager = Manager()
    log = manager.dict(defaultdict(int))
    mw = MonoWorker()

    def proc(func_num, arg, log):
        """Awaits func_num's future to release,
        then calls `log[func_num]=arg`."""
        log[func_num] = mw.submit(time.sleep, 0.1).result()
        time.sleep(0.3)
        log[func_num] = arg
    p1 = Process(target=proc, args=(1, 6, log))
    p2 = Process(target=proc, args=(2, 7, log))
    p3

# Generated at 2022-06-14 13:43:25.221482
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    from time import sleep
    from itertools import repeat

    def _step(i):
        """
        `i` = 0: running
        `i` = 1: waiting
        `i` > 1: lost
        """
        sleep(0.01 * random.random())
        return i

    def _step2(i):
        """
        `i` = 0: running
        `i` = 1: waiting
        `i` > 1: lost
        """
        sleep(0.1 * random.random())
        return i

    pool = MonoWorker()
    assert len(pool.futures) == 0

    future1 = pool.submit(_step, 0)
    assert len(pool.futures) == 1
    a = list(pool.futures)

# Generated at 2022-06-14 13:43:32.795195
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from tqdm import tqdm
    import time
    mw = MonoWorker()
    def task(x):
        time.sleep(0.1)
        return x
    # if submitting up to two tasks at a time, two tasks are immediately run
    # (and two tasks is the maximum concurrency)
    for _ in tqdm(range(5)):
        mw.submit(task, 1)
        mw.submit(task, 2)
    # if submitting more than two tasks, the third and subsequent tasks are
    # queued up and must wait for the second task to finish (because
    # max_workers=1)
    for i in range(5):
        mw.submit(task, i)
    # if submitting more than two tasks, the third and subsequent tasks replace
    # the second task in the queue (and

# Generated at 2022-06-14 13:43:43.006814
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def do_work(x, sleep=0.01):
        time.sleep(sleep)
        return x

    worker = MonoWorker()

    # submit the first task
    worker.submit(do_work, x=1, sleep=0.02)

    # submit another task which should be canceled before being executed
    future1 = worker.submit(do_work, x=2, sleep=0.02)
    assert not future1.done()
    assert not future1.cancelled()
    worker.submit(do_work, x=3, sleep=0.02)
    assert future1.cancelled()
    assert future1.done()

    # submit the 4th task which should replace the 3rd task
    future2 = worker.submit(do_work, x=4, sleep=0.02)
   

# Generated at 2022-06-14 13:43:52.288207
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # prepare environment
    global dummy_number_of_calls
    dummy_number_of_calls = 10
    global dummy_results
    dummy_results = []
    def dummy_function(parameter):
        global dummy_number_of_calls
        dummy_number_of_calls -= 1
        global dummy_results
        dummy_results.append(parameter)
        return

    # test MonoWorker.submit

# Generated at 2022-06-14 13:44:01.954418
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from contextlib import contextmanager
    import time

    @contextmanager
    def print_time(handle):
        start = time.time()
        yield
        duration = time.time() - start
        handle.write("took {} s\n".format(duration))

    mw = MonoWorker()

    @contextmanager
    def print_time_first_task(handle):
        with print_time(handle):
            try:
                yield mw.submit(time.sleep, 3)
            except Exception as e:
                handle.write(str(e) + "\n")


# Generated at 2022-06-14 13:44:11.969850
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    As unit test for method submit of MonoWorker, it tests the following
    capabilities of the MonoWorker.submit method:

        1. Capable to submit a task for completion by the MonoWorker.
        2. Capable to abort a running task when a new one is submitted.
        3. Capable to keep a running task when a new task is submitted.
        4. Capable to keep a running task if a new task is not successfully submitted.
    """

    import time
    import numpy as np
    import os

    # Create test file

# Generated at 2022-06-14 13:44:16.727490
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..compat import range
    mw = MonoWorker()
    # Simulate no waiting
    [mw.submit(time.sleep, 0.1) for _ in range(2)]
    assert len(mw.futures) == 1
    # Simulate waiting
    [mw.submit(time.sleep, 0.1) for _ in range(5)]
    assert len(mw.futures) == 2
    assert mw.futures[0] == mw.futures[1]
    # And cancel waiting
    mw.submit(lambda: 1)
    assert mw.futures[0] == mw.futures[1]
    assert len(mw.futures) == 1
    # Test that running is not replaced

# Generated at 2022-06-14 13:44:26.930028
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Event
    from concurrent.futures import TimeoutError
    m = MonoWorker()
    start = time.time()
    e = Event()

    m.submit(e.wait)
    time.sleep(0.1)
    assert not e.is_set()

    m.submit(time.sleep, 20)
    time.sleep(0.1)
    assert not e.is_set()
    e.set()

    time.sleep(20)
    assert abs(time.time() - start - 20) < 1

    e.clear()
    start = time.time()

    m.submit(e.wait)
    time.sleep(0.1)
    assert not e.is_set()

    # Waiting task is aborted; the following is started instead

# Generated at 2022-06-14 13:44:37.868624
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import tqdm
    import threading
    import multiprocessing

    mworker = MonoWorker()

    def produce(start, end):
        time.sleep(0.01)
        return list(range(start, end))

    def consume(lst):
        time.sleep(0.02)
        return 0

    def produce_and_consume(i):
        producers = [
            mworker.submit(produce, 0, 100),
            mworker.submit(produce, 100, 200),
            mworker.submit(produce, 200, 300),
            mworker.submit(produce, 300, 400),
            mworker.submit(produce, 400, 500)
        ]

# Generated at 2022-06-14 13:44:46.553330
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import time

    def id_getter(n):
        import time
        time.sleep(random.randint(0, 3))
        return n

    iterator = iter(range(10))
    worker = MonoWorker()
    results = []

    while True:
        try:
            id_ = next(iterator)
        except StopIteration:
            break
        else:
            future = worker.submit(id_getter, id_)
            if future is not None:
                future.add_done_callback(lambda f: results.append(f.result()))

    time.sleep(3)
    assert results == [0]

# Generated at 2022-06-14 13:44:54.254735
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import functools
    import concurrent.futures
    from ..utils import _decorate_partial
    from ..std import next

    def raise_exception(e):
        """Raise `e` in a new thread."""
        def raise_e():
            raise e
        mono_worker.submit(raise_e)

    work = lambda: time.sleep(0.1)

    # tqdm unit tests
    raise_exception(BlockingIOError)
    with tqdm_auto.tqdm(desc='Download', disable=False,
                        unit='B', unit_scale=True, unit_divisor=1024,
                        dynamic_ncols=True) as t:
        t.write("testing `tqdm_notebook`")

# Generated at 2022-06-14 13:45:05.506841
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep  # NOQA
    from random import randint  # NOQA

    class ExampleClass(object):
        pass

    ec = ExampleClass()

    def job():
        ec.job_running += 1
        sleep(randint(1, 2))
        ec.job_running -= 1
        # ec.job_num_finished += 1
        # return "job" + str(ec.job_num_finished)

    ec.job_running = 0
    ec.job_num_finished = 0
    ec.mono_worker = MonoWorker()

    while ec.job_running < 1:
        ec.mono_worker.submit(job)  # Will start job if not running
        sleep(randint(1, 2))

    while ec.job_running:
        ec.mono_worker.submit

# Generated at 2022-06-14 13:45:15.856532
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    mw = MonoWorker()
    from asyncio import sleep as asyncio_sleep

    # Handle exception
    from six.moves import xrange as originalxrange
    try:
        _range = originalxrange(10)
    except:
        _range = range(10)
    for _ in _range:
        mw.submit(1)

    # Handle asynchronous functions
    import asyncio
    loop = asyncio.get_event_loop()

    async def wait(dt):
        await asyncio_sleep(dt)
        return True

    future = mw.submit(loop.run_until_complete, wait(0.01))
    assert future.result()

    # Asynchronous functions should not be called twice
    results = set()
    def report_result(result):
        results.add(result)

# Generated at 2022-06-14 13:45:21.478100
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test `MonoWorker.submit`."""
    import time
    import unittest
    try:
        import queue
    except ImportError:  # pragma: no cover
        import Queue as queue

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.result_q = queue.Queue()
            self.abort = False

        def test_submit(self):
            def foo(delay, x):
                time.sleep(delay)
                self.result_q.put(x)
            worker = MonoWorker()
            worker.submit(foo, 0.1, 1)
            worker.submit(foo, 0.2, 2)
            worker.submit(foo, 0.3, 3)
            time.sleep(0.4)

# Generated at 2022-06-14 13:45:31.289002
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def do_time(n):
        time.sleep(n)
        return n

    def assert_time(n, expected=None):
        expected = expected or n
        assert next(MonoWorker().submit(do_time, n)) == expected

    assert_time(0.1)  # Test simplest case
    assert_time(0.1)  # Second task not queued as first is running
    assert_time(0.1)  # Third task replaces second task
    assert_time(0.1, 0.2)  # Test return value of third task
    assert_time(0.3)  # Second task replaced has not finished

# Generated at 2022-06-14 13:45:44.679464
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from sys import stderr
    from time import sleep
    from ..utils import format_sizeof
    import gc

    def f(x):
        sleep(0.1)
        return x

    # test waiting tasks are cleared
    mw = MonoWorker()
    f1 = mw.submit(f, 1)
    f2 = mw.submit(f, 2)
    assert f1.done()
    assert not f2.done()
    assert f2.result() == 2
    f3 = mw.submit(f, 3)
    assert f3.result() == 3

    # test that long running tasks are not cleared
    f4 = mw.submit(f, 4)
    assert f4.result() == 4
    f5 = mw.submit(f, 5)
    f6 = mw

# Generated at 2022-06-14 13:45:55.809052
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    import unittest
    class Test_MonoWorker_submit(unittest.TestCase):
        def test_run(self):
            def slow10():
                time.sleep(10)
                return True
            def slow11():
                time.sleep(11)
                return True
            def slow12():
                time.sleep(12)
                return True
            def end():
                return True
            mw = MonoWorker()
            f1 = mw.submit(slow10)
            f2 = mw.submit(slow11)
            f3 = mw.submit(slow12)
            f4 = mw.submit(end)
            f1.cancel()
            f2.cancel()
            f3.cancel()
            f4.cancel()
           

# Generated at 2022-06-14 13:46:06.970927
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import sys

    def f(x):
        time.sleep(x)
        return x

    mw = MonoWorker()
    assert len(mw.futures) == 0, mw.futures
    mw.submit(f, 0.01)
    assert len(mw.futures) == 1, mw.futures
    mw.submit(f, 0.01)
    assert len(mw.futures) == 1, mw.futures
    mw.submit(f, 0.01)
    assert len(mw.futures) == 1, mw.futures
    mw.submit(f, 0.02)
    assert len(mw.futures) == 1, mw.futures
    m

# Generated at 2022-06-14 13:46:16.927891
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .slow_stream import SlowStream
    from .read import read
    from time import sleep
    from sys import platform
    from os import stat, close

    def test_open_fn(f, mode="r", **kwargs):
        close(3)
        stat(f.name)
        return open(f.name, mode, **kwargs)

    def test_read_fn(f, length):
        return read(f, length)

    def test_close_fn(f):
        f.close()

    file_size = 10000

    if platform == "win32":
        from os import _get_osfhandle as _get_handle
        from msvcrt import setmode as _setmode
        from os import O_BINARY as _O_BINARY

# Generated at 2022-06-14 13:46:23.884919
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from random import shuffle

    def f(x):
        def g():
            time.sleep(x)
            return x

        return g

    generator = (f(i) for i in range(10))
    assert list(range(10)) == sorted(MonoWorker().submit(f, i).result()
                                     for f, i in zip(generator, range(10)))

    generator = [f(i) for i in range(10)]
    shuffle(generator)
    assert list(range(10)) == sorted(MonoWorker().submit(f).result()
                                     for f in generator)

# Generated at 2022-06-14 13:46:31.822891
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from concurrent.futures import Future
    from time import sleep
    from unittest import TestCase, main

    class TestCase(TestCase):
        def test_submit(self):
            def mock_submit(f, *args, **kwargs):
                r = Future()
                r.set_result(None)
                return r

            mw = MonoWorker()
            mw.pool.submit = mock_submit
            self.assertIsNone(mw.submit(sleep, 0))
            self.assertIsNone(mw.submit(sleep, 0))

    main(module='monoworker', exit=False, verbosity=2, buffer=False)

# Generated at 2022-06-14 13:46:41.831354
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    # basic test
    mw = MonoWorker()
    def test_func(i, time_sleep):
        time.sleep(time_sleep)
        return i
    time_sleep = 0.1
    assert mw.submit(test_func, 1, time_sleep).result() == 1
    assert mw.submit(test_func, 2, time_sleep).result() == 2
    assert mw.submit(test_func, 3, time_sleep*2).result() == 3
    # running task cancelling
    assert mw.submit(test_func, 4, time_sleep).result() == 4
    time.sleep(time_sleep/2)
    assert mw.submit(test_func, 5, time_sleep).result() == 5
    # waiting task cancelling

# Generated at 2022-06-14 13:46:49.973795
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    from time import sleep
    import traceback

    def attempt_error():
        sleep(0.1)
        raise Exception('test_MonoWorker_submit error')

    def error_safety():
        for _ in range(2):
            try:
                attempt_error()
                return True
            except Exception as e:
                traceback.print_exc()

    def ui(w):
        from threading import Thread
        from threading import Event
        import time

        class UI(Thread):
            def __init__(self):
                Thread.__init__(self)
                self._stop_event = Event()

            def stop(self):
                self._stop_event.set()

            def stopped(self):
                return self._stop_event.is_set()

            def run(self):
                from time import sleep


# Generated at 2022-06-14 13:46:59.862291
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def add(x, y):
        return x + y
    mw = MonoWorker()
    mw.submit(add, 1, 2)
    mw.submit(add, 3, 4)  # should discard the first (1, 2) task
    mw.submit(add, 5, 6)  # should discard the second (3, 4) task
    assert mw.futures[0].result() == 11
    try:
        mw.futures[1].result()  # should raise exception
        assert False
    except AssertionError:
        raise
    except Exception as e:
        # cancelled?
        pass

# Generated at 2022-06-14 13:47:08.740238
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Monoworker for testing
    worker = MonoWorker()

    def slow_return():
        from time import sleep
        sleep(0.1)
        return 1

    def slow_print():
        from time import sleep
        sleep(0.1)
        print('OK')

    # submit functions and get results
    from random import randint
    for _ in range(0, randint(4, 12)):
        for _ in range(randint(1, 4)):
            # 4 times, submit slow_return, wait
            future = worker.submit(slow_return)
        assert future.result() == 1

    # submit the same function twice
    for _ in range(1, 4):
        # testing: submit slow_print, submit slow_print, wait, wait
        worker.submit(slow_print)

# Generated at 2022-06-14 13:47:18.647087
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    import time
    def mysleep(sec):
        time.sleep(sec)
        return sec

    mw = MonoWorker()
    # task = mw.submit(mysleep, 1)
    mw.submit(mysleep, 2)
    task = mw.submit(mysleep, 3)
    assert task.result() == 3
    """
    pass

# Generated at 2022-06-14 13:47:26.366692
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import concurrent.futures
    import random
    import time
    # import threading
    # print('Starting main threads')
    # threading.current_thread().name
    mono = MonoWorker()

    for i in range(5):
        mono.submit(_test_MonoWorker_submit_worker, i)

    time.sleep(3)
    # print('main threads done sleeping')

    def callback(future):
        # print('callback')
        # print(future.result())
        pass

    # print('Starting main threads')

    for i in range(5, 11):
        myfuture = mono.submit(_test_MonoWorker_submit_worker, i)
        # print('main thread appended myfuture')
        myfuture.add_done_callback(callback)
        # print('main thread added callback to my

# Generated at 2022-06-14 13:47:35.538719
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event

    mw = MonoWorker()

    # test that running is not interrupted when nothing is waiting
    ev_running = Event()
    def running():
        ev_running.wait()
    mw.submit(running)
    sleep(0.01)
    assert len(mw.futures) == 1
    assert not mw.futures[-1].done()
    ev_running.set()

    # test that waiting is cleared when running is not done
    ev_running = Event()
    def running():
        ev_running.wait()

    def waiting():
        ev_waiting.set()

    ev_running.clear()
    ev_waiting = Event()
    mw.submit(running)
    mw.submit(waiting)
    ev_wa

# Generated at 2022-06-14 13:47:46.309154
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> from time import sleep
    >>> from .monoworker import MonoWorker  # doctest: +SKIP
    >>> worker = MonoWorker()  # doctest: +SKIP
    >>> def f(t):  # doctest: +SKIP
    ...     sleep(t)  # doctest: +SKIP
    ...     return t  # doctest: +SKIP
    >>> for i in range(4):
    ...     worker.submit(f, 2)  # doctest: +SKIP
    >>> list(worker.futures)  # doctest: +SKIP
    [<Future at ... state=pending>]
    >>> list(worker.futures)[0].result()  # doctest: +SKIP
    2
    """
    pass

# Generated at 2022-06-14 13:47:55.386300
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    mw = MonoWorker()

    def f(d):
        time.sleep(d)
        return d

    def g(d):
        time.sleep(2 * d)
        return 2 * d

    tqdm_auto.write('submit 1')
    mw.submit(f, 1)
    tqdm_auto.write('submit 2')
    mw.submit(f, 2)
    tqdm_auto.write('submit 3')
    mw.submit(f, 3)
    tqdm_auto.write('submit 4')
    mw.submit(f, 4)
    tqdm_auto.write('submit 5')
    mw.submit(f, 5)
    tqdm_auto.write('submit 6')

# Generated at 2022-06-14 13:48:05.016427
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import threading, queue

    from .threading import CIOThread, ThreadWithReturnValue

    def print_thread(p, q):
        try:
            with tqdm_auto.tqdm(total=1,
                                file=p,
                                bar_format="{l_bar} {postfix[0]} {postfix[1]}") \
                    as t:
                while t.total is None or t.n < t.total:
                    status = q.get()
                    if isinstance(status, Exception):
                        t.set_postfix(prefix=str(status), status='fail')
                        break
                    else:
                        t.update()
                        t.set_postfix(prefix=status)
        finally:
            try:
                p.flush()
            except IOError:
                pass


# Generated at 2022-06-14 13:48:13.823845
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import functools
    import concurrent.futures
    def out(*args):
        time.sleep(1)
        return ' '.join(args)
    mw = MonoWorker()
    print(mw.submit(out, 'a'))
    print(mw.submit(out, 'b'))
    print(mw.submit(out, 'c'))
    print(mw.submit(out, 'd'))
    print(mw.submit(out, 'e'))
    print(mw.submit(out, 'f'))
    print(mw.submit(out, 'g'))
    print(mw.submit(out, 'h'))
    print(mw.futures)

# Generated at 2022-06-14 13:48:22.741491
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def sleep_long():
        sleep(2)

    def sleep_short():
        sleep(1)

    worker = MonoWorker()
    worker.submit(sleep_long)  # should run
    worker.submit(sleep_short)  # should replace currently waiting task
    worker.submit(sleep_short)  # should replace currently waiting task
    worker.submit(sleep_short)  # should replace currently waiting task
    worker.submit(sleep_long)  # should replace currently waiting task
    sleep(0.5)  # sleep a bit to ensure last submitted (running) is finished
    worker.submit(sleep_short)  # should replace currently waiting task
    sleep(1.5)  # sleep a bit to ensure first submitted (running) is finished
    worker.submit(sleep_short)  # should not replace currently waiting

# Generated at 2022-06-14 13:48:31.421518
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Imports
    import time
    from random import randint
    from datetime import datetime
    # Prepare
    mw = MonoWorker()
    # Run
    for _ in range(5):
        mw.submit(
            time.sleep, randint(5, 10) / 10,
            desc=str(datetime.now()))
    # Wait for it …
    for i in tqdm_auto.tqdm(range(11), desc='Async'):
        time.sleep(1)
    # Manual finish if required
    for f in mw.futures:
        if not f.done():
            f.cancel()
    # Finish
    return mw

# Generated at 2022-06-14 13:48:36.498066
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def f(*args):
        pass

    mw = MonoWorker()
    mw.submit(f, 0)
    mw.submit(f, 1)
    mw.submit(f, 2)
    mw.submit(f, 3)
    assert len(mw.futures) == 1
    assert mw.futures[0].result() == 3



# Generated at 2022-06-14 13:48:53.400350
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from multiprocessing import Queue
    from threading import Thread
    from time import sleep, time

    def submit_to_queue(queue):
        queue.put(1)
        sleep(0.1)
        queue.put(1)
        sleep(0.1)
        queue.put(1)
        sleep(0.1)
        queue.put(1)

    def submit_to_queue_slowly(queue):
        queue.put(1)
        sleep(0.5)
        queue.put(1)
        sleep(0.5)
        queue.put(1)
        sleep(0.5)
        queue.put(1)

    def submit_to_queue_err(queue):
        queue.put(1)
        raise RuntimeError("runtime error!")

    # Test for MonoWork

# Generated at 2022-06-14 13:49:04.381388
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from collections import deque
    import random
    import threading
    import unittest

    class MonoTest(unittest.TestCase):
        def setUp(self):
            self.worker = worker = MonoWorker()
            self.calls = calls = []

            def _call(i, j, k):
                sleep(random.random() / 3)
                calls.append((i, j, k))
                return i + j + k

            def _submit(i, j, k):
                return worker.submit(_call, i, j, k)

            self.submit = _submit

        def _submit_some(self, seq):
            for i, j, k in seq:
                self.submit(i, j, k)


# Generated at 2022-06-14 13:49:11.958002
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    x, y, z = mw.submit(time.sleep, 0.1), mw.submit(time.sleep, 0.1), mw.submit(time.sleep, 0.1)
    x.result(); y.result(); z.result()
    assert x.done() and not x.cancelled()
    assert y.done() and not y.cancelled()
    assert z.done() and not z.cancelled()

# Generated at 2022-06-14 13:49:15.067203
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    def worker(x):
        time.sleep(random.uniform(1, 3))
        tqdm_auto.write(x)

    for i in tqdm_auto.trange(10):
        MonoWorker().submit(worker, i)



# Generated at 2022-06-14 13:49:23.578947
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ..utils import format_sizeof

    def slow_function(sleep_for=0.1, **kwargs):
        sleep(sleep_for)
        return kwargs['size']

    worker = MonoWorker()

    data = list(range(20))
    data[-1] = "Last"
    with tqdm_auto.tqdm(data,
                        desc='Data',
                        ascii=True, mininterval=0.1, miniters=1) as t:
        for size in t:
            if size == 'Last':
                continue
            future = worker.submit(
                slow_function, sleep_for=0.1, size=size * 2)
            fmt = format_sizeof(size)
            t.set_postfix_str(fmt)
           

# Generated at 2022-06-14 13:49:33.570885
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def print_and_wait(m, s):
        tqdm_auto.write(m)
        sleep(s)
        tqdm_auto.write(m + " done")

    w = MonoWorker()
    w.submit(print_and_wait, "first", 1)
    sleep(0.5)
    w.submit(print_and_wait, "second", 0.1)
    sleep(0.5)
    w.submit(print_and_wait, "third", 0.5)
    sleep(0.5)
    w.submit(print_and_wait, "fourth", 0.5)
    sleep(0.5)
    w.submit(print_and_wait, "fifth", 0.5)

# Generated at 2022-06-14 13:49:41.602292
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from contextlib import contextmanager
    from .utils import silence_stderr

    @contextmanager
    def get_monoworker():
        """Return a monoworker with a thread running for 1 second."""
        mw = MonoWorker()
        mw.submit(time.sleep, 1)
        yield mw
        mw.pool.shutdown(wait=True)

    with silence_stderr(), get_monoworker() as mw:
        tqdm_auto.write('submit mono')
        mw.submit(tqdm_auto.write, 'mono')
        tqdm_auto.write('submit mono-duo')
        mw.submit(tqdm_auto.write, 'mono-duo')

# Generated at 2022-06-14 13:49:51.074819
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def f(n):
        time.sleep(n)
        return n

    mono_worker = MonoWorker()

    def test_submit(n, sleep, overwrite, exp_res):
        if overwrite:
            mono_worker.futures.append(None)
        t = time.time()
        res = mono_worker.submit(f, n)
        if res is not None:
            res = res.result()
        t = time.time() - t
        if exp_res is not None:
            assert res == exp_res, (res, exp_res)
            assert exp_res <= t <= exp_res + sleep, (exp_res, t, sleep)
        else:
            assert res is None, res
            assert t < sleep, (t, sleep)
    # test_submit(n,

# Generated at 2022-06-14 13:50:00.619463
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    import os
    import subprocess
    from time import sleep
    from tempfile import NamedTemporaryFile
    from .utils import FileGenerator, FileReader

    mw = MonoWorker()
    # Test replace waiting job
    fg = FileGenerator()
    fr = FileReader()
    with NamedTemporaryFile() as ft:
        mw.submit(fg.generate, filename=ft.name, size=3)
        sleep(0.1)
        mw.submit(fr.read, filename=ft.name)
        sleep(0.1)
        mw.submit(fr.read, filename=ft.name)
        sleep(0.1)
        mw.submit(fg.generate, filename=ft.name, size=5)
        sleep(0.5)

# Generated at 2022-06-14 13:50:07.890478
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    mw = MonoWorker()
    results = [0, 0, 0]

    def f(i):
        time.sleep(0.2)
        results[i] += 1
        time.sleep(0.2)
        results[i] += 2
        time.sleep(0.2)
        results[i] += 4
        time.sleep(0.2)
        results[i] += 8

    # all work is done in the same order
    mw.submit(f, 0)
    mw.submit(f, 1)
    mw.submit(f, 2)
    mw.submit(f, 0)
    mw.submit(f, 1)
    mw.submit(f, 2)
    mw.submit(f, 0)

# Generated at 2022-06-14 13:50:32.294668
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import time
    from unittest import TestCase
    from unittest.case import SkipTest

    from ..utils import _term_move_up

    class TestMonoWorker(TestCase):
        def test_MonoWorker(self):
            def f(t):
                [time() for _ in range(10 ** 8)]
                return "done:" + t

            mono = MonoWorker()

            # submit running
            t1 = time()
            running = mono.submit(f, 'hello')
            self.assertEqual(running.result(), "done:hello")
            t2 = time()
            # submit waiting
            waiting = mono.submit(f, 'world')
            self.assertEqual(waiting.result(), "done:world")
            t3 = time()
            # submit waiting again
            waiting

# Generated at 2022-06-14 13:50:42.092500
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def func_a():  # pragma: no cover
        time.sleep(3)
        return "func_a"

    def func_b():  # pragma: no cover
        time.sleep(1)
        return "func_b"

    def func_c():  # pragma: no cover
        time.sleep(2)
        return "func_c"

    mw = MonoWorker()
    fa = mw.submit(func_a)
    time.sleep(0.2)
    fb = mw.submit(func_b)
    time.sleep(0.2)
    fc = mw.submit(func_c)
    time.sleep(0.2)
    assert fc == mw.submit(func_c)
    fb.result()
    assert fa

# Generated at 2022-06-14 13:50:49.891944
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import unittest
    # noinspection PyPep8Naming
    class Test(unittest.TestCase):
        def test_MonoWorker_submit(self):
            results = []
            nums = [1, 2, 3, 4, 5]

            def work(x):
                time.sleep(1)
                results.append(x)

            this = MonoWorker()
            this.submit(work, nums[0])
            this.submit(work, nums[1])
            this.submit(work, nums[2])
            this.submit(work, nums[3])
            this.submit(work, nums[4])
            self.assertEqual(results, [nums[-1]])


# Generated at 2022-06-14 13:50:56.293802
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> import time
    >>> mw = MonoWorker()
    >>> assert len(mw.futures) == 0
    >>> waiting = mw.submit(time.sleep, 0.1)
    >>> assert len(mw.futures) == 1
    >>> waiting.result() is None
    >>> running = mw.submit(time.sleep, 0.1)
    >>> assert len(mw.futures) == 1  # waiting is replaced
    >>> running.result() is None
    >>> for i in range(6):
    ...     mw.submit(time.sleep, 0.1)

    """
    # This docstring is used as a unit test (see `test_MonoWorker_submit`)
    # as well as documentation.



# Generated at 2022-06-14 13:51:07.106203
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    pool = MonoWorker()

    def long_task():
        sleep(2)
        return 42

    def short_task():
        sleep(1)
        return 42

    # Submit done
    assert pool.submit(long_task).result() == 42

    # Submit overrunning
    pool.submit(long_task).result()
    assert pool.submit(short_task).result() == 42

    # Submit waiting
    pool.submit(long_task).result()
    assert pool.submit(long_task).result() == 42
    assert pool.submit(short_task).result() == 42

    # Submit cancel
    assert pool.submit(long_task).result() == 42
    assert pool.submit(long_task).result() == 42
    assert pool.submit(short_task).cancel()

# Generated at 2022-06-14 13:51:17.634392
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test case 1: submit function with long running time."""
    import time
    func = lambda x, y: time.sleep(x) or y
    worker = MonoWorker()
    future = worker.submit(func, 3, 1)
    time.sleep(1)
    # get the result
    assert future.result() == 1
    # submit another request
    future = worker.submit(func, 3, 2)
    # submit another request which would be discarded
    future = worker.submit(func, 3, 3)
    # submit another request, then the previous one would be discarded
    future = worker.submit(func, 3, 4)
    # get the result
    assert future.result() == 4
    # submit a request will no longer be discarded
    future = worker.submit(func, 3, 5)
    # get the result


# Generated at 2022-06-14 13:51:23.332395
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Unit test for method submit of class MonoWorker"""
    from time import sleep
    from random import random

    def time_sleep(n):
        sleep(n)
        return n

    mw = MonoWorker()
    for i in tqdm_auto(range(4)):
        mw.submit(time_sleep, random())
        sleep(0.5)

# Generated at 2022-06-14 13:51:30.072187
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def sleep_and_return(t):
        from time import sleep
        sleep(t)
        return t

    mono = MonoWorker()
    from multiprocessing import cpu_count
    num_workers = cpu_count()
    for i in tqdm_auto.tqdm(range(4 * num_workers + 1), desc="submit", mininterval=0.1):
        mono.submit(sleep_and_return, i)
    mono.pool.shutdown()



# Generated at 2022-06-14 13:51:39.956302
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import unittest
    from collections import deque
    from unittest import TestCase

    class TestMonoWorkerSubmit(TestCase):
        __test__ = True

        def sleep_func(self, seconds):
            time.sleep(seconds)

        def test_submit(self):
            mw = MonoWorker()
            func = self.sleep_func

            d1 = mw.submit(func, 1)
            d2 = mw.submit(func, 2)
            d3 = mw.submit(func, 3)

            # Only d3 is waiting
            self.assertIs(mw.futures.pop(), d3)

            d4 = mw.submit(func, 4)
            d5 = mw.submit(func, 5)

            # Only d5 is waiting
            self

# Generated at 2022-06-14 13:51:48.624414
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def exec_sleep(n):
        time.sleep(n)
        return str(n)

    mono_worker = MonoWorker()
    # Submit two tasks.
    r1 = mono_worker.submit(exec_sleep, 2)
    r2 = mono_worker.submit(exec_sleep, 1)
    # r3 will discard r1 because r1 is the previous task submitted before r2.
    r3 = mono_worker.submit(exec_sleep, 3)
    # r4 will discard r2 because r2 is the previous task submitted before r3.
    r4 = mono_worker.submit(exec_sleep, 4)
    # Verify result.
    assert r1.cancelled() and r2.cancelled()
    assert not r3.cancelled() and not r4.cancelled()


# Generated at 2022-06-14 13:52:25.616627
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from six.moves import xrange as range
    import time

    def f(i):
        time.sleep(.01)
        return i

    mw = MonoWorker()
    lst = []
    for i in range(10):
        lst.append(mw.submit(f, i))
    time.sleep(.05)
    lst.append(mw.submit(f, 10))
    time.sleep(.2)
    assert lst[-1].result() == 10
    assert lst[-2].cancelled()
    lst.append(mw.submit(f, 11))
    time.sleep(.2)
    assert lst[-2].result() == 11
    assert lst[-3].cancelled()
    for i in range(10):
        assert l

# Generated at 2022-06-14 13:52:33.621033
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import FreezableIterable
    m = MonoWorker()
    print("** running")
    for i in range(1, 11):
        tqdm_auto.write("{}: {}".format(i, m.submit(time.sleep, .1).result()))
    print("** waiting")
    for i in range(1, 11):
        tqdm_auto.write("{}: {}".format(
            i, m.submit(time.sleep, .1).result()))

    print("\n** running")
    for i in range(1, 11):
        tqdm_auto.write("{}: {}".format(
            i, m.submit(time.sleep, .1).result()))
    print("** freezing")