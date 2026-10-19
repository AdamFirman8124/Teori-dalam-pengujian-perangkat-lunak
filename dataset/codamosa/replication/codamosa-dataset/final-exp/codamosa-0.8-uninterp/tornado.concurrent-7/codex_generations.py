

# Generated at 2022-06-14 11:50:18.940079
# Unit test for function chain_future
def test_chain_future():
    f = Future()  # type: Future[int]
    g = Future()  # type: Future[int]
    chain_future(f, g)
    f.set_result(42)
    assert g.result() == 42
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_exception(ValueError())
    try:
        g.result()
        assert False, 'expected exception'
    except ValueError as e:
        assert True



# Generated at 2022-06-14 11:50:30.232216
# Unit test for function run_on_executor
def test_run_on_executor():
    from tornado.ioloop import IOLoop
    import time

    class FakeTime(object):
        calls = []

        def __init__(self, result):
            self.result = result

        def sleep(self, secs):
            self.calls.append(secs)
            return self.result

    ioloop = IOLoop()
    ioloop.make_current()
    ft = FakeTime(result=None)
    # run_on_executor, even though it calls "blocking" code, does not
    # delay the ioloop or wait for actual time to pass.
    @run_on_executor
    def f():
        time.sleep(1e6)
        return 42

    @run_on_executor
    def g():
        time.sleep(1e6)
        1 / 0



# Generated at 2022-06-14 11:50:39.481840
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.ioloop import IOLoop, PeriodicCallback
    import logging

    IOLoop.clear_instance()
    IOLoop.clear_current()
    app_log.name = __name__
    logging.getLogger().setLevel(logging.DEBUG)

    future = Future()
    PeriodicCallback(
        lambda: future_set_exception_unless_cancelled(future, RuntimeError()), 100
    ).start()
    IOLoop.current().add_callback(future.cancel)
    IOLoop.current().run_sync(lambda: future)
    assert future.cancelled()

# Generated at 2022-06-14 11:50:46.033856
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test
    from tornado.platform.asyncio import AsyncIOMainLoop

    AsyncIOMainLoop().install()

    @gen_test
    async def f():
        af = Future()
        cf = futures.Future()
        chain_future(cf, af)
        test_args = (None, None, None)
        cf.set_exception(RuntimeError())
        try:
            await af
        except RuntimeError:
            _, _, test_args = sys.exc_info()
        assert test_args[2] is not None

# Generated at 2022-06-14 11:51:00.127276
# Unit test for function chain_future
def test_chain_future():
    def setup_future(value, is_exc=False):
        f = Future()
        if is_exc:
            f.set_exception(value)
        else:
            f.set_result(value)
        return f

    f1, f2 = setup_future(1), setup_future(2)
    chain_future(f1, f2)
    assert f1.result() == 1 and f2.result() == 1

    f1, f2 = setup_future(1), setup_future(2)
    chain_future(f1, f2)
    f2.set_result(3)
    assert f1.result() == 1 and f2.result() == 1

    f1, f2 = setup_future(1, is_exc=True), setup_future(2)

# Generated at 2022-06-14 11:51:12.533274
# Unit test for function chain_future
def test_chain_future():
    "Test the chain_future() function."

    @run_on_executor
    def get_five() -> int:
        return 5

    @run_on_executor
    def get_ten() -> int:
        return 10

    @run_on_executor
    def get_division(num: int, divisor: int) -> int:
        return num / divisor

    @run_on_executor
    def get_string(num1: int, num2: int, num3: int) -> str:
        return '{} {} {}'.format(num1, num2, num3)

    @run_on_executor
    def raise_future_error() -> None:
        raise ZeroDivisionError

    @run_on_executor
    def raise_exception() -> None:
        raise Att

# Generated at 2022-06-14 11:51:16.247875
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, "test")
    assert future.result() == "test"

    future.cancel()
    future_set_result_unless_cancelled(future, "test")
    assert future.cancelled()



# Generated at 2022-06-14 11:51:22.391208
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    assert b.result() == 42
    a.set_result(1729)
    assert b.result() == 42



