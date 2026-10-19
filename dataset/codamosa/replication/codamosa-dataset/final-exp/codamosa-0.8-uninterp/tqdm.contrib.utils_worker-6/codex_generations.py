

# Generated at 2022-06-14 13:42:43.909170
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    mw = MonoWorker()
    assert len(mw.futures) == 0

# Generated at 2022-06-14 13:42:52.779717
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event, Lock
    from time import time

    # decorator for thread safety
    lock = Lock()

    def with_lock(func):
        def wrapper(*args, **kwargs):
            with lock:
                return func(*args, **kwargs)
        return wrapper

    @with_lock
    def append_with_ts(lst, val):
        lst.append((val, time()))

    # wait 3s, append 1s and 2s, wait 3s, append 3s and 4s
    def wait_append(lst1, append_ts, delay, n):
        sleep(delay)
        for _ in range(n):
            sleep(1)
            append_ts(lst1, delay)

    # wait 3s and then start append 1s and 2s, then

# Generated at 2022-06-14 13:43:01.877216
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from unittest import TestCase

    def func():
        sleep(0.1)
        return 1

    class TestMonoWorker(TestCase):
        def runTest(self):
            th = MonoWorker()

            # test that only one task is working at the same time
            th.submit(func)
            sleep(0.05)
            th.submit(func)
            sleep(0.05)
            self.assertEqual(len(th.futures), 1, "one task should be waiting")

            # test that waiting task is the most recent task,
            # and waiting tasks before that get discarded
            th.submit(func), sleep(0.05)
            th.submit(func), sleep(0.05)
            th.submit(func), sleep(0.05)

# Generated at 2022-06-14 13:43:10.198178
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    # noinspection PyGlobalUndefined
    global global_res

    def func():
        time.sleep(1)
        # noinspection PyGlobalUndefined
        global global_res
        global_res = True

    global_res = False
    worker = MonoWorker()
    worker.submit(func)
    worker.submit(func)  # this should be discarded
    assert not global_res
    assert len(worker.futures) == 1
    assert not global_res
    worker.futures[0].result()
    assert global_res

# Generated at 2022-06-14 13:43:17.680834
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    mw = MonoWorker()
    f1 = mw.submit(lambda: 1)
    f2 = mw.submit(lambda: 2)
    f3 = mw.submit(lambda: 3)
    f4 = mw.submit(lambda: 4)

    assert f1 == f3 == f4
    assert f2.cancelled()

    f5 = mw.submit(lambda: 5)
    f6 = mw.submit(lambda: 6)

    assert f1.done()
    assert f5 == f6
    assert f3.done()

    assert f1.result() == 1
    assert f5.result() == 5
    assert f2.cancelled()
    assert f3.result() == 3
    assert f4.result() == 4
    assert f6.result() == 6



# Generated at 2022-06-14 13:43:28.362899
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    mw = MonoWorker()
    assert len(mw.futures) == 0
    f1 = mw.submit(sleep, 1)
    assert len(mw.futures) == 1
    mw.submit(sleep, 2)
    assert len(mw.futures) == 1
    f2 = mw.submit(sleep, 2)
    assert len(mw.futures) == 1
    f3 = mw.submit(sleep, 3)
    assert len(mw.futures) == 1
    for f in [f1, f2, f3]:
        assert not f.done()
    f3.cancel()
    assert not f1.done()
    assert not f2.done()
    f2.cancel()
    assert f1

# Generated at 2022-06-14 13:43:35.189693
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def lambda_f(x):
        import time
        time.sleep(0.5 * x)
        return x

    mw = MonoWorker()
    mw.submit(lambda_f, 0.1)
    mw.submit(lambda_f, 0.2)
    mw.submit(lambda_f, 0.3)
    assert mw.futures[0].result() == 0.3, str(mw.futures)

# Generated at 2022-06-14 13:43:44.035125
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():  # pragma: no cover
    from time import sleep
    from calendar import timegm
    from datetime import datetime
    from threading import Thread
    import unittest
    import uuid

    # All variables accessed by threads are protected by lock
    # It uses a lock to make all operations atomic
    lock = ThreadPoolExecutor(max_workers=1)

    # Unique identifer of this test
    test_uid = uuid.uuid4()
    # Start time of this test
    start_time = timegm(datetime.now().utctimetuple())

    # Logging function

