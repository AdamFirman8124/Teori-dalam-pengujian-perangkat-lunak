

# Generated at 2022-06-14 13:42:44.790774
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event

    def identity(x):
        return x

    mw = MonoWorker()
    e1 = Event()
    f1 = mw.submit(identity, e1)
    e2 = Event()
    f2 = mw.submit(identity, e2)
    assert f1.done()
    assert f2 is not None
    assert not f2.done()
    e2.set()
    assert f2.result() is e2



# Generated at 2022-06-14 13:42:53.094442
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from math import sqrt
    from sys import stderr

    def proc1(t):
        from random import randint
        sleep(t)
        return sqrt(randint(1, 8))

    def proc2(t):
        sleep(t)
        raise ValueError

    m = MonoWorker()
    f0 = m.submit(proc1, 1)
    f0.result()
    assert f0.cancel()
    assert f0.cancelled()
    f1 = m.submit(proc1, 1)
    f1.result()
    f2 = m.submit(proc2, 1)
    try:
        f2.result()
    except Exception as e:
        print(e, file=stderr)
    # try:
    #     f2.result

# Generated at 2022-06-14 13:43:02.017843
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from itertools import repeat
    from random import randint

    def _test_MonoWorker_submit():
        def run(name, func, *args, **kwargs):
            sleep(0.2 * randint(1, 5))
            tqdm_auto.write("{0}({1}, {2}, {3})".format(name, func, args, kwargs))
            if func == 'cancel':
                raise RuntimeError("{0}({1}, {2}, {3}) should never be called".format(name, func, args, kwargs))
            return func(*args, **kwargs)
        funcs = ['add', 'mul', 'div', 'cancel']
        xy = [(1, 2), (3, 4), (5, 6)]

# Generated at 2022-06-14 13:43:12.970611
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    from datetime import datetime

    def sleep_message(interval, mess='Hello world'):
        time.sleep(interval)
        print('{0:3.3f}: {1} @ {2}'.format(interval, mess,
                                           datetime.now().isoformat()))
        return interval, mess

    mw = MonoWorker()
    for i in range(20):
        mw.submit(sleep_message, i*0.1, mess='OK')

    # Spin up a thread that will kill the main process
    # if we don't do our job right.
    threading.Thread(target=lambda: time.sleep(5)).start()

    for fut in mw.futures:
        fut.result()

# Generated at 2022-06-14 13:43:23.066287
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    #pylint: disable=no-member
    import time
    import random

    def wait_then_return(result, delay):
        """delay: 0 means no wait"""
        if delay:
            time.sleep(random.random() * delay)
        return result

    mw = MonoWorker()
    fw = mw.submit(wait_then_return, "waiting", 2)
    fr = mw.submit(wait_then_return, "running", 2)
    assert fr.result() == "running"
    assert fw.result() == "waiting"

    # Re-run
    mw = MonoWorker()
    fw = mw.submit(wait_then_return, "waiting", 2)
    fr = mw.submit(wait_then_return, "running", 2)

# Generated at 2022-06-14 13:43:31.020011
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from collections import deque
    from itertools import count

    results = deque([], 2)
    inputs = deque(['first', 'second', 'third', 'fourth'], 4)

    def func(arg):
        time.sleep(0.1)
        return arg

    mw = MonoWorker()
    for _ in count():
        if len(results) == results.maxlen:
            for result in results:
                print(result.result())
                results.popleft().result()
        if inputs:
            results.append(mw.submit(func, inputs.popleft()))
        if not inputs and not results:
            break
        time.sleep(0.1)

