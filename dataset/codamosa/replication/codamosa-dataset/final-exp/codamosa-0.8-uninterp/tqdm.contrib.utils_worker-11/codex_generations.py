

# Generated at 2022-06-14 13:42:48.264253
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    def f(n):
        sleep(n)
        return n

    mo = MonoWorker()
    assert mo.submit(f, 0.1) is None
    # TODO: fix this
    # assert mo.submit(f, 0.2) is None
    mo.pool.shutdown()



# Generated at 2022-06-14 13:42:55.330301
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def func(x, time_sleep_sec=0.1):
        time.sleep(time_sleep_sec)
        return x

    mono_worker = MonoWorker()
    for i in range(4):
        mono_worker.submit(func, i)
        time.sleep(0.01)
    time.sleep(0.1)

if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:43:03.395042
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test that MonoWorker.submit() works."""
    import time
    import traceback
    from os import system
    from time import time as now
    from concurrent.futures import CancelledError

    def run_mw(mw, func_list, fargs, fkwargs):
        for f in func_list:
            mw.submit(f, *fargs, **fkwargs)

    def wait_mw(mw, timeout=5):
        end = now() + timeout
        while True:
            try:
                if mw.pool.shutdown(wait=True):
                    return
            except Exception:
                traceback.print_exc()
            if now() > end:
                return

    def target_func(time_to_sleep):
        time.sleep(time_to_sleep)

   

# Generated at 2022-06-14 13:43:13.908738
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # pylint: disable=protected-access
    import time
    import multiprocessing as mp
    _avail_time = mp.cpu_count() / 2.0
    mw = MonoWorker()
    assert len(mw.pool._threads) == 1
    assert len(mw.futures) == 0
    assert mw.pool._work_queue.qsize() == 0
    # submit with replace
    mw.submit(time.sleep, _avail_time / 2.0)
    assert len(mw.futures) == 1
    assert mw.pool._work_queue.qsize() == 1
    mw.submit(time.sleep, _avail_time * 2.0)
    assert len(mw.futures) == 1
    assert mw.pool._work

# Generated at 2022-06-14 13:43:23.751097
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from itertools import count
    import sys

    mw = MonoWorker()
    result = None
    for i in count():
        def callback(ii, result=None):
            for j in range(3):
                sys.stdout.write('\a')
                sys.stdout.flush()
                sleep(0.5)
            sleep(0.5)
            return ii + (result or 0)
        if i % 2:
            result = mw.submit(callback, i, result=result)
        if i == 3:
            # kill pending task
            running = mw.futures.popleft()  # TODO: this is dangerous
            running.cancel()
        elif i > 3:
            # don't bother with waiting tasks
            mw.futures.clear

# Generated at 2022-06-14 13:43:29.275337
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def printmsg(msg):
        time.sleep(0.1)
        print(msg)

    mono = MonoWorker()
    mono.submit(printmsg, 'A')
    mono.submit(printmsg, 'B')
    mono.submit(printmsg, 'C')
    time.sleep(0.2)
    mono.submit(printmsg, 'D')
    time.sleep(0.2)

# Generated at 2022-06-14 13:43:40.607555
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from concurrent.futures import Future
    from time import time
    from traceback import format_exc
    from contextlib import closing
    import sys

    if sys.version_info[0] > 2:
        from queue import Queue  # Python 3
    else:
        from Queue import Queue  # Python 2

    def log(msg, wait_for=None):
        timestamp = time()
        if wait_for:
            try:
                wait_for.result()
            except KeyboardInterrupt:
                raise
            except Exception as e:
                tqdm_auto.write(format_exc())
        tqdm_auto.write(str(timestamp) + ' ' + msg)

    def appender(filename, times):
        """Append multiple times to file"""

# Generated at 2022-06-14 13:43:47.998630
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from itertools import count

    def func(i):
        time.sleep(0.1)
        return i, time.time()

    mono = MonoWorker()
    for i in count(1):
        waiting = mono.submit(func, i)
        if waiting is not None:
            i1, t1 = waiting.result()
            i2, t2 = mono.submit(func, i + 1).result()
            if i1 + 1 == i2 and t1 < t2:
                break
    else:
        raise Exception("Too many iterations")

# Generated at 2022-06-14 13:43:59.111915
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    stop = False

    def proc_1(time_, stop):
        i = 0
        while not stop:
            i += 1
            time.sleep(time_)
        return i

    def proc_2(time_, stop):
        i = 0
        while not stop:
            i += 1
            time.sleep(time_)
        return i

    worker = MonoWorker()

    result_1 = worker.submit(proc_1, 0.1, stop)
    time.sleep(0.2)
    result_2 = worker.submit(proc_2, 0.1, stop)
    time.sleep(0.2)
    result_3 = worker.submit(proc_1, 0.1, stop)
    time.sleep(0.2)
    result_4 = worke

# Generated at 2022-06-14 13:44:04.677306
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    3 submissions, 2 tasks
    """
    def test_func(x):
        return x ** 2

    mw = MonoWorker()
    res = [mw.submit(test_func, i) for i in range(3)]
    for i in range(2):
        assert res[i] == sorted(res, key=lambda f: f.result())[i]
    for i in range(2):
        assert res[i].result() == i ** 2