# Generated at 2022-06-14 13:43:52.715244
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from ..utils import _term_move_up
    from ..utils import format_sizeof
    import time
    import random

    def task(l, *args, **kwargs):
        for i in range(random.randint(1, 5)):
            l.append(i)
            with tqdm_auto.external_write_mode():
                tqdm_auto.write("{}/{}".format(format_sizeof(i),
                                               format_sizeof(5)), end='')
            _term_move_up()
            time.sleep(0.2)
        return l

    mw = MonoWorker()
    l = [i for i in range(5)]
    mw.submit(task, l, total=5)  # first task
    time.sleep(0.2)  #

# Generated at 2022-06-14 13:43:59.749403
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    mono_worker = MonoWorker()
    try:
        for i in range(4):
            mono_worker.submit(sleep, 4 - i)
            for _ in range(4):
                sleep(1)
                print('.', end='')
            print('')
    except KeyboardInterrupt:
        pass
    print('OK')

if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:44:05.309676
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import concurrent.futures
    import time

    MonoWorker.submit(time.sleep, 1)
    sleep2 = MonoWorker.submit(time.sleep, 2)
    sleep3 = MonoWorker.submit(time.sleep, 3)
    assert sleep2.done()
    assert sleep3.done()



# Generated at 2022-06-14 13:44:11.071752
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():  # pragma: no cover
    from operator import add, sub
    from time import sleep

    def wait(t):
        sleep(t)
        return t

    mw = MonoWorker()

    # test pending task
    assert mw.submit(add, 3, 5)
    
    sleep(0.01)  # Wait for thread to start

    # test lack of task replace
    assert mw.submit(sub, 3, 5)

    sleep(0.01)  # Wait for thread to start

    # test task replace
    assert mw.submit(wait, 1)

    sleep(0.01)  # Wait for thread to start

    # test lack of task replace

# Generated at 2022-06-14 13:44:15.941563
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    mw = MonoWorker()
    from tqdm.auto import tqdm
    for i in tqdm(range(2)):
        print('\ni:', i)
        # print('\nSubmit new task:', i)
        mw.submit(sleep, 1)
        # print('\nSubmit new task:', i+1)
        mw.submit(sleep, 1)
        print('\n')


# Generated at 2022-06-14 13:44:24.096586
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event
    import time
    mw = MonoWorker()
    event = Event()
    sum = 1
    def set_event():
        nonlocal sum
        sum += 1
        time.sleep(0.1)  # make sure it runs for a while
        event.set()
    mw.submit(set_event)
    event.wait()
    assert sum == 2
    sum = 1
    wait_event = Event()
    event.clear()
    def set_event_then_wait():
        nonlocal wait_event
        set_event()
        wait_event.set()
        event.wait()
    mw.submit(set_event_then_wait)
    wait_event.wait()
    assert sum == 2
    wait_event.clear()
    event.clear()
    mw

# Generated at 2022-06-14 13:44:31.927775
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from .testing import fake_tqdm
    import time

    _test_sleep = 1.0

    mw = MonoWorker()
    with fake_tqdm(total=1) as f:
        mw.submit(time.sleep, _test_sleep)
        f.update()

        mw.submit(time.sleep, _test_sleep)
        f.update()
        mw.submit(time.sleep, _test_sleep)
        f.update()

        mw.submit(time.sleep, _test_sleep)
        f.update()
        mw.submit(time.sleep, _test_sleep)
        f.update()
        mw.submit(time.sleep, _test_sleep)
        f.update()

    assert len(f._instances) == 2
    f._instances

# Generated at 2022-06-14 13:44:37.021773
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def f(time_):
        time.sleep(time_)
        return time_

    mw = MonoWorker()
    mw.submit(f, 2)
    res = mw.submit(f, 1)
    assert res.result() == 1
    assert mw.futures.pop().result() == 1

