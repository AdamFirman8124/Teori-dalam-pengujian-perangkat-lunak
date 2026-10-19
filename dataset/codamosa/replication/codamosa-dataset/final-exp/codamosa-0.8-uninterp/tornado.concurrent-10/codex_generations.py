

# Generated at 2022-06-14 11:50:20.825735
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    assert not f2.done()
    f1.set_result(42)
    assert f2.done()
    assert f2.result() == 42
    f3 = Future()
    chain_future(f1, f3)
    assert f3.done()
    assert f3.result() == 42
    chain_future(f3, f3)
    assert f3.result() == 42
    # error cases
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.set_exception(ZeroDivisionError())
    assert f2.done()
    assert isinstance(f2.exception(), ZeroDivisionError)



# Generated at 2022-06-14 11:50:30.545171
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test
    from tornado.ioloop import IOLoop

    io_loop = IOLoop()

    @gen_test
    def test_chain_future():
        output = []

        @gen.coroutine
        def test_subgen():
            output.append(1)
            yield gen.moment
            output.append(2)

        @gen.coroutine
        def test_main():
            f = Future()  # type: Future[int]
            chain_future(test_subgen(), f)
            output.append(0)
            yield f
            output.append(3)

        io_loop.run_sync(test_main)
        assert output == [0, 1, 2, 3]



# Generated at 2022-06-14 11:50:37.520120
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()

    def fail_f2():
        f2.set_exception(ValueError())

    chain_future(f1, f2)
    f1.add_done_callback(fail_f2)
    f1.set_result(None)
    try:
        f2.result()
    except ValueError:
        pass
    else:
        assert False, 'ValueError should have been raised'



# Generated at 2022-06-14 11:50:43.074235
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    def callback():
        return 1

    try:
        raise ValueError

    except ValueError:
        exc_info = sys.exc_info()

    future = Future()
    future_set_exception_unless_cancelled(future, exc_info[1])
    future_add_done_callback(future, callback)

# Generated at 2022-06-14 11:50:50.810952
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()
    a.set_result(1)
    assert b.done()
    assert b.result() == 1
    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()
    a.set_exception(ValueError())
    assert b.done()
    try:
        b.result()
        assert False
    except ValueError:
        pass



# Generated at 2022-06-14 11:50:52.320742
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f1.result()
    assert f2.done()



# Generated at 2022-06-14 11:51:00.974089
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, ValueError("test exception"))
    assert future.exception() is not None
    assert isinstance(future.exception(), ValueError)
    assert future.cancelled() is False

    future = Future()
    future.cancel()
    new_future = Future()
    future_set_exception_unless_cancelled(new_future, ValueError("test exception"))
    assert new_future.exception() is None
    assert new_future.cancelled() is True



# Generated at 2022-06-14 11:51:10.715992
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    from concurrent import futures

    def f(future):
        future.set_result(1)
        return 1

    for f1_cls in [Future, futures.Future]:
        for f2_cls in [Future, futures.Future]:
            f1 = f1_cls()  # type: Union[Future,futures.Future]
            f2 = f2_cls()  # type: Union[Future,futures.Future]
            chain_future(f1, f2)
            f(f1)
            assert f2.result() == 1



# Generated at 2022-06-14 11:51:16.469551
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing

    future1 = futures.Future()
    future2 = futures.Future()
    future3 = Future()
    future4 = Future()
    chain_future(future1, future2)
    chain_future(future3, future4)
    future1.set_result(42)
    future3.set_result(84)
    assert future1.result() == 42
    assert future2.result() == 42
    assert future3.result() == 84
    assert future4.result() == 84

# Generated at 2022-06-14 11:51:23.902542
# Unit test for function future_set_result_unless_cancelled
def test_future_set_result_unless_cancelled():
    # type: () -> None
    future = Future()
    future.cancel()
    future_set_result_unless_cancelled(future, "value")
    assert future.cancelled()
    assert not future.done()

    future = Future()
    future_set_result_unless_cancelled(future, "value")
    assert not future.cancelled()
    assert future.done()