# Generated at 2022-06-14 13:43:41.799406
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    We have 2 loops (running and waiting) and 2 `MonoWorker` instances:
    > * A: `MonoWorker` with both loops running (validates `running` behaviour)
    > * B: `MonoWorker` with only one loop running (validates `waiting` behaviour)
    """
    import time
    import random
    # pylint: disable=W0621

    def wait(seconds, *args, **kwargs):
        """Mock task that sleeps for fixed amount of time"""
        return time.sleep(seconds)

    def wait_random(*args, **kwargs):
        """Mock task that sleeps for random amount of time"""
        return random.random() / 10


# Generated at 2022-06-14 13:43:50.396113
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import traceback
    from ..utils import _term_move_up
    mw = MonoWorker()
    c = lambda i: tqdm_auto.write('Start %d' % i) or sleep(1) or tqdm_auto.write('End %d\n' % i)
    futures = [mw.submit(c, i) for i in range(3)]
    i = 0
    try:
        while futures:
            futures.pop().result()
            i += 1
            _term_move_up()
            _term_move_up()
    finally:
        tqdm_auto.write(traceback.format_exc())
    assert i == 3

# Generated at 2022-06-14 13:43:56.505456
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    import time
    worker = MonoWorker()  # pylint: disable=undefined-variable

    def _(x):
        print('\t{} started'.format(x))
        time.sleep(0.2)
        print('\t{} done'.format(x))

    for x in range(10):
        print('submit {}'.format(x))
        worker.submit(_, x)

# Generated at 2022-06-14 13:44:06.222645
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import current_thread
    import sys

    def test_func(*args, **kwargs):
        sleep(1)
        name = current_thread().getName()
        tqdm_auto.write('{0}: {1}'.format(name, kwargs['timestamp']))

    mw = MonoWorker()
    f1 = mw.submit(test_func, timestamp=sys.version_info[:])
    f2 = mw.submit(test_func, timestamp=sys.version_info[:])
    f3 = mw.submit(test_func, timestamp=sys.version_info[:])
    f4 = mw.submit(test_func, timestamp=sys.version_info[:])

# Generated at 2022-06-14 13:44:16.939045
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event
    from time import sleep
    import weakref
    from ..utils import _range

    def func(i, evt):
        sleep(0.01)
        evt.set()
        return i

    results = []
    evts = [Event() for i in _range(10)]
    mw0 = MonoWorker()
    mw1 = weakref.ref(mw0)
    assert mw1() == mw0
    mw0.submit(func, -1, evts[0])
    del mw0
    assert mw1() is None
    mw0 = MonoWorker()
    mw1 = weakref.ref(mw0)
    for i in _range(10):
        mw0.submit(func, i, evts[i])

# Generated at 2022-06-14 13:44:27.017578
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    def dummy_func(n, wait):
        time.sleep(wait)
        return n

    def func_producer():
        yield lambda: dummy_func(0, 0)

    def func_consumer():
        yield lambda: dummy_func(1, 0)
        yield lambda: dummy_func(2, 0)
        yield lambda: dummy_func(None, 0)

    mw = MonoWorker()
    assert len(mw.futures) == 0

    producer = func_producer()
    mw.submit(*next(producer)())
    assert len(mw.futures) == 1
    time.sleep(1)  # wait for task to complete
    assert list(mw.futures)[0].result() == 0

    producer = func_producer()

# Generated at 2022-06-14 13:44:36.673136
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from multiprocessing import Pool

    def run(d):
        print('start')
        time.sleep(d)
        print('end')

    mw = MonoWorker()
    mw.submit(run, 2)
    mw.submit(run, 1)
    mw.submit(run, 3)
    mw.submit(run, 4)

    # Multiprocessing
    p = Pool(processes=1)
    p.apply_async(run, [2])
    p.apply_async(run, [1])
    p.apply_async(run, [3])
    p.apply_async(run, [4])

# Generated at 2022-06-14 13:44:47.152311
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import multiprocessing

    def testfunc(num):
        time.sleep(random.randrange(3))
        return num * num

    def testfunc_error():
        time.sleep(random.randrange(3))
        raise Exception("test")

    count = 10

    for is_mp in (True, False):
        pool = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())
        mono_pool = MonoWorker()
        tqdm_auto.write("{}".format("Testing using ThreadPoolExecutor"
                                    if is_mp else "Testing using MonoWorker"))
        tests = [pool.submit if is_mp else mono_pool.submit]
        results = []

# Generated at 2022-06-14 13:44:57.737925
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    import time
    import traceback
    from collections import Counter
    from queue import Queue
    from threading import Thread

    def test_print(txt):
        tqdm_auto.write(str(txt))

    def worker(q):
        while True:
            item = q.get()
            if item is None:  # stop
                break
            try:
                time.sleep(0.2)  # wait for the next job to arrive
                test_print('result: {}'.format(item))
            except Exception:
                test_print(traceback.format_exc())
                sys.exit(1)
            q.task_done()

    def test_func(item):
        time.sleep(0.1)  # wait for the next job to arrive
        return item

    q = Queue()


# Generated at 2022-06-14 13:45:08.078657
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from os import getpid
    from multiprocessing import cpu_count
    from concurrent.futures import wait
    from datetime import datetime

    def print_pid():
        print(datetime.now().strftime('%H:%M:%S.%f'),
              'pid:', getpid(), 'on CPU:', CPU_NUM)
        sleep(0.01)

    n_cpus = cpu_count()
    MonoWorker.submit(print_pid)
    MonoWorker.submit(print_pid)
    MonoWorker.submit(print_pid)
    MonoWorker.submit(print_pid)
    CPU_NUM = 0
    a = MonoWorker.submit(print_pid)
    CPU_NUM = 1
    b = MonoWorker.submit(print_pid)

# Generated at 2022-06-14 13:45:15.978524
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Unit test for method submit of class MonoWorker."""
    mw = MonoWorker()

    def task(i):
        if i == 1:
            import time
            time.sleep(1)

    t1 = mw.submit(task, 1)
    t2 = mw.submit(task, 2)
    assert t1.running()
    t1.result()
    assert t2.done()
    t2 = mw.submit(task, 3)
    assert t2.done()
    mw.shutdown()