# Generated at 2022-06-14 13:44:47.497661
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from unittest import TestCase

    def test_func():
        sleep(5)
        return 1

    test_obj = MonoWorker()
    test_future = test_obj.submit(test_func)
    test_future.cancel()
    assert test_future.cancelled()

    test_obj.submit(test_func)
    test_future = test_obj.submit(test_func)
    test_future.cancel()
    assert test_future.cancelled()

    # Both running and waiting tasks are available at the same time
    test_obj.submit(test_func)
    test_obj.submit(test_func)
    test_future = test_obj.submit(test_func)
    assert not test_future.cancelled()
    test_future.cancel

# Generated at 2022-06-14 13:44:55.869858
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def f(x):
        time.sleep(x)
        return x

    worker = MonoWorker()
    # Submit a task to run:
    future = worker.submit(f, 2)
    result = future.result()
    assert result == 2, result
    # Submit another task to just wait:
    future2 = worker.submit(f, 1)
    assert future2.result() == 1
    # Submit a task to replace currently waiting task:
    future3 = worker.submit(f, 3)
    assert future2.result() == 3

# Generated at 2022-06-14 13:45:06.972978
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    import threading
    import time
    from ..utils import _term_move_up

    old_stdout = sys.stdout
    sys.stdout = open('/dev/null', 'w')

    def _mock_time_sleep(n):
        time.sleep(n)
        return n

    def _mock_input(inpt):
        def _mock_input_f(*args, **kwargs):
            return inpt
        return _mock_input_f

    # Mock input and sleep for testing
    time_sleep = time.sleep
    time.sleep = _mock_time_sleep
    input = input
    input = _mock_input(0)

    def _run_test(wait_time):
        out = []

        def _test_write(s):
            out

# Generated at 2022-06-14 13:45:17.125911
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import subprocess
    import time
    import sys
    import warnings

    try:
        subprocess.run(['sleep', '1'], check=True)
    except Exception:  # noqa
        # Python <3.5 or Windows
        warnings.warn('Skip test_MonoWorker_submit')
    else:
        def snow(t):
            time.sleep(t)
            print('snow(%s)' % t)

        mw = MonoWorker()

        t0 = time.time()
        f1 = mw.submit(snow, 1)
        f2 = mw.submit(snow, 2)
        f4 = mw.submit(snow, 4)
        f2.result()  # wait for f2 to complete
        f3 = mw.submit(snow, 3)



# Generated at 2022-06-14 13:45:32.611960
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys

    # Tests running job with waiting job.
    def test_1():
        # set up
        mw = MonoWorker()
        running = mw.submit(lambda x: sys.stdout.write('running {}\n'.format(x)), 'running')
        waiting = mw.submit(lambda x: sys.stdout.write('waiting {}\n'.format(x)), 'waiting')
        running.result()
        waiting.result()

    # Tests running job without waiting job.
    def test_2():
        # set up
        mw = MonoWorker()
        running = mw.submit(lambda x: sys.stdout.write('running {}\n'.format(x)), 'running')
        running.result()

    # Tests running job with over-length waiting queue.

# Generated at 2022-06-14 13:45:42.385595
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    # simulates execution of a lengthy task
    def sleep(n, ignore=None):
        time.sleep(n)
        return n

    def run_test(bar, i, mw):  # pragma: no cover
        n = random.uniform(0.5, 1)
        start_time = time.time()
        # submit with waiting
        future = mw.submit(sleep, n, None)
        bar.update(1)
        # progress update
        i += 1
        time_to_run = time.time() - start_time

# Generated at 2022-06-14 13:45:46.115602
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import unittest
    from unittest import mock

    class TestSubmit(unittest.TestCase):
        def test_submit(self):
            with mock.patch('time.sleep'):
                mw = MonoWorker()
                assert mw.submit(time.sleep, 0.1).result() is None

    unittest.main(module=__name__, failfast=True, exit=False)