# Generated at 2022-06-14 11:51:31.653210
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop.current()
    io_loop.run_sync(functools.partial(_test_chain_future, io_loop))
    io_loop.run_sync(functools.partial(_test_chain_future, io_loop))



# Generated at 2022-06-14 11:51:38.927871
# Unit test for function chain_future
def test_chain_future():
    import time
    import unittest
    from tornado.gen import coroutine

    io_loop = get_running_loop()

    @coroutine
    def wait(arg):
        if isinstance(arg, futures.Future):
            # concurrent.futures.Future
            yield asyncio.wrap_future(arg)
        else:
            yield arg

    def sleep(t):
        time.sleep(t)
        return 5

    # Callbacks added before the result is available are still run.
    @coroutine
    def test_chain_before(future, expected):
        a = Future()
        b = Future()
        chain_future(a, b)
        result = yield [wait(a), wait(b)]
        future.set_result((result[0], result[1]))

# Generated at 2022-06-14 11:51:43.696032
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    from concurrent.futures import Future as ConcFuture
    from tornado.concurrent import Future as AsyncFuture
    import tornado.gen

    class FakeExecutor(object):
        def __init__(self):
            # type: () -> None
            self.submitted = []  # type: List[Tuple[Callable, Any, Any]]
            self.new_future = AsyncFuture

        def submit(
            self, fn, *args, **kwargs
        ):  # type: (Callable, *Any, **Any) -> Union[ConcFuture, Future]
            self.submitted.append((fn, args, kwargs))
            f = self.new_future()
            f.set_result((fn, args, kwargs))
            return f


# Generated at 2022-06-14 11:51:53.778800
# Unit test for function run_on_executor
def test_run_on_executor():
    import concurrent.futures
    import threading
    import time

    executor = concurrent.futures.ThreadPoolExecutor(1)
    io_loop = None
    future = None

    class A:
        def __init__(self) -> None:
            self.executor = executor

        @run_on_executor
        def f(self, arg) -> None:
            nonlocal io_loop, future
            io_loop = self.io_loop
            future = self.future

        @run_on_executor(executor="executor")
        def g(self, arg) -> None:
            pass

    a = A()
    # This is a little confusing, because @run_on_executor is a decorator
    # for class methods and this test calls it on an instance. So the
    # "

# Generated at 2022-06-14 11:52:00.879754
# Unit test for function chain_future
def test_chain_future():
    def copy(future):
        assert future is a
        if not b.done():
            b.set_result(future.result())

    a = Future()
    b = Future()
    chain_future(a, b)
    a.set_result(42)
    b.result()
    a = Future()
    b = Future()
    a.set_result(42)
    chain_future(a, b)
    b.result()
    a = Future()
    b = Future()
    a.set_exception(RuntimeError())
    chain_future(a, b)
    try:
        b.result()
        assert False
    except RuntimeError:
        pass


if typing.TYPE_CHECKING:
    _OldFuture = typing.TypeVar("_OldFuture", futures.Future, Future)

    #

# Generated at 2022-06-14 11:52:07.695578
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    f = Future()
    f.set_result(2)
    g = Future()
    chain_future(f, g)
    assert g.result() == 2

    f = Future()
    f.set_exception(ZeroDivisionError())
    g = Future()
    chain_future(f, g)
    assert g.exception() is not None

    # Keyword arguments are preserved (note
    # that the real use case for this is in
    # the @return_future decorator)
    f = Future()
    g = Future()
    chain_future(f, g)
    f.set_result(kw="test")
    assert g.result(kw="test") == "test"

    # If f is already done, the result is preserved
    f = Future()
    f

# Generated at 2022-06-14 11:52:18.167117
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test

    from tornado.httpclient import AsyncHTTPClient

    http_client = AsyncHTTPClient()

    @gen_test
    def fetch(url):
        res = yield http_client.fetch(url)
        raise gen.Return(res)

    @gen_test
    def main():
        # Using a future
        future1 = Future()  # type: Future[Any]
        chain_future(fetch("http://www.google.com"), future1)
        res = yield future1

        # Using a concurrent.futures.Future
        future2 = futures.Future()  # type: futures.Future[Any]
        chain_future(fetch("http://www.google.com"), future2)
        res = yield future2