# Generated at 2022-06-14 13:44:15.361360
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import concurrent.futures
    import time

    def get_state(pool):
        if pool._threads:
            return 'running'
        elif pool._work_queue.empty() and pool._results_queue.empty():
            return 'done'
        else:
            return 'waiting'

    pool = MonoWorker()
    assert get_state(pool.pool) == 'done'

    f1 = pool.submit(time.sleep, .5)
    assert get_state(pool.pool) == 'running'
    assert f1.done() is False
    assert f1.result() is None
    assert get_state(pool.pool) == 'done'

    f2 = pool.submit(time.sleep, .5)
    f3 = pool.submit(time.sleep, .5)
    assert get_state

# Generated at 2022-06-14 13:44:23.526474
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:44:30.826554
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    >>> import time
    >>> import random
    >>> from tqdm._utils import _term_move_up
    >>> mw = MonoWorker()
    >>> def sleep(x):
    ...     time.sleep(x)
    ...     return x
    >>> for i in tqdm_auto.trange(10):
    ...     t = random.random()
    ...     assert mw.submit(sleep, t).result() == t
    ...     s = '{: <10}'.format(i)
    ...     tqdm_auto.write(_term_move_up() + s)
    >>> mw.pool.shutdown()
    """

# Generated at 2022-06-14 13:44:41.475720
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from tqdm.auto import trange

    def print_sleep(x):
        print(x)
        sleep(.1)

    monoworker = MonoWorker()
    monoworker.submit(print_sleep, 'start')
    sleep(.01)
    monoworker.submit(print_sleep, 'wait')
    sleep(.01)
    monoworker.submit(print_sleep, 'skip')
    sleep(.5)
    monoworker.submit(print_sleep, 'restart')
    sleep(.01)
    monoworker.submit(print_sleep, 'wait2')
    sleep(.01)
    monoworker.submit(print_sleep, 'skip2')
    sleep(.5)

# Generated at 2022-06-14 13:44:47.746082
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from tqdm import trange

    def print_output(n):
        """To be executed by MonoWorker"""
        for _ in trange(n):
            time.sleep(.1)

    mw = MonoWorker()

    for _ in trange(4):
        # Each submission should override the waiting task
        mw.submit(print_output, n=20)
        time.sleep(1)

    time.sleep(10)

# Generated at 2022-06-14 13:44:54.187273
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def returner_func(x, y):
        time.sleep(0.5)
        return x + y

    worker = MonoWorker()
    future1 = worker.submit(returner_func, 1, 2)
    future2 = worker.submit(returner_func, 2, 3)

    time.sleep(0.25)
    future3 = worker.submit(returner_func, 3, 4)

    time.sleep(0.3)

    assert future1.cancelled() is True
    assert future2.result() == 5
    assert future3.cancelled() is True

# Generated at 2022-06-14 13:45:05.453178
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from random import randint
    from threading import Event
    from tqdm import tqdm

    def func(i, j):
        time.sleep(0.01)
        return i * j

    m = MonoWorker()
    N = 5
    with tqdm(total=N*N) as t:
        finish = Event()
        while not finish.wait(randint(0, 20)/100):
            t.update(1)
            m.submit(func, N, N)
            if t.n == N*N:
                break
        finish.set()
    assert t.n == t.total


if __name__ == '__main__':
    try:
        test_MonoWorker_submit()
    finally:
        import os

# Generated at 2022-06-14 13:45:15.808177
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import numpy as np
    mw = MonoWorker()
    is_after_submit1 = False
    is_after_submit2 = False
    is_after_submit3 = False
    is_after_submit4 = False
    is_after_submit5 = False

    def a_func(x):
        return x*np.linspace(0, 1, 1000)

    def slow_func(x):
        for i in range(10):
            sleep(1)
            if i > 6:
                is_after_submit4 = True
                if i > 8:
                    is_after_submit5 = True
        return x

    f0 = mw.submit(a_func, 0)
    assert not is_after_submit1
    sleep(0.5)
    assert not is_after

# Generated at 2022-06-14 13:45:19.739798
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    def wait(delay):
        time.sleep(delay)
        return random.random()

    mw = MonoWorker()

    results = []
    for i in tqdm_auto.tqdm(range(10), desc='MonoWorker.submit'):
        r = mw.submit(wait, random.random() / 2.)
        results.append(r)
        time.sleep(random.random() / 10.)

    for r in results:
        print(r.result())

# Generated at 2022-06-14 13:45:30.340491
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .env import MONO_WORKER_TIME_TO_RUN, MONO_WORKER_TIME_TO_CANCEL
    from .test_env import expected_gen

    # Unit test for method submit of class MonoWorker
    def print_args(*args, **kwargs):
        tqdm_auto.write(str(args) + str(kwargs))
        sleep(MONO_WORKER_TIME_TO_RUN)
        return args[0]

    mono = MonoWorker()

    # submit will wait until the currently running task completed
    assert mono.submit(print_args, "1")
    assert mono.futures[0].result() == "1"

    # submit will replace the currently waiting task if len(futures) == 2

# Generated at 2022-06-14 13:45:35.232811
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # TODO
    pass


# Generated at 2022-06-14 13:45:42.502071
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from os import path

    def func():
        sleep(.5)
        raise ValueError
    assert not path.exists('test_MonoWorker_submit.txt')
    with MonoWorker() as p:
        p.submit(func)
        p.submit(lambda: 1 / 0)
        p.submit(lambda: open('test_MonoWorker_submit.txt', 'w').close())
        assert not path.exists('test_MonoWorker_submit.txt')
    assert path.exists('test_MonoWorker_submit.txt')

# Generated at 2022-06-14 13:45:53.874532
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import functools
    import concurrent.futures

    def error_after(secs):
        """Raise Exception after `secs` seconds"""
        @functools.wraps(error_after)  # preserve function name
        def _error_after(x, y):
            time.sleep(secs)
            raise Exception()
        return _error_after

    def safe_plus(x, y):
        """Add two numbers"""
        time.sleep(2)
        return x + y

    mworker = MonoWorker()
    f1 = mworker.submit(error_after(1), 0, 1)
    time.sleep(2)
    assert f1.done()
    assert f1.cancelled()

# Generated at 2022-06-14 13:46:02.881009
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def time_consuming(i, n=1):
        time.sleep(n)
        return i + 1

    def get_results(expected, futures):
        results = []
        for _ in range(expected):
            future = futures.popleft()
            if not future.done():
                tqdm_auto.write(
                    "Next future is not yet done even "
                    "though it should have been by now."
                )
            results.append(future.result())
        return results

    def check_results(expected, results, msg):
        assert results == expected, msg + "\nGot %r, expected %r." % (
            results, expected)

    # Test basic functionality:
    # submit jobs, get results in order and in time
    mono_worker = MonoWorker()
    futures = deque()

# Generated at 2022-06-14 13:46:13.617433
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from concurrent.futures import Future
    from time import sleep
    m = MonoWorker()

    # Setup
    Fut = Future()
    Fut.set_result("0")
    Fut1 = Future()
    Fut2 = Future()
    Fut3 = Future()
    Fut4 = Future()
    Fut5 = Future()
    m.futures.append(Fut)
    m.futures.append(Fut1)
    m.futures.append(Fut2)
    m.futures.append(Fut3)
    m.futures.append(Fut4)
    m.futures.append(Fut5)
    Fut1.set_result("1")
    Fut2.set_result("2")
    Fut3.set_result("3")

# Generated at 2022-06-14 13:46:19.590403
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def wait(this):
        time.sleep(0.01)  # this work should be discarded

    def work(this):
        for _ in tqdm_auto.tqdm(range(10)):  # this work should be kept
            time.sleep(0.01)

    instance = MonoWorker()
    instance.submit(wait, instance)
    time.sleep(0.1)
    instance.submit(work, instance)
    time.sleep(1)

# Generated at 2022-06-14 13:46:29.072544
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading
    from threading import Event
    from nose.tools import eq_

    def sleeper(event):
        event.wait()

    mw = MonoWorker()
    e = Event()
    f1 = mw.submit(sleeper, e)
    f2 = mw.submit(sleeper, e)
    mw.submit(sleeper, e)  # should do nothing

    eq_(len(mw.futures), 2)
    eq_(len(mw.pool._threads), 1)

    e.set()  # allow waiters to complete
    for future in [f1, f2]:
        future.cancel()  # should do nothing

    eq_(len(mw.futures), 2)
    eq_(len(mw.pool._threads), 1)



# Generated at 2022-06-14 13:46:36.742018
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import string
    from multiprocessing.dummy import Pool
    pool = Pool(4)

    def call(sleep_sec, task_name=None):
        if task_name is None:
            task_name = ''.join(random.choice(string.ascii_lowercase)
                                for _ in range(8))
        time.sleep(sleep_sec)
        return task_name, sleep_sec

    # Wait for results in order
    mono = MonoWorker()

    def wait_for(mono, sleep_sec, task_name=None):
        future = mono.submit(call, sleep_sec, task_name)
        return future.result()

    start = time.time()

# Generated at 2022-06-14 13:46:46.101970
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    def monkey(input_str, wait_time):
        sleep(wait_time)
        return input_str

    mono_worker = MonoWorker()

    future1 = mono_worker.submit(monkey, '1', 0.3)
    result1 = future1.result()
    assert result1 == '1'

    future2 = mono_worker.submit(monkey, '2', 0.1)
    result2 = future2.result()
    assert result2 == '2'

    future3 = mono_worker.submit(monkey, '3', 0.2)
    assert future1.done()
    assert not future2.done()
    assert not future3.done()
    result3 = future3.result()
    assert result3 == '3'
    assert not future2.done()

# Generated at 2022-06-14 13:46:52.971752
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from sys import version_info
    import time

    worker = MonoWorker()
    assert hasattr(worker, 'futures')

    assert worker.futures.maxlen == 2
    assert not worker.futures
    worker.futures.maxlen = 1
    assert worker.futures.maxlen == 1

    assert worker.futures.maxlen == 1
    assert not worker.futures

    def test(a, b):
        time.sleep(a)
        return a + b

    with tqdm_auto.tqdm(total=10) as pbar:
        for ii in range(10):
            pbar.update(1)
            worker.submit(test, ii, ii)
            time.sleep(0.1)


# Generated at 2022-06-14 13:47:05.782113
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Test the MonoWorker class by submitting a function.
    """
    with tqdm_auto.tqdm() as t:
        for i in tqdm_auto.tqdm(range(4)):
            MonoWorker().submit(lambda x: x ** 0.5, i)