# Generated at 2022-06-14 11:51:33.462989
# Unit test for function chain_future
def test_chain_future():
    import unittest

    class ChainFutureTest(unittest.TestCase):
        def test_chain_future(self):
            f = Future()

            def copy(future):
                assert future is f
                future_set_result_unless_cancelled(g, "test")

            g = Future()
            chain_future(f, g)
            f.add_done_callback(copy)
            f.set_result(None)
            self.assertEqual(g.result(), "test")
            h = Future()
            chain_future(f, h)
            self.assertEqual(h.result(), "test")
            self.assertRaises(ReturnValueIgnoredError,
                              chain_future, f, Future())

    unittest.main()

# Generated at 2022-06-14 11:51:45.769521
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import concurrent.futures
    import asyncio
    from tornado.platform.asyncio import to_asyncio_future, to_tornado_future

    executor = concurrent.futures.ThreadPoolExecutor(1)
    io_loop = asyncio.get_event_loop()

    def make_concurrent_future():
        return executor.submit(lambda: 5)

    def make_asyncio_future():
        return asyncio.Future()

    def make_tornado_future():
        return to_tornado_future(io_loop, make_asyncio_future())


# Generated at 2022-06-14 11:51:57.415058
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.ioloop import IOLoop

    async_future = Future()
    IOLoop.current().add_future(async_future, lambda future: None)
    future = async_future.result()
    assert not future.cancelled()

    future_set_exception_unless_cancelled(future, RuntimeError())
    assert isinstance(future.exception(), RuntimeError)

    future_set_exception_unless_cancelled(future, RuntimeError())
    assert isinstance(future.exception(), RuntimeError)

# Generated at 2022-06-14 11:52:03.246506
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    assert not f.done()

    future_set_result_unless_cancelled(f, 1)
    assert f.done()
    assert f.result() == 1

    e = Future()
    e.cancel()
    assert e.done()

    future_set_result_unless_cancelled(e, 2)
    assert e.done()
    assert e.cancelled()

# Generated at 2022-06-14 11:52:15.136779
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    assert b.result() == 42
    a = Future()
    b = Future()
    a.set_result(42)
    chain_future(a, b)
    assert b.result() == 42
    a = Future()
    b = Future()
    chain_future(a, b)
    b.set_exception(ValueError())
    assert_raises(ValueError, a.result)
    a = Future()
    b = Future()
    a.set_exception(ValueError())
    chain_future(a, b)
    assert_raises(ValueError, b.result)

# Generated at 2022-06-14 11:52:19.912701
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    def do_test(method):
        future = asyncio.Future()
        method(future, "success")
        assert future.result() == "success"

        future = asyncio.Future()
        future.cancel()
        method(future, "should not set value")
        assert future.cancelled()
        assert not future.done()

    do_test(future_set_result_unless_cancelled)

# Generated at 2022-06-14 11:52:32.707371
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_result('foo')
    assert future2.result() == 'foo'

    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1_exc_info = (ZeroDivisionError, ZeroDivisionError(), None)
    future1.set_exception(future1_exc_info[1])
    assert future2.exception() == future1_exc_info[1]

    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1_exc_info = (ZeroDivisionError, ZeroDivisionError(), None)
    future1.set_exception

# Generated at 2022-06-14 11:52:37.905878
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42

    # let's make sure f1 isn't holding a reference to f2 anywhere
    f2 = None
    import gc
    gc.collect()
    f1 = None
    gc.collect()

# Generated at 2022-06-14 11:52:50.798733
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import logging
    import time

    def f(future):
        time.sleep(0.0001)  # yield to other thread
        future.set_result(42)

    def g(future):
        future.set_result(23)

    # case 1: f is called before g
    future = Future()
    chain_future(future, Future())
    f(future)

    # case 2: g is called before f
    future = Future()
    chain_future(future, Future())
    g(future)

    # case 3: g is called before f, and then f raises an exception
    future = Future()
    chain_future(future, Future())
    g(future)
    f(future)



# Generated at 2022-06-14 11:52:55.076387
# Unit test for function chain_future
def test_chain_future():
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_result(None)
    assert g.done()


if __name__ == "__main__":
    import unittest
    unittest.main()