# Generated at 2022-06-14 13:45:20.585620
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Thread

    def create_writer():
        def write(i):
            sleep(i % 2)  # stagger the threads
            tqdm_auto.write(str(i))
        return write

    mw = MonoWorker()
    threads = [Thread(target=create_writer(), args=(i,))
               for i in range(1, 11)]
    for t in threads:
        t.start()

    for i in range(len(threads)):
        mw.submit(create_writer(), i)
        sleep(0.1)

    for t in threads:
        t.join()

# Generated at 2022-06-14 13:45:30.855284
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep as time_sleep
    import sys
    from tqdm import tqdm
    from threading import Lock
    lock = Lock()

    def sleep(secs):
        time_sleep(secs)
        return secs

    if sys.version_info < (3, 2):
        raise Exception("Requires Python >= 3.2")

    mw = MonoWorker()  # workers number == 1
    # sum is != 3 because the first sleep() will be replaced
    sum_ = sum([mw.submit(sleep, i).result()
                for i in tqdm(range(3),
                              file=sys.stderr,
                              leave=False)])
    assert sum_ == 2, sum_

    mw = MonoWorker()  # workers number == 1

# Generated at 2022-06-14 13:45:40.988879
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    # MonoWorker is run in a separate process
    # so that multiprocessing concurrent.futures.ProcessPoolExecutor
    # is not tested in the same process
    from multiprocessing import Process
    class_instance = MonoWorker()
    p = Process(target=class_instance.submit, args=(time.sleep, 0.1))
    p.start()
    time.sleep(0.01)
    p2 = Process(target=class_instance.submit, args=(time.sleep, 0.1))
    p2.start()
    time.sleep(0.01)
    p3 = Process(target=class_instance.submit, args=(time.sleep, 0.1))
    p3.start()
    time.sleep(0.01)
    p.join()
    p2.join

# Generated at 2022-06-14 13:45:53.681467
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import collections
    import unittest
    expected_screen_output = ['1', '2', '3', '4', '5', '6']
    screen_output = collections.deque([], len(expected_screen_output))
    import builtins
    builtins.print = lambda x: screen_output.append(x)
    mw = MonoWorker()
    for i in range(6):
        mw.submit(time.sleep, 0.1)
    time.sleep(0.2)
    assert list(screen_output) == expected_screen_output
    unittest.main()

# Generated at 2022-06-14 13:45:58.789792
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import graphics

    def plot(i):
        time.sleep(1)
        graphics.plot(i)

    with tqdm_auto.tqdm(smoothing=0, leave=False) as t:
        t.total = 30
        mw = MonoWorker()
        for i in range(3):
            mw.submit(plot, i)
            t.update()

