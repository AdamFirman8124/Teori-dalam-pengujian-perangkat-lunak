

# Generated at 2022-06-14 13:42:46.948782
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    for i in tqdm_auto.trange(3, desc="A"):
        mw.submit(time.sleep, .1)
    for i in tqdm_auto.trange(3, desc="B"):
        mw.submit(time.sleep, .1)

# Generated at 2022-06-14 13:42:54.470743
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from multiprocessing import Manager, Process
    from threading import Event, Thread

    from ..utils import _decode

    with Manager() as manager:
        results = manager.list()
        worker = MonoWorker()

        def func_write(q):
            @worker.submit
            def write_task(arg):
                # time.sleep(0.1)
                q.append(arg)
            for i in range(10):
                write_task(i)

        def func_read(q, r, stop=None):
            @worker.submit
            def read_task():
                try:
                    r.append(q.pop())
                except IndexError:
                    pass
            while stop is None or not stop.is_set():
                read_task()
                time.sleep(0.1)

       

# Generated at 2022-06-14 13:43:04.803464
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event
    def time_consuming_task(evt, ms=2000):
        evt.wait(2)
        return ms
    import tqdm
    evts = [Event() for _ in range(2)]
    MW = MonoWorker()
    for evt in evts:
        future = MW.submit(time_consuming_task, evt)
        assert future.result(1) == 2000
    print("\n")
    # Test cancellation
    evts = [Event() for _ in range(2)]
    def countdown(evt, ms=2000):
        evt.wait(2)
        for _ in tqdm.tqdm(range(ms)):
            sleep(0.002)

# Generated at 2022-06-14 13:43:14.719517
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep, time
    from threading import Lock
    def time_nano():
        """Return nanoseconds since epoch."""
        return int(1e9 * time())
    def sleep_nano(t):
        """"""
        sleep(1e-9 * t)
    lock = Lock()
    m = MonoWorker()
    assert m.submit(sleep_nano, 1e9), RejectableFuture()
    assert m.submit(sleep_nano, 1e9), RejectableFuture()

    def t0():
        """Task 0"""
        with lock:
            start = time_nano()
            assert m.submit(sleep_nano, 1e9)
            end = time_nano()
        return start, end

    def t1():
        """Task 1"""

# Generated at 2022-06-14 13:43:24.110451
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from testserver import TestServer

    def doit(m, seed):
        sleep(2)
        return seed * 2

    M = MonoWorker()

    ts = TestServer(lambda *args, **kwargs: print("doit:", args[0], args[1]))
    ts.start()

    for i in tqdm_auto.trange(5, desc="outer"):
        M.submit(ts.run, doit, i)
        sleep(0.5)

    # Since doit() takes 2s to run, we should see two
    # numbers printed every 2s, until the 10th and final number
    # is printed after 4s. Each number is a multiple of two and
    # corresponds to the input values i.



# Generated at 2022-06-14 13:43:32.357055
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    import multiprocessing
    from concurrent.futures import CancelledError
    from concurrent.futures import TimeoutError
    from concurrent.futures import Future

    def func_ret(x):
        time.sleep(x)
        return x

    def func_none(x):
        time.sleep(x)
        return None

    def func_err(x):
        time.sleep(x)
        raise Exception

    # Test "one at a time"
    mw = MonoWorker()
    assert len(mw.futures) == 0
    mw.submit(func_ret, 0.2)
    assert len(mw.futures) == 1

# Generated at 2022-06-14 13:43:42.751195
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys

    def get_time():
        return time.time()
    func = get_time

    # test case 0: no submit
    monoWorker = MonoWorker()
    time.sleep(1)  # 1
    assert monoWorker.futures == deque()

    # test case 1: submit
    monoWorker.submit(func)
    time.sleep(1)  # 2
    assert monoWorker.futures == deque([], 2)

    # test case 2: submit then get
    monoWorker.submit(func)
    time.sleep(1)  # 3
    assert monoWorker.futures.pop().result() < get_time()

    # test case 3: submit twice then get
    monoWorker.submit(func)

# Generated at 2022-06-14 13:43:51.963144
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import itertools
    import random
    import string
    from time import sleep

    class fakerunner(object):
        def __init__(self, msg, delay):
            self.msg = msg
            self.delay = delay

        def __call__(self, *args, **kwargs):
            sleep(self.delay)
            print(self.msg)

    length = 2
    delay = 0.1
    msg_gen = (''.join(random.sample(string.ascii_letters, 8)) for _ in
               itertools.count())
    runner_gen = (fakerunner(next(msg_gen), delay) for _ in itertools.count())

    worker = MonoWorker()
    for _ in range(length):
        worker.submit(next(runner_gen))
    sleep(delay)