# Generated at 2022-06-14 13:45:54.758967
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    import time

    def foo(T):
        for i in range(T):
            time.sleep(1.0)

    def bar(T):
        for i in range(T):
            time.sleep(1.0)

    mw = MonoWorker()
    mw.submit(foo, 10)
    print("foo(10) submitted")
    mw.submit(bar, 10)
    print("bar(10) submitted")
    mw.submit(foo, 10)
    print("foo(10) submitted")


if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:46:03.493869
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test MonoWorker.submit"""
    def func(*args, **kwargs):
        return args + tuple(kwargs.items())
    mw = MonoWorker()
    q = mw.submit(func, 1, 2, 3, a=4, b=5, c=6)
    assert q.result() == ((1, 2, 3), ('a', 4), ('b', 5), ('c', 6))
    q = mw.submit(func, 3, 4, 5, a=6, b=7, c=8)
    assert q.result() == ((3, 4, 5), ('a', 6), ('b', 7), ('c', 8))
    # Same args, same task
    q = mw.submit(func, 3, 4, 5, a=6, b=7, c=8)

# Generated at 2022-06-14 13:46:08.055744
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def f(t, i):
        sleep(t)
        return i

    worker = MonoWorker()
    res = []
    for i in range(4):
        worker.submit(f, 1, i)
    for i in range(4):
        res.append(worker.futures[0].result())
    for i in range(4):
        assert res[i] == i

# Generated at 2022-06-14 13:46:18.218112
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    from ..utils import format_sizeof

    def print_task(i, *args, **kwargs):
        time.sleep(0.02)
        tqdm_auto.write("#{} '{}' '{}'".format(i,
                                               format_sizeof(args),
                                               format_sizeof(kwargs)))

    worker = MonoWorker()
    for i in tqdm_auto.trange(4, desc='Outer'):
        worker.submit(print_task, i, args=i, kwargs={str(i): i})

    worker.pool.shutdown()
    assert len(worker.futures) <= 1
    assert all(map(lambda fut: fut.done(), worker.futures))

# Generated at 2022-06-14 13:46:26.665026
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import format_interval
    from ..utils import time_to_next_multiple

    def time_consuming():
        time.sleep(1)

    def sleep(n):
        time.sleep(n)

    def busy_sleep(n):
        start = time.time()
        for _ in tqdm_auto(range(n * 1000000), total=n * 1000000):
            pass
        assert time.time() - start >= n

    def busy_sleep_loop(n, t=0.05):
        start = time.time()
        for _ in tqdm_auto(range(n * 1000000), total=n * 1000000):
            time.sleep(t)
        assert time.time() - start >= n


# Generated at 2022-06-14 13:46:33.462345
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def wait_3s(i):
        import time
        time.sleep(3)
        return i

    mw = MonoWorker()
    assert mw.submit(wait_3s, 0) == 0
    assert mw.submit(wait_3s, 1) == 1
    assert mw.submit(wait_3s, 2) == 1
    assert mw.submit(wait_3s, 3) == 3
    assert mw.submit(wait_3s, 4) == 4

# Generated at 2022-06-14 13:46:44.158610
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import Queue
    from itertools import count
    c = count(start=1)

    def func(i, q):
        sleep(1 - (i % 2))
        tqdm_auto.write("Executing {}...".format(i))
        q.put(i)

    q = Queue()
    mw = MonoWorker()
    for i in range(4):
        mw.submit(func, next(c), q)
        c.send(None)
    q.get(timeout=2)
    q.get(timeout=2)
    q.get(timeout=2)
    # Output:
    #   Executing 1...
    #   Executing 2...
    #   Executing 4...

# Generated at 2022-06-14 13:46:54.368849
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    worker = MonoWorker()
    for i in tqdm_auto.tqdm(range(5)):
        time.sleep(0.3)
        worker.submit(time.sleep, 2)
        time.sleep(0.1)

# Generated at 2022-06-14 13:47:01.800003
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def func1(msg):
        tqdm_auto.write(msg)
        time.sleep(1)
    def func2(msg):
        tqdm_auto.write(msg)
        time.sleep(2)
    def func3(msg):
        tqdm_auto.write(msg)
        time.sleep(3)

    worker = MonoWorker()
    worker.submit(func1,'hello')
    worker.submit(func2,'world')
    worker.submit(func3,'!')
    time.sleep(2)

# Generated at 2022-06-14 13:47:10.269944
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import gc
    from multiprocessing import Queue
    q = Queue()
    worker = MonoWorker()

    def wait_until(t, func, *args, **kwargs):
        try:
            while func(*args, **kwargs) and t > 0:
                sleep(0.1)
                t -= 0.1
        finally:
            q.put(t)

    def submit(i):
        for j in range(2):
            future = worker.submit(wait_until, 60, q.empty)
            assert future == worker.futures[-1]

    fail = False
    try:
        submit(i)
        gc.collect()
    except AssertionError as e:
        tqdm_auto.write(str(e))
        fail = True

# Generated at 2022-06-14 13:47:19.068750
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from random import random
    worker = MonoWorker()

    def slow(n):
        for k in range(n):
            time.sleep(random())

    def quicker(n):
        for k in range(n):
            time.sleep(random() / 4)

    def quick(n):
        for k in range(n):
            time.sleep(random() / 8)

    worker.submit(slow, 3)
    worker.submit(quicker, 3)
    worker.submit(quick, 3)
    worker.submit(quick, 3)
    worker.submit(quicker, 3)


# Generated at 2022-06-14 13:47:28.881187
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # prepare
    import time
    from math import sqrt
    import random
    import threading
    import multiprocessing as mp
    from ..utils import _range

    # function for testing
    def test_func(id, sleep=0):
        time.sleep(sleep)
        return id

    # setup
    mw = MonoWorker()
    processes = []
    threads = []
    results = []
    random.seed(1234)

    # test
    for i in range(20):
        sleep = random.uniform(0, 0.01)
        future = mw.submit(test_func, i, sleep=sleep)
        processes.append(mp.Process(target=mw.submit, args=(test_func, i,
                                                            sleep),
                                    kwargs={}))
        threads

# Generated at 2022-06-14 13:47:36.556442
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    def submit(sleep_time):
        return mw.submit(time.sleep, sleep_time)
    submit(0.1)
    submit(0.1)
    submit(0)
    submit(0.1)
    submit(0)
    time.sleep(0.2)
    submit(0.2)
    time.sleep(0.6)
    submit(0.1)
    time.sleep(0.2)
    submit(0)

# Generated at 2022-06-14 13:47:45.667498
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test method `submit` of class `MonoWorker`."""
    from time import sleep
    from random import random
    global counter

    counter = 0
    def incr_counter(sleep_time):
        global counter
        print("sleeping: %s" % sleep_time)
        sleep(sleep_time)
        counter += 1

    mw = MonoWorker()

    # regular case
    mw.submit(incr_counter, 2)
    assert counter == 0
    sleep(1)
    mw.submit(incr_counter, 1)
    assert counter == 0
    sleep(1)
    mw.submit(incr_counter, 1)
    assert counter == 0
    sleep(1)
    mw.submit(incr_counter, 1)
    assert counter == 1