# Generated at 2022-06-14 13:46:08.821906
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """test_MonoWorker_submit"""
    import time
    from ._utils import BetterMock

    # pylint: disable=too-many-locals
    def _waiting_func(idx, sleep=0):
        """_waiting_func"""
        time.sleep(sleep)
        return idx

    ret = [0] * 3
    output = []

    worker = MonoWorker()
    ret[0] = worker.submit(_waiting_func, 0, sleep=0)
    ret[1] = worker.submit(_waiting_func, 1, sleep=0)
    ret[2] = worker.submit(_waiting_func, 2, sleep=0.5)  # will be cancelled
    worker.submit(_waiting_func, 3, sleep=0.5)


# Generated at 2022-06-14 13:46:18.574573
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from concurrent.futures import Future

    style, options = tqdm_auto.get_lock_args()
    tqdm_auto.write("Starting tests")
    # Create an instance of MonoWorker
    mw = MonoWorker()

    # A given function, args, kwargs
    def func(a, b=None):
        return a + (b or 0)

    # Create a sample list of submitted tasks
    T = [
        (func, 1, 2),
        (func, 1, 2),
        (func, 1, 2),
        (func, 1),
        (func, 1, 2),
        (func, 1),
        (func, 1, 2),
    ]

    # Create a list of Futures from T

# Generated at 2022-06-14 13:46:24.870296
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def f_slow(n):
        time.sleep(5)
        return n

    def f_fast(n):
        return n

    worker = MonoWorker()

    first_fut = worker.submit(f_slow, 1)
    time.sleep(2)
    second_fut = worker.submit(f_fast, 2)
    assert second_fut.done()
    assert second_fut.result() == 2
    assert not first_fut.done()
    assert first_fut.result() == 1


# Generated at 2022-06-14 13:46:36.241435
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import fcntl
    import time
    from .utils import io_wrap
    sleeping = False
    sleep_ticks = 1
    def init():
        global sleeping
        sleeping = False

    def test_fn():
        global sleeping
        global sleep_ticks
        sleeping = True
        time.sleep(1)
        sleeping = False

    def write(s):
        with io_wrap() as fd:
            while True:
                try:
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                except IOError:
                    time.sleep(sleep_ticks)
                else:
                    break
            tqdm_auto.write(s, file=fd)

# Generated at 2022-06-14 13:46:45.732656
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import threading
    import time
    import traceback
    from datetime import datetime

    m = MonoWorker()
    end = threading.Event()
    def task():
        try:
            while not end.is_set():
                time.sleep(10)
        except:  # noqa
            tqdm_auto.write(str(traceback.format_exc()))

    def test():
        with tqdm_auto.tqdm(total=33, leave=False) as pbar:
            for _ in range(3):
                m.submit(task)
                for _ in range(10):
                    time.sleep(1)
                    pbar.update()
                time.sleep(5)  # to catch in-flight tasks
        time.sleep(1)
        end.set()
        time.sleep

# Generated at 2022-06-14 13:46:50.090429
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from itertools import count
    from .test_test_examples import notests

    def func(i, s):
        sleep(s)
        return i

    pool = MonoWorker()
    for i in count():
        notests(pool.submit(func, i, 0.5))
        # if i % 2 == 0:
        #     pool.submit(func, i, 1)
        # else:
        #     pool.submit(func, i, 0.5)

# Generated at 2022-06-14 13:46:58.699943
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import os
    from threading import Thread
    from time import sleep

    mw = MonoWorker()

    def wait_print(t, *s):
        sleep(t)
        print("\t%s: %s" % (os.getpid(),
                            " ".join(x for x in map(str, s))))

    for i in range(10):
        mw.submit(wait_print, 0.1, i)


# if __name__ == '__main__':
#     test_MonoWorker_submit()

# Generated at 2022-06-14 13:47:04.910412
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def waiting_task():
        sleep(10)
        return "done"

    def non_waiting_task():
        return "done now"

    worker = MonoWorker()
    worker.submit(waiting_task)
    print("Submitted waiting task.")
    worker.submit(non_waiting_task)
    print("Submitted non-waiting task.")
    sleep(11)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Generated at 2022-06-14 13:47:23.789120
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .async_ import as_completed
    from .format_size import sizeof_fmt as size

    def dummy(deterministic_sleep_time=1):
        sleep(deterministic_sleep_time)
        return size(deterministic_sleep_time, 'B')

    worker = MonoWorker()

    original_max_workers = ThreadPoolExecutor.__init__.__defaults__[0]

