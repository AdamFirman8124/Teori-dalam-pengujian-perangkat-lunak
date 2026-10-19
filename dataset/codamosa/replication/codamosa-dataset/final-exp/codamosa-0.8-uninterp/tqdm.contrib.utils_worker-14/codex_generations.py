

# Generated at 2022-06-14 13:42:52.988198
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event

    mw = MonoWorker()

    class Count:
        def __init__(self):
            self.n = 0
            self.e = Event()

        def inc(self):
            self.n += 1

        def dec(self):
            self.n -= 1

            if self.n == 0:
                self.e.set()

    count = Count()
    def inc_count():
        count.inc()
        sleep(0.05)
        count.dec()

    # Test call to inc_count() is not blocked
    count.e.wait()

    # Test 1st call to inc_count()
    mw.submit(inc_count)
    count.e.wait()
    assert count.n == 0

    # Test 2nd call to inc_count

# Generated at 2022-06-14 13:43:00.585231
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import functools
    import operator

    def tick(n, k, t=1):
        time.sleep(t * random.random())
        return n + k

    worker = MonoWorker()
    tick_next = functools.partial(tick, n=0)
    for k in range(1, 5):
        worker.submit(tick_next, k=k)
        time.sleep(0.5)
    for k in range(5, 8):
        worker.submit(tick_next, k=k)
    assert operator.ge(*[future.result() for future in worker.futures])

# Generated at 2022-06-14 13:43:11.895123
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from sys import exc_info
    from os.path import join

    class SleepSort(MonoWorker):
        """Sleep sort in decreasing order with O(1) memory."""
        def __init__(self, sleep_time, sleep_func=sleep):
            self.sleep_time = sleep_time
            self.sleep_func = sleep_func
            super(SleepSort, self).__init__()

        def submit(self, s, *args, **kwargs):
            """`sleep_time` seconds after `s`, puts `s` in `output`.
            `*args, **kwargs` are passed to `super.submit`.
            """
            super(SleepSort, self).submit(self.sleep_func, self.sleep_time)


# Generated at 2022-06-14 13:43:22.582473
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys
    import os
    import multiprocessing as mp
    import random
    
    class log_file(object):
        def __init__(self, filename):
            self.filename = filename
            self.file = open(filename, 'w')
            self.process_number = mp.current_process()._identity[0]
        
        def log_print(self, string):
            self.file.write('-' * 10 + '\n')
            self.file.write(str(self.process_number) + ': ' + string + '\n')
            self.file.write('-' * 10 + '\n\n')
            self.file.flush()
        
        def __del__(self):
            self.file.close()
    

# Generated at 2022-06-14 13:43:31.581201
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    import time
    import unittest

    from .utils import decode_ascii, check_tqdm_write_io

    class MonoWorkerTestCase(unittest.TestCase):
        def test_write(self):
            for buf in [False,
                        True,
                        'hello'.encode('utf-8'),
                        sys.stdout,
                        sys.stdout.buffer]:
                with check_tqdm_write_io(buf) as (_, tqdm_write):
                    mw = MonoWorker()
                    mw.submit(decode_ascii, "Héllô, 世界")
                    time.sleep(0.1)
                    # TODO: change "ascii" to "utf-8" once
                    # https://github.com/tqdm

# Generated at 2022-06-14 13:43:42.225022
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def _submit(mw, func, x, delay):
        mw.submit(func, x, delay=delay)

    def plus_one(x, delay=0.1):
        time.sleep(delay)
        return x + 1

    mw = MonoWorker()
    mw.submit(plus_one, 0, delay=0)  # test blocking
    _submit(mw, plus_one, 1, delay=0.1)  # test blocking
    _submit(mw, plus_one, 2, delay=0.3)  # test blocking
    _submit(mw, plus_one, 3, delay=0.2)  # test blocking
    _submit(mw, plus_one, 4, delay=0.4)  # test blocking

# Generated at 2022-06-14 13:43:51.563785
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from concurrent.futures import CancelledError

    def myfunc(x):
        time.sleep(x)
        return 2*x

    worker = MonoWorker()
    # test basic functionality
    f1 = worker.submit(myfunc, 1)
    f2 = worker.submit(myfunc, 2)
    assert f1.done()
    assert f2.done()
    assert f1.result() == 2
    assert f2.result() == 4
    # test replacement
    f1 = worker.submit(myfunc, 3)
    assert f2.done()
    assert f2.cancelled()
    with tqdm_auto.external_write_mode():
        assert f1.result() == 6
    # test clear-all
    f3 = worker.submit(myfunc, 4)


