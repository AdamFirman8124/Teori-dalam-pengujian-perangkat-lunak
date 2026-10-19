

# Generated at 2022-06-14 13:42:50.660903
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    worker = MonoWorker()
    def callback(arg, time=time.sleep):
        time(arg)
        return 'callback(%r)' % arg

    assert not worker.futures, 'initial'
    future0 = worker.submit(callback, 0)
    assert len(worker.futures) == 1, 'len 1'
    future1 = worker.submit(callback, 1)
    assert len(worker.futures) == 2, 'len 2'
    future0.result()
    assert len(worker.futures) == 1, 'len 1 after 0'
    future1.result()
    assert not worker.futures, 'final'
    future2 = worker.submit(callback, 2)
    future3 = worker.submit(callback, 3)
    future3.result()

# Generated at 2022-06-14 13:43:00.864856
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func12(*args, **kwargs):
        pass

    def func34(*args, **kwargs):
        pass

    # Test normal add-remove
    mw = MonoWorker()
    mw.submit(func12, 1, 2)
    assert len(mw.futures) == 1
    mw.submit(func34, 3, 4)
    assert len(mw.futures) == 2
    # Test new function clears waiting
    mw.submit(func12, 1, 2)
    assert len(mw.futures) == 2
    mw.submit(func12, 1, 2)
    assert len(mw.futures) == 1
    # Test new function clears running
    mw = MonoWorker()
    mw.submit(func12, 1, 2)
   

# Generated at 2022-06-14 13:43:11.752935
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .sleep import test_sleep_top
    from time import time
    with MonoWorker() as mw:
        try:
            mw.submit(test_sleep_top, 0.2)

            # scheduler is 'round-robin' -- waiting task
            # takes over after running task is done,
            # and then becomes the running task
            assert len(mw.futures) == 1
            time0 = time()
            mw.submit(test_sleep_top, 0.1)
            assert len(mw.futures) == 1
            time1 = time()
            assert time1 - time0 < 0.2
            assert time1 - time0 >= 0.1
        except Exception:
            raise
        else:
            assert True
            return
    raise RuntimeError

# Generated at 2022-06-14 13:43:22.582733
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()

    def f(x, y=0):
        time.sleep(x)
        if y:
            raise RuntimeError()
        return x

    N = 11
    tb = tqdm_auto.tqdm(total=N)
    for i in range(N):
        mw.submit(f, 2)
        mw.submit(f, 3)
        mw.submit(f, 1, 0)
        mw.submit(f, 1, 1)
        tb.update()
    tb.close()

    def g(x):
        time.sleep(x)
        return x

    mw = MonoWorker()
    tb = tqdm_auto.tqdm(total=N)

# Generated at 2022-06-14 13:43:29.103195
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from queue import Queue
    from contextlib import contextmanager

    @contextmanager
    def external_progress_bar(_):
        yield

    with external_progress_bar('') as external:
        def _submit(mw, i):
            sleep(0.01)
            mw.submit(lambda i: i, i)

        mw = MonoWorker()
        q = Queue()
        with tqdm_auto(total=2, position=external.n, leave=False) as t:
            t.set_description("(%s)" % t.n)

            # two tasks submitted
            q.put(_submit(mw, 0))
            q.put(_submit(mw, 1))
            sleep(0.02)
            t.update()

            # one task submitted
            q

# Generated at 2022-06-14 13:43:38.599700
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import requests
    import tqdm.contrib.concurrent as tqc
    try:
        from urllib.request import urlopen  # Python 3.x
    except ImportError:
        from urllib2 import urlopen  # Python 2.x

    worker = tqc.MonoWorker()
    # Run 3 tasks, but only 1 at a time (most recent is always waiting)
    for i in tqdm_auto.trange(3, desc='test'):
        time.sleep(.5)
        worker.submit(urlopen, requests.compat.urljoin('http://www.', 'ipify.org'))