# Generated at 2022-06-14 11:53:07.283989
# Unit test for function chain_future

# Generated at 2022-06-14 11:53:14.663807
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing

    f = Future()
    g = Future()

    chain_future(f, g)
    assert not g.done()
    f.set_result(None)
    assert g.done()

    f = Future()
    g = Future()
    h = Future()
    chain_future(f, g)
    chain_future(h, f)
    assert not f.done()
    assert not g.done()
    h.set_result(None)
    assert f.done()
    assert g.done()

    f = Future()
    g = Future()
    h = Future()

    chain_future(f, g)
    f.set_exception(KeyError())
    assert g.done()
    assert g.exception() is not None

    chain_future(h, f)


# Generated at 2022-06-14 11:53:34.892334
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None

    class Foo(object):
        executor = dummy_executor

        def __init__(self) -> None:
            self.async_result = None  # type: Future

        def sync_method(self) -> str:
            return "result"

        @run_on_executor
        def async_method(self) -> str:
            return self.sync_method()

        @run_on_executor
        def async_method_with_callback(self) -> str:
            self.async_result = Future()
            return self.async_result

    foo = Foo()
    future = foo.async_method()
    assert future.result() == "result"

    IO_loop = IOLoop.current()  # type: IOLoop
    future = foo.async_

# Generated at 2022-06-14 11:53:40.713399
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    async def test():
        future = Future()
        future_set_exception_unless_cancelled(future, ValueError())
        assert future.exception() is not None
        assert isinstance(future.exception(), ValueError)
        future = Future()
        future.cancel()
        future_set_exception_unless_cancelled(future, ValueError())
        assert future.exception() is None
        await tornado.gen.sleep(0)

    tornado.testing.unittest_run_loop(test())

# Generated at 2022-06-14 11:53:53.793057
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import logging
    import unittest

    class F(Future):
        def __init__(self, *, cancelled: Optional[bool] = None):
            super().__init__()
            self.cancelled = cancelled

        def cancel(self) -> bool:
            return self.cancelled

    class UT(unittest.TestCase):
        def test_set_exception(self):
            f = F()
            future_set_exception_unless_cancelled(f, RuntimeError)
            self.assertEqual(f.exception(), RuntimeError)

        def test_set_exception_cancelled(self):
            f = F(cancelled=True)
            f.set_exception(RuntimeError)
            with self.assertLogs(level=logging.ERROR) as cm:
                future

# Generated at 2022-06-14 11:53:57.087135
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    future = Future()
    future_set_result_unless_cancelled(future, 42)
    assert future.result() == 42
    future_set_result_unless_cancelled(future, 42)


# Generated at 2022-06-14 11:54:09.537282
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()  # type: Future[int]
    f2 = Future()  # type: Future[int]
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ZeroDivisionError())
    try:
        f2.result()
    except ZeroDivisionError:
        pass
    else:
        raise AssertionError("did not propagate exception")
    f3 = Future()
    f3.cancel()
    chain_future(f1, f3)
    assert f3.cancelled()



# Generated at 2022-06-14 11:54:16.869258
# Unit test for function chain_future
def test_chain_future():
    from concurrent.futures import Future as CFuture
    from tornado.testing import AsyncTestCase

    cf = CFuture()
    f = Future()
    chain_future(cf, f)
    assert f.result() is cf.result() is _NO_RESULT
    cf.set_result(42)
    assert f.result() is _NO_RESULT
    cf = CFuture()
    f = Future()
    chain_future(cf, f)
    cf.set_exception(ZeroDivisionError())
    assert f.result() is _NO_RESULT
    cf = CFuture()
    f = Future()
    chain_future(cf, f)
    cf.cancel()
    assert f.result() is _NO_RESULT


# Generated at 2022-06-14 11:54:25.546692
# Unit test for function chain_future
def test_chain_future():
    async def target(i: int) -> int:
        await asyncio.sleep(0.01)
        return i + 1

    async def source() -> None:
        target_future = target(1)
        chain_future(target_future, source_future)
        result = await target_future
        assert result == 2

    io_loop = asyncio.get_event_loop()
    source_future = Future()
    io_loop.run_until_complete(source())
    assert isinstance(source_future.result(), int)
    assert source_future.result() == 2