# Generated at 2022-06-14 13:44:01.243374
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Output example:

    waiting task: 0123456789
    should cancel: 012
      | cancelled: 012
  running task: 0123456789
    should cancel: 0123456789
      | cancelled: 0123456789
    should cancel: 3456789
    """
    import time
    import _thread as thread
    worker = MonoWorker()
    fut = worker.submit(_print_and_wait, '0123456789', 0.2)
    # print waiting
    thread.start_new_thread(_wait_and_print, (fut, '0123456789'))
    time.sleep(0.001)
    # submit new
    worker.submit(_print_and_wait, '3456789', 0.2)
    fut.result()



# Generated at 2022-06-14 13:44:09.043266
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test MonoWorker.submit"""
    import time

    def f(x, y):
        time.sleep(0.1)
        return x + y

    mw = MonoWorker()
    assert not mw.futures
    r = mw.submit(f, 1, 2)
    assert isinstance(r, future)
    assert len(mw.futures) == 1
    assert r.done()
    assert not r.result() == 4  # wrong
    r = mw.submit(f, 3, 4)
    assert isinstance(r, future)
    assert len(mw.futures) == 1
    assert not r.done()
    assert r.result() == 7
    time.sleep(0.2)
    assert r.done()

# Generated at 2022-06-14 13:44:14.606909
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from concurrent.futures import as_completed
    from tqdm.contrib.concurrency import MonoWorker
    def sleep_times_3(t):
        sleep(t * 3)
        return t

    with MonoWorker() as worker:
        from concurrent.futures import FIRST_COMPLETED
        for t in [2, 1, 3, 5, 4]:
            worker.submit(sleep_times_3, t)
        for future in as_completed(worker.futures,
                                   timeout=12,
                                   first_completed=True):
            print('\nOutput of task {}: {}'.format(
                future, future.result()))

    with MonoWorker() as worker:
        from concurrent.futures import FIRST_EXCEPTION

# Generated at 2022-06-14 13:44:27.192185
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = tqdm.contrib.MonoWorker()
    # Wait for immediate execution, then wait an extra 10s
    f1 = mw.submit(time.sleep, 0.1)
    f2 = mw.submit(time.sleep, 0.2)
    f2.result()  # wait
    f1.cancel()  # should have no effect
    assert f1.cancel()  # should have no effect

    def long_task():
        time.sleep(0.2)
        raise Exception("Bad long task")

    # Wait for immediate execution
    f1 = mw.submit(long_task)
    f2 = mw.submit(time.sleep, 0.1)
    f2.result()  # wait

