

# Generated at 2022-06-14 13:42:53.042641
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import string
    import concurrent.futures
    from ..utils import _environ_cols_wrapper
    N = 100000

    def func(i):
        import random
        time.sleep(random.random() / 1000.)
        return ''.join(random.choice(string.ascii_letters)
                       for _ in range(random.randint(60, 100)))
    with MonoWorker() as mw:
        futures = [mw.submit(func, i) for i in range(N)]
    assert all(future.done() for future in futures)


# Generated at 2022-06-14 13:43:02.016927
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    try:
        import time
    except ImportError:
        pass
    else:
        def slow_task(n):
            time.sleep(1)
            return 42

        def cancel_task(n):
            import time
            while True:
                time.sleep(1)

        pool = MonoWorker()
        # The first task takes a while to run
        assert 42 == pool.submit(slow_task, 1).result()
        # The second task starts as soon as the previous one finishes
        assert 42 == pool.submit(slow_task, 1).result()
        # The third task will replace the second task
        assert 42 == pool.submit(slow_task, 1).result()
        try:
            # The fourth task is never run
            pool.submit(cancel_task, 1).result()
        except Exception:
            pass


# Generated at 2022-06-14 13:43:12.970788
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def test_func(i):
        time.sleep(i)
        return i

    mw = MonoWorker()
    mw.submit(test_func, 1)
    mw.submit(test_func, 1)
    mw.submit(test_func, 3)
    mw.submit(test_func, 2)
    mw.submit(test_func, 0.5)
    mw.submit(test_func, 2)
    mw.submit(test_func, 3)
    mw.submit(test_func, 0.8)
    assert len(mw.futures) == 1  # only the last (most recent) is submitted
    assert mw.futures[0].result() == 0.8  # last submitted has result



# Generated at 2022-06-14 13:43:23.066231
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event

    def test_func(t, i, n, future_i, e):
        sleep(t)
        future_i[0] = i
        e.set()

    e = Event()
    i = [None]
    mw = MonoWorker()
    for _ in range(6):
        mw.submit(test_func, 0.01, i=_, n=6, future_i=i, e=e)
        e.wait()
        assert i[0] == _
        e.clear()
    mw.submit(test_func, 0.1, i=6, n=6, future_i=i, e=e)
    e.wait(0.11)
    assert i[0] == 6
    e.clear()

# Generated at 2022-06-14 13:43:31.792896
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import concurrent.futures
    import time
    import unittest

    class TestCase(unittest.TestCase):
        def setUp(self):
            self.worker = MonoWorker()
            self.passed = False

        def test_blocking_1(self):
            def f_short(n):
                return n
            for x in range(4):
                self.worker.submit(f_short, x)

        def test_blocking_2(self):
            def f_short(n):
                return n
            def f_long(n):
                time.sleep(6)
                return n
            for x in range(4):
                self.worker.submit(f_short, x)
                self.worker.submit(f_long, x)


# Generated at 2022-06-14 13:43:42.337277
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import concurrent.futures
    import time
    import multiprocessing
    num_processors = multiprocessing.cpu_count()
    # pylint: disable=no-member
    assert num_processors > 1, "num_processors = 1, no test"
    num_threads = num_processors // 2
    assert num_threads > 0 and num_threads < num_processors, \
        "num_threads = 0 or num_processors, no test"

    def _execute(futures, func, *args, sleep_time=3, **kwargs):
        def future_status(future):
            try:
                return str(future.result())
            except concurrent.futures.CancelledError:
                return 'CANCELLED'
            except Exception as e:
                return

# Generated at 2022-06-14 13:43:49.244917
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import unittest

    class TestMonoWorker(unittest.TestCase):
        def setUp(self):
            self.MW = MonoWorker()

        def test_submit_simultaneous_tasks(self):
            start_time = time.time()
            for _ in range(4):
                self.MW.submit(time.sleep, 0.1)
            end_time = time.time()
            self.assertLessEqual(end_time - start_time, 0.2)

    unittest.main()

# Generated at 2022-06-14 13:43:59.687799
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import RLock
    from math import factorial

    m = MonoWorker()
    lock = RLock()
    func_times = []
    func_ints = []

    def moo(inp):
        sleep(0.3)
        with lock:
            func_ints.append(inp)
            func_times.append(tqdm_auto.format_interval(tqdm_auto.now()))

    for i in tqdm_auto.trange(9, smoothing=0.5):
        if i == 5:
            moo.func_code = lambda x: factorial(x)
        if i == 5:
            m.submit(moo, i)
        else:
            m.submit(moo, i)
        # m.submit(moo