# Generated at 2022-06-14 11:54:38.596367
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()
    future3 = Future()

    chain_future(futures.Future(), future2)
    assert not future2.done()
    chain_future(future1, futures.Future())
    assert not future2.done()
    chain_future(future1, future2)

    future1.set_result(42)
    assert not future2.done()
    chain_future(future1, future3)
    assert future3.result() == 42
    chain_future(future1, future3)
    assert future3.result() == 42

    future2.set_exception(RuntimeError())
    assert future2.exception() is not None
    assert future2.result() is None

    future1.set_exception(RuntimeError())
    assert future2.done()



# Generated at 2022-06-14 11:54:46.559239
# Unit test for function chain_future
def test_chain_future():
    # This is a little complicated because we want to test the
    # future-compatibility of chain_future.
    io_loop = IOLoop()
    future = Future()
    future2 = Future()
    chain_future(future, future2)
    io_loop.add_callback(future.set_result, 42)
    io_loop.add_callback(future.set_result, 1729)
    io_loop.add_timeout(time.time() + 1, io_loop.stop)
    io_loop.start()
    assert future2.result() == 42

# Generated at 2022-06-14 11:54:58.534870
# Unit test for function chain_future
def test_chain_future():
    import time

    result = object()
    timeout = 3
    future3 = Future()  # type: Future
    start = time.time()

    def callback(future):
        try:
            assert future.result() is result
            assert time.time() - start < timeout
            future3.set_result(None)
        except Exception:
            future3.set_exc_info(sys.exc_info())
            raise

    future1 = Future()
    chain_future(future1, callback)
    future2 = Future()
    chain_future(future2, future1)
    future2.set_result(result)
    return future3


# Wrapper for concurrent.futures.ThreadPoolExecutor.  This is a very
# simple wrapper that turns the synchronous methods of the
# concurrent.futures.ThreadPoolExec

# Generated at 2022-06-14 11:55:14.027178
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.testing import AsyncTestCase, gen_test

    class TestCase(AsyncTestCase):
        def test_chain(self):
            # type: () -> None
            f1 = Future()
            f2 = Future()
            chain_future(f1, f2)
            f1.set_result(42)
            self.assertEqual(f2.result(), 42)

    test = TestCase()
    test.run_sync(gen_test(test.test_chain))

# Generated at 2022-06-14 11:55:21.318038
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    # This function is mainly to generate the typing of the test
    def fn(a: int, b: str) -> float:
        return a + float(b)

    io_loop = IOLoop.current()
    io_loop.make_current()
    with closing(DummyExecutor()) as e:
        f1 = Future()  # type: Future[float]
        f2 = e.submit(fn, 1, "2")  # type: Future[float]
        chain_future(f2, f1)
        io_loop.add_future(f2, lambda _: None)
        assert f1.result() == 3.0
        assert f2.result() == 3.0

# Generated at 2022-06-14 11:55:34.281423
# Unit test for function chain_future
def test_chain_future():
    e = futures.Executor()

    def a():
        return 1

    def b(x: int) -> int:
        return x + 1

    def c(x: int) -> int:
        raise ValueError(x)

    fa = e.submit(a)
    fb = e.submit(b, 1)
    fc = e.submit(c, 2)
    fb_err = e.submit(c, 3)
    fboth = e.submit(b, 2)

    chain_future(fa, fb)
    chain_future(fa, fc)
    chain_future(fb_err, fboth)

    assert fb.result() == 2
    assert fc.exception() and fc.exception().args[0] == 1

# Generated at 2022-06-14 11:55:47.248864
# Unit test for function run_on_executor
def test_run_on_executor():
    from concurrent import futures
    from tornado import gen
    from tornado.escape import native_str
    from tornado.ioloop import IOLoop
    from tornado.testing import AsyncTestCase, gen_test

    class Test(object):
        _thread_pool = futures.ThreadPoolExecutor(1)

        def __init__(self):
            self.executor = futures.ThreadPoolExecutor(1)

        @run_on_executor
        def blocking(self, arg):
            import time
            time.sleep(arg)
            return arg

        @run_on_executor(executor="_thread_pool")
        def blocking2(self, arg):
            import time
            time.sleep(arg)
            return arg