# Generated at 2022-06-14 13:44:01.513987
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import errno
    import os
    import socket
    import subprocess
    import sys
    import time

    def normal_executor(func, *args, **kwargs):
        return func(*args, **kwargs)

    def kill_switch(func, *args, **kwargs):
        raise OSError(errno.ESRCH, "Keep calm, I am a fake exception.")

    def a_sleep(duration):
        time.sleep(duration)
        return True

    def open_many_fds(n=10):
        return [os.open(__file__, os.O_RDONLY) for _ in range(n)]

    def socket_connection(addr):
        s = socket.socket()
        s.connect(addr)
        return s.recv(100)


# Generated at 2022-06-14 13:44:09.229377
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .statistics_ import Statistics
    import gc
    for gc_status in [True, False]:
        for the_end in [True, False]:
            mw = MonoWorker()
            s = Statistics()
            for i in range(1000):
                if len(mw.futures) != 1:
                    s.add(1, i)
            mw_submit = lambda: mw.submit(sleep, 0)
            for i in range(1000):
                if gc_status and not i % 10:
                    gc.collect()
                mw_submit()
            for j in range(1000):
                if len(mw.futures) != 1:
                    s.add(2, j)

# Generated at 2022-06-14 13:44:20.148683
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from ..auto import tqdm as tqdm_auto
    from time import sleep
    from timeit import default_timer as clock
    from itertools import repeat

    mw = MonoWorker()

    def foo(i):
        sleep(1)
        return i

    def bar(i):
        sleep(2)
        return i

    def baz(i):
        sleep(3)
        return i

    _, now = clock(), clock()
    for i in tqdm_auto(range(3)):
        # starts 3, 2, 3
        mw.submit(foo, i)
        sleep(0.1)
    mw.submit(lambda: None)  # to clear waiting task

    for i in range(5):
        mw.submit(bar, i)  # starts 5, clears 3,

# Generated at 2022-06-14 13:44:29.960628
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randrange

    RESULT_SIZE = 10000
    SLEEP_MAX = 1000
    ITR = 1000

    results = dict([])

    def _submit_check(results, index, worker, wait_time):
        sleep(wait_time / 1000.0)
        results[index] = wait_time

    worker = MonoWorker()

    # Test if results are correct
    def _test_correct(results, pos):
        lst = [x for x in results]
        assert len(lst) == pos
        sleep(randrange(SLEEP_MAX) / 1000.0)
        for i in range(pos):
            assert worker.futures[i].result() == results[i]

    # Test if there are no extra results

# Generated at 2022-06-14 13:44:40.609951
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    result = []
    for i in range(1, 5):
        result.append("Started " + str(i) + "!")
        time.sleep(i)
        result.append("Finished " + str(i) + "!")
    def func():
        for i in range(1, 5):
            result.append("Started " + str(i) + "!")
            time.sleep(i)
            result.append("Finished " + str(i) + "!")
    def test():
        mw = MonoWorker()
        mw.submit(func)
        mw.submit(func)
        return mw.futures
    mw_future = []

# Generated at 2022-06-14 13:44:50.185777
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    m = MonoWorker()
    print("Submitting task 1 to MonoWorker...")
    f1 = m.submit(time.sleep, 2)
    print("Submitting task 2 to MonoWorker...")
    f2 = m.submit(time.sleep, 2)
    print("Submitting task 3 to MonoWorker...")
    f3 = m.submit(time.sleep, 2)
    print("Submitting task 4 to MonoWorker...")
    f4 = m.submit(time.sleep, random.randint(2, 5))
    print("All tasks submitted.")
    f1.result(), f2.result(), f3.result(), f4.result()
    print("All tasks done.")

# Generated at 2022-06-14 13:44:57.356257
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from random import random
    from time import sleep
    from tqdm import tqdm

    def f(a, t=1):
        sleep(t)
        return a

    mw = MonoWorker()
    mw.submit(f, 0)
    mw.submit(f, 1)
    mw.submit(f, 2)
    mw.submit(f, 3)
    for _ in tqdm(range(4)):
        mw.submit(f, random() * 10, t=random() * .5)
    res = list(mw.futures)
    sleep(1)
    assert all(r.done() for r in res)