# Generated at 2022-06-14 13:43:48.050631
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from tqdm import trange
    from threading import Lock

    mw = MonoWorker()
    lock = Lock()

    def test_func(i):
        sleep(1 / (1 + i))
        lock.acquire()
        print()
        print(i)
        print(tqdm_auto.format_sizeof(len(range(i))))
        print()
        lock.release()
        return i

    with trange(8, desc='Test MonoWorker', leave=False) as pbar:
        for i in pbar:
            mw.submit(test_func, i, range(i))

# Generated at 2022-06-14 13:43:56.139094
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # The test depends on sleep, so it may not pass if run too quickly
    import time
    from ..std.testing import _SupportsInterval

    def func(i):
        time.sleep(i)
        return i

    worker = MonoWorker()
    for i in range(10):
        worker.submit(func, i)

    for i in range(0, 5, 0.1):
        time.sleep(0.1)
        assert worker.futures[0].running(), worker.futures[0]
        # The worker is running the last task
        assert i <= worker.futures[0].result(), worker.futures[0]
        # The running task takes longer than i to complete
        assert worker.futures[0] == worker.pool.running(), worker.futures


# Generated at 2022-06-14 13:44:03.626940
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Lock
    lock = Lock()
    time.sleep(0.000001)  # w/o this doesn't capture
    def flush():
        with lock:
            tqdm_auto.write('FLUSH')

    mono_worker_object = MonoWorker()

    for i in range(5):
        mono_worker_object.submit(flush)
        time.sleep(0.5)

    for future in mono_worker_object.futures:
        future.result()


# Generated at 2022-06-14 13:44:10.067658
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Lock

    lock = Lock()
    with lock:
        func = lambda i: (print("thread {0} acquired lock".format(i)),
                          sleep(i), print("thread {0} released lock".format(i)))
        w = MonoWorker()
        w.submit(func, 1)
        sleep(0.1)
        w.submit(func, 2)
        sleep(0.1)
        w.submit(func, 3)
        sleep(0.1)
        w.submit(func, 4)
        sleep(0.1)

# if __name__ == "__main__":
#     test_MonoWorker_submit()

# Generated at 2022-06-14 13:44:25.398227
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:44:30.138604
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    worker = MonoWorker()
    assert len(worker.futures) == 0
    assert worker.submit(time.sleep, 3600)
    assert len(worker.futures) == 1
    assert worker.submit(time.sleep, 3600)
    assert len(worker.futures) == 2
    assert worker.submit(time.sleep, 3600)
    assert len(worker.futures) == 2

# Generated at 2022-06-14 13:44:37.872096
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
  # Initialize a MonoWorker
  mono_worker = MonoWorker()

  # run the function
  def func1():
    for i in tqdm_auto.trange(10):
      import time
      time.sleep(1)
  mono_worker.submit(func1)

  # run the function
  def func2():
    for i in tqdm_auto.trange(10):
      import time
      time.sleep(1)
  mono_worker.submit(func2)

if __name__ == "__main__":
  test_MonoWorker_submit()

# Generated at 2022-06-14 13:44:43.759024
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def task(a):
        time.sleep(a)


    def test(n, x):
        t = time.time()
        worker = MonoWorker()

        fut = worker.submit(task, n)


        worker.submit(task, x)

        fut.result()
        assert time.time() - t >= x


    test(5, 4)
    test(2, 5)

# Generated at 2022-06-14 13:44:53.301099
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from sys import version_info
    import threading

    def f(x):
        """Blocking function that sleeps for *x* seconds."""
        sleep(x)
        if version_info[0] < 3:  # Python 2
            return repr(threading.current_thread())
        else:  # Python 3
            return repr(threading.current_thread().name)

    # Test that overlapping calls to f use the same thread
    m = MonoWorker()
    m.submit(f, 0.7)  # finish before last object is garbage collected
    for i in range(4):
        t = m.submit(f, 0.7)
        print('Started %3i' % i)
        assert t.result() == repr(threading.current_thread().name)

    # Test that on

# Generated at 2022-06-14 13:44:58.044795
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def foo():
        time.sleep(5)

    mw = MonoWorker()
    for i in range(10):
        mw.submit(foo)
    time.sleep(2)
    for i in range(10):
        mw.submit(foo)
    time.sleep(15)