# Generated at 2022-06-14 13:47:33.340895
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    tqdm_auto.write('')
    mw = MonoWorker()
    def f():
        time.sleep(0.05)
        return 1

    assert mw.submit(f).result() == 1  # 1
    assert mw.submit(f).result() == 1  # 2
    assert mw.submit(f).result() == 1  # 3
    assert mw.submit(f).result() == 1  # 4
    assert mw.futures[-1].result() == 1  # 1

    start = time.time()
    assert mw.submit(f).result() == 1  # 1
    assert mw.submit(f).result() == 1  # 2
    assert mw.submit(f).result() == 1  # 3

# Generated at 2022-06-14 13:47:43.449952
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from contextlib import closing
    from multiprocessing import Queue, Process
    from concurrent.futures import CancelledError

    def test_func(num, queue):
        time.sleep(num)
        queue.put(num)

    def send_input(queue):
        print("Enter input:")
        while True:
            try:
                cmd = raw_input(">> ").strip()
                if cmd not in ['1', '2', '3']:
                    raise ValueError("Invalid input: '{}'".format(cmd))
                queue.put(cmd)
            except EOFError:
                queue.put("exit")
                break

    # the number of the task that is executed
    # e.g. enter 1, then 2, the output should be: 1 2.
    # e.g.

# Generated at 2022-06-14 13:47:52.937730
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from random import random
    from time import sleep, time
    from multiprocessing import cpu_count

    dt = 0.1
    num_tests = cpu_count() * 3
    error_threshold = 1

    with tqdm_auto.trange(num_tests) as t:
        mw = MonoWorker()
        for _ in t:
            start = time()
            mw.submit(sleep, dt)
            dt = min(dt*1.1, dt + 0.1)  # slowly grow dt in order to be random
            t.set_postfix(dt=dt)
            err = abs(dt - (time() - start))
            assert err < error_threshold



# Generated at 2022-06-14 13:48:03.671954
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    # Sequential
    mw = MonoWorker()
    for i in range(0, 3):
        assert len(mw.futures) == i
        mw.submit(lambda i: i, i)
        assert len(mw.futures) == i + 1
    assert mw.futures[0].result() == 2

    # Concurrent
    from threading import Thread
    from time import sleep
    mw = MonoWorker()
    for i in range(0, 3):
        sleep(i / 100.0)
        assert len(mw.futures) == 0
        Thread(target=mw.submit, args=(lambda i: i, i)).start()
    sleep(0.5)
    assert len(mw.futures) == 1
    assert mw.futures

# Generated at 2022-06-14 13:48:09.052541
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    def func(*args):
        print("func(%s)" % str(args))
        time.sleep(random.randint(2, 5))

    mw = MonoWorker()
    mw.submit(func, 1)
    mw.submit(func, 2)
    mw.submit(func, 3)
    print(list(mw.futures))

# Generated at 2022-06-14 13:48:18.024586
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from copy import copy
    from sys import stderr

    from ..utils import _supports_unicode
    from ..utils import WriteMixin
    from ..utils import _environ_cols_wrapper

    def func(text):
        tqdm_auto.write(text)

    class Test(WriteMixin):
        def __init__(self):
            self.prev = 0
            self.line_len = 0

        def write(self, s):
            if self.prev == '\n':
                line_len = 0
            else:
                line_len = len(s)
            self.line_len += line_len
            self.prev = s[-1]

        def flush(self):
            self.prev = 0

    test = Test()
    worker = MonoWorker()

# Generated at 2022-06-14 13:48:26.909597
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    fut = mw.submit(time.sleep, 1)
    # fut.done()
    time.sleep(0.5)
    fut2 = mw.submit(print, 'mwalt')
    # fut2.done()
    assert len(mw.futures) == 1
    assert mw.futures[0] is fut2
    time.sleep(2.0)
    # fut.done()
    assert fut.done()
    assert fut2.done()