# Generated at 2022-06-14 13:44:37.917281
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Unit test for method submit of class MonoWorker
    """
    import time
    import random
    from concurrent.futures import as_completed
    from ..utils import format_sizeof

    def test_func(*args, **kwargs):
        """
        Return the number of seconds this function runs for.
        """
        time.sleep(random.random())  # randomly sleep for 0-1 seconds
        return random.random()

    worker = MonoWorker()
    futures = []
    for _ in range(6):
        futures.append(worker.submit(test_func,
                                     "hello",  # positional argument
                                     test_arg="test"))  # keyword argument
    print("\nTest concurrency and `MonoWorker.submit()`:")

# Generated at 2022-06-14 13:44:45.813108
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import multiprocessing
    worker = MonoWorker()
    print(worker.submit(lambda: time.sleep(1), 1))
    print(worker.submit(lambda: time.sleep(2), 2))
    print(worker.submit(lambda: time.sleep(3), 3))
    print(worker.submit(lambda: time.sleep(4), 4))
    print([f.result() for f in worker.futures])

if __name__ == "__main__":
    multiprocessing.freeze_support()
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:44:52.087059
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(args):
        return args
    mw = MonoWorker()
    for i in range(9):
        mw.submit(func, i)
    assert len(mw.futures) == 2
    assert mw.futures[0].done()
    assert not mw.futures[1].done()
    mw.futures[1].result()
    assert mw.futures[1].done()
    assert mw.futures[1].result() == 8

# Generated at 2022-06-14 13:44:59.397168
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import _get_term_width
    from ..std import tqdm
    from multiprocessing import Pool

    def run(arg, from_pool=False, progressbar=False):
        time.sleep(arg)
        if progressbar:
            len_ = 10
            pbar = tqdm(total=len_)
            for i in range(len_):
                time.sleep(0.1)
                pbar.update()
            pbar.close()
            return arg
        elif from_pool:
            p = Pool(1)
            return p.apply(run, (arg,))

    def callback(f, i):
        assert f.result() == i, "expected {0} got {1}".format(i, f.result())

    mw = MonoWorker()


# Generated at 2022-06-14 13:45:10.642239
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    mw = MonoWorker()
    # [ ] submit 1
    assert mw.submit(time.sleep, 0.5)

    # [ ] submit 2
    time.sleep(0.05)
    assert mw.submit(time.sleep, 0.5)

    # [ ] submit 3 (func 3 should replace func 2)
    time.sleep(0.05)
    assert mw.submit(time.sleep, 0.5)

    # [ ] submit 4 (func 4 should replace func 3)
    time.sleep(0.05)
    assert mw.submit(time.sleep, 0.5)

    time.sleep(0.05)
    # [x] run submit 1
    # [ ] replace submit 1 with 2
    assert mw.futures[0].result(timeout=0.1)

# Generated at 2022-06-14 13:45:17.069838
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def simple_func(x):
        """Dummy function that prints its argument and returns it."""
        time.sleep(x)
        tqdm_auto.write("Executed function: %s" % x)
        return x

    m = MonoWorker()
    m.submit(simple_func, 1)
    time.sleep(1.5)
    m.submit(simple_func, 2)
    time.sleep(2)
    m.submit(simple_func, 3)
    time.sleep(3)

# Generated at 2022-06-14 13:45:27.783537
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    assert not mw.futures
    r = mw.submit(time.sleep, 0.5)
    assert r == mw.futures[-1]
    time.sleep(0.1)
    r2 = mw.submit(time.sleep, 0.5)
    assert r2 == mw.futures[-1]
    assert not mw.futures[0].done()
    assert not mw.futures[0].cancel()
    assert r.running
    assert r2.running
    r3 = mw.submit(time.sleep, 0.5)
    assert not mw.futures[0].done()
    assert r.cancel()
    assert r2.done()
    assert not r2.c

# Generated at 2022-06-14 13:45:38.366074
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    def functionab(a, b, abc):
        return a + b + abc

    mw = MonoWorker()
    fs = []
    fs.append(mw.submit(functionab, 1, 2, abc="hi"))
    fs.append(mw.submit(functionab, 3, 4, abc="hi"))
    fs.append(mw.submit(functionab, 5, 6, abc="hi"))
    fs.append(mw.submit(functionab, 7, 8, abc="hi"))
    fs.append(mw.submit(functionab, 9, 10, abc="hi"))
    assert str(fs[0].result()) == "3hi"
    assert str(fs[1].result()) == "7hi"
    assert str(fs[2].result()) == "7hi"


# Generated at 2022-06-14 13:45:45.993791
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import os, random, sys
    from collections import deque

    class EchoWorker(MonoWorker):
        """
        A concurrent task that prints the received arguments
        in the order received and returns the same values.
        """
        def submit(self, *args, **kwargs):
            # super(EchoWorker, self).submit(print, *args, **kwargs)
            return super(EchoWorker, self).submit(
                lambda *a, **k: sys.stdout.write(
                    "{0} {1} {2}\n".format(a, k, os.getpid())))

    worker = EchoWorker()
    assert worker.futures == deque([])
    worker.submit(1, a=2)
    assert len(worker.futures) == 1

# Generated at 2022-06-14 13:46:00.535226
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import functools
    import threading

    def t(i):
        time.sleep(1)
        tqdm_auto.write('[{}]'.format(i))
        return i

    m = MonoWorker()
    r = []
    for i in range(4):
        m.submit(t, i)
        r.append(m.futures[-1].result())
        time.sleep(0.2)

    assert r == [3] * 4
    assert sorted(m.futures) == [
        functools.partial(t, 0),  # submitted but not running
        functools.partial(t, 1),
        functools.partial(t, 2),
        functools.partial(t, 3),
    ]

    # simulate a task taking a

# Generated at 2022-06-14 13:46:09.336455
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test the MonoWorker submit method.

    Note:
        `tqdm.tqdm()` is intentionally NOT used to ensure that
        `tqdm.auto.tqdm()` is actually used.
    """
    import sys
    import time

    # pylint: disable=undefined-variable
    void_tqdm = tqdm_auto
    # pylint: enable=undefined-variable

    mw = MonoWorker()
    assert len(mw.futures) == 0

    # first task
    assert mw.submit(pow, 2, 5) is not None
    assert len(mw.futures) == 1
    assert not mw.futures[0].done()

    # second task (waiting)