if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:47:14.717870
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import os
    import time
    import threading

    mw = MonoWorker()

    t1_result = None
    def t1():
        time.sleep(0)
        os.write(1, b"test 1\n")
        nonlocal t1_result
        t1_result = True

    t2_result = None
    def t2():
        time.sleep(1)
        os.write(1, b"test 2\n")
        nonlocal t2_result
        t2_result = True

    t3_result = None
    def t3():
        time.sleep(0)
        os.write(1, b"test 3\n")
        nonlocal t3_result
        t3_result = True

    def main():
        # t1 should print "test 1"
        m

# Generated at 2022-06-14 13:47:25.699775
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from concurrent.futures import ThreadPoolExecutor
    from time import sleep
    def excep_adder(x, y):
        raise Exception('div by 0: {} + {}'.format(x, y))
    def slow_adder(x, y, secs=2):
        sleep(secs)
        return x + y

    worker = MonoWorker()
    res1 = worker.submit(slow_adder, 1, 2)
    res2 = worker.submit(excep_adder, 3, 4)
    assert not res1.done()
    assert res2.done()
    assert res1.result() == 3
    try:
        res2.result()
    except Exception as e:
        assert str(e) == 'div by 0: 3 + 4'
    else:
        assert False  # expected exception
    #

# Generated at 2022-06-14 13:47:34.775452
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from os import getcwd

    # Prepare data
    def mytask(i):
        sleep(2)
        return i, getcwd()

    def show_futures(monow, i=0):
        """ Show futures in queue, and their status if running. """
        print(('\n[' + str(i) + '] ' + '-' * 96))
        print(('[' + str(i) + '] ' + '#' * 96))
        for j, f in enumerate(monow.futures):
            print(('[' + str(i) + '] '), j, ')', f, f.done())
            if f.done():
                print(('[' + str(i) + '] '), 'result', f.result())