# Generated at 2022-06-14 13:45:08.225833
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import traceback

    def f(x):
        sleep(x)
        return x

    def g(x):
        raise ValueError("x={}".format(x))

    def h(x):
        if x == 10:
            raise ValueError("x=10")
        sleep(x)
        return x

    def i(x):
        sleep(x)
        if x == 10:
            raise ValueError("x=10")
        return x

    def j(x):
        sleep(x)
        if x == 10:
            raise ValueError("x=10")
        return x

    def k(x):
        if x == 10:
            raise ValueError("x=10")
        return x

    async_func_list = [f, g, h, i, j, k]

# Generated at 2022-06-14 13:45:16.818466
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    # Decorate _time.sleep to show progress bar
    def time_sleep(sec):
        for _ in tqdm_auto.trange(sec):
            time.sleep(1)

    def func(x, y):
        return x + y

    mw = MonoWorker()
    for _ in range(3):
        # Submit a task,
        # which may replace currently waiting task
        mw.submit(time_sleep, 1)

    # Submit a task,
    # which always replaces currently running task
    for _ in range(3):
        mw.submit(func, 1, 3)

# Generated at 2022-06-14 13:45:23.405834
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import unittest

    class TestMonoWorker(unittest.TestCase):
        def test_oneoff(self):

            def counter():
                for _ in tqdm_auto.trange(10, ncols=0):
                    time.sleep(.1)

            mw = MonoWorker()
            mw.submit(counter)
            time.sleep(.5)
            mw.submit(tqdm_auto.write, "one")
            time.sleep(.5)
            mw.submit(tqdm_auto.write, "two")
            time.sleep(.5)
            mw.submit(tqdm_auto.write, "three")
            mw.submit(counter)
            time.sleep(2)

# Generated at 2022-06-14 13:45:29.174371
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    worker = MonoWorker()
    future1 = worker.submit(lambda x:x, 1)
    future2 = worker.submit(lambda x:x, 2)
    assert future1.done()
    assert future1.result() == 1
    assert not future2.done()
    future3 = worker.submit(lambda x:x, 3)
    assert not future2.done()
    assert not future3.done()



# Generated at 2022-06-14 13:45:44.271440
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep as time_sleep
    from unittest import TestCase

    class TestMonoWorker(TestCase):
        def test_submit(self):
            def f(text):
                time_sleep(1)
                return text

            worker = MonoWorker()
            self.assertEqual(True, worker.submit(f, 'a').result())
            self.assertEqual(True, worker.submit(f, 'b').result())
            self.assertEqual(True, worker.submit(f, 'c').result())
            self.assertEqual(True, worker.submit(f, 'd').result())

    TestMonoWorker('test_submit').test_submit()

# Generated at 2022-06-14 13:45:55.471563
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys
    import re
    import threading
    from tqdm.utils import get_ipython

    if not get_ipython():
        raise unittest.SkipTest("MonoWorker can only be tested in IPython")

    def run_test(test_id, **kwargs):
        from IPython.display import clear_output
        from tqdm._tqdm_gui import tqdm

        time.sleep(0.01)
        mw = MonoWorker()

        def func():
            time.sleep(0.01)
            return 1

        def func_e():
            raise Exception("Error: " + test_id)

        def func_c():
            time.sleep(0.01)
            return -1

        def func_i():
            time.sleep(0.01)

# Generated at 2022-06-14 13:46:05.211536
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    class dummy:
        t = 0
        def task(self):
            sleep(1)
            self.t += 1
    
    d = dummy()
    m = MonoWorker()
    t = m.submit(d.task)
    assert t.done()
    assert d.t == 1

    m.submit(d.task)
    assert t.done()
    assert d.t == 1

    m.submit(d.task)
    assert not t.done()
    assert d.t == 1

    m.submit(d.task)
    assert not t.done()
    assert d.t == 1

# Generated at 2022-06-14 13:46:15.824835
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys
    from ..utils import _supports_unicode
    from ..auto import tqdm
    with tqdm(total=3) as bar:
        bar.set_description("STARTING")
        mw = MonoWorker()

        def task1(name, delay=0.5):
            time.sleep(delay)
            return "task1: " + name

        def task2(delay=0.5):
            time.sleep(delay)
            return "task2 (no name)"

        def task3(name):
            return "task3: " + name

        def task4(name):
            bar.set_description(name)

        def task5():
            return "task5 (no args)"

        def task6(name):
            return "task6: " + name