# Generated at 2022-06-14 13:46:19.039066
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..auto import tqdm

    def work(t):
        """
        Simulates a function doing work for `t` seconds.
        """
        for _ in tqdm(range(10), desc='foo', leave=False):
            time.sleep(t / 10)

    mw = MonoWorker()
    f1 = mw.submit(work, 0.5)
    f2 = mw.submit(work, 0.75)
    f1.cancel()  # should be ignored
    f2.result()
    assert f1.cancel()  # should be waiting (and no longer running)
    f3 = mw.submit(work, 1.0)
    f3.result()
    mw.submit(work, 1.5)

# Generated at 2022-06-14 13:46:27.247941
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    def func(i):
        time.sleep(1)
        return i

    mw = MonoWorker()

    mw.submit(func, 0)
    mw.submit(func, 1)
    mw.submit(func, 2)

    mw.submit(func, 3)
    mw.submit(func, 4)

    assert mw.futures[0].result() == 4
    assert mw.futures[1].result() == 2

    def func(i, c, d):
        time.sleep(1)
        raise RuntimeError()

    mw = MonoWorker()
    for i in range(3):
        mw.submit(func, i, c='', d='')

    assert mw.futures[0].exception()

# Generated at 2022-06-14 13:46:35.822971
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from unittest import TestCase, main as run_tests

    from .utils import _

    class FakeFuture(object):
        """
        Imitates the behaviour of concurrent.futures.Future
        """
        def __init__(self, done=False, cancelled=False, delay=None):
            self.done = done
            self.cancelled = cancelled
            self.delay = delay

        def __iter__(self):
            return self

        def __next__(self):
            if not self.done:
                if self.cancelled:
                    raise StopIteration
                else:
                    sleep(self.delay)
                    self.done = True
                    self.result = 'result'
                    self.exception = None
            raise StopIteration

        def cancel(self):
            self.cance

# Generated at 2022-06-14 13:46:46.056669
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    results = []
    futures = []
    for i in range(10):
        f = mw.submit(time.sleep, i/2)
        futures.append(f)
        results.append(i)
    assert all(f.done() for f in futures[:2])
    assert not all(f.done() for f in futures[2:])
    time.sleep(10)
    print(tuple(f.result() for f in futures[:2]))
    assert all(f.result() for f in futures[:2])
    assert not all(f.result() for f in futures[2:])
    assert any(f.cancelled() for f in futures[2:])
    assert results[2:] == [9] * 8

# Generated at 2022-06-14 13:46:52.926391
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep, time

    def check(mw, nb_running, nb_waiting, nb_finished):
        assert (len(mw.pool._threads) == nb_running + nb_waiting +
                nb_finished)
        assert (len(mw.futures) == nb_waiting + nb_finished)
        assert ([fut.done() for fut in mw.futures] ==
                [False] * nb_waiting + [True] * nb_finished)
        assert ([fut.running() or fut.done()
                 for fut in mw.pool._threads.values()] ==
                [True] * nb_running + [False] * nb_waiting +
                [True] * nb_finished)


# Generated at 2022-06-14 13:47:03.253407
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def waiter(n):
        time.sleep(n)
        return n
    mono = MonoWorker()
    f1 = mono.submit(waiter, 1)
    assert f1.running()
    time.sleep(2)
    assert f1.done() and f1.result() == 1
    f2 = mono.submit(waiter, 2)
    assert f2.running()
    f3 = mono.submit(waiter, 3)
    assert f2.cancelled() and not f3.done()
    assert f3.result() == 3
    f4 = mono.submit(waiter, 4)
    time.sleep(2)
    assert f3.done() and not f4.done()
    assert f4.cancel() and not f4.done()

# Generated at 2022-06-14 13:47:08.183380
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def a_func():
        import time
        time.sleep(1)

    # Create a MonoWorker object
    obj = MonoWorker()

    # Submit the first task
    obj.submit(a_func)

    # Submitting another task will cancel the first task
    obj.submit(a_func)
    print('All tasks have been cancelled.')