if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:48:34.637905
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    mw = MonoWorker()
    assert len(mw.futures) == 0
    f1 = mw.submit(time.sleep, 5)
    assert len(mw.futures) == 1
    f2 = mw.submit(time.sleep, 5)
    assert len(mw.futures) == 1
    f1.result()
    assert len(mw.futures) == 1
    f3 = mw.submit(time.sleep, 5)
    assert len(mw.futures) == 1
    f2.cancel()
    f3.cancel()
    try:
        f3.result()
    except Exception:
        assert len(mw.futures) == 0
    else:
        assert False, "Did not raise exception"

# Generated at 2022-06-14 13:48:43.190663
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Lock, RLock
    from .test_tqdm import with_setup

    shared_var = []
    lock = Lock()
    rlock = RLock()

    def test_func(var, lock=None):
        """Thread-safe test function."""
        sleep(0.1)
        with lock:
            shared_var.append(var)

    test_list = list(range(100))
    tp = MonoWorker()
    with tp.pool:  # close pool automatically on success, without exceptions
        with tqdm_auto(total=len(test_list)) as t:  # trange is a special case of tqdm
            for i in test_list:
                old_length = len(shared_var)

# Generated at 2022-06-14 13:49:06.160354
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from traceback import format_exc
    from sys import stderr

    def f(n, s):
        sleep(s)
        if (n % 100) == 0:
            print("sleep {0}s".format(s))
        return n

    mw = MonoWorker()

    def p(f, n, s):
        """Print `f(n, s)` ignoring result."""
        try:
            mw.submit(f, n, s)
        except Exception as e:
            tqdm_auto.write(str(e), file=stderr)
            tqdm_auto.write(format_exc(), file=stderr)

    # We're going to have 100 tasks.
    # - The first 50 tasks will take 2s, start and end at 0, 1, 2

# Generated at 2022-06-14 13:49:16.978376
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import threading
    from concurrent.futures import Future

    mw = MonoWorker()

    def _submit():  # Add a random time in the middle to simulate variability
        future = mw.submit(time.sleep, random.random())
        assert isinstance(future, Future)
        r = future.result()

    _submit()  # Currently running
    _submit()  # Will replace the currently waiting
    _submit()  # Will be discarded

    assert len(mw.futures) == 2
    assert mw.futures[0].done()
    assert not mw.futures[1].done()

    time.sleep(0.1)  # Enough time for the above tasks to have started

    _submit()  # Will cancel the currently waiting


# Generated at 2022-06-14 13:49:24.037440
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def foo():
        sleep(1)

    MW = MonoWorker()

    # Submit a task to the pool that will be running
    running = MW.submit(foo)

    # Submit a task to the pool that will be waiting
    waiting = MW.submit(foo)

    # Submit a task to the pool that will be discarded
    discarded = MW.submit(foo)

    assert discarded is None
    assert running.done()
    assert not waiting.done()

    # Submit a task that will replace the waiting task
    new_waiting = MW.submit(foo)

    assert not new_waiting.done()
    assert discarded.done()
    assert running.done()
    assert waiting.done()