# Generated at 2022-06-14 13:45:08.682582
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import threading

    result = []
    def run(i):
        time.sleep(.01 * random.uniform(.5, 2))
        result.append(i)
    import six
    if six.PY2:
        def _input(msg):
            return raw_input(msg).lower()
    else:
        def _input(msg):
            return input(msg).lower()

    mw = MonoWorker()
    for i in range(5):
        mw.submit(run, i)
        time.sleep(.01 * random.uniform(.5, 2))
    _input("Check result on console (may be out of order)")
    _input("Press Enter to cancel tasks")
    mw.pool.shutdown(wait=False)

# Generated at 2022-06-14 13:45:17.869614
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, random
    from threading import RLock
    from concurrent.futures import TimeoutError

    def echo(x):
        time.sleep(random.random())
        return x

    num_futures = 2
    mw = MonoWorker()

    lock = RLock()
    with tqdm_auto.tqdm(total=num_futures) as pbar:
        for i in range(num_futures):
            mw.submit(lock.acquire)
            try:
                mw.submit(echo, i, timeout=1e-6).result()
            except TimeoutError:
                pass
            pbar.update(1)
            lock.release()

# Generated at 2022-06-14 13:45:28.984573
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import Lock, Value
    import re

    def f(lock, val):
        lock.acquire()
        if val.value == 0:
            val.value = int(val.value + 1)
            lock.release()
            sleep(2)
        elif val.value == 1:
            val.value = int(val.value + 1)
            lock.release()
            sleep(3)
            return

    # Create a MonoWorker and locks, etc.
    mono = MonoWorker()
    lock = Lock()
    val = Value('i', 0)
    # Now execute the test
    fut1 = mono.submit(f, lock, val)
    fut2 = mono.submit(f, lock, val)
    fut3 = mono.submit(f, lock, val)

# Generated at 2022-06-14 13:45:39.495391
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def callback():
        sleep(0.1)
        return 1

    mw = MonoWorker()

    assert mw.futures == []
    assert not mw.futures

    f1 = mw.submit(callback)
    assert not f1.done()
    # assert f1.result() == 1  # blocks

    f2 = mw.submit(callback)
    assert not f2.done()
    # assert f2.result() == 1  # blocks
    assert not f1.done()
    # assert f1.result() == 1  # blocks

    f3 = mw.submit(callback)
    assert not f3.done()
    assert not f1.done()
    assert not f2.done()

    sleep(0.2)

    assert f3.done