# Generated at 2022-06-14 11:56:00.567490
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    loop = IOLoop()
    gen = None

    def f():
        yield gen.sleep(1)
        if future2.done():
            raise Exception("future2 should not complete until future1 is done")
        raise Exception("did not wait for future1")

    async def async_f():
        await gen.sleep(1)
        if future2.done():
            raise Exception("future2 should not complete until future1 is done")
        raise Exception("did not wait for future1")

    @gen.coroutine
    def check_completion():
        yield gen.sleep(1)
        if not future1.done():
            raise Exception("future1 should be complete")
        if not future2.done():
            raise Exception("future2 should be complete")

# Generated at 2022-06-14 11:56:04.649850
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(42)
    assert f2.result() == 42



# Generated at 2022-06-14 11:56:10.498756
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    a = 1
    b = 2
    executor = DummyExecutor()
    future = executor.submit(lambda x,y: x + y, a, b)
    try:
        r = future.result()
    except:
        r = None
    assert r == 3


# Generated at 2022-06-14 11:56:23.447886
# Unit test for function chain_future
def test_chain_future():
    from tornado.gen import Return
    from tornado.testing import AsyncTestCase, gen_test

    class TestChainFuture(AsyncTestCase):
        @gen_test
        def test_chain(self):
            async_future = Future()
            conc_future = Future()
            chain_future(conc_future, async_future)

            async_future2 = Future()
            chain_future(async_future, async_future2)

            conc_future.set_result(42)
            x = await async_future2
            self.assertEqual(42, x)

            async_future = Future()
            conc_future = Future()
            chain_future(conc_future, async_future)

            async_future2 = Future()
            chain_future(async_future, async_future2)


# Generated at 2022-06-14 11:56:36.549217
# Unit test for function chain_future
def test_chain_future():
    # This test verifies that the future's result is copied from one
    # future to another, unless the second future is already complete or
    # has been cancelled by the time the first one completes.
    #
    # Use a thread pool executor to ensure that
    # ThreadPoolExecutor.submit() works with Futures as well as
    # callables.  (This is just a convenience for the test; generally
    # we expect both sides of a chain_future call to use the same kind
    # of Future.)

    from tornado.concurrent import futures

    executor = futures.ThreadPoolExecutor(1)

    def run():
        f1 = Future()
        executor.submit(lambda: f1)
        assert not f1.done()

        f2 = Future()
        chain_future(f1, f2)

        f1.set

# Generated at 2022-06-14 11:56:41.686755
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    # pylint: disable=invalid-name
    import unittest

    class Test(object):
        executor = dummy_executor

        @run_on_executor
        def foo(self):
            # type: () -> None
            return 42

    test = Test()
    future = test.foo()  # type: Future
    assert future.result() == 42


if __name__ == "__main__":
    test_run_on_executor()

# Generated at 2022-06-14 11:56:52.521810
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()
    future_set_exception_unless_cancelled(f, RuntimeError())
    assert f.exception() is not None  # type: ignore
    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, RuntimeError())
    assert f.cancelled()

# Generated at 2022-06-14 11:57:00.209741
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    import io
    import re
    import unittest
    import warnings

    # @unittest.skipIf(sys.version_info[:2] >= (3, 5),
    #                 "futures does not support this use case")
    class TestFutureSetException(unittest.TestCase):
        def setUp(self):
            self.buf = io.StringIO()
            self.stream = logging.StreamHandler(self.buf)
            app_log.addHandler(self.stream)

        def tearDown(self):
            app_log.removeHandler(self.stream)

        def test_no_exception(self):
            f = Future()
            future_set_exception_unless_cancelled(f, RuntimeError())

            self.assertIn('RuntimeError', str(f.exception()))
           

# Generated at 2022-06-14 11:57:02.896903
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(42)
    assert f2.done()