# Generated at 2022-06-14 13:47:18.898450
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test method `MonoWorker.submit()`."""
    import time
    from threading import Event

    ready = Event()
    worker = MonoWorker()
    assert len(worker.futures) == 0

    # First task
    r1 = worker.submit(time.sleep, 1)
    assert len(worker.futures) == 1
    assert not r1.done()

    # Second task queued
    r2 = worker.submit(ready.wait)
    assert len(worker.futures) == 2
    assert not r2.done()

    # First task finishes
    time.sleep(0.5)  # give first task time to finish
    assert len(worker.futures) == 1
    assert r1.done()
    assert not r2.done()

    # Clear second task
   

# Generated at 2022-06-14 13:47:36.102124
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def my_func(seconds=0.01):
        time.sleep(seconds)

    worker = MonoWorker()
    # Prints: "Waiting task submitted!"
    worker.submit(tqdm_auto.write, "Waiting task submitted!")
    # Prints: "Running task submitted!"
    worker.submit(tqdm_auto.write, "Running task submitted!")
    # Prints: "Running task submitted!"
    worker.submit(tqdm_auto.write, "Running task submitted!")
    # Prints: "Running task submitted!"
    worker.submit(tqdm_auto.write, "Running task submitted!")

    # Should be finished by now
    print(worker.futures.pop().result())
    # Should be finished by now

# Generated at 2022-06-14 13:47:45.216893
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from contextlib import contextmanager
    import time
    import threading

    @contextmanager
    def queue_locker(queue, lock):
        """Lock, and clear queue"""
        with lock:
            del queue[:]
            yield

    def target(queue, lock, _sleep=1):
        with queue_locker(queue, lock):
            time.sleep(_sleep)

    q = []
    l = threading.Lock()
    with MonoWorker() as mw:
        mw.submit(target, q, l)
        assert q == []  # queue not yet cleared
        mw.submit(target, q, l)
        assert q == []  # queue not yet cleared
        time.sleep(0.5)
        mw.submit(target, q, l)
        assert q == []  # queue not yet

# Generated at 2022-06-14 13:47:53.418777
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .tests import SlowTest
    from multiprocessing import cpu_count
    num_workers = cpu_count()
    # Submit simple function that does nothing
    worker = MonoWorker()
    for i in range(num_workers):
        worker.submit(lambda: 0)
    # Submit function that waites forever
    worker = MonoWorker()
    for i in range(num_workers):
        worker.submit(lambda: SlowTest.wait_forever())

    # Submit function that waites n seconds
    worker = MonoWorker()
    for i in range(num_workers):
        worker.submit(lambda s=i * 0.1: SlowTest.wait(s))

# Generated at 2022-06-14 13:48:04.044271
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Make sure `MonoWorker.submit` accepts, runs, and returns in order.
    """
    import time, threading
    m = MonoWorker()
    lock = threading.Lock()
    c = 0

    def f(a, b=0):
        with lock:
            nonlocal c
            c += 1
            cb = c
        time.sleep(a)
        with lock:
            nonlocal c
            cb = c - cb
            c += 1
        return cb

    futures = [m.submit(f, i * 0.5, b=j) for i, j in zip(range(1, 5), range(3))]