# Generated at 2022-06-14 13:47:42.678573
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def test(x):
        time.sleep(2)
        return x * 2

    mw = MonoWorker()
    mw.submit(test, 1)
    mw.submit(test, 2)
    mw.submit(test, 3)
    mw.submit(test, 4)
    assert mw.futures.maxlen == 2
    assert len(mw.futures) == 2
    assert mw.futures[0].result() == 4
    assert mw.futures[1].result() == 8

# Generated at 2022-06-14 13:47:50.900989
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def job(dur):
        time.sleep(dur)
        return dur

    mw = MonoWorker()
    t0 = time.time()
    d0 = mw.submit(job, 0.3)
    d1 = mw.submit(job, 0.1)
    assert (d1.result() == 0.1)
    assert (time.time() - t0 <= 0.3)
    d2 = mw.submit(job, 0.2)
    assert (d2.result() == 0.2)
    assert (time.time() - t0 <= 0.3)

# Generated at 2022-06-14 13:47:59.930693
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(x):
        import time
        time.sleep(x)
        return x

    mw = MonoWorker()

    def test(array1, array2):
        assert mw.submit(func, 1) not in array1
        assert mw.submit(func, 2) not in array2
        assert mw.submit(func, 3)     in array2

    test([1, 2], [2, 3])
    test([ ],    [3])
    test([1],    [1, 3])