# Generated at 2022-06-14 11:57:18.156249
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_result(1)
    assert f2.result() == 1
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(KeyError)
    assert_raises(KeyError, f2.result)
    f1 = Future()
    f2 = Future()
    f2.set_result(2)
    chain_future(f1, f2)
    assert f2.result() == 2

if __name__ == "__main__":
    import unittest
    from tornado.testing import AsyncTestCase, gen_test



# Generated at 2022-06-14 11:57:31.212047
# Unit test for function chain_future
def test_chain_future():
    def f(x: int, y: int) -> int:
        return x + y

    f1 = Future()  # type: Future[int]
    f2 = Future()  # type: Future[int]
    chain_future(f1, f2)
    assert f2.done()
    f1.set_result(1)
    assert not f2.done()
    f1.set_result(None)
    assert f2.done()
    f2 = Future()
    f1.set_exception(RuntimeError())
    assert f2.done()

    # test concurrent.futures.Future
    f1 = futures.Future()
    f2 = Future()
    chain_future(f1, f2)
    assert f2.done()
    f1.set_result(1)

# Generated at 2022-06-14 11:57:40.223448
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from tornado.ioloop import IOLoop

    asyncio_loop = asyncio.get_event_loop()
    # Make sure we have an asyncio loop running this time.  Because
    # this test involves concurrent futures, it breaks randomly with
    # 3.7's default ProactorEventLoop.
    if asyncio_loop is None:
        asyncio_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(asyncio_loop)
    io_loop = IOLoop()

# Generated at 2022-06-14 11:57:52.743714
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f1 = Future()
    f2 = Future()

    def finish_f1(arg):
        # type: (Any) -> None
        f1.set_result(arg)

    def finish_f2(arg):
        # type: (Any) -> None
        f2.set_result(arg)

    chain_future(f1, f2)
    f1.add_done_callback(finish_f1)
    f2.add_done_callback(finish_f2)
    assert f1.result() == f2.result()

    # When one future is already completed, the result of the
    # completed future should be copied to the other future.
    f1 = Future()
    f2 = Future()
    f1.set_result("done")
    chain_

# Generated at 2022-06-14 11:58:02.333768
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import logging

    io_loop = IOLoop()

    @coroutine
    def f():
        yield gen.sleep(0.01)
        raise Exception("test")

    class TestChain(unittest.TestCase):
        def setUp(self):
            self.a = Future()
            self.b = Future()
            chain_future(self.a, self.b)

        def test_success(self):
            result = object()
            self.a.set_result(result)
            self.assertTrue(self.b.done())
            self.assertFalse(self.b.cancelled())
            self.assertIs(self.b.result(), result)

        def test_failure(self):
            self.a.set_exception(RuntimeError("test"))

# Generated at 2022-06-14 11:58:08.005634
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()  # type: Future

    exception1 = RuntimeError("first exception")
    exception2 = RuntimeError("second exception")
    future_set_exception_unless_cancelled(f, exception1)
    future_set_exception_unless_cancelled(f, exception2)

    assert f.exception() == exception1

    f2 = Future()
    f2.cancel()
    future_set_exception_unless_cancelled(f2, exception1)
    try:
        f2.exception()
    except asyncio.CancelledError:
        pass

# Generated at 2022-06-14 11:58:18.697213
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest.mock

    @run_on_executor()
    def x(self, a, b, c):
        return a, b, c

    mock1 = unittest.mock.Mock()
    mock2 = unittest.mock.Mock()
    mock3 = unittest.mock.Mock()

    class O:
        executor = dummy_executor

    o = O()
    fut = x(o, mock1, mock2, mock3)
    assert is_future(fut)
    assert [mock1, mock2, mock3] == fut.result()
    assert not mock1.called
    assert not mock2.called
    assert not mock3.called

# Generated at 2022-06-14 11:58:37.433120
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import concurrent
    import threading
    from tornado.ioloop import IOLoop

    def try_future():
        import sys
        from tornado import platform
        try:
            from asyncio import Future
        except ImportError:
            pass
        else:
            # platform.asyncio indicates that asyncio is usable
            # (python 3.4+ with the asyncio backport or python 3.5+)
            if not platform.asyncio:
                Future = None
        if Future is not None:
            class Future(Future):
                @classmethod
                def __subclasshook__(cls, C):
                    if (issubclass(C, concurrent.futures.Future) and not
                            issubclass(C, Future)):
                        return True
                    return NotImplemented
            # Replace the module