# Generated at 2022-06-14 13:48:09.450853
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Unit test for method submit of class MonoWorker
    """
    def f(x):
        return x
    m = MonoWorker()
    m.submit(f, 1)
    m.submit(f, 2)
    assert m.futures[0].result() == 1
    m.submit(f, 3)
    assert m.futures[0].result() == 3

# Generated at 2022-06-14 13:48:16.483570
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        with tqdm_auto.tqdm(total=4) as t:
            mw = MonoWorker()
            for i in range(4):
                f = mw.submit(time.sleep, .2)
                if f is not None:
                    f.add_done_callback(
                        lambda f, bar=t: bar.update(1) if f.done() else None)
                    t.update(1)
    assert t.n == 4  # no coverage



# Generated at 2022-06-14 13:48:26.045560
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from multiprocessing.pool import ThreadPool
    from time import sleep
    from os import cpu_count

    pool = ThreadPool(processes=cpu_count() + 2)  # size of pool

    def func(foo):  # dummy function
        return foo + 1

    # Here is the tqdm part
    mw = MonoWorker()
    mw.pool = pool  # replace default MonoWorker pool by that of ThreadPool

    res = [mw.submit(func, i) for i in range(100)]  # submit all the work
    assert all(r.done() for r in res)
    assert mw.futures == deque([], 2)

    pool.close()

# Generated at 2022-06-14 13:48:35.185181
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    # GIVEN
    worker = MonoWorker()
    running_execution_time = 0.2
    waiting_execution_time = 0.1
    expected_execution_time = running_execution_time + waiting_execution_time
    running_result = 1
    waiting_result = 2
    expected_results = [running_result, waiting_result]

    # WHEN
    measures = []
    measure_func = lambda: time.monotonic()
    running_func = lambda: measure_func() + running_execution_time
    waiting_func = lambda: measure_func() + waiting_execution_time
    measures.append(measure_func())
    running = worker.submit(running_func, *(), **{})
    measures.append(measure_func())
    running.result()


# Generated at 2022-06-14 13:48:43.687654
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from .utils import silence_stderr
    from ..utils import str_dict

    def sleep_then_return(msg, seconds):
        time.sleep(seconds)
        return msg

    with silence_stderr():
        mono = MonoWorker()
        tqdm_auto.write(">>> mono.submit(sleep_then_return, 'waiting1', 0.2)")
        waiting1 = mono.submit(sleep_then_return, 'waiting1', 0.2)
        tqdm_auto.write(">>> mono.submit(sleep_then_return, 'waiting2', 0.2)")
        waiting2 = mono.submit(sleep_then_return, 'waiting2', 0.2)
        tqdm_auto.write(">>> waiting1.result()")
        assert waiting1.result

# Generated at 2022-06-14 13:48:52.551927
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event
    def run(event=None):
        event.wait()
    from time import sleep
    from operator import is_not
    from functools import partial
    from random import randint
    from unittest import TestCase

    class Test(TestCase):
        def test(self):
            mw = MonoWorker()
            events = [Event() for _ in range(10)]
            waits = [randint(1, 5) for _ in range(9)]
            for e, wait in zip(events, waits):
                mw.submit(partial(run, e), None)
                sleep(wait)
            from itertools import chain
            from concurrent.futures import wait
            runtimes = chain(*[event.wait(0) for event in events])
            wait(mw.futures)


# Generated at 2022-06-14 13:49:19.314696
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .string import Stringy

    mw = MonoWorker()
    s = Stringy()
    func = s.join
    args = ('1',)
    kwargs = {}
    future1 = mw.submit(func, *args, **kwargs)
    sleep(0.2)
    assert s.string == '1'
    future2 = mw.submit(func, *args, **kwargs)
    sleep(0.2)
    assert s.string == '11'
    assert future1.done()
    assert not future2.done()
    future3 = mw.submit(func, *args, **kwargs)
    sleep(0.2)
    assert s.string == '111'
    assert future2.done()
    assert not future3.done()
    m

# Generated at 2022-06-14 13:49:30.459602
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import current_thread
    from functools import partial

    def func_sleep(sec, *args, **kwargs):
        """testing function"""
        sleep(sec)
        return (sec, current_thread().getName(), args, kwargs)

    mono = MonoWorker()
    f1 = mono.submit(func_sleep, sec=0.2, id=1)
    sleep(0.1)
    f2 = mono.submit(func_sleep, sec=0.1, id=2)
    f3 = mono.submit(func_sleep, sec=0.3, id=3)
    sleep(0.1)
    f4 = mono.submit(func_sleep, sec=0.2, id=4)
    sleep(0.1)

# Generated at 2022-06-14 13:49:38.621854
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    mw = MonoWorker()
    with mw as mw:
        def f(x):
            sleep(x)
            return x
        A = mw.submit(f, 1)
        B = mw.submit(f, 2)
        C = mw.submit(f, 3)
        D = mw.submit(f, 4)
        assert B.done() and (not A.done())
        assert D.done() and C.done()
        assert A.result() == 1
        assert B.result() == 2
        assert C.result() == 3
        assert D.result() == 4

if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:49:48.907638
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from operator import add  # noqa
    from concurrent.futures import TimeoutError  # noqa

    def f(x):
        time.sleep(1)
        return x

    workers = MonoWorker()
    f1 = workers.submit(f, 1)
    assert f1.result(0) is None  # timeout
    # attempt to call f
    f2 = workers.submit(f, 2)
    # noone else but f2 can be running
    assert f2.result(0) is None
    try:
        f1.result(0)
    except TimeoutError:
        pass
    else:
        raise AssertionError('f1 should not be running')
    f2.cancel()
    f3 = workers.submit(f, 3)
    # noone else but f

# Generated at 2022-06-14 13:49:59.306931
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import numpy as np
    from concurrent.futures import TimeoutError

    def square(n):
        """Sleep random time < n and return n ** 2."""
        time.sleep(random.random() * n)
        return n ** 2

    def test_func(x):
        """Sleep random time < x and return x ** 4."""
        return x ** 4

    def test_error(s):
        """Raise ValueError("s is not float!")."""
        if not isinstance(s, float):
            raise ValueError("s is not float!")
        return s

    def test_timeout(s):
        """Sleep for s seconds and return 1."""
        time.sleep(s)
        return 1


# Generated at 2022-06-14 13:50:07.225622
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ubelt import util_test

    def func(x):
        sleep(x)
        return x

    with util_test.TempDir() as dir_:
        # Test that we can only queue 2 jobs
        worker = MonoWorker()
        for x in range(4):
            worker.submit(func, x)
            sleep(0.1)

        # Test that once a job starts, it must finish before a new one can run
        worker = MonoWorker()
        num_submitted = 4
        for x in range(num_submitted):
            worker.submit(func, 0.2)
            sleep(0.1)
        # Wait 0.25 seconds and then submit a new task
        sleep(0.25)
        worker.submit(func, 0)

        # Wait for all jobs to complete

# Generated at 2022-06-14 13:50:17.147492
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def slow_add(x, y, z):
        sleep(1)
        return x + y + z

    def fast_add(x, y, z):
        return x + y + z

    mw = MonoWorker()

    mw.submit(slow_add, 1, 2, 3)
    assert mw.futures[0].result() == 6
    assert not mw.futures[0].cancelled()

    mw.submit(slow_add, 4, 5, 6)
    assert mw.futures[0].cancelled() or not mw.futures[0].done()
    assert mw.futures[1].result() == 15
    assert not mw.futures[1].cancelled()


# Generated at 2022-06-14 13:50:27.220630
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from concurrent.futures import Future
    from threading import Thread
    import multiprocessing

    class NeverEndingThread(Thread):
        """Non-daemonic thread that never stops until killed"""
        def __init__(self, *args, **kwargs):
            super(NeverEndingThread, self).__init__(*args, **kwargs)
            self.daemon = False

        def run(self):
            while True:
                time.sleep(0.1)

    def raise_error(*args, **kwargs):
        raise Exception('error')

    mw = MonoWorker()
    assert len(mw.futures) == 0
    tqdm_auto.write('submit 1 running')
    mw.submit(NeverEndingThread().start)

# Generated at 2022-06-14 13:50:33.096102
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randrange
    from ..utils import suppress_warnings

    with suppress_warnings():
        from concurrent.futures import TimeoutError

    maker = MonoWorker()
    class Printer(object):
        def __init__(self, name):
            self.name = name
        def __call__(self):
            sleep(randrange(100) / 1000)
            tqdm_auto.write(self.name)
    p1 = Printer('p1')
    p2 = Printer('p2')
    p3 = Printer('p3')
    p4 = Printer('p4')
    maker.submit(p1)  # waiting
    maker.submit(p2)  # running
    waiting = maker.submit(p3)  # waiting

# Generated at 2022-06-14 13:50:38.872900
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> mw = MonoWorker()
    >>> futures = []
    >>> for i in range(10):
    ...     wait = i % 3
    ...     futures.append(mw.submit(wait_and_mul, wait, i, 2))
    >>> len(futures)
    10
    >>> for i, future in enumerate(futures):
    ...     assert future.result() == i * 2
    """