# Generated at 2022-06-14 13:45:51.665628
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test MonoWorker.submit."""
    import time
    from multiprocessing import Value, Lock
    from random import randint

    class Futures(object):
        def __init__(self):
            self.maxlen = 2
            self.queue = []
            self.lock = Lock()

        def append(self, x):
            with self.lock:
                self.queue.append(x)

        def popleft(self):
            with self.lock:
                return self.queue.pop(0)

        def __len__(self):
            return len(self.queue)

    class Future(object):
        def __init__(self, val):
            self.val = val
            self.is_done = Value('i', 0)
            self.is_cancelled = Value('i', 0)



# Generated at 2022-06-14 13:46:00.694550
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .test_examples import _reader
    from time import sleep

    print('\nTest `MonoWorker.submit`:')
    w = MonoWorker()
    for i in tqdm_auto.tqdm(range(4), desc='test', unit='test'):
        w.submit(sleep, 1)
    with _reader(filename=__file__) as r:
        w.submit(yield_line_widths, r)

# Generated at 2022-06-14 13:46:09.417088
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import multiprocessing as mp
    from ..utils import _range

    def wait(n):
        time.sleep(n)
        return 'done' + str(n)

    mw = MonoWorker()
    assert mw.submit(wait, 10) is not None
    assert mw.futures[0].result() == 'done10'
    assert mw.futures[0].done() is True
    assert mw.submit(wait, 20) is not None
    assert mw.futures[0].cancel()

    # Test IO re-insertion
    for i in _range(4):
        assert mw.submit(wait, i) is not None
    assert mw.futures[0].result() == 'done3'
    # Test MP re-insertion
   

# Generated at 2022-06-14 13:46:18.550180
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from concurrent.futures import as_completed, TimeoutError
    from random import uniform

    def wait_then_return(seconds, value):
        time.sleep(seconds)
        return value

    mw = MonoWorker()
    f2 = mw.submit(wait_then_return, 2, 2)
    try:
        f1 = mw.submit(wait_then_return, 1, 1)
    except Exception as e:
        print("f1 failed:", e)
    else:
        print("f1 not failed")
    print("f2 done:", f2.done())
    for f in as_completed(mw.futures, 1):
        if f == f2:
            print("f2 timed out")
            break

# Generated at 2022-06-14 13:46:26.908890
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep, time
    from random import random

    def worker(seconds):
        sleep(seconds)
        return seconds, time()

    mw = MonoWorker()
    delays = list(range(3))

    total_delay = sum(delays)
    t0 = time()
    for delay in delays:
        mw.submit(worker, delay)
    print('Total delay: {}s'.format(delays))
    for future in mw.futures:
        print('Future: {}s, {}'.format(*future.result()))
    t1 = time()
    print('Elapsed: {}s, diff: {}s'.format(t1 - t0, t1 - t0 - total_delay))

if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:46:35.472445
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import numpy as np
    from concurrent.futures import (as_completed,
                                    wait,
                                    thread as ThreadPoolExecutor)
    mw = MonoWorker()
    n = 6
    futures = []
    for i in range(n):
        def f(t=i):
            time.sleep(np.random.rand(1) * 2)
            return 'done iteration {}'.format(t)
        futures.append(mw.submit(f))
    for future in as_completed(futures):
        print(future.result())
    print('now:')
    for future in futures:
        print(future.result())

# Also can be run from the command line with:
# ```bash
# python -c "import tqdm.contrib as tc; tc.

# Generated at 2022-06-14 13:46:45.774710
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Initialize
    from multiprocessing.pool import ThreadPool  # Use old ThreadPool to avoid clobbering global one
    from time import sleep
    from tqdm import tqdm

    def f(x):
        sleep(.01)
        return x**2
    pool = ThreadPool(1)
    f1 = pool.apply_async(f, [1])
    f2 = pool.apply_async(f, [2])
    assert not f1.ready()  # pylint: disable=no-member
    assert not f2.ready()  # pylint: disable=no-member
    assert f1.get() == 1  # pylint: disable=no-member
    assert f2.get() == 4  # pylint: disable=no-member


# Generated at 2022-06-14 13:46:52.362576
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(x):
        """Sleeps for approximate given time"""
        time.sleep(x)
        return x

    mono = MonoWorker()
    future_first = mono.submit(func, 3.0)
    time.sleep(1)
    future_second = mono.submit(func, 1.0)
    time.sleep(1)
    future_third = mono.submit(func, 1.0)
    result_first = future_first.result()
    result_second = future_second.result()
    try:
        result_third = future_third.result()
        assert False
    except Exception as e:
        assert "cancelled" in str(e)
    assert result_first == 3.0
    assert result_second == 1.0



# Generated at 2022-06-14 13:47:02.828278
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mono = MonoWorker()
    assert mono.pool._threads  # pylint: disable=W0212
    assert not mono.futures
    running = mono.submit(time.sleep, 0.004)
    assert mono.pool._threads  # pylint: disable=W0212
    assert len(mono.futures) == 1
    assert running.done()
    waiting = mono.submit(time.sleep, 0.002)
    assert mono.pool._threads  # pylint: disable=W0212
    assert len(mono.futures) == 1
    assert not waiting.done()
    running.result()
    assert mono.pool._threads  # pylint: disable=W0212
    assert len(mono.futures) == 1
    assert waiting

# Generated at 2022-06-14 13:47:12.355006
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import logging
    logging.basicConfig(level=logging.DEBUG)
    mw = MonoWorker()
    def f(queue, n):
        time.sleep(n)
        queue.append(n)
    import queue
    q = queue.Queue()
    mw.submit(f, q, 0.5)
    mw.submit(f, q, 0.2)  # should replace 0.5
    mw.submit(f, q, 0.1)  # should discard
    mw.submit(f, q, 0.4)  # should replace 0.2
    mw.submit(f, q, 0.1)  # should discard
    mw.submit(f, q, 0.6)  # should discard (both 0.4 and 0.2 are running)
    mw

# Generated at 2022-06-14 13:47:23.497070
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from os import remove
    from tempfile import NamedTemporaryFile
    from time import sleep

    def writer(filename, string):
        sleep(.1)
        with open(filename, "w+") as f:
            f.write(string)

    f = NamedTemporaryFile(mode='w+', delete=False)
    mw = MonoWorker()
    fname = f.name
    mw.submit(writer, fname, "test_test")
    remove(fname)
    mw.submit(writer, fname, "test_test2")

    try:
        mw.submit(writer, f.name, "test_test3")
    except BrokenPipeError:
        pass
    else:
        raise Exception("BrokenPipeError expected")

# Generated at 2022-06-14 13:47:41.537329
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(a, p=1, q=1, r=1):
        import time
        time.sleep(a)
        return a, p, q, r
    mw = MonoWorker()
    f = mw.submit(func, 2, r=3)
    f = mw.submit(func, 5, p=7, q=8)
    f = mw.submit(func, 3, p=11, r=13)
    f = mw.submit(func, 7, r=17, q=19)
    assert f.result() == (7, 11, 19, 17)
if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:47:52.269530
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import random
    import numpy as np

    def threaded_sleep(barrier, sleep_time=0.1, standard_deviation=0.01):
        """ Sleep for some time, with a bit of randomness
        # Parameters
            barrier: deterministic and reproducible randomness
            sleep_time: the time to sleep
            standard_deviation: parameter that determins the randomness
        """
        sleep(sleep_time * (1+np.random.normal(scale=standard_deviation)))

    ####

    def test_not_crashing():
        import tqdm
        w = MonoWorker()
        sleep_time = 1

        def submit_threaded_sleep(barrier, sleep_time=sleep_time):
            return w.submit(threaded_sleep, barrier, sleep_time)

       

# Generated at 2022-06-14 13:48:03.117894
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..tests.common import with_setup

    def sleeping_function_0():
        time.sleep(1)
        return 0

    def sleeping_function_1():
        time.sleep(1)
        return 1

    def sleeping_function_2():
        time.sleep(1)
        return 2

    mono_worker = MonoWorker()

    # Testing that function is actually executed
    assert mono_worker.submit(sleeping_function_0).result() == 0

    # Testing that only one function is executed
    waiting_future = mono_worker.submit(sleeping_function_1)
    assert sleeping_function_2() == 2  # function is not executed

    # Testing that a waiting task is replaced if another task is submitted
    waiting_future = mono_worker.submit(sleeping_function_2)

# Generated at 2022-06-14 13:48:10.564001
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    import multiprocessing as mp
    # import random
    import threading as td
    import time

    def proc_fn():
        time.sleep(0.2)

    def multiproc_fn(i):
        time.sleep(0.2)
        return i

    def thread_fn(i):
        time.sleep(0.1)
        return i

    worker = MonoWorker()
    assert len(worker.futures) == 0

    worker.submit(proc_fn)
    assert len(worker.futures) == 1
    worker.submit(proc_fn)  # waiting
    assert len(worker.futures) == 2

    for _ in range(4):
        worker.submit(proc_fn)  # only the last waiting in future
    assert len(worker.futures) == 2



# Generated at 2022-06-14 13:48:14.987080
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from functools import partial

    def do_print(x, sleep_duration=0.01):
        sleep(sleep_duration)
        return x

    mw = MonoWorker()
    for i in range(5):
        mw.submit(partial(do_print, (i, i * 2)))
    # TODO: test the replacement
    pass

# Generated at 2022-06-14 13:48:25.364897
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from collections import deque

    def mock_future(*args, **kwargs):
        return _MockFuture(*args, **kwargs)

    def func_running():
        time.sleep(1)
        return 'running'

    def func_waiting():
        time.sleep(1)
        return 'waiting'

    def func_quick():
        return 'quick'

    # Test with just running future
    mono = MonoWorker()
    assert len(mono.futures) == 0
    waiting = mono.submit(func_waiting)
    assert len(mono.futures) == 1
    running = mono.submit(func_running)
    assert len(mono.futures) == 1
    assert mono.futures[0] is running

    # Test with quick future
   

# Generated at 2022-06-14 13:48:34.692423
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from queue import Queue
    from time import sleep
    from threading import Thread

    q = Queue()

    def job(job_id, duration, result_queue):
        sleep(duration)
        result = str(job_id) * duration
        result_queue.put(result)

    def test(durations):
        mpw = MonoWorker()
        q.queue.clear()
        futures = []
        for i, d in enumerate(durations):
            f = mpw.submit(job, i, d, q)
            futures.append(f)

        t1 = Thread(target=q.get)
        t2 = Thread(target=q.get)
        t1.start()
        t2.start()

        for f in futures:
            f.result()
        t1.join()
       

# Generated at 2022-06-14 13:48:42.349504
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    
    def f(a ,b):
        return a*b
    mono = MonoWorker()
    print(mono.futures)
    mono.submit(f,1,2)
    print(mono.futures)
    mono.submit(f,2,2)
    print(mono.futures)
    mono.submit(f,3,2)
    print(mono.futures)
    mono.submit(f,4,2)
    print(mono.futures)
    mono.submit(f,5,2)
    print(mono.futures)

if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:48:51.420617
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from math import sqrt
    from time import sleep
    from datetime import timedelta
    from concurrent.futures import as_completed
    from ..utils import _range as trange

    mw = MonoWorker()

    # Concurrent iteration
    for i in trange(10, desc='MonoWorker'):
        if i > 5:
            sleep(0.2)
        mw.submit(sqrt, i)

    # Concurrent map
    mw = MonoWorker()
    result = [None] * 10
    futures = mw.submit(lambda x: (x, sleep(0.2 - x / 10)),
                        *range(10))  # returns list of futures


# Generated at 2022-06-14 13:48:53.652111
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    worker = MonoWorker()
    worker.submit(sum, range(10 ** 5))
    worker.submit(sum, range(10 ** 5))
    worker.submit(sum, range(10 ** 5))

# Generated at 2022-06-14 13:49:19.150273
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import unittest
    import multiprocessing
    try:
        import queue
    except ImportError:
        import Queue as queue
    from tqdm.contrib.concurrency import MonoWorker

    class Test_MonoWorker(unittest.TestCase):
        def setUp(self):
            self.worker = MonoWorker()
            self.results = []

        def test_MonoWorker_submit(self):
            def func(num):
                time.sleep(random.random())
                self.results.append(num)
                return num

            self.worker.submit(func, 0)
            time.sleep(0.2)
            self.worker.submit(func, 1)
            time.sleep(0.2)

# Generated at 2022-06-14 13:49:30.283942
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from concurrent.futures import Future

    def func(n):
        time.sleep(n)
        return n

    worker = MonoWorker()
    for i, n in enumerate([1.1, 2.1, 2.6, 4.0, 2.8, 2.1, 2.6, 2.0, 2.8]):
        fut = worker.submit(func, n)
        # print("i {} n {} fut {} result {}".format(i, n, fut, fut.result()))
        assert isinstance(fut, Future)

    # print("future results: {}".format([fut.result() for fut in worker.futures]))
    assert all(isinstance(fut, Future) for fut in worker.futures)

# Generated at 2022-06-14 13:49:39.076494
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import _supports_unicode

    def test_func(task_id, sleep_time, result="done"):
        time.sleep(sleep_time)
        return '{} {}'.format(task_id, result)

    tasks = [
        (1, 0.3, "done"),
        (2, 0.2, "done"),
        (3, 0.1, "error", "error"),  # should raise an exception
        (4, 0.2, "done"),
        (5, 0.1, "done"),
        (6, 0.0, "done"),
        (7, 0.1, "error", "error")
    ]

    # Preliminary test to print on stderr
    for task in tasks:
        result = test_func(*task)

# Generated at 2022-06-14 13:49:49.361934
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys
    import threading
    from queue import Queue
    from concurrent.futures import TimeoutError

    if sys.version_info[:2] < (3, 4):
        raise ImportError("requires Python >= 3.4")

    class DelayedOutputStream(object):
        def __init__(self, delegate, delay):
            self._delegate = delegate
            self._delay = delay
            self._queue = Queue()
            self._thread = threading.Thread(target=self._writer)
            self._thread.daemon = True
            self._thread.start()

        def _writer(self):
            while True:
                msg = self._queue.get()
                if not msg:
                    break
                time.sleep(self._delay)
                self._delegate.write(msg)

       

# Generated at 2022-06-14 13:49:59.385997
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def _err(*args, **kw):
        raise ValueError('FAILED')
    def _echo(*args, **kw):
        return args, kw

    # test calls that raise exception
    mw = MonoWorker()
    mw.submit(_err)
    assert not mw.pool._threads
    mw.submit(_err)
    assert not mw.pool._threads

    # test calls that return
    mw = MonoWorker()
    assert mw.submit(_echo, 1, 2, a=3, b=4) == ((1, 2), {'a': 3, 'b': 4})
    assert mw.pool._threads

# Generated at 2022-06-14 13:50:07.252716
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def slow_func(wait):
        time.sleep(wait)
        return "done in {}".format(wait)

    worker = MonoWorker()
    assert worker.submit(slow_func, 0.5)
    assert worker.submit(slow_func, 0.1)
    assert worker.submit(slow_func, 1)
    assert worker.submit(slow_func, 0.1)
    assert worker.submit(slow_func, 0.3)
    assert worker.submit(slow_func, 0.1)
    assert worker.submit(slow_func, 0.5)
    assert worker.submit(slow_func, 0.1)
    assert worker.submit(slow_func, 1)
    assert worker.submit(slow_func, 0.3)

# Generated at 2022-06-14 13:50:16.345197
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .simpledisplay import SimpleDisplay
    from .utils import _write

    with SimpleDisplay() as disp:
        disp.write('test_MonoWorker_submit\n')
        worker = MonoWorker()
        sleep_time = 0.2
        _write(disp, 'first passing\n')
        worker.submit(sleep, sleep_time)
        sleep(sleep_time/2)
        _write(disp, 'second passing\n')
        worker.submit(sleep, sleep_time)
        sleep(sleep_time * 3/2)
        _write(disp, 'third passing\n')
        worker.submit(sleep, sleep_time)
        sleep(sleep_time * 5/2)
        _write(disp, 'fourth passing\n')

# Generated at 2022-06-14 13:50:26.712658
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def pop_leftmost(q):
        if len(q) < 1:
            return None
        else:
            return q.popleft()

    def push_rightmost(q, x):
        if len(q) >= q.maxlen:
            return
        q.append(x)

    def test_helper(timing_list, futures_list):
        mw = MonoWorker()
        futures_maxlen = mw.futures.maxlen
        N = len(timing_list)
        assert len(futures_list) >= N
        assert len(futures_list) <= futures_maxlen
        for n in range(min(N, futures_maxlen)):
            mw.futures.append(futures_list[n])

# Generated at 2022-06-14 13:50:34.531703
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # pylint: disable-msg=missing-docstring

    def bad_func(*_args, **_kwargs):
        raise ValueError

    def good_func(*args, **kwargs):
        return args, kwargs

    worker = MonoWorker()
    assert worker.submit(bad_func, 1, 2, kwarg=7).exception() is not None
    assert worker.submit(bad_func, 1, 2, kwarg=7).exception() is not None
    assert worker.submit(good_func, 1, 2, kwarg=7).result() == ((1, 2), {'kwarg': 7})

# Generated at 2022-06-14 13:50:43.955447
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> from time import sleep
    >>> from tqdm import tqdm
    >>> def slow(x):
    ...     sleep(1)
    ...     return x
    >>> w = MonoWorker()
    >>> f1 = w.submit(slow, 1)
    >>> f2 = w.submit(slow, 2)
    >>> [f1.result(), f2.result()]  # f1 is discarded
    [2, 2]
    >>> f3 = w.submit(slow, 3)
    >>> [f2.result(), f3.result()]  # f2 is discarded
    [3, 3]
    >>> f4 = w.submit(slow, 4)
    >>> [f3.result(), f4.result()]  # f3 is discarded
    [4, 4]
    """
    pass