# Generated at 2022-06-14 13:49:34.097957
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test correctness and corner cases of MonoWorker.submit"""
    from ..utils import format_sizeof
    from os import getpid
    from threading import Event
    from time import sleep

    def _return_true():
        return True

    def _return_false():
        return False

    def _sleep_and_return_true(sleep_time):
        sleep(sleep_time)
        return True

    mw = MonoWorker()
    assert not mw.futures
    # Submit one job
    fut = mw.submit(_return_true)
    assert len(mw.futures) == 1
    assert fut.done()
    assert fut.result()
    print('  PID:', getpid(), '\tmem=', format_sizeof(get_memory_usage()), end='\r')
    #

# Generated at 2022-06-14 13:49:42.353655
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from decimal import Decimal

    def wait(n):
        time.sleep(Decimal(n))
        return n

    worker = MonoWorker()

    # Get a first future to wait for it
    assert worker.submit(wait, 1).result() == 1

    # Submit a second future and assert the worker thread does not wait for it
    assert worker.submit(wait, 0.5).result() == 0.5

    # Submit a third future,
    # assert the second future is cancelled
    # and assert the worker still waits for the first future
    assert worker.submit(wait, 2).result() == 2



# Generated at 2022-06-14 13:49:50.739928
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from random import random
    from time import sleep
    from multiprocessing import Lock

    lock = Lock()
    log = []
    def func(idx):
        with lock:
            log.append(idx)
        sleep(random())
        with lock:
            log.append(idx)
        return idx

    mw = MonoWorker()
    futures = []
    for i in range(10):
        sleep(random() / 10)
        futures.append(mw.submit(func, i))

    for f in futures:
        f.result()

    assert [f.result() for f in futures] == log

# Generated at 2022-06-14 13:49:55.250468
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from ..utils import _range

    def func(i):
        sleep(0.1)
        return i

    mono = MonoWorker()
    for i in _range(10):
        mono.submit(func, i)
    assert len(mono.futures) == 2
    assert mono.futures[0].done()
    assert not mono.futures[1].done()
    assert mono.futures[0].result() == 9

# Generated at 2022-06-14 13:50:02.992712
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random

    # stdlib
    from time import sleep
    from socket import socket, AF_INET

    def worker_1(socket, host, port):
        sleep(0.5)
        socket.connect((host, port))

    def worker_2(socket, host, port):
        sleep(0.5)
        socket.send(b'foo')

    def worker_3(socket, host, port):
        sleep(0.5)
        socket.close()

    host = '127.0.0.1'
    port = random.randint(2000, 9000)

    tqdm_auto.write(
        'Testing MonoWorker\n'
        'Listening on {}:{}'.format(host, port))

    s = socket(AF_INET)
    s.bind((host, port))
   

# Generated at 2022-06-14 13:50:11.942054
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import string
    import unittest

    def hello(name):
        time.sleep(random.random())
        return 'Hello {}!'.format(name)

    class TestMonoWorker(unittest.TestCase):
        def setUp(self):
            self.sut = MonoWorker()

        def test_some_scenario(self):
            def make_random_string(n):
                return ''.join(random.choice(string.ascii_uppercase +
                                             string.digits)
                               for _ in range(n))

            with tqdm_auto.tqdm() as t:
                while True:
                    if t.n >= t.total:
                        break
                    name = make_random_string(5)
                    future = self.sut

# Generated at 2022-06-14 13:50:20.303783
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from queue import Queue

    mw = MonoWorker()
    q = Queue()

    def _append(a, s):
        time.sleep(s)
        q.put(a)
    for i in range(10):
        mw.submit(_append, i, 0.1)
    mw.submit(_append, 'stop', 0.3)
    mw.submit(_append, 'stop-1', 0.3)
    mw.submit(_append, 'stop-2', 0.3)
    # mw.submit(_append, 'stop-3', 0.3)

    while True:
        a = q.get()
        if a == 'stop':
            break;
        print(a)

# Generated at 2022-06-14 13:50:53.292975
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from ..utils import _string_type  # type: ignore
    from time import sleep
    from copy import copy

    def _write(fd, chars):
        fd.write(chars.encode())
        fd.flush()

    def _write_and_sleep(fd, chars, t):
        _write(fd, chars)
        sleep(t)

    def _sleep_and_write(fd, chars, t):
        sleep(t)
        _write(fd, chars)

    chars = ["abc", "def", "ghi", "jkl", "mno"]
    ctimes = [1.0, 1.0, 1.0, 1.0, 1.0]
    wtimes = [0.0, 0.0, 0.0, 0.0, 0.0]


# Generated at 2022-06-14 13:51:03.217676
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Unit test for method submit of class MonoWorker"""
    import os
    import time
    import subprocess
    cmd_write = "echo "
    cmd_fail = "exit 1"
    cmd_howlong = "sleep "
    def cmd_wget(url):
        return "wget -q " + url

    workers = MonoWorker()
    workers.submit(subprocess.check_output, cmd_write + "hello", shell=True)
    time.sleep(0.1)
    workers.submit(subprocess.check_output, cmd_write + "world", shell=True)
    time.sleep(0.1)
    workers.submit(subprocess.check_output, cmd_howlong + "0.5", shell=True)