# Generated at 2022-06-14 13:51:26.779818
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test method submit of class MonoWorker."""
    # Finished jobs
    worker = MonoWorker()

    def finished_func(a):
        return a

    # `finished_func` has not been used before
    assert worker.futures.maxlen == 2  # `worker.submit` sets `maxlen=2`
    assert len(worker.futures) == 0

    fut1 = worker.submit(finished_func, 1)
    assert len(worker.futures) == 1
    assert fut1.done()

    fut2 = worker.submit(finished_func, 2)
    assert len(worker.futures) == 2
    assert fut2.done()

    # `finished_func` has been used before
    fut3 = worker.submit(finished_func, 3)

# Generated at 2022-06-14 13:51:32.006228
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    mw = MonoWorker()
    n = 10

    def mysleep(i):
        time.sleep(random.random() * 3)
        return i

    for i in tqdm_auto.trange(10, desc='Test'):
        mw.submit(mysleep, i)

# Generated at 2022-06-14 13:51:41.270964
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event
    from traceback import print_exc
    from unittest import TestCase

    ev_timeout = Event()
    ev_timeout.set()

    def timeout_func():
        """
        This function is used to enforce a timeout to the thread execution.
        """
        ev_timeout.wait()

    def test_func():  # pylint: disable=inconsistent-return-statements
        """
        The test itself is built around this function.
        """
        sleep(0.1)
        return True

    def add_test(worker_, submit_args):
        """
        The generic test function, called for each test case.
        """

# Generated at 2022-06-14 13:51:49.232027
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from logging import debug, warning
    from threading import current_thread

    debug("DEBUG: %s" % __name__)

    # Test worker
    worker = MonoWorker()

    # Test function with name
    def func_str(arg):
        """Test function with string

        Parameters
        ----------
        arg: str
            argument to print
        """
        thread_id = current_thread().ident
        debug("DEBUG: start %s by thread %d" % (arg, thread_id))
        sleep(0.1)
        debug("DEBUG: done %s by thread %d" % (arg, thread_id))
        return arg

    # Test function without name
    def func_int(arg):
        thread_id = current_thread().ident

# Generated at 2022-06-14 13:51:55.380976
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from tqdm.auto import trange
    import sys

    def foo(i):
        sleep(0.1)
        return i

    # Test basic thread-safe queuing + cancelling
    # Works seamlessly when not using `trange`
    mw = MonoWorker()
    print()
    results = []
    for i in trange(3):
        mw.submit(foo, i)
        mw.submit(results.append, i)
        if i == 1:
            mw.submit(tqdm_auto.write, 'hello world!')

    print(results)

    # Test max_workers
    mw = MonoWorker()
    print()
    results = []
    for i in trange(3):
        mw.submit(foo, i)
        mw

# Generated at 2022-06-14 13:52:05.557689
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    from concurrent.futures import as_completed
    from ..utils import format_sizeof, format_interval

    mem = lambda: format_sizeof(random.randrange(1, 1000000000))
    clock = time.time()

    def callback(*args, **kwargs):
        time.sleep(1)  # simulation of time-expensive task
        return clock() - time.time()  # callback(start_time=time.time())

    mw = MonoWorker()
    futures = []
    while clock() <= clock() + 3:
        future = mw.submit(callback, clock())
        assert future
        futures.append(future)
        time.sleep(1)
    assert len(mw.futures) >= 2
    assert len(futures) > 2
    all

# Generated at 2022-06-14 13:52:12.998574
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from concurrent.futures import wait, FIRST_EXCEPTION
    import time

    def long_task(_):
        time.sleep(0.3)
        raise Exception("long_task: error")
    def short_task(x):
        time.sleep(0.1)
        return x

    w = MonoWorker()
    done, not_done = wait([w.submit(long_task, None) for _ in range(2)],
                          return_when=FIRST_EXCEPTION)
    # First long task terminated
    assert len(done) == 1
    assert len(not_done) == 1
    # Second long task skipped and cleared
    assert len(w.futures) == 1
    # Submit a short task while waiting long
    res = w.submit(short_task, 10)
    # Short task

# Generated at 2022-06-14 13:52:17.963976
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from itertools import count
    from random import random
    from six.moves import input as get_input

    try:
        from Queue import Queue, Empty
    except ImportError:
        from queue import Queue, Empty  # Python 3

    try:
        from _thread import interrupt_main
    except ImportError:
        from thread import interrupt_main  # Python 3

    def hello():
        sleep(int(random() * 10))
        if random() < .5:
            raise RuntimeError('Hello, World!')
        return 'Hello, World!'

    def thread_worker(q, counter, tq):
        while not q.empty():
            # Acquire a new task
            try:
                task = q.get_nowait()
            except Empty:
                break

# Generated at 2022-06-14 13:52:28.283162
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import random
    import sys
    
    def func(t):
        sleep(t)
        return t
    
    def check():
        w = MonoWorker()
        random.seed(42)
        sys.stderr.write('Checking MonoWorker.submit()...\r')
        
        ts = []
        futs = []
        
        # Submit some tasks
        for i in range(10):
            t = random.random()
            fut = w.submit(func, t)
            ts.append(t)
            futs.append(fut)
        
        # Check that the first three tasks are still running
        for i in range(3):
            assert not futs[i].done()
        
        # Check that the rest tasks are cancelled

# Generated at 2022-06-14 13:52:34.454800
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Import guard
    from time import sleep as time_sleep

    def fn(x):
        time_sleep(0.1)
        return x

    mw = MonoWorker()
    mw.submit(fn, 0)
    sleep_times = [0.001, 0.002, 0.003, 0.004]
    for t in sleep_times:
        time_sleep(t)
        mw.submit(fn, t)
    for i, t in enumerate(sleep_times):
        assert mw.futures[i].result() == t, "Expected: {} got: {}".format(t, mw.futures[i].result())