# Generated at 2022-06-14 13:46:24.946750
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from tqdm.utils import _term_move_up

    def func(sleep_time):
        sleep(sleep_time)
        return sleep_time

    max_workers = 3
    pool = MonoWorker()

    # Case : one full queue
    for i in range(max_workers):
        pool.submit(func, (i+1)/max_workers)
        tqdm_auto.write(repr(pool.futures))
    # Case : try to append to a full queue
    pool.submit(func, 0)
    tqdm_auto.write(repr(pool.futures))
    # Case : try to append to the queue after an execution
    sleep(0.5)
    pool.submit(func, 0.5)

# Generated at 2022-06-14 13:46:36.286870
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    class TestWorker(MonoWorker):
        def test_func(self):
            sleep(1)
            return True

    test = TestWorker()
    assert len(test.futures) == 0
    # submit first task
    tqdm_auto.write('work {} started'.format(0))
    assert len(test.futures) == 0
    test.submit(test.test_func)
    assert len(test.futures) == 1
    running = test.futures[0]
    assert not running.done()
    # submit second task
    tqdm_auto.write('work {} started'.format(1))
    test.submit(test.test_func)
    assert len(test.futures) == 2
    running, waiting = test.futures

# Generated at 2022-06-14 13:46:45.770656
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys

    mw = MonoWorker()

    def foo(i):
        time.sleep(i)
        return i

    # Submits the first job
    t1 = time.time()
    fut1 = mw.submit(foo, 1)
    t2 = time.time()
    assert fut1.result() == 1
    t3 = time.time()
    assert t2 - t1 < 1.0 < t3 - t1

    # Submits a second job before the first is finished
    t1 = time.time()
    fut2 = mw.submit(foo, 2)
    t2 = time.time()
    assert fut2.result() == 2
    t3 = time.time()
    assert t2 - t1 < 1.0 < t3 - t1

    # Submits

# Generated at 2022-06-14 13:46:52.647428
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(x):
        time.sleep(x)
        return x

    import time
    from ..utils import format_sizeof
    tqdm_auto.write(format_sizeof(MonoWorker()))  # ensure no memory leak
    # single invocation
    a = MonoWorker()
    a.submit(lambda: func(0.5))
    a.submit(lambda: func(0.1))
    a.submit(lambda: func(0.2))
    a.submit(lambda: func(0.3))
    assert a.futures[0].result() == 0.3
    # concurrent invocations
    b = MonoWorker()
    b.submit(lambda: func(0.5))
    b.submit(lambda: func(0.1))
    time.sleep(0.05)  #

# Generated at 2022-06-14 13:47:03.065214
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:47:08.008441
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(x):
        import os
        import time
        time.sleep(0.1)
        return (x, os.getpid())

    mw = MonoWorker()
    for x in range(10):
        f = mw.submit(func, x)
    assert f.result() == (9, os.getpid())

# Generated at 2022-06-14 13:47:25.982927
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from contextlib import contextmanager

    worker = MonoWorker()  # pylint: disable=invalid-name
    counter = 0
    @contextmanager
    def sleep_context(seconds=2, count=[0]):
        """Just for testing"""
        time.sleep(seconds)
        count[0] += 1
        yield
        count[0] -= 1

    def submit_sleep():
        """Just for testing"""
        global counter
        counter += 1
        return worker.submit(sleep_context, seconds=2)

    # Verify current behaviour:
    with submit_sleep():
        assert counter == 1
    assert counter == 0
    # Verify new behaviour:
    with submit_sleep():
        assert counter == 1
    with submit_sleep():
        assert counter == 1
        time.sleep(1)