# Generated at 2022-06-14 13:47:53.731894
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # import sys
    from .utils import delegator
    from .std import sleep
    mw = MonoWorker()
    arg = {}  # global arg
    arg["started"] = 0

    def func(wait=None):
        """loop which prints 'start' and then waits for wait seconds"""
        arg["started"] += 1
        tqdm_auto.write('start')
        if wait is None:
            wait = 1
        sleep(wait)
        return wait

    # 1) basic test
    delegator(mw.submit(func, wait=3))
    delegator(mw.submit(func, wait=2))
    delegator(mw.submit(func, wait=1))
    assert arg["started"] == 3
    # tqdm.write(sys.stdout.buffer.read())

    # 2)

# Generated at 2022-06-14 13:48:04.082916
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def testfunc1(text, sleep):
        time.sleep(sleep)
        tqdm_auto.write("testfunc1: " + text)

    def testfunc2(text, sleep):
        time.sleep(sleep)
        tqdm_auto.write("testfunc2: " + text)

    worker = MonoWorker()

    assert worker.submit(testfunc1, "Hello", 0.5)
    assert worker.submit(testfunc2, "World", 1.0)

    time.sleep(0.3)
    assert not worker.futures[0].done()
    time.sleep(0.6)
    assert worker.futures[0].done()

    assert worker.submit(testfunc1, "Hello2", 1.0)

    time.sleep(0.3)
   