# For backwards compatibility with previous versions of Tornado
AsyncResult

# Generated at 2022-06-14 11:52:20.850158
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    dummy_executor.submit(lambda x: x + 1, 1)

# Generated at 2022-06-14 11:52:24.529234
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    def add(a: int, b: int) -> int:
        return a + b

    assert dummy_executor.submit(add, 1, 2).result() == 3


# Generated at 2022-06-14 11:52:32.319489
# Unit test for function chain_future
def test_chain_future():
    import tornado.testing

    def f():
        raise tornado.testing.gen_test(Exception("foobar"))

    io_loop = tornado.testing.AsyncTestCase().io_loop
    future1 = io_loop.run_in_executor(None, f)
    future2 = Future()
    chain_future(future1, future2)
    future2.add_done_callback(lambda future: io_loop.stop())
    io_loop.start()
    assert isinstance(future2.exception(), Exception)

# Generated at 2022-06-14 11:52:48.824315
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    loop = IOLoop.current()

    def f():
        raise RuntimeError()

    a = Future()
    b = Future()

    chain_future(a, b)
    # a failing future should not fail b
    loop.run_sync(lambda: a.set_exception(RuntimeError()))
    assert b.exception() is None

    a = Future()
    b = Future()
    chain_future(a, b)
    # a cancelled future should not affect b
    loop.run_sync(a.cancel)
    assert not b.cancelled()
    loop.run_sync(lambda: a.set_result(True))
    assert b.result() is True

    a = Future()
    b = Future()
    c = Future()
    chain_future

# Generated at 2022-06-14 11:52:55.624048
# Unit test for function chain_future
def test_chain_future():

    def cb_test(future: "Future[int]") -> None:
        assert future.result() == 1
        future.set_result(future.result() + 1)

    loop = asyncio.get_event_loop()
    a = asyncio.Future()  # type: Future[int]
    b = asyncio.Future()  # type: Future[int]
    chain_future(a, b)
    future_add_done_callback(b, cb_test)
    a.set_result(1)
    loop.run_until_complete(b)
    assert b.result() == 2


# Generated at 2022-06-14 11:53:07.514835
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)

    a_result = object()
    a.set_result(a_result)
    assert a.result() is a_result
    assert b.result() is a_result

    a = Future()
    b = Future()
    chain_future(a, b)

    b.cancel()
    a.set_result(object())
    assert b.cancelled()

    a = Future()
    b = Future()
    chain_future(a, b)

    a_exception = RuntimeError("test")
    a.set_exception(a_exception)
    assert a.exception() is a_exception
    assert b.exception() is a_exception
    assert b.exception().__traceback__

   

# Generated at 2022-06-14 11:53:14.931873
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    import time

    def future_set_result_unless_cancelled(future, value):
        assert future is a
        if not b.cancelled():
            b.set_result(value)

    def future_set_exc_info(future, exc_info):  # type: ignore
        assert future is a
        if exc_info[1] is None:
            raise Exception("future_set_exc_info called with no exception")
        future_set_exception_unless_cancelled(b, exc_info[1])

    def future_add_done_callback(future, callback):
        if future.done():
            callback(future)
        else:
            future.add_done_callback(callback)

    a = Future()
    b = Future()

# Generated at 2022-06-14 11:53:23.415816
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase

    async def async_foo():
        await asyncio.sleep(0)
        return 1

    @gen_test
    def gen_foo():
        yield gen.moment
        return 2

    @gen_test
    def test_chain_future(self):
        a = async_foo()
        b = self.future()
        c = gen_foo()
        d = self.future()
        chain_future(a, b)
        chain_future(c, d)
        self.assertEqual(1, await b)
        self.assertEqual(2, await d)