# Generated at 2022-06-14 13:47:34.972895
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def sleep(t=1):
        """Sleep for t seconds and return t."""
        import time
        time.sleep(t)
        return t

    def check_tqdm(t=1):
        """Sleep for t seconds and return t (using tqdm)."""
        with tqdm_auto.tqdm(unit='sec', desc='check') as t:
            t.update(sleep(t))

    worker = MonoWorker()
    try:
        from queue import Empty
    except ImportError:  # Python 2
        from Queue import Empty

    for _ in tqdm_auto.trange(3):
        import random
        # pylint: disable=protected-access
        for _ in tqdm_auto.trange(10):
            t = random.random()

# Generated at 2022-06-14 13:47:46.210283
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    # Check that the waiting task is the most recent submitted task
    def _check_waiting(waiting1, waiting2, waiting3=False):
        worker = MonoWorker()
        start = time.time()
        worker.submit(sleep_func, 5, 0.5)  # running
        worker.submit(sleep_func, 4, True)  # waiting
        worker.submit(sleep_func, 3, waiting1)  # discard
        worker.submit(sleep_func, 2, waiting2)  # discard
        worker.submit(sleep_func, 1, waiting3)  # discard
        waiting = worker.futures[-1]  # get the waiting task
        result = waiting.result()
        assert result == waiting2
        end = time.time()
        assert end-start < 5

    _check_

# Generated at 2022-06-14 13:47:55.311877
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import threading, queue
    import time
    import logging

    logger = logging.getLogger('MonoWorker')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

    import sys
    import bz2
    import traceback

    def get_traceback():
        etype, value, tb = sys.exc_info()
        return bz2.compress(
            ''.join(traceback.format_exception(etype, value, tb)).encode())

    def _log(msg):
        logger.info(msg)

    def _exception(msg):
        logger.error(msg)

    def _decomp_log(msg):
        _log(bz2.decompress(msg).decode())


# Generated at 2022-06-14 13:48:02.724491
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    m = MonoWorker()
    assert (m.submit(input, "Waiting ")  # interactive
            .result() == "Waiting ...")
    assert (m.submit(input, "Running ")
            .result() == "Running ...")
    assert (m.submit(input, "Discarded")
            .cancelled() == True)
    assert (m.submit(input, "Waiting ")  # interactive
            .result() == "Waiting ...")
    assert (m.submit(input, "Running ")
            .result() == "Running ...")

# Generated at 2022-06-14 13:48:10.353999
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import format_sizeof

    def slow_add(a, b):
        time.sleep(0.5)
        return a + b

    mw = MonoWorker()

    # submit many tasks (only most recent one will actually run)
    for i in tqdm_auto.tqdm(range(100), desc=format_sizeof(1e6)):
        mw.submit(slow_add, i, 1)

    # force running all tasks
    for f in mw.futures:
        if not f.done():
            f.result()

# Generated at 2022-06-14 13:48:18.958531
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .test_tqdm import SlowTestException

    def test_func(a, b):
        sleep(.2)
        if b == 5:
            raise SlowTestException('Test Exception')
        return a + b

    mw = MonoWorker()
    # Test 1st Task
    task_a = mw.submit(test_func, 1, 2)
    assert task_a.result() == 3
    # Test 2nd Task
    task_b = mw.submit(test_func, 3, 4)
    assert task_b.result() == 7
    # Test cancellation of task_a
    assert task_a.cancel()
    # Test replacement of task_b
    task_c = mw.submit(test_func, 5, 6)

# Generated at 2022-06-14 13:48:29.486165
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import os
    def monotonic():
        return time.time()
    worker = MonoWorker()
    assert len(worker.futures) == 0
    time.sleep(1 / 500)
    time0 = monotonic()
    worker.submit(time.sleep, 0.5)
    assert len(worker.futures) == 1
    time.sleep(1 / 500)
    time1 = monotonic()
    assert time0 < time1
    assert (time1 - time0) < 0.5

    time.sleep(1 / 500)
    time2 = monotonic()
    assert time1 < time2
    assert (time2 - time1) < 0.5

    task1 = worker.submit(os.getpid)

    time.sleep(1 / 500)