# Generated at 2022-06-14 13:48:09.120077
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random

    def long(n):
        sleep(random())
        return n

    mw = MonoWorker()

    for i in range(4):
        running = mw.submit(long, i)
        sleep(random())

    results = list(running.result() for running in mw.futures)
    assert results == [3], results

# Generated at 2022-06-14 13:48:29.695324
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import multiprocessing.pool as mp_pool
    from concurrent.futures import ThreadPoolExecutor as _ThreadPoolExecutor
    from ..auto import tqdm

    # Python 3.6+ have a shutdown(wait=False) method in mp_pool
    if not hasattr(mp_pool, 'shutdown'):
        def shutdown(pool, wait=False):
            pool.close()
            if wait:
                pool.join()
    else:
        shutdown = mp_pool.shutdown

    # Python 3.4+ have a shutdown(wait=False) method in ThreadPoolExecutor
    if not hasattr(_ThreadPoolExecutor, 'shutdown'):
        def shutdown(pool, wait=False):
            pool.shutdown(wait)
    else:
        shutdown = lambda pool, wait: pool.shutdown

# Generated at 2022-06-14 13:48:34.399529
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def timeout(seconds, msg):
        time.sleep(seconds)
        print(msg)

    worker = MonoWorker()
    worker.submit(timeout, 1, '1')
    worker.submit(timeout, 5, '5')
    worker.submit(timeout, 7, '7')
    worker.submit(timeout, 3, '3')

# Generated at 2022-06-14 13:48:42.386896
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> import time
    >>> from concurrent.futures import ThreadPoolExecutor
    >>> executor = ThreadPoolExecutor(max_workers=1)
    >>> def func(i):
    ...     time.sleep(i)
    ...     return i
    >>> worker = MonoWorker()
    >>> futures = []
    >>> for i in range(4):
    ...     futures.append(worker.submit(func, i))
    >>> list(futures)
    [<Future at 0x7ff30c795e10 state=finished returned int>,
     <Future at 0x7ff30c795e10 state=finished returned int>,
     <Future at 0x7ff30c795e10 state=finished returned int>, None]
    """
    pass

# Generated at 2022-06-14 13:48:51.419895
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event
    from time import sleep
    from inspect import getdoc
    from nose.tools import timed
    from ..utils import _term_move_up

    # test on a method that needs to be called more than once to succeed
    def retry(n=0):
        """
        test that fails again and again, like a browser
        """
        if n < 3:
            sleep(1)
            raise Exception("reset")
        else:
            return n
    if nb:
        print("\nTesting return value:")
    n = MonoWorker().submit(retry).result()
    assert n == 3
    if nb:
        line = getdoc(retry).split("\n")[0]  # first line of docstring

    if nb:
        print("\nTiming:")
   

# Generated at 2022-06-14 13:48:59.088084
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def loop():
        for i in range(3):
            sleep(0.1)
            yield i

    m = MonoWorker()

    # Start 3 loops in order
    for _ in loop():
        m.submit(lambda: next(l))
        sleep(0.1)

    # Start one more loop, 1st loop should be discarded.
    l = loop()
    next(l)
    m.submit(lambda: next(l))
    sleep(0.1)

    # Start also 2nd loop, 2nd loop should be discarded.
    l = loop()
    next(l)
    m.submit(lambda: next(l))
    sleep(0.1)

    # Start also 3rd loop, 3rd loop should be discarded.
    l = loop()
    next(l)
   

# Generated at 2022-06-14 13:49:08.339940
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from concurrent.futures import Future
    from time import sleep

    def f():
        sleep(0.1)
        return "f"

    def g():
        sleep(0.2)
        return "g"

    def push_future(mw, f):
        mw.submit(
            lambda: f.set_result(None)
        )

    def assert_not_equal(a, b):
        assert (a != b)

    mw = MonoWorker()
    fut_f = Future()
    fut_g = Future()

# Generated at 2022-06-14 13:49:18.108118
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randint
    from threading import Thread
    from queue import Queue

    def func(q, x):
        sleep(randint(1, 3))
        q.put('func #{0} run'.format(x))

    q = Queue()

    # Submit two functions
    a, b = MonoWorker(), MonoWorker()
    a.submit(func, q, 0)
    b.submit(func, q, 1)
    sleep(0.1)  # ensure they are running

    # Submit two new functions
    a.submit(func, q, 2)
    b.submit(func, q, 3)
    sleep(0.1)  # ensure they are waiting
    q.get()  # clear func #0
    q.get()  # clear func #1 (still

# Generated at 2022-06-14 13:49:29.561518
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def long_sleep(t):
        sleep(t)
        return t

    def short_sleep(t):
        sleep(t)
        return t

    m = MonoWorker()
    m.submit(long_sleep, 2)
    assert not m.futures[0].done()
    m.submit(short_sleep, 0.1)
    assert m.futures[0].done()
    assert not m.futures[1].done()
    m.submit(short_sleep, 0.1)
    assert m.futures[0].done()
    assert not m.futures[1].done()
    try:
        m.submit(long_sleep, 0.1)
    except Exception as e:
        assert "Traceback" in str(e)
   

# Generated at 2022-06-14 13:49:38.700707
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test the `MonoWorker.submit` method."""
    import time
    import random

    def sleeper(x):
        time.sleep(random.uniform(0, 1))
        return x

    try:
        from queue import Queue
        # python2
        def get(f):
            return f.get(timeout=10)
    except ImportError:
        # python3
        from queue import SimpleQueue as Queue
        get = lambda f: f.get()

    queue = Queue()

    def enqueue(x):
        queue.put(x)

    def test(on_complete=True, on_cancel=True, on_error=False):
        queue.queue.clear()
        worker = MonoWorker()  # this is the object under test
        futs = []