# Generated at 2022-06-14 11:53:35.681196
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import AsyncTestCase, gen_test, main

    class ChainFutureTest(AsyncTestCase):
        def test_chain(self):
            future1 = Future()
            future2 = Future()
            chain_future(future1, future2)
            future1.set_result(42)
            self.assertEqual(future2.result(), 42)

        @gen_test
        def test_chain_first(self):
            future1 = Future()
            future2 = Future()
            chain_future(future1, future2)
            future2.set_result(42)
            self.assertEqual(future1.result(), 42)

        @gen_test
        def test_chain_exc(self):
            future1 = Future()
            future2 = Future()

# Generated at 2022-06-14 11:53:39.008628
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.cancel()
    try:
        future_set_exception_unless_cancelled(future, ValueError())
    except InvalidStateError:
        pass
    else:
        raise Exception("Expected InvalidStateError")

# Generated at 2022-06-14 11:53:52.707084
# Unit test for function chain_future
def test_chain_future():
    import random

    def test(executor: futures.Executor, n: int) -> None:
        @run_on_executor(executor=executor)
        def f(x: int) -> int:
            return x

        check_future(f(n))

    def check_future(future: Future[int]) -> None:
        chained_resolved, n = False, random.randrange(100000)
        future.add_done_callback(lambda f: f.result())

        def future_callback(f: Future[int]) -> None:
            nonlocal chained_resolved, n
            assert future.done()
            assert not f.done()
            assert f is not future
            assert n not in (f.result(), f.exception())
            assert not chained_resolved

# Generated at 2022-06-14 11:53:58.284587
# Unit test for function chain_future
def test_chain_future():
    io_loop = IOLoop.current()
    io_loop.make_current()
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)
    f2.add_done_callback(lambda f: io_loop.stop())
    f1.set_result(None)
    io_loop.start()
    assert f2.done()
    assert f2.result() is None



# Generated at 2022-06-14 11:54:03.233387
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    exc = RuntimeError("Foobar")
    future = Future()
    future_set_exception_unless_cancelled(future, exc)
    assert future.exception() == exc
    future_set_exception_unless_cancelled(future, RuntimeError("Other"))
    assert future.exception() == exc

# Generated at 2022-06-14 11:54:16.965257
# Unit test for function chain_future
def test_chain_future():
    import unittest
    import functools

    class TestChainFuture(unittest.TestCase):
        def test_exception(self):
            fut1 = Future()
            fut2 = Future()

            chain_future(fut1, fut2)
            self.assertFalse(fut2.done())

            e = Exception()
            fut1.set_exception(e)
            self.assertTrue(fut2.done())
            self.assertIs(fut2.exception(), e)
            self.assertIs(type(fut2.exception()), type(e))

        def test_future_concurrent_futures(self):
            loop = IOLoop.current()
            executor = futures.ThreadPoolExecutor(1)

            fut1 = Future()
            fut2 = futures.Future()

# Generated at 2022-06-14 11:54:27.822870
# Unit test for function run_on_executor
def test_run_on_executor():  # pragma: no cover
    import logging
    import time

    logging.getLogger().setLevel(logging.DEBUG)

    class MyClass:
        executor = dummy_executor

    @run_on_executor
    def foo(self, a, b, callback=None):
        time.sleep(0.01)
        logging.debug("executor: %s %s %s %s", self, a, b, callback)
        callback([self, a, b, callback])

    @run_on_executor(executor="_thread_pool")
    def foo_with_kwargs(self, a, b, callback=None):
        time.sleep(0.01)
        logging.debug("executor: %s %s %s %s", self, a, b, callback)

# Generated at 2022-06-14 11:54:34.869221
# Unit test for function chain_future
def test_chain_future():  # pragma: no cover
    import tornado.testing

    io_loop = tornado.ioloop.IOLoop.current()


    def f():
        return io_loop.add_future(Future(), lambda f: f.result() + 1)


    def callback(future):
        io_loop.stop()


    future = f()
    future.add_done_callback(callback)
    io_loop.start()
    future.result()