# Generated at 2022-06-14 13:44:04.564783
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Event
    stop = Event()
    mw = MonoWorker()
    f2, f3 = mw.submit(time.sleep, 0.5), mw.submit(time.sleep, 2.5)
    mw.submit(time.sleep, 0.5)  # task f3 should be cancelled
    stop.set()
    f2.result(), f3.result()



# Generated at 2022-06-14 13:44:11.421455
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    import time

    def f(m, x):
        time.sleep(m)
        return x

    def g(m, x):
        global flag
        flag = True
        time.sleep(m)
        return x

    mw = MonoWorker()

    mw.submit(f, 0.1, 42)
    time.sleep(0.05)
    assert mw.futures[0].running() == True
    time.sleep(0.2)
    assert mw.futures[0].done() == True
    assert mw.futures[0].result() == 42

    global flag
    flag = False
    mw.submit(g, 0.1, 42)
    time.sleep(0.05)
    assert flag == True

# Generated at 2022-06-14 13:44:26.488237
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from concurrent.futures import TimeoutError
    from .std_import import ThreadPoolExecutor, Queue, Empty, \
        get_current_time_fun
    from ..std_lib import _wakeup_fd, \
        is_py3

    def _sleep(sec, terminate_flag=None):
        # simulate slow output
        if terminate_flag and terminate_flag.is_set():
            raise RuntimeError('cannot finish')
        time.sleep(sec)

    def _timeout_sleep(sec, terminate_flag=None):
        # simulate slow output
        if terminate_flag and terminate_flag.is_set():
            raise TimeoutError('cannot finish')
        time.sleep(sec)

    # Test default
    t = get_current_time_fun()
    w = MonoWorker()


# Generated at 2022-06-14 13:44:37.781729
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from . import MonoWorker
    from time import time
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    def fib_with_time(n):
        sleep(1)
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    # Test simple
    m = MonoWorker()
    assert m.submit(fib, 10).result() == 55
    assert m.submit(fib, 9).result() == 34

    # Test that second task will be run immediately
    t1 = time()
    assert m.submit(fib_with_time, 10).result() == 55
    assert time() - t1 < 1.05

    # Test that second task

# Generated at 2022-06-14 13:44:48.408965
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from signal import signal, SIGINT
    #from concurrent.futures import TimeoutError
    #from multiprocessing.pool import ThreadPool

    #signal(SIGINT, lambda signal, frame: pool.terminate())

    def test_func(arg, sleep_time):
        time.sleep(sleep_time)
        return arg

    mw = MonoWorker()
    try:
        for i in range(3):
            time.sleep(0.3)
            mw.submit(test_func, i, 1)
    except KeyboardInterrupt:
        assert False

    # TODO: not working
    # assert len(mw.futures) == 0
    # mw = MonoWorker()
    # for i in range(2):
    #     mw.submit(test_func,

# Generated at 2022-06-14 13:44:55.435464
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from ..utils import format_sizeof

    mw = MonoWorker()
    N = 4
    S = 1e9
    kw = dict()

    def g(i):
        kw['time'] = int(time.time())
        kw['i'] = i
        tqdm_auto.write('{time}  '.format(**kw))
        tqdm_auto.write('{i}  '.format(**kw))
        return S

    f1 = mw.submit(g, 1)
    f2 = mw.submit(g, 2)
    f3 = mw.submit(g, 3)
    f4 = mw.submit(g, 4)
    assert f4 == mw.futures[-1]
    f4.result()
    assert f4

# Generated at 2022-06-14 13:45:06.708929
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import cpu_count, Pool
    from sys import stderr

    # Write all stderr to /dev/null
    # (Need ';' because `with` is a compound statment and `if` is not)
    _stderr = stderr
    if 'win' in sys.platform.lower():
        from subprocess import check_call
        _stderr = open(os.devnull, 'w')
        with open(os.devnull, 'w') as devnull:
            check_call('SET ONN', shell=True, stdout=devnull,
                       stderr=devnull)  # noqa
    else:
        # Hide useless stderr output
        _stderr = open('/dev/null', 'w')