# Generated at 2022-06-14 13:49:47.239804
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import tqdm
    import numpy as np

    def is_divisible(x, y):
        sleep(np.random.rand() * 0.01)
        return x % y == 0

    def test_iter(N, mw):
        for i in tqdm.tqdm(range(1, N + 1), desc="Looping over N=%d" % N):
            mw.submit(is_divisible, i, N)

    for N in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        test_iter(N, MonoWorker())



# Generated at 2022-06-14 13:50:29.946186
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def l():
        time.sleep(1)
        return 0

    worker = MonoWorker()
    worker.submit(l)
    time.sleep(4)
    worker.submit(l)
    time.sleep(4)
    worker.submit(l)
    time.sleep(4)

# Generated at 2022-06-14 13:50:40.481780
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, shutil, sys
    from concurrent.futures import TimeoutError
    from ..utils import _range

    DEFAULT_MAX_WIDTH = shutil.get_terminal_size()[0]

    def func(args):
        """[sleep_time, kwargs]"""
        sleep_time, kwargs = args
        with tqdm_auto.tqdm(desc='task', total=sleep_time, unit_scale=True,
                            smoothing=1, leave=True, dynamic_ncols=True,
                            mininterval=0, disable=False, **kwargs) as pbar:
            for i in _range(1, sleep_time + 1):
                time.sleep(1)
                pbar.update()

    mw = MonoWorker()
    tqdm_

# Generated at 2022-06-14 13:50:49.189169
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # pylint: disable=too-many-locals
    import time, signal
    from ..utils import _range
    signal.signal(signal.SIGINT, lambda _, __: False)  # ignore SIGINT

    # Basic method test
    mw = MonoWorker()
    res = []
    for i in _range(5):
        res.append(mw.submit(
            time.sleep, 1).result())  # should take at most 5 secs
    assert not res, res  # No exceptions should have been raised

    # Asynchronous test
    def wait_on(i, sleep_time=1):
        # pylint: disable=unused-argument
        time.sleep(sleep_time)
    # Simulate very delayed tasks