# Generated at 2022-06-14 13:51:12.846260
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from functools import partial

    def sleep_return(value, s):
        sleep(s)
        return value

    # Outcome:
    # - First call: return '1' after a 2.0-second delay
    # - Second call: return '2' after a 1.0-second delay (replaces '1')
    # - Third call: return '3' after a 1.0-second delay (replaces '2')
    # - Fourth call: immediately return '4' (replaces '3')
    # - Fifth call: immediately return '5' (replaces '4')
    # - Sixth call: immediately return '6' (replaces '5')
    # NOTE: the last four calls are submitted immediately after each other.
    # We expect the final three of them to be discarded.

# Generated at 2022-06-14 13:51:17.937648
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random
    x = MonoWorker()
    assert not x.futures
    for i in tqdm_auto.tqdm(range(4), desc='Testing'):
        assert len(x.futures) <= 1  # may never be more than 1
        sleep(random())
        x.submit(sleep, random())
        sleep(random())
    while x.futures:
        sleep(random())
    assert not x.futures

# Generated at 2022-06-14 13:51:28.778859
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def one():
        sleep(1)
        return 1

    def two():
        print("two")
        sleep(2)
        return 2

    def three():
        sleep(3)
        return 3

    def test(func, *args, **kwargs):
        worker = MonoWorker()
        futures = []
        futures.append(worker.submit(func))
        futures.append(worker.submit(func))
        futures.append(worker.submit(func))
        futures.append(worker.submit(func))
        for f in futures:
            try:
                f.result()
            except Exception as e:
                print(type(e), e)

    test(one)
    test(two)
    test(three)

# Generated at 2022-06-14 13:51:35.472312
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def wait(secs, i):
        sleep(secs)
        return i

    with MonoWorker() as mono:
        for i in range(3):
            mono.submit(wait, 1, i)
    mono.submit(wait, 1, 3)
    sleep(2)
    mono.submit(wait, 1, 4)
    sleep(3)
    mono.submit(wait, 1, 5)
    sleep(4)

# Generated at 2022-06-14 13:51:43.168078
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import functools
    import threading

    def time_sleep(time_):
        time.sleep(time_)
        return time_

    def time_sleep_w_print(time_):
        time.sleep(time_)
        print('Done sleeping for {}s'.format(time_))
        return time_

    ca = MonoWorker()
    ex = ThreadPoolExecutor(max_workers=2)

# Generated at 2022-06-14 13:51:50.611881
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Lock
    import time
    import sys
    import os

    def write_n_times(n, msg):
        """
        Writes `msg` `n` times, sleeping 1 second between writes
        """

        with Lock():
            sys.stdout.write('\nlock acquired\n')
            print(os.getpid())
        for i in range(n):
            sys.stdout.write(str(i) + msg + '\n')
            time.sleep(1)

    mono_worker = MonoWorker()
    mono_worker.submit(write_n_times, 4, 'test')
    time.sleep(2)
    mono_worker.submit(write_n_times, 4, 'foo')
    time.sleep(0.5)

# Generated at 2022-06-14 13:51:54.624157
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random
    from multiprocessing import cpu_count
    NUM_THREADS = cpu_count() - 1

    # Make a progress bar
    pbar = tqdm_auto.tqdm(total=NUM_THREADS)

    # Make a worker pool
    worker = MonoWorker()

    def func(sleep_time):
        sleep(sleep_time)
        # A common use case is to update the progress bar on success
        pbar.update()

    # Submit many threads
    for _ in range(NUM_THREADS):
        worker.submit(func, random())

    # Cancel waiting threads
    for fut in list(worker.futures):
        fut.cancel()

# Generated at 2022-06-14 13:52:04.770020
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from threading import Event
    from time import time

    from .common import is_notebook, in_ipython

    class Test(object):
        def __init__(self):
            self.prev_time = time()
            self.cur_time = self.prev_time

            self.mono = MonoWorker()
            self.evt = Event()
            self.evt.clear()

            self.stopped = False

        def test_submit(self):
            if self.stopped:
                self.evt.set()
                return

            self.prev_time = self.cur_time
            self.cur_time = time()

            tqdm_auto.write('submit time: {}'.format(self.prev_time))
            self.mono.submit(self.test_submit)

    test = Test()