# Generated at 2022-06-14 13:45:16.907815
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep

    mw = MonoWorker()

    def func(i):
        sleep(i)
        return i

    for i in range(3):
        mw.submit(func, i+1)
    for i in range(3):
        f = mw.submit(func, i+1)
        assert f.result() == 3
    assert 1 == mw.submit(func, 0.001).result()  # done, not replaced
    assert 2 == mw.submit(func, 0.002).result()  # done, not replaced
    assert 3 == mw.submit(func, 0.003).result()  # done, not replaced
    assert 0.001 == mw.submit(func, 0.001).result()  # none done, replaced

# Generated at 2022-06-14 13:45:27.493645
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from multiprocessing import cpu_count
    from contextlib import closing
    from traceback import format_exc

    class TestFutures(object):
        """
        A method for testing the `submit` function of `MonoWorker`.
        Worker: 1, Futures: 1
        """

        def __init__(self):
            from concurrent.futures import Future

            self.future = Future()
            self.future.set_result(True)
            self.worker = MonoWorker()
            self.func = self.func_gen()
            self.args = ()
            self.kwargs = {}

        @staticmethod
        def func_gen():
            """Generator, returns next integer."""
            i = 0
            while True:
                i += 1
                yield i


# Generated at 2022-06-14 13:45:38.218888
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from sys import stderr

    # Workaround for: http://bugs.python.org/issue27964
    import concurrent.futures

    orig_executor_class, concurrent.futures.ThreadPoolExecutor = concurrent.futures.ThreadPoolExecutor, lambda *args: orig_executor_class(*args, initializer=lambda: setattr(threading.current_thread(), 'daemon', False))

    # Unit test
    # Separated to avoid the multiprocessing bug
    # http://bugs.python.org/issue9400
    # Fixed in Python 3.4, tested on Windows 7 64-bit
    # But cannot test on, eg, Python 3.2 (Windows 8)
    # or Python 3.3.3 (Linux)
    MW = MonoWorker()


# Generated at 2022-06-14 13:45:45.920378
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from concurrent.futures import as_completed

    def f(x):
        sleep(1)
        return x * x

    worker = MonoWorker()
    # Only the waiting task will be executed
    futures = {}
    tqdm_auto.write('submit waiting')
    futures['w'] = worker.submit(f, 2)
    sleep(0.5)
    tqdm_auto.write('submit running')
    futures['r'] = worker.submit(f, 3)
    sleep(0.5)
    tqdm_auto.write('submit running again')
    futures['ra'] = worker.submit(f, 4)

# Generated at 2022-06-14 13:45:56.998227
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from threading import Event
    e1, e2, e3, e4, e5, e6, e7, e8, e9 = (Event() for _ in range(9))
    e10, e11, e12, e13, e14, e15, e16, e17, e18 = (Event() for _ in range(9))
    e19, e20, e21, e22, e23, e24, e25, e26, e27 = (Event() for _ in range(9))

    def fake_work(e, sleeptime, msg):
        e.wait(sleeptime)
        tqdm_auto.write(msg)

    # init
    mw = MonoWorker()

# Generated at 2022-06-14 13:46:09.802499
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import traceback
    from concurrent.futures import TimeoutError

    def sleep_then_raise(i, seconds, exp):
        from time import sleep
        sleep(seconds)
        raise exp

    def sleep_then_return(i, seconds, value):
        from time import sleep
        sleep(seconds)
        return value

    # Clear tqdm output for doctesting
    tqdm_auto.write("")

    # Test timeout
    with tqdm_auto.tqdm(disable=True) as t:
        worker = MonoWorker()

        f1 = worker.submit(sleep_then_return, 1, 1, 42)
        f2 = worker.submit(sleep_then_raise, 2, 1, ValueError("2"))
        f3 = worker.submit(sleep_then_return, 3, 1, 13)

# Generated at 2022-06-14 13:46:17.006695
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def func(*args, **kwargs):
        for i in tqdm_auto.tqdm(range(10), desc='func1', leave=False, **kwargs):
            assert i % 3 == 0
    worker = MonoWorker()
    worker.submit(func, **set_kwargs)
    worker.submit(func, **set_kwargs)
    worker.submit(func, **set_kwargs)
    try:
        func(**set_kwargs)
    except Exception as e:
        tqdm_auto.write(str(e))
    return worker

test_MonoWorker_submit()