# Generated at 2022-06-14 13:48:36.506821
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def foo():
        sleep(0.5)
        return "foo"

    def bar():
        sleep(1)
        return "bar"

    def baz():
        sleep(2)
        return "baz"

    mw = MonoWorker()
    f1 = mw.submit(foo)
    f2 = mw.submit(bar)
    f3 = mw.submit(baz)
    print(f1.result(), f2.result(), f3.result())
    f4 = mw.submit(foo)
    f5 = mw.submit(bar)
    print(f4.result(), f5.result())

# Generated at 2022-06-14 13:48:44.605894
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import multiprocessing
    import numpy as np
    # Test if there is no error in running
    def test_submit(func, name, n_proc=2, wait_time=0.1):
        mono_workers = [
            MonoWorker() for _ in range(n_proc)]
        for i in tqdm_auto.trange(n_proc, desc=name):
            mono_workers[i].submit(func, wait_time)

    test_submit(time.sleep, "time.sleep")
    test_submit(time.sleep, "time.sleep", n_proc=4)
    test_submit(
        time.sleep, "time.sleep", n_proc=4, wait_time=0.01)

# Generated at 2022-06-14 13:49:06.950411
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from tqdm.contrib import enumerate_with
    from unittest.case import TestCase

    class TestCaseMonoWorker(TestCase):
        def test1(self):
            try:
                from Queue import Queue
            except ImportError:
                from queue import Queue
            q = Queue()
            mw = MonoWorker()
            mw.submit(time.sleep, 0.3)
            mw.submit(q.put, 0)
            q.get()
            mw.submit(q.put, 1)
            self.assertEqual(q.get(), 1)

        def test2(self):
            q = deque()
            mw = MonoWorker()
            mw.submit(time.sleep, 0.3)

# Generated at 2022-06-14 13:49:17.325710
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:49:28.935942
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from multiprocessing import Process
    from threading import Thread
    from queue import Queue
    from typing import cast

    from .utils import _call

    # Test initial state
    mw = MonoWorker()
    assert len(mw.futures) == 0

    # Create a background thread to verify that it only ever runs one at a time
    q = Queue()  # type: ignore  # pylint: disable=unsubscriptable-object

    def adder(a, b, mw):
        q.put(mw.submit(lambda x, y: x + y, a, b).result())

    # Test MonoWorker with one thread
    adder(1, 2, mw)
    assert q.get() == 3
    adder(3, 4, mw)
    assert q

# Generated at 2022-06-14 13:49:31.353288
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .utils import _test_MonoWorker_submit
    _test_MonoWorker_submit(MonoWorker)

# Generated at 2022-06-14 13:49:39.362840
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import multiprocessing
    from time import sleep

    def f(n, s):
        sleep(s)
        return n

    m = MonoWorker()
    f1 = m.submit(f, 1, 2)
    f2 = m.submit(f, 2, 1)
    f3 = m.submit(f, 3, .5)
    f4 = m.submit(f, 4, .1)
    assert multiprocessing.active_children()  # == [multiprocessing.Process(f4)]
    assert [f.result() for f in (f1, f2, f3, f4)] == [4, 4, 4, 4]
    assert not multiprocessing.active_children()

# Generated at 2022-06-14 13:49:49.484616
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Lock
    from time import sleep
    from .example import test_case_1 as func
    lock = Lock()

    # test no waiting task
    m = MonoWorker()
    m.submit(func, 0, lock)
    assert len(m.futures) == 1
    assert not m.futures[0].done()

    # test pop waiting task
    m.submit(func, 1, lock)
    assert len(m.futures) == 2
    assert not m.futures[0].done()
    assert not m.futures[1].done()

    sleep(0.5)
    assert len(m.futures) == 2
    assert m.futures[0].done()
    assert not m.futures[1].done()

    m.fut

# Generated at 2022-06-14 13:49:59.464392
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    # pylint: disable=unused-argument,dangerous-default-value,redefined-outer-name,unused-variable
    def badfunc():
        raise Exception("Intentional error")
    def func1(x):
        sleep(0.1)
        return x + 1
    def func2(x):
        sleep(0.1)
        return x + 2

    mw = MonoWorker()
    assert len(mw.futures) == 0
    assert mw.submit(badfunc) is None  # no waiting task to discard
    assert len(mw.futures) == 0

    assert mw.submit(func1, 1).result() == 2  # no waiting task to discard
    assert len(mw.futures) == 1

    assert mw.submit