# Generated at 2022-06-14 13:51:34.254320
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def f(x):
        time.sleep(x)
        return x

    m = MonoWorker()
    f1 = m.submit(f, 1)
    f2 = m.submit(f, 1)
    f3 = m.submit(f, 2)
    assert f1.done() and f2.result() == 1 and not f3.done()
    assert f3.result() == 2
    assert f1.result() == 1

    f4 = m.submit(f, 2)
    f5 = m.submit(f, 3)
    f6 = m.submit(f, 4)
    assert f4.done() and f5.result() == 3 and not f6.done()
    assert f6.result() == 4
    assert f5.result() == 3
    assert f4

# Generated at 2022-06-14 13:51:42.533401
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .test_tqdm_notebook import timeit
    from .tqdm import tqdm

    tqdm.monitor_interval = 0  # prevent auto monitor (forked from tqdm)

    def sleeper(delay, to_cancel=None):
        """Returns a `Future` with `result=5` after `delay` (seconds)"""
        delay = float(delay) / 1000
        if to_cancel:
            to_cancel.cancel()
        try:
            sleep(delay)
        except KeyboardInterrupt:
            tqdm_auto.write('\nInterrupted wait')
        return 5

    mw1 = MonoWorker()

    # submit a sleepy job
    f1 = mw1.submit(sleeper, 5000)
    assert not f1.done()