# Generated at 2022-06-14 13:46:23.284648
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def do_work(x):
        time.sleep(1)
        return x

    worker = MonoWorker()
    for i in range(3):
        worker.submit(do_work, i)
        time.sleep(0)
    worker.submit(do_work, 0)
    worker.submit(do_work, 1)
    worker.submit(do_work, 2)
    worker.submit(do_work, 3)


if __name__ == "__main__":
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:46:32.457288
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    # test cases
    def f1():
        time.sleep(2)
        return 1

    def f2():
        time.sleep(1)
        return 2

    def f3():
        time.sleep(3)
        return 3

    def f4():
        time.sleep(1)
        return 4

    def error_f():
        time.sleep(1)
        raise ValueError("error_f")

    # initialize worker
    worker = MonoWorker()

    # submit f1 and f2 (in this order)
    # since f2 is submitted later, it will replace f1 as the waiting task
    f1_future = worker.submit(f1)
    f2_future = worker.submit(f2)
    assert f1_future.done()
    assert f2_future.done()

# Generated at 2022-06-14 13:46:38.678287
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    def slow_square(x):
        time.sleep(random.random() / 10)
        return x ** 2

    mw = MonoWorker()
    futures = []
    for i in range(5):
        futures.append(mw.submit(slow_square, i * 2))
        time.sleep(random.random() / 10)
    for n, future in enumerate(futures):
        print(n, future.result())

# Generated at 2022-06-14 13:46:48.072794
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():

    import time
    import threading

    def do_work(i):
        time.sleep(0.5)
        return i

    worker = MonoWorker()

    # test clear waiting task
    worker.submit(do_work, 0)
    worker.submit(do_work, 1)
    worker.submit(do_work, 2)
    time.sleep(1)
    assert worker.futures[0].done()
    assert worker.futures[1].cancelled()

    # test do not clear running task
    worker.submit(do_work, 3)
    worker.submit(do_work, 4)
    worker.submit(do_work, 5)
    worker.submit(do_work, 6)
    assert worker.futures[0].result() == 3

# Generated at 2022-06-14 13:46:57.441091
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Lock
    from sys import stderr

    def write(msg):
        """thread-safe `print >>stderr, msg`"""
        with stderr_lock:
            tqdm_auto.write(msg, file=stderr)

    mw = MonoWorker()
    stderr_lock = Lock()
    res = []
    fut1 = mw.submit(res.append, 1)
    fut2 = mw.submit(res.append, 2)
    if fut2 is not None:
        write("Nothing should execute yet")
        assert fut2.cancel()
        assert not fut2.cancel()
    time.sleep(1e-3)
    if not fut1.done():
        write("Waiting for fut1 to be done...")

# Generated at 2022-06-14 13:47:06.826859
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from ._version import __version__
    from .tqdm import tqdm_deco, tqdm_notebook_deco
    from time import sleep

    @tqdm_deco(total=10, unit="b", ascii=True)
    def foo(x=1, delay=0.01, unit="", desc="Waiting..."):
        """Slow `sleep` but faster `tqdm`."""
        if unit == "":
            unit = x
        with tqdm_notebook_deco(total=x, unit=unit,
                                desc=desc, leave=False, miniters=1) as t:
            for i in range(x):
                sleep(delay)
                t.update()

    # Test slow `sleep` but faster `tqdm`
    foo(x=10)

# Generated at 2022-06-14 13:47:13.738874
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from .example import with_bar

    worker = MonoWorker()
    with_bar(worker, 7)
    worker.submit(sleep, 10)  # will be cancelled by next submit
    worker.submit(sleep, 10)
    worker.submit(sleep, 10)  # will be cancelled by cancel running
    with_bar(worker, 7)
    worker.submit(sleep, 10)  # will be cancelled by next submit
    worker.submit(sleep, 10)
    worker.submit(sleep, 10)  # will be cancelled by next submit
    with_bar(worker, 7)