# Generated at 2022-06-14 13:50:07.304054
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Tests MonoWorker.submit"""
    import time  # Needed for output reprisals

    def echo(msg, duration):
        """Simulates a running task."""
        tqdm_auto.write(msg)
        time.sleep(duration)

    def test_submit(args):
        """Tests MonoWorker.submit."""
        monoworker = MonoWorker()
        last_msg = None
        for message, duration in args:  # pylint: disable=unused-variable
            last_msg = message
            future = monoworker.submit(echo, message, duration)
            if not future:
                tqdm_auto.write("# Task canceled: %s" % message)
        time.sleep(3)  # For option "repeat"
        if last_msg:
            tqdm

# Generated at 2022-06-14 13:50:16.383003
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def _f(t):
        sleep(t)
        return t

    mw = MonoWorker()
    assert mw._pool._threads  # pylint: disable=protected-access
    assert not mw.futures  # pylint: disable=protected-access
    future = mw.submit(_f, 0.1)
    sleep(0.03)
    assert len(mw.futures) == 1
    assert not mw.futures[0].done()
    assert mw.pool._threads  # pylint: disable=protected-access
    future = mw.submit(_f, 0.2)
    sleep(0.03)
    assert len(mw.futures) == 2
    assert mw.futures[0].done()


# Generated at 2022-06-14 13:50:26.748444
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import threading

    pool = ThreadPoolExecutor(max_workers=1)
    mw = MonoWorker()
    futures = {}

    def start_task(name, duration):
        def task():
            time.sleep(duration)
            # tqdm_auto.write("{} finished after {}.".format(name, duration))
        futures[name] = pool.submit(task)

    threads = []

    # queue-1
    start_task("job_1", 3.0)
    start_task("job_2", 0.5)
    # queue-2
    start_task("job_3", 0.4)
    start_task("job_4", 0.3)
    start_task("job_5", 0.2)
    # queue-3
    start_

# Generated at 2022-06-14 13:50:47.830801
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from collections import Counter
    from concurrent.futures import TimeoutError

    def sleeper(sleep_for):
        sleep(sleep_for)
        return sleep_for

    mw = MonoWorker()
    assert mw.submit(sleeper, 5).result() == 5
    assert mw.submit(sleeper, 3).result() == 3
    assert mw.submit(sleeper, 2).result() == 2
    assert mw.submit(sleeper, 1).result() == 1
    assert mw.submit(sleeper, 0.5).result() == 0.5
    assert mw.submit(sleeper, 0.2).result() == 0.2
    assert mw.submit(sleeper, 0.1).result() == 0.1

# Generated at 2022-06-14 13:50:54.999948
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random
    from itertools import product
    from multiprocessing import current_process
    worker = MonoWorker()
    for seq, f in product([[], [None], [None, None]], [False, True]):
        for do in seq:
            sleep(random())
            if do is not None:
                print(do, current_process(), "waiting")
            if f:
                print(do, current_process(), "running")
                sleep(random())
            if do is not None:
                res = worker.submit(sleep, random())
                print(do, current_process(), "submitted", res)
                if not f:
                    res.result()
            else:
                worker.submit(sleep, random())
            print(do, current_process(), "done")


# Generated at 2022-06-14 13:51:05.417036
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    import tqdm.contrib.concurrency.MonoWorker as MonoWorker
    import tqdm.contrib.concurrency.ThreadWithLogAndExc as ThreadWithLogAndExc
    import tqdm.contrib.util as util
    with util.disconnected():
        def func(i):
            time.sleep(1 / (1 + i))
            return i
        mw = MonoWorker()
        w_progressbar = tqdm_auto.tqdm(leave=False, desc='w',
                                       position=1, mininterval=0)
        r_progressbar = tqdm_auto.tqdm(leave=False, desc='r',
                                       position=2, mininterval=0)
        futures = []

# Generated at 2022-06-14 13:51:14.307449
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Unit test for `MonoWorker.submit`."""
    from concurrent.futures import TimeoutError
    import time
    import sys

    def foo(x, y):
        """Sleep with output."""
        time.sleep(x)
        print(x, y)
        for i in tqdm_auto(list(range(y)), desc='bar' + str(x)):
            time.sleep(x / y)
        sys.stdout.flush()
        return x

    worker = MonoWorker()
    # check that slow jobs are cancelled
    t0 = time.time()
    assert worker.submit(foo, 2, 3) is None
    assert time.time() - t0 < 1
    assert worker.submit(foo, 2, 4) is None
    assert len(worker.futures) == 1