# Generated at 2022-06-14 11:54:43.929836
# Unit test for function chain_future
def test_chain_future():
    import types
    import tornado.testing

    # Test concurrent.futures.Future
    def func1(x, y):
        return x * y

    def func2(x, y):
        return x / y

    @tornado.testing.gen_test
    def test_concurrent_futures_future():
        with futures.ThreadPoolExecutor(1) as executor:
            fut1 = executor.submit(func1, 7, 6)
            fut2 = Future()
            chain_future(fut1, fut2)
            result = yield fut2
            self.assertEqual(42, result)

            fut3 = executor.submit(func2, 42, 0)
            fut4 = Future()
            chain_future(fut3, fut4)

# Generated at 2022-06-14 11:54:56.373304
# Unit test for function chain_future
def test_chain_future():
    from tornado.ioloop import IOLoop

    @run_on_executor
    def f1(arg):
        return arg + 1

    @run_on_executor
    def f2(arg):
        return arg + 1

    @run_on_executor
    def f3(arg):
        return arg + 1

    @run_on_executor
    def f4(arg):
        return arg + 1

    @run_on_executor
    def f5(arg):
        return arg + 1

    @run_on_executor
    def f6(arg):
        return arg + 1

    @run_on_executor
    def f7(arg):
        return arg + 1

    @run_on_executor
    def f8(arg):
        return arg + 1


# Generated at 2022-06-14 11:55:04.291070
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
    import time
    import tornado
    from tornado.platform.asyncio import to_tornado_future
    from aiohttp import ClientSession
    from tornado.ioloop import IOLoop
    from tornado.concurrent import run_on_executor
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    dummy = DummyExecutor()
    ioloop = IOLoop.current()
    def test_sleep(self):
        time.sleep(1)
        return 12
    @run_on_executor(executor=dummy)
    async def test_sleep_async(self):
        return test_sleep(self)
    
    @tornado.gen.coroutine
    def sleep_async():
        t = yield test_sleep_async(self)


# Generated at 2022-06-14 11:55:11.580129
# Unit test for function chain_future
def test_chain_future():
    def get_future():
        # type: () -> Future[object]
        f = Future()
        f.set_result(object())
        return f

    f1 = get_future()
    f2 = Future()
    chain_future(f1, f2)
    assert f2.done()
    assert f2.result() is not None


__test__ = {
    "test_chain_future": test_chain_future,
}

# Generated at 2022-06-14 11:55:20.418514
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from concurrent.futures import Future
    from tornado.log import LogFormatter
    import logging

    class _MockLogHandler(logging.Handler):
        def __init__(self) -> None:
            logging.Handler.__init__(self)
            self.last_record = None

        def handle(self, record: logging.LogRecord) -> None:
            self.last_record = record


# Generated at 2022-06-14 11:55:30.959008
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    # This test doesn't require a running IOLoop, so it is safe to run
    # in parallel with the other tests.
    import unittest

    asyncio = pytest.importorskip("asyncio")  # type: ignore
    concurrent_future = pytest.importorskip("concurrent.futures").Future
    import time

    def f():
        # type: () -> None
        raise Exception("foo")

    f2 = lambda x: x * 2

    class FutureTest(unittest.TestCase):
        def test_chain_future(self):
            # type: () -> None
            f1 = Future()
            f2 = Future()
            chain_future(f1, f2)
            f1.set_result(42)

# Generated at 2022-06-14 11:55:37.994133
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future_set_exception_unless_cancelled(future, Exception())
    assert not future.cancelled()
    assert future.exception() is not None
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception())
    assert future.cancelled()
    assert future.exception() is None



# Generated at 2022-06-14 11:56:08.170879
# Unit test for function chain_future
def test_chain_future():
    from tornado.testing import gen_test, AsyncTestCase
    from tornado.platform.asyncio import to_tornado_future

    class TestChainFuture(AsyncTestCase):
        def setUp(self):
            self.concurrent_future = futures.Future()
            self.asyncio_future = Future()
            chain_future(self.concurrent_future, self.asyncio_future)
            super().setUp()

        def assert_future_done(self, future):
            self.assertTrue(future.done())
            self.assertRaises(
                futures.InvalidStateError, future.result
            )  # type: ignore

        def conc_future_complete(self, result_or_exc):
            self.concurrent_future.set_result(result_or_exc)