# Generated at 2022-06-14 13:50:59.852414
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import inspect
    import time
    import random
    import string
    import sys
    import threading
    import traceback
    try:
        from StringIO import StringIO  # Python 2
    except ImportError:
        from io import StringIO  # Python 3
    from contextlib import contextmanager

    # Run the following block under an isolated stdout, stderr
    @contextmanager
    def nostderr(stderr=None):
        """Send stderr to a buffer rather than the terminal"""
        oldstderr = sys.stderr
        sys.stderr = StringIO() if stderr is None else stderr
        try:
            yield sys.stderr
        finally:
            sys.stderr = oldstderr


# Generated at 2022-06-14 13:51:04.824757
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random

    def sleeper(n):
        sleep(n)
        return n

    worker = MonoWorker()
    assert [worker.submit(sleeper, random() / 10) for i in range(4)] == \
        [worker.submit(sleeper, random() / 10) for i in range(4)]

# Generated at 2022-06-14 13:51:14.925303
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Unit test for `MonoWorker` method `submit`."""
    import time
    import threading
    result = None
    def test_func(var, wait):
        time.sleep(wait)
        return var + wait

    def test_thread(mw, args):
        global result
        result = mw.submit(*args)

    mw = MonoWorker()
    # No result yet (as thread might be waiting for the `sleep()` call!)
    assert result is None
    # Submit 1
    test_thread(mw, (test_func, 0, 1))
    # This one is discarded
    test_thread(mw, (test_func, 1, 2))
    # This one should replace the waiting task
    test_thread(mw, (test_func, 2, 3))
    # Wait for

# Generated at 2022-06-14 13:51:26.413220
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    # TODO: unittest
    def dummy(seconds):
        time.sleep(seconds)
        return seconds

    worker = MonoWorker()

    f1 = worker.submit(dummy, 1)
    f2 = worker.submit(dummy, 1)
    print('f1 result: {}'.format(f1.result()))
    print('f2 result: {}'.format(f2.result()))
    f3 = worker.submit(dummy, 1)
    f4 = worker.submit(dummy, 1)
    print('f3 result: {}'.format(f3.result()))
    print('f4 result: {}'.format(f4.result()))
    f5 = worker.submit(dummy, 1)
    f6 = worker.submit(dummy, 1)

# Generated at 2022-06-14 13:51:37.204171
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys, time
    out = sys.stderr
    tqdm_auto.write("\nstart of test_MonoWorker_submit")
    m = MonoWorker()
    print(m.futures)

    def f(x, y):
        tqdm_auto.write("sleeping ({}, {})".format(x, y))
        time.sleep(2)
        tqdm_auto.write("end of sleep ({}, {})".format(x, y))

    m.submit(f, 1, 2)
    time.sleep(1)
    print(m.futures)
    m.submit(f, 3, 4)
    time.sleep(1)
    print(m.futures)


# Generated at 2022-06-14 13:51:44.084946
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import time

    random.seed(1)

    def bad_func():
        raise RuntimeError

    def waiting(t):
        def func():
            time.sleep(t)
            return t
        return func

    # two successive calls to MonoWorker().submit(bad_func) should not
    # raise the exception
    w = MonoWorker()
    w.submit(bad_func)
    for _ in range(100):
        w.submit(bad_func)

    # the last call to MonoWorker().submit(waiting) should be the only one
    # to return a Future, and that Future should have the same time as the
    # function submitted
    for _ in range(100):
        t = random.random()
        f = w.submit(waiting(t))

# Generated at 2022-06-14 13:51:51.048467
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import warnings

    try:
        from concurrent.futures import TimeoutError
    except ImportError:
        TimeoutError = RuntimeError

    class MyException(Exception):
        pass

    def func_raises_timeout(t):
        time.sleep(t)
        raise TimeoutError

    def func_raises_my_exception(t):
        time.sleep(t)
        raise MyException()

    def func_doesnt_raise(t):
        time.sleep(t)

    def test(func, timings):
        # NB: `timings` is a list of [submit_time, func_time]
        worker = MonoWorker()