# Generated at 2022-06-14 13:51:19.050219
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Run and test the code, return the exit status"""
    import time
    from ..utils import _range

    def wait(n):
        time.sleep(n / 100)
        return n

    strings = []

    def capture_string(s):
        strings.append(s)

    mw = MonoWorker()

    # basic
    assert len(mw.futures) == 0
    assert mw.submit(wait, 2).result() == 2

    # submit waiting task and wait
    mw.submit(wait, 4)
    assert len(mw.futures) == 1
    assert mw.submit(wait, 8).result() == 8
    assert len(mw.futures) == 1
    assert mw.futures[0].result() == 4

    # submit running and waiting task


# Generated at 2022-06-14 13:51:30.594291
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from nose.tools import eq_, ok_

    def func(duration):
        sleep(duration)
        return duration

    def check(calls, expected_results):
        me = MonoWorker()
        results = list()
        for duration in calls:
            future = me.submit(func, duration)
            if future is not None:
                # (note: in actual use, consume and save results asap)
                results.append(future.result())
        eq_(results, expected_results)

    check([1, 2], [1])
    check([3], [3])
    check([1, 2, 3, 4], [4])
    check([1, 2, 3, 4, 5, 6, 7], [7])

# Generated at 2022-06-14 13:51:40.274243
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from random import random

    def sleep_for_a_while(duration=None):
        duration = duration or 10 * random()
        time.sleep(duration)
        return duration

    # test basic correctness
    w = MonoWorker()
    for i in range(10):
        r = w.submit(sleep_for_a_while)
        assert r.result() > 0

    # test that the most recent result is retained
    w = MonoWorker()
    f1 = w.submit(sleep_for_a_while)
    f2 = w.submit(sleep_for_a_while)
    assert f1.cancelled()
    assert f2.result() > 0

    # test that running tasks are retained
    w = MonoWorker()

# Generated at 2022-06-14 13:51:48.791770
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .util import StatefulTester

    func_calls = []
    def func(*args):
        sleep(0.1)
        func_calls.append(args)

    w = MonoWorker()
    with StatefulTester(w, clean=lambda x: x.pool.shutdown()) as t:
        assert t.state == []
        assert func_calls == []
        fut0 = t.worker.submit(func, 1)
        assert t.state == [fut0]
        assert func_calls == []
        sleep(0.05)
        assert t.state == [fut0]
        assert func_calls == []
        fut1 = t.worker.submit(func, 2)
        assert t.state == [fut1]

# Generated at 2022-06-14 13:51:55.022006
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    from concurrent.futures import Future
    import multiprocessing
    try:
        mp = multiprocessing.get_context('spawn')
    except Exception:
        mp = multiprocessing

    def func(id):
        print("Starting", id)
        time.sleep(1)
        print("Finish", id)

    def func2(id):
        print("Starting", id)
        time.sleep(2)
        print("Finish", id)

    def wait(futures, state=None):
        for f in futures:
            assert isinstance(f, Future)
            assert isinstance(f.done(), bool)
            if state is None or f.done() is state:
                f.result()  # wait for completion


# Generated at 2022-06-14 13:52:04.536266
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .__init__ import assert_eq_

    # Test sequential, forked, & concurrency
    for _ in tqdm_auto(range(3)):
        worker = MonoWorker()
        assert_eq_(worker.futures, deque([]))

        def long_running_fn(i):
            sleep(i)
            return i

        for _ in tqdm_auto(range(10)):
            i = len(worker.futures)
            f = worker.submit(long_running_fn, i)
            assert_eq_(f.result(), i)
            assert_eq_(worker.futures, deque([f]))

        assert_eq_(len(worker.futures), 1)