# Generated at 2022-06-14 13:47:24.803928
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    It tests various scenarios with the `MonoWorker` class.

    This unit test is executed as `python -m tqdm.contrib.monoworker`.
    """
    import time
    import sys

    print("# Start testing: test_MonoWorker_submit")

# Generated at 2022-06-14 13:47:42.358553
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """This test aims to assert that MonoWorker.submit()
    only has a maximum of two submitted jobs"""
    import time
    import numpy as np

    def work(item, sleep=0.5):
        """A dummy function to simulate heavy task"""
        time.sleep(sleep)
        return item

    mw = MonoWorker()
    items = np.random.randint(0, 5, 10)
    for item in items:
        if item <= 2:
            mw.submit(work, item, sleep=0.5)
        else:
            mw.submit(work, item, sleep=0.1)

    time.sleep(2)
    assert len(mw.futures) == 1

# Generated at 2022-06-14 13:47:52.816950
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    worker = MonoWorker()
    assert worker.submit(lambda x=0: 1 / x) is None
    assert worker.submit(lambda x: 2 * x, 2).result() == 4.0
    assert worker.submit(lambda x: 2 * x, 42).result() == 84.0
    assert len(worker.futures) == 1
    assert worker.futures[0].result() == 84.0
    assert worker.submit(lambda x: 2 * x, 84).result() == 168.0
    assert len(worker.futures) == 1
    assert worker.futures[0].result() == 168.0
    assert worker.submit(lambda x: 2 * x, 168).result() == 336.0
    assert len(worker.futures) == 1

# Generated at 2022-06-14 13:48:03.586385
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    def do_nothing():
        pass
    def do_wait(dur):
        time.sleep(dur)
        return dur
    worker = MonoWorker()

    # test non-blocking (running) tasks
    # no waiting tasks
    assert worker.submit(do_nothing).result() is None
    # have waiting tasks
    assert worker.submit(do_nothing).result() is None

    # test blocking (waiting) tasks
    # no running tasks
    assert worker.submit(do_wait, 1).result() == 1
    # have running tasks
    assert worker.submit(do_wait, 2).result() == 2
    assert worker.submit(do_wait, 3).result() == 3
    assert worker.submit(do_wait, 0).result() == 0

# Generated at 2022-06-14 13:48:13.357727
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from timeit import default_timer
    from sys import stdout
    from multiprocessing import cpu_count
    from concurrent.futures import TimeoutError

    expected_results = []
    actual_results = []

    def record_result(result):
        actual_results.append(result)
        for out in expected_results, actual_results:
            tqdm_auto.write(str(out), file=stdout)

    def worker(n):
        def inner():
            sleep(1)
            return n
        return inner

    mw = MonoWorker()
    expected_results.append([0])
    mw.submit(worker(0), callback=record_result)
    s = default_timer()

# Generated at 2022-06-14 13:48:22.323390
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time

    def test(x):
        time.sleep(0.1)
        return x * x

    m = MonoWorker()
    assert m.submit(test, 2) is None
    assert m.submit(test, 3) is None
    assert m.submit(test, 4) is None

    times = []
    for i in range(5):
        m.submit(test, i)
        start = time.time()
        x = m.futures[0].result()
        times.append((i, x, time.time() - start))
        time.sleep(0.05)

# Generated at 2022-06-14 13:48:32.481506
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """
    Unit test for method submit of class MonoWorker
    """
    import time
    import numpy as np
    from tqdm.auto import tqdm
    from multiprocessing import Queue
    from concurrent.futures import Future

    q = Queue()

    def run_worker():
        a = MonoWorker()
        for _ in tqdm(range(100), desc="submit"):
            a.submit(q.put, np.random.randint(0, 10))
            time.sleep(0.1)
        for _ in tqdm(range(10), desc="results"):
            print(q.get(block=True))

        a = MonoWorker()

# Generated at 2022-06-14 13:48:39.938704
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    mw = MonoWorker()
    assert len(mw.futures) == 0  # pylint: disable=len-as-condition
    mw.submit(sleep, 0.1).result()
    assert len(mw.futures) == 0  # pylint: disable=len-as-condition
    mw.submit(sleep, 0.2).result()
    assert len(mw.futures) == 0  # pylint: disable=len-as-condition
    mw.submit(sleep, 2).result()
    assert len(mw.futures) == 0  # pylint: disable=len-as-condition
    mw.submit(sleep, 2).result()
    assert len(mw.futures) == 0  # pylint: disable

# Generated at 2022-06-14 13:48:49.524051
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    from collections import deque
    from time import time
    from time import sleep

    def do_work(n):
        tqdm_auto.write('n = %r' % n)
        sleep(0.2)
        return n * n

    class Test():
        """Mock tqdm.auto.tqdm"""
        def write(self, s):
            sys.stderr.write(s + '\n')
        def __enter__(self):
            return self
        def __exit__(self, *exc):
            return False

    class Out():
        """Mock sys.stdout"""
        def write(self, s):
            self.s = s
        def getvalue(self):
            return self.s


# Generated at 2022-06-14 13:48:57.726209
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random
    from multiprocessing import cpu_count
    from .utils import get_context_manager
    num_cpus = cpu_count()
    # for i in range(num_cpus * 3):
    for i in range(10):
        with get_context_manager() as t:
            t.set_description('task %s' % i)
            sleep(random() + 0.1)
            last_waiting_fut = t.worker.futures[-1]
            assert (len(t.worker.futures) == 1 or
                    last_waiting_fut.done())

# Generated at 2022-06-14 13:49:07.144904
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time, random
    from contextlib import contextmanager

    def worker(name, t):
        time.sleep(t)
        return name, t

    @contextmanager
    def maybe_cancel(tasks):
        yield
        for task in tasks:
            with tqdm_auto.maybe_show_bar(task) as pbar:
                if pbar:
                    pbar.close()
                else:
                    tqdm_auto.write("# cancelled")
            task.cancel()
        time.sleep(1)  # wait for cancellation


# Generated at 2022-06-14 13:49:31.394968
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys

    def print_time(*args, **kwargs):
        time.sleep(0.1)
        print(time.time())

    mw = MonoWorker()
    mw.submit(print_time, 0)
    time.sleep(0.1)
    mw.submit(print_time, 1)
    time.sleep(0.1)
    mw.submit(print_time, 2)
    time.sleep(0.1)
    mw.submit(print_time, 3)
    time.sleep(0.1)
    mw.submit(print_time, 4)
    time.sleep(0.1)
    mw.submit(print_time, 5)
    time.sleep(0.1)
    mw.submit(print_time, 6)


# Generated at 2022-06-14 13:49:40.038687
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import sys

    def func(n):
        time.sleep(n)
        return n

    worker = MonoWorker()
    start_time = time.time()
    task1 = worker.submit(func, 2)
    task2 = worker.submit(func, 1)
    task3 = worker.submit(func, 1)
    task4 = worker.submit(func, 1)
    task5 = worker.submit(func, 2)
    for task in [task3, task4, task5]:
        task.cancel()
        with tqdm_auto.wrapattr(sys.stderr, "buffer", 0):
            print(task.cancelled())

# Generated at 2022-06-14 13:49:49.804096
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    def run(i, delay=1):
        import time
        time.sleep(delay)
        return i

    mw = MonoWorker()
    mw.submit(run, 0, delay=5)
    assert len(mw.futures) == 1
    assert mw.futures[0].result() == 0

    mw.submit(run, 1, delay=5)
    assert len(mw.futures) == 1
    assert mw.futures[0].result() == 1

    mw.submit(run, 2, delay=3)
    assert len(mw.futures) == 2
    assert mw.futures[0].result() == 1
    assert mw.futures[1].result() == 2


# Generated at 2022-06-14 13:49:59.735459
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import gc
    import time
    try:
        from queue import Empty
    except ImportError:
        from Queue import Empty

    from ..utils import format_sizeof

    def sleeper(t):
        time.sleep(t)
        return t

    mw = MonoWorker()
    f1 = mw.submit(sleeper, 0.5)
    f2 = mw.submit(sleeper, 0.1)
    f3 = mw.submit(sleeper, 0.5)
    f4 = mw.submit(sleeper, 0.8)

    # NOTE: `gc.collect()` is needed for `f1` to be collected on Python 2
    gc.collect()
    assert f1.done() and not f2.done() and f3.done() and not f4.done()

# Generated at 2022-06-14 13:50:06.118428
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    mw = MonoWorker()

    def f1(a, b=1):
        return a * b

    def f2(a, b=1):
        return a * b

    f1_res = mw.submit(f1, 1, 2)
    f2_res1 = mw.submit(f2, 2, 2)
    # f1 is still running
    f2_res2 = mw.submit(f2, 3, 3)
    # f1 is being replace by f2
    f1_res.result()
    f2_res2.result()
    mw.shutdown()

# Generated at 2022-06-14 13:50:16.239198
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from concurrent.futures import TimeoutError

    def wait_n_inc(n, x=0):
        time.sleep(n)
        return x + 1

    def time_limit_raise(n, x=0):
        time.sleep(n)
        raise TimeoutError('timeout!')

    # test wait_n_inc, max_workers = 1
    mw = MonoWorker()

    # test wait_n_inc
    a = mw.submit(wait_n_inc, 1)
    b = mw.submit(wait_n_inc, 2)
    time.sleep(0.2)
    assert not a.done()
    assert a.result() == 1
    assert b.result() == 1

    # test time_limit_raise

# Generated at 2022-06-14 13:50:26.563070
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from tqdm.auto import trange
    import time
    from threading import Thread

    def _print(x):
        time.sleep(x)
        tqdm_auto.write("{}".format(x))

    # 1) Test basic working
    worker = MonoWorker()
    worker.submit(_print, 0.2)
    time.sleep(0.1)
    worker.submit(_print, 0.3)
    time.sleep(0.6)
    tqdm_auto.write("Should be only 0.3")

    # 2) Test queuing
    worker = MonoWorker()
    worker.submit(_print, 0.2)
    time.sleep(0.1)
    worker.submit(_print, 0.5)
    worker.submit(_print, 0.3)

# Generated at 2022-06-14 13:50:32.751562
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    from threading import Event
    from .utils import TestCase

    with TestCase():
        event = Event()

        def sleeper():
            event.wait(2)

        @MonoWorker.submit
        def monkey():
            return "Monkey!"

        @MonoWorker.submit
        def idiot():
            return "I am an idiot"

        @MonoWorker.submit
        def panda():
            while not event.wait(1):
                pass
            raise ValueError("panda")

        assert monkey.result() == "Monkey!"
        assert idiot.result() == "I am an idiot"
        assert monkey.cancel()
        assert not monkey.cancelled()
        assert panda.cancel()

# Generated at 2022-06-14 13:50:39.312207
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random

    def foo(x, y):
        time.sleep(random.random())
        return x + y

    worker = MonoWorker()
    futures = []
    for i in range(10):
        future = worker.submit(foo, i, 2)
        futures.append(future)
    for future in futures:
        assert future.result() == 3
# Run unit test above
if __name__ == '__main__':
    test_MonoWorker_submit()

# Generated at 2022-06-14 13:50:48.213093
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from queue import Empty, Queue
    from unittest import main

    class TestTask(object):
        def __init__(self, q):
            self.q = q

        def __call__(self, *args, **kwargs):
            # Run task with no wait
            self.q.put(args + tuple(kwargs.values()))

    class TestTQDM(tqdm_auto.tqdm):
        def __init__(self, *args, **kwargs):
            super(TestTQDM, self).__init__(*args, **kwargs)
            self.task_no = 0

        def submit(self, *args, **kwargs):
            # Submit task with a wait
            self.task_no += 1
            sleep(0.1)


# Generated at 2022-06-14 13:51:30.307668
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    # Imports
    import time
    from queue import Queue
    from threading import Thread
    # Test environment
    queue = Queue()
    # Thread pool test
    results = [0] * 10
    pool = MonoWorker()
    threads_expected = []
    for i in tqdm_auto.tqdm(range(10), desc='threads'):
        threads_expected.append(i)
        future_expected = None
        if i % 3 == 0:
            future_expected = pool.submit(lambda: 42)
        f = pool.submit(lambda x: results.__setitem__(x, 2), i)
        if future_expected is not None:
            assert f == future_expected
        queue.put(f)

# Generated at 2022-06-14 13:51:35.258124
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from random import random
    from time import sleep

    def test_task(i):
        sleep(random())
        return i

    task_num = 10
    mw = MonoWorker()
    for i in range(task_num):
        mw.submit(test_task, i)
    sleep(1)  # sleep to make sure that all tasks are submitted
    assert len(mw.futures) == 1, '%s != 1' % (len(mw.futures))



# Generated at 2022-06-14 13:51:44.085017
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from random import random
    print('testing MonoWorker.submit(func, args, kwargs)')

    # test function
    def _f(tqdm=tqdm_auto, sleep=sleep, random=random,
           mul=2, add=0, div=1):
        sleep(mul * random() / div + add)

    # initialize worker
    worker = MonoWorker()

    # try fast but simple task
    print('trying fast but simple task...')
    fut1 = worker.submit(_f, add=0.1, div=0.1)
    fut1.result()

    # try slow and complex task
    print('trying slow and complex task...')
    fut2 = worker.submit(_f, mul=10, add=3, div=3)

# Generated at 2022-06-14 13:51:51.392783
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import threading
    import multiprocessing.dummy as mp
    from time import time
    from time import sleep
    from concurrent.futures import ThreadPoolExecutor

    NUM_WORKERS = 5
    SLEEP_TIME = 0.1

    result_queue = mp.Queue()
    pool = ThreadPoolExecutor(max_workers=NUM_WORKERS)

    def do_work(num):
        """
        A blocking function
        """
        sleep_time = random.randint(1, 5)
        sleep_time = SLEEP_TIME * sleep_time
        sleep(sleep_time)
        result_queue.put(num)

    def worker_main(worker):
        """
        worker main function
        """

# Generated at 2022-06-14 13:52:02.200230
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import threading

    def dummy_task(time_to_sleep):
        print('start dummy task to sleep', time_to_sleep)
        time.sleep(time_to_sleep)
        print('finished dummy task to sleep', time_to_sleep)
        return threading.current_thread()

    mw = MonoWorker()
    mw.submit(dummy_task, 1)  # start sleep(1) in a thread
    print(mw.futures)  # [<Future at 0x2f7a828 state=running>]
    time.sleep(0.1)
    mw.submit(dummy_task, 2)  # start sleep(2) in a thread but cancel sleep(1)
    print(mw.futures)  # [<Future at 0x2f7

# Generated at 2022-06-14 13:52:08.305058
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import time
    import random
    import unittest
    from more_itertools import pairwise

    class TestMonoWorker_submit(unittest.TestCase):
        def test_MonoWorker_submit(self):
            random.seed(0)
            self.assertEqual([(None, None), (0, 1), (1, 2), (2, 3)],
                             list(pairwise(MonoWorker().submit(n)
                                           for n in [None, 0, 1, 2, 3])))

            def func(n):
                if n == 0:
                    raise Exception(n)
                time.sleep(random.random() * 0.2)
                return n

            # Supposed to be aborted and replaced with 1

# Generated at 2022-06-14 13:52:16.186531
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import sys
    import time
    import traceback
    from .tests import _monkeypatch_tqdm  # noqa

    class writer(object):
        def __init__(self):
            self.text = ''

        def write(self, txt):
            self.text += txt

        def flush(self):
            pass

    def test_func(i):
        time.sleep(3)
        return i

    def test_func_err():
        raise ValueError("TEST_ERROR")

    # common test
    sys.stdout = writer()
    mw = MonoWorker()
    i = 1
    mw.submit(test_func, i)
    time.sleep(0.1)
    assert mw.futures[0].result() == i
    assert sys.stdout.text == ""

# Generated at 2022-06-14 13:52:26.350163
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    """Test method submit of class MonoWorker (uses futures)."""
    import time
    from random import randint

    def f(i):
        time.sleep(2)
        return i**2

    m = MonoWorker()
    assert len(m.futures) == 0
    assert m.submit(f, 2)  # will wait
    assert len(m.futures) == 1
    assert m.submit(f, 2) is None  # will be discarded
    assert len(m.futures) == 1
    assert m.submit(f, 3) is None  # will be discarded
    assert len(m.futures) == 1
    time.sleep(2)
    assert m.submit(f, 4)  # will wait
    assert len(m.futures) == 1

# Generated at 2022-06-14 13:52:28.994781
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    from time import sleep
    from os import getpid

    a = None

    def assign(value):
        nonlocal a
        sleep(1)
        a = value

    m = MonoWorker()
    m.submit(assign, 1)
    m.submit(assign, 2)
    m.submit(assign, 3)
    assert a is None
    sleep(1.5)
    print(getpid(), a)
    assert a == 2



# Generated at 2022-06-14 13:52:33.515877
# Unit test for method submit of class MonoWorker
def test_MonoWorker_submit():
    import random
    import time
    import warnings

    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        def compute(x):
            time.sleep(random.random())
            return x**2

        worker = MonoWorker()
        assert len(worker.futures) == 0

        assert [44, 49, 64] == [
            compute(i)
            for i in range(10, 13)
            if i % 2 == 0
        ]

        assert [9, 16, 25] == [
            worker.submit(compute, i).result()
            for i in range(10, 13)
            if i % 3 == 0
        ]