# Generated at 2022-06-14 11:58:43.920892
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    test_future = Future()
    test_exception = Exception()
    future_set_exception_unless_cancelled(test_future, test_exception)
    assert test_future.exception() == test_exception
    test_future.cancel()
    future_set_exception_unless_cancelled(test_future, test_exception)

# Generated at 2022-06-14 11:58:51.624706
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest

    class Test(unittest.TestCase):
        def setUp(self):
            self.executor = futures.ThreadPoolExecutor(10)

        @run_on_executor
        def blocking_method(self, x):
            return x + 1

        async def test_run_on_executor(self):
            self.assertEqual(2, await self.blocking_method(1))

    unittest.main()

# Generated at 2022-06-14 11:58:58.753876
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.ioloop import IOLoop
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.testing import AsyncTestCase, bind_unused_port, gen_test

    # Use AsyncIOMainLoop so the loop is created with asyncio
    # Future instead of tornado Future for this test.
    class TestFutureSetExceptionUnlessCancelled(AsyncTestCase):
        def setUp(self):
            super().setUp()
            # We use a different IOLoop to test future_set_exception_unless_cancelled
            # because this test case stops the loop and the main test IOLoop may
            # be used by other tests.
            s = bind_unused_port()[1]
            self.io_loop = IOLoop(make_current=False)
            self.addClean

# Generated at 2022-06-14 11:59:08.713665
# Unit test for function chain_future
def test_chain_future():
    future1 = Future()
    future2 = Future()

    def callback(future):
        future3.set_result(future.result() + 1)

    chain_future(future1, future2)
    future2.add_done_callback(callback)
    future3 = Future()
    chain_future(future2, future3)

    future1.set_result(1)
    io_loop.run_sync(lambda: future_result(future3))
    assert 2 == future3.result()

# Generated at 2022-06-14 11:59:21.394021
# Unit test for function run_on_executor
def test_run_on_executor():
    import unittest
    import tornado.escape
    import tornado.ioloop

    class FakeExecutor:
        executor = None

        def __init__(self, io_loop: "tornado.ioloop.IOLoop") -> None:
            self.io_loop = io_loop
            self.executor = None  # type: Optional[tornado.platform.asyncio.BaseAsyncIOMainLoop]

        def submit(self, fn: Callable[..., _T], *args: Any, **kwargs: Any) -> Any:
            future = tornado.concurrent.Future()
            self.io_loop.add_callback(
                lambda: future.set_result(fn(*args, **kwargs))
            )
            return future


# Generated at 2022-06-14 11:59:24.189229
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    f = Future()
    future_set_result_unless_cancelled(f, None)
    f.cancel()



# Generated at 2022-06-14 11:59:26.770800
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    executor = DummyExecutor()
    future = executor.submit(lambda: 5)
    assert future.result() == 5


# Generated at 2022-06-14 11:59:39.807833
# Unit test for function chain_future
def test_chain_future():
    foo_callbacks = []  # type: list
    foo_results = []  # type: list

    def foo_done(foo):
        foo_callbacks.append(foo)
        foo_results.append(foo.result())

    bar_callbacks = []  # type: list
    bar_results = []  # type: list

    def bar_done(bar):
        bar_callbacks.append(bar)
        bar_results.append(bar.result())

    loop = asyncio.get_event_loop()
    foo = Future()
    bar = Future()

    # Make sure foo is done before we attach callbacks
    loop.call_soon(foo.set_result, "foo")
    foo.add_done_callback(foo_done)

    chain_future(foo, bar)
    bar.add_done

# Generated at 2022-06-14 11:59:44.972215
# Unit test for function chain_future
def test_chain_future():
    from tornado.platform.asyncio import to_asyncio_future

    def f(result):
        return result * 2

    @to_asyncio_future
    def g(result):
        return result * 3

    t = Future()
    u = g(t)
    chain_future(t, u)

    t.set_result(10)

    assert u.result() == 60

