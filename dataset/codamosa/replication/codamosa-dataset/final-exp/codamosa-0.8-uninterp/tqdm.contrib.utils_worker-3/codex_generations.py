

# Generated at 2022-06-14 13:42:50.768046
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from ..auto import tqdm
    from time import sleep

    def worker(delay, val):
        sleep(delay)
        return val

    mw = MonoWorker()

    # test long first
    f = mw.submit(worker, 0.5, 1)
    f2 = mw.submit(worker, 0.5, 2)

    # test short
    f3 = mw.submit(worker, 0.05, 3)

    # test re-entrance
    f4 = mw.submit(worker, 0.05, 4)

    # assert all(w in [f, f2, f3, f4] for w in mw.futures)
    assert f.result() == 1
    assert f2.result() == 2
    assert f3.result() == 3
    assert f4.result()

# Generated at 2022-06-14 13:42:59.909042
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def sleeper(t):
        time.sleep(t)
        return t
    mw = MonoWorker()
    mw.submit(sleeper, 1)
    mw.submit(sleeper, 2)
    assert mw.futures.maxlen == 2
    assert len(mw.futures) == 1
    mw.submit(sleeper, 3)
    assert len(mw.futures) == 1
    assert mw.futures[0].result() == 2
    mw.submit(sleeper, 4)
    assert len(mw.futures) == 1
    assert mw.futures[0].result() == 3

# Generated at 2022-06-14 13:43:11.451366
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def test():
        def count(i):
            return i

        def always_raise():
            raise RuntimeError('This should not occur')

        mono = MonoWorker()

        assert mono.pool._max_workers == 1

        assert mono.submit(count, 1).result() == 1
        assert len(mono.futures) == 1
        assert mono.submit(count, 2).result() == 2
        assert len(mono.futures) == 1
        from itertools import repeat
        for i in repeat(None, 3):
            assert mono.submit(count, i).result() == i
        assert len(mono.futures) == 1

        assert len(mono.futures) == 1
        assert mono.submit(always_raise) is None

# Generated at 2022-06-14 13:43:22.336209
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Lock
    import time
    def func(x):
        time.sleep(x)
        return x
    m = MonoWorker()
    assert len(m.futures) == 0
    assert(m.futures.maxlen == 2)  # default args
    f1 = m.submit(func, 2)
    assert len(m.futures) == 1
    f2 = m.submit(func, 1)
    assert len(m.futures) == 2
    f1.result()
    f2.result()
    f3 = m.submit(func, 1)
    f4 = m.submit(func, 3)
    f5 = m.submit(func, 1)
    assert f3 is None
    assert len(m.futures) == 1

# Generated at 2022-06-14 13:43:28.769405
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    tester = MonoWorker()
    tester.pool._max_workers = 2

    tmp = tester.submit(time.sleep, 0.1)
    tmp = tester.submit(time.sleep, 0.2)
    tmp = tester.submit(time.sleep, 0.3)
    tmp = tester.submit(time.sleep, 0.4)

    def my_fun(arg):
        return time.sleep(arg)
    tmp = tester.submit(my_fun, 0.5)
    tmp = tester.submit(my_fun, 0.6)

    # Test for exception
    tmp = tester.submit(random.choice, [])
    tmp = tester.submit(random.choice, [])

# Generated at 2022-06-14 13:43:40.114229
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from collections import defaultdict

    def delayed_print(x):
        time.sleep(0.1)
        print(x)

    count = defaultdict(int)

    worker = MonoWorker()
    for i in range(10):
        worker.submit(delayed_print, str(i) + 'a')
        worker.submit(delayed_print, str(i) + 'b')
        count[str(i) + 'b'] += 1
    for i in range(10, 20):
        worker.submit(delayed_print, str(i) + 'a')
        worker.submit(delayed_print, str(i) + 'b')
        count[str(i) + 'b'] += 1
    assert count['19b'] == 2
    assert count['19a'] == 1

# Generated at 2022-06-14 13:43:47.444609
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .demo import slow_incr
    from .concurr import barrier
    from ..utils import format_sizeof

    with barrier():
        worker = MonoWorker()
        for i in tqdm_auto.trange(10, desc='outer'):
            for j in tqdm_auto.trange(2, leave=False, desc='inner'):
                future = worker.submit(slow_incr, 0, format_sizeof(i, j))
                tqdm_auto.write('{} -> {}'.format(i, future.result()))