# Generated at 2022-06-14 13:51:50.028840
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from .itercounter import itercounter
    from threading import Event
    from ..utils import format_sizeof

    if tqdm_auto.get_instances(tqdm_auto.get_ipython()):
        tqdm_auto.write("Tests disabled due to IPython (issue #1188)")
        return

    tqdm_auto.write("Testing MonoWorker.submit() with fake itercounter generator (may take a while)")
    worker = MonoWorker()

    def print_time(n):
        print(" (%.1fs)" % (time.time() - start_time,))
        time.sleep(1)
        return n

    start_time = time.time()

# Generated at 2022-06-14 13:52:00.716122
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Python 2 and 3 compatible.
    """
    import time
    import sys
    if sys.version_info.major < 3:
        try:
            import queue
        except ImportError:
            import Queue as queue
    else:
        import queue

    queue = queue.Queue()

    def put(v, q=queue):
        try:
            q.put(v, timeout=2)
        except queue.Full:
            pass

    def get(q=queue):
        try:
            return q.get(timeout=2)
        except queue.Empty:
            return None

    def quick_func(i):
        put(i)
        return i

    def slow_func(i, delay=3):
        put(i)
        time.sleep(delay)
        return i

    mw = Mono

# Generated at 2022-06-14 13:52:08.055204
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event

    ev = Event()
    mw = MonoWorker()
    for i in range(4):  # 4th will just be discarded
        mw.submit(ev.wait)
    ev.set()
    assert not mw.futures[0].done()  # should still be running
    assert mw.futures[1].done()  # should have been cancelled

    mw.submit(ev.wait)
    mw.submit(ev.wait)
    assert len(mw.futures) == 2  # discard bad submit instead of wait
    mw.submit(ev.wait)
    assert all(f.done() for f in mw.futures)

# Generated at 2022-06-14 13:52:16.181095
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from itertools import count

    def slow_fib(n):
        sleep(1)
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a

    def print_counter(n):
        for _ in range(n):
            sleep(1)
            print(_)

    worker = MonoWorker()
    for i in count():
        if i == 0:
            worker.submit(print_counter, 3)
        elif i == 3:
            worker.submit(print_counter, 3)
        elif i == 6:
            worker.submit(print_counter, 3)
            break
        worker.submit(slow_fib, 10)
        sleep(1)
        print(worker.futures)

# Generated at 2022-06-14 13:52:26.349616
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import string
    import threading

    from ..utils import _range

    try:  # Python 2
        from Queue import Queue
    except ImportError:  # Python 3
        from queue import Queue
    try:  # Python 2
        from Queue import Empty as QueueEmptyException
    except ImportError:  # Python 3
        from queue import Empty as QueueEmptyException

    def random_string(string_length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in _range(string_length))


# Generated at 2022-06-14 13:52:34.060478
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randint, random
    from threading import Lock
    from qtpy.QtWidgets import QApplication, QLabel
    import sys

    def test_M():
        app = QApplication(sys.argv)
        label = QLabel()
        label.show()
        sys.exit(app.exec_())

    m = MonoWorker()
    m.submit(test_M)
    tqdm_auto.write('submitted')

    def a():
        sleep(1)
        tqdm_auto.write('a finished')
        sleep(1)
        return 'a finished'

    m.submit(a)
    tqdm_auto.write('submitted a')

    def b():
        sleep(0.6)

# Generated at 2022-06-14 13:52:43.661195
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    try:
        from multiprocessing import Process
    except ImportError:
        from multiprocessing.dummy import Process
    from time import sleep
    from queue import Queue
    from tqdm.contrib.concurrent import MonoWorker

    MW = MonoWorker()
    queue = Queue()

    def process_fun():
        queue.put(MW.submit(sleep, 0.01))
        queue.put(MW.submit(sleep, 0.03))
        queue.put(MW.submit(sleep, 0.02))
        queue.put(MW.submit(sleep, 0.06))

    process = Process(target=process_fun)
    process.start()
    process.join()

    futures = []
    while not queue.empty():
        futures.append(queue.get())