if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:48:10.025939
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import multiprocessing as mp
    from ..compat import ThreadPoolExecutor as PoolExecutor
    from ..compat import is_terminal_running
    from ..utils import write_ignore_interrupt

    if not is_terminal_running():
        return

    write = write_ignore_interrupt

    def wait(seconds):
        for _ in tqdm_auto.tqdm(range(seconds), desc='wait',
                                unit='second', file=write):
            time.sleep(1)

    def wait_mt(seconds):
        def do_wait(seconds):
            for _ in tqdm_auto.tqdm(range(seconds), desc='wait',
                                    unit='second', file=write):
                time.sleep(1)

# Generated at 2022-06-14 13:48:18.714819
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    import sys

    def _test_MonoWorker_submit(a, sleep_time=0.01):
        print("Saving {} on disk...".format(a), file=sys.stderr)
        sleep(sleep_time)
        print("Saved {} on disk.".format(a), file=sys.stderr)
        return a

    def _test_MonoWorker_submit_exception(a, sleep_time=0.01):
        raise Exception("Intentional raise in _test_MonoWorker_submit_exception")

    worker = MonoWorker()
    worker.submit(_test_MonoWorker_submit, 'a')
    worker.submit(_test_MonoWorker_submit, 'b')

# Generated at 2022-06-14 13:48:29.347025
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import numpy as np

    def process(i, delay_=0):
        time.sleep(delay_)
        return i

    num_tasks = 5
    np.random.seed(0)
    delays = np.random.exponential(size=num_tasks)
    tasks = [i + 1 for i in range(num_tasks)]

    tqdm_auto.write("{: >10}  {: >10}  {: >10}  {: >10}".format("task", "delay", "reach", "time"))

    worker = MonoWorker()
    prev_reach = 0
    while tasks:
        i = random.choice(tasks)
        # submit
        waiting = worker.submit(process, i, delays[i - 1])
        # record time