# Generated at 2022-06-14 11:56:16.403043
# Unit test for function chain_future
def test_chain_future():
    import nose

    future1 = Future()
    future2 = Future()
    chain_future(future1, future2)
    future1.set_result(42)
    nose.tools.assert_is(future2.result(0), 42)

    future3 = Future()
    future4 = Future()
    chain_future(future3, future4)
    future3.set_exception(ValueError())
    with nose.tools.assert_raises(ValueError):
        future4.result(0)

# Generated at 2022-06-14 11:56:26.837944
# Unit test for function chain_future
def test_chain_future():
    import threading
    import unittest
    import warnings

    from tornado import gen
    from tornado import ioloop
    import concurrent.futures

    ioloop.IOLoop.clear_current()

    executor = concurrent.futures.ThreadPoolExecutor(1)

    @gen.coroutine
    def target():
        yield gen.moment

    class TestCase(unittest.TestCase):
        def setUp(self):
            super(TestCase, self).setUp()
            self.io_loop = ioloop.IOLoop()
            self.io_loop.make_current()

        def tearDown(self):
            self.io_loop.clear_current()
            self.io_loop.close(all_fds=True)
            super(TestCase, self).tearDown()



# Generated at 2022-06-14 11:56:34.932765
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    from tornado.ioloop import IOLoop

    async_future = Future()
    concurrent_future = futures.Future()
    for future in (async_future, concurrent_future):
        future_set_exception_unless_cancelled(future, ZeroDivisionError())
        assert future.exception() is not None
        future.cancel()
        future_set_exception_unless_cancelled(future, ZeroDivisionError())
    IOLoop.current().run_sync(async_future)



# Generated at 2022-06-14 11:56:43.162018
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    chain_future(f1, f2)

    assert not f1.done()
    assert not f2.done()

    f1.set_result(1234)

    assert f1.done()
    assert f2.result() == 1234

    f3 = Future()
    f4 = Future()
    chain_future(f3, f4)

    assert not f3.done()
    assert not f4.done()

    try:
        1 / 0
    except ZeroDivisionError:
        exc_info = sys.exc_info()

    f3.set_exc_info(exc_info)

    assert f3.done()
    assert f3.exception() is exc_info[1]
    assert f4.exception() is exc_info

# Generated at 2022-06-14 11:56:51.505084
# Unit test for function run_on_executor
def test_run_on_executor():
    import time
    import tornado.ioloop

    class Foo(object):
        executor = dummy_executor

        @run_on_executor
        def bar(self):
            time.sleep(0.001)
            return 42

    ioloop = tornado.ioloop.IOLoop()
    f = Foo()
    res = []
    f.bar().add_done_callback(res.append)
    ioloop.add_future(f.bar(), res.append)
    ioloop.add_future(f.bar(), lambda f: res.append(f.result()))
    ioloop.add_callback(lambda: res.append(ioloop.run_in_executor(None, f.bar)))
    ioloop.add_callback(lambda: ioloop.stop())
    ioloop.start

# Generated at 2022-06-14 11:56:59.749458
# Unit test for function chain_future
def test_chain_future():
    # type: () -> None
    pass
    # f = Future()
    # g = Future()
    # chain_future(f, g)
    # assert not g.done()
    # f.set_result(42)
    # assert g.result() == 42
    # g.cancel()
    # f.set_result(1729)
    # assert g.result() == 42

    # f = Future()
    # g = Future()
    # chain_future(f, g)
    # assert not g.done()
    # f.set_exception(RuntimeError())
    # assert g.exception() is not None
    # assert isinstance(g.exception(), RuntimeError)

    # f = Future()
    # g = Future()
    # chain_future(f, g)
    # assert not