# Generated at 2022-06-14 13:43:55.509925
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import os
    import time
    import psutil
    from multiprocessing import current_process
    from ..utils import _environ_cols_wrapper, _range

    # Unit test for MonoWorker.submit
    def wait(secs):
        #time.sleep(0.01)
        #print(os.getpid())
        #print(psutil.Process(os.getpid()).children())
        time.sleep(secs)
        return secs

    def test(n_secs, secs_per_task=None, force_refresh=False,
             disable=False, leave=True, desc=None, max_workers=1, t_unit='s'):
        """Unit test for tqdm.MonoWorker"""

# Generated at 2022-06-14 13:44:04.065063
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import traceback

    # We define a function to test our worker,
    # it will run  2 seconds, then sleep 1 second
    def test_func():
        time.sleep(2)
        time.sleep(1)

    # General test
    # Generate one worker
    worker = MonoWorker()

    # Submit 6 jobs and get their futures
    futures = []
    for i in range(6):
        futures.append(worker.submit(test_func))

    # Wait for all futures to terminate, none should be canceled
    for fut in futures:
        try:
            fut.result()
        except:
            print("Traceback (most recent call last):")
            traceback.print_exc()
            assert False

    # Specific test for MonoWorker
    # Generate one worker
    worker = MonoWork

# Generated at 2022-06-14 13:44:12.475919
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from queue import Queue
    from threading import Event
    from unittest import TestCase

    def _test_func(q, event):
        try:
            q.put(None)
            event.wait()  # wait for the next job to come in
            q.put("job2")
        except Exception:
            import traceback
            q.put(traceback.format_exc())

    class _TestMonoWorker(TestCase):
        def test_empty(self):
            mono = MonoWorker()
            q = Queue()
            event = Event()
            mono.submit(_test_func, q, event)
            sleep(0.1)
            self.assertEqual(q.get(), None)
            q.put("job1")
            event.set()

# Generated at 2022-06-14 13:44:25.494937
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # create a GIL-less (multi-thread-friendly) future
    from concurrent.futures import Future
    from threading import Event
    done = Event()
    def setter():
        done.wait()
        return 3.2
    future = Future()
    future.set_running_or_notify_cancel()
    t = Thread(target=lambda: future.set_result(setter()))
    t.start()
    # test method submit of class MonoWorker
    worker = MonoWorker()
    assert worker.futures == deque([], 2)
    worker.submit(future.set_result, "done")
    assert worker.futures == deque([], 2)
    worker.submit(future.set_result, "done")
    assert worker.futures == deque([], 2)

# Generated at 2022-06-14 13:44:32.576139
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from subprocess import Popen, PIPE
    from time import sleep
    from os import path

    def task(x, waitms=100):
        sleep(waitms/1000.)
        return x

    # Test 1 -- this should error
    tqdm_auto.write("Test 1")
    mono = MonoWorker()
    mono.submit(task, 0.3, waitms=300)
    mono.submit(task, 0.2, waitms=200)
    mono.submit(task, 0.1, waitms=100)

    # Test 2 -- this should work
    tqdm_auto.write("Test 2")
    mono = MonoWorker()
    mono.submit(task, 0.3, waitms=300)
    mono.submit(task, 0.2, waitms=200)

# Generated at 2022-06-14 13:44:36.507331
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def do_task(sleep, idx):
        time.sleep(sleep)
        tqdm_auto.write("Task{0} finished".format(idx))
        return idx

    tqdm_auto.write("Submit first task")
    mw = MonoWorker()
    mw.submit(do_task, 1.0, 1)
    time.sleep(0.4)
    tqdm_auto.write("Submit second task")
    mw.submit(do_task, 0.5, 2)
    time.sleep(0.6)
    tqdm_auto.write("Submit third task")
    mw.submit(do_task, 0.8, 3)
    time.sleep(2.0)

if __name__ == '__main__':
    test_Mono

# Generated at 2022-06-14 13:44:47.152487
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randint
    mw = MonoWorker()
    count_start = 0
    count_stop = 0

    def start():
        nonlocal count_start
        count_start += 1
        sleep(randint(5, 10))

    def stop():
        nonlocal count_stop
        count_stop += 1
        sleep(randint(5, 10))

    mw.submit(start)
    mw.submit(stop)
    sleep(1)
    assert count_start == 0
    assert count_stop == 1
    mw.submit(start)
    sleep(1)
    assert count_start == 0
    assert count_stop == 1
    sleep(10)
    assert count_start == 1
    assert count_stop == 1

    # race condition check

# Generated at 2022-06-14 13:44:57.703802
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from platform import system
    from threading import Event
    from math import modf
    from concurrent.futures import TimeoutError

    def func(s):
        sleep(s)
        return s

    def check_MonoWorker_submit(waiting_time=.25, n_tasks=3,
                                sleep_time=.05, timeout=0.5):
        # Launch `n` tasks appearing in wrong order
        mw = MonoWorker()
        ev = Event()
        futs = [mw.submit(func, s) for s in sleep_time * n_tasks * 2 / 5]
        futs.append(mw.submit(ev.wait))  # blocks until after `ev.set()`
        sleep(waiting_time)
        ev.set()
       

# Generated at 2022-06-14 13:45:08.079637
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import time

    def func(x):
        time.sleep(random.random())
        return x + 1

    mw = MonoWorker()
    aysnc_results = [mw.submit(func, i) for i in range(10)]
    for r in aysnc_results:
        r.wait()

    # Only the last task is waiting, the others are discarded
    assert len(mw.futures) == 1
    # The last task is waiting and the last task is the last submitted
    assert mw.futures[0].running() and mw.futures[0].result() == 9
    # The results of tasks are not the same as the submitted tasks
    assert [r.result() for r in aysnc_results] != list(range(10))

# Generated at 2022-06-14 13:45:18.697559
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def _f(x):
        if x == 'except':
            raise ValueError('Got except')
        elif x == 'cancel':
            while True:
                pass
        else:
            import time
            time.sleep(x)
            return x

    worker = MonoWorker()

    # Submit a task which takes 1.5s to run
    f1 = worker.submit(_f, 1.5)
    assert f1 is not None
    f1.result()

    # Submit a task which takes 2s to run
    # Should be discarded because f1 is running
    f2 = worker.submit(_f, 2)
    assert f2 is None

    # Submit a task which takes 3s to run
    # Should replace the waiting task f2
    f3 = worker.submit(_f, 3)

# Generated at 2022-06-14 13:45:29.996901
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from tqdm.utils import _term_move_up
    from time import sleep
    from traceback import print_exc
    from nose.tools import timed

    @timed(60)
    def test():
        import concurrent.futures
        from platform import system

        def func(v, delay=0.1):
            sleep(delay)
            if v % 3 == 0:
                raise Exception("Value {0} is divisible by 3".format(v))
            elif v % 7 == 0:
                raise ValueError("Value {0} is divisible by 7".format(v))
            return v

        def progress_bar_wrapper(func, *args, **kwargs):
            bar = tqdm_auto(total=1, desc=str(args[0]))

# Generated at 2022-06-14 13:45:40.208752
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from multiprocessing import Queue
    from threading import Thread
    from time import sleep
    from tqdm.contrib.concurrent import MonoWorker
    q_in, q_out = Queue(), Queue()

    def f(x):
        """Test function"""
        sleep(1)
        q_out.put(x)
        return x

    def g(q_in, q_out, w):
        """Test function"""
        while True:
            x = q_in.get()
            if x is None:
                break
            w.submit(f, x)

    thread = Thread(target=g, args=(q_in, q_out, MonoWorker()))
    thread.start()

    q_in.put(0)
    sleep(0.1)
    q_in.put

# Generated at 2022-06-14 13:45:47.188057
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def sleeper(t):
        time.sleep(t)
        return t

    worker = MonoWorker()
    with tqdm_auto.tqdm(unit="sec") as t:
        while True:
            worker.submit(sleeper, 1)
            result = worker.submit(sleeper, 0.5)
            worker.submit(sleeper, 0.3)
            t.update(result.result())

# Generated at 2022-06-14 13:45:58.400607
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def slow_inc(*args, **kwargs):
        """Sleep for a second, then return args[0] incremented by 1."""
        sleep(1)
        return args[0] + 1

    worker = MonoWorker()

    # test that `futures` is deque with maxlen 2 and `data` is deque with maxlen 1
    assert isinstance(worker.futures, deque)
    assert worker.futures.maxlen == 2
    assert not worker.futures
    data = deque([0], 1)
    assert isinstance(data, deque)
    assert data.maxlen == 1
    assert data[0] == 0

    # submit a `slow_inc` task that takes 1 second to finish
    assert worker.submit(slow_inc, data[0]).result

# Generated at 2022-06-14 13:46:08.588528
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test method `MonoWorker.submit`."""

    import os
    import queue
    from time import sleep

    from ..utils import _decay_linear

    def f(x, t_kwargs):
        """Helper function for writing output."""
        _sleep = _decay_linear(
            1, 0, t_kwargs['total'], t_kwargs['unit_div'])
        sleep(_sleep)
        t_kwargs['output_str'] = repr(x)
        return

    worker = MonoWorker()
    task_queue = queue.Queue()
    output_queue = queue.Queue()
    output_str = None
    def task_queue_worker():
        """Non-blocking method to read/write output data.
        Run as a daemon thread.
        """
        while True:
            t_

# Generated at 2022-06-14 13:46:18.480988
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def task():
        time.sleep(1)
        print('B')
        time.sleep(1)
    worker = MonoWorker()
    print('A')
    worker.submit(task)
    time.sleep(0.1)
    print('C')
    worker.submit(task)
    time.sleep(0.1)
    print('D')
    worker.submit(task)
    time.sleep(0.1)
    print('E')
    worker.submit(task)
    time.sleep(0.1)
    print('F')
    worker.submit(task)
    print('G')
    worker.submit(task)
    print('H')
    worker.submit(task)
    # Output:
    # A
    # C
    # D
    # E
   

# Generated at 2022-06-14 13:46:26.938763
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from copy import copy
    from time import sleep
    from random import randint
    from operator import add

    def say(msg, sleep_time=None):
        sleep(sleep_time or 0)
        return msg

    def _assert_equal(x, y):
        assert x == y, '{} != {}'.format(x, y)

    def _validate(mono_worker, expected_msgs):
        sleep(0.1)
        _assert_equal(expected_msgs, [f.result() for f in mono_worker.futures])

    # Unit test for method submit of class MonoWorker
    def _test(sleep_time=None):
        expected_msgs = [1, 2, 3, 4, 5]
        # submit in same order as expected_msgs
        mono_worker = MonoWorker

# Generated at 2022-06-14 13:46:35.704788
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from random import random
    from threading import Lock
    from concurrent.futures import ThreadPoolExecutor

    mw = MonoWorker()
    map_lock = Lock()
    results = []
    map_result = []
    with ThreadPoolExecutor(max_workers=1) as executor:
        for i in range(10):
            with mw.pool as mw_executor:
                for j in range(3):
                    mw_executor.submit(
                        lambda i=i, j=j: map_lock.acquire() or
                        results.append((i, j)) or map_lock.release())
                while len(mw.futures) > 1:
                    time.sleep(random()/5)

# Generated at 2022-06-14 13:46:43.464876
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ..auto import tqdm
    from ..std import time

    mw = MonoWorker()

    def wait(sleep_time=1.):
        with tqdm(total=100, leave=False) as t:
            for _ in range(100):
                sleep(sleep_time)
                t.update(1)
    mw.submit(wait)
    mw.submit(wait, sleep_time=0.05)

    assert (100 - time.time()) < 0.05 * 100 + 2 * 1  # wait() should run

# Generated at 2022-06-14 13:46:50.887141
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from queue import Queue
    import threading

    q = Queue()
    m = MonoWorker()
    assert m.pool._max_workers == 1

    def log(x):
        tqdm_auto.write("{}".format(x))
        q.put(x)

    def func(x):
        time.sleep(0.5)
        log("func " + str(x))

    def func_err(x):
        log("func_err " + str(x))
        raise ValueError(x)

    # Submit new task
    log("1")
    m.submit(log, "A")
    assert m.futures[0].done() is False
    assert len(m.futures) == 1
    log("2")

# Generated at 2022-06-14 13:47:01.982127
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:47:10.446593
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import format_sizeof
    from ..pandas import tqdm_pandas

    # Create a worker
    worker = MonoWorker()

    # Get the version of pandas
    version = tqdm_pandas.__version__

    # Make a dummy dataframe
    df = tqdm_pandas.tqdm(range(1))
    df['col'] = df['col'].astype(str)

    start = time.time()

    # Run the method
    # If the method works, it gets the version of pandas
    # If the method fails in the future, it gets an error message
    result = worker.submit(format_sizeof, df)

    # Print the result
    tqdm_auto.write(result.result())
    end = time.time()

# Generated at 2022-06-14 13:47:16.843377
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def printer(name, delay, printstr):
        time.sleep(delay)
        tqdm_auto.write('{}: {}'.format(name, printstr))

    mw = MonoWorker()
    for i in range(4):
        mw.submit(printer, i, i, 'hello')
    time.sleep(4)
    tqdm_auto.write('slept for 4 seconds')

# Generated at 2022-06-14 13:47:34.741138
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def test_func(*args):
        time.sleep(args[0])
        return args

    worker = MonoWorker()

    # Should give 5, not 4 (discard waiting)
    worker.submit(test_func, 0, 1)
    worker.submit(test_func, 0, 2)
    worker.submit(test_func, 0, 3)
    waiting = worker.submit(test_func, 0, 4)
    assert waiting.result() == (0, 4)

    # Should give 6, not 5 (discard waiting)
    worker.submit(test_func, 0, 1)
    worker.submit(test_func, 0, 2)
    worker.submit(test_func, 0, 3)
    waiting = worker.submit(test_func, 0, 4)
    waiting.cancel()


# Generated at 2022-06-14 13:47:41.338082
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def _task(n):
        time.sleep(n)
        return n

    worker = MonoWorker()

    task1 = worker.submit(_task, 1)
    time.sleep(0.2)
    task2 = worker.submit(_task, 0.5)
    time.sleep(0.2)
    assert task1.done()
    assert task2.done()
    assert task1.result() == 1
    assert task2.result() == 0.5

# Generated at 2022-06-14 13:47:52.094593
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import struct
    import sys
    from six.moves import xrange as range

    def wait_and_print(x, output_stream=None, wait_time=0.05):
        """
        Waits for `wait_time` seconds and prints string `x` to `output_stream`.
        """
        if output_stream:
            time.sleep(wait_time)
            output_stream.write(x)
            output_stream.flush()

    # Obtain data from pipe
    def get_data():
        from os import read
        from os.path import commonprefix
        data = read(pipe, 1024)
        prefix = commonprefix([last, data])
        assert len(prefix) == len(last) - 1
        assert prefix == last[:-1]

# Generated at 2022-06-14 13:48:02.943977
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:48:11.704601
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    mw = MonoWorker()
    f = mw.submit(sleep, 0.5)
    f.result()  # wait for the first task to be completed
    assert f.done()
    f = mw.submit(sleep, 0.5)
    f.result()
    assert f.done()
    f = mw.submit(sleep, 0.5)
    f.result()
    assert f.done()
    progress = tqdm_auto.tqdm(desc='Testing MonoWorker', total=3)
    progress.update()
    progress.close()

if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:48:20.279827
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def f(n):
        time.sleep(n)
        return 'sleep {}s'.format(n)

    mw = MonoWorker()
    assert mw.submit(f, 0.1)
    assert mw.submit(f, 0.2)
    assert mw.submit(f, 0.3)
    assert mw.submit(f, 0.4)
    assert mw.submit(f, 0.5)
    assert mw.submit(f, 0.6)
    assert mw.submit(f, 0.7)
    assert mw.submit(f, 0.8)
    assert mw.submit(f, 0.9)
    assert mw.submit(f, 1)
    assert mw.submit(f, 1.1)

# Generated at 2022-06-14 13:48:30.604345
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()

    # check waiting task is replaced
    try:
        mw.submit(time.sleep, 10)
        mw.submit(time.sleep, 10)
        mw.submit(time.sleep, 10)
    except Exception:
        pass
    else:
        assert False, "This should fail due to Exception"

    # check exception handling
    try:
        mw.submit(Exception)
    except Exception:
        pass
    else:
        assert False, "This should fail due to Exception"


# Uncomment below to run test_MonoWorker_submit()
#if __package__ is None or __package__ == '':
#    from tqdm.contrib import *
#else:
#    from .tqdm.contrib import *
#test_Mono

# Generated at 2022-06-14 13:48:39.179050
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randint
    import sys
    OUT = sys.stdout

    n_calls = 5
    n_pause = 5
    mw = MonoWorker()

    def func(n):
        sleep(randint(*n_pause * (1, 2)))
        OUT.write("{} ".format(n))
        OUT.flush()
        return n

    for n in range(n_calls):
        mw.submit(func, n)
    for i in range(n_calls):
        futures = mw.futures
        len_futures = len(futures)
        if len_futures:
            f = futures.popleft()
            while not f.done() and len(futures):
                f = futures.popleft()
           

# Generated at 2022-06-14 13:48:48.940354
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import shuffle
    from unittest import TestCase

    class DummyException(Exception): pass
    class DummyFuture(object):
        def __init__(self, *args):
            self.args = args
            shuffle(self.args)
            self.done = False
        def result(self):
            sleep(0.1)
            self.done = True
            return self.args
        def exception(self):
            if not self.done:
                try:
                    # This should never happen unless we have a bug
                    raise AssertionError("MonoWorker failed to wait on result()")
                except Exception as e:
                    return e
            else:
                return None
        def cancel(self):
            pass


# Generated at 2022-06-14 13:48:57.696865
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Adapted from doctest
    import time
    import sys
    import threading
    import concurrent.futures as cf
    class Server(object):
        """
        Fork of a server that executes commands when called.

        """

        def run(self, command):
            """
            Runs `command` after a short delay

            """
            time.sleep(1)  # simulate a long-running task
            tqdm_auto.write('Running %s...' % command)

    server = Server()
    tqdm_auto.write('ENTER to quit')
    tqdm_auto.write('> ')
    tqdm_auto.flush()
    worker = MonoWorker()
    lines = []
    def queue_input(line):
        lines.append(line)
    import queue
    q = queue.Queue

# Generated at 2022-06-14 13:49:30.064883
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from contextlib import contextmanager

    # Data
    mw = MonoWorker()
    r = 'running'
    w = 'waiting'
    ds = 'discarded'
    i = 10

    # Methods
    @contextmanager
    def run(id_, time_, *args, **kwargs):
        yield mw.submit(sleep, time_)
        tqdm_auto.write('{id_} finished!'.format(id_=id_))
        yield id_

    # Test

# Generated at 2022-06-14 13:49:38.924743
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event
    from unittest import main

    global TEST_EXECUTED
    TEST_EXECUTED = Event()

    def run(delay, value):
        sleep(delay)
        TEST_EXECUTED.set()
        return value

    # Waiting task is replaced by a slower running task
    mw = MonoWorker()
    mw.submit(run, 0.1, 1)
    mw.submit(run, 0.5, 2)
    TEST_EXECUTED.wait(timeout=0.2)
    assert not TEST_EXECUTED.isSet()
    TEST_EXECUTED.wait(timeout=0.5)
    assert TEST_EXECUTED.isSet()
    mw.pool.shutdown(wait=True)   # Don

# Generated at 2022-06-14 13:49:47.479893
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from itertools import repeat
    from nose.tools import assert_in, assert_is_instance

    def func(x):
        sleep(x)
        return x

    worker = MonoWorker()
    futures = list(map(worker.submit, repeat(func), repeat(1), repeat(0.2),
                       repeat(2)))

    assert_is_instance(futures[0], type(futures[1].result()),
                        "First call to submit returned a future")
    assert_in(futures[1].result(), (0.2, 2),
              "Second call to submit returned a future which has not future")

# Generated at 2022-06-14 13:49:55.351515
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import _range

    def sleep_1s(i):
        time.sleep(1)

    # Test for the following scenario:
    # 3 calls to submit(sleep_1s) are made.
    # Since there is only one worker, the first 2 calls are queued.
    # The first 1s passes, only the first call is done.
    # The second 1s passes, only the second call is done.
    # The third 1s passes, the third call is also done.

    worker = MonoWorker()
    for a in _range(3):
        worker.submit(sleep_1s, a)
    while len(worker.futures) > 0:
        worker.futures[0].result()
        worker.futures.popleft()



# Generated at 2022-06-14 13:50:03.046507
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import warnings

    warnings.filterwarnings("ignore", category=DeprecationWarning)

    mw = MonoWorker()
    assert mw.submit(sleep, 1)
    assert mw.submit(sleep, 1)
    mw.futures[0].cancel()
    assert mw.submit(sleep, 1)
    assert mw.submit(sleep, 1)
    assert mw.submit(sleep, 1)
    mw.futures[0].cancel()
    assert mw.submit(sleep, 1)
    assert mw.submit(sleep, 1)
    assert mw.submit(sleep, 1)
    assert len(mw.futures) == 2
    print("Unit test for method submit of class MonoWorker passed.")



# Generated at 2022-06-14 13:50:14.865836
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # pylint: disable=missing-docstring
    import time
    import threading

    class Task:
        def __init__(self, id_):
            self.id = id_
            self.finished = False

        def run(self):
            # pylint: disable=missing-docstring
            # print(str(self.id) + ' begin')
            self.finished = False
            time.sleep(2)
            self.finished = True
            # print(str(self.id) + ' end')

    def thread(mw, id_):
        mw.submit(Task(id_).run)

    mw = MonoWorker()
    id_ = 0

    t1 = threading.Thread(target=thread, args=(mw, id_))
    t1.start()

# Generated at 2022-06-14 13:50:21.871565
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Lock
    from contextlib import contextmanager
    lock = Lock()
    def proc(*args):
        try:
            with lock:  # see if there are others running
                pass
        except Exception:
            pass
        else:
            sleep(0.1)

    def test(mw, start, end):
        with mw:
            while start < end:
                end = mw.submit(proc, start)
                start += 1
        return int(end)

    with mw_context() as mw:
        assert test(mw, 1, 6) == 5
        assert test(mw, 6, 11) == 10
        assert test(mw, 11, 16) == 15
        assert test(mw, 16, 21) == 15  # 16 discarded, only 15 concurrent

# Generated at 2022-06-14 13:50:30.029560
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import tqdm

    def sleep1(seconds=1):
        print('sleep1', seconds)
        time.sleep(seconds)
        return seconds

    def sleep2(seconds=2):
        print('sleep2', seconds)
        time.sleep(seconds)
        return seconds

    def sleep3(seconds=3):
        print('sleep3', seconds)
        time.sleep(seconds)
        return seconds

    worker = MonoWorker()

    t = time.time()
    # Run the first task
    task1 = worker.submit(sleep1, 10)
    # Submit a second task that should replace the waiting task (task2)
    task2 = worker.submit(sleep2, 10)
    # Submit a third task that should be discarded
    task3 = worker.submit(sleep3, 10)
    # Verify

# Generated at 2022-06-14 13:50:40.522809
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Lock
    from ..utils import format_sizeof

    def pause_writer(pause, write_lock, message):
        with tqdm_auto.external_write_mode(lock=write_lock):
            time.sleep(pause)
            tqdm_auto.write(message)

    # Start writing
    write_lock = Lock()
    mw = MonoWorker()

    # Thread 1: New task is submitted before old task is done
    message = "T1: " + format_sizeof(1e9) + "\n"
    mw.submit(pause_writer, 0.1, write_lock, message)
    time.sleep(0.05)

    # Thread 2: New task is submitted while old task is still running

# Generated at 2022-06-14 13:50:49.220873
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Thread
    import multiprocessing as mp
    from contextlib import contextmanager

    @contextmanager
    def poolcontext(*args, **kwargs):
        pl = mp.pool.ThreadPool(*args, **kwargs)
        yield pl
        pl.terminate()
        pl.join()

    counter = 0
    counter_parent = 0
    counter_child = 0

    def _counter(x):
        global counter, counter_parent, counter_child
        if not x:
            counter_parent = counter
            counter = max(counter, 1)
            raise KeyError
        else:
            counter += x
            counter_child = counter
            return

    def _data():
        for n in range(4):
            time.sleep(0.1)
            yield n

    # Test success


# Generated at 2022-06-14 13:51:42.719528
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import _range

    def time_func():
        time.sleep(0.1)

    mw = MonoWorker()
    with tqdm_auto.tqdm(iterable=_range(10), mininterval=0.1) as t:
        for _ in t:
            mw.submit(time_func)

    mw = MonoWorker()
    with tqdm_auto.tqdm(iterable=_range(10), mininterval=0.1) as t:
        for i in t:
            mw.submit(time_func)
            if i == 5:
                mw.submit(time_func)  # should now wait
            if i == 6:
                mw.submit(time_func)  # should now cancel

# Generated at 2022-06-14 13:51:48.013869
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import tqdm.contrib
    # The number of pending futures should not exceed 2 at any time
    def simple_func(n):
        time.sleep(n)
        return "done"
    worker = MonoWorker()
    for i in tqdm.contrib.itertools_chain([0, 0, 0], [1, 2, 3, 4]):
        worker.submit(simple_func, i)
    for i in range(4):
        print(worker.futures.popleft().result())

# Generated at 2022-06-14 13:51:52.679035
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def f(msg, t=2):
        sleep(t)
        print(msg)

    worker = MonoWorker()
    worker.submit(f, "1st", 1)
    worker.submit(f, "2nd", 1)
    worker.submit(f, "3rd", 4)
    worker.submit(f, "4th", 1)
    worker.submit(f, "5th", 1)
    worker.submit(f, "6th", 4)

    """
    Expected output:
    1st
    2nd
    3rd
    6th
    """


# Generated at 2022-06-14 13:52:00.870845
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import pytest

    def func(x, y):
        print("start", x, y)
        time.sleep(0.1)
        return x + y

    mw = MonoWorker()

    start = time.perf_counter()
    mw.submit(func, 2, 1)
    time.sleep(0.75)
    mw.submit(func, 3, 2)
    time.sleep(0.1)
    end = time.perf_counter()

    assert end - start > 0.4

# Generated at 2022-06-14 13:52:08.213607
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ..auto import trange
    from ..std import sys

    def slow_func(sleep_time, val):
        sleep(sleep_time)
        return val

    with trange(10) as t, MonoWorker() as mono:
        for i in t:
            mono.submit(slow_func, i * .1, i)
            t.set_description(str(mono.futures))
    assert str(mono.futures) == '<deque([], maxlen=2)>', str(mono.futures)
    # Manual check of other outputs
    sys.stderr.flush()
    sys.stdout.flush()



# Generated at 2022-06-14 13:52:16.187717
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    running = [0]
    waiting = [0]
    def long_running():
        running[0] = 1
        time.sleep(5)
        running[0] = 0
        return running
    def very_long_running():
        running[0] = 1
        time.sleep(10)
        running[0] = 0
        return running
    def long_waiting():
        waiting[0] = 1
        time.sleep(6)
        waiting[0] = 0
        return waiting
    def very_long_waiting():
        waiting[0] = 1
        time.sleep(12)
        waiting[0] = 0
        return waiting
    assert mw.submit(long_running) is None
    assert running == [0]
    assert mw

# Generated at 2022-06-14 13:52:22.283021
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    mw = MonoWorker()

    def a():
        import time
        time.sleep(2)
        return 1

    def b():
        import time
        time.sleep(1)
        return 2

    def c():
        import time
        time.sleep(3)
        return 3

    assert mw.submit(a).result() == 1
    assert mw.submit(b).result() == 2
    assert mw.submit(c).result() == 2



# Generated at 2022-06-14 13:52:31.570510
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():  # pragma: no cover
    import time
    import threading
    from queue import Queue

    class MockWorker(MonoWorker):
        def __init__(self, output):
            super(MockWorker, self).__init__()
            self.output = output
            self.output_lock = threading.Lock()

        def submit(self, func, *args, **kwargs):
            with self.output_lock:
                self.output.put("submit " + str(func) + str(args) + str(kwargs))
            res = super(MockWorker, self).submit(func, *args, **kwargs)
            with self.output_lock:
                self.output.put("return")
            return res


# Generated at 2022-06-14 13:52:41.443550
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    from random import shuffle
    from time import sleep

    if sys.version_info < (3, 2):
        return

    mw = MonoWorker()

    # test with no args
    mw.submit(sleep, 1)
    assert len(mw.futures) == 1
    sleep(2)  # let waiting task complete
    assert not mw.futures[0].done()

    # test multiple args, kwargs
    mw.submit(lambda x, y: print(x, y), 0, y=0)
    mw.submit(lambda x, y: print(x, y), 1, y=1)
    assert len(mw.futures) == 1  # only recent waiting task

    # test running task with long wait time
    mw.submit(sleep, 5)