# Generated at 2022-06-14 13:48:52.698441
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import multiprocessing
    from threading import current_thread

    mw = MonoWorker()

    def _m_time():
        return time.time(), current_thread().name

    def _add(*args):
        time.sleep(0.5)  # simulate work
        return args[0] + args[1]

    def _mul(*args):
        time.sleep(0.5)  # simulate work
        return args[0] * args[1]

    def _print(arg):
        print("\r" * 80 + str(arg), end="")

    def _clear():
        print("\r" * 80, end="")

    def _test_task():
        for i in range(4):
            rng = random.Random()

# Generated at 2022-06-14 13:49:04.128381
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test `MonoWorker.submit()`"""
    import time

    def N(n):
        time.sleep(n)
        return n

    t = MonoWorker()
    assert t.submit(N, 1) == 1
    assert t.submit(N, 2) == 1
    assert t.submit(N, 3) == 3
    assert t.submit(N, 4) == 3
    assert t.submit(N, 5) == 5
    assert t.submit(N, 6) == 5
    assert t.submit(N, 7) == 6
    assert t.submit(N, 8) == 7
    assert t.submit(N, 9) == 8
    assert t.submit(N, 10) == 9
    assert t.submit(N, 11) == 10

# Generated at 2022-06-14 13:49:15.484103
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def sleep(t):
        import time
        time.sleep(t)
        return t

    st = tqdm_auto._time()
    mw = MonoWorker()
    f1 = mw.submit(sleep, 1)
    f2 = mw.submit(sleep, 3)
    tqdm_auto.write('f1.result={}, f2.result={}'.format(f1.result(), f2.result()))
    f3 = mw.submit(sleep, 5)
    f4 = mw.submit(sleep, 7)
    tqdm_auto.write('f3.result={}, f4.result={}'.format(f3.result(), f4.result()))

# Generated at 2022-06-14 13:49:21.579119
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from unittest.mock import Mock
    import time
    from .test_tqdm_gui import _range

    mw = MonoWorker()

    for i in _range(1, 3):
        assert len(mw.futures) == i

    for i in _range(1, 2):
        mw.submit(time.sleep, 0.1)
        assert len(mw.futures) == 1

    mw.submit(Mock(side_effect=RuntimeError("test")))
    assert True  # no exception

# Generated at 2022-06-14 13:49:32.125339
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    i0 = 0

    def incr():
        """Simulate running task."""
        from time import sleep
        from sys import stderr
        nonlocal i0
        print("incr:", i0, file=stderr)
        i0 += 1
        sleep(1)

    def chk():
        """Simulate waiting task."""
        from sys import stderr
        print("chk:", i0, file=stderr)

    def chk2():
        """Simulate waiting task."""
        from sys import stderr
        print("chk2:", i0, file=stderr)

    mw = MonoWorker()
    mw.submit(incr)

    mw.submit(chk)
    mw.submit(chk2)

# Generated at 2022-06-14 13:49:39.243586
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import time
    import threading
    class Sleep(Exception):
        def __init__(self, t):
            super(Sleep, self).__init__()
            self.t = t
        def __str__(self):
            return str(self.t)

    mw = MonoWorker()
    seq = [random.randint(1, 10) for i in range(20)]
    def sleep(t):
        if t == 'x':
            raise Exception('just an exception')
        if t == 'y':
            raise Sleep('just a sleep')
        time.sleep(t)
        return t
    runs = []
    def _th():
        for s in seq:
            try:
                ret = sleep(s)
            except Exception as e:
                runs.append(str(e))
           

# Generated at 2022-06-14 13:49:49.484208
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event

    mw = MonoWorker()
    e1 = Event()
    e2 = Event()
    e3 = Event()
    e1.clear()
    e2.clear()
    e3.clear()

    def f1():
        with tqdm_auto.tqdm(desc="f1") as t:
            t.write("f1 starting")
            sleep(2)
            t.write("f1 running")
            e1.set()
            e2.wait()
            t.write("f1 stopping")
    def f3():
        with tqdm_auto.tqdm(desc="f3") as t:
            t.write("f3 starting")
            e3.wait()
            t.write("f3 running")
            t.write

# Generated at 2022-06-14 13:49:59.104742
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import numpy as np
    from ..std.testing import rands

    def is_a_palindrome(x):
        return str(x) + str(x)[::-1]
    # run the tests
    mono_worker = MonoWorker()
    tqdm_auto.write('MonoWorker test:')
    with tqdm_auto.tqdm(rands(30), dynamic_ncols=True) as t:
        for i in t:
            t.set_description('running')
            mono_worker.submit(is_a_palindrome, np.random.randint(0, 999999))
            t.set_description('waiting')
            time.sleep(0.1)
    tqdm_auto.write('\n')

# Generated at 2022-06-14 13:50:07.086105
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Lock
    m = MonoWorker()
    n_tasks_done = 0
    n_tasks_running = 0
    n_tasks_waiting = 0

    def task(lock, n):
        sleep(.5)
        with lock:
            nonlocal n_tasks_done
            n_tasks_done += 1

    lock = Lock()
    for i in tqdm_auto.tqdm(range(10)):
        with lock:
            assert n_tasks_running <= 1 and n_tasks_waiting <= 1
            n_tasks_running += 1
            n_tasks_waiting = len(m.futures) - n_tasks_running

        f = m.submit(task, lock, i)


# Generated at 2022-06-14 13:50:10.898692
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import randint
    from itertools import count

    mw = MonoWorker()
    for i in count():
        mw.submit(sleep, randint(0, 10))
        sleep(0.01)
        if i == 100:
            break

# Generated at 2022-06-14 13:50:44.166452
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from concurrent.futures import as_completed

    def func(x):
        sleep(x)
        return x

    worker = MonoWorker()
    futures = [worker.submit(func, x) for x in range(5)]
    for future in as_completed(futures):
        print(future.result())

# Generated at 2022-06-14 13:50:55.503335
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(*args, **kwargs):
        input_queue.get()
        return args, kwargs

    import time
    import multiprocessing
    import queue
    import threading

    input_queue = multiprocessing.Queue(1)
    output_queue = queue.Queue()

    def reader():
        while True:
            try:
                output_queue.put(worker.submit(func, "args", kwargs="kwargs"))
            except RuntimeError as e:
                output_queue.put(e)

    worker = MonoWorker()
    thread = threading.Thread(target=reader)
    thread.start()
    for _ in range(4):
        output_queue.get()
    input_queue.put(1)

# Generated at 2022-06-14 13:51:06.271715
# Unit test for method submit of class MonoWorker

# Generated at 2022-06-14 13:51:14.746221
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    worker = MonoWorker()

    def test_func(wait):
        time.sleep(wait)
        return wait

    # test running task
    worker.submit(test_func, 2)
    time.sleep(1)
    worker.submit(test_func, 1)
    time.sleep(1)
    worker.submit(test_func, 0)
    time.sleep(3)
    assert len(worker.futures) == 2

    # test running and waiting tasks with different durations
    worker.submit(test_func, 1)
    assert worker.submit(test_func, 2).result() == 2
    time.sleep(1)
    worker.submit(test_func, 3)
    time.sleep(4)

    # test running task with exception
    # e = Exception('exception')


# Generated at 2022-06-14 13:51:22.078262
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import gc
    from concurrent.futures import ThreadPoolExecutor

    def test_func(x):
        time.sleep(0.05)
        return x+1
    mw_1 = MonoWorker()
    mw_2 = MonoWorker()
    mw_3 = MonoWorker()
    tp_1 = ThreadPoolExecutor(max_workers=1)
    tp_2 = ThreadPoolExecutor(max_workers=2)
    # test when task is finished normally
    mw_1.submit(test_func, 1)
    if mw_1.futures[0].result() != 2:
        raise AssertionError()
    mw_2.submit(test_func, 3)
    mw_2.submit(test_func, 4)

# Generated at 2022-06-14 13:51:33.617199
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def func1(i):
        time.sleep(5)
        return i

    def func2(i):
        time.sleep(5)
        return 10 / i

    mw = MonoWorker()

    f = mw.submit(func1, 1)
    time.sleep(1)
    f = mw.submit(func1, 2)
    time.sleep(1)
    f = mw.submit(func1, 3)
    time.sleep(1)
    assert f.result() == 2

    f = mw.submit(func2, 0)
    time.sleep(1)
    assert f.result() == 10

    f = mw.submit(func1, 4)
    time.sleep(1)
    assert f.result() == 4


# Generated at 2022-06-14 13:51:41.689352
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Imports
    import sys
    import time

    queue = list('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')

    def sleep_and_print(s):
        time.sleep(s)
        sys.stdout.write(s)
        sys.stdout.flush()
        return s

    worker = MonoWorker()
    while len(queue) > 0:
        worker.submit(sleep_and_print, queue.pop(0))
        worker.submit(sleep_and_print, queue.pop(-1))


if __name__ == '__main__':
    # Unit test for method submit of class MonoWorker
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:51:49.476679
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from subprocess import run, PIPE
    from time import sleep
    from .tqdm_test_utils import with_prog_bar, closing

    x = MonoWorker()

    def dummy(sleep_for):
        sleep(sleep_for)
        return "Done sleeping for {} seconds".format(sleep_for)

    with closing(tqdm_auto.tqdm(total=2, unit='test')) as pbar:
        x.submit(dummy, 0.1)
        x.submit(dummy, 0.01)
        sleep(0.01)
        x.submit(dummy, 0.1)
        x.submit(dummy, 0.01)
        pbar.update()
        x.submit(dummy, 0.1)
        x.submit(dummy, 0.01)


# Generated at 2022-06-14 13:51:59.834452
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing.pool import ThreadPool
    from multiprocessing import cpu_count
    from threading import Thread
    from queue import Queue, Empty
    from contextlib import contextmanager

    max_workers = cpu_count()
    _pool = ThreadPool(max_workers)

    @contextmanager
    def mono_pool():
        """Context manager helper."""
        workers = MonoWorker()
        yield workers
        workers.shutdown()

    def test_max_workers(max_workers=max_workers, pool=_pool):
        """Make sure that max_workers is respected."""
        def dummy_task():
            sleep(1)


# Generated at 2022-06-14 13:52:08.250587
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import gc
    import time
    mw = MonoWorker()

    def func_a(*args, **kwargs):
        mw.func_a_args = args, kwargs
        time.sleep(1)
        return "func_a_result"

    def func_b(*args, **kwargs):
        mw.func_b_args = args, kwargs
        time.sleep(1)
        return "func_b_result"

    # submit func_a
    future_a = mw.submit(func_a, 1, 2, kwarg1='v1')
    assert future_a is not None
    assert mw.func_a_args == ((1, 2), {'kwarg1': 'v1'})
    assert not future_a.done()

    # submit func_b