# Generated at 2022-06-14 11:57:01.188795
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, Exception("err"))

# Generated at 2022-06-14 11:57:09.385754
# Unit test for function chain_future
def test_chain_future():
    from concurrent.futures import Future as CFuture
    import asyncio

    success = object()
    failure = Exception()

    def do_test(first, second):
        # type: (Union[futures.Future[Any], Future[Any]], Union[futures.Future[Any], Future[Any]]) -> None
        first.result = success
        first.set_result(None)
        assert second.result() is success
        assert not second.exception()

        first.set_exception(failure)
        assert second.exception() is failure
        try:
            second.result()
            assert False
        except Exception as e:
            assert e is failure

    for f in CFuture, Future:
        do_test(f(), f())
        loop = asyncio.new_event_loop()
        do_

# Generated at 2022-06-14 11:57:19.716475
# Unit test for function chain_future
def test_chain_future():
    @run_on_executor
    def f():
        return 3

    done_callback = None

    def done_callback_canceller(callback):
        def check(future):
            if not future.cancelled():
                callback(future)

        return check

    import functools

    async def async_test():
        future = f()
        wrapped_future = Future()
        chain_future(future, wrapped_future)
        try:
            # this will throw if the inner future is cancelled
            # when it is completed
            x = await wrapped_future
        except asyncio.CancelledError:
            # since this is a mocked future, the current implementation of
            # chain_future will never cancel it, so we can remove this
            # exception in the future
            raise Exception("inner future should never be cancelled")
        assert x

# Generated at 2022-06-14 11:57:49.381513
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    # should not raise InvalidStateError
    future = asyncio.Future()
    future_set_exception_unless_cancelled(future, RuntimeError)

    # should not log anything
    future_set_exception_unless_cancelled(future, RuntimeError)

# Generated at 2022-06-14 11:57:53.001353
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    f = Future()

    f.set_exception(Exception())
    assert f.exception() is not None

    f = Future()
    f.cancel()
    future_set_exception_unless_cancelled(f, Exception())
    assert f.exception() is None

# Generated at 2022-06-14 11:58:03.677184
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    loop = asyncio.get_event_loop()

    def check_future(
        future: Future[None], expected_exception: Optional[BaseException]
    ) -> None:
        assert future.done()
        if expected_exception is None:
            future.result()
        else:
            with pytest.raises(type(expected_exception)) as e:
                future.result()
            assert e.value is expected_exception

    def set_future(future: Future[None], exception: BaseException) -> None:
        future_set_exception_unless_cancelled(future, exception)

    future = Future()
    test_exception = RuntimeError()

# Generated at 2022-06-14 11:58:09.660715
# Unit test for function chain_future
def test_chain_future():
    f1 = Future()
    f2 = Future()
    f3 = Future()
    f4 = Future()
    chain_future(f1, f2)
    assert f2.done()
    assert not f2.result()
    chain_future(f1, f3)
    assert f3.done()
    assert not f3.result()
    f1.set_result(True)
    assert f2.done()
    assert f2.result()
    assert f3.done()
    assert f3.result()

    f1 = Future()
    f1.set_exception(ZeroDivisionError())
    with pytest.raises(ZeroDivisionError):
        f1.result()
    chain_future(f1, f4)

# Generated at 2022-06-14 11:58:15.960058
# Unit test for function chain_future
def test_chain_future():

    def f(sleep):
        # type: (float) -> "Future[int]"
        f = Future()
        asyncio.get_event_loop().call_later(sleep, f.set_result, 42)
        return f

    def g(sleep):
        # type: (float) -> "Future[int]"
        f = Future()
        asyncio.get_event_loop().call_later(sleep, f.set_result, 24)
        return f

    f2 = Future()
    chain_future(f(0.01), f2)
    f2.result()  # 42

    f2 = Future()
    chain_future(f(0.01), f2)
    f2.result()  # 42

    f2 = Future()
    chain_future(g(0.01), f2)
   

# Generated at 2022-06-14 11:58:23.801173
# Unit test for function chain_future
def test_chain_future():

    class Future(object):
        def __init__(self, loop):
            self.loop = loop
            self.callbacks = []  # type: list[Callable[["Future"], None]]
            self._done = False
            self._result = None

        def add_done_callback(self, callback: Callable[["Future"], None]) -> None:
            self.callbacks.append(callback)

        def set_result(self, result: Any) -> None:
            assert not self._done
            self.loop.add_callback(self._set_result, result)

        def _set_result(self, result: Any) -> None:
            assert not self._done
            self._result = result
            for callback in self.callbacks:
                callback(self)
            self._done = True


# Generated at 2022-06-14 11:58:29.450675
# Unit test for function future_set_exception_unless_cancelled
def test_future_set_exception_unless_cancelled():
    future = Future()
    exception = Exception()
    future_set_exception_unless_cancelled(future, exception)
    assert future.exception() == exception

    future = Future()
    future.cancel()
    future_set_exception_unless_cancelled(future, exception)
    assert future.exception() is None

# Generated at 2022-06-14 11:58:39.293149
# Unit test for function chain_future
def test_chain_future():
    class ErrorZeroDivision(Exception):
        pass

    async def get_future(value):
        future = Future()
        future.set_result(value)
        return future

    def _func(value):
        if value == 0:
            raise ErrorZeroDivision()
        return value

    @asyncio.coroutine
    def func(value):
        yield from asyncio.sleep(0.1)
        return _func(value)

    def func_callback(future):
        future.set_result(_func(future.result()))

    def func_errback(future):
        e = future.exception()
        future.set_exception(e)

    async def test_await_future():
        future = Future()
        future_add_done_callback(future, func_callback)
        future_add_

# Generated at 2022-06-14 11:58:44.118356
# Unit test for function chain_future
def test_chain_future():
    a = Future()
    b = Future()
    chain_future(a, b)
    assert not b.done()
    a.set_result("foo")
    assert b.done()
    assert b.result() == "foo"



# Generated at 2022-06-14 11:58:50.441040
# Unit test for method submit of class DummyExecutor
def test_DummyExecutor_submit():
  import time
  def test_func(x, y):
    time.sleep(1)
    return (x+y, x-y)
  dummy_executor = DummyExecutor()
  future = dummy_executor.submit(test_func, 1, 2)
  assert future.result() == (3, -1)

# Generated at 2022-06-14 11:59:48.761815
# Unit test for function run_on_executor
def test_run_on_executor():
    # type: () -> None
    class TestClass(object):
        def __init__(self, executor):
            # type: (futures.Executor) -> None
            self.executor = executor

        @run_on_executor
        def blk(self, arg, kwarg=None):
            # type: (float, Optional[float]) -> float
            return arg * kwarg

        @gen.coroutine
        def test_executor(self, arg, kwarg):
            # type: (float, float) -> float
            result = yield self.blk(arg, kwarg=kwarg)
            raise gen.Return(result)

    exec_ = futures.ThreadPoolExecutor(10)
    test = TestClass(exec_)

# Generated at 2022-06-14 11:59:57.409246
# Unit test for function chain_future
def test_chain_future():
    import unittest
    from tornado.platform.asyncio import AsyncIOMainLoop
    from tornado.testing import AsyncTestCase, gen_test

    AsyncIOMainLoop().install()

    class ChainFutureTest(AsyncTestCase):
        @gen_test
        def test_chain_future(self):
            f = Future()
            g = Future()
            chain_future(f, g)
            f.set_result(42)

# Generated at 2022-06-14 12:00:05.765651
# Unit test for function chain_future
def test_chain_future():
    import tornado.gen

    # Ensure that base Future and AsyncIO Future can be used interchangeably
    a = tornado.gen.Future()
    b = asyncio.Future()
    c = tornado.gen.Future()
    chain_future(a, b)
    assert not b.done()
    a.set_result(42)
    assert b.result() == 42
    chain_future(a, c)
    assert c.result() == 42
    a.set_result(1729)
    assert c.result() == 42